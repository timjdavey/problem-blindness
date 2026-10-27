---
type: Axis
aliases:
  - Stationary vs drifting
title: Durable vs perishable lessons
description: "Durable lessons: the rules behind your past data still hold, so what you learnt keeps working (e.g. gravity). Perishable lessons: the rules behind your past data keep changing, so what you learnt goes stale (e.g. fashion and slang)."
group: environment
subgroup: change
easy_end: Durable lessons
hard_end: Perishable lessons
sources:
  - resource: /frameworks/1987-vuca.md
    title: VUCA
  - resource: /frameworks/1992-task-characteristics-of-expertise.md
    title: Task characteristics of expertise
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
  - resource: /frameworks/2009-conditions-for-intuitive-expertise.md
    title: Conditions for intuitive expertise
  - resource: https://doi.org/10.1145/2523813
    title: A survey on concept drift adaptation (Gama, 2014)
---
# Durable vs perishable lessons

An axis in the [Change](index.md#change) set of the [environment](index.md#environment) group.

Do the patterns in your past data still hold, or does the world keep shifting so that what you learnt goes stale? Gravity stays put, so what you learnt about it keeps working. Music tastes, fashion and slang keep moving, so old data goes stale. The cause is in the world, not in you. The rules that produce the data change, and what you learnt from them perishes as a result. Statisticians call such a world non-stationary, and machine learning calls the change concept drift.

The same gap can open between practice and the real task. Robin Hogarth, Tomás Lejarraga and Emre Soyer split learning into the setting where you learn and the setting where you use it. When the two don't match, experience teaches the wrong lesson, and they call that a [wicked learning environment](../frameworks/2001-kind-vs-wicked-learning-environments.md). A pilot trained only in calm weather has learnt in a different world from the one they fly in. Drift opens the same gap over time, so a model trained on last year's data is used in a world that no longer matches it.

## Actions

**Durable lessons**: Learn once and check in now and then.
- Trust last year's results. In a stable world they predict this year well, so a bridge engineer doesn't relearn the physics each spring. [2, 4]
- Update slowly and keep a long memory. When the world isn't moving, reacting fast to each new case mostly chases noise. [5]
- Lean on experts who learnt in this setting. Long practice with quick, clear feedback in a stable world is what builds real skill, as in weather forecasting and chess. [2, 4]

**Perishable lessons**: Plan for what you know to go stale.
- Judge your method on the latest cases, not on a mix of old and new. A mix lets patterns that have since faded flatter you, as when a trader tests a strategy on years the market has left behind. [5]
- Give recent cases more weight than old ones. The older a case, the less it says about today. [5]
- Watch for the cases in front of you to stop looking like the ones you learnt on. A buyer who sees last season's best sellers stop selling has spotted drift, and so has a team whose model starts seeing inputs it never trained on. [3, 5]
- Plan to relearn on a schedule, and budget for it from the start. A rule, a habit or a model that was right at the start will go wrong later without anyone touching it. [5]
- Don't trust confidence built in a world that has since moved. Experience feels like expertise even after its lessons go stale. Ask whether the expert's setting still matches today's, not how sure they are. [2, 3, 4]

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) shows patterns break once people react to policy built on them, so a reflexive system drifts by its own doing.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Opponents learn your method and change their play, so last year's patterns stop working.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (study). [Shanteau](../frameworks/1992-task-characteristics-of-expertise.md) and [Kahneman and Klein](../frameworks/2009-conditions-for-intuitive-expertise.md) both need a stable setting and quick feedback before experience turns into skill. Delay makes drift worse, since the world may have moved by the time the grade arrives.
- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (logic). [Knight](../frameworks/1921-risk-vs-uncertainty.md)'s uncertainty starts where the future may not look like the past.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A drifting world keeps serving up cases nobody has seen.
- [Foreseeable vs unforeseeable outcomes](foreseeable-vs-unforeseeable-outcomes.md) (logic). A drifting world keeps adding states nobody listed.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Hayek's point was that local circumstances change every day ([Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)).
- [Stable vs chaotic](stable-vs-chaotic.md) (independent). Both make forecasts go bad with time, so they get mixed up. Chaos means small errors grow while the rules stay fixed. Drift means the rules themselves change. Weather is chaotic, yet the physics behind it never moves. Slang drifts, but nothing about it is chaotic.
- [Curable vs chronic](curable-vs-chronic.md) (logic). A drifting world is one reason a problem never ends, since every answer goes stale. But weeds grow back in a garden where nothing has changed.
- [Turn-based vs real-time](turn-based-vs-real-time.md) (independent). Drift makes what you learnt go stale over months. A real-time world makes what you saw go stale within one task. The rules of tennis haven't drifted in decades, yet every rally moves.
- [Self-righting vs tipping](self-righting-vs-tipping.md) (independent). In drift the rules slowly change. In a tip the rules stay fixed and the state jumps. Slang drifts with no tipping point, and a shallow lake tips while its chemistry stays the same.
- [Antifragile vs wears out](antifragile-vs-wears-out.md) (independent). Drift happens on its own, while wear and growth are caused by stress. A muscle you stop using shrinks, which looks like drift, but the cause is the missing load.

## Citations

[1] [VUCA](../frameworks/1987-vuca.md)

[2] [Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)

[3] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)

[4] [Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)

[5] [A survey on concept drift adaptation (Gama, 2014)](https://doi.org/10.1145/2523813)
