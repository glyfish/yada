# Election Predictions as Martingales: An Arbitrage Approach 

Nassim Nicholas Taleb<br>Tandon School of Engineering, New York University 3rd Version, October 2017<br>Forthcoming, Quantitative Finance

## I. Introduction

A standard result in quantitative finance is that when the volatility of the underlying security increases, arbitrage pressures push the corresponding binary option to trade closer to $50 \%$, and become less variable over the remaining time to expiration. Counterintuitively, the higher the uncertainty of the underlying security, the lower the volatility of the binary option. This effect should hold in all domains where a binary price is produced - yet we observe severe violations of these principles in many areas where binary forecasts are made, in particular those concerning the U.S. presidential election of 2016. We observe stark errors among political scientists and forecasters, for instance with 1) assessors giving the candidate D. Trump between $0.1 \%$ and $3 \%$ chances of success, 2 ) jumps in the revisions of forecasts from $48 \%$ to $15 \%$, both made while invoking uncertainty.

Conventionally, the quality of election forecasting has been assessed statically by De Finetti's method, which consists in minimizing the Brier score, a metric of divergence from the final outcome (the standard for tracking the accuracy of probability assessors across domains, from elections to weather). No intertemporal evaluations of changes in estimates appear to have been imposed outside the quantitative finance practice and literature. Yet De Finetti's own principle is that a probability should be treated like a two-way "choice" price, which is thus violated by conventional practice.

![](https://cdn.mathpix.com/cropped/2025_11_22_48b614b3d11371e11879g-1.jpg?height=505&width=798&top_left_y=1832&top_left_x=208)
Fig. 1. Election arbitrage "estimation" (i.e., valuation) at different expected proportional votes $Y \in[0,1]$, with $s$ the expected volatility of $Y$ between present and election results. We can see that under higher uncertainty, the estimation of the result gets closer to 0.5 , and becomes insensitive to estimated electoral margin.

![](https://cdn.mathpix.com/cropped/2025_11_22_48b614b3d11371e11879g-1.jpg?height=483&width=510&top_left_y=702&top_left_x=1263)
Fig. 2. $X$ is an open non observable random variable (a shadow variable of sorts) on $\mathbb{R}, Y$, its mapping into "votes" or "electoral votes" via a sigmoidal function $S($.$) , which maps one-to-one, and the binary as the expected value$ of either using the proper corresponding distribution.

In this paper we take a dynamic, continuous-time approach based on the principles of quantitative finance and argue that a probabilistic estimate of an election outcome by a given "assessor" needs be treated like a tradable price, that is, as a binary option value subjected to arbitrage boundaries (particularly since binary options are actually used in betting markets). Future revised estimates need to be compatible with martingale pricing, otherwise intertemporal arbitrage is created, by "buying" and "selling" from the assessor.

A mathematical complication arises as we move to continuous time and apply the standard martingale approach: namely that as a probability forecast, the underlying security lives in $[0,1]$. Our approach is to create a dual (or "shadow") martingale process $Y$, in an interval $[L, H]$ from an arithmetic Brownian motion, $X$ in $(-\infty, \infty)$ and price elections accordingly. The dual process $Y$ can for example represent the numerical votes needed for success. A complication is that, because of the transformation from $X$ to $Y$, if $Y$ is a martingale, $X$ cannot be a martingale (and vice-versa).

The process for $Y$ allows us to build an arbitrage relationship between the volatility of a probability estimate and that of the underlying variable, e.g. the vote number. Thus we are able to show that when there is a high uncertainty about the final outcome, 1) indeed, the arbitrage value of the forecast (as a binary option) gets closer to $50 \%$ and 2) the estimate should not undergo large changes even if polls or other bases
show significant variations ${ }^{1}$
The pricing links are between 1) the binary option value (that is, the forecast probability), 2) the estimation of $Y$ and 3 ) the volatility of the estimation of $Y$ over the remaining time to expiration (see Figures 1 and 2 ).

## A. Main results

For convenience, we start with our notation. Notation:
$Y_{0} \quad$ the observed estimated proportion of votes expressed in $[0,1]$ at time $t_{0}$. These can be either popular or electoral votes, so long as one treats them with consistency.
$T$ period when the irrevocable final election outcome $Y_{T}$ is revealed, or expiration.
$t_{0} \quad$ present evaluation period, hence $T-t_{0}$ is the time until the final election, expressed in years.
$s$ annualized volatility of $Y$, or uncertainty attending outcomes for $Y$ in the remaining time until expiration. We assume $s$ is constant without any loss of generality -but it could be time dependent.
$B($.$) "forecast probability", or estimated continuous-$ time arbitrage evaluation of the election results, establishing arbitrage bounds between $B(),. Y_{0}$ and the volatility $s$.

