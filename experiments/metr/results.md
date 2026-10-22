# METR retagging: results

Runs file: time horizon 1.1. SWAA and human runs dropped.

These runs used kind-vs-wicked-feedback. That axis has since been narrowed to [Immediate vs delayed feedback](../../axes/immediate-vs-delayed-feedback.md), so its rows here tag the old, wider idea.

## 0. Baseline: METR's time horizons from public data

Check these against METR's published numbers before trusting anything below.

| model | runs | horizon_minutes |
|---|---|---|
| Claude 3 Opus (Inspect) | 642 | 2.7 |
| GPT-4 Turbo (Inspect) | 636 | 3.1 |
| GPT-4 1106 (Inspect) | 633 | 3.2 |
| GPT-4 0314 | 873 | 3.4 |
| GPT-4o (Inspect) | 648 | 6.1 |
| Claude 3.5 Sonnet (Old) (Inspect) | 609 | 9.8 |
| Claude 3.5 Sonnet (New) (Inspect) | 620 | 19.5 |
| o1-preview | 1133 | 19.8 |
| o1 (Inspect) | 648 | 38.5 |
| Claude 3.7 Sonnet (Inspect) | 647 | 61.6 |
| Claude 4.1 Opus (Inspect) | 647 | 100.3 |
| Claude 4 Opus (Inspect) | 972 | 100.4 |
| o3 (Inspect) | 648 | 119.9 |
| GPT-5 (Inspect) | 660 | 203.0 |
| GPT-5.1-Codex-Max (Inspect) | 973 | 223.7 |
| Gemini 3 Pro | 648 | 224.6 |
| Claude Opus 4.5 (Inspect) | 648 | 292.1 |
| GPT-5.3-Codex | 1206 | 347.5 |
| GPT-5.2 | 697 | 350.4 |
| Claude Opus 4.6 (Inspect) | 995 | 673.3 |

## 1. Reliability

Raters: opus, opus-shuffled, sonnet. Axes go further only if no more than 50% of tags are n/a, alpha is at least 0.4 and the spread (sd) across tasks is at least 0.1.

| item | alpha | sd | na_rate | status |
|---|---|---|---|---|
| known-vs-unknown-odds | 1.000 | 0.164 | 0.952 | mostly n/a |
| long-vs-short-predictability-horizon | 1.000 | 0.152 | 0.948 | mostly n/a |
| plentiful-vs-scarce-data | 0.916 | 0.335 | 0.313 | kept |
| neutral-vs-adversarial | 0.895 | 0.330 | 0.000 | kept |
| deterministic-vs-statistical | 0.865 | 0.310 | 0.000 | kept |
| choose-vs-design-the-options | 0.840 | 0.374 | 0.048 | kept |
| explicit-vs-tacit-know-how | 0.807 | 0.296 | 0.000 | kept |
| convergent-vs-divergent | 0.805 | 0.198 | 0.000 | kept |
| survivable-vs-ruinous | 0.770 | 0.066 | 0.000 | untested here |
| loose-vs-tight-coupling | 0.753 | 0.200 | 0.393 | kept |
| inert-vs-reflexive | 0.751 | 0.087 | 0.000 | untested here |
| single-vs-multiple-objectives | 0.737 | 0.341 | 0.000 | kept |
| tractable-vs-intractable-search | 0.736 | 0.310 | 0.052 | kept |
| familiar-vs-novel-to-the-solver | 0.708 | 0.355 | 0.000 | kept |
| satisficing-vs-optimising | 0.702 | 0.425 | 0.000 | kept |
| decomposable-vs-tangled | 0.702 | 0.244 | 0.012 | kept |
| stationary-vs-drifting | 0.684 | 0.110 | 0.083 | kept |
| reversible-vs-irreversible | 0.668 | 0.179 | 0.000 | kept |
| smooth-vs-rugged | 0.648 | 0.208 | 0.008 | kept |
| kind-vs-wicked-feedback | 0.631 | 0.218 | 0.000 | kept |
| well-vs-ill-structured | 0.592 | 0.255 | 0.000 | kept |
| complete-vs-incomplete-score | 0.587 | 0.191 | 0.000 | kept |
| general-vs-local-knowledge | 0.579 | 0.323 | 0.000 | kept |
| transparent-vs-opaque-causes | 0.576 | 0.319 | 0.044 | kept |
| standalone-vs-sequential | 0.561 | 0.311 | 0.000 | kept |
| reducible-vs-irreducible-uncertainty | 0.554 | 0.120 | 0.000 | kept |
| test-vs-watch | 0.530 | 0.124 | 0.198 | kept |
| spread-vs-single-bet | 0.502 | 0.232 | 0.500 | kept |
| private-vs-accountable | 0.498 | 0.045 | 0.000 | untested here |
| easy-vs-hard-to-verify | 0.440 | 0.238 | 0.000 | kept |
| small-vs-large-world | 0.216 | 0.185 | 0.099 | unreliable |
| coherent-vs-incoherent | 0.181 | 0.079 | 0.790 | mostly n/a |
| slack-vs-time-pressure | 0.134 | 0.132 | 0.000 | unreliable |
| shared-vs-contested-values | -0.005 | 0.044 | 0.111 | untested here |
| skin-in-the-game-vs-none | -0.482 | 0.357 | 0.667 | mostly n/a |
| additive-vs-multiplicative | nan | 0.000 | 0.988 | mostly n/a |
| clustered-vs-scattered | nan | 0.139 | 0.964 | mostly n/a |
| even-vs-lopsided-errors | nan | 0.217 | 0.929 | mostly n/a |
| thin-vs-fat-tails | nan | 0.095 | 0.980 | mostly n/a |
| yours-to-fix-vs-needs-others-to-change | nan | 0.000 | 0.000 | untested here |

