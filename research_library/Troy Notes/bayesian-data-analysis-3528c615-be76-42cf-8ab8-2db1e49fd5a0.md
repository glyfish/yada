Bayesian Data Analysis

Troy Stribling May 28, 2017

## Bernoulli Trial

Consider tree Bernoulli trial

$$
P(X=S)=P \quad P(\bar{X}=F)=1-P
$$

Where $s$ represents a success and $F Q$ failure. Let $M$ be the number of successes in $n$ attenpts. $\mu$ will have a binomial distribution which has density,

$$
f_{M}(m)=\binom{n}{m} p^{m}(1-p)^{n-m}
$$

Now

$$
\begin{aligned}
& \sum_{m=0}^{n} f_{\mu}(m)=\sum_{m=0}^{n}\binom{n}{m} p^{m}(1-p)^{n-m} \\
& =(p+1-p)^{n}=1
\end{aligned}
$$

and

$$
\begin{aligned}
\mu&=E(M) \\
&=\sum_{m=0}^{n} m f_{\mu}(m) \\
&=\sum_{m=0}^{n} m\binom{n}{m} p^{m}(1-p)^{n-m} \\
&=\sum_{m=0}^{n} m \frac{n!}{(n-m)!m!} P^{m}(1-P)^{n-m} \\
&=\sum_{m=1}^{n} m \frac{n!}{(n-m)!m!} P^{m}(l-p)^{n-m}
\end{aligned}
$$

since the first term is zero

$$
\begin{aligned}
&=\sum_{m=1}^{n} \frac{n!}{(n-m)!}(m-1)!P^{m}(1-P)^{n-m} \\
&=\sum_{m=1}^{n} \frac{n(n-1)!}{[(n-1)-(m-1)]!(m-1)!P^{m}(1-P)^{n-m}} \\
&=n p \sum_{m=1}^{n} \frac{n(n-1)!}{[(n-1)-(m-1)]!(m-1)!P^{m-1}(1-p)^{(n-1)-(m-1)}} \\
\end{aligned}
$$

using the change of variable

$$
K=m-1
$$

gives

$$
\begin{aligned}
E(M) & =n p \sum_{k=0}^{n-1} \frac{(n-1)!}{[(n-1)-k]!k!} P^{k}(1-p)^{(n-1)-k} \\
& =n p \sum_{k=0}^{n-1}\binom{n-1}{k} p^{k}(1-p)^{(n-1)-k} \\
& =n p[p+(1-p)]^{n-1}=n p
\end{aligned}
$$

and

