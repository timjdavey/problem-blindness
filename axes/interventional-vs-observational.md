---
type: Axis
title: Interventional vs observational
description: "Interventional: you can set the cause yourself and let chance decide who gets it (e.g. a drug trial). Observational: people's own choices or nature set the cause, so you can only watch what follows and guess (e.g. a study of nurses who chose hormone therapy)."
group: knower
subgroup: evidence
easy_end: Interventional
hard_end: Observational
sources:
  - resource: /frameworks/1933-multi-armed-bandit.md
    title: Multi-armed bandit
  - resource: /frameworks/1991-exploration-vs-exploitation.md
    title: Exploration vs exploitation
  - resource: /frameworks/2000-ladder-of-causation.md
    title: Ladder of causation
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
---
# Interventional vs observational

An axis in the [Evidence](index.md#evidence) set of the [knower](index.md#the-knower) group.

Can you set the cause yourself and let chance decide who gets it, or do people's own choices or nature set it, so you can only watch what follows? A drug trial gives the pill to some people and a dummy to others at random, so any gap comes from the pill. In 1991 a study of nearly 50,000 nurses found women on hormone therapy had about half the heart disease. That was watching, and the women who chose hormones were healthier to start with. A 2002 trial found the hormones raised heart disease. Judea Pearl puts seeing and doing on the bottom two rungs of his ladder of causation. Evidence from the first is called observational, and evidence from the second interventional.

Watching is worse still when you only see how your own choices turned out. A hiring manager sees how the people they took on did, but never the ones they turned away. A model trained on repaid loans has the same blind spot, because the people it refused never got the chance to repay. Robin Hogarth counts this as one way a [learning environment turns wicked](../frameworks/2001-kind-vs-wicked-learning-environments.md), since years of results can confirm a bad rule.

## Actions

**Interventional**: Run the experiment.
- Randomise, A/B test or use a bandit. A fair test tells you what works, not just what goes with what. A bandit tests as it goes. In 1933 William Thompson proposed giving each new patient a treatment at random, weighted towards whichever looked better so far ([Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)).
- Let the result decide. A fair test should beat anyone's opinion of the outcome.

**Observational**: Treat logged data as biased until shown otherwise.
- Remember what the logs teach. A model trained on what happened learns who chose what, not what works.
- Write down what you assume causes what. Then use methods that adjust for it, so others can see and challenge your guesses.
- Check against any small test you can run. Even a little random data can show if the logs mislead you.
- Never read a pattern in the logs as the effect of acting on it. The nurses study did, and got hormone therapy backwards.
- Let a small random share through that the model would have refused. It's the only way to see how the road not taken turns out.

## Correlated with

- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (independent). The nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [Spread vs single bet](spread-vs-single-bet.md) (logic). A fair test needs you to do more than one thing at once. With only one economy there is no control group. But a portfolio spreads without testing anything.

## Citations

[1] [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)

[2] [Exploration vs exploitation](../frameworks/1991-exploration-vs-exploitation.md)

[3] [Ladder of causation](../frameworks/2000-ladder-of-causation.md)

[4] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)
