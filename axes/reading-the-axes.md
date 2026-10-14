---
type: Guide
title: Reading the axes
description: How the axes are grouped, what the correlation labels mean and what changes at the hard end.
---
# Reading the axes

Each axis is a scale with two ends, and any problem sits somewhere along it. They fall into three groups. The first is about the world you act on. The second is about what you can know about it. The third is about the decision itself, what it needs and what it costs to get wrong.

The Correlated with list under each axis names the other axes it tends to move with. On every axis the first end is the easy one and the second is the hard one. So "correlated" means a problem near the hard end of one axis tends to sit near the hard end of the other. A few entries say "opposite" when the hard end of one goes with the easy end of the other. "Tension" marks two hard ends that clash when they meet, and "independent" marks two axes that look linked but aren't.

Each entry also says where the link comes from. "By definition" means one axis is partly built into the other, so tagging both may count the same thing twice. "Bundled" means a framework puts both under one label. "Study" means there is evidence or a worked case showing them together. "Logic" means it follows from what the two axes mean.

Under each axis, the actions say what to do differently at each end, with the easy end first. Each one opens with a plain rule that holds for anyone. A list then says what that rule means when you build or deploy an AI model, since that is the main use of this project. The section [What changes at the hard end](#what-changes-at-the-hard-end) pulls out the pattern the actions share.

## The three groups

- [The world](index.md#the-world). These describe the system, whoever is looking at it.
- [The knower](index.md#the-knower). These describe what you can find out. The same problem can sit at different points for different people.
- [The decision](index.md#the-decision). These describe what you are trying to achieve and what happens if you get it wrong.

## What changes at the hard end

Read down the actions and the same move keeps turning up. Near the easy ends you can trust the test you ran before launch. A held-out test set predicts how the model will do in production, so you can automate fully, monitor lightly and plan the project like normal engineering. Spending months on live experiments or fallbacks here is waste.

As a problem moves towards the hard ends, the offline test stops being enough to decide on. What replaces it comes in a set order. First you pair the model with a checker, like tests, a rules engine or an expert, and let it act alone only where the checker can confirm the output. Next you stop trusting offline tests as the gate at all. You ship to small groups, run variants side by side and measure what happens downstream rather than how accurate the model is. At the far end you need a way to take the model out of the loop, such as people who can take over, a kill switch or a freeze on automated decisions when inputs stop looking like the training data. These four steps line up with the clear, complicated, complex and chaotic domains of [Cynefin](../frameworks/1999-cynefin.md).

A real problem sits near the hard end of several axes at once, and their actions can pull against each other. A drifting world says retrain often and ship fast, while a ruinous one says put a person at the door. When they clash, the action furthest along that order wins. A fallback and a cap on losses come before any experiment, and an experiment comes before trust in the offline test.

Both stories in the [README](../README.md) show someone running the easy end playbook on a hard end problem. The reverse is a mistake too, just a cheaper one. Building bandits and kill switches for a stable task you can check in seconds wastes months you could have spent shipping it.

## Grain and horizon

Where a problem sits on most axes depends on how closely you look and over what time. One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate. Weather is chaotic two weeks out, while climate is steady over decades. So before you place a problem on any axis, say what scale and what timescale you mean, or the same problem will get tagged two different ways.

Split a task into its separate decisions before you tag it. The cardiology story in the [README](../README.md) is one task with two problems inside it. Putting in a stent is a practised skill with fast, clear feedback. Deciding whether to put one in is a slow, statistical call where your gut misleads you. Tag the task as a whole and you average two different problems into one that doesn't exist.

Also ask whether you are deciding one case or setting a policy for many. In 1990 Donald Redelmeier and Amos Tversky gave doctors the same case in two forms. Seen as one patient, a student with fatigue got an extra $20 blood test 30% of the time. Seen as one of a group of patients just like them, the figure was 17% ([Individual vs group decisions](../frameworks/1990-individual-vs-group-decisions.md)). A single case feels special, so it gets the extra test. But a doctor who sees the same kind of patient every week is setting a policy whether they mean to or not, and should judge the choice that way.
