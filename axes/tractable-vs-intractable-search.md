# Tractable vs intractable search

An axis in the [world](README.md#the-world) group.

How many options do you have to search through? Noughts and crosses has so few possible games that you can check every one. Chess is fully visible, fixed and rule bound, yet the number of possible games is so vast that you can't. The hardest searches of all are called NP-complete, which means nobody knows a method that stays fast as the problem grows.

**Tractable**: Search the lot.
- Check every option if you can. A full search is exact and needs no tuning.
- Use a model only to speed things up. The search already gives the right answer, so the model shouldn't change it.

**Intractable**: Use the model to guide the search, not to finish it.
- Let the model suggest which branches to try. AlphaGo works this way, with a learned guess steering a search too big to finish.
- Prune hard. Drop weak looking branches early, and accept you will sometimes drop a good one.
- Accept good enough and cap the time spent. Set a budget up front, since the search will never tell you it is done.
- Check the answer with a separate checker where you can. Many hard searches have answers that are quick to check.

**Sources.** [Satisficing](../frameworks/1956-satisficing.md), [NP problems](../frameworks/1971-np-problems.md)

**Correlated with**

- [Smooth vs rugged](smooth-vs-rugged.md) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Decomposable vs holistic](decomposable-vs-holistic.md) (logic). A problem that splits into parts can be searched one part at a time, like Simon's [watchmakers](../frameworks/1962-near-decomposability.md).
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). Needing the best answer from a search too big to finish is the hardest case.
- [Slack vs time pressure](slack-vs-time-pressure.md) (tension). A search too big to finish, done against the clock, is the worst case.
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (independent). [NP problems](../frameworks/1971-np-problems.md) are hard to find and easy to check.
- [Full vs partial observability](full-vs-partial-observability.md) (independent). Chess hides nothing and still can't be searched in full.
- [Discrete vs continuous](discrete-vs-continuous.md) (opposite). Clean steps often make the search harder. Finding the best mix of products is fast when amounts can be any number, and NP-complete when they must be whole numbers ([NP problems](../frameworks/1971-np-problems.md)).
- [Choose vs design the options](choose-vs-design-the-options.md) (independent). Search size assumes the options already exist. A design problem can have only three options once someone has thought of them.
