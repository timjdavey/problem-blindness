---
type: Overview
title: Motivation
description: Why this project exists. Experts bring the same hammer to every problem, and people and AI agents both need a shared way to name the kind of problem in front of them.
---
# Motivation

> "If all you have is a hammer, everything looks like a nail." [Maslow's law of the instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument)

This came from the 19th century joke of calling a hammer a [Birmingham screwdriver](https://en.wikipedia.org/wiki/Brummagem). It neatly frames the perennial battle between the ignorant and the skilled expert.

The ironic thing is that this is exactly how most of us treat expertise and skills. You're smart or not. High IQ or low. Skilled or not. Since Adam Smith's pin factory, _specialisation_ has slowly become synonymous with _expertise_. So we research, seek out and promote a single type of expert hammer to solve all our problem nails.

We can all _feel_ there's a difference between types of expertise and skills, but it's really hard to pin down exactly why or how.

![Comic smug pilots by Will McPhail](https://i.snap.as/ukU760IM.jpeg) _[By artist Will McPhail for the New Yorker](https://x.com/willmcphail/status/815899174474567680)_


## Problem blindness

There's an old joke that heart doctors used to tell while hobnobbing at conventions:

> Where's the safest place to have a heart attack? At a cardiology convention!

But if this is true, what happens to the patients left behind while the experts are away? In 2015 [a study](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2038979) set out to find out. As the [journal's editor](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2038976) put it:

> Contrary to the a priori hypothesis that care would be compromised by so many of the top cardiologists being gone, they find that adjusted mortality for high-risk heart failure and cardiac arrest **is lower** at teaching hospitals during the cardiology meetings than during the rest of the year...

Strangely, it turns out that it's _not more_ risky to be treated by the doctors who stayed behind. It's actually **less** risky.

What's going on here? It would be easy to assume it was some confounding factor. Maybe the conventions fall at a time of year when people are less active, so they strain their hearts less. But the analysis was robust and ruled out the usual suspects. It compared the meeting days with the same days three weeks before and after, and it used non-teaching hospitals, where few doctors leave for the meetings, as a control group. Instead the smoking gun was that "high-risk patients with AMI admitted to teaching hospitals during meetings were less likely to receive PCI, without any mortality effect."

What's happening is that two very distinct types of problem are being treated as the same. First there's the diagnosis, deciding what to do. Second there's the physical act of the procedure.

The failure didn't come from a poorly done procedure. It came from the experienced experts tending to overprescribe PCI, a procedure to unblock the heart's arteries that carries real risks of its own. The doctors left behind were more cautious and deliberate in what they prescribed, and fewer stents went in with no more deaths. So, ironically, the patients did better overall, even though the most skilled hands were away.

What we find here is that these doctors are trained to be incredibly good at fast thinking (System 1), so they can perform in the operating room. The [trouble is](https://www.edge.org/conversation/daniel_kahneman-the-marvels-and-the-flaws-of-intuitive-thinking-edge-master-class-2011):

> [Fast brain thinking] is a mechanism that takes whatever information is available and makes the best possible story out of the information currently available, and tells you very little about information it doesn't have. So what you get **are people jumping to conclusions**... That will very often create a flaw. It will create overconfidence.

All their experience in the operating room reinforces the habit of trusting their fast-brain intuition. That is fine and correct when doing the procedure, but diagnosis is a System 2, slow-brain job. It requires calculation, deep thought and reliance on industry statistics. You should not trust your intuition.

Viewed through a systems lens, it requires a different _sort of thinking_, because it's a different _type of problem_.


## Unreliable feedback

Fast and slow problems are probably the most famous split, but there are countless others.

Another is whether experience teaches you the right lesson at all. The psychologist Robin Hogarth tells the story, first written down by the physician Lewis Thomas, of an early 20th century New York doctor who was famous for spotting typhoid before any symptoms showed. He felt each patient's tongue with his bare hands, and his predictions kept coming true. They came true because he was carrying typhoid from patient to patient.

Every hit made him surer of his skill. Hogarth called this a [wicked learning environment](frameworks/2001-kind-vs-wicked-learning-environments.md), where feedback is missing, late or misleading, so the more experience you have, the more confidently wrong you can become. Darts is the opposite. Each throw lands a second later and shows you exactly how far off you were. The two call for completely different kinds of expertise, even though both look like "getting better with practice".


## Attempts to make sense of this

I went into this project with the naive assumption that I'd be able to discover a simple, legible system for describing all the different types of problems we have. I was extremely wrong, and humbled.

However, it turns out I wasn't the first person to make this mistake. There is a long history of frameworks like [Cynefin](frameworks/1999-cynefin.md), the [Stacey matrix](frameworks/1996-stacey-matrix.md), [VUCA](frameworks/1987-vuca.md) and Russell and Norvig's [task environment properties](frameworks/1995-task-environment-properties.md), along with [more than eighty others](frameworks/index.md). Each describes something real about the differences between problems, but each also misses the whole picture, as each is grounded in the problems of the industry it was born out of.

Worse, many people have stretched the definitions to project their own industries' interpretations onto them. For example, [wicked problems](frameworks/1973-tame-vs-wicked-problems.md) were first defined by Horst Rittel and Melvin Webber in 1973 to mean planning problems where people can't agree on what the problem even is, there's no point where it's finished, and every attempt leaves a mark that can't be undone. Robin Hogarth later borrowed the word in 2001 to mean a [learning environment](frameworks/2001-kind-vs-wicked-learning-environments.md) where feedback is missing or misleading. Simon Sinek did a similar thing with [infinite games](frameworks/1986-finite-and-infinite-games.md). James Carse meant a game played not to win but to keep the play going. Sinek's book [*The Infinite Game*](https://simonsinek.com/books/the-infinite-game/) stretched it to mean thinking long term in business.


## Where we are headed

So the job has switched to pulling out the independent axes and creating rigour around the definitions as a whole. Firstly, so that definitions don't get co-opted or drift, as this is hugely confusing for people and devastating for AI training. Secondly, so that we can do meta-studies and collate evidence about how to behave, and how to build expertise, when dealing with each type of axis.

This way we can consistently label the jobs that people and agents do. Then we can robustly show that cardiologists need different methods and different sorts of expertise to make a diagnosis than to carry out the procedure.

This becomes all the more important as we start shifting work to AI agents. There will undoubtedly be top models that outperform across all axes. This matters because, to be effective, an agent needs to get many jobs done to complete a task, likely featuring many different axis types. Trusting an agent to complete jobs across that spectrum is huge. **But** that means we need to be testing for it. We need to make sure we're actively benchmarking across these axes, and ideally doing meta-analysis to make sure there's no cocktail effect.

Also, although it would be nice to freely offload all tasks to frontier models, in practice this doesn't make sense, as there's always a trade-off with speed, price, energy and so on. This is why we're seeing a resurgence of specialist models like [Jev](https://typesafe.ai) and [Timestral](https://mistral.ai/news/timestral).

Being able to accurately map the expertise of these specialists to their performance against problem types will give us all much greater confidence.


## How this relates to skills and training

This matters in education. For instance, children's first exposure to maths is mental arithmetic and times tables. This is System 1 rote learning, and a completely different skill set from the slow, deliberate System 2 thinking involved in algebra. Many kids start their academic journey thinking they are terrible at maths, when actually they just have poor working memories, which are common in engineers.

Worse still, arithmetic has been solved by calculators, and algebra has been solved by Mathematica and now LLMs. The real skills left are making sense of proofs and asking good questions, both of which sit on completely different axes from what we teach in school.

I truly hope we can urgently solve our problem blindness, as it will make the journey of integrating agents alongside humans a much easier one.
