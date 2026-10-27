---
type: Axis
title: Diversifiable vs single bet
description: "Diversifiable: you can split your stake across several options at once, so no one choice has to be right (e.g. a pension fund holding many shares). Single bet: you can only take one course of action, so everything rides on it (e.g. which job offer to accept)."
group: actions
subgroup: options
easy_end: Diversifiable
hard_end: Single bet
sources:
  - resource: /frameworks/1952-portfolio-selection.md
    title: Portfolio selection
  - resource: /frameworks/1999-ecological-rationality.md
    title: Ecological rationality
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
  - resource: https://doi.org/10.1145/1879831.1879836
    title: Parallel prototyping leads to better design results, more divergence, and increased self-efficacy (Dow, 2010)
---
# Diversifiable vs single bet

An axis in the [Options](index.md#options) set of the [actions](index.md#actions) group.

Can you split your stake across several options at once, or does everything ride on one? A pension fund holds hundreds of shares, so no single one has to be right. You can only accept one job offer, and a bridge can only be built in one town. Being able to undo a choice is another way to avoid staking everything on one guess. That spreads your tries across time, and this axis spreads them across options. But spreading only helps when the bets can fail on their own. Harry Markowitz showed that bets which rise and fall together are close to one bet ([Portfolio selection](../frameworks/1952-portfolio-selection.md)).

## Actions

**Diversifiable**: Back several and let the results pick.
- Run several attempts side by side, so no one of them has to be right. A publisher signs many books because it can't tell which will sell. [1]
- Check that the bets aren't secretly one bet. Loans in one housing market fail together. So do advisers who all read the same report, or answers drawn from one model. [1]
- Barbell when the tails are fat. Put most of the stake on the safe option and a small slice on a few wild ones. The safe part caps the loss and the wild slice keeps the chance of a big win. [3]
- Split evenly when you can't tell the options apart. In a 2009 test, none of 14 optimising models was reliably better than equal shares. [2]

**Single bet**: Put the effort into choosing, and make the bet smaller where you can.
- Spread the drafts, then commit to one action. Designers who made several ads side by side before any feedback made better ads than those who refined one at a time. An architect can sketch ten designs, but only one gets built. [4]
- Pick the option that holds up across scenarios, not the one with the best forecast. Ask what happens if things go very badly or very well. If a big surprise would ruin you, a good forecast won't save you. [3]
- Turn one big bet into several small ones where you can, such as a pilot in one region first. Harm grows faster than the shock. Ten jumps from one metre do no harm, but one jump from ten metres can break your legs. [3]

## Correlated with

- [Reversible vs irreversible](reversible-vs-irreversible.md) (independent). An index fund is spread and you can sell it tomorrow. A venture fund is spread too, but each cheque is gone once written. A lunch spot is a single bet you can undo, and selling the family home is one you can't. Each can stand in for the other, so a single bet you can't undo is the worst corner.
- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). Spreading is the main cure for ruin, since no one loss can knock you out. But they aren't the same. Mortgage bonds in 2008 looked spread across thousands of loans and still failed together ([Portfolio selection](../frameworks/1952-portfolio-selection.md)), and a single bet on lunch harms nobody.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). When the tails are fat a few wild bets carry most of the upside, so you need to be able to back several. A barbell puts a small slice on them and keeps the rest safe ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)).
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). Spreading is not blending. Halfway between a funny speech and a moving one is a bad speech, but you can draft both and keep one. A barbell beats the middling option because it spreads across a fork instead of blending it.
- [Interventional vs observational](interventional-vs-observational.md) (logic). A fair test needs you to do more than one thing at once. With only one economy there is no control group. But the two come apart, since a portfolio spreads without testing anything.
- [Standalone vs sequential](standalone-vs-sequential.md) (independent). This axis asks whether you can back several options at once. That one asks whether each choice shapes the next. A [bandit](../frameworks/1933-multi-armed-bandit.md) makes one pull at a time and each pull shapes what it tries next, while a fund can back a hundred shares and treat each as its own call.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). A budget can be split between rival groups, so each gets some of what it wants. A bridge can't, so someone has to lose.

## Citations

[1] [Portfolio selection](../frameworks/1952-portfolio-selection.md)

[2] [Ecological rationality](../frameworks/1999-ecological-rationality.md)

[3] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)

[4] [Parallel prototyping leads to better design results, more divergence, and increased self-efficacy (Dow, 2010)](https://doi.org/10.1145/1879831.1879836)
