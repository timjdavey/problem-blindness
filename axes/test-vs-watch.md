---
type: Axis
title: Test vs watch
description: "Test: you can run a fair test where chance decides who gets what (e.g. a drug trial). Watch: you can only watch what happens and guess at the cause (e.g. a study of nurses who chose hormone therapy)."
group: knower
easy_end: Test
hard_end: Watch
sources:
  - resource: /frameworks/1933-multi-armed-bandit.md
    title: Multi-armed bandit
  - resource: /frameworks/1991-exploration-vs-exploitation.md
    title: Exploration vs exploitation
  - resource: /frameworks/2000-ladder-of-causation.md
    title: Ladder of causation
---
# Test vs watch

An axis in the [knower](index.md#the-knower) group.

Can you run a fair test, where chance decides who gets what, or can you only watch what happens and guess at the cause? A drug trial gives the pill to some people and a dummy to others at random, so any gap comes from the pill. In 1991 a study of nearly 50,000 nurses found women on hormone therapy had about half the heart disease. That was watching, and the women who chose hormones were healthier to start with. A 2002 trial found the hormones raised heart disease. Judea Pearl calls watching and testing the bottom two rungs of his ladder of causation.

## Actions

**Test**: Run the experiment.
- Randomise, A/B test or use a bandit. A fair test tells you what works, not just what goes with what.
- Let the result decide. A fair test should beat anyone's opinion of the outcome.

**Watch**: Treat logged data as biased until shown otherwise.
- Remember what the logs teach. A model trained on what happened learns who chose what, not what works.
- Write down what you assume causes what. Then use methods that adjust for it, so others can see and challenge your guesses.
- Check against any small test you can run. Even a little random data can show if the logs mislead you.
- Never read a pattern in the logs as the effect of acting on it. The nurses study did, and got hormone therapy backwards.

## Correlated with

- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (independent). The nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (logic). Watching mixes the effect of a choice with the kind of people who made it, so it can teach the wrong lesson. Doctors read the nurses study as proof that hormones protect the heart.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [One-shot vs sequential](one-shot-vs-sequential.md) (opposite). Each pull of a [bandit](../frameworks/1933-multi-armed-bandit.md) is a small test, so a chain of choices lets you test as you go. Thompson picked each new patient's treatment at random, weighted towards whichever looked better so far.
- [Spread vs single bet](spread-vs-single-bet.md) (logic). A fair test needs you to do more than one thing at once. With only one economy there is no control group. But a portfolio spreads without testing anything.

## Citations

[1] [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)

[2] [Exploration vs exploitation](../frameworks/1991-exploration-vs-exploitation.md)

[3] [Ladder of causation](../frameworks/2000-ladder-of-causation.md)
