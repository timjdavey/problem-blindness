---
type: Axis
title: Small vs large world
description: "Small: a fixed procedure generates every way things might turn out, so you can compute or sample the outcomes before you choose, even when there are too many to list (e.g. a lottery ticket). Large: no procedure generates the outcomes, so you can't sample them and the result could be something nobody thought to list (e.g. a new product hit by a change in the law)."
group: knower
easy_end: Small
hard_end: Large
sources:
  - resource: /frameworks/1954-small-and-large-worlds.md
    title: Small and large worlds
  - resource: /frameworks/2002-known-and-unknown-unknowns.md
    title: Known and unknown unknowns
  - resource: /frameworks/2020-radical-uncertainty.md
    title: Radical uncertainty
---
# Small vs large world

An axis in the [knower](index.md#the-knower) group.

Can you list every way things might turn out before you choose, or could the result be something nobody thought to list? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. In a small world the outcomes come from a fixed procedure, so you can compute them or run the procedure many times to sample them. In a large world there is no procedure to run, so there is nothing to sample from. Leonard Savage called the first a small world and the second a large one, and said his theory of rational choice only works in the small one.

## Actions

**Small**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so a model can weigh them all.
- Test against the full list. There are only so many cases, so you can check the model handles each one.
- Simulate when the list is too long. Run the procedure many times and count how often each outcome comes up.

**Large**: Leave room for what nobody listed.
- Build a "don't know" or "out of scope" answer into the model. A model forced to pick from a list will pick wrong with confidence.
- Don't trust a simulation to cover it. A simulator can only produce the outcomes someone built into it.
- Flag inputs unlike any in training and route those to a person. That is where the unlisted states show up first.
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list.
- Revisit the list after launch. Log the cases that fit none of your categories and add them.

## Correlated with

- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). You can't put odds on a state you never listed, so a large world has unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](../frameworks/1961-ambiguity-aversion.md)).
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (independent). A hidden fact is a state you know exists but can't see. Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). Small means a procedure generates the outcomes, not that there are few of them. Go is a small world, since the rules fix every position, and still far too big to search. Picking between two job offers is a large world with only two options to check.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)).
- [Choose vs design the options](choose-vs-design-the-options.md) (bundled). Savage's small world fixes the list of actions as well as the list of states. In a large world you often have to invent the options too.

## Citations

[1] [Small and large worlds](../frameworks/1954-small-and-large-worlds.md)

[2] [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md)

[3] [Radical uncertainty](../frameworks/2020-radical-uncertainty.md)
