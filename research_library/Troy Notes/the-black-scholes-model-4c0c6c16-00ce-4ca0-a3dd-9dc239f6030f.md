## The Black-Scholes Model,

Troy Stribling
Sept. 18, 2021

## Asset Dyramics

In the simpilest model the maket consists of two undehing securities, the risk-free asset and nsky asset.

1) The risk-free asset (Money: maket account), defribed by the deterministic differential equation

$$
d A(t)=r A(t) d t
$$

where $r$ is the risk-free rate. The solution to this equation is

$$
A(t)=A(0) e^{r t}
$$

2) The risky asset is modeled as an Itŝ process,

$$
d s(t)=\mu s(t) d t+\sigma s(t) d \omega(t)
$$

with $S(0)$ given where $\mu \in \mathbb{R}$ is the drift and $\sigma>0$ the volitility of the asset price $s(t)$.

Tre probability space undelying the weiner process $\omega(t)$ is denoted by $(R, F, P)$ the filtration is defined by

$$
\mathcal{F}_{t}^{s}=\sigma(s(u): u \leqslant t)
$$

The solution to this equation was previosly disussed. It is unique and given by

$$
s(t)=s(0) e^{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)}
$$

Previously it was shown that

$$
E[s(t)]=s(0) e^{\mu t}
$$

$\operatorname{Uar}[s(t)]=s^{2}(0) e^{2 \mu t}\left(e^{\sigma^{2} t}-1\right)$

From the expression for $E[s(t)]$ the annualized logarithmic return of the expected price is given by

$$
\begin{aligned}
& E[s(t)]=s(0) e^{\mu t} \\
\Rightarrow & \mu=\frac{1}{t} \ln \left\{\frac{E[s(t)]}{s(0)}\right\}
\end{aligned}
$$

This should not be contlesed with the expected (anualized) logarithmic return which is given by,

$$
\begin{aligned}
& \frac{1}{t} E\left[\ln \frac{S(t)}{S(0)}\right]=\frac{1}{t} E\left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
& \quad=\mu-\frac{1}{2} \sigma^{2}+\frac{\sigma}{t} E[\omega(t)] \\
& \quad=\mu-\frac{1}{2} \sigma^{2} \\
& \text { since } E[\omega(t)]=0
\end{aligned}
$$

Similarly the variance of the logarithm return is given by

$$
\begin{aligned}
& \operatorname{var}\left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
& =\sigma^{2} \operatorname{var}[\omega(t)] \\
& =\sigma^{2} t
\end{aligned}
$$

Since

$$
\operatorname{var}\left[\mu t-\frac{1}{2} \sigma^{2} t\right]=0
$$

The volatility, 6, can be estimated in the following manner

$$
\begin{aligned}
& s(t)=s(0) e^{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)} \\
\Rightarrow & \ln s(t)=\ln s(\sigma)+\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t) \\
\Rightarrow & \ln s(t)-\ln s(\sigma)=\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)
\end{aligned}
$$

Consider the partition of $[0, t]$ given by

$$
0=t_{1}<\cdots<t_{n}=t
$$

with the size of the bagest interval given by

$$
\max \left(t_{k+1}-t_{k}\right)
$$

Now consider

$$
\begin{aligned}
& \ln S\left(t_{k+1}\right)-\ln S\left(t_{k}\right) \\
& =\left(\mu-\frac{1}{2} \sigma^{2}\right)\left(t_{k+1}-t_{k}\right) \\
& \quad+\sigma\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
\sum_{k}\left[\ln s\left(t_{k+1}\right)-\ln s\left(t_{k}\right)\right]^{2} \\
=\sum_{k}\left[\left(\mu-\frac{1}{2} \sigma^{2}\right)\left(t_{k+1}-t_{k}\right)\right. \\
\left.\quad+\sigma\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right]^{2} \\
=\sum_{k}\left(\mu-\frac{1}{2} \sigma^{2}\right)^{2}\left(t_{k+1}-t_{k}\right)^{2} \\
\quad+2 \sigma\left(\mu-\frac{1}{2} \sigma^{2}\right)\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)
\end{aligned}
$$

$$
+\sigma^{2}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)^{2}
$$

For large $n \quad t_{k+1}-t_{k} \approx 0$, so

$$
\begin{aligned}
\sum_{k} & {\left[\ln s\left(t_{k+1}\right)-\ln s\left(t_{k}\right)\right]^{2} } \\
= & \sum_{k} 2 \sigma\left(\mu-\frac{1}{2} \sigma^{2}\right)\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right) \\
& +\sigma^{2}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)^{2} \\
= & 2 \sigma\left(\mu-\frac{1}{2} \sigma^{2}\right) \sum_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right) \\
& +\sigma^{2} \sum_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)^{2}
\end{aligned}
$$

Now for lars $n$

$$
\begin{aligned}
\sum_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right) & \\
& \approx \sum_{k} E\left[\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right] \\
& =0
\end{aligned}
$$

and

$$
\begin{aligned}
\sum_{k} & \left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)^{2} \\
& \approx \sum_{k} E\left[\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)^{2}\right] \\
& =\sum_{k} t_{k+1}-t_{k} \\
& =t
\end{aligned}
$$

## Thus

$$
\begin{aligned}
& \sum_{k}\left[\ln s\left(t_{k+1}\right)-\ln s\left(t_{k}\right)\right]^{2}=\sigma^{2} t \\
= & \sum_{k} \ln ^{2}\left[\frac{s\left(t_{k+1}\right)}{s\left(t_{k}\right)}\right] \approx \sigma^{2} t \\
\Rightarrow & \sigma=\frac{1}{t} \sum_{k} \ln ^{2}\left[\frac{s\left(t_{k+1}\right)}{s\left(t_{k}\right)}\right]
\end{aligned}
$$

Consider the Black-Sholes model,

$$
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t)
$$

which has solution

$$
s(t)=s(0) e^{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)}
$$

Now $\omega(t)$ is a weiner process so it has distribution

$$
\omega(t) \sim \operatorname{Normal}(0, t)
$$

It follows that

$$
\begin{aligned}
& s(t)=s(\sigma) e^{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)} \\
\Rightarrow & \ln s(t)=\ln s(\sigma)+\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t) \\
\Rightarrow & \omega(t)=\frac{1}{\sigma}\left[\ln s(t)-\ln s(\sigma)-\mu t+\frac{1}{2} \sigma^{2} t\right] \\
= & \frac{1}{\sigma}\left[\ln s(t)-\ln s(\sigma)-\left(\mu-\frac{1}{2} \sigma^{2}\right) t\right]
\end{aligned}
$$

since $\omega(t)$ is normal with mean zero and variance $t$ it follows that

$$
\begin{aligned}
& \frac{1}{\sigma}\left[\ln s(t)-\ln s(0)-\left(\mu-\frac{1}{2} \sigma^{2}\right) t\right] \sim \operatorname{Normal}(0, t) \\
& \Rightarrow \ln s(t)-\ln s(0)-\left(\mu-\frac{1}{2} \sigma^{2}\right) t \sim \sigma \operatorname{Normal}(0, t) \\
& \Rightarrow \ln s(t)-\ln s(0)-\left(\mu-\frac{1}{2} \sigma^{2}\right) t \sim \operatorname{Normal}\left(0, \sigma^{2} t\right) \\
& \Rightarrow \ln s(t) \sim \operatorname{Normal}\left(\ln s(0)+\left(\mu-\frac{1}{2} \sigma^{2}\right) t, \sigma^{2} t\right)
\end{aligned}
$$

Thus In $S(t)$ has a normal distribution implying $S(t)$ has a log-normal distribution.
Recall that for a random variable $x$ with density $f(x)$ if $x$ is a function of $y$ then the density of $y$ is given by

$$
g(y)=f(x) \frac{d x}{d y}
$$

here $x=\ln y$ thus

$$
g(y)=\frac{f(\ln y)}{y}
$$

using this formula with $y=s(t)$ sives the density for $s(t)$ is

$$
\begin{aligned}
f(s(t)) & =\frac{1}{2 \pi} \frac{1}{s(t) \sigma \sqrt{t}} \\
& \exp \left\{\left[\frac{\left.\ln s(t)-\ln s(0)-\left(\mu-\frac{1}{2} \sigma^{2}\right) t\right]^{2}}{\sigma^{2} t}\right\}\right.
\end{aligned}
$$

## Methods of Option Pricing

## Risk-Neutral Probability Approach

This is the approach taken when previously discussing discrete models It is assumed that there exists a pair of random processes, $(x, y)$, adapted to the filtration,

$$
\left(\mathcal{F}_{t}^{s}\right)_{t \in[0, T]}
$$

generated by the asset price $s(t)$. The value process for the portfolio consisting of the risky-asset, $S(t)$, and the risk-free incestment $A(t)$

$$
U(t)=x(t) S(t)+y(t) A(t)
$$

where $(x, y)$ is said to be the repicating stratedy for the papff of the derivative security $H$. The
payoff of the derivative security at time $T$ is given by

$$
H(T)=U(T)
$$

The self-financing conditon for the replicating strategy $(x, y)$ is defined by the differential equation

$$
d U(t)=x(t) d s(t)+y(t) d A(t)
$$

The risk-neutral probability, $Q$, is defined such that the discounted asset price and value processes,

$$
\begin{aligned}
& \tilde{S}(t)=e^{-r t} S(t) \\
& \tilde{U}(t)=e^{-r t} U(t)
\end{aligned}
$$

are martigales with respect to $Q$ and the fittration,

$$
\left(\mathfrak{F}_{t}^{s}\right)_{t \in[0, T]}
$$

## The price of the derivative security is defined by

$$
\begin{aligned}
H(0) & =U(0)=E_{Q}\left[e^{-r t} V(T)\right] \\
& =E_{Q}\left[e^{-r t} H(T)\right]
\end{aligned}
$$

## The PDE Approach

An alternative approach to option pricing uses a partial differential equation model. The risk-neutral approach assumes trat the value of the replicating strategy and the derivative security are equal at $t=0, T$. In the PDE approach the price of the derivative security and value process are asswined equal.

$$
H(t)=x(t) S(t)+y(t) A(t)
$$

It is assumed that,

$$
H(t)=u(t, S(t))
$$

where $u(t, z)$ has a continuous first derivative with respect to $t \in[0, T]$ and continuous first and second derivative with respect to 2 .

Recall that the Its formula for
![](https://cdn.mathpix.com/cropped/2025_09_20_0e2ad360ecb2a5cadea0g-016.jpg?height=140&width=1134&top_left_y=177&top_left_x=284) is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here the Ith process is guen by

$$
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t)
$$

It follows that

$$
a(t)=\mu S(t) \quad b(t)=\sigma S(t)
$$

and

$$
\begin{aligned}
& u(t, z)=F(t, x) \\
d H= & u_{t} d t+\mu S(t) u_{2} d t \\
& +\sigma S(t) u_{2} d \omega(t) \\
& +\frac{1}{2} \sigma^{2} s^{2}(t) u_{2 z} d t \\
= & \left(u_{t}+\mu u_{2} s(t)+\frac{1}{2} \sigma^{2} s^{2}(t) u_{2 z}\right) d t \\
& +\sigma s(t) u_{2} d \omega
\end{aligned}
$$

Now recalling that the self financing assumption is given by

$$
d H=x(t) d S(t)+y(t) d A(t)
$$

using

$$
\begin{gathered}
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t) \\
d A(t)=r A(t) d t
\end{gathered}
$$

gives

$$
\begin{aligned}
d H= & x(t)[\mu s(t) d t+\sigma s(t) d \omega(t)] \\
& +y(t) r A(t) d t \\
= & {[x(t) \mu s(t)+y(t) r A(t)] d t } \\
& +x(t) \sigma s(t) d \omega(t)
\end{aligned}
$$

previously it was shown that

$$
\begin{aligned}
d H= & \left(u_{t}+\mu u_{z} s(t)+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z z}\right) d t \\
& +\sigma s(t) u_{z} d w
\end{aligned}
$$

Assuming uniqueness of 'Its proccess requires that these expressions are equal. Equating differentials gives

$$
\begin{aligned}
x(t) & \mu S(t)+y(t) r A(t) \\
& =u_{t}+\mu u_{z} s(t)+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z z}
\end{aligned}
$$

$$
x(t) \sigma s(t)=\sigma s(t) u_{2}
$$

The second equation implies that

$$
u_{2}(t, S(t))=x(t)
$$

using this expression in the first equation gives

$$
\begin{aligned}
& x(t) \mu s(t)+y(t) r A(t) \\
& =u_{t}+\mu u_{z} s(t)+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z z} \\
& \Rightarrow \mu y_{z} s(t)+y(t) r A(t) \\
& =u_{t}+\mu u_{z} s(t)+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z z} \\
& \Rightarrow y(t) r A(t)=u_{t}+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z z} \\
& \Rightarrow y(t)=\frac{1}{r A(t)}\left[u_{t}+\frac{1}{2} \sigma^{2} s^{2}(t) u_{z 2}\right]
\end{aligned}
$$

Thus,

$$
\begin{gathered}
x(t)=u_{2} \\
y(t)=\frac{1}{r A(t)}\left[u_{t}+\frac{1}{2} \sigma^{2} s^{2}(t) u_{22}\right]
\end{gathered}
$$

but the replication condition is given by

$$
H(t)=x(t) S(t)+y(t) A(t)
$$

and

$$
u(t, s(t))=H(t)
$$

50

$$
\begin{aligned}
& u(t, s(t))=u_{2}(t, s(t)) s(t) \\
& \quad+\frac{1}{r}\left[u_{t}(t, s(t))+\frac{1}{2} \delta^{2} s^{2}(t) u_{2 z}\right]
\end{aligned}
$$

but $z=s(t)$ so,

$$
\begin{aligned}
u(t, z)= & u_{z}(t, z) z \\
& +\frac{1}{r}\left[u_{t}(t, z)+\frac{1}{2} \sigma^{2} z^{2} u_{z z}\right) \\
\Rightarrow r u_{(t, z)}= & r z u_{z}(t, z)+u_{t}(t, z) \\
& +\frac{1}{2} \sigma^{2} z^{2} u_{z z}(t, z) \\
\Rightarrow \quad u_{t}(t, z)= & r u_{(t, z)}-r z u_{z}(t, z) \\
& -\frac{1}{2} \sigma^{2} z^{2} u_{z z}(t, z)
\end{aligned}
$$

The boundany condition on $t=T$ is given by

$$
h(z)=u(z, T) \quad z \in \mathbb{R}
$$

where $h(z)$ is the option payoff.

This PDE is the Black-Sholes equation.

## Strategies and Risk-Neutral Probability

Consider the discounded stock price

$$
\tilde{s}(t)=e^{-r t} s(t)
$$

for

$$
S(t)=S(0) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]
$$

it follows that

$$
\begin{aligned}
\tilde{S}(t) & =e^{-r t} S(t) \\
& =s(0) \exp \left[(\mu-r) t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]
\end{aligned}
$$

Theorem
For $s<t$

$$
E\left[\tilde{S}(t) \mid \tilde{f}_{s}^{\omega}\right]=\tilde{S}(s) e^{(\mu-r)(t-s)}
$$

where $\tilde{s}(t)$ is $\tilde{f}_{t}^{\omega}$-adapted. Proof

$$
\begin{aligned}
& \text { Consider } \\
& \begin{aligned}
& s(t)=s(0) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
& \text { since } s<t \\
& s(t)=s(0) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-s+s)\right. \\
&+\sigma(\omega(t)-\omega(s)+\omega(s))] \\
&=s(0) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right) s+\sigma \omega(s)\right] \\
& \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-s)+\sigma(\omega(t)-\omega(s))\right] \\
&=s(s) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-s)+\sigma(\omega(t)-\omega(s))\right]
\end{aligned}
\end{aligned}
$$

and

$$
\begin{aligned}
\tilde{s}(t)= & e^{-r t} s(t) \\
= & e^{-r t} s(s) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-s)\right. \\
& +\sigma(\omega(t)-\omega(s))]
\end{aligned}
$$

$$
\begin{aligned}
& =\tilde{s}(s) e^{-r(t-s)} \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-s)\right. \\
& \quad+\sigma(\omega(t)-\omega(s))] \\
& =\tilde{s}(s) \exp \left[(\mu-r)(t-s)-\frac{1}{2} \sigma^{2}(t-s)\right. \\
& \quad+\sigma(\omega(t)-\omega(s))]
\end{aligned}
$$

Now

$$
\begin{gathered}
E\left[\tilde{S}(t) \mid \tilde{J}_{s}^{\omega}\right]=E[\tilde{S}(\omega) \exp [(\mu-r)(t-s) \\
\left.\left.-\frac{1}{2} \sigma^{2}(t-s)+\sigma(\omega(t)-\omega(s)) \right\rvert\, \tilde{J}_{s}^{\omega}\right]
\end{gathered}
$$

Now $\tilde{s}(s)$ is $\tilde{f}_{s}^{\omega}$-measureable 50

$$
\begin{gathered}
E\left[\tilde{s}(t) \mid \tilde{f}_{s}^{\omega}\right]=\tilde{s}(s) E[\exp [(\mu-r)(t-s) \\
\left.\left.-\frac{1}{2} \sigma^{2}(t-s)+\sigma(\omega(t)-\omega(s)) \right\rvert\, J_{s}^{\omega}\right]
\end{gathered}
$$

Now the conditional expectation is rependent of $\mathcal{F}_{s}^{\omega}>0$

$$
\begin{aligned}
E\left[\tilde{s}(t) \mid \tilde{j}_{s}^{\omega}\right] & =\tilde{s}(s) E[\exp [(\mu-r)(t-s) \\
-\frac{1}{2} \sigma^{2}(t-s) & +\sigma(\omega(t)-\omega(s))]
\end{aligned}
$$

previously it was shown that the expectation of
$S(t)=S(0) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]$
is given by

$$
E[S(t)]=S(0) e^{\mu t}
$$

and the desired result follows

$$
\begin{aligned}
& E\left[\tilde{s}(t) \mid \tilde{f}_{s}^{\omega}\right]=\tilde{s}(s) E[\exp [(\mu-r)(t-s) \\
& \left.-\frac{1}{2} \sigma^{2}(t-s)+\sigma(\omega(t)-\omega(s))\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\tilde{S}(s) e^{(\mu-r)(t-s)} \\
\Rightarrow E\left[\tilde{S}(t) \mid \tilde{J}_{s}^{\omega}\right] & =\tilde{S}(s) e^{(\mu-r)(t-s)}
\end{aligned}
$$

Note that if $\mu=r$ then $\tilde{s}(t)$ is a martingale.

The next tast is to construct a probability measure such that $\tilde{J}(t)$ is a martingale. This is denoted as the risk-neutral probability $Q$.
Now,

$$
\tilde{s}(t)=s(0) \exp \left[(\mu-r) t \cdot \frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]
$$

recall that

$$
\exp \left[\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]
$$

is a martingale.

Let

$$
\omega_{Q}(t)=t\left(\frac{\mu-r}{\sigma}\right)+\omega(t)
$$

Then

$$
\begin{aligned}
\tilde{s}(t) & =s(0) \exp \left[(\mu-r) t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
& =s(\sigma) \exp \left\{-\frac{1}{2} \sigma^{2} t+\sigma[(\mu-r) t+\omega(t)]\right\} \\
& =s(\sigma) \exp \left[-\frac{1}{2} \sigma^{2} t+\sigma \omega_{Q}(t)\right]
\end{aligned}
$$

Now if a probability measure $Q$ can be constructed such that $\omega_{Q(t)}$ is a weiner process, then $\tilde{\zeta}(t)$ is a martingale with respect to $Q$ and the natural filtration $\mathcal{F}_{t}^{\omega}=\mathcal{F}$.

Next determine is $\omega_{Q}(t)$ is a wiener process. Recall that a wiener process is defined by

1) $\omega(0)=0$
2) For $0 \leqslant s<t<\infty$ the increment $\omega(t)-\omega(s)$ has a normal distribution with zero mean and variance ( $t-s$ ).
3) For every $m \geqslant 0$ and the partition

$$
0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{m}
$$

the non-overlapping increments

$$
\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)
$$

for $n=0,1,2, \ldots, m-1$ are independent.
4) $\omega(t)$ is continuous

Now since $\omega(t)$ is a Wener process and $\omega_{Q}(t)$ is given Dy

$$
\omega_{Q}(t)=t\left(\frac{\mu-r}{\sigma}\right)+\omega(t)
$$

It follows that

$$
\omega_{Q}(0)=\omega(0)=0
$$

so (1) is satisfied. Now for $s<t$

$$
\begin{aligned}
\omega_{Q}(t)-\omega_{Q}(s) & =\frac{(\mu-r)(t-s)}{\sigma} \\
+ & (\omega(t)-\omega(s))
\end{aligned}
$$

Now

$$
\begin{gathered}
E\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=E\left[\frac{(\mu-r)(t-s)}{\Delta}\right] \\
+E[\omega(t)-\omega(s)]
\end{gathered}
$$

but

$$
E[\omega(t)-\omega(s)]=0
$$

by definition of a weiner process, so

$$
E\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=\frac{(\mu-r)(t-s)}{\sigma} \neq 0
$$

and

$$
\begin{aligned}
\text { Uar } & {\left[\omega_{Q}(t)-\omega_{Q}(s)\right] } \\
= & E\left[\left(\omega_{Q}(t)-\omega_{Q}(s)\right)^{2}\right] \\
- & \left(E\left[\omega_{Q}(t)-\omega_{Q}(s)\right]\right]^{2} \\
= & E\left[\left(\omega_{Q}(t)-\omega_{Q}(s)\right)^{2}\right] \\
& -\frac{(\mu-r)^{2}(t-s)^{2}}{\sigma^{2}}
\end{aligned}
$$

Now

$$
\begin{aligned}
& E\left[\left(\omega_{Q}(t)-\omega_{Q}(s)\right)^{2}\right] \\
= & E\left[\left\{\frac{(\mu-r)_{(t-s)}}{\sigma}+(\omega(t)-\omega(s))\right\}^{2}\right] \\
= & E\left[\left(\frac{(\mu-r)(t-s)}{\sigma}\right)^{2}\right]
\end{aligned}
$$

$$
\begin{aligned}
& +2 E[(\mu-r)(t-s)(\omega(t)-\omega(s))] \\
& +E\left[(\omega(t)-\omega(s))^{2}\right] \\
& =\left[\left(\mu-\frac{r x(t-s)}{0}\right]^{2}+t-s\right.
\end{aligned}
$$

since

$$
\begin{gathered}
E[\omega(t)-\omega(s))]=0 \\
E\left[\left(\frac{(\mu-r)(t-s)}{\sigma}\right)^{2}\right]=\left[\left(\mu-\frac{r x(t-s)}{\sigma}\right]^{2}\right. \\
\text { Bringing things together gives } \\
\operatorname{Uar}\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=E\left[\left(\omega_{Q}(t)-\omega_{Q}(s)\right)^{2}\right] \\
-\frac{(\mu-r)^{2}(t-s)^{2}}{\sigma^{2}} \\
=t-s
\end{gathered}
$$

## Thus

$E\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=\frac{(\mu-r)(t-s)}{\sigma} \neq \gamma$
$\operatorname{var}\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=t-s$
Next, consider two non-overtaping intervals $t_{1}<t_{2}<s_{1}<s_{2}$. If the covarience of the intervals is zero they are independent.

$$
\begin{aligned}
\operatorname{Cov} & {\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}(s)\right)\right] } \\
= & E\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}(s)\right)\right] \\
& -E\left[\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right] E\left[\omega_{Q}\left(s_{2}\right)-\omega_{Q}(s)\right]
\end{aligned}
$$

Now previously it was shown

$$
\begin{aligned}
& E\left[\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right]=\frac{(\mu-r)\left(t_{2}-t_{1}\right)}{\sigma} \\
& E\left[\omega_{Q}\left(s_{2}\right)-\omega_{Q}(s)\right]=\left(\mu-\frac{r)}{\sigma} s_{2}-s_{1}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
E & {\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}\left(s_{1}\right)\right)\right]\right.} \\
=E & {\left[\left\{\left(\mu-\frac{r)\left(t_{2}-t_{1}\right)}{\sigma}+\omega\left(t_{2}\right)-\omega\left(t_{1}\right)\right\}\right.\right.} \\
& \left\{\left(\mu-\frac{r)\left(s_{2}-s_{1}\right)}{\sigma}+\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\right\}\right] \\
= & E\left[\left(\mu-\frac{r x\left(t_{2}-t_{1}\right)}{\sigma} \frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma}\right]\right. \\
& +E\left[\frac{(\mu-r)\left(t_{2}-t_{1}\right)\left(\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\right)}{\sigma}\right] \\
& +E\left[\frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma}\left(\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right)\right] \\
& +E\left[\left(\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\left(\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right)\right]\right. \\
N & \theta \omega \\
& E\left[\left(\mu-\frac{r x\left(t_{2}-t_{1}\right)}{\sigma}(\mu-r)\left(s_{2}-s_{1}\right)\right]\right. \\
\sigma &
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{(\mu-r)\left(t_{2}-t_{1}\right)}{\sigma} \frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma} \\
& E\left[\frac{(\mu-r)\left(t_{2}-t_{1}\right)\left(\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\right)}{\sigma}\right] \\
& =\frac{(\mu-r)\left(t_{2}-t_{1}\right)}{\sigma} E\left[\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\right] \\
& =0 \\
& E\left[\frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma}\left(\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right)\right] \\
& =\left(\mu-\frac{r)\left(s_{2}-s_{1}\right)}{\sigma} E\left[\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right]\right. \\
& =0
\end{aligned}
$$

Where the last two relations follow from

$$
E\left[\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right]=0
$$

and finally

$$
E\left[\left(\omega\left(s_{2}\right)-\omega\left(s_{1}\right)\right)\left(\omega\left(t_{1}\right)-\omega\left(t_{2}\right)\right)\right]=0
$$

since $\omega(t)$ is a weiner process. Bringing things together gives

$$
\begin{gathered}
E\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}\left(s_{1}\right)\right)\right] \\
=\frac{(\mu-r)\left(t_{2}-t_{1}\right)}{\sigma} \frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma}
\end{gathered}
$$

and finally

