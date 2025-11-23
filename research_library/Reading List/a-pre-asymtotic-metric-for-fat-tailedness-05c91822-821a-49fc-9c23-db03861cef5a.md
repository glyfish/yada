# How Much Data Do You Need? A Pre-asymptotic Metric for Fat-tailedness 

Nassim Nicholas Taleb<br>Tandon School of Engineering, New York University<br>November 2018<br>Forthcoming, International Journal of Forecasting

## Abstract-

This paper presents an operational metric for univariate unimodal probability distributions with finite first moment, in [ 0,1 ] where $\mathbf{0}$ is maximally thin-tailed (Gaussian) and 1 is maximally fat-tailed. It is based on "how much data one needs to make meaningful statements about a given dataset?"

Applications: Among others, it

- helps assess the sample size $n$ needed for statistical significance outside the Gaussian,
- helps measure the speed of convergence to the Gaussian (or stable basin),
- allows practical comparisons across classes of fattailed distributions,
- allows the assessment of the number of securities needed in portfolio construction to achieve a certain level of risk-reduction from diversification,
- helps assess risks under various settings,
- helps understand some inconsistent attributes of the lognormal, pending on the parametrization of its variance.
The literature is rich for what concerns asymptotic behavior, but there is a large void for finite values of $n$, those needed for operational purposes.

Background: Conventional measures of fat-tailedness, namely 1) the tail index for the power law class, and 2) Kurtosis for finite moment distributions fail to apply to some distributions, and do not allow comparisons across classes and parametrization, that is between power laws outside the Levy-Stable basin, or power laws to distributions in other classes, or power laws for different number of summands. How can one compare a sum of 100 Student T distributed random variables with 3 degrees of freedom to one in a Levy-Stable or a Lognormal class? How can one compare a sum of 100 Student $T$ with 3 degrees of freedom to a single Student $\mathbf{T}$ with $\mathbf{2}$ degrees of freedom?

We propose an operational and heuristic metric that allows us to compare $n$-summed independent variables under all distributions with finite first moment. The method

[^0]is based on the rate of convergence of the law of large numbers for finite sums, $n$-summands specifically.

We get either explicit expressions or simulation results and bounds for the lognormal, exponential, Pareto, and the Student $\mathbf{T}$ distributions in their various calibrations -in addition to the general Pearson classes.

E| $S_{n}=X_{1}+X_{2}+\ldots+X_{n} \mid$

![](https://cdn.mathpix.com/cropped/2025_11_22_c78621e5e373be4e5dc8g-01.jpg?height=475&width=800&top_left_y=1089&top_left_x=1160)
Fig. 1. The intuition of what $\kappa$ is measuring: how the mean deviation of the sum of identical copies of a r.v. $S_{n}=X_{1}+X_{2}+\ldots X_{n}$ grows as the sample increases and how we can compare preasymptotically distributions from different classes.

## I. Introduction and Definitions

How can one compare a Pareto distribution with tail $\alpha=2.1$ that is, with finite variance, to a Gaussian? Asymptotically, these distributions in the regular variation class with finite second moment, under summation, become Gaussian, but preasymptotically, we have no standard way of comparing them given that metrics that depend on higher moments, such as kurtosis, cannot be of help. Nor can we easily compare an infinite variance Pareto distribution to its limiting $\alpha$-Stable distribution (when both have the same tail index or tail exponent). Likewise, how can one compare the "fat-tailedness" of, say a Student T with 3 degrees of freedom to that of a LevyStable with tail exponent of 1.95? Both distributions have a finite mean; of the two, only the first has a finite variance but, for a small number of summands, behaves more "fat-tailed" according to some operational criteria ${ }^{1}$

[^1]![](https://cdn.mathpix.com/cropped/2025_11_22_c78621e5e373be4e5dc8g-02.jpg?height=1218&width=890&top_left_y=187&top_left_x=159)
Fig. 2. Watching the effect of the Generalized Central Limit Theorem: Pareto and Student T Distribution, in the $\mathfrak{P}$ class, with $\alpha$ exponent, $\kappa$ converge to $2-\left(\mathbb{1}_{\alpha<2} \alpha+\mathbb{1}_{\alpha \geq 2} 2\right)$, or the Stable $\mathfrak{S}$ class. We observe how slow the convergence, even after 1000 summands. This discounts Mandelbrot's assertion that an infinite variance Pareto can be subsumed into a stable distribution.

1) Criterion for "fat-tailedness": There are various ways to "define" Fat Tails and rank distributions according to each definition. In the narrow class of distributions having all moments finite, it is the kurtosis, which allows simple comparisons and measure departures from the Gaussian, which is used as a norm. For the power law class, it can be the tail exponent. One can also use extremal values, taking the probability of exceeding a maximum value, adjusted by the scale (as practiced in extreme value theory). For operational uses, practitioners' fat-tailedness is a degree of concentration, such as "how much of the statistical properties will be attributable to a single observation?", or, appropriately adjusted by the scale (or the mean dispersion), "how much is the total wealth of a country in the hands of the richest individual?"

Here we use the following criterion for our purpose, which maps to the measure of concentration in the past paragraph: "How much will additional data (under such a probability distribution) help increase the stability of the observed mean". The purpose is not entirely statistical: it can equally mean: "How much will adding an additional security into my portfolio allocation (i.e., keeping the total constant) increase its
stability?"
Our metric differs from the asymptotic measures (particularly ones used in extreme value theory) in the fact that it is fundamentally preasymptotic.

Real life, and real world realizations, are outside the asymptote.
2) What does the metric do: The metric we propose, $\kappa$ does the following:

- Allows comparison of $n$-summed variables of different distributions for a given number of summands, or same distribution for different $n$, and assess the preasymptotic properties of a given distributions.
- Provides a measure of the distance from the limiting distribution, namely the Lévy $\alpha$-Stable basin (of which the Gaussian is a special case).
- For statistical inference, allows assessing the "speed" of the law of large numbers, expressed in change of the mean absolute error around the average thanks to the increase of sample size $n$.
- Allows comparative assessment of the "fat-tailedness" of two different univariate distributions, when both have finite first moment.
- Allows us to know ahead of time how many runs we need for a Monte Carlo simulation.

3) The state of statistical inference: The last point, the "speed", appears to have been ignored. For in the 9,400 pages of the Encyclopedia of Statistical Science [1], we were unable to find a single comment as to how long it takes to reach the asymptote, or how to deal with $n$ summands that are large but perhaps not sufficiently so for the socalled "normal approximation". Further, the entry on statistical inference (authored by W. Hoeffding) explicitly brushes away the problem, stating:
"The exact distribution of a statistic is usually highly complicated and difficult to work with. Hence the need to approximate the exact distribution by a distribution of a simpler form whose properties are more transparent. The limit theorems of probability theory provide an important tool for such approximations. In particular, the classical central limit theorems state that the sum of a large number of independent random variables is approximately normally distributed under general conditions. In fact, the normal distribution plays a dominating role among the possible limit distributions.
(...) Moreover, many statistics behave asymptotically like sums of independent random variables. All of this helps to explain the importance of the normal distribution as an asymptotic distribution."
Even social science discussions of the "law of small numbers" [2] assume Gaussian attributes as the norm. As to extreme value theory, the "functional law of small numbers" [3] concerns Poisson hitting with small probabilities; more generally, extreme value theory (while naturally equipped with the tools for fat tails) is concerned with the behavior of maxima, not averages.

