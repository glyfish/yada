Brownian Motion

$$
\begin{aligned}
& \text { Troy Stribling } \\
& \text { Feb. } 52017
\end{aligned}
$$

## Brownian Motion

A slochastic process $B=\{B(): t \geqslant 0\}$ is Brownian Motion is

1. $B(0)=0$
2. B has both stationary and independent increments
3. $B(t)-B(s)$ has a normal distribution with 0 mean and wariance $t-s$ where $0 \leqslant s \leqslant t$.

To generate $B(t)$ simulate $k$ steps at times

$$
t_{0}=0<t_{1}<t_{2}<\cdots<t_{k}
$$

to obtain

$$
\left(B\left(t_{0}\right), B\left(t_{1}\right), B\left(t_{2}\right), \ldots, B\left(t_{k}\right)\right)
$$

Using

$$
\begin{aligned}
& B\left(t_{n}\right)=B\left(t_{n-1}\right)+\left[B\left(t_{n}\right)-B\left(t_{\text {(nr) }}\right)\right] \\
& n=1,2,3, \ldots, K
\end{aligned}
$$

where

$$
B\left(t_{n}\right)-B\left(t_{n-1}\right)=\Delta B\left(t_{n}\right)
$$

is normally distributed with
0 mean and variance

$$
\sigma^{2}=t_{n} \cdot t_{n-1}=\Delta t_{n}
$$

then generate $k$ unit normals

$$
z_{1}, z_{2}, \ldots, z_{k}
$$

50

$$
\Delta B\left(t_{n}\right)=\sqrt{\Delta t_{n}} Z_{n}
$$

and

$$
B\left(t_{n}\right)=B\left(t_{n-1}\right) \rightarrow \Delta B\left(t_{n}\right)
$$

Now using $t_{0}=0, B(0)=0$

$$
\Delta t_{1}=t_{1}
$$

and

$$
\begin{aligned}
B\left(t_{1}\right) & =\Delta B\left(t_{1}\right) \\
& =\sqrt{t_{1}} Z_{1}
\end{aligned}
$$

and

$$
\begin{aligned}
B\left(t_{2}\right)= & B\left(t_{1}\right)+\Delta B\left(t_{2}\right) \\
= & \sqrt{t_{1}} z_{1}+\sqrt{t_{2}-t_{1}} z_{2} \\
B\left(t_{3}\right)= & B\left(t_{2}\right)+\Delta B\left(t_{2}\right) \\
= & \sqrt{t_{1}} z_{1}+\sqrt{t_{2}-t_{1}} z_{2} \\
& +\sqrt{t_{2}-t_{3}} z_{3}
\end{aligned}
$$

it follows that

$$
B\left(t_{n}\right)=\sum_{i=1}^{n} \sqrt{t_{i}-t_{i-1}} z_{i}=\sum_{i=1}^{n} \sqrt{\Delta t_{i}} z_{n}
$$

If it is furthur assumed that $\Delta t_{i}$ is constant for

$$
0<t_{1}<t_{2}<\cdots<t_{n}<\cdots<t_{k}
$$

then

$$
\Delta t_{i}=\frac{t_{k}}{k}
$$

and

$$
B\left(t_{n}\right)=\sqrt{\frac{E_{k}}{k}} \sum_{i=1}^{n} Z_{i}
$$

The mean of $B\left(t_{n}\right)$ is easily seen to be

$$
\left\langle B\left(t_{n}\right)\right\rangle=0
$$

Since

$$
\left\langle Z_{n}\right\rangle=0
$$

and since $\left\langle B\left(t_{n}\right)\right\rangle=0$ the variance is given by

$$
\begin{aligned}
\sigma^{2} & =\left\langle B\left(t_{n}\right)^{2}\right\rangle=t_{k} \sum_{i=1}^{n} 1 \\
& =\frac{t_{k}}{k} n=
\end{aligned}
$$

Since the variance of $z_{n}$ is 1. After $k$ steps

$$
\sigma^{2}=t_{k}
$$

## Browniar Motion with Drift

