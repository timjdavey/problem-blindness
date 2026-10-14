---
type: Axis
title: Decomposable vs holistic
description: Can you split the problem into parts, solve each one and put them back together?
group: world
easy_end: Decomposable
hard_end: Holistic
sources:
  - resource: /frameworks/1948-simplicity-disorganised-and-organised-complexity.md
    title: Simplicity, disorganised complexity and organised complexity
  - resource: /frameworks/1962-near-decomposability.md
    title: Near decomposability
  - resource: /frameworks/1974-messes.md
    title: Messes
  - resource: /frameworks/1989-complex-problem-solving.md
    title: Complex problem solving
  - resource: /frameworks/2002-simple-complicated-and-complex.md
    title: Simple, complicated and complex
---
# Decomposable vs holistic

An axis in the [world](index.md#the-world) group.

Can you split the problem into parts, solve each one and put them back together? A car engine mostly can. A family, an ecosystem or a company culture can't, because the parts only make sense together.

## Actions

**Decomposable**: Split, solve and recombine.
- Give each part its own model or agent and its own test. Small parts are easier to build, check and swap out.
- Trust the whole if the parts pass. When the parts don't affect each other, good parts make a good whole.

**Holistic**: Test the whole system, not just the parts.
- Run end to end evals. Unit evals can all pass while the system fails.
- Watch for one part's gain turning into another's loss. Track a measure for the whole as well as one for each part.
- Prefer one model that sees the whole problem over a pipeline. A pipeline cuts the problem where it doesn't split.
- Change one part at a time and retest the whole. In a tangled system a small fix can break something far away.

## Correlated with

- [Smooth vs rugged](smooth-vs-rugged.md) (study). Kauffman's NK model ([Rugged fitness landscapes](../frameworks/1987-rugged-fitness-landscapes.md)) makes the land rugged by linking the parts.
- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) (bundled). [Organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md), [Normal accidents](../frameworks/1984-normal-accidents.md), [Cynefin](../frameworks/1999-cynefin.md) and Glouberman and Zimmerman's [complex problems](../frameworks/2002-simple-complicated-and-complex.md) all say tangled parts hide causes.
- [Single vs multiple objectives](single-vs-multiple-objectives.md) (bundled). In Ackoff's [messes](../frameworks/1974-messes.md) a gain in one part turns up as a loss in another.
- [Well-posed vs ill-posed](well-posed-vs-ill-posed.md) (bundled). [Rittel and Webber](../frameworks/1973-tame-vs-wicked-problems.md) call each wicked problem a symptom of another, and [Jonassen](../frameworks/2000-problem-typology.md) ranks problems on structure and complexity together.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (logic). A problem that splits into parts can be solved one small unit at a time, like Simon's [watchmakers](../frameworks/1962-near-decomposability.md).
- [Loose vs tight coupling](loose-vs-tight-coupling.md) (independent). Perrow keeps tangled parts and lack of slack apart in [Normal accidents](../frameworks/1984-normal-accidents.md). A university is tangled but loose, and a dam is tight but simple.
- [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md) (bundled). In Ackoff's [messes](../frameworks/1974-messes.md) the fix for one department becomes the next department's problem, so nobody holds the levers for the whole.

## Citations

[1] [Simplicity, disorganised complexity and organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md)

[2] [Near decomposability](../frameworks/1962-near-decomposability.md)

[3] [Messes](../frameworks/1974-messes.md)

[4] [Complex problem solving](../frameworks/1989-complex-problem-solving.md)

[5] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)
