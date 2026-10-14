# Axes for sorting problems

Each axis is a scale with two ends, and any problem sits somewhere along it. They fall into three groups. The first is about the world you act on. The second is about what you can know about it. The third is about the decision itself, what it needs and what it costs to get wrong.

The Correlated with list under each axis names the other axes it tends to move with. On every axis the first end is the easy one and the second is the hard one. So "correlated" means a problem near the hard end of one axis tends to sit near the hard end of the other. A few entries say "opposite" when the hard end of one goes with the easy end of the other. "Tension" marks two hard ends that clash when they meet, and "independent" marks two axes that look linked but aren't.

Each entry also says where the link comes from. "By definition" means one axis is partly built into the other, so tagging both may count the same thing twice. "Bundled" means a framework puts both under one label. "Study" means there is evidence or a worked case showing them together. "Logic" means it follows from what the two axes mean.

Under each axis, the actions say what to do differently at each end, with the easy end first. Each one opens with a plain rule that holds for anyone. A list then says what that rule means when you build or deploy an AI model, since that is the main use of this project. The section after the axes pulls out the pattern the actions share.

## All axes

Each name links to its section below.

| Axis | Group | Easy end | Hard end |
| --- | --- | --- | --- |
| [Deterministic vs statistical](#deterministic-vs-statistical) | World | Deterministic | Statistical |
| [Thin vs fat tails](#thin-vs-fat-tails) | World | Thin | Fat |
| [Smooth vs rugged](#smooth-vs-rugged) | World | Smooth | Rugged |
| [Long vs short predictability horizon](#long-vs-short-predictability-horizon) | World | Long | Short |
| [Stationary vs drifting](#stationary-vs-drifting) | World | Stationary | Drifting |
| [Inert vs reflexive](#inert-vs-reflexive) | World | Inert | Reflexive |
| [Neutral vs adversarial](#neutral-vs-adversarial) | World | Neutral | Adversarial |
| [Decomposable vs holistic](#decomposable-vs-holistic) | World | Decomposable | Holistic |
| [Loose vs tight coupling](#loose-vs-tight-coupling) | World | Loose | Tight |
| [Tractable vs intractable search](#tractable-vs-intractable-search) | World | Tractable | Intractable |
| [Discrete vs continuous](#discrete-vs-continuous) | World | Discrete | Continuous |
| [Known vs unknown odds](#known-vs-unknown-odds) | Knower | Known | Unknown |
| [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) | Knower | Reducible | Irreducible |
| [Small vs large world](#small-vs-large-world) | Knower | Small | Large |
| [Full vs partial observability](#full-vs-partial-observability) | Knower | Full | Partial |
| [Transparent vs opaque causes](#transparent-vs-opaque-causes) | Knower | Transparent | Opaque |
| [Test vs watch](#test-vs-watch) | Knower | Test | Watch |
| [Kind vs wicked feedback](#kind-vs-wicked-feedback) | Knower | Kind | Wicked |
| [Plentiful vs scarce data](#plentiful-vs-scarce-data) | Knower | Plentiful | Scarce |
| [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) | Knower | Explicit | Tacit |
| [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) | Knower | Familiar | Novel |
| [General vs local knowledge](#general-vs-local-knowledge) | Knower | General | Local |
| [Well-posed vs ill-posed](#well-posed-vs-ill-posed) | Decision | Well-posed | Ill-posed |
| [Choose vs design the options](#choose-vs-design-the-options) | Decision | Choose | Design |
| [Convergent vs divergent](#convergent-vs-divergent) | Decision | Convergent | Divergent |
| [Single vs multiple objectives](#single-vs-multiple-objectives) | Decision | Single | Multiple |
| [Shared vs contested values](#shared-vs-contested-values) | Decision | Shared | Contested |
| [Commensurable vs incommensurable values](#commensurable-vs-incommensurable-values) | Decision | Commensurable | Incommensurable |
| [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) | Decision | Yours to fix | Needs others |
| [Satisficing vs optimising](#satisficing-vs-optimising) | Decision | Satisficing | Optimising |
| [Easy vs hard to verify](#easy-vs-hard-to-verify) | Decision | Easy | Hard |
| [Complete vs incomplete goal](#complete-vs-incomplete-goal) | Decision | Complete | Incomplete |
| [One-shot vs sequential](#one-shot-vs-sequential) | Decision | One-shot | Sequential |
| [Reversible vs irreversible](#reversible-vs-irreversible) | Decision | Reversible | Irreversible |
| [Survivable vs ruinous](#survivable-vs-ruinous) | Decision | Survivable | Ruinous |
| [Additive vs multiplicative](#additive-vs-multiplicative) | Decision | Additive | Multiplicative |
| [Convex vs concave payoff](#convex-vs-concave-payoff) | Decision | Convex | Concave |
| [Even vs lopsided errors](#even-vs-lopsided-errors) | Decision | Even | Lopsided |
| [Slack vs time pressure](#slack-vs-time-pressure) | Decision | Slack | Time pressure |
| [Private vs accountable](#private-vs-accountable) | Decision | Private | Accountable |
| [Skin in the game vs none](#skin-in-the-game-vs-none) | Decision | Skin in the game | None |

## The world

These describe the system, whoever is looking at it.

### Deterministic vs statistical

Do the same inputs always give the same result, or only a stable spread of results? A sum is deterministic. Which boiler breaks down this winter is statistical, though the rate across many boilers is steady.

**Deterministic**: Write the rule down and test it like code.
- Don't ask a model to guess at a rule you could state. A rule that is right most of the time is a bug.
- Use the model to draft the rule or the code, then check that against tests. The tests decide if it ships, not the model.
- Test for exact output. The same input should give the same answer every run, so any variation is a fault to fix.

**Statistical**: Judge the spread, not single cases.
- Evaluate on a large held-out set. A few good examples tell you nothing when any one case can go either way.
- Report error rates and calibration. Calibration means that when the model says 70%, it is right about 70% of the time.
- Decide as a policy over many cases. Ask what rule gives the best results across the whole group, not what suits this one.
- Don't judge the model on one bad outcome. A right call can still lose, so look at the rate across many calls.

**Sources.** [Simplicity, disorganised complexity and organised complexity](frameworks/1948-simplicity-disorganised-and-organised-complexity.md), [Clocks and clouds](frameworks/1966-clocks-and-clouds.md), [Task environment properties](frameworks/1995-task-environment-properties.md)

**Correlated with**

- [Long vs short predictability horizon](#long-vs-short-predictability-horizon) (bundled). [Clocks and clouds](frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end, though chaos shows a fully deterministic system can still have a short horizon.
- [Full vs partial observability](#full-vs-partial-observability) (logic). Russell and Norvig note that a deterministic world you can only half see looks random to you ([Task environment properties](frameworks/1995-task-environment-properties.md)).
- [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) (logic). Pure chance is one kind of doubt that no new data can shrink.
- [Thin vs fat tails](#thin-vs-fat-tails) (by definition). The tails axis only applies once a problem is statistical. A deterministic problem has no spread of results, so it has no tails to speak of.

### Thin vs fat tails

When results are statistical, how extreme can a single one get? Heights are thin tailed, so the average tells you a lot. Floods, pandemics and startup returns are fat tailed, so one outlier can outweigh everything else and past averages mislead you.

**Thin**: Trust the average.
- Use mean error on a test set as your guide. With thin tails a few odd cases won't change the picture.
- Size the test set by the usual rules. A few thousand cases pin the average down well, because no single case can drag it far.

**Fat**: Plan around the worst case, not the average.
- Report tail metrics, like the worst 1% of errors or the largest single loss. A good average on a calm test set tells you nothing about the next crash.
- Stress test with extreme cases you build on purpose. The real extremes are too rare to turn up in your data by chance.
- Cap exposure with limits on size or spend. No single prediction should be able to do unbounded harm.
- Don't read a long calm run as proof of safety. Banks in 2007 had years of quiet data, and it said nothing about 2008.

**Sources.** [Mediocristan vs Extremistan](frameworks/2007-mediocristan-vs-extremistan.md), [Fourth quadrant](frameworks/2008-fourth-quadrant.md)

**Correlated with**

- [Deterministic vs statistical](#deterministic-vs-statistical) (by definition). This axis sits inside that one. It only applies near the statistical end, because a deterministic problem has no spread to have tails.
- [Survivable vs ruinous](#survivable-vs-ruinous) (bundled). The [Fourth quadrant](frameworks/2008-fourth-quadrant.md) and [Ergodicity](frameworks/2016-ergodicity.md) both warn that one extreme outcome can end the game.
- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (logic). The events that matter most in a fat tailed world are rare, so your record holds few of them or none. But card fraud is fat tailed and still has millions of cases. Fat tails make the cases that matter rare, not the data overall.
- [Known vs unknown odds](#known-vs-unknown-odds) (logic). Tail odds can't be read off a calm past, which is how banks in 2008 came to treat [uncertainty as risk](frameworks/1921-risk-vs-uncertainty.md).
- [Loose vs tight coupling](#loose-vs-tight-coupling) (study). In [Normal accidents](frameworks/1984-normal-accidents.md) small faults cascade through a tight system into huge losses.
- [Inert vs reflexive](#inert-vs-reflexive) (study). [Reflexivity](frameworks/1987-reflexivity.md) and the [bank run](frameworks/1948-self-fulfilling-prophecy.md) show beliefs and facts feeding each other into booms and crashes.
- [Additive vs multiplicative](#additive-vs-multiplicative) (logic). Compounding piles the gains on a lucky few. In Peters' coin game the crowd's average keeps rising only because a handful of players get vastly rich ([Ergodicity](frameworks/2016-ergodicity.md)).
- [Small vs large world](#small-vs-large-world) (logic). The worst outcomes are often ones nobody listed, which is what Taleb means by a black swan.
- [Convex vs concave payoff](#convex-vs-concave-payoff) (bundled). The [Fourth quadrant](frameworks/2008-fourth-quadrant.md) is a fat tailed world met with a payoff whose shape you don't understand. You can't change the tails, but you can often change your exposure to them.

### Smooth vs rugged

Can small steps carry you to the best answer, or will they get stuck? On a smooth problem every step that helps also brings you closer to the best answer, so steady tweaking works. On a rugged one there are many local peaks, and small steps stop on whichever is nearest. Seasoning a soup to taste is smooth. Designing a new protein is rugged, because changing one part changes what every other part is worth.

**Smooth**: Tweak and climb.
- Keep small changes to prompts, features or settings that help. On smooth ground each gain is a step towards the best answer.
- Use plain gradient methods or greedy search. They will get you near the top without anything fancier.

**Rugged**: Search wide before you search deep.
- Start from many different points. Restarts and population methods such as evolutionary search stop one bad start from deciding the result.
- Keep some poor looking candidates alive. A weak design today may sit at the foot of a much higher peak.
- Don't read a plateau as the top. When progress stops, try a big jump before you decide you're done.
- Pair a model that proposes many candidates with a separate scorer that picks among them. The model supplies the range and the scorer supplies the judgement.

**Sources.** [Convex vs non-convex optimisation](frameworks/1970-convex-vs-non-convex-optimisation.md), [Rugged fitness landscapes](frameworks/1987-rugged-fitness-landscapes.md)

**Correlated with**

- [Decomposable vs holistic](#decomposable-vs-holistic) (study). In Kauffman's NK model ([Rugged fitness landscapes](frameworks/1987-rugged-fitness-landscapes.md)) the land gets more rugged as each part depends on more of the others. If every part adds to the score on its own, there is only one peak.
- [Tractable vs intractable search](#tractable-vs-intractable-search) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Satisficing vs optimising](#satisficing-vs-optimising) (tension). Needing the best answer on rugged land is the worst case, because small steps stop on the nearest peak.
- [Long vs short predictability horizon](#long-vs-short-predictability-horizon) (independent). They sound alike but ask different things. Rugged is about many peaks among the possible answers. The horizon is about small errors growing over time. A rugged design problem can give each design a fixed score that never drifts.

### Long vs short predictability horizon

How far ahead does a forecast hold before small errors blow up? A cup pushed off a table is easy to predict. The weather two weeks out is not, even though the physics is simple. This is called chaos.

**Long**: Forecast and plan.
- Act on a point forecast. It holds well enough to schedule and commit ahead.
- Check the horizon now and then. Measure how accuracy falls with distance, so you notice if it starts to shrink.

**Short**: Forecast only as far as it holds, then forecast again.
- Find the horizon first. Plot forecast error against how far ahead you look, and stop where it is no better than a naive guess.
- Report a spread of outcomes instead of one number. Running a model further out than its horizon gives you confident noise.
- Judge the model on short range accuracy. A score that blends near and far forecasts hides where it stops working.
- Act in small steps and update as new data arrives. Weather services rerun their models several times a day for this reason.

**Sources.** [Sensitive dependence (chaos)](frameworks/1963-sensitive-dependence-chaos.md), [Clocks and clouds](frameworks/1966-clocks-and-clouds.md)

**Correlated with**

- [Deterministic vs statistical](#deterministic-vs-statistical) (bundled). [Clocks and clouds](frameworks/1966-clocks-and-clouds.md) puts chance and unpredictability at the same cloud end.
- [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) (logic). Past the horizon more data barely moves the forecast, so forecasters report a spread instead ([Sensitive dependence](frameworks/1963-sensitive-dependence-chaos.md)).
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (study). Weather forecasters work inside the horizon and are well calibrated ([Task characteristics of expertise](frameworks/1992-task-characteristics-of-expertise.md)). Tetlock's pundits made long range calls and did little better than chance ([Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)).
- [Smooth vs rugged](#smooth-vs-rugged) (independent). They sound alike. The horizon is about small errors growing over time, while rugged is about many local peaks among the possible answers.

### Stationary vs drifting

Do the lessons you learn today still hold next year? Gravity stays put. Music tastes, fashion and slang keep moving, so old data goes stale.

**Stationary**: Train once and monitor lightly.
- Trust last year's test set. In a stable world it predicts this year well.
- Use a slow release cycle. Retraining often costs effort and buys you little.

**Drifting**: Plan for the model to go stale.
- Test on the most recent slice of time, not a random split. A random split leaks the future into training and flatters the model.
- Weight recent data more heavily than old. The older a case, the less it says about today.
- Watch live inputs for drift. Compare what the model sees now with what it was trained on, and raise an alert when they part.
- Retrain on a schedule, and budget for it from the start. A model that was right at launch will go wrong later without anyone touching it.

**Sources.** [VUCA](frameworks/1987-vuca.md), [Task characteristics of expertise](frameworks/1992-task-characteristics-of-expertise.md), [Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)

**Correlated with**

- [Inert vs reflexive](#inert-vs-reflexive) (study). The [Lucas critique](frameworks/1976-lucas-critique.md) shows patterns break once people react to policy built on them, so a reflexive system drifts by its own doing.
- [Neutral vs adversarial](#neutral-vs-adversarial) (logic). Opponents learn your method and change their play, so last year's patterns stop working.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (study). [Shanteau](frameworks/1992-task-characteristics-of-expertise.md) and [Kahneman and Klein](frameworks/2009-conditions-for-intuitive-expertise.md) both need a stable, regular setting before experience turns into skill.
- [Known vs unknown odds](#known-vs-unknown-odds) (logic). [Knight](frameworks/1921-risk-vs-uncertainty.md)'s uncertainty starts where the future may not look like the past.
- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (logic). A drifting world keeps serving up cases nobody has seen.
- [Small vs large world](#small-vs-large-world) (logic). A drifting world keeps adding states nobody listed.
- [General vs local knowledge](#general-vs-local-knowledge) (logic). Hayek's point was that local circumstances change every day ([Use of knowledge in society](frameworks/1945-use-of-knowledge-in-society.md)).

### Inert vs reflexive

Does looking at the system, or acting on your forecast, change it? A rock doesn't care if you measure it. Publish a forecast that a bank will fail and people pull their money out, which makes it fail.

**Inert**: Measure and act freely.
- Learn from logged data. Your forecast won't change the thing you forecast, so the logs are a fair record.
- Publish scores and forecasts openly. Nobody can game a rock.

**Reflexive**: Expect your model to change the world it was trained on.
- Hold back a small random group the model doesn't act on. It shows you what would have happened without the model.
- Watch for feedback loops. A recommender that only learns from what it chose to show will narrow until it shows the same few things.
- Expect people to game any score they are judged on. Keep some of the inputs private and change the score now and then.
- Retrain with care. Data collected after launch carries the model's own effect, so it is no longer a clean picture of the world.

**Sources.** [Keynesian beauty contest](frameworks/1936-keynesian-beauty-contest.md), [Self-fulfilling prophecy](frameworks/1948-self-fulfilling-prophecy.md), [Goodhart's law](frameworks/1975-goodharts-law.md), [Campbell's law](frameworks/1976-campbells-law.md), [Lucas critique](frameworks/1976-lucas-critique.md), [Reflexivity](frameworks/1987-reflexivity.md)

**Correlated with**

- [Thin vs fat tails](#thin-vs-fat-tails) (study). [Reflexivity](frameworks/1987-reflexivity.md) and the [bank run](frameworks/1948-self-fulfilling-prophecy.md) show beliefs and facts feeding each other into booms and crashes.
- [Stationary vs drifting](#stationary-vs-drifting) (study). Under the [Lucas critique](frameworks/1976-lucas-critique.md) acting on a model changes the behaviour it was fitted to.
- [Neutral vs adversarial](#neutral-vs-adversarial) (bundled). The [Keynesian beauty contest](frameworks/1936-keynesian-beauty-contest.md) and [zero-sum games](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) are both about other minds reacting to yours. The difference is intent. A bank run is reflexive with no enemy, since each saver only wants their own money back. A chess opponent is out to beat you, but the board doesn't change because someone forecast the result.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (logic). By [Goodhart's law](frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it.
- [Private vs accountable](#private-vs-accountable) (study). [Campbell's law](frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Test vs watch](#test-vs-watch) (study). The [Lucas critique](frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (study). By [Goodhart's law](frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (logic). Both put other people inside the problem. Once a fix depends on others changing, how they react to it becomes part of the problem.

### Neutral vs adversarial

Is someone working against you? Rain doesn't try to beat your umbrella. Fraudsters, hackers and rival traders learn your methods and change their play to beat them.

**Neutral**: Optimise for the typical case.
- Test on typical data. Errors are accidents, so a random sample of real inputs is a fair test.
- Publish how the model works if that helps users. Nobody is reading it to find a way round.

**Adversarial**: Assume someone is probing for your weak spots.
- Red team the model. Pay people to attack it before launch, and test on those attacks rather than typical inputs.
- Retrain fast as attackers adapt. A drop in the attacks you catch may mean they found a way round, not that they gave up.
- Keep part of the logic hidden or changing. A fixed public rule is one an attacker only has to beat once.
- Layer the model with rules and rate limits. Beating one check should not be enough to get through.

**Sources.** [Zero-sum vs non-zero-sum games](frameworks/1944-zero-sum-vs-non-zero-sum-games.md), [Task environment properties](frameworks/1995-task-environment-properties.md)

**Correlated with**

- [Inert vs reflexive](#inert-vs-reflexive) (bundled). The [Keynesian beauty contest](frameworks/1936-keynesian-beauty-contest.md) and [zero-sum games](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) are both about other minds reacting to yours. The difference is intent. A bank run is reflexive with no enemy in it. A chess opponent wants to beat you, but nothing about the game shifts because of a forecast.
- [Stationary vs drifting](#stationary-vs-drifting) (logic). Fraudsters and rivals change their play once they learn yours.
- [Full vs partial observability](#full-vs-partial-observability) (bundled). Opponents hide what they can, as in poker ([Task environment properties](frameworks/1995-task-environment-properties.md)).
- [Shared vs contested values](#shared-vs-contested-values) (logic). Rivals often want different things, so the two tend to come together. But two players in a [zero-sum game](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) agree on what winning means. They each just want to be the winner. Contested values is a fight over what a good result even is.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (independent). A chess opponent works against you, but every move you need is yours to make. Two firms in a [non-zero-sum game](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) want the same deal and still need each other to close it.

### Decomposable vs holistic

Can you split the problem into parts, solve each one and put them back together? A car engine mostly can. A family, an ecosystem or a company culture can't, because the parts only make sense together.

**Decomposable**: Split, solve and recombine.
- Give each part its own model or agent and its own test. Small parts are easier to build, check and swap out.
- Trust the whole if the parts pass. When the parts don't affect each other, good parts make a good whole.

**Holistic**: Test the whole system, not just the parts.
- Run end to end evals. Unit evals can all pass while the system fails.
- Watch for one part's gain turning into another's loss. Track a measure for the whole as well as one for each part.
- Prefer one model that sees the whole problem over a pipeline. A pipeline cuts the problem where it doesn't split.
- Change one part at a time and retest the whole. In a tangled system a small fix can break something far away.

**Sources.** [Simplicity, disorganised complexity and organised complexity](frameworks/1948-simplicity-disorganised-and-organised-complexity.md), [Near decomposability](frameworks/1962-near-decomposability.md), [Messes](frameworks/1974-messes.md), [Complex problem solving](frameworks/1989-complex-problem-solving.md), [Simple, complicated and complex](frameworks/2002-simple-complicated-and-complex.md)

**Correlated with**

- [Smooth vs rugged](#smooth-vs-rugged) (study). Kauffman's NK model ([Rugged fitness landscapes](frameworks/1987-rugged-fitness-landscapes.md)) makes the land rugged by linking the parts.
- [Transparent vs opaque causes](#transparent-vs-opaque-causes) (bundled). [Organised complexity](frameworks/1948-simplicity-disorganised-and-organised-complexity.md), [Normal accidents](frameworks/1984-normal-accidents.md), [Cynefin](frameworks/1999-cynefin.md) and Glouberman and Zimmerman's [complex problems](frameworks/2002-simple-complicated-and-complex.md) all say tangled parts hide causes.
- [Single vs multiple objectives](#single-vs-multiple-objectives) (bundled). In Ackoff's [messes](frameworks/1974-messes.md) a gain in one part turns up as a loss in another.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (bundled). [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) call each wicked problem a symptom of another, and [Jonassen](frameworks/2000-problem-typology.md) ranks problems on structure and complexity together.
- [Tractable vs intractable search](#tractable-vs-intractable-search) (logic). A problem that splits into parts can be solved one small unit at a time, like Simon's [watchmakers](frameworks/1962-near-decomposability.md).
- [Loose vs tight coupling](#loose-vs-tight-coupling) (independent). Perrow keeps tangled parts and lack of slack apart in [Normal accidents](frameworks/1984-normal-accidents.md). A university is tangled but loose, and a dam is tight but simple.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (bundled). In Ackoff's [messes](frameworks/1974-messes.md) the fix for one department becomes the next department's problem, so nobody holds the levers for the whole.

### Loose vs tight coupling

When one part fails, how fast does it spread? In a loose system there is slack and time to step in. In a tight one, like a power grid or a nuclear plant, one fault can cascade before anyone reacts.

**Loose**: Let things fail and fix them.
- Rely on review after the fact. There is time to spot an error and step in before it spreads.
- Automate early. A mistake costs a fix, not a cascade.

**Tight**: Build in slack and breaks before you automate.
- Put circuit breakers, rate limits and kill switches between a model and anything it can trigger. Automated trading learnt this in the 2010 flash crash, when US shares fell about 9% in minutes.
- Don't let models feed each other without a check in between. One model's error becomes the next one's input and grows at each step.
- Add slack where you can. Queues, buffers and delays give people time to see a fault before it spreads.
- Practise the failure. Run drills where a part breaks, so you know the breaks work before you need them.

**Sources.** [Loosely coupled systems](frameworks/1976-loosely-coupled-systems.md), [Normal accidents](frameworks/1984-normal-accidents.md)

**Correlated with**

- [Slack vs time pressure](#slack-vs-time-pressure) (by definition). Perrow defines tight coupling as having no slack, so when a tight system fails it hands you a decision with no time ([Normal accidents](frameworks/1984-normal-accidents.md)).
- [Survivable vs ruinous](#survivable-vs-ruinous) and [Reversible vs irreversible](#reversible-vs-irreversible) (study). In [Normal accidents](frameworks/1984-normal-accidents.md) small faults cascade into a meltdown before anyone can step in.
- [Thin vs fat tails](#thin-vs-fat-tails) (study). Cascades turn many small faults into rare huge losses, as in the 2010 flash crash.
- [Decomposable vs holistic](#decomposable-vs-holistic) (independent). Perrow treats how tangled the parts are and how tight the links are as separate traits.

### Tractable vs intractable search

How many options do you have to search through? Noughts and crosses has so few possible games that you can check every one. Chess is fully visible, fixed and rule bound, yet the number of possible games is so vast that you can't. The hardest searches of all are called NP-complete, which means nobody knows a method that stays fast as the problem grows.

**Tractable**: Search the lot.
- Check every option if you can. A full search is exact and needs no tuning.
- Use a model only to speed things up. The search already gives the right answer, so the model shouldn't change it.

**Intractable**: Use the model to guide the search, not to finish it.
- Let the model suggest which branches to try. AlphaGo works this way, with a learned guess steering a search too big to finish.
- Prune hard. Drop weak looking branches early, and accept you will sometimes drop a good one.
- Accept good enough and cap the time spent. Set a budget up front, since the search will never tell you it is done.
- Check the answer with a separate checker where you can. Many hard searches have answers that are quick to check.

**Sources.** [Satisficing](frameworks/1956-satisficing.md), [NP problems](frameworks/1971-np-problems.md)

**Correlated with**

- [Smooth vs rugged](#smooth-vs-rugged) (study). Stepping downhill on rugged land stops at a false bottom ([Convex vs non-convex optimisation](frameworks/1970-convex-vs-non-convex-optimisation.md)). Edward Weinberger proved in 1996 that finding the top of a general NK landscape is NP-complete.
- [Decomposable vs holistic](#decomposable-vs-holistic) (logic). A problem that splits into parts can be searched one part at a time, like Simon's [watchmakers](frameworks/1962-near-decomposability.md).
- [Satisficing vs optimising](#satisficing-vs-optimising) (tension). Needing the best answer from a search too big to finish is the hardest case.
- [Slack vs time pressure](#slack-vs-time-pressure) (tension). A search too big to finish, done against the clock, is the worst case.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (independent). [NP problems](frameworks/1971-np-problems.md) are hard to find and easy to check.
- [Full vs partial observability](#full-vs-partial-observability) (independent). Chess hides nothing and still can't be searched in full.
- [Discrete vs continuous](#discrete-vs-continuous) (opposite). Clean steps often make the search harder. Finding the best mix of products is fast when amounts can be any number, and NP-complete when they must be whole numbers ([NP problems](frameworks/1971-np-problems.md)).
- [Choose vs design the options](#choose-vs-design-the-options) (independent). Search size assumes the options already exist. A design problem can have only three options once someone has thought of them.

### Discrete vs continuous

Does the problem move in clean steps or by degrees? A chess move is one of a fixed set, and a square is either taken or not. Steering a car, setting a drug dose or judging how hard to brake is a matter of degree, so the answer is a number and being a little off counts.

**Discrete**: Treat it as classification or search, with exact checks.
- Score exact matches. Each answer is right or wrong, so there is no tolerance to argue about.
- Use solvers where they fit. Rule engines and search often beat a model on clean steps.

**Continuous**: Decide how close is close enough before you start.
- Set a tolerance for each output. Without one, nobody can say if the model passed.
- Predict a range, not just a point. A range tells the user how far off the answer might be.
- Test near the edges of the tolerance. That is where small errors cross the line.
- Budget for far more data and simulation on physical tasks. Control tasks need much more than their ease for people suggests, which is Moravec's paradox.

**Sources.** [Task environment properties](frameworks/1995-task-environment-properties.md), [Convex vs non-convex optimisation](frameworks/1970-convex-vs-non-convex-optimisation.md), [Moravec's paradox](frameworks/1988-moravecs-paradox.md)

**Correlated with**

- [Tractable vs intractable search](#tractable-vs-intractable-search) (opposite). Clean steps often make the search harder, not easier. Finding the best mix of products to make is fast when amounts can be any number. Insist they are whole numbers and it becomes one of Karp's 21 NP-complete problems ([NP problems](frameworks/1971-np-problems.md)).
- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (study). [Moravec's paradox](frameworks/1988-moravecs-paradox.md) is that machines beat people at chess long before they could walk across a room. Skills of degree, like balance and grip, are the ones nobody can write down.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (logic). A discrete answer is right or wrong. A continuous one is only close or far, so checking it needs a tolerance someone has to pick.

## The knower

These describe what you can find out. The same problem can sit at different points for different people.

### Known vs unknown odds

Do you know the chances, or only that things are uncertain? A dice roll has known odds. Whether a new technology takes off does not, and pretending it does gives you false confidence. Doubt you can't put a number on is called Knightian uncertainty, after Frank Knight.

**Known**: Compute and optimise.
- Use expected value as the test. With odds you trust, the best choice is the one that does best on average.
- Let a calibrated model make the call. Its probabilities mean what they say.

**Unknown**: Don't trust a model's probabilities just because they are precise.
- Test several plausible scenarios rather than one forecast. Ask what you would do in each, not which is most likely.
- Favour choices that hold up across all of them. A choice that is fine everywhere beats one that is best in one world and bad in the rest.
- Keep a margin of safety. Assume your estimate of the odds is wrong and leave room for it.
- Don't read past calibration as future calibration. Calibration on past data says nothing about a case with no past.

**Sources.** [Risk vs uncertainty](frameworks/1921-risk-vs-uncertainty.md), [Ambiguity aversion](frameworks/1961-ambiguity-aversion.md), [Four levels of uncertainty](frameworks/1997-four-levels-of-uncertainty.md), [Ecological rationality](frameworks/1999-ecological-rationality.md), [Levels of uncertainty](frameworks/2003-levels-of-uncertainty.md), [Deep uncertainty](frameworks/2003-deep-uncertainty.md), [Incertitude matrix](frameworks/2007-incertitude-matrix.md), [Radical uncertainty](frameworks/2020-radical-uncertainty.md)

**Correlated with**

- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (logic). [Knight](frameworks/1921-risk-vs-uncertainty.md)'s known odds come from a long record of similar cases.
- [Stationary vs drifting](#stationary-vs-drifting) (logic). Knight's uncertainty starts where the future may not look like the past.
- [Thin vs fat tails](#thin-vs-fat-tails) (logic). Tail odds can't be read off a calm past ([Mediocristan vs Extremistan](frameworks/2007-mediocristan-vs-extremistan.md)).
- [Shared vs contested values](#shared-vs-contested-values) (bundled). [Deep uncertainty](frameworks/2003-deep-uncertainty.md) and [Post-normal science](frameworks/1993-post-normal-science.md) put unknown odds and disputed values in one box. [Stirling](frameworks/2007-incertitude-matrix.md) and [Thompson and Tuden](frameworks/1959-decision-strategies-matrix.md) keep them apart, so they go together in practice but not by definition.
- [One-shot vs sequential](#one-shot-vs-sequential) (opposite). In a [bandit](frameworks/1933-multi-armed-bandit.md) problem each choice teaches you a little, so a sequential problem slowly turns unknown odds into known ones.
- [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) (independent). These two get mixed up more than any other pair. Known odds asks whether you can put a number on your doubt. Reducible asks whether more data would shrink it. A coin toss has known odds and doubt you can't shrink. A new drug has unknown odds and doubt you can shrink, because you can run a trial. Doubt that comes from pure chance is called aleatory, and doubt that comes from missing knowledge is called epistemic.
- [Small vs large world](#small-vs-large-world) (logic). You can't put odds on a state you never listed. But Ellsberg's urn has only two states and the odds are still unknown ([Ambiguity aversion](frameworks/1961-ambiguity-aversion.md)).

### Reducible vs irreducible uncertainty

Could more information shrink your doubt, or would no amount of fact finding settle it? Some doubt is pure chance, like the next roll of a dice. Some hangs on choices people haven't made yet, like whether a rival will cut prices next year. Some is a clash over what the facts mean. If your doubt is reducible you should go and gather data. If it's irreducible you should hedge instead.

**Reducible**: Go and get the data.
- Label more cases. Focus labelling on the cases the model is least sure of, which is called active learning.
- Ask the user the missing question before acting. One question often settles what no model could guess.

**Irreducible**: Stop paying for more data and hedge instead.
- Report a spread, not a single answer. More training won't shrink the doubt, so hiding it only misleads.
- Spread your bets. Make the decision cope with either result instead of staking it on one.
- Use an ensemble to tell the two kinds of doubt apart. Models that disagree point to doubt more data could fix. Models that agree on a wide spread point to doubt it can't.
- Check where the doubt comes from. If it hangs on a choice nobody has made yet, no data will settle it, so plan for each way the choice could go.

**Sources.** [Uncertainty vs equivocality](frameworks/1986-uncertainty-vs-equivocality.md), [Puzzles vs mysteries](frameworks/2001-puzzles-vs-mysteries.md)

**Correlated with**

- [Deterministic vs statistical](#deterministic-vs-statistical) (logic). Pure chance is one kind of doubt that no new data can shrink.
- [Long vs short predictability horizon](#long-vs-short-predictability-horizon) (logic). Past the horizon more data barely moves the forecast.
- [Full vs partial observability](#full-vs-partial-observability) (opposite). Hidden facts are the classic reducible doubt, like Treverton's [puzzles](frameworks/2001-puzzles-vs-mysteries.md), so partial observability usually leans to the reducible end.
- [Shared vs contested values](#shared-vs-contested-values) (bundled). Treverton's mysteries and Daft and Lengel's [equivocality](frameworks/1986-uncertainty-vs-equivocality.md) are doubts that more facts won't settle, because people read the facts differently or haven't yet chosen what to do.
- [Known vs unknown odds](#known-vs-unknown-odds) (independent). Reducible asks whether more data would shrink your doubt, while known odds asks whether you can put a number on it. A coin toss has known odds and irreducible doubt. A new drug has unknown odds and reducible doubt, because you can run a trial.

### Small vs large world

Can you list every way things might turn out before you choose? A lottery ticket wins or loses, and nothing else can happen. A new product can fail in ways nobody thought to list, like a rival's launch or a change in the law. Leonard Savage called the first a small world and the second a large one, and said his theory of rational choice only works in the small one.

**Small**: List the outcomes and optimise over them.
- Score each outcome and pick. Every state is known, so a model can weigh them all.
- Test against the full list. There are only so many cases, so you can check the model handles each one.

**Large**: Leave room for what nobody listed.
- Build a "don't know" or "out of scope" answer into the model. A model forced to pick from a list will pick wrong with confidence.
- Flag inputs unlike any in training and route those to a person. That is where the unlisted states show up first.
- Prefer actions that keep options open. The one that scores best on the list you have may do badly on the outcome you didn't list.
- Revisit the list after launch. Log the cases that fit none of your categories and add them.

**Sources.** [Small and large worlds](frameworks/1954-small-and-large-worlds.md), [Known and unknown unknowns](frameworks/2002-known-and-unknown-unknowns.md), [Radical uncertainty](frameworks/2020-radical-uncertainty.md)

**Correlated with**

- [Known vs unknown odds](#known-vs-unknown-odds) (logic). You can't put odds on a state you never listed, so a large world has unknown odds. The reverse doesn't hold. Ellsberg's urn has only two states, red or black, and the odds are still unknown ([Ambiguity aversion](frameworks/1961-ambiguity-aversion.md)).
- [Full vs partial observability](#full-vs-partial-observability) (independent). Observability asks whether you can see a state you know exists. Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [Stationary vs drifting](#stationary-vs-drifting) (logic). A drifting world keeps adding states nobody listed.
- [Thin vs fat tails](#thin-vs-fat-tails) (logic). The worst outcomes are often the ones nobody listed, which is what Taleb means by a black swan ([Mediocristan vs Extremistan](frameworks/2007-mediocristan-vs-extremistan.md)).
- [Choose vs design the options](#choose-vs-design-the-options) (bundled). Savage's small world fixes the list of actions as well as the list of states. In a large world you often have to invent the options too.

### Full vs partial observability

Can you see everything that matters? In chess you see the whole board. In poker the other hands are hidden, and in medicine you often see only symptoms, not the cause.

**Full**: Act on what you see.
- Decide straight from the input. It holds everything that matters.
- Skip the clarifying questions. Asking for what you can already see wastes the user's time.

**Partial**: Find out before you act.
- Gather the missing facts. An agent should look things up or ask a question before it commits.
- Keep track of what you believe about the hidden state. Update it as each new clue comes in, like a doctor narrowing a diagnosis.
- Say what you can't see. A model that answers as if it had the full picture hides its biggest weakness.
- Test the model on cases where the key evidence is missing. That is how it will meet many real ones.

**Sources.** [Johari window](frameworks/1955-johari-window.md), [Complex problem solving](frameworks/1989-complex-problem-solving.md), [Task environment properties](frameworks/1995-task-environment-properties.md), [Known and unknown unknowns](frameworks/2002-known-and-unknown-unknowns.md)

**Correlated with**

- [Deterministic vs statistical](#deterministic-vs-statistical) (logic). Russell and Norvig note that a deterministic world you can only half see looks random ([Task environment properties](frameworks/1995-task-environment-properties.md)).
- [Transparent vs opaque causes](#transparent-vs-opaque-causes) (study). Hidden variables are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every line of an open source codebase and still not trace the chain. A poker hand is a simple cause that is hidden from view.
- [Neutral vs adversarial](#neutral-vs-adversarial) (bundled). Opponents hide what they can, as in poker.
- [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) (opposite). What is hidden can often be found, so partial observability usually leans to the reducible end.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (logic). A hiring manager never sees how the people they turned away would have done, so half the feedback is missing ([Kind vs wicked learning environments](frameworks/2001-kind-vs-wicked-learning-environments.md)).
- [Tractable vs intractable search](#tractable-vs-intractable-search) (independent). Chess hides nothing and still can't be searched in full.
- [Small vs large world](#small-vs-large-world) (independent). Every possible poker hand is known in advance, and you still can't see the one in front of you.
- [General vs local knowledge](#general-vs-local-knowledge) (logic). Local facts are often out of sight for anyone far away. But the shop manager can see the stock levels that head office can't, so the gap is about who holds the facts.

### Transparent vs opaque causes

Can you trace the chain from cause to effect? A lever is transparent. A large codebase follows rules, yet no one person can hold the whole chain in their head.

**Transparent**: Model the mechanism.
- Write the cause and effect into the system as rules or structure. A model that has to rediscover a known mechanism wastes data.
- Debug by following the chain. When something goes wrong you can trace it to the step that failed.

**Opaque**: Don't trust explanations, trust experiments.
- Treat the model's story of why as a guess. It will sound right and may be wrong.
- Change one thing at a time and measure the effect. That is how you find a cause you can't trace.
- Use the model to predict, and hold back claims about cause. Test a claim before you build a decision on it.
- Expect a fix to have side effects. When you can't see the chain, you can't see what else it touches.

**Sources.** [Decision strategies matrix](frameworks/1959-decision-strategies-matrix.md), [Normal accidents](frameworks/1984-normal-accidents.md), [Detail vs dynamic complexity](frameworks/1990-detail-vs-dynamic-complexity.md), [Task environment properties](frameworks/1995-task-environment-properties.md), [Stacey matrix](frameworks/1996-stacey-matrix.md), [Cynefin](frameworks/1999-cynefin.md), [Simple, complicated and complex](frameworks/2002-simple-complicated-and-complex.md)

**Correlated with**

- [Decomposable vs holistic](#decomposable-vs-holistic) (bundled). Weaver's [organised complexity](frameworks/1948-simplicity-disorganised-and-organised-complexity.md), Perrow's tangled systems in [Normal accidents](frameworks/1984-normal-accidents.md), the complex domain of [Cynefin](frameworks/1999-cynefin.md) and Glouberman and Zimmerman's [complex problems](frameworks/2002-simple-complicated-and-complex.md) all say causes are hard to trace because the parts keep changing each other.
- [Full vs partial observability](#full-vs-partial-observability) (study). Hidden variables are part of why Dörner's players couldn't trace their own effects ([Complex problem solving](frameworks/1989-complex-problem-solving.md)). The two still differ. You can read every line of an open source codebase and still not trace the chain. A poker hand is a simple cause that is hidden from view.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) and [One-shot vs sequential](#one-shot-vs-sequential) (study). In Senge's [beer game](frameworks/1990-detail-vs-dynamic-complexity.md) delays put weeks between an order and its effect, so players blame the wrong thing.
- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (bundled). Perrow's [unanalysable work](frameworks/1967-routine-vs-non-routine-technology.md) has no logical way to search for answers, so people fall back on hunch. But the two come apart. Riding a bike has clear physics and needs tacit skill. A tax code has explicit rules and knock-on effects nobody can trace.
- [Test vs watch](#test-vs-watch) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right ([Ladder of causation](frameworks/2000-ladder-of-causation.md)).

### Test vs watch

Can you run a fair test, or can you only watch what happens? A drug trial gives the pill to some people and a dummy to others at random, so any gap comes from the pill. In 1991 a study of nearly 50,000 nurses found women on hormone therapy had about half the heart disease. That was watching, and the women who chose hormones were healthier to start with. A 2002 trial found the hormones raised heart disease. Judea Pearl calls watching and testing the bottom two rungs of his ladder of causation.

**Test**: Run the experiment.
- Randomise, A/B test or use a bandit. A fair test tells you what works, not just what goes with what.
- Let the result decide. A fair test should beat anyone's opinion of the outcome.

**Watch**: Treat logged data as biased until shown otherwise.
- Remember what the logs teach. A model trained on what happened learns who chose what, not what works.
- Write down what you assume causes what. Then use methods that adjust for it, so others can see and challenge your guesses.
- Check against any small test you can run. Even a little random data can show if the logs mislead you.
- Never read a pattern in the logs as the effect of acting on it. The nurses study did, and got hormone therapy backwards.

**Sources.** [Multi-armed bandit](frameworks/1933-multi-armed-bandit.md), [Exploration vs exploitation](frameworks/1991-exploration-vs-exploitation.md), [Ladder of causation](frameworks/2000-ladder-of-causation.md)

**Correlated with**

- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (independent). The nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](frameworks/2000-ladder-of-causation.md)).
- [Transparent vs opaque causes](#transparent-vs-opaque-causes) (logic). A fair test is how you find a cause you can't trace. If you can only watch, you have to write down what you think causes what and hope the model is right.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (logic). Watching mixes the effect of a choice with the kind of people who made it, so it can teach the wrong lesson. Doctors read the nurses study as proof that hormones protect the heart.
- [Reversible vs irreversible](#reversible-vs-irreversible) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Inert vs reflexive](#inert-vs-reflexive) (study). The [Lucas critique](frameworks/1976-lucas-critique.md) is a warning about answering a question on stepping in with data from watching. The Phillips curve held while nobody leaned on it and broke once policy did.
- [One-shot vs sequential](#one-shot-vs-sequential) (opposite). Each pull of a [bandit](frameworks/1933-multi-armed-bandit.md) is a small test, so a chain of choices lets you test as you go. Thompson picked each new patient's treatment at random, weighted towards whichever looked better so far.

### Kind vs wicked feedback

Do you find out quickly and honestly whether you were right? A chess player gets fast and clear feedback, so skill builds. A fund manager waits years for noisy results, so experience can teach the wrong lesson.

**Kind**: Learn from results.
- Retrain on outcomes. Fast, honest feedback means the labels are good.
- Trust experience. A person or model that has seen many results here has learnt something real.

**Wicked**: Don't let experience grade itself.
- Check the labels before you train on them. They may be late, noisy or missing for the cases you turned down, so the model can learn the wrong lesson.
- Get labels from outside the loop. Audits and expert review give a view the model's own record can't.
- Let a small random share through that the model would have refused. It's the only way to see how the road not taken turns out.
- Judge on long term outcomes rather than the first signal you can measure. Clicks today can hide lost customers next year.

**Sources.** [Task characteristics of expertise](frameworks/1992-task-characteristics-of-expertise.md), [Kind vs wicked learning environments](frameworks/2001-kind-vs-wicked-learning-environments.md), [Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)

**Correlated with**

- [Plentiful vs scarce data](#plentiful-vs-scarce-data) and [Stationary vs drifting](#stationary-vs-drifting) (study). [Shanteau](frameworks/1992-task-characteristics-of-expertise.md) found experts got good where decisions came often in the same form about a stable subject. [Kahneman and Klein](frameworks/2009-conditions-for-intuitive-expertise.md) say the same of intuition you can trust.
- [Long vs short predictability horizon](#long-vs-short-predictability-horizon) (study). Weather forecasters work inside the horizon and are well calibrated, while Tetlock's long range pundits did little better than chance.
- [Transparent vs opaque causes](#transparent-vs-opaque-causes) and [One-shot vs sequential](#one-shot-vs-sequential) (study). In Senge's [beer game](frameworks/1990-detail-vs-dynamic-complexity.md) delays hide which move caused which result.
- [Full vs partial observability](#full-vs-partial-observability) (logic). If you never see how the road not taken turned out, as in hiring, half your feedback is missing ([Hogarth](frameworks/2001-kind-vs-wicked-learning-environments.md)).
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (logic). Feedback is the world checking your answer for you, so an answer that is hard to check gives slow feedback. They still differ. Verifying is checking one answer before you act on it. Feedback is the world grading you after you act, over many tries. A sudoku is easy to check but teaches you little about the next one. A doctor can't prove a diagnosis on the day, yet learns over years which calls turned out right.
- [Reversible vs irreversible](#reversible-vs-irreversible) (bundled). [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) note you can't learn by trial and error when each try leaves a mark.
- [Test vs watch](#test-vs-watch) (logic). Watching mixes the effect of a choice with the kind of people who made it, so it can teach the wrong lesson. Doctors read a 1991 study of nurses as proof that hormones protect the heart, and a 2002 trial showed they did harm ([Ladder of causation](frameworks/2000-ladder-of-causation.md)).
- [Skin in the game vs none](#skin-in-the-game-vs-none) (logic). If the cost of a mistake lands on someone else, the decider may never hear about it.

### Plentiful vs scarce data

Do you have enough cases to learn from? Card fraud happens millions of times a year. A nuclear accident or a once in a century flood gives you almost nothing to go on.

**Plentiful**: Let the model learn the pattern.
- Prefer a statistical model to expert judgement. Meehl found that simple formulas fitted to many cases beat clinicians.
- Hold out a big test set. With data to spare you can measure the model properly.

**Scarce**: Borrow knowledge from elsewhere.
- Start from a pre-trained model. It brings what it learnt from other data, so you need far fewer cases of your own.
- Use base rates from similar cases. This is called the outside view, and it beats reasoning from the details of one case.
- Add expert priors or simulation where you can. They fill the gaps your data leaves.
- Report wide error bars, and don't trust a test set of thirty examples. A lucky few can make a weak model look great.

**Sources.** [Clinical vs statistical prediction](frameworks/1954-clinical-vs-statistical-prediction.md), [Task characteristics of expertise](frameworks/1992-task-characteristics-of-expertise.md), [Inside vs outside view](frameworks/1993-inside-vs-outside-view.md), [Ecological rationality](frameworks/1999-ecological-rationality.md)

**Correlated with**

- [Thin vs fat tails](#thin-vs-fat-tails) (logic). The events that matter most in a fat tailed world are the rare ones. But card fraud is fat tailed and still has millions of cases. Fat tails make the cases that matter rare, not the data overall.
- [Known vs unknown odds](#known-vs-unknown-odds) (logic). Odds come from a long record of similar cases ([Risk vs uncertainty](frameworks/1921-risk-vs-uncertainty.md)).
- [Stationary vs drifting](#stationary-vs-drifting) (logic). Drift makes old data stale, so a big record can still leave you short of cases that still apply.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (study). [Shanteau](frameworks/1992-task-characteristics-of-expertise.md) found skill grows where the same decision comes round often.
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (logic). A rare kind of case is one the solver has seldom seen. Simon's [programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md) are the ones that recur. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Survivable vs ruinous](#survivable-vs-ruinous) (logic). You can't learn from your own ruin, because it only happens once ([Ergodicity](frameworks/2016-ergodicity.md)).
- [Test vs watch](#test-vs-watch) (independent). The 1991 nurses study had nearly 50,000 women and still got the cause backwards. A pile of data from watching can't tell you what happens when you step in ([Ladder of causation](frameworks/2000-ladder-of-causation.md)).

### Explicit vs tacit know-how

Can the expertise be written down? A tax rule can. How a master chef judges when bread is done, or how a nurse senses a patient is about to crash, is hard to put into words.

**Explicit**: Write it down and hand it over.
- Put the rules in the prompt, the code or a checklist. If an expert can say it, a model can be told it.
- Test the model against the written rules. Each rule becomes a test case.

**Tacit**: Learn from examples and judges, not instructions.
- Collect demonstrations. Showing the model good work teaches what words can't.
- Gather expert ratings. Experts can tell good from bad even when they can't say why.
- Keep experts in the loop to grade outputs. Their judgement is the only check you have.
- Expect a long tail of cases that written guidance misses. Plan to review the odd ones rather than add more rules.

**Sources.** [Routine vs non-routine technology](frameworks/1967-routine-vs-non-routine-technology.md), [Skill, rule and knowledge-based behaviour](frameworks/1983-skill-rule-and-knowledge-based-behaviour.md), [Cognitive continuum](frameworks/1987-cognitive-continuum.md), [Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)

**Correlated with**

- [Transparent vs opaque causes](#transparent-vs-opaque-causes) (bundled). Perrow's [unanalysable work](frameworks/1967-routine-vs-non-routine-technology.md) has no logical way to search for answers, so people rely on hunch. But the two come apart. Riding a bike has clear physics and needs tacit skill. A tax code has explicit rules and knock-on effects nobody can trace.
- [Slack vs time pressure](#slack-vs-time-pressure) (study). Hammond's [cognitive continuum](frameworks/1987-cognitive-continuum.md) puts tasks with many cues and little time at the intuitive end. Klein's fire lieutenant got his crew out on a gut call he couldn't explain ([Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)).
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (opposite). Rasmussen found that novel cases force slow, explicit reasoning, since there is no trained pattern to fall back on ([Skill, rule and knowledge-based behaviour](frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)).
- [Private vs accountable](#private-vs-accountable) (tension). Know-how you can't put into words is hard to defend in an audit. Meehl's [formulas](frameworks/1954-clinical-vs-statistical-prediction.md) and the Apgar score show the usual fix, which is to write a rule down and give up some of the craft.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (independent). Both say an expert can't just hand over the fix, but for different reasons. Tacit know-how is hard to put into words. In an adaptive challenge the know-how is often plain, like stop smoking, and the hard part is getting people to act on it ([Technical vs adaptive challenges](frameworks/1994-technical-vs-adaptive-challenges.md)).
- [Discrete vs continuous](#discrete-vs-continuous) (study). By [Moravec's paradox](frameworks/1988-moravecs-paradox.md) machines beat people at chess long before they could walk across a room, because skills of degree are the ones nobody can write down.
- [General vs local knowledge](#general-vs-local-knowledge) (bundled). Scott's metis is both local and tacit ([Use of knowledge in society](frameworks/1945-use-of-knowledge-in-society.md)). But today's stock levels are local and written down, and riding a bike is tacit and the same in every town.

### Familiar vs novel to the solver

Has the solver seen this kind of problem before? A doctor sees a common cold every day but a rare disease once in a career. For an AI model the question is whether the problem sits inside its training data, which decides if it is reasoning or recalling.

**Familiar**: Trust recall.
- Accept a quick answer. A problem like those in training is one the model has seen solved.
- Spend less on reasoning. Long chains of working add cost and little accuracy on a problem the model knows.

**Novel**: Make the solver reason, and check the result.
- Ask for working. A step by step answer shows where the reasoning went wrong.
- Break the task into steps and verify each one. Errors on a new problem stack up, so catch them early.
- Test the model on problems written after its training cutoff. A benchmark it has seen measures memory, not skill.
- Watch for a familiar answer to the wrong problem. A model will often match a new problem to an old one it looks like.

**Sources.** [Programmed vs non-programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md), [Routine vs non-routine technology](frameworks/1967-routine-vs-non-routine-technology.md), [Skill, rule and knowledge-based behaviour](frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)

**Correlated with**

- [Stationary vs drifting](#stationary-vs-drifting) (logic). A drifting world keeps serving up cases nobody has seen.
- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (logic). A rare kind of case is one the solver has seldom seen. But the world can hold millions of cases the solver has never met. For an AI model, anything after its training cutoff sits in that gap.
- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (opposite). With no trained pattern to call on, the solver has to reason slowly from an explicit model ([Skill, rule and knowledge-based behaviour](frameworks/1983-skill-rule-and-knowledge-based-behaviour.md)).
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) and [Reversible vs irreversible](#reversible-vs-irreversible) (bundled). Simon's [non-programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md) are new, messy and high stakes all at once.
- [General vs local knowledge](#general-vs-local-knowledge) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.

### General vs local knowledge

Does the answer rest on facts anyone could look up, or on facts about this place, this firm or this moment? How insulin works is general. Whether this patient has been taking theirs is local, and only someone close to them knows. Friedrich Hayek called this knowledge of the particular circumstances of time and place.

**General**: Let the model answer from what it knows.
- Trust its training data. Facts anyone could look up are already in it.
- Skip the search step. Feeding in documents adds cost, and can add noise when the model already knows the answer.

**Local**: Feed in the local facts or ask someone who has them.
- Search your own records. That puts facts in front of the model that no training data holds.
- Give the model live data. Local facts change daily, so a snapshot goes stale.
- Treat the person on the ground as the source of truth. When the model and the shop manager disagree about the shop, the manager wins.
- Make the model say when it is falling back on general knowledge. A model that answers a local question from general knowledge gives a plausible answer about some other shop.

**Sources.** [Use of knowledge in society](frameworks/1945-use-of-knowledge-in-society.md)

**Correlated with**

- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (bundled). James C. Scott's metis is knowledge that is both local and tacit ([Use of knowledge in society](frameworks/1945-use-of-knowledge-in-society.md)). But the two come apart. Today's stock levels are local and sit in a spreadsheet. Riding a bike is tacit and works the same in every town.
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (logic). Local facts are never in the training data, however common the type of problem. An AI model may know everything about stock control and nothing about this shop.
- [Full vs partial observability](#full-vs-partial-observability) (logic). Local facts are often out of sight for anyone far away. But observability is about what the world hides, while this axis is about who holds the facts. The shop manager can see the stock levels. Head office can't.
- [Stationary vs drifting](#stationary-vs-drifting) (logic). Hayek's point was that local circumstances change every day, so local facts go stale fast.

## The decision

These describe what you are trying to achieve and what happens if you get it wrong.

### Well-posed vs ill-posed

Is the goal clear and do you know when you are done? A maths exam question is well posed. "Fix homelessness" is not, so working out what the problem actually is becomes part of the job.

**Well-posed**: Solve it.
- Let the model work towards the test. With a clear goal and a test for done, it doesn't need a person watching.
- Automate the check. The test for done can run on every output.

**Ill-posed**: Work out the problem before solving it.
- Draft several framings of the goal. Each one points to a different solution, so compare them before you pick.
- Write down what done looks like and agree it before building. Otherwise every review turns into an argument about the goal.
- Expect to revise the goal once the first version ships, and budget for it. Seeing a draft is often what tells people what they wanted.
- Use the model to explore, not to finish. Ask it for framings and questions rather than an answer.

**Sources.** [Well vs ill-structured problems](frameworks/1964-well-vs-ill-structured-problems.md), [Tame vs wicked problems](frameworks/1973-tame-vs-wicked-problems.md), [Presented vs discovered problems](frameworks/1976-presented-vs-discovered-problems.md), [Single vs double-loop learning](frameworks/1978-single-vs-double-loop-learning.md), [High ground vs swampy lowlands](frameworks/1983-high-ground-vs-swampy-lowlands.md), [Problem typology](frameworks/2000-problem-typology.md)

**Correlated with**

- [Easy vs hard to verify](#easy-vs-hard-to-verify) (by definition). Simon's [well-structured problems](frameworks/1964-well-vs-ill-structured-problems.md) come with a test for an answer, and [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) say a wicked problem has no point where it is done.
- [Shared vs contested values](#shared-vs-contested-values) (bundled). [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md), [Checkland](frameworks/1981-hard-vs-soft-systems.md) and [Roberts](frameworks/2000-simple-complex-and-wicked.md) all say the hard part is that people don't agree what the problem is.
- [Single vs multiple objectives](#single-vs-multiple-objectives) (bundled). Simon's house design and Jonassen's [dilemmas](frameworks/2000-problem-typology.md) are hard to pin down because several wants pull against each other. These three axes all get bundled under "wicked", but they come apart. "Cure this cancer" has one goal that everyone shares, yet nobody can say how to get there or what to try first. Buying a car has many objectives but is well posed once you set the weights.
- [Decomposable vs holistic](#decomposable-vs-holistic) (bundled). Ackoff's [messes](frameworks/1974-messes.md) and Jonassen's typology put tangled problems at the ill-structured end.
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (bundled). Simon's [non-programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md) are both new and poorly structured.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (logic). If you can't state the goal, you can't score all of it. The reverse doesn't hold. Rating CVs looked well posed, yet Amazon's score left out fairness ([Need for interpretability](frameworks/2017-need-for-interpretability.md)).
- [Choose vs design the options](#choose-vs-design-the-options) (independent). "Build a bridge across this river for under £10m" is well posed, and every option still has to be drawn.
- [Convergent vs divergent](#convergent-vs-divergent) (independent). "Write a sonnet about autumn" is well posed and has endless good answers.

### Choose vs design the options

Are the options handed to you, or do you have to invent them? Picking a mortgage from a bank's list is choosing. Deciding what to do about a dying high street means making up the options first, and the best one may be something nobody has tried. Herbert Simon split decision making into finding the problem, designing options and choosing among them.

**Choose**: Compare and pick.
- Score the given list against your goal. This is a job a model does well.
- Spend the effort on the scoring. With the options fixed, the quality of the choice comes down to how well you weigh them.

**Design**: Make many options before you choose.
- Start from what you value, not from the obvious options. Keeney's point is that the best option is often one nobody listed.
- Use a model to widen the set. It can draft dozens of options in the time a team drafts three.
- Keep making and choosing apart. Judging too early kills odd ideas before anyone understands them.
- Only then narrow down. Score the full set against the values you started from.

**Sources.** [Programmed vs non-programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md), [Value-focused thinking](frameworks/1992-value-focused-thinking.md)

**Correlated with**

- [Tractable vs intractable search](#tractable-vs-intractable-search) (independent). Search size assumes the options already exist. A design problem can have only three options once someone has thought of them.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (independent). A design brief can be crisp. "Build a bridge across this river for under £10m" is well posed, and every option still has to be drawn.
- [Convergent vs divergent](#convergent-vs-divergent) (logic). Options you invent rarely line up to one right answer, so design problems tend to have many good ones.
- [Small vs large world](#small-vs-large-world) (bundled). Savage's small world fixes the list of actions along with the list of states ([Small and large worlds](frameworks/1954-small-and-large-worlds.md)).

### Convergent vs divergent

Is there one right answer, or many good ones? A sum has one. A wedding speech, a logo or a sonnet about autumn has many, and two very different ones can both be excellent. J. P. Guilford called the thinking for the first kind convergent and for the second divergent.

**Convergent**: Score against the key.
- Use exact match, unit tests or a reference answer. They tell you if the model is right without anyone reading the output.
- Turn the model's randomness down, which is called lowering the temperature. You want the one right answer every time, not variety.

**Divergent**: Judge quality, not match.
- Use human raters or a model grader with a clear rubric. The rubric says what good looks like without fixing one answer.
- Compare outputs in pairs. People judge which of two is better more reliably than they give a score out of ten.
- Reward variety. Generate several and keep the best, rather than asking for one safe answer.
- Never score a creative task against one reference answer. It punishes good answers that differ from it.

**Sources.** [Convergent vs divergent thinking](frameworks/1956-convergent-vs-divergent-thinking.md)

**Correlated with**

- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (independent). "Write a sonnet about autumn" is well posed. You know what is wanted and when you're done, yet there are endless good answers.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (logic). One right answer can be checked against a key. Many good answers need someone to judge them.
- [Satisficing vs optimising](#satisficing-vs-optimising) (opposite). With many good answers there is no single best one to chase.
- [Choose vs design the options](#choose-vs-design-the-options) (logic). Options you invent rarely line up to one right answer.

### Single vs multiple objectives

Is there one thing to get right, or several that pull against each other? The fastest route home is one objective. A new car trades price against safety, comfort and running costs, so there are many good answers, not one.

**Single**: Optimise the one number.
- Use it as both the training target and the release gate. When there is one goal, the score and the job are the same.
- Compare models on it directly. Higher is better, so there is nothing to argue about.

**Multiple**: Make the trade offs plain.
- Track each objective as its own metric. A model tuned on one blended score hides which goal it gave up.
- Show decision makers the best trade offs on offer. Lay out the options where you can't gain on one goal without losing on another, and let them pick.
- Agree the weights before training, not after. Weights set after you see results tend to favour the model you already like.
- Set a floor for each objective. No gain on one should push another below what is acceptable.

**Sources.** [Decisions with multiple objectives](frameworks/1976-decisions-with-multiple-objectives.md), [Problem typology](frameworks/2000-problem-typology.md), [Need for interpretability](frameworks/2017-need-for-interpretability.md)

**Correlated with**

- [Decomposable vs holistic](#decomposable-vs-holistic) (bundled). In Ackoff's [messes](frameworks/1974-messes.md) a gain in one part turns up as a loss in another.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (bundled). Simon's house design and Jonassen's [dilemmas](frameworks/2000-problem-typology.md) are hard to pin down because several wants pull against each other. But buying a car has many objectives and is still well posed once you set the weights.
- [Shared vs contested values](#shared-vs-contested-values) (logic). Once there are several goals, different people weigh them differently. Stirling calls this [ambiguity](frameworks/2007-incertitude-matrix.md). But one person buying a car has many objectives and nobody to argue with.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (logic). With no single score there is no simple check that one answer beats another.
- [Satisficing vs optimising](#satisficing-vs-optimising) (opposite). With several goals there is a set of good trade offs and no one best answer, so you have to settle for good enough.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (bundled). Doshi-Velez and Kim ([Need for interpretability](frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap in the score. But a car buyer who writes down every want and sets the weights has many objectives and a complete goal.
- [Commensurable vs incommensurable values](#commensurable-vs-incommensurable-values) (by definition). The question only comes up with more than one objective. Setting weights, as Keeney and Raiffa do, assumes every goal can be turned into one score.

### Shared vs contested values

Does everyone agree what a good result looks like? A bridge should stay up, and nobody argues. Where to build the bridge, and whose homes it passes, depends on whose interests count.

**Shared**: Go straight to the technical work.
- Let experts build it and judge it. Everyone agrees what good looks like.
- Keep the review inside the team. There is no outside group whose view you are missing.

**Contested**: Settle whose values count before you build, and do it in the open.
- Bring the affected groups in early. Their objections are cheaper to hear before launch than after.
- Publish the trade offs the model makes. If people can see them, they can argue with them.
- Let people outside the team challenge the choices. An outside review catches the side you didn't know you took.
- Don't ship one side's view as neutral fact. If nobody asks whose side a model is on, that is what it does.

**Sources.** [Decision strategies matrix](frameworks/1959-decision-strategies-matrix.md), [Tame vs wicked problems](frameworks/1973-tame-vs-wicked-problems.md), [Hard vs soft systems](frameworks/1981-hard-vs-soft-systems.md), [Post-normal science](frameworks/1993-post-normal-science.md), [Technical vs adaptive challenges](frameworks/1994-technical-vs-adaptive-challenges.md), [Stacey matrix](frameworks/1996-stacey-matrix.md), [Simple, complex and wicked](frameworks/2000-simple-complex-and-wicked.md), [Deep uncertainty](frameworks/2003-deep-uncertainty.md)

**Correlated with**

- [Neutral vs adversarial](#neutral-vs-adversarial) (logic). Rivals often want different things, so the two tend to come together. But two players in a [zero-sum game](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) agree on what winning means. They each just want to be the winner. Contested values is a fight over what a good result even is.
- [Known vs unknown odds](#known-vs-unknown-odds) and [Slack vs time pressure](#slack-vs-time-pressure) (bundled). [Post-normal science](frameworks/1993-post-normal-science.md) joins disputed values with uncertain facts and urgent deadlines, and [Deep uncertainty](frameworks/2003-deep-uncertainty.md) joins them with unknown odds. [Stirling](frameworks/2007-incertitude-matrix.md) and [Thompson and Tuden](frameworks/1959-decision-strategies-matrix.md) keep facts and values apart, so this is a link in practice, not by definition.
- [Reducible vs irreducible uncertainty](#reducible-vs-irreducible-uncertainty) (bundled). Daft and Lengel's [equivocality](frameworks/1986-uncertainty-vs-equivocality.md) is a clash of meanings that more data won't settle.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (bundled). [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md), [Checkland](frameworks/1981-hard-vs-soft-systems.md) and [Roberts](frameworks/2000-simple-complex-and-wicked.md) all trace ill-posed problems back to a fight over goals. But "cure this cancer" has one goal that everyone shares and is still ill-posed.
- [Single vs multiple objectives](#single-vs-multiple-objectives) (logic). Once there are several goals, different people weigh them differently. Stirling calls this [ambiguity](frameworks/2007-incertitude-matrix.md). But one person buying a car has many objectives and nobody to argue with.
- [Private vs accountable](#private-vs-accountable) (logic). A choice that picks winners has to be defended in public, which is why [Post-normal science](frameworks/1993-post-normal-science.md) calls for a wider group to judge it.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (logic). When people disagree on what a good result is, any one score takes a side and leaves the other wants out.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (bundled). [Heifetz](frameworks/1994-technical-vs-adaptive-challenges.md) says adaptive work often means people giving up something they value. [Super wicked problems](frameworks/2007-super-wicked-problems.md) have nobody in charge to settle whose interests count.
- [Commensurable vs incommensurable values](#commensurable-vs-incommensurable-values) (independent). Everyone can agree a child's life is sacred and still face a budget.
- [Even vs lopsided errors](#even-vs-lopsided-errors) (logic). How much worse a miss is than a false alarm is a value judgement, so people fight over where to set the bar.

### Commensurable vs incommensurable values

Can every want be priced in one currency? Choosing a flight trades price against time, and you can say what an hour is worth to you. A hospital budget trades money against lives, and most people refuse to put a price on a child. Alan Fiske and Philip Tetlock called these taboo trade offs.

**Commensurable**: Price everything and add it up.
- Use a single score with weights. Every want has a price, so one number can stand for the whole.
- Let the model make the trade offs. Once the weights are agreed, it can apply them more evenly than a person.

**Incommensurable**: Set hard limits instead of weights.
- Treat sacred values as rules the model can't break, not costs it can trade. No gain elsewhere should buy a breach.
- Leave the remaining trade offs to a person who can own them. Some choices need someone to answer for them.
- Keep prices on lives and other sacred things out of the system. A loss function that puts a price on a life will be found and quoted.

**Sources.** [Decisions with multiple objectives](frameworks/1976-decisions-with-multiple-objectives.md), [Taboo trade-offs](frameworks/1997-taboo-trade-offs.md)

**Correlated with**

- [Single vs multiple objectives](#single-vs-multiple-objectives) (by definition). The question only comes up when there is more than one objective. Keeney and Raiffa's weights assume every goal can be turned into one score ([Decisions with multiple objectives](frameworks/1976-decisions-with-multiple-objectives.md)).
- [Shared vs contested values](#shared-vs-contested-values) (independent). Everyone can agree a child's life is sacred and still face a budget. People can also fight over how to weigh two things that both have a price.
- [Private vs accountable](#private-vs-accountable) (study). In 2000 Tetlock asked people to judge a hospital manager who could spend $1m on a child's liver transplant or on equipment and salaries. Choosing the equipment after long thought scored 5.71 for outrage out of 7. Saving the child at once scored 1.51. Even being seen to weigh a sacred value counts against you, so a choice you must defend in public pushes the trade off out of sight.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (logic). A single score has to price everything. So the sacred value is either left out or priced where nobody can see.

### Yours to fix vs needs others to change

Do you hold the levers, or does the fix depend on other people changing? A surgeon can unblock a man's arteries on his own. Whether the man lives another twenty years depends on whether he stops smoking, and no surgeon can do that for him. Climate change is harder still, because nobody is in charge and the people trying to fix it are also causing it. Ronald Heifetz calls the first kind of problem technical and the second adaptive.

**Yours to fix**: Fix it.
- Build the tool and ship it. You hold the levers.
- Measure the model directly. If it works, the problem is solved.

**Needs others**: Design for take up, not just accuracy.
- Involve the people who must change early. A tool built for them without them tends to sit unused.
- Make the change easy. Fit the model into what people already do rather than asking them to learn a new habit.
- Measure what people do, not model scores. A perfect model nobody uses fixes nothing.
- Plan for the people who lose out. If the change costs someone something they value, expect them to push back.

**Sources.** [Zero-sum vs non-zero-sum games](frameworks/1944-zero-sum-vs-non-zero-sum-games.md), [Messes](frameworks/1974-messes.md), [Technical vs adaptive challenges](frameworks/1994-technical-vs-adaptive-challenges.md), [Super wicked problems](frameworks/2007-super-wicked-problems.md)

**Correlated with**

- [Shared vs contested values](#shared-vs-contested-values) (bundled). [Heifetz](frameworks/1994-technical-vs-adaptive-challenges.md) says adaptive work often means people giving up something they value. [Super wicked problems](frameworks/2007-super-wicked-problems.md) have nobody in charge to settle whose interests count.
- [Slack vs time pressure](#slack-vs-time-pressure) (bundled). Super wicked problems join a clock to a world with nobody in charge, so each actor has a reason to wait while time runs out.
- [Decomposable vs holistic](#decomposable-vs-holistic) (bundled). In Ackoff's [messes](frameworks/1974-messes.md) the fix for one department becomes the next department's problem, so nobody holds the levers for the whole.
- [Inert vs reflexive](#inert-vs-reflexive) (logic). Both put other people inside the problem. Once a fix depends on others changing, how they react to it becomes part of the problem.
- [Neutral vs adversarial](#neutral-vs-adversarial) (independent). A chess opponent works against you, but every move you need is yours to make. Two firms in a [non-zero-sum game](frameworks/1944-zero-sum-vs-non-zero-sum-games.md) want the same deal and still need each other to close it.
- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (independent). Both say an expert can't just hand over the fix, but for different reasons. Tacit know-how is hard to put into words. In an adaptive challenge the know-how is often plain, like stop smoking, and the hard part is getting people to act on it.

### Satisficing vs optimising

Is good enough fine, or does the last bit matter? Picking a lunch spot is satisficing. Setting the dose of a strong drug, or tuning a racing car, needs the best answer you can find.

**Satisficing**: Set a bar and stop when you clear it.
- Ship the first model that meets the need. More tuning past the bar is waste.
- Write the bar down before you start. Without it, tuning drags on because better always seems possible.

**Optimising**: Spend on the last few percent, and check you got it.
- Use larger searches, ensembles and careful tuning. Here the small gains are the whole point.
- Confirm the gain on fresh data. Otherwise you may just be fitting the test set.
- Check the gain is real before you pay for it. Small gaps between models often vanish when you rerun them.

**Sources.** [Satisficing](frameworks/1956-satisficing.md), [Flat maximum](frameworks/1973-flat-maximum.md), [Ecological rationality](frameworks/1999-ecological-rationality.md)

**Correlated with**

- [Smooth vs rugged](#smooth-vs-rugged) and [Tractable vs intractable search](#tractable-vs-intractable-search) (tension). Needing the best answer when the land is rugged or the search is too big is the hardest case. Small steps stop on the nearest peak, and the [NP problems](frameworks/1971-np-problems.md) note advises settling for a good answer.
- [Slack vs time pressure](#slack-vs-time-pressure) (tension). Needing the best answer with no time to look for it is a clash. Simon's point was that limited time and attention push people to good enough, and Klein's fire commanders took the first plan that would work rather than compare options ([Satisficing](frameworks/1956-satisficing.md)).
- [Single vs multiple objectives](#single-vs-multiple-objectives) (opposite). "Best" needs one agreed score, so several goals push you towards good enough.
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (tension). You can't claim you found the best answer if you can't check it.
- [Convergent vs divergent](#convergent-vs-divergent) (opposite). With many good answers there is no single best one to chase.

### Easy vs hard to verify

Can you check an answer cheaply, even if finding it was hard? A solved sudoku takes seconds to check. A business strategy or a diagnosis may take years to prove right or wrong.

**Easy**: Generate and check.
- Let the model try many answers and keep the one that passes the checker. This is why code with tests and maths with proofs suit models so well.
- Automate the checker and let it gate releases. A cheap check can run on every output.

**Hard**: Build a check before you trust the output.
- Use expert review, spot audits or a slow real world check. Pick the cheapest one that still catches real errors.
- Keep a person signing off until you have one. Without a check, the person is the check.
- Don't let a model grade its own work where nobody else can. It tends to pass its own mistakes.
- Check the checker. Plant known errors and see how many it catches.

**Sources.** [Well vs ill-structured problems](frameworks/1964-well-vs-ill-structured-problems.md), [NP problems](frameworks/1971-np-problems.md), [Tame vs wicked problems](frameworks/1973-tame-vs-wicked-problems.md)

**Correlated with**

- [Inert vs reflexive](#inert-vs-reflexive) (logic). By [Goodhart's law](frameworks/1975-goodharts-law.md) a cheap check stops working once people are judged on it.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (logic). Feedback is the world checking your answer for you, so a hard check means slow feedback. They still differ. Verifying is checking one answer before you act on it. Feedback is the world grading you after you act, over many tries. A sudoku is easy to check but teaches you little about the next one. A doctor can't prove a diagnosis on the day, yet learns over years which calls turned out right.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (by definition). A test for the answer is part of what Simon means by [well-structured](frameworks/1964-well-vs-ill-structured-problems.md).
- [Single vs multiple objectives](#single-vs-multiple-objectives) (logic). With no single score there is no simple check.
- [Satisficing vs optimising](#satisficing-vs-optimising) (tension). You can't claim the best answer if you can't check it.
- [Private vs accountable](#private-vs-accountable) (tension). You can only defend a choice if someone can check it, so a choice that is hard to verify is hard to account for.
- [Tractable vs intractable search](#tractable-vs-intractable-search) (independent). [NP problems](frameworks/1971-np-problems.md) are the textbook case of hard to find and easy to check.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings for job applicants against past hires, but fairness was never in the score ([Need for interpretability](frameworks/2017-need-for-interpretability.md)).
- [Discrete vs continuous](#discrete-vs-continuous) (logic). A continuous answer is only close or far, so checking it needs a tolerance someone has to pick.
- [Convergent vs divergent](#convergent-vs-divergent) (logic). One right answer can be checked against a key. Many good answers need someone to judge them.

### Complete vs incomplete goal

Does the score capture everything you want? A machine that sorts letters by postcode has a complete goal, since reading the code right is the whole job. From 2014 Amazon built a tool that rated job applicants by learning from ten years of past CVs. It marked down CVs with the word "women's", because fairness was never in the score. Finale Doshi-Velez and Been Kim call this gap incompleteness.

**Complete**: Optimise the score.
- Push the metric up. If the metric is the whole job, pushing it up is doing the job.
- Use it to gate releases. A better score means a better model.

**Incomplete**: Watch what the score leaves out.
- List the wants the metric misses. Ask users and affected groups what a high score could still get wrong.
- Track those wants as guardrail metrics. A guardrail is a measure you don't optimise but won't let fall.
- Have people read outputs for harms no number catches. Amazon's CV tool learnt to mark down women because nobody had scored it for fairness.
- Expect the model to find the gaps in the score and exploit them. This is called reward hacking.

**Sources.** [Goodhart's law](frameworks/1975-goodharts-law.md), [Campbell's law](frameworks/1976-campbells-law.md), [Need for interpretability](frameworks/2017-need-for-interpretability.md)

**Correlated with**

- [Easy vs hard to verify](#easy-vs-hard-to-verify) (independent). A score can be quick to check and still miss what you want. Amazon could test its star ratings against past hires, but that only checked the score.
- [Well-posed vs ill-posed](#well-posed-vs-ill-posed) (logic). If you can't state the goal, you can't score all of it. The reverse doesn't hold, since rating CVs looked well posed and the score still left out fairness.
- [Single vs multiple objectives](#single-vs-multiple-objectives) (bundled). Doshi-Velez and Kim ([Need for interpretability](frameworks/2017-need-for-interpretability.md)) count goals that pull against each other as one kind of gap. But a car buyer who writes down every want and sets the weights has many objectives and a complete goal.
- [Shared vs contested values](#shared-vs-contested-values) (logic). When people disagree on what a good result is, any one score takes a side and leaves the other wants out.
- [Private vs accountable](#private-vs-accountable) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score.
- [Inert vs reflexive](#inert-vs-reflexive) (study). By [Goodhart's law](frameworks/1975-goodharts-law.md) people work on whatever the score leaves out. In 1902 Hanoi paid a bounty for each rat tail, so people cut off the tails and let the rats go to breed. [Campbell's law](frameworks/1976-campbells-law.md) adds that teachers drill the test and drop the parts of the subject it doesn't cover.
- [Commensurable vs incommensurable values](#commensurable-vs-incommensurable-values) (logic). A single score has to price everything, so a sacred value is left out or priced where nobody can see.
- [Even vs lopsided errors](#even-vs-lopsided-errors) (logic). Plain accuracy counts a missed cancer and a false scare as the same mistake.
- [Skin in the game vs none](#skin-in-the-game-vs-none) (logic). An agent scored on fees or loans signed has a score that leaves out the owner's loss.

### One-shot vs sequential

Is it a single choice, or a chain where each step shapes the next? Choosing a paint colour is one shot. Running a project or treating a long illness is a series of moves, and it's hard to tell which early move caused the final result.

**One-shot**: Get the single call right.
- Put the effort in before you act. There is no second go.
- Use the best model and the most checks you can afford. All the value rests on this one output.

**Sequential**: Act, watch and adjust.
- Treat it as a trade off between trying new moves and repeating good ones. Bandits and reinforcement learning are built for this.
- Credit each move with its share of the final result. Otherwise the last move gets the blame for what an early one caused.
- Watch for effects that show up late. Judge a move by where it led, not by the next step.
- Keep room to change course. Each step should leave the next one open.

**Sources.** [Multi-armed bandit](frameworks/1933-multi-armed-bandit.md), [Exploration vs exploitation](frameworks/1991-exploration-vs-exploitation.md), [Task environment properties](frameworks/1995-task-environment-properties.md)

**Correlated with**

- [Transparent vs opaque causes](#transparent-vs-opaque-causes) and [Kind vs wicked feedback](#kind-vs-wicked-feedback) (study). In Senge's [beer game](frameworks/1990-detail-vs-dynamic-complexity.md) delays between moves and results hide which move caused what.
- [Known vs unknown odds](#known-vs-unknown-odds) (opposite). In a [bandit](frameworks/1933-multi-armed-bandit.md) problem each choice teaches you something, so repeating the choice slowly turns unknown odds into known ones.
- [Reversible vs irreversible](#reversible-vs-irreversible) (opposite). A chain of moves usually gives you a chance to correct course, so sequential problems lean towards the reversible end. Watch the name clash. [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) call each try at a wicked problem a one-shot operation, but they mean it can't be undone. That is a point about reversibility, not about how many moves there are.
- [Test vs watch](#test-vs-watch) (opposite). Each pull of a [bandit](frameworks/1933-multi-armed-bandit.md) is a small test, so a chain of choices lets you test as you go. Thompson picked each new patient's treatment at random, weighted towards whichever looked better so far.
- [Additive vs multiplicative](#additive-vs-multiplicative) (by definition). The gap between the crowd and the single player only opens over repeated plays. For a single toss of Peters' coin the crowd's average is a fair guide, and the harm builds up toss by toss ([Ergodicity](frameworks/2016-ergodicity.md)).

### Reversible vs irreversible

Can you undo it if it goes wrong? Trying a new recipe is a two way door. Selling the family home or cutting off a leg is a one way door.

**Reversible**: Move fast and let the model act.
- Ship small changes often and learn from what breaks. You can roll back.
- Let agents act without sign off. A mistake costs an undo, not a disaster.

**Irreversible**: Slow down and put a person at the door.
- Require human sign off for actions that can't be undone. Deleting data, sending money and emailing customers are the usual ones.
- Give agents a dry run mode. They show what they would do, and a person approves it.
- Turn one way doors into two way ones where you can. Staging, soft deletes and a delay before a send all buy you an undo.
- Gate only the actions that are hard to undo. Gating everything trains people to click approve without reading.

**Sources.** [Tame vs wicked problems](frameworks/1973-tame-vs-wicked-problems.md), [One-way vs two-way doors](frameworks/2015-one-way-vs-two-way-doors.md)

**Correlated with**

- [Survivable vs ruinous](#survivable-vs-ruinous) (by definition). All ruin is irreversible, but not every irreversible choice ruins you.
- [Loose vs tight coupling](#loose-vs-tight-coupling) (study). In [Normal accidents](frameworks/1984-normal-accidents.md) faults cascade into damage that can't be undone before anyone can step in.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (bundled). [Rittel and Webber](frameworks/1973-tame-vs-wicked-problems.md) note you can't learn by trial and error when each try leaves a mark.
- [Familiar vs novel to the solver](#familiar-vs-novel-to-the-solver) (bundled). Simon's [non-programmed decisions](frameworks/1960-programmed-vs-non-programmed-decisions.md) are new and carry high stakes.
- [One-shot vs sequential](#one-shot-vs-sequential) (opposite). A chain of moves usually gives you a chance to correct course. Rittel and Webber's "one-shot operation" means a choice that can't be undone, so it belongs here rather than on that axis.
- [Private vs accountable](#private-vs-accountable) (logic). Bezos argues one-way doors deserve a slow process with many views ([One-way vs two-way doors](frameworks/2015-one-way-vs-two-way-doors.md)), and that brings scrutiny.
- [Test vs watch](#test-vs-watch) (logic). You can't run a fair test of a one way door, because there is no going back to try the other side.
- [Convex vs concave payoff](#convex-vs-concave-payoff) (logic). Cheap two way doors make tinkering convex, because you keep what works and walk back from what fails.

### Survivable vs ruinous

Could one bad outcome take you out of the game for good? If so, the average result over many tries is useless, because you won't get many tries. Russian roulette has good odds and still isn't worth playing.

**Survivable**: Maximise the average.
- Run a model that is right more often than not. Losses can be absorbed, so the average is what counts.
- Accept some big misses. You will be around to learn from them.

**Ruinous**: Avoid ruin first and optimise second.
- Put hard limits on what the model can do, whatever its confidence. Limits hold when the model is wrong, and confidence doesn't.
- Have a fallback ready. When the model fails, something safe should take over.
- Never let average accuracy justify a small chance of disaster. A model that is 99.9% right and can wipe you out will get there given enough tries.
- Count tries, not just odds. A one in ten thousand chance per decision is close to certain across a million decisions.

**Sources.** [Fourth quadrant](frameworks/2008-fourth-quadrant.md), [Fragile, robust and antifragile](frameworks/2012-fragile-robust-and-antifragile.md), [Ergodicity](frameworks/2016-ergodicity.md)

**Correlated with**

- [Thin vs fat tails](#thin-vs-fat-tails) (bundled). The [Fourth quadrant](frameworks/2008-fourth-quadrant.md) and [Ergodicity](frameworks/2016-ergodicity.md) both warn that one extreme loss can end the game.
- [Reversible vs irreversible](#reversible-vs-irreversible) (by definition). Ruin is the worst kind of choice you can't undo.
- [Loose vs tight coupling](#loose-vs-tight-coupling) (study). Tight systems let small faults cascade into a meltdown ([Normal accidents](frameworks/1984-normal-accidents.md)).
- [Plentiful vs scarce data](#plentiful-vs-scarce-data) (logic). You can't learn from your own ruin, because it only happens once.
- [Additive vs multiplicative](#additive-vs-multiplicative) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin. Peters' coin game never wipes anyone out. It just makes the typical player a little poorer each round ([Ergodicity](frameworks/2016-ergodicity.md)).
- [Convex vs concave payoff](#convex-vs-concave-payoff) (logic). A bet that can ruin you is the most concave payoff there is.
- [Even vs lopsided errors](#even-vs-lopsided-errors) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.

### Additive vs multiplicative

Does the average across many players match what one player gets over time? When gains and losses add up, it does. When they compound, it may not. In Ole Peters' coin game heads grows your wealth by 50% and tails shrinks it by 40%. The crowd's average rises 5% a round, while a typical player loses about 5% a round. When the two averages differ, the game is called non-ergodic.

**Additive**: Judge by the average across cases.
- Use expected value per decision as the test. Gains and losses sum, so the average is what you get.
- Compare models on mean return. One bad case costs only itself.

**Multiplicative**: Judge by what one path does over time.
- Simulate long runs of the model's decisions compounding, not one step. A trading model that wins on average per trade can still drain the account.
- Size each bet so a run of losses can't sink you. The Kelly rule sets each stake as a share of what you have, so you never bet the lot.
- Report the typical path, not the average one. The average is pulled up by a lucky few, while the median shows what a typical run gets.
- Watch for losses that shrink your base. Losing half needs a doubling to get back.

**Sources.** [Ergodicity](frameworks/2016-ergodicity.md)

**Correlated with**

- [Survivable vs ruinous](#survivable-vs-ruinous) (by definition). Ruin is the extreme case, since a ruined player gets nothing over time whatever the crowd's average says. But the gap can open without ruin, and the coin game never wipes anyone out.
- [Thin vs fat tails](#thin-vs-fat-tails) (logic). Compounding piles the gains on a lucky few. In the coin game the crowd's average keeps rising only because a handful of players get vastly rich.
- [One-shot vs sequential](#one-shot-vs-sequential) (by definition). The gap only opens over repeated plays. For a single toss the crowd's average is a fair guide, and the harm builds up toss by toss.

### Convex vs concave payoff

Does a swing in results help you or hurt you? A drug company testing many compounds loses a little on each failure and gains hugely from one hit, so more variety is good for it. A tightrope walker gains nothing from a lucky gust and can lose everything to an unlucky one. When the downside is small and the upside large, the payoff is called convex. This is a different convex from the one in optimisation, which is about the shape of the search, not the shape of your bet.

**Convex**: Try lots of things.
- Run many experiments. Small cheap failures and rare big wins mean more tries pay off.
- Let the model propose wild ideas. A bad idea costs little, and a good one can pay for all the rest.

**Concave**: Cut variance.
- Prefer the dull, predictable model over the clever one with rare failures. The rare failure costs more than the clever gains are worth.
- Add limits that cap the downside. A cap turns an open ended loss into a known one.
- Change your exposure if you can't change the world. Make failures cheap, for example by testing in a sandbox before going live.

**Sources.** [Fragile, robust and antifragile](frameworks/2012-fragile-robust-and-antifragile.md), [Fourth quadrant](frameworks/2008-fourth-quadrant.md)

**Correlated with**

- [Survivable vs ruinous](#survivable-vs-ruinous) (logic). A bet that can ruin you is the most concave payoff there is.
- [Thin vs fat tails](#thin-vs-fat-tails) (bundled). Taleb's [Fourth quadrant](frameworks/2008-fourth-quadrant.md) is a fat tailed world met with a payoff whose shape you don't understand. The tails are the world and the payoff is your exposure to it, so you can change the second even when you can't change the first.
- [Reversible vs irreversible](#reversible-vs-irreversible) (logic). Cheap two way doors make tinkering convex, because you keep what works and walk back from what fails ([One-way vs two-way doors](frameworks/2015-one-way-vs-two-way-doors.md)).

### Even vs lopsided errors

Do false alarms and misses cost the same? A smoke alarm that goes off over toast costs you a minute. One that stays quiet in a fire can cost your life, so it should be set to cry wolf. A court leans the other way and would rather free the guilty than jail the innocent. Where to set the bar for saying yes depends on what each mistake costs, not just on how often you're right.

**Even**: Maximise accuracy.
- Use the default threshold. A false alarm and a miss cost the same.
- Report one accuracy figure. It tells you all you need when both errors weigh the same.

**Lopsided**: Set the threshold from the costs.
- Put a price on each kind of error. Ask what a miss costs and what a false alarm costs, in the same units.
- Tune the threshold to those prices. A cancer screen should flag far more than it misses.
- Report the two error rates separately, never accuracy alone. A model can score 99% on a rare disease by never flagging anyone.
- Plan for the false alarms. If the model is set to cry wolf, make sure someone can check each alarm quickly.

**Sources.** [Signal detection theory](frameworks/1954-signal-detection-theory.md)

**Correlated with**

- [Survivable vs ruinous](#survivable-vs-ruinous) (logic). When one kind of mistake can ruin you and the other can't, the costs are as lopsided as they get.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (logic). A score that counts every mistake the same leaves the costs out. A model tuned for plain accuracy treats a missed cancer and a false scare as equal.
- [Shared vs contested values](#shared-vs-contested-values) (logic). How much worse a miss is than a false alarm is a value judgement, so people fight over where to set the bar.

### Slack vs time pressure

How long do you have to decide, compared to how fast things change? A pension plan gives you months. A pilot with a failed engine has seconds.

**Slack**: Take your time.
- Use a bigger model and more reasoning steps. The extra seconds cost nothing here.
- Get a second opinion or human review. There is time for someone to catch a mistake.

**Time pressure**: Decide the playbook in advance.
- Work out answers and fallbacks ahead of time. In the moment the model should pick from a plan, not write one.
- Use small fast models with a strict time limit. A slow good answer is useless after the deadline.
- Take the first good enough action. Klein found that expert fire commanders do this rather than compare options.
- Check the deadline is real. A false crisis is a common excuse to skip review.

**Sources.** [Post-normal science](frameworks/1993-post-normal-science.md), [Cynefin](frameworks/1999-cynefin.md), [Tame, wicked and critical](frameworks/2005-tame-wicked-and-critical.md), [Super wicked problems](frameworks/2007-super-wicked-problems.md)

**Correlated with**

- [Loose vs tight coupling](#loose-vs-tight-coupling) (by definition). Perrow defines tight coupling as having no slack, so when a tight system fails it hands you a decision with no time ([Normal accidents](frameworks/1984-normal-accidents.md)).
- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (study). Hammond's [cognitive continuum](frameworks/1987-cognitive-continuum.md) puts tasks with little time at the intuitive end, and Klein's fire lieutenant got out on a gut call ([Conditions for intuitive expertise](frameworks/2009-conditions-for-intuitive-expertise.md)).
- [Satisficing vs optimising](#satisficing-vs-optimising) (tension). With no time to search, you have to settle for good enough. Klein's fire commanders took the first plan that would work rather than compare options ([Satisficing](frameworks/1956-satisficing.md)).
- [Tractable vs intractable search](#tractable-vs-intractable-search) (tension). A search too big to finish, done against the clock, is the worst case.
- [Shared vs contested values](#shared-vs-contested-values) (bundled). [Post-normal science](frameworks/1993-post-normal-science.md) and [super wicked problems](frameworks/2007-super-wicked-problems.md) both join a clock to a fight over values. Grint warns that leaders sometimes call a problem a crisis to justify giving orders ([Tame, wicked and critical](frameworks/2005-tame-wicked-and-critical.md)), so check that the deadline is real.
- [Yours to fix vs needs others to change](#yours-to-fix-vs-needs-others-to-change) (bundled). [Super wicked problems](frameworks/2007-super-wicked-problems.md) join a clock to a world with nobody in charge, so each actor has a reason to wait while time runs out.

### Private vs accountable

Must you explain and defend the choice? A hunch is fine for picking a film. A loan refusal, a court ruling or a medical decision may have to be explained, audited or defended in law, which rules out some methods even when they would work better.

**Private**: Use whatever works best.
- Pick the most accurate model, black box or not. Nobody needs to know why.
- Keep light records. Logs are for debugging, not defence.

**Accountable**: Use a method you can explain and keep the records.
- Prefer models you can read. If you must use a black box, be able to give a reason for each decision.
- Log inputs and outputs. You can't defend a decision you can't rebuild.
- Name a person who owns each decision. "The model decided" is not an answer anyone accepts.
- Check the law first. Some decisions, like refusing credit, must come with a reason.

**Sources.** [Accountability](frameworks/1999-accountability.md), [Need for interpretability](frameworks/2017-need-for-interpretability.md)

**Correlated with**

- [Explicit vs tacit know-how](#explicit-vs-tacit-know-how) (tension). Know-how you can't put into words is hard to defend in an audit, so accountability pushes towards written rules like Meehl's [formulas](frameworks/1954-clinical-vs-statistical-prediction.md).
- [Easy vs hard to verify](#easy-vs-hard-to-verify) (tension). You can only defend a choice if someone can check it.
- [Inert vs reflexive](#inert-vs-reflexive) (study). [Campbell's law](frameworks/1976-campbells-law.md) says the more a number decides people's fate, the more they bend it.
- [Shared vs contested values](#shared-vs-contested-values) (logic). A choice that picks winners has to be defended in public ([Post-normal science](frameworks/1993-post-normal-science.md)).
- [Reversible vs irreversible](#reversible-vs-irreversible) (logic). One-way doors get the slow, careful process, and with it more scrutiny ([One-way vs two-way doors](frameworks/2015-one-way-vs-two-way-doors.md)).
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (bundled). Doshi-Velez and Kim say people need explanations when part of the goal, like fairness, safety or the law, never made it into the score ([Need for interpretability](frameworks/2017-need-for-interpretability.md)).
- [Commensurable vs incommensurable values](#commensurable-vs-incommensurable-values) (study). In Tetlock's hospital study, a manager who spent money on equipment instead of a child's transplant after long thought drew the most outrage of any version ([Taboo trade-offs](frameworks/1997-taboo-trade-offs.md)). Even weighing a sacred value in public counts against you.
- [Skin in the game vs none](#skin-in-the-game-vs-none) (independent). Accountable means you must explain the choice, while skin in the game means you pay for it. A judge gives reasons and loses nothing if wrong. A gambler pays for every bad bet and explains nothing.

### Skin in the game vs none

Does whoever makes the call pay if it goes wrong? A shopkeeper pricing their own stock does. A broker paid for each loan they sign, whether or not it is repaid, does not, and will sign worse loans. Michael Jensen and William Meckling called the cost of this gap an agency cost. An AI model never pays for its own mistakes, so it starts at the hard end.

**Skin in the game**: Let the decider decide.
- Trust their judgement. Someone who pays for mistakes learns from them and has the right reasons to care.
- Keep oversight light. Their own loss is the check.

**None**: Tie the model to someone who pays.
- Put a named person or team on the hook for the model's outputs. A model never bears its own losses.
- Judge that team on outcomes. Ask what happened to the people the model affected, not how often it ran.
- Watch the incentives of whoever tunes the model. They are often scored on use, so add harm avoided to how they are judged.
- Make sure the losses get reported back. A cost that lands on someone else is one the team never hears about.

**Sources.** [Agency costs](frameworks/1976-agency-costs.md)

**Correlated with**

- [Private vs accountable](#private-vs-accountable) (independent). Accountable means you must explain the choice. Skin in the game means you pay for it. A judge must give reasons and loses nothing if wrong. A gambler pays for every bad bet and explains nothing to anyone.
- [Kind vs wicked feedback](#kind-vs-wicked-feedback) (logic). If the cost lands on someone else, the decider may never hear about it, so they can't learn from it.
- [Complete vs incomplete goal](#complete-vs-incomplete-goal) (logic). The agent is scored on something of their own, like fees or loans signed, and the owner's loss is left out of that score.

## What changes at the hard end

Read down the actions and the same move keeps turning up. Near the easy ends you can trust the test you ran before launch. A held-out test set predicts how the model will do in production, so you can automate fully, monitor lightly and plan the project like normal engineering. Spending months on live experiments or fallbacks here is waste.

As a problem moves towards the hard ends, the offline test stops being enough to decide on. What replaces it comes in a set order. First you pair the model with a checker, like tests, a rules engine or an expert, and let it act alone only where the checker can confirm the output. Next you stop trusting offline tests as the gate at all. You ship to small groups, run variants side by side and measure what happens downstream rather than how accurate the model is. At the far end you need a way to take the model out of the loop, such as people who can take over, a kill switch or a freeze on automated decisions when inputs stop looking like the training data. These four steps line up with the clear, complicated, complex and chaotic domains of [Cynefin](frameworks/1999-cynefin.md).

A real problem sits near the hard end of several axes at once, and their actions can pull against each other. A drifting world says retrain often and ship fast, while a ruinous one says put a person at the door. When they clash, the action furthest along that order wins. A fallback and a cap on losses come before any experiment, and an experiment comes before trust in the offline test.

Both stories in the [README](README.md) show someone running the easy end playbook on a hard end problem. The reverse is a mistake too, just a cheaper one. Building bandits and kill switches for a stable task you can check in seconds wastes months you could have spent shipping it.

## Grain and horizon

Where a problem sits on most axes depends on how closely you look and over what time. One boiler breaking down is random, but a fleet of ten thousand breaks down at a steady rate. Weather is chaotic two weeks out, while climate is steady over decades. So before you place a problem on any axis, say what scale and what timescale you mean, or the same problem will get tagged two different ways.

Split a task into its separate decisions before you tag it. The cardiology story in the [README](README.md) is one task with two problems inside it. Putting in a stent is a practised skill with fast, clear feedback. Deciding whether to put one in is a slow, statistical call where your gut misleads you. Tag the task as a whole and you average two different problems into one that doesn't exist.

Also ask whether you are deciding one case or setting a policy for many. In 1990 Donald Redelmeier and Amos Tversky gave doctors the same case in two forms. Seen as one patient, a student with fatigue got an extra $20 blood test 30% of the time. Seen as one of a group of patients just like them, the figure was 17% ([Individual vs group decisions](frameworks/1990-individual-vs-group-decisions.md)). A single case feels special, so it gets the extra test. But a doctor who sees the same kind of patient every week is setting a policy whether they mean to or not, and should judge the choice that way.