Our motto here and elsewere is "statistics is never standard". This metric aims at showing how standard is standard, and
measure the exact departure from the standard from the standpoint of statistical significance.

## II. The Metric

![](https://cdn.mathpix.com/cropped/2025_11_22_c78621e5e373be4e5dc8g-03.jpg?height=589&width=890&top_left_y=425&top_left_x=159)
Fig. 3. The lognormal distribution behaves like a Gaussian for low values of $\sigma$, but becomes rapidly equivalent to a power law. This illustrates why, operationally, the debate on whether the distribution of wealth was lognormal (Gibrat) or Pareto (Zipf) doesn't carry much operational significance.

Definition 1 (the $\kappa$ metric). Let $X_{1}, \ldots, X_{n}$ be i.i.d. random variables with finite mean, that is $\mathbb{E}(X)<+\infty$. Let $S_{n}= X_{1}+X_{2}+\ldots+X_{n}$ be a partial sum. Let $\mathbb{M}(n)=\mathbb{E}\left(\mid S_{n}-\right. \left.\mathbb{E}\left(S_{n}\right) \mid\right)$ be the expected mean absolute deviation from the mean for $n$ summands. Define the "rate" of convergence for $n$ additional summands starting with $n_{0}$ :

## III. Stable Basin of Convergence as Benchmark

Definition 2 (the class $\mathfrak{P}$ ). The $\mathfrak{P}$ class of power laws (regular variation) is defined for r.v. $X$ as follows:

$$
\begin{equation*}
\mathfrak{P}=\left\{X: \mathbb{P}(X>x) \sim L(x) x^{-\alpha}\right\} \tag{3}
\end{equation*}
$$

where $\sim$ means that the limit of the ratio or rhs to lhs goes to $l$ as $x \rightarrow \infty . L:\left[x_{\min },+\infty\right) \rightarrow(0,+\infty)$ is a slowly varying function, defined as $\lim _{x \rightarrow+\infty} \frac{L(k x)}{L(x)}=1$ for any $k>0$. The constant $\alpha>0$.

Next we define the domain of attraction of the sum of identically distributed variables, in our case with identical parameters.
Definition 3. (stable $\mathfrak{S}$ class) A random variable $X$ follows a stable (or $\alpha$-stable) distribution, symbolically $X \sim S(\tilde{\alpha}, \beta, \mu, \sigma)$, if its characteristic function $\chi(t)=\mathbb{E}\left(e^{i t X}\right)$ is of the form:

$$
\chi(t)=\left\{\begin{array}{ll}
e^{\left(i \mu t-|t \sigma|^{\tilde{\alpha}}\left(1-i \beta \tan \left(\frac{\pi \tilde{\alpha}}{2}\right) \operatorname{sgn}(t)\right)\right)} & \tilde{\alpha} \neq 1  \tag{4}\\
e^{i t\left(\frac{2 \beta \sigma \log (\sigma)}{\pi}+\mu\right)-|t \sigma|\left(1+\frac{2 i \beta \operatorname{sgn}(t) \log (|t \sigma|)}{\pi}\right)} & \tilde{\alpha}=1
\end{array},\right.
$$

Next, we define the corresponding stable $\tilde{\alpha}$ :

$$
\tilde{\alpha} \triangleq \begin{cases}\alpha \mathbb{1}_{\alpha<2}+2 \mathbb{1}_{\alpha \geq 2} & \text { if } \mathrm{X} \text { is in } \mathfrak{P}  \tag{5}\\ 2 & \text { otherwise. }\end{cases}
$$

Further discussions of the class $\mathfrak{S}$ are as follows.

## A. Equivalence for stable distributions

For all $n_{0}$ and $n \geq 1$ in the Stable $\mathfrak{S}$ class with $\tilde{\alpha} \geq 1$ :

$$
\kappa_{\left(n_{0}, n\right)}=2-\tilde{\alpha},
$$

$\kappa_{n_{0}, n}=\min \left\{\kappa_{n_{0}, n}: \frac{\mathbb{M}(n)}{\mathbb{M}\left(n_{0}\right)}=\left(\frac{n}{n_{0}}\right)^{\frac{1}{2-\kappa_{n}, n}}, n_{0}=1,2, \ldots\right\}$, 'simply from the property that

$$
\begin{equation*}
\mathbb{M}(n)=n^{\frac{1}{\alpha}} \mathbb{M}(1) \tag{6}
\end{equation*}
$$

Further, for the baseline values $n=n_{0}+1$, we use the shorthand $\kappa_{n_{0}}$.

We can also decompose $\kappa\left(n_{0}, n\right)$ in term of "local" intermediate ones similar to "local" interest rates, under the constraint.

$$
\begin{equation*}
\kappa\left(n_{0}, n\right)=2-\frac{\log (n)-\log \left(n_{0}\right)}{\sum_{i=0}^{n} \frac{\log (i+1)-\log (i)}{2-\kappa(i, i+1)}} . \tag{2}
\end{equation*}
$$

Use of Mean Deviation: Note that we use for measure of dispersion around the mean the mean absolute deviation, to stay in norm $L^{1}$ in the absence of finite variance -actually, even in the presence of finite variance, under power law regimes, distributions deliver an unstable and uninformative second moment. Mean deviation proves far more robust there. (Mean absolute deviation can be shown to be more "efficient" except in the narrow case of kurtosis equals 3 (the Gaussian), see a longer discussion in [4]; for other advantages, see [5].)

This, simply shows that $\kappa_{n_{0}, n}=0$ for the Gaussian.
The problem of the preasymptotics for $n$ summands reduces to:

- What is the property of the distribution for $n_{0}=1$ (or starting from a standard, off-the shelf distribution)?
- What is the property of the distribution for $n_{0}$ summands?
- How does $\kappa_{n} \rightarrow 2-\tilde{\alpha}$ and at what rate?


## B. Practical significance for sample sufficiency

Confidence intervals: As a simple heuristic, the higher $\kappa$, the more disproportionally insufficient the confidence interval. Any value of $\kappa$ above . 15 effectively indicates a high degree of unreliability of the "normal approximation". One can immediately doubt the results of numerous research papers in fat-tailed domains.

Computations of the sort done Table II for instance allows us to compare various distributions under various parametriazation. (comparing various Pareto distributions to symmetric

TABLE I
Kappa for 2 summands, $\kappa_{1}$.
| Distribution | $\kappa_{1}$ |
| :--- | :--- |
| Student T ( $\alpha$ ) | $2-\frac{2 \log (2)}{2 \log \left(\frac{2^{2-\alpha} \Gamma\left(\alpha-\frac{1}{2}\right)}{\Gamma\left(\frac{\alpha}{2}\right)^{2}}\right)+\log (\pi)}$ |
| Exponential/Gamma | $2-\frac{\log (2)}{2 \log (2)-1} \approx .21$ |
| Pareto ( $\alpha$ ) | $2-\frac{\log (2)}{\log \left((\alpha-1)^{2-\alpha} \alpha^{\alpha-1} \int_{0}^{\frac{2}{\alpha-1}}-2 \alpha^{2}(y+2)^{-2 \alpha-1}\left(\frac{2}{\alpha-1}-y\right)\left(B_{\frac{1}{y+2}}(-\alpha, 1-\alpha)-B_{\frac{y+1}{y+2}}(-\alpha, 1-\alpha)\right) d y\right)}$ a |
| Normal $(\mu, \sigma)$ with switching variance $\sigma^{2} a$ w.p $\gamma^{b}$ | $2-\frac{\log (2)}{\log \left(\frac{\sqrt{2}\left(\sqrt{\frac{a p}{p-1}+\sigma^{2}}+p\left(-2 \sqrt{\frac{a p}{p-1}+\sigma^{2}}+p\left(\sqrt{\frac{a p}{p-1}+\sigma^{2}}-\sqrt{2 a\left(\frac{1}{p-1}+2\right)+4 \sigma^{2}}+\sqrt{a+\sigma^{2}}\right)+\sqrt{2 a\left(\frac{1}{p-1}+2\right)+4 \sigma^{2}}\right)\right)}{p \sqrt{a+\sigma^{2}}-(p-1) \sqrt{\frac{a p}{p-1}+\sigma^{2}}}\right)}$ |
| Lognormal ( $\mu, \sigma$ ) | $\approx 2-\frac{\log (2)}{\log \left(\frac{2 \operatorname{erf}\left(\frac{\sqrt{\log \left(\frac{1}{2}\left(e^{\sigma^{2}+1}\right)\right)}}{2 \sqrt{2}}\right)}{\operatorname{erf}\left(\frac{\sigma}{2 \sqrt{2}}\right)}\right)}$. |
| ${ }^{a} B .(.,$.$) is the incomplete Beta function: B_{z}(a, b)=\int_{0}^{z} t^{a-1}(1-t)^{b-1} d t ; \operatorname{erf}($.$) is the error function \operatorname{erf}(z)=\frac{2}{\sqrt{\pi}} \int_{0}^{z} e^{-t^{2}} d t$. <br> ${ }^{b}$ See comments and derivations in the appendix for switching both variance and mean as it can produce negative values for kappa. |  |
|  |  |


TABLE II
Main results
| Distribution | $\kappa_{n}$ |
| :--- | :--- |
| Exponential/Gamma | Explicit |
| Lognormal ( $\mu, \sigma$ ) | No explicit $\kappa_{n}$ but explicit lower and higher bounds (low or high $\sigma$ or $n$ ). Approximated with Pearson IV for $\sigma$ in between. |
| Pareto ( $\alpha$ ) (Constant) | Explicit for $\kappa_{2}$ (lower bound for all $\alpha)$. |
| Student $\mathrm{T}(\alpha)$ (slowly varying function) | Explicit for $\kappa_{1}, \alpha=3$. |


Student T and, of course the Gaussian which has a flat kappa of 0 )

As we mentioned in the introduction, required sample size for statistical inference is driven by $n$, the number of summands. Yet the law of large numbers is often invoked in erroneous conditions; we need a rigorous sample size metric.

Many papers, when discussing financial matters, say [6] use finite variance as a binary classification for fat tailedness: power laws with a tail exponent greater than 2 are therefore classified as part of the "Gaussian basin", hence allowing the use of variance and other such metrics for financial applications. A much more natural boundary is finiteness of expectation for financial applications [7]. Our metric can thus be useful as follows:

TABLE III
Comparing Pareto to Student T (Same tail exponent $\alpha$ )
|  | Pareto | Pareto | Pareto | Student | Student | Student |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $\kappa_{1}$ | $\kappa_{1,30}$ | $\kappa_{1,100}$ | $\kappa_{1}$ | $\kappa_{1,30}$ | $\kappa_{1,100}$ |
| 1.25 | 0.829 | 0.787 | 0.771 | 0.792 | 0.765 | 0.756 |
| 1.5 | 0.724 | 0.65 | 0.631 | 0.647 | 0.609 | 0.587 |
| 1.75 | 0.65 | 0.556 | 0.53 | 0.543 | 0.483 | 0.451 |
| 2. | 0.594 | 0.484 | 0.449 | 0.465 | 0.387 | 0.352 |
| 2.25 | 0.551 | 0.431 | 0.388 | 0.406 | 0.316 | 0.282 |
| 2.5 | 0.517 | 0.386 | 0.341 | 0.359 | 0.256 | 0.227 |
| 2.75 | 0.488 | 0.356 | 0.307 | 0.321 | 0.224 | 0.189 |
| 3. | 0.465 | 0.3246 | 0.281 | 0.29 | 0.191 | 0.159 |
| 3.25 | 0.445 | 0.305 | 0.258 | 0.265 | 0.167 | 0.138 |
| 3.5 | 0.428 | 0.284 | 0.235 | 0.243 | 0.149 | 0.121 |
| 3.75 | 0.413 | 0.263 | 0.222 | 0.225 | 0.13 | 0.10 |
| 4. | 0.4 | 0.2532 | 0.211 | 0.209 | 0.126 | 0.093 |


Let $X_{g, 1}, X_{g, 2}, \ldots, X_{g, n_{g}}$ be a sequence of Gaussian variables with mean $\mu$ and scale $\sigma$. Let $X_{\nu, 1}, X_{n u, 2}, \ldots, X_{n u, n_{\nu}}$ be a sequence of some other variables scaled to be of the same $\mathbb{M}(1)$, namely $\mathbb{M}^{\nu}(1)=\mathbb{M}^{g}(1)=\sqrt{\frac{2}{\pi}} \sigma$. We would be looking for values of $n_{\nu}$ corresponding to a given $n_{g}$.
$\kappa_{n}$ is indicative of both the rate of convergence under the law of large number, and for $\kappa_{n} \rightarrow 0$, for rate of convergence of summands to the Gaussian under the central limit, as illustrated in Figure 2.

$$
\begin{aligned}
n_{\min }=\inf \left\{n_{\nu}: \mathbb{E}\right. & \left(\left|\sum_{i=1}^{n_{\nu}} \frac{X_{\nu, i}-m_{p}}{n_{\nu}}\right|\right) \\
& \left.\leq \mathbb{E}\left(\left|\sum_{i=1}^{n_{g}} \frac{X_{g, i}-m_{g}}{n_{g}}\right|\right), n_{\nu}>0\right\}
\end{aligned}
$$

which can be computed using $\kappa_{n}=0$ for the Gaussian and backing our from $\kappa_{n}$ for the target distribution with the simple approximation:

$$
\begin{equation*}
n_{\nu}=n_{g}^{-\frac{1}{\kappa_{1, n_{g}}-1}} \approx n_{g}^{-\frac{1}{\kappa_{1}-1}}, n_{g}>1 \tag{7}
\end{equation*}
$$

The approximation is owed to the slowness of convergence. So for example, a Student T with 3 degrees of freedom ( $\alpha=3$ ) requires 120 observations to get the same drop in variance from averaging (hence confidence level) as the Gaussian with 30, that is 4 times as much. The one-tailed Pareto with the same tail exponent $\alpha=3$ requires 543 observations to match a Gaussian sample of 30, 4.5 times more than the Student, which shows 1) finiteness of variance is not an indication of fat tailedness (in our statistical sense), 2) neither are tail exponents good indicators 3) how the symmetric Student and the Pareto distribution are not equivalent because of the "bell-shapedness" of the Student (from the slowly moving function) that dampens variations in the center of the distribution.

