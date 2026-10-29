---
type: Grid
title: Which assumption breaks
description: Each column is one textbook assumption behind fitting on the past, averaging and optimising, and an axis goes where its hard end breaks it. It sorts the randomness, change and evidence axes well and finds one assumption, ergodicity, broken in three groups, but 24 of the 50 axes break none of the seven, so it fails as a test of the whole set.
columns_from:
  - resource: /frameworks/1921-risk-vs-uncertainty.md
    title: Risk vs uncertainty
  - resource: /frameworks/2024-incoherence.md
    title: Incoherence
  - resource: /frameworks/1976-lucas-critique.md
    title: Lucas critique
  - resource: /frameworks/2016-ergodicity.md
    title: Ergodicity
  - resource: /frameworks/1963-sensitive-dependence-chaos.md
    title: Sensitive dependence (chaos)
  - resource: /frameworks/1962-near-decomposability.md
    title: Near decomposability
  - resource: /frameworks/1987-reflexivity.md
    title: Reflexivity
  - resource: /frameworks/1975-goodharts-law.md
    title: Goodhart's law
  - resource: /frameworks/1970-convex-vs-non-convex-optimisation.md
    title: Convex vs non-convex optimisation
  - resource: /frameworks/1987-rugged-fitness-landscapes.md
    title: Rugged fitness landscapes
---
# Which assumption breaks

**Each column is one textbook assumption behind the usual playbook, and an axis goes where its hard end breaks that assumption.**

## The columns

The usual playbook is to fit a model on the past, trust the average and improve step by step. That works when a handful of assumptions hold. Each column asks whether one of them does.