$$
\begin{aligned}
E\left(M^{2}\right) =& \sum_{m=0}^{n} m^{2} f_{M}(m) \\
= & \sum_{m=0}^{n} m^{2}\binom{n}{m} P^{m}(1-P)^{n-m} \\
= & \sum_{m=0}^{n} m m \frac{n!}{(n-m)!m!} P^{m}(1-P)^{n-m} \\
= & \sum_{m=1}^{n} m p n\left\{\frac{(n-1)!}{[(n-1)-(m-1)]!(m-1)!}\right\} P^{m-1}\left((-p)^{(n-1)-(m-1)}\right.
\end{aligned}
$$

as before let

$$
\begin{aligned}
E\left(\mu^{2}\right)= & p n \sum_{k=0}^{k-1}(k+1) \frac{(n-1)!}{[(n-1)-k]!k!} p^{k}(1-p)^{(n-1) k} \\
= & p n\left\{\sum_{k=0}^{n-1} k \frac{(n-1)!}{[(n-1)-k]!k!} p^{k}(1-p)^{(n-1)-k}\right. \\
& \left.+\sum_{k=0}^{n-1}\binom{n-1}{k} p^{k}(1-p)^{(n-1)-k}\right\}
\end{aligned}
$$

In the first sum the first term is zero and the second term sums to 1 so,

$$
\begin{aligned}
&=p n \{\sum_{k=1}^{n-1}(n-1) \frac{(n-2)!}{[(n-2)-(k-1)](k-1)!} p^{k}(1-p)^{(n-2)-(k-1)} +1\} \\
&=p n+p n \cdot p(n-1) \sum_{k=1}^{m-1}\binom{n-2}{k-1} p^{k-1}(1-p)^{(n-2) \cdot(k-1)}
\end{aligned}
$$

let

$$
l=k-1
$$

then

$$
\begin{aligned}
E\left(\mu^{2}\right) & =p n+p^{2} n(n-1) \sum_{l=0}^{n-2}\binom{n-2}{l} p^{l}(1-p)^{(n-2)-l} \\
& =p n+p^{2} n(n-1)
\end{aligned}
$$

and

$$
\begin{aligned}
\sigma^{2}=\operatorname{Var}(\mu) & =E\left(\mu^{2}\right)-[E(\mu)]^{2} \\
& =p n+p^{2} n(n-1)-p^{2} n^{2} \\
& =p n+p^{2} n^{2}-p^{2} n-p^{2} n^{2} \\
& =p n-p^{2} n \\
& =p n(1-p)
\end{aligned}
$$

For $n, n p$ and $n(1-p)$ large the binomial distribution can be appoximated by a normal distribution with density

$$
f_{\mu}(m) \approx \frac{1}{\sqrt{2 \pi} \sigma} e^{-(m-\mu)^{2} / 2 \sigma^{2}}
$$

where

$$
\begin{aligned}
& \mu=n p \\
& \sigma^{2}=n p(1-p)
\end{aligned}
$$

## Expectation of Success Frequency

Consider the Bernoulli trial

$$
P(X=s)=P \quad P(\bar{X}=F)=1-P
$$

Where $s$ represents a success and $F Q$ failure. Let $M$ be the number of successes in $n$ afternpts. $M$ will have a binomial distribution which has density,

$$
f_{M}(m)=\binom{n}{m} p^{m}(1-p)^{n-m}
$$

Let

$$
s=\frac{m}{n}
$$

represent the fraction of successes in $n$ attempts.
Then using the previous result $E(s)=\frac{E(\mu)}{n}=\frac{n p}{n}=P$
and

$$
\begin{aligned}
E\left(s^{2}\right) & =E \frac{\mu^{2}}{n^{2}}=\frac{1}{n^{2}}\left[p n+p^{2} n(n-1)\right] \\
& =\frac{p}{n}+\frac{p^{2}}{n}(n-1)
\end{aligned}
$$

50

$$
\begin{aligned}
\operatorname{Var}\left(s^{2}\right) & =E\left(s^{2}\right)-[E(s)]^{2} \\
& =\frac{p}{n}+\frac{p^{2}}{n}(n-1)-p^{2} \\
& =\frac{p}{n}+p^{2}-\frac{p^{2}}{n}-p^{2} \\
& =\frac{p}{n}(1-p)
\end{aligned}
$$

Trues

$$
\begin{aligned}
& \mu_{s}=E(s)=p \\
& \sigma_{s}^{2}=\operatorname{var}\left(s^{2}\right)=\frac{p}{n}(1-p)
\end{aligned}
$$

If $P$ is unknown us provides as estimate $P$ and $O_{s}$ the variance of the estimate.

## Difference of Random Variables

Consider two independent random variables $\bar{X}_{A}$ and $\bar{X}_{B}$ with densities $f_{X_{A}}\left(x_{A}\right)$ and $f_{X_{B}}\left(x_{B}\right)$. let

$$
\bar{x}=g\left(\bar{x}_{A}\right)-h\left(\bar{x}_{B}\right)
$$

where

$$
f_{\bar{I}}\left(x_{A}, x_{B}\right)=f_{\bar{X}_{A}}\left(x_{A}\right) f_{\bar{I}_{B}}\left(x_{B}\right)
$$

Now, the expectaon of $\bar{X}$ is given by

$$
\begin{aligned}
E(\bar{x}) & =\sum_{x_{A}} \sum_{x_{B}}\left[g\left(x_{A}\right)-h\left(x_{B}\right)\right] f\left(x_{A}, x_{B}\right) \\
& =\sum_{x_{A}} \sum_{x_{B}} g\left(x_{A}\right) f_{I_{A}}\left(x_{A}\right) f_{I_{B}}\left(x_{B}\right) \\
& -\sum_{x_{A}} \sum_{x_{B}} h\left(x_{B}\right) f_{I_{A}}\left(x_{A}\right) f_{I_{B}}\left(x_{B}\right)
\end{aligned}
$$

but

$$
\sum_{x_{A}} f_{I_{A}}\left(x_{A}\right)=1 \quad \sum_{x_{B}} f\left(x_{B}\right)=1
$$

50

$$
\begin{aligned}
E(X) & =\sum_{x_{A}} h\left(x_{A}\right) f\left(x_{A}\right)-\sum_{x_{B}} g\left(x_{B}\right) f\left(x_{B}\right) \\
& =E\left[h\left(x_{A}\right)\right] \cdot E\left[g\left(x_{B}\right)\right]
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left(\bar{X}^{2}\right)=\sum_{x_{A}} \sum_{x_{B}}\left[h\left(x_{A}\right)-g\left(x_{B}\right)\right]^{2} f\left(x_{A}, x_{B}\right) \\
& =\sum_{x_{A}} \sum_{x_{B}}\left[h^{2}\left(x_{A}\right)-2 h\left(x_{A}\right) g\left(x_{B}\right)+g^{2}\left(x_{B}\right)\right] f\left(x_{A}, x_{B}\right) \\
& =\sum_{x_{A}} \sum_{x_{B}} h^{2}\left(x_{A}\right) f_{I_{A}}\left(x_{A}\right) f_{I_{B}}\left(x_{B}\right) \\
& -2 \sum_{x_{A}} \sum_{x_{B}} h\left(x_{A}\right) g\left(x_{B}\right) f_{I_{A}}\left(x_{A}\right) f_{I_{B}}\left(x_{B}\right) \\
& +\sum_{x_{A}} \sum_{x_{B}} g^{2}\left(x_{B}\right) f_{I_{A}}\left(x_{A}\right) f_{I_{B}}\left(x_{B}\right) \\
& =\sum_{x_{A}} h^{2}\left(x_{A}\right) f_{I_{A}}\left(x_{A}\right)+\sum_{x_{B}} g^{2}\left(x_{B}\right) f_{I_{B}}\left(x_{B}\right) \\
& -2\left[\sum_{x_{A}} h\left(x_{A}\right) f_{I_{A}}\left(x_{A}\right)\right]\left[\sum_{x_{B}} g\left(x_{B}\right) f_{I_{B}}\left(x_{B}\right)\right]
\end{aligned}
$$

$$
=E\left[h^{2}\left(x_{A}\right)\right]+E\left[S^{2}\left(x_{B}\right)\right]-2 E\left[h\left(x_{A}\right)\right] E\left[g\left(x_{B}\right)\right]
$$

and

$$
\begin{aligned}
& \operatorname{Var}(X)=E\left(\bar{X}^{2}\right)-E^{2}(\bar{X}) \\
= & E\left[h^{2}\left(x_{A}\right)\right]+E\left[g^{2}\left(x_{B}\right)\right] \\
& -2 E\left[h\left(x_{A}\right)\right] E\left[g\left(x_{B}\right)\right] \\
& -\left\{E\left[h\left(x_{A}\right)\right]-E\left[g\left(x_{B}\right)\right] \xi^{2}\right. \\
= & E\left[h^{2}\left(x_{A}\right)\right]+E\left[g^{2}\left(x_{B}\right)\right]-2 E\left[h\left(x_{A}\right)\right] E\left[g\left(x_{B}\right)\right] \\
= & E^{2}\left[h\left(x_{A}\right)\right]-E^{2}\left[g\left(x_{B}\right)\right]+2 E\left[h_{\left(X_{A}\right)}\right] E\left[g\left(x_{B}\right)\right] \\
= & E\left[h^{2}\left(x_{A}\right)\right]-E^{2}\left[h\left(x_{A}\right)\right]+E\left[g^{2}\left(x_{B}\right)\right] \\
= & E^{2}\left[g\left(x_{B}\right)\right] \\
= & \operatorname{Var}\left[h\left(x_{A}\right)\right]+\operatorname{Var}\left[g\left(x_{B}\right)\right]
\end{aligned}
$$

## A/B Test

Consider two Bernoulli trials $A$ and $B$. det $M_{A}$ indicate the number of successes of trial $A$ and $M_{B}$ the number of successes of trial $B$.
Assume trad the Probability of success for each trial is unkwon.

For the $A / B$ test let

$$
S_{A B}=\frac{\mu_{A}}{n_{A}}-\frac{\mu_{B}}{n_{B}}
$$

Where $M_{\Delta}$ is the number of successes for trial $A$ and $n_{A}$ the number of attempts. Likewise let $\mu_{B}$ be the numer of saccesses of trial $B$ and $n_{B}$ the number of attempts

50

$$
E\left(s_{A B}\right)=E\left(\frac{\mu_{A}}{n_{A}}\right)-E\left(\frac{\mu_{B}}{n_{B}}\right)
$$

and

$$
\operatorname{Var}\left(S_{A B}\right)=\operatorname{Var}\left(\frac{M_{A}}{n_{A}}\right)+\operatorname{Var}\left(\frac{M_{B}}{n_{B}}\right)
$$

Since the probability of each trial is assumed unknown use the estimates

$$
\begin{aligned}
& \hat{P}_{A}=E\left(\frac{\mu_{A}}{n_{D}}\right)=\frac{m_{A}}{n_{A}} \\
& \hat{P}_{B}=E\left(\frac{\mu_{B}}{n_{B}}\right)=\frac{m_{B}}{n_{B}}
\end{aligned}
$$

Here $m_{A}$ and $m_{B}$ are the observed number of suceesses of trials $A$ and $B$ respectively and $n_{A}$ and $n_{B}$ are the number of attempts for the trials.

Now

$$
\begin{aligned}
& \operatorname{var}\left(\frac{m_{A}}{n_{A}}\right)=\frac{p_{A}}{n_{A}}\left(1-p_{A}\right) \\
& \operatorname{var}\left(\frac{m_{B}}{n_{B}}\right)=\frac{p_{B}}{n_{B}}\left(1-p_{B}\right)
\end{aligned}
$$

using the estimated probabilities gives

$$
\begin{aligned}
& \operatorname{Var}\left(\hat{p}_{A}\right)=\hat{p}_{A}\left(1-\hat{p}_{A}\right) \\
& \operatorname{Var}\left(\hat{p}_{B}\right)=\hat{p}_{B}\left(1-\hat{p}_{B}\right)
\end{aligned}
$$

Bringing things together and letting

$$
\hat{P}_{A B}=E\left(S_{A B}\right)
$$

gives

$$
\begin{aligned}
\hat{p}_{A B} & =\hat{p}_{A}-\hat{p}_{B} \\
\operatorname{Var}\left(\hat{p}_{A B}\right) & =\hat{p}_{A}\left(1-\hat{p}_{A}\right)+\hat{p}_{B}\left(1-\hat{p}_{B}\right) \\
& =\sigma_{\hat{p}_{B}}^{2} \hat{p}_{A B}
\end{aligned}
$$

Since, $\hat{P}$ is has a Bionomial distribution which is appoximately normal Pab can be assumed to be normally distribuded.

To deformine if there is any differnce between the trials $A$ and $B$ that results from anything other than the random hature of the trial a null hypothesis of

$$
\hat{P}_{A B}=0
$$

is assumed.
The sisnificance of departures from the null hypothesis is determined by checking the $95 \%$ confidence interval of

$$
\frac{\hat{P}_{A B}}{\hat{S}_{P A B}}
$$

which will be assumed normally distributed with mean 0 and variance 1

$$
N(0,1)
$$

## Baysian Inference Definitions

* Sum Rule

$$
P(\bar{X}=x)+P(\bar{X} \neq x)=1
$$

The sum rule defines normalization of the probability density.

* Product Rule

$$
P(\mathbb{Z}, I)=P(\mathbb{X} \mid I) P(\underline{I})
$$

which follows from the definition of conditional probability.

* Marginalization

This should be a SUM of $P(X, Y)$ over $Y$

$$
P(X)=\sum_{y} P(X \mid \bar{I}=y)
$$

or

$$
P(x)=\int_{-\infty}^{\infty} p(x, y) d y
$$

* Bayes Theorem

$$
P(\bar{X} \mid \bar{Y})=\frac{P(\bar{I} \mid \bar{X}) P(\bar{X})}{P(\bar{I})}
$$

This can be derived from the product rule by neting that

$$
\begin{aligned}
& P(\bar{X}, \bar{Y})=P(\bar{X} \mid \bar{Y}) P(\bar{Y}) \\
& P(\bar{X}, \bar{Y})=P(\bar{Y} \mid \bar{X}) P(\bar{X})
\end{aligned}
$$

equating the two expressions gives Bayes Rule

$$
\begin{aligned}
& P(\underline{x} \mid \bar{y}) P(\underline{y})=P(\underline{y} \mid \bar{x}) P(\underline{x}) \\
& \Rightarrow P(\bar{x} \mid \underline{y})=\frac{P(\bar{y} \mid \bar{x}) P(\bar{x})}{P(\bar{y})}
\end{aligned}
$$

when doing an analysis it is useful to think of

$$
\begin{aligned}
& \bar{I}=H=\text { hipothesis } \\
& \bar{I}=D=\text { data }
\end{aligned}
$$

Then Bayes Rule can be stated as

$$
P(H \mid D)=\frac{P(D(H) P(H)}{P(D)}
$$

The terms in this expression have formal names

$$
\begin{aligned}
& P(H \mid D)=\text { posterior distribution } \\
& P(H)=\text { prior distribution } \\
& P(D \mid H)=\text { liklihood distribution } \\
& P(D)=\text { evidence }
\end{aligned}
$$

The prior represents the knowledge of the hypothesis before any data has been analyzed.
The liklihood distribution represents the experimental measurements.
The posterior distribution is the combination of the liklihood and prior distribution to represent the truth of the nypothesis groen the observed doda.

The evidence distribution is
the marginalized data distribution In some anlysis it is not needed. If it is needed it can by computed by normalizing the posterior distribution or
using marginilization

$$
\begin{aligned}
P(D) & =P(D, H)+P(D, \bar{H}) \\
& =\frac{P(D \mid H)}{P(H)}+\frac{P(D(\bar{H})}{P(H)}
\end{aligned}
$$

where $\bar{H}$ indicates that the hypothesis is false.

## Bayesian Coin Flip

Let the probability of throwing neads be denoted by $n$. The probability of throwing $r$ heads in $n$ trials. will be given by a binomial distribution density/

$$
P(r, n \mid h)=\binom{n}{r} h^{r}(1-h)^{n-r}
$$

Bayes Theorem will be

$$
p(h \mid r, n)=\frac{p(r, n \mid h) p(h)}{p(r, n)}
$$

Since $0 \leqslant n \leqslant 1$ assume $a$ uniform prior

$$
p(h)= \begin{cases}1 & 0 \leqslant h \leqslant 1 \\ 0 & \text { otherwise }\end{cases}
$$

The likelyhood distribution

$$
p(r, n \mid h)=\binom{n}{r} h^{r}(1-h)^{n-r}
$$

So the posterior distribution

$$
\begin{aligned}
& p(h \mid n, r)=\frac{1}{p(n, r)}\binom{n}{r} h^{r}(1-n)^{n-r} \\
& \text { where } 0<h<1 \\
& \text { Normalizing the posterior } \\
& \text { distribution gives } \\
& \int_{0}^{1} p(h \mid n, r) d h=\frac{1}{p(n, r)}\binom{n}{r} \int_{0}^{1} h^{r}(1-h)^{n-r} d x \\
& =1 \\
& \text { But } \\
& B(a, b)=\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
& \int_{0}^{1} h^{r}(1-h)^{n-r} d x=B(r+1, n-r+1) \\
& \text { and } \\
& \int_{0}^{1} p(h \mid n, r) d h=\frac{1}{p(n, r)}\binom{n}{r} B(r+1, n-r+1) \\
& =1
\end{aligned}
$$

$$
\Rightarrow \frac{1}{p(n, r)}\binom{n}{r}=\frac{1}{B(r+1, n-r+1)}
$$

and the normalized posterior is given by

$$
P(h \mid n, r)=\frac{h^{r+1}(1-h)^{n-r+1}}{B(r+1, n-r+1)}
$$

which is the Beta distribution

$$
P(n \mid n, r)=\operatorname{Beta}(r+1, n-r+1)
$$

* Non. Uniform Prior
with a non-uniform prior more information about the expeded result can be encoded in the prior.
The Beta distribution is a good choice for a Binomial Since the postier is a Beta. This relationship is called a conjugate prior.
so Bayes Rule is

$$
p(h \mid r, n)=\frac{1}{p(r, n)} p(r, n(h) p(h)
$$

and

$$
\begin{aligned}
& p(r, n \mid h)=\binom{n}{r} h^{r}(1-h)^{n-r} \\
& \begin{aligned}
p(h) & =\operatorname{Beta}(h, \alpha, \beta) \\
& =\frac{1}{B(\alpha, \beta)} h^{\alpha-1}(1-h)^{\beta-1}
\end{aligned}
\end{aligned}
$$

where $\alpha$ and $\beta$ are free parameters. The maximum value of Beta $(n, \alpha, \beta)$

$$
\begin{aligned}
& h_{\text {max }}=\frac{\alpha}{\alpha+\beta} \\
& \text { so } \\
& p(n \mid r, n)=\frac{1}{p(r, n)} \frac{1}{B(a, \beta)}\binom{n}{r} h^{r+a-1}(1-h)^{n-r+\beta-1}
\end{aligned}
$$

$$
\begin{aligned}
& \text { Normalizing gives } \\
& \int_{0}^{1} p(n / n, r) d h=1 \\
= & \frac{1}{p(n, r)} \frac{1}{B(\alpha, \beta)}\binom{n}{r} \int_{0}^{1} n^{r+\alpha-1}(1-n)^{n-r+\beta-1} d h \\
= & \frac{1}{p(n, r)} \frac{1}{B(\alpha, \beta)}\binom{n}{r} B(r+\alpha, n-r+\beta) \\
= & 1 \\
= & \frac{1}{(n, r)} \frac{1}{B(\alpha, \beta)}\binom{n}{r}=\frac{1}{B(r+\alpha, n-r+\beta)} \\
& p(n \mid n, r)=\frac{h^{r+\alpha-1}(1-h)^{n-r+\beta-1}}{B(r+\alpha, n-r+\beta)} \\
& =\operatorname{Beta}(r+\alpha, n-r+\beta)
\end{aligned}
$$

## Sequential Data Analysis

sequential analysis of data using Bayes Rule would apply the analysis on each data item as they become available and use the obtained posterior as the prior for the next data item.
under what conditions is this the same as analyzing all data at the same time?

Consider a set of data $\left\{D_{n}\right\}$ where $n=1,2,3, \ldots, N$.

In a one-step analysis Bayes Theorem would give

$$
p\left(H \mid\left\{D_{n}\right\}\right) \propto p\left(\left\{D_{n}\right\} \mid H\right) p(H)
$$

In a sequntral analysis for the $n=1$

$$
p\left(H \mid D_{1}\right) \text { \& } p\left(D_{1} \mid H\right) p(t)
$$

For $n=2$ use the $n=1$ posterior as the $n=2$ prior so that

$$
\begin{aligned}
& P\left(H \mid D_{2}, D_{1}\right) \propto P\left(D_{2} \mid H, D_{1}\right) p\left(H \mid D_{1}\right) \\
& =p\left(D_{2} \mid H, D_{1}\right) p\left(D_{1} \mid H\right) p(H)
\end{aligned}
$$

and for $n=3$

$$
\begin{aligned}
& p\left(H \mid D_{3}, D_{2}, D_{1}\right) \propto p\left(D_{3} \mid H, D_{1}, D_{2}\right) p\left(H \mid D_{1} D_{2}\right) \\
& =p\left(D_{3} \mid H, D_{1}, D_{2}\right) p\left(D_{2} \mid H, D_{1}\right) p\left(D_{1} \mid H\right) p(H)
\end{aligned}
$$

and for $n=N$

$$
\begin{aligned}
& p\left(H \mid\left\{D_{n}\right\}\right) \propto p\left(D_{N} \mid H, D_{1}, D_{2}, \ldots D_{N-1}\right) \\
& p\left(D_{N-1} \mid H, D_{1}, D_{2}, \ldots, D_{N-2}\right) \cdots p\left(D_{1} \mid H\right) p(H)
\end{aligned}
$$

comparing with the one-stel anylsis it is seen that

$$
p\left(H \mid\left\{D_{n}\right\}\right) \propto p\left(\left\{D_{N}\right\} \mid H\right) p(H)
$$

If it is assumed that the $\left\{D_{n}\right\}$ are independent
$p\left(\left\{D_{n}\right\} \mid H\right)=p\left(D_{N} \mid H\right) p\left(D_{N-1} \mid H\right) \cdots p\left(D_{1}(H)\right.$ and for the sequential anylsis, if the $\left\{D_{n}\right\}$ are independencl $p\left(D_{N} \mid H, D_{1}, D_{2}, \ldots, D_{N-1}\right)=p\left(D_{N} \mid H\right)$ It the follows that for both

$$
\begin{aligned}
& p\left(H \mid\left\{D_{n}\right\}\right)=p\left(D_{N} \mid H\right) p\left(D_{N-1} \mid H\right) \cdots p\left(D_{1} \mid H\right) p(H)
\end{aligned}
$$

Thus for sequential analysis to be equivalent $0_{n} \xi$ one-step analysis the $\left\{D_{n}\right\}$ mu

## Best Estimate

The best estimate of a parameter with a posterisr distribution inferred from Bayes Rule will be the value that maximizes the distribution. If this value is denoted by $x_{0}$ then

$$
\left.\frac{d p}{d x}\right|_{x=x_{0}}=0
$$

where

$$
p=p(x \mid D)
$$

Also, the ensure that $x_{0}$ is a maximum

$$
\begin{equation*}
\left.\frac{d^{2} p}{d x^{2}}\right|_{x=x_{0}} <\ 0
\end{equation*}
$$

Since $P$ may have a sharp peak the logarithm of $P$ will vary more slowly and also be maximum at $x_{0}$. Let

$$
L=\log p(x \mid D)
$$

if 2 is expanded in a Taylor series absut $x_{0}$ to lowest Grder

$$
L=L\left(x_{0}\right)+\left.\frac{1}{2} \frac{d^{2} L}{d x^{2}}\right|_{\substack{x=x_{0} \\\left(x-x_{0}\right)^{2}}}
$$

The linear term is zero since

$$
\left.\frac{d L}{d x}\right|_{x=x_{0}}=0
$$

Thus near $x_{0}$ the porterior pdf is appoximately normal

$$
P \approx A \exp \left[\left.\frac{1}{2} \frac{d^{2} l}{d x^{2}}\right|_{x=x_{0}}\left(x-x_{0}\right)^{2}\right]
$$

where

$$
\mu=X_{0}
$$

and

$$
\frac{1}{b^{2}}=-\left.\frac{d^{2} L}{d x^{2}}\right|_{x=x_{0}}
$$

recall that for to to be a makimum

$$
\left.\frac{d^{2}}{d x^{2}}\right|_{x=x_{0}}<0
$$

Thus $x_{0}$ is the best estimate and 0 a measure of the accuracy of the estimate. 0 is usually referred to as the error bar.

$$
x_{0} \pm 36
$$

Any estimate of $x$ lying outside 36 is considered improbable
For an asymetric posterior poff confidence interval is defined as the 95\% percentile
$P\left(x_{1} \leqslant x \leqslant x_{2} \mid D\right)=\int_{x_{1}}^{x_{2}} p(x \mid D) d x=0.95$
Any estimate of $x_{0}$ lying outside the confidence interval is considered im probable.

## * Best Estimáte Corn Toss

Consider the coin toss example where the postier with a uniform prior is given by

$$
P(h \mid h, r) \propto h^{r}(1-h)^{n-r}
$$

where $h$ is the probability of tossing heads $n l$ is the number of tosses and $r$ the number of heads tossed

Taking the logarithm gives with ${ }^{2}$ cepresenting the log of the proportionality constant $\log p(h \mid h, r)=c+\log \left[h^{r}(1-h)^{n-r}\right]$
$=c+\log h^{r}+\log (1-h)^{n-r}$
$=C+r \log h+(n-r) \log (1-h)$
The best estimate will be given by the value of $h$ the the posterior distribution
$\frac{d}{d h} \log p(h \mid n, r)=\frac{r}{h} \cdot \frac{n-r}{1-h}$
$\Rightarrow \quad \frac{r}{h_{0}}-\frac{n-r}{1-h_{0}}=0$

$$
\begin{aligned}
& \Rightarrow \frac{r}{h_{0}}=\frac{n-r}{1-h_{0}} \Rightarrow r(1-h)=h(n-r) \\
& \Rightarrow r=h_{0}[(n-r)+r]=h_{0} n \\
& \Rightarrow h_{0}=\frac{r}{n}
\end{aligned}
$$

Which is the expeted result
The error bar is given

$$
\frac{1}{\sigma^{2}}=-\left.\frac{d^{2}}{d h^{2}} \log p(h \mid n, r)\right|_{h=h_{0}}
$$

now

$$
\begin{aligned}
& \frac{d^{2}}{d h^{2}} \log p(h \mid h, r)=\frac{d}{d h}\left[\frac{r}{h}-\frac{h-r}{1-h}\right] \\
& =-\frac{r}{h^{2}}-\frac{n-r}{(1-h)^{2}}
\end{aligned}
$$

so

$$
\frac{1}{\sigma^{2}}=\frac{r}{h_{0}^{2}}+\frac{n-r}{\left(1-h_{0}\right)^{2}} \frac{r\left(1-h_{0}\right)^{2}+h_{0}^{2}(n-r)}{h_{0}^{2}\left(1-h_{0}\right)^{2}}
$$

$$
\begin{aligned}
& =\frac{r\left[\left(1-h_{0}\right)^{2}-h_{0}^{2}\right]+h_{0}^{2} n}{h_{0}^{2}\left(1-h_{0}\right)^{2}} \\
& =\frac{r\left(1-2 h_{0}+h_{0}^{2}-h_{0}^{2}\right)+h_{0}^{2} n}{h_{0}^{2}\left(1-h_{0}\right)^{2}} \\
& =\frac{r\left(1-2 h_{0}\right)+h_{0}^{2} n}{h_{0}^{2}\left(1-h_{0}\right)^{2}}
\end{aligned}
$$

usin 9

$$
h_{0}=\frac{r}{n}
$$

The numerctor becomes

$$
\begin{aligned}
& =r\left(1-\frac{2 r}{n}\right)+\frac{r^{2}}{n} \\
& =r-\frac{2 r^{2}}{n}+\frac{r^{2}}{n}=r-\frac{r^{2}}{n} \\
& =r\left(1-\frac{r}{n}\right)=n h_{0}\left(1-h_{0}\right) \\
& \text { so } \frac{1}{\sigma^{2}}=\frac{n h_{0}\left(1-h_{0}\right)}{h_{0}^{2}\left(1-h_{0}\right)^{2}}=\frac{n}{h_{0}\left(1-h_{0}\right)} \\
& \Rightarrow \sigma=\frac{h_{0}\left(1-h_{0}\right)}{n}
\end{aligned}
$$

## * Gaussian Noise Best Estimate of mean

Gaussian noise with mean $\mu$ and standard deviation $\sigma$ has a pdf of

$$
p\left(x_{k} \mid \mu, \sigma\right)=\frac{1}{\sigma \sqrt{\theta \pi}} \exp \left[\frac{-\left(x_{k}-\mu\right)^{2}}{2 \sigma^{2}}\right]
$$

where $x_{k}$ represents the $k^{\prime}$ th data item.

What is the best estimate of $\mu$ given data $\left\{x_{k}\right\}$ and what is the confderice in this estimate assuming the $x_{k}$ are independent.
using Bayes Rule

$$
p\left(\mu \mid\left\{x_{k}\right\}, \sigma\right) \propto p\left(\left\{x_{k}\right\} \mid \mu, \sigma\right) p(\mu \mid \sigma)
$$

Since the $x_{k}$ are independent the liklihood is given by with $N_{X_{k}}$ representing the number of $X_{k}$

$$
p\left(\left\{x_{k}\right\} \mid \mu, \sigma\right)=\prod_{k}^{N} p\left(x_{k} \mid \mu, \sigma\right)
$$

a knowledge of the width of the distribution tells us nothing about the mean $\mu$ so

$$
p(\mu \mid \sigma)=p(\mu)
$$

if it is believed that $\mu$ lies between $\mu_{\text {min }}$ and $\mu_{\text {max }}$ and is distributed uniformly

$$
p(\mu \mid \sigma)=\left\{\begin{array}{cl}\frac{1}{\mu_{\text {max }}}-\mu_{\text {min }} & \mu_{\text {min }} \leqslant \mu \leqslant \mu_{\text {max }} \\ 0 & \text { otherwise }\end{array}\right.
$$

The log of the posterior distribution is with $C$ the los of all preportionatity constants

$$
\begin{aligned}
& \log p\left(\mu \mid\left\{x_{k}\right\}, \sigma\right)=c+\log \prod_{k}^{N} p\left(x_{k} \mid \mu, \sigma\right) \\
& =c+\sum_{k} \log p\left(x_{k} \mid \mu, \sigma\right)
\end{aligned}
$$

for $\mu_{\text {min }} \leqslant \mu \leqslant \mu_{\text {max }}$ and 0 otherwise
Inserting gives the Gaussian liklihood

$$
\log p\left(\mu \mid\left\{x_{k}\right\}, \sigma\right)=C-\sum_{k}^{N} \frac{\left(x_{k}-\mu\right)^{2}}{2 \sigma^{2}}
$$

The Best Estimate is given by

$$
\begin{aligned}
& \frac{d}{d \mu} \log p\left(\mu / \xi x_{k} \xi, \sigma\right)=0 \\
& \Rightarrow \sum_{k}\left(x_{k}-\mu\right)=\frac{1}{\sigma^{2}} \sum_{k}\left(x_{k}-\mu\right)=0 \\
& \Rightarrow \sum_{k} x_{k}-N_{\mu}=0 \\
& \Rightarrow \mu=\frac{1}{N} \sum_{k} x_{k}
\end{aligned}
$$

and the error bar is given

$$
\begin{aligned}
& \frac{1}{\sigma^{2}}=-\frac{d^{2}}{d \mu^{2}} \log P\left(\mu \mid\left\{x_{k}\right\}, \sigma\right) \\
= & \frac{1}{\sigma^{2}} \sum_{k}^{N} 1=\frac{N}{\sigma^{2}} \\
\Rightarrow & \sigma^{2}=\frac{\sigma^{2}}{N}
\end{aligned}
$$

* If the data have different size error bars denoted by $\sigma_{k}$.
Then the Best Estimate becomes

$$
\begin{aligned}
&\frac{d}{d \mu} \log p\left(\mu /\left\{x_{k}\right\}, \sigma\right)=0 \\
&\Rightarrow \sum_{k}^{N}\left(\frac{x_{k}-\mu}{\sigma_{k}^{2}}\right)=0 \\
&\Rightarrow \sum_{k}^{N} \frac{x_{k}}{\sigma_{k}^{2}}=\mu \sum_{k}^{N} \frac{1}{\sigma_{k}^{2}} \\
\therefore \mu &=\frac{\sum_{k}^{N} \frac{x_{k}}{\theta_{k}{ }^{2}}}{\sum_{k}^{N} \frac{1}{\theta_{k}{ }^{2}}}
\ \ and \ \
\frac{1}{\bar{\sigma}^{2}}=\sum_{k}^{N} \frac{1}{\sigma_{k}^{2}}$
\end{aligned}
$$

## Feedforward Layered Neural Network

$\rightarrow$ Forward Data Propogation
![](https://cdn.mathpix.com/cropped/2025_09_18_4a3a8c593a89973bc7c8g-038.jpg?height=133&width=136&top_left_y=241&top_left_x=174)

## (xy)

![](https://cdn.mathpix.com/cropped/2025_09_18_4a3a8c593a89973bc7c8g-038.jpg?height=138&width=134&top_left_y=406&top_left_x=180)

## $x_{1}^{3}$

![](https://cdn.mathpix.com/cropped/2025_09_18_4a3a8c593a89973bc7c8g-038.jpg?height=131&width=136&top_left_y=465&top_left_x=586)
$x_{3}^{\prime}$
![](https://cdn.mathpix.com/cropped/2025_09_18_4a3a8c593a89973bc7c8g-038.jpg?height=131&width=137&top_left_y=753&top_left_x=181)

## (bi)

## Layer 1 Layer 2 Layer 3

Here inputs are denoted by circles and labeled by $x_{i}^{e}$ where $f=$ layer and $c$ is node number relative to layer
The connections beteen nodes are represented by the collored lines and. each has a corresponding wieght which is a real number indicating the strensth of the connection between the
nodes. The weight between node I in layer $l$ and node $i$ in $l+1$ is denoted by $\omega_{i j}^{l}$
Data folows from left to right in the network as indicated by the arrow at the top of diagram

The ' $b$ ' node represents a bias node which takes no input but has a constant out put.
Now the input from layer $l$ to layer $l+1$ at node $i$ is defined by the linear function
(1) $\quad I_{i}^{l+1} \quad \sum_{j} \omega_{i j}^{l} O_{j}^{l}+b_{i}^{l}$

Where $O_{j}^{0}$ is the output of node $j$ in layer $l$ and by the bias. To define $O_{i}^{p}$ the adivation function must be specified.

Typical activation functions are the logistic function
(2) $\quad a(x)=\frac{1}{1+e^{-x}}$
$a(0)=12, x \rightarrow \infty \Rightarrow a(x) \rightarrow 1$
and $x \rightarrow-\infty=G(x) \rightarrow 0$
Another is the hyperbolic tangent
(3) $\quad a(x)=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$
$a(0)=0, x \rightarrow \infty \Rightarrow a(x) \rightarrow 1$
and $x \rightarrow-\infty=a(x) \rightarrow-1$
As a final example the rectified linear function

$$
a(x)=\max (0, x)
$$

Now the sutput of node $i$ in layer $y$ is defined by

$$
O_{i}^{l}=a\left(I_{i}^{l}\right)
$$

If the 3 layer network defined at the besining of this section is considered where $O_{i}^{\prime}$ is assumed given equation (1) becomes

$$
I_{i}^{2}=\sum_{j} \omega_{i j}^{\prime} \Delta_{j}^{\prime}
$$

using matrix notation

$$
\left(\begin{array}{l}I_{1}^{2} \\ I_{2}^{2} \\ I_{3}^{2}\end{array}\right)=\left(\begin{array}{llll}\omega_{11}^{\prime} & \omega_{12}^{\prime} & \omega_{13}^{\prime} & \omega_{14}^{\prime} \\ \omega_{21}^{\prime} & \omega_{22}^{\prime} & \omega_{23}^{\prime} & \omega_{21}^{\prime} \\ \omega_{31}^{\prime} & \omega_{32}^{\prime} & \omega_{33}^{\prime} & \omega_{34}^{\prime}\end{array}\right)\left(\begin{array}{l}0_{1}^{\prime} \\ 0_{2}^{\prime} \\ 0_{3}^{\prime} \\ 0_{4}^{\prime}\end{array}\right)
$$

(4) $\quad \Rightarrow I^{2}=\omega^{\prime} 0^{\prime}$

Next

$$
O_{i}^{2}=a\left(I_{i}^{2}\right)
$$

and

$$
I_{i}^{3}=\sum_{j} \omega_{i j}^{2} o_{j}^{2}+b_{i}^{2}
$$

In matrix form

$$
\binom{I_{1}^{3}}{I_{2}^{3}}=\left(\begin{array}{lll}\omega_{11}^{2} & \omega_{12}^{2} & \omega_{13}^{2} \\ \omega_{21}^{2} & \omega_{22}^{2} & \omega_{23}^{2}\end{array}\right)\left(\begin{array}{l}0_{1}^{2} \\ 0_{2}^{2} \\ 0_{3}^{2}\end{array}\right)+\binom{b_{1}^{2}}{b_{1}^{2}}$
(5) $\Rightarrow \quad I^{3}=\omega^{2} 0^{2}+B^{2}
$$

and the output of the network at kyer 3 will be

$$
O_{i}^{3}=Q\left(I_{i}^{3}\right)
$$

This process is referred to as forward propogation.

## Back prepagation

Consider a feedforward layeved neural network with $n$ layers Assume a traing set is avialable which means $O^{\prime}$ and $O^{n}$ are known.

## Inverse CDF Sampling

For a continuous PDF the CDF is defined by

$$
F_{\bar{x}}(x)=S^{x} f_{x}(t) d t=P(\bar{x} \leqslant x)=V
$$

Here $f_{\underline{X}}(x) \geqslant 0 \quad \forall x, 0 \leqslant F_{\bar{X}}(x) \leqslant 1$ $\forall x, 0 \leqslant u \leqslant 1$ and $F_{\bar{x}}(x)$ is monitonically increasing
Assume that $F_{I}(x)$ is invertable so that

$$
F_{X}(x)=v \quad \Rightarrow \quad x=F_{X}^{-1}(v)
$$

If I assumed to be a random variable

$$
F_{\bar{I}}(v)=\int^{v} f_{\bar{I}}(\omega) d \omega
$$

making a change of variables

$$
V=F_{\bar{X}}(x)
$$

and assuming $F_{\bar{x}}(x)$ is monotonically increasing gives

$$
\begin{aligned}
d v&=\frac{d F_{\bar{X}}(x) d x}{d x} \\
& =f_{\bar{X}}(x) d x \\
F_{\bar{I}}(v)&= \int_{f_{\bar{I}}(v)} d v^{v} \\
&= \int_{\bar{I}(x)}^{F_{\bar{I}}} f_{\bar{I}}(v) d v \\
&= S^{x} f_{\bar{I}}\left(F_{\bar{I}}(t)\right) f_{\bar{X}}(t) d t \\
\end{aligned}
$$

if $\nabla$ is uniform $f_{\bar{I}}\left(F_{\bar{I}}(t)\right)=1$ and $F_{\bar{I}}(v)= S^{x} f_{\bar{I}}(t) d t=F_{\bar{I}}(x)$

The Inverse CDF can be summarized as follows

1) Generate a uniform $v$
2) $x=F_{X}^{-1}(v)$
3) I will then have densily f_{X}(x)

As an example consider the exponential distribution

$$
\begin{aligned}
f_{\bar{I}}(x) & =\alpha e^{-\alpha x} \\
F_{\bar{X}}(x) & =\int_{0}^{x} f_{\bar{X}}(t) d t \\
& =\alpha \int_{0}^{x} e^{-\alpha t} d t \\
& =\left.\alpha\left(-\frac{1}{\alpha}\right) e^{-\alpha t}\right|_{0} ^{x} \\
& =-\left(e^{-\alpha t}-1\right) \\
& =1-e^{-\alpha x}
\end{aligned}
$$

so using $v=F_{Z}(x)$ gives

$$
\begin{aligned}
v&=1-e^{-\alpha x} \Rightarrow e^{-\alpha x}=1-v \\
\Rightarrow e^{\alpha x}&=\frac{1}{1-v} \\
\Rightarrow x=&\frac{1}{\alpha} \ln \left(\frac{1}{1-v}\right)=F_{\underline{\underline{x}}}^{-1}(v)
\end{aligned}
$$

## Rejection Sampling

The Rejection Sampling algorithm is used to generale samples of a random variable $\underline{I}$ with distribution $F$.
It can be summarizd as follows.

1) Eenerate a random variable
2) Generale a uniform random variable a independent of
3) If

$$
\underline{u} \leqslant \frac{f(\bar{y})}{c g(\bar{y})}
$$

then "accept" I and set $\bar{X}=7$. If the inequality is not satisfied "reject" $I$.
Here $A$ is assumed that
$0 \leqslant \frac{f(\eta)}{c_{g}(\bar{y})} \leqslant 1$
where $c$ is a constant chosen such that the inequality is satisfied.

* Let $N$ be the number of terations required to generate an X. $N$ is a random variable. The probability of accepting II is given by

$$
p=\frac{f(I)}{C_{g}(I)}
$$

and the probability of "accepting" $\mathbb{Z}$ in $N$ rerations is geometric

$$
P(N=n)=(1-p)^{n-1} p \quad n \geqslant 1
$$

Here a success after $n$ tries will occur after n-1 failures.

The average value of $N$ is given by

$$
\begin{aligned}
\left.E^{[ } N\right] & =\sum_{n=1}^{\infty} n(1-p)^{n-1} p \\
& -p \sum_{n=1}^{\infty} \frac{d}{d p}(1-p)^{n}
\end{aligned}
$$

$$
=-P \frac{d}{d p} \sum_{n=1}^{\infty}(1-p)^{n}
$$

Now

$$
\begin{aligned}
& \sum_{n=1}^{\infty}(1-p)^{n}=\sum_{n=0}^{\infty}(1-p)^{n}-1 \\
& =\frac{1}{p}-1
\end{aligned}
$$

50

$$
\begin{aligned}
E[N] & =\sum_{n=1}^{\infty}(1-P)^{n-1} P \\
& =-P \frac{d}{d P}\left(\frac{1}{P}-1\right) \\
& =-P\left(\frac{-1}{P^{2}}\right)=\frac{1}{P}
\end{aligned}
$$

* If $\bar{A}$ and $\bar{U}$ are independent random variables and $\underline{u}$ is uniform with $0 \leqslant Q \leqslant 1$ and $0 \leqslant \bar{A} \leqslant 1$. Show that

$$
P(\bar{u} \leqslant \bar{A})=E[\bar{A}]
$$

Let $f_{\bar{A}}(a)$ and $f_{\bar{I}}(u)$ be the densities of $I$ and a respectively
Since $\bar{A}$ and $\underline{a}$ are independent the joint density is

$$
f_{\bar{A} \underline{a}}(a, u)=f_{\bar{a}}(a) f_{\underline{a}}(u)
$$

So

$$
\begin{aligned}
& P(\overline{\underline{u}} \leqslant \bar{I})=\int_{0}^{1} \int_{0}^{a} f_{\bar{I} \bar{U}}(a, u) d u d a \\
& =\int_{0}^{1} \int_{0}^{a} f_{\bar{A}}(a) f_{\bar{U}}(u) d u d a \\
& =\int_{0}^{1} f_{\bar{E}}(a) \int_{0} f_{\bar{L}}(u) d u d a
\end{aligned}
$$

since $f_{\underline{u}}(w)$ is uniform

$$
\int_{0}^{a} f_{\underline{\square}}(u) d u=a
$$

50

$$
P(\bar{u} \leqslant A)=\int_{0}^{1} a f_{\bar{A}}(a) d a=E[\mathbb{A}]
$$

* Show that the probability of "accepting" a I sample

$$
P(\text { accept })=\frac{1}{c}
$$

Recall that

$$
P(\text { accept })=P[\underline{u} \leqslant f(\Xi) / c g(1)]
$$

using the previous result gives

$$
\begin{aligned}
& P\left[\underline{u} \leqslant f(\underline{y}) l_{C g}(\underline{y})\right]=E\left[f(\underline{y}) l_{C g}(\bar{y})\right] \\
= & \int \frac{f(y)}{C g(y)} g(y) d y \\
= & \int \frac{f(y)}{C} d y=\frac{1}{C} \int f(y) d y \\
= & \frac{1}{C}
\end{aligned}
$$

* Snow that rejection samplins works, namely,

$$
P[\underline{I} \leqslant y \mid \bar{u} \leqslant f(\bar{I}) / C g(\underline{I})]=F(\bar{I})
$$

Now using Bayes Theorem

$$
\begin{aligned}
& P[\bar{I} \leqslant y \mid \bar{u} \leqslant f(\bar{y}) / c g(\bar{y})] \\
& =\frac{P[\bar{u} \leqslant f(\bar{y}) \operatorname{cg}(\bar{y}) \mid \bar{I} \leqslant y] P[\bar{I} \leqslant y]}{P[\bar{a} \leqslant f(\bar{y}) / c g(Y)]}
\end{aligned}
$$

It was previously shown that

$$
P[a \leqslant f(\bar{y}) / \operatorname{cg}(\bar{y})]=\frac{1}{c}
$$

and by definition

$$
P[\bar{Y} \leqslant y]=G(\bar{Y})
$$

Now

$$
\begin{aligned}
& P\left[\bar{u} \leqslant f(\bar{y}) / c_{g}(\bar{I}) \mid \bar{I} \leqslant y\right] \\
& =\frac{P[\bar{u} \leqslant f(\eta) / c g(\bar{I}), \bar{I} \leqslant y]}{P[\bar{I} \leqslant y]}
\end{aligned}
$$

obtained from using Bayes Theorem.

$$
\begin{aligned}
& P[\bar{a} \leqslant f(\bar{y}) \log (\bar{y}), \bar{I} \leqslant y] \\
& =\int_{0}^{y} \int_{0}^{f(y) \log (y)} f_{\underline{u} \underline{I}}(u, w) d u d w
\end{aligned}
$$

Since I and I are independent

$$
f_I(u, y)=f(u) g(y)
$$

But $\bar{u}$ is uniform so

$$
f_{\square}(u)=1
$$

$$
\begin{aligned}
P\left[\bar{u} \leqslant P(\bar{y}) / C_{g}(\underline{z}), \underline{\bar{y}} \leqslant y\right]
&=\int^{y} \int_{0}^{f(y) \log (y)}(1) g(y) d y \\
&=\int^{y} \frac{f(\omega)}{c g(\omega)} g(\omega) d \omega=\frac{1}{c} S^{y} f(\omega) d \omega \\
&=\frac{F(y)}{c}
\end{aligned}
$$

so bringing thigs together

$$
\begin{aligned}
P\left[\bar{u} \leqslant f(\bar{y}) / c_{g}(\bar{y}) \mid \bar{I} \leqslant y\right] 
& =\frac{P[\bar{u} \leqslant f(\bar{I}) / c g(\bar{I}), \bar{I} \leqslant y]}{P[\bar{I} \leqslant y]} \\
& =\frac{F(y)}{c \in(y)}
\end{aligned}
$$

The desired probability the demonstrated that the agory thm works is

$$
\begin{aligned}
& P[\bar{I} \leqslant y \mid \bar{u} \leqslant f(\bar{I}) / C g(\bar{I})] \\
= & \frac{P[\bar{u} \leqslant f(\bar{Y}) / C g(\bar{I})[\bar{I} \leqslant y] P[\bar{I} \leqslant y]}{P[\bar{a} \leqslant f(\bar{Y}) / C g(\bar{I})]} \\
= & \frac{F(y)}{C \in(y)} \frac{C(y)}{1 / 6}=F(y)
\end{aligned}
$$

which is the desired result

## Markov Chains

Consider a system that is represented by a random varicable $\bar{x}_{t}$ that can take on a finite number values denoted by $x_{1}, x_{2}, \ldots, x_{n}$. Here $t$ is assume to represent time and takes on the values $0,1,2, \ldots$,
It is also assumed that the probability that $I_{t}$ has a vclue $s_{t+1}$ at $t+1$ onk depends on the value at time $t$, namely

$$
P\left(\bar{X}_{t+1}=s_{t+1} \mid \bar{X}_{t}=s_{t}, \bar{X}_{t-1}=s_{t-1}, \ldots,
X_{0}=s_{0}\right)
=P\left(\bar{X}_{t+1}=s_{t+1} \mid \quad \bar{X}_{t}=s_{t}\right)
$$

since a Markou process only depends on the previous value

$$
P\left(X_{t+1}=s_{t+1} \mid X_{t}=s_{t}\right)
$$

can be represented by a matrix

$$
P_{i j}=P\left(X_{t+1}=j \mid X_{t}=i\right)
$$

$P_{ij}$ will be a square $n \times n$ matrix since the trarsitions will be betwer the $n$ possible values of $x$, namely, $x_{1}, x_{2}, x_{3}, \ldots, x_{n}$. The rows of ' $P_{i j}$ ' represent the value of $x$ at $t$ and the columns the value at $t+1$. Since $x$ must take on one of the values $x_{1}, x_{2}, \ldots, x_{n}$ it follows that

$$
\sum_{j=1}^{n} P_{i j}=1
$$

Recall that

$$
\begin{aligned}
P_{i j} & =P\left(\bar{X}_{1}=j \mid \bar{X}_{0}=i\right) \\
& =P\left(\bar{X}_{t}=j \mid \bar{X}_{t-1}=i\right)
\end{aligned}
$$

Thus $P_{i j}$ contains the probabilities for all. single step transitions from $i$ to $j$

* what is the probability of transitioning from $i$ to $j$ in two steps

The desired probability is

$$
P\left(\bar{X}_{2}=j \mid \bar{X}_{0}=i\right)
$$

Now from the law of Total Probability

$$
\begin{aligned}
& P\left(\bar{X}_{2}=j \mid \bar{X}_{0}=i\right) \\
& =\sum_{k} P\left(X_{2}=j \mid X_{0}=i, \bar{X}_{1}=k\right) P\left(X_{1}=k \mid X_{0}=i\right)
\end{aligned}
$$

But from the Markou properly

$$
\begin{aligned}
& P\left(\underline{X}_{2}=j \mid \bar{X}_{0}=i, \bar{X}_{1}=k\right)=P\left(\bar{X}_{2}=j \mid \bar{X}_{1}=k\right) \\
& \text { so } \\
& P\left(\bar{X}_{2}=j \mid \bar{X}_{0}=i\right) \\
= & \sum_{k} P\left(\bar{X}_{2}=j \mid \bar{X}_{1}=k\right) P\left(\bar{X}_{1}=k \mid \bar{X}_{0}=i\right) \\
= & \sum_{k} P_{k j} P_{i k} \\
= & \sum_{k} P_{i k} P_{k j} \\
= & \left(P^{2}\right)_{i j}
\end{aligned}
$$

## Similarly for a 2 slep difference after $n$ sleps

$$
\begin{aligned}
& P\left(\bar{X}_{n+2}=j \mid \bar{X}_{n}=i\right) \\
= & \sum_{k}\left\{P\left(\bar{X}_{n+2}=j \mid \bar{X}_{n}=i, \bar{X}_{n+1}=k\right)\right. \\
& \left.P\left(\bar{X}_{n+1}=k \mid \bar{X}_{n}=i\right)\right\} \\
= & \sum_{k} P\left(\bar{X}_{n+2}=j \mid \bar{X}_{n+1}=k\right) P\left(\bar{X}_{n+1}=k \mid \bar{X}_{n}=i\right) \\
= & \sum_{k} P_{k j} P_{i k}=\sum_{k} P_{i k} P_{k j} \\
= & \left(P^{2}\right)_{i j}
\end{aligned}
$$

Summarizing these results

$$
\begin{aligned}
P_{i j}&=P\left(\bar{X}_{n+1}=i \mid \bar{X}_{n}=j\right) \\
\left(P^{2}\right)_{i j}&=P\left(\bar{x}_{n+2}=j \mid \bar{x}_{n}\right) \\
\end{aligned}
$$

Now for an arbitray $t$ step difference Indection can be used to show

$$
\left(P^{t}\right)_{i j}=P\left(\bar{X}_{n+t}=j \mid \underline{X}_{n}\right)
$$

Previously it was shown that

$$
\begin{array}{ll}
t=1 & P_{i j}=P\left(\bar{X}_{n+1}=j \mid \bar{X}_{n}=i\right) \\
t=2 & \left(P_{i j}\right)^{2}=P\left(\bar{X}_{n+2}=j \mid \bar{X}_{n}=i\right)
\end{array}
$$

The induction hypotheses asscomes

$$
P\left(X_{n+t}=j \mid \bar{X}_{n}=i\right)=\left(P^{t}\right)_{i j}
$$

so for $t+1$

$$
\begin{aligned}
P & \left(\bar{X}_{n+t+1}=j \mid X_{n}=i\right) \\
= & \sum_{k}\left\{P\left(\bar{X}_{n+t+1}=j \mid \bar{X}_{n}=i, \bar{X}_{n+t}=k\right)\right. \\
& \left.P\left(\bar{X}_{n+t}=k \mid \bar{X}_{n}=i\right)\right\} \\
= & \sum_{k}\left\{P\left(\bar{X}_{n+t+1}=j \mid \bar{X}_{n+t}=k\right)\right. \\
& \left.P\left(\bar{X}_{n+t}=k \mid \bar{X}_{n}=i\right)\right\} \\
= & \sum_{k} P_{k j}\left(P^{t}\right)_{i k}= \\
= & \sum_{k}\left(P^{t}\right)_{i k} P_{k j}=\left(P^{t+1}\right)_{i j}
\end{aligned}
$$

This completes the proof.

## Markov Chain Equilibrium Distribution

Let $\left\{\bar{I}_{0}, \underline{X}_{1}, \underline{X}_{2}, \ldots, \bar{X}_{N}\right\}$ be a Markov Chain with State spoce $S=\{1,2,3, \ldots, N\}$

Now the $\bar{X}_{t}$ are random variables. The probability distribution of $\bar{X}_{t}$ can be represented by a column vector.
For $\underline{X}_{0}$,

$$
\pi=\left(\begin{array}{c}
\pi_{1} \\
\pi_{2} \\
\vdots \\
\pi_{N}
\end{array}\right)=\left(\begin{array}{c}
P\left(\bar{x}_{0}=1\right) \\
P\left(\bar{x}_{0}=2\right) \\
\vdots \\
P\left(\bar{x}_{0}=N\right)
\end{array}\right)
$$

It represents the probabability that I $X_{0}$ has value $n \in S$.

What is the probability distribution of $\bar{X}_{1}$ ? Using the law of Total Probability

$$
\begin{aligned}
P\left(X_{1}=j\right) & =\sum_{i} P\left(X_{1}=j \mid X_{0}=i\right) P\left(X_{0}=i\right) \\
& =\sum_{i} P_{i j} \pi_{i} \\
& =\sum_{i} \pi_{i} P_{i j} \\
& =\left(\pi^{\top} P\right)_{j}
\end{aligned}
$$

Similarly for $\bar{X}_{2}$

$$
\begin{aligned}
P\left(\bar{X}_{2}=j\right) & =\sum_{i} P\left(\bar{X}_{2}=j \mid \bar{X}_{1}=i\right) P\left(\bar{X}_{1}=i\right) \\
& =\sum_{i} P_{i j}\left(\pi^{\top} P\right)_{i} \\
& =\sum_{i}\left(\pi^{\top} P\right)_{i} P_{i j} \\
& =\sum_{i} \sum_{k} \pi_{k} P_{k i} P_{i j} \\
& =\sum_{k} \sum_{i} \pi_{k} P_{k i} P_{(j)} \\
& =\sum_{k} \pi_{k} \sum_{i} P_{k i} P_{i j} \\
& =\sum_{k} \pi_{k}\left(P^{2}\right)_{k J} \\
& =\left(\pi^{\top} P^{2}\right)_{1}$
\end{aligned}
$$

The distribution of $\bar{X}_{t}$ can be shown to be

$$
P\left(\bar{x}_{t}=j\right)=\left(\pi^{\top} P^{t}\right)_{j}
$$

where

$$
P\left(\bar{x}_{0}=j\right)=\pi_{j}
$$

It has been shown that

$$
P\left(Z_{1}=j\right)=\left(\pi^{\top} P\right)_{j}
$$

The induction assumption is

$$
P\left(\bar{x}_{i}=j\right)=\left(\pi^{\top} p^{t}\right)_{j}
$$

SO

$$
\begin{aligned}
& P\left(\bar{X}_{t+1}=j\right)=\sum_{i} P\left(\bar{X}_{t+1}=j \mid X_{t}=i\right) P\left(X_{t}=i\right) \\
&= \sum_{i} P_{i j}\left(\pi^{T} P^{t}\right)_{i} \\
&= \sum_{i}\left(\pi^{T} P^{t}\right)_{i} P_{i j} \\
&= \sum_{i} \sum_{k} \pi_{k}\left(P^{t}\right)_{k i} P_{i j} \\
&= \sum_{k} \pi_{k} \sum_{i}\left(P^{t}\right)_{k i} P_{i j} \\
&= \sum_{k} \Pi_{k}\left(P^{t+1}\right)_{k j} \\
&= \Pi^{T}\left(P^{t+1}\right)_{j} \\
\end{aligned}
$$

This completes the proof. Equilibrium The equillibrium distribution of 部tor a is defined by

$$
\pi_{E}^{\top}=\pi_{E}^{\top} P^{t} \quad \forall t=1,2,3, \ldots
$$

That is $\pi_{E}^{\top}$ is the same for all values of $t$. It is casy to verify that

$$
\pi_{E}^{T}=\pi_{E}^{T} P
$$

is an equilibrium distribution.

$$
\begin{aligned}
\pi_{E}^{T} P^{t} & =\pi_{E}^{T} P P^{t-1}=\pi_{E}^{T} P^{t-1} \\
& =\pi_{E}^{T} P P^{t-2}=\pi_{E}^{T} P^{t-2} \\
& =\cdots \\
& =\pi_{E}^{T} P=\pi_{E}^{T}
\end{aligned}
$$

$\pi_{E}^{\top}$ must salisty the following conditions ,

1) $\quad \pi_{E}^{\top}=\pi_{E}^{\top} P \quad \forall t=1,2,3, \ldots$
2) $\sum_{i} \Pi_{\bar{E}_{i}}^{\top}=1$
3) $\quad \pi_{E_{i}}^{\top} \geqslant 0 \quad \forall \quad i$

conditions 2 and 3 state that $\pi E$ is a probability distribution.

Condition 1 specifies $\prod_{E}^{\top}$ up to a scalor multiplicative constant. Conditions 2 and 3 are used to determine the constant.
Now starting with

$$
\begin{aligned}
& \pi_{E}^{\top}=\pi_{E}^{\top} P \\
& \Rightarrow \pi_{E j}=\sum_{i} \pi_{E i} P_{i j} \\
\end{aligned}
$$

using $P_{i j}=P_{j i}^{\top}$ gives

$$
\begin{aligned}
& \Rightarrow \pi_{E j}=\sum_{i} \pi_{E i} P_{j i}^{T}=\sum_{i} P_{j i}^{T} \pi_{E i} \\
& \Rightarrow \pi_{E}=P^{T} \pi_{E}
\end{aligned}
$$

## Example

Consider the simple 2 slate Markow chain
![](https://cdn.mathpix.com/cropped/2025_09_18_4a3a8c593a89973bc7c8g-065.jpg?height=281&width=806&top_left_y=853&top_left_x=267)
which has the fransition matrix

$$
P=\left(\begin{array}{ll}
0.7 & 0.3 \\
0.4 & 0.6
\end{array}\right)
$$

The equilibrium distribution is given by

$$
\Pi_{E}^{\top}=\Pi_{E}^{\top} P, \quad \sum_{i} \Pi_{E i}^{\top}=1
$$

$$
\Rightarrow \Pi_{E}^{\top}(P-\mathbb{1})=0
$$

Where 11 is the identity matix. So

$$
\left(\pi_{E_{1}}, \pi_{E_{2}}\right)\left(\begin{array}{cc}
-0.3 & 0.3 \\
0.4 & -0.4
\end{array}\right)=0
$$

This combined with $\sum_{i} \pi_{E_{i}}=1$ gives the sytem of iequations

$$
\begin{gathered}
-0.3 \pi_{E_{1}}+0.4 \pi_{E_{2}}=0 \\
0.3 \pi_{E_{1}}-0.4 \pi_{E_{2}}=0 \\
\pi_{E_{1}}+\pi_{E_{2}}=1
\end{gathered}
$$

or

$$
\left(\begin{array}{cc}
-0.3 & 0.4 \\
0.3 & -0.4 \\
1 & 1
\end{array}\right) \pi_{E}=\left(\begin{array}{l}
0 \\
0 \\
1
\end{array}\right)
$$

SC

$$
\begin{aligned}
& 0.3 \pi_{E_{1}}=0.4 \pi_{E_{2}} \\
& \Rightarrow \pi_{E_{2}}=\frac{3}{4} \pi_{E_{1}}
\end{aligned}
$$

using

$$
\begin{aligned}
& \pi_{E_{1}}+\pi_{E_{2}}=1 \\
\Rightarrow & \frac{3}{4} \pi_{E_{1}}+\pi_{E_{1}}=1 \\
\Rightarrow & \pi_{E_{1}}(3 / 4+1)=1 \\
\Rightarrow & \pi_{E_{1}} 7 / 4=1 \\
\Rightarrow & \pi_{E_{1}}=\frac{4}{7} \\
\Rightarrow & \pi_{E_{2}}=\left(\frac{3}{4}\right) \pi_{E_{1}}=\left(\frac{3}{4}\right)\left(\frac{4}{7}\right)=\frac{3}{7}
\end{aligned}
$$

50

$$
\pi_{E}^{T}=(4 / 7,3 / 7)
$$

## Markou Chain Equilibrium Linear Dependence

The Markou Chain Equilibrium distribution $\pi_{E}$ is defined as the solution to

$$
\pi_{E}^{\top}(P-\mathbb{1})=0
$$

where

$$
\sum_{i}\left(\pi_{E}\right)_{i}=1 \quad \sum_{j} P_{i j}=1
$$

Consider a two state Markou process

$$
P=\left(\begin{array}{ll}
p_{11} & p_{12} \\
p_{21} & p_{22}
\end{array}\right)
$$

50

$$
P-11=\left(\begin{array}{ll}
P_{11}-1 & P_{12} \\
P_{21} & P_{22}-1
\end{array}\right)
$$

but

$$
P_{11}-1=-P_{12} \quad P_{22}-1=-P_{21}
$$

so

$$
P-11=\left(\begin{array}{cc}
-P_{12} & P_{12} \\
P_{21} & -P_{21}
\end{array}\right)
$$

and

$$
\begin{aligned}
& \pi^{\top}(P-\underline{1})=\left(\pi_{1} \pi_{2}\right)\left(\begin{array}{ll}
-P_{12} & P_{12} \\
P_{21} & -P_{21}
\end{array}\right) \\
& \Rightarrow \quad-\pi_{1} P_{12}+\pi_{2} P_{21}=0 \\
& \quad \pi_{1} P_{12}-\pi_{2} P_{21}=0
\end{aligned}
$$

Which are linearly dependent since the bottom equation can be multipied by 11 to obtain the to.

Gonsider the three state Markov Chain

$$
P=\left(\begin{array}{lll}
p_{11} & p_{12} & p_{13} \\
p_{21} & p_{22} & p_{23} \\
p_{31} & p_{32} & p_{33}
\end{array}\right)
$$

$$
P-\underline{\mathbb{1}}=\left(\begin{array}{lll}
P_{11}-1 & P_{12} & P_{13} \\
P_{21} & P_{22}-1 & P_{23} \\
P_{31} & P_{32} & P_{33}-1
\end{array}\right).
$$

Now

$$
\begin{aligned}
& P_{11}-1=-P_{12}-P_{13} \\
& P_{22}-1=-P_{21}-P_{23} \\
& P_{33}-1=-P_{31}-P_{32}
\end{aligned}
$$

$$
\begin{gathered}
\pi_{T}(P-11)=\left(\pi_{1} \pi_{2} \pi_{3}\right)\left(\begin{array}{lll}
-P_{12}-P_{13} & P_{2} & P_{13} \\
P_{21} & -P_{21}-P_{23} & P_{23} \\
P_{31} & P_{32}-P_{31}-P_{32}
\end{array}\right) \\
-\pi_{1}\left(P_{12}+P_{13}\right)+\pi_{2} P_{21}+\pi_{3} P_{31}=0 \\
=\pi_{1} P_{12}-\pi_{2}\left(P_{21}+P_{23}\right)+\pi_{3} P_{32}=0 \\
\pi_{1} P_{13}+\pi_{2} P_{23}-\pi_{3}\left(P_{31}+P_{32}\right)=0
\end{gathered}
$$

Adding the top two equations gives

$$
-\pi_{1} P_{13}-\pi_{2} P_{23}+\pi_{3}\left(P_{31}+P_{32}\right)=0
$$

Multiplying this equation by (-1) produces the bottom equation so the system is linearly dependent
For an $N$ state

$$
\pi^{\top}(P-\underline{\mathbb{1}})=\left(\Pi_{1} \Pi_{2} \ldots \Pi_{N}\right)
$$

$$
\left(\begin{array}{cccc}
P_{11}-1 & P_{12} & \cdots & P_{1 N} \\
P_{21} & P_{22}-1 & \cdots & P_{2 N} \\
\vdots & & & \\
P_{N 1} & P_{N 2} & \cdots & P_{N N}-1
\end{array}\right)=0
$$

$\Rightarrow\left[\pi^{\top}(P-\underline{\mathbb{I}})\right]_{j}=\sum_{i} \pi_{i}\left(P_{i j}-\delta_{i j}\right)=0$
To prove linear dependence it must be shown that one of the equations can be eliminated by linear row manipulations. It will be shown

$$
\begin{aligned}
\sum_{i}^{N} \pi_{i}\left(P_{i N}-\delta_{N N}\right) & =-\sum_{K}^{N-1} \frac{N}{2} \pi_{i}\left(P_{i k}-\delta_{i k}\right) \\
\Rightarrow & \left(P_{i N}-\delta_{N N}\right)=-\sum_{K}^{N-1}\left(P_{i k}-\delta_{i k}\right)
\end{aligned}
$$

Now from definition of stochastic matrix

50

$$
\begin{aligned}
& \sum_{j} P_{i j}=1 \\
=\rightarrow & P_{i l}=1-\sum_{j \neq i}^{N} P_{i j} \\
=> & P_{i c}-1=-\sum_{j \neq i}^{N} P_{i j} \\
P_{N N^{-}} 1 & =-\sum_{k} P_{i k}
\end{aligned}
$$

and for $i<N$

$$
\begin{aligned}
& P_{i i}-1=\sum_{k \neq i}^{N-1} P_{i k}-P_{i N} \\
\end{aligned}
$$

for i=1

$$
\begin{aligned}
& \sum_{k}^{N-1}\left(P_{1 k}-\delta_{i k}\right)=P_{11}-1+P_{12}+P_{13}+\cdots+P_{1, N-1}
\end{aligned}
$$

$$
\begin{aligned}
& =-\left(P_{12}+P_{13}+\cdots+P_{1 N}\right)+P_{12}+P_{13}+\cdots+P_{1, N-1} \\
& =-P_{1 N}
\end{aligned}
$$

for $i<N$
N-I

$$
\begin{aligned}
& \sum_{k}\left(P_{i k}-S_{i k}\right)=P_{i 1}+P_{i 2}+\cdots+\left(P_{i i}-1\right) \\
& +P_{i, N-1} \\
& =P_{i 1}+P_{i 2}+\cdots-\left(P_{i 1}+P_{i 2}+\cdots+P_{i, i-1}+\right. \\
& \left.P_{i, i+1}+\cdots+P_{i, N-1}+P_{i N}\right)+P_{i, N-1} \\
& =-P_{i N}
\end{aligned}
$$

for $i=N$

$$
\sum_{k}^{N-1}\left(P_{N K}-\delta_{N K}\right)=\sum_{k}^{N-1} P_{N K}=1-P_{N N}
$$

Thus

$$
\left(P_{i N}-\delta_{i N}\right)=-\sum_{k}^{N-1}\left(P_{i k}-\delta_{i k}\right)
$$

Markou Chain Transition Matrix Diagonalization
The Markov chain equilibrium distribution is defined by

$$
\Pi_{E}^{\top}=\Pi_{E}^{\top} P^{t} \quad \forall t \geqslant 0 \quad I
$$

and satisfies the following
additional conditions

1) $\Pi_{E}^{\top}=\Pi_{E}^{\top} P$
2) $\prod_{E}^{\top} \prod_{E}=l$
3) $\pi_{E i} \geqslant 0 \quad \forall i$

Condition 1) can be shown
to be the solution to
equation I and conditons
2 and 3 define $\pi_{E}$ as a
probability distribution.
The Markov Chain Transition
Matrix satisfies the following conditions

