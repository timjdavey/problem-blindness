---
type: Axis
title: Complete vs incomplete score
description: "Complete: the thing you measure captures everything you want (e.g. sorting letters by postcode). Incomplete: some goals are left out because they are hard to write down (e.g. fairness in hiring)."
group: decision
subgroup: goal
easy_end: Complete
hard_end: Incomplete
sources:
  - resource: /frameworks/1975-goodharts-law.md
    title: Goodhart's law
  - resource: /frameworks/1976-campbells-law.md
    title: Campbell's law
  - resource: /frameworks/2017-need-for-interpretability.md
    title: Need for interpretability
---
# Complete vs incomplete score

An axis in the [Goal](index.md#goal) set of the [decision](index.md#the-decision) group.

Does the thing you measure capture everything you want, or are some goals, such as fairness, left out because they are hard to write down? A machine that sorts letters by postcode has a complete score, since reading the code right is the whole job. From 2014 Amazon built a tool that rated job applicants by learning from CVs sent to the company over ten years. Most came from men, so it learnt to mark down CVs with the word "women's". Nothing in the score said that was wrong, because fairness was never in it. Finale Doshi-Velez and Been Kim call this gap incompleteness. The goal in your head may be whole. It is the score that leaves things out.

## Actions

**Complete**: Optimise the score.
- Push the metric up. If the metric is the whole job, pushing it up is doing the job.
- Use it to gate releases. A better score means a better model.

**Incomplete**: Watch what the score leaves out.
- List the wants the metric misses. Ask users and affected groups what a high score could still get wrong.
- Track those wants as guardrail metrics. A guardrail is a measure you don't optimise but won't let fall.
- Have people read outputs for harms no number catches. Amazon's engineers only found the CV tool marking down women by looking inside it, since no score measured fairness.
- Expect the model to find the gaps in the score and exploit them. This is called reward hacking.

## Correlated with

- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings against past hires, but that only checked the score.
- [Well vs ill-structured](well-vs-ill-structured.md) (logic). If you can't state the goal, you can't score all of it. The reverse doesn't hold, since rating CVs looked well structured and the score still left out fairness.
- [Single vs multiple objectives](single-vs-multiple-objectives.md) (bundled). Doshi-Velez and Kim ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap. But a car buyer who writes down every want and sets the weights has many objectives and a complete score. Where some wants are sacred, a single score has to leave them out or price them where nobody can see.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). When people disagree on what a good result is, any one score takes a side and leaves the other wants out.
- [Private vs accountable](private-vs-accountable.md) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed. [Campbell's law](../frameworks/1976-campbells-law.md) adds that teachers drill the test and drop the parts of the subject it doesn't cover.
- [Even vs lopsided errors](even-vs-lopsided-errors.md) (logic). Plain accuracy counts a missed cancer and a false scare as the same mistake.
- [Standalone vs sequential](standalone-vs-sequential.md) (logic). Some wants only show up once people see a draft, so a goal that looked complete fills out as you go. Chris Argyris and Donald Schön called it double-loop learning when you question the goal itself, not just how you reach it ([Single vs double-loop learning](../frameworks/1978-single-vs-double-loop-learning.md)).
- [Skin in the game vs none](skin-in-the-game-vs-none.md) (logic). An agent scored on fees or loans signed has a score that leaves out the owner's loss.

## Citations

[1] [Goodhart's law](../frameworks/1975-goodharts-law.md)

[2] [Campbell's law](../frameworks/1976-campbells-law.md)

[3] [Need for interpretability](../frameworks/2017-need-for-interpretability.md)
