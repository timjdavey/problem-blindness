---
type: Framework
title: Near decomposability
description: >-
  Many complex systems are built from parts that interact strongly inside and weakly between. If a problem breaks up like this you can solve it one part at a time. If it doesn't, every fix touches everything else.
date: 1962
creators:
  - Herbert Simon
sources:
  - resource: https://www.jstor.org/stable/985254
    title: The architecture of complexity
  - resource: https://en.wikipedia.org/wiki/Herbert_A._Simon
    title: Herbert A. Simon (Wikipedia)
  - resource: https://en.wikipedia.org/wiki/The_Sciences_of_the_Artificial
    title: The Sciences of the Artificial (Wikipedia)
  - resource: https://pages.gseis.ucla.edu/faculty/agre/simon.html
    title: Hierarchy and history in Simon's "Architecture of Complexity"
---
# Near decomposability

**Many complex systems are built from parts that interact strongly inside and weakly between.**

1962 · Herbert Simon · [Original paper](https://www.jstor.org/stable/985254) · Feeds 1 axis

## The idea

Think of an office building on a cold day. Heat moves fast between the desks in one room, so each room soon settles at its own even temperature. Heat moves slowly through the walls between rooms. So you can work out each room on its own first, and only then worry about how the rooms affect each other. Herbert Simon used this example in his 1962 paper "The Architecture of Complexity".

Simon argued that most complex systems are built like this. Cells make up organs and organs make up bodies. People form teams and teams form firms. The links inside each part are strong and fast, while the links between parts are weak and slow. He called this near decomposability. "Decomposable" means it can be split into pieces. "Near" means the pieces still touch a little, but not enough to stop you treating them one at a time.

The trait this sorts problems on is how the links are spread. If they cluster inside parts, you can split the problem, solve each piece and put them back together. That is how most engineering and most organisations work. If the links run everywhere, there are no clean pieces. Every fix in one place changes something somewhere else.

## What goes wrong

The common mistake is to split a tangled problem as if it broke apart neatly. You hand each piece to a different team, each team does well, and the whole thing still fails.

## What to do instead

The better response is to map where the strong links run before you split the work. Cut along the weak links, and make someone responsible for checking each link between the pieces.

## Examples

### The two watchmakers

Simon told a parable about two watchmakers, Hora and Tempus. Each built watches of about 1,000 parts. Tempus put each watch together in one go, so when the phone rang and he put it down, it fell to pieces. Hora built small units of ten parts, then joined those into bigger units. An interruption only cost him the unit he was on. Hora prospered while Tempus went out of business.

### Mars Climate Orbiter

NASA lost this probe in September 1999 as it reached Mars. One team's software reported thruster data in imperial units, while the team using it expected metric ones. The spec between the teams said metric, but nobody checked that both sides followed it. Each team tested its own part and treated the link as too simple to check. That one link sent a $125 million craft too deep into the Martian air.

### Fixing a car versus fixing a diet

If your car's radio breaks you can replace it without touching the brakes. A car is close to decomposable. Your health is not. Cut out sugar and you may sleep better, change your mood and eat more of something else. Treating a body like a car, one part at a time, is why so many neat fixes come with side effects.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Reductionist vs holistic](../axes/reductionist-vs-holistic.md) | Environment › Structure | Strong links inside parts and weak links between them let you solve one part at a time |

## Further reading

- [The architecture of complexity](https://www.jstor.org/stable/985254), Herbert Simon, *Proceedings of the American Philosophical Society*, 1962. The original paper, with the office building and the two watchmakers.
- [Herbert A. Simon](https://en.wikipedia.org/wiki/Herbert_A._Simon) on Wikipedia, which covers his theorems on near decomposability.
- [The Sciences of the Artificial](https://en.wikipedia.org/wiki/The_Sciences_of_the_Artificial) on Wikipedia, on the 1969 book that grew out of the paper.
- [Hierarchy and history in Simon's "Architecture of Complexity"](https://pages.gseis.ucla.edu/faculty/agre/simon.html), Philip Agre, *Journal of the Learning Sciences*, 2003. An essay that places the paper in the history of Simon's work, free on the author's site.