Brownian motion with drift is defined by

$$
X(t)=\sigma B(t)+\mu t \quad \sigma>0
$$

## where

1. $x(t)=0$
2. $x$ is stationary with independent increments.
3. $x(t)-x(s)$ is normally distributed with mean $\mu(t-s)$ and variance $\sigma^{2}(t-s)$ where $0 \leqslant s<t$

Just like Brownian motion a reccurence can be used to compute the value at time $t_{n}$ for $k$ slees

$$
\begin{aligned}
X\left(t_{n}\right) & =X\left(t_{n-1}\right)+\left[X\left(t_{n}\right)-X\left(t_{n-1}\right)\right] \\
& =X\left(t_{n-1}\right)+\Delta X\left(t_{n}\right)
\end{aligned}
$$

where

$$
n=1,2,3, \ldots, k \quad 0<t_{1}<t_{2}<\cdots<t_{n}<\cdots<t_{k}
$$

From the definition of Brownian Motion with Drift $\Delta x\left(t_{n}\right)$ is Normally distributed with mean

$$
\mu\left(t_{n}\right)=\mu \Delta t_{n}
$$

and variance

$$
\sigma^{2}\left(t_{n}\right)=\sigma^{2} \Delta t_{n}
$$

where

$$
\Delta t_{n}=t_{n}-t_{n-1}
$$

and $\mu$ and $\sigma$ are given parameterizonts of the process. $\Delta x\left(t_{n}\right)$ can be generated with a unit normal $z_{n}$ using

$$
\Delta x\left(t_{n}\right)=\sigma \sqrt{\Delta t_{n}} Z_{n}+\mu \Delta t_{n}
$$

using $x(0)=0$ and $t_{0}=0$

