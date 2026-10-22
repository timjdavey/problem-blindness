---
type: Guide
title: Reading the axes
description: How the axes are grouped, what the correlation labels mean and what changes at the hard end.
---
# Reading the axes

Each axis is a scale with two ends, and any problem sits somewhere along it. They fall into five groups, which follow the way Stuart Russell and Peter Norvig describe any task an AI agent faces. The first is the environment you act on. The second is the information you can get about it, and the third is the actions you can take. The fourth is the performance you are judged on, meaning what counts as good and what a miss costs. The last is the agent itself, meaning what the task asks of whoever solves it. Each group splits into a few smaller sets of axes that ask about the same thing. The [axes index](index.md) lists every axis under its group and set.

The Correlated with list under each axis names the other axes it tends to move with. On every axis the first end is the easy one and the second is the hard one. A few axes also name their middle, when it is a case of its own. A Word document is neither self-righting nor tipping. It stays wherever you push it. So "correlated" means a problem near the hard end of one axis tends to sit near the hard end of the other. A few entries say "opposite" when the hard end of one goes with the easy end of the other. "Tension" marks two hard ends that clash when they meet, and "independent" marks two axes that look linked but aren't.

Each entry also says where the link comes from. "By definition" means one axis is partly built into the other, so tagging both may count the same thing twice. "Bundled" means a framework puts both under one label. "Study" means there is evidence or a worked case showing them together. "Logic" means it follows from what the two axes mean.

