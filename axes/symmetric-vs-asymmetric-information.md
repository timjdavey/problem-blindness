---
type: Axis
title: Symmetric vs asymmetric information
description: "Symmetric information: everyone in the deal sees the same facts (e.g. a game of chess). Asymmetric information: the other side knows things you don't and chooses what reaches you (e.g. buying a used car)."
group: information
subgroup: evidence
easy_end: Symmetric information
hard_end: Asymmetric information
sources:
  - resource: /frameworks/1970-market-for-lemons.md
    title: Market for lemons
  - resource: /frameworks/1976-agency-costs.md
    title: Agency costs
---
# Symmetric vs asymmetric information

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Does the other side of the deal see the same facts you do, or do they know more? In chess both players see the whole board. A used car seller knows whether the car is a lemon and the buyer doesn't. George Akerlof showed what follows. Owners of good cars won't sell at an average price, so the cars on offer are worse than average ([Market for lemons](../frameworks/1970-market-for-lemons.md)). The fact that something reaches you is itself evidence about it. This is called adverse selection. Where a problem sits depends on who you are. The same deal is symmetric for the seller and asymmetric for the buyer.

## Actions

**Symmetric information**: Take what you're told at face value.
- Use the inputs as given. When both sides see the same facts, nobody can pick which cases reach you.
- Train on the cases you have. They are a fair sample of the cases to come.

**Asymmetric information**: Ask why this is on offer to you, and make the other side prove what they know.
- Ask who chose to send each case to the model. A pool of loan applicants or insurance claims is filtered by people who know more than you.
- Check who the model attracts once it is live. A lender that approves more easily than its rivals gets the applicants the rivals turned down, so last year's data no longer describes this year's pool.
- Weight claims by what they cost to fake. Self-reported fields are cheap. A deposit, a warranty or a track record costs a cheat more than an honest party.
- Offer choices that sort people. A cheap plan with a high excess draws the low risk customers, so their choice tells you what they know.
- Make the model say when a claim comes from someone with a stake in the answer. A model reading a CV or a sales listing should flag that the writer chose what to put in it.

## Correlated with

- [General vs local knowledge](general-vs-local-knowledge.md) (logic). Asymmetric information is often local knowledge held by someone with a stake in what you decide. That flips the action. Local knowledge says to treat the person on the ground as the source of truth. Here that person has a reason to shade what they tell you. A shop manager's stock count is local but symmetric, since the manager gains nothing by getting it wrong.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (logic). Opponents hide what they know, as in poker, so the two often come together. But they come apart both ways. Chess is adversarial and both players see the whole board. Harvard's staff weren't aiming at anyone's rule when they left the generous health plan. Each one just picked the plan that suited them, and the plan still collapsed ([Market for lemons](../frameworks/1970-market-for-lemons.md)).
- [Skin in the game vs none](skin-in-the-game-vs-none.md) (logic). These are the two halves of the problem Jensen and Meckling described ([Agency costs](../frameworks/1976-agency-costs.md)). This axis is what the other side knows before the deal. Skin in the game is what they do after it, when the cost lands on someone else. Hammurabi's builder had both. He knew where the shortcuts were hidden, and without the law the owner would have paid if the house fell.
- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (logic). A cheap check closes the gap. A mechanic's inspection turns a market for lemons back into a market for cars.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (logic). The facts exist and someone holds them, so the doubt is reducible in principle. But the person who holds them decides what they cost to find.

## Citations

[1] [Market for lemons](../frameworks/1970-market-for-lemons.md)

[2] [Agency costs](../frameworks/1976-agency-costs.md)
