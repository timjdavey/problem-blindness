---
type: Axis
title: Interventional vs observational
aliases:
  - Test vs watch
description: "Interventional: you can set the cause yourself and let chance decide who gets it (e.g. a drug trial). Observational: people's own choices or nature set the cause, so you can only watch what follows and guess (e.g. a study of nurses who chose hormone therapy)."
group: information
subgroup: evidence
easy_end: Interventional
hard_end: Observational
sources:
  - resource: /frameworks/1943-survivorship-bias.md
    title: Survivorship bias
  - resource: /frameworks/1933-multi-armed-bandit.md
    title: Multi-armed bandit
  - resource: /frameworks/1991-exploration-vs-exploitation.md
    title: Exploration vs exploitation
  - resource: /frameworks/2000-ladder-of-causation.md
    title: Ladder of causation
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
  - resource: https://doi.org/10.1056/NEJM199109123251102
    title: "Postmenopausal estrogen therapy and cardiovascular disease: ten-year follow-up from the Nurses' Health Study (Stampfer, 1991)"
  - resource: https://doi.org/10.1001/jama.288.3.321
    title: "Risks and benefits of estrogen plus progestin in healthy postmenopausal women: principal results from the Women's Health Initiative randomized controlled trial (Rossouw, 2002)"
---
# Interventional vs observational

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Can you set the cause yourself and let chance decide who gets it, or do people's own choices or nature set it, so you can only watch what follows? A drug trial gives the pill to some people and a dummy to others at random, so any gap comes from the pill. In 1991 a study of nearly 50,000 nurses found women on hormone therapy had about half the heart disease. That was watching, and the women who chose hormones were healthier to start with. A 2002 trial found the hormones raised heart disease. Judea Pearl puts seeing and doing on the bottom two rungs of his ladder of causation. Evidence from the first is called observational, and evidence from the second interventional.

Watching is worse still when you only see how your own choices turned out. A hiring manager sees how the people they took on did, but never the ones they turned away. A model trained on repaid loans has the same blind spot, because the people it refused never got the chance to repay. Robin Hogarth counts this as one way a [learning environment turns wicked](../frameworks/2001-kind-vs-wicked-learning-environments.md), since years of results can confirm a bad rule.

## Actions

**Interventional**: Run the experiment.
- Run a fair test where you can. When chance decides who gets the change, any gap comes from the change, while watching only tells you what goes with what. [4]
- Shift towards what is winning while the test runs. A fixed trial keeps sending half its patients or users to an option that is plainly losing. In 1933 William Thompson proposed giving each new patient a treatment at random, weighted towards whichever looked better so far. [2]
- Keep testing now and then after a winner emerges. An early lead can be luck, and only fresh tests will show it. [2]
- Give tests their own budget. They pay back slowly, so this year's results will starve them otherwise. [3]

**Observational**: Treat past records as biased until shown otherwise.
- Ask who chose each option before you read a pattern. Records mix the effect of a choice with the kind of person who made it. Keen gym members may sign up for classes and lose weight whatever the classes do. [4]
- Ask who is missing from the records, as well as who chose what. Funds that closed drop out of the databases, so the funds left look better than the average investor did, by about 0.9% a year across American mutual funds. [1]
- Write down what you assume causes what, and see which links your answer rests on. Others can then check and challenge those guesses. [4]
- Check the records against a fair test wherever you can run one, however small. It shows whether the pattern holds once you step in. [4]
- Never read a pattern in the records as the effect of acting on it. Nurses who took hormones had about half the heart disease, so doctors gave hormones to protect the heart. A 2002 trial found they raised it instead. [4, 6, 7]
- Say yes at random to a few cases you would have turned away. A lender or a recruiter otherwise never sees how the people it refused would have done. [2, 5]

## Correlated with

- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (independent). The nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [Diversifiable vs single bet](diversifiable-vs-single-bet.md) (logic). A fair test needs you to do more than one thing at once. With only one economy there is no control group. But a portfolio spreads without testing anything.
- [Rehearsable vs live only](rehearsable-vs-live-only.md) (independent). A fair test sets the cause for real, and a rehearsal tries it on a copy. A canary deploy is a fair test with no faithful copy, and a weather forecaster can rehearse against past weather without ever setting the cause.

## Citations

[1] [Survivorship bias](../frameworks/1943-survivorship-bias.md)

[2] [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)

[3] [Exploration vs exploitation](../frameworks/1991-exploration-vs-exploitation.md)

[4] [Ladder of causation](../frameworks/2000-ladder-of-causation.md)

[5] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)

[6] [Postmenopausal estrogen therapy and cardiovascular disease: ten-year follow-up from the Nurses' Health Study (Stampfer, 1991)](https://doi.org/10.1056/NEJM199109123251102)

[7] [Risks and benefits of estrogen plus progestin in healthy postmenopausal women: principal results from the Women's Health Initiative randomized controlled trial (Rossouw, 2002)](https://doi.org/10.1001/jama.288.3.321)