1) $P_{i j} \geqslant 0 \quad \forall i, j$
2) $\sum_{j} P_{i j}=1$

Condition. D states that the transition matrix elements are nonegative. Condition 2 states that the rows are normalized or that each state of the chain tranistions to a future state with probability 1.

It is furthur assumed that
3) $\left(P^{k}\right)_{i j}>0$
for some $k \geqslant 1$
This states that siven sufficient time all states of Prowill be sampled with probability 1.
These conditions on $P$ are Sufficent to guarantel Convergence to an equillibrum distribution.

Consider an eigenvalue and
eigenveetor of $p$ eigenvetor of $P$

$$
\begin{aligned}
& P x=\lambda x \\
\Rightarrow & P^{n} x=\lambda^{n} x
\end{aligned}
$$

Since $p^{n}$ is also a transition matrix beteen states seperated by $n$ iteretions

$$
\begin{aligned}
& 0<\left(P^{n}\right)_{i j}<1 \\
& \sum_{j}\left(P^{n}\right)_{i j}=1
\end{aligned}
$$

For the righthard side to remain bounded we must have

$$
\lambda \leqslant 1 \quad \text { II }
$$

Assume that

$$
x=\mathbb{1}
$$

where II is a column vector where all elements are 1. Now

$$
\begin{aligned}
P \underline{1} & \Rightarrow(P \underline{1})_{i}=\sum_{k} P_{i k} \underline{1}_{k} \\
& =\sum_{k} P_{i k}=1
\end{aligned}
$$

