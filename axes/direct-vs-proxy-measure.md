---
type: Axis
title: Direct vs proxy measure
aliases:
  - Complete vs incomplete goal
  - Complete vs incomplete score
description: "Direct measure: the thing you measure is everything you want (e.g. sorting letters by postcode). Proxy measure: the thing you measure stands in for what you want and leaves out goals that are hard to write down (e.g. a hiring score learnt from past CVs, which says nothing about fairness)."
group: performance
subgroup: goal
easy_end: Direct measure
hard_end: Proxy measure
sources:
  - resource: /frameworks/1975-goodharts-law.md
    title: Goodhart's law
  - resource: /frameworks/1976-campbells-law.md
    title: Campbell's law
  - resource: /frameworks/2017-need-for-interpretability.md
    title: Need for interpretability
  - resource: https://arxiv.org/abs/1606.06565
    title: Concrete problems in AI safety (Amodei, 2016)
---
# Direct vs proxy measure

An axis in the [Goal](index.md#goal) set of the [performance](index.md#performance) group.

Is the thing you measure the thing you want, or only a stand-in for it that leaves out goals, such as fairness, that are hard to write down? A machine that sorts letters by postcode has a direct measure, since reading the code right is the whole job. From 2014 Amazon built a tool that rated job applicants by learning from CVs sent to the company over ten years. Most came from men, so it learnt to mark down CVs with the word "women's". Nothing in the score said that was wrong, because fairness was never in it. A measure that stands in for what you want is called a proxy. Finale Doshi-Velez and Been Kim call the gap between the two incompleteness. The goal in your head may be whole. It is the score that leaves things out.

## Actions

**Direct measure**: Optimise the score.
- Trust the score and push it up. When nothing that matters is missing from it, a better score is better work, whoever or whatever did it. A sorting office that reads more postcodes right is simply doing better. [3]
- Don't ask for an explanation as well. Demanding one from a well tested system can cost accuracy for nothing. [3]

**Proxy measure**: Watch what the score leaves out.
- List the wants the score misses. Ask the people it serves and the people it affects what a high score could still get wrong. [3]
- Track those wants as guardrails. A guardrail is a measure you don't push up but won't let fall. A call centre timed on call length should still check that callers get their problem solved. [2]
- Keep the number you reward apart from the number you learn from. Once a number becomes a target it stops telling you what is going on, so change targets before people learn to game them. [1]
- Check the work itself for harms the score can't see. Amazon's CV tool learnt to mark down CVs with the word "women's", and nothing in its score measured fairness. Editing out such terms could not rule out other ways to discriminate. [3]
- Expect whoever is scored to find the gaps and use them. Wells Fargo staff pushed to sell more products opened about two million accounts customers never asked for. When a model does the same, it is called reward hacking. [1, 4]

## Correlated with

- [Verifiable vs unverifiable](verifiable-vs-unverifiable.md) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings against past hires, but that only checked the score.
- [Well vs ill-structured](well-vs-ill-structured.md) (logic). If you can't state the goal, you can't score all of it. The reverse doesn't hold, since rating CVs looked well structured and the score still left out fairness.
- [Single objective vs trade-offs](single-objective-vs-trade-offs.md) (bundled). Doshi-Velez and Kim ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap. But a car buyer who writes down every want and sets the weights has many objectives and a direct measure. Where some wants are sacred, a single score has to leave them out or price them where nobody can see.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). When people disagree on what a good result is, any one score takes a side and leaves the other wants out.
- [Private vs accountable](private-vs-accountable.md) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score.
- [Neutral vs adversarial](neutral-vs-adversarial.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed. [Campbell's law](../frameworks/1976-campbells-law.md) adds that teachers drill the test and drop the parts of the subject it doesn't cover.
- [Even vs lopsided mistakes](even-vs-lopsided-mistakes.md) (logic). Plain accuracy counts a missed cancer and a false scare as the same mistake.
- [Standalone vs sequential](standalone-vs-sequential.md) (logic). Some wants only show up once people see a draft, so a measure that looked direct turns out to be a proxy as you go. Chris Argyris and Donald Schön called it double-loop learning when you question the goal itself as well as how you reach it ([Single vs double-loop learning](../frameworks/1978-single-vs-double-loop-learning.md)).
- [Skin in the game vs none](skin-in-the-game-vs-none.md) (logic). An agent scored on fees or loans signed has a score that leaves out the owner's loss.
- [Winnable vs no-win](winnable-vs-no-win.md) (logic). A score measured from zero makes every no-win outcome look like failure. What would have happened anyway has to be part of the score.
- [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md) (logic). A test of a bounded part, used to judge an open-ended whole, is a proxy measure. Scott Paris found that drilling letters gives young readers a quick gain that fades. But a chess rating is a direct measure of an open-ended skill.

## Citations

[1] [Goodhart's law](../frameworks/1975-goodharts-law.md)

[2] [Campbell's law](../frameworks/1976-campbells-law.md)

[3] [Need for interpretability](../frameworks/2017-need-for-interpretability.md)

[4] [Concrete problems in AI safety (Amodei, 2016)](https://arxiv.org/abs/1606.06565)
