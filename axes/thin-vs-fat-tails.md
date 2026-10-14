---
type: Axis
title: Thin vs fat tails
description: When results are statistical, how extreme can a single one get?
group: world
easy_end: Thin
hard_end: Fat
sources:
  - resource: /frameworks/2007-mediocristan-vs-extremistan.md
    title: Mediocristan vs Extremistan
  - resource: /frameworks/2008-fourth-quadrant.md
    title: Fourth quadrant
---
# Thin vs fat tails

An axis in the [world](index.md#the-world) group.

When results are statistical, how extreme can a single one get? Heights are thin tailed, so the average tells you a lot. Floods, pandemics and startup returns are fat tailed, so one outlier can outweigh everything else and past averages mislead you.

## Actions

**Thin**: Trust the average.
- Use mean error on a test set as your guide. With thin tails a few odd cases won't change the picture.
- Size the test set by the usual rules. A few thousand cases pin the average down well, because no single case can drag it far.

**Fat**: Plan around the worst case, not the average.
- Report tail metrics, like the worst 1% of errors or the largest single loss. A good average on a calm test set tells you nothing about the next crash.
- Stress test with extreme cases you build on purpose. The real extremes are too rare to turn up in your data by chance.
- Cap exposure with limits on size or spend. No single prediction should be able to do unbounded harm.
- Don't read a long calm run as proof of safety. Banks in 2007 had years of quiet data, and it said nothing about 2008.

## Correlated with

- [Deterministic vs statistical](deterministic-vs-statistical.md) (by definition). This axis sits inside that one. It only applies near the statistical end, because a deterministic problem has no spread to have tails.
- [Survivable vs ruinous](survivable-vs-ruinous.md) (bundled). The [Fourth quadrant](../frameworks/2008-fourth-quadrant.md) and [Ergodicity](../frameworks/2016-ergodicity.md) both warn that one extreme outcome can end the game.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). The events that matter most in a fat tailed world are rare, so your record holds few of them or none. But card fraud is fat tailed and still has millions of cases. Fat tails make the cases that matter rare, not the data overall.
- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). Tail odds can't be read off a calm past, which is how banks in 2008 came to treat [uncertainty as risk](../frameworks/1921-risk-vs-uncertainty.md).
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (study). In [Normal accidents](../frameworks/1984-normal-accidents.md) small faults cascade through a tight system into huge losses.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). [Reflexivity](../frameworks/1987-reflexivity.md) and the [bank run](../frameworks/1948-self-fulfilling-prophecy.md) show beliefs and facts feeding each other into booms and crashes.
- [Additive vs multiplicative](additive-vs-multiplicative.md) (logic). Compounding piles the gains on a lucky few. In Peters' coin game the crowd's average keeps rising only because a handful of players get vastly rich ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Small vs large world](small-vs-large-world.md) (logic). The worst outcomes are often ones nobody listed, which is what Taleb means by a black swan.
- [Convex vs concave payoff](convex-vs-concave-payoff.md) (bundled). The [Fourth quadrant](../frameworks/2008-fourth-quadrant.md) is a fat tailed world met with a payoff whose shape you don't understand. You can't change the tails, but you can often change your exposure to them.

## Citations

[1] [Mediocristan vs Extremistan](../frameworks/2007-mediocristan-vs-extremistan.md)

[2] [Fourth quadrant](../frameworks/2008-fourth-quadrant.md)
