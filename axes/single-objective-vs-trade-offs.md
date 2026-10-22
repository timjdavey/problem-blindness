---
type: Axis
title: Single objective vs trade-offs
description: "Single objective: there is one thing to get right (e.g. the fastest route home). Trade-offs: several goals pull against each other, so a gain on one costs you on another (e.g. price against safety in a new car)."
group: decision
subgroup: goal
easy_end: Single objective
hard_end: Trade-offs
sources:
  - resource: /frameworks/1976-decisions-with-multiple-objectives.md
    title: Decisions with multiple objectives
  - resource: /frameworks/2000-problem-typology.md
    title: Problem typology
  - resource: /frameworks/2017-need-for-interpretability.md
    title: Need for interpretability
  - resource: /frameworks/1997-taboo-trade-offs.md
    title: Taboo trade-offs
  - resource: /frameworks/2007-super-wicked-problems.md
    title: Super wicked problems
---
# Single objective vs trade-offs

An axis in the [Goal](index.md#goal) set of the [decision](index.md#the-decision) group.

Is there one thing to get right, or several goals that pull against each other, so a gain on one costs you on another? The fastest route home is one objective. A new car trades price against safety, comfort and running costs. The best cars form a front, where you can't gain on one goal without losing on another, and a car between two of them is usually on or near it too. What matters is the clash, not the count. A cook who wants a soup that is hot, cheap and quick has three goals, but if none costs the others anything they act as one.

Most trade offs can be priced. You can say what an hour of travel is worth to you. Some can't. A hospital budget trades money against lives, and most people refuse to put a price on a child. Alan Fiske and Philip Tetlock called these taboo trade offs.

The most common clash is between now and later. A pension trades spending today against income in 40 years. A climate policy trades costs now against harm to people not yet born. How much less a future gain counts than one today is called the discount rate, and it is just the weight between the two goals. Kelly Levin and colleagues count a habit of putting too little weight on the future as one trait of [super wicked problems](../frameworks/2007-super-wicked-problems.md).

This axis asks how many parts the goal has. It doesn't ask who sets the weights, which is [Shared vs contested values](shared-vs-contested-values.md), or whether good answers can be blended, which is [Convergent vs divergent](convergent-vs-divergent.md). One person buying a car has trade-offs, nobody to argue with and good answers that blend.

## Actions

**Single objective**: Optimise the one number.
- Use it as both the training target and the release gate. When there is one goal, the score and the job are the same.
- Compare models on it directly. Higher is better, so there is nothing to argue about.

**Trade-offs**: Make the trade offs plain.
- Track each objective as its own metric. A model tuned on one blended score hides which goal it gave up.
- Show decision makers the best trade offs on offer. Lay out the options where you can't gain on one goal without losing on another, and let them pick.
- Agree the weights before training, not after. Weights set after you see results tend to favour the model you already like.
- Set a floor for each objective. No gain on one should push another below what is acceptable.
- Treat sacred values as rules the model can't break, not weights it can trade. A loss function that puts a price on a life will be found and quoted.

## Correlated with

- [Decomposable vs tangled](decomposable-vs-tangled.md) (bundled). In Ackoff's [messes](../frameworks/1974-messes.md) a gain in one part turns up as a loss in another.
- [Well vs ill-structured](well-vs-ill-structured.md) (bundled). Simon's house design and Jonassen's [dilemmas](../frameworks/2000-problem-typology.md) are hard to pin down because several wants pull against each other. But buying a car has many objectives and is still well structured once you set the weights.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). Once there are several goals, different people weigh them differently. Stirling calls this [ambiguity](../frameworks/2007-incertitude-matrix.md). But one person buying a car has many objectives and nobody to argue with. And it runs the other way. Two towns that each want the bridge have one objective each, yet they rank the sites in opposite orders.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). With no single score there is no simple check that one answer beats another.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (opposite). Simon's own model of satisficing works this way. With several goals, people set a floor on each and take the first option that clears them all ([Satisficing](../frameworks/1956-satisficing.md)).
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (bundled). Doshi-Velez and Kim ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap in the score. But a car buyer who writes down every want and sets the weights has many objectives and a direct measure.
- [Private vs accountable](private-vs-accountable.md) (study). In 2000 Tetlock asked people to judge a hospital manager who could spend $1m on a child's liver transplant or on equipment and salaries. Choosing the equipment after long thought scored 5.71 for outrage out of 7. Saving the child at once scored 1.51. Even being seen to weigh a sacred value counts against you, so a choice you must defend in public pushes the trade off out of sight ([Taboo trade-offs](../frameworks/1997-taboo-trade-offs.md)).
- [Convergent vs divergent](convergent-vs-divergent.md) (independent). Both give many good answers, but a trade off between goals gives answers that differ only in degree, and there a blend of two good ones is also good. A car buyer has trade-offs and convergent answers. A best man has one goal and divergent answers. Choosing between two job offers is both, since salary pulls against location and the two jobs differ in kind.
- [Winnable vs no-win](winnable-vs-no-win.md) (bundled). Tetlock's tragic trade-offs, such as choosing which of two sick boys to treat, set one sacred value against another, so some loss is certain ([Taboo trade-offs](../frameworks/1997-taboo-trade-offs.md)). But a pilot with no engines has one objective and still can't win.

## Citations

[1] [Decisions with multiple objectives](../frameworks/1976-decisions-with-multiple-objectives.md)

[2] [Problem typology](../frameworks/2000-problem-typology.md)

[3] [Need for interpretability](../frameworks/2017-need-for-interpretability.md)

[4] [Taboo trade-offs](../frameworks/1997-taboo-trade-offs.md)

[5] [Super wicked problems](../frameworks/2007-super-wicked-problems.md)
