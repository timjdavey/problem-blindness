---
type: Axis
title: Loose vs tight coupling
description: When one part fails, how fast does it spread?
group: world
easy_end: Loose
hard_end: Tight
sources:
  - resource: /frameworks/1976-loosely-coupled-systems.md
    title: Loosely coupled systems
  - resource: /frameworks/1984-normal-accidents.md
    title: Normal accidents
---
# Loose vs tight coupling

An axis in the [world](index.md#the-world) group.

When one part fails, how fast does it spread? In a loose system there is slack and time to step in. In a tight one, like a power grid or a nuclear plant, one fault can cascade before anyone reacts.

## Actions

**Loose**: Let things fail and fix them.
- Rely on review after the fact. There is time to spot an error and step in before it spreads.
- Automate early. A mistake costs a fix, not a cascade.

**Tight**: Build in slack and breaks before you automate.
- Put circuit breakers, rate limits and kill switches between a model and anything it can trigger. Automated trading learnt this in the 2010 flash crash, when US shares fell about 9% in minutes.
- Don't let models feed each other without a check in between. One model's error becomes the next one's input and grows at each step.
- Add slack where you can. Queues, buffers and delays give people time to see a fault before it spreads.
- Practise the failure. Run drills where a part breaks, so you know the breaks work before you need them.

## Correlated with

- [Slack vs time pressure](slack-vs-time-pressure.md) (by definition). Perrow defines tight coupling as having no slack, so when a tight system fails it hands you a decision with no time ([Normal accidents](../frameworks/1984-normal-accidents.md)).
- [Survivable vs ruinous](survivable-vs-ruinous.md) and [Reversible vs irreversible](reversible-vs-irreversible.md) (study). In [Normal accidents](../frameworks/1984-normal-accidents.md) small faults cascade into a meltdown before anyone can step in.
- [Thin vs fat tails](thin-vs-fat-tails.md) (study). Cascades turn many small faults into rare huge losses, as in the 2010 flash crash.
- [Decomposable vs holistic](decomposable-vs-holistic.md) (independent). Perrow treats how tangled the parts are and how tight the links are as separate traits.

## Citations

[1] [Loosely coupled systems](../frameworks/1976-loosely-coupled-systems.md)

[2] [Normal accidents](../frameworks/1984-normal-accidents.md)
