---
type: Axis
title: Reducible vs irreducible uncertainty
description: "Reducible uncertainty: the facts that would settle your doubt exist and can be found (e.g. waiting on a blood test). Irreducible uncertainty: no amount of fact finding would settle it (e.g. whether a rival cuts prices next year)."
group: information
subgroup: uncertainty
easy_end: Reducible uncertainty
hard_end: Irreducible uncertainty
sources:
  - resource: /frameworks/1955-johari-window.md
    title: Johari window
  - resource: /frameworks/1986-uncertainty-vs-equivocality.md
    title: Uncertainty vs equivocality
  - resource: /frameworks/1989-complex-problem-solving.md
    title: Complex problem solving
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
  - resource: /frameworks/2001-puzzles-vs-mysteries.md
    title: Puzzles vs mysteries
  - resource: /frameworks/2002-known-and-unknown-unknowns.md
    title: Known and unknown unknowns
---
# Reducible vs irreducible uncertainty

An axis in the [Uncertainty](index.md#uncertainty) set of the [information](index.md#information) group.

Is your doubt a gap that more data or research could close, or would no amount of fact finding settle it? Waiting on a blood test is reducible doubt, since the result will settle it. The most common reducible doubt is a fact that already exists but is hidden from you, like the other hands in poker. When nothing that matters is hidden, as on a chess board, you have no doubt of this kind and can act on what you see.

Three kinds of doubt are irreducible. Some is pure chance, like the next roll of a die. Some hangs on choices people haven't made yet, like whether a rival will cut prices next year. Some is a clash over what the facts mean, where people read the same evidence in different ways. That last kind sits close to [Shared vs contested values](shared-vs-contested-values.md), since the fight is often over what matters. If your doubt is reducible you should go and gather data. If it's irreducible you should hedge instead.

## Actions

**Reducible uncertainty**: Go and get the data.
- Label more cases. Focus labelling on the cases the model is least sure of, which is called active learning.
- Ask the user the missing question before acting. One question often settles what no model could guess.
- Keep track of what you believe about the hidden facts. Update it as each new clue comes in, like a doctor narrowing a diagnosis.
- Say what you can't see. A model that answers as if it had the full picture hides its biggest weakness.
- Test the model on cases where the key evidence is missing. That is how it will meet many real ones.

**Irreducible uncertainty**: Stop paying for more data and hedge instead.
- Report a spread, not a single answer. More training won't shrink the doubt, so hiding it only misleads.
- Make the decision cope with either result instead of staking it on one. Where you can, back several options at once, as under [Diversifiable vs single bet](diversifiable-vs-single-bet.md).
- Use an ensemble to tell the two kinds of doubt apart. Models that disagree point to doubt more data could fix. Models that agree on a wide spread point to doubt it can't.
- Check where the doubt comes from. If it hangs on a choice nobody has made yet, no data will settle it, so plan for each way the choice could go.

## Correlated with

- [Deterministic vs stochastic](deterministic-vs-stochastic.md) (logic). Pure chance is one kind of doubt that no new data can shrink. But Russell and Norvig note that a deterministic world you can only half see looks random ([Task environment properties](../frameworks/1995-task-environment-properties.md)). Doubt that looks like chance may be a hidden fact you could find.
- [Stable vs chaotic](stable-vs-chaotic.md) (logic). Past the horizon more data barely moves the forecast.
- [Shared vs contested values](shared-vs-contested-values.md) (bundled). Treverton's mysteries and Daft and Lengel's [equivocality](../frameworks/1986-uncertainty-vs-equivocality.md) are doubts that more facts won't settle, because people read the facts differently or haven't yet chosen what to do. His [puzzles](../frameworks/2001-puzzles-vs-mysteries.md) are the other end, hidden facts that someone could find.
- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (independent). Reducible asks whether more data would shrink your doubt, while Knightian uncertainty is about whether you can put a number on it. A coin toss has known odds and irreducible doubt. A new drug has unknown odds and reducible doubt, because you can run a trial.
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (study). Hidden variables are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](../frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every weight of an open model and still not trace the chain. A poker hand is a simple cause that is hidden from view.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (bundled). Opponents hide what they can, as in poker. The facts exist, but they cost more to find.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). Go hides nothing and still can't be searched in full.
- [Small vs large world](small-vs-large-world.md) (independent). Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Local facts are often out of sight for anyone far away. But the shop manager can see the stock levels that head office can't, so the gap is about who holds the facts.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). When someone across the deal already holds the facts, the doubt is reducible, but they decide what it costs you to find them.

## Citations

[1] [Johari window](../frameworks/1955-johari-window.md)

[2] [Uncertainty vs equivocality](../frameworks/1986-uncertainty-vs-equivocality.md)

[3] [Complex problem solving](../frameworks/1989-complex-problem-solving.md)

[4] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[5] [Puzzles vs mysteries](../frameworks/2001-puzzles-vs-mysteries.md)

[6] [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md)
