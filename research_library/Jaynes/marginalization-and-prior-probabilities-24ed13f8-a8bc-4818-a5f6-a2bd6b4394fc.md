To appear in Studies in Bayesian Statistics, in honor of Sir Harold Jeffreys (Arnold Zellner, Editor)

# MARGINALIZATION AND PRIOR PROBABILITIES* 

Edwin T. Jaynes<br>Department of Physics<br>Washington University<br>St. Louis, Missouri 63130

1. INTRODUCTION ..... 2
2. THE PARADOX ..... 3
3. THE RESOLUTION ..... 4
4. A REINTERPRETATION ..... 10
5. IMPROPER PRIORS - DISCUSSION ..... 12
6. THE INTEGRAL EQUATIONS ..... 14
7. AN EXAMPLE ..... 19
8. THE ONE-DIMENSIONAL CASE ..... 22
9. HIGHER DIMENSIONALITY ..... 28
10. SINGULAR SOLUTIONS: KNOWLEDGE IS IGNORANCE ..... 35
11. STRUCTURE OF THE INTEGRAL EQUATIONS ..... 38
12. EXAMPLE 1 - A FOURTH LOOK ..... 42
13. CONCLUSION ..... 47
14. APPENDIX A - COMMENTS ON GROUP ANALYSIS ..... 48
[^0]A recent article of Dawid, Stone, and Zidek (1973) notes two Bayesian calculation methods--the first using an improper prior, the second avoiding it--that one feels intuitively ought to lead to the same result, but in general do not. This "marginalization paradox" has been interpreted widely as revealing a fundamental inconsistency in the common Bayesian practice of using improper priors to express prior ignorance.

We argue that, on the contrary, resolution of the paradox is very simple, the discrepancy arising not from any defect of improper priors, but from a rather subtle failure of the second method to take into account all the relevant information. This situation, far from revealing an inconsistency in Bayesian methods, shows that to violate them in seemingly harmless ways, can generate paradoxes; i.e., it is only by strict adherence to the Bayesian principles expounded by Jeffreys in 1939, that one can avoid inconsistencies in statistical reasoning.

The marginalization process is then turned to advantage by showing that it leads to a new means for defining what is meant by "uninformative" and for constructing noninformative priors, as the solution of an integral equation. This method draws only upon the universally accepted principles of probability theory, making no appeal to such additional desiderata as entropy, group invariance, or Fisher information. However, its range of applicability is still largely unexplored.
2. THE PARADOX

A conscientious Bayesian $B_{1}$ studies a problem with parameters $\theta$ which he partitions into two sets, $\theta=(n, \zeta)$, being interested only in inferences about $\zeta$. Dawid, Stone, and Zidek (1973; hereafter denoted DSZ) note that, in several examples where $B_{1}$ uses an improper prior for $n$, the data $x$ may also be partitioned into two sets, $x=(y, z)$ in such a way that $B_{1}$ 's marginal posterior distribution for $\zeta$ "is a function of $z$ only," while the sampling distribution of $z$ depends only on $\zeta$.

A lazy Bayesian $B_{2}$ then tries to derive the posterior distribution $p(\zeta \mid x)=p(\zeta \mid z)$ more easily by applying Bayes' theorem directly to the sampling distribution $p(z \mid \zeta)$; and finds that he cannot reproduce $B_{1}$ 's result whatever prior $\pi(\zeta)$ he assigns.

DSZ then point the accusing finger at $B_{1}$ thus: " $B_{2}$ 's intervention has revealed the paradoxical unBayesianity of $B_{1}$ 's posterior distribution for $5 . "$ In the ensuing discussion there was near unanimity of all opinions expressed, holding that $B_{1}$ is the party at fault, his transgression lying in his use of an improper prior.

A group-theoretical analysis by DSZ showed that if the sampling distribution $p(d y d z \mid n s)$ has a certain group structure [invariant under the combined action of coupled homomorphic groups $G, \bar{G}$ which are exact and transitive on the spaces $S(y), S(\eta)]$, the paradox can be avoided by choosing the prior as the right-invariant measure on $S(n)$. This procedure has, indeed, been advocated by a long list of writers starting with Poincare (1912). However, as soon as we pass beyond the case of location and scale parameters it is rather exceptional to find a problem with all that group structure; and the paradox persists even in problems that have no group structure at all. In general, therefore, no way emerged for avoiding the paradox.

Predictably, some have seized upon this as a new tool for the abrogation of Bayesian statistics in general. However unimportant the practical consequences may be, it is imperative for Bayesian theory that this puzzle be cleared up.

In the following we argue that (1) Resolution of the paradox is far too simple a problem to be in need of group-theoretical analysis. That it can be made to appear and disappear by different choices of the n-prior, shows immediately where the difficulty lies. (2) the real cause of the paradox is not $B_{1}$ 's use of improper priors, or indeed any transgression on $\mathrm{B}_{1}$ 's part. On the contrary, it appears only when $\mathrm{B}_{2}$ violates elementary Bayesian principles. $\mathrm{B}_{2}$ 's transgression was concealed from view by concise notation. (3) Nevertheless, the prior $\pi(n)$ that "avoids the paradox" has a useful interpretation as being, in a certain sense, "completely uninformative."
(4) Recognizing this, marginalization leads to a new means for constructing noninformative priors, via a set of simultaneous integral equations. This method is consistent with, but appears more general than, the group analysis.
3. THE RESOLUTION

We must be careful to note exactly what the first quoted statement of DSZ means. From the mathematics it is clear that to say the posterior distribution of $\zeta$ "is a function of $z$ only" means that it depends on the data $x$ only through the value of $z$. But of course, any posterior distribution depends not only on the data, but also on the prior information. As Jeffreys (1939) stressed, to avoid ambiguities the prior information (or hypotheses) on which our probabilities are conditional, ought to be stated explicitly to the right of the stroke in our probability symbols $p(A \mid B)$.
$B_{1}$ 's prior information includes the whole structure of the model, the qualitative fact of the existence of the components $n$ and $y$; and the prior distribution of $\eta$. How, then, can one be sure that $B_{2}$ is justified in considering only the reduced problem in which ( $n, y$ ) never appear at all? According to Bayesian principles, one may not disregard any part of either the data or the prior information, unless that part is shown to be irrelevant in the sense that it cancels out mathematically.
$B_{2}$ 's reduction appears, at first glance, to be reasonable; but so did a multitude of ad hoc procedures of non-Bayesian statistics, which were found eventually to contain defects. Surely, there is no room for personal opinions about this; the mathematical rules of probability theory are quite competent to tell us whether $B_{2}$ 's reduction is or is not justified.

As a constant reminder of the presence of prior information, we extend the notation of DSZ by introducing the symbols $I_{1}, I_{2}$ to stand for the totality of prior information used by $B_{1}, B_{2}$ respectively. The quoted first statement is then, more precisely,

$$
\begin{equation*}
p\left(\zeta \mid x I_{1}\right)=p\left(\zeta \mid z I_{1}\right) \tag{1}
\end{equation*}
$$

Now the rules of probability theory tell us that

$$
\begin{equation*}
p\left(\zeta \mid \times I_{1}\right)=\int d \eta p\left(\zeta \mid \eta \times I_{1}\right) p\left(n \mid \times I_{1}\right) \tag{2}
\end{equation*}
$$

If, given $I_{1}$ and all the data $x$, additional knowledge of $\eta$ would be irrelevant for inference about $\zeta$; i.e., if

$$
\begin{equation*}
p\left(\zeta \mid n \times I_{1}\right)=p\left(\zeta \mid \times I_{1}\right) \tag{3}
\end{equation*}
$$

then $\eta$ integrates out of (2) trivially. But if (3) does not hold, then $\eta$ is relevant, and the posterior distribution $p\left(\eta \mid \times I_{1}\right)$ intrudes itself inevitably into the problem, bringing with it a dependence on the prior $-\left(\cdot \mid I_{1}\right)$.

In this case, we have to expect that the separation property (1) cannot hold for all $n$-priors. If (1) holds for some class $C$ of priors, then while $p\left(\zeta \mid \times I_{1}\right)$ is, in a sense, "a function of $z$ only," it is a different function of $\zeta$ for different $n$-priors in $C$. But since $B_{2}$ 's posterior distribution $p\left(\zeta \mid z I_{2}\right)$ is independent of $\pi\left(n \mid I_{1}\right)$, it appears that we have at hard all the material needed to manufacture paradoxes. In other words, we suggest that: this paradox has, fundamentally, nothing to do with improper priors; 3 , and $B_{2}$ obtain different results when, and only when, $B_{2}$ ignores relevant prior information (about $n$ and/or the model), that $\mathrm{B}_{1}$ is taking into account.

It remains to be shown that the mechanism just suggested is the one actually operative in the examples of CSZ. Since (3) is equivalent to

$$
\begin{equation*}
p(\eta, \zeta \mid \times I)=p(\eta \mid \times I) p(\zeta \mid \times I) \tag{4}
\end{equation*}
$$

we examine some of the DSZ examples for this factorization property.

Example 1. The model is described in DSZ. For present purposes we need note only that the raw data $x=\left\{x_{1} \ldots x_{n}\right\}$ are partitioned into $y \equiv x_{1}$, and $z \equiv\left\{z_{i}=x_{i} / x_{1}, 1 \leq i \leq n\right\}$. The joint posterior distribution is

$$
\begin{equation*}
p\left(n \zeta \mid \times I_{1}\right) \propto \pi\left(\zeta \mid I_{1}\right) c^{-\zeta} n^{n} \exp (-n y Q) \pi\left(n \mid I_{1}\right) \tag{5}
\end{equation*}
$$

where

$$
\begin{equation*}
Q(\zeta, z) \equiv \sum^{\zeta} z_{i}+c \sum_{\zeta+1}^{n} z_{i} \tag{6}
\end{equation*}
$$

is a function that is known from the data. Here $B_{1}$ has helped $B_{2}$ 's prospects as much as possible by assigning independent priors to $\eta, \zeta$. Nevertheless, the likelihood function mixes them up and we find the conjectured lack of factorization (4). $\mathrm{B}_{1}$ 's marginal posterior distribution is

$$
\begin{equation*}
p\left(\zeta \mid x I_{1}\right) \propto \pi\left(\zeta \mid I_{1}\right) c^{-\zeta \int_{0}^{(\infty)}} n^{n} e^{-\cdots \varphi Q_{0}} \pi\left(n \mid I_{1}\right) d n \tag{7}
\end{equation*}
$$

from which we note several things:
(A) As predicted, the dependence on the prior $\pi\left(n \mid I_{1}\right)$ is manifest. Prior information about $n$ is clearly relevant to inference about $\zeta$; and $B_{2}$ 's reduction violates Eayesian principles by throwing it away.
(B) The dependence on $y$ drops out on normalization, leading to (1), if and only if the n-prior is in the class $\left\{C ; \pi\left(n \mid I_{1}\right) \propto n^{k},-n-1<k<\infty\right\}$, which includes all those considered by DSZ.
(C) For any prior in class $C$ there are no convergence problems. It is therefore difficult to see how use of an improper prior can in itself be grounds for reproach; all of $B_{1}$ 's conclusions can be approximated to any accuracy we please (e.g., one part in $10^{1000}$ ) by use of a proper prior (as shown explicitly below, Eq. (24)).
(D) Cn the other hand, use of a proper prior, $f \pi\left(n \mid I_{1}\right) d n=1$, will take us out of the class $C$. But then the statistic $y$ cannot be disentangled, and remains relevant; the separation property (1) is lost, and $\mathrm{B}_{2}$ becomes superfluous.
(E) The proof of DSZ that use of proper priors avoids the paradox, rested on two assumptions: that $B_{1}$ uses a proper prior, and [DSZ, Eq. (1.20)] that the separation property still holds. But for this model, those assumptions are contradictory. DSZ supposed that, with proper priors, the paradox would disappear because $\mathrm{B}_{1}$ and $\mathrm{B}_{2}$ then agree. We now see that, at least in this example, the paradox disappears rather because the comparison disappears; $\mathrm{B}_{2}$ can no longer play his game at all.

For efficient verbalization at this point, we need to coin a new term. A prior $\pi(1)$ that leads to the separation property (1) nullifies the effect of the data $y$ for inference about $\zeta$. Let us call such a prior nullifying (more precisely: $y$-nullifying within the context of a particular model).

What DSZ proved is then: If a proper prior is also nullifying, then it necessarily leaves $B_{1}$ and $B_{2}$ in agreement. However, except in the trivial case of complete independence: $p(d y d z \mid n \zeta)=p(d y \mid \eta) p(d z \mid \zeta)$ one cannot assume ohne weiteres the existence of such a prior, as this example illustrates.

Example 2. We have parameters $\theta=\left(\mu_{1}, \mu_{2} \sigma\right)$ and data $x=\left(u_{1}, u_{2}, s\right)$ with sampling density function

$$
\begin{equation*}
p\left(u_{1} u_{2} s / \mu_{1} \mu_{2} \sigma\right)=A\left(s^{\nu-1} / \sigma^{\nu+2}\right) \exp (-Q) \tag{8}
\end{equation*}
$$

where $A$ is a normalizing constant and

$$
\begin{equation*}
Q \equiv \frac{1}{2 \sigma^{2}}\left[\left(u_{1}-\mu_{1}\right)^{2}+\left(u_{2}-\mu_{2}\right)^{2}+v s^{2}\right] \tag{9}
\end{equation*}
$$

However, we are interested in inference only about

$$
\begin{equation*}
\zeta \equiv \frac{\mu_{1}-\mu_{2}}{\sigma \sqrt{2}} \tag{10}
\end{equation*}
$$

and the sampling distribution of

$$
\begin{equation*}
z=\frac{u_{1}-u_{2}}{s \sqrt{2}} \tag{11}
\end{equation*}
$$

is found to depend only on $\zeta$ :

