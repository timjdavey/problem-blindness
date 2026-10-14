# Problem Blindness

Treating every problem the same way leads to mistakes. People have noticed this again and again over the last hundred years, in economics, town planning, psychology, physics, management and computer science. Each of them came at it from their own field and their own experience, so each gave the idea their own names. The result is a vocabulary that grew up on its own, with dozens of overlapping terms and no map between them.

Because the terms are fuzzy, they also drift. A word gets a precise meaning in one field, then someone borrows it for another and stretches it until it means something else.

"Wicked" is the clearest case. In 1973 Horst Rittel and Melvin Webber, two planners at Berkeley, called a problem [wicked](frameworks/1973-tame-vs-wicked-problems.md) when people can't agree what the problem even is. In 2001 the psychologist Robin Hogarth called a learning environment [wicked](frameworks/2001-kind-vs-wicked-learning-environments.md) when feedback is missing or misleading, so experience teaches you the wrong lesson. The word is the same but the traits are different.

Ergodicity has drifted even further. The word comes from 19th century physics, where a system is ergodic if its average over time matches its average across many copies at one moment. In 2016 Ole Peters and Murray Gell-Mann brought the idea into [economics](frameworks/2016-ergodicity.md) to show why a bet that looks good on average can still make most players poorer. Since then popular writing has stretched "non-ergodic" to mean any risk of ruin. But Peters' own coin game never ruins anyone. It just makes the typical player a little poorer each round.

