---
type: Axis
title: Convergent vs divergent
description: "Convergent: there is one right answer that everyone would agree on (e.g. a sum). Divergent: there are many good answers that differ in kind (e.g. a wedding speech)."
group: decision
subgroup: goal
easy_end: Convergent
hard_end: Divergent
sources:
  - resource: /frameworks/1956-convergent-vs-divergent-thinking.md
    title: Convergent vs divergent thinking
---
# Convergent vs divergent

An axis in the [Goal](index.md#goal) set of the [decision](index.md#the-decision) group.

Is there one right answer that everyone would agree on, or many good answers that differ in kind? A sum has one. A wedding speech, a logo or a sonnet about autumn has many, and two very different ones can both be excellent. J. P. Guilford called the thinking for the first kind convergent and for the second divergent.

Many good answers come in two shapes. Some lie along one trade off and differ only in degree. A phone can swap battery life for size, and any phone between two good ones is also a good phone, so you can split the difference. [Single objective vs trade-offs](single-objective-vs-trade-offs.md) covers that case. Others differ in kind, and that is the hard end of this axis. Halfway between a funny speech and a moving one is a speech that is neither, so averaging and compromise land in the gap.

## Actions

**Convergent**: Score against the key.
- Use exact match, unit tests or a reference answer. They tell you if the model is right without anyone reading the output.
- Turn the model's randomness down, which is called lowering the temperature. You want the one right answer every time, not variety.

**Divergent**: Judge quality, not match.
- Use human raters or a model grader with a clear rubric. The rubric says what good looks like without fixing one answer.
- Compare outputs in pairs. People judge which of two is better more reliably than they give a score out of ten.
- Reward variety. Generate several and keep the best, rather than asking for one safe answer.
- Never score a creative task against one reference answer. It punishes good answers that differ from it.
- Commit to one answer, and don't blend two. Halfway between two good answers that differ in kind is often worse than either.
- Train the model to sample one good answer, not to predict the average of them. If half the demonstrations steer left round a tree and half steer right, a model that learns the average drives straight into it.

## Correlated with

- [Well vs ill-structured](well-vs-ill-structured.md) (independent). "Write a sonnet about autumn" is well structured. You know what is wanted and when you're done, yet there are endless good answers.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). One right answer can be checked against a key. Many good answers need someone to judge them.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (independent). Many good answers don't settle whether extra quality pays. A wedding speech only needs to be good. An advert has just as many good answers, yet each extra bit of quality still pays off in sales.
- [Choose vs design the options](choose-vs-design-the-options.md) (logic). Options you invent rarely line up to one right answer.
- [Single objective vs trade-offs](single-objective-vs-trade-offs.md) (logic). A trade off between goals gives many good answers that differ only in degree. There a blend of two good answers is also good.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). When the options differ in kind there is no middle ground to settle on. Two towns that each want the bridge can't have half of it each, so someone has to lose.
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). Good answers that differ in kind are separate peaks, and the ground between them is a valley.
- [Coherent vs incoherent](coherent-vs-incoherent.md) (logic). It is the same trap on the answer side. Runs that split into groups average to a result none of them produced, and good answers that differ in kind blend into one nobody would choose.
- [Spread vs single bet](spread-vs-single-bet.md) (logic). Spreading is not blending. You can't blend a funny speech and a moving one, but you can draft both and keep one. A barbell beats the middling option because it spreads across a fork instead of blending it.

## Citations

[1] [Convergent vs divergent thinking](../frameworks/1956-convergent-vs-divergent-thinking.md)