$$
\begin{equation*}
p\left(z \mid \mu_{1} \mu_{2} \sigma\right)=p(z \mid \zeta)=\sqrt{2 \pi} A \int_{0}^{\infty} \omega^{\nu} e^{-R} d \omega \tag{12}
\end{equation*}
$$

where

$$
\begin{equation*}
R(z, \zeta, \omega) \equiv \frac{1}{2}\left[v \omega^{2}+(\omega z-\zeta)^{2}\right] \tag{13}
\end{equation*}
$$

Making the additional change of variables

$$
\begin{equation*}
\mu=\frac{1}{2}\left(\mu_{1}+\mu_{2}\right) \quad, \quad u=\frac{1}{2}\left(u_{1}+u_{2}\right) \tag{14}
\end{equation*}
$$

the unwanted components are $\eta=(\mu, \sigma) ; y=(u, s)$, and $B_{1}$ 's posterior distribution of $\zeta$ is

$$
\begin{equation*}
p\left(\zeta \mid \times I_{1}\right) \propto \pi\left(\zeta \mid I_{1}\right) \int_{0}^{\infty} \omega^{\nu} d \omega e^{-R} f(u, \sigma) \tag{15}
\end{equation*}
$$

where

$$
\begin{equation*}
f(u, \sigma) \equiv \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} d \mu \pi(\mu, \sigma) \exp \left[-\left(\frac{u-\mu}{\sigma}\right)^{2}\right] \tag{16}
\end{equation*}
$$

and in the integration over $\omega=s / \sigma, s$ is held constant while $\sigma$ varies. Again, a certain class $C$ of priors $\pi(n)=\pi(\mu, \sigma)$ is found to be nullifying, leading to the separation property (1). This includes the class

$$
\begin{equation*}
\left\{c^{\prime}: d \mu_{1} d \mu_{2} \sigma^{-k} d \sigma=\sqrt{2} d \zeta d \mu \sigma^{1-k} d \sigma\right\} \tag{17}
\end{equation*}
$$

considered by DSZ, or indeed any prior $\pi(\mu, \sigma)$ independent of $\mu$, for which $(15)$ is independent of $y$ :

$$
\begin{equation*}
p\left(\zeta \mid x I_{1}\right) \propto \pi\left(\zeta \mid I_{1}\right) \int_{0}^{\infty} \omega^{\nu-1} d \omega e^{-R} \pi(\sigma) \tag{18}
\end{equation*}
$$

From this we confirm Eq. (1.3) of DSZ (with $k=1$ ) and comparing with (12) it is seen that $B_{1}$ and $B_{2}$ will agree if $k=2$. Once again it is clear from (15), (18) that in general their conclusions will differ because $B_{1}$ is taking into account relevant prior information about $\eta=(\mu, \sigma)$ that $B_{2}$ is ignoring.

Rather than continuing with a rather tedious, but still superficial, inspection of more examples, which would only reconfirm the mechanism already established, we can get a better understanding by returning to a second look at Example 1.
4. A REINTERPRETATION

We may take a more charitable view of $B_{2}$, if DSZ will grant a similar courtesy to $B_{1}$. In these examples, independently of all questions of priors, it is true that the marginal sampling distribution of $z$ depends only on $\zeta$. Suppose that we now regard $\mathrm{B}_{2}$, not as a lazy fellow who "always arrives late on the scene of inference" and tries to simplify $B_{1}$ 's analysis; but merely, through no fault of his own, an uninformed fellow whose knowledge about the experiment consists only of the sampling distribution

$$
\begin{equation*}
p\left(z \mid \zeta I_{1}\right)=p\left(z \mid \zeta I_{2}\right) \tag{19}
\end{equation*}
$$

and is unaware of the existence of the components $(n, y)$. Then $B_{2}$ is following strict Bayesian principles, and

$$
\begin{equation*}
p\left(\zeta \mid z I_{2}\right) \propto \pi\left(\zeta \mid I_{2}\right) p\left(z \mid \zeta I_{2}\right) \tag{20}
\end{equation*}
$$

will always represent the best inferences that can be made on the information he has-- whether or not $B_{1}$ 's posterior distribution has the separation property $p\left(\zeta \mid y z I_{1}\right)$ independent of $y$, that initiated all this.

It then makes sense to compare $B_{2}$ 's results with $B_{1}$ 's in all cases, whether $B_{1}$ 's prior for $\eta$ is proper or improper; and in all cases the comparison will reveal just how much difference $B_{1}$ 's extra information has made. For the most meaningful comparison, we suppose they have the same prior information about $\zeta$ :

$$
\begin{equation*}
\pi\left(\zeta \mid I_{1}\right)=\pi\left(\zeta \mid I_{2}\right)=\pi(\zeta) \tag{21}
\end{equation*}
$$

Returning now to Example 1, from Eq. (1.2) of DSZ, $B_{2}$ 's conclusions are given by

$$
\begin{equation*}
p\left(\zeta \mid z I_{2}\right) \propto \pi(\zeta) c^{-\zeta}[Q(\zeta, z)]^{-n} \tag{22}
\end{equation*}
$$

while $B_{1}$ 's are given by our Eq. (7). Let $B_{1}$ assign a proper n-prior of the conjugate form

$$
\begin{equation*}
\pi\left(n \mid I_{1}\right) \propto n^{k-1} e^{-t \eta}, \quad t>0 \tag{23}
\end{equation*}
$$

which as $t \rightarrow 0$ goes into the family of improper priors used by DSZ. Then 81's result is

$$
\begin{equation*}
p\left(\zeta \mid y z I_{1}\right) \propto \pi(\zeta) c^{-n}\left[\frac{y}{t+y Q(\zeta, z)}\right]^{n+k} \tag{24}
\end{equation*}
$$

which, we note, goes smoothly and continuously into $\mathrm{B}_{2}$ 's result (22) as $\mathrm{t} \rightarrow 0, \mathrm{k} \rightarrow 0$.

Sut no "paradoxical unBayesianity" or "impropriety" is apparent. Strictly speaking, the dependence on $y$ drops out, leading to the separation property (1), only when $t=0$, but for $t \ll y Q$ there is virtually no $y$-dependence, even though the prior is still proper. There is no discontinuous change; as t becomes smaller and the prior (23) becomes more nearly nullifying, the $y$-statistic just becomes less and less informative.

If then $B_{1}$, having noted that $t \ll y Q$, decides to simplify (24) by setting $t=0$, this now appears, not as a paradox-creating transgression into the realm of improper priors, but rather as a perfectly harmless and reasonable approximation--indeed, an approximation far better justified than many that are accepted without question in non-Bayesian statistics.

If $B_{1}$ has very little prior information about $\eta$ [i.e., if $(t, k)$ are small], then there is virtually no difference between his conclusions and $B_{2}$ 's, whether his prior is proper or improper. If, on the other hand, $(t, k)$ are large, then $B_{1}$ is in possession of additional, highly cogent, information relevant to inference about $\zeta$; and it is only right and proper that his conclusions deviate from $B_{2}$ 's. Any statistical method that failed
to make use of this information although it was available to the user, would then be deserving of the epithet, "impropriety."
5.

## IMPROPER PRIORS - DISCUSSION

In view of the great emphasis on the issue of improper priors in DSZ and in the ensuing discussion--almost to the exclusion of all else--and subsequent attempts to use this as an argument against all Bayesian methods, some further exegesis defending the use of improper priors is needed.

A sequence $\left\{\pi_{i}\right\}$ of proper priors defines a corresponding sequence $\left\{P_{i}\right\}$ of posterior distributions. Often, even though the limit of $\left\{\pi_{i}\right\}$ is improper, the limit of $\left\{\mathrm{P}_{\mathrm{j}}\right\}$ is a proper, well-behaved, and analytically simple, distribution. The Bayesian will often take that limit for mathematical convenience, after it is clear--whether by specific calculation in the manner of (24) or through past experience with similar problems--that this will make no practical difference in the results.

Often, the experimental data are so much more informative than the prior information that to carry along all the details of any particular proper prior, although in principle the correct thing to do, would in practice only increase the amount of computation without yielding anything of value for the purposes at hand. Usually, it is so clear when we have this situation that there is no need to construct specific sequences of the type (23), (24); one proceeds immediately to the simpler limit.

In a similar way, a person using the Chi-squared test knows in advance, from common sense and the past experience of Statisticians in general, about how much data he needs, and how many categories, to give a test that is good enough for his purposes. Beyond that, further
refinements, although correct in principle, would only increase the amount of computation without useful return. In orthodox statistics, use of a little practical common sense in applying a method is not regarded as an inconsistency. Perhaps, when his methods are more widely understood, the Bayesian may hope to be granted an equal dispensation.

Now, as noted by several participants in the discussion following the DSZ paper and discussed at greater length in Jaynes (1976), it is just the Bayesian results based on noninformative improper priors that correspond closely--often exactly--with those obtained by orthodox methods. In these cases, it is difficult to see how one can reject the Bayesian use of an improper prior, without thereby rejecting with equal force the orthodox method which yields the same result.