which follows from condition 11 for transition matrices.Thus is an eigen value and is an eigenvector.

From the Ferron-Frobenius Theorem and $\lambda \leqslant 1 . \quad \lambda=1$ has multiplicity 1 and is the largest eigenvalue

Let $D$ be the dragonal matrix of eigenudlues

$$
D=\left[\begin{array}{llll}
1 & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{n}
\end{array}\right]
$$

and $E$ be the matrix of eigenvectors as columns

$$
E=\left[\begin{array}{ccccc}
1 & e_{21} & e_{31} & \cdots & e_{n 1} \\
1 & e_{22} & e_{32} & \cdots & e_{n 2} \\
1 & \vdots & \vdots & & \vdots \\
\vdots & e_{2 n} & e_{3 n} & \cdots & e_{n n}
\end{array}\right]
$$

Then

$$
P=E D E^{-1}
$$

and

$$
\begin{aligned}
P^{t} & =\left(E D E^{-1}\right)\left(E D E^{-1}\right) \cdots\left(E D E^{-1}\right) \\
& =E D^{t} E^{-1}
\end{aligned}
$$

Now

$$
D^{t}=\left[\begin{array}{lllll}
1 & & & & \\
& \lambda_{2} & & & \\
& & \lambda_{3} & & \\
& & & \ddots & \\
& & & & \lambda_{n}
\end{array}\right]^{t}
$$

$$
=\left[\begin{array}{lllll}
1 & t & & & \\
& \lambda_{2}^{t} & & & \\
& & \lambda_{3}^{t} & & \\
& & & \ddots & \\
& & & & \lambda_{n}^{t}
\end{array}\right]
$$

But $\lambda_{i}<\mid \forall i>1$ so for large $t$

$$
\lim _{t \rightarrow \infty} \lambda_{c}^{t}=0
$$

So,

$$
\lim _{t \rightarrow \infty} D^{t}=\left[\begin{array}{llll}
1 & & & \\
& 0 & & \\
& & 0 & \\
& & & \ddots \\
& & & 0
\end{array}\right]
$$

and

$$
\lim _{t \rightarrow \infty} P^{t}=E\left[\begin{array}{lllll}
1 & & & & \\
& 0 & & & \\
& & 0 & & \\
& & & \ddots & \\
& & & & 0
\end{array}\right] E^{-1}
$$

Evaluation of the righthand
side gives

$$
\begin{aligned}
& E D^{\infty}=\left[\begin{array}{ccccc}
1 & e_{21} & e_{31} & \cdots & e_{n 1} \\
1 & e_{22} & e_{32} & \cdots & e_{n 2} \\
1 & \vdots & \vdots & & \vdots \\
\vdots & e_{2 n} & e_{3 n} & \cdots & e_{n n}
\end{array}\right] \\
& {\left[\begin{array}{lllll}
1 & & & & \\
& 0 & & & \\
& & 0 & & \\
& & & \ddots & \\
& & & & 0
\end{array}\right]=\left[\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
1 & 0 & & 0 \\
1 & 0 & & 0 \\
\vdots & \vdots & & \vdots \\
1 & 0 & & 0
\end{array}\right]} \\
& \text { let } \\
& E^{-1}=\left[\begin{array}{cccc}
e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\
e_{-21}^{-1} & e_{22}^{-1} & \cdots & e_{2 n}^{-1} \\
\vdots & \vdots & & \\
e_{n 1}^{-1} & e_{n 2}^{-1} & \cdots & e_{n n}^{-1}
\end{array}\right] \\
& \text {then } \\
& E D^{\infty} E^{-1}=\left[\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
1 & 0 & & 0 \\
1 & 0 & & 0 \\
\vdots & \vdots & & \vdots \\
1 & 0 & & 0
\end{array}\right]\left[\begin{array}{cccc}
e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\
e_{-1}^{-1} & e_{22}^{-1} & \cdots & e_{-2 n}^{-1} \\
\vdots & \vdots & & \\
e_{n 1}^{-1} & e_{n 2}^{-1} & \cdots & e_{n n}^{-1}
\end{array}\right] \\
& \Rightarrow\left(E D^{\infty} E^{-1}\right)_{i j}=\sum_{k}\left(E D^{\infty}\right)_{i k} e_{k j}^{-1}
\end{aligned}
$$