We can also elicit quite counterintuitive results. From Eq. 7, the "Pareto 80/20" in the popular mind, which maps to a tail exponent around $\alpha \approx 1.14$, requires $>10^{9}$ more observations than the Gaussian.

## IV. Technical Consequences

## A. Some oddities with asymmetric distributions

The stable distribution, when skewed, has the same $\kappa$ index as a symmetric one (in other words, $\kappa$ is invariant to the $\beta$ parameter in Eq. 4, which conserves under summation). But a one-tailed simple Pareto distribution is fatter tailed (for our purpose here) than an equivalent symmetric one.

This is relevant because the stable is never really observed in practice and used as some limiting mathematical object, while the Pareto is more commonly seen. The point is not well grasped in the literature. Consider the following use of the substitution of a stable for a Pareto. In Uchaikin and Zolotarev [8]:

Mandelbrot called attention to the fact that the use of the extremal stable distributions (corresponding to $\beta=1$ ) to describe empirical principles was preferable to the use of the Zipf-Pareto distributions for a number of reasons. It can be seen from many publications, both theoretical and applied, that Mandelbrot's ideas receive more and more wide recognition of experts. In this way, the hope arises to confirm empirically established principles in the framework of mathematical models and, at the same time, to clear up the mechanism of the formation of these principles.
These are not the same animals, even for large number of summands.

