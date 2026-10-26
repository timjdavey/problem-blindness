---
type: Axis
title: Antifragile vs wears out
description: "Antifragile: each stress leaves the system stronger than before, up to a point (e.g. a muscle after a workout). Wears out: each stress uses up some of the system's life, until it fails (e.g. metal fatigue in an aircraft)."
group: environment
subgroup: stimulus
easy_end: Antifragile
middle: Robust
hard_end: Wears out
sources:
  - resource: /frameworks/2012-fragile-robust-and-antifragile.md
    title: Fragile, robust and antifragile
  - resource: https://www.faa.gov/lessons_learned/transport_airplane/accidents/G-ALYV
    title: De Havilland DH-106 Comet 1 (FAA)
  - resource: https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116
    title: The Netflix Simian Army (Izrailevsky, 2011)
  - resource: https://digitalassets.jointcommission.org/api/public/content/f65e5c9df2b94000a99445e0a7877007
    title: Medical device alarm safety in hospitals (The Joint Commission, 2013)
  - resource: https://doi.org/10.1126/science.aaa9375
    title: "The reusable holdout: preserving validity in adaptive data analysis (Dwork, 2015)"
---
# Antifragile vs wears out

An axis in the [Stimulus](index.md#stimulus) set of the [environment](index.md#environment) group.

After many pushes, has the system itself changed for the better or for the worse? A muscle comes back from a workout a little stronger. Bone does the same, and it withers without load. Astronauts lose 1 to 1.5% of their bone density for every month they spend in space. Nassim Nicholas Taleb called things that gain from stress antifragile ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)). In the middle sit robust things, which stress leaves the same. A computer program is the same after a billion runs as after one.

At the other end, each stress uses up some of the system's life. The de Havilland Comet was the first jet airliner. On 10 January 1954 one broke up in the air off the island of Elba, and another was lost three months later. Investigators put a Comet fuselage in a water tank and pumped it up and down, once for each flight. It split open after 3,057 cycles. Every climb had stretched the metal around the corners of a window or hatch a little, and the damage added up until a crack ran. This is called metal fatigue.

This axis differs from [Self-righting vs tipping](self-righting-vs-tipping.md). That one asks where the system settles after one push. This one asks how the system has changed after many. The Comet's skin sprang back after every flight, so it was self-righting, and it was still wearing out.

Better for the system is not always better for you. Bacteria are antifragile to antibiotics, since each course kills the weak and leaves the hardy to breed. Weeds do the same to weedkiller. When the system is the thing you are fighting, its gain from your push is your loss, so treat it as the hard end.

## Actions

**Antifragile**: Let small stresses in and feed them back.
- Turn every failure into a check that catches it next time. Flying gets safer with each crash because the findings change the rules for every airline, and a codebase gets stronger when each bug adds a test. [1]
- Don't shield the system from every small shock. Netflix built a tool called Chaos Monkey that switches off its own servers at random during working hours, so engineers find the weak spots while they are at their desks. [1, 3]
- Keep spare cash or capacity ready to use when a shock comes. A household with cash to invest can buy cheaply in a crash and end up better off. [1]
- Watch the dose. A workout builds muscle and too heavy a lift tears it, so the gain only holds up to a point. [1]

**Robust**: Rely on it, within the limits it was built for.
- Keep a buffer that absorbs the shocks you expect. A household with six months of cash keeps the house after a lost job and ends up about where it started. [1]
- Check it once and rely on the result. A robust thing is the same after many stresses, so a check passed on the first day still holds after the thousandth use. [1]
- Know the biggest shock it was built for, because past that it may simply break. Fukushima's sea wall was built for a tsunami of under six metres, and in 2011 a wave of about 14 metres flooded the backup generators. [1]

**Wears out**: Budget the stress and count the cycles.
- Count uses, not time. The Comet that broke up off Elba had flown for less than two years, but its 1,290 pressurised flights had worn out its fuselage. [2]
- Set a life in cycles from tests that match the real thing, and repair or replace before it runs out. The Comet's fatigue test used a fuselage already strengthened by an earlier overload test. It lasted 16,000 cycles, while planes in service cracked at about 1,000. [2]
- Treat a test as something that wears. Each time you check against it and adjust, it tells you a little less about new cases. A student who keeps resitting the same mock paper learns that paper, so keep a fresh one back. [5]
- Count the load on the people who check, and cut the alarms that ask nothing of them. An estimated 85 to 99% of hospital alarms need no action, so staff grow numb and miss real ones. [4]

## Correlated with

- [Self-righting vs tipping](self-righting-vs-tipping.md) (independent). A muscle rights itself after one workout and grows stronger over months. A bridge rights itself after every lorry and still wears out.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (independent). Drift happens on its own, while this change is caused by the stress. A muscle you stop using shrinks, which looks like drift, but the cause is the missing load.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Bacteria have no aim, yet each course of antibiotics leaves them harder to kill. An adversary is a system that gains from your rule on purpose.
- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). When the tails are fat, an exposure that gains from wild swings is worth more than one that only survives them. That is the idea behind the barbell ([Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)).

## Citations

[1] [Fragile, robust and antifragile](../frameworks/2012-fragile-robust-and-antifragile.md)

[2] [De Havilland DH-106 Comet 1 (FAA)](https://www.faa.gov/lessons_learned/transport_airplane/accidents/G-ALYV)

[3] [The Netflix Simian Army (Izrailevsky, 2011)](https://netflixtechblog.com/the-netflix-simian-army-16e57fbab116)

[4] [Medical device alarm safety in hospitals (The Joint Commission, 2013)](https://digitalassets.jointcommission.org/api/public/content/f65e5c9df2b94000a99445e0a7877007)

[5] [The reusable holdout: preserving validity in adaptive data analysis (Dwork, 2015)](https://doi.org/10.1126/science.aaa9375)
