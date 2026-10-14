# General vs local knowledge

An axis in the [knower](README.md#the-knower) group.

Does the answer rest on facts anyone could look up, or on facts about this place, this firm or this moment? How insulin works is general. Whether this patient has been taking theirs is local, and only someone close to them knows. Friedrich Hayek called this knowledge of the particular circumstances of time and place.

**General**: Let the model answer from what it knows.
- Trust its training data. Facts anyone could look up are already in it.
- Skip the search step. Feeding in documents adds cost, and can add noise when the model already knows the answer.

**Local**: Feed in the local facts or ask someone who has them.
- Search your own records. That puts facts in front of the model that no training data holds.
- Give the model live data. Local facts change daily, so a snapshot goes stale.
- Treat the person on the ground as the source of truth. When the model and the shop manager disagree about the shop, the manager wins.
- Make the model say when it is falling back on general knowledge. A model that answers a local question from general knowledge gives a plausible answer about some other shop.

**Sources.** [Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)

**Correlated with**

- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (bundled). James C. Scott's metis is knowledge that is both local and tacit ([Use of knowledge in society](../frameworks/1945-use-of-knowledge-in-society.md)). But the two come apart. Today's stock levels are local and sit in a spreadsheet. Riding a bike is tacit and works the same in every town.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.
- [Full vs partial observability](full-vs-partial-observability.md) (logic). Local facts are often out of sight for anyone far away. But observability is about what the world hides, while this axis is about who holds the facts. The shop manager can see the stock levels. Head office can't.
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Hayek's point was that local circumstances change every day, so local facts go stale fast.