$$
\begin{aligned}
x\left(t_{1}\right) & =\Delta x\left(t_{1}\right) \\
x\left(t_{2}\right) & =x\left(t_{1}\right)+\Delta x\left(t_{2}\right) \\
& =\Delta x\left(t_{1}\right)+\Delta x\left(t_{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
x\left(t_{3}\right) & =x\left(t_{2}\right)+\Delta x\left(t_{3}\right) \\
& =\Delta x\left(t_{1}\right)+\Delta x\left(t_{2}\right)+\Delta x\left(t_{3}\right)
\end{aligned}
$$

So for th

$$
\begin{aligned}
x\left(t_{n}\right) & =\sum_{i=1}^{n} \Delta x\left(t_{i}\right) \\
& =\sum_{i=1}^{n}\left(\sigma \sqrt{\Delta t_{i}} z_{i}+\mu \Delta t_{i}\right)
\end{aligned}
$$

where for $k$ steps

$$
n=1,2,3, \cdots, k \quad 0<t_{1}<t_{2}<\cdots<t_{n}<\cdots<t_{k}
$$

If it is funther assumed that $\Delta t_{i}$ is constant and siven by

$$
\begin{aligned}
\Delta t_{i} & =\frac{t_{k}}{k} \\
x\left(t_{n}\right)= & \sigma \sqrt{\frac{t_{k}}{k}} \sum_{i=1}^{n} z_{i}+\mu \frac{t_{k}}{k} \sum_{i=1}^{n}( \\
= & \sigma \sqrt{\frac{t_{k}}{k}} \sum_{i=1}^{n} z_{i}+\mu \frac{t_{k}}{k} n
\end{aligned}
$$

Now the mean after $n$ steps is

$$
\left\langle x\left(t_{n}\right)\right\rangle=\mu_{n}=\mu \frac{t_{k}}{k} n
$$

since for the unit normal

$$
\left\langle Z_{i}\right\rangle=0
$$

The variance aften $n$ steps is given by

$$
\begin{aligned}
\sigma_{n}^{2}= & \left\langle x\left(t_{n}\right)^{2}\right\rangle-\mu_{n}^{2} \\
& \left\langle\left[\sigma \sqrt{\frac{t_{k}}{k}} \sum_{i=1}^{n} z_{i}+\mu_{n}\right]^{2}\right\rangle-\mu_{n}^{2} \\
= & \left\langle\sigma^{2} \frac{t_{k}}{k} \sum_{i=1}^{n} \sum_{j=1}^{n} z_{i} z_{j}+\right. \\
& \left.+2 \mu_{n} \sigma \sqrt{\frac{t_{k}}{k}} \sum_{i=1}^{n} z_{i}+\mu_{n}^{2}\right\rangle-\mu_{n}^{2} \\
=\sigma^{2} \frac{t_{k}}{k} & \sum_{i=1}^{n} \sum_{s=1}^{n}\left\langle z_{i} z_{j}\right\rangle+2 \mu_{n} \sigma \sum_{i=1}^{n}\left\langle z_{i}\right\rangle \\
+ & \mu_{n}^{2}-\mu_{n}^{2}
\end{aligned}
$$

The unit normal la definition has zero mean and whit ugriance and from the definition of Brownian Motion the increments $x\left(t_{n}\right)$ are independent. If follows trat

$$
\begin{gathered}
\left\langle z_{i}\right\rangle=0 \\
\left\langle z_{i} z_{j}\right\rangle= \begin{cases}\left\langle z_{i}^{2}\right\rangle=1 & i=j \\
\left\langle z_{i}\left\langle z_{j}\right\rangle=0\right. & i \neq j\end{cases}
\end{gathered}
$$

$$
\begin{aligned}
& \text { sing }\left\langle z_{i} z_{j}\right\rangle=\delta_{i j}= \begin{cases}1 & i=j \\
0 & i \neq j\end{cases} \\
& \sigma_{n}^{2}=\sigma^{2} \frac{t_{k}}{k} \sum_{i=1}^{n} \sum_{i=1}^{n} \delta_{i j}+0 \\
&+\mu_{n}^{2}-\mu_{n}^{2} \\
&= \sigma^{2} \frac{t_{k}}{k} n
\end{aligned}
$$

After $k$ steps we have

$$
\begin{aligned}
& \mu_{k}=\mu t_{k} \\
& \sigma_{k}^{2}=\sigma^{2} t_{k}
\end{aligned}
$$

## Geometric Brownian Motion

Geometric Brownian Motion is defined by

$$
S(t)=S(0) e^{x(t)} \quad t \geqslant 0
$$

where

$$
x(t)=\sigma B(t)+\mu t
$$

and $B(t)$ is Brownian Motion. The reccurence relation for $\lambda\left(t_{n}\right)$ is

$$
x\left(t_{n}\right)=x\left(t_{n-1}\right)+x x\left(t_{n}\right)
$$

with $k$ the number of steps

$$
n=1,2,3, \ldots, k \quad 0<t_{1}<t_{2}<\cdots<t_{n} 2 \cdots<t_{k}
$$

so

$$
\begin{aligned}
s\left(t_{n}\right) & =s(0) e^{x\left(t_{n-1}\right)+\Delta x\left(t_{n}\right)} \\
& =s(0) e^{x\left(t_{n-1}\right)} e^{\Delta x\left(t_{n}\right)}
\end{aligned}
$$

and

$$
S\left(t_{1}\right)=S(0) e^{\underline{\Delta x\left(t_{1}\right)}}=S(0) e^{x\left(t_{1}\right)}
$$

$$
\begin{aligned}
S\left(t_{2}\right) & =S(0) e^{x\left(t_{1}\right)+\Delta x\left(t_{2}\right)} \\
& =S(0) e^{\Delta x\left(t_{1}\right)} e^{\Delta x\left(t_{2}\right)} \\
S\left(t_{3}\right) & =S(0) e^{x\left(t_{2}\right)+\Delta x\left(t_{3}\right)} \\
& =S(0) e^{x\left(t_{2}\right)} e^{\Delta x\left(t_{3}\right)} \\
& =S(0) e^{\Delta x\left(t_{1}\right)}+\Delta x\left(t_{2}\right) e^{\Delta x\left(t_{3}\right)} \\
& =S(0) e^{\Delta x\left(t_{1}\right)} e^{\Delta x\left(t_{2}\right)} e^{\Delta x\left(t_{3}\right)}
\end{aligned}
$$

It follows that $n$

$$
S\left(t_{n}\right)=S(0) \prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)}
$$

Since the $\Delta x\left(t_{i}\right)$ are independent it follows that the $e^{\Delta x\left(t_{i}\right)}$ are independent.
The mean after $n$ steps is given by

$$
\begin{aligned}
\mu_{n}= & \left\langle s\left(t_{n}\right)\right\rangle=\left\langle s(0) \prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)}\right\rangle \\
& =s(0) \prod_{i=1}^{n}\left\langle e^{\Delta x\left(t_{i}\right)}\right\rangle
\end{aligned}
$$