$$
\begin{gathered}
\operatorname{Cov}\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}\left(s_{1}\right)\right]\right. \\
=E\left[\left(\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right)\left(\omega_{Q}\left(s_{2}\right)-\omega_{Q}\left(s_{1}\right)\right)\right] \\
-E\left[\omega_{Q}\left(t_{2}\right)-\omega_{Q}\left(t_{1}\right)\right] E\left[\omega_{Q}\left(s_{2}\right)-\omega_{Q}\left(s_{0}\right)\right] \\
=\frac{(\mu-r)\left(t_{2}-t_{1}\right)}{\sigma} \frac{(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma} \\
-\frac{(\mu-r)\left(t_{2}-t_{1}\right)(\mu-r)\left(s_{2}-s_{1}\right)}{\sigma}
\end{gathered}
$$

$=0$
Finally for tem (4) $\omega_{Q}(t)$ will be continuous since $1 / 6(\mu-r) t$ and $\omega(t)$ are continuous.

It is seen that $\omega_{0}(t)$ satisfies all requirements of a wiener process accept zero mean for the increments. Where

$$
E\left[\omega_{Q}(t)-\omega_{Q}(s)\right]=\frac{(\mu-r)(t-s)}{\sigma}
$$

Now, returing to

$$
\omega_{Q}(t)=\frac{(\mu-r)}{\sigma} t+\omega(t)
$$

let

$$
b=\frac{(\mu-r)}{\sigma}
$$

then

$$
\omega_{Q}(t)=6 t+\omega(t)
$$

Note that

$$
b=\frac{(\mu-r)}{\sigma}
$$

is called the market price of risk
Recall that the distribution of the weiner process is given by

## $\omega(t) \sim \operatorname{Normal}(0, t)$

denote this distribution by

$$
p(x)=\frac{1}{\sqrt{2 \pi t}} e^{-x^{2} / 2 t}
$$

Thus it has been shown that $E_{P}\left(\omega_{Q}(t)\right)=\int_{-\infty}^{-\infty}(b t+x) \frac{1}{2 \pi t} e^{-x^{2} b t} d x$

## $=b t$

Now consider the distribution

## Normal $(b t, t)$

and dende it by

$$
q(x)=\frac{1}{\sqrt{2 \pi t}} e^{-(x+b t)^{2} / 2 t}
$$

It follows that

$$
E_{Q}\left[\omega_{Q}(t)\right]=\frac{1}{2 \pi t} \int_{-\infty}^{\infty}(x+b t) e^{-(x+b t)^{2} / 2 t} d x
$$

let $y=x+b t \Rightarrow d y=d x$, so

$$
\begin{aligned}
E_{Q}\left[\omega_{Q}(t)\right] & =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\Delta} y e^{-y^{2} / \partial t} d y \\
& =0
\end{aligned}
$$

Thus for the distribution $q(x)$
$\omega_{Q}(t)$ has zero mean: Now consider the integral

$$
\begin{aligned}
& E_{Q}\left[\omega_{Q}(t)\right]=\frac{1}{2 \pi t} \int_{-\infty}^{\infty}(x+b t) e^{-(x+b t)^{2} / 2 t} d x \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty}(b t+x) e^{-\left(x^{2}+2 b x t+b^{2} t^{2}\right) / 2 t} d x \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty}(b t+x) e^{-\left(2 b x t+b^{2} t^{2}\right) / 2 t} e^{-x^{2} / 2 t} d x \\
& =\int_{-\infty}^{\infty}(b t+x) e^{-b x-\frac{1}{2} b^{2} t} \frac{1}{\sqrt{2 \pi t}} e^{-x^{2} / 2 t} d x
\end{aligned}
$$

let

$$
f_{\omega(t)}(x)=\frac{1}{\sqrt{2 \pi t}} e^{-x^{2} / 2 t}
$$

then
$E_{Q}\left[\omega_{Q}(t)\right]=\int_{-\infty}^{\infty}(b t+x) e^{-b x-\frac{1}{2} b^{2} t} f_{\omega(t)}(x) d x$
Now this can be converted
to the measure theoretic form by noting that

$$
d P=f_{\omega(t)}(x) d x
$$

so

$$
E_{Q}\left[\omega_{Q}(t)\right]=\int_{\Omega}(b t+\omega(t)) e^{-b \omega(t)-\frac{1}{2} b^{2} t} d P
$$

For $A C \Omega, A \in \mathcal{F}$ define a new measure $Q$ such tat

$$
Q(A)=\int_{A} e^{-\frac{1}{2} b^{2} t-b \omega(t)} d P
$$

It then follows that

$$
\begin{aligned}
E_{Q}\left[\omega_{Q}(t)\right] & =\int_{\Omega}(b t+\omega(t)) d Q \\
& =0
\end{aligned}
$$

and

$$
E_{Q}\left[\omega_{Q}(t)\right]=E_{P}\left[e^{-\frac{1}{\partial} b^{2} t-b \omega(t)} \omega_{Q}(t)\right]
$$

the rardom variable

$$
\mu(t)=e^{-\frac{1}{2} b^{2} t-b \omega(t)}
$$

plays the role of a density of $Q$ with respect to $P$. Note that $M(t)>0$ for all $t$ and that

$$
\begin{aligned}
& \int_{\Omega} M(t) d P=\int_{-\infty}^{\infty} e^{-\frac{1}{2} b^{2} t-b x} \frac{1}{\sqrt{2 \pi t}} e^{-x^{2} / 2 t} d x \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} e^{-\left(x^{2}+b^{2} t^{2}+2 b t\right) / 2 t} d x \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} e^{-(x+b t)^{2} / 2 t} d x \\
& =1
\end{aligned}
$$

which is required for a probobility density.

## Gersanow Theorem (simple version)

A version of the bersanou theorem can be stated as, the process

$$
\omega_{Q}(t)=b t+\omega(t)
$$

is a weiner process under the prabability $Q$ defined by

$$
Q(A)=\int_{A} e^{-\frac{1}{2} b^{2} T-b \omega(T)} d P
$$

## Proof

Recall that the properties of a martingale are given by

1) $\omega(0)=0$
2) For $0 \leqslant s<t<\infty$ the increment $\omega(t)-\omega(s)$ has a normal distribution with zero mean and variance ( $t-s$ ).
3) For every $m \geqslant 0$ and the partition

$$
0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{m}
$$

the non-overlapping increments

$$
\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)
$$

for $n=0,1,2, \ldots, m-1$ are independent.
4) $\omega(t)$ is continuous

Propert, (1) and (4) have been proven. Also, the variance and and mean have been shown the satisfy the requirements of a wiener process and it has been shown that the increments of $\omega_{Q}(t)$ are independent. So it only needs to be shown that they have a normal distribution.
consider the partition,

$$
0=t_{0}<t_{1}<t_{2}<\cdots<t_{n}=T
$$

and

$$
a_{1}, a_{2}, \ldots, a_{n} \in \mathbb{R}
$$

The cumulative distribution function is computed by considering the event

$$
A=\bigcap_{i=1}^{n}\left\{\omega_{Q}\left(t_{i}\right)-\omega_{Q}\left(t_{i-1}\right) \leqslant a_{i}\right\}
$$

and computing $Q$ from the expectation.

$$
\begin{aligned}
Q(A) & =E_{Q}\left[\underline{1}_{A}\right] \\
& =E_{P}\left[\underline{1}_{A} e^{-b \omega(t)-\frac{1}{2} b^{2} t}\right]
\end{aligned}
$$

For any random variable I

$$
\begin{array}{r}
\int_{\Omega} I e^{-b w(t) \cdot \frac{1}{2} b^{2} t} d P \\
=\int_{\Omega} I d Q
\end{array}
$$

Now the indicator of the intersection is the product
of the indicators so
$\mathbb{1}_{A}=\prod_{i=1}^{n} \mathbb{1}\left\{\omega_{Q}\left(t_{i}\right)-\omega_{Q}\left(t_{i-1}\right) \leqslant a_{i}\right\}$
but

$$
\begin{aligned}
\omega_{Q}\left(t_{i}\right) & -\omega_{Q}\left(t_{i-1}\right)=\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right) \\
& +b\left(t_{i}-t_{i-1}\right)
\end{aligned}
$$

50

$$
\underline{11}_{A}=\prod_{i=1}^{n} \underline{1}^{n}\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leqslant a_{i}\right\}
$$

Now

$$
\begin{gathered}
e^{-\sigma \omega(t)-\frac{1}{\partial b^{2} t}} \frac{11}{1}\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right)\right\} \\
=e^{-\sigma\left(\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)\right)-\frac{1}{2} b^{2}\left(t_{i}-t_{i-1}\right)} \\
\underline{1}\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leqslant a_{i}\right\}
\end{gathered}
$$

50

$$
\begin{aligned}
Q(A)=E_{P} & {\left[\prod_{i=1}^{n} e^{-\left(\omega\left(t_{i}\right)-\omega\left(t_{(-1)}\right)-\frac{1}{d} b^{2}\left(t_{i}-t_{i-1}\right)\right)}\right.} \\
& \left.\underline{1}\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leqslant a_{i}\right\}\right]
\end{aligned}
$$

since the increments are independent it follows that
$Q(A)=E_{P}\left[\prod_{i=1}^{n} e^{-\left(\omega\left(t_{i}\right)-\omega\left(t_{(-1)}\right)-\frac{1}{\partial b^{2}}\left(t_{i}-t_{i-1}\right)\right)}\right.$

$$
\begin{aligned}
& \frac{11}{\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leqslant a_{i}\right\}} \\
= & \prod_{i=1}^{n} E_{p}\left[e^{\left.-\left(\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)\right)-\frac{1}{\partial b^{2}\left(t_{i}-t_{i}-1\right)}\right)}\right.
\end{aligned}
$$

Now

$$
\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right) \sim \text { Normal }\left(0, t_{i}-t_{i-1}\right)
$$

Consider the case where a random variable

$$
\bar{X} \sim \operatorname{Normal}(0, t)
$$

then

$$
E_{p}\left[e^{-b \bar{x}-\frac{1}{\partial b^{2}} t} \underline{1}\{\bar{x}+b t \leqslant a\}\right]
$$

$$
\begin{aligned}
& =\int_{x+b t \leqslant a} e^{-b x-\frac{1}{a} b^{2} t} \sqrt{2 \pi t} e^{-x^{2} / 2 t} d x \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{x+b t \leqslant a} e^{-\left(\frac{x^{2}}{2 t}+b x+\frac{1}{2} b^{2} t\right)} d x \\
& =\frac{1}{2 \pi t} \int_{x+b t \leqslant a} e^{-\left(x^{2}+2 b t x+b^{2}\right) / 2 t} d x \\
& =\frac{1}{2 \pi t} \int_{x+b t \leqslant a} e^{-(x+b t)^{2} / 2 t} d x
\end{aligned}
$$

let $y=x+b t \Rightarrow d y=d x$ so

$$
\begin{aligned}
E_{p}\left[e^{-b X-\frac{1}{2} b^{2} t}\right. & 11\{\bar{x}+b t \leqslant a\}] \\
& =\frac{1}{2 \pi t} \int_{y \leqslant a} e^{-y^{2} / 2 t} d y
\end{aligned}
$$

but $x \sim \operatorname{Normal}(0, t)$ thus

$$
\frac{1}{2 \pi t} \int_{y \leqslant a} e^{-y^{2} / 2 t} d y=P(\bar{x} \leqslant a)
$$

thus

$$
E_{P}\left[e^{-b \bar{x}-\frac{1}{2} b^{2} t} \underline{1}\{\bar{x}+b t \leqslant a\}\right]=P(\bar{x} \leqslant a)
$$

so using $\bar{x}=\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)$ and $t=t_{i}-t_{c-1}$

$$
\begin{aligned}
E_{p}\left[e^{\left.-\left(w\left(t_{i}\right)-w\left(t_{(-1}\right)\right)-\frac{1}{\partial b^{2}}\left(t_{i}-t_{i}-1\right)\right)}\right. & \frac{11}{-\left\{w\left(t_{i}\right)-w\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leqslant a_{i}\right\}} \\
= & P\left(w\left(t_{i}\right)-w\left(t_{i-1}\right) \leqslant a_{i}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
Q(A) & =\prod_{i=1}^{n} E_{P}\left[e^{-\left(\omega\left(t_{i}\right)-\omega\left(t_{(-1)}\right)-\frac{1}{\partial} b^{2}\left(t_{i}-t_{i-1}\right)\right)}\right. \\
& \left.\quad \underline{1}\left\{\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right)+b\left(t_{i}-t_{i-1}\right) \leq a_{i}\right\}\right] \\
& =\prod_{i=1}^{n} P\left(\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right) \leq a\right) \\
& =\prod_{i=1}^{n} Q\left(A_{i}\right) \\
& =\prod_{i=1}^{n} Q\left(\left\{\omega_{Q}\left(t_{i}\right)-\omega\left(t_{i-1}\right) \leq a\right\}\right)
\end{aligned}
$$

The desired result follows by equating components of the product.

$$
\begin{aligned}
& Q\left(\left\{\omega_{Q}\left(t_{i}\right)-\omega\left(t_{i-1}\right) \leqslant a\right\}\right) \\
& =P\left(\omega\left(t_{i}\right)-\omega\left(t_{i-1}\right) \leqslant a\right)
\end{aligned}
$$

which is a normal distribution. This result is called the Eirsanou theorem which can be exterder
to the case where $b$ is $a$ random process.

## Theorem

The stochastic processes for the asset price and discounted asset price are given by,

$$
\begin{gathered}
d S(t)=r S(t) d t+\sigma S(t) d \omega_{Q}(t) \\
d \tilde{S}(t)=\tilde{S}(t) \sigma d \omega_{Q}(t)
\end{gathered}
$$

## Proof

If $s(t)$ is given

$$
S(t)=S(0) \exp \left\{r t-\frac{1}{\partial} \sigma^{2} t+\sigma \omega_{Q}(t)\right\}
$$

then

$$
\tilde{s}(t)=s(0) \exp \left\{-\frac{1}{2} \sigma^{2} t+\sigma \omega_{Q}(t)\right\}
$$

as expected.
Recall the Itó formula for
a function of an Itô process is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, s(t))=F_{t} d t+a(t) F_{x} d t \\
& \quad+b(t) F_{x} d \omega(t)+\frac{1}{2} b^{2}(t) F_{x x} d t
\end{aligned}
$$

Here

$$
\begin{gathered}
a(t)=0 \quad b(t)=1 \\
\omega(t)=\omega_{Q}(t) \\
F\left(t, \omega_{Q}(t)\right)=s(0) \exp \left\{r t-\frac{1}{\partial} \sigma^{2} t+\sigma \omega_{Q}(t)\right\}
\end{gathered}
$$

It follows that

$$
\begin{aligned}
& F_{t}=\frac{\partial F}{\partial t}=\left(r-\frac{1}{2} \sigma^{2} t\right) s(t) \\
& F_{x}=\frac{\partial F}{\partial x}=\sigma s(t)
\end{aligned}
$$

$$
\begin{aligned}
F_{x x}=\frac{\partial^{2} F}{\partial x^{2}}= & \sigma^{2} s(t) \\
s o & \\
d s(t)= & \left(r-\frac{1}{2} \sigma^{2} t\right) s(t) d t \\
& +\sigma s(t) d \omega_{Q}(t) \\
& +\frac{1}{2} \sigma^{2} s(t) d t \\
\Rightarrow d s(t)= & r s(t) d t+\sigma s(t) d \omega_{Q}(t)
\end{aligned}
$$

which is the desired result. To complete the next part recall that the product rule for an Itô process is given by

$$
\begin{aligned}
d(\bar{x}(t) \bar{I}(t))= & \bar{X}(t) d \bar{I}(t)+\bar{I}(t) d \bar{X}(t) \\
& +b_{x}(t) b_{y}(t) d t
\end{aligned}
$$

Here

$$
\bar{X}(t)=e^{-r t} \quad \bar{I}(t)=s(t)
$$

$$
\begin{aligned}
& b_{x}(t)=0 \quad b_{y}(t)=1 \\
& d \Psi(t)=d s(t)=r s(t) d t+\sigma s(t) d \omega_{Q}(t) \\
& d \bar{x}(t)=-r e^{-r t} d t \\
& s o \\
& d \tilde{s}(t)=d\left(e^{-r t} s(t)\right) \\
& =-r e^{-r t} s(t) d t+e^{-r t} d s(t) \\
& =-r e^{-r t} s(t) d t+e^{-r t} r s(t) d t \\
& +e^{-r t} \sigma s(t) d \omega_{Q}(t) \\
& =\sigma \tilde{s}(t) d \omega_{Q}(t)
\end{aligned}
$$

thus the desired result is obtained.

$$
d \tilde{S}(t)=\sigma \tilde{S}(t) d \omega_{Q}(t)
$$

## Self Financong strategies

In discrete time models strategies were assumed predectable. The strategy defined by $(X(n), y(n))$ is assumed to be known at time $n-1$ and trus $\Im_{n-1}$-measureable.
In continuous time models if the stochastic processes is continuous, which is the case for a weiner process, it is sufficent that the strategy be adopted, that is $\Im_{n}$ - measureable.

## Definition Trading strategy

A trading strategy in the undelying, (single-asset) market is an adapted process.

$$
(x, y)=\{(x(t), y(t)): t \in[0, T]\}
$$

with $x(t)$ indicating the number of shares in the asset and
$y(t)$ the amount of the riskfree asset held at time $t$.

## Definition Value Process

The value of the trading strategy $(x, y)$ is the process

$$
\begin{gathered}
U_{x y}=\left(U_{x y}(t)\right) t \in[0, T] \\
U_{x y}=x(t) S(t)+y(t) A(t)
\end{gathered}
$$

In the discussion if the strategy is obvious the subscripts are droped.

## Definition Self Financing

The stratgey $(x, y)$ is self finanang If

$$
d V(t)=x(t) d s(t)+y(t) d A(t)
$$

but

$$
\begin{gathered}
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t) \\
d A(t)=r A(t) d t
\end{gathered}
$$

so

$$
\begin{aligned}
d v(t)= & x(t)(\mu S(t) d t+\sigma S(t) d \omega(t)) \\
& y(t) r A(t) d t \\
= & (\mu x(t) s(t)+r y(t) A(t)) d t \\
& +\sigma x(t) S(t) d \omega(t)
\end{aligned}
$$

The stochastic processes $x(t)$ and $y(t)$ are assumed to be square integrable.

$$
\begin{aligned}
& \int_{0}^{T} x^{2}(s) d s<\infty \\
& \int_{0}^{T} y^{2}(s) d s<\infty
\end{aligned}
$$

## Theorem

A strategl is self-financing if and only if

$$
d \tilde{V}(t)=x(t) d \tilde{S}(t)
$$

where $V(t)$ is the discounder value process

$$
\tilde{V}(t)=e^{-r t} V(t)
$$

## Proof

The proof requires that assuming self-finaning implies

$$
d \tilde{v}(t)=x(t) d s(t)
$$

and assuming the above relation implies self-financing.
Recall that a self-firancing strategy satisfies

$$
d V(t)=x(t) d S(t)+y(t) d A(t)
$$

First assume that $(x(t), y(t))$ is self financing.
Recall the product rule for stochastic differentials is given by

$$
d(X Y)=X d I+I d \bar{X}
$$

using

$$
\bar{X}=e^{-r t} \quad I=V(t)
$$

gives

$$
\begin{aligned}
d \tilde{v}(t) & =d\left(V(t) e^{-r t}\right) \\
& =e^{-r t} d V(t)+V(t) d\left(e^{-r t}\right) \\
& =e^{-r} d V(t)-r e^{-r t} V(t) d t
\end{aligned}
$$

Now it is assumed that $U(t)$ satisfies the self-finanaing condition so

$$
d V(t)=x(t) d S(t)+y(t) d A(t)
$$

and from the defintion of the value process

$$
V(t)=x(t) S(t)+y(t) A(t)
$$

and the risk-free investment satisfies

$$
\begin{aligned}
A(t) & =A(0) e^{r t} \\
\Rightarrow d A(t) & =r A(t) d t
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
d \tilde{v}(t)= & e^{-r t} d V(t)-r e^{-r t} V(t) d t \\
= & e^{-r t}[x(t) d S(t)+y(t) d A(t)] \\
& -r e^{-r t}[x(t) S(t)+y(t) A(t)] d t \\
= & x(t) e^{-r t} d S(t)+y(t) e^{-r t} d A(t) \\
& +x(t) S(t)\left(-r e^{-r t}\right) d t \\
& -y(t) r e^{-r t} A(t) d t
\end{aligned}
$$

$$
\begin{aligned}
= & x(t)\left[e^{-r t} d s(t)+s(t)\left(-r e^{-r t}\right) d t\right] \\
& +y(t)\left[e^{-r t} d A(t)-r e^{-r t} A(t) d t\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
& e^{-r t} d s(t)+s(t)\left(-r e^{-r t}\right) d t \\
= & e^{-r t} d s(t)+s(t) d\left(e^{-r t}\right) \\
= & d\left(e^{-r t} s(t)\right) \\
= & d \tilde{s}(t)
\end{aligned}
$$

and

$$
\begin{aligned}
& e^{-r t} d A(t)-r e^{-r t} A(t) d t \\
= & e^{-r t} d A(t)-e^{-r t}(r A(r)) d t \\
= & e^{-r t} d A(t)-e^{-r t} d A(t) \\
= & 0
\end{aligned}
$$

Thus the desired result is obtained

$$
d \tilde{v}(t)=x(t) d \tilde{S}(t)
$$

To complete the proof assume that

$$
d \tilde{v}(t)=x(t) d \tilde{s}(t)
$$

Now

$$
\tilde{V}(t)=e^{-r t} V(t)
$$

so

$$
\begin{aligned}
d v(t) & =d\left(e^{r t} \tilde{v}(t)\right) \\
& =e^{r t} d \tilde{v}(t)+\tilde{v}(t) r e^{r t} d t \\
& =e^{r t} d \tilde{v}(t)+r V(t) d t
\end{aligned}
$$

but

$$
\begin{gathered}
d \tilde{v}(t)=x(t) d \tilde{s}(t) \\
v(t)=x(t) S(t)+y(t) A(t)
\end{gathered}
$$

So

$$
d v(t)=e^{r t} x(t) d \tilde{S}(t)+r v(t) d t
$$

but

$$
\begin{aligned}
& d \tilde{S}(t)=e^{-r t} d S(t)+s(t)\left(-r e^{-r t}\right) d t \\
& d A(t)=r A(t) d t
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
d v(t)= & e^{r t} x(t)\left[e^{-r t} d s(t)\right. \\
& \left.+s(t)\left(-r e^{-r t}\right) d t\right] \\
& +r(x(t) s(t)+y(t) A(t)) d t \\
= & x(t) d s(t)-r x(t) s(t) d t \\
& +r x(t) s(t) d t+y(t) r A(t) d t \\
= & x(t) d s(t)+y(t) d A(t)
\end{aligned}
$$

which is the desired result. Thus

$$
d \tilde{v}(t)=x(t) d \tilde{s}(t)
$$

if and only if

$$
d V(t)=x(t) d s(t)+y(t) d A(t)
$$

## Theorem

The process $x(t)$ and $v(0)$ determine the adapted process $y(t)$ so that $(x(t), y(t))$ is self franaing.

## Proof

From the previous theorem

$$
\begin{aligned}
& d \tilde{v}(t)=x(t) d \tilde{s}(t) \\
\Rightarrow \quad \tilde{v}(t) & =v(0)+\int_{0}^{t} x(t) d \tilde{s}(t)
\end{aligned}
$$

but

$$
\begin{aligned}
v(t) & =e^{r t} \tilde{v}(t) \\
& =x(t) s(t)+y(t) A(t)
\end{aligned}
$$

it follows that

$$
V(t)=x(t) s(t)+y(t) A(t)
$$

$$
\begin{aligned}
=e^{r t} & \left(v(0)+\int_{0}^{t} x(t) d \tilde{S}(t)\right) \\
\Rightarrow y(t)=\frac{1}{A(t)} & \left(e^{r t}\left[v(0)+\int_{0}^{t} x(t) d \tilde{S}(t)\right]\right. \\
& -x(t) s(t))
\end{aligned}
$$

## No Arbitrage Pinciple

## Definition

It is said that $(x(t), y(t))$ is an arbitrage opportunity, or an arbitrage

$$
\begin{aligned}
& V_{x y}(0)=0 \\
& V_{x y}(t) \geqslant-L
\end{aligned}
$$

for all $t$ and some constant $L$ and with positive probability

$$
V_{x y}\left(t^{\prime}\right)>0
$$

for some $t^{\prime}$.
It is assumed that a European derivative security is traded and its price is dendted by $H(t)=H$ as a given, $\mathcal{F}_{T}$-measureable random variable.

Adding the derivative security
to the risky and risk-free assets areates an extended market consisting of the assets,

$$
S(t), A(t), H(t)
$$

A trading strategy is now a triple $(x(t), y(t), z(t))$ with the value process

$$
V_{x y z}(t)=x(t) S(t)+y(t) A(t)+z(t) H(t)
$$

It is assumed that $H(t)$ is an ttô process and that

$$
\int_{0}^{T} z^{2}(t) d t<\infty
$$

so that the self firancing condition becomes

$$
\begin{aligned}
d v_{x y z}(t)=x(t) & d s(t)+y(t) d A(t) \\
& +z(t) d H(t)
\end{aligned}
$$

In practice it is usually assumed that $z(t)=1$ or -1 . The self financing condition then becomes

$$
\begin{aligned}
& V_{x y z}(T)-V_{x y z}(0)=\int_{0}^{T} x(t) d S(t) \\
& +\int_{0}^{T} y(t) d A(t)+H(T)-H(0)
\end{aligned}
$$

## Definition

The stratetgy $(x(t), y(t), z(t))$ is an arbitrage in the extended market

$$
\begin{aligned}
& V_{x y z}(0)=0 \\
& V_{x y z}(t)>-L
\end{aligned}
$$

for all $t$ and some constant $L$ and with positue probablity

$$
V_{x y 2}\left(t^{\prime}\right)>0
$$

for some $t^{\prime}$.

A fundamental assumption is that arbitrage opportinities do not exist in the extended market.

## Defintion

A strategy $(x, y)$ replicates the derivative security with payoff $H$ if

$$
H=V_{x y}(T)
$$

The market model is complete if every $f_{T}^{S}$ - measureable random variable $H$ can be replicated.

## Theorem

If $H$ is replicated and its price process $H(t)$ is an $E t o ̂$ process, the No Arbitrage Princple implies that for all $t$ in

$$
[0, T] \quad H(t)=V_{x y}(t)
$$

## Admissible Strategies

This discussion will begin by giving examples of strategies that are not in the cass of admissable strategies.

## Example: Doubling strategy

The dowbling strategy can be employed to make a riskless profit is a sequence of bair coin toss games A player of the game wins double the amount bet or loses the bet. If the player cloopts a strategy of doulding the bet on each loss a tetal amout bet is given be

$$
\begin{aligned}
\sum_{k=1}^{n} 2^{k-1} & =2^{0}+2^{1}+2^{2}+2^{3}+\cdots+2^{n-1} \\
& =1+2+4+8+\cdots+2^{n-1}
\end{aligned}
$$

$$
=\sum_{k=0}^{n-1} 2^{k}
$$

Now

$$
\sum_{k=0}^{n} r^{k}=\frac{1-r^{n+1}}{1-r}=\frac{r^{n+1}-1}{r-1}
$$

so with $r=2$

$$
\begin{aligned}
\sum_{k=1}^{n} 2^{k-1} & =\sum_{k=0}^{n-1} 2^{k}=\frac{2^{n}-1}{a-1} \\
& =2^{n}-1
\end{aligned}
$$

It follows that if the player wins the n'th game the payout is $2^{n}$. It follows that a risk-free profit of

$$
2^{n}-2^{n}+1=1
$$

is made when the player eventually wins the game. The probability of lossing $n$ straight games is

$$
a^{-n}
$$

As $n \rightarrow \infty$ this probability goes to zero. It follows that for $n<\infty$

$$
\begin{aligned}
& P(n<\infty)=\sum_{k=1}^{\infty} 2^{-k} \\
& =\lim _{n \rightarrow \infty} \frac{1-2^{-(n+1)}}{1-1 / 2}-1 \\
& =\lim _{n \rightarrow \infty} \frac{1-2^{-(n+1)}-1+1 / 2}{1-(1 / 2} \\
& =\lim _{n \rightarrow \infty} \frac{1 / 2-2^{(n+1)}}{1 / 2} \\
& =1
\end{aligned}
$$

Trus the probability that the number of toses before payout is finite is given by,

$$
P(n<\infty)=1
$$

since in an deal market there are unlimited funds can be borrowed thus the game can
be played cuntil it is won. However unlimited funds and waiting indefinitley are required to obtain the risk-free payout of $\$ 1$.

## Example Black-shotes Version

A strategil similar to the prevous example can be constructed using the Black-Scholes model. The strategy restricts rebalaraing to a countable set of times, $t_{n}, n=0,1,2, \ldots$ where $t_{n}<T$. Recall in the Black-Sholes molel the discounted asset prre is given by,
$\tilde{s}(t)=s(0) \exp \left\{(\mu-r) t-12 \sigma^{2} t+\sigma \omega(t)\right\}$
The value process is given by

$$
V(t)=x(t) S(t)+y(t) A(t)
$$

## where

$$
A(t)=A(0) e^{r t}
$$

and the self financing stratesy is given by

$$
d V(t)=x(t) d S(t)+y(t) d A(t)
$$

For simplicity assume $r=0$ and $A(0)=1$ and let
then

$$
m=\mu-\frac{1}{2} \sigma^{2}
$$

$$
\tilde{s}(t)=s(t)=s(0) e^{m t+\sigma \omega(t)}
$$

To construct an investment strategy that with prodobility doubles the initral investment assume that the initial investment is

$$
V(0)=1
$$

also assume $y(0)=0$
then

$$
x(0)=\frac{1}{S(0)}
$$

This position is held until $t_{1}$.
Now the strategy seeks to at least double the intral investment of 1. It will be shown that this is the case by proving that with probability 1 the initral investment is at least doulded.

Consider the probability that the investment des not double, now

$$
V\left(t_{1}\right)=\frac{S\left(t_{1}\right)}{S(0)}
$$

50

$$
P\left(v\left(t_{1}\right)<2\right)=P\left(\frac{1}{s(0)} s\left(t_{1}\right)<2\right)
$$

but

$$
s\left(t_{1}\right)=s(0) e^{m t_{1}+\sigma \omega\left(t_{1}\right)}
$$

50

$$
P\left(\frac{1}{s(0)} s\left(t_{1}\right)<2\right)=P\left(e^{m t_{1}+\sigma \omega\left(t_{1}\right)}<2\right)
$$

now

$$
\begin{aligned}
& e^{m t_{1}+\gamma \omega\left(t_{1}\right)}<2 \\
\Rightarrow & \omega\left(t_{1}\right)<\log \frac{2-m t_{1}}{6}
\end{aligned}
$$

then

$$
\begin{aligned}
P\left(e^{m t_{1}+\sigma \omega\left(t_{1}\right)}\right. & <2) \\
=P\left(\omega\left(t_{1}\right)\right. & \left.<\frac{1}{\sigma}\left(\log 2-m t_{1}\right)\right)
\end{aligned}
$$

but

$$
\omega\left(t_{1}\right) \sim \operatorname{Normal}\left(0, t_{1}\right)
$$

so

$$
P\left(\omega\left(t_{1}\right)<\frac{1}{\delta}\left(\log 2-m t_{1}\right)\right)
$$

$$
=N\left(\frac{1}{6 \mathbb{E}_{1}}\left(\log 2-m t_{1}\right)\right)
$$

where $N$ is the unit noronal cumulative distribution

$$
\begin{aligned}
& N\left(\frac{1}{\sigma \mathbb{E}_{1}}\left(\log 2-m t_{1}\right)\right) \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\frac{1}{\partial t_{1}}\left(\log 2-m t_{1}\right)} e^{-x^{2} / 2} d x
\end{aligned}
$$

let

$$
P=N\left(\frac{1}{\sigma \mathbb{E}_{1}}\left(\log 2-m t_{1}\right)\right)
$$

Now at $t_{1}$ choose $x\left(t_{1}\right)$ such that with probability $P V\left(t_{2}\right)<2$
From the definition of the value process at $t_{1}$,

$$
V\left(t_{1}\right)=x\left(t_{1}\right) S\left(t_{1}\right)+y\left(t_{1}\right)
$$

$$
\Rightarrow y\left(t_{1}\right)=v\left(t_{1}\right)-x\left(t_{1}\right) s\left(t_{1}\right)
$$

It follows that at $t=t_{2}$

$$
\begin{aligned}
v\left(t_{2}\right) & =x\left(t_{1}\right) s\left(t_{2}\right)+y\left(t_{1}\right) \\
\Rightarrow \quad x\left(t_{1}\right) & =\frac{v\left(t_{2}\right)-y\left(t_{1}\right)}{s\left(t_{2}\right)}
\end{aligned}
$$

assume that $V\left(t_{2}\right)$ is the limiting value of 2 then

$$
\begin{aligned}
& x\left(t_{1}\right)=\frac{2-v\left(t_{1}\right)+x\left(t_{1}\right) s\left(t_{1}\right)}{s\left(t_{2}\right)} \\
\Rightarrow & x\left(t_{1}\right)\left(s\left(t_{2}\right)-s\left(t_{1}\right)\right)=2-v\left(t_{1}\right) \\
\Rightarrow & x\left(t_{1}\right)=\frac{2-v\left(t_{1}\right)}{s\left(t_{2}\right) \cdot s\left(t_{1}\right)}
\end{aligned}
$$

and

$$
\begin{aligned}
y\left(t_{1}\right) & =v\left(t_{1}\right)-x\left(t_{1}\right) s\left(t_{1}\right) \\
& =v\left(t_{1}\right)-\frac{\left(\partial-v\left(t_{1}\right)\right) s\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{v\left(t_{1}\right)\left(s\left(t_{2}\right)-s\left(t_{1}\right)\right)-\left(2-v\left(t_{1}\right)\right) s\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)} \\
& =\frac{v\left(t_{1}\right) s\left(t_{2}\right)-v\left(t_{1}\right) s\left(t_{1}\right)-2 s\left(t_{1}\right)+v\left(t_{1}\right) s\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)} \\
& =\frac{v\left(t_{1}\right) s\left(t_{2}\right)-2 s\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)}
\end{aligned}
$$