## using

$$
\left(E D^{\infty}\right)_{i j}=\delta_{i j}
$$

gives

$$
\begin{aligned}
\sum_{k}\left(E D^{\infty}\right)_{i k} e_{k j}^{-1}
=&\sum_{k} \delta_{1 k} e_{k j}^{-1} \\
=&e_{1 j}^{-1} \\
\Rightarrow &\lim _{t \rightarrow \infty} P^{t}=\left[\begin{array}{cccc}e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\ e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\ \vdots & & & \\ e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1}\end{array}\right]
\end{aligned}
$$

thus all rows are equal to the first row.

Where

$$
\sum_{j} e_{i j}^{-1}=1
$$

If $x$ is an arbitrary normalized column vector

$$
\sum_{i} x_{i}=1
$$

then

$$
\begin{aligned}
x^{\top} P^{-1}=\left[x_{1} x_{2}\right. & \left.\cdots x_{n}\right]\left[\begin{array}{cccc}
e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\
e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1} \\
\vdots & & & \\
e_{11}^{-1} & e_{12}^{-1} & \cdots & e_{1 n}^{-1}
\end{array}\right] \\
\Rightarrow\left(x^{\top} P^{0}\right)_{j} & =\sum_{k} x_{k} e_{11}^{-1} \\
& =e_{1 j}^{-1} \sum_{k} x_{k} \\
& =e_{i 1}^{-1} \\
& =\pi_{1}
\end{aligned}
$$

Trus

$$
\lim _{t \rightarrow \infty} P^{t}=\left[\begin{array}{cccc}
\pi_{1} & \pi_{2} & \cdots & \pi_{n} \\
\pi_{1} & \pi_{2} & \cdots & \pi_{n} \\
\vdots & \vdots & & \\
\pi_{1} & \pi_{2} & \cdots & \pi_{n}
\end{array}\right]
$$

## Continuous state Markou Chains

If the state space of a Markou Process is continuous the transition matrix, $P_{i,}$, used to represent transitions' between states in the discrete case is replaced by the continuous stochastic Kernel $p(x, y)$ where $x$ and $y$ are real numbers $x, y \in \mathbb{R}$. where $x$ represents the state at time $t$ and 1 the state at time $t+1$. Time is still assumed to be discrete with $t=0,1,2, \ldots$

The stochastic Kernel has the following properties

1) $p(x, y) \geqslant 0 \quad \forall \quad x, y$
2) $\int p(x, y) d y=1 \quad \forall x$
where the integral in property 2 is over the entire range of $y$.
for a fixed $x$ indicated by $x_{t} p(x, y)$ can be assumed to be a conditional probability density

$$
p\left(x_{t}, y\right)=f\left(y \mid x_{t}\right)
$$

In general this not the case and probability measures must be used.
In the density case $p(x, y)$ can be viewest as a family of condrional distributions with each $x$ giving the probabitity of a transition from $x$ to $y$ in one time step.
From the Markou condition the current state only depends on the previous stele, so

$$
\begin{aligned}
p\left(x_{t}, y\right)= & f\left(y \mid x_{t}, x_{t-1}, x_{t-2}, \ldots\right) \\
& f\left(y \mid x_{t}\right)
\end{aligned}
$$

The stochastic Kernel after two time steps $t-1, t$

$$
\begin{aligned}
p\left(x_{t-1}, y\right)&=f\left(y \mid x_{t-1}\right) \\
&=\int f\left(y \mid x_{t-1}, x_{t}\right) f\left(x_{t} \mid x_{t-1}\right) d x_{t}
\end{aligned}
$$

using the Morkow property

$$
=\int f\left(y \mid x_{t}\right) f\left(x_{t} \mid x_{t-1}\right) d x_{t}
$$

If $w$ is the value of $y$ at $t$ then

$$
\int f(y \mid \omega) f\left(\omega \mid x_{t-1}\right) d \omega
$$

This is analosous to the matrix product occurring in the descrete state case. If it is denoted
2 is the operator stochastic kennel is given by

$$
p\left(x_{t-1}, y\right)=p(x, y) * p(x, y)=p^{2}(x, y)
$$

The $n$ step stochastic kernel can be found using. The madhematical induction. The induction mpothesis assumes

$$
\begin{aligned}
p\left(x_{t-1}, y\right)&=p^{2}\left(x_{t}, y\right) \\
&=\int f(y \mid \omega) f\left(\omega \mid x_{t-1}\right) d \omega \\
p\left(x_{t-n+1}, y\right)&=p^{n}\left(x_{t}, y\right) \\
& =\iint \cdots \int f\left(y \mid \omega_{1}\right) f\left(\omega_{1} \mid \omega_{2}\right) \cdots f\left(\omega_{n-1} \mid x\right) d \omega_{1} d \omega_{2} \cdots d \omega_{n-1}
\end{aligned}
$$

Now for $n+1$

$$
\begin{aligned}
p\left(x_{t-n}, y\right)&=\int f\left(y \mid x_{t-n}, x_{t-n+1}\right) f\left(x_{t-n+1} \mid x_{t-n}\right) d x_{t-n+1} \\
& =\int f\left(y \mid x_{t-n+1}\right) f\left(x_{t-n+1} \mid x_{t-n}\right) d x_{t-n+1} \\
& =p\left(x_{t-n+1}, y\right) * p\left(x_{t-n}, x_{t-n+1}\right)
\end{aligned}
$$

The righthand side is the one step kernel and the left. is the $n$ step kernel.
So

$$
\begin{aligned}
p\left(x_{t-n}, y\right) & =p^{n}\left(x_{t}, y\right) * p\left(x_{t}, y\right) \\
& =p^{n+1}\left(x_{t}, y\right)
\end{aligned}
$$

## Continuous State Marka Chain

## Equilibrium Distribution

Let $\left\{x_{0}, x_{1}, x_{2}, \ldots, x_{n}\right\}$ indicate the sequence, of states produced by successive application of the Stochcstic kernel $\rho(x, y)$
Let $\Pi(x)$ represent the distribution of the sequence of states, where

$$
\begin{aligned}
& \text { 1) } \quad \pi(x) \geqslant 0 \quad \forall x \\
& \text { 2) } \quad \int \pi(x) d x=1
\end{aligned}
$$

Let $\Pi_{0}(x)$ indicate the intial distribution which can be any function satisty ins condions 1 and 2 . The distributial of states after one application of $p(x, y)$

$$
\pi_{1}(y)=\int p(x, y) \pi_{0}(x) d x
$$

if $t$ is an arbitrary step in the sequence then

$$
\pi_{t+1}(y)=\int p(x, y) \pi_{t}(x) d x
$$

The righthand side can be represented by the linear operator

$$
(\pi P)(y)=\int P(x, y) \pi(x) d x
$$

$P$ is called the Markou operator.
Pis applied to the distribution
$\pi_{t}(x)$ produce $\pi_{t+1}(x)$.
The distribution obtained after 2 applications of the stochastic kernel is

$$
\begin{aligned}
& \pi_{2}(y)=\int p(x, y) \pi_{1}(x) d x \\
& =\int p(x, y)\left[\int p(\omega, x) \pi_{0}(\omega) d \omega\right] d x \\
& =\iint p(x, y) p(\omega, x) \pi_{0}(\omega) d \omega d x \\
& =\left(\pi P^{2}\right)(y)
\end{aligned}
$$

after $t$ steps

$$
\begin{aligned}
\pi_{t}(y)&=\int p(x, y) \pi_{L-1}(x) d x \\
&=\iint p(x, y) p(\omega, x) \pi_{t-2}(\omega) d \omega d x
\end{aligned}
$$

following this procechere $t$ times will give

$$
\begin{aligned}
\pi_{t}(y)&=\int S \cdots S p\left(\omega_{t-1}, y\right) p\left(\omega_{t-2}, \omega_{t-1}\right)
\cdots p\left(\omega_{0}, \omega_{1}\right) \pi_{0}\left(\omega_{0}\right) d \omega_{t-1} d \omega_{t-2} d \omega_{0} \\
&=\left(\pi_{0} P^{t}\right)(y)
\end{aligned}
$$

Here, $\pi_{0}(x)$ is the initial distribution

In general it is easy to see that.

$$
\pi_{t+n}(y)=\left(\pi_{t} P^{n} x_{y}\right)
$$

* The equilbrium distribution is defined by

$$
\pi_{E}(y)=\left(\pi_{E} P^{n}\right)(y) \quad \forall \quad n=0,1,2, \ldots
$$

A solution is

$$
\begin{aligned}
\pi_{E}(y) & =\left(\pi_{E} P\right)(y) \\
& =\int P(x, y) \pi_{E}(x) d x
\end{aligned}
$$

which is easy to verify

$$
\begin{aligned}
\left(\pi_{E} P^{t}\right)(y)&=\int S \cdots S p\left(\omega_{t-1}, y\right) p\left(\omega_{t-2}, \omega_{t-1}\right)
\left(\omega_{0}, \omega_{1}\right) \pi_{E}\left(\omega_{0}\right) d \omega_{t-1} d \omega_{t-2} \cdots d \omega_{0} \\
& =\iint \cdots \int p\left(\omega_{t-1}, y\right) p\left(\omega_{t-2}, \omega_{t-1}\right)
\cdots p\left(\omega_{1}, \omega_{2}\right) \pi_{E}\left(\omega_{1}\right) d \omega_{t-1} d \omega_{t-2} \cdots d \omega_{1} \\
& = \iint \cdots \int p\left(\omega_{t-1}, y\right) p\left(\omega_{t-2}, \omega_{t-1}\right) p\left(\omega_{t-1}, y\right) p\left(\omega_{t-2}, \omega_{t-1}\right)
\cdots p\left(\omega_{2}, \omega_{3}\right) \pi_{E}\left(\omega_{2}\right) d \omega_{t-1} d \omega_{t-2} \cdots d \omega_{2} \\
& =\int p\left(\omega_{t-1}, y\right) \pi_{E}\left(\omega_{t-1}\right) d \omega_{t-1} \\
& =\pi_{E}(y)
\end{aligned}
$$

Stochastic Difference Equation Relation to Stachasic Kernel
Stochastic kernels can be derived from stochastic difference equations
Consider the difference eguation for a random walk

$$
x_{t+1}=x_{t}+\eta_{t+1}
$$

Where $n$ has unit normal distribution with values that are independent and identically distributed. gives
where $y=x_{t+1}$ and $x=x_{t}$
gaking the change of variables

* First Order Autoregressive Process

The first order autoregressive process AR(1) is defined

$$
x_{t+1}=\alpha x_{t}+\varepsilon_{t+1}
$$

where $\varepsilon_{t+1}$ is Normal with mean of zero and constant variance that are independent and identically distributed ,

$$
\varepsilon_{t+1} \stackrel{\text { IID }}{\sim} N\left(0, \sigma^{2}\right)
$$

From the difference equations

$$
\varepsilon_{t+1}=x_{t+1}-\alpha x_{t}
$$

So letting $y=x_{t+1}$ and $x=x_{t}$

$$
-(y-\alpha x)^{2} / 2 \sigma^{2}
$$

$$
p(x, y)=1 e^{-1,} 120^{2}
$$

The normalization condition gives

$$
\int_{-\infty}^{\infty} P(y, x) d y=\frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{-(y-a x)^{2}\left(2 \sigma^{2}\right.} d y
$$

let $\quad z=\frac{y-2 x}{\sigma} \Rightarrow \sigma d z=d y$ so then integral becomes

$$
\begin{aligned}
\int_{-\infty}^{\infty} P(y, x) d y=&\frac{\sigma}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{-z^{2} / 2} d z \\
=&\frac{1}{\sqrt{2 \pi}} \sqrt{2 \pi}=1
\end{aligned}
$$

Recall that AR(1) is defined by

$$
x_{t+1}=\alpha x_{t}+\varepsilon_{t+1}
$$

Now

$$
\begin{aligned}
& x_{1}=\alpha x_{0}+\varepsilon_{1} \\
& x_{2}=\alpha x_{1}+\varepsilon_{2} \\
& x_{3}=\alpha x_{2}+\varepsilon_{3}
\end{aligned}
$$

Substintins $x_{1}$ into $x_{2}$ and that result in $x_{3}$ gives

$$
\begin{aligned}
x_{2} & =\alpha\left(\alpha x_{0}+\varepsilon_{1}\right)+\varepsilon_{2} \\
& =\alpha^{2} x_{0}+\alpha \varepsilon_{1}+\varepsilon_{2} \\
x_{3} & =\alpha x_{2}+\varepsilon_{3} \\
& =\alpha\left(\alpha^{2} x_{0}+\alpha \varepsilon_{1}+\varepsilon_{2}\right)+\varepsilon_{3} \\
& =\alpha^{3} x_{0}+\alpha^{2} \varepsilon_{1}+\alpha \varepsilon_{2}+\varepsilon_{3}
\end{aligned}
$$

continuing this $t+1$ times gioes

$$
\begin{aligned}
x_{t+1}= & \alpha^{t+1} x_{0}+\alpha^{t} \varepsilon_{1}+\alpha^{t-1} \varepsilon_{2}+\cdots-1 \alpha \varepsilon_{t}+\varepsilon_{t+1} \\
= & \varepsilon_{t+1}+\alpha \varepsilon_{t}+\cdots+\alpha^{t-1} \varepsilon_{2}
+\alpha^{t} \varepsilon_{1}+\alpha^{t+1} x_{0} \\
= & \alpha^{t+1} x_{0}+\sum_{i=1}^{t+1} \alpha^{t+1-i} \varepsilon_{i}
\end{aligned}
$$

where $\varepsilon_{i} \stackrel{\text { IID }}{\sim} N(0, \sigma)$

## Equillibrium Mean and Variance

Equilibrium Mean and variane afe given by

$$
\begin{aligned}
& \mu_{E}=\lim _{t \rightarrow \infty} E\left(X_{t}\right) \\
& \sigma_{E}^{2}=\lim _{t \rightarrow \infty} E\left(X_{t}^{2}\right)-\left[E\left(X_{t}\right)\right]^{2}
\end{aligned}
$$

where

$$
x_{t}=\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}
$$

The expectation of $x_{t}$ is given by

$$
\begin{aligned}
& E\left(x_{t}\right)=E\left[\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}\right] \\
& =\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} E\left(\varepsilon_{i}\right)
\end{aligned}
$$

By definition

$$
E\left(\varepsilon_{i}\right)=0
$$

SO)

$$
E\left(x_{t}\right)=\alpha^{t} x_{0}
$$

Now the equilibrium mean is given by

$$
\begin{aligned}
\mu_{E}&=\lim _{t \rightarrow \infty} E\left(X_{t}\right) \\
&=\lim _{t \rightarrow \infty} \alpha^{t} X_{0} \\
& \text { Inis }_{|\alpha|} \lim _{\mid \alpha} t \text { exists for }|\alpha| \leqslant 1 . \\
& \mu_{E}=X_{0}
\end{aligned}
$$

and if $|\alpha|<1$

$$
\mu_{E}=0
$$

Trus

$$
\mu_{E}= \begin{cases}x_{0} & |\alpha|=1 \\ 0 & |\alpha| \leqslant 1\end{cases}
$$

Before computing $S_{E}$ an expression for $x^{2} t$ is required namely

$$
\begin{aligned}
x_{t}^{2} & =\left[\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}\right]^{2} \\
& =\alpha^{2 t} x_{0}^{2}+2 \alpha^{t} x_{0} \sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i} \\
& +\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{t-i} \alpha^{t-j} \varepsilon_{i} \varepsilon_{j}
\end{aligned}
$$

so the expection of $x_{t}^{2}$ is

$$
\begin{aligned}
E\left(x_{t}^{2}\right) & =E\left[\alpha^{2 t} x_{0}^{2}+2 \alpha^{t} x_{0} \sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}\right. \\
& \left.+\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{2 t-i-j} \varepsilon_{i} \varepsilon_{j}\right] \geqslant 0 \\
= & \alpha^{2 t} x_{0}^{2}+2 \alpha t x_{0} \sum_{i=1}^{t} \alpha^{t-i} / E\left(\varepsilon_{i}\right) \\
& +\sum_{i=c}^{t} \sum_{j=1}^{t} \alpha^{2 t-i-j} E\left(\varepsilon_{i} \varepsilon_{j}\right)
\end{aligned}
$$

The second ferm vanishes because by definition

$$
E\left(\varepsilon_{i}\right)=0
$$

also by defintion the $\varepsilon_{i}$ are independent so,

$$
E\left(\varepsilon_{i} \varepsilon_{1}\right)=\sigma^{2} \delta_{i j}
$$

where $\delta_{i}$ is the Kroneker detto and $\sigma^{2}=E\left(\varepsilon_{i}^{2}\right)$

$$
\delta_{i j}= \begin{cases}0 & i \neq j \\ 1 & i=j\end{cases}
$$

So

$$
\begin{aligned}
E\left(x_{t}^{2}\right) & =\alpha^{2 t} x_{0}^{2}+\sigma^{2} \sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{2 t-i-j} \delta \ddot{j} \\
& =\alpha^{2 t} x_{0}^{2}+\sigma^{2} \sum_{i=1}^{t} \alpha^{2(t-i)} \\
& =\alpha^{2 t} x_{0}^{2}+\sigma^{2} \sum_{i=1}^{t}\left(\alpha^{2}\right)^{t-i}
\end{aligned}
$$

The second term is a
geometrif series which converges
shly for $1 \alpha i<1$. sonly For $1 \alpha T<1$.
Rearranging a bit gives

$$
\begin{aligned}
& \sum_{i=1}^{t}\left(\alpha^{2}\right)^{t-i}=\sum_{k=0}^{t-1}\left(\alpha^{2}\right)^{k} \\
& =\frac{1-\left(\alpha^{2}\right)^{t-1}}{1-\alpha^{2}}
\end{aligned}
$$

50

$$
E\left(x_{t}^{2}\right)=\alpha^{2 t} x_{0}^{2}+\sigma^{2} \frac{\left[1-\left(\alpha^{2}\right)^{t-1}\right]}{1-\alpha^{2}}
$$

and for $121<1$

$$
\begin{aligned}
\sigma_{E}^{2} & =\lim _{t \rightarrow \infty} E\left(X_{t}^{2}\right) \\
& =\lim _{t \rightarrow \infty} \alpha^{2 t} X_{0}^{2}+\frac{\gamma^{2}\left[1-\left(\alpha^{2}\right)^{t-1}\right]}{1-\alpha^{2}} \\
& =\frac{\sigma^{2}}{1-\alpha^{2}}
\end{aligned}
$$

