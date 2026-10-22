# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Build the tagging rubric from the axis files, so the axes stay the single source.

Run it on its own to print the rubric, or with --sheet to write a blank hand
tagging sheet for a random sample of units.
"""

import argparse
import csv
import json
import random
import re
from pathlib import Path

import yaml

from metr_factors import FACTORS

HERE = Path(__file__).parent
AXES = HERE.parent.parent / "axes"
SKIP = {"index.md", "README.md"}

PREFACE = """You are tagging tasks from a benchmark for AI agents. Each task is given to an AI agent working alone in a sandboxed computer, with a time limit. Tag the task as the agent receives it. The solver is the AI agent, not a human expert.

You will see the task text only. Some tasks are a full prompt and some are a one or two sentence summary of a family of similar tasks. Tag what the text supports and say so in the evidence when you are inferring.

Part 1 is a set of axes. For each axis, pick:
- "easy" if the task sits at the easy end,
- "hard" if it sits at the hard end,
- "mixed" if it sits in between or parts of the task differ,
- "n/a" if the axis has nothing to grip on in this task.
Give one short sentence of evidence for each.

Part 2 is a set of yes or no questions. Answer each with true or false and one short sentence of evidence."""


def load_axes() -> list[dict]:
    axes = []
    for path in sorted(AXES.glob("*.md")):
        if path.name in SKIP:
            continue
        text = path.read_text()
        _, front, body = text.split("---", 2)
        meta = yaml.safe_load(front)
        # The first paragraph after the "An axis in the ..." line is the plain question.
        paras = [p.strip() for p in body.split("\n\n") if p.strip() and not p.strip().startswith("#")]
        question = paras[1] if paras and paras[0].startswith("An axis in") else ""
        question = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", question)  # drop links
        axes.append({
            "id": path.stem,
            "title": meta["title"],
            "easy_end": meta["easy_end"],
            "hard_end": meta["hard_end"],
            "description": meta["description"],
            "question": question,
            "group": meta.get("group"),
        })
    return axes


def rubric(axes: list[dict], seed: int | None = None) -> str:
    """The system prompt. A seed shuffles the order of axes and factors."""
    axes = list(axes)
    factors = list(FACTORS.items())
    if seed is not None:
        rng = random.Random(seed)
        rng.shuffle(axes)
        rng.shuffle(factors)
    lines = [PREFACE, "", "# Part 1: axes", ""]
    for a in axes:
        lines += [
            f"## {a['id']}",
            f"Easy end: {a['easy_end']}. Hard end: {a['hard_end']}.",
            a["description"],
            a["question"],
            "",
        ]
    lines += ["# Part 2: yes or no questions", ""]
    for key, definition in factors:
        lines += [f"## {key}", definition, ""]
    return "\n".join(lines)


def output_schema(axes: list[dict]) -> dict:
    """JSON schema for structured output: one object per axis and per factor."""
    axis_item = {
        "type": "object",
        "properties": {
            "value": {"type": "string", "enum": ["easy", "mixed", "hard", "n/a"]},
            "evidence": {"type": "string"},
        },
        "required": ["value", "evidence"],
        "additionalProperties": False,
    }
    factor_item = {
        "type": "object",
        "properties": {"value": {"type": "boolean"}, "evidence": {"type": "string"}},
        "required": ["value", "evidence"],
        "additionalProperties": False,
    }
    return {
        "type": "object",
        "properties": {
            "axes": {
                "type": "object",
                "properties": {a["id"]: axis_item for a in axes},
                "required": [a["id"] for a in axes],
                "additionalProperties": False,
            },
            "factors": {
                "type": "object",
                "properties": {k: factor_item for k in FACTORS},
                "required": list(FACTORS),
                "additionalProperties": False,
            },
        },
        "required": ["axes", "factors"],
        "additionalProperties": False,
    }


def write_sheet(n: int, seed: int) -> None:
    """A blank sheet for hand tagging. Fill value with easy, mixed, hard or n/a,
    and true or false for the factors. Save it as data/hand_tags.csv."""
    units = [json.loads(line) for line in open(HERE / "data" / "units.jsonl")]
    sample = random.Random(seed).sample(units, n)
    axes = load_axes()
    out = HERE / "data" / "hand_tags_template.csv"
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["unit_id", "item", "value"])
        for u in sample:
            for a in axes:
                w.writerow([u["unit_id"], a["id"], ""])
            for k in FACTORS:
                w.writerow([u["unit_id"], k, ""])
    with open(HERE / "data" / "hand_tags_tasks.md", "w") as f:
        for u in sample:
            f.write(f"## {u['unit_id']}\n\n{u['text']}\n\n")
    print(f"wrote {out} and data/hand_tags_tasks.md for {n} units")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", type=int, metavar="N", help="write a hand tagging sheet for N units")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    if args.sheet:
        write_sheet(args.sheet, args.seed)
    else:
        print(rubric(load_axes()))