Now consider

$$
\begin{aligned}
& P\left(\frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}<\alpha\right) \\
& =P\left(\exp \left[\left(t_{2}-t_{1}\right) m+\sigma\left(\omega\left(t_{2}\right)-\omega\left(t_{1}\right)\right)\right]<\alpha\right) \\
& =P\left(\left(t_{2}-t_{1}\right) m+\sigma\left(\omega\left(t_{2}\right)-\omega\left(t_{1}\right)\right)<\log \alpha\right) \\
& =P\left(\omega\left(t_{2}\right)-\omega\left(t_{1}\right)<\frac{\log \alpha-\left(t_{2}-t_{1}\right) m}{\sigma}\right)
\end{aligned}
$$

but

$$
\begin{aligned}
& \omega\left(t_{2}\right)-\omega\left(t_{1}\right) \sim \operatorname{Normal}\left(0, t_{2}-t_{1}\right) \\
& \text { so } \\
& \begin{aligned}
P\left(\omega\left(t_{2}\right)-\omega\left(t_{1}\right)<\frac{\log \alpha-\left(t_{2}-t_{1}\right) m}{\sigma}\right) \\
=N\left(\frac{\log \alpha-\left(t_{2}-t_{1}\right) m}{\sigma \sqrt{t_{2}-t_{1}}}\right)
\end{aligned}
\end{aligned}
$$

where $N$ is the unit noronal cumulative distribution. Let

$$
P=N\left(\frac{\log \alpha-\left(t_{2}-t_{1}\right) m}{\sigma \sqrt{t_{2}-t_{1}}}\right)
$$

and solve for $\alpha$. For the specal case $t_{2}-t_{1}=t_{1}$ gives $\alpha=2$

Now using

$$
S\left(t_{2}\right)=\alpha S\left(t_{1}\right)
$$

it follows that

$$
\begin{aligned}
x\left(t_{1}\right) & =\frac{2-V\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)} \\
& =\frac{2-V\left(t_{1}\right)}{s\left(t_{1}\right)(\alpha-1)} \\
y\left(t_{1}\right) & =\frac{V\left(t_{1}\right) s\left(t_{2}\right)-2 s\left(t_{1}\right)}{s\left(t_{2}\right)-s\left(t_{1}\right)} \\
& =\frac{V\left(t_{1}\right) \alpha s\left(t_{1}\right)-2 s\left(t_{1}\right)}{s\left(t_{1}\right)(\alpha-1)} \\
& =s\left(t_{1}\right) \frac{\left(V\left(t_{1}\right) \alpha-2\right)}{s\left(t_{1}\right)(\alpha-1)} \\
& =\frac{\alpha V\left(t_{1}\right)-2}{\alpha-1} \\
& =\frac{\alpha V\left(t_{1}\right)-2+V\left(t_{1}\right)-V\left(t_{1}\right)}{\alpha-1}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{V\left(t_{1}\right)(\alpha-1)}{\alpha-1}+\frac{V\left(t_{1}\right)-2}{\alpha-1} \\
& =\frac{V\left(t_{1}\right)-2}{\alpha-1}+V\left(t_{1}\right)
\end{aligned}
$$

Trus

$$
\begin{aligned}
& x\left(t_{1}\right)=\frac{2-V\left(t_{1}\right)}{\delta\left(t_{1}\right)(\alpha-1)} \\
& y\left(t_{1}\right)=V\left(t_{1}\right)-\frac{2-V\left(t_{1}\right)}{\alpha-1}
\end{aligned}
$$

Now

$$
\begin{aligned}
& P\left(V\left(t_{2}\right)<2\right)=P\left(x\left(t_{1}\right) s\left(t_{2}\right)+y\left(t_{1}\right)<2\right) \\
= & P\left(\frac{\left(2-v\left(t_{1}\right)\right)}{s\left(t_{1}\right)(2-1)} s\left(t_{2}\right)+v\left(t_{1}\right)-\frac{2-v\left(t_{1}\right)}{\alpha-1}<2\right)
\end{aligned}
$$

$$
\begin{gathered}
=P\left(\frac{s\left(t_{2}\right)}{s\left(t_{1}\right)} \frac{\left(2-v\left(t_{1}\right)\right.}{\alpha-1}+\frac{(\alpha-1) v\left(t_{1}\right)}{\alpha-1}\right. \\
\left.-\frac{\left(2-v\left(t_{1}\right)\right)}{\alpha-1}<2\right)
\end{gathered}
$$

## Consider the argument

$$
\begin{aligned}
\frac{S\left(t_{2}\right)}{S\left(t_{1}\right)} & \frac{\left(\partial-V\left(t_{1}\right)\right.}{\partial-1}+\frac{(\alpha-1) V\left(t_{1}\right)}{\partial-1}-\frac{\left(\partial-V\left(t_{1}\right)\right)}{\partial-1} \\
& <2 \\
= & \frac{S\left(t_{2}\right)}{S\left(t_{1}\right)} \frac{\left(\partial-V\left(t_{1}\right)\right.}{\partial-1}+\frac{\alpha V\left(t_{1}\right)-V\left(t_{1}\right)}{\partial-1} \\
& \frac{\partial-V\left(t_{1}\right)}{\partial-1}<2 \\
= & \frac{S\left(t_{2}\right)}{S\left(t_{1}\right)} \frac{\left(\partial-V\left(t_{1}\right)\right)}{\partial-1}+\frac{\alpha V\left(t_{1}\right)-2}{d-1}<2
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}\left(\partial-v\left(t_{1}\right)\right)+\alpha v\left(t_{1}\right)-2<\partial(\alpha-1) \\
& \Rightarrow \frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}\left(\partial-v\left(t_{1}\right)<\partial(\alpha-1)-\alpha v\left(t_{1}\right)+2\right. \\
& =2 \alpha-2-\alpha v\left(t_{1}\right)+2 \\
& =\alpha\left(2-v\left(t_{1}\right)\right. \\
& \Rightarrow \frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}\left(\partial-\gamma\left(t_{1}\right)\right)<\alpha\left(\partial-v\left(t_{1}\right)\right) \\
& \Rightarrow \frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}<\alpha
\end{aligned}
$$

bringing things together gives

$$
P\left(V\left(t_{2}\right)<2\right)=P\left(\frac{S\left(t_{2}\right)}{S\left(t_{1}\right)}<\alpha\right)
$$

where $a$ is depermined by the relation

$$
P\left(V\left(t_{2}\right)<2\right)=P\left(\frac{s\left(t_{2}\right)}{s\left(t_{1}\right)}<\alpha\right)=P
$$

using this proceedure a step-wise continuous strategy $(x(t), y(t))$ can be constructed such that the value is less than 2.

Each step is independent since it is a weiner process the probability that the strategy is less than 2 for each step is then,

$$
p^{n}
$$

The probability that the value is always less than 2 is

$$
\lim _{n \rightarrow \infty} p^{n}=0
$$

It follows that for some $t V(t)>2$ with probability 1. At this time a risk-free profit where the initial investment is dowbled is had unfortunately it could take a long time

## Example

Here continuous time is considerd Recall that the asset price is given by

$$
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t)
$$

assume that both $r=0$ and $\mu=0$ so trat

$$
d s(t)=\sigma s(t) d \omega(t)
$$

Consider a discrete approximation with time step length, $h$, then

$$
s(t+h)-s(t)=\sigma s(t) \sqrt{h} \varepsilon
$$

where $\varepsilon= \pm 1$. It follows that

$$
s(t+h)=s(t)(1+\sigma \sqrt{h} \varepsilon)
$$

To implement a doubling strategy at time $t$ an $x(t)$ must be found so that in the positive scenerio an amount of money M(t) is earned which is sufficient to cover past losses and generate the additional income needen to dowble the money invested at time 0. In the positure scenerio, $\varepsilon=1$, so the price goes up. The amound of money earned is given by

$$
\begin{aligned}
& x(t)(s(t+h)-s(t)) \\
= & x(t)[s(t)(1+\sigma \sqrt{h})-s(t)] \\
= & x(t) s(t) \sigma \sqrt{h} \\
= & M(t)
\end{aligned}
$$

For return $M(t)$ it follows that

$$
x(t)=\frac{M(t)}{\sigma S(t) \sqrt{h}}
$$

As in the previous examples unlimited funds are availble for loans to cover loses which are carried over to the next rebalancing perood.
If $V(0)$ is arbitrary and taking inspiration from the precious result let

$$
x(t)=\frac{1}{\sigma \tilde{S}(t) \sqrt{T-t}}
$$

The risk-free component is computed using

$$
\begin{aligned}
& V(t)=x(t) S(t)+y(t) \\
& \Rightarrow y(t)=V(t)-x(t) S(t)
\end{aligned}
$$

where it has been assumed that $A(0)=1$ and $r=0$.
It is seen that $y(t)<0$ if $x(t) s(t)>V(t)$ intrating that money is deposited in the risk-free position and if $y(t)>0$ then $x(t) s(t)<v(t)$ so money is berrowed at the risk-free rate to cover loses.
In the following it will be shown that an arbitrary amount of money can be made in a specified time limit.

## Theorem

If $a(t)$ is a deterministic function then

$$
I(t)=\int_{0}^{t} a(s) d \omega(s)
$$

has a normal distribution with variance

$$
\int_{0}^{t} a^{2}(s) d s
$$

in addition the process $\bar{y}(t)$ is Caussion.

## Intuition

If the discrete version of the integral is considered,

$$
\sum_{i=0}^{n} a\left(t_{i}\right)\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)
$$

from the definition of a wiener process $w\left(t_{i+1}\right)-w\left(t_{i}\right)$ is gaussion with variance $a^{2}\left(t_{i}\right)\left(t_{i+1}-t_{i}\right)$. It follows that $I(t)$ is a gaussian process and that the sum is a gaussian with variace that is the
sum of the variance of the of each varrable. Thus

$$
\begin{aligned}
\sigma^{2} & =\sum_{i=0}^{n} a^{2}\left(t_{i}\right)\left(t_{i+1}-t_{i}\right) \\
& \approx \int_{0}^{t} a^{2}(s) d s
\end{aligned}
$$

## Theorem

For each $\mu>0$

$$
P(\min \{t: \tilde{v}(t) \geq M\} \leq T)=1
$$

## Proof

This proof is complicated and will be completed in three steps

## Step 1

An expression for $\tilde{V}(t)$ will be derived.
Previously it was shown that

$$
d \tilde{S}(t)=\sigma \tilde{S}(t) d \omega_{Q}(t)
$$

and for a self financing strategy

$$
d \tilde{v}(t)=x(t) d \tilde{s}(t)
$$

It follows that

$$
\begin{aligned}
d \tilde{v}(t) & =x(t) d \tilde{S}(t) \\
& =x(t) \circlearrowleft \tilde{S}(t) d \omega_{Q}(t)
\end{aligned}
$$

previously on argument was made for,

$$
x(t)=\frac{1}{\sigma \tilde{S}(t) \sqrt{T-t}}
$$

80

$$
d \tilde{V}(t)=\frac{1}{\sqrt{T-t}} d \omega_{Q}(t)
$$

and

$$
\tilde{v}(t)=\int_{0}^{t} \frac{1}{\sqrt{T-u}} d \omega_{Q}(u)
$$

From a previous theorem it follows the $\tilde{v}(t)$ is a gaussion process and has a gaussian distribution.

Let

$$
\gamma(t)=\int_{0}^{t} \frac{1}{T-u} d u
$$

Clearly $r(0)=0$ and $r(T)=\infty$. This integral can be evaluated.

$$
r(t)=\int_{0}^{t} \frac{1}{T-u} d u
$$

Let

$$
\begin{aligned}
\omega & =T-u \\
\Rightarrow-d \omega & =d u
\end{aligned}
$$

then

$$
r(t)=-\int_{T}^{T-t} \frac{1}{\omega} d \omega
$$

$$
\begin{aligned}
& =\int_{T-t}^{T} \frac{d \omega}{\omega} \\
& =\left.\ln \omega\right|_{T-t} ^{T} \\
& =\ln T-\ln (T-t)
\end{aligned}
$$

and

$$
\lim _{t \rightarrow T} r(t)=\infty
$$

## Step 2

It is claimed that $\omega_{Q}(Y(t))$ and $\tilde{v}(t)$ have the same distribution. Here the covariance of the processes is compared.
Assume $s \leqslant t$ then

$$
\begin{aligned}
E_{Q} & {[\tilde{v}(s) \tilde{v}(t)]=E\left[E\left[\tilde{v}(s) \tilde{v}(t) \mid \tilde{J}_{s}\right]\right] } \\
& =E\left[\tilde{v}(s) E\left[\tilde{v}(t) \mid \tilde{J}_{s}\right]\right] \\
& =E\left[\tilde{v}^{2}(s)\right] \\
& =\gamma(s)
\end{aligned}
$$

Note that it is assumed that $\tilde{v}(t)$ is a martingale and the last step follows from the previous treorem.
Also,

$$
\begin{aligned}
& E_{Q}\left[\omega_{Q}\left(r(s) \omega_{Q}(r(t))\right]\right. \\
= & E_{Q}\left[E_{Q}\left[\omega_{Q}(r(s)) \omega_{Q}(r(t)) \mid \mathcal{F}_{r(s)}\right]\right] \\
= & E_{Q}\left[\omega_{Q}(r(s)) E_{Q}\left[\omega_{Q}(r(t)) \mid \mathcal{F}_{r(s)}\right]\right] \\
= & E_{Q}\left[\omega_{Q}^{2}(r(s))\right] \\
= & r(s)
\end{aligned}
$$

Thus,

$$
\begin{aligned}
E_{Q}[\tilde{v}(s) \tilde{v}(t)] & =\min (\gamma(s), \gamma(t)) \\
E_{Q}\left[\omega_{Q}(s) \omega_{Q}(t)\right] & =\min (\gamma(s), \gamma(t))
\end{aligned}
$$

## Step 3

For both the risk-neutral distribution, $Q$, and distribution, $P$, of
a weiner process satusfies the following relations for some real number M

$$
\begin{aligned}
& Q\left(\max _{u \geqslant 0} \omega_{Q}(u) \leqslant M\right)=0 \\
& P\left(\max _{u \geqslant 0} \omega_{Q}(u) \leqslant M\right)=0
\end{aligned}
$$

These relations are saying that for any real number will eventually be exceeded.
Since $\tilde{V}(t)$ and $\omega_{Q}(\gamma(t))$ have the same distribution. It follows that for some interval $[0, T)$ and level $M$ that P-almost surely, for

$$
\begin{aligned}
& \tau=\min \{t: \tilde{v}(t)=\mu\} \\
& \tau \in[0, T)
\end{aligned}
$$

Modify the strategy to liquidate at $t=\tau$

$$
x^{\prime}(t)=\left\{\begin{array}{cc}
x(t) & t \leqslant \tau \\
0 & t>\tau
\end{array}\right.
$$

the risk-free portion of the strategy is determined using the relation,

$$
e^{r t} \tilde{v}(t)=x(t) s(t)+y(t)
$$

Then $T$ and $M$ will satisfy

$$
\tilde{v}_{x^{\prime} y^{\prime}}(T)=M
$$

In practice this strategy is impractical since money is borrowed with no collateral and $T$ could be a longtrme. A modification would be to place a lower bound on $\tilde{v}(t)$

## Theorem

If $(x, y)$ is self-financing and $V(t)$ is bounded from below
then $\tilde{V}(t)$ is a supermartingale with respect to the risk-neutral distribution, $Q$.

## Proof

Recall that

$$
\begin{aligned}
d \tilde{v}(t) & =x(t) d \tilde{s}(t) \\
& =x(t) \tilde{s}(t) \sigma d \omega_{Q}(t)
\end{aligned}
$$

Now $\tilde{v}(t)$ is a stochastic integral and previously it was stown the a stochastic integral is a beal martingale. So $\tilde{V}(t)$ is a local martingale. It has also been shown that any non-negative local martigale is a supermartingale.
Since $\tilde{v}(t)$ is bounded from below by, $\tilde{V}(t) \geqslant-L$, it follows trat

$$
\tilde{v}(t)+L \geqslant 0
$$

If $\tilde{v}(t)+L$ is considered then the desired result is obtained.

## Theorem

Doubling strategies contradict the assumption $\tilde{V}(t) \geqslant-L$.

## Proof

The doubling strategy assumes that for Zarbitrary $M$ there exits a $T$ such shat

$$
\tilde{V}(T)=M
$$

Recall that a supermartingale satisfies

$$
E[\tilde{V}(t)] \leqslant V(0)
$$

This contraticts the assumption that $M$ is arbitrary.

## Definition

A self-firancing strategy $(x, y)$ is called admissable if

1) $V(t) \geqslant-L$
2) $\tilde{v}(t)$ is a $Q$-martingale

## Theorem

If a derivative security with payoff $H$ can be redicated by a self-financing strategy ( $x_{1}, y_{1}$ ) and $b y$ an odmissible strategy $\left(x_{2}, y_{2}\right)$, then

$$
V_{x_{2} y_{2}}(0) \leqslant V_{x_{1} y_{1}}(0)
$$

This is stating that the intral investment for an admissible strategy is less than the ment for just a investment for just a both strategies are replicating the payout of the same

## derivative secunty.

## Proof

Recall that for a martigale the expectation is constant, so for the odmissable strategy

$$
H=E\left[V_{x_{2 Y_{2}}}(T)\right]=V_{x_{2 Y_{2}}}(0)
$$

The self-financing strategy is a supper mortingale so

$$
H=E\left[V_{x, y,}(T)\right] \leqslant V_{x, y,}(0)
$$

The desired result follows

$$
V_{x_{2, y_{2}}}(0) \leqslant V_{x_{1, y_{1}}}(0)
$$

## Option Pricing and Hedging

This section will discuss the calculation of the price of European call and put options using the Black-Sholes model.

Let $H(t)$ be the value process of a derivative security and assume that it has a replicating portfolio. This means there exists an admissible strategy $(x(t), y(t))$ such that

$$
V_{x y}(t)=H(t)
$$

Recall that a strategy is admissible if the forbowing conditions are met

1) $V(t)$ is self financing
2) $V(t) \geqslant-L$ (lower bound)
3) $\tilde{V}(t)$ is a martingale with respect to the risk-neutral distribution $Q$

It follows that the discounted value process, $\tilde{H}(t)$, is a Q martingle,

$$
\begin{aligned}
\tilde{H}(t) & =E_{Q}\left[\tilde{H}(T) \mid \tilde{J}_{t}\right] \\
& =E_{Q}\left[e^{-r T} H \mid \tilde{J}_{t}\right]
\end{aligned}
$$

Since $\tilde{v}(t)$ is self-financing

$$
\begin{aligned}
d \tilde{v}(t) & =x(t) d \tilde{s}(t) \\
& =x(t) \tilde{s}(t) \sigma d \omega_{Q}(t)
\end{aligned}
$$

This can be integrated

$$
\begin{aligned}
\tilde{V}(t) & =V(0)+\int_{0}^{t} x(t) \tilde{S}(t) \sigma d \omega_{Q}(t) \\
& =\tilde{H}(t) \\
& =E_{Q}\left[e^{-r T} H / \tilde{J}_{t}\right]
\end{aligned}
$$

The general problem can be stated as follows. Eiven a martingale $M(t)$, find a process $\bar{X}(t)$ such that $M(t)$ is the stochastic integral of $x(t)$.

Martingale Representation Theorem

Recall that for $f \in M^{2}$, that is,

$$
E\left[\int_{0}^{T} f^{2}(s) d s\right]<\infty
$$

the stochastic integral

$$
M(t)=\int_{0}^{t} f(s) d \omega(s)
$$

is a martingale. where $M(t)$ is square integrable, $M(t) \in L^{2}(\Omega)$,

$$
\int_{0}^{T} f^{2}(t) d t<\infty
$$

## Theorem

For any bounded deterministic function $g:[0, T] \rightarrow \mathbb{R}$ there exists $f_{g} \in M^{2}$ such that

$$
\exp \left\{S_{0}^{t} g(s) d \omega(s)-\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\}
$$

$$
=1+\int_{0}^{t} f_{g}(s) d w(s)
$$

## Proof

The process of interest can be written in the form,

$$
z(t)=e^{\bar{x}(t)}
$$

where

$$
\bar{X}(t)=\int_{0}^{t} g(s) d \omega(s)-\frac{1}{2} \int_{0}^{t} g^{2}(s) d s
$$

Recall that the Itô formula for a continuous function of an Itô process is given by

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