On the other hand, in some cases the attempted passage to an improper prior may fail, by yielding a non-normalizable posterior distribution in the limit. This is symptomatic that the experiment is so uninformative that our prior information is, necessarily, still highly relevant to any inference that can be made; and in such a case we had jolly well better take that prior information explicitly into account by using the appropriate proper prior. In this case an orthodox method, by its nature incapable of taking prior information into account, is practically guaranteed to produce absurd or dangerously misleading results [for a specific example, see Jaynes (1976); reply to Kempthorne's comments].

The actual equations both in DSZ and in the present work, are not in any way changed by our reinterpretation of $B_{2}$ 's role; but the analysis is seen in a different and perhaps more constructive light. We are not merely exhibiting the folly of a defective Bayesian procedure--ignoring information or using improper priors. We are comparing two entirely
correct Bayesian procedures, making inferences about the same quantity $\zeta$, at two different stages of knowledge. The parameter $n$ is not merely an "unwanted" complication; it represents new information relevant to the desired inference about $\zeta$.

The comparison is, in effect, a microcosm of an often-occurring real life phenomenon, the effect of advancing knowledge on a scientific inference.

For example, from the known rate ( $z=2 \times 10^{20}$ megawatts) of radiation of energy from the sun, estimate its future lifespan ( $\zeta$ ); how much longer can it continue pouring out energy at that rate? The datum (z) was known 120 years ago about as well as it is today, and on the basis of the laws of physics as then known, $\mathrm{B}_{2}$ [better known as Lord Kelvin ( 1862 )] estimated a future life of $\zeta=$ a few million years; an entirely valid conclusion from the information he had. But today we know of a new parameter ( $n=$ energy release from nuclear reactions) that has an important bearing on the question, and we have new data ( $y=$ abundance of various elements in the sun, and energy release of a number of nuclear reactions). As a result, $B_{1}$ [George Gamow (1945)] reestimated the future life of the sun to be vastly greater, about $10^{10}$ years.

Doubtless, an econometrician could give much more immediate examples; e.g., the effect of new knowledge (the role of oil prices) on prediction of economic activity from models in which, prior to 1973, oil price did not appear as a factor.

## 6. THE INTEGRAL EQUATIONS

Can we extract something of positive value from all this, leaving Bayesian theory with a net gain? As is now clear, there is no reason to be surprised when $B_{1}$ and $B_{2}$ disagree; that was only to be expected. What
is perhaps surprising, and calls for explanation, is rather that in some cases $B_{1}$ 's extra information was unavailing, and they did agree, after all. How is that possible?

Clearly, in all cases, $B_{2}$ was incorporating no prior information about $n$. If, nevertheless, they agree in one case, it seems natural to conclude that, in that case, $B_{1}$ must not have been incorporating any prior information either; at least, none that was relevant to $\zeta$.

The prior $\pi(\eta)$ that leaves them in agreement should, then, have some close relation to the one describing "complete ignorance" of $\eta$, if such exists. Is it possible that marginalization is giving us a new, objective, and above all, workable criterion for defining precisely what is meant by "complete ignorance," and for telling us whether and when such priors do or do not exist?

But we must proceed cautiously. It is not clear how marginalization could tell us that a prior is "completely uninformative" without qualifications. But marginalization can and does provide an answer to the question whether, within the context of a given model, any proposed prior $\pi(\eta)$ is or is not "completely uninformative about $\zeta$."

Two further cautions are necessary. A prior $\pi(n)$ that is held to be uninformative about $n$ ought, one would suppose, to have the property that it is uninformative a fortiori about any other quantity $\zeta$. Clearly, however, the converse need not hold. In any given model, a prior $\pi(n)$ might express very great knowledge about $\eta$; and still be $\zeta$-uninformative because of the functional form of $p(y z \mid n \zeta)$. On the other hand, if one could prove that a given prior $\pi(n)$ is $\zeta$-uninformative for all models in which $n$ appears as a scale parameter, and unique for one, that would seem to be valid grounds for a stronger claim.

Finally, we note that in another respect the property of a prior $\pi(n)$ to leave $B_{1}$ in agreement with $B_{2}$ involves rather more than what one usually means by the term "uninformative." $B_{1}$ 's advantage over $B_{2}$ does not lie only in his prior knowledge of $n$; he has also the additional data $y$. If a prior $\pi(n)$ is to leave him in agreement with $B_{2}$, therefore, it is not enough for $\pi(n)$ to have the passive property of being $\zeta$-uninformative (i.e., of not in itself providing any information relevant to $\varsigma$ ). It must perform also the active function of rendering the new data $y$ irrelevant to $\zeta$; that is what we have termed "nullifying."

The necessary and sufficient condition for a prior $\pi(n)$ to be nullifying independently of $\pi(\zeta)$ is that $B_{1}$ 's quasi-likelihood contains $y$ and $\zeta$ in separate factors:

$$
\begin{equation*}
\int p(y, z \mid \eta, \zeta) \pi(\eta) d \eta=f(y, z) g(z, \zeta) \tag{25}
\end{equation*}
$$

for some functions $f, g$. The surprising discovery of DSZ was then that, while a proper prior that is nullifying is also necessarily uninformative [Proof: integrating $y$ out of (25), it then reduces to $B_{2}$ 's likelihood $p(z \mid \zeta)]$, an improper prior may be nullifying without being uninformative. In Example 1, the prior (23) is nullifying if $t=0$; but it is not uninformative unless $k=0$ also.

Let us seek the necessary and sufficient condition for agreement of $B_{1}, B_{2}$, subject to three assumptions. Firstly the property (19) without which we should have little reason to compare $B_{1}$ and $B_{2}$ at all. Secondly,
it would make little sense to ask whether an $\eta$-prior is uninformative about $\zeta$ if it contained $\zeta$; so we assume that $B_{1}$ assigns independent priors:

$$
\begin{equation*}
\pi\left(n c \mid I_{1}\right)=\pi\left(n \mid I_{1}\right) \pi\left(\zeta_{0} \mid I_{1}\right) \tag{26}
\end{equation*}
$$

Thirdly, DSZ considered whether $B_{2}$ could, by any choice of his prior $\pi\left(\zeta \mid I_{2}\right)$, achieve agreement with $B_{1}$ 's posterior distribution. But for present purposes we cannot allow $\mathrm{B}_{2}$ that much freedom; for if $\mathrm{B}_{1}$ and $\mathrm{B}_{2}$ had different priors for $\zeta$, that would in itself lead to a difference in their conclusions, that really has nothing to do with $B_{1}$ 's prior knowledge about $\eta$, although agreement of the posterior distributions might be, fortuitously, restored by a particular $n$-prior. But in that case it would be very wrong to label such an $\eta$-prior as "uninformative about $\zeta . "$ To avoid this, we must suppose rather that $B_{1}$ and $B_{2}$ start from the same state of prior knowledge about $\zeta$ as in (21):

$$
\pi\left(\zeta \mid I_{1}\right)=\pi\left(\zeta \mid I_{2}\right)=\pi(\zeta)
$$

and end up still in agreement as to the posterior distribution. And by "agreement", we do not mean that they agree for one particular sample or one particular prior. In order to justify saying that $B_{1}$ 's prior for $n$ was completely $\zeta$-uninformative and $y$-nullifying, they must remain in agreement for all data sets $x=(y, z)$, all sample sizes, and all priors $\pi(\zeta)$.

With these assumptions, $B_{1}$ 's posterior distribution is

$$
\begin{equation*}
p\left(\zeta \mid y, z, I_{1}\right) \propto \pi(\zeta) p(z \mid \zeta) \int d n \pi\left(\eta \mid I_{1}\right) p\left(y \mid z \cap \zeta I_{1}\right) \tag{27}
\end{equation*}
$$

While $B_{2}$ 's is

$$
\begin{equation*}
p\left(\zeta \mid z I_{2}\right) \propto \pi(\zeta) p(z \mid \zeta) \tag{28}
\end{equation*}
$$

Evidently, the necessary and sufficient condition for agreement is that

$$
\begin{equation*}
\int d n \pi\left(n \mid I_{1}\right) p\left(y \mid z n \zeta I_{1}\right)=p\left(y \mid z \zeta I_{1}\right) \tag{29}
\end{equation*}
$$

shall be independent of $\zeta$ for all $y, z$. Denoting the parameter space and our partitioning of it into subspaces by $S_{\theta}=S_{\zeta} \otimes S_{\eta}$, we may write (29) as

$$
\begin{equation*}
\int_{S_{\eta}} p(y, z \mid \zeta, \eta) \pi(\eta) d \eta=\lambda(y, z) p(z \mid \zeta) \quad, \quad \zeta \text { in } S_{\zeta} \tag{30}
\end{equation*}
$$

This is a Fredholm integral equation in which the kernel is $B_{1}$ 's likelihood, $K(\zeta, n)=p(y, z \mid \zeta, n)$, the "driving force" is $B_{2}$ 's likel ihood $p(z \mid \zeta)$, and $\lambda(y, z) \equiv p\left(y \mid z I_{1}\right)$ is an unknown function to be determined from (30).

For each possible data set $x=(y, z)$ we have an equation of the form (30); so if a single prior $\pi(n)$ is to suffice for all data sets it must satisfy not just one integral equation, but a large--in general infinite-class of simultaneous integral equations.

Now in other applications we are accustomed to find that a single Fredholm equation has already a unique solution. At first glance, therefore, it seems almost beyond belief that the system of equations (30) could fail to be grossly overdetermined; from which one would be forced to conclude, with the antiBayesian skeptics, that uninformative priors do not exist.

Clearly, the consistency of previous Bayesian thought, which presupposed the existence of uninformative priors, is being put here to a severe test. But it is also an eminently fair and "objective" test. The question whether, in a given model, the notion of an uninformative prior is contradictory, ambiguous, or well defined, is removed from the realm of philosophical debate, and reduced to the question whether a set of simultaneous integral equations is overdetermined, underdetermined, or well-posed.
7. AN EXAMPLE

We know at least that the system of equations (30) is not always overdetermined; for in several examples DSZ were able to recognize particular priors $\pi(n)$ which leave $B_{1}$ and $B_{2}$ in harmony for all samples. Each of the DSZ examples can tell us something about the mathematical structure of (30) and its correspondence with previous group invariance arguments.

Example 1. The sampling distribution is

$$
\begin{equation*}
p(y z \mid n \zeta)=n^{n} c^{n-\zeta} y^{n-1} \exp [-n y Q(z, \zeta)] \tag{31}
\end{equation*}
$$

with $Q(z, 5)$ defined by (6). This gives the marginal sampling distribution

$$
\begin{equation*}
p(z \mid \zeta)=(n-1)!c^{n-\zeta} Q^{-n} . \tag{32}
\end{equation*}
$$

$S_{\eta}$ is the positive real line, and the family of integral equations (30) becomes: for each possible sample $(y, z)$,

$$
\begin{equation*}
\int_{0}^{\infty} \pi(n) n^{n} e^{-\dot{n} y Q} d n=(n-1)!y \lambda(y, z)[y Q(z, \zeta)]^{-n}, \quad \zeta=1,2, \ldots, n-1 . \tag{33}
\end{equation*}
$$

Now choose any two values $\zeta \neq \zeta^{\prime}$, and write $Q \equiv Q(z, \zeta), Q^{\prime} \equiv Q\left(z, \zeta^{\prime}\right)$. Equation (33) then requires that for all $(y, z)$
or

$$
\begin{equation*}
\int_{0}^{\infty} \pi(\eta)(\eta y Q)^{n} e^{-\eta y Q} d \eta=\int_{0}^{\infty} \pi(\eta)\left(\eta y Q^{\prime}\right)^{n} e^{-\eta y Q^{\prime}} d \eta \tag{34}
\end{equation*}
$$

$$
\begin{equation*}
\int_{0}^{\infty}\left[\pi(n)-\frac{Q}{Q^{\prime}} \pi\left(\eta \frac{Q}{Q^{2}}\right)\right] \eta^{n} e^{-\eta y Q} d n=0, \quad 0<y<\infty \tag{35}
\end{equation*}
$$

Since the Laplace transform is uniquely invertible, this requires that for all choices of $\left\{2, \zeta, \zeta^{\prime}\right\}$ we must have, setting $a \equiv Q / Q$,

$$
\begin{equation*}
\pi(\eta)=a \pi(a \eta), \quad 0<\eta<\infty \tag{36}
\end{equation*}
$$

But this is the same functional equation that was deduced earlier from the transformation group that expresses "complete ignorance" of a scale parameter. To complete the proof, note that from (6), if $\zeta^{\prime}<\zeta$, Eq. (36) must hold in the continuous range ( $1 \leq \mathrm{a} \leq \mathrm{c}$ ), and so the only possibility is, to within a constant factor,

$$
\begin{equation*}
\pi(n)=n^{-1} . \tag{37}
\end{equation*}
$$

This argument shows that no $\pi(n)$ other than (37) can satisfy (33). Conversely, on substitution we see that (33) is indeed satisfied for all $\{y, z, \zeta\}$, with $y \lambda(y, z)=1$. Again, we note several things:
(A) This argument made no use of the separation property (1). The solution (37) implies this as a necessary, if obvious, condition for agreement of $B_{1}$ and $B_{2}$.
(B) The problem turned out to be well-posed; there is one unique prior $\pi(n)$ that is "completely uninformative about $\zeta$," and it is just the one that Jeffreys anticipated, on partly intuitive grounds, some forty years ago (as the prior representing "complete ignorance" of a parameter known to be positive). It follows also from the fact that $\eta$ is a scale parameter, by some transformation group methods (for example, Jaynes, 1968; one of several quite different approaches all called "the transformation group method" or "the group invariance principle," although they utilize different groups which operate in different spaces, are chosen by different criteria, and yield different results. For further comments, see Appendix A).
(C) But the prior (37) is now derived in a way that is completely independent of anybody's intuition or any additional desiderata such as entropy, group invariance, or Fisher Information. Given the sampling distribution (31), the result (37) follows by straightforward mathematical steps. [Indeed, on sufficiently fine analysis, it will be seen that the only elements of probability theory used in the transition from (31) to (37) are the product rule $p(A B \mid C)=p(A \mid B C) p(B \mid C)$, and the sum rule $p(A \mid B)+p(-A \mid B)=1]$.
(D) This, however, recalls the oft-quoted remark of Lindley (1971): "Why should one's knowledge, or ignorance, of a quantity depend on the experiment being used to determine it?" The answer, in our view, is that the prior distribution should, of course, be based on all the prior information available. But the role a parameter plays in a sampling distribution is always a part of that information. Indeed, that is the irreducible minimum information without which a problem of inference cannot be formulated. Often, in pedagogical examples, it is the only prior information at hand, because (as in all the DSZ examples) the person formulating the problem simply neglects to provide any more. In this case--and only in this case--the prior distribution is, necessarily, determined (not necessarily uniquely) by the sampling distribution. But this is just the case we are solving by (37).
(E) In a real problem, a parameter will be, in general, "a physically meaningful quantity about which we know something." But for the mechanics of incorporating that something into our informative prior there are, to the best of the writer's knowledge, only two known principles: Bayes' theorem and maximum entropy; and both of these still require an ignorance pre-prior like (37) as their starting-point (Jaynes, 1968).

Therefore, for any problem of inference we see no way to avoid the notion of "complete ignorance," any more than we could avoid the concept of zero in arithmetic. Nor should we wish to avoid it; for clearly, to ask, "What is our state of knowledge after receiving information I?" cannot have any definite answer until we specify: What was our state of knowledge before receiving I? And this holds with equal force whether we choose to classify I as part of the data, or part of the prior information (see, however, Appendix A for some further comments).
(F) In this example, $n$ was a scale parameter, the sampling distribution (31) having the functional form $p(y, z \mid \zeta, n)=y^{-1} g(z, \zeta ; y n)$. For any sampling distribution of this form [or equally well, $y^{-1} g(z, r ; y / n)$ ] one readily verifies that the Jeffreys prior $\pi(\eta) \sim \eta^{-1}$ satisfies (30), and $y \lambda(y, z)$ is then a constant. Whether this solution is unique depends, of course, on how $z, \zeta$ enter into the function $g$.

## 8. THE ONE-DIMENSIONAL CASE

With the insight gained from the DSZ Example 1, we are able to give a more general discussion of the case where $y$, n are one-dimensional. We started cautiously, asking only for a prior $\pi(n)$ that is uninformative about $\zeta$ within the context of a given model. We now see that for a scale parameter $\eta$, the Jeffreys prior is $\zeta$-uninformative for all models, and unique for one. But this is already enough to establish it as the only prior for a scale parameter that is "completely uninformative" without qualifications.

Since the location and scale parameter cases are equivalent by the transformation $\mu=\log \sigma$, it follows that the uniform prior d is similarly general and unique for a location parameter (but in this case the result is so intuitive that it had never been doubted anyway).

The analysis may be generalized in the following way [suggested to the writer by a remark of W. D. Fisher]. Consider any sampling distribution with the functional form

$$
\begin{equation*}
p(y z \mid n \zeta)=g[z, \zeta ; h(y, n)] \frac{\partial h}{\partial y} \tag{38}
\end{equation*}
$$

for which the property $p(z \mid n \zeta)=\dot{p}(z \mid \zeta)$ underlying marginalization theory follows at once. The integral equation (30) for an uninformative prior becomes

$$
\begin{equation*}
\int g(z, ; h) \frac{\partial h}{\partial y} \pi(n) d n=\lambda(y, z) \int g(z \zeta ; h) d h \tag{39}
\end{equation*}
$$

If this is to hold without further assumptions about the functional form of $g(z r ; h)$, it is necessary that $\lambda(y, z)=\lambda(y)$ be independent of $z$, and that

$$
\begin{equation*}
\frac{\partial h}{\partial y} \pi(n)=\lambda(y) \frac{\partial h}{\partial n} . \tag{40}
\end{equation*}
$$

But then, making the change of variables $(y, n) \rightarrow(\bar{y}, \bar{\eta})$ where

$$
\begin{align*}
& \bar{y} \equiv \exp \int \lambda(y) d y \\
& \bar{\eta} \equiv \exp \int \pi(\eta) d \eta \tag{41}
\end{align*}
$$

Eq. (40) reduces $h$ to a function of $(\bar{y} \bar{n})$ :

$$
\begin{equation*}
h(y, \eta)=\bar{h}(\bar{y} \bar{\eta}) \tag{42}
\end{equation*}
$$

and (38) assumes the functional form $p(\bar{y}, z \mid \bar{\eta}, \zeta)=\bar{y}^{-1} \bar{g}(z, \zeta ; \bar{y} \bar{\eta})$ of remark ( $F$ ) above, where $\bar{g}(z \zeta ; \alpha) \equiv g(z, \zeta ; \bar{h}(\alpha))$. Thus the class of functions $h(y, \eta)$ for which $\pi(n)$ and $\lambda(y)$ can be constructed as in (40) takes us back, to within the change of variables (41), to the scale parameter case.

For example, if

$$
h(y, \eta)=\tanh \sqrt{y^{n}+\eta^{m}-a} \quad, \quad 0<\eta<\infty
$$

we have at once from (40) that the uninformative prior is

$$
\pi(n)=n^{m-1}
$$

Likewise, if

$$
h(y, \eta)=f(y)[\tan \alpha \eta]^{3 / 2}, \quad 0<\alpha \eta<\frac{\pi}{2}
$$

the uninformative prior is

$$
\pi(n)=\csc (2 \alpha n)
$$

and if

$$
h(y, n)=\log \left[\frac{(n y-1)(n+y)}{n y}\right]
$$

the uninformative prior is

$$
\pi(n)=1+n^{-2}
$$

Now, although the result (40) is rather special in the class of all problems with one-dimensional $(y, n)$, it is easily seen to exhaust the possibilities of the DSZ group analysis for that class. They took the sampling distribution as [OSZ, Eq. (2.6)] $p(d y d z \mid n \zeta)=f(y z \mid n \zeta)_{\text {G }}(d y) d z$, where $\mu_{G}$ is "a fixed general measure element" and defined the group structure by [DSZ, Eq. (2.7)]:

$$
\begin{equation*}
f(y, z \mid \eta, \zeta)=f(g y, z \mid \bar{g} \eta, \zeta) \tag{43}
\end{equation*}
$$

where $g, \bar{g}$ are corresponding elements of the groups $G, \bar{G}$ mentioned in Sec. 2 above. Evidently, if $(y, n)$ are one-dimensional, (43) says only that we have the functional form [compare (38)]:

$$
\begin{equation*}
f(y z \mid n \zeta)=g[z, \zeta ; h(y, \eta)] \tag{44}
\end{equation*}
$$

the "combined action of the groups" signifying a kind of hydrodynamic flow in the $(y, \eta)$ plane, whose streamlines are the contours $h(y, \eta)=$ const. But just as our Eq. (40) cannot be satisfied for all functional forms of $h(y, \eta)$, so the group structure (43) restricts the form of $h(y, y)$ in (44).

The form of that restriction can be anticipated at once by the following argument. A continuous exact group of mappings of the real line onto itself is necessarily a one-parameter group [for in $y^{\prime}=g y$ with fixed $y$, each group element $g$ is represented by one and only one value of $y^{\prime}$; thus $y^{\prime}$ parameterizes the group]. But a one-parameter continuous group is isomorphic with the group of simple translations $\left(x^{\prime}=x+a\right)$. We infer that the group structure (43) must restrict us to problems that are equivalent, to within a change of variables, to the location/scale parameter case. Indeed, on following through the analysis (Hamermesh, 1962) we find that the condition imposed
on (44) by the group structure is just our Eq. (40); i.e., the functions denoted $h(y, n)$ in (38), (44) are identical.

The condition found here is the same as that given by Lindley (1958) for agreement of a Bayesian posterior with a fiducial distribution; such relations were noted also by Fraser (1961) and Villegas (1971).

Now we arrive at the really interesting question: What happens in the one-dimensional case if we try to go beyond the class of problems just discussed? Do we continue to find uninformative priors from (30) beyond those obtainable by group analysis; or do we come up against that threatening overdetermination? This opens up a wide class of new mathematical problems, interesting in their own right and of obvious importance for the future of Bayesian statistical theory. At the time of writing (January 1978) progress on them is far from complete, consisting mostly of isolated results.

The following example, due to C. L. Mallows, shows that further solutions do exist beyond those resulting from the group structure (43); and that the apparent overdetermination is not always real.

Let $y, z$ be non-negative integers, and

$$
p(y z \mid n \zeta) \propto \frac{\zeta^{z} \eta^{y}(1-\eta)^{z-y}}{y!(z-y)!}, \quad \begin{align*}
& 0 \leq \zeta, \eta<\infty  \tag{45}\\
& 0 \leq y \leq z
\end{align*} .
$$

Then the marginal sampling distributions are Poisson:

$$
\begin{equation*}
p(z \mid \zeta \eta)=p(z \mid \zeta)=e^{-\zeta} \frac{\zeta^{z}}{z!} \tag{46}
\end{equation*}
$$

independent of $n$, as required by marginalization theory and

$$
\begin{equation*}
p(y \mid \zeta, \eta)=e^{-\zeta \eta} \frac{(n \zeta)^{y}}{y!} \tag{47}
\end{equation*}
$$

depending on both parameters; thus seemingly leading to a nontrivial marginalization problem. This example lacks the group structure (43), since $y$ is discrete, n continuous. But we now find the peculiarity that

$$
\begin{equation*}
p(y \mid z, \zeta, \eta) \tag{48}
\end{equation*}
$$

is independent of $\zeta$, and as a consequence the integral equations (30) are satisfied trivially; all priors $\pi(n)$ are nullifying and uninformative about $\zeta$.

That the opposite behavior can also occur, is shown by Example 5 of DSZ. The concluding message of their Sec. 1 was that all is well as long as $B_{1}$ uses proper priors. Later, they consider the model:

$$
\begin{equation*}
\left.p(y z \mid n \zeta) \propto \int_{0}^{\infty} t^{2 n-1} \exp \left\{-\frac{1}{2}\left[t^{2}+n(z t-\zeta)^{2}+n(y t-n)\right)^{2}\right]\right\} d t \tag{49}
\end{equation*}
$$

and note that, if $y=0$, the posterior distributions of $B_{1}$ and $B_{2}$ are

$$
\begin{align*}
& p\left(\zeta \mid z I_{1}\right) \propto \pi(\zeta) \int_{0}^{p^{\infty}} t^{2 n-1} \exp \left\{-\frac{1}{2}\left[t^{2}+n(z t-\zeta)^{2}\right]\right\} d t  \tag{50}\\
& p\left(\zeta \mid z I_{2}\right) \propto \pi(\zeta) \int_{0}^{\infty} t^{2 n-2} \exp \left\{-\frac{1}{2}\left[t^{2}+n(z t-\zeta)^{2}\right]\right\} d t \tag{51}
\end{align*}
$$

But if $z>0$, the ratio of the integrals is (by a Schwarz inequality) a monotonic increasing function of $\zeta$; and so $B_{1}$ and $B_{2}$ cannot agree unless they assign a singular prior $\pi(\zeta)=\delta\left(\zeta-\zeta_{0}\right)$, in which case their posterior distribution is independent of the data.

DSZ (Appendix 2) term this situation, "The Inevitable Paradox of Example 5." It is, perhaps, even more inevitable and more paradoxical than they intended; for it is clear from (49) that this situation arises for all priors $\pi(n)$, proper or improper! What, then, are we to make of their proof in Sec. 1, that this discrepancy "could not have arisen if $B_{1}$ had employed proper prior distributions"?

Passing over this query, the DSZ Example 5 is particularly instructive, just because at first glance the trouble appears so acute. The only nullifying prior is the uniform one $\pi(\pi)=$ const.; and it leads us back to (50) for all $y$. Surely, we have now run up against that overdetemination;
it is simply a mathematical fact that there is no prior $\pi(n)$ that can leave $B_{1}$ and $B_{2}$ in agreement for all data sets $(y, z)$ and all priors $\pi(\zeta)$.

Yet we would argue that there is still no real paradox here. This situation should not be disconcerting to anyone who has noted, in other Bayesian problems, that the effective sample number $n$ often drops by one unit when we integrate out an unwanted parameter; or who, in using the Chi-squared test, has reduced the number of degrees of freedom by one unit to take account of a parameter estimated from the data.

In fact, the explanation was noted in our Sec. 3 above; the mere qualitative fact of the existence of the components ( $n, y$ ); i.e., the knowledge that other parameters are present in our model beyond those of interest--already constitutes prior information relevant to $B_{1}$ 's inferences, that $B_{2}$ is ignoring. For further discussion, see Sec. 11 below.

These examples demonstrate that two opposite extremes of behavior are possible; presumably, many or all of the conceivable intermediate cases are also possible. It is evident that a great deal more insight into the content of the integral equations (30) will be needed before any overall understanding of marginalization and its implications for Bayesian theory can be reached. In the writer's judgment, the remaining space available here is best used, not in communicating a mass of further isolated results like the above (which the reader can easily invent for himself), but by giving a preliminary survey of a more general attack on the structure of those integral equations, not restricted to the one-dimensional case. But before turning to that, we note some further pertinent clues from the DSZ examples with higher dimensionality.
9. HIGHER DIMENSIONALITY

It appears from the foregoing that the case of a single location or scale parameter-or one that can be reduced to this by a change of variables--is disposed of once and for all; the only remaining function of the integral equations (30) is to determine whether, in a given model, the result is unique. Mathematically, this is the question whether the kernel of the integral equation is complete.

If the parameter $n$ is two-valued, comprising both a location and scale parameter; i.e., if $n=(\mu, \sigma)$ and the corresponding data $y$ can be separated into two components $y=(u, s)$ such that the sampling distribution has the form

$$
\begin{equation*}
p(z u s \mid \zeta \xi \sigma)=s^{-2} g\left(z, \zeta ; \frac{u-\mu}{\sigma} ; \frac{s}{\sigma}\right) \tag{52}
\end{equation*}
$$

then we can verify that the element of prior probability

$$
\begin{equation*}
\pi(\mu, \sigma) d \mu d \sigma=\frac{d \mu d \sigma}{\sigma} \tag{53}
\end{equation*}
$$

will satisfy (30) with $s \lambda(s, u, z)$ a constant. Clearly, then, whether or not (53) is uniquely determined by (30), no disagreement of $B_{1}$ and $B_{2}$ can arise from its use. Yet DSZ produce apparent counter-examples, in which a prior of the form (53) does lead to disagreement! The DSZ paradoxes must, then, have been in part illusory. In the following examples we will see just how this has come about.

Example 2. Here we appear to be in the aforementioned difficulty, for DSZ note that the "paradox" (i.e., disagreement of $B_{1}$ and $B_{2}$ ) does not disappear for the "widely recommended prior" $d \mu_{1} d \mu_{2} d \sigma / \sigma$; but it does for $d \mu_{1} d \mu_{2} d \sigma / \sigma^{2}$ for which "no recommendations appear to exist." Of course, in a problem with two parameters the prior $d \mu d \sigma / \sigma$ is indeed widely--and as we have just seen, justifiably--recommended; but that is a very different problem. In Appendix A we discuss the present problem from the standpoint of the transformation group method recommended by the writer (Jaynes, 1968) and show that either result may be obtained depending on further details of the "real-life" situation which are not conveyed by the mere words "location parameter" or "scale parameter".

Our sampling distribution is, in the notation of Eqs. (9)-(18),

$$
\begin{equation*}
p(u s z \mid \mu \sigma \zeta)=A \frac{s^{v}}{\sigma^{v+2}} \exp \left[-\left(\frac{u-u}{\sigma}\right)^{2}-R(z, \zeta, s / \sigma)\right] \ldots \tag{54}
\end{equation*}
$$

Note particularly that from (14), $\mu=\frac{1}{2}\left(\mu_{1}+\mu_{2}\right)$. Since (54) has the form (52), the prior $d \mu d \sigma / \sigma$ must be a solution of (30). To see this directly, and to see whether the result is unique, we can write (30), using (12), in the form

$$
\begin{equation*}
\int_{0}^{\infty} \omega^{v} e^{-R}[f(u, \sigma)-s \lambda(u, s, z)] d \omega=0 \quad 0<s<\infty ~-\infty<u, z, \zeta<\infty ~ 200-\infty=0 \tag{55}
\end{equation*}
$$

where $\lambda(u s z)=p\left(u s \mid z I_{1}\right), f(u, \sigma)$ is given by (16), and in the integration over $\omega=s / \sigma, s$ is held constant.

But (55) is an integral equation with complete kernel, since $e^{-R}$ is the generating function for a complete set of (Hermite) functions:

$$
\begin{equation*}
e^{-R}=e^{-\frac{1}{2} \omega^{2}\left(\nu+z^{2}\right)} \sum_{n=0}^{\infty} H_{n}\left(\frac{\omega z}{\sqrt{2}}\right) \frac{(\tau / \sqrt{2})^{n}}{n!} . \tag{56}
\end{equation*}
$$

Substituting this into (55), it is apparent that each term of the surmand must vanish separately. A function orthogonal to a complete set must vanish almost everywhere, and so the necessary and sufficient condition (NASC) for an uninformative prior reduces to

$$
f(u, \sigma)=s \lambda(u, s, z), \quad 0<s, \sigma<\infty
$$

from which we infer that $f(u, \sigma)$ is independent of $\sigma$, and the undetermined function

$$
\begin{equation*}
g(u) \equiv s \lambda(u, s, z) \tag{58}
\end{equation*}
$$

is independent of $s, z$. Using (16), the NASC is then

$$
\begin{equation*}
\frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} d \mu e^{-\left(\frac{\mu-u}{\sigma}\right)^{2}} \pi(\mu, \sigma)=g(u), \quad 0<\sigma<\infty \tag{59}
\end{equation*}
$$

