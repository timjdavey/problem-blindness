---
type: Guide
title: Reading the axes
description: How the axes are grouped, how to read one and what to do when a problem sits at the hard end.
---

See [index](index.md) for full list.

## The five groups

There is no single "correct" way to collate or break the space of all problems into. Therefore we've chosen to use Stuart Russell and Peter Norvig method as a practical start. They sum up any task an AI agent faces as PEAS: its performance measure, environment, actuators and sensors ([Task environment properties](../frameworks/1995-task-environment-properties.md)). The groups follow them, with actions and information in place of actuators and sensors for everyday readability. The sub-groups are our own.

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
- [Agent](index.md#agent). What does the task ask of whoever solves it? The same problem sits at different points for different solvers, so this is where you check a solver fits the task.
  - [Know-how](index.md#know-how): where the skill and the facts live.
  - [Incentives](index.md#incentives): who has to answer for the call and who pays for a mistake.

## What's on an axis page

Every axis page has the same four parts.

- **The two ends.** We have tried to order these axes so that the "easy end" comes first (as it can be argued that a deterministic system is easier to deal with than a stochastic one), however these are obviously subjective. A few axes also name a middle when it is a case of its own e.g. [Self-righting vs tipping](self-righting-vs-tipping.md).
- **Actions.** What to do differently at each end. Each opens with a plain rule that holds for anyone.
- **Correlated with.** The other axes this one tends to move with, each with a tag in brackets.
- **Citations.** The frameworks the axis came from.

Correlated means a problem near the hard end of one axis tends to sit near the hard end of the other. Most entries are correlated, and their tag says how we know. The rest are tagged with how they break that pattern.

| Tag | Meaning |
|---|---|
| **logic** | Correlated, because it follows from what the two axes mean |
| **study** | Correlated, and there is evidence or a worked case showing them together |
| **bundled** | Correlated, because a framework puts both under one label |
| **by definition** | Correlated, because one axis is partly built into the other. Tagging both may count the same thing twice |
| **opposite** | The hard end of one goes with the easy end of the other |
| **tension** | The two hard ends clash when they meet |
| **independent** | They look linked but aren't |

## Before you tag a problem

Three checks stop the same problem getting tagged two different ways.

1. **Say the scale and timescale.** Where a problem sits on most axes depends on how closely you look and over what time. One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate.
2. **Split the task into its decisions.** The cardiology story in the [overview](../README.md) is two problems in one task. Putting in a stent is a practised skill with fast, clear feedback. Deciding whether to is a slow, statistical call where your gut misleads you. Tag the whole task and you average them into a problem that doesn't exist.
3. **Ask whether it's one case or a policy.** In 1990 Donald Redelmeier and Amos Tversky gave doctors the same case in two forms ([Individual vs group decisions](../frameworks/1990-individual-vs-group-decisions.md)). Seen as one patient, a student with fatigue got an extra $20 blood test 30% of the time. Seen as one of a group just like them, the figure was 17%. A doctor who sees that kind of patient every week is setting a policy whether they mean to or not, and should judge the choice that way.

## What changes at the hard end

Near the easy ends you can trust the test you ran before launch. Towards the hard ends that test stops being enough.

1. **Trust the offline test.** A held-out test set predicts how the model will do in production. Automate fully, monitor lightly and plan the project like normal engineering.
2. **Add a checker.** Pair the model with tests, a rules engine or an expert. Let it act alone only where the checker can confirm the output.
3. **Experiment live.** Stop using offline tests as the gate. Ship to small groups, run variants side by side and measure what happens downstream rather than how accurate the model is.
4. **Keep a way out.** Have people who can take over, a kill switch or a freeze on automated decisions when inputs stop looking like the training data.

A real problem sits near the hard end of several axes at once, and their actions can pull against each other. A drifting world says retrain often and ship fast, while a ruinous one says put a person at the door. **When actions clash, the step furthest down the list wins.**

Both stories in the [overview](../README.md) show someone running the easy end playbook on a hard end problem. The reverse is a mistake too, just a cheaper one. Building bandits and kill switches for a stable task you can check in seconds wastes months you could have spent shipping it.

## Telling look-alike axes apart

Three axes describe problems with no one right answer, and they used to blur together. They split on why there are many good answers, and each reason calls for a different move.

| Why there are many good answers | Axis | Can you blend two good answers? | What to do | Example |
|---|---|---|---|---|
| The goal has several parts that pull against each other | [Single objective vs trade-offs](single-objective-vs-trade-offs.md) | Yes, a blend sits on or near the trade-off | Lay out the trade-offs and let the owner set the weights | A car buyer weighing price against comfort |
| The good answers differ in kind | [Convergent vs divergent](convergent-vs-divergent.md) | No, halfway is worse than either | Commit to one, and sample rather than average | A best man writing his speech |
| The goal has several owners who rank the results differently | [Shared vs contested values](shared-vs-contested-values.md) | Only as a deal between them | Settle whose weights count, in the open | Two towns that each want the bridge |

The moves clash, so tagging the wrong one does harm. Blending is right for the car buyer and wrong for the best man. Letting the buyer pick works, but nobody has the standing to pick between the two towns. Each example sits at the hard end of its own axis and the easy end of the other two.

## Adding or renaming an axis

### Three tests for a new axis

Most ideas for a new axis turn out to be an old one in new words. A new axis has to pass three tests.

1. **Corner test.** Name a problem at the new axis's hard end that sits at the easy end of the axes closest to it. If you can't, the new axis is a copy of one of them.
2. **Action test.** The hard end has to call for something the nearby axes don't already say. If it doesn't, the idea may still be real. But it belongs as a note on one of those axes.
3. **Combination test.** No mix of two or three existing axes can land the same problems at the hard end and call for the same actions. An idea can pass the first two tests against each axis alone and still fail this one.

Fixed vs moving goal failed the third test. A couple planning a wedding for 100 people on 5 June for under £20k have a clear brief, yet what they want shifts once they see venues. That passes the corner test, since the brief is clear and the world isn't drifting. But the brief left out wants they could only find by looking, the hard end of [Direct vs proxy measure](direct-vs-proxy-measure.md). They found them through a chain of choices where each shaped the next, the hard end of [Standalone vs sequential](standalone-vs-sequential.md). Those two axes already say what to do, so moving goals became a note on them.

### Naming rules

- **Each end makes sense on its own.** Picture the label written alone at one end of a chart. "None" could mean anything, but "No skin in the game" can only mean one thing. "Easy" is worse, since every axis has an easy end. So labels carry the noun, like "Fat tails" or "Proxy measure", and the title can stay short.
- **Use the field's own term**, so readers can look it up. "Chaotic" beats "short predictability horizon", and "Knightian uncertainty" beats "unknown odds".
- **Don't sound like another axis**, in its name or in the words of its description. "Complete vs incomplete score" sounded too much like tractable vs intractable search, so it became [Direct vs proxy measure](direct-vs-proxy-measure.md). "Slack" was Perrow's word for a buffer in [Loose vs tight coupling](loose-vs-tight-coupling.md), so the time to decide became [Ample time vs time pressure](ample-time-vs-time-pressure.md).
- **Name the problem, not the response.** "Test vs watch" named two things you might do. [Interventional vs observational](interventional-vs-observational.md) names the kind of evidence the world lets you get.