Under each axis, the actions say what to do differently at each end, with the easy end first. Each one opens with a plain rule that holds for anyone. A list then says what that rule means when you build or deploy an AI model, since that is the main use of this project. The section [What changes at the hard end](#what-changes-at-the-hard-end) pulls out the pattern the actions share.

## The five groups

Russell and Norvig sum up a task with four letters, PEAS. They stand for the performance measure, the environment, the actuators an agent acts through and the sensors it learns through ([Task environment properties](../frameworks/1995-task-environment-properties.md)). The groups follow them, with plain words in place of sensors and actuators, and add a fifth group for the agent itself. Each group asks one question, and every axis in it answers part of that question.

- [Environment](index.md#environment). How does the system behave, whoever is looking at it?
  - [Randomness](index.md#randomness): what the spread of outcomes looks like.
  - [Change](index.md#change): how the system moves over time.
  - [Stimulus](index.md#stimulus): what a push does to the system, whether it comes from you or from outside.
  - [Reactivity](index.md#reactivity): whether the world notices your model and reacts to it.
  - [Structure](index.md#structure): how the parts fit together, and so how hard a good answer is to find.
- [Information](index.md#information). What can you find out, and how fast?
  - [Uncertainty](index.md#uncertainty): what kind of doubt you face.
  - [Evidence](index.md#evidence): how you can learn what is going on, and whether you can tell you were right.
- [Actions](index.md#actions). What moves do you have?
  - [Options](index.md#options): what choices are on the table and how they link.
  - [Control](index.md#control): whether you hold the levers, whether you can undo a move and how long you have.
- [Performance](index.md#performance). What counts as good, and what does a miss cost?
  - [Goal](index.md#goal): what a good answer looks like and who decides.
  - [Stakes](index.md#stakes): what it costs to be wrong.
- [Agent](index.md#agent). What does the task ask of whoever solves it? Here the same problem sits at different points for different solvers, so this is where you check whether a solver fits the task.
  - [Know-how](index.md#know-how): where the skill and the facts live.
  - [Incentives](index.md#incentives): who has to answer for the call and who pays for a mistake.

## What changes at the hard end

Read down the actions and the same move keeps turning up. Near the easy ends you can trust the test you ran before launch. A held-out test set predicts how the model will do in production, so you can automate fully, monitor lightly and plan the project like normal engineering. Spending months on live experiments or fallbacks here is waste.

As a problem moves towards the hard ends, the offline test stops being enough to decide on. What replaces it comes in a set order. First you pair the model with a checker, like tests, a rules engine or an expert, and let it act alone only where the checker can confirm the output. Next you stop trusting offline tests as the gate at all. You ship to small groups, run variants side by side and measure what happens downstream rather than how accurate the model is. At the far end you need a way to take the model out of the loop, such as people who can take over, a kill switch or a freeze on automated decisions when inputs stop looking like the training data. These four steps line up with the clear, complicated, complex and chaotic domains of [Cynefin](../frameworks/1999-cynefin.md).

A real problem sits near the hard end of several axes at once, and their actions can pull against each other. A drifting world says retrain often and ship fast, while a ruinous one says put a person at the door. When they clash, the action furthest along that order wins. A fallback and a cap on losses come before any experiment, and an experiment comes before trust in the offline test.

Both stories in the [overview](../README.md) show someone running the easy end playbook on a hard end problem. The reverse is a mistake too, just a cheaper one. Building bandits and kill switches for a stable task you can check in seconds wastes months you could have spent shipping it.

## Grain and horizon

Where a problem sits on most axes depends on how closely you look and over what time. One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate. Weather is chaotic two weeks out, while climate is steady over decades. So before you place a problem on any axis, say what scale and what timescale you mean, or the same problem will get tagged two different ways.

Split a task into its separate decisions before you tag it. The cardiology story in the [overview](../README.md) is one task with two problems inside it. Putting in a stent is a practised skill with fast, clear feedback. Deciding whether to put one in is a slow, statistical call where your gut misleads you. Tag the task as a whole and you average two different problems into one that doesn't exist.

Also ask whether you are deciding one case or setting a policy for many. In 1990 Donald Redelmeier and Amos Tversky gave doctors the same case in two forms. Seen as one patient, a student with fatigue got an extra $20 blood test 30% of the time. Seen as one of a group of patients just like them, the figure was 17% ([Individual vs group decisions](../frameworks/1990-individual-vs-group-decisions.md)). A single case feels special, so it gets the extra test. But a doctor who sees the same kind of patient every week is setting a policy whether they mean to or not, and should judge the choice that way.

## When is it a new axis?

Most ideas for a new axis turn out to be an old one in new words. So a new axis has to pass three tests.

The first is the corner test. Name a problem at the new axis's hard end that sits at the easy end of the axes closest to it. If you can't find one, the new axis is a copy of one of them.

The second is the action test. The hard end has to call for something the nearby axes don't already say. If it doesn't, the idea may still be real. But it belongs as a note on one of those axes.

The third is the combination test. No mix of two or three existing axes can land the same problems at the hard end and call for the same actions. An idea can pass the first two tests against each axis on its own and still fail this one.

Fixed vs moving goal looked like a gap until it met the third test. A couple planning a wedding for 100 people on 5 June for under £20k have a clear brief. Yet what they want shifts once they start seeing venues. That passes the corner test, since the brief is well structured and the world around it isn't drifting. But the brief left out wants the couple could only find by looking, which is the hard end of [Direct vs proxy measure](direct-vs-proxy-measure.md). They found them through a chain of choices where each shaped the next, which is the hard end of [Standalone vs sequential](standalone-vs-sequential.md). Those two axes already say what to do. Don't trust the brief to hold everything you want, and learn as you go. So moving goals went in as a note on those two axes.

## Three reasons for many good answers

Some axes look alike because they share a symptom. Three axes all describe problems with no one right answer, and they used to blur together. They split on why there are many good answers, and each reason calls for a different move.

| Why there are many good answers | Axis | Can you blend two good answers? | What to do |
|---|---|---|---|
| The goal has several parts that pull against each other | [Single objective vs trade-offs](single-objective-vs-trade-offs.md) | Yes, a blend sits on or near the trade off | Lay out the trade offs and let the owner set the weights |
| The good answers differ in kind | [Convergent vs divergent](convergent-vs-divergent.md) | No, halfway is worse than either | Commit to one, and sample rather than average |
| The goal has several owners who rank the results differently | [Shared vs contested values](shared-vs-contested-values.md) | Only as a deal between them | Settle whose weights count, in the open |

The moves clash, so tagging the wrong one does harm. Blending is the right move for a car buyer and the wrong move for a best man. Letting the decision maker pick works for the car buyer and fails for two towns that each want the bridge, since nobody there has the standing to pick. Each axis has a corner case that sits at its hard end and the easy end of the other two. A car buyer has trade-offs, shared values and answers that blend. A best man writing alone has one goal, nobody to argue with and answers that differ in kind. Two towns that each want the bridge have one goal each and contested values.

## Naming an axis

Each end needs a label that makes sense on its own. Picture it written alone at one end of a chart. "None" could mean anything, but "No skin in the game" can only mean one thing. "Easy" was worse, since every axis already has an easy end and a hard end. So the labels give the noun as well, like "Fat tails" or "Proxy measure", and the title can stay short.

Use the field's own term when there is one, so readers can look it up. "Chaotic" beats "short predictability horizon", and "Knightian uncertainty" beats "unknown odds". Then check the name doesn't sound like another axis. "Complete vs incomplete score" sounded too much like tractable vs intractable search, so it became [Direct vs proxy measure](direct-vs-proxy-measure.md). Check the words in other axes' descriptions too, not just their names. "Slack" was Perrow's word for a buffer in [Loose vs tight coupling](loose-vs-tight-coupling.md), so the time to decide became [Ample time vs time pressure](ample-time-vs-time-pressure.md). "Spread" already meant how far results scatter, so spreading your stake became [Diversifiable vs single bet](diversifiable-vs-single-bet.md).

Last, the name should describe the problem, not what you do about it. "Test vs watch" named two things you might do. [Interventional vs observational](interventional-vs-observational.md) names the kind of evidence the world lets you get.
