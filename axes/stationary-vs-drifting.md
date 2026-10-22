---
type: Axis
title: Stationary vs drifting
description: "Stationary: the patterns in past data still hold today (e.g. gravity). Drifting: the world keeps shifting, so what you learnt goes stale (e.g. fashion and slang)."
group: world
subgroup: change
easy_end: Stationary
hard_end: Drifting
sources:
  - resource: /frameworks/1987-vuca.md
    title: VUCA
  - resource: /frameworks/1992-task-characteristics-of-expertise.md
    title: Task characteristics of expertise
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
  - resource: /frameworks/2009-conditions-for-intuitive-expertise.md
    title: Conditions for intuitive expertise
---
# Stationary vs drifting

An axis in the [Change](index.md#change) set of the [world](index.md#the-world) group.

Do the patterns in your past data still hold, or does the world keep shifting so that what you learnt goes stale? Gravity stays put. Music tastes, fashion and slang keep moving, so old data goes stale.

The same gap can open between practice and the real task. Robin Hogarth, Tomás Lejarraga and Emre Soyer split learning into the setting where you learn and the setting where you use it. When the two don't match, experience teaches the wrong lesson, and they call that a [wicked learning environment](../frameworks/2001-kind-vs-wicked-learning-environments.md). A pilot trained only in calm weather has learnt in a different world from the one they fly in. Drift opens the same gap over time, so a model trained on last year's data is used in a world that no longer matches it.

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
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (study). [Shanteau](../frameworks/1992-task-characteristics-of-expertise.md) and [Kahneman and Klein](../frameworks/2009-conditions-for-intuitive-expertise.md) both need a stable setting and quick feedback before experience turns into skill. Delay makes drift worse, since the world may have moved by the time the grade arrives.
- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). [Knight](../frameworks/1921-risk-vs-uncertainty.md)'s uncertainty starts where the future may not look like the past.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A drifting world keeps serving up cases nobody has seen.
- [Small vs large world](small-vs-large-world.md) (logic). A drifting world keeps adding states nobody listed.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Hayek's point was that local circumstances change every day ([Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)).
- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (independent). Both make forecasts go bad with time, so they get mixed up. A short horizon means small errors grow while the rules stay fixed. Drift means the rules themselves change. Weather is chaotic, yet the physics behind it never moves. Slang drifts, but nothing about it is chaotic.
- [Ends vs never-ending](ends-vs-never-ending.md) (logic). A drifting world is one reason a problem never ends, since every answer goes stale. But weeds grow back in a garden where nothing has changed.
- [Still vs moving](still-vs-moving.md) (independent). Drift makes what you learnt go stale over months. A moving world makes what you saw go stale within one task. The rules of tennis haven't drifted in decades, yet every rally moves.

## Citations

[1] [VUCA](../frameworks/1987-vuca.md)

[2] [Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)

[3] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)

[4] [Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)
