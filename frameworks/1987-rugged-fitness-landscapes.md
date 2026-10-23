---
type: Framework
title: Rugged fitness landscapes
description: >-
  When the parts of a problem don't affect each other, small steps uphill always reach the top. When the parts interact, the landscape fills with small peaks. Step by step improvement then gets stuck on whichever peak is nearest.
date: 1987
cited_date: 1993
creators:
  - Stuart Kauffman
  - Simon Levin
sources:
  - resource: https://doi.org/10.1016/S0022-5193(87)80029-2
    title: Towards a general theory of adaptive walks on rugged landscapes
  - resource: https://en.wikipedia.org/wiki/NK_model
    title: NK model (Wikipedia)
  - resource: https://doi.org/10.1287/mnsc.43.7.934
    title: Adaptation on rugged landscapes
  - resource: https://doi.org/10.1287/mnsc.46.6.824.11940
    title: Imitation of complex strategies
---
# Rugged fitness landscapes

**When the parts of a problem don't affect each other, small steps uphill always reach the top. When the parts interact, the landscape fills with small peaks.**

1987 (1993) · Stuart Kauffman and Simon Levin · [Original paper](https://doi.org/10.1016/S0022-5193(87)80029-2) · Feeds 1 axis

## The idea

In 1932 the geneticist Sewall Wright pictured evolution as a walk across a landscape. Each point is a possible set of genes, and its height is how well that creature survives and breeds. Selection pushes a population uphill, which can strand it on a small hill while a far higher one stands nearby. In 1987 Stuart Kauffman and Simon Levin turned the picture into maths. They compared a smooth landscape with a fully random one and showed how uphill steps fare on each. Kauffman then asked what decides how many hills there are. He built a model with a dial for how rugged the land is, first in papers from 1989 and then in full in his 1993 book The Origins of Order.

The answer is how much the parts interact. Take a problem with many parts, each of which you can set one way or another. If each part adds to the score on its own, the land has a single peak and small steps always reach it. Now let each part's value depend on a few others. Changing one part then helps some things and hurts others, and the land breaks into many peaks. This is called a rugged landscape. Kauffman's model uses N for the number of parts and K for how many others each one depends on, so it is known as the NK model. The trait this sorts on is how much the parts of a problem depend on each other.

## What goes wrong

The mistake is to improve a rugged problem one small change at a time. Each step helps, so it feels like progress. Then nothing small helps any more, and you decide you have found the best. You have only found the top of the nearest hill, and it may be a low one.

## What to do instead

The better response on rugged land is to make bigger jumps that change many linked parts at once, or to have many teams start from different places. Expect most big jumps to fail, because a long leap on rugged land lands somewhere close to random.

## Examples

### Levinthal's firms

In 1997 Daniel Levinthal brought the NK model into management. He treated a firm as a bundle of linked choices, such as what to make, how to sell it and how to organise staff. When the choices interacted a lot, firms that started in different places settled on different peaks and stayed there. When the market shifted, firms that could only make small changes were often stuck on a peak that had sunk.

### Continental Lite

Michael Porter told this story in his 1996 essay "What is strategy?". In October 1993 Continental Airlines launched Continental Lite to copy Southwest's cheap short flights. It took some of Southwest's parts, like low fares and quick turnarounds, but kept others from its old business. The pieces fought each other, and it lost an estimated $100 million in its first full year. In 2000 Jan Rivkin used the NK model to explain cases like this. When the parts of a strategy interact, copying most of them can leave you far from the top.

## Axes

| Axis | Group | What this framework adds |
|---|---|---|
| [Smooth vs rugged](../axes/smooth-vs-rugged.md) | Environment › Structure | When the parts interact the land fills with small peaks, so small steps stall on the nearest one |

## Further reading

- [Towards a general theory of adaptive walks on rugged landscapes](https://doi.org/10.1016/S0022-5193(87)80029-2), Stuart Kauffman and Simon Levin, *Journal of Theoretical Biology*, 1987. The original paper comparing uphill walks on smooth and random landscapes.
- [NK model](https://en.wikipedia.org/wiki/NK_model) on Wikipedia, which explains the model with a dial for ruggedness that Kauffman built next.
- [Adaptation on rugged landscapes](https://doi.org/10.1287/mnsc.43.7.934), Daniel Levinthal, *Management Science*, 1997. The paper that brought the NK model into management, with firms as bundles of linked choices.
- [Imitation of complex strategies](https://doi.org/10.1287/mnsc.46.6.824.11940), Jan Rivkin, *Management Science*, 2000. Why copying most of a rival's linked choices can leave you far from the top.
