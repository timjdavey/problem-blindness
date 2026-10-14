---
type: Axis
title: Convex vs concave payoff
description: Does a swing in results help you or hurt you?
group: decision
easy_end: Convex
hard_end: Concave
sources:
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
  - resource: /frameworks/2008-fourth-quadrant.md
    title: Fourth quadrant
---
# Convex vs concave payoff

An axis in the [decision](index.md#the-decision) group.

Does a swing in results help you or hurt you? A drug company testing many compounds loses a little on each failure and gains hugely from one hit, so more variety is good for it. A tightrope walker gains nothing from a lucky gust and can lose everything to an unlucky one. When the downside is small and the upside large, the payoff is called convex. This is a different convex from the one in optimisation, which is about the shape of the search, not the shape of your bet.

## Actions

**Convex**: Try lots of things.
- Run many experiments. Small cheap failures and rare big wins mean more tries pay off.
- Let the model propose wild ideas. A bad idea costs little, and a good one can pay for all the rest.

**Concave**: Cut variance.
- Prefer the dull, predictable model over the clever one with rare failures. The rare failure costs more than the clever gains are worth.
- Add limits that cap the downside. A cap turns an open ended loss into a known one.
- Change your exposure if you can't change the world. Make failures cheap, for example by testing in a sandbox before going live.

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). A bet that can ruin you is the most concave payoff there is.
- [Thin vs fat tails](thin-vs-fat-tails.md) (bundled). Taleb's [Fourth quadrant](../frameworks/2008-fourth-quadrant.md) is a fat tailed world met with a payoff whose shape you don't understand. The tails are the world and the payoff is your exposure to it, so you can change the second even when you can't change the first.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (logic). Cheap two way doors make tinkering convex, because you keep what works and walk back from what fails ([One-way vs two-way doors](../frameworks/2015-one-way-vs-two-way-doors.md)).

## Citations

[1] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)

[2] [Fourth quadrant](../frameworks/2008-fourth-quadrant.md)
