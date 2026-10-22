---
type: Axis
title: Bounded vs open-ended skill
description: "Bounded skill: the know-how is a small, closed set that anyone competent masters fully (e.g. the alphabet). Open-ended skill: the know-how has no ceiling, so solvers keep improving and differ widely (e.g. knowing which research questions are worth asking)."
group: agent
subgroup: know-how
easy_end: Bounded skill
hard_end: Open-ended skill
sources:
  - resource: /frameworks/2005-constrained-vs-unconstrained-skills.md
    title: Constrained vs unconstrained skills
---
# Bounded vs open-ended skill

An axis in the [Know-how](index.md#know-how) set of the [agent](index.md#agent) group.

Can the know-how the task needs be learnt in full, or does it have no ceiling? There are 26 letters, and once you know them all there is nothing left to learn. Interpreting a poem is different. Readers find more in the same sonnet at sixty than they did at sixteen. Research taste is the same. Knowing which questions are worth asking keeps improving over a whole career, and the best researchers are far ahead of the merely good. Scott Paris called the first kind constrained and the second unconstrained ([Constrained vs unconstrained skills](../frameworks/2005-constrained-vs-unconstrained-skills.md)).

The axis matters most when you test a solver. On a bounded skill a test can cover everything, and every competent solver ends up with full marks. On an open-ended skill any test is a small sample, and a full score only says the test ran out of room.

## Actions

**Bounded skill**: Test all of it, then check it off.
- Test the whole set, not a sample. With a closed list, like unit conversions or a house style guide, you can check every case.
- Once a solver passes, use the test as a gate and stop using it to rank. At the ceiling everyone competent scores the same, so a driving test says who may drive, not who drives best.

**Open-ended skill**: No test covers it, so keep measuring.
- Treat any pass as a sample, not proof. A finite test covers a sliver of a skill with no edge.
- Use measures with no ceiling. Head to head ratings, where judges pick the better of two answers, keep separating solvers long after percent correct has filled up. So does the size of job a solver can finish alone, which is how a firm judges an apprentice and how METR's time horizons judge AI models.
- Don't read mastery of the bounded part as mastery of the whole. A score on a bounded part only tracks the whole skill while solvers are still learning that part. Once they all have it, the link vanishes, and so do the gains from drilling it.
- Raise the bar or replace the test once scores bunch at the top. England added an A* grade at A level to tell apart the many pupils getting an A. MMLU spread AI models out in 2020 and barely told the best apart by 2024.
- Expect slow gains and wide gaps between solvers. Pay for the best where the task rewards it, since the gap between good and great never closes.

## Correlated with

- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (independent). Paris's bounded skills, like letters, are easy to write down. But riding a bike is tacit and bounded, since once you can balance there is little more to learn. Vocabulary is explicit and open-ended, since every word has a written definition and there is always another word.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A bounded skill runs out of new cases, so a solver who has learnt it meets nothing novel. An open-ended skill keeps serving up cases the solver hasn't met. But a famous poem is familiar ground, and the skill of reading it still has no ceiling.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). A test of the bounded part, used to judge the open-ended whole, is a proxy measure. Teachers then drill the part the test covers, and Paris found that drilling letters gives a quick gain that fades ([Constrained vs unconstrained skills](../frameworks/2005-constrained-vs-unconstrained-skills.md)). The two axes still differ. A chess rating is a direct measure of an open-ended skill.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (independent). This axis asks whether the skill has a ceiling. That one asks whether the payoff does. A thank you note only needs to be warm, though writing well has no ceiling. Setting the dose of a strong drug is worth every extra bit of care, yet the sums behind it are a bounded skill.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). Bounded skills tend to come with an answer key, since the whole set is known. An open-ended skill often has no key, so checking an answer takes another expert.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). Knowing how the pieces move in chess is bounded and playing chess well is open-ended, in one and the same game. An open-ended skill needn't involve a search at all. Research taste has no ceiling and no list of options to check.

## Citations

[1] [Constrained vs unconstrained skills](../frameworks/2005-constrained-vs-unconstrained-skills.md)
