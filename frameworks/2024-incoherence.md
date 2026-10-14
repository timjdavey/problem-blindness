---
type: Framework
title: Incoherence
description: >-
  Run the same system many times and compare the runs. If they agree, the average stands for a typical run. If each run lands somewhere different, the average can describe none of them, and planning for it goes wrong.
date: 2024
creators:
  - Tim J. Davey
sources:
  - resource: https://doi.org/10.3390/e26080683
  - resource: https://timjdavey.com/incoherence/
---

# Incoherence

Most of the time we sum up a system by its average and its spread. Run a simulation five times, take the mean, add an error bar and move on. In 2024 Tim Davey argued in the journal Entropy that this hides a question worth asking first. Can the average stand in for a typical run at all?

A die is random, but every roll draws from the same spread, so a thousand rolls tell you what the next one will look like. Davey calls that coherent. Other systems settle somewhere different each time you run them. Pool their runs and you get an average that none of them produced. Davey calls that incoherent, and he measures it with entropy. The pooled runs are more mixed than any single run, and the size of that gap shows how far the runs are from being draws from the same thing. Unlike a test of whether runs differ, it says how much they differ, and on a scale you can compare across systems.

The mistake is to pool runs that disagree and plan for the average. Ordinary tests like ANOVA can tell you that runs differ, but not by how much. The better response is to look at the runs one by one before you pool them. If they agree, the average is a fair guide. If they don't, plan for the outcomes that actually happen, and prefer options that hold up in all of them.

## Examples

**The train connection.** You take two one hour trains with ten minutes to change, then a taxi. The first train often runs late, and two times in five you miss the connection and wait an hour. Run the trip many times and arrivals pile up at 2 hours 10 and 3 hours 10. The average is 2 hours 34, a time that almost never happens. Book the taxi for 2 hours 10 and rebook if you miss the train.

**The average pilot.** In the late 1940s US Air Force pilots kept losing control of their jets, and on the worst day 17 crashed. The cockpit had been laid out in 1926 to fit the average pilot. In 1950 Lieutenant Gilbert Daniels measured 4,063 pilots and checked ten key sizes. Not one pilot was average on all ten. The fix was to make seats, pedals and straps adjust to fit everyone from the 5th to the 95th percentile, which is why car seats move today.

**Two factory upgrades.** A chip plant takes about 100 minutes per chip and can afford one of two upgrades. A digital twin runs each five times. Option A averages 96 minutes, and its runs sit almost on top of each other. Option B averages 94, but one run is brilliant and the other four land between 93 and 99.5. The 94 falls in a gap none of the runs produced. You only build one factory, so B is a one in five bet on a big win. A is the better choice.
