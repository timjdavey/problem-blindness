---
type: Guide
title: Reading the axes
description: How the axes are grouped, what the correlation labels mean and what changes at the hard end.
---
# Reading the axes

Each axis is a scale with two ends, and any problem sits somewhere along it. They fall into three groups. The first is about the world you act on. The second is about what you can know about it. The third is about the decision itself, what it needs and what it costs to get wrong. Each group splits into a few smaller sets of axes that ask about the same thing.

The Correlated with list under each axis names the other axes it tends to move with. On every axis the first end is the easy one and the second is the hard one. So "correlated" means a problem near the hard end of one axis tends to sit near the hard end of the other. A few entries say "opposite" when the hard end of one goes with the easy end of the other. "Tension" marks two hard ends that clash when they meet, and "independent" marks two axes that look linked but aren't.

Each entry also says where the link comes from. "By definition" means one axis is partly built into the other, so tagging both may count the same thing twice. "Bundled" means a framework puts both under one label. "Study" means there is evidence or a worked case showing them together. "Logic" means it follows from what the two axes mean.

Under each axis, the actions say what to do differently at each end, with the easy end first. Each one opens with a plain rule that holds for anyone. A list then says what that rule means when you build or deploy an AI model, since that is the main use of this project. The section [What changes at the hard end](#what-changes-at-the-hard-end) pulls out the pattern the actions share.

## The three groups

- [The world](index.md#the-world). These describe the system, whoever is looking at it.
  - [Randomness](index.md#randomness): what the spread of outcomes looks like.
  - [Change](index.md#change): how the result moves when the inputs or the times move.
  - [Response](index.md#response): whether the world reacts to what you do.
  - [Structure](index.md#structure): how the parts fit together.
- [The knower](index.md#the-knower). These describe what you can find out. The same problem can sit at different points for different people.
  - [Uncertainty](index.md#uncertainty): what kind of doubt you face.
  - [Evidence](index.md#evidence): how you can learn what is going on.
  - [Know-how](index.md#know-how): where the skill and the facts live.
- [The decision](index.md#the-decision). These describe what you are trying to achieve and what happens if you get it wrong.
  - [Goal](index.md#goal): what a good answer looks like and how you can tell.
  - [Options](index.md#options): what you can do and when.
  - [Stakes](index.md#stakes): what it costs to be wrong.
  - [People](index.md#people): who decides, who judges and who pays.

## What changes at the hard end

Read down the actions and the same move keeps turning up. Near the easy ends you can trust the test you ran before launch. A held-out test set predicts how the model will do in production, so you can automate fully, monitor lightly and plan the project like normal engineering. Spending months on live experiments or fallbacks here is waste.

As a problem moves towards the hard ends, the offline test stops being enough to decide on. What replaces it comes in a set order. First you pair the model with a checker, like tests, a rules engine or an expert, and let it act alone only where the checker can confirm the output. Next you stop trusting offline tests as the gate at all. You ship to small groups, run variants side by side and measure what happens downstream rather than how accurate the model is. At the far end you need a way to take the model out of the loop, such as people who can take over, a kill switch or a freeze on automated decisions when inputs stop looking like the training data. These four steps line up with the clear, complicated, complex and chaotic domains of [Cynefin](../frameworks/1999-cynefin.md).

A real problem sits near the hard end of several axes at once, and their actions can pull against each other. A drifting world says retrain often and ship fast, while a ruinous one says put a person at the door. When they clash, the action furthest along that order wins. A fallback and a cap on losses come before any experiment, and an experiment comes before trust in the offline test.

Both stories in the [README](../README.md) show someone running the easy end playbook on a hard end problem. The reverse is a mistake too, just a cheaper one. Building bandits and kill switches for a stable task you can check in seconds wastes months you could have spent shipping it.

## Grain and horizon

Where a problem sits on most axes depends on how closely you look and over what time. One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate. Weather is chaotic two weeks out, while climate is steady over decades. So before you place a problem on any axis, say what scale and what timescale you mean, or the same problem will get tagged two different ways.

Split a task into its separate decisions before you tag it. The cardiology story in the [README](../README.md) is one task with two problems inside it. Putting in a stent is a practised skill with fast, clear feedback. Deciding whether to put one in is a slow, statistical call where your gut misleads you. Tag the task as a whole and you average two different problems into one that doesn't exist.

Also ask whether you are deciding one case or setting a policy for many. In 1990 Donald Redelmeier and Amos Tversky gave doctors the same case in two forms. Seen as one patient, a student with fatigue got an extra $20 blood test 30% of the time. Seen as one of a group of patients just like them, the figure was 17% ([Individual vs group decisions](../frameworks/1990-individual-vs-group-decisions.md)). A single case feels special, so it gets the extra test. But a doctor who sees the same kind of patient every week is setting a policy whether they mean to or not, and should judge the choice that way.

## When is it a new axis?

Most ideas for a new axis turn out to be an old one in new words. So a new axis has to pass three tests.

The first is the corner test. Name a problem at the new axis's hard end that sits at the easy end of the axes closest to it. If you can't find one, the new axis is a copy of one of them.

The second is the action test. The hard end has to call for something the nearby axes don't already say. If it doesn't, the idea may still be real. But it belongs as a note on one of those axes.

The third is the combination test. No mix of two or three existing axes can land the same problems at the hard end and call for the same actions. An idea can pass the first two tests against each axis on its own and still fail this one.

Fixed vs moving goal looked like a gap until it met the third test. A couple planning a wedding for 100 people on 5 June for under £20k have a clear brief. Yet what they want shifts once they start seeing venues. That passes the corner test, since the brief is well structured and the world around it isn't drifting. But the brief left out wants the couple could only find by looking, which is the hard end of [Direct vs proxy measure](direct-vs-proxy-measure.md). They found them through a chain of choices where each shaped the next, which is the hard end of [Standalone vs sequential](standalone-vs-sequential.md). Those two axes already say what to do. Don't trust the brief to hold everything you want, and learn as you go. So moving goals went in as a note on those two axes.

## Naming an axis

Each end needs a label that makes sense on its own. Picture it written alone at one end of a chart. "None" could mean anything, but "No skin in the game" can only mean one thing. "Easy" was worse, since every axis already has an easy end and a hard end. So the labels give the noun as well, like "Fat tails" or "Proxy measure", and the title can stay short.

Use the field's own term when there is one, so readers can look it up. "Chaotic" beats "short predictability horizon", and "Knightian uncertainty" beats "unknown odds". Then check the name doesn't sound like another axis. "Complete vs incomplete score" sounded too much like tractable vs intractable search, so it became [Direct vs proxy measure](direct-vs-proxy-measure.md).

Last, the name should describe the problem, not what you do about it. "Test vs watch" named two things you might do. [Interventional vs observational](interventional-vs-observational.md) names the kind of evidence the world lets you get.