## B. Rate of convergence of a student $T$ distribution to the Gaussian Basin

We show in the appendix -thanks to the explicit derivation of $\kappa$ for the sum of students with $\alpha=3$, the "cubic" commonly noticed in finance -that the rate of convergence of $\kappa$ to 0 under summation is slow. The semi-closed form for the density of an n -summed cubic Student allows to complement the result in Bouchaud and Potters [9] (see also [10], which is as follows. Their approach is to separate the "Gaussian zone" where the density is approximated by that of a Gaussian, and a "power law zone" in the tails which retains the original distribution with power law decline. The "crossover" between the two moves right and left of the center at a rate of $\sqrt{n \log (n)}$ standard deviations) which is excruciatingly slow. Indeed, one can note that more summands fall at the center of the distribution, and fewer outside of it, hence the speed of convergence according to the central limit theorem will differ according to whether the density concerns the center or the tails.

Further investigations would concern the convergence of the Pareto to a Levy-Stable, which so far we only got numerically.

## C. The lognormal is neither thin nor fat tailed

Naively, as we can see in Figure II. at low values of the parameter $\sigma$, the lognormal behaves like a Gaussian, and, at high $\sigma$, it appears to have the behavior of a Cauchy of sorts (a one-tailed Cauchy, rather a stable distribution with $\alpha=1$, $\beta=1$ ), as $\kappa$ gets closer and closer to 1 . This gives us an idea about some aspects of the debates as to whether some variable is Pareto or lognormally distributed, such as, say, the debates about wealth [11], [12], [13]. Indeed, such debates can be irrelevant to the real world. As P. Cirillo [14] observed, many cases of Paretianity are effectively lognormal situations with high variance; the practical statistical consequences, however, are smaller than imagined.

## D. Can kappa be negative?

Just as kurtosis for a mixed Gaussian (i.e., with stochastic mean, rather than stochastic volatility) can dip below 3 (or become "negative" when one uses the convention of measuring Kurtosis as excess over the Gaussian by adding 3 to the measure), the kappa metric can become negative when kurtosis is "negative". These situations require bimodality (i.e., a switching process between means under fixed variance, with modes far apart in terms of standard deviation). They do not appear to occur with unimodal distributions.

Details and derivations are presented in the appendix.

## V. Conclusion and Consequences

To summarize, while the limit theorems (the law of large numbers and the central limit) are concerned with the behavior as $n \rightarrow+\infty$, we are interested in finite and exact $n$ both small and large (and its statistical and risk implications).

We may draw a few operational consequences:

![](https://cdn.mathpix.com/cropped/2025_11_22_c78621e5e373be4e5dc8g-06.jpg?height=584&width=882&top_left_y=189&top_left_x=162)
Fig. 4. In short, why the $1 / n$ heuristic works in portfolio theory (and similar decision problems): it takes many, many more securities to get the same risk reduction as via portfolio allocation according to Markowitz. We assume to simplify that the securities are independent, which they are not, something that compounds the effect.

## A. Portfolio pseudo-stabilization

Our method can also naturally and immediately apply to portfolio construction and the effect of diversification since adding a security to a portfolio has the same "stabilizing" effect as adding an additional observation for the purpose of statistical significance. "How much data do you need?" translates into "How many securities do you need?". Clearly, the Markowicz allocation method in modern finance [15] (which seems to not be used by Markowitz himself for his own portfolio [16]) applies only for $\kappa$ near 0 ; people use convex heuristics, otherwise they will underestimate tail risks and "blow up" the way the famed portfolio-theory oriented hedge fund Long Term Management did in 1998 [17] [18].)

We mentioned earlier that a Pareto distribution close to the "80/20" requires up to $10^{9}$ more observations than a Gaussian; consider that the risk of a portfolio under such a distribution would be underestimated by at least 8 orders of magnitudes if one uses modern portfolio criteria. Following such a reasoning, one simply needs broader portfolios.