In summary equillibrium solutions only exists for $|\alpha|<1$ with

$$
\begin{aligned}
& \mu_{E}=0 \\
& \sigma_{E}^{2}=\frac{\sigma^{2}}{1-\alpha^{2}}
\end{aligned}
$$

## * Estimation of $\pi_{E}$

Recall that $\pi_{E}$ is defined by

$$
\pi_{E}(y)=\int p(x, y) \pi_{E}(x) d x
$$

The righthand side is
the expectation of the stochastic kernel so for sufficiently large $n$

$$
\begin{aligned}
\frac{1}{n+1} \sum_{i=0}^{n} P\left(x_{i}, y\right) & \rightarrow S P(x, y) \pi_{E}(x) d x \\
& =\pi_{E}(x)
\end{aligned}
$$

as $n \rightarrow \infty$

The samples $\left\{x_{0}, x_{1}, x_{2}, \ldots, x_{n}\right\}$ are generated from the differonce equation defining the process.
For AR(1) the stochastic Kernel is given by

$$
p(x, y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y-\alpha x)^{2} / 2 \sigma^{2}}
$$

with the difference equation

$$
x_{t+1}=\alpha x_{t}+\varepsilon_{c+1}
$$

where $|\alpha|<1$ and

$$
\varepsilon_{i+1} \stackrel{I I D}{\sim} N(0, \gamma)
$$

To estimate $\pi_{E}(y)$ a sequence

$$
\left\{x_{0}, x_{1}, x_{2}, \ldots, x_{n}\right\}
$$

using the difference equation

$$
\pi_{E}(y) \approx \frac{1}{n+1} \sum_{i=1}^{n} P\left(x_{i}, y\right)
$$

AR(1) large $\alpha$ Limit

The AR(1) difference equation
is defined by

$$
x_{t+1}=\alpha x_{t}+\varepsilon_{t+1}
$$

where

$$
\varepsilon_{t+1} \stackrel{\text { IID }}{\sim} N(0, \sigma)
$$

For $|\alpha|>1$ the first term will eventually domingte $t$ the noise term, so for large

$$
\begin{aligned}
x_{t} & \approx \alpha x_{t-1} \\
& =\alpha^{t} x_{0}
\end{aligned}
$$

AR(1) Equillibrium Analytic solution for $T_{E}(y)$

The equillibrium mean and yariance for AR(1) were found to be

$$
\begin{aligned}
& \mu_{E}=0 \\
& \sigma_{E}^{2}=\frac{\sigma^{2}}{1-\alpha^{2}}
\end{aligned}
$$

and the stochastic kernel is given by

$$
P(x, y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y-\alpha x)^{2} / 2 \sigma^{2}}
$$

Now $\Pi_{E}(y)$ is defined by

$$
\pi_{E}(y)=\int p(x, y) \pi_{E}(x) d x
$$

Assume

$$
\pi_{E}(x)=\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-\left(x-\mu_{E}\right)^{2} / 2 \sigma_{E}^{2}}
$$

$$
=\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-x^{2} / 2 \sigma_{E}^{2}}
$$

## Then

$$
\begin{aligned}
& \int p(x, y) \pi_{E}(x) d x \\
= & \int_{-\infty}^{\infty}\left\{\left[\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y-\alpha x)^{2} / 2 \sigma^{2}}\right]\right. \\
& \left.\sqrt{2 \pi \sigma_{E}^{2}} e^{-x^{2} / 2 \sigma_{E}^{2}}\right\} d x \\
= & \frac{1}{\sqrt{2 \pi \sigma^{2}}} \frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left[\frac{1}{\sigma^{2}}(y-\alpha x)^{2}+\frac{1}{\sigma_{E}^{2}} x^{2}\right]} d x
\end{aligned}
$$

Consider the exponent

$$
\begin{aligned}
\frac{1}{\sigma^{2}}(y-\alpha x)^{2}-\frac{x^{2}}{\sigma_{E}^{2}}&=\frac{1}{\sigma^{2}}\left(y^{2}-2 \alpha x y+\alpha^{2} x^{2}\right) +\frac{x^{2}}{\sigma_{E}^{2}} \\
&=\frac{1}{\sigma_{E}^{2}} \sigma^{2}\left[\sigma_{E}^{2}\left(y^{2}-2 \alpha x y+\alpha^{2} x^{2}\right)\right.
\left.+\sigma^{2} x^{2}\right] \\
& =\frac{1}{\sigma_{E}^{2} \sigma^{2}}\left[\sigma_{E}^{2} y^{2}-\sigma_{E}^{2} 2 \alpha x y+\sigma_{E}^{2} \alpha^{2} x^{2}+\sigma^{2} x^{2}\right] \\
&=\frac{1}{\sigma_{E}^{2} \sigma^{2}}\left[\sigma_{E}^{2} y^{2}-2 \sigma_{E}^{2} \alpha x y+x^{2}\left(\sigma_{E}^{2} \alpha^{2}+\sigma^{2}\right)\right]
\end{aligned}
$$

Now for the $x^{2}$ term

$$
\begin{aligned}
\sigma_{E}^{2} \alpha^{2}+\sigma^{2}=&\frac{\sigma^{2} \alpha^{2}}{1-\alpha^{2}}+\sigma^{2} \\
= & \frac{\sigma^{2} \alpha^{2}+\sigma^{2}\left(1-\alpha^{2}\right)}{1-\alpha^{2}} \\
= & \frac{\sigma^{2} \alpha^{2}+\sigma^{2}-\sigma^{2} \alpha^{2}}{1-\alpha^{2}}=\frac{\sigma^{2}}{1-\alpha^{2}}=\sigma_{E}^{2}
\end{aligned}
$$

substituting into the original expression

$$
\begin{aligned}
& \frac{1}{\sigma_{E}^{2} \sigma^{2}}\left(\sigma_{E}^{2} y^{2}-2 \sigma_{E}^{2} \alpha x y+\sigma_{E}^{2} x^{2}\right) \\
= & \frac{1}{\sigma^{2}}\left(y^{2}-2 \alpha x y+x^{2}\right) \\
= & \frac{1}{\sigma^{2}}\left(y^{2}+x^{2}-2 \alpha x y+\alpha^{2} y^{2}-\alpha^{2} y^{2}\right) \\
= & \frac{1}{\sigma^{2}}\left(y^{2}-\alpha^{2} y^{2}\right)+\frac{1}{\sigma^{2}}\left(x^{2}-2 \alpha y x+\alpha^{2} y^{2}\right) \\
= & \frac{\left(1-\alpha^{2}\right)}{\sigma^{2}} y^{2}+\frac{1}{\sigma^{2}}(x-\alpha y)^{2}
\end{aligned}
$$

$$
=\frac{y^{2}}{\sigma_{E}^{2}}+\frac{(x-\alpha y)^{2}}{\sigma^{2}}
$$

Recall that the integral is given by
$\frac{1}{\sqrt{2 \pi \sigma^{2}}} \frac{1}{2 \pi \sigma_{E}^{2}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left[\frac{1}{\sigma^{2}}(y-\alpha x)^{2}+\frac{1}{\sigma_{E}^{2}} x^{2}\right]} d x$
$=\frac{1}{\sqrt{2 \pi \sigma^{2}}} \frac{1}{\sqrt{2 \pi} \sigma_{E}^{2}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left[\frac{1}{\sigma_{E}^{2}} y^{2}+\frac{1}{\sigma^{2}}(x-\alpha y)^{2}\right]} d x$
$=\frac{1}{\sqrt{2 \pi} \sigma_{E}^{2}} e^{-y^{2} / 2 \sigma_{E}^{2}} \frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{-\left(x-\alpha y^{2}\right) / 2 \sigma^{2}} d x$
$=\frac{1}{2 \pi \sigma_{E}^{2}} e^{-Y^{2} / 2 \sigma_{E}^{2}}$
Thus

$$
\pi_{E}(y)=\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-y^{2} / 2 \sigma_{E}^{2}}
$$

## Metropolis-tlastings Algorithm

The Metropolis-Hastings algorithm is defined as follows.
Let $f(y)$ be the function
to be sampled. The algorithm constructs a Markou Chaih
with an equilibrium distribution $\pi_{E}(y)$ where

$$
\pi_{E}(y)=f(y)
$$

The algorithm must determine the stochastic kernel p(xyy) which satisfies the equilibrium condition

$$
\pi_{E}(y)=\int^{x} P(x, y) \pi_{E}(x) d x
$$

$\pi_{E}(y)$ is approximated by

$$
\pi_{E}(y) \approx \frac{1}{n+1} \sum_{i=0}^{n} p\left(x_{i}, y\right)
$$

for a sufficiently large number of samples.

To generate samples from $p(x, y)$ a candidate samplable stochastic Kernel $q(x, y)$ is proposed.
Let $x_{t}^{*}$ be the sample generated a step $t$ by $q\left(x_{t-1}, x_{t}^{*}\right)$ and $x_{t}$ be the previous sample. Then define a function $\alpha\left(x_{t-1}, x_{t}^{*}\right)$ that satisfies

$$
0 \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \leqslant 1
$$

Later it will be shown that

$$
\alpha(x, y)=\min \left[\frac{f(y) q(y, x)}{f(x) q(x, y)}, 1\right]
$$

Now let ut be a uniformly distributed random variable

$$
u_{t} \sim \mathcal{U}(0,1)
$$

Now if $u_{t}$

$$
u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right)
$$

accept the proposed sample

$$
x_{t}=x_{t}^{*}
$$

But if

$$
u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right)
$$

reject the propased by propogating the previous sample

$$
x_{t}=x_{t-1}
$$

This differs from the Rejection sampling Algorithim only in that Rejection Samplin does not addance in time if the proposed sample is rejected, but instead tries a new sample and does not advance in time until a propsed sample is accepted.
The rejection step in MetropolisHastings is viewed as a transition that does not lead to a state change.
In summary groen a function $f(y)$ the Matropolis-Hastings Algorithm will produce samples with distribution $f(x)$ from the following steps

For $t=0,1,2, \ldots, n$

1) Eenerate a proposal sample
$x_{t+1}^{*}$ from $g\left(x_{t}, y\right)$ and $a$
$u_{t+1}^{t+1}$ from $u(0,1)$ idependently.
2) if $u_{t+1} \leqslant \alpha\left(x_{t}, x_{t+1}^{*}\right) \quad x_{t+1}=x_{t+1}^{*}$
3) If $\quad u_{t+1}>\alpha\left(x_{t}, x_{t+1}^{*}\right) \quad x_{t+1}=x_{t}$

The resulting $x_{0}, x_{1}, x_{2}, \ldots, x_{n}$ will have distribution $f(x)$.

## * Detailed Balance

If $\Pi_{E}(x)$ is the equilibrium distribution of the stochastic Kernel $p(x, y)$

$$
\pi_{E}(y)=\int p(x, y) \pi_{E}(x) d x
$$

Detalied Balance is a symmetry representing time reversal of transitions between $y$ and $x$

$$
\pi(x) p(x, y)=\pi(y) p(y, x)
$$

If $\pi(x)$ is the equilibrium distribution

$$
\pi_{E}(x) p(x, y)=\pi_{E}(y) p(y, x)
$$

so

$$
\begin{aligned}
\pi(y) & =\int p(x, y) \pi(x) d x \\
& =\int p(y, x) \pi(y) d x \\
& =\pi(y) \int p(y, x) d x
\end{aligned}
$$

But by definition

$$
\int p(y, x) d x=1
$$

thus any distribution satisfying Detailed Balance is an equillibrium distribution.

* Proof that Metropolis-Hastings Algrithm Works

To prove that the Metropolis Hastings Algorithm works it must be shown that the computed stochastic Kernerl $P(x, y)$ has an equilibrium distribution $\pi_{E}(y)$ that is
equal to the function to be sampled $f(y)$

$$
\pi_{E}(y)=f(y)
$$

Consider the Stochastic Kernel
$p(x, y)$ and assume that
it can be written, in the form of a probability
desity

$$
p(x, y)=h(y \mid x)
$$

80
$P\left[\bar{x}_{t} \leqslant x_{t} \mid \bar{x}_{t-1}=x_{t-1}\right]=\int^{x_{t}} h\left(x_{t-1} \mid \omega\right) d \omega$

$$
=\int^{x_{t}} p\left(x_{t-1}, \omega\right) d \omega
$$

To compute the probability + that a proposed sample, $x_{t}^{*}$, generated by $q(x, y)$ is accepted the cacceptance probawility,

$$
u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right)
$$

and rejection probability

$$
u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right)
$$

must both be considered and in dependence of $x_{t}^{*}$ and ut used.

Now using the law of Total probability $u_{t}$ can be injected into the distribution

$$
\begin{aligned}
& P\left[\bar{x}_{t} \leqslant x_{t} \mid \bar{x}_{t-1}=x_{t-1}\right] \\
= & P\left[\bar{x}_{t} \leqslant x_{t} \mid u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right), \bar{x}_{t-1}=x_{t-1}\right] \\
& P\left[u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right] \\
+ & P\left[\bar{x}_{t} \leqslant x_{t} \mid u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right), \bar{x}_{t-1}=x_{t-1}\right] \\
& P\left[u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]
\end{aligned}
$$

The first term is the case when the proposed sample $x_{t}^{*}$ is accepted and the second term when it is rejected
$P\left[\bar{x}_{t} \leqslant x_{t} \mid u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right), \bar{x}_{t-1}=x_{t-1}\right]$
$P\left[u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=P\left[\mathbb{Z}_{t} \leqslant x_{t}, u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \mathbb{X}_{t-1}=x_{t-1}\right]$

For $u \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right), x_{t}=x_{t}^{*}$. Since $u_{t}$ is independent of $x_{t}^{*}$ conditioned on $X_{t-1}$, the joint density is assumed to be

$$
h\left(x ; u_{t} \mid x_{t-1}\right)=(1) q\left(x_{t-1}, x^{*}\right)
$$

since $u_{t} \sim u(0,1)$ it has density 1 and the desity of $x_{t}^{*}$ conditioned on $x_{t-1}$ is $q\left(x_{t-1}, x_{t}^{*}\right)$

So,
$P\left[z_{+} \leqslant x_{t}, u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \mathbb{Z}_{t-1}=x_{t-1}\right]$
$=\int^{x_{t}} \int_{0}^{\alpha\left(x_{t-1}, x^{*}\right)} n\left(x^{*}, u \mid x_{t-1}\right) d u d x^{*}$
$=\int^{x_{t}} \int_{0}^{\alpha\left(x_{t-1}, x^{*}\right)} q\left(x_{t-1}, x^{*}\right) d u d x^{*}$
$=\int^{x_{t}} \alpha\left(x_{t-1}, x^{*}\right) q\left(x_{t-1}, x^{*}\right) d x^{*}$

