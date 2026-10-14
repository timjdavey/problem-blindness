---
type: Axis
title: Smooth vs rugged
description: Can small steps carry you to the best answer, or will they get stuck?
group: world
easy_end: Smooth
hard_end: Rugged
sources:
  - resource: /frameworks/1970-convex-vs-non-convex-optimisation.md
    title: Convex vs non-convex optimisation
  - resource: /frameworks/1987-rugged-fitness-landscapes.md
    title: Rugged fitness landscapes
---
# Smooth vs rugged

An axis in the [world](index.md#the-world) group.

Can small steps carry you to the best answer, or will they get stuck? On a smooth problem every step that helps also brings you closer to the best answer, so steady tweaking works. On a rugged one there are many local peaks, and small steps stop on whichever is nearest. Seasoning a soup to taste is smooth. Designing a new protein is rugged, because changing one part changes what every other part is worth.

## Actions

**Smooth**: Tweak and climb.
- Keep small changes to prompts, features or settings that help. On smooth ground each gain is a step towards the best answer.
- Use plain gradient methods or greedy search. They will get you near the top without anything fancier.

**Rugged**: Search wide before you search deep.
- Start from many different points. Restarts and population methods such as evolutionary search stop one bad start from deciding the result.
- Keep some poor looking candidates alive. A weak design today may sit at the foot of a much higher peak.
- Don't read a plateau as the top. When progress stops, try a big jump before you decide you're done.
- Pair a model that proposes many candidates with a separate scorer that picks among them. The model supplies the range and the scorer supplies the judgement.

## Correlated with

- [Decomposable vs holistic](decomposable-vs-holistic.md) (study). In Kauffman's NK model ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)) the land gets more rugged as each part depends on more of the others. If every part adds to the score on its own, there is only one peak.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). Needing the best answer on rugged land is the worst case, because small steps stop on the nearest peak.
- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (independent). They sound alike but ask different things. Rugged is about many peaks among the possible answers. The horizon is about small errors growing over time. A rugged design problem can give each design a fixed score that never drifts.

## Citations

[1] [Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)

[2] [Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)