It has also been noted that there is practically no financial security that is not fatter tailed than the Gaussian, from the simple criterion of kurtosis [19], meaning Markowitz portfolio allocation is never the best solution. It happens that agents wisely apply a noisy approximation to the $\frac{1}{n}$ heuristic which has been classified as one of those biases by behavioral scientists but has in fact been debunked as false (a false bias is one in which, while the observed phenomenon is there, it does not constitute a "bias" in the bad sense of the word; rather it is the researcher who is mistaken owing to using the wrong tools instead of the decision-maker). This tendency to "overdiversify" has been deemed a departure from optimal investment behavior by Benartzi and Thaler [20], explained in [21] "when faced with $n$ options, divide assets evenly across the options. We have dubbed this heuristic the " $1 / n$ rule."" However, broadening one's diversification is effectively as least as optimal as standard allocation(see critique by Windcliff and Boyle [22] and [23]). In short, an equally
weighted portfolio outperforms the SP500 across a broad range range of metrics. But even the latter two papers didn't conceive of the full effect and properties of fat tails, which we can see here with some precision. Fig. V shows the effect for securities compared to Markowitz.

This false bias is one in many examples of policy makers "nudging" people into the wrong rationality [17] and driving them to increase their portfolio risk many folds.

A few more comments on financial portfolio risks. The SP500 has a $\kappa$ of around .2, but one needs to take into account that it is itself a basket of $n=500$ securities, albeit unweighted and consisting of correlated members, overweighing stable stocks. Single stocks have kappas between .3 and .7 , meaning a policy of "overdiversification" is a must.

Likewise the metric gives us some guidance in the treatment of data for forecasting, by establishing sample sufficiency, to state such matters as how many years of data do we need before stating whether climate conditions "have changed", see [24].

## B. Other aspects of statistical inference

So far we considered only univariate distributions. For higher dimensions, a potential area of investigation is an equivalent approach to the multivariate distribution of fat tailed variables, the sampling of which is not captured by the Marchenko-Pastur (or Wishhart) distributions. As in our situation, adding variables doesn't easily remove noise from random matrices.

## C. Final comment

As we said earlier, "statistics is never standard"; however there are heuristics methods to figure out where and by how much we depart from the standard.

## Appendix

## A. Cubic Student T (Gaussian Basin)

The Student T with 3 degrees of freedom is of special interest in the literature owing to its prevalence in finance [6]. It is often mistakenly approximated to be Gaussian owing to the finiteness of its variance. Asymptotically, we end up with a Gaussian, but this doesn't tell us anything about the rate of convergence. Mandelbrot and Taleb 25 remarks that the cubic acts more like a powerlaw in the distribution of the extremes, which we will elaborate here thanks to an explicit PDF for the sum.

Let $X$ be a random variable distributed with density $p(x)$ :

$$
\begin{equation*}
p(x)=\frac{6 \sqrt{3}}{\pi\left(x^{2}+3\right)^{2}}, x \in(-\infty, \infty) \tag{8}
\end{equation*}
$$

Proposition 1. Let $Y$ be a sum of $X_{1}, \ldots, X_{n}, n$ identical copies of $X$. Let $\mathbb{M}(n)$ be the mean absolute deviation from the mean for $n$ summands. The "rate" of convergence $\kappa_{1, n}=\left\{\kappa: \frac{\mathbb{M}(n)}{\mathbb{M}(1)}=n^{\frac{1}{2-\kappa}}\right\}$ is:

$$
\begin{equation*}
\kappa_{1, n}=2-\frac{\log (n)}{\log \left(e^{n} n^{-n} \Gamma(n+1, n)-1\right)} \tag{9}
\end{equation*}
$$

where $\Gamma(.,$.$) is the incomplete gamma function \Gamma(a, z)=\int_{z}^{\infty} d t t^{a-1} e^{-t}$.
Since the mean deviation $\mathbb{M}(n)$ :

$$
\mathbb{M}(n)= \begin{cases}\frac{2 \sqrt{3}}{\pi} & \text { for } n=1  \tag{10}\\ \frac{2 \sqrt{3}}{\pi}\left(e^{n} n^{-n} \Gamma(n+1, n)-1\right) & \text { for } n>1\end{cases}
$$

The derivations are as follows. For the pdf and the MAD we followed different routes.
We have the characteristic function for $n$ summands:

$$
\varphi(\omega)=(1+\sqrt{3}|\omega|)^{n} e^{-n \sqrt{3}|\omega|}
$$

The pdf of $Y$ is given by:

$$
p(y)=\frac{1}{\pi} \int_{0}^{\infty}(1+\sqrt{3} \omega)^{n} e^{-n \sqrt{3} \omega} \cos (\omega y) d \omega
$$

After arduous integration we get the result in 10 . Further, since the following result does not appear to be found in the literature, we have a side useful result: the PDF of $Y$ can be written as

$$
\begin{equation*}
p(y)=\frac{e^{n-\frac{i y}{\sqrt{3}}}\left(e^{\frac{2 i y}{\sqrt{3}}} E_{-n}\left(n+\frac{i y}{\sqrt{3}}\right)+E_{-n}\left(n-\frac{i y}{\sqrt{3}}\right)\right)}{2 \sqrt{3} \pi} \tag{11}
\end{equation*}
$$

where $E_{(.)}($.$) is the exponential integral E_{n} z=\int_{1}^{\infty} \frac{e^{t(-z)}}{t^{n}} d t$.
Note the following identities (from the updating of Abramowitz and Stegun) [26]

$$
n^{-n-1} \Gamma(n+1, n)=E_{-n}(n)=e^{-n} \frac{(n-1)!}{n^{n}} \sum_{m=0}^{n} \frac{n^{m}}{m!}
$$

As to the asymptotics, we have the following result (proposed by Michail Loulakis): Reexpressing Eq. 10.

$$
\mathbb{M}(n)=\frac{2 \sqrt{3} n!}{\pi n^{n}} \sum_{m=0}^{n-1} \frac{n^{m}}{m!}
$$

Further,

$$
e^{-n} \sum_{m=0}^{n-1} \frac{n^{m}}{m!}=\frac{1}{2}+O\left(\frac{1}{\sqrt{n}}\right)
$$

(From the behavior of the sum of Poisson variables as they converge to a Gaussian by the central limit theorem: $e^{-n} \sum_{m=0}^{n-1} \frac{n^{m}}{m!}=\mathbb{P}\left(X_{n}<n\right)$ where $X_{n}$ is a Poisson random variable with parameter $n$. Since the sum of $n$ independent Poisson random variables with parameter 1 is Poisson with parameter $n$, the Central Limit Theorem says the probability distribution of $Z_{n}=\left(X_{n}-n\right) / \sqrt{n}$ approaches a standard normal distribution. Thus $\mathbb{P}\left(X_{n}<n\right)=\mathbb{P}\left(Z_{n}<0\right) \rightarrow 1 / 2$ as $n \rightarrow \infty$. ${ }^{2}$ For another approach, see [27] for proof that $1+\frac{n}{1!}+\frac{n^{2}}{2!}+\cdots+\frac{n^{n-1}}{(n-1)!} \sim \frac{e^{n}}{2}$.)

Using the property that $\lim _{n \rightarrow \infty} \frac{n!\exp (n)}{n^{n} \sqrt{n}}=\sqrt{2 \pi}$, we get the following exact asymptotics:

