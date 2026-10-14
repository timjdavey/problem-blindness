---
type: Framework
title: Portfolio selection
description: >-
  The risk of a portfolio depends on how its parts move together, not just on how risky each one is. Spreading your stake only cuts risk when the bets don't all fail at once. Bets that rise and fall together are one bet in disguise.
date: 1952
creators:
  - Harry Markowitz
sources:
  - resource: https://doi.org/10.2307/2975974
---

# Portfolio selection

Everyone knows not to put all your eggs in one basket. In 1952 Harry Markowitz, then a graduate student at Chicago, showed in the Journal of Finance that the advice is only half right. What matters is not how many baskets you use but whether they all fall when you trip. He won a Nobel prize for the idea in 1990.

Before Markowitz, investors judged each share on its own and bought the best ones. He pointed out that the risk of the whole depends on how the parts move together. Two shares that each swing wildly can make a steady pair if one tends to rise when the other falls. Two safe looking shares can make a risky pair if they always fall together. So the risk of a portfolio is not the sum of the risks of its parts. With many holdings, most of the risk that is left is the part they all share, and no amount of spreading removes it.

The mistake is to count bets instead of checking how far they are independent. A hundred loans to people in one town are close to one loan, because one factory closing hits them all. Spreading only works when the bets can fail on their own.

## Examples

**The 1/N portfolio.** Markowitz gave a formula for the best mix of shares, but it needs good estimates of how every pair moves together, and those are hard to get. In 2009 a study found that splitting money equally across N assets beat 14 optimising models, including his ([Ecological rationality](1999-ecological-rationality.md)). Markowitz later told a reporter that he split his own retirement money half and half between shares and bonds, so he would regret it less whichever way markets went.

**Mortgage bonds in 2008.** Banks bundled thousands of American home loans into bonds and sold slices of them rated as safe as government debt. The ratings assumed that homeowners in different states would rarely stop paying at the same time. When house prices fell across the whole country at once, the loans failed together. The bonds looked spread across thousands of bets, but they were close to one bet on American house prices.

**Best of n with one model.** A common way to get a better answer from an LLM is to draw several and keep the one most of them agree on. That works when the errors are random. But samples from one model share its blind spots, so on a question it misreads, all ten answers can agree and all ten can be wrong. Answers from different models, or checks against an outside test, fail together less often.
