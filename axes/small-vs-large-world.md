---
type: Axis
title: Small vs large world
description: "Small world: a fixed procedure generates every way things might turn out, so you can compute or sample the outcomes before you choose, even when there are too many to list (e.g. a lottery ticket). Large world: no procedure generates the outcomes, so you can't sample them and the result could be something nobody thought to list (e.g. a new product hit by a change in the law)."
group: information
subgroup: uncertainty
easy_end: Small world
hard_end: Large world
sources:
  - resource: /frameworks/1954-small-and-large-worlds.md
    title: Small and large worlds
  - resource: /frameworks/2002-known-and-unknown-unknowns.md
    title: Known and unknown unknowns
  - resource: /frameworks/2020-radical-uncertainty.md
    title: Radical uncertainty
---
# Small vs large world

An axis in the [Uncertainty](index.md#uncertainty) set of the [information](index.md#information) group.

Is there a fixed procedure that generates every way things might turn out, so you can work out or sample the outcomes before you choose? Or could the result be something nobody thought to list? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. Go has more positions than anyone could list, yet its rules generate every one. A large world has no such procedure, so there is nothing to sample from. Leonard Savage called the first a small world and the second a large one, and said his theory of rational choice only works in the small one.

## Actions

**Small world**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so a model can weigh them all.
- Test against the full list. There are only so many cases, so you can check the model handles each one.
- Simulate when the list is too long. Run the procedure many times and count how often each outcome comes up.

**Large world**: Leave room for what nobody listed.
- Build a "don't know" or "out of scope" answer into the model. A model forced to pick from a list will pick wrong with confidence.
- Don't trust a simulation to cover it. A simulator can only produce the outcomes someone built into it.
- Flag inputs unlike any in training and route those to a person. That is where the unlisted states show up first.
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list.
- Revisit the list after launch. Log the cases that fit none of your categories and add them.

## Correlated with

- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (by definition). You can't put odds on a state you never listed, so a large world has unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](../frameworks/1961-ambiguity-aversion.md)).
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (independent). A hidden fact is a state you know exists but can't see. Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). Small means a procedure generates the outcomes, not that there are few of them. Go is a small world, since the rules fix every position, and still far too big to search. Picking between two job offers is a large world with only two options to check.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)).
- [Given vs invented options](given-vs-invented-options.md) (bundled). Savage's small world fixes the list of actions as well as the list of states. In a large world you often have to invent the options too.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). Clear groups let you list the ways things might turn out. Scattered runs leave outcomes nobody thought to list.

## Citations

[1] [Small and large worlds](../frameworks/1954-small-and-large-worlds.md)

[2] [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md)

[3] [Radical uncertainty](../frameworks/2020-radical-uncertainty.md)
