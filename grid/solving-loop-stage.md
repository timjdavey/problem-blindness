---
type: Grid
title: Solving loop stage
description: The columns ask at which stage of a loop of sensing, modelling, deciding, acting and learning the hard end bites. The feared overlap with Information and Actions didn't happen, but Performance collapsed into Deciding and two columns took two thirds of the axes, so the grid fails as a test.
columns_from:
  - title: OODA loop (John Boyd)
  - resource: /frameworks/1978-single-vs-double-loop-learning.md
    title: Single vs double-loop learning
  - resource: /frameworks/1983-skill-rule-and-knowledge-based-behaviour.md
    title: Skill, rule and knowledge-based behaviour
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
  - resource: /frameworks/1954-signal-detection-theory.md
    title: Signal detection theory
  - resource: /frameworks/1986-uncertainty-vs-equivocality.md
    title: Uncertainty vs equivocality
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
---
# Solving loop stage

**Each column asks where in the loop of sensing, modelling, deciding, acting and learning the hard end makes the work go wrong.**

## The columns

The fighter pilot John Boyd described a loop that every solver runs. You observe, orient, decide and act, then observe again. This is called the OODA loop. We call orient modelling, and add a learning stage that Boyd folds into his feedback. We expected this grid to fail, because sensing looks like the Information row and acting like the Actions row. The verdict tests that.

| Column | The question | Where it comes from |
|---|---|---|
| Sensing | Is the trouble in taking in what is going on? | Boyd's observe. Russell and Norvig's agent senses its world ([Task environment properties](../frameworks/1995-task-environment-properties.md)), and picking a signal out of noise is a sensing job ([Signal detection theory](../frameworks/1954-signal-detection-theory.md)) |
| Modelling | Is it in making sense of what you see and predicting what comes next? | Boyd's orient. Rasmussen's top level, where you build a picture of how the system works ([Skill, rule and knowledge-based behaviour](../frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)), and Daft and Lengel's work on agreeing what events mean ([Uncertainty vs equivocality](../frameworks/1986-uncertainty-vs-equivocality.md)) |
| Deciding | Is it in choosing among the options, or in knowing what counts as good? | Boyd's decide. Argyris and Schön's second loop, which questions the goal itself ([Single vs double-loop learning](../frameworks/1978-single-vs-double-loop-learning.md)) |
| Acting | Is it in carrying the choice out in the world? | Boyd's act. Russell and Norvig's agent acts on its world, and Rasmussen's skill level fails through slips of the hand |
| Learning | Is it in seeing how it went and updating for next time? | Boyd's feedback back to observe. Argyris and Schön's first loop, which adjusts against a fixed goal, and Hogarth's split of quick, honest feedback from missing or misleading feedback ([Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)) |

## The grid