Evidently, for any $\pi(\mu, \sigma)$ that could be taken seriously as a prior, the integral (59) converges so well that $g(u)$ must be an entire function. But then appealing again to completeness and generating function relations of the form (56), the most general function satisfying (59) is

$$
\begin{equation*}
\pi(\mu, \sigma)=\sum_{n=0}^{\infty} a_{n} \sigma^{n-1} H_{n}\left(\frac{\mu}{\sigma}\right) \tag{60}
\end{equation*}
$$

where $a_{n}$ are arbitrary constants, and $H_{n}$ are the Hermite polynomials. We then find $g(u)=\sum a_{n}(2 u)^{n}$. Conversely, on substituting (60) back into (15), we find that $B_{1}$ 's posterior distribution reduces to $B_{2}$ 's, all the arbitrary constants $a_{n}$ cancelling out upon nomalization.

Of course, not all functions of the form (60) satisfy the further requirement $\pi(\mu, \sigma) \geq 0$; but (60) includes many non-negative priors. For example, if $\omega(q)$ is any non-negative function with moments of all orders, the choice

$$
\begin{equation*}
a_{n}=\frac{1}{n!} \int_{-\infty}^{\infty} \omega(q) q^{n} d q \tag{61}
\end{equation*}
$$

leads to a non-negative prior

