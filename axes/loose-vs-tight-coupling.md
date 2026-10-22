---
type: Axis
title: Loose vs tight coupling
description: "Loose coupling: when one part fails there is slack and time to step in (e.g. the post, where one late parcel doesn't stop the rest). Tight coupling: a fault spreads to other parts before anyone can react (e.g. a power grid)."
group: world
subgroup: structure
easy_end: Loose coupling
hard_end: Tight coupling
sources:
  - resource: /frameworks/1976-loosely-coupled-systems.md
    title: Loosely coupled systems
  - resource: /frameworks/1984-normal-accidents.md
    title: Normal accidents
---
# Loose vs tight coupling

An axis in the [Structure](index.md#structure) set of the [world](index.md#the-world) group.

When one part fails, is there slack and time to step in, or does the fault spread to other parts before anyone can react? A delayed parcel rarely stops the rest of the post. In a tightly coupled system, like a power grid or a nuclear plant, one fault can cascade before anyone reacts.

## Actions

**Loose coupling**: Let things fail and fix them.
- Rely on review after the fact. There is time to spot an error and step in before it spreads.
- Automate early. A mistake costs a fix, not a cascade.

**Tight coupling**: Build in slack and breaks before you automate.
- Put circuit breakers, rate limits and kill switches between a model and anything it can trigger. Automated trading learnt this in the 2010 flash crash, when US shares fell about 9% in minutes.
- Don't let models feed each other without a check in between. One model's error becomes the next one's input and grows at each step.
- Add slack where you can. Queues, buffers and delays give people time to see a fault before it spreads.
- Practise the failure. Run drills where a part breaks, so you know the breaks work before you need them.

## Correlated with

- [Slack vs time pressure](slack-vs-time-pressure.md) (logic). Perrow's slack is a buffer in the process, while that axis is about time to decide, but the two meet. When a tight system fails it hands you a decision with no time ([Normal accidents](../frameworks/1984-normal-accidents.md)).
- [Survivable vs ruinous](survivable-vs-ruinous.md) and [Reversible vs irreversible](reversible-vs-irreversible.md) (study). In [Normal accidents](../frameworks/1984-normal-accidents.md) small faults cascade into a meltdown before anyone can step in.
- [Thin vs fat tails](thin-vs-fat-tails.md) (study). Cascades turn many small faults into rare huge losses, as in the 2010 flash crash.
- [Decomposable vs tangled](decomposable-vs-tangled.md) (independent). Perrow treats how tangled the parts are and how tight the links are as separate traits.
- [Still vs moving](still-vs-moving.md) (logic). When a tightly coupled system fails, the fault spreads while you are still working out what happened, so the world moves on under you.

## Citations

[1] [Loosely coupled systems](../frameworks/1976-loosely-coupled-systems.md)

[2] [Normal accidents](../frameworks/1984-normal-accidents.md)
