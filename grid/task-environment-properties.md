---
type: Grid
title: Task environment properties
description: Crosses the five groups with Russell and Norvig's seven properties of a task environment, from partly observable to unknown rules. It fills the environment and information rows, but leaves 22 axes with no home, nearly all from performance, information evidence and the agent.
columns_from:
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Task environment properties

**Asks of each group whether it breaks one of Russell and Norvig's seven properties of a task environment, such as whether you can see the whole state or whether chance plays a part.**

## The columns

The five rows come from Russell and Norvig's PEAS. The columns come from their seven properties of a task environment, so this grid crosses their two lists with each other. Each property has an easy side and a hard side. The header gives the easy side, as the book names it, and each column is filled by axes whose hard end breaks that property.

| Column | The question | Where it comes from |
|---|---|---|
| Observable | Partly observable? Can you not see the whole state at once? | [Task environment properties](../frameworks/1995-task-environment-properties.md), fully vs partly observable |
| Deterministic | Stochastic? Does the next state depend on chance as well as on the current state and your move? | [Task environment properties](../frameworks/1995-task-environment-properties.md), deterministic vs stochastic |
| Episodic | Sequential? Does today's choice change the cases you face later? | [Task environment properties](../frameworks/1995-task-environment-properties.md), episodic vs sequential |
| Static | Dynamic? Does the world change while you are thinking? | [Task environment properties](../frameworks/1995-task-environment-properties.md), static vs dynamic |
| Discrete | Continuous? Are states, time or moves smooth rather than a countable set? | [Task environment properties](../frameworks/1995-task-environment-properties.md), discrete vs continuous |
| Single agent | Multi agent? Are other agents acting in the same world, whether helping or competing? | [Task environment properties](../frameworks/1995-task-environment-properties.md), single vs multi agent (added in later editions) |
| Known | Unknown rules? Do you not know how the world responds to your moves? | [Task environment properties](../frameworks/1995-task-environment-properties.md), known vs unknown (added in later editions) |

## The grid