$$
\begin{equation*}
\pi(\mu, \sigma)=\sigma^{-1} \int d q \omega(q) \exp \left(2 q \mu-q^{2} \sigma^{2}\right) \tag{62}
\end{equation*}
$$

for which $B_{1}$ and $B_{2}$ will be in agreement. As a special case, if $\omega(q)$ goes into a delta-function $\delta(q-t)$ we get $a_{n}=t^{n} / n!$ which in turn yields the anticipated Jeffreys prior $d \mu d \sigma / \sigma$ in the special case $t=0$.

Also in this example, then, our early fears for the poverty of overdetermination disappear in an embarrassment of riches; from a mathematical standpoint, the problem is grossly underdetermined. Nevertheless, out of the many different solutions of (59) the Jeffreys prior $\pi(\mu, \sigma) \sim \sigma^{-1}$ still appears to hold a favored position. Out of the class of solutions (62) it is the only one that does not become exponentially large as $|\mu| \rightarrow \infty$. We conjecture that some further restriction on the allowable behavior at infinity [ for example that $\pi(\mu, \sigma)$ shall be at most $O\left(|\mu|^{N}\right)$ for some $N<\infty$ ] may lead, after all, to the Jeffreys prior as the unique solution.

Example 3. We have $n$ independent observations of a bivariate ( $x_{1}, x_{2}$ ) with model structure

$$
\begin{equation*}
x_{1}=\sigma_{1} e_{1} \quad, \quad x_{2}=\gamma x_{1}+\sigma_{2} e_{2} \tag{63}
\end{equation*}
$$

where $e_{1}, e_{2}$ are independent and $N(0,1)$. We require inference about the correlation coefficient $\zeta=\gamma \sigma_{1} /\left(\gamma^{2} \sigma^{2}+\sigma_{2}^{2}\right)^{\frac{1}{2}}$. The prior that avoids the paradox should then express complete ignorance about those components of
the parameter space that can be varied with $\zeta$ held constant. DSZ note that the "recommended" prior

$$
\begin{equation*}
d \gamma \frac{d \mu_{1}}{\sigma_{1}} \frac{d \mu_{2}}{\sigma_{2}} \tag{64}
\end{equation*}
$$

yields a posterior distribution identical with Fraser's structural distribution; but that the marginalization paradox is still present.

However, from the standpoint of the writer's transformation group method, the difficulty with (64) is obvious. For the model equation (63) is written in such a way that the parameter $\gamma$ is not decoupled [i.e., it gets entangled in the change of scale transfomations which express the fact that $\sigma_{1}, \sigma_{2}$ are scale parameters]; and so of course, it cannot be assigned an independent prior. If we rewrite (63) as

$$
\begin{equation*}
x_{1}=\sigma_{1} e_{1} \quad, \quad x_{2}=\sigma_{2}\left(e_{2}+\tau e_{1}\right) \tag{65}
\end{equation*}
$$

then $\tau \equiv \gamma \sigma_{1} / \sigma_{2}$ is decoupled, an arbitrary change of scale $c_{1}=a_{1} \sigma_{1}$, $\sigma_{2}^{\prime}=a_{2} \sigma_{2}$ inducing no change in $\tau$. But since the parameter of interest $\zeta$ is a function of $\tau$ [if $\tau=\tan \alpha$, then $\zeta=\sin \alpha$ ], the prior assigned to $\tau$ should not have anything to do with the paradox. Re-examining the equations of DSZ we find, as expected, that use of the prior

$$
\begin{equation*}
f(\tau) d \tau \frac{d \sigma_{1}}{\sigma_{2}} \frac{d \sigma_{2}}{\sigma_{2}} \tag{66}
\end{equation*}
$$

avoids the paradox, where $f(\tau)$ is an arbitrary function.
The same result can be reasoned out without introducing $\tau$. For in the model equation (63), $\gamma$ appears not as a location parameter, but as a scale parameter [note that the product or ratio of two scale parameters is still a scale parameter]. Complete ignorance of all three parameters should then be represented by a product of three Jeffreys priors. Sut again the prior assigned to the quantity of interest; should not matter;
so we should be able to insert an arbitrary function $g(\zeta)$ without disrupting the agreement of $B_{1}$ and $B_{2}$. Indeed, one can verify that the prior

$$
\begin{equation*}
g(\zeta) \frac{d y}{y} \frac{d \mu_{1}}{\sigma_{2}} \frac{d \mu_{2}}{\sigma_{2}} \tag{67}
\end{equation*}
$$

leads to agreement, and is equivalent to (66). The prior which DSZ noted as "avoiding the paradox" is a special case of (67), corresponding to $g(\zeta)=\zeta /\left(1-\zeta^{2}\right)^{\frac{1}{2}}$.

The joint likelihood function, which forms the kernel of the integral equations, can be read off from Eq. (1.8) of DSZ. However, to avoid cumbersome expressions we introduce the notation

$$
\begin{align*}
B & \equiv \log \frac{\sigma_{1}}{\sigma_{2}} \sqrt{1-\zeta^{2}}  \tag{68}\\
b & \equiv \log \sqrt{\frac{S_{11}}{S_{22}}}  \tag{69}\\
\omega & \equiv \frac{\sqrt{S_{11} S_{22}}}{\sigma_{1} \sigma_{2}} \tag{70}
\end{align*}
$$

where $S_{11}, S_{22}$ are the sample moments as defined by DSZ. The joint likelihood is then

$$
\begin{equation*}
L\left(\zeta, \sigma_{1}, \sigma_{2}\right)=\omega^{n} e^{-\omega T} \tag{71}
\end{equation*}
$$

where

$$
\begin{equation*}
T(z, b ; \zeta, \beta) \equiv \frac{\cosh (\beta-b)-z \zeta}{\sqrt{1-\zeta^{2}}} \tag{72}
\end{equation*}
$$

and $z \equiv S_{12} / \sqrt{S_{11} S_{22}}$ is the sample correlation coefficient, whose sampling distribution depends only on $\zeta$ [DS2, Eq. (1.10)]. The "unwanted" components of the parameter and sample spaces may then be taken as $n=\left(\sigma_{1}, \sigma_{2}\right)$; $y=\left(S_{11}, S_{22}\right)$; and the NASC that a prior $\pi\left(\sigma_{1}, \sigma_{2}\right)$ shall be completely
uninformative about $\zeta$ is

$$
\int_{0}^{\infty} d \omega \int_{-\infty}^{\infty} d B\left[\pi\left(\sigma_{1}, \sigma_{2}\right)-\omega \lambda\right] \omega^{n-2} e^{-\omega T}=0,\left\{\begin{align*}
-1 & <z, \zeta<1  \tag{73}\\
0 & <s_{11}, s_{22}<\infty \\
n & =2,3, \ldots
\end{align*}\right\}
$$

where $\lambda\left(z, S_{11}, S_{22}\right)$ is an undetermined function, $\left\{S_{11}, S_{22}, \zeta\right\}$ are held constant in the integrations over $\omega, \beta$.

Evidently, if the kernels $\omega^{n-2} \exp (-\omega T)$ are complete on the domain of integration we shall be led to the Jeffreys prior $\left(d \sigma_{1} / c_{1}\right)\left(d \sigma_{2} / \sigma_{2}\right)$ as the unique solution. We conjecture that this is the case; however we have not succeeded in finding a fully rigorous proof of this, or a counter-example. Therefore, in view of the writer's astonishment at discovering the nonuniqueness of (59) after long believing it unique but being unable to prove it, we leave this an open question which others may perhaps answer.

Example 4a. At this point in the DSZ narrative, the sense of paradox increases sharply; for they produce two versions of a problem that appear not only paradoxical, but unavoidably inconsistent with each other. We obtain the sample $\left\{x_{11}, x_{12}, \ldots x_{1 n}\right\}$ from $N\left(H_{1}, C\right)$ and $\left\{x_{21}, x_{22}, \ldots x_{2 n}\right\}$ from $N\left(\mu_{2}, \sigma\right)$. In version (1) $B_{1}$ is interested in inference about $\zeta \exists\left\{\zeta=\mu_{1} / \mathrm{c}\right.$, $\left.\zeta_{2}=\mu_{2} / \sigma\right\}$. The "unwanted" component is $n=\sigma$, and the corresponding data separation is in part $\left\{z_{i}=(n s)^{-1} \Sigma_{j} x_{i j}, i=1,2\right\}$; y was not specified. Using the class of priors

$$
\begin{equation*}
\sigma^{p} d \mu_{1} d \mu_{2} d \sigma \tag{74}
\end{equation*}
$$

DSZ show that $B_{1}$ and $B_{2}$ cannot agree unless $p=-3$.

But then in version (2) $\mathrm{B}_{2}$ "asserts his interest in $\zeta_{1}$ alone." Now $\zeta_{2}$ becomes part of the "unwanted" parameters: $\eta=\left\{\sigma, \mu_{2} / \sigma\right\}$, and the paradox is resurrected; $B_{1}$ and $B_{2}$ cannot agree unless $p=-2$. Not only do the two priors contradict the Jeffreys rule; they contradict each other!

In view of our earlier demonstrations, something must be very amiss; yet we can find no error in the DSZ calculations. So the resolution must be--and is--very much simpler. We have here a case of paradox by optical illusion.
$B_{1}$ and $B_{2}$ are free to partition the parameter space $S_{\theta}=S_{\zeta} \otimes S_{n}$ in any way they please; but having chosen any such partition, the mathematical problem is; what prior $\pi(n)$ in the space $S_{n}$, i.e. with $\zeta$ held constant, is uninformative about $\zeta$ ? The trouble was simply that, after choosing a partition, DSZ continued to write their prior (74) in terms of the old variables $\left(\mu_{1}, \mu_{2}, \sigma\right)$, thereby failing to make the condition ( $\zeta=$ const.). visible. Had DSZ transformed their priors to the new variables $\pi(\zeta) \pi(\eta)$ they would have found, in all these examples, that the "paradox" disappears just for the priors $\pi(n)$ recommended by Jeffreys. Far from suggesting any inconsistency in Bayesian principles, marginalization thus demonstrates again the power and basic soundess of the notions introduced into this field by Jeffreys some forty years ago.
10. SINGULAR SOLUTIONS: KNOWLEDGE IS IGNORANCE

In the DSZ example 3, the correlation coefficient was considered the quantity of interest, $\rho=\zeta$, and we found that the prior $\pi(\eta) d \eta=\left(d \sigma_{1} / \sigma_{1}\right)\left(d \sigma_{2} / \sigma_{1}\right)$ was completely uninformative about $\zeta$. Can we reverse our viewpoint, and find an uninformative prior $\pi(\rho) d \rho$ for the correlation coefficient? Most people, facing the problem of expressing ignorance of $\rho$, have chosen the form
$\pi(\rho) \sim\left(1-\rho^{2}\right)^{-k}$ more or less instinctively; but complete agreement on the value of $k$ still eludes us.

We would like to make the choice: $\left\{\zeta=\left(\sigma_{1}, \sigma_{2}\right), \eta=\rho\right\}$, and our method then requires that we find a separation of data $x=(y, z)$ for which $p(z \mid \zeta \eta)=p(z \mid \zeta)$. Perhaps this is possible, but our first guess: $\left\{y=\left(S_{11}, S_{22}\right) ; z=r=S_{12} /\left(S_{11} S_{22}\right)^{\frac{1}{2}}\right\}$ does not work. The joint sampling distribution of ( $\mathrm{S}_{11}, \mathrm{~S}_{22}$ ) still depends on $\rho$, containing as a factor the modified Bessel function

$$
I_{\frac{n}{2}-1}\left[\frac{\rho}{\sigma_{1} \sigma_{2}} \sqrt{\frac{s_{11} S_{22}}{1-\rho^{2}}}\right]
$$

However, the sampling distribution of $S_{11}$ depends only on $\sigma_{1}$; so let us marginalize using the choice: $\left\{\zeta=\sigma_{1}, \eta=\left(\sigma_{2}, \rho\right), z=S_{11}, y=\left(S_{22}, r\right)\right\}$. In view of what we found above, we shall perhaps be willing to take from the start $\pi(n)=\pi\left(\sigma_{2}, \rho\right)=\sigma_{2}^{-1} \pi(\rho)$. From Eq. (1.8) of DSZ, we are led to the integral equation

$$
\begin{align*}
\int_{-1}^{1} \pi(\rho) d \rho & \int_{0}^{\infty} \frac{d \sigma_{2}}{\sigma_{2}^{n+1}} \exp \left\{-\frac{1}{2}\left[\frac{S_{11}}{\left(1-\rho^{2}\right) \sigma_{1}^{2}}-\frac{2 \sigma_{12}}{\left(1-\rho^{2}\right)^{\frac{1}{2}} \sigma_{1} \sigma_{2}}+\frac{S_{22}}{\sigma_{2}^{2}}\right]\right\} \\
& =\lambda \exp \left(-\frac{S_{11}}{2 \sigma_{1}^{2}}\right) \tag{75}
\end{align*}
$$

where $\lambda$ must be independent of $\sigma_{1}$. For the class of samples: $\left\{S_{22}=2, S_{12}=0\right\}$, (75) collapses to

$$
\begin{equation*}
\left(\frac{n-2}{2}\right)!\int_{-1}^{1} \exp \left\{-\frac{\rho^{2} S_{11}}{2\left(1-\rho^{2}\right) \sigma_{1}^{2}}\right\} \pi(\rho) d \rho=\lambda\left(S_{11}\right) \tag{76}
\end{equation*}
$$