Main results:

$$
\begin{equation*}
B\left(Y_{0}, \sigma, t_{0}, T\right)=\frac{1}{2} \operatorname{erfc}\left(\frac{l-\operatorname{erf}^{-1}\left(2 Y_{0}-1\right) e^{\sigma^{2}\left(T-t_{0}\right)}}{\sqrt{e^{2 \sigma^{2}\left(T-t_{0}\right)}-1}}\right), \tag{1}
\end{equation*}
$$

where

$$
\begin{equation*}
\sigma \approx \frac{\sqrt{\log \left(2 \pi s^{2} e^{\left.2 \operatorname{erf}^{-1}\left(2 Y_{0}-1\right)^{2}+1\right)}\right.}}{\sqrt{2} \sqrt{T-t_{0}}}, \tag{2}
\end{equation*}
$$

$l$ is the threshold needed (defaults to .5), and $\operatorname{erfc}($.$) is the$ standard complementary error function, 1-erf(.), with $\operatorname{erf}(z)= \frac{2}{\sqrt{\pi}} \int_{0}^{z} e^{-t^{2}} d t$. $\square$

We find it appropriate here to answer the usual comment by statisticians and people operating outside of mathematical finance: "why not simply use a Beta-style distribution for $Y$ ?". The answer is that 1) the main purpose of the paper is establishing (arbitrage-free) time consistency in binary forecasts, and 2 ) we are not aware of a continuous time stochastic process that accommodates a beta distribution or a similarly bounded conventional one.

## B. Organization

The remaining parts of the paper are organized as follows. First, we show the process for $Y$ and the needed transformations from a specific Brownian motion. Second, we derive

[^0]the arbitrage relationship used to obtain equation (1). Finally, we discuss De Finetti's approach and show how a martingale valuation relates to minimizing the conventional standard in the forecasting industry, namely the Brier Score.

A comment on absence of closed form solutions for $\sigma$ : We note that for $Y$ we lack a closed form solution for the integral reflecting the total variation: $\int_{t_{0}}^{T} \frac{\sigma}{\sqrt{\pi}} e^{-\operatorname{erf}^{-1}\left(2 y_{s}-1\right)^{2}} d s$, though the corresponding one for $X$ is computable. Accordingly, we have relied on propagation of uncertainty methods to obtain a closed form solution for the probability density of $Y$, though not explicitly its moments as the logistic normal integral does not lend itself to simple expansions [1].

Time slice distributions for $X$ and $Y$ : The time slice distribution is the probability density function of $Y$ from time $t$, that is the one-period representation, starting at $t$ with $y_{0}=\frac{1}{2}+\frac{1}{2} \operatorname{erf}\left(x_{0}\right)$. Inversely, for $X$ given $y_{0}$, the corresponding $x_{0}, X$ may be found to be normally distributed for the period $T-t_{0}$ with

$$
\begin{aligned}
\mathbb{E}(X, T) & =X_{0} e^{\sigma^{2}\left(T-t_{0}\right)}, \\
\mathbb{V}(X, T) & =\frac{e^{2 \sigma^{2}\left(T-t_{0}\right)}-1}{2}
\end{aligned}
$$

and a kurtosis of 3 . By probability transformation we obtain $\varphi$, the corresponding distribution of $Y$ with initial value $y_{0}$ is given by

$$
\begin{array}{r}
\varphi\left(y ; y_{0}, T\right)=\frac{1}{\sqrt{e^{2 \sigma^{2}\left(t-t_{0}\right)}-1}} \exp \left\{\operatorname{erf}^{-1}(2 y-1)^{2}\right. \\
-\frac{1}{2}\left(\operatorname{coth}\left(\sigma^{2} t\right)-1\right)\left(\operatorname{erf}^{-1}(2 y-1)\right.  \tag{3}\\
\left.\left.-\operatorname{erf}^{-1}\left(2 y_{0}-1\right) e^{\sigma^{2}\left(t-t_{0}\right)}\right)^{2}\right\}
\end{array}
$$

and we have $\mathbb{E}\left(Y_{t}\right)=Y_{0}$.
As to the variance, $\mathbb{E}\left(Y^{2}\right)$, as mentioned above, does not lend itself to a closed-form solution derived from $\varphi($.$) , nor$ from the stochastic integral; but it can be easily estimated from the closed form distribution of $X$ using methods of propagation of uncertainty for the first two moments (the delta method).

