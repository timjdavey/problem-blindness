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
  - resource: https://en.wikipedia.org/wiki/NP-completeness
---

# NP problems

Some problems are hard to solve but easy to check. A sudoku can take an hour to fill in, yet you can check a finished grid in a minute by running down each row, column and box. That gap between finding and checking is the trait this framework sorts on. Problems where an answer can be checked fast are called NP. Here "fast" means the time grows gently as the problem gets bigger, rather than doubling with each extra piece.

In 1971 Stephen Cook showed that some problems in NP are the hardest of the lot. If you found a fast way to solve any one of them, you could solve them all fast. These are called NP-complete. A year later Richard Karp showed that 21 well known problems belonged to this group, and Leonid Levin found the same idea on his own in the Soviet Union. Whether every problem that is easy to check is also easy to solve is still unknown. It is called P versus NP, and it carries a million dollar prize.

The mistake is to treat a problem that is hard to solve as if it were easy, just because the answer is easy to recognise. You promise the best possible delivery route or the perfect school timetable. Then the search blows up as the problem grows. The better response is to aim for a good answer rather than the best one, using rules of thumb, and to lean on the cheap check to compare the options you find.

## Examples

**RSA-129.** In August 1977 Martin Gardner's column in *Scientific American* printed a 129 digit number and offered $100 to anyone who could find its two prime factors. It took until 1994, when about 600 volunteers pooled their computers over the internet. Checking their answer took one multiplication. The hidden message turned out to be "The Magic Words are Squeamish Ossifrage". Much of today's online security rests on that same gap between finding and checking. Factoring is in NP, but it is not thought to be NP-complete, so it is probably not one of the hardest of the lot.

**A delivery van.** A driver with 10 drops can visit them in 3,628,800 different orders. With 20 drops there are about 2.4 billion billion orders, far too many to try one by one. This is a version of the travelling salesman problem, which is NP-complete. Yet if someone hands the driver a route, it takes seconds to add up the miles and see if it beats yesterday's. Courier firms don't search for the perfect route. They use shortcuts that find good routes fast and check them against each other.
