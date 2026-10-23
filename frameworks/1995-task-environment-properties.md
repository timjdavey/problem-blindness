---
type: Framework
title: Task environment properties
description: >-
  Sorts the world an agent acts in by a few plain questions. Can it see everything, does chance play a part and does the world change while it thinks? Later editions added whether anyone else is acting. A crossword is easy on every count and driving a taxi is hard on every count.
date: 1995
creators:
  - Stuart Russell
  - Peter Norvig
sources:
  - resource: https://aima.cs.berkeley.edu/
    title: "Artificial intelligence: a modern approach"
  - resource: https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach
    title: "Artificial Intelligence: A Modern Approach (Wikipedia)"
  - resource: https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf
    title: Collision between vehicle controlled by developmental automated driving system and pedestrian
  - resource: https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg
    title: Death of Elaine Herzberg (Wikipedia)
---
# Task environment properties

**Sorts the world an agent acts in by a few plain questions. Can it see everything, does chance play a part and does the world change while it thinks?**

1995 · Stuart Russell and Peter Norvig · [Original book](https://aima.cs.berkeley.edu/) · Feeds 6 axes

## The idea

In 1995 Stuart Russell and Peter Norvig published Artificial Intelligence: A Modern Approach, which became the standard textbook in the field. The book treats an AI as an agent that senses its world and acts in it. So before you design the agent you have to describe its world, and they gave a short list of questions for doing that.

Can the agent see everything that matters, or is some of it hidden? Does an action always have the same result, or does chance get a say? Does each choice stand alone, or shape the ones that follow? Does the world change while the agent thinks? Do things come in clean steps like moves in a game, or flow smoothly like speed and steering? Later editions added two more. Are other agents acting, and do they compete or help? And does the agent even know the rules? The book calls these the properties of the task environment. Each has an easy end and a hard end. The hardest world is partly hidden, crowded and ruled by chance, and it moves on without you.

## What goes wrong

The mistake is to build for an easier world than the real one. A system tested where everything is visible and nothing moves can look brilliant. Then it meets the real world and fails in ways the tests could never show. People do this too, when a plan assumes rivals will stand still.

## What to do instead

The better response is to describe the world honestly on every count before choosing a tool. If it is partly hidden, you need a running guess about what you can't see. If others act, you need a model of what they want. If chance plays a part, you need odds rather than certainties.

## Examples

### From crosswords to taxis

The book's own table runs from easy to hard. A crossword is fully visible and solo, with a grid that waits for you. Chess with a clock adds an opponent and time pressure. Poker hides the cards and adds luck. Taxi driving is hard on every count. Deep Blue beat Garry Kasparov at chess in 1997 and a program beat top poker professionals in 2017. Waymo only opened fully driverless rides to the public in 2020, in a small patch of suburban Phoenix.

### Uber in Tempe

On 18 March 2018 a self-driving Uber test car killed Elaine Herzberg as she pushed her bicycle across a road at night in Tempe, Arizona. Its sensors picked her up 5.6 seconds before impact. The software kept changing its mind about what she was, and each time it threw away her track, so it never worked out where she was heading. US safety investigators found that "the system design did not include a consideration for jaywalking pedestrians." The car was built for a world where people cross at crossings.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Deterministic vs stochastic](../axes/deterministic-vs-stochastic.md) | Environment › Randomness | Whether an action always has the same result or chance gets a say |
| [Neutral vs adversarial](../axes/neutral-vs-adversarial.md) | Environment › Reactivity | Whether other agents are acting, and whether they compete or help |
| [Static vs dynamic](../axes/static-vs-dynamic.md) | Environment › Change | Whether the world changes while the agent thinks |
| [Standalone vs sequential](../axes/standalone-vs-sequential.md) | Actions › Options | Whether each choice stands alone or shapes the ones that follow |
| [Reducible vs irreducible uncertainty](../axes/reducible-vs-irreducible-uncertainty.md) | Information › Uncertainty | Whether the agent can see everything that matters, or some of it is hidden |
| [Transparent vs opaque causes](../axes/transparent-vs-opaque-causes.md) | Information › Evidence | Whether the agent even knows the rules of its world |

## Further reading

- [Artificial intelligence: a modern approach](https://aima.cs.berkeley.edu/), Stuart Russell and Peter Norvig. The book's own site, now for the fourth edition.
- [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach) on Wikipedia.
- [Collision between vehicle controlled by developmental automated driving system and pedestrian](https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf), *National Transportation Safety Board*, 2019. The full report on the Tempe crash, including how the software classified Elaine Herzberg.
- [Death of Elaine Herzberg](https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg) on Wikipedia.
