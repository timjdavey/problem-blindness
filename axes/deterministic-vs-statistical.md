---
type: Axis
title: Deterministic vs statistical
description: "Deterministic: the same inputs always give exactly the same output (e.g. a sum). Statistical: the same inputs give different results each time, but the rate across many cases is steady (e.g. which boilers break down this winter)."
group: world
subgroup: randomness
easy_end: Deterministic
hard_end: Statistical
sources:
  - resource: /frameworks/1948-simplicity-disorganised-and-organised-complexity.md
    title: Simplicity, disorganised complexity and organised complexity
  - resource: /frameworks/1966-clocks-and-clouds.md
    title: Clocks and clouds
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Deterministic vs statistical

An axis in the [Randomness](index.md#randomness) set of the [world](index.md#the-world) group.

Do the same inputs always give the same result, or only the same spread of results, so you can predict the rate but not the single case? A sum is deterministic. Which boiler breaks down this winter is statistical, though the rate across many boilers is steady.

## Actions

**Deterministic**: Write the rule down and test it like code.
- Don't ask a model to guess at a rule you could state. A rule that is right most of the time is a bug.
- Use the model to draft the rule or the code, then check that against tests. The tests decide if it ships, not the model.
- Test for exact output. The same input should give the same answer every run, so any variation is a fault to fix.

**Statistical**: Judge the spread, not single cases.
- Evaluate on a large held-out set. A few good examples tell you nothing when any one case can go either way.
- Report error rates and calibration. Calibration means that when the model says 70%, it is right about 70% of the time.
- Decide as a policy over many cases. Ask what rule gives the best results across the whole group, not what suits this one.
- Don't judge the model on one bad outcome. A right call can still lose, so look at the rate across many calls.

## Correlated with

- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (bundled). [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end, though chaos shows a fully deterministic system can still have a short horizon.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Pure chance is one kind of doubt that no new data can shrink. But Russell and Norvig note that a deterministic world you can only half see looks random to you ([Task environment properties](../frameworks/1995-task-environment-properties.md)). So doubt that looks like chance may be a hidden fact you could find.
- [Thin vs fat tails](thin-vs-fat-tails.md) (by definition). The tails axis only applies once a problem is statistical. A deterministic problem has no spread of results, so it has no tails to speak of.
- [Coherent vs incoherent](coherent-vs-incoherent.md) (by definition). A deterministic problem gives the same result every run, so it is always coherent. But a statistical one can be coherent too. A die varies roll to roll, yet every thousand rolls look alike.

## Citations

[1] [Simplicity, disorganised complexity and organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md)

[2] [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md)

[3] [Task environment properties](../frameworks/1995-task-environment-properties.md)