The mean can be pulled inside the product because the esx(ti)
are independent.
Now for a log normally distributed variable $s$ the expectation of the $m$ 'th power of is

$$
\left\langle s^{m}\right\rangle=e^{m \mu-m^{2} \sigma^{2} / 2}
$$

Where $\mu$ and $\sigma^{2}$ are the mean and variance of the wrderlying normal distribution.
Here the interest is in

$$
\left\langle\left(e^{\Delta x\left(t_{i}\right)}\right)^{m}\right\rangle
$$

where distributed.

$$
\begin{aligned}
& \left\langle\Delta x\left(t_{i}\right)\right\rangle=\mu \Delta t_{i} \\
& \left\langle\Delta x\left(t_{i}\right)^{2}\right\rangle=\sigma^{2} \Delta t_{i}
\end{aligned}
$$

50

$$
\left\langle e^{\Delta x\left(t_{i}\right)}\right\rangle=e^{\Delta t_{i}\left(\mu-\frac{1}{2} \sigma^{2}\right)}
$$

and

$$
\mu_{n}=S(0) \prod_{i=1}^{n}\left\langle e^{\Delta x\left(t_{i}\right)}\right\rangle
$$

$$
=S(0) \prod_{i=1}^{n} e^{\Delta t_{i}\left(\mu-\frac{1}{2} \sigma^{2}\right)}
$$

The variance after $n$ steps is given by

$$
\sigma_{n}^{2}=\left\langle S\left(t_{n}\right)^{2}\right\rangle-\left\langle S\left(t_{n}\right)\right\rangle^{2}
$$

Now

$$
\begin{gathered}
\left\langle S\left(t_{n}\right)^{2}\right\rangle=\left\langle\left(S(0) \prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)}\right)^{2}\right\rangle \\
=\left\langle S(0)^{2} \prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)} \prod_{j=1}^{n} e^{\Delta x\left(t_{j}\right)}\right\rangle \\
=S(0)^{2}\left\langle\prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)} e^{\Delta x\left(t_{i}\right)}\right\rangle \\
=S(0)^{2} \prod_{i=1}^{n}\left\langle e^{\Delta x\left(t_{i}\right)} e^{\Delta x\left(t_{i}\right)}\right\rangle
\end{gathered}
$$

The average can be brought inside protuct since the $\Delta x\left(t_{i}\right)$ are independent
so

$$
\left\langle S\left(t_{n}\right)^{2}\right\rangle=S(0)^{2} \prod_{i=1}^{n}\left\langle\left(e^{\Delta x\left(t_{i}\right)}\right)^{2}\right\rangle
$$

using the expression for expectation of the square of a log normal random variable

$$
\left\langle S^{2}\right\rangle=e^{2\left(\mu-\sigma^{2}\right)}
$$

gives

$$
\left\langle\left(e^{\Delta x\left(t_{i}\right)}\right)^{2}\right\rangle=e^{2 \Delta t_{i}\left(\mu-\sigma^{2}\right)}
$$

and

$$
\left\langle S\left(t_{n}\right)^{2}\right\rangle=S(0)^{2} \prod_{i=1}^{n} e^{2 \Delta t_{i}}\left(\mu-\sigma^{2}\right)
$$

The variance is

