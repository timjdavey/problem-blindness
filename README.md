# Problem Blindness


## Motivation

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

## The goal of this project

> "I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail." Abraham Maslow, 1966

The philosopher Abraham Kaplan made the same point two years earlier and called it the [law of the instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument). Most people know it in a shorter form: if all you have is a hammer, everything looks like a nail.

In England a hammer is sometimes called a [Birmingham screwdriver](https://www.urbandictionary.com/define.php?term=birmingham%20screwdriver). The usual story is that the joke goes back generations. Southerners liked to cast the workers of Birmingham as simpletons who would just hammer in any screw you handed them. It's a neat picture of the clumsy amateur next to the skilled expert.

The irony is that this is how most of us treat expertise and problems.

Ever since Adam Smith described his pin factory in 1776, specialisation has slowly come to mean the same thing as expertise. We train people to go deeper into one thing. Then we seek out and promote whoever has the best hammer, so every problem gets treated as a nail.

It's easy to forgive any one expert for leaning on their training. The problem is we've built around that expertise, rewarding that habit because we picture expertise as a single ladder you climb.

AI models seem more subtle and nuanced in their thinking, but they are still expert systems. So a lot of what we know about human experts carries over, and we can use it to work out when to trust these systems at scale.

## What already exists

People have been sorting problems for over a century. The [frameworks folder](frameworks/README.md) lists more than sixty attempts, from Frank Knight's split of risk and uncertainty in 1921 to John Kay and Mervyn King's radical uncertainty in 2020. Each one sees part of the picture, and none sees all of it.

Worse, they use overlapping definitions that don't fit together. "Wicked" means two different things. For [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) a wicked problem is one where people can't agree what the problem even is. For [Hogarth](frameworks/2001-kind-vs-wicked-learning-environments.md) a wicked environment is one where feedback is missing or misleading, so experience teaches you the wrong lesson. [Cynefin's](frameworks/1999-cynefin.md) "complex" domain covers much of the same ground as [deep uncertainty](frameworks/2003-deep-uncertainty.md), yet neither acknowledges the other.

A person can read around these clashes. An LLM or a benchmark can't. If you want either to use these ideas consistently, someone has to write the crosswalk. That is a map between the frameworks which says, with explicit conditions, when one label means the same as another and when it doesn't.

The best place to start is Stuart Russell and Peter Norvig's list of task environment properties in [*Artificial Intelligence: A Modern Approach*](https://aima.cs.berkeley.edu/). It sorts any task on a handful of plain traits. Can you see everything you need? Does the same action always give the same result? Does each choice shape the next one? Each trait is clear and testable, which is why it works so well.

But it was built to design agents, not to judge when to trust one. So it misses four traits that the rest of the frameworks keep coming back to.

- **Sensitivity.** Does a small change at the start lead to a big change at the end? See [sensitive dependence](frameworks/1963-sensitive-dependence-chaos.md) and [Mediocristan vs Extremistan](frameworks/2007-mediocristan-vs-extremistan.md).
- **Feedback.** Do you find out quickly and honestly whether you were right? See [kind vs wicked learning environments](frameworks/2001-kind-vs-wicked-learning-environments.md) and [conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md).
- **Stakes.** Can you undo a mistake, and could one mistake ruin you? See [one-way vs two-way doors](frameworks/2015-one-way-vs-two-way-doors.md) and [fragile, robust and antifragile](frameworks/2012-fragile-robust-and-antifragile.md).
- **Goal clarity.** Do you know what done looks like, and does everyone agree? See [tame vs wicked problems](frameworks/1973-tame-vs-wicked-problems.md) and [well vs ill-structured problems](frameworks/1964-well-vs-ill-structured-problems.md).

## Why it has to be practical

A neat scheme nobody uses is useless. There is already a precedent that tagging tasks this way pays off. In 2025 [METR](https://arxiv.org/abs/2503.14499) scored its tasks for "messiness", meaning how far they sit from a clean test and how close to real work. Even after allowing for how long a task took, a one-point increase in messiness on their scale cut mean success rates by about 8.1%.

That is a single, crude axis, and it already predicts how well a model will do. A richer tagging scheme, checked against real results, could do far more.

This project is designed to rationalise what we know about problems, so that it can be used as a SKILL or at least a reference guide.

