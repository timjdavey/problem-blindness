---
type: Axis
title: Skin in the game vs none
description: "Skin in the game: whoever makes the call bears the cost if it goes wrong (e.g. a shopkeeper pricing their own stock). No skin in the game: the cost lands on someone else (e.g. a broker paid for each loan whether or not it is repaid)."
group: agent
subgroup: incentives
easy_end: Skin in the game
hard_end: No skin in the game
sources:
  - resource: /frameworks/1976-agency-costs.md
    title: Agency costs
---
# Skin in the game vs none

An axis in the [Incentives](index.md#incentives) set of the [agent](index.md#agent) group.

Does whoever makes the call bear the cost if it goes wrong, or does it land on someone else? A shopkeeper pricing their own stock does. A broker paid for each loan they sign, whether or not it is repaid, does not, and will sign worse loans. Michael Jensen and William Meckling called the cost of this gap an agency cost. An AI model never pays for its own mistakes, so ask whether the team that ships it does.

## Actions

**Skin in the game**: Let the decider decide.
- Trust their judgement. Someone who bears the whole cost of a mistake has every reason to avoid it. [1]
- Keep oversight light. Watching a decider costs money, and when they bear the loss themselves it buys little. [1]

**No skin in the game**: Tie the decision to someone who pays.
- Make the decider share the loss. Whoever gains when things go well should also lose when they go wrong. Hammurabi's laws made a builder whose house fell rebuild it at his own cost. [1]
- Reward outcomes, not volume. US lenders checked borrowers less carefully on loans they could easily sell on, and those loans defaulted 10 to 25% more often. [1]
- Where the decider can't pay, check their work harder or keep the decision yourself. A committee bears little of its own losses, and an AI model bears none. [1]

## Correlated with

- [Private vs accountable](private-vs-accountable.md) (independent). Accountable means you must explain the choice. Skin in the game means you pay for it. A judge must give reasons and loses nothing if wrong. A gambler pays for every bad bet and explains nothing to anyone.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (logic). If the cost lands on someone else, news of it reaches the decider late or never, so they can't learn from it.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). The agent is scored on something of their own, like fees or loans signed, and the owner's loss is left out of that score.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). It is the other half of the agency problem. This axis is what the other side does after the deal, when the cost lands on someone else. Asymmetric information is what they know before it.

## Citations

[1] [Agency costs](../frameworks/1976-agency-costs.md)
