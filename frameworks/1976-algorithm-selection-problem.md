---
type: Framework
title: Algorithm selection problem
description: >-
  When many methods could solve a problem, the best one often changes from case to case. If you can measure a few features of a case before you start, you can learn which method to pick for it. The method with the best average is often not the best choice for any one case.
date: 1976
creators:
  - John R. Rice
sources:
  - resource: https://doi.org/10.1016/S0065-2458(08)60520-3
---

# Algorithm selection problem

John Rice was a mathematician who joined Purdue University in 1964, two years after it opened the first computer science department in the United States. He went on to head it. His own work was on numerical methods, such as ways to work out the area under a curve. There were dozens of these routines, and none was best on every curve. So in 1976 he asked a plain question in a chapter of *Advances in Computers*: given a problem, how do you choose which method to run on it?

Rice broke the question into four parts. There is the set of problems you might face. There are features you can measure on a problem before you solve it, like how wiggly a curve is or how large a puzzle is. There is the set of methods you could run. And there is a score for how well each method did. The job is to find a rule that goes from the features to the method. He worked the idea through on area routines and on how a computer decides which job to run next. The trait this sorts on is whether the best method changes from case to case in a way you can see coming.

This is the law of the instrument turned into a question you can answer with data. [No free lunch](1997-no-free-lunch.md) says no method wins on every problem, and the [law of requisite variety](1956-law-of-requisite-variety.md) says one tool can't cover many kinds of case. Rice says what to do about it. The mistake is to rank methods by their average score and then use the winner everywhere. That winner is called the single best solver. The better response is to measure each case first and pick the method its features point to. Then check how far the single best solver falls short of picking the best method for every case. If the gap is small, one tool is fine and you can stop. If it is large, it pays to learn the rule.

This framework feeds the [Clustered vs scattered runs](../axes/clustered-vs-scattered-runs.md) axis.

## Examples

**SATzilla.** A SAT puzzle asks whether there is a way to set a long list of true or false switches so that every rule holds. Many solvers exist, and each is fast on some puzzles and hopeless on others. Lin Xu, Frank Hutter, Holger Hoos and Kevin Leyton-Brown at the University of British Columbia built SATzilla, which runs no clever search of its own. It measures cheap features of each puzzle, predicts how long each solver would take and hands the puzzle to the one it expects to be fastest. At the 2007 SAT Competition it won three gold medals, one silver and one bronze, beating the solvers it was built from.

**The M4 forecasting competition.** In 2018 the M4 competition asked teams to forecast 100,000 time series, from company sales to population counts. Pablo Montero-Manso, George Athanasopoulos, Rob Hyndman and Thiyanga Talagala didn't pick one forecasting method. They measured features of each series, such as how seasonal and how noisy it was, and learned how much weight to give each of nine methods for a series of that kind. Their entry came second of the 49 teams that sent in valid forecasts.

**Routing questions between AI models.** A large AI model is better than a small one but costs far more to run, and most questions don't need it. In 2024 a team at LMSYS trained a router that reads each question and sends it to GPT-4 or to a cheaper model. On one test set it cut costs by over 85% compared with sending everything to GPT-4, and kept 95% of GPT-4's score.