| Column | The question | Where it comes from |
|---|---|---|
| Same each time? | Are cases independent draws from one fixed spread? This is called i.i.d. | Knight's risk needs a long record of like cases ([Risk vs uncertainty](../frameworks/1921-risk-vs-uncertainty.md)). Davey measures how far runs are from being draws from one spread ([Incoherence](../frameworks/2024-incoherence.md)) |
| Same tomorrow? | Does the process stay the same over time? This is called stationarity | Lucas showed patterns in past data break once the rules change ([Lucas critique](../frameworks/1976-lucas-critique.md)) |
| Does the average mean anything? | Does the average over many cases match what one case lives through over time? This is called ergodicity | Peters and Gell-Mann ([Ergodicity](../frameworks/2016-ergodicity.md)), and pooled runs that describe no run ([Incoherence](../frameworks/2024-incoherence.md)) |
| Small cause, small effect? | Do effects scale with their causes? This is called linearity | Lorenz's butterfly effect ([Sensitive dependence (chaos)](../frameworks/1963-sensitive-dependence-chaos.md)) |
| Do the parts add up? | Can you solve or score the parts one at a time and sum them? This is called separability | Simon's rooms and walls ([Near decomposability](../frameworks/1962-near-decomposability.md)) |
| Does looking change it? | Does the system behave the same whether or not you model, score or act on it? This is called observer independence | [Lucas critique](../frameworks/1976-lucas-critique.md), [Reflexivity](../frameworks/1987-reflexivity.md) and [Goodhart's law](../frameworks/1975-goodharts-law.md) |
| Is halfway good? | Is a point between two good answers also good, so local improvement finds the best? This is called convexity | [Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md) and Kauffman's peaks ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)) |

## The grid

| Group | Same each time? | Same tomorrow? | Does the average mean anything? | Small cause, small effect? | Do the parts add up? | Does looking change it? | Is halfway good? |
|---|---|---|---|---|---|---|---|
| Environment | [Scattered runs](../axes/clustered-vs-scattered-runs.md), *[Incoherent runs](../axes/coherent-vs-incoherent-runs.md)* | [Perishable lessons](../axes/durable-vs-perishable-lessons.md), [Wears out](../axes/antifragile-vs-wears-out.md) | [Incoherent runs](../axes/coherent-vs-incoherent-runs.md), [Fat tails](../axes/thin-vs-fat-tails.md) | [Chaotic](../axes/stable-vs-chaotic.md), [Tipping point](../axes/self-righting-vs-tipping.md), [Exacting landscape](../axes/forgiving-vs-exacting.md) | [Cascading system](../axes/buffered-vs-cascading.md), [Holistic problem](../axes/reductionist-vs-holistic.md) | [Reflexive](../axes/inert-vs-reflexive.md), [Adversarial](../axes/neutral-vs-adversarial.md) | *[Exacting landscape](../axes/forgiving-vs-exacting.md)* |
| Information | [Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md), [Observational](../axes/interventional-vs-observational.md), [Scarce data](../axes/plentiful-vs-scarce-data.md), [Live only](../axes/rehearsable-vs-live-only.md) | *empty* | *empty* | *empty* | [Opaque causes](../axes/transparent-vs-opaque-causes.md) | [Asymmetric information](../axes/symmetric-vs-asymmetric-information.md) | *empty* |
| Actions | *empty* | *empty* | [Single bet](../axes/diversifiable-vs-single-bet.md), [Irreversible](../axes/reversible-vs-irreversible.md) | *empty* | [Sequential](../axes/standalone-vs-sequential.md) | *empty* | *empty* |
| Performance | *empty* | *empty* | [Ruinous](../axes/survivable-vs-ruinous.md), [Compounding results](../axes/flat-vs-compounding-results.md) | *empty* | *empty* | *empty* | [Divergent](../axes/convergent-vs-divergent.md) |
| Agent | [Novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | *empty* | *empty* | *empty* | *empty* | [Accountable choice](../axes/private-vs-accountable.md) | *empty* |

## Where each axis goes

| Axis | Cell | Why |
|---|---|---|
| [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) | No home | Draws around a steady rate are the textbook case, so nothing breaks. |
| [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) | Environment, Does the average mean anything? and Environment, Same each time? | The pooled average describes no run, and the runs are not draws from one spread. |
| [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) | Environment, Same each time? | Scattered runs can't be sorted into a few fixed spreads. |
| [Thin vs fat tails](../axes/thin-vs-fat-tails.md) | Environment, Does the average mean anything? | One extreme case sets the average, so a typical case lives far from it. |
| [Stable vs chaotic](../axes/stable-vs-chaotic.md) | Environment, Small cause, small effect? | Tiny errors grow fast, the plainest break of linearity. |
| [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) | Environment, Same tomorrow? | The rules behind past data keep changing. |
| [Turn-based vs real-time](../axes/turn-based-vs-real-time.md) | No home | The state moves, but the rules can stay fixed, and stationarity only asks about the rules. |
| [Self-righting vs tipping](../axes/self-righting-vs-tipping.md) | Environment, Small cause, small effect? | Past a threshold a small push flips the whole system. |
| [Antifragile vs wears out](../axes/antifragile-vs-wears-out.md) | Environment, Same tomorrow? | Each stress changes the system itself. |
| [Buffered vs cascading](../axes/buffered-vs-cascading.md) | Environment, Do the parts add up? | A fault in one part spreads to the others. |
| [Inert vs reflexive](../axes/inert-vs-reflexive.md) | Environment, Does looking change it? | Putting out a forecast changes the thing it forecasts. |
| [Neutral vs adversarial](../axes/neutral-vs-adversarial.md) | Environment, Does looking change it? | Someone studies your rule and changes what you meet. |
| [Reductionist vs holistic](../axes/reductionist-vs-holistic.md) | Environment, Do the parts add up? | Each part only makes sense in light of the others. |
| [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) | Environment, Small cause, small effect? and Environment, Is halfway good? | A small change swings the result, and small steps stall on the nearest peak. |
| [Tractable vs intractable options](../axes/tractable-vs-intractable-options.md) | No home | It is only about size, and convexity is about shape. |
| [Risk vs Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md) | Information, Same each time? | There is no record of like cases to treat as draws from one spread. |
| [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | No home | Doubt no test can settle is plain chance, which the playbook assumes. |
| [Known vs unknown unknowns](../axes/known-vs-unknown-unknowns.md) | No home | A fact nobody thought to ask about breaks none of the seven. |
| [Foreseeable vs unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md) | No home | It breaks the fixed list of outcomes, which none of the seven names. |
| [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) | Information, Do the parts add up? | You can't read off each part's share and add them up. |
| [Interventional vs observational](../axes/interventional-vs-observational.md) | Information, Same each time? | Those who chose the cause differ from those who didn't. |
| [Symmetric vs asymmetric information](../axes/symmetric-vs-asymmetric-information.md) | Information, Does looking change it? | The other side picks what reaches you because you are asking. |
| [Plentiful vs scarce data](../axes/plentiful-vs-scarce-data.md) | Information, Same each time? | Few past cases come from the same spread as this one. |
| [High vs low base rate](../axes/high-vs-low-base-rate.md) | No home | Rare targets can still be fair draws, so no assumption breaks. |
| [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) | No home | The cost of checking an answer is not one of the seven. |
| [Rehearsable vs live only](../axes/rehearsable-vs-live-only.md) | Information, Same each time? | Rehearsal cases are not drawn from the real spread. |
| [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) | No home | A late result breaks none of the seven. |
| [Given vs invented options](../axes/given-vs-invented-options.md) | No home | It breaks the fixed menu of options, which none of the seven names. |
| [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md) | Actions, Does the average mean anything? | With one bet you live one path, not the average. |
| [Standalone vs sequential](../axes/standalone-vs-sequential.md) | Actions, Do the parts add up? | Each choice changes the next, so none can be scored alone. |
| [Reversible vs irreversible](../axes/reversible-vs-irreversible.md) | Actions, Does the average mean anything? | You can't undo and retry, so you live one path. |
| [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) | No home | Who holds the levers is not one of the seven. |
| [Ample time vs time pressure](../axes/ample-time-vs-time-pressure.md) | No home | A deadline breaks none of the seven. |
| [Well vs ill-structured](../axes/well-vs-ill-structured.md) | No home | Not knowing the problem comes before any of the seven. |
| [Convergent vs divergent](../axes/convergent-vs-divergent.md) | Performance, Is halfway good? | Halfway between two good answers is worse than either. |
| [Single objective vs trade-offs](../axes/single-objective-vs-trade-offs.md) | No home | Priced trade-offs still sum and still blend, so nothing breaks. |
| [Shared vs contested values](../axes/shared-vs-contested-values.md) | No home | Whose ranking counts is not one of the seven. |
| [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) | No home | The hard end is the playbook's own goal, so it breaks nothing. |
| [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md) | No home | A score that leaves goals out breaks none of the seven. |
| [Curable vs chronic](../axes/curable-vs-chronic.md) | No home | A problem with no end state breaks none of the seven. |
| [Survivable vs ruinous](../axes/survivable-vs-ruinous.md) | Performance, Does the average mean anything? | A good average is no use if your one path ends. |
| [Flat vs compounding results](../axes/flat-vs-compounding-results.md) | Performance, Does the average mean anything? | Compounding sends one path far from the crowd's average. |
| [Equal vs unequal error costs](../axes/equal-vs-unequal-error-costs.md) | No home | It breaks the even loss behind averaging, which isn't one of the seven. |
| [Winnable vs no-win](../axes/winnable-vs-no-win.md) | No home | Losing less is still optimising, so nothing breaks. |
| [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) | No home | Learning from examples is what the playbook already does. |
| [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md) | No home | A skill with no ceiling breaks none of the seven. |
| [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | Agent, Same each time? | The case isn't drawn from the spread the solver learnt on. |
| [General vs local knowledge](../axes/general-vs-local-knowledge.md) | No home | Where the facts live is not one of the seven. |
| [Skin in the game vs none](../axes/skin-in-the-game-vs-none.md) | No home | Who bears the result is not one of the seven. |
| [Private vs accountable](../axes/private-vs-accountable.md) | Agent, Does looking change it? | Knowing you will be judged changes how you choose. |

## What it shows

### Empty cells

Nineteen of the 35 cells are empty. Most of them name a question an axis already asks from another cell, because the same assumption can break in more than one group.

| Cell | Candidate axis | The question | Status |
|---|---|---|---|
| Information, Same tomorrow? | Fresh vs stale evidence | Does what you learnt still describe the world now? | Already an axis: [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) |
| Information, Does the average mean anything? | Pooled vs personal evidence | Does evidence pooled across people tell you how one person changes? | Already an axis: [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md), with each person as a run |
| Information, Small cause, small effect? | Small vs growing errors | Can a small error in what you know grow into a big error in what you conclude? | Already an axis: [Stable vs chaotic](../axes/stable-vs-chaotic.md) |
| Information, Is halfway good? | Close vs misleading guesses | Does being near a good answer tell you yours is nearly as good? | Already an axis: [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) |
| Actions, Same each time? | Independent vs linked moves | Is each move a fresh try that leaves the next one alone? | Already an axis: [Standalone vs sequential](../axes/standalone-vs-sequential.md) |
| Actions, Same tomorrow? | Lasting vs fading levers | Does a move that worked last year still work, or does the world adapt to it? | Already an axis: [Antifragile vs wears out](../axes/antifragile-vs-wears-out.md), with bacteria hardening to antibiotics |
| Actions, Small cause, small effect? | Proportional vs threshold moves | Does twice the push give twice the result? | Already an axis: [Self-righting vs tipping](../axes/self-righting-vs-tipping.md), whose pushes can come from you |
| Actions, Does looking change it? | Price taker vs price maker | Does your own move shift the prices you planned around, as when a big fund sells? | Untested. Crowded vs empty field was [already tested](../log.md#2026-10-27), but that was about others acting, not your own move |
| Actions, Is halfway good? | Divisible vs all-or-nothing moves | Can you do part of the move for part of the gain, or is half a bridge worth nothing? | Untested |
| Performance, Same each time? | Independent vs correlated losses | Do losses land one at a time, or all at once, as when one hurricane hits every policy? | Untested |
| Performance, Same tomorrow? | Fixed vs moving goal | Does what counts as good stay put while you work? | [Already tested](../CONTRIBUTING.md#is-it-a-new-axis) |
| Performance, Small cause, small effect? | Steady vs stepped value | Does value rise in step with quality? | Already an axis: [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) |
| Performance, Do the parts add up? | Additive vs entangled goals | Can you score each goal alone and add them, or does one goal's worth hang on another? | Untested |
| Performance, Does looking change it? | Steady vs gamed score | Does the score still mean the same once people aim at it? | Already an axis: [Neutral vs adversarial](../axes/neutral-vs-adversarial.md), via Goodhart's law |
| Agent, Same tomorrow? | Steady vs shifting solver | Does the solver stay the same, or change through fatigue, turnover or an update? | Untested |
| Agent, Does the average mean anything? | Average vs own track record | Does the average solver's career tell you how this one's will go? | Already an axis: [Flat vs compounding results](../axes/flat-vs-compounding-results.md), whose example is a scientist's reputation |
| Agent, Small cause, small effect? | Graded vs winner-takes-all | Does a small edge in skill bring a small edge in result, or does the best solver take everything? | Untested |
| Agent, Do the parts add up? | Additive vs weakest-link teamwork | Can solvers each do a piece and add their work, or does the team move at its weakest member's pace? | [Already tested](../log.md#2026-10-29), and folded into [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md), since a team that hangs on its weakest member is one bet |
| Agent, Is halfway good? | Blendable vs pick-one methods | Does a blend of two good solvers' methods also work? | Already an axis: [Convergent vs divergent](../axes/convergent-vs-divergent.md) |

### Overfull cells

- **Environment, Small cause, small effect?** (Chaotic, Tipping point, Exacting landscape). Split, not merge. Chaos is errors growing over time, tipping is a threshold after a push and exacting is a sharp landscape with no time in it.
- **Information, Same each time?** (Knightian uncertainty, Observational, Scarce data, Live only). All four ask whether your evidence is a fair sample of the case in front of you, for four different reasons. Knightian uncertainty and Scarce data are the closest, since Knight's test is a long record of like cases, and they are worth a merge review.

### Straddles and axes with no home

There are two straddles.

- [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) asks whether runs are draws from one spread and whether their pooled average means anything.
- [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) asks whether small changes stay small and whether small steps find the top.

There are 24 axes with no home, nearly half the set. Most break some other assumption the playbook makes, which the seven columns don't name. The table groups them by what breaks instead.

| What breaks instead | Axes |
|---|---|
| Nothing, since the hard end is the playbook's own case | [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md), [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md), [High vs low base rate](../axes/high-vs-low-base-rate.md), [Satisficing vs optimising](../axes/satisficing-vs-optimising.md), [Single objective vs trade-offs](../axes/single-objective-vs-trade-offs.md), [Winnable vs no-win](../axes/winnable-vs-no-win.md) |
| Time to think, act and learn | [Turn-based vs real-time](../axes/turn-based-vs-real-time.md), [Ample time vs time pressure](../axes/ample-time-vs-time-pressure.md), [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) |
| Cheap search and cheap checks | [Tractable vs intractable options](../axes/tractable-vs-intractable-options.md), [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) |
| A fixed list of facts, outcomes, options or problem | [Known vs unknown unknowns](../axes/known-vs-unknown-unknowns.md), [Foreseeable vs unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md), [Given vs invented options](../axes/given-vs-invented-options.md), [Well vs ill-structured](../axes/well-vs-ill-structured.md) |
| A single, even, complete score with one owner | [Shared vs contested values](../axes/shared-vs-contested-values.md), [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md), [Equal vs unequal error costs](../axes/equal-vs-unequal-error-costs.md), [Curable vs chronic](../axes/curable-vs-chronic.md) |
| A solver who holds the levers, has the know-how and pays for mistakes | [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md), [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md), [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md), [General vs local knowledge](../axes/general-vs-local-knowledge.md), [Skin in the game vs none](../axes/skin-in-the-game-vs-none.md) |

### Axes outside their group

None. Every axis that found a cell landed in its own row. The columns ask about the process, not about who faces it, so they never pull an axis across rows. The grid neither backs the groups nor questions them.

## Verdict

The grid fails. Only 26 of the 50 axes find a cell, and 24 have no home. The two straddles are fair and only two cells are overfull. But of the 19 empty cells, 11 are questions an axis already asks from another cell, two were already tested and only six are new leads. The seven assumptions are about the data and the process. So they sort the Environment group and the evidence half of Information well, and say almost nothing about options, goals or the solver.

What it sees that the groups don't is one assumption breaking in several places. Six axes in three groups break ergodicity: Incoherent runs, Fat tails, Single bet, Irreversible, Ruinous and Compounding results. The groups file them under Randomness, Options, Control and Stakes, yet one move serves all six, which is to judge by the one path you live and not by the crowd's average. In the same way, six axes in three groups break i.i.d., from Scattered runs through four kinds of evidence to Novel to the solver. The 24 axes with no home are useful too. They list what the playbook assumes beyond the textbook seven: a fixed menu, a single score with one owner, time to think and a solver who pays for their own mistakes.
