---
type: Axis
title: Smooth vs rugged
description: "Smooth: a small change to the inputs makes a small change to the result, so roughly right is good enough (e.g. seasoning a soup). Rugged: a small change can make a big difference, so an answer that looks almost right can be worth nothing (e.g. one wrong character in code)."
group: world
subgroup: change
easy_end: Smooth
hard_end: Rugged
sources:
  - resource: /frameworks/1970-convex-vs-non-convex-optimisation.md
    title: Convex vs non-convex optimisation
  - resource: /frameworks/1973-flat-maximum.md
    title: Flat maximum
  - resource: /frameworks/1987-rugged-fitness-landscapes.md
    title: Rugged fitness landscapes
  - resource: https://timjdavey.com
    title: Tim Davey
---
# Smooth vs rugged

An axis in the [world](index.md#the-world) group.

If you change the inputs a little, does the result change a little, so rough answers and rules of thumb get you close, or can a small change make a big difference, so every detail matters and small steps stall? Seasoning a soup to taste is smooth. A pinch more salt makes it a little saltier, so a cook who is roughly right still serves a good soup. Code is rugged. One wrong character can stop it running, so an answer that looks almost right can be worth nothing. Tim Davey frames ruggedness this way, as how far a small change in the inputs can move the result.

Two things follow on rugged ground. Rules of thumb stop working, because being close to a good answer tells you little about how good yours is. And step by step improvement stalls. When changing one part changes what every other part is worth, the landscape fills with small peaks, and small steps stop on whichever is nearest. Designing a new protein is rugged in both ways. Smooth ground is kind at the top as well. Von Winterfeldt and Edwards found the best answer often sits on a flat top, so being near it is almost as good as being on it ([Flat maximum](../frameworks/1973-flat-maximum.md)).

## Actions

**Smooth**: Tweak and climb, and trust rough answers.
- Keep small changes to prompts, features or settings that help. On smooth ground each gain is a step towards the best answer.
- Use plain gradient methods or greedy search. They will get you near the top without anything fancier.
- Accept an answer that is close. Nearly right is nearly as good here, so a loose check will do and weeks of fine tuning buy little.

**Rugged**: Check every detail, and search wide before you search deep.
- Test for exact correctness, not a close look. Run it, compile it or check it against the source, because an answer that looks almost right can be wholly wrong.
- Don't trust a rule of thumb, or a model's sense that it is close. Looking like a good answer says little about being one.
- Start from many different points. Restarts and population methods such as evolutionary search stop one bad start from deciding the result.
- Don't read a plateau as the top. When progress stops, try a big jump before you decide you're done, and keep some poor looking candidates alive in case they sit at the foot of a higher peak.
- Pair a model that proposes many candidates with a separate scorer that picks among them. The model supplies the range and the scorer supplies the judgement.

## Correlated with

- [Decomposable vs holistic](decomposable-vs-holistic.md) (study). In Kauffman's NK model ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)) the land gets more rugged as each part depends on more of the others. If every part adds to the score on its own, there is only one peak.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). Needing the best answer on rugged land is the worst case, because small steps stop on the nearest peak. On a [flat maximum](../frameworks/1973-flat-maximum.md) the clash goes away, since good enough is nearly as good as best.
- [Coherent vs incoherent](coherent-vs-incoherent.md) (logic). On a rugged landscape each run stalls on whichever peak is nearest, so runs that start in different places settle in different places.
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (logic). On smooth ground a quick look tells you if an answer is close to good. On rugged ground looking close proves nothing, so you need a check that tests every detail.
- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (independent). Both are about small differences growing large, but in different places. The horizon is about errors growing over time as a system runs. Rugged is about a small change to an answer making a big change to how good it is, at one fixed moment. A rugged design problem can give each design a fixed score that never drifts.
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). Good answers that differ in kind are separate peaks, and the ground between them is a valley.

## Citations

[1] [Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)

[2] [Flat maximum](../frameworks/1973-flat-maximum.md)

[3] [Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)

[4] [Tim Davey](https://timjdavey.com)
