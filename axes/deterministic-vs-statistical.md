# Deterministic vs statistical

An axis in the [world](README.md#the-world) group.

Do the same inputs always give the same result, or only a stable spread of results? A sum is deterministic. Which boiler breaks down this winter is statistical, though the rate across many boilers is steady.

**Deterministic**: Write the rule down and test it like code.
- Don't ask a model to guess at a rule you could state. A rule that is right most of the time is a bug.
- Use the model to draft the rule or the code, then check that against tests. The tests decide if it ships, not the model.
- Test for exact output. The same input should give the same answer every run, so any variation is a fault to fix.

**Statistical**: Judge the spread, not single cases.
- Evaluate on a large held-out set. A few good examples tell you nothing when any one case can go either way.
- Report error rates and calibration. Calibration means that when the model says 70%, it is right about 70% of the time.
- Decide as a policy over many cases. Ask what rule gives the best results across the whole group, not what suits this one.
- Don't judge the model on one bad outcome. A right call can still lose, so look at the rate across many calls.

**Sources.** [Simplicity, disorganised complexity and organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md), [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md), [Task environment properties](../frameworks/1995-task-environment-properties.md)

**Correlated with**

- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (bundled). [Clocks and clouds](../frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end, though chaos shows a fully deterministic system can still have a short horizon.
- [Full vs partial observability](full-vs-partial-observability.md) (logic). Russell and Norvig note that a deterministic world you can only half see looks random to you ([Task environment properties](../frameworks/1995-task-environment-properties.md)).
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). Pure chance is one kind of doubt that no new data can shrink.
- [Thin vs fat tails](thin-vs-fat-tails.md) (by definition). The tails axis only applies once a problem is statistical. A deterministic problem has no spread of results, so it has no tails to speak of.