[^2]$$
\lim _{n \rightarrow \infty} \log (n) \kappa_{1, n}=\frac{\pi^{2}}{4}
$$
thus $\kappa$ goes to 0 (i.e, the average becomes Gaussian) at speed $\frac{1}{\log (n)}$, which is excruciatingly slow. In other words, even with $10^{6}$ summands, the behavior cannot be summarized as that of a Gaussian, an intuition often expressed by B. Mandelbrot [25].

## B. Lognormal Sums

From the behavior of its cumulants for $n$ summands, we can observe that a sum behaves likes a Gaussian when $\sigma$ is low, and as a lognormal when $\sigma$ is high - and in both cases we know explicitly $\kappa_{n}$.

The lognormal (parametrized with $\mu$ and $\sigma$ ) doesn't have an explicit characteristic function. But we can get cumulants $K_{i}$ of all orders $i$ by recursion and for our case of summed identical copies of r.v. $X_{i}, K_{i}^{n}=K_{i}\left(\sum_{n} X_{i}\right)=n K_{i}\left(X_{1}\right)$.

Cumulants:

$$
\begin{aligned}
& K_{1}^{n}=n e^{\mu+\frac{\sigma^{2}}{2}} \\
& K_{2}^{n}=n\left(e^{\sigma^{2}}-1\right) e^{2 \mu+\sigma^{2}} \\
& K_{3}^{n}=n\left(e^{\sigma^{2}}-1\right)^{2}\left(e^{\sigma^{2}}+2\right) e^{3 \mu+\frac{3 \sigma^{2}}{2}} \\
& K_{4}^{n}=\ldots
\end{aligned}
$$

Which allow us to compute: Skewness $=\frac{\sqrt{e^{\sigma^{2}}-1}\left(e^{\sigma^{2}}+2\right) e^{\frac{1}{2}\left(2 \mu+\sigma^{2}\right)-\mu-\frac{\sigma^{2}}{2}}}{\sqrt{n}}$ and Kurtosis $=3+\frac{e^{2 \sigma^{2}}\left(e^{\sigma^{2}}\left(e^{\sigma^{2}}+2\right)+3\right)-6}{n}$ We can immediately prove from the cumulants/moments that:

$$
\lim _{n \rightarrow+\infty} \kappa_{1, n}=0, \lim _{\sigma \rightarrow 0} \kappa_{1, n}=0
$$

and our bound on $\kappa$ becomes explicit:
Let $\kappa_{1, n}^{*}$ be the situation under which the sums of lognormal conserve the lognormal density, with the same first two moments. We have

$$
\begin{gathered}
0 \leq \kappa_{1, n}^{*} \leq 1, \\
\kappa_{1, n}^{*}=2-\frac{\log (n)}{\log \left(\frac{n \operatorname{erf}\left(\frac{\sqrt{\log \left(\frac{n+e^{\sigma^{2}-1}}{n}\right)}}{2 \sqrt{2}}\right)}{\operatorname{erf}\left(\frac{\sigma}{2 \sqrt{2}}\right)}\right)}
\end{gathered}
$$

1) Heuristic attempt: Among other heuristic approaches, we can see in two steps how 1) under high values of $\sigma, \kappa_{1, n} \rightarrow \kappa_{1, n}^{*}$, since the law of large numbers slows down, and 2) $\kappa_{1, n}^{*} \xrightarrow{\sigma \rightarrow \infty} 1$.
2) Loulakis' Proof: Proving the upper bound, that for high variance $\kappa_{1, n}$ approaches 1 has been shown formally my Michail Loulaki $S^{3}$ which we summarize as follows. We start with the identify $\mathbb{E}(|X-m|)=2 \int_{m}^{\infty}(x-m) f(x) d x=2 \int_{m}^{\infty} \bar{F}_{X}(t) d t$, where $f($.$) is the density, m$ is the mean, and $\bar{F}_{X}($.$) is the survival function. Further, \mathbb{M}(n)=2 \int_{n m}^{\infty} \bar{F}(x) d x$. Assume $\mu=\frac{1}{2} \sigma^{2}$, or $X=\exp \left(\sigma Z-\frac{\sigma^{2}}{2}\right)$ where Z is a standard normal variate. Let $S_{n}$ be the sum $X_{1}+\ldots+X_{n}$; we get $\mathbb{M}(n)=2 \int_{n}^{\infty} \mathbb{P}\left(S_{n}>\right. t) d t$. Using the property of subexponentiality $([28]), \mathbb{P}\left(S_{n}>t\right) \geq \mathbb{P}\left(\max _{0<i \leq n}\left(X_{i}\right)>t\right) \geq n \mathbb{P}\left(X_{1}>t\right)-\binom{n}{2} \mathbb{P}\left(X_{1}>t\right)^{2}$. Now $\mathbb{P}\left(X_{1}>t\right) \xrightarrow{\sigma \rightarrow \infty} 1$ and the second term to 0 (using Hölder's inequality).

