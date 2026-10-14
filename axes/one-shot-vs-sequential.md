# One-shot vs sequential

An axis in the [decision](README.md#the-decision) group.

Is it a single choice, or a chain where each step shapes the next? Choosing a paint colour is one shot. Running a project or treating a long illness is a series of moves, and it's hard to tell which early move caused the final result.

**One-shot**: Get the single call right.
- Put the effort in before you act. There is no second go.
- Use the best model and the most checks you can afford. All the value rests on this one output.

**Sequential**: Act, watch and adjust.
- Treat it as a trade off between trying new moves and repeating good ones. Bandits and reinforcement learning are built for this.
- Credit each move with its share of the final result. Otherwise the last move gets the blame for what an early one caused.
- Watch for effects that show up late. Judge a move by where it led, not by the next step.
- Keep room to change course. Each step should leave the next one open.

**Sources.** [Multi-armed bandit](../frameworks/1933-multi-armed-bandit.md), [Exploration vs exploitation](../frameworks/1991-exploration-vs-exploitation.md), [Task environment properties](../frameworks/1995-task-environment-properties.md)

**Correlated with**

- [Transparent vs opaque causes](transparent-vs-opaque-causes.md) and [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (study). In Senge's [beer game](../frameworks/1990-detail-vs-dynamic-complexity.md) delays between moves and results hide which move caused what.
- [Known vs unknown odds](known-vs-unknown-odds.md) (opposite). In a [bandit](../frameworks/1933-multi-armed-bandit.md) problem each choice teaches you something, so repeating the choice slowly turns unknown odds into known ones.
- [Reversible vs irreversible](reversible-vs-irreversible.md) (opposite). A chain of moves usually gives you a chance to correct course, so sequential problems lean towards the reversible end. Watch the name clash. [Rittel and Webber](../frameworks/1973-tame-vs-wicked-problems.md) call each try at a wicked problem a one-shot operation, but they mean it can't be undone. That is a point about reversibility, not about how many moves there are.
- [Test vs watch](test-vs-watch.md) (opposite). Each pull of a [bandit](../frameworks/1933-multi-armed-bandit.md) is a small test, so a chain of choices lets you test as you go. Thompson picked each new patient's treatment at random, weighted towards whichever looked better so far.
- [Additive vs multiplicative](additive-vs-multiplicative.md) (by definition). The gap between the crowd and the single player only opens over repeated plays. For a single toss of Peters' coin the crowd's average is a fair guide, and the harm builds up toss by toss ([Ergodicity](../frameworks/2016-ergodicity.md)).
