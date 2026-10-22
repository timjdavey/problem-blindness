---
type: Axis
title: Even vs lopsided mistakes
description: "Even mistakes: a false alarm and a miss cost about the same (e.g. deciding whether to take an umbrella). Lopsided mistakes: one mistake is far worse than the other (e.g. a smoke alarm that stays quiet in a fire)."
group: performance
subgroup: stakes
easy_end: Even mistakes
hard_end: Lopsided mistakes
sources:
  - resource: /frameworks/1954-signal-detection-theory.md
    title: Signal detection theory
---
# Even vs lopsided mistakes

An axis in the [Stakes](index.md#stakes) set of the [performance](index.md#performance) group.

Do a false alarm and a miss cost about the same, or is one mistake far worse than the other? A smoke alarm that goes off over toast costs you a minute. One that stays quiet in a fire can cost your life, so it should be set to cry wolf. A court leans the other way and would rather free the guilty than jail the innocent. Where to set the bar for saying yes depends on what each mistake costs, not just on how often you're right.

## Actions

**Even mistakes**: Maximise accuracy.
- Use the default threshold. A false alarm and a miss cost the same.
- Report one accuracy figure. It tells you all you need when both errors weigh the same.

**Lopsided mistakes**: Set the threshold from the costs.
- Put a price on each kind of error. Ask what a miss costs and what a false alarm costs, in the same units.
- Tune the threshold to those prices. A cancer screen should flag far more than it misses.
- Report the two error rates separately, never accuracy alone. A model can score 99% on a rare disease by never flagging anyone.
- Plan for the false alarms. If the model is set to cry wolf, make sure someone can check each alarm quickly.

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). A score that counts every mistake the same leaves the costs out. A model tuned for plain accuracy treats a missed cancer and a false scare as equal.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). How much worse a miss is than a false alarm is a value judgement, so people fight over where to set the bar.

## Citations

[1] [Signal detection theory](../frameworks/1954-signal-detection-theory.md)
