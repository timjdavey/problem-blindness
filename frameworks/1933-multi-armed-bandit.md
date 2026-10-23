---
type: Framework
title: Multi-armed bandit
description: >-
  You choose again and again between options with noisy, unknown payoffs. Each choice pays out and also teaches you something. The problem is how to balance trying new options against using the best one so far.
date: 1933
cited_date: 1952
creators:
  - William R. Thompson
  - Herbert Robbins
sources:
  - resource: https://doi.org/10.1093/biomet/25.3-4.285
    title: On the likelihood that one unknown probability exceeds another in view of the evidence of two samples
  - resource: https://doi.org/10.1090/S0002-9904-1952-09620-8
    title: Some aspects of the sequential design of experiments
  - resource: https://en.wikipedia.org/wiki/Multi-armed_bandit
    title: Multi-armed bandit (Wikipedia)
  - resource: https://arxiv.org/abs/1707.02038
    title: A tutorial on Thompson sampling
---
# Multi-armed bandit

**You choose again and again between options with noisy, unknown payoffs. Each choice pays out and also teaches you something.**

1933 (1952) · William R. Thompson and Herbert Robbins · [Original paper](https://doi.org/10.1093/biomet/25.3-4.285) · Feeds 2 axes

## The idea

Picture a row of slot machines, each paying out at a different rate that you can't see. You have a hundred coins. Every pull earns you something, and it also tells you a little about that machine. If you only play the first machine that pays well, you may never find a better one. If you keep trying every machine, you waste coins on the bad ones. A slot machine is nicknamed a one-armed bandit, so this is called the multi-armed bandit problem.

William Thompson posed it in 1933, thinking about which of two medical treatments to give the next patient. Herbert Robbins set it out as a general problem in 1952. The trait it picks out is that you learn and earn from the same choices, over and over. You can't stop to study first and act later. Every test has a cost, and every safe choice has a cost in what you don't learn. Balancing the two is called the trade off between exploration and exploitation.

## What goes wrong

People get this wrong in two ways. Some treat it as a one-off choice. They pick what looks best today and never test again, so they lock in an early guess that was mostly luck. Others treat it as pure research. They run a long fixed experiment and keep sending half their users to the option that is plainly losing, because the test plan says so.

## What to do instead

A bandit problem needs you to shift towards what works while still checking now and then.

## Examples

### Your local restaurants

You moved to a new town and found a curry house you like in the first month. You could go there every Friday for ten years. But you have only tried four places, so the odds are good that a better one exists. The usual fix is to go back to your favourite most weeks and try somewhere new now and then.

### Thompson's patients

In a classic drug trial half the patients get each treatment until the end, even once one is clearly ahead. Thompson's idea was to pick each new patient's treatment at random, with each treatment's chance of being picked equal to the chance that it is the better one. More patients get the better drug while the trial is still running. His method is now called Thompson sampling.

### Website tests

A shop testing two versions of a checkout page can split traffic fifty fifty for a month. That treats the question as research and pays for it in lost sales. A bandit approach sends more traffic to the page that is winning as the evidence builds. It still keeps a little traffic on the other page in case the early lead was noise.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Standalone vs sequential](../axes/standalone-vs-sequential.md) | Actions › Options | You learn and earn from the same choices over and over, so each pull shapes the next |
| [Interventional vs observational](../axes/interventional-vs-observational.md) | Information › Evidence | You set the cause yourself, and can shift towards the winner while the test still runs |

## Further reading

- [On the likelihood that one unknown probability exceeds another in view of the evidence of two samples](https://doi.org/10.1093/biomet/25.3-4.285), William R. Thompson, *Biometrika*, 1933. The original paper, which asks which of two treatments to give the next patient.
- [Some aspects of the sequential design of experiments](https://doi.org/10.1090/S0002-9904-1952-09620-8), Herbert Robbins, *Bulletin of the American Mathematical Society*, 1952. Sets out the bandit as a general problem of running experiments one step at a time.
- [Multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) on Wikipedia.
- [A tutorial on Thompson sampling](https://arxiv.org/abs/1707.02038), Daniel Russo, Benjamin Van Roy, Abbas Kazerouni, Ian Osband and Zheng Wen, *Foundations and Trends in Machine Learning*, 2018. A modern guide to Thompson's method, free on arXiv.
