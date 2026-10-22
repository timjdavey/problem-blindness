---
type: Axis
title: Tractable vs intractable search
description: "Tractable search: you know every option and there are few enough to check them all (e.g. noughts and crosses). Intractable search: you know every option, but there are too many for any computer to check (e.g. Go, with about 10¹⁷⁰ legal board positions)."
group: environment
subgroup: structure
easy_end: Tractable search
hard_end: Intractable search
sources:
  - resource: /frameworks/1956-satisficing.md
    title: Satisficing
  - resource: /frameworks/1971-np-problems.md
    title: NP problems
---
# Tractable vs intractable search

An axis in the [Structure](index.md#structure) set of the [environment](index.md#environment) group.

Are there few enough options to check them all, or so many that no computer could, even when the rules are clear and everything is in view? Noughts and crosses has so few possible games that you can check every one. Go is fully visible, fixed and rule bound, yet it has about 10¹⁷⁰ legal board positions, far more than there are atoms in the universe, so you can't. The hardest problems whose answers are quick to check are called NP-complete. Nobody knows a method for them that stays fast as the problem grows.

## Actions

**Tractable search**: Search the lot.
- Check every option if you can. A full search is exact and needs no tuning.
- Use a model only to speed things up. The search already gives the right answer, so the model shouldn't change it.

**Intractable search**: Use the model to guide the search, not to finish it.
- Let the model suggest which branches to try. AlphaGo works this way, with a learned guess steering a search too big to finish.
- Prune hard. Drop weak looking branches early, and accept you will sometimes drop a good one.
- Accept good enough and cap the time spent. Set a budget up front, since the search will never tell you it is done.
- Check the answer with a separate checker where you can. Many hard searches have answers that are quick to check.

## Correlated with

- [Smooth vs rugged](smooth-vs-rugged.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Decomposable vs tangled](decomposable-vs-tangled.md) (logic). A problem that splits into parts can be searched one part at a time, like Simon's [watchmakers](../frameworks/1962-near-decomposability.md).
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). Needing the best answer from a search too big to finish is the hardest case.
- [Ample time vs time pressure](ample-time-vs-time-pressure.md) (tension). A search too big to finish, done against the clock, is the worst case.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (independent). [NP problems](../frameworks/1971-np-problems.md) are hard to find and easy to check.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (independent). Go hides nothing, so there is no fact left to find, and it still can't be searched in full.
- [Small vs large world](small-vs-large-world.md) (independent). Search size assumes a procedure generates the options. More computing power can finish a big search in principle. It can't search outcomes nobody can generate.
- [Given vs invented options](given-vs-invented-options.md) (independent). Search size assumes the options already exist. A design problem can have only three options once someone has thought of them.
- [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md) (independent). Knowing how the pieces move in chess is bounded and playing chess well is open-ended, in one and the same game. Research taste has no ceiling and no list of options to search.

## Citations

[1] [Satisficing](../frameworks/1956-satisficing.md)

[2] [NP problems](../frameworks/1971-np-problems.md)
