# Discrete vs continuous

An axis in the [world](README.md#the-world) group.

Does the problem move in clean steps or by degrees? A chess move is one of a fixed set, and a square is either taken or not. Steering a car, setting a drug dose or judging how hard to brake is a matter of degree, so the answer is a number and being a little off counts.

**Discrete**: Treat it as classification or search, with exact checks.
- Score exact matches. Each answer is right or wrong, so there is no tolerance to argue about.
- Use solvers where they fit. Rule engines and search often beat a model on clean steps.

**Continuous**: Decide how close is close enough before you start.
- Set a tolerance for each output. Without one, nobody can say if the model passed.
- Predict a range, not just a point. A range tells the user how far off the answer might be.
- Test near the edges of the tolerance. That is where small errors cross the line.
- Budget for far more data and simulation on physical tasks. Control tasks need much more than their ease for people suggests, which is Moravec's paradox.

**Sources.** [Task environment properties](../frameworks/1995-task-environment-properties.md), [Convex vs non-convex optimisation](../frameworks/1970-convex-vs-non-convex-optimisation.md), [Moravec's paradox](../frameworks/1988-moravecs-paradox.md)

**Correlated with**

- [Tractable vs intractable search](tractable-vs-intractable-search.md) (opposite). Clean steps often make the search harder, not easier. Finding the best mix of products to make is fast when amounts can be any number. Insist they are whole numbers and it becomes one of Karp's 21 NP-complete problems ([NP problems](../frameworks/1971-np-problems.md)).
- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (study). [Moravec's paradox](../frameworks/1988-moravecs-paradox.md) is that machines beat people at chess long before they could walk across a room. Skills of degree, like balance and grip, are the ones nobody can write down.
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (logic). A discrete answer is right or wrong. A continuous one is only close or far, so checking it needs a tolerance someone has to pick.
