# Single vs multiple objectives

An axis in the [decision](README.md#the-decision) group.

Is there one thing to get right, or several that pull against each other? The fastest route home is one objective. A new car trades price against safety, comfort and running costs, so there are many good answers, not one.

**Single**: Optimise the one number.
- Use it as both the training target and the release gate. When there is one goal, the score and the job are the same.
- Compare models on it directly. Higher is better, so there is nothing to argue about.

**Multiple**: Make the trade offs plain.
- Track each objective as its own metric. A model tuned on one blended score hides which goal it gave up.
- Show decision makers the best trade offs on offer. Lay out the options where you can't gain on one goal without losing on another, and let them pick.
- Agree the weights before training, not after. Weights set after you see results tend to favour the model you already like.
- Set a floor for each objective. No gain on one should push another below what is acceptable.

**Sources.** [Decisions with multiple objectives](../frameworks/1976-decisions-with-multiple-objectives.md), [Problem typology](../frameworks/2000-problem-typology.md), [Need for interpretability](../frameworks/2017-need-for-interpretability.md)

**Correlated with**

- [Decomposable vs holistic](decomposable-vs-holistic.md) (bundled). In Ackoff's [messes](../frameworks/1974-messes.md) a gain in one part turns up as a loss in another.
- [Well-posed vs ill-posed](well-posed-vs-ill-posed.md) (bundled). Simon's house design and Jonassen's [dilemmas](../frameworks/2000-problem-typology.md) are hard to pin down because several wants pull against each other. But buying a car has many objectives and is still well posed once you set the weights.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). Once there are several goals, different people weigh them differently. Stirling calls this [ambiguity](../frameworks/2007-incertitude-matrix.md). But one person buying a car has many objectives and nobody to argue with.
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (logic). With no single score there is no simple check that one answer beats another.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (opposite). With several goals there is a set of good trade offs and no one best answer, so you have to settle for good enough.
- [Complete vs incomplete goal](complete-vs-incomplete-goal.md) (bundled). Doshi-Velez and Kim ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap in the score. But a car buyer who writes down every want and sets the weights has many objectives and a complete goal.
- [Commensurable vs incommensurable values](commensurable-vs-incommensurable-values.md) (by definition). The question only comes up with more than one objective. Setting weights, as Keeney and Raiffa do, assumes every goal can be turned into one score.
