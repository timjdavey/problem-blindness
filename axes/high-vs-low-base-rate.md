---
type: Axis
title: High vs low base rate
description: "High base rate: the thing you're looking for is common among the cases you check, so most yeses are real (e.g. a flu test on patients with flu symptoms in winter). Low base rate: the thing is so rare among the cases you check that even a good test is wrong most times it says yes (e.g. screening everyone for a disease 1 in 10,000 people have)."
group: information
subgroup: evidence
easy_end: High base rate
hard_end: Low base rate
sources:
  - resource: /frameworks/1955-base-rates.md
    title: Base rates
  - resource: /frameworks/1954-signal-detection-theory.md
    title: Signal detection theory
---
# High vs low base rate

An axis in the [Evidence](index.md#evidence) set of the [information](index.md#information) group.

Is the thing you're looking for common among the cases you check, or so rare that even a good test is wrong most times it says yes? Say a disease hits 1 person in 10,000 and the test is right 99% of the time. Screen a million people. About 100 have the disease and the test catches 99 of them. But 1% of the 999,900 who are well get a false alarm too. That is about 10,000 false alarms against 99 real cases, so a positive means you are about 1% likely to be ill. People read "99% accurate" as "a positive is 99% likely to be real", and doctors make the same slip. The base rate belongs to the group you test, not to the test. The same test does far better on people who already have symptoms than on everyone.

## Actions

**High base rate**: Trust a good test.
- Read a yes from an accurate test at face value. When the real thing is common among the cases you check, most of the cases the test flags have it. [1]
- Use the test on the kind of group it was built on. A sign tested on a sample where half the cases were real works as well as it looked when about half the cases you see are real too. [1]

**Low base rate**: Start from how common the real thing is.
- Start from how common the real thing is before you read a yes. When it is rare, most yeses are wrong even from a good test. Asked about a disease that hits one person in a thousand and a test with a 5% false alarm rate, 27 of 60 Harvard doctors and students said a positive meant a 95% chance of disease. The answer is about 2%. [1]
- Count it out in people, not percentages. One in a thousand has it, and fifty of the rest get a false alarm, so a positive is one real case in about fifty-one. People get the answer right far more often this way. [1]
- Judge a test by how many of its yeses are real, not by how often it's right. A doctor, a lab test or a model can be right 99% of the time on a rare disease by never flagging anyone. [1, 2]
- Check the test beats betting on the base rate at all. Meehl and Rosen showed a sign built on a sample where half the cases were real can flag more healthy people than ill ones once the real thing is rare, and then saying no to everyone makes fewer mistakes. [1]
- Screen in two stages. Use a cheap test that can't beat the base rate alone to choose who gets a second, better test. [1]

## Correlated with

- [Equal vs unequal error costs](equal-vs-unequal-error-costs.md) (tension). These are the two things signal detection theory sets the bar from. A rare target says raise the bar, since most yeses will be false. A costly miss says lower it. Cancer screening sits at both hard ends.
- [Plentiful vs scarce data](plentiful-vs-scarce-data.md) (independent). Card fraud has millions of past cases to learn from, yet only a tiny share of payments are fraud. A big record doesn't make the thing you're looking for common.
- [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md) (logic). A thing that is rare among the cases you check is one the solver seldom meets. A doctor sees a common cold every day but a rare disease once in a career.
- [Direct vs proxy measure](direct-vs-proxy-measure.md) (logic). When the real thing is rare, plain accuracy is a proxy that hides the misses. Saying no to everyone scores well and catches nothing.

## Citations

[1] [Base rates](../frameworks/1955-base-rates.md)

[2] [Signal detection theory](../frameworks/1954-signal-detection-theory.md)