Elsewhere two names cover the same ground. [Cynefin's](frameworks/1999-cynefin.md) "complex" domain overlaps much of [deep uncertainty](frameworks/2003-deep-uncertainty.md), yet neither mentions the other.

## What this project does

This project pulls those attempts together into one consistent vocabulary. The [frameworks folder](frameworks/README.md) collects more than sixty of them, from Frank Knight's split of risk and uncertainty in 1921 to John Kay and Mervyn King's radical uncertainty in 2020. The [axes](axis.md) pull out the traits underneath. Each axis is a scale with two ends, such as whether you can undo a mistake or whether feedback comes quickly and honestly. Each one lists the frameworks it came from and how it links to the other axes.

The starting point was Stuart Russell and Peter Norvig's list of task environment properties in [*Artificial Intelligence: A Modern Approach*](https://aima.cs.berkeley.edu/). Every trait on it is plain and testable, which is why it works so well. But it was built to design agents, not to judge when to trust one, so the axes add the traits the other frameworks keep coming back to.

The first use is for people. A precise, shared vocabulary gives you something to reason with, and it shows you when two people mean different things by the same word.

The bigger use is for LLMs. A person can read around a clash in meaning. A model mostly can't, and it will happily treat Rittel's wicked and Hogarth's wicked as one idea. Give it a consistent set of axes, with clear conditions for when two labels match, and it has a second brain to reason with. It can place a problem on every axis in far more detail than a person has patience for, then work out which tools fit.

## Why it has to be practical

A neat scheme nobody uses is useless. There is already proof that tagging tasks this way pays off. In 2025 [METR](https://arxiv.org/abs/2503.14499) scored its tasks for "messiness", meaning how far they sit from a clean test and how close to real work. Even after allowing for how long a task took, a one-point increase in messiness on their scale cut mean success rates by about 8.1%.

That is a single, crude axis, and it already predicts how well a model will do. A richer set of axes, checked against real results, could do far more. We want the same thing when building expert systems. Before you hand a task to a model or a person, you should be able to say what shape it is, what kind of expert it needs and how far to trust the answer. The aim is for this project to work as a skill an AI agent can load, or at least as a reference guide.

## How to contribute

This is an open source project and we'd love your help. It is not a finished analysis and never will be. People will keep finding new axes, and there are surely frameworks we have missed. If you spot a gap, a wrong link or a better example, please open a pull request.

A new framework goes in `frameworks/` as a file named by year and title, like `1973-tame-vs-wicked-problems.md`, with the same front matter as the others. Add a row for it to the [frameworks list](frameworks/README.md). A new axis goes in [axis.md](axis.md), with its sources and how it links to the existing axes.

## Why does treating one problem as another matter?

The two stories below show the same mistake. In each, someone used a tool that suited one kind of problem on a problem of a different kind.

### Example 1: Using fast thinking on slow tasks

Cardiologists used to tell a joke at their conventions: the safest place to have a heart attack is at a cardiology convention. Once you stop laughing, the flip side starts to worry you. What happens to patients back home while thousands of the best heart doctors are away?

In 2015 a [study](https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/2038979) looked at ten years of American hospital admissions to find out. Patients did better while the experts were away. At teaching hospitals, 17.5% of high-risk heart failure patients died within a month during the conventions, against 24.8% the rest of the year.

Heart attacks tell you why. During the conventions, high-risk heart attack patients at teaching hospitals were less likely to get a stent put in to open a blocked artery (20.8% against 28.2%), yet no more of them died. The experts weren't worse at their craft. They were worse at deciding when to use it. When they were at work they reached for a risky procedure more often than the doctors who stayed behind, and they saved no more lives for it.

Treating a heart attack is two problems, not one. Doing the procedure rewards the [fast, trained intuition](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow) that years of practice build. Deciding whether to do it is a slow, statistical problem where your gut is the wrong tool. The experts had spent years learning to trust their gut, so they brought the same hammer to both.

### Example 2: Mistaking a neat story for the truth

This example comes from [a talk on judging businesses](https://www.youtube.com/watch?v=KDWfsxfRKXc).

In January you invest in an electronics firm. For six months its sales are so-so. In July it rebrands, and over the next three months sales fall off a cliff. In October a new chief executive arrives. By November things are picking up, and December is the best month of the year.

The lessons look obvious. Rebrands are risky, and a new leader can turn a business round fast.

Now look wider. In July a worldwide supply chain problem hit every firm in the industry, so the rebrand had nothing to do with the fall. The old chief executive wasn't fired. They retired in a handover planned years before. And over the last ten years, sales have picked up every December because the business is seasonal.

Every lesson was wrong. You treated one year of one firm as the whole story, and your gut filled in the causes. A business is tangled and hard to read, so this type of problem needs a long history and a look at everyone else before you learn anything from it.

### Why it keeps happening

> "I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail." Abraham Maslow, 1966

The philosopher Abraham Kaplan made the same point two years earlier and called it the [law of the instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument). Most people know it in a shorter form: if all you have is a hammer, everything looks like a nail.

In England a hammer is sometimes called a [Birmingham screwdriver](https://www.urbandictionary.com/define.php?term=birmingham%20screwdriver). The usual story is that the joke goes back generations. Southerners liked to cast the workers of Birmingham as simpletons who would just hammer in any screw you handed them. It's a neat picture of the clumsy amateur next to the skilled expert.

The irony is that this is how most of us treat expertise and problems.

Ever since Adam Smith described his pin factory in 1776, specialisation has slowly come to mean the same thing as expertise. We train people to go deeper into one thing. Then we seek out and promote whoever has the best hammer, so every problem gets treated as a nail.

It's easy to forgive any one expert for leaning on their training. The problem is we've built around that expertise, rewarding that habit because we picture expertise as a single ladder you climb.

There is a proof that no single hammer can win. In 1997 David Wolpert and William Macready showed that, averaged over every possible problem, all search methods do exactly as well as each other. This is called the [no free lunch](frameworks/1997-no-free-lunch.md) theorem. A method only beats the rest by fitting the shape of the problem in front of it. So the first job is to work out what shape the problem has, and only then pick the tool.

AI models seem more subtle and nuanced in their thinking, but they are still expert systems. So a lot of what we know about human experts carries over, and we can use it to work out when to trust these systems at scale.
