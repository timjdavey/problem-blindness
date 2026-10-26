---
type: Guide
title: Contributing
description: How to add, rename or fix an axis or framework.
---
# Contributing

**How to add, rename or fix an axis or framework.**

This will never be finished. If you spot a missing framework, a wrong link or a better example, please open a pull request. A small fix needs nothing more than the fix and a line in [log.md](log.md).

## Adding a page

Every file starts with YAML front matter that needs a `type`, as the [Open Knowledge Format](https://okf.md) asks.

| Adding | File | Front matter | Then |
|---|---|---|---|
| A framework | `frameworks/1973-tame-vs-wicked-problems.md` | `type: Framework`, `title`, `description`, `date`, `creators`, `sources` (3 or more, each with a `title`) | Follow the [page layout](frameworks/README.md#whats-on-a-framework-page), then add it to the [frameworks index](frameworks/index.md) |
| An axis | `axes/thin-vs-fat-tails.md` | `type: Axis`, `title`, `description` (each end in one line), `group`, `subgroup`, `easy_end`, `hard_end`, `sources`, and `aliases` once it has been renamed | Follow the [page layout](axes/README.md#whats-on-an-axis-page), then add it to the [axes index](axes/index.md) under its set and link the axes it moves with |

Each action on an axis page must end with a number, like [2], that points at its source under Citations. An action nothing backs doesn't go in.

## Is it a new axis?

Most ideas for a new axis turn out to be an old one in new words. A new axis has to pass three tests.

1. **Corner test.** Name a problem at the new axis's hard end that sits at the easy end of the axes closest to it. If you can't, the new axis is a copy of one of them.
2. **Action test.** The hard end has to call for something the nearby axes don't already say. If it doesn't, the idea may still be real. But it belongs as a note on one of those axes.
3. **Combination test.** No mix of two or three existing axes can land the same problems at the hard end and call for the same actions. An idea can pass the first two tests against each axis alone and still fail this one.

Fixed vs moving goal failed the third test. A couple planning a wedding for 100 people on 5 June for under £20k have a clear brief, yet what they want shifts once they see venues. That passes the corner test, since the brief is clear and the world isn't drifting. But the brief left out wants they could only find by looking, the hard end of [Direct vs proxy measure](axes/direct-vs-proxy-measure.md). They found them through a chain of choices where each shaped the next, the hard end of [Standalone vs sequential](axes/standalone-vs-sequential.md). Those two axes already say what to do, so moving goals became a note on them.

## Naming an axis

- **Each end makes sense on its own.** Picture the label written alone at one end of a chart. "None" could mean anything, but "No skin in the game" can only mean one thing. "Easy" is worse, since every axis has an easy end. So labels carry the noun, like "Fat tails" or "Proxy measure", and the title can stay short.
- **No two ends share a label.** People [tag tasks](README.md#how-to-reference-axes) with the end labels, so `fat-tails` must point at one end of one axis.
- **Use the field's own term**, so readers can look it up. "Chaotic" beats "short predictability horizon", and "Knightian uncertainty" beats "unknown odds".
- **Don't sound like another axis**, in its name or in the words of its description. "Complete vs incomplete score" sounded too much like tractable vs intractable search, so it became [Direct vs proxy measure](axes/direct-vs-proxy-measure.md). "Slack" was Perrow's word for a buffer in [Buffered vs cascading](axes/buffered-vs-cascading.md), so the time to decide became [Ample time vs time pressure](axes/ample-time-vs-time-pressure.md).
- **Name the problem, not the response.** "Test vs watch" named two things you might do. [Interventional vs observational](axes/interventional-vs-observational.md) names the kind of evidence the world lets you get.

## Renaming a page

1. **Move the file** with `git mv`, so its history follows it. Nothing is left at the old path.
2. **Add the old name to `aliases`** in the renamed page's front matter.
3. **Update every link in the repo** to the new path, and record the rename in [log.md](log.md).

A merge or split works the same way. Every link moves to the page that took it in, or to the right half.

## Recording changes

Every change worth knowing about gets a line in [log.md](log.md).

1. **Put it under today's date**, as a `## 2026-10-26` heading. The newest date goes at the top.
2. **Start with what kind of change it is.** Use `**Creation**` for a new page and `**Update**` for anything else.
3. **Say why, not just what.** "Renamed Test vs watch, since it named two things you do" helps the next person more than "Renamed Test vs watch".
4. **Link with paths from the repo root**, like `/axes/thin-vs-fat-tails.md`, so the links work wherever the log is read.
