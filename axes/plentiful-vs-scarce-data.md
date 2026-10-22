---
type: Axis
title: Plentiful vs scarce data
description: "Plentiful data: there are many past cases like this one to learn from (e.g. card fraud). Scarce data: there are so few past cases that you have almost nothing to go on (e.g. a nuclear accident)."
group: information
subgroup: evidence
easy_end: Plentiful data
hard_end: Scarce data
sources:
  - resource: /frameworks/1954-clinical-vs-statistical-prediction.md
    title: Clinical vs statistical prediction
  - resource: /frameworks/1967-routine-vs-non-routine-technology.md
    title: Routine vs non-routine technology
  - resource: /frameworks/1992-task-characteristics-of-expertise.md
    title: Task characteristics of expertise
  - resource: /frameworks/1993-inside-vs-outside-view.md
    title: Inside vs outside view
  - resource: /frameworks/1999-ecological-rationality.md
    title: Ecological rationality
  - resource: https://doi.org/10.1109/TKDE.2009.191
    title: A survey on transfer learning (Pan, 2010)
---
# Plentiful vs scarce data

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Have there been enough past cases like this one to learn the pattern from, or so few that you have almost nothing to go on? Card fraud happens millions of times a year. A nuclear accident or a once in a century flood gives you almost nothing to go on.

## Actions

**Plentiful data**: Let the cases teach you the pattern.
- Prefer a formula to expert judgement on a decision that comes round often. Meehl found formulas matched or beat clinicians in nearly every study he gathered. [1]
- Fit a full model when cases are many and the world holds still. A rule of thumb there throws away accuracy that a proper model would give. [5]
- Keep some cases back for testing. In one contest regression came first on data it had already seen. On fresh data it dropped the most, and a simpler rule won. [5]

**Scarce data**: Borrow knowledge from elsewhere.
- Borrow what was learnt on related problems. A vet seeing a rare breed draws on every dog they have treated, and a pre-trained model draws on other data. Either way you need far fewer cases of your own. [6]
- Start from the spread of results in similar cases, then adjust for what is really different about yours. This is the outside view, and it is less hopeful than reasoning from one case's details. [4]
- Prefer a simple rule to a model with many dials. With few cases, luck sets the dials and the forecasts swing about. [5]
- Let judgement overrule the formula only for a fact the formula can't hold. Meehl's example is a formula that says a professor goes to the cinema every Tuesday. If he broke his leg this morning, overrule it. [1]
- Don't trust a short track record. With few cases luck and skill look alike, like a fund manager after three good years. [3]
- Count by kind of case, not in total. A support inbox can hold millions of tickets and still have only a handful of each odd kind. Charles Perrow warned against forcing such cases through a process built for the common ones. [2]

## Correlated with

- [Thin vs fat tails](thin-vs-fat-tails.md) (logic). The events that matter most in a fat tailed world are the rare ones. But card fraud is fat tailed and still has millions of cases. Fat tails make the cases that matter rare, not the data overall.
- [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md) (logic). Odds come from a long record of similar cases ([Risk vs uncertainty](../frameworks/1921-risk-vs-uncertainty.md)).
- [Stationary vs drifting](stationary-vs-drifting.md) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (logic). Slow feedback means few graded tries. [Shanteau](../frameworks/1992-task-characteristics-of-expertise.md) found skill grows where the same decision comes round often.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A rare kind of case is one the solver has seldom seen. Simon's [programmed decisions](../frameworks/1960-programmed-vs-non-programmed-decisions.md) are the ones that recur. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Survivable vs ruinous](survivable-vs-ruinous.md) (logic). You can't learn from your own ruin, because it only happens once ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Interventional vs observational](interventional-vs-observational.md) (independent). The 1991 nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (logic). Pooling runs that disagree gives a lot of data that describes none of them. A big record only helps if its cases draw from the same spread.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). With clear groups a few readings can rule a whole group out, so a little data goes a long way ([Cohesion](../frameworks/2023-cohesion.md)).
- [Static vs dynamic](static-vs-dynamic.md) (logic). Ann Gentile split out settings that sit still during each attempt but differ from one attempt to the next, like a billiards table. Like varied cases here, they need practice across many setups, not one.

## Citations

[1] [Clinical vs statistical prediction](../frameworks/1954-clinical-vs-statistical-prediction.md)

[2] [Routine vs non-routine technology](../frameworks/1967-routine-vs-non-routine-technology.md)

[3] [Task characteristics of expertise](../frameworks/1992-task-characteristics-of-expertise.md)

[4] [Inside vs outside view](../frameworks/1993-inside-vs-outside-view.md)

[5] [Ecological rationality](../frameworks/1999-ecological-rationality.md)

[6] [A survey on transfer learning (Pan, 2010)](https://doi.org/10.1109/TKDE.2009.191)
