---
type: Axis
title: Antifragile vs wears out
description: "Antifragile: each stress leaves the system stronger than before, up to a point (e.g. a muscle after a workout). Wears out: each stress uses up some of the system's life, until it fails (e.g. metal fatigue in an aircraft)."
group: world
subgroup: stimulus
easy_end: Antifragile
middle: Robust
hard_end: Wears out
sources:
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
---
# Antifragile vs wears out

An axis in the [Stimulus](index.md#stimulus) set of the [world](index.md#the-world) group.

After many pushes, has the system itself changed for the better or for the worse? A muscle comes back from a workout a little stronger. Bone does the same, and it withers without load. Astronauts lose 1 to 1.5% of their bone density for every month they spend in space. Nassim Nicholas Taleb called things that gain from stress antifragile ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)). In the middle sit robust things, which stress leaves the same. A computer program is the same after a billion runs as after one.

At the other end, each stress uses up some of the system's life. The de Havilland Comet was the first jet airliner. On 10 January 1954 one broke up in the air off the island of Elba, and another was lost three months later. Investigators put a Comet fuselage in a water tank and pumped it up and down, once for each flight. It split open after 3,057 cycles. Every climb had stretched the metal around the corners of a window or hatch a little, and the damage added up until a crack ran. This is called metal fatigue.

This axis differs from [Self-righting vs tipping](self-righting-vs-tipping.md). That one asks where the system settles after one push. This one asks how the system has changed after many. The Comet's skin sprang back after every flight, so it was self-righting, and it was still wearing out.

Better for the system is not always better for you. Bacteria are antifragile to antibiotics, since each course kills the weak and leaves the hardy to breed. Weeds do the same to weedkiller. When the system is the thing you are fighting, its gain from your push is your loss, so treat it as the hard end.

## Actions

**Antifragile**: Let small stresses in and feed them back.
- Turn every failure into a test. A codebase where each bug adds a test that catches it gets stronger with each bug.
- Don't shield the system from every small shock. Netflix built a tool called Chaos Monkey that switches off its own servers at random during working hours, so engineers find the weak spots while they are at their desks.
- Watch the dose. A workout builds muscle and too heavy a lift tears it, so the gain only holds up to a point.

**Wears out**: Budget the stress and count the cycles.
- Count uses, not time. The Comet's life was set by how many flights it made, not by how many years it had flown.
- Treat a held out test set as something that wears. Each time you check a model against it and tune, the set tells you a little less about new data. Keep a fresh set that nobody has looked at.
- Count the load on the people in the loop. Every false alarm wears down the person who checks alerts, until they start waving real ones through. Cap the alarms each reviewer sees.
- Plan the upkeep and retire things before they fail, not after.

## Correlated with

- [Self-righting vs tipping](self-righting-vs-tipping.md) (independent). A muscle rights itself after one workout and grows stronger over months. A bridge rights itself after every lorry and still wears out.
- [Stationary vs drifting](stationary-vs-drifting.md) (independent). Drift happens on its own, while this change is caused by the stress. A muscle you stop using shrinks, which looks like drift, but the cause is the missing load.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Bacteria have no aim, yet each course of antibiotics leaves them harder to kill. An adversary is a system that gains from your rule on purpose.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). When the tails are fat, an exposure that gains from wild swings is worth more than one that only survives them. That is the idea behind the barbell ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)).

## Citations

[1] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)
