---
type: Axis
title: Static vs dynamic
description: "Static world: the world waits while you act, so a plan made at the start holds to the end (e.g. a crossword). Dynamic world: the world changes while you act, even if you do nothing, so you have to watch and adjust as you go (e.g. returning a tennis serve)."
group: environment
subgroup: change
easy_end: Static world
hard_end: Dynamic world
sources:
  - resource: /frameworks/1957-open-vs-closed-skills.md
    title: Open vs closed skills
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Static vs dynamic

An axis in the [Change](index.md#change) set of the [environment](index.md#environment) group.

Does the world wait while you act, or does it keep changing even if you do nothing? A crossword sits on the table until you finish it. A tennis serve is on you in half a second, so you have to watch the ball and predict where it will be. The psychologist E. C. Poulton called skills like the first closed and skills like the second open ([Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)). Russell and Norvig asked the same question of AI agents, and called the two ends static and dynamic ([Task environment properties](../frameworks/1995-task-environment-properties.md)).

The question is whether your picture of the world goes stale while you work. A trader's prices move while they think, and a chess player's board doesn't. The same holds for an AI agent. A model fixing a bug in a frozen copy of the code is in a static world. An agent that edits a shared repo or browses sites that update is in a dynamic one. What it read a minute ago may no longer be true when it acts on it.

## Actions

**Static world**: Plan it, then run the plan.
- Write the whole plan up front and carry it out. Nothing will change between steps to make it stale, so a joiner can cut every piece of a bookcase before gluing any.
- Practise on a copy of the task. When the world waits, a dry run tells you how you will do for real, as past papers do for a student.

**Dynamic world**: Look again before every move.
- Work in short loops of look, act, look. A plan written at the start goes stale before the end.
- Check again just before you act, and only go ahead if nothing has moved since. The gap between checking and acting is where mistakes creep in, as when two travel agents sell the same last seat.
- Rehearse in a world that moves while you work, live or simulated. A replay freezes the world, so it hides every failure that comes from acting on old information.
- Aim at where things will be, not where they are. A slow response lands on a world that has already moved on, so a fielder runs to where the ball will come down.
- Practise from many different starts, not one. A routine tuned to one setup breaks when the world moves a different way.

## Correlated with

- [Ample time vs time pressure](ample-time-vs-time-pressure.md) (tension). Time pressure says decide the playbook in advance. A dynamic world says a plan made in advance goes stale. The way out is to plan responses to cues, not a fixed sequence of moves. The two still come apart. A bomb with a timer sits still and gives you minutes. A yacht crossing an ocean is in a dynamic world for weeks, with hours to make each call.
- [Stationary vs drifting](stationary-vs-drifting.md) (independent). Drift is about what you learnt going stale over months. This axis is about what you saw going stale within one task. The rules of tennis haven't drifted in decades, yet every rally moves.
- [Standalone vs sequential](standalone-vs-sequential.md) (logic). In a sequential problem your own choices change what comes next. In a dynamic world things change even if you do nothing. Catching one ball is a single choice in a dynamic world. Chess by post is a long chain of choices, and the board waits for you.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (bundled). Russell and Norvig's harder worlds have other agents in them, and an opponent is the most common reason the world won't wait ([Task environment properties](../frameworks/1995-task-environment-properties.md)). But a surfer's wave moves and isn't trying to beat anyone.
- [Stable vs chaotic](stable-vs-chaotic.md) (independent). A ball in flight follows simple physics and is easy to predict, yet you still have to act before it lands. Poulton's paper was about exactly this, the prediction a skilled movement needs ([Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)).
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (logic). In a tightly coupled system a fault spreads faster than you can react, so the world moves on while you are still working out what happened.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (logic). Gentile split out settings that are still during each attempt but differ from one attempt to the next, like a billiards table. That variety is the "count by kind of case" problem, and it needs varied practice even when the world waits ([Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)).

## Citations

[1] [Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)

[2] [Task environment properties](../frameworks/1995-task-environment-properties.md)
