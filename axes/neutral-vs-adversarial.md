---
type: Axis
title: Neutral vs adversarial
description: "Neutral: your mistakes are accidents, because the world doesn't care what you do (e.g. rain doesn't try to beat your umbrella). Adversarial: someone whose goals differ from yours hunts for the cases your rule gets wrong (e.g. fraudsters)."
group: environment
subgroup: reactivity
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
  - resource: https://doi.org/10.1145/1014052.1014066
    title: Adversarial classification (Dalvi, 2004)
  - resource: https://doi.org/10.1609/aies.v7i1.31647
    title: "Red-teaming for generative AI: silver bullet or security theater? (Feffer, 2024)"
  - resource: https://doi.org/10.6028/NIST.SP.800-63B-4
    title: "Digital identity guidelines: authentication and authenticator management (Temoshok, 2025)"
---
# Neutral vs adversarial

An axis in the [Reactivity](index.md#reactivity) set of the [environment](index.md#environment) group.

Are your mistakes accidents, or is someone picking them for you? Rain doesn't try to beat your umbrella, so the cases you meet are a fair sample and your errors fall where chance puts them. Fraudsters, hackers and rival traders are different. They study your rule, find the cases it gets wrong and send you more of those.

The other side doesn't have to be an enemy. It only needs goals that differ from yours and a way to see what you reward. Judge teachers on test results and they drill the test, dropping the parts of the subject it doesn't cover. They aren't out to hurt anyone. They found the gap between what the rule counts and what it is for, and went through it. This is [Goodhart's law](../frameworks/1975-goodharts-law.md). When the outcome moves because a lot of people believe or follow your forecast, with nobody aiming at your rule, that is the hard end of [Inert vs reflexive](inert-vs-reflexive.md) instead.

## Actions

**Neutral**: Optimise for the typical case.
- Test on typical cases. Errors are accidents, so a random sample of real cases is a fair test. [5]
- Publish your rules if that helps people use them. Guarding them from people who aren't against you only leaves both sides worse off. [1]

**Adversarial**: Assume someone is probing for your weak spots.
- Red team your rule before it goes live. Pay people to play the attacker and break it, as armies have long done and AI labs do before they release a model. Then test on those attacks, not on typical cases. [4, 5, 6]
- Expect attackers to adapt, and update fast. A drop in the attacks you catch may mean they found a way round, not that they gave up. [1, 5]
- Keep part of the rule hidden or changing. A fixed public rule is one an attacker only has to beat once. [1, 2]
- Judge people on more than one number. Anyone scored on a single measure will learn to move it, so keep some judgement that no number can replace. [3]
- Learn from a different number than the one you reward. Once a number is a target, it shows how well people can hit it. [2]
- Layer your defences. Beating one check should not be enough to get through, which is why a bank asks for a code from your phone as well as a password. [7]

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (logic). Both are about people reacting to you, so they often turn up together, as in a market. What splits them is whether anyone is aiming at your rule. A bank run is reflexive with no adversary in it. A chess opponent hunts for your weakest line, but the board doesn't change because someone forecast the result. If someone studies your rule to find its gaps, it is adversarial. If the outcome moves with nobody aiming at anything, it is reflexive.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (logic). Fraudsters and rivals change their play once they learn yours.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (bundled). Opponents hide what they can, as in poker ([Task environment properties](../frameworks/1995-task-environment-properties.md)). The facts exist, but they cost more to find, and some choices an opponent hasn't made yet can't be found at all.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). Rivals often want different things, so the two tend to come together. But two players in a [zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) agree on what winning means. They each just want to be the winner. Contested values is a fight over what a good result even is.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). By [Goodhart's law](../frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it, because they learn to pass the check instead of doing the work.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed.
- [Private vs accountable](private-vs-accountable.md) (study). [Campbell's law](../frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (independent). A chess opponent works against you, but every move you need is yours to make. Two firms in a [non-zero-sum game](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) want the same deal and still need each other to close it.
- [Static vs dynamic](static-vs-dynamic.md) (bundled). Russell and Norvig's harder worlds have other agents in them, and an opponent is the most common reason the world won't wait. But a surfer's wave moves and isn't trying to beat anyone.
- [Antifragile vs wears out](antifragile-vs-wears-out.md) (logic). Bacteria have no aim, yet each course of antibiotics leaves them harder to kill. An adversary is a system that gains from your rule on purpose.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). Opponents hide what they know, as in poker. But chess is adversarial with nothing hidden, and the worst cases can pile up with nobody aiming at your rule. When an insurer can't see who is sick, the healthy leave and the sick stay, each just picking the plan that suits them.

## Citations

[1] [Zero-sum vs non-zero-sum games](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md)

[2] [Goodhart's law](../frameworks/1975-goodharts-law.md)

[3] [Campbell's law](../frameworks/1976-campbells-law.md)

[4] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[5] [Adversarial classification (Dalvi, 2004)](https://doi.org/10.1145/1014052.1014066)

[6] [Red-teaming for generative AI: silver bullet or security theater? (Feffer, 2024)](https://doi.org/10.1609/aies.v7i1.31647)

[7] [Digital identity guidelines: authentication and authenticator management (Temoshok, 2025)](https://doi.org/10.6028/NIST.SP.800-63B-4)
