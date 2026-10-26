---
type: Axis
aliases:
  - Loose vs tight coupling
title: Buffered vs cascading
description: "Buffered system: when one part fails there is slack and time to step in (e.g. the post, where one late parcel doesn't stop the rest). Cascading system: a fault spreads to other parts before anyone can react (e.g. a power grid)."
group: environment
subgroup: stimulus
easy_end: Buffered system
hard_end: Cascading system
sources:
  - resource: /frameworks/1976-loosely-coupled-systems.md
    title: Loosely coupled systems
  - resource: /frameworks/1984-normal-accidents.md
    title: Normal accidents
  - resource: https://www.sec.gov/news/studies/2010/marketevents-report.pdf
    title: Findings regarding the market events of May 6, 2010 (CFTC and SEC, 2010)
  - resource: https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116
    title: The Netflix Simian Army (Izrailevsky, 2011)
---
# Buffered vs cascading

An axis in the [Stimulus](index.md#stimulus) set of the [environment](index.md#environment) group.

When one part fails, does the fault stay where it started, or does it spread from part to part before anyone can step in? A late parcel doesn't stop the rest of the post. In a power grid one line that trips pushes its load onto the next, which trips in turn, and a whole region can go dark in minutes. That chain is a cascading failure. What stops it is a buffer, like slack, spare capacity, a queue or a delay, which keeps one failure local and gives people time to react. Charles Perrow called systems without those buffers tightly coupled ([Normal accidents](../frameworks/1984-normal-accidents.md)), and Karl Weick wrote about the loosely coupled kind ([Loosely coupled systems](../frameworks/1976-loosely-coupled-systems.md)).

## Actions

**Buffered system**: Let things fail and fix them.
- Rely on review after the fact. There is time to spot an error and step in before it spreads. [1, 2]
- Hand work over early. A mistake stays in one part, so it costs a fix, not a cascade. [1]
- Keep the slack. Tightening the links for control or efficiency loses the buffer that keeps one failure local. [1]

**Cascading system**: Build in slack and breaks before you hand over control.
- Put a break between each part and whatever it can set off. Fuses, spending limits and off switches stop one fault from running on. In the 2010 flash crash US share prices plunged 5 to 6% in about four minutes. Regulators then added circuit breakers that pause trading in any share that moves 10% in five minutes. [2, 3]
- Don't let one step feed the next without a check in between. A wrong figure in one team's report becomes the next team's input and grows at each step. [1, 2]
- Add slack before you add safety devices. Queues, buffers and delays give people time to see a fault before it spreads, while each new device is one more link that can fail. [2]
- If the parts are tangled as well, ask whether the system is worth running at all. There, accidents are built in, whatever safety devices you add. [2]
- Practise the failure. Run drills where a part breaks, so you know the breaks work before you need them. [4]

## Correlated with

- [Ample time vs time pressure](ample-time-vs-time-pressure.md) (logic). Perrow's slack is a buffer in the process, while that axis is about time to decide, but the two meet. When a system with no buffers fails it hands you a decision with no time ([Normal accidents](../frameworks/1984-normal-accidents.md)).
- [Survivable vs ruinous](survivable-vs-ruinous.md) and [Reversible vs irreversible](reversible-vs-irreversible.md) (study). In [Normal accidents](../frameworks/1984-normal-accidents.md) small faults cascade into a meltdown before anyone can step in.
- [Self-righting vs tipping](self-righting-vs-tipping.md) (logic). A cascade is a tip that spreads. One part flips and pushes the next one over its own edge.
- [Thin vs fat tails](thin-vs-fat-tails.md) (study). Cascades turn many small faults into rare huge losses, as in the 2010 flash crash.
- [Decomposable vs tangled](decomposable-vs-tangled.md) (independent). Perrow treats how tangled the parts are and how tightly they are coupled as separate traits.
- [Turn-based vs real-time](turn-based-vs-real-time.md) (logic). When a cascading system fails, the fault spreads while you are still working out what happened, so the world moves on under you.

## Citations

[1] [Loosely coupled systems](../frameworks/1976-loosely-coupled-systems.md)

[2] [Normal accidents](../frameworks/1984-normal-accidents.md)

[3] [Findings regarding the market events of May 6, 2010 (CFTC and SEC, 2010)](https://www.sec.gov/news/studies/2010/marketevents-report.pdf)

[4] [The Netflix Simian Army (Izrailevsky, 2011)](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116)