Since the variance of a function $f$ of a finite moment random variable $X$ can be approximated as $V(f(X))= f^{\prime}(\mathbb{E}(X))^{2} V(X)$ :

$$
\begin{array}{r}
\left.\frac{\partial S^{-1}(y)}{\partial y}\right|_{y=Y_{0}} s^{2} \approx \frac{e^{2 \sigma^{2}\left(T-t_{0}\right)}-1}{2} \\
s \approx \sqrt{\frac{e^{-2 \operatorname{erf}^{-1}\left(2 Y_{0}-1\right)^{2}}\left(e^{2 \sigma^{2}\left(T-t_{0}\right)}-1\right)}{2 \pi}} . \tag{4}
\end{array}
$$

Likewise for calculations in the opposite direction, we find

$$
\sigma \approx \frac{\sqrt{\log \left(2 \pi s^{2} e^{\left.2 \operatorname{erf}^{-1}\left(2 Y_{0}-1\right)^{2}+1\right)}\right.}}{\sqrt{2} \sqrt{T-t_{0}}},
$$

which is (2) in the presentation of the main result.
Note that expansions including higher moments do not bring a material increase in precision - although $s$ is highly

![](https://cdn.mathpix.com/cropped/2025_11_22_48b614b3d11371e11879g-3.jpg?height=1224&width=896&top_left_y=181&top_left_x=151)
Fig. 3. Shows the estimation process cannot be in sync with the volatility of the estimation of (electoral or other) votes as it violates arbitrage boundaries

nonlinear around the center, the range of values for the volatility of the total or, say, the electoral college is too low to affect higher order terms in a significant way, in addition to the boundedness of the sigmoid-style transformations.

## C. A Discussion on Risk Neutrality

We apply risk neutral valuation, for lack of conviction regarding another way, as a default option. Although $Y$ may not necessarily be tradable, adding a risk premium for the process involved in determining the arbitrage valuation would necessarily imply a negative one for the other candidate(s), which is hard to justify. Further, option values or binary bets, need to satisfy a no Dutch Book argument (the De Finetti form of no-arbitrage) (see [4]), i.e. properly priced binary options interpreted as probability forecasts give no betting "edge" in all outcomes without loss. Finally, any departure from risk neutrality would degrade the Brier Score (about which, below) as it would represent a diversion from the final forecast.

Also note the absence of the assumptions of financing rate usually present in financial discussions.

## II. The Bachelier-Style valuation

Let $F($.$) be a function of a variable X$ satisfying

$$
\begin{equation*}
d X_{t}=\sigma^{2} X_{t} d t+\sigma d W_{t} . \tag{5}
\end{equation*}
$$

We wish to show that $X$ has a simple Bachelier option price $B($.$) . The idea of no arbitrage is that a continuously$ made forecast must itself be a martingale.

Applying Itô's Lemma to $F \triangleq B$ for $X$ satisfying (5) yields

$$
d F=\left[\sigma^{2} X \frac{\partial F}{\partial X}+\frac{1}{2} \sigma^{2} \frac{\partial^{2} F}{\partial X^{2}}+\frac{\partial F}{\partial t}\right] d t+\sigma \frac{\partial F}{\partial X} d W
$$

so that, since $\frac{\partial F}{\partial t} \triangleq 0, F$ must satisfy the partial differential equation

$$
\begin{equation*}
\frac{1}{2} \sigma^{2} \frac{\partial^{2} F}{\partial X^{2}}+\sigma^{2} X \frac{\partial F}{\partial X}+\frac{\partial F}{\partial t}=0 \tag{6}
\end{equation*}
$$

which is the driftless condition that makes $B$ a martingale.
For a binary (call) option, we have for terminal conditions $B(X, t) \triangleq F, F_{T}=\theta(x-l)$, where $\theta($.$) is the Heaviside theta$ function and $l$ is the threshold:

$$
\theta(x):= \begin{cases}1, & x \geq l \\ 0, & x<l\end{cases}
$$

with initial condition $x_{0}$ at time $t_{0}$ and terminal condition at $T$ given by:

$$
\frac{1}{2} \operatorname{erfc}\left(\frac{x_{0} e^{\sigma^{2} t}-l}{\sqrt{e^{2 \sigma^{2} t}-1}}\right)
$$

which is, simply, the survival function of the Normal distribution parametrized under the process for $X$.

Likewise we note from the earlier argument of one-to one (one can use Borel set arguments) that

$$
\theta(y):= \begin{cases}1, & y \geq S(l) \\ 0, & y<S(l),\end{cases}
$$

so we can price the alternative process $B(Y, t)=\mathbb{P}\left(Y>\frac{1}{2}\right)$ (or any other similarly obtained threshold $l$, by pricing

$$
B\left(Y_{0}, t_{0}\right)=\mathbb{P}\left(x>S^{-1}(l)\right) .
$$

The pricing from the proportion of votes is given by:

$$
B\left(Y_{0}, \sigma, t_{0}, T\right)=\frac{1}{2} \operatorname{erfc}\left(\frac{l-\operatorname{erf}^{-1}\left(2 Y_{0}-1\right) e^{\sigma^{2}\left(T-t_{0}\right)}}{\sqrt{e^{2 \sigma^{2}\left(T-t_{0}\right)}-1}}\right),
$$

the main equation (1), which can also be expressed less conveniently as

$$
\begin{array}{r}
B\left(Y, \sigma, t_{0}, T\right)=\frac{1}{\sqrt{e^{2 \sigma^{2} t}-1}} \int_{l}^{1} \exp \left(\operatorname{erf}^{-1}(2 y-1)^{2}\right. \\
-\frac{1}{2}\left(\operatorname{coth}\left(\sigma^{2} t\right)-1\right)\left(\operatorname{erf}^{-1}(2 y-1)\right. \\
\left.\left.-\operatorname{erf}^{-1}\left(2 y_{0}-1\right) e^{\sigma^{2} t}\right)^{2}\right) d y
\end{array}
$$

## III. Bounded Dual Martingale Process

$Y_{T}$ is the terminal value of a process on election day. It lives in $[0,1]$ but can be generalized to the broader $[L, H]$, $L, H \in[0, \infty)$. The threshold for a given candidate to win is fixed at $l . Y$ can correspond to raw votes, electoral votes, or any other metric. We assume that $Y_{t}$ is an intermediate realization of the process at $t$, either produced synthetically from polls (corrected estimates) or other such systems.

![](https://cdn.mathpix.com/cropped/2025_11_22_48b614b3d11371e11879g-4.jpg?height=453&width=709&top_left_y=187&top_left_x=162)
Fig. 4. Process and Dual Process

Next, we create, for an unbounded arithmetic stochastic process, a bounded "dual" stochastic process using a sigmoidal transformation. It can be helpful to map processes such as a bounded electoral process to a Brownian motion, or to map a bounded payoff to an unbounded one, see Figure 2.

Proposition 1. Under sigmoidal style transformations $S: x \mapsto y, \mathbb{R} \rightarrow[0,1]$ of the form a) $\frac{1}{2}+\frac{1}{2} \operatorname{erf}(x)$, or b) $\frac{1}{1+\exp (-x)}$, if $X$ is a martingale, $Y$ is only a martingale for $Y_{0}=\frac{1}{2}$, and if $Y$ is a martingale, $X$ is only a martingale for $X_{0}=0$.

Proof. The proof is sketched as follows. From Itô's lemma, the drift term for $d X_{t}$ becomes 1) $\sigma^{2} X(t)$, or 2) $\frac{1}{2} \sigma^{2} \operatorname{Tanh}\left(\frac{X(t)}{2}\right)$, where $\sigma$ denotes the volatility, respectively with transformations of the forms a) of $X_{t}$ and b) of $X_{t}$ under a martingale for $Y$. The drift for $d Y_{t}$ becomes: 1) $\frac{\sigma^{2} e^{-\operatorname{erf}^{-1}(2 Y-1)^{2}} \operatorname{erf}^{-1}(2 Y-1)}{\sqrt{\pi}}$ or 2) $\frac{1}{2} \sigma^{2} Y(Y-1)(2 Y-1)$ under a martingale for $X$. $\square$

We therefore select the case of $Y$ being a martingale and present the details of the transformation a). The properties of the process have been developed by Carr [2]. Let $X$ be the arithmetic Brownian motion (5), with $X$-dependent drift and constant scale $\sigma$ :

