# Axes for sorting problems

* [Reading the axes](reading-the-axes.md): how the axes are grouped, what the correlation labels mean and what changes at the hard end.

# The world

## Randomness

* [Deterministic vs statistical](deterministic-vs-statistical.md)
  * **Deterministic**: the same inputs always give exactly the same output (e.g. a sum).
  * **Statistical**: the same inputs give different results each time, but the rate across many cases is steady (e.g. which boilers break down this winter).
* [Coherent vs incoherent](coherent-vs-incoherent.md)
  * **Coherent**: every run of the system gives the same spread of results, so the pooled average stands for any run (e.g. a die).
  * **Incoherent**: each run settles somewhere different, so the pooled average describes none of them (e.g. climate model runs that split into warm and cold futures).
* [Clustered vs scattered](clustered-vs-scattered.md)
  * **Clustered**: runs that disagree fall into a few clear groups, so a few clues tell you which one you are in (e.g. snowflakes are plates, columns or stars).
  * **Scattered**: runs that disagree spread out with no pattern to latch onto (e.g. where the shards land when a glass breaks).
* [Thin vs fat tails](thin-vs-fat-tails.md)
  * **Thin**: results stay close to the average, so the average tells you a lot (e.g. people's heights).
  * **Fat**: one extreme case can outweigh all the rest put together (e.g. floods or startup returns).

## Change

* [Smooth vs rugged](smooth-vs-rugged.md)
  * **Smooth**: a small change to the inputs makes a small change to the result, so roughly right is good enough (e.g. seasoning a soup).
  * **Rugged**: a small change can make a big difference, so an answer that looks almost right can be worth nothing (e.g. one wrong character in code).
* [Long vs short predictability horizon](long-vs-short-predictability-horizon.md)
  * **Long**: small errors in what you know today stay small, so you can forecast far ahead (e.g. the tides).
  * **Short**: tiny errors grow fast, so a forecast soon becomes useless (e.g. the weather two weeks out).
* [Stationary vs drifting](stationary-vs-drifting.md)
  * **Stationary**: the patterns in past data still hold today (e.g. gravity).
  * **Drifting**: the world keeps shifting, so what you learnt goes stale (e.g. fashion and slang).

## Response

* [Inert vs reflexive](inert-vs-reflexive.md)
  * **Inert**: the system behaves the same whether or not you model it (e.g. a rock).
  * **Reflexive**: your forecasts, scores or actions change what people do and so change the outcome (e.g. a forecast that a bank will fail sets off a run on it).
* [Neutral vs adversarial](neutral-vs-adversarial.md)
  * **Neutral**: the world doesn't care what you do (e.g. rain doesn't try to beat your umbrella).
  * **Adversarial**: someone studies your methods and changes their play to beat them (e.g. fraudsters).

## Structure

* [Decomposable vs tangled](decomposable-vs-tangled.md)
  * **Decomposable**: you can solve each part on its own and put them back together (e.g. a car engine).
  * **Tangled**: each part only makes sense in light of the others (e.g. a company culture).
