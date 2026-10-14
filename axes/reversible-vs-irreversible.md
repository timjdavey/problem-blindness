---
type: Axis
title: Reversible vs irreversible
description: "Reversible: if it goes wrong you can undo it cheaply and try again (e.g. a new recipe). Irreversible: once it is done you are stuck with it (e.g. selling the family home)."
group: decision
easy_end: Reversible
hard_end: Irreversible
sources:
  - resource: /frameworks/1973-tame-vs-wicked-problems.md
    title: Tame vs wicked problems
  - resource: /frameworks/2015-one-way-vs-two-way-doors.md
    title: One-way vs two-way doors
---
# Reversible vs irreversible

An axis in the [decision](index.md#the-decision) group.

If it goes wrong, can you undo it cheaply and try again, or are you stuck with it? Trying a new recipe is a two way door. Selling the family home or cutting off a leg is a one way door.

## Actions

**Reversible**: Move fast and let the model act.
- Ship small changes often and learn from what breaks. You can roll back.
- Let agents act without sign off. A mistake costs an undo, not a disaster.

**Irreversible**: Slow down and put a person at the door.
- Require human sign off for actions that can't be undone. Deleting data, sending money and emailing customers are the usual ones.
- Give agents a dry run mode. They show what they would do, and a person approves it.
- Turn one way doors into two way ones where you can. Staging, soft deletes and a delay before a send all buy you an undo.
- Gate only the actions that are hard to undo. Gating everything trains people to click approve without reading.

## Correlated with

- [Survivable vs ruinous](survivable-vs-ruinous.md) (by definition). All ruin is irreversible, but not every irreversible choice ruins you.
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (study). In [Normal accidents](../frameworks/1984-normal-accidents.md) faults cascade into damage that can't be undone before anyone can step in.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (bundled). [Rittel and Webber](../frameworks/1973-tame-vs-wicked-problems.md) note you can't learn by trial and error when each try leaves a mark.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (bundled). Simon's [non-programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md) are new and carry high stakes.
- [One-shot vs sequential](one-shot-vs-sequential.md) (opposite). A chain of moves usually gives you a chance to correct course. Rittel and Webber's "one-shot operation" means a choice that can't be undone, so it belongs here rather than on that axis.
- [Private vs accountable](private-vs-accountable.md) (logic). Bezos argues one-way doors deserve a slow process with many views ([One-way vs two-way doors](../frameworks/2015-one-way-vs-two-way-doors.md)), and that brings scrutiny.
- [Test vs watch](test-vs-watch.md) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Spread vs single bet](spread-vs-single-bet.md) (independent). Both are ways to avoid staking everything on one guess. This axis spreads your tries across time, and that one spreads them across options. A venture fund is spread but each cheque is gone once written, and a lunch spot is a single bet you can undo.

## Citations

[1] [Tame vs wicked problems](../frameworks/1973-tame-vs-wicked-problems.md)

[2] [One-way vs two-way doors](../frameworks/2015-one-way-vs-two-way-doors.md)
