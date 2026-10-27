---
type: Axis
aliases:
  - Small vs large world
  - Closed vs open outcomes
title: Foreseeable vs unforeseeable outcomes
description: "Foreseeable outcomes: you don't know which outcome will come, but you can list every one that could, however many there are (e.g. a lottery ticket). Unforeseeable outcomes: things can turn out in ways nobody could have listed in advance, so the result could be something nobody thought of (e.g. a new product hit by a change in the law)."
group: information
subgroup: uncertainty
easy_end: Foreseeable outcomes
hard_end: Unforeseeable outcomes
sources:
  - resource: /frameworks/1936-unanticipated-consequences.md
    title: Unanticipated consequences
  - resource: /frameworks/1954-small-and-large-worlds.md
    title: Small and large worlds
  - resource: /frameworks/2007-incertitude-matrix.md
    title: Incertitude matrix
  - resource: /frameworks/2020-radical-uncertainty.md
    title: Radical uncertainty
  - resource: https://doi.org/10.1080/01621459.1949.10483310
    title: The Monte Carlo method (Metropolis, 1949)
---
# Foreseeable vs unforeseeable outcomes

An axis in the [Uncertainty](index.md#uncertainty) set of the [information](index.md#information) group.

Can you list every way things might turn out, even if you don't know which will happen? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. The lottery's outcomes are foreseeable, since you know what might happen but not which. The launch's are not.

The outcome nobody listed can be a windfall as well as a disaster. In 1928 Alexander Fleming came back from holiday to find a mould had killed the bacteria on one of his plates, and it gave the world penicillin. A plan with no room for surprise misses the good ones too.

Often the outcome nobody foresaw comes from your own action. In 1936 the sociologist Robert Merton called these the unanticipated consequences of purposive action. He found people miss them through ignorance and error, and because they care so much about the result they want that they don't look past it. In 1935 the US Forest Service ruled that every fire be out by the next morning, and the dead wood that built up made later fires burn hotter. How far side effects can spread depends on the problem. In a [reductionist problem](reductionist-vs-holistic.md) a change to one part stays there. In a holistic problem or a [cascading system](buffered-vs-cascading.md) it reaches parts you never meant to touch.

This axis is about gaps, not size. Go's rules decide every position, so you can foresee every way a game could end, even though there are far too many to check. How many there are is a question for [Tractable vs intractable options](tractable-vs-intractable-options.md). It is also about what comes out, not what goes in. Whether you know which facts you're missing is a question for [Known vs unknown unknowns](known-vs-unknown-unknowns.md). When fixed rules decide the outcomes, you can work them out or sample them before you choose. When nothing does, there is nothing to sample from and the result can be something new.

Leonard Savage called a world where you can list every outcome a small world, and one where you can't a large one. He said his theory of rational choice only works in the small one. Andy Stirling calls not knowing what could happen ignorance, and keeps it apart from not knowing the odds. Machine learning meets the same split as open-set recognition, where a model has to notice an input from a class it never trained on.

## Actions

**Foreseeable outcomes**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so you can weigh them all, as Edward Thorp did in 1961 for every mix of cards left in a blackjack deck. [2, 4]
- Test against the full list. The list is complete, so a plan that handles every case on it won't meet a surprise. [2]
- Simulate when the list is too long. Run the procedure many times and count how often each outcome comes up, as you might deal many games of solitaire to learn the odds of winning. [5]

**Unforeseeable outcomes**: Leave room for what nobody listed.
- Make "none of these" an answer. A nurse with a triage chart or a model with fixed labels has to put every case somewhere, so a case off the list gets filed wrong. [2]
- Don't trust a simulation to cover it. A war game or a stress test can only produce the outcomes someone built into it. [2, 4]
- Look past the result you want. Ask what else your action will touch, since the side effects are the outcomes people most often fail to list. [1]
- Treat a case that fits nothing as news, whether it looks like a fault or a gift. Ask what is going on, build the best story that explains it and test it against what others think. [4]
- Keep watching after you act. No model predicted the sudden hole in the ozone over Antarctica that scientists reported in 1985, and it was found by people measuring the sky. [3]
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list. [2, 3, 4]
- Leave slack, and people who can improvise. Apollo 13's crew survived in 1970 because engineers on the ground built a filter adapter from bags, cardboard and tape. [2]

## Correlated with

- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (by definition). You can't put odds on a state you never listed, so unforeseeable outcomes have unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](../frameworks/1961-ambiguity-aversion.md)).
- [Known vs unknown unknowns](known-vs-unknown-unknowns.md) (independent). That axis asks whether you know which facts you're missing, and this one asks whether you can list what might happen. A bank's loan model has only two outcomes, repaid or not, yet it can miss a cause nobody thought to measure, like a local factory about to close. The opposite also happens. Apple knew every part that went into the first iPhone in 2007, yet nobody listed a taxi firm run from it, as Uber became two years later.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (independent). Reducible vs irreducible uncertainty asks whether a missing fact can be found, and this axis asks whether you can list what might happen. A foreseeable outcome can be irreducible. You know a rival might cut prices next year, and no research can tell you whether they will. An unforeseeable outcome can be reducible. Nobody listed the hole in the ozone, yet it was there to be measured.
- [Tractable vs intractable options](tractable-vs-intractable-options.md) (independent). These two are easy to confuse, since both can leave you unable to check everything. This axis asks whether you can list everything that could happen once you choose, and no computing helps. Tractable vs intractable options asks how many options you have to choose from, and more computing helps. Go has intractable options, yet every outcome is foreseeable, since its rules decide every position. Choosing between two job offers has tractable options, yet anything could happen after you choose. Designing a new drug is hard on both, with far too many molecules to test and side effects nobody listed.
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (logic). When you can't follow the chain from cause to effect, you can't list where a change will end up, so a fix brings side effects nobody foresaw.
- [Reductionist vs holistic](reductionist-vs-holistic.md) and [Buffered vs cascading](buffered-vs-cascading.md) (logic). The further an action's effects can travel, the more outcomes it can have that nobody meant.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)).
- [Given vs invented options](given-vs-invented-options.md) (bundled). Savage's small world fixes the list of actions as well as the list of states. When outcomes are unforeseeable you often have to invent the options too.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). Clear groups let you list the ways things might turn out. Scattered runs leave outcomes nobody thought to list.

## Citations

[1] [Unanticipated consequences](../frameworks/1936-unanticipated-consequences.md)

[2] [Small and large worlds](../frameworks/1954-small-and-large-worlds.md)

[3] [Incertitude matrix](../frameworks/2007-incertitude-matrix.md)

[4] [Radical uncertainty](../frameworks/2020-radical-uncertainty.md)

[5] [The Monte Carlo method (Metropolis, 1949)](https://doi.org/10.1080/01621459.1949.10483310)
