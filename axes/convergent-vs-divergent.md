---
type: Axis
title: Convergent vs divergent
description: "Convergent: the good answers sit together, so a blend of two good ones is also good (e.g. a sum, or a phone trading battery life for size). Divergent: the good answers differ in kind, so halfway between two is worse than either (e.g. a funny wedding speech and a moving one)."
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

Do the good answers sit together, or in separate places that differ in kind? A sum has one right answer. A wedding speech, a logo or a sonnet about autumn has many, and two very different ones can both be excellent. J. P. Guilford called the thinking for the first kind convergent and for the second divergent.

The test is whether you can blend two good answers and still have a good one. A phone can swap battery life for size, and any phone between two good ones is also a good phone, so you can split the difference. That is the convergent end, even though there are many good phones. How many good answers there are, and where they sit along the trade off, is a question for [Single objective vs trade-offs](single-objective-vs-trade-offs.md). The divergent end is when the good answers differ in kind. Halfway between a funny speech and a moving one is a speech that is neither, so averaging and compromise land in the gap.

This axis asks about the shape of the good answers, not about who wants them. A best man writing alone has one goal, a good speech, and nobody to argue with. The answers still differ in kind.

## Actions

**Convergent**: Aim for the middle, and score against the key.
- Use exact match, unit tests or a reference answer where there is one right answer. They tell you if the model is right without anyone reading the output.
- Turn the model's randomness down, which is called lowering the temperature. You want the same good answer every time, not variety.
- Averaging is safe. A model that predicts the mean of its examples, or an ensemble that averages several models, lands on a good answer.

**Divergent**: Commit to one answer, and judge it on quality, not match.
- Commit to one answer, and don't blend two. Halfway between two good answers that differ in kind is often worse than either.
- Train the model to sample one good answer, not to predict the average of them. If half the demonstrations steer left round a tree and half steer right, a model that learns the average drives straight into it.
- Reward variety. Generate several and keep the best, rather than asking for one safe answer. The safe answer is often the blend.
- Never score against one reference answer. Good answers that differ in kind can't share one key, so it punishes every good answer but one.
- Use human raters or a model grader with a clear rubric. The rubric says what good looks like without fixing one answer.
- Compare outputs in pairs. People judge which of two is better more reliably than they give a score out of ten.

## Correlated with

- [Well vs ill-structured](well-vs-ill-structured.md) (independent). "Write a sonnet about autumn" is well structured. You know what is wanted and when you're done, yet there are endless good answers.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). One right answer can be checked against a key. Many good answers need someone to judge them.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (independent). Many good answers don't settle whether extra quality pays. A wedding speech only needs to be good. An advert has just as many good answers, yet each extra bit of quality still pays off in sales.
- [Choose vs design the options](choose-vs-design-the-options.md) (logic). Options you invent rarely line up to one right answer.
- [Single objective vs trade-offs](single-objective-vs-trade-offs.md) (independent). Both give many good answers, but a trade off between goals gives answers that differ only in degree, and there a blend of two good ones is also good. A car buyer has trade-offs and convergent answers. A best man has one goal and divergent answers. Choosing between two job offers is both, since salary pulls against location and the two jobs differ in kind.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). When the options differ in kind there is no middle ground to settle on. Two towns that each want the bridge can't have half of it each, so someone has to lose. But a fork with one owner is still a fork. The best man has nobody to argue with and still can't blend the two drafts.
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). Good answers that differ in kind are separate peaks, and the ground between them is a valley.
- [Coherent vs incoherent](coherent-vs-incoherent.md) (logic). It is the same trap on the answer side. Runs that split into groups average to a result none of them produced, and good answers that differ in kind blend into one nobody would choose.
- [Spread vs single bet](spread-vs-single-bet.md) (logic). Spreading is not blending. You can't blend a funny speech and a moving one, but you can draft both and keep one. A barbell beats the middling option because it spreads across a fork instead of blending it.

## Citations

[1] [Convergent vs divergent thinking](../frameworks/1956-convergent-vs-divergent-thinking.md)
