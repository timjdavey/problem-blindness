---
type: Axis
title: Long vs short predictability horizon
description: How far ahead can you forecast before tiny errors in what you know today grow too large for the forecast to be any use?
group: world
easy_end: Long
hard_end: Short
sources:
  - resource: /frameworks/1963-sensitive-dependence-chaos.md
    title: Sensitive dependence (chaos)
  - resource: /frameworks/1966-clocks-and-clouds.md
    title: Clocks and clouds
---
# Long vs short predictability horizon

An axis in the [world](index.md#the-world) group.

How far ahead can you forecast before tiny errors in what you know today grow too large for the forecast to be any use? A cup pushed off a table is easy to predict. The weather two weeks out is not, even though the physics is simple. Systems where small errors grow this fast are called chaotic.

## Actions

**Long**: Forecast and plan.
- Act on a point forecast. It holds well enough to schedule and commit ahead.
- Check the horizon now and then. Measure how accuracy falls with distance, so you notice if it starts to shrink.

**Short**: Forecast only as far as it holds, then forecast again.
- Find the horizon first. Plot forecast error against how far ahead you look, and stop where it is no better than a naive guess.
- Report a spread of outcomes instead of one number. Running a model further out than its horizon gives you confident noise.
- Judge the model on short range accuracy. A score that blends near and far forecasts hides where it stops working.
- Act in small steps and update as new data arrives. Weather services rerun their models several times a day for this reason.

## Correlated with

- [Deterministic vs statistical](deterministic-vs-statistical.md) (bundled). [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Past the horizon more data barely moves the forecast, so forecasters report a spread instead ([Sensitive dependence](../frameworks/1963-sensitive-dependence-chaos.md)).
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (study). Weather forecasters work inside the horizon and are well calibrated ([Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)). Tetlock's pundits made long range calls and did little better than chance ([Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)).
- [Smooth vs rugged](smooth-vs-rugged.md) (independent). They sound alike. The horizon is about small errors growing over time, while rugged is about many local peaks among the possible answers.

## Citations

[1] [Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)

[2] [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md)
