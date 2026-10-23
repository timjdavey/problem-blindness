---
type: Framework
title: Incoherence
description: >-
  Systems which give wildly different output distributions each run.
date: 2024
creators:
  - Tim J. Davey
sources:
  - resource: https://doi.org/10.3390/e26080683
    title: "Incoherence: a generalized measure of complexity to quantify ensemble divergence in multi-trial experiments and simulations"
  - resource: https://timjdavey.com/incoherence/
    title: Complexity, and how to measure it (primer)
  - resource: https://github.com/timjdavey/incoherence
    title: incoherence (code on GitHub)
  - resource: https://arxiv.org/abs/1911.02969
    title: "BERTs of a feather do not generalize together: large variability in generalization across models with similar test set performance"
  - resource: https://archive.org/details/DTIC_AD0010203
    title: The "average man"?
---
# Incoherence

**Systems which give wildly different output distributions each run.**

2024 · Tim J. Davey · [Original paper](https://doi.org/10.3390/e26080683) · Feeds 2 axes

## The idea

Most of the time we sum up a system by its average and its spread. Run a simulation five times, take the mean, add an error bar and move on. In 2024 Tim Davey argued in the journal Entropy that this hides a question worth asking first. Can the average stand in for a typical run at all?

Davey's measure works on runs, not on single outcomes. A run is one whole go of a system, like a full simulation or a thousand rolls of a die. Every thousand rolls give the same spread, so by this measure a die is coherent. Other systems settle somewhere different each time you run them. Pool their runs and you get an average that none of them produced. Davey calls that incoherent, and he measures it with entropy. The pooled runs are more mixed than any single run, and the size of that gap shows how far the runs are from being draws from the same thing.

Ordinary tests like ANOVA can tell you that runs differ, but not by how much. This measure gives the size, on a scale you can compare across systems. The trait this sorts on is whether repeated runs agree well enough to pool. The [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) axis uses this same test.

## What goes wrong

The mistake is to pool runs that disagree and plan for the average.

## What to do instead

The better response is to look at the runs one by one before you pool them. If they agree, the average is a fair guide. If they don't, plan for the outcomes that actually happen, and prefer options that hold up in all of them.

## Examples

### A hundred copies of BERT

In 2020 Tom McCoy, Junghyun Min and Tal Linzen fine-tuned the language model BERT 100 times on the same data. The only change was the random seed. On the usual test set the copies scored almost the same, at about 84%. On a harder set of sentences where the subject and object swap places, they scored anywhere from 0% to 66%. Each copy had settled on its own way of reading, and the average of the hundred described none of them.

### The average pilot

In the late 1940s US Air Force pilots kept losing control of their jets, and on the worst day 17 crashed. The cockpit had been laid out in 1926 to fit the average pilot. In 1950 Lieutenant Gilbert Daniels measured 4,063 pilots and checked ten key sizes. Not one pilot was average on all ten. The fix was to make seats, pedals and straps adjust to fit everyone from the 5th to the 95th percentile, which is why car seats move today.

### Two factory upgrades

A chip plant takes about 100 minutes per chip and can afford one of two upgrades. Once built, the plant settles into one way of running and stays there, so a digital twin runs each option five times to see where it might settle. Option A's runs all land close to 96 minutes. Option B's runs land at 84, 96, 96.5, 96.5 and 97, so it averages 94. That 94 falls in a gap none of the runs produced. Four times in five B ends up no better than A, and one time in five it does far better. You only build one factory, so B is a one in five bet on a big win. If you need a plant you can count on, A is the better choice.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Coherent vs incoherent runs](../axes/coherent-vs-incoherent-runs.md) | Environment › Randomness | Measures with entropy how far runs disagree, so you know whether the pooled average stands for any run |
| [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) | Environment › Randomness | Runs must first disagree before it matters whether they fall into clear groups |

## Further reading

- [Incoherence: a generalized measure of complexity to quantify ensemble divergence in multi-trial experiments and simulations](https://doi.org/10.3390/e26080683), Timothy Davey, *Entropy*, 2024. The original paper, free to read.
- [Complexity, and how to measure it](https://timjdavey.com/incoherence/), Tim J. Davey. A primer with no equations, with practical and business examples.
- [incoherence](https://github.com/timjdavey/incoherence) on GitHub, Tim J. Davey. The code behind the paper, including the `ensemblepy` library and the simulations.
- [BERTs of a feather do not generalize together](https://arxiv.org/abs/1911.02969), R. Thomas McCoy, Junghyun Min and Tal Linzen, *BlackboxNLP*, 2020. The hundred BERTs study, free on arXiv.
- [The "average man"?](https://archive.org/details/DTIC_AD0010203), Gilbert S. Daniels, US Air Force Aero Medical Laboratory, 1952. Daniels's original report on why no pilot is average, from the DTIC archive.