| Group | Sensing | Modelling | Deciding | Acting | Learning |
|---|---|---|---|---|---|
| Environment | [Real-time world](../axes/turn-based-vs-real-time.md) | [Stochastic](../axes/deterministic-vs-stochastic.md), [Incoherent runs](../axes/coherent-vs-incoherent-runs.md), [Scattered runs](../axes/clustered-vs-scattered-runs.md), [Fat tails](../axes/thin-vs-fat-tails.md), [Chaotic](../axes/stable-vs-chaotic.md), [Reflexive](../axes/inert-vs-reflexive.md), [Holistic problem](../axes/reductionist-vs-holistic.md) | [Adversarial](../axes/neutral-vs-adversarial.md), [Exacting landscape](../axes/forgiving-vs-exacting.md), [Intractable options](../axes/tractable-vs-intractable-options.md) | [Tipping point](../axes/self-righting-vs-tipping.md), [Wears out](../axes/antifragile-vs-wears-out.md), [Cascading system](../axes/buffered-vs-cascading.md) | [Perishable lessons](../axes/durable-vs-perishable-lessons.md) |
| Information | [Unknown unknowns](../axes/known-vs-unknown-unknowns.md), [Asymmetric information](../axes/symmetric-vs-asymmetric-information.md), [Low base rate](../axes/high-vs-low-base-rate.md) | [Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md), [Irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md), [Unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md), [Opaque causes](../axes/transparent-vs-opaque-causes.md), [Observational](../axes/interventional-vs-observational.md), [Scarce data](../axes/plentiful-vs-scarce-data.md) | [Unverifiable](../axes/verifiable-vs-unverifiable.md) | *empty* | [Delayed feedback](../axes/immediate-vs-delayed-feedback.md), [Live only](../axes/rehearsable-vs-live-only.md), *[Observational](../axes/interventional-vs-observational.md)* |
| Actions | *empty* | *empty* | [Invented options](../axes/given-vs-invented-options.md), [Single bet](../axes/diversifiable-vs-single-bet.md), [Time pressure](../axes/ample-time-vs-time-pressure.md), *[Sequential](../axes/standalone-vs-sequential.md)* | [Irreversible](../axes/reversible-vs-irreversible.md), [Needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) | [Sequential](../axes/standalone-vs-sequential.md) |
| Performance | *empty* | [Ill-structured](../axes/well-vs-ill-structured.md) | [Divergent](../axes/convergent-vs-divergent.md), [Trade-offs](../axes/single-objective-vs-trade-offs.md), [Contested values](../axes/shared-vs-contested-values.md), [Optimising](../axes/satisficing-vs-optimising.md), [Proxy measure](../axes/direct-vs-proxy-measure.md), [Ruinous](../axes/survivable-vs-ruinous.md), [Compounding results](../axes/flat-vs-compounding-results.md), [Unequal error costs](../axes/equal-vs-unequal-error-costs.md), [No-win](../axes/winnable-vs-no-win.md), *[Ill-structured](../axes/well-vs-ill-structured.md)* | [Chronic](../axes/curable-vs-chronic.md) | *empty* |
| Agent | [Local knowledge](../axes/general-vs-local-knowledge.md) | [Novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | [No skin in the game](../axes/skin-in-the-game-vs-none.md), [Accountable choice](../axes/private-vs-accountable.md) | *empty* | *empty* |

## Where each axis goes

| Axis | Cell | Why |
|---|---|---|
| [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) | Environment, Modelling | You can predict the rate but not the next case. |
| [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) | Environment, Modelling | The pooled forecast describes none of the runs. |
| [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) | Environment, Modelling | With no pattern to latch onto, you can't predict which outcome you are heading for. |
| [Thin vs fat tails](../axes/thin-vs-fat-tails.md) | Environment, Modelling | Past averages mislead any forecast of what comes next. |
| [Stable vs chaotic](../axes/stable-vs-chaotic.md) | Environment, Modelling | Tiny errors in the picture grow until the forecast is useless. |
| [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) | Environment, Learning | What you learnt last time stops working, so the update itself goes stale. |
| [Turn-based vs real-time](../axes/turn-based-vs-real-time.md) | Environment, Sensing | Your reading of the world goes stale while you work, so you must look again before every move. |
| [Self-righting vs tipping](../axes/self-righting-vs-tipping.md) | Environment, Acting | A push can flip the system, and stopping the push doesn't undo it. |
| [Antifragile vs wears out](../axes/antifragile-vs-wears-out.md) | Environment, Acting | Each use spends some of the system's life, so the doing itself is the cost. |
| [Buffered vs cascading](../axes/buffered-vs-cascading.md) | Environment, Acting | A fault spreads before anyone can step in and act. |
| [Inert vs reflexive](../axes/inert-vs-reflexive.md) | Environment, Modelling | Putting out a forecast changes the thing it forecasts. |
| [Neutral vs adversarial](../axes/neutral-vs-adversarial.md) | Environment, Deciding | Someone studies your rule and picks the cases it gets wrong, so the choice must hold up against them. |
| [Reductionist vs holistic](../axes/reductionist-vs-holistic.md) | Environment, Modelling | Each part only makes sense in light of the others. |
| [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) | Environment, Deciding | Being close to a good option tells you little, so the search for one stalls. |
| [Tractable vs intractable options](../axes/tractable-vs-intractable-options.md) | Environment, Deciding | There are too many options to try and keep the best. |
| [Risk vs Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md) | Information, Modelling | You can't put a number you trust on what comes next. |
| [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | Information, Modelling | No amount of looking helps, since the answer lies in a future you can only predict. |
| [Known vs unknown unknowns](../axes/known-vs-unknown-unknowns.md) | Information, Sensing | The facts that matter never get looked for. |
| [Foreseeable vs unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md) | Information, Modelling | You can't list what might come next. |
| [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) | Information, Modelling | You see every part but can't follow the chain. |
| [Interventional vs observational](../axes/interventional-vs-observational.md) | Information, Modelling and Information, Learning | Watching mixes cause with choice, and you only ever see how your own choices turned out. |
| [Symmetric vs asymmetric information](../axes/symmetric-vs-asymmetric-information.md) | Information, Sensing | The other side picks what reaches you. |
| [Plentiful vs scarce data](../axes/plentiful-vs-scarce-data.md) | Information, Modelling | Too few past cases to build the pattern from. |
| [High vs low base rate](../axes/high-vs-low-base-rate.md) | Information, Sensing | The screen you take the world in through gives mostly false alarms. |
| [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) | Information, Deciding | You can't check an option is good before you pick it. |
| [Rehearsable vs live only](../axes/rehearsable-vs-live-only.md) | Information, Learning | No dry run can teach you before the real go. |
| [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) | Information, Learning | The result arrives too late to update on. |
| [Given vs invented options](../axes/given-vs-invented-options.md) | Actions, Deciding | You must make up the options before you can choose. |
| [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md) | Actions, Deciding | Everything rides on one choice. |
| [Standalone vs sequential](../axes/standalone-vs-sequential.md) | Actions, Learning and Actions, Deciding | You can't tell which early move caused the result, and each choice has to plan for the ones it shapes. |
| [Reversible vs irreversible](../axes/reversible-vs-irreversible.md) | Actions, Acting | Once the move is carried out you are stuck with it. |
| [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) | Actions, Acting | Someone else has to carry it out. |
| [Ample time vs time pressure](../axes/ample-time-vs-time-pressure.md) | Actions, Deciding | You must choose before there is time to think. |
| [Well vs ill-structured](../axes/well-vs-ill-structured.md) | Performance, Modelling and Performance, Deciding | You must work out what the problem is, and often what the goal is. |
| [Convergent vs divergent](../axes/convergent-vs-divergent.md) | Performance, Deciding | You must commit to one kind of answer, since a blend is worse. |
| [Single objective vs trade-offs](../axes/single-objective-vs-trade-offs.md) | Performance, Deciding | Goals pull against each other, so good is a weighting. |
| [Shared vs contested values](../axes/shared-vs-contested-values.md) | Performance, Deciding | Nobody can settle what counts as good. |
| [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) | Performance, Deciding | Every extra bit of quality still pays, so the choice must be the best. |
| [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md) | Performance, Deciding | The score you choose by leaves out part of what counts as good. |
| [Curable vs chronic](../axes/curable-vs-chronic.md) | Performance, Acting | The work never ends, so carrying it out has to go on for good. |
| [Survivable vs ruinous](../axes/survivable-vs-ruinous.md) | Performance, Deciding | You must choose to avoid ruin before you choose by the odds. |
| [Flat vs compounding results](../axes/flat-vs-compounding-results.md) | Performance, Deciding | You must judge a choice by one path over time, not the average. |
| [Equal vs unequal error costs](../axes/equal-vs-unequal-error-costs.md) | Performance, Deciding | Where to set the bar depends on which mistake costs more. |
| [Winnable vs no-win](../axes/winnable-vs-no-win.md) | Performance, Deciding | Good means losing less. |
| [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) | No home | Tacit skill bites in the eyes, the gut and the hands alike, and the trouble is passing it on, which no stage asks. |
| [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md) | No home | The trouble is that no test can rate the solver, which is not a stage of the loop. |
| [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | Agent, Modelling | No stored rule fits, so the solver must build a picture from scratch. |
| [General vs local knowledge](../axes/general-vs-local-knowledge.md) | Agent, Sensing | The facts sit with people close to the case. |
| [Skin in the game vs none](../axes/skin-in-the-game-vs-none.md) | Agent, Deciding | The decider chooses without paying for the result. |
| [Private vs accountable](../axes/private-vs-accountable.md) | Agent, Deciding | The choice must be one you can defend to others. |

## What it shows

### Empty cells

| Cell | Candidate axis | The question | Status |
|---|---|---|---|
| Information, Acting | Confirmed vs unconfirmed moves | Once you act, can you see that the move took effect? | Already an axis: [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) asks how soon the world shows you the result |
| Actions, Sensing | Probing vs watching | Can your own moves be used to find out what is going on? | Already an axis: [Interventional vs observational](../axes/interventional-vs-observational.md) |
| Actions, Modelling | Known vs unknown effects of moves | Can you predict what each move will do? | Already an axis: [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) |
| Performance, Sensing | Readable vs unreadable score | Can you see how well you are doing while you work? | Already an axis: [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md), since a proxy exists because the real goal can't be read |
| Performance, Learning | Fixed vs moving goal | After seeing how it went, must you change what counts as good, not only your method? | [Already tested](../CONTRIBUTING.md#is-it-a-new-axis) |
| Agent, Acting | Steady vs slip-prone execution | Does the task ask the solver for long runs of exact steps, so a slip is likely somewhere? | Untested |
| Agent, Learning | Retained vs lost lessons | Does whoever solves the problem keep what they learnt for next time? | Untested |

Slip-prone execution sits close to [Forgiving vs exacting](../axes/forgiving-vs-exacting.md), which asks what a slip costs, not how likely one is. Lost lessons sit close to [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md), which asks whether the world keeps a lesson true, not whether the solver keeps it. Think of an AI model that starts each session blank.

### Overfull cells

- **Environment, Modelling (7).** All ask why a forecast fails, but for different reasons: spread, drift, reaction and links. Keep them apart. The cell is the Randomness set plus three friends.
- **Information, Modelling (6).** Knightian, irreducible and unforeseeable all ask about doubt over the future, and the repo already split them with care. Opaque, observational and scarce ask about building a causal picture. No merge.
- **Performance, Deciding (9).** This is the Performance group minus two axes. The column can't tell them apart, so it says nothing about merging. It shows the column repeats the row.
- **Environment, Deciding (3).** An opponent, a rugged landscape and too many options are three different reasons a search fails. Keep.
- **Environment, Acting (3).** This is the whole Stimulus set. Each asks what a push does, but one push, many pushes and a spreading fault are distinct. Keep.
- **Information, Sensing (3).** Facts not asked for, facts held back and facts drowned in false alarms. Keep.
- **Actions, Deciding (3).** No options yet, one shot and no time are unrelated. Keep.

### Straddles and axes with no home

- [Interventional vs observational](../axes/interventional-vs-observational.md) straddles Modelling and Learning. Its page has two halves, the nurses' study and the hiring manager who never sees the people turned away.
- [Standalone vs sequential](../axes/standalone-vs-sequential.md) straddles Learning and Deciding. Its hard end names the credit problem, and its moves plan for how choices shape each other.
- [Well vs ill-structured](../axes/well-vs-ill-structured.md) straddles Modelling and Deciding. Framing the problem and questioning the goal are both part of its job.
- [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) has no home. Tacit skill shows up at every stage, so the stage can't be what makes it hard.
- [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md) has no home. It asks whether you can rate the solver, which happens outside the loop.

### Axes outside their group

None. The columns ask when the trouble comes, not where it lives, so no axis had a reason to change row. This grid can't test the rows at all.

## Verdict

We feared that sensing would repeat Information and acting would repeat Actions. That didn't happen. Only 3 of the 12 Information axes sit in Sensing, and half sit in Modelling. Only 2 of the 6 Actions axes sit in Acting, and 3 sit in Deciding. But the columns repeat the rows anyway, just not the ones we expected. Nine of the 11 Performance axes land in Deciding, and 7 of the 15 Environment axes land in Modelling. Modelling and Deciding hold 33 of the 48 placed axes, while Sensing holds 5 and Learning 4. The grid places all but 2 axes with only 3 straddles, but 7 overfull cells and 5 empties already covered by other axes leave little to learn. It fails as a test of the groups.

It does see two things the groups miss. The Stimulus set is the only part of Environment about what your acts do to the world, and it reads more clearly as acting than as stimulus. And the Agent row only asks what the solver knows and wants. Nothing asks whether the solver's hands are steady or whether it remembers what it learnt. Those two empty cells are the only real leads here.
