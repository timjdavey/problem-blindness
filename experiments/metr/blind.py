# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Tag with subagents or a fresh chat instead of the API.

  uv run blind.py prepare   writes data/blind/<pass>/batch_<n>/ with a rubric,
                            the tasks under anonymous ids and an empty out/ folder
  uv run blind.py collect   checks the replies and copies them into data/raw/,
                            the same place tag.py writes, then run tag.py --collect-only

Task names are replaced by ids like T017 and the order is shuffled, so the
tagger can't spot families or recall results. The key lives in data/blind/key.json.
"""

import json
import random
import sys
from pathlib import Path

from codebook import load_axes, rubric
from metr_factors import FACTORS
from tag import PASSES

HERE = Path(__file__).parent
DATA = HERE / "data"
BLIND = DATA / "blind"
BATCHES = 3

SUBAGENT_MODEL = {"opus": "claude-opus (subagent)", "sonnet": "claude-sonnet (subagent)",
                  "opus-shuffled": "claude-opus (subagent)"}

INSTRUCTIONS = """# Tagging instructions

Read `rubric.md` in this folder, then tag every task in `tasks.md` in this folder.

Work only from these two files. Do not open any other file in the repository, and do
not search the web. The point is to tag blind.

For each task write one JSON file to `out/<id>.json`, for example `out/T017.json`:

```json
{
  "axes": {"<axis id>": {"value": "easy|mixed|hard|n/a", "evidence": "one short sentence"}, ...},
  "factors": {"<factor name>": {"value": true, "evidence": "one short sentence"}, ...}
}
```

Every one of the {n_axes} axes and {n_factors} factors in the rubric must appear, spelt
exactly as in the rubric headings. Keep evidence short. Tag each task on its own merits.
"""


def prepare() -> None:
    units = [json.loads(line) for line in open(DATA / "units.jsonl")]
    random.Random(7).shuffle(units)
    key = {f"T{i:03d}": u["unit_id"] for i, u in enumerate(units, 1)}
    (BLIND).mkdir(parents=True, exist_ok=True)
    (BLIND / "key.json").write_text(json.dumps(key, indent=1))
    ids = list(key)
    by_id = {k: u for k, u in zip(ids, units)}
    axes = load_axes()
    for p, cfg in PASSES.items():
        system = rubric(axes, seed=cfg["seed"])
        for b in range(BATCHES):
            d = BLIND / p / f"batch_{b + 1}"
            (d / "out").mkdir(parents=True, exist_ok=True)
            (d / "rubric.md").write_text(system)
            (d / "INSTRUCTIONS.md").write_text(
                INSTRUCTIONS.replace("{n_axes}", str(len(axes))).replace("{n_factors}", str(len(FACTORS))))
            chunk = ids[b::BATCHES]
            (d / "tasks.md").write_text("\n".join(f"## {i}\n\n{by_id[i]['text']}\n" for i in chunk))
    print(f"{len(ids)} tasks in {BATCHES} batches for passes {', '.join(PASSES)}")


def collect() -> None:
    key = json.loads((BLIND / "key.json").read_text())
    axis_ids = {a["id"] for a in load_axes()}
    ok = bad = 0
    for p in PASSES:
        (DATA / "raw" / p).mkdir(parents=True, exist_ok=True)
        for anon, unit_id in key.items():
            hits = list((BLIND / p).glob(f"batch_*/out/{anon}.json"))
            if not hits:
                print(f"missing {p}/{anon}")
                bad += 1
                continue
            tags = json.loads(hits[0].read_text())
            problems = (axis_ids ^ set(tags.get("axes", {}))) | (set(FACTORS) ^ set(tags.get("factors", {})))
            problems |= {a for a, t in tags.get("axes", {}).items() if t.get("value") not in ("easy", "mixed", "hard", "n/a")}
            problems |= {f for f, t in tags.get("factors", {}).items() if not isinstance(t.get("value"), bool)}
            if problems:
                print(f"bad {p}/{anon}: {sorted(problems)[:5]}")
                bad += 1
                continue
            out = DATA / "raw" / p / (unit_id.replace("/", "__") + ".json")
            out.write_text(json.dumps({"unit_id": unit_id, "pass": p, "served_model": SUBAGENT_MODEL[p],
                                       "usage": None, "tags": tags}, indent=1))
            ok += 1
    print(f"{ok} collected, {bad} missing or bad")


if __name__ == "__main__":
    {"prepare": prepare, "collect": collect}[sys.argv[1]]()
