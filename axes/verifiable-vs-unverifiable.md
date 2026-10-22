---
type: Axis
title: Verifiable vs unverifiable
description: "Verifiable: you can check an answer quickly and cheaply before you act on it (e.g. a solved sudoku). Unverifiable: checking an answer costs about as much as finding it, or more, so in practice you can't check it before you act (e.g. a business strategy)."
group: information
subgroup: evidence
easy_end: Verifiable
hard_end: Unverifiable
sources:
  - resource: /frameworks/1964-well-vs-ill-structured-problems.md
    title: Well vs ill-structured problems
  - resource: /frameworks/1971-np-problems.md
    title: NP problems
  - resource: /frameworks/1973-tame-vs-wicked-problems.md
    title: Tame vs wicked problems
---
# Verifiable vs unverifiable

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Once you have an answer, can you check it quickly and cheaply before you act on it? A solved sudoku takes seconds to check. A business strategy has no such check, and the world may take years to grade it. Unverifiable here doesn't mean the answer can never be judged. It means a check before you act would cost about as much as finding the answer, or more, and a check that dear is no check at all. Computer scientists draw the line in the same place. A problem in NP is one whose answers are verifiable fast, however long they take to find. Proving a delivery route is the shortest is not, since no known method checks it much faster than solving the whole problem again. AI labs now train models on tasks with verifiable rewards for the same reason.

## Actions

**Verifiable**: Generate and check.
- Let the model try many answers and keep the one that passes the checker. This is why code with tests and maths with proofs suit models so well.
- Automate the checker and let it gate releases. A cheap check can run on every output.

**Unverifiable**: Build a check before you trust the output.
- Use expert review, spot audits or a slow real world check. Pick the cheapest one that still catches real errors.
- Keep a person signing off until you have one. Without a check, the person is the check.
- Don't let a model grade its own work where nobody else can. It tends to pass its own mistakes.
- Check the checker. Plant known errors and see how many it catches.

## Correlated with

- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). By [Goodhart's law](../frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it, because they learn to pass the check instead of doing the work.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (logic). Feedback is the world checking your answer for you, so an answer that is hard to check often gives slow feedback. They still differ. Verifying is checking one answer before you act on it. Feedback is the world grading you after you act, over many tries. A sudoku is easy to check but teaches you little about the next one. You can't check tomorrow's weather forecast before you act on it, yet the next day grades it clearly.
- [Well vs ill-structured](well-vs-ill-structured.md) (by definition). A test for the answer is part of what Simon means by [well-structured](../frameworks/1964-well-vs-ill-structured-problems.md).
- [Single objective vs trade-offs](single-objective-vs-trade-offs.md) (logic). With no single score there is no simple check.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). You can't claim the best answer if you can't check it.
- [Private vs accountable](private-vs-accountable.md) (tension). You can only defend a choice if someone can check it, so a choice that is hard to verify is hard to account for.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). [NP problems](../frameworks/1971-np-problems.md) are the textbook case of hard to find and easy to check.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings for job applicants against past hires, but fairness was never in the score ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)).
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). One right answer can be checked against a key. Good answers that differ in kind can't share one key, so someone has to judge them.
- [Smooth vs rugged](smooth-vs-rugged.md) (logic). On smooth ground a quick look tells you if an answer is close to good. On rugged ground looking close proves nothing, so you need a check that tests every detail.
- [Curable vs chronic](curable-vs-chronic.md) (logic). With no end there is no final answer to check, only the level so far.
- [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md) (logic). Bounded skills tend to come with an answer key, since the whole set is known. An open-ended skill often has no key, so checking an answer takes another expert.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). A cheap check closes the gap between what the seller knows and what you know. A mechanic's inspection turns a market for lemons back into a market for cars.

## Citations

[1] [Well vs ill-structured problems](../frameworks/1964-well-vs-ill-structured-problems.md)

[2] [NP problems](../frameworks/1971-np-problems.md)

[3] [Tame vs wicked problems](../frameworks/1973-tame-vs-wicked-problems.md)