$$
d X_{t}=\sigma^{2} X_{t} d t+\sigma d W_{t}, \quad 0<t<T<+\infty .
$$

We note that this has similarities with the OrnsteinUhlenbeck process normally written $d X_{t}=\theta\left(\mu-X_{t}\right) d t+ \sigma d W$, except that we have $\mu=0$ and violate the rules by using a negative mean reversion coefficient, rather more adequately described as "mean repelling", $\theta=-\sigma^{2}$.

We map from $X \in(-\infty, \infty)$ to its dual process $Y$ as follows. With $S: \mathbb{R} \rightarrow[0,1], Y=S(x)$,

$$
S(x)=\frac{1}{2}+\frac{1}{2} \operatorname{erf}(x)
$$

the dual process (by unique transformation since $S$ is one to one, becomes, for $y \triangleq S(x)$, using Ito's lemma (since $S($.$) is$ twice differentiable and $\partial S / \partial t=0$ ):

$$
d S=\left(\frac{1}{2} \sigma^{2} \frac{\partial^{2} S}{\partial x^{2}}+X \sigma^{2} \frac{\partial S}{\partial x}\right) \mathrm{d} t+\sigma \frac{\partial S}{\partial x} d W
$$

which with zero drift can be written as a process

$$
d Y_{t}=s(Y) d W_{t},
$$

for all $t>\tau, \mathbb{E}\left(Y_{t} \mid Y_{\tau}\right)=Y_{\tau}$. and scale

$$
s(Y)=\frac{\sigma}{\sqrt{\pi}} e^{-\operatorname{erf}^{-1}(2 y-1)^{2}}
$$

which as we can see in Figure $5 . s(y)$ can be approximated by the quadratic function $y(1-y)$ times a constant.

![](https://cdn.mathpix.com/cropped/2025_11_22_48b614b3d11371e11879g-4.jpg?height=438&width=711&top_left_y=479&top_left_x=1076)
Fig. 5. The instantaneous volatility of $Y$ as a function of the level of $Y$ for two different methods of transformations of $X$, which appear to not be substantially different. We compare to the quadratic form $y-y^{2}$ scaled by a constant $\frac{1}{\sqrt[3]{\frac{8 \pi}{2}}}$. The volatility declines as we move away from $\frac{1}{2}$ and collapses at the edges, thus maintaining $Y$ in ( 0,1 ). For simplicity we assumed $\sigma=t=1$.

We can recover equation (5) by inverting, namely $S^{-1}(y)=$ erf $^{-1}(2 y-1)$, and again applying Itô's Lemma. As a consequence of gauge invariance option prices are identical whether priced on $X$ or $Y$, even if one process has a drift while the other is a martingale. In other words, one may apply one's estimation to the electoral threshold, or to the more complicated $X$ with the same results. And, to summarize our method, pricing an option on $X$ is familiar, as it is exactly a Bachelier-style option price.

## IV. Relation to De Finetti's Probability Assessor

This section provides a brief background for the conventional approach to probability assessment. De Finetti [3] has shown that the "assessment" of the "probability" of the realization of a random variable in $\{0,1\}$ requires a nonlinear loss function - which makes his definition of probabilistic assessment differ from that of the $\mathrm{P} / \mathrm{L}$ of a trader engaging in binary bets.

Assume that a betting agent in an $n$-repeated two period model, $t_{0}$ and $t_{1}$, produces a strategy $\mathfrak{S}$ of bets $b_{0, i} \in[0,1]$ indexed by $i=1,2, \ldots, n$, with the realization of the binary r.v. $\mathbb{1}_{t_{1}, i}$. If we take the absolute variation of his $\mathrm{P} / \mathrm{L}$ over $n$ bets, it will be

$$
L_{1}(\mathfrak{S})=\frac{1}{n} \sum_{i=1}^{n}\left|\mathbb{1}_{t_{1}, i}-b_{t_{0}, i}\right| .
$$

For example, assume that $\mathbb{E}\left(\mathbb{1}_{t_{1}}\right)=\frac{1}{2}$. Betting on the probability, here $\frac{1}{2}$, produces a loss of $\frac{1}{2}$ in expectation, which is the same as betting either 0 or 1 - hence not favoring the agent to bet on the exact probability.

If we work with the same random variable and non-timevarying probabilities, the $L^{1}$ metric would be appropriate:

$$
L_{1}(\mathfrak{S})=\frac{1}{n}\left|\mathbb{1}_{t_{1}, i}-\sum_{i=1}^{n} b_{t_{0}, i}\right| .
$$

De Finetti proposed a "Brier score" type function, a quadratic loss function in $L^{2}$ :

$$
L_{2}(\mathfrak{S})=\frac{1}{n} \sum_{i=1}^{n}\left(\mathbb{1}_{t_{1}, i}-b_{t_{0}, i}\right)^{2}
$$

the minimum of which is reached for $b_{t_{0}, i}=\mathbb{E}\left(\mathbb{1}_{t_{1}}\right)$.
In our world of continuous time derivative valuation, where, in place of a two period lattice model, we are interested, for the same final outcome at $t_{1}$, in the stochastic process $b_{t}, t_{0} \geq t \geq t_{1}$, the arbitrage "value" of a bet on a binary outcome needs to match the expectation, hence, again, we map to the Brier score - by an arbitrage argument. Although there is no quadratic loss function involved, the fact that the bet is a function of a martingale, which is required to be itself a martingale, i.e. that the conditional expectation remains invariant to time, does not allow an arbitrage to take place. A "high" price can be "shorted" by the arbitrageur, a "low" price can be "bought", and so on repeatedly. The consistency between bets at period $t$ and other periods $t+\Delta t$ enforces the probabilistic discipline. In other words, someone can "buy" from the forecaster then "sell" back to him, generating a positive expected "return" if the forecaster is out of line with martingale valuation.

As to the current practice by forecasters, although some election forecasters appear to be aware of the need to minimize their Brier Score, the idea that the revisions of estimates should also be subjected to martingale valuation is not well established.

## V. Conclusion and Comments

As can be seen in Figure 1 , a binary option reveals more about uncertainty than about the true estimation, a result well known to traders, see [5].

In the presence of more than 2 candidates, the process can be generalized with the following heuristic approximation. Establish the stochastic process for $Y_{1, t}$, and just as $Y_{1, t}$ is a process in $[0,1], Y_{2, t}$ is a process $\in\left(Y_{1, t}, 1\right]$, with $Y_{3, t}$ the residual $1-Y_{2, t}-Y_{1, t}$, and more generally $Y_{n-1, t} \in\left(Y_{n_{2}, t}, 1\right]$ and $Y_{n, t}$ is the residual $Y_{n}=1-\sum_{i=1}^{n-1} Y_{i, t}$. For $n$ candidates, the $\mathrm{n}^{\text {th }}$ is the residual.

## VI. Acknowledgements

The author thanks Dhruv Madeka and Raphael Douady for detailed and extensive discussions of the paper as well as thorough auditing of the proofs across the various iterations, and, worse, the numerous changes of notation. Peter Carr helped with discussions on the properties of a bounded martingale and the transformations. I thank David Shimko,Andrew Lesniewski, and Andrew Papanicolaou for comments. I thank Arthur Breitman for guidance with the literature for numerical approximations of the various logistic-normal integrals. I thank participants of the Tandon School of Engineering and Bloomberg Quantitative Finance Seminars. I also thank Bruno Dupire,MikeLawler, theEditors-In-Chief, and various friendly
people on social media. DhruvMadeka fromBloomberg, while working on a similar problem, independently came up with the same relationships between the volatility of an estimate and its bounds and the same arbitrage bounds. All errors are mine.

Dhruv Madeka from Bloomberg, while working on a similar problem, independently came up with the same relationships between the volatility of an estimate and its bounds and the same arbitrage bounds. All errors are mine.

## References

[1] D. Pirjol, "The logistic-normal integral and its generalizations," Journal of Computational and Applied Mathematics, vol. 237, no. 1, pp. 460-469, 2013.
[2] P. Carr, Private conversation on bounded Brownian motion, NYU Tandon School of Engineering, 2017.
[3] B. De Finetti, Philosophical Lectures on Probability: collected, edited, and annotated by Alberto Mura. Springer Science \& Business Media, 2008, vol. 340.
[4] D. A. Freedman, Notes on the Dutch Book Argument, Lecture Notes, Department of Statistics, University of Berkley at Berkley, https://www.stat.berkeley.edu/ census/sample.pdf, 2003.
[5] N. N. Taleb, Dynamic Hedging: Managing Vanilla and Exotic Options. John Wiley \& Sons (Wiley Series in Financial Engineering), 1997.


[^0]:    ${ }^{1}$ A central property of our model is that it prevents $B($.$) from varying more$ than the estimated $Y$ : in a two candidate contest, it will be capped (floored) at $Y$ if lower (higher) than .5 . In practice, we can observe probabilities of winning of $98 \%$ vs. $02 \%$ from a narrower spread of estimated votes of $47 \%$ vs. $53 \%$; our approach prevents, under high uncertainty, the probabilities from diverging away from the estimated votes. But it remains conservative enough to not give a higher proportion.