The second term represents the case where $x_{t}^{*}$ is rejected and $\quad x_{t}=x_{t-1}$
$P\left[\bar{x}_{t} \leqslant x_{t} \mid u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right), \bar{x}_{t-1}=x_{t-1}\right]$
$P\left[u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=P\left[X_{t} \leqslant x_{t}, u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
For $u_{t} \geqslant \alpha\left(x_{t-1}, x_{t}^{*}\right), x_{t}=x_{t-1}$ and as before $u_{t}$ is independent of $x_{t}^{*}$ conditioned on $x_{t-1}$ but here $x_{t}^{*}$ is rejected. The density for this case is the same used previously, namely
$h\left(x^{*}, u_{t} \mid x_{t-1}\right)=(1) q\left(x_{t-1}, x^{*}\right)$
But since $X_{t}^{*}$ is rejected
any value is possible so
it follows that the probability
that $x_{t}=x_{t-1}$ must integrate over all possible values of $x_{t}^{x}, x^{*}$. The probability that $x_{t}^{*}$ is rejected is,
$P\left[x_{t}=x_{t-1}, u_{t}>\alpha\left(x_{t-1}, x^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=\iint_{\alpha\left(x_{t-1}, x^{*}\right)}^{1} q\left(x_{t-1}, x^{*}\right) d u d x^{*}$
$=\int\left[1-d\left(x_{t-1}, x^{*}\right)\right] q\left(x_{t-1}, x^{*}\right) d x^{*}$
$=\int q\left(x_{t-1}, x^{*}\right) d x^{*}$

$$
-\int \alpha\left(x_{t-1}, x^{*}\right) q\left(x_{t-1}, x^{*}\right) d x^{*}
$$

$=1-\int \alpha\left(x_{t-1}, x^{*}\right) q\left(x_{t-1}, x^{*}\right) d x^{*}$ since by defintion
$\int q\left(x_{t-1}, x^{*}\right) d x^{*}=1$
So the regection probability is
$P\left[x_{t}=x_{t-1}, u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=1-\int \alpha\left(x_{t-1}, x^{*}\right) q\left(x_{t-1}, x^{*}\right) d x^{*}$
Define
$P_{R}\left(x_{t-1}\right)=1-\int \alpha\left(x_{t-1} x^{*}\right) q\left(x_{t-1} x^{*}\right) d x^{*}$

To get the desired probability density the Dirac Deta function is neleded

$$
\int f(x) \delta_{x_{0}}(x) d x=f\left(x_{0}\right)
$$

$P\left[x_{t} \leqslant x_{t}, u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=\int^{x_{t}} p_{R}(x) \delta_{x_{t-1}}(x) d x$
Putting everything together
$P\left[\bar{x}_{t} \leqslant x_{t} \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=P\left[z_{+} \leqslant x_{t}, u_{t} \leqslant \alpha\left(x_{t-1}, x_{t}^{*}\right) \mid z_{t-1}=x_{t-1}\right]+$
$P\left[x_{t} \leqslant x_{t}, u_{t}>\alpha\left(x_{t-1}, x_{t}^{*}\right) \mid \bar{x}_{t-1}=x_{t-1}\right]$
$=\int^{x_{t}} p\left(x_{t-1}, \omega\right) d \omega$
$=\int_{x_{t}}^{x_{t}} \alpha\left(x_{t-1}, y\right) q\left(x_{t-1}, y\right) d y+$
$\int^{x_{t}} p_{p}(y) \delta_{x_{t-1}}(y) d y$

$$
\begin{array}{r}
=\int^{x_{t}}\left\{\alpha\left(x_{t-1}, y\right) q\left(x_{t-1}, y\right)+\right. \\
P_{R}(y) \delta_{x_{t-1}}(y) d y
\end{array}
$$

$=\int^{x_{t}} p\left(x_{t-1}, y\right) d y$
Letting $x=x_{t-1}$ and using
$x_{t}=x_{t-n}=x$ in the Detta function since for this term the proposed sample is rejected and $x_{t}=x_{t-1}$ gives a nicer looking expression for $p(x, y)$ going forward

$$
\begin{gathered}
p(x, y)=\alpha(x, y) q(x, y)+p_{R}(y) \delta_{x}(y) \\
p_{R}(x)=1-\int \alpha(x, y) q(x, y) d y
\end{gathered}
$$

Consider

$$
\begin{gathered}
p(x, y)=\alpha(x, y) q(x, y)+p_{R}(y) \delta_{x}(y) \\
p_{R}(x)=1-\int \alpha(x, y) q(x, y) d y
\end{gathered}
$$

verify that

$$
\int p(x, y) d y=1
$$

$$
\begin{aligned}
& \int p(x, y) d y=\int \alpha(x, y) q(x, y) d y \\
& +\int\left[1-\int \alpha(y, v) q(y, v) d v\right] \delta x(y) d y \\
& =\int \alpha(x, y) q(x, y) d y \\
& +1-\int \alpha(x, v) q(x, v) d v \\
& =\int \alpha(x, y) q(x, y) d y+1 \\
& -\int \alpha(x, y) q(x, y) d y \\
& =1
\end{aligned}
$$

As expected

* Detailed Balance as Equilibrium Distribution.


## Now

$$
\begin{gathered}
p(x, y)=\alpha(x, y) q(x, y)+p_{R}(y) \delta_{x}(y) \\
p_{R}(x)=1-\int \alpha(x, y) q(x, y) d y
\end{gathered}
$$

If a function $\pi(y)$ is assumed
to satisfy Detailed Balance

$$
\pi(x) \alpha(x, y) q(x, y)=\pi(y) \alpha(y, x) q(y, x)
$$

It can be shown that

$$
\pi(y)=\int p(x, y) \pi(x) d x
$$

To prove this

$$
\int\left[\int^{a} p(x, y) d y\right] \pi(x) d x
$$

must be evaluated using the Detailed Balance assumption
so

$$
\begin{aligned}
& \int\left[\int^{a} p(x, y) d y\right] \pi(x) d x \\
= & \int^{a} \int p(x, y) \pi(x) d x d y \\
= & \int S[\alpha(x, y) q(x, y) \\
& \left.+P_{R}(y) \delta_{x}(y)\right] \pi(x) d x d y
\end{aligned}
$$

$$
\begin{aligned}
= & \int^{a} \int \alpha(x, y) q(x, y) \pi(x) d x d y \\
& +\iint^{a} P_{R}(y) \delta_{x}(y) \pi(x) d y d x
\end{aligned}
$$

For the second term the Delta Fenction

$$
\delta_{x}(y)= \begin{cases}0 & x \neq y \\ 1 & x=y\end{cases}
$$

so evaluating the integral for the second term over y gives

$$
\begin{aligned}
& S^{a} \int \alpha(x, y) q(x, y) \pi(x) d x d y \\
& +S^{a} P_{R}(x) \pi(x) d x
\end{aligned}
$$

Recall that

$$
\operatorname{PR}(x)=1-\int \alpha(x, y) q(x, y) d y
$$

so putting thing together

$$
\begin{aligned}
& \int^{a} \int p(x, y) \pi(x) d x d y \\
= & S^{a} \int \alpha(x, y) q(x, y) \pi(x) d x d y \\
+ & S^{a}\left[1-\int \alpha(x, y) q(x, y) d y\right] \pi(x) d x \\
= & S^{a} \int \alpha(x, y) q(x, y) \pi(x) d x d y \\
& +S^{\pi} \pi(x) d x-S^{s} \int \alpha(x, y) q(x, y) \pi(x) d y d x
\end{aligned}
$$

The first and last terms are equal if the Detailed Balance condition is applied to the tirst term, namely,
$\alpha(x, y) q(x, y) \pi(x)=\alpha(y, x) q(y, x) \pi(y)$
so
$\int^{a} \int p(x, y) \pi(x) d x d y$
$=\int^{a} \int \alpha(y, x) q(y, x) \pi(y) d x d y$
$+\int^{a} \pi(x) d x-\int^{a} \int \alpha(x, y) q(x, y) \pi(x) d y d x$
Cleaning up so that the itegral to $a$ is over $y$ gives

$$
\begin{aligned}
& =\int^{a} \int \alpha(y, x) q(y, x) \pi(y) d x d y \\
& +\int^{a} \pi(y) d y-\int^{a} \int \alpha(y, x) q(y, x) \pi(y) d x d y \\
& \Rightarrow S^{a} \int p(x, y) \pi(x) d x d y=\int \pi(y) d y \\
& \Rightarrow \int p(x, y) \pi(x) d x=\pi(y)
\end{aligned}
$$

* Determination of $\alpha(x, y)$

It has been shown that for

$$
\begin{gathered}
p(x, y)=\alpha(x, y) q(x, y)+p_{R}(y) \delta_{x}(y) \\
p_{R}(x)=1-\int \alpha(x, y) q(x, y) d y
\end{gathered}
$$

if

$$
\alpha(x, y) g(x, y) \pi(x)=\alpha(y, x) q(y, x) \pi(y)
$$

Then

$$
S p(x, y) \pi(x)=\pi(y)
$$

Bet $\alpha(x, y)$ has not been determined. Onhy that it nas the constraint

$$
0 \leqslant \alpha(x, y) \leqslant 1
$$

Nor has it been epplained how to achieve detailed balance with an arbritrary choice for $q(x, y)$.

In general $q(x, y)$ will satisfy

$$
\pi(x) q(x, y)>\pi(y) c_{q}(y, x)
$$

or

$$
\pi(x) q(x, y)<\pi(y) q(y, x)
$$

If the first condilion is the case transitions from $x$ to $y$ occur more frequently than transitions from $y$ to $x$. To corred the problem would be to reduce the number of $x$ to $y$ transitions by reducing their probability, i.e.

$$
\alpha(x, y)<1
$$

Transitions from $x$ to are made with probablility

$$
\alpha(x, y) q(x, y)
$$

Also, since transitions from y to $x$ are not made often enough the frequency of these transitions should be increased. Letting

$$
\alpha(y, x)=1
$$

would give the result of the $y$ to $x$ transition
always occuring. An expression
for $\alpha(x, y)$ can be found
for this case from the Detailed
Ballance condition for $p(x, y)$
$\alpha(x, y) q(x, y) \pi(x)=\alpha(y, x) q(y, x) \pi(y)$
setting
gives

$$
\alpha(y, x)=1
$$

$$
\alpha(x, y)=\frac{q(y, x) \pi(y)}{q(x, y) \pi(x)}
$$

This choice for $\alpha(x, y)$ will drive choice of accepting or rejecting a proposed sample twand a state where

$$
\pi(x) q(x, y)=\pi(y) q(y, x)
$$

Resultins in Detailed Balace for the generated samples.
If it is assumed that

$$
\pi(x) q(x, y)<\pi(y) q(y, x)
$$

The time reversed version of $\alpha(x, y)$ is obtained.

In Summany

$$
\alpha(x, y)=\min \left[1, \frac{\pi(y) q(y, x)}{\pi(x) q(x, y)}\right]
$$

* Choices of $q(x, y)$

Choices for $g(x, y)$ are made from distribstions that require specitication of parameters
such as shape bcation and scale that impact convergence to equilibrium.

* The Metropolis Algorithm assumed

$$
q(x, y)=q(y-x)
$$

The proposed sample $y^{*}$ is choosen using the difference equation

$$
\begin{aligned}
& y^{*}=x+\varepsilon \\
\Rightarrow & \varepsilon=y^{*}-x
\end{aligned}
$$

Thus $G(x, y)$ will be determined hy the distribution choosen for $\varepsilon$.

This choice has the form of a random walk and is referred to as a random walk chain. For the case

$$
\begin{aligned}
q(y-x) & =q(x-y) \\
\Rightarrow q(x, y) & =q(y, x)
\end{aligned}
$$

the acceptance probability becomes

$$
\alpha(x, y)=\min \left[1, \frac{\pi(y)}{\pi(x)}\right]
$$

Which is Metropplis Algorithm acceptence probability.

* For any $\left.g_{( } x, y\right)$ it can be assumed that the location is given by $x$ and y can be generated.
For example in the random walk chain with

$$
\begin{gathered}
\varepsilon \sim N(0, \sigma) \\
q(x, y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y-x)^{2} / 2 \sigma^{2}}
\end{gathered}
$$

If $g(x, y)$ is assumed to be a gamma distribution with shape $k$ and scale $\theta$ the mean is given by

$$
x=k \theta \Rightarrow k=\frac{x}{\theta}
$$

and

$$
q(x, y)=\frac{1}{\Gamma(y / \theta) \theta^{k / \theta}} y^{x / \theta-1} e^{-x / \theta}
$$

Another possibility is to assume that $q(x, y)$ is indepent of $x$. This case is called an independence chain.

$$
q(x, y)=q(y)
$$

* If $q(x, y)$ is assumed to be normal

$$
-(y-\mu)^{2} / 2 \sigma^{2}
$$

$$
q(1)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e
$$

* For this case the mean $\mu$ in addition to $\sigma$ must be specified
As a limiting case assume that $\varphi(y)$ is uniform over the interval $[a, b]$. In this case

$$
\begin{gathered}
\mu=\frac{1}{2}(b-a) \quad \sigma^{2}=\frac{1}{2}(b-a)^{2} \\
q(y)=\frac{1}{b-a}
\end{gathered}
$$

## Acceptance Probability

The probability of acceptance of a sample is given by

$$
P\left[\bar{u} \leqslant \alpha\left(x, y^{*}\right)\right]
$$

where

$$
\alpha\left(x, y^{*}\right)=\min \left[\frac{f\left(y^{*}\right) g\left(y^{*}, x\right)}{f(x) g\left(x, y^{*}\right)}, 1\right]
$$

the joint distribution is given by

$$
\begin{aligned}
f\left(u, x, y^{*}\right) & =f_{\underline{a}}(u) f\left(x, y^{*}\right) \\
& =f\left(x, y^{*}\right)
\end{aligned}
$$

since $f_{\bar{l}}(u)=1$
Now

$$
f\left(x, y^{*}\right)=f\left(y^{*} \mid x\right) f(x)
$$

SO
$P\left[\bar{u} \leqslant \alpha\left(x, y^{*}\right)\right]=\iiint_{0}^{\alpha\left(x, y^{*}\right)} q\left(x, y^{*}\right) f(x) d u d x d y^{*}$
$=\iint \alpha\left(x, y^{*}\right) f(x) d x d y^{*}$
$=\iint f\left(y^{*}\right) q\left(y^{*}, x\right) d x d y^{*}$
Now consider the case where the target distribution is a weilbull with shape parameter $\lambda=1$ and scale parameter $k=5$.

$$
f(x)=5 x^{4} e^{-x^{5}}
$$

Also assume that the proposal distribution is Normal with stochastic kernel

$$
q\left(y^{*}, x\right)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y \cdot x)^{2} / 2 \sigma^{2}}
$$

Now,
$P\left[u \leqslant \alpha\left(x, y^{*}\right)\right]=\iint f\left(y^{*}\right) q\left(y^{*}, x\right) d x d y^{*} =\int_{0}^{\infty} \int_{0}^{\infty} S\left(y^{*}\right)^{4} e^{-\left(y^{*}\right)^{5}}\left[\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\left(y^{*}-x\right)^{2} / 2 \sigma^{2}}\right] d x d y^{*}$
let

$$
\begin{aligned}
& \omega=\left(y^{*}\right)^{5} \Rightarrow d \omega=5\left(y^{*}\right)^{4} d y^{*} \\
& y^{*}=\omega^{1 / 5}
\end{aligned}
$$

$$
P\left[u \leqslant \alpha\left(x, y^{*}\right)\right]=\int_{0}^{\infty} \int_{0}^{\infty} e^{-\omega} e^{\left(\omega^{1 / 5}-x\right)^{2}} d x d \omega
$$

## Gibbs Sampling

Gibbs Sampling is a method for obtaing samples from multivarite distributions that uses Bayes Theorem to write the distribution as single variable conditional distributions which are sampled sequentially.
For example consider the bivarite distribution $p(x, y)$. Bayes Theorem gives

$$
p(x, y)=p(x \mid y) p(y)
$$

For a given $y$

$$
p(x, y) \propto p(x \mid y)
$$

similarly

$$
p(x, y)=p(y \mid x) p(x)
$$

and for a given $x$

$$
p(x, y) \propto p(y \mid x)
$$

If both $p(x \mid y)$ and $p(y \mid x)$ can be sampled samples for
$P(x, y)$ can be obtained using the following proceedure.
Choose starting values for $x$ and $y$, namely ( $x_{0}, y_{0}$ )
subsequent samples are generated using

1) sample $x_{t} \sim p\left(x \mid y_{t-1}\right)$
2) sample $y_{t} \sim p\left(y \mid x_{t}\right)$

This proceedure generates the sequence

$$
\left(x_{0}, y_{0}\right),\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{N}, y_{N}\right)
$$

The sequence is a Markoy Chain since the samples generated at a given step in the procredure depend on samples at the previous step.
Gilabs sampling does not reject any proposed samples for the conditional distributions.

It can be shown that Gibbs sampling is equivalent to Metropolis Hastings sampling with an acceptance function that is always 1.
The seneralization of Gibbs samplin softo an arbitrary number of varialdes is straight forward.
Consider the multivariate distribution

$$
p\left(x^{1}, x^{2}, \ldots, x^{N}\right)
$$

Choose starting values

$$
\left(x_{0}^{1}, x_{0}^{2}, \ldots, x_{0}^{n}\right)
$$

subsequent samples are obtained using the following to seguentially sample each $x_{t}^{n} s$

1) $x_{t}^{1} \sim p\left(x^{1} \mid x_{t-1}^{2}, x_{t-1}^{3}, \ldots, x_{t-1}^{N}\right)$
2) $x_{t}^{2} \sim p\left(x^{2} \mid x_{t}^{1}, x_{t-1}^{3}, \ldots, x_{t-1}^{N}\right)$
n) $x_{t}^{n} \sim p\left(x^{n} \mid x_{t}^{1}, x_{t}^{2}, \ldots, x_{t}^{n-1}, x_{t-1}^{n+1}, \ldots, x_{t-1}^{N}\right)$
i) $x_{t}^{N} \sim p\left(x^{N}\left(x_{t}^{1}, x_{t}^{2}, \ldots, x_{t}^{N-1}\right)\right.$

A simplifyins notation is to denole the conditional distribution for the n'th variable at the t'th step by

$$
p\left(x^{n} \mid x_{-t}^{n}\right)=p\left(x^{n} \mid x_{t}^{1}, x_{t}^{2}, \ldots, x_{t}^{n-1}, x_{t-1}^{n+1}, \ldots, x_{t-1}^{N}\right)
$$

## Gibbs Sampling from Metropols-Hastings

The Metropolis Hastings acceptance function is defined by

$$
\alpha\left(x_{t-1}, x_{t}^{*}\right)=\min \left[1, \frac{f\left(x_{t}^{*}\right) g\left(x_{t}^{*}, x_{t-1}\right)}{f\left(x_{t-1}\right) g\left(x_{t-1}, x_{t}^{*}\right)}\right]
$$

Here $y$ is the propsed sample, $x$ the sample from the previous step, $f(x)$ is the target PDF and $q(x, y)$ the proposal PDF.
For Gibbs Sampling assume the target distribution is the bivariate distribution

$$
p(x, y)=p(x \mid y) p(x)
$$

At time step $t$ in the generation of the sample $x_{t}^{*}$ given itt-1. Assume the proposal distribution is given by

$$
\begin{aligned}
& q\left(x_{t-1}, x_{t}^{*}\right)=p\left(x_{t}^{*} \mid y_{t-1}\right) \\
& q\left(x_{t}^{*}, x_{t-1}\right)=p\left(x_{t-1} \mid y_{t-1}\right)
\end{aligned}
$$

and using

$$
f\left(x_{t}^{*}\right)=p\left(x_{t,}^{*} y_{t-1}\right)
$$

$$
f\left(x_{t-1}\right)=p\left(x_{t-1}, y_{t-1}\right)
$$

gives

$$
\alpha\left(x_{t}, x_{t-1}^{*}\right)=\min \left[1, \frac{p\left(x_{t}^{*}, y_{t-1}\right) p\left(x_{t-1} \mid y_{t-1}\right)}{p\left(x_{t-1}, 1,(t-1) p\left(x_{t}^{*} \mid y_{t-1}\right)\right.}\right]
$$

Now

$$
\begin{aligned}
& p\left(x_{t}^{*}, y_{t-1}\right)=p\left(x_{t}^{*} \mid y_{t-1}\right) p\left(y_{t-1}\right) \\
& p\left(x_{t-1}, y_{t-1}\right)=p\left(x_{t-1} \mid y_{t-1}\right) p\left(y_{t-1}\right)
\end{aligned}
$$

so

$$
\frac{p\left(x_{t}^{*}, y_{t-1}\right) p\left(x_{t}^{*} \mid y_{t-1}\right)}{p\left(x_{t-1}, 1 y_{t-1}\right) p\left(x_{t-1} \mid y_{t-1}\right)}=\frac{p\left(x_{t}^{*} \mid y_{t-1}\right) p\left(y_{t-1}\right)}{p\left(x_{t-1} \mid y_{t-1}\right) p\left(y_{t-1}\right)}
$$

$\frac{p\left(x_{t-1} \mid y_{t-1}\right)}{p\left(x_{t+1}^{*}+y_{t-1}\right)}=1$
thus

$$
\alpha\left(x_{t-1}, x_{t}^{*}\right)=1
$$

so the proposal is always accepted.
In summary Gildbs sampling is a special case of the Metropolis

Hastincs algorithim where the Generation of a sample for $x_{t}$ conditioned on $y_{t-1}$ has a preposal distribution of

$$
P\left(x_{t}^{*} \mid y_{t-1}\right)
$$

which is always accepted since this proposal implies that

$$
\alpha\left(x_{t-1}, x_{t}^{*}\right)=1
$$

## Example: Change Point Model

A Change Point Model is a randsm sequence in which the distribution changes at some point in the sequence. The problem to solve is trat given the sequence what are the distribution parameters
A Change Point Model is costructed as follows
Consider a time sequence of counts
$x_{1: N}=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}, x_{n+1}, x_{n-12}, \ldots, x_{N-1}\right)$
Assume that $X_{t}$ are independent Poisson random variables with with mean that changes at $t=n$, namely,

## $x_{t} \sim \operatorname{Poisson}\left(\lambda_{1}\right)$

for $1 \leqslant t<n$ and for $n \leqslant t \leqslant N$

$$
x_{t} \sim \text { Poisson }\left(\lambda_{2}\right)
$$

A ssume that the mean $\left(\lambda_{i}\right)$ are independent Camma random variables

## $\lambda_{i} \sim \operatorname{Gamma}(\alpha, \beta)$

where $\alpha$ is the shape parameler and $\beta$ is the rate parameter. It will be assumed that $\alpha=2$ and $\beta=1$.
Finally, assume that the the time, $n$, where the change in $\lambda_{i}$ occurs is a uniform random varable on ( $1, N$ )

## $n \sim \operatorname{Uniform}(1, N)$

Thus, the model generating the sequence is given by $n \sim$ Uniform $(1, N)$
$\lambda_{i} \sim \operatorname{Camma}(2,1)$

$$
x_{t}= \begin{cases}\text { Poisson }\left(\lambda_{1}\right) & 1 \leqslant t \leqslant n \\ \text { Poisson }\left(\lambda_{2}\right) & n<t \leqslant N\end{cases}
$$

the densities are

$$
P(n)=\frac{1}{N}
$$

