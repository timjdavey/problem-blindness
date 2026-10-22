---
type: Axis
title: Neutral vs adversarial
description: "Neutral: your mistakes are accidents, because the world doesn't care what you do (e.g. rain doesn't try to beat your umbrella). Adversarial: someone whose goals differ from yours hunts for the cases your rule gets wrong (e.g. fraudsters)."
group: world
subgroup: response
easy_end: Neutral
hard_end: Adversarial
sources:
  - resource: /frameworks/1944-zero-sum-vs-non-zero-sum-games.md
    title: Zero-sum vs non-zero-sum games
  - resource: /frameworks/1975-goodharts-law.md
    title: Goodhart's law
  - resource: /frameworks/1976-campbells-law.md
    title: Campbell's law
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Neutral vs adversarial

An axis in the [Response](index.md#response) set of the [world](index.md#the-world) group.

Are your mistakes accidents, or is someone picking them for you? Rain doesn't try to beat your umbrella, so the cases you meet are a fair sample and your errors fall where chance puts them. Fraudsters, hackers and rival traders are different. They study your rule, find the cases it gets wrong and send you more of those.

The other side doesn't have to be an enemy. It only needs goals that differ from yours and a way to see what you reward. Judge teachers on test results and they drill the test, dropping the parts of the subject it doesn't cover. They aren't out to hurt anyone. They found the gap between what the rule counts and what it is for, and went through it. This is [Goodhart's law](../frameworks/1975-goodharts-law.md). When the outcome moves because a lot of people believe or follow your forecast, with nobody aiming at your rule, that is the hard end of [Inert vs reflexive](inert-vs-reflexive.md) instead.

## Actions

**Neutral**: Optimise for the typical case.
- Test on typical data. Errors are accidents, so a random sample of real inputs is a fair test.
- Publish how the model works if that helps users. Nobody is reading it to find a way round.

**Adversarial**: Assume someone is probing for your weak spots.
- Red team the model. Pay people to attack it before launch, and test on those attacks rather than typical inputs.
- Retrain fast as attackers adapt. A drop in the attacks you catch may mean they found a way round, not that they gave up.
- Keep part of the logic hidden or changing. A fixed public rule is one an attacker only has to beat once.
- Judge people on more than one number. Anyone scored on a single measure will learn to move it, so keep some judgement that no number can replace.
- Layer the model with rules and rate limits. Beating one check should not be enough to get through.

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (logic). Both are about people reacting to you, so they often turn up together, as in a market. What splits them is whether anyone is aiming at your rule. A bank run is reflexive with no adversary in it. A chess opponent hunts for your weakest line, but the board doesn't change because someone forecast the result. If someone studies your rule to find its gaps, it is adversarial. If the outcome moves with nobody aiming at anything, it is reflexive.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Fraudsters and rivals change their play once they learn yours.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (bundled). Opponents hide what they can, as in poker ([Task environment properties](../frameworks/1995-task-environment-properties.md)). The facts exist, but they cost more to find, and some choices an opponent hasn't made yet can't be found at all.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). Rivals often want different things, so the two tend to come together. But two players in a [zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) agree on what winning means. They each just want to be the winner. Contested values is a fight over what a good result even is.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). By [Goodhart's law](../frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it, because they learn to pass the check instead of doing the work.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed.
- [Private vs accountable](private-vs-accountable.md) (study). [Campbell's law](../frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (independent). A chess opponent works against you, but every move you need is yours to make. Two firms in a [non-zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) want the same deal and still need each other to close it.
- [Static vs dynamic](static-vs-dynamic.md) (bundled). Russell and Norvig's harder worlds have other agents in them, and an opponent is the most common reason the world won't wait. But a surfer's wave moves and isn't trying to beat anyone.
- [Antifragile vs wears out](antifragile-vs-wears-out.md) (logic). Bacteria have no aim, yet each course of antibiotics leaves them harder to kill. An adversary is a system that gains from your rule on purpose.

## Citations

[1] [Zero-sum vs non-zero-sum games](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md)

[2] [Goodhart's law](../frameworks/1975-goodharts-law.md)

[3] [Campbell's law](../frameworks/1976-campbells-law.md)

[4] [Task environment properties](../frameworks/1995-task-environment-properties.md)
