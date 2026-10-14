---
type: Axis
title: Easy vs hard to verify
description: Once you have an answer, can you check it quickly and cheaply, or might it take years to know if it was right?
group: decision
easy_end: Easy
hard_end: Hard
sources:
  - resource: /frameworks/1964-well-vs-ill-structured-problems.md
    title: Well vs ill-structured problems
  - resource: /frameworks/1971-np-problems.md
    title: NP problems
  - resource: /frameworks/1973-tame-vs-wicked-problems.md
    title: Tame vs wicked problems
---
# Easy vs hard to verify

An axis in the [decision](index.md#the-decision) group.

Once you have an answer, can you check it quickly and cheaply, or might it take years to know if it was right? A solved sudoku takes seconds to check. A business strategy or a diagnosis may take years to prove right or wrong.

## Actions

**Easy**: Generate and check.
- Let the model try many answers and keep the one that passes the checker. This is why code with tests and maths with proofs suit models so well.
- Automate the checker and let it gate releases. A cheap check can run on every output.

**Hard**: Build a check before you trust the output.
- Use expert review, spot audits or a slow real world check. Pick the cheapest one that still catches real errors.
- Keep a person signing off until you have one. Without a check, the person is the check.
- Don't let a model grade its own work where nobody else can. It tends to pass its own mistakes.
- Check the checker. Plant known errors and see how many it catches.

## Correlated with

- [Inert vs reflexive](inert-vs-reflexive.md) (logic). By [Goodhart's law](../frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) (logic). Feedback is the world checking your answer for you, so a hard check means slow feedback. They still differ. Verifying is checking one answer before you act on it. Feedback is the world grading you after you act, over many tries. A sudoku is easy to check but teaches you little about the next one. A doctor can't prove a diagnosis on the day, yet learns over years which calls turned out right.
- [Well-posed vs ill-posed](well-posed-vs-ill-posed.md) (by definition). A test for the answer is part of what Simon means by [well-structured](../frameworks/1964-well-vs-ill-structured-problems.md).
- [Single vs multiple objectives](single-vs-multiple-objectives.md) (logic). With no single score there is no simple check.
- [Satisficing vs optimising](satisficing-vs-optimising.md) (tension). You can't claim the best answer if you can't check it.
- [Private vs accountable](private-vs-accountable.md) (tension). You can only defend a choice if someone can check it, so a choice that is hard to verify is hard to account for.
- [Tractable vs intractable search](tractable-vs-intractable-search.md) (independent). [NP problems](../frameworks/1971-np-problems.md) are the textbook case of hard to find and easy to check.
- [Complete vs incomplete goal](complete-vs-incomplete-goal.md) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings for job applicants against past hires, but fairness was never in the score ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)).
- [Convergent vs divergent](convergent-vs-divergent.md) (logic). One right answer can be checked against a key. Many good answers need someone to judge them.

## Citations

[1] [Well vs ill-structured problems](../frameworks/1964-well-vs-ill-structured-problems.md)

[2] [NP problems](../frameworks/1971-np-problems.md)

[3] [Tame vs wicked problems](../frameworks/1973-tame-vs-wicked-problems.md)
