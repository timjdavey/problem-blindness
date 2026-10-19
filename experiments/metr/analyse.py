# /// script
# requires-python = ">=3.11"
# dependencies = ["pandas", "numpy", "statsmodels", "scikit-learn", "krippendorff"]
# ///
"""Test which axes predict agent failure on METR's tasks once length is controlled for.

Steps, each written to results.md:
  0. Baseline: reproduce METR's 50% time horizons from the public runs alone.
  1. Reliability: Krippendorff's alpha per axis across the tagging passes.
  2. Tagger check: does our tagging of METR's 16 factors reproduce their slope?
  3. One axis at a time: residual success on each axis, clustered by family.
  4. All together: lasso with stability selection, giving the shortlist.
  5. Added value: do the axes predict better than METR's messiness sum, out of sample?
  6. Shuffle test: does the real tagging beat tags shuffled across families?

Run with no tags.csv and only step 0 runs.
"""

import argparse
import json
from pathlib import Path

import krippendorff
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import ElasticNetCV, Ridge, lasso_path
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.multitest import multipletests

HERE = Path(__file__).parent
DATA = HERE / "data"

# The models in METR's March 2025 paper, as aliased in runs-1.0.jsonl.
PAPER_MODELS = [
    "davinci-002 (GPT-3)", "gpt-3.5-turbo-instruct", "GPT-4 0314", "GPT-4 1106", "GPT-4 0125",
    "GPT-4 Turbo", "GPT-4o", "Claude 3 Opus", "Claude 3.5 Sonnet (Old)", "Claude 3.5 Sonnet (New)",
    "Claude 3.7 Sonnet", "o1-preview", "o1",
]
METR_SLOPE = -0.081  # change in mean success per messiness point, controlling for log length
MIN_ALPHA = 0.4      # below this an axis tag can't be reproduced, so it is dropped
MIN_SD = 0.1         # below this an axis barely varies here, so it is untested
MAX_NA = 0.5         # above this the taggers found nothing to grip on, so it is untested
SHORTLIST_SHARE = 0.8  # an axis must survive in this share of half samples
STABILITY_Q = 8        # axes kept per half sample


def load_runs(version: str) -> pd.DataFrame:
    runs = pd.read_json(DATA / f"runs-{version}.jsonl", lines=True)
    runs = runs[(runs.task_source != "SWAA") & (runs.alias != "human")]
    return runs.assign(log2_minutes=np.log2(runs.human_minutes))


# Step 0 ---------------------------------------------------------------------

def fit_curve(df: pd.DataFrame) -> tuple[float, float]:
    """METR's curve: logistic success on log2 human minutes, weighted so each family counts alike."""
    X = sm.add_constant(df.log2_minutes)
    fit = sm.GLM(df.score_binarized, X, family=sm.families.Binomial(),
                 var_weights=df.invsqrt_task_weight / df.invsqrt_task_weight.mean()).fit()
    return fit.params["const"], fit.params["log2_minutes"]


