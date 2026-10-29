---
type: Guide
title: Testing the groups with grids
description: Three grids that cross the five axis groups with a second set of questions, so a missing axis shows up as an empty cell, and how they beat the three we ditched.
---
# Testing the groups with grids

**Three grids that cross the five axis groups with a second set of questions, so a missing axis shows up as an empty cell.**

## Start here

| Grid | The columns ask | Verdict |
|---|---|---|
| [Sources of difficulty](sources-of-difficulty.md) | What makes it hard: does it vary, move, interact, hold others, hide, sprawl or resist undoing? | **Keep.** It finds what the ditched Task environment properties grid found, with fewer axes left over |
| [Which assumption breaks](which-assumption-breaks.md) | Which textbook assumption fails: i.i.d., stationarity, ergodicity, linearity, separability, observer independence or convexity? | **Keep** as a gap finder. Most leads and the least overlap, but half the axes have no home |
| [Second party](second-party.md) | Who is on the other side: nobody, nature, allies, rivals or your future self? | **Keep.** Places 49 of 50 and is the only grid that sorts by who causes the trouble |

The shared row axis means every grid can be read against [placements.csv](placements.csv), which holds the cell each grid gave each axis. It keeps the columns of the three [ditched grids](#ditched-grids) too, since the tables below are counted from all six.

## What is this?

The axes sit in five groups, and each group splits into sets named after the axes already in it. So a missing axis has no empty slot to show up in. A grid fixes that by crossing the five groups with a second list of questions, written down before any axis is placed. An empty cell is then a question nobody has asked yet.

We built six grids, each with its columns taken from a different idea, and kept three. Two grids that leave the same cells empty are measuring the same thing, so one can go. A grid that leaves an axis with no home, or crams many axes into one cell, fails as a test.

## How the grids scored

Counted from [placements.csv](placements.csv). A cell is filled if any axis sits in it, even as a second cell. A cell is overfull with 3 or more axes that call it their first cell.

| Grid | Columns | Filled | Empty | Overfull | No home | Straddles | Outside group | Untested leads |
|---|---|---|---|---|---|---|---|---|
| Sources of difficulty | 7 | 21 | 14 | 3 | 14 | 2 | 1 | 4 |
| Which assumption breaks | 7 | 16 | 19 | 2 | 24 | 2 | 0 | 6 |
| Kind vs wicked loop (ditched) | 5 | 16 | 9 | 4 | 20 | 3 | 0 | 2 |
| Task environment properties (ditched) | 7 | 18 | 17 | 2 | 22 | 1 | 0 | 3 |
| Second party | 5 | 17 | 8 | 8 | 1 | 2 | 0 | 3 |
| Solving loop stage (ditched) | 5 | 18 | 7 | 7 | 2 | 3 | 0 | 2 |

No grid passes. Each fails one of two ways, and the two trade against each other.

1. **Narrow columns leave axes with no home.** The four grids whose columns name a property of the world each leave 14 to 24 axes over. Every one of those column sets comes from a framework about the environment, so none of them asks about goals, stakes or the solver. [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) has no home in five grids, and [Winnable vs no-win](../axes/winnable-vs-no-win.md), [Satisficing vs optimising](../axes/satisficing-vs-optimising.md), [Given vs invented options](../axes/given-vs-invented-options.md), [Equal vs unequal error costs](../axes/equal-vs-unequal-error-costs.md) and [Bounded vs open-ended skill](../axes/bounded-vs-open-ended-skill.md) in four.
2. **Broad columns cram axes together.** Second party and Solving loop stage place nearly everything, but only because Nobody and Nature hold 41 axes in one, and Modelling and Deciding hold 33 in the other.

Only one axis left its group in any grid. Sources of difficulty moved [Tractable vs intractable options](../axes/tractable-vs-intractable-options.md) from Environment to Actions, since a search too big to run is a limit on your options. So the grids test the sets inside each group, not the five groups themselves.

## Gaps more than one grid found

Each empty cell was turned into a candidate axis. These are the candidates that more than one grid came up with, in different words.

| Candidate | Grids that flag it | Status |
|---|---|---|
| Consistent vs noisy judgement. Does the same solver give the same answer to the same case? | Sources of difficulty, Task environment properties (ditched), Second party | Untested |
| Clean vs shaky execution. Does the move you pick come off as you meant it? | Sources of difficulty, Task environment properties (ditched), Solving loop stage (ditched) | Untested, close to [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) and [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) |
| Steady vs drifting solver. Does the solver change over the task, through fatigue, turnover, forgetting or an update? | Sources of difficulty, Which assumption breaks, Solving loop stage (ditched) | Untested |
| Solo vs coordinated. Does the result hang on several people's moves fitting together? | Second party, Which assumption breaks, Task environment properties (ditched), Sources of difficulty | Split. Two grids call it untested and two say [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md) or [Reductionist vs holistic](../axes/reductionist-vs-holistic.md) already asks it |
| Absolute vs relative standard. Is good a fixed bar, or beating what rivals manage? | Second party, Which assumption breaks | Untested, close to [Flat vs compounding results](../axes/flat-vs-compounding-results.md) |
| Divisible vs all-or-nothing moves. Can you do part of a move for part of the gain? | Which assumption breaks, Task environment properties (ditched) | Split. One grid calls it untested and one says [Diversifiable vs single bet](../axes/diversifiable-vs-single-bet.md) already asks it |
| Fixed vs moving goal | Which assumption breaks, Kind vs wicked loop (ditched), Task environment properties (ditched), Solving loop stage (ditched) | [Already tested](../CONTRIBUTING.md#is-it-a-new-axis) |
| Clean vs noisy readings, including noisy grading and lucky results | Sources of difficulty, Task environment properties (ditched) | [Already tested](../log.md#2026-10-27) |
| Can you see what your move did? | Sources of difficulty, Kind vs wicked loop (ditched), Task environment properties (ditched), Solving loop stage (ditched) | Already an axis, [Immediate vs delayed feedback](../axes/immediate-vs-delayed-feedback.md) |
| Fresh vs stale facts | Sources of difficulty, Which assumption breaks, Task environment properties (ditched) | Already an axis, [Turn-based vs real-time](../axes/turn-based-vs-real-time.md) or [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md) |
| Can you see the state? | Sources of difficulty, Task environment properties (ditched) | Already an axis, [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) |
| Does the score still mean the same once people aim at it? | Which assumption breaks, Kind vs wicked loop (ditched) | Already an axis, [Direct vs proxy measure](../axes/direct-vs-proxy-measure.md) |

Many empty cells point at ideas the log has already tested, and Fixed vs moving goal came up four times. So a cell can ask a real question and still not need a new axis.

The three strongest new leads are all about the solver. Five of the six grids asked in some form whether the solver is steady, and the Know-how and Incentives sets have no axis for a solver who is noisy, slips or drifts. The Agent group asks whether a solver fits the task, but never whether the solver behaves the same way twice.

Sources of difficulty and Task environment properties share seven of these candidates, more than any other pair. Their columns are near copies: varies matches stochastic, moves matches dynamic, see matches observable and others matches multi agent. So they are measuring the same thing.

## How alike the grids cut

For each pair of grids, this is the share of axis pairs that sit in one cell together in either grid that also sit together in the other. Axes with no home are left out.

| | Sources | Assumption | Loop | Russell and Norvig | Second party | Stage |
|---|---|---|---|---|---|---|
| Sources of difficulty | | 0.10 | 0.20 | 0.20 | 0.16 | 0.10 |
| Which assumption breaks | 0.10 | | 0.16 | 0.10 | 0.06 | 0.05 |
| Kind vs wicked loop (ditched) | 0.20 | 0.16 | | 0.15 | 0.19 | 0.14 |
| Task environment properties (ditched) | 0.20 | 0.10 | 0.15 | | 0.10 | 0.12 |
| Second party | 0.16 | 0.06 | 0.19 | 0.10 | | 0.28 |
| Solving loop stage (ditched) | 0.10 | 0.05 | 0.14 | 0.12 | 0.28 | |

Every pair is low, so the six column sets cut the axes in different ways. The highest pair, Second party and Solving loop stage, is high because both put many axes in a few big cells, not because they ask the same thing. Which assumption breaks overlaps least with every other grid.

## Verdict

Keep three. Sources of difficulty, Which assumption breaks and Second party ask three different things: what makes it hard, which assumption fails and who is on the other side. Their empties overlap little, and between them they found every untested lead in the table above. Ditch Task environment properties, since it repeats Sources of difficulty with more axes left over and shares a source with the rows. Ditch Solving loop stage and Kind vs wicked loop, since one crams and the other leaves the goal axes out.

No grid is fit to replace the sets. The kept grids are tools for finding gaps, and none places every axis cleanly. Run these candidates through the [new axis tests](../CONTRIBUTING.md#is-it-a-new-axis) next, in this order.

1. **Consistent vs noisy judgement.** Three grids found it, and nothing in the Agent group asks it. [Clinical vs statistical prediction](../frameworks/1954-clinical-vs-statistical-prediction.md) is the place to start.
2. **Steady vs drifting solver.** Three grids found it in some form. Test it against [Durable vs perishable lessons](../axes/durable-vs-perishable-lessons.md), which asks whether the world drifts, not the solver.
3. **Clean vs shaky execution.** Three grids found it. Test it against [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) and [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) taken together.
4. **Solo vs coordinated.** Four grids touched it, but they split on whether an axis already asks it. Test it against [Yours to fix vs needs others to change](../axes/yours-to-fix-vs-needs-others-to-change.md).
5. **Absolute vs relative standard.** Two grids found it. Test it against [Flat vs compounding results](../axes/flat-vs-compounding-results.md).

Leads only one kept grid found are on its page, under What it shows. The ditched grids' best finds are below.

## Ditched grids

| Grid | The columns asked | Why it went | Worth keeping |
|---|---|---|---|
| Kind vs wicked loop | Which link in learning from experience breaks? | Blind to goals and stakes. Twenty axes had no home, eight of them Performance axes, since the loop takes the goal as given | Two untested leads. Calibrated vs uncalibrated solver asks whether the solver can tell when its own judgement is right, from Kahneman and Klein. Portable vs context-bound moves asks whether a move that worked elsewhere works here, as California's copy of Tennessee's small classes did not |
| Task environment properties | Which of Russell and Norvig's seven properties breaks? | Circular with the rows, since the Environment row was partly built from the same book. It also repeats Sources of difficulty, sharing seven candidates, with 22 axes left over | The book rates chaos as deterministic, so it would call the weather two weeks out an easy world. One untested lead, Smooth vs stepped states, which asks whether the world can change by small amounts or only jump, and may fold into [Forgiving vs exacting](../axes/forgiving-vs-exacting.md) |
| Solving loop stage | At which stage of sense, model, decide, act and learn does it bite? | Two columns take two thirds of the axes. Modelling and Deciding held 33 of the 48 it placed | One untested lead, Steady vs slip-prone execution, which asks whether the task needs long runs of exact steps, so a slip is likely somewhere. And Performance collapses into Deciding, with 9 of its 11 axes there, so that column repeats the row |

The full pages are in commit b5d866d.

## How an axis is placed

The same rules hold on every grid, so the grids can be compared cell for cell.

1. **The rows are the five groups.** Environment, Information, Actions, Performance and Agent, in that order, on every grid.
2. **The columns come first.** Each grid writes its columns and their plain questions before placing anything, and never tunes them afterwards.
3. **Place by the hard end.** Ask what makes the hard end hard and which cell asks that question. An axis can land in a different row from its `group` if the grid says so. That mismatch is recorded, since it may mean the axis sits in the wrong group.
4. **One cell per axis.** A second cell only when the axis asks both questions in full. The second cell shows the axis in italics.
5. **Don't bend a column to fit.** If no column asks the axis's question, the axis has no home, and that counts against the grid.

## Adding a grid

Every grid page has the same parts, in this order.

| Part | What it holds |
|---|---|
| Front matter | `type: Grid`, `title`, `description` and `columns_from`, a list of `resource` and `title` like an axis's `sources`. A framework the columns come from links to its page |
| Tagline | One bold line saying what the columns ask |
| The columns | A table of column, plain question and where it comes from |
| The grid | Rows are the five groups and cells hold axes by their hard end label, linked to the axis page. An empty cell says *empty* |
| Where each axis goes | All 50 axes, each with its cell and a one line reason. A second cell only when the axis asks both questions. "No home" when no column fits |
| What it shows | Empty cells as candidate axes, overfull cells, axes with no home, axes that straddle two cells and axes that land outside their group |
| Verdict | Whether the grid passes: every axis placed, few straddles and empties that read as real questions |

Each grid also gets a column in [placements.csv](placements.csv), which the scorecard is counted from.