$$
\begin{aligned}
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +a(t) F_{x}(t, \bar{X}(t)) d t+b(t) F_{x}(t, \bar{X}(t) d \omega(t) \\
& +\frac{1}{2} b^{2}(t) F_{x x}(t, \bar{X}(t)) d t
\end{aligned}
$$

Here

$$
d \bar{x}(t)=g(t) d \omega(t)-2 g^{2}(t) d t
$$

so

$$
\begin{aligned}
a(t) & =-\frac{1}{2} g^{2}(t) \\
b(t) & =g(t) \\
F(t, \bar{X}(t)) & =e^{\bar{X}(t)}
\end{aligned}
$$

50

$$
\begin{aligned}
& F_{t}=0 \\
& F_{x}=e^{\bar{x}(t)} \\
& F_{x x}=e^{\bar{x}(t)}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
d z(t) & =0+\left(-\frac{1}{2} g^{2}(t)\right) z(t) d t \\
& +g(t) z(t) d \omega(t)+\frac{1}{2} g^{2}(t) z(t) d t \\
& =g(t) z(t) d \omega(t)
\end{aligned}
$$

$\Rightarrow \quad d z(t)=g(t) z(t) d \omega(t)$
integrating gives

$$
z(t)-z(0)=\int_{0}^{t} g(s) z(s) d \omega(s)
$$

letting $2(0)=1$ gives the destred result

$$
z(t)=1+\int_{0}^{t} g(s) z(s) d \omega(s)
$$

where

$$
f_{g}(s)=g(s) z(s)
$$

Next it must be shown that

$$
f_{g}(s) \in \mu^{2}
$$

Recall that this implies

$$
E\left[\int_{0}^{t} f_{g}^{2}(s) d s\right]<\infty
$$

Thus it must be shown that

$$
E\left[\int_{0}^{t}(g(s) Z(s))^{2} d s\right]<\infty
$$

Now it is assumed that $g(t)$ is bounded, so for some $C \in \mathbb{R}$

$$
|g(t)| \leqslant C
$$

for every $t \geqslant 0$ and
$z(t)=\exp \left\{\int_{0}^{t} g(s) d \omega(s)-\frac{1}{2} \int_{0}^{t} s^{2}(s) d s\right\}$
It follows that
$E\left[\int_{0}^{T}(g(t) z(t))^{2} d t\right] \leqslant c^{2} E\left[\int_{0}^{T} z^{2}(t d t]\right.$

Now

$$
z^{2}(t)=\exp \left\{2 \int_{0}^{t} g(s) d \omega(s)-\int_{0}^{t} g^{2}(s) d s\right\}
$$

$$
\begin{array}{r}
=\exp \left\{2 \int_{0}^{t} g(s) d w(s)\right\} \\
\exp \left\{-\int_{0}^{t} g^{2}(s) d s\right\}
\end{array}
$$

The second term is deterministic so
$E\left[\int_{0}^{T} z^{2}(t) d t\right]=E\left[\int_{0}^{T} \exp \left\{2 \int_{0}^{t} g(s) d w(s)\right\}\right.$

$$
\begin{aligned}
\exp \{ & \left.\left.-\int_{0}^{t} g^{2}(s) d s\right\} d t\right] \\
=\int_{0}^{T} E & {\left[\exp \left\{2 \int_{0}^{t} g(s) d w(s)\right\}\right] } \\
& \exp \left\{-\int_{0}^{t} g^{2}(s) d s\right\} d t
\end{aligned}
$$

Now

$$
\int_{0}^{t} g(s) d \omega(s)
$$

has a gaussian distribution with varrance

$$
\int_{0}^{t} g^{2}(s) d s
$$

So

$$
\begin{gathered}
E\left[\exp \left\{2 \int_{0}^{t} g(s) d w(s)\right\}\right] \\
=\exp \left[2 \int_{0}^{t} g^{2}(s) d s\right]
\end{gathered}
$$

Bringing things together gives

$$
\begin{gathered}
E\left[\int_{0}^{T} z^{2}(t) d t\right]=\int_{0}^{T} \exp \left[-\int_{0}^{t} g^{2}(s) d s\right] \\
\exp \left[2 \int_{0}^{t} g^{2}(s) d s\right] d t
\end{gathered}
$$

using $g^{2}(s) \leqslant c^{2}$ gives

$$
\begin{aligned}
& =\int_{0}^{T} \exp \left[\int_{0}^{t} S^{2}(s) d s\right] d t \\
& \quad \leqslant \int_{0}^{T} \exp \left[\int_{0}^{t} c^{2} d s\right] d t \\
& \quad=\int_{0}^{T} e^{c^{2} t} d t \\
& \quad=\frac{e^{c^{2} T}}{c^{2}}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
E\left[\int_{0}^{T} f_{g}(t) d t\right] & =E\left[\int_{0}^{T}(g(t) z(t))^{2} d t\right] \\
& \leqslant c^{2} E\left[\int_{0}^{T} z^{2}(t d t]\right. \\
& \leqslant e^{c^{2} T}<\infty
\end{aligned}
$$

Thus $f_{g} \in \mu^{2}$
and the desired result is obtained

$$
\begin{aligned}
z(t) & =\exp \left\{\int_{0}^{t} g(s) d \omega(s)-\frac{1}{2} \int_{0}^{t} s^{2}(s) d s\right\} \\
& =1+\int_{0}^{t} g(s) z(s) d \omega(s)
\end{aligned}
$$

## Theorem

Suppose that for any $\mathcal{F}_{T}$-measureable $\bar{x} \in L^{2}(\Omega)$ there exists $f_{X} \in M^{2}$ such that

$$
\bar{X}=E[\bar{X}]+\int_{0}^{T} f_{\bar{X}}(s) d \omega(s)
$$

Then any martingale $M(t) \in L^{2}(\omega)$ can be written in the form

$$
M(t)=M(0)+\int_{0}^{t} f_{M}(s) d \omega(s)
$$

for some $f_{M} \in M^{2}$

## Proof

Since it is assumed that $M(t) \in L^{2}(\Omega)$

$$
\int_{0}^{t} M(s) d s<\infty
$$

it follows that $M(t)-M(0) \in L^{2}(\Omega)$ and a martingale. So assume that $M(0)=0$.
Let $\bar{x}=M(T)$ and $f_{X}=f_{M}$ so that since it is assumed that

$$
\underline{\bar{x}}=E[\bar{x}]+\int_{0}^{T} f_{\bar{X}}(s) d \omega(s)
$$

It follows that

$$
M(T)=\int_{0}^{T} f_{M}(s) d \omega(s)
$$

Since $M(t)$ is a martingale taking conditional expectation
gives

$$
E\left[M(T) \mid \mathcal{F}_{t}^{\omega}\right]=M(t)
$$

where $\mathcal{F}_{t}^{w}$ is the filtration generated by $\omega(t)$

The desired result is dotained by taking conditional expectation of the integral

$$
\begin{gathered}
E\left[\int_{0}^{T} f_{\mu}(s) d \omega(s) \mid \mathcal{F}_{t}^{\omega}\right] \\
=\int_{0}^{t} f_{\mu}(s) d \omega(s)
\end{gathered}
$$

## Theorem

An $\mathcal{F}_{T}$ - Measureable $\bar{X} \in L^{2}(\Omega)$ can be written in the form

$$
\underline{X}=E[\bar{X}]+\int_{0}^{T} f_{\bar{X}}(s) d \omega(s)
$$

in a conique way. If $f_{1}, f_{2} \in M^{2}$ such that

$$
\begin{aligned}
& \bar{X}=E[X]+\int_{0}^{\top} f_{1}(s) d \omega(s) \\
& \bar{X}=E[\bar{X}]+\int_{0}^{\top} f_{2}(s) d \omega(s)
\end{aligned}
$$

then $f_{1}=f_{2}$.

The general idea here is to provide a general representation of a random variable by approximating it with a sequence of random variables of some seccial form for which there is a representation result.

From the first theorem there is a stochastic integral representalion of a random variable.

$$
\bar{x}=\exp \left\{\int_{0}^{\top} g(s) d \omega(s)-\frac{1}{2} S_{0}^{\top} g^{2}(s) d s\right\}
$$

This idea needs to be extended to arbitrary X.

## Theorem

Random variables of the form

$$
X=\exp \left\{\sum_{k=1}^{n} c_{k}\left[\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right]\right\}
$$

where $t_{k} \in[0, T], t_{k}<t_{k+1}, C_{k} \in \mathbb{R}$ have a representation of the form of a complex-valued random process, $f_{x} \in \mu_{c}^{2}$

## Proof

## consider

$$
z(t)=\exp \left\{i \int_{0}^{t} g(s) d w(s)+\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\}
$$

It will be shown that

$$
z(t)=1+i \int_{0}^{t} g(s) z(s) d s
$$

This is the extension of the previous result to complex numbers. start by writing $z(t)$ in real and imaginary components.

$$
z(t)=\exp \left\{i \int_{0}^{t} g(s) d w(s)+\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\}
$$

$$
\begin{aligned}
& =\exp \left\{\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\} \exp \left\{i \int_{0}^{t} g(s) d \omega(s)\right\} \\
& =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos \left[\int_{0}^{t} g(s) d \omega(s)\right] \\
& +i \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin \left[\int_{0}^{t} g(s) d \omega(s)\right] \\
& =z_{R}(t)+i z_{I}(t)
\end{aligned}
$$

Now consider the real and imaginary components of 2 seperately.
Recall that the Itô formula for an Itó process is given by

$$
\begin{gathered}
z(t)=F(t, \bar{X}(t)) \\
d \bar{X}(t)=a(t) d t+b(t) d \omega(t)
\end{gathered}
$$

$$
\begin{aligned}
d z(t) & =F_{t} d t+a(t) F_{x} d t \\
& +b(t) F_{x} d \omega(t)+\frac{1}{2} b^{2}(t) F_{x x} d t
\end{aligned}
$$

Here

$$
\bar{x}(t)=\int_{0}^{t} g(s) d \omega(s)
$$

It follows that

$$
d \bar{x}(t)=g(s) d \omega(s)
$$

so that

$$
a(t)=0 \quad b(t)=g(s)
$$

It follows that

$$
\begin{aligned}
d z(t)= & F_{t} d t+g(t) F_{x} d \omega(t) \\
& +\frac{1}{2} g^{2}(t) F_{x x} d t
\end{aligned}
$$

Now the real and imaginary components of 2 will be
treated seperately.

$$
\begin{aligned}
Z(t) & =F(t, \omega(t)) \\
& =Z_{R}(t)+i Z_{I}(t) \\
& =F^{R}(t, \omega(t))+i F^{I}(t, \omega(t))
\end{aligned}
$$

## where

$$
\begin{aligned}
z(t) & =\exp \left\{\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\} \exp \left\{i \int_{0}^{t} g(s) d \omega(s)\right\} \\
& =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos \left[\int_{0}^{t} g(s) d \omega(s)\right] \\
& +i \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin \left[\int_{0}^{t} g(s) d \omega(s)\right] \\
& \text { so } \\
& F^{R}(t, \omega(t))=z_{R}(t, \omega(t)) \\
& =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos \left[\int_{0}^{t} g(s) d \omega(s)\right]
\end{aligned}
$$

$$
\begin{aligned}
& F^{I}(t, \omega(t))=z_{I}(t, \omega(t)) \\
& =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin \left[\int_{0}^{t} g(s) d \omega(s)\right]
\end{aligned}
$$

but,

$$
\begin{aligned}
x & =\int_{0}^{t} g(s) d \omega(s) \\
F^{R}(t, x) & =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x \\
F^{I}(t, x) & =\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x
\end{aligned}
$$

For the real part

$$
\begin{aligned}
& F_{t}^{R}=\frac{1}{2} g^{2}(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x \\
& F_{x}^{R}=-\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x \\
& F_{x x}^{R}=-\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x
\end{aligned}
$$

SO

$$
\begin{aligned}
& d z_{R}(t)=F_{t}^{R} d t+g(t) F_{x}^{2} d \omega(t) \\
& +\frac{1}{2} g^{2}(t) F_{x x}^{R} d t \\
& =\frac{1}{2} g^{2}(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x d t \\
& -g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x d \omega(t) \\
& -\frac{1}{2} g^{2}(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x d t \\
& =-g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x d \omega(t) \\
& =c^{2} g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \\
& \sin \left[\int_{0}^{t} g(s) d \omega(s)\right] d \omega(t)
\end{aligned}
$$

similarly for the imaginary part.

$$
d Z_{I}(t)=F_{t}^{I} d t+g(t) F_{x}^{I} d \omega(t)
$$

$$
\begin{aligned}
& \quad+\frac{1}{2} g^{2}(t) F_{x x}^{I} d t \\
& \text { since } \\
& F^{I}(t, x)=\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x \\
& F_{t}^{I}(t, x)=\frac{1}{2} g^{2}(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x \\
& F_{x}^{I}=\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x \\
& F_{x x}^{I}=-\exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x
\end{aligned}
$$

thus

$$
\begin{aligned}
& d Z_{I}(t)= F_{t}^{I} d t+g(t) F_{x}^{I} d \omega(t) \\
&+\frac{1}{2} g^{2}(t) F_{x x}^{I} d t \\
&=\frac{1}{2} g^{2}(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x d t \\
&+g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x d \omega(t) \\
&-\frac{1}{2} g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \sin x d t
\end{aligned}
$$

$$
\begin{gathered}
=g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \cos x d \omega(t) \\
=g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \\
\cos \left[\int_{0}^{t} g(s) d \omega(t)\right]
\end{gathered}
$$

Binging things together gives

$$
\begin{aligned}
d z(t)= & d z_{R}(t)+i d z_{I}(t) \\
= & i^{2} g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \\
& \sin \left[\int_{0}^{t} g(s) d \omega(s)\right] d \omega(t) \\
+ & i g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \\
& \cos \left[\int_{0}^{t} g(s) d \omega(t)\right] \\
= & i g(t) \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right]
\end{aligned}
$$

$$
\begin{aligned}
\left\{\cos \left[\int_{0}^{t} g(s) d \omega(t)\right]\right. & \\
+i \sin & {\left.\left[\int_{0}^{t} g(s) d \omega(s)\right]\right\} d \omega(t) } \\
=i g(t) & \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right] \\
& \exp \left[i \int_{0}^{t} g(s) d \omega(s)\right] d \omega(t) \\
=i g(t) & \exp \left[\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right. \\
& \left.+i \int_{0}^{t} g(s) d \omega(s)\right] d \omega_{s}
\end{aligned}
$$

but

$$
z(t)=\exp \left\{i \int_{0}^{t} g(s) d w(s)+\frac{1}{2} \int_{0}^{t} g^{2}(s) d s\right\}
$$

thut

$$
d z(t)=i g(t) z(t) d \omega(t)
$$

$\Rightarrow \quad z(t)-z(0)=i \int_{0}^{t} g(t) z(t) d \omega(t)$
The desired result is obtainged by assuming $z(0)=1$.

$$
z(t)=1+i \int_{0}^{t} g(t) z(t) d \omega(t)
$$

## Theorem

For any $\mathcal{J}_{T}$-measurectble real-valued $\bar{X} \in L^{2}(D)$ there exists a unique $f_{\bar{x}} \in M^{2}$ such that

$$
\bar{\Delta}=E[\bar{x}]+\int_{0}^{\top} f_{\bar{X}}(s) d \omega(s)
$$

## Theorem

If $M$ is a martingale with respect to the fittration generated by the Weiner process such that $M(t) \in L^{2}(\Omega)$ for all $t$, then there is a unique process $f_{\mu} \in \mu^{2}$ such that

$$
M(t)=M(0)+\int_{0}^{t} f_{M}(s) d \omega(s)
$$

## Completeness of the Model

Recall thal a path-indepent dervative security of European type has a payoff of the form

$$
H=h(S(T))
$$

It is assumed that

1) $H \geqslant 0$
2) $h\left(H^{\alpha}\right)<\Delta$ for some $d>2$

The derivative pricing model is based on probability space $(\Omega, F, P)$ and time set $t \in[0, T]$. The model contcins a single underlying asset, $s(t)$, and a risk-free investment, $A(t)$. The asset, $S(t)$, has natural fitration, $\mathcal{F}_{t}^{s}$, where $\mathcal{F}=\mathcal{F}_{T}^{S}$.
A drivative pricing model is complete if each European
derivative $H$ can be replicated by a self-financing strategy.
To avoid doubling and suicide To avoid doubling and suicide and other nonadmissible startegies. Recall that an investment strategy is admissible if the following conditions are satisfed by the value process $V(t)$

1) $V(t) \geqslant-L$
2) $\tilde{v}(t)$ is a martingale with respect to the risk-neutral probability $Q$.

It follows that a complete maket assumes that replicating strategies are admissible.

Here it will be shown that the Black-schies model is complete

The martigale representotion theorem discussed in the previous section will be with respect to the risk-nautral distribution $\omega_{Q}$.

## Theorem

If $E_{p}\left(H^{\alpha}\right)<\infty$ for some $\alpha>2$ then $E_{Q}\left(H^{2}\right)<\&$ where $Q$ is the Black-Shdles martingale measure.

## This theorem proves the sque integrability of $H$

with respect to the riskneutral destribution so that

$$
H \in M_{Q}^{2}
$$

## Theorem

The Black-Scholes model is complete in the following
sense: for each $\mathcal{F}_{T}$-measureable $H \geqslant 0$ with $E\left(H^{\alpha}\right)<\infty$ for some $\alpha$ there is an admissible replicating strategy 1 $(x, y)$ such that

$$
V_{x y}(t)=E_{Q}\left[e^{-r(T-t)} H \mid J_{t}\right]
$$

## Proof

The goal is to find a replicating strategy that satisfies,

$$
V_{x y}(t)=E_{Q}\left[e^{-r(T-t)} H \mid \mathcal{F}_{t}\right]
$$

setting $t=T$ and using the assumption that $H$ is $\mathcal{F}_{T}$-measureable gives

$$
V_{x y}(T)=E_{Q}\left[H \mid \mathcal{F}_{T}\right]=H
$$

which the expression must satisfy to be a replicating
stratesy.
Recall that

$$
A(t)=e^{r t}
$$

so

$$
\begin{aligned}
V_{x y}(t) & =E_{Q}\left[e^{-r(T-t)} H \mid \mathcal{F}_{t}\right] \\
& =A(t) E_{Q}\left[e^{-r T} H \mid \mathcal{F}_{t}\right] \\
& =A(t) M(t)
\end{aligned}
$$

where

$$
M(t)=E_{Q}\left[e^{-r T} H \mid \mathcal{F}_{t}\right]
$$

Now

$$
E_{Q}\left[\mu^{2}(t)\right]=E_{Q}\left[\left(E_{Q}\left[e^{-r T} H \mid \mathcal{F}_{t}\right]\right)^{2}\right]
$$

Recall Jenser's inequality

$$
\varphi(E[x]) \leqslant E[\varphi(\bar{x})]
$$

where $\Phi$ is a convex function. here $q(x)=x^{2}$ which is convex. Thus

$$
\begin{aligned}
E_{Q}\left[M^{2}(t)\right] & =E_{Q}\left[\left(E_{Q}\left[e^{-r T} H \mid \mathcal{F}_{t}\right]\right)^{2}\right] \\
& \leqslant E_{Q}\left[E_{Q}\left[e^{-2 r T} H^{2} \mid \mathcal{F}_{t}\right]\right] \\
& =e^{-2 r T} E_{Q}\left[E_{Q}\left[H^{2} \mid \mathcal{F}_{t}\right]\right] \\
& =e^{-2 r T} E_{Q}\left[H^{2}\right] \\
& <\infty
\end{aligned}
$$

which follows from the previous theorem.
It follows that $M(t) \in M_{Q}^{2}$. This Now the goal is to find an admissable strategy $(x, y)$ with value

$$
V_{x y}(t)=A(t) \mu(t)
$$

Since $M(t) \in M_{Q}^{2}$ it follows that $M(t)$ is a martingale with
respect $Q$, additionally there exists a detrministic function $f(t) \in \mu^{2}$ such that

$$
M(t)=M(0)+\int_{0}^{t} f(s) d \omega_{Q}(s)
$$

in differential form

$$
d M(t)=f(t) d \omega_{Q}(t)
$$

Recall that $V_{x y}(t)$ is assumed to be addmissabe so $t$ is self firancing
$d v_{x y}(t)=x(t) d S(t)+y(t) d A(t)$
using

$$
\begin{aligned}
& d S(t)=r S(t) d t+\sigma S(t) d \omega_{Q}(t) \\
& d A(t)=r A(t) d t
\end{aligned}
$$

gives

$$
\begin{aligned}
d v_{x y}(t)= & x(t)\left(r s(t) d t+\sigma s(t) d w_{Q}(t)\right) \\
& +y(t) r A(t) d t \\
= & r(x(t) s(t)+y(t) A(t) d t \\
& +x(t) \sigma s(t) d w_{Q}(t)
\end{aligned}
$$

Now consider

$$
\begin{aligned}
d V_{x y}(t) & =d(A(t) M(t)) \\
& =A(t) d M(t)+M(t) d A(t)
\end{aligned}
$$

using

$$
d M(t)=f(t) d \omega_{Q}(t)
$$

gives

$$
\begin{aligned}
d v_{x y}(t)= & A(t) f(t) d \omega_{Q}(t) \\
& +M(t) r A(t) d t
\end{aligned}
$$

equating this to the previous expression

$$
\begin{aligned}
r(x(t) S(t)+y(t) A(t) d t & \\
+ & x(t) \sigma S(t) d \omega_{Q}(t) \\
= & A(t) f(t) d \omega_{Q}(t)+M(t) r A(t) d t \\
\Rightarrow r & (x(t) S(t)+y(t) A(t)) d t-M(t) r A(t) d t \\
= & A(t) f(t) d \omega_{Q}(t)-x(t) \sigma S(t) d \omega_{Q}(t) \\
\Rightarrow 0= & r[x(t) S(t)+y(t) A(t)-M(t) A(t)] d t \\
& +[x(t) \sigma S(t)-A(t) f(t)] d \omega_{Q}(t)
\end{aligned}
$$

Two equations are obtained by equating the components to zero

$$
\begin{gathered}
r[x(t) S(t)+y(t) A(t)-M(t) A(t)]=0 \\
x(t) \sigma S(t)-A(t) f(t)=0
\end{gathered}
$$

From the second equation

$$
x(t)=\frac{A(t) f(t)}{\sigma S(t)}
$$

inserting into the first equation gives

$$
\begin{aligned}
& x(t) S(t)+y(t) A(t)-M(t) A(t)=0 \\
\Rightarrow & \frac{A(t) f(t)}{\sigma S(t)} S(t)+y(t) A(t)-M(t) A(t)=0 \\
\Rightarrow & A(t) f(t)+\sigma y(t) A(t)-\sigma M(t) A(t)=0 \\
\Rightarrow & \sigma y(t) A(t)=\sigma M(t) A(t)-A(t) f(t) \\
\Rightarrow & y(t)=M(t)-\frac{f(t)}{\sigma}
\end{aligned}
$$

Thus

$$
x(t)=\frac{A(t) f(t)}{\sigma S(t)}
$$

$$
y(t)=\mu(t) \cdot \frac{f(t)}{\sigma}
$$

This solution can be verified by insertion into the equation for the value process.

$$
\begin{aligned}
V_{x y}(t) & =x(t) S(t)+y(t) A(t) \\
& =\frac{A(t) f(t)}{\sigma S(t)} S(t)+\left[M(t)-\frac{f(t)}{\sigma}\right] A(t) \\
& =A(t) \frac{f(t)}{\sigma}+M(t) A(t)-\frac{f(t) A(t)}{\sigma} \\
& =M(t) A(t) \\
& =M(t) e^{r t} \\
\Rightarrow \quad \tilde{V}_{x y}(t) & =M(t)
\end{aligned}
$$

Furthwer it is assumed that

$$
\mu(t)=E_{Q}\left[e^{-r T} H \mid \tilde{J}_{t}\right]
$$

Trus

$$
\begin{aligned}
V_{x y}(t) & =e^{r t} E_{Q}\left[e^{-r T} H \mid \mathcal{F}_{t}\right] \\
& =E_{Q}\left[e^{-r(T-t)} H \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

which was asswined initially
Thus the admissable stategy which satisfies

$$
V_{x y}(t)=E_{Q}\left[e^{-r(T-t)} H \mid \mathcal{F}_{t}\right]
$$

is given by

$$
x(t)=\frac{A(t) f(t)}{\sigma S(t)}
$$

$$
y(t)=\mu(t) \cdot \frac{f(t)}{\sigma}
$$

where

$$
\begin{gathered}
M(t)=\tilde{V}_{x y}(t) \\
M(t)=M(0)+\int_{0}^{t} f(s) d w_{Q}(s)
\end{gathered}
$$

Recall the previously it was shown that a self-firancing strategy satisfies

$$
d \tilde{v}(t)=x(t) d \tilde{s}(t)
$$

It will be show that the result gust obtained satisfies this relation.

Now

$$
u(t)=\tilde{V}_{x y}(t)
$$

$$
\Rightarrow d \tilde{V}_{x y}(t)=d M(t)
$$

but

$$
d M(t)=f(t) d \omega_{Q}(t)
$$

and

$$
\begin{array}{r}
x(t)=\frac{A(t) f(t)}{\sigma S(t)} \\
\Rightarrow f(t)=\frac{\sigma S(t)}{A(t)} x(t) \\
=\sigma \tilde{S}(t) x(t)
\end{array}
$$

since $A(t)=e^{r t}$. Thus the desired result is obtained

$$
d \tilde{v}_{x y}(t)=x(t) \sigma \tilde{s}(t) d \omega_{Q}(t)
$$

## Derivatue Pricing

In the Black-Scholes model the exists at least one probobility $Q$, called the risk-neutral probability, where the discownted asset price, $\tilde{s}(t)$, is a martingale.

## Theorem

The martingale probability $Q$ in the Black-Scholes model is unique.

## Proof

Let $B \in \mathcal{F}_{T}^{S}=\mathcal{F}$ and let $H=\underline{1}_{B}$. This bounded random variable is assumed to be the payoff of a derivative security, Assume there are two risk-nentral probabilities, $Q_{1}$ and $Q_{2}$, From the defintion of $H$,

$$
e^{-r t} Q_{1}(B)=e^{-r t} E_{Q_{1}}\left[\mathbb{1}_{B}\right]
$$

$$
\begin{aligned}
& =e^{-r t} E_{Q_{1}}[H] \\
& =e^{-r t} E_{Q_{1}}[\tilde{v}(\tau)]
\end{aligned}
$$

For a complete maket $\tilde{V}(T)$ is a martingale, so

$$
E_{Q,}[\tilde{V}(T)]=V(0)
$$

Similarly,

$$
e^{-r t} Q_{2}(B)=E_{Q_{2}}[\tilde{V}(T)]=V(0)
$$

thus

$$
\begin{aligned}
& Q_{1}(B)=Q_{2}(B) \\
\Rightarrow & Q_{1}=Q_{2}
\end{aligned}
$$

## General Derivative Securites

Consider a general path-independent European derivative security

$$
H=h(S(T))
$$

where the asset price satisfies

$$
\begin{gathered}
S(T)=S(t) \exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\right. \\
\left.\sigma\left[\omega_{Q}(T)-\omega_{Q}(t)\right]\right\}
\end{gathered}
$$

To determine the derivative security price the following problem must be solved

$$
\begin{array}{r}
H(t)=e^{-r(T-t)} E_{Q}\left[h(s(T)) \mid \mathcal{F}_{t}\right] \\
=E_{Q}\left[e ^ { - r ( T - t ) } h \left(s ( t ) \operatorname { e x p } \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right.\right. \\
\left.\left.\left.+\sigma\left[\omega_{Q}(T)-\omega_{Q}(t)\right]\right]\right) \mid \tilde{J}_{t}\right]
\end{array}
$$

## Definition: Borel Eunction

A map $f: x \rightarrow I$ betwen two topological spaces is called Borel (or Borel measureable) if $f^{-1}(A)$ is a Borel set for and $A \in \mathcal{F}$.

## Theorem

Let $\mathcal{H}$ be a sub-6-field of $\mathcal{F}$ and assume that $Y$ is independent of $\psi$ and that $z$ is $\psi$-measuredble Given a bounded Borel function $\psi(1,2)$ define the function then,

$$
E[\psi(I, z) \mid \otimes]=\psi(z)
$$

This relation can be used to evaluate $H(t)$. Make the associations

$$
\begin{aligned}
& A=\mathcal{F}_{t} \\
& I=\omega_{Q}(T)-\omega_{Q}(t) \\
& Z=S(t)
\end{aligned}
$$

$$
\begin{aligned}
\psi(y, z) & =e^{-r(T-t)} h\left(z \operatorname { e x p } \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right. \\
+\sigma & {\left.\left.\left[\omega_{Q}(T)-\omega_{Q}(t)\right]\right]\right) }
\end{aligned}
$$

Here $z$ is $z_{t}$-mensureable and $I$ is independent of $z$ and thus $\mathcal{F}_{t}$.

Now to determine $H(t)$ the following expression must be evaluated

$$
\psi(t, z)=E_{Q}\left[\psi(t, z, \bar{Y}) \mid \mathcal{F}_{t}\right]
$$

Note that since $\omega_{Q}(t)$ is a weiner process

$$
I=\omega_{Q}(T)-\omega_{Q}(t) \sim \text { Normal }(0, T-t)
$$

It follows that

$$
I=\omega_{Q}(T)-\omega_{Q}(t) \sim \sqrt{T-t} \bar{I}_{1}
$$

where $I$, has a unit normal

## distribution.

$$
\bar{I}_{1} \sim \operatorname{Normal}(0,1)
$$

## Thus

$$
\begin{aligned}
& \psi(y, z)=e^{-r(T-t)} h\left(2 \operatorname { e x p } \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right. \\
&\left.\left.+\sigma \sqrt{T-t} I_{1}\right]\right)
\end{aligned}
$$

since $I_{\text {i }}$ is a unit normal it has probability density

$$
f(y)=\frac{e^{-y^{2} / 2}}{\sqrt{\partial \pi}}
$$

It follows that the expectation is given by

$$
\begin{aligned}
& E_{Q}\left[\Psi(t, z, \bar{I}) \backslash \mathcal{F}_{t}\right] \\
& =\int_{\mathbb{R}} f(y) \Psi(t, y, z) d y
\end{aligned}
$$

$=e^{-r(T t)} \int_{R} e^{-Y^{2} / 2} h\left(z \exp \left[\left(r-\frac{1}{\partial \pi} \sigma^{2}\right)(T-t)\right.\right.$

$$
+\sigma y \sqrt{T-t}]) d y
$$

To go foothur the payoff function $h(t, y, z)$ must be known. Following sections will evaluate this integral for different option types.

## Put Options

In this section the price of a Europear call option is computed using the Black-Scholes model. In the previous section it was shown that for the Black-Sholes model a European derivative security with payout $h(2)$ the price is given by

$$
H=h(S(T))
$$

where $s(t)$ follows the Black-Scholes model

$$
\begin{aligned}
S(T)= & S(t) \exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\right. \\
& \left.\sigma\left[\omega_{Q}(T)-\omega_{Q}(t)\right]\right\}
\end{aligned}
$$