* [Loose vs tight coupling](loose-vs-tight-coupling.md)
  * **Loose**: when one part fails there is slack and time to step in (e.g. the post, where one late parcel doesn't stop the rest).
  * **Tight**: a fault spreads to other parts before anyone can react (e.g. a power grid).
* [Tractable vs intractable search](tractable-vs-intractable-search.md)
  * **Tractable**: you know every option and there are few enough to check them all (e.g. noughts and crosses).
  * **Intractable**: you know every option, but there are too many for any computer to check (e.g. Go, with about 10¹⁷⁰ legal board positions).

# The knower

## Uncertainty

* [Known vs unknown odds](known-vs-unknown-odds.md)
  * **Known**: you can put a number you trust on each outcome (e.g. a dice roll).
  * **Unknown**: you know things are uncertain but can't say how likely each outcome is (e.g. whether a new technology takes off).
* [Reducible vs irreducible uncertainty](reducible-vs-irreducible-uncertainty.md)
  * **Reducible**: the facts that would settle your doubt exist and can be found (e.g. waiting on a blood test).
  * **Irreducible**: no amount of fact finding would settle it (e.g. whether a rival cuts prices next year).
* [Small vs large world](small-vs-large-world.md)
  * **Small**: a fixed procedure generates every way things might turn out, so you can compute or sample the outcomes before you choose, even when there are too many to list (e.g. a lottery ticket).
  * **Large**: no procedure generates the outcomes, so you can't sample them and the result could be something nobody thought to list (e.g. a new product hit by a change in the law).

## Evidence

* [Transparent vs opaque causes](transparent-vs-opaque-causes.md)
  * **Transparent**: you can follow how one thing leads to another and predict what a change will do (e.g. a lever).
  * **Opaque**: you can see every part but can't follow the whole chain (e.g. a large codebase).
* [Test vs watch](test-vs-watch.md)
  * **Test**: you can run a fair test where chance decides who gets what (e.g. a drug trial).
  * **Watch**: you can only watch what happens and guess at the cause (e.g. a study of nurses who chose hormone therapy).
* [Kind vs wicked feedback](kind-vs-wicked-feedback.md)
  * **Kind**: you find out soon and clearly whether you were right (e.g. a game of chess).
  * **Wicked**: feedback is slow, noisy or missing, so experience can teach the wrong lesson (e.g. a fund manager's results).
* [Plentiful vs scarce data](plentiful-vs-scarce-data.md)
  * **Plentiful**: there are many past cases like this one to learn from (e.g. card fraud).
  * **Scarce**: there are so few past cases that you have almost nothing to go on (e.g. a nuclear accident).

## Know-how

* [Explicit vs tacit know-how](explicit-vs-tacit-know-how.md)
  * **Explicit**: the know-how can be written down as rules (e.g. a tax rule).
  * **Tacit**: the know-how lives in experts' hands and gut feel, so it can only be learnt from examples (e.g. a nurse sensing a patient is about to crash).
* [Familiar vs novel to the solver](familiar-vs-novel-to-the-solver.md)
  * **Familiar**: the solver has met this kind of problem many times before (e.g. a doctor seeing a common cold).
  * **Novel**: the problem is new to the solver, even if others have solved it (e.g. a question outside a model's training data).
* [General vs local knowledge](general-vs-local-knowledge.md)
  * **General**: the answer rests on facts anyone could look up (e.g. how insulin works).
  * **Local**: the answer rests on facts that only people close to it know (e.g. whether this patient takes their insulin).

# The decision

## Goal

* [Well vs ill-structured](well-vs-ill-structured.md)
  * **Well-structured**: the problem is clearly stated, with a known goal, known moves and a clear end (e.g. a maths exam question).
  * **Ill-structured**: working out what the problem is, or how to attack it, becomes part of the job (e.g. "fix homelessness").
* [Convergent vs divergent](convergent-vs-divergent.md)
  * **Convergent**: there is one right answer that everyone would agree on (e.g. a sum).
  * **Divergent**: there are many good answers that differ in kind (e.g. a wedding speech).
* [Single vs multiple objectives](single-vs-multiple-objectives.md)
  * **Single**: there is one thing to get right (e.g. the fastest route home).
  * **Multiple**: several goals pull against each other, so a gain on one costs you on another (e.g. price against safety in a new car).
* [Satisficing vs optimising](satisficing-vs-optimising.md)
  * **Satisficing**: any answer that clears the bar will do (e.g. a lunch spot).
  * **Optimising**: each extra bit of quality still pays off, so you need the best you can find (e.g. the dose of a strong drug).
* [Easy vs hard to verify](easy-vs-hard-to-verify.md)
  * **Easy**: you can check an answer quickly and cheaply (e.g. a solved sudoku).
  * **Hard**: there is no quick or cheap way to check an answer before you act on it (e.g. a business strategy).
* [Complete vs incomplete score](complete-vs-incomplete-score.md)
  * **Complete**: the thing you measure captures everything you want (e.g. sorting letters by postcode).
  * **Incomplete**: some goals are left out because they are hard to write down (e.g. fairness in hiring).

## Options

* [Choose vs design the options](choose-vs-design-the-options.md)
  * **Choose**: the options are handed to you to pick from (e.g. a mortgage from a bank's list).
  * **Design**: you have to invent the options first (e.g. saving a dying high street).
* [Yours to fix vs needs others to change](yours-to-fix-vs-needs-others-to-change.md)
  * **Yours to fix**: you hold the levers yourself (e.g. a surgeon unblocking an artery).
  * **Needs others**: the fix depends on other people changing what they do (e.g. a patient giving up smoking).
* [Standalone vs sequential](standalone-vs-sequential.md)
  * **Standalone**: each choice stands alone, so one doesn't change the next (e.g. checking invoices for fraud).
  * **Sequential**: each choice shapes the next, so it is hard to tell which one caused the result (e.g. treating a long illness).
* [Slack vs time pressure](slack-vs-time-pressure.md)
  * **Slack**: you have time to gather facts and think before things change (e.g. a pension plan).
  * **Time pressure**: you must act in seconds or minutes (e.g. a pilot with a failed engine).

## Stakes

* [Reversible vs irreversible](reversible-vs-irreversible.md)
  * **Reversible**: if it goes wrong you can undo it cheaply and try again (e.g. a new recipe).
  * **Irreversible**: once it is done you are stuck with it (e.g. selling the family home).
* [Spread vs single bet](spread-vs-single-bet.md)
  * **Spread**: you can split your stake across several options at once, so no one choice has to be right (e.g. a pension fund holding many shares).
  * **Single bet**: you can only take one course of action, so everything rides on it (e.g. which job offer to accept).
* [Survivable vs ruinous](survivable-vs-ruinous.md)
  * **Survivable**: no single loss can knock you out, so good odds pay off over many tries (e.g. a casino taking many small bets).
  * **Ruinous**: one bad outcome can take you out of the game for good (e.g. Russian roulette).
* [Additive vs multiplicative](additive-vs-multiplicative.md)
  * **Additive**: gains and losses add up, so the average is what you can expect (e.g. betting the same £10 every round).
  * **Multiplicative**: gains and losses compound, so one player over time can do far worse than the average (e.g. betting half your savings every round).
* [Even vs lopsided errors](even-vs-lopsided-errors.md)
  * **Even**: a false alarm and a miss cost about the same (e.g. deciding whether to take an umbrella).
  * **Lopsided**: one mistake is far worse than the other (e.g. a smoke alarm that stays quiet in a fire).

## People

* [Shared vs contested values](shared-vs-contested-values.md)
  * **Shared**: everyone affected agrees on what a good result looks like (e.g. a bridge should stay up).
  * **Contested**: people want different things from the result (e.g. where to build the bridge).
* [Private vs accountable](private-vs-accountable.md)
  * **Private**: the choice is yours alone (e.g. picking a film).
  * **Accountable**: you must explain and defend the choice to others (e.g. a bank refusing a loan).
* [Skin in the game vs none](skin-in-the-game-vs-none.md)
  * **Skin in the game**: whoever makes the call bears the cost if it goes wrong (e.g. a shopkeeper pricing their own stock).
  * **None**: the cost lands on someone else (e.g. a broker paid for each loan whether or not it is repaid).
