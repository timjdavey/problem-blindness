# /// script
# requires-python = ">=3.11"
# dependencies = ["anthropic", "pyyaml"]
# ///
"""Tag every unit on the axes and on METR's 16 factors, blind to outcomes.

The tagger sees the rubric and the task text, nothing else: no task id, family
name, human time, score or model. Three passes give three raters:

  opus          claude-opus-5-5, axes in file order
  sonnet        claude-sonnet-5-5, axes in file order
  opus-shuffled claude-opus-5-5, axes and factors in a shuffled order

Raw replies, evidence included, go to data/raw/<pass>/ and are resumable.
tags.csv holds the values only, with no task text, so it is safe to commit.

Uses the server-side refusal fallback, so a declined request is re-run on
another model. The model that actually answered is kept in the served_model
column, so the analysis can drop or flag those rows.
"""

import argparse
import csv
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import anthropic

from codebook import load_axes, output_schema, rubric
from metr_factors import FACTORS

HERE = Path(__file__).parent
DATA = HERE / "data"
RAW = DATA / "raw"

PASSES = {
    "opus": {"model": "claude-opus-5-5", "seed": None},
    "sonnet": {"model": "claude-sonnet-5-5", "seed": None},
    "opus-shuffled": {"model": "claude-opus-5-5", "seed": 1},
}
VALUES = {"easy": 0.0, "mixed": 0.5, "hard": 1.0, "n/a": None}

client = anthropic.Anthropic()


def tag_one(unit: dict, pass_name: str, system: str, schema: dict) -> dict:
    cfg = PASSES[pass_name]
    with client.messages.stream(
        model=cfg["model"],
        max_tokens=32000,
        thinking={"type": "adaptive"},
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": schema}},
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": f"<task>\n{unit['text']}\n</task>"}],
        extra_headers={"anthropic-beta": "server-side-fallback-2026-07-01"},
        extra_body={"fallbacks": "default"},
    ) as stream:
        msg = stream.get_final_message()
    if msg.stop_reason in ("refusal", "max_tokens"):
        raise RuntimeError(f"{unit['unit_id']} {pass_name}: stop_reason {msg.stop_reason}")
    text = next(b.text for b in msg.content if b.type == "text")
    return {
        "unit_id": unit["unit_id"],
        "pass": pass_name,
        "served_model": msg.model,
        "usage": msg.usage.model_dump(),
        "tags": json.loads(text),
    }


def run(passes: list[str], limit: int | None, workers: int) -> None:
    units = [json.loads(line) for line in open(DATA / "units.jsonl")]
    if limit:
        units = units[:limit]
    axes = load_axes()
    schema = output_schema(axes)

    jobs = []
    for p in passes:
        (RAW / p).mkdir(parents=True, exist_ok=True)
        system = rubric(axes, seed=PASSES[p]["seed"])
        for u in units:
            out = RAW / p / (u["unit_id"].replace("/", "__") + ".json")
            if not out.exists():
                jobs.append((u, p, system, out))
    print(f"{len(jobs)} calls to make")

    with ThreadPoolExecutor(workers) as pool:
        futures = {pool.submit(tag_one, u, p, s, schema): out for u, p, s, out in jobs}
        for i, f in enumerate(as_completed(futures), 1):
            try:
                futures[f].write_text(json.dumps(f.result(), indent=1))
                print(f"{i}/{len(jobs)} {futures[f].parent.name}/{futures[f].stem}")
            except (anthropic.APIError, RuntimeError) as e:
                print(f"{i}/{len(jobs)} FAILED {futures[f].stem}: {e}")


def collect() -> None:
    """Flatten data/raw into tags.csv: one row per unit, pass and item."""
    units = {json.loads(line)["unit_id"]: json.loads(line) for line in open(DATA / "units.jsonl")}
    rows = []
    for path in sorted(RAW.glob("*/*.json")):
        r = json.loads(path.read_text())
        u = units[r["unit_id"]]
        base = {"unit_id": r["unit_id"], "family": u["family"], "kind": u["kind"],
                "pass": r["pass"], "served_model": r["served_model"]}
        for axis, t in r["tags"]["axes"].items():
            rows.append({**base, "item_type": "axis", "item": axis, "label": t["value"],
                         "value": VALUES[t["value"]]})
        for factor, t in r["tags"]["factors"].items():
            rows.append({**base, "item_type": "factor", "item": factor, "label": str(t["value"]).lower(),
                         "value": float(t["value"])})
    with open(HERE / "tags.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote tags.csv with {len(rows)} rows")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--passes", nargs="+", default=list(PASSES), choices=list(PASSES))
    ap.add_argument("--limit", type=int, help="tag only the first N units, for a smoke test")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--collect-only", action="store_true")
    args = ap.parse_args()
    if not args.collect_only:
        run(args.passes, args.limit, args.workers)
    collect()
