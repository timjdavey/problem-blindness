---
type: Overview
title: Problem Blindness
description: A shared vocabulary for the shape of a problem, built from a century of frameworks, so people and AI models can tell what kind of expert a task needs.
---
<div align="center">

# Problem Blindness

**A shared vocabulary for the shape of problems, so people and AI models
can tell what kind of expert a task needs.**

[![Open Knowledge Format](https://img.shields.io/badge/format-OKF-lightgrey?style=flat-square)](https://okf.md) [![Axes](https://img.shields.io/badge/axes-47-blue?style=flat-square)](axes/index.md) [![Frameworks](https://img.shields.io/badge/frameworks-97-blue?style=flat-square)](frameworks/index.md) [![Licence](https://img.shields.io/badge/licence-CC%20BY%204.0-lightgrey?style=flat-square)](LICENCE)

</div>

<br>

## What is this?

[We've seen](MOTIVATION.md) experts and AI models tend to get good at one kind of problem then bring those tools to all problems they encounter. There's no one right method for every problem ([no free lunch](frameworks/1997-no-free-lunch.md)), so the first job is for us to break down what ways problems can differ. Then we can start to map what works for what problems. Economists, planners, psychologists and computer scientists have all come up with various frameworks for spotting differences based on their industry. But each in their own words and with no map.

This repo is an attempt to tease out the traits which underpin those frameworks. So we can build a joint consistent vocabulary.

## A quick taste

Treating a heart attack is two problems in one task.

| Axis | Putting in the stent | Deciding whether to |
|---|---|---|
| [Immediate vs delayed feedback](axes/immediate-vs-delayed-feedback.md) | **Immediate.** You see the artery open on the screen | **Delayed.** Whether it helped shows up only in death rates across many patients |
| [Verifiable vs unverifiable](axes/verifiable-vs-unverifiable.md) | **Verifiable.** The scan shows whether blood flows | **Unverifiable.** You can't check whether this patient would have lived without it |
| [Explicit vs tacit know-how](axes/explicit-vs-tacit-know-how.md) | **Tacit.** The skill lives in trained hands | **Explicit.** Trial data and risk scores can be written down |

We've seen cardiologists trained to trust their gut on the procedure brought the same gut to the decision, and their patients did worse for it. The [motivation](MOTIVATION.md#problem-blindness) tells the full story.

## Why the vocabulary needs pinning down

Frameworks are slippy it's easy for their meaning to drift. This is particularly true when theres many axes bundled into a single concept. When a problem is defined by a bunch of "OR" things it _could_ be invites people to add to that definition over time. Because those observations and axis need a home, so it's natural people add them to concepts which _feel_ the same.

| Term | First meant | Later stretched to | Axes it feeds |
|---|---|---|---|
| Wicked | Rittel and Webber, 1973: a [planning problem](frameworks/1973-tame-vs-wicked-problems.md) where people can't agree what the problem is | Hogarth, 2001: a [learning environment](frameworks/2001-kind-vs-wicked-learning-environments.md) where feedback is missing or misleading | [Shared vs contested values](axes/shared-vs-contested-values.md) for the first, [Immediate vs delayed feedback](axes/immediate-vs-delayed-feedback.md) for the second |
| Black swan | Taleb, 2007: an [event](frameworks/2007-mediocristan-vs-extremistan.md) from a fat-tailed world that past data gives no hint of | Popular writing: any nasty surprise, even a widely predicted one. Taleb called Covid a white swan | [Thin vs fat tails](axes/thin-vs-fat-tails.md) and [Risk vs Knightian uncertainty](axes/risk-vs-knightian-uncertainty.md) |
| Goodhart's law | Goodhart, 1975: a [pattern in the data](frameworks/1975-goodharts-law.md) that collapses once policy leans on it | Strathern, 1997: people game any target you set them | [Inert vs reflexive](axes/inert-vs-reflexive.md) for the first, [Direct vs proxy measure](axes/direct-vs-proxy-measure.md) for the second |
| Infinite game | Carse, 1986: a [game](frameworks/1986-finite-and-infinite-games.md) played to keep play going, not to win | Sinek, 2019: thinking long term in business | [Curable vs chronic](axes/curable-vs-chronic.md) |

## The five groups

We've grouped the axis for sanity using Russell and Norvig's [task environment properties](frameworks/1995-task-environment-properties.md). These aren't strict boundaries but their categories is a really great start.

| Group | The question it asks | Sets |
|---|---|---|
| Environment | How does the system behave, whoever is looking at it? | [Randomness](axes/index.md#randomness), [Change](axes/index.md#change), [Stimulus](axes/index.md#stimulus), [Reactivity](axes/index.md#reactivity), [Structure](axes/index.md#structure) |
| Information | What can you find out, and how fast? | [Uncertainty](axes/index.md#uncertainty), [Evidence](axes/index.md#evidence) |
| Actions | What moves do you have? | [Options](axes/index.md#options), [Control](axes/index.md#control) |
| Performance | What counts as good, and what do you stand to win or lose? | [Goal](axes/index.md#goal), [Stakes](axes/index.md#stakes) |
| Agent | What does the task ask of whoever solves it? | [Know-how](axes/index.md#know-how), [Incentives](axes/index.md#incentives) |

## How to reference axes

Link to the axis page, like [`axes/thin-vs-fat-tails.md`](axes/thin-vs-fat-tails.md). Names still change as we find better words, and a renamed page moves to its new path. It lists its old names under `aliases` in its front matter, so a search for an old name still finds it.

To tag a task, write the end labels in lower case with hyphens. No two ends share a label, so `fat-tails` can only mean one end of one axis. Here is the heart attack from the quick taste.

```text
Putting in the stent    immediate-feedback, verifiable, tacit-know-how
Deciding whether to     delayed-feedback, unverifiable, explicit-know-how
```

## What's in the repo

```text
README.md                    this page
MOTIVATION.md                why the project exists, we call it "problem blindness"
CONTRIBUTING.md              how to add, name and rename pages
index.md                     the Open Knowledge Format index of the whole project
log.md                       big changes, newest first
LICENCE                      CC BY 4.0, the terms for reusing these pages
axes/
├── README.md                how to read an axis page, what the tags mean and how to tag a task
├── index.md                 every axis by group, with both ends in one line
└── thin-vs-fat-tails.md     one file per axis, 47 in all
frameworks/
├── README.md                what the frameworks share and what's on a framework page
├── index.md                 every framework by date, oldest first
└── 1921-risk-vs-uncertainty.md   one file per framework, 97 in all
```

## Contributing

This will never be finished. If you spot a missing framework, a wrong link or a better example, please open a pull request. [CONTRIBUTING.md](CONTRIBUTING.md) covers adding an axis or framework, the tests a new axis must pass, naming, how to write and cite actions, which pages to update together and how to rename a page without breaking links.

## Future projects

In 2025 [METR](https://arxiv.org/abs/2503.14499) scored its tasks for "messiness". They found each point cut AI agents' mean success by about 8.1%. That is a fantastic start at using these axis to quantify performance.

We tried to benchmark out axis on the full set on METR's 23 public tasks. We found an suspiciously similar result of 8.5% per point against their 8.1%. However, this dataset is far too small to draw any meaningful conclusions beyond this feels like a meaningful avenue to continue. The aim is to roll this out on a larger set of benchmarks to conduct a more robust meta study.

## Licence

The writing in this repo is under [CC BY 4.0](LICENCE). You can copy, adapt and build on it for any purpose, including commercial work and training models, as long as you credit [Problem Blindness by Tim Davey](https://github.com/timjdavey/problem-blindness). You don't need to credit anyone just to tag a task with the end labels. Quotes and the works we link to keep their owners' terms.
