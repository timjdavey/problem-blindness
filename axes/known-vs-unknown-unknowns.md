---
type: Axis
aliases:
  - Small vs large world
  - Closed vs open outcomes
title: Known vs unknown unknowns
description: "Known unknowns: you don't know which outcome will come, but you know every one that could, however many there are (e.g. a lottery ticket). Unknown unknowns: things can turn out in ways nobody could have listed in advance, so the result could be something nobody thought of (e.g. a new product hit by a change in the law)."
group: information
subgroup: uncertainty
easy_end: Known unknowns
hard_end: Unknown unknowns
sources:
  - resource: /frameworks/1954-small-and-large-worlds.md
    title: Small and large worlds
  - resource: /frameworks/2002-known-and-unknown-unknowns.md
    title: Known and unknown unknowns
  - resource: /frameworks/2020-radical-uncertainty.md
    title: Radical uncertainty
  - resource: https://doi.org/10.1080/01621459.1949.10483310
    title: The Monte Carlo method (Metropolis, 1949)
---
# Known vs unknown unknowns

An axis in the [Uncertainty](index.md#uncertainty) set of the [information](index.md#information) group.

Do you know everything that could happen, even if you don't know which will? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. The lottery is a known unknown, since you know what might happen but not which. The launch is full of unknown unknowns, the things nobody knew to ask about. Donald Rumsfeld made both names famous in 2002.

The outcome nobody listed can be a windfall as well as a disaster. In 1928 Alexander Fleming came back from holiday to find a mould had killed the bacteria on one of his plates, and it gave the world penicillin. A plan with no room for surprise misses the good ones too.

This axis is about gaps, not size. Go's rules decide every position, so you know every way a game could end, even though there are far too many to check. How many there are is a question for [Tractable vs intractable options](tractable-vs-intractable-options.md). When fixed rules decide the outcomes, you can work them out or sample them before you choose. When nothing does, there is nothing to sample from and the result can be something new.

Leonard Savage called a world of known unknowns a small world and one with unknown unknowns a large one, and said his theory of rational choice only works in the small one. Machine learning meets the same split as open-set recognition, where a model has to notice an input from a class it never trained on.

## Actions

**Known unknowns**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so you can weigh them all, as Edward Thorp did in 1961 for every mix of cards left in a blackjack deck. [1, 3]
- Test against the full list. The list is complete, so a plan that handles every case on it won't meet a surprise. [1]
- Simulate when the list is too long. Run the procedure many times and count how often each outcome comes up, as you might deal many games of solitaire to learn the odds of winning. [4]

**Unknown unknowns**: Leave room for what nobody listed.
- Make "none of these" an answer. A nurse with a triage chart or a model with fixed labels has to put every case somewhere, so a case off the list gets filed wrong. [1]
- Don't trust a simulation to cover it. A war game or a stress test can only produce the outcomes someone built into it. [1, 3]
- Treat a case that fits nothing as news, whether it looks like a fault or a gift. Ask what is going on, build the best story that explains it and test it against what others think. [3]
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list. [1, 2, 3]
- Leave slack, and people who can improvise. Apollo 13's crew survived in 1970 because engineers on the ground built a filter adapter from bags, cardboard and tape. [1, 2]

## Correlated with

- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (by definition). You can't put odds on a state you never listed, so unknown unknowns have unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](../frameworks/1961-ambiguity-aversion.md)).
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (independent). Both are about what you don't know, but they ask different things. Reducible vs irreducible uncertainty asks whether the missing fact can be found, and this axis asks whether you know what the possibilities are. A known unknown can be irreducible. You know a rival might cut prices next year, and no research can tell you whether they will. An unknown unknown can be reducible. A drug can have a side effect that a simple lab test would have shown, if anyone had thought to run it.
- [Tractable vs intractable options](tractable-vs-intractable-options.md) (independent). These two are easy to confuse, since both can leave you unable to check everything. This axis asks whether you know everything that could happen once you choose, and no computing helps. Tractable vs intractable options asks how many options you have to choose from, and more computing helps. Go has intractable options, yet every outcome is a known unknown, since its rules decide every position. Choosing between two job offers has tractable options, yet anything could happen after you choose. Designing a new drug is hard on both, with far too many molecules to test and side effects nobody listed.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)).
- [Given vs invented options](given-vs-invented-options.md) (bundled). Savage's small world fixes the list of actions as well as the list of states. When there are unknown unknowns you often have to invent the options too.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). Clear groups let you list the ways things might turn out. Scattered runs leave outcomes nobody thought to list.

## Citations

[1] [Small and large worlds](../frameworks/1954-small-and-large-worlds.md)

[2] [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md)

[3] [Radical uncertainty](../frameworks/2020-radical-uncertainty.md)

[4] [The Monte Carlo method (Metropolis, 1949)](https://doi.org/10.1080/01621459.1949.10483310)
