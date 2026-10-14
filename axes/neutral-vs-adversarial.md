---
type: Axis
title: Neutral vs adversarial
description: Is someone working against you?
group: world
easy_end: Neutral
hard_end: Adversarial
sources:
  - resource: /frameworks/1944-zero-sum-vs-non-zero-sum-games.md
    title: Zero-sum vs non-zero-sum games
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Neutral vs adversarial

An axis in the [world](index.md#the-world) group.

Is someone working against you? Rain doesn't try to beat your umbrella. Fraudsters, hackers and rival traders learn your methods and change their play to beat them.

## Actions

**Neutral**: Optimise for the typical case.
- Test on typical data. Errors are accidents, so a random sample of real inputs is a fair test.
- Publish how the model works if that helps users. Nobody is reading it to find a way round.

**Adversarial**: Assume someone is probing for your weak spots.
- Red team the model. Pay people to attack it before launch, and test on those attacks rather than typical inputs.
- Retrain fast as attackers adapt. A drop in the attacks you catch may mean they found a way round, not that they gave up.
- Keep part of the logic hidden or changing. A fixed public rule is one an attacker only has to beat once.
- Layer the model with rules and rate limits. Beating one check should not be enough to get through.

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (bundled). The [Keynesian beauty contest](../frameworks/1936-keynesian-beauty-contest.md) and [zero-sum games](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) are both about other minds reacting to yours. The difference is intent. A bank run is reflexive with no enemy in it. A chess opponent wants to beat you, but nothing about the game shifts because of a forecast.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Fraudsters and rivals change their play once they learn yours.
- [Full vs partial observability](full-vs-partial-observability.md) (bundled). Opponents hide what they can, as in poker ([Task environment properties](../frameworks/1995-task-environment-properties.md)).
- [Shared vs contested values](shared-vs-contested-values.md) (logic). Rivals often want different things, so the two tend to come together. But two players in a [zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) agree on what winning means. They each just want to be the winner. Contested values is a fight over what a good result even is.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (independent). A chess opponent works against you, but every move you need is yours to make. Two firms in a [non-zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) want the same deal and still need each other to close it.

## Citations

[1] [Zero-sum vs non-zero-sum games](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md)

[2] [Task environment properties](../frameworks/1995-task-environment-properties.md)