25 of 40 axes kept.

METR factors:

| item | alpha | na_rate |
|---|---|---|
| irreversible mistake availability | 0.867 | 0.000 |
| dynamic environment | 0.845 | 0.000 |
| not easily resettable | 0.801 | 0.000 |
| difficult counterfactuals | 0.788 | 0.000 |
| resource limited | 0.762 | 0.000 |
| is suboptimal behavior exploited | 0.747 | 0.000 |
| realtime coordination | 0.747 | 0.000 |
| information seeking required | 0.701 | 0.000 |
| novel situation | 0.692 | 0.000 |
| non explicit scoring description | 0.667 | 0.000 |
| implicit generalizability required and scored | 0.649 | 0.000 |
| self modification required | 0.498 | 0.000 |
| no provided verification mechanisms | 0.449 | 0.000 |
| real life source | 0.427 | 0.000 |
| not purely automatic scoring | 0.303 | 0.000 |
| self improvement required | nan | 0.000 |

## 2. Tagger check: METR's 16 factors, tagged by our pipeline

METR found a slope of -0.081 per point, controlling for log length.

| data | slope | 95% CI | r2 | tasks | mean sum |
|---|---|---|---|---|---|
| 1.0 runs, paper models | -0.029 | -0.074 to 0.016 | 0.567 | 89 | 3.640 |
| 1.1 runs, all models | -0.018 | -0.044 to 0.008 | 0.539 | 162 | 3.370 |
| 1.1 runs, full task text only | -0.085 | -0.151 to -0.019 | 0.717 | 23 | 2.696 |
| 1.1 runs, family summaries only | -0.015 | -0.040 to 0.011 | 0.528 | 139 | 3.482 |

METR's mean messiness was 3.2.

## 3. One axis at a time

Effect is the change in success rate, beyond what length predicts, from the easy end to the hard end. Errors are clustered by family. q is the p value after Benjamini Hochberg.

