---
name: Task environment properties
date: 1995
creators:
  - Stuart Russell
  - Peter Norvig
link: https://aima.cs.berkeley.edu/
summary: >-
  Sorts the world an agent acts in by a few plain questions. Can it see everything, does chance play a part and does the world change while it thinks? Later editions added whether anyone else is acting. A crossword is easy on every count and driving a taxi is hard on every count.
---

# Task environment properties

In 1995 Stuart Russell and Peter Norvig published Artificial Intelligence: A Modern Approach, which became the standard textbook in the field. The book treats an AI as an agent that senses its world and acts in it. So before you design the agent you have to describe its world, and they gave a short list of questions for doing that.

Can the agent see everything that matters, or is some of it hidden? Does an action always have the same result, or does chance get a say? Does each choice stand alone, or shape the ones that follow? Does the world change while the agent thinks? Do things come in clean steps like moves in a game, or flow smoothly like speed and steering? Later editions added two more. Are other agents acting, and do they compete or help? And does the agent even know the rules? The book calls these the properties of the task environment. Each has an easy end and a hard end. The hardest world is partly hidden, crowded and ruled by chance, and it moves on without you.

The mistake is to build for an easier world than the real one. A system tested where everything is visible and nothing moves can look brilliant. Then it meets the real world and fails in ways the tests could never show. People do this too, when a plan assumes rivals will stand still. The better response is to describe the world honestly on every count before choosing a tool. If it is partly hidden, you need a running guess about what you can't see. If others act, you need a model of what they want. If chance plays a part, you need odds rather than certainties.

## Examples

**From crosswords to taxis.** The book's own table runs from easy to hard. A crossword is fully visible and solo, with a grid that waits for you. Chess with a clock adds an opponent and time pressure. Poker hides the cards and adds luck. Taxi driving is hard on every count. Deep Blue beat Garry Kasparov at chess in 1997 and a program beat top poker professionals in 2017. Waymo only opened fully driverless rides to the public in 2020, in a small patch of suburban Phoenix.

**Uber in Tempe.** On 18 March 2018 a self-driving Uber test car killed Elaine Herzberg as she pushed her bicycle across a road at night in Tempe, Arizona. Its sensors picked her up 5.6 seconds before impact. The software kept changing its mind about what she was, and each time it threw away her track, so it never worked out where she was heading. US safety investigators found that "the system design did not include a consideration for jaywalking pedestrians." The car was built for a world where people cross at crossings.