$$
\sigma_{n}=\left\langle S\left(t_{n}\right)^{2}\right\rangle-\left\langle S\left(t_{n}\right)\right\rangle^{2}
$$

where
$\langle S(\operatorname{tn})\rangle^{2}=\left[S(0) \prod_{i=1}^{n} e^{\Delta t_{i}\left(\mu-\frac{1}{2} \sigma\right)}\right]^{2}$
If it is assumed the $\Delta t_{i}$ is constant, for $k$ total steps

$$
\Delta t_{i}=\frac{t_{k}}{k}
$$

where $t_{k}$ is the time of the kth step. The mean after $n$ steps beomes

$$
\begin{aligned}
\mu_{n} & =s(0) \prod_{i=1}^{n} e^{\Delta t_{i}\left(\mu-\frac{1}{2} \sigma\right)} \\
& =s(0) \prod_{i=1}^{n} \exp \left[\frac{t_{k}}{k}\left(\mu-\frac{1}{2} \sigma\right)\right] \\
& =s(0)\left\{\exp \left[\frac{t_{k}}{k}\left(\mu-\frac{1}{2} \sigma\right)\right]\right\}^{n} \\
& =s(0) \exp \left[\frac{n t_{k}}{k}\left(\mu-\frac{1}{2} \sigma\right)\right]
\end{aligned}
$$

and

$$
\begin{aligned}
\left\langle S\left(t_{n}\right)^{2}\right\rangle & =S(0)^{2} \prod_{i=1}^{n} e^{2 \Delta t_{i}}(\mu-\sigma) \\
& =S(0)^{2} \prod_{i=1}^{n} \exp \left[\frac{2 t_{k}}{k}(\mu-\sigma)\right] \\
& =S(0)^{2}\left\{\exp \left[\frac{\partial t_{k}}{k}(\mu-\sigma)\right]\right\}^{n}
\end{aligned}
$$

$$
=s(0)^{2} \exp \left[\frac{2 n t_{k}}{k}(\mu-0)\right]
$$

The variance is

$$
\begin{aligned}
& \sigma_{n}^{2}=\left\langle s\left(t_{n}\right)^{2}\right\rangle-\left\langle s\left(t_{n}\right)\right\rangle^{2} \\
= & s(0)^{2} \exp \left[\frac{2 n t_{k}}{k}(\mu-\sigma)\right] \\
= & \left.s(0) \exp \left[\frac{n t_{k}}{k}\left(\mu-\frac{1}{2} 0\right)\right]\right\}^{2} \\
= & s(0)^{2}\left\{\exp \left[\frac{2 n t_{k}}{k}(\mu-\sigma)\right]\right. \\
& \left.-\exp \left[\frac{2 n t_{k}}{k}\left(\mu-\frac{1}{2} \sigma\right)\right]\right\} \\
= & s(0)^{2} \exp \left(\frac{2 n t_{k}}{k} \mu\right)\left\{\exp \left(-\frac{2 n t_{k}}{k} \sigma\right)\right. \\
& \left.-\exp \left(-\frac{2 n t_{k}}{k} \frac{1}{2} \sigma\right)\right\} \\
= & s(0)^{2} \exp \left[\frac{2 n t_{k}}{k}(\mu-0)\right][1] \\
& \left.-\exp \left(\frac{2 n t_{k}}{k} 0\right)\right]
\end{aligned}
$$

## after $k$ steps

$$
\begin{aligned}
& \mu_{k}=s(0) e^{t_{k}\left(\mu-t_{0} \sigma\right)} \\
& \sigma_{k}^{2}=s(0)^{2} e^{2 t_{k}(\mu-\sigma)}\left[1-e^{2 t_{k} \sigma}\right]
\end{aligned}
$$

Geometric Brownian motion is simulated using

$$
s\left(t_{n}\right)=s(0) \prod_{i=1}^{n} e^{\Delta x\left(t_{i}\right)}
$$

where $\Delta x\left(t_{i}\right)$ is generated using a unit normal distribution as described in the Brownian Motion with Prift section.

## Self Similarity

