---
name: Convex vs non-convex optimisation
date: 1970
cited_date: 2004
creators:
  - R. Tyrrell Rockafellar
  - Stephen Boyd
  - Lieven Vandenberghe
link: https://en.wikipedia.org/wiki/Convex_optimization
summary: >-
  In a convex problem the landscape has one valley, so going downhill always finds the best answer. A non-convex problem has many valleys. Where you start decides where you end up, and small changes can send you somewhere else.
---

# Convex vs non-convex optimisation

Picture yourself on a hillside in thick fog, trying to reach the lowest point. You feel which way the ground slopes and step downhill. If the land is one big bowl, this always works. Every downhill step takes you nearer the bottom, and when the ground goes flat you know you have arrived. A problem shaped like that is called convex.

Now picture land full of hollows and ridges. Stepping downhill still takes you to a low point, but only the one nearest where you started. It feels like the bottom, yet there may be a far deeper valley over the next ridge. This is a non-convex problem, and the false bottom is called a local optimum.

The trait this sorts on is the shape of the problem, not its size. A convex problem with a million variables can be solved fast, and the answer is the true best. A non-convex problem with a few dozen variables can be hopeless to solve exactly. Rockafellar set out the maths in 1970. In 2004 Boyd and Vandenberghe wrote the textbook that turned it into an everyday tool for engineers.

The mistake is to treat a non-convex problem as convex. You improve step by step until no small change helps, and then you declare it the best. In fact you only found the best near where you began. The fix is to start from many places or take a big jump now and then, and to accept that your answer depends on your starting point.

## Examples

**Stigler's diet.** In 1945 the economist George Stigler asked for the cheapest diet that met an adult's needs, choosing from 77 foods. The maths of that problem is convex, so there is one true best. He had no way to solve it exactly and made a careful guess instead. In 1947 the new simplex method found the exact answer, and Stigler's guess was less than a dollar a year more expensive. In a bowl, sensible steps get you close.

**Tweaking a website.** A team tests every small change to a sign up page and keeps whatever wins. After a year every small tweak makes things worse, so the page looks perfect. A full redesign might do far better, but small steps can never reach it, because every route there goes uphill first.

**Training neural networks.** Training a large neural network is a hugely non-convex problem. Engineers start from random settings and add noise to each step, which helps shake the model out of shallow hollows. Two runs with different random starts end in different places, which is one reason results can be hard to reproduce.