But this cannot be independent of $\sigma_{1}$ unless $\pi(\rho)$ is singular:

$$
\begin{equation*}
\pi(\rho)=\delta(\rho) \tag{77}
\end{equation*}
$$

i.e., the prior information must be that $\rho=0$ with certainty! Conversely, the prior (77) satisfies (75) for all samples.

On further reflection, we see that this result does, after all, make sense. $B_{2}$ is (in our reinterpretation) given data $\left\{x_{1} \ldots x_{n}\right\}$ whose sampling distribution depends only on $\sigma_{1}$; and uses it to make the standard Bayesian inference about $\sigma_{1} . B_{1}$ has in addition the other data components $\left\{y_{1} \ldots y_{n}\right\}$. But if $B_{1}$ also knows that $\rho=0$, then these additional data cannot help him to estimate $c_{1}$; uncorrelated normal distributions are independent. $B_{1}$ and $B_{2}$ will then agree, not because $B_{1}$ is totally ignorant of $\rho$, but for the opposite reason that his perfect knowledge of $\rho$ makes his extra data irrelevant.

To recognize this puts a new dimension into the marginalization game. A prior $\pi(n)$ that is uninformative about $\zeta$ does not necessarily express ignorance about $n$; it depends on the structure of the model. If $B_{1}$ did not know $\rho$, his extra data $\left\{y_{1} \ldots y_{n}\right\}$ would always be relevant and he would always revise $B_{2}$ 's conclusions about $\sigma_{1}$; there is no ignorance prior $\pi(0) \sim\left(1-\rho^{2}\right)^{-k}$ that can avoid this. But if $B_{1}$ had far greater knowledge, he might throw away the new data and accept $\mathrm{B}_{2}$ 's conclusions after all!

This is not paradoxical, but is a natural and necessary part of consistent plausible reasoning. We can see this phenomenon in generality already in Eq. (2). If for some particular value $\eta_{1}=\eta_{0}$ we should have

$$
\begin{equation*}
\frac{\partial}{\partial y} p\left(c \mid \eta_{0}, y, z, I_{1}\right)=0 \tag{78}
\end{equation*}
$$

then the singular prior $\pi\left(n \mid I_{1}\right)=\delta\left(n-\eta_{0}\right)$ will bring about agreement of $B_{1}$ and $B_{2}$ by making the data $y$ irrelevant. Whenever the property (78) exists, the integral equation will have singular solutions representing ignorance of $\zeta$ due to perfect knowledge of $\eta$.

Now, at long last, we have enough clues in hand to commence a general attack on the integral equations.
11. STRUCTURE OF THE INTEGRAL EQUATIONS

For any fixed data set $x=(y, z),(30)$ is an integral equation which we write, for suggestiveness, in the form

$$
\begin{equation*}
\int_{S_{\eta}} k(\zeta, \eta) \pi(\eta) d \eta=\lambda f(\zeta) \quad, \quad \zeta \varepsilon S_{\zeta} \tag{79}
\end{equation*}
$$

Already at this stage, it is possible to have "s-overdetermination". The set of all functions on $S_{\zeta}$ forms a Hilbert space $H_{\zeta}$. As $n$ ranges over $S_{\eta}$. the functions $K(\zeta, n)$ span a certain subspace $H_{\zeta}^{\prime}$ of $H_{\zeta}$. If $f(\zeta)$ does not lie in $H_{\zeta}^{\prime}$, there can be no solution of (79). In these cases, the rere qualitative fact of the existence of the components ( $7, y$ )--irrespective of their numerical values--already constitutes prior information relevant to $B_{1}$ 's inferences [because introducing them restricts the space of $B_{1}$ 's possible posterior distributions to $\left.\pi(\zeta) H_{L_{3}}^{\prime}\right]$. We saw an example in (69). In this case, the shrinkage of $H_{r}$ cannot be restored by any prior on $S_{n}$ and the integral equations (79) ask an ill-advised question. In the following we consider only the case where the problem is free from $\mathrm{overdetermination}$.

If we think of $\pi(n)$ as a vector in a Hilbert space $H$ of functions on $S_{n}$, then for each $\zeta$, Eq. (79) specifies the inner product of $7(n)$ with the function $K(\zeta, n)$. If as $\zeta$ varies over $S_{\zeta}$ these functions span the full space of $H$ then the kernel $K(\zeta, \eta)$ may be said to be "complete," and the function $\pi(n)$ is defined "uniquely"; i.e., almost everywhere.

On the other hand, if the functions $\left\{K(\zeta, n): \zeta_{\zeta} \zeta_{\zeta}\right\}$ are not complete on $S_{n}$, they span some subspace $H_{0} \varepsilon H$, and (79) detemines only the projection
$\pi_{0}(n)$ of $\pi(n)$ onto $H_{0}$; i.e., $\pi(n)=\pi_{0}(n)+\pi_{1}(n)$ where $\pi_{1}(n)$ is orthogonal to $\pi_{0}(n)$ but is otherwise undetermined. Since the coefficient $\lambda$ is at this stage arbitrary, $\pi_{0}(n)$ is determined to within a multiplicative constant.

But all this has referred to only one particular data set $x$. For every different data set we can have a different kernel

$$
\begin{equation*}
K_{x}(\zeta, \eta)=p(y z \mid \eta, \zeta) \tag{80}
\end{equation*}
$$

a different "driving force"

$$
\begin{equation*}
f_{x}(\zeta)=p(z \mid \zeta)=\int d y p(y z \mid n \zeta) \tag{81}
\end{equation*}
$$

and a different coefficient $\lambda_{x}$. The equations

$$
\begin{equation*}
\int_{S_{\eta}} K_{x}(\zeta, \eta) \pi(\eta) d \eta=\lambda_{x} f_{x}(\zeta) \quad, \quad \zeta \varepsilon S_{\zeta} \tag{82}
\end{equation*}
$$

will, for two different data sets $x, x^{\prime}$, determine the projections $\pi_{x}(n)$, $\pi_{x^{\prime}}(n)$ of $\pi(n)$ onto two different subspaces $H_{x^{\prime}}, H_{x^{\prime}}$ of $H$. If $H_{x}, H_{x^{\prime}}$ are disjoint, the two integral equations (82) determine no relation between these solutions; i.e., the arbitrary constants $C_{x}$ in $\left[\pi_{x}(n), \lambda_{x}\right]$ and $C_{x}$, $n_{n}\left[\pi_{x^{\prime}}(n), \lambda_{x^{\prime}}\right]$ may be specified independently. But if $H_{x}$ and $H_{x^{\prime}}$ are
sisjoint (i.e., they have a common linear manifold $M$ ), then there are several possibilities:

Case I. If M has dimensionality greater than one, the two integral equations for $x$ and $x^{\prime}$ may determine different (i.e., linearly independent) projections of $\pi(n)$ onto $M$. If these are both non-zero, then formally we can still escape overdetermination by setting $\lambda_{x}=\lambda_{x^{\prime}}=0$; and then hoping that some other data point $x^{\prime \prime}$ will allow $\lambda_{x^{\prime \prime}} \neq 0$. If one of the projections (say of $\pi_{x^{\prime}}$ ) vanishes, then we need set only $\lambda_{x}=0$. But in either case there will
be an embarrassing situation; since $\lambda_{x}$ has the meaning: $\lambda(y, z)=p\left(y \mid z I_{1}\right)$, we are escaping overdetermination only by assigning a prior $\pi(n)$ which says that the trouble-making data set $x=(y, z)$ is impossible!

One would be very reluctant to accept such a prior as "uninformative"; indeed, it would seem to be a rather obvious minimum requirement of any prior deserving of that name, that it should not exclude in advance any data set permitted by the sampling distribution $p(y, z \mid n \zeta)$. A fully acceptable solution ought to lead to $\lambda>0$ over the entire sample space. Case I thus represents a kind of moral--even if not formal mathematical-overdetermination. If it should occur for many pairs of data points, we could have also mathematical overdetermination, the only solution of (82) being $\lambda_{x} \equiv 0, \pi(\eta) \equiv 0$.

Case II. The two integral equations for $x, x^{\prime}$ agree that $\pi(n)$ is orthogonal to $M$. Then the situation is basically as if the subspaces $H_{x}, H_{x}$, were disjoint; i.e., no connection is established, and $\lambda_{x}, \lambda_{x^{\prime}}$ may still be specified independently. As far as $x, x$ ' are concerned, the "unused" manifold $M$ could be removed from the Hilbert space with no essential change in the problem (of course, if some other data point $x^{\prime \prime}$ should determine a non-zero projection onto $M$, we are back to Case I).

Case III. The two integral equations agree in assigning nonzero projections of $\pi(n)$ onto $M$, that are the same within a multiplicative constant. Then the existence of a single function $\pi(n)$ demands that these multiplicative constants be equal. A connection is thus established, so that, given $\lambda_{x}, \lambda_{x}$, is determined. This can happen whatever the dimensionality of.. If we can find a third data set $x^{\prime \prime}$ for which $\lambda_{x^{\prime}}$ and $\lambda_{x}$ " have common manifold, then $\lambda_{x}$ " is in turn determined by $\lambda_{x}$.

In this way, by a sequence of points $\left\{x \rightarrow x^{\prime} \rightarrow x^{\prime \prime} \rightarrow \ldots\right\}$ with overlapping manifolds the constants $\lambda_{x}$, originally arbitrary and independent at each point of the sample space, become tied together by the requirement of a single solution $\pi(n)$, into a function $\lambda(x)$ defined at many points. The existence or nonexistence of unique and "morally acceptable" noninformative priors then depends on whether by this process a single function $\lambda(x)>0$ can be set up over the entire sample space.

Let us call any sequence $\left\{x_{1}, x_{2}, x_{3}, \ldots\right\}$ such that $H_{x_{i}}$ and $H_{x_{i+1}}$ overlap, a continuation path $P$. Then for any two points $x, x^{\prime}$ that can be connected by a continuetion path, the ratio $\left[\lambda\left(x^{\prime}\right) / \lambda(x)\right]$ is determined by the integral equations ( 82 ). The process is somewhat analogous to analytic continuation [hut very different topologically; i.e., a sequence $\|_{x}, H_{x}, \ldots$ of overlapping manifolds does not in general corresnond to a continuous path in the sample space].

Case III is thus in turn comprised of three possibilities:
Case II a. "Nonintegrability." Two points $x, x^{\prime}$ can be connected by two different continuation paths $P_{1}, P_{2}$; but they yield different ratios $\left[\therefore\left(x^{\prime}\right) / \therefore(x)\right]_{1} \neq\left[\lambda\left(x^{\prime}\right) / \therefore(x)\right]_{2}$. Then there is no single-valued nonvanishing function $\lambda(x)$ and as in Case I the problem is morally--and, depending on how much of the sample space is infected with this disease, perhaps also mathematically-overdetermined. The avoidance of this case is analogous to a condition of integrability [but again, very different topologically!].

Case IIIb. "Intransitivity." The sample space $S_{x}$ can be decomposed into two subspaces $S_{x}^{(1)}, S_{x}^{(2)}$ in such a way that there is no continuation path from any point in $S_{x}^{(1)}$ to any point in $S_{x}^{(2)}$. Then no connection is established between ${ }^{(1)}(x)$ and $)^{(2)}(x)$; i.e., they can be assigned independent arbitrary
multiplicative constants. The problem is then underdetermined, and more than one "noninformative prior" exists. If there are $K$ disconnected subspaces $\left\{S_{X}^{(1)} \ldots S_{X}^{(K)}\right\}$, then the prior $\pi(M)$ determined by $(3 C)$ will contain $K$ arbitrary constants.

Case IIIc. "Integrable Transitivity." Any two points $x, x$ ' in the semple space can be connected by a continuation path, and if more than one such path exists, all paths assign the same ratio $\left[\lambda\left(x^{\prime}\right) / \lambda(x)\right]$. Then a singlevalued function $\lambda(x)>0$ exists over the entire sample space, and the equations (82) define one unique noninformative prior $-\left(r_{1}\right)$, to xithin a normalization constant.