Let $x=\left\{x_{k}: k=1,2,3, \ldots\right\}$ be a stetionary discrete-time stochastic process. This implies that for $d, n \geqslant 1$ and $k_{1}, k_{2}, \ldots, k_{d} \geqslant 0$ the vectors

$$
\left(x_{k_{1}}, x_{k_{2}}, \ldots, x_{k_{d}}\right)
$$

and the vector shifted by

$$
\left(x_{k_{1}+n}, x_{k_{2}+h}, \ldots, x_{k_{d+h}}\right)
$$

have the same distributions
For Qaussian processes this is equivalent to the outocovariane

$$
\gamma(k)=\operatorname{Cov}\left(x_{n}, x_{n+k}\right)
$$

being indenendent of $n$.
The first statement is
refered to a strict stationarity and the second as second order stationarily.

Consider the speration of binning the elements of the random process $x$ and taking the average
$x_{0}, x_{1}, x_{2}, x_{3}, x_{4}, x_{5}, x_{6}, x_{7}, x_{8}$,
If the bin size is taken as

$$
m=3
$$

The following partition is abtained

$$
\begin{aligned}
& x_{0}^{3}=y_{3}\left(x_{0}+x_{1}+x_{2}\right) \\
& x_{1}^{3}=\frac{1}{3}\left(x_{3}+x_{4}+x_{5}\right) \\
& x_{2}^{3}=\frac{1}{3}\left(x_{6}+x_{7}+x_{8}\right)
\end{aligned}
$$

Let $k=0,1,2, \ldots$ parmetorize the average value Then the starting element for bin each bin with size $m=3$

$$
k m=0,3,6
$$

and the last elemement in the bin is

$$
(k+1) m-1=2,5,8
$$

it follows that the bin awerage is given by

$$
x_{k}^{m}=\frac{1}{m} \sum_{i=k m}^{(k+1) m-1} x_{i}
$$

where $k=0,1,2,3, \ldots, m=1,2,3, \ldots$
A discreb⿱e time stochastic process $x$ is self similar with Hurst parameter $t$ where

$$
0<H<1
$$

if

$$
x_{i} \text { and } m^{1-H} x_{k}^{m}
$$

have the same finite dimensional distributions for all $m \geqslant 1$. This means that the vectors with

$$
d \geqslant 1 \text { and } 0 \leqslant k_{1}<\cdots<k_{d}
$$

$$
\left(x_{k_{1}}, x_{k_{2}}, \ldots, x_{k_{d}}\right)
$$

and

$$
\left(m^{1-H} x_{k_{1}}^{m}, m^{1-H} x_{k_{2}}^{m}, \ldots, m^{1-H} x_{k_{d}}^{m}\right)
$$

$$
\begin{aligned}
& \text { Have the same probability } \\
& \text { distributions. }
\end{aligned}
$$

## Fractional Brownian Motion

Fractional Brownian Motion is defined by the stochastic integral

$$
\begin{aligned}
B_{H}(t)=\frac{1}{\Gamma\left(H+\frac{1}{2}\right)} & \left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}-(-s)^{H-4 / 2}\right] d B(s)\right. \\
& \left.+\int_{0}^{t}(t-s)^{H-4 / 2} d B(s)\right\}
\end{aligned}
$$

where $\Gamma$ is the Camma Function

$$
\Gamma(\alpha)=\int_{0}^{\infty} x^{\alpha-1} \exp ^{-x} d x
$$

and $0<H<1$ is the Hurst parameter and dB(s) is ordinary Brownian motion.
A normalized Fractional Brownian Motion $B_{H}=\left\{B_{H}(t): 0 \leqslant t<\infty\right\}$ with or $H<1$ is characterized by the following

1) $B_{H}(t)$ has stationary increments
2) $B_{H}(0)=0$ and $E\left[B_{H}(t)\right]=0$ for $t>0$
3) $E\left[B_{H}^{2}(t)\right]=t^{2 H}$ for $t \geqslant 0$ 4) $B_{H}(t)$ has a Gaussian distribution for $t>0$
