# Evaluating gambles using dynamics 

Ole Peters ${ }^{1,2}$ and Murray Gell-Mann ${ }^{2}$<br>${ }^{1}$ London Mathematical Laboratory, 14 Buckingham Street, London WC2N 6DF, UK.<br>${ }^{2}$ Santa Fe Institute, 1399 Hyde Park Road, Santa Fe, NM, 87501, USA<br>o.peters@lml.org.uk, mgm@santafe.edu


#### Abstract

Gambles are random variables that model possible changes in monetary wealth. Classic decision theory transforms money into utility through a utility function and defines the value of a gamble as the expectation value of utility changes. Utility functions aim to capture individual psychological characteristics, but their generality limits predictive power. Expectation value maximizers are defined as rational in economics, but expectation values are only meaningful in the presence of ensembles or in systems with ergodic properties, whereas decision-makers have no access to ensembles and the variables representing wealth in the usual growth models do not have the relevant ergodic properties. Simultaneously addressing the shortcomings of utility and those of expectations, we propose to evaluate gambles by averaging wealth growth over time. No utility function is needed, but a dynamic must be specified to compute time averages. Linear and logarithmic "utility functions" appear as transformations that generate ergodic observables for purely additive and purely multiplicative dynamics, respectively. We highlight inconsistencies throughout the development of decision theory, whose correction clarifies that our perspective is legitimate. These invalidate a commonly cited argument 15 for bounded utility functions.


## I. PRELIMINARIES

Over the past few years we have explored a simple but conceptually deep and often counter-intuitive change of perspective that resolves important problems in economic theory. Here we illustrate this conceptual change by resolving the general gamble problem in a very simple setup. For clarity of exposition we limit ourselves to the context of an individual evaluating gambles in situations where any attendant circumstances other than monetary wealth can be disregarded.

Currently the dominant formalism for treating this problem is utility theory. Utility theory was born out of the failure of the following behavioral null model: individuals were assumed to optimize changes in the expectation values of their wealth. We argue that this null model is a priori a bad starting point because the expectation value of wealth does not generally reflect what happens over time. We propose a different null model of human behavior that eliminates, in many cases, the need for utility theory: an individual optimizes what happens to his wealth as time passes.

The question whether the time average of an observable is well represented by an appropriate expectation value dates back to the $19^{\text {th }}$-century development of statistical mechanics [7] and is the origin of the field called "ergodic theory." In the following we will identify, for different stochastic processes, stationary independent increments. Being stationary and independent these observables have many ergodic properties, of which the following specific property is relevant here.

## Ergodic property (equality of averages):

The expectation value of the observable is a constant (independent of time), and the finite-time average of the observable converges to this constant with probability one as the averaging time tends to infinity.

Whether an observable possesses this property is crucial when assessing the signifcance of its expectation value. We will refer to observables with this property as "ergodic observables."

Gambles are the formal basis of decision theory. Decision theory studies mathematical models of situations that create an internal conflict and necessitate a decision. For instance we may wish to model the situation of being offered a lottery ticket. The conflict is between the unpleasant certainty that we have to pay for the ticket, and the pleasant possibility that we may win the jackpot. It necessitates the decision whether to buy a ticket or not. Although economics deals with many types of decisions, not all of which are monetary, the quantitative treatment of the gamble problem is central to many branches of economics including utility theory, decision theory, game theory, and asset pricing theory which in turn informs macroeconomics, as has been argued convincingly 6 .

We will be dealing with mathematical models but use a common suggestive nomenclature. In this section we write in SMALL CAPITALS those terms of everyday language that in the following will refer to mathematical objects and operations.

A gamble is a set of possible changes in monetary wealth $\Delta W(n)$ with associated probabilities $p_{n}(n)$, where $n$ are integers designating outcomes (or elementary events). For convenience, we order outcomes such that $\Delta W(n+1)>\Delta W(n)$. Different gambles are compared, the decision being which to subject one's wealth to, and more generally to what extent.

Gambles are versatile models, useful to describe a number of real-world prospects. An insurance contract may be modeled as a GAMBLE, as may an investment. Lotteries are important in the historical development of decision theory. Here, possible payouts $D(n)$ are
purchased for a ticket price, $P$, leading to changes in monetary wealth, $\Delta W(n)=D(n)-P$, that are negative up to some value of $n$ and then positive. This creates a decision problem, when comparing to the option of DOING NOTHING: the certain unpleasant prospect of LOSING the TICKET PRICE has to be weighed against the uncertain prospect of WINNING one of the $n_{\text {max }}$ POSSIBLE PAYOUTS.

## II. OUTLINE

Section III is a modern treatment of the problem, using dynamics, that is, we use information about temporal behavior, not exclusively measure-theoretic probabilistic information. Expectation values play a central role in economics, essentially for two reasons. Firstly, the expectation value of any observable is, by definition, the average over $N$ instances of the observable, in the limit $N \rightarrow \infty$. It can therefore be relevant for a member of a large resource-sharing group. Decision theory, however, is concerned with individuals, not with groups, wherefore we disregard this first possible reason for using expectation values. Secondly, an observable may have the ergodic property mentioned in Section 1, in which case it is informative of what happens to an individual over time. We are concerned with the conditions under which this second reason for using expectation values is relevant.

