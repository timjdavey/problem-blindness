---
type: Framework
title: Flat maximum
description: >-
  Near the best answer the payoff is often flat, so small errors in your weights or choices cost little. Where the payoff is peaked, the last bit of tuning matters a lot.
date: 1973
cited_date: 1982
creators:
  - Detlof von Winterfeldt
  - Ward Edwards
sources:
  - resource: https://doi.org/10.1037/0033-2909.91.3.609
---

# Flat maximum

Picture a hill with a broad, flat top. Anywhere near the summit you are about as high as you can get. Now picture a sharp peak, where one step off the top drops you a long way. Many decisions look like the first hill, so once you are close to the best choice, moving closer gains you almost nothing. This is called a flat maximum, and the trait it sorts problems on is the shape of the payoff near the top.

In 1973 Detlof von Winterfeldt and Ward Edwards at the University of Michigan wrote a report called "Flat maxima in linear optimization models". Others kept finding flat tops when they tested how much a model's answer moved as its inputs changed. The report showed why the maths of linear decision models, which add up weighted scores, tends to force this shape. The version most often cited is a later paper by the pair in *Psychological Bulletin* in 1982.

Herbert Simon's satisficing treats good enough as a habit of the person. The flat maximum makes it a trait of the problem. If the top is flat, good enough is nearly as good as best, so a long hunt for the perfect answer wastes effort. If the top is peaked, settling early is a real loss. The mistake runs both ways. People polish the weights in a scoring model for weeks when any sensible weights would do. Others bring a relaxed habit to a problem with a sharp peak, where small errors hurt.

This framework feeds the [Satisficing vs optimising](../axes/satisficing-vs-optimising.md) and [Smooth vs rugged](../axes/smooth-vs-rugged.md) axes.

## Examples

**Graduate admissions in Oregon.** In a 1979 paper in *American Psychologist*, Robyn Dawes tried to predict how the faculty would later rate graduate students at the University of Oregon from three numbers: a test score, their college grades and how selective their college was. On a scale where 0 means no link and 1 means a perfect forecast, the admissions committee's own judgement scored .19. Weights fitted to half the students and tested on the other half scored .38. Just adding the three scores with equal weights scored .48. Dawes explained this with von Winterfeldt and Edwards' flat maximum: weights near the best ones give almost the same answer. What mattered was choosing the right measures and knowing which way each one pointed.

**Warfarin.** The blood thinner warfarin has the opposite shape. Doctors adjust the dose to hit a target on a blood test called the INR, which for many patients is 2 to 3. Below about 1.5 the risk of a clot goes up, and above about 3.5 to 4 the risk of bleeding in the brain goes up. The window is narrow, so patients have regular blood tests to keep them on the peak. Here a small error costs a lot, and getting the dose just right pays.
