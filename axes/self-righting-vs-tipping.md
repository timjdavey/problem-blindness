---
type: Axis
title: Self-righting vs tipping
description: "Self-righting: after a push the system goes back to where it was, like a ball in a bowl (e.g. body temperature). Tipping point: past some push the system flips into a new state and stays there, like a ball on a hilltop (e.g. a clear lake turning murky)."
group: world
subgroup: stimulus
easy_end: Self-righting
middle: Malleable
hard_end: Tipping point
sources:
  - resource: /frameworks/1973-resilience-and-stability.md
    title: Resilience and stability
  - resource: /frameworks/2001-critical-transitions.md
    title: Critical transitions
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
---
# Self-righting vs tipping

An axis in the [Stimulus](index.md#stimulus) set of the [world](index.md#the-world) group.

When something pushes the system, does it go back to where it was or stay where it was pushed? Or does it flip into a new state and stay there? Picture a ball. In a bowl it rolls back to the bottom. On a flat table it stays wherever you leave it. On a hilltop a small nudge sends it off the edge, and it won't roll back up. Materials show the same three cases. Elastic things spring back, plastic things stay bent and brittle things snap.

This is a question about the system, not about you. [Reversible vs irreversible](reversible-vs-irreversible.md) asks whether you can undo your own move. Deleting a paragraph in Word is reversible, because you can press undo. But the document never puts the paragraph back by itself, so it sits in the middle of this axis. We call that middle malleable. It takes whatever shape you push it into and keeps it.

There are two ways to be self-righting, and Taleb lumps them together ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)). A robust system barely moves when pushed, like your body holding its temperature on a hot day. A resilient system moves a long way and still comes back, like a forest growing back after a fire. In 1973 the ecologist C. S. Holling split these two apart ([Resilience and stability](../frameworks/1973-resilience-and-stability.md)). He said speed of return was one thing, and the size of push a system can take before it flips was another.

At the far end sit systems with a tipping point. A shallow lake fed more and more fertiliser from farms stays clear for years, then turns murky in a season. Cutting the fertiliser back to where it was doesn't bring the clear water back. You have to cut it much further. This is called hysteresis, and it means stopping the push is not the same as undoing it ([Critical transitions](../frameworks/2001-critical-transitions.md)).

## Actions

**Self-righting**: Let small errors wash out.
- Automate freely. The system absorbs a bad output and returns to normal, so one mistake costs little.
- Measure your errors directly, not by watching the system. A system that absorbs your mistakes also hides them, so you can be wrong for a long time without seeing it.

**Malleable**: Check the state, not just the action.
- Nothing will fix a bad change for you, so look at what the system holds after each step. A model that edits files or records leaves every mistake in place until someone finds it.
- Keep an undo trail. The system won't recover, so recovery has to come from you.

**Tipping point**: Stay well clear of the edge.
- Find the thresholds before you push. Ask what level of load, traffic or nudging has flipped this kind of system before.
- Keep a wide margin. The flip is fast and the way back is long, so the cost of getting close is far bigger than it looks.
- Watch how fast the system recovers from small pushes. Recovery slows as a system nears its tipping point, and that slowing is one of the few warnings you get ([Critical transitions](../frameworks/2001-critical-transitions.md)).
- Don't plan on reversing the input. A recommender that has nudged a user base into a new habit won't undo it by switching the nudge off.
- Test the effect of many small nudges together, not one at a time. Each nudge passes an offline test on its own. The flip comes from the sum.

## Correlated with

- [Stable vs chaotic](stable-vs-chaotic.md) (independent). Both are about small pushes growing, but in different ways. Chaos means small differences grow all the time, while the system stays the same kind of system. A tipping point means a system that holds steady until one threshold, then jumps. Day to day weather is chaotic, yet global temperature came back within a few years of the 1991 Pinatubo eruption cooling it by about half a degree. A shallow lake is easy to forecast on either side of its threshold and still tips.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (independent). That axis is about your undo button and this one is about the system. A Word document is reversible and malleable. A felled forest can't be un-felled, yet it grows back. A lake whose fertiliser you can stop at any time still stays murky.
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (logic). A system with two stable states sends runs that start close together to different places, so the average of the runs describes neither.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). A tipping system has a few stable states, so its runs fall into a few clear groups.
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (logic). A cascade in a tight system is a tip that spreads from one part to the next.
- [Stationary vs drifting](stationary-vs-drifting.md) (independent). In drift the rules slowly change. In a tip the rules stay fixed and the state jumps. Slang drifts with no tipping point, and the lake tips while the chemistry stays the same.
- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). A tip you can't climb back from is ruin for whoever depends on the old state.
- [Antifragile vs wears out](antifragile-vs-wears-out.md) (independent). This axis asks where the system settles after one push. That one asks how the system itself has changed after many. A bridge rights itself after every lorry and still wears out.

## Citations

[1] [Resilience and stability](../frameworks/1973-resilience-and-stability.md)

[2] [Critical transitions](../frameworks/2001-critical-transitions.md)

[3] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)
