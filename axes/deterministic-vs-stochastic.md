---
type: Axis
title: Deterministic vs stochastic
aliases:
  - Deterministic vs statistical
description: "Deterministic: the same inputs always give exactly the same output (e.g. a sum). Stochastic: the same inputs give different results each time, but the rate across many cases is steady (e.g. which boilers break down this winter)."
group: environment
subgroup: randomness
easy_end: Deterministic
hard_end: Stochastic
sources:
  - resource: /frameworks/1948-simplicity-disorganised-and-organised-complexity.md
    title: Simplicity, disorganised complexity and organised complexity
  - resource: /frameworks/1954-clinical-vs-statistical-prediction.md
    title: Clinical vs statistical prediction
  - resource: /frameworks/1966-clocks-and-clouds.md
    title: Clocks and clouds
  - resource: /frameworks/1988-outcome-bias.md
    title: Outcome bias
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
---
# Deterministic vs stochastic

An axis in the [Randomness](index.md#randomness) set of the [environment](index.md#environment) group.

Do the same inputs always give the same result, or only the same spread of results, so you can predict the rate but not the single case? A sum is deterministic. Which boiler breaks down this winter is statistical, though the rate across many boilers is steady.

A statistical world grades you with noise. A fund manager can beat the market five years running on luck alone, and each good year feels like proof of skill. Robin Hogarth counts this as one way a [learning environment turns wicked](../frameworks/2001-kind-vs-wicked-learning-environments.md). It gets worse when you only get a few graded tries, since a handful of results can't separate luck from skill.

## Actions

**Deterministic**: Write the rule down and test it like code.
- Don't go by feel where you could state the rule. A rule that is right most of the time is a bug. A payroll clerk who works out overtime by eye will get some payslips wrong. [1, 2]
- Check the rule against cases where you already know the answer, whoever wrote it. The same input should give the same answer every time, so any miss or any variation is a fault to fix. [1, 5]
- Predict and plan far ahead. A system that runs like a clock can be forecast precisely, as Halley timed the 1715 eclipse to within about four minutes. [3]

**Stochastic**: Judge the spread, not single cases.
- Test on many fresh cases, not a few you remember. A few good examples tell you nothing when any one case can go either way, so a head teacher can't judge a reading scheme by the three pupils who shone. [1, 6]
- Give odds, not certainties, and keep a record of how they turn out. Things you call 70% likely should happen about 70% of the time. [3, 5, 6]
- Decide as a policy over many cases. Ask what rule gives the best results across the whole group, not what suits this one. In repeated, noisy calls, simple formulas matched or beat expert judgement in nearly every study Meehl gathered. [1, 2]
- Don't judge a call by one outcome. A poker player can bet right and still lose the hand. Judge the call by what was known when it was made, and the caller by the rate across many calls. [4]

## Correlated with

- [Stable vs chaotic](stable-vs-chaotic.md) (bundled). [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end, though chaos shows a fully deterministic system can still have a short horizon.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Pure chance is one kind of doubt that no new data can shrink. But Russell and Norvig note that a deterministic world you can only half see looks random to you ([Task environment properties](../frameworks/1995-task-environment-properties.md)). So doubt that looks like chance may be a hidden fact you could find.
- [Thin vs fat tails](thin-vs-fat-tails.md) (by definition). The tails axis only applies once a problem is statistical. A deterministic problem has no spread of results, so it has no tails to speak of.
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (by definition). A deterministic problem gives the same result every run, so it is always coherent. But a statistical one can be coherent too. A die varies roll to roll, yet every thousand rolls look alike.

## Citations

[1] [Simplicity, disorganised complexity and organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md)

[2] [Clinical vs statistical prediction](../frameworks/1954-clinical-vs-statistical-prediction.md)

[3] [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md)

[4] [Outcome bias](../frameworks/1988-outcome-bias.md)

[5] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[6] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)
