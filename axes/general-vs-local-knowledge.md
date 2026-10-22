---
type: Axis
title: General vs local knowledge
description: "General knowledge: the answer rests on facts anyone could look up (e.g. how insulin works). Local knowledge: the answer rests on facts that only people close to it know (e.g. whether this patient takes their insulin)."
group: agent
subgroup: know-how
easy_end: General knowledge
hard_end: Local knowledge
sources:
  - resource: /frameworks/1945-use-of-knowledge-in-society.md
    title: Use of knowledge in society
---
# General vs local knowledge

An axis in the [Know-how](index.md#know-how) set of the [agent](index.md#agent) group.

Does the answer rest on facts anyone could look up, or on facts about this place, this firm or this moment that only people close to it know? How insulin works is general. Whether this patient has been taking theirs is local, and only someone close to them knows. Friedrich Hayek called this knowledge of the particular circumstances of time and place.

## Actions

**General knowledge**: Let the model answer from what it knows.
- Trust its training data. Facts anyone could look up are already in it.
- Skip the search step. Feeding in documents adds cost, and can add noise when the model already knows the answer.

**Local knowledge**: Feed in the local facts or ask someone who has them.
- Search your own records. That puts facts in front of the model that no training data holds.
- Give the model live data. Local facts change daily, so a snapshot goes stale.
- Treat the person on the ground as the source of truth. When the model and the shop manager disagree about the shop, the manager wins.
- Make the model say when it is falling back on general knowledge. A model that answers a local question from general knowledge gives a plausible answer about some other shop.

## Correlated with

- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (bundled). James C. Scott's metis is knowledge that is both local and tacit ([Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)). But the two come apart. Today's stock levels are local and sit in a spreadsheet. Riding a bike is tacit and works the same in every town.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Local facts are often out of sight for anyone far away, so to head office they are reducible doubt. But this axis is about who holds the facts. The shop manager can see the stock levels. Head office can't.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Hayek's point was that local circumstances change every day, so local facts go stale fast.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). When whoever holds the local facts has a stake in your decision, trusting the person on the ground is the wrong move. A shop manager has no reason to miscount the stock. A used car seller has every reason to keep quiet about the gearbox.

## Citations

[1] [Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)
