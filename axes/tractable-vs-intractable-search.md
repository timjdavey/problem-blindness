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
  - resource: https://doi.org/10.1515/9783110800647
    title: Thought and choice in chess (de Groot, 1965)
  - resource: https://doi.org/10.1016/0004-3702%2875%2990019-3
    title: An analysis of alpha-beta pruning (Knuth, 1975)
  - resource: https://doi.org/10.1038/nature16961
    title: Mastering the game of Go with deep neural networks and tree search (Silver, 2016)
---
# Tractable vs intractable search

An axis in the [Structure](index.md#structure) set of the [environment](index.md#environment) group.

Are there few enough options to check them all, or so many that no computer could, even when the rules are clear and everything is in view? Noughts and crosses has so few possible games that you can check every one. Go is fully visible, fixed and rule bound, yet it has about 10¹⁷⁰ legal board positions, far more than there are atoms in the universe, so you can't. The hardest problems whose answers are quick to check are called NP-complete. Nobody knows a method for them that stays fast as the problem grows.

## Actions

**Tractable search**: Search the lot.
- Check every option if you can. A full search is exact and needs no tuning. [1]
- Let hunches set the order of the search, not its answer. Trying the likeliest option first makes a full search finish sooner, and what it finds stays the same. [4]

**Intractable search**: Use judgement to guide the search, not to finish it.
- Let an expert's eye pick which branches to try. Adriaan de Groot found chess masters looked at no more moves than weaker players, but chose better ones to look at. AlphaGo works the same way, letting a guess it learnt from past games steer a search too big to finish. [3, 5]
- Prune hard. Drop weak looking branches early, and accept you will sometimes drop a good one. [2, 5]
- Accept good enough and cap the time spent. Set a budget up front, since the search will never tell you it is done. [1, 2]
- Use a quick check to compare the answers you find. Many hard searches have answers that are quick to check. A courier can't find the best route for 20 drops, but can add up the miles on any route in seconds. [2]

## Correlated with

- [Forgiving vs exacting](forgiving-vs-exacting.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Reductionist vs holistic](reductionist-vs-holistic.md) (logic). A problem that splits into parts can be searched one part at a time, like Simon's [watchmakers](../frameworks/1962-near-decomposability.md).
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

[3] [Thought and choice in chess (de Groot, 1965)](https://doi.org/10.1515/9783110800647)

[4] [An analysis of alpha-beta pruning (Knuth, 1975)](https://doi.org/10.1016/0004-3702%2875%2990019-3)

[5] [Mastering the game of Go with deep neural networks and tree search (Silver, 2016)](https://doi.org/10.1038/nature16961)