| Group | Observable | Deterministic | Episodic | Static | Discrete | Single agent | Known |
|---|---|---|---|---|---|---|---|
| Environment | *empty* | [Stochastic](../axes/deterministic-vs-stochastic.md), [Incoherent runs](../axes/coherent-vs-incoherent-runs.md), [Scattered runs](../axes/clustered-vs-scattered-runs.md), [Fat tails](../axes/thin-vs-fat-tails.md) | [Tipping point](../axes/self-righting-vs-tipping.md), [Wears out](../axes/antifragile-vs-wears-out.md) | [Real-time world](../axes/turn-based-vs-real-time.md), [Cascading system](../axes/buffered-vs-cascading.md) | *empty* | [Reflexive](../axes/inert-vs-reflexive.md), [Adversarial](../axes/neutral-vs-adversarial.md) | [Perishable lessons](../axes/durable-vs-perishable-lessons.md) |
| Information | [Asymmetric information](../axes/symmetric-vs-asymmetric-information.md) | [Irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | *empty* | *empty* | *empty* | *[Asymmetric information](../axes/symmetric-vs-asymmetric-information.md)* | [Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md), [Unknown unknowns](../axes/known-vs-unknown-unknowns.md), [Unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md), [Opaque causes](../axes/transparent-vs-opaque-causes.md) |
| Actions | *empty* | *empty* | [Sequential](../axes/standalone-vs-sequential.md), [Irreversible](../axes/reversible-vs-irreversible.md) | [Time pressure](../axes/ample-time-vs-time-pressure.md) | *empty* | [Needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) | *empty* |
| Performance | [Proxy measure](../axes/direct-vs-proxy-measure.md) | *empty* | [Ruinous](../axes/survivable-vs-ruinous.md), [Compounding results](../axes/flat-vs-compounding-results.md) | *empty* | *empty* | [Contested values](../axes/shared-vs-contested-values.md) | [Ill-structured](../axes/well-vs-ill-structured.md) |
| Agent | [Local knowledge](../axes/general-vs-local-knowledge.md) | *empty* | *empty* | *empty* | *empty* | *empty* | [Novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) |

## Where each axis goes

| Axis | Cell | Why |
|---|---|---|
| [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) | Environment, Deterministic | The same move gives different results by chance, which is the column word for word. |
| [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) | Environment, Deterministic | Chance decides where each whole run settles. |
| [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) | Environment, Deterministic | It asks how chance spreads the runs that disagree. |
| [Thin vs fat tails](../axes/thin-vs-fat-tails.md) | Environment, Deterministic | It asks how heavy the tails of the chance are. |
| [Stable vs chaotic](../axes/stable-vs-chaotic.md) | No home | Chaos is deterministic, so the book rates the weather two weeks out as easy, and no column asks how fast small errors grow. |
| [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) | Environment, Known | The rules behind the data drift, so rules you once knew become unknown. |
| [Turn-based vs real-time](../axes/turn-based-vs-real-time.md) | Environment, Static | The world moves while you think. |
| [Self-righting vs tipping](../axes/self-righting-vs-tipping.md) | Environment, Episodic | One push past the point changes every case after it. |
| [Antifragile vs wears out](../axes/antifragile-vs-wears-out.md) | Environment, Episodic | Each use spends life that later cases needed. |
| [Buffered vs cascading](../axes/buffered-vs-cascading.md) | Environment, Static | The fault spreads faster than anyone can think and react. |
| [Inert vs reflexive](../axes/inert-vs-reflexive.md) | Environment, Single agent | Other people act on your forecast and change what it describes. |
| [Neutral vs adversarial](../axes/neutral-vs-adversarial.md) | Environment, Single agent | Another agent studies your rule and works against it. |
| [Reductionist vs holistic](../axes/reductionist-vs-holistic.md) | No home | None of the seven asks whether the parts can be solved one at a time. |
| [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) | No home | It asks how sharply the result jumps, not whether the states are smooth or countable. |
| [Tractable vs intractable options](../axes/tractable-vs-intractable-options.md) | No home | Go is discrete, deterministic and fully visible, and no column asks how many options there are. |
| [Risk vs Knightian uncertainty](../axes/risk-vs-knightian-uncertainty.md) | Information, Known | You can't put numbers on the outcomes, which is what the book means by an unknown world. |
| [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | Information, Deterministic | The answer isn't fixed yet and rests on chance, while the hidden but findable easy end is the partly observable case. |
| [Known vs unknown unknowns](../axes/known-vs-unknown-unknowns.md) | Information, Known | Your model of the world is missing pieces you don't know about. |
| [Foreseeable vs unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md) | Information, Known | You can't list what your moves might lead to. |
| [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) | Information, Known | You can't follow how the world turns a move into a result. |
| [Interventional vs observational](../axes/interventional-vs-observational.md) | No home | No column asks whether you can run an experiment. |
| [Symmetric vs asymmetric information](../axes/symmetric-vs-asymmetric-information.md) | Information, Observable and Information, Single agent | You can't see part of the state, and another agent picks what you do see. |
| [Plentiful vs scarce data](../axes/plentiful-vs-scarce-data.md) | No home | A reactor's rules are well known yet accident data is scarce, so this isn't unknown rules. |
| [High vs low base rate](../axes/high-vs-low-base-rate.md) | No home | No column asks how rare the target is. |
| [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) | No home | It asks what checking an answer costs, which no column asks. |
| [Rehearsable vs live only](../axes/rehearsable-vs-live-only.md) | No home | No column asks whether a faithful copy exists. |
| [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) | No home | Sequential asks whether a choice changes later cases, not how long its result takes to show. |
| [Given vs invented options](../axes/given-vs-invented-options.md) | No home | The book takes the list of moves as given, so no column asks whether you must invent it. |
| [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md) | No home | The hard end is one whole choice, which is the discrete side, so the column points the wrong way. |
| [Standalone vs sequential](../axes/standalone-vs-sequential.md) | Actions, Episodic | This is the column word for word. |
| [Reversible vs irreversible](../axes/reversible-vs-irreversible.md) | Actions, Episodic | A move you can't undo shapes every case that follows. |
| [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) | Actions, Single agent | The fix needs other agents to act. |
| [Ample time vs time pressure](../axes/ample-time-vs-time-pressure.md) | Actions, Static | The world won't wait while you decide. |
| [Well vs ill-structured](../axes/well-vs-ill-structured.md) | Performance, Known | Nobody gives you the goal or the moves, let alone how they work. |
| [Convergent vs divergent](../axes/convergent-vs-divergent.md) | No home | Good answers that differ in kind are separate points, so again the hard end is the discrete side. |
| [Single objective vs trade-offs](../axes/single-objective-vs-trade-offs.md) | No home | No column asks how many goals pull against each other. |
| [Shared vs contested values](../axes/shared-vs-contested-values.md) | Performance, Single agent | Other agents with their own rankings have a say in what counts as good. |
| [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) | No home | No column asks whether clearing a bar is enough. |
| [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md) | Performance, Observable | You only see a stand-in for what you want, not the whole of it. |
| [Curable vs chronic](../axes/curable-vs-chronic.md) | No home | The book's episodic asks whether cases are independent, not whether the task ever ends. |
| [Survivable vs ruinous](../axes/survivable-vs-ruinous.md) | Performance, Episodic | One bad result ends every case after it. |
| [Flat vs compounding results](../axes/flat-vs-compounding-results.md) | Performance, Episodic | Each result changes what you start the next round with. |
| [Equal vs unequal error costs](../axes/equal-vs-unequal-error-costs.md) | No home | No column asks how a miss compares with a false alarm. |
| [Winnable vs no-win](../axes/winnable-vs-no-win.md) | No home | No column asks whether the best outcome is still a loss. |
| [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) | No home | The expert knows the rules but can't say them, which isn't unknown rules. |
| [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md) | No home | No column asks whether skill has a ceiling. |
| [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | Agent, Known | The book says known is about what the agent knows, and a novel problem is one this solver doesn't know the rules of. |
| [General vs local knowledge](../axes/general-vs-local-knowledge.md) | Agent, Observable | The facts that matter are visible only to people close to them. |
| [Skin in the game vs none](../axes/skin-in-the-game-vs-none.md) | No home | The person who pays needn't act at all, so it isn't multi agent. |
| [Private vs accountable](../axes/private-vs-accountable.md) | No home | Others judge the call but don't act in the world, so it isn't multi agent. |

## What it shows

### Empty cells

| Cell | Candidate axis | The question | Status |
|---|---|---|---|
| Environment, Observable | Visible vs hidden state | Does the world show its whole state to anyone who looks? | Already an axis: [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md), whose easy end is hidden but findable facts |
| Environment, Discrete | Smooth vs stepped states | Can the world change by small amounts, or only jump between separate states? | Untested |
| Information, Episodic | Seen vs unseen roads | Does today's choice decide which results you get to see later? | [Already tested](../log.md#2026-10-22) as the road not taken |
| Information, Static | Fresh vs stale facts | Do the facts you hold go out of date while you think? | Already an axis: [Turn-based vs real-time](../axes/turn-based-vs-real-time.md) |
| Information, Discrete | Counted vs measured readings | Do readings come as smooth amounts rather than counts? | Not a question |
| Actions, Observable | Seen vs unseen effects | Can you not see what your own move did? | Already an axis: [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md), whose hard end says the result may never come |
| Actions, Deterministic | Clean vs shaky execution | Does the move you pick come off as you meant it? | Untested. Close to [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md), but there the world adds the noise and here your own hand does |
| Actions, Discrete | Fine vs all or nothing moves | Can you adjust a move by small amounts? | Already an axis: [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md), with the ends the other way round |
| Actions, Known | Tried vs untried moves | Do you not know what your moves will do? | Already an axis: [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) |
| Performance, Deterministic | Earned vs lucky results | Does chance set your score even after a good choice? | [Already tested](../log.md#2026-10-22) as the noisy grade |
| Performance, Static | Fixed vs moving goal | Does the goal change while you work on it? | [Already tested](../CONTRIBUTING.md#is-it-a-new-axis) |
| Performance, Discrete | Pass mark vs sliding scale | Is the score a smooth scale rather than pass or fail? | Already an axis: [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) |
| Agent, Deterministic | Consistent vs inconsistent solver | Does the same solver give a different answer to the same case on a second go? | Untested |
| Agent, Episodic | Standalone vs sequential solving | Does the solver's choice today change the cases they face later? | Already an axis: [Standalone vs sequential](../axes/standalone-vs-sequential.md), since the solver's choices are the moves |
| Agent, Static | Fresh vs stale know-how | Does the solver's know-how go stale while they work? | Already an axis: [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) |
| Agent, Discrete | Stepped vs smooth skill | Is skill a smooth scale rather than a set of steps? | Not a question |
| Agent, Single agent | Solo vs team solver | Do other people act alongside the solver on the same task? | Already an axis: [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) |

### Overfull cells

- **Environment, Deterministic** (4). No merge. Each asks a different thing about chance: whether it acts, whether whole runs agree, how they disagree and how heavy the tails are. The book has one property where the repo has a whole set, Randomness.
- **Information, Known** (4). Review [Unknown unknowns](../axes/known-vs-unknown-unknowns.md) against [Unforeseeable outcomes](../axes/foreseeable-vs-unforeseeable-outcomes.md), since one is missing facts and the other missing outcomes. Knightian uncertainty (no trusted numbers on a known list) and opaque causes (no view of the chain) ask different things.

### Straddles and axes with no home

- **Straddle:** [Symmetric vs asymmetric information](../axes/symmetric-vs-asymmetric-information.md) is partly observable and multi agent in full, since the other side picks what you see.
- **No home, Environment** (4): Chaotic, Holistic problem, Exacting landscape and Intractable options. None of the seven asks about error growth, parts, sharpness or size.
- **No home, Information** (6): Observational, Scarce data, Low base rate, Unverifiable, Live only and Delayed feedback. The whole Evidence set but one is missing, because the book asks what the world is like, not how you learn about it.
- **No home, Actions** (2): Invented options and Single bet. The book takes the moves as given.
- **No home, Performance** (6): Divergent, Trade-offs, Optimising, Chronic, Unequal error costs and No-win. The book treats the performance measure as fixed by the designer.
- **No home, Agent** (4): Tacit know-how, Open-ended skill, No skin in the game and Accountable choice. The book's agent is a program with no pay and nobody to answer to.

Three of these hard ends sit on the easy side of a column. Single bet and Divergent are the discrete side, and Chaotic is the deterministic side.

### Axes outside their group

None. Every placed axis landed in its own row. That is no sign the groups are right. The columns only ask which property breaks, never which part of PEAS an axis is about, so nothing pulls an axis into another row.

## Verdict

It fails. 22 of 50 axes have no home, and they come from the Performance, Agent and Evidence parts of the repo. Only one axis straddles, but the empties are weak too. Of 17, only three are untested leads: smooth vs stepped states, which may fold into Forgiving vs exacting, a move that doesn't come off as meant, and a solver that answers the same case two ways. The rest are already axes, already tested or not questions at all.

Using the same book for rows and columns is partly circular. The seven properties describe the E in PEAS and a little of the S and A, so they say nothing about the P or the agent. Those rows were bound to be empty. The Environment row was also partly built from this framework, which feeds six axes, so its full row is by design rather than a test. What the grid does see is real. Chaos slips through as deterministic, so the book's list would rate the weather two weeks out as an easy world. Its single "known" property covers four repo axes. And plain hidden state, with no rival picking what you see, has no axis of its own beyond the easy end of Reducible vs irreducible uncertainty.
