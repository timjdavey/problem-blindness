---
type: Axis
title: Additive vs multiplicative
description: Do gains and losses add up, so the average outcome is what you can expect, or do they compound, so one player over time can do far worse than the average?
group: decision
easy_end: Additive
hard_end: Multiplicative
sources:
  - resource: /frameworks/2016-ergodicity.md
    title: Ergodicity
---
# Additive vs multiplicative

An axis in the [decision](index.md#the-decision) group.

Do gains and losses add up, so the average outcome is what you can expect, or do they compound, so one player over time can do far worse than the average? In Ole Peters' coin game heads grows your wealth by 50% and tails shrinks it by 40%. The crowd's average rises 5% a round, while a typical player loses about 5% a round. When the crowd's average and one player's long run result differ like this, the game is called non-ergodic.

## Actions

**Additive**: Judge by the average across cases.
- Use expected value per decision as the test. Gains and losses sum, so the average is what you get.
- Compare models on mean return. One bad case costs only itself.

**Multiplicative**: Judge by what one path does over time.
- Simulate long runs of the model's decisions compounding, not one step. A trading model that wins on average per trade can still drain the account.
- Size each bet so a run of losses can't sink you. The Kelly rule sets each stake as a share of what you have, so you never bet the lot.
- Report the typical path, not the average one. The average is pulled up by a lucky few, while the median shows what a typical run gets.
- Watch for losses that shrink your base. Losing half needs a doubling to get back.

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin, and the coin game never wipes anyone out.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). Compounding piles the gains on a lucky few. In the coin game the crowd's average keeps rising only because a handful of players get vastly rich.
- [One-shot vs sequential](one-shot-vs-sequential.md) (by definition). The gap only opens over repeated plays. For a single toss the crowd's average is a fair guide, and the harm builds up toss by toss.
- [Coherent vs incoherent](coherent-vs-incoherent.md) (logic). Compounding splits players' paths apart, so the crowd's average describes almost nobody. That is incoherence across players over time.

## Citations

[1] [Ergodicity](../frameworks/2016-ergodicity.md)
