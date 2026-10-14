---
type: Axis
title: Inert vs reflexive
description: "Inert: the system behaves the same whether or not you measure or forecast it (e.g. a rock). Reflexive: your forecast changes what people do and so changes the outcome (e.g. a forecast that a bank will fail sets off a run on it)."
group: world
subgroup: response
easy_end: Inert
hard_end: Reflexive
sources:
  - resource: /frameworks/1936-keynesian-beauty-contest.md
    title: Keynesian beauty contest
  - resource: /frameworks/1948-self-fulfilling-prophecy.md
    title: Self-fulfilling prophecy
  - resource: /frameworks/1975-goodharts-law.md
    title: Goodhart's law
  - resource: /frameworks/1976-campbells-law.md
    title: Campbell's law
  - resource: /frameworks/1976-lucas-critique.md
    title: Lucas critique
  - resource: /frameworks/1987-reflexivity.md
    title: Reflexivity
---
# Inert vs reflexive

An axis in the [world](index.md#the-world) group.

Does the system behave the same whether or not you measure and forecast it, or do your forecasts change what people do and so change the outcome? A rock doesn't care if you measure it. Publish a forecast that a bank will fail and people pull their money out, which makes it fail.

## Actions

**Inert**: Measure and act freely.
- Learn from logged data. Your forecast won't change the thing you forecast, so the logs are a fair record.
- Publish scores and forecasts openly. Nobody can game a rock.

**Reflexive**: Expect your model to change the world it was trained on.
- Hold back a small random group the model doesn't act on. It shows you what would have happened without the model.
- Watch for feedback loops. A recommender that only learns from what it chose to show will narrow until it shows the same few things.
- Expect people to game any score they are judged on. Keep some of the inputs private and change the score now and then.
- Retrain with care. Data collected after launch carries the model's own effect, so it is no longer a clean picture of the world.

## Correlated with

- [Thin vs fat tails](thin-vs-fat-tails.md) (study). [Reflexivity](../frameworks/1987-reflexivity.md) and the [bank run](../frameworks/1948-self-fulfilling-prophecy.md) show beliefs and facts feeding each other into booms and crashes.
- [Stationary vs drifting](stationary-vs-drifting.md) (study). Under the [Lucas critique](../frameworks/1976-lucas-critique.md) acting on a model changes the behaviour it was fitted to.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (bundled). The [Keynesian beauty contest](../frameworks/1936-keynesian-beauty-contest.md) and [zero-sum games](../frameworks/1944-zero-sum-vs-non-zero-sum-games.md) are both about other minds reacting to yours. The difference is intent. A bank run is reflexive with no enemy, since each saver only wants their own money back. A chess opponent is out to beat you, but the board doesn't change because someone forecast the result.
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (logic). By [Goodhart's law](../frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it.
- [Private vs accountable](private-vs-accountable.md) (study). [Campbell's law](../frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Test vs watch](test-vs-watch.md) (study). The [Lucas critique](../frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [Complete vs incomplete goal](complete-vs-incomplete-goal.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (logic). Both put other people inside the problem. Once a fix depends on others changing, how they react to it becomes part of the problem.

## Citations

[1] [Keynesian beauty contest](../frameworks/1936-keynesian-beauty-contest.md)

[2] [Self-fulfilling prophecy](../frameworks/1948-self-fulfilling-prophecy.md)

[3] [Goodhart's law](../frameworks/1975-goodharts-law.md)

[4] [Campbell's law](../frameworks/1976-campbells-law.md)

[5] [Lucas critique](../frameworks/1976-lucas-critique.md)

[6] [Reflexivity](../frameworks/1987-reflexivity.md)
