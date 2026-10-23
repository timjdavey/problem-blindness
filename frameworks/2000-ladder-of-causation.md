---
type: Framework
title: Ladder of causation
description: >-
  Questions about cause sit on three rungs: seeing, doing and imagining. Data from a lower rung can't answer a question from a higher one on its own. You need a test, or a stated model of what causes what.
date: 2000
cited_date: 2018
creators:
  - Judea Pearl
  - Dana Mackenzie
sources:
  - resource: https://doi.org/10.1017/CBO9780511803161
    title: Causality
  - resource: http://bayes.cs.ucla.edu/WHY/
    title: "The book of why: the new science of cause and effect"
  - resource: https://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf
    title: The seven tools of causal inference, with reflections on machine learning (free PDF)
  - resource: https://en.wikipedia.org/wiki/The_Book_of_Why
    title: The Book of Why (Wikipedia)
---
# Ladder of causation

**Questions about cause sit on three rungs: seeing, doing and imagining. Data from a lower rung can't answer a question from a higher one on its own.**

2000 (2018) · Judea Pearl and Dana Mackenzie · [Original book](https://doi.org/10.1017/CBO9780511803161) · Feeds 2 axes

## The idea

For most of the 20th century statistics taught that correlation is not causation, and then said little more about cause at all. Judea Pearl, a computer scientist at UCLA, spent the 1990s building a maths of cause and effect. He set it out in his book Causality in 2000, with a second edition in 2009, and won the Turing Award for this work in 2011. In 2018 he and the science writer Dana Mackenzie wrote The Book of Why for a general reader. There they gave the idea a simple picture, which is a ladder with three rungs.

The bottom rung is seeing. You notice that two things go together, such as a falling barometer and rain. The middle rung is doing. You ask what happens if you step in and change something, like taking a pill. The top rung is imagining. You ask what would have happened if things had gone differently, like whether a patient would have lived without the pill. Pearl calls these association, intervention and counterfactuals. The trait this sorts on is which rung your question sits on. His main claim is that data from a lower rung can't answer a higher question by itself. To climb you need either an experiment or a clear model of what causes what.

## What goes wrong

The mistake is reading causes straight off patterns. Most data we have is bottom rung, because it records what people chose to do. Those who chose differently also differ in other ways, so the pattern mixes the effect of the choice with the effect of who chose it.

## What to do instead

The better response is to name the rung of your question first. If it is a doing question, run a fair test where you can. Where you can't, write down what you think causes what and see which links the answer rests on.

## Examples

### The barometer

A falling barometer predicts a storm very well. Yet nobody thinks pushing the needle down with a finger will bring rain. We all know that falling air pressure moves both the needle and the weather. In messier fields we don't know, and people push the needle all the time.

### Hormone therapy

In 1991 a large study of nearly 50,000 American nurses found that women taking oestrogen after the menopause had about half the rate of major heart disease. Doctors began to prescribe it partly to protect the heart. That was a doing conclusion drawn from seeing data. The women who chose hormones tended to be healthier and better off to begin with. In 2002 the Women's Health Initiative, a trial that randomly gave 16,608 women either hormones or a dummy pill, was stopped early. Women on the hormones had 29% more heart disease, not less.

### The firing squad

Pearl uses this to show the top rung. Two soldiers shoot a prisoner on the captain's order and both bullets kill him. Would he have died if soldier A had not fired? Yes, because B fired too. Watching firing squads can't tell you that. You need a model of how the event works.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Interventional vs observational](../axes/interventional-vs-observational.md) | Information › Evidence | Seeing data can't answer a doing question without a fair test or a model of causes |
| [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) | Information › Evidence | Where you can't test, write down what causes what and check which links the answer rests on |

## Further reading

- [Causality](https://doi.org/10.1017/CBO9780511803161), Judea Pearl, *Cambridge University Press*, 2009. The second edition of the original book, and the full maths.
- [The book of why](http://bayes.cs.ucla.edu/WHY/), Judea Pearl and Dana Mackenzie, *Basic Books*, 2018. The book's own site, with author bios and background reading.
- [The seven tools of causal inference, with reflections on machine learning](https://ftp.cs.ucla.edu/pub/stat_ser/r481.pdf), Judea Pearl, *Communications of the ACM*, 2019. A free six page summary of the three level hierarchy and what each level can answer.
- [The Book of Why](https://en.wikipedia.org/wiki/The_Book_of_Why) on Wikipedia.
