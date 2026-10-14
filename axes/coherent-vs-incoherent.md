---
type: Axis
title: Coherent vs incoherent
description: "Coherent: the average of all outcomes represents the typical outcome (e.g. the mean height of a population closely matches the median and mode). Incoherent: each instance of a system looks very different and never like the average (e.g. climate tipping points)."
group: world
easy_end: Coherent
hard_end: Incoherent
sources:
  - resource: /frameworks/1963-sensitive-dependence-chaos.md
    title: Sensitive dependence (chaos)
  - resource: /frameworks/2002-simple-complicated-and-complex.md
    title: Simple, complicated and complex
  - resource: /frameworks/2024-incoherence.md
    title: Incoherence
---
# Coherent vs incoherent

An axis in the [world](index.md#the-world) group.

If you run the same thing again, do the runs land on the same spread of results, so the average stands for a typical run, or does each run settle somewhere different, so the average describes none of them? A die is random but coherent, since every roll draws from the same spread. A trip with a tight train connection is incoherent. Arrivals pile up at 2 hours 10 and 3 hours 10, and the average of 2 hours 34 almost never happens. Tim Davey measures the gap with entropy and calls it incoherence.

## Actions

**Coherent**: Pool the runs and trust the average.
- Report the mean and spread across runs. Every run draws from the same spread, so the pooled figure is a fair guide to the next one.
- A few runs are enough to judge the model. More runs only tighten the error bar.

**Incoherent**: Look at each run before you pool them.
- Rerun the same eval or agent task with different seeds, and compare the runs, not just one score. If they disagree, a single benchmark number hides it.
- Plot each run on its own before you take an average. If the runs split into groups, the average may be a result none of them produced.
- Plan for the outcomes that actually happen. Book the taxi for 2 hours 10 and rebook if you miss the train, rather than booking for the average.
- When you only get one go, prefer the option whose runs agree over the one with the best average. A factory upgrade that averages 94 minutes but only hits it one run in five is a bet, not a plan.
- Design to fit the range, not the average. In 1950 not one of 4,063 US Air Force pilots was average on all ten key sizes, so cockpits were made to adjust.

## Correlated with

- [Deterministic vs statistical](deterministic-vs-statistical.md) (by definition). A deterministic problem gives the same result every run, so it is always coherent. But statistical doesn't mean incoherent. A die varies every roll yet stays coherent.
- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (logic). Chaos pulls runs that start almost alike far apart. Weather forecasters run the same model many times and read the spread, because no single run can be trusted ([Sensitive dependence](../frameworks/1963-sensitive-dependence-chaos.md)).
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). On a rugged landscape each run stalls on whichever peak is nearest, so runs settle in different places.
- [Additive vs multiplicative](additive-vs-multiplicative.md) (logic). Compounding splits paths apart, so the crowd's average describes almost nobody. That is incoherence across players over time.
- [Thin vs fat tails](thin-vs-fat-tails.md) (independent). A fat tailed process can still be coherent if every run draws from the same wild spread. Incoherence is about runs disagreeing, not about any one run being extreme.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Pooling incoherent runs gives a lot of data that describes none of them. Raising a child is complex because success with one is no guide to the next ([Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)).
- [Clustered vs scattered](clustered-vs-scattered.md) (by definition). Once runs disagree, the next question is whether they fall into a few clear groups. That axis only applies at the incoherent end.

## Citations

[1] [Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)

[2] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)

[3] [Incoherence](../frameworks/2024-incoherence.md)
