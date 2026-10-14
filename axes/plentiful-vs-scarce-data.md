---
type: Axis
title: Plentiful vs scarce data
description: "Plentiful: there are many past cases like this one to learn from (e.g. card fraud). Scarce: there are so few past cases that you have almost nothing to go on (e.g. a nuclear accident)."
group: knower
subgroup: evidence
easy_end: Plentiful
hard_end: Scarce
sources:
  - resource: /frameworks/1954-clinical-vs-statistical-prediction.md
    title: Clinical vs statistical prediction
  - resource: /frameworks/1992-task-characteristics-of-expertise.md
    title: Task characteristics of expertise
  - resource: /frameworks/1993-inside-vs-outside-view.md
    title: Inside vs outside view
  - resource: /frameworks/1999-ecological-rationality.md
    title: Ecological rationality
---
# Plentiful vs scarce data

An axis in the [knower](index.md#the-knower) group.

Have there been enough past cases like this one to learn the pattern from, or so few that you have almost nothing to go on? Card fraud happens millions of times a year. A nuclear accident or a once in a century flood gives you almost nothing to go on.

## Actions

**Plentiful**: Let the model learn the pattern.
- Prefer a statistical model to expert judgement. Meehl found that simple formulas fitted to many cases beat clinicians.
- Hold out a big test set. With data to spare you can measure the model properly.

**Scarce**: Borrow knowledge from elsewhere.
- Start from a pre-trained model. It brings what it learnt from other data, so you need far fewer cases of your own.
- Use base rates from similar cases. This is called the outside view, and it beats reasoning from the details of one case.
- Add expert priors or simulation where you can. They fill the gaps your data leaves.
- Report wide error bars, and don't trust a test set of thirty examples. A lucky few can make a weak model look great.

## Correlated with

- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The events that matter most in a fat tailed world are the rare ones. But card fraud is fat tailed and still has millions of cases. Fat tails make the cases that matter rare, not the data overall.
- [Known vs unknown odds](known-vs-unknown-odds.md) (logic). Odds come from a long record of similar cases ([Risk vs uncertainty](../frameworks/1921-risk-vs-uncertainty.md)).
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (study). [Shanteau](../frameworks/1992-task-characteristics-of-expertise.md) found skill grows where the same decision comes round often.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A rare kind of case is one the solver has seldom seen. Simon's [programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md) are the ones that recur. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). You can't learn from your own ruin, because it only happens once ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Test vs watch](test-vs-watch.md) (independent). The 1991 nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).

## Citations

[1] [Clinical vs statistical prediction](../frameworks/1954-clinical-vs-statistical-prediction.md)

[2] [Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)

[3] [Inside vs outside view](../frameworks/1993-inside-vs-outside-view.md)

[4] [Ecological rationality](../frameworks/1999-ecological-rationality.md)
