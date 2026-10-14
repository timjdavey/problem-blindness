# Update Log

## 2026-10-14

* **Creation**: Added the [Spread vs single bet](/axes/spread-vs-single-bet.md) axis, which asks whether you can split your stake across several options at once or must take one course of action. It differs from [Reversible vs irreversible](/axes/reversible-vs-irreversible.md), which spreads your tries across time rather than across options.
* **Creation**: Added the [Portfolio selection](/frameworks/1952-portfolio-selection.md) framework, from Harry Markowitz's 1952 paper in the Journal of Finance.
* **Update**: Added a barbell example to [Fragile, robust and antifragile](/frameworks/2012-fragile-robust-and-antifragile.md).
* **Update**: Split the divergent end of [Convergent vs divergent](/axes/convergent-vs-divergent.md) into answers that differ in degree and answers that differ in kind. Blending two good answers works for the first and fails for the second, which is the answer side of [Coherent vs incoherent](/axes/coherent-vs-incoherent.md). A separate Dial vs fork axis was considered and folded in here.
* **Update**: Folded Full vs partial observability into [Reducible vs irreducible uncertainty](/axes/reducible-vs-irreducible-uncertainty.md). A hidden fact is the main kind of reducible doubt, and the two axes gave the same advice.
* **Update**: Separated [Small vs large world](/axes/small-vs-large-world.md) from [Tractable vs intractable search](/axes/tractable-vs-intractable-search.md). A small world is one where a fixed procedure generates the outcomes, so you can sample them however many there are. Intractable search only applies once the options are known. Go, with about 10¹⁷⁰ legal positions, replaces chess as the intractable example, and each axis now links to the other.
* **Update**: Rewrote every axis description to describe each end in one line with a short example, in place of a single long question. The [axes index](/axes/index.md) now lists both ends under each axis.
* **Update**: Reframed [Smooth vs rugged](/axes/smooth-vs-rugged.md) around how far a small change in the inputs can move the result, following Tim Davey. Local peaks are now one result of that, and the axis cites the [Flat maximum](/frameworks/1973-flat-maximum.md).
* **Creation**: Added the [Coherent vs incoherent](/axes/coherent-vs-incoherent.md) axis, which asks whether repeated runs agree well enough for the average to stand for a typical run.
* **Creation**: Added the [Incoherence](/frameworks/2024-incoherence.md) framework, from Tim Davey's 2024 paper in Entropy.
* **Creation**: Added the [Clustered vs scattered](/axes/clustered-vs-scattered.md) axis, which asks whether runs that disagree still fall into a few clear groups.
* **Creation**: Added the [Cohesion](/frameworks/2023-cohesion.md) framework, from Tim Davey's 2023 paper in Entropy.
* **Update**: Moved the project to the [Open Knowledge Format](https://okf.md) 0.2. Every framework and axis now has `type`, `title`, `description` and `sources` front matter.
* **Creation**: Added the root [index](/index.md), the [axes index](/axes/index.md), the [frameworks index](/frameworks/index.md) and the [Reading the axes](/axes/reading-the-axes.md) guide, which replace the folder READMEs.
* **Update**: Folded Commensurable vs incommensurable values into [Single vs multiple objectives](/axes/single-vs-multiple-objectives.md). It only applies when there are several objectives, and its main action matched setting a floor for each one.
* **Update**: Folded Convex vs concave payoff into [Thin vs fat tails](/axes/thin-vs-fat-tails.md). Its actions were already covered by fat tails, ruin and irreversibility, so only the point about changing your exposure moved across.
* **Update**: Removed Discrete vs continuous. Its hard end isn't harder, since whole number problems are often the harder search, and its actions were already under [Easy vs hard to verify](/axes/easy-vs-hard-to-verify.md). Moravec's paradox now sits in [Explicit vs tacit know-how](/axes/explicit-vs-tacit-know-how.md).
