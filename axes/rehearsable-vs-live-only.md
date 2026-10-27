---
type: Axis
title: Rehearsable vs live only
description: "Rehearsable: you can try the task on a copy faithful enough that a dry run tells you how you'll do for real (e.g. a pilot in a flight simulator). Live only: no copy behaves like the real thing, so the first real go is the first go (e.g. a new dish on a restaurant menu)."
group: information
subgroup: evidence
easy_end: Rehearsable
hard_end: Live only
sources:
  - resource: /frameworks/1933-multi-armed-bandit.md
    title: Multi-armed bandit
  - resource: /frameworks/1957-open-vs-closed-skills.md
    title: Open vs closed skills
  - resource: /frameworks/2001-kind-vs-wicked-learning-environments.md
    title: Kind vs wicked learning environments
  - resource: /frameworks/2009-conditions-for-intuitive-expertise.md
    title: Conditions for intuitive expertise
  - resource: /frameworks/2015-one-way-vs-two-way-doors.md
    title: One-way vs two-way doors
  - resource: https://doi.org/10.1287/orsc.2.1.1
    title: Learning from samples of one or fewer (March, 1991)
  - resource: https://doi.org/10.1207/s15327876mp0402_1
    title: "Flight simulator training effectiveness: a meta-analysis (Hays, 1992)"
  - resource: https://doi.org/10.1097/00000658-200210000-00008
    title: "Virtual reality training improves operating room performance: results of a randomized, double-blinded study (Seymour, 2002)"
  - resource: https://warontherocks.com/2015/11/millennium-challenge-the-real-story-of-a-corrupted-military-exercise-and-its-legacy/
    title: "Millennium Challenge: the real story of a corrupted military exercise and its legacy (Zenko, 2015)"
  - resource: https://www.collectspace.com/news/news-092016b-obituary-jack-garman-apollo11.html
    title: Jack Garman, NASA engineer who 'saved' Apollo 11 from alarms, dies at 72 (Pearlman, 2016)
  - resource: https://sre.google/workbook/canarying-releases/
    title: Canarying releases (Google SRE workbook, 2018)
---
# Rehearsable vs live only

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Can you try the task on a copy that behaves like the real thing, or does the first real go have to be the first go? A pilot can fly a simulator for hours before taking a plane up, and a student can sit past papers. A restaurant can cook and taste a new dish, but only real diners choosing from the real menu say whether it sells. A code change can pass every test in staging and still fail under real traffic, because no test environment matches production. Robin Hogarth, Tomás Lejarraga and Emre Soyer split learning into the setting where you learn and the setting where you use what you learnt ([Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)). A rehearsal is a learning setting built on purpose, and this axis asks whether one can be built that matches.

A copy fails when the thing that decides the outcome isn't in it. A simulator can hold the physics of flight, since that holds still and is known. It can't hold a crowd, a market or an enemy, which behave differently once the stakes are real. Nor can it hold a system that is one of a kind and too big to copy, like an economy or this patient's body. So live only problems bunch up wherever other people's reactions decide the result.

This axis is about trying before you act. [Reversible vs irreversible](reversible-vs-irreversible.md) is about undoing after, [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) about checking an answer by looking at it, and [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) about how soon the real world grades you.

## Actions

**Rehearsable**: Build the copy and practise on it before you go live.
- Practise on the copy until the routine is automatic, and let the live run wait on it. In a randomised trial, surgeons trained on a virtual reality simulator made fewer errors in real gallbladder operations. A meta-analysis of flight training studies found pilots trained in a simulator as well as the aircraft did better than those trained in the aircraft alone. [7, 8]
- Rehearse the rare and the dangerous, which only a copy lets you do cheaply. In a simulation before Apollo 11, the trainers threw a computer alarm at Mission Control, and the guidance officer called an abort. Afterwards Gene Kranz had every alarm listed with the right response. When a 1202 alarm came up during the real landing, the list said go. [9]
- Trust the rehearsal only where the copy is regular and gives quick, clear feedback. Kahneman and Klein found that is when practice turns into skill. [4]
- Practise the way the real task will run, still or moving, from one start or from many. Each kind of skill needs its own kind of practice. [2]
- Check the copy against live results and fix it where they part. A rehearsal only teaches you where it matches the real thing. [3]