def horizons(runs: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for alias, df in runs.groupby("alias"):
        b0, b1 = fit_curve(df)
        rows.append({"model": alias, "runs": len(df), "horizon_minutes": 2 ** (-b0 / b1) if b1 < 0 else np.nan})
    return pd.DataFrame(rows).sort_values("horizon_minutes")


def task_residuals(runs: pd.DataFrame) -> pd.DataFrame:
    """Each task's success minus the success its length predicts, averaged over models.

    Positive means agents did better than the task's length suggests.
    """
    parts = []
    for alias, df in runs.groupby("alias"):
        b0, b1 = fit_curve(df)
        t = df.groupby(["task_id", "task_family"]).agg(success=("score_binarized", "mean"),
                                                        log2_minutes=("log2_minutes", "first")).reset_index()
        t["residual"] = t.success - 1 / (1 + np.exp(-(b0 + b1 * t.log2_minutes)))
        parts.append(t)
    all_ = pd.concat(parts)
    return all_.groupby(["task_id", "task_family"]).agg(
        residual=("residual", "mean"), log2_minutes=("log2_minutes", "first")).reset_index()


# Tags -----------------------------------------------------------------------

def load_tags() -> pd.DataFrame | None:
    path = HERE / "tags.csv"
    if not path.exists():
        return None
    tags = pd.read_csv(path)
    hand = DATA / "hand_tags.csv"
    if hand.exists():
        h = pd.read_csv(hand).dropna(subset=["value"])
        label = h.value.astype(str).str.strip().str.lower()
        h["value"] = label.map({"easy": 0.0, "mixed": 0.5, "hard": 1.0, "true": 1.0, "false": 0.0})
        h["item_type"] = np.where(label.isin(["true", "false"]), "factor", "axis")
        h["pass"] = "hand"
        tags = pd.concat([tags, h[["unit_id", "item", "item_type", "value", "pass"]]])
    return tags


def reliability(tags: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (item_type, item), df in tags.groupby(["item_type", "item"]):
        m = df.pivot_table(index="pass", columns="unit_id", values="value", aggfunc="first")
        level = "ordinal" if item_type == "axis" else "nominal"
        try:
            a = krippendorff.alpha(reliability_data=m.to_numpy(dtype=float), level_of_measurement=level)
        except ValueError:  # every rater gave the same value everywhere
            a = np.nan
        rows.append({"item_type": item_type, "item": item, "alpha": a,
                     "na_rate": df.value.isna().mean()})
    return pd.DataFrame(rows)


def consensus(tags: pd.DataFrame, units: pd.DataFrame, tasks: pd.DataFrame) -> pd.DataFrame:
    """One value per task and item: the mean over model passes, with n/a taken as the easy end.

    A task with its own text uses its own tags. Otherwise it takes its family's.
    """
    model_tags = tags[tags["pass"] != "hand"]
    wide = model_tags.pivot_table(index="unit_id", columns="item", values="value", aggfunc="mean").fillna(0.0)
    own = tasks.task_id.isin(wide.index)
    unit_for_task = np.where(own, tasks.task_id, tasks.task_family)
    out = wide.reindex(unit_for_task)
    out.index = tasks.task_id
    return out


# Steps 2 to 6 ---------------------------------------------------------------

def tagger_check(factors: pd.DataFrame, runs: pd.DataFrame) -> dict:
    """METR's own spec: task mean success ~ factor sum + ln(human minutes), OLS.
    Errors are clustered by family, which METR's code does not do."""
    t = runs.groupby("task_id").agg(success=("score_binarized", "mean"),
                                   minutes=("human_minutes", "mean"), family=("task_family", "first"))
    df = t.join(factors.sum(axis=1).rename("factor_sum"), how="inner")
    df["log_minutes"] = np.log(df.minutes.clip(lower=0.1))
    fit = sm.OLS(df.success, sm.add_constant(df[["factor_sum", "log_minutes"]])).fit(
        cov_type="cluster", cov_kwds={"groups": df.family})
    lo, hi = fit.conf_int().loc["factor_sum"]
    return {"slope": fit.params["factor_sum"], "lo": lo, "hi": hi, "r2": fit.rsquared, "n": len(df),
            "mean_sum": df.factor_sum.mean()}


def metr_label_agreement(factors: pd.DataFrame) -> pd.DataFrame | None:
    """If METR sent their labels as data/metr_messiness.csv, compare per factor."""
    path = DATA / "metr_messiness.csv"
    if not path.exists():
        return None
    theirs = pd.read_csv(path)
    id_col = "task id" if "task id" in theirs else "task_id"
    theirs = theirs.groupby(id_col).mean(numeric_only=True)
    if {"implicit generalizability required", "implicit generalizability requirements are scored"} <= set(theirs):
        theirs["implicit generalizability required and scored"] = (
            (theirs["implicit generalizability required"] >= 0.5)
            & (theirs["implicit generalizability requirements are scored"] >= 0.5)).astype(float)
    rows = []
    for f in factors.columns:
        if f not in theirs:
            continue
        both = pd.concat([factors[f] >= 0.5, theirs[f] >= 0.5], axis=1, join="inner").dropna()
        both.columns = ["ours", "theirs"]
        a = krippendorff.alpha(reliability_data=both.T.to_numpy(dtype=float), level_of_measurement="nominal")
        rows.append({"factor": f, "n": len(both), "agree": (both.ours == both.theirs).mean(), "alpha": a})
    return pd.DataFrame(rows)


def one_at_a_time(X: pd.DataFrame, y: pd.Series, groups: pd.Series) -> pd.DataFrame:
    rows = []
    for axis in X.columns:
        fit = sm.OLS(y, sm.add_constant(X[[axis]])).fit(cov_type="cluster", cov_kwds={"groups": groups})
        lo, hi = fit.conf_int().loc[axis]
        rows.append({"axis": axis, "effect": fit.params[axis], "lo": lo, "hi": hi, "p": fit.pvalues[axis]})
    out = pd.DataFrame(rows)
    out["q"] = multipletests(out.p, method="fdr_bh")[1]
    return out


def family_folds(groups: pd.Series, k: int | None = None) -> list:
    """Leave one family out, or k folds by family."""
    if k is None:
        fams = groups.unique()
        return [(np.where(groups != f)[0], np.where(groups == f)[0]) for f in fams]
    return list(GroupKFold(k).split(np.zeros(len(groups)), groups=groups))


def stability(X: pd.DataFrame, y: pd.Series, groups: pd.Series, n_sub: int, seed: int) -> pd.DataFrame:
    """Stability selection (Meinshausen and Buhlmann 2010). On each random half of the
    families, run the lasso path and keep the first STABILITY_Q axes to enter. An axis
    joins the shortlist if it is kept in at least SHORTLIST_SHARE of the halves. This
    bounds the expected number of noise axes on the shortlist (see stability_bound)."""
    Xs = StandardScaler().fit_transform(X)
    yc = (y - y.mean()).to_numpy()
    rng = np.random.default_rng(seed)
    fams = groups.unique()
    hits = np.zeros(X.shape[1])
    for _ in range(n_sub):
        pick = rng.choice(fams, len(fams) // 2, replace=False)
        idx = np.where(groups.isin(pick))[0]
        _, coefs, _ = lasso_path(Xs[idx], yc[idx], n_alphas=200)
        entered = (coefs != 0).argmax(axis=1).astype(float)
        entered[~(coefs != 0).any(axis=1)] = np.inf
        hits[np.argsort(entered, kind="stable")[:STABILITY_Q]] += 1
    full = ElasticNetCV(l1_ratio=1.0, cv=family_folds(groups, 5), max_iter=50000).fit(Xs, y)
    return pd.DataFrame({"axis": X.columns, "lasso_coef_sd": full.coef_, "kept_share": hits / n_sub})


def stability_bound(p: int) -> float:
    """Upper bound on the expected number of noise axes on the shortlist."""
    return STABILITY_Q ** 2 / ((2 * SHORTLIST_SHARE - 1) * p)


def logo_r2(X: np.ndarray, y: np.ndarray, groups: pd.Series, make_model) -> float:
    """Out of sample R² with each family held out in turn."""
    pred = np.zeros_like(y)
    for train, test in family_folds(groups):
        pred[test] = make_model(train).fit(X[train], y[train]).predict(X[test])
    return 1 - ((y - pred) ** 2).sum() / ((y - y.mean()) ** 2).sum()


def added_value(axes: pd.DataFrame, factor_sum: pd.Series, y: pd.Series, groups: pd.Series) -> pd.DataFrame:
    """Compare length-only (the residual itself, so R² 0), METR's sum, axes, and both.

    The axes models choose their own features inside each fold, so selection
    never sees the held out family.
    """
    yv = y.to_numpy()
    sc = StandardScaler()

    def enet(train):
        inner = family_folds(groups.iloc[train].reset_index(drop=True), 5)
        return ElasticNetCV(l1_ratio=[0.5, 0.9, 1.0], cv=inner, max_iter=50000)

    def ols(train):
        return Ridge(alpha=1e-6)

    both = np.column_stack([factor_sum, axes])
    return pd.DataFrame([
        {"model": "METR messiness sum", "logo_r2": logo_r2(sc.fit_transform(factor_sum.to_frame()), yv, groups, ols)},
        {"model": "Our axes (elastic net)", "logo_r2": logo_r2(sc.fit_transform(axes), yv, groups, enet)},
        {"model": "Messiness sum + our axes", "logo_r2": logo_r2(sc.fit_transform(both), yv, groups, enet)},
    ])


def shuffle_test(axes: pd.DataFrame, y: pd.Series, groups: pd.Series, n_perm: int, seed: int) -> dict:
    """Ridge on all reliable axes, scored by leave one family out R².
    Then shuffle which family gets which tags and score again, n_perm times."""
    Xs = StandardScaler().fit_transform(axes)
    yv = y.to_numpy()

    def ridge(_):
        return Ridge(alpha=10.0)

    real = logo_r2(Xs, yv, groups, ridge)
    fam_rows = {f: np.where(groups == f)[0] for f in groups.unique()}
    fam_tags = {f: Xs[idx].mean(axis=0) for f, idx in fam_rows.items()}
    fams = list(fam_rows)
    rng = np.random.default_rng(seed)
    null = []
    for _ in range(n_perm):
        perm = dict(zip(fams, rng.permutation(fams)))
        Xp = np.zeros_like(Xs)
        for f, idx in fam_rows.items():
            Xp[idx] = fam_tags[perm[f]]
        null.append(logo_r2(Xp, yv, groups, ridge))
    null = np.array(null)
    return {"real_r2": real, "null_mean": null.mean(), "null_95": np.quantile(null, 0.95),
            "p": (1 + (null >= real).sum()) / (1 + n_perm)}


# Report ---------------------------------------------------------------------

def md(df: pd.DataFrame, floatfmt: str = ".3f") -> str:
    cols = list(df.columns)
    out = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(f"{v:{floatfmt}}" if isinstance(v, float) else str(v) for v in r) + " |")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", default="1.1", help="which METR runs file to use for the main analysis")
    ap.add_argument("--boot", type=int, default=200)
    ap.add_argument("--perms", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    runs = load_runs(args.runs)
    report = ["# METR retagging: results", "",
              f"Runs file: time horizon {args.runs}. SWAA and human runs dropped.", ""]

    h = horizons(runs)
    report += ["## 0. Baseline: METR's time horizons from public data", "",
               "Check these against METR's published numbers before trusting anything below.", "",
               md(h, ".1f"), ""]
    print(h.to_string(index=False))

    tags = load_tags()
    if tags is None:
        report += ["No tags.csv yet. Run tag.py to go further.", ""]
        (HERE / "results.md").write_text("\n".join(report))
        print("no tags.csv, wrote baseline only")
        return

    units = pd.read_json(DATA / "units.jsonl", lines=True)
    tasks = task_residuals(runs)
    cons = consensus(tags, units, tasks).loc[tasks.task_id]
    groups = tasks.task_family.reset_index(drop=True)
    y = tasks.residual.reset_index(drop=True)

    # 1. Reliability
    rel = reliability(tags)
    axis_names = sorted(tags.loc[tags.item_type == "axis", "item"].unique())
    factor_names = sorted(tags.loc[tags.item_type == "factor", "item"].unique())
    A = cons[axis_names].reset_index(drop=True)
    F = cons[factor_names].reset_index(drop=True)
    rel = rel.merge(pd.DataFrame({"item": axis_names, "sd": A.std().to_numpy()}), on="item", how="left")
    ax_rel = rel[rel.item_type == "axis"].copy()
    ax_rel["status"] = np.select(
        [ax_rel.na_rate > MAX_NA, ax_rel.sd < MIN_SD, ax_rel.alpha.isna() | (ax_rel.alpha < MIN_ALPHA)],
        ["mostly n/a", "untested here", "unreliable"], "kept")
    kept = ax_rel.loc[ax_rel.status == "kept", "item"].tolist()
    passes = sorted(tags["pass"].unique())
    report += ["## 1. Reliability", "",
               f"Raters: {', '.join(passes)}. Axes go further only if no more than {MAX_NA:.0%} of tags are n/a, "
               f"alpha is at least {MIN_ALPHA} and the spread (sd) across tasks is at least {MIN_SD}.", "",
               md(ax_rel.sort_values("alpha", ascending=False)[["item", "alpha", "sd", "na_rate", "status"]]), "",
               f"{len(kept)} of {len(axis_names)} axes kept.", "",
               "METR factors:", "",
               md(rel[rel.item_type == "factor"].sort_values("alpha", ascending=False)[["item", "alpha", "na_rate"]]), ""]
    served = tags[tags["pass"] != "hand"].drop_duplicates(["unit_id", "pass"])
    swapped = served[~served.apply(lambda r: r.served_model.startswith(
        "claude-sonnet" if r["pass"] == "sonnet" else "claude-opus"), axis=1)] if "served_model" in served else []
    if len(swapped):
        report += [f"{len(swapped)} tagging calls were answered by a fallback model after a refusal.", ""]

    # 2. Tagger check
    report += ["## 2. Tagger check: METR's 16 factors, tagged by our pipeline", "",
               f"METR found a slope of {METR_SLOPE} per point, controlling for log length.", ""]
    F_by_task = F.set_index(tasks.task_id)
    rows = []
    paper = load_runs("1.0")
    paper = paper[paper.alias.isin(PAPER_MODELS)]
    full = F_by_task.index.isin(units.loc[units.kind == "full", "unit_id"])
    for label, f, r in [("1.0 runs, paper models", F_by_task, paper),
                        (f"{args.runs} runs, all models", F_by_task, runs),
                        (f"{args.runs} runs, full task text only", F_by_task[full], runs),
                        (f"{args.runs} runs, family summaries only", F_by_task[~full], runs)]:
        c = tagger_check(f, r)
        rows.append({"data": label, "slope": c["slope"], "95% CI": f"{c['lo']:.3f} to {c['hi']:.3f}",
                     "r2": c["r2"], "tasks": c["n"], "mean sum": c["mean_sum"]})
    report += [md(pd.DataFrame(rows)), "", "METR's mean messiness was 3.2.", ""]
    agree = metr_label_agreement(F_by_task)
    if agree is not None:
        report += ["Agreement with METR's own labels:", "", md(agree), ""]

    # 3. One axis at a time
    single = one_at_a_time(A[kept], y, groups).sort_values("p")
    report += ["## 3. One axis at a time", "",
               "Effect is the change in success rate, beyond what length predicts, from the easy end to the "
               "hard end. Errors are clustered by family. q is the p value after Benjamini Hochberg.", "",
               md(single), ""]

    # 4. Shortlist
    stab = stability(A[kept], y, groups, args.boot, args.seed).sort_values("kept_share", ascending=False)
    shortlist = stab.loc[stab.kept_share >= SHORTLIST_SHARE, "axis"].tolist()
    report += ["## 4. All together: the shortlist", "",
               f"Stability selection on the {len(kept)} kept axes. On each of {args.boot} random halves of the "
               f"families, the first {STABILITY_Q} axes to enter the lasso are kept. kept_share is how often "
               f"each axis was kept. The shortlist is every axis kept in at least {SHORTLIST_SHARE:.0%} of halves. "
               f"Expect at most {stability_bound(len(kept)):.1f} noise axes on it. lasso_coef_sd is the full "
               f"data lasso coefficient per standard deviation, for the sign.", "",
               md(stab), "", f"Shortlist: {', '.join(shortlist) or 'none'}.", ""]

    # 5. Added value
    av = added_value(A[kept], F.sum(axis=1), y, groups)
    report += ["## 5. Added value over METR's messiness sum", "",
               "Out of sample R² for the residual (success beyond length), holding out one family at a time. "
               "Zero means no better than guessing the average.", "", md(av), ""]

    # 6. Shuffle test
    sh = shuffle_test(A[kept], y, groups, args.perms, args.seed)
    report += ["## 6. Shuffle test", "",
               f"Real tags: R² {sh['real_r2']:.3f}. Tags shuffled across families {args.perms} times: "
               f"mean {sh['null_mean']:.3f}, 95th percentile {sh['null_95']:.3f}. p = {sh['p']:.3f}.", ""]

    (HERE / "results.md").write_text("\n".join(report))
    print("wrote results.md")


if __name__ == "__main__":
    main()
