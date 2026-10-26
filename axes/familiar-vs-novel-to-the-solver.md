---
type: Axis
title: Familiar vs novel to the solver
description: "Familiar to the solver: the solver has met this kind of problem many times before (e.g. a doctor seeing a common cold). Novel to the solver: the problem is new to the solver, even if others have solved it (e.g. a question outside a model's training data)."
group: agent
subgroup: know-how
easy_end: Familiar to the solver
hard_end: Novel to the solver
sources:
  - resource: /frameworks/1960-programmed-vs-non-programmed-decisions.md
    title: Programmed vs non-programmed decisions
  - resource: /frameworks/1967-routine-vs-non-routine-technology.md
    title: Routine vs non-routine technology
  - resource: /frameworks/1983-skill-rule-and-knowledge-based-behaviour.md
    title: Skill, rule and knowledge-based behaviour
  - resource: /frameworks/1988-moravecs-paradox.md
    title: Moravec's paradox
  - resource: https://arxiv.org/abs/2405.00332
    title: A careful examination of large language model performance on grade school arithmetic (Zhang, 2024)
---
# Familiar vs novel to the solver

An axis in the [Know-how](index.md#know-how) set of the [agent](index.md#agent) group.

Has the solver, person or model, met this kind of problem before, or is it new to them even if others have solved it? A doctor sees a common cold every day but a rare disease once in a career. For an AI model the question is whether the problem sits inside its training data, which affects whether it can recall an answer or has to work one out.

## Actions

**Familiar to the solver**: Trust recall.
- Accept a quick answer. A mechanic who has heard a rattle a hundred times knows the fault before opening the bonnet. [3]
- Spend less on reasoning. Treating a routine case as special each time wastes judgement and gives different answers to the same question. [1]

**Novel to the solver**: Make the solver reason, and check the result.
- Judge novelty for the solver in front of you, not for yourself. What is routine for people and what is routine for machines barely overlap. AlphaGo beat Lee Sedol in 2016 but needed a person to place its stones. [4]
- Watch for a familiar answer to the wrong problem. A rule that worked last time gets used on a case that only looks the same. Build in a pause when the usual fix isn't working, so the solver steps up to reasoning. [3]
- Ask for the working and check it for gaps. Reasoning from scratch goes wrong because the solver is slow, misses facts and stops too early. [3]
- Don't run a new case through a procedure built for old ones. It will be confidently wrong on every case it didn't foresee, as Australia's Robodebt scheme was for about 400,000 people. Leave the call to someone with the skill and the power to decide. [1, 2]
- Test the solver on problems they can't have seen, or you measure memory, not skill. When researchers wrote fresh maths problems like those in a popular benchmark, some models scored up to 8% lower. An exam needs fresh questions for the same reason. [5]

## Correlated with

- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (logic). A drifting world keeps serving up cases nobody has seen.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). A rare kind of case is one the solver has seldom seen. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (opposite). With no trained pattern to call on, the solver has to reason slowly from an explicit model ([Skill, rule and knowledge-based behaviour](../frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)).
- [Well vs ill-structured](well-vs-ill-structured.md) and [Reversible vs irreversible](reversible-vs-irreversible.md) (bundled). Simon's [non-programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md) are new, messy and high stakes all at once.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.
- [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md) (logic). A bounded skill runs out of new cases, while an open-ended one keeps serving up cases the solver hasn't met. But a famous poem is familiar ground, and reading it well still has no ceiling.

## Citations

[1] [Programmed vs non-programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md)

[2] [Routine vs non-routine technology](../frameworks/1967-routine-vs-non-routine-technology.md)

[3] [Skill, rule and knowledge-based behaviour](../frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)

[4] [Moravec's paradox](../frameworks/1988-moravecs-paradox.md)

[5] [A careful examination of large language model performance on grade school arithmetic (Zhang, 2024)](https://arxiv.org/abs/2405.00332)
