Autoregressive
Processes

Troy Stribling
Aug 26, 2019

## Fractional Brownian Motion Price Models

Here price time series are modeled as geometric fractional Brownian Motion. Let $X_{t}$ denote a geometric fractional Brownian motion time series. It follows that $\ln X_{t}$ is fractional Brownian motion, if

$$
E\left(\ln X_{t}\right)=\mu
$$

then let

$$
y_{t}=\ln x_{t}-\mu
$$

So that $E\left(Y_{t}\right)=0$. Then since $y_{t}$ is Fractional brownian motion it follows that,

$$
E\left(y_{t}^{2}\right)=t^{2 H}
$$

and for $t>s$

$$
\begin{gathered}
E\left[\left(y_{t}-y_{s}\right)^{2}\right]=(t-s)^{2 H} \\
E\left(y_{t} y_{s}\right)=\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{gathered}
$$

and finally if $t$ is discrete and equally spaced, then

$$
\begin{aligned}
& t_{0}=0 \\
& t_{n}=\Delta t n \quad i=0,1,2, \ldots \\
& \Delta t=t_{n}-t_{n-1} \\
& y_{n}=y_{t_{n}}
\end{aligned}
$$

Fractional Brownian noise is defined by

$$
\Delta Y_{n}=Y_{n}-Y_{n-1}
$$

so that

$$
\begin{aligned}
& E\left(y_{n}^{2}\right)=\Delta t^{2 H} n^{2 H} \\
& E\left(\Delta y_{n}^{2}\right)=\Delta t^{2 H}
\end{aligned}
$$

and for $k=1,2,3, \ldots$ the autocorriance is given by

$$
\begin{aligned}
& E\left(\Delta Y_{n} \Delta Y_{n+k}\right)= \\
& \qquad \frac{1}{2} \Delta t^{2 H}\left[(k-1)^{2 H}+(k+1)^{2 H}-2 K^{2 H}\right]
\end{aligned}
$$

## and the autocorrelation by

$$
\begin{aligned}
r_{k}^{H} & =\frac{E\left(\Delta Y_{n} \Delta Y_{n+k}\right)}{E\left(\Delta Y_{n}^{2}\right)} \\
& =\frac{1}{2}\left[(k-1)^{2 H}+(k+1)^{2 H} \cdot 2 k^{2 H}\right]
\end{aligned}
$$

The following pots illustrate the behavior of $E\left(Y_{n}^{2}\right)$ and $r_{k}^{H}$ as functions of time and $H$

Fraction Brownian Motion Variance, $t^{2 H}$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-004.jpg?height=789&width=1204&top_left_y=1051&top_left_x=179)

The above plot shows the variance, $E\left(Y_{n}^{2}\right)$ as a function of time where

$$
t=n \Delta t \quad n=0,1,2, \ldots
$$

For $H=1 / 2$ the variance is a linear function of time,

$$
E\left(Y_{n}^{2}\right)=n \Delta t
$$

and fractional Brownian motion becomes Brownian motion
For $H=1$ the variance is quadratic

$$
E\left(y^{2}\right)=(n \Delta t)^{2}
$$

and finally as $H \rightarrow 0 \quad E\left(Y^{2}\right)$ approaches 1.

Thus for $1<H<1 / 2$ the variance is super linear and for $1 / 2<H<0$ the variance is sublinear. In the plot above the sublinear curves increase
faster than linear for $0<t<1$ and slower for $t>0$. similarly the superlinear curves increase more slowly the lnear for $0<t<1$ and faster than linear for $t>1$
The following plots show the autocorrelation, $r_{n}^{H}$, as a function of time las and example simulations for $0<H<1 / 2$ and $1 / 2<H<1$.
For $0<H<1 / 2$ r $n_{n}^{H}$ exhibits short range negative antocorrelation or antiautocorrelation that quickly approaches zero becoming uncorrelated.

Fraction Brownian Motion Autocovariance, $r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-006.jpg?height=639&width=1032&top_left_y=1322&top_left_x=278)

The following plot shows examples of fractional Brownian motion simulated for $0<H \leqslant 1 / 2$ using the FFT method which models fractional Brownian motion multivariable Gaussian distribution with covariance matrix defined using

$$
\begin{gathered}
r_{k}^{H}=\frac{1}{2}\left[(K-1)^{2 H}+(K+1)^{2 H}-2 K^{2 H}\right] \\
r_{0}^{H}=1
\end{gathered}
$$

FFT Fractional Brownian Motion Comparison
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-007.jpg?height=811&width=1218&top_left_y=1096&top_left_x=197)

The negative autocorrelation is apporent in the examples from small variance and frequent change in direction.
The firal plots show $r_{n}^{H}$ and example simulations for
$1 / 2<H<1$. In this regime $r_{n}^{H}$ is positive but decays more slowly as $H$ approaches 1. The decay is so slow it leads to a property called long range dependence for indicating long range time correlation for fractional Brownian noise.

Fraction Brownian Motion Autocovariance, $r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-008.jpg?height=722&width=1110&top_left_y=1283&top_left_x=225)

The final plot shows example simulations of fractional Brownian motion using the FET method for $1 / 2<H<P$.

FFT Fractional Brownian Motion Comparison
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-009.jpg?height=838&width=1254&top_left_y=519&top_left_x=159)

Here the long range autocorrelation is apparent from the large variance which results from accumulation of correlated noise that infrequently change direction.

## Linear Stochastic Models

## The Autoregressive Process

Let $\varepsilon_{0}, \varepsilon_{1}, \varepsilon_{2}, \ldots, \varepsilon_{n}$ be a sequence of indepedendent and identically distributed random variables with a zero mean Normal distribution with standad deviation $\sigma$,

$$
\varepsilon_{i} \sim N\left(0, \sigma^{2}\right)
$$

The simplest I Inear stochastic model called autoregressive model of order 1, AR(1), is defined by the difference equation

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

where $t=1,2,3, \ldots$
For $\varphi=1$ this becomes Brownian motion low writing out a few steps gives

$$
\begin{aligned}
& x_{1}=\varphi x_{6}+\varepsilon_{1} \\
& x_{2}=\phi x_{1}+\varepsilon_{2}
\end{aligned}
$$

$$
x_{3}=\varphi x_{2}+\varepsilon_{3}
$$

Elimination of $x_{2}$ and $x_{1}$ from $x_{3}$ gives

$$
\begin{aligned}
x_{3} & =\phi x_{2}+\varepsilon_{3}=\phi\left(\phi x_{1}+\varepsilon_{2}\right)+\varepsilon_{3} \\
& =\phi^{2} x_{1}+\phi \varepsilon_{2}+\varepsilon_{3} \\
& =\phi^{2}\left(\theta x_{0}+\varepsilon_{1}\right)+\phi \varepsilon_{2}+\varepsilon_{3} \\
& =\phi^{3} x_{0}+\phi^{2} \varepsilon_{1}+\phi_{2}+\varepsilon_{3}
\end{aligned}
$$

If this is reseated $t$ times

$$
x_{t}=\phi^{t} x_{0}+\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i}
$$

by definition

$$
\begin{aligned}
& E\left(\varepsilon_{i}\right)=0 \\
& E\left(\varepsilon_{i}^{2}\right)=\sigma^{2}
\end{aligned}
$$

making use of this it follows trat the mean, variance and and autscovariance are given by

$$
E\left(x_{t}\right)=\varphi^{t} x_{0}
$$

$$
\begin{aligned}
& E\left(x_{t}^{2}\right)=\phi^{2 t} x_{t}^{2}+\sigma^{2} \frac{\left[1-\left(\phi^{2}\right)^{t-1}\right]}{1-\phi^{2}} \\
\Rightarrow & E\left(x_{t}^{2}\right)-\theta^{2} x_{0}^{2}=\sigma^{2} \frac{\left[1-\left(\phi^{2}\right)^{t-1}\right]}{1-\varphi^{2}} \\
& =E\left(x_{t}^{2}\right)-\left[E\left(x_{t}\right)\right]^{2} \\
\Rightarrow & \operatorname{Var}\left(x_{t}\right)=\sigma^{2} \frac{\left[1-\left(\phi^{2}\right)^{t-1}\right]}{1-\varphi^{2}} \\
& \operatorname{Cov}\left(x_{t} x_{t+n}\right)=\phi^{n} \operatorname{Uar}\left(x_{t}\right)
\end{aligned}
$$

The stochastic process is called stationary if its distribution is intependent or time. This is also referred to as equilibrium. since $x_{t}$ is a sum of normal random random variables $X_{t}$ has a normal distribution. It follows that to show that the process is stationary it is sufficient to show that the
first and second moments are independent of time. To prove this it is sufficient to show that the limit $t \rightarrow \infty$ for the moments is finite which implies that for increasing time the moments approach a constant. It is easy to see that the limit exists for each moment only for

$$
|\varphi|<1
$$

it follows that if this condition is salisfied

$$
\begin{aligned}
& \lim _{t \rightarrow \infty} E\left(x_{t}\right)=0=\mu_{x} \\
& \lim _{t \rightarrow \infty} \operatorname{var}\left(x_{t}\right)=\frac{\sigma^{2}}{1-\varphi^{2}}=\sigma_{x}^{2} \\
& \lim _{t \rightarrow \infty} \operatorname{cov}\left(x_{t} x_{t+n}\right)=\varphi^{n} \sigma^{2}=\gamma(n)
\end{aligned}
$$

The p'th order autoregressive process, AR(p) is defined by

$$
x_{t}=\sum_{i=1}^{P} \varphi_{i} x_{t-i}+\varepsilon_{t}
$$

For example,
$\operatorname{AR(1):~} x_{t}=\varphi_{1} x_{t-1}+\varepsilon_{t}$
$\operatorname{AR(2)}: x_{t}=\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+\varepsilon_{t}$
$\operatorname{ARC3}$ : $x_{t}=\varphi_{1} x_{t-1}+\varphi_{2} x_{t-2}+\varphi_{3} x_{t-3}+\varepsilon_{t}$

## Moving Average Model

Let $\varepsilon_{0}, \varepsilon_{1}, \varepsilon_{2}, \ldots, \varepsilon_{n}$ be a sequence of indepedendent and identically distributed random variables with a zero mean Normal distribution with standard deviation $\sigma$,

$$
\varepsilon_{i} \sim N\left(0, \sigma^{2}\right)
$$

The moving average model of order 1 is defined by,

$$
x_{t}=\theta \varepsilon_{t-1}+\varepsilon_{t}
$$

and the moving average mole 1 of order $q, M A(q)$, is defined by

$$
x_{t}=\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}
$$

## Relationship to AR(1)

It the previous section it was shown that for the ARCI) model defined by,

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

an expression for $x_{t}$ in terms of only the $\varepsilon_{i}$ cond be obtained by repeated substitution of the $x_{i}$ term to obtain,

$$
\begin{aligned}
x_{t}=\phi^{t} x_{0} & +\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i} \\
\Rightarrow \quad x_{t}-\phi^{t} x_{0} & =\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i} \\
& =\sum_{i=0}^{t-1} \phi^{t-1-i} \varepsilon_{i+1}
\end{aligned}
$$

Let $j=t-i \Rightarrow i=t-j$ then

$$
x_{t}-\varphi^{t} x_{0}=\sum_{j=t} \varphi^{j-1} \varepsilon_{t+1-j}
$$

$$
\begin{aligned}
& =\sum_{j=1}^{t} q^{j-1} \varepsilon_{t+1-j} \\
& =\sum_{j=2}^{t} q^{j-1} \varepsilon_{t+1-j}+\varepsilon_{t}
\end{aligned}
$$

finally let $i=j-1$ then

$$
x_{t}-\phi^{t} x_{0}=\sum_{i=1}^{t-1} \phi^{i} \varepsilon_{t-i}+\varepsilon_{t}
$$

Now from the expression for MA (q) abooe it is seen that

$$
\operatorname{MA}(t-1)=\sum_{i=1}^{t-1} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}
$$

Thus $M A(t-1)$ is equal to the expression for $A R C D$ if

$$
\theta_{i}=\phi^{i}
$$

MA(p) Moments
The moments of MA(P) are easily evaluated using

$$
E\left(\varepsilon_{i}\right)=0 \quad E\left(\varepsilon_{i} \varepsilon_{j}\right)=\sigma^{2} \delta_{i j}
$$

thus

$$
\begin{array}{rl}
n u s & E\left(x_{t}\right)=E\left[\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}\right] \\
= & \sum_{i=1}^{q} \theta_{i} E\left(\varepsilon_{t-i}\right)+E\left(\varepsilon_{t}\right) \\
= & 0 \\
E\left(x_{t}^{2}\right)= & E\left[\left(\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}\right)^{2}\right] \\
=E & {\left[\sum_{i=1}^{q} \sum_{j=1}^{q} \theta_{i} \theta_{j} \varepsilon_{t-i} \varepsilon_{t-j}+2 \sum_{i=1}^{q} \theta_{i} \varepsilon_{t} \varepsilon_{t-i}\right.} \\
& \left.+\varepsilon_{t}^{2}\right] \\
= & \frac{9}{\sum_{i=1}^{q}} \sum_{j=1}^{q} \theta_{i} \theta_{j} E\left[\varepsilon_{t-i} \varepsilon_{t-j}\right] \\
& +2 \sum_{i=1}^{s} \theta_{i} E\left[\varepsilon_{t} \varepsilon_{t-i}\right]+E\left(\varepsilon_{t}^{2}\right)
\end{array}
$$

Now for the first term

$$
E\left(\varepsilon_{t-i} \varepsilon_{t-3}\right)=6^{2} \delta_{i j}
$$

and since $t-i<t$ for $i=1,2, \ldots, 9$

$$
E\left(\varepsilon_{t} \varepsilon_{t-i}\right)=0
$$

and finally

$$
E\left(\varepsilon_{t}^{2}\right)=\sigma^{2}
$$

bringing things together gives

$$
\begin{aligned}
E\left(x_{t}^{2}\right) & =\sum_{i=1}^{a} \sum_{j=1}^{a} \theta_{i} \theta_{j} \sigma^{2} \delta_{i j}+\sigma^{2} \\
& =\sum_{i=1}^{a} \theta_{i}^{2} \sigma^{2}+\sigma^{2} \\
& =\sigma^{2}\left(\sum_{i=1}^{a} \theta_{i}^{2}+1\right)
\end{aligned}
$$

and finally for $n>0$

$$
\begin{aligned}
& E\left(x_{t} x_{t+h}\right)=E\left[\left(\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}\right)\right. \\
& \left.\left(\sum_{i=1}^{q} \theta_{i} \varepsilon_{t+h-i}+\varepsilon_{t+h}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & E\left[\sum_{i=1}^{9} \sum_{j=1}^{9} \theta_{i} \theta_{j} \varepsilon_{t-i} \varepsilon_{t+h-i}\right. \\
& +\sum_{i=1}^{9} \theta_{i} \varepsilon_{t-i} \varepsilon_{t+h}+\sum_{i=1}^{9} \theta_{i} \varepsilon_{t+h-i} \varepsilon_{t} \\
& \left.+\varepsilon_{t} \varepsilon_{t+h}\right] \\
= & \sum_{i=1}^{9} \sum_{j=1}^{9} \theta_{i} \theta_{j} E\left(\varepsilon_{t-i} \varepsilon_{t+h-j}\right) \\
& +\sum_{i=1}^{9} \theta_{c} E\left(\varepsilon_{t-i} \varepsilon_{t+h}\right) \\
& +\sum_{i=1}^{9} \theta_{i} E\left(\varepsilon_{t+h-i} \varepsilon_{t}\right) \\
& +E\left(\varepsilon_{t} \varepsilon_{t-h}\right)
\end{aligned}
$$

For the first term
$E\left(\varepsilon_{t-i} \varepsilon_{t+h-j}\right)=\sigma^{2} \delta_{i, j-h}=\sigma^{2} \delta_{i+h, j}$
for the second term $n, i>0$ so $t-i<t+h$ for every $i$ so

$$
E\left(\varepsilon_{t-i} \varepsilon_{t+h}\right)=0
$$

for the throd term

$$
E\left(\varepsilon_{t+h-i} \varepsilon_{t}\right)=\sigma^{2} \delta_{i h}
$$

and for the final term $n>0 \quad$ so

$$
E\left(\varepsilon_{t} \varepsilon_{t+h}\right)=0
$$

Bringing things together gives

$$
\begin{aligned}
& E\left(X_{t} X_{t+h}\right)=\sum_{i=1}^{q} \sum_{j=1}^{q} \theta_{i} \theta_{j} \sigma^{2} \delta_{i+h, j} \\
& +\sum_{i=1}^{q} \theta_{i} \sigma^{2} \delta_{i h} \\
& =\sum_{i=1}^{q} \theta_{i} \theta_{i+h} \sigma^{2}+\theta_{h} \sigma^{2}
\end{aligned}
$$

but $\theta_{i+h}=0$ for $i+h<q$

$$
\rightarrow \quad i<q-h
$$

thus

$$
\begin{aligned}
E\left(x_{t} x_{t+h}\right) & =\sum_{i=1}^{9-h} \theta_{i} \theta_{i+h} \sigma^{2}+\theta_{h} \sigma^{2} \\
& =\sigma^{2}\left[\sum_{i=1}^{9-h} \theta_{i} \theta_{i+h}+\theta_{n}\right]
\end{aligned}
$$

Thus in summary the moments or $M A(G)$ are given by

$$
\begin{gathered}
E\left(x_{t}\right)=0 \\
E\left(x_{t}^{2}\right)=\sigma^{2}\left(\sum_{i=1}^{a} \theta_{i}^{2}+1\right) \\
E\left(x_{t} x_{t+h}\right)=\sigma^{2}\left[\sum_{i=1}^{q-h} \theta_{i} \theta_{i+h}+\theta_{h}\right]
\end{gathered}
$$

## MA(1) Example

A Mouing average model of order 1, MACIS is defined by

$$
x_{t}=\varepsilon_{t}+\theta \varepsilon_{t-1}
$$

The finst and second moments are given by

$$
\begin{aligned}
E\left(x_{t}\right) & =0 \\
E\left(x_{t}^{2}\right) & =\sigma^{2} \theta^{2} \\
E\left(x_{t} x_{t-h}\right) & =\left\{\begin{array}{cc}
\sigma^{2} \theta & n=1 \\
0 & n>1
\end{array}\right.
\end{aligned}
$$

(ARMA) Autoregressive Moving Average Model

As the name suggest the ARMA(q) model combines the AR(q) and $M A(G)$. It was prerioush/ shown that $A R(1)$ and $M A(t)$ are related if the coefficients of the MA process are given by

$$
\theta_{i}=\varphi^{i}
$$

To furthure explore the relationship between the two processes and to define ARMA(q) the las operatior will be discussed

## las operators

The lag operator is defined by

$$
\begin{aligned}
L X_{t} & =X_{t-1} \\
L^{2} X_{t} & =X_{t-2} \\
\vdots & \\
L^{n} X_{t} & =X_{t-n}
\end{aligned}
$$

where $n=1,2,3, \ldots$ and $t$ is assumed to have the distributive property

$$
L\left(x_{t}+y_{t}\right)=x_{t-1}+y_{t-1}
$$

Recall that $A R(q)$ is defined by

$$
x_{t}=\sum_{i=1}^{P} \varphi_{i} x_{t-i}+\varepsilon_{t}
$$

so AR(1) is given by

$$
x_{t}=\varphi_{1} x_{t-1}+\varepsilon_{t}
$$

Using the las operator $A B(1)$ can be written as

$$
\begin{aligned}
\varepsilon_{t} & =x_{t}-\phi_{1} x_{t-1} \\
& =\left(1-\phi_{1} L\right) x_{t}
\end{aligned}
$$

similarly $A R(q)$ is given by

$$
\varepsilon_{t}=x_{t}-\varphi_{1} x_{t-1}-\varphi_{2} x_{t-2}-\cdots-\varphi_{q} x_{t-q}
$$

$$
=\left(1-\varphi_{1} L-\varphi_{2} L^{2}-\varphi_{3} L^{3} \cdots-\varphi_{q} L^{q}\right) x_{t}
$$

similarly the MA(a) can be written in terms of las operators. Recall that MA(q) is given by

$$
x_{t}=\sum_{i=1}^{q} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}
$$

so MACID is given by

$$
x_{t}=\theta \varepsilon_{t-1}+\varepsilon_{t}
$$

it follows that

$$
x_{t}=(1+\theta L) \varepsilon_{t}
$$

and similarly $M A(q)$ by

$$
\begin{aligned}
x_{t} & =\varepsilon_{t}+\theta_{1} \varepsilon_{t-1}+\theta_{2} \varepsilon_{t-2}+\cdots+\theta_{q} \varepsilon_{t-q} \\
& =\left(1+\theta_{1} L+\theta_{2} L^{2}+\cdots+\theta_{q} L^{q}\right) \varepsilon_{t-q}
\end{aligned}
$$

Let $\varphi_{0}=1$ and $\theta_{0}=1$ and define the lag polynomials by

$$
\begin{aligned}
& \varphi(L)=1-\Phi_{1} L-\Phi_{2} L^{2}-\Phi_{3} L^{3} \cdots \cdots \varphi_{9} L^{9} \\
& \theta(L)=1+\theta_{1} L+\theta_{2} L^{2}+\theta_{3} L^{3}+\cdots+\theta_{9} L^{9}
\end{aligned}
$$

It follows that
$A R(q): \varphi(L) X_{t}=\varepsilon_{t}$
$\operatorname{MACq}): \quad x_{t}=\theta(L) \varepsilon_{t}$
and the ARMA(q) process is defined by

$$
\phi(L) x_{t}=\theta(L) \varepsilon_{t}
$$

As and example ARMACD is given by

$$
\begin{array}{ll} 
& \left(1-\varphi_{1} L\right) x_{t}=\left(1+\theta_{1} L\right) \varepsilon_{t} \\
\Rightarrow \quad & x_{t}-\varphi_{1} x_{t-1}=\varepsilon_{t}+\theta_{1} \varepsilon_{t-1} \\
\Rightarrow \quad & x_{t}=\varphi_{1} x_{t-1}+\theta_{1} \varepsilon_{t-1}+\varepsilon_{t}
\end{array}
$$

## MA( $\infty$ )

Previously it was shown that that $A R(1)$ is related to $M A(t-1)$ if

$$
\theta_{i}=\varphi^{i}
$$

It is desirable to be able to convert between the models in general. This is because differet problems are more easily expressed in one model over the other. If $\varepsilon_{t}$ is unknown and $x_{t}$ is known then $A R(q)$ is preferable. If $\varepsilon_{t}$ is known MA(q) is preferable.
To derive a general method to convert between the processes or determine if the conoersion is possible start by reusiting AR(1) to MA(t-1) conversion. Previously it was shown that

$$
A R(1)-q^{t} x_{0}=M A(t-1)
$$

It will be shown that for $t \rightarrow \infty$ the relation becomes exact

$$
A R(1)=M A(\infty)
$$

where $M A(\infty)$ is given by,

$$
x_{t}=\theta(L) \varepsilon_{t}=\sum_{k=0}^{\infty}\left(\theta_{k} L^{k}\right) \varepsilon_{t}
$$

Eirst the condition for stationarity for $x_{t}$ imposed on the coefficients $\theta_{k}$ must be established. Previously it was shown that the oariance and couariance for $M A(q)$ are given by

$$
\begin{array}{r}
E\left(x_{t}^{2}\right)=\sigma^{2}\left(\sum_{i=1}^{9} \theta_{i}^{2}+1\right) \\
E\left(x_{t} x_{t+h}\right)=\sigma^{2}\left[\sum_{i=1}^{9} \theta_{i} \theta_{i+h}+\theta_{h}\right]
\end{array}
$$

using $\theta_{0}=1$ for $M(\infty)$ these expressions become

$$
\begin{aligned}
& E\left(x_{t}^{2}\right)=\sigma^{2} \sum_{i=0}^{\infty} \theta_{i}^{2} \\
& E\left(x_{t} x_{t+h}\right)=\sigma^{2} \sum_{i=0}^{\infty} \theta_{i} \theta_{i+h}
\end{aligned}
$$

Now for $E\left(X_{t}^{2}\right)$ to converge it must be that

$$
\sum_{i=0}^{\infty} \theta_{i}^{2}<\infty
$$

This condition is called square summable. A stricter constraint is typically used, absolute summability, namely

$$
\sum_{i=0}^{\infty}\left|\theta_{i}\right|<\infty
$$

It is easily seen that this constraint implies both $E\left(X_{t}^{2}\right)$ and $E\left(X_{t} X_{t+h}\right)$ are finite so that MA( $\infty$ ) is stationan/. For $E\left(x_{t}^{2}\right)$,

$$
\begin{aligned}
E\left(x_{t}^{2}\right) & =\sigma^{2} \sum_{i=0}^{\Delta} \theta_{l}^{2} \\
& =\sigma^{2} \sum_{i=0}^{\infty}\left|\theta_{i}\right|^{2} \\
& \leqslant \sigma^{2}\left(\sum_{i=0}\left|\theta_{i}\right|\right)^{2} \\
& <\infty
\end{aligned}
$$

and similarly consider

$$
\begin{aligned}
\sum_{n=0}^{\infty}\left|E\left(x_{t} x_{t+h}\right)\right| & =\sigma^{2} \sum_{h=0}^{\infty}\left|\sum_{i=0}^{\infty} \theta_{i} \theta_{i+h}\right| \\
& \leqslant \sigma^{2} \sum_{h=0}^{\infty} \sum_{i=0}^{\infty}\left|\theta_{i} \theta_{i+h}\right| \\
& =\sigma^{2} \sum_{i=0}^{\infty} \sum_{h=0}^{\infty}\left|\theta_{i} \theta_{i+h}\right| \\
& =\sigma^{2} \sum_{i=0}^{\infty}\left|\theta_{i}\right| \sum_{h=0}^{\infty}\left|\theta_{i+h}\right|
\end{aligned}
$$

Now since $i \geqslant 0$

$$
\sum_{n=0}^{\infty}\left|\theta_{i+h}\right| \leqslant \sum_{n=0}^{\infty}\left|\theta_{h}\right|
$$

thus

$$
\begin{aligned}
\sum_{n=0}^{\infty}\left|E\left(x_{t} x_{t+h}\right)\right| & \leqslant \sigma^{2} \sum_{i=0}^{\infty}\left|\theta_{i}\right| \sum_{n=0}^{\infty}\left|\theta_{n}\right| \\
& =\sigma^{2}\left(\sum_{i=0}^{\infty}\left|\theta_{1}\right|\right)^{2}
\end{aligned}
$$

* In summary, $M A(\infty)$ is stationory

$$
\sum_{i=0}^{\infty}\left|\theta_{i}\right|<\infty
$$

and the first and second moments are given by

$$
\begin{aligned}
\sigma_{\text {MAOD }}^{2} & =E\left(x_{t}^{2}\right)=\sigma^{2} \sum_{i=0}^{\alpha} \theta_{l}^{2} \\
r_{\text {MAOD }}(h) & =E\left(x_{t} x_{t+h}\right)=\sigma^{2} \sum_{i=0}^{\infty} \theta_{i} \theta_{i+h}
\end{aligned}
$$

Recall that $A R(1)$ is defined by

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

The process is stationary for $1 \varphi /<1$ with variance and oobariace given by

$$
\begin{aligned}
\sigma_{A R 1}^{2} & =\frac{\sigma^{2}}{1-\varphi^{2}} \\
\gamma_{A R 1}(n) & =\varphi^{n} \sigma_{A R 1}^{2}=\varphi^{n} \frac{\sigma^{2}}{1-\varphi^{2}}
\end{aligned}
$$

Now for $M A(\infty)$ let

$$
\theta_{i}=\varphi^{i}
$$

then

$$
\begin{aligned}
\sigma_{M A \alpha}^{2} & =\sigma^{2} \sum_{i=0}^{A} \theta_{i}^{2}=\sigma^{2} \sum_{i=0}^{\infty}\left(\phi^{2}\right)^{i} \\
& =\frac{\sigma^{2}}{1-\varphi^{2}}
\end{aligned}
$$

and

$$
\begin{aligned}
\gamma_{M A_{\infty}}(n) & =\sigma^{2} \sum_{i=0}^{\infty} \theta_{i} \theta_{i+h}=\sigma^{2} \sum_{i=0}^{\infty} \phi^{i} \phi^{i+h} \\
& =\sigma^{2} \sum_{i=0}^{\infty} \phi^{2 i+h} \\
& =\sigma^{2} \phi^{h} \sum_{i=0}^{\infty}\left(\phi^{2}\right)^{i} \\
& =\phi^{h} \frac{\sigma^{2}}{1-\phi^{2}}
\end{aligned}
$$

* Thus

$$
\begin{aligned}
& \sigma_{A R 1}^{2}=\sigma_{M A \infty}^{2} \\
& \gamma_{A R 1}(h)=\gamma_{M A O}(h)
\end{aligned}
$$

so $M A(\infty)$ is equivalent to $A R(1)$ in the limit $t \rightarrow \infty$.

## Transforming $A R(q)$ to $M A(p)$

In the previous section it was shown that for the limit $t \rightarrow \infty A R C D$ and $M A(\infty)$ are identical if

$$
\theta_{i}=\phi^{i}
$$

where $A R(1)$ is given by

$$
x_{t}=\phi x_{t-1}+\varepsilon_{t}
$$

and $M A(\infty)$ is given by

$$
x_{t}=\sum_{i=1}^{\infty} \theta_{i} \varepsilon_{t-i}+\varepsilon_{t}
$$

Now it was previously shown that AR(1) can be written using the shift operator, $L$, as

$$
\varepsilon_{t}=(1-\phi L) x_{t}
$$

if it is assumed that $(1-Q L)$ is invertable and denoted
by $(1-\varphi L)^{-1}$ so that

$$
(1-\varphi L)(1-\varphi L)^{-1}=1
$$

Then ARCD can be solved for $x_{t}$,

$$
\begin{aligned}
(1-\varphi L)^{-1} \varepsilon_{i} & =(1-\varphi L)^{-1}(1-\varphi L) x_{t} \\
& =x_{t}
\end{aligned}
$$

50

$$
x_{t}=(1-\varphi L)^{-1} \varepsilon_{t}
$$

Now what is $(1-\varphi L)^{-1}$. Recall that $M A(\infty)$ can be writen with shift operator, to obtain

$$
\begin{aligned}
x_{t} & =\theta(L) \varepsilon_{t} \\
& =\left(1+\theta_{1} L+\theta_{2} L^{2}+\theta_{3} L^{3}+\cdots\right) \varepsilon_{t} \\
& =\sum_{i=0}^{\infty}\left(\theta_{i} L^{i}\right) \varepsilon_{t}
\end{aligned}
$$

using
$\theta_{i}=\phi^{i}$
gives

$$
x_{t}=\sum_{c=0}^{\infty}\left(\phi^{i} L^{i}\right) \varepsilon_{t}
$$

It was shown that ARCD and $M A(\infty)$ are identical so a resonable guess is that

$$
(1-\phi L)^{-1}=\sum_{i=0}^{\infty} \phi^{i} L^{i}
$$

This guess can be verified by evaluating

$$
\begin{aligned}
& (1-\phi L) \sum_{i=0}^{\infty} \phi^{i} L^{i}=\sum_{i=0}^{\infty} \phi^{i} L^{i} \\
& -\phi L \sum_{i=0}^{\infty} \phi^{i} L^{i} \\
& =\sum_{i=0}^{\infty} \phi^{i} L^{i}-\sum_{i=0}^{\infty} \phi^{i+1} L^{i+1} \\
& =1+\sum_{i=1}^{\infty} \phi^{i} L^{i}-\sum_{i=1}^{\infty} \phi^{i} L^{i} \\
& =1
\end{aligned}
$$

Thus

$$
(1-\phi L)^{-1}=\sum_{i=0}^{\infty} \phi^{i} L^{i}
$$

and it follows that

$$
x_{t}=(1-\varphi L)^{-1} \varepsilon_{t}
$$

is $M A(\infty)$. Thus the two processes can be readily tra
into one another.
This result suggests a proceedure for for transforming between $A R(q)$ proccesses of arbitran order and the equvalent $M A(q)$ processes. An AR(q) process can be writen in terms of shift operators

$$
\begin{aligned}
\varepsilon_{t} & =\left(1-\varphi_{1} L-\varphi_{2} L^{2}-\cdots-\varphi_{q} L^{9}\right) x_{t} \\
& =\varphi(L) x_{t}
\end{aligned}
$$

Assume that the shift pshnomial can be factored

$$
\varphi(L)=\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right) \cdots\left(1-\lambda_{q} L\right)
$$

where $\lambda_{i}$ is the $i$ 'th root of the AR(g) shift polynomial.
It follows that

$$
\begin{aligned}
\varepsilon_{t} & =\varphi(L) x_{t} \\
& =\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right) \cdots\left(1-\lambda_{q} L\right) x_{t} \\
\Rightarrow x_{t} & =\left(1-\lambda_{q} L\right)^{-1} \cdots\left(1-\lambda_{2} L\right)^{-1}\left(1-\lambda_{1} L\right)^{-1} \varepsilon_{t}
\end{aligned}
$$

Thus if

$$
\begin{aligned}
& \theta_{1}(L)=\left(1-\lambda_{1} L\right)^{-1} \\
& \theta_{2}(L)=\left(1-\lambda_{2} L\right)^{-1} \\
& \vdots \\
& \theta_{q}(L)=\left(1-\lambda_{q} L\right)^{-1}
\end{aligned}
$$

then

$$
x_{t}=\theta_{1}(L) \theta_{2}(L) \cdots \theta_{q}(L) \varepsilon_{t}
$$

using the previous result obtaned for inverting ARCD it follows that

$$
\theta_{l}(L)=\left(1-\lambda_{i} L\right)^{-1}=\sum_{j=0}^{\infty} \lambda_{i}^{j} L^{j}
$$

For this expansion to converge it must be that

$$
\left|\lambda_{i}\right|<1
$$

To summarize the procceedure just described for converting an orbitrary order AR process to an MA process where

$$
\varepsilon_{t}=\Phi(L) x_{t}
$$

1) Factor the AR(q) shift polynomial to the form
$\varphi(L)=\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right) \cdots\left(1-\lambda_{q} L\right)$
where $\lambda_{1}, \lambda_{2}, \ldots, \lambda_{q}$ are the roots of $\phi(L)$
2) Compute for $i=1,2,3, \ldots 9$

$$
\theta_{i}(L)=\sum_{j=0}^{\infty} \lambda_{i}^{j} L^{j}
$$

3) Compute

$$
X_{t}=\theta_{1}(L) \theta_{2}(L) \cdots \theta_{q}(L) \varepsilon_{t}
$$

## AR(2) Example

As an example consider the AR(2) process

$$
\begin{aligned}
\varepsilon_{t} & =x_{t}-\phi_{1} x_{t-1}-\phi_{2} x_{t-2} \\
& =\left(1-\phi_{1} L-\phi_{2} L^{2}\right) x_{t}
\end{aligned}
$$

Now

$$
\begin{aligned}
\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right) & =1-\lambda_{1} L-\lambda_{2} L+\lambda_{1} \lambda_{2} L^{2} \\
& =1-\left(\lambda_{1}+\lambda_{2}\right) L+\lambda_{1} \lambda_{2} L^{2}
\end{aligned}
$$

comparing terms gives

$$
\begin{aligned}
& \frac{\Phi_{1}=\lambda_{1}+\lambda_{2}}{\Phi_{2}=\lambda_{1} \lambda_{2}} \\
\Rightarrow \quad & \lambda_{1}=\Phi_{1}-\lambda_{2} \\
& \Phi_{2}=\lambda_{2}\left(\Phi_{1}-\lambda_{2}\right) \\
\Rightarrow & \lambda_{2}^{2}-\lambda_{2} \Phi_{1}+\Phi_{2}=0 \\
\Rightarrow & \lambda_{2}^{2}-\lambda_{2} \Phi_{1}+\Phi_{2}-\frac{1}{4} \Phi_{1}^{2}+\frac{1}{4} \Phi_{1}=0
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \lambda_{2}^{2}-\lambda_{2} \varphi_{1}+\frac{1}{4} \varphi_{1}^{2}=\frac{1}{4} \varphi_{1}^{2}-\varphi_{2} \\
& \Rightarrow\left(\lambda_{2}-\frac{1}{2} \varphi_{1}\right)^{2}=\frac{1}{4} \varphi_{1}^{2}-\varphi_{2} \\
& \Rightarrow \lambda_{2}=\frac{1}{2} \varphi_{1} \pm \sqrt{\frac{1}{4} \varphi_{1}^{2}-\varphi_{2}}
\end{aligned}
$$

so

$$
\begin{aligned}
& \lambda_{2}=\frac{1}{2} \Phi_{1} \pm \sqrt{\frac{1}{4}\left(\Phi_{1}^{2}-\Phi_{2}\right.} \\
& \lambda_{1}=\frac{\Phi_{2}}{\lambda_{2}}
\end{aligned}
$$

Now

$$
\begin{aligned}
& \varepsilon_{t}=\varphi(L) x_{t}=\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right) x_{t} \\
\Rightarrow & x_{t}=\left(1-\lambda_{1} L\right)^{-1}\left(1-\lambda_{2} L\right)^{-1} \varepsilon_{t}
\end{aligned}
$$

consider the factorization

$$
\left(1-\lambda_{1} L\right)^{-1}\left(1-\lambda_{2} L\right)^{-1}=\frac{1}{\left(1-\lambda_{2} L\right)\left(1-\lambda_{2} L\right)}
$$

$$
\begin{aligned}
& =\frac{C_{1}}{\left(1-\lambda_{1} L\right)}+\frac{C_{2}}{\left(1-\lambda_{2} L\right)} \\
& =\frac{C_{1}\left(1-\lambda_{2} L\right)+C_{2}\left(1-\lambda_{1} L\right)}{\left(1-\lambda_{1} L\right)\left(1-\lambda_{2} L\right)}
\end{aligned}
$$

To solve this equation it must be that

$$
\begin{array}{r}
C_{1}\left(1-\lambda_{2} L\right)+C_{2}\left(1-\lambda_{1} L\right)=1 \\
\Rightarrow \quad C_{1}+C_{2}-\left(C_{1} \lambda_{2}+C_{2} \lambda_{1}\right) L=1
\end{array}
$$

50

$$
\begin{aligned}
& c_{1}+c_{2}=1 \\
& c_{1} \lambda_{2}+c_{2} \lambda_{1}=0
\end{aligned}
$$

soluch the finst equation for $c_{1}$ and substituting into equation 2 gives

$$
\begin{array}{r}
c_{1}=1-c_{2} \\
\Rightarrow\left(1-c_{2}\right) \lambda_{2}+c_{2} \lambda_{1}=0
\end{array}
$$

$$
\begin{aligned}
\Rightarrow \lambda_{2}-c_{2}\left(\lambda_{2}-\lambda_{1}\right)=0 & \\
\Rightarrow c_{2} & =\frac{\lambda_{2}}{\lambda_{2}-\lambda_{1}} \\
c_{1} & =1-\frac{\lambda_{2}}{\lambda_{2}-\lambda_{1}}=-\frac{\lambda_{1}}{\lambda_{2}-\lambda_{1}} \\
& =\frac{\lambda_{1}}{\lambda_{1}-\lambda_{2}}
\end{aligned}
$$

thus

$$
c_{1}=\frac{\lambda_{1}}{\lambda_{1}-\lambda_{2}} \quad c_{2}=\frac{\lambda_{2}}{\lambda_{2}-\lambda_{1}}
$$

It follows that

$$
\begin{aligned}
x_{t}= & \left(1-\lambda_{1} L\right)^{-1}\left(1-\lambda_{2} L\right)^{-1} \varepsilon_{t} \\
& {\left[\frac{C_{1}}{\left(1-\lambda_{1} L\right)}+\frac{C_{2}}{\left(1-\lambda_{2} L\right)}\right] \varepsilon_{t} }
\end{aligned}
$$

and finally expanding the inverse shift polynomials gives

$$
\begin{aligned}
& \left(1-\lambda_{1} L\right)^{-1}=\sum_{i=0}^{\infty} \lambda_{1}^{i} L^{i} \\
& \left(1-\lambda_{2} L\right)^{-1}=\sum_{i=0}^{\infty} \lambda_{2}^{i} L^{i}
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
X_{t} & =\left[\sum_{i=0}^{\infty} C_{1} \lambda_{1}^{i} L^{i}+\sum_{i=0}^{\infty} C_{2} \lambda_{2}^{i} L^{i}\right] \varepsilon_{t} \\
& =\sum_{i=0}^{\infty}\left(C_{1} \lambda_{1}^{i}+C_{2} \lambda_{2}^{i}\right) L^{i} \varepsilon_{t} \\
& =\sum_{l=0}^{\infty}\left(C_{1} \lambda_{1}^{i}+C_{2} \lambda_{2}^{i}\right) \varepsilon_{t-i}
\end{aligned}
$$

Let

$$
\psi_{i}=c_{1} \lambda_{1}^{i}+c_{2} \lambda_{2}^{i}
$$

*In summary the following rescut was obtained, Consider the AR(2) process defined by

$$
\varepsilon_{t}=\left[1-\left(\lambda_{1}+\lambda_{2}\right) L+\lambda_{1} \lambda_{2} L^{2}\right] x_{t}
$$

where $\left|\lambda_{1}\right|<1$ and $\left|\lambda_{2}\right|<1$. It has been shown that the inverse MA( $\infty$ ) process is given by

$$
x_{t}=\sum_{i=0}^{\infty}\left(c_{1} \lambda_{1}^{i}+c_{2} \lambda_{2}^{i}\right) \varepsilon_{t-i}
$$

where

$$
c_{1}=\frac{\lambda_{1}}{\lambda_{1}-\lambda_{2}} \quad c_{2}=\frac{\lambda_{2}}{\lambda_{2}-\lambda_{1}}
$$

## AR(1) Simulations

The ARCD random process is defined by

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

where $\varepsilon_{t}$ are independent identically distributed random oariables with

$$
\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

thus

$$
\begin{aligned}
& E\left(\varepsilon_{t}\right)=0 \\
& E\left(\varepsilon_{t}^{2}\right)=\sigma^{2} \\
& E\left(\varepsilon_{t} \varepsilon_{s}\right)=\sigma^{2} \delta_{t s}
\end{aligned}
$$

It can be shown that in the limit $t \rightarrow \infty$ with $|\varphi|<1$

$$
\lim _{t \rightarrow \infty} E\left(x_{t}\right)=0
$$

$$
\begin{gathered}
\lim _{t \rightarrow \infty} \operatorname{var}\left(x_{t}\right)=\frac{\sigma^{2}}{1-\varphi^{2}} \\
\lim _{t \rightarrow \infty} \operatorname{cov}\left(x_{t} x_{t+n}\right)=\varphi^{n} \sigma^{2}
\end{gathered}
$$

where $n \geqslant 0$.
Now AR(1) is related to MA( $\infty$ ). To see this consider

$$
x_{t}=(1-\varphi L)^{-1} \varepsilon_{t}
$$

where $L$ is the shift operator. In the limit $t \rightarrow \infty$ it can be shown that for $|q|<1$.

$$
(1-\phi L)^{-1}=\sum_{i=0}^{\infty} \phi^{i} L^{i}
$$

so that

$$
x_{t}=\sum_{i=0}^{\infty} \phi^{i} L^{i} \varepsilon_{t}
$$

which is MA( $\infty$ ).
The following series of plots show example realizations of AR(1)
for $6=1$ and a range of values of $|\varphi|<1$. The first panel shows positive values and the second negative values.

AR(1) Series Comparison: $\sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-050.jpg?height=340&width=1308&top_left_y=910&top_left_x=122)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-050.jpg?height=200&width=1301&top_left_y=1247&top_left_x=124)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-050.jpg?height=347&width=1323&top_left_y=1471&top_left_x=122)

AR(1) Series Comparison: $\sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-051.jpg?height=930&width=1321&top_left_y=245&top_left_x=124)

It will be seen in later plots that convergence and value of the first and second moments is indepent of the sign of $\varphi$ but the character of the result is very different. For $\varphi<0$ negative autocorrelation causes rapid changes in direction of $x_{t}$

In the following plots the autocorrelation coefficient

$$
v_{\tau}=\frac{\operatorname{cov}\left(x_{t} x_{t+\tau}\right)}{\sigma^{2}}=\varphi^{\top}
$$

is compared with simulations with positive and negative $\varphi$. clearly if $\varphi<0 \quad r_{\tau}$ will ocsiliate in sign. For 个 even it will positure and for $\uparrow$ odd it will be negative. This ocsillation of the sign of $r_{r}$ leads to the very different charater of the time series realization. The first plots compare $\gamma_{\uparrow}$ for $\varphi= \pm 0.5$

AR(1) Cumulative Autocorrelation: $\sigma=1.0, \varphi=0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-052.jpg?height=589&width=924&top_left_y=1374&top_left_x=358)

$\operatorname{AR}(1)$ Cumulative Autocorrelation: $\sigma=1.0, \varphi=-0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-053.jpg?height=605&width=961&top_left_y=179&top_left_x=388)

The agreement between $\gamma_{\tau}=\varphi^{\top}$ and similation results is good. In the next plots $\varphi= \pm 0.9$ are compare the decay of $\gamma_{\tau}$ is much slower leading to a more prononunce effect.

AR(1) Cumulative Autocorrelation: $\sigma=1.0, \varphi=0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-053.jpg?height=593&width=906&top_left_y=1370&top_left_x=356)

$\mathrm{AR}(1)$ Cumulative Autocorrelation: $\sigma=1.0, \varphi=-0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-054.jpg?height=598&width=940&top_left_y=203&top_left_x=372)

The next series of pots illustrate convergence of the first and second momements to the equillibrium values. Within $10^{3}$ to $10^{4}$ steps the simulation results are dose to the equillibrium values
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-054.jpg?height=598&width=882&top_left_y=1390&top_left_x=356)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-055.jpg?height=625&width=918&top_left_y=137&top_left_x=348)

## The convergence is slower for larger $\phi$ as seen in the following plots

AR(1) Cumulative Mean: $\sigma=1.0, \varphi=0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-055.jpg?height=637&width=1023&top_left_y=1195&top_left_x=312)

$\mathrm{AR}(1)$ Cumulative Variance: $\sigma=1.0, \varphi=0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-056.jpg?height=634&width=1011&top_left_y=261&top_left_x=314)

The following plot illustrates convergence for $\varphi<0$. When compared with the $\varphi>0$ simulation the convergence appears more rapid.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-056.jpg?height=591&width=872&top_left_y=1366&top_left_x=356)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-057.jpg?height=617&width=916&top_left_y=147&top_left_x=386)

Finally to illustrate the sensitivly of convergence to equilibrioum corcund $|q|=1$ consider the following two simulations
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-057.jpg?height=733&width=980&top_left_y=1166&top_left_x=308)

## Parameter Estimation

Given a Inear model with some number of unknown parameters and a time series to be modled a method is neeled to deduce the value of the parameters from analyss of the time series and also the accuracy of the estimate. In this section several methods will be revewed that perform this task. The first examined will be the method called Simple Linear Regression (SLR). Estumates of linear model parameters are ontained withe error estimates. Next ordinary Least squares (OUS) is discussed. OLS extends SLR it multivariable linear models. Next the Classical Linear Model (CLM) is discussed. As an example SLR is used to estimate the AR(1) parameter.

Next the Maximum Likelihod method of parameter estimation is discussed and it is shown that for AR(1) the Maximum Likelihood estimate is equivalent to the SLR estimate. Finally the method of moments parameter estimation method is reviewed.
The final section of this write up reviews and provides examples of parameter estimation methods.

## Simple Lnear Regression (SLR)

Consider the data shown below
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-060.jpg?height=745&width=1035&top_left_y=358&top_left_x=261)

Let $x$ and $y$ denote the observation vectors of length, $n$

$$
\begin{aligned}
& x=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\} \\
& y=\left\{y_{1}, y_{1}, y_{3}, \ldots, y_{n}\right\}
\end{aligned}
$$

Here the red line is defined by

$$
\alpha+\beta x_{i}
$$

The measurements of $y_{i}$ for each $x_{i}$ are indicated by the green dots and the resistual for
each measurement, $\varepsilon_{i}$, is the difference between the measurement and $\alpha+\beta x_{i}$. It follows that

$$
\varepsilon_{i}=y_{i}-\alpha-\beta x_{i}
$$

If it is assumed that $E\left(\varepsilon_{i}\right)=0$ then

$$
E\left(y_{i}\right)=\alpha+E\left(\beta x_{i}\right)
$$

The problem that needs to be solved is given $n$ measurements $y_{i}$ and the variable values $x_{i}$ what are the estimated values of $\alpha$ and $\beta$ that minimiz the sum of the squares of the residuals,

$$
E=\sum_{i=1}^{n} \varepsilon_{i}^{2}=\sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right)^{2}
$$

This is accomplished by evaluating the $\alpha$ and $\beta$ that satisfy,

$$
\left.\frac{\partial E}{\partial \alpha}\right|_{\alpha=\hat{\alpha}}=\left.0 \quad \frac{\partial E}{\partial \beta}\right|_{\beta=\hat{\beta}}=0
$$

where $\hat{\alpha}$ and $\hat{\beta}$ are are the estimates of $\alpha$ and $\beta$ repectively obtame by evaluation of the two equations above.

It follows that,

$$
\begin{aligned}
\frac{\partial E}{\partial \alpha} & =\frac{\partial}{\partial \alpha} \sum_{i=1}^{n} \varepsilon_{i}^{2} \\
& =\frac{\partial}{\partial \alpha} \sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right)^{2} \\
& =\sum_{i=1}^{n} \frac{\partial\left(y_{i}-\alpha-\beta x_{i}\right)^{2}}{\partial \alpha} \\
& =\sum_{i=1}^{n}-2\left(y_{i}-\alpha-\beta x_{i}\right) \\
& =-2 \sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right) \\
& =2 n \alpha-2 \sum_{i=1}^{n}\left(y_{i}-\beta x_{i}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
\frac{\partial E}{\partial \beta} & =\frac{\partial}{\partial \beta} \sum_{i=1}^{n} \varepsilon_{i}^{2} \\
& =\frac{\partial}{\partial \beta} \sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right)^{2} \\
& =\sum_{i=1}^{n} \frac{\partial}{\partial \beta}\left(y_{i}-\alpha-\beta x_{i}\right)^{2} \\
& =\sum_{i=1}^{n}-2 x_{i}\left(y_{i}-\alpha-\beta x_{i}\right)
\end{aligned}
$$

Now for the first equation

$$
\begin{aligned}
\left.\frac{\partial E}{\partial \alpha}\right|_{\alpha=\hat{\alpha}} & =0 \\
& =2 n \hat{\alpha}-2 \sum_{i=1}^{n}\left(y_{i}-\hat{\beta} x_{i}\right) \\
\Rightarrow \hat{\alpha} & =\frac{1}{n} \sum_{i=1}^{n} y_{i}-\frac{\hat{\beta}}{n} \sum_{i=1}^{n} x_{i}
\end{aligned}
$$

denote the averages of $y_{i}$ and $x_{i}$ by

$$
\bar{y}=\frac{1}{n} \sum_{i=1}^{n} y_{i}
$$

$$
\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

50

$$
\hat{\alpha}=\bar{y}-\hat{\beta} \bar{x}
$$

and
$\left.\frac{\partial E}{\partial \beta}\right|_{\beta=\hat{\beta}}=0$

$$
=\sum_{i=1}^{n}-2 x_{i}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right)
$$

$=\sum_{i=1}^{n} x_{i} \hat{y}_{i}-\hat{\alpha} \sum_{i=1}^{n} x_{i}-\hat{\beta} \sum_{i=1}^{n} x_{i}^{2}$
$\Rightarrow \hat{\beta} \sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} x_{i} y_{i}-\hat{\alpha} \sum_{i=1}^{n} x_{i}$
Now previously it was shown that

$$
\hat{\alpha}=\bar{y}-\hat{\beta} \bar{x}
$$

and using

$$
\sum_{i=1}^{n} x_{i}=n \bar{x}
$$

gives
$\hat{\beta} \sum_{i=1}^{n} x_{i}^{2}=\sum_{i=1}^{n} x_{i} y_{i}-(\bar{y}-\beta \bar{x}) n \bar{x}$

$$
\begin{aligned}
\Rightarrow \hat{\beta}\left[\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}-\bar{x}^{2}\right] & \\
& =\frac{1}{n} \sum_{i=1}^{n} x_{i} y_{i}-\bar{x} \bar{y}
\end{aligned}
$$

Now

$$
\begin{aligned}
\operatorname{Var} & (x)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \\
= & \frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}-\frac{2 \bar{x}}{n} \sum_{i=1}^{n} x_{i}+\bar{x}^{2} \\
= & \frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}-2 \bar{x}^{2}+\bar{x}^{2} \\
= & \frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}-\bar{x}^{2}
\end{aligned}
$$

and

$$
\begin{aligned}
& \operatorname{Cov}(x y)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right) \\
& =\frac{1}{n} \sum_{i=1}^{n} x_{i} y_{i}-\frac{1}{n} \bar{y} \sum_{i=1}^{n} x_{i}-\frac{1}{n} \bar{x} \sum_{i=1}^{n} \hat{y}_{i} \\
& \quad+\bar{x} \bar{y} \\
& =\frac{1}{n} \sum_{i=1}^{n} x_{i} y_{i}-\bar{x} \bar{y} \\
& \text { Thus } \\
& \quad \hat{\beta}\left[\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2}-\bar{x}^{2}\right] \\
& \quad=\frac{1}{n} \sum_{i=1}^{n} x_{i} y_{i}-\bar{x} \bar{y} \\
& \Rightarrow \hat{\beta} \operatorname{Var}(x)=\operatorname{Cov}(x y) \\
& \Rightarrow \hat{\beta}=\frac{\operatorname{Cov}(x, y)}{\operatorname{Var}(x)}
\end{aligned}
$$

Thus the ols estimate of $\alpha$ and $\beta$ are given by

$$
\begin{array}{r}
\bar{y}=\frac{1}{n} \sum_{i=1}^{n} y_{i} \quad \bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
\hat{\alpha}=\bar{y}-\hat{\beta} \bar{x} \\
\hat{\beta}=\frac{\operatorname{cov}(x, y)}{\operatorname{var}(x)}
\end{array}
$$

$$
\begin{aligned}
& \operatorname{var}(x)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \\
& \operatorname{rov}(x y)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(\hat{y}_{i}-\bar{y}\right)
\end{aligned}
$$

## unbiaseness of SLR

In the previous section it was shown that for,

$$
\varepsilon_{i}=y_{i}-\alpha-\beta x_{i}
$$

where $x$ and $y$ are random vectors of length, $n$, and

$$
E\left(\varepsilon_{i}\right)=0
$$

For given $x$ and $y$ the values of $\alpha$ and $\beta$ that minimize

$$
\sum_{i=1}^{n} \varepsilon_{c}^{2}
$$

are the estimated values which are denoted by, $\hat{\alpha}$ and $\hat{\beta}$, and given by

$$
\begin{aligned}
& \hat{\alpha}=\bar{y}-\hat{\beta} \bar{x} \\
& \hat{\beta}=\frac{\operatorname{cov}(x, y)}{\operatorname{var}(x)}
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{Var}(x)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \\
& \operatorname{Cov}(x y)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right) \\
& \bar{y}=\frac{1}{n} \sum_{i=1}^{n} y_{i} \quad \bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
\end{aligned}
$$

Here it will be shown that the estimates $\hat{\alpha}$ and $\hat{\beta}$ are unbrased. unbiased means,

$$
\begin{aligned}
& E(\hat{\alpha})=\alpha \\
& E(\hat{\beta})=\beta
\end{aligned}
$$

A property that will be useful later and that foltows from the assumption that $E\left(\varepsilon_{i}\right)=0$ and additionally assuming that $\varepsilon_{i}$ and $x_{i}$ are independent is

$$
E\left(\varepsilon_{i} \mid x_{i}\right)=E\left(\varepsilon_{i}\right)=0
$$

Now

$$
\begin{aligned}
\hat{\beta} & =\frac{\operatorname{cov}(x, y)}{\operatorname{var}(x)}=\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
& =\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) y_{i}-\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \bar{y}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

Now consider the second term in the numerator

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \bar{y}=\bar{y} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \\
= & \bar{y}(n \bar{x}-n \bar{x})=0
\end{aligned}
$$

Also using $y_{i}=\alpha+\beta x_{i}+\varepsilon_{i}$ gives

$$
\hat{\beta}=\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) y_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
$$

$$
\begin{aligned}
& =\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(\alpha+\beta x_{i}+\varepsilon_{i}\right)}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
& =\frac{\alpha \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)+\beta \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) x_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
& +\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

Now consider the form

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) x_{i}=\sum_{i=1}^{n} x_{i}^{2}-\bar{x} \sum_{i=1}^{n} x_{i} \\
& =\sum_{i=1}^{n} x_{i}^{2}-n \bar{x}^{2} \\
& =\sum_{i=1}^{n}\left(x_{i}^{2}-\bar{x}^{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & \sum_{i=1}^{n}\left(x_{i}^{2}-2 \bar{x}^{2}+\bar{x}^{2}\right) \\
= & \sum_{i=1}^{n}\left(x_{i}-2 x_{i} \bar{x}+\bar{x}^{2}\right) \\
= & \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \\
\text { Continuin } S & \\
\hat{\beta}= & \beta \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) x_{i}+\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i} \\
= & \frac{\beta \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}+\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
= & \beta+\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

Now in computing expectations it is assumed the vector $x$ is given and is independent of $\varepsilon_{i}$ so that $E\left(\varepsilon_{i} \mid x_{i}\right)=E\left(\varepsilon_{i}\right)$. Also it is assumed that all of the variation in $\hat{\alpha}$ and $\hat{\beta}$ cones frow $\varepsilon_{i}$ so that

$$
\begin{aligned}
& E(\hat{\beta} \mid x)=E(\hat{\beta}) \\
& E(\hat{\alpha} \mid x)=E(\hat{\alpha})
\end{aligned}
$$

Taking expectations gives using these assumptions gives,

$$
\begin{aligned}
E(\hat{\beta}) & =E(\beta)+E\left[\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}\right] \\
& =\beta+\frac{\sum_{i=1}^{n} E\left[\left(x_{i}-\bar{x}\right) \varepsilon_{i}\right]}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

Consider the numerator of the second term

$$
\begin{aligned}
E\left[\left(x_{i}-\bar{x}\right) \varepsilon_{i}\right] & =E\left(x_{i} \varepsilon_{i}\right)-\bar{x} E\left(\varepsilon_{i}\right) \\
& =E\left(x_{i}\right) E\left(\varepsilon_{i}\right)-\bar{x} E\left(\varepsilon_{i}\right) \\
& =\left[E\left(x_{i}\right)-\bar{x}\right] E\left(\varepsilon_{i}\right) \\
& =0
\end{aligned}
$$

where the second step follows from the assumed independence of $x_{i}$ and $\varepsilon_{i}$ and the last step from the assumption that $E\left(\varepsilon_{i}\right)=0$. Thus the desired result is obtained and $\hat{\beta}$ is unbiased

$$
E(\hat{\beta})=\beta
$$

Finally recall that

$$
\begin{aligned}
\hat{\alpha} & =\bar{y}-\hat{\beta} \bar{x} \\
& =\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{\beta} x_{i}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{n} \sum_{i=1}^{n}\left(\alpha+\beta x_{i}-\hat{\beta} x_{i}\right) \\
& =\alpha+(\beta-\hat{\beta}) \bar{x}
\end{aligned}
$$

Thus

$$
\begin{aligned}
E(\hat{\alpha}) & =E[\alpha+(\beta-\hat{\beta}) \bar{x}] \\
& =E(\alpha)+\bar{x} E(\beta-\hat{\beta}) \\
& =\alpha
\end{aligned}
$$

and the desired result that bot $\hat{\beta}$ and $\hat{\alpha}$ are unbiased has been proven.

## Uariance and Error for SLR Estimates $\hat{\alpha}$ and $\hat{\beta}$

In the previous section tt was shown that estimate $\hat{\beta}$ is related to $\beta$ in the following manner

$$
\hat{\beta}=\beta+\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
$$

and that

$$
E(\hat{\beta})=\beta
$$

It will be assumed that

$$
\operatorname{var}\left(\varepsilon_{i}\right)=\sigma^{2}
$$

Additionally homoskedacity is assumed that is $\varepsilon_{i}$ and $x_{i}$ are independent so that

$$
\operatorname{Var}\left(\varepsilon_{i} \mid x_{i}\right)=\operatorname{Var}\left(\varepsilon_{i}\right)=\sigma^{2}
$$

is independent of $x$. The $\varepsilon_{i}$ will also assumed to be independent,

$$
E\left(\varepsilon_{i} \varepsilon_{i}\right)=\sigma^{2} \delta_{i j}
$$

When computing the variance of $\mathcal{A}$ and $\hat{\beta}$ the vector $x$ is assumed given so that all of the variance in 2 and $\hat{\beta}$ is due to $\varepsilon$,

$$
\begin{aligned}
& \operatorname{Var}(\hat{\alpha} \mid x)=\operatorname{Var}(\hat{\alpha}) \\
& \operatorname{Var}(\hat{\beta} \mid x)=\operatorname{Var}(\hat{\beta})
\end{aligned}
$$

Now, Consder

$$
\begin{aligned}
\operatorname{Var}(\hat{\beta}) & =E\left[(\hat{\beta}-\beta)^{2}\right] \\
& =E\left[\left\{\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}\right\}\right] \\
& =\frac{E\left[\left\{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}\right\}^{2}\right]}{\left[\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}\right]^{2}}
\end{aligned}
$$

Consider the numerator

$$
\begin{aligned}
E & {\left[\left\{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i} \xi^{2}\right]\right.} \\
& =E\left[\sum_{i=1}^{n} \sum_{j=1}^{n}\left(x_{i}-\bar{x}\right)\left(x_{j}-\bar{x}\right) \varepsilon_{i} \varepsilon_{j}\right] \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n}\left(x_{i}-\bar{x}\right)\left(x_{j}-\bar{x}\right) E\left(\varepsilon_{i} \varepsilon_{j}\right)
\end{aligned}
$$

Since $\varepsilon_{i}$ and $\varepsilon_{j}$ are independent

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=\sigma^{2} \delta_{i j}
$$

It follows that

$$
\begin{aligned}
E[\{ & \left.\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i} \xi^{2}\right] \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n}\left(x_{i}-\bar{x}\right)\left(x_{j}-\bar{x}\right) \sigma^{2} \delta_{i j} \\
& =\sigma^{2} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}
\end{aligned}
$$

Thus

$$
\operatorname{var}(\hat{\beta})=\frac{E\left[\left\{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right) \varepsilon_{i}\right\}^{2}\right]}{\left[\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}\right]^{2}}
$$

$$
\begin{aligned}
& =\frac{\sigma^{2} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}{\left[\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}\right]^{2}} \\
& =\frac{\sigma^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

Now for $\hat{\alpha}$, using

$$
\hat{\alpha}=\alpha+(\beta-\hat{\beta}) \bar{x}
$$

gives

$$
\begin{aligned}
\operatorname{Var}(\hat{\alpha}) & =E\left[(\alpha-\alpha)^{2}\right] \\
& =E\left[(\beta-\hat{\beta})^{2} \bar{x}^{2}\right] \\
& =\bar{x}^{2} E\left[(\beta-\hat{\beta})^{2}\right] \\
& =\bar{x}^{2} \operatorname{Var}(\hat{\beta}) \\
& =\frac{\bar{x}^{2} \sigma^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

In summary

$$
\begin{aligned}
& \operatorname{Var}(\hat{\beta})=\frac{\sigma^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} \\
& \operatorname{Var}(\hat{\alpha})=\frac{\bar{x}^{2} \sigma^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{aligned}
$$

The standard error in the estimates $\hat{\beta}$ and $\hat{\alpha}$ is defined by

$$
\begin{aligned}
& \operatorname{Err}(\hat{\beta})=\sqrt{\operatorname{var}(\hat{\beta})} \\
& \operatorname{Err}(\hat{\alpha})=\sqrt{\operatorname{var}(\hat{\alpha})}
\end{aligned}
$$

The often seen regression statistic $R^{2}$ quanitifies the fraction of the sample variation that is described by

$$
\hat{y}_{i}=\hat{\alpha}+\hat{\beta} x_{i}=y_{i}-\varepsilon_{i}
$$

namely

$$
R^{2}=\frac{\sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right)^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}
$$

low there are three differens sum of squares of interest,

1. Explained sum of squares (SSE)

$$
\text { SSE }=\sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right)^{2}
$$

2. Residual sum of squares (SSR)

$$
S S R=\sum_{i=1}^{n} \varepsilon_{i}^{2}
$$

3. The total sum of squares (SST)

$$
S S T=\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}
$$

It is seen that

$$
R^{2}=\frac{S S E}{S S T}
$$

Now using $\hat{y}_{i}+\varepsilon_{i}=y_{i}$

$$
\begin{aligned}
& S S T=\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2} \\
= & \sum_{i=1}\left(\hat{y}_{i}+\varepsilon_{i}-\bar{y}\right)^{2} \\
= & \sum_{i=1}^{n}\left(\hat{y}_{i}+\varepsilon_{i}\right)^{2}-2\left(\hat{y}_{i}+\varepsilon_{i}\right) \bar{y}+\bar{y}^{2} \\
= & \sum_{i=1}^{n}\left[\hat{y}_{i}^{2}+2 \hat{y}_{i} \varepsilon_{i}+\varepsilon_{i}^{2}-2 \hat{y}_{i} \bar{y}-2 \varepsilon_{i} \bar{y}\right. \\
& \left.+\bar{y}^{2}\right] \\
= & \sum_{i=1}^{n} \hat{y}_{i}^{2}-2 \hat{y}_{i} \bar{y}+\bar{y}^{2}+\sum_{i=1}^{n} \varepsilon_{i}^{2} \\
& +\sum_{i=1}^{n} 2 \hat{y}_{i} \varepsilon_{i}-2 \varepsilon_{i} \bar{y}
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right)^{2}+\sum_{i=1}^{n} \varepsilon_{i}^{2}+\sum_{i=1}^{n} 2\left(\hat{y}_{i}-\bar{y}\right) \varepsilon_{i} \\
& =S S E+S S R+\sum_{i=1}^{n} 2\left(\hat{y}_{i}-\bar{y}\right) \varepsilon_{i}
\end{aligned}
$$

If the last term is zero then

$$
S S T=S S E+S S R
$$

Consider the last term

$$
\begin{aligned}
2 & \sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right) \varepsilon_{i}=2 \sum_{i=1}^{n}(\hat{y} i-\bar{y})\left(y_{i}-\hat{y}\right) \\
= & 2 \sum_{i=1}^{n}\left(\hat{\alpha}+\hat{\beta} x_{i}-\bar{y}\right)\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) \\
= & 2 \sum_{i=1}^{n}(\hat{\alpha}-\bar{y})\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) \\
& +2 \hat{\beta} \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) x_{i} \\
= & 2(\hat{\alpha}-\hat{y}) \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) \\
& +2 \hat{\beta} \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) x_{i}
\end{aligned}
$$

now $\hat{\alpha}$ and $\hat{\beta}$ are the values of $\alpha$ and $\beta$ that minimize the residual sum of squares

$$
\sum_{i=1}^{n} \varepsilon_{c}^{2}=\sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right)^{2}
$$

50
$\frac{\partial}{\partial \alpha}\left(\sum_{i=1}^{n} \varepsilon_{i}^{2}\right)=-2 \sum_{i=1}^{n}\left(y_{i}-\alpha-\beta x_{i}\right)$
$\frac{\partial}{\partial \beta}\left(\sum_{i=1}^{n} \varepsilon_{i}^{2}\right)=-2 \sum_{i=0}^{n}\left(y_{i}-\alpha-\beta x_{i}\right) x_{i}$
Now $\hat{\alpha}$ and $\hat{\beta}$ are the solutions to the equations
$\left.\frac{\partial}{\partial \alpha}\left(\sum_{i=1}^{n} \varepsilon_{l}^{2}\right)\right|_{\alpha=\hat{2}}=0$

$$
\left.\frac{\partial}{\partial \beta}\left(\sum_{i=1}^{n} \varepsilon_{c}^{2}\right)\right|_{\beta=\hat{\beta}}=0
$$

Thus

$$
\begin{aligned}
& \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right)=0 \\
& \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) x_{i}=0
\end{aligned}
$$

and

$$
\begin{aligned}
& 2 \sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right) \varepsilon_{i}=0 \\
& \quad 2(\hat{\alpha}-\hat{y}) \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) \\
& \quad+2 \hat{\beta} \sum_{i=1}^{n}\left(y_{i}-\hat{\alpha}-\hat{\beta} x_{i}\right) x_{i} \\
& =0
\end{aligned}
$$

and Finally

$$
\begin{aligned}
S S T & =\sum_{i=1}^{n}\left(\hat{y}_{i}-\bar{y}\right)^{2}+\sum_{i=1}^{n} \varepsilon_{i}^{2} \\
& =S S E+S S R \\
\Rightarrow \quad S S T & =S S E+S S R \\
\Rightarrow S S E & =S S T-S S R
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& R^{2}=\frac{S S E}{S S T}=\frac{S S T}{S S T} \cdot \frac{S S R}{S S T} \\
= & 1-\frac{\sum_{i=1}^{n} \varepsilon_{i}^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}
\end{aligned}
$$

## Ordinary least squares (Ols)

A general multivariate regression model can be written as

$$
\begin{aligned}
y_{i} & =\beta_{0}+\beta_{1} x_{i_{1}}+\beta_{2} x_{i_{2}}+\cdots+\beta_{k} x_{i n}+\varepsilon_{i} \\
& =\sum_{j=0}^{k} \beta_{j} x_{i j}+\varepsilon_{i} \quad i=1,2,3, \ldots, n
\end{aligned}
$$

where $\beta$, are constants and $\varepsilon_{i}$ are the residuals and it is assumed that $x_{i 0}=1$. In matrix form
$\left[\begin{array}{c}y_{1} \\ y_{2} \\ y_{3} \\ \vdots \\ y_{n}\end{array}\right]=\left[\begin{array}{ccccc}1 & x_{11} & x_{12} & \cdots & x_{1 k} \\ 1 & x_{21} & x_{22} & \cdots & x_{2 k} \\ \vdots & \vdots & & & \\ 1 & x_{n 1} & x_{n 2} & \cdots & x_{n k}\end{array}\right]\left[\begin{array}{c}\beta_{0} \\ \beta_{1} \\ \vdots \\ \beta_{k}\end{array}\right]+\left[\begin{array}{c}\varepsilon_{1} \\ \varepsilon_{2} \\ \vdots \\ \varepsilon_{n}\end{array}\right]$
$\Rightarrow \bar{I}=\bar{X} \beta+\varepsilon$
where $\Psi$ and $\varepsilon$ are column vectors of length $n$ and $\beta$
is a column vector of length $k$ and $\bar{X}$ is a $n \times k$ matrix.
Following the proceedure used for a single variable, the regression coefficients $\beta$ are determined by minimizing the sum of squares of the residual,

$$
\varepsilon^{\top} \varepsilon
$$

using

$$
\varepsilon=I-\bar{x} \beta
$$

gives

$$
\begin{aligned}
\varepsilon^{\top} \varepsilon & =(\bar{Y}-\bar{X} \beta)^{\top}(\bar{Y}-\bar{X} \beta) \\
& =\left(Z^{\top}-\beta^{\top} \bar{X}^{\top}\right)(\bar{Y}-\bar{X} \beta) \\
& =I^{\top} \bar{Y}-\beta^{\top} \bar{X}^{\top} \bar{Y}-I^{\top} \bar{X} \beta+\beta^{\top} \bar{X}^{\top} \bar{X} \beta
\end{aligned}
$$

Now

$$
\left(\varepsilon^{\top} \varepsilon\right)^{\top}=\varepsilon^{\top} \varepsilon
$$

It follows that

$$
\beta^{\top} \bar{X}^{\top} I=\left(\beta^{\top} \bar{X}^{\top} I\right)^{\top}=I^{\top} \underline{X} \beta
$$

thus

$$
\varepsilon^{\top} \varepsilon=\underline{I}^{\top} \bar{Y}-2 \beta^{\top} \underline{X}^{\top} \underline{Y}+\beta^{\top} \underline{X}^{\top} \bar{X} \beta
$$

using the Enstein scommation convention, to facilitale differentiation, gives

$$
\varepsilon_{i} \varepsilon_{i}=y_{i} y_{i}-2 \beta_{j} x_{j i} y_{i}+\beta_{j} x_{j i} x_{i j} \beta_{j}
$$

differentiating with respect to $\beta_{j}$ gives

$$
\frac{\partial}{\partial \beta_{j}}\left(\varepsilon_{i} \varepsilon_{i}\right)=\frac{\partial}{\partial \beta_{j}}\left[y_{i} y_{i}-2 \beta_{j} x_{j i} y_{i}\right.
$$

$=-2 x_{j i} y_{i}+2 x_{j i} x_{i j} \beta_{j}$
The estimate of $\beta_{j}$ will be denoted by $\hat{\beta}_{j}$ so

$$
\left.\frac{\partial}{\partial \beta_{j}}\left(\varepsilon_{i} \varepsilon_{i}\right)\right|_{\beta_{j}=\hat{\beta}_{j}}=0
$$

$\Rightarrow x_{j i} x_{i j} \hat{\beta}_{j}=x_{j i} y_{i}$
going back to matrix notation

$$
\begin{aligned}
& \underline{X}^{\top} \bar{X} \hat{\beta}=\bar{X}^{\top} \underline{Y} \\
\Rightarrow & \hat{\beta}=\left(\bar{X}^{\top} \bar{X}\right)^{-1} \underline{X}^{\top} \underline{Y}
\end{aligned}
$$

This expression for $\hat{\beta}$ is called the ordinary least squares estimator

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} Z^{\top} I
$$

This expression is equivalent to the system of equations

$$
\begin{gathered}
\bar{x}^{\top} I-\bar{x}^{\top} \bar{x} \hat{\beta}=0 \\
\Rightarrow \bar{x}^{\top}(I-\bar{x} \hat{\beta})=0 \\
\Rightarrow\left[\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
x_{11} & x_{21} & \cdots & x_{n 1} \\
\vdots & & \ddots & \vdots \\
x_{1 k} & x_{2 k} & \cdots & x_{n k}
\end{array}\right]\left\{\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right]-\left[\begin{array}{l}
\sum_{i=1}^{k} \hat{\beta}_{i} x_{1 i} \\
\sum_{i=1}^{k} \hat{\beta}_{i} x_{2 i} \\
\sum_{i=1}^{k} \hat{\beta}_{i} x_{n i}
\end{array}\right]\right\}=0
\end{gathered}
$$

$\Rightarrow\left[\begin{array}{cccc}1 & 1 & \cdots & 1 \\ x_{11} & x_{21} & \cdots & x_{n 1} \\ \vdots & & \ddots & \vdots \\ x_{1 k} & x_{2 k} & \cdots & x_{n k}\end{array}\right]\left[\begin{array}{cc}y_{1} & -\sum_{i=1}^{k} \hat{\beta}_{i} x_{1 i} \\ y_{2} & -\sum_{i=1}^{k} \hat{\beta}_{i} x_{2 i} \\ \vdots & y_{n}\end{array}\right]=0$
Muttplying the first row of the lefthand side by the righthand side gives

$$
\sum_{j=1}^{n}\left(y_{j}-\sum_{i=1}^{k} \hat{\beta}_{i} x_{j i}\right)=0
$$

Doing the same for the second row gives

$$
\sum_{j=1}^{n} X_{j 1}\left(y_{j}-\sum_{i=1}^{k} \hat{B}_{i} X_{j i}\right)=0
$$

and for the $k$ 'th row

$$
\sum_{j=1}^{n} X_{j k}\left(Y_{j}-\sum_{i=1}^{k} \hat{B}_{i} X_{j k}\right)=0
$$

It follows that the as estimate of $\hat{\beta}$ is found by solving the system of $k+1$ linear equations

$$
\sum_{j=1}^{n}\left(y_{j}-\sum_{i=1}^{k} \hat{\beta}_{i} x_{j i}\right)=0
$$

and for $m=1,2,3, \ldots, k$

$$
\sum_{j=1}^{n} X_{j m}\left(y_{j}-\sum_{i=1}^{k} \hat{B}_{i} X_{j i}\right)=0
$$

## unbiasedness of as Estimate

unbiasedness of as means that the ous estimate, $\hat{B}$, has expectation

$$
E(\hat{\beta})=\beta
$$

To prove this donsider the as estimator

$$
\hat{\beta}=\left(\Sigma^{\top} \Sigma\right)^{-1} \Sigma^{\top} I
$$

as in the single variable case it is assumed that

$$
E(\varepsilon)=0
$$

and that $\varepsilon$ and $\Sigma$ are idependent so that

$$
E(\varepsilon \mid \nabla)=E(\varepsilon)=0
$$

It is also assumed the $\bar{X}$ is given so that it is not random.

Now

$$
\bar{Y}=\bar{X} \beta+\varepsilon
$$

so

$$
\begin{aligned}
\hat{\beta} & =\left(Z^{\top} Z\right)^{-1} \underline{X}^{\top} \underline{Y} \\
& =\left(Z^{\top} Z\right)^{-1} \underline{X}^{\top}(X \beta+\varepsilon) \\
& =\left(\underline{X}^{\top} \underline{X}\right)^{-1}\left(Z^{\top} X\right) \beta+\left(\bar{X}^{\top} X\right)^{-1} \underline{X}^{\top} \varepsilon \\
& =\beta+\left(Z^{\top} Z\right)^{-1} Z^{\top} \varepsilon
\end{aligned}
$$

Now

$$
\begin{aligned}
E(\hat{\beta}) & =E\left[\beta+\left(X^{\top} X\right)^{-1} X^{\top} \varepsilon\right] \\
& =E(\beta)+E\left[\left(X^{\top} X\right)^{-1} X^{\top} \varepsilon\right] \\
& =\beta+\left(X^{\top} X\right)^{-1} X^{\top} E(\varepsilon) \\
& =\beta
\end{aligned}
$$

Thus $\hat{\beta}$ is unbiased

## Variance and Error of ols Estimate

In evaluating the variance of the ors estimate the assumptons made for SLR estimate variance are also made. This is that

$$
\operatorname{var}(\varepsilon)=\sigma^{2}
$$

Additionally homoskedacity is assumed that is $\varepsilon$ and $X$ are independent so that

$$
\operatorname{Var}(\varepsilon \mid \nabla)=\operatorname{Var}(\varepsilon)=\sigma^{2}
$$

is independent of $X$. The elements of $\varepsilon$ will be assumed independent,

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=6 \delta_{i j}
$$

It follows that the covariace matrix is given by

$$
E\left(\varepsilon \varepsilon^{\top}\right) \equiv \sigma^{2} \mathbb{1}
$$

where II is the dentity matrix. It follows that

$$
\begin{aligned}
& \operatorname{var}(\hat{\beta})=\operatorname{var}\left[\beta+\left(X^{\top} Z\right)^{-1} Z^{\top} \varepsilon\right] \\
& =E\left[(\hat{\beta}-\beta)(\hat{\beta}-\beta)^{\top}\right] \\
& =E\left[\left(X^{\top} X\right)^{-1} X^{\top} \varepsilon\left\{X^{\top} X\right)^{-1} X^{\top} \varepsilon \xi^{\top}\right] \\
& =E\left[\left(X^{\top} X\right)^{-1} X^{\top} \varepsilon \varepsilon^{\top} X\left\{\left(X^{\top} X\right)^{-1} \xi^{\top}\right]\right. \\
& =E\left[\left(\bar{X}^{\top} X\right)^{-1} X^{\top} \varepsilon \varepsilon^{\top} X\left(X^{\top} X\right)^{-1}\right] \\
& =\left(X^{\top} X\right)^{-1} X^{\top} E\left(\varepsilon \varepsilon^{\top}\right) X\left(X^{\top} \bar{X}\right)^{-1} \\
& =\left(X^{\top} X\right)^{-1} X^{\top}\left(\delta^{2} \mathbb{I}\right) X\left(X^{\top} X\right)^{-1} \\
& =\sigma^{2}\left(X^{\top} \bar{X}\right)^{-1}\left(X^{\top} X\right)\left(X^{\top} X\right)^{-1} \\
& =\sigma^{2}\left(X^{\top} X\right)^{-1}
\end{aligned}
$$

Trus

$$
\operatorname{var}(\hat{\beta})=\sigma^{2}\left(\bar{X}^{\top} \bar{X}\right)^{-1}
$$

## OLS Example SLE

Previously it was shown that for the linear model

$$
\bar{Y}=x \beta+\varepsilon
$$

which consists of $n$ observations and a linear model of order the estimates of the linear coefficienls are given by

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} Z^{\top} I
$$

and

$$
\begin{gathered}
E(\hat{\beta})=\beta \\
\operatorname{Var}(\hat{\beta})=\sigma^{2}\left(\bar{X}^{\top} X\right)^{-1}
\end{gathered}
$$

Consider a first order model

$$
y_{i}=\beta_{0}+\beta_{1} x_{1 i}+\varepsilon_{i}
$$

In matrix form

$$
\begin{aligned}
& \bar{Y}=\bar{X} \beta+\varepsilon \\
\Rightarrow & {\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right]=\left[\begin{array}{cc}
1 & x_{11} \\
1 & x_{21} \\
\vdots & \vdots \\
1 & x_{n 1}
\end{array}\right]\left[\begin{array}{c}
\beta_{0} \\
\beta_{1}
\end{array}\right]+\left[\begin{array}{c}
\varepsilon_{1} \\
\varepsilon_{2} \\
\vdots \\
\varepsilon_{n}
\end{array}\right] }
\end{aligned}
$$

50

$$
\begin{aligned}
\bar{Y}=\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right] \quad \underline{X} & =\left[\begin{array}{cc}
1 & x_{11} \\
1 & x_{21} \\
\vdots & \vdots \\
1 & x_{n 1}
\end{array}\right] \quad \varepsilon=\left[\begin{array}{c}
\varepsilon_{1} \\
\varepsilon_{2} \\
\vdots \\
\varepsilon_{n}
\end{array}\right] \\
\beta & =\left[\begin{array}{c}
\beta_{0} \\
\beta_{1}
\end{array}\right]
\end{aligned}
$$

Now

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} Z^{\top} I
$$

Eualuating the terms gives

$$
\begin{aligned}
x^{\top} x & =\left[\begin{array}{llll}
1 & 1 & \cdots & 1 \\
x_{11} & x_{12} & \cdots & x_{1 n}
\end{array}\right]\left[\begin{array}{cc}
1 & x_{11} \\
1 & x_{12} \\
\vdots & \vdots \\
1 & x_{1 n}
\end{array}\right] \\
& =\left[\begin{array}{lll}
\sum_{i=1}^{n} 1 & \sum_{i=1}^{n} x_{1 i} \\
\sum_{i=1}^{n} x_{1 i} & \sum_{i=1}^{n} & x_{1 i}^{2}
\end{array}\right] \\
& =\left[\begin{array}{lll}
n & n \bar{x} & \\
n \bar{x} & \sum_{i=1}^{n} x_{1 i}^{2}
\end{array}\right]
\end{aligned}
$$

now

$$
\begin{aligned}
& \left(\bar{x}^{\top} \bar{\Delta}\right)^{-1}=\left[\begin{array}{cc}
n & n \bar{x} \\
n \bar{x} & \sum_{i=1}^{n} x_{i i}^{2}
\end{array}\right]^{-1} \\
= & \frac{1}{n \sum_{i=1}^{n} x_{1 i}^{2}-n \bar{x}^{2}}\left[\begin{array}{cc}
\sum_{i=1}^{n} x_{1 i}^{2} & -n \bar{x} \\
-n \bar{x} & n
\end{array}\right]
\end{aligned}
$$

$$
=\frac{1}{n \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)}\left[\begin{array}{cc}
\sum_{i=1}^{n} x_{1 i}^{2} & -n \bar{x} \\
-n \bar{x} & n
\end{array}\right]
$$

and

$$
\begin{aligned}
& \underline{X}^{\top} I=\left[\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
x_{11} & x_{12} & \cdots & x_{1 n}
\end{array}\right]\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right] \\
& =\left[\begin{array}{l}
\sum_{i=1}^{n} y_{i} \\
\sum_{i=1}^{n} y_{i} x_{1 i}
\end{array}\right]=\left[\begin{array}{c}
n \bar{y} \\
\sum_{i=1}^{n} y_{i} x_{1 i}
\end{array}\right]
\end{aligned}
$$

Thus

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} \Sigma^{\top} I=
$$

$$
\frac{1}{n \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)}\left[\begin{array}{cr}
\sum_{i=1}^{n} x_{1 i}^{2} & -n \bar{x} \\
-n \bar{x} & n
\end{array}\right]\left[\begin{array}{c}
n \bar{y} \\
\sum_{i=1}^{n} y_{i} x_{1 i}
\end{array}\right]
$$

$$
=\frac{1}{\sqrt{n} \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)}\left[\begin{array}{l}
n \bar{y} \sum_{i=1}^{n} x_{i i}^{2}-n \bar{x} \sum_{i=1}^{n} y_{i} x_{1 i} \\
-n^{2} \bar{x} \bar{y}+\bar{y} \sum_{i=1}^{n} y_{i} x_{1 i}
\end{array}\right]
$$

$$
=\frac{1}{\sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)}\left[\begin{array}{c}
\bar{y} \sum_{i=1}^{n} x_{1 i}^{2}-\bar{x} \sum_{i=1}^{n} y_{i} x_{1 i} \\
\sum_{i=1}^{n}\left(y_{i} x_{1 i}-\bar{x} \bar{y}\right)
\end{array}\right]
$$

Now consider the term

$$
\begin{aligned}
\bar{y} & \sum_{i=1}^{n} x_{1 i}^{2}-\bar{x} \sum_{i=1}^{n} y_{i} x_{1 i} \\
& =\bar{y} \sum_{i=1}^{n} x_{1 i}^{2}-n \bar{y} \bar{x}^{2}+n \bar{y} \bar{x}^{2}-\bar{x} \sum_{i=1}^{n} y_{i} x_{1 i}
\end{aligned}
$$

$$
=\bar{y} \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)-\bar{x} \sum_{i=1}^{n}\left(y_{i} x_{1 i}-\bar{y} \bar{x}\right)
$$

Putting things together
$\hat{\beta}=\left(Z^{\top} Z\right)^{-1} \Sigma^{\top} I=$
$=\frac{1}{\sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)}\left[\begin{array}{c}\bar{y} \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right)-\bar{x} \sum_{i=1}^{n}\left(y_{i} x-\bar{y} \bar{x}\right) \\ \sum_{i=1}^{n}\left(y_{i} x_{1 i}-\bar{x} \bar{y}\right)\end{array}\right]$
Now

$$
\begin{aligned}
& \operatorname{Var}(x)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{1 i}^{2}-\bar{x}^{2}\right) \\
& \operatorname{Cov}(x y)=\frac{1}{n} \sum_{i=1}^{n}\left(y_{i} x_{1 i}-\bar{x} \bar{y}\right)
\end{aligned}
$$

then

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} Z^{\top} \Psi
$$

$$
=\frac{1}{\operatorname{Var}(x)}\left[\begin{array}{c}
\bar{y} \operatorname{Var}(x)-\bar{x} \operatorname{Cov}(x y) \\
\operatorname{Cov}(x y)
\end{array}\right]
$$

thus

$$
\begin{aligned}
\hat{\beta}_{1} & =\frac{\operatorname{Cov}(x y)}{\operatorname{Var}(x)} \\
\hat{\beta}_{0} & =\bar{y}-\bar{x} \frac{\operatorname{Cov}(x y)}{\operatorname{Uar}(x)} \\
& =\bar{y}-\bar{x} \beta_{1}
\end{aligned}
$$

Thus

$$
\hat{\beta}_{0}=\bar{y}-\bar{x} \beta_{1} \quad \hat{\beta}_{1}=\frac{\operatorname{Cov}(x y)}{\operatorname{Uar}(x)}
$$

which is the same as obtained in the SLR example.

## Classical Linear Model CLM

Previously it was shown that for the linear model

$$
\bar{Y}=x \beta+\varepsilon
$$

which consists of $n$ observations and a linear model of order $k$ the estimates of the linear coefficienls are given by

$$
\hat{\beta}=\left(Z^{\top} Z\right)^{-1} Z^{\top} I
$$

and

$$
\begin{gathered}
E(\hat{\beta})=\beta \\
\operatorname{Var}(\hat{\beta})=\sigma^{2}\left(\bar{X}^{\top} X\right)^{-1}
\end{gathered}
$$

where homoskedastrity has been assumed for the ressiduls, $\varepsilon$,

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=6 \delta_{i j}
$$

To perform inference, mypothesis testing, on $\hat{\beta}$ the full distribution of $\beta$ must be known. Thus far only the assumption of homoskedacity has been made which assumes that the vesiduals are independent and indentically distributed normal random variables with zero mean and variance 0 . Additionally it has been assumed that the residuals, $\varepsilon$, and $\bar{X}$ are independent and known. This assumption was sufficient to derive the expressions for the mean and variance of $\hat{\beta}$ shown above.
The Classical Linear Model, furthur assumes that $\hat{\beta}$ is a Normal distribution with mean,

$$
\mu=\beta
$$

and covariance matrix

$$
\sigma^{2}\left(\bar{X}^{\top} X\right)^{-1}
$$

Thus $\hat{\beta}$ has the multivariate distribution

$$
\hat{\beta} \sim N\left[\beta, \sigma^{2}\left(\underline{x}^{\top} \underline{x}\right)^{-1}\right]
$$

This means that each element of $\hat{\beta}$, denoted by $\hat{\beta}_{k}$, is normally distributed,

$$
\hat{\beta}_{k} \sim N\left[\beta_{k}, \sigma^{2}\left(\bar{X}^{\top} \bar{X}\right)_{k k}^{-1}\right]
$$

where $\left(X^{\top} X\right)_{K K}^{-1}$ are the dagonal elements of $\left(X^{\top} X\right)^{-1}$. Let

$$
S_{K K}=\left(\bar{X}^{\top} \bar{X}\right)_{K K}^{-1}
$$

so that

$$
\hat{\beta}_{k} \sim N\left(\beta_{k}, \sigma^{2} S_{k k}\right)
$$

A unit normal distribution can be obtained with the
following transformation

$$
z_{k}=\frac{\hat{\beta}_{k}-\beta_{k}}{\sqrt{\sigma^{2} S_{k k}}}
$$

How ever $\delta^{2}$ is unknown and an estimate must be used. The unbrased estimator is given by

$$
s^{2}=\frac{\varepsilon^{\top} \varepsilon}{n-(k+1)}
$$

replacing $\sigma^{2}$ with $s^{2}$ gives

$$
t_{k}=\frac{\hat{\beta}_{k}-\beta_{k}}{\sqrt{s^{2} s_{k k}}}
$$

$t_{k}$ has a $t$-distribution with $n-k-1$ degrees of freedom. It has a $t$-distribution because it is the ratio of a variable with a standard normal distribution and a variable with a chi-squared
distribution. $\varepsilon^{\top} \varepsilon$ has a chi-squard distribution.
The standard error of $\hat{\beta}_{k}$ is given by

$$
S E\left(\beta_{k}\right)=\sqrt{S^{2} S_{k k}} .
$$

## Regression Through the Origin

Consider a linear model that passes through the origin

$$
\begin{aligned}
& y_{i}=\beta x_{i}+\varepsilon_{i} \\
\Rightarrow \quad & \varepsilon_{i}=y_{i}-\beta x_{i}
\end{aligned}
$$

The $S S R$ is given by

$$
\sum_{i=1}^{n} \varepsilon_{i}^{2}=\sum_{i=1}^{n}\left(y_{i}-\beta x_{i}\right)^{2}
$$

The estimated $\hat{\beta}$ is given by

$$
\left.\frac{\partial}{\partial \beta}\left(\sum_{i=1}^{n} \varepsilon_{i}^{2}\right)\right|_{\beta=\hat{\beta}}=0
$$

Thus

$$
\frac{\partial}{\partial \beta}\left(\sum_{i=1}^{n} \varepsilon_{i}^{2}\right)=\frac{\partial}{\partial \beta}\left\{\sum_{i=1}^{n}\left(y_{i}-\beta x_{i}\right)^{2}\right\}
$$

$$
=\sum_{i=1}^{n}-2 x_{i}\left(y_{i}-\beta x_{i}\right)
$$

50

$$
\begin{aligned}
& \left.\frac{\partial}{\partial \beta}\left(\sum_{i=1}^{n} \varepsilon_{i}^{2}\right)\right|_{\beta=\hat{\beta}}=0 \\
\Rightarrow & \sum_{i=1}^{n}-2 x_{i}\left(y_{i}-\hat{\beta} x_{i}\right)=0 \\
\Rightarrow & \sum_{i=1}^{n} x_{i} y_{i}=\hat{\beta} \sum_{i=1}^{n} x_{i}^{2} \\
\Rightarrow & \hat{\beta}=\frac{\sum_{i=1}^{n} x_{i} y_{i}}{\sum_{i=1}^{n} x_{i}^{2}}
\end{aligned}
$$

Recall that

$$
y_{i}=\beta x_{i}+\varepsilon_{i}
$$

50

$$
\begin{aligned}
\hat{\beta} & =\frac{\sum_{i=1}^{n} x_{i}\left(\beta x_{i}+\varepsilon_{i}\right)}{\sum_{i=1}^{n} x_{i}^{2}} \\
& =\frac{\beta \sum_{i=1}^{n} x_{i}^{2}+\sum_{i=1}^{n} x_{i} \varepsilon_{i}}{\sum_{i=1}^{n} x_{i}^{2}} \\
& =\beta+\frac{\sum_{i=1}^{n} x_{i} \varepsilon_{i}}{\sum_{i=1}^{n} x_{i}^{2}}
\end{aligned}
$$

Next show that $\hat{\beta}$ is unbiased. This is shown by proving

$$
E(\hat{\beta})=\beta
$$

Now

$$
E(\hat{\beta})=E\left[\beta+\frac{\sum_{i=1}^{n} x_{i} \varepsilon_{i}}{\sum_{i=1}^{n} x_{i}^{2}}\right]
$$

$$
=E(\beta)+\frac{1}{\sum_{i=1}^{n} x_{i}^{2}} \sum_{i=1}^{n} E\left(x_{i} \varepsilon_{i}\right)
$$

Recall that $x_{i}$ and $\varepsilon_{i}$ are independent

$$
E\left(x_{i} \varepsilon_{i}\right)=0
$$

thus

$$
E(\hat{\beta})=B
$$

so that $\hat{\beta}$ is unbiased. Next consider

$$
\begin{aligned}
& \operatorname{Var}(\hat{\beta})=E\left[(\hat{\beta}-E[\hat{\beta}])^{2}\right] \\
& =E\left[(\hat{\beta}-\beta)^{2}\right]
\end{aligned}
$$

using the previous result

$$
\hat{\beta}-\beta=\frac{\sum_{i=1}^{n} x_{i} \varepsilon_{i}}{\sum_{i=1}^{n} x_{i}^{2}}
$$

gives

$$
E\left[(\hat{\beta}-\beta)^{2}\right]=E\left[\left(\frac{\sum_{i=1}^{n} x_{i} \varepsilon_{i}}{\sum_{i=1}^{n} x_{i}^{2}}\right)^{2}\right]
$$

Now since $x_{i}$ is assumed given and indepenendent of $\varepsilon_{i}$

$$
E\left[(\hat{\beta}-\beta)^{2}\right]=\frac{1}{\left(\sum_{i=1}^{n} x_{i}^{2}\right)^{2}} E\left[\left(\sum_{i=1}^{n} x_{i} \varepsilon_{i}\right)^{2}\right]
$$

Consider

$$
\begin{aligned}
& E\left[\left(\sum_{i=1}^{n} x_{i} \varepsilon_{i}\right)^{2}\right]=E\left[\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j} \varepsilon_{i} \varepsilon_{j}\right] \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j} E\left(\varepsilon_{i} \varepsilon_{j}\right)
\end{aligned}
$$

using

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=\sigma^{2} \delta_{i j}
$$

then

$$
\begin{aligned}
& E\left[\left(\sum_{i=1}^{n} x_{i} \varepsilon_{i}\right)^{2}\right]=\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j} \sigma^{2} \delta_{i j} \\
& =\sigma^{2} \sum_{i=1}^{n} x_{i}^{2}
\end{aligned}
$$

Bringing things together gives the final result

$$
\begin{aligned}
\operatorname{Var}(\hat{\beta}) & =E\left[(\hat{\beta}-\beta)^{2}\right] \\
& =\frac{1}{\left(\sum_{i=1}^{n} x_{i}^{2}\right)^{2}} \sigma^{2} \sum_{i=1}^{n} x_{i}^{2} \\
& =\frac{6^{2}}{\sum_{i=1}^{n} x_{i}^{2}}
\end{aligned}
$$

Next consider the linear model of order K

$$
y_{i}=\sum_{j=1}^{K} \beta_{j} x_{i j}+\varepsilon_{i}
$$

let

$$
\begin{gathered}
y=\left[\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right] \quad \varepsilon=\left[\begin{array}{c}
\varepsilon_{1} \\
\varepsilon_{2} \\
\vdots \\
\varepsilon_{n}
\end{array}\right] \\
x=\left[\begin{array}{cccc}
x_{11} & x_{12} & \cdots & x_{1 k} \\
x_{21} & x_{22} & \cdots & x_{2 k} \\
\vdots & \vdots & \ddots & \vdots \\
x_{n 1} & x_{n 2} & x_{n k}
\end{array}\right] \quad \beta=\left[\begin{array}{c}
\beta_{1} \\
\beta_{2} \\
\vdots \\
\beta_{k}
\end{array}\right]
\end{gathered}
$$

Then the linear model becomes

$$
\begin{aligned}
y & =x \beta+\varepsilon \\
\Rightarrow \varepsilon & =y-x \beta
\end{aligned}
$$

The SSR is given by

$$
\begin{aligned}
\varepsilon^{\top} \varepsilon & =(y-x \beta)^{\top}(y-x \beta) \\
& =\left(y^{\top}-\beta^{\top} x^{\top} x y-x \beta\right)
\end{aligned}
$$

$$
=y^{\top} y-\beta^{\top} x^{\top} y-y^{\top} x \beta-\beta^{\top} x^{\top} x \beta
$$

Now since

$$
\left(\varepsilon^{\top} \varepsilon\right)^{\top}=\varepsilon^{\top} \varepsilon
$$

It follows that
$y^{T} x \beta=\left(y^{T} x \beta\right)^{T}=\beta^{T} x^{T} y$
Thus

$$
\varepsilon^{\top} \varepsilon=y^{\top} y-\partial \beta^{\top} x^{\top} y-\beta^{\top} x^{\top} x \beta
$$

The estimate $\hat{\beta}$ is given by

$$
\left.\frac{\partial}{\partial \beta}\left(\varepsilon^{\top} \varepsilon\right)\right|_{\beta=\hat{\beta}}=0
$$

using the Enstein summation convention to Pacilitate differentiation

$$
\varepsilon_{i} \varepsilon_{i}=y_{i} y_{i}-2 \beta_{j} x_{j i} y_{i}+\beta_{j} x_{j i} x_{i j} \beta_{j}
$$

50

$$
\frac{\partial}{\partial \beta_{j}}\left(\varepsilon_{i} \varepsilon_{i}\right)=-2 x_{j i} y_{i}+2 x_{j i} x_{i j} \beta_{j}
$$

and the estimate is given by

$$
\left.\frac{\partial}{\partial \beta_{j}}\left(\varepsilon_{i} \varepsilon_{i}\right)\right|_{\beta_{j}=\hat{\beta}_{j}}=0
$$

thus

$$
\begin{aligned}
& -2 x_{j i} y_{i}+2 x_{j i} x_{i j} \hat{\beta}_{j}=0 \\
\Rightarrow & \hat{\beta}_{j}=\frac{x_{j i} y_{i}}{x_{j i} x_{i j}} \\
\Rightarrow & \hat{\beta}=\left(x^{\top} x\right)^{-1} x^{\top} y
\end{aligned}
$$

## Using OLS to Estimate Parameters in an AR(q) Model

Ous can be used to estimate the parameters in an AR(q) model. Consider the first order model AR(1),

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

where $\varepsilon_{t}$ are independent identically distributed Normal random variables with zero mean and variance, $\sigma^{2}$,

$$
\varepsilon_{t} \sim N\left(0, \sigma^{2}\right)
$$

Now using repeated substitution on the ARCD model above gives

$$
x_{t}=\phi^{t} x_{0}+\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i}
$$

It follows that

$$
x_{t-1}=\varphi^{t-1} x_{0}+\sum_{i=1}^{t-1} \varphi^{t-i} \varepsilon_{i}
$$

and since the $\varepsilon_{t}$ are independet it follows that

$$
\begin{aligned}
& E\left(\varepsilon_{t} x_{t-1}\right)=\varphi^{t-1} x_{0} E\left(\varepsilon_{t}\right) \\
& +\sum_{i=1}^{t-1} \varphi^{t-i} E\left(\varepsilon_{t} \varepsilon_{i}\right)
\end{aligned}
$$

Now by definition

$$
E\left(\varepsilon_{t}\right)=0
$$

and since $t>i$

$$
E\left(\varepsilon_{t} \varepsilon_{i}\right)=0
$$

thus

$$
E\left(\varepsilon_{t} X_{t-1}\right)=0
$$

so $\varepsilon_{t}$ is independent of $x_{t-1}$.
Consider SLR with the model

$$
y_{i}=\beta x_{i}+\varepsilon_{i}
$$

Assuming SLR through the origin the unbiased estimate $\hat{\beta}$ is
given by

$$
\hat{\beta}=\frac{\sum_{i=1}^{n} x_{i} y_{i}}{\sum_{i=1}^{n} x_{i}^{2}}
$$

If it is assumed that $x_{i}$ is known and $x_{i}$ and $\varepsilon_{i}$ are independent, so

$$
E\left(x_{i} \varepsilon_{c}\right)=0
$$

then $i t$ can be shown that

$$
\begin{aligned}
E(\hat{\beta}) & =\beta \\
\operatorname{Var}(\hat{\beta}) & =\frac{6^{2}}{\sum_{i=1}^{n} x_{i}^{2}}
\end{aligned}
$$

If the linear model is compared with AR(1) the following associations can be made

$$
x_{t}=y_{i} \quad x_{t-1}=x_{i} \quad \varphi=\beta
$$

Then the estimate $\hat{\phi}$ is given by

$$
\hat{\phi}=\frac{\sum_{i=1}^{t} x_{i} x_{i-1}}{\sum_{i=1}^{t} x_{i-1}^{2}}
$$

where

$$
\operatorname{Var}(\hat{\varphi})=\frac{\sigma^{2}}{\sum_{i=1}^{t} x_{i-1}^{2}}
$$

The $R^{2}$ pararameter is used to estimate the amount of variance described by the fit.

$$
R^{2}=1-\frac{\sum_{i=1}^{n} \varepsilon_{i}^{2}}{\sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}
$$

AR(1) Parameter Estimation Example
Simulations of ARCD were performed and the SLR estimate

$$
\hat{\varphi}=\frac{\sum_{i=1}^{t} x_{i} x_{i-1}}{\sum_{i=1}^{t} x_{i-1}^{2}}
$$

was used to evaluate $\hat{\phi}$. The results for several values of $|\varphi|<1$ are shown. Estimates of $\phi$ obtained using SLR compare well input parameters

AR(1) Series: $\sigma=1.0, \varphi=-0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-122.jpg?height=699&width=1060&top_left_y=1281&top_left_x=259)

AR(1) Series: $\sigma=1.0, \varphi=0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-123.jpg?height=688&width=1036&top_left_y=137&top_left_x=278)

AR(1) Series: $\sigma=1.0, \varphi=-0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-123.jpg?height=742&width=1118&top_left_y=1076&top_left_x=261)

AR(1) Series: $\sigma=1.0, \varphi=0.9$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-124.jpg?height=714&width=1097&top_left_y=181&top_left_x=278)

AR(1) Series: $\sigma=1.0, \varphi=0.1$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-124.jpg?height=747&width=1122&top_left_y=1019&top_left_x=257)

These two final simulations investigate the behavior as the $|\phi|=1$ threchold is crossed. The difference between $\varphi=0.99$ and $\varphi=1.01$ is significant. As $|\varphi|$ crosses the value of 1 the $x_{t-1}$ term begins to dominate the noise term $\varepsilon_{t}$. Even at $\phi=1.01$ the impact is pronounced with explosive growth occuring rapidly.

AR(1) Series: $\sigma=1.0, \varphi=0.99$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-125.jpg?height=754&width=1154&top_left_y=1064&top_left_x=227)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-126.jpg?height=769&width=1168&top_left_y=219&top_left_x=199)

## Comparision with statsmodels OLS

This section will compare the previous analysis lising the derived estimate $\hat{\varphi}, \operatorname{var}(\hat{\varphi})$ and $R^{2}$ with an analysis performed using the as implementation provoder by the pithon package statsmodels. Consider the AR(1) simulation

$$
x_{t}=0.5 x_{t-1}+\varepsilon_{t}
$$

shown below.

AR(1) Series: $\sigma=1.0, \varphi=0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-127.jpg?height=656&width=970&top_left_y=1299&top_left_x=298)

The estimated $\hat{\varphi}, S E$ and $R^{2}$ are given by

$$
\begin{gathered}
\hat{\varphi}=0.478 \\
S E=\sigma_{\hat{\varphi}}=0.027 \\
R^{2}=0.226
\end{gathered}
$$

The python code used to perform the analysis is shown below
import statsmodels.api as sm

$$
\begin{aligned}
& x=\text { series }[0:-1] \\
& y=\text { series }[1:] \\
& \text { est }=\text { sm.OLS }(y, x) \\
& \text { est }=\text { est.fit(0) } \\
& \text { est.summary() }
\end{aligned}
$$

$$
\begin{aligned}
& \text { est.rsquared }=0.2286790669663884 \\
& \text { est.params= array([0.47820967]) } \\
& \text { est.bse= array([0.02780081]) }
\end{aligned}
$$

where the array series contains the simulation results.

The results obtained agree will with the implemented algorithm

$$
\begin{gathered}
\hat{\phi}=0.4782 \quad S E=0.028 \\
R^{2}=0.229
\end{gathered}
$$

## Maximum Likelihood Estimation of ARMA Models

Consider a random sample vetor,

$$
y=\left(y, 1, y_{2}, \ldots, y_{n}\right)
$$

of length $n$ of independet idenitically distributed random variables sharing parameters $\theta=\left(\theta_{1}, \theta_{2}, \ldots, \theta_{m}\right)$. If $y_{i}$ has distribution

$$
y_{i} \sim f\left(y_{i} ; \theta\right)
$$

It follows that the joint density for the sample defined by the vector $y$ is given by

$$
\begin{aligned}
f(y ; \theta) & =f\left(y_{1}, y_{2}, \ldots, y_{n} ; \theta\right) \\
& =\prod_{i=1}^{n} f\left(y_{i} ; \theta\right)
\end{aligned}
$$

For $f(y ; \theta) \theta$ is assumed known and $y$ unknown. The likelihood function switches this by assuming that $y$ is given and $\theta$ is
unknown. It is defined by

$$
L(\theta ; y)=\prod_{i=1}^{n} f(y ; i ; \theta)
$$

The los-likelihood function is obviously the log of $L(\theta ; y)$. Its use is to turn the product into a sum

$$
\begin{aligned}
\ln L(\theta ; y) & =\ln \prod_{i=1}^{n} f\left(y_{i} ; \theta\right) \\
& =\sum_{i=1}^{n} \ln f\left(y_{i} ; \theta\right)
\end{aligned}
$$

For an ARMA process this depomoposition is not valid since the elements of the sample vector are not independent. Consider the case where $n=2$ then the density is given by

$$
f\left(y_{1}, y_{2} ; \theta\right)
$$

using the deffinition of the
conditional probability density it follows that

$$
f\left(y_{1}, y_{2} ; \theta\right)=f\left(y_{2} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right)
$$

similarly for $n=3$
$f\left(y_{1} ; 1_{2}, y_{3} ; \theta\right)=f\left(y_{2}, y_{3} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right)$
$=f\left(y_{3} \mid y_{2}, y_{1} ; \theta\right) f\left(y_{2} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right)$
and $n=4$

$$
\begin{aligned}
f & \left(y_{1}, y_{2}, y_{3}, y_{4} ; \theta\right)=f\left(y_{2}, y_{3}, y_{4} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right) \\
= & f\left(y_{3}, y_{4} \mid y_{2}, y_{1} ; \theta\right) f\left(y_{2} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right) \\
= & f\left(y_{4} \mid y_{3}, y_{2}, y_{1} ; \theta\right) f\left(y_{3} \mid y_{2}, y_{1} ; \theta\right) \\
& f\left(y_{2} \mid y_{1} ; \theta\right) f\left(y_{1} ; \theta\right)
\end{aligned}
$$

Thus for $n$ samples

$$
f(y ; \theta)=\prod_{i=2}^{n} f\left(y_{i} \mid I_{i-1}\right) f\left(y_{1} ; \theta\right)
$$

where $I_{i}$ are the samples
upto $i$,

$$
\begin{aligned}
& I_{1}=y_{1} \\
& I_{2}=y_{2}, y_{1} \\
& \vdots \\
& I_{i}=y_{i}, y_{i-1}, \ldots, y_{2}, y_{1}
\end{aligned}
$$

It follows that the log likelyhod function is given by

$$
\begin{aligned}
\ln L(y ; \theta)= & \sum_{i=2}^{n} \ln f\left(y_{i} \mid I_{i-1} ; \theta\right) \\
& +\ln f\left(y_{i} ; \theta\right)
\end{aligned}
$$

The maximum likelinood estimate $\hat{\theta}$ is the value that maximizes the log likely hood function making it the most probable value given the samples,

$$
\left.\frac{\partial}{\partial \theta} \ln L(y ; \theta)\right|_{\theta=\hat{\theta}}=0 .
$$

## Maximum Likelihood Estimation of AR(1) Model

Consider the AR(1) model

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t} \quad t=1,2,3, \ldots
$$

where $\varepsilon_{t}$ are indentically distributed Normal random variables with zero mean and standard deviations

$$
\varepsilon_{t} \sim N\left(0, \sigma^{2}\right)
$$

Now

$$
\varepsilon_{t}=x_{t}-\phi x_{t-1}
$$

it follows, assuming $x_{t-1}$ is known, that

$$
x_{t} \mid x_{t-1} \sim N\left(\phi x_{t-1}, \sigma^{2}\right)
$$

where $t=2,3,4, \ldots$
Thus $x_{t}$ depends only on the previous value. The log likelihood function is constructed as folbws

$$
\theta=(\varphi, \sigma)
$$

and

$$
\begin{aligned}
& f\left(x_{t} \mid I_{t-1} ; \theta\right)=f\left(x_{t} \mid x_{t-1} ; \theta\right) \\
& =\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\left(x_{t}-\phi x_{t-1}\right)^{2} / 2 \sigma^{2}}
\end{aligned}
$$

where $t=2,3,4, \ldots$
To complete the construction the distribution of $x_{1}$ is regured. Recall that the mean and variance of $x_{t}$ are given by

$$
\begin{gathered}
\mu_{t}=\varphi^{t} x_{0} \\
\sigma_{t}^{2}=\sigma^{2} \frac{\left[1-\left(\varphi^{2}\right)^{t-1}\right]}{1-\varphi^{2}}
\end{gathered}
$$

it follows that for $t=1$

$$
\mu_{1}=\varphi x_{0} \quad \sigma_{1}^{2}=\frac{\sigma^{2}}{1-\varphi^{2}}
$$

thes

$$
\begin{aligned}
& f\left(x_{1} ; \theta\right) \sim N\left(\varphi x_{0}, \frac{\sigma^{2}}{1-\varphi^{2}}\right) \\
& =\sqrt{\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}} e^{-\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2} / 2 \sigma^{2}}
\end{aligned}
$$

In the previous section it was shown that the log-likelinood function

$$
\begin{aligned}
\ln L(y ; \theta)= & \sum_{i=2}^{n} \ln f\left(y_{i} \mid I_{i-1} ; \theta\right) \\
& +\ln f\left(y_{i} ; \theta\right)
\end{aligned}
$$

Now

$$
\begin{aligned}
& \ln f\left(x_{t} \mid I_{t-1} ; \theta\right)= \\
& \ln \left[\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\left(x_{t}-\varphi x_{t-1}\right)^{2} / 2 \sigma^{2}}\right] \\
& =\ln \left(\frac{1}{\sqrt{2 \pi \sigma^{2}}}\right)+\ln \left[e^{-\left(x_{t}-\varphi x_{t-1}\right)^{2} / 2 \sigma^{2}}\right]
\end{aligned}
$$

$$
=-\frac{1}{2} \ln \left(2 \pi \sigma^{2}\right)-\frac{1}{2 \sigma^{2}}\left(x_{t}-\varphi x_{t-1}\right)^{2}
$$

and

$$
\begin{aligned}
& \ln f\left(x_{1} ; \theta\right)= \\
& \quad \ln \left[\sqrt{\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}} e^{\left.-\left(1-\varphi^{2}\right)\left(x_{1}+\varphi x_{0}\right)^{2} / 2 \sigma^{2}\right]}\right. \\
& =\ln \left(\sqrt{\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}}\right)+\ln \left[e^{\left.-\left(1-\varphi^{2}\right)\left(x_{1}+\varphi x_{0}\right)^{2} / 2 \sigma^{2}\right]}\right. \\
& =\frac{1}{2} \ln \left(\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}\right)-\frac{\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}}{2 \sigma^{2}}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \ln L(x ; \theta)=\sum_{t=2}^{n}\left\{-\frac{1}{2} \ln \left(2 \pi \sigma^{2}\right)\right. \\
& \left.-\frac{1}{2 \sigma^{2}}\left(x_{t}-\varphi x_{t-1}\right)^{2}\right\} \\
& \frac{1}{2} \ln \left(\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}\right)-\frac{\left(1-\varphi^{2}\right)}{2 \sigma^{2}}\left(x_{1}-\varphi x_{0}\right)^{2}
\end{aligned}
$$

$$
\begin{aligned}
= & -\frac{(n-1)}{2} \ln \left(2 \pi \sigma^{2}\right)+\frac{1}{2} \ln \left(\frac{1-\varphi^{2}}{2 \pi \sigma^{2}}\right) \\
& -\frac{\left(1-\varphi^{2}\right)}{2 \sigma^{2}}\left(x_{1}-\varphi x_{0}\right)^{2} \\
& -\frac{1}{2 \sigma^{2}} \sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2} \\
= & -\left(\frac{n-1}{2} \ln \left(2 \pi \sigma^{2}\right)-\frac{1}{2} \ln \left(2 \pi \sigma^{2}\right)\right. \\
& +\frac{1}{2} \ln \left(1-\varphi^{2}\right)-\frac{1}{2 \sigma^{2}}\left\{\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}\right. \\
& \left.+\sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2}\right\} \\
= & -\frac{n}{2} \ln \left(2 \pi \sigma^{2}\right)+\frac{1}{2} \ln \left(1-\varphi^{2}\right) \\
= & \frac{1}{2 \sigma^{2}}\left[\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}+\sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2}\right]
\end{aligned}
$$

Recall that the AR(1) model is given by

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

$$
\Rightarrow \varepsilon_{t}=x_{t}-\varphi x_{t-1}
$$

The sum is clearly the sum of the residuls squared for $t>1$ and the term

$$
\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}
$$

is the residual for $x_{1}$,

$$
\varepsilon_{1}=\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}
$$

since

$$
\varepsilon_{1} \sim N\left(0, \sigma^{2}\right)
$$

50

$$
\begin{aligned}
& S S R=\sum_{i=1}^{n} \varepsilon_{i}^{2} \\
& =\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}+\sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2}
\end{aligned}
$$

The Maximum Likelyhood estimate (MLE) is given by

$$
\left.\frac{\partial}{\partial \sigma^{2}} \ln L\left(x ; \varphi, \sigma^{2}\right)\right|_{\sigma^{2}=\hat{\sigma}^{2}}=\partial
$$

$$
\left.\frac{\partial}{\partial \phi} \ln L\left(x ; \phi, \sigma^{2}\right)\right|_{\phi=\hat{\varphi}}=0
$$

For the first expression
$\frac{\partial}{\partial \sigma^{2}} \ln L\left(x ; \phi, \sigma^{2}\right)=\frac{\partial}{\partial \sigma^{2}}\left\{-\frac{n}{2} \ln \left(2 \pi \sigma^{2}\right)\right.$

$$
\begin{aligned}
& +\frac{1}{2} \ln \left(1-\varphi^{2}\right)-\frac{1}{2 \sigma^{2}}\left[\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}\right. \\
& \left.\left.+\sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2}\right]\right\}
\end{aligned}
$$

$=-\frac{n}{2} \frac{1}{\sigma^{2}}+\frac{S S R}{2 \sigma^{4}}$
and for the second expression
$\frac{\partial}{\partial \varphi} \ln L\left(x ; \varphi, \sigma^{2}\right)=\frac{\partial}{\partial \varphi}\left\{-\frac{n}{2} \ln \left(2 \pi \sigma^{2}\right)\right.$

$$
\begin{aligned}
& +\frac{1}{2} \ln \left(1-\varphi^{2}\right)-\frac{1}{2 \sigma^{2}}\left[\left(1-\varphi^{2}\right)\left(x_{1}-\varphi x_{0}\right)^{2}\right. \\
& \left.\left.+\sum_{t=2}^{n}\left(x_{t}-\varphi x_{t-1}\right)^{2}\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2}\left(\frac{-2 \varphi}{1-\varphi^{2}}\right)-\frac{1}{2 \sigma^{2}}\left[-2 \varphi\left(x_{1}-\varphi x_{0}\right)^{2}\right. \\
& +2\left(1-\varphi^{2}\right)\left(-x_{0}\right)\left(x_{1}-\varphi x_{0}\right) \\
& \left.+\sum_{t=2}^{n}\left(-2 x_{t-1}\right)\left(x_{t}-\varphi x_{t-1}\right)\right] \\
= & -\frac{\varphi}{1-\varphi^{2}}+\frac{\left(x_{1}-\varphi x_{0}\right)}{\sigma^{2}}\left[\varphi\left(x_{1}-\varphi x_{0}\right)\right. \\
& \left.+x_{0}\left(1-\varphi^{2}\right)\right]+\frac{1}{\sigma^{2}} \sum_{t=2}^{n} x_{t-1}\left(x_{t}-\varphi x_{t-1}\right) \\
= & -\frac{\phi}{1-\varphi^{2}}+\left(\frac{x_{1}-\varphi x_{0}}{\sigma^{2}}\right)\left[\varphi x_{1}-\varphi^{2} x_{0}+x_{0}\right. \\
& \left.-x_{0} \varphi^{2}\right]+\frac{1}{\sigma^{2}} \sum_{t=2}^{n} x_{t-1}\left(x_{t}-\varphi x_{t-1}\right) \\
= & -\frac{\varphi}{1-\varphi^{2}}+\frac{\left(x_{1}-\varphi x_{0}\right)}{\sigma^{2}}\left[x_{0}\left(1-2 \varphi^{2}\right)+\varphi x_{1}\right] \\
& +\frac{1}{\sigma^{2}} \sum_{t=2}^{n} x_{t-1}\left(x_{t}-\varphi x_{t-1}\right)
\end{aligned}
$$

vext the estimates will be
determined. For $\hat{\sigma}^{2}$ it is seen that

$$
\left.\frac{\partial}{\partial \sigma^{2}} \ln L\left(x ; \varphi, \sigma^{2}\right)\right|_{\sigma^{2}=\sigma^{2}}=0
$$

$$
\begin{aligned}
& \Rightarrow-\frac{n}{2} \frac{1}{\hat{\sigma}^{2}}+\frac{S S R}{2 \hat{\sigma}^{4}}=0 \\
& =\frac{S S R}{\hat{\sigma}^{2}}=n \\
& \Rightarrow \hat{\sigma}^{2}=\frac{S S R}{n}
\end{aligned}
$$

and for $\hat{\varphi}$

$$
\begin{aligned}
& \left.\frac{\partial}{\partial \varphi} \ln L\left(x_{j} ; \varphi, \sigma^{2}\right)\right|_{\phi=\hat{\phi}}=0 \\
\Rightarrow & -\frac{\hat{\phi}}{1-\hat{\varphi}^{2}}+\frac{\left(x_{1}-\hat{\phi} x_{0}\right)}{\hat{\sigma}^{2}}\left[x_{0}\left(1-2 \hat{\phi}^{2}\right)+\hat{\phi} x_{1}\right]
\end{aligned}
$$

$$
\begin{aligned}
+ & \frac{1}{\hat{\sigma}^{2}} \sum_{t=2}^{n} x_{t-1}\left(x_{t}-\hat{\varphi} x_{t-1}\right)=0 \\
\Rightarrow & \sum_{t=2}^{n}\left(x_{t}-\hat{\varphi} x_{t-1}\right) x_{t-1}=\frac{\hat{\sigma}^{2} \hat{\varphi}}{1-\hat{\varphi}^{2}} \\
& -\left(x_{1}-\hat{\varphi} x_{0}\right)\left[x_{0}\left(1-2 \hat{\varphi}^{2}\right)+\hat{\varphi} x_{1}\right]
\end{aligned}
$$

If the righthand side of this expression is zero then the MLE $\hat{\phi}$ is equal to the SLR estimate which is given by

$$
\hat{\phi}=\frac{\sum_{i=1}^{t} x_{i} x_{i-1}}{\sum_{i=1}^{t} x_{i-1}^{2}}
$$

It can be seen that this is approximately the case

$$
\begin{aligned}
& \frac{\hat{\sigma}^{2} \hat{\varphi}}{1-\hat{\varphi}^{2}}-\left(x_{1}-\hat{\varphi} x_{0}\right)\left[x_{0}\left(1-2 \hat{\varphi}^{2}\right)+\hat{\varphi} x_{1}\right] \\
= & \frac{\hat{\sigma}^{2} \hat{\varphi}}{1-\hat{\varphi}^{2}}-\left(x_{1}-\hat{\phi} x_{0}\right)\left[x_{0}\left(1-\hat{\varphi}^{2}\right)+\hat{\varphi}\left(x_{1}-\hat{\phi} x_{0}\right)\right] \\
= & \frac{\hat{\sigma}^{2} \hat{\varphi}}{1-\hat{\varphi}^{2}}-\left(x_{1}-\hat{\phi} x_{0}\right)\left(1-\hat{\varphi}^{2}\right) x_{0} \\
& -\hat{\varphi}\left(x_{1}-\hat{\varphi} x_{0}\right)^{2}
\end{aligned}
$$

Since

$$
E\left(x_{1}\right)=\varphi x_{0}
$$

The middle torm will average to zero and since

$$
E\left[\left(x_{1}-\hat{\varphi} x_{0}\right)^{2}\right]=\frac{\sigma^{2}}{1-\varphi^{2}}
$$

the first and last terms will cancel on average.

## Method of Moments Estimation

The method of moments is based on the law of large numbers. As an illustrative example consider a sample of independent identically distributed random varibles

$$
x=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

with distribution parameterized by $\theta, f(x \mid \theta)$. If the samples are generated with a particular for $\theta$ then

$$
\mu_{x}(\theta)=\int_{-\infty}^{\infty} x f(x \mid \theta) d x
$$

From the law of large numbers the sample average

$$
\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

approaches $\mu_{x}(\theta)$ as $n \rightarrow \infty$.

It follows that $\bar{x}$ can be used as an estimate for $\mu_{x}(\hat{\theta})$

$$
\bar{X}=\mu_{x}(\hat{\theta})
$$

which can be solved for $\hat{\theta}$. This proceedure can be used for any moment estimated from the sample data. Let $u_{m}$ denote the m'th moment of the data set. Then

$$
\begin{aligned}
& \mu_{m}=\int_{-\infty}^{\infty} x^{m} f(x \mid \theta) d x \\
& \overline{x^{m}}=\frac{1}{n} \sum_{i=1}^{n} x^{m}
\end{aligned}
$$

and

$$
\bar{x}^{m}=\mu_{m}(\hat{\theta})
$$

which can be solved of $\hat{\theta}$.
The general proceedure consists of the following steps. Consider $a$ set of $n$ samples

$$
x=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

that are independent and identically distributed with a distribution containing $m$ parameters.

1) Compute the first $m$ moments using the assumed distribution

$$
\begin{aligned}
\mu_{m}\left(\theta_{1}, \theta_{2}, \theta_{3}\right. & \left., \ldots, \theta_{m}\right) \\
& =\int_{-\infty}^{\infty} x f\left(x \mid \theta_{1}, \theta_{2}, \ldots, \theta_{m}\right) d x
\end{aligned}
$$

2) Solve for the $m$ porameters $\theta_{m}$ by solving the equations

$$
\begin{aligned}
& \mu_{1}=\mu_{1}\left(\theta_{1}, \theta_{2}, \ldots, \theta_{m}\right) \\
& \mu_{2}=\mu_{2}\left(\theta_{1}, \theta_{2}, \ldots, \theta_{m}\right) \\
& \vdots \\
& \mu_{m}=\mu_{3}\left(\theta_{1}, \theta_{2}, \ldots, \theta_{m}\right)
\end{aligned}
$$

to obtain

$$
\begin{aligned}
& \theta_{1}=\theta_{1}\left(\mu_{1}, \mu_{2}, \ldots, \mu_{m}\right) \\
& \theta_{2}=\theta_{2}\left(\mu_{1}, \mu_{2}, \ldots, \mu_{m}\right) \\
& \vdots \\
& \theta_{m}=\theta_{m}\left(\mu_{1}, \mu_{2}, \ldots, \mu_{m}\right)
\end{aligned}
$$

3) compute the sample moments

$$
\begin{aligned}
& \bar{x}^{1}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
& \bar{x}^{2}=\frac{1}{n} \sum_{i=1}^{n} x_{i}^{2} \\
& \vdots \\
& \bar{x}^{m}=\frac{1}{n} \sum_{i=1}^{n} x_{i}^{m}
\end{aligned}
$$

4) use $\bar{x}^{m}$ as an estimate for $\mu_{m}$ in the equations obtained in stel 3 to dotain the parameter estimates

$$
\begin{aligned}
& \hat{\theta}_{1}=\theta_{1}\left(x^{1}, x^{2}, \ldots, x^{m}\right) \\
& \hat{\theta}_{2}=\theta_{2}\left(x^{1}, x^{2}, \ldots, x^{m}\right) \\
& \vdots \\
& \hat{\theta}_{3}=\theta_{3}\left(x^{1}, x^{2}, \ldots, x^{m}\right)
\end{aligned}
$$

## using the Detta Method to Calculate Estimation variance

The Delta Method can be used to estimate the variance of the distribution parameters estimated using the method of moments. The method will be first derived for the single parameter case and then extended to the multivariate case.

Consider $n$ samples,

$$
x=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}
$$

with asswmed distribution

$$
f(x \mid \theta)
$$

containing single parameter $\theta$. let

$$
\mu(\theta)=\int_{-\infty}^{\infty} x f(x \mid \theta) d x
$$

solurns for $\theta$ gives

$$
\theta=\theta(\mu)
$$

let

$$
\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

then the estimate $\hat{\theta}$ is given by

$$
\hat{\theta}=\theta(\bar{x})
$$

Now recall that the Central Limit theorem states that as $n \rightarrow \infty$

$$
\sqrt{n}\left(\bar{x}_{n}-\mu\right) \xrightarrow{D} \sigma z
$$

where $\xrightarrow{D}$ means converges in distribution, 2 is the stardard normal distribution,
and

$$
\begin{aligned}
& Z \sim N(0,1) \\
& \sigma Z \sim N\left(0, \sigma^{2}\right)
\end{aligned}
$$

and if $x_{n} \sim f(x)$

$$
\bar{x}_{n}=\frac{1}{n} \sum_{c=1}^{n} x_{n}
$$

$$
\begin{aligned}
\mu & =\int_{-\infty}^{\infty} x f(x) d x \\
\sigma^{2} & =\int_{-\infty}^{\infty}(x-\mu)^{2} f(x) d x
\end{aligned}
$$

What the Contral Limt Theorem says is that the difference between the average of a finite number of samples with distribution $f(x)$ and the distribution mean, $\mu$ approaches a Normal instribution with mean of zero and variance $\sigma^{2}$ as the number of samples increases.
Next the Central Limit Theorem as stated above will be extended to functions of $\bar{x}$ and $\mu$, $\theta(\bar{x})$ and $\theta(\mu)$.
Now consider $\theta(t)$ and assume $t-\mu \ll 1$. It follows that $\theta(t)$ can be expanded in a Taylor series about $\mu$ to obtained

$$
\begin{aligned}
\theta(t) \approx & \theta(\mu)+\left.\frac{d \theta}{d t}\right|_{t=\mu}(t-\mu) \\
= & \theta(\mu)+\theta^{\prime}(\mu)(t-\mu)
\end{aligned}
$$

where

$$
\theta^{\prime}(\mu)=\left.\frac{d \theta}{d t}\right|_{t=\mu}
$$

It follows that

$$
\theta(t)-\theta(\mu)=\theta^{\prime}(\mu)(t-\mu)
$$

Now let $t=\bar{x}$, then

$$
\begin{aligned}
\theta(\bar{x})-\theta(\mu) & =\theta^{\prime}(\mu)(\bar{x}-\mu) \\
& \Rightarrow \theta^{\prime}(\mu) \frac{\sigma}{\sqrt{n}} 2
\end{aligned}
$$

where the last step follows from the Central Limit Theorem,

$$
\bar{x}-\mu \xrightarrow{D} \frac{\sigma^{\prime} \theta^{\prime}(\mu) z}{\sqrt{n}}
$$

Thus the difference

$$
\theta(\bar{x})-\theta(\mu) \xrightarrow{\unrhd} \frac{\sigma}{\sqrt{n}} \theta^{\prime}(\mu) z
$$

has distribution

$$
\frac{\sigma \theta^{\prime}}{\sqrt{n}}(\mu) Z \sim N\left(0, \frac{\sigma^{2}}{n} \theta^{\prime}(\mu)^{2}\right)
$$

Now the parameter estimate is

$$
\hat{\theta}=\theta(\bar{x})
$$

using the previous result the difference between the estimate and the true value has a normal distribution with variance,

$$
\hat{\theta}-\theta(\mu) \sim N\left(0, \frac{\sigma^{2}}{n} \theta^{\prime}(\mu)^{2}\right)
$$

It follows that the varkance can be used as estimate of the error in the estimation,

$$
\sigma_{\hat{\theta}}^{2}=E\left[(\hat{\theta}-\theta(\mu))^{2}\right]=\frac{\sigma^{2}}{n} \theta^{\prime}(\mu)^{2}
$$

In summary the estimation variance is given by

$$
\sigma_{\hat{\theta}}^{2}=\frac{\sigma^{2}}{n} \theta^{\prime}(\mu)^{2}
$$

## Estimation of Hurst Parameter

Recall that Fractional Brownian motion is defined by the stochastec integral.
$Z^{H}(t)=\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s)$
where $H$ is the Hurst parameter which is assumed to satisfy

$$
0<H<1
$$

and $d B(s)$ is Brownian noise,

$$
\begin{aligned}
& (t-s)_{+}=\left\{\begin{array}{cc}
t-s & t>s \\
0 & t \leqslant s
\end{array}\right. \\
& (-s)_{+}=\left\{\begin{array}{cc}
-s & s<0 \\
0 & s \geqslant 0
\end{array}\right.
\end{aligned}
$$

and

$$
\begin{aligned}
C(H)^{2}= & \int_{-\infty}^{0}\left[(1-S)^{H-1 / 2}-(-S)^{H-1 / 2}\right]^{2} d S \\
& +\frac{1}{2 H}
\end{aligned}
$$

The mean and variance are given by

$$
\begin{aligned}
E\left[Z^{H}(t)\right] & =0 \\
\operatorname{Var}\left[Z^{H}(t)\right] & =E\left[\left(Z^{H}(t)\right)^{2}\right] \\
& =t^{\partial H}
\end{aligned}
$$

The variance of an increment of Fractional Brownian Motion is given by

$$
\begin{aligned}
\operatorname{Var}\left[z^{H}(t)-z^{H}(s)\right] & =E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right] \\
& =(t-s)^{2 H}
\end{aligned}
$$

The actocovariance is defined by

$$
\begin{aligned}
\rho(t, s) & =\operatorname{Cov}\left[z^{H}(t) z^{H}(s)\right] \\
& =E\left[z^{H}(t) z^{H}(s)\right] \\
& =\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

For $t \gg s$

$$
\rho(t, s) \approx \frac{1}{2}\left(s^{2 H}+2 H s t^{2 H-1}\right)
$$

and

$$
\rho(t+s, s)=t^{2 H}
$$

Fractional Brownian Noise is defined by

$$
\Delta z_{k}^{H}=z^{H}\left(t_{k}\right)-z^{H}\left(t_{k-1}\right)
$$

where

$$
t_{k}=k \Delta t
$$

It follows that

$$
z^{H}(n \Delta t)=\sum_{i=1}^{n} \Delta z_{k}
$$

The autocouviace of fractional Brownian Noise is given by

$$
\begin{aligned}
\gamma_{n}^{H} & =\operatorname{Cov}\left(\Delta Z_{k}^{H} \Delta Z_{k+n}^{H}\right) \\
& =\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
\end{aligned}
$$

For $n \gg 1$

$$
\gamma_{n}^{H} \approx \Delta t^{2 H} H(2 H-1) n^{2 H-2}
$$

The variance of Fractional Gaussian Norse is given by

$$
\operatorname{Var}\left(\Delta Z_{k}^{H}\right)=\Delta t^{2 H}
$$

Fractional Brownian Noise is self similar. Self similar means that for a constant, a.

$$
a^{-2 H} \rho(a t, s)=\rho(t, s)
$$

The moments of increments of Fractional Brownian are invariant under transtation in time.
This property is called stationarity. An increment is defined by

$$
Z^{H}(t+s)-Z^{H}(s)
$$

Stationarity Implies

$$
\begin{aligned}
& E\left[\left(z^{H}(t+s)-z^{H}(s)\right)\left(z^{H}(r+s)-z^{H}(s)\right)\right] \\
& =E\left[z^{H}(t) z^{H}(r)\right]
\end{aligned}
$$

Also, it is a consequence of stationarity that

$$
\gamma_{n}^{H}=\operatorname{Cov}\left(\Delta Z_{k}^{H} \Delta Z_{k+n}^{H}\right)
$$

is independent of $k$.
In this section methods for evaluation of H from a given time series ore discussed.

## Aggregated Variance Method.

Consider a time series of dentically distributed samples

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

If the series is divided into $d$ smaller series of length $m$ where

$$
m d=n
$$

let $k=0,1,2, \ldots, d-1$ and define the aggregated sum by

$$
\begin{aligned}
x_{k}^{m} & =\frac{1}{m}\left(x_{k m+1}+x_{k m+2}+\cdots+\right. \\
& \left.x_{k m+m-1}+x_{k m+m}\right) \\
& =\frac{1}{m}\left(x_{k m+1}+\cdots+x_{(k+1) m}\right) \\
& =\frac{1}{m} \sum_{i=k m+1}^{(k+1) m} x_{i}
\end{aligned}
$$

and

$$
\bar{X}^{m}=\frac{1}{d} \sum_{i=0}^{d-1} X_{i}^{m}
$$

Then the aggregated variance is defined by

$$
\operatorname{Var}\left(x^{m}\right)=\frac{1}{d} \sum_{i=0}^{d-1}\left(x_{i}^{m}-\bar{x}^{m}\right)^{2}
$$

Because of stationarity the terms in the sum are independent of $k$, thus an ensemble of size $d$ for each chore of $m$ is created.

Consider the sum

$$
x_{k}^{m}=\frac{1}{m} \sum_{i=k m+1}^{(k+1) m} x_{i}
$$

in the absence of correlation and if the $x_{i}$ are independent and
dentically distributed the central limit theorem,

$$
\sqrt{n}\left(\frac{x_{k}^{m}-\mu}{\sigma}\right) \xrightarrow{D} \operatorname{Normal}(0,1)
$$

where $\mu$ and $\sigma^{2}$ are mean and variance of the $x_{i}$ gives the asymntotic variance of

$$
\operatorname{Var}\left(x^{m}\right) \xrightarrow{\text { Avar }} \frac{\sigma^{2}}{m}
$$

let

$$
\gamma\left(i_{j}\right)=\frac{\operatorname{cov}\left(x_{i} x_{j}\right)}{\sigma^{2}}
$$

Then cossume that

$$
\operatorname{Var}\left(x^{m}\right) \xrightarrow{A \cup A R} \frac{1}{m^{2}} \sum_{i=1}^{m} \sum_{j=1}^{m} \operatorname{Cov}\left(x_{i} x_{j}\right)
$$

$$
=\frac{\sigma^{2}}{m^{2}} \sum_{i=1}^{m} \sum_{j=1}^{m} \gamma(i, j)
$$

In the absence of correlation

$$
\gamma(i, j)=\delta_{i j}
$$

so that

$$
\begin{aligned}
\operatorname{Var}\left(x^{m}\right) \xrightarrow{\text { Avar }} & \frac{\sigma^{2}}{m^{2}} \sum_{i=1}^{m} \sum_{j=1}^{m} \delta_{i j} \\
& =\frac{\sigma^{2}}{m^{2}} m \\
& =\frac{\sigma^{2}}{m}
\end{aligned}
$$

which is the same result obtained previously. Now

$$
\frac{\sigma^{2}}{m^{2}} \sum_{i=1}^{m} \sum_{j=1}^{m} \gamma(i, j)=\frac{\sigma^{2}}{m^{2}} \sum_{i=j}^{m} \gamma(i, j)
$$

$$
\begin{aligned}
& \left.+\sum_{i \neq j}^{m} r(i, j)\right\} \\
= & \frac{\sigma^{2}}{m^{2}}\left\{m+\sum_{i \neq j}^{m} r(i, j)\right\} \\
= & \frac{\sigma^{2}}{m}\left\{1+\frac{1}{m} \sum_{i \neq j}^{m} r(i, j)\right\}
\end{aligned}
$$

Thus if it is assumed that $\gamma(i, j)$ is small it can be considered a correction to the central limit result, so that the assymptotic variance in the presence of correlation can be approximated by
$\operatorname{var}\left(x^{m}\right) \xrightarrow{A U R} \frac{\sigma^{2}}{m}\left\{1+\frac{1}{m} \sum_{i \neq j}^{m} \gamma(i, j)\right\}$
furthure if it is assumed that $r\left(c_{j}\right)$ depends only on

$$
k=|i-j|
$$

then

$$
\frac{1}{m} \sum_{i \neq j}^{m} \gamma(|i-j|)=\frac{1}{m} \sum_{k=1}^{m} n(k) \gamma(k)
$$

where $n(k)$ is the number of terms summic to $|i-j|=k$ for each $k$. By insepection it can be seen that

$$
n(k)=2(m-k)
$$

thus
$\frac{1}{m} \sum_{k=1}^{m} n(k) \gamma(k)=\frac{1}{m} \sum_{k=1}^{m} 2(m-k) \gamma(k)$

$$
\begin{aligned}
& =2 \sum_{k=1}^{m} m\left(1-\frac{k}{m}\right) \gamma(k) \\
& =2 \sum_{k=1}^{m-1}\left(1-\frac{k}{m}\right) \gamma(k)
\end{aligned}
$$

Thus for the sum

$$
x_{k}^{m} \quad \frac{1}{m} \sum_{i=k m+1}^{(k+1) m} x_{i}
$$

The asymtotic variance is given by
$\operatorname{var}\left(x^{m}\right) \xrightarrow{\text { AUAR }} \frac{\sigma^{2}}{m}\left\{1+2 \sum_{k=1}^{m-1}\left(1-\frac{k}{m}\right) \gamma(k)\right\}$

## Aggregated Variance for Fractional Brownian Motion

Consider the aggregated process

$$
x_{0}^{m}=\frac{1}{m} \sum_{i=1}^{m} x_{i}
$$

From self-smilarity for $a=1,2,3, \ldots$

$$
X_{a i} \stackrel{D}{=} a^{H} X_{i}
$$

where ? means equal in distribution It follows that

$$
X_{0}^{m} \stackrel{D}{=} \frac{m^{H}}{m} X_{1}=m^{H-1} X_{1}
$$

Now $X_{1}$ is a single instance of Fractional Brownian noise so

$$
\begin{aligned}
& E\left(x_{1}\right)=0 \\
& \operatorname{var}\left(x_{1}\right)=\Delta t^{2 H}=\sigma^{2}
\end{aligned}
$$

So

$$
\begin{aligned}
\operatorname{Var}\left(x_{0}^{m}\right) & =\operatorname{Var}\left(m^{H-1} x_{1}\right) \\
& =m^{2 H-2} \operatorname{Uar}\left(x_{1}\right) \\
& =\sigma^{2} m^{2 H-2}
\end{aligned}
$$

Since samples of Fractional Brownian joise are identically distributed and stationary the relation above is valid for any oalue of $k$. Thus

$$
\operatorname{Var}\left(x_{k}^{m}\right)=\sigma^{2} m^{2 H-2}
$$

Simulations of Aggregate Variane for Fractional Brownian Motion

In the previous section it was shown that for samples of Frational Brownian Noise dended by

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

That the aggregated process defined
by by

$$
x_{k}^{m}=\frac{1}{m} \sum_{i=k m+1}^{(k+1) m} x_{i}
$$

where

$$
d=\frac{n}{m}
$$

Define the aggregated mean by

$$
\bar{x}^{m}=\frac{1}{d} \sum_{i=0}^{d-1} x_{i}^{m}
$$

Then the aggregated variance is defined by

$$
\operatorname{Var}\left(x^{m}\right)=\frac{1}{d} \sum_{i=0}^{d-1}\left(x_{i}^{m}-\bar{x}^{m}\right)^{2}
$$

In the previous section it was shown

$$
\begin{aligned}
& \operatorname{Var}\left(x^{m}\right)=C m^{2 H-2} \\
& \Rightarrow \log \operatorname{Var}\left(x^{m}\right)= \\
& \log C+(2 H-2) \log m
\end{aligned}
$$

For a given time series $H$ can be estimated by computing Var ( $x^{m}$ ) for a range of values of $m$ and fitting a line using ols to a los-log plot of $\operatorname{var}\left(x^{m}\right)$ us. $m^{5}$. if $\beta$ is the slope of the line then

$$
\partial H-2=\beta \Rightarrow H=\frac{\beta}{2}+1
$$

The following two plots show the results of two Fractional Brownian Doise simulations, using the FFT, method compared to the the aggregated processes Where 10 and 50 samples. The reduction in variance is apparent.

Aggregated Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.8$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-171.jpg?height=265&width=1273&top_left_y=902&top_left_x=183)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-171.jpg?height=274&width=1282&top_left_y=1204&top_left_x=180)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-171.jpg?height=343&width=1283&top_left_y=1489&top_left_x=181)

Aggregated Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.4$

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-172.jpg?height=275&width=1313&top_left_y=187&top_left_x=161)
The next plots show the resuls obtained by using ols to estimate 4 by fitting a line to the plot of $\log \left(\operatorname{Uar}\left(x^{m}\right)\right)$ us. $\log (m)$.

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-172.jpg?height=289&width=1320&top_left_y=497&top_left_x=156)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-172.jpg?height=343&width=1323&top_left_y=812&top_left_x=157)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-173.jpg?height=836&width=1232&top_left_y=102&top_left_x=177)

Aggregated Variance: $\mathrm{H}=0.8$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-173.jpg?height=807&width=1232&top_left_y=1092&top_left_x=177)

## Periodigram Method

The periodigram method of estimation of the Hurst parameter, $H$, makes use of the Fractional Brownian Noise power spectrum. The power spectrum is Fourier Tranform of the fractional Brownian voice auto correlation Function. This relationship is called the weinerknichnin Theorem

Recall that Fractional Brownian Doise defined by is

$$
\Delta z_{k}^{H}=z^{H}\left(t_{k}\right)-z^{H}\left(t_{k-1}\right)
$$

where

$$
t_{k}=k \Delta t
$$

It follows that

$$
Z^{H}(n \Delta t)=\sum_{i=1}^{n} \Delta Z_{k}
$$

The autocouoriace of fractional Brownian Noise is given by

$$
\begin{aligned}
\gamma_{n}^{H} & =\operatorname{Cov}\left(\Delta Z_{k}^{H} \Delta Z_{k+n}^{H}\right) \\
& =\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
\end{aligned}
$$

For $n \gg 1$

$$
\gamma_{n}^{H} \approx \Delta t^{2 H} H(2 H-1) n^{2 H-2}
$$

and the actocorrelation coefficient by

$$
e_{n}^{H}=\frac{\gamma_{n}^{H}}{\Delta t^{2 H}}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

and for $n \gg 1$

$$
e_{n}^{H} \approx H(2 H-1) n^{2 H-2}
$$

Let $f_{\omega}$ denote the Fractional Brownian Motion power spectrum,
then from the weiner-khinchin Theorem

$$
f_{\omega}=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e_{n}^{H} e^{-i \omega n} d n
$$

$f_{\omega}$ is real so

$$
f_{\omega}=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{H} \cos (\omega n) d n
$$

using the $n \gg 1$ expression for $e_{n}^{H}$ gives

$$
f_{\omega}=\frac{1}{2 \pi} \int_{-\infty}^{\infty} H(2 H-1)|n|^{2 H-2} \cos (\omega n) d n
$$

let

$$
\begin{array}{rl}
u & =\omega n \\
\Rightarrow n & =\frac{u}{\omega} \\
\Rightarrow \frac{1}{\omega} d u & d n
\end{array}
$$

then

$$
\begin{aligned}
f_{\omega}= & \frac{1}{2 \pi} H(2 H-1) \int_{-\infty}^{\infty}\left(\left\lvert\, \frac{u}{\omega}\right.\right)^{2 H-2} \cos (u) \frac{1}{\omega} d u \\
= & \frac{1}{2 \pi} H(2 H-1)\left(\frac{1}{|\omega|}\right)^{2 H-1} \\
& \int_{-\infty}^{\infty} \cos (u)|u|^{2 H-2} d u
\end{aligned}
$$

let

$$
C=\frac{1}{2 \pi} H(2 H-1) \int_{-\infty}^{\infty}|u|^{2 H-2} \cos u d u
$$

then

$$
f_{\omega}=C|\omega|^{1-2 H}
$$

Simulations of Periodigram Method

In the previous section it was shown that for samples of Frational Brownian Noise denoted by

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

with Discret Fourier Trensform

$$
\hat{f}_{\omega}=\sum_{j=1}^{n} x_{j} e^{2 \pi i\left(y_{n}\right) \omega}
$$

Has a power spectron, $F(\omega)$, defined

$$
F(\omega)=\hat{f}_{\omega} \hat{f}_{\omega}^{*}=\left|\hat{f}_{\omega}\right|^{2}
$$

where $f_{w}^{*}$ is the complex conjugate of fw.
If $e_{n}^{H}$ is the autocorrelation function, its Fourier transform is given by

$$
\hat{\rho}_{\omega}^{H}=\sum_{j=1}^{n} \rho_{j}^{H} e^{-2 \pi(j / n) \omega}
$$

The Weiner - Khinchin Theorem relates $F(\omega)$ to the Fourier Transform of the autocorrelation function,

$$
F(\omega)=\hat{e}^{H}
$$

In the previous section it was shown that for Fractional Brownian Noise with $n \gg 1$

$$
e_{n}^{H} \approx H(2 H-1) n^{2 H-2}
$$

that

$$
\hat{e}_{\omega}^{H} \approx C \omega^{1-\partial H}
$$

where $c$ is a constant given by

$$
C=\frac{1}{2 \pi} H(2 H-1) \int_{-\infty}^{\infty}|u|^{2 H-2} \cos u d u
$$

Thus for $\omega \gg 1$

$$
\begin{aligned}
& e_{\omega}^{H}=\left|\hat{f}_{\omega}\right|^{2} \\
& \Rightarrow \quad\left|\hat{f}_{\omega}\right|^{2} \approx C \omega{ }^{1-\partial H}
\end{aligned}
$$

This relationship is lesed to estimate $H$ for Fractional Brownian Noise examples.
Another useful relationship used in the analysis can be fourd by considering the sum of squares of the noise samples.
The inverse Farier Transform is defined by

$$
x_{k}=\frac{1}{n} \sum_{j=1}^{n} \hat{f}_{\omega} e^{2 \pi i(\omega / n) k}
$$

50

$$
\begin{aligned}
& \sum_{k=1}^{n} x_{k}^{2}=\sum_{k=1}^{n}\left[\frac{1}{n} \sum_{j=1}^{n} \hat{f}_{j} e^{2 \pi i(j / n+1) k}\right] \\
& {\left[\frac{1}{n} \sum_{m=1}^{n} \hat{f}_{m} e^{2 \pi i\left(\frac{m}{n+1}\right) k}\right] } \\
= & \frac{1}{n^{2}} \sum_{k=1}^{n} \sum_{m=1}^{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{m} e^{2 \pi i\left(\frac{j+m}{n+1}\right)^{k}}
\end{aligned}
$$

From orthogonality of Fourier loasis

$$
\sum_{k=1}^{n} e^{2 \pi i\left(\frac{j+m}{n+1}\right)^{k}}=n \delta_{j,-m}
$$

where

$$
\delta_{j,-m}= \begin{cases}0 & j \neq m \\ 1 & -j=m\end{cases}
$$

It follows that

$$
\begin{aligned}
& \frac{1}{n^{2}} \sum_{k=1}^{n} \sum_{m=1}^{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{m} e^{2 \pi i\left(\frac{j+m}{n+1}\right)^{k}} \\
& =\frac{1}{n^{2}} \sum_{m=1}^{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{m}\left[\sum_{k=1}^{n} e^{2 \pi i\left(\frac{j+m}{n+1}\right)^{k}}\right] \\
& =\frac{1}{n^{2}} \sum_{m=1}^{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{m} n \delta_{j,-m} \\
& =\frac{1}{n} \sum_{j=1}^{n} \hat{f}_{j} \sum_{m=1}^{n} \hat{f}_{m} \delta_{j,-m} \\
& =\frac{1}{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{-j} \\
& =\frac{1}{n} \sum_{j=1}^{n} \hat{f}_{j} \hat{f}_{j}^{*} \\
& =\frac{1}{n} \sum_{j=1}^{n} 1 \hat{f}_{j} l^{2}
\end{aligned}
$$

Thus

$$
\sum_{k=1}^{n} x_{k}^{2}=\frac{1}{n} \sum_{j=1}^{n}\left|\hat{f}_{j}\right|^{2}
$$

This relation is used to normalize the power spectrum in the simulations

$$
\frac{1}{n \sum_{k=1}^{n} x_{k}^{2}} \sum_{j=1}^{n}\left|\hat{f}_{j}\right|^{2}=1
$$

The following plots show the results for two simulations For the first simulation $t l=08$ It is seen that the slope of the power spectrum is negative. The estimated value of H is close to the true value and is as accurate as the result dotamed using owriance
aggregation in a previous section. The first plots show the Fractional Brownian Noise time series and power spectrum,

Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.4$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-184.jpg?height=926&width=1386&top_left_y=650&top_left_x=124)

Fractional Brownian Noise Power Spectrum: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.8$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-185.jpg?height=870&width=1374&top_left_y=217&top_left_x=102)

The final plot shows the as fit to the power spectrum. The obtained result is comparable to the variace aggregation result.

Fractional Brownian Noise Power Spectrum: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.8, \mathrm{~N}=65536$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-186.jpg?height=849&width=1303&top_left_y=185&top_left_x=163)

The next plots show the result for a simclation with $H=0.4$. It is notable that for $H<1_{2}$ the slope of the powes spectum is positive.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-187.jpg?height=878&width=1280&top_left_y=114&top_left_x=167)

Fractional Brownian Noise Power Spectrum: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.4$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-187.jpg?height=819&width=1262&top_left_y=1082&top_left_x=165)

## The final plot shows the ols estimate,

Fractional Brownian Noise Power Spectrum: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.4, \mathrm{~N}=65536$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-188.jpg?height=825&width=1266&top_left_y=395&top_left_x=165)

## Hypothesis Testing

Hypothesis testing albws deasions to be mode about an analysis of a data sample. The proceedure consits of an assertion called the Null Hypothesis, usually denoted by $t_{0}$, and an atternative assertion, called the atternative thyothesis, usually denated by $H_{A}$. The Hypothesis Test performed on the data sample then decides whether $H_{0}$ or $H_{x}$ is accepted
An example of a null Hypothesis can be that the mean of the sumple is equal to some value and an atternative Hypothesis can be that the mean is less than that value.
Each Hypothesis test defines a test-statistic with a known distribution. The distribation
of the test-statistic takes into consideration random variations in the sample due to finite sample size.
A significance level is defined for the Hypothis Test, which specifies the probability that the Null Hypothesis is rejected and the alternative thyothis is acceted. Typical values for the significance level are 0.05 or 0.01.
The tests discussed here include:

## Chi-Squared Test

The Chi-Squared test is used to compare the frequencies of occurrence of a disorete set of events in a sample with a know multinomial distribution or with the
frequencies observed in another sample
I-Test
The $T$-Test is used to asmpare the mean value of a sample to a known value or to the mean value of another sample
ADF - Test
The Augmented-Dikey Fuller test is used to determine is a data sample can be modeled by a stationary random process
F-Test
The F-Test is used to dompare the variance of a sample to a Khoun value or to the variance of arother sample.

## Chi Square Test

Consider a normal random variable with mean and variance

$$
x \sim N\left(\mu, \sigma^{2}\right)
$$

Let

$$
z=\frac{(x-\mu)}{\sigma}
$$

then

$$
Z \sim N(0,1)
$$

let

$$
y=z^{2}
$$

what is the distribution of $y$ ? Recall the change of variable formula for a probability denstiy where

$$
y=g(2)
$$

namely

$$
f_{y}(y)=f_{2}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|
$$

where $s^{-1}(y)$ is the inverse of $g(x)$

$$
z=g^{-1}(y)
$$

Now $y>0$ by definition and

$$
y=z^{2} \Rightarrow z= \pm \sqrt{y}
$$

So

$$
\frac{d g^{-1}}{d y}(y)= \pm \frac{1}{2 \sqrt{y}}
$$

Since for each y value there are two 2 values so

$$
\begin{array}{r}
f_{y}(y)=f_{z}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|_{z=\sqrt{y}}+ \\
\quad f_{z}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|_{z=-\sqrt{y}}
\end{array}
$$

Now

$$
f_{2}(z)=\frac{1}{\sqrt{2 \pi}} e^{-z^{2} / 2}
$$

$f_{2}(z)$ is symetric so

$$
f_{2}(\sqrt{y})=f_{2}(-\sqrt{y})
$$

80

$$
f_{y}(y)=2 f_{x}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|_{x=\sqrt{y}}
$$

using

$$
\left|\frac{d g^{-1}(y)}{d y}\right|=\frac{1}{2 \sqrt{y}}
$$

gives

$$
f_{y}(y)=\frac{1}{\sqrt{2 \pi y}} e^{-y / 2}
$$

This distribution is the Chi-squared distribution with 1 degree of freedom.

The chi-squared distribution of two degrees of freedom is defined by

$$
y=z_{1}^{2}+z_{2}^{2}
$$

where $z_{1}$ and $z_{2}$ are two dentically distributed unit normal rardom variables

$$
\begin{aligned}
& Z_{1} \sim N(0,1) \\
& Z_{2} \sim N(0,1)
\end{aligned}
$$

Now define two random variables,

$$
\begin{aligned}
& \omega_{1}=z_{1}^{2} \\
& \omega_{2}=z_{2}^{2}
\end{aligned}
$$

thus $\omega_{1}$ and $\omega_{2}$ are two identically distributed independent chi-squared random variables

$$
f_{\omega}(\omega)=\frac{1}{\sqrt{2 \pi \omega}} e^{-\omega / 2}
$$

where

$$
y=\omega_{1}+\omega_{2}
$$

Now since $\omega_{1}$ and $\omega_{2}$ are independent

$$
f\left(\omega_{1}, \omega_{2}\right)=\frac{1}{2 \pi \sqrt{\omega_{1} \omega_{2}}} e^{-\left(\omega_{1}+\omega_{2}\right) / 2}
$$

Define two new random variables by

$$
\begin{aligned}
& A=\omega_{1} \omega_{2} \\
& B=\omega_{1}+\omega_{2}
\end{aligned}
$$

Now the two dimensional change of variables for probability/ density function is given by

$$
f(A, B)=f\left(\omega_{1}(A, B), \omega_{2}(A, B)\right)|J|
$$

where $|J|$ is the Jacobian matrix defined by

$$
\begin{aligned}
& |J|=\left|\frac{\partial\left(\omega_{1}, \omega_{2}\right)}{\partial(A, B)}\right|=\left|\begin{array}{ll}
\frac{\partial \omega_{1}}{d A} & \frac{\partial \omega_{1}}{\partial B} \\
\frac{\partial \omega_{2}}{\partial A} & \frac{\partial \omega_{3}}{\partial B}
\end{array}\right| \\
& =\left|\frac{\partial \omega_{1}}{\partial A} \frac{\partial \omega_{2}}{\partial B}-\frac{\partial \omega_{1}}{\partial B} \frac{\partial \omega_{2}}{\partial A}\right|
\end{aligned}
$$

To go furthure $\omega_{1}(A, B)$ and $\omega_{2}(A, B)$ are required,

$$
A=\omega_{1} \omega_{2} \quad B=\omega_{1}+\omega_{2}
$$

from the second equation

$$
B=\omega_{1}+\omega_{2} \Rightarrow \omega_{2}=B-\omega_{1}
$$

and

$$
\begin{aligned}
& A=\omega_{1} \omega_{2}=\left(B-\omega_{1}\right) \omega_{1} \\
\Rightarrow & \omega_{1}^{2}-\omega_{1} B+A=0 \\
\Rightarrow & \omega_{1}^{2}-\omega_{1} B+\frac{1}{4} B^{2}-\frac{1}{4} B^{2}+A=0 \\
\Rightarrow & \left(\omega_{1}-\frac{1}{2} B\right)^{2}=\frac{1}{4} B^{2}-A \\
\Rightarrow & \left(\omega_{1}-1 / 2 B\right)^{2}=\frac{1}{4}\left(B^{2}-4 A\right) \\
\Rightarrow & \omega_{1}-1 / 2 B= \pm \frac{1}{2} \sqrt{B^{2}-4 A} \\
\Rightarrow & \omega_{1}=\frac{1}{2}\left(B \pm \sqrt{B^{2}-4 A}\right)
\end{aligned}
$$

using

$$
\begin{aligned}
& B=\omega_{1}+\omega_{2} \Rightarrow \omega_{2}=B-\omega_{1} \\
\Rightarrow & \omega_{2}=\frac{1}{2}\left(B \mp \sqrt{B^{2}-4 A}\right)
\end{aligned}
$$

thus

$$
\begin{aligned}
& \omega_{1}=\frac{1}{2}\left(B \pm \sqrt{B^{2}-4 A}\right) \\
& \omega_{2}=\frac{1}{2}\left(B \mp \sqrt{B^{2}-4 A}\right)
\end{aligned}
$$

$\omega_{1}$ and $\omega_{2}$ are symmetric in the use of $\pm$. If $w$, uses - $\omega_{2}+$ and if $\omega_{1}$ uses + $\omega_{2}$ uses - Since their distributions are the same choosing one set of solutions is sufficiently general if the result is multiplied by 2. So it will be assumed that

$$
\begin{aligned}
& \omega_{1}=\frac{1}{2}\left(B+\sqrt{B^{2}-4 A}\right) \\
& \omega_{2}=\frac{1}{2}\left(B-\sqrt{B^{2}-4 A}\right)
\end{aligned}
$$

Next the Jacobian will be evaluated

$$
|J|=\left|\frac{\partial \omega_{1}}{\partial A} \frac{\partial \omega_{2}}{\partial B}-\frac{\partial \omega_{1}}{\partial B} \frac{\partial \omega_{2}}{\partial A}\right|
$$

50

$$
\begin{aligned}
\frac{\partial \omega_{1}}{\partial A} & =\frac{-4}{2} \frac{1}{2 \sqrt{B^{2}-4 A}} \\
& =\frac{-1}{\sqrt{B^{2}-4 A}} \\
\frac{\partial \omega_{2}}{\partial B} & =\frac{1}{2}\left[1-\frac{\partial B}{\sqrt{B^{2}-4 A}}\right] \\
& =\frac{1}{2}-\frac{B}{\sqrt{B^{2}-4 A}} \\
\frac{\partial \omega_{1}}{\partial B} & =\frac{1}{2}+\frac{B}{B^{2}-4 A} \\
\frac{\partial \omega_{2}}{\partial A} & =\frac{1}{\sqrt{B^{2}-4 A}}
\end{aligned}
$$

It follows that

$$
\begin{gathered}
|J|=\left|\frac{\partial \omega_{1}}{\partial A} \frac{\partial \omega_{2}}{\partial B}-\frac{\partial \omega_{1}}{\partial B} \frac{\partial \omega_{2}}{\partial A}\right| \\
\left.=\left\lvert\,\left(\frac{-1}{\sqrt{B^{2}-4 A}}\right) \neq \frac{1}{2}-\frac{B}{\sqrt{B^{2}-4 A}}\right.\right) \\
\left.-\left(\frac{1}{2}+\frac{B^{0}}{B^{2}-4 A}\right)\left(\frac{1}{\sqrt{B^{2}-4 A}}\right) \right\rvert\,
\end{gathered}
$$

$$
=\frac{1}{\sqrt{B^{2}-4 A}}
$$

Now $f(A, B)$ can be computed using

$$
\begin{aligned}
& A=\omega_{1} \omega_{2} \\
& B=\omega_{1}+\omega_{2}
\end{aligned}
$$

and

$$
f\left(\omega_{1}, \omega_{2}\right)=\frac{1}{2 \pi \sqrt{\omega_{1} \omega_{2}}} e^{-\left(\omega_{1}+\omega_{2}\right) / 2}
$$

gives, including the factor of 2

$$
\begin{aligned}
f(A, B) & =2 f\left(\omega_{1}(A, B), \omega_{2}(A, B)\right) \mid J l \\
= & \frac{\partial}{B^{2}-4 A} \frac{1}{2 \pi \sqrt{A}} e^{-B / 2} \\
= & \frac{1}{\pi \sqrt{A\left(B^{2}-4 A\right)}} e^{-B / 2}
\end{aligned}
$$

The desired result is obtained by integrating over $A$ to obtain the distribution of $B$
and recalling that

$$
B=\omega_{1}+\omega_{2}=z_{1}^{2}+z_{2}^{2}
$$

and noting that

$$
\begin{aligned}
& B^{2}-4 A>0 \\
\Rightarrow \quad & \frac{B^{2}}{4}>A
\end{aligned}
$$

so that result is real. Thus

$$
\begin{aligned}
& f(B)=\int_{0}^{B^{2} / 4} \frac{1}{\pi \sqrt{A\left(B^{2}-4 A\right)}} e^{-B / 2} d A \\
& =\frac{e^{-B / 2}}{\pi} \int_{0}^{B^{2} / 4} \frac{1}{\sqrt{A\left(B^{2}-4 A\right)}} d A
\end{aligned}
$$

making the change of variables

$$
A=\frac{B^{2}}{4} \sin ^{2} t
$$

$A=0 \Rightarrow t=0$
$A=\frac{B^{2}}{4} \Rightarrow \sin ^{2} t=1=\pi / 2$ and

$$
\begin{aligned}
& d A=\frac{B^{2}}{4}(2) \sin t \cos t \\
& \sqrt{A\left(B^{2}-4 A\right)}=\sqrt{\frac{B^{2}}{4} \sin ^{2} t\left(B^{2}-B^{2} \sin ^{2} t\right)} \\
= & \sqrt{\frac{B^{2}}{4} \sin ^{2} t B^{2}\left(1-\sin ^{2} t\right)} \\
= & \frac{B^{2}}{2} \sin t \cos t
\end{aligned}
$$

thus

$$
\begin{aligned}
S(B) & =\frac{e^{-B / 2}}{\pi} \int_{0}^{\pi / 2} d t \\
& =\frac{e^{-B / 2}}{\pi}\left(\frac{\pi}{2}\right) \\
& =\frac{e^{-B / 2}}{2}
\end{aligned}
$$

Thus the Chi squared distribution with 2 degrees of freedom
is given by, with

$$
\begin{aligned}
& y=z_{1}^{2}+z_{2}^{2} \\
& z_{1} \sim N(0,1) \quad z_{2} \sim N(0,1) \\
& f(y)=\frac{e^{-y}}{2}
\end{aligned}
$$

For $k$ degices of freedom let

$$
y=\sum_{i=1}^{k} z_{i}^{2}
$$

This expression defines a sphere in a $k$ dimensional space with radius $\sqrt{y}$.
Consider the probabildy of $y$ lying in a thin spherical shell of width $d y$ where $y$ is constant. Denote the volume of thin shell by $v$. Then
$f(y) d y=\frac{1}{(2 \pi)^{k / 2}} \int_{v} e^{-\left(z_{1}^{2}+z_{2}^{2}+\cdots z_{n}^{2}\right) / 2} d z_{1} d z_{2} \cdots d z_{n}$
since $y$ is constant

$$
y=z_{1}^{2}+z_{2}^{2}+\cdots z_{n}^{2}
$$

is a constant so

$$
f(y) d y=\frac{e^{-y / 2}}{(2 \pi)^{k / 2}} \int_{v} d z_{1} d z_{2} \cdots d z_{n} .
$$

The integral becomes the volume of a thin spherical shell in $k$ dimensions. The radius of the sphere is given by

$$
R=\sqrt{y}
$$

thus

$$
d R=\frac{1}{2 \sqrt{y}} d y
$$

The surface area of $a k$ dimensional hypersphere was
derived in the "Math / Geometry" notebook. The result obtained was

$$
A_{k-1}=\frac{k \pi^{k / 2}}{\Gamma(k / 2+1)} R^{k-1}
$$

A property of the Camma function is

$$
\Gamma(x+1)=x \Gamma(x)
$$

so

$$
\Gamma(k / 2+1)=\frac{1}{2} k \Gamma(k / 2)
$$

and

$$
A_{k-1}=\frac{2 R^{k-1} \pi^{k / 2}}{\Gamma(k / 2)}
$$

The volume of the shell is then

$$
V=A_{k-1} d R
$$

Thus

$$
\begin{aligned}
& f(y) d y=\frac{e^{-y / 2}}{(2 \pi)^{k / 2}} A_{k-1} d R \\
& =\frac{e^{-y / 2}}{(2 \pi)^{k / 2}} \frac{(2)^{\hat{( }(y)^{k-1} \pi^{k / 2}}}{\Gamma(k / 2)}\left(\frac{1}{2 \sqrt{y}}\right) d y \\
& =\frac{1}{2^{k / 2} \Gamma(k / 2)} y^{k / 2-1 / 2-1 / 2} e^{-y / 2} d y \\
& =\frac{1}{2^{k / 2} \Gamma(k / 2)} y^{k / 2-1} e^{-y / 2} d y
\end{aligned}
$$

and finally

$$
f(y)=\frac{1}{2^{k / 2} \Gamma\left(k_{1}\right)} y^{k / 2-1} e^{-y / 2}
$$

It is intercsting to compare the Chi-squared distribution to the Gamma distribution,

$$
g(x)=\frac{1}{\theta^{n} \Gamma(n)} x^{n-1} e^{-x / \theta}
$$

the mean and variance are given by

$$
\mu=n \theta \quad \sigma^{2}=n \theta^{2}
$$

Comparing with the chi-squared distribution, $f(y)$, above it is seen the the Chi-squared distribution is a Gamma distribution with parameters

$$
\theta=2 \quad n=k / 2
$$

The CDF of the chi-square $d$ distribution is given by

$$
\begin{aligned}
& P(I \leqslant y)=\int_{0}^{y} f(y) d y \\
& =\frac{1}{2^{k / 2} \Gamma\left(k_{2}\right)} \int_{0}^{y} t^{k / 2-1} e^{-t / 2} d y
\end{aligned}
$$

The lower incomple Camma function
is defined by

$$
\gamma(s, x)=\int_{0}^{x} t^{s-1} e^{-t} d t
$$

thus

$$
\gamma\left(\frac{1}{2} k, \frac{1}{2} x\right)=\int_{0}^{1 / 2 x} t^{\frac{1}{2} k-1} e^{-t} d t
$$

let

$$
\begin{aligned}
& \omega=2 t \Rightarrow \quad t=1 / 2 \omega \\
& \Rightarrow \quad d t=\frac{1}{2} \omega
\end{aligned}
$$

So

$$
\begin{aligned}
\gamma\left(\frac{1}{2} k, \frac{1}{2} x\right) & =\int_{0}^{x}\left(\frac{1}{2} \omega\right)^{1 / 2 k-1} e^{-\omega / 2} \frac{1}{2} d \omega \\
& =\frac{1}{2^{k / 2}} \int_{0}^{x} \omega^{k / 2-1} e^{-\omega / 2} d \omega
\end{aligned}
$$

It follows that the COF is given by

$$
P(\bar{x} \leqslant x)=\frac{\gamma\left(\frac{1}{2} k, \frac{1}{2} x\right)}{\Gamma(k / 2)}
$$

In summary the Chi-Squared PDF and CDF are given by

$$
\begin{aligned}
& f(y)=\frac{1}{2^{k / 2} \Gamma\left(k_{1}\right)} y^{k / 2-1} e^{-y / 2} \\
& P(\bar{x} \leqslant x)=\frac{\gamma\left(\frac{1}{2} k, \frac{1}{2} x\right)}{\Gamma(k / 2)}
\end{aligned}
$$

where $\gamma(1 / 2 k, 1 / 2 x)$ is the lower incomple camma function

$$
\gamma\left(\frac{1}{2} k, \frac{1}{2} x\right)=\frac{1}{2^{k / 2}} \int_{0}^{x} t^{k / 2-1} e^{-t / 2} d \omega
$$

The following plots show examples of the Chi-squared PDF, CDF and tail CDF, where

$$
C D F_{\text {tail }}=1-C D F
$$

for a range of degrees of freedom. It will be seen later the CDFtail is useful in hypothesis testing.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-210.jpg?height=551&width=769&top_left_y=100&top_left_x=427)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-210.jpg?height=551&width=767&top_left_y=765&top_left_x=477)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-210.jpg?height=545&width=775&top_left_y=1370&top_left_x=469)

## Properties of Chi-Squared Distribution

It the previous section it was shown that the random variable

$$
y=\sum_{i=1}^{k} z_{l}^{2}
$$

where $z_{i}$ are independent and identically distributed unit normal random variables,

$$
Z_{i} \sim N(0,1)
$$

has distribution

$$
f(y)=\frac{1}{2^{k / 2} \Gamma(k / 2)} y^{k / 2-1} e^{-y / 2}
$$

where $0<y<\infty$.
Now y can be writen as a sum of Chi-squared random variables with 1 degree of freedom

$$
\omega_{i}=z_{i}^{2}
$$

## where

## $\omega_{i} \sim x_{1}$

In fact any chi-squared random variable can by writen as a sum of chi-squared random variables where the number of degrees of freedom the sum is equal to the sum of the degrees of freedom.

The normalization of $f(y)$ is grven by
$\int_{0}^{\infty} f(y) d y=\frac{1}{2^{k / 2} \Gamma(k / 2)} \int_{0}^{\infty} y^{k / 2-1} e^{-y / 2} d y$
make the change of variables

$$
x=\frac{1}{2} \Rightarrow 2 d x=d y
$$

obtaining
$\int_{0}^{\infty} f(y) d y=\frac{1}{2^{k / 2} \Gamma(k / 2)} \int_{0}^{\infty}(2 x)^{k / 2-1} e^{-x} 2 d x$

$$
\begin{aligned}
& =\frac{2^{k / 2}}{2^{k / 2}} \frac{1}{\Gamma(k / 2)} \int_{0}^{\infty} x^{k / 2-1} e^{-x} d x \\
& =\frac{1}{\Gamma(k / 2)} \Gamma(k / 2)=1
\end{aligned}
$$

The mean is given by

$$
\begin{aligned}
\mu & =\int_{0}^{\infty} y f(y) d y \\
& =\frac{1}{2 k / 2} \Gamma(k / 2) \int_{0}^{\infty} y^{k / 2} e^{-y / 2} d y
\end{aligned}
$$

using indegration by parts

$$
\int u d v=u v-\int v d u
$$

let

$$
\begin{aligned}
& u=y^{k / 2} \Rightarrow d u=\frac{k}{2} y^{k / 2-1} d y \\
& d v=e^{-y / 2} d y \Rightarrow v=-2 e^{-y / 2}
\end{aligned}
$$

Thus

$$
\mu=\frac{1}{2 k_{12}} \Gamma\left(k_{12}\right) \int_{0}^{\infty} y^{k / 2} e^{-y / 2} d y
$$

$$
\begin{aligned}
& =\frac{1}{2^{k / 2} \Gamma(k / 2)}\left\{-\left.2 y^{k / 2} e^{-y / 2}\right|_{0} ^{\infty}\right. \\
& \left.-\int_{0}^{\infty}\left(\frac{k}{2} y^{k / 2-1}\right)\left(-2 e^{-y / 2}\right) d y\right\} \\
& =\frac{1}{2^{k / 2} \Gamma(k / 2)}\left\{0-0+k \int_{0}^{\infty} y^{k / 2-1} e^{-y / 2 d y}\right\} \\
& =\frac{k}{2^{k / 2} \Gamma(k / 2)} \int_{0}^{\infty} y^{k / 2-1} e^{-y / 2} d y \\
& =k \\
& \text { since } \\
& \int_{0}^{\infty} f(y) d y=\frac{1}{2^{k / 2} \Gamma(k / 2)} \int_{0}^{\infty} y^{k / 2-1} e^{-y / 2} d y \\
& =1
\end{aligned}
$$

The standard deviation is given by

$$
\sigma^{2}=E\left(y^{2}\right)-u^{2}
$$

50

$$
\begin{aligned}
& E\left(y^{2}\right)=\int_{0}^{\infty} y^{2} f(y) d y \\
= & \frac{1}{2^{k / 2} \Gamma\left(k_{2}\right)} \int_{0}^{\infty} y^{k / 2+1} e^{-y / 2} d y
\end{aligned}
$$

using integration by parts gives

$$
\int u d v=u v-\int v d u
$$

with

$$
\begin{aligned}
& u=y^{k / 2+1} \Rightarrow d u=(k / 2+1) y^{k / 2} d y \\
& d v=e^{-y / 2} d y \Rightarrow v=-2 e^{-y / 2}
\end{aligned}
$$

so that

$$
\begin{array}{rl}
\int_{0}^{\infty} y^{2} & f(y) d y=\frac{1}{2^{k / 2} \Gamma\left(k_{2}\right)}\left\{\left.y^{k / 2+1} e^{-y / 2}\right|_{0} ^{\infty}\right. \\
& \left.-\int_{0}^{\infty}(k / 2+1) y^{k / 2}\left(-2 e^{-y / 2}\right) d y\right\}
\end{array}
$$

$$
\begin{aligned}
& =\frac{1}{2^{k / 2} \Gamma(k / 2)}\left\{0-0+2(k / 2+1) \int_{0}^{\infty} y^{k / 2} e^{-y / 2} d y\right\} \\
& =\frac{2(k / 2+1)}{\partial^{k / 2} \Gamma\left(k^{k} / 2\right)} \int_{0}^{\infty} y^{k / 2} e^{-y / 2} d y
\end{aligned}
$$

but

$$
\mu=\frac{1}{2 k / 2} \Gamma(k / 2) \int_{0}^{\infty} y^{k / 2} e^{-y / 2} d y=k
$$

Thus

$$
E\left(y^{2}\right)=2(k / 2+1) k=k(k+2)
$$

it follows that the variance is given by

$$
\begin{aligned}
\sigma^{2} & =E\left(y^{2}\right)-\mu^{2} \\
& =k(k+2)-k^{2} \\
& =2 k
\end{aligned}
$$

In summary it has been shown that for the chi-squared distribution of $k$ degrees of freedom defined by

$$
f(y)=\frac{1}{2^{k / 2} \Gamma(k / 2)} y^{k / 2-1} e^{-y / 2}
$$

that

$$
\begin{aligned}
& \int_{0}^{\infty} f(y) d y=1 \\
& \mu=k \quad \delta^{2}=2 k
\end{aligned}
$$

## Multinomial Distribution

The multinomial distribution is defined by the probability mass function

$$
\begin{array}{r}
f\left(x_{1}, x_{2}, \ldots, x_{k}: n, p_{1}, p_{2} \ldots, p_{k}\right) \\
=\frac{n!}{x_{1}!x_{2}!\cdots x_{k}!} p_{1}^{x_{1}} p_{2}^{x_{2}} \cdots p_{k}^{x_{k}}
\end{array}
$$

where

$$
\begin{aligned}
& \sum_{i=1}^{k} x_{i}=n \\
& \sum_{i=1}^{k} p_{i}=1
\end{aligned}
$$

let

$$
\begin{aligned}
& x=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\} \\
& p=\left\{p_{1}, p_{2}, \ldots, p_{n}\right\}
\end{aligned}
$$

then the probability mass function can be written as

$$
f(x, n, p)=\frac{n!}{x_{1}!\cdot x_{2}!\cdots x_{n}!} p_{1}^{x_{1}} p_{2}^{x_{2}} \cdots p_{n}^{x_{3}}
$$

## Multinouli Distribution

The multinomial distribution can be decomposed inlo a sum of of vectors with multinoulli
distriputions. The multinoulli distribution is atso called the categorical
distribution. The multinoulli distribution is a generalization of the Bernoulli distribation to multiple outcomes. The Bernoulli random ariable takes on two values

$$
x=\{0,1\}
$$

in a single trial where the probability that $x=1$ and $x=0$ are given by

$$
P(x=1)=P \quad P(x=0)=1-P
$$

with $0 \leqslant p \leqslant 1$.

$$
\begin{aligned}
E(x) & =(1) p+(0)(1-p)=p \\
\operatorname{Var}(x) & =E\left(x^{2}\right)-E^{2}(x) \\
& =p-p^{2}=p(1-p)
\end{aligned}
$$

Thus for the Bernoulli distribution

$$
\begin{aligned}
& \mu=P \\
& \sigma^{2}=p(1-p)
\end{aligned}
$$

A multinoulli random variable can take on an arbitrary number of values in a single trial.
There are several constructions of the mutinaull random variable. one is to denote the number of values by $k$ and assume that the possible values are

$$
x=\{1,2,3, \ldots, k\}
$$

The probability of $x$ taking on value $i$ is given by

$$
f(x=i)=p_{i} \quad i=1,2,3, \ldots, k
$$

where

$$
\sum_{i=1}^{k} P_{i}=1
$$

## and

which depends on the values choosen for $x_{i}$.

Another construction, which does not have this issue and is more widely used defines $K$ categories labeled $1,2,3, \ldots, k$ the vector of probabilities

$$
P=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k}\right)
$$

and the random variable $x$ in a single trial takes on a value in the set of $k$ elements

$$
x \in\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{k}\right\} \quad i=1,2,3, \ldots, k
$$

where $x_{i}$ is a vector of length $k$ which is 1 at $c=j$ and zero otherwise,

$$
x_{i j}=\left\{\begin{array}{ll}
1 & i=j \\
0 & i \neq j
\end{array}=\delta_{i j}\right.
$$

It follows that the probability
mass function can be written as

$$
f\left(x_{i}, p\right)=\prod_{j=1}^{K} P_{j}^{x_{i j}}=\prod_{j=1}^{K} P_{j}^{\delta_{i j}}=P_{i}
$$

This form is used in the construction of the multinomial distributions.
The mean of $x$ is given by

$$
\begin{aligned}
& E(x)=\sum_{i=1}^{K} x_{i} P_{i}=(1,0,0, \ldots, 0) P_{1} \\
& +(0,1,0, \ldots, 0) P_{2}+(0,0,1, \ldots, 0) P_{3} \\
& +(0,0,0, \ldots, 1) P_{k}=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k}\right) \\
& =P
\end{aligned}
$$

thus

$$
E(x)=P
$$

or equiociently

$$
E\left(x_{i}\right)=\rho_{i}
$$

Next the Covariance is
defined by
$\operatorname{Coo}\left(x_{i} x_{j}\right)=E\left(x_{i} x_{j}\right) \cdot E\left(x_{i}\right) E\left(x_{j}\right)$
First consider the case $i=j$

$$
\begin{aligned}
\operatorname{var}\left(x_{i}\right) & =\operatorname{cov}\left(x_{i} x_{i}\right) \\
& =E\left(x_{i}^{2}\right)-E\left(x_{i}\right)^{2}
\end{aligned}
$$

Now $x_{i}=1$ or 0 so

$$
E\left(x_{i}^{2}\right)=E\left(x_{i}\right)
$$

and

$$
E\left(x_{i}\right)=P_{i}
$$

thus

$$
\begin{aligned}
\operatorname{var}\left(x_{i}\right) & =\operatorname{cov}\left(x_{i} x_{i}\right) \\
& =E\left(x_{i}\right)-E\left(x_{i}\right)^{2} \\
& =p_{i}-p_{i}^{2} \\
& =p_{i}\left(1-p_{i}\right)
\end{aligned}
$$

Now for $i \neq j$ one of $x_{i}$ or
$x_{j}$ will be 0 so $x_{i} x_{j}=0$. It follows that

$$
\begin{aligned}
\operatorname{Cov}\left(x_{i} x_{j}\right) & =E\left(x_{i} x_{j}\right)-E\left(x_{i}\right) E\left(x_{j}\right) \\
& =-P_{i} P_{j}
\end{aligned}
$$

It follows that

$$
\operatorname{Cov}\left(X_{i} X_{j}\right)=P_{i} \delta_{i j}-P_{i} P_{j}
$$

In summary

$$
\begin{aligned}
E\left(x_{i}\right) & =P_{i} \\
\operatorname{Cov}\left(x_{i} x_{j}\right) & =P_{i} \delta_{i j}-P_{i} P_{j}
\end{aligned}
$$

Multinomial Random variable as sum of Multinoulli Random variables

Denote a muttinomial random vanable by
$y \sim$ muttinomial $(n, p)$
where

$$
\begin{gathered}
p=\left(p_{1}, p_{2}, \ldots, p_{k}\right) \\
y \in\left\{y_{1}, y_{2}, \ldots, y_{k}\right\} \\
f(y, n, p)=\frac{n!}{y_{1}!y_{2}!\cdots y_{k}!} p_{1}^{y_{1}} p_{2}^{y_{2}} \cdots p_{n}^{y_{k}}
\end{gathered}
$$

where $y_{i}$ denoled the number of relizations occuring with probability $P_{i}$.
First consider the case $n=1$. If this is the case
$y \sim$ multinomial $(1, P)$
with probability mass function

$$
f(y, 1, p)=\frac{1}{y_{1}!y_{2}!\cdots y_{k}!} p_{1}^{y_{1}} p_{2}^{y_{2}} \cdots p_{n}^{y_{k}}
$$

so 1 event occurs and $y$ will be a vector of length $k$ where

$$
l=\sum_{i=1}^{k} y_{i}
$$

if for all $i, y_{i}>0$, it follows that for one value of $i \quad y_{i}=1$ and for the others $y_{i}=0$. Thus $y$ has the form of a multinouli event vector. vext it follows that

$$
\frac{1}{y_{1}!y_{2}!\cdots y_{k}!}=1
$$

thus the probability mass function is given by

$$
f(y, 1, p)=\prod_{i=1}^{k} p^{y_{i}}
$$

which is the multinaulli probability mass function thus
$y \sim$ multinomial $(1, p)$
has a multinoulli distribution.
Just as the binomial distribution is constructed a sum of Bernoulli random variables The muttinomial distribution can be constucted from a sum of Muttinoulli random variables. It has just been shown that a single multinomial trial denoted by

$$
\text { muttinomial }(1, p)
$$

justifing this assertion. To proceed consider the muttinalli random variable $x$ densting occurrence
of an event with with probablility $P$, where

$$
x \in\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{k}\right\}
$$

and $x_{i}$ is a vector of length $k$ satisfying, $x_{i j}=\delta_{i j}$
Now write the multinomial random variable, $y$, as a sum of $n$ trials of $x$

$$
y=x_{1}+x_{2}+\cdots+x_{n}
$$

y will be a vector

$$
y=\left(y_{1}, y_{2}, y_{3}, \ldots, y_{k}\right)
$$

where the elements are the total number of times each multinoulli event occured in the $n$ trials. That is $y_{1}$ will count the number of times the first element is 1 in the multinoulli outcome vector, $y_{z}$ the number of times the
second element is 1 , and so on up to $y_{k}$ counting the number of times the k'th element is 1 in the multinoulli outcome vector. It follows that

$$
n=\sum_{i=1}^{n} y_{i}
$$

Each realization of a term in the muttinoulli sum will occur with probability

$$
p^{y_{1}} p^{y_{2}} \cdots p^{y_{k}}
$$

The number of different ways that the sum can be constucted that are indistinguishable is given by the multinomial coefficient which counts the number of ways $n$ abjects can be partitioned into

$$
\left\{y_{1}, y_{2}, y_{3}, \ldots, y_{k}\right\}
$$

objects and is given by

$$
\frac{n!}{y_{1}!y_{2}!\cdots y_{k}!}
$$

It follows that for

$$
y=x_{1}+x_{2}+x_{3}+\cdots+x_{n}
$$

where the $x_{i}$ are dentically distributed multinoulli radom uariables the probability mass function for $y$ is given by.

$$
f(y)=\frac{n!}{y_{1}^{\prime} \cdot y_{2}^{\prime} \cdot \cdots y_{k}!} p_{1}^{y_{1}} p_{2}^{y_{2}} \cdots p_{k}^{y_{k}}
$$

proving that a sum of $n$ identically distributed muttinouli random variables nas a multinomial distribution.

## Mean and Variance of Muttinomial Distribution

The mean and covariance of the muttinomial distribution are now easily computed using the previous results obtained for the multinoulli distribution.

For the mean

$$
\begin{aligned}
E(y) & =E\left(\sum_{i=1}^{n} x_{i}\right) \\
& =\sum_{i=1}^{n} E\left(x_{i}\right) \\
& =\sum_{i=1}^{n} E(x) \\
& =n p
\end{aligned}
$$

Since the $X_{i}$ are identically distributed so for each $i$.

$$
E(x)=P
$$

Similarly the covariance matrix is given by

$$
\begin{aligned}
\operatorname{cov}(y) & =\operatorname{cov}\left(\sum_{i=1}^{n} x_{i}\right) \\
& =\sum_{i=1}^{n} \operatorname{cov}\left(x_{i}\right) \\
& =n \operatorname{cov}(x)
\end{aligned}
$$

where the second step follows from the assumed independence of $X_{i}$ and the second because the are dentically distributed.
In summary the mean and coorriance of the muttinomial distribution are given by,
$y \sim$ multinomial $(n, p)$

$$
E(y)=n p
$$

$$
\operatorname{Cov}\left(y_{i} y_{j}\right)=n\left(p_{i} \delta_{i j}-p_{i} p_{j}\right)
$$

## Pearson's Chi-Square Test statistic

Consider $n$ independent trials of a random variable $x$

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

where $x$ is a category $k$-vector of length $k$ assumed to have a multinoulli distribution,

$$
x_{i} \sim \text { multinomial }(1, P)
$$

with

$$
P=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k}\right)
$$

since the $x_{i}$ are category vectors of length $k$ there $k$ possible values for $x_{i}$, namely

$$
\begin{array}{ccc}
1 & (1,0,0, \ldots, 0) \\
2 & (0,1,0, \ldots, 0) \\
3 & (0,0,1, \ldots, 0) \\
k & (0,0,0, \ldots, 1)
\end{array}
$$

Denote the $j$ th component of $x_{i}$ by $x_{i j}$ then

$$
P\left(x_{i j}=1\right)=1-P\left(x_{i j}=0\right)=P_{j}
$$

It was previously shown that for the multinoulli distribution assuming the values of category vectors that

$$
\begin{aligned}
E\left(X_{i}\right) & =P \\
\Rightarrow E\left(X_{i j}\right) & =P_{j}
\end{aligned}
$$

and

$$
\operatorname{Cov}\left(X_{i j} X_{i l}\right)=\Sigma_{j l}=P_{j} \delta_{j l}-P_{j} P_{l}
$$

so the covariance matrix is given by

$$
\left(\begin{array}{cccc}
P_{1}\left(1-P_{1}\right) & -P_{1} P_{2} & -P_{1} P_{3} & \cdots \\
-P_{2} P_{1} & P_{2}\left(1-P_{2}\right) & -P_{2} P_{3} & \cdots \\
\vdots & \vdots & & \\
-P_{k} P_{1} & -P_{k} P_{2} & -P_{k} P_{3} & \cdots
\end{array}\right)
$$

Define the Pearson chi-square statistic by

$$
x^{2}=\sum_{j=1}^{k} \frac{\left(n j-n P_{j}\right)^{2}}{n P_{j}}
$$

where $n_{j}$ is the number of vectors with a 1 at position $j$ indicating success in the J'th category. The statistic provides a measure of the deviations of trial from the result expected for a muttinoulli distribution,

$$
E\left(n_{j}\right)=n p_{j}
$$

It will be shown that the test statistic asymtotically approaches a chi-squared for large $n$.
Denole the average value of component $j$ of $x$ over the $n$ trials by, $\bar{x}_{n}^{j}$, then

$$
\bar{x}_{n}^{j}=\frac{1}{n} \sum_{i=1}^{n} x_{i}^{j}
$$

where $x_{i}^{j}$ is the value of component $j$ for trial $i$. The average of the vector is given by

$$
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

For the multinoulli distribution

$$
E(x)=P
$$

from the central limit theorem it follows that as $n$ increases

$$
\sqrt{n}\left(\bar{x}_{n}-p\right) \xrightarrow{d} N(0, \Sigma)
$$

that is $\sqrt{n}\left(\bar{x}_{n}-p\right)$ approaches a muttivariate normal distribution with covariance matrix $\Sigma$.
A complication is that $\Sigma$ is not invertable since the sum over any column is
zero implying that the covoriace matrix is inearly dependent.

$$
\begin{gathered}
\sum_{l=1}^{K} P_{j} \delta_{j l}-P_{j} P_{l}=P_{j}-P_{j}\left(\sum_{l=1}^{K} P_{l}\right) \\
=P_{j}-P_{j}=0
\end{gathered}
$$

since

$$
\sum_{e=1}^{K} P_{e}=1
$$

To get around this problem define the vector $y_{i}$ as the first $k-1$ components of $x_{i j}$

$$
y_{i}=\left(x_{i 1}, x_{i 2}, x_{i 3}, \ldots, x_{i, k-1}\right)
$$

The covariance matrix for $y_{i}$ is the upper left portion of $\Sigma$ ignoring the $k$ 'th column and row. Denote this covariance matrix by $\Sigma^{*}$ similarly let $p^{*}$ denote the first k-l elements
of $P$,

$$
P^{*}=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k-1}\right)
$$

Now consider the matrix
$\Delta=\left(\begin{array}{cccc}\frac{1}{P_{1}}+\frac{1}{P_{k}} & \frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \frac{1}{P_{k}} & \frac{1}{P_{2}}+\frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \vdots & \vdots & \ddots & \\ \frac{1}{P_{k}} & \frac{1}{P_{k}} & & \frac{1}{P_{k}-1}+\frac{1}{P_{k}}\end{array}\right)$
and
$\Delta \Sigma^{*}=\left(\begin{array}{cccc}\frac{1}{P_{1}}+\frac{1}{P_{k}} & \frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \frac{1}{P_{k}} & \frac{1}{P_{2}}+\frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \vdots & \vdots & \ddots & \\ \frac{1}{P_{k}} & \frac{1}{P_{k}} & & \frac{1}{P_{k-1}}+\frac{1}{P_{k}}\end{array}\right)$

$$
\left(\begin{array}{cccc}
P_{1}\left(1-P_{1}\right) & -P_{1} P_{2} & -P_{1} P_{3} & \cdots \\
-P_{2} P_{1} & P_{2}\left(1-P_{2}\right) & -P_{2} P_{3} & \cdots \\
\vdots & \vdots & \vdots & -P_{2} P_{k-1} \\
-P_{k-1} P_{1} & -P_{k-1} P_{2} & -P_{k-1} P_{3} & \cdots \\
P_{k-1}\left(1-P_{k-1}\right)
\end{array}\right)
$$

The first element in the first row of the product is given by

$$
\begin{aligned}
& P_{1}\left(1-P_{1}\right)\left(\frac{1}{P_{1}}+\frac{1}{P_{k}}\right)-\frac{1}{P_{k}}\left(\sum_{i=2}^{k-1} P_{1} P_{i}\right) \\
= & \frac{P_{1}\left(1-P_{1}\right)}{P_{1}}+\frac{1}{P_{k}} P_{1}\left(1-P_{1}\right)-\frac{P_{1}}{P_{k}}\left(\sum_{i=2}^{k-1} P_{i}\right) \\
= & 1-P_{1}+\frac{P_{1}}{P_{k}}\left(1-P_{1}\right)-\frac{P_{1}}{P_{k}}\left(\sum_{i=2}^{k-1} P_{i}\right)
\end{aligned}
$$

Now

$$
\sum_{i=2}^{k-1} P_{i}=1-P_{k}-P_{1}
$$

80

$$
\begin{aligned}
& \left.1-p_{1}+\frac{p_{1}}{p_{k}}\left(\hat{1}-p_{1}\right)-\frac{p_{1}}{p_{k}} \hat{1}-p_{k}-p_{1}\right) \\
& =1-\hat{p}_{1}-\frac{p_{1}^{2}}{p_{k}}+\bar{p}_{1}+\frac{p_{1}^{2}}{p_{k}} \\
& =1
\end{aligned}
$$

It follows that for any diagonal element of the product

$$
P_{j}\left(1-P_{j}\right)\left(\frac{1}{P_{j}}+\frac{1}{P_{k}}\right)-\frac{1}{P_{k}}\left(\sum_{i \neq j}^{k-1} P_{j} P_{i}\right)
$$

but

$$
\begin{aligned}
& \sum_{i \neq j}^{k-1} P_{j} P_{i}=P_{j} \sum_{i \neq j}^{k-1} P_{i} \\
= & P_{j}\left(1-P_{k}-P_{j}\right)
\end{aligned}
$$

so the above expression becomes

$$
\begin{aligned}
& 1-P_{j}+P_{p_{k}}\left(1-P_{j}\right)-P_{p_{k}}\left(1-P_{k}-P_{j}\right) \\
& 1-P_{j}^{\prime}+P_{p_{k}}\left(1-P_{j}\right)-P_{p_{k}}^{*}\left(1-P_{j}\right)+P_{j}
\end{aligned}
$$

$$
=1
$$

for an off diagonal element consider $i=1, j=2$
$-P_{1} P_{2}\left(\frac{1}{P_{1}}+\frac{1}{P_{k}}\right)+P_{\frac{1}{P}}\left(1-P_{2}\right)-P_{2} \sum_{l=3}^{k-1} P_{l}$
Now $\sum_{l=3}^{k-1} P_{l}=1-P_{1}-P_{2}-P_{k}$
So

$$
\begin{aligned}
- & P_{1} P_{2}\left(\frac{1}{P_{1}}+\frac{1}{P_{k}}\right)+\frac{P_{2}}{P_{k}}\left(1-P_{2}\right)-\frac{P_{2}}{P_{k}}\left(1-P_{1}-P_{2}-P_{k}\right) \\
= & -P_{1} P_{2}\left(\frac{1}{P_{1}}+\frac{1}{P_{k}}\right)+\frac{P_{2}}{P_{k}}\left(1-P_{2}\right)-\frac{P_{2}}{P_{k}}\left(1-P_{2}\right) \\
& +\frac{P_{2}}{P_{k}}\left(P_{1}+P_{k}\right) \\
= & -P_{2}-\frac{P_{1} P_{2}}{P_{k}}+\frac{P_{2}}{P_{k}}\left(1-P_{2}\right)-\frac{P_{2}}{P_{k}}\left(1-P_{2}\right) \\
& +\frac{P_{2} P_{1}}{P_{k}}+P_{2}=0
\end{aligned}
$$

It follows that for any off diagonal element $i \neq j$
$-P_{i} P_{j}\left(\frac{1}{P_{i}}+\frac{1}{P_{k}}\right)+\frac{P_{k}}{P_{k}}\left(1-P_{j}\right)-P_{\frac{1}{P_{k}}} \sum_{\substack{l=1 \\ l \neq j}}^{k-1} P_{l}$
for the last term

$$
\sum_{l \neq i}^{k-1} P_{l}=1-P_{k}-P_{i}-P_{j}
$$

substitution into the previous expression gives

$$
\begin{aligned}
- & P_{j}-\frac{P_{i} P_{j}}{P_{k}}+P_{i}\left(1-P_{j}\right)-P_{j}\left(1-P_{k}-P_{i}-P_{j}\right) \\
= & -P_{j}-P_{\frac{i}{P_{k}}}+P_{j}+P_{j}\left(1-P_{j}\right)-P_{j}\left(1-P_{j}\right) \\
& +P_{P_{k}}+P_{\frac{i}{P_{k}}} \\
= & 0
\end{aligned}
$$

It follows that

$$
\Delta \Sigma^{*}=\mathbb{1}
$$

Where 11 is the identity matrix. Thus

$$
\Delta=\left(\Sigma^{*}\right)^{-1}
$$

Next consider the product

$$
n\left(\bar{y}-p^{*}\right)^{\top}\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-p^{*}\right)
$$

$\left(\Sigma^{*}\right)^{-1}=\left(\begin{array}{cccc}\frac{1}{P_{1}}+\frac{1}{P_{k}} & \frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \frac{1}{P_{k}} & \frac{1}{P_{2}}+\frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \vdots & \vdots & \ddots & \\ \frac{1}{P_{k}} & \frac{1}{P_{k}} & & \frac{1}{P_{k-1}}+\frac{1}{P_{k}}\end{array}\right)$
Now $\quad \bar{y}-P^{*}=\left(\begin{array}{c}\frac{1}{n} \sum_{i=1}^{n} x_{i 1}-P_{1} \\ \frac{1}{n} \sum_{i=1}^{n} x_{i 2}-P_{2} \\ \vdots \\ \frac{1}{n} \sum_{i=1}^{n} x_{i, k-1}-P_{k-1}\end{array}\right)$
noting that the number of occurances of $X_{j}$ in $n$ trials is given by

$$
\sum_{i=i}^{n} x_{i j}=n_{j}
$$

then

$$
\bar{Y}-P^{*}=\left(\begin{array}{c}
\frac{n_{1}}{n}-P_{1} \\
\frac{n_{2}}{n}-P_{2} \\
\vdots \\
\frac{n_{k-1}}{n}-P_{k-1}
\end{array}\right)
$$

so

$$
\frac{1}{P_{1}}+\frac{1}{P_{k}} \frac{1}{P_{k}} \cdots \frac{1}{P_{k}}
$$

$\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-P^{*}\right)=\left(\begin{array}{cccc}\frac{1}{P_{k}} & \frac{1}{P_{2}}+\frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \vdots & \vdots & \ddots & \\ \frac{1}{P_{k}} & \frac{1}{P_{k}} & & \frac{1}{P_{k-1}}+\frac{1}{P_{k}}\end{array}\right)$

$$
\left(\begin{array}{c}
\frac{n_{1}}{n}-P_{1} \\
\frac{n_{2}}{n}-P_{2} \\
\vdots \\
\frac{n_{k-1}}{n}-P_{k-1}
\end{array}\right)
$$

For the first element

$$
\begin{aligned}
& \left(\frac{1}{P_{1}}+\frac{1}{P_{k}}\right)\left(\frac{n_{1}}{n}-P_{1}\right)+\frac{1}{P_{k}} \sum_{j=2}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
& =\frac{1}{P_{1}}\left(\frac{n_{1}}{n}-P_{1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)
\end{aligned}
$$

and for the l'th element

$$
\begin{aligned}
& \left(\frac{1}{P_{l}}+\frac{1}{P_{k}}\right)\left(\frac{n_{l}}{n}-P_{l}\right)+\frac{1}{P_{k}} \sum_{j \neq l}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
& =\frac{1}{P_{l}}\left(\frac{n_{l}}{n}-P_{l}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)
\end{aligned}
$$

Thus
$\left(\Sigma^{*}\right)^{-1}\left(\bar{y} \cdot \bar{p}^{*}\right)=$

$$
\left(\begin{array}{c}
\frac{1}{P_{1}}\left(\frac{n_{1}}{n}-P_{1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
\frac{1}{P_{2}}\left(\frac{n_{2}}{n}-P_{2}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
\vdots \\
\frac{1}{P_{k-1}}\left(\frac{n_{k-1}}{n}-P_{k-1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)
\end{array}\right)
$$

Finally

$$
\begin{aligned}
& \left(\bar{y}-p^{*}\right)^{\top}\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-p^{*}\right) \\
& =\left(\frac{n_{1}}{n}-p_{1} \frac{n_{2}}{n}-p_{2} \ldots \frac{n_{k}-1}{n}-p_{(-1}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \left(\begin{array}{c}
\frac{1}{P_{1}}\left(\frac{n_{1}}{n}-P_{1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
\frac{1}{P_{2}}\left(\frac{n_{2}}{n}-P_{2}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \\
\vdots \\
\frac{1}{P_{k-1}}\left(\frac{n_{k-1}}{n}-P_{k-1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)
\end{array}\right) \\
& =\left(\frac{n_{1}}{n}-P_{1}\right)\left[\frac{1}{P_{1}}\left(\frac{n_{1}}{n}-P_{1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)\right] \\
& +\left(\frac{n_{2}}{n}-P_{2}\right)\left[\frac{1}{P_{2}}\left(\frac{n_{2}}{n}-P_{2}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)\right] \\
& +\cdots \\
& +\left(\frac{n_{k-1}}{n}-P_{k-1}\right)\left[\frac{1}{P_{k-1}}\left(\frac{n_{k-1}}{n}-P_{k-1}\right)+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)\right] \\
& =\frac{1}{P_{1}}\left(\frac{n_{1}}{n}-P_{1}\right)^{2}+\frac{1}{P_{2}}\left(\frac{n_{2}}{n}-P_{2}\right)^{2}+\cdots \\
& +\frac{1}{P_{k-1}}\left(\frac{n_{k-1}}{n-1}-P_{k-1}\right)^{2}+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right)[
\end{aligned}
$$

$$
\begin{aligned}
&\left.\left(\frac{n_{1}}{n}-P_{1}\right)+\left(\frac{n_{l}}{n}-P_{2}\right)+\cdots+\left(\frac{n_{k-1}}{n}-P_{k-1}\right)\right] \\
&=\sum_{j=1}^{k-1} \frac{1}{P_{j}}\left(\frac{n_{i}}{n}-P_{j}\right)^{2} \\
&+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \sum_{l=1}^{k-1}\left(\frac{n_{l}}{n}-P_{l}\right)
\end{aligned}
$$

Now consider the righthand side sums

$$
\sum_{j=1}^{k-1}\left(n_{i}-P_{j}\right)=\frac{1}{n} \sum_{j=1}^{k-1} n_{j}-\sum_{j=1}^{k-1} P_{j}
$$

but

$$
\begin{aligned}
& \sum_{j=1}^{k-1} n_{j}=n-n_{k} \\
& \sum_{j=1}^{k-1} p_{j}=1-p_{k}
\end{aligned}
$$

then

$$
\begin{aligned}
& \sum_{j=1}^{k-1}\left(\frac{n_{1}}{n}-P_{j}\right)=\frac{1}{n}\left(\hat{n}^{2}-n_{k}\right)-Y_{+} P_{k} \\
& =-\left(\frac{n_{k}}{n}-P_{k}\right)
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
& \left(\bar{y}-P^{*}\right)^{\top}\left(\sum^{*}\right)^{-1}\left(\bar{y}-P^{*}\right) \\
& =\sum_{j=1}^{k-1} \frac{1}{P_{j}}\left(\frac{n_{i}}{n}-P_{j}\right)^{2} \\
& \quad+\frac{1}{P_{k}} \sum_{j=1}^{k-1}\left(\frac{n_{j}}{n}-P_{j}\right) \sum_{l=1}^{k-1}\left(\frac{n_{l}}{n}-P_{l}\right) \\
& =\sum_{j=1}^{k-1} \frac{1}{P_{j}}\left(\frac{n_{i}}{n}-P_{j}\right)^{2}+\frac{1}{P_{k}}\left(\frac{n_{k}}{n}-P_{k}\right)^{2} \\
& =\sum_{j=1}^{k} \frac{1}{P_{j}}\left(\frac{n_{j}}{n}-P_{j}\right)^{2} \\
& =\frac{1}{n^{2}} \sum_{j=1}^{k} \frac{1}{P_{j}}\left(n_{j}-n P_{j}\right)^{2}
\end{aligned}
$$

Recall that the proposed $x^{2}$ statistic

$$
x^{2}=\sum_{j=1}^{k} \frac{\left(n_{j}-n P_{j}\right)^{2}}{n P_{j}}
$$

It follows that

$$
x^{2}=n\left(\bar{y}-p^{*}\right)^{\top}\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-p^{*}\right)
$$

To determine the distribution of $y^{2}$ note that

$$
z_{n}=\sqrt{n}\left(\Sigma^{*}\right)^{-1 / 2}\left(\bar{y}-p^{*}\right)
$$

and from the central limit theorem it follows that assymtotically for large $n$

$$
Z_{n} \rightarrow N(0, \mathbb{1})
$$

Thus $x^{2}$ is a sum of squares of unit normal random variables which is a chi-squared distribution with $k-1$ degrees of freedom

$$
x^{2}=z_{n}^{\top} z_{n} \xrightarrow{c} x^{2}(k-1)
$$

## Summany of Results of Pearson's Chi-Squared Test

The argument prooing Pearson's Oni-squared test was complicated so it will be summarized here.
Consider $n$ independent and dentically distributed trials of a Multinoulli random variable with $K$ different out comes.

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

A Muttinoulli random variable is also called a categorical random variable. The distribution is densted by

$$
x \sim \text { multinomial }(1, p)
$$

indicating that the multinoulli randsm variable has the same distribution as a single muttinomial event.

If the probability of occurand of each outcome of the random variable is denoted by the vector

$$
P=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k}\right)
$$

and the $K$ possible outcomes of $x$ by the actegory vectors since the $x_{i}$ are category vectors of lencth $k$ there $k$ possible values for $x_{i}$, namely

$$
\begin{array}{ccc}
1 & (1,0,0, \ldots, 0) \\
2 & (0,1,0, \ldots, 0) \\
3 & (0,0,1, \ldots, 0) \\
k & (0,0,0, \ldots, 1)
\end{array}
$$

The mean of $x$ is given by

$$
E(x)=\rho
$$

and the covariance matorix is given by
$\Sigma=\left(\begin{array}{ccccc}P_{1}\left(1-P_{1}\right) & -P_{1} P_{2} & -P_{1} P_{3} & \cdots & -P_{1} P_{k} \\ -P_{2} P_{1} & P_{2}\left(1-P_{2}\right) & -P_{2} P_{3} & \cdots & -P_{2} P_{k} \\ \vdots & & & & \\ -P_{k} P_{1} & -P_{k} P_{2} & -P_{k} P_{3} & \cdots & P_{k}\left(1-P_{k}\right)\end{array}\right)$
The Pearson Chi-squared test statistic is defined by

$$
x^{2}=\sum_{j=1}^{k} \frac{\left(n j-n p_{j}\right)^{2}}{n p_{j}}
$$

where $n$ is the total number of trials and $n_{j}$ is the total number of outcomes with probability PJ.
It is desired to show that the test parameter $x^{2}$ does infact approach a chi-squared distribution as the number of trials becomes large.

To accomplish this the cental limit theorem is used the evaluate the limiting distribution of the $n$ trials obtaining

$$
\sqrt{n}\left(\bar{x}_{n}-p\right) \xrightarrow{d} N(0, \Sigma)
$$

where is the average value of $x$ computed from the $n$ trials

$$
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

Next it is desired to find an expression for the $x^{2}$ test statistic in terms of the distribution parameters an thus deduce the distribution of the test statistic. To accomplish this the inverse of the coveriance matrix is required. It twons out $\Sigma$ is not invertable. It is shown
that the matrix $\Sigma^{*}$ which consists of upper left portion of $\sum$ with row and colum indicles lying between 1 and $k-1$ is invertale and has inverse
$\left(\Sigma^{*}\right)^{-1}=\left(\begin{array}{cccc}\frac{1}{P_{1}}+\frac{1}{P_{k}} & \frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \frac{1}{P_{k}} & \frac{1}{P_{2}}+\frac{1}{P_{k}} & \cdots & \frac{1}{P_{k}} \\ \vdots & \vdots & \ddots & \\ \frac{1}{P_{k}} & \frac{1}{P_{k}} & & \frac{1}{P_{k-1}}+\frac{1}{P_{k}}\end{array}\right)$
Next truncated versons of $P$ and $x$ are introduced that exclude the $k$ 'th component

$$
\begin{aligned}
& p^{*}=\left(p_{1}, p_{2}, p_{3}, \ldots, p_{k-1}\right) \\
& y=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{k-1}\right)
\end{aligned}
$$

and the following expression is evaluated

$$
n\left(\bar{y}-p^{*}\right)^{\top}\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-p^{*}\right)
$$

This expression is the argument of the limiting normal distribution of the multinoulli distribution obtained previously by application of the central limit theorem but using the truncated parameters. It is next shown that

$$
\begin{aligned}
x^{2} & =\sum_{j=1}^{k} \frac{\left(n_{j}-n p_{j}\right)^{2}}{n p_{j}} \\
& =n\left(\bar{y}-p^{*}\right)^{\top}\left(\Sigma^{*}\right)^{-1}\left(\bar{y}-p^{*}\right)
\end{aligned}
$$

It is then shown that $x^{2}$ has a chi-squared distribution with $K-L$ degrees of freedom,

$$
x^{2} \sim x^{2} k-1
$$

since the expression for $x^{2}$ is a sum of squares of unit normal random variables

## Chi-Squared Test Example

Previously it was shown that the chi-squared test statistic for a multinowli random variable, $x$,

$$
x \sim \text { multinomial }(1, P)
$$

with probability vector

$$
P=\left(P_{1}, P_{2}, P_{3}, \ldots, P_{k}\right)
$$

and ategory vector outcomes, $x_{1}, x_{2}, x_{3}, \ldots, x_{k}$

$$
\begin{aligned}
& x_{1}=(1,0,0, \cdots, 0) \\
& x_{2}=(0,1,0, \cdots, 0) \\
& x_{3}=(0,0,1, \cdots, 0) \\
& \vdots \\
& x_{k}=(0,0,0, \cdots, 1)
\end{aligned}
$$

is given by

$$
x^{2}=\sum_{i=1}^{k} \frac{\left(n_{i}-n_{p_{i}}\right)^{2}}{n_{p_{i}}}
$$

and has a chi-squared distribution with $k-1$ degrees of freedom

$$
x^{2} \sim x_{k-1}^{2}
$$

where $n$ is the total number of trials and $n_{i}$ is the number of occurances of outcome $x_{i}$ with probability $P_{i}$.
The null hypothesis is that the number of obsered outcomes, $n_{i}$, is equal to the expected number of outcomes,

$$
n_{i}=n p_{i} \quad i=1,2,3, \ldots, k
$$

The alternative hypothis is that the observed outcomes differ significantly from the expected outcomes to a sufficient degree to invalidate the null hypothesis.

$$
n_{i} \neq n p_{i} \quad i=1,2,3, \ldots, k .
$$

## Goodness of Fit Example (Age Distribution of Sample)

Consider the following age distribution of participants in a study compared to the representation in the Census.

| Age |  | Number in <br> Sample | Per Cent <br> in Census |  | Expected <br> Sample |
| :--- | :---: | :--- | :---: | :--- | :---: |
| $20-24$ |  | 103 |  | 18 |  |
| $24-34$ |  | 216 |  | 88.2 |  |
| $35-44$ |  | 171 |  | 32 | 245 |
| Total |  | 490 |  | 100 |  |
|  |  |  | 156.8 |  |  |
|  |  |  |  | 490 |  |

The claim is that the age disdistribution in the sample matches distribution found in the census. It follows that the null hypothesis is that the distributions are equal. The alternative hypothesis is that the distributions differ. Use
a significance level of 0.05 to determine the validity of the null hypothis
The following table summarizes the calculation

| Age | Number in sample | Expected sample | $x^{2}$ |
| :--- | :--- | :--- | :--- |
| 20-24 | 103 | 88.2 | 2.48 |
| 24-34 | 216 | 245 | 3.43 |
| 35-44 | 171 | $\underline{156.8}$ | 1,29 |
| Total | 490 | 490 | 7.2 |

Where $x^{2}$ is computed using two degrees of freedom.

$\chi^{2}$ PDF, Number of Degrees of Freedom: 2
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-260.jpg?height=643&width=1188&top_left_y=1326&top_left_x=308)

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-261.jpg?height=660&width=1002&top_left_y=133&top_left_x=298)

The previous plots show the PDF and CDF for this distribution.

Next the value of $y^{2}$ required the meet the null hypothesis assuption of a 0.05 significance level is required. The value of $x^{2}$ required for at least 0.05 significance is calle the critical $x^{2}$ and is denoted by $x^{2} c$.
A significance level of 0.05 means that a value of $0<x^{2}<x_{c}^{2}$ will occur by random qs\% of the time. If this
is the case the null hypothesis is accepted. The interpretation being trat this is a likely occurance. If $x^{2}>x^{2} c$ values in this range will occur
less than 5\% of the time leading to the iterpretation that the value is improbable and the rejection of the null hypotheis. In the above $x^{2}$ PDF plot the value of $x_{c}^{2} \approx 6$ for two degrees of freedom is indicated with the range of values boding to acceptance or refection of the null hypothesis shown. From the plot $t$ is seen $X_{C}^{2}$ is the value of $X^{2}$ satisfying

$$
P\left(x^{2} \geqslant x_{c}^{2}\right)=0.05 .
$$

The following plot shows illustrates how the value can be determined. $P\left(x^{2} \geqslant x_{c}{ }^{2}\right)$ is a tail probability

$\chi^{2}$ Tail CDF, Number of Degrees of Freedom: 2
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-263.jpg?height=724&width=1098&top_left_y=133&top_left_x=229)

The plot above shows the tail probability as a function of $x^{2} . x_{c}^{2}$ is the intersection of the line $1-F\left(x^{2} ; 2\right)=0.05$. Inspection of the plot gives the estimate

$$
x_{c} \approx 6
$$

A more pricise estimate gives $\psi_{c}=51991$.

Finally completing the analysis of the tral age distribution being representative of the population
it was found that trial age distribution had a

$$
x^{2}=7.2
$$

with a significance level of 0.08 it was found that

$$
x_{c}^{2}=6
$$

since $x^{2}>x_{c}^{2}$ it lies in the region in which the null hypothesis should be regected. Thus the trial age distribution is not representative of the population in general.

## Simulation of Results

In the previous section the results of an anaysis of a data set with 2 degrees of freedom for an undelying muttinomial distribution was shown. Here a simulation result is presented using the multinomial random variable

## $x \sim \operatorname{mattinomial}(n, p)$

where $n=1000, p=(0.18,0.5,0.32)$.
$P$ is the same as assumed in the cralysis of the previous section.
10000 trials were performed and $y^{2}$ was computed for each and results are compared with the $x^{2}$ distribution for two degrees of freedom in the plot below. The agreement with the simulation is very good.

## Though quit large ensembles are required to obtain good

results. A simulation using 1000 trials is also shown for comparison.

$\chi^{2}$ Sampled Distribution 10000 Trails, 2 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-266.jpg?height=670&width=996&top_left_y=485&top_left_x=308)

$\chi^{2}$ Sampled Distribution 1000 Trails, 2 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-266.jpg?height=662&width=1002&top_left_y=1283&top_left_x=310)

## The $t$-Test

Consider a random variable $x$ with $n$ samples and sample mean

$$
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

If the population mean, $\mu$, and population variance, $\sigma^{2}$, core known. Then if the central limit theorem is assumed the distribution of

$$
\frac{\sqrt{n}\left(\bar{x}_{n}-\mu\right)}{\sigma} \xrightarrow{d} N(0,1)
$$

approaches a unit normal distribution That is the distribution of deviations of the sample mean $x$ from the population $\mu$ when scaled by the population 6 . The test statistic

$$
z=\frac{\bar{x}_{n}-\mu}{\sigma / \sqrt{n}}
$$

can be used in hypothesis testing. If $\sigma$ is not known the the

6 can be replaced by the sample variance

$$
S_{n}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}
$$

to produce the $t$-statistic to be used in the $t$-test

$$
t=\frac{\bar{x}_{n}-\mu}{s_{n} / \sqrt{n}}
$$

Now Consider

$$
\begin{aligned}
& t=\frac{\left(\bar{x}_{n}-\mu\right)}{S_{n} / \sqrt{n}}=\frac{\left(\bar{x}_{n}-\mu\right)}{S_{n} / \sqrt{n}} \frac{\frac{\sqrt{n}}{\frac{\sqrt{n}}{\sigma}}}{\sigma} \\
&=\frac{\left(\bar{x}_{n}-\mu\right)}{\frac{S_{n}}{\sigma} \frac{\sqrt{n}}{\sqrt{n}}}=\frac{\left(\bar{x}_{n}-\mu\right)}{\sigma / \sqrt{n}} \\
& \frac{S_{n}}{\sigma} \frac{\sqrt{n-1}}{\sqrt{n-1}}
\end{aligned}
$$

The numerator is a unit normal random variable

$$
z_{n}=\frac{\left(\bar{x}_{n}-\mu\right)}{\sigma \sqrt{n}} \xrightarrow{d} N(0,1)
$$

and for the denominator let

$$
\begin{aligned}
& \sqrt{x^{2}}=\sqrt{n-1} \frac{s_{n}}{\sigma} \\
\Rightarrow & (n-1) \frac{s_{n}^{2}}{\sigma^{2}} \\
= & \frac{n-1}{\sigma^{2}} \frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2} \\
= & \frac{1}{\sigma^{2}} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2} \\
= & \sum_{i=1}^{n}\left(\frac{x_{i}-\mu}{\sigma}\right)^{2}
\end{aligned}
$$

If $t$ is assumed that,

$$
\frac{x_{i}-\mu}{\sigma} \sim N(0,1)
$$

then

$$
x^{2}=(n-1) \frac{s^{2} n}{\sigma^{2}} \sim \operatorname{chi-squared}(n-1)
$$

thus $x^{2}$ has a Chi-squared distributution with $n-l$ degrees of freedom, so the $t$-statislic is the ratio of a unit normal random variable and the
square root of chi-squared random variable.

$$
t=\frac{2 n}{\sqrt{\frac{x^{2}}{n-1}}}
$$

To go further the distribution of $\sqrt{x^{2}}$ must be determined and it must be assumed that $Z_{n}$ and $\sqrt{x^{2}}$ are independent to eveluate the distribution of the ratio.

## Distribution of square Root of Chi-squared Random varrable

The Chi-square distribution for $k$ degrees of freedom is given by

$$
f(z)=\frac{1}{2^{k / 2} \Gamma(k / 2)} z^{k / 2-1} e^{-z / 2}
$$

where $0<2<\infty$.
Recall the change of variable formula for a probability denstiy where

$$
y=g(2)
$$

namely

$$
f_{y}(y)=f_{2}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|
$$

Now to obtain the distribution of the square root of a Chi-squared random variable, 2 , let,

$$
\begin{aligned}
y & =g(z)=\sqrt{z} \\
\Rightarrow z & =g^{-1}(y)=y^{2}
\end{aligned}
$$

where $y>0$ and

$$
\frac{d g^{-1}(y)}{d y}=2 y
$$

Thus

$$
\begin{aligned}
& f(y)=f_{2}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right| \\
= & \frac{1}{2^{k / 2} \Gamma(k / 2)}\left(y^{2}\right)^{k / 2-1} e^{-y^{2} / 2}(2 y) \\
= & \frac{\partial}{2^{k / 2} \Gamma(k / 2)} y^{k-2} y e^{-y^{2} / 2} \\
= & \frac{1}{2^{k / 2-1} \Gamma(k / 2)} y^{k-1} e^{-y^{2} / 2}
\end{aligned}
$$

## Ratio Distribution

The $t$-statistic is a random variable that is a ratio of a unit normal random variable and the square root of a chi-squared random variable which are assumed independent. A general result for the distribution of the ratio of two independent random variables is called the ratio distribution. In this section this result will be dericed.

Recall the two dimensional change of variables for a probability desity function for the change of variables

$$
u=u(x, y) \quad v=v(x, y)
$$

which can be inverted to give

$$
x=x(u, v) \quad y=y(u, v)
$$

has a probability density
$f_{u v}(u, v)=f_{x y}(x(u, v), y(u, v))|J|$ where $|J|$ is the determinate of the Jacobian matrix, namely

$$
\begin{aligned}
|J| & =\left|\frac{\partial(x, y)}{\partial(u, v)}\right|=\left|\begin{array}{ll}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{array}\right| \\
& =\left|\frac{\partial x}{\partial u} \frac{\partial y}{\partial v}-\frac{\partial x}{\partial v} \frac{\partial y}{\partial u}\right|
\end{aligned}
$$

For the ratio distribution consider two indeperdent random variables $x$ and $y$ with probability densities

$$
f_{x}(x) \quad f_{y}(y)
$$

since $x$ and $y$ are independent

$$
f_{x y}(x, y)=f_{x}(x) f_{y}(y)
$$

Define the change of variables

$$
u=y \quad v=\alpha \frac{x}{y}
$$

where $y>0$ and $\alpha$ is a constant. These equations can be inverted to give

$$
v=\alpha \frac{x}{u}=\Rightarrow \quad x=\frac{u v}{\alpha}
$$

The Jacobran is given by

$$
\begin{aligned}
1 J 1= & \left|\frac{\partial x}{\partial u} \frac{\partial y}{\partial v}-\frac{\partial x}{\partial v} \frac{\partial y}{\partial u}\right| \\
& \left|v(0)-\frac{u}{\alpha}(1)\right|=-\frac{u}{\alpha}
\end{aligned}
$$

Now the density is given by

$$
\begin{aligned}
& f_{u v}(u, v)=f_{x y}(x(u, v), y(u, v))|J| \\
& =f_{x}(x(u, v)) f_{y}(y(u, v)|J| \\
& =f_{x}(u v) f_{y}(u) \frac{u}{\alpha}
\end{aligned}
$$

the desired ratio density is $f_{v}(v)$ thus with

$$
v=\alpha \frac{x}{y}
$$

and $y>0$ which implies $u>0$ it follows that

$$
f_{v}(v)=\int_{0}^{\infty} f_{x}(u v) f_{y}(u) \frac{u}{\alpha} d u
$$

To put the result in a more common form let

$$
R=v=\alpha \frac{x}{y}
$$

and since $u=y$, the ratio density is given by

$$
f_{R}(R)=\int_{0}^{\infty} f_{x}(R y) f_{y}(y) \frac{y}{\alpha} d y
$$

## t-Distribution

Consider $n$ trials of a random variable $x$ denoted by

$$
\begin{array}{r}
\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\} \\
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{n}
\end{array}
$$

If the population mean $\mu$ is known,

$$
s_{n}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}
$$

and the $t$-statistic is defined

$$
t=\frac{Z_{n}}{\sqrt{X_{n-1}^{2}}}
$$

where

$$
\begin{aligned}
& z_{n}=\frac{\left(\bar{x}_{n}-\mu\right)}{\sigma / \sqrt{n}} \sim N(0,1) \\
& x^{2}=(n-1) \frac{s^{2} n}{\sigma^{2}} \sim \text { chi-squared }(n-1)
\end{aligned}
$$

If $Z_{n}$ and $X_{n}$ are assumed independent then $t$ is a ratio distribution where the numerator distribution is a unit normal and the denominator is the distribution of square root of a $x_{n}^{2}$ divided by $\sqrt{n-1}$.
so for the numerator

$$
Z \sim N(0,1)=\frac{1}{\sqrt{2 \pi}} e^{-2^{2} / 2}
$$

In a previous section it was shown that
$\sqrt{x^{2}}=x \sim \frac{1}{2^{(n-1) / 2-1} \Gamma(n-1 / 2)} x^{(n-1)-1} e^{-x^{2} / 2}$
let

$$
y=\frac{x}{\sqrt{n-1}}
$$

using the change of variable

$$
f_{y}(y)=f_{x}\left(g^{-1}(y)\right)\left|\frac{d g^{-1}(y)}{d y}\right|
$$

with

$$
\begin{aligned}
y & =g(x)=\frac{x}{\sqrt{n-1}} \\
\Rightarrow \quad x & =g^{-1}(y)=y \sqrt{n-1}
\end{aligned}
$$

So

$$
\frac{d g^{-1}(y)}{d y}=\sqrt{n-1}
$$

thus

$$
\begin{aligned}
f_{y}(y) & =\frac{\sqrt{n-1}}{2^{(n-1) / 2-1} \Gamma\left(\frac{n-1}{2}\right)}(\sqrt{n-1} y)^{(n-1)-1} e^{-\frac{(n-1) y 2}{2}} \\
& =\frac{\sqrt{n-1}(\sqrt{n-1})^{(n-1)-1}}{2^{(n-1) / 2-1} \Gamma\left(\frac{n-1}{2}\right)} y^{(n-1)-1} e^{-\frac{(n-1) y^{2}}{2}} \\
& =\frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) / 2-1} \Gamma\left(\frac{n-1}{2}\right)} y^{(n-1)-1} e^{-\frac{(n-1) y^{2}}{2}}
\end{aligned}
$$

Recall that the ratio distribution of independent randam variables is given by, assuming $\alpha=1$.

$$
f_{t}(t)=\int_{0}^{\infty} f_{z}(t y) f_{y}(y) y d y
$$

where

$$
t=\frac{2}{y}
$$

using the provious results gives

$$
\begin{aligned}
& f_{2}(t y) f_{y}(y) y=\frac{1}{\sqrt{2 \pi}} e^{-(t-1)^{2} / 2} \\
& \frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) l_{2}-1} \Gamma\left(\frac{n-1}{2}\right)} y^{(n-1)-1} e^{-\left(\frac{n-1)}{2} y^{2}\right.} y \\
= & \frac{1}{\sqrt{2 \pi}} \frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) l_{2}-1} \Gamma\left(\frac{n-1}{2}\right)} y^{n-1} e^{-y_{2}^{2}\left(t^{2}+n-1\right)} \\
= & \frac{1}{\sqrt{2 \pi}} \frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) l_{2}-1} \Gamma\left(\frac{n-1}{2}\right)} y^{n-1} e^{-y^{2}\left(\frac{n-1}{2}\right)\left(\frac{t^{2}}{n-1}+1\right)}
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
& f_{t}(t)=\int_{0}^{\infty} f_{z}(t y) f_{y}(y) y d y \\
= & \frac{1}{\sqrt{2 \pi}} \frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) I_{2}-1} \Gamma\left(\frac{n-1}{2}\right)} \int_{0}^{\infty} y^{n-1} e^{-\frac{y^{2}}{2}(n-1)\left(\frac{t^{2}}{n-1}+1\right)} d y
\end{aligned}
$$

Consider the integral and make the change of wariable

$$
\begin{aligned}
& \omega=y^{2}\left(\frac{n-1}{2}\right)\left(\frac{t^{2}}{n-1}+1\right) \\
= & \left(\frac{t^{2}}{n-1}+1\right)^{-1} \frac{2}{n-1} \omega=y^{2} \\
\Rightarrow & \frac{2}{n-1}\left(\frac{t^{2}}{n-1}+1\right)^{-1} d \omega=2 y d y \\
\Rightarrow & \frac{1}{n-1}\left(\frac{t^{2}}{n-1}+1\right)^{-1} d \omega=y d y
\end{aligned}
$$

substitution into the integral gives

$$
\begin{aligned}
& \int_{0}^{\infty} y^{n-1} e^{-\frac{y^{2}}{2}(n-1)\left(\frac{t^{2}}{n-1}+1\right)} d y \\
& =\int_{0}^{\infty} y^{n-2} e^{-\frac{y^{2}}{2}(n-1)\left(\frac{t^{2}}{n-1}+1\right)} y d y \\
& =\int_{0}^{\infty}\left[\left(\frac{t^{2}}{n-1}+1\right)^{-1} \frac{2}{n-1}\right]^{\frac{n-2}{2}} \omega^{\frac{n-2}{2}} e^{-\omega} \\
& =\frac{1}{n-1}\left(\frac{t^{2}}{n-1}+1\right)^{-1} d \omega \\
& \left.=\frac{2^{\frac{n}{2}-1}}{\left[\frac{1}{n-1}\right.}\left(\frac{t^{2}}{n-1}+1\right)^{-1}\right]^{\frac{n}{2}} \int_{0}^{\infty} \omega^{\frac{n-2}{2}} e^{-\omega} d \omega \\
& =\frac{2^{n / 2-1}}{(n-1)^{\frac{n}{2}}}\left(\frac{t^{2}}{n-1}+1\right)^{-\frac{n}{2}} \int_{0}^{\infty} \omega^{\frac{n}{2}-1} e^{-\frac{-1}{2}} d \omega
\end{aligned}
$$

The integral is a Camma function

$$
\Gamma\left(\frac{n}{2}\right)=\int_{0}^{\infty} \omega^{\frac{n}{2}-1} e^{-\omega} d \omega
$$

Putting the integral together gives

$$
\begin{aligned}
& \int_{0}^{\infty} y^{n-1} e^{-\frac{y^{2}}{2}(n-1)\left(\frac{t^{2}}{n-1}+1\right)} d y \\
& =\frac{2^{n / 2-1}}{(n-1)^{n / 2}}\left(\frac{t^{2}}{n-1}+1\right)^{-\frac{n}{2}} \Gamma\left(\frac{n}{2}\right)
\end{aligned}
$$

Putting the whole thing together gues

$$
\begin{aligned}
& f_{t}(t)= \int_{0}^{\infty} f_{z}(t y) f_{y}(y) y d y \\
&= \frac{1}{\sqrt{2 \pi} \frac{(\sqrt{n-1})^{n-1}}{2^{(n-1) l_{2}-1} \Gamma\left(\frac{n-1}{2}\right)}} \\
& \frac{2^{n / 2-1}}{(n-1)^{n / 2}}\left(\frac{t^{2}}{n-1}+1\right)^{-\frac{n}{2}} \Gamma\left(\frac{n}{2}\right) \\
&=\frac{1}{\sqrt{\pi}} \frac{(\sqrt{n-1})^{n-1}}{(\sqrt{n-1})^{2}} \frac{2^{n-1}}{2^{(n-1) 2^{-1+1 / 2}}}\left(\frac{t^{2}}{n-1}+1\right)^{-\frac{n}{2}} \\
& \frac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n-1}{2}\right)}
\end{aligned}
$$

$$
=\frac{1}{\sqrt{\pi}} \frac{1}{\sqrt{n-1}}\left(\frac{t^{2}}{n-1}+1\right)^{-\frac{n}{2}} \frac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n-1}{2}\right)}
$$

Getting close, note that

$$
\frac{n}{2}=\frac{n-1+1}{2}=\frac{(n-1)+1}{2}
$$

so

$$
\begin{aligned}
f_{t}(t) & =\frac{1}{\sqrt{\pi(n-1)}} \frac{\Gamma\left(\frac{n-1+1}{2}\right)}{\Gamma\left(\frac{n-1}{2}\right)}\left(\frac{t^{2}}{n-1}+1\right)^{\frac{-(n-1+1)}{2}} \\
& =T(n-1)
\end{aligned}
$$

This is a t-distribution with $n-1$ degrees of freedom. Thus the distribution of the $t$-statistic

$$
t=\frac{\bar{x}_{n}-\mu}{S_{n} / \sqrt{n}} \sim T_{t}(n-1)
$$

The t-distribution for $n$ degrees of freedom is given

$$
\tau_{t}(n)=\frac{1}{\sqrt{\pi n}} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}\left(\frac{t^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)}
$$

## Hypergeometric Function

The Hypergeometric function arises in the calculation of the t-distribution CDF. Here a discussion of the relevant properties is given. In general a series defined by

$$
\sum_{n=0}^{\infty} c_{n}
$$

is called Hypergeometric if
$\frac{C_{n+1}}{C_{n}}=\frac{\left(n+a_{1}\right)\left(n+a_{2}\right) \cdots\left(n+a_{p}\right)}{\left(n+b_{1}\right)\left(n+b_{2}\right) \cdots\left(n+b_{p}\right)(n+1)} 2$
where $n=0,1,2,3, \ldots$
This should be compared with the more common geometric series where

$$
\frac{C_{n+1}}{C_{n}}=2
$$

Iterating and asswing that Co is known gives

$$
\begin{aligned}
c_{1} & =\frac{a_{1} a_{2} a_{3} \cdots a_{p}}{b_{1} b_{2} b_{3} \cdots b_{q}} c_{0} z \\
c_{2} & =\frac{\left(1+a_{1}\right)\left(1+a_{2}\right) \cdots\left(1+a_{p}\right)}{\left(1+b_{1}\right)\left(1+b_{2}\right) \cdots\left(1+b_{q}\right)(2)} \\
& =\frac{a_{1}\left(1+a_{1}\right) a_{2}\left(1+a_{2}\right) \cdots a_{p}\left(1+a_{p}\right) c_{0} z^{2}}{b_{1}\left(1+b_{1}\right) b_{2}\left(1+b_{2}\right) \cdots b_{q}\left(1+b_{q}\right)(2)}
\end{aligned}
$$

noticing the pattern, the shifted factorial is defined by

$$
\begin{gathered}
(a)_{n}=a(a+1)(a+2) \cdots(a+n-1) \\
(a)_{0}=1
\end{gathered}
$$

then

$$
c_{n}=\frac{\left(a_{1}\right)_{n}\left(a_{2}\right)_{n} \cdots\left(a_{p}\right)_{n}}{\left(b_{1}\right)_{n}\left(b_{2}\right)_{n} \cdots\left(b_{q}\right)_{n}} \frac{c_{0}}{n!} z^{n}
$$

SO

$$
\sum_{n=0}^{\infty} c_{n}=\sum_{n=0}^{\infty} \frac{\left(a_{1}\right)_{n}\left(a_{2}\right)_{n} \cdots\left(a_{p}\right)_{n}}{\left(b_{1}\right)_{n}\left(b_{2}\right)_{n} \cdots\left(b_{q}\right)_{n}} \frac{2^{n}}{n!}
$$

The Generalized thpergeometric function is defined by

$$
\begin{aligned}
p F_{q}\binom{a_{1}, a_{2},}{b_{1}, b_{2}, \cdots a_{p}} \\
\quad=\sum_{n=0}^{\infty} \frac{\left(a_{1}\right)_{n}\left(a_{2}\right)_{n} \cdots\left(a_{p}\right)_{n}}{\left(b_{1}\right)_{n}\left(b_{2}\right)_{n} \cdots\left(b_{q}\right)_{n}} \frac{z^{n}}{n!}
\end{aligned}
$$

The special case $p=2$ and $q=1$ is called the Hypergeometric series

$$
{ }_{2} F_{1}(a, b ; c ; z)=\sum_{n=0}^{\infty} \frac{(a)_{n}(b)_{n}}{(c)_{n}} \frac{z^{n}}{n!}
$$

## Incomplete Beta Function

The incomplete Beta function is useful in the evaluation of the $t$-distribution. Here a discussion of the relevant propertics is given.
The Beta function is defined by,

$$
\begin{aligned}
B(a, b) & =\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
& =\frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)}
\end{aligned}
$$

The Incomplete Beta function is defined by

$$
B(t ; a, b)=\int_{0}^{t} x^{a-1}(1-x)^{b-1} d x
$$

and the regularized Incomplete Beta
function is defined by

$$
I_{t}(a, b)=\frac{B(t ; a, b)}{B(a, b)}
$$

A more use representation of the Beta function can be found by making the change of variables

$$
\begin{aligned}
u & =\frac{x}{1-x} \\
& \Rightarrow u(1-x)=x \\
& \Rightarrow \frac{1-x}{x}=\frac{1}{u} \\
& \Rightarrow \frac{1}{x}=\frac{1}{u}+1 \\
& =\frac{1+u}{u} \\
& \Rightarrow x=\frac{u}{1+u}
\end{aligned}
$$

and

$$
\begin{aligned}
1-x & =1-\frac{u}{1+u}=1+\frac{u-u}{1+u} \\
& =\frac{1}{1+u}
\end{aligned}
$$

Finally

$$
\begin{aligned}
d x & =\left[\frac{1}{1+u}-\frac{u}{(1+u)^{2}}\right] d u \\
& =\left[\frac{1+u-u}{(1+u)^{2}}\right] d u \\
& =\frac{d u}{(1+u)^{2}}
\end{aligned}
$$

The integration limits transform using

$$
\begin{gathered}
u=\frac{x}{1-x} \\
u(1)=\infty \quad u(0)=0
\end{gathered}
$$

Making the change of variables
gives

$$
\begin{aligned}
& B(a, b)=\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
= & \int_{0}^{\infty}\left(\frac{u}{1+u}\right)^{a-1}\left(\frac{1}{1+u}\right)^{b-1} \frac{1}{(1+u)^{2}} d u \\
= & \int_{0}^{\infty} \frac{u^{a-1}}{(1+u)^{a+b}} d u
\end{aligned}
$$

Thus the alternative form is given by

$$
\begin{aligned}
B(a, b) & =\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
& =\int_{0}^{\infty} \frac{x^{a-1}}{(1+x)^{a+b}} d x
\end{aligned}
$$

If $a$ and $b$ are integers and using

$$
\Gamma(a)=(a-1)!
$$

It follows that

$$
\begin{aligned}
B(a, b) & =\frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)} \\
& =\frac{(a-1)!(b-1)!}{(a+b-1)!}
\end{aligned}
$$

A recurrence relation for $B(a, b)$ follows

$$
\begin{aligned}
B(a+1, b) & =\frac{a!(b-1)!}{(a+b)!} \\
& =\frac{(a-1)!a(b-1)!}{(a+b-1)!(a+b)} \\
& =\frac{(a-1)!(b-1)!}{(a+b-1)!} \frac{a}{a+b}
\end{aligned}
$$

$$
=B(a, b) \frac{a}{a+b}
$$

Similarly

$$
\begin{aligned}
B(a, b+1) & =\frac{(a-1)!b!}{(a+b)!} \\
& =\frac{(a-1)!(b-1)!b}{(a+b-1)!(a+b)} \\
& =B(a, b) \frac{b}{a+b}
\end{aligned}
$$

Thus

$$
\begin{aligned}
& B(a+1, b)=B(a, b) \frac{a}{a+b} \\
& B(a, b+1)=B(a, b) \frac{b}{a+b}
\end{aligned}
$$

The Beta function is also related to the binomial coefficient if $a$ and $b$ are integers

Recall the Binomial coefficient is given by

$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

if $n=a+b$ then $k=b$

$$
\begin{aligned}
\binom{n}{k} & =\binom{a+b}{b}=\frac{(a+b)!}{a!b!} \\
& =\frac{\Gamma(a+b+1)}{\Gamma(a+1) \Gamma(b+1)} \\
& =\frac{(a+b) \Gamma(a+b)}{a \Gamma(a) b \Gamma(b)} \\
& =\frac{(a+b)}{a b} \frac{\Gamma(a+b)}{\Gamma(a) \Gamma(b)} \\
& =\frac{(a+b)}{a b} \frac{1}{B(a, b)}
\end{aligned}
$$

$$
\Rightarrow B(a, b)=\frac{(a+b)}{a b} \frac{1}{(a+b)}
$$

Back to the incomplete Beta function

$$
B(t ; a, b)=\int_{0}^{t} x^{a-1}(1-x)^{b-1} d x
$$

where $0 \leqslant t \leqslant 1$
It follows that

$$
\begin{aligned}
B(0 ; a, b) & =\int_{0}^{0} x^{a-1}(1-x)^{b-1} d x \\
& =0 \\
B(1 ; a, b) & =\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
& =B(a, b) \\
B(t ; 1, b) & =\int_{0}^{t}(1-x)^{b-1} d x
\end{aligned}
$$

let $s=1-x=0-d s=d x$ then

$$
\begin{aligned}
B(t ; 1, b) & =-\int_{1}^{1-t} s^{b-1} d s \\
& =\int_{1-t}^{1} s^{b-1} d s \\
& =\left.\frac{1}{b-1} s^{b}\right|_{1-t} ^{1} \\
& =\frac{1}{b-1}\left[1-(1-t)^{b}\right]
\end{aligned}
$$

Finally consider

$$
B(1-t ; b, a)=\int_{0}^{1-t} x^{b-1}(1-x)^{a-1} d x
$$

let

$$
\begin{aligned}
u=1-x & \Rightarrow \quad x=1-u \\
-d u & =d u
\end{aligned}
$$

then

$$
\begin{aligned}
B(1-t ; b, a) & =-\int_{1}^{t}(1-u)^{b-1} u^{a-1} d u \\
& =\int_{t}^{1}(1-u)^{b-1} u^{a-1} d u \\
& =\int_{t}^{1} x^{a-1}(1-x)^{b-1} d x
\end{aligned}
$$

but

$$
\begin{aligned}
& B(a, b)= \int_{0}^{1} x^{a-1}(1-x)^{b-1} d x \\
&= \int_{0}^{t} x^{a-1}(1-x)^{b-1} d x \\
&+\int_{t}^{1} x^{a-1}(1-x)^{b-1} d x \\
& \Rightarrow \int_{0}^{t} x^{a-1}(1-x)^{b-1} d x \\
&= B(a, b)-\int_{t}^{1} x^{a-1}(1-x)^{b-1} d x
\end{aligned}
$$

but

$$
B(t, a, b)=\int_{0}^{t} x^{a-1}(1-x)^{b-1} d x
$$

and

$$
B(1-t ; b, a)=\int_{t}^{1} x^{a-1}(1-x)^{b-1} d x
$$

Thus

$$
B(t ; a, b)=B(a, b)-B(1-t ; b, a)
$$

* In summary it has been shown

$$
\begin{gathered}
B(0 ; a, b)=0 \\
B(1 ; a, b)=B(a, b) \\
B(t ; 1, b)=\frac{1}{b-1}\left[1-(1-t)^{b}\right] \\
B(t ; a, b)=B(a, b)-B(1-t ; b, a)
\end{gathered}
$$

In terms of the regularized incomplete Beta function,

$$
I_{t}(a ; b)=\frac{B(t ; a, b)}{B(a, b)}
$$

and using the result

$$
\begin{aligned}
B(1, b) & =\int_{0}^{1}(1-x)^{b-1} d x \\
& =-\left.\frac{1}{b-1}(1-x)^{b}\right|_{0} ^{1} \\
& =\frac{1}{b-1}
\end{aligned}
$$

gives

$$
\begin{aligned}
& I_{0}(a, b)=0 \\
& I_{1}(a, b)=1 \\
& I_{t}(a, b)=1-(1-t)^{b} \\
& I_{t}(a, b)=1-I_{1-t}(b, a)
\end{aligned}
$$

Finally $I_{t}(a, b)$ has a representation as a Hypergeometric series if use is rode of the EulerPochnammer integral

$$
\begin{aligned}
& 2 F_{1}(a, b ; c ; z)=\sum_{n=0}^{\infty} \frac{(a)_{n}(b)_{n}}{(c)_{n}} \frac{z^{n}}{n!} \\
= & \frac{\Gamma(c)}{\Gamma(b) \Gamma(c-b)} \int_{0}^{1} u^{b-1}(1-w)^{c-b-1}(1-w) d u
\end{aligned}
$$

It follows that

$$
I_{t}(a, b)=\frac{\Gamma(a+b)}{\Gamma(a+1) \Gamma(b)} \text {, } F_{1}(1-b, a ; a+1 ; t)
$$

## Properties of t-distribution

In the previous section the distribution of the $t$-statistic was derived. It was shown that the PDF, $f(t)$, for $n$ degrees of freedom

$$
\begin{aligned}
f(t) & =T_{t}(n) \\
& =\frac{1}{\sqrt{\pi n}} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}\left(\frac{t^{2}}{n}+1\right)^{-\frac{(n+1)}{2}}
\end{aligned}
$$

First the CDF is computed. Recall that the CDF is defined by

$$
\begin{aligned}
& P(T \leqslant t)=\int_{-\infty}^{t} T_{s}(n) d s \\
& =\frac{1}{\sqrt{n \pi}} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{1}{2}\right)} \int_{-\infty}^{t}\left(\frac{s^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s
\end{aligned}
$$

and the regularized incomplete Beta function is given by
$I_{x}(a, b)=\frac{1}{B(a, b)} \int_{0}^{x} u^{a-1}(1-u)^{b-1} d u$
Let

$$
\begin{aligned}
& u=\frac{n}{s^{2}+n}=\left(s^{2} / n+1\right)^{-1} \\
& \begin{aligned}
1-u & =1-\frac{n}{s^{2}+n} \\
& =1-\frac{1}{s^{2} / n+1} \\
& =\frac{s^{2} / n}{s^{2} / n+1} \\
d u & =\frac{d}{d s}\left(\frac{1}{s^{2} / n+1}\right) d s \\
& =\frac{-2 s / n}{\left(s^{2} / n+1\right)^{2}} d s
\end{aligned} \\
&
\end{aligned}
$$

The upper integration limit is given by

$$
x=\frac{1}{t^{2} / n+1}
$$

and the lower limit of 0 requires $t \rightarrow \pm \infty$. For the sign of the integral to work out $t \rightarrow \infty$ will be choosen.
It follows that

$$
\begin{aligned}
& I_{x}(a, b)=\frac{1}{B(a, b)} \int_{0}^{x} u^{a-1}(1-u)^{b-1} d u \\
& \Rightarrow I_{t}(a, b)=\frac{1}{B(a, b)} \int_{\infty}^{t}\left(\frac{1}{s^{2} / n+1}\right)^{a-1} \\
& \left(\frac{s^{2} / n}{s^{2} / n+1}\right)^{b-1} \frac{(-2 s / n)}{\left(s^{2} / n+1\right)^{2}} d s
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{B(a, b)} \int_{\infty}^{t} \frac{(-2 s / n)\left(s^{2} / n\right)^{b-1}}{\left(s^{2} / n+1\right)^{a-1}\left(s^{2} / n+1\right)^{b-1}} \\
& =\frac{1}{\left(s^{2} / n+1\right)^{2}} d s \\
& =\frac{2}{B(a, b)} \int_{t}^{\infty} \frac{(s / n)\left(s^{2} / n\right)^{b-1}}{\left(s^{2} / n+1\right)^{a+b}} d s
\end{aligned}
$$

Recall that the t-distribution is given by
$T_{t}(n)=\frac{1}{\pi n} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}\left(\frac{t^{2}}{n}+1\right)^{-\frac{(n+1)}{2}}$
to get the exponent correct let

$$
a=\frac{n}{2} \quad b=\frac{1}{2}
$$

thus
$I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)=\frac{2}{B\left(\frac{n}{2}, \frac{1}{2}\right)} \int_{t}^{\infty} \frac{\left.(s / n)^{s / n}\right)^{-1 / 2}}{(s / n+1)^{n / 2+1 / 2}} d s$

$$
\begin{aligned}
& =\frac{2}{B\left(\frac{n}{2}, \frac{1}{2}\right)} \int_{t}^{\infty} \frac{\left(\frac{s_{1}}{n}\right)}{(\sqrt{n} / \sqrt{n})}\left(\frac{s 3}{n}+1\right)^{-\frac{1}{2}(n+1)} d s \\
& =\frac{2}{B\left(\frac{n}{2}, \frac{1}{2}\right)} \int_{t}^{\infty} \frac{1}{\sqrt{n}}\left(\frac{s 2}{n}+1\right)^{-\frac{1}{2}(n+1)} d s \\
& =\frac{2}{\sqrt{n} B\left(\frac{n}{2}, \frac{1}{2}\right)} \int_{t}^{\infty}\left(\frac{s 2}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s
\end{aligned}
$$

Getting close. Now

$$
B\left(\frac{n}{2}, \frac{1}{2}\right)=\frac{\Gamma\left(\frac{n}{2}\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left(\frac{n+1}{2}\right)}
$$

but

$$
\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}
$$

50

$$
B\left(\frac{n}{2}, \frac{1}{2}\right)=\frac{\pi \Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n+1}{2}\right)}
$$

and finally
$I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)=\frac{2 \Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n \pi} \Gamma\left(\frac{n}{2}\right)} \int_{t}^{\infty}\left(\frac{s^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d s$
Now using
$T_{t}(n)=\frac{1}{\sqrt{\pi n}} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}\left(\frac{t^{2}}{n}+1\right)^{-\frac{(n+1)}{2}}$
gives

$$
\int_{t}^{\infty} T_{s}(n) d s=\frac{1}{2} I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)
$$

Finally, since

$$
\begin{aligned}
& \int_{-\infty}^{\infty} T_{s}(n) d s=1 \\
= & \int_{-\infty}^{t} T_{s}(n) d s+\int_{t}^{\Delta} T_{s}(n) d s
\end{aligned}
$$

It follows that the $t$-distribution CDF is given by

$$
\begin{aligned}
P(T \leqslant t) & =\int_{-\infty}^{t} T_{s}(n) d s \\
& =1-\int_{t}^{\infty} T_{s}(n) d s
\end{aligned}
$$

Now it was just shown that

$$
\int_{t}^{\infty} T_{s}(n) d s=\frac{1}{2} I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)
$$

Thus the CDF is given by

$$
\begin{aligned}
P(t \leqslant T) & =\int_{-\infty}^{t} T_{s}(n) d s \\
& =1-\frac{1}{2} I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)
\end{aligned}
$$

Next the mean and variance are computed. First, the mean is given by,

$$
\begin{aligned}
& \mu=E(T)=\int_{-\infty}^{\infty} s T_{s}(n) d s \\
& =\frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n \pi} \Gamma\left(\frac{n}{2}\right)} \int_{-\infty}^{\infty} s\left(\frac{s^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d s
\end{aligned}
$$

Consider the integral

$$
\begin{aligned}
\int_{-\infty}^{\infty} s & \left(\frac{s^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d s \\
= & \int_{-\infty}^{0} s\left(\frac{s^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d s \\
& +\int_{0}^{\infty} s\left(\frac{s^{2}}{n+1}+1\right)^{-\frac{(n+1)}{2}} d s
\end{aligned}
$$

for the first integral let

$$
\begin{aligned}
u & =-s \\
\Rightarrow d u & =-d s
\end{aligned}
$$

then

$$
\begin{aligned}
\int_{-\infty}^{0} s & \left(s^{2} / n+1\right)^{-\left(\frac{n+1}{2}\right)} d s=\int_{\infty}^{0} u\left(\frac{u^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d u \\
& =-\int_{0}^{\infty} u\left(\frac{u^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d u
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\mu= & -\int_{0}^{\infty} u\left(\frac{u^{2}}{n}+1\right)^{-\frac{(n+1)}{2}} d u \\
& +\int_{0}^{\infty} s\left(\frac{s^{2}}{n+1}\right)^{-\frac{(n+1)}{2}} d s \\
& =0
\end{aligned}
$$

Now $n=1,2,3, \ldots$ when evaluating the difference above $t$ is assumed that the integrals are finite. If that is not the case then the result is indeterminate. The integrard scales like

$$
S S^{-(n+1)}=S^{-n}
$$

for $n>1$ the integral converces by for $n=1$ the integral will diverge, Conster the case $n=1$. The integral for the mean becomes

$$
\mu=\int_{0}^{\infty} s\left(s^{2}+1\right)^{-1} d s
$$

Let

$$
\begin{aligned}
u & =s^{2}+1 \\
\Rightarrow s & =\sqrt{u-1}
\end{aligned}
$$

$$
d s=\frac{1}{2} \sqrt{\frac{1}{u-1}} d u
$$

then

$$
\begin{aligned}
\mu & =\int_{0}^{\infty} s\left(s^{2}+1\right)^{-1} d s \\
& =\int_{1}^{\infty} \sqrt{(u-1)} \frac{1}{u}\left(\frac{1}{2}\right) \sqrt{\frac{1}{\sqrt{-1}}} d u \\
& =\frac{1}{2} \int_{1}^{\infty} \frac{1}{u} d u \\
& =\left.\frac{1}{2} \ln u\right|_{1} ^{\infty}=\infty
\end{aligned}
$$

To verify convergence of the integral for $n \geq 1$ consider the integral

$$
\int_{0}^{\infty} s\left(s^{2} n+1\right)^{-\frac{(n+1)}{2}}
$$

let

$$
\begin{aligned}
u & =\frac{s^{2}}{n}+1 \\
\Rightarrow s & =\sqrt{n(u-1)} \\
d s & =\frac{1}{2} \sqrt{\frac{n}{u-1}} d u
\end{aligned}
$$

then

$$
\begin{aligned}
\mu & =\int_{0}^{\infty} s\left(s^{2} / n+1\right)^{-\frac{(n+1)}{2}} d s \\
& =\int_{1}^{\infty} \sqrt{n(u-1)} \frac{1}{u^{\frac{n+1}{2}} \frac{1}{2} \sqrt{\frac{n}{u-1}} d u} \\
& =n \int_{1}^{\infty} u^{-\frac{(n+1)}{2}} d u \\
& =\left.n\left(\frac{-2}{n+3}\right) u^{-\left(\frac{n+3}{2}\right)}\right|_{1} ^{\infty} \\
& =\frac{2 n}{n+3}
\end{aligned}
$$

thus for $n=1 \quad \mu$ is wrdefined. and fmite for $n>1$

## In summary

$$
\mu=0 \text { for } n>1
$$

and $\mu$ is undefined for $n=1$

Next since $\mu=0$ the variance is given by

$$
\begin{aligned}
& \sigma^{2}=E\left(T^{2}\right)=\int_{-\infty}^{\infty} s^{2} T_{s}(n) d s \\
= & \frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n \pi} \Gamma\left(\frac{n}{2}\right)} \int_{-\infty}^{\infty} s^{2}\left(\frac{s^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s
\end{aligned}
$$

since the integrand is symmetric about the origin

$$
\begin{aligned}
\int_{-\infty}^{\infty} s^{2}\left(\frac{s^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s & \\
= & 2 \int_{0}^{\infty} s^{2}\left(\frac{s^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s
\end{aligned}
$$

let

$$
\begin{aligned}
u & =\frac{s^{2}}{n} \\
\Rightarrow \quad s & =\sqrt{n u} \\
\Rightarrow \quad d s & =\frac{1}{2} \sqrt{\frac{n}{u}} d u
\end{aligned}
$$

50

$$
\begin{aligned}
2 \int_{0}^{\infty} & s^{2}\left(s^{2} / n+1\right)^{-(n+1)} d s \\
& =2 \int_{0}^{\infty}(n u)(u+1)^{-\frac{(n+1)}{2}} \frac{1}{2} \sqrt{\frac{n}{u}} d u \\
& =(n)^{3 / 2} \int_{0}^{\infty} \frac{u^{1 / 2}}{(u+1)^{(n+1) / 2}} d u
\end{aligned}
$$

Recall that

$$
B(a, b)=\int_{0}^{\infty} \frac{x^{a-1}}{(1+x)^{a+b}} d x
$$

comparing with the integral above gives

$$
\begin{aligned}
& a=3 / 2 \\
& a+b=\frac{n+1}{2} \\
\Rightarrow & b=\frac{n+1}{2}-\frac{3}{2}=\frac{n}{2}-1
\end{aligned}
$$

$$
=\frac{n-2}{2}
$$

So

$$
\begin{aligned}
(n)^{3 / 2} & \int_{0}^{\infty} \frac{u^{1 / 2}}{(u+1)^{(n+1) / 2}} d u \\
& =(n)^{3 / 2} B\left(\frac{3}{2}, \frac{n-2}{2}\right) \\
& =(n)^{3 / 2} \frac{\Gamma(3 / 2) \Gamma\left(\frac{n-2}{2}\right)}{\Gamma\left(\frac{n+1}{2}\right)}
\end{aligned}
$$

Now

$$
\Gamma(3 / 2)=\frac{1}{2} \sqrt{\pi}
$$

and recall the Camma function relation

$$
\Gamma(a+1)=a \Gamma(a)
$$

50

$$
\Gamma\left(\frac{n}{2}\right)=\Gamma\left(\frac{n}{2}-1+1\right)=\Gamma\left(\frac{n-2}{2}+1\right)
$$

$$
\begin{aligned}
& =\frac{n-2}{2} \Gamma\left(\frac{n-2}{2}\right) \\
& \Rightarrow \Gamma\left(\frac{n-2}{2}\right)=\frac{2}{n-2} \Gamma\left(\frac{n}{2}\right)
\end{aligned}
$$

Putting things together gives

$$
\begin{aligned}
&(n)^{3 / 2} \int_{0}^{\infty} \frac{u^{1 / 2}}{(u+1)^{(n+1) / 2}} d u \\
&=(n)^{3 / 2} \Gamma\left(\frac{3 / 2}{2}\right) \Gamma\left(\frac{n-2}{2}\right) \\
& \Gamma\left(\frac{n+1}{2}\right)
\end{aligned}
$$

$=(n)^{3 / 2\left(\frac{1}{2} \sqrt{\pi}\right)\left(\frac{2}{n-2}\right) \Gamma\left(\frac{n}{2}\right)} \frac{\Gamma\left(\frac{n+1}{2}\right)}{}$
and finally the variance is given by

$$
\sigma^{2}=\int_{-\infty}^{\infty} s^{2} T_{s}(n) d s
$$

$=\frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n \pi} \Gamma\left(\frac{n}{2}\right)} \int_{-\infty}^{\infty} s^{2}\left(\frac{s^{2}}{n}+1\right)^{-\left(\frac{n+1}{2}\right)} d s$
$=\frac{\Gamma\left(\frac{n+1}{2}\right)}{\sqrt{n \pi} \Gamma\left(\frac{n}{2}\right)}(n)^{3 / 2} \int_{0}^{\infty} \frac{u^{1 / 2}}{(u+1)^{(n+1) / 2}} d u$
$=\frac{\Gamma\left(\frac{n+1}{2}\right)(n)^{3 / 2}}{\sqrt{n \pi}} \frac{\Gamma\left(\frac{1}{2} \sqrt{\pi}\right)\left(\frac{2}{n-2}\right) \Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{n+1}{2}\right)}$
$=\frac{n}{n-2}$

Thus

$$
\sigma^{2}=\frac{n}{n-2}
$$

Just as for the mean, $\sigma^{2}$ will not be defined for all values of $n$. From inspection
of the equation for $\sigma^{2} \quad n=2$ clearly has problems.

$$
\int_{0}^{\infty} s^{2}\left(s^{2} / n+1\right)^{-(n+1)} d s
$$

The integrand scales like

$$
s^{2} s^{-(n+1)} \sim s^{-n+1}
$$

which will be infinite for $n \leqslant 2$.
To check for convergence first consder the case $n=1$.

$$
\begin{aligned}
& \sigma^{2}=\int_{0}^{\infty} \frac{s^{2}}{s^{2}+1} d s \\
& \int_{0}^{\infty} 1-\frac{1}{s^{2}+1} d u
\end{aligned}
$$

To integrate the second term recall

$$
\begin{aligned}
& \sin ^{2} t+\cos ^{2} t=1 \\
\Rightarrow \quad & \tan ^{2} t+1=\sec ^{2} t
\end{aligned}
$$

let

$$
\begin{aligned}
& \quad s=\tan t \\
& \frac{d s}{d t}=\frac{d \tan t}{d t}=\frac{d}{d t} \frac{\sin t}{\cos t} \\
& =\frac{\cos t}{\cos t}+-\frac{\sin t}{\cos ^{2} t}(-\sin t) \\
& =1+\tan ^{2} t=\sec ^{2} t \\
& \Rightarrow d u=\sec ^{2} t d t
\end{aligned}
$$

then the integral becomes

$$
\int \frac{1}{u^{2}+1} d u=\int \frac{1}{\tan ^{2} t+1} \sec ^{2} t d t
$$

$$
\begin{aligned}
& =\int \frac{\sec ^{2} t}{\sec ^{2} t} d t \\
& =\int d t \\
& =t
\end{aligned}
$$

but

$$
\begin{aligned}
u & =\tan t \\
\Rightarrow t & =\arctan u
\end{aligned}
$$

thus

$$
\int \frac{1}{1+u^{2}} d u=\arctan u
$$

Putting things together

$$
\begin{aligned}
\sigma^{2}=\int_{0}^{\infty} & \frac{s^{2}}{s^{2}+1} d s \\
& =\int_{0}^{\infty} 1-\frac{1}{s^{2}+1} d u
\end{aligned}
$$

$$
\begin{aligned}
& =\left.(s-\operatorname{artan} s)\right|_{0} ^{\infty} \\
& =\infty
\end{aligned}
$$

Next consider $n=2$

$$
\sigma^{2}=\int_{0}^{\infty} \frac{s^{2}}{\left(s^{2} / 2+1\right)^{3 / 2}} d s
$$

let

$$
u=\frac{s}{\sqrt{2}} \quad \sqrt{2} d u=d s
$$

then

$$
\begin{aligned}
\sigma^{2} & =\int_{0}^{\infty} \frac{2 u^{2}}{\left(u^{2}+1\right)^{3 / 2}} \sqrt{2} d u \\
& =2^{3 / 2} \int_{0}^{\infty} \frac{u^{2}}{\left(u^{2}+1\right)^{3 / 2}} d u
\end{aligned}
$$

$$
\begin{aligned}
& =2^{3 / 2} \int_{0}^{\infty} \frac{u^{2}+1-1}{\left(u^{2}+1\right)^{3 / 2}} d u \\
& =2^{3 / 2} \int_{0}^{\infty} \frac{1}{\sqrt{u^{2}+1}}-\frac{1}{\left(u^{2}+1\right)^{3 / 2}} d u
\end{aligned}
$$

make the change of variables

$$
\begin{gathered}
u=\tan t \\
d u=\sec ^{2} t d t \\
\tan ^{2}+1=\sec ^{2} t
\end{gathered}
$$

then the integral is given by

$$
\begin{aligned}
& 2^{3 / 2} \int \frac{\sec ^{2} t}{\sec t}+\frac{\sec ^{2} t}{\sec ^{3} t} d t \\
& =2^{3 / 2} \int(\sec t+\cos t) d t
\end{aligned}
$$

Now

$$
\int \cos t d t=\sin t
$$

The sect integral is given by

$$
\begin{aligned}
& \int \sec t d t=\int \sec t \frac{(\sec t+\tan t)}{(\sec t+\tan t)} d t \\
& =\int \frac{\sec ^{2} t+\sec t \tan t}{(\sec t+\tan t)} d t
\end{aligned}
$$

make another change of variables

$$
\omega=\sec t+\tan t
$$

using

$$
\begin{aligned}
& \frac{d \sec t}{d t}=\frac{d}{d t} \frac{1}{\cos t}=-\frac{1}{(\cos t)^{2}}(-\sin t) \\
& =\frac{\sin t}{(\cos t)^{2}}=\sec t \tan t
\end{aligned}
$$

and

$$
\frac{d}{d t} \tan t=\frac{d}{d t} \frac{\sin t}{\cos t}
$$

$$
\begin{aligned}
& =\sin t \frac{d(\sec t)}{d t}+\frac{1}{\cos t} \frac{d}{d t} \sin t \\
& =\sin t(\sec t \tan t)+\frac{\cos t}{\cos t} \\
& =\sin t \sec t \tan t+1 \\
& =\tan ^{2} t+1 \\
& =\sec ^{2} t
\end{aligned}
$$

It follows that

$$
\begin{aligned}
d w & =\frac{d}{d t}(\sec t+\tan t) d t \\
& =\left(\sec t \tan t+\sec ^{2} t\right) d t
\end{aligned}
$$

making the change of variables gives
$\int \frac{\sec ^{2} t+\sec t \tan t}{(\sec t+\tan t)} d t$

$$
\begin{aligned}
& =\int \frac{1}{u} d u \\
& =\ln u
\end{aligned}
$$

thus

$$
\int \sec t d t=\ln (\sec t+\tan t)
$$

and it follows that

$$
\begin{aligned}
2^{3 / 2} & \int(\sec t+\cos t) d t \\
& =2^{3 / 2}[\ln (\sec t+\tan t)+\sin t]
\end{aligned}
$$

Now back to the original integral

$$
\sigma^{2}=2^{3 / 2} \int_{0}^{\infty} \frac{u^{2}}{\left(u^{2}+1\right)^{3 / 2}} d u
$$

making the change of variables

$$
u=\tan t=t=\arctan u
$$

produces the integral

$$
\begin{aligned}
\int(\sec t+\cos t) d t \\
=\ln (\sec t+\tan t)+\sin t \\
=\ln [\sec (\arctan u)+\tan (\arctan \omega)] \\
+\sin (\arctan u)
\end{aligned}
$$

## Now Consider

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-328.jpg?height=437&width=537&top_left_y=882&top_left_x=487)

$$
\begin{gathered}
\sin \theta=\frac{x}{\sqrt{1+x^{2}}} \quad \cos \theta=\frac{1}{\sqrt{1+x^{2}}} \\
\tan \theta=x
\end{gathered}
$$

it follows that

$$
\theta=\arctan x
$$

and

$$
\begin{aligned}
\sin \theta & =\sin (\arctan x) \\
& =\frac{x}{\sqrt{1+x^{2}}} \\
\sec \theta & =\frac{1}{\cos \theta}=\sqrt{1+x^{2}} \\
\Rightarrow \sec \theta & =\sec (\arctan x) \\
& =\sqrt{1+x^{2}}
\end{aligned}
$$

So

$$
\begin{aligned}
\int( & \sec t+\cos t) d t \\
= & \ln [\sec (\arctan u)+\tan (\arctan \omega)] \\
& +\sin (\arctan u) \\
= & \ln \left(\sqrt{1+x^{2}}+1\right)+\frac{x}{\sqrt{1+x^{2}}}
\end{aligned}
$$

and the final result is given by

$$
\begin{aligned}
\sigma^{2} & =2^{3 / 2} \int_{0}^{\infty} \frac{u^{2}}{\left(u^{2}+1\right)^{3 / 2}} d u \\
& \left.=2^{3 / 2}\left[\ln \left(\sqrt{1+x^{2}}\right)+1\right)+\frac{x}{\sqrt{1+x^{2}}}\right]\left.\right|_{0} ^{\infty} \\
& =\infty
\end{aligned}
$$

Thus for $n=2 \quad \sigma^{2}=\infty$.
In summary it has been shown that
for $n>1$

$$
\mu=0
$$

otherwise $\mu$ is undefined for $n>2$

$$
\sigma^{2}=\frac{n}{n-2}
$$

otherwise $\quad \sigma^{2}=\infty$.

The following plots show the t-distribution PDF, CDF and tail CDF for a range of values of the degrees of freedom $n$. The PDF plot also plots the unit normal distribution illustrating convergence as $n$ increases.

Student-t PDF, for Range of Degrees of Freedom Compared to Unit Normal
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-331.jpg?height=763&width=1154&top_left_y=830&top_left_x=173)

Student-t CDF, for Range of Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-332.jpg?height=769&width=1164&top_left_y=169&top_left_x=211)

Student-t Tail CDF, for Range of Degrees of Freedom Compared to Unit Normal
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-332.jpg?height=752&width=1168&top_left_y=1090&top_left_x=201)

The following plots show the results of triree simulations with $n=3,5$ and 20. Each simulation consists of. an ensemble of 1000 trials which is used to estimate the PDF. The PDF is then compared to $T_{n}(t)$ and $\mu$ and $\sigma^{2}$.
The implimentation of the simcilation is as follows. For each trial $n$ independet and Normal $\left(\mu, \sigma^{2}\right)$ are generated. $\bar{x}_{n}$ and $s_{n}^{2}$ are then evaluted and used to compute a realization of $t$.

t-Test Sampled Distribution 1000 Trails, 3 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-333.jpg?height=501&width=745&top_left_y=1442&top_left_x=372)

t-Test Sampled Distribution 1000 Trails, 5 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-334.jpg?height=555&width=833&top_left_y=133&top_left_x=342)

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-334.jpg?height=563&width=799&top_left_y=798&top_left_x=382)
The fit to the disfribution for each simulation is acceptable.

The convergence of moments is very slow for a low number of degrees of freedsm. This is
illustrated in the following plots. The first shows the result of a simulation with $n=3$ degrees of freedom with 100,000 trials. $10^{4}$ timesteps are required for $u$ to settle to the asymptotic value of 0 but $\sigma^{2}$ has yet to settle to the asymptotic This is because of the fat tail the distribution has for a low number of degrees of freedom. It is casy to see that events far in the tail occur creating the large deviations from the asymtotic oclue.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-335.jpg?height=535&width=870&top_left_y=1394&top_left_x=378)

t-Test Cumulative $\sigma 100000$ Trails, 3 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-336.jpg?height=545&width=1005&top_left_y=219&top_left_x=386)

The following plots show the result of an $n=20$ simulation in which both the mean and oariance both approach their asymptotic values with $\sim 1000$ trials.

t-Test Cumulative $\mu 100000$ Trails, 20 Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-336.jpg?height=581&width=928&top_left_y=1364&top_left_x=340)

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-337.jpg?height=654&width=948&top_left_y=173&top_left_x=338)

## t-Test Examples

In this section examples vising the $t$-test are solved.
Recall that for a set of $n$ samples

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

with known population mean, $\mu$, and sample variance

$$
S_{n}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\mu\right)^{2}
$$

and sample mean

$$
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

The $t$-statistic is defined by,

$$
t=\frac{\bar{x}_{n}-\mu}{s_{n} / \sqrt{n}}
$$

If the $x_{i}$ are assumed to be normally distributed and the numerator and denominator of $t$ are assumed to be independent then $t$ has the student t-distribution

$$
\begin{gathered}
t \sim T_{n}(t) \\
T_{n}(t)=\frac{1}{\sqrt{\pi n}} \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}\left(\frac{t^{2}}{n}+1\right)^{-\frac{(n+1)}{2}}
\end{gathered}
$$

The CDF is given by

$$
P(t \leqslant T)=1-\frac{1}{2} I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)
$$

and tail CDF

$$
P(t \geqslant T)=\frac{1}{2} I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)
$$

Where $I_{t}\left(\frac{n}{2}, \frac{1}{2}\right)$ is the regularized incomplete Beta function. The mean and varrance of
$t$ are given by,
for $n>1$

$$
\mu=0
$$

otherwise $\mu$ is undefined for $n>2$

$$
\sigma^{2}=\frac{n}{n-2}
$$

otherwise $\quad \sigma^{2}=\infty$.
Unlike the chi-squared distribution, which has a single tail, the student -t distribution has two tails. To define the confidence interval both tails need to be considered. This is illustrated in the following plot where a level of significance of 0.05 is assumed
indicated which is the values of $t$ lying between prodabilities 0.25 and 0.975

$$
P\left(t_{1} \leqslant t \leqslant t_{2}\right)=0.95
$$

Student-t CDF, Number of Degrees of Freedom: 3
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-341.jpg?height=767&width=1172&top_left_y=594&top_left_x=163)

An acceptance interval of this type is used in two-sided test. It is also possible to have one-sided tests. Acceptance intervals of this type are illustrated in the following figures.

$$
P\left(t_{1} \leqslant t\right)=0.95
$$

Student-t CDF, Number of Degrees of Freedom: 3
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-342.jpg?height=765&width=1156&top_left_y=245&top_left_x=163)

$$
P\left(t_{2} \geqslant t\right)=0.95
$$

Student-t CDF, Number of Degrees of Freedom: 3
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-342.jpg?height=757&width=1170&top_left_y=1229&top_left_x=211)

## One sample $t$-Test

A one sample $t$-Test consists of a single sample of $n$ observations

$$
x_{1}, x_{2}, x_{3}, \ldots, x_{n}
$$

The test on the sample can be one or two sided. A one sample test is used to determine if the sample mean is equal to the known population mean, $\mu$.

* The two-sided test can be stated as,
Null Hypothesis $H_{0}$ : The sample mean is equal to $\mu$.
Alternative Hypothesis $H_{A}$ : The sample mean is not equal to $\mu$

There are two possible one sided tests

* Null Hypothesis Ho : The sample mean is equal to $\mu$.
Alternative Hypothesis $H_{A}$ : The sample mean is less than $\mu$.
* Null Hypothesis Ho: The sample mean is equal to $\mu$.
Atternative Aypothesis $H_{A}$ : The sample mean is greater than $\mu$.


## One Sample Two Tailed t-Test

A cottee shop requires 402 of espresso for lattes. A random sample of 25 lattes has sample mean and Standard deviation

$$
\begin{aligned}
& \bar{x}=4,6 \mathrm{oz} \\
& \sqrt{\mathrm{~s}}=0,22 \mathrm{oz}
\end{aligned}
$$

using a one sample two-tailed test the null hypothesis is
$H_{0}$ : The average espresso per batte is 402.
The alternative hypothesis is
$H_{A}$ : The average espresso per latte is not $40 z$.

The $t$-statistic is given by

$$
t=\frac{\sqrt{n}(\bar{x}-\mu)}{s}
$$

Here

$$
\begin{array}{ll}
\mu=4 & \bar{x}=4.6 \\
n=25 & s=0.22
\end{array}
$$

80

$$
\begin{aligned}
t & =\frac{\sqrt{25}(4.6-4)}{0.22} \\
& =13.6
\end{aligned}
$$

The degrees of freedom of the $t$-distribution is

$$
d f=n-1=24
$$

The following plot illustrates the confidence intervals for a signifance level of

$$
\alpha=0.05
$$

for two tails. Since the total acceptance level for both tails is 0.05 each tail will contribute 0.025 . This is indicated in
the plot of the Tail CDF of the $t$-distribution below where the ranges of the values of $t$ where $H_{0}$ and $H_{a}$ are accepted.

Student-t Tail CDF, Number of Degrees of Freedom: 24
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-347.jpg?height=753&width=1332&top_left_y=614&top_left_x=130)

Let $F(t)$ indicate the tail CDF which is given by

$$
F(t)=\frac{1}{2} I_{t}\left(\frac{d f}{2}, \frac{1}{2}\right)
$$

where $I_{+}\left(\frac{f}{2}, \frac{1}{2}\right)$ is the regularized incomplete Beta function.

The left cutoff for acceptance is determined by

$$
\begin{aligned}
& F(2.05)=0.975 \\
& F(2.05)=0.025
\end{aligned}
$$

It follows that for

$$
-2.05 \leqslant t \leqslant 2.05
$$

$H_{0}$ is accepted otherwise it is accepted.
For the sample of 25 lattes given

$$
t=13.6
$$

thus the null hypothesis that the sample has 402 of espresso per latte is rejected and
the Altornative hypothesis that the population mean of the sample is not 402 is accepted. The reasoning for this is that
within the significance level assumption of $\alpha=0.05$ the truth of the null hypothesis, that the mean comount of espresso per latte is 402, is improbable
Note that

$$
F(t)=F(13.6)=4.24 \times 10^{-13}
$$

is the probability of a $t$-stastistic having a value of at least 13.6. This event is very improbable within the assumptions of a population mean of 402 and the doserved sample mean and variance.

## One Sample Right Tailed $t$-Test

The next example is the same as the previous but using a different atternative hypothers requiring the use of a one-sided test.
Recall that the population mean of the amount of espresso per latte is 402 and for a scample of 25 lattes the sample mean and variance are

$$
\begin{aligned}
& \bar{x}=4.6 \mathrm{oz} \\
& \sqrt{s}=0.22 \mathrm{oz}
\end{aligned}
$$

using a one sample right-tailed test the null hypothesis is
$H_{0}$ : The average espresso per bate is 402.

The alternative nypothesis is
$H_{A}$ : The average espresso per latte is greater than $40 z$.

The $t$-statistic is groen by

$$
t=\sqrt{n} \frac{(\bar{x}-\mu)}{s}
$$

Here

$$
\begin{array}{ll}
\mu=4 & \bar{x}=4.6 \\
n=25 & s=0.22
\end{array}
$$

80

$$
\begin{aligned}
t & =\frac{\sqrt{25}(4.6-4)}{0.22} \\
& =13.6
\end{aligned}
$$

The degrees of freedom of the $t$-distribution is

$$
d f=n-1=24
$$

The following plot illustrates the confedence intervals for a signifance level of

$$
\alpha=0.05
$$

Student-t Tail CDF, Number of Degrees of Freedom: 24
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-352.jpg?height=815&width=1321&top_left_y=580&top_left_x=135)

If $F(t)$ is the tail CDF for 24 degrees of freedom, shown above, the cutoff value of $t$ for accoptane of $H_{0}$ is the value of $t$ satisfying

$$
F(1.71)=\alpha=0.05
$$

were. Thus $H_{0}$ is accepled for

$$
t \leqslant 1.71
$$

and $H_{A}$ is accepted for

$$
t>1.71
$$

For the 25 latte sample the $t$-statistic was found to be

$$
t=13.6
$$

Thus $H_{A}$ is accepted, that the population mean is greater than 402 . Since the probablitity of $t$ values greater tran or equal to $B, 6$
$P(t \geqslant 13,6)=F(B, 6)=4.24 \times 10^{-13}$
This is considered an improbabable event assuming a level of significance of $\alpha=0.05$

## One sample Left-Tailed $t$-Test

In this final example the same latte problem previously discussed is revisited but with a different alternative Hypothesis.
The problem is to determine if a sample of 25 lattes has the required 402 of espresso. The $t$-statistic of the sample is

$$
t=13.6
$$

This time a let tailed atternative hypothesis is assumed. The null hypothesis is
$H_{0}$ : The average espresso per batte is 402 .
The alternative hypothesis is
$H_{A}$ : The average espresso pe latte is less than 402.

The following plot illudrates the range of $t$-values were each hypothesis is accepted if a significance level of

$$
\alpha=0.05
$$

Student-t Tail CDF, Number of Degrees of Freedom: 24
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-355.jpg?height=813&width=1337&top_left_y=663&top_left_x=207)

Thus the null hypothesis is accepted if

$$
-1.71 \leqslant t
$$

and the altterative hypothesis is accepted if

$$
-1.71 \geqslant t
$$

where

$$
\begin{aligned}
F(-1.71) & =0.95 \\
& =1-\alpha
\end{aligned}
$$

The $t$-statistic for the sample is

$$
t=13.6
$$

It follows that for a left-tailed alteranative hypotheis $H_{0}$ is accepted. So the sample has 402 of espresso per latte if a left-tailed alternative myothesis is assumed. This is in contrast to the other alternatice hypothesis assumptions which led to a rejection of the null hypothesis.

## Two sample $t$-Test

A two sample test is used to compare two seperate samples

$$
\begin{aligned}
& x_{1}, x_{2}, x_{3}, \ldots, x_{n} \\
& y_{1}, y_{2}, y_{3}, \ldots, y_{m}
\end{aligned}
$$

If the samples are of equal size $n=m$ the test is called paired and the sample is compared pairwise. If the sample sizes are different the sample means are compare.
The Hypothesis for each ase can be stated as follows

* Paired Two-Sample t-Test.

For the paried test the difference between the processes

Is computed

$$
d_{i}=x_{i}-y_{i}
$$

and the Null and Alternative Hypothesis are given by
Null Hypothesis Ho: The mean of the sample differece is 0 , the samples have the same mean.

Alternative Hypothesis $H_{A}$ : The mean of the sample difference is not 0 .

* Unparred Two-Sample $t$-Test. If $\mu_{x}$ is the mean of the $x_{i}$ samples and $\mu_{y}$ the mean of the $y_{i}$ samples Null Hypothesis Ho: The mean of the tw samples is equal, $\mu_{x}=\mu_{y}$


## Alternative Hypothesis $H_{A}$ : The

mean of the two samples is different, $\mu_{x} \neq \mu_{y}$

To determine the $t$-statistic recall that it is assumed that

$$
\begin{aligned}
& x \sim \operatorname{Normal}\left(\mu_{x}, \sigma_{x}^{2}\right) \\
& y \sim \operatorname{Normal}\left(\mu_{y}, \sigma_{y}^{2}\right)
\end{aligned}
$$

From the central limit theorem it follows that

$$
\begin{aligned}
& \sqrt{n}\left(\bar{x}_{n}-\mu_{x}\right) \sim \operatorname{Normal}\left(0, \sigma_{x}^{2}\right) \\
\Rightarrow & \bar{x}_{n}-\mu_{x} \sim \operatorname{Normal}\left(0, \sigma_{x}^{2} / n\right)
\end{aligned}
$$

and

$$
\bar{y}_{m}-\mu_{y} \sim \operatorname{Normal}\left(0, \sigma_{y}^{2} / m\right)
$$

If $\bar{x}_{n}$ and $\bar{y}_{m}$ are assumed to be independent, and using

$$
\begin{aligned}
& \bar{X}_{n} \sim \operatorname{Normal}\left(\mu_{x}, \sigma_{x / n}^{2}\right) \\
& \bar{Y}_{m} \sim \operatorname{Normal}\left(\mu_{y}, \sigma_{y / m}^{2}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
f\left(\bar{x}_{n}, \bar{y}_{m}\right) & =\frac{1}{2 \pi \left\lvert\, \frac{\sigma_{x}^{2} \sigma_{y}^{2}}{n m}\right.} \exp \left[\frac{n\left(\bar{x}_{n}-\mu_{x}\right)^{2}}{\sigma_{x}^{2}}\right. \\
& \left.+\frac{m\left(\bar{y}_{m}-\mu_{y}\right)^{2}}{\sigma_{y}^{2}}\right]
\end{aligned}
$$

Consider

$$
\begin{aligned}
& E\left(\bar{x}_{n}-\bar{y}_{m}\right)=\mu_{x}-\mu_{y} \\
& \operatorname{Uar}\left(\bar{x}_{n}-\bar{y}_{m}\right) \\
& \quad=E\left[\left(\bar{x}_{n}-\bar{y}_{n}\right)^{2}\right]-\left[E\left(\bar{x}_{n}-\bar{y}_{n}\right)\right]^{2}
\end{aligned}
$$

$$
\begin{aligned}
= & E\left(\bar{x}_{n}^{2}-2 \bar{x}_{n} \bar{y}_{m}+\bar{y}_{m}^{2}\right)-\left(\mu_{x}-\mu_{y}\right)^{2} \\
= & E\left(\bar{x}_{n}^{2}\right)+E\left(\bar{y}_{m}^{2}\right)-2 E\left(\bar{x}_{n}^{2}\right) E\left(y_{n}\right) \\
& -\mu_{x}^{2}-\mu_{y}^{2}+2 \mu_{x} \mu_{y} \\
= & E\left(\bar{x}_{n}^{2}\right)-\mu_{x}^{2}+E\left(\bar{y}_{m}^{2}\right)-\mu_{y} \\
= & \operatorname{var}\left(\bar{x}_{n}\right)+\operatorname{var}\left(\bar{y}_{m}\right) \\
= & \frac{\sigma_{x}^{2}}{n}+\frac{\sigma_{y}^{2}}{m}
\end{aligned}
$$

thus

$$
\begin{aligned}
& E\left(\bar{x}_{n}-\bar{y}_{m}\right)=\mu_{x}-\mu_{y} \\
& \operatorname{var}\left(\bar{x}_{n}-\bar{y}_{m}\right)=\frac{\sigma_{x}^{2}}{n}+\frac{\sigma_{y}^{2}}{m}
\end{aligned}
$$

and finally the distribution of the difference is given by

$$
\bar{X}_{n}-\bar{Y}_{m} \sim \operatorname{Normal}\left(\mu_{x}-\mu_{y}, \frac{\sigma_{y}^{2}}{n}+\frac{\sigma_{y}^{2}}{m}\right)
$$

It follows that

$$
t=\frac{\bar{x}_{n}-\bar{y}_{m}-\left(\mu_{x}-\mu_{y}\right)}{\sqrt{\frac{s_{x}^{2}}{n}+\frac{s_{y}^{2}}{m}}}
$$

In the two sample test it is assumed that

$$
\mu_{x}=\mu_{y}
$$

and in calculation of the sample variance, since $\mu_{x}$ and $\mu_{y}$ are assumed unknown and replaced with $\bar{x}_{n}$ and $\bar{y}_{m}$ in the calculation of the sample variance. It follows

$$
t=\frac{\bar{x}_{n}-\bar{y}_{m}}{\sqrt{\frac{s_{y}^{2}}{n}+\frac{s_{y}^{2}}{m}}}
$$

and

$$
\begin{aligned}
& s_{y}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2} \\
& s_{y}^{2}=\frac{1}{m-1} \sum_{i=1}\left(y_{i}-\bar{y}_{n}\right)^{2}
\end{aligned}
$$

For the paired sample case let

$$
d_{i}=x_{i}-y_{i}
$$

then using $m=n$ and

$$
\bar{d}_{n}=\bar{x}_{n}-\bar{y}_{n}
$$

and

$$
\begin{aligned}
s_{D}^{2}= & \frac{1}{n-1} \sum_{i=1}^{n}\left(d_{i}-\bar{d}_{n}\right)^{2} \\
= & \frac{1}{n-1} \sum_{i=1}^{n}\left[\left(x_{i}-\bar{x}_{n}\right)-\left(y_{i}-\bar{y}_{n}\right)\right]^{2} \\
= & \frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2}+\left(y_{-} \bar{y}_{n}\right)^{2} \\
& -2\left(x_{i}-\bar{x}_{n}\right)\left(y_{i}-\bar{y}_{n}\right) \\
= & s_{x}^{2}+s_{y}^{2}-2 \sum_{i=1}^{n}\left(x_{i} y_{i}-x_{i} \bar{y}_{n}\right. \\
& \left.-y_{i} \bar{x}_{n}+\bar{x}_{n} \bar{y}_{n}\right) \\
= & s_{x}^{2}+s_{y}^{2}-2 \sum_{i=1}^{n} x_{i} y_{i}+2 n \bar{x}_{n} \bar{y}_{n}
\end{aligned}
$$

$$
+2 n \bar{x}_{n} \bar{y}_{n}-2 n \bar{x}_{n} \bar{y}_{n}
$$

But since $x_{i}$ and $y_{i}$ are assumed independent

$$
2 \sum_{i=1}^{n} x_{i} y_{i}=2 n \bar{x}_{n} \bar{y}_{n}
$$

thus

$$
\delta_{D}^{2}=\delta_{x}^{2}+\delta_{y}^{2}
$$

It follows that the t-stastic for the parred sample test is given by

$$
t=\frac{\bar{d}_{n}}{\sqrt{S_{D}^{2} / n}}
$$

where

$$
\begin{aligned}
& \bar{d}_{n}=\bar{x}_{n}-\bar{y}_{n} \\
& s_{D}^{2}=s_{x}^{2}+s_{y}^{2}
\end{aligned}
$$

The number of degrees of freedom is given by

$$
d f=n-1
$$

For the conpaired sample test the $t$-statistic is given by

$$
t=\frac{\bar{x}_{n}-\bar{y}_{m}}{\sqrt{\frac{s_{x}^{2}}{n}+\frac{s_{y}^{2}}{m}}}
$$

the number of derees of
freedom used in the $t$-distribution is not straight forward. It is approximated by the harmonc mean

$$
\frac{2}{\frac{1}{n}+\frac{1}{m}}
$$

Another opproximation is called variance pooling which assumes that the variaces of $x$ and $y$ are equal so the samples are aggregated in the variance estimation. Let

$$
s^{2}=s_{x}^{2}=s_{y}^{2}
$$

then

$$
\begin{aligned}
& s_{x}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2} \\
& s_{y}^{2}=\frac{1}{m-1} \sum_{i=1}^{n}\left(y_{i}-\bar{y}_{n}\right)^{2}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow(n-1) s_{x}^{2}+(m-1) s_{y}^{2} \\
&= \sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2}+\sum_{i=1}^{m}\left(y_{i}-\bar{y}_{n}\right)^{2} \\
& \Rightarrow s^{2}=\frac{1}{m+n-2}\left[\sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2}+\right. \\
&\left.\sum_{i=1}^{m}\left(y_{i}-\bar{y}_{n}\right)^{2}\right]
\end{aligned}
$$

Thus for posled variances

$$
t=\frac{\bar{x}_{n}-\bar{y}_{m}}{s^{2} \sqrt{\frac{1}{m}+\frac{1}{n}}}
$$

$$
\begin{array}{r}
s^{2}=\frac{1}{m+n-2}\left[\sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2}+\right. \\
\left.\sum_{i=1}^{m}\left(y_{i}-\bar{y}_{n}\right)^{2}\right]
\end{array}
$$

The number of degrees of freedsm of the t-distribution is

$$
m+n-2
$$

## Paired Two Sample t-Test

A paired two sample $t$-test compares the sample means of two equal sized samples pairwize to determine if the population means are the same.
In this example an analysis is performed to determine if there is a difference between the salary for the same job in Borse, Idaha and los Angeles, CA.
The sataries of 6 employees in the 25 'th percentile are listed below

| Profession |  | Bozse |  |
| :--- | :--- | :--- | :--- |
| Executive Chef |  | 53,047 |  |
| Cenetic Cownselor | 49,958 |  | 58,850 |
| Grants writer | 41,974 | 49,445 |  |
| Librarian | 44,366 | 52,263 |  |
| School Teacher | 40,470 | 47,674 |  |
| Social worker | 36,963 | 43,542 |  |

Let $x_{i}$ and $y_{i}$ represent the LA and Boise samples respectively. The $t$-statistic is given by

$$
t=\frac{\bar{x}_{n}-\bar{y}_{n}}{\sqrt{\frac{s_{x}^{2}}{n}+\frac{s_{y}^{2}}{n}}}
$$

where

$$
\begin{aligned}
& s_{x}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(x_{i}-\bar{x}_{n}\right)^{2} \\
& s_{y}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\bar{y}_{n}\right)^{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& d=x-y=\underset{7204 ., 6579 .]}{[9443 ., 8892.7471 ., 7897 .,} \\
& \bar{d}=7914.33 \\
& S_{D}=1074.91
\end{aligned}
$$

$$
t=\frac{\bar{d}}{5 b / \sqrt{n}}=18.04
$$

First Consider a two tailed test. The null hpothesis is
$H_{0}$ : The mean salary in LA and Boise are the same.
and the alternative hypothesis is
$H_{1}$ : The mean salary in LA and Boise are not the same.
If a signifance level of 0.05 is assumed the $t$-static cutoff values are given by

$$
\begin{aligned}
& F(2.571)=0.025=P(t \geqslant 2.571) \\
& F(-2.571)=0.975=P(t \leqslant-2.571)
\end{aligned}
$$

where $F(t)$ is the $t$-distribution tail CDF. The intervals for $t$ where $H_{0}$ or $H_{1}$ are accepted
is shown in the plot of $F(t)$ below

Student-t Tail CDF, Number of Degrees of Freedom: 5
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-371.jpg?height=777&width=1261&top_left_y=380&top_left_x=213)

Clearly $t=18.04$ falls in the interoal

$$
t \geqslant 2.57(
$$

thus the null hypothesis is rejected and the atternative hypothesis is accepted. It follows tract the mean salaries in LA and Bose are not equal. in fact

$$
F(18,04)=4,81 \times 10^{-6}
$$

Thus the probability of obtaining a oalue of at least $t=18.04$ is $4.81 \times 10^{-6}$. which is considered highly improbable given the assumption that the mean salaries in the otties are equal.
Finally consider a right single tail atternative hypothesis,
$H_{0}$ : The mean salary in Bose and $L A$ are equal.
$H_{A}$ : The mean salary in $\angle A$ is greater than in Borse.

Assuming a significance level of 0.05 the cutoff value for the $t$-statistic is given by

$$
F(2.01)=0.05=P(t \geqslant 2.01)
$$

The intervals for acceptance of
$H_{0}$ and $H_{A}$ are shown below

Student-t Tail CDF, Number of Degrees of Freedom: 5
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-373.jpg?height=761&width=1263&top_left_y=316&top_left_x=197)

clearly $t=18.04$ falls in the interval

$$
t \geqslant 2,01
$$

thus $H_{0}$ is rejected and $H_{A}$ is accepted. So the mean sakury in LA is greater tran in Boise.

## The Dickey-Fuller Test

Consider the AR(1) process difference equation,

$$
x_{t}=q x_{t-1}+\varepsilon_{t} \quad t=1,2,3, \ldots
$$

where the $\varepsilon_{t}$ are independent identically distributed random variables with distribution

$$
\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

and $x_{0}$ is assumed given.
By recursive substitution using the difference equation it can be shown that,

$$
x_{t}=\phi^{t} x_{0}+\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i}
$$

Using this expression and the assumptions

$$
E\left(\varepsilon_{t}\right)=0 \quad E\left(\varepsilon_{t}^{2}\right)=\sigma^{2}
$$

It can be shown that the expectations conditioned on the initial value are given by

$$
E\left(x_{t} \mid x_{0}\right)=\varphi^{t} x_{0}
$$

$$
\begin{aligned}
& \operatorname{Var}\left(x_{t} \mid x_{0}\right)=E\left(x_{t}^{2} \mid x_{0}\right)-\left(E\left(x_{t} \mid x_{0}\right)\right)^{2} \\
& =\sigma^{2} \frac{\left[1-\left(\varphi^{2}\right)^{t-1}\right]}{1-\varphi^{2}} \\
& \operatorname{Cov}\left(x_{t} x_{t+n} \mid x_{0}\right)=E\left(x_{t} x_{t+n} \mid x_{0}\right) \\
& -E\left(x_{t} \mid x_{0}\right) E\left(x_{t+n} \mid x_{0}\right) \\
& =\phi^{n} \operatorname{Uar}\left(x_{t} \mid x_{0}\right)
\end{aligned}
$$

computing expectation by conditioning the unconditioned mean is given by.

$$
\begin{aligned}
E\left(x_{t}\right) & =E\left(E\left(x_{t} \mid x_{0}\right)\right) \\
& =\phi^{t} E\left(x_{0}\right)
\end{aligned}
$$

$E\left(x_{t}\right)$ is independent of $t$ only if

$$
E\left(x_{0}\right)=0
$$

leading to

$$
E\left(x_{t}\right)=0
$$

for all $t$.
Similarly the unconditioned variance is given by

$$
\begin{aligned}
\operatorname{Var}\left(x_{t}\right)= & E\left(x_{t}^{2}\right)-\left[E\left(x_{t}\right)\right]^{2} \\
= & E\left[E\left(x_{t}^{2} \mid x_{0}\right)\right]-\left[E\left(E\left(x_{t} \mid x_{0}\right)\right)\right]^{2} \\
= & E\left[E\left(x_{t}^{2} \mid x_{0}\right)-\left(E\left(x_{t} \mid x_{0}\right)\right)^{2}+\right. \\
& \left.\left(E\left(x_{t} \mid x_{0}\right)\right)^{2}\right]-\left[E\left(E\left(x_{t} \mid x_{0}\right)\right)\right]^{2} \\
= & E\left[E\left(x_{t}^{2} \mid x_{0}\right)-\left(E\left(x_{t} \mid x_{0}\right)\right)^{2}\right]
\end{aligned}
$$

$$
\begin{aligned}
&+E\left[\left(E\left(X_{t} \mid X_{0}\right)\right)^{2}\right]+\left[E\left(E\left(X_{t} \mid X_{0}\right)\right)\right]^{2} \\
&= E\left[\operatorname{Var}\left(X_{t}^{2} \mid X_{0}\right)\right]+\operatorname{Var}\left[E\left(X_{t} \mid X_{0}\right)\right] \\
& \hline
\end{aligned}
$$

Consider the first term

$$
\begin{aligned}
& E\left[\operatorname{var}\left(x_{t}^{2} \mid x_{0}\right)\right] \\
& =E\left[\frac{\sigma^{2}\left[1-\left(\varphi^{2}\right)^{t-1}\right]}{1-\varphi^{2}}\right] \\
& =\sigma^{2} \frac{\left[1-\left(\varphi^{2}\right)^{t-1}\right]}{1-\varphi^{2}} \\
& =\frac{\sigma^{2}}{1-\varphi^{2}}-\frac{\sigma^{2}\left(\varphi^{2}\right)^{t-1}}{1-\varphi^{2}}
\end{aligned}
$$

and for the second term

$$
\begin{aligned}
& \operatorname{Var}\left[E\left(x_{t} \mid x_{0}\right)\right]=\operatorname{var}\left(\phi^{t} x_{0}\right) \\
& =\phi^{2 t} \operatorname{var}\left(x_{0}\right)
\end{aligned}
$$

Thus

$$
\begin{aligned}
& \operatorname{var}\left(x_{t}\right)=\frac{\sigma^{2}}{1-\varphi^{2}}-\frac{\sigma^{2}\left(\varphi^{2}\right)^{t-1}}{1-\varphi^{2}} \\
& +\varphi^{2 t} \operatorname{var}\left(x_{0}\right) \\
& =\frac{\sigma^{2}}{1-\varphi^{2}}+\varphi^{2 t}\left[\operatorname{var}\left(x_{0}\right)-\frac{\sigma^{2}}{\varphi^{2}\left(1-\varphi^{2}\right)}\right]
\end{aligned}
$$

$\operatorname{var}\left(x_{t}\right)$ is independent of time only if

$$
\operatorname{Var}\left(x_{0}\right)=\frac{\sigma^{2}}{\varphi^{2}\left(1-\varphi^{2}\right)}
$$

for all $t$. Since $\operatorname{var}\left(x_{0}\right)>0$ and must be finite it follows that

$$
|q|<1 .
$$

If the conditions are met the AR(1) process is said to be covariance stationary.
In summary for a finite $t$
an AR(1) process is stationary If the following conditions are met then for,

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

where

$$
\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

and

$$
\begin{aligned}
E\left(x_{0}\right) & =0 \\
\operatorname{Var}\left(x_{0}\right) & =\frac{\sigma^{2}}{\varphi^{2}\left(1-\varphi^{2}\right)} \\
|q| & <1
\end{aligned}
$$

then

$$
\begin{aligned}
E\left(x_{t}\right) & =0 \\
\operatorname{var}\left(x_{t}\right) & =\frac{\sigma^{2}}{1-\varphi^{2}} \\
\operatorname{Cov}\left(x_{t} x_{t+\tau}\right) & =\varphi^{\tau} \frac{\sigma^{2}}{1-\varphi^{2}}
\end{aligned}
$$

The same result can be obtained by taking the limit $t \rightarrow \infty$ as well as the condition that $|\varphi|<1$.

The same expressions for the mean, variance and covariance of $x_{t}$ can also be obtained from the AR(1) difference equation by assuming

$$
\begin{gathered}
E\left(X_{0}\right)=0 \\
|\varphi|<1
\end{gathered}
$$

and that the mean, variance and covariance are independent of time,

$$
\begin{aligned}
& E\left(x_{t}\right)=E\left(x_{t-1}\right) \\
& \operatorname{var}\left(x_{t}\right)=\operatorname{var}\left(x_{t-1}\right)
\end{aligned}
$$

thus since $E\left(x_{0}\right)$ is zero

$$
\begin{aligned}
E\left(x_{t}\right) & =E\left(\phi x_{t-1}+\varepsilon_{t}\right) \\
& =\phi E\left(x_{t-1}\right)+E\left(\varepsilon_{t}\right)
\end{aligned}
$$

but it is assumed that

$$
\begin{gathered}
E\left(\varepsilon_{t}\right)=0 \\
E\left(x_{t}\right)=E\left(x_{t-1}\right)
\end{gathered}
$$

Thus

$$
\begin{aligned}
E\left(x_{t}\right) & =\varphi E\left(x_{t-1}\right) \\
& =\varphi E\left(x_{t}\right)
\end{aligned}
$$

Since $|\varphi|<1$ for this expression to be true. It must be that

$$
E\left(x_{t}\right)=0
$$

similarly

$$
\begin{aligned}
\operatorname{var}\left(x_{t}\right) & =E\left(x_{t}^{2}\right)-\left(E\left(x_{t}\right)\right)^{2} \\
& =E\left(x_{t}^{2}\right) \\
& =E\left[\left(\varphi x_{t-1}+\varepsilon_{t}\right)^{2}\right]
\end{aligned}
$$

$$
=E\left(\phi^{2} x_{t-1}^{2}+2 \phi x_{t-1} \varepsilon_{t}+\varepsilon_{t}^{2}\right)
$$

but

$$
E\left(x_{t-1} \varepsilon_{t}\right)=0
$$

which follows from

$$
x_{t}=\phi^{t} x_{0}+\sum_{i=1}^{t} \phi^{t-i} \varepsilon_{i}
$$

and the assumption that the $\varepsilon_{i}$ are independent. Thus

$$
\begin{aligned}
\operatorname{Var}\left(x_{t}\right) & =\varphi^{2} E\left(x_{t-1}^{2}\right)+E\left(\varepsilon_{t}^{2}\right) \\
& =\varphi^{2} \operatorname{Var}\left(x_{t}\right)+\sigma^{2} \\
\Rightarrow \operatorname{Var}\left(x_{t}\right) & =\frac{\sigma^{2}}{1-\varphi^{2}}
\end{aligned}
$$

Finally,

$$
\begin{aligned}
\operatorname{Cov}\left(x_{t} x_{t+\tau}\right) & =\phi^{\tau} U \operatorname{car}\left(x_{t}\right) \\
& =\phi^{\tau} \frac{\sigma^{2}}{1-\phi^{2}}
\end{aligned}
$$

## SLR Estimate of AR(1) Parameters

Simple Linear Regression (SLR) can be used to estimate the $\Phi$ parameter in an AR(1) process.
Recall that for the linear model

$$
\varepsilon_{i}=y_{i}-\alpha-\beta x_{i}
$$

where there are $n$ observations of $y_{i}$ and $x_{i}$

$$
\begin{aligned}
& y=\left\{y_{0}, y_{1}, y_{2}, \ldots, y_{n}\right\} \\
& x=\left\{x_{0}, x_{1}, x_{2}, \ldots, x_{n}\right\}
\end{aligned}
$$

and $i t$ is assumed that the $\varepsilon_{i}$ are independent with distribution

$$
\varepsilon_{i} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

then the SLR estimates of $\hat{\alpha}$ and $\hat{\beta}$ are given by

$$
\begin{gathered}
\begin{array}{l}
\bar{y}=\frac{1}{n} \sum_{i=1}^{n} y_{i} \\
\hat{\alpha}=\bar{x}=\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
\hat{\beta}=\frac{\hat{\operatorname{cov}(x, y)}}{\operatorname{var}(x)}
\end{array} \\
\operatorname{Var}(\hat{\beta})=\frac{\sigma^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}} E(\hat{\beta})=\beta \\
\operatorname{Var}(x)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \\
\operatorname{Cov}(x y)=\frac{1}{n} \sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)
\end{gathered}
$$

If $t$ is assumed $\alpha=0$ so that the regression is through the
origin then the unbrased estimate is given by

$$
\begin{gathered}
\hat{\beta}=\frac{\sum_{i=1}^{n} x_{i} y_{i}}{\sum_{i=1}^{n} x_{i}^{2}} \\
E(\hat{\beta})=\beta \quad \operatorname{Uar}(\hat{\beta})=\frac{\sigma^{2}}{\sum_{i=1}^{n} x_{i}^{2}}
\end{gathered}
$$

Now ARCI) is defined by

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

If the associations are mode

$$
\begin{gathered}
\beta \rightarrow \beta \quad \alpha=0 \quad x_{t} \rightarrow y_{i} \quad x_{i} \rightarrow x_{t-1} \\
n \rightarrow T \quad x_{0}=0
\end{gathered}
$$

and using the result obtained for SLR through the origin

$$
\begin{gathered}
\hat{\phi}=\frac{\sum_{t=1}^{T} x_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
\Rightarrow \hat{\phi}-\phi=\frac{\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
E(\hat{\phi})=\phi \quad \operatorname{Uar}(\hat{\phi})=\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t-1}^{2}}
\end{gathered}
$$

Furthure if stationarity is assemed so that $|\varphi|<1$

$$
\begin{aligned}
& \operatorname{Var}\left(x_{t}\right)=\frac{1}{T} \sum_{t=1}^{T} x_{t-1}^{2}=\frac{\sigma^{2}}{1-\varphi^{2}} \\
& \Rightarrow \sum_{t=1}^{T} x_{t-1}^{2}=\frac{T \sigma^{2}}{1-\varphi^{2}}
\end{aligned}
$$

thus

$$
\begin{aligned}
\operatorname{var}(\hat{\varphi}) & =\frac{\sigma^{2}}{\sigma^{2}} \frac{\left(1-\phi^{2}\right)}{T} \\
& =\frac{1-\phi^{2}}{T}
\end{aligned}
$$

The asymptotic cariance is the variance of the central limit distribution, namely

$$
\sqrt{n}\left(\bar{x}_{n}-\mu\right) \xrightarrow{d} N\left(0, \sigma^{2}\right)
$$

where $\bar{x}_{n}$ is a sum of $n$ random variables

$$
\bar{x}_{n}=\frac{1}{n} \sum_{i=1}^{n} x_{i}
$$

with

$$
E\left(X_{i}\right)=\mu \quad \operatorname{var}\left(X_{i}\right)=\sigma^{2}
$$

Now consider expectation of of the numerator of $\hat{\varphi}-\varphi$

$$
\begin{aligned}
& E\left[\frac{1}{\left.\sqrt{T} \sum_{i=1}^{T} x_{i} \varepsilon_{i}\right]}=\frac{1}{\sqrt{T}} \sum_{i=1}^{T} x_{i} E\left(\varepsilon_{i}\right)\right. \\
& =0 \\
& \operatorname{Uar}\left[\frac{1}{\sqrt{T}} \sum_{i=1}^{T} x_{i} \varepsilon_{i}\right]=E\left[\left(\frac{1}{\sqrt{T}} \sum_{i=1}^{T} x_{i} \varepsilon_{i}\right)^{2}\right] \\
& =E\left[\frac{1}{T} \sum_{i=1}^{T} \sum_{j=1}^{T} x_{i} x_{j} \varepsilon_{i} \varepsilon_{j}\right] \\
& =\frac{1}{T} \sum_{i=1}^{T} \sum_{j=1}^{T} x_{i} x_{j} E\left(\varepsilon_{i} \varepsilon_{j}\right)
\end{aligned}
$$

It is assumed that

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=\sigma^{2} \delta_{i j}
$$

50

$$
\frac{1}{T} \sum_{i=1}^{T} \sum_{j=1}^{T} x_{i} x_{j} E\left(\varepsilon_{i} \varepsilon_{j}\right)
$$

$$
\begin{aligned}
& =\frac{1}{T} \sum_{i=1}^{T} \sum_{j=1}^{T} x_{i} x_{j} \sigma^{2} \delta_{i j} \\
& =\frac{\sigma^{2}}{T} \sum_{i=1}^{T} x_{i}^{2}
\end{aligned}
$$

If stationarity is asswemed

$$
\frac{1}{T} \sum_{i=1}^{T} x_{i}^{2}=\frac{\sigma^{2}}{1-\varphi^{2}}
$$

then

$$
\operatorname{Var}\left[\frac{1}{\sqrt{T}} \sum_{i=1}^{T} x_{i} \varepsilon_{i}\right]=\frac{\sigma^{4}}{1-\varphi^{2}}
$$

From the central limit theorem

$$
\sqrt{T}\left(\frac{1}{\sqrt{T}} \sum_{t=1}^{T} x_{t} \varepsilon_{t}\right) \xrightarrow{D} \operatorname{Normal}\left(0, \frac{\sigma^{4}}{1-\varphi^{2}}\right)
$$

Next the asymptotic distribution of $\hat{\phi}-\phi$ will be determined, recall

$$
\begin{aligned}
\pi(\hat{\phi}-\phi) & =\sqrt{T} \frac{\sum_{t=1}^{T} \varepsilon_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
& =\frac{\frac{1}{T} \sum_{t=1}^{T} x_{t-1} \varepsilon_{i}}{\frac{1}{T} \sum_{t=1}^{T} x_{t-1}^{2}}
\end{aligned}
$$

using the previous resut

$$
\sqrt{T}\left(\frac{1}{\sqrt{T}} \sum_{t=1}^{T} x_{t} \varepsilon_{t}\right) \xrightarrow{D} \operatorname{Normal}\left(0, \frac{\sigma^{4}}{1-\varphi^{2}}\right)
$$

gives

$$
\sqrt{T}(\hat{\phi}-\phi) \xrightarrow{D} \frac{1}{\frac{1}{T} \sum_{t=1}^{T} x_{t-1}^{2}} \operatorname{Normal}\left(0, \frac{\sigma^{4}}{1-\varphi^{2}}\right)
$$

but from stationarity

$$
\frac{1}{T} \sum_{t=1}^{T} x_{t-1}^{2}=\frac{\sigma^{2}}{1-\phi^{2}}
$$

It follows that

$$
\begin{aligned}
& \sqrt{\tau}(\hat{\varphi}-\varphi) \xrightarrow{D} \frac{1-\phi^{2}}{\sigma^{2}} \operatorname{Normal}\left(0, \frac{\sigma^{4}}{1-\phi^{2}}\right) \\
& =\operatorname{Normal}\left(0, \frac{\sigma^{4}}{1-\phi^{2}}\left(\frac{1-q^{2}}{\sigma^{4}}\right)^{2}\right) \\
& =\operatorname{Normal}\left(0,1-\varphi^{2}\right)
\end{aligned}
$$

Thus asymtoticaly $\sqrt{T}(\hat{\phi}-\phi)$ approaches a normal distribution with mean 0 and variance ( $-\varphi^{2}$ )

$$
\sqrt{T}(\hat{\varphi}-\varphi) \rightarrow \operatorname{Normal}\left(0,1-\varphi^{2}\right)
$$

and the asymtotic variance is given by

$$
\operatorname{avar}[\sqrt{\tau}(\hat{\varphi}-\varphi)]=1-\varphi^{2}
$$

It follows that asymtotically

$$
\operatorname{avar}[\sqrt{T}(\hat{\varphi}-\phi)] \sim O(1)
$$

Note that $|\varphi| \rightarrow 1$ implies that

$$
\operatorname{avar}[\sqrt{T}(\hat{\varphi}-\varphi)] \rightarrow 0
$$

It is clear that this result is invalid since $|\varphi|=1$ is not stationary, stationarity was used to obtain this result. It will be shown in the next section that for $q l=1$

$$
\operatorname{avar}[T(\hat{\varphi}-\varphi)] \sim O(1)
$$

## ARCD unit Root

Consider the trme series

$$
x_{0}, x_{1}, x_{2}, \ldots, x_{t-1}, x_{t}, x_{t+1}, \ldots, x_{T}
$$

Recall the las operator, 2 , which is defined by

$$
\begin{aligned}
L x_{t} & =x_{t-1} \\
L^{2} x_{t} & =x_{t-2} \\
\vdots & \\
L^{n} x_{t} & =x_{t-n}
\end{aligned}
$$

The AR(1) process can then be denoted by

$$
\begin{aligned}
& x_{t}=\varphi L x_{t}+\varepsilon_{t} \\
\Rightarrow & (1-\varphi L) x_{t}=\varepsilon_{t}
\end{aligned}
$$

Denote the lag polynomial by

$$
\Phi(L)=1-\varphi L
$$

then ARCD becomes

$$
\Phi(L) X_{t}=\varepsilon_{t}
$$

The characteristic equation is given by

$$
\Phi(z)=1-\phi z
$$

The root of the characteristic equation is given by

$$
\begin{aligned}
& \Phi(z)=0 \\
\Rightarrow & 1-\phi z=0 \\
\Rightarrow & z=\frac{1}{\varphi}
\end{aligned}
$$

The process is stationary if $|\varphi|<1$, thus the root of the cracateristic must satisfy

$$
z=\frac{1}{|\varphi|}>1
$$

Consider the case $\varphi=1$. For this case the characteristic equation is said to have a unit root.
with $\varphi=1$ the $A R C D$ process becomes

$$
x_{t}=x_{t-1}+\varepsilon_{t}
$$

Recall that the ols estimate is given by

$$
\hat{\varphi}-\phi=\frac{\sum_{t=1}^{T} \varepsilon_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

For the unit root case

$$
\hat{\varphi}-1=\frac{\sum_{t=1}^{T} \varepsilon_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

Without loss of generality assume that $x_{0}=0$

It follows that,

$$
\begin{aligned}
x_{1} & =\varepsilon_{1} \\
x_{2} & =x_{1}+\varepsilon_{2} \\
& =\varepsilon_{1}+\varepsilon_{2} \\
x_{3} & =x_{2}+\varepsilon_{3} \\
& =\varepsilon_{1}+\varepsilon_{2}+\varepsilon_{3}
\end{aligned}
$$

after $T$ terations it is seen

$$
x_{T}=\sum_{t=1}^{T} \varepsilon_{t}
$$

The conditional momements are given by, using the following assumptions

$$
\begin{aligned}
& E\left(\varepsilon_{t}\right)=0 \\
& E\left(\varepsilon_{t} \varepsilon_{s}\right)=\sigma^{2} \delta_{t s}
\end{aligned}
$$

then

$$
E\left(x_{t-1} \mid x_{0}=0\right)=E\left[\sum_{i=1}^{t-1} \varepsilon_{i}\right]
$$

$$
\begin{aligned}
& =\sum_{i=1}^{t-1} E\left(\varepsilon_{i}\right) \\
& =0
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left(x_{t-1}^{2} \mid x_{0}=0\right)=E\left[\left(\sum_{i=1}^{t-1} \varepsilon_{i}\right)^{2}\right] \\
& =E\left[\sum_{i=1}^{t-1} \sum_{j=1}^{t-1} \varepsilon_{i} \varepsilon_{j}\right] \\
& =\sum_{i=1}^{t-1} \sum_{j=1}^{t-1} E\left(\varepsilon_{i} \varepsilon_{j}\right) \\
& =\sum_{i=1}^{t-1} \sum_{j=1}^{t-1} \sigma^{2} \delta_{i j} \\
& =\sum_{i=1}^{t-1} \sigma^{2} \\
& =(t-1) \sigma^{2}
\end{aligned}
$$

and
$E\left[\sum_{t=1}^{T} x_{t-1}^{2} \mid x_{0}=0\right]=\sum_{t=1}^{T} E\left(x_{t-1}^{2} \mid x_{0}=0\right)$

$$
\begin{aligned}
& =\sum_{t=1}^{T}(t-1) \sigma^{2} \\
& =\sigma^{2} \sum_{t=1}^{T}(t-1) \\
& \approx \sigma^{2} \int_{1}^{T}(t-1) d t \\
& =\left.\sigma^{2}\left(\frac{1}{2} t^{2}-t\right)\right|_{1} ^{T} \\
& =\sigma^{2}\left[\left(\frac{1}{2} T^{2}-T\right)-\left(\frac{1}{2}-1\right)\right] \\
& =\sigma^{2}\left(\frac{1}{2} T^{2}-T+\frac{1}{2}\right)
\end{aligned}
$$

To leading order
$E\left[\sum_{t=1}^{T} x_{t-1}^{2} \mid x_{0}=0\right] \& \sigma^{2} T^{2}=O\left(T^{2}\right)$
Next consider

$$
\begin{aligned}
& E\left(x_{t-1} \varepsilon_{t} \mid x_{0}=0\right)=E\left[\sum_{i=1}^{t-1} \varepsilon_{i} \varepsilon_{t} \mid x_{0}=0\right] \\
& =\sum_{i=1}^{t-1} E\left(\varepsilon_{i} \varepsilon_{t} \mid x_{0}=0\right)
\end{aligned}
$$

$$
=0
$$

since $E\left(\varepsilon_{i} \varepsilon_{j}\right)=0$ for $i \neq j$ and $i<t$ for all terms in the sum.
It follows that

$$
\begin{aligned}
& E\left[\sum_{t=1}^{T} x_{t-1} \varepsilon_{t} \mid x_{0}=0\right] \\
& \quad=\sum_{t=1}^{T} E\left(x_{t-1} \varepsilon_{t} \mid x_{0}=0\right) \\
& \quad=0
\end{aligned}
$$

and finally consider

$$
\begin{aligned}
& E\left(x_{t-1}^{2} \varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =E\left[\left(\sum_{i=1}^{t-1} \varepsilon_{i}\right)^{2} \varepsilon_{t}^{2} \mid x_{0}=0\right] \\
& =E\left[\sum_{i=1}^{t-1} \sum_{j=1}^{t-1} \varepsilon_{i} \varepsilon_{j} \varepsilon_{t}^{2} \mid x_{0}=0\right]
\end{aligned}
$$

$$
=\sum_{i=1}^{t-1} \sum_{j=1}^{t-1} E\left(\varepsilon_{i} \varepsilon_{j} \varepsilon_{t}^{2} \mid x_{0}=0\right)
$$

Now since the $\varepsilon_{i}$ are independent and $i, j<t$ for $i \neq j$

$$
\begin{aligned}
& E\left(\varepsilon_{i} \varepsilon_{j} \varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =E\left(\varepsilon_{i} \mid x_{0}=0\right) E\left(\varepsilon_{j} \mid x_{0}=0\right) E\left(\varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =0
\end{aligned}
$$

for $i=j<t$

$$
\begin{aligned}
E( & \left.\varepsilon_{l}^{2} \varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =E\left(\varepsilon_{l}^{2} \mid x_{0}=0\right) E\left(\varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =\sigma^{2} \sigma^{2} \\
& =\sigma^{4}
\end{aligned}
$$

Thus

$$
E\left(\varepsilon_{i} \varepsilon_{j} \varepsilon_{t}^{2} \mid x_{0}=0\right)=\sigma^{4} \delta_{i j}
$$

So putting things together gives

$$
\begin{aligned}
& E\left(x_{t-1}^{2} \varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =\sum_{j=1}^{t-1} \sum_{i=1}^{t-1} E\left(\varepsilon_{i} \varepsilon_{j} \varepsilon_{t}^{2} \mid x_{0}=0\right) \\
& =\sum_{j=1}^{t-1} \sum_{i=1}^{t-1} \sigma^{4} \delta_{i j} \\
& =\sum_{j=1}^{t-1} \sigma^{4} \\
& =\sigma^{4}(t-1)
\end{aligned}
$$

Next consder the case $t>s$

$$
\begin{aligned}
& E\left(X_{t-1} \varepsilon_{t} X_{s-1} \varepsilon_{s} \mid X_{0}=0\right) \\
& =E\left[\sum_{i=1}^{t-1} \sum_{j=1}^{s-1} \varepsilon_{i} \varepsilon_{j} \varepsilon_{t} \varepsilon_{s} \mid X_{0}=0\right] \\
& =\sum_{i=1}^{t-1} \sum_{j=1}^{s-1} E\left(\varepsilon_{i} \varepsilon_{j} \varepsilon_{t} \varepsilon_{s} \mid X_{0}=0\right)
\end{aligned}
$$

since $t>s$

$$
\begin{aligned}
& E\left(\varepsilon_{j} \varepsilon_{i} \varepsilon_{t} \varepsilon_{s} \mid x_{0}=0\right) \\
& \quad=E\left(\varepsilon_{j} \varepsilon_{i} \varepsilon_{s} \mid x_{0}=0\right) E\left(\varepsilon_{t} \mid x_{0}=0\right) \\
& \quad=0
\end{aligned}
$$

a similar result follows for $s>t$. Putting things together

$$
\begin{array}{r}
E\left(x_{t-1} \varepsilon_{t} x_{s-1} \varepsilon_{s} \mid x_{0}=0\right) \\
=\sigma^{4}(t-1) \delta_{t s}
\end{array}
$$

Finally

$$
\begin{aligned}
& E\left[\left(\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}\right)^{2} \mid x_{0}=0\right] \\
& =E\left[\sum_{t=1}^{T} \sum_{s=1}^{T} x_{t-1} \varepsilon_{t} x_{s-1} \varepsilon_{s} \mid x_{0}=0\right] \\
& =\sum_{t=1}^{T} \sum_{s=1}^{T} E\left(x_{t-1} \varepsilon_{t} x_{s-1} \varepsilon_{s} \mid x_{0}=0\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{t=1}^{T} \sum_{s=1}^{T} \sigma^{4}(t-1) \delta_{t s} \\
& =\sum_{t=1}^{T} \sigma^{4}(t-1) \\
& \approx \sigma^{4} \int_{1}^{T}(t-1) d t \\
& \alpha \sigma^{4} T^{2} \\
& =O\left(T^{2}\right)
\end{aligned}
$$

Now an estimate of the asymtotic variance can be obtained following the proceedere previously used, recall that for $\varphi=1$ the estimate $\phi$ is given by

$$
\hat{\varphi}-1=\frac{\sum_{t=1}^{T} \varepsilon_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

gues

$$
\operatorname{avar}(\hat{\varphi}-1)=\frac{\operatorname{var}\left(\sum_{t=1}^{T} \varepsilon_{t} X_{t-1}\right)}{\left[\operatorname{var}\left(\sum_{t=1}^{T} X_{t-1}\right)\right]^{2}}
$$

using the previous result

$$
\begin{aligned}
& \operatorname{var}\left(\sum_{t=1}^{T} \varepsilon_{t} X_{t-1}\right) \propto \sigma^{4} T^{2} \\
& \operatorname{var}\left(\sum_{t=1}^{T} X_{t-1}\right) \propto \sigma^{2} T^{2}
\end{aligned}
$$

gives

$$
\begin{aligned}
& \operatorname{avar}(\hat{\varphi}-1) \propto \frac{O^{4} T^{2}}{O^{4} T^{4}}=T^{-2} \\
\Rightarrow & \operatorname{avar}[T(\hat{\varphi}-1)] \sim O(1)
\end{aligned}
$$

for the case $|\varphi|<1$ it was found that

$$
\operatorname{avar}[\sqrt{T}(\hat{\varphi}-\varphi)] \sim O(1)
$$

This explains the invalid result by taking the limit $\varphi^{-31}$ for the previous result.

## Integration order

In the literature there is mention of integration order. A time series is said to be of integration order 0 if $t$ supports an a inifinite moving asserage model that satisfies

$$
\sum_{i=0}^{\infty}\left|b_{i}\right|^{2}<\infty
$$

where $b_{k}$ are the coefficients of the moving average model. It was prevously shown that AR(1), given by,

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

is equivalent to $a ~ M A(\infty) ~ m o d e l ~$ with coefficients

$$
b_{i}=\phi^{i}
$$

If the series is stationary then $|\phi|<1$ and the condition for
integration order 0 is satisfled. Thus ARCD for $l \varphi<1$ has integration order 0 , denoted by I(0)

In general a time series is sad to have integration order $q$ if

$$
(1-L)^{9} x_{t}
$$

is a stationary process.
For unit root AR(1),

$$
\begin{aligned}
& x_{t}=x_{t-1}+\varepsilon_{t} \\
\Rightarrow & x_{t}-x_{t-1}=\varepsilon_{t}
\end{aligned}
$$

for a single slep is stationary since $\varepsilon_{t}$ has constant mean and variance. Thus the unit root case has integration order 1, denoted by ICM.

## Unit Root form of AR(1)

An alternative representation of AR(1) used when estimating $\varphi$ is given by

$$
\begin{gathered}
x_{t}=\varphi x_{t-1}+\varepsilon_{t} \\
\Rightarrow \quad x_{t}-x_{t-1}=(\varphi-1) x_{t-1}+\varepsilon_{t}
\end{gathered}
$$

define the difference operator

$$
\Delta=(1-L)
$$

where $L$ is the lag operator, then

$$
\Delta x_{t}=(\varphi-1) x_{t-1}+\varepsilon_{t}
$$

let

$$
\delta=\varphi-1
$$

then

$$
\Delta x_{t}=\delta x_{t-1}+\varepsilon_{t}
$$

Stationarity implies that
while nonstationority, unit root, implies $\delta=0$.

Recall that

$$
\hat{\phi}=\frac{\sum_{t=1}^{T} x_{t} x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

Now

$$
\begin{aligned}
\Delta x_{t} & =x_{t}-x_{t-1} \\
\Rightarrow x_{t} & =\Delta x_{t}+x_{t-1}
\end{aligned}
$$

so

$$
\hat{\varphi}=\frac{\sum_{t=1}^{T}\left(x_{t-1}+\Delta x_{t}\right) x_{t-1}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

$$
\begin{aligned}
& =1+\frac{\sum_{t=1}^{T} \Delta x_{t} x_{t-1}}{\frac{T}{\sum_{t=1}^{T} x_{t-1}^{2}}} \\
\Rightarrow \hat{\varphi}-1 & =\frac{\sum_{t=1}^{T} \Delta x_{t} x_{t-1}}{\frac{T}{\sum_{t=1} x_{t-1}^{2}}} \\
\Rightarrow \hat{\delta} & =\frac{\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} x_{t-1}^{2}}
\end{aligned}
$$

Now

$$
\begin{aligned}
E(\hat{\delta}) & =\frac{\sum_{t=1}^{T} x_{t-1} E\left(\varepsilon_{t}\right)}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
& =0
\end{aligned}
$$

and

$$
\begin{aligned}
& \operatorname{Uar}(\hat{\delta})=E\left(\hat{\delta}^{2}\right) \\
& \left.=E\left[\frac{\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} x_{t-1}^{2}}\right)^{2}\right] \\
& =E\left[\frac{\sum_{t=1}^{T} \sum_{j=1}^{T} x_{t-1} x_{j-1} \varepsilon_{t} \varepsilon_{j}}{\left(\sum_{t=1}^{T} x_{t-1}^{2}\right)^{2}}\right] \\
& =\frac{1}{\left(\sum_{t=1}^{T} x_{t-1}^{2}\right)^{2} \sum_{t=1}^{T} \sum_{j=1}^{T} x_{t-1} x_{j-1} E\left(\varepsilon_{t} \varepsilon_{j}\right)} \\
& =\frac{1}{\left(\sum_{t=1}^{T} x_{t-1}^{2}\right)^{2} \sum_{t=1}^{T} \sum_{j=1}^{T} x_{t-1} x_{j-1} \sigma^{2} \delta_{t j}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\left(\sum_{t=1}^{T} x_{t-1}^{2}\right)^{2}} \sigma^{2}\left(\sum_{t=1}^{T} x_{t-1}^{2}\right) \\
& =\frac{\sigma^{2}}{\left(\sum_{t=1}^{T} x_{t-1}^{2}\right)}
\end{aligned}
$$

Thus it has been shown that for AR(1) in unit root form the estimate of the whit root parameter, $\hat{\delta}$ is given by,

$$
\begin{gathered}
\Delta x_{t}=\delta x_{t-1}+\varepsilon_{t} \\
\hat{\delta}=\frac{\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
E(\hat{\delta})=0 \quad \operatorname{var}(\hat{\delta})=\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t-1}^{2}}
\end{gathered}
$$

## unit Root form of $A R(q)$

Recall that the AR(1) model is given by

$$
\begin{aligned}
& x_{t}=\varphi x_{t-1}+\varepsilon_{t} \\
\Rightarrow & x_{t}-\varphi x_{t-1}=\varepsilon_{t}
\end{aligned}
$$

and the las operator by

$$
\begin{aligned}
L x_{t} & =x_{t-1} \\
L^{2} x_{t} & =x_{t-2} \\
\vdots & \\
L^{n} x_{t} & =x_{t-n}
\end{aligned}
$$

using the lag operator AR(1) can be written as

$$
(1-\varphi L) x_{t}=\varepsilon_{t}
$$

The ARCD Lag polynomial is defined by

$$
\Phi^{\prime}(L)=1-\phi L
$$

so that $A R(1)$ can by written as

$$
\Phi^{\prime}(L) X_{t}=\varepsilon_{t}
$$

The unit root is defined by

$$
\begin{aligned}
& \Phi^{\prime}(1)=0 \\
\Rightarrow \quad 1-\phi & =0
\end{aligned}
$$

let

$$
\delta=\varphi-1
$$

and define the difference operator by

$$
\Delta x_{t}=x_{t}-x_{t-1}
$$

then $A R(1)$ can by written as

$$
\begin{aligned}
& x_{t}=\varphi x_{t-1}+\varepsilon_{t} \\
\Rightarrow & x_{t}-x_{t-1}=(\varphi-1) x_{t}+\varepsilon_{t} \\
\Rightarrow & \Delta x_{t}=\delta x_{t}+\varepsilon_{t}
\end{aligned}
$$

In summary the unit root problem for ARCI) is defined by

$$
\begin{gathered}
\Phi^{\prime}(L) x_{t}=\varepsilon_{t} \\
\Phi^{\prime}(1)=0=1-\phi \\
\delta=\phi-1=0 \\
\Delta x_{t}=\delta x_{t}+\varepsilon_{t}
\end{gathered}
$$

Next consider $A R(2)$. The lag polynomial is given by

$$
\Phi^{2}(L)=1-\varphi_{1} L-\varphi_{2} L^{2}
$$

so $A R(2)$ is given by

$$
\begin{aligned}
& \Phi^{2}(L) X_{t}=\varepsilon_{t} \\
\Rightarrow \quad & X_{t}=\varphi_{1} X_{t-1}+\varphi_{2} X_{t-2}+\varepsilon_{t}
\end{aligned}
$$

The unit root is given by

$$
\Phi^{2}(1)=0
$$

$$
\Rightarrow 1-\varphi_{1}-\varphi_{2}=0
$$

let

$$
\delta=\varphi_{1}+\varphi_{2}-1
$$

subtrating $x_{t-1}$ from both sides of AR(2) gives

$$
\begin{aligned}
& x_{t}-x_{t-1}=\left(\varphi_{1}-1\right) x_{t-1}+\varphi_{2} x_{t-2}+\varepsilon_{t} \\
\Rightarrow & \Delta x_{t}=\left(\varphi_{1}-1\right) x_{t-1}+\varphi_{2} x_{t-2}+\varepsilon_{t}
\end{aligned}
$$

adding and subtracting $q_{2} x_{t-1}$ gives

$$
\begin{aligned}
\Delta x_{t}= & \left(\varphi_{1}-1\right) x_{t-1}+\varphi_{2} x_{t-2}+\varepsilon_{t} \\
& +\varphi_{2} x_{t-1}-\varphi_{2} x_{t-1} \\
= & \left(\varphi_{2}+\varphi_{1}-1\right) x_{t-1}+\varphi_{2}\left(x_{t-2}-x_{t-1}\right)+\varepsilon_{t} \\
= & \delta x_{t-1}-\varphi_{2} \Delta x_{t-1}+\varepsilon_{t}
\end{aligned}
$$

Thus the unit root problem for $A R(2)$ is defined by

$$
\begin{gathered}
\Phi^{2}(L) x_{t}=\varepsilon_{t} \\
\Phi^{2}(1)=1-\Phi_{1}-\Phi_{2}=0 \\
\delta=\Phi_{1}+\Phi_{2}-1=0 \\
\Delta x_{t}=\delta x_{t-1}-\varphi_{2} \Delta x_{t-1}+\varepsilon_{t}
\end{gathered}
$$

To see the pattern consider one more example, $A R(3)$. The lag polynomial is given by

$$
\Phi^{3}(L)=1-\Phi_{1} L-\Phi_{2} L^{2}-\Phi_{3} L^{3}
$$

50

$$
\begin{gathered}
\Phi^{3}(L) x_{t}=\varepsilon_{t} \\
\Rightarrow \quad x_{t}=\Phi_{1} x_{t-1}+\Phi_{2} x_{t-2}+\varphi_{3} x_{t-3}+\varepsilon_{t}
\end{gathered}
$$

The unct root is given by

$$
\Phi^{3}(1)=1-\varphi_{1}-\varphi_{2}-\varphi_{3}=0
$$

let

$$
\delta=\varphi_{1}+\varphi_{2}+\varphi_{3}-1
$$

following the same proceedure used for ARC3). Subtract $x_{t-1}$ from both sides

$$
\begin{aligned}
& x_{t}-x_{t-1}=\left(\phi_{1}-1\right) x_{t-1}+\phi_{2} x_{t-2}+\phi_{3} x_{t-3} \\
&+\varepsilon_{t} \\
& \Rightarrow \Delta x_{t}=\left(\phi_{1}-1\right) x_{t-1}+\phi_{2} x_{t-2}+\phi_{3} x_{t-3}+\varepsilon_{t} \\
& \text { Adding and subtracting }\left(\phi_{2}+\phi_{3}\right) x_{t-1} \\
& \text { gives } \\
& \Delta x_{t}=\left(\phi_{3}+\phi_{2}+\phi_{1}-1\right) x_{t-1}+\phi_{2}\left(x_{t-2}-x_{t-1}\right) \\
&-\phi_{3} x_{t-1}+\phi_{3} x_{t-3}+\varepsilon_{t} \\
&= \delta x_{t-1}-\phi_{2} \Delta x_{t-1}-\phi_{3} x_{t-1}+\phi_{3} x_{t-3} \\
&+\varepsilon_{t}
\end{aligned}
$$

Finally ading and subtracting $\varphi_{3} x_{t-2}$ gives

$$
\begin{aligned}
\Delta x_{t}= & \delta x_{t-1}-\varphi_{2} \Delta x_{t-1}-\varphi_{3} x_{t-1}+\varphi_{3} x_{t-3} \\
& -\varphi_{3} x_{t-2}+\varphi_{3} x_{t-3}+\varepsilon_{t}
\end{aligned}
$$

$$
\begin{aligned}
= & \delta x_{t-1}-\Phi_{2} \Delta x_{t-1}-\Phi_{3}\left(x_{t-1}+x_{t-2}\right) \\
& -\Phi_{3}\left(x_{t-2}-x_{t-3}\right)+\varepsilon_{t} \\
= & \delta x_{t-1}-\left(\Phi_{3}+\Phi_{2}\right) \Delta x_{t-1}-\Phi_{3} \Delta x_{t-2} \\
& +\varepsilon_{t}
\end{aligned}
$$

Thus the unit root problem for $A R(3)$ is given by

$$
\begin{gathered}
\Phi^{3}(L) x_{t}=\varepsilon_{t} \\
\Phi^{3}(1)=1-\Phi_{1}-\Phi_{2}-\Phi_{3}=0 \\
\delta=\Phi_{1}+\Phi_{2}+\Phi_{3}-1=0 \\
c_{1}=-\left(\Phi_{3}+\Phi_{2}\right) \\
c_{2}=-\Phi_{3} \\
\Delta x_{t}=\delta x_{t-1}+c_{1} \Delta x_{t-1}+c_{2} \Delta x_{t-2}+\varepsilon_{t}
\end{gathered}
$$

For $A R(q)$ the unit root problem is defined by

$$
\begin{gathered}
\Phi^{q}(L)=1-\varphi_{1} L-\varphi_{2} L^{2} \cdots-q_{q} L^{q} \\
\Phi^{q}(1)=1-q_{1}-\varphi_{2}-\cdots-\varphi_{q}=0 \\
\delta=\varphi_{1}+\varphi_{2}+\varphi_{3}+\cdots+\varphi_{q}-1 \\
c_{i}=-\sum_{j=i+1}^{q} \varphi_{j} \\
\Delta x_{t}=\delta x_{t-1}+c_{1} \Delta x_{t-1}+c_{2} \Delta x_{t-2}+\cdots+ \\
c_{q-1} \Delta x_{t-(q-1)}+\varepsilon_{t}
\end{gathered}
$$

## Dickey-Fuller Test Statistic

Consider AR(1)

$$
\Delta x_{t}=\delta x_{t-1}+\varepsilon_{t}
$$

The desire is to design a test given $T$ samples,

$$
x_{1}, x_{2}, \ldots, x_{T}
$$

to determine if the sequence of samples is stationary Given the sample data the estimate, $\hat{\delta}$, is given by

$$
\begin{gathered}
\Delta x_{t}=\delta x_{t-1}+\varepsilon_{t} \\
\hat{\delta}=\frac{\sum_{t=1}^{T} x_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
E(\hat{\delta})=0 \quad \operatorname{var}(\hat{\delta})=\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t-1}^{2}}
\end{gathered}
$$

where

$$
\sigma^{2}=E\left(\varepsilon_{i}^{2}\right)
$$

The hypothels tested is "Is $\hat{\delta}$ a unit root?", namely

$$
\hat{\delta}=0
$$

if $\delta=0$ then the data set is not stationary.
The atternate mypothesis is "Is $\hat{\delta}<O^{\nu}$. If this is the case then the sample data is stationary

The proposed test statistic is given by

$$
t=\frac{\hat{\delta}}{S E(\hat{\delta})}
$$

where $S E(\hat{\delta})$ is the standard error, namely,

$$
\operatorname{se}(\hat{\delta})=\sqrt{\operatorname{Uar}(\hat{\delta})}
$$

To evaluate the validity of the hypotheis a Pualue is needed thus the distribution of the test statistic is required.
For the stationary case, using

$$
\begin{gathered}
\sum_{t=1}^{T} x_{t-1}^{2}=\frac{T \sigma^{2}}{1-\varphi^{2}} \\
E(\hat{\delta})=0 \\
\operatorname{var}(\hat{\delta})=\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t 1}^{2}}=\frac{1-\varphi^{2}}{T}
\end{gathered}
$$

Thus asymptotically

$$
\sqrt{T} \hat{\delta} \xrightarrow{D} \operatorname{Normal}\left(0,1-\varphi^{2}\right)
$$

It follows that the asymptatic
distribution of the t-statistic is given by

$$
\begin{aligned}
& \operatorname{SE}(\hat{\delta}) t=\hat{\delta} \xrightarrow{\frac{1}{\sqrt{T}} \operatorname{Normal}\left(0,1-\varphi^{2}\right)} \\
\Rightarrow & \sqrt{T} t \xrightarrow{\frac{\sqrt{T}}{1-\varphi^{2}}} \operatorname{Normal}\left(0,1-\varphi^{2}\right) \\
\Rightarrow t & \xrightarrow{D} \operatorname{Normal}(0,1)
\end{aligned}
$$

Thus for the stationory case the $t$-statistic asymptotically approaches an unit jormal distributions.

For the nonstationary case the asymtotic distribution station anty assumptions cannot be made. It was previously shown that in the unit root case the asymptotic variance is of order $T^{-2}$ not $T^{-1}$ as wall be the case if it were normal.
since $x_{t-1}$ will be a sum of the $\varepsilon_{i}$ the numearator and denominator are correlated since the are computed from the same random samples. It follows that the assumption that they are independent used to derive the $t$-distribution cannot be used. To evaluate the Imiting distribution results from stochastic calculus are required.
The following section will review stochastic calculus and the retwon to this problem

## Reveew of Stochastic Calculus

To go furthur the Itô integral must be reviewed. In the theory Its integration functions are approximated as sums of simple functions. Consider a function, $f\left(t, B_{t}\right)$, where $B_{t}$ is Brownian motion, $B_{t} \sim$ Normal $(0, t)$, and the partion of the interval $0 \leqslant t \leqslant t_{n}$ into subintervals

$$
0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{n}
$$

Define the indicator function

$$
\underline{11}_{\left[t_{i-1}, t_{i}\right]}= \begin{cases}1 & t_{i-1} \leqslant t \leqslant t_{i} \\ 0 & t<t_{i-1} \text { and } t>t_{i}\end{cases}
$$

Then the simple function expansion of $f\left(t, B_{t}\right)$ is given by

$$
f\left(t, B_{t}\right)=\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e\left(B_{t_{i}}\right) \mathbb{1}_{\left[t_{i-1}, t_{i}\right]}
$$

where $e\left(B t_{i}\right)$ is a constant value of $f\left(t, B_{t}\right)$ over the interval $t_{i-1} \leqslant t \leqslant t_{i}$. The Itô integral assumes $e\left(B_{i}\right)$ is the value at the leftmost point of the interval

$$
e\left(B_{i}\right)=f\left(t_{i-1}, B_{t i-1}\right)
$$

The Itô integral is defined by
$\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}$
$=\int_{0}^{t}\left\{\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(t_{i-1}, B_{t_{i-1}}\right) \underline{I}_{\left[t_{i-1}, t_{i}\right]}\right\} d B_{S}$
$=\lim _{n \rightarrow \infty} \sum_{i=1}^{n}\left\{\int_{t_{i-1}}^{t_{i}} f\left(t_{i-1}, B_{t_{i-1}}\right) d B_{S}\right\}$

$$
\begin{aligned}
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(t_{i-1}, B_{t_{i-1}}\right) \int_{t_{i-1}}^{t_{i}} d B_{s} \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(t_{i-1}, B_{t_{i-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(t_{i-1}, B_{t_{i-1}}\right) \Delta B t_{i}
\end{aligned}
$$

Thus the Itô integral is defined by

$$
\begin{aligned}
\int_{0}^{t} f(s & \left., B_{s}\right) d B_{s} \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f\left(t_{i-1}, B_{t-1}\right) \Delta B t_{i}
\end{aligned}
$$

In the analysis of the Pickey-fuller test statistic the integral is required to be over the interval $0 \leqslant s \leqslant 1$. This is accomplished by using the portition

$$
0 \leqslant \frac{1}{T} \leqslant \frac{2}{T} \leqslant \cdots \leqslant 1
$$

where $T=t_{n}$.
Then

$$
\begin{aligned}
\int_{0}^{1} f(s & \left., B_{s}\right) d B_{s} \\
& =\lim _{T \rightarrow \infty} \sum_{s=1}^{T} f\left(\frac{s}{T}, B_{\frac{s-1}{T}}\right) \Delta B_{\frac{s}{T}}
\end{aligned}
$$

Now $B_{t}$ is Brownian motion 80

$$
B_{T} \sim \text { Normal }(0, T)
$$

it follows that

$$
\begin{aligned}
& B \frac{S}{T} \sim \operatorname{Normal}\left(0, \frac{S}{T}\right) \\
\Rightarrow & \sqrt{T} B \frac{S}{T} \sim \operatorname{Normal}(0, S)
\end{aligned}
$$

It follows that

$$
B \frac{S}{T}=\frac{1}{\pi} B_{S}
$$

and

$$
\begin{aligned}
\Delta B_{\frac{S}{T}} & =B_{\frac{S}{T}}-B_{S-1}=\frac{1}{\sqrt{T}}\left(B_{S}-B_{S-1}\right) \\
& =\frac{1}{\sqrt{T}} \Delta B_{S}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\int_{0}^{1} f(s & \left., B_{s}\right) d B_{s} \\
& =\lim _{T \rightarrow \infty} \sum_{s=1}^{T} f\left(\frac{s}{T}, \frac{B_{s-1}}{T}\right) \frac{\Delta B_{s}}{T T}
\end{aligned}
$$

To go furthur the form of $f(t, B t)$ is required.

Another result that will be usefull is the Itô formula. consider a twice differentiable function, $f\left(x_{t}, t\right)$ where

$$
x_{t}=\mu t+\sigma d B_{t}
$$

It can be shown that

$$
\begin{aligned}
d f= & {\left[\frac{\partial f}{\partial t}+\mu \frac{\partial f}{\partial x_{t}}+\frac{\sigma^{2}}{2} \frac{\partial^{2} f}{\partial x_{t}^{2}}\right] d t } \\
& +\sigma \frac{\partial f}{\partial x_{t}} d B_{t}
\end{aligned}
$$

## Donsker's Functional Central Limit Theorem (FCLT)

Recall the Central Limit theorem for a sum of $n$ independent and identically distributed random voriables,

$$
\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}
$$

where

$$
S_{n}=\sum_{i=1}^{n} x_{i}
$$

and

$$
E\left(X_{i}\right)=\mu \quad \operatorname{var}\left(X_{i}\right)=\sigma
$$

The average of $n$ realizations of $x_{i}$ is given by

$$
\begin{aligned}
\bar{x}_{n} & =\frac{1}{n} \sum_{i=1}^{n} x_{i} \\
& =\frac{s_{n}}{n}
\end{aligned}
$$

The Central Limit Theorem states that in the limit $n \rightarrow \infty$

$$
\frac{\sqrt{n}\left(\bar{x}_{n}-\mu\right)}{\sigma} \xrightarrow{D} \operatorname{Normal}(0,1)
$$

that is as $n$ increases the distribution of the random variable

$$
\frac{\sqrt{n}\left(\bar{x}_{n}-\mu\right)}{\sigma}
$$

approaches a unit normal distribution which is denoted $\underset{\rightarrow}{D}$
In terms of the sum $s_{n}$

$$
\begin{aligned}
& \sqrt{n}\left(\frac{S_{n} / n-\mu}{\sigma}\right) \xrightarrow{D} \operatorname{Normal}(0,1) \\
\Rightarrow & \frac{\left(S_{n}-n \mu\right)}{\sqrt{n} \sigma} \xrightarrow{D} \operatorname{Normal}(0,1)
\end{aligned}
$$

In the litcature $\xrightarrow{D}$ may be denoted by $\Rightarrow$ and called weak convergence.
The central limit theorem can be used to deduce confidence intervals. For the unit normal distribution

$$
P(-2 \leqslant y \leqslant 2) \approx 0,95
$$

Letting

$$
y=\frac{\sqrt{n}\left(\bar{x}_{n}-\mu\right)}{\sigma}
$$

gives
$P\left(-2 \leqslant \sqrt{n}\left(\frac{\bar{x}_{n}-\mu}{6}\right) \leqslant 2\right)$
$=P\left(-2 \sigma / \sqrt{n} \leqslant \bar{x}_{n}-\mu \leqslant 2 \sigma / \sqrt{n}\right)$
$=P\left(\mu-2 \sigma / \sqrt{n} \leqslant \bar{x}_{n} \leqslant \mu+2 \sigma / \sqrt{n}\right) \approx 0.95$
Next consider the sequence of sums

$$
\left\{s_{1}, s_{2}, s_{3}, \ldots, s_{n}\right\}
$$

The Donsker CLT is that this sequence, in the limit $n \rightarrow \infty$, converges to a weiner Process. Recall that a weiner Process is the continuous version of a baussian random walk.

To go furthur a continuous time version of $\mathrm{Sn}^{n}$ is required. Let

$$
S_{n}(t)=\frac{1}{\sqrt{n}}\left(s_{\text {Lnt } 1}-\mu n t\right)
$$

where

$$
S_{(n t)}=\sum_{i=1}^{\operatorname{Ln} t 1} X_{i}
$$

To understand what this means assume than $0 \leqslant t \leqslant 1$ and $n=10$ and recall that Lnt 1 is the floor of the product of $n t$, the floor of a real number is the largest integer less than
the real number. It follows that the values of Lnt」 for this choice of $n$ and $t$ are the integers

$$
0,1,2,3,4,5,6,7,8,9,10
$$

As a function of $t$ a possible realization of $\delta_{n}(t)$ is shown below
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-436.jpg?height=582&width=1088&top_left_y=876&top_left_x=151)

Thus the result of having the sum limit LntJ is to provide linear interpolation between points in the discrete sum.

The Donster FCLT can now be
stated as follows. Consider a sequence of independent identically distributed random variables

$$
\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

with finite mean and variance

$$
\mu=E\left(x_{i}\right) \quad \sigma^{2}=\operatorname{var}\left(x_{i}\right)
$$

Let $s_{n}$ denote the sum

$$
s_{n}=\sum_{i=1}^{n} x_{i}
$$

with

$$
E\left(S_{n}\right)=\mu n \quad \operatorname{Var}\left(S_{n}\right)=n \sigma^{2}
$$

Then the CLT gives

$$
\frac{\left(S_{n}-n \mu\right)}{\sqrt{n} \sigma} \xrightarrow{D} \operatorname{Normal}(0,1)
$$

Define the continuous function of time

$$
S_{n}(t)=\frac{1}{\sqrt{n}}\left(S_{[n t]}-\mu_{n} t\right)
$$

where $t>0$. The Donsker FCLT states that in the limit $n \rightarrow \infty$

$$
\frac{\phi_{n}(t)}{\sigma} \xrightarrow{D} \omega(t)
$$

where $\omega(t)$ is a standard weiner process which has the properties

$$
\omega(0)=0
$$

$\omega(t) \sim$ Normal $(0, t)$
and for $s>0$

$$
\omega(t+s)-\omega(t) \sim \operatorname{Normal}(0, s)
$$

and $\omega(t+s)-\omega(t)$ is independent of $\omega(t)$

The following plots illustrate the Dosker CLT. Each plot shows examples where $n$ is increased from 50 to 1000 and assumes different values for $\mu$ an $\sigma$.

In the calculations an $n$ is increased more samples are added to the tail of the provos simulation and rescaled. This is noticable if the simulations are compared.

Donsker CLT $\mu=0.0, \sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-439.jpg?height=686&width=1090&top_left_y=1134&top_left_x=243)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-440.jpg?height=730&width=1091&top_left_y=185&top_left_x=278)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-440.jpg?height=716&width=1067&top_left_y=1082&top_left_x=276)

Donsker's CLT can be extended by use of the continous maping theorem which states that if

$$
x_{n} \xrightarrow{D} x
$$

as $n \rightarrow \infty$ then for a function $g(x)$

$$
g\left(x_{n}\right) \xrightarrow{D} g(x)
$$

It follows that

$$
g\left(\frac{1}{6} A_{n}(t)\right) \xrightarrow{D} g(\omega(t))
$$

## Continuous Mapping Theorem

The continuous maping theorem is used to cualuate asymptotic distributions.
It can be stated as follows. Given a sequence of random variables

$$
\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

for the limit $n \rightarrow \infty$ if

$$
x_{n} \xrightarrow{D} x
$$

then for a function $g\left(x_{n}\right)$ for $n \rightarrow \infty$

$$
g\left(x_{n}\right) \xrightarrow{D} g(x)
$$

## Distribution of Dickey. Fuller Test statistic

Previolesly it was shown that the estimate of the Dickey-Fuller parameter is given by

$$
\hat{\delta}=\frac{\sum_{t=1}^{T} X_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} X_{t-1}^{2}}
$$

Next consider

$$
\begin{aligned}
T \hat{\delta} & =T \frac{\sum_{t=1}^{T} X_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} X_{t-1}^{2}} \\
& =\frac{\sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{\sigma^{2} T}}\right)\left(\frac{\varepsilon_{t}}{\sqrt{\sigma^{2} T}}\right)}{\frac{1}{T} \sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{\sigma^{2} T}}\right)^{2}}
\end{aligned}
$$

Now recall that

$$
\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

and here assume that

$$
\Delta T=\frac{1}{T}
$$

so that

$$
\Delta B(t / T) \sim \operatorname{Normal}(0,1 / T)
$$

It follows that

$$
F_{T} \Delta B(t / T)=\sigma \varepsilon_{t} \sim \operatorname{Normal}(0,1)
$$

thus

$$
\Delta B\left(t_{T}\right)=\frac{\varepsilon_{t}}{\sqrt{\delta^{2} T}}
$$

Now

$$
\begin{aligned}
B(t / T) & =\sum_{s=1}^{t} \Delta B(S / T) \\
& =\sum_{s=1}^{t} \frac{\varepsilon_{s}}{\sqrt{b^{2} T}}
\end{aligned}
$$

Nole that

$$
B(1)=\sum_{t=1}^{T} \frac{\varepsilon_{t}}{\sqrt{\sigma^{2} T}}
$$

and

$$
B(1) \sim \text { Normal }(0,1)
$$

Now for unit root

$$
x_{T}=\sum_{t=1}^{T} \varepsilon_{t}
$$

so that

$$
\begin{aligned}
& x_{t}=\sqrt{\sigma^{2} T} B(t / T) \\
& B(t / T)=\frac{x_{t}}{\sqrt{\sigma^{2} T}}
\end{aligned}
$$

using, these results an expression for 's can be written as swms over Brawnian Motion

$$
\begin{aligned}
T \hat{\delta} & =\frac{\sum_{t=1}^{T} X_{t-1} \varepsilon_{t}}{\sum_{t=1}^{T} X_{t-1}^{2}} \\
& =\frac{\sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{\sigma^{2} T}}\right)\left(\frac{\varepsilon_{t}}{\sqrt{\sigma^{2} T}}\right)}{\frac{1}{T} \sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{\sigma^{2} T}}\right)^{2}} \\
& =\frac{\sum_{t=1}^{T} B(t-1 / T) \Delta B\left(t_{T}\right)}{\sum_{t=1}^{T} B^{2}(t-1 / T) \frac{1}{T}}
\end{aligned}
$$

In the provias section in the definition of the Itô integral it was shown that for a function of Brownian motion, $f\left(B_{t}, t\right)$, that in the limit $T \rightarrow \infty$

$$
\begin{aligned}
& \int_{0}^{1} f\left(s, B_{s}\right) d B_{s} \\
&=\lim _{T \rightarrow \infty} \sum_{s=1}^{T} f\left(\frac{s}{T}, B_{\frac{s-1}{T}}\right) \Delta B_{\frac{s}{T}}
\end{aligned}
$$

Here for the numerator

$$
f\left(t, B_{t}\right)=B(t)
$$

trus
$\int_{0}^{1} B(s) d B(s)=\lim _{T \rightarrow \infty} \sum_{t=1}^{T} B(t-1 / T) \Delta B(t / T)$
and for the denominator, noting that as $T \rightarrow \infty$

$$
\frac{1}{T} \rightarrow d t
$$

The sum approaches the integral

$$
\int_{0}^{1} B^{2}(s) d s=\lim _{T \rightarrow \infty} \sum_{t=1}^{T} B^{2}(t-1 / T) \frac{1}{T}
$$

Bringing things together in the limit $T \rightarrow \infty$ and using the Donsker FCLT Theorem which states that asymptotically sums of random variables apprach the distribution of a standard wiener process it follows that,

$$
T \hat{\delta} \xrightarrow{\int_{0}^{1} B(s) d B(s)} \frac{\int_{0}^{1} B^{2}(s) d s}{}
$$

Now the integral in the numerator can be evaluated using the Itó formula,

$$
\begin{aligned}
d f= & {\left[\frac{\partial f}{\partial t}+\mu \frac{\partial f}{\partial x_{t}}+\frac{\sigma^{2}}{2} \frac{\partial^{2} f}{\partial x_{t}^{2}}\right] d t } \\
& +\sigma \frac{\partial f}{\partial x_{t}} d B_{t}
\end{aligned}
$$

wth

$$
\begin{aligned}
& f\left(t, B_{t}\right)=\frac{1}{2} B^{2}(t) \\
& \mu=0 \quad \sigma=1
\end{aligned}
$$

so that

$$
X_{t}=B(t)
$$

gives

$$
\begin{aligned}
& d f=\frac{1}{2} \frac{\partial^{2} f}{\partial B_{t}^{2}} d t+\frac{\partial f}{\partial B_{t}} d B_{t} \\
\Rightarrow & d\left(\frac{1}{2} B^{2}(t)\right)=\frac{1}{2} d t+B(t) d B(t) \\
\Rightarrow & \frac{1}{2} B^{2}(t)=\int d t+\int B(t) d B(t)
\end{aligned}
$$

$\Rightarrow \int B(t) d B(t)=\frac{1}{2} B^{2}(t)-\int d t$
The definite integral is given by

$$
\begin{aligned}
\int_{0}^{1} B(t) & d B(t)=\left.\frac{1}{2} B^{2}(t)\right|_{0} ^{1}-\int_{0}^{1} d t \\
= & \frac{1}{2}\left[B^{2}(1)-1\right]
\end{aligned}
$$

since by definition $B(0)=0$. Thus

$$
\begin{aligned}
T \hat{\delta} \xrightarrow{D} & \frac{\int_{0}^{1} B(s) d B(s)}{\int_{0}^{1} B^{2}(s) d s} \\
& =\frac{\frac{1}{2}\left[B^{2}(1)-1\right]}{\int_{0}^{1} B^{2}(s) d s}
\end{aligned}
$$

Recalling that the $t$-statistry
is given by

$$
t=\frac{\hat{\delta}}{S E(\hat{\delta})}
$$

and

$$
\operatorname{se}(\hat{\delta})=\sqrt{\operatorname{var}(\hat{\delta})}
$$

Recalling that

$$
\begin{aligned}
\operatorname{Var}(\hat{\delta}) & =\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t-1}^{2}} \\
& =\frac{\left(\frac{1}{T}\right)^{2}}{\sum_{t=1}^{T}\left(\frac{x_{t-1}}{\sigma \sqrt{T}}\right)^{2} \frac{1}{T}} \\
\Rightarrow T^{2} \operatorname{var}(\hat{\delta}) & =\frac{1}{\sum_{t=1}^{T}\left(\frac{x_{t-1}}{\sigma T}\right)^{2} \frac{1}{T}}
\end{aligned}
$$

But

$$
B(t-1 / T)=\frac{X_{t-1}}{\sqrt{\sigma^{2} T}}
$$

and previously it was shown that in the limit $T \rightarrow \infty$ that

$$
\sum_{t=1}^{T} B^{2}(t-1 / T) \frac{1}{T} \xrightarrow{D} \int_{0}^{1} B^{2}(s) d s
$$

it follows that

$$
T^{2} \operatorname{Var}(\hat{\delta}) \xrightarrow{D} \frac{1}{\int_{0}^{1} B^{2}(s) d s}
$$

and from the continuous mapping
theorem theorem

$$
\operatorname{TSE}(\hat{\delta})=T \sqrt{\operatorname{Uar}(\hat{\delta})} \xrightarrow{D} \frac{l}{/ \int_{0}^{1} B^{2}(s) d s}
$$

The Desired result follows

$$
\begin{aligned}
t= & \frac{T \hat{\delta}}{T S E(\hat{\delta})}=\frac{\hat{\delta}}{S E(\hat{\delta})} \\
& \xrightarrow{D} \frac{\frac{1}{2}\left[B^{2}(1)-1\right]}{\sqrt{\int_{0}^{1} B^{2}(s) d s}}
\end{aligned}
$$

thus the distribution of the t-statistic is given by

$$
t \xrightarrow{D} \frac{\frac{1}{2}\left[B^{2}(1)-1\right]}{\sqrt{\int_{0}^{1} B^{2}(s) d s}}
$$

This is a nonstandard distribution that has no closed form. Simulation is required for evaluation.

## Dickey-Fuller Distribution Simulations

In the previous section the asymptotic distribution of the Dickey- Fuller test otatistic was derived. The result was a random variable not a standard distribution. To determine the distribution a simulation must be performed.
The Dickey- Fuller test statistic is defined by

$$
t=\frac{\hat{\delta}}{\sqrt{\operatorname{Uar}(\hat{\delta})}}
$$

where $\hat{\delta}$ is the ols estimate of the ARCC) parameter,

$$
\begin{aligned}
x_{t} & =\varphi x_{t-1}+\varepsilon_{t} \\
\delta & =\varphi-1
\end{aligned}
$$

and the $\varepsilon_{t}$ are independent and identically distribated random variables

$$
\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)
$$

for the simulations of the $t$-statistic distribution the variance of $\varepsilon_{t}$ does not matter so it is assumed that $\sigma=1$ then

$$
\varepsilon_{t} \sim \operatorname{Normal}(0,1)
$$

For the unt root case $\varphi=1$ so $\delta=0$ and if $t$ is assumed also that $x_{0}=0$ then

$$
x_{t}=\sum_{i=1}^{t} \varepsilon_{i}
$$

In the derivation of the asimptofic distributions use was made of the Donsker Functional central Limit Theorem which states that in the limit $T \rightarrow \infty$ for $t<T$

$$
\frac{X_{t}}{\sqrt{T}}=\sum_{i=1}^{t} \frac{\varepsilon_{i}}{\sqrt{T}} \xrightarrow{D} B(t / T)
$$

where $B(t / T)$ is a continuous time weiner process also

$$
\Delta B(t)=\frac{\varepsilon_{i}}{\sqrt{T}}
$$

so,

$$
\operatorname{Var}(A B(t))=\frac{1}{T}
$$

Further, from the defintion of the Its integral asymptotically

$$
\begin{aligned}
& \sum_{t=1}^{T} \frac{X_{t-1}}{\sqrt{T}} \frac{\varepsilon_{t}}{\sqrt{T}} \xrightarrow{1} \int_{0}^{1} B(s) d B(s) \\
& \sum_{t=1}^{T} \frac{X_{t-1}^{2}}{T} \perp \int_{0}^{1} B^{2}(s) d s
\end{aligned}
$$

using these results it follows that the asymtotic distribution of $\hat{\delta}$ is given by

$$
T \hat{\delta} \xrightarrow{\int_{0}^{1} B(s) d B(s)} \frac{\int_{0}^{1} B^{2}(s) d s}{}
$$

and that

$$
T \sqrt{\operatorname{Uar}(\hat{\delta})} \xrightarrow{L} \frac{l}{T \int_{0}^{1} B^{2}(s) d s}
$$

It follows that

$$
t \xrightarrow{\int_{0}^{1} B(s) d B(s)} \frac{\sqrt{\int_{0}^{1} B^{2}(s) d s}}{}
$$

The integral in the numerator can be evaluated analytically
using the Itô formula

$$
\int_{0}^{1} B(s) d B(s)=\frac{1}{2}\left[B^{2}(1)-1\right]
$$

so that

$$
t \xrightarrow{\frac{1}{2}\left[B^{2}(1)-1\right]} \frac{\sqrt{\int_{0}^{1} B^{2}(s) d s}}{}
$$

First consider the numerator, Since

$$
B(1) \sim \operatorname{Normal}(0,1)
$$

$B^{2}(1)$ has a chi-squared distribution with 1 degree of freedom

$$
B^{2}(1) \sim x_{1}^{2}
$$

where the $y^{2}$ I PDF is given by

$$
x_{1}^{2}(y)=\frac{1}{\sqrt{2 \pi y}} e^{-y / 2}
$$

where

$$
\begin{aligned}
& E(y)=1 \\
& \operatorname{Var}(y)=2
\end{aligned}
$$

To find the PDF of $\frac{1}{2}\left[B^{2}(1)-1\right]$ let

$$
\begin{aligned}
\omega & =\frac{1}{2}(y-1) \\
\Rightarrow y & =2 \omega+1
\end{aligned}
$$

then

$$
\frac{d y}{d \omega}=2
$$

where $-1 / 2<\omega<\infty$ since $0<y<\infty$

$$
f_{\omega}(\omega)=\frac{2}{\sqrt{2 \pi(2 \omega+1)}} e^{-(2 \omega+1) / 2}
$$

The mean and variance are given by

$$
E(\omega)=E\left[\frac{1}{2}(y-1)\right]
$$

$$
\begin{aligned}
&= \frac{1}{2}(E(y)-1) \\
&= \frac{1}{2}(1-1) \\
&= 0 \\
& \operatorname{Var}(\omega)=E\left(\omega^{2}\right)-(E(\omega))^{2} \\
&=E\left[\frac{1}{4}(y-1)^{2}\right]-0 \\
&=\frac{1}{4} E\left[(y-1)^{2}\right] \\
&=\frac{1}{4} \operatorname{Uar}(y) \\
&=\frac{1}{4}(2)=1 / 2
\end{aligned}
$$

Thus

$$
\begin{gathered}
\frac{1}{2}\left[B^{2}(1)-1\right] \sim \frac{2}{\sqrt{2 \pi(2 \omega-1)}} e^{-(2 \omega-1) / 2} \\
\frac{1}{2} E\left[B^{2}(1)-1\right]=0 \\
\frac{1}{4} \operatorname{Uar}\left[B^{2}(1)-1\right]=\frac{1}{2}
\end{gathered}
$$

The first simulations validate the integral

$$
\int_{0}^{1} B(S) d B(S)=\frac{1}{2}\left[B^{2}(1)-1\right]
$$

A Riemann sum is used to approximate the integral

$$
\begin{aligned}
& \int_{0}^{1} B(s) d B(s) \approx \sum_{t=1}^{T} B(t-1 / T) \Delta B\left(t_{T}\right) \\
& =\sum_{t=1}^{T} \frac{x_{t-1}}{\sqrt{T}} \frac{\varepsilon_{t}}{\sqrt{T}}
\end{aligned}
$$

and

$$
\mu=0 \quad \sigma=\frac{1}{12}=0.707
$$

The solution PDF is given by,

$$
f_{\omega}(\omega)=\frac{2}{\sqrt{2 \pi(2 \omega+1)}} e^{-(2 \omega+1) / 2}
$$

The following plots compare a simulation of the solution and a simulation of the integral with the analytic PDF, mean and standad deviation for different sample size. The first plots compute

$\frac{1}{2}\left[B^{2}(1)-1\right]$, Sample Size $=1000, \mu=-0.02, \sigma=0.69$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-462.jpg?height=636&width=933&top_left_y=650&top_left_x=386)

$\int_{0}^{1} B(s) d B(s)$, Sample Size $=1000, \mathrm{~T}=1000, \mu=-0.03, \sigma=0.65$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-462.jpg?height=618&width=922&top_left_y=1370&top_left_x=378)

the distribution, mean and variance using an ensemble of 1000 samples and the second set 10,00d 100,000 samples. Both agree well with the analytic results.

$\frac{1}{2}\left[B^{2}(1)-1\right]$, Sample Size $=100000, \mu=-0.00, \sigma=0.70$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-463.jpg?height=588&width=870&top_left_y=602&top_left_x=382)

$\int_{0}^{1} B(s) d B(s)$, Sample Size $=100000, \mathrm{~T}=1000, \mu=-0.00, \sigma=0.70$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-463.jpg?height=581&width=859&top_left_y=1332&top_left_x=395)

The next set of simulations eveluate the distribution of the integral

$$
\sqrt{\int_{0}^{1} B^{2}(s) d s} \approx \sqrt{\frac{1}{T} \sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{T}}\right)^{2}}
$$

Before simulating the integral above for validation consider

$$
\int_{0}^{1} B^{2}(s) d s=\frac{1}{T} \sum_{t=1}^{T}\left(\frac{X_{t-1}}{\sqrt{T}}\right)^{2}
$$

Recall that

$$
x_{t-1}=\sum_{i=1}^{t-1} \varepsilon_{i}
$$

Since

$$
E\left(\varepsilon_{i}\right)=0 \quad E\left(\varepsilon_{i}^{2}\right)=1
$$

It follows that

$$
E\left(x_{t-1}^{2}\right)=t-1
$$

The mean value of the integral can be computed and compared and compared with simclations since the distribution is unknown

$$
\begin{aligned}
E & {\left[\frac{1}{T} \sum_{t=1}^{T}\left(\frac{X_{t-1}}{\Gamma T}\right)^{2}\right]=\frac{1}{T^{2}} \sum_{t=1}^{T} E\left(X_{t-1}\right)^{2} } \\
& =\frac{1}{T^{2}} \sum_{t=1}^{T} t-1 \\
& =\frac{1}{T^{2}}\left[\frac{T(T+1)}{2}-1\right] \\
& =\frac{1}{2 T^{2}}\left(T^{2}+T-1\right) \\
& =\frac{1}{2}\left(1+1 / T-1 / T^{2}\right)
\end{aligned}
$$

For $T \rightarrow \infty$

$$
E\left[\frac{1}{T} \sum_{t=1}^{T}\left(\frac{x_{t-1}}{\Gamma T}\right)^{2}\right]=\frac{1}{2}
$$

The following plot shows the result
of 10,000 simulations with $T=1000$ of the integral.

$$
\int_{0}^{1} B^{2}(s) d s
$$

The mean obtainted agrees with the analytic result of $1 / 2$. The distribution obtained is not obviously of any known type but is possibly related to a variant of the $x^{2}$.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-466.jpg?height=807&width=1120&top_left_y=1102&top_left_x=243)

The following plot shows the results of 10,000 smulations of

$$
\sqrt{\int_{0}^{1} B^{2}(s) d s}
$$

with $T=1000$. The result obtained is not a well thoun distribution.
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-467.jpg?height=875&width=1188&top_left_y=955&top_left_x=195)

The final set of simulations evaluate the distribution of the Dickey. Fuller $t$-statistic using the previous results

$$
t \sim \frac{\frac{1}{2}\left[B^{2}(1)-1\right]}{\sqrt{\int_{0}^{1} B^{2}(s) d s}}
$$

The first plot shows the result of 1000 simulations of $t$ and is compared to the cont normal distribution
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-468.jpg?height=737&width=970&top_left_y=1170&top_left_x=324)

The next two simulation ensembles of size 10,000 and 100,000 illustrate convergence of the distribution to

$$
\begin{aligned}
& \mu \rightarrow 0 \\
& \sigma \rightarrow 1.65
\end{aligned}
$$

The result is clearly not a whit normal. Though $\mu \rightarrow 0$ the distribution is assymetric about the mean with mode approaching -0.5 .
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-469.jpg?height=739&width=970&top_left_y=1184&top_left_x=292)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-470.jpg?height=813&width=1070&top_left_y=70&top_left_x=261)

To the left of the mode the decay of the distribution is more rapd than a unit normal while to the right of the mode the decay is much slower than a unit normal leading to a fat tail. It is likely trat the mean and variance do not converge but this has not been verified in the literature. I have not even been able to locate a good plot of the distribution.

## Dickey-Fuller Test Example

Consider AR(1)

$$
x_{t}-x_{t-1}=\Delta x_{t}=\delta x_{t-1}+\varepsilon_{t}
$$

The desire is to design a test given $T$ samples,

$$
x_{1}, x_{2}, \ldots, x_{T}
$$

to determine if the sequence of samples is stationary
Given the sample data the estimate, $\hat{\delta}$, is given by

$$
\hat{\delta}=\frac{\sum_{t=1}^{T} X_{t-1} \Delta X_{t}}{\sum_{t=1}^{T} X_{t-1}^{2}}
$$

and

$$
\operatorname{Var}(\hat{\delta})=\frac{\sigma^{2}}{\sum_{t=1}^{T} x_{t-1}^{2}}
$$

The $t$-statistic is defined by

$$
\begin{aligned}
t & =\frac{\hat{\delta}}{\sqrt{\operatorname{Uar}(\hat{\delta})}} \\
& =\frac{\sum_{t=1}^{T} x_{t-1} \Delta x_{t}}{\sigma^{2} \sqrt{\sum_{t=1}^{T} x_{t-1}^{2}}}
\end{aligned}
$$

The null hypothesis for the test is
$H_{0}$ : The estimated value of $\delta$ is zero so the analyzed samples are not stationary
The alternative hypothesis is
$H_{A}$ : The estimated value of $\delta$ is less than zero so the analyzed samples are stationary

This is a one sided left-tail test. A significance level of $\alpha=0.05$ is illustrated in the following plots of simulations of Dickey-Fuller PDF and CDF. The critical value is indicated in both plots occurs at the value of $t$ where the CDF equals 2,

$$
P\left(t \leqslant t_{c}\right)=\alpha=0.05
$$

$$
\mathrm{t}=\frac{\frac{1}{2}\left[B^{2}(1)-1\right]}{\sqrt{\int_{0}^{1} B^{2}(s) d s}} \text {, Sample Size }=10000, \mathrm{~T}=1000, \mu=-0.02, \sigma=1.59
$$

![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-473.jpg?height=796&width=1134&top_left_y=1144&top_left_x=227)
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-474.jpg?height=898&width=1154&top_left_y=189&top_left_x=211)

From inspecton of the CDF plot the critical value of $t$ is about $-1,8$. The the ADF test in the statsmills python package reports a critical value of -1.94 for the DF test. This is close to the crude estimate obtined by inspection of the simulated DF distribution.

The following plots show the results of three simulations of AR(1) with $\varphi=0.5,0.99,1.01$. The first two are stationary, but the second barely and the final simulation is barely not stationary. The t-statistic is computed using,

$$
t=\frac{\hat{\delta}}{\sqrt{\operatorname{Uar}(\hat{\delta})}}
$$

and compared to the previously estimated critical value of -1.8 testing for stationants. The results obtained are cosistent values of $\varphi$ wed to generate the simulation data used in the analysis. The results are also consisitent with an analysis of the simulted samples using the python statsmodels adfuller package.

AR(1) Series: $\varphi=0.5, \sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-476.jpg?height=690&width=1045&top_left_y=147&top_left_x=259)

## statsmodels odfuller results

ADF Statistic: -19.061976
p-value: 0.000000
Is Stationary at $5 \%$ : True
Critical Values
1\%: -2.568
5\%: -1.941
10\%:-1.617

AR(1) Series: $\varphi=0.99, \sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-477.jpg?height=678&width=1051&top_left_y=233&top_left_x=261)

## statsmodels odfuller results

ADF Statistic: -3.352189
p-value: 0.000817
Is Stationary at 5\%: True
Critical Values
1\%: -2.568
5\%: -1.941
10\%: -1.617
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-478.jpg?height=724&width=1061&top_left_y=183&top_left_x=253)

## statsmodels odfuller results

ADF Statistic: 5.376149
p-value: 1.000000
Is Stationary at 5\%: False
Critical Values
1\%: -2.570
5\%: -1.942
10\%:-1.616

A couple of simulations were also perfomed to examine the results for two stationary cases with $-1<\varphi<0$.

AR(1) Series: $\varphi=-0.5, \sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-479.jpg?height=698&width=1045&top_left_y=594&top_left_x=257)

statsmodels odfuller results

ADF Statistic: -54.216374
p-value: 0.000000
Is Stationary at 5\%: True
Critical Values
1\%: -2.568
5\%: -1.941
10\%: -1.617

AR(1) Series: $\varphi=-0.99, \sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-480.jpg?height=747&width=1142&top_left_y=197&top_left_x=187)
statsmodels odfuller results

ADF Statistic: -423.525877
p-value: 0.000000
Is Stationary at 5\%: True
Critical Values
1\%: -2.568
5\%: -1.941
10\%: -1.617

## Augmented Dekey-Fuller Test Example

The previous section disoussed the Dickey-Fuller test which is used to estumate $\delta$ for samples from the AR(1) process

$$
x_{t}=\varphi x_{t-1}+\varepsilon_{t}
$$

There are two other cases which address two other models. These tests are called the Augmented Dickey. Fuller Tests.
The first adds a constant to ARCD givng

$$
x_{t}=\mu+\varphi x_{t-1}+\varepsilon_{t}
$$

The second of Augmented Dickey. Fuller tests additionally assumes a linear trend so that three parameters are estimated. The model is given by

$$
x_{t}=\mu+\gamma t+\phi x_{t-1}+\varepsilon_{t}
$$

The $t$-statistic used to test for stationarity of these two forms will differ from the one used for the Drokey - Fuller test. Because of this t-statistic distribution preciously used for mypothis testing aunnot be used.
In the following sections stationary and non stationar simulations of the two models will be used as inputs into the statsmodels package adfuller test to illustrate usage

## $x_{t}=\mu+\phi x_{t-1}+\varepsilon_{t} \quad$ Examples

Three smulations of the model

$$
x_{t}=\mu+\phi x_{t-1}+\varepsilon_{t}
$$

performed with a range of values of $\phi$. For the first $q=0.5$. The second is barely stationary with $\varphi=0.99$ and the last barely not stationary with $\varphi=1.01$. The simulated data is used as irput into statmodels adfaller to illestrate its usage.

AR(1) Series with constant offset: $\varphi=0.5, \sigma=1.0, \mu=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-483.jpg?height=670&width=1069&top_left_y=1291&top_left_x=308)

## statsmodels odfuller results

ADF Statistic: -18.374148
p-value: 0.000000
Is Stationary at 5\%: True
Critical Values
1\%: -3.437
5\%: -2.864
10\%: -2.568
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-484.jpg?height=714&width=1055&top_left_y=671&top_left_x=231)
statsmodels odfuller results
ADF Statistic: -8.124984
p-value: 0.000000
Is Stationary at $5 \%$ : True
Critical Values
1\%: -3.437
5\%: -2.864
10\%: -2.568
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-485.jpg?height=821&width=1053&top_left_y=171&top_left_x=257)

$$
\begin{aligned}
& \text { ADF Statistic: } 33.225628 \\
& \text { p-value: } 1.000000 \\
& \text { Is Stationary at } 5 \% \text { : False } \\
& \text { Critical Values } \\
& 1 \%:-3.437 \\
& 5 \%:-2.864 \\
& 10 \%:-2.568
\end{aligned}
$$

$x_{t}=\mu+\gamma t+\phi x_{t-1}+\varepsilon_{t} \quad$ Examples Three simulations of the model

$$
x_{t}=\mu+\gamma t+\varphi x_{t-1}+\varepsilon_{t}
$$

performed with a range of values of $\phi$. For the first $q=0.5$. The second is barely stationary with $\varphi=0.99$ and the last barely not stationary with $\varphi=1.01$. The simulated data is used as irput into statmodels adtaller to illestrate its usage.

AR(1) Series with constant offset and trend: $\varphi=0.5, \sigma=1.0, \mu=1.0, \gamma=0.01$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-486.jpg?height=633&width=969&top_left_y=1275&top_left_x=329)

## statsmodels odfuller results

ADF Statistic: -8.876475
p-value: 0.000000
Is Stationary at 5\%: True
Critical Values
1\%: -3.968
5\%: -3.415
10\%: -3.130

AR(1) Series with constant offset and trend: $\varphi=0.99, \sigma=1.0, \mu=1.0, \gamma=0.01$
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-487.jpg?height=595&width=942&top_left_y=693&top_left_x=264)

statsmodels odfuller results
ADF Statistic: -3.422254
p-value: 0.048485
Is Stationary at 5\%: True
Critical Values
1\%: -3.968
5\%: -3.415
10\%: -3.130
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-488.jpg?height=619&width=989&top_left_y=213&top_left_x=294)

## statsmodels odfuller results

ADF Statistic: 181728.838579
p-value: 1.000000
Is Stationary at 5\%: False
Critical Values
1\%: -3.968
5\%: -3.415
10\%: -3.130

## The F-test

Consider a set of $m$ observations

$$
x_{1}, x_{2}, x_{3}, \ldots x_{m}
$$

The sample variance is defined by

$$
S_{x}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(x_{i}-\mu_{x}\right)^{2}
$$

Let $\sigma_{y}^{2}$ denote the population variance then

$$
\begin{aligned}
\Rightarrow(m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}} & =\sum_{i=1}^{m} \frac{\left(x_{i}-\mu_{x}\right)^{2}}{\sigma_{x}^{2}} \\
& =\sum_{i=1}^{m}\left(\frac{x_{i}-\mu_{x}}{\sigma_{x}}\right)^{2}
\end{aligned}
$$

if it is assumed that

$$
\frac{x_{i}-\mu_{x}}{\sigma_{x}} \sim \operatorname{Normal}(0,1)
$$

then in the analysis of Pearson's Chi-squared test it was shown that asymtotically

$$
(m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}}=x_{m-1}^{2} \xrightarrow{D} \text { Chi-Squared }(m-1)
$$

thus,

$$
(m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}}
$$

assymtotically approaches a Chi-Squared distribution with $m-1$ degrees of freedom.
Thus asymptotically

$$
S_{x}^{2} \xrightarrow{D} \frac{\sigma_{x}^{2}}{m-1} x_{m-1}^{2}
$$

A test on a single variance can be constructed in the following maner.
If the population variance is assumed to be

$$
\sigma_{x}^{2}=a
$$

Then a $t$-statistic that tests the null hypothesis
$H_{0}: \sigma_{x}^{2}=a$
and alternative hypothesis

$$
H_{A}: \sigma_{x}^{2} \neq a
$$

Can be constructed in the following manner

$$
t=(m-1) \frac{s_{x}^{2}}{a} \xrightarrow{D} x_{m-1}^{2}
$$

For the stated null and atternalive hypothesis a
two tailed test is used. ofsuming a significance level

$$
\alpha=0.05
$$

gives the oritical values

$$
113.65,180.23
$$

$\chi^{2}$ CDF, Number of Degrees of Freedom: 145
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-492.jpg?height=831&width=1166&top_left_y=856&top_left_x=195)

Consider an experiment where it is observed that

$$
S_{x}^{2}=308.56
$$

and test against the variance

$$
a=225
$$

then

$$
t=\frac{(146-1)(308.56)}{225}=198.85
$$

Since

$$
t \geqslant 180.23
$$

the null hypotheis is rejected. In fact an atternative hypothesis that the sample variace is greater that $a=225$ can be accepted.
The P-value which measures the probability of dotaining $t=198.85$ is the tail propeplility

$$
1-P(t \geqslant 198.85)=0.002
$$

The confidence interval for a given level of significance, $a$, is defined by

$$
P\left(t_{1} \leqslant t \leqslant t_{2}\right)=1-\alpha
$$

where

$$
\begin{aligned}
& P\left(t \leqslant t_{1}\right)=\frac{1}{2} \alpha \\
& P\left(t \geqslant t_{2}\right)=1 / 2 \alpha
\end{aligned}
$$

Now using

$$
t=(m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}}
$$

gives

$$
\begin{aligned}
& P\left(t_{1} \leqslant t \leqslant t_{2}\right)=P\left[t_{1} \leqslant(m-1) \frac{S_{x}^{2}}{S_{x}^{2}} \leqslant t_{2}\right] \\
& =P\left[\frac{1}{t_{2}} \leqslant \frac{\sigma_{x}^{2}}{(m-1) S_{x}^{2}} \leqslant \frac{1}{t_{1}}\right] \\
& =P\left[\frac{(m-1) S_{x}^{2}}{t_{2}} \leqslant \sigma_{x}^{2} \leqslant \frac{(m-1) S_{x}^{2}}{t_{1}}\right] \\
& =1-\alpha
\end{aligned}
$$

For a two tailed test it follows that for a level of significance of $\alpha=0.05$ and using the oalues of $m$ and $s_{x}^{2}$ from the previous experiment

$$
\begin{array}{ll}
m=146 & S_{x}^{2}=308.56 \\
t_{1}=113.65 & t_{2}=180.23
\end{array}
$$

it follows that

$$
\begin{aligned}
& \frac{(m-1) S_{x}^{2}}{t_{2}}=\frac{(146-1)(308.56)}{180.23}=248.25 \\
& \frac{(m-1) S_{x}^{2}}{t_{1}}=\frac{(146-1)(308.56)}{113.64}=393.99
\end{aligned}
$$

thus with a probability of 0,95

$$
P\left(248.25 \leqslant \sigma_{x}^{2} \leqslant 393.99\right)=0.95
$$

which defines the $95 \%$ confidence interval.
vext consider the case where the varrance of two sets of observations are compared. Denote the observations by

$$
\begin{aligned}
& x_{1}, x_{2}, x_{3}, \ldots, x_{m} \\
& y_{1}, y_{2}, y_{3}, \ldots, y_{n}
\end{aligned}
$$

where $m$ samples of the $X_{i}$ observations are available and $n$ observations of $y_{i}$ are available. The sample variances are given by

$$
\begin{aligned}
& s_{x}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(x_{i}-\mu_{x}\right)^{2} \\
& s_{y}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\mu_{y}\right)^{2}
\end{aligned}
$$

Also, assume that the pspulation variances are given by $\sigma_{x}^{2}$ and $\sigma_{y}^{2}$. Consider the natio

$$
\frac{(m-1) \frac{S_{x}^{2}}{S_{x}^{2}}}{(n-1) \frac{S_{y}^{2}}{\sigma_{y}^{2}}}
$$

assymtotically

$$
\begin{aligned}
& (m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}} \xrightarrow{D} x_{m-1}^{2} \\
& (n-1) \frac{S_{y}^{2}}{\sigma_{y}^{2}} \xrightarrow{D} x_{n-1}^{2}
\end{aligned}
$$

If the numerator and denominator are asswed to be irdependent then asymtotically

$$
\frac{(m-1) \frac{S_{x}^{2}}{\sigma_{x}^{2}}}{(n-1) \frac{S_{y}^{2}}{\sigma_{y}^{2}}} \xrightarrow{D} \frac{x_{m-1}^{2}}{x_{n-1}^{2}}
$$

$$
\Rightarrow \frac{\delta_{x}^{2}}{\delta_{y}^{2}} \xrightarrow{D} \frac{\sigma_{x}^{2}}{\sigma_{y}^{2}} \frac{\frac{x_{m-1}^{2}}{(m-1)}}{\frac{x^{2}-1}{n-1}}
$$

If the null hypothesis assumed is that the peoulation variances are equal then

$$
\begin{aligned}
\frac{S_{x}^{2}}{S_{y}^{2}} \xrightarrow{D} & \frac{x_{m-1}^{2} / m-1}{x^{2}-1 / n-1} \\
& =\frac{n-1}{m-1} \frac{x^{2} m-1}{x_{n-1}^{2}}
\end{aligned}
$$

thus the ratio of the sample variances cassymtotically approaches a ratio of chi-squared distributions of order $m-1$ and $n-1$.
The next section will derive this distribution

## F-Distribution

In the previous section it was shown that for two sets of samples with population varrances

$$
\begin{aligned}
& S_{x}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(x_{i}-\mu_{x}\right)^{2} \\
& S_{y}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\mu_{x}\right)^{2}
\end{aligned}
$$

that if both data sets are assumed to have equal population variances $\sigma_{x}^{2}=\sigma_{y}^{2}$ then the ratio of the sample variances asymtotically approaches a disfribution that is the ratis of independent Chi-squared distributions,

$$
\frac{s_{x}^{2}}{s_{y}^{2}} \unrhd \rightarrow \frac{n-1}{m-1} \frac{x^{2} m-1}{x_{n-1}^{2}}
$$

Now recall that the $x_{n}^{2}$ PDF is given by

$$
f(x)=\frac{1}{2^{k / 2} \Gamma\left(k_{k}\right)} x^{k / 2-1} e^{-x / 2}
$$

and the distribution of the ratio of two indepent random variables is given by

$$
\begin{gathered}
t=\alpha \frac{x}{y} \\
f_{T}(t)=\int_{0}^{\infty} f_{x}(t y) f_{y}(y) \frac{y}{\alpha} d y
\end{gathered}
$$

Here

$$
x \sim x_{m}^{2} \quad y \sim x_{m}^{2}
$$

It follows that

$$
f_{x}(x ; m)=\frac{1}{2^{m / 2} \Gamma\left(\frac{m}{2}\right)} x^{m / 2-1} e^{-x / 2}
$$

$$
f_{y}(y ; n)=\frac{1}{2^{n / 2} \Gamma\left(\frac{n}{2}\right)} y^{\frac{n}{2}-1} e^{-y / 2}
$$

Now since

$$
t=\frac{s_{x}^{2}}{s_{y}^{2}} \xrightarrow{D} \frac{n-1}{m-1} \frac{x_{m-1}^{2}}{x_{n-1}^{2}}
$$

let

$$
\begin{aligned}
t & =\frac{x_{m}}{y / n}=\frac{n}{m} \frac{x}{y} \\
& \Rightarrow x=\frac{m}{n} t y
\end{aligned}
$$

so the expression for the ratio distribution gives assuming,

$$
\begin{gathered}
\alpha=\frac{n}{m} \\
f_{T}(t)=\int_{0}^{\infty} f_{x}(t y) f_{y}(y) \frac{y}{2} d y
\end{gathered}
$$

$$
\begin{aligned}
& =\int_{0}^{\infty}\left[\frac{1}{2^{m / 2} \Gamma\left(\frac{m}{2}\right)}\left(\frac{m}{n} t y\right)^{m / 2-1} e^{-\frac{m}{n} t y / 2}\right] \\
& {\left[\frac{1}{2^{n / 2} \Gamma\left(\frac{n}{2}\right)} y^{\frac{n}{2}-1} e^{-y / 2}\right] y d y} \\
& =\frac{1}{2^{m / 2} \Gamma\left(\frac{m}{2}\right)} \frac{1}{2^{n / 2} \Gamma\left(\frac{n}{2}\right)} \int_{0}^{\infty}\left(\frac{m}{n} t y\right)^{m / 2-1} e^{-\frac{1}{2} \frac{m}{n} t y} \\
& y^{\frac{3}{2}-1} e^{-y / 2} y\left(\frac{m}{n}\right) d y \\
& =\frac{\left(\frac{m}{n} t\right)^{\frac{m}{2}-1}\left(\frac{m}{n}\right)}{2^{m / 2+n_{2}} \Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)^{\infty}} \int^{\infty} y^{\frac{m}{2}+\frac{n}{2}-1} e^{-\frac{1}{2} y\left(\frac{m}{n} t+1\right)} d y
\end{aligned}
$$

Consider the integral and the change of variables

$$
\begin{aligned}
u & =\frac{1}{2} y\left(\frac{m}{n} t+1\right) \\
\Rightarrow y & =\frac{2 u}{\left(\frac{m}{n} t+1\right)}
\end{aligned}
$$

$$
\Rightarrow d y=\frac{2}{\left(\frac{m}{n} t+1\right)} d u
$$

so

$$
\begin{aligned}
& \int_{0}^{\infty} y^{\frac{m}{2}+\frac{n}{2}-1} e^{-\frac{1}{2} y}\left(\frac{m}{n} t+1\right) \\
& =\int_{0}^{\infty}\left[\frac{2 u}{\left(\frac{m}{n} t+1\right)}\right]^{\frac{m}{2}+\frac{n}{2}-1} e^{-u} \frac{2}{\left(\frac{m}{n} t+1\right)} d u \\
& =\left[\frac{2}{\left(\frac{m}{n} t+1\right)}\right]^{\frac{m}{2}+\frac{n}{2}} \int_{0}^{\infty} u^{\frac{m}{2}+\frac{n}{2}-1} e^{-u} d u
\end{aligned}
$$

Recall trot the Camma function is defined by

$$
\Gamma(t)=\int_{0}^{\infty} x^{t-1} e^{-x} d x
$$

Thus

$$
\Gamma\left(\frac{m}{2}+\frac{n}{2}\right)=\int_{0}^{\infty} u^{\frac{m}{2}+\frac{n}{2}-1} e^{-u} d u
$$

So

$$
\begin{aligned}
\int_{0}^{\infty} y^{\frac{m}{2}+\frac{n}{2}-1} & e^{-\frac{1}{2} y\left(\frac{m}{n} t+1\right)} d y \\
& =\left[\frac{2}{\left(\frac{m}{n} t+1\right)}\right]^{\frac{m}{2}+\frac{n}{2}} \Gamma\left(\frac{m}{2}+\frac{n}{2}\right)
\end{aligned}
$$

and the final result for the distribution of the $F$-test statistic, $t$, is given by
$f_{T}(t)$
$=\frac{\left(\frac{m}{n} t\right)^{\frac{m}{2}-1}\left(\frac{m}{n}\right)}{2^{m_{k}+n_{k}} \Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)^{0}} \int^{\infty} y^{\frac{m}{2}+\frac{n}{2}-1} e^{-\frac{1}{2} y\left(\frac{m}{n} t+1\right)} d y$
$=\frac{\left(\frac{m}{n} t\right)^{\frac{m}{2}-1}\left(\frac{m}{n}\right)}{2^{m / n_{2}+n_{2}} \Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)}\left[\frac{2^{2}}{\left(\frac{m}{n} t+1\right)}\right]^{\frac{m}{2}+\frac{n}{2}} \Gamma\left(\frac{m}{2}+\frac{n}{2}\right)$

$$
\begin{aligned}
& =\frac{\Gamma\left(\frac{m}{2}+\frac{n}{2}\right)}{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)} \frac{\left(\frac{m}{n} t\right)^{\frac{m}{2}-1}\left(\frac{m}{n}\right)}{\left(\frac{n}{n} t+1\right)^{\frac{m}{2}+\frac{n}{2}}} \\
& =\frac{\Gamma\left(\frac{m}{2}+\frac{n}{2}\right)}{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)} \frac{\left(\frac{m}{n}\right)^{\frac{m}{2}} t^{\frac{m}{2}-1}}{\left(\frac{m}{n} t+1\right)^{\frac{m}{2}+\frac{n}{2}}}
\end{aligned}
$$

Recall that the Beta function is defined by

$$
B\left(\frac{m}{2}, \frac{A}{2}\right)=\frac{\Gamma\left(\frac{m}{2}\right) \Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{m}{2}+\frac{n}{2}\right)}
$$

It follows that

$$
f_{T}(t ; m, n)=\frac{1}{B\left(\frac{m}{2}, \frac{n}{2}\right)} \frac{\left(\frac{m}{n}\right)^{\frac{m}{2}} t^{\frac{m}{2}-1}}{\left(\frac{m}{n} t+1\right)^{\frac{m}{2}+\frac{n}{2}}}
$$

This is called the f-distribution * In summary the distribution of the ratio of the sample variances of the data sets

$$
\begin{aligned}
& X_{1}, X_{2}, X_{3}, \ldots, X_{m} \\
& Y_{1}, Y_{2}, Y_{3}, \ldots, Y_{n}
\end{aligned}
$$

where the sample variances are given by

$$
\begin{aligned}
s_{x}^{2} & =\frac{1}{m-1} \sum_{i=1}^{m}\left(x_{i}-\mu_{x}\right)^{2} \\
s_{y}^{2} & =\frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\mu_{y}\right)^{2}
\end{aligned}
$$

where the test statiste, $t$, asimitodically approaches the F-Distribution of order $m-1$ ard $n-1$.

$$
t=\frac{S_{y}^{2}}{S_{y}^{2}} D F(m-1, n-1)
$$

Where the density of the $F$-Distribution of order $m$
and $n$ is given by
$f_{T}(t ; m, n)=\frac{1}{B\left(\frac{n}{2}, \frac{n}{2}\right)} \frac{\left(\frac{m}{n}\right)^{\frac{m}{2}} t^{\frac{m}{2}-1}}{\left(\frac{m}{n} t+1\right)^{\frac{m}{2}+\frac{n}{2}}}$

## Properties of the F-Distribution

In the previous section it was stown that for to data sets of size $m$ and $n$,

$$
\begin{aligned}
& x_{1}, x_{2}, x_{3}, \ldots, x_{m} \\
& y_{1}, y_{2}, y_{3}, \ldots, y_{n}
\end{aligned}
$$

with sample variances

$$
\begin{aligned}
& S_{x}^{2}=\frac{1}{m-1} \sum_{i=1}^{m}\left(x_{i}-\mu_{y}\right)^{2} \\
& S_{y}^{2}=\frac{1}{n-1} \sum_{i=1}^{n}\left(y_{i}-\mu_{y}\right)^{2}
\end{aligned}
$$

that the variance ratio

$$
t=\frac{S_{x}^{2}}{S_{y}^{2}} \xrightarrow{D} F(t ; m-1, n-1)
$$

asymptotically approaches the F-Distribution of order $m-1, n-1$ where the PDF of F-Distribution
of order $a, b$ is given by
$f(t ; a, b)=\frac{1}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}} t^{\frac{a}{2}-1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{1}{2}}}$
The $F$ distribution CDF is given by

$$
\begin{aligned}
& P(T \leqslant t ; a, b)=\int_{0}^{t} f(u ; a, b) d u \\
= & \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{t} \frac{u^{\frac{a}{2}-1}}{\left(\frac{a}{b} u+1\right)^{\frac{a}{2}+\frac{b}{2}}} d u
\end{aligned}
$$

Now recall that the regularized meomplete Beta function is defined by
$I_{2}(c, d)=\frac{1}{B(c, d)} \int_{0}^{2} u^{c-1}(1-u)^{d-1} d u$
Consider the change of vamables

$$
\begin{aligned}
u & =\frac{c \omega}{c \omega+d}=\frac{\frac{d}{d} \omega}{\left(\frac{c}{d} \omega+1\right)} \\
\Rightarrow \quad 1-u & =1-\frac{c \omega}{c \omega+d} \\
& =\frac{d}{c \omega+d}=\frac{1}{\frac{c}{d \omega+1}} \\
\Rightarrow \quad d u & =\left[\frac{c}{c \omega+d}-\frac{c^{2} \omega}{(c \omega+d)^{2}}\right] d \omega \\
& =\left[\frac{c(c \omega+d)-c^{2} \omega}{(c \omega+d)^{2}}\right] d \omega \\
& =\frac{c d}{(c \omega+d)^{2}} d \omega \\
& =\frac{\frac{c}{d}}{\left(\frac{c}{d} \omega+1\right)^{2}} d \omega
\end{aligned}
$$

Consider the integration limits

$$
\begin{gathered}
u=0 \Rightarrow \omega=0 \\
u=z(t)=\frac{c t}{c t+d} \Rightarrow \omega=t
\end{gathered}
$$

Applying the change of variables gives

$$
I_{t}(c, d)=\frac{1}{B(c d)} \int_{0}^{t}\left[\frac{\frac{d}{d} \omega}{\left(\frac{c}{d} \omega+1\right)}\right]^{c-1}
$$

$$
\left[\frac{1}{\frac{c}{c} \omega+1}\right]^{d-1} \frac{\frac{d}{d}}{\left(\frac{c}{d} \omega+1\right)^{2}} d \omega
$$

$=\frac{1}{B(c d)} \int_{0}^{t} \frac{\left(\frac{c}{d}\right)^{c-1} \omega^{c-1}\left(\frac{c}{d}\right)}{\left(\frac{c}{d} \omega+1\right)^{c+d}} d \omega$
$=\frac{\left(\frac{d}{d}\right)^{c}}{B(c, d)} \int_{0}^{t} \frac{\omega^{c-1}}{(f \omega+1)^{c+d}} d \omega$
comparing with resuld obtained
for the PDF,

$$
f(t ; a, b)=\frac{1}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}} t^{\frac{a}{2}-1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{b}{2}}}
$$

and making the associations

$$
c=\frac{1}{2} a \quad d=\frac{1}{2} b
$$

Erves

$$
\begin{aligned}
I_{t}\left(\frac{a}{2}, \frac{b}{2}\right) & =\frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{t} \frac{\omega^{\frac{a}{2}-1}}{\left(\frac{a}{b} \omega+1\right)^{\frac{a}{2}+\frac{1}{2}}} d \omega \\
& =P(T<t) \\
& =I_{2(t)}\left(\frac{a}{2}, \frac{b}{2}\right)
\end{aligned}
$$

Thus the F-Distribution CDF is given by

$$
P(T \leqslant t)=I_{2(t)}\left(\frac{a}{2}, \frac{b}{2}\right)
$$

where $I_{2(t)}\left(\frac{a}{a}, \frac{b}{a}\right)$ is the incomplete

Beta function
$I_{z(t)}\left(\frac{a}{a}, \frac{b}{2}\right) \frac{1}{B\left(\frac{a}{a}, \frac{b}{b}\right)} \int_{0}^{z(t)} u^{\frac{a}{2}-1}(1-u)^{\frac{b}{b}-1} d u$
with

$$
z(t)=\frac{a t}{a t+b}
$$

Next the mean is computed.

$$
\begin{aligned}
& E[T]=\int_{0}^{\infty} t f_{T}(t, a, b) d t \\
= & \frac{1}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} t \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}} t^{\frac{a}{2}-1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{1}{2}}} d t \\
= & \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{t^{\frac{a}{2}}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{1}{2}}} d t
\end{aligned}
$$

Consider the change of variables

$$
\begin{aligned}
& u=\frac{a}{b} t \Rightarrow t=\frac{b}{a} u \\
& \Rightarrow d t=\frac{b}{a} d u
\end{aligned}
$$

the integral becomes

$$
\begin{aligned}
& \frac{1}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{\left(\frac{a}{b} t\right)^{\frac{a}{2}}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{b}{2}}} d t \\
& =\frac{1}{B\left(\frac{a}{a}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{u^{\frac{a}{2}}}{(u+1)^{\frac{a}{2}+\frac{1}{2}}} \frac{b}{a} d t \\
& =\frac{\left(\frac{b}{a}\right)}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{u^{\left(\frac{a}{2}+1\right)-1}}{(u+1)^{\left(\frac{a}{2}+1\right)+\left(\frac{b}{2}-1\right)}} d t
\end{aligned}
$$

But

$$
B\left(\frac{a}{2}+1, \frac{b}{2}-1\right)=\int_{0}^{\infty} \frac{u^{\left(\frac{a}{2}-1\right)}}{(u+1)^{\left(\frac{a}{2}+1\right)+\left(\frac{b}{2}-1\right)}} d t
$$

Thus

$$
E[T]=\frac{\left(\frac{b}{a}\right) B\left(\frac{a}{a}+1, \frac{b}{a}-1\right)}{B\left(\frac{a}{a}, \frac{b}{a}\right)}
$$

using the definition of the beta function

$$
\begin{aligned}
& B\left(\frac{a}{2}+1, \frac{b}{2}-1\right)=\frac{\Gamma\left(\frac{a}{2}+1\right) \Gamma\left(\frac{b}{2}-1\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)} \\
& B\left(\frac{a}{2}, \frac{b}{2}\right)=\frac{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)}
\end{aligned}
$$

and Camma function identies that will be wefull,

$$
\begin{aligned}
\Gamma\left(\frac{a}{2}+1\right) & =\frac{a}{2} \Gamma\left(\frac{a}{2}\right) \\
\Gamma\left(\frac{b}{2}\right) & =\Gamma\left(\frac{b}{2}-1+1\right) \\
& =\left(\frac{b}{2}-1\right) \Gamma\left(\frac{b}{2}-1\right)
\end{aligned}
$$

$$
\Rightarrow \Gamma\left(\frac{b}{z}-1\right)=\frac{\Gamma\left(\frac{b}{y}\right)}{\frac{b}{a}-1}
$$

putting things together glos

$$
\begin{aligned}
E[T] & =\frac{\left(\frac{b}{a}\right) B\left(\frac{a}{2}+1, \frac{b}{2}-1\right)}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \\
& =\left(\frac{b}{a}\right) \frac{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)}{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)} \frac{\Gamma\left(\frac{a}{2}+1\right) \Gamma\left(\frac{b}{2}-1\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)} \\
& =\frac{b}{a} \frac{\Gamma\left(\frac{a}{2}+1\right) \Gamma\left(\frac{b}{2}-1\right)}{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)} \\
& =\frac{b}{a} \frac{\frac{a}{2} \Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)}{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)\left(\frac{b}{2}-1\right)} \\
& =\frac{b}{a} \frac{\left(\frac{a}{2}\right)}{\left(\frac{b}{2}-1\right)}=\frac{\frac{1}{2} b}{\frac{1}{2 b-1}} \\
& =\frac{b}{b-2}
\end{aligned}
$$

Thus the mean value is

$$
E[T]=\frac{b}{b-2}
$$

Next the variance of the $t$-statistic is calculted.

$$
\operatorname{Var}(T)=E\left(T^{2}\right)-E(T)^{2}
$$

To complete the calculation $E\left(T^{2}\right)$ is required.

$$
\begin{aligned}
& E\left(T^{2}\right)=\int_{0}^{\infty} t^{2} f_{T}(t, a, b) d t \\
& =\frac{1}{B\left(\frac{a}{a}, \frac{b}{a}\right)} \int_{0}^{\infty} t^{2} \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}} t^{\frac{a}{\partial}-1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{h}{2}}} d t \\
& =\frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}}{B\left(\frac{a}{a}, \frac{b}{\partial}\right)} \int_{0}^{\infty} \frac{t^{\frac{a}{b}+1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{b}{2}}} d t
\end{aligned}
$$

## Consider the change of varables

$$
\begin{aligned}
& u=\frac{a}{b} t \Rightarrow t=\frac{b}{a} u \\
& \Rightarrow d t=\frac{b}{a} d u
\end{aligned}
$$

The integral becomes

$$
\begin{aligned}
& \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{\left(\frac{b}{a} u\right)^{\frac{a}{2}+1}}{(u+1)^{\frac{a}{2}+\frac{b}{2}}}\left(\frac{b}{a}\right) d u \\
= & \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}}\left(\frac{b}{a}\right)^{\frac{a}{2}+2}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{u^{\frac{a}{2}+1}}{(u+1)^{\frac{a}{2}+\frac{b}{2}}} d u \\
= & \frac{\left(\frac{b}{a}\right)^{2}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \int_{0}^{\infty} \frac{u^{\left(\frac{a}{2}+2\right)-1}}{(u+1)^{\left(\frac{a}{2}+2\right)+\left(\frac{b}{2}-2\right)}} d u
\end{aligned}
$$

But

$$
B\left(\frac{a}{2}+2, \frac{b}{2}-2\right)=\int_{0}^{\infty} \frac{u^{\left(\frac{a}{2}+2\right)-1}}{(u+1)^{\left(\frac{a}{2}+2\right)+\left(\frac{b}{2}-2\right)}} d u
$$

Thus

$$
E\left(T^{2}\right)=\frac{\left(\frac{b}{a}\right)^{2}}{B\left(\frac{a}{2}, \frac{b}{2}\right)} B\left(\frac{a}{2}+2, \frac{b}{2}-2\right)
$$

Now

$$
\begin{aligned}
& B\left(\frac{a}{2}, \frac{b}{2}\right)=\frac{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)} \\
& B\left(\frac{a}{2}+2, \frac{b}{2}-2\right)=\frac{\Gamma\left(\frac{a}{2}+2\right) \Gamma\left(\frac{b}{2}-2\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)}
\end{aligned}
$$

and using lamma function identities

$$
\begin{aligned}
\Gamma\left(\frac{a}{2}+2\right) & =\left(\frac{a}{2}+1\right) \Gamma\left(\frac{a}{2}+1\right) \\
& =\left(\frac{a}{2}+1\right)\left(\frac{a}{2}\right) \Gamma\left(\frac{a}{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
\Gamma\left(\frac{b}{2}\right) & =\left(\frac{b}{a}-1\right) \Gamma\left(\frac{b}{2}-1\right) \\
& =\left(\frac{b}{2}-1\right)\left(\frac{b}{2}-2\right) \Gamma\left(\frac{b}{2}-2\right) \\
\Rightarrow \Gamma\left(\frac{b}{2}-2\right) & =\frac{\Gamma\left(\frac{b}{2}\right)}{\left(\frac{b}{2}-1\right)\left(\frac{b}{2}-2\right)}
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
& E\left(T^{2}\right)=\frac{\left(\frac{b}{a}\right)^{2}}{B\left(\frac{a}{2} n\right.}, B\left(\frac{a}{2}+2, \frac{b}{2}-2\right) \\
& =\left(\frac{b}{a}\right)^{2}\left[\begin{array}{l}
\Gamma\left(\frac{a}{2}+\frac{b}{2}\right) \\
\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)
\end{array}\right]\left[\frac{\Gamma\left(\frac{a}{2}+2\right) \Gamma\left(\frac{b}{2}-2\right)}{\Gamma\left(\frac{a}{2}+\frac{b}{2}\right)}\right] \\
& =\left(\frac{b}{a}\right)^{2}\left[\frac{1}{\Gamma\left(\frac{a}{2}\right) \Gamma\left(\frac{b}{2}\right)}\right]\left[\left(\frac{a}{2}+1\right)\left(\frac{a}{2}\right) \Gamma\left(\frac{a}{2}\right)\right] \\
& {\left[\frac{\Gamma\left(\frac{b}{2}\right)}{\left(\frac{b}{2}-1\right)\left(\frac{b}{2}-2\right)}\right]} \\
& =\frac{\left(\frac{b}{a}\right)^{2}\left(\frac{a}{2}+1\right)\left(\frac{a}{2}\right)}{\left(\frac{b}{2}-1\right)\left(\frac{b}{2}-2\right)}
\end{aligned}
$$

$$
\begin{aligned}
& =\left(\frac{b}{a}\right)^{2} \frac{a(a+2)}{(b-2)(b-4)} \\
& =\frac{b^{2}(a+2)}{a(b-2) b-4)}
\end{aligned}
$$

Thus

$$
E\left(T^{2}\right)=\frac{b^{2}(a+2)}{a(b-2)(b-4)}
$$

Previously it was shown

$$
E(T)=\frac{b}{b-2}
$$

Thus

$$
\begin{aligned}
\operatorname{Var}(T) & =E\left(T^{2}\right)-E(T)^{2} \\
& =\frac{b^{2}(a+2)}{a(b-2)(b-4)}-\frac{b^{2}}{(b-2)^{2}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{b^{2}(a+2)(b-2)^{2}-b^{2} a(b-2)(b-4)}{a(b-2)^{3}(b-4)} \\
& =\frac{b^{2}(b-2)[(a+2)(b-2)-a(b-4)]}{a(b-2)^{3}(b-4)} \\
& =\frac{\left.b^{2}(2 a b+2 b-2 a-4-a b+2)^{2} a\right)}{a(b-2)^{2}(b-4)} \\
& =\frac{b^{2}(2 b+2 a-4)}{a(b-2)^{2}(b-4)} \\
& =\frac{2 b^{2}(b+a-2)}{a(b-2)^{2}(b-4)}
\end{aligned}
$$

In summary it has been shown that for the F-Distribution

$$
f(t ; a, b)=\frac{1}{B\left(\frac{a}{2}, \frac{b}{2}\right)} \frac{\left(\frac{a}{b}\right)^{\frac{a}{2}} t^{\frac{a}{2}-1}}{\left(\frac{a}{b} t+1\right)^{\frac{a}{2}+\frac{b}{2}}}
$$

The CDF

$$
\begin{aligned}
P(T \leqslant t ; a, b) & =\int_{0}^{t} f(s ; a, b) d s \\
& =I_{2(t)}\left(\frac{a}{2}, \frac{b}{2}\right)
\end{aligned}
$$

where $I_{2(t)}\left(\frac{9}{2}, \frac{h}{2}\right)$ is the incomplete Beta function
$I_{z(t)}\left(\frac{a}{a}, \frac{b}{2}\right) \frac{1}{B\left(\frac{a}{a}, \frac{b}{a}\right)} \int_{0}^{z(t)} u^{\frac{a}{a}-1}(1-u)^{\frac{b}{b}-1} d u$
with

$$
z(t)=\frac{a t}{a t+b}
$$

and the mean and variance are given by

$$
E(T)=\frac{b}{b-2}
$$

$$
\operatorname{Var}(T)=\frac{2 b^{2}(b+a-2)}{a(b-2)^{2}(b-4)}
$$

The following two pots scan the F-distribution PDF for a range of values of $a$ and b. For the first plot $b=10$ and a scans a range of values between 1 and 100

F-Distibution PDF for Range of Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-524.jpg?height=743&width=1102&top_left_y=1136&top_left_x=231)

The next plot scans the range $a=10$ and $b$ between 1 and 100.

F-Distibution PDF for Range of Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-525.jpg?height=767&width=1150&top_left_y=501&top_left_x=229)

The nexp plots look at the CDF for the same range of values examined on the previous plots.

F-Distibution PDF for Range of Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-526.jpg?height=708&width=1077&top_left_y=181&top_left_x=211)

F-Distibution PDF for Range of Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-526.jpg?height=732&width=1128&top_left_y=1084&top_left_x=213)

## Simulation of F-Distribotion

It this section the results of a simulation of the F-distribution are presented. The simulation consists of multiple trials where two sets of samples are generated in each trial. The distribution of the samples is assumed to Normal(0,1) for both sets. For each trail the two sets of generated samples are used to compute

$$
\begin{aligned}
s_{x}^{2} & =\frac{1}{m-1} \sum_{i=1}^{m} x_{i}^{2} \\
s_{y}^{2} & =\frac{1}{n-1} \sum_{i=1}^{n} y_{i}^{2}
\end{aligned}
$$

and the $t$-statistic is computed using

$$
t=\frac{s_{x}^{2}}{s_{y}^{2}}
$$

The ensemble of $t$ values is then used to estimate the F-Distribution and its mean and variance which are compared with the analytic expression dotainel in the previous sections.

The results of a simumulation of 10,000 trials with $a=100$ and $b=50$ are shown in the plot below are in agreement weth the analysis

Sampled F-Distribution 10000 Trails, $(100,50)$ Degrees of Freedom
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-528.jpg?height=716&width=1084&top_left_y=1215&top_left_x=247)

For the assumed sample sizes of $m=100$ and $n=50$ the distribution mean and cariance are

$$
\begin{gathered}
\mu=\frac{b}{b-2}=1.043 \\
\sigma^{2}=\frac{2 b^{2}(b+a-2)}{a(b-2)^{2}(b-4)}=0.0712
\end{gathered}
$$

The mean and variance computed from the simulation esemble are

$$
\begin{aligned}
& \mu=1.032 \\
& \sigma^{2}=0.0655
\end{aligned}
$$

F-Test Eample
In this section an example $F$-Test calculation is performed.
The example data is

$$
\begin{aligned}
& 93,50,53,92,21,1,2,85,86,22 \\
& 12,11,20,31,65,10,3,9,1,4,12, \\
& 87,43,23,52,49,17,17,14,24
\end{aligned}
$$

The first data set contains 10 values and the second 20 .

The semple variance is given by

$$
\begin{aligned}
& S_{x}^{2}=1385.61 \\
& S_{y}^{2}=521.22
\end{aligned}
$$

the test statistic is

$$
t=\frac{1385, \mathrm{Ge}}{521.22}=2.65
$$

The null hypothesis is given by
$H_{0}$ : The sample variaces are
equal
and the alternative hypothea's is that
$H_{A}$ : The variance of sample
$A$ is larger than the
variance of sample $B$.

If a signifance level of $\alpha=0.05$ is assumed and a right tailed test is performed the critical value is given by

$$
t_{c}=2.425
$$

It follows that since $t>t_{c}$ the null hypothesis is vegected and the hypothesis that the variance of sample I is larger is accepted.

The following plot shows the accetance level and intical $t$-volve.

F-Distibution CDF, Number of Degrees of Freedom: 9, 19
![](https://cdn.mathpix.com/cropped/2025_09_20_986f549f0033fe8bfbdbg-532.jpg?height=765&width=1294&top_left_y=487&top_left_x=135)

The p-value of the $t$-statistic is

$$
P(2.65)=0.035
$$

Thus the probability of obtaining a value at least as large a $t$ is 6.035 which is about 1 in 30.

It should be noted that if the accetance level were 6.025 the critical value would by

$$
t_{c}=2.88
$$

which is greater than $t=2.66$ so the null mypothesis wand be accepted and the sample bariances would be assumed statically equal.

