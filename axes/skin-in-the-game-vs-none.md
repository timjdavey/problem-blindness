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
- Trust their judgement. Someone who pays for mistakes learns from them and has the right reasons to care.
- Keep oversight light. Their own loss is the check.

**No skin in the game**: Tie the decision to someone who pays.
- Make the decider share the loss. A broker who keeps part of each loan on their own books cares whether it is repaid.
- Where the decider can't pay, name someone who can. A committee never bears its own losses, and nor does an AI model, so put a named person on the hook.
- Judge the decider on outcomes, not volume. Ask what happened to the people affected, not how many loans were signed.
- Make sure the losses get reported back. A cost that lands on someone else is one the decider never hears about.

## Correlated with

- [Private vs accountable](private-vs-accountable.md) (independent). Accountable means you must explain the choice. Skin in the game means you pay for it. A judge must give reasons and loses nothing if wrong. A gambler pays for every bad bet and explains nothing to anyone.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) (logic). If the cost lands on someone else, news of it reaches the decider late or never, so they can't learn from it.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). The agent is scored on something of their own, like fees or loans signed, and the owner's loss is left out of that score.
- [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md) (logic). It is the other half of the agency problem. This axis is what the other side does after the deal, when the cost lands on someone else. Asymmetric information is what they know before it.

## Citations

[1] [Agency costs](../frameworks/1976-agency-costs.md)
