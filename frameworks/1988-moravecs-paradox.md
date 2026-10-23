---
type: Framework
title: Moravec's paradox
description: >-
  What is hard for people and what is hard for machines don't line up. Computers played draughts and passed intelligence tests long before they could see or pick things up, which a toddler does without trying. So "hard" means nothing until you say who is doing the solving.
date: 1988
creators:
  - Hans Moravec
  - Marvin Minsky
  - Rodney Brooks
sources:
  - resource: https://archive.org/details/mindchildrenfutu00mora
    title: "Mind Children: the future of robot and human intelligence"
  - resource: https://en.wikipedia.org/wiki/Moravec%27s_paradox
    title: Moravec's paradox (Wikipedia)
  - resource: https://people.csail.mit.edu/brooks/papers/elephants.pdf
    title: Elephants don't play chess (free PDF)
---
# Moravec's paradox

**What is hard for people and what is hard for machines don't line up.**

1988 · Hans Moravec, Marvin Minsky and Rodney Brooks · [Original book](https://archive.org/details/mindchildrenfutu00mora) · Feeds 2 axes

## The idea

In 1988 Hans Moravec, a roboticist at Carnegie Mellon University, published *Mind Children* with Harvard University Press. In it he wrote that "it is comparatively easy to make computers exhibit adult level performance on intelligence tests or playing checkers, and difficult or impossible to give them the skills of a one-year-old when it comes to perception and mobility". Others had seen the same thing. Marvin Minsky at MIT put it as "we're least aware of what our minds do best". In 1990 Rodney Brooks, also at MIT, wrote a paper called "Elephants don't play chess". He argued that AI should start from robots that sense and move in the real world, not from puzzles. In 1994 Steven Pinker summed it up: "the main lesson of thirty-five years of AI research is that the hard problems are easy and the easy problems are hard."

Moravec's answer was evolution. Seeing, grasping and walking have been tuned for so long that we do them without noticing. He wrote that the parts of the brain that handle them hold "a billion years of experience about the nature of the world and how to survive in it". Reasoning is new, so it feels like hard work to us, even though it takes far less computing. A machine has no such history. What it finds hard depends on how it was built and what it was trained on. The trait this sorts on is who is solving. Difficulty isn't a property of the problem alone, so "hard" has to be stated relative to the solver. This is the [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) axis. Moravec showed that the list of things familiar to people and the list familiar to machines barely overlap.

## What goes wrong

The mistake is to judge how hard a task will be for a machine by how hard it feels to you. People hand machines the jobs that feel simple and keep the jobs that feel clever, and get both wrong. It also runs the other way. A machine that does something impressive seems smart, so people trust it with things that look easier, where it may fail.

## What to do instead

The better response is to name the solver every time you call something hard. Before you hand over a task, ask whether this kind of task is familiar to this solver, not whether it would be hard for you. Then test the machine on the dull parts of the job as well as the clever ones.

## Examples

### AlphaGo needed a hand

From 9 to 15 March 2016 DeepMind's AlphaGo played Lee Sedol, one of the world's best Go players, at the Four Seasons Hotel in Seoul. It won four games to one. Yet AlphaGo couldn't put a single stone on the board. The program ran on Google's servers in the United States. Aja Huang, a DeepMind researcher and amateur 6-dan player, sat at the board and placed each stone for it. The machine could beat a world champion at the thinking but needed a person for the part any child can do.

### Tesla's flufferbot

In July 2017 Elon Musk said Tesla would make 20,000 Model 3 cars a month by December. In the whole of the last three months of 2017 it made 2,425. On 13 April 2018 Musk tweeted "Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated." On a call with investors in May 2018 he gave an example. Tesla had tried to get a machine to place fibreglass mats, which he called "fluff", on top of each battery pack. The machine often failed to pick the fluff up or put it in the wrong place, and the line kept breaking down. Human hands were far better at it, and the robot was taken off the line.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Explicit vs tacit know-how](../axes/explicit-vs-tacit-know-how.md) | Agent › Know-how | Seeing, grasping and walking are tacit skills that machines found far harder than reasoning |
| [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md) | Agent › Know-how | What is familiar to people and what is familiar to machines barely overlap, so name the solver |

## Further reading

- [Mind Children: the future of robot and human intelligence](https://archive.org/details/mindchildrenfutu00mora), Hans Moravec, *Harvard University Press*, 1988. The book where Moravec stated the paradox, free to borrow from the Internet Archive.
- [Moravec's paradox](https://en.wikipedia.org/wiki/Moravec%27s_paradox) on Wikipedia.
- [Elephants don't play chess](https://people.csail.mit.edu/brooks/papers/elephants.pdf), Rodney Brooks, *Robotics and Autonomous Systems*, 1990. The case for building AI from robots that sense and move in the real world, free on Brooks's MIT page.
