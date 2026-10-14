---
type: Axis
title: Even vs lopsided errors
description: Do false alarms and misses cost the same?
group: decision
easy_end: Even
hard_end: Lopsided
sources:
  - resource: /frameworks/1954-signal-detection-theory.md
    title: Signal detection theory
---
# Even vs lopsided errors

An axis in the [decision](index.md#the-decision) group.

Do false alarms and misses cost the same? A smoke alarm that goes off over toast costs you a minute. One that stays quiet in a fire can cost your life, so it should be set to cry wolf. A court leans the other way and would rather free the guilty than jail the innocent. Where to set the bar for saying yes depends on what each mistake costs, not just on how often you're right.

## Actions

**Even**: Maximise accuracy.
- Use the default threshold. A false alarm and a miss cost the same.
- Report one accuracy figure. It tells you all you need when both errors weigh the same.

**Lopsided**: Set the threshold from the costs.
- Put a price on each kind of error. Ask what a miss costs and what a false alarm costs, in the same units.
- Tune the threshold to those prices. A cancer screen should flag far more than it misses.
- Report the two error rates separately, never accuracy alone. A model can score 99% on a rare disease by never flagging anyone.
- Plan for the false alarms. If the model is set to cry wolf, make sure someone can check each alarm quickly.

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.
- [Complete vs incomplete goal](complete-vs-incomplete-goal.md) (logic). A score that counts every mistake the same leaves the costs out. A model tuned for plain accuracy treats a missed cancer and a false scare as equal.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). How much worse a miss is than a false alarm is a value judgement, so people fight over where to set the bar.

## Citations

[1] [Signal detection theory](../frameworks/1954-signal-detection-theory.md)