| axis | effect | lo | hi | p | q |
|---|---|---|---|---|---|
| easy-vs-hard-to-verify | -0.234 | -0.396 | -0.071 | 0.005 | 0.122 |
| test-vs-watch | -0.204 | -0.383 | -0.024 | 0.026 | 0.324 |
| spread-vs-single-bet | -0.143 | -0.300 | 0.013 | 0.073 | 0.609 |
| reversible-vs-irreversible | -0.206 | -0.478 | 0.067 | 0.139 | 0.633 |
| neutral-vs-adversarial | 0.073 | -0.024 | 0.170 | 0.140 | 0.633 |
| familiar-vs-novel-to-the-solver | -0.098 | -0.232 | 0.036 | 0.152 | 0.633 |
| convergent-vs-divergent | 0.124 | -0.090 | 0.338 | 0.257 | 0.917 |
| plentiful-vs-scarce-data | -0.078 | -0.234 | 0.077 | 0.324 | 0.961 |
| standalone-vs-sequential | -0.070 | -0.233 | 0.093 | 0.398 | 0.961 |
| general-vs-local-knowledge | -0.065 | -0.226 | 0.096 | 0.427 | 0.961 |
| smooth-vs-rugged | -0.082 | -0.291 | 0.126 | 0.438 | 0.961 |
| stationary-vs-drifting | -0.114 | -0.425 | 0.196 | 0.471 | 0.961 |
| loose-vs-tight-coupling | 0.057 | -0.141 | 0.255 | 0.572 | 0.961 |
| complete-vs-incomplete-score | 0.059 | -0.190 | 0.308 | 0.643 | 0.961 |
| tractable-vs-intractable-search | 0.027 | -0.111 | 0.166 | 0.698 | 0.961 |
| explicit-vs-tacit-know-how | 0.022 | -0.123 | 0.166 | 0.767 | 0.961 |
| deterministic-vs-statistical | -0.018 | -0.175 | 0.138 | 0.817 | 0.961 |
| kind-vs-wicked-feedback | -0.022 | -0.204 | 0.161 | 0.817 | 0.961 |
| single-vs-multiple-objectives | -0.017 | -0.163 | 0.130 | 0.824 | 0.961 |
| well-vs-ill-structured | -0.017 | -0.189 | 0.154 | 0.844 | 0.961 |
| decomposable-vs-tangled | 0.016 | -0.170 | 0.201 | 0.869 | 0.961 |
| choose-vs-design-the-options | 0.008 | -0.108 | 0.124 | 0.896 | 0.961 |
| transparent-vs-opaque-causes | 0.008 | -0.139 | 0.154 | 0.918 | 0.961 |
| satisficing-vs-optimising | -0.003 | -0.116 | 0.109 | 0.953 | 0.961 |
| reducible-vs-irreducible-uncertainty | 0.006 | -0.253 | 0.266 | 0.961 | 0.961 |

## 4. All together: the shortlist

Stability selection on the 25 kept axes. On each of 200 random halves of the families, the first 8 axes to enter the lasso are kept. kept_share is how often each axis was kept. The shortlist is every axis kept in at least 80% of halves. Expect at most 4.3 noise axes on it. lasso_coef_sd is the full data lasso coefficient per standard deviation, for the sign.

| axis | lasso_coef_sd | kept_share |
|---|---|---|
| easy-vs-hard-to-verify | -0.013 | 0.845 |
| familiar-vs-novel-to-the-solver | -0.000 | 0.635 |
| deterministic-vs-statistical | -0.000 | 0.570 |
| neutral-vs-adversarial | 0.000 | 0.565 |
| reversible-vs-irreversible | -0.000 | 0.495 |
| loose-vs-tight-coupling | 0.000 | 0.465 |
| stationary-vs-drifting | -0.000 | 0.365 |
| complete-vs-incomplete-score | 0.000 | 0.340 |
| spread-vs-single-bet | -0.000 | 0.325 |
| satisficing-vs-optimising | 0.000 | 0.300 |
| test-vs-watch | -0.000 | 0.300 |
| reducible-vs-irreducible-uncertainty | 0.000 | 0.290 |
| smooth-vs-rugged | -0.000 | 0.265 |
| transparent-vs-opaque-causes | 0.000 | 0.255 |
| convergent-vs-divergent | 0.000 | 0.250 |
| kind-vs-wicked-feedback | 0.000 | 0.240 |
| general-vs-local-knowledge | -0.000 | 0.235 |
| decomposable-vs-tangled | 0.000 | 0.230 |
| plentiful-vs-scarce-data | -0.000 | 0.210 |
| tractable-vs-intractable-search | 0.000 | 0.200 |
| single-vs-multiple-objectives | -0.000 | 0.190 |
| standalone-vs-sequential | -0.000 | 0.190 |
| well-vs-ill-structured | -0.000 | 0.090 |
| choose-vs-design-the-options | 0.000 | 0.085 |
| explicit-vs-tacit-know-how | 0.000 | 0.065 |

Shortlist: easy-vs-hard-to-verify.

## 5. Added value over METR's messiness sum

Out of sample R² for the residual (success beyond length), holding out one family at a time. Zero means no better than guessing the average.

| model | logo_r2 |
|---|---|
| METR messiness sum | -0.056 |
| Our axes (elastic net) | -0.018 |
| Messiness sum + our axes | -0.017 |

## 6. Shuffle test

Real tags: R² -0.415. Tags shuffled across families 1000 times: mean -0.291, 95th percentile -0.030. p = 0.773.
