---
type: Framework
title: Funnel experiment
description: >-
  Drop marbles through a funnel at a target and move the funnel after each miss to cancel it, and the marbles spread wider, not narrower. Deming called this tampering. A reading that jumps about may be noise from a stable process, and correcting for noise adds to it.
date: 1986
creators:
  - W. Edwards Deming
sources:
  - resource: https://mitpress.mit.edu/9780262535946/out-of-the-crisis/
    title: Out of the Crisis
  - resource: https://archive.org/details/outofcrisis0000demi
    title: Out of the Crisis (Internet Archive)
  - resource: https://sites.ualberta.ca/~yreshef/orga432/funnel.html
    title: The funnel experiment (Yonatan Reshef, University of Alberta)
  - resource: https://en.wikipedia.org/wiki/W._Edwards_Deming
    title: W. Edwards Deming (Wikipedia)
  - resource: https://doi.org/10.1115/1.3662552
    title: A new approach to linear filtering and prediction problems
  - resource: https://en.wikipedia.org/wiki/Kalman_filter
    title: Kalman filter (Wikipedia)
---
# Funnel experiment

**Move the funnel after every miss and the marbles spread wider. A reading that jumps about may be noise, and correcting for noise adds to it.**

1986 · W. Edwards Deming · [Original book](https://mitpress.mit.edu/9780262535946/out-of-the-crisis/) · Feeds 2 axes

## The idea

W. Edwards Deming was a statistician who learnt his trade from Walter Shewhart at Bell Labs in the 1930s. Shewhart had split the variation in any process into two kinds. Common causes are the everyday jitter of a stable process, and they belong to the system. Special causes are events from outside it, like a worn tool or a new supplier. Deming spent the 1950s teaching this to Japanese engineers and the 1980s teaching it to American managers. His 1986 book *Out of the Crisis* set out the funnel experiment to show what goes wrong when the two are confused.

The experiment needs a funnel, a marble and a target on a table. Drop the marble through the funnel and mark where it lands. It never lands on the same spot twice, because the process has common causes in it. Deming then gave four rules for where to hold the funnel next. Rule 1 leaves it over the target. Rule 2 moves it from where it was to cancel the last miss. Rule 3 moves it from the target to cancel the last miss. Rule 4 sets it over wherever the last marble landed. Rule 1 gives a stable cluster. Rule 2 roughly doubles the spread. Rule 3 swings ever wider, as each miss is overcorrected in turn. Rule 4 wanders off the table, since each marble sets the aim for the next. Deming called rules 2 to 4 tampering, and said they are what people do by instinct.

The trait this sorts on is whether a change in a reading means a change in the thing. In a stable process it usually doesn't. The reading moved because readings always move, and the right response is to leave the process alone until a reading falls outside its usual spread. A fixed fact seen through a noisy instrument works the same way. The fact hasn't moved. Only your view of it has.

Rudolf Kalman gave the maths for the other case in 1960. If the thing really does move, and each reading of it is noisy, the best estimate pools the readings and weights each by how far it can be trusted. Both ideas say the same thing. Don't act on one reading. Work out what the readings together say.

## What goes wrong

The mistake is to treat every reading as news. An operator resets a machine after each part that comes out a shade off, and the parts come out less alike than if the machine had been left alone. That is Rule 2. A manager who sets each month's target from last month's result is on Rule 4, and so is a worker trained by a worker who was trained by a worker, with each copy drifting a little from the last. Each correction is aimed at the last miss, and the last miss was mostly chance, so the correction adds its own error on top.

## What to do instead

The better response is to learn the usual spread of the process first, from many readings taken while nobody tampers. Then act only when a reading falls outside that spread, or when the readings drift one way, since those point to a special cause. A reading inside the usual spread tells you nothing on its own, however far it sits from the target. If the spread itself is too wide, change the process, not the aim.

## Examples

### The four rules on a table

Yonatan Reshef at the University of Alberta runs the experiment in class and publishes the drops. Over 15 drops, Rule 1 landed between 5 units short and 5 long. Rule 2 ran from 10 short to 7 long. Rule 3 ran from 14 short to 16 long, swinging from one side to the other. Every rule that tried to correct the last miss did worse than leaving the funnel alone.

### Apollo's star sightings

The Apollo navigation computer had to know where the spacecraft was from measurements that were each a little off. Stanley Schmidt at NASA Ames saw that Kalman's filter fitted the job after Kalman visited, and it went into the flight computer. The filter pooled every measurement so far and weighted each by its reliability. No single reading was trusted, and the estimate got tighter with each one. It is the same lesson as the funnel from the other side. When the readings are noisy, pool them rather than chase them.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) | Environment › Randomness | A reading that jumps about may be noise from a stable process, and re-aiming after each reading widens the spread |
| [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | Information › Uncertainty | A fixed fact seen through a noisy instrument looks like chance, and pooled readings close in on it |

## Further reading

- [Out of the Crisis](https://mitpress.mit.edu/9780262535946/out-of-the-crisis/), W. Edwards Deming, MIT Press, 1986. The original book. Chapter 11 has the funnel experiment and the four rules.
- [Out of the Crisis](https://archive.org/details/outofcrisis0000demi) on the Internet Archive. A copy to borrow.
- [The funnel experiment](https://sites.ualberta.ca/~yreshef/orga432/funnel.html), Yonatan Reshef, University of Alberta. A free one page explainer with the four rules and a table of drops.
- [W. Edwards Deming](https://en.wikipedia.org/wiki/W._Edwards_Deming) on Wikipedia. Covers common and special causes.
- [A new approach to linear filtering and prediction problems](https://doi.org/10.1115/1.3662552), Rudolf Kalman, *Journal of Basic Engineering*, 1960. The maths for pooling noisy readings of a moving target.
- [Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter) on Wikipedia. Has the Apollo story.