to determine the derivative security price the following problem must be solved

$$
\begin{gathered}
H(t)=e^{-r(T-t)} E_{Q}\left[h(s(T)) \mid \mathcal{F}_{t}\right] \\
=E_{Q}\left[e ^ { - r ( T - t ) } h \left(s ( t ) \operatorname { e x p } \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right.\right. \\
\left.\left.\left.+\sigma\left[\omega_{Q}(T)-\omega_{Q}(t)\right]\right]\right) \mid \mathcal{F}_{t}\right]
\end{gathered}
$$

In the previous section it was shown that for

$$
\begin{aligned}
Z & =s(t) \\
I & =\omega_{Q}(T)-\omega_{Q}(t) \\
H(t) & =\psi(t, z)
\end{aligned}
$$

$$
\begin{gathered}
\psi(t, z)= \\
e^{-r(T t)} \int_{R} \frac{e^{-y^{2} / 2}}{\sqrt{2 \pi}} h\left(z \operatorname { e x p } \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right. \\
+\sigma y \sqrt{T-t}]) d y
\end{gathered}
$$

For the European Put option

$$
\begin{aligned}
h & =\max \{k-2,0\} \\
& =(k-2)^{+}
\end{aligned}
$$

It follows that $0 \leqslant n \leqslant K$ which is bounded.

It follows that

$$
h(z)=\left(K-z \exp \left[\left(r-\partial \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t}\right]\right)^{t}
$$

and

$$
\begin{aligned}
& \psi(t, z)=e^{-r(T t)} \int_{R} \frac{e^{-y^{2} / 2}}{\partial \pi} \\
& \left(K-z \exp \left[\left(r-\frac{\partial}{\partial} \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t}\right]\right)^{+} d y
\end{aligned}
$$

Here this integral will be evaluated. first the range of integration
is determined. The integrated function is non-zero only for

$$
\begin{aligned}
& K-z \exp \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t}\right] \geqslant 0 \\
& \Rightarrow K \geqslant z \exp \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t}\right]
\end{aligned}
$$

This equation can be solved for $y$ to defermine the integration limits.

$$
\begin{aligned}
& K \geqslant 2 \exp \left[\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t}\right] \\
\Rightarrow & \ln \frac{k}{2} \geqslant\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma y \sqrt{T-t} \\
\Rightarrow & \ln \frac{k}{2}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t) \geqslant \sigma y \sqrt{T-t} \\
\Rightarrow & \frac{1}{\sigma \sqrt{T-t}}\left[\ln \frac{k}{2} \cdot\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right] \geqslant y
\end{aligned}
$$

let

$$
d(t, z)=\frac{1}{\delta \sqrt{T \cdot t}}\left[\ln \frac{k}{2} \cdot\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right]
$$

then

$$
y \leqslant d(t, 2)
$$

it follows that the integration limits are given by

$$
-\infty<y \leqslant d(t, z)
$$

over this range the integrand is positive so,

$$
\begin{aligned}
& \psi(t, 2)=e^{-r(T-t)} \int_{-\infty}^{d(t, 2)} \frac{e^{-y^{2} / 2}}{\partial \pi} \\
&\left(k-2 \exp \left[\left(r-\frac{\partial}{\partial \sigma^{2}}\right)(T-t)+\sigma y \sqrt{T-t}\right]\right) d y \\
&=\frac{e^{-r(T-t)}}{\sqrt{2 \pi}}\left\{\int_{-\infty}^{d(t, 2)} k e^{-y^{2} / 2} d y\right.
\end{aligned}
$$

$$
\begin{aligned}
- & z \int_{-\infty}^{d(t, z)} e^{-y^{2} / 2} e^{\left(r-a \sigma^{2}\right)(T-t)} \\
& \left.e^{\sigma y \sqrt{T-t}} d y\right\} \\
= & \frac{k e^{-r(T-t)}}{\frac{1}{\partial \pi}} \int_{-\infty}^{d(t, z)} e^{-r^{2} / 2} d y \\
- & \frac{2 e^{\left(r-\partial \sigma^{2}\right)(T-t)}}{\frac{1}{\partial \pi}} e^{-r(T-t)} \\
& \int_{-\infty}^{d(t, z)} e^{-\left(y^{2} / 2-\sigma y \sqrt{T-t}\right)} d y
\end{aligned}
$$

Now for the first term, recall that the cumulative distribution function for the normal distribution is given by

$$
N(d)=\frac{1}{12 \pi} \int_{\Delta}^{d} e^{-x^{2} / 2} d x
$$

It follows that

$$
\begin{aligned}
& \frac{K e^{-r(T-t)}}{\sqrt{2 \pi}} \int_{-\infty}^{d(t, z)} e^{-1^{2} / 2} d y \\
& =K e^{-r(T-t)} N(d(t, z))
\end{aligned}
$$

For the second term consider the integral

$$
\frac{1}{12 \pi} \int_{-\infty}^{d(t, 2)} e^{-\left(y^{2} / 2-\sigma y \sqrt{T-t}\right)} d y
$$

completing the square of the exponential argument gives

$$
\begin{aligned}
\frac{1}{2} y^{2}-\sigma y \sqrt{T-t} & =\frac{1}{2}\left[y^{2}-2 \sigma_{y} \sqrt{T-t}\right. \\
+\sigma^{2}(T-t) & \left.-\sigma^{2}(T-t)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{2}(y-\sigma \sqrt{T-t})^{2}-\frac{1}{2} \sigma^{2}(T-t) \\
& \text { so, } \\
& \frac{1}{12 \pi} \int_{-\infty}^{d(t, z)} e^{-\left(y^{2} / 2-\sigma y \sqrt{T-t}\right)} d y \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{d(t, z)} e^{-\left(y-\frac{1}{2} \sigma \sqrt{T-t}\right)^{2}}+\frac{1}{2} \sigma^{2}(T-t) d y \\
& =e^{\frac{1}{2} \sigma^{2}(T-t)} \int_{-\infty}^{d(t, z)} e^{-(y-\sigma \sqrt{T-t})^{2} / 2} d y \\
& \text { let } \sqrt{2 \pi} \\
& \text { then } u=y-\sigma \sqrt{T-t}=>d u=d y \\
& \frac{1}{2 \pi} \int_{-\infty}^{d(t, z)} e^{-(y-\sigma \sqrt{T-t})^{2} / 2} d y \\
& =\frac{1}{2 \pi} \int_{-\infty}^{d(t, z)-\sigma \sqrt{T-t}} u^{2} / 2 d u
\end{aligned}
$$

$$
=N(d(t, z)-\sigma \sqrt{T-t})
$$

Bringing things together

$$
\begin{aligned}
& \psi(t, z)=K e^{-r(T-t)} N(d(t, z)) \\
&-z e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)} e^{-r(T-t)} e^{\frac{1}{2} \sigma^{2}(T-t)} \\
& N(d(t, z)-\sigma \sqrt{T-t}) \\
&= K e^{-r(T-t)} N(d(t, z)) \\
&-z N(d(t, z)-\sigma \sqrt{T-t})
\end{aligned}
$$

The price of the put option is given by

$$
\begin{aligned}
P(t) & =\psi(t, s(t)) \\
& =K e^{-r(T-t)} N(d(t, s(t))) \\
& -s(t) N(d(t, s(t))-\sigma \sqrt{T-t})
\end{aligned}
$$

Thus the price of a Euoropean put option is

$$
\begin{gathered}
P(t)=K e^{-r(T-t)} N(d(t, s(t))) \\
-s(t) N(d(t, s(t))-\sigma \sqrt{T-t})
\end{gathered}
$$

where

$$
\begin{aligned}
d(t, s(t))= & \frac{1}{\sigma T T-t}\left[\ln \frac{k}{s(t)}\right. \\
& \left.-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right]
\end{aligned}
$$

## Call Option

Recall that the payoff for a European call option with strike price $K$ and wnderlying asset $s(t)$ is given by

$$
\begin{aligned}
C(T) & =\max \{0, S(T)-K\} \\
& =(S(T)-K)^{+}
\end{aligned}
$$

Recall that for $C(T)$ to have a replicating portfolio it must be that for $\alpha>2$,

$$
C(T) \in L^{d}(P)
$$

where $L^{\alpha}(P)$ is the set of all functions with bounded P- Expectation of the a power or function, explaitly.
$L^{\alpha}(P)=\left\{f:[0, T] \times \Omega \rightarrow \mathbb{R}: E_{p}\left[f^{\alpha}(T)\right]<\infty\right\}$

If the asset price is given by

$$
S(T)=S(O) e^{\mu T-\frac{1}{2} \sigma^{2} T+\sigma \omega(T)}
$$

Then

$$
E_{p}\left[C^{\alpha}(T)\right]=E_{p}\left[(S(T)-K)^{\alpha}\right]
$$

Now since $k$ is constant it follows that for some $c_{1}$ and Ce

$$
E_{p}\left[(S(T)-K)^{2}\right] \leqslant C_{1} E_{p}\left[S^{\alpha}(T)\right]+C_{2}
$$

It follows that

$$
\begin{aligned}
E_{p}\left[s^{\alpha}(T)\right] & =E_{p}\left[\left\{s(0) e^{\left.\mu T-\frac{1}{2} \sigma^{2} T+\sigma \omega(T)\right\}^{\alpha}}\right]\right. \\
& =E_{p}\left[s^{2}(0) e^{\alpha\left(\mu T-\frac{1}{2} \sigma^{2} T+\sigma \omega(T)\right)}\right] \\
& =s^{2}(0) e^{\alpha\left(\mu T-\frac{1}{2} \sigma^{2} T\right)} E_{p}\left[e^{\alpha \sigma \omega(T)}\right]
\end{aligned}
$$

Previouly for a weiner process it was shown that

$$
E_{p}\left[e^{\alpha \sigma \omega(T)}\right]=e^{\alpha^{2} \sigma^{2} T}
$$

so

$$
\begin{aligned}
E_{p}\left[s^{\alpha}(T)\right] & =s^{2}(0) e^{\alpha\left(\mu T-\frac{1}{2} \sigma^{2} T\right)} e^{\alpha^{2} \sigma^{2} T} \\
& <\alpha
\end{aligned}
$$

thus C(T) can be replicated.

## Theorem Put-call Parity

If the price of European call and put options are denoted by $C(t)$ and $P(t)$ respecturely, then

$$
c(t)-P(t)=s(t) \cdot K e^{-r(T-t)}
$$

Proof

Now

$$
\begin{aligned}
& C(T)=(S(T)-K)^{+} \\
& P(T)=(K-S(T))^{+}
\end{aligned}
$$

so,

$$
\begin{aligned}
S(T) & -C(T)+P(T)=S(T)-(S(T)-K)^{t} \\
& +(K-S(T))^{t}
\end{aligned}
$$

if $S(T)-K \geqslant 0$ then

$$
\begin{aligned}
S(T)-C(T)+P(T) & =S(T) \cdot S(T)+K \\
& =K
\end{aligned}
$$

similarly $K-S(T) \geqslant 0$

$$
\begin{aligned}
S(T)-C(T)+P(T) & =S(T)+K-S(T) \\
& =K
\end{aligned}
$$

it follows that

$$
S(T)-C(T)+P(T)=K
$$

multiplying by $e^{-r T}$ gives

$$
\tilde{S}(T)-\tilde{C}(T)+\tilde{D}(T)=K e^{-r T}
$$

Now $\tilde{S}(T), \tilde{C}(T)$ and $\tilde{P}(T)$ are Q martingales so they are $F_{t}$-measureable, so for conditional expectation of $T \geqslant, t$

$$
\begin{aligned}
& E_{Q}\left[\tilde{S}(T)-\tilde{C}(T)+\tilde{P}(T) \mid \mathcal{F}_{t}\right] \\
= & E_{Q}\left[K e^{-r T} \mid \mathcal{F}_{t}\right] \\
\Rightarrow & \tilde{S}(t)-\tilde{C}(t)+\tilde{P}(t)=K e^{-r T} \\
\Rightarrow & S(t)-c(t)+P(t)=K e^{-r(T-t)} \\
\Rightarrow & S(t)-K e^{-r(T-t)}=c(t)-P(t)
\end{aligned}
$$

which is the desired result. This relation can be used to compute the price of a European call option from the previous result for a put
option, namely,

$$
\begin{array}{r}
P(t)=K e^{-r(T-t)} N(d(t, s(t))) \\
-s(t) N(d(t, s(t))-\sigma \sqrt{T-t})
\end{array}
$$

where

$$
d(t, s(t))=\frac{1}{\sigma T T-t}\left[\ln \frac{K}{s(t)}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right]
$$

Now

$$
\begin{aligned}
& s(t)-K e^{-r(T-t)}=C(t)-P(t) \\
= & \\
= & \\
= & \\
& (t)-K(t)+P e^{-r(T-t)} \\
& +K e^{-r(T-t)} N(d(t, s(t))) \\
& - \\
& s(t) N(d(t, s(t))-\sigma \sqrt{T-t})
\end{aligned}
$$

$$
\begin{aligned}
= & k e^{-r(T-t)}[N(d(t, s(t))-1] \\
& -s(t)[N(d(t, s(t)-o \sqrt{T-t})-1] \\
= & s(t)[1-N(d(t, s(t)-o \sqrt{T-t})] \\
& -K e^{-r(T-t)}[1-N(d(t, s(t))]
\end{aligned}
$$

Now

$$
\begin{aligned}
& N(d)=\frac{1}{2 \pi} \int_{-\infty}^{d} e^{-x^{2} / 2} d x \\
& \text { so } \\
& 1-N(d)=1-\frac{1}{2 \pi} \int_{-\infty}^{d} e^{-x^{2} / 2} d x \\
& =\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{-x^{2} / 2} d x-\frac{1}{2 \pi} \int_{-\infty}^{d} e^{-x^{2} / 2} d x \\
& =\frac{1}{\sqrt{2 \pi}} \int_{d}^{\infty} e^{-x^{2} / 2} d x
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-d} e^{-x^{2} / 2} d x \\
& =N(-d)
\end{aligned}
$$

Thus

$$
\begin{aligned}
c(t)= & s(t)[1-N(d(t, s(t))-\sigma \sqrt{T-t})] \\
- & K e^{-r(T-t)}[1-N(d(t, s(t))] \\
= & s(t) N(\sigma \sqrt{T-t}-d(t, s(t))) \\
& -K e^{-r(T-t)} N(-d(t, s(t)))
\end{aligned}
$$

Thus

$$
\begin{aligned}
c(t)= & s(t) N(\sigma \sqrt{T-t}-d(t, s(t))) \\
& -K e^{-r(T-t)} N(-d(t, s(t)))
\end{aligned}
$$

$$
d(t, s(t))=\frac{1}{\sigma / T-t}\left[\ln \frac{K}{s(t)}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right]
$$

## Theorem Black-Schdes Formula

The prices for Euoropean call and put options are given by

$$
\begin{aligned}
& C(t)=S(t) N\left(d_{+}(t, S(t))\right. \\
& -K e^{-r(T-t)} N\left(d_{-}(t, S(t))\right. \\
& P(t)=-S(t) N\left(-d_{+}(t, S(t))\right) \\
& +K e^{-r(T-t)} N\left(-d_{-}(t, S(t))\right)
\end{aligned}
$$

where

$$
\begin{aligned}
& d_{+}(t, z)=\frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, z)=\frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

## Proof

Previously it was shown that,

$$
\begin{gathered}
P(t)=K e^{-r(T-t) N(d(t, S(t)))} \\
-S(t) N(d(t, S(t))-\sigma \sqrt{T-t}) \\
C(t)=S(t) N(\sigma \sqrt{T-t}-d(t, S(t))) \\
-K e^{-r(T-t)} N(-d(t, S(t))) \\
d(t, z)=\frac{1}{\sigma \mid T-t}\left[\ln \frac{K}{2}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right] \\
\text { Now, } \\
-d(t, z)=\frac{-\ln \frac{K}{2}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
=\frac{\ln \frac{2}{K}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
=d(t, z)
\end{gathered}
$$

next consider

$$
d(t, z)-\sigma \sqrt{T-t}=\frac{\ln \frac{k}{2}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
$$

$$
\begin{aligned}
& =\frac{\sigma \sqrt{T-t}}{\ln \frac{k}{2}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)-\sigma^{2}(T-t)} \\
& =\frac{-\ln \frac{2}{k}-r(T-t)+2 \sigma^{2}(T-t)-\sigma^{2}(T-t)}{\sigma \sqrt{T-t}} \\
& =\frac{-\ln \frac{2}{k}-r(T-t)-2 \sigma^{2}(T-t)}{\sigma \sqrt{T-t}} \\
& =\frac{-\left[\ln \frac{2}{k}+\left(r+\frac{1}{2} \sigma^{2}\right)(T-t)\right]}{\sigma \sqrt{T-t}} \\
& =d_{+}(t, 2)
\end{aligned}
$$

Thus

$$
\begin{array}{r}
d(t, z)=d(t, z) \\
d(t, z)-\sigma \sqrt{T-t}=-d_{+}(t, z)
\end{array}
$$

Now consider

$$
\begin{aligned}
P(t)= & K e^{-r(T-t)} N(d(t s(t))) \\
- & S(t) N(d(t, s(t))-\sigma \sqrt{T-t}) \\
= & K e^{-r(T-t)} N\left(-d_{-}(t, s(t))\right) \\
& -s(t) N\left(-d_{+}(t, s(t))\right)
\end{aligned}
$$

and

$$
\begin{aligned}
c(t)= & s(t) N(\sigma \sqrt{T-t}-d(t, s(t))) \\
& -K e^{-r(T-t)} N(-d(t, s(t))) \\
= & s(t) N\left(d_{+}(t, s(t))\right) \\
& -K e^{-r(T-t)} N(d(t, s(t)))
\end{aligned}
$$

Thus the desired result is obtained

$$
\begin{aligned}
& C(t)=S(t) N\left(d_{+}(t, S(t))\right) \\
& -K e^{-r(T-t)} N\left(d_{-}(t, S(t))\right) \\
& \hline P(t)=-S(t) N\left(-d_{+}(t, S(t))\right) \\
& +K e^{-r(T-t)} N\left(-d_{-}(t, S(t))\right)
\end{aligned}
$$

## Theorem: Black-Sholes Premium

The call and put options at time $t=0$ are given by,

$$
\begin{aligned}
& C(r, T, K, S(0), \sigma) \\
& \quad=S(0) N\left(d_{+}(S(0))\right)-K e^{-r T} N\left(d_{-}(S(0))\right)
\end{aligned}
$$

$$
\begin{aligned}
& P(r, T, K, S(0), \sigma) \\
& \quad=-S(0) N\left(-d_{+}(S(0))\right)+K e^{-r T} N(-d(S(0)))
\end{aligned}
$$

where

$$
\begin{aligned}
& d_{+}(z)=\frac{\ln \frac{z}{K}+\left(r+\frac{1}{2} \sigma^{2}\right) T}{\sigma \sqrt{T}} \\
& d_{-}(z)=\frac{\ln \frac{z}{K}+\left(r-\frac{1}{2} \sigma^{2}\right) T}{\sigma \sqrt{T}}
\end{aligned}
$$

From the previous theorem

$$
\begin{aligned}
C(t)=S(t) & N\left(d_{+}(t, S(t))\right) \\
& -K e^{-r(T-t)} N\left(d_{-}(t, S(t))\right)
\end{aligned}
$$

$$
\begin{aligned}
& P(t)=-S(t) N\left(-d_{+}(t, S(t))\right) \\
& +k e^{-r(T-t)} N\left(-d_{-}(t, S(t))\right) \\
& d_{+}(t, z)=\frac{\ln \frac{2}{k}+\left(r+\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, z)=\frac{\ln \frac{2}{k}+\left(r-\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

setting $t=0$ gives the desired result.

$$
\begin{array}{r}
d_{+}(z)=\frac{\ln \frac{z}{K}+\left(r+\frac{1}{2} \sigma^{2}\right) T}{\sigma \sqrt{T}} \\
d_{-}(z)=\frac{\ln \frac{z}{K}+\left(r-\frac{1}{2} \sigma^{2}\right) T}{\sigma \sqrt{T}} \\
c(r, T, K, s(0), \sigma) \\
=s(0) N\left(d_{+}(s(0))\right)-K e^{-r T} N(d(s(0)))
\end{array}
$$

$$
\begin{aligned}
& P(r, T, K, S(0), \gamma) \\
& =-S(0) N\left(-d_{+}(S(0))\right)+K e^{-r T} N\left(-d_{-}(S(0))\right)
\end{aligned}
$$

## Theorem

For any $k>0$ and $t \leqslant T$ the stock price process $s(t)$ satisfies

$$
\begin{aligned}
& \left.E_{Q}\left[\underline{1}_{[S(T)} \leqslant k\right] \mid \mathcal{J}_{t}\right]=N\left(d_{-}(t, S(t))\right) \\
& E_{Q}\left[S(T) \underline{1}_{[S(T) \leqslant k]} \mid \mathcal{J}_{t}\right] \\
& =e^{r(T-t)} S(t) N\left(-d_{+}(t, S(t))\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& E_{Q}\left[\mathbb{1}_{[s(T) \geqslant k]} \mid \mathcal{F}_{t}\right]=N(d(t, s(t))) \\
& E_{Q}\left[s(T) \mathbb{1}_{[s(T) \geqslant k]} \mid \mathcal{F}_{t}\right] \\
& \quad=e^{r(T-t)} s(t) N\left(d_{+}(t, s(t))\right)
\end{aligned}
$$

## Proof

Recall that

$$
\begin{aligned}
& S(T)=S(t) \exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\right. \\
& \left.\sigma \omega_{Q}(T)-\omega_{Q}(t)\right\}
\end{aligned}
$$

and that $\omega_{Q}(t)$ is a weiner process so that

1) $\omega_{Q}(0)=0$
2) $\omega_{Q}(T)-\omega_{Q}(t) \sim \operatorname{Normal}(0, T-t)$
3) For $s<t<u$
$E_{Q}\left[\left(\omega_{Q}(t)-\omega_{Q}(s)\right)\left(\omega_{Q}(u)-\omega(t)\right)\right]=0$
since $\omega_{Q}(t)$ is a waner process it follows that
$\omega_{Q}(T)-\omega_{Q}(t) \sim \operatorname{Normal}(0, T-t)$
then since

$$
\omega_{Q}(T)-\omega_{Q}(t) \sim \sqrt{T \cdot t} I
$$

where In Normal $(0,1)$ it follows that,

$$
S(T)=S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma \sqrt{T-t} y}
$$

so that

$$
\begin{aligned}
\Rightarrow \quad & S(T) \leqslant K \\
\Rightarrow \quad & S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+y \sigma \sqrt{T-t}} \leqslant K \\
\Rightarrow \quad & y \leqslant \frac{\ln \frac{K}{S(t)}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
= & -\left\{\frac{\ln \frac{S(t)}{K}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}\right\}
\end{aligned}
$$

Now recall

$$
d_{-}(t, z)=\frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
$$

thus

$$
\begin{aligned}
& S(T) \leqslant K \\
\Rightarrow \quad & y \leqslant-d(t, S(t))
\end{aligned}
$$

Now since $\omega_{Q}(T)-\omega_{Q}(t)$ is mdependent of $\mathcal{F}_{t}$ and $S(t)$ is $\mathcal{F}_{t}$-measureable it follows that

$$
\begin{aligned}
& E_{Q}\left[\underline{11}[s(T) \leqslant k] \mid \mathcal{J}_{t}\right] \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} \frac{1}{[s(\tau) \leqslant k]} e^{-y^{2} / 2} d y \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-d-(t, s(t)} e^{-y^{2} / 2} d y
\end{aligned}
$$

$$
=N\left(-d_{-}(t, s(t))\right)
$$

Next consider

$$
E_{Q}\left[S(T) \mathbb{1}_{[S(T) \leq K]} \mid \mathcal{F}_{t}\right]
$$

where

$$
\begin{aligned}
S(T) & =S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma \sqrt{T-t} y} \\
& =S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)} e^{\sigma \sqrt{T-t} y}
\end{aligned}
$$

It follows that

$$
\begin{gathered}
E_{Q}\left[S(T) \mathbb{1}_{\left.[S(T) \leqslant K] \mid \mathcal{F}_{t}\right]}\right. \\
=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\Delta} S(T) \mathbb{1}_{[S(T) \leqslant K]} e^{-y^{2} / 2} d y \\
=\frac{1}{2 \pi} \int_{-\infty}^{-d(t, S(t))} S(t) e^{\left(r-2 \sigma^{2}\right)(T-t)} e^{\sigma \sqrt{T-t} y} e^{-y^{2} / 2} d y
\end{gathered}
$$

$$
=\frac{1}{\sqrt{2 \pi}} S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)} \int_{-\infty}^{-\frac{d}{2}(t, s(t))} e^{\sigma \sqrt{T-t}} y-T^{2} b d y
$$

