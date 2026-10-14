# Small vs large world

An axis in the [knower](README.md#the-knower) group.

Can you list every way things might turn out before you choose? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. Leonard Savage called the first a small world and the second a large one, and said his theory of rational choice only works in the small one.

**Small**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so a model can weigh them all.
- Test against the full list. There are only so many cases, so you can check the model handles each one.

**Large**: Leave room for what nobody listed.
- Build a "don't know" or "out of scope" answer into the model. A model forced to pick from a list will pick wrong with confidence.
- Flag inputs unlike any in training and route those to a person. That is where the unlisted states show up first.
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list.
- Revisit the list after launch. Log the cases that fit none of your categories and add them.

**Sources.** [Small and large worlds](../frameworks/1954-small-and-large-worlds.md), [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md), [Radical uncertainty](../frameworks/2020-radical-uncertainty.md)

**Correlated with**

- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). You can't put odds on a state you never listed, so a large world has unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](../frameworks/1961-ambiguity-aversion.md)).
- [Full vs partial observability](full-vs-partial-observability.md) (independent). Observability asks whether you can see a state you know exists. Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)).
- [Choose vs design the options](choose-vs-design-the-options.md) (bundled). Savage's small world fixes the list of actions as well as the list of states. In a large world you often have to invent the options too.
