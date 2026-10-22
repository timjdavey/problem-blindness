---
type: Axis
title: Inert vs reflexive
description: "Inert: the system behaves the same whether or not you model it (e.g. a rock). Reflexive: people believe or follow your forecasts and scores, and that changes the outcome, with nobody aiming at you (e.g. a forecast that a bank will fail sets off a run on it)."
group: environment
subgroup: reactivity
easy_end: Inert
hard_end: Reflexive
sources:
  - resource: /frameworks/1936-keynesian-beauty-contest.md
    title: Keynesian beauty contest
  - resource: /frameworks/1948-self-fulfilling-prophecy.md
    title: Self-fulfilling prophecy
  - resource: /frameworks/1976-lucas-critique.md
    title: Lucas critique
  - resource: /frameworks/1987-reflexivity.md
    title: Reflexivity
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
---
# Inert vs reflexive

An axis in the [Reactivity](index.md#reactivity) set of the [environment](index.md#environment) group.

Does the system behave the same whether or not you model it, or does the way people respond to your forecasts, scores and actions change the outcome? A rock doesn't care if you measure it. Publish a forecast that a bank will fail and people pull their money out, which makes it fail. A forecast can also defeat itself. Warn that a road will jam and drivers take another route, so it flows freely. Both are reflexive, because in each case the forecast changed the outcome. Actions do it too. A recommender changes what people click, then learns from those clicks as if they were the world.

Nobody in these stories is trying to beat you. Each saver only wants their own money back, and each driver only wants to get home. The outcome moves because a lot of people believe or follow what you put out. When someone studies your rule to find the cases it gets wrong, that is the hard end of [Neutral vs adversarial](neutral-vs-adversarial.md) instead.

The worst case is when your own action makes the result you take as proof. Robin Hogarth tells of a doctor who seemed to spot typhoid early by feeling patients' tongues, when he was spreading it with his hands. Every hit made him surer of his skill. Hogarth counts this as one way a [learning environment turns wicked](../frameworks/2001-kind-vs-wicked-learning-environments.md).

## Actions

**Inert**: Measure and act freely.
- Learn from logged data. Your forecast won't change the thing you forecast, so the logs are a fair record.
- Publish scores and forecasts openly. A rock doesn't move because you said where it was.

**Reflexive**: Expect your model to change the world it was trained on.
- Ask what people will do once they see the output. A forecast that sets off a run, or calls one off, needs a different launch from one that nobody acts on.
- Hold back a small random group the model doesn't act on. It shows you what would have happened without the model.
- Watch for feedback loops. A recommender that only learns from what it chose to show will narrow until it shows the same few things.
- Retrain with care. Data collected after launch carries the model's own effect, so it is no longer a clean picture of the world.
- Get labels from outside the loop. Audits and expert review give a view the model's own record can't.

## Correlated with

- [Thin vs fat tails](thin-vs-fat-tails.md) (study). [Reflexivity](../frameworks/1987-reflexivity.md) and the [bank run](../frameworks/1948-self-fulfilling-prophecy.md) show beliefs and facts feeding each other into booms and crashes.
- [Stationary vs drifting](stationary-vs-drifting.md) (study). Under the [Lucas critique](../frameworks/1976-lucas-critique.md) acting on a model changes the behaviour it was fitted to.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Both are about people reacting to you, so they often turn up together, as in a market. What splits them is whether anyone is aiming at your rule. A bank run is reflexive with no adversary in it. A chess opponent hunts for your weakest line, but the board doesn't change because someone forecast the result. If someone studies your rule to find its gaps, it is adversarial. If the outcome moves with nobody aiming at anything, it is reflexive.
- [Interventional vs observational](interventional-vs-observational.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (logic). Both put other people inside the problem. Once a fix depends on others changing, how they react to it becomes part of the problem.
- [Curable vs chronic](curable-vs-chronic.md) (logic). When people react to your fix, the fix becomes part of the next problem, so there is no point where you are done.

## Citations

[1] [Keynesian beauty contest](../frameworks/1936-keynesian-beauty-contest.md)

[2] [Self-fulfilling prophecy](../frameworks/1948-self-fulfilling-prophecy.md)

[3] [Lucas critique](../frameworks/1976-lucas-critique.md)

[4] [Reflexivity](../frameworks/1987-reflexivity.md)

[5] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)
