# Predictions

Written before any task was tagged. Commit this file before running `tag.py`, so the git history shows the guesses came first.

With 40 axes and about 75 task families, a few axes will look strong by luck alone. Writing the guesses down first is what stops us from telling a story after the fact. If the axes below fail and others pass, that is the finding, and we report it as such.

## How to read the numbers

Each effect is the change in an agent's success rate when a task moves from the easy end of an axis to the hard end. It is measured beyond what the task's length already predicts. So "−0.15" means agents succeed 15 points less often on hard end tasks than on easy end tasks of the same length.

## The axes I expect to matter

These are Claude's guesses from the planning session. Tim should edit them before tagging starts.

| Axis | Expected effect | Why |
|---|---|---|
| Easy vs hard to verify | −0.15 | An agent that can run a check can try, fail and try again. Without one it stops at its first plausible answer. |
| Complete vs incomplete score | −0.10 | Agents optimise the stated score and miss what the task really wanted. |
| Well vs ill-structured | −0.10 | Agents are trained on tasks with a clear goal and a clear end. |
| Familiar vs novel to the solver | −0.10 | Novel tasks remove the patterns the model has seen many times. |
| Kind vs wicked feedback | −0.10 | Inside a run, slow or noisy feedback leaves the agent unable to learn which of its moves worked. |
| Stationary vs drifting | −0.05 | Few of these tasks change while the agent works, so the spread is small. |
| Reversible vs irreversible | −0.05 | Agents make careless early moves and can't undo them. |
| Decomposable vs tangled | −0.05 | Agents work step by step and lose track when the steps depend on each other. |
| Test vs watch | −0.05 | Being able to probe the system is a form of verification. |

## What I expect overall

- **Shortlist.** Between three and eight axes survive stability selection. Easy vs hard to verify is on it.
- **Untested.** The social axes barely vary on lab tasks: shared vs contested values, skin in the game, private vs accountable and yours to fix vs needs others. They should come back as untested, not as failures.
- **Tagger check.** Our tagging of METR's own 16 factors gives a slope between −0.04 and −0.12 per point. If it falls outside that range, the tagger is broken and nothing else counts.
- **Added value.** Our axes beat METR's messiness sum out of sample, but only a little. I expect a gain in R² of 0.02 to 0.08, because several axes overlap with METR's factors.

## What would change my mind

If no axis survives and the shuffle test fails, the axes are a dictionary for this kind of task. That doesn't make them useless elsewhere, but it does mean the README's claim that tagging pays off rests on METR's work, not ours.
