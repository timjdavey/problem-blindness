---
type: Axis
title: Forgiving vs exacting
description: "Forgiving landscape: a small change to the inputs makes a small change to the result, so roughly right is good enough (e.g. seasoning a soup). Exacting landscape: a small change can make a big difference, so an answer that looks almost right can be worth nothing (e.g. one wrong character in code)."
group: environment
subgroup: structure
easy_end: Forgiving landscape
hard_end: Exacting landscape
sources:
  - resource: /frameworks/1970-convex-vs-non-convex-optimisation.md
    title: Convex vs non-convex optimisation
  - resource: /frameworks/1973-flat-maximum.md
    title: Flat maximum
  - resource: /frameworks/1987-rugged-fitness-landscapes.md
    title: Rugged fitness landscapes
  - resource: https://timjdavey.com
    title: Tim Davey
  - resource: https://arxiv.org/abs/2110.14168
    title: Training verifiers to solve math word problems (Cobbe, 2021)
---
# Forgiving vs exacting

An axis in the [Structure](index.md#structure) set of the [environment](index.md#environment) group.

If you change the inputs a little, does the result change a little, so rough answers and rules of thumb get you close, or can a small change make a big difference, so every detail matters and small steps stall? Seasoning a soup to taste is forgiving. A pinch more salt makes it a little saltier, so a cook who is roughly right still serves a good soup. Code is exacting. One wrong character can stop it running, so an answer that looks almost right can be worth nothing. Tim Davey frames the axis this way, as how far a small change in the inputs can move the result. Exacting means every detail has to be right, not that a mistake is fatal. One wrong character breaks the code, but you can fix it and run it again, which is the question [Survivable vs ruinous](survivable-vs-ruinous.md) asks.

Two things follow on exacting ground. Rules of thumb stop working, because being close to a good answer tells you little about how good yours is. And step by step improvement stalls. When changing one part changes what every other part is worth, the landscape fills with small peaks, and small steps stop on whichever is nearest. Stuart Kauffman called a landscape like this rugged, and one with a single gentle hill smooth ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)). Designing a new protein is exacting in both ways. Forgiving ground is kind at the top as well. Von Winterfeldt and Edwards found the best answer often sits on a flat top, so being near it is almost as good as being on it ([Flat maximum](../frameworks/1973-flat-maximum.md)).

## Actions

**Forgiving landscape**: Tweak and climb, and trust rough answers.
- Keep any small change that helps. On forgiving ground each gain is a step towards the best answer, so a cyclist can find the right saddle height a few millimetres at a time. [1, 3]
- Trust simple methods to get you close. In 1945 George Stigler worked out a cheap diet that met an adult's needs by careful guesswork. The exact answer, found in 1947, saved less than a dollar a year. [1]
- Accept an answer that is close. Near a flat top any sensible choice does about as well as the best, so a loose check will do and weeks of polishing buy little. [2]

**Exacting landscape**: Check every detail, and search wide before you search deep.
- Test for exact correctness, not a close look. Run the code, try the key in the lock or check the quote against the source, because an answer that looks almost right can be wholly wrong. [2]
- Don't trust a rule of thumb, or anyone's feeling that they are close. In 1993 Continental Lite copied some of Southwest's parts and kept others from its old business. Close to Southwest on paper, it lost an estimated $100 million in its first full year. [3]
- Start from many different points. A firm that backs several early designs, rather than polishing one, stops a bad start from deciding the result. [1, 3]
- Don't read a plateau as the top. When small changes stop helping, try a big jump that changes many linked parts at once, and expect most jumps to fail. [1, 3]
- Keep coming up with options apart from judging them. One side supplies the range and a separate judge chooses, as with a brainstorm and a tough review, or a model that drafts many answers and a checker that picks one. [5]

## Correlated with

- [Reductionist vs holistic](reductionist-vs-holistic.md) (study). In Kauffman's NK model ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)) the land gets more rugged as each part depends on more of the others. If every part adds to the score on its own, there is only one peak.
- [Tractable vs intractable options](tractable-vs-intractable-options.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). Needing the best answer on rugged land is the worst case, because small steps stop on the nearest peak. On a [flat maximum](../frameworks/1973-flat-maximum.md) the clash goes away, since good enough is nearly as good as best.
- [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md) (logic). On a rugged landscape each run stalls on whichever peak is nearest, so runs that start in different places settle in different places.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). On forgiving ground a quick look tells you if an answer is close to good. On exacting ground looking close proves nothing, so you need a check that tests every detail.
- [Stable vs chaotic](stable-vs-chaotic.md) (independent). Both are about small differences growing large, but in different places. The horizon is about errors growing over time as a system runs. Exacting is about a small change to an answer making a big change to how good it is, at one fixed moment. An exacting design problem can give each design a fixed score that never drifts.
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). Good answers that differ in kind are separate peaks, and the ground between them is a valley.
- [Clustered vs scattered runs](clustered-vs-scattered-runs.md) (logic). A rugged landscape with a few big peaks gives one cluster per peak, as runs stall on whichever is nearest.

## Citations

[1] [Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)

[2] [Flat maximum](../frameworks/1973-flat-maximum.md)

[3] [Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)

[4] [Tim Davey](https://timjdavey.com)

[5] [Training verifiers to solve math word problems (Cobbe, 2021)](https://arxiv.org/abs/2110.14168)
