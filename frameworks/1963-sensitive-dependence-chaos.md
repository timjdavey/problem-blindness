---
type: Framework
title: Sensitive dependence (chaos)
description: >-
  In some systems a tiny change at the start grows into a huge change later. Long range forecasts fail even when you know the rules perfectly. This is called the butterfly effect.
date: 1963
creators:
  - Edward Lorenz
sources:
  - resource: "https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2"
    title: Deterministic nonperiodic flow
  - resource: https://en.wikipedia.org/wiki/Butterfly_effect
    title: Butterfly effect (Wikipedia)
  - resource: https://en.wikipedia.org/wiki/Ensemble_forecasting
    title: Ensemble forecasting (Wikipedia)
  - resource: https://doi.org/10.1063/pt.eike.hsbz
    title: The real butterfly effect and maggoty apples
---
# Sensitive dependence (chaos)

**In some systems a tiny change at the start grows into a huge change later. Long range forecasts fail even when you know the rules perfectly.**

1963 · Edward Lorenz · [Original paper](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2) · Feeds 2 axes

## The idea

Most of us assume that if you know the rules of a system and where it starts, you can say where it will end up. For a planet or a cannonball that is true. Some systems don't work like that. In them a tiny gap between two starting points doubles, then doubles again, until the two paths have nothing in common. We call this sensitive dependence on initial conditions, and systems that behave this way are called chaotic.

The framework sorts problems by how fast small errors grow. Where errors stay small, prediction is a matter of effort. Where they grow, there is a horizon past which no amount of effort helps. The rules can be simple and known with no randomness at all, and the forecast still fails. The MIT weather scientist Edward Lorenz showed this in 1963 with a model of just three equations.

## What goes wrong

The mistake is to treat a chaotic problem as if it were only complicated. You buy a bigger computer and build a finer model, and the long range forecast barely moves.

## What to do instead

The better response is to stop asking for one answer and ask for a range. Forecasters now run the same model many times from slightly different starts and look at how far the results spread. This is called ensemble forecasting, and the spread tells you how far ahead you can trust what you see.

## Examples

### Lorenz's rounding error

In 1961 Lorenz was running a small weather model on a computer at MIT. To see one run again, he restarted it halfway with a number typed from the printout. The printout showed 0.506, but the computer had stored 0.506127. He went for a coffee, and when he came back the new run had drifted far from the old one. A difference in the fourth decimal place had produced a different weather pattern within about two months of model time.

### The two week wall

Weather forecasts have gained roughly one extra day of useful range every decade since the 1980s. Yet Lorenz's work suggests a hard limit of around two weeks for day to day weather, however good the tools get. That is why nobody can tell you if it will rain on your wedding day three months out.

### A snooker break

A single snooker shot is easy to predict from its speed and angle. The break is different. Each collision magnifies any tiny error in the angle of the cue, so after a few bounces the balls end up somewhere no player could have planned. The rules are the same in both cases, but the number of collisions decides whether the outcome can be forecast.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) | Environment › Randomness | Runs from nearly the same start drift apart until they have nothing in common |
| [Stable vs chaotic](../axes/stable-vs-chaotic.md) | Environment › Change | Tiny starting errors grow until there is a horizon past which no forecast helps |

## Further reading

- [Deterministic nonperiodic flow](https://doi.org/10.1175/1520-0469(1963)020%3C0130:DNF%3E2.0.CO;2), Edward Lorenz, *Journal of the Atmospheric Sciences*, 1963. The original paper with the three equation model, free from the American Meteorological Society.
- [Butterfly effect](https://en.wikipedia.org/wiki/Butterfly_effect) on Wikipedia, which tells the story of the rounding error.
- [Ensemble forecasting](https://en.wikipedia.org/wiki/Ensemble_forecasting) on Wikipedia, on running the same model from many slightly different starts.
- [The real butterfly effect and maggoty apples](https://doi.org/10.1063/pt.eike.hsbz), Tim Palmer, *Physics Today*, 2024. Argues that Lorenz's real butterfly effect sets a finite limit on weather forecasts, and that AI forecasting models miss it.
