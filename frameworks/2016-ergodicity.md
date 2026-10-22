---
type: Framework
title: Ergodicity
description: >-
  Some bets look good on average across a crowd yet ruin almost everyone who keeps playing them. The test is whether the average over many people at one moment matches the average for one person over time. When it doesn't, expected value is the wrong guide.
date: 2016
cited_date: 2019
creators:
  - Ole Peters
  - Murray Gell-Mann
sources:
  - resource: https://doi.org/10.1038/s41567-019-0732-0
    title: The ergodicity problem in economics
  - resource: https://arxiv.org/abs/1405.0585
    title: Evaluating gambles using dynamics
  - resource: https://ergodicityeconomics.com/lecture-notes/
    title: An introduction to ergodicity economics (lecture notes)
  - resource: https://en.wikipedia.org/wiki/Ergodicity_economics
    title: Ergodicity economics (Wikipedia)
  - resource: https://doi.org/10.1038/s41567-020-01106-x
    title: Economists' views on the ergodicity problem
---
# Ergodicity

**Some bets look good on average across a crowd yet make almost everyone who keeps playing them poorer.**

2016 (2019) · Ole Peters and Murray Gell-Mann · [Key paper](https://doi.org/10.1038/s41567-019-0732-0) · Feeds 2 axes

## The idea

Since the 1650s people have judged a gamble by its expected value. You list every outcome, weight each by its chance and add them up. Ole Peters, a physicist at the London Mathematical Laboratory, thought this hid an assumption that physicists check and economists rarely did. In 2016 he and the Nobel winning physicist Murray Gell-Mann set out the case in a paper on how to judge gambles. In 2019 Peters made it again for a wider audience in Nature Physics.

Imagine a coin game where heads grows your wealth by 50% and tails shrinks it by 40%. If a huge crowd plays one round, the average player gains 5%, so expected value says play. Now follow one person over many rounds. A head and a tail together multiply your wealth by 1.5 times 0.6, which is 0.9. So a typical player loses about 5% a round. The crowd average keeps rising only because a lucky few get vastly rich. When the average over a crowd matches the average for one person over time, a process is called ergodic. This game is not, and nor is most of life where gains and losses compound.

## What goes wrong

The mistake is to judge a repeated, compounding bet by its expected value. You live one path through time, not the average of a million parallel lives. In the coin game nobody is ever wiped out, yet the typical player still grows poorer every round while the crowd's average climbs.

## What to do instead

Popular writing often stretches "non-ergodic" to mean any risk of ruin, but that is a different trait, covered by [Survivable vs ruinous](../axes/survivable-vs-ruinous.md). The better response is to ask what happens to one player who keeps playing. That means looking at the growth rate over time, and staking only a share of what you have each round.

## Examples

### The coin game over 100 rounds

Give a crowd £100 each and have them toss the coin 100 times. The expected wealth at the end is about £13,150. A player who gets 50 heads and 50 tails, the most likely split, ends with about 52p. About 86% of the crowd ends with less than they started with. The average describes almost nobody.

### Kelly betting

In 1956 John Kelly at Bell Labs worked out how much of your money to stake on a repeated bet so that it grows fastest over time. The answer is a fixed share, never everything. In the coin game, staking a quarter of your wealth on each toss turns a losing game into one that grows about 0.6% a round. In the early 1960s Ed Thorp used Kelly's rule to size his bets at blackjack.

### Insurance

On expected value, insurance is a puzzle. The insurer only signs if it expects to profit, so the buyer must expect to lose. In 2015 Peters and Alexander Adamou argued that the puzzle goes away once you look at growth over time. A family that a house fire could ruin grows its wealth faster by paying the premium. An insurer with far more money also grows faster by taking it, because the same loss does far more lasting harm to a small fortune than to a large one.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Additive vs multiplicative returns](../axes/additive-vs-multiplicative-returns.md) | Performance › Stakes | When gains and losses compound, the crowd average and the typical path split apart |
| [Survivable vs ruinous](../axes/survivable-vs-ruinous.md) | Performance › Stakes | Often confused with ergodicity, though the coin game makes players poorer without ever ruining them |

## Further reading

- [The ergodicity problem in economics](https://doi.org/10.1038/s41567-019-0732-0), Ole Peters, *Nature Physics*, 2019. The short version for a wide audience.
- [Evaluating gambles using dynamics](https://arxiv.org/abs/1405.0585), Ole Peters and Murray Gell-Mann, *Chaos*, 2016. The original paper, free on arXiv.
- [An introduction to ergodicity economics](https://ergodicityeconomics.com/lecture-notes/), Ole Peters and Alexander Adamou. Free lecture notes that work through the coin game, Kelly betting and insurance.
- [Ergodicity economics](https://en.wikipedia.org/wiki/Ergodicity_economics) on Wikipedia.
- [Economists' views on the ergodicity problem](https://doi.org/10.1038/s41567-020-01106-x), Jason Doctor, Peter Wakker and Tong Wang, *Nature Physics*, 2020. A reply arguing that economists already knew most of this.
