---
type: Axis
title: Private vs accountable
description: "Private: the choice is yours alone (e.g. picking a film). Accountable: you must explain and defend the choice to others (e.g. a bank refusing a loan)."
group: decision
easy_end: Private
hard_end: Accountable
sources:
  - resource: /frameworks/1999-accountability.md
    title: Accountability
  - resource: /frameworks/2017-need-for-interpretability.md
    title: Need for interpretability
---
# Private vs accountable

An axis in the [decision](index.md#the-decision) group.

Is the choice yours alone, or must you explain and defend it to others, such as a regulator, a court or the person affected? A hunch is fine for picking a film. A loan refusal, a court ruling or a medical decision may have to be explained, audited or defended in law, which rules out some methods even when they would work better.

## Actions

**Private**: Use whatever works best.
- Pick the most accurate model, black box or not. Nobody needs to know why.
- Keep light records. Logs are for debugging, not defence.

**Accountable**: Use a method you can explain and keep the records.
- Prefer models you can read. If you must use a black box, be able to give a reason for each decision.
- Log inputs and outputs. You can't defend a decision you can't rebuild.
- Name a person who owns each decision. "The model decided" is not an answer anyone accepts.
- Check the law first. Some decisions, like refusing credit, must come with a reason.

## Correlated with

- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (tension). Know-how you can't put into words is hard to defend in an audit, so accountability pushes towards written rules like Meehl's [formulas](../frameworks/1954-clinical-vs-statistical-prediction.md).
- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (tension). You can only defend a choice if someone can check it.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). [Campbell's law](../frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). A choice that picks winners has to be defended in public ([Post-normal science](../frameworks/1993-post-normal-science.md)).
- [Reversible vs irreversible](reversible-vs-irreversible.md) (logic). One-way doors get the slow, careful process, and with it more scrutiny ([One-way vs two-way doors](../frameworks/2015-one-way-vs-two-way-doors.md)).
- [Complete vs incomplete goal](complete-vs-incomplete-goal.md) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)).
- [Single vs multiple objectives](single-vs-multiple-objectives.md) (study). In Tetlock's hospital study, a manager who spent money on equipment instead of a child's transplant after long thought drew the most outrage of any version ([Taboo trade-offs](../frameworks/1997-taboo-trade-offs.md)). Even weighing a sacred value in public counts against you.
- [Skin in the game vs none](skin-in-the-game-vs-none.md) (independent). Accountable means you must explain the choice, while skin in the game means you pay for it. A judge gives reasons and loses nothing if wrong. A gambler pays for every bad bet and explains nothing.

## Citations

[1] [Accountability](../frameworks/1999-accountability.md)

[2] [Need for interpretability](../frameworks/2017-need-for-interpretability.md)
