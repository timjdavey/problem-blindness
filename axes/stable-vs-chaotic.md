---
type: Axis
title: Stable vs chaotic
aliases:
  - Long vs short predictability horizon
description: "Lyapunov stable: small errors in what you know today stay small, so you can forecast far ahead (e.g. the tides). Chaotic: tiny errors grow fast, so a forecast soon becomes useless (e.g. the weather two weeks out)."
group: environment
subgroup: change
easy_end: Lyapunov stable
hard_end: Chaotic
sources:
  - resource: /frameworks/1963-sensitive-dependence-chaos.md
    title: Sensitive dependence (chaos)
  - resource: /frameworks/1966-clocks-and-clouds.md
    title: Clocks and clouds
---
# Stable vs chaotic

An axis in the [Change](index.md#change) set of the [environment](index.md#environment) group.

How far ahead can you forecast before tiny errors in what you know today grow too large for the forecast to be any use? The tides can be forecast years ahead. The weather two weeks out can't, even though the physics is well understood. Systems where small errors grow this fast are called chaotic. Edward Lorenz found this in 1961, when rounding one number in his weather model to three decimal places gave a different forecast. Systems where small errors stay small are called Lyapunov stable, after the Russian mathematician Aleksandr Lyapunov. Stable here means the errors stay small, not that the world stays the same. A stable system can still drift, as [Durable vs perishable lessons](durable-vs-perishable-lessons.md) explains.

How far ahead a forecast stays useful is called the predictability horizon. It is years for the tides and about two weeks for the weather.

## Actions

**Lyapunov stable**: Forecast and plan.
- Act on a single best forecast. It holds well enough to schedule and commit ahead, as a port does with its tide tables. [2]
- Spend effort on a sharper model. Where small errors stay small, better data and a finer model buy a better forecast. [1]
- Check the horizon now and then. Measure how accuracy falls with distance, since many systems taken for clocks are more cloudlike than they look. [2]

**Chaotic**: Forecast only as far as it holds, then forecast again.
- Find the horizon first. Plot forecast error against how far ahead you look, and stop where it is no better than a naive guess. A single score that blends near and far hides that point. [1]
- Give a spread of outcomes instead of one number. A single forecast past the horizon is confident noise, however expert the forecaster. [1, 2]
- Don't buy a bigger model to see further. Past the horizon a bigger computer and a finer model barely move the forecast. [1]
- Act in small steps you can change, and update as new data arrives. Past the horizon a plan built on an old forecast is a guess. [2]

## Correlated with

- [Deterministic vs stochastic](deterministic-vs-stochastic.md) (bundled). [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Past the horizon more data barely moves the forecast, so forecasters report a spread instead ([Sensitive dependence](../frameworks/1963-sensitive-dependence-chaos.md)).
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (study). Weather forecasters work inside the horizon and are well calibrated ([Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)). Tetlock's pundits made calls years ahead, which took years to grade, and did little better than chance ([Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)).
- [Smooth vs rugged](smooth-vs-rugged.md) (independent). Both are about small differences growing large, but in different places. Chaos is about errors growing over time as a system runs. Rugged is about a small change to an answer making a big change to how good it is, at one fixed moment.
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (logic). Chaos pulls runs that start almost alike far apart, so past the horizon the runs disagree and their average describes none of them.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (independent). Both make forecasts go bad with time, and both sound like the world being unsteady, so they get mixed up. Chaos means small errors grow while the rules stay fixed. Drift means the rules themselves change. Weather is chaotic, yet the physics behind it never moves. Slang drifts, but nothing about it is chaotic.
- [Turn-based vs real-time](turn-based-vs-real-time.md) (independent). A ball in flight follows simple physics and is easy to predict, yet it won't wait while you work out where it will land.
- [Self-righting vs tipping](self-righting-vs-tipping.md) (independent). Both are about small pushes growing, but in different ways. Chaos means small differences grow all the time. A tipping point means a system that holds steady until one threshold and then jumps. Day to day weather is chaotic, yet global temperature came back within a few years of the 1991 Pinatubo eruption cooling it. A shallow lake is easy to forecast on either side of its threshold and still tips.

## Citations

[1] [Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)

[2] [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md)
