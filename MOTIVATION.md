---
type: Overview
title: Motivation
description: Why this project exists. Experts bring the same hammer to every problem, and people and AI agents both need a shared way to name the kind of problem in front of them.
---
# Motivation

> "If all you have is a hammer, everything looks like a nail." [Maslow's law of the instrument](https://en.wikipedia.org/wiki/Law_of_the_instrument)

This came from the 19th century joke of calling a hammer a [Birmingham screwdriver](https://en.wikipedia.org/wiki/Brummagem). It neatly frames the perennial snobbery between the ignorant and skilled.

The ironic thing is that this is exactly how most of us treat expertise itself. We coarse grain into you're smart or not. Have a high IQ or not. Skilled or not. Since Adam Smith's pin factory, _specialisation_ has slowly become synonymous with _expertise_. So we research, find and promote a single type of expert hammer to solve all our problem nails.

We can all _feel_ there's a difference between types of expertise and skills, but it's really hard to pin down exactly why or how they differ.

![Comic smug pilots by Will McPhail](https://i.snap.as/ukU760IM.jpeg) _[By artist Will McPhail for the New Yorker](https://x.com/willmcphail/status/815899174474567680)_


## Problem blindness

There's an old joke that heart doctors used to tell while hobnobbing at conventions:

> Where's the safest place to have a heart attack? At a cardiology convention!

But if this is true, is this ethical? In 2015 [a study](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2038979) set out to find out and [they found](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2038976):

> Contrary to the a priori hypothesis that care would be compromised by so many of the top cardiologists being gone, they find that adjusted mortality for high-risk heart failure and cardiac arrest **is lower** at teaching hospitals during the cardiology meetings than during the rest of the year...

So contrary to what anyone would have guessed but it turns out that it's **less** risky to be treated during a convention!

How can this be? It would be easy to assume it was some confounding factor. Maybe the conventions fall at a time of year when people are less active, so they strain their hearts less. But the analysis was robust and ruled out the usual suspects. It compared the meeting days with the same days three weeks before and after, and it used non-teaching hospitals, where few doctors leave for the meetings, as a control group.

Instead the smoking gun was that "high-risk patients with AMI admitted to teaching hospitals during meetings were less likely to receive PCI, without any mortality effect." Meaning the failure didn't come from a poorly done procedure. It came from the experienced experts tending to _overprescribe_ stents which are a specific type of procedure to unblock the heart's arteries that carries a real and high set of risks of its own. Meanwhile the doctors left behind were more cautious and deliberate in what they prescribed, and fewer stents went in with no more deaths. So, ironically, the patients did better overall, even though the most skilled hands were away.

What we find here is that these doctors are trained to be incredibly good at fast thinking (System 1), so they can perform in the operating room. The [trouble is](https://www.edge.org/conversation/daniel_kahneman-the-marvels-and-the-flaws-of-intuitive-thinking-edge-master-class-2011):

> [Fast brain thinking] is a mechanism that takes whatever information is available and makes the best possible story out of the information currently available, and tells you very little about information it doesn't have. So what you get **are people jumping to conclusions**... That will very often create a flaw. It will create overconfidence.

All their experience in the operating room reinforces the habit of trusting their fast-brain intuition. That is fine and correct when doing the procedure, but diagnosis is a System 2, slow-brain job. It requires calculation, deep thought and reliance on industry statistics. You should not trust your intuition.

What's happening is that two very distinct types of problem are being treated as the same. First there's the diagnosis, deciding what to do. Second there's the physical act of the procedure.

Viewed through a systems lens, there are two very distinct _types of problems_, requiring very different _sorts of thinking_, which were treated as the same.


## Fat tails

Fast and slow problems are probably the most famous split, but there are countless others.

Another is whether the average tells you anything at all. In 1994 the bond trader John Meriwether set up a hedge fund called [Long-Term Capital Management](https://www.federalreservehistory.org/essays/ltcm-near-failure). His partners included Myron Scholes and Robert Merton, who won the Nobel prize in economics in 1997 for their work on pricing options. The fund made 43% in 1995 and 41% in 1996, borrowing about $30 for every $1 it held. Then in August 1998 Russia stopped paying its debts. Markets moved in ways the models said should almost never happen, and the fund lost 44% of its value in that month alone. The Federal Reserve had to bring 14 banks together to put in $3.6 billion before its collapse dragged others down with it.

The models weren't sloppy. They assumed prices behave like people's heights, where results stay close to the average and no single day can move the total much. Nassim Taleb calls this world [Mediocristan](frameworks/2007-mediocristan-vs-extremistan.md). Markets live in Extremistan instead, where one day can outweigh years of calm. We call this [thin vs fat tails](axes/thin-vs-fat-tails.md). In a thin-tailed world you trust the average and squeeze out every edge. In a fat-tailed one you plan for the worst case and make sure no single bet can wipe you out, however good the odds look. Four calm years only made the partners surer, because the event that mattered most hadn't happened yet.

The lesson still hasn't been learnt. In June 2024 Leopold Aschenbrenner, a former OpenAI researcher, published an essay called [Situational Awareness](https://situational-awareness.ai). It argued that AI might be doing its own research by 2027. He then launched a hedge fund with the same name to bet on it. By the end of June 2026 the fund was [up 439% for the year](https://techcrunch.com/2026/07/30/ai-hedge-fund-situational-awareness-may-have-sold-its-public-portfolio-but-it-still-has-its-anthropic-shares/), with its gains magnified by borrowed money. Then in July shares in AI chips, power and data centres fell, some by more than 30% in a month. The fund had to sell most of its public shares to Citadel, and reports put its losses at about $35 billion. Aschenbrenner may still be right about AI. But being right about where the world ends up doesn't help if one bad month on the way can force you to sell everything.


## Attempts to make sense of this

I went into this project with the naive assumption that I'd be able to discover a simple, legible system for describing all the different types of problems we have. I was extremely wrong and very humbled.

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