Consider the argument of the integrated exponential,

$$
\begin{aligned}
& \sigma \sqrt{T-t} y-\frac{1}{2} y^{2}=-\frac{1}{2}\left(y^{2}-2 y \sigma \sqrt{T-t}\right) \\
= & -\frac{1}{2}\left[y^{2}-2 y \sigma \sqrt{T-t}+\sigma^{2}(T-t)-\sigma^{2}(T-t)\right] \\
= & -\frac{1}{2}\left[y^{2}-2 y \sigma \sqrt{T-t}+\sigma^{2}(T-t)\right]+\frac{1}{2} \sigma^{2}(T-t) \\
= & -\frac{1}{2}(y-\sigma \sqrt{T-t})^{2}+\frac{1}{2} \sigma^{2}(T-t)
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
& E_{Q}\left[S(T) \mathbb{1}_{\left.[S(T) S K] \mid \mathcal{F}_{t}\right]}\right. \\
& =\frac{1}{\sqrt{2 \pi}} S(t) e^{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)} \int_{-\infty}^{-d(t, S(t)}
\end{aligned}
$$

$$
\begin{gathered}
e^{\frac{-1}{2} \sigma^{2}(T-t)} e^{-1 / 2(y-\sigma \sqrt{T-t})^{2}} d y \\
=s(t) e^{r(T-t)} \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-d(t, s(t)} e^{-\frac{1}{\partial}(y-6 \sqrt{T-t})^{2}} d y
\end{gathered}
$$

and

$$
\begin{aligned}
& & \infty<y \leqslant-d_{-}(t, s(t)) \\
\Rightarrow & & -\infty<u+\sigma \sqrt{T-t} \leqslant-d_{-}(t, s(t)) \\
\Rightarrow & & -\infty<u<-d_{-}(t, s(t))-\sigma \sqrt{\tau-t}
\end{aligned}
$$

Now

$$
\begin{aligned}
& -d_{-}(t, z)-\sigma \sqrt{T-t}=-\frac{\left[\ln \frac{2}{K}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right]}{\sigma \sqrt{T-t}} \\
& -\frac{\sigma \sqrt{T-t}}{\sigma \sqrt{T-t}} \\
& =\frac{-\ln \frac{2}{K}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)-\sigma^{2}(T-t)}{\sigma}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-\ln \frac{2}{k}-\left(r+\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& =-d_{+}(t, z)
\end{aligned}
$$

Putting things together gives

$$
\begin{aligned}
& E_{Q}\left[S(T) \mathbb{1}_{\left.[S(T) \leq K] \mid \mathcal{F}_{t}\right]}\right. \\
& =S(t) e^{r(T-t)} \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-d_{+}(t, S(t)} e^{-u^{2} / 2} d u \\
& =S(t) e^{r(T-t)} N\left(-d_{+}(t, S(t))\right.
\end{aligned}
$$

The final two expressions can be evaluated by using the identity

$$
\mathbb{1}_{[S(T) \geqslant K]}=1-\mathbb{1}_{[S(T) \leqslant K]}
$$

Then

$$
E_{Q}\left[\mathbb{1}_{[S(T) \geqslant k]} \mid \mathcal{F}_{t}\right]
$$

$$
\begin{aligned}
& =E_{Q}\left[1-\mathbb{I}[s(T) \leq K] \mid \mathcal{J}_{t}\right] \\
& =1-E_{Q}\left[1 \underline{1}_{[s(T) \leq K]} \mid \mathcal{J}_{t}\right]
\end{aligned}
$$

and

$$
\begin{aligned}
E_{Q} & {\left[S(T) \mathbb{1}_{[S(T) \geqslant K]} \mid \mathcal{F}_{t}\right] } \\
& =E_{Q}\left[S(T)(1-\mathbb{1}[S(T) \leq K]) \mid \mathcal{F}_{t}\right] \\
& =E_{Q}\left[S(T) \mid \mathcal{F}_{t}\right]-E\left[S(T) \mathbb{1}_{[S(T) \leq K]} \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

Now for the first term $\tilde{S}(T)$ is a marlingale with respect to $Q$, so

$$
\begin{aligned}
E_{Q} & {\left[S(T) \mid \mathcal{F}_{t}\right]=e^{r T} E_{Q}\left[\tilde{S}(T) \mid \mathcal{F}_{t}\right] } \\
& =e^{r T} \tilde{S}(t) \\
& =e^{r(T-t)} s(t)
\end{aligned}
$$

and

$$
\begin{gathered}
E_{Q}\left[S(T) \mathbb{1}_{[S(T) \geqslant k]} \mid \mathcal{F}_{t}\right]=e^{r(T-t)} s(t) \\
-E\left[S(T) \mathbb{1}_{[S(T) \leqslant k]} \mid \mathcal{F}_{t}\right]
\end{gathered}
$$

So using the previous results gives

$$
\begin{aligned}
E_{Q}\left[\mathbb{1}_{[s(T)}\right. & \left.\geqslant k] \mid \mathcal{F}_{t}\right] \\
& =1-E_{Q}\left[\mathbb{1}_{[s(T) \leq k]} \mid \mathcal{F}_{t}\right] \\
& =1-N(-d(t, s(t))) \\
& =N(d(t, s(t))
\end{aligned}
$$

and

$$
\begin{aligned}
& E_{Q}\left[S(T) \mathbb{1}_{[S(T) \geqslant K]} \mid \mathcal{F}_{t}\right] \\
& =e^{r(T-t)} s(t)-E\left[S(T) \mathbb{1}_{[S(T) \leqslant K]} \mid \mathcal{F}_{t}\right] \\
& =s(t) e^{r(T-t)} \\
& \quad-s(t) e^{r(T-t)} N\left(-d_{+}(t, s(t))\right.
\end{aligned}
$$

$$
\begin{aligned}
& =s(t) e^{r(T-t)}\left[1-N\left(-d_{t}(t, s(t))\right)\right] \\
& =s(t) e^{r(T-t)} N\left(d_{1}(t, s(t))\right)
\end{aligned}
$$

This proves all of the relations,

$$
\begin{aligned}
& E_{Q}\left[\mathbb{1}_{\left.[s(T) \leqslant k] \mid \mathcal{F}_{t}\right]=N\left(d_{-}(t, s(t))\right)}\right. \\
& E_{Q}\left[s(T) \mathbb{1}_{\left.[s(T) \leqslant k] \mid \mathcal{F}_{t}\right]}\right. \\
& =e^{r(T-t)} s(t) N\left(-d_{+}(t, s(t))\right) \\
& \frac{E_{Q}\left[\mathbb{1}_{[s(T) \geqslant k]} \mid \mathcal{F}_{t}\right]=N(d(t, s(t)))}{E_{Q}\left[s(T) \mathbb{1}_{[s(T) \geqslant k]} \mid \mathcal{F}_{t}\right]} \\
& =e^{r(T-t)} s(t) N\left(d_{+}(t, s(t))\right)
\end{aligned}
$$

## The Black-Scholes PDE

In deriving the PDE a European call option is assumed, recall that the price of a European call option is given by,

$$
c(t)=u(t, s(t))
$$

where

$$
\begin{array}{rl}
u(t, z)=2 & N\left(d_{+}(t, z)\right) \\
& -k e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
d_{+}(t, z)= & \frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
d_{-}(t, z)= & \frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{array}
$$

## Theorem

The finction $u(t, z)$ satisfies the partial differential equation and the boundary condition,

$$
\begin{gathered}
u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}=r u \\
u(T, z)=(z-k)^{+}
\end{gathered}
$$

## Proof

It will be shown that

$$
\begin{aligned}
& u(t, z)=2 N\left(d_{+}(t, z)\right) \\
&-k e^{-r(T-t)} N\left(d_{-}(t, z)\right)
\end{aligned}
$$

is a solution to the PDE and satisfies the boundry condition.

Step 1
First it will be shown
that

$$
k e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right)
$$

where

$$
n(d)=N^{\prime}(d)=\frac{1}{\sqrt{2 \pi}} e^{-d^{2} / 2}
$$

and

$$
\begin{aligned}
& d_{+}(t, z)=\frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, z)=\frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

From the assumed relation it follows that

$$
\begin{aligned}
& k e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right) \\
\Rightarrow & k e^{-r(T-t)} e^{-d_{-12}^{2}}=2 e^{-d_{1 / 2}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \frac{2}{k}= e^{d_{+2}^{2}} e^{-d_{-2}^{2}} e^{-r(T-t)} \\
&= e^{d_{+2}^{2} / 2-d_{-2}^{2}-r(T-t)} \\
& \Rightarrow \ln \frac{2}{k}= \frac{d_{+}^{2}(t, 2)}{2}-\frac{d_{-2}^{2}(t, 2)}{2} \\
&-r(T-t) \\
&= \frac{1}{2}\left[d_{+}^{2}(t, 2)-d_{-}^{2}(t, 2)\right]^{2} \\
&-r(T-t) \\
&=\frac{1}{2}\left[d_{+}(t, 2)+d_{-}(t, 2)\right]\left[d_{+}(t, 2)-d_{-}(t, 2)\right] \\
&-r(T-t)
\end{aligned}
$$

now consider,

$$
\begin{aligned}
& d_{-}(t, z)+d_{+}(t, z)=\frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& \quad+\frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\sigma \sqrt{T-t}}\left[\ln \frac{2}{K}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\ln \frac{2}{K}\right. \\
& \left.+\left(r+\frac{1}{2} \sigma^{2}\right)(T-t)\right] \\
& =\frac{1}{\sigma \sqrt{T-t}}\left[2 \ln \frac{2}{K}+(T-t)\left(r-\frac{1}{2} \sigma^{2}+r+\frac{1}{2} \sigma^{2}\right)\right] \\
& =\frac{1}{\sigma \sqrt{T-t}}\left[2 \ln \frac{2}{K}+2 r(T-t)\right] \\
& =\frac{2}{\sigma \sqrt{T-t}}\left[\ln \frac{2}{K}+r(T-t)\right]
\end{aligned}
$$

and

$$
\begin{aligned}
& d_{+}(t, 2)-d_{-}(t, 2)=\frac{\ln \frac{2}{k}+\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& -\frac{\ln \frac{2}{k}+\left(r-\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& =\frac{1}{\sigma \sqrt{T-t}}\left[\frac{\ln \frac{2}{k}+\left(r+\frac{1}{\partial \sigma^{2}}\right)(T-t)}{-\ln \frac{2}{k}-\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}\right]
\end{aligned}
$$

$=\frac{(T-t)}{\sigma \sqrt{T-t}}\left(r^{2}+\frac{1}{2} \sigma^{2}-r^{2}+\frac{1}{2} \sigma^{2}\right)$
$=\frac{\sigma^{2}(T-t)}{\sigma \sqrt{T-t}}=\sigma \sqrt{T-t}$
Bringing things together,

$$
\begin{aligned}
\frac{1}{2} & {\left[d_{+}(t, 2)+d_{-}(t, 2)\right]\left[d_{+}(t, 2)-d_{-}(t, 2)\right] } \\
& -r(T-t) \\
= & \frac{1}{2}\left\{\frac{2}{\sigma T-t}\left[\ln \frac{2}{k}+r(T-t)\right]\right\} o \sqrt{T-t} \\
& -r(T-t) \\
= & \ln \frac{2}{k}+r(T-t)-r(T-t) \\
= & \ln \frac{2}{k}
\end{aligned}
$$

which must be the case for the expression to be true, thus
$K e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right)$
Next the time derivatue is computed

$$
u_{t}(t, 2)=\frac{\partial}{\partial t} u(t, 2)
$$

where

$$
\begin{aligned}
& u(t, z)=2 N\left(d_{+}(t, z)\right) \\
&-k e^{-r(T-t)} N\left(d_{-}(t, z)\right)
\end{aligned}
$$

and

$$
\frac{d N(d)}{d d}=n(d)
$$

Now

$$
\begin{aligned}
& \frac{\partial}{\partial t} u(t, z)=2 n\left(d_{+}(t, z)\right) \frac{\partial d_{+}(t, z)}{\partial t} \\
&-r k e^{-r(T-t)} N\left(d_{-}(t, z)\right)
\end{aligned}
$$

$$
-k e^{-r(T-t)} n\left(d_{-}(t, z)\right) d d_{-}(t, z)
$$

Recall that in the first step it was shown that,

$$
k e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right)
$$

using this relation on the last term gives

$$
\begin{aligned}
& \frac{\partial}{\partial t} u(t, z)=2 n\left(d_{+}(t, z)\right) \frac{\partial d_{+}}{\partial t}(t, z) \\
& -r k e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
& -2 n\left(d_{+}(t, z)\right) \frac{\partial d_{-}}{\partial t}(t, z) \\
& =2 n\left(d_{+}(t, z)\right)\left[\frac{\partial d_{+}(t, z)}{\partial t}-\frac{\partial d_{-}(t, z)}{\partial t}\right] \\
& -r k e^{-r(T-t)} N\left(d_{-}(t, z)\right)
\end{aligned}
$$

## consider

$$
\frac{\partial d_{1}(t, 2)}{\partial t}-\frac{\partial d_{(t, 2)}}{\partial t}=\frac{\partial}{\partial t}\left[d_{1}(t, 2)-d(t, 2)\right]
$$

In the previous step it was shown that

$$
d_{+}(t, 2)-d(t, 2)=\sigma \sqrt{T-t}
$$

56

$$
\begin{aligned}
\frac{\partial}{\partial t} & {\left[d_{1}(t, 2)-d(t, 2)\right]=\frac{\partial}{\partial t} \sigma \sqrt{T-t} } \\
& =\frac{-\sigma}{\partial \sqrt{T-t}}
\end{aligned}
$$

it Pollows that

$$
\begin{aligned}
& \frac{\partial}{\partial t} u(t, z)=2 n\left(d_{+}(t, z)\right)\left(\frac{-\sigma}{\partial T-t}\right) \\
&-r K e^{-r(T-t)} N\left(d_{-}(t, z)\right)
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow \frac{\partial}{\partial t} u(t, z) & =-r K e^{-r(T-t)} N(d(t, z)) \\
& -Z n\left(d_{+}(t, z)\right) \frac{\sigma}{2 \sqrt{T-t}}
\end{aligned}
$$

Next $u_{2}(t, 2)$ is evaluated, where

$$
\begin{aligned}
& u(t, z)=z N\left(d_{+}(t, z)\right) \\
& \text { so }-K e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
& \frac{\partial}{\partial z} u(t, z)=\frac{\partial}{\partial z}\left[z N\left(d_{+}(t, z)\right)\right. \\
& \left.-K e^{-r(T-t)} N\left(d_{-}(t, z)\right)\right] \\
& =N\left(d_{+}(t, z)\right)+Z n\left(d_{+}(t, z)\right) \frac{\partial d_{+}(t, z)}{\partial z} \\
& -K e^{-r(T-t)} n\left(d_{-}(t, z)\right) \frac{\partial d_{-}(t, z)}{\partial z}
\end{aligned}
$$

again using

$$
\begin{aligned}
& K e^{-r(T-t)} n\left(d_{-}(t, z)\right)=z n\left(d_{+}(t, z)\right) \\
& \text { gives } \\
& \frac{\partial}{\partial z} u(t, z)=N\left(d_{+}(t, z)\right) \\
& +2 n\left(d_{+}(t, z)\right) \frac{\partial d_{+}(t, z)}{\partial z} \\
& -2 n\left(d_{+}(t, z)\right) \frac{\partial d_{-}}{\partial z}(t, z) \\
& =N\left(d_{+}(t, z)\right) \\
& +2 n\left(d_{+}(t, z)\right)\left[\frac{\partial d_{+}(t, z)}{\partial z}-\frac{\partial d_{-}(t, z)}{\partial z}\right]
\end{aligned}
$$

Dut

$$
\begin{gathered}
\frac{\partial d_{1}(t, z)}{\partial z}-\frac{\partial d(t, z)}{\partial z}=\frac{\partial}{\partial z}\left[d_{+}(t, z)\right. \\
-d(t, z)]
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{\partial}{\partial z}(\sigma \sqrt{T-t}) \\
& =0
\end{aligned}
$$

so it follows that

$$
\frac{\partial}{\partial z} u(t, z)=N\left(d_{+}(t, z)\right)
$$

For the final step $u_{22}(t, 2)$ is evaluated

$$
\begin{aligned}
u_{22}(t, 2) & =\frac{\partial^{2}}{\partial 2^{2}} u(t, 2) \\
& =\frac{\partial}{\partial 2} \frac{\partial u(t, 2)}{\partial 2}
\end{aligned}
$$

From the previous result it follows that

$$
\frac{\partial}{\partial z} \frac{\partial u(t, z)}{\partial z}=\frac{\partial}{\partial z} N\left(d_{+}(t, z)\right)
$$

$$
=n\left(d_{+}(t, z)\right) \frac{\partial d_{+}}{\partial z}(t, z)
$$

Now

$$
\begin{aligned}
d_{+}(t, z) & =\frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& =\frac{\ln \frac{z}{k}}{\sigma \sqrt{T-t}}+\frac{\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
\text { so } & \frac{\partial d_{-1}(t, z)}{\partial z}=\frac{1}{z \sigma \sqrt{T-t}}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
u_{22}(t, 2) & =n\left(d_{+}(t, 2)\right) \frac{\partial d_{+}}{\partial z}(t, 2) \\
\Rightarrow u_{2 z}(t, 2) & =\frac{n\left(d_{+}(t, 2)\right)}{2 \sigma \sqrt{T-t}}
\end{aligned}
$$

Everything has been evaluated. Bringing them together gives

$$
\begin{aligned}
u(t, z)= & z N\left(d_{+}(t, z)\right) \\
& -K e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
u_{t}(t, z)= & -r K e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
- & Z n\left(d_{+}(t, z)\right) \frac{\sigma}{2 \sqrt{T-t}} \\
u_{2}(t, z)= & N\left(d_{+}(t, z)\right) \\
u_{z z}(t, z)= & \frac{n\left(d_{+}(t, z)\right)}{z \sigma \sqrt{T-t}} \\
d_{+}(t, z)= & \frac{\ln \frac{z}{k}+\left(r+\frac{1}{\partial \sigma^{2}}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

$$
d_{-}(t, z)=\frac{\ln \frac{z}{k}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
$$

The Black-Sholes PDE is given by

$$
\begin{gathered}
u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}=r u \\
u(T, z)=(z-K)^{+}
\end{gathered}
$$

Plugging things into the POE
grues

$$
\begin{array}{rl}
-r & K e^{-r(T-t)} N\left(d_{-}(t, z)\right) \\
& -Z n\left(d_{+}(t, z)\right) \frac{\sigma}{2 \sqrt{T-t}} \\
& +r z\left\{N\left(d_{+}(t, z)\right)\right\} \\
& +\frac{1}{2} \sigma^{2} z^{2} \frac{n\left(d_{+}(t, z)\right)}{z \sigma \sqrt{T-t}}
\end{array}
$$

$$
\begin{aligned}
= & r\left[2 N\left(d_{+}(t, z)\right)-K e^{-r(T-t)} N\left(d_{-}(t, z)\right]\right. \\
& -2 n\left(d_{+}\left(t_{2}, z\right)\right) \frac{\sigma}{2 \sqrt{T-t}}+\frac{2 n\left(d_{+}(t, z)\right) \sigma}{2 \sqrt{T-t}} \\
=r & {\left[2 N\left(d_{+}(t, z)\right)-K e^{-r(T-t)} N\left(d_{-}(t, z)\right]\right.} \\
= & r u(t, z)
\end{aligned}
$$

which veriftes that $u(t, 2)$ is a solution to the PDE

For the boundary condition

$$
u(T, z)=z N\left(d_{t}(T, z)\right) \cdot K N\left(d_{-}(t, z)\right)
$$

Now for both,

$$
d_{+}(T, Z)=d_{-}(T, Z)=\infty
$$

and

$$
\begin{aligned}
N(\infty) & =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-x^{2} / 2} d x \\
& =1
\end{aligned}
$$

thus the boundary condition is satisfied

$$
\begin{aligned}
u(T, z) & =2 N(\infty) \cdot K N(\infty) \\
& =2-K
\end{aligned}
$$

## Solving PDE for option Price

In this section methods for solums the Black-scholes POE

## Theorem

Let $u(t, 2)$ be a function with first and second derivative,
i.e. of class $c^{1,2}$ from $\mathbb{R}^{2} \rightarrow \mathbb{R}$ at let $S(t)$ satisfy

$$
d s(t)=r s(t) d t+\sigma s(t) d \omega_{Q}(t)
$$

If $u(t, 2)$ has bounded derivative $u_{2}$ and

$$
r u=u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}
$$

Then

$$
e^{-r t} u(t, s(t))
$$

is a $Q$-martingale.

## Proof

Consider the differential of $e^{-r t} u(t, s(t))$,

$$
\begin{gathered}
d\left\{e^{-r t} u(t, s(t))\right\}=e^{-r t} d u(t, s(t)) \\
-r e^{-r t} u(t, s(t)) d t
\end{gathered}
$$

Now recall that the Its formula for a function $u(t, z)$ of an Itô process

$$
\begin{aligned}
& d \bar{x}(t)=a(t) d t+b(t) d w(t) \\
& d u(t, 2)=u_{t} d t+a(t) u_{2} d t \\
& \quad+b(t) u_{2} d w(t)+\frac{1}{2} b^{2}(t) u_{22} d t
\end{aligned}
$$

Here

$$
\begin{aligned}
& d \omega(t)=d \omega_{Q}(t) \quad z=S(t) \\
& a(t)=r S(t) b(t)=\sigma S(t)
\end{aligned}
$$

$$
\begin{aligned}
& s \partial \\
& \begin{array}{l}
d u(t, s(t))=u_{t} d t+r s(t) u_{2} d t \\
\quad \sigma s(t) u_{2} d w_{Q}(t) \\
+\frac{1}{\partial} \sigma^{2} s^{2}(t) u_{22} d t
\end{array}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& d\left[e^{-r t} u\left(t_{1} s(t)\right)\right]= \\
& e^{-r t} d u-r e^{-r t} u d t \\
& =-r e^{-r t} u d t+e^{-r t}\left\{u_{t} d t\right. \\
& +r s(t) u_{2} d t+\sigma s(t) u_{2} d \omega_{Q}(t) \\
& \left.+\frac{1}{2} \sigma^{2} s^{2}(t) u_{22} d t\right\} \\
& =-r e^{-r t} u_{d t}+e^{-r t}\left[u_{t}\right. \\
& \left.+r s(t) u_{2}+\frac{1}{2} \sigma^{2} s^{2}(t) u_{22}\right] d t
\end{aligned}
$$

$$
+e^{-r t} \sigma s(t) u_{2} d \omega_{Q}(t)
$$

It is assumed that

$$
r u=u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}
$$

with $2=S(t)$

$$
r u=u_{t}+r s(t) u_{2}+\frac{1}{2} \sigma^{2} s^{2}(t) u_{22}
$$

It follows that

$$
\begin{aligned}
d[ & \left.e^{-r t} u(t, s(t))\right]=-r e^{-r t} u d t \\
& +e^{r t} r u d t \\
& +e^{-r t} \sigma s(t) u_{2} d \omega_{Q}(t) \\
\Rightarrow & d\left[e^{-r t} u\left(t_{1} s(t)\right)\right] \\
& =e^{-r t} \sigma s(t) u_{2} d \omega_{Q}(t)
\end{aligned}
$$

Now it is assumed that $u_{2}$ is bownded, previously it has been shown that $S(t) \in M^{2}$ so

$$
E\left[\int_{0}^{T} s^{2}(t) d t\right]<\infty
$$

since $e^{-r T}$ is bounded over any interval $[0, T]$ it follows that

$$
e^{-r t} \sigma s(t) u_{z} \in \mu^{2}
$$

it follows that $e^{-r t} s(t)$ is a martigale with respect to $Q$.

## Theorem

If $H(T)=h(S(T)) \geqslant 0$ is in $L^{2}(Q)$ and if $u(t, 2)$ is a solution to

$$
\begin{gathered}
u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}=r u \\
u(T, z)=h(z)
\end{gathered}
$$

with bounded $u_{2}$, then for all $t \in[0, T]$

$$
H(t)=u(t, s(t))
$$

where $L^{2}(Q)$ is the space of square integral random variables with risk-nentral distribution, $Q$
$L^{2}(Q)=\left\{h:[0, T] \times \Omega: \rightarrow \mathbb{R}: \int_{0}^{\top} h^{2}(t) d \omega_{\phi}(t)<d\right\}$

## Proof

From the bowndry cordition $u(T, z)=h(z)$ it follows that

$$
u(T, S(T))=h(S(T))=H(T)
$$

It was previously shown that

$$
\tilde{H}(t)=E_{Q}\left[\tilde{H}(T) \mid \mathcal{F}_{t}\right]
$$

Previously it was shown that

$$
e^{-r t} u(t, s(t))
$$

is a $Q$-mertingale

It follows

$$
\begin{aligned}
\tilde{H}(t) & =E_{Q}\left[\tilde{H}(T) \mid \mathcal{F}_{t}\right] \\
\Rightarrow \quad H(t) & =e^{r t} E_{Q}\left[e^{-r T} H(T) \mid \mathcal{F}_{t}\right] \\
& =e^{r t} E_{Q}\left[e^{-r T} u(T, s(T)) \mid \mathcal{F}_{t}\right] \\
& =e^{r t} e^{-r t} u(t, s(t)) \\
& =u(t, s(t))
\end{aligned}
$$

which is the desired result.
Consider

$$
s(t+u)=x+\sigma \omega(u)
$$

where $s(t)=x$ and suppose

$$
\begin{aligned}
& u_{t}+\frac{1}{2} \sigma^{2} u_{z z}=0 \\
& u(T, z)=h(z)
\end{aligned}
$$

Then $u(t, x+6 \omega(T-t))$ is $a$ martingale and

$$
u(t, x)=E[\ln (x+\Delta \omega(T-t))]
$$

Note that the equalion solved by $u(t, z)$ is the heat equation and this is a special case of the Feyman-Kac formula.

## The Replicating Strategy

In previous sections it was shown that the Black-sholes model is complete so a replication strategy exists but no proceedure was given for finding the strategy. Here a method for finding a replicating strategy, prourded the PDE can be solved, is discussed.

## Theorem

If $H(T)=h(S(T)) \geqslant 0$ is $L^{2}$ with respect to $Q$ and if $u(t, z)$ is a solution to

$$
\begin{gathered}
u_{t}+r z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}=r u \\
u(T, z)=h(z)
\end{gathered}
$$

with bounded $u_{2}$, then

$$
\begin{aligned}
& x(t)=u_{z}(t, s(t)) \\
& y(t)=\frac{u(t, s(t))-x(t) s(t)}{A(t)}
\end{aligned}
$$

is an admissible strategy that replicates the payoff $H(T)$.

## Proof

The replicating portfolio is given by the value process.

$$
V_{x y}(t)=x(t) S(t)+y(t) A(t)
$$

using the desired strategy gives

$$
\begin{aligned}
v_{x y}(t) & =x(t) s(t) \\
+ & A(t)\left[\frac{u(t, s(t))-x(t) s(t)}{A(t)}\right] \\
= & x(t) s(t)+u(t, s(t) \cdot x(t) s(t) \\
= & u(t, s(t))
\end{aligned}
$$

Previously it was shown that

$$
u(t, s(t))=H(t)=V_{x y}(t)
$$

It is assumed that $H(t) \geqslant 0$ so $u(t, s(t)) \geqslant 0$. Recall that an admissable strategy $(x, y)$, satisfies,

1) $V(t) \geqslant-L$
2) $\tilde{v}(t)$ is a $Q$-martigale

Thus since $u(t, s(t))$ is bounded from below the first condion of an admissable strategy is satisfied.

Since $u(t, s(t))=H(t)$ and,

$$
\tilde{H}(t)=E\left[\tilde{H}(T) \mid \mathcal{F}_{t}\right]
$$

It follows that $\tilde{v}_{x y}(t)$ is a martingale and

$$
d \tilde{V}_{x y}(t)=d\left(e^{-r t} u(t, s(t))\right)
$$

previously it was shown that

$$
\begin{aligned}
d\left(e^{-r t}\right. & u(t, s(t)) \\
& =e^{-r t} \sigma s(t) u_{2} d \omega_{Q}(t) \\
& =\sigma \tilde{s}(t) u_{2} d \omega_{Q}(t)
\end{aligned}
$$

but $x(t)=u_{2}(t, s(t))$ and

$$
d \tilde{S}(t)=\tilde{S}(t) \sigma d \omega_{Q}(t)
$$

trues

$$
\begin{aligned}
d\left(e^{-r t} u(t, S(t))\right. & =x(t) d \tilde{S}(t) \\
& =d \tilde{V}(t)
\end{aligned}
$$

previously it was shown that a self-finansid strategy satisfles tnis relation.

## The Greeks

The greeks are the parameters used to represent properties of the replicating portfolio. The parameters are denoted by greek letters leading to the name.
Replaction proudes a method of protecting a short position in an option. A replicating portfolio can be can be constructed the ensures the option payoff can be covered.

The first parameter discussed is delta. Consider an investor on the short side of European call option. Also, assume that the volitility, $\sigma$, and risk-free interest rate, $r$, are constant.
Consider a portfolio $(x, y, z)$ in the extended market. For
$a$ fixed $t$ since $\sigma$ and $r$ are constant the value process of the portfolio is a function only of the asset price $s(t)$. This dependency leads to the notation

$$
V_{x y z}(t)=V(s)
$$

The rate of change of the value process with respect to the asset price is called delta.

$$
\delta_{V}=\frac{\partial V(S)}{\partial S}
$$

if

$$
\frac{\partial V(S)}{\partial S}=0
$$

then for $|\varepsilon| \ll 1$

$$
V(s+\varepsilon) \approx V(s)
$$

For the short side of a call option $z=-1$. The delta
hedgins statesy tries to find
$(x, y)$ such that

$$
\frac{\partial V(S)}{\partial S}=0
$$

It follows that

$$
V(S)=x S+y A-C
$$

where $C$ is the price of the call option which was previoushy shown to be given by,
$C(S)=S N\left(d_{+}(S)\right)-K e^{-r(T-t)} N\left(d_{-}(S)\right)$
From the self financing assumption

$$
d V=x d S+y d A-d C
$$

so

$$
\frac{\partial V}{\partial S}=x+y \frac{\partial A}{\partial S}-\frac{\partial C}{\partial S}
$$

but $A$ is independent of $S$ so

$$
\frac{\partial V}{\partial S}=x-\frac{\partial C}{\partial S}
$$

using the expression for $C$ and

$$
\frac{d N(d)}{d d}=n(d)
$$

gives

$$
\begin{aligned}
\frac{\partial L}{\partial S}= & \frac{\partial}{\partial S}\left\{S N\left(d_{+}(S)\right)-\right. \\
& \left.k e^{-r(T-t)} N\left(d_{-}(S)\right)\right\} \\
= & N\left(d_{+}(S)\right)+S n\left(d_{+}(S)\right) \frac{\partial d_{+}(S)}{\partial S} \\
& -k e^{-r(T-t)} n\left(d_{-}(S)\right) \frac{\partial d_{-}(S)}{\partial S}
\end{aligned}
$$

Recalling the identity

$$
k e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right)
$$

gives

$$
\begin{aligned}
\frac{\partial c}{\partial s}= & N\left(d_{+}(s)\right)+s n\left(d_{+}(s)\right) \frac{\partial d_{+}(s)}{\partial s} \\
& -s n\left(d_{+}(s)\right) \frac{\partial d_{-}(s)}{\partial s} \\
= & N\left(d_{+}(s)\right)+\operatorname{sn}\left(d_{1}(s)\right)\left[\frac{\partial d_{+}(s)}{\partial s}\right. \\
& \left.-\frac{\partial d_{-}(s)}{\partial s}\right]
\end{aligned}
$$

Now,
$\frac{\partial d_{+}(s)}{\partial s}-\frac{\partial d_{-}(s)}{\partial s}=\frac{\partial}{\partial s}\left[d_{+}(s)-d_{-}(s)\right]$
but previously it was shown that

$$
d_{+}(s)-d(s)=\sigma \sqrt{T-t}
$$

so

$$
\frac{\partial d_{t}(s)}{\partial s}-\frac{\partial d(s)}{\partial s}=0
$$

it follows that

$$
\frac{\partial c}{\partial s}=N\left(d_{+}(s)\right)
$$

and finally

$$
\begin{aligned}
\frac{\partial V}{\partial S} & =x-\frac{\partial C}{\partial S} \\
& =x-N\left(d_{+}(s)\right) \\
\Rightarrow \frac{\partial V}{\partial S} & =x-N\left(d_{+}(s)\right)
\end{aligned}
$$

Finally the hedging strategy requires

$$
\frac{\partial V(S)}{\partial S}=0
$$

which implies that the value
process dbes not change with the asset price. It follows that

$$
\begin{array}{ll} 
& x-N\left(d_{t}(s)\right)=0 \\
\Rightarrow \quad & x=N\left(d_{t}(s)\right)
\end{array}
$$

To define the remaining greeks note that the value process depends on the following variables,

1) S-Asset price
2) T - Expiry time
3) 6-volatility
4) $r$-risk-free rate of return

