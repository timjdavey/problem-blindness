---
type: Axis
title: Additive vs multiplicative returns
description: "Additive returns: gains and losses add up, so the average is what you can expect (e.g. betting the same £10 every round). Multiplicative returns: gains and losses compound, so one player over time can do far worse than the average (e.g. betting half your savings every round)."
group: performance
subgroup: stakes
easy_end: Additive returns
hard_end: Multiplicative returns
sources:
  - resource: /frameworks/2016-ergodicity.md
    title: Ergodicity
---
# Additive vs multiplicative returns

An axis in the [Stakes](index.md#stakes) set of the [performance](index.md#performance) group.

Do gains and losses add up, so the average outcome is what you can expect, or do they compound, so one player over time can do far worse than the average? In Ole Peters' coin game heads grows your wealth by 50% and tails shrinks it by 40%. The crowd's average rises 5% a round, while a typical player loses about 5% a round. When the crowd's average and one player's long run result differ like this, the game is called non-ergodic.

## Actions

**Additive returns**: Judge by the average across cases.
- Use expected value per decision as the test. Gains and losses sum, so the average is what you get. [1]
- Don't pay to insure a loss you can easily absorb. The insurer only signs if it expects to profit, so on average the buyer loses. [1]

**Multiplicative returns**: Judge by what one path does over time.
- Play out a long run of choices as they compound, not a single step. A trader who wins on average per trade can still drain the account. [1]
- Size each bet so a run of losses can't sink you. The Kelly rule sets each stake as a share of what you have, so you never bet the lot. [1]
- Report the typical path, not the average one. In the coin game over 100 rounds the average ends near £13,150 from a £100 start, while the most likely result is about 52p. [1]
- Watch for losses that shrink your base. In the coin game a 50% gain after a 40% loss still leaves you 10% down. [1]
- Pay to insure against a loss that would cut deep, even at a price above its average cost. Peters and Adamou argued that a family a house fire would ruin grows richer over time by paying the premium. [1]

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin, and the coin game never wipes anyone out.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). Compounding piles the gains on a lucky few. In the coin game the crowd's average keeps rising only because a handful of players get vastly rich.
- [Standalone vs sequential](standalone-vs-sequential.md) (by definition). Compounding is a sequential problem, since each bet's result sets the stake for the next. Bet the same fixed sum each round and the rounds stand alone, so the crowd's average is a fair guide.
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (logic). Compounding splits players' paths apart, so the crowd's average describes almost nobody. That is incoherence across players over time.

## Citations

[1] [Ergodicity](../frameworks/2016-ergodicity.md)
