# Survivable vs ruinous

An axis in the [decision](README.md#the-decision) group.

Could one bad outcome take you out of the game for good? If so, the average result over many tries is useless, because you won't get many tries. Russian roulette has good odds and still isn't worth playing.

**Survivable**: Maximise the average.
- Run a model that is right more often than not. Losses can be absorbed, so the average is what counts.
- Accept some big misses. You will be around to learn from them.

**Ruinous**: Avoid ruin first and optimise second.
- Put hard limits on what the model can do, whatever its confidence. Limits hold when the model is wrong, and confidence doesn't.
- Have a fallback ready. When the model fails, something safe should take over.
- Never let average accuracy justify a small chance of disaster. A model that is 99.9% right and can wipe you out will get there given enough tries.
- Count tries, not just odds. A one in ten thousand chance per decision is close to certain across a million decisions.

**Sources.** [Fourth quadrant](../frameworks/2008-fourth-quadrant.md), [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md), [Ergodicity](../frameworks/2016-ergodicity.md)

**Correlated with**

- [Thin vs fat tails](thin-vs-fat-tails.md) (bundled). The [Fourth quadrant](../frameworks/2008-fourth-quadrant.md) and [Ergodicity](../frameworks/2016-ergodicity.md) both warn that one extreme loss can end the game.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (by definition). Ruin is the worst kind of choice you can't undo.
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (study). Tight systems let small faults cascade into a meltdown ([Normal accidents](../frameworks/1984-normal-accidents.md)).
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). You can't learn from your own ruin, because it only happens once.
- [Additive vs multiplicative](additive-vs-multiplicative.md) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin. Peters' coin game never wipes anyone out. It just makes the typical player a little poorer each round ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Convex vs concave payoff](convex-vs-concave-payoff.md) (logic). A bet that can ruin you is the most concave payoff there is.
- [Even vs lopsided errors](even-vs-lopsided-errors.md) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.
