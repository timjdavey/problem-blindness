---
type: Axis
title: Survivable vs ruinous
description: "Survivable: no single loss can knock you out, so good odds pay off over many tries (e.g. a casino taking many small bets). Ruinous: one bad outcome can take you out of the game for good (e.g. Russian roulette)."
group: performance
subgroup: stakes
easy_end: Survivable
hard_end: Ruinous
sources:
  - resource: /frameworks/2008-fourth-quadrant.md
    title: Fourth quadrant
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
  - resource: /frameworks/2016-ergodicity.md
    title: Ergodicity
---
# Survivable vs ruinous

An axis in the [Stakes](index.md#stakes) set of the [performance](index.md#performance) group.

Could one bad outcome take you out of the game for good, so that good odds over many tries no longer help? If so, the average result over many tries is useless, because you won't get many tries. Russian roulette has good odds and still isn't worth playing.

## Actions

**Survivable**: Maximise the average.
- Run a model that is right more often than not. Losses can be absorbed, so the average is what counts.
- Accept some big misses. You will be around to learn from them.

**Ruinous**: Avoid ruin first and optimise second.
- Put hard limits on what the model can do, whatever its confidence. Limits hold when the model is wrong, and confidence doesn't.
- Have a fallback ready. When the model fails, something safe should take over.
- Never let average accuracy justify a small chance of disaster. A model that is 99.9% right and can wipe you out will get there given enough tries.
- Count tries, not just odds. A one in ten thousand chance per decision is close to certain across a million decisions.

## Correlated with

- [Thin vs fat tails](thin-vs-fat-tails.md) (bundled). The [Fourth quadrant](../frameworks/2008-fourth-quadrant.md) and [Ergodicity](../frameworks/2016-ergodicity.md) both warn that one extreme loss can end the game.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (by definition). Ruin is the worst kind of choice you can't undo.
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (study). Tight systems let small faults cascade into a meltdown ([Normal accidents](../frameworks/1984-normal-accidents.md)).
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). You can't learn from your own ruin, because it only happens once.
- [Additive vs multiplicative returns](additive-vs-multiplicative-returns.md) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin. Peters' coin game never wipes anyone out. It just makes the typical player a little poorer each round ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Even vs lopsided mistakes](even-vs-lopsided-mistakes.md) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.
- [Diversifiable vs single bet](diversifiable-vs-single-bet.md) (logic). Spreading is the main cure for ruin. But bets that fail together can still ruin you, as mortgage bonds did in 2008 ([Portfolio selection](../frameworks/1952-portfolio-selection.md)), and a single bet on lunch harms nobody.
- [Winnable vs no-win](winnable-vs-no-win.md) (independent). This axis is about how bad the worst case is, and that one is about how good the best case is. A tightrope walk has ruin as its worst case and a clean win as its best. Choosing which of two friends to let down is no-win but small.
- [Self-righting vs tipping](self-righting-vs-tipping.md) (logic). A tip you can't climb back from is ruin for whoever depends on the old state.

## Citations

[1] [Fourth quadrant](../frameworks/2008-fourth-quadrant.md)

[2] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)

[3] [Ergodicity](../frameworks/2016-ergodicity.md)
