---
type: Axis
title: Full vs partial observability
description: Can you see everything that matters?
group: knower
easy_end: Full
hard_end: Partial
sources:
  - resource: /frameworks/1955-johari-window.md
    title: Johari window
  - resource: /frameworks/1989-complex-problem-solving.md
    title: Complex problem solving
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
  - resource: /frameworks/2002-known-and-unknown-unknowns.md
    title: Known and unknown unknowns
---
# Full vs partial observability

An axis in the [knower](index.md#the-knower) group.

Can you see everything that matters? In chess you see the whole board. In poker the other hands are hidden, and in medicine you often see only symptoms, not the cause.

## Actions

**Full**: Act on what you see.
- Decide straight from the input. It holds everything that matters.
- Skip the clarifying questions. Asking for what you can already see wastes the user's time.

**Partial**: Find out before you act.
- Gather the missing facts. An agent should look things up or ask a question before it commits.
- Keep track of what you believe about the hidden state. Update it as each new clue comes in, like a doctor narrowing a diagnosis.
- Say what you can't see. A model that answers as if it had the full picture hides its biggest weakness.
- Test the model on cases where the key evidence is missing. That is how it will meet many real ones.

## Correlated with

- [Deterministic vs statistical](deterministic-vs-statistical.md) (logic). Russell and Norvig note that a deterministic world you can only half see looks random ([Task environment properties](../frameworks/1995-task-environment-properties.md)).
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (study). Hidden variables are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](../frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every line of an open source codebase and still not trace the chain. A poker hand is a simple cause that is hidden from view.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (bundled). Opponents hide what they can, as in poker.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (opposite). What is hidden can often be found, so partial observability usually leans to the reducible end.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (logic). A hiring manager never sees how the people they turned away would have done, so half the feedback is missing ([Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)).
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). Chess hides nothing and still can't be searched in full.
- [Small vs large world](small-vs-large-world.md) (independent). Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Local facts are often out of sight for anyone far away. But the shop manager can see the stock levels that head office can't, so the gap is about who holds the facts.

## Citations

[1] [Johari window](../frameworks/1955-johari-window.md)

[2] [Complex problem solving](../frameworks/1989-complex-problem-solving.md)

[3] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[4] [Known and unknown unknowns](../frameworks/2002-known-and-unknown-unknowns.md)