Skipping steps, we get $\liminf _{\sigma \rightarrow \infty} \frac{\mathbb{M}(n)}{\mathbb{M}(1)} \geq n$, while at the same time we need to satisfy the bound $\frac{\mathbb{M}(n)}{\mathbb{M}(1)} \leq n$. So for $\sigma \rightarrow \infty$ ,$\frac{\mathbb{M}(n)}{\mathbb{M}(1)}=n$, hence $\kappa_{1, n} \xrightarrow{\sigma \rightarrow \infty} 1$.
3) Pearson Family approach for computation: For computational purposes, for the $\sigma$ parameter not too large (below $\approx .3$, we can use the Pearson family for computational convenience -although the lognormal does not belong to the Pearson class (the normal does, but we are close enough for computation). Intuitively, at low sigma, the first four moments can be sufficient because of the absence of large deviations; not at higher sigma for which conserving the lognormal would be the right method.

The use of Pearson class is practiced in some fields such as information/communication theory, where there is a rich literature: for summation of lognormal variates see Nie and Chen, [29], and for Pearson IV, [30], [31].

The Pearson family is defined for an appropriately scaled density $f$ satisfying the following differential equation.

$$
\begin{equation*}
f^{\prime}(x)=-\frac{\left(a_{0}+a_{1} x\right)}{b_{0}+b_{1} x+b_{2} x^{2}} f(x) \tag{12}
\end{equation*}
$$

[^3]We note that our parametrization of $a_{0}, b_{2}$, etc. determine the distribution within the Pearson class - which appears to be the Pearson IV. Finally we get an expression of mean deviation as a function of $n, \sigma$, and $\mu$.

Let $m$ be the mean. Diaconis et al [32] from an old trick by De Moivre, Suzuki [33] show that we can get explicit mean absolute deviation. Using, again, the identity $\mathbb{E}(|X-m|)=2 \int_{m}^{\infty}(x-m) f(x) \mathrm{d} x$ and integrating by parts,

$$
\begin{equation*}
\mathbb{E}(|X-m|)=\frac{2\left(b_{0}+b_{1} m+b_{2} m^{2}\right)}{a_{1}-2 b_{2}} f(m) \tag{13}
\end{equation*}
$$

We use cumulants of the n -summed lognormal to match the parameters. Setting $a_{1}=1$, and $m=\frac{b_{1}-a_{0}}{1-2 b_{2}}$, we get

$$
\left\{\begin{aligned}
a_{0} & =\frac{e^{\mu+\frac{\sigma^{2}}{2}}\left(-12 n^{2}+(3-10 n) e^{4 \sigma^{2}}+6(n-1) e^{\sigma^{2}}+12(n-1) e^{2 \sigma^{2}}-(8 n+1) e^{3 \sigma^{2}}+3 e^{5 \sigma^{2}}+e^{6 \sigma^{2}}+12\right)}{2\left(6(n-1)+e^{2 \sigma^{2}}\left(e^{\sigma^{2}}\left(5 e^{\sigma^{2}}+4\right)-3\right)\right)} \\
b_{2} & =\frac{e^{2 \sigma^{2}}\left(e^{\sigma^{2}}-1\right)\left(2 e^{\sigma^{2}}+3\right)}{2\left(6(n-1)+e^{2 \sigma^{2}}\left(e^{\sigma^{2}}\left(5 e^{\sigma^{2}}+4\right)-3\right)\right)} \\
b_{1} & =\frac{\left(e^{\sigma^{2}}-1\right) e^{\mu+\frac{\sigma^{2}}{2}}\left(e^{\sigma^{2}}\left(e^{\sigma^{2}}\left(e^{\sigma^{2}}\left(-4 n+e^{\sigma^{2}}\left(e^{\sigma^{2}}+4\right)+7\right)-6 n+6\right)+6(n-1)\right)+12(n-1)\right)}{2\left(6(n-1)+e^{2 \sigma^{2}}\left(e^{\sigma^{2}}\left(5 e^{\sigma^{2}}+4\right)-3\right)\right)} \\
b_{0} & =-\frac{n\left(e^{\sigma^{2}}-1\right) e^{2\left(\mu+\sigma^{2}\right)}\left(e^{\sigma^{2}}\left(-2(n-1) e^{\sigma^{2}}-3 n+e^{3 \sigma^{2}}+3\right)+6(n-1)\right)}{2\left(6(n-1)+e^{2 \sigma^{2}}\left(e^{\sigma^{2}}\left(5 e^{\sigma^{2}}+4\right)-3\right)\right)}
\end{aligned}\right.
$$

4) Polynomial expansions: Other methods, such as Gram-Charlier expansions, such as Schleher [34], Beaulieu,[35], proved less helpful to obtain $\kappa_{n}$. At high values of $\sigma$, the approximations become unstable as we include higher order Lhermite polynomials. See review in Dufresne [36] and [37].

## C. Exponential

The exponential is the "entry level" fat tails, just at the border.

$$
f(x)=\quad \lambda e^{-\lambda x}, \quad x \geq 0
$$

By convolution the sum $Z=X_{1}, X_{2}, \ldots X_{n}$ we get, by recursion, since $f(y)=\int_{0}^{y} f(x) f(y-x) d x=\lambda^{2} y e^{-\lambda y}$ :

$$
\begin{equation*}
f_{n}(z)=\frac{\lambda^{n} z^{n-1} e^{-\lambda z}}{(n-1)!} \tag{14}
\end{equation*}
$$

which is the gamma distribution; we get the mean deviation for $n$ summands:

$$
\begin{equation*}
\mathbb{M}(n)=\frac{2 e^{-n} n^{n}}{\lambda \Gamma(n)} \tag{15}
\end{equation*}
$$

hence:

$$
\begin{equation*}
\kappa_{1, n}=2-\frac{\log (n)}{n \log (n)-n-\log (\Gamma(n))+1} \tag{16}
\end{equation*}
$$

We can see the asymptotic behavior is equally slow (similar to the student) although the exponential distribution is sitting at the cusp of subexponentiality:

$$
\lim _{n \rightarrow \infty} \log (n) \kappa_{1, n}=4-2 \log (2 \pi)
$$

## D. Negative kappa

Consider the simple case of a Gaussian with switching means and variance: with probability $\frac{1}{2}, X \sim \mathcal{N}\left(\mu_{1}, \sigma_{1}\right)$ and with probability $\frac{1}{2}, X \sim \mathcal{N}\left(\mu_{2}, \sigma_{2}\right)$. The kurtosis will be

$$
\begin{equation*}
\text { Kurtosis }=3-\frac{2\left(\left(\mu_{1}-\mu_{2}\right)^{4}-6\left(\sigma_{1}^{2}-\sigma_{2}^{2}\right)^{2}\right)}{\left(\left(\mu_{1}-\mu_{2}\right)^{2}+2\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)\right)^{2}} \tag{17}
\end{equation*}
$$

As we see the kurtosis is a function of $d=\mu_{1}-\mu_{2}$. For situations where $\sigma_{1}=\sigma_{2}, \mu_{1} \neq \mu_{2}$, the kurtosis will be below that of the regular Gaussian, and our measure will naturally be negative. In fact for the kurtosis to remain above 3,

$$
|d| \leq \sqrt[4]{6} \sqrt{\max \left(\sigma_{1}, \sigma_{2}\right)^{2}-\min \left(\sigma_{1}, \sigma_{2}\right)^{2}}
$$

the stochasticity of the mean offsets the stochasticity of volatility.
These situations with thinner tails than the Gaussian are encountered with bimodal situations where $\mu_{1}$ and $\mu_{2}$ are separated; the effect becomes acute when they are separated by several standard deviations. Let $\mathrm{d}=\mu_{1}-\mu_{2}$ and $\sigma=\sigma_{1}=\sigma_{2}$ (to achieve minimum kurtosis),

$$
\begin{equation*}
\kappa_{1}=\frac{\log (4)}{\log (\pi)-2 \log \left(\frac{\sqrt{\pi} d e^{\frac{d^{2}}{4 \sigma^{2}}} \operatorname{erf}\left(\frac{d}{2 \sigma}\right)+2 \sqrt{\sigma^{2}} e^{\frac{d^{2}}{4 \sigma^{2}}}+2 \sigma}{d e^{\frac{d^{2}}{4 \sigma^{2}}} \operatorname{erf}\left(\frac{d}{2 \sqrt{2} \sigma}\right)+2 \sqrt{\frac{2}{\pi}} \sigma e^{\frac{d^{2}}{8 \sigma^{2}}}}\right)}+2 \tag{18}
\end{equation*}
$$

which we see is negative for wide values of $\mu_{1}-\mu_{2}$.

## References

