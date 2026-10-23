---
type: Framework
title: Well vs ill-structured problems
description: >-
  A well-structured problem has a clear goal, known moves and a way to check an answer, like chess. An ill-structured problem lacks one or more of these, like designing a house. Simon argued most real problems are ill-structured.
date: 1964
cited_date: 1973
creators:
  - Walter Reitman
  - Herbert Simon
sources:
  - resource: https://doi.org/10.1016/0004-3702%2873%2990011-8
    title: The structure of ill structured problems
  - resource: https://ojs.unbc.ca/index.php/design/article/view/1273
    title: The structure of ill structured problems (free reprint)
  - resource: https://doi.org/10.1287/opre.6.1.1
    title: "Heuristic problem solving: the next advance in operations research"
  - resource: https://doi.org/10.1007/s10648-015-9343-1
    title: The structure of ill-structured (and well-structured) problems revisited
---
# Well vs ill-structured problems

**A well-structured problem has a clear goal, known moves and a way to check an answer. An ill-structured problem lacks one or more of these.**

1964 (1973) · Walter Reitman and Herbert Simon · [Key paper](https://doi.org/10.1016/0004-3702%2873%2990011-8) · Feeds 2 axes

## The idea

Some problems come with everything you need to know whether you have solved them. The goal is clear, the moves you can make are known and there is a test that tells a good answer from a bad one. Chess is like this. Other problems are missing one or more of those parts. You don't fully know what you want, what you are allowed to do or how to tell when you are done. Herbert Simon and his colleague Allen Newell called the two kinds well-structured and ill-structured as early as 1958. In 1964 the psychologist Walter Reitman called the second kind ill-defined problems and was the first to study what makes them so, which is why this page dates the idea to him. In 1973 Simon gave his full account of the split.

Simon's point was that the tidy kind is rare outside games and textbooks. Designing a house is his classic ill-structured problem. The client can't list every want up front, and the wants change once they see a sketch. Each choice about the roof changes what makes sense for the windows. Simon thought people cope by carving off small well-structured pieces as they go, and pinning down the goal a little more each time. He also argued that the line depends on the solver. Even chess is fully well-structured only in principle, since no player can search every move. The trait this sorts on is whether the goal, the moves and the test are all clear to the person solving it, which ties it to [Familiar vs novel to the solver](../axes/familiar-vs-novel-to-the-solver.md).

## What goes wrong

The usual mistake is to treat an ill-structured problem as if it were well-structured. You write a full specification and fix the budget and the date. Then you act surprised when the real goal turns up halfway through. The reverse mistake also happens. People treat a problem with a clear answer as if it were open to endless debate, and so never sit down and work it out.

## What to do instead

The better response is to check which parts are missing (the goal, the moves or the test) and to pin down what you can before you plan the rest.

## Examples

### Deep Blue

In May 1997 IBM's Deep Blue beat the world champion Garry Kasparov over six games in New York. Chess is hard but well-structured. The board, the legal moves and the meaning of a win are all fixed, so a machine could search its way to strength. That same approach is useless where the moves and the goal are themselves unclear.

### Sydney Opera House

In 1957 Jørn Utzon won the design competition with a sketch of curved shells that nobody yet knew how to build. The project was run as if it had a fixed plan, with a budget of about A$7 million and an opening planned for 1963. Working out how to build the roof took years. Utzon quit in 1966, and the building finally opened in 1973 at a cost of A$102 million. The problem was ill-structured from the start, and the budget pretended it wasn't.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) | Information › Evidence | An ill-structured problem may lack a test that tells a good answer from a bad one |
| [Well vs ill-structured](../axes/well-vs-ill-structured.md) | Performance › Goal | Whether the goal, the moves and the test are all clear to the person solving it |

## Further reading

- [The structure of ill structured problems](https://doi.org/10.1016/0004-3702%2873%2990011-8), Herbert Simon, *Artificial Intelligence*, 1973. Simon's full account of the split, which argues that the line between the two kinds is vague and shifts with the solver.
- [The same paper as a free reprint](https://ojs.unbc.ca/index.php/design/article/view/1273), in the classic articles section of the *Annual Review of Policy Design*, 2015.
- [Heuristic problem solving: the next advance in operations research](https://doi.org/10.1287/opre.6.1.1), Herbert Simon and Allen Newell, *Operations Research*, 1958. The early paper that set well-structured problems against ill-structured ones, and predicted a computer chess champion.
- [The structure of ill-structured (and well-structured) problems revisited](https://doi.org/10.1007/s10648-015-9343-1), Stephen Reed, *Educational Psychology Review*, 2016. Revisits Simon's split more than forty years on.