The two key quantities in our treatment are the expected rate of change in wealth, $\frac{1}{\Delta t}\langle\Delta W\rangle$, for additive dynamics, and the expected exponential growth rate of wealth, $\frac{1}{\Delta t}\langle\Delta \ln (W)\rangle$, for multiplicative dynamics. Both quantities were suggested as criteria to evaluate a gamble, $\frac{1}{\Delta t}\langle\Delta W\rangle$ by Huygens 12, and $\frac{1}{\Delta t}\langle\Delta \ln (W)\rangle$ by Laplace [14, although their dynamic significance was overlooked, and time scales $\Delta t$ were usually omitted and implicitly set to 1 .

Section IV discusses the complicated historical development of these two criteria, which we now briefly summarize. It is a partial explanation of the fact that this perspective has lain hidden from view, despite its otherwise implausible problem-solving power, and the availability of its conceptual building blocks for more than 100 years now. It is necessary to re-tell the history of the problem because of an important misconception that forbids the modern perspective.

Bernoulli 3 suggested a quantity similar to the exponential growth rate and called it a "moral expectation," interpreting the logarithm in the exponential growth rate as a psychological re-weighting that humans apply to monetary amounts. This presented a very
simple criterion - maximizing the expected exponential growth rate - in a very complicated way. Laplace [14] corrected Bernoulli formally, though not conceptually, writing down exactly the expected exponential growth rate, though not pointing out its dynamical significance. Menger [15] did decision theory a crucial disservice by undoing Laplace's correction, adding further errors, and writing a persuasive but invalid paper on the subject that concluded incorrectly - in the language of utility theory - that only bounded utility functions are permissible. This forbade the use of either of the dynamically sensible quantities because - forced into the framework of utility theory - the expected rate of change in wealth corresponds to a linear (unbounded) utility function, and the expected exponential growth rate corresponds to a logarithmic (unbounded) utility function.

That unbounded utility functions are not allowed became an established result. We ask here why we cannot use unbounded utility functions, and find no good reason. The arguments for the boundedness of utility functions that we found are not scientifically compelling. A visual representation of the convoluted history of the problem is shown in Fig. 1.

We conclude in Section V that the modern dynamic perspective is legitimate and powerful. Conceptually, its power derives from a new notion of rationality. Reasonable models of wealth cannot be stationary processes. Observables representing wealth then do not have the ergodic property of Section I. and therefore rationality must not be defined as maximizing expectation values of wealth. Rather, we propose as a null model to define rationality as maximizing the time-average growth of wealth. This can be done by first converting the nonergodic processes into stationary independent increments per time unit and then maximizing expectation values of these (identical to their time averages because these observables do have the ergodic property of Section I). These observables are growth rates, and their definition is dictated by the dynamics of the wealth model. Because the gamble problem is phrased without reference to possible causes of the changes in wealth it is entirely general, wherefore our work resolves a host of more specific problems in economics, such as the leverage problem [18], the 300-year-old St Petersburg paradox [19], and the equitypremium puzzle 20. The requirement of boundedness for utility functions is both unnecessary and detrimental to the formalism of decision theory. Our analysis of the history of the problem removes this unnecessary obstacle in the way of using physically sensible criteria in decision theory.

![](https://cdn.mathpix.com/cropped/2025_11_22_acb6f37a8e9fab68ff36g-03.jpg?height=1554&width=1706&top_left_y=197&top_left_x=208)
FIG. 1: History of the classic decision theory problem of evaluating a gamble. The two physically meaningful solutions are on the left and right of the figure. Typically, wealth processes are better modeled as multiplicative than as additive, meaning that Laplace's Criterion is usually more relevant, especially when changes in wealth $\Delta W$ are of similar scale as wealth $W$ itself. Problematic aspects are color-coded in red.

## III. THE DYNAMIC PERSPECTIVE

In order to evaluate a gamble, we ask: how are the dynamics that the gamble is part of to be modeled? In the examples below, an answer to this question allows us to identify stationary independent increments, i.e. to construct an ergodic observable, whose expectation value reflects the behavior over time. Without an answer the problem is underspecified and cannot be resolved without further assumptions, for instance about human psychology.

Requesting the specification of a dynamic exposes as underspecified the original set-up of many problems in economics. Economics treats randomness in a purely measure-theoretic way: possible outcomes are given weights (measures, or probabilities), and the overall quality of a gamble is a weighted average over outcomes, as if all possibilities were materializing simultaneously with different degrees of reality. Modern perspectives on randomness actively downplay the importance of the specific model of measure theory, and emphasize the need to place the aim of the theory above the conditions imposed by a
specific axiomatization. Thus Gell-Mann and Hartle 11 demonstrate that probabilities beyond the interval $[0,1]$ are useful in quantum mechanics, and Tao [24] points out the importance of invariance under extension of the sample space. In our case we argue that a dynamic is needed in addition to the random variable, turning the gamble into a stochastic process. Dynamics means repetition, and requiring the specification of a dynamic is requiring the admission that we live through time, not in a superverse of parallel worlds with which we can share resources.

Gambles are often treated in economics as so-called one-shot games, meaning that they are not part of any dynamic and are assumed to reside outside of time, an assumption that is difficult to describe: "it's more or less impossible to consider any gamble as happening outside of time" [4, p. 3]. The one-shot setup seems ill-conceived to us, and the methods we propose produce little insight into the situations it may represent. It is ill-conceived because any gamble affects what we may be able to do after the gamble. If we lose our house, we cannot bet the house again. The typical decision problem only makes sense in the context of a notion of irreversible time and dynamics - we cannot go back in time after the gamble, and our future will be affected by the decisions we make today. One situation that may be represented by a oneshot game is a bet on a coin toss after which the player (who does not believe in an afterlife) will drop dead. Our methods are not developed for such a-typical cases.

## A. Additive repetition

Treating $\Delta W(n)$ as a (stationary) random variable, repetition of a gamble may mean different things. Firstly, a gamble may be repeated additively, so that the wealth after $T$ rounds of the gamble is

$$
\begin{equation*}
W(t+T \Delta t)=W(t)+\sum_{\tau=1}^{T} \Delta W\left(n_{\tau}\right) \tag{1}
\end{equation*}
$$

where $n_{\tau}$ is the value of the random variable $n$ in the $\tau^{\text {th }}$ round of the gamble.
$W$ does not have the ergodic property of Section I the expectation value is not constant in time,
$\langle W(t+T \Delta t)\rangle=W(t)+T\langle\Delta W\rangle$; the finite-time average, $\bar{W}_{T}=\frac{1}{T} \sum_{\tau=1}^{T} W(t+\tau \Delta t)$, does not converge to the expectation value but rather is a random variable whose distribution broadens indefinitely as $T \rightarrow \infty$. Averaging $N$ realizations of $W(t)$ over a large ensemble ( $N \rightarrow \infty$ ) is not equivalent to averaging $W(t)$ over a long time interval $T \Delta t$ (where $T \rightarrow \infty$ ).

An ergodic observable for Equation (1) exists in the absolute changes in wealth, $W(t+T \Delta t)-W(t)$, whose distribution does not depend on $t$. They are stationary independent increments for this dynamic. The finite-time average of the rate of change in wealth converges to the expectation value of the rate of change with probability one,

$$
\begin{equation*}
\lim _{T \rightarrow \infty} \frac{1}{T \Delta t}[W(t+T \Delta t)-W(t)]=\frac{1}{\Delta t}\langle\Delta W(n)\rangle \tag{2}
\end{equation*}
$$

The expectation value, by definition, is identical to the ensemble average, $\langle\Delta W(n)\rangle= \lim _{N \rightarrow \infty} \frac{1}{N} \sum_{\nu=1}^{N}\left[W_{\nu}(t+\Delta t)-W(t)\right], \quad$ where $W_{\nu}(t+\Delta t)$ are different parallel realizations of wealth after one round of the gamble.

This explains Huygens' Criterion: under additive dynamics as in (Eq. 1), the rate of change in wealth is an ergodic observable, and he who chooses wisely with respect to its expectation value also chooses wisely with respect to the time average.

For the specific dynamics of (Eq. 1) an analysis of this particular observable using our perspective will agree with an analysis using the economics concept of rationality. This is not the case for other observables - Huygens' Criterion defines something very special: an ergodic observable on a non-ergodic wealth process.

Additive dynamics is a simple model, but a moment's reflection reveals that it is very unrealistic: it assumes that possible changes in wealth are not affected by the current level of wealth. The millionnaire and the penniless are modeled as having equal chances of increasing their respective wealths by $\$ 10,000$. For very small gambles ( $\Delta W \ll W$ ) this linear approximation can be valid (the chances of gaining $\$ 0.01$ may really be similar), and indeed the use of Huygens' Criterion emerged from considerations of recreational gambling where an insignificant amount is bet on a game of dice.

![](https://cdn.mathpix.com/cropped/2025_11_22_acb6f37a8e9fab68ff36g-05.jpg?height=1218&width=1741&top_left_y=200&top_left_x=200)
FIG. 2: Assume initial wealth $W\left(t_{0}\right)=\$ 1$ and toss a fair coin. If tails shows $(n=1), W$ decreases to $W\left(t_{0}+\Delta t\right)=\$ 0.60$. If heads shows $(n=2), W$ increases to $W\left(t_{0}+\Delta t\right)=\$ 1.50$. The gamble is repeated (a) additively, linear plot, and (b) multiplicatively, log-linear plot (zoom-ins below the main panels). For clarity, the same sequence of heads and tails is used in both plots, and the color-codings are identical. A typical trajectory is shown (magenta lines). Under (a) the expectation value of $W$ (dashed line) grows in time with the expected rate of change (ergodic observable for this dynamic, blue line), and a trajectory growing exponentially at the expected exponential growth rate (green line) does not describe the long-time behavior. Under (b) the expectation value of $W$ grows exponentially but has nothing to do with the long-time behavior $W$ typically decays exponentially in this case, following the expectation value of the exponential growth rate (ergodic observable for this dynamic). The probability distribution of $W$ is concentrated near the green line at any $t$, while a small number of a-typical trajectories let the mean grow along the dashed line. Linear growth in time at the expected rate of change in $W$ does not describe the long-time behavior.

## B. Multiplicative repetition

A gamble may also be repeated multiplicatively. To simplify notation, we define per-round growth factors $r(n)=\frac{W\left(t_{0}\right)+\Delta W(n)}{W\left(t_{0}\right)}$, where $t_{0}$ is the time just before the first round of the gamble. These inherit their stationarity and independence from $\Delta W(n)$. In this case,

$$
\begin{equation*}
W(t+T \Delta t)=W(t) \prod_{\tau=1}^{T} r\left(n_{\tau}\right), \tag{3}
\end{equation*}
$$

which may be re-written as

$$
\begin{equation*}
W(t+T \Delta t)=W(t) \exp \left[\sum_{\tau=1}^{T} \ln \left(r\left(n_{\tau}\right)\right)\right] . \tag{4}
\end{equation*}
$$

$W$ again lacks the ergodic property of Section the expectation value is not constant in time, $\langle W(t+T \Delta t)\rangle= W(t) \exp [T \ln (\langle r\rangle)] ;$ the finite-time average $\bar{W}_{T}= \frac{1}{T} \sum_{\tau=1}^{T} W(t+\tau \Delta t)$ does not converge to the expectation value but rather is a random variable whose distribution is not stationary. Again, averaging many realizations of $W(t)$ over a large ensemble ( $N \rightarrow \infty$ ) is not equivalent to
averaging $W(t)$ over a long time interval ( $T \rightarrow \infty$ ). Crucially, and in contrast to the additive dynamic (Eq. 1), absolute changes in wealth are not ergodic either. The construction of an ergodic observable now requires a nonlinear transformation.

An ergodic observable for (Eq. 3) exists in the relative changes in wealth, $\frac{W(t+T \Delta t)}{W(t)}$, whose distribution does not depend on $t$. Increments in the logarithm of $W$ are now stationary and independent. The finite-time average of the rate of change in the logarithm of wealth, i.e. the exponential growth rate, converges to the expectation value of the rate of change in the logarithm with probability one,

$$
\begin{equation*}
\lim _{T \rightarrow \infty} \frac{1}{T \Delta t} \ln \left(\frac{W(t+T \Delta t)}{W(t)}\right)=\frac{1}{\Delta t}\langle\Delta \ln W(n)\rangle \tag{5}
\end{equation*}
$$

The expectation value, by definition, is identical to the ensemble average, $\langle\Delta \ln (W(n))\rangle= \lim _{N \rightarrow \infty} \frac{1}{N} \sum_{\nu=1}^{N} \ln \left(\frac{W_{\nu}(t+\Delta t)}{W(t)}\right)$.

This explains Laplace's Criterion: under multiplicative dynamics, the rate of change in the logarithm of wealth is an ergodic observable, and he who chooses wisely with respect to its expectation value also chooses wisely with respect to the time average. Multiplicative repetition is exemplified by geometric Brownian motion, the most influential model in mathematical finance.

Multiplicative repetition usually resembles real wealth processes more closely than additive repetition. For instance, under multiplicative repetition the likelihood of a $\$ 10,000$ increase in wealth is no longer independent of initial wealth. Instead of modelling the millionnaire and the penniless as having equal chances of gaining $\$ 10,000$, multiplicative repetition models them as having equal chances of increasing their respective wealths by $1 \%$. Multiplicative repetition treats zero wealth as a special state, resembling a no-borrowing constraint: betting more than we have can have qualitatively different consequences from betting less than we have. Another important, subtle, and more realistic property of multiplicative repetition is this: time-average growth is impaired by fluctuations. Unlike under additive repetition, the introduction of fluctuations that do not affect the expectation value does reduce the growth rate that is observed with probability one over a long time. In the sense that some dynamical models are more realistic than others, reality imposes a dynamic and corresponding ergodic growth rates on the decision-maker. We may choose which gamble to play but we do not get to choose the mode of repetition.

Equipped with these modern tools, we have no need for the concept of utility. The general gamble problem can be resolved without it, as can - of course - special cases, such as the 300-year-old St Petersburg paradox [18].

## Common error

Prominent texts in decision theory make incorrect statements about the equality of expectation values and time averages, as for instance in the following passage: "If a game is 'favorable' from the point of view of the expectation value and you have the choice of repeating it many times, then it is wise to do so. For eventually, your amount of money and, consequently, your utility are bound to increase (assuming that utility increases if money increases)," [5, p. 98].

This statement by Chernoff and Moses is not true if "favorability" is judged by an observable that does not have the ergodic property of Section I. The general falsity of their statement is evident in panel (b) of Fig. 2, an example of the multiplicative binomial process, studied in detail by Redner 22. Here, $W$ is not ergodic, and the game is "favorable from the point of view of the expectation value" of $W$, but it is certainly not wise to repeat it many times. We will use red text in square boxes to highlight errors and weaknesses in arguments that are commonly believed to be valid.

## IV. HISTORICAL DEVELOPMENT OF DECISION THEORY

In this section we relate the modern treatment of the gamble problem to classic treatments and highlight common misconceptions as well as inconsistencies within the classic view. Aspects of this history, which are included here for completeness, are also discussed in [19]. Menger's ill-conceived rejection of unbounded utility functions was discussed in 17. Its treatment here is briefer and more accessible to those unfamiliar with his original text.

## A. Pre-1713 decision theory - expected wealth

Following the first formal treatment by Fermat and Pascal 10 of random events, it was widely believed that gambles are to be evaluated according to the expected rate of change in monetary wealth. To give it a label, this criterion may be attributed to Huygens [12, who wrote "if any one should put 3 shillings in one hand without telling me which, and 7 in the other, and give me choice of either of them; I say, it is the same thing as if he should give me 5 shillings..."

## Huygens' Criterion:

Maximize the rate of change in the expectation value of wealth,

$$
\begin{equation*}
\frac{1}{\Delta t}\langle\Delta W(n)\rangle . \tag{6}
\end{equation*}
$$

In modern terms, Huygens suggested to maximize the ergodic growth rate assuming additive dynamics.

Nicolas Bernoulli, in a letter to Montmort [16] challenged this notion by introducing a lottery whose expected payout, $\langle D(n)\rangle$, diverges positively with the number of possible outcomes, $n_{\text {max }}$. Since the expected rate of change in wealth $\frac{1}{\Delta t}\langle\Delta W(n)\rangle=\frac{1}{\Delta t}(\langle D(n)\rangle-P)$ is linear in $\langle D(n)\rangle$, it too diverges for any finite ticket price $P$. According to Huygens' Criterion any finite ticket price should be paid for the lottery. However, N. Bernoulli chose the lottery such that large gains only occur with small probability, and found that typical individuals when (hypothetically) offered this lottery were not willing to pay much. This seeming incongruence became known as the St Petersburg paradox. From the modern perspective, the paradox challenges the notion of rationality defined as expectation-optimization, or the assumption of unrealistic additive dynamics. It exposes

## Huygens' weakness

Expectation values are averages over (imagined or real) ensembles of random realizations. The conceptual weakness of Huygens's Criterion is its limited relevance to an individual making a decision. Either the individual has to be part of a large resourcesharing group mimicking a statistical ensemble[27], or the wealth process $W(t)$ has to be additive for the rate of change to be ergodic so that the expectation value reflects how the individual will fare over time. Wealth is often better modeled with multiplicative $d y$ namics.

Specifically, N. Bernoulli proposed the following lottery: a fair coin is tossed until heads appears for the first time. The number of coin tosses, $n \in\{1,2 \ldots\}$, is modeled as a random variable with geometric distribution, $p_{n}(n)=2^{-n}$. The payout as a function of $n$ is $D(n)=\$ 2^{n-1}$. It follows that $D(n)$ is power-law distributed with diverging first moment. The time $\Delta t$ to generate an instance of the random variable, i.e. to play the lottery, is considered independent of $n$ in this study. The lottery is usually presented without restriction on $n$. For a more careful treatment of the problem one must initially require $n \leq n_{\text {max }}$. For more than $n_{\text {max }}$ coin tosses the lottery is declared invalid and no change in wealth occurs. The behavior of the original unrestricted case is investigated as the limit $n_{\text {max }} \rightarrow \infty$.

## B. 1738-1814 decision theory - utility

By 1738 N. Bernoulli's cousin Daniel Bernoulli and Cramer [3, p. 33] had conceptualized the problem as follows. They argued that people attach a value to money
[27] The necessary size of this group grows exponentially in time for multiplicative dynamics 21, 22
that is non-linear in the dollar amount. Cramer had written to N. Bernoulli in 1728: "in their theory [i.e. Huygens' Criterion] mathematicians evaluate money in proportion to its quantity while, in practice, people with common sense evaluate money in proportion to the utility they can obtain from it." Bernoulli suggested a logarithm to map a dollar amount into utility [27] $U_{B}(W)=\ln (W)$. The quantity, Bernoulli suggested, that people consider when deciding whether to take part in the lottery is a combination of the expected gain in their utility if no ticket price were paid, and the loss in utility they suffer when they pay the ticket price. This leads to

## Bernoulli's Criterion:

a lottery ticket is worth buying if the following quantity is positive [3, pp. 26-27]:

$$
\begin{equation*}
\left\langle\Delta U_{B}^{+}\right\rangle-\Delta U_{B}^{-}=\sum_{n}^{n_{\max }} p_{n}(n) \ln \left(\frac{W+D(n)}{W}\right)-\ln \left(\frac{W}{W-P}\right) \tag{7}
\end{equation*}
$$

The first terms on either side of the equation represent the expected gain in logarithmic utility, resulting from the payouts of the lottery. This would represent the net change in utility if tickets were given away for free, $P=0$. The second terms represent the loss in logarithmic utility suffered at the time of purchase, i.e. after the ticket is bought but before any payout from the lottery is received. This is inconsistent with expected-utility theory, as was pointed out in 19 . The conceptual inconsistency may be phrased as follows: Bernoulli thought of utility as a new currency, but currency conversion is always linear - at odds with the non-linear logarithm favored by Bernoulli.

## Bernoulli's inconsistency

Bernoulli's Criterion is mathematically inconsistent with later work in expected-utility theory because Bernoulli did not calculate the expected net change in logarithmic utility. He did not only replace money with utility of money but also computed an observable other than the expected change in this new object.

## C. 1814-1934 decision theory - expected utility

The consensus in the literature on utility theory is that Bernoulli meant to compute the expected net change in utility and made a slight error. Laplace [14] re-told Bernoulli's resolution of the St Petersburg paradox and the invention of utility. Perceiving Bernoulli's Criterion as an error, he implicitly "corrected" Bernoulli's formal inconsistency without mention.

## Laplace's Criterion:

Maximize the expected rate of change in logarithmic utility [14, pp. 439-442],

$$
\begin{equation*}
\frac{1}{\Delta t}\left\langle\Delta U_{B}(W)\right\rangle=\frac{1}{\Delta t} \sum_{n}^{n_{\max }} p_{n}(n)[\ln (W+D(n)-P)-\ln (W)] \tag{8}
\end{equation*}
$$

Later researchers adopted Laplace's corrected criterion. Todhunter 25 followed Laplace, as do modern textbooks in stating that utility is an object encoding human preferences in its expectation value, e.g. [5, 23, 26. Laplace stayed within Bernoulli's conceptual framework and was almost certainly not aware of the physical interpretation of his criterion as the ergodic growth rate under multiplicative dynamics (Eq. 5).

Bernoulli motivated the logarithm by suggesting that the perceived utility change induced by an extra dollar is inversely proportional to total wealth, leading to the differential equation $d U(W)=1 / W$, whose solution is the logarithm. But Bernoulli also considered Cramer's suggestion of $U_{C}=\sqrt{W}$ a good representation of diminishing marginal utility. The modern perspective takes Bernoulli's logarithm more seriously than he himself did. The route to the modern treatment of the gamble problem is to ask: "what if the logarithm was not merely convenient and a good fit to the data, what would be its physical meaning if it truly was a logarithm?" Using the logarithm in exactly the same place as the utility function is equivalent to assuming multiplicative dynamics and constructing an ergodic observable.

## D. Post-1934 decision theory - bounded utility

Karl Menger 15 re-visited Bernoulli's 1738 study, and came to the incorrect conclusion that only bounded utility functions are permissible. Of course, whether a utility function, or anything else, is bounded or not in the limit of diverging wealth is practically irrelevant because financial wealth will always be represented by a finite number, as was pointed out e.g. by Coolidge [8]. However, based on formal arguments Menger drew conclusions for the structure of the permissible formalism, namely he ruled out linear and logarithmic functions as models of behavior, and, equivalently, additive and multiplicative processes as models of wealth. Because of the central role of these dynamical models the development of decision theory suffered from this restriction, and it is satisfying to see that formal arguments against these important models are invalid, as intuition would suggest. Menger must have been unaware of the correction to Bernoulli's work by Laplace. His error may be phrased as using Bernoulli's Criterion instead of Laplace's, and only considering the first term in Bernoulli's Criterion, implicitly setting the ticket price to zero, $P=0$. The invalidity of Menger's claim was pointed out in [19, for a detailed dis-
cussion, see 17. Menger's argument survives as received wisdom. For completeness, we state it here and specify the invalid inferences involved.

## Menger's flawed argument

1. Logarithmic utility resolves the original St Petersburg paradox because it turns exponentially increasing wealth-payouts, $D_{n} \propto \exp (n)$, into linearly increasing utility-payouts $\Delta U(n) \propto n$ for large $n$.
2. If payouts increase even faster, e.g. as the exponential of an exponential, $\exp (\exp (n))$, then expected utility changes will diverge positively as $n_{\text {max }}$ diverges, just as expected wealth changes diverge for exponentially increasing payouts.
3. In such games logarithmic utility predicts that the player will be willing to pay any ticket price, just as linear utility does for exponentially increasing payouts. In this sense logarithmic utility is not qualitatively different from linear utility. For utility theory to achieve the desired generality, utility functions must be bounded.

The argument sounds plausible. If the logarithm specifies the value attached to money, like another currency, then there is no intuitive reason why it should be qualitatively different from a linear function. But the logarithm encoding multiplicative dynamics provides us with additional intuition: multiplicative dynamics imply an absorbing boundary. Unlike under additive dynamics it is impossible to recover from bankruptcy, and this is a qualitative difference. In the coin-toss example in Fig. 2 bankruptcy cannot occur, but in the general gamble under multiplicative dynamics, bankruptcy is possible if at least one possible outcome, $n^{*}$, say, leads to the loss of one's entire wealth, $\Delta W\left(n^{*}\right)=-W\left(t_{0}\right)$, so that the corresponding growth factor is $r\left(n^{*}\right)=0$. The absorbing state $W=0$ can be reached but not escaped from. Closer inspection of Menger's argument reveals that the issue is indeed more nuanced than he thought.

We separate out the first term, for the smallest payout, and write the expected utility change as

$$
\begin{equation*}
\left\langle\Delta U_{B}(W)\right\rangle=p_{n}(1) \ln \left(\frac{W+D(1)-P}{W}\right)+\sum_{n=2}^{n_{\max }} p_{n}(n) \ln \left(\frac{W+D(n)-P}{W}\right) . \tag{9}
\end{equation*}
$$

This form motivates the following evaluation of the three steps in Menger's argument

1. Apart from turning exponential wealth changes into linear utility changes, logarithmic utility also imposes a no-bankruptcy condition. Bankruptcy becomes possible at $P= W+D(1)$. Reflecting this, the limit $\lim _{P \rightarrow W+D(1)}\left\langle\Delta U_{B}(W)\right\rangle$ is negatively divergent for any $n_{\text {max }}$.
2. If payouts increase as the exponential of an exponential then the expected utility change is positively divergent in the limit $n_{\text {max }} \rightarrow \infty$ only for ticket prices satisfying $P<W+D(1)$. The doublelimit $\lim _{P \rightarrow W+D(1)} \lim _{n_{\text {max }} \rightarrow \infty} \frac{1}{\Delta t}\left\langle\Delta U_{B}(W)\right\rangle$ results in the indeterminate form " $-\infty+\infty$." Note that the positive divergence only happens in the unrealistic limit $n_{\text {max }} \rightarrow \infty$, whereas the negative divergence happens at finite $P$. The negative divergence is physically meaningful in that it reflects the impossibility to recover from bankruptcy under multiplicative dynamics.
3. In such games logarithmic utility does not predict that the player will want to pay any finite ticket price. Instead, it predicts that the player will not pay more than $W+D(1)$, irrespective of how $D(n)$ may diverge for large $n$. This is qualitatively different from behavior predicted by Huygens' criterion (linear utility), where under diverging expected payouts no ticket price exists that the player would not be willing to pay. Logarithmic utility, carefully interpreted, resolves the class of problems for which Menger thought it would fail.

Despite a persisting intuitive discomfort, renowned economists accepted Menger's conclusions and considered them an important milestone in the development of utility theory. Menger implicitly ruled out the allimportant logarithmic function that connects utility theory to information theory [9, 13] and provides the most natural connection to the ergodicity argument we have presented. Menger also ruled out the linear function that corresponds to Huygens' Criterion, which utility theory was supposed to generalize.

Requiring boundedness for utility functions is methodologically inapt. It is often stated that a diverging expected utility is "impossible" [5, p. 106], or that it "seems natural" to require all expected utilities to be finite 1 , p. 28-29]. Presumably, these statements reflect the intuitive notion that no real thing can be infinitely useful. To implement this notion in the formalism of decision theory, it was decided to make utility functions bounded. A far more natural way to implement the same notion would be to recognize that money amounts (and quantities of anything physical, anything money could represent) are
themselves bounded, and that this makes any usefulness one may assign to them finite, even if utility functions are unbounded. There is no need to place bounds on $U(W)$ if $W$ itself is bounded.

## V. SUMMARY AND CONCLUSION

Our method starts by recognizing the inevitable nonergodicity of stochastic growth processes, e.g. noisy multiplicative growth. The specific stochastic process implies a set of meaningful observables with ergodic properties, e.g. the exponential growth rate. These observables make use of a mapping that in the tradition of economics is viewed as a psychological utility function, e.g. the logarithm.

The dynamic approach to the gamble problem makes sense of risk aversion as optimal behavior for a given dynamic and and level of wealth, implying a different concept of rationality. Maximizing expectation values of observables that do not have the ergodic property of Section I cannot be considered rational for an individual. Instead, it is more useful to consider rational the optimization of time-average performance, or of expectation values of appropriate ergodic observables. We note that where optimization is used in science, the deep insight is finding the right object to optimize (e.g. the action in Hamiltonian mechanics, or the entropy in the microcanonical ensemble). The same is true in the present case - deep insight is gained by finding the right object to optimize - we suggest time-average growth. Laplace's Criterion interpreted as an ergodic growth rate under multiplicative dynamics avoids the fundamental circularity of the behavioral interpretation. In the latter, preferences, i.e. choices an individual would make, have to be encoded in a utility function, the utility function is passed through the formalism, and the output is the same as the input: the choices an individual would make.

We have repeated here that Bernoulli 3 did not actually compute the expected net change in logarithmic utility, as was pointed out in [19]. Perceiving this as an error, Laplace 14] corrected him implicitly without mention. Later researchers used Laplace's corrected criterion until Menger [15] unwittingly re-introduced Bernoulli's inconsistency and introduced a new error by neglecting the second diverging term, $\Delta U^{-}$. Throughout the twentieth century, Menger's incorrect conclusions were accepted by prominent economists although they noticed, and struggled with, detrimental consequences of the (undetected) error for the developing formalism.

We have presented Menger's argument against unbounded utility functions as it is commonly stated nowadays. This argument is neither formally correct (it ignores the negative divergence of the logarithm), nor compatible with physical intuition (it ignores the absorbing boundary). Laplace's Criterion - contrary to common belief - elegantly resolves Menger-type games.

Logarithmic utility must not be banned formally be-
cause it is mathematically equivalent to the modern method of defining an ergodic observable for multiplicative dynamics. This point of view provides a firm basis on which to erect a scientific formalism. The concepts we have presented resolve the fundamental problem of decsision theory, therefore game theory, and asset pricing. Cochrane's book [6] is important in this context as it sets out clearly that all of asset pricing can be derived from the "basic pricing equation" - precisely the combination of a utility function and expectation values we have critiqued here. He further argues that the methods used in asset pricing summarize much of macroeconomics. The problems listed there as those of greatest importance to the discipline at the moment can be addressed using the modern dynamic perspective.

In presenting our results we have made a judgement call between clarity and generality. We have chosen the most general problem of decision theory, but have treated it specifically for discrete time and wealth changes. Gambles that are continuous in time and wealth changes can be treated along the lines of [18]. The specific St Petersburg problem was treated in detail in [19]. We have contrasted purely additive dynamics with purely multiplicative dynamics. A generalization beyond purely additive or multiplicative dynamics is possible, just as it is possible to define utility functions other than the linear or logarithmic function. This will be the subject of a future publication. The arguments we have outlined are not restricted to monetary wealth but apply to anything that is well modeled by a stochastic growth process. Applications to ecology and biology seem natural.

## Acknowledgments

We thank K. Arrow for discussions that started at the workshop "Combining Information Theory and Game

Theory" in 2012 at the Santa Fe Institute, and for numerous helpful comments during the preparation of the manuscript. OP would like to thank A. Adamou for discussions and a careful reading of the manuscript.

TABLE I: List of symbols
| Symbol | Name and interpretation |
| :--- | :--- |
| $t$ | time |
| $t_{0}$ | time before the first round of a gamble |
| $\Delta t$ | duration of one round of a gamble |
| T | total number of sequential rounds of a gamble |
| $\tau$ | index specifying one sequential round of a gamble |
| N | total number of parallel realizations of a gamble |
| $\nu$ | index specifying one parallel realization of a gamble |
| n | integer specifying an outcome |
| $n^{*}$ | integer specifying an outcome that leads to bankruptcy |
| $n_{\text {max }}$ | number of possible outcomes |
| $n_{\tau}$ | random outcome that occurs in round $\tau$ |
| $W$ | wealth |
| $\bar{W}_{T}$ | finite-time average wealth |
| $W_{\nu}$ | wealth in realization $\nu$ |
| $\Delta W(n)$ | change in wealth from $t$ to $t+\Delta t$ if outcome $n$ occurs |
| $r(n)$ | growth factor if outcome $n$ occurs, $r(n)=\frac{W\left(t_{0}\right)+\Delta W(n)}{W\left(t_{0}\right)}$ |
| $p_{n}(n)$ | probability of outcome $n$ |
| $D(n)$ | payout resulting from a lottery if outcome $n$ occurs |
| $\Delta U(n)$ | change in utility resulting from outcome $n$ |
| P | price for a ticket in a lottery |
| U | utility function |
| $U_{C}$ | Cramer's square-root utility function |
| $U_{B}$ | Bernoulli's logarithmic utility function |
| $\left\langle\Delta U_{B}^{+}\right\rangle$ | expectation value of gains in logarithmic utility at zero ticket price |
| $\langle\cdot\rangle$ | loss in logarithmic utility when reducing $W$ by $P$ |


[1] K. Arrow. The use of unbounded utility functions in expected-utility maximization: Response. Q. J. Econ., 88(1):136-138, 1974.
[2] G. I. Barenblatt. Scaling. Cambridge University Press, 2003.
[3] D. Bernoulli. Specimen Theoriae Novae de Mensura Sortis. Translation "Exposition of a new theory on the measurement of risk" by L. Sommer (1954). Econometrica, 22(1):23-36, 1738.
[4] M. Buchanan. Gamble with time. Nature Phys., 9:3, January 2013.
[5] H. Chernoff and L. E. Moses. Elementary Decision Theory. John Wiley \& Sons, 1959.
[6] J. H. Cochrane. Asset Pricing. Princeton University Press, 2001.
[7] E. G. D. Cohen. Boltzmann and statistical mechanics. In Boltzmann's Legacy 150 Years After His Birth, Atti dei Convegni Lincei, volume 131, pages 9-23. Accademia Nazionale dei Lincei, Rome, 1997.
[8] J. L. Coolidge. An introduction to mathematical probability. Oxford University Press, 1925.
[9] T. M. Cover and J. A. Thomas. Elements of Information Theory. John Wiley \& Sons, 1991.
[10] P. Fermat and B. Pascal. Private correspondence between Fermat and Pascal, 1654.
[11] M. Gell-Mann and J. B. Hartle. Decoherent histories quantum mechanics with one real fine-grained history. Phys. Rev. A, 85:062120(1-12), 2012.
[12] C. Huygens. De ratiociniis in ludo aleae. (On reckoning at Games of Chance). T. Woodward, London, 1657.
[13] J. L. Kelly Jr. A new interpretation of information rate. Bell Sys. Tech. J., 35(4):917-926, July 1956.
[14] P. S. Laplace. Théorie analytique des probabilités. Paris, Ve. Courcier, 2 edition, 1814.
[15] K. Menger. Das Unsicherheitsmoment in der Wertlehre. J. Econ., 5(4):459-485, 1934.
[16] P. R. Montmort. Essay d'analyse sur les jeux de hazard. Jacque Quillau, Paris. Reprinted by the American

Mathematical Society, 2006, 2 edition, 1713.
[17] O. Peters. Menger 1934 revisited. http://arxiv.org/abs/1110.1578, 2011.
[18] O. Peters. Optimal leverage from non-ergodicity. Quant. Fin., 11(11):1593-1602, November 2011.
[19] O. Peters. The time resolution of the St Petersburg paradox. Phil. Trans. R. Soc. A, 369(1956):4913-4931, December 2011.
[20] O. Peters and A. Adamou. Stochastic market efficiency. SFI working paper 13-06-022, 2013.
[21] O. Peters and W. Klein. Ergodicity breaking in geometric Brownian motion. Phys. Rev. Lett., 110(10):100603, March 2013.
[22] S. Redner. Random multiplicative processes: An elementary tutorial. Am. J. Phys., 58(3):267-273, March 1990.
[23] P. A. Samuelson. Foundations of economic analysis. Harvard University Press, enlarged edition, 1983.
[24] T. Tao. Topics in random matrix theory. American Mathematical Society, 2012.
[25] I. Todhunter. A history of the mathematical theory of probability. Macmillan \& Co., 1865.
[26] J. von Neumann and O. Morgenstern. Theory of games and economic behavior. Princeton University Press, 1944.
[27] We know today that this conceptualization is problematic. From the requirement that there be no distinguished currency follows that a change in currency by some factor must lead to a corresponding change in any physical quantity that is some power of that factor, but the logarithm is not a power law, see [2, p. 17 ff].

