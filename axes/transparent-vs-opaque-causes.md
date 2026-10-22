---
type: Axis
title: Transparent vs opaque causes
description: "Transparent causes: you can follow how one thing leads to another and predict what a change will do (e.g. a lever). Opaque causes: you can see every part but can't follow the whole chain (e.g. a trained neural network)."
group: information
subgroup: evidence
easy_end: Transparent causes
hard_end: Opaque causes
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

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Even when you can see every part, can you follow how one thing leads to another well enough to predict what a change will do? A lever is transparent. A trained neural network is opaque. You can read every one of its weights, and it follows fixed rules, yet nobody can say why it gave a particular answer. A large codebase is not the same, because a stack trace lets you follow a bug back step by step. Nothing like a stack trace exists for the weights.

## Actions

**Transparent causes**: Model the mechanism.
- Write the known cause and effect into your rules. An engineer sizing a beam works from the physics, not from a pile of past beams that held.
- Fix faults by following the chain. When something goes wrong you can trace it to the step that failed, as an electrician does along a circuit.

**Opaque causes**: Don't trust explanations, trust experiments.
- Treat any story of why as a guess. An expert's account of why sales fell, or a model's account of its own answer, will sound right and may be wrong.
- Change one thing at a time and measure the effect. That is how you find a cause you can't trace.
- Use patterns to predict, and hold back claims about cause. Test a claim before you build a decision on it.
- Expect a fix to have side effects. When you can't see the chain, you can't see what else it touches.

## Correlated with

- [Decomposable vs tangled](decomposable-vs-tangled.md) (bundled). Weaver's [organised complexity](../frameworks/1948-simplicity-disorganised-and-organised-complexity.md), Perrow's tangled systems in [Normal accidents](../frameworks/1984-normal-accidents.md), the complex domain of [Cynefin](../frameworks/1999-cynefin.md) and Glouberman and Zimmerman's [complex problems](../frameworks/2002-simple-complicated-and-complex.md) all say causes are hard to trace because the parts keep changing each other.
- [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md) (study). Hidden facts are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](../frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every weight of an open model and still not trace the chain. A poker hand is a simple cause that is hidden from view, and you would know it the moment you saw it.
- [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md) and [Standalone vs sequential](standalone-vs-sequential.md) (study). In Senge's [beer game](../frameworks/1990-detail-vs-dynamic-complexity.md) delays put weeks between an order and its effect, so players blame the wrong thing.
- [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md) (bundled). Perrow's [unanalysable work](../frameworks/1967-routine-vs-non-routine-technology.md) has no logical way to search for answers, so people fall back on hunch. But the two come apart. Riding a bike has clear physics and needs tacit skill. A tax code has explicit rules and knock-on effects nobody can trace.
- [Interventional vs observational](interventional-vs-observational.md) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right ([Ladder of causation](../frameworks/2000-ladder-of-causation.md)).

## Citations

[1] [Decision strategies matrix](../frameworks/1959-decision-strategies-matrix.md)

[2] [Normal accidents](../frameworks/1984-normal-accidents.md)

[3] [Detail vs dynamic complexity](../frameworks/1990-detail-vs-dynamic-complexity.md)

[4] [Task environment properties](../frameworks/1995-task-environment-properties.md)

[5] [Stacey matrix](../frameworks/1996-stacey-matrix.md)

[6] [Cynefin](../frameworks/1999-cynefin.md)

[7] [Simple, complicated and complex](../frameworks/2002-simple-complicated-and-complex.md)
