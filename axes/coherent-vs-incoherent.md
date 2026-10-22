---
type: Axis
title: Coherent vs incoherent
description: "Coherent runs: every run of the system gives the same spread of results, so the pooled average stands for any run (e.g. a die). Incoherent runs: each run settles somewhere different, so the pooled average describes none of them (e.g. climate model runs that split into warm and cold futures)."
group: world
subgroup: randomness
easy_end: Coherent runs
hard_end: Incoherent runs
sources:
  - resource: /frameworks/1963-sensitive-dependence-chaos.md
    title: Sensitive dependence (chaos)
  - resource: /frameworks/2002-simple-complicated-and-complex.md
    title: Simple, complicated and complex
  - resource: /frameworks/2024-incoherence.md
    title: Incoherence
---
# Coherent vs incoherent

An axis in the [Randomness](index.md#randomness) set of the [world](index.md#the-world) group.

Run the same system several times. Does each run give the same spread of results, so the pooled average stands for any of them? Or does each run settle somewhere different, so the pooled average describes none of them? A run here is a whole outcome with many parts, like one simulation, one week of trips or one snowflake. A die is coherent, since a thousand rolls on Monday look like a thousand on Tuesday. Climate model runs for the UK are incoherent. Most end 7 to 9 degrees warmer, while a few have the Atlantic current fail and end colder than today. Pool them and you get a mild future no run produced. Tim Davey measures how far runs disagree with entropy and calls it incoherence ([Incoherence](../frameworks/2024-incoherence.md)).

This is a test of the runs, not of one spread. A trip with a tight train connection arrives at either 2 hours 10 or 3 hours 10, so the average of 2 hours 34 almost never happens. But every week of trips has the same two humps, so the trip is coherent. Its trap is a lumpy spread, and the fix is to plan for each hump. Also don't mix this up with coherence in probability, where beliefs are coherent if they obey the rules of chance.

## Actions

**Coherent runs**: Trust the average.
- Report the mean and spread. Every run draws from the same spread, so the pooled figures are a fair guide to the next run.
- A few runs are enough to judge the model. More runs only tighten the error bar.

**Incoherent runs**: Compare the runs before you pool them.
- Rerun the same eval or agent task with different seeds, and compare the runs, not just one score. If they disagree, a single benchmark number hides it.
- Plot each run on its own before you take an average. If the runs settle in different places, the pooled average may be a result no run produced.
- Plan for the outcomes the runs actually reach, not the pooled average.
- When you only get one go, prefer the option whose runs agree over the one with the best average. A factory upgrade whose runs average 94 minutes is a bet, not a plan, if four runs land near 97 and one lands at 84.

## Correlated with

- [Deterministic vs statistical](deterministic-vs-statistical.md) (by definition). A deterministic problem gives the same result every run, so it is always coherent. But statistical doesn't mean incoherent. A die varies roll to roll, yet every thousand rolls look alike.
- [Stable vs chaotic](stable-vs-chaotic.md) (logic). Chaos pulls runs that start almost alike far apart. Weather forecasters run the same model many times and read the spread, because no single run can be trusted ([Sensitive dependence](../frameworks/1963-sensitive-dependence-chaos.md)).
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). On a rugged landscape each run stalls on whichever peak is nearest, so runs settle in different places.
- [Additive vs multiplicative](additive-vs-multiplicative.md) (logic). Compounding splits paths apart, so the crowd's average describes almost nobody. That is incoherence across players over time.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). With fat tails one extreme case can dominate a run, so two runs of the same system can look very different. But thin tails don't make a system coherent. Each climate run has thin tails, yet the runs still split into a warm group and a cold one.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Pooling incoherent runs gives a lot of data that describes none of them. Raising a child is complex because success with one is no guide to the next ([Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)).
- [Clustered vs scattered](clustered-vs-scattered.md) (by definition). Once the average stops standing for a typical outcome, the next question is whether the outcomes fall into a few clear groups. That axis only applies at the incoherent end.
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). It is the same trap on the answer side. Good answers that differ in kind blend into one nobody would choose, just as runs that split into groups average to a result none of them produced.

## Citations

[1] [Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)

[2] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)

[3] [Incoherence](../frameworks/2024-incoherence.md)