**Live only**: Go small and for real, and treat the first go as the lesson.
- Try it on a small slice of the real thing, judge by what happens there, then widen. Google rolls a change out to a few percent of real traffic as a canary and compares it with the rest, because no test environment matches production. Thompson's 1933 proposal did the same with patients: give each new one a treatment at random, weighted towards whichever looks better so far. [1, 11]
- Watch the first run closely and keep a way back. A canary that fails is rolled back before the change reaches everyone else. Coca-Cola kept its old formula when it launched New Coke, so a one way door became a two way one. [5, 11]
- Don't take success in the copy as readiness. When the setting you practised in differs from the one you act in, experience teaches the wrong lesson. Ask what the copy left out, and expect the live run to fail there. [3]
- Learn from near misses and from other people's live runs. March, Sproull and Tamuz studied how organisations learn from events that happen once or never, and found them drawing on the near misses around each case and on what might have happened as well as what did. [6]
- If you do build a rehearsal, don't rig it. In Millennium Challenge 2002 the opposing force sank 19 ships in the first days, so the exercise refloated them, forbade the tactics that had worked and ran on to a scripted end. [10]

## Correlated with

- [Reversible vs irreversible](reversible-vs-irreversible.md) (independent). Rehearsing is trying before you act, and reversing is undoing after. Surgery can't be undone, yet a simulator lets you practise it. A new dish can be dropped from the menu, yet nothing but real diners tells you if it sells.
- [Interventional vs observational](interventional-vs-observational.md) (independent). A fair test sets the cause for real, and a rehearsal tries it on a copy. A canary deploy is a fair test with no faithful copy, and a weather forecaster can rehearse against past weather without ever setting the cause.
- [Inert vs reflexive](inert-vs-reflexive.md) (logic). A crowd that reacts to what you put out can't be copied cheaply, so reflexive problems are mostly live only. A stress test of a bank run is a rehearsal, just an unfaithful one.
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (independent). A transparent system is easier to copy, but a traceable codebase still fails in ways only real traffic shows. A trained network, which nobody can trace, can be tried on held-out data before it goes live.
- [Durable vs perishable lessons](durable-vs-perishable-lessons.md) (logic). Both open a gap between where you learn and where you act. Drift opens it over time, as the world moves on from your data. This axis opens it at once, when the copy never matched. A pilot trained only in calm weather learnt in a different world from the one they fly in, however little the weather has drifted.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (independent). A rehearsal grades you before you go, and feedback grades you after. A canary deploy grades you in minutes but had no faithful rehearsal. A pension plan can be backtested against a century of markets and still takes decades to grade.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (independent). Verifying checks an answer by looking at it, and rehearsing runs it on a copy. A deploy passes every test and still breaks under real load. A chess move can't be checked by inspection, but you can play it out against an engine.
- [Turn-based vs real-time](turn-based-vs-real-time.md) (independent). Poulton's open and closed skills each need their own kind of practice, which assumes a place to practise ([Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)). That axis asks whether the world moves while you act, and this one whether a copy of it can be built. A tennis serve moves and can be practised for years. A house price sits still and can't be rehearsed.
- [Foreseeable vs unforeseeable outcomes](foreseeable-vs-unforeseeable-outcomes.md) (logic). A war game can only hold the outcomes someone built into it, so unforeseeable outcomes are one reason no copy is faithful. But a deploy holds few surprises in what can happen and still has no faithful copy.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (independent). Scarce data is why people build simulators, since a nuclear operator can't wait for accidents. And a team with thousands of past deploys still has no copy of the next one.

## Citations

[1] [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md)

[2] [Open vs closed skills](../frameworks/1957-open-vs-closed-skills.md)

[3] [Kind vs wicked learning environments](../frameworks/2001-kind-vs-wicked-learning-environments.md)

[4] [Conditions for intuitive expertise](../frameworks/2009-conditions-for-intuitive-expertise.md)

[5] [One-way vs two-way doors](../frameworks/2015-one-way-vs-two-way-doors.md)

[6] [Learning from samples of one or fewer (March, 1991)](https://doi.org/10.1287/orsc.2.1.1)

[7] [Flight simulator training effectiveness: a meta-analysis (Hays, 1992)](https://doi.org/10.1207/s15327876mp0402_1)

[8] [Virtual reality training improves operating room performance: results of a randomized, double-blinded study (Seymour, 2002)](https://doi.org/10.1097/00000658-200210000-00008)

[9] [Jack Garman, NASA engineer who 'saved' Apollo 11 from alarms, dies at 72 (Pearlman, 2016)](https://www.collectspace.com/news/news-092016b-obituary-jack-garman-apollo11.html)

[10] [Millennium Challenge: the real story of a corrupted military exercise and its legacy (Zenko, 2015)](https://warontherocks.com/2015/11/millennium-challenge-the-real-story-of-a-corrupted-military-exercise-and-its-legacy/)

[11] [Canarying releases (Google SRE workbook, 2018)](https://sre.google/workbook/canarying-releases/)