[1] S. Kotz and N. Johnson, Encyclopedia of Statistical Sciences. Wiley, 2004.
[2] A. Tversky and D. Kahneman, "Belief in the law of small numbers." Psychological bulletin, vol. 76, no. 2, p. 105, 1971.
[3] M. Falk, J. Hüsler, and R.-D. Reiss, Laws of small numbers: extremes and rare events. Springer Science \& Business Media, 2010.
[4] N. N. Taleb, Technical Incerto Vol 1: The Statistical Consequences of Fat Tails, Papers and Commentaries. Monograph, 2018.
[5] T. Pham-Gia and T. Hung, "The mean and median absolute deviations," Mathematical and Computer Modelling, vol. 34, no. 7-8, pp. 921-936, 2001.
[6] X. Gabaix, "Power laws in economics and finance," National Bureau of Economic Research, Tech. Rep., 2008.
[7] N. N. Taleb, "Finiteness of variance is irrelevant in the practice of quantitative finance," Complexity, vol. 14, no. 3, pp. 66-76, 2009.
[8] V. V. Uchaikin and V. M. Zolotarev, Chance and stability: stable distributions and their applications. Walter de Gruyter, 1999.
[9] J.-P. Bouchaud and M. Potters, Theory of financial risk and derivative pricing: from statistical physics to risk management. Cambridge University Press, 2003.
[10] D. Sornette, Critical phenomena in natural sciences: chaos, fractals, selforganization, and disorder: concepts and tools. Springer, 2004.
[11] B. Mandelbrot, "The pareto-levy law and the distribution of income," International Economic Review, vol. 1, no. 2, pp. 79-106, 1960.
[12] C. Dagum, "Inequality measures between income distributions with applications," Econometrica, vol. 48, no. 7, pp. 1791-1803, 1980.
[13] -, Income distribution models. Wiley Online Library, 1983.
[14] P. Cirillo, "Are your data really pareto distributed?" Physica A: Statistical Mechanics and its Applications, vol. 392, no. 23, pp. 5947-5962, 2013.
[15] H. Markowitz, "Portfolio selection*," The journal of finance, vol. 7, no. 1, pp. 77-91, 1952.
[16] H. Neth and G. Gigerenzer, "Heuristics: Tools for an uncertain world," Emerging trends in the social and behavioral sciences: An Interdisciplinary, Searchable, and Linkable Resource, 2015.
[17] N. N. Taleb, Skin in the Game: Hidden Asymmetries in Daily Life. Penguin (London) and Random House (N.Y.), 2018.
[18] E. O. Thorp, "Optimal gambling systems for favorable games," Revue de l'Institut International de Statistique, pp. 273-293, 1969.
[19] N. N. Taleb, "Errors, robustness, and the fourth quadrant," International Journal of Forecasting, vol. 25, no. 4, pp. 744-759, 2009.
[20] S. Benartzi and R. H. Thaler, "Naive diversification strategies in defined contribution saving plans," American economic review, vol. 91, no. 1, pp. 79-98, 2001.
[21] S. Benartzi and R. Thaler, "Heuristics and biases in retirement savings behavior," Journal of Economic perspectives, vol. 21, no. 3, pp. 81-104, 2007.
[22] H. Windcliff and P. P. Boyle, "The 1/n pension investment puzzle," North American Actuarial Journal, vol. 8, no. 3, pp. 32-45, 2004.
[23] V. DeMiguel, L. Garlappi, and R. Uppal, "Optimal versus naive diversification: How inefficient is the $1 / \mathrm{n}$ portfolio strategy?" The review of Financial studies, vol. 22, no. 5, pp. 1915-1953, 2007.
[24] S. Makridakis and N. Taleb, "Decision making and planning under low levels of predictability," 2009.
[25] B. B. Mandelbrot and N. N. Taleb, "Random jump, not random walk," 2010.
[26] "NIST Digital Library of Mathematical Functions," http://dlmf.nist.gov/, Release 1.0.19 of 2018-06-22, f. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller and B. V. Saunders, eds. [Online]. Available: http://dlmf.nist.gov/
[27] D. J. Newman, A problem seminar. Springer Science \& Business Media, 2012.
[28] E. Pitman, "Subexponential distribution functions," J. Austral. Math. Soc. Ser. A, vol. 29, no. 3, pp. 337-347, 1980.
[29] H. Nie and S. Chen, "Lognormal sum approximation with type iv pearson distribution," IEEE Communications Letters, vol. 11, no. 10, 2007.
[30] S. Chen, H. Nie, and B. Ayers-Glassey, "Lognormal sum approximation with a variant of type iv pearson distribution," IEEE Communications Letters, vol. 12, no. 9, 2008.
[31] M. Di Renzo, F. Graziosi, and F. Santucci, "Further results on the approximation of log-normal power sum via pearson type iv distribution: a general formula for log-moments computation," IEEE Transactions on Communications, vol. 57, no. 4, 2009.
[32] P. Diaconis and S. Zabell, "Closed form summation for classical distributions: variations on a theme of de moivre," Statistical Science, pp. 284-302, 1991.
[33] G. Suzuki, "A consistent estimator for the mean deviation of the pearson type distribution," Annals of the Institute of Statistical Mathematics, vol. 17, no. 1, pp. 271-285, 1965.
[34] D. Schleher, "Generalized gram-charlier series with application to the sum of log-normal variates (corresp.)," IEEE Transactions on Information Theory, vol. 23, no. 2, pp. 275-280, 1977.
[35] N. C. Beaulieu, A. A. Abu-Dayya, and P. J. McLane, "Estimating the distribution of a sum of independent lognormal random variables," Communications, IEEE Transactions on, vol. 43, no. 12, p. 2869, 1995.
[36] D. Dufresne, "Sums of lognormals," in Proceedings of the 43rd actuarial research conference. University of Regina, 2008.
[37] D. Dufresne et al., "The log-normal approximation in financial and other computations," Advances in Applied Probability, vol. 36, no. 3, pp. 747773, 2004.


[^0]:    The author owes the most to the focused comments by Michail Loulakis who, in addition, provided the rigorous derivations for the limits of the $\kappa$ for the Student T and lognormal distributions, as well as to the patience and wisdom of Spyros Makridakis. The paper was initially presented at Extremes and Risks in Higher Dimensions, Sept 12-16 2016, at the Lorentz Center, Leiden and at Jim Gatheral's Festschrift at the Courant Institute, in October 2017. The author thanks Jean-Philippe Bouchaud, John Einmahl, Pasquale Cirillo, and others. Laurens de Haan suggested changing the name of the metric from "gamma" to "kappa" to avoid confusion. Additional thanks to Colman Humphrey, Michael Lawler, Daniel Dufresne and others for discussions and insights with derivations.

[^1]:    ${ }^{1}$ By "fat tails" we are using the generic term used by finance practitioners to refer to thicker tails than the Gaussian, without reference to any particular class of distributions.

[^2]:    ${ }^{2}$ Robert Israel on Math Stack Exchange

[^3]:    ${ }^{3}$ Review of this paper; Loulakis proposed a formal proof in place of the heuristic derivation.

