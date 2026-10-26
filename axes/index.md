# Axes for sorting problems

* [Reading the axes](README.md): how the axes are grouped, how to read one and what to do when a problem sits at the hard end.

# Environment

## Randomness

* [Deterministic vs stochastic](deterministic-vs-stochastic.md)
  * **Deterministic**: the same inputs always give exactly the same output (e.g. a sum).
  * **Stochastic**: the same inputs give different results each time, but the rate across many cases is steady (e.g. which boilers break down this winter).
* [Coherent vs incoherent runs](coherent-vs-incoherent-runs.md)
  * **Coherent runs**: every run of the system gives the same spread of results, so the pooled average stands for any run (e.g. a die).
  * **Incoherent runs**: each run settles somewhere different, so the pooled average describes none of them (e.g. climate model runs that split into warm and cold futures).
* [Clustered vs scattered runs](clustered-vs-scattered-runs.md)
  * **Clustered runs**: runs that disagree fall into a few clear groups, so a few clues tell you which one you are in (e.g. snowflakes are plates, columns or stars).
  * **Scattered runs**: runs that disagree spread out with no pattern to latch onto (e.g. where the shards land when a glass breaks).
* [Thin vs fat tails](thin-vs-fat-tails.md)
  * **Thin tails**: results stay close to the average, so the average tells you a lot (e.g. people's heights).
  * **Fat tails**: one extreme case can outweigh all the rest put together (e.g. floods or startup returns).

## Change

* [Stable vs chaotic](stable-vs-chaotic.md)
  * **Lyapunov stable**: small errors in what you know today stay small, so you can forecast far ahead (e.g. the tides).
  * **Chaotic**: tiny errors grow fast, so a forecast soon becomes useless (e.g. the weather two weeks out).
* [Durable vs perishable lessons](durable-vs-perishable-lessons.md)
  * **Durable lessons**: the patterns in past data still hold today, so what you learnt keeps working (e.g. gravity).
  * **Perishable lessons**: the world keeps shifting, so what you learnt goes stale (e.g. fashion and slang).
* [Static vs dynamic](static-vs-dynamic.md)
  * **Static world**: the world waits while you act, so a plan made at the start holds to the end (e.g. a crossword).
  * **Dynamic world**: the world changes while you act, even if you do nothing, so you have to watch and adjust as you go (e.g. returning a tennis serve).

## Stimulus

* [Self-righting vs tipping](self-righting-vs-tipping.md)
  * **Self-righting**: after a push the system goes back to where it was, like a ball in a bowl (e.g. body temperature).
  * **Malleable** (the middle): the system stays wherever it is pushed, like a ball on a flat table (e.g. a Word document).
  * **Tipping point**: past some push the system flips into a new state and stays there, like a ball on a hilltop (e.g. a clear lake turning murky).
* [Antifragile vs wears out](antifragile-vs-wears-out.md)
  * **Antifragile**: each stress leaves the system stronger than before, up to a point (e.g. a muscle after a workout).
  * **Robust** (the middle): stress leaves the system the same (e.g. a computer program, which is the same after a billion runs).
  * **Wears out**: each stress uses up some of the system's life, until it fails (e.g. metal fatigue in an aircraft).
* [Loose vs tight coupling](loose-vs-tight-coupling.md)
  * **Loose coupling**: when one part fails there is slack and time to step in (e.g. the post, where one late parcel doesn't stop the rest).
  * **Tight coupling**: a fault spreads to other parts before anyone can react (e.g. a power grid).

## Reactivity

* [Inert vs reflexive](inert-vs-reflexive.md)
  * **Inert**: the system behaves the same whether or not you model it (e.g. a rock).
  * **Reflexive**: putting out a forecast or score changes the thing it describes, because people act on it, even though nobody is trying to beat you (e.g. a forecast that a bank will fail sets off the run that sinks it).
* [Neutral vs adversarial](neutral-vs-adversarial.md)
  * **Neutral**: nobody is looking for the gaps in your rule, so the cases you meet are a fair sample and your errors land where chance puts them (e.g. rain doesn't try to beat your umbrella).
  * **Adversarial**: someone whose goals differ from yours studies your rule, finds the cases it gets wrong and sends you more of them (e.g. fraudsters probing a bank's fraud checks).

## Structure

* [Decomposable vs tangled](decomposable-vs-tangled.md)
  * **Decomposable**: you can solve each part on its own and put them back together (e.g. a car engine).
  * **Tangled**: each part only makes sense in light of the others (e.g. a company culture).
* [Smooth vs rugged](smooth-vs-rugged.md)
  * **Smooth landscape**: a small change to the inputs makes a small change to the result, so roughly right is good enough (e.g. seasoning a soup).
  * **Rugged landscape**: a small change can make a big difference, so an answer that looks almost right can be worth nothing (e.g. one wrong character in code).
* [Tractable vs intractable search](tractable-vs-intractable-search.md)
  * **Tractable search**: you know every option and there are few enough to check them all (e.g. noughts and crosses).
  * **Intractable search**: you know every option, but there are too many for any computer to check (e.g. Go, with about 10¹⁷⁰ legal board positions).

# Information

## Uncertainty

* [Risk vs Knightian uncertainty](risk-vs-knightian-uncertainty.md)
  * **Measurable risk**: you can put a number you trust on each outcome (e.g. a dice roll).
  * **Knightian uncertainty**: you know things are uncertain but can't say how likely each outcome is (e.g. whether a new technology takes off).
* [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md)
  * **Reducible uncertainty**: the facts that would settle your doubt exist and can be found (e.g. waiting on a blood test).
  * **Irreducible uncertainty**: no amount of fact finding would settle it (e.g. whether a rival cuts prices next year).
* [Small vs large world](small-vs-large-world.md)
  * **Small world**: a fixed procedure generates every way things might turn out, so you can compute or sample the outcomes before you choose, even when there are too many to list (e.g. a lottery ticket).
  * **Large world**: no procedure generates the outcomes, so you can't sample them and the result could be something nobody thought to list (e.g. a new product hit by a change in the law).

## Evidence

* [Transparent vs opaque causes](transparent-vs-opaque-causes.md)
  * **Transparent causes**: you can follow how one thing leads to another and predict what a change will do (e.g. a lever).
  * **Opaque causes**: you can see every part but can't follow the whole chain (e.g. a trained neural network).
* [Interventional vs observational](interventional-vs-observational.md)
  * **Interventional**: you can set the cause yourself and let chance decide who gets it (e.g. a drug trial).
  * **Observational**: people's own choices or nature set the cause, so you can only watch what follows and guess (e.g. a study of nurses who chose hormone therapy).
* [Symmetric vs asymmetric information](symmetric-vs-asymmetric-information.md)
  * **Symmetric information**: everyone in the deal sees the same facts (e.g. a game of chess).
  * **Asymmetric information**: the other side knows things you don't and chooses what reaches you (e.g. buying a used car).
* [Plentiful vs scarce data](plentiful-vs-scarce-data.md)
  * **Plentiful data**: there are many past cases like this one to learn from (e.g. card fraud).
  * **Scarce data**: there are so few past cases that you have almost nothing to go on (e.g. a nuclear accident).
* [Verifiable vs unverifiable](verifiable-vs-unverifiable.md)
  * **Verifiable**: you can check an answer quickly and cheaply before you act on it (e.g. a solved sudoku).
  * **Unverifiable**: checking an answer costs about as much as finding it, or more, so in practice you can't check it before you act (e.g. a business strategy).
* [Immediate vs delayed feedback](immediate-vs-delayed-feedback.md)
  * **Immediate feedback**: you find out soon whether you were right (e.g. throwing darts).
  * **Delayed feedback**: the result arrives years later or never, so you get few chances to learn (e.g. planting an orchard).

# Actions

## Options

* [Given vs invented options](given-vs-invented-options.md)
  * **Given options**: the options are handed to you to pick from (e.g. a mortgage from a bank's list).
  * **Invented options**: you have to invent the options first (e.g. saving a dying high street).
* [Diversifiable vs single bet](diversifiable-vs-single-bet.md)
  * **Diversifiable**: you can split your stake across several options at once, so no one choice has to be right (e.g. a pension fund holding many shares).
  * **Single bet**: you can only take one course of action, so everything rides on it (e.g. which job offer to accept).
* [Standalone vs sequential](standalone-vs-sequential.md)
  * **Standalone**: each choice stands alone, so one doesn't change the next (e.g. checking invoices for fraud).
  * **Sequential**: each choice shapes the next, so it is hard to tell which one caused the result (e.g. treating a long illness).

## Control

* [Reversible vs irreversible](reversible-vs-irreversible.md)
  * **Reversible**: if it goes wrong you can undo it cheaply and try again (e.g. a new recipe).
  * **Irreversible**: once it is done you are stuck with it (e.g. selling the family home).
* [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md)
  * **Yours to fix**: you hold the levers yourself (e.g. a surgeon unblocking an artery).
  * **Needs others to change**: the fix depends on other people changing what they do (e.g. a patient giving up smoking).
* [Ample time vs time pressure](ample-time-vs-time-pressure.md)
  * **Ample time**: you have time to gather facts and think before things change (e.g. a pension plan).
  * **Time pressure**: you must act in seconds or minutes (e.g. a pilot with a failed engine).

# Performance

## Goal

* [Well vs ill-structured](well-vs-ill-structured.md)
  * **Well-structured**: the problem is clearly stated, with a known goal, known moves and a clear end (e.g. a maths exam question).
  * **Ill-structured**: working out what the problem is, or how to attack it, becomes part of the job (e.g. \"fix homelessness\").
* [Convergent vs divergent](convergent-vs-divergent.md)
  * **Convergent**: the good answers sit together, so a blend of two good ones is also good (e.g. a sum, or a phone trading battery life for size).
  * **Divergent**: the good answers differ in kind, so halfway between two is worse than either (e.g. a funny wedding speech and a moving one).
* [Single objective vs trade-offs](single-objective-vs-trade-offs.md)
  * **Single objective**: there is one thing to get right (e.g. the fastest route home).
  * **Trade-offs**: several goals pull against each other, so a gain on one costs you on another (e.g. price against safety in a new car).
* [Shared vs contested values](shared-vs-contested-values.md)
  * **Shared values**: everyone affected ranks the possible results the same way, or one person owns the choice (e.g. a bridge should stay up).
  * **Contested values**: the people affected rank the results differently, and nobody has the standing to settle it alone (e.g. where to build the bridge).
* [Satisficing vs optimising](satisficing-vs-optimising.md)
  * **Satisficing**: any answer that clears the bar will do (e.g. a lunch spot).
  * **Optimising**: each extra bit of quality still pays off, so you need the best you can find (e.g. the dose of a strong drug).
* [Direct vs proxy measure](direct-vs-proxy-measure.md)
  * **Direct measure**: the thing you measure is everything you want (e.g. sorting letters by postcode).
  * **Proxy measure**: the thing you measure stands in for what you want and leaves out goals that are hard to write down (e.g. fairness in hiring).
* [Curable vs chronic](curable-vs-chronic.md)
  * **Curable**: there is a point where the problem is solved and you can stop (e.g. wiping out smallpox).
  * **Chronic**: there is no solved state, only a level you have to keep up (e.g. keeping malaria down).

## Stakes

* [Survivable vs ruinous](survivable-vs-ruinous.md)
  * **Survivable**: no single loss can knock you out, so good odds pay off over many tries (e.g. a casino taking many small bets).
  * **Ruinous**: one bad outcome can take you out of the game for good (e.g. Russian roulette).
* [Additive vs multiplicative returns](additive-vs-multiplicative-returns.md)
  * **Additive returns**: gains and losses add up, so the average is what you can expect (e.g. betting the same £10 every round).
  * **Multiplicative returns**: gains and losses compound, so one player over time can do far worse than the average (e.g. betting half your savings every round).
* [Even vs lopsided mistakes](even-vs-lopsided-mistakes.md)
  * **Even mistakes**: a false alarm and a miss cost about the same (e.g. deciding whether to take an umbrella).
  * **Lopsided mistakes**: one mistake is far worse than the other, whether it lets in a harm or lets a prize slip (e.g. a smoke alarm that stays quiet in a fire, or an investor who passes on the next Google).
* [Winnable vs no-win](winnable-vs-no-win.md)
  * **Winnable**: a clean win is possible, so you can come out ahead (e.g. proving a famous theorem).
  * **No-win**: even the best outcome is a loss, so the job is to lose less (e.g. landing a plane with engine failure).

# Agent

## Know-how

* [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md)
  * **Explicit know-how**: the know-how can be written down as rules (e.g. a tax rule).
  * **Tacit know-how**: the know-how lives in experts' hands and gut feel, so it can only be learnt from examples (e.g. a nurse sensing a patient is about to crash).
* [Bounded vs open-ended skill](bounded-vs-open-ended-skill.md)
  * **Bounded skill**: the know-how is a small, closed set that anyone competent masters fully (e.g. the alphabet).
  * **Open-ended skill**: the know-how has no ceiling, so solvers keep improving and differ widely (e.g. knowing which research questions are worth asking).
* [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md)
  * **Familiar to the solver**: the solver has met this kind of problem many times before (e.g. a doctor seeing a common cold).
  * **Novel to the solver**: the problem is new to the solver, even if others have solved it (e.g. a question outside a model's training data).
* [General vs local knowledge](general-vs-local-knowledge.md)
  * **General knowledge**: the answer rests on facts anyone could look up (e.g. how insulin works).
  * **Local knowledge**: the answer rests on facts that only people close to it know (e.g. whether this patient takes their insulin).

## Incentives

* [Skin in the game vs none](skin-in-the-game-vs-none.md)
  * **Skin in the game**: whoever makes the call bears the cost if it goes wrong (e.g. a shopkeeper pricing their own stock).
  * **No skin in the game**: the cost lands on someone else (e.g. a broker paid for each loan whether or not it is repaid).
* [Private vs accountable](private-vs-accountable.md)
  * **Private choice**: the choice is yours alone (e.g. picking a film).
  * **Accountable choice**: you must explain and defend the choice to others (e.g. a bank refusing a loan).
