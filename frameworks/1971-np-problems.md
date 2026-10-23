---
type: Framework
title: NP problems
description: >-
  Some problems are hard to solve but easy to check, like a sudoku. Finding the answer may take ages. Once someone hands you an answer, you can test it fast.
date: 1971
creators:
  - Stephen Cook
  - Richard Karp
  - Leonid Levin
sources:
  - resource: https://doi.org/10.1145/800157.805047
    title: The complexity of theorem-proving procedures
  - resource: https://www.cs.toronto.edu/~sacook/homepage/1971.pdf
    title: The complexity of theorem-proving procedures (free PDF)
  - resource: https://en.wikipedia.org/wiki/NP-completeness
    title: NP-completeness (Wikipedia)
  - resource: https://doi.org/10.1007/978-1-4684-2001-2_9
    title: Reducibility among combinatorial problems
  - resource: https://lance.fortnow.com/papers/files/pnp-cacm.pdf
    title: The status of the P versus NP problem (free PDF)
---
# NP problems

**Some problems are hard to solve but easy to check, like a sudoku.**

1971 · Stephen Cook, Richard Karp and Leonid Levin · [Original paper](https://doi.org/10.1145/800157.805047) · Feeds 2 axes

## The idea

Some problems are hard to solve but easy to check. A sudoku can take an hour to fill in, yet you can check a finished grid in a minute by running down each row, column and box. That gap between finding and checking is the trait this framework sorts on. Problems where an answer can be checked fast are called NP. Here "fast" means the time grows gently as the problem gets bigger, rather than doubling with each extra piece.

In 1971 Stephen Cook showed that some problems in NP are the hardest of the lot. If you found a fast way to solve any one of them, you could solve them all fast. These are called NP-complete. A year later Richard Karp showed that 21 well known problems belonged to this group, and Leonid Levin found the same idea on his own in the Soviet Union. Whether every problem that is easy to check is also easy to solve is still unknown. It is called P versus NP, and it carries a million dollar prize.

## What goes wrong

The mistake is to treat a problem that is hard to solve as if it were easy, just because the answer is easy to recognise. You promise the best possible delivery route or the perfect school timetable. Then the search blows up as the problem grows.

## What to do instead

The better response is to aim for a good answer rather than the best one, using rules of thumb, and to lean on the cheap check to compare the options you find.

## Examples

### RSA-129

In August 1977 Martin Gardner's column in *Scientific American* printed a 129 digit number and offered $100 to anyone who could find its two prime factors. It took until 1994, when about 600 volunteers pooled their computers over the internet. Checking their answer took one multiplication. The hidden message turned out to be "The Magic Words are Squeamish Ossifrage". Much of today's online security rests on that same gap between finding and checking. Factoring is in NP, but it is not thought to be NP-complete, so it is probably not one of the hardest of the lot.

### A delivery van

A driver with 10 drops can visit them in 3,628,800 different orders. With 20 drops there are about 2.4 billion billion orders, far too many to try one by one. This is a version of the travelling salesman problem, which is NP-complete. Yet if someone hands the driver a route, it takes seconds to add up the miles and see if it beats yesterday's. Courier firms don't search for the perfect route. They use shortcuts that find good routes fast and check them against each other.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Verifiable vs unverifiable](../axes/verifiable-vs-unverifiable.md) | Information › Evidence | An answer that takes ages to find can still be checked fast, like a finished sudoku |
| [Tractable vs intractable search](../axes/tractable-vs-intractable-search.md) | Environment › Structure | For NP-complete problems the search blows up as the problem grows, so the best answer is out of reach |

## Further reading

- [The complexity of theorem-proving procedures](https://doi.org/10.1145/800157.805047), Stephen Cook, *Proceedings of the Third Annual ACM Symposium on Theory of Computing*, 1971. The original paper that defined NP-completeness.
- [The same paper as a free PDF](https://www.cs.toronto.edu/~sacook/homepage/1971.pdf), a scanned copy from Cook's home page at the University of Toronto.
- [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness) on Wikipedia.
- [Reducibility among combinatorial problems](https://doi.org/10.1007/978-1-4684-2001-2_9), Richard Karp, *Complexity of Computer Computations*, 1972. The paper that showed 21 well known problems are NP-complete.
- [The status of the P versus NP problem](https://lance.fortnow.com/papers/files/pnp-cacm.pdf), Lance Fortnow, *Communications of the ACM*, 2009. A short, readable survey of where the question stands, free from the author's site.
