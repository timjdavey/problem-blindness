---
type: Overview
title: Problem Blindness
description: A shared vocabulary for the shape of a problem, built from a century of frameworks, so people and AI models can tell what kind of expert a task needs.
---
<div align="center">

# Problem Blindness

**A shared vocabulary for the shape of a problem, so people and AI models
can tell what kind of expert a task needs before they hand it over.**

[![47 axes](https://img.shields.io/badge/axes-47-8A2BE2?style=flat-square)](axes/index.md)
[![95 frameworks](https://img.shields.io/badge/frameworks-95-008080?style=flat-square)](frameworks/index.md)
[![Motivation](https://img.shields.io/badge/read-the_motivation-FBFAF7?style=flat-square&labelColor=333)](MOTIVATION.md)
[![Open Knowledge Format](https://img.shields.io/badge/format-OKF-lightgrey?style=flat-square)](https://okf.md)

</div>

<br>

## Start here

<table>
  <tr>
    <td width="33%" valign="top">
      <h3><a href="MOTIVATION.md">Why this exists</a></h3>
      <p>Why the best cardiologists did more harm than the ones they left behind, and why experts and AI models bring the same hammer to every problem.</p>
      <p>📖 <a href="MOTIVATION.md">Read the motivation</a></p>
    </td>
    <td width="33%" valign="top">
      <h3><a href="axes/README.md">The axes</a></h3>
      <p>47 traits that set one problem apart from another, each with what to do at either end and the sources behind it.</p>
      <p>🧭 <a href="axes/README.md">Read the guide</a> · <a href="axes/index.md">See the list</a></p>
    </td>
    <td width="33%" valign="top">
      <h3><a href="frameworks/README.md">The frameworks</a></h3>
      <p>95 attempts to sort problems by what they are like, from Knight's risk and uncertainty in 1921 to incoherence in 2024.</p>
      <p>📚 <a href="frameworks/README.md">Read the guide</a> · <a href="frameworks/index.md">See the list</a></p>
    </td>
  </tr>
</table>

## What is this?

Experts and AI models get good at one kind of problem, then bring the same tools to problems they don't suit. No single method wins on every problem ([no free lunch](frameworks/1997-no-free-lunch.md)), so the first job is to see what kind of problem you have. Economists, planners, psychologists and computer scientists have each named the differences, but in their own words and with no map between them.

This repo pulls out the traits under those frameworks as **axes**. The easy end always comes first, so in [Immediate vs delayed feedback](axes/immediate-vs-delayed-feedback.md) delayed is the harder case. Each axis page says what to do at either end and cites a source for every move.

## A quick taste

Treating a heart attack is two problems in one task, and they land at opposite ends.

| Axis | Putting in the stent | Deciding whether to |
|---|---|---|
| [Immediate vs delayed feedback](axes/immediate-vs-delayed-feedback.md) | **Immediate.** You see the artery open on the screen | **Delayed.** Whether it helped shows up only in death rates across many patients |
| [Verifiable vs unverifiable](axes/verifiable-vs-unverifiable.md) | **Verifiable.** The scan shows whether blood flows | **Unverifiable.** You can't check whether this patient would have lived without it |
| [Explicit vs tacit know-how](axes/explicit-vs-tacit-know-how.md) | **Tacit.** The skill lives in trained hands | **Explicit.** Trial data and risk scores can be written down |

Each end tells you what to do. This is the explicit end, [as it appears](axes/explicit-vs-tacit-know-how.md#actions) on the axis page:

> **Explicit know-how**: Write it down and hand it over.
> - Put the rules in a manual, a checklist or a prompt. Work with clear methods and few surprises runs well on rules, so a new hire or a model can simply be told them. [1]
> - Follow the written rule rather than gut feel. On a task with a clear rule, gut feel only adds noise to what a formula would get right every time. [3]

Cardiologists trained to trust their gut on the procedure brought the same gut to the decision, and their patients did worse for it. The [motivation](MOTIVATION.md#problem-blindness) tells the full story.

## Why the words need pinning down

A word gets a precise meaning in one field, then another field borrows it and stretches it. People can read around the clash, but a model will treat the two meanings as one. The axes give each meaning its own place.

| Term | First meant | Later stretched to | Axes it feeds |
|---|---|---|---|
| Wicked | Rittel and Webber, 1973: a [planning problem](frameworks/1973-tame-vs-wicked-problems.md) where people can't agree what the problem is | Hogarth, 2001: a [learning environment](frameworks/2001-kind-vs-wicked-learning-environments.md) where feedback is missing or misleading | [Shared vs contested values](axes/shared-vs-contested-values.md) for the first, [Immediate vs delayed feedback](axes/immediate-vs-delayed-feedback.md) for the second |
| Non-ergodic | Peters and Gell-Mann, 2016: a [bet](frameworks/2016-ergodicity.md) that pays on average yet leaves the typical player poorer | Popular writing: any risk of ruin | [Additive vs multiplicative returns](axes/additive-vs-multiplicative-returns.md) and [Survivable vs ruinous](axes/survivable-vs-ruinous.md), kept apart |
| Infinite game | Carse, 1986: a [game](frameworks/1986-finite-and-infinite-games.md) played to keep play going, not to win | Sinek, 2019: thinking long term in business | [Curable vs chronic](axes/curable-vs-chronic.md) |

## The five groups

The groups follow Russell and Norvig's [task environment properties](frameworks/1995-task-environment-properties.md). An agent is anything that senses and acts, whether a person, a firm or a program.

| Group | The question it asks | Sets |
|---|---|---|
| Environment | How does the system behave, whoever is looking at it? | [Randomness](axes/index.md#randomness), [Change](axes/index.md#change), [Stimulus](axes/index.md#stimulus), [Reactivity](axes/index.md#reactivity), [Structure](axes/index.md#structure) |
| Information | What can you find out, and how fast? | [Uncertainty](axes/index.md#uncertainty), [Evidence](axes/index.md#evidence) |
| Actions | What moves do you have? | [Options](axes/index.md#options), [Control](axes/index.md#control) |
| Performance | What counts as good, and what does a miss cost? | [Goal](axes/index.md#goal), [Stakes](axes/index.md#stakes) |
| Agent | What does the task ask of whoever solves it? | [Know-how](axes/index.md#know-how), [Incentives](axes/index.md#incentives) |

## How to tag a task

1. **Split the task into its decisions.** Tag the stent and the choice to use one together and you average them into a problem that doesn't exist.
2. **Say the scale and timescale.** One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate.
3. **Ask whether it's one case or a policy.** A doctor who sees the same kind of patient every week is setting a policy, and should judge the choice that way.
4. **Place each decision on every axis**, then read the actions at the ends it lands on. When actions clash, follow [What changes at the hard end](axes/README.md#what-changes-at-the-hard-end).

[Before you tag a problem](axes/README.md#before-you-tag-a-problem) gives the full checks. The whole repo is plain Markdown in the [Open Knowledge Format](https://okf.md), so an AI agent can load it as a skill or a reference with no special tools.

## Does it predict anything?

In 2025 [METR](https://arxiv.org/abs/2503.14499) scored its tasks for "messiness", meaning how far each sits from a clean test. After allowing for task length, each point cut AI agents' mean success by about 8.1%. That is one crude axis, so we tried the full set on METR's public tasks.

| Data | What we found |
|---|---|
| 23 tasks from 11 families with full text | Our tagger matched METR's messiness result, at 8.5% per point against their 8.1% |
| The rest, with a one or two sentence summary | Almost nothing, since a sentence is too little to tag from |

[Verifiable vs unverifiable](axes/verifiable-vs-unverifiable.md) came out strongest, as predicted, but didn't survive correction for testing 25 axes at once.

> [!NOTE]
> **Hold private task text? Let's run the real test.**
> METR keeps most task text private so models aren't trained on it. We'd love to work with METR or any lab in the same position. The tagging can run on your side.

## What's in the repo

```text
README.md                    this page
MOTIVATION.md                why the project exists, told through the cardiologists and the typhoid doctor
index.md                     the Open Knowledge Format index of the whole project
log.md                       big changes, newest first
axes/
├── README.md                how to read an axis page, what the tags mean and how to tag a task
├── index.md                 every axis by group, with both ends in one line
└── thin-vs-fat-tails.md     one file per axis, 47 in all
frameworks/
├── README.md                what the frameworks share and how they feed the axes
├── index.md                 every framework by date, oldest first
└── 1921-risk-vs-uncertainty.md   one file per framework, 95 in all
```

## Contributing

This will never be finished. If you spot a missing framework, a wrong link or a better example, please open a pull request. Every file starts with YAML front matter that needs a `type`.

| Adding | File | Front matter | Then |
|---|---|---|---|
| A framework | `frameworks/1973-tame-vs-wicked-problems.md` | `type: Framework`, `title`, `description`, `date`, `creators`, `sources` | Add it to the [frameworks index](frameworks/index.md) |
| An axis | `axes/thin-vs-fat-tails.md` | `type: Axis`, `title`, `description` (each end in one line), `group`, `subgroup`, `easy_end`, `hard_end`, `sources` | Add it to the [axes index](axes/index.md) under its set, and link the axes it moves with |

Each end label must make sense on its own, so write "Fat tails" rather than "Fat" ([Naming rules](axes/README.md#naming-rules)). Each action must cite a source, so an action nothing backs doesn't go in.

Most new axes turn out to be an old one in new words, so a new axis has to pass [three tests](axes/README.md#three-tests-for-a-new-axis).

1. **Corner test.** Name a problem at its hard end that sits at the easy end of the axes closest to it.
2. **Action test.** Its hard end calls for actions those axes don't already list.
3. **Combination test.** No mix of two or three existing axes lands the same problems at the hard end and calls for the same actions.

An idea that fails the second or third test goes in as a note on the axis that covers it. Record big changes in [log.md](log.md).
