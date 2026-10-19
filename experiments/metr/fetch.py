# /// script
# requires-python = ">=3.11"
# dependencies = ["pypdf", "requests"]
# ///
"""Download METR's public run data and whatever task text is public.

Writes, all under data/ (gitignored, never commit it):
  runs-1.0.jsonl, runs-1.1.jsonl  per run results from METR/eval-analysis-public
  units.jsonl                     one row per thing to tag: full task text where public,
                                  otherwise the family summary from the HCAST paper
  metr_task_text/                 drop METR's private task text here if they share it,
                                  one file per task named <family>__<task>.txt

The units carry no times, scores or model names, so tagging stays blind.
"""

import io
import json
import re
from pathlib import Path

import requests
from pypdf import PdfReader

HERE = Path(__file__).parent
DATA = HERE / "data"

RUNS = {
    "1.0": "https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-0/data/raw/runs.jsonl",
    "1.1": "https://raw.githubusercontent.com/METR/eval-analysis-public/main/reports/time-horizon-1-1/data/raw/runs.jsonl",
}
HCAST_PDF = "https://arxiv.org/pdf/2503.17354"
README_REPOS = ["METR/public-tasks", "METR/RE-Bench"]


def get(url: str) -> bytes:
    r = requests.get(url, timeout=120)
    r.raise_for_status()
    return r.content


def fetch_runs() -> list[dict]:
    for version, url in RUNS.items():
        path = DATA / f"runs-{version}.jsonl"
        if not path.exists():
            path.write_bytes(get(url))
    return [json.loads(line) for line in open(DATA / "runs-1.1.jsonl")]


def hcast_family_summaries() -> dict[str, str]:
    """Parse the task family table in the HCAST paper's appendix.

    Each entry is: name, a line with time and domain, a line with privacy and
    experience, then the description. Only the description is kept.
    """
    text = "\n".join(p.extract_text() for p in PdfReader(io.BytesIO(get(HCAST_PDF))).pages)
    body = text[text.find("Task Family Information"):]
    body = re.sub(r"Continued on next page\.\.\.\n\d+\nPreprint\. Under review\.\nTask Family Information\n", "", body)
    name = r"\n([a-z0-9][a-z0-9 _\-]+)"
    meta = r"\n[\d.]+[smh] \((?:baseline|estimate)\) · [^\n]+\n[^\n]+\n"
    next_entry = r"\n[a-z0-9][a-z0-9 _\-]+" + meta
    pattern = re.compile(name + meta + r"(.*?)(?=" + next_entry + r"|\n[A-Z]\.\d|\Z)", re.S)
    summaries = {}
    for m in pattern.finditer(body):
        desc = re.sub(r"-\n(?=[a-z])", "", m.group(2))
        desc = re.sub(r"\s+", " ", desc).strip()
        desc = re.sub(r"\s+\d+$", "", desc)  # trailing page number
        summaries[m.group(1).strip().replace(" ", "_")] = desc
    return summaries


def readme_instructions(repo: str, family: str) -> dict[str, str]:
    """Return {task_name: instructions} from a family README's 'Full Task Instructions'.

    Only that section is kept. The rest of the README holds baseline times and
    scores, which the tagger must not see.
    """
    url = f"https://raw.githubusercontent.com/{repo}/main/{family}/README.md"
    r = requests.get(url, timeout=60)
    if r.status_code != 200:
        return {}
    text = r.text
    start = text.find("## Full Task Instructions")
    if start < 0:
        return {}
    section = text[start + len("## Full Task Instructions"):]
    end = re.search(r"\n# |\n## ", section)
    section = section[: end.start()] if end else section
    tasks = {}
    for m in re.finditer(r"\n### (\S+)\n(.*?)(?=\n### |\Z)", section, re.S):
        body = m.group(2).strip().strip("`").strip()
        if body:
            tasks[m.group(1)] = body
    return tasks


def main() -> None:
    DATA.mkdir(exist_ok=True)
    (DATA / "metr_task_text").mkdir(exist_ok=True)
    runs = fetch_runs()

    # SWAA tasks are seconds long with no messiness range; METR dropped them too.
    tasks = sorted({(r["task_family"], r["task_id"]) for r in runs if r["task_source"] != "SWAA"})
    families = sorted({f for f, _ in tasks})

    summaries = hcast_family_summaries()
    full: dict[str, str] = {}
    for family in families:
        for repo in README_REPOS:
            for name, body in readme_instructions(repo, family).items():
                full[f"{family}/{name}"] = body

    private = {
        p.stem.replace("__", "/"): p.read_text()
        for p in (DATA / "metr_task_text").glob("*.txt")
    }

    units = []
    tagged_families = set()
    for family, task_id in tasks:
        text = private.get(task_id) or full.get(task_id)
        if text:
            units.append({"unit_id": task_id, "family": family, "kind": "full", "text": text})
            tagged_families.add(family)
    for family in families:
        if family in tagged_families:
            continue
        if family in summaries:
            units.append({"unit_id": family, "family": family, "kind": "summary", "text": summaries[family]})
        else:
            print(f"no text for family {family}")

    with open(DATA / "units.jsonl", "w") as f:
        for u in units:
            f.write(json.dumps(u) + "\n")
    n_full = sum(u["kind"] == "full" for u in units)
    print(f"{len(units)} units: {n_full} full task texts, {len(units) - n_full} family summaries")
    print(f"{len(families)} families, {len(tasks)} non-SWAA tasks in runs")


if __name__ == "__main__":
    main()
