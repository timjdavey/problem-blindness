---
type: Axis
title: Coherent vs incoherent runs
description: "Coherent runs: every run of the system gives the same spread of results, so the pooled average stands for any run (e.g. a die). Incoherent runs: each run settles somewhere different, so the pooled average describes none of them (e.g. climate model runs that split into warm and cold futures)."
group: environment
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
# Coherent vs incoherent runs

An axis in the [Randomness](index.md#randomness) set of the [environment](index.md#environment) group.

Run the same system several times. Does each run give the same spread of results, so the pooled average stands for any of them? Or does each run settle somewhere different, so the pooled average describes none of them? A run here is a whole outcome with many parts, like one simulation, one week of trips or one snowflake. A die is coherent, since a thousand rolls on Monday look like a thousand on Tuesday. Climate model runs for the UK are incoherent. Most end 7 to 9 degrees warmer, while a few have the Atlantic current fail and end colder than today. Pool them and you get a mild future no run produced. Tim Davey measures how far runs disagree with entropy and calls it incoherence ([Incoherence](../frameworks/2024-incoherence.md)).

This is a test of the runs, not of one spread. A trip with a tight train connection arrives at either 2 hours 10 or 3 hours 10, so the average of 2 hours 34 almost never happens. But every week of trips has the same two humps, so the trip is coherent. Its trap is a lumpy spread, and the fix is to plan for each hump. Also don't mix this up with coherence in probability, where beliefs are coherent if they obey the rules of chance.

## Actions

**Coherent runs**: Trust the average.
- Report the mean and spread, and stop after a few runs. Every run draws from the same spread, so a shopkeeper needs only a few ordinary weeks to know what a normal week looks like. [3]
- Copy what worked. When every run behaves alike a success can be repeated, as NASA landed on the moon five more times after Apollo 11. [2]

**Incoherent runs**: Compare the runs before you pool them.
- Get more than one run and compare them before you trust a result. A single simulation or a model trained once may be one of several very different outcomes. Weather forecasters run the same model many times for this reason. [1, 3]
- Plot each run on its own before you take an average. If the runs settle in different places, the pooled average may be a result no run produced. [3]
- Plan for the outcomes the runs actually reach, not the pooled average. A town that plans for the mild average climate is ready for neither the warm future nor the cold one. [3]
- When you only get one go, prefer the option whose runs agree over the one with the best average. A factory upgrade whose runs average 94 minutes is a bet, not a plan, if four runs land between 96 and 97 and one lands at 84. [3]
- Try a change small and watch how it lands before you spread it. In a complex system success in one place is no guide to the next, so a scheme that worked on one ward still has to prove itself on the next. [2]

## Correlated with

- [Deterministic vs stochastic](deterministic-vs-stochastic.md) (by definition). A deterministic problem gives the same result every run, so it is always coherent. But statistical doesn't mean incoherent. A die varies roll to roll, yet every thousand rolls look alike.
- [Stable vs chaotic](stable-vs-chaotic.md) (logic). Chaos pulls runs that start almost alike far apart. Weather forecasters run the same model many times and read the spread, because no single run can be trusted ([Sensitive dependence](../frameworks/1963-sensitive-dependence-chaos.md)).
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). On a rugged landscape each run stalls on whichever peak is nearest, so runs settle in different places.
- [Additive vs multiplicative returns](additive-vs-multiplicative-returns.md) (logic). Compounding splits paths apart, so the crowd's average describes almost nobody. That is incoherence across players over time.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). With fat tails one extreme case can dominate a run, so two runs of the same system can look very different. But thin tails don't make a system coherent. Each climate run has thin tails, yet the runs still split into a warm group and a cold one.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Pooling incoherent runs gives a lot of data that describes none of them. Raising a child is complex because success with one is no guide to the next ([Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)).
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (by definition). Once the average stops standing for a typical outcome, the next question is whether the outcomes fall into a few clear groups. That axis only applies at the incoherent end.
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). It is the same trap on the answer side. Good answers that differ in kind blend into one nobody would choose, just as runs that split into groups average to a result none of them produced.
- [Self-righting vs tipping](self-righting-vs-tipping.md) (logic). A system with two stable states sends runs that start close together to different places, so the average of the runs describes neither.

## Citations

[1] [Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)

[2] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)

[3] [Incoherence](../frameworks/2024-incoherence.md)
