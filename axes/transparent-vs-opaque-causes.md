---
type: Axis
title: Transparent vs opaque causes
description: Even when you can see every part, can you follow how one thing leads to another well enough to predict what a change will do?
group: knower
easy_end: Transparent
hard_end: Opaque
sources:
  - resource: /frameworks/1959-decision-strategies-matrix.md
    title: Decision strategies matrix
  - resource: /frameworks/1984-normal-accidents.md
    title: Normal accidents
  - resource: /frameworks/1990-detail-vs-dynamic-complexity.md
    title: Detail vs dynamic complexity
  - resource: /frameworks/1995-task-environment-properties.md
    title: Task environment properties
  - resource: /frameworks/1996-stacey-matrix.md
    title: Stacey matrix
  - resource: /frameworks/1999-cynefin.md
    title: Cynefin
  - resource: /frameworks/2002-simple-complicated-and-complex.md
    title: Simple, complicated and complex
---
# Transparent vs opaque causes

An axis in the [knower](index.md#the-knower) group.

Even when you can see every part, can you follow how one thing leads to another well enough to predict what a change will do? A lever is transparent. A large codebase follows rules, yet no one person can hold the whole chain in their head.

## Actions

**Transparent**: Model the mechanism.
- Write the cause and effect into the system as rules or structure. A model that has to rediscover a known mechanism wastes data.
- Debug by following the chain. When something goes wrong you can trace it to the step that failed.

**Opaque**: Don't trust explanations, trust experiments.
- Treat the model's story of why as a guess. It will sound right and may be wrong.
- Change one thing at a time and measure the effect. That is how you find a cause you can't trace.
- Use the model to predict, and hold back claims about cause. Test a claim before you build a decision on it.
- Expect a fix to have side effects. When you can't see the chain, you can't see what else it touches.

## Correlated with

- [Decomposable vs holistic](decomposable-vs-holistic.md) (bundled). Weaver's [organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md), Perrow's tangled systems in [Normal accidents](../frameworks/1984-normal-accidents.md), the complex domain of [Cynefin](../frameworks/1999-cynefin.md) and Glouberman and Zimmerman's [complex problems](../frameworks/2002-simple-complicated-and-complex.md) all say causes are hard to trace because the parts keep changing each other.
- [Full vs partial observability](full-vs-partial-observability.md) (study). Hidden variables are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](../frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every line of an open source codebase and still not trace the chain. A poker hand is a simple cause that is hidden from view.
- [Kind vs wicked feedback](kind-vs-wicked-feedback.md) and [One-shot vs sequential](one-shot-vs-sequential.md) (study). In Senge's [beer game](../frameworks/1990-detail-vs-dynamic-complexity.md) delays put weeks between an order and its effect, so players blame the wrong thing.
- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (bundled). Perrow's [unanalysable work](../frameworks/1967-routine-vs-non-routine-technology.md) has no logical way to search for answers, so people fall back on hunch. But the two come apart. Riding a bike has clear physics and needs tacit skill. A tax code has explicit rules and knock-on effects nobody can trace.
- [Test vs watch](test-vs-watch.md) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).

## Citations

[1] [Decision strategies matrix](../frameworks/1959-decision-strategies-matrix.md)

[2] [Normal accidents](../frameworks/1984-normal-accidents.md)

[3] [Detail vs dynamic complexity](../frameworks/1990-detail-vs-dynamic-complexity.md)

[4] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[5] [Stacey matrix](../frameworks/1996-stacey-matrix.md)

[6] [Cynefin](../frameworks/1999-cynefin.md)

[7] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)
