---
type: Framework
title: Cohesion
description: >-
  When runs of a system disagree, they can still fall into a few clear groups, like snowflakes that are all different yet each a plate, a column or a star. Clear groups let you plan for each one and spot early which you are in. Runs with no groups give you nothing to latch onto.
date: 2023
creators:
  - Tim J. Davey
sources:
  - resource: https://doi.org/10.3390/e25121605
    title: "Cohesion: a measure of organisation and epistemic uncertainty of incoherent ensembles"
  - resource: https://timjdavey.com/cohesion/
    title: Self-organisation, and how to measure it (primer)
  - resource: https://github.com/timjdavey/incoherence
    title: incoherence (code on GitHub)
  - resource: https://www.snowcrystals.com/morphology/morphology.html
    title: Guide to snowflakes
  - resource: https://en.wikipedia.org/wiki/Self-organization
    title: Self-organization (Wikipedia)
---
# Cohesion

**When runs of a system disagree, they can still fall into a few clear groups, like snowflakes that are each a plate, a column or a star.**

2023 · Tim J. Davey · [Original paper](https://doi.org/10.3390/e25121605) · Feeds 1 axis

## The idea

No two snowflakes are alike, yet anyone can tell a snowflake at a glance. Each one is different, but they all follow the same few patterns. In 2023 Tim Davey set out a way to measure that in the journal Entropy. He called it cohesion, and it goes with his later measure of [incoherence](2024-incoherence.md).

A system organises itself when nothing outside it imposes the pattern. Snowflakes do this twice. Every flake has six arms, each symmetrical down its middle. And flakes settle into a few distinct kinds, so a plate is far more like another plate than like a column.

To measure this, Davey runs a system many times and joins every pair of runs with a line. If the runs fall into tight groups, the line lengths bunch into a few clear sizes. The entropy of those lengths shows how organised the system is. Diamonds and water both score 1, the top of the scale, because each turns out the same every time. Every diamond is the same lattice and every glass of water is the same even jumble. So cohesion only means something once a system is incoherent and its runs disagree. The trait this sorts on is whether runs that disagree still fall into a few clear groups.

## What goes wrong

The mistake is to treat every spread of results as one fuzzy cloud.

## What to do instead

The better response is to check whether the runs fall into groups. If they do, plan for each group and watch for the signs that tell them apart. Davey puts it this way. Incoherence tells you how far you can trust frequentist statistics, which pool the runs. Cohesion tells you how far you can trust Bayesian statistics, which update your belief about which group you are in as evidence comes in.

## Examples

### Bentley's snowflakes

From 1885 Wilson Bentley photographed more than 5,000 snowflakes and never found two the same. Each flake grows by feeding on itself, since wherever it sticks out it catches more vapour and grows faster. Average 24 flakes together and you get a blur, so snowflakes are incoherent. Yet every one is clearly a snowflake.

### Nakaya's shapes

In the 1930s the physicist Ukichiro Nakaya grew snowflakes in a lab at different temperatures. He found they form thin plates, columns and needles, or the familiar stars, depending on the conditions. The shapes don't blend smoothly into each other. They fall into a few distinct kinds.

### UK climate

Davey works through a thought experiment. Say you must prepare the UK for climate change and you commission a climate model. Most runs have the UK 7 to 9 degrees warmer. A few have the Atlantic current that warms Britain shutting down, leaving it 7 to 10 degrees colder than today. The runs fall into two clear groups, so planners can prepare for each, and just three temperature readings can rule out a whole group at once. If the runs had been scattered with no pattern, they could only split the budget across a vague spread.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) | Environment › Randomness | Measures whether runs that disagree still fall into a few clear groups |

## Further reading

- [Cohesion: a measure of organisation and epistemic uncertainty of incoherent ensembles](https://doi.org/10.3390/e25121605), Timothy Davey, *Entropy*, 2023. The original paper, free to read.
- [Self-organisation, and how to measure it](https://timjdavey.com/cohesion/), Tim J. Davey. A primer with no equations, using climate change as the example.
- [incoherence](https://github.com/timjdavey/incoherence) on GitHub, Tim J. Davey. The code behind both the cohesion and incoherence papers, including the `ensemblepy` library.
- [Guide to snowflakes](https://www.snowcrystals.com/morphology/morphology.html), Kenneth Libbrecht, *SnowCrystals.com*. How snowflake shapes depend on temperature, including the Nakaya diagram.
- [Self-organization](https://en.wikipedia.org/wiki/Self-organization) on Wikipedia.
