---
type: Axis
title: Standalone vs sequential
description: "Standalone: each choice stands alone, so one doesn't change the next (e.g. checking invoices for fraud). Sequential: each choice shapes the next, so it is hard to tell which one caused the result (e.g. treating a long illness)."
group: actions
subgroup: options
easy_end: Standalone
hard_end: Sequential
sources:
  - resource: /frameworks/1933-multi-armed-bandit.md
    title: Multi-armed bandit
  - resource: /frameworks/1991-exploration-vs-exploitation.md
    title: Exploration vs exploitation
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
---
# Standalone vs sequential

An axis in the [Options](index.md#options) set of the [actions](index.md#actions) group.

Does each choice stand alone, or does it shape the ones that follow? Checking invoices for fraud is standalone. Flagging one invoice doesn't change the next, so each can be judged on its own. Treating a long illness is sequential. Each drug changes what the next one does, and it's hard to tell which early move caused the final result. Russell and Norvig call the first kind episodic ([Task environment properties](../frameworks/1995-task-environment-properties.md)).

Standalone doesn't mean one-shot. A single choice you can't repeat or take back is the hard end of [Reversible vs irreversible](reversible-vs-irreversible.md) and [Diversifiable vs single bet](diversifiable-vs-single-bet.md). This axis only asks whether your choices change each other.

## Actions

**Standalone**: Judge each case on its own.
- Treat each case as fresh. A clerk checking invoices needs no memory of the last one, which makes the job simpler to teach and to check.
- Score your work case by case. How many you get right in a fair sample of single cases is the whole story.
- Take cases in any order, or split them among several people. Nothing carries over between them.

**Sequential**: Act, watch and adjust.
- Balance trying new moves against repeating the ones that worked. A chef who only cooks the best seller never finds the next one, and one who keeps changing the menu never learns which dish works.
- Credit each move with its share of the final result. Otherwise the last move gets the blame for what an early one caused.
- Watch for effects that show up late. Judge a move by where it led, not by the next step.
- Keep room to change course. Each step should leave the next one open.
- Judge whole runs, not single steps. A negotiator can win every point and still lose the deal. An AI agent can get every step right and still end up somewhere useless.

## Correlated with

- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) and [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (study). In Senge's [beer game](../frameworks/1990-detail-vs-dynamic-complexity.md) delays between moves and results hide which move caused what.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (independent). Standalone choices can each be final, like a stream of loans where each one is gone once paid out. A chain of edits to a document is sequential, yet every step can be undone. Watch the name clash. [Rittel and Webber](../frameworks/1973-tame-vs-wicked-problems.md) call each try at a wicked problem a "one-shot operation", but they mean it can't be undone. That belongs on the reversible axis, not this one.
- [Additive vs multiplicative returns](additive-vs-multiplicative-returns.md) (by definition). Compounding is a sequential problem, since each bet's result sets the stake for the next. Bet the same fixed sum each round and the rounds stand alone, so the crowd's average is a fair guide ([Ergodicity](../frameworks/2016-ergodicity.md)).
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). Each step can show you a want the goal left out, so over a chain of choices the goal itself can move ([Single vs double-loop learning](../frameworks/1978-single-vs-double-loop-learning.md)).
- [Diversifiable vs single bet](diversifiable-vs-single-bet.md) (independent). That axis asks whether you can back several options at once. This one asks whether each choice shapes the next. A [bandit](../frameworks/1933-multi-armed-bandit.md) makes one pull at a time and each pull shapes what it tries next, while a fund can back a hundred shares and treat each as its own call.
- [Curable vs chronic](curable-vs-chronic.md) (logic). Each round of work on an ongoing problem starts from where the last one left things. But a chain of choices can still end, as treating a long illness does when the patient is well.
- [Static vs dynamic](static-vs-dynamic.md) (logic). Here your own choices change what comes next. In a dynamic world things change even if you do nothing. Chess by post is a long chain of choices, and the board still waits for you.

## Citations

[1] [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)

[2] [Exploration vs exploitation](../frameworks/1991-exploration-vs-exploitation.md)

[3] [Task environment properties](../frameworks/1995-task-environment-properties.md)
