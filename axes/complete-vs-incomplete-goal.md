# Complete vs incomplete goal

An axis in the [decision](README.md#the-decision) group.

Does the score capture everything you want? A machine that sorts letters by postcode has a complete goal, since reading the code right is the whole job. From 2014 Amazon built a tool that rated job applicants by learning from ten years of past CVs. It marked down CVs with the word "women's", because fairness was never in the score. Finale Doshi-Velez and Been Kim call this gap incompleteness.

**Complete**: Optimise the score.
- Push the metric up. If the metric is the whole job, pushing it up is doing the job.
- Use it to gate releases. A better score means a better model.

**Incomplete**: Watch what the score leaves out.
- List the wants the metric misses. Ask users and affected groups what a high score could still get wrong.
- Track those wants as guardrail metrics. A guardrail is a measure you don't optimise but won't let fall.
- Have people read outputs for harms no number catches. Amazon's CV tool learnt to mark down women because nobody had scored it for fairness.
- Expect the model to find the gaps in the score and exploit them. This is called reward hacking.

**Sources.** [Goodhart's law](../frameworks/1975-goodharts-law.md), [Campbell's law](../frameworks/1976-campbells-law.md), [Need for interpretability](../frameworks/2017-need-for-interpretability.md)

**Correlated with**

- [Easy vs hard to verify](easy-vs-hard-to-verify.md) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings against past hires, but that only checked the score.
- [Well-posed vs ill-posed](well-posed-vs-ill-posed.md) (logic). If you can't state the goal, you can't score all of it. The reverse doesn't hold, since rating CVs looked well posed and the score still left out fairness.
- [Single vs multiple objectives](single-vs-multiple-objectives.md) (bundled). Doshi-Velez and Kim ([Need for interpretability](../frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap. But a car buyer who writes down every want and sets the weights has many objectives and a complete goal.
- [Shared vs contested values](shared-vs-contested-values.md) (logic). When people disagree on what a good result is, any one score takes a side and leaves the other wants out.
- [Private vs accountable](private-vs-accountable.md) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score.
- [Inert vs reflexive](inert-vs-reflexive.md) (study). By [Goodhart's law](../frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed. [Campbell's law](../frameworks/1976-campbells-law.md) adds that teachers drill the test and drop the parts of the subject it doesn't cover.
- [Commensurable vs incommensurable values](commensurable-vs-incommensurable-values.md) (logic). A single score has to price everything, so a sacred value is left out or priced where nobody can see.
- [Even vs lopsided errors](even-vs-lopsided-errors.md) (logic). Plain accuracy counts a missed cancer and a false scare as the same mistake.
- [Skin in the game vs none](skin-in-the-game-vs-none.md) (logic). An agent scored on fees or loans signed has a score that leaves out the owner's loss.
