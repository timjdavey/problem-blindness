# Reducible vs irreducible uncertainty

An axis in the [knower](README.md#the-knower) group.

Could more information shrink your doubt, or would no amount of fact finding settle it? Some doubt is pure chance, like the next roll of a dice. Some hangs on choices people haven't made yet, like whether a rival will cut prices next year. Some is a clash over what the facts mean. If your doubt is reducible you should go and gather data. If it's irreducible you should hedge instead.

**Reducible**: Go and get the data.
- Label more cases. Focus labelling on the cases the model is least sure of, which is called active learning.
- Ask the user the missing question before acting. One question often settles what no model could guess.

**Irreducible**: Stop paying for more data and hedge instead.
- Report a spread, not a single answer. More training won't shrink the doubt, so hiding it only misleads.
- Spread your bets. Make the decision cope with either result instead of staking it on one.
- Use an ensemble to tell the two kinds of doubt apart. Models that disagree point to doubt more data could fix. Models that agree on a wide spread point to doubt it can't.
- Check where the doubt comes from. If it hangs on a choice nobody has made yet, no data will settle it, so plan for each way the choice could go.

**Sources.** [Uncertainty vs equivocality](../frameworks/1986-uncertainty-vs-equivocality.md), [Puzzles vs mysteries](../frameworks/2001-puzzles-vs-mysteries.md)

**Correlated with**

- [Deterministic vs statistical](deterministic-vs-statistical.md) (logic). Pure chance is one kind of doubt that no new data can shrink.
- [Long vs short predictability horizon](long-vs-short-predictability-horizon.md) (logic). Past the horizon more data barely moves the forecast.
- [Full vs partial observability](full-vs-partial-observability.md) (opposite). Hidden facts are the classic reducible doubt, like Treverton's [puzzles](../frameworks/2001-puzzles-vs-mysteries.md), so partial observability usually leans to the reducible end.
- [Shared vs contested values](shared-vs-contested-values.md) (bundled). Treverton's mysteries and Daft and Lengel's [equivocality](../frameworks/1986-uncertainty-vs-equivocality.md) are doubts that more facts won't settle, because people read the facts differently or haven't yet chosen what to do.
- [Known vs unknown odds](known-vs-unknown-odds.md) (independent). Reducible asks whether more data would shrink your doubt, while known odds asks whether you can put a number on it. A coin toss has known odds and irreducible doubt. A new drug has unknown odds and reducible doubt, because you can run a trial.
