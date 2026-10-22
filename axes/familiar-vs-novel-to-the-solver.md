---
type: Axis
title: Familiar vs novel to the solver
description: "Familiar: the solver has met this kind of problem many times before (e.g. a doctor seeing a common cold). Novel: the problem is new to the solver, even if others have solved it (e.g. a question outside a model's training data)."
group: knower
subgroup: know-how
easy_end: Familiar
hard_end: Novel
sources:
  - resource: /frameworks/1960-programmed-vs-non-programmed-decisions.md
    title: Programmed vs non-programmed decisions
  - resource: /frameworks/1967-routine-vs-non-routine-technology.md
    title: Routine vs non-routine technology
  - resource: /frameworks/1983-skill-rule-and-knowledge-based-behaviour.md
    title: Skill, rule and knowledge-based behaviour
---
# Familiar vs novel to the solver

An axis in the [Know-how](index.md#know-how) set of the [knower](index.md#the-knower) group.

Has the solver, person or model, met this kind of problem before, or is it new to them even if others have solved it? A doctor sees a common cold every day but a rare disease once in a career. For an AI model the question is whether the problem sits inside its training data, which affects whether it can recall an answer or has to work one out.

## Actions

**Familiar**: Trust recall.
- Accept a quick answer. A problem like those in training is one the model has seen solved.
- Spend less on reasoning. Long chains of working add cost and little accuracy on a problem the model knows.

**Novel**: Make the solver reason, and check the result.
- Ask for working. A step by step answer shows where the reasoning went wrong.
- Break the task into steps and verify each one. Errors on a new problem stack up, so catch them early.
- Test the model on problems written after its training cutoff. A benchmark it has seen measures memory, not skill.
- Watch for a familiar answer to the wrong problem. A model will often match a new problem to an old one it looks like.

## Correlated with

- [Stationary vs drifting](stationary-vs-drifting.md) (logic). A drifting world keeps serving up cases nobody has seen.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). A rare kind of case is one the solver has seldom seen. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (opposite). With no trained pattern to call on, the solver has to reason slowly from an explicit model ([Skill, rule and knowledge-based behaviour](../frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)).
- [Well vs ill-structured](well-vs-ill-structured.md) and [Reversible vs irreversible](reversible-vs-irreversible.md) (bundled). Simon's [non-programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md) are new, messy and high stakes all at once.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.
- [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md) (logic). A bounded skill runs out of new cases, while an open-ended one keeps serving up cases the solver hasn't met. But a famous poem is familiar ground, and reading it well still has no ceiling.

## Citations

[1] [Programmed vs non-programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md)

[2] [Routine vs non-routine technology](../frameworks/1967-routine-vs-non-routine-technology.md)

[3] [Skill, rule and knowledge-based behaviour](../frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)