The remaining greeks characterize the variability, of the value process with respect to other parameters,

$$
\delta_{v}=\frac{\partial v}{\partial s} \quad r_{v}=\frac{\partial^{2} v}{\partial s^{2}}
$$

$$
\begin{gathered}
\theta_{v}=\frac{\partial v}{\partial T} \quad \text { vega }_{v}=\frac{\partial v}{\partial \sigma} \\
\rho_{v}=\frac{\partial v}{\partial r}
\end{gathered}
$$

Now recall that the price of European call and put options,

$$
\begin{aligned}
C(t)=S(t) & N\left(d_{+}(t, S(t))\right. \\
& -K e^{-r(T-t)} N\left(d_{-}(t, S(t))\right. \\
P(t)=-S(t) & N\left(-d_{+}(t, S(t))\right) \\
& +K e^{-r(T-t)} N\left(-d_{-}(t, S(t))\right)
\end{aligned}
$$

where

$$
\begin{aligned}
& d_{+}(t, z)=\frac{\ln \frac{2}{K}+\left(r+\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, z)=\frac{\ln \frac{2}{K}+\left(r-\frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

and a useful identity is
$K e^{-r(T-t)} n\left(d_{-}(t, z)\right)=2 n\left(d_{+}(t, z)\right)$

## Exercise

Given European call, c, and put, $P$, options both with strike price $K$ and expiny $T$. show

$$
\begin{gathered}
\delta_{c}-\delta_{p}=1 \\
\delta_{p}=-N\left(-d_{+}\right) \\
\gamma_{p}=\gamma_{c}
\end{gathered}
$$

Previously it was shown that

$$
\delta_{c}=N\left(d_{+}(s)\right)
$$

Now

$$
\delta_{p}=\frac{\partial D}{\partial S}
$$

$$
\begin{aligned}
= & \frac{\partial}{\partial S}\left\{-S N\left(-d_{+}(t, S)\right)\right. \\
& +K e^{-r(T-t)} N\left(-d_{-}(t, S)\right\} \\
= & -N\left(-d_{+}\right)+S n\left(-d_{+}\right) \frac{\partial d_{+}}{\partial S} \\
& -K e^{-r(T-t)} n\left(-d_{-}\right) \frac{\partial d_{-}}{\partial S} \\
=- & N\left(d_{-}\right)+S n\left(-d_{+}\right) \frac{\partial d_{+}}{\partial S} \\
& -S n\left(-d_{-}\right) \frac{\partial d_{-}}{\partial S} \\
= & -N\left(-d_{+}\right)+\operatorname{sn}\left(-d_{-}\right)\left\{\frac{\partial d_{+}}{\partial S}-\frac{\partial d_{-}}{\partial S}\right\}
\end{aligned}
$$

since

$$
d_{+}(s)-d(s)=\sigma \sqrt{T-t}
$$

Thus

$$
\delta_{P}=\frac{\partial P}{\partial S}=-N\left(-d_{+}\right)
$$

Further

$$
\begin{aligned}
& \delta_{c}-\delta_{p}=N\left(d_{+}\right)+N\left(-d_{+}\right) \\
= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{d_{+}} e^{-x^{2} / 2} d x+\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-d_{+}} e^{-x^{2}} d x \\
= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{d_{+}} e^{-x^{2} / 2} d x+\frac{1}{\sqrt{2 \pi}} \int_{d_{+}}^{\infty} e^{-x^{2} / 2} d x \\
= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-x^{2} / 2} d x \\
= & 1
\end{aligned}
$$

which is the desired result Finally

$$
\begin{aligned}
\gamma_{P} & =\frac{\partial^{2} P}{\partial s^{2}} \\
& =\frac{\partial}{\partial s}\left(\frac{\partial P}{\partial s}\right) \\
& =\frac{\partial}{\partial s}\left(\delta_{p}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{\partial}{\partial S}\left(-N\left(-d_{+}\right)\right) \\
& =n\left(-d_{+}\right) \frac{\partial d_{+}}{\partial S}
\end{aligned}
$$

Similarly,

$$
\begin{aligned}
\gamma_{c} & =\frac{\partial^{2} s}{\partial s^{2}} \\
& =\frac{\partial \delta c}{\partial s} \\
& =\frac{\partial}{\partial s} N\left(d_{+}\right) \\
& =n\left(d_{+}\right) \frac{\partial d_{x}}{\partial s}
\end{aligned}
$$

but $n\left(d_{+}\right)=n\left(-d_{+}\right)$trues

$$
\gamma_{p}=\gamma_{e}
$$

Deta hedging provides protection against small changes in the asset price. A better strategy can be construded by dso considering the second derivate with respect to $s$,

$$
r_{c}=\frac{\partial^{2} c}{\partial s^{2}}
$$

## Risk and Return

Here the volatility of a European call option is compared to the volatility, of the underlying asset. Recall that,

$$
\begin{aligned}
C(t) & =u(t, S(t))=S(t) N\left(d_{+}(t, S(t))\right. \\
& -K e^{-r(T-t)} N\left(d_{-}(t, S(t))\right.
\end{aligned}
$$

working with the market probability, so that

$$
d S=\mu S d t+\sigma S d \omega
$$

Recall the Itô formula for an Itá process

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t
\end{aligned}
$$

$$
\begin{aligned}
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here

$$
\begin{aligned}
a(t) & =\mu s(t) \\
b(t) & =\sigma s(t) \\
F(t, \bar{X}(t)) & =u(t, z)
\end{aligned}
$$

It follows that,

$$
\begin{aligned}
d u= & u_{t} d t+u_{z} \mu s d t \\
& +u_{z} \sigma s d \omega+2 u_{z z} \sigma^{2} s^{2} d t \\
= & \left(u_{t}+\mu u_{z} s+2 u_{z z} \sigma^{2} s^{2}\right) d t \\
& +u_{z} \sigma s d w
\end{aligned}
$$

To compare the performance of $s$ and $c$ the Black Scholes dinamics of the denvative security,

$$
\begin{aligned}
& \frac{d u}{u}=\mu_{c} d t+\sigma_{c} d \omega \\
\Rightarrow & d u=u\left(\mu_{c} d t+\sigma_{c} d \omega\right)
\end{aligned}
$$

comparing the two relations gives

$$
\begin{aligned}
\left(u_{t}\right. & \left.+\mu u_{z} s+2 u_{z z} \sigma^{2} s^{2}\right) d t \\
& +u_{z} \sigma s d \omega \\
& =u\left(\mu_{c} d t+\sigma_{c} d \omega\right)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
\mu_{c} u & =u_{t}+\mu u_{z} s+\frac{1}{2} u_{2 z} \sigma^{2} s^{2} \\
\Rightarrow \mu_{c} & =\frac{1}{u}\left[u_{t}+\mu u_{z} s+\frac{1}{2} u_{2 z} \sigma^{2} s^{2}\right] \\
\sigma_{c} u & =u_{2} \sigma s
\end{aligned}
$$

$$
\Rightarrow \sigma_{c}=\frac{\sigma S}{u} u_{2}
$$

The volatility of the call opton is $\sigma_{c}$ and $\sigma$ is the volitility of the asset

Previously, it was shown that

$$
u_{2}=N\left(d_{+}\right)
$$

It follows that the ratio of the volatilities

$$
\begin{aligned}
\frac{\sigma_{c}}{\sigma} & =\frac{s}{u} u_{2} \\
& =\frac{s(t)}{c(t)} N\left(d_{1}(t)\right)
\end{aligned}
$$

but

$$
C(t)=S(t) N\left(d_{+}(t)\right)-K e^{-r(T-t)} N\left(d_{-}(t)\right)
$$

50
$\beta_{c}=\frac{\sigma_{c}}{\sigma}=\frac{s(t) N\left(d_{+}(t)\right)}{s(t) N\left(d_{+}(t)\right)-K e^{-r(T-t)} N\left(d_{-}(t)\right)}$

The second term in the denominator is positive

$$
K e^{-r(T-t)} N(d(t))>\partial
$$

it follows that

$$
\frac{\sigma_{c}}{\delta}>1
$$

thus the call option is riskier than the asset.

Now consider $\mu_{c}$. From the Black-Sholes PDE

$$
r u=u_{t}+r S u_{2}+\frac{1}{2} \sigma^{2} s^{2} u_{22}
$$

$$
\begin{aligned}
= & u_{t}+(r-\mu) s u_{z}+\mu s u_{z} \\
& +\frac{1}{2} \sigma^{2} s^{2} u_{z z} \\
= & (r-\mu) s u_{z}+u_{t}+\mu u_{z} s \\
& +\frac{1}{2} u_{z z} \sigma^{2} s^{2}
\end{aligned}
$$

but

$$
\mu_{c} u=u_{t}+\mu u_{z} S+\frac{1}{2} u_{2 z} \sigma^{2} S^{2}
$$

so

$$
\begin{aligned}
r u & =(r-\mu) s u_{2}+\mu_{c} u \\
\Rightarrow \quad \mu_{c} & =\frac{1}{u}\left[r u-(r-\mu) s u_{2}\right] \\
& =\frac{s}{u}(\mu-r) u_{2}+r
\end{aligned}
$$

Bringing things together,

$$
\mu_{c}=\frac{S}{c}(\mu-r) u_{z}+r
$$

$$
\begin{aligned}
& =\frac{s}{c} N\left(d_{+}\right)(\mu-r)+r \\
\beta_{c} & =\frac{s}{c} N\left(d_{+}\right)
\end{aligned}
$$

50

$$
\begin{aligned}
& \mu_{c}=\beta_{c}(\mu-r)+r \\
\Rightarrow & \mu_{c}-r=\beta_{c}(\mu-r)
\end{aligned}
$$

## Extensions and Applications

## Options on Foreign Currency

Currencies are modeled with the same Black-Stoles mode I previously discussed.
The securities used in the model are,
$A(t)$ : The money market account in the home currency
$s(t)$ : The price of one unit of foreign currency.
The model used is given by

$$
\begin{gathered}
d A(t)=r A(t) d t \\
d S(t)=\mu S(t) d t+\sigma S(t) d \omega(t)
\end{gathered}
$$

The foreign currency is thanght
of as a bank account balance in the foreign currency so that an interest rate is earned if the asset is held. If the foreign currency risk-free interest rate is denoted $b y, \delta$, then the position in the foreign currency will compound continuously.
For the stratesy $(x, y)$ it follows that
$v(t)=x(t) e^{\delta t} S(t)+y(t) A(t)$
let

$$
x^{\delta}(t)=x(t) e^{\delta t}
$$

then

$$
v(t)=x^{\delta}(t) S(t)+y(t) A(t)
$$

This strategy represents the deposites in a foreign and domestic banks.

Another representation is given by

$$
\delta^{\delta}(t)=\delta(t) e^{\delta t}
$$

Then

$$
V(t)=x(t) S^{\delta}(t)+y(t) A(t)
$$

Consider this representation. It follows that,

$$
\begin{aligned}
& d s^{\delta}(t)=d\left(e^{\delta t} s(t)\right) \\
& =\delta e^{\delta t} s(t) d t+e^{\delta t} d s(t)
\end{aligned}
$$

but

$$
d s(t)=\mu s(t) d t+\sigma s(t) d \omega(t)
$$

So

$$
\begin{aligned}
& d^{\delta} s(t)=\delta e^{\delta t} s(t) d t \\
& +e^{\delta t}[\mu s(t) d t+\sigma s(t) d \omega(t)]
\end{aligned}
$$

$$
\begin{aligned}
= & (\delta+\mu) e^{\delta t} s(t) d t \\
& +\sigma e^{\delta t} s(t) d \omega(t) \\
= & (\delta+\mu) \delta^{\delta}(t) d t+\sigma \delta^{\delta}(t) d \omega(t)
\end{aligned}
$$

Now for the value process

$$
V(t)=x(t) S^{\delta}(t)+y(t) A(t)
$$

the self financing stratesy is given by

$$
\begin{aligned}
d V(t)= & x(t) d S^{\delta}(t)+y(t) d A(t) \\
= & x(t) d\left(e^{\delta t} S(t)\right)+y(t) d A(t) \\
= & x(t) e^{\delta t} d S(t)+ \\
& +x(t) S(t) \delta e^{\delta t} d t+y(t) d A(t)
\end{aligned}
$$

using

$$
x^{\delta}(t)=x(t) e^{\delta t}
$$

gives

$$
\begin{aligned}
d V(t)=x^{\delta}(t) d S(t) & +y(t) d A(t) \\
& +\delta x^{\delta}(t) S(t) d t
\end{aligned}
$$

Next Consider the discounted value process,

$$
\tilde{v}(t)=e^{-r t} V(t)
$$

so

$$
\begin{aligned}
d \tilde{v}(t) & =d\left(e^{-r t} V(t)\right) \\
& =-r e^{-r t} V(t) d t+e^{-r t} d V(t)
\end{aligned}
$$

From the self-financing condition

$$
d v(t)=x(t) d S^{\delta}(t)+y(t) d A(t)
$$

it follows that

$$
\begin{aligned}
& d \tilde{V}(t)=-r e^{-r t} v(t) d t \\
& \quad+e^{-r t}\left[x(t) d s^{\delta}(t)+y(t) d A(t)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & -r e^{-r t} v(t) d t+e^{-r} x(t) d S^{\delta}(t) \\
& +e^{-r t} y(t) d A(t)
\end{aligned}
$$

Next, recall that

$$
\begin{gathered}
d A(t)=r A(t) d t \\
V(t)=x(t) S^{\delta}(t)+y(t) A(t)
\end{gathered}
$$

50

$$
\begin{aligned}
& d \tilde{V}(t)=-r e^{-r t}\left[x(t) S^{\delta}(t)+y(t) A(t)\right] d t \\
& e^{-r} x(t) d S^{\delta}(t)+e^{-r t} y(t) r A(t) d t \\
&=-r e^{-r t} x(t) S^{\delta}(t) d t \\
&-r e^{-r t} y(t) A(t) d t \\
&+e^{-r} x(t) d S^{\delta}(t) \\
&+r e^{-r t} y(t) A(t) d t
\end{aligned}
$$

$$
\begin{aligned}
= & -r e^{-r t} x(t) S^{\delta}(t) d t \\
& +e^{-r} x(t) d S^{\delta}(t)
\end{aligned}
$$

Previaesly it was shown that,
$d S^{\delta}(t)=(\delta+\mu) S^{\delta}(t) d t+\sigma S^{\delta}(t) d \omega(t)$
thus

$$
\begin{aligned}
& d \tilde{v}(t)=-r e^{-r t} x(t) S^{\delta}(t) d t \\
& +x(t) e^{-r t}\left[(\delta+\mu) S^{\delta}(t) d t\right. \\
& \left.+\sigma S^{\delta}(t) d \omega(t)\right] \\
& =-e^{-r t} S^{\delta}(t) x(t) r d t \\
& +e^{-r t} S^{\delta}(t) x(t)(\delta+\mu) d t \\
& +e^{-r t} S^{\delta}(t) x(t) \sigma d \omega(t) \\
& =e^{-r t} S^{\delta}(t) x(t)[(\delta+\mu-r) d t \\
& +\sigma d \omega(t)]
\end{aligned}
$$

If the bracket term can be written as the differential of a weiner process it is a local martingale.
Let

$$
\omega_{Q}^{\delta}(t)=\frac{(\mu+\delta-r) t}{0}+\omega(t)
$$

It then follows that

$$
\begin{aligned}
d \tilde{V}(t) & =e^{-r t} S^{\delta}(t) x(t) \sigma d \omega_{Q}^{\delta}(t) \\
& =\sigma x(t) \tilde{S}^{\delta}(t) d \omega_{Q}^{\delta}(t)
\end{aligned}
$$

For $\omega_{Q}^{s}$ to be a martingale the risk-neutral probabality is constructed using the simplified Girsanou theorem. Let

$$
u^{\delta}=\frac{\mu+\delta-r}{\sigma}
$$

The distribution where $\omega_{Q}^{\delta}$ is
a weiner process is given by

$$
\begin{array}{r}
Q^{\delta}(A)=E\left(1 _ { A } \operatorname { e x p } \left\{-\frac{1}{2}\left(u^{\delta}\right)^{2} T\right.\right. \\
\left.\left.-u^{\delta} \omega(T)\right\}\right)
\end{array}
$$

Recall

$$
\begin{gathered}
d s^{\delta}=(\delta+\mu) s^{\delta}(t) d t+ \\
\sigma s^{\delta}(t) d \omega(t)
\end{gathered}
$$

using

$$
\begin{aligned}
& \omega_{Q}^{\delta}(t)=\frac{(\mu+\delta-r)}{\sigma}+\omega(t) \\
\Rightarrow & \omega(t)=\omega_{Q}^{\delta}(t)-\left(\frac{\mu+\delta-r}{\sigma}\right) t \\
\Rightarrow & d \omega(t)=d \omega_{Q}^{\delta}(t)-\frac{(\mu+\delta-r)}{\sigma} d t
\end{aligned}
$$

50,

$$
\begin{aligned}
d s^{\delta}= & (\delta+\mu) s^{\delta}(t) d t+ \\
& \sigma s^{\delta}(t)\left\{d \omega_{Q}^{\delta}(t)-\frac{(\mu+\delta-r)}{\sigma} d t\right\} \\
= & (\delta+\mu\} s^{\delta}(t) d t+\sigma s^{\delta}(t) d \omega_{Q}^{\delta}(t) \\
& -s^{\delta}(t)[\mu+\delta-r) d t \\
= & r s^{\delta}(t) d t+\sigma s^{\delta}(t) d \omega_{Q}^{\delta}(t)
\end{aligned}
$$

It follows that the discounted return is given by

$$
\begin{aligned}
d \tilde{s}^{\delta}(t)= & d\left(e^{-r t} s^{\delta}(t)\right) \\
= & -r e^{-r t} s^{\delta}(t) d t+e^{-r t} d s^{\delta}(t) \\
= & -r e^{-r t} / s^{\delta}(t) d t+e^{-r t}\left\{r s^{\delta}(t) d t\right. \\
& \left.\sigma s^{\delta}(t) d \omega_{Q}^{\delta}(t)\right\}
\end{aligned}
$$

$\Rightarrow \quad d \tilde{S}^{\delta}(t)=\sigma \delta^{\delta}(t) d \omega_{Q}^{\delta}(t)$

Since $\omega_{Q}^{\delta}(t)$ is a weiner process
It follows that the discounted value process is a martingale since

$$
d \tilde{V}(t)=\sigma x(t) \tilde{S}^{\delta}(t) d \omega_{Q}^{\delta}(t)
$$

## Definition

A stratesy $(x, y)$ is admissble if its value process satisfies

1) $d v(t)=x(t) d s^{\delta}(t)+y(t) d A(t)$
2) $V(t) \geqslant-L$ for some $L \geqslant 0$
3) $\tilde{V}(t)$ is a $Q^{\delta}$-martingale

The foreign currecy option model is now in a form similar to stock option model

Here for the change in currency price

$$
d s^{\delta}(t)=r s^{\delta}(t) d t+\delta s^{\delta}(t) d \omega \omega_{Q}^{\delta}(t)
$$

while the change in stock price is given by

$$
d S(t)=r S(t) d t+\sigma S(t) d \omega_{Q}(t)
$$

The currency price is obtained by replocing $s(t)$ with $s^{s}(t)$ and $Q$ with $Q^{\delta}$

Now using replication to model the price of a security derivative it is assumed that if it has payoff $H$ then

$$
V(T)=H
$$

The no arbitrage principal implies trat

$$
H(t)=E_{Q}^{\delta}\left[e^{-(T t)} H \mid \mathcal{F}_{t}\right]
$$

For an asset option it was shown that

$$
\begin{aligned}
H(t)=e^{-r(T-t)} & E_{Q}\left[h(S(T)) \mid \mathcal{F}_{t}\right] \\
=e^{-r(T-t)} & E_{Q}\left[h \left(S ( t ) \operatorname { e x p } \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)\right.\right.\right. \\
& \left.\left.+\sigma\left(\omega_{Q}(T)-\omega_{Q}(t)\right\}\right)\right]
\end{aligned}
$$

Making the substitutions

$$
\begin{aligned}
& \text { gives } Q^{\rightarrow} Q^{\delta} \quad S(t)=e^{-\delta t} s^{\delta}(t) \\
& H(t)=e^{-r(T-t)} E_{Q^{\delta}}\left[h(s(T)) \mid \mathcal{F}_{t}\right] \\
& =e^{-r(T-t)} E_{Q^{\delta}}\left[h\left(e^{-\delta T} \delta^{\delta}(T)\right) \mid \mathcal{F}_{t}\right] \\
& =e^{-r(T-t)} E_{Q^{\delta}}\left[h \left(e^{-\delta T} s^{\delta}(t)\right.\right.
\end{aligned}
$$

$$
\begin{aligned}
\exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma\left(\omega_{Q}^{\delta}(T)\right.\right. & \left.\left.\left.-\omega_{Q}^{\delta}(t)\right)\right\} \mid \widetilde{J}_{t}\right] \\
=e^{-r(T-t)} & E_{Q}\left[h \left(e^{-\delta(T-t)} s(t)\right.\right. \\
\exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma\left(\omega_{Q}^{\delta}(T)\right.\right. & \left.\left.\left.-\omega_{Q}^{\delta}(t)\right)\right\} \mid \widetilde{J}_{t}\right] \\
=e^{-r(T-t)} & E_{Q}^{\delta}[h(s(t) \\
\exp \left\{\left(r-\delta-\frac{1}{2 \sigma^{2}}\right)(T-t)\right. & \left.+\sigma\left(\omega_{Q}^{\delta}(T)-\omega_{Q}^{\delta}(t)\right)\right\} \\
& \left.+\mathcal{F}_{t}\right]
\end{aligned}
$$

Here $h(S(T))$ is the derivative security payoff function. Consider a European put opton on the toreign currency
then

$$
h(z)=(k-z)^{+}
$$

Recall the auxillany functions

$$
\psi(t, z)=E_{Q}\left[\psi(t, z, \bar{y}) \mid \mathcal{F}_{t}\right]
$$

Here

$$
\begin{gathered}
z=s(t) \\
\left.\sqrt{T \cdot t} I=\omega_{Q}^{\delta}(T)-\omega_{Q}^{\delta}(t)\right) \\
I \sim \operatorname{Normal}(0,1) \\
h(z)=\psi(t, z, I) \\
H(t)=\psi(t, z)
\end{gathered}
$$

It follows that

$$
\psi(t, z, \bar{I})=(K-S(T))^{+}
$$

$$
\begin{aligned}
S(T)= & S(t) \exp \left\{\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)\right. \\
& +\sigma \sqrt{T-t} \underline{Y}\}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
\psi(t, 2) & =e^{-r(T-t)} \int_{R} \frac{1}{\sqrt{2 \pi}} e^{-y^{2} / 2} \\
(K & =2 \exp \left\{\left(r-\delta \cdot \frac{1}{2} \sigma^{2}(T-t)\right.\right. \\
& +\sigma \sqrt{T-t} y\})^{+} d y
\end{aligned}
$$

The integral is zero if

$$
\begin{aligned}
\Rightarrow \quad k-2 \exp \left\{\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)\right. \\
+\sigma \sqrt{T-t} y\}<0 \\
\Rightarrow \ln \frac{k}{2}<\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)+\sigma \sqrt{T-t} y
\end{aligned}
$$

$$
\Rightarrow \frac{\ln \frac{k}{2}-\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}<y
$$

let

$$
d^{\delta}(t, 2)=\frac{\ln \frac{k}{2}-\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
$$

Then

$$
\begin{aligned}
& \psi(t, z)=\frac{e^{-r(T-t)}}{\sqrt{2 \pi}} \int_{-\infty}^{\delta^{\delta}(t, z)} e^{-y^{2} / 2} \\
& K-z \exp \left\{\left(r-\delta \cdot 2 \sigma^{2}\right)(T-t)\right. \\
&+\sigma \sqrt{T-t} y\} d y \\
&=\frac{e^{-r(T-t)}}{\sqrt{2 \pi}} \int_{-\alpha}^{d^{\delta}(t, z)} k e^{-y^{2} / 2} d y
\end{aligned}
$$

$$
\begin{aligned}
-\frac{e^{-r(T-t)}}{\sqrt{2 \pi}} & \int_{-\infty}^{d^{\delta}(t, z)} 2 \exp \left\{\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)\right. \\
& +\sigma \sqrt{T-t} y\} e^{-y^{2} / 2} d y \\
= & e^{-r(T-t)} K N\left(d^{\delta}(t, z)\right) \\
- & e^{-r\left(T^{2}-t\right)} z e^{\left(r-\delta-\frac{1}{2} \sigma^{2}\right)(T-t)} \\
& \int_{-\infty}^{\sqrt{2 \pi}} e^{\left(\sigma \sqrt{T-t} y-\frac{1}{\partial y^{2}}\right)} d y
\end{aligned}
$$

The integral can be cualuate by completing the square The resultis

$$
\int_{-\infty}^{d^{\delta}(t, z)} e^{\left(\gamma \sqrt{1-t} y-\frac{1}{\partial} y^{2}\right)} d y
$$

$$
=e^{\frac{1}{2} \sigma^{2}(T-t)} N\left(d^{\delta}(t, z)-\sigma \sqrt{T-t}\right)
$$

bringing things together
gives

$$
\begin{aligned}
\psi(t, z) & =e^{-r(T-t)} K N\left(d^{\delta}(t, z)\right) \\
- & e^{-\delta(T-t)} Z N\left(d^{\delta}(t, z)-\sigma \sqrt{T-t}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
P(t) & =e^{-r(T-t)} K N\left(d^{\delta}(t, s(t))\right) \\
- & e^{-\delta(T-t)} s(t) N\left(d^{\delta}(t, s(t)-\sigma \sqrt{T-t})\right.
\end{aligned}
$$

Recall that for a put option or a derivative security it was previously found that

$$
\begin{gathered}
P(t)=K e^{-r(T-t)} N(d(t, s(t))) \\
-s(t) N(d(t, s(t))-\sigma \sqrt{T-t})
\end{gathered}
$$

Which are equal is $\delta=0$.
Following the proceedure used previously it can be shown trat

$$
\begin{array}{r}
C(t)=e^{-\delta(T-t)} S(t) N\left(d_{-}^{\delta}(t, S(t))\right) \\
-k e^{-r(T-t)} N\left(d_{-}^{\delta}(t, S(t))\right) \\
P(t)=e^{-\delta(T-t)} S(t) N\left(-d_{-}^{\delta}(t, S(t))\right) \\
-k e^{-r(T-t)} N\left(-d_{-}^{\delta}(t, S(t))\right) \\
d_{ \pm}^{\delta}(t, z)=\frac{\ln \frac{2}{K}+\left(r-\delta \pm \frac{1}{\partial} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{array}
$$

$$
=\frac{\ln \frac{2}{k} e^{-\delta(T-t)}\left(r \pm \frac{1}{2} \delta^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
$$

Now for a European call option

$$
C(t)=u(t, S(t))
$$

where $u(t, z)$ is the deterministic function

$$
\begin{aligned}
u(t, z) & =e^{-\delta(T-t)} z N\left(d_{+}^{\delta}(t, z)\right) \\
- & k e^{-r(T-t)} N\left(d_{-}^{\delta}(t, z)\right)
\end{aligned}
$$

which satisfies the equation

$$
\begin{gathered}
u_{t}+(r-\delta) z u_{z}+\frac{1}{2} \sigma^{2} z^{2} u_{z z}=r u \\
u(T, z)=(z-K)^{+}
\end{gathered}
$$

The replicating strategy is the same as obtained previously

$$
\begin{gathered}
x(t)=u_{2}(t, S(t)) \\
y(t)=\frac{u(t, S(t))-x(t) S(t)}{A(t)}
\end{gathered}
$$

which has the value process

$$
v_{x y}(t)=x(t) S(t)+y(t) A(t)
$$

where the discounted value process is a $Q^{\delta}$-martingale satisfying

$$
\tilde{V}_{x y}(t)=\tilde{H}(t)=e^{-r T} E_{Q}^{s}\left[h(s(T)) \mid \mathcal{F}_{t}\right]
$$

This same model can be used for a dividend paying stock.

## Stuctural Model of Credit Risk

The Black-Sholes model can also be used to model credit risk.

Consider a company with assets worth $v(t)$ at time $t$. It is assumed that all assets are liquid firancial securities. Assume that the purchase of the assets were financed with an amount of debt D. Also, assume that the debt payment is due at time $T$.
If $V(T) \leqslant D$ the company goes bankrupt and the debt holders recreve V(T) while the equily hoders recieve 0 .
If $V(T)>D$ the debt is repaid
and the debt hodders get 0 and the equity holders get $V(T)-D$.
Denote the equity by

$$
E(T)=\left\{\begin{array}{cc}
V(T)-0 & \text { if } V(T)>D \\
0 & \text { if } V(T) \leqslant D
\end{array}\right.
$$

This is the same payoff as a european call option with strike proce $D$.
The following associations can be made with the previous crahysis of asset prices

$$
\begin{aligned}
S(t) & =V(t) \\
K & =D \\
C(t) & =E(t)
\end{aligned}
$$

## Compound Options

A compound option is an option on an option. If this is restricted to ewropean Call and put options there are four possibilities

1) Call on Call
2) Put on call
3) call on Put
4) Put on Put

Consider a european call option with strike price $k_{2}$ and an exercise time $T_{2}$ is traded.
The call option will be considered as the underl/ing asset for a derivative security. The parameters of the call option are assumed fixed. The call option price at trme $t$ will be

## denoted by $C(t)$

Consider a new call option (referred to as a call on call) with exercise time $T_{1} \leqslant T_{2}$, the conderlying option must be active, and strike price $K_{1}$. The payoff of the callon call is given by

$$
H\left(T_{1}\right)=\left(C\left(T_{1}\right)-K_{1}\right)^{+}
$$

The idea is to formulate this payoff, contingent on $c(t)$, as a payoff with stock as the underlying security.

Now, from the Black-Sholes formula

$$
c(t)=u(t, s(t))
$$

where

$$
\begin{array}{rl}
u(t, z)=2 & N\left(d_{1}(t, z)\right) \\
& -K_{2} e^{-r(T-t)} N(d(t, z))
\end{array}
$$

It follows that

$$
C\left(T_{1}\right)=u\left(T_{1}, S\left(T_{1}\right)\right)
$$

The pajoff $H$ can be roplicated by a strategy whose discounted value process follows a martingal with respect to the TISK nextral probability $Q$ with random variable $\omega_{Q}$.
Here a risk-neutoral probability $Q$ is assumed and will not be indicated in the notation.

It follows that the price of the call on call option is given b. 1

$$
C C(t)=E\left[e^{-r\left(T_{1}-t\right)} H\left(T_{1}\right) \mid \mathcal{F}_{t}\right]
$$

$$
\begin{aligned}
& =e^{-r\left(T_{1}-t\right)} E\left[H\left(T_{1}\right) \mid \mathcal{F}_{t}\right] \\
& =e^{-r\left(T_{1}-t\right)} E\left[\left(u\left(T_{1}, S\left(T_{1}\right)\right)-K_{1}\right)^{t} \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

at $t=0$

$$
c c(0)=e^{-r T_{1}} E\left[\left(u\left(T_{1}, s\left(T_{1}\right)\right)-k_{1}\right)^{t} \mid \mathcal{F}_{t}\right]
$$

From the Black-Sholes model

$$
\begin{aligned}
s\left(T_{1}\right) & =s(0) \exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right) T_{1}+\sigma \omega\left(T_{1}\right)\right\} \\
& =F\left(T_{1}, X_{1}\right)
\end{aligned}
$$

where
$F(t, x)=s(0) \exp \left\{\left(r-\frac{1}{2} \sigma^{2}\right) T_{1}+\sigma \sqrt{t} x\right\}$
with

$$
\begin{aligned}
& \bar{X}_{1} \sim N(0,1) \\
\Rightarrow \quad & \bar{X}_{1}=\frac{1}{\sqrt{T_{1}}} \omega(t)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
c c(t) & =e^{-r\left(T_{1}-t\right)} E\left[\left(u\left(T_{1}, s\left(T_{1}\right)\right)-K_{1}\right)^{t} \mid \mathcal{F}_{t}\right] \\
& =e^{-r\left(T_{1}-t\right)} E\left[\left(u\left(T_{1}, F\left(T_{1}, X_{1}\right)-K_{1}\right)^{t} \mid \mathcal{F}_{t}\right]\right.
\end{aligned}
$$

since $\bar{X}_{1} \sim N(0,1)$ it follows that the probability density is given by

$$
f(x)=\frac{1}{12 \pi} e^{-x^{2} / 2}
$$

It follows that

$$
\begin{aligned}
& C C(O)=e^{-r T_{1}} \int_{-\infty}^{\Delta}\left(u\left(T_{1}, F\left(T_{1}, T_{1}\right)-k_{1}\right)^{+}\right. \\
& \frac{1}{12 \pi} e^{-x^{2} / 2} d x
\end{aligned}
$$

If the functions $F(T, x)$ and $u(T, 2)$ are assumed to have
positive first derivatives so are invertable. Let

$$
\theta(x)=u\left(T_{1}, F\left(T_{1}, x\right)\right)
$$

which is also inoreasing and invertable.
The integrend is positue of

$$
\begin{aligned}
& u\left(T_{1}, F\left(T_{1}, \bar{X}_{1}\right)-K_{1}>0\right. \\
= & \theta(x)-K_{1}>0 \\
\Rightarrow & \theta(x)>K_{1} \\
\Rightarrow & x_{1}=\theta^{-1}\left(K_{1}\right)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
C C(0) & =\frac{e^{-r T_{1}}}{\sqrt{2 \pi}} \int_{x_{1}}^{\infty}\left(u\left(T_{1}, s\left(T_{1}\right)\right)-K_{1}\right) e^{-x^{2} / 2} d x \\
& =\frac{e^{-r T_{1}}}{\sqrt{2 \pi}} \int_{x_{1}}^{\infty} u\left(T_{1}, s\left(T_{1}\right)\right) e^{-x^{2} / 2} d x
\end{aligned}
$$

$$
\begin{aligned}
& -\frac{e^{-r T_{1}}}{\sqrt{2 \pi}} \int_{x_{1}}^{\infty} k_{1} e^{-x^{2} / 2} d x \\
= & \frac{e^{-r T_{1}}}{\sqrt{2 \pi}} \int_{x_{1}}^{\infty} u\left(T_{1}, s\left(T_{1}\right)\right) e^{-x^{2} / 2} d x \\
& -k_{1} e^{-r T_{1}}\left(1-N\left(x_{1}\right)\right)
\end{aligned}
$$

since

$$
1-N\left(x_{1}\right)=\int_{x_{1}}^{\infty} e^{-x^{2} / 2} d x
$$

For a Ewropean call option,

$$
\begin{aligned}
C\left(T_{1}\right)= & U\left(T_{1}, S\left(T_{1}\right)\right) \\
= & S\left(T_{1}\right) N\left(d_{+}\left(T_{1}, S\left(T_{1}\right)\right)\right) \\
& -K_{2} e^{-r\left(T_{2}-T_{1}\right)} N\left(d_{-}\left(T_{1}, S\left(T_{1}\right)\right)\right.
\end{aligned}
$$

It follows that

$$
\frac{e^{-r \pi_{1}}}{\sqrt{2 \pi}} \int_{x_{1}}^{\infty} u\left(T_{1}, s\left(T_{1}\right)\right) e^{-x^{2} / 2} d x
$$

$$
\begin{aligned}
= & e^{-r T_{1}} \int_{x_{1}}^{\infty} S\left(T_{1}\right) N\left(d_{+}\left(T_{1}, S\left(T_{1}\right)\right)\right) \frac{e^{-\frac{x^{2}}{2}}}{\sqrt{2 \pi}} d x \\
& -K_{2} e^{-r T_{2}} \int_{x_{1}}^{\infty} N\left(d_{-}\left(T_{1}, S\left(T_{1}\right)\right) e^{-\frac{x^{2}}{2}} d x\right.
\end{aligned}
$$

Bringing thing together gives

$$
\begin{aligned}
C C(0)= & e^{-r T_{1}} \int_{x_{1}}^{\infty} S\left(T_{1}\right) N\left(d_{1}\left(T_{1}, S\left(T_{1}\right)\right)\right) \frac{e^{-\frac{x^{2}}{2}}}{\sqrt{2 \pi}} d x \\
- & K_{2} e^{-r T_{2}} \int_{x_{1}}^{\infty} N\left(d_{-}\left(T_{1}, S\left(T_{1}\right)\right) e^{-\frac{x^{2}}{2}} d x\right. \\
& -K_{1} e^{-r T_{1}}\left(1-N\left(x_{1}\right)\right)
\end{aligned}
$$

This is considered a closed for solution but eocluating $x_{1}$ is non-trivial. After significant algebra tt can be snown that

$$
\begin{aligned}
C C(0) & =S(0) N_{2}\left(d_{+}\left(T_{1}, S^{*}\right), d_{+}\left(T_{2}, K_{2}\right) ; \rho\right) \\
& -K_{2} e^{-r T_{2}} N_{2}\left(d_{-}\left(T_{1}, S^{*}\right), d_{-}\left(T_{2}, K_{2}\right) ; \rho\right) \\
& -K_{1} e^{-r T_{1}} N_{1}\left(d_{-}\left(T_{1}, S^{*}\left(T_{1}\right)\right)\right.
\end{aligned}
$$

where,

$$
e=\sqrt{\frac{T_{1}}{T_{2}}}
$$

and $s^{*}$ is the solution to the equation

$$
u\left(T_{1}, Z\right)=S\left(T_{1}\right)
$$

and

$$
N_{2}(a, b ; e)=\int_{a}^{\infty} \int_{b}^{\infty} f_{x y}(x, y) d x d y
$$

where $f_{x y}(x, y)$ is the bioarrate normal distribution with covariace e.

## American Call Options

In this section it will be shown that that American options and European options on the same asset have the same price process.
Here a risk-neutral distribution is assumed and will not specified in the notation.

## Theorem

Let $c(t)$ be the price process of a European call option for $t \in[0, T]$

$$
(s(t)-k)^{+} \leqslant c(t)
$$

## Proof

Recall that an admissalde replication strategy for a value process $V(t)$ is given
by,

1) $V(t) \geqslant-L$
2) $\tilde{v}(t)$ is a $Q$ - martingale

It follows that if $v(t)$ is a replicating stratesy for the call option that

$$
\tilde{c}(t)=\tilde{v}(t)
$$

it follows that $\tilde{c}(t)$ is a Q-maringale, so

$$
c(t)=e^{r t} \tilde{c}(t)
$$

since $\tilde{C}(t)$ is a martingale

$$
\tilde{c}(t)=E\left[\tilde{c}(T) \mid \tilde{J}_{t}\right]
$$

so

$$
\begin{aligned}
c(t) & =e^{r t} \tilde{c}(t) \\
& =e^{r t} E\left[\tilde{c}(T) \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =e^{r t} E\left[e^{-r T} C(\tau) \mid \mathcal{F}_{t}\right] \\
& =e^{-r(T-t)} E\left[(S(T)-K)^{t} \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
& (S(T)-K)^{+}=\max [(S(T)-K), 0] \\
\Rightarrow \quad & S(T)-K \leqslant \max [(S(T)-K), 0]
\end{aligned}
$$

so

$$
\begin{aligned}
c(t)= & e^{-r(T-t)} E\left[(S(T)-K)^{t} \mid \mathcal{F}_{t}\right] \\
\geqslant & e^{-r(T-t)} E\left[S(T)-K \mid \mathcal{F}_{t}\right] \\
= & e^{-r(T-t)} E\left[S(T) \mid \mathcal{F}_{t}\right] \\
& -e^{r(T-t)_{k}} \\
= & e^{r t} E\left[e^{-r T} S(T) \mid \mathcal{F}_{t}\right] \\
& -K e^{r(T-t)} \\
= & e^{r t} E\left[\tilde{S}(T) \mid \mathcal{F}_{t}\right] \cdot K e^{r(T-t)}
\end{aligned}
$$

$$
=e^{r t} \tilde{s}(t)-k e^{r(T-t)}
$$

since $\tilde{S}(T)$ is a $Q$ - maxtingale Finally,

$$
\begin{aligned}
c(t) & \geqslant e^{r t} e^{-r t} s(t)-k e^{r(T-t)} \\
& =s(t)-k e^{r(T-t)} \\
& \geqslant s(t)-k
\end{aligned}
$$

The last step follows from

$$
e^{-r(T-t)} \geqslant 1
$$

Thus

$$
c(t) \geqslant s(t)-k
$$

now since

$$
\begin{aligned}
& c(t)=\max (s(t)-k, 0) \\
& \Rightarrow \quad c(t) \geqslant 0
\end{aligned}
$$

and the final result follows

$$
c(t) \geqslant(s(t)-k)^{t}
$$

## Theorem

The prices of American and European options or equal.

## Proof

If the hoder of an American option were to exerase before $T$ it follows from the previous theorem that the return from exercising the option is less than the option price. The holder of the option would make more by selling the option.

This relation does not hod for put options. Let $P(t)$ be the price of a europan put option. let

$$
\tilde{P}(t)=\tilde{V}(t)
$$

for some admissable replication strategy. It follows that $\hat{P}(t)$ is a martingule.
Now,

$$
P(t)=e^{r t} \tilde{P}(t)
$$

since $\tilde{P}(t)$ is a martingle

$$
\widetilde{P}(t)=E\left[\tilde{P}(T) \mid \widetilde{F}_{t}\right]
$$

50

$$
\begin{aligned}
P(t) & =e^{r t} E\left[\tilde{P}(T) \mid \mathcal{F}_{t}\right] \\
& =e^{-r(T-t)} E\left[P(T) \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

but

$$
\begin{aligned}
P(T) & =(K-S(T))^{+} \\
& =\max (K-S(T), 0) \\
& \geqslant K-S(T) \\
S 0 & \\
P(t) & =e^{-r(T-t)} E\left[P(T) \mid \mathcal{F}_{t}\right] \\
& =e^{-r(T-t)} E\left[(K-S(T))^{+} \mid \mathcal{F}_{t}\right] \\
& \geqslant e^{-r(T-t)} E\left[K-S(T) \mid \mathcal{F}_{t}\right] \\
& =K e^{-r(T-t)}-e^{-r(T-t)} E\left[S(T) \mid \mathcal{F}_{t}\right] \\
& =K e^{-r(T-t)}-e^{r t} E\left[e^{-r T} S(T) \mid \mathcal{F}_{t}\right] \\
& =K e^{-r(T-t)}-e^{r t} E\left[\tilde{S}(T) \mid \mathcal{F}_{t}\right] \\
& =K e^{-r(T-t)}-e^{r t} \tilde{S}(t) \\
& =K e^{-r(T-t)}-S(t)
\end{aligned}
$$

The next to last step follows because $\vec{S}(t)$ is a martingate
so

$$
P(t) \geqslant k e^{-r(T-t)}-s(t)
$$

unlike the studion with a call option here

$$
\begin{aligned}
& K e^{-r(T-t)} \leqslant K \\
\Rightarrow & K e^{-r}-S(t) \leqslant K-S(t)
\end{aligned}
$$

it follows that the same inequality established for call options does not exist for put options.

## Variable Coefficients

So far it has been assumed that the parameters $\mu$ and $\sigma$ is the Black-Sholes model have been assumed constant. Here the case where the are functions of time are considered.
The asset differential is given by

$$
d s(t)=\mu(t) s(t) d t+\sigma(t) s(t) d \omega(t)
$$

It as assumed that $\mu(t)$ and $\sigma(t)$ are bounded and measureable on interval $[O, T]$

Consider

$$
\begin{gathered}
s(t)=s(0) \exp \left\{s_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
\left.+\int_{0}^{t} \sigma(s) d \omega(s)\right\}
\end{gathered}
$$

Snow that $S(t)$ has the differential previously stated

Recall the It's formla for a function of the form $F(t, \bar{X}(t))$

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here

$$
\begin{aligned}
s(t, \omega(t)) & =F(t, \bar{X}(t)) \\
\omega(t) & =\bar{X}(t)
\end{aligned}
$$

so

$$
\begin{array}{r}
a(t)=0 \quad b(t)=1 \\
d X(t)=d \omega(t)
\end{array}
$$

It follows that

$$
\begin{aligned}
& F_{t}=\frac{\partial S(t)}{\partial t} \\
& =\frac{\partial}{\partial t}\left\{S ( 0 ) \operatorname { e x p } \left[\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right.\right. \\
& \left.\left.\quad+\int_{0}^{t} \sigma(s) d \omega(s)\right]\right\} \\
& =\quad s(0)\left[\mu(t)-\frac{1}{2} \sigma^{2}(t)\right] \\
& \quad \exp \left[\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
& \left.\quad+\int_{0}^{t} \sigma(s) d \omega(s)\right] \\
& =\left[\mu(t)-\frac{1}{2} \sigma^{2}(t)\right] s(t)
\end{aligned}
$$

$$
\begin{aligned}
F_{x}= & \frac{\partial S(t)}{\partial \omega(t)} \\
= & \frac{\partial}{\partial \omega(t)}\left\{S ( \partial ) \operatorname { e x p } \left[\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right.\right. \\
& \left.\left.+\int_{0}^{t} \sigma(s) d \omega(s)\right]\right\} \\
= & \sigma(t) S(0) \exp \left[\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
& \left.\int_{0}^{t} \sigma(s) d \omega(s)\right] \\
= & \sigma(t) S(t)
\end{aligned}
$$

and

$$
\begin{aligned}
F_{x x} & =\frac{\partial^{2}}{\partial \omega^{2}(t)} s(t) \\
& =\frac{\partial}{\partial \omega(t)} \frac{\partial s(t)}{\partial \omega(t)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{\partial}{\partial \omega(t)} \sigma(t) S(t) \\
& =\sigma(t) \frac{\partial S(t)}{\partial \omega(t)} \\
& =\sigma^{2}(t) S(t)
\end{aligned}
$$

50

$$
\begin{aligned}
& F_{t}=\left[\mu(t)-\frac{1}{2} \sigma^{2}(t)\right] s(t) \\
& F_{x}=\sigma(t) s(t) \\
& F_{x x}=\sigma^{2}(t) s(t) \\
& a(t)=0 \quad b(t)=1 \quad s(t)=F(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d w(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
d S(t)= & {\left[\mu(t)-\frac{1}{2} \sigma^{2}(t)\right] S(t) d t } \\
& +\sigma(t) S(t) d \omega(t) \\
& +\frac{1}{2} \sigma^{2}(t) S(t) d t \\
d S(t)= & \mu(t) S(t) d t+\sigma(t) S(t) d \omega(t)
\end{aligned}
$$

which is the desired result.

