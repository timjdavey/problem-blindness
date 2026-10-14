---
name: Need for interpretability
date: 2017
creators:
  - Finale Doshi-Velez
  - Been Kim
link: https://arxiv.org/abs/1702.08608
summary: >-
  We only need a model to explain itself when the problem can't be fully written down. If the goal is complete and well tested, a score is enough. When parts of the goal are missing, like fairness, safety or the law, an explanation lets a person check what the score leaves out.
---

# Need for interpretability

Nobody asks the machine that sorts letters by postcode to explain itself. If it reads the code right, the job is done. Now picture a model that decides which patients go to hospital. A good score on past cases is not enough, because we also want it to be safe and fair, and we can't write those wants down in full. That gap between what we want and what we can score is the trait this framework sorts on.

In February 2017 Finale Doshi-Velez and Been Kim set this out in a paper called "Towards a rigorous science of interpretable machine learning". They said an explanation isn't needed when mistakes cost little, or when a problem is so well tested that we trust the system, as with ad servers or aircraft collision avoidance. The need comes from a gap in how the problem was written down, which they call incompleteness. It differs from uncertainty, which you can put a number on. A goal that never made it into the score is invisible to it, like fairness or two goals that pull against each other.

The mistake runs both ways. Demanding an explanation from a well tested system can cost accuracy for nothing. Trusting a model you can't see inside because it scores well is worse, when part of the goal never made it into the score. The better response is to ask what the score leaves out. If nothing that matters is missing, trust the score. If safety, fairness or the law is missing, a person needs a way to look inside.

## Examples

**Asthma and pneumonia.** In the mid 1990s a project funded by Cost-Effective HealthCare built models to predict which pneumonia patients would die, so that low-risk patients could be treated at home. Neural nets were the most accurate. But a simpler model made of readable rules learned that patients with asthma were at lower risk. The pattern was real, because asthmatic patients were usually sent straight to intensive care and the care worked. The neural nets had likely learned it too, and who knew what else, so the team used a simpler model they could read and fix. Rich Caruana and colleagues told the story in 2015.

**Amazon's hiring tool.** From 2014 Amazon built a model that rated job applicants from one to five stars. It learned from CVs sent to the company over ten years, most of them from men. It marked down CVs with the word "women's", as in "women's chess club captain", and graduates of two all-women colleges. Engineers edited it to ignore those terms, but it could still find other ways to discriminate. Amazon broke up the team by early 2017, and Reuters reported the story in October 2018. Fairness was never in the score, so only looking inside could show the gap.