Previous Bayesian thought (including the writer's) which simply took for granted the existence of unique noninformative priors, has thus in effect assumed that we always have Case Ille. But loolod at in this now way, it seems astonishing that such a thing could be true. If for zmy two points $x, x^{\prime}$ in our sample space we should have Case I or Case Illa, then it is all over with cur search for a "morally acceptable" mominfer ative prior. Yet we have the counter-gamples of DSZ where such solutions gookst. What, in the structure of the problem, prevents these cases from occurring?

For enlightenment let us turn back, still another time, to our faithful DSZ Example 1, which has never yet failed to give us an interesting and useful answer to any question we have put to it.
12. EXAMPLE 1 - A FOURTH LOOK

We have seen already, in Eq. (37), that the integral equations determine the Jeffreys prior $\pi\left(n_{i}\right)=n^{-1}$ uniquely now we want to eyaine in minute detail the mechanism by which this is acconplished. Intretuoing
the Laplace transform of $\eta^{n} \pi(\eta)$ :

$$
\begin{equation*}
F(a) \equiv \int_{0}^{0} \eta^{n} \pi(n) e^{-a n} d \eta \tag{83}
\end{equation*}
$$

the set of integral equations (33) becomes

$$
\begin{equation*}
F[y Q(z, \zeta)]=\frac{(n-1)!y \vdots(y, z)}{[y Q(z, \zeta)]^{n}}, \zeta=1,2, \ldots,(n-1) . \tag{84}
\end{equation*}
$$

For a fixed data set $x=(y, z)$ this determines the value of $F(a)$ to within a multiplicative factor, at $(n-1)$ discrete points $a_{\zeta}=y Q(z, \zeta)$. The set of points $\left\{a_{1}(y, z) \ldots a_{n-1}(y, z)\right\}$ will be called the spectrum of $x$. We can suppose without loss of generality that $c>1$. From (6), the $a_{i}$ are nonincreasing: $a_{1} \geq a_{2} \geq \ldots \geq a_{n-1}$, and all lie within a factor c of each otner; i.e.,

$$
\begin{equation*}
1 \leq a_{1} / a_{n-1} \leq c \tag{85}
\end{equation*}
$$

The subspace $H_{x}$ is the one spanned by the set of functions

$$
\begin{equation*}
a_{i}(n)=n^{n} e^{-a i^{n}}, \quad i=1,2, \ldots(n-1) \tag{86}
\end{equation*}
$$

linearly independent if the $a_{i}$ are all distinct.
Clearly, for $n>3$ we can in general find another data set $x^{\prime}=\left(y^{\prime}, z^{\prime}\right)$
such that

$$
\begin{align*}
& a_{1}(y, z)=a_{2}\left(y^{\prime}, z^{\prime}\right)  \tag{87a}\\
& a_{2}(y, z)=a_{3}\left(y^{\prime}, z^{\prime}\right) \tag{87b}
\end{align*}
$$

and the subspaces $H_{X}, H_{X}$ then have a two-dimensional linear manifold $M$ in common, consisting of all functions of the form

$$
\begin{equation*}
c(n)=c_{1} c_{1}\left(r_{i}\right)+c_{2} c_{2}(n) \tag{88}
\end{equation*}
$$

with arbitrary coefficients $\mathrm{C}_{1}, \mathrm{C}_{2}$.

Therefore unless both data sets $x, x^{\prime}$ detemine the same projection of $\pi(\eta)$ onto this manifold:

$$
\begin{equation*}
\frac{F\left(a_{1}\right)}{F\left(a_{2}\right)}=\frac{F\left(a_{2}^{\prime}\right)}{F\left(a_{3}^{\prime}\right)} \tag{62}
\end{equation*}
$$

we shall have Case I, and the problem will be morally overdetermined. iori from the data set $x$ we have

$$
\begin{equation*}
\frac{F\left(a_{1}\right)}{F\left(a_{2}\right)}=\left[\frac{Q\left(z, \zeta_{1}\right)}{O\left(z, \zeta_{2}\right)}\right]^{n} \tag{90}
\end{equation*}
$$

and from $x^{\prime}=\left(y^{\prime} z^{\prime}\right)$

$$
\begin{equation*}
\frac{F\left(a_{2}^{\prime}\right)}{F\left(a_{3}^{\prime}\right)}=\left[\frac{Q\left(z^{\prime}, c_{2}^{\prime}\right)}{Q\left(z^{\prime}, \zeta_{3}^{\prime}\right)}\right]^{n} . \tag{91}
\end{equation*}
$$

But (87) is, more explicitly,

$$
\begin{align*}
& \mathrm{yQ}\left(z, r_{1}\right)=y^{\prime}\left(1\left(z^{\prime}, r_{2}^{\prime}\right)\right.  \tag{92c}\\
& \mathrm{yQ}\left(z, r_{2}\right)=y^{\prime} Q\left(z^{\prime}, r_{3}^{\prime}\right) \tag{925}
\end{align*}
$$

from which we see that (90) and (91) are indeed equal. We have escaped overdetermination only because of the connection (87) required to produce a common linear manifold.

Likewise, we could have a three-dimensional common manifold by adding to (87) the condition

$$
\begin{equation*}
a_{3}(y, z)=a_{4}\left(y^{\prime}, z^{\prime}\right) \tag{93}
\end{equation*}
$$

which is generally possible if $n>4$. But again the three conditions (Ela), (87b), (93) are just sufficient to bring about equality of the three retios $F\left(a_{j}\right) / F\left(a_{j}\right)$; and so on. We continue to have Case IIIc.

We see now how different this problem is from the usual theory of integral equations with complete kernel. It is just the very great incompleteness of our kernel $K(\zeta, n)$ that, so to speak, creates room for agreement so that all the integral equations (82) can be satisfied simultaneously. Because of this incompleteness the subspaces $H_{x}$ are so small, and scattered about so widely in the full Hilbert space $H$ like stars in the sky, that it requires a very special relation between $x, x^{\prime}$ to bring about any overlapping manifold at all.

But it still seems magical that the relation required to produce overlapping should also be just the one that brings about agreement in the projections. So we still have not found the real key to understanding how Case I is avoided.

Since there is a unique solution (37), a single-valued function $\lambda_{x}>0$ must have been determined over the sample space $S_{x}$. Evidently, then, our integral equations must be transitive on $S_{x}$; i.e., there must exist a continuation path connecting any two points $x, x^{\prime}$. What are these paths? Are there more than one for given $x, x^{\prime}$ ? If so, how was nonintegrability (Case Illa) avoided?

We suppose the spectra $\left\{a_{1}, a_{2}, \ldots, a_{n-1}\right\},\left\{a_{1}^{\prime}, a_{2}^{\prime}, \ldots, a_{n-1}^{\prime}\right\}$ of $x, x^{\prime}$ to have no point in common (otherwise $H_{x}$, $H_{x^{\prime}}$, have already a common manifold $M$ and there is no need for a continuation path). If any point $\mathrm{a}_{\mathrm{i}}$ is within a factor $c$ of some point $a_{j}^{\prime}$ we define a new data point $x^{\prime \prime}=\left(y^{\prime \prime}, z^{\prime \prime}\right)$ by

$$
\begin{equation*}
y^{\prime \prime}=\frac{c a_{j}^{\prime}-a_{i}}{c-1}, \quad z_{2}^{\prime \prime}=\frac{a_{i}-a_{j}^{\prime}}{c a_{j}-a_{i}} \tag{94}
\end{equation*}
$$

and $z_{3}^{\prime \prime}=z_{4}^{\prime \prime}=\ldots=z_{n}^{\prime \prime}=0$. Then the first two points of the spectrum of $x^{\prime \prime}$ are, from (6),

$$
\begin{equation*}
a_{1}^{\prime \prime}=a_{i}, \quad a_{2}^{\prime \prime}=a_{j}^{\prime} \tag{95}
\end{equation*}
$$

and $x \rightarrow x^{\prime \prime} \rightarrow x^{\prime}$ is a continuation path. If the spectra of $x, x^{\prime}$ are more widely separated (i.e., if $c^{k-1}<a_{n-1} / a_{1}^{\prime \prime}<c^{k}$ ), then [because of the restriction (85) on the spectrum of any one point $x^{\prime \prime}$ ] it will require a continuation path with at least $k$ intermediate points to connect them; but this can always be done by repetition of the above process. The reason for the transitivity is thus clear.

Now, how does this determine the function $\lambda(y, z)$ ? Writing the family of integral equations (33) as

$$
\begin{equation*}
G(a) \equiv \int_{0}^{\infty} d \eta \pi(n)(n Q)^{n} e^{-v Q}=(n-1)!y \lambda(y, z) \tag{96}
\end{equation*}
$$

for any given data point $x$, the necessary and sufficient condition that $-(n)$ be uninformative about $\zeta$ was that the integral in (95) take on equal values at $(n-1)$ discrete values of $\zeta$, or $G\left(a_{1}\right)=G\left(a_{2}\right)=\ldots=G\left(a_{n-1}\right)$. Introducing new data points $x^{\prime}, x^{\prime \prime}, \ldots$ connected by continuation paths, this equality is extended to further values $\mathrm{a}^{\prime}, \mathrm{a}^{\prime \prime}, \ldots$. Now $G(\mathrm{a})$ is a continuous function. As we continue to all points of the sample space $S_{x}$, if the set of spectral points $\mathrm{a}^{\prime}$ where $G\left(\mathrm{a}^{\prime}\right)=G\left(\mathrm{a}_{1}\right)$ becomes everywhere dense on $0<\mathrm{a}^{\prime}<\infty$, then $G(a)=$ const. is the only possibility. Equation (96) then reads:

$$
\begin{equation*}
\int_{0}^{\infty} d \eta \pi(\eta) \eta^{n} e^{-\eta a}=(\text { const }) \times a^{-n}, \quad 0<a<\infty \tag{97}
\end{equation*}
$$

and on inverting the Laplace transform we have again the unique solution (41). On setting $\pi(\eta)=\eta^{-1}$, (97) reduces to

$$
\begin{equation*}
\lambda(y, z)=y^{-1}>0 \tag{98}
\end{equation*}
$$

Our questions have now been answered. Uniqueness of the solution requires that the set of spectral points $a^{\prime}$ be everywhere dense on the fositive real line; and nonintegrability was avoided because extension of $\lambda_{x}$ along any continuation path connecting two points took the eminently satisfactory
form that a function of ( $x, \zeta$ ) was a constant. So, by study of Example 1 we see how all the conditions can be met, leading to the Case III most pleasing to a Bayesian.

The structure thus revealed will, of course, generalize readily to other problems. But our story has already grown too long, and the next Chapter must be told elsewhere.
13. CONCLUSION

While the full implications of marginalization for Bayesian statistical theory are still far from explored, the analysis given here represents at least the necessary beginnings. However, in research of this type, more than half the game usually lies in the slow process of recognizing the existence of an important solvable problem, and learning how to reduce vague conceptual questions to definite, clearly formulated mathematical ones. After that, further progress to the limit of our mathematical capabilities generally comes rapidly.

Viewed in this way, one is encouraged to think that the slow initial stages are now over, and we may hope to see major advances in the determination of prior probabilities by logical analysis, in the near future.

The integral equations introduced here may or may not prove to be more widely useful, in practice, than previous desiderata for uninformative priors. At present, they seem to have at least the advantage of being general and noncontroversial; i.e., they express only the universally accepted principles of probability theory, making no use of intuitive ideas (symmetry, entropy, indifference, group invariance, "letting the data speak for themselves", etc.) which appeal differently to different people. Of course, with full understanding, those integral equations may
in time be seen as stepping-stones to a still more appropriate and useful method, as yet unimagined.

The most encouraging sign of all is simply that, at last, the first prerequisite for progress in Bayesian theory is now an accomplished fact. The blind alleys have been tracked to their ends, and after decades of neglect and worse--even from some who professed to be Bayesians--the program started by Jeffreys is recognized as the true road to progress. Mathematical problems that might have been solved by Wald or Fisher in 1940 are, at last, being taken seriously and actually worked on.

At present, the crucial problem before us is: What is the necessarv and sufficient condition on the functional form of $p(y, z \mid n, \zeta)$ for the integral equations (30) to possess nontrivial and "morally acceptable" solutions? Our analysis in Sec. 11 above does not yet answer this; only the future will tell how close it has come to that goal.
14. APPENDIX A - COMMENTS ON GROUP ANALYSIS

The explicit mathematical use of group invariance as a criterion for assigning probability distributions goes back to Poincare (1912), although of course the intuitive recognition of symmetry in gambling devices was present from the very beginnings (Cardano and Pascal). It appears to the writer that, in the final analysis, all applications of probability theory are based necessarily on such considerations, however much those motivations have been disavowed.

Since the term "group analysis" has several different meanings, we try here to indicate how they are related to each other and to the general problem of inference.

In the group structure (43) considered by DSZ the sampling distribution is invariant under two groups $G, \bar{G}$ operating simultaneously on the sample space and the parameter space. The status of that approach can be seen as follows: (A) Whatever group structure of this kind a problem may possess, is determined by the functional form of the sampling distribution. (B) Ergo, whatever results may be deduced from that group structure, must also be deducible directly from the functional form. (C) Since the group analysis cannot be more general than a "functional form" analysis--and is easily seen to be less general--the question of method reduces to whether, in a problem where it is applicable, the group analysis leads to a more efficient calculation, or a better intuitive understanding, of the result. It seems clear that group analysis does accomplish both; and often brilliantly. Therefore, by all means, let us take advantage of the DSZ group analysis whenever we can. (D) Nevertheless, whether or not any group structure exists, the necessary and sufficient condition for agreement of $B_{1}$ and $B_{2}$ is always the set of integral equations (30). For a general understanding of marginalization, then, it appears that we should appeal to the integral equations rather than the group structure.

Now an entirely different kind of group analysis (Jaynes, 1968;1971;1976) has also been proposed and illustrated in several applications. Since I believe it to be closer to the spirit of what one means intuitively by "ignorance", and also more widely applicable mathematically, let us look at it in the context of the DSZ Example 2 [Eqs. (54)-(62) above].

What prior probability element $\pi\left(\mu_{1} \mu_{2} \sigma\right) d \mu_{1} d \mu_{2} d \sigma$ expresses "complete ignorance" of two location parameters associated with a common scale parameter? We have a sampling distribution of the form

$$
\begin{equation*}
p\left(d x d y \mid \mu_{1} \mu_{2} \sigma\right)=h\left(\frac{x-\mu_{1}}{\sigma} ; \frac{y-\mu_{2}}{\sigma}\right) \frac{d x}{\sigma} \frac{d y}{\sigma} \tag{A.1}
\end{equation*}
$$

and we consider
Problem 1: Given the data $D \equiv\left\{\left(x_{1}, y_{1}\right) ;\left(x_{2}, y_{2}\right), \ldots\left(x_{n}, y_{n}\right)\right\}$, estimate $\left(\mu_{1}, \mu_{2}, \sigma\right)$.
Complete initial ignorance means, intuitively, that having no other basis for inference, our estimates are obliged to follow the data; i.e., a noninformative prior is the means by which one achieves Fisher's goal of letting the data speak for themselves. As noted in the text, it is also the necessary starting point for construction of an informative prior.

Of course, a mere verbal statement such as "complete initial ignorance" is too vague to determine any mathematically well-posed problem. However, there is a rather obvious and basic desideratum of consistency: In two problems where we have the same prior information we should assign the same prior probabilities. Surely, any method for assigning priors which was found to violate this requirement would be rejected as self-contradictory.

Yet, as noted before (Jaynes, 1963), in many cases this desideratum is already sufficient to determine a unique solution. For, given the above Problem 1, we can carry out a transfomation of all variables: $\left\{x_{\mathrm{j}}, y_{\mathrm{j}}, \mu_{1} \mu_{2}^{(\mathrm{T})} \rightarrow\left\{x_{\mathrm{j}}^{\prime} y_{\mathrm{i}}^{\prime} \mu_{1}^{\prime} \mu_{2}^{\prime} \sigma^{\prime}\right\}\right.$ which involves a mapping $0 \rightarrow 0^{\prime}$ of the parameter space onto itself, and consider:

Problen 2: Given the data $D^{\prime}$, estimate $\left(\mu_{1}^{\prime}, \mu_{2}^{\prime}, \sigma^{\prime}\right)$. Any proposed prior $f\left(\mu_{1} \mu_{2} \sigma\right) d \mu_{1} d \mu_{2} d \sigma$ will be transformed into $g\left(\mu_{1}^{\prime} \mu_{2}^{\prime} \sigma\right) d \mu_{1}^{\prime} d \mu_{2}^{\prime} d \sigma^{\prime}$ according to the Jacobian of the transformation:

$$
\begin{equation*}
g\left(\mu_{1}^{\prime} \mu_{2}^{\prime} \sigma^{\prime}\right)=J^{-1} f\left(\mu_{1} \mu_{2} \sigma\right) \tag{A.2}
\end{equation*}
$$

where $J\left(n_{1} \nu_{2} \sigma\right)=a\left(\mu_{1}^{\prime} \mu_{2}^{\prime} \sigma^{\prime}\right) / \partial\left(\mu_{1} \mu_{2} \sigma\right)$; and of course the transformation rule (A.2) will hold whatever the function $f\left(\mu_{1} \mu_{2} \sigma\right)$. But now the transformation may be such that we recognize Problems 1 and 2 as entirely equivalent problems; i.e., they have the same sampling distribution and if initially we were "completely ignorant" of ( $\mu_{1} \mu_{2} \sigma$ ) in Problem 1-whatever that means--we are at least in the same state of knowledge about ( $\mu_{1}^{\prime} \mu_{2}^{\prime}{ }^{\prime}$ ) in Problem 2. But our desideratum of consistency then demands that $f$ and $g$ must be the same function; i.e., the prior representing complete ignorance must satisfy the functional equation

$$
\begin{equation*}
f\left(\mu_{1}^{\prime} \mu_{2}^{\prime} \sigma^{\prime}\right)=J^{-1} f\left(\mu_{1} \mu_{2} \sigma\right) \tag{A.3}
\end{equation*}
$$

which determines the ratio of prior density at any two points $\theta, \theta^{\prime}$ of the parameter space that are connected by the mapping.

If then the mapping $0 \rightarrow 0^{\prime}$ is one of a group of transformations that is transitive on the parameter space (i.e., from any point $\theta$ any other point $\theta^{\prime}$ can be reached by some transformation of the group), then (A.3) determines the prior, to within a multiplicative constant, everywhere.

Note that, in this method the prior is determined by the Jacobian of the transformation on the parameter space; and this remains true whether the group is Abelian or non-Abelian, compact or non-compact. Therefore, considerations of right Har razsure or left Haar measure do not arise. Haar measure is defind on the group manifolds and mot on our paranoter space.

Furthermore, this method is more general; for if by any means we can recognize the group on the parameter space that transforms our prior state of knowledge into an equivalent one, the same result (A.3) will follow whether there is or is not an image group on the sample space. Thus, the Mallows example (45) has no group structure of the DSZ type; yet there is a natural group induced on $S_{\eta}$ by Bayes' theorem (Jaynes, 1968) which leads to the uninformative prior $\pi(n) \propto[n(1-n)]^{-1}$; and let me acknowledge [correcting an erroneous statement in Jaynes (1968)] that, unknown to me at the time, this result, too, had been anticipated by Jeffreys.

This will perhaps make clearer the distinction between our method and other group invariance arguments which do not appear to be motivated by the desideratum of consistency; or at least, to the best of the writer's knowledge, do not explicitly invoke it.

In this method a noninformative prior is not in general determined merely by the form of the sampling distribution; it is determined by specifying the invariance group on the parameter space. Furthermore, even if we do choose a group by the form of the sampling distribution, a given sampling distribution may be invariant under more than one group.

For the sampling distribution (A.1) perhaps the simplest transformation group is given by

$$
\begin{align*}
\sigma^{\prime} \mu_{1}^{\prime} & =a \sigma & 0 & <a<\infty \\
\mu_{1}^{\prime} & =\mu_{1}+b_{1} & -\infty<b_{1} & <\infty  \tag{A.4}\\
\mu_{2}^{\prime} & =\mu_{2}+b_{2} & -\infty & <b_{2}<\infty .
\end{align*}
$$

with

$$
\begin{align*}
& \left(x_{i}^{\prime}-\mu_{1}^{\prime}\right)=a\left(x_{i}-\mu_{1}\right) \\
& \left(y_{i}^{\prime}-\mu_{2}^{\prime}\right)=a\left(y_{i}-\mu_{2}\right) \tag{4.5}
\end{align*}
$$

The new sampling distribution $\left.p(d x)^{\prime} d y^{\prime} \mid h_{1}^{\prime} h_{2}^{\prime} c^{\prime}\right)$ is then identice in 's! (A.1). If our state of prior knowledge is such that this transfuration
results in a Problem 2 that is entirely equivalent to Problem 1, then from the Jacobian $J=a^{-1}$ of (A.4) the uninformative prior must satisfy the functional equation

$$
\begin{equation*}
a f\left(\mu_{1}+b_{1}, \mu_{2}+b_{2}, a \sigma\right)=f\left(\mu_{1} \mu_{2} \sigma\right) \tag{A.6}
\end{equation*}
$$

from which we obtain the "widely recommended" prior element

$$
\begin{equation*}
f\left(\mu_{1} \mu_{2} \sigma\right) d \mu_{1} d \mu_{2} d \sigma=d \mu_{1} d \mu_{2} \frac{d \sigma}{\sigma} \tag{A.7}
\end{equation*}
$$

However, when two "location" parameters are present, we may in some cases feel that this does not represent our prior knowledge. In (A.4).
a change of scale $\sigma^{\prime}=$ ad affects only the accuracy of the $x_{j}, y_{i}$ measurements. It may be that for other reasons not discernible in the sampling distribution (A.1), we know that the parameter a not only sets. the scale for the "measurement errors" $\left(x_{i}-\mu_{1}\right),\left(y_{i}-\mu_{2}\right)$; it also sets the scale on which the difference of means ( $\mu_{2}-\mu_{1}$ ) is to be measured.

As a concrete if oversimplified example, a spectroscopist may wish to determine the difference in magnetic moment of two atomic states by observation of the Zeeman effect, but the available magnet has uncontrollable field fluctuations. Here o corresponds to the magnetic field strength, and $\mu_{1}, \mu_{2}$ to the resonant frequencies one is trying to measure. Doubling a doubles the probable error in the measurements; but it also doubles the measurable difference $\left(\mu_{2}-\mu_{1}\right)$. On the other hand, the crystalline environment of the atoms affects both their frequencies in the same unknown way independent of $\sigma$. All this prior information is in the mind of an experimenter $E_{1}$, but it does not appear at all
in the sampling distribution (A.1). Because of it, $E_{1}$ replaces (A.4) by

$$
\begin{align*}
\sigma^{\prime} & =a, & 0 & <a<\infty \\
\left(\mu_{2}^{\prime}-\mu_{1}^{\prime}\right) & =a\left(\mu_{2}-\mu_{1}\right)+c, & & -\infty<c<\infty \\
\frac{1}{2}\left(\mu_{1}^{\prime}+\mu_{2}^{\prime}\right) & =\frac{1}{2}\left(\mu_{1}+\mu_{2}\right)+b, & & -\infty<b<\infty \tag{A.B}
\end{align*}
$$

This leads to the functional equation

$$
\begin{equation*}
a^{2} f\left(q \mu_{1}+p \mu_{2}+b-c, p \mu_{1}+q \mu_{2}+b+c, a \sigma\right)=f\left(\mu_{1}^{\mu_{2}} \sigma\right) \tag{A.9}
\end{equation*}
$$

where $2 q \equiv 1+a, 2 p \equiv 1-a$. But the LHS can be independent of both $b, c$ only if $f\left(\mu_{1} \mu_{2} \sigma\right)=f(\sigma)$. The functional equation then collanses to $a^{2} f(a \sigma)=f(\sigma)$, or $f(\sigma) \propto \sigma^{-2}$, the prior that DSZ found to avoid the paradox in Example 2.

We are far from having exhausted the number of transitive groups under which the sampling distribution (A.1) is invariant. For example,

$$
\begin{aligned}
\sigma^{\prime} & =a \sigma & 0 & <a<\infty \\
\mu_{1}^{\prime} & =a \mu_{1}+b & -\infty & <b<\infty \\
\mu_{2}^{\prime} & =\mu_{2}+c & -\infty & <c<\infty
\end{aligned}
$$

leads again to $f\left(\mu_{1} \mu_{2} \sigma\right) \propto \sigma^{-2}$; while

$$
\begin{aligned}
\sigma^{\prime} & =a \sigma \\
\mu_{1}^{\prime} & =a \mu_{1}+b \\
\mu_{2}^{\prime} & =a \mu_{2}+c
\end{aligned}
$$

leads to $f\left(\mu_{1} \mu_{2} \sigma\right) \propto \sigma^{-3}$, which DSZ noted as avoiding the paradox in Example 4a, Version 1.

All of these correspond to different possible kinds of prior knowledge about the physical meaning of the parameters. These differences cannot be seen in the sampling distribution, which describes only the measurement errors. Thus, when we pass beyond pedagogical examples to real life problems, a further aspect of the quoted remark of Lindley (1971) becomes apparent.

As we see from this, group analysis does not answer questions of uniqueness. A given group leads to a definite prior, but there may be more than one group, and in any event group analysis--at least in any form yet visudized--does not tell us whether other solutions of the integral equations (30) may exist beyond those resulting from the group structure. However, it may be that new theorems bearing on this are waiting to be discovered.

## APPENDIX 8 - HISTORICAL NOTE

Since statistical theory is returning to the original viewpoint of Laplace on the relation of inference and probability, we follow Laplace's example also in concluding with two remarks on the background of the marginalization problem, in addition to those noted by DSZ.

The mathematical facts underlying marginalization were fully recognized-and in the writer's view correctly interpreted--by Geisser and Cornfield (1963). Their equations (3.10) and (3.26) are just what we now call $B_{1}$ 's result and $B_{2}$ 's result; but instead of seeing a paradox in the difference, they very wisely tenned the latter a "pseudoposterior distribution."

And inevitably, when we search for the origin of a Bayesian result, we turn to Jeffreys (1939). His 93.8 considers the bivariate normal case, and although the sample correlation coefficient $r$ is a sufficient statistic for p. the posterior distributions (10), (24) again reveal the slight difference caused by different prior information about the location parameters ( $a, b$ ). The comparison is reminiscent of our Equations (50), (51) above.

## REFERENCES

A. P. Dawid, M. Stone, and J. V. Zidek (1973), "Marginalization Paradoxes in Bayesian and Structural Inference." J. Roy Stat. Soc. B 35, 189-233.
D. A. S. Fraser (1961), "On Fiducial Inference." Ann. Math. Stat. 32, 661-676.

George Gamow, The Birth and Death of the Sun, Penguin Books, Inc. New York (1945). The concluding sentence is: "And the year $12,000,000,000$ after the Creation of the Universe, or A.D. $10,000,000,000$, will find infinite space sparsely filled with still receding stellar islands populated by dead or dying stars."
M. Hamermesh (1962), Group Theory. Addison-Wesley, Reading, Mass. pp. 293-295.
E. T. Jaynes (1968), "Prior Probabilities," IEEE Trans. Systems Sci. and Cybernetics SSC-4, pp. 227-241. Reprinted in Concepts and Applications of Modern Decision Models, V. M. Rao Tummala and R. C. Henshaw. Editors (Michigan State University Business Studies Series: 1975).
E. T. Jaynes (1971), "The Well-Posed Problem," in Foundation of Statistical Inference (V. P. Godambe and D. A. Sprott, Editors) Toronto: Holt, Reinhart and Winston.
E. T. Jaynes (1976), "Confidence Intervals vs. Bayesian Intervals," in Foundations of Probability Theory, Statistical Inference, and Statistical Theories of Science, W. L. Harper and C. A. Hooker, Editors, D. F.eidel Publishing Co. Dordrecht-Holland; Vol. II, pp. 175-257.

Lord Kelvin, "On the Age of the Sun's Heat," Macmillan's Magazine, March 1862. He concludes: "It seems, therefore, on the whole most probable that the sun has not illuminated the earth for $100,000,000$ years, and almost certain that he has not done so for $500,000,000$ years. As for the future, we may say, with equal certainty, that inhabitants of the earth cannot continue to enjoy the light and heat essential to their life, for many million years longer, unless sources now unknown to us are prepared in the great storehouse of creation." Those unknown sources were revealed 43 years later, when Albert Einstein wrote $E=m c^{2}$.
D. V. Lindley (1958), "Fiducial Distributions and Bayes' Theorem," J. Roy. Stat. Soc. (B), 20, 102.
D. V. Lindley (1971), Bayesian Statistics: A Review. Philadelphia; Society of Industrial and Applied Mathematics.
H. Poincaré (1912), Calcul des Probabilites, pp. 118-130.
C. Villegas (1971), On Haar Priors, in Foundations of Statistical Inference (V. P. Godambe and D. A. Spott, Editors), Toronto: Holt, Rinehart, and Winston.


[^0]:    ** preliminary account of this work was given at the 14 th NBER-NSF. Seminar on Bayesian Inference, Holmdel, N. J. (June 1977).

