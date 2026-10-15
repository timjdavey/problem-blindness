---
type: Framework
title: No free lunch
description: >-
  Averaged over every possible problem, all search methods do exactly as well as each other. A method only wins by matching the shape of the problem in front of it. There is no best tool in general.
date: 1997
creators:
  - David Wolpert
  - William Macready
sources:
  - resource: https://doi.org/10.1109/4235.585893
---

# No free lunch

In the 1980s and 1990s a lot of hope rested on general purpose search methods. Genetic algorithms copied evolution, and simulated annealing copied the slow cooling of metal. Their fans claimed they did well on a broad range of problems without needing to know much about any of them. David Wolpert and William Macready tested that claim with maths. Their paper came out in 1997 in the first issue of IEEE Transactions on Evolutionary Computation, the field's own journal.

Think of every possible problem as a hidden landscape of good and bad answers. A search method tests points one after another and uses what it finds to choose the next. Wolpert and Macready proved that, averaged over every possible landscape, all methods find good answers at exactly the same rate. Climbing uphill, evolving a population and guessing at random all tie. Any method that does better on some problems must do worse on others. This is called the no free lunch theorem. In 1996 Wolpert had shown the same for machine learning: no learning method beats the others across all possible data.

The law of the instrument is the habit of using the tool you know best on every job. Ashby's [law of requisite variety](1956-law-of-requisite-variety.md) says one tool can't cover many kinds of problem. This theorem goes further. Averaged over every problem, no tool beats any other, so whatever edge a tool has comes from the problems it happens to suit. The mistake is to believe there is a best general method and to keep reaching for it. A team that has done well with one technique starts to see each new problem as another chance to use it. The theorem says the old wins came from the fit between that tool and those problems. The better response is to ask first what you know about the shape of this problem, then pick the method whose built in guesses match it. John Rice set out how to make that choice from data two decades earlier, as the [algorithm selection problem](1976-algorithm-selection-problem.md).

## Examples

**Genetic algorithms.** John Holland set out genetic algorithms in 1975, and David Goldberg's 1989 textbook made them popular. They were often sold as a method that worked well enough on almost anything. The no free lunch paper didn't say they were bad. It said that wherever they did well, the problem suited them, and on other problems some other method would beat them.

**Tables of data.** Deep learning swept image recognition after 2012, and many assumed it would win everywhere. In 2022 Léo Grinsztajn, Edouard Oyallon and Gaël Varoquaux tested it on 45 sets of ordinary table data. Older tree based methods still came out on top for datasets of around 10,000 rows. Neural networks suit images, where nearby pixels relate smoothly. Trees suit tables, where each column means something different and the answer can jump at a threshold.

**Lost keys.** You lose your keys and check your coat pocket, the hall table and the car. This works because your keys aren't placed at random. If someone hid them at random each time, checking the usual places first would be no better than any other order. Your search beats chance only because it fits the way your life is laid out.
