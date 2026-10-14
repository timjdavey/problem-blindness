---
type: Axis
title: Stationary vs drifting
description: Do the patterns in your past data still hold, or does the world keep shifting so that what you learnt goes stale?
group: world
easy_end: Stationary
hard_end: Drifting
sources:
  - resource: /frameworks/1987-vuca.md
    title: VUCA
  - resource: /frameworks/1992-task-characteristics-of-expertise.md
    title: Task characteristics of expertise
  - resource: /frameworks/2009-conditions-for-intuitive-expertise.md
    title: Conditions for intuitive expertise
---
# Stationary vs drifting

An axis in the [world](index.md#the-world) group.

Do the patterns in your past data still hold, or does the world keep shifting so that what you learnt goes stale? Gravity stays put. Music tastes, fashion and slang keep moving, so old data goes stale.

## Actions

**Stationary**: Train once and monitor lightly.
- Trust last year's test set. In a stable world it predicts this year well.
- Use a slow release cycle. Retraining often costs effort and buys you little.

**Drifting**: Plan for the model to go stale.
- Test on the most recent slice of time, not a random split. A random split leaks the future into training and flatters the model.
- Weight recent data more heavily than old. The older a case, the less it says about today.
- Watch live inputs for drift. Compare what the model sees now with what it was trained on, and raise an alert when they part.
- Retrain on a schedule, and budget for it from the start. A model that was right at launch will go wrong later without anyone touching it.

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) shows patterns break once people react to policy built on them, so a reflexive system drifts by its own doing.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Opponents learn your method and change their play, so last year's patterns stop working.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (study). [Shanteau](../frameworks/1992-task-characteristics-of-expertise.md) and [Kahneman and Klein](../frameworks/2009-conditions-for-intuitive-expertise.md) both need a stable, regular setting before experience turns into skill.
- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). [Knight](../frameworks/1921-risk-vs-uncertainty.md)'s uncertainty starts where the future may not look like the past.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A drifting world keeps serving up cases nobody has seen.
- [Small vs large world](small-vs-large-world.md) (logic). A drifting world keeps adding states nobody listed.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Hayek's point was that local circumstances change every day ([Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)).

## Citations

[1] [VUCA](../frameworks/1987-vuca.md)

[2] [Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)

[3] [Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)