$$
\begin{aligned}
& p(\lambda)=\frac{\lambda}{\Gamma(2)} e^{-\lambda}=\lambda e^{-\lambda} \\
& p\left(x_{t} \mid \lambda_{i}\right)= \begin{cases}\frac{\lambda_{1}^{x}}{x!} e^{-\lambda_{1}} & 0 \leqslant t \leqslant n \\
\frac{\lambda_{2}^{x}}{x!} e^{-\lambda_{2}} & n \leqslant t \leqslant N\end{cases}
\end{aligned}
$$

The proccedure to generate the model is the following,

1) sample $n$ from $p(n)$
2) Sample $\lambda_{1}$ and $\lambda_{2}$ from $p(\lambda)$
3) Draw $n$ samples from

$$
\begin{aligned}
& P\left(x_{t} \mid \lambda_{1}\right) \text { followed by } N-n \\
& \text { samples } p\left(x_{t} \mid \lambda_{2}\right) \text {. }
\end{aligned}
$$

The joint distribution of the parametrs conditioned on $x_{1: N}$ is

$$
p\left(\lambda_{1}, \lambda_{2}, n \mid x_{1: N}\right)
$$

using Bayes Theorem
$p\left(\lambda_{1}, \lambda_{2}, n \mid x_{1: N}\right) \propto p\left(x_{1: N} \mid \lambda_{1}, \lambda_{2}, n\right)$
$p\left(\lambda_{1}, \lambda_{2}, n\right)$

Now $\lambda_{1}, \lambda_{2}$ and $n$ are assumed independent, so

$$
p\left(\lambda_{1}, \lambda_{2}, n\right)=p\left(\lambda_{1}\right) p\left(\lambda_{2}\right) p(n)
$$

In the generative model it is asscumed that $p\left(x_{t} \mid \lambda_{i}\right)$
are conditionally independent and independent of $n$, so,

$$
\begin{aligned}
P\left(x_{1: N} \mid \lambda_{1}, \lambda_{2}, n\right) & =\prod_{t=1}^{n} P\left(x_{t} \mid \lambda_{1}\right) \prod_{t=n+1}^{N} P\left(x_{t} \mid \lambda_{2}\right) \\
& =P\left(x_{1: n} \mid \lambda_{1}\right) P\left(x_{n+1: N} \mid \lambda_{2}\right)
\end{aligned}
$$

so

$$
p\left(\lambda_{1}, \lambda_{2}, n \mid x_{1: N}\right)
$$

$\alpha p\left(x_{1: n} \mid \lambda_{1}\right) p\left(x_{n+1: N} \mid \lambda_{2}\right) p\left(\lambda_{1}\right) p\left(\lambda_{2}\right) p(n)$ Now from the model defintion

$$
P\left(x_{1: n} \mid \lambda_{1}\right)=\prod_{t=1}^{n} \frac{\lambda_{t}^{x_{t}}}{x_{t}!} e^{-\lambda_{1}}
$$

$$
P\left(x_{n+1: N} \mid \lambda_{2}\right)=\prod_{t=n+1}^{N} \frac{\lambda_{2}^{x_{t}}}{x_{t}!} e^{-\lambda_{2}}
$$

$$
\begin{aligned}
& p\left(\lambda_{1}\right)=\lambda_{1} e^{-\lambda_{1}} \\
& p\left(\lambda_{2}\right)=\lambda_{2} e^{-\lambda_{2}} \\
& p(n)=\frac{1}{N}
\end{aligned}
$$

To sample the parameter posterior distributions the probability of each purameler conditioned on the others is required, namely,

$$
\begin{aligned}
& P\left(\lambda_{1} \mid X_{1: N}, \lambda_{2}, n\right) \\
& P\left(\lambda_{2} \mid X_{1: N}, \lambda_{1}, n\right) \\
& P\left(n \mid X_{1: N}, \lambda_{1}, \lambda_{2}\right)
\end{aligned}
$$

Now since $\lambda_{1}$ is independent of $\lambda_{2}, n$ and $x_{n+1: N}$
$P\left(\lambda_{1} \mid x_{1: N}, \lambda_{2}, n\right)=P\left(\lambda_{1} \mid x_{1: n}\right)$
$\alpha p\left(x_{1: n} \mid \lambda_{1}\right) p\left(\lambda_{1}\right)$
$=\left[\prod_{t=1}^{n} e^{-\lambda_{1}} \frac{\lambda_{1}^{x_{-}}}{x_{t}!}\right] \lambda_{1} e^{-\lambda_{1}}$
$=e^{-n \lambda_{1}} \lambda_{t=0}^{n} x_{t}^{n}\left(\prod_{t=1}^{n} \frac{1}{x_{t}!}\right) \lambda_{1} e^{-\lambda_{1}}$

Now the term

$$
\prod_{t=1}^{n} \frac{1}{x_{t}!}
$$

is a constant so it can be ignored, and
$P\left(\lambda_{1} \mid x_{1: N}, \lambda_{2}, n\right) \alpha e^{-n \lambda_{1}} \lambda_{1}^{\sum_{t=0}^{n} x_{t}} \lambda_{1} e^{-\lambda_{1}} =\lambda_{1} \sum_{t=0}^{n} x_{t}+1 e^{-(n+1) \lambda_{1}}$
Recall that the Camma distribution is defined by

$$
\operatorname{Camma}(\alpha, \beta)=\frac{\beta^{\alpha}}{\Gamma^{\prime}(\alpha)} \lambda^{\alpha-1} e^{-\beta \lambda}
$$

so with

$$
\beta=n+1, \quad \alpha=\sum_{t=0}^{n} x_{t}+2
$$

$P\left(\lambda_{1} \mid x_{1: N}, \lambda_{2}, n\right) \propto \operatorname{Camma}\left(\sum_{t=0}^{n} x_{t}+2, n+1\right)$
This result is expected since the Gamma distribution has
the Poisson Distribution as a conjugate prior.
Similary since $\lambda_{2}$ is independent of $\lambda_{1}$ and $n$
$p\left(\lambda_{2} \mid x_{1: N}, \lambda_{1}, n\right)=p\left(\lambda_{2} \mid x_{n+1: N}\right) \alpha p\left(x_{n+1: N} \mid \lambda_{2}\right) p\left(\lambda_{2}\right)$
$=\left[\prod_{t=n+1}^{N} \frac{\lambda_{2}^{X_{t}}}{\lambda_{t}!} e^{-\lambda_{2}}\right] \lambda_{2} e^{-\lambda_{2}}$
$=e^{-(N-n+1)^{t} \lambda_{2}} \lambda_{2}^{\sum_{t=n+1}^{N} x_{t+1}}\left(\prod_{t=n+1}^{N} \frac{1}{x_{t}!}\right)$
$\alpha \quad \lambda_{2} \sum_{t=n+1}^{N} x_{t}+1 \quad e^{-(N-n+1) \lambda_{2}}$
with

$$
\beta=N-n+1 \quad \alpha=\sum_{t=n+1}^{N} x_{t}+2
$$

$p\left(\lambda_{2}\left(x_{1: N}, \lambda_{1}, n\right) \propto \operatorname{Gamma}\left(\sum_{t=n+1}^{N} x_{t}+2, N-n+1\right)\right.$
Finally since $n$ is indepent of $\lambda_{1}$ and $\lambda_{2}$
$p\left(n \mid x_{1: N}, \lambda_{1}, \lambda_{2}\right)=p\left(n \mid x_{1: N}\right)$
$\alpha p\left(x_{1: N} \mid n\right) p(n)$
$=\left[\prod_{t=1}^{n} \frac{\lambda_{1}^{x_{t}}}{x_{t}!} e^{-\lambda_{1}}\right]\left[\prod_{t=n+1}^{N} \frac{\lambda_{2}^{x_{t}}}{x_{t}!} e^{-\lambda_{2}}\right] \frac{1}{N}$
But $1 / N$ is a constant so

$$
\begin{aligned}
& P\left(n \mid x_{1}: N, \lambda_{1}, \lambda_{2}\right) \\
& \alpha\left[\prod_{t=1}^{n} \frac{\lambda_{1}^{x_{t}}}{x_{t}!} e^{-\lambda_{1}}\right]\left[\begin{array}{cc}
\prod_{n+1}^{N} & \lambda_{2}^{x_{t}} e^{-\lambda_{2}} \\
x_{t}!
\end{array}\right] \\
& \alpha \lambda_{1} \sum_{t=1}^{n} x_{t} e^{-n \lambda_{1}} \lambda_{2} \sum_{t=n+1}^{N} x_{t} e^{-(N-n) \lambda_{2}} \\
& =\lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} e^{-N \lambda_{2}} e^{-n\left(\lambda_{1}-\lambda_{2}\right)}
\end{aligned}
$$

SC

$$
P\left(n \mid x_{1: N}, \lambda_{1}, \lambda_{2}\right) \propto \lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} e^{-N \lambda_{2}} e^{\cdot n\left(\lambda_{1}-\lambda_{2}\right)}
$$

This distribution is not of a known twe. In evaluating the terms or $p\left(n \mid x_{1}: N_{1} \lambda_{1}, \lambda_{2}\right)$ esaluation of the robuct of exponentials
with large or small values is numerically problematic. Consider

$$
\begin{aligned}
\ln \left(p\left(n \mid x_{1: N}, \lambda_{1}, \lambda_{2}\right)=\right. & \ln \left[\lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} x_{t}\right. \\
& \left.e^{-N \lambda_{2}} e^{n\left(\lambda_{2}-\lambda_{1}\right)}\right]+C
\end{aligned}
$$

where $C$ is an arbitrary constant
Now

$$
\begin{aligned}
& \ln \left[\lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} x_{t} e^{n\left(\lambda_{2}-\lambda_{1}\right)} e^{-N \lambda_{2}}\right] \\
& =\ln \lambda_{1} \sum_{t=1}^{n} x_{t}+\ln \lambda_{2} \sum_{t=n+1}^{N} x_{t}+n\left(\lambda_{2}-\lambda_{1}\right) \\
& -N \lambda_{2}=P_{n}
\end{aligned}
$$

Let the max of the distribution be denoted by Pmar then properly normallzed

$$
P\left(n \mid x_{1: N}, \lambda_{1} \lambda_{2}\right)=\exp \left[\frac{P_{n}-P_{\max }}{\sum_{i=1}^{N} P_{i}}\right]
$$

In summary for a given

$$
x_{1: N}=\left(x_{1}, x_{2}, \ldots, x_{n}, x_{n+1}, \ldots, x_{n}\right)
$$

$P\left(\lambda_{1} \mid x_{1: N}, \lambda_{2}, n\right) \propto \operatorname{Camma}\left(\sum_{t=0}^{n} x_{t}+2, n+1\right)$
$p\left(\lambda_{2}\left(x_{1: N}, \lambda_{1}, n\right) \propto \operatorname{Gamma}\left(\sum_{t=n+1}^{N} x_{t}+2, N-n+1\right)\right.$
$p\left(n \mid x_{1: N}, \lambda_{1}, \lambda_{2}\right) \propto \lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} e^{-N \lambda_{2}} e^{\cdot n\left(\lambda_{1}-\lambda_{2}\right)}$
To obtain samples using Eibbs sampling the steps are as follows
Init: Generate $x_{1: N}$ using the previously described proceedure Pick initial values for $n_{0}$, $\lambda_{1,0}$ and $\lambda_{2,0}$.
Evaluation loop nsample times. The $K$ 'th step is given by

1) Draw $\lambda_{1, k} \sim p\left(\lambda_{1} \mid x_{1: N}, \lambda_{2, k-1}, n_{k-1}\right)$
2) Draw $\lambda_{2, k} \sim p\left(\lambda_{2} \mid x_{1: N}, \lambda_{1, k}, n_{k-1}\right)$
3) Draw $n_{k} \sim p\left(n \mid x_{1: N}, \lambda_{1, k}, \lambda_{2, k}\right)$

The Distributions $p\left(\lambda_{1} \mid x_{1: N}, \lambda_{2, k-1}, n_{k-1}\right) D\left(\lambda_{2} \mid x_{1: N}, \lambda_{1, k}, n_{k-1}\right)$ are well known Dut $P^{2}\left(n \mid x_{1: N}, \lambda_{1, k}, \lambda_{2, k}\right)$ is unfomiliar so worth investigating to build intuition.

Now
$p\left(n \mid x_{1: N}, \lambda_{1}, \lambda_{2}\right) \propto \lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} e^{-N \lambda_{2}} e^{n\left(\lambda_{1}-\lambda_{2}\right)}$ The first case considered is

$$
\lambda_{1}=\lambda_{2}=\lambda
$$

gives
$p\left(n \mid x_{1: N} \lambda\right)=\lambda^{\sum_{t=1}^{N} x_{t}} e^{-N \lambda}$
using $\frac{N}{2} x_{t} \approx N \lambda$
$t=1$
gives
$P\left(n \mid X_{1: N}, \lambda\right)=\lambda^{N \lambda} e^{-N \lambda}=$ constant
Thus $n \sim$ uniform $(1, N)$

If the change point beteen $\lambda_{1}$ and $\lambda_{2}$ is denoted by $n_{c}$, consider the limit $n \rightarrow n_{c}$

$$
\begin{aligned}
& \lim _{n \rightarrow n_{c}} p\left(n \mid x_{1}: N, \lambda_{1}, \lambda_{2}\right) \\
& =\lim _{n \rightarrow n_{c}} \lambda_{1} \sum_{t=1}^{n} x_{t} \lambda_{2} \sum_{t=n+1}^{N} x_{t} e^{-N \lambda_{2}} e^{-n\left(\lambda_{1}-\lambda_{2}\right)} \\
& =\lim _{n \rightarrow n_{c}} \exp \left[\ln \left(\lambda_{1}\right) \sum_{t=1}^{n} x_{t}+\ln \left(\lambda_{2}\right) \sum_{t=n+1}^{N} x_{t}\right. \\
& \left.\quad-N \lambda_{2}-n\left(\lambda_{1}-\lambda_{2}\right)\right] \\
& \quad \text { Now } \quad a s \quad{ }_{e}^{n} x_{t} \quad \lambda_{1} n \\
& \quad \sum_{t=1}^{N} x_{t} \approx \lambda_{2}(N-n) \\
& \quad \sum_{t=n+1}^{n} \quad \lim _{n \rightarrow n_{c}} p\left(n \operatorname{l} x_{1}: N, \lambda_{1}, \lambda_{2}\right)=\exp \left[\ln \left(\lambda_{1}\right) n_{c} \lambda_{1}\right. \\
& \left.\quad+\ln \left(\lambda_{2}\right)\left(N-n_{c}\right) \lambda_{2}-N \lambda_{2}-n_{c}\left(\lambda_{1}-\lambda_{2}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
=\exp & {\left[\ln \left(\lambda_{1}\right) n_{c} \lambda_{1}-n_{c} \lambda_{1}+\ln \left(\lambda_{2}\right)\left(N-n_{c}\right) \lambda_{2}\right.} \\
& \left.-\left(N-n_{c}\right) \lambda_{2}\right] \\
=\exp & {\left[n_{c} \lambda_{1}\left(\ln \lambda_{1}-1\right)+\left(N-n_{c}\right) \lambda_{2}\left(\ln \lambda_{2}-1\right)\right] }
\end{aligned}
$$

## Gibbs Sampling Examples

1) AM 207 Gibbs Sampler Example

Consider the bivariate distribution

$$
f(x, y)=x^{2} \exp \left(-x y^{2}-y^{2}+2 y-4 x\right)
$$

Now

$$
\begin{aligned}
f(x \mid y) & =f(x, y) \propto f(x, y) \\
& =x^{2} \exp \left[-x\left(y^{2}+4\right)-y(y-2)\right] \\
& =x^{2} \exp \left[-x\left(y^{2}+4\right)\right] \exp [-y(y-2)]
\end{aligned}
$$

Now

$$
\operatorname{Gamma}(\gamma, \beta)=\frac{\beta^{\gamma}}{\Gamma(\gamma)} x^{\gamma-1} e^{-\beta x}
$$

So

$$
\gamma=3, \quad \beta=y^{2}+4
$$

and with

$$
h(y)=\exp [-y(y-2)]
$$

$f(x \mid y) \propto h(y)$ Gamma $\left(3, y^{2}+4\right)$
similarly,

$$
\begin{aligned}
f(y \mid x) & =f(x, y) \propto f(x, y) \\
& =x^{2} \exp \left[-y^{2}(x+1)+2 y-4 x\right] \\
& =x^{2} \exp \left[-y^{2}(x+1)+2 y\right] \exp (-4 x)
\end{aligned}
$$

completins the square on the y dependent term gives

$$
\begin{aligned}
& y^{2}(x+1)-2 y+\frac{1}{(x+1)}-\frac{1}{(x+1)} \\
= & (x+1)\left[y^{2}-\frac{2 y}{x+1}+\frac{1}{(x+1)^{2}}\right]-\frac{1}{x+1} \\
= & (x+1)\left(y-\frac{1}{x+1}\right)^{2}-\frac{1}{x+1} \\
\text { so, } & x^{2} \exp \left[(x+1)\left(y-\frac{1}{x+1}\right)^{2}\right] \exp (-4 x) \\
f(y(x) & \exp \left(\frac{1}{x+1}\right)
\end{aligned}
$$

$\operatorname{Normal}(\mu, \sigma)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(x-\mu)^{2} / 2 \sigma^{2}}$ so with

$$
\mu=\frac{1}{x+1}, \quad \sigma=\frac{1}{\sqrt{2(x+1)}}
$$

and with

$$
g(x)=x^{2} \exp \left(\frac{1}{x+1}-4 x\right)
$$

gives

$$
f(y \mid x) \propto \operatorname{Normal}\left[\frac{1}{x+1}, \frac{1}{\sqrt{2(x+1)}}\right] g(x)
$$

In summary
$f(x \mid y) \propto h(y)$ Gamma $\left(3, y^{2}+4\right)$
$f(y \mid x) \propto$ Normal $\left[\frac{1}{x+1}, \frac{1}{\sqrt{2(x+1)}}\right] g(x)$
2) AM207 Bavariale Normals

Consider the Bivariate Eaussian

$$
f(x, y)=\frac{1}{c} e^{-\left(x^{2} y^{2}+x^{2}+y^{2}-8 x-8 y\right) / 2}
$$

Cleanup the exponential argument

$$
\begin{aligned}
& x^{2} y^{2}+x^{2}+y^{2}-8 x-8 y \\
= & y^{2}\left(x^{2}+1\right)+x^{2}-8 x-8 y \\
= & y^{2}\left(x^{2}+1\right)-8 y+x^{2}-8 x \\
= & \left(x^{2}+1\right)\left(y^{2}-\frac{8 y}{x^{2}+1}\right)+x^{2}-8 x \\
= & \left(x^{2}+1\right)\left[y^{2}-\frac{8 y}{x^{2}+1}+\frac{4^{2}}{\left(x^{2}+1\right)^{2}} \cdot \frac{4^{2}}{\left(x^{2}+1\right)^{2}}\right] \\
& +x^{2}-8 x \\
= & \left(x^{2}+1\right)\left[y^{2}-\frac{8 y}{x^{2}+1}+\frac{y^{2}}{\left(x^{2}+1\right)^{2}}\right]-\frac{16}{x^{2}+1}+x^{2}-8 x \\
= & \left(x^{2}+1\right)\left[y-\frac{4}{x^{2}+1}\right]^{2} \cdot \frac{16}{x^{2}+1}+x^{2}-8 x
\end{aligned}
$$

