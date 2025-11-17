The Volatility Surface

> Troy Stribling
> Nov. 7, 2021

## One-Dimensional Diffusion Process

This book asswmes knowledge of diflusion processes here one-dimensional processe are reviewed.
Consider the stochastic differential equation.

$$
d s_{t}=\mu\left(s_{t}, t\right) d t+\sigma\left(s_{t}, t\right) d \omega_{t}
$$

and the function $V\left(s_{t}, t\right)$ where

$$
z_{u}=e^{-S_{t}^{u} r(v) d v} v\left(S_{u}, u\right)
$$

Recall the Itô formula

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
& t=u \\
& \bar{x}(u)=s_{u} \\
& a(u)=u(u) \\
& b(u)=\sigma(u) \\
& F(u, \bar{x}(u))=z_{u}
\end{aligned}
$$

To roduce writing let

$$
\begin{aligned}
g(u)=e^{-s_{t}^{u} r(v) d v} \\
F_{u}=\frac{\partial}{\partial u}\left[g(u) v\left(u, s_{u}\right)\right] \\
=\frac{g \frac{\partial v}{\partial u}+v \frac{\partial g}{\partial u}}{F_{x}}=\frac{\partial}{\partial s_{u}}\left[g(u) v\left(u, s_{u}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =g(u) \frac{\partial v}{\partial s_{u}} \\
F_{x x} & =\frac{\partial^{2}}{\partial s_{u}^{2}}\left[g(u) v\left(u, s_{u}\right)\right] \\
& =\frac{\partial}{\partial s_{u}}\left[g(u) \frac{\partial v}{\partial s_{u}}\right] \\
& =g(u) \frac{\partial^{2} v}{\partial s_{u}^{2}}
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
& d z_{u}=\left(g \frac{\partial v}{\partial u}+v \frac{\partial g}{\partial u}\right) d u \\
& +u(u) g(u) \frac{\partial v}{\partial S_{u}} d u \\
& +\sigma(u) g(u) \frac{\partial v}{\partial S_{u}} d d w_{u}
\end{aligned}
$$

$$
\begin{aligned}
& +\frac{1}{2} \sigma^{2}(u) g(u) \frac{\partial^{2} v}{\partial S_{u}^{2}} d u \\
& =\left[g \frac{\partial v}{\partial u}+v \frac{\partial g}{\partial u}+u g \frac{\partial v}{\partial S_{u}}\right. \\
& \left.+\frac{1}{2} \sigma^{2} g \frac{\partial^{2} v}{\partial S_{u}^{2}}\right] d u \\
& +\sigma g \frac{\partial v}{\partial S_{u}} d S_{u}
\end{aligned}
$$

Now

$$
d s_{u}=\mu d u+o d \omega_{u}
$$

and

$$
\begin{aligned}
\frac{\partial g}{\partial u} & =\frac{\partial}{\partial u}\left(e^{-S_{t}^{u} r(v) d v}\right) \\
& =-r(u) e^{-S_{t}^{u} r(v) d v} \\
& =-r g
\end{aligned}
$$

$$
\begin{aligned}
& \Delta z_{u}=( \\
& \underline{g} \frac{\partial v}{\partial u}-r g v+\mu g \frac{\partial v}{\partial s_{u}} \\
&\left.+\frac{1}{2 \sigma^{2}} g \frac{\partial^{2} v}{\partial s^{2} u}\right) d u \\
&+\sigma g \frac{\partial v}{\partial s_{u}} d \omega_{u} \\
&=\left(g \frac{\partial v}{\partial u}-r g v+\mu g \frac{\partial v}{\partial s_{u}}+\frac{1}{2} \sigma^{2} g \frac{\partial^{2} v}{\partial s^{2} u}\right) d u \\
&+\sigma g \frac{\partial v}{\partial s_{u}} d \omega_{u} \\
&=g\left(\frac{\partial v}{\partial u}+\mu \frac{\partial v}{\partial s_{u}}+\frac{1}{2} \sigma^{2} \frac{\partial^{2} v}{\partial s_{u}^{2}}-r v\right) d u \\
&+\sigma g \frac{\partial v}{\partial s_{u}} d \omega_{u}
\end{aligned}
$$

$$
\begin{aligned}
d z_{u}=g & \left(\frac{\partial v}{\partial u}+u \frac{\partial v}{\partial s_{u}}+\frac{1}{2} \sigma^{2} \frac{\partial^{2} v}{\partial s_{u}^{2}}-r v\right) d u \\
& +\sigma g \frac{\partial v}{\partial s_{u}} d \omega_{u}
\end{aligned}
$$

Now if

$$
\frac{\partial v}{\partial u}+u \frac{\partial v}{\partial S_{u}}+\frac{1}{2} \sigma^{2} \frac{\partial^{2} v}{\partial S_{u}^{2}}-r v=0
$$

then

$$
d z_{u}=g(u) \sigma\left(S_{u}, u\right) \frac{\partial V}{\partial S_{u}} d \omega_{u}
$$

Integrating gives

$$
\int_{t}^{\top} d z_{u}=\int_{t}^{\top} g(u) \sigma(S u, u) \frac{\partial v}{\partial S_{u}} d \omega_{u}
$$

$$
\Rightarrow z_{T}-z_{t}=\int_{t}^{T} g(u) \sigma(S u, u) \frac{\partial v}{\partial S_{u}} d w_{u}
$$

The right-hand side is an Its integral which has expectation zero. It follows that

$$
\begin{aligned}
& E\left[z_{T}-z_{t}\right]=0 \\
\Rightarrow & E\left[z_{T}\right]=E\left[z_{t}\right]
\end{aligned}
$$

An Itô intergral is a Martingale so

$$
E\left[z_{T} \mid \mathcal{F}_{t}\right]=z_{t}
$$

where $\mathcal{F}_{t}$ is the weiner process filtration.

Now

$$
Z_{u}=e^{-S_{t}^{u} r(v) d v} v\left(S_{u}, u\right)
$$

$$
\begin{aligned}
z_{t} & =e^{\int_{t}^{t} r(v) d v} V\left(s_{t}, t\right) \\
& =V\left(s_{t}, t\right)
\end{aligned}
$$

and

$$
Z_{T}=e^{-S_{t}^{\top} r(v) d v} v\left(S_{T}, T\right)
$$

It follows that

$$
\begin{aligned}
& E\left[z_{T} \mid \mathcal{F}_{t}\right]=z_{t} \\
= & E\left[e^{-S_{t}^{T} r(v) d v} v\left(S_{T}, T\right) \mid \mathcal{F}_{t}\right]=v\left(S_{t}, t\right)
\end{aligned}
$$

let $\Psi(T)=V\left(S_{T}, T\right)$ so
$V\left(S_{t}, t\right)=E\left[e^{-S_{t}^{T} r(v) d v} \psi(T) \mid \mathcal{F}_{t}\right]$

## This expression is called the Feyman-Kac formula.

## Backward Kolmogorv Equation

Let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a wiener process on the probability space $(\Omega, \mathcal{F}, \mathbb{P})$. For $t \in[0, T], T>0$ consider the SDE

$$
d \bar{X}_{t}=\mu\left(\bar{X}_{t}, t\right) d t+\sigma\left(\bar{X}_{t}, t\right) d \omega_{t}
$$

By conditioning on $X_{t}=X$ and $Z_{T}=y$ let $p(x, t: y, T)$ be the transition probability of $\bar{x}_{T}$ at time $T$ starting from $I_{t}$ at $t$.
For any $\Psi(T)$ from the Feymannkac formula the function,

$$
\begin{aligned}
f(x, t) & =E\left[e^{-\int_{t}^{\top} r(u) d u} \Psi(\tau) \mid \mathcal{F}_{t}\right] \\
& =e^{-\int_{t}^{\top} r(u) d u} \int \Psi(y) p(x, t: y, T) d y
\end{aligned}
$$

satisfies the partial differential equation
$\frac{\partial f}{\partial t}+\frac{1}{2} \sigma^{2}(x, t) \frac{\partial^{2} f}{\partial x^{2}}+\mu(x, t) \frac{\partial f}{\partial x}-r(t) f=0$

It will be shown that

$$
\begin{gathered}
\frac{\partial}{\partial t} p(x, t: y, T)+\frac{1}{2} \sigma^{2}(x, t) \frac{\partial^{2}}{\partial x^{2}} p(x, t: y, T) \\
+\mu(x, t) \frac{\partial}{\partial x} p(x, t: y, T)=0
\end{gathered}
$$

## Solution

First it will be shown that

$$
\begin{aligned}
& f(x, t)=e^{-S_{t}^{\top} r(u) d u} \\
& \int \Psi(y) p(x, t: y, T) d y
\end{aligned}
$$

satisfies

$$
\frac{\partial f}{\partial t}+\frac{1}{2} \sigma^{2}(x, t) \frac{\partial^{2} f}{\partial x^{2}}+\mu(x, t) \frac{\partial f}{\partial x}-r(t) f=0
$$

The three derijatives must be evaluated,

$$
\begin{aligned}
& \frac{\partial f}{\partial t}=\frac{\partial}{\partial t}\left\{e^{-S_{t}^{\top} r(u) d u}\right. \\
&\left.\int \Psi(y) p(x, t: y, T) d y\right\} \\
&=r(t) e^{-S_{t}^{\top} r(u) d u} \int \Psi(y) p(x, t ; y, T) d y \\
&+ e^{-S_{t}^{\top} r(u) d u} \int \Psi(y) \frac{\partial p(x, t ; y, T) d y}{\partial t} \\
&=r(t) f(x, y)+e^{-S_{t}^{\top} r(u) d u} \\
& \int \Psi(y) \frac{\partial p(x, t ; y, T) d y}{\partial t}
\end{aligned}
$$

$$
\begin{aligned}
& \frac{\partial f}{\partial x}=\frac{\partial}{\partial x}\left\{e^{-\int_{t}^{\top} r(u) d u}\right. \\
&\left.\int \Psi(y) p(x, t: y, T) d y\right\} \\
&= e^{-\int_{t}^{\top} r(u) d u} \int \Psi(y) \frac{\partial p}{\partial x}\left(x, t: y_{1} T\right) d y \\
& \frac{\partial^{2} f}{\partial x^{2}}=e^{-\int_{t}^{\top} r(u) d u} \int \Psi(y) \frac{\partial^{2} p}{\partial x^{2}}\left(x, t: y_{1} T\right) d y
\end{aligned}
$$

substituting into the above equation gives

$$
\begin{gathered}
\frac{\partial f}{\partial t}+\frac{1}{2} \sigma^{2}(x, t) \frac{\partial^{2} f}{\partial x^{2}}+\mu(x, t) \frac{\partial f}{\partial x} \\
-r(t) f=0
\end{gathered}
$$

$$
\begin{aligned}
& =r(t) \frac{f(x, y)}{\int \Psi(y)}+e^{-\int_{t}^{T} r(u) d u} \\
& \frac{\partial p(x, t ; y, T) d y}{\partial t} \\
& +\frac{1}{2} \sigma^{2} e^{-\int_{t}^{T} r(u) d u} \int \Psi(y) \frac{\partial^{2} p}{\partial x^{2}}(x, t: y, T) d y \\
& +\mu e^{-\int_{t}^{T} r(u) d u} \int \Psi(y) \frac{\partial p}{\partial x}(x, t: y, T) d y \\
& -r(t) f(x, y) \\
& =e^{-\int_{t}^{T} r(u) d u}\left\{\int \Psi(y) \frac{\partial p}{\partial t}(x, t ; y, T) d y\right. \\
& +\frac{1}{2} \sigma^{2} e^{-\int_{t}^{T} r(u) d u} \int \Psi(y) \frac{\partial^{2} p}{\partial x^{2}}(x, t: y, T) d y \\
& \left.+\mu e^{-\int_{t}^{T} r(u) d u} \int \Psi(y) \frac{\partial p}{\partial x}(x, t: y, T) d y\right\}
\end{aligned}
$$

$$
\begin{aligned}
& =e^{-\int_{t}^{\top} r(u) d u} \int \Psi(y)\left\{\frac{\partial p}{\partial t}(x, t ; y, T)\right. \\
& \left.+\frac{1}{2} \sigma \frac{\partial^{2} p}{\partial x^{2}}(x, t: y, T)+\mu \frac{\partial p}{\partial x}(x, t: y, T)\right\} d y \\
& =0
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \frac{\partial p}{\partial t}(x, t ; y, T)+\frac{1}{2} \sigma \frac{\partial^{2} p}{\partial x^{2}}(x, t ; y, T) \\
& +\mu \frac{\partial p}{\partial x}(x, t: y, T)=0
\end{aligned}
$$

which is the desided result.

## Forward Kolmogorov Equation

Let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process on the probability space $(\Omega, \mathcal{F}, \mathbb{P})$. For $t \in[0, T], T>0$ consider the generalized stachastic differential equation,

$$
d \bar{x}_{t}=\mu\left(\bar{x}_{t}, t\right) d t+\sigma\left(\bar{x}_{t}, t\right) d \omega_{t}
$$

and the function $f\left(\bar{x}_{t}\right)$. The Itố formula is given by,

$$
\begin{aligned}
d f & =\left(\frac{1}{2} \delta^{2}\left(x_{t}, t\right) \frac{\partial^{2} f}{\partial x_{t}^{2}}\right) d t+\frac{\partial f}{\partial x} d x \\
& =\left(\frac{\partial f}{\partial t}+\frac{1}{2} \frac{\partial^{2} f}{\partial x_{t}^{2}}\right) d t \\
& +\frac{\partial f}{\partial x_{t}}\left[\mu\left(x_{t}, t\right) d t+\sigma\left(x_{t}, t\right) d \omega_{t}\right]
\end{aligned}
$$

$$
\begin{gathered}
=\left[\frac{1}{2} \delta^{2}\left(x_{t}, t\right) \frac{\partial^{2} f}{\partial x_{t}^{2}}+\mu\left(x_{t}, t\right) \frac{\partial f}{\partial x_{t}}\right] d t \\
+\sigma\left(x_{t}, t\right) \frac{\partial f}{\partial x_{t}} d \omega_{t}
\end{gathered}
$$

Now by conditioning on $\mathbb{Z}_{t}=x$ and $Z_{T}=y$ let $p(x, t: y, T)$ be the transition probability of $\bar{X}_{T}$ at time $T$ starting from $I_{\text {t }}$ at $t$.
The conditional expectatation for $x_{t}=x$ of $f(y)$ is given by

$$
\begin{aligned}
& E\left[f(y) \mid \bar{X}_{t}=x\right] \\
& \quad=\int_{-\infty}^{\infty} f(y) p(x, t \mid y, T) d y
\end{aligned}
$$

Taking expectation of the equation for $d f(y)$ gives
$E\left[d f(y) \mid \bar{x}_{t}=x\right]$
$=E\left[\left.\left(\frac{1}{2} \delta^{2}(y, T) \frac{\partial^{2} f}{\partial y^{2}}+\mu(y, T) \frac{\partial f}{\partial y}\right) d t \right\rvert\, Z_{t}=x\right]$

$$
+E\left[\left.\sigma(y, T) \frac{\partial f}{\partial y} d \omega_{T} \right\rvert\, \underline{Z}_{t}=x\right]
$$

Dow, if it is assumed that

$$
E\left[\int_{0}^{T}\left(\delta(y, s) \frac{\partial f}{\partial y}\right)^{2} d s\right]<\infty
$$

then the expectation is a martingale, so

$$
E\left[\left.\sigma(y, T) \frac{\partial f}{\partial y} d \omega_{t} \right\rvert\, Z_{t}=x\right]=0
$$

then

$$
\begin{aligned}
& E\left[d f(y) \mid E_{t}=x\right] \\
& =E\left[\left.\left(\frac{1}{2} \delta^{2}(y, T) \frac{\partial^{2} f}{\partial y^{2}}+\mu(y ; T) \frac{\partial f}{\partial y}\right) d t \right\rvert\, Z_{t}=x\right] \\
& =E\left[\left.\left(\frac{1}{2} \delta^{2}(y, T) \frac{\partial^{2} f}{\partial y^{2}}+\mu(y, T) \frac{\partial f}{\partial y}\right) \right\rvert\, Z_{t}=x\right] d T \\
& \Rightarrow \frac{\partial}{\partial t} E\left[f(y) \mid \bar{X}_{t}=x\right] \\
& =E\left[\left.\left(\frac{1}{2} \delta^{2}(y, T) \frac{\partial^{2} f}{\partial y^{2}}+\mu(y, T) \frac{\partial f}{\partial y}\right) \right\rvert\, Z_{t}=x\right]
\end{aligned}
$$

The last step can be shown to be a consequence of the Dominated Convergance Theorem. Now evaluating the integrals Sives

$$
\begin{aligned}
& \frac{\partial}{\partial T} \int_{-\infty}^{\infty} f(y) p(x, t \mid y, T) d y \\
= & \int_{-\infty}^{\infty}\left(\frac{1}{2} \sigma^{2}(y, T) \frac{\partial^{2} f(y)}{\partial y^{2}}+\mu(y ; T) \frac{\partial f}{\partial y}(y)\right) \\
& p(x, t \mid y, T) d y
\end{aligned}
$$

For the left hand side

$$
\begin{aligned}
& \frac{\partial}{\partial T} \int_{-\infty}^{\infty} f(y) p(x, t \mid y, T) d y \\
& \quad=\int_{-\infty}^{\infty} f(y) \frac{\partial}{\partial T} p(x, t \mid y, T) d y
\end{aligned}
$$

and the second term on the righthand side can be easluated using integration by parts.

$$
\int u d v=u v-\int v d u
$$

$$
\int_{-\infty}^{\infty} \mu(y, T) \frac{\partial f}{\partial y}(y) p(x, t \mid y, T) d y
$$

here

$$
\begin{aligned}
d v & =\frac{\partial f}{\partial y}(y) d y \quad v=f(y) \\
u & =\mu(y, T) p\left(x,\left.t\right|_{y}, T\right) \\
d u & =\frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] d y
\end{aligned}
$$

56

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \mu(y, T) \frac{\partial f}{\partial y} p(x, t \mid y, T) d y \\
& =\left.f(y) \mu(y, T) p(x, t \mid y, T)\right|_{-\infty} ^{\infty} \\
& -\int_{-\infty}^{\infty} f(y) \frac{\partial}{\partial y}[\mu(y, T) p(x t \mid y T)]_{d y}
\end{aligned}
$$

Now $p(x, t \mid y, T) \rightarrow 0$ as $y^{\rightarrow \infty}$ and $y^{\rightarrow-\infty}$ so the first term vanishes. Thus

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \mu(y, T) \frac{\partial f}{\partial y} p(x, t \mid y, T) d y \\
& =-\int_{-\infty}^{\infty} f(y) \frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] d y
\end{aligned}
$$

For the second term

$$
\int_{-\infty}^{4} \frac{1}{2} \delta^{2}(y, t) \frac{\partial^{2} f(y)}{\partial y^{2}} p(x, t \mid y, T) d y
$$

So,

$$
\begin{aligned}
& d v=\frac{\partial^{2} f(y) d y}{\partial y^{2}} \quad v=\frac{\partial f(y)}{\partial y} \\
& u=\frac{1}{2} \sigma^{2}(y, T) p(x, t / y, T)
\end{aligned}
$$

$$
d u=\frac{1}{2} \frac{\partial}{\partial y}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]
$$

50

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \frac{1}{2} \sigma^{2}(y, T) \frac{\partial^{2} f(y)}{\partial y^{2}} p(x, t \mid y, T) d y \\
& =\left.\frac{\partial f(y)}{\partial y}\left(\frac{1}{\partial} \sigma^{2}(y, T) p(x, t \mid y, T)\right)\right|_{-\infty} ^{\infty} \\
& -\int_{-\infty}^{\infty} \frac{\partial f(y)}{\partial y} \frac{\partial\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y}{\partial y} \\
& =-\frac{1}{2} \int_{-\infty}^{\infty} \frac{\partial f(y)}{\partial y} \frac{\partial\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y}{\partial y}
\end{aligned}
$$

Integrating one more time gives

$$
d v=\frac{\partial f(y) d y}{\partial y} \quad v=f(y)
$$

$$
\begin{gathered}
u=\frac{\partial\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]}{\partial y} \\
d u=\frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y \\
-\int_{-\alpha}^{\infty} \frac{1}{\partial} \frac{\partial f(y)}{\partial y} \frac{\partial\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y}{\partial y} \\
=-\frac{f(y)}{\partial} \frac{\left.\partial\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]\right|_{-\alpha} ^{\infty}}{\partial y} \\
+\frac{1}{\partial} \int_{-\alpha}^{\infty} f(y) \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y
\end{gathered}
$$

bringing things together gres,

$$
\int_{-\infty}^{A} f(y) \frac{\partial}{\partial t} p(x, t \mid y, T) d y
$$

$$
\begin{aligned}
= & -\int_{-\infty}^{\infty} f(y) \frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] d y \\
+ & \frac{1}{2} \int_{-\infty}^{\infty} f(y) \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right] d y \\
\Rightarrow \int_{-\infty}^{\infty} f(y) & \left\{\frac{\partial}{\partial t} p(x, t \mid y, T)\right. \\
+ & \frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] \\
- & \left.\frac{1}{2} \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]\right\} d y \\
= & 0
\end{aligned}
$$

This relation must be true for any function $f(y)$ it must be that

$$
\begin{gathered}
\frac{\partial}{\partial T} p(x, t \mid y, T)+\frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] \\
-\frac{1}{\partial} \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]=0
\end{gathered}
$$

which is the desired result. This is also the Fokker-Planck equation from physics statistical mechanics.
In summary, for a stachaste random variable

$$
d \bar{x}_{t}=\mu\left(\bar{x}_{t}, t\right) d t+\sigma\left(\bar{x}_{t}, t\right) d \omega_{t}
$$

and the function $f\left(x_{t}\right)$ has conditional expectation,

$$
\begin{aligned}
& E\left[f(y) \mid \bar{X}_{t}=x\right] \\
& \quad=\int_{-\infty}^{\infty} f(y) p(x, t \mid y, T) d y
\end{aligned}
$$

where $P(x, t: y, T)$ is the transition probability of $\Sigma_{T}$ at time $T$ starting from $Z_{t}$ at $t$.
The distribution, $P(x, t: y, T)$, satisfies the equation,

$$
\begin{gathered}
\frac{\partial}{\partial T} p(x, t \mid y, T)+\frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] \\
-\frac{1}{\partial} \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]=0
\end{gathered}
$$

It can be shown that the same equation holds for more general functions of the form $f(y, T)$.

## Stochastic Volatility and local volutility

In this section the ideas of stochastic and local volatility are discussed.
stochastic volatility arises from randomness and local oodatility, will be shown to be the conditional expectation of the instantanedus variance. lesing these ideas when computing option prices the volatility can be considered deterministic instead of stochastic

## Stochastic volatility

Consider the following stochastic differential equations,

Where $s$ is the asset price and $v$ is the variance

$$
\begin{gathered}
d S_{t}=\mu_{t} S_{t} d t+\sqrt{v_{t}} S_{t} d z_{1} \\
d v=\alpha\left(S_{t}, v_{t}, t\right) d t+\eta \beta\left(S_{t}, v_{t}, t\right) \sqrt{v_{t}} d z_{2} \\
\left\langle d z_{1} d z_{2}\right\rangle=e d t
\end{gathered}
$$

$z_{1}$ and $z_{2}$ are weiner processes, $\mu_{t}$ is the drift of the asset price, $\eta$ is the volatility of the volatility, $e$ is the correlation between random asset prices and changes in variance.

The asset price $S_{t}$ is given by the Black-sholes molel.
The Black-sholes model is recovered in the limit $\eta \rightarrow 0$.
The parameters $\alpha$ and $\beta$ have no assumptions on

## their functional forms.

In the Black-sholes model only $s_{t}$ needs to be hedged. In this model both $s_{t}$ and $v_{t}$ require hedging.
A hedging strategy can be constructed for an optor with price, $V(s, v, t)$, by considering the portfolio,

$$
\pi=V-\Delta S-\Delta_{1} V_{1}
$$

here $-\Delta$ is the quantity of stock ownend and - $\Delta$, is the quanity of $V$, owned.
Recall that the portfolio used to construct the delta hedging strategl,

$$
V=x S+y A-C
$$

Here $V$ is the portfolio
value, $C$ is the eption price, $S$ is the asset price, $x$ is the quantuly of the asset owned, $A$ is the risk-free investment and $y$ is the quentity of this asset In this portfolio the awner is on the stort side of the option, is the seller

In the volatility model the risk-free asset is replaced by the volatility.

## show that

$$
\begin{aligned}
d \pi= & \left\{\frac{\partial v}{\partial t}+\frac{1}{\partial} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+e \eta v \beta s \frac{\partial^{2} v}{\partial s^{2}}\right\} d t \\
& -\Delta_{1}\left\{\frac{\partial V_{1}}{\partial t}+\frac{1}{\partial} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+e \eta v \beta s \frac{\partial^{2} v}{\partial s^{2}}\right\} d t \\
& -\left\{\frac{\partial v}{\partial s}-\Delta_{1} \frac{\partial v}{\partial s}-\Delta\right\} d s
\end{aligned}
$$

$$
+\left\{\frac{\partial v}{\partial v}-\Delta_{1} \frac{\partial v}{\partial v}\right\} d v
$$

## Solution

solving this problem requires the itô formula for two random variables. The ttó formula for $n$ randam variables for the function,

$$
f\left(s_{1}(t), s_{2}(t), \ldots, s_{n}(t), t\right)
$$

where

$$
d S_{i}(t)=a_{i}(t) d t+b(t) d z(t)
$$

and $\omega_{i}(t)$ are standard wiener processes satisfying

$$
\begin{gathered}
e_{i j} \in[-1,1] \quad i \neq j \\
e_{i i}=1
\end{gathered}
$$

where $e_{i j}$ is the correlation

## coefficient between $\omega_{i}(t)$ and $\omega_{j}(t)$

The ㅍtô formula is given by

$$
\begin{array}{r}
d f\left(s_{1}(t), s_{2}(t), \ldots, s_{n}(t), t\right) \\
=\frac{\partial f}{\partial t} d t+\sum_{i=1}^{n} a_{i} \frac{\partial f}{\partial s_{i}} d t \\
+\frac{1}{\partial} \sum_{i=1}^{n} \sum_{j-1}^{n} \rho_{i j} b_{i}^{2} \frac{\partial^{2} f}{\partial s_{i} \partial s_{j}} d t \\
+\sum_{i=1}^{n} b_{i} \frac{\partial f}{\partial s_{i}} d z_{i}(t) \\
\text { For } n=2 \text { with } \\
e_{12}=e \\
f\left(s_{1}, s_{2}, t\right)=f(x, y, t)
\end{array}
$$

$$
\begin{aligned}
& d f(x, y, t)=\frac{\partial f}{\partial t} d t+a_{1} \frac{\partial f}{\partial x} d t \\
& +a_{2} \frac{\partial f}{\partial y} d t+\frac{1}{2} b_{1}^{2} \frac{\partial^{2} f}{\partial x^{2}} d t \\
& +\frac{1}{2} b_{2}^{2} \frac{\partial^{2} f}{\partial y^{2}} d t+e b_{1} b_{2} \frac{\partial^{2} f}{\partial x \partial y} d t \\
& +b_{1} \frac{\partial f}{\partial x} d z_{1}+b_{2} \frac{\partial f}{\partial y} d z_{2} \\
& =\frac{\partial f}{\partial t} d t+\left[a_{1} \frac{\partial f}{\partial x}+a_{2} \frac{\partial f}{\partial y}\right. \\
& +\frac{1}{2} b_{1}^{2} \frac{\partial^{2} f}{\partial x^{2}}+\frac{1}{2} b_{2}^{2} \frac{\partial^{2} f}{\partial y} \\
& \left.+e b_{1} b_{2} \frac{\partial^{2} f}{\partial x \partial y}\right] d t+b_{1} \frac{\partial f}{\partial x} d z_{1} \\
& +b_{2} \frac{\partial f}{\partial y} d z_{2}
\end{aligned}
$$

Now here

$$
\pi=V-\Delta S-\Delta_{1} V_{1}
$$

and the equivalent of the self finacing assumption is

$$
\begin{gathered}
d \pi=d V-\Delta d S-\Delta_{1} d V_{1} \\
x=S \quad y=v
\end{gathered}
$$

and

$$
\begin{aligned}
& v=v(s, v, t) \\
& v_{1}=v_{1}(s, v, t)
\end{aligned}
$$

Also,

$$
\begin{aligned}
& d s(t)=\mu(t) s(t) d t+\sqrt{v(t)} s(t) d z_{1} \\
& d v(t)=\alpha(s, v, t) d t+\eta \beta(s, v, t) \sqrt{v(t)} d z_{2}
\end{aligned}
$$

assume that $S(t)$ and
$v(t)$ do not have explict dependence on $t$ so that

$$
\mu=0 \quad \alpha=0
$$

It follows that

$$
\begin{aligned}
& d s=\sqrt{v} s d z_{1} \\
& d v=\eta \beta \sqrt{v} d z_{2}
\end{aligned}
$$

comparing with the Itô formula
gives

$$
b_{1}=\sqrt{v} S \quad b_{2}=\eta \beta \sqrt{v}
$$

Now since

$$
d \pi=d V-\Delta d S-\Delta_{1} d V_{1}
$$

dII will be computed by using the Itô formula for $d v(s, v, t)$ and $d v_{1}\left(s_{1}, v, t\right)$

First consider $d V$

$$
\begin{aligned}
d v= & \frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
+ & \left.\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s} \eta \beta \frac{\partial^{2} v}{\partial s \partial v}\right] d t \\
& \sqrt{v} S \frac{\partial v}{\partial s} d z_{1}+\eta \beta \sqrt{v} \frac{\partial v}{\partial v} d z_{z}
\end{aligned}
$$

but

$$
\begin{aligned}
& d s=\sqrt{U} s d z_{1} \\
& d v=\eta \beta \sqrt{v} d z_{2}
\end{aligned}
$$

So

$$
\begin{aligned}
& d v=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v S^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s} \eta \beta \frac{\partial^{2} v}{\partial s \partial v}\right] d t
\end{aligned}
$$

$$
+\frac{\partial v}{\partial s} d s+\frac{\partial v}{\partial v} d v
$$

Similarly,

$$
\begin{aligned}
& d v_{1}=\frac{\partial v_{1}}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v_{1}}{\partial v^{2}}+e^{v s \eta \beta} \frac{\partial^{2} v_{1}}{\partial s \partial v}\right] d t \\
& +\frac{\partial v_{1}}{\partial s} d s+\frac{\partial v_{1}}{\partial v} d v
\end{aligned}
$$

Bringins things together gives the desired result

$$
\begin{aligned}
& d \pi=d v-\Delta d s-\Delta_{1} d v_{1} \\
&=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
&\left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s} \eta \beta \frac{\partial^{2} v}{\partial s \partial v}\right] d t
\end{aligned}
$$

$$
\begin{aligned}
& +\frac{\partial v}{\partial s} d s+\frac{\partial v}{\partial v} d v-\Delta d s \\
& -\Delta_{1}\left\{\frac{\partial v_{1}}{\partial t}+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}}\right.\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v_{1}}{\partial v^{2}}+e^{v} s_{\eta} \beta \frac{\partial^{2} v_{1}}{\partial s \partial v}\right] d t \\
& \left.+\frac{\partial v_{1}}{\partial s} d s+\frac{\partial v_{1}}{\partial v} d v\right\}
\end{aligned}
$$

Gathering terms gives the
final result.

$$
\begin{aligned}
\Rightarrow & d \pi=\left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& +\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{\left.v s \eta \beta \frac{\partial^{2} v}{\partial s \partial v}\right\} d t} \\
-\Delta & \frac{\left\{\frac{\partial v_{1}}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right.}{} \\
& \left.+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}\right\} d t \\
& +\left\{\frac{\partial v}{\partial s}-\Delta_{1} \frac{\partial v_{1}}{\partial s}-\Delta\right\} d s \\
& +\left\{\frac{\partial v}{\partial v}-\Delta_{1} \frac{\partial v_{1}}{\partial v}\right\} d v
\end{aligned}
$$

The portfolio can be made risk-free for a given $t$ if the random differential components are eliminated. It is said that
this makes the portfolio instataneously risk-frce. This means that for time $t$ the differential is deterministic since the random differential terms are zero.

To accomplish this it must be that

$$
\begin{aligned}
& \frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}-\Delta=0 \\
& \frac{\partial V}{\partial U}-\Delta_{1} \frac{\partial V_{1}}{\partial U}=0
\end{aligned}
$$

The first equation eliminates the ds term and the second the $d v$ term.

It follows that

$$
d \pi=\left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right.
$$

$$
\begin{aligned}
+ & \left.\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s} \eta \beta \frac{\partial^{2} v}{\partial s \partial v}\right\} d t \\
-\Delta_{1} & \left\{\frac{\partial v_{1}}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& +e^{\left.v \sin \beta \frac{\partial^{2} v}{\partial s \partial v}\right\} d t}
\end{aligned}
$$

If the return is risk-free it increases at the risk-free rate of return, $r$, which is assumed deterministic, so

$$
\begin{aligned}
d \pi & =r \pi d t=r\left(v \cdot \Delta s-\Delta_{1} v_{1}\right) d t \\
& =\left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
+ & \left.\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}\right\} d t
\end{aligned}
$$

$$
\begin{aligned}
-\Delta_{1} & \left\{\frac{\partial V_{1}}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} V_{1}}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} V_{1}}{\partial v^{2}}\right. \\
+ & \left.e^{v} \sin \beta \frac{\partial^{2} V_{1}}{\partial s \partial v}\right\} d t
\end{aligned}
$$

$\Delta$ and $\Delta_{1}$ can be determined from the following relations,

$$
\begin{aligned}
& \frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}-\Delta=0 \\
& \frac{\partial V}{\partial U}-\Delta_{1} \frac{\partial V_{1}}{\partial U}=0
\end{aligned}
$$

From the second equation

$$
\Delta_{1}=\frac{\frac{\partial v}{\partial u}}{\frac{\partial v_{i}}{\partial u}}
$$

inserting this into the second equation gives

$$
\begin{aligned}
& \frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}-\Delta=0 \\
\Rightarrow & \Delta=\frac{\partial V}{\partial S}-\frac{\partial V}{\frac{\partial V}{\partial U}} \frac{\partial V_{1}}{\partial S}
\end{aligned}
$$

So,

$$
\Delta=\frac{\partial V}{\partial S}-\frac{\frac{\partial V}{\partial U}}{\frac{\partial V}{\partial U}} \frac{\partial V_{1}}{\partial S}
$$

$$
\Delta_{1}=\frac{\frac{\partial V}{\partial U}}{\frac{\partial V_{i}}{\partial U}}
$$

Now returning to the expression for $d \pi$

$$
\begin{aligned}
d \pi= & r \pi d t=r\left(v-\Delta s-\Delta_{1} v_{1}\right) d t \\
= & \left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
+ & \left.\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}\right\} d t \\
-\Delta_{1} & \left\{\frac{\partial v_{1}}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& +e^{\left.v \sin \beta \frac{\partial^{2} v}{\partial s \partial v}\right\} d t}
\end{aligned}
$$

Consider the as term

$$
\Delta S=\left[\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}\right] S
$$

Collecting $V$ terms on the left and $v$, on the right gives after substiting the above expression gives

$$
\begin{aligned}
& \left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
+ & \frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}-r v \\
+ & \left.r \frac{\partial v}{\partial s} s\right\} d t \\
= & \Delta_{1}\left\{\frac{\partial v_{1}}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& \left.+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}-r v_{1}+r s \frac{\partial v_{1}}{\partial s}\right\} d t
\end{aligned}
$$

using

$$
\Delta_{1}=\frac{\frac{\partial V}{\partial U}}{\frac{\partial V_{1}}{\partial U}}
$$

and cleaning up gives

$$
\begin{aligned}
\frac{1}{\partial v} & \left\{\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& \left.+e^{v s \eta \beta} \frac{\partial^{2} v}{\partial s \partial v}-r v+r \frac{\partial v}{\partial s} s\right\} \\
= & \frac{1}{\partial v_{1}}\left\{\frac{\partial v_{1}}{\partial v}+\frac{1}{2} v s^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& \left.+e^{v s \eta \beta \frac{\partial^{2} v}{\partial s \partial v}-r v_{1}}+r s \frac{\partial v_{1}}{\partial s}\right\}
\end{aligned}
$$

Now, the left hand side deperds only on $v$ and the righthand side only on $V_{1}$. This implies that both must equal to the same function of the dependent variables, $S, V$ and $t$. This function is assumed to have the form

$$
-(\alpha-\varphi \beta \sqrt{U})
$$

where $\alpha$ and $\beta$ are the orift and volatility term for the stocastic differential equation (SDE) for $v$,

$$
d v(t)=\alpha d t+\eta \beta \sqrt{v} d z_{2}
$$

and the function $\varphi(S, v, t)$, which has yet to be determined is called the market price of volatility.
This leads to the expression
$\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}$

$$
\begin{aligned}
& +e^{v S \eta \beta \frac{\partial^{2} v}{\partial S \partial v}-r v+r S \frac{\partial v}{\partial S}} \\
& \quad=-(\alpha-\varphi \beta \sqrt{v}) \frac{\partial v}{\partial v}
\end{aligned}
$$

To understand the market price of volatility risk consider the portfolio,

$$
\pi_{1}=V-\Delta S
$$

where $v$ is an option and s the underlying asset. If dela hedging is assumed,

$$
\Delta=\frac{\partial V}{\partial S}
$$

then

$$
\pi_{1}=v-\frac{\partial v}{\partial S} S
$$

Recall that the It's formula is given by,

$$
\begin{gathered}
f\left(s_{1}, s_{2}, t\right) \\
d s_{i}(t)=a_{i}(t) d t+b_{i}(t) d z(t)
\end{gathered}
$$

$$
\begin{aligned}
d f(x, y, t) & =\frac{\partial f}{\partial t} d t+\left[a_{1} \frac{\partial f}{\partial x}+a_{2} \frac{\partial f}{\partial y}\right. \\
+ & \frac{1}{2} b_{1}^{2} \frac{\partial^{2} f}{\partial x^{2}}+\frac{1}{2} b_{2}^{2} \frac{\partial^{2} f}{\partial y} \\
+ & \left.e b_{1} b_{2} \frac{\partial^{2} f}{\partial x \partial y}\right] d t+b_{1} \frac{\partial f}{\partial x} d z_{1} \\
+ & b_{2} \frac{\partial f}{\partial y} d z_{2}
\end{aligned}
$$

Here it is assumed that $S$ and $v$ do not depend explicitly on time so $a_{i}(t)=0$. It follows that,

$$
\begin{aligned}
& d s(t)=\sqrt{v(t)} s(t) d z_{1} \\
& d v(t)=\eta \beta(s, v, t) \sqrt{v(t)} d z_{2}
\end{aligned}
$$

So

$$
b_{1}=\sqrt{v} S
$$

$$
b_{2}=\eta \beta \sqrt{v}
$$

Now using the self fonancing
condition

$$
d \pi_{1}=d V-\Delta d S
$$

consider $d V(S, v, t)$, from the Its formula

$$
\begin{aligned}
& d v=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e \eta \beta v s \frac{\partial^{2} v}{\partial s \partial v}\right] d t \\
& +\sqrt{v} s \frac{\partial v}{\partial s} d z_{1}+\eta \beta \sqrt{v} \frac{\partial v}{\partial v} d z_{2} \\
& =\left[\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.+\rho \eta \beta v s \frac{\partial^{2} v}{\partial s \partial v}\right] d t+\frac{\partial v}{\partial s} d s \\
& +\frac{\partial v}{\partial v} d v
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& d \pi_{1}=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e \eta \beta v s \frac{\partial^{2} v}{\partial s \partial u}\right] d t \\
& +\left[\frac{\partial v}{\partial s}-\Delta\right] d s \\
& +\frac{\partial v}{\partial v} d v
\end{aligned}
$$

From the assumption of delta hedging it follows that the ds term vanishes since,

$$
\Delta=\frac{\partial v}{\partial s}
$$

It follows that

$$
\begin{aligned}
& d \pi_{1}=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e \eta \beta u s \frac{\partial^{2} v}{\partial s \partial u}\right] d t \\
& +\frac{\partial v}{\partial v} d v
\end{aligned}
$$

If it is assumed that $\pi_{1}$ is risk-free then

$$
\begin{aligned}
d \pi_{1} & =r \pi_{1} d t \\
& =r\left[v-\frac{\partial v}{\partial s} s\right] d t
\end{aligned}
$$

The difference between $d \pi_{1}$ and the risk-free estimate is given by

$$
\begin{aligned}
& d \pi-r \pi d t=\frac{\partial v}{\partial t} d t+\left[\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}\right. \\
& \left.+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}+e \eta \beta u s \frac{\partial^{2} v}{\partial s \partial v}\right] d t \\
& +\frac{\partial v}{\partial v} d v-r\left[v-\frac{\partial v s}{\partial s}\right] d t \\
& =\left[\frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} u^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}}\right. \\
& \left.+e n \beta v s \frac{\partial^{2} v}{\partial s \partial u}-r v+r s \frac{\partial v}{\partial s}\right] d t \\
& +\frac{\partial v}{\partial v} d v
\end{aligned}
$$

Recall that presiously it was shown that,

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v S^{2} \frac{\partial^{2} v}{\partial S^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e^{v s \eta \beta \frac{\partial^{2} v}{\partial s \partial v}-r v+r \frac{\partial v}{\partial s} s} \\
& =-(\alpha-\varphi \beta \sqrt{v}) \frac{\partial v}{\partial v}
\end{aligned}
$$

Here it is assumed that $\alpha=0$ it follows that

$$
\begin{aligned}
d \pi- & r \pi_{1} d t=\varphi \beta \sqrt{U} \frac{\partial V}{\partial U} d t \\
& +\frac{\partial V}{\partial U} d U
\end{aligned}
$$

but $d v=\beta \eta \sqrt{v} d z_{2}$, thus

$$
\begin{gathered}
d \pi-r \Pi_{1} d t=\rho \beta \sqrt{v} \frac{\partial V}{\partial v}(\varphi d t \\
\left.+\eta d z_{1}\right)
\end{gathered}
$$

which gives the return beyond the risk-free return. It is seen that $\varphi$ plays the role of a rate of return on the exess above the risk-free return. This justifies the name "market price of volatility".
Now define the risk-newrtral drift by,

$$
\alpha^{\prime}=\alpha-\beta \sqrt{v} \varphi
$$

If this were the original drift term so that the risk-neutral SOE is given by

$$
d v=\alpha^{\prime} d t+\beta \sqrt{v} d z_{2}
$$

there would be no market price of odatility term and the return of $\pi$ would be risk-neutoral.
eoing forward it is assumed
that the SDE's for $S$ and $v$ are risk-neutral so that it can be used for option pricing.

## Local Uobatrity/

Here the local volatitity model developed by Dupier is discussed. It is shown that local odbatility is an average over instantaneaus volatilities.

Consider an option with expration $T$ and curent underlying stock price so. The collection of undiscounted opition prices with different strikes is denoted by,

$$
\left\{C\left(S_{0}, K, T\right)\right\}
$$

This collection of option prices is related to the risk-neutral density function $\varphi$ of the final spot price $s_{T}$ by

$$
C\left(S_{0}, K, T\right)=\int_{K}^{\Delta} \varphi\left(S_{T}, T_{1}: S_{0}\right)\left(S_{T}-K\right) d S_{T}
$$

The payoff for a European call option has been asscumed. Consider the derivative with respect to $K$,

$$
\begin{aligned}
\frac{\partial C}{\partial K}= & \frac{\partial}{\partial K} \int_{K}^{\Delta} \varphi\left(S_{T}, T: S_{0}\right)\left(S_{T}-K\right) d S_{T} \\
= & \frac{\partial}{\partial K} \int_{K}^{\infty} S_{T} \varphi\left(S_{T}, T ; S_{0}\right) d S_{T} \\
& -\frac{\partial}{\partial K} K \int_{K}^{\infty} \varphi\left(S_{T}, T: S_{0}\right) d S_{T} \\
= & -K \Phi\left(K, T: S_{0}\right)-\int_{K}^{\infty} \varphi\left(S_{T}, T: S_{0}\right) d S_{T} \\
& +K \varphi\left(K, T: S_{0}\right) \\
= & -\int_{K}^{\infty} \phi\left(S_{T}, T ; S_{0}\right) d S_{T}
\end{aligned}
$$

Taking the second derivative gives

$$
\begin{aligned}
\frac{\partial^{2} C}{\partial K^{2}} & =-\frac{\partial}{\partial K} S_{K}^{\alpha} \varphi\left(S_{T}, T ; S_{0}\right) d S_{T} \\
& =\varphi\left(K_{1} T: S_{0}\right)
\end{aligned}
$$

Thus the distribution of $S_{T}$ is given $y$

$$
\frac{\partial^{2} C}{\partial K^{2}}=\varphi\left(K, T: S_{0}\right)
$$

Now, if it is assumed that the risk-neutral drift is given by

$$
\mu_{t}=\left(r_{t}-D_{t}\right)
$$

where $r_{t}$ is the risk-free interest rate and $D_{t}$ the dividend yield. and the bcal volatility is given $b \%$,

$$
\sigma\left(s_{t}, t\right)
$$

then assume the asset price is given by,

$$
d s_{t}=\mu_{t} s_{t} d t+\sigma\left(s_{t}, t\right) s_{t} d z_{t}
$$

If the pseudo-probability density of the asset price at time $T$ is given by

$$
\varphi\left(S_{T}, T ; S_{0}\right)
$$

where $s_{0}$ is the asset price at $t=0$, find the Fokker-Plank equation satisfied by $Q\left(S_{T}, T ; S_{0}\right)$.
Recall the forward Kolmogorou equation, (i.e. Fokker Plank equation) for a random process,

$$
d \bar{x}_{t}=\mu\left(\bar{x}_{t}, t\right) d t+\sigma\left(\bar{x}_{t}, t\right) d z_{t}
$$

and the function with $f\left(\mathbb{Z}_{T}, T\right)$ with conditional expectation

$$
\begin{aligned}
& E\left[f(y, T) \mid X_{t}=x\right] \\
& \quad=\int_{-\infty}^{\infty} f(y, T) p(x, t \mid y, T) d y
\end{aligned}
$$

where $P(x, t: y, T)$ is the transition probability of $\Sigma_{T}$ at time $T$ starting from $X_{t}$ at $t$.

The distribution, $P(x, t: y, T)$, satisfies the equation

$$
\begin{gathered}
\frac{\partial}{\partial T} p(x, t \mid y, T)+\frac{\partial}{\partial y}[\mu(y, T) p(x, t \mid y, T)] \\
-\frac{1}{\partial} \frac{\partial^{2}}{\partial y^{2}}\left[\sigma^{2}(y, T) p(x, t \mid y, T)\right]=0
\end{gathered}
$$

Now, here $S_{T}=\bar{X}_{T}$, so

$$
d s_{t}=\mu_{t} s_{t} d t+\sigma\left(s_{t}, t\right) s_{t} d z_{t}
$$

$$
\begin{gathered}
P\left(\mathbb{Z}_{t}, t \mid \mathbb{X}_{T}, T\right)=\varphi\left(S_{T}, T ; S_{0}\right) \\
\mu\left(X_{T}, T\right)=\mu(T) S_{T} \\
\sigma\left(X_{T}, T\right)=\sigma\left(S_{T}, T\right) S_{T}
\end{gathered}
$$

It follows that $\varphi\left(S_{T}, T ; S_{0}\right)$ satisfies the equation,

$$
\frac{\partial \varphi}{\partial T}=\frac{1}{2} \frac{\partial^{2}}{\partial S_{T}^{2}}\left(\sigma^{2} S_{T}^{2} \varphi\right)-\frac{\partial}{\partial S_{T}}\left(\mu S_{T} \varphi\right)
$$

Now previously it was shown that for

$$
c\left(S_{0}, K, T\right)=\int_{K}^{\Delta} \varphi\left(S_{T}, T_{1}: S_{0}\right)\left(S_{T}-K\right) d S_{T}
$$

that

$$
\frac{\partial C}{\partial K}=-\int_{K}^{\alpha} \varphi\left(S_{T}, T ; S_{0}\right) d S_{T}
$$

$$
\frac{\partial^{2} c}{\partial k^{2}}=\varphi\left(k_{1} \tau: S_{0}\right)
$$

differentiating with respect to $T$ gives

$$
\begin{aligned}
\frac{\partial C}{\partial T} & =\frac{\partial}{\partial T}\left\{S_{K}^{\Delta} \varphi\left(S_{T}, T: S_{0}\right)\left(S_{T}-K\right) d S_{T}\right\} \\
& =\int_{K}^{\infty}\left(S_{T}-K\right) \frac{\partial \varphi}{\partial T} d S_{T} \\
& =\int_{K}^{\infty}\left\{\frac{1}{2} \frac{\partial^{2}}{\partial S_{T}^{2}}\left(\sigma^{2} S_{T}^{2} \varphi\right)-\right. \\
& \left.\frac{\partial}{\partial S_{T}}\left(\mu S_{T} \varphi\right)\right\}\left(S_{T}-K\right) d S_{T}
\end{aligned}
$$

Integrating by parts gives,

$$
\int u d v=u v-\int v d u
$$

$$
\begin{gathered}
d v=\left[\frac{1}{2} \frac{\partial^{2}}{\partial S_{T}^{2}}\left(\sigma^{2} S_{T}^{2} \varphi\right)-\frac{\partial}{\partial S_{T}}\left(\mu S_{T} \varphi\right)\right] d S_{T} \\
v=\frac{1}{2} \frac{\partial\left(\sigma^{2} S_{T}^{2} \varphi\right)}{\partial S_{T}} \cdot \mu S_{T} \varphi \\
u=S_{T}-K \quad d u=d S_{T}
\end{gathered}
$$

So,
$\frac{\partial C}{\partial T}=\left.\left\{\frac{1}{2} \frac{\partial\left(\sigma^{2} s_{T}^{2} \varphi\right)}{\partial s_{T}} \cdot \mu s_{T} \varphi\right\}\left(s_{T}-k\right)\right|_{k} ^{\infty}$

$$
-\int_{k}^{\infty}\left\{\frac{1}{2} \frac{\partial\left(\sigma^{2} S_{T}^{2} \varphi\right)}{\partial S_{T}}-\mu S_{T} \varphi\right\} d S_{T}
$$

Now as $S_{1} \rightarrow \infty \quad q \rightarrow 0$ and $\frac{\partial \varphi}{\partial S_{T}} \rightarrow 0$ so the first term is $\partial S_{T}$
zero.

$$
\begin{aligned}
\frac{\partial C}{\partial T} & =-\int_{k}^{\infty}\left\{\frac{1}{2} \frac{\partial\left(\sigma^{2} S_{T}^{2} \varphi\right)}{\partial S_{T}}-\mu S_{T} \varphi\right\} d S_{T} \\
& =-S_{k}^{\infty} \frac{1}{2} \frac{\partial\left(\sigma^{2} S_{T}^{2} \varphi\right) d S_{T}+\int_{k}^{\Delta} \mu S_{T} \varphi d S_{T}}{} \\
& =-\left.\frac{1}{2}\left(\sigma^{2} S_{T}^{2} \varphi\right)\right|_{k} ^{\infty}+\int_{k}^{\infty} \mu S_{T} \varphi d S_{T} \\
& =\frac{1}{2} \sigma^{2} K^{2} \varphi+\int_{k}^{\infty} \mu S_{T} \varphi d S_{T}
\end{aligned}
$$

Since $\mu_{T}$ is only a function of $T$ it follows that

$$
\int_{k}^{\infty} \mu S_{T} \varphi d S_{T}=\mu S_{k}^{\infty} S_{T} \varphi d S_{T}
$$

consider the integral
$\int_{k}^{\infty} S_{T} \varphi d S_{T}=\int_{k}^{\infty} S_{T} \varphi d S_{T}$

$$
\begin{aligned}
& -\int_{k}^{\infty} k \varphi d s_{T}+\int_{k}^{\infty} k \varphi d s_{T} \\
= & \int_{k}^{\infty} \varphi\left(s_{T}-k\right) d s_{T}+k \int_{k}^{-\Delta} \varphi d s_{T}
\end{aligned}
$$

Recall that

$$
\begin{aligned}
C\left(S_{0}, K, T\right) & =\int_{K}^{\Delta} \varphi\left(S_{T}, T ; S_{0}\right)\left(S_{T}-K\right) d S_{T} \\
\frac{\partial C}{\partial K} & =-\int_{K}^{\alpha} \varphi\left(S_{T}, T ; S_{0}\right) d S_{T}
\end{aligned}
$$

Thus

$$
\int_{K}^{\infty} S_{T} \varphi d S_{T}=C-K \frac{\partial C}{\partial K}
$$

putting things together gives

$$
\begin{aligned}
\frac{x}{\partial T} & =-\int_{k}^{\infty}\left\{\frac{1}{2} \frac{\partial\left(\sigma^{2} S_{T}^{2} \varphi\right)}{\partial S_{T}} \cdot \mu S_{T} \varphi\right\} d S_{T} \\
& =\frac{1}{2} \sigma^{2} K^{2} \varphi+\mu S_{k}^{A} S_{T} \varphi d S_{T}
\end{aligned}
$$

To get the final result recall

$$
\frac{\partial^{2} C}{\partial k^{2}}=\varphi
$$

Thus
$\frac{\partial C}{\partial T}\left(S_{0}, K, T\right)=\frac{\sigma^{2} K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}+\mu(T)\left[C-K \frac{\partial C}{\partial K}\right]$
This result is the Dupire equation.

## Forward Price

The forward price of the asset at time $t$ is given by

$$
F_{t}=s_{t} \exp \left[\int_{t}^{\top} \mu(s) d s\right]
$$

it follows that

$$
F_{T}=S_{T}
$$

and the forward price at $t=0$ is given by

$$
F_{0}=s_{0} \exp \left[\int_{0}^{\top} \mu(s) d s\right]
$$

where $\mu(t)$ is the risk-neutral drift term.

Consider the $S_{t} S D E$.

$$
d S_{t}=\mu_{t} S_{t} d t+\sigma\left(S_{t}, t\right) d z_{t}
$$

now

$$
\begin{aligned}
d F_{t} & =\exp \left[\int_{t}^{T} \mu(s) d s\right] d s_{t} \\
+s_{t} & (-\mu(t)) \exp \left[\int_{t}^{T} \mu(s) d s\right] d t \\
& =\exp \left[\int_{t}^{T} \mu(s) d s\right] d s_{t} \\
& -s_{t} \mu(t) \exp \left[\int_{t}^{T} \mu(s) d s\right] d t
\end{aligned}
$$

but

$$
d S_{t}=\mu_{t} S_{t} d t+\sigma\left(S_{t}, t\right) S_{t} d z_{t}
$$

so

$$
\begin{aligned}
d F_{t}= & \exp \left[\int_{t}^{T} \mu(s) d s\right]\left(\mu_{t} S_{t} d t\right. \\
& \left.+\sigma\left(s_{t}, t\right) s_{t} d Z_{t}\right) \\
& -s_{t} \mu(t) \exp \left[\int_{t}^{T} \mu(s) d s\right] d t
\end{aligned}
$$

$$
\begin{aligned}
& =\sigma\left(s_{t}, t\right) s_{t} \exp \left[\int_{t}^{\top} \mu(s) d s\right] d z_{t} \\
& =\sigma\left(s_{t}, t\right) F_{t} d z_{t}
\end{aligned}
$$

thus

$$
d F_{t}=\sigma\left(s_{t}, t\right) F_{t} d z_{t}
$$

but

$$
S_{t}=F_{t} \exp \left[-\int_{t}^{\top} \mu(s) d s\right]
$$

so

$$
\begin{aligned}
\sigma\left(F_{t}, t\right) & =\tilde{\sigma}\left(F_{t} \exp \left[-\int_{t}^{T} \mu(s) d s\right]\right) \\
& =\sigma\left(s_{t}, t\right)
\end{aligned}
$$

and finally

$$
d F_{t}=\sigma\left(F_{t}, t\right) F_{t} d z_{t}
$$

Recall that $F_{T}=S_{T}$ so

$$
c\left(F_{0}, K, T\right)=\int_{k}^{\infty} \varphi\left(F_{T}, T ; F_{0}\right)\left(F_{T}-k\right) d F_{T}
$$

and

$$
\begin{aligned}
\frac{\partial C}{\partial K}= & \frac{\partial}{\partial K}\left\{\int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right)\left(F_{T}-K\right) d F_{T}\right\} \\
= & \frac{\partial}{\partial K}\left\{\int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right) F_{T} d F_{T}\right. \\
& \left.-K \int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right) d F_{T}\right\} \\
= & -\varphi\left(K, T ; F_{0}\right) K-\int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right) d F_{T} \\
& +\varphi\left(K, T ; F_{0}\right) K \\
\Rightarrow \quad \frac{\partial C}{\partial K}= & -\int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right) d F_{T}
\end{aligned}
$$

$$
\frac{\partial^{2} c}{\partial K^{2}}=\varphi\left(K, T ; F_{0}\right)
$$

In summary

$$
\begin{gathered}
F_{t}=s_{t} \exp \left[\int_{t}^{T} \mu(s) d s\right] \\
d F_{t}=\sigma\left(s_{t}, t\right) F_{t} d z_{t} \\
c\left(F_{0}, K, T\right)=\int_{k}^{\Delta} \varphi\left(F_{T}, T ; s_{0}\right)\left(F_{T}-K\right) d F_{T} \\
\frac{\partial c}{\partial k}=-\int_{k}^{\Delta} \varphi\left(F_{T}, T ; F_{0}\right) d F_{T} \\
\frac{\partial^{2} c}{\partial K^{2}}=\varphi\left(K, T ; F_{0}\right)
\end{gathered}
$$

The Fokker-Plank equation for $\varphi\left(F_{T}, T ; F_{0}\right)$ is given by

$$
\frac{\partial \phi}{\partial T}=\frac{1}{2} \frac{\partial^{2}}{\partial F_{T}^{2}}\left(\sigma^{2} F_{T}^{2} \varphi\right)
$$

To find the equation for $C\left(F_{0}, K, T\right)$ consider

$$
\begin{aligned}
\frac{\partial C}{\partial T} & =\frac{\partial}{\partial T}\left\{\int_{K}^{\infty} \varphi\left(F_{T}, T ; F_{0}\right)\left(F_{T}-K\right) d F_{T}\right\} \\
& =\int_{K}^{\infty}\left(F_{T}-K\right) \frac{\partial \varphi}{\partial T} d F_{T} \\
& =\int_{K}^{\infty}\left(F_{T}-K\right) \frac{1}{2} \frac{\partial^{2}}{\partial F_{T}^{2}}\left(\sigma^{2} F_{T}^{2} \varphi\right) d F_{T}
\end{aligned}
$$

Integrating by parts gives

$$
\begin{array}{r}
\int u d v=u v-\int v d u \\
u=F_{T}-k \quad d u=d F_{T} \\
d v=\frac{\partial^{2}}{\partial F_{T}^{2}}\left(\sigma^{2} F_{T}^{2} \varphi\right) d F_{T}
\end{array}
$$

$$
\begin{aligned}
v & =\frac{\partial}{\partial F_{T}}\left(\sigma^{2} F_{T}^{2} \varphi\right) \\
\text { so } & \\
\frac{\partial C}{\partial T}= & \int_{k}^{\infty}\left(F_{T}-k\right) \frac{1}{2} \frac{\partial^{2}}{\partial F_{T}^{2}}\left(\sigma^{2} F_{T}^{2} \varphi\right) d F_{T} \\
= & \left.\left(F_{T}-k\right) \frac{\partial^{2}}{\partial F_{T}}\left(\sigma^{2} F_{T}^{2} \varphi\right) d F_{T}\right|_{k} ^{\infty} \\
& -\frac{1}{2} \int_{k}^{\infty} \frac{\partial}{\partial F_{T}}\left(\sigma^{2} F_{T}^{2} \varphi\right) d F_{T} \\
= & -\left.\frac{\sigma^{2}}{\partial} F_{T}^{2} \varphi\right|_{k} ^{\infty} \\
= & \frac{\sigma^{2}}{2}\left(k, T ; S_{0}\right) k^{2} \varphi\left(k, T ; F_{0}\right)
\end{aligned}
$$

recall that

$$
\frac{\partial^{2} c}{\partial K^{2}}=\varphi^{\left(K, T ; F_{0}\right)}
$$

## Thus

$$
\frac{\partial C}{\partial T}\left(F_{0}, K, T\right)=\frac{1}{2} \sigma^{2}\left(K, T ; S_{0}\right) K^{2} \frac{\partial^{2} C}{\partial K^{2}}
$$

Note that the drift term has been removed.
soluing for the colatility gives

$$
\sigma^{2}\left(K, T ; S_{0}\right)=\frac{\frac{\partial C}{\partial K}}{\frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}}
$$

The righthand side can be computed from the price history of the option.
This equation defines the local volatility.

## Local Dolatillty in Terms of Implied volatility

Market prices of options are quoted in terms of the lack.scholes implied volatility,

$$
\sigma_{B S}\left(K, T_{i} S_{0}\right)
$$

So,

$$
C\left(S_{0}, K, T\right)=C_{B S}\left(S_{0}, K, \sigma_{B S}\left(K, T ; S_{0}\right), T\right)
$$

Define the dimensionless variables:

1. The Black-Scholes inplied total variance,

$$
\omega\left(S_{0}, K, T\right)=\sigma_{B S}^{2}\left(S_{0}, K, T\right) T
$$

2. The log-strike

$$
y=\ln \frac{k}{F_{0}}
$$

where

$$
F_{0}=s_{0} \exp \left\{\int_{0}^{T} u(s) d s\right\}
$$

is the forward price of the asset at $t=0$

Recall that the Black-Sholes solution for a European call option was previously found to be,

$$
\begin{aligned}
& c(t)=s(t) N\left(d_{+}(t, s(t))\right. \\
& -k e^{-r(T-t)} N\left(d_{-}(t, s(t))\right. \\
& d_{+}(t, z)=\frac{\ln \frac{2}{k}+\left(r+2 \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, z)=\frac{\ln \frac{2}{k}+\left(r-1 \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}}
\end{aligned}
$$

here $t=0$ and $F_{t}=s(t) e^{\int_{t}^{\top} u(s) d s}$. since the forward price is
used the risk-tree drift tom is zero, using this info

$$
\begin{aligned}
C_{B S} & =F_{0} N\left(d_{+}\left(0, F_{0}\right)\right)-K N\left(d\left(0, F_{0}\right)\right) \\
d_{+}\left(0, F_{0}\right) & =\frac{\ln \frac{F_{0}}{K}+\frac{1}{2} \sigma^{2} T}{\sigma \sqrt{T}} \\
d_{-}\left(0, F_{0}\right) & =\frac{\ln \frac{F_{0}}{K}-\frac{1}{2} \sigma^{2} T}{\sigma \sqrt{T}}
\end{aligned}
$$

Now, using

$$
\begin{aligned}
\omega & =\sigma_{B S}^{2}\left(S_{0}, K, T\right) T \\
y & =\ln \frac{K}{F_{0}}
\end{aligned}
$$

gives

$$
\begin{aligned}
d_{1}\left(0, F_{0}\right) & =-\frac{y+\frac{1}{2} \omega}{\sqrt{\omega}} \\
& =\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}
\end{aligned}
$$

$$
\begin{aligned}
d_{-}\left(0, F_{0}\right) & =\frac{-y-\frac{1}{2} \omega}{\sqrt{\omega}} \\
& =\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}
\end{aligned}
$$

putting things together

$$
\begin{aligned}
& C_{B S}=F_{0} N\left(\frac{-}{H^{2}}+\frac{\sqrt{\omega}}{2}\right)-K N\left(-\frac{y}{W^{2}}-\frac{\sqrt{\omega}}{2}\right) \\
& \left.=F_{0}\left[N\left(-\frac{H}{2}\right)+\frac{\sqrt{\omega}}{2}\right)-\frac{k}{F_{0}} N\left(-\frac{\frac{H}{\omega}}{\omega}-\frac{\sqrt{\omega}}{2}\right)\right] \\
& =F_{0}\left[N\left(\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{y} N\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)\right] \\
& \Rightarrow C_{B s}=F_{0}\left[N\left(\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{y} N\left(\frac{-y}{\omega}-\frac{\sqrt{\omega}}{2}\right)\right] \\
& \text { Now consider, }
\end{aligned}
$$

$$
\begin{aligned}
\omega\left(S_{0}, K, T\right) & =\sigma_{B S}^{2}\left(S_{0}, K, T\right) T \\
& =\omega(Y, T) \\
y\left(S_{0}, K, T\right) & =\ln \frac{K}{F_{0}} \\
& =y(T)
\end{aligned}
$$

Differentiating $C(\omega, y, T)$ with respect to its dependent variables gives

$$
\begin{aligned}
\frac{\partial C}{\partial y}= & \frac{\partial C_{B S}}{\partial y}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y} \\
\frac{\partial^{2} C}{\partial y^{2}}= & \frac{\partial^{2} C_{B S}}{\partial y^{2}}+\frac{\partial^{2} C_{B S}}{\partial y \partial \omega} \frac{\partial \omega}{\partial y} \\
& +\frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y}+\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2} \\
& +\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{\partial^{2} C_{B S}}{\partial y^{2}}+2 \frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y} \\
& +\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}} \\
\frac{\partial C}{\partial T}= & \frac{\partial C_{B S}}{\partial T}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial T}
\end{aligned}
$$

Now from inspection of $C_{B S}$,

$$
C_{B S}=F_{0}\left[N\left(\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{y} N\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)\right]
$$

it is seen that the only explicit $T$ dependence is in

$$
E_{0}=s_{0} e^{S_{0}^{T} u(s) d s}
$$

so

$$
\begin{aligned}
\frac{\partial F_{0}}{\partial T} & =\mu(T) S_{0} e^{S_{0}^{T} \mu(s) d s} \\
& =\mu(T) F_{0}
\end{aligned}
$$

it follows that

$$
\frac{\partial C_{B S}}{\partial T}=\mu(T) C_{B S}
$$

trus

$$
\begin{aligned}
\frac{\partial C}{\partial T} & =\frac{\partial C_{B S}}{\partial T}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial T} \\
& =\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial T}+\mu(T) C_{B S}
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
\frac{\partial C}{\partial y}= & \frac{\partial C_{B S}}{\partial y}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y} \\
\frac{\partial^{2} C}{\partial y^{2}}= & \frac{\partial^{2} C_{B S}}{\partial y^{2}}+2 \frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y} \\
& +\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}}
\end{aligned}
$$

$$
\frac{\partial C}{\partial T}=\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial T}+\mu(T) C_{B S}
$$

Next the CBS derivatives will be evaluated from the expression for CBS, recall
$C_{B S}=F_{0}\left[N\left(\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{y} N\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)\right]$
where

$$
\begin{aligned}
& N(x)=\frac{1}{\sqrt{2 \pi}} \int_{-a}^{x} e^{-y^{2} / 2} d y \\
& \frac{\partial N}{\partial x}=n(x)=\frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2} \\
& \frac{\partial^{2} N}{\partial x^{2}}=\frac{\partial}{\partial x} n(x)=\frac{\partial}{\partial x}\left(\frac{1}{\sqrt{2 \pi}} e^{-x^{2} / 2}\right) \\
&=-\frac{1}{\sqrt{2 \pi}} x e^{-x^{2} / 2} \\
&=-x n(x)
\end{aligned}
$$

## The following derivatives are required,

$$
\frac{\partial C_{B S}}{\partial \omega} \quad \frac{\partial^{2} C_{B S}}{\partial \omega^{2}} \quad \frac{\partial C_{B S}}{\partial y} \quad \frac{\partial^{2} C_{B S}}{\partial y^{2}} \quad \frac{\partial^{2} C_{B S}}{\partial \omega \partial y}
$$

Now

$$
d_{+}=-\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2} \quad r_{-}=-\frac{y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}
$$

Then

$$
C_{B S}=F_{0}\left[N\left(d_{+}\right)-e^{y} N\left(d_{-}\right)\right]
$$

First a few useful derivatives are evaluated

$$
\frac{\partial N}{\partial d_{t}}=n\left(d_{t}\right) \quad \frac{\partial N}{\partial d_{-}}=n\left(d_{-}\right)
$$

$$
\begin{aligned}
& \frac{\partial n\left(d_{+}\right)}{\partial \omega}=-d_{+} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \omega} \\
& \begin{aligned}
\frac{\partial n(d)}{\partial \omega} & =-d_{-} n\left(d_{-}\right) \frac{\partial d_{-}}{\partial \omega} \\
\frac{\partial d_{+}}{\partial \omega} & =\frac{\partial}{\partial \omega}\left(\frac{-y}{1 \omega}+\frac{\sqrt{\omega}}{\partial}\right) \\
& =\frac{y}{2 \omega^{3 / 2}}+\frac{1}{4 \omega} \\
& =\frac{1}{2 \omega}\left(\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{\partial}\right) \\
& =-\frac{d}{\partial \omega}
\end{aligned} \\
& \begin{aligned}
\frac{\partial d_{-}}{\partial \omega} & =\frac{\partial}{\partial \omega}\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right) \\
& =\frac{y}{\partial \omega^{3 / 2}}-\frac{1}{4 \sqrt{\omega}}
\end{aligned}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-1}{2 \omega}\left[\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right] \\
& =-\frac{d_{+}}{2 \omega} \\
\frac{\partial d_{+}}{\partial y} & =\frac{2}{2 y}\left[-\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right] \\
& =-\frac{1}{\sqrt{\omega}} \\
\frac{\partial d_{-}}{\partial y} & =\frac{2}{\partial y}\left[-\frac{y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right] \\
& =-\frac{1}{\sqrt{\omega}} \\
d_{+} d_{-} & =\left(\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)\left(-\frac{y}{\omega}-\frac{\sqrt{\omega}}{2}\right) \\
& =\frac{y^{2}}{\omega}-\frac{\omega}{4}-\frac{y}{2}+\frac{y}{2} \\
& =\frac{y^{2}}{\omega}-\frac{\omega}{4}
\end{aligned}
$$

$$
\begin{aligned}
d_{-}-d_{+} & =\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)-\left(-\frac{\sqrt{\omega}}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right) \\
& =-\sqrt{\omega} \\
d_{-}+d_{+} & =\left(\frac{-y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)+\left(-\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right) \\
& =-\frac{2 y}{\sqrt{\omega}}
\end{aligned}
$$

Next it will be shown that

$$
n\left(d_{+}\right)=e^{\prime} n\left(d_{-}\right)
$$

If it assumed that

$$
\begin{aligned}
n\left(d_{+}\right) & =e^{y} n\left(d_{-}\right) \\
e^{-d_{+12}^{2}} & =e^{y} e^{-d_{-12}^{2}} \\
\Rightarrow e^{y} & =e^{d_{-12}^{2}-d_{+12}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow y & =\frac{d_{-}^{2}}{2}-\frac{d_{+}^{2}}{2} \\
& =\frac{1}{2}\left(d_{-}-d_{-1}\right)\left(d_{-}+d_{+}\right)
\end{aligned}
$$

but

$$
d_{-}-d_{+}=-\sqrt{\omega} \quad d_{-}+d_{+}=-\frac{2 y}{\sqrt{\omega}}
$$

so for the righthand side

$$
\begin{aligned}
\frac{1}{2}\left(d_{-}-d_{-1}\right)\left(d_{-}+d_{+}\right) & =\frac{1}{2}(-\sqrt{\omega})\left(-\frac{2 y}{\sqrt{\omega}}\right) \\
& =y
\end{aligned}
$$

Thus

$$
n\left(d_{+}\right)=e^{y} n\left(d_{-}\right)
$$

In summary

$$
\begin{gathered}
\frac{\partial N}{\partial d_{+}}=n\left(d_{+}\right) \quad \frac{\partial N}{\partial d_{-}}=n\left(d_{-}\right) \\
\frac{\partial n\left(d_{+}\right)}{\partial \omega}=-d_{+} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \omega} \\
\frac{\partial n\left(d_{-}\right)}{\partial \omega}=-d_{-} n\left(d_{-}\right) \frac{\partial d_{-}}{\partial \omega} \\
\frac{\partial d_{+}}{\partial \omega}=-\frac{d_{-}}{\partial \omega} \quad \frac{\partial d_{-}}{\partial \omega}=-\frac{d_{+}}{\partial \omega} \\
\frac{\partial d_{+}}{\partial y}=-\frac{1}{\sqrt{\omega}} \quad \frac{\partial d_{-}}{\partial y}=-\frac{1}{\sqrt{\omega}} \\
d_{+} d_{-}=\frac{y^{2}}{\omega}-\frac{\omega}{4} \\
d_{-}-d_{+}=-\sqrt{\omega} \quad d_{-}+d_{+}=-\frac{2 y}{\sqrt{\omega}} \\
y=\frac{d_{+}^{2}}{2}-\frac{d_{-}^{2}}{2} \\
n\left(d_{+}\right)=e^{y} n\left(d_{-}\right)
\end{gathered}
$$

Now

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial \omega} & =\frac{\partial}{\partial \omega}\left\{F_{0}\left[N\left(d_{+}\right)-e^{y} N\left(d_{-}\right)\right]\right\} \\
& =F_{0}\left[\frac{\partial N}{\partial d_{+}} \frac{\partial d_{+}}{\partial \omega}-e^{y} \frac{\partial N}{\partial d_{-}} \frac{\partial d_{-}}{\partial \omega}\right] \\
& =F_{0}\left[n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \omega}-e^{y} n\left(d_{-}\right) \frac{\partial d_{-}}{\partial \omega}\right] \\
& =F_{0}\left[n\left(d_{+}\right)\left(-\frac{d_{-}}{\partial \omega}\right)-e^{y} n\left(d_{-}\right)\left(-\frac{d_{+}}{\partial \omega}\right)\right] \\
& =-F_{0}\left[n\left(d_{+}\right) \frac{d_{-}}{\partial \omega}-e^{y} n\left(d_{-}\right) \frac{d_{+}}{\partial \omega}\right] \\
& =-\frac{F_{0}}{\partial \omega}\left[n\left(d_{+}\right) d_{-}-e^{y} n\left(d_{-}\right) d_{+}\right]
\end{aligned}
$$

but

$$
n\left(d_{+}\right)=e^{\prime} n\left(d_{-}\right)
$$

so

$$
\frac{\partial C_{B S}}{\partial \omega}=-\frac{F_{0}}{\partial \omega}\left[n\left(d_{+}\right) d_{-}-n\left(d_{+}\right) d_{+}\right]
$$

$$
\begin{aligned}
& =-\frac{F_{0}}{2 \omega} n\left(d_{+}\right)\left(d_{-}-d_{+}\right) \\
& =-\frac{F_{0}}{\partial \omega} n\left(d_{+}\right)(-\sqrt{\omega}) \\
& =\frac{F_{0} n\left(d_{+}\right)}{\partial \sqrt{\omega}}
\end{aligned}
$$

Thus

$$
\frac{\partial C_{B S}}{\partial \omega}=\frac{F_{0} n\left(d_{+}\right)}{\partial \sqrt{\omega}}
$$

Now

$$
\begin{aligned}
\frac{\partial^{2} C_{B S}}{\partial \omega^{2}} & =\frac{\partial}{\partial \omega}\left(\frac{\partial C_{B S}}{\partial \omega}\right) \\
& =\frac{\partial}{\partial \omega}\left[\frac{F_{0}}{\partial \sqrt{\omega}} n\left(d_{+}\right)\right] \\
& =\frac{F_{0}}{2} n\left(d_{+}\right) \frac{\partial}{\partial \omega}\left(\frac{1}{\sqrt{\omega}}\right)
\end{aligned}
$$

$$
+\frac{F_{0}}{\partial I \omega} \frac{\partial n\left(d_{+}\right)}{\partial \omega}
$$

Now

$$
\begin{aligned}
& \frac{\partial n\left(d_{+}\right)}{\partial \omega}=-d_{+} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \omega} \\
& \frac{\partial}{\partial \omega}\left(\frac{1}{\sqrt{\omega}}\right)=-\frac{1}{2 \omega^{3 / 2}}
\end{aligned}
$$

So

$$
\begin{aligned}
\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}= & \frac{F_{0}}{2} n\left(d_{+}\right)\left(-\frac{1}{\partial \omega^{3 / 2}}\right) \\
& +\frac{F_{0}}{\partial \sqrt{\omega}}\left(-d_{+} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \omega}\right) \\
= & \frac{F_{0}}{\partial \sqrt{\omega}} n\left(d_{+}\right)\left(-\frac{1}{2 \omega}-d_{+} \frac{\partial d_{+}}{\partial \omega}\right)
\end{aligned}
$$

consider the righthand side term

$$
\frac{\partial d_{t}}{\partial \omega}=-\frac{d}{2 \omega} \quad d_{t} d_{-}=\frac{y^{2}}{\omega}-\frac{\omega}{4}
$$

So,

$$
\begin{aligned}
-\frac{1}{\partial \omega}-d_{+} \frac{\partial d_{+}}{\partial \omega} & =-\frac{1}{\partial \omega}-\left(\frac{-d_{-}}{\partial \omega}\right) d_{+} \\
& =-\frac{1}{\partial \omega}+\frac{1}{\partial \omega}\left(\frac{y^{2}}{\omega}-\frac{\omega}{4}\right) \\
& =-\frac{1}{2 \omega}-\frac{1}{8}+\frac{y^{2}}{\partial \omega^{2}}
\end{aligned}
$$

Finally

$$
\begin{aligned}
\frac{\partial^{2} C_{B S}}{\partial \omega^{2}} & =\frac{F_{0}}{\partial \sqrt{\omega}} n\left(d_{+}\right)\left(-\frac{1}{\partial \omega}-d_{+} \frac{\partial d_{+}}{\partial \omega}\right) \\
& =\frac{F_{0}}{\partial \sqrt{\omega}} n\left(d_{+}\right)\left(-\frac{1}{\partial \omega}-\frac{1}{8}+\frac{y^{2}}{\partial \omega}\right) \\
& =\left(-\frac{1}{8}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right) \frac{\partial C_{B S}}{\partial \omega}
\end{aligned}
$$

## Thus

$$
\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}=\left(-\frac{1}{8}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right) \frac{\partial C_{B S}}{\partial \omega}
$$

Next consider,

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial y}= & \frac{\partial}{\partial y}\left\{F_{0}\left[N\left(d_{+}\right)-e^{y} N\left(d_{-}\right)\right]\right\} \\
= & F_{0}\left[n\left(d_{+}\right) \frac{\partial d_{+}}{\partial y}-e^{y} n(d) \frac{\partial d}{\partial y}\right. \\
& \left.-e^{y} N\left(d_{-}\right)\right]
\end{aligned}
$$

Now

$$
\begin{gathered}
\frac{\partial d_{1}}{\partial y}=-\frac{1}{\sqrt{\omega}} \frac{\partial d_{2}}{\partial y}=-\frac{1}{\sqrt{\omega}} \\
n\left(d_{+}\right)=e^{y} n\left(d_{-}\right)
\end{gathered}
$$

So,

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial y}=F_{0}\left[n\left(d_{+}\right) \frac{\partial d_{+}}{\partial y}-e^{y} n(d) \frac{\partial d}{\partial y}\right. \\
\left.-e^{y} N\left(d_{-}\right)\right] \\
=F_{0}\left[n\left(d_{+}\right)(-1)-n\left(d_{+}\right)(-1)\right. \\
\left.-e^{y} N\left(d_{-}\right)\right] \\
=F_{0}\left[\frac{n\left(d_{+}\right)}{\sqrt{\omega}}+\frac{n\left(d_{+}\right)}{\sqrt{\omega}}\right]-F_{0} e^{y} N\left(d_{-}\right) \\
=-F_{0} e^{y} N\left(d_{-}\right) \\
\Rightarrow \frac{\partial C_{B S}}{\partial y}=-F_{0} e^{y} N\left(d_{-}\right)
\end{aligned}
$$

Next,

$$
\frac{\partial^{2} C_{B s}}{\partial y \partial \omega}=\frac{\partial}{\partial y}\left[\frac{F_{0} n\left(d_{+}\right)}{\partial \sqrt{\omega}}\right]
$$

$$
\begin{aligned}
& =\frac{F_{0}}{\partial \sqrt{\omega}} \frac{\partial}{\partial y} n\left(d_{+}\right) \\
& =-\frac{F_{0}}{\partial \sqrt{\omega}} d_{+} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial y}
\end{aligned}
$$

but

$$
\begin{gathered}
\frac{\partial d_{+}}{\partial y}=-\frac{1}{\sqrt{\omega}} \quad d_{+}=-\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2} \\
\frac{\partial C_{B S}}{\partial \omega}=\frac{F_{0} n\left(d_{+}\right)}{\partial \omega^{\omega}}
\end{gathered}
$$

so

$$
\begin{aligned}
\frac{\partial^{2} C_{B S}}{\partial y \partial \omega} & =-\frac{F_{0}}{\partial \sqrt{\omega}} d_{+} n\left(d_{+}\right) \frac{\partial d_{1}}{\partial y} \\
& =-\frac{F_{0}}{\partial \sqrt{\omega}} n\left(d_{+}\right)\left(-\frac{1}{\sqrt{\omega}}\right)\left(-\frac{y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right) \\
& =\frac{\partial C_{B S}}{\partial \omega}\left(\frac{1}{2}-\frac{y}{\omega}\right)
\end{aligned}
$$

$$
\Rightarrow \quad \frac{\partial^{2} C_{B S}}{\partial y \partial \omega}=\frac{\partial C_{B S}}{\partial \omega}\left(\frac{1}{2}-\frac{y}{\omega}\right)
$$

Finally,

$$
\begin{aligned}
\frac{\partial^{2} C_{B S}}{\partial y^{2}} & =\frac{\partial}{\partial y}\left(\frac{\partial C_{B S}}{\partial y}\right) \\
& =\frac{\partial}{\partial y}\left[-F_{0} e^{y} N(d-)\right] \\
& =-F_{0} e^{y} n(d) \frac{\partial d}{\partial y}-F_{0} e^{y} N(d)
\end{aligned}
$$

Now

$$
\frac{\partial d_{-}}{\partial y}=-\frac{1}{\sqrt{\omega}} \quad n\left(d_{+}\right)=e^{\prime} n\left(d_{-}\right)
$$

$$
\begin{aligned}
& \frac{\partial C_{B S}}{\partial y}=-F_{0} e^{y} N\left(d_{-}\right) \\
& \frac{\partial C_{B S}}{\partial \omega}=\frac{F}{\partial}_{0} n\left(d_{+}\right)
\end{aligned}
$$

So,

$$
\begin{aligned}
& \frac{\partial^{2} C_{B s}}{\partial y^{2}}=-F_{0} e^{y} n\left(d_{-}\right) \frac{\partial d_{-}}{\partial y}-F_{0} e^{y} N\left(d_{-}\right) \\
&=-F_{0} e^{y} n\left(d_{-}\right)\left(-\frac{1}{\sqrt{\omega}}\right)-F_{0} e^{y} N\left(d_{-}\right) \\
&=\frac{F_{0}}{\sqrt{\omega}} e^{y} n\left(d_{-}\right)-F_{0} e^{y} N\left(d_{-}\right) \\
&=\frac{F_{0}}{\sqrt{\omega}} n\left(d_{+}\right)-F_{0} e^{y} N\left(d_{-}\right) \\
&=2 \frac{\partial C_{B s}}{\partial \omega}+\frac{\partial C_{B s}}{\partial y} \\
& \Rightarrow \frac{\partial^{2} C_{B s}}{\partial y^{2}}-\frac{\partial C_{B s}}{\partial y}=2 \frac{\partial C_{B s}}{\partial \omega}
\end{aligned}
$$

In summary,

$$
\begin{gathered}
\frac{\partial C_{B S}}{\partial \omega}=\frac{F_{0}}{\partial \omega^{\prime} \omega}\left(d_{+}\right) \\
\frac{\partial C_{B S}}{\partial y}=-F_{0} e^{y} N(d) \\
\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}=\left(-\frac{1}{\delta}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right) \frac{\partial C_{B S}}{\partial \omega} \\
\frac{\partial^{2} C_{B S}}{\partial y \partial \omega}=\frac{\partial C_{B S}}{\partial \omega}\left(\frac{1}{2}-\frac{y}{\omega}\right) \\
\frac{\partial^{2} C_{B S}}{\partial y^{2}}-\frac{\partial C_{B S}}{\partial y}=2 \frac{\partial C_{B S}}{\partial \omega}
\end{gathered}
$$

Next recall the Dupire equation for $c\left(S_{0}, K, T\right)$
$\frac{\partial C}{\partial T}\left(S_{0}, K, T\right)=\frac{\sigma^{2} K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}+\mu(T)\left[C-K \frac{\partial C}{\partial K}\right]$

Now using,

$$
\begin{aligned}
y=\ln \frac{K}{F_{0}} & \Rightarrow K=F_{0} e^{y} \\
\frac{\partial K}{\partial y} & =K
\end{aligned}
$$

gives for $C\left(S_{0}, F_{0} e^{Y}, T\right)$

$$
\begin{array}{r}
\frac{\partial c}{\partial y}=\frac{\partial c}{\partial k} \frac{\partial k}{\partial y}=\frac{\partial c}{\partial k} k \\
\frac{\partial^{2} c}{\partial y^{2}}=\frac{\partial^{2} c}{\partial^{2} k} k^{2}+\frac{\partial c}{\partial k} k \\
\Rightarrow k^{2} \frac{\partial^{2} c}{\partial^{2} k}=\frac{\partial^{2} c}{\partial y^{2}}-\frac{\partial c}{\partial y} \\
\text { since, } F_{0}=s_{0} e^{\int_{0}^{\top} w(s) d s}
\end{array}
$$

The total deriodtue with respect $\tau$ is gien $d y$

$$
\frac{\partial C}{\partial T}=\frac{\partial C^{*}}{\partial T}+\frac{\partial C}{\partial K} \frac{\partial K}{\partial T}
$$

Here $\partial C^{*}$ is the deridative of $C$ with repect to the independent variable $T$.

Now

$$
\begin{aligned}
\frac{\partial K}{\partial T} & =\frac{\partial}{\partial T} F_{0} e^{y}=e^{y} \frac{\partial F_{0}}{\partial T} \\
& =e^{y} \mu(T) F_{0} \\
& =\mu(T) K
\end{aligned}
$$

so the total $T$ derivative is given by

$$
\frac{\partial C}{\partial T}=\frac{\partial C^{*}}{\partial T}+\mu K \frac{\partial C}{\partial K}
$$

$$
\Rightarrow \frac{\partial C^{*}}{\partial T}=\frac{\partial C}{\partial T}-\mu K \frac{\partial C}{\partial K}
$$

Bringing things together

$$
\begin{aligned}
& \frac{\partial C^{*}}{\partial T}=\frac{\partial C}{\partial T}-\mu K \frac{\partial C}{\partial K} \\
= & \frac{\sigma^{2} K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}+\mu(T)\left[C-K \frac{\partial C}{\partial K}\right] \\
\Rightarrow & \frac{\partial C}{\partial T}-\mu K^{2} \frac{\partial C}{\partial K}+\tilde{\mu} K \frac{\partial C}{\partial K}=\frac{\sigma^{2} K^{2}}{2} \frac{\partial C}{\partial K^{2}} \\
& +\mu C \\
\Rightarrow & \frac{\partial C}{\partial T}=\frac{\sigma^{2} K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}+\mu C
\end{aligned}
$$

but

$$
k^{2} \frac{\partial^{2} C}{\partial^{2} k}=\frac{\partial^{2} C}{\partial y^{2}}-\frac{\partial C}{\partial y}
$$

The local variance is defined by,

$$
\sigma^{2}=\nu_{l}
$$

50

$$
\frac{\partial C}{\partial T}=\frac{U_{L}}{2}\left(\frac{\partial^{2} C}{\partial y^{2}}-\frac{\partial C}{\partial y}\right)+\mu C
$$

Now it is time to put everythis together,

$$
\begin{gathered}
C_{B S}=F_{0}\left[N\left(d_{+}\right)-e^{y} N\left(d_{-}\right)\right] \\
d_{+}=\frac{-y}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2} \quad C_{-}=-\frac{y}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2} \\
F_{0}=S_{0} e^{S_{0}^{T} u(s) d s} \\
\omega\left(S_{0}, K, T\right)=\sigma_{B S}^{2}\left(S_{0}, K, T\right) T \\
y=\ln \frac{K}{F_{0}}
\end{gathered}
$$

It has been shown that

$$
\begin{aligned}
& \frac{\partial C_{B S}}{\partial \omega}=\frac{F_{0}}{\partial T_{\omega}} n\left(d_{+}\right) \\
& \frac{\partial C_{B S}}{\partial y}=-F_{0} e^{y} N\left(d_{-}\right)
\end{aligned}
$$

(1) $\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}=\left(-\frac{1}{8}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right) \frac{\partial C_{B S}}{\partial \omega}$
(2)

$$
\frac{\partial^{2} C_{B S}}{\partial y \partial \omega}=\frac{\partial C_{B S}}{\partial \omega}\left(\frac{1}{2}-\frac{y}{\omega}\right)
$$

(3)

$$
\frac{\partial^{2} C_{B S}}{\partial y^{2}}-\frac{\partial C_{B S}}{\partial y}=\frac{2 \partial C_{B S}}{\partial \omega}
$$

It has also been shown that for,

$$
C\left(F_{0}, \omega, y\right)=C_{B s}\left(F_{0}, \omega, y, \sigma_{B s}\left(S_{0}, K, T\right)\right)
$$

(1) $\frac{\partial C}{\partial y}=\frac{\partial C_{B S}}{\partial y}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y}$
(5) $\frac{\partial^{2} C}{\partial y^{2}}=\frac{\partial^{2} C_{B S}}{\partial y^{2}}+2 \frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y}$

$$
+\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}}
$$

(6) $\quad \frac{\partial C}{\partial T}=\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial T}+\mu(T) C_{B S}$
and that the Dupire equation
for $C\left(S_{0}, F_{0} e^{y}, T\right)$ is given by
(1) $\quad \frac{\partial C}{\partial T}=\frac{U_{L}}{2}\left(\frac{\partial^{2} C}{\partial y^{2}}-\frac{\partial C}{\partial y}\right)+\mu C$

Now equating (6) and (1) and
noting that

$$
C=C_{B S}
$$

gives

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial \omega} & \frac{\partial \omega}{\partial T}+\mu C_{B S}=\frac{\nu_{L}}{2}\left(\frac{\partial^{2} C}{\partial y^{2}}-\frac{\partial C}{\partial y}\right) \\
& +\mu C_{B S} \\
\Rightarrow & \frac{\partial C_{B S}}{\partial T} \frac{\partial \omega}{\partial T}=\frac{\nu_{L}}{2}\left(\frac{\partial^{2} S}{\partial y^{2}}-\frac{\partial C}{\partial y}\right)
\end{aligned}
$$

Now from equations (4) an (b)

$$
\begin{aligned}
& \frac{\partial C_{B S}}{\partial T} \frac{\partial \omega}{\partial T}=\frac{\nu_{L}}{\partial} \frac{\partial^{2} C}{\partial y^{2}}-\frac{\nu_{L}}{\partial} \frac{\partial C}{\partial y} \\
& =\frac{\nu_{L}}{\partial}\left[\frac{\partial^{2} C_{B S}}{\partial y^{2}}+2 \frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y}\right.
\end{aligned}
$$

$$
\begin{aligned}
+ & \left.\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}}\right] \\
-\frac{U_{L}}{2} & {\left[\frac{\partial C_{B S}}{\partial y}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y}\right] } \\
=\frac{U_{L}}{2} & {\left[\frac{\partial^{2} C_{B S}}{\partial y^{2}}-\frac{\partial C_{B S}}{\partial y}+2 \frac{\partial^{2} C_{B S}}{\partial \omega \partial y} \frac{\partial \omega}{\partial y}\right.} \\
& +\frac{\partial^{2} C_{B S}}{\partial \omega^{2}}\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}} \\
& \left.-\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y}\right]
\end{aligned}
$$

The first four terms can be replaced by equations (3), (1) and (2) resulting in,

$$
\frac{\partial C_{B S}}{\partial T} \frac{\partial \omega}{\partial T}=\frac{U_{L}}{2}\left[2 \frac{\partial C_{B S}}{\partial \omega}\right.
$$

$$
\begin{aligned}
& +2 \frac{\partial C_{B S}}{\partial \omega}\left(\frac{1}{2}-\frac{y}{\omega}\right) \frac{\partial \omega}{\partial y}+ \\
& \left(-\frac{1}{\delta}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right) \frac{\partial C_{B S}}{\partial \omega}\left(\frac{\partial \omega}{\partial y}\right)^{2} \\
& \left.+\frac{\partial C_{B S}}{\partial \omega} \frac{\partial^{2} \omega}{\partial y^{2}}-\frac{\partial C_{B S}}{\partial \omega} \frac{\partial \omega}{\partial y}\right] \\
& =\frac{U_{L}}{2} \frac{\partial C_{B S}}{\partial \omega}\left[2^{1}+2\left(\frac{1}{2}-\frac{y}{\omega}\right) \frac{\partial \omega}{\partial y}\right. \\
& +\left(-\frac{1}{\delta}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2} \\
& \left.+\frac{\partial^{2} \omega}{\partial y^{2}}-\frac{\partial \omega}{\partial y}\right] \\
& =\frac{U_{L}}{2} \frac{\partial C_{B S}}{\partial \omega}\left[2-\frac{\partial \omega}{\partial y}+2\left(\frac{1}{2}-\frac{y}{\omega}\right) \frac{\partial \omega}{\partial y}\right. \\
& \left.+\left(-\frac{1}{\delta}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial^{2} \omega}{\partial y^{2}}\right]
\end{aligned}
$$

## Thus,

$$
\begin{aligned}
& \frac{\partial C_{B S}}{\partial T} \frac{\partial \omega}{\partial T}=\frac{U_{L}}{2} \frac{\partial C_{B S}}{\partial \omega}\left[2-\frac{\partial \omega}{\partial y}+2\left(\frac{1}{2}-\frac{y}{\omega}\right) \frac{\partial \omega}{\partial y}\right. \\
& \left.+\left(-\frac{1}{8}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{\partial^{2} \omega}{\partial y^{2}}\right] \\
& \text { soluins for } U_{L} \text { gives } \\
& \Rightarrow \frac{\partial \omega}{\partial T}=U_{L}\left[1-\frac{1}{2} \frac{\partial \omega}{\partial y}+\frac{1}{2} \frac{\partial \omega}{\partial y}-\frac{y}{\omega} \frac{\partial \omega}{\partial y}\right. \\
& \left.+\frac{1}{2}\left(-\frac{1}{8}-\frac{1}{\partial \omega}+\frac{y^{2}}{\partial \omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{1}{2} \frac{\partial^{2} \omega}{\partial y^{2}}\right] \\
& =V_{L}\left[1-\frac{y}{\omega} \frac{\partial \omega}{\partial y}+\frac{1}{4}\left(-\frac{1}{4}-\frac{1}{\omega}+\frac{y^{2}}{\omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}\right. \\
& \left.+\frac{1}{2} \frac{\partial^{2} \omega}{\partial y^{2}}\right]
\end{aligned}
$$

$$
\Rightarrow \nu_{L}=\frac{\frac{\partial \omega}{\partial T}}{1-\frac{y}{\omega} \frac{\partial \omega}{\partial y}+\frac{1}{4}\left(-\frac{1}{4}-\frac{1}{\omega}+\frac{y^{2}}{\omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{1}{2} \frac{\partial^{2} \omega}{\partial y^{2}}}
$$

## Special Case: No Skew

Previously it was shown that the local variance $U_{L}$ is related to,

$$
\omega=O_{B S}^{2} T
$$

$$
y=\ln \frac{K}{F_{0}}
$$

where $\sigma_{B S}^{2}$ is the implied volatility, by the following relation

$$
J_{L}=\frac{\frac{\partial \omega}{\partial T}}{1-\frac{y}{\omega} \frac{\partial \omega}{\partial y}+\frac{1}{4}\left(-\frac{1}{4}-\frac{1}{\omega}+\frac{y^{2}}{\omega}\right)\left(\frac{\partial \omega}{\partial y}\right)^{2}+\frac{1}{2} \frac{\partial^{2} \omega}{\partial y^{2}}}
$$

consider the case of zero skew. For this case

$$
\frac{\partial \omega}{\partial y}=0
$$

## It follows that,

$$
\nu_{L}=\frac{\partial \omega}{\partial T}
$$

50

$$
\omega(T)=\int_{0}^{T} U_{L}(t) d t
$$

## Local Ucriance as conditional Expectation of Instantaneous Viriance

Consider the SDE for the price of an asset.

$$
d s_{t}=\mu_{t} s_{t} d t+\sqrt{v_{t}} s_{t} d z_{1}
$$

Recall that the forward price is defined by,

$$
F_{t}=s_{t} e^{S_{t}^{\top}} \mu_{s} d s
$$

previously it was shown that

$$
d F_{t}=\sqrt{v_{t}} F_{t} d z_{t}
$$

From the definition of $F_{t}$ it is seen that

$$
F_{T}=S_{T}
$$

thus

$$
d F_{T}=d S_{T}
$$

Now the undiscanted value of a European option with strike $k$ expiring at time $T$ is given by

$$
C\left(S_{0}, K, T\right)=E\left[\left(S_{T}-K\right)^{+}\right]
$$

differentiating with respect to $k$ gives

$$
\frac{\partial C}{\partial K}=\frac{\partial}{\partial K} E\left[\left(S_{\tau}-K\right)^{+}\right]
$$

for $S_{T}-K<0,\left(S_{T}-K\right)^{t}=0$, so

$$
\frac{\partial c}{\partial k}=0
$$

for $S_{T}-K>0,\left(S_{T}-K\right)^{+}=S_{T}-K$, so
$\frac{\partial C}{\partial K}=\frac{\partial}{\partial K} E\left[S_{T}-K\right]$

$$
\begin{aligned}
& =E\left[\frac{\partial}{\partial K}\left(S_{T}-K\right)\right] \\
& =E[-1] \\
& =-1
\end{aligned}
$$

Thus

$$
\frac{\partial C}{\partial K}=\left\{\begin{aligned}
-1 & S_{T}-K>0 \\
0 & S_{T}-K \leq 0
\end{aligned}\right.
$$

The Heaviside function is defined by

$$
\theta(x)= \begin{cases}1 & x>0 \\ 0 & x \leqslant 0\end{cases}
$$

Thus

$$
\frac{\partial C}{\partial K}=E\left[\theta\left(S_{T}-K\right)\right]
$$

To evaluate the second derivative
recall that the Dirac delta function is defined by

$$
\begin{aligned}
\delta(x) & =\frac{d \theta}{d x} \\
\Rightarrow \theta(x) & =\int_{-\infty}^{x} \delta(s) d s
\end{aligned}
$$

thus,

$$
\begin{aligned}
\frac{\partial^{2} C}{\partial K^{2}} & =\frac{\partial E}{\partial K}\left[\theta\left(S_{T}-K\right)\right] \\
& =E\left[\delta\left(S_{T}-K\right)\right]
\end{aligned}
$$

Recall the Its formula for a function $f\left(S_{T}, T\right)$,

$$
d f=\frac{\partial f}{\partial T} d T+\nu_{T} S_{T}^{2} \frac{\partial^{2} f}{\partial S_{T}^{2}} d T+\frac{\partial S}{\partial S_{T}} d S_{T}
$$

let $f\left(S_{T}-T\right)=\left(S_{T}-K\right)^{+}$
then

$$
\begin{aligned}
& \frac{\partial f}{\partial T}=0 \\
& \frac{\partial f}{\partial S_{T}}=\theta\left(S_{T}-K\right) \\
& \frac{\partial^{2} f}{\partial S_{T}^{2}}=\delta\left(S_{T}-K\right)
\end{aligned}
$$

Then

$$
\begin{aligned}
d\left(S_{T}-K\right)=\theta\left(S_{T}-K\right) & d S_{T} \\
& +\frac{\nu_{T} S_{T}^{2}}{2} \delta\left(S_{T}-K\right) d T
\end{aligned}
$$

Now, since $S_{\tau}=F_{\tau}$

$$
d F_{T}=d S_{T}
$$

$F_{T}$ is a martingale so it has constant expectation it follows that

$$
E\left[d F_{T}\right]=d E\left[F_{T}\right]=0=E\left[d S_{\tau}\right]
$$

$E\left[d\left(S_{T}-K\right)^{+}\right]=d E\left[\left(S_{T}-K\right)^{+}\right]$
$=E\left[\theta\left(S_{T}-K\right) d S_{T}+\nu_{T} S_{T}^{2} \delta\left(S_{T}-K\right) d T\right]$
$=E\left[\theta\left(S_{T}-K\right) d S_{T}\right]+E\left[\nu_{T} S_{T}^{2} \delta\left(S_{T}-K\right) d T\right]$
For the first term

$$
\theta\left(S_{T}-k\right) d S_{T}= \begin{cases}0 & S_{T}-k \leqslant 0 \\ d S_{T} & S_{T}-k>0\end{cases}
$$

it follows that

$$
E\left[\theta\left(S_{T}-K\right) d S_{T}\right]=E\left[d S_{T}\right]=0
$$

For the second term since $d T$ is deterministic

$$
\begin{aligned}
& E\left[\nu_{T} S_{T}^{2} \delta\left(S_{T}-K\right) d T\right] \\
& \quad=E\left[\nu_{T} S_{T}^{2} \delta\left(S_{T}-K\right)\right] d T
\end{aligned}
$$

Consider the expectation argument

$$
\begin{aligned}
& \int_{-\Delta}^{\infty} U_{T} S_{T}^{2} \delta\left(S_{T}-k\right) d S_{T} \\
= & U_{T}(k) k^{2} \int_{-\infty}^{\infty} \delta\left(S_{T}-k\right) d S_{T}
\end{aligned}
$$

Thus

$$
\begin{aligned}
& E\left[U_{T} S_{T}^{2} \delta\left(S_{T}-k\right)\right] \\
& \quad=E\left[U_{T} \mid S_{T}=k\right] k^{2} E\left[\delta\left(S_{T}-k\right)\right]
\end{aligned}
$$

but

$$
E\left[\delta\left(S_{T}-K\right)\right]=\frac{\partial^{2} C}{\partial K^{2}}
$$

and

$$
\begin{aligned}
& E\left[d\left(S_{T}-K\right)^{t}\right]=d E\left[\left(S_{T}-K\right)^{t}\right] \\
& =d c
\end{aligned}
$$

putting things together gives

$$
\begin{aligned}
& d C=E\left[U_{T} \mid S_{T}=K\right] \frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}} d T \\
\Rightarrow & \frac{\partial C}{\partial T}=E\left[U_{T} \mid S_{T}=K\right] \frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}} \\
\Rightarrow & E\left[U_{T} \mid S_{T}=K\right]=\frac{\frac{\partial C}{\partial T}}{\frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}}
\end{aligned}
$$

Recall that the local variance is given by,

$$
U_{C}\left(K, T ; S_{0}\right)=\frac{\frac{\partial C}{\partial K}}{\frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}}
$$

It follows that

$$
U_{L}\left(K, T ; S_{0}\right)=E\left[U_{T} \mid S_{\tau}=K\right]
$$

Thus the local variance is equal to the expectation of the istantaneous variance given that $s_{T}=K$.

These two variances are computed differenly. The long variance, $u$, is the volatility coefficient obtained from the Fokker-Plank equation for the tranistition probability of the option price from time $t$ to $T$.

The long varrance can also be computed directly from the option price.

The instaniedes variance, $v_{\tau}$, is the variance dotained using the matingale definition of the option price for the computation.

## The Heston Model

Recall the general volatility model previously described,

$$
\begin{gathered}
d s_{t}=\mu_{t} s_{t} d t+\sqrt{v_{t}} s_{t} d z_{1} \\
d v_{t}=\alpha\left(s_{t}, v_{t}, t\right) d t+\eta \beta\left(s_{t}, v_{t}, t\right) \sqrt{v_{2}} d z_{2}
\end{gathered}
$$

The Heston Model is defined by assuming

$$
\begin{gathered}
\alpha\left(s_{t}, v_{t}, t\right)=-\lambda\left(v_{t}-\bar{v}\right) \\
\beta\left(s_{t}, v_{t}, t\right)=1
\end{gathered}
$$

Thus the SDE for the Heston model is given by

$$
\begin{gathered}
d s_{t}=\mu_{t} s_{t} d t+\sqrt{v_{t}} s_{t} d z_{1} \\
d v_{t}=-\lambda\left(v_{t}-\bar{v}\right) d t+\eta \sqrt{v_{t}} d z_{2}
\end{gathered}
$$

where

$$
\left\langle d z_{1}, d z_{2}\right\rangle=\rho d t
$$

and $\bar{v}$ is the average value of $v_{t}$ and $\lambda$ is the rate of return of $v_{t}$ to a deviation from $\overline{0}$.

Note the similarity to the discrete error-correction model previously studied.
Here it is called an affine jump diffusion process (AJD).

The Error correction model is used to model mean reverting processes.
Recall that previously it was shown that the value of an option $V\left(s_{t}, v_{t}, t\right)$ satisfies the following equation for the general volatility model,

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v S^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial u^{2}} \\
& +e u S \eta \beta \frac{\partial^{2} v}{\partial s \partial v}-r v+r s \frac{\partial v}{\partial s} \\
& =-(\alpha-\varphi \beta \sqrt{u}) \frac{\partial v}{\partial u}
\end{aligned}
$$

Here

$$
\alpha=-\lambda\left(U_{t}-\bar{v}\right) \quad \beta=1
$$

the valuation equation becomes

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e v s \eta \frac{\partial^{2} v}{\partial s \partial v}-r v+r s \frac{\partial v}{\partial s} \\
& =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}+\varphi \sqrt{u} \frac{\partial v}{\partial v}
\end{aligned}
$$

To get the Heston model it must also be assumed that $\varphi=0$ which implies that the market cost of rist is zero.

This is equivalent to assuming a risk-neutral measure.

It follows that

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e v s \eta \frac{\partial^{2} v}{\partial s \partial u}-r v+r s \frac{\partial v}{\partial s} \\
& =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}
\end{aligned}
$$

## Hestan Solution For Europen Options

To motivate the solution of the Heston model recall the Blacksholes solution for the European call option

$$
\begin{aligned}
& c(t)=s(t) N\left(d_{+}(t, s(t))\right. \\
&-k e^{-r(T-t)} N\left(d_{-}(t, s(t))\right. \\
& d_{+}(t, 2)=\frac{\ln \frac{2}{k}+\left(r+\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T-t}} \\
& d_{-}(t, 2)=\frac{\ln \frac{2}{k}+\left(r-\frac{1}{2} \sigma^{2}\right)(T-t)}{\sigma \sqrt{T t}}
\end{aligned}
$$

The call option price is seen to be composed of two terms. The first,

$$
S(t) N\left(d_{+}(t, S(t))\right.
$$

can be thought of as the precolo-expectation of the asset price at time $t$ given that the option is in the money. For the second,

$$
k e^{-r(T-t)} N\left(d_{-}(t, s(t))\right.
$$

the torm $k e^{-r(T-t)}$ is the discounted strike price of the option so the second term can be viewed as the psendo-expectation that the option is excercised.
This motivates seeking a solution to the Heston model of the form

$$
C(x, v, \tau)=K\left[e^{x} P_{1}(x, v, \tau) \cdot P_{0}(x, v, \tau)\right]
$$

where the interpretation is the same as for the Black-Shotes solution. Here $k$ is the strike price and $k e^{x}$ is the asset price.

Furthur consis der the variables,

$$
x=\ln \frac{F_{t}}{K} \quad \tau=T-t
$$

were

$$
F_{t}=s_{t} e^{\int_{t}^{T} \mu(s) d s}
$$

which is similar to the parameterization used prevously. Now, previously the Hestom model was derived and stown to be,

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v S^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e v s \eta \frac{\partial^{2} v}{\partial s \partial u}-r v+r s \frac{\partial v}{\partial s} \\
& =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}
\end{aligned}
$$

where $U$ is the option price. It is desired to express this equation in terms of the variables $x, v, \tau$.

So,

$$
\begin{aligned}
& \frac{\partial v}{\partial t}=\frac{\partial v}{\partial \tau} \frac{\partial \tau}{\partial t} \\
& \begin{aligned}
\frac{\partial v}{\partial S_{t}} & =\frac{\partial v}{\partial x} \frac{\partial x}{\partial S_{t}} \\
\frac{\partial^{2} v}{\partial S_{t}^{2}} & =\frac{\partial}{\partial S_{t}} \frac{\partial v}{\partial S_{t}} \\
& =\frac{\partial}{\partial S_{t}}\left(\frac{\partial v}{\partial x} \frac{\partial x}{\partial S_{t}}\right) \\
& =\frac{\partial^{2} v}{\partial x^{2}}\left(\frac{\partial x}{\partial S_{t}}\right)^{2}+\frac{\partial v}{\partial x} \frac{\partial^{2} x}{\partial S_{t}^{2}}
\end{aligned}
\end{aligned}
$$

Now,

$$
\frac{\partial \tau}{\partial t}=-1
$$

and

$$
\begin{aligned}
\frac{\partial F_{t}}{\partial S_{t}} & =\frac{\partial}{\partial S_{t}} S_{t} e^{S_{t}^{T} \mu(s) d s} \\
& =e^{S_{t}^{T} \mu(s) d s} \\
\frac{\partial x}{\partial S_{t}} & =\frac{\partial}{\partial S_{t}}\left(\ln \frac{F_{t}}{k}\right) \\
& =\frac{1}{F_{t}} \frac{\partial F_{t}}{\partial S_{t}} \\
& =\frac{e^{S_{t}^{T} \mu(s) d s}}{S_{t}^{T} \mu(s) d s} \\
& =\frac{1}{S_{t}}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial x^{2}}{\partial s_{t}^{2}} & =\frac{\partial}{\partial s_{t}}\left(\frac{1}{s_{t}}\right) \\
& =-\frac{1}{s_{t}^{2}}
\end{aligned}
$$

thus

$$
\begin{gathered}
\frac{\partial \tau}{\partial t}=-1 \\
\frac{\partial x}{\partial S_{t}}=\frac{1}{S_{t}} \quad \frac{\partial x^{2}}{\partial S_{t}^{2}}=-\frac{1}{S_{t}}
\end{gathered}
$$

Putting things together,

$$
\begin{aligned}
& \frac{\partial V}{\partial t}=\frac{\partial V}{\partial \tau} \frac{\partial \tau}{\partial t}=-\frac{\partial V}{\partial \tau} \\
& \frac{\partial V}{\partial S_{t}}=\frac{\partial V}{\partial x} \frac{\partial x}{\partial S_{t}}=\frac{\partial V}{\partial x} \frac{1}{S_{t}} \\
& \frac{\partial^{2} V}{\partial S_{t}^{2}}=\frac{\partial^{2} V}{\partial x^{2}}\left(\frac{\partial x}{\partial S_{t}}\right)^{2}+\frac{\partial V}{\partial x} \frac{\partial^{2} x}{\partial S_{t}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{\partial^{2} v}{\partial x^{2}}\left(\frac{1}{s_{t}^{2}}\right)-\frac{\partial v}{\partial x}\left(\frac{1}{s_{t}^{2}}\right) \\
= & \frac{1}{s_{t}^{2}}\left[\frac{\partial^{2} v}{\partial x^{2}}+\frac{\partial v}{\partial x}\right] \\
\frac{\partial^{2} v}{\partial s_{t} \partial v_{t}} & =\frac{\partial}{\partial v_{t}}\left(\frac{\partial v}{\partial s}\right) \\
& =\frac{\partial}{\partial u}\left(\frac{\partial v}{\partial x} \frac{1}{s_{t}}\right) \\
& =\frac{\partial^{2} v}{\partial v \partial x} \frac{1}{s_{t}} \\
\text { Thus } & \\
\frac{\partial v}{\partial t}= & \frac{\partial v}{\partial \tau} \\
\frac{\partial v}{\partial s_{t}} & =\frac{\partial v}{\partial x} \frac{1}{s_{t}} \\
\frac{\partial^{2} v}{\partial s_{t}^{2}} & =\frac{1}{s_{t}^{2}}\left[\frac{\partial^{2} v}{\partial x^{2}}+\frac{\partial v}{\partial x}\right]
\end{aligned}
$$

$$
\frac{\partial^{2} v}{\partial S_{t} \partial v_{t}}=\frac{\partial^{2} v}{\partial v \partial x} \frac{1}{S_{t}}
$$

Now

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v s^{2} \frac{\partial^{2} v}{\partial s^{2}}+\frac{1}{2} \eta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e v s \eta \frac{\partial^{2} v}{\partial s \partial u}-r v+r s \frac{\partial v}{\partial s} \\
& =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}
\end{aligned}
$$

Here it is assumed that $r=0$ so,

$$
\begin{aligned}
& -\frac{\partial v}{\partial \tau}+\frac{1}{2} v_{t} S_{t}^{2} N_{1} \frac{1}{S_{t}^{2}}\left[\frac{\partial^{2} v}{\partial x^{2}}+\frac{\partial v}{\partial x}\right] \\
& +\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} v}{\partial v^{2}}+e v_{t} S_{t \eta} \frac{\partial^{2} v}{\partial v_{t} \partial x} \frac{1}{S_{t}} \\
& =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}
\end{aligned}
$$

$$
\begin{aligned}
= & -\frac{\partial v}{\partial \tau}+\frac{v_{t}}{2}\left[\frac{\partial^{2} v}{\partial x^{2}}-\frac{\partial v}{\partial x}\right] \\
& +\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} v}{\partial v^{2}}+\rho v_{t} \frac{\partial^{2} v}{\partial v_{t} \partial x} \\
= & \lambda\left(v_{t}-\bar{v}\right) \frac{\partial v}{\partial v}
\end{aligned}
$$

Let $v=c$ then

$$
\begin{aligned}
& -\frac{\partial c}{\partial \tau}+\frac{v_{t}}{2} \frac{\partial^{2} c}{\partial x^{2}}-\frac{v_{t}}{2} \frac{\partial c}{\partial x}+\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} c}{\partial v_{t}^{2}} \\
& +e \eta v_{t} \frac{\partial^{2} c}{\partial v_{t} \partial x}-\lambda\left(v_{t}-\bar{v}\right) \frac{\partial c}{\partial v_{t}} \\
& =0
\end{aligned}
$$

Assuming a solution of the form

$$
C(x, v, \tau)=K\left[e^{x} P_{1}(x, v, \tau) \cdot P_{0}(x, v, \tau)\right]
$$

Equations for $P_{1}(x, v, \tau)$ and $P_{0}(x, v, \tau)$ are obtained by substitution into the equation for $c(x, v, \tau)$.
First each term will be evaluated

$$
\begin{aligned}
-\frac{\partial C}{\partial \tau} & =-k e^{x} \frac{\partial P_{1}}{\partial \tau}+k \frac{\partial P_{0}}{\partial \tau} \\
\frac{v_{t}}{2} \frac{\partial C}{\partial x} & =\frac{v_{t}}{2} \frac{\partial}{\partial x} k\left(e^{x} P_{1}-P_{2}\right) \\
& =\frac{v_{t}}{2} k\left[e^{x} P_{1}+e^{x} \frac{\partial P_{1}}{\partial x}-\frac{\partial P_{0}}{\partial x}\right]
\end{aligned}
$$

$$
\begin{aligned}
\frac{v_{t}}{2} \frac{\partial^{2} C}{\partial x^{2}} & =\frac{v_{t}}{2} \frac{\partial}{\partial x}\left(\frac{\partial C}{\partial x}\right) \\
& =\frac{v_{t}}{2} \frac{\partial}{\partial x} k\left[e^{x} P_{1}+e^{x} \frac{\partial P_{1}}{\partial x}-\frac{\partial P_{0}}{\partial x}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{k v_{t}}{2}\left[e^{x} P_{1}+e^{x} \frac{\partial P_{1}}{\partial x}+e^{x} \frac{\partial P_{1}}{\partial x}\right. \\
& \left.+e^{x} \frac{\partial^{2} P_{1}}{\partial x^{2}}-\frac{\partial^{2} P_{0}}{\partial x^{2}}\right] \\
& =\frac{k v_{t}}{\partial}\left[e^{x} P_{1}+2 e^{x} \frac{\partial P_{1}}{\partial x}+e^{x} \frac{\partial^{2} P_{1}}{\partial x^{2}}-\frac{\partial^{2} P_{0}}{\partial x^{2}}\right] \\
& \begin{aligned}
\lambda\left(v_{t}-\bar{v}\right) \frac{\partial c}{\partial v_{t}} & =\lambda\left(v_{t}-\bar{v}\right) \frac{\partial}{\partial v_{t}}\left(k e^{x} P_{1}-P_{0}\right) \\
= & \lambda k\left(v_{t}-\bar{v}\right)\left[e^{x} \frac{\partial P_{t}}{\partial v_{t}}-\frac{\partial P_{0}}{\partial v_{t}}\right] \\
\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} c}{\partial v_{t}^{2}}= & \frac{1}{2} \eta^{2} v_{t} \frac{\partial}{\partial v_{t}}\left(\frac{\partial c}{\partial v_{t}}\right) \\
= & \frac{1}{2} \eta^{2} v_{t} \frac{\partial}{\partial v_{t}} k\left[e^{x} \frac{\partial P_{1}}{\partial v_{t}}-\frac{\partial P_{0}}{\partial v_{t}}\right] \\
= & \frac{1}{2} k \eta^{2} v_{t}\left[e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t}^{2}}-\frac{\partial^{2} P_{0}}{\partial v_{t}^{2}}\right]
\end{aligned}
\end{aligned}
$$

$$
\begin{aligned}
e \eta v_{t} & \frac{\partial^{2} c}{\partial v_{t} \partial x}=e \eta v_{t} \frac{\partial}{\partial v_{t}}\left(\frac{\partial c}{\partial x}\right) \\
& =e \eta v_{t} \frac{\partial}{\partial v_{t}} k\left[e^{x} P_{1}+e^{x} \frac{\partial P_{1}}{\partial x}-\frac{\partial P_{0}}{\partial x}\right] \\
& =e \eta v_{t} k\left[e^{x} \frac{\partial P_{1}}{\partial v_{t}}+e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x} \cdot \frac{\partial^{2} P_{0}}{\partial v_{t} \partial x}\right]
\end{aligned}
$$

Putting things together gives.

$$
\begin{aligned}
& -\frac{\partial C}{\partial \tau}+\frac{v_{t}}{2} \frac{\partial^{2} C}{\partial x^{2}}-\frac{v_{t}}{2} \frac{\partial C}{\partial x}+\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} C}{\partial v_{t}^{2}} \\
& +e \eta v_{t} \frac{\partial^{2} C}{\partial v_{t} \partial x}-\lambda\left(v_{t}-\bar{v}\right) \frac{\partial C}{\partial v_{t}} \\
& =0 \\
& =-k e^{x} \frac{\partial P_{1}}{\partial \tau}+k \frac{\partial P_{0}}{\partial \tau}+k \frac{v_{t}}{\partial}\left[e^{x} P_{1}+2 e^{x} \frac{\partial P_{1}}{\partial x}\right. \\
& \left.+e^{x} \frac{\partial^{2} P_{1}}{\partial x^{2}}-\frac{\partial^{2} P_{0}}{\partial x^{2}}\right]-\frac{v_{t}}{2} k\left[e^{x} P_{1}\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.+e^{x} \frac{\partial P_{1}}{\partial x}-\frac{\partial P_{0}}{\partial x}\right]+\frac{1}{2} k \eta^{2} v_{t}\left[e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t}^{2}}\right. \\
& \left.-\frac{\partial^{2} P_{0}}{\partial v_{t}^{2}}\right]+k e \eta v_{t} k\left[e^{x} \frac{\partial P_{1}}{\partial v_{t}}+e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x}\right. \\
& \left.-\frac{\partial^{2} P_{0}}{\partial v_{t} \partial x}\right]-\lambda k\left(v_{t}-\bar{v}\right)\left[e^{x} \frac{\partial P_{1}}{\partial v_{t}}-\frac{\partial P_{0}}{\partial v_{t}}\right] \\
& =0
\end{aligned}
$$

Gathering terms gives,

$$
\begin{aligned}
& -k e^{x} \frac{\partial P_{1}^{\prime}}{\partial \tau}+k \frac{v_{t}}{\partial}\left[e^{x} P_{1}+2 e^{x} \frac{\partial P_{1}}{\partial x}\right. \\
& \left.+e^{x} \frac{\partial^{2} P_{1}}{\partial x^{2}}\right]-\frac{v_{t}}{2} k\left[e^{x} P_{1}+e^{x} \frac{\partial P_{1}}{\partial x}\right] \\
& +\frac{1}{2} k \eta^{2} v_{t} e^{x} \frac{\partial^{2} P_{1}^{\prime}}{\partial v_{t}^{2}}+e \eta v_{t} k\left[e^{x} \frac{\partial P_{1}^{\prime}}{\partial v_{t}}\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.+e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x}\right]-\lambda K\left(v_{t}-\bar{v}\right) e^{x} \frac{\partial P_{1}}{\partial v_{t}} \\
& +\frac{K \frac{\partial P_{0}}{\partial \tau}}{2}-\frac{K v_{t}}{\partial} \frac{\partial^{2} P_{0}}{\partial x^{2}}+\frac{v_{t}}{2} K \frac{\partial P_{0}}{\partial x} \\
& -\frac{1}{2} K \eta^{2} v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t}^{2}}-e \eta v_{t} K \frac{\partial^{2} P_{0}}{\partial v_{t} \partial x} \\
& +\lambda K\left(v_{t}-\bar{v}\right) \frac{\partial P_{0}}{\partial v_{t}} \\
& =0 \\
& \Rightarrow+\frac{K e^{x}}{\partial P_{1}}+\frac{K v_{t} e^{x} P_{1}}{\partial \tau}-\frac{v_{t}}{2} K e^{x} P_{1} \\
& +K v_{t} e^{x} \frac{\partial P_{1}}{\partial x}-\frac{v_{t} k}{2} e^{x} \frac{\partial P_{1}}{\partial x}+\frac{K v_{t}}{\partial} e^{x} \frac{\partial^{2} P_{1}}{\partial x^{2}} \\
& +\frac{1}{2} K \eta^{2} v_{t} e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t}^{2}}+e \eta v_{t} k e^{x} \frac{\partial P_{1}}{\partial v_{t}} \\
& +e \eta v_{t} k e^{x} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x}-\lambda k\left(v_{t}-\bar{v}\right) e^{x} \frac{\partial P_{1}}{\partial v_{t}}
\end{aligned}
$$

$$
\begin{aligned}
& +\frac{K \partial P_{0}}{\partial \tau}-K \frac{v_{t}}{\partial} \frac{\partial^{2} P_{0}}{\partial x^{2}}+\frac{v_{t}}{2} K \frac{\partial P_{0}}{\partial x} \\
& -\frac{1}{2} K \eta^{2} v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t}^{2}}-e \eta v_{t} K \frac{\partial^{2} P_{0}}{\partial v_{t} \partial x} \\
& +\lambda K\left(v_{t}-\bar{v}\right) \frac{\partial P_{0}}{\partial v_{t}} \\
& =0 \\
& =K e^{x}\left[-\frac{\partial P_{1}}{\partial \tau}+\frac{v_{t}}{2} \frac{\partial P_{1}}{\partial x}+\frac{v_{t}}{\partial} \frac{\partial^{2} P_{1}}{\partial x^{2}}\right. \\
& +\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} P}{\partial v_{t}^{2}}+e \eta v_{t} \frac{\partial P_{1}}{\partial v_{t}} \\
& \left.+e \eta v_{t} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x}-\lambda\left(v_{t}-\bar{v}-e \eta v_{t}\right) \frac{\partial P_{1}}{\partial v_{t}}\right] \\
& -K\left[-\frac{\partial P_{0}}{\partial \tau}+\frac{v_{t} \partial^{2} P_{0}}{\partial x^{2}}-\frac{v_{t} \frac{\partial P_{0}}{\partial}}{\partial x}\right. \\
& +\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t}^{2}}+e \eta v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t} \partial x}
\end{aligned}
$$

$$
\left.=0 \quad-\lambda\left(v_{t}-\bar{v}\right) \frac{\partial P_{0}}{\partial v_{t}}\right]
$$

Now since $e^{x}>0$ for all values of $x$. It follow that for the equation to equal zero for any $x$ it must be that

$$
\begin{aligned}
& -\frac{\partial P_{1}}{\partial \tau}+\frac{v_{t}}{2} \frac{\partial P_{1}}{\partial x}+\frac{v_{t}}{\partial} \frac{\partial^{2} P_{1}}{\partial x^{2}} \\
+ & \frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} P}{\partial v_{t}^{2}}+e \eta v_{t} \frac{\partial P_{1}}{\partial v_{t}} \\
+ & e \eta v_{t} \frac{\partial^{2} P_{1}}{\partial v_{t} \partial x}-\left[\lambda\left(v_{t}-\bar{v}\right)-e \eta v_{t}\right] \frac{\partial P_{1}}{\partial v_{t}}=0
\end{aligned}
$$

and

$$
\begin{aligned}
& -\frac{\partial P_{0}}{\partial \tau}+\frac{v_{t}}{\partial} \frac{\partial^{2} P_{0}}{\partial x^{2}}-\frac{v_{t}}{2} \frac{\partial P_{0}}{\partial x}+\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t}^{2}} \\
& +e \eta v_{t} \frac{\partial^{2} P_{0}}{\partial v_{t} \partial x}-\lambda\left(v_{t}-\bar{v}\right) \frac{\partial P_{0}}{\partial v_{t}}=0
\end{aligned}
$$

Consider

$$
\left[\lambda\left(v_{t}-\bar{v}\right)-e \eta v_{t}\right]=v_{t}(\lambda-e \eta)-\lambda \bar{v}
$$

let $j=0,1$ it then follows that both equations satisfy

$$
\begin{aligned}
& -\frac{\partial P_{j}}{\partial t}+\frac{v}{2} \frac{\partial^{2} P_{j}}{\partial x^{2}}-\left(\frac{1}{2}-j\right) v \frac{\partial P_{j}}{\partial x} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} P_{j}}{\partial v^{2}}+e \eta v \frac{\partial^{2} P_{j}}{\partial x \partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial P_{j}}{\partial v}=0
\end{aligned}
$$

where $j=0,1$

$$
a=\lambda \bar{v} \quad b_{j}=\lambda-j l \eta
$$

Now consider the limit $\tau \rightarrow 0$. of $P_{j}(x, v, \tau)$ as a function of $x$ for fixed $v$,

In this limit $t \rightarrow T$, thus the option appoaches expiration. To evaluate the boundary on $P_{j}(x, v, r)$ in this limit, note that,

$$
x_{t}=\ln \frac{F_{t}}{K}
$$

so, $F_{t}>K \Rightarrow x>0$ and $F_{t} \leqslant K=2 x \leqslant 0$. Now if $x \geqslant 0$ then the option is in the money, so

$$
C=F_{T}-K
$$

and

$$
P_{j}(x, v, 0)=1
$$

and if $x \leqslant 0$ the option is out of the money, so $c=0$ and

$$
P_{j}(x, 0,0)=0
$$

Thus the boundary condition is given by

$$
\begin{aligned}
P_{j}(x, v, 0) & = \begin{cases}1 & x>0 \\
0 & x \leqslant 0\end{cases} \\
& =\theta(x)
\end{aligned}
$$

where $\theta(x)$ is the teaviside step function.
The $P_{j}(x, v, \tau)$ equations are solved using the Fourier transform to eliminate the
variable $x$. The Fourier transform of $P_{j}(x, v, \tau)$ is given by,
$\tilde{P}_{j}(u, v, \tau)=\int_{-\infty}^{\infty} e^{-i u x} P_{j}(x, v, \tau) d x$
and the nuerse transform is given by

$$
P_{j}(x, v, \tau)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \tilde{P}_{j}(u, v, \tau) d u
$$

For the boundary condition

$$
\begin{aligned}
\tilde{P}_{j} & (u, v, 0)=\int_{-\infty}^{\infty} e^{-i u x} \theta(x) d x \\
& =\int_{0}^{\infty} e^{-i u x} d x \\
& =\frac{1}{i n}
\end{aligned}
$$

This is the result stated in the book. It is incorrect the correct answere is given by,

$$
\tilde{P}_{j}(u, v, 0)=\frac{1}{i u}+\delta(u) \pi
$$

Substituting the inverse transform into the equation for $P_{j}(x, u, \tau)$ gives

$$
\begin{aligned}
& P_{j}(x, v, \tau)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \tilde{P}_{j}(u, v, \tau) d u \\
& -\frac{\partial P_{j}}{\partial t}+\frac{v}{2} \frac{\partial^{2} P_{j}}{\partial x^{2}}-\left(\frac{1}{2}-j\right) v \frac{\partial P_{j}}{\partial x} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} P_{j}}{\partial v^{2}}+e \eta v \frac{\partial^{2} P_{j}}{\partial x \partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial P_{j}}{\partial v}=0
\end{aligned}
$$

The following derivatives are required,

$$
\begin{aligned}
\frac{\partial P_{j}}{\partial \tau} & =\frac{\partial}{\partial t} \frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \tilde{P}_{j} d u \\
& =\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial \tilde{P}_{j}}{\partial \tau} d u \\
\frac{\partial P_{j}}{\partial U} & =\frac{1}{\partial \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial \tilde{P}_{j}}{\partial U} d u \\
\frac{\partial^{2} P_{j}}{\partial v^{2}} & =\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial^{2} \tilde{P}_{j}}{\partial U} d u \\
\frac{\partial P_{j}}{\partial x} & =\frac{1}{2 \pi} \int_{-\infty}^{\infty} \frac{\partial}{\partial x} e^{i u x} \tilde{P}_{j} d u \\
& =\frac{1}{\partial \pi} \int_{-\infty}^{\infty} i u e^{i u x} \tilde{P}_{j} d u \\
\frac{\partial^{2} P_{j}}{\partial x^{2}} & =\frac{1}{\partial \pi} \int_{-\infty}^{\infty} \frac{\partial}{\partial x} i u e^{i u x} \tilde{P}_{j} d u
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2 \pi} \int_{-\infty}^{\infty}-u^{2} e^{i u x} \tilde{P}_{j} d u \\
\frac{\partial^{2} P_{j}}{\partial x \partial U} & =\frac{\partial}{\partial U} \frac{\partial P_{j}}{\partial x}=\frac{\partial}{\partial U} \frac{1}{2 \pi} \int_{-\infty}^{\Delta} i u e^{i u x} \tilde{P}_{j} \\
& =\frac{1}{\partial \pi} \int_{-\infty}^{\infty} u e^{j u x} \frac{\partial \tilde{P}_{j}}{\partial U} d u
\end{aligned}
$$

Putting things tgether gives,

$$
\begin{aligned}
& -\frac{\partial P_{j}}{\partial t}+\frac{v}{2} \frac{\partial^{2} P_{j}}{\partial x^{2}}-\left(\frac{1}{2}-j\right) v \frac{\partial P_{j}}{\partial x} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} P_{j}}{\partial v^{2}}+\rho \eta v \frac{\partial^{2} P_{j}}{\partial x \partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial P_{j}}{\partial v}=0
\end{aligned}
$$

$$
\begin{aligned}
& -\left[\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial \tilde{P}_{j}}{\partial \tau} d u\right] \\
& +\frac{v}{2}\left[\frac{1}{\partial \pi} \int_{-\infty}^{\infty}-u^{2} e^{i j x} \tilde{P}_{j} d u\right] \\
& -\left(\frac{1}{2}-j\right) v\left[\frac{1}{2 \pi} \int_{-\infty}^{\infty} i u e^{i u x} \tilde{P}_{j} d u\right] \\
& +\frac{1}{2} \eta^{2} v\left[\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}} d u\right] \\
& +e \eta v\left[\frac{1}{\partial \pi} \int_{-\infty}^{\infty} u e^{j u x} \frac{\partial \tilde{P}_{j}}{\partial v}\right] \\
& +\left(a-b_{j} v\right)\left[\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \frac{\partial \tilde{P}_{j}}{\partial u} d u\right] \\
& =0
\end{aligned}
$$

$$
\begin{aligned}
= & -\frac{\partial \tilde{P}_{j}}{\partial \tau}-\frac{1}{2} v u^{2} \tilde{P}_{j}-\left(\frac{1}{2}-j\right) v i u \tilde{P}_{j} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial U^{2}}+\rho \eta v u \frac{\partial \tilde{P}_{j}}{\partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial \tilde{P}_{j}}{\partial v}=0
\end{aligned}
$$

## Thus,

$$
\begin{aligned}
& -\frac{\partial \tilde{P}_{j}}{\partial \tau}-\frac{1}{2} v u^{2} \tilde{P}_{j}-\left(\frac{1}{2}-j\right) v i u \tilde{P}_{j} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial U^{2}}+\rho \eta v u \frac{\partial \tilde{P}_{j}}{\partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial \tilde{P}_{j}}{\partial v}=0
\end{aligned}
$$

Now let,

$$
\begin{gathered}
\alpha=-\frac{u^{2}}{2}-\frac{i u}{2}+i j u \\
\beta=\lambda-\rho \eta i-\rho n i u \\
\gamma=\frac{\eta^{2}}{2}
\end{gathered}
$$

Then

$$
\begin{aligned}
& -\frac{\partial \tilde{P}_{j}}{\partial \tau}-\frac{1}{2} v u^{2} \tilde{P}_{j}-\left(\frac{1}{2}-j\right) v i u \tilde{P}_{j} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\rho \eta v u \frac{\partial \tilde{P}_{j}}{\partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial \tilde{P}_{j}}{\partial v}=0 \\
& =-\frac{\partial \tilde{P}_{j}}{\partial \tau}+\left(-\frac{1}{2} v u^{2}-\frac{i u v}{2}+i u j v\right) \tilde{P}_{j} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\left(\rho \eta v u u+a-b_{j} v\right) \frac{\partial \tilde{P}_{j}}{\partial v}
\end{aligned}
$$

$$
\begin{aligned}
= & -\frac{\partial \tilde{P}_{j}}{\partial \tau}+\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+v\left(-\frac{u^{2}}{2}-\frac{i u}{2}\right. \\
& +i u j) \tilde{P}_{j}+v\left(e \eta i u-b_{j}\right) \frac{\partial \tilde{P}_{j}}{\partial v} \\
& +\frac{a \partial \tilde{P}_{j}}{\partial v}=0 \\
= & \frac{\partial \tilde{P}_{j}}{\partial \tau}+v\left[\frac{1}{2} \eta^{2} \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\left(-\frac{u^{2}}{2}-\frac{i u}{2}\right.\right. \\
& \left.+i u j) \tilde{P}_{j}+\left(e \eta i u-b_{j}\right) \frac{\partial \tilde{P}_{j}}{\partial v}\right] \\
& +a \frac{\partial \tilde{P}_{j}}{\partial v} \\
= & \frac{\partial \tilde{P}_{j}}{\partial \tau}+v\left[r \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\alpha \tilde{P}_{j}\right. \\
& \left.+\left(e \eta i u-b_{j}\right) \frac{\partial \tilde{P}_{j}}{\partial v}\right]+a \frac{\partial \tilde{P}_{j}}{\partial v}
\end{aligned}
$$

## Consider the term

recall that

$$
b_{j}=\lambda-j l \eta
$$

then

$$
\begin{aligned}
& e^{\eta} i u-\lambda+j e \eta \\
= & -(\lambda-e \eta i u-j e \eta)
\end{aligned}
$$

but

$$
\beta=\lambda-\rho \eta i-\rho n i u
$$

and the final result is detained

$$
\begin{aligned}
-\frac{\partial \tilde{P}_{j}}{\partial \tau} & +v\left[r \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\alpha \tilde{P}_{j}-\beta \frac{\partial \tilde{P}_{j}}{\partial v}\right] \\
& +a \frac{\partial \tilde{P}_{j}}{\partial v}=0
\end{aligned}
$$

$$
\begin{aligned}
&=v {\left[\alpha \tilde{P}_{j}-\beta \frac{\partial \tilde{P}_{j}}{\partial v}+\gamma \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}\right] } \\
&+a \frac{\partial \tilde{P}_{j}}{\partial v}-\frac{\partial \tilde{P}_{j}}{\partial \tau}=0
\end{aligned}
$$

Now assume that
$\tilde{P}_{j}(u, v, \tau)=$

$$
\begin{aligned}
& \tilde{P}_{j}(u, v, 0) \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\} \\
& =\frac{1}{i u} \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\}
\end{aligned}
$$

Now the derivatives of $\widetilde{P}_{j}(u, v, \tau)$ are given by
$\frac{\partial \tilde{P}_{j}}{\partial \tau}=\frac{1}{i u} \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\}$

$$
\left(\frac{\partial C j}{\partial \tau} \bar{v}+\frac{\partial D j v}{\partial \tau}\right)
$$

$$
\begin{aligned}
& =\left(\frac{\partial C_{j}}{\partial \tau}+\frac{\partial D_{j} v}{\partial \tau}\right) \tilde{P}_{j} \\
\frac{\partial \tilde{P}_{j}}{\partial v} & =\frac{1}{i u} \exp \left\{C_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\} D \\
& =D_{j} \tilde{P}_{j} \\
\frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}} & =D_{j}^{2} \tilde{P}_{j} \\
T h u s & \\
\frac{\partial \tilde{P}_{j}}{\partial \tau} & =\left(\frac{\partial C_{j}}{\partial \tau}+\frac{\partial D_{j} v}{\partial \tau}\right) \tilde{P}_{j} \\
\frac{\partial \tilde{P}_{j}}{\partial v} & =D_{j} \tilde{P}_{j} \\
\frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}} & =D_{j}^{2} \tilde{P}_{j}
\end{aligned}
$$

Inserting into the equation for $P_{j}$ gives

$$
\begin{aligned}
v & {\left[\alpha \tilde{P}_{j}-\beta \frac{\partial \tilde{P}_{j}}{\partial v}+\gamma \frac{\partial^{2} \tilde{P}_{j}}{\partial U^{2}}\right] } \\
+ & a \frac{\partial \tilde{P}_{j}}{\partial v}-\frac{\partial \tilde{P}_{j}}{\partial \tau}=0 \\
\Rightarrow v & {\left[\alpha \tilde{P}_{j}-\beta D_{j} \tilde{P}_{j}+\gamma D_{j}^{2} \tilde{P}_{j}\right]+a D_{j} \tilde{P}_{j} } \\
& -\left(\frac{\partial C_{j}}{\partial \tau} \bar{v}+\frac{\partial D_{j} v}{\partial \tau}\right) \tilde{P}_{j}=0 \\
\Rightarrow v & \left(\alpha-\beta D_{j}+\gamma D_{j}^{2}\right)+a D \\
& -\left(\frac{\partial C_{j}}{\partial \tau} \bar{v}+\frac{\partial D_{j} v}{\partial \tau}\right)=0
\end{aligned}
$$

Clearly this equation is solved if

$$
\begin{aligned}
v\left(\alpha-\beta D_{j}+\gamma D_{j}^{2}\right)+a D_{j} \\
=\left(\frac{\partial C}{\partial \tau} \bar{\nu}+\frac{\partial D_{j} v}{\partial \tau}\right)
\end{aligned}
$$

Consider

$$
\begin{aligned}
& \frac{\partial C_{j}}{\partial \tau}=\lambda D_{j} \\
& \frac{\partial D_{j}}{\partial \tau}=\alpha-\beta D_{j}+\gamma D_{j}^{2}
\end{aligned}
$$

then

$$
\begin{aligned}
\frac{\partial C}{\partial \tau} \bar{v} & +\frac{\partial D_{j} v}{\partial \tau} \\
& =\lambda D_{j} \bar{v}+\left(\alpha-\beta D_{j}+\gamma D_{j}^{2}\right) v
\end{aligned}
$$

Recall

$$
a=\lambda \bar{v}
$$

Then the desired result is obtained

$$
\begin{aligned}
\frac{\partial C j}{\partial \tau} \bar{v} & +\frac{\partial D_{j} v}{\partial \tau}= \\
& v\left(\alpha-\beta D_{j}+\gamma D_{j}^{2}\right)+a D
\end{aligned}
$$

Thus

$$
\begin{aligned}
& \frac{\partial C_{j}}{\partial \tau}=\lambda D_{j} \\
& \frac{\partial D_{j}}{\partial \tau}=\alpha-\beta D_{j}+\gamma D_{j}^{2}
\end{aligned}
$$

is a solution to

$$
\begin{aligned}
& v\left[\alpha \tilde{P}_{j}-\beta \frac{\partial \tilde{P}_{j}}{\partial v}+\gamma \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}\right] \\
& +a \frac{\partial \tilde{P}_{j}}{\partial v}-\frac{\partial \tilde{P}_{j}}{\partial \tau}=0
\end{aligned}
$$

If

$$
\begin{aligned}
\tilde{P}_{j}(u, v, \tau) & \\
& =\frac{1}{i u} \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\}
\end{aligned}
$$

Furtnure consider

$$
\alpha-\beta D_{j}+\gamma D_{j}^{2}=0
$$

It follows that the roots are

$$
\begin{aligned}
r_{ \pm} & =\frac{\beta \pm \sqrt{\beta^{2}-4 \alpha r}}{2 r} \\
& =\frac{\beta \pm d}{\eta^{2}}
\end{aligned}
$$

Since

$$
\gamma=\frac{\eta^{2}}{2}
$$

So, consider

$$
\begin{aligned}
& \left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)=\left[D_{j}-\frac{\beta+d}{2 r}\right]\left[D_{j}-\frac{\beta-d}{2 r}\right] \\
& =D_{j}^{2}-\frac{D_{j}(\beta+d)}{2 r}-D_{j}\left(\frac{\beta-d}{2 r}+\frac{(\beta+d)(\beta-d)}{4 r^{2}}\right. \\
& =D_{j}^{2}-\frac{\beta D_{j}}{r}+\frac{\beta^{2}-d^{2}}{4 r^{2}} \\
& =D_{j}^{2}-\frac{\beta D_{j}}{r} \frac{\beta^{2}-\beta^{2}+4 \alpha r^{2}}{4 r^{2}} \\
& =D_{j}^{2}-\frac{\beta D_{j}}{r}+\frac{\alpha}{r} \\
& =\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)=D_{j}^{2}-\frac{\beta D_{j}}{r}+\frac{\alpha}{r} \\
& \Rightarrow r\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)=r D_{j}^{2}-\beta D_{j}+\alpha
\end{aligned}
$$

It follows that

$$
\frac{\partial C_{j}}{\partial \tau}=\lambda D_{j}
$$

$$
\frac{\partial D_{j}}{\partial \tau}=r\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)
$$

Now the boundary condition is given by

$$
\tilde{P}_{i}(u, v, 0)=\frac{1}{i u}
$$

It follows that the boundary condition on $C_{j}(u, \tau)$ and $D,(u, \tau)$ is given by

$$
C_{j}(u, 0)=D_{j}(u, 0)=0
$$

The solution for the $D(u, \tau)$ equation is given by

$$
D_{j}(u, \tau)=r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}
$$

where

$$
g=\frac{r_{-}}{r_{t}} \quad \alpha=\sqrt{\beta^{2}-4 \alpha \gamma}
$$

This solution can be verified,

$$
\begin{aligned}
D_{j}-r_{+} & =r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}-r_{+} \\
& =\frac{r_{-}\left(1-e^{-d \tau}\right)-r_{+}\left(1-g e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)} \\
D_{j}-r_{-} & =\frac{r_{-}\left(1-e^{-d \tau}\right)-r_{-}}{\left(1-g e^{-d \tau}\right)} \\
& =\frac{r_{-}\left(1-e^{-d \tau}\right)-r_{-}\left(1-g e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}
\end{aligned}
$$

Now

$$
\begin{gathered}
\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)= \\
{\left[\frac{r_{-}\left(1-e^{-d \tau}\right)-r_{+}\left(1-g e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}\right]}
\end{gathered}
$$

$$
\begin{aligned}
& {\left[\frac{r_{-}\left(1-e^{-d \tau}\right)-r_{-}\left(1-g e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}\right]} \\
& =\frac{1}{\left(1-g e^{-d \tau}\right)^{2}}\left[r_{-}^{2}\left(1-e^{-d \tau}\right)^{2}\right. \\
& -r_{+}\left(1-g e^{-d \tau}\right) r_{-}\left(1-e^{d \tau}\right) \\
& -r_{-}\left(1-e^{-d \tau}\right) r_{-}\left(1-g e^{-d \tau}\right) \\
& \left.+r_{+}\left(1-g e^{-d \tau}\right) r_{-}\left(1-g e^{-d \tau}\right)\right] \\
& =\frac{1}{\left(1-g e^{-d \tau}\right)^{2}}\left[\begin{array}{r}
r_{-}^{2}\left(1-e^{-d \tau}\right)^{2} \\
-r_{+} r_{-}\left(1-g e^{-d \tau}\right)\left(1-e^{-d \tau}\right) \\
-r_{-}^{2}\left(1-g e^{d \tau}\right)\left(1-e^{-d \tau}\right) \\
\left.+r_{+} r_{-}\left(1-g e^{-d \tau}\right)^{2}\right] \\
\left\{r _ { - } ^ { 2 } \left[\left(1-e^{-d \tau}\right)^{2}-\right.\right. \\
\left.\left(1-g e^{-d \tau}\right)\left(1-e^{-d \tau}\right)\right]
\end{array}\right.
\end{aligned}
$$

$$
\begin{aligned}
& -r_{+} r_{-}\left[\left(1-g e^{-d \tau}\right)\left(1-e^{-d \tau}\right)\right. \\
& \left.\left.-\left(1-g e^{-d \tau}\right)^{2}\right]\right\} \\
& =\frac{1}{\left(1-g e^{-d \tau}\right)^{2}} \begin{array}{r}
\left\{r _ { - } ^ { 2 } ( 1 - e ^ { - d \tau } ) \left[\left(1-e^{-d \tau}\right)\right.\right. \\
\left.-\left(1-g e^{-d \tau}\right)\right] \\
-r_{+} r_{-}\left(1-g e^{-d \tau}\right)\left[\left(1-e^{-d \tau}\right)\right. \\
\left.\left.-\left(1-g e^{-d \tau}\right)\right]\right\}
\end{array} \\
& =\frac{1}{\left(1-g e^{-d \tau}\right)^{2}}\left\{r_{-}^{2}\left(1-e^{-d \tau}\right)\left(g e^{-d \tau}-e^{-d \tau}\right)\right. \\
& \left.-r_{+} r_{-}\left(1-g e^{-d \tau}\right)\left(g e^{-d \tau}-e^{-d \tau}\right)\right\} \\
& =\frac{\left(g e^{-d \tau}-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)^{2}}\left[r_{-}^{2}\left(1-e^{-d \tau}\right)\right. \\
& S^{n} \omega \\
& r_{+} \frac{r_{-}}{r_{+}}
\end{aligned}
$$

So,

$$
\begin{aligned}
& \frac{\left(g e^{-d \tau}-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)^{2}}\left[r_{-}^{2}\left(1-e^{-d \tau}\right)\right. \\
= & \frac{\left(g e^{-d \tau}-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)^{2}}\left(r_{-}^{2}-r_{-}^{2} e^{-d \tau} e^{-d \tau}-r_{-} r_{+}+r_{-}^{2} e^{-d \tau}\right) \\
= & \frac{\left(g e^{-d \tau}-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)^{2}}\left(r_{-}^{2}-r_{-} r_{+}\right) \\
= & \frac{e^{-d \tau}(g-1)}{\left(1-g e^{-d \tau}\right)^{2}}\left(r_{-}^{2}-r_{-} r_{+}\right) \\
= & \frac{e^{-d \tau}\left(r_{-}-r_{+}\right) r_{-}\left(r_{-}-r_{+}\right)}{r_{+}\left(1-g e^{-d \tau}\right)^{2}} \\
= & \frac{e^{-d \tau} r_{-}\left(r_{-}-r_{+}\right)^{2}}{r_{+}\left(1-g e^{-d \tau}\right)^{2}}
\end{aligned}
$$

$$
=\frac{g e^{-d \tau}\left(r_{-}-r_{+}\right)^{2}}{\left(1-g e^{-d \tau}\right)^{2}}
$$

Now

$$
r_{ \pm}=\frac{\beta \pm d}{\eta^{2}}
$$

so

$$
\begin{aligned}
r_{-}-r_{+} & =\frac{(\hat{\beta}-d)-(\hat{\beta}+d)}{\eta^{2}} \\
& =\frac{-2 d}{\eta^{2}}=\frac{-d}{r} \\
\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right) & =\frac{g e^{-d \tau}\left(r_{-}-r_{+}\right)^{2}}{\left(1-g e^{-d \tau}\right)^{2}} \\
& =\frac{d^{2} g e^{-d \tau}}{r^{2}\left(1-g e^{-d \tau}\right)^{2}}
\end{aligned}
$$

Next consider,

$$
\begin{aligned}
\frac{\partial D}{\partial \tau} j & =\frac{\partial}{\partial \tau}\left[r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}\right] \\
& =r_{-} \frac{\partial}{\partial \tau}\left[\frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}\right] \\
& =r_{-} \frac{\partial}{\partial \tau}\left[\frac{1}{\left(1-g e^{-d \tau}\right)}-\frac{e^{-d \tau}}{\left(1-g e^{-d \tau}\right)}\right] \\
& =r_{-}\left[\frac{-1}{\left(1-g e^{-d \tau}\right)^{2}}+\frac{d e^{-d \tau}}{\left(1-g e^{-d \tau}\right)}\right. \\
& \left.+\frac{e^{-d \tau}}{\left(1-g e^{-d \tau}\right)^{2}}\right] \\
& =r_{-}\left[\frac{-1}{\left(1-g e^{-d \tau}\right)^{2}}+\frac{d e^{-d \tau}\left(1-g e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)^{2}}\right. \\
& \left.+\frac{e^{-d \tau}}{\left(1-g e^{-d \tau}\right)^{2}}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{r_{-}}{\left(1-g e^{-d \tau}\right)^{2}}\left[\begin{array}{l}
-1+d e^{-d \tau}\left(1-g e^{-d \tau}\right) \\
\left.+e^{-d \tau}\right]
\end{array}\right. \\
& =\frac{r_{-} e^{-d \tau}}{\left(1-g e^{-d \tau}\right)^{2}}\left[\begin{array}{l}
-e^{d \tau}+d\left(1-g e^{-d \tau}\right) \\
+1]
\end{array}\right. \\
& =\frac{r_{-} e^{-d \tau}}{\left(1-g e^{-d \tau}\right)^{2}}\left[-e^{d \tau}-d g e^{-d \tau}+d+1\right] \\
& =\frac{r_{-} e^{-d \tau}}{\left(1-g e^{-d \tau}\right)^{2}}\left[1-e^{d \tau}+d\left(1-g e^{-d \tau}\right)\right]
\end{aligned}
$$

Recall

$$
\begin{array}{r}
r_{-}-r_{+}=\frac{-d}{r} \\
S=\frac{r}{r_{+}}
\end{array}
$$

so

$$
\begin{aligned}
1-e^{d \tau} & +d\left(1-g e^{-d \tau}\right) \\
& =1-e^{d \tau}+\left(r_{-}-r_{+}\right) \gamma\left[1-\frac{r_{-}}{r_{+}} e^{-d \tau}\right] \\
& =1-e^{d \tau}+\gamma\left[r_{-}-r_{+}-\frac{r_{-}^{2}}{r_{+}}\right.
\end{aligned}
$$

Right now I do not see how this will work out. Will return later.

Assuming

$$
D_{j}(u, \tau)=r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}
$$

It follows that

$$
\frac{\partial C}{\partial \tau} j=\lambda D_{j}
$$

with the intitial cordition of $c_{j}(u, 0)=D_{j}(u, 0)=0$ integrating gives,

$$
\begin{aligned}
& c_{j}(u, \tau)=\lambda \int_{0}^{\tau} D_{j}(u, s) d s \\
& =\lambda \int_{0}^{\tau} r_{-} \frac{\left(1-e^{-d s}\right)}{\left(1-g e^{-d s}\right)} d s \\
& =\lambda r-\int_{0}^{\tau} \frac{1}{1-g e^{-d s}}-\frac{e^{-d s}}{1-s^{e-d s}} d s
\end{aligned}
$$

$$
\begin{aligned}
=\lambda r & \int_{0}^{\tau} \frac{1}{1-g e^{-d s}} d s \\
& -\lambda r-\int_{0}^{\tau} \frac{e^{-d s}}{1-g e^{-d s}} d s
\end{aligned}
$$

Consider the second integral

$$
\int_{0}^{\tau} \frac{e^{-d s}}{1-g e^{-d s}} d s
$$

let

$$
\begin{aligned}
u & =1-g e^{-d s} \\
d u & =g d e^{-d s} d s \\
\Rightarrow \frac{d u}{g^{d}} & =e^{-d s} d s
\end{aligned}
$$

then

$$
\begin{aligned}
\int_{0}^{\tau} & \frac{e^{-d s}}{1-g e^{-d s}} d s \\
& =\frac{1}{g d} \int_{1-g}^{1-g e^{-d \tau}} \frac{d u}{u} \\
& =\left.\frac{1}{g d} \ln u\right|_{1-g} ^{1-g e^{-d \tau}} \\
& =\frac{1}{g d}\left[\ln \left(1-g e^{-d \tau}\right)-\ln (1-g)\right] \\
& =\frac{1}{g d} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)
\end{aligned}
$$

Now for the first integral

$$
\begin{aligned}
& \int_{0}^{\tau} \frac{1}{1-g e^{-d s}} d s=\int_{0}^{\tau} \frac{e^{d s}}{e^{d s}\left(1-g e^{-d s}\right)} d s \\
& =\int_{0}^{\tau} \frac{e^{d s}}{\left(e^{d s}-g\right)} d s
\end{aligned}
$$

let

$$
\begin{aligned}
& u=e^{d s}-g \\
& d u=d e^{d s} d s \Rightarrow \frac{d u}{d}=e^{d s} d s \\
& \int_{0}^{\tau} \frac{1}{1-g e^{-d s}} d s=\frac{1}{d} \int_{1-g}^{e^{d \tau}}-g \frac{d u}{u} \\
& =\left.\frac{1}{d} \ln u\right|_{1-g} ^{e^{d \tau}-s} \\
& =\frac{1}{d}\left[\ln \left(e^{d \tau}-g\right)-\ln (1-g)\right]
\end{aligned}
$$

$$
=\frac{1}{d} \ln \left(\frac{e^{d \tau}-g}{1-g}\right)
$$

putting things together

$$
\begin{aligned}
& \lambda \int_{0}^{\tau} r_{-} \frac{\left(1-e^{-d s}\right)}{\left(1-g e^{-d s}\right)} d s \\
= & \lambda r_{-}\left\{\frac{1}{d} \ln \left(\frac{e^{d \tau}-g}{1-g}\right)-\right. \\
& \left.\frac{1}{g d} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\} \\
= & \frac{\lambda r}{d}\left\{\ln \left[e^{d \tau}\left(\frac{1-g e^{-d \tau}}{1-g}\right)\right]\right. \\
& \left.-\frac{1}{g} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}
\end{aligned}
$$

$$
=\frac{\lambda r_{-}}{d}\left\{\ln e^{d \tau}+\left(1-\frac{1}{g}\right) \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}
$$

Now

$$
S=\frac{r_{-}}{r_{+}}
$$

so

$$
1-\frac{1}{g}=1-\frac{r_{+}}{r_{-}}=\frac{1}{r_{-}}\left(r_{-}-r_{+}\right)
$$

but

$$
r_{-}-r_{+}=-\frac{2 d}{\eta^{2}}
$$

so

$$
\begin{aligned}
C_{j}(u, \tau) & =\frac{\lambda r}{d}\left\{d \tau-\frac{2 d}{r_{-} \eta^{2}} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\} \\
& =\lambda\left\{r_{-} \tau-\frac{2}{\eta^{2}} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}
\end{aligned}
$$

## Thus

$$
c_{1}(u, \tau)=\lambda\left\{r_{-\tau}-\frac{2}{\eta^{2}} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}
$$

Now $P_{j}(x, v, \tau)$ can be computed Since

$$
\begin{aligned}
\tilde{P}_{j}(u, v, \tau) & \\
& =\frac{1}{i u} \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\}
\end{aligned}
$$

and

$$
P_{j}(x, v, \tau)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} e^{i u x} \tilde{P}_{j}(u, v, \tau) d u
$$

This integral can be partially cualuated using Residue theory from complex integration.

The result dotained is

$$
\begin{aligned}
& P_{j}(x, v, \tau)=\frac{1}{2}+ \\
& \frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{e^{i u x} \tilde{P}_{j}(u, v, \tau)\right\} d u \\
&=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac { 1 } { i u } \operatorname { e x p } \left[C_{j}(u, \tau) \bar{u}+\right.\right. \\
&\left.\left.D_{j}(u, \tau) v+i u x\right]\right\} d u
\end{aligned}
$$

This integral can be evaluated using methods such as

1) Exponetally - Fitted Eauss-Laguerre Quadrature
https://hpcquantlib. wordpress.com/2020/05/17/optimized-heston-model-integration-exponentialıy-fitted-gauss-iaguerre-quadrature-rūle/
2) Fourier - Gauss-Laguere and Fourier - cosine series
https://lup.lub.lu.se/luur/download?
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-180.jpg?height=43&width=900&top_left_y=1898&top_left_x=259)

## Heston Model Characteristic Function

The characteristic fonction for the option to be in the money is defined by,

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}} \mid x_{t}=0\right]
$$

where $x_{t}=0 \Rightarrow F_{t}=K$
Recall the expression for a European option

$$
C(x, u, \tau)=k\left[e^{x} P_{1}(x, u, \tau) \cdot P_{0}(x, u, \tau)\right]
$$

The $P_{0}(x, v, \tau)$ is interepreted as the probability that the asset price is greater than the strike price. It follows that the probability that the log strike price at option expirity is greater tran the strike price is given by

$$
P\left(x_{\tau}>x\right)=P_{0}(x, 0, \tau)
$$

$$
\begin{gathered}
=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\Delta} \operatorname{Re}\left\{\frac { 1 } { i u } \operatorname { e x p } \left[C_{0}(u, \tau) \bar{v}+\right.\right. \\
\left.\left.D_{0}(u, \tau) v+i u x\right]\right\} d u
\end{gathered}
$$

where

$$
\begin{aligned}
& x=\ln \frac{F_{t}}{K} \quad x_{T}=\ln \frac{S_{T}}{K} \\
& \tau=T-t
\end{aligned}
$$

and define the log-strike by

$$
k=\ln \frac{k}{F_{t}}=-x
$$

The probebility density function

$$
\begin{aligned}
P(k) & =\frac{\partial P_{6}}{\partial x} \frac{d x}{d k} \\
& =-\frac{\partial P_{0}}{\partial R}
\end{aligned}
$$

$$
\begin{gathered}
=\frac{-\partial}{\partial R}\left\{\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac { 1 } { i u ^ { \prime } } \operatorname { e x p } \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+\right.\right.\right. \\
\left.\left.\left.D_{0}\left(u^{\prime}, \tau\right) v-i u^{\prime} k\right]\right\} d u^{\prime}\right\} \\
=\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\operatorname { e x p } \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v\right.\right. \\
\left.\left.-i u^{\prime} k\right]\right\} d u
\end{gathered}
$$

Now
$\operatorname{Re}\left\{\exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v-i u^{\prime} k\right]\right\}$
$=\frac{1}{2}\left\{\exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v-i u^{\prime} k\right]\right. +\exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v-i u^{\prime} k\right]^{*} \xi$
$\frac{1}{2}\left\{\exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) U-i u^{\prime} k\right]\right.$

$$
\left.+\exp \left[C_{0}^{*}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}^{*}\left(u^{\prime}, \tau\right) v+i u^{\prime} k\right]\right\}
$$

50

$$
\begin{aligned}
P(k)= & \frac{1}{2 \pi} \int_{0}^{\Delta}\left\{\operatorname { e x p } \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v\right.\right. \\
& \left.-i u^{\prime} k\right]+\exp \left[C_{0}^{*}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}^{*}\left(u^{\prime}, \tau\right) v\right. \\
& \left.\left.+i u^{\prime} k\right]\right\} d u^{\prime}
\end{aligned}
$$

Consider the second term
$\int_{0}^{\Delta} \exp \left[C_{0}^{*}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}^{*}\left(u^{\prime}, \tau\right) v+i u^{\prime} k\right] d u^{\prime}$
For both $C_{0}^{*}\left(u^{\prime}, \tau\right)$ and $D_{0}^{*}\left(u^{\prime}, \tau\right)$ the imaginary part has the form

## cú

so making the change of variable

$$
u^{\prime \prime}=-u^{\prime}
$$

gives the integral
$\int_{0}^{\infty} \exp \left[C_{0}^{*}\left(u^{\prime}, \tau\right) \bar{u}+D_{0}^{*}\left(u^{\prime}, \tau\right) v+i u^{\prime} k\right] d u^{\prime}$
$=-\int_{0}^{-A} \exp \left[C_{0}\left(u^{\prime \prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime \prime}, \tau\right) v-i u^{\prime \prime} k\right] d u^{\prime \prime}$
$=\int_{-\infty}^{0} \exp \left[C_{0}\left(u^{\prime \prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime \prime}, \tau\right) U_{-} i u^{\prime \prime} k\right] d u^{\prime \prime}$
putting things together gives

$$
\begin{aligned}
p(k)= & \frac{1}{2 \pi}\left\{\int _ { 0 } ^ { A } \operatorname { e x p } \left[C_{0}\left(u^{\prime}, r\right) \bar{U}+D_{0}\left(u^{\prime}, r\right) v\right.\right. \\
& \left.-i u^{\prime} k\right]+\int_{-\infty}^{0} \exp \left[C_{0}\left(u^{\prime \prime}, r\right) \bar{U}+D_{0}\left(u^{\prime \prime}, r\right) v\right. \\
& \left.\left.-i u^{\prime \prime} k\right] d u^{\prime \prime}\right\} \\
= & \frac{1}{2 \pi} \int_{-\infty}^{\infty} \exp \left[C_{0}\left(u^{\prime}, r\right) \bar{U}+D_{0}\left(u^{\prime}, r\right) v\right. \\
& \left.-i u^{\prime} k\right] d u^{\prime}
\end{aligned}
$$

Now

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}} \mid x_{t}=0\right]
$$

$$
\begin{gathered}
=\int_{-\infty}^{\infty} p(k) e^{i u k} d k \\
=\int_{-\infty}^{\infty}\left\{\frac { 1 } { 2 \pi } \int _ { - \infty } ^ { \infty } \operatorname { e x p } \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v\right.\right. \\
\left.\left.-i u^{\prime} k\right] d u^{\prime}\right\} e^{i u k} d k \\
=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v\right] \\
e^{i\left(u-u^{\prime}\right) k} d k d u^{\prime} \\
=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) v\right] \\
\int_{-\infty}^{\infty} e^{i\left(u-u^{\prime}\right) k} d k d u^{\prime}
\end{gathered}
$$

But

$$
\int_{-\infty}^{\infty} e^{i\left(u-u^{\prime}\right) k} d k=2 \pi \delta\left(u-u^{\prime}\right)
$$

it follows that

$$
\begin{aligned}
\Phi_{T}(R)= & \int_{-\infty}^{\infty} \exp \left[C_{0}\left(u^{\prime}, \tau\right) \bar{U}+D_{0}\left(u^{\prime}, \tau\right) U\right] \\
& \delta\left(u-u^{\prime}\right) d u \\
= & \exp \left[C_{0}(u, \tau) \bar{U}+D_{0}(u, \tau) v\right]
\end{aligned}
$$

Thus

$$
\Phi_{T}(R)=\exp \left[C_{0}(u, \tau) \bar{v}+D_{0}(u, \tau) v\right]
$$

Before soing furtur the results obtained thus far are sumarized

## Executive Summary

In the previous section the solution of the Heston equation for European Call options was computed. The result is complicated with several variable changes there the results are summarized.

The colatility model is given by,

$$
d S_{t}=\mu_{t} S_{t} d t+\sqrt{v_{t}} S_{t} d z_{1}
$$

$d v=\alpha\left(s_{t}, v_{t}, t\right) d t+\eta \beta\left(s_{t}, v_{t}, t\right) \sqrt{v_{t}} d z_{2}$

$$
\left\langle d z_{1} d z_{2}\right\rangle=\rho d t
$$

where $s_{t}$ is the asset price, $v$ is the variance of $s_{t}$, is the correlation belween $s_{t}$, $v_{t}, u_{t}$ is the orift of stock
price retworns which is deterministic. $e$ is the correlation between $s_{t}$, $v_{t} \alpha$ and $\beta$ are arbitrary functions of $s_{t}, v_{t}$ and $t$ and $\eta$ is the standard deviation of the variance of $s_{t}, v_{t}$.
Assuming this model an option on the underlying asset $S_{t}$, denoted by $v$, salisfies the differential equation,

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} v S^{2} \frac{\partial^{2} v}{\partial S^{2}}+\frac{1}{2} \eta^{2} \beta^{2} v \frac{\partial^{2} v}{\partial v^{2}} \\
& +e^{v s \eta \beta \frac{\partial^{2} v}{\partial s \partial v}}-r v+r s \frac{\partial v}{\partial s} \\
& =-(\alpha-\varphi \beta \sqrt{v}) \frac{\partial v}{\partial v}
\end{aligned}
$$

The Heston model is obtained by assuming

$$
\begin{gathered}
\alpha(s, v, t)=-\lambda(v-\bar{v}) \\
\beta(s, v, t)=1
\end{gathered}
$$

to obtain,

$$
\begin{gathered}
\frac{d s_{t}=\mu_{t} s_{t} d t+\sqrt{v_{t}} s_{t} d z_{1}}{d v_{t}=-\lambda\left(v_{t}-\bar{v}\right) d t+\eta \sqrt{v_{t}} d z_{2}} \\
\left\langle d z_{1}, d z_{2}\right\rangle=\rho d t
\end{gathered}
$$

Here $\bar{v}$ is the mean of $v_{t}$, which is constant and $\lambda$ is the rate that $v$ is driven to $\bar{v}$. Note that if $v_{t} \bar{v}>0$ this term will decrease $v_{t}$ ant if $v_{t}-\bar{v}<0$ the term will inarease $v_{t}$.

The solution for curopean call obtions is obtained by making the change of variables

$$
x=\ln \frac{F_{t}}{k} \quad \tau=T \cdot t
$$

where $K$ is the option strike price, $T$ is the option expiry and $F_{t}$ is the forward asset price defined by

$$
F_{t}=s_{t} \exp \left\{\int_{t}^{T} u(s) d s\right\}
$$

where $\mu(t)$ is the asset price deterministic drift letting

$$
c(x, v, \tau)
$$

denote the option price, the option price PDE becomes.

$$
\begin{aligned}
& -\frac{\partial c}{\partial \tau}+\frac{v_{t}}{2} \frac{\partial^{2} c}{\partial x^{2}}-\frac{v_{t}}{2} \frac{\partial c}{\partial x}+\frac{1}{2} \eta^{2} v_{t} \frac{\partial^{2} c}{\partial v_{t}^{2}} \\
& +e \eta v_{t} \frac{\partial^{2} c}{\partial v_{t} \partial x}-\lambda\left(v_{t}-\bar{v}\right) \frac{\partial c}{\partial v_{t}}=0
\end{aligned}
$$

Assuming

$$
C(x, v, \tau)=k\left[e^{x} P_{1}(x, v, \tau) \cdot P_{0}(x, v, \tau)\right]
$$

which has the form of the Black-Sholes solution.
substituting into the equation for $c(x, v, t)$ gives for $j=0,1$

$$
\begin{aligned}
& -\frac{\partial P_{j}}{\partial t}+\frac{v}{2} \frac{\partial^{2} P_{j}}{\partial x^{2}}-\left(\frac{1}{2}-j\right) v \frac{\partial P_{j}}{\partial x} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} P_{j}}{\partial v^{2}}+\rho \eta v \frac{\partial^{2} P_{j}}{\partial x \partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial P_{j}}{\partial v}=0
\end{aligned}
$$

with the boundary condition

$$
\lim _{\tau \rightarrow 0} P_{j}(x, v, \tau)=\theta(x)
$$

where $\theta(x)$ is the Heavyside function,

This equation is solved using Fourier transforms,

$$
\tilde{P}_{j}(u, v, \tau)=\int_{-\infty}^{\infty} P_{j}(x, v, \tau) e^{-i u x} d x
$$

with

$$
\tilde{P}_{j}(u, v, 0)=\frac{1}{i u}
$$

Substituting into the equation for $P_{j}$ gives

$$
\begin{aligned}
& -\frac{\partial \tilde{P}_{j}}{\partial \tau}-\frac{1}{2} v u^{2} \tilde{P}_{j}-\left(\frac{1}{2}-j\right) v<u \tilde{P}_{j} \\
& +\frac{1}{2} \eta^{2} v \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}+\rho \eta v u \frac{\partial \tilde{P}_{j}}{\partial v} \\
& +\left(a-b_{j} v\right) \frac{\partial \tilde{P}_{j}}{\partial v}=0
\end{aligned}
$$

where

$$
a=\lambda \bar{v} \quad b_{j}=\lambda-j e_{\eta}
$$

Next let,

$$
\begin{gathered}
\alpha=-\frac{u^{2}}{2}-\frac{i u}{2}+i j u \\
\beta=\lambda-\rho \eta i-\rho n i u \\
\gamma=\frac{\eta^{2}}{2}
\end{gathered}
$$

then the equation for $\tilde{P}_{j}(u, v, \tau)$ becomes,

$$
\begin{aligned}
& v\left[\alpha \tilde{P}_{j}-\beta \frac{\partial \tilde{P}_{j}}{\partial v}+r^{2} \frac{\partial^{2} \tilde{P}_{j}}{\partial v^{2}}\right] \\
& +a \frac{\partial \tilde{P}_{j}}{\partial v}-\frac{\partial \tilde{P}_{j}}{\partial \tau}=0
\end{aligned}
$$

Next assume

$$
\begin{aligned}
\tilde{P}_{j}(u, v, \tau) & = \\
\frac{1}{i u} & \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\}
\end{aligned}
$$

Then, substitution into the above equation gives equations for $C$ and $D$,

$$
\begin{gathered}
\frac{\partial C_{j}}{\partial \tau}=\lambda D_{j} \\
\frac{\partial D_{j}}{\partial \tau}=r\left(D_{j}-r_{+}\right)\left(D_{j}-r_{-}\right)
\end{gathered}
$$

where,

$$
\begin{aligned}
r_{ \pm} & =\frac{\beta \pm \sqrt{\beta^{2}-4 \alpha \gamma}}{2 \gamma} \\
& =\frac{\beta \pm d}{\eta^{2}}
\end{aligned}
$$

with the boundary condition

$$
C(u, 0)=D(u, 0)=0
$$

The solution to these equations is given by

$$
D_{j}(u, \tau)=r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)}
$$

$c_{j}(u, \tau)=\lambda\left\{r_{-} \tau-\frac{2}{\eta^{2}} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}$
where

$$
g=\frac{r_{1}}{r_{t}}
$$

It follows that the inverse Fourier transform is given by

$$
\begin{aligned}
& P_{j}(x, v, \tau)=\frac{1}{\partial \pi} \int_{-\infty}^{\infty} e^{i u x} \\
& \frac{1}{i u} \exp \left\{c_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) v\right\} d u
\end{aligned}
$$

This equation is solved using the Gil-Palaez Inversion formula which is derived in a later section.
$P_{j}(x, u, \tau)=$

$$
\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac { 1 } { i u } \operatorname { e x p } \left[C_{j}(u, \tau) \bar{u}+\right.\right.
$$

$$
\left.\left.D_{j}(u, \tau) v+i u x\right]\right\} d u
$$

This integral can be solved using numerical methods.

The characteristic fonction for the option to be in the money is defined by

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}} \mid x_{t}=0\right]
$$

where $x_{t}=0 \Rightarrow F_{t}=K$
is found to be

$$
\Phi_{T}(R)=\exp \left[C_{0}(u, \tau) \bar{v}+D_{0}(u, \tau) v\right]
$$

## Digression: Complex Analysis

Consider a complex number,

$$
z=x+i y=121\left(\cos \varphi_{1}+i \sin \varphi_{1}\right)
$$

graphically,
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-199.jpg?height=590&width=890&top_left_y=759&top_left_x=330)

The argument of $z$ is defined by

$$
\arg 2=\varphi
$$

$\arg 2$ is a muttioalued function since $q+2 \pi n, n=0,1,2, \ldots$
is valid for a given value of 2 . The principal value of the argument of $z$ is defined

$$
\operatorname{Arg} z=\varphi_{1}
$$

is single valued and satisfies

$$
\begin{aligned}
& -\pi<\operatorname{Arg} z<\pi \\
& \arg z=\operatorname{Arg} z+2 \pi n
\end{aligned}
$$

Argz can written as a function $\operatorname{crg}^{2}$

$$
\operatorname{Arg} z=\arg z+2 \pi\left[\frac{1}{2}-\frac{\arg z}{2 \pi}\right]
$$

where $[x]$ is the greatest integer function which is the largest integer less tran $x$.

$$
x-1<[x] \leqslant x
$$

This relationship can be verified by considering a few examples,

$$
\begin{gathered}
\arg (z)=2 \pi+\pi \quad \arg (z)=2 \pi+\frac{\pi}{4} \\
\arg (z)=2 \pi
\end{gathered}
$$

It follows that

1) $\left[\frac{1}{2}-\frac{2 \pi+\pi}{2 \pi}\right]=\left[\frac{1}{2}-1-\frac{1}{2}\right]=\left[\frac{1}{2}-\frac{3}{2}\right]$

$$
\begin{aligned}
& =[-1]=-1 \\
& \operatorname{Arg}(z)=3 \pi-2 \pi=\pi
\end{aligned}
$$

$$
\text { 2) } \begin{aligned}
{\left[\frac{1}{2}-\frac{2 \pi+\pi / 4}{2 \pi}\right]=\left[\frac{1}{2}-1-\frac{1}{8}\right]=\left[\frac{4}{8} \cdot \frac{9}{8}\right] } \\
=\left[\frac{5}{8}\right]=-1 \\
\operatorname{Arg}(2)=(2 \pi+\pi / 4)-2 \pi \\
=\pi / 4
\end{aligned}
$$

3) $\left[\frac{1}{2}-\frac{2 \pi+3 \pi / 2}{2 \pi}\right]=\left[\frac{1}{2}-1-\frac{3}{4}\right]=\left[\frac{1}{2}-\frac{7}{4}\right]$

$$
=\left[-\frac{5}{4}\right]=-2
$$

$$
\begin{aligned}
\operatorname{Arg}(z) & =2 \pi+\frac{3 \pi}{2}-4 \pi \\
& =\frac{3}{2} \pi-2 \pi \\
& =-\frac{\pi}{2}
\end{aligned}
$$

Some properties of argz are given

1) $\arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)$
2) $\arg \left(\frac{z_{1}}{z_{2}}\right)=\arg \left(z_{1}\right)-\arg \left(z_{2}\right)$
3) $\arg \left(\frac{1}{2}\right)=\arg \overline{2}=-\arg 2$

Since $\arg ^{(2)}$ is multi-valued equality is set equality where the set of all values are identical,

$$
\begin{gathered}
\arg (z)=\{\varphi, \varphi+2 \pi, \varphi-2 \pi, \varphi+4 \pi, \\
\varphi-4 \pi, \ldots\}
\end{gathered}
$$

Now for (1) using

$$
\begin{aligned}
& z_{1}=\left|z_{1}\right| e^{i \arg \left(z_{1}\right)} \\
& z_{2}=\left|z_{2}\right| e^{i \arg \left(z_{2}\right)}
\end{aligned}
$$

$$
\begin{aligned}
& z_{1} z_{2}=\left|z_{1}\right|\left|z_{2}\right| e^{i\left[\arg \left(z_{1}\right)+\arg \left(z_{2}\right)\right]} \\
\Rightarrow & \arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)
\end{aligned}
$$

For (2)

$$
\frac{z_{1}}{z_{2}}=\frac{\left|z_{1}\right| e^{i \arg \left(z_{1}\right)}}{\left|z_{2}\right| e^{i \arg \left(z_{2}\right)}}
$$

$$
\begin{array}{r}
=\frac{\left|z_{1}\right|}{\left|z_{2}\right|} e^{i\left[\arg \left(z_{1}\right)-\arg \left(z_{2}\right)\right]} \\
\Rightarrow \arg \left(\frac{z_{1}}{z_{2}}\right)=\arg \left(z_{1}\right)-\arg \left(z_{2}\right)
\end{array}
$$

For (3)

$$
\begin{aligned}
& \frac{1}{z}=\frac{1}{|z| e^{i \arg (z)}}=\frac{1}{|z|} e^{-i \arg (z)} \\
\Rightarrow & \arg \left(\frac{1}{z}\right)=-\arg (z)
\end{aligned}
$$

Next set equality will be verified
for

$$
\arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)
$$

Now

$$
z_{1} z_{2}=\left|z_{1}\right| e^{i \arg \left(z_{1}\right)}\left|z_{2}\right| e^{i \arg \left(z_{2}\right)}
$$

and

$$
\begin{aligned}
& \arg \left(z_{1}\right)=\operatorname{Arg}\left(z_{1}\right)+2 \pi n_{1} \\
& \arg \left(z_{2}\right)=\operatorname{Arg}\left(z_{2}\right)+2 \pi n_{2}
\end{aligned}
$$

50

$$
12,1 e^{i\left[\operatorname{Arg}\left(z_{1}\right)+2 \pi n_{1}\right]}=12,1 e^{i \operatorname{Arg}\left(z_{1}\right)} e^{i 2 \pi n}
$$

but for every $n$,

$$
e^{i 2 \pi n_{1}}=1
$$

50

$$
z_{1} z_{2}=\left|z_{1} z_{2}\right| e^{i\left[\operatorname{Arg}\left(z_{1}\right)+\operatorname{Arg}\left(z_{2}\right)\right]}
$$

it follows that

$$
\arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)+2 \pi n_{12}
$$

where $n_{12}$ is an arbitrary integer

Now

$$
\begin{aligned}
\arg \left(z_{1}\right) & +\arg \left(z_{2}\right)=\operatorname{Arg}\left(z_{1}\right)+2 \pi n_{1} \\
& +\operatorname{Arg}\left(z_{2}\right)+2 \pi n_{2} \\
=\operatorname{Arg}\left(z_{1}\right) & +\operatorname{Arg}\left(z_{2}\right)+2 \pi\left(n_{1}+n_{2}\right)
\end{aligned}
$$

since $n_{12}, n_{1}$ and $n_{2}$ are arbitrary

$$
\arg \left(z_{1} z_{2}\right)=\arg \left(z_{1}\right)+\arg \left(z_{2}\right)
$$

Next consider

$$
\arg (z z)=\arg (z)+\arg (z)
$$

is the following true

$$
\begin{aligned}
\arg (z z) & =\arg (z)+\arg (z) \\
& \stackrel{?}{=} 2 \arg (z)
\end{aligned}
$$

Now

$$
z^{2}=\left|z^{2}\right| e^{i 2 \arg \left(z^{2}\right)}
$$

$$
=\left|z^{2}\right| e^{i 2 \operatorname{Arg}\left(z^{2}\right)}
$$

50

$$
\arg \left(z^{2}\right)=2 \operatorname{Arg}\left(z^{2}\right)+2 \pi n
$$

but

$$
\begin{aligned}
\arg (z) & =2[\operatorname{Arg}(z)+2 \pi n] \\
& =2 \operatorname{Arg}(z)+4 \pi n
\end{aligned}
$$

Thus every other element of darg ( 2 ) is contained in $\arg \left(2^{2}\right)$.
It follows that $2 \mathrm{crg}(2)$ is a subset of $\arg \left(2^{2}\right)$ but not equal to it.
Similarly,

$$
\begin{aligned}
\arg (1) & =\arg \left(z_{1}\right)-\arg \left(z_{2}\right) \\
& \neq 0
\end{aligned}
$$

$m$ terms

$$
\begin{aligned}
\arg \left(z^{m}\right) & =\arg (z)+\arg (z)+\cdots+\arg (z) \\
& \neq \operatorname{marg}(z)
\end{aligned}
$$

The complex logarithm is defined as follows,

Let

$$
z=e^{\omega}
$$

where 2 is a complex number. If

$$
\omega=u+i v
$$

then

$$
|z| e^{i \arg z}=e^{u} e^{i v}
$$

it follows that

$$
|z|=e^{u} \quad v=\arg (z)
$$

From the first equation

$$
u=\ln |z|
$$

It follows that

$$
\begin{aligned}
\omega & =\ln |z|+i \arg (z) \\
& =\ln |z|+i[\operatorname{Arg}(z)+2 \pi n]
\end{aligned}
$$

This defines the complex logarithm and is writen as

$$
\omega=\ln z
$$

This definition is multivalued.
The principal value of $\ln z$ is denoted by $\ln z$ and denoted
by

$$
\ln (z)=\ln |z|+i \operatorname{Arg}(z)
$$

where

$$
-\pi<\operatorname{Arg}(z) \leqslant \pi
$$

This extends the loganthm to the complex plane, note that
there is a singularity at $z=0$.

This definition allows logarithm with negative arguments,

$$
\ln (-1)=i \pi
$$

also,

$$
\ln (z)=\ln (z)+2 \pi i n
$$

Some properties of the complex logarithm are,

1) $e^{\ln 2}=e^{\ln |z|} e^{i \operatorname{Arg}(z)} e^{2 \pi i n}$

$$
\begin{aligned}
& =|z| e^{i \operatorname{Arg}(z)} \\
& =z
\end{aligned}
$$

2) For $z=x+i y \Rightarrow e^{z}=e^{x} e^{i y}$

$$
\ln \left(e^{2}\right)=\ln \left|e^{x}\right|+\operatorname{larg}\left(e^{2}\right)
$$

$$
\begin{aligned}
& =x+i(y+2 \pi n) \\
& =x+i y+i 2 \pi n \\
& =2+i 2 \pi n
\end{aligned}
$$

## Contow Integrals

To understand the problem consider the contour integral in the complex plane,

$$
\oint f(z) d z
$$

If the cowntour is parameterized by $z(t)$ with end points $a$ and b
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-212.jpg?height=527&width=718&top_left_y=1015&top_left_x=439)
then

$$
\oint f(z) d z=\int_{a}^{b} f(z(t)) z^{\prime}(t) d t
$$

Consider the contow integral of $f(z)=z^{2}$ over the half unit circle in the complex plane,
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-213.jpg?height=618&width=751&top_left_y=441&top_left_x=390)

It follows that

$$
\begin{aligned}
z(\varphi) & =e^{i \varphi} \\
z^{\prime}(\varphi) & =i e^{i \varphi} \\
\oint f(z) d z & =\int_{0}^{\pi} z^{2}(\varphi) z^{\prime}(\varphi) d \varphi \\
& =\int_{0}^{\pi}\left(e^{i \varphi}\right)^{2}\left(i e^{i \varphi}\right) d \varphi
\end{aligned}
$$

$$
\begin{aligned}
& =\int_{0}^{\pi} i e^{3 i \varphi} d \varphi \\
& =\left.\frac{i}{3 i} e^{3 i \varphi}\right|_{0} ^{\pi} \\
& =\frac{1}{3}\left(e^{3 i \pi}-1\right) \\
& =-\frac{2}{3}
\end{aligned}
$$

## Cauchy Integral Formula

![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-214.jpg?height=652&width=693&top_left_y=1118&top_left_x=378)

The cauchy integral formula
states that for an analytic function in the regron defined by C,

$$
f(z)=\frac{1}{2 \pi i} \oint_{c} \frac{f(\omega)}{\omega-z} d \omega
$$

As an example consider the function

$$
f(0)=1
$$

Where $C$ is the unit circle centered at the origin.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-215.jpg?height=458&width=583&top_left_y=1197&top_left_x=453)

From the Cauchy integral formula

$$
1=\frac{1}{2 \pi i} \oint_{c} \frac{1}{\omega} d \omega
$$

The curve parameterization gives

$$
\omega=e^{i \varphi} \Rightarrow d \omega=i e^{i \varphi} d \varphi
$$

it follows that

$$
\begin{aligned}
& \oint_{C} \frac{1}{\omega} d \omega=\int_{0}^{2 \pi} i \frac{e^{i \varphi}}{e^{c \varphi}} d \varphi \\
& =i \int_{0}^{2 \pi} d \varphi=i 2 \pi
\end{aligned}
$$

Trus

$$
\frac{1}{2 \pi i} \oint_{c} \frac{1}{\omega} d \omega=1
$$

verifying the cauchy formula. Cauchy Integral Theorem
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-217.jpg?height=521&width=642&top_left_y=84&top_left_x=445)

The Cauchy-Integral Theorem states that for any analytic fundion (i.e. a function with a convergent power series which implies that it is infinetly differentiable. ) that a closed path integral satifies,

$$
\oint f(z) d z=0
$$

Intuititively, for a closed path the endpoints of the integral are the same so

$$
\oint f^{\prime}(z) d z=f\left(z_{1}\right)-f\left(z_{2}\right)=0
$$

We are now in a position to evaluate the the contour integral of the complex loganthm

Consider the integral

$$
\oint_{c} \frac{1}{z} d z
$$

where
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-218.jpg?height=691&width=735&top_left_y=904&top_left_x=406)
parameterizing 2 gives,

$$
\begin{aligned}
z=r e^{i \theta} & \Rightarrow d z=i r e^{i \theta} \\
\oint_{c} \frac{1}{z} d z & =\int_{-\pi}^{\pi} \frac{i r e^{i \theta}}{r e^{i \theta}} d \theta \\
& =\int_{-\pi}^{\pi} i d \theta \\
& =2 \pi i \\
& \neq 0
\end{aligned}
$$

This seems to be in contratiction to the Cauchy integral theorem since

$$
\oint_{c} \frac{1}{z} d z=\log z_{2}-\log z_{1}
$$

Previolesly it was shown that the logarithm of a complex number, 2 , is given by

$$
\ln z=\ln |z|+i \arg (z)
$$

which is a multi-valued function and the cause of the problem since in the complex plane $e^{0}$ and $e^{i 2 \pi}$ are the same point.
The way out of the problem is to regard $e^{0}$ and $e^{i 2 \pi}$ as different points. This is accomplished with the Riemann surface.

Assume that the complex plane is in the plane of the page.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-220.jpg?height=480&width=639&top_left_y=1219&top_left_x=405)

The negative real axis is refered to as the branch cut. Imagire that $e^{0}$ and $e^{i 2 \pi}$ are in
different planes. In each plane make a cut alons the branch cut and bend the portion above the axis up and and the portion below the axis down while the plane flops into the third dimension to form surfaces as shown below,
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-221.jpg?height=380&width=561&top_left_y=955&top_left_x=556)
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-221.jpg?height=384&width=561&top_left_y=1418&top_left_x=558)
connecting the upper and lower portions of the surfaces
produces the continuous spiral shown below, called the Riemann surface,
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-222.jpg?height=936&width=809&top_left_y=576&top_left_x=376)

For a complex numbe $z=121 e^{i \varphi}$ increasing $\varphi$ moves up along the imaginary axis and decreasing q moves down. Thus $e^{i 2 n k}$ is on a different surface for
each value of $k$.
Integrating $1 / 2$ around a closed follows the shaded portion of the surface as shown below
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-223.jpg?height=554&width=807&top_left_y=519&top_left_x=420)

It follows that the integral is over a branch of the Riemann surface thus

$$
\begin{aligned}
\int_{e^{i \pi}}^{e^{i \pi}} \frac{1}{2} & d z=\left.\ln z\right|_{e^{-i \pi}} ^{e^{i \pi}}=i \pi-(-i \pi) \\
& =2 \pi i
\end{aligned}
$$

## Simulation of The Heston Process

Recall the Heston process is given by

$$
\begin{gathered}
d s=\mu s d t+\sqrt{v} s d z_{1} \\
d v=-\lambda(v-\bar{v}) d t+\eta \sqrt{v} d z_{2} \\
\left\langle d z_{1} d z_{2}\right\rangle=\rho d t
\end{gathered}
$$

Discretation of the process leads to the equations,

$$
\begin{aligned}
& d S=S_{n+1}-S_{n} \\
& d U=U_{n+1}-U_{n} \\
& d Z_{1}=Z_{1} \Delta t \\
& d Z_{2}=Z_{2} \Delta t
\end{aligned}
$$

where

$$
\begin{aligned}
& z_{1} \sim \operatorname{Normal}(0,1) \\
& z_{2} \sim \operatorname{Normal}(0,1)
\end{aligned}
$$

$$
\left\langle z_{1}, z_{2}\right\rangle=l
$$

it follows that
$S_{n+1}=S_{n}+\mu S_{n} \Delta t+\sqrt{U}_{n} S_{n} Z_{1} \sqrt{\Delta t}$
$v_{n+1}=v_{n}-\lambda\left(v_{n}-\bar{v}\right) \Delta t+\eta \sqrt{v_{n}} z_{2} \sqrt{\Delta t}$
The problem with this discretation is that it can lead to negative values for $v_{n+1}$.

There are two approaches to dealing with this.

1) Absorbtion

If $v<0$ then $v=0$
2) Reflection

If $v<0$ then $v=-v$
A better approach is describled in next section.

## Milstein Discretization

Milstein discretiration is dotained by including a second order term in discretiration mode.
The result obtained is,

$$
\begin{aligned}
v_{n+1}= & v_{n}-\lambda\left(v_{n} \cdot \bar{v}\right) \Delta t+\eta \sqrt{v_{n}} \sqrt{\Delta t} z_{2} \\
& +\frac{\eta^{2}}{4} \Delta t\left(z_{2}^{2}-1\right) \\
= & v_{n}-\lambda\left(v_{n}-\bar{v}\right) \Delta t+\eta \sqrt{v_{i}} \sqrt{\Delta t} z_{2} \\
& +\frac{\eta^{2}}{4} \Delta t z_{2}^{2}-\frac{\eta^{2}}{4} \Delta t \\
= & v_{n}+\eta \sqrt{v_{i}} \sqrt{\Delta t} z_{2}+\frac{\eta^{2}}{4} \Delta t z_{2}^{2} \\
& -\lambda\left(v_{n}-\bar{v}\right) \Delta t-\frac{\eta^{2}}{4} \Delta t
\end{aligned}
$$

$$
\begin{aligned}
= & \left(\sqrt{v_{n}}+\frac{\eta}{2} \sqrt{\Delta t} z_{2}\right)^{2}-\lambda\left(v_{n}-\bar{v}\right) \Delta t \\
& -\frac{\eta^{2}}{4} \Delta t
\end{aligned}
$$

Consider the case $v_{n}=0$, then if

$$
\begin{aligned}
& \lambda \bar{v}-\frac{\eta^{2}}{4} \geqslant 0 \\
\Rightarrow & \lambda \bar{v} \geqslant \frac{\eta^{2}}{4} \\
\Rightarrow & \frac{4 \lambda \bar{v}}{\eta^{2}} \geqslant 1
\end{aligned}
$$

It follows that

$$
\begin{aligned}
v_{n+1}=\left(\frac{n}{2} \sqrt{\Delta t} z_{2}\right)^{2} & +\lambda \bar{v} \Delta t \\
-\frac{\eta^{2}}{4} \Delta t & \geqslant 0
\end{aligned}
$$

Even if the mequality fails negative negative values of unti are still far less likely but possible, so reflection or absorbtion of negtive values must still be implimented.

A better discretization of the asset price can be dotained by using the Black-Sholes solution,

$$
\begin{aligned}
& s_{t}=s_{0} \exp \left[\mu t-\frac{1}{2} v_{t} t+\sqrt{v_{t}} z_{1}\right] \\
\Rightarrow & \frac{s_{t}}{s_{0}}=\exp \left[\mu t-\frac{1}{2} v_{t} t+\sqrt{v_{t}} z_{1}\right] \\
\Rightarrow & \ln \frac{s_{t}}{s_{0}}=\mu t-\frac{v_{t} t+\sqrt{v_{t}} z_{1}}{2}
\end{aligned}
$$

let

$$
x_{t}=\ln \frac{s_{t}}{s_{0}}
$$

then

$$
x_{t}=\mu t-\frac{v_{t}}{2} t+\sqrt{v_{t}} z_{1}
$$

If $v_{t}$ is assume known at time $t$ it follows that

$$
d x_{t}=\left(\mu-\frac{v_{t}}{2}\right) d t+{\sqrt{v_{t}}} d z_{1}
$$

Discretizing this model gives
$x_{n}=x_{n-1}+\left(\mu-\frac{v_{n}}{2}\right) \Delta t+\sqrt{v_{t} \Delta t} Z_{1}$
where 2,~Normal (0,1)
Thus the discrete odatility model is given by
$x_{n}=x_{n-1}+\left(\mu-\frac{v_{n}}{2}\right) \Delta t+\sqrt{v_{t} \Delta t} Z_{1}$

$$
\begin{gathered}
v_{n+1}=\left(\sqrt{v_{n}}+\frac{\eta}{2} \sqrt{\Delta t} z_{2}\right)^{2}-\lambda\left(v_{n}-\bar{v}\right) \Delta t \\
-\frac{\eta^{2}}{4} \Delta t
\end{gathered}
$$

## Implied Volatity Surface

Recall that the local volatility is defined as the volatility of the Fokker-Plank equation written in terms of the forward price,

$$
\frac{\partial C}{\partial T}\left(F_{0}, K, T\right)=\frac{1}{2} U_{L}\left(K, T ; S_{0}\right) K^{2} \frac{\partial^{2} C}{\partial K^{2}}
$$

It follows that,

$$
v_{L}\left(K, T ; S_{0}\right)=\frac{\frac{\partial C}{\partial K}}{\frac{K^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}}
$$

Also, recall that the optron price at exerase is defined by,

$$
C\left(F_{0}, K, T\right)=\int_{K}^{\infty} \varphi\left(F_{T}, T ; S_{0}\right)\left(F_{T}-K\right) d F_{T}
$$

Where $\varphi\left(F_{T}, T ; S_{0}\right)$ is the probability density of realizing $F_{T}$ at time $T$.

It follows that the probability that the option is in the money is given by,

$$
\frac{\partial c}{\partial k}=-\int_{k}^{\Delta} q\left(F_{T}, T ; F_{0}\right) d F_{T}
$$

and the probability density that the option is in the money is given by,

$$
\frac{\partial^{2} c}{\partial K^{2}}=\varphi\left(K, T ; F_{0}\right)
$$

The implied volatility $\sigma_{B S}\left(K, T ; S_{0}\right)$ by

$$
C\left(S_{0}, K, T\right)=C_{B S}\left(S_{0}, K, \sigma_{B S}\left(K, T ; S_{0}\right), T\right)
$$

where $C_{B S}$ is the Black-Sholes option price.
The implied vobatility and local volatility are related by
$U_{L}\left(K, T, S_{0}\right)=E\left[O_{B S}^{2}\left(S_{T}, T ; S_{0}\right) \mid S_{T}=K\right]$

Recall, that the forward price is given by

$$
F_{t}=S_{t} \exp \left[\int_{t}^{T} \mu(s) d s\right]
$$

In the following analysis it is assumed that $\mu=0$. It follows that,

$$
F_{t}=S_{t}
$$

## undestanding Implied Odatility

Here a general path-integral representation of Black Sholes implied variance is derived. Assume the asset satisfies the

$$
d s_{t}=\mu_{t} s_{t} d t+\sigma_{t} s_{t} d z_{t}
$$

For fixed $K$ and $T$, define the Black-Sholes gamma

$$
\Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right)=\frac{\partial^{2}}{\partial S_{t}^{2}} C_{B S}\left(S_{t}, K, \bar{\sigma}(t), T t\right)
$$

furthur define the Black-Sholes forward implied variance

$$
U_{k, T}(t)=\frac{E\left[\sigma_{t}^{2} S_{t}^{2} \Gamma_{B S}\left(S_{t}, \sigma(t)\right) \mid \mathcal{F}_{0}\right]}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}, \sigma(t) \mid \mathcal{F}_{0}\right]\right.}
$$

where

$$
\bar{\sigma}^{2}(t)=\frac{1}{T-t} \int_{t}^{T} v_{k, T}(u) d u
$$

Consider a function of the form $f\left(s_{t}, t\right)$. From the Ito formula,

$$
d f=\frac{\partial f}{\partial s_{t}} d s_{t}+\frac{\partial f}{\partial t} d t+\frac{1}{2} \frac{\partial^{2} f}{\partial s_{t}^{2}}\left(d s_{1}\right)^{2}
$$

If $u_{t}=0$ then,

$$
\begin{aligned}
d S_{t} & =\sigma S_{t} d Z_{t} \\
\left(d S_{t}\right)^{2} & =\sigma^{2} S_{t}^{2}\left(d Z_{t}\right)^{2} \\
& =\sigma^{2} S_{t}^{2} d t
\end{aligned}
$$

So
$d f=\frac{\partial f}{\partial S_{t}} d S_{t}+\frac{\partial f}{\partial t} d t+\frac{1}{\partial} \sigma^{2} S_{t}^{2} \frac{\partial^{2} f}{\partial S_{t}^{2}} d t$

Integrating gives

$$
\begin{aligned}
& \int_{0}^{T} d f=\int_{0}^{T}\left\{\frac{\partial f}{\partial S_{t}} d S_{t}+\frac{\partial f}{\partial t} d t\right. \\
& \left.+\frac{1 \sigma^{2} S_{t}^{2} \frac{\partial^{2} f}{\partial S_{t}^{2}} d t}{\partial}\right\} d t \\
& =f\left(S_{T}, T\right)-f\left(S_{0}, 0\right)
\end{aligned}
$$

Consider the option $C\left(S_{0}, K, T\right)$. Recall that the nondiscounted value of a call option is given by the expectation of the final payoff woder the risk nuetral measure

$$
C\left(S_{0}, K, T\right)=E\left[\left(S_{T}-K\right)^{+} \mid \mathcal{F}_{0}\right]
$$

Now a $t=T$

$$
C_{B S}\left(S_{T}, K, \bar{\delta}(T), 0\right)=\left(S_{T}-K\right)^{+}
$$

$$
\begin{aligned}
& \text { So, } \\
& E\left[\left(S_{T}-K\right)^{+} \mid \mathcal{F}_{0}\right] \\
& =E\left[C_{B S}\left(S_{T}, K, \bar{\sigma}(T), 0\right) \mid \mathcal{F}_{0}\right] \\
& \text { let } \\
& f\left(S_{t}, t\right)=C_{B S}\left(S_{t}, K, \bar{\sigma}(t), T-t\right) \\
& \text { using } \\
& f\left(S_{T}, T\right)-f\left(S_{0}, 0\right)= \\
& \int_{0}^{T}\left\{\frac{\partial f}{\partial S_{t}} d S_{t}+\frac{\partial f}{\partial t} d t\right. \\
& \text { Sues }
\end{aligned}
$$

$$
\begin{gathered}
C_{B S}\left(S_{T}, K, \bar{\sigma}(T), 0\right)=C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \\
+\int_{0}^{T}\left\{\frac{\partial C_{B S}}{\partial S_{t}} d S_{t}+\frac{\partial C_{B S}}{\partial t} d t\right. \\
\left.+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}} d t\right\}
\end{gathered}
$$

It follows that

$$
\begin{aligned}
E[ & {\left[C_{B S}\left(S_{T}, K, \bar{\sigma}(T), 0\right) \mid \mathcal{F}_{0}\right] } \\
=E & {\left[C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right)+\int_{0}^{T}\left\{\frac{\partial C_{B S}}{\partial S_{t}} d S_{t}\right.\right.} \\
& \left.\left.+\frac{\partial C_{B S}}{\partial t} d t+\frac{1}{2} \sigma_{t}^{2} S_{t}^{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}} d t\right\} \mid \mathcal{F}_{0}\right] \\
=E & {\left[C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \mid \mathcal{F}_{0}\right]+} \\
& E\left[\left.\int_{0}^{T} \frac{\partial C_{B S}}{\partial S_{t}} d S_{t} \right\rvert\, \mathcal{F}_{0}\right]+
\end{aligned}
$$

$$
E\left[\left.\int_{0}^{T}\left(\frac{\partial C_{3 S}}{\partial t}+\frac{1}{2} \sigma_{t}^{2} S_{t}^{2} \partial^{2} \frac{C_{B S}}{\partial S_{t}^{2}}\right) d t \right\rvert\, \tilde{J}_{0}\right]
$$

Now for the first term since $t$ is the $t=0$ value it follows that

$$
\begin{array}{r}
E\left[C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \mid \mathcal{F}_{0}\right] \\
=C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right)
\end{array}
$$

For the second

$$
E\left[\left.\int_{0}^{T} \frac{\partial C_{B S}}{\partial S_{t}} d S_{t} \right\rvert\, \tilde{J}_{0}\right]
$$

since $S_{t}$ is a martigale it follows that an integral of a function of $s_{t}$ is a martigate. Thus the expectation is a constant which is assumed to be zero

So.

$$
E\left[\left.\int_{0}^{T} \frac{\partial C_{B S}}{\partial S_{t}} d S_{t} \right\rvert\, \tilde{f}_{0}\right]=0
$$

Bringing trings together gives

$$
\begin{aligned}
& E\left[C_{B S}\left(S_{T}, K, \bar{\delta}(T), 0\right) \mid \mathcal{F}_{0}\right] \\
= & C_{B S}\left(S_{0}, K, \bar{\delta}(0), T\right) \\
+ & E\left[\left.\int_{0}^{T}\left(\frac{\partial C_{B S}}{\partial t}+\frac{1}{2} \sigma_{t}^{2} S_{t}^{2} \partial^{2} \frac{C_{B S}}{\partial S_{t}^{2}}\right) d t \right\rvert\, \tilde{J}_{0}\right]
\end{aligned}
$$

Now for zero interest and no dividends the Black-Sholes equation for CBS becomes

$$
\frac{\partial C_{B S}}{\partial t}=-\frac{1}{\partial} \sigma^{2} S_{t}^{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}}
$$

Let

$$
\sigma^{2}=U_{k, T}
$$

so that

$$
\frac{\partial C_{B S}}{\partial t}=-\frac{1}{2} U_{K, T} S_{t}^{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}}
$$

It follows that

$$
\begin{aligned}
E & {\left[C_{B S}\left(S_{T}, K, \bar{\sigma}(T), 0\right) \mid \mathcal{F}_{0}\right] } \\
& =C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \\
+E & {\left[\int_{0}^{T}\left[\left.\frac{S_{t}^{2}}{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}}\left(O_{t}^{2}-U_{k_{T}}(t)\right) d t \right\rvert\, \tilde{J}_{0}\right]\right.}
\end{aligned}
$$

In words this equation gives the expected realized profit on the sale of a call option at implied volatility of $\bar{\sigma}(0)$, detta-hedged using the deterministic forward
variance function $V_{K, T}$ when the actual realized volatility is $\sigma_{t}$.

The term $C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right)$ is the original sale price of the option and the second term returns from the replicating portfolio.
Now from the definition of $U_{K, T}$

$$
\begin{aligned}
& E\left[C_{B S}\left(S_{T}, K, \bar{\sigma}(T), 0\right) \mid \mathcal{F}_{0}\right] \\
& =C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \\
& +E\left[\int_{0}^{T}\left[\left.\frac{S_{t}^{2}}{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}}\left(O_{t}^{2}-U_{k_{T}}(t)\right) d t \right\rvert\, \tilde{J}_{0}\right]\right. \\
& =C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right) \\
& +E\left[\int_{0}^{T}\left[\left.\frac{S_{t}^{2}}{2} \frac{\partial^{2} C_{B S}}{\partial S_{t}^{2}}\left(O_{t}^{2}-U_{k_{T}}(t)\right) d t \right\rvert\, \tilde{J}_{0}\right]\right.
\end{aligned}
$$

$$
\begin{aligned}
=C_{B S} & \left(S_{0}, K, \sigma(0), T\right) \\
+ & \int_{0}^{T}\left\{\frac{1}{2} E\left[\left.\sigma^{2} S_{t}^{2} \frac{\partial C_{B S}}{\partial S_{t}^{2}} \right\rvert\, \mathcal{F}_{0}\right]\right. \\
& \left.-\frac{1}{2} E\left[\left.\bar{U}_{K T}(t) S_{t}^{2} \frac{\partial C_{B S}}{\partial S_{t}^{2}} \right\rvert\, \mathcal{F}_{0}\right]\right\} d t
\end{aligned}
$$

Now using

$$
\Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right)=\frac{\partial^{2}}{\partial S_{t}^{2}} C_{B S}\left(S_{t}, K, \bar{\sigma}(t), T-t\right)
$$

and since $\bar{U}_{K T}(t)$ is deterministic it follows that

$$
\begin{aligned}
\int_{0}^{T} & \left\{\frac{1}{2} E\left[\left.\sigma_{t}^{2} s_{t}^{2} \frac{\partial C_{B s}}{\partial s_{t}^{2}} \right\rvert\, z_{0}\right]\right. \\
& \left.-\frac{1}{2} E\left[\left.\bar{U}_{k T}(t) s_{t}^{2} \frac{\partial C_{B s}}{\partial s_{t}^{2}} \right\rvert\, \tilde{J}_{0}\right]\right\} d t \\
& =\int_{0}^{T} \frac{1}{2}\left\{E \left[s_{t}^{2} \sigma_{t}^{2} \Gamma_{B s}\left(s_{t}, \bar{\sigma}(t) \mid \widetilde{J}_{0}\right]\right.\right.
\end{aligned}
$$

$$
-\bar{U}_{k T}(t) E\left[S_{t}^{2} \Gamma_{B s}\left(S_{t}, \bar{\sigma}(t) \mid \mathcal{F}_{0}\right]\right\} d t
$$

but from the definition of $\cup_{K_{1} T}$

$$
\begin{aligned}
& E\left[s_{t}^{2} \Gamma_{B s}\left(s_{t}, \bar{\sigma}(t) \mid \widetilde{J}_{0}\right] U_{k_{1} T}(t)\right. \\
& \quad=E\left[\sigma_{t}^{2} s_{t}^{2} \Gamma_{B s}\left(s_{t}, \bar{\sigma}(t)\right) \mid \widetilde{J}_{0}\right]
\end{aligned}
$$

Thus

$$
C\left(S_{0}, K, T\right)=C_{B S}\left(S_{0}, K, \bar{\sigma}(0), T\right)
$$

From this expression it follows that by noting that the implied variance at $T$ is $\sigma_{B S}(K, T)$

$$
\begin{aligned}
\sigma_{B S}^{2} & \left(K_{1} T\right)=\bar{\sigma}^{2}(0) \\
& =\frac{1}{T} \int_{0}^{T} \frac{E\left[\sigma_{t}^{2} S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid J_{0}\right]}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid \mathcal{F}_{0}\right]} d t \\
& =\frac{1}{T} \int_{0}^{T} U_{k, T}(t) d t
\end{aligned}
$$

Thus the implied variance is expressed as the expected instantaneas variance under some probability measure.

It is seen that this definition is intended to remove the possibility of arbitrage on variance.

Now this expression can be expressed in a nicer form using the Radon-Nikodym derivative Let

$$
\begin{aligned}
\sigma_{B S} & \left(K_{1} T\right)^{2}=\bar{\sigma}(0)^{2} \\
& =\frac{1}{T} \int_{0}^{T} E^{C}\left[\sigma_{t}^{2}\right] d t
\end{aligned}
$$

Where $E^{6}$ is the expectation of $\sigma_{t}^{2}$ with respect to the probability measure $G_{t}$ defined relative tr the pricing measure $P$, by the Radon-Nikodym derivative.

$$
\frac{d E}{d P}=\frac{S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right)}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(0)\right) \mid \mathcal{J}_{0}\right]}
$$

Consider the case $\sigma_{t}=\sigma(t)$ is a deterministic of only $t$.

Then

$$
\begin{aligned}
U_{K T}(t) & =\frac{E\left[\sigma_{t}^{2} S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid \mathcal{F}_{0}\right]}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid \mathcal{F}_{0}\right]} \\
& =\sigma^{2}(t) \frac{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid \mathcal{F}_{0}\right]}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}\right) \mid \mathcal{F}_{0}\right]} \\
& =\sigma^{2}(t)
\end{aligned}
$$

As a comparison consider the expectation under the risk-neutral measure

$$
E^{p}\left[f\left(s_{t}\right)\right]=\int p\left(s_{t}, t ; s_{0}\right) f\left(s_{1}\right) d s_{t}
$$

recall that the risk-newtral POF is given by

$$
p\left(s_{t}, t ; s_{0}\right)=\left.\frac{\partial^{2} C}{\partial K^{2}}\right|_{K=s_{t}}
$$

Now the relation between the the $G$ measure and the risk-nautral measure is given by

$$
\begin{aligned}
v_{k, T} & =E^{C}\left[\sigma_{t}^{2}\right] \\
& =E^{P}\left[\sigma_{t}^{2} \frac{d G_{t}}{d D}\right] \\
& =\int q\left(S_{t}: S_{0}, K, T\right) E^{P}\left[\sigma_{t}^{2} \mid S_{t}\right]
\end{aligned}
$$

Recall that the local variance is defined by

$$
V_{L}\left(K, T, S_{0}\right)=E^{P}\left[\sigma_{t}^{2} \mid S_{T}=K\right]
$$

It follows that
$v_{K, T}=\int v_{L}\left(K, T, S_{0}\right) q\left(S_{t}: S_{0}, K, T\right) d S_{t}$
Let

$$
q\left(s_{t}: s_{0}, k, T\right)=\frac{P\left(s_{t}, t ; s_{0}\right) s_{t}^{2} \Gamma_{B s}\left(s_{t}\right)}{E\left[s^{2} \Gamma_{B s}\left(s_{t}\right) \mid \mathcal{F}_{0}\right]}
$$

This density has the form of a brownian bridge density. write the integral in terms of the los stock price,

$$
x=\ln \frac{s_{t}}{s_{0}}
$$

so that
$U_{K T}(t)=\int q\left(x_{t}, t ; x_{T}, T\right) U_{L}\left(x_{t}, t\right) d x_{t}$
Numerical solutions for $U_{k T}(t)$
show that pecks dong a line between, denoted by, $\bar{x}_{t}$ joining the stock price today with the strike price at expiration. Moreover the density appears symetric about the line. This metruates an expansion around the $\bar{x}_{t}$ which is a peak where the derivative of $q\left(x_{t}, t ; x_{T}, T\right)$ with respect to $X_{t}$ is zero, so

$$
\begin{aligned}
q\left(x_{t}, t ; x_{T}, T\right) & \approx q\left(\bar{x}_{t}, t ; x_{T}, T\right) \\
& +\left.\frac{1}{2}\left(x_{t}-\bar{x}_{t}\right)^{2} \frac{\partial^{2} q}{\partial x_{t}^{2}}\right|_{x_{t}=\bar{x}_{t}}
\end{aligned}
$$

Numerical experiments also show that $U_{L}\left(x_{t}, t\right)$ is near linear in $x_{t}$ in the same area where $q\left(x_{t}, t ; x_{t}, T\right)$ is significant, so

$$
\begin{aligned}
U_{L}\left(x_{t}, t\right) \approx & U_{L}\left(\bar{x}_{t}, t\right) \\
& +\left.\left(x_{t}-\bar{x}_{t}\right) \frac{\partial U_{L}}{\partial x_{t}}\right|_{x_{t}=\bar{x}_{t}}
\end{aligned}
$$

substituting into the expression for $v_{k T}(t)$ gius

$$
\begin{aligned}
v_{k T}(t)= & \int q\left(x_{t}, t ; x_{T}, T\right) v_{L}\left(x_{t}, t\right) d x_{t} \\
\approx \int & {\left[q\left(\bar{x}_{t}, t ; x_{T}, T\right)\right.} \\
& \left.+\left.\frac{1}{2}\left(x_{t}-\bar{x}_{t}\right)^{2} \frac{\partial^{2} q}{\partial x_{t}^{2}}\right|_{x_{t}=\bar{x}_{t}}\right] \\
& {\left[\begin{array}{l}
v_{L}\left(\bar{x}_{t}, t\right) \\
+\left.\left(x_{t}-\bar{x}_{t}\right) \frac{\partial v_{L}}{\partial x_{t}}\right|_{x_{t}=\bar{x}_{t}}
\end{array}\right] d x_{t} }
\end{aligned}
$$

neglecting the linear and quadratic terms gives

$$
\begin{aligned}
& \approx \int q\left(\bar{x}_{t}, t ; x_{T}, \tau\right) v_{L}\left(\bar{x}_{t}, t\right) d x_{t} \\
& \approx u_{L}\left(\bar{x}_{t}, t\right) \int q\left(\bar{x}_{t}, t ; x_{T}, \tau\right) d x_{t} \\
& \approx u_{L}\left(\bar{x}_{t}, t\right)
\end{aligned}
$$

Trus

$$
U_{K T}(t) \approx U_{L}\left(\bar{x}_{t}, t\right)
$$

It follows from the definition of implied forward variance

$$
\begin{aligned}
\sigma_{B S}(k, T)^{2} & =\frac{1}{T} \int_{0}^{T} U_{k T}(u) d u \\
& \approx \frac{1}{T} \int_{0}^{T} U_{L}\left(\bar{x}_{t}, u\right) d u
\end{aligned}
$$

Thus the Black-Sholes implied volatility is approximately related to the local odatility by

$$
\sigma_{B S}(K, T)^{2} \approx \frac{1}{T} \int_{0}^{T} U_{L}\left(\bar{x}_{t}, u\right) d u
$$

where $U_{L}\left(K, T ; S_{0}\right)$ is computed from,

$$
v_{L}\left(k, T ; S_{0}\right)=\frac{\frac{\partial C}{\partial K}}{\frac{k^{2}}{2} \frac{\partial^{2} C}{\partial k^{2}}}
$$

Local volatility in the Heston Model

Recall the Heston model is given by

$$
\begin{gathered}
d s_{t}=\mu_{t} s_{t} d t+\sqrt{v_{t}} s_{t} d z_{1} \\
d v_{t}=-\lambda\left(v_{t}-\bar{v}\right) d t+\eta \sqrt{u} d z_{2}
\end{gathered}
$$

where

$$
\left\langle d z_{1} d z_{2}\right\rangle=e d t
$$

First, with

$$
x_{t}=\ln \frac{S_{t}}{K}
$$

and using that the asset proe satisfies

$$
s_{t}=s_{0} \exp \left[\mu t-\frac{1}{2} v_{t} t+\overline{v_{t}} z_{1}\right]
$$

let $\mu=0$ and $s_{0}=K$ then

$$
\begin{aligned}
\ln \frac{S_{t}}{K} & =-\frac{V_{t} t}{2}+\sqrt{V_{t}} Z_{1} \\
& =x_{t}
\end{aligned}
$$

If $v_{t}$ is assumed fixed then

$$
d x_{t}=-\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z_{1}
$$

Next, consider consider the relation

$$
\Rightarrow \quad \begin{aligned}
& \left\langle d z_{1} d z_{2}\right\rangle=e^{d t} \\
& d z_{2}=e d z_{1}
\end{aligned}
$$

If $z_{2}$ is decomposed into ortagonal random variables, (i.e. uncorrelated random variables), 2, and $\omega$
where

$$
\operatorname{Cov}(2, \omega)=0
$$

## Now asswe

$$
d z_{2}=e^{d z_{1}+a d \omega}
$$

Where $a$ is determined so that the variance is equal to the variance of $z_{2}$, it follows that

$$
\operatorname{var}\left(d z_{2}\right)=d t
$$

and since $z_{1}$ and $w$ are uncorrelated

$$
\begin{aligned}
\operatorname{var} & \left(\rho d z_{1}+a d \omega\right)=e^{2} \operatorname{Uar}\left(d z_{1}\right) \\
+ & a^{2} \operatorname{Uar}(d \omega) \\
= & \left(e^{2}+a^{2}\right) d t
\end{aligned}
$$

It follows that

$$
\begin{aligned}
e^{2}+a^{2} & =1 \Rightarrow a^{2}=1-e^{2} \\
\Rightarrow a & =\sqrt{1-e^{2}}
\end{aligned}
$$

Thus

$$
d z_{2}=e d z_{1}+\sqrt{1-e^{2}} d \omega
$$

It follows the $d z_{z}$ can be eliminated from the equation for $v_{t}$,

$$
\begin{aligned}
d v_{t}= & \lambda\left(v_{t}-\bar{v}\right) d t+\eta \bar{U}_{t} d Z_{z} \\
= & -\lambda\left(v_{t}-\bar{v}\right) d t \\
& +\eta \bar{U}_{t}\left(e d Z_{1}+\sqrt{1-e^{2}} d \omega\right)
\end{aligned}
$$

let $d z_{1} \rightarrow d z$ so that the Heston model becomes,

$$
\begin{aligned}
d x_{t}= & -\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z \\
d v_{t}= & -\lambda\left(v_{t}-\bar{v}\right) d t+\eta \rho \sqrt{v_{t}} d z \\
& +\eta \sqrt{1-e^{2}} \sqrt{v_{t}} d \omega
\end{aligned}
$$

Next $d z$ can be eliminated since

$$
\sqrt{U_{t}} d z=d x_{t}+\frac{1}{\partial} U_{t} d t
$$

So,

$$
\begin{aligned}
d v_{t}= & \lambda\left(v_{t}-\bar{v}\right) d t+\eta \rho\left(d x_{t}+\frac{1}{2} v_{t} d t\right) \\
& +\eta \sqrt{v}_{t} \sqrt{1-\rho^{2}} d \omega
\end{aligned}
$$

The strategy will be to compute local variances using the Heston model and then integrate local variance from the valuation date to the expration date to approximate the BS implied varrance using

$$
\sigma_{B S}(K, T)^{2} \approx \frac{1}{T} \int_{0}^{T} U_{L}\left(\bar{x}_{t}, u\right) d u
$$

Now consider

$$
\begin{aligned}
d v_{t}=- & \lambda\left(v_{t}-\bar{v}\right) d t \\
& +\eta v_{t}\left(e d z_{1}+\sqrt{1-e^{2}} d \omega\right)
\end{aligned}
$$

The two terms with with random diffierentials are martinggles which have constant expectation that is zero since $\mu=0$.

$$
\begin{aligned}
& E\left[d v_{t}\right]=-E\left[-\lambda\left(v_{t}-\bar{v}\right) d t\right] \\
\Rightarrow & d E\left[v_{t}\right]=-\lambda E\left[v_{s}-\bar{v}\right] d t
\end{aligned}
$$

let

$$
\hat{U}_{t}=E\left[U_{t}\right]
$$

Then

$$
d \hat{v}_{t}=-\lambda\left(\hat{v}_{t}-\bar{v}\right) d t
$$

since $\tau$ is constat $d u=0$

50

$$
\begin{aligned}
& d\left(\hat{v}_{t}-\bar{v}\right)=-\lambda\left(\hat{v}_{t}-\bar{v}\right) d t \\
\Rightarrow & \frac{1}{\left(\hat{v}_{t} \cdot \bar{v}\right)} d\left(\hat{v}_{t}-\bar{v}\right)=-\lambda d t \\
\Rightarrow & d \ln \left(\hat{v}_{t}-\bar{v}\right)=-\lambda d t \\
\Rightarrow & \ln \left(\hat{v}_{t}-\bar{v}\right)=-\lambda t+c \\
\Rightarrow & \hat{v}_{t}-\bar{v}=e^{-\lambda t+c} \\
& =c e^{-\lambda t}
\end{aligned}
$$

At $t=0$

$$
\hat{v}_{0}=v_{0}
$$

so

$$
v_{0}-\bar{v}=c
$$

Thus

$$
\hat{v}_{t}=\left(v_{0}-\bar{v}\right) e^{-\lambda t}+\bar{v}
$$

Define the expected total variance to time $t$ by

$$
\begin{aligned}
\hat{\omega}_{t} & =\int_{0}^{t} \hat{v}_{s} d s \\
& =\int_{0}^{t}\left[\left(v_{0}-\bar{v}\right) e^{-\lambda s}+\bar{v}\right] d s \\
& =-\frac{\left(v_{0}-\bar{v}\right)}{\lambda} e^{-\lambda s}+\left.\bar{v} s\right|_{0} ^{t} \\
& =-\frac{\left(v_{0}-\bar{v}\right)}{\lambda}\left(e^{-\lambda t}-1\right)+\bar{v} t \\
& =\left(v_{0}-\bar{v}\right) \frac{\left(1-e^{-\lambda t}\right)}{\lambda}+\bar{v} t
\end{aligned}
$$

Thus

$$
\hat{\omega}_{t}=\left(v_{0}-\bar{v}\right) \frac{\left(1-e^{-\lambda t}\right)}{\lambda}+\bar{v} t
$$

Next, the Heston local volatility is defined by

$$
u_{t}=E\left[U_{t} \mid X_{T}\right]
$$

The following relation is assumed without proof,

$$
E\left[x_{S} \mid x_{T}\right]=x_{T} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}}
$$

where

$$
\hat{\omega}_{t}=\int_{0}^{t} \hat{v}_{s} d s
$$

is the expected total vanance to time $t$.
Next consider the $d x_{t}$ term from the Heston model,

$$
d x_{t}=-\frac{v_{t}}{2} d t+\sqrt{v}_{t} d z
$$

Taking expectation gives

$$
\begin{aligned}
E\left[d x_{t}\right] & =E\left[\frac{v_{t}}{2} d t\right]+E\left[\sqrt{v_{t}} d z\right] \\
\Rightarrow d E\left[x_{t}\right] & =-\frac{1}{2} E\left[v_{t} d t\right]+E\left[\sqrt{v_{t}} d z\right] \\
\Rightarrow E\left[x_{t}\right] & =-\frac{1}{2} E\left[\int_{0}^{t} v_{t} d t\right] \\
& +E\left[\int_{0}^{t} \sqrt{v_{t}} d z\right]
\end{aligned}
$$

The second intergicl is a martingale so in vanishes, so

$$
\begin{aligned}
E\left[x_{t}\right] & =-\frac{1}{2} \int_{0}^{t} E\left[v_{t}\right] d t \\
& =-\frac{1}{2} \int_{0}^{t} \hat{v}_{t} d t \\
& =-\frac{\hat{\omega}_{t}}{2}
\end{aligned}
$$

Taking

$$
E\left[x_{t}\right]=\frac{-\hat{\omega}_{t}}{2}
$$

To see that on that the assumed relation is a plausable approximation

$$
\begin{aligned}
& E\left[X_{S} \mid X_{T}\right]=X_{T} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}} \\
\Rightarrow & E\left[E\left[X_{S} \mid X_{T}\right]\right]=E\left[X_{T} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}}\right] \\
\Rightarrow & E\left[X_{S}\right]=E\left[X_{T}\right] \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}} \\
& =-\frac{\hat{\omega}_{T}}{2} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}} \\
& =-\frac{\hat{\omega}_{S}}{2}
\end{aligned}
$$

This agrees with previoles calculation of $E\left[x_{t}\right]$ and
justifies the assumption for the value assumed for $E\left[X_{S} \mid X_{T}\right]$

Recall

$$
\begin{aligned}
d v_{t}= & \lambda\left(v_{t}-\bar{v}\right) d t+\eta \rho\left(d x_{t}+\frac{1}{2} v_{t} d t\right) \\
& +\eta \sqrt{v}_{t} \sqrt{1-\rho^{2}} d \omega
\end{aligned}
$$

and trat

$$
u_{t}=E\left[U_{t} \mid X_{T}\right]
$$

Applying this to the above relation gives

$$
\begin{aligned}
d u_{t} & =-\lambda\left(u_{t}-\bar{v}\right) d t+\frac{e \eta}{2} u_{t} d t \\
& +\eta \rho E\left[d x_{t} \mid x_{T}\right] \\
& +\sqrt{1-e^{2}} \eta \sqrt{v_{t}} E\left[d \omega_{t} \mid x_{T}\right]
\end{aligned}
$$

but

$$
\begin{aligned}
& E\left[x_{t} \mid x_{T}\right]=x_{T} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}} \\
\Rightarrow & E\left[d x_{t} \mid x_{T}\right]=x_{T} \frac{d \hat{\omega}_{S}}{\hat{\omega}_{T}}
\end{aligned}
$$

so

$$
\begin{aligned}
d u_{t} & =-\lambda\left(u_{t}-\bar{v}\right) d t+\frac{e \eta}{2} u_{t} d t \\
& +\eta \rho x_{T} \frac{d \hat{\omega}_{t}}{\hat{\omega}_{T}} \\
& +\sqrt{1-e^{2}} \eta \sqrt{v_{t}} E\left[d \omega_{t} \mid x_{T}\right]
\end{aligned}
$$

If $e$ is near $\pm 1$ so that $\sqrt{1-e^{2}}$ is small the last term can be ignored to give

$$
\begin{aligned}
d u_{t} & \approx-\lambda\left(u_{t}-\bar{v}\right) d t+\frac{e \eta}{2} u_{t} d t \\
& +\eta e x_{T} \frac{d \hat{\omega}_{t}}{\hat{\omega}_{T}}
\end{aligned}
$$

$$
\begin{aligned}
=- & \lambda u_{t} d t+\frac{e \eta}{2} u_{t} d t+\lambda \bar{v} d t \\
& +\eta e \frac{x_{T}}{\hat{\omega}_{T}} d \hat{\omega}_{t} \\
= & \left(-\lambda+\frac{e \eta}{2}\right) u_{t} d t+\lambda \bar{v} d t \\
& +\eta e \frac{x_{T}}{\hat{\omega}_{T}} d \hat{\omega}_{t}
\end{aligned}
$$

Let

$$
\lambda^{\prime}=\lambda-\frac{\rho y}{2}
$$

then

$$
\begin{aligned}
d u_{t} \approx- & \lambda^{\prime} u_{t} d t+\lambda \bar{v} d t \\
& +\eta \rho \frac{x_{T}}{\hat{\omega}_{\tau}} d \hat{\omega}_{t} \\
=- & -\lambda^{\prime}\left(u_{t}-\frac{\lambda}{\lambda^{\prime}} \bar{v}\right) d t
\end{aligned}
$$

$$
+\eta \rho \frac{x_{I}}{\hat{\omega}_{T}} d \hat{\omega}_{t}
$$

furthur let

$$
\bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v}
$$

then

$$
d u_{t} \approx-\lambda^{\prime}\left(u_{t}-\bar{v}^{\prime}\right) d t+\eta \rho \frac{x_{I}}{\hat{\omega}_{I}} d \hat{\omega}_{t}
$$

Finally recall that

$$
\begin{aligned}
& \hat{\omega}_{t}=\int_{0}^{t} \hat{v}_{s} d s \\
\Rightarrow & d \hat{\omega}_{t}=\hat{v}_{t} d t
\end{aligned}
$$

Thus
$d u_{t} \approx-\lambda^{\prime}\left(u_{t}-\bar{v}^{\prime}\right) d t+\eta \rho \frac{x_{I}}{\hat{\omega}_{7}} \hat{v}_{t} d t$

$$
=\left[-\lambda^{\prime}\left(u_{t}-\bar{v}^{\prime}\right)+\eta \rho \frac{x_{I}}{\hat{\omega}_{\tau}} \hat{v}_{t}\right] d t
$$

So,

$$
d u_{t} \approx\left[-\lambda^{\prime}\left(u_{t}-\bar{v}^{\prime}\right)+\eta e \frac{x_{I}}{\hat{\omega}_{T}} \hat{v}_{t}\right] d t
$$

where

$$
\lambda^{\prime}=\lambda-e \frac{y}{2} \quad \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v}
$$

This equation can be solved using an itegration factor

$$
\begin{aligned}
d u_{t}= & -\lambda^{\prime}\left(u_{t}-\bar{v}^{\prime}\right) d t+\eta e \frac{x_{T}}{\hat{\omega}_{\tau}} \hat{v}_{t} d t \\
\Rightarrow d u_{t} & +\lambda^{\prime} u_{t} d t=\lambda^{\prime} \bar{v}^{\prime} d t \\
& +\eta e \frac{x_{T}}{\hat{\omega}_{\tau}} \hat{v}_{t} d t
\end{aligned}
$$

The interation factor is given by

$$
e^{\int \lambda^{\prime} d t}=e^{\lambda^{\prime} t}
$$

It follows that

$$
\begin{aligned}
e^{\lambda^{\prime} t} d u_{t} & +\lambda^{\prime} e^{\lambda^{\prime} t} u_{t} d t=\lambda^{\prime} \bar{v}^{\prime} d t \\
& +\eta\left(\frac{x_{T}}{\hat{\omega}_{\tau}} \hat{v}_{t} d t\right. \\
\Rightarrow d\left(e^{\lambda^{\prime} t} u_{t}\right) & =e^{\lambda^{\prime} t} \lambda^{\prime} \bar{v}^{\prime} d t \\
& +e^{\lambda^{\prime} t} \eta \rho \frac{x_{\tau}}{\hat{\omega}_{\tau}} \hat{v}_{t} d t
\end{aligned}
$$

Integrating gives

$$
\begin{array}{rl}
\int_{0}^{T} & d\left(e^{\lambda^{\prime} t} u_{t}\right)=\int_{0}^{T} \lambda^{\prime} v^{\prime} e^{\lambda^{\prime} t} d t \\
& +\int_{0}^{T} e^{\lambda^{\prime} t} h e \frac{x_{T}}{\hat{\omega}_{T}} \hat{v}_{t} d t
\end{array}
$$

$$
\begin{aligned}
=\left.e^{\lambda^{\prime} t} u_{t}\right|_{0} ^{T}=\lambda^{\prime} \bar{v}^{\prime} \int_{0}^{T} e^{\lambda^{\prime} t} d t \\
+\eta \rho \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} e^{\lambda^{\prime} t} \hat{v}_{t} d t \\
=e^{\lambda^{\prime} T} u_{T}-u_{0}=\left.\lambda^{\prime} \bar{v}^{\prime} \frac{e^{\lambda^{\prime} t}}{\lambda^{\prime}}\right|_{0} ^{T} \\
+\eta \rho \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} e^{\lambda^{\prime} t} \hat{v}_{t} d t \\
=e^{\lambda^{\prime} T} u_{T}=u_{0}+\bar{v}\left(e^{\lambda^{\prime} T}-1\right) \\
+\eta e \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} e^{\lambda^{\prime} t} \hat{v}_{t} d t \\
\Rightarrow u_{T}=u_{0} e^{-\lambda^{\prime} T}+\bar{v}^{\prime}\left(1-e^{-\lambda^{\prime} T}\right) \\
+\eta e \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} e^{-\lambda(T-t)} \hat{v}_{t} d t
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow u_{T}= & \left(u_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} T}+\bar{v}^{\prime} \\
& +\eta \rho \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} e^{-\lambda(T-t)} \hat{v}_{t} d t
\end{aligned}
$$

Recall that

$$
u_{t}=E\left[U_{t} \mid X_{T}\right]
$$

since $v_{0}$ is a constant it follows that,

$$
u_{0}=E\left[v_{0} \mid x_{T}\right]=v_{0}
$$

So

$$
\begin{aligned}
\left(u_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} T}+\bar{v}^{\prime} & =\left(v_{0}-\bar{\sigma}^{\prime}\right) e^{-\lambda^{\prime} T}+\bar{v}^{\prime} \\
& =\hat{v}_{T}^{\prime}
\end{aligned}
$$

Thus

$$
u_{T} \approx \hat{v}_{T}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} \hat{v}_{S} e^{-\lambda^{\prime}(T-S)} d s
$$

## Digression : Ornstein Whlenbeck Process

The PDEs being disussed have the form of a ornstein wenbeck process. Hore soluing the SDE for the process is dcussed
The omstein unlenbeck SDE is given by,

$$
d x_{t}=k\left(\theta-x_{t}\right) d t+\gamma d z
$$

which is the basis of a mean reverting process
The Integrating factor method is used to solve the SDE.
For a first order ODE of the form

$$
\frac{d y}{d x}+p(x) y(x)=q(x)
$$

let

$$
v(x)=\int p(x) d x
$$

then

$$
\frac{d u}{d x}=p(x)
$$

The integrating factor is defined by

$$
e^{v(x)}
$$

multiplying the SDE by the integrating factor gives

$$
\begin{aligned}
& \frac{d y}{d x} e^{v(x)}+p(x) y(x) e^{v(x)}=q(x) e^{v(x)} \\
= & \frac{d}{d x}\left[e^{v(x)} y(x)\right]=q(x) e^{v(x)}
\end{aligned}
$$

The integrating makes the RHS a prefet differential whon can be easily integrated to give

$$
y(x)=e^{-v(x)} \int e^{v(x)} g(x) d x
$$

Applying this method to the ornstein-uktenbeck process gives

$$
\begin{aligned}
d x_{t} & =k\left(\theta-x_{t}\right) d t+\sigma d z \\
& =-k x_{t} d t+k \theta d t+\sigma d z \\
\Rightarrow d x_{t} & +k x_{t} d t=k \theta d t+\sigma d z
\end{aligned}
$$

The integrating factor is given by

$$
e^{S k d t}=e^{k t}
$$

50

$$
\begin{aligned}
e^{k t} d x_{t} & +k e^{k t} x_{t} d t \\
& =e^{k t} k \theta d t+e^{k t} \sigma d z
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & d\left(e^{k t} x_{t}\right)=k \theta e^{k t} d t \\
& +\sigma e^{k t} d z
\end{aligned}
$$

Integrating from $t=0$ to $t=T$ gives

$$
\begin{gathered}
\int_{0}^{T} d\left(e^{k t} x_{t}\right)=\int_{0}^{T} k \theta e^{k t} d t \\
+\int_{0}^{T} \sigma e^{k t} d z
\end{gathered}
$$

$$
\begin{aligned}
\Rightarrow & \left.e^{k t} x_{t}\right|_{0} ^{T}=\left.\theta e^{k t}\right|_{0} ^{T}+\sigma \int_{0}^{T} e^{k t} d z \\
\Rightarrow & e^{k T} x_{T}-x_{0}=\theta\left(e^{k T}-1\right)+\sigma \int_{0}^{T} e^{k t} d z \\
\Rightarrow & e^{k T} x_{T}=x_{0}+\theta\left(e^{k T}-1\right)+\sigma \int_{0}^{T} e^{k t} d z \\
\Rightarrow & x_{T}=x_{0} e^{-k T}+\theta\left(1-e^{-k T}\right) \\
& +\sigma \int_{0}^{T} e^{-k(T-t)} d z
\end{aligned}
$$

## Thus

$x_{T}=x_{0} e^{-k T}+\theta\left(1-e^{-k T}\right)+\sigma \int_{0}^{T} e^{-k(T-t)} d z$
$X_{T}$ is a Gaussian process since dz is Gaussian process.

The mean is given by,

$$
\begin{aligned}
& E\left[X_{T}\right]= E\left[X_{0} e^{-k T}\right]+E\left[\theta\left(1-e^{-k T}\right)\right] \\
&+ E\left[\sigma \int_{\varnothing}^{T} e^{-k(T-D)} d z\right] \\
&=x_{0} e^{-k T}+\theta\left(1-e^{-k T}\right)
\end{aligned}
$$

The last term is zero since it is a martingale.
The variance is given by
$\operatorname{Uar}\left(x_{T}\right)=E\left[\left(x_{T}-E\left[x_{T}\right]\right)^{2}\right]$

$$
\begin{aligned}
=E & {\left[\left(x_{0} e^{-k T}+\theta\left(1-e^{-k T}\right)+\sigma \int_{0}^{T} e^{-k(T-t)} d z\right.\right.} \\
& \left.\left.-x_{0} e^{-k T}-\theta\left(1-e^{-k T}\right)\right)^{2}\right] \\
=E & {\left[\left(\sigma \int_{0}^{T} e^{-k(T-t)} d z\right)^{2}\right] }
\end{aligned}
$$

Recall Itso isometry

$$
\begin{aligned}
& E\left[\left(\int_{0}^{T} f(t) d z\right)^{2}\right] \\
& =E\left[\int_{0}^{T} f^{2}(t) d t\right]
\end{aligned}
$$

50

$$
\begin{aligned}
& \operatorname{var}\left(x_{T}\right)=E\left[\left(\sigma \int_{0}^{T} e^{-k(T-t)} d z\right)^{2}\right] \\
& =\sigma^{2} E\left[\int_{0}^{T} e^{-2 k(T-t)} d t\right]
\end{aligned}
$$

$$
=\sigma^{2} \int_{0}^{T} e^{-\partial K(T-t)} d t
$$

make the change of variables

$$
\begin{aligned}
& u=T-t \Rightarrow-d u=d t \\
& \text { so } \\
& \operatorname{var}\left(x_{T}\right)=-\sigma^{2} \int_{T}^{0} e^{-2 k u} d u \\
& =\sigma^{2} \int_{0}^{T} e^{-2 k u} d u \\
& =\left.\frac{-\sigma^{2}}{2 k} e^{-2 k u}\right|_{0} ^{T}=-\frac{\sigma^{2}}{2 k}\left(e^{-2 k T}-1\right) \\
& =\frac{\sigma^{2}}{2 k}\left(1-e^{-2 k T}\right)
\end{aligned}
$$

Thus the mean and variance are given by

$$
\begin{aligned}
& E\left[x_{t}\right]=x_{0} e^{-k T}+O\left(1-e^{-k T}\right) \\
& \operatorname{var}\left[x_{t}\right]=\frac{\theta^{2}}{2 k}\left(1-e^{-2 k T}\right)
\end{aligned}
$$

## Digresion: Brownian Bridge Process

The Brownain bridge is a wiener process with fixed endpoints. It is used to model the possible paths of the asset intantaneous variance as a function of the asset price between fixed intutral and final prices.
The SDE for the Brownian Bridge with endpaints $a$ and $b$

$$
d x_{t}=\frac{b-x_{t}}{T-t} d t+d z
$$

with

$$
x_{0}=a \quad x_{\tau}=b
$$

The solution of the SDE is dotained using an integration factor,

$$
\begin{aligned}
d x_{t} & =\frac{b-x_{t}}{T-t} d t+d z \\
& =\frac{b d t}{T-t}-\frac{x_{t} d t}{T-t}+d z \\
\Rightarrow d x_{t} & +\frac{1}{T-t} x_{t} d t=\frac{b}{T-t} d t+d z
\end{aligned}
$$

The integration factor is given by

$$
v=\int \frac{1}{T-t} d t
$$

let

$$
u=T \cdot t \quad \Rightarrow-d u=d t
$$

So

$$
\begin{aligned}
v= & -\int \frac{1}{u} d u \\
& =-\ln u \\
& =-\ln (T-t)
\end{aligned}
$$

thus the integration factor is given by

$$
\begin{aligned}
& \exp [-\ln (T-t)]=\exp \left[\ln \left(\frac{1}{T-t}\right)\right] \\
& =\frac{1}{T-t}
\end{aligned}
$$

so the SDE becomes

$$
\begin{aligned}
& d x_{t}+\frac{1}{T-t} x_{t} d t=\frac{b}{T-t} d t+d z \\
\Rightarrow & \frac{1}{T-t} d x_{t}+\frac{1}{(T-t)^{2}} x_{t} d t \\
= & \frac{b}{(T-t)^{2}} d t+\frac{1}{T-t} d z \\
\Rightarrow & d\left[\frac{x_{t}}{T-t}\right]=\frac{b}{(T-t)^{2}} d t+\frac{1}{T-t} d z
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & \int_{0}^{t} d\left[\frac{X_{s}}{T-s}\right]=\int_{0}^{t} \frac{b}{(T-s)^{2}} d s \\
& +\int_{0}^{t} \frac{1}{T t} d Z_{s} \\
\Rightarrow & \left.\frac{X_{s}}{T-s}\right|_{0} ^{t}=\int_{0}^{t} \frac{b}{(T-s)^{2}} d s \\
& +\int_{0}^{t} \frac{1}{T-s} d Z_{s} \\
\Rightarrow & \frac{X_{t}}{T-t}-\frac{X_{0}}{T}=b \int_{0}^{t} \frac{1}{(T-s)^{2}} d s \\
& +\int_{0}^{t} \frac{1}{T-s} d Z_{s}
\end{aligned}
$$

Now $x_{0}=a$ so the lefthand side becomes

$$
\frac{x_{t}}{T-t}-\frac{a}{T}
$$

and for the first integral on the right tand side is given by

$$
\begin{aligned}
& u=T-s \Rightarrow-d u=d s \\
& \int_{0}^{t} \frac{1}{(T-s)^{2}} d s=-\int_{T}^{T-t} \frac{d u}{u^{2}} \\
& =\left.\frac{1}{u}\right|_{T} ^{T-t}=\frac{1}{T-t}-\frac{1}{T} \\
& =\frac{1}{T(T-t)}(T-T+t)=\frac{t}{T(T-t)}
\end{aligned}
$$

putting things together
$\frac{x_{t}}{T-t}-\frac{a}{T}=\frac{t}{T(T-t)} b+\int_{0}^{t} \frac{1}{T-s} d z_{s}$

$$
\begin{aligned}
\Rightarrow \quad \frac{X_{t}}{T-t}=\frac{t b}{T(T-t)}+\frac{a}{T}+\int_{0}^{t} \frac{1}{T-s} d z_{s} \\
\Rightarrow \quad X_{t}=b \frac{t}{T}+a \frac{(T-t)}{T} \\
+(T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s} \\
=a+\frac{t}{T}(b-a)+(T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s}
\end{aligned}
$$

Thus

$$
\begin{array}{r}
x_{t}=a+\frac{t}{T}(b-a)+ \\
(T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s}
\end{array}
$$

It is interesting to verfy that the solution gives the correct values,

$$
\begin{aligned}
x_{0} & =a+T \int_{0}^{6} \frac{1}{T-s} d z_{s} \\
& =a \\
x_{T} & =a+b-a \\
& =b
\end{aligned}
$$

## It does

The mean is given by

$$
\begin{aligned}
E\left[x_{t}\right]= & E\left[a+\frac{t}{T}(b-a)+\right. \\
(T-t) & \left.\int_{0}^{t} \frac{1}{T-s} d z_{s}\right] \\
=a & +\frac{t}{T}(b-a) \\
& +E\left[(T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s}\right]
\end{aligned}
$$

The lest term is a martingale so it vanishes, thus

$$
E\left[x_{t}\right]=a+\frac{t}{T}(b-a)
$$

The variance is given by,

$$
\begin{aligned}
& \operatorname{var}\left(x_{t}\right)=E\left[\left(x_{t}-E\left[x_{t}\right]\right)^{2}\right] \\
= & E\left[\left(a+\frac{t}{T}(b-a)+(T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s}\right.\right. \\
& \left.\quad-\frac{\left.a+\frac{t}{T}(b-a)\right)^{2}}{T}\right] \\
= & E\left[\left((T-t) \int_{0}^{t} \frac{1}{T-s} d z_{s}\right)^{2}\right]
\end{aligned}
$$

Application of Itô isometry gives

$$
E\left[\left((T-t) \int_{0}^{t} \frac{1}{T-S} d Z_{s}\right)^{2}\right]
$$

$$
\begin{aligned}
& =E\left[(T-t)^{2} \int_{0}^{t} \frac{1}{(T-s)^{2}} d s\right] \\
& =(T-t)^{2} \frac{t}{T(T-t)} \\
& =\frac{t}{T}(T-t)
\end{aligned}
$$

Thus the mean and variance

$$
\begin{aligned}
& E\left[x_{t}\right]=\mu=a+\frac{t}{T}(b-a) \\
& \operatorname{Var}\left(x_{t}\right)=\sigma^{2}=\frac{t}{T}(T-t)
\end{aligned}
$$

The Caussian Brigge is a Caussian process so it has distribution

$$
\text { Normal }\left(\mu, \sigma^{2}\right)
$$

To simulate the process a difference equation must be
derived. Assume the following time descritation where to $=0$ so the

$$
t=t_{0}, t_{1}, t_{2}, \ldots, T
$$

The boundary conditions become,

$$
x_{t_{0}}=a \quad x_{T}=b
$$

also, note that

$$
\begin{aligned}
& T=T-0=T-t_{0} \\
& t=T-0=t-t_{0}
\end{aligned}
$$

using this descretization the mean and variance are given by,

$$
E\left[x_{t_{i}}\right]=x_{t_{0}}+\left(x_{T}-x_{t_{0}}\right) \frac{\left(t_{i}-t_{0}\right)}{\left(T-t_{0}\right)}
$$

the variance is given

$$
\operatorname{Var}\left(x_{t_{i}}\right)=\frac{t_{i}-t_{0}}{T-t_{0}}\left(T-t_{i}\right)
$$

Any baussian process can be simulated using an expression of the form

$$
\Delta x_{i}=\mu_{i} \Delta t_{i}+\sigma_{i} N(0,1)
$$

where

$$
\begin{aligned}
& \Delta x_{i}=x_{t_{i}}-x_{t_{i-1}} \\
& \Delta t_{i}=t_{i}-t_{i-1}
\end{aligned}
$$

and $N(0,1)$ is a unit normal.
This leads to the difference equation

$$
\begin{aligned}
x_{t_{i}}=x_{t_{i-1}} & +\left(x_{T}-x_{t-1}\right) \frac{\Delta t_{i}}{T-t_{i}} \\
& +\sqrt{\frac{\Delta t_{i}\left(T-t_{i}\right)}{T-t_{i-1}}} N(0,1)
\end{aligned}
$$

## Implied Volatility in the Heston Model

The path to this point will be summarized
Recall the begining, the local volatility is defined as the volatility of the Fokker-Plank equation written in terms of the forward price,

$$
\frac{\partial C}{\partial T}\left(F_{0}, K, T\right)=\frac{1}{2} U_{L}\left(K, T ; S_{0}\right) K^{2} \frac{\partial^{2} C}{\partial K^{2}}
$$

The local odatility can be computed from available option price data using

$$
v_{L}\left(K, T ; S_{0}\right)=\frac{\frac{\partial C}{\partial K}}{\frac{k^{2}}{2} \frac{\partial^{2} C}{\partial K^{2}}}
$$

Next, the Black-Sholes implied volatility was defined. The Black-Sholes implied volatility is the volatility of an opton price at expiry that appears in the Black-Andes equation of the option price. It is denoted by,

$$
U_{\tau}\left(K ; S_{0}\right)=\sigma_{B S}^{2}\left(K, T ; S_{0}\right)
$$

$U_{T}(K)$ is also called the instantanedes variance, It was shown that the local and instantaneous variance are related by,

$$
U_{L}\left(K, T ; S_{0}\right)=E\left[U_{T} \mid S_{T}=K\right]
$$

From this relation the local volatility can be computed from intaneous volatitility.

An inverse relation is more desirable since $U_{L}$ can be casily computed from available option price data
Define the Black-sholes gamma by
$\Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right)=\frac{\partial}{\partial S_{t}^{2}} C_{B S}\left(S_{t}, K, \bar{\sigma}(t), T-t\right)$
furtur define the Black-Scholes forward

$$
v_{k, T}(t)=\frac{E\left[\sigma_{t}^{2} S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right) \mid \mathcal{F}_{0}\right]}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(t) \mid \mathcal{F}_{0}\right]\right.}
$$

Here $\sigma_{t}$ is the instaneous volatility from the asset price SDE

$$
d S_{t}=\mu_{t} S_{t} d t+\sigma_{t} S_{t} d z_{t}
$$

$v_{k, T}(t)$ is the expectation $\theta$
$\sigma_{t}$ with respect to the probability density,

$$
\frac{S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(t)\right)}{E\left[S_{t}^{2} \Gamma_{B S}\left(S_{t}, \bar{\sigma}(t) \mid \mathcal{F}_{0}\right]\right.}
$$

where

$$
\bar{\sigma}^{2}(t)=\frac{1}{T-t} \int_{t}^{T} v_{k, T}(u) d u
$$

It is shown that the Blacksholes implied variance at $T$, denoted by $\sigma_{B S}^{2}(K, T)$, is given by

$$
\begin{aligned}
\sigma_{B S}^{2}(k, T) & =\sigma^{2}(0) \\
& =\frac{1}{T} \int_{0}^{T} v_{k, T}(t) d t
\end{aligned}
$$

This integral is solued by approximation, before starting

## a crange of variables is performed. Let,

$$
x=\ln \frac{S_{t}}{S_{0}}
$$

so that

$$
v_{k, T}(t)=\int q\left(x_{t}, t ; x_{T}, T\right) v_{L}\left(x_{t}, t\right) d x_{t}
$$

lumerical solutions of this integral show that it is shanply peaked about a value, $\bar{x}_{t}$, which forms a line on the surface $x_{t}, t$ Expanding $q\left(x_{t}, t ; x_{T}, T\right)$ and $U_{L}\left(x_{t}, t\right)$ to leading order it is shown that,

$$
v_{k, T}(t) \approx v_{L}\left(\bar{x}_{t}, t\right)
$$

From the definition of implier forward variance it follows that

$$
\sigma_{B S}^{2}(K, T) \approx \frac{1}{T} \int_{0}^{T} U_{L}\left(\bar{X}_{t}, u\right) d u
$$

Next the Heston model is used to approximate $v_{L}\left(\bar{x}_{t}, \omega\right)$ so that $\sigma_{B S}^{2}(K, T)$ can be computed.

From the Heston model the sol for the instantaneous variance is given by

$$
\begin{aligned}
d U_{t}= & -\lambda\left(U_{t}-t\right) d t \\
& +\eta \sqrt{u}_{t}\left(e d z+\sqrt{1-e^{2}} d \omega\right)
\end{aligned}
$$

Taking expectation gives

$$
\begin{gathered}
\hat{U}_{t}=E\left[U_{t}\right] \\
d \hat{U}_{t}=-\lambda\left(\hat{U}_{t}-\bar{U}\right) d t
\end{gathered}
$$

The solution to this equation
is given by

$$
\hat{v}_{t}=\left(v_{0}-\bar{v}\right) e^{-\lambda t}+\bar{v}
$$

Define the expected total variance by

$$
\begin{aligned}
\hat{\omega}_{t} & =\int_{0}^{t} \hat{v}_{s} d s \\
& =\left(v_{0} \cdot \bar{v}\right) \frac{\left(1-e^{-\lambda t}\right)}{\lambda}+\overline{u t}
\end{aligned}
$$

Next define the local Heston volatility by

$$
u_{t}=E\left[v_{t} \mid x_{T}\right]
$$

and the following relation is

$$
E\left[X_{S} \mid X_{T}\right]=X_{T} \frac{\hat{\omega}_{S}}{\hat{\omega}_{T}}
$$

From the teston model

$$
d x_{t}=-\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z
$$

Taking expectation and integrating gives

$$
E\left[x_{t}\right]=-\frac{\hat{\omega}_{t}}{2}
$$

Next the conditional expectation of the Heston model is taken to obtain the following equation for $u_{t}$ assuming $\mid e^{l} \approx 1$

$$
\begin{aligned}
d u_{t} & =\left(-\lambda+\frac{\rho \eta}{2}\right) u_{t} d t+\lambda \bar{u} d t \\
& +\eta l \frac{x_{T}}{\hat{\omega}_{T}} d \hat{\omega}_{t}
\end{aligned}
$$

The solution to this equation is given by

$$
u_{T} \approx \hat{v}_{T}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} \hat{v}_{S} e^{-\lambda^{\prime}(T-S)} d S
$$

where

$$
\begin{aligned}
& \lambda^{\prime}=\lambda-\frac{e \eta}{2} \quad \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v} \\
& \hat{v}_{t}^{\prime}=\left(v_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{v}^{\prime}
\end{aligned}
$$

To continue recall that

$$
\sigma_{B S}^{2}(K, T) \approx \frac{1}{T} \int_{0}^{T} U_{L}\left(\bar{x}_{t}, u\right) d u
$$

where $U_{L}\left(\bar{x}_{t}, u\right)$ is the local volatility and $\bar{x}_{t}$ is the maximum of $U_{L}\left(x_{t}, u\right)$ referred to as the most probable path
using local odatility obtained from the Heston madel

$$
\sigma_{B s}^{2}\left(K_{1} T\right) \approx \frac{1}{T} \int_{0}^{T} u_{t}\left(\bar{x}_{t}\right) d t
$$

The volatility density is starply peaked around $\bar{x}_{t}$ so most of the mass is a around this line it follows that

$$
E\left[x_{t}-\bar{x}_{t} \mid x_{t}\right] \approx 0
$$

since $x_{t}$ is constant it follows that

$$
\begin{aligned}
\bar{x}_{t} & =E\left[\bar{x}_{t} \mid x_{T}\right] \\
& =E\left[\bar{x}_{t}-x_{t}+x_{t} \mid x_{T}\right] \\
& \approx 0 \\
& =E\left[\bar{x}_{t}-x_{t} \mid x_{T}\right]+E\left[x_{t} \mid x_{T}\right] \\
& \approx E\left[x_{t} \mid x_{T}\right] \\
& =\frac{\hat{\omega}_{t}}{\hat{\omega}_{T}} x_{T}
\end{aligned}
$$

Here the previously assumed relation is used
Using the approximation for
$u_{T}$ prevously found and changing the integration
to $t$ gives,

$$
u_{t} \approx \hat{v}_{t}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s
$$

Inserting this expresion into the expression for $\sigma_{B S}(K, T)$ gives

$$
\begin{aligned}
& \sigma_{B s}^{2}\left(K_{1} T\right) \approx \frac{1}{T} \int_{0}^{T} u_{t}\left(\bar{x}_{t}\right) d t \\
& =\frac{1}{T} \int_{0}^{T}\left[\hat{v}_{t}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s\right] d t \\
& =\frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
& \quad+e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s\right] d t
\end{aligned}
$$

Thus

$$
\begin{aligned}
\sigma_{B s}^{2}\left(K_{1} T\right) & \approx \frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
+ & e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s\right] d t
\end{aligned}
$$

where

$$
\lambda^{\prime}=\lambda-\frac{e n}{2} \quad \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v}
$$

$$
\hat{v}_{t}^{\prime}=\left(v_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{v}^{\prime}
$$

## At the-Money (ATM) Term structure of Block-Sholes Implied Volatility

The at the money structure of BS implied varrance in the Heston model is obtained by setting $x_{7}=0$,

$$
\begin{aligned}
& x_{T}=\ln \frac{S_{T}}{K}=0 \\
& \Rightarrow S_{T}=K
\end{aligned}
$$

Recall,

$$
\begin{aligned}
\sigma_{B s}^{2}\left(K_{1} T\right) & \approx \frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
& +\ln \frac{x_{T}}{\hat{\omega}_{\tau}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s\right] d t
\end{aligned}
$$

setting $x_{T}=0$ and recalling that

$$
F_{T}=S_{T}
$$

gives,

$$
\left.\sigma_{B S}^{2}(K, T)\right|_{K=F_{T}} \approx \frac{1}{T} \int_{0}^{T} \hat{u}^{\prime} d t
$$

where

$$
\hat{v}_{t}^{\prime}=\left(v_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{v}^{\prime}
$$

evaluating the integral gives

$$
\begin{aligned}
& \frac{1}{T} \int_{0}^{T} U^{\prime} d t=\frac{1}{T} \int_{0}^{T}\left(U_{0}-\bar{U}^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{U}^{\prime} d t \\
& =\left.\frac{1}{T}\left[-\frac{\left(U_{0}-\bar{U}^{\prime}\right)}{\lambda^{\prime}} e^{-\lambda^{\prime} t}+\bar{U}^{\prime} t\right]\right|_{0} ^{T} \\
& =\frac{1}{T}\left\{\left[-\frac{\left(U_{0}-\bar{U}^{\prime}\right)}{\lambda^{\prime}} e^{-\lambda^{\prime} T}+\bar{U}^{\prime} T\right]\right. \\
& \left.\quad+\frac{\left(U_{0}-\bar{U}^{\prime}\right)}{\lambda^{\prime}}\right\}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{T}\left[\frac{\left(U_{0} \cdot \bar{U}^{\prime}\right)\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime}}+\bar{U}^{\prime} T\right] \\
& =\frac{\left(U_{0} \cdot \bar{U}^{\prime}\right)\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}+\bar{U}^{\prime}
\end{aligned}
$$

For the limit $T \ll \lambda^{\prime}$

$$
\begin{aligned}
1-e^{-\lambda^{\prime} T} & \approx 1-\left(1-\lambda^{\prime} T\right) \\
& =\lambda^{\prime} T
\end{aligned}
$$

It follows that

$$
\sigma_{B S}^{2}(K, T) \approx v_{0}
$$

which is expected and for

$$
\begin{gathered}
\lambda^{\prime} \ll T \\
\sigma_{B S}^{2}(K, T) \approx \bar{U}^{\prime}
\end{gathered}
$$

## Digression: Distribution skew and volatility skew

## Distribution Stew

Skew is a measure of the asymetry of a distribution about its mean. A function with zero skew is symetric. Examples of positive and negative skew are shown below

![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-306.jpg?height=356&width=551&top_left_y=1164&top_left_x=229)
Negative Skew

![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-306.jpg?height=358&width=543&top_left_y=1164&top_left_x=794)
Positive Skew

Pearsons skewness coefficient is defined by

## mean - mode <br> Standan Deviation

Thus for a symetric distribution

$$
\text { mean }=\text { mode }
$$

## Volatility Skew

volatility skew is a measure of the slope of the implied volatility for a given expry. Thus

$$
\text { volatility skew }=\frac{\partial \sigma_{B S}^{2}}{\partial x_{t}}(k, T)
$$

## The Black-scholes Implied odatility skew in the Heston Model

Recall the Black-Sholes Implied volatility is given by,

$$
\begin{aligned}
\sigma_{B s}^{2}\left(K_{1} T\right) & \approx \frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
+ & e \eta \frac{x_{T}}{\hat{\omega}_{\tau}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(T-s)} d s\right] d t \\
\lambda^{\prime} & =\lambda-\frac{e \eta}{2} \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v} \\
\hat{v}_{t}^{\prime} & =\left(v_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{v}^{\prime} \\
\hat{v}_{t} & =\left(v_{0}-\bar{v}\right) e^{\lambda t}+\bar{v}
\end{aligned}
$$

$$
\begin{aligned}
\hat{\omega}_{t}= & \int_{0}^{t} \hat{v}_{s} d s \\
= & \left(v_{0}-\bar{v}\right) \frac{\left(1-e^{-\lambda t}\right)}{\lambda}+\bar{U} t \\
& \bar{x}_{t} \approx \frac{\hat{\omega}_{t}}{\hat{\omega}_{T}} x_{T}
\end{aligned}
$$

Consider the special ase $v_{0}=\bar{U}$, then

$$
\hat{v}_{t}=\bar{v} \quad \hat{\omega}_{t}=\bar{v} t
$$

So

$$
\begin{aligned}
& \sigma_{B s}^{2}\left(K_{1} T\right) \approx \frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
& +l \eta \frac{X_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(T-s)} d s\right] d t
\end{aligned}
$$

Now,

$$
\frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t=\frac{\hat{\omega}_{T}^{\prime}}{T}
$$

furtiner using

$$
\hat{v}_{S}=\bar{v} \quad \hat{\omega}_{T}=\bar{v} T
$$

gives

$$
\begin{aligned}
& e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{U}_{s} e^{-\lambda^{\prime}(t-s)} d s\right] d t \\
= & e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T} \int_{0}^{t} \bar{v} e^{-\lambda^{\prime}(t-s)} d s d t \\
= & e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{\bar{v}}{T} \int_{0}^{T} \int_{0}^{t} e^{-\lambda^{\prime}(t-s)} d s d t \\
= & e \frac{\eta}{\tau} \frac{\bar{u}}{T^{2}} x_{T} \int_{0}^{T} \int_{0}^{t} e^{-\lambda^{\prime}(t-s)} d s d t
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{e \eta}{T^{2}} x_{T} \int_{0}^{T} e^{-\lambda^{\prime} t} \int_{0}^{t} e^{\lambda^{\prime} s} d s d t \\
& =\frac{e \eta}{T^{2}} x_{T} \int_{0}^{T} e^{-\lambda^{\prime} t}\left[\left.\frac{1}{\lambda^{\prime}} e^{\lambda^{\prime} s}\right|_{0} ^{t}\right] d t \\
& =\frac{e \eta}{T^{2}} x_{T} \int_{0}^{T} e^{-\lambda^{\prime} t}\left[\frac{1}{\lambda^{\prime}}\left(e^{\lambda^{\prime} t}-1\right)\right] d t \\
& =\frac{e \eta}{T^{2}} \frac{x_{T}}{\lambda^{\prime}} \int_{0}^{T}\left(1-e^{-\lambda^{\prime} t}\right) d t \\
& =\left.\frac{e \eta}{T^{2}} \frac{x_{T}}{\lambda^{\prime}}\left[t+\frac{e^{-\lambda^{\prime}} t}{\lambda^{\prime}}\right]\right|_{0} ^{T} \\
& =\frac{e \eta}{T^{2}} \frac{x_{T}}{\lambda^{\prime}}\left[T+\frac{1}{\lambda^{\prime}}\left(e^{-\lambda^{\prime} T}-1\right)\right] \\
& =e \eta \frac{x_{T}}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right]
\end{aligned}
$$

Putling things together gives,

$$
\begin{aligned}
& \sigma_{B s}^{2}\left(K_{1} T\right) \approx \frac{1}{T} \int_{0}^{T} \hat{v}_{t}^{\prime} d t \\
& +e \eta \frac{x_{T}}{\hat{\omega}_{T}} \frac{1}{T} \int_{0}^{T}\left[\int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(T-s)} d s\right] d t \\
& =\frac{\hat{\omega}_{T}^{\prime}}{T}+e \eta \frac{x_{T}}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right] \\
& \text { thus, } \\
& \sigma_{B s}^{2}\left(K_{1} T\right) \approx \frac{\hat{\omega}_{T}^{\prime}}{T}+e \eta \frac{x_{T}}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right] \\
& \lambda^{\prime}=\lambda_{-} \int_{2} \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v} \\
& \hat{\omega}_{T}^{\prime}=\int_{0}^{T} \hat{v}_{t}^{\prime} d t
\end{aligned}
$$

Next consider the variance slow defined by

$$
\frac{\partial}{\partial x_{T}} \sigma_{B S}^{2}(K, T)
$$

Taking the derivative of the previous equation gives
$\frac{\partial}{\partial X_{T}} \sigma_{B S}^{2}(K, T)=\frac{\partial}{\partial X_{T}}\left\{\frac{\hat{\omega}_{T}^{\prime}}{T}+\right.$

$$
\begin{aligned}
& \left.e \eta \frac{x_{T}}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right]\right\} \\
= & \frac{e \eta}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right]
\end{aligned}
$$

Thus,
$\frac{\partial}{\partial X_{T}} \sigma_{B S}^{2}(K, T)=\frac{e \eta}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right]$

Note that this expression is independent of $v_{T}$ and $\bar{v}$ and as approximately, even when $U_{T} \neq \bar{U}$ as assumed.
This expression can be used to calibrate the Heston model.
only two expirations are required to determine $\lambda^{\prime}$ and the product ey.
The currature of the stew (not discussed) can be used to determine $\rho$ and $\eta$ seperately

Note that skew is an increasing function of $e$ and $\eta$.

Consider the limt $T \rightarrow 0$

$$
\begin{aligned}
& \lim _{T \rightarrow 0} \frac{\partial}{\partial x_{T}} \sigma_{B S}^{2}\left(K_{1} T\right) \\
& =\lim _{T \rightarrow 0} \frac{\rho \eta}{\lambda^{\prime} T}\left[1-\frac{\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right] \\
& =\lim _{T \rightarrow 0} \frac{\rho \eta}{\lambda^{\prime} T}\left[\frac{\lambda^{\prime} T-\left(1-e^{-\lambda^{\prime} T}\right)}{\lambda^{\prime} T}\right]
\end{aligned}
$$

Expanding $e^{-\lambda^{\prime} T}$ to second order,

$$
e^{-\lambda^{\prime} T} \approx 1-\lambda^{\prime} T+\frac{1}{2}\left(\lambda^{\prime} T\right)^{2}
$$

$$
\begin{aligned}
& =\lim _{T \rightarrow 0} \frac{e y}{\left(\lambda^{\prime} T\right)^{2}}\left[\lambda^{\prime} T-\gamma+\gamma-\lambda^{\prime} T+\frac{1}{2}\left(\lambda^{\prime} T\right)^{2}\right] \\
& =\rho y \frac{1}{\left(\lambda^{\prime} T\right)^{2}}\left(\lambda^{\prime} T\right)^{2} \\
& =\frac{e \eta}{2}
\end{aligned}
$$

## Thus

$$
\lim _{T \rightarrow 0} \frac{\partial}{\partial x_{T}} \sigma_{B S}^{2}(K, T)=\rho \frac{\eta}{2}
$$

Finally, consider T>>1

$$
\begin{aligned}
\frac{\partial}{\partial x_{T}} \sigma_{B S}^{2}\left(K_{1} T\right) & \approx \frac{\rho \eta}{\lambda^{\prime} T}\left[1-\frac{\left(\gamma^{-e^{-\lambda^{\prime} T}}\right)}{\lambda^{\prime} T}\right] \\
& \approx \frac{\rho \eta}{\lambda^{\prime} T}
\end{aligned}
$$

Thus, for $T \gg 1$

$$
\frac{\partial}{\partial x_{T}} \sigma_{B S}^{2}(K, T) \approx \frac{e y}{\lambda^{\prime} T}
$$

## The Heston-Nardi Model

Recall that for,

$$
x_{t}=\ln \frac{S_{t}}{K}
$$

the Heston model is given by,

$$
\begin{aligned}
d x_{t}= & -\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z \\
d v_{t}= & -\lambda\left(v_{t}-\tau\right) d t \\
& +\eta \sqrt{v_{t}}\left(e d z+\sqrt{1-e^{2}} d \omega\right)
\end{aligned}
$$

By making the assumption

$$
E\left[x_{S} \mid x_{T}\right]=x_{T} \frac{\hat{\omega}_{S}}{\omega_{t}}
$$

and $|e| \approx \mid$ is was shown that the local variance is given by

$$
\begin{gathered}
u_{t}=E\left[U_{t} \mid X_{T}\right] \\
u_{t} \approx \hat{v}_{t}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s
\end{gathered}
$$

where

$$
\begin{gathered}
\hat{\omega}_{t}=\int_{0}^{t} \hat{v}_{s} d s \\
\hat{v}_{t}=E\left[v_{t}\right]
\end{gathered}
$$

Here the assumptions used to derive this equation are applied to the Heston model and the impact on option voluation is discussed.

The Heston-Nandi model is dotained by assuming $e=-1$

$$
\begin{gathered}
d x_{t}=-\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z \\
d v_{t}=-\lambda\left(v_{t}-\tau\right) d t-\eta \sqrt{v_{t}} d z
\end{gathered}
$$

which reduces the model to a single random variable

Local Variance in the Heston-Nandi Model

From the equation for $x_{t}$ it is seen that,

$$
\begin{aligned}
& d x_{t}=-\frac{v_{t}}{2} d t+\sqrt{v_{t}} d z \\
\Rightarrow & \sqrt{v}_{t} d z=d x_{t}+\frac{v_{t}}{2} d t
\end{aligned}
$$

so the $d z$ term can be eliminated from the equation for $v_{t}$

$$
\begin{aligned}
d v_{t} & =-\lambda\left(v_{t}-\tau\right) d t-\eta \sqrt{v_{t}} d z \\
& =-\lambda\left(v_{t}-\bar{v}\right) d t-\eta\left(d x_{t}+\frac{v_{t}}{\partial} d t\right) \\
& =-\lambda\left(v_{t}-\bar{v}\right) d t-\eta d x_{t}-\frac{\eta v_{t}}{\partial} d t
\end{aligned}
$$

$$
=\left[-U_{t}\left(\lambda+\frac{1}{2} \eta\right)+\lambda \bar{U}\right] d t-\eta d x_{t}
$$

let

$$
\lambda^{\prime}=\lambda+\frac{1}{2} y \quad \bar{v}^{\prime}=\frac{\lambda}{\lambda^{\prime}} \bar{v}
$$

then

$$
\begin{aligned}
d U_{t}= & {\left[-U_{t}\left(\lambda+\frac{1}{\partial} \eta\right)+\lambda \bar{U}\right] d t } \\
& -\eta d x_{t} \\
= & \left(-U_{t} \lambda^{\prime}+\lambda \bar{U}\right) d t-\eta d x_{t} \\
= & -\lambda^{\prime}\left(U_{t}-\frac{\lambda}{\lambda^{\prime}} \bar{U}\right) d t-\eta d x_{t} \\
= & -\lambda^{\prime}\left(U_{t}-\overline{U^{\prime}}\right) d t-\eta d x_{t}
\end{aligned}
$$

Thus

$$
d v_{t}=-\lambda^{\prime}\left(v_{t}-\bar{v}^{\prime}\right) d t-\eta d x_{t}
$$

Recall the local variance is given by
$u_{t}=\hat{v}_{t}^{\prime}+\rho \eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s$
For this case

$$
u_{t}=\hat{v}_{t}^{\prime}-\eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{t} \hat{v}_{s} e^{-\lambda^{\prime}(t-s)} d s
$$

where

$$
\begin{aligned}
& \hat{v}_{t}=\left(v_{0}-\bar{v}\right) e^{-\lambda t}+\bar{v} \\
& \hat{v}_{t}^{\prime}=\left(v_{0}-\sigma^{\prime}\right) e^{-\lambda^{\prime} t}+\bar{v}^{\prime}
\end{aligned}
$$

It follows that

$$
u_{T}=\hat{v}_{T}^{\prime}+\eta \frac{X_{T}}{\hat{\omega}_{T}} \int_{0}^{T} \hat{v}_{S} e^{-\lambda^{\prime}(T-S)} d s
$$

Consider the integral

$$
\begin{aligned}
& \int_{0}^{T} \hat{v}_{s} e^{-\lambda^{\prime}(T-s)} d s \\
= & \int_{0}^{T}\left[\left(v_{0}-\bar{v}\right) e^{-\lambda s}+\bar{v}\right] e^{-\lambda^{\prime}(T-s)} d s \\
= & e^{-\lambda^{\prime} T} \int_{0}^{T}\left(v_{0}-\bar{v}\right) e^{\left(\lambda^{\prime}-\lambda\right) s}+\bar{v} e^{\lambda^{\prime} s} d s \\
= & \left.e^{-\lambda^{\prime} T}\left(v_{0}-\bar{v}\right) \frac{e^{\left(\lambda^{\prime}-\lambda\right) s}}{\left(\lambda^{\prime}-\lambda\right)}\right|_{0} ^{T} \\
& +\left.\frac{\bar{v}}{\lambda^{\prime}} e^{\lambda^{\prime}}\right|_{0} ^{T} \\
= & e^{-\lambda^{\prime} T} \frac{\left(v_{0}-\bar{v}\right)}{\lambda^{\prime}-\lambda}\left[e^{\left(\lambda^{\prime}-\lambda\right) T}-1\right] \\
& +\frac{\bar{U}}{\lambda^{\prime}}\left(e^{\lambda^{\prime} T}-1\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{e^{-\lambda^{\prime} T} \lambda^{\prime}\left(v_{0}-\bar{v}\right)\left[e^{\left(\lambda^{\prime}-\lambda\right) T}-1\right]}{\lambda^{\prime}\left(\lambda^{\prime}-\lambda\right)} \\
& \quad+\frac{\left(\lambda^{\prime}-\lambda\right) \bar{v}\left(e^{\lambda^{\prime} T}-1\right)}{\lambda^{\prime}\left(\lambda^{\prime}-\lambda\right)} \\
& =\frac{1}{\lambda^{\prime}\left(\lambda^{\prime}-\lambda\right)}\left\{\lambda^{\prime}\left(v_{0}-\bar{v}\right) e^{-\lambda^{\prime} T} e^{\left(\lambda^{\prime}-\lambda\right) T}\right. \\
& \quad-e^{-\lambda^{\prime} T} \lambda^{\prime}\left(v_{0}-\bar{v}\right)+\left(\lambda^{\prime}-\lambda\right) \bar{v} e^{\lambda^{\prime} T} \\
& \left.\quad-\left(\lambda^{\prime}-\lambda\right) \bar{v}\right\} \\
& =\frac{1}{\lambda^{\prime}\left(\lambda^{\prime}-\lambda\right)}\left\{e^{-\lambda^{\top} T} \lambda^{\prime}\left(v_{0}-\bar{v}\right)\right. \\
& \quad-e^{-\lambda^{\top} T} \lambda^{\prime}\left(v_{0}-\bar{v}\right)
\end{aligned}
$$

I do not see how this will work out

Continuing with the result from

$$
\begin{aligned}
u_{T} & =\hat{v}_{T}^{\prime}+\eta \frac{x_{T}}{\hat{\omega}_{T}} \int_{0}^{T} \hat{v}_{S} e^{-\lambda^{\prime}(T-S)} d S \\
& =\left(v_{0}-\bar{v}^{\prime}\right) e^{-\lambda^{\prime} T}+\bar{v}^{\prime}-\eta x_{T}\left[\frac{1-e^{-\lambda^{\prime} T}}{\lambda T}\right]
\end{aligned}
$$

The implied volatility is given by

$$
\sigma_{B S}^{2}\left(K_{1} T\right) \approx \frac{1}{T} \int_{0}^{T} u_{t}\left(\bar{x}_{t}\right) d t
$$

## Adding Jumps

The Heston model does a good job of modeling option prices far from expration but as the options approach expiry it does not perform well. As options approach eppration the option price can fluctuate because of anticipation of large majes which are possible but are extremly unlikley in the Heston model because solatility is assumed to have a Gaussian distribution.

Jumps solve this problem by providing a model for large price moves near option expration.

## Jump Diffusion

The jump diffusion model assumes the stock price follows the SDE,

$$
d s_{t}=\mu s_{t} d t+\sigma s_{t} d z_{t}+(J-1) s_{t} d q_{t}
$$

let

$$
d q_{t}= \begin{cases}0 & \text { with probobility } 1-\lambda(t) d t \\ 1 & \text { with probility } \lambda(t) d t\end{cases}
$$

where $\lambda(t)$ is a Poisson process.
When $d q=1$ the process $S_{t}$ jumps from $s_{t}$ to $J s_{t}$. It is assumed that $d q_{t}$ and $d z_{t}$ are independent.
Following the proceedure used for stochastic valatility the valuation equation is derived by considering the hedging of
the replicating portfolio for a contingent daim.
For now it is assumed that $J$ is known.

The replicating portfolio is given by

$$
\Pi=V-\Delta S-\Delta_{1} V_{1}
$$

Where $U$ is the option being priced, $S$ is the undelying asset and $v_{1}$ is an asset with value that depends on the jump. The parameters $\Delta$ and $\Delta_{1}$ are the quantities of $s$ and $v_{1}$ contained in the portfolio.

From definition of the portfolio and assuming self - firancing so that $\Delta$ and $\Delta_{1}$ are assumed given at a given time $t$, it follows that

$$
d \pi=d v-\Delta d s_{t}-\Delta_{1} d v_{1}
$$

Assume $V\left(S_{t}, q_{t}, t\right)$ and $V_{1}\left(S_{t}, q_{t}, t\right)$ then

Now

$$
d v=\frac{\partial v}{\partial t} d t+\frac{\partial v}{\partial s} d s_{t}+\frac{1}{2} \frac{\partial^{2} v}{\partial s^{2}}\left(d s_{t}^{2}\right)
$$

$$
+\frac{\partial v}{\partial q} d q_{t}
$$

$$
\begin{aligned}
(d s)^{2} & =\left(\mu s_{t} d t+\sigma s_{t} d z_{t}+(J-1) s_{t} d q_{t}\right)^{2} \\
& =s_{t}^{2}\left(d z_{t}\right)^{2} \\
& =\sigma^{2} s_{t}^{2} d t
\end{aligned}
$$

So,

$$
\begin{aligned}
d v= & \frac{\partial v}{\partial t} d t+\frac{\partial v}{\partial s} d s_{t}+\frac{1}{2} \delta^{2} s_{t}^{2} \frac{\partial^{2} v}{\partial s^{2}} d t \\
& +\frac{\partial v}{\partial q} d q_{t}
\end{aligned}
$$

similarly,

$$
\begin{aligned}
d V_{1}= & \frac{\partial V_{1}}{\partial t} d t+\frac{\partial V_{1}}{\partial S} d S_{t}+\frac{1}{\partial} \delta^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S^{2}} d t \\
& +\frac{\partial V_{1}}{\partial G} d q_{t}
\end{aligned}
$$

and finaly define the continuous differential increment in asset price by

$$
d s_{t}^{c}=d s_{t}+(J-1) s_{t} d q_{t}
$$

This includes the stochastic portion and the jump

Bringing things together

$$
\begin{aligned}
d \pi= & d v-\Delta d s_{t}^{c}-\Delta_{1} d v_{1} \\
= & \frac{\partial v}{\partial t} d t+\frac{\partial v}{\partial s} d s_{t}+\frac{1}{\partial} \nabla^{2} s_{t}^{2} \frac{\partial^{2} v}{\partial s^{2}} d t \\
& +\frac{\partial v}{\partial q} d q_{t}
\end{aligned}
$$

$$
\begin{aligned}
& -\Delta\left(d s_{t}+(J-1) s_{t} d q_{t}\right) \\
& -\Delta_{1}\left(\frac{\partial v_{t}^{2}}{\partial t} d t+\frac{\partial v_{1}}{\partial s} d s_{t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v_{1}}{\partial s^{2}} d t\right. \\
& \left.+\frac{\partial v_{1}}{\partial q} d q_{t}\right) \\
& =\left(\frac{\partial v}{\partial t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v}{\partial s_{t}^{2}}\right) d t-\Delta_{1}\left(\frac{\partial v_{1}}{\partial t}+\right. \\
& \left.\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v_{1}}{\partial s_{t}^{2}}\right)+\left(\frac{\partial v}{\partial s}-\Delta_{1} \frac{\partial v_{1}}{\partial s}-\Delta\right) d s_{t}^{c}+ \\
& \left(\frac{\partial v}{\partial q}-\Delta(J-1) s_{t}-\Delta_{1} \frac{\partial v_{1}}{\partial q}\right) d q
\end{aligned}
$$

Recall that,
$d q_{t}= \begin{cases}0 & \text { with probobility } 1-\lambda(t) d t \\ 1 & \text { with probility } \lambda(t) d t\end{cases}$

It follows that

$$
\begin{aligned}
& \frac{\partial v}{\partial q}=v(J s, t)-v(s, t) \\
& \frac{\partial v_{1}}{\partial q}=v_{1}(J s, t)-v_{1}(s, t)
\end{aligned}
$$

So,

$$
\begin{aligned}
d \pi= & \frac{\left(\frac{\partial v}{\partial t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v}{\partial s_{t}^{2}}\right) d t}{} \frac{-\Delta_{1}\left(\frac{\partial v_{1}}{\partial t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v_{1}}{\partial s_{t}^{2}}\right) d t}{} \frac{+\left(\frac{\partial v}{\partial s}-\Delta_{1} \frac{\partial v_{1}}{\partial s}-\Delta\right) d s_{t}^{c}}{} \\
& +[v(J s, t)-v(s, t)- \\
& \Delta_{1}\left(v_{1}(J s, t)-v_{1}(s, t)\right)- \\
& \left.\Delta(J-1) s_{t}\right] d q
\end{aligned}
$$

Now for the portfolio to have no risk with respect to the asset price $s_{t}$ it must be that,

$$
\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}-\Delta=0
$$

and to eliminate the risk with respect to 9 it must be that,

$$
\begin{aligned}
& v(J s, t)-v(s, t)-\Delta_{1}\left(v_{1}(J s, t)-\right. \\
& \left.v_{1}(s, t)\right)-\Delta(J-1) s_{t}=0
\end{aligned}
$$

If these equations are satisfied

$$
\begin{aligned}
d \pi= & \left(\frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}\right) d t \\
& -\Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right) d t
\end{aligned}
$$

Since the risk in the asset price and $q$ has been eliminated the return is risk-free so must equal the risk-free return, $r$.

## Trues

$$
\begin{aligned}
d \Pi= & \left(\frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}\right) d t \\
& -\Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right) d t \\
= & r \pi d t \\
= & r\left(V-\Delta S-\Delta_{1} V_{1}\right) d t
\end{aligned}
$$

To go furthur expressions for $\Delta$ and $\Delta_{1}$ are required Also, let

$$
\delta V=V(J S, t)-V(S, t)
$$

then,

$$
\begin{aligned}
& \frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}-\Delta=0 \\
\Rightarrow & \Delta=\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}
\end{aligned}
$$

and

$$
\begin{aligned}
V & (J s, t)-v(s, t)-\Delta_{1}\left(v_{1}(J s, t)-\right. \\
V & \left.v_{1}(s, t)\right)-\Delta(J-1) s_{t}=0 \\
\Rightarrow & \delta v-\Delta_{1} \delta v_{1}-\Delta(J-1) s_{t}=0 \\
= & \delta v-\Delta_{1} \delta v_{1}-(J-1) s_{t}\left[\frac{\partial v}{\partial s}-\Delta_{1} \frac{\partial v_{1}}{\partial s}\right] \\
= & \delta v-\Delta_{1} \delta v_{1}-(J-1) s_{t} \frac{\partial v}{\partial s} \\
& +(J-1) s_{t} \Delta_{1} \frac{\partial v_{1}}{\partial s} \\
\Rightarrow & \delta v-(J-1) s_{t} \frac{\partial v}{\partial s}=\Delta_{1}\left(\delta v_{1}-(J-1) s_{t} \frac{\partial v_{1}}{\partial s}\right)
\end{aligned}
$$

$$
\Rightarrow \Delta_{1}=\frac{\delta v-(J-1) S_{t} \frac{\partial V}{\partial S}}{\delta V_{1}-(J-1) S_{t} \frac{\partial V}{\partial S}}
$$

So

$$
\begin{aligned}
& \Delta=\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S} \\
& =\frac{\partial V}{\partial S}-\frac{\partial V_{1}}{\partial S}\left[\frac{\delta V-(J-1) S_{t} \frac{\partial V}{\partial S}}{\delta V_{1}-(J-1) S_{t} \frac{\partial V_{1}}{\partial S}}\right]
\end{aligned}
$$

Thus

$$
\Delta_{1}=\frac{\delta v-(J-1) S_{t} \frac{\partial v}{\partial S}}{\delta v_{1}-(J-1) S_{t} \frac{\partial V_{1}}{\partial S}}
$$

$$
\Delta=\frac{\partial v}{\partial S}-\frac{\partial v_{1}}{\partial S}\left[\frac{\delta v-(J-1) S_{t} \frac{\partial v}{\partial S}}{\delta v_{1}-(J-1) S_{t} \frac{\partial V_{1}}{\partial S}}\right]
$$

Now, collecting $v$ and $v_{1}$ terms gives

$$
\begin{aligned}
d \pi= & \left(\frac{\partial v}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} v}{\partial S_{t}^{2}}\right) d t \\
& -\Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right) d t \\
= & r \pi d t \\
= & r\left(V-\Delta S-\Delta_{1} V_{1}\right) d t \\
\Rightarrow( & \left.\frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} v}{\partial S_{t}^{2}}\right) d t \\
- & \Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right) d t
\end{aligned}
$$

$$
\begin{aligned}
= & r\left(v-\Delta S-\Delta_{1} v_{1}\right) d t \\
\Rightarrow & \left(\frac{\partial v}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} v}{\partial S_{t}^{2}}\right)-r v= \\
& \Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right)-r \Delta S-r \Delta_{1} V_{1}
\end{aligned}
$$

but

$$
\Delta=\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}
$$

so

$$
\begin{aligned}
& \left(\frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}\right)-r V= \\
& \Delta_{1}\left(\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}\right)-r \Delta_{1} V_{1} \\
& -r S_{t}\left(\frac{\partial V}{\partial S}-\Delta_{1} \frac{\partial V_{1}}{\partial S}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =>\frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V}{\partial S}-r V \\
& =\Delta_{1}\left[\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V_{1}}{\partial S}-r V_{1}\right]
\end{aligned}
$$

Recall,

$$
\Delta_{1}=\frac{\delta V-(J-1) S_{t} \frac{\partial V}{\partial S}}{\delta V_{1}-(J-1) S_{t} \frac{\partial V_{1}}{\partial S}}
$$

It follows that

$$
\begin{aligned}
& \frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V}{\partial S}-r V \\
& =\frac{\delta V-(5-1) S_{t} \frac{\partial V}{\partial S}}{\delta V_{1}-(J-1) S_{t} \frac{\partial V}{\partial S}}
\end{aligned}
$$

$$
\begin{aligned}
& \frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V_{1}}{\partial S}-r V_{1} \\
\Rightarrow & \frac{\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V}{\partial S}-r V}{\delta V-(S-1) S_{t} \frac{\partial V}{\partial S}} \\
= & \frac{\frac{\partial V_{1}}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V_{1}}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V_{1}}{\partial S}-r V_{1}}{\delta V_{1}-(J-1) S_{t} \frac{\partial V_{1}}{\partial S}}
\end{aligned}
$$

Now the righthand side is a function only of $V_{1}$ and the left hardside is ority a function of $v$. The only way this is possible is if both sides are equal to the same function of the independent varidbles
$s_{t}$ and $t$, denote it by $-\lambda\left(s_{t}, t\right)$
It follows that

$$
\begin{aligned}
& \frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V}{\partial S}-r V \\
& +\lambda\left(S_{t}, t\right)\left[\delta V-(5-1) S_{t} \frac{\partial V}{\partial S}\right]=0
\end{aligned}
$$

## Uncertain Jump size

In the previous section it was assumed that the jump size was known.

This is unredistic so a distribution of jumps is used. A contenuas function of jumps is impractical since hedging the replication portfolio would require hedging against an infinite number of jumps
The solution is to use the expectation of the jump. Consider the asset price SDE

$$
d s_{t}=\mu s_{t} d t+\sigma s_{t} d z_{t}+(J-1) s_{t} d q_{t}
$$

If $\mu$ is the risk-free return then

$$
d s_{t}=r s_{t} d t+\sigma s_{t} d z_{t}+(J-1) s_{t} d q_{t}
$$

Taking expectation with respect to the risk-neutral drift gives,

$$
\begin{aligned}
E\left[d s_{t}\right] & =r s_{t} d t+E\left[(J-1) s_{t} d q\right] \\
& =r s_{t} d t+E[(J-1)] s_{t} E[d q]
\end{aligned}
$$

since 9 has a Poisson distribution with mean $\lambda(t)$,

$$
E[q]=\lambda(t)
$$

80

$$
E[d q]=\lambda(t) d t
$$

Putting things together gives

$$
\begin{aligned}
E\left[d S_{t}\right] & =r S_{t} d t+E[(J-1)] S_{t} E[d q] \\
& =r S_{t} d t+E[(J-1)] \lambda(t) d t
\end{aligned}
$$

It follows that

$$
S_{t}=S_{0} e^{\{r+\lambda(t) E[(J-1)]\} t}
$$

so the risk-neutral drift is given by

$$
r+\lambda(t) E[(J-1)]
$$

Recall that for a constant jump amplitude it was found that,

$$
\begin{aligned}
& \frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} V}{\partial S_{t}^{2}}+r S_{t} \frac{\partial V}{\partial S}-r V \\
& +\lambda\left(S_{t}, t\right)\left[\delta V-(5-1) S_{t} \frac{\partial V}{\partial S}\right]=0
\end{aligned}
$$

The result for rardom jump is obtained $b_{1}$ replocing the gump torm with the jump expectation, thus

$$
\begin{aligned}
& \frac{\partial V}{\partial t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} V}{\partial s_{t}^{2}}+r s_{t} \frac{\partial V}{\partial s}-r V \\
& +\lambda\left(s_{t}, t\right)\left\{E[\delta v]-E[J-1] s_{t} \frac{\partial V}{\partial s}\right\}=0
\end{aligned}
$$

where

$$
\delta v=v(\Delta s, t)-v(s, t)
$$

and $\lambda\left(s_{t, t}\right)$ is the mean of the $q(t)$ Poisson distribution.

## Characteristic Function Methods

In the previous section the Black-sholes equation for a random jump diffusion was show to be given by

$$
\begin{aligned}
& \frac{\partial v}{\partial t}+\frac{1}{2} \sigma^{2} s_{t}^{2} \frac{\partial^{2} v}{\partial s_{t}^{2}}+r s_{t} \frac{\partial v}{\partial s}-r v \\
+ & \lambda\left(s_{t}, t\right)\left\{E[\delta v]-E[J-1] s_{t} \frac{\partial v}{\partial s}\right\}=0
\end{aligned}
$$

where

$$
\delta v=v(\Delta s, t) \cdot v(s, t)
$$

and $\lambda\left(s_{t, t}\right)$ is the mean of the $q(t)$ Poisson distribution. Since the equation contains the expectation of the option value
it is an integro-differential equatetion. This leads to using Fourier transforms in the solution.

Recall that the charateristic function is the expectation of the Fourier transform since.

$$
\Phi(u)=E\left[e^{i u x_{T}}\right]
$$

The jume diffusion SDE for the asset price is given by

$$
\begin{aligned}
d s_{t}= & (r+\lambda(t) E[(J-1)]) s_{t} d t \\
& +\sigma s_{t} d z \\
\Rightarrow \frac{d s_{t}}{s_{t}}= & (r+\lambda(t) E[(J-1)]) d t \\
& +\sigma s_{t} d z
\end{aligned}
$$

This is an example of a Lévy process which are jump processes.
Before defining a le'vy process a cádla'g function is defined.

## Càdlàs Function

A cádiag function is a function that is continuous from the right with a limit from the left. Below are plots of examples of cádlog functions.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-348.jpg?height=420&width=1055&top_left_y=665&top_left_x=257)
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-348.jpg?height=392&width=1053&top_left_y=1104&top_left_x=259)
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-348.jpg?height=404&width=1057&top_left_y=1495&top_left_x=259)

From these examples it is seen that codlas fundtions include continuous functions as well a functions with jump discontinuities. This motivates their use here.

Now a le'vy process can be defined,

## Lévy Process

A Le'uy process is a continuous in probability, cadlag stochaslic process $x(t), t>0$ with independent incremenls and $x(0)=0$.

A Lévy process can be written as the sum of a linear drift, a Brownian motion and a jump process. Which is the process being discussed The charateristic function for a leivy process is given by the lévy-Khintchine Representation

## Lévy - Khintchine Representation

If $x_{t}$ is a lévy process, and if Le'vy density $\rho(x)$ is well behaved at the origin, its characteristic function

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}}\right]
$$

has the representation

$$
\begin{aligned}
\Phi_{T}(u)= & \exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
& \left.+T S\left[e^{i u s}-1\right] e(s) d s\right\}
\end{aligned}
$$

To evaluate the drift term it is assumed that the risk-neutral expectation of the asset price is the forward price,

$$
E\left[s_{t}\right]=s_{0} e^{\int_{0}^{t} \mu(s) d s}
$$

thus

$$
\begin{aligned}
E\left[x_{T}\right] & =\ln \frac{E\left[S_{T}\right]}{S_{0}} \\
& =\ln e^{S_{0}^{T}} \mu(s) d s \\
& =\int_{0}^{T} \mu(s) d s
\end{aligned}
$$

It is assumed that $\mu=0$ so

$$
E\left[X_{T}\right]=0
$$

It follows that

$$
\begin{aligned}
\Phi(-i) & =E\left[e^{i(-i) x_{T}}\right] \\
& =E\left[e^{x_{T}}\right] \\
& =1
\end{aligned}
$$

Trus

$$
\Phi(-\bar{i})=1
$$

This expriession can be used to determine $\omega$.

## Black-Scholes Charateristic Function

The characteristic function for the Black-Sholes model is botn directly and using lévyKhintchen Representation.
In the Black-sholes model the asset price satisfres the SDE

$$
d S_{t}=\mu S_{t} d t+\sigma S_{t} d z_{t}
$$

where

$$
Z_{t} \sim \operatorname{Normal}(0, t)
$$

Consider the log asset price

$$
x_{t}=\ln s_{t}
$$

using the itô formula
$d x_{t}=\frac{\partial x_{t}}{\partial s_{t}} d s_{t}+\frac{1}{2} \frac{\partial^{2} x_{t}}{\partial s_{t}^{2}}\left(d s_{t}\right)^{2}$

Now

$$
\begin{aligned}
\left(d s_{t}\right)^{2}= & \left(\mu s_{t} d t+\sigma s_{t} d z_{t}\right)^{2} \\
= & \mu^{2} s_{t}^{2}(d t)^{2} \\
& +2 \mu \sigma s_{t}^{2} d t d z_{t} \\
& +\sigma^{2} s_{t}^{2}\left(d z_{t}\right)^{2}
\end{aligned}
$$

recall

$$
d z=\sqrt{d t}
$$

so to lowest order

$$
\left(d S_{t}\right)^{2}=\sigma^{2} S_{t}^{2} d t
$$

It follows that

$$
d x_{t}=\frac{\partial x_{t}}{\partial S_{t}} d S_{t}+\frac{1}{2} \sigma^{2} S_{t}^{2} \frac{\partial^{2} x_{t}}{\partial S_{t}^{2}} d t
$$

Now,

$$
\frac{\partial x_{t}}{\partial s_{t}}=\frac{1}{s_{t}} \quad \frac{\partial^{2} x_{t}}{\partial s_{t}^{2}}=-\frac{1}{s_{t}^{2}}
$$

50

$$
d x_{t}=\frac{1}{s_{t}} d s_{t}-\frac{1}{2} \sigma^{2} d t
$$

but

$$
d S_{t}=\mu S_{t} d t+\sigma S_{t} d z_{t}
$$

80

$$
\begin{aligned}
d x_{t}= & \frac{1}{S_{t}}\left(\mu S_{t} d t+\sigma S_{t} d z_{t}\right) \\
& -\frac{1}{2} \sigma^{2} d t \\
= & \left(\mu-\frac{1}{2} \sigma^{2}\right) d t+\sigma d z_{t}
\end{aligned}
$$

Since

$$
z_{t} \sim \operatorname{Normal}(0, t)
$$

It follows that $x_{t}$ has a normal distribution with meen, if $\mu$ and $\sigma$ are constant.

$$
\left(\mu-\frac{1}{2} \sigma^{2}\right) t
$$

and variance

$$
\sigma^{2} t
$$

where

$$
\ln x_{T}=\ln \frac{S_{T}}{S_{0}}
$$

consider the case $t=T$. It follows that the PDF is given by
$P\left(x_{T}\right)=\frac{1}{\sqrt{2 \pi \sigma^{2} T}} \exp \left\{-\left[\frac{x_{\tau}-\left(\mu+\frac{1}{2} \sigma^{2}\right) T}{2 \sigma^{2} T}\right]^{2}\right\}$
This is also the risk-neutral PDF
Now the charateristic function is given by

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}}\right]=\int_{-\alpha}^{\infty} e^{i u x_{T}} p\left(x_{T}\right) d x_{T}
$$

$$
\begin{aligned}
=\frac{1}{\sqrt{2 \pi \sigma^{2}} T} & \int_{-\infty}^{\infty} \exp \left\{i \omega x_{T}\right. \\
& -\frac{\left.\left[\frac{x_{T}}{2 \sigma^{2} T}\left(\mu+\frac{1}{2} \sigma^{2}\right) T\right]^{2}\right\}}{d x_{T}}
\end{aligned}
$$

consider the argument

$$
c u x_{T}-\frac{\left[x_{T}-\left(\mu+\frac{1}{2} \sigma^{2}\right) T\right]^{2}}{2 \sigma^{2} T}
$$

let

$$
\hat{\sigma}^{2}=\sigma^{2} T \quad \hat{\mu}=\mu T+\frac{1}{2} \hat{\sigma}^{2}
$$

Then

$$
\begin{aligned}
& i u x_{T}-\frac{\left(x_{T}-\hat{\mu}\right)^{2}}{\partial \hat{\sigma}^{2}} \\
= & \frac{\partial i u \hat{\sigma}^{2} x_{T}-x_{T}^{2}+\partial \hat{\mu} x_{T}-\hat{\mu}^{2}}{\partial \hat{\sigma}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
=-\frac{1}{2 \hat{\sigma}^{2}} & {\left[x_{T}^{2}-2 x_{T}\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)+\hat{\mu}^{2}\right] } \\
=-\frac{1}{2 \hat{\sigma}^{2}} & {\left[x_{T}^{2}-2 x_{T}\left(\hat{\mu}+\bar{c} u \hat{\sigma}^{2}\right)+\right.} \\
& +\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right)^{2}-\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right)^{2} \\
& \left.+\hat{\mu}^{2}\right] \\
=-\frac{1}{2 \hat{\sigma}^{2}}[ & x_{T}^{2}-2\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right) \\
& \left.+\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right)^{2}\right] \\
& +\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right)^{2}-\hat{\mu}^{2} \\
=-\frac{1}{2 \hat{\sigma}^{2}} & {\left[x_{T}-\left(\hat{\mu}+\overline{c u \hat{\sigma}^{2}}\right)\right]^{2} } \\
& +\frac{\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)^{2}-\hat{\mu}^{2}}{2 \hat{\sigma}^{2}} \\
=-\frac{1}{2 \hat{\sigma}^{2}} & {\left[x_{T}-\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)\right]^{2} } \\
& +\frac{\hat{\mu}^{2}+2 \overline{c u} \hat{\mu}^{2}-\hat{u}^{2} \hat{\sigma}^{4}-\hat{\mu}^{2}}{\partial \hat{\sigma}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
=\frac{-1}{2 \hat{\sigma}^{2}} & {\left[x_{T}-\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)\right]^{2} } \\
& +\frac{\hat{\mu}^{2}+2 \bar{u} \hat{\mu} \hat{\sigma}^{2}-u^{2} \hat{\sigma}^{4}-\hat{\mu}^{2}}{\partial \hat{\sigma}^{2}} \\
=-\frac{1}{2 \hat{\sigma}^{2}} & {\left[x_{T}-\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)\right]^{2} } \\
& +\frac{2 i u \hat{\mu} \hat{\sigma}^{2}-u^{2} \hat{\sigma}^{4}}{2 \hat{\sigma}^{2}}
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
\frac{1}{2 \pi \sigma^{2} T} & \int_{-\infty}^{\infty} \exp \left\{i u x_{T}\right. \\
& \left.-\left[\frac{x_{T}-\left(\mu+\frac{1}{2} \sigma^{2}\right) T}{2 \sigma^{2} T}\right]^{2}\right\} d x_{T} \\
=\frac{1}{\sqrt{2 \hat{\sigma}^{2}}} & \int_{-\infty}^{\infty} \exp \left\{\frac{\left[x_{T}-\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)\right]^{2}}{2 \hat{\sigma}^{2}}\right. \\
& \left.\frac{2 i u \hat{\mu} \hat{\sigma}^{2}-u^{2} \hat{\sigma}^{4}}{2 \hat{\sigma}^{2}}\right\} d x_{T}
\end{aligned}
$$

$$
\begin{aligned}
& =\exp \left\{\frac{2 i u \hat{\mu} \hat{\sigma}^{2}-u^{2} \hat{\sigma}^{4}}{2 \hat{\sigma}^{2}}\right\} \\
& \frac{1}{2 \hat{\sigma}^{2}} \int_{-\infty}^{\infty} \exp \left\{\frac{\left[x_{T}-\left(\hat{\mu}+i u \hat{\sigma}^{2}\right)\right]^{2}}{2 \hat{\sigma}^{2}}\right\} d x_{T} \\
& =\exp \left\{\frac{2 i u \hat{\mu} \hat{\sigma}^{2}-u^{2} \hat{\sigma}^{4}}{2 \hat{\sigma}^{2}}\right\} \\
& =\exp \left(i u \hat{\mu}-\frac{1}{2} u^{2} \hat{\sigma}^{2}\right)
\end{aligned}
$$

but

$$
\hat{\sigma}^{2}=\sigma^{2} T \quad \hat{\mu}=\mu T+\frac{1}{2} \hat{\sigma}^{2}
$$

So

$$
\begin{gathered}
\Phi_{T}(u)=\exp \left[i u\left(\mu T+\frac{1}{2} \sigma^{2} T\right)\right. \\
\left.-\frac{1}{2} u^{2} \sigma^{2} T\right]
\end{gathered}
$$

$$
=\exp \left\{u\left[i\left(\mu+\frac{1}{2} \sigma^{2}\right) T-\frac{1}{2} u \sigma^{2} T\right]\right\}
$$

## Thus

$$
\Phi_{T}(u)=\exp \left\{u\left[i\left(\mu+\frac{1}{2} \sigma^{2}\right) T-\frac{1}{2} u \sigma^{2} T\right]\right\}
$$

Consider the case $\mu=0$

$$
\begin{aligned}
\Phi_{T}(u) & =\exp \left[\frac{1}{2} i u \sigma^{2} T-\frac{1}{2} u^{2} \sigma^{2} T\right] \\
& =\exp \left[-\frac{1}{2} u \sigma^{2} T(u+i)\right]
\end{aligned}
$$

Recall the Le'vy-Khintchine representation,

$$
\begin{aligned}
\Phi_{T}(u)=\exp & \left\{i u \omega T-\frac{1}{\partial} u^{2} \sigma^{2} T\right. \\
& \left.+T S\left[e^{i u s}-1\right] e(s) d s\right\}
\end{aligned}
$$

Since Black Scholes has no jumps $e(s)=0$ thus

$$
\Phi_{T}(u)=\exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right\}
$$

using

$$
\Phi_{\tau}(-i)=l
$$

gives

$$
\begin{aligned}
& \exp \left\{\omega T+\frac{1}{2} \sigma^{2} T\right\}=1 \\
& =\Rightarrow \omega=-\frac{1}{2} \sigma^{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\Phi_{T}(u) & =\exp \left\{-i u \frac{\sigma^{2}}{2} T-\frac{1}{2} u^{2} \sigma^{2} T\right\} \\
& =\exp \left\{-\frac{1}{2} \sigma^{2} T u(u+i)\right\}
\end{aligned}
$$

which is same as obtained by integration.

## Heston Model Charateristic Function

Previously it was shown that the Heston model charateristic function is given by,

$$
\begin{gathered}
\Phi_{T}(R)=\exp \left[c_{0}(u, \tau) \bar{v}+D_{0}(u, \tau) v\right] \\
D_{j}(u, \tau)=r_{-} \frac{\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)} \\
c_{j}(u, \tau)=\lambda\left\{r_{-} \tau-\frac{2}{\eta^{2}} \ln \left(\frac{1-g e^{-d \tau}}{1-g}\right)\right\}
\end{gathered}
$$

where

$$
g=\frac{r_{-}}{r_{t}}
$$

$$
\begin{aligned}
& r_{ \pm}= \frac{\beta \pm \sqrt{\beta^{2}-4 \alpha r}}{2 r} \\
&= \frac{\beta \pm d}{\eta^{2}} \\
& d= \sqrt{\beta^{2} \cdot 4 \alpha r} \\
& \alpha=-\frac{u^{2}}{2}-\frac{i u}{2}+i j u \\
& \beta= \lambda-\rho \eta i-\rho n i u \\
& r=\frac{\eta^{2}}{2}
\end{aligned}
$$

## Merton's Jump Diffussion Model charateristic Function

In the Merton Jump Diffusion Model the jump-size is assumed to be lognormally distributed with mean log-jump $\alpha$ and standard deviation $\delta$.
It follows that the asset-price SDE is given by
$d S_{t}=\mu S_{t} d t+\sigma S_{t} d z_{t}+\left(e^{\alpha+\delta \varepsilon}-1\right) S_{t} d q$
where $\varepsilon \sim \operatorname{Normal}(0,1)$
For this model the log asset price is a Lévy process. It follows that the Le'vy-Khintchine representation cand be used to compute the moment generating function. From
the SDE

$$
\begin{gathered}
\frac{d s_{t}}{s_{t}}=d \ln s_{t}=\mu d t+\sigma d z_{t} \\
+\left(e^{\alpha+\delta \varepsilon}-1\right) d q
\end{gathered}
$$

the los asset price is given by

$$
x_{t}=\ln \frac{S_{t}}{S_{0}}
$$

it follows that

$$
d x_{t}=\mu d t+\sigma d z_{t}+\left(e^{\alpha+\delta \varepsilon}-1\right) d q
$$

Now $j$ has a lognomal distribution but 9 has a Poisson distribution with constant parameter $\lambda$, so,

$$
d q=\lambda d t
$$

so

$$
d x_{t}=\mu d t+\sigma d z_{t}+\left(e^{\alpha+\delta \varepsilon}-1\right) \lambda d t
$$

From the Le'vy-Khintchine representation the Fourrer transform of the probability distribution of $x_{T}$ is the moment generating and is groen $b_{y}$

$$
\begin{aligned}
\Phi_{T}(u)= & E\left[e^{i u x_{T}}\right] \\
= & \exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
& \left.+T \int\left[e^{i u s}-1\right] e(s) d s\right\}
\end{aligned}
$$

Now since

$$
J=e^{\alpha+\delta \varepsilon}
$$

and
$\varepsilon \sim \operatorname{Normal}(0,1)$
It follows that $J$ is lognormal with distribution
$J \sim \operatorname{Normal}(\alpha, \delta)=\frac{1}{\sqrt{2 \pi \delta^{2}}} e^{-(\alpha-\delta)^{2} / 2 \delta^{2}}$

50

$$
e^{(s)}=\frac{\lambda}{\sqrt{2 \pi \delta^{2}}} e^{-(\alpha-s)^{2} / 2 \delta^{2}}
$$

Applying the Le'vy-Khintchine representation groes,

$$
\begin{aligned}
& \Phi(u)=\exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
& \left.+T \int\left[e^{i u s}-1\right] \rho(s) d s\right\} \\
& =\exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
& \left.+T \int_{-\infty}^{\infty}\left(e^{i u s}-1\right) \frac{\lambda}{\sqrt{2 \pi \delta^{2}}} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s\right\}
\end{aligned}
$$

Consider the integral,
$T \int_{-\infty}^{\infty}\left(e^{i u s}-1\right) \frac{\lambda}{\sqrt{2 \pi \delta^{2}}} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s$

$$
\begin{aligned}
=T \lambda & {\left[\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty} e^{i u s} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s\right.} \\
& \left.\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s\right]
\end{aligned}
$$

Now the second integral is given by

$$
\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s=1
$$

And bock to the first integral,
$\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty} e^{i u s} e^{-(\alpha-s)^{2} / 2 \delta^{2}} d s$
$=\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty} \exp \left\{i \omega s-\frac{(\alpha-s)^{2}}{\partial \delta^{2}}\right\} d s$
consider the exponental argument,

$$
\begin{aligned}
& i u s-\frac{(\alpha-s)^{2}}{2 \delta^{2}}=\frac{2 i \delta^{2} u s-(\alpha-s)^{2}}{2 \delta^{2}} \\
& =\frac{2 i \delta^{2} u s-\left(\alpha^{2}-2 \alpha s+s^{2}\right)}{2 \delta^{2}} \\
& =\frac{2 i \delta^{2} u s+2 \alpha s-s^{2}-\alpha^{2}}{2 \delta^{2}} \\
& =\frac{-\left[\delta^{2}-2 s\left(\alpha+i u \delta^{2}\right)\right]-\alpha^{2}}{2 \delta^{2}}
\end{aligned}
$$

let $b=\alpha+i u \delta^{2}$ then the above expression becomes

$$
\begin{aligned}
& -\frac{\left(s^{2}-2 s b\right)-\alpha^{2}}{2 \delta^{2}} \\
= & -\frac{\left(s^{2}-2 s b+b^{2}-b^{2}\right)-\alpha^{2}}{2 \delta^{2}} \\
= & -\frac{\left(s^{2}-2 s b+b^{2}\right)+b^{2}-\alpha^{2}}{2 \delta^{2}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-(s-b)^{2}+b^{2}-\alpha^{2}}{2 \delta^{2}} \\
& =\frac{-(s-b)^{2}}{2 \delta^{2}}+\frac{b^{2}-\alpha^{2}}{2 \delta^{2}} \\
& =\frac{-\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}}+\frac{\left(\alpha+i u \delta^{2}\right)^{2}-\alpha^{2}}{2 \delta^{2}} \\
& =\frac{-\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}} \\
& \quad+\frac{\alpha^{2}+2 i u \alpha \delta^{2}-u^{2} \delta^{4}-\alpha^{2}}{2 \delta^{2}} \\
& =\frac{-\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}}+i u \alpha-\frac{u^{2} \delta^{2}}{2}
\end{aligned}
$$

Now back to the integral,

$$
\frac{1}{2 \pi \delta^{2}} \int_{-\infty}^{\infty} \exp \left\{i u s-\frac{(\alpha-s)^{2}}{\partial \delta^{2}}\right\} d s
$$

$$
\begin{aligned}
& =\frac{1}{2 \pi \delta^{2}} \int_{-\Delta}^{\infty} \exp \left\{\frac{\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}}\right. \\
& \left.\quad i u \alpha-\frac{u^{2} \delta^{2}}{2}\right\} d s \\
& =e^{i u \alpha-u^{2} \delta^{2} / 2} \frac{1}{\sqrt{2 \pi \delta^{2}}} \\
& \quad \int_{-\alpha}^{\infty} \exp \left\{\frac{\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}} d s\right.
\end{aligned}
$$

but

$$
\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\alpha}^{\beta} \exp \left\{\frac{\left[s-\left(\alpha+i u \delta^{2}\right)\right]^{2}}{2 \delta^{2}} d s=1\right.
$$

Putting the integral together gives

$$
T \int_{-\infty}^{\infty}\left(e^{i u s}-1\right) \frac{\lambda}{\sqrt{\partial \pi \delta^{2}}} e^{-(\alpha-s)^{2} / \partial \delta^{2}} d s
$$

$$
\begin{aligned}
=T \lambda & {\left[e^{i u d-u^{2} s^{2} / 2}-1\right] } \\
\text { Thus } & \\
\Phi_{T}(u)= & \exp \left\{i u \omega T-\frac{1}{2} u^{2} s^{2} T\right. \\
& \left.+T S\left[e^{i u s}-1\right] e(s) d s\right\} \\
= & \exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
& \left.+T \lambda\left(e^{i u d-u^{2} s^{2} / 2}-1\right)\right\}
\end{aligned}
$$

To determine $\omega$ the boundary condition is used,

$$
\Phi_{1}(-i)=1
$$

It follows that the exponential argument is zero,

$$
\begin{gathered}
i U \omega T-\frac{1}{2} u^{2} \sigma^{2} T+T \lambda\left(e^{i u d-u^{2} \delta^{2} / 2}-1\right)=0 \\
\Rightarrow i u \omega T=\frac{1}{2} u^{2} \sigma^{2} T- \\
T \lambda\left(e^{i u d-u^{2} \delta^{2} / 2}-1\right) \\
\Rightarrow \omega=\frac{1}{i u T}\left[\frac{1}{2} u^{2} \sigma^{2} T-\right. \\
\left.T \lambda\left(e^{i u d-u^{2} \delta^{2} / 2}-1\right)\right]
\end{gathered}
$$

but $u=-i$, so

$$
\begin{aligned}
\omega & =\frac{1}{T}\left[-\frac{1}{2} \sigma^{2} T-T \lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)\right] \\
& =-\frac{1}{2} \gamma^{2}-\lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)
\end{aligned}
$$

It follows that the characteristic function is given by

$$
\begin{aligned}
& \Phi_{T}(u)= \exp \left\{i u \omega T-\frac{1}{2} u^{2} \sigma^{2} T\right. \\
&\left.+T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)\right\} \\
&=\exp \left\{-i u T\left[\frac{1}{2} \sigma^{2}+\lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)\right]\right. \\
&\left.-\frac{1}{2} u^{2} \delta^{2} T+T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)\right\} \\
&=\exp \left\{-i \frac{u T \sigma^{2}-\frac{1}{2} u^{2} \sigma^{2} T}{}\right. \\
&-i u T \lambda\left(e^{\alpha+\delta^{2} / 2}-1\right) \\
&\left.+T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)\right\} \\
&=\exp \left\{-\frac{1}{2} u(i+u) \sigma^{2} T-i u T \lambda\left(e^{\alpha+\delta^{2} / 2}\right.\right. \\
&\left.-1)+T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)\right\}
\end{aligned}
$$

Thus, the charateristic function for the Merton model is given by,

$$
\begin{aligned}
\Phi_{T}(u)=\exp & \left\{-\frac{1}{2} u(i+u) \sigma^{2} T\right. \\
& -i u T \lambda\left(e^{\alpha+\delta^{2} / 2}-1\right) \\
& \left.+T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)\right\}
\end{aligned}
$$

## Computing option Prices from Characteristra function

The expression used for option pricing is given by
$C(S, K, T)=S$.

$$
\sqrt{S K} \frac{1}{\pi} \int_{0}^{A} \frac{\operatorname{Re}\left[e^{-i u k^{2}} \Phi_{T}(u-i / 2)\right]}{u^{2}+1 / 4} d u
$$

where $s$ is the asset price, $k$ the option strike price, $T$ the option expiny and

$$
R=\ln \frac{K}{S_{t}}
$$

In the following discussion this equation will be derived.

Consider a covered call position, where the seller of the aption, short side, also purchases the

## asset.

The payoff of the covered call will be $s_{T}$ if the option expres out-of the-money, $S_{7}<K$ and $K$ if the option expires in-the-money since the option seller will owe the optor buyer $s_{T}-k$. It follows that the payoff for the covered call portfolio is given by

$$
\min \left(S_{\tau}, K\right)
$$

benote the replicating portfolid of the covered call position by $G(k, \tau)$ where

$$
\tau=T-t
$$

Consider the Fourier transform of $G(k, \tau)$ with respect to $k$

$$
\hat{C}(u, \tau)=\int_{-\infty}^{\infty} e^{i u k} G(k, \tau) d k
$$

Now the log asset price is given by

$$
x_{T}=\ln \frac{S_{I}}{S_{t}}
$$

and the portfolio payoff is given by

$$
\min \left(S_{\tau}, K\right)
$$

as a function of $x_{T}$ and $k$

$$
\begin{aligned}
& S_{t} \min \left(\frac{S_{I}}{S_{t}}, \frac{k}{S_{t}}\right)=S_{t} \min \left(e^{\ln \frac{S_{T}}{S_{t}}}, e^{\ln \frac{k}{S_{t}}}\right) \\
& =S_{t} \min \left(e^{x_{T}}, e^{k}\right)
\end{aligned}
$$

The portforio value at time $t$ is the expected return given the current asset price.

It follows that

$$
x_{t}=\ln \frac{s_{t}}{s_{t}}=0
$$

tnus,

$$
\begin{aligned}
G(k, \tau) & =E\left[S_{t} \min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right] \\
& =S_{t} E\left[\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right]
\end{aligned}
$$

it follows that

$$
\begin{aligned}
& \hat{G}(u, \tau)=\int_{-\infty}^{\infty} e^{i u k} G(k, \tau) d k \\
= & S_{t} \int_{-\infty}^{\infty} e^{i u k} E\left[\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right] d k \\
=\frac{1}{S_{t}} \hat{C}(u, \tau)= & \\
& \int_{-\infty}^{\infty} e^{i u k} E\left[\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right] d k
\end{aligned}
$$

Since $s_{t}$ is given $k$ is not random so
$\frac{1}{S_{t}} \hat{C}(u, \tau)=$

$$
E\left[\int_{-\infty}^{\infty} e^{i u k} \min \left(e^{x_{T}}, e k\right) d k\left(x_{t}=0\right]\right.
$$

Now if $k<x_{T}$,

$$
\min \left(e^{x_{T}}, e^{k}\right)=e^{k}
$$

and if $X_{T} \geqslant K$

$$
\min \left(e^{x_{T}}, e^{k}\right)=e^{x_{T}}
$$

It follows

$$
\begin{array}{r}
\frac{1}{S_{t}} \hat{C}(u, \tau)=E\left[\int_{-\infty}^{x_{T}} e^{i u k} e^{k} d k\right. \\
\left.+\int_{x_{T}}^{\infty} e^{i u k} e^{x_{T}} d k \mid x_{t}=0\right]
\end{array}
$$

$$
\begin{aligned}
=E & {\left[\begin{array}{l}
\int_{-\infty}^{x_{T}} e^{k(1+i u)} d k \\
\left.+e^{x_{T}} \int_{x_{T}}^{\infty} e^{i u k} d k \mid x_{t}=0\right]
\end{array}\right.} \\
=E & {\left[\frac{\left.\left.e^{k(1+i u)}\right|^{x_{T}}+\left.\frac{e^{x_{T}}}{i u} e^{i u k}\right|_{x_{T}} ^{\infty}\right]}{1+i u}-_{\infty}\right] }
\end{aligned}
$$

consider the first exponential term evcluated as $k \rightarrow-\infty$

$$
\begin{aligned}
& e^{k(1+i u)}=e^{k} e^{k i u}=e^{k} e^{k i(\operatorname{Re}(u)+i \operatorname{Im}(u))} \\
= & e^{k} e^{i k \operatorname{Re}(u)} e^{-k \operatorname{Im}(u)}=e^{k(1-\operatorname{Im}(u))} e^{i k \operatorname{Re}(u)} \\
& \rightarrow 0 \\
\text { If } & \operatorname{Im}(u)<1 .
\end{aligned}
$$

and for second term as $k \rightarrow \alpha$

$$
\begin{aligned}
e^{i u k} & =e^{k i(\operatorname{Re}(u)+i \operatorname{Im}(u))} \\
& =e^{i k \operatorname{Re}(u)} e^{-k \operatorname{Im}(u)} \rightarrow 0
\end{aligned}
$$

If $\operatorname{Im}(u)<0$. It follows that

$$
\begin{aligned}
& \frac{1}{S_{t}} \hat{C}(u, \tau)=E\left[\left.\frac{e^{x_{T}(1+i u)}}{1+i u}-\frac{e^{x_{T}(1+i u)}}{i u} \right\rvert\, x_{t}=0\right] \\
& =E\left[\left.\frac{i u e^{x_{T}(1+i u)}-(1+i u) e^{x_{T}(1+i u)}}{i u(1+i u)} \right\rvert\, x_{t}=0\right] \\
& =E\left[\left.\frac{-i u e^{x_{T}(1+i u)}}{u(i-u)} \right\rvert\, x_{t}=0\right] \\
& =\frac{1}{u(u-i)} E\left[e^{x_{T}(1+i u)} \mid x_{t}=0\right]
\end{aligned}
$$

Recall that the cracracteristic function is defined by

$$
\Phi_{T}(u)=E\left[e^{i u x_{T}} \mid x_{t}=0\right]
$$

It follows that

$$
\begin{aligned}
E\left[e^{x_{T}(1+i u)} \mid x_{t}=0\right] & =E\left[e^{i(u-i) x_{T}} \mid x_{t}=0\right] \\
& =\Phi_{T}(u-i)
\end{aligned}
$$

Thus,

$$
\frac{1}{S_{t}} \hat{C}(u, \tau)=\frac{1}{u(u-i)} \Phi_{T}(u-i)
$$

Now the return on the covered call portfolio is the inverse fourier transform of $\hat{G}(u, \tau)$. This integral is evaluated using contair integration methods. The integral is evaluated along the line $\operatorname{Im}(u)=1 / 2$. It will later be seen that this chorce makes things work out for the Black-Sholes model. It follows that,

$$
\begin{aligned}
& G(k, \tau)=\frac{1}{2 \pi} \int_{-\infty+i \frac{1}{2}}^{\infty+i \frac{1}{2}} \hat{C}(u, \tau) e^{-i u k} d u \\
& =\frac{1}{2 \pi} \int_{-\infty+L_{1} \frac{1}{2}}^{\alpha+\frac{1}{2}} \frac{1}{u(u-i)} \Phi_{T}(u-i) e^{-i u k} d u \\
& =\frac{1}{2 \pi} S_{t} \int_{-\infty+i \frac{1}{2}}^{\infty+i \frac{1}{2}} \frac{1}{u(u-i)} \Phi_{T}(u \cdot i) e^{-i u k} d u
\end{aligned}
$$

let

$$
\omega=u-i \frac{1}{2} \quad d \omega=d u
$$

$$
\begin{aligned}
& \Rightarrow u=\omega+i \frac{1}{2} \\
& u-i=\omega+i \frac{1}{2}-i=\omega \cdot i \frac{1}{2}
\end{aligned}
$$

80

$$
e^{-i \omega k}=e^{-i(\omega+i b) k}=e^{-i \omega k} e^{k / 2}
$$

but

$$
R=\ln \frac{K}{S_{t}}
$$

50

$$
\begin{aligned}
e^{-i \omega k} & =e^{-i \omega k} e^{\frac{1}{2} \ln \frac{k}{s_{t}}} \\
& =e^{-i \omega k}\left(e^{\left.\ln \frac{k}{s_{t}}\right)^{1 / 2}}\right. \\
& =\sqrt{\frac{k}{s_{t}}} e^{-i \omega k}
\end{aligned}
$$

putting things together

$$
\begin{aligned}
& G(k, \tau)= \\
& \quad \frac{S_{t}}{\partial \pi} \sqrt{\frac{k}{S_{t}}} \int_{-\infty}^{\infty} \frac{e^{-i \omega k}}{\left(\omega+i \frac{1}{2}\right)\left(\omega-i \frac{1}{2}\right)} \Phi_{T}\left(\omega-i \frac{1}{\partial}\right) d \omega \\
& \quad=\sqrt{\frac{S_{t} k}{\partial \pi}} \int_{-\infty}^{\infty} \frac{e^{-i \omega k}}{\left(\omega^{2}+\frac{1}{4}\right)} \Phi_{T}\left(\omega-i \frac{1}{\partial}\right) d \omega
\end{aligned}
$$

Next consider the partion function,

$$
\begin{aligned}
& \Phi_{T}(u)=E\left[e^{i u x_{T}} \mid x_{t}=0\right] \\
\Rightarrow & \Phi_{T}(u)=E\left[e^{-i u x_{T}} \mid x_{t}=0\right]=\Phi_{T}^{*}(u)
\end{aligned}
$$

where $\Phi^{*}(u)$ is the complex conjugate of $\Phi(\omega)$, now

$$
\begin{aligned}
G(k, \tau)= & \frac{\sqrt{S_{t} k}}{2 \pi} \int_{-\infty}^{\infty} \frac{e^{-i u k}}{\left(u^{2}+t_{1}\right)} \Phi_{T}\left(u-i_{2}\right) d u \\
=\frac{\sqrt{S_{t} k}}{2 \pi}\{ & \left\{\int_{-\infty}^{0} \frac{e^{-i u k}}{\left(u^{2}+t_{1}\right)} \Phi_{T}\left(u-i_{2}\right) d u\right. \\
& \left.+\int_{0}^{\infty} \frac{e^{-i u k}}{\left(u^{2}+t_{1}\right)} \Phi_{T}\left(u \cdot i_{2}\right) d u\right\}
\end{aligned}
$$

Consider the first integral with let,

$$
\begin{gathered}
\omega=-u=-d \omega=d u \\
\int_{-\alpha}^{0} \frac{e^{-i u k}}{\left(u^{2}+\frac{1}{4}\right)} \Phi_{T}\left(u \cdot i \frac{1}{2}\right) d u \\
=\int_{\infty}^{0} \frac{-e^{i \omega k}}{\left(\omega^{2}+k_{1}\right)} \Phi\left(-\omega \cdot i \frac{1}{2}\right) d \omega
\end{gathered}
$$

Consider.

$$
\begin{aligned}
& \underline{\Phi}_{T}\left(-\omega-i \frac{1}{a}\right)=E\left[\left.e^{-i\left(\omega+i \frac{1}{a}\right) x_{T}} \right\rvert\, x_{t}=0\right] \\
& =E\left[\left.e^{i\left(\omega-i \frac{1}{a}\right) x_{T}} \right\rvert\, x_{t}=0\right]^{*} \\
& =\Phi_{T}^{*}\left(\omega-i \frac{1}{a}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
G(k, \tau)= & \frac{\sqrt{S_{t} k}}{2 \pi}\left\{\int_{-\infty}^{0} \frac{e^{-i u k}}{\left(u^{2}+t_{4}\right)} \Phi_{T}\left(u \cdot i_{2}^{1}\right) d u\right. \\
& \left.+\int_{0}^{\Delta} \frac{e^{-i u k}}{\left(u^{2}+t_{1}\right)} \Phi_{T}\left(u \cdot i_{2}^{1}\right) d u\right\} \\
= & \frac{\sqrt{S_{t} k}}{2 \pi}\left\{\int_{\infty}^{0} \frac{-e^{i u k}}{\left(u^{2}+\frac{1}{4}\right)} \Phi_{T}^{*}\left(u \cdot i_{2}^{1}\right)\right. \\
& \left.+\int_{0}^{\Delta} \frac{e^{-i u k}}{\left(u^{2}+t_{1}\right)} \Phi_{T}\left(u \cdot i_{2}^{1}\right) d u\right\}
\end{aligned}
$$

$$
\begin{array}{r}
=\frac{\sqrt{s_{t} k}}{\partial \pi}\left\{\int_{0}^{\infty} \frac{e^{i u k}}{\left(u^{2}+\frac{1}{4}\right)} \Phi_{T}^{*}\left(u \cdot i \frac{1}{2}\right)\right. \\
\left.+\int_{0}^{\Delta} \frac{e^{-i u k}}{\left(u^{2}+\frac{1}{4}_{1}\right)} \Phi_{T}\left(u \cdot i^{\frac{1}{2}}\right) d u\right\} \\
=\frac{\sqrt{s_{t} k}}{\partial T 1} \int_{0}^{\infty} \frac{1}{\left(u^{2}+\frac{1}{4}\right)}\left[e^{i u k} \Phi_{T}^{*}\left(u-i \frac{1}{2}\right)\right. \\
\left.+e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)\right] d u
\end{array}
$$

Consider

$$
e^{i u k} \Phi_{T}^{*}\left(u-i \frac{1}{2}\right)+e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)
$$

Let

$$
\Phi_{T}(u-i b)=g(u-i b)+i h(u-i b)
$$

50

$$
\begin{aligned}
e^{i u k} & \Phi_{T}^{*}\left(u-i \frac{1}{2}\right)+e^{-i u k} \Phi\left(u-i \frac{1}{2}\right) \\
=e^{i u k} & {\left[g\left(u-i \frac{1}{2}\right)-i h\left(u-i \frac{1}{2}\right)\right] } \\
& +e^{-i u k}\left[g\left(u-i \frac{1}{2}\right)+i h\left(u-i \frac{1}{2}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & g\left(u-i \frac{1}{\partial}\right)\left(e^{-i u k}+e^{i u k}\right) \\
& -i h\left(u-i \frac{1}{\partial}\right)\left(e^{i u k}-e^{-i u k}\right) \\
= & g\left(u-i \frac{1}{\partial}\right) 2 \cos (u k)-i h\left(u-i \frac{1}{\partial}\right) 2 i \sin (u k) \\
= & 2 g\left(u-i \frac{1}{\partial}\right) \cos (u k)+2 h\left(u-i \frac{1}{\partial}\right) \sin (u k)
\end{aligned}
$$

Next consider

$$
\begin{aligned}
\operatorname{Re} & {\left[e^{-i u k} \Phi_{T}(u-i b)\right] } \\
= & \operatorname{Re}\{[\cos (u k) \cdot i \sin (u k)][g(u-i b) \\
& +i h(u-i b)]\} \\
= & g(u-i b) \cos (u k)+h(u-i b) \sin (u k)
\end{aligned}
$$

Thus
$2 \operatorname{Re}\left[e^{-i u k} \Phi_{T}(u-i b)\right]$

$$
=e^{i u k} \Phi_{T}^{*}\left(u-i \frac{1}{a}\right)+e^{-i u k} \Phi\left(u-i \frac{1}{a}\right)
$$

It follows that

$$
\begin{array}{r}
G(k, \tau)=\frac{\sqrt{S_{t} k}}{2+1} \int_{0}^{\infty} \frac{1}{\left(u^{2}+\frac{1}{4}\right)}\left[e^{i u k} \Phi_{T}^{*}\left(u-i \frac{1}{2}\right)\right. \\
\left.+e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)\right] d u \\
=\frac{\sqrt{S_{t} k}}{\pi} \int_{0}^{\infty} \frac{1}{\left(u^{2}+t_{l}\right)} \operatorname{Re}\left[e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)\right] d u
\end{array}
$$

Thus
$G(k, \tau)=\frac{\sqrt{s_{t} k}}{\pi} \int_{0}^{\infty} \frac{1}{\left(u^{2}+\frac{1}{4}\right)} \operatorname{Re}\left[e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)\right] d u$
Now, recall that

$$
G(k, \tau)=S_{t} E\left[\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right]
$$

and consider

$$
\begin{aligned}
S_{t}-G(k, \tau) & =S_{t}\left\{1-E\left[\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right]\right\} \\
& =S_{t} E\left[1-\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right]
\end{aligned}
$$

If $S_{T}<K$

$$
\begin{aligned}
& \min \left(e^{x_{T}}, e^{k}\right)=e^{x_{T}}=\frac{S_{T}}{S_{t}} \\
& \text { so } \\
& s_{t} E\left[1-\min \left(e^{x_{T}}, e^{k}\right) \mid x_{t}=0\right]=S_{t} E\left[\left.1-\frac{S_{T}}{S_{t}} \right\rvert\, x_{t}=0\right] \\
& =E\left[S_{t}-S_{T} \mid x_{t}=0\right] \\
& =S_{t}-E\left[S_{T} \mid x_{t}=0\right]
\end{aligned}
$$

and if $S_{T}>K$

$$
\min \left(e^{x_{T}}, e^{k}\right)=e^{k}=\frac{k}{s_{t}}
$$

so
$S_{t} E\left[1-\min \left(e^{x_{T}}, e k\right) \mid x_{t}=0\right]=S_{t}-k$
since zero risk-free resturn is assumed this corresponds to the price of a call stion sold at time $t$ with strike price $K$ and expiny $T$.

This motroates the following expression for a call ostion price

$$
\begin{aligned}
& c\left(S_{t}, K_{1} T\right)=S_{t}-G(k, \tau) \\
& =S_{t}-\frac{\sqrt{S_{t} k}}{\pi} \int_{0}^{\infty} \frac{\operatorname{Re}\left[e^{-i u k} \Phi\left(u-i \frac{1}{2}\right)\right]}{\left(u^{2}+\frac{1}{t}\right)} d u
\end{aligned}
$$

## Digression: Inverse Fourrer Transforms, Gil-Palaer Inversion

This section will discuss the Gill-Pakez Fourier inversion formula. The Gil-Pabez form ula was first encountered in the discussion of the Fourier transform of a European call option in the Heston model. There it was shown that For a European option, $C(x, v, \tau)$,

$$
C(x, v, \tau)=k\left[e^{x} P_{1}(x, v, \tau)-P_{0}(x, v, \tau)\right]
$$

where $x$ is the log asset price, 0 the volatility and $\tau=T-t$. That the characteristic function is is given by

$$
\Phi_{T}^{j}(u)=\exp \left\{C_{j}(u, \tau) \bar{v}+D_{j}(u, \tau) \cup\right\}
$$

where $\bar{U}$ is the average volatility and $C_{j}(u, \tau)$ and $D_{j}(u, \tau)$ are known
functions. The Gil-Palaez formula was used to relate the $P$ terms in the call opton to the inverse Fourier transform of the $\Phi_{1}^{j}(u)$,

$$
P_{j}(x, v, \tau)=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi_{\tau}^{j}(u) e^{i u x}}{i u}\right\} d u
$$

Here the Gil-Pelaez formula will be derived.

The characterstic function is defined by

$$
\begin{aligned}
\Phi(u) & =E\left[e^{i u x}\right] \\
& =\int_{-\infty}^{\infty} e^{i u x} d P(x)
\end{aligned}
$$

where $P(x)$ is a cumulative distribution function.

Consider

$$
e^{l u x} \Phi(-u)-e^{-i u x} \Phi(u)
$$

$$
\begin{aligned}
& =e^{i u x} \int_{-\infty}^{\infty} e^{-i u y} d P(y)-e^{-i u x} \int_{-\infty}^{\infty} e^{i u y} d P(y) \\
& =\int_{-\infty}^{\infty}\left[e^{i u(x-y)}-e^{i u(y-x)}\right] d P(y) \\
& \Rightarrow \frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u} \\
& =\int_{-\infty}^{\infty} \frac{\left[e^{i u(x-y)}-e^{-i u(x-y)}\right] d P(y)}{2 \pi i u}
\end{aligned}
$$

but

$$
\begin{aligned}
& \frac{\left[e^{i u(x-y)}-e^{-i u(x-y)}\right]}{2 \pi i u}=2 i \frac{\sin [u(x-y)]}{2 \pi u} \\
& =\frac{\sin [u(x-y)]}{\pi u}
\end{aligned}
$$

It follows that

$$
\frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u}=\int_{-\infty}^{\infty} \frac{\sin [u(x-y)]}{\pi u} d P(y)
$$

Integrating over $u>0$ gives

$$
\begin{aligned}
& \int_{0}^{\infty} \frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u} d u \\
& \quad=\int_{0}^{\infty} \int_{-\infty}^{\infty} \frac{\sin [u(x-y)]}{\pi u} d P(y) d u
\end{aligned}
$$

The integration order can be cranged since Fubini's and the dominated convergence theorem can be show to hold so

$$
\begin{aligned}
\int_{0}^{\infty} & \frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u} d u \\
& \left.=\int_{-\infty}^{\infty} \int_{0}^{\alpha} \frac{\sin [u(x-y)]}{\pi u} d u d P_{y}\right)
\end{aligned}
$$

Consider the lefthand side recalling that

$$
\Phi(-u)=\Phi^{*}(u)
$$

$$
\frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u}=\frac{e^{i u x} \Phi^{*}(u)-e^{-i u x} \Phi(u)}{2 \pi u}
$$

let $\Phi(u)=g(u)+i h(u)$ then for the numerator

$$
\begin{aligned}
& e^{i u x} \Phi^{*}(u)-e^{-i u x} \Phi(u) \\
& =e^{i u x}[g(u)-i h(u)]-e^{-i u x}[g(u)+i h(u)] \\
& =g(u)\left(e^{i u x}-e^{-i u x}\right)-i h(u)\left(e^{i u x}+e^{-i u x}\right) \\
& =g(u) 2 i \sin (u x)-2 i h(u) \cos (u x)
\end{aligned}
$$

tnues

$$
\begin{aligned}
& \frac{e^{u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u} \\
& =\frac{2 i[g(u) \sin (u x)-h(u) \cos (u x)]}{2 \pi i u}
\end{aligned}
$$

$$
=\frac{g(u) \sin (u x)-h(u) \cos (u x)}{\pi u}
$$

next consider

$$
\begin{gathered}
\frac{\Phi(u) e^{i u x}}{i u \pi}=\frac{[g(u)+i h(u)][\cos (u x)-i \sin (u x)]}{i u \pi} \\
=\frac{g(u) \cos (u x)+h(u) \sin (u x)}{i u \pi} \\
+\frac{i[h(u) \cos (u x)-g(u) \sin (u x)]}{l u \pi} \\
=\frac{h(u) \cos (u x)-g(u) \sin (u x)}{u \pi} \\
-i[g(u) \cos (u x)+h(u) \sin (u x)] \\
u \pi
\end{gathered}
$$

It follows that,
$-\operatorname{Re}\left\{\frac{\Phi(u) e^{-i u x}}{i u \pi}\right\}=\frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u}$
next the ighthard side inner integral has the well known solution,

$$
\int_{0}^{\alpha} \frac{\sin [u(x-y)]}{\pi u} d u=\frac{1}{2} \operatorname{sgn}(x-y)
$$

where sgn is the signum function

$$
\operatorname{sgn}=\left\{\begin{array}{cc}
1 & x>y \\
0 & x=y \\
-1 & x<y
\end{array}\right.
$$

It follows that

$$
\begin{array}{r}
\int_{-\infty}^{\infty} \int_{0}^{\infty} \frac{\sin [u(x-y)]}{\pi u} d u d P_{(y)} \\
\quad=\int_{-\infty}^{\infty} \frac{1}{2} \operatorname{sgn}(x-y) d P(y)
\end{array}
$$

$$
\begin{aligned}
& =\frac{1}{2}\left\{\int_{-\alpha}^{x} d P(y)-\int_{x}^{-\Delta} d P(y)\right\} \\
& =\frac{1}{2}\left\{\int_{-\alpha}^{x} d P(y)-1+\int_{-\alpha}^{x} d P(y)\right\} \\
& =\frac{1}{2}\left\{2 \int_{-\infty}^{x} d P(y)-1\right\} \\
& =P(x)-\frac{1}{2}
\end{aligned}
$$

Pletting things together sives

$$
\begin{gathered}
\int_{0}^{\infty} \frac{e^{i u x} \Phi(-u)-e^{-i u x} \Phi(u)}{2 \pi i u} d u \\
=\int_{-\alpha}^{\infty} \int_{0}^{\alpha} \frac{\sin [u(x-y)]}{\pi u} d u P(y) \\
=-\int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi(u) e^{-i u x}}{i u \pi}\right\} d u \\
=P(x)-\frac{1}{2}
\end{gathered}
$$

$\Rightarrow P(x)=\frac{1}{2} \cdot \frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi(u) e^{-i u x}}{i u}\right\} d u$
which is the desired result. Where

$$
P(x)=P(\bar{y} \leq \bar{x})
$$

Likewise

$$
\begin{aligned}
& P(\bar{y} \geq \bar{X})=1-P(\bar{Y} \leq \bar{X}) \\
& =1 \cdot \frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi(u) e^{-i u x}}{i u}\right\} d u \\
& =\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi(u) e^{-i u x}}{i u}\right\} d u
\end{aligned}
$$

Next consider a Europan Call option with strike price $K$ and expiry $T$. An expression for $C_{T}(k)$ in terms
of the charateristic function will be found.

Assume $Q$ is the risk neutral measure and all expectations are with respect 0 and $r$ is the risk-free rate of return then

$$
\begin{aligned}
& C_{T}(k)=e^{-r T} E\left[\left(S_{T}-k\right)^{+}\right] \\
= & e^{-r T} E\left[S_{T}-k \mid S_{T}>k\right] \\
= & e^{-r T} E\left[S_{T} \mid S_{T} \geqslant k\right]-e^{-r T} k E\left[\mathbb{1}_{S_{T}}>k\right] \\
= & e^{-r T} E\left[S_{T} \mid S_{T} \geqslant k\right]-e^{r T} k Q\left(S_{T}>k\right)
\end{aligned}
$$

Let

$$
S=\ln S_{T} \quad k=\ln K
$$

Then the moment generating function is defined by,

$$
\begin{aligned}
\Phi_{T}(u) & =E\left[e^{i u s}\right] \\
& =\int_{-\alpha}^{\alpha} e^{i u s} d Q(s)
\end{aligned}
$$

Using the Gil-Pabez inversion formula

$$
\begin{aligned}
& Q\left(s_{T}>k\right)=Q(s>k) \\
&=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi_{T}(u) e^{-i u k}}{l u}\right\} d u
\end{aligned}
$$

Define a now measure using the Radon-Nikodym derivative

$$
d P=\frac{S_{T}}{E\left[S_{T}\right]} d Q
$$

Then

$$
\begin{aligned}
E\left[S_{T} \mid S_{T}>K\right] & =\int_{\left\{S_{T}>K\right\}} S_{T} d Q \\
& =E\left[S_{T}\right] \int_{\left\{S_{T}>K \xi\right.} \frac{S_{T}}{E\left[S_{T}\right]} d Q \\
& =E\left[S_{T}\right] P\left(S_{T}>K\right)
\end{aligned}
$$

Now the moment generating function with respect to $P$ is given by

$$
\begin{aligned}
\Phi_{T}^{P}(u) & =\int_{\Omega} e^{i u s} d P(s) \\
& =\int_{\Omega} e^{i u s} \frac{S_{T}}{E\left[S_{T}\right]} d Q(s) \\
& =\frac{1}{E\left[S_{T}\right]} \int_{\Omega} e^{i u s} e^{s} d Q(s) \\
& =\frac{1}{E\left[S_{T}\right]} \int_{\Omega} e^{i u s+s} d Q(s) \\
& =\frac{1}{E\left[S_{T}\right]} \int_{-2} e^{i(u-i) s} d Q(s) \\
& =\frac{\Phi_{T}(u-i)}{E\left[S_{T}\right]}
\end{aligned}
$$

But

$$
\begin{aligned}
E\left[S_{T}\right] & =\int_{\Omega} S_{T} d Q(s)=\int_{\Omega} e^{s} d Q(s) \\
& =\int_{\Omega} e^{i(-i) s} d Q(s)
\end{aligned}
$$

$$
=\Phi_{T}(-i)
$$

It follows that

$$
\Phi_{T}^{P}(u)=\frac{\Phi_{i}(u-i)}{\Phi_{T}(-i)}
$$

using the Gil-Palaez formula,
$P\left(s_{T}>k\right)=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi_{T}(u-i)}{\Phi_{T}(-i)} \frac{e^{-i u k}}{i u}\right\} d u$
and it follows trat
$E\left[S_{T} \mid S_{T}>K\right]=E\left[S_{T}\right] P\left(S_{T}>K\right)$
$=E\left[S_{T}\right]\left\{\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left[\frac{\Phi_{T}(u-i)}{\Phi_{T}(i)} \frac{e^{-i u k}}{i u}\right] d u\right\}$
Putting things together it follows that the price of the call option in terms of the moment generating function is siven $b_{1}$

$$
\begin{aligned}
C_{T}(K) & =e^{-r T} E\left[S_{T} \mid S_{T} \geqslant K\right]-e^{r T} K Q\left(S_{T}>K\right) \\
& =e^{-r T} E\left[S_{T}\right] P\left(S_{T}>K\right) \cdot e^{r T} K Q\left(S_{T}>K\right)
\end{aligned}
$$

where

$$
\begin{aligned}
& P\left(S_{T}>k\right)=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi_{T}(u-i)}{\Phi_{T}(-i)} \frac{e^{-i u k}}{i u}\right\} d u \\
& Q\left(S_{T}>k\right)=\frac{1}{2}+\frac{1}{\pi} \int_{0}^{\infty} \operatorname{Re}\left\{\frac{\Phi_{T}(u) e^{-i u k}}{i u}\right\} d u
\end{aligned}
$$

## Computung Implied Vobatility

Previously it was shown that the moment generatong function for the Black-Sholes model is given by

$$
\Phi_{T}(u)=\exp \left[-\frac{1}{2} u \sigma^{2} T(u+i)\right]
$$

The option price and moment generating function are related by,

$$
\begin{aligned}
& c\left(S_{t}, K, T\right) \\
& =S_{t}-\frac{\sqrt{S_{t} k}}{\pi} \int_{0}^{\infty} \frac{\operatorname{Re}\left[e^{-i u k} \Phi_{T}\left(u-i \frac{1}{2}\right)\right]}{\left(u^{2}+\frac{1}{t_{1}}\right)} d u
\end{aligned}
$$

Presidusly it was shown that the Block-sholes moment generating function is given by.

$$
\Phi_{T}^{B S}(u)=\exp \left[\frac{1}{2} u \sigma_{B S}^{2} T(u+i)\right]
$$

It follows that

$$
\begin{aligned}
\Phi_{T}^{B S}\left(u-\frac{1}{\partial} i\right) & =\exp \left[-\frac{1}{2}\left(u-i \frac{1}{2}\right) \sigma_{B S}^{2} T\left(u-i \frac{1}{2}+i\right)\right] \\
& =\exp \left[-\frac{1}{2} \sigma_{B S}^{2} T\left(u-i \frac{1}{2}\right)\left(u+\frac{1}{2} i\right)\right] \\
& =\exp \left[-\frac{1}{2} \sigma_{B S}^{2} T\left(u^{2}+\frac{1}{4}\right)\right]
\end{aligned}
$$

It follows that the Black-Shokes option price is given by

$$
\begin{aligned}
& C_{B S}\left(S_{t}, K, T\right)=S_{t}-\frac{\sqrt{S_{t} K}}{\pi} \int_{0}^{\infty} \frac{1}{u^{2}+t_{1}} \\
& \operatorname{Re}\left\{\exp (-i u k) \exp \left[-\frac{1}{2} \sigma_{B S}^{2} T\left(u^{2}+d_{1}\right)\right]\right\} d u
\end{aligned}
$$

It follows from the definition of implied volatility trat

$$
\begin{aligned}
\int_{0}^{\infty} \frac{1}{u^{2}+\frac{1}{1}} & \operatorname{Re}\left\{e ^ { - i u k } \left[\Phi_{T}\left(u-i \frac{1}{2}\right)-\right.\right. \\
& \left.\exp \left[-\frac{1}{2} \sigma_{B S}^{2} T\left(u^{2}+\frac{1}{d_{1}}\right)\right]\right\} d u=0
\end{aligned}
$$

I do not see where this expession comes from. It seems to be saying trat for the option
price defined by

$$
\begin{aligned}
& c\left(S_{t}, K, T\right) \\
& =S_{t}-\frac{\sqrt{S_{t} k}}{\pi} \int_{0}^{\infty} \frac{\operatorname{Re}\left[e^{-i u R^{\prime}} \Phi_{T}\left(u-i \frac{1}{2}\right)\right]}{\left(u^{2}+\frac{1}{t_{1}}\right)} d u
\end{aligned}
$$

That

$$
C\left(S_{t}, K, T\right)-C_{B S}\left(S_{t}, K, T\right)=0
$$

where $S_{t}$ is equivalent for both expressions. I do not see how this follows from implied velatility.

## Computing the At the Money Udatility skew

Assume that $S_{t}$ is at the money so that $k=0$.

It follows that $\Phi_{T}$ does not depend on $R$. For this case the $k$ dependence is assumed to be in $C_{B S}(K, T)$ and eiuk

The volatility skew with respect to $k$ is defined by

$$
\frac{\partial \omega_{B S}}{\partial k}
$$

where

$$
\omega_{B S}=\sigma_{B S} T
$$

is the total implied volatility The interest is in at the-money so $k=0$. It follows that the skew is evoluated at $k=0$.

Differentiry the relation from the previous expression for the implied volatility with respect to $R$ gives

$$
\begin{aligned}
& \frac{\partial}{\partial k} \int_{0}^{\infty} \frac{1}{u^{2}+\frac{1}{4}} \operatorname{Re}\left\{e ^ { - i u k } \left[\Phi_{T}\left(u-i_{2}\right)-\right.\right. \\
& \left.\exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+i_{1}\right)\right]\right\} d u=0 \\
& =\int_{0}^{\infty} \frac{1}{u^{2}+1 / 4} \operatorname{Re}\left\{( - i u ) e ^ { - i u k } \left[\Phi_{T}\left(u-i_{2}\right)-\right.\right. \\
& \left.\exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+i_{1}\right)\right]\right]+e^{-i u k}[ \\
& -\frac{1}{2}\left(u^{2}+\frac{1}{4}\right) \exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+i_{1}\right)\right] \\
& \left.\left.\frac{\partial \omega_{B S}}{\partial k}\right]\right\} d u \\
& =0
\end{aligned}
$$

setting $k=0$ gives

$$
\begin{aligned}
= & \int_{0}^{\infty} \frac{-1}{u^{2}+u_{1}} \operatorname{Re}\left\{i u \Phi_{T}(u-i t)+\right. \\
& i u \exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+\frac{1}{4}_{1}\right)\right]- \\
& \left.\left.\frac{1}{\partial}\left(u^{2}+\frac{1}{4}\right) \exp \left[-\frac{1}{\partial \omega_{B S}}\left(u^{2}+\frac{1}{4}\right)\right] \frac{\partial \omega_{B S}}{\partial R}\right|_{k=0}\right\} d u \\
= & 0
\end{aligned}
$$

Now $\exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+\frac{1}{4}\right)\right]$ is real so the integral becomes

$$
\begin{aligned}
& =\int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u \\
& \quad+\left.\frac{1}{2} \frac{\partial \omega_{B S}}{\partial k}\right|_{k=0} \exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+\frac{1}{4}\right)\right] d u \\
& =0
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u \\
& \quad=-\left.\frac{1}{2} \frac{\partial \omega_{B S}}{\partial k}\right|_{k=0} \int_{0}^{\infty} \exp \left[-\frac{1}{2} \omega_{B S}\left(u^{2}+\frac{1}{4}\right)\right] d u
\end{aligned}
$$

Consider the integral

$$
\begin{aligned}
& \int_{0}^{\infty} \exp \left[-\frac{1}{\partial} \omega_{B S}\left(u^{2}+\frac{1}{4}\right)\right] d u \\
= & e^{-\frac{1}{8} \omega_{B S}} \int_{0}^{\Delta} e^{-\frac{1}{\partial} \omega_{B S} u^{2}} d u \\
= & e^{-\frac{1}{8} \omega_{B S}} \frac{1}{2} \sqrt{\frac{\partial \pi}{\omega_{B S}}}=e^{-\frac{1}{t} \omega_{B S}} \sqrt{\frac{\pi}{\partial \omega_{B S}}}
\end{aligned}
$$

Putting things together gives

$$
\begin{aligned}
\int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} & \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u \\
= & -\left.\frac{1}{2} \frac{\partial \omega_{R S}}{\partial R}\right|_{k=0} \sqrt{\frac{I I}{2 \omega_{B S}}} e^{-\frac{1}{8} \omega_{B S}} \\
= & -\left.\frac{\partial \omega_{B S}}{\partial R}\right|_{k=0} \sqrt{\frac{I I}{8 \omega_{B S}}} e^{-\frac{1}{8} \omega_{B S}} \\
\left.\Rightarrow \frac{\partial \omega_{B S}}{\partial k}\right|_{k=0}= & -e^{\frac{1}{\gamma \omega_{B S}} \sqrt{\frac{8 \omega_{B S}}{\pi}}} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u
\end{aligned}
$$

Recall that,

$$
\begin{aligned}
& \omega_{B S}=\sigma_{B S}^{2} T \\
& \Rightarrow \frac{\partial \omega_{B S}}{\partial k}=\partial \sigma_{B S} T \frac{\partial \sigma_{B S}}{\partial k} \\
& s o\left.\frac{\partial \omega_{B S}}{\partial R}\right|_{k=0}=\left.2 \sigma_{B S} T \frac{\partial \sigma_{B S}}{\partial R}\right|_{k=0} \\
&= e^{1+\sigma_{B S}^{2} T} \sqrt{\frac{8 \sigma_{B S}^{2} T}{\pi}} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u \\
&\left.\Rightarrow \frac{\partial \sigma_{B S}}{\partial k}\right|_{k=0}=\frac{1}{\partial \sigma_{B S} T} \sqrt{\frac{8 \sigma_{B S}^{2} T}{\pi}} e^{\frac{1}{T} \sigma_{B S}^{2} T} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u
\end{aligned}
$$

$$
=-e^{\frac{1}{8} \sigma_{B S}^{2} T}\left[\frac{2}{\pi T} \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u\right.
$$

Thus

$$
\begin{aligned}
\left.\frac{\partial G_{B S}}{\partial k}\right|_{k=0}= & -e^{\frac{1}{8} \sigma_{B S}^{2} T} \sqrt{\frac{2}{\pi T}} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u
\end{aligned}
$$

## Example: Black-Sholes

The Black-Sholes charactoristic function was previausly shown to be,

$$
\Phi_{T}(u)=\exp \left\{-\frac{1}{2} \sigma^{2} T u(u+i)\right\}
$$

It follows that

$$
\begin{aligned}
\Phi_{T}\left(u-i \frac{1}{\partial}\right) & =\exp \left[-\frac{1}{\partial} \sigma^{2} T\left(u-i \frac{1}{\partial}\right)\left(u+i \frac{1}{\partial}\right)\right] \\
& =\exp \left[-\frac{1}{\partial} \sigma^{2} T\left(u^{2}+\frac{1}{4}\right)\right]
\end{aligned}
$$

Recall the volatility skew is given by

$$
\begin{aligned}
\left.\frac{\partial \sigma_{B S}}{\partial k}\right|_{k=0} & =-e^{\frac{1}{8} \sigma_{B S}^{2} T} \sqrt{\frac{2}{\pi T}} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u
\end{aligned}
$$

since $\Phi_{T}\left(u-i \frac{1}{2}\right)$ is real it follows it follows that

$$
\operatorname{Im}\left\{\exp \left[-\frac{1}{2} \sigma^{2} T\left(u^{2}+\frac{1}{4}\right)\right]\right\}=0
$$

Thus

$$
\left.\frac{\partial G_{B S}}{\partial k}\right|_{k=0}=0
$$

Example: Merton's Jump Diffusion Model
The Merton jump diffusion characteriste function was prevously shown to be

$$
\Phi_{T}(u)=\exp \left[-\frac{1}{2} u(i+u) \sigma^{2} T\right] \exp [\psi(u) T]
$$

where

$$
\psi(u)=-i \lambda u e^{\alpha-\frac{1}{2} \delta^{2}}+\lambda\left(e^{i u \alpha-\frac{1}{2} u^{2} \delta^{2}}-1\right)
$$

and

$$
\begin{gathered}
d S_{t}=\mu S_{t} d t+\sigma S_{t} d z_{t}+\left(e^{\alpha+\delta \varepsilon}-1\right) S_{t} d q \\
\varepsilon \sim N(0,1)
\end{gathered}
$$

the log-jump mean is $\alpha$ and standard deviation $\delta$.

Now

$$
\begin{aligned}
\Phi_{T}\left(u-\frac{1}{2} i\right)= & \exp \left[\frac{1}{2}\left(u-\frac{1}{2} i\right)\left(u+\frac{1}{2} i\right) \sigma^{2} T\right] \\
& \exp \left[\psi\left(u-\frac{1}{2} i\right) T\right] \\
= & \exp \left[\frac{1}{2}\left(u^{2}+\frac{1}{4}\right) \sigma^{2} T\right] \\
& \exp \left[\psi\left(u-\frac{1}{2} i\right) T\right]
\end{aligned}
$$

since the first term is real

$$
\begin{aligned}
\operatorname{Im}\left[\Phi_{T}\left(u-\frac{1}{2} i\right)\right]= & \exp \left[-\frac{1}{2}\left(u^{2}+\frac{1}{4}\right) \sigma^{2} T\right] \\
& \operatorname{Im}\left\{\exp \left[\psi\left(u-\frac{1}{2} i\right) T\right]\right\}
\end{aligned}
$$

## How Jumps Impact the Udatility Skew

Recall Merton jump diffussion SDE is given by.

$$
\begin{gathered}
d S_{t}=\mu S_{t} d t+\sigma S_{t} d z_{t}+\left(e^{\alpha+\delta \varepsilon}-1\right) S_{t} d q \\
\varepsilon \sim N(0,1)
\end{gathered}
$$

the log-jump mean is $\alpha$ and standard deviation $\delta$, and

$$
d q= \begin{cases}0 & \text { with probability }(1-\lambda) d t \\ 1 & \text { with probability } \lambda d t\end{cases}
$$

where $\lambda d t$ has a Poisson distribution with constant mean $\lambda$.

Consider an option approaching expiny so that $\tau=T-t \rightarrow 0$. Let $C_{J}(S, K, \tau)$ denote the price of the option when jumps are considered. As $\tau \rightarrow 0$ the time window for a jump is small so assume there is only
one jump. Since the probability of a jump is independent of the Black-sholes diffusion process the value of the option is the expectation of the price with and without a jump. The probabity of a jump occuring within $\tau$ is given by $\lambda \tau$ and the probability of no jump is $1-\lambda \tau$.

Recall that the characteristic function for the Merton model is given by

$$
\begin{gathered}
\Phi_{T}(u)=\exp \left\{\frac{1}{2} u(i+u) \sigma^{2} T-i u T \lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)\right. \\
\left.+T \lambda\left(e^{i u \alpha \cdot u^{2} \delta^{2} / 2}-1\right)\right\}
\end{gathered}
$$

and the option price and characteristic function satisfy

$$
\begin{aligned}
& C_{J}\left(s_{t}, k, T\right)= \\
& \quad s_{t}-\frac{s_{t} k}{\pi} \int_{0}^{\Delta} \frac{\operatorname{Re}\left[e^{-i u k} \Phi\left(u-i t_{2}\right)\right] d u}{\left(u^{2}+t_{1}\right)}
\end{aligned}
$$

consider the exponential term

$$
\begin{aligned}
-\frac{1}{2} u(i+u) & \sigma^{2} T-i u T \lambda\left(e^{\alpha+\delta^{2} / 2}-1\right) \\
+ & T \lambda\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right) \\
=i u[ & \left.-\frac{1}{2} \sigma^{2}-\lambda\left(e^{\alpha+\frac{1}{2} \delta^{2}}-1\right)\right] T \\
+ & T \lambda\left(e^{i u \alpha \cdot u^{2} \delta^{2} / 2}-1\right)
\end{aligned}
$$

let $\mu_{j}=\lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)$ then the exponential torm becomes

$$
i u\left(-\frac{1}{2} \sigma^{2}+u_{j}\right) T+T \lambda\left(e^{i u \alpha \cdot u^{2} \delta^{2} / 2}-1\right)
$$

The term linear in in is the riskneutral drift of the option price when compared to Black-Stoles charateristic function. It follows that $\mu_{1}$ is a drift like the risk-free return.

Now $C_{j}(S, K, \tau)$ is the expection of the price with and without a jump. In the absence of a
jump the price is the Black-Sholes price so if $j s$ is the price with a jump it follows that

$$
\begin{gathered}
C_{j}(s, k, \tau) \approx(1-\lambda \tau) C_{B s}\left(s_{t} e^{\mu_{j} \tau}, k, \tau\right) \\
+\lambda \tau C_{j}(j s, k, T) \\
=C_{B s}\left(s_{t} e^{\mu_{j} \tau}, k, \tau\right)+\lambda \tau\left[C_{j}(j s, k, \tau)\right. \\
\left.-C_{B s}\left(s_{t} e^{\mu_{j} \tau}, k, \tau\right)\right] \\
=C_{B<}\left(s_{t} e^{\mu_{j} \tau}, k, \tau\right)+o(\tau)
\end{gathered}
$$

Further if it is assumed that the jump is down and large enough that the option is out-of-the-money $c_{j}(J S, K, \tau)$ can be ignored it follows that for $\tau \rightarrow 0$ to leading order

$$
C_{\jmath}(S, K, \tau) \approx C_{B S}\left(S_{t} e^{\mu_{\jmath} \tau}, K, \tau\right)
$$

The interest is in computing the at the money implied oodatility skew

$$
\left.\frac{\partial \sigma_{B S}}{\partial k}\right|_{k=0}
$$

to get there differentiale the prevous approximation with respect to $k$ and recall that $\sigma_{B S}(k, \tau)$ also depends on $k$.

$$
\begin{aligned}
& \frac{\partial C_{S}}{\partial k}=\frac{\partial C_{B S}}{\partial k}+\frac{\partial C_{B S}}{\partial C_{B S}} \frac{\partial C_{B S}}{\partial k} \\
& \Rightarrow \frac{\partial C_{B S}}{\partial k}=\frac{\frac{\partial C_{J}}{\partial k}-\frac{\partial C_{B S}}{\partial k}}{\frac{\partial C_{B S}}{\partial C_{B S}}}
\end{aligned}
$$

It follows that

$$
\left.\frac{\partial G_{B S}}{\partial k}\right|_{k=0}=\left.\frac{\frac{\partial C_{J}}{\partial k}-\frac{\partial C_{B S}}{\partial G_{B S}}}{\frac{\partial C_{B S}}{\partial G_{B S}}}\right|_{k=0}
$$

Next this expression will be evaluated using the Black-Sholes call option.

Recall that the Black-Shotes price for a call option is given by

$$
\begin{aligned}
C(\tau)= & S_{t} N\left(d_{t}\left(\tau, S_{t}\right)\right)-k e^{-r \tau} N\left(d-\left(\tau, S_{t}\right)\right. \\
& d_{t}\left(\tau, S_{t}\right)= \\
& d\left(\tau, S_{t}\right)=\frac{-k+\left(r+d \sigma^{2}\right) \tau}{\sigma \sqrt{\tau}} \\
& \\
\sigma \sqrt{\tau} &
\end{aligned}
$$

Now if $r=0$

$$
\begin{aligned}
c(\tau) & =S_{t}\left[N\left(d_{+}\right)-\frac{k}{S_{t}} N\left(d_{-}\right)\right] \\
& =S_{t}\left[N\left(d_{+}\right)-e^{k} N\left(d_{-}\right)\right] \\
d_{+} & =\frac{-k+\frac{1}{2} \sigma^{2} \tau}{\sigma \sqrt{\tau}}=\frac{-k}{\sigma \sqrt{\tau}}+\frac{\sigma \sqrt{\tau}}{2} \\
d_{-} & =\frac{-k-\frac{1}{2} \sigma^{2} \tau}{\sigma \sqrt{\tau}}=-\frac{k}{\sigma \sqrt{\tau}}-\frac{\sigma \sqrt{\tau}}{2}
\end{aligned}
$$

clearly, $d_{1}<d$ -
If the option is at the money $k=0$, then

$$
C(\tau)=S_{t}\left[N\left(d_{+}\right)-N\left(d_{-}\right)\right]
$$

and

$$
d_{+}=\frac{\sigma \sqrt{\tau}}{2} \quad d_{-}=\frac{\sigma \sqrt{\tau}}{2}
$$

Now

$$
\begin{aligned}
& N\left(d_{+}\right)=\frac{1}{2 \pi} \int_{-\alpha}^{\frac{\sigma \sqrt{\tau}}{2}} e^{-x^{2} / 2} d x \\
&=\frac{1}{2 \pi} \int_{-\alpha}^{0} e^{-x^{2} / 2} d x+\frac{1}{2 \pi} \int_{0}^{\frac{\sigma \sqrt{\tau}}{2}} e^{-x^{2} / 2} d x
\end{aligned}
$$

similarly $\quad-6 \frac{\sqrt{\pi}}{2}$

$$
\begin{aligned}
N\left(d_{-}\right) & =\frac{1}{\sqrt{2 \pi}} \int_{-\alpha} e^{-x^{2} / 2} d x \\
& =\frac{1}{2 \pi} \int_{-\alpha}^{0} e^{-x^{2} / 2} d x-\frac{1}{2 \pi} \int_{-\frac{6 \sqrt{x}}{2}}^{0} e^{-x_{12}^{2}} d x
\end{aligned}
$$

It follows that

$$
N\left(d_{+}\right)-N\left(d_{-}\right)=\frac{1}{\sqrt{2 \pi}} \int_{0}^{\frac{\sigma \sqrt{\tau}}{2}} e^{-x^{2} / 2} d x
$$

$$
\begin{array}{r}
+\frac{1}{2 \pi} \int_{-\frac{\sigma \sqrt{\tau}}{2}}^{0} e^{-x^{2} / 2} d x \\
=\frac{1}{2 \pi} \int_{-\frac{\sigma \sqrt{\tau}}{2}}^{\sigma \frac{\sqrt{\tau}}{2}} e^{-x^{2} / 2} d x
\end{array}
$$

Now for $\tau \rightarrow 0 \quad e^{-x^{2} / 2} \rightarrow 1 \leq 0$

$$
\begin{aligned}
N\left(d_{+}\right)-N\left(d_{-}\right) \approx \frac{1}{\sqrt{2 \pi}} \int_{\frac{-\sigma \sqrt{\tau}}{2}}^{\frac{\sigma \sqrt{\tau}}{2}} d x \\
=\frac{\sigma \sqrt{\tau}}{\sqrt{2 \pi}}
\end{aligned}
$$

Thus for an at-the-money-option as $\tau \rightarrow 0$

$$
\begin{aligned}
C(\tau) & =S_{t}\left[N\left(d_{+}\right) \cdot N\left(d_{-}\right)\right] \\
& \approx \frac{\sigma S_{t} \sqrt{\tau}}{12 \pi}
\end{aligned}
$$

It follows that for $k=0$ and $\tau \rightarrow 0$

$$
\begin{aligned}
& \left.\frac{\partial C_{B S}}{\partial \sigma_{B S}}\right|_{k=0} \approx \frac{\partial}{\partial \sigma_{B S}}\left[\frac{\sigma_{B S} S_{t} \sqrt{\tau}}{\sqrt{2 \pi}}\right] \\
& \left.\Rightarrow \frac{\partial C_{B S}}{\partial \sigma_{B S}}\right|_{k=0}=\frac{S_{t} \sqrt{\tau}}{\sqrt{2 \pi}}
\end{aligned}
$$

Next consider

$$
\frac{x_{1}}{\partial k}-\frac{x_{B S}}{\partial k}
$$

and recall that for $\tau \rightarrow 0$ it was previously shown that

$$
C_{j}(S, K, \tau) \approx C_{B S}\left(S_{t} e^{\mu_{j} \tau}, K, \tau\right)
$$

First consider the second term and recall that
$c(\tau)=S_{t} N\left(d_{+}\left(\tau_{1}, S_{t}\right)\right)-K e^{-r \tau} N\left(d_{-}\left(\tau, S_{t}\right)\right.$

$$
\begin{aligned}
d_{+}\left(\tau, s_{t}\right) & =\frac{-k+\left(r+b \sigma^{2}\right) \tau}{\sigma \sqrt{\tau}} \\
& =\frac{-k}{\sigma \sqrt{\tau}}+\frac{\left(r+\frac{1}{2} \sigma^{2}\right) \sqrt{\tau}}{\sigma} \\
d_{\left(\tau, s_{t}\right)} & =\frac{-k+\left(r-\frac{1}{2} \sigma^{2}\right) \tau}{\sigma \sqrt{\tau}} \\
& =\frac{-k}{\sigma \sqrt{\tau}}+\frac{\left(r-\frac{1}{2} \sigma^{2}\right) \sqrt{\tau}}{\sigma}
\end{aligned}
$$

It is assumed that $r=0$ so

$$
\begin{aligned}
& d_{+}\left(\tau, s_{t}\right)=-\frac{k}{\sigma \sqrt{\tau}}+\frac{1}{2} \sigma \sqrt{\tau} \\
& d_{-}\left(\tau, s_{t}\right)=-\frac{k}{\sigma \sqrt{\tau}}-\frac{1}{2} \sigma \sqrt{\tau}
\end{aligned}
$$

also consider $C(\tau)$

$$
\begin{aligned}
C(k, \tau) & =S_{t} N\left(d_{+}\left(\tau_{1}, S_{t}\right)\right)-k N\left(d_{-}\left(\tau, S_{t}\right)\right. \\
& =S_{t}\left[N\left(d_{+}\right)-\frac{1}{S_{t}} N(d)\right]
\end{aligned}
$$

$$
=S_{t}\left[N\left(d_{+}\right) \cdot e^{k} N\left(d_{-}\right)\right]
$$

It follows that

$$
\frac{1}{S_{t}} \frac{\partial C}{\partial k}=\frac{\partial N}{\partial d_{t}} \frac{\partial d_{t}}{\partial k}-e^{k} \frac{\partial N}{\partial d_{-}} \frac{\partial d}{\partial k} \cdot e^{k N\left(d_{-}\right)}
$$

Now

$$
\begin{aligned}
\frac{\partial N}{\partial d_{+}} \frac{\partial d_{+}}{\partial k} & =n\left(d_{+}\right)\left(-\frac{1}{\sigma \sqrt{\tau}}\right) \\
& =-\frac{n\left(d_{+}\right)}{\sigma \sqrt{\tau}}
\end{aligned}
$$

and

$$
e^{k} \frac{\partial N}{\partial d} \frac{\partial d}{\partial k}=-\frac{e^{k} n(d)}{\sigma \sqrt{\tau}}
$$

where

$$
\begin{aligned}
& n\left(d_{+}\right)=\frac{1}{\sqrt{2 \pi}} e^{-d_{+12}^{2}} \\
& n\left(d_{-}\right)=\frac{1}{\sqrt{2 \pi}} e^{-d_{-12}^{2}}
\end{aligned}
$$

putting things together

$$
\begin{gathered}
\frac{1}{s_{t}} \frac{\partial C}{\partial k}=\frac{1}{\sigma \sqrt{\tau}}\left[-n\left(d_{+}\right)+e^{k} n(d)\right] \\
-e^{k} N(d)
\end{gathered}
$$

setting $k=0$ gives

$$
\begin{aligned}
& d_{+}=\frac{1}{2} \sigma \sqrt{\tau} \quad d_{-}=-\frac{1}{2} \sigma \sqrt{\tau} \\
& n\left(d_{+}\right)=\frac{1}{\sqrt{2 \pi}} e^{-\sigma^{2} \tau / \delta} \\
& n\left(d_{-}\right)=\frac{1}{\sqrt{2 \pi}} e^{-\sigma^{2} \tau / \delta} \\
& =n\left(d_{+}\right)
\end{aligned}
$$

It follows that

$$
\frac{1}{s_{t}} \frac{\partial c}{\partial k}=\frac{1}{\sigma \sqrt{\tau}}\left[-\eta\left(d_{t}\right)+n(d)\right]-N(d)
$$

$$
\begin{aligned}
=-N\left(d_{-}\right) & =-N\left(-\frac{1}{\partial} \sigma \sqrt{\tau}\right) \\
\left.\Rightarrow \quad \frac{1}{s_{t}} \frac{\partial c}{\partial k}\right|_{k=0} & =-N\left(-\frac{1}{\partial} \sigma \sqrt{\tau}\right)
\end{aligned}
$$

For the first term

$$
\frac{\partial x_{j}}{\partial k}
$$

and using

$$
C_{j}(S, K, \tau) \approx C_{B S}\left(S_{t} e^{\mu_{j} \tau}, K, \tau\right)
$$

For this term a drift must be includer, namely

$$
\mu, \tau
$$

It follows that

$$
\begin{aligned}
& d_{+}^{\prime}\left(\tau, s_{t}\right)=-\frac{k}{\sigma \sqrt{\tau}}+\frac{\mu_{\sqrt{ }} \sqrt{\tau}}{\sigma}+\frac{\sigma \sqrt{\tau}}{2} \\
& d_{-}^{\prime}\left(\tau, s_{t}\right)=-\frac{k}{\sigma \sqrt{\tau}}+\frac{\mu_{j} \sqrt{\tau}}{\sigma}-\frac{\sigma \sqrt{\tau}}{2}
\end{aligned}
$$

and since

$$
C_{\jmath}(k, \tau)=S_{t}\left[N\left(d_{+}^{\prime}\right) \cdot e^{k} N\left(d_{-}^{\prime}\right)\right]
$$

it is seen that
$\frac{\partial C_{1}}{\partial k}=\frac{\partial N}{\partial d_{+}^{\prime}} \frac{\partial d_{+}^{\prime}}{\partial k}-e^{k} \frac{\partial N}{\partial d_{-}^{\prime}} \frac{\partial d_{-}^{\prime}}{\partial k}-e^{k} N\left(d_{-}^{\prime}\right)$
where

$$
\frac{\partial d_{t}^{\prime}}{\partial k}=\frac{\partial d^{\prime}}{\partial k}=-\frac{1}{\sigma \sqrt{\tau}}
$$

and

$$
\frac{\partial N}{\partial d_{+}^{\prime}}=n\left(d_{+}^{\prime}\right) \quad \frac{\partial N}{\partial d_{-}^{\prime}}=n\left(d_{-}^{\prime}\right)
$$

Now for $k=0$

$$
\begin{aligned}
& d_{+}^{\prime}\left(\tau, s_{t}\right)=\frac{\mu_{\sqrt{ }} \tau}{\sigma}+\frac{\sigma \sqrt{\tau}}{2} \\
& d_{-}^{\prime}\left(\tau, s_{t}\right)=\frac{\mu_{j} \sqrt{\tau}}{\sigma}-\frac{\sigma \sqrt{\tau}}{2}
\end{aligned}
$$

consider

$$
\begin{aligned}
& n\left(d_{+}^{\prime}\right)=\frac{1}{\sqrt{2 \pi}} e^{-d_{+}^{\prime 2} / 2} \\
& n\left(d_{-}^{\prime}\right)=\frac{1}{\sqrt{2 \pi}} e^{-d_{-}^{\prime 2} / 2}
\end{aligned}
$$

For the arguments

$$
\begin{aligned}
d_{t}^{\prime 2} & =\left(\frac{\mu_{y} \sqrt{\tau}}{\sigma}+\frac{\sigma \sqrt{\tau}}{2}\right)^{2} \\
& =\left(\frac{\mu_{y}}{\sigma}+\frac{\sigma}{2}\right)^{2} \tau \\
d^{\prime 2} & =\left(\frac{\mu_{f}}{\sigma}-\frac{\sigma}{2}\right)^{2} \tau
\end{aligned}
$$

It follows that

$$
\left.\frac{1}{S_{t}} \frac{\partial C_{t}}{\partial k}\right|_{k=0}=\frac{\partial N}{\partial d_{t}^{\prime}} \frac{\partial d_{t}^{\prime}}{\partial k}-\frac{\partial N}{\partial d_{-}^{\prime}} \frac{\partial d^{\prime}}{\partial k}-N\left(d^{\prime}\right)
$$

$$
\begin{aligned}
=-\frac{1}{\sigma \sqrt{\tau}} & \left\{n\left[\left(\frac{\mu_{1}}{\sigma}+\frac{\sigma}{2}\right)^{2} \tau\right]\right. \\
- & \left.n\left[\left(\frac{\mu_{1}}{\sigma}+\frac{\sigma}{2}\right)^{2} \tau\right]\right\} \\
- & N\left[\left(\frac{\mu_{1}}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}\right]
\end{aligned}
$$

Consider the limit $\tau \rightarrow 0$. For the first two terms for $\tau \rightarrow 0$

$$
\begin{aligned}
& n\left[\left(\frac{\mu_{y}}{0}+\frac{\sigma}{2}\right)^{2} \tau\right]-n\left[\left(\frac{\mu_{y}}{0}-\frac{\sigma}{2}\right)^{2} \tau\right] \\
& 1-1=0
\end{aligned}
$$

since the difference is second order.
Pletting things together for $\tau \rightarrow 0$
$\frac{\partial C_{J}}{\partial k}-\frac{\partial C_{B S}}{\partial k}=-S_{t} N\left[\left(\frac{\mu_{J}}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}\right]+S_{t} N\left(-\frac{1}{2} \sigma \sqrt{\tau}\right)$

Now

$$
\begin{array}{r}
-s_{t} N\left[\left(\frac{\mu}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}\right]+s_{t} N\left(-\frac{1}{2} \sigma \sqrt{\tau}\right) \\
=s_{t}\left\{\frac{-1}{\partial \pi} \int_{-\alpha}^{\left(\frac{\mu}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}} e^{-x^{2} / 2} d x\right. \\
\left.+\int_{-\infty}^{-\frac{1}{2} \sigma \sqrt{\tau}} e^{-x^{2} / 2} d x\right\}
\end{array}
$$

assume $\mu_{j}>0$ so that

$$
\left(\frac{\mu}{\sigma} \cdot \frac{\sigma}{2}\right) \sqrt{\tau}>-\frac{1}{2} 6 \sqrt{\tau}
$$

If the opposite is true the sign of the integral will change. Now

$$
\begin{aligned}
& =-\frac{1}{2 \pi} \int_{-1 / 2 \sigma \sqrt{\tau}}^{\left(\frac{u_{u}}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}} e^{-x^{2} / 2} d x \\
& \text { as } \tau \rightarrow 0 \\
& \approx-\frac{1}{2 \pi} \int_{-1 / 2 \sigma \sqrt{\tau}}^{\left(\frac{u_{u}}{\sigma}-\frac{\sigma}{2}\right) \sqrt{\tau}} d x
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{2 \pi}\left[\frac{\mu_{1}}{\sigma} \sqrt{\tau}-\frac{\sigma}{\sigma} \pi+\frac{\sigma}{2} \pi\right] \\
& =-\frac{1}{\sqrt{2 \pi}} \frac{\mu_{2}}{\sigma} \sqrt{\tau}
\end{aligned}
$$

Thus

$$
\frac{\partial C_{1}}{\partial k}-\left.\frac{\partial C_{B S}}{\partial k}\right|_{k=0} \approx-\frac{S_{4}}{\sqrt{2 \pi}} \frac{\mu_{j}}{\sigma} \sqrt{\tau}
$$

Putting things together the at the-money variance skew is given by

$$
\begin{aligned}
\left.\frac{\partial G_{B S}}{\partial k}\right|_{k=0}= & \left.\frac{\frac{\partial C_{1}}{\partial k}-\frac{\partial C_{B S}}{\partial G_{B S}}}{\frac{\partial C_{B S}}{\partial \sigma_{B S}}}\right|_{k=0} \\
= & \frac{-\frac{S_{t}}{\sqrt{2 \pi}} \frac{\mu_{J} \sqrt{\pi}}{\sigma_{B S}}}{\frac{\Sigma_{t} \sqrt{\tau}}{\sqrt{2 \pi}}}
\end{aligned}
$$

$$
\begin{gathered}
=\frac{\mu_{J}}{\sigma_{B S}} \\
\left.\Rightarrow \frac{\partial \sigma_{B S}}{\partial k}\right|_{k=0}=-\frac{\mu_{J}}{\sigma_{B S}} \\
\left.\Rightarrow \sigma_{B S} \frac{\partial \sigma_{B S}}{\partial k}\right|_{k=0}-\mu_{J} \\
\left.\Rightarrow \frac{\partial \sigma_{B S}^{2}}{\partial k}\right|_{k=0}=-2 \mu_{J}
\end{gathered}
$$

Recall

$$
\mu_{\jmath}=-\lambda\left(e^{\alpha+\delta^{2} / 2}-1\right)
$$

thus the implied variance skew is parameterized by
$\alpha$ - los jump size mean
$\delta$ - los jump size variance
$\lambda$ - mean jump frequeny

Nert consider the following volatility smile plot, which stows the implied volatility as a function of the expry log-strike with chorces

|  | $\sigma$ | $\lambda$ | $\alpha$ | $\delta$ |
| :--- | :---: | :---: | :---: | :---: |
| Solid | 0.2 | 0.5 | -0.15 | 0.05 |
| Dashed | 0.2 | 1.0 | -0.07 | 0.00 |
| Long-dashed | 0.2 | 1.0 | -0.07 | 0.05 |

FIGURE 5.2 The 3-month volatility smile for various choices of jump diffusion parameters.

![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-438.jpg?height=727&width=1132&top_left_y=890&top_left_x=195)
for the jump diffussion parameters. The region where the approximation applies is shown in red.

The at-the-money variance skew as a function of time to expiry is shown above

FIGURE 5.3 The term structure of ATM variance skew for various choices of jump diffusion parameters.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-439.jpg?height=607&width=1013&top_left_y=560&top_left_x=257)

TABLE 5.3 Interpreting Figures 5.2 and 5.3.
|  | $\sigma$ | $\lambda$ | $\alpha$ | $\delta$ | T* | $\psi_{0}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Solid | 0.2 | 0.5 | -0.15 | 0.05 | 0.69 | -0.133 |
| Dashed | 0.2 | 1.0 | -0.07 | 0.00 | 0.34 | -0.135 |
| Long-dashed | 0.2 | 1.0 | -0.07 | 0.05 | 0.33 | -0.133 |


From the plot above it is seen that ATM term structure (i.e this torm is used in the book in means the implied volatility as a function of the epiny date as shown in the figue) decays
rapidly with time to expiry cor time to maturity dates)

The area in which the approximation applies is indicated in red.

If there are infrequent bis jumps as assumed in the model, that occur below some charateristic time $\tau^{*}$, it should be possible to detect the jump in the return distribution.
$\tau^{*}$ is computed by assuming

$$
-\left(e^{\alpha+\delta^{2} / 2}-1\right) \approx \sigma \sqrt{\tau^{*}}
$$

## Stochastic Nobatility Plus Jumps

Consider a Heston process with a Merton type of jump process added, namely,

$$
\begin{aligned}
& d s_{t}=\mu s_{t} d t+\sqrt{v_{t}} s_{t} d z_{t}^{\prime}+\left(e^{\alpha+\delta \varepsilon}-1\right) s_{t} d q_{t} \\
& d v_{t}=-\lambda(v-\bar{v}) d t+\eta v_{t} d z_{t}^{2}
\end{aligned}
$$

where

$$
\begin{aligned}
& \left\langle d z_{t}^{1} d z_{t}^{2}\right\rangle=e d t \\
& \varepsilon \sim \operatorname{Normal}(0,1)
\end{aligned}
$$

and $d q$ is a Poisson process satisfying

$$
d q= \begin{cases}0 & \text { with probability } \\ 1 & \text { with probability } \\ & \lambda_{j} d t\end{cases}
$$

where $\lambda_{J}$ is the jump intensity (or hazzard rate) which is the mean of the Porsson process.
It can be shown that the characteristic function for the model is given by

$$
\Phi_{T}(u)=e^{C_{0}(u, T) \bar{v}+D_{0}(u, T) v} e^{\psi(\omega T}
$$

where for $j=0,1$

$$
\begin{gathered}
D_{j}(u, t)=\frac{r_{-}\left(1-e^{-d \tau}\right)}{\left(1-g e^{-d \tau}\right)} \\
C_{j}(u, t)=\lambda\left\{r_{-} t-\frac{2}{\eta^{2}} \ln \left(\frac{1-g e^{-d t}}{1-g}\right)\right\} \\
r_{ \pm}=\frac{\beta \pm \sqrt{\beta^{2}-4 \alpha \gamma}}{2 \gamma}=\frac{\beta \pm d}{\eta^{2}} \\
\alpha=\sqrt{\beta^{2} \cdot 4 \alpha \gamma} \\
S^{=\frac{r_{-}}{r_{+}}} \\
\alpha=-\frac{u^{2}}{2} \cdot \frac{c u}{2}+i j u \\
\beta=\lambda \cdot e^{\eta i} \cdot e^{n i u} \\
\gamma=\frac{\eta^{2}}{2}
\end{gathered}
$$

and $\psi(u)$ is the jump diffusion charateristic coefficient which is given b)

$$
\begin{aligned}
\psi(u)=-\lambda_{J} i u & \left(e^{\alpha+\delta^{2} / 2}-1\right) \\
& +\lambda_{J}\left(e^{i u \alpha-u^{2} \delta^{2} / 2}-1\right)
\end{aligned}
$$

This expression can be used to compute the option price

$$
\begin{aligned}
& c\left(S_{t}, K, T\right) \\
& =S_{t}-\frac{\sqrt{S_{t} k}}{\pi} \int_{0}^{\infty} \frac{\operatorname{Re}\left[e^{-i u k} \Phi_{T}\left(u-i \frac{1}{2}\right)\right]}{\left(u^{2}+\frac{1}{4}\right)} d u
\end{aligned}
$$

The implied volatility using

$$
\begin{aligned}
\int_{0}^{\infty} \frac{1}{u^{2}+\frac{1}{4}} & \operatorname{Re}\left\{e ^ { - i u k } \left[\Phi_{T}\left(u-i \frac{1}{2}\right)-\right.\right. \\
& \left.\exp \left[-\frac{1}{2} \sigma_{B S}^{2} T\left(u^{2}+\frac{1}{1}_{1}\right)\right]\right\} d u=0
\end{aligned}
$$

and the implied volatility stow using

$$
\begin{aligned}
\left.\frac{\partial G_{B S}}{\partial k}\right|_{k=0}= & -e^{\frac{1}{8} \sigma_{B S}^{2} T} \sqrt{\frac{2}{\pi T}} \\
& \int_{0}^{\infty} \frac{u}{u^{2}+\frac{1}{4}} \operatorname{Im}\left[\Phi_{T}\left(u-i \frac{1}{2}\right)\right] d u
\end{aligned}
$$

## Disital Options and Digital Cliquels

A disital call option denoted by $D(K, T)$ pays 1 if the stock price $S_{T}$ at expiration $T$ is greater tran the strike price $K$ and zero otherwise. It is valued as the limit of a call spread as the spreed between the strikes goes to zoro. In other words the derivative of the call option price with respect to $K$, thus

$$
D(K, T)=\frac{\partial C(K, T)}{\partial K}
$$

Note that $C(K, T)$ is assumed to decrease with $K$.

If the call option is priced using the Black-Sholes price then

$$
C(K, T)=C_{B s}\left(K, T, \sigma_{B s}(K, T)\right)
$$

where $G_{B S}(K, T)$ is the implied volatility. It follows that

$$
\begin{aligned}
D(K, T) & =-\frac{\partial C_{B S}}{\partial K}\left(K, T, \sigma_{B S}(K, T)\right) \\
& =-\frac{\partial C_{B S}}{\partial K}-\frac{\partial C_{B S}}{\partial \sigma_{B S}} \frac{\partial \sigma_{B S}}{\partial K}
\end{aligned}
$$

Thus $D(K, T)$ depends on the implied volatility skew. Recall that the Black-Scholes option price if the risk-free return is assumed to be zero then

$$
\begin{aligned}
& c(\tau)=s_{t}\left[N\left(d_{+}\right)-e^{k} N\left(d_{-}\right)\right] \\
& d_{+}(\tau, k)=\frac{-k+2 \sigma^{2} \tau}{\sigma \sqrt{\tau}}=-\frac{k}{\sigma \sqrt{\tau}}+\frac{\sigma \sqrt{\tau}}{2} \\
& d_{-}(\tau, k)=\frac{-k-2 \sigma^{2} \tau}{\sigma \sqrt{\tau}}=-\frac{k}{\sigma \sqrt{\tau}}-\frac{\sigma \sqrt{\tau}}{2} \\
& k=\ln \frac{k}{s_{t}}
\end{aligned}
$$

Now for the first term

$$
\begin{gathered}
\frac{\partial C_{B S}}{\partial K}=\frac{\partial}{\partial K}\left\{S_{t}\left[N\left(d_{+}\right) \cdot e^{k} N\left(d_{-}\right)\right]\right\} \\
=S_{t} \frac{\partial N\left(d_{+}\right)}{\partial K}-S_{t} N(d) \frac{\partial e^{k}}{\partial K} \\
-S_{t} e^{k} \frac{\partial N(d)}{\partial K}
\end{gathered}
$$

For each term

$$
\begin{aligned}
S_{t} \frac{\partial N\left(d_{+}\right)}{\partial K} & =S_{t} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial K} \\
S_{t} N\left(d_{-}\right) \frac{\partial e^{k}}{\partial K} & =S_{t} N\left(d_{-}\right) \frac{\partial}{\partial K}\left(\frac{K}{S_{t}}\right) \\
& =N\left(d_{-}\right) \\
S_{t} e^{k} \frac{\partial N\left(d_{d}\right)}{\partial K} & =K n\left(d_{-}\right) \frac{\partial d}{\partial K}
\end{aligned}
$$

Consider

$$
\frac{\partial k}{\partial k}=\frac{\partial}{\partial k} \ln \frac{k}{s t}=\frac{1}{k}
$$

50

$$
\begin{aligned}
& \frac{\partial d_{1}}{\partial K}=-\frac{1}{\sigma \sqrt{\tau} K} \\
& \frac{\partial d}{\partial K}=-\frac{1}{\sigma \sqrt{\tau} K}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
S_{t} \frac{\partial N\left(d_{+}\right)}{\partial K} & =S_{t} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial K} \\
& =-\frac{S_{t}}{\sigma \sqrt{\tau} K} n\left(d_{+}\right) \\
S_{t} e^{k} \frac{\partial N\left(d_{-}\right)}{\partial K} & =K n\left(d_{-}\right) \frac{\partial d}{\partial K} \\
& =\frac{-K}{\sigma \sqrt{\tau} K} n\left(d_{-}\right) \\
& =\frac{-1}{\sigma \sqrt{\tau}} n\left(d_{-}\right)
\end{aligned}
$$

Platting things together

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial K}= & S_{t} \frac{\partial N\left(d_{1}\right)}{\partial K}-S_{t} N(d) \frac{\partial e^{k}}{\partial K} \\
& -S_{t} e^{k} \frac{\partial N(d)}{\partial K} \\
= & -\frac{S_{t}}{\sigma \sqrt{2} K} n\left(d_{t}\right)+\frac{1}{\sigma \sqrt{2}} n\left(d_{-}\right)+N(d)
\end{aligned}
$$

Next consider the second term

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial C_{B S}} & =\frac{\partial}{\partial \sigma_{B S}}\left\{S_{t}\left[N\left(d_{+}\right)-e^{k} N\left(d_{-}\right)\right]\right\} \\
& =S_{t} \frac{\partial N\left(d_{+}\right)}{\partial \sigma_{B S}}-S_{t} e^{k} \frac{\partial}{\partial \sigma_{B S}} N\left(d_{-}\right) \\
& =S_{t} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \sigma_{B S}}-K n\left(d_{-}\right) \frac{\partial d_{-}}{\partial \sigma_{B S}}
\end{aligned}
$$

Now

$$
\frac{\partial d_{A}}{\partial \sigma_{B S}}=\frac{\partial}{\partial \sigma_{B S}}\left\{\frac{R}{\sigma \sqrt{\tau}}+\frac{\sigma \sqrt{\tau}}{2}\right\}
$$

$$
\begin{aligned}
= & \frac{R}{\sigma^{2} \sqrt{\tau}}+\frac{\sqrt{\tau}}{2} \\
\frac{\partial d}{\partial \sigma_{B}} & =\frac{R}{\sigma^{2} \sqrt{\tau}} \cdot \frac{\sqrt{\tau}}{2}
\end{aligned}
$$

so

$$
\begin{aligned}
\frac{\partial C_{B S}}{\partial C_{B S}}= & S_{t} n\left(d_{+}\right) \frac{\partial d_{+}}{\partial \sigma_{B S}}-K n\left(d_{-}\right) \frac{\partial d_{-}}{\partial \sigma_{B S}} \\
= & S_{t} n\left(d_{+}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}}+\frac{\sqrt{\tau}}{2}\right] \\
& -K n\left(d_{-}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}} \cdot \frac{\sqrt{\tau}}{2}\right]
\end{aligned}
$$

Putting things together

$$
\begin{aligned}
D(K, \tau) & =-\frac{\partial C_{B S}}{\partial K}-\frac{\partial C_{B S}}{\partial C_{B S}} \frac{\partial G_{B S}}{\partial K} \\
& =-\frac{s_{t}}{\sigma \sqrt{2} K} n\left(d_{t}\right)+\frac{1}{\sigma \sqrt{2}} n(d .)+N(d)
\end{aligned}
$$

$$
\begin{aligned}
&+ s_{t}\left\{n\left(d_{+}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}}+\frac{\sqrt{\tau}}{2}\right]-\right. \\
&\left.e^{k} n\left(d_{-}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}} \frac{\sqrt{\tau}}{2}\right]\right\} \frac{\partial \sigma_{B s}}{\partial k} \\
& \Rightarrow D(k, \tau)=-\frac{s_{t}}{\sigma \sqrt{\tau}} n\left(d_{+}\right)+\frac{1}{\sigma \sqrt{\tau}} n\left(d_{-}\right)+N\left(d_{-}\right) \\
&+\left\{n\left(d_{+}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}}+\frac{\sqrt{\tau}}{2}\right]-\right. \\
&\left.e^{k} n\left(d_{-}\right)\left[\frac{k}{\sigma^{2} \sqrt{\tau}} \cdot \frac{\sqrt{\tau}}{2}\right]\right\} s_{t} \frac{\partial \sigma_{B s}}{\partial k} \\
& d_{+}(\tau, k)= \frac{k}{\sigma \sqrt{\tau}}+\frac{\sigma \sqrt{\tau}}{2} \\
& d_{-}(\tau, k)= \frac{k}{\sigma \sqrt{\tau}}-\frac{\sigma \sqrt{\tau}}{2}
\end{aligned}
$$

If the option is sold with $s_{t}=k$, i.e. struck at the-money, and $\tau=1$ then

$$
\begin{aligned}
D(1,1)= & \frac{n\left(d_{1}\right)}{\sigma}+\frac{n\left(d_{1}\right)}{\sigma}+N\left(d_{2}\right)+ \\
& {\left[n\left(d_{1}\right)\left(\frac{1}{2}\right)-n\left(d_{1}\right)\left(-\frac{1}{2}\right)\right] K \frac{\partial G_{B S}}{\partial K} }
\end{aligned}
$$

Now ATM for $\tau=1$

$$
\begin{aligned}
& d_{+}=\frac{k}{\sigma \sqrt{\tau}}+\frac{\sigma \sqrt{\tau}}{2}=\frac{\sigma}{2} \\
& d_{-}=\frac{k}{\sigma \sqrt{\tau}}-\frac{\sigma \sqrt{\tau}}{2}=\frac{\sigma}{2}
\end{aligned}
$$

So

$$
n\left(d_{1}\right)=n(d)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{\delta^{2}}{\delta}}
$$

Trues

$$
D(1,1)=\frac{-n\left(\delta_{1}\right)}{0}+\frac{\bar{n}\left(d_{2}\right)}{\sigma}+N\left(d_{-}\right)+
$$

$$
\begin{aligned}
& {\left[n(d)\left(\frac{1}{2}\right)-n(d)\left(\frac{1}{2}\right)\right] K \frac{\partial G_{B S}}{\partial K} } \\
= & N\left(-\frac{G_{B S}}{\partial}\right)+\frac{1}{\sqrt{\partial \pi}} e^{-\frac{\sigma_{B S}^{2}}{\sigma^{3}}}\left(K \frac{\partial G_{B S}}{\partial K}\right) \\
= & D(1,1)=N\left(-\frac{\sigma_{B S}}{\partial}\right)+\frac{1}{\sqrt{2 \pi}} e^{-\frac{\sigma_{B S}^{2}}{8}}\left(K \frac{\partial \sigma_{B S}}{\partial K}\right)
\end{aligned}
$$

## Volatility Derivatives

This section will discuss the pricing of volatility derivatives.
Recall that the PDF of the asset price is related to a European style option in the following matter,

$$
\begin{aligned}
p\left(S_{T}, T, S_{t}, t\right) & =\left.\frac{\partial^{2} \tilde{C}}{\partial K^{2}}\left(S_{t}, K, t, T\right)\right|_{K=S_{T}} \\
& =\left.\frac{\partial^{2} \tilde{P}}{\partial K^{2}}\left(S_{t}, K, t, T\right)\right|_{K=S_{T}}
\end{aligned}
$$

Where $C\left(S_{t}, K, t, T\right)$ and $P\left(S_{t}, K, t, T\right)$ are the price of European Call and Put options and $p\left(S_{T}, T ; S_{t}, t\right)$ is the PDF for $s_{T}$ given $s_{t}$.
Consider the generalized contigent claim, $g\left(S_{\tau}\right)$. The price of the contigent claim at time $T$ given the asset price at $t$ is given by
$E\left[g\left(S_{T}\right) \mid S_{t}\right]_{1}$ where the expectation is with respect to the risk-neutral probalitity and it is assumed thal the risk-free return is zero.

Now,

$$
\begin{aligned}
E\left[g\left(s_{T}\right) \mid s_{t}\right]=\int_{0}^{d} p\left(K, T ; s_{t}, t\right) g(K) d K \\
=\int_{0}^{F} \frac{\partial^{2} \tilde{P}\left(K, T ; s_{t}, t\right)}{\partial K^{2}} g(K) d K \\
+\int_{F}^{d} \frac{\partial^{2} \tilde{C}\left(K, T ; s_{t}, t\right)}{\partial K^{2}} g(K) d K
\end{aligned}
$$

This follows from,

$$
\tilde{P}=(K-F)^{+} \quad \tilde{C}=(F-K)^{+}
$$

so that $\tilde{P}=0$ for $F \geqslant K$ and $\tilde{c}=0$ for $F \leqslant K$.

Now integrating by parts gives for the first term with,

$$
\begin{aligned}
& \int_{0}^{T} u d v=\left.u v\right|_{0} ^{T}-\int_{0}^{T} v d u \\
& u=g(k) \Rightarrow d u=g^{\prime}(k) d k \\
& d v=\frac{\partial^{2} \tilde{P}}{\partial k^{2}} d k \Rightarrow v=\frac{\partial \tilde{P}}{\partial k}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \int_{0}^{F} \frac{\partial^{2} \tilde{P}\left(K, T ; S_{t}, t\right)}{\partial K^{2}} g(K) d K \\
& \quad=\left.g(K) \frac{\partial \tilde{P}}{\partial K}\right|_{0} ^{F}-\int_{0}^{F} \frac{\partial \tilde{P}}{\partial K} g^{\prime}(K) d K
\end{aligned}
$$

doing the integral again gives

$$
\begin{aligned}
& u=S^{\prime}(k) \Rightarrow d u=\zeta^{\prime \prime}(k) d k \\
& d v=\frac{\partial \tilde{P}}{\partial k} d k \Rightarrow v=\tilde{P}(k)
\end{aligned}
$$

so

$$
\begin{array}{r}
=\left.g(k) \frac{\partial \tilde{P}}{\partial k}\right|_{0} ^{F}-\left.g^{\prime}(k) \tilde{P}(k)\right|_{0} ^{F} \\
+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k
\end{array}
$$

similarly,

$$
\begin{aligned}
\int_{F}^{A} \frac{\partial^{2} \tilde{c}\left(k, T_{i} S_{t}, t\right)}{\partial k^{2}} & g(k) d k \\
= & \left.g(k) \frac{\partial \tilde{c}}{\partial k}\right|_{F} ^{\infty}-\left.g^{\prime}(k) \tilde{c}(k)\right|_{F} ^{A} \\
& +\int_{F}^{A} \tilde{c}(k) g^{\prime \prime}(k) d k
\end{aligned}
$$

Putting things together gives

$$
\begin{aligned}
& E\left[g\left(S_{T}\right) \mid S_{t}\right]=\left.g(k) \frac{\partial \tilde{P}}{\partial k}\right|_{0} ^{F}-\left.g^{\prime}(k) \tilde{P}(k)\right|_{0} ^{F} \\
& +\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+\left.g(k) \frac{\partial \tilde{C}}{\partial k}\right|_{F} ^{\infty}
\end{aligned}
$$

$$
\begin{aligned}
& \left.g^{\prime}(k) \tilde{C}(k)\right|_{F} ^{\infty}+\int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k \\
& \left.=g^{\prime F}\right)\left.\frac{\partial \tilde{P}}{\partial k}\right|_{k=F}-\left.g^{(0)} \frac{\partial \tilde{P}}{\partial k}\right|_{k=0} ^{0} \\
& +\left.g(\infty) \frac{\partial \tilde{C}}{\partial k}\right|_{k=\infty} ^{0}-\left.g(F) \frac{\partial \tilde{C}}{\partial k}\right|_{k=F} \\
& -g^{\prime}(F) \tilde{P}(F)+g^{\prime}(\alpha) \tilde{P}(0)-g^{\prime}(\alpha) x^{\tilde{C}}(\infty) \\
& +g^{\prime}(F) \tilde{C}(F)+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+ \\
& \int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{aligned}
$$

Now $P(0)=0$ and $\tau(\alpha)=0$.
Recall that Put-call Parity for zero risk-free return implies

$$
\begin{aligned}
& \tilde{C}(F, K)-\tilde{P}(F, K)=F-K \\
\Rightarrow & \tilde{C}(F, K)=\tilde{P}(F, K)+F \cdot K
\end{aligned}
$$

50

$$
\frac{\partial \tilde{C}}{\partial K}-\frac{\partial \tilde{P}}{\partial K}=-1
$$

Now as $K \rightarrow 0$ for fixed $F, \tilde{C} \rightarrow F-K \tilde{p} \rightarrow 0$, so

$$
\frac{\partial \tilde{x}}{\partial K} \rightarrow-1 \Rightarrow \frac{\partial \tilde{P}}{\partial K} \rightarrow 0
$$

and as $K \rightarrow \infty \quad \tilde{C} \rightarrow 0$ and $\tilde{P} \rightarrow K-F$

$$
\frac{\partial \tilde{C}}{\partial K} \rightarrow 0 \quad \frac{\partial \tilde{P}}{\partial K} \rightarrow 1
$$

thes,

$$
\left.\frac{\partial \tilde{P}}{\partial K}\right|_{K=0}=\left.0 \quad \frac{\partial \tilde{C}}{\partial K}\right|_{K=8}=0
$$

so

$$
\begin{aligned}
& E\left[g\left(S_{T}\right) \mid S_{t}\right]=\left.g(F) \frac{\partial \tilde{P}}{\partial k}\right|_{k=F}-\left.g(F) \frac{\partial \tilde{C}}{\partial k}\right|_{k=F} \\
& -g^{\prime}(F) \tilde{P}(F)+g^{\prime}(F) \tilde{C}(F) \\
& +\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+\int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{aligned}
$$

$$
\begin{aligned}
= & g(F)\left[\left.\frac{\partial \tilde{P}}{\partial k}\right|_{k=F}-\left.\frac{\partial \tilde{C}}{\partial K}\right|_{k=F}\right] \\
& +g(F)[\tilde{\zeta}(F)-\tilde{P}(F)]+ \\
& \int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+\int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{aligned}
$$

Again for $k=F$ from

$$
\tilde{C}(F, K)=\tilde{P}(F, K)
$$

and

$$
\frac{\partial \tilde{C}}{\partial k}-\frac{\partial \tilde{P}}{\partial k}=-1
$$

thus,

$$
\begin{gathered}
E\left[g\left(S_{T}\right) \mid S_{t}\right]=g(F)+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+ \\
\int_{F}^{\Delta} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{gathered}
$$

This is a very interesting result. It is saying the any derioative security that is twice differentiable can be written as integrals over European Call and Put options weighted by the second derivative over contigent claim.

## Example: European Call option

consider a European call option.

$$
g\left(S_{T}\right)=\left(S_{T}-L\right)^{+}
$$

Now for $S_{T}=K$

$$
\begin{aligned}
& g^{\prime}(k)=\theta(k \cdot L) \\
& g^{\prime \prime}(k)=\delta(k \cdot L)
\end{aligned}
$$

It follows that,

$$
\begin{gathered}
E\left[\left(S_{T}-L\right)^{+}\right]=(F-L)^{+}+\int_{0}^{F} \tilde{P}(k) \delta(k-L) d k \\
+\int_{F}^{\infty} \tilde{C}(k) \delta(k-L) d k
\end{gathered}
$$

Consider the case $L<F$ for this case only the first two terms contribute so

$$
E\left[\left(S_{T}-L\right)^{H}\right]=(F-L)+\tilde{P}(L)
$$

and for $L \geqslant F$ only the second torm contributes

$$
E\left[\left(S_{T}-L\right)^{+}\right]=\tilde{C}(L)
$$

so

$$
E\left[\left(S_{T}-L\right)^{+}\right]= \begin{cases}(F-L)+\tilde{P}(L) & L<F \\ \tilde{C}(L) & L \geqslant F\end{cases}
$$

Recall put-call parity

$$
\begin{aligned}
& \tilde{C}(F, L)-\tilde{P}(F, L)=F-L \\
\Rightarrow & \tilde{C}(F, L)=(F-L)+\tilde{P}(L)
\end{aligned}
$$

Thus as expected.

$$
E\left[\left(S_{T} \cdot L\right)^{+}\right]=\tilde{c}(L)
$$

## Example: Amortizing Options

Amortizing options are defined by

$$
g\left(S_{T}\right)=\frac{\left(S_{T}-L\right)^{t}}{S_{T}}
$$

Now for $S_{T}=K$

$$
\begin{aligned}
g(k)= & \frac{(k-L)^{+}}{k} \\
g^{\prime}(k)= & \frac{\theta(k-L)}{k}-\frac{(k-L)^{+}}{k^{2}} \\
S^{\prime \prime}(k)= & \frac{\delta(k-L)}{k}-\frac{\theta(k-L)}{k^{2}}-\frac{\theta(k-L)}{k^{2}} \\
& +\frac{2(k-L)^{+}}{k^{3}} \\
= & \frac{\delta(k-L)}{k}-\frac{2 \frac{\theta(k-L)}{k^{2}}}{k}+2 \frac{(k-L)^{+}}{k^{3}}
\end{aligned}
$$

Consider the last two terms for $K \geqslant L$

$$
\begin{aligned}
& 2 \frac{2 \theta(k-L)}{k^{2}}+2 \frac{(k-L)^{1}}{k^{3}}=\frac{2}{k^{2}}+\frac{2(k-L)}{k^{3}} \\
& =\frac{-2 k^{3}+2 k^{3}-2 L}{k^{3}}=-\frac{2 L}{k^{3}} \\
& =\frac{-2 L \theta(K-L)}{k^{3}}
\end{aligned}
$$

Putting things together gives

$$
S^{\prime \prime}\left(S_{T}\right)=\frac{\delta\left(S_{T}-L\right)}{S_{T}}-\frac{2 L \theta\left(S_{T}-L\right)}{S_{T}^{3}}
$$

using

$$
\begin{gathered}
E\left[g\left(S_{T}\right) \mid S_{t}\right]=g(F)+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+ \\
\int_{F}^{\Delta} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{gathered}
$$

gives

$$
\begin{aligned}
E & {\left[\frac{\left(S_{T}-L\right)^{+}}{S_{T}}\right]=\frac{(F-L)^{+}}{F} } \\
& +\int_{0}^{F}\left[\frac{\delta(K-L)}{K}-\frac{2 L \theta(K-L)}{K^{3}}\right] \tilde{P}(K) d K \\
& +\int_{F}^{\infty}\left[\frac{\delta(K-L)}{K}-\frac{2 L \theta(K-L)}{K^{3}}\right] \tilde{C}(K) d K
\end{aligned}
$$

Consider the case L>F, The first two terms are zero, then

$$
\begin{aligned}
E\left[\frac{\left(S_{T}-L\right)^{+}}{S_{T}}\right] & =\int_{F}^{\infty}\left[\frac{\delta(K-L)}{K}-\frac{2 L \theta(K-L)}{K^{3}}\right] \tilde{C}(K) d K \\
& =\frac{\tilde{C}(L)}{L} \cdot \int_{L}^{\infty} \frac{2 L}{K^{3}} \tilde{C}(K) d K \\
\Rightarrow E\left[\frac{\left(S_{T}-L\right)^{+}}{S_{T}}\right] & =\frac{\tilde{C}(L)}{L} \cdot 2 L \int_{L}^{\infty} \frac{\tilde{C}(K)}{K^{3}} d K
\end{aligned}
$$

## Example: Log Contract

Consider

$$
g\left(S_{T}\right)=\ln \left(\frac{S_{I}}{F}\right)
$$

Now

$$
\begin{aligned}
& g^{\prime}(k)=\frac{1}{k} \\
& g^{\prime \prime}(k)=-\frac{1}{k^{2}}
\end{aligned}
$$

using

$$
\begin{gathered}
E\left[g\left(s_{T}\right) \mid s_{t}\right]=g(F)+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k+ \\
\int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{gathered}
$$

It follows that

$$
E\left[\ln \left(\frac{S_{I}}{F}\right)\right]=\ln \left(\frac{F}{F}\right)-\int_{0}^{F} \frac{\hat{P}(K)}{K^{2}} d K
$$

$$
\begin{gathered}
-\int_{F}^{\infty} \frac{\tilde{C}(k)}{k^{2}} d k \\
=-\int_{0}^{F} \frac{\tilde{P}(k)}{k^{2}} d k \cdot \int_{F}^{\infty} \frac{\tilde{C}(k)}{k^{2}} d k
\end{gathered}
$$

write the integral in terms of the log-strike

$$
\begin{aligned}
& k=\ln \left(\frac{k}{F}\right) \Rightarrow k=F e^{k} \\
\Rightarrow & d k=\frac{d k}{k}
\end{aligned}
$$

It follows that
$E\left[\ln \left(\frac{S_{I}}{F}\right)\right]=-\int_{-\infty}^{0} \frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}} d k-\int_{0}^{\infty} \frac{\tilde{C}\left(F e^{k}\right)}{F e^{k}} d k$
let

$$
p(k)=\frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}} \quad c(k)=\frac{\tilde{C}\left(F e^{k}\right)}{F e^{k}}
$$

Then

$$
E\left[\ln \left(\frac{S_{I}}{F}\right)\right]=-\int_{-\infty}^{0} p(k) d k-\int_{0}^{\infty} c(k) d k
$$

## Variance and volatility swaps

consider the log-spot price

$$
\ln \left(\frac{S_{I}}{F}\right)
$$

Where $F$ is the forward price

$$
F=s_{0} e \int_{0}^{T} u d t
$$

If the riskfree rate of return is zero at there are no dividends

$$
F=S_{0}
$$

now

$$
\ln \left(\frac{S_{I}}{F}\right)=\ln \left(\frac{S_{I}}{S_{0}}\right)=\int_{0}^{T} d\left(\ln S_{t}\right)
$$

if

$$
d S_{t}=\sigma\left(S_{t}\right) S_{t} d \omega_{t}
$$

then from Itô's lemma

$$
d f\left(s_{t}\right)=\frac{\partial f}{\partial s_{t}} d s_{t}+\frac{1}{2} \frac{\partial^{2} f}{\partial s_{t}}\left(d s_{t}\right)^{2}
$$

Now

$$
\left(d s_{t}\right)^{2}=\sigma^{2} s_{t}^{2} d t
$$

It follows that

$$
d f\left(S_{t}\right)=\frac{\partial f}{\partial S_{t}} d S_{t}+\sigma^{2} S_{t}^{2} \frac{\partial^{2} f}{\partial S_{t}^{2}} d t
$$

for $f\left(s_{t}\right)=\ln s_{t}$

$$
\begin{aligned}
d \ln S_{t} & =\frac{d S_{t}}{S_{t}}-\frac{\sigma^{2}}{\partial S_{t}^{2}}\left(S_{t}\right) S_{t}^{2} d t \\
& =\frac{1}{S_{t}} d S_{t}-\frac{\sigma^{2}\left(S_{t}\right)}{2} d t
\end{aligned}
$$

So

$$
\ln \left(\frac{S_{T}}{S_{0}}\right)=\int_{0}^{T} d\left(\ln S_{t}\right)
$$

$$
=\int_{0}^{T} \frac{1}{S_{t}} d S_{t}-\int_{0}^{T} \frac{\sigma^{2}\left(S_{t}\right)}{2} d t
$$

Now the total variance is given by,

$$
\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t
$$

Taking expectation gives

$$
\begin{aligned}
& E\left[\ln \left(\frac{S_{I}}{S_{0}}\right)\right]=E\left[\int_{0}^{T} \frac{1}{S_{t}} d S_{t}-\int_{0}^{T} \frac{\sigma^{2}\left(S_{t}\right)}{2} d t\right] \\
& =E\left[\int_{0}^{T} \frac{1}{S_{t}} d S_{t}\right]-\frac{1}{2} E\left[\int_{0}^{T} \sigma^{2}\left(S_{t}\right) d t\right]
\end{aligned}
$$

Now $S_{t}$ is a martingale since zero drift has been assumed, so

$$
E\left[\int_{0}^{T} \frac{1}{S_{t}} d S_{t}\right]=0
$$

Thus the expectation of the total variance is given by

$$
E\left[\int_{0}^{\top} \sigma\left(s_{t}\right) d t\right]=-2 E\left[\ln \left(\frac{s_{I}}{s_{0}}\right)\right]
$$

Previously it was shown that

$$
E\left[\ln \left(\frac{S_{I}}{F}\right)\right]=-\int_{-\infty}^{0} p(k) d k \cdot \int_{0}^{\infty} c(k) d k
$$

it follows that

$$
\begin{gathered}
E\left[\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t\right]=2\left\{\int_{-\infty}^{0} p(k) d k+\right. \\
\left.\int_{0}^{\infty} c(k) d k\right\}
\end{gathered}
$$

## Variance Swaps

A variance swap is not a swap but a forward contract to deliver a specified amount of total variance annualized variance at time $T$.

The total variance is computed numerically ard is given by,

$$
\begin{aligned}
& U_{T}=\operatorname{var}\left[\ln \left(\frac{S_{I}}{F}\right)\right] \\
& * \frac{1}{N} \sum_{i=1}^{N}\left[\ln \frac{S_{i}}{S_{i-1}}\right]^{2}-\left[\frac{1}{N} \ln \left(\frac{S_{N}}{S_{0}}\right)\right]^{2}
\end{aligned}
$$

The variance delivered is given by

$$
N \times A \times U_{T}-N K_{u a r}
$$

where $N$ is the notional amount of swap, Kucr is the is the strike price and $A$ is the arrualization factor.

## Variance Swaps in the Heston model

Recall that in the Heston model the instantaneous variance, $v_{t}$, is given by

$$
d v_{t}=-\lambda\left(v_{t}-\bar{v}\right) d t+\eta \sqrt{v_{t}} d z_{t}
$$

Where $2 \sim$ Normal $(0,1), \bar{v}$ is the mean value of $v_{t}, \eta$ is the variance of the variance and $\lambda$ the rate of relaxation to $\bar{U}$.

The total variance is given by

$$
\omega_{T}=\int_{0}^{T} v_{t} d t
$$

The expectation of $\omega_{T}$ is given by

$$
\begin{aligned}
E\left[\omega_{T}\right] & =E\left[\int_{0}^{T} v_{t} d t\right] \\
& =\int_{0}^{T} E\left[v_{t}\right] d t
\end{aligned}
$$

$$
=\int_{0}^{T} \hat{U}_{t} d t
$$

Now from the SDE

$$
\begin{aligned}
& E\left[d v_{t}\right]=d E\left[v_{t}\right]=d \hat{v}_{t} \\
& \quad=-\lambda\left(\hat{v}_{t}-\bar{v}\right) d t+\eta E\left[v_{t} d z_{t}\right]
\end{aligned}
$$

The last term is zero since it is a martingale with zero mean it follows that

$$
\begin{aligned}
& d \hat{v}_{t}=-\lambda\left(\hat{v}_{t}-\bar{v}\right) d t \\
\Rightarrow & d\left(\hat{v}_{t}-\bar{v}\right)=-\lambda\left(\hat{v}_{t}-\bar{v}\right) d t \\
\Rightarrow & \frac{d\left(\hat{v}_{t}-\bar{v}\right)}{\left(\hat{v}_{t}-\bar{v}\right)}=-\lambda d t \\
\Rightarrow & d \ln \left(\hat{v}_{t}-\bar{v}\right)=-\lambda d t \\
\Rightarrow & \ln \left(\hat{v}_{t}-\bar{v}\right)=-\lambda t+c \\
\Rightarrow & \hat{v}_{t}-\bar{v}=c e^{-\lambda t}
\end{aligned}
$$

If $t=0$, then

$$
c=\hat{v}_{0} \cdot \bar{v}
$$

50

$$
\hat{v}_{t}=\left(\hat{v}_{0}-\bar{v}\right) e^{\lambda t}+\bar{v}
$$

it follows that the total variance is given by

$$
\begin{aligned}
E\left[\omega_{t}\right] & =\int_{0}^{T} \hat{v}_{t} d t \\
& =\int_{0}^{T}\left(\hat{v}_{0}-\bar{v}\right) e^{-\lambda t}+\bar{v} d t \\
& =-\frac{\left(\hat{v}_{0} \cdot \bar{v}\right)}{\lambda} e^{-\lambda t}+\left.\bar{v}\right|_{0} ^{T} \\
& =-\frac{\left(\hat{v}_{0} \cdot \bar{v}\right)}{\lambda} e^{-\lambda T}+\frac{\left(\hat{v}_{0} \cdot \bar{v}\right)}{\lambda}+\bar{v} T \\
& =\left(1-e^{-\lambda T}\right)\left(\frac{\hat{v}_{0} \cdot \bar{v}}{\lambda}+\bar{v} T\right.
\end{aligned}
$$

The annualized total variance is given by

$$
\frac{E\left[\omega_{t}\right]}{T}=\left(1-e^{-\lambda T}\right) \frac{\left(\hat{v}_{0}-\bar{v}\right)}{\lambda T}+\bar{v}
$$

## Dependence on stow and Curvature

In this section an expression for the price of a varrance swap in the Heston model is derived.
starting with a strip of European options of a given expiration the relation of the price of a variance swap to the at the-money forward implied odatility, the oolatility skew and the volatility curvature (smile).
It will be shown that the fair value of variance is given by

$$
E\left[\omega_{T}\right]=\int_{-\infty}^{\infty} N^{\prime}(z) \sigma_{B S}^{z}(z) T d z
$$

where

$$
z(k)=\frac{k}{\sigma_{B S}(k) / T}-\frac{\sigma_{B S}(k) \sqrt{T}}{2}
$$

where $k$ is the log strike,

$$
k=\ln \frac{k}{F}
$$

To start, recall that the price of an undiscounted European call option price is given by

$$
c=F\left\{N\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{k} N\left(-\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)\right\}
$$

where

$$
\begin{array}{r}
k=\ln \frac{K}{F} \quad \omega=\sigma_{B S}(k) \sqrt{T} \\
F=S_{0} e^{\int_{0}^{T} \mu d t}
\end{array}
$$

let

$$
d_{+}=-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2} \quad d_{-}=\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}
$$

Previously it was shown that the value of the variance steap is given by,

$$
\partial E\left[\ln \frac{S_{I}}{F}\right]=2 \int_{0}^{A} \ln \left(\frac{K}{F}\right) \frac{\partial^{2} C}{\partial K^{2}} d K
$$

let

$$
\begin{aligned}
& k=\ln \left(\frac{K}{F}\right) \\
\Rightarrow & d k=\frac{\partial k}{\partial K} d K=\frac{1}{K} d K \\
\Rightarrow & k d k=d K
\end{aligned}
$$

thus

$$
\partial E\left[\ln \frac{S_{I}}{F}\right]=2 \int_{-\infty}^{\infty} k k \frac{\partial^{2} C}{\partial k^{2}} d k
$$

Now differentiating $C$ with respect to $K$ gives

$$
\frac{\partial C}{\partial K}=\frac{\partial C}{\partial K} \frac{\partial K}{\partial K}=\frac{1}{K} \frac{\partial C}{\partial K}
$$

$$
\begin{aligned}
& =\frac{1}{k} \frac{\partial}{\partial k}\left\{F\left[N\left(d_{+}\right)-e^{k} N\left(d_{-}\right)\right]\right\} \\
& =\frac{F}{k}\left[n\left(d_{+}\right) \frac{\partial d_{+}}{\partial k}-e^{k} N\left(d_{-}\right)-e^{k} n\left(d_{-}\right) \frac{\partial d}{\partial k}\right]
\end{aligned}
$$

Assume.

$$
\begin{aligned}
& n\left(d_{+}\right)=e^{k} n\left(d_{-}\right) \\
\Rightarrow & \frac{1}{\sqrt{2 \pi}} e^{-d_{1 / 2}^{2}}=e^{k} \frac{1}{\sqrt{2 \pi}} e^{-d_{-1}^{2}} \\
\Rightarrow & e^{-d_{+/ 2}^{2}+d_{-1}^{2}}=e^{k} \\
\Rightarrow & -\frac{d_{+}^{2}}{2}+\frac{d_{-}^{2}}{2}=k \\
\Rightarrow & -d_{+}^{2}+d_{-}^{2}=2 k
\end{aligned}
$$

Now

$$
\begin{aligned}
& -d_{+}^{2}+d_{-}^{2}=-\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)^{2}+\left(-\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)^{2} \\
& =-\left(\frac{k^{2}}{\omega}-k+\frac{\omega}{2}\right)+\left(\frac{k^{2}}{\omega}+k+\frac{\omega}{2}\right) \\
& =2 k
\end{aligned}
$$

Trues

$$
n\left(d_{+}\right)=e^{k} n\left(d_{-}\right)
$$

It follows that

$$
\begin{aligned}
\frac{1}{k} \frac{\partial C}{\partial k} & =\frac{F}{k}\left[n\left(d_{+}\right) \frac{\partial d_{+}}{\partial k}-e^{k} N\left(d_{-}\right)-e^{k} n\left(d_{-}\right) \frac{\partial d^{-}}{\partial k}\right] \\
& =\frac{E}{k}\left[e^{k} n\left(d_{-}\right) \frac{\partial d_{+}}{\partial k} \cdot e^{k} n\left(d_{-}\right) \frac{\partial d_{-}}{\partial k} \cdot e^{k} N\left(d_{-}\right)\right] \\
& =\frac{E e^{k}}{k}\left[n\left(d_{-}\right)\left(\frac{\partial d_{+}}{\partial k} \cdot \frac{\partial d_{-}}{\partial k}\right)-N\left(d_{-}\right)\right]
\end{aligned}
$$

Now consider the derivatives

$$
\begin{aligned}
\frac{\partial d_{+}}{\partial k} \cdot \frac{\partial d_{-}}{\partial k} & =\frac{\partial}{\partial k}\left(d_{+}-d_{-}\right) \\
& =\frac{\partial}{\partial k}\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}+\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right) \\
& =\frac{\partial}{\partial k} \sqrt{\omega}
\end{aligned}
$$

and

$$
\frac{E e^{k}}{k}=\frac{E}{k} e^{\ln \frac{k}{F}}=1
$$

Putting things together gives
$\frac{\partial C}{\partial K}=\frac{1}{K} \frac{\partial C}{\partial R}=\left[n(d) \frac{\partial \sqrt{\omega}}{\partial R}-N\left(d_{-}\right)\right]$

Now for the second derivative

$$
\begin{aligned}
\frac{\partial^{2} C}{\partial K^{2}} & =\frac{1}{K} \frac{\partial}{\partial k}\left(\frac{1}{K} \frac{\partial C}{\partial k}\right) \\
& =\frac{1}{K} \frac{\partial}{\partial k}\left[n(d) \frac{\partial \sqrt{\omega}}{\partial k}-N\left(d_{-}\right)\right]
\end{aligned}
$$

Now for the first derivative

$$
\begin{aligned}
\frac{\partial}{\partial k} & {\left[n(d) \frac{\partial \sqrt{\omega}}{\partial k}\right]=\frac{\partial n(d)}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k} } \\
& +n(d) \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}} \\
= & \frac{\partial n(d)}{\partial d}\left(\frac{\partial d}{\partial k}\right)\left(\frac{\partial \sqrt{\omega}}{\partial k}\right)+n(d) \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}} \\
\frac{\partial}{\partial k} & v(d)=n(d) \frac{\partial d}{\partial k}
\end{aligned}
$$

Now consider

$$
\begin{aligned}
\frac{\partial n(d)}{\partial d_{-}} & =\frac{\partial}{\partial d}\left(\frac{1}{\sqrt{2 \pi}} e^{-d^{2} / 2}\right) \\
& =\frac{1}{\sqrt{2 \pi}} e^{-d^{2} / 2}\left(-d_{-}\right) \\
& =-d_{-} n\left(d_{-}\right)
\end{aligned}
$$

so
$\frac{\partial}{\partial k}\left[n(d) \frac{\partial \sqrt{\omega}}{\partial k}\right]=$

$$
-2 d_{-} n\left(d_{-}\right)\left(\frac{\partial d}{\partial k}\right)\left(\frac{\partial \sqrt{\omega}}{\partial k}\right)+n\left(d_{-}\right) \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}
$$

putting things together

$$
\begin{aligned}
\frac{\partial^{2} c}{\partial k^{2}} & =\frac{1}{k} \frac{\partial}{\partial k}\left[n(d) \frac{\partial \sqrt{\omega}}{\partial k}-N\left(d_{-}\right)\right] \\
& =\frac{1}{k}\left[-d \_n(d)\left(\frac{\partial d}{\partial k}\right)\left(\frac{\partial \sqrt{\omega}}{\partial k}\right)\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.+n\left(d_{-}\right) \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}-n\left(d_{-}\right) \frac{\partial d_{-}}{\partial k}\right] \\
\Rightarrow \frac{\partial^{2} c}{\partial k^{2}}= & \frac{n\left(d_{-}\right)}{k}\left[-\frac{\partial d_{-}}{\partial k}\left(d_{-} \frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right]
\end{aligned}
$$

Next consider

$$
\begin{aligned}
\frac{\partial d}{\partial k} & =\frac{\partial}{\partial k}\left(\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right) \\
& =-\frac{1}{\sqrt{\omega}}+\frac{k}{\omega} \frac{\partial \sqrt{\omega}}{\partial k}-\frac{1}{2} \frac{\partial \sqrt{\omega}}{\partial k} \\
& =\frac{1}{\sqrt{\omega}}\left(-1+\frac{k}{\sqrt{\omega}} \frac{\partial \sqrt{\omega}}{\partial k}-\frac{\sqrt{\omega}}{2} \frac{\partial \sqrt{\omega}}{\partial k}\right) \\
& =\frac{1}{\sqrt{\omega}}\left[-1-\frac{\partial \sqrt{\omega}}{\partial k}\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)\right] \\
& =-\frac{1}{\sqrt{\omega}}\left(1+d_{+} \frac{\partial \sqrt{\omega}}{\partial k}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \frac{\partial^{2} c}{\partial k^{2}}=\frac{n\left(d_{-}\right)}{k} {\left[\frac{\partial d_{-}}{\partial k}\left(d_{-} \frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right] } \\
&=\frac{n\left(d_{-}\right)}{k} {\left[\frac{1}{\sqrt{\omega}}\left(1+d_{+} \frac{\partial \sqrt{\omega}}{\partial k}\right)\left(d_{-} \frac{\partial \sqrt{\omega}}{\partial k}+1\right)\right.} \\
&\left.+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right] \\
&=\frac{n\left(d_{-}\right)}{k}\left\{\frac { 1 } { \sqrt { \omega } } \left[d_{+} d_{-}\left(\frac{\partial \sqrt{\omega}}{\partial k}\right)^{2}+\frac{\partial \sqrt{\omega}}{\partial k}\left(d_{+}+d_{-}\right)\right.\right. \\
&+\left.1]+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right\}
\end{aligned}
$$

but

$$
\begin{aligned}
d_{+}+d & =\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2} \frac{k}{\sqrt{\omega}} \cdot \frac{\sqrt{\omega}}{2} \\
& =-\frac{\partial k}{\sqrt{\omega}}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial^{2} c}{\partial k^{2}}=\frac{n(d)}{k} & \left\{\frac { 1 } { \sqrt { \omega } } \left[d_{+} d\left(\frac{\partial \sqrt{\omega}}{\partial k}\right)^{2}-\frac{\partial k}{\sqrt{\omega}} \frac{\partial \sqrt{\omega}}{\partial k}\right.\right. \\
+1] & \left.+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right\}
\end{aligned}
$$

Recall that the value of a variance swap is given by

$$
\partial E\left[\ln \frac{S_{I}}{F}\right]=2 \int_{-\infty}^{\infty} k k \frac{\partial^{2} C}{\partial K^{2}} d k
$$

using

$$
\frac{\partial^{2} c}{\partial k^{2}}=\frac{n\left(d_{-}\right)}{k}\left[-\frac{\partial d_{-}}{\partial k}\left(0-\frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right]
$$

gives
$\partial E\left[\ln \frac{S_{I}}{F}\right]=2 \int_{-\infty}^{\infty} k n(d)\left[-\frac{\partial d}{\partial k}\left(d-\frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial R^{2}}\right] d k$
now consider

$$
\begin{aligned}
& k\left[-\frac{\partial d}{\partial k}\left(d-\frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}\right] \\
& =-k \frac{\partial d}{\partial k}-k d-\frac{\partial d}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}+k \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}
\end{aligned}
$$

Now

$$
\begin{aligned}
\frac{\partial d}{\partial k} & =\frac{\partial}{\partial k}\left(\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right) \\
& =-\frac{1}{\sqrt{\omega}}+k \frac{1}{\omega} \frac{\partial \sqrt{\omega}}{\partial k}-\frac{1}{2} \frac{\partial \sqrt{\omega}}{\partial k} \\
& =-\frac{1}{\sqrt{\omega}}\left[1+\frac{\partial \sqrt{\omega}}{\partial k}\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)\right] \\
& =-\frac{1}{\sqrt{\omega}}\left(1+d_{+} \frac{\partial \sqrt{\omega}}{\partial k}\right)
\end{aligned}
$$

consider
$d-\frac{\partial d}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}=\frac{1}{2} \frac{\partial d^{2}}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}$
but

$$
\begin{aligned}
& \frac{\partial}{\partial k}\left(\frac{1}{2} d^{2}-\frac{\partial \sqrt{\omega}}{\partial k}\right)=d-\frac{\partial d}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}+\frac{1}{2} d^{2} \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}} \\
\Rightarrow & d-\frac{\partial d}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}=\frac{\partial}{\partial k}\left(\frac{1}{2} d^{2}-\frac{\partial \sqrt{\omega}}{\partial k}\right)-\frac{1}{2} d^{2} \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}
\end{aligned}
$$

and

$$
\begin{gathered}
d-\frac{\partial d}{\partial k} \frac{\partial \sqrt{\omega}}{\partial k}+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}=\frac{\partial}{\partial k}\left(\frac{1}{2} d^{2}-\frac{\partial \sqrt{\omega}}{\partial k}\right)- \\
\frac{1}{2} d^{2} \frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}+\frac{\partial^{2} \sqrt{\omega}}{\partial k^{2}}
\end{gathered}
$$

I do not see how this is going to work out. I think this is the correct approach but in may take sometime. In the book the term brute force approach is used. It can be shown that.
$\partial E\left[\ln \frac{S_{I}}{F}\right]=2 \int_{-\infty}^{\infty} k n(d)\left[-\frac{\partial d}{\partial k}\left(d-\frac{\partial \sqrt{\omega}}{\partial k}+1\right)+\frac{\partial^{2} \sqrt{\omega}}{\partial R^{2}}\right] d k$

$$
\begin{aligned}
& =2 \int_{-\infty}^{\infty} n\left(d_{-}\right)\left[k \frac{\partial d}{\partial k}-\frac{\partial \sqrt{\omega}}{\partial k}\right] d k \\
& =\int_{-\alpha}^{\infty} n\left(d_{-}\right) \frac{\partial d}{\partial k} \omega d k
\end{aligned}
$$

Thus the value of a variance sloop is given by

$$
\partial E\left[\ln \frac{S_{I}}{F}\right]=\int_{-\alpha}^{\infty} n(d) \frac{\partial d}{\partial k} \omega d k
$$

Now consider

$$
\begin{array}{r}
d=-\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2} \\
\Rightarrow d d=\frac{\partial d}{\partial t} d k
\end{array}
$$

so

$$
\partial E\left[\ln \frac{S_{I}}{F}\right]=\int_{-\infty}^{\infty} n(d) \omega d d-
$$

Now

$$
\omega=\sigma_{B S}^{2} T
$$

and

$$
\begin{aligned}
E\left[\omega_{T}\right] & =2 E\left[\ln \frac{S_{T}}{F}\right] \\
& =\int_{-\infty}^{A} n\left(d_{-}\right) \sigma_{B S}^{2}\left(d_{-}\right) T d d
\end{aligned}
$$

letting $z=d$. the final result becomes

$$
E\left[\omega_{T}\right]=\int_{-\infty}^{\infty} n(z) \sigma_{B S}^{2}(z) T d z
$$

If $\sigma_{B S}^{2}(2)$ is assumed to have the form

$$
\sigma_{B S}^{2}(z)=\sigma_{0}^{2}+\alpha z+\beta z^{2}
$$

It follows that,

$$
\begin{aligned}
E\left[\omega_{T}\right]= & \int_{-\infty}^{\infty} n(z) \sigma_{B S}^{2}(z) T d z \\
= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-z^{2} / 2}\left(\sigma_{0}^{2}+\alpha z+\beta z^{2}\right) T d z \\
= & \left.\frac{\sigma_{0}^{2} T}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-z^{2} / 2} d z+\frac{\alpha T}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} z\right]^{0} z e^{z / 2} d z \\
& +\frac{\beta T}{\sqrt{2 \pi}} \int_{-\alpha}^{\infty} z^{2} e^{-z^{2} / 2} d z \\
= & \sigma_{0}^{2} T+\beta T
\end{aligned}
$$

It follows that the price of the variance sloap is given by

$$
E\left[\omega_{T}\right]=\sigma_{0}^{2} T+\beta T
$$

now consider the terms in

$$
\sigma_{B S}^{2}(z)=\sigma_{0}^{2}+\alpha z+\beta z^{2}
$$

$\sigma_{0}^{2}$ is the offset, $\alpha$ is the value of the first derivate, the skew, and $\beta$ the value of the second derivative which is the curvature. Thus the value of the swap only depends on the curvatue not the skew.

Digression: Poisson Proccess

A Porssion process is used to model model random queing events, such as the number people ariving at a store in a given time.
For example consider an interval $T$ divided into $n$ equal length subinteroals of length $t$, so trat

$$
T=n t
$$

Also, assume that only one event, such as one person arrichy within the subinteroal, can occur in the subinterual. Consider the following sequence of subintervals where red indicates the event occured.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-496.jpg?height=160&width=1041&top_left_y=1652&top_left_x=290)

Thus on 5 intervals the event
occured. If it is assumed that the events occur randomly with equal and independent probability, it follows that the average number of events that occur is given by

$$
\lambda=n p
$$

where $\lambda$ is the average number of events, $n$ the total number of events and $P$ is the probability that the event occurs. It follows trat

$$
P=\frac{\lambda}{n}
$$

Using the previous example of 5 events it is seen 5 events can occur in multiple ways. For example
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-497.jpg?height=162&width=1041&top_left_y=1795&top_left_x=390)

In general $k$ events can occur on $n$ intervals

$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}
$$

different ways. where $\binom{n}{k}$ is the binomial coefficient. The probability of a single realization of $k$ events is given by the probability $k$ events occuring and $n-k$ events not occurring That is,

$$
p^{k}(1-p)^{k}=\left(\frac{\lambda}{n}\right)^{k}\left(1-\frac{\lambda}{n}\right)^{n-k}
$$

Since there are ( $\hat{k}$ ) ways the $k$ events can occur on $n$ intervals it follows trat the probability of $k$ events can occur is given $b_{y}$

$$
P(k)=\binom{n}{k}\left(\frac{\lambda}{n}\right)^{k}\left(1-\frac{\lambda}{n}\right)^{n-k}
$$

The Poisson distribution is obtained by taking the limit $n \rightarrow \infty$ which is equivalent to the size of each interval approaching zero.
Now

$$
\begin{aligned}
& \binom{n}{k}\left(\frac{\lambda}{n}\right)^{k}\left(1-\frac{\lambda}{n}\right)^{n-k} \\
& =\frac{n!}{(n-k)!k!} \frac{\lambda^{k}}{n^{k}}\left(1-\frac{\lambda}{n}\right)^{n}\left(1-\frac{\lambda}{n}\right)^{k} \\
& =\frac{n!}{(n-k)!n^{k}} \frac{\lambda^{k}}{k!}\left(1-\frac{\lambda}{n}\right)^{n}\left(1-\frac{\lambda}{n}\right)^{k}
\end{aligned}
$$

For $n \gg 1$ for the first term

$$
\begin{aligned}
& \frac{n^{!}}{n^{k}(n-k)!}=\frac{n(n-1)(n-2) \cdots(n-k+1)}{n^{k}} \\
& \pi \frac{n^{k}+O\left(n^{k-1}\right)}{n^{k}}
\end{aligned}
$$

So,

$$
\lim _{n \rightarrow \infty} \frac{n!}{n^{k}(n-k)!}=1
$$

For the last term

$$
\lim _{n \rightarrow \infty}\left(1-\frac{\lambda}{n}\right)^{k}=1
$$

and

$$
\lim _{n \rightarrow \infty}\left(1-\frac{\lambda}{n}\right)^{n}=e^{-\lambda}
$$

Putting things together gives

$$
\begin{aligned}
P(k)=\lim _{n \rightarrow \infty} & \frac{n!}{(n-k)!n^{k}} \frac{\lambda^{k}}{k!}\left(1-\frac{\lambda}{n}\right)^{n}\left(1-\frac{\lambda}{n}\right)^{k} \\
= & \frac{\lambda^{k}}{k!} e^{-\lambda}
\end{aligned}
$$

Thus the Poisson distribution is given by

$$
P(K)=\frac{\lambda^{K}}{K!} e^{-\lambda}
$$

The mean is guen by

$$
\begin{aligned}
E[k] & =\sum_{k=0}^{\infty} k \frac{\lambda^{k}}{k!} e^{-\lambda}=\sum_{k=1}^{\infty} k \frac{\lambda^{k}}{k!} e^{-\lambda} \\
& =e^{-\lambda} \sum_{k=1}^{\infty} \frac{k \lambda^{k}}{k!} \\
& =e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k}}{(k-1)^{!}} \\
& =e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k+1}}{k!} \\
& =\lambda e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda}{k!} \\
& =\lambda e^{-\lambda} e^{\lambda} \\
& =\lambda \\
\Rightarrow E[k] & =\lambda
\end{aligned}
$$

The variance is given by

$$
\begin{aligned}
\operatorname{Var}(k) & =E\left[k^{2}\right]-E[k]^{2} \\
& =E\left[k^{2}\right]-\lambda^{2}
\end{aligned}
$$

Now

$$
\begin{aligned}
E\left[k^{2}\right] & =\sum_{k=0}^{\infty} \frac{k^{2} e^{-\lambda} \lambda^{k}}{k!}=\sum_{k=1}^{\infty} \frac{k^{2} e^{-\lambda} \lambda^{k}}{k!} \\
& =e^{-\lambda} \sum_{k=1}^{\infty} \frac{k \lambda^{k}}{(k-1)!} \\
& =e^{-\lambda} \sum_{k=0}^{\infty} \frac{(k+1) \lambda^{k+1}}{k!} \\
& =e^{-\lambda} \lambda \sum_{k=0}^{\infty} \frac{k \lambda^{k}}{k!}+\frac{\lambda^{k}}{k!} \\
& =e^{-\lambda} \lambda\left[e^{\lambda}+\sum_{k=0}^{\infty} \frac{k \lambda^{k}}{k!}\right]
\end{aligned}
$$

For the last torm the first tom in the sum is zero since $0!=1$

$$
\sum_{k=0}^{\infty} \frac{k \lambda^{k}}{k!}=\sum_{k=1}^{\infty} \frac{k \lambda^{k}}{k!}=e^{\lambda}
$$

Thus

$$
E\left[k^{2}\right]=2 \lambda
$$

and

$$
\begin{aligned}
\operatorname{var}(k) & =E\left[k^{2}\right]-E^{2}[k] \\
& =2 \lambda-\lambda \\
& =\lambda
\end{aligned}
$$

so

$$
\operatorname{var}(k)=\lambda
$$

Also, note the $P(k)$ is a PDF since

$$
\begin{aligned}
\sum_{k=0}^{\infty} P(k) & =\sum_{k=0}^{\infty} e^{-\lambda} \frac{\lambda^{k}}{k!}=e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^{k}}{k!} \\
& =e^{-\lambda} e^{\lambda}=1
\end{aligned}
$$

In summary for a Poisson process the probability of $k$ events occuring with rate $\lambda$ is given by

$$
P(k)=\frac{\lambda^{k} e^{-\lambda}}{k!}
$$

the mean and variane are given by

$$
E[k]=\lambda \quad \operatorname{Var}[k]=\lambda
$$

Arrival and Interarioal Times
Consider a sequerce of arrival times.

$$
t_{1}<t_{2}<t_{3}<\cdots<t_{n}
$$

and let $x_{1}$ denote the time elapsed on the first arival, $x_{2}$ the time elapsed between the first and second arrival, etc. The arrival times form a collection of disjont intervals. Ferthure assume that the interamioal
times denoted by $x_{1}, x_{2}, x_{n}$ are independent.
![](https://cdn.mathpix.com/cropped/2025_09_20_ae86e486843af6e629fcg-505.jpg?height=180&width=905&top_left_y=310&top_left_x=407)

Let $N(t)$ be a Poisson process with rate $\lambda$. Let $x$, be the time of the first arroval, then for $t>0$

$$
\begin{aligned}
P(x,>t) & =P(\text { no arrival in }(0, t]) \\
& =e^{-\lambda t}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
P\left(x_{1} \leqslant t\right) & =1-P\left(T_{1}>t\right) \\
& =1-e^{-\lambda t}
\end{aligned}
$$

Thus the waiting time for the first event has an exponential distribution.

Next consider s>0 and $t>0$ forming the disjoint intervals,

$$
(0, s] \text { and }(s, s+t]
$$

when computing the probability that $x_{2} \geqslant t$ it must be assumed that $x_{1}=s$ has occured, thus

$$
\begin{gathered}
P\left(x_{2}>t \mid x_{1}=s\right)=P\left(\text { no amual on }(s, s+t] \mid x_{1}=s\right) \\
=P(\text { no amual on }(s, s+t])
\end{gathered}
$$

since $X_{2}$ is independent of $T_{1}$, thus

$$
\begin{aligned}
& P\left(x_{2}>t \mid x_{1}=s\right)=e^{-\lambda t} \\
\Rightarrow & P\left(x_{2} \leqslant t\right)=1-e^{-\lambda t}
\end{aligned}
$$

It follows that the Poisson process is memoryless. This is called the Marka property.
The interarrival times have an exponental distribution and are independent. The PDF for the
interamival time is given by

$$
\begin{aligned}
P_{x}(t) & =\frac{\partial}{\partial t} P(x \leqslant t)=1-e^{-\lambda t} \\
& =\lambda e^{-\lambda t}
\end{aligned}
$$

The arrival times can be written as sums of interarrival times allowing computation of the arrival time distribution.

$$
\begin{aligned}
& T_{1}=x_{1} \\
& T_{2}=x_{1}+x_{2} \\
& T_{3}=x_{1}+x_{2}+x_{3} \\
& \vdots \\
& T_{n}=\sum_{i=1}^{n} x_{i}
\end{aligned}
$$

Since $x_{i} \sim \lambda e^{-\lambda t}$ it follows that trat $T_{k}$ has an Erlang distribution with PDF

$$
T_{k} \sim \frac{\lambda^{k} t^{k-1} e^{-\lambda t}}{(k-1)!}
$$

and the CDF is given

$$
\begin{aligned}
P\left(T_{k} \leqslant t\right) & =\int_{0}^{t} \frac{\lambda^{k} x^{k-1} e^{-\lambda x}}{(k-1)!} d x \\
& =\int_{0}^{t} \lambda \frac{(\lambda x)^{k-1}}{(k-1)!} e^{\lambda x} d x
\end{aligned}
$$

let $y=\lambda x \Rightarrow \frac{d y}{\lambda}=d x$
it follows that

$$
P\left(T_{k} \leqslant t\right)=\frac{1}{(k-1)} \int_{0}^{\lambda t} y^{k-1} e^{y} d y
$$

Recall that the incorplete gamma function is defined by

$$
\gamma(s, x)=\int_{0}^{x} t^{s-1} e^{-t} d t
$$

it follows that

$$
P\left(T_{k}(t)=\frac{Y(\lambda t, k)}{(k-1)!}\right.
$$

The mean and variance are easily computed using the assuption of independence of $X_{k}$. Recall that for an exponetral distribution the mean and varrance are given by

$$
E\left[x_{k}\right]=\frac{1}{\lambda} \quad \operatorname{Uar}\left[x_{k}\right]=\frac{1}{\lambda^{2}}
$$

It follows that

$$
\begin{aligned}
& E\left[T_{k}\right]=E\left[\sum_{n=1}^{k} X_{n}\right] \\
& =K E[X]=\frac{K}{\lambda} \\
& \operatorname{Uar}\left[T_{k}\right]=\operatorname{Uar}\left[\sum_{n=1}^{k} X_{n}\right] \\
& =E\left[\left(\sum_{n=1}^{k} X_{n}\right)^{2}\right]-E\left[\sum_{n=1}^{k} X_{n}\right]^{2} \\
& =E\left[\sum_{n=1}^{k} \sum_{m=1}^{k} X_{m} X_{n}\right]-\left(\sum_{n=1}^{k} E\left[X_{n}\right]\right)^{2}
\end{aligned}
$$

$$
\begin{aligned}
= & \sum_{n=1}^{k} \sum_{m=1}^{k} E\left[x_{m} x_{n}\right]-\left(\sum_{n=1}^{k} E\left[x_{n}\right]\right)^{2} \\
= & \sum_{n=1}^{k} E\left[x_{n}^{2}\right]+\sum_{n \neq m}^{k} E\left[x_{m}\right] E\left[x_{n}\right]- \\
& \left(\sum_{n=1}^{k} E\left[x_{n}\right]\right)^{2} \\
= & K E\left[x^{2}\right]+\left(x^{2}-K\right) E[x]^{2} \\
& -\bar{K}^{2} E[x]^{2} \\
= & K E\left[x^{2}\right]-K E[x]^{2} \\
= & K \operatorname{Var}(x) \\
= & \frac{K}{\lambda^{2}}
\end{aligned}
$$

Thus for interarrival times

$$
\begin{gathered}
\frac{T_{k}=\sum_{n=1}^{k} X_{k}}{\lambda e^{-\lambda t}} \quad \frac{P\left(X_{k} \leqslant t\right)=1-e^{-\lambda t}}{P_{x}(t)=\lambda} \\
E\left[X_{k}\right]=\frac{1}{\lambda} \quad \operatorname{Var}\left(X_{k}\right)=\frac{1}{\lambda^{2}}
\end{gathered}
$$

$$
\begin{aligned}
& P_{T}(k, t)=\frac{\lambda^{k} t^{k-1} e^{-\lambda t}}{(k-1)!} \\
& P\left(T_{k}(t)=\frac{Y(\lambda t, k)}{(k-1)!}\right. \\
& Y(s, x)=\int_{0}^{x} t^{s-1} e^{-t} d t \\
& E\left[T_{k}\right]=\frac{k}{\lambda} \quad \operatorname{Uar}\left(T_{k}\right)=\frac{k}{\lambda^{2}}
\end{aligned}
$$

## Compound Poisson Process

In a Poisson process each interval contains zero or one event. In a compound Poisson process each interval has an associated random variable that represents the value of the event. The random values are assumed to be independent and identically distributed and independent of the Poisson process.

For example this model can be used to model withdrawl from an ATM. In this example the customers accessing the ATM are modeled as a Poisson process and the amount of money withdrawn a random variable assigned to the event value.

Let $N(t)$ be a Poisson process with rate $\lambda$ and let $\lambda$ be
a random variable representing the value of the event.

The compound Poisson process is the random sum

$$
y(t)=\sum_{n=1}^{N(t)} x_{n}
$$

Expectations of Random Sums
To compute expectations of a compand Poisson process expectations of random sums must be evalued.

Consider the sum

$$
y=\sum_{m=1}^{N} x_{m}
$$

Here $N$ is a random variable and $x_{m}$ are identically distributed random variables $N$ and $X$ are assurned to be independent.
consider the conditional expectation given $N=n$

$$
\begin{aligned}
E[Y & \mid N=n]=E\left[\sum_{m=1}^{n} X_{m}\right] \\
& =\sum_{m=1}^{n} E\left[X_{m}\right] \\
& =n E[X]
\end{aligned}
$$

Now

$$
\begin{aligned}
E[y] & =E[E[y \mid N]] \\
& =E[N E[x]] \\
& =E[N] E[x]
\end{aligned}
$$

similarly the conditional variance of the sum is given by

$$
\begin{aligned}
& \operatorname{Var}[y \mid N=n]=\operatorname{Var}\left[\sum_{m=1}^{n} X_{m}\right] \\
& =\sum_{m=1}^{n} \operatorname{Uar}\left[X_{m}\right]=n \operatorname{Uar}[x]
\end{aligned}
$$

Now to compute the variance the law of total variance must be used. From the definition of variance

$$
\operatorname{Var}[x]=E\left[x^{2}\right]-E[x]^{2}
$$

For a conditional expectation using conditional probability,

$$
\operatorname{Var}[Y \mid N]=E\left[Y^{2} \mid N\right]-E[Y \mid N]^{2}
$$

Taking expectation gives

$$
\begin{aligned}
& E[\operatorname{Uar}(Y \mid N)]=E\left[E\left[Y^{2} \mid N\right]-E[Y \mid N]^{2}\right] \\
& \quad=E\left[E\left[Y^{2} \mid N\right]\right]-E\left[E[Y \mid N]^{2}\right]
\end{aligned}
$$

But

$$
E\left[Y^{2}\right]=E\left[E\left[Y^{2} \mid N\right]\right]
$$

50

$$
E[\operatorname{Var}(Y \mid N)]=E\left[Y^{2}\right]-E\left[E[Y \mid N]^{2}\right]
$$

Recall the definition of variance again

$$
\operatorname{Var}[x]=E\left[x^{2}\right]-E[x]^{2}
$$

This time let

$$
x=E[Y \mid N]
$$

so
$\operatorname{Var}[E[Y \mid N]]=E\left[E[Y \mid N]^{2}\right]-E[E[Y \mid N]]^{2}$
This time instead of taking expectation with respect to conditional probability the expectation is using the PDF for $N$

Now

$$
E[E[Y \mid N]]=E[Y]
$$

50
$\operatorname{var}[E[y \mid D]]=E\left[E[y \mid N]^{2}\right]-E[y]^{2}$

But the previous result obtained using the conditional probability is given by,

$$
\begin{aligned}
& E[\operatorname{Uar}(Y \mid N)]=E\left[Y^{2}\right]-E\left[E[Y \mid N]^{2}\right] \\
\Rightarrow & E\left[E[Y \mid N]^{2}\right]=E\left[Y^{2}\right]-E[\operatorname{Uar}[Y \mid N]]
\end{aligned}
$$

substituting into the previous expression gives

$$
\begin{aligned}
\operatorname{Uar}[E[Y \mid N]]= & E\left[Y^{2}\right]-E[Y]^{2} \\
& -E[\operatorname{Uar}[Y \mid N]] \\
\Rightarrow E\left[Y^{2}\right]-E[Y]^{2}= & \operatorname{Uar}[E[Y \mid N]] \\
& +E[\operatorname{Uar}[Y \mid N]]
\end{aligned}
$$

but

$$
\operatorname{var}[y]=E\left[y^{2}\right]-E[y]^{2}
$$

Thus

$$
\operatorname{Uar}[Y]=\operatorname{Uar}[E[Y \mid N]]+E[\operatorname{Uar}[Y \mid N]]
$$

Now the vorrance of the compand Poisson process can be computed. It is known that

$$
\operatorname{Var}[Y \mid N=n]=n \operatorname{Uar}[x]
$$

and

$$
E[Y \mid N=n]=n E[X]
$$

It follows that

$$
\begin{aligned}
\operatorname{Var}[y] & =\operatorname{Uar}[N E[x]]+E[N \operatorname{Var}[x]] \\
& =E[x]^{2} \operatorname{Uar}[N]+\operatorname{Var}[x] E[N]
\end{aligned}
$$

Thus for the random sum

$$
y=\sum_{m=1}^{N} x_{m}
$$

where the $x_{m}$ are identically distributed and $N$ and $X_{m}$ are independent, the mean and variarce are given by

$$
\begin{gathered}
E[Y]=E[N] E[X] \\
\operatorname{Var}[Y]=E[X]^{2} \operatorname{Var}[N]+\operatorname{Var}[X] E[N]
\end{gathered}
$$

Thus for the compound Poisson process

$$
y=\sum_{m=1}^{N} x_{m}
$$

where $N(t)$ be a Poisson process with rate $\lambda$

$$
E[0]=\operatorname{Var}[n]=\lambda T
$$

Thus

$$
\begin{gathered}
E[y]=\lambda T E[x] \\
\operatorname{Var}[y]=\lambda T E[x]^{2}+\lambda T \operatorname{Uar}[x]
\end{gathered}
$$

If $\mu=E[x]$ and $\sigma^{2}=\operatorname{Var}[x]$

$$
\begin{aligned}
& E[y]=\lambda T \mu \\
& \operatorname{Var}[y]=\lambda T \mu^{2}+\lambda T \sigma^{2} \\
&=\lambda T\left(\mu^{2}+\gamma^{2}\right) \\
& \Rightarrow \quad \frac{E[y]}{\operatorname{Uar}[y]}=\lambda T \mu \\
& \operatorname{UT}\left(\mu^{2}+\sigma^{2}\right)
\end{aligned}
$$

## The Effect of Jumps

Consider the compound Porsson process

$$
x_{T}=\sum_{n=1}^{N_{T}} y_{n}
$$

where $N_{T}$ is a Poisson process with rate $\lambda$, the $y_{n}$ are independent and dentically distributed and independent of $N_{T}$ and $X_{T}$ is the log spot price

$$
x_{T}=\ln \left(\frac{S_{T}}{F}\right)
$$

and $F$ is the forward price

$$
F=s_{0} e \int_{0}^{T} \mu d t
$$

Define the quadratic variation as

$$
\left\langle x_{T}\right\rangle=\sum_{n=1}^{N_{T}}\left|y_{n}\right|^{2}
$$

It follows that

$$
E\left[\left\langle x_{T}\right\rangle\right]=E\left[N_{T}\right] E\left[\left|y_{n}\right|^{2}\right]
$$

$$
E\left[N_{T}\right]=\lambda T
$$

and

$$
E\left[\left|y_{i}\right|^{2}\right]=\int_{0}^{A} y^{2} \mu(y) d y
$$

where $u(y)$ is a probability measure. It follows that

$$
E\left[\left\langle x_{T}\right\rangle\right]=\lambda T \int_{0}^{\infty} y^{2} \mu(y) d y
$$

also

$$
\begin{aligned}
E\left[x_{T}\right] & =E\left[N_{T}\right] E\left[y_{n}\right] \\
& =\lambda T \int_{0}^{\alpha} y \mu(y) d y
\end{aligned}
$$

To simplify notation in the following let

$$
E[y]=\int_{0}^{\infty} y \mu(y) d y \quad E\left[y^{2}\right]=\int_{0}^{\infty} y^{2} \mu(y) d y
$$

Recall that the variance of a compound Poisson process is given by

$$
\operatorname{Var}[y]=\lambda T E[x]^{2}+\lambda T \operatorname{Var}[x]
$$

Here

$$
y=x_{T} \quad \text { and } \quad x=y_{n}
$$

So

$$
\begin{aligned}
\operatorname{Uar}\left[x_{T}\right]= & \lambda T E[y]^{2}+\lambda T \operatorname{Uar}[y] \\
= & E\left[x_{T}^{2}\right]-E\left[x_{T}\right]^{2} \\
\Rightarrow E\left[x_{T}^{2}\right]= & \lambda T E[y]^{2}+E\left[x_{T}\right]^{2} \\
& +\lambda T \operatorname{Uar}[y]
\end{aligned}
$$

Now

$$
E\left[x_{T}\right]^{2}=(\lambda T)^{2} E[y]^{2}
$$

and

$$
\operatorname{Var}[y]=E\left[y^{2}\right]-E[y]^{2}
$$

so

$$
\begin{aligned}
E\left[x_{T}^{2}\right] & =\lambda T E[y]^{2}+(\lambda T)^{2} E[y]^{2} \\
& +\lambda T\left(E\left[y^{2}\right]-E[y]^{2}\right) \\
& =\lambda T E\left[y^{2}\right]+(\lambda T)^{2} E[y]^{2}
\end{aligned}
$$

Now

$$
\begin{aligned}
(\lambda T)^{2} E[y]^{2} & =(\lambda T E[y])^{2} \\
& =E\left[x_{T}\right]^{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[x_{T}^{2}\right]=\lambda T E\left[y^{2}\right]+E\left[x_{T}\right]^{2} \\
\Rightarrow & E\left[x_{T}^{2}\right]-E\left[x_{T}\right]^{2}=\lambda T E\left[y^{2}\right]
\end{aligned}
$$

But

$$
\operatorname{var}\left[x_{T}\right]=E\left[x_{T}^{2}\right]-E\left[x_{T}\right]^{2}
$$

50

$$
\lambda T E\left[y^{2}\right]=\operatorname{Var}\left[x_{T}\right]
$$

Recall that

$$
\begin{aligned}
E\left[\left\langle x_{T}\right\rangle\right] & =\lambda T \int_{0}^{\Delta} y^{2} \mu(y) d y \\
& =\lambda T E\left[y^{2}\right]
\end{aligned}
$$

Thus

$$
\operatorname{Var}\left[x_{T}\right]=E\left[\left\langle x_{T}\right\rangle\right]
$$

$$
E\left[\left\langle x_{T}\right\rangle\right]=\lambda T \int_{0}^{\infty} y^{2} \mu(y) d y
$$

Now recall that

$$
E\left[\log \left(\frac{S_{T}}{F}\right)\right]=-\int_{-\infty}^{0} p(k) d k-\int_{0}^{\infty} c(k) d k
$$

where

$$
\begin{array}{cc}
k=\ln \left(\frac{k}{F}\right) & F=s_{0} e \int_{0}^{T} u d t \\
c(k)=\frac{\tilde{C}\left(F e^{k}\right)}{F e^{k}} & p(k)=\frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}}
\end{array}
$$

Again recall that

$$
\begin{gathered}
E\left[g\left(S_{T}\right) \mid S_{t}\right]=g(F)+\int_{0}^{F} \tilde{P}(k) g^{\prime \prime}(k) d k \\
+\int_{F}^{\infty} \tilde{C}(k) g^{\prime \prime}(k) d k
\end{gathered}
$$

Next consider

$$
g\left(S_{T}\right)=\left[\log \left(\frac{S_{T}}{F}\right)\right]^{2}
$$

differentiating gives

$$
\begin{aligned}
g^{\prime}(k) & =2 \log \left(\frac{K}{F}\right) \frac{1}{K} \\
g^{\prime \prime}(K) & =\frac{2}{K}\left(\frac{1}{K}\right)-2 \log \left(\frac{K}{F}\right) \frac{1}{K^{2}} \\
& =\frac{2}{K^{2}}\left[1-\log \left(\frac{K}{F}\right)\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[\left\{\log \left(\frac{S_{T}}{F}\right)\right\}^{2}\right]=\left[\log \left(\frac{F}{F}\right)\right]^{2} \\
& +\int_{0}^{F} \tilde{D}(K) \frac{2}{K^{2}}\left[1-\log \left(\frac{K}{F}\right)\right] d K \\
& +\int_{F}^{\infty} \tilde{C}(K) \frac{2}{K^{2}}\left[1-\log \left(\frac{K}{F}\right)\right] d K \\
& =\int_{0}^{F} 2 \tilde{P}(K) d K+\int_{F}^{\infty} 2 \tilde{C}(K) d K \\
& -2 \int_{0}^{F} \log \left(\frac{K}{F}\right) \frac{1}{K^{2}} \tilde{P}(K) d K \\
& -2 \int_{0}^{F} \log \left(\frac{K}{F}\right) \frac{1}{K^{2}} \tilde{C}(K) d K
\end{aligned}
$$

let

$$
\begin{aligned}
k & =\log \left(\frac{k}{F}\right) \\
\Rightarrow d k & =\frac{1}{k} d k
\end{aligned}
$$

Then

$$
\begin{aligned}
& E\left[\left\{\log \left(\frac{S_{T}}{F}\right)\right\}^{2}\right]=2 \int_{-\infty}^{0} \frac{\tilde{P}(k)}{k} d k \\
& +2 \int_{0}^{\infty} \frac{\tilde{C}(k)}{k} d k-2 \int_{-\infty}^{0} k \frac{\tilde{P}(k)}{k} d k \\
& 2 \int_{0}^{\infty} k \frac{\tilde{C}(k)}{k} d k \\
& =2 \int_{-\infty}^{0} p(k) d k+2 \int_{0}^{\infty} c(k) d k \\
& -2 \int_{-\infty}^{0} k p(k) d k-2 \int_{0}^{\infty} k c(k) d k \\
& =2 \int_{-\infty}^{0}(1-k) p(k) d k \\
& +2 \int_{0}^{\infty}(1-k) c(k) d k
\end{aligned}
$$

The result in the book appears to assume that

$$
1-k x k
$$

This is reasonable since $|k|$ takes on all values between 0 and infinity and $P(k)$ will be nonzerd only for negative values of $k$ and increase as $k$ becomes more negative. Similarly, $c(k)$ is nonzero only for positive $k$ and increases as $k$ increases.

Making this assumption gives,

$$
\begin{aligned}
E\left[\left\{\log \left(\frac{S_{T}}{F}\right)\right\}^{2}\right] & = \\
& -2 \int_{-\alpha}^{0} k p(k) d k-2 \int_{0}^{\infty} k c(k) d k
\end{aligned}
$$

Since

$$
x_{T}=\log \left(\frac{S_{T}}{F}\right)
$$

it follows that,

$$
\begin{aligned}
& E\left[x_{T}\right]=E\left[\log \left(\frac{S_{T}}{F}\right)\right] \\
& E\left[x_{T}^{2}\right]=E\left[\left\{\log \left(\frac{S_{T}}{F}\right)\right\}^{2}\right]
\end{aligned}
$$

Thus $X_{T}$ represents a jump in the variance of the asset price and $X_{1}^{2}$ a jump in the variance of the variance.

$$
\begin{aligned}
& E\left[x_{T}\right]=-\int_{-\infty}^{0} p(k) d k-\int_{0}^{\infty} c(k) d k \\
& E\left[x_{T}^{2}\right]=-2 \int_{-\infty}^{0} k p(k) d k-2 \int_{0}^{\infty} k c(k) d k
\end{aligned}
$$

where

$$
\begin{gathered}
k=\ln \left(\frac{K}{F}\right) \\
C(k)=\frac{\tilde{C}\left(F e^{k}\right)}{F e^{k}} \quad p(k)=\frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}}
\end{gathered}
$$

In a jump-diffusion process the jump and diffusssion components are assumed independent Here the jump component has been determined. In a previous section the diffusion component was found to be
$E\left[\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t\right]=-2 E\left[\log \left(\frac{s_{T}}{F}\right)\right]$

$$
2\left\{\int_{-\infty}^{0} p(k) d k+\int_{0}^{\infty} c(k) d k\right\}
$$

50

$$
E\left[\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t\right]=-2 E\left[x_{T}\right]
$$

since

$$
x_{T}=\log \left(\frac{S_{T}}{F}\right)
$$

Also, since

$$
\left\langle x_{T}\right\rangle=\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t
$$

It follows that

$$
E\left[\int_{0}^{T} \sigma^{2}\left(s_{t}\right) d t\right]=E\left[\left\langle X_{T}\right\rangle\right]=-2 E\left[X_{T}\right]
$$

This should be compared with the result obtained for the jump process,

$$
\begin{aligned}
\operatorname{Var}\left[x_{T}\right] & =E\left[\left\langle x_{T}\right\rangle\right] \\
& =E\left[x_{T}^{2}\right]-E\left[x_{T}\right]^{2}
\end{aligned}
$$

In practice it is not known which process operates. Since two methods are available to compute $E\left[\left\langle X_{T}\right\rangle\right]$ a judgement about the impact of each process. This can be accomplished by computing the difference a chorce in the underlying process makes.

Recall that the characteristic function is defined by

$$
\Phi_{T}(u)=E\left[e^{i x_{T} u}\right]
$$

it follows that

$$
\frac{\partial \Phi}{\partial u}=E\left[i x_{T} e^{i x_{T} u}\right]
$$

thus

$$
\begin{aligned}
-\left.i \frac{\partial \Phi_{T}}{\partial u}\right|_{u=0} & =E\left[X_{T}\right] \\
& =E\left[\ln \left(\frac{S_{T}}{F}\right)\right]
\end{aligned}
$$

Recall the Le'oy-Khintchine representation of the characteristic function

$$
\begin{aligned}
\Phi_{T}(u)= & \exp \left\{i \omega \omega T-\frac{1}{2} u^{2} s^{2} T\right. \\
& \left.+\lambda T \int_{0}^{T}\left(e^{i u s}-1\right) \mu(s) d s\right\}
\end{aligned}
$$

with $w$ determined by the condition

$$
\Phi_{T}(-i)=E\left[e^{x_{T}}\right]=1
$$

it follows that

$$
\begin{aligned}
\Phi_{T}(-i)= & \exp \left\{\omega T+\frac{1}{\partial} \sigma^{2} T\right. \\
& \left.+\lambda T \int_{0}^{T}\left(e^{s}-1\right) \mu(s) d s\right\} \\
= & 1 \\
\Rightarrow & \omega T+\frac{1}{\partial} \sigma^{2} T+\lambda T \int_{0}^{T}\left(e^{s}-1\right) \mu(s) d s \\
= & 0 \\
\Rightarrow & \omega=-\frac{1}{2} \sigma^{2}-\lambda \int_{0}^{T}\left(e^{s}-1\right) \mu(s) d s
\end{aligned}
$$

Thus the argument of the exponentacl becomes

$$
\begin{aligned}
& \angle U \omega T-\frac{1}{2} U^{2} \sigma^{2} T-\lambda T \int_{0}^{T}\left(e^{i u s}-1\right) \mu(s) d s \\
& =i U T\left[-\frac{1}{2} \sigma^{2}-\lambda \int_{0}^{T}\left(e^{s}-1\right) \mu(s) d s\right] \\
& -\frac{1}{2} u^{2} \sigma^{2} T+\lambda T \int_{0}^{T}\left(e^{i u s}-1\right) \mu(s) d s
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{-i u \sigma^{2} T-\lambda i u T \int_{0}^{T}\left(e^{s}-1\right) \mu(s) d s}{} \\
& -\frac{u^{2} \sigma^{2} T}{2}+\lambda T \int_{0}^{T}\left(e^{i u s}-1\right) \mu(s) d s \\
= & -u(u+i) \frac{\sigma^{2} T}{2}+\lambda T \int_{0}^{T}\left(e^{i u s}-i u e^{s}\right. \\
& +i u-1) \mu(s) d s
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\Phi_{T}(u) & =\exp \left\{-u(u+i) \frac{\sigma^{2} T}{2}\right. \\
& \left.+\lambda T \int_{0}^{T}\left(e^{i u s}-i u e^{s}+i u-1\right) \mu(s) d s\right\}
\end{aligned}
$$

The first term represents the contribution from the continuoles prosses and the second the contribution from the jump process. Let

$$
\begin{gathered}
\Phi_{T}^{c}(u)=\exp \left\{-u(u+i) \frac{\sigma^{2} T}{2}\right\} \\
\Phi_{T}^{J}(u)=\exp \left\{\lambda T \int_{0}^{T}\left(e^{i u s}-i u e^{s}+i u-1\right) \mu(s) d s\right\}
\end{gathered}
$$

Thus

$$
\Phi_{T}(u)=\Phi_{T}^{c}(u) \Phi_{T}^{J}(u)
$$

For the jump component

$$
-\left.i \frac{\partial \Phi_{T}^{J}}{\partial u}\right|_{u=0}=E\left[X_{T}\right]
$$

so

$$
\begin{aligned}
& \frac{\partial \Phi_{+}^{J}}{\partial u}=\left\{\lambda T \int_{0}^{T}\left(i s e^{i u s}-i e^{s}+i\right) \mu(s) d s\right\} \\
& \exp \left\{\lambda T \int_{0}^{T}\left(e^{i u s}-i u e^{s}+i u-1\right) \mu(s) d s\right\}
\end{aligned}
$$

so,

$$
\begin{aligned}
-\left.i \frac{\partial \Phi_{I}^{J}}{\partial u}\right|_{u=0} & =-i\left\{\lambda T \int_{0}^{T}\left(i s-i e^{s}+i\right) \mu(s) d s\right\} \\
& =\lambda T \int_{0}^{T}\left(s-e^{s}+1\right) \mu(s) d s
\end{aligned}
$$

and for the continous component

$$
\frac{\partial \Phi^{c}}{\partial u}=-\frac{\sigma^{2} T}{2}(2 u+i) \exp \left\{-u(u+i) \frac{\sigma^{2} T}{2}\right\}
$$

It follows that

$$
\begin{aligned}
-\left.i \frac{\partial \Phi_{T}^{c}}{\partial u}\right|_{u} & =E\left[X_{T}\right] \\
& =-i\left(-\frac{\delta^{2} T i}{2}\right)=\frac{\delta^{2} T}{2}
\end{aligned}
$$

Now it was shown that the continudes component satisfies,

$$
E\left[\left\langle x_{T}\right\rangle\right]=-2 E\left[x_{T}\right]
$$

## Where

$$
E\left[\left\langle x_{T}\right\rangle\right]=E\left[\int_{0}^{\top} \sigma^{2}(t) d t\right]
$$

$E\left[\left\langle x_{T}\right\rangle\right]$ is the expected total realized variance and it is considered the fair value of the variance swap. For the conticus case the fair value of the option is equal to twice the expectation which is given by the expectation of $\log ^{S T / F}$, which is related to the integral of over European option strike prices. This expression is called the "log strip".
For the jump model this relation was shown not to be true, namely,

$$
E\left[\left\langle x_{T}\right\rangle\right]=E\left[x_{T}^{2}\right]-E\left[x_{T}\right]^{2}
$$

where

$$
E\left[\left\langle x^{J}\right\rangle_{T}\right]=\lambda T \int_{0}^{T} y^{2} \mu(y) d y
$$

For this case the variance swap fair value is not equal to the
log-stripe. It was just shown that

$$
E\left[x_{T}^{\top}\right]=\lambda T \int_{0}^{T}\left(y \cdot e^{y}+1\right) \mu(y) d y
$$

Thus the difference between the fair value and the log stripe is siven by.

$$
\begin{aligned}
& E\left[\left\langle x_{T}\right\rangle\right]+2 E\left[x_{T}\right]=\lambda T \int_{0}^{T} y^{2} \mu(y) d y+ \\
& \partial \lambda T \int_{0}^{T}\left(y-e^{y}+1\right) \mu(y) d y \\
& =2 \lambda T \int_{0}^{T}\left(1+y+\frac{1}{\partial} y^{2}-e^{y}\right) \mu(y) d y \\
& \Rightarrow E\left[\left\langle x_{T}\right\rangle\right]+2 E\left[x_{T}\right] \\
& =2 \lambda T \int_{0}^{T}\left(1+y+\frac{1}{\partial} y^{2}-e^{y}\right) \mu(y) d y
\end{aligned}
$$

Dote that the first three terms in the integral are the first three torms of the Taylor series expansion,

$$
e^{y}=1+y+\frac{1}{2} y^{2}+O\left(y^{3}\right)
$$

Thus to lowest order the effect of jumps is the cube of the jump size

Recall the Merton model, which assumes a lognormal distribution for the jump size,

$$
\mu(y)=\frac{1}{\sqrt{2 \pi \delta^{2}}} \exp \left\{\frac{(\ln y-\alpha)^{2}}{2 \delta^{2}}\right\}
$$

Consider the integral

$$
\int_{0}^{T}\left(1+y+\frac{1}{d} y^{2}-e^{y}\right) \mu(y) d y
$$

the time dependence of $y(t)$ is implied. Naw $y(t)$ can vary over all positive values,

$$
\int_{0}^{T}\left(1+y+\frac{1}{2} y^{2}-e^{y}\right) \mu(y) d y
$$

$$
\begin{aligned}
= & \int_{-\infty}^{\infty} \mu(y) d y+\int_{-\infty}^{\infty} y u(y) d y+\int_{-\infty}^{\infty} \frac{b}{\partial y^{2}} u(y) d y \\
& -\int_{-\infty}^{\infty} e^{y} \mu(y) d y
\end{aligned}
$$

For the last inlegral

$$
\begin{aligned}
& \int_{-\alpha}^{\infty} e^{y} \mu(y) d y=\frac{1}{2 \pi \delta^{2}} \int_{-\alpha}^{\infty} e^{y} e^{-(y-\alpha)^{2} / \partial \delta^{2}} d y \\
& =\frac{1}{\sqrt{2 \pi \delta^{2}}} \int_{-\alpha}^{\infty} \exp \left\{y^{-(y-\alpha)^{2}} \frac{\partial}{\partial \delta^{2}}\right\} d y
\end{aligned}
$$

make the change of variables

$$
x=\frac{y-\alpha}{\delta} \Rightarrow y=\alpha+\delta x
$$

and

$$
d y=\delta d x
$$

then

$$
\begin{aligned}
& \int_{-\alpha}^{\infty} e^{y} \mu(y) d y=\frac{1}{\sqrt{2 \pi}} \int_{-\alpha}^{\infty} e^{\alpha+\delta x} e^{-x^{2} / 2} d x \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\alpha}^{\infty} e^{\alpha+\delta x-\frac{1}{2 x^{2}}} d x
\end{aligned}
$$

Consider the exponential argument

$$
\begin{aligned}
& \alpha+\delta x-\frac{1}{2} x^{2}=-\frac{1}{2}\left(-2 \alpha-2 \delta x+x^{2}\right) \\
& =\alpha-\frac{1}{2}\left(-2 \delta x+x^{2}\right) \\
& =\alpha-\frac{1}{2}\left(\delta^{2}-\delta^{2}-2 \delta x+x^{2}\right) \\
& =\alpha+\frac{\delta^{2}}{2}-\frac{1}{2}\left(\delta^{2}-2 \delta x+x^{2}\right) \\
& =\alpha+\frac{\delta^{2}}{2}-\frac{1}{2}\left(x-\delta^{2}\right)
\end{aligned}
$$

so

$$
\begin{aligned}
& \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{\alpha+\delta x-\frac{1}{2} x^{2}} d x \\
& \quad=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\alpha} e^{\alpha+\delta^{2} / 2} e^{-\left(x-\delta^{2}\right) / 2} d x \\
& \quad=e^{\alpha+\delta^{2} / 2}
\end{aligned}
$$

Putting things together gives

$$
\begin{aligned}
& \int_{0}^{T}\left(1+y+\frac{1}{2} y^{2}-e^{y}\right) \mu(y) d y \\
& =1+\alpha+\frac{\delta^{2}}{2}-\int_{-\infty}^{\infty} e^{y} \mu(y) d y \\
& =1+\alpha+\frac{\delta^{2}}{2}-e^{\alpha+\delta^{2} / 2}
\end{aligned}
$$

Next consider

$$
\int_{-\infty}^{\infty} \frac{1}{\partial} y^{2} \mu(y) d y=\int_{-\infty}^{\infty} \frac{1}{2} y^{2} \exp \left\{y^{-} \frac{(y-\alpha)^{2}}{\partial \delta^{2}}\right\} d y
$$

making the same change of variables

$$
\begin{aligned}
x= & \frac{y-\alpha}{\delta} \Rightarrow y=\alpha+\delta x \\
& d y=\delta d x \\
\frac{1}{2 \pi \delta^{2}} & \int_{-\infty}^{\infty} \frac{1}{2} y^{2} \exp \left\{\frac{(y-\alpha)^{2}}{2 \delta^{2}}\right\} d y \\
= & \frac{1}{2 \sqrt{2 \pi \delta^{2}}} \int_{-\infty}^{\infty}(\alpha+\delta x)^{2} e^{-x^{2} / 2} \delta d x \\
= & \frac{1}{2 \sqrt{2 \pi}} \int_{-\infty}^{\infty}\left(\alpha^{2}+2 \delta x+\delta^{2} x^{2}\right) e^{-x^{2} / 2} d x \\
= & \frac{1}{2}\left(\alpha^{2}+\delta^{2}\right)
\end{aligned}
$$

and for the first two integrals

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \mu(y) d y=1 \\
& \int_{-\infty}^{\infty} y \mu(y) d y=\alpha
\end{aligned}
$$

Putting things together

$$
\begin{aligned}
& E\left[\left\langle x_{1}\right\rangle\right]+2 E\left[x_{T}\right] \\
& =2 \lambda T\left[1+\alpha+\frac{1}{2}\left(\alpha^{2}+\delta^{2}\right)-e^{\alpha+\delta^{2} / 2}\right] \\
& =\lambda T\left(\delta^{2}+\alpha^{2}\right)+2 \lambda T\left(1+\alpha-e^{\alpha+\delta^{2} / 2}\right) \\
& \Rightarrow E\left[\left\langle x_{1}\right\rangle\right]+2 E\left[x_{1}\right] \\
& =\lambda T\left(\alpha^{2}+\delta^{2}\right)+2 \lambda T\left(1+\alpha-e^{\alpha+\delta^{2} / 2}\right)
\end{aligned}
$$

It has been shown by researchers
that the log-strip price differs from fair value price with about a 190 error.

## Valuing Uolatility Derivatives

Recall that for any twree differentable function of the asset price,

$$
\begin{aligned}
E\left[g\left(S_{T}\right)\right]=g(F) & +\int_{0}^{F} \hat{P}(K, T) g^{\prime \prime}(K) d K \\
& +\int_{F}^{\infty} \tilde{C}(K, T) g^{\prime \prime}(K) d K
\end{aligned}
$$

where $\tilde{C}$ and $P$ represent undiscounted call and put prices respectively and $F$ is the forward price defined by

$$
F=s_{0} e^{\int_{0}^{\top} \mu(t) d t}
$$

Let $g\left(S_{T}\right)=S_{T}^{P}$ then the replicating portfalio for the power-payoff is obtained, so,

$$
g^{\prime}\left(s_{T}\right)=p s_{T}^{p-1} \quad g^{\prime \prime}\left(s_{T}\right)=p(p-1) s_{T}^{p-2}
$$

It follows that

$$
\begin{aligned}
E\left[S_{T}^{P}\right]=F^{P} & +p(p-1) \int_{0}^{F} \tilde{P}(K, T) K^{P-2} d K \\
& +p(p-1) \int_{F}^{\infty} \tilde{C}(K, T) K^{P-2} d K
\end{aligned}
$$

changing variables to the log-strike gives,

$$
\begin{aligned}
& k=\ln \left(\frac{K}{F}\right) \Rightarrow e^{k}=\frac{K}{F} \\
& d k=\frac{d K}{K} \Rightarrow K d k=d K
\end{aligned}
$$

So,

$$
\begin{aligned}
E\left[S_{T}^{P}\right]= & F^{P}+p(p-1) \int_{-\infty}^{0} \tilde{P}(K, T) K^{P-1} d k \\
& +p(p-1) \int_{0}^{\infty} \tilde{C}(K, T) K^{P-1} d k
\end{aligned}
$$

Recall,

$$
\hat{p}(k)=\frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}} \quad \hat{c}(k)=\frac{\tilde{C}\left(F e^{k}\right)}{F e^{k}}
$$

It follows that

$$
\begin{aligned}
E\left[S^{P}\right]= & F^{P}+p(p-1) \int_{-\infty}^{0} \hat{P}(k) F e^{k} k^{P-1} d k \\
& +p(p-1) \int_{0}^{\infty} \hat{c}(k) F e^{k} k^{P-1} d k \\
= & F^{P}+p(p-1) \int_{-\infty}^{0} \hat{P}(k) F^{P} e^{k}\left(\frac{k}{F}\right)^{P-1} d k \\
& +p(p-1) \int_{0}^{\infty} \hat{c}(k) F^{P} e^{k}\left(\frac{k}{F}\right)^{P-1} d k \\
= & F^{P}\left[1+p(p-1) \int_{-\infty}^{0} \hat{P}(k) e^{k}\left(e^{k}\right)^{P-1} d k\right. \\
& \left.+p(p-1) \int_{0}^{\infty} \hat{c}(k) e^{k}\left(e^{k}\right)^{P-1} d k\right] \\
= & F^{P}\left[1+p(p-1) \int_{-\infty}^{0} \hat{P}(k) e^{P k} d k\right. \\
& \left.+p(p-1) \int_{0}^{\infty} \hat{c}(k) e^{P k} d k\right]
\end{aligned}
$$

Recall,

$$
\begin{aligned}
& P(K)=(K-F)^{+} \\
& C(K)=(F-K)^{+}
\end{aligned}
$$

so.

$$
\begin{aligned}
\hat{p}(k)=\frac{\tilde{P}\left(F e^{k}\right)}{F e^{k}} & =\frac{\left(F e^{k}-F\right)^{+}}{F e^{k}} \\
& =\left(1-e^{-k}\right)^{+} \\
\hat{c}(-k)=\frac{\tilde{c}\left(F e^{-k}\right)}{F e^{-k}} & =\frac{\left(F-F e^{-k}\right)^{+}}{F e^{-k}} \\
& =\left(e^{k}-1\right)^{+}
\end{aligned}
$$

and

$$
\begin{aligned}
e^{-k} \hat{c}(-k) & =e^{-k}\left(e^{-k}-1\right)^{+} \\
& =\left(1-e^{-k}\right)^{+} \\
& =\hat{p}(k)
\end{aligned}
$$

Thus

$$
\hat{p}(k)=e^{-k} \hat{c}(-k)
$$

which is equivalent to put-call parity.
It follows that

$$
\begin{array}{r}
E\left[S_{T}^{P}\right]=F^{P}\left[1+p(p-1) \int_{-\infty}^{0} \hat{P}(k) e^{p k} d k\right. \\
\left.+p(p-1) \int_{0}^{\infty} \hat{C}(k) e^{p k} d k\right] \\
=F^{P}\left[1+p(p-1) \int_{-\infty}^{0} e^{-k} \hat{C}(k) e^{p k} d k\right. \\
\left.+p(p-1) \int_{0}^{\infty} \hat{C}(k) e^{p k} d k\right] \\
=F^{P}\left[1+p(p-1) \int_{0}^{\infty} e^{k} \hat{C}(k) e^{-p k} d k\right. \\
\left.+p(p-1) \int_{0}^{\infty} \hat{C}(k) e^{p k} d k\right] \\
=F^{P}\left[1+p(p-1) \int_{0}^{\infty} \hat{C}(k)\left(e^{-(p-1) k}+e^{p k}\right) d k\right] \\
=F^{P}\left[1+p(p-1) \int_{0}^{\infty} \hat{C}(k) e^{\frac{1}{\partial k}}\left(e^{-(p-1) k-\frac{1}{\partial k}}\right.\right. \\
\left.\left.+e^{p k-1} d k\right) d k\right] \\
=F^{P}\left[1+p(p-1) \int_{0}^{\infty} \hat{C}(k) e^{\frac{1}{\partial k}}\left(e^{-\left(p-\frac{1}{2}\right) k}\right.\right. \\
\left.\left.e^{(p-1) k}\right) d k\right]
\end{array}
$$

but

$$
\cosh x=\frac{1}{2}\left(e^{x}+e^{-x}\right)
$$

so

$$
\begin{aligned}
& E\left[s_{T}^{p}\right]=F^{p}\left\{1+2 p(p-1) \int_{0}^{\infty} e^{\frac{1}{\partial} k} \hat{c}(k)\right. \\
&\left.\cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k\right\}
\end{aligned}
$$

## The Laplace Transform of Quadradic Variation under Zero Correlation

It can be shown that conditional on a particular realization of the volatility process (volatility path) and under a zero correlation between asset and probability, assuption that

$$
x_{T}=\int_{0}^{T} \sigma_{t} d \omega_{t}-\frac{1}{2}\langle x\rangle_{T}
$$

see Carr and Lee (Robust Replication of volatility Derivatives).
This relation can be understood by considering the SDE for the log asset price. From Itô's formula it can be shown trat.

$$
d \ln s_{t}=\frac{1}{s_{t}} d s_{t}-\frac{s_{t}}{2} d t
$$

If $S_{t}$ is assumed that

$$
d s_{t}=\sigma_{t} s_{t} d \omega_{t}
$$

Note that $d s_{t}$ does not depend on changes in sigma but on the known value $\sigma_{t}$. This is the assumption that is stated as "movements in asset price are irdependent of movements volatility".
It follows that

$$
d \ln S_{t}=\sigma_{t} d \omega_{t}-\frac{\sigma_{t}^{2}}{2} d t
$$

Integrating gives

$$
\begin{aligned}
\int_{0}^{T} d \ln S_{t} & =\int_{0}^{T} \sigma_{t} d \omega_{t}-\frac{1}{\partial} \int_{0}^{T} \sigma_{t}^{2} d t \\
& =\ln S_{T}-\ln S_{0} \\
& =\ln \frac{S_{I}}{S_{0}}
\end{aligned}
$$

but

$$
x_{T}=\ln \frac{s_{I}}{s_{0}}
$$

and

$$
\left\langle x_{T}\right\rangle=\int_{0}^{T} \sigma_{t}^{2} d t
$$

50

$$
X_{T}=\int_{0}^{T} \sigma_{t} d \omega_{t}-\frac{1}{2}\left\langle X_{T}\right\rangle
$$

Since $d \omega_{t} \sim \operatorname{Normal}(0, d t)$ it follows that $X_{T}$ is normally distributed with mean $-\frac{1}{\partial}\left\langle x_{T}\right\rangle$ and vanance $\left\langle x_{T}\right\rangle$.

Now consider $E\left[e^{P X_{T}}\right]$ since $X_{T}$ and $\sigma_{T}$ are assumed independent the PDF has the form

$$
p\left(x_{T}, \sigma_{t}\right)=p\left(x_{T}\right) p\left(\sigma_{t}\right)
$$

but

$$
x_{T} \sim \frac{1}{\sqrt{2 \pi\left\langle x_{T}\right\rangle}} \int_{-\infty}^{\infty} e^{-\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2} / 2\left\langle x_{T}\right\rangle}
$$

It follows that

$$
\begin{aligned}
E\left[e^{P x_{T}}\right] & =\int_{0}^{\infty} \int_{-\infty}^{\infty} e^{P x_{T}} p\left(x_{T}\right) p\left(\sigma_{t}\right) d x_{T} d \sigma_{t} \\
& =\int_{0}^{\infty}\left[\int_{-\infty}^{\infty} e^{P x_{T}} p\left(x_{T}\right) d x_{T}\right] p\left(\sigma_{t}\right) d \sigma_{t}
\end{aligned}
$$

consider the integral

$$
\begin{aligned}
& \int_{-\infty}^{\infty} e^{P x_{T}} P\left(x_{T}\right) d x_{T} \\
& =\frac{1}{\sqrt{2 \pi}\left\langle x_{T}\right\rangle} \int_{-\infty}^{\infty} e^{P x_{T}} e^{-\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2} / \partial\left\langle x_{T}\right\rangle} d x_{T} \\
& =\frac{1}{\sqrt{2 \pi\left\langle x_{T}\right\rangle}} \int_{-\infty}^{\infty} e^{P x_{T}-\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2} / 2\left\langle x_{T}\right\rangle} d x_{T}
\end{aligned}
$$

consder the exponential argument

$$
\begin{aligned}
& P x_{T}-\frac{\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2}}{2\left\langle x_{T}\right\rangle} \\
= & \frac{2 P x_{T}\left\langle x_{T}\right\rangle-\left(x_{T}^{2}+x_{T}\left\langle x_{T}\right\rangle+t_{T}\left\langle x_{T}\right\rangle^{2}\right)}{2\left\langle x_{T}\right\rangle}
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{2\left\langle x_{T}\right\rangle}\left[\left(x_{T}^{2}+x_{T}\left\langle x_{T}\right\rangle+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}\right)-2 p x_{T}\left\langle x_{T}\right\rangle\right] \\
& =\frac{-1}{2\left\langle x_{T}\right\rangle}\left[x_{T}^{2}+x_{T}\left(\left\langle x_{T}\right\rangle-2 p\left\langle x_{T}\right\rangle\right)+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}\right] \\
& =\frac{-1}{2\left\langle x_{T}\right\rangle}\left[x_{T}^{2}+x_{T}\left\langle x_{T}\right\rangle(1-2 p)+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}\right]
\end{aligned}
$$

Complete the square by adding and subtracting,

$$
\frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2}
$$

so for the numerator

$$
\begin{aligned}
x_{T}^{2} & +x_{T}\left\langle x_{T}\right\rangle(1-2 p)+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2} \\
- & \frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2} \\
= & x_{T}^{2}+x_{T}\left\langle x_{T}\right\rangle(1-2 p)+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2} \\
& +\frac{1}{4}\left\langle x_{T}\right\rangle^{2}-\frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2}
\end{aligned}
$$

$$
\begin{aligned}
= & {\left[x_{T}+\frac{1}{2}\left\langle x_{T} x_{1}-2 p\right\rangle\right]^{2}+\frac{1}{4}\left\langle x_{T}\right\rangle^{2} } \\
& -\frac{1}{4}\left\langle x_{T}\right\rangle^{2}(1-2 p)^{2} \\
= & {\left[x_{T}+\frac{1}{2}\left\langle x_{T} x(1-2 p)\right]^{2}+\frac{1}{4}\left\langle x_{T}\right\rangle^{2}\right.} \\
& -\frac{1}{4}\left\langle x_{T}\right\rangle^{2}\left(x-4 p+4 p^{2}\right) \\
= & {\left[x_{T}+\frac{1}{2}\left\langle x_{T} x(1-2 p)\right]^{2}-\left\langle x_{T}\right\rangle^{2}\left(p^{2}-p\right)\right.}
\end{aligned}
$$

putting the exponential argument together

$$
\begin{aligned}
p x_{T}-\frac{\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2}}{2\left\langle x_{T}\right\rangle}= & \frac{-1}{2\left\langle x_{T}\right\rangle}\left[x_{T}+\frac{1}{2}\left\langle x_{T}\right)(1-2 p)\right]^{2} \\
& +\frac{\left\langle x_{T}\right\rangle}{2}\left(p^{2}-p\right)
\end{aligned}
$$

so the integral becomes

$$
\begin{aligned}
& \int_{-\infty}^{\infty} e^{P x_{T}} P\left(x_{T}\right) d x_{T} \\
& \quad=\frac{1}{\sqrt{2 \pi\left\langle x_{T}\right\rangle}} \int_{-\infty}^{\infty} e^{P x_{T}-\left(x_{T}+\frac{1}{2}\left\langle x_{T}\right\rangle\right)^{2} / 2\left\langle x_{T}\right\rangle} d x_{T}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\sqrt{2 \pi\left\langle x_{T}\right\rangle}} \int_{-\Delta}^{\infty} e^{\frac{\left(x_{T}\right)}{2}\left(p^{2} \cdot p\right)} \\
& e^{\frac{-1}{\left.2 x_{T}\right\rangle}\left[x_{T}-\frac{1}{2}\left\langle x_{T}\right\rangle(1-2 p)\right]^{2}} d x_{T} \\
& \left.=e^{\left\langle x_{T}\right\rangle\left(p^{2}-p\right)} \frac{1}{\sqrt{2 \pi\left\langle x_{T}\right\rangle}}\right\rangle 1 \\
& \quad \int_{-\infty}^{\infty} e^{-\frac{1}{\left.2 x_{T}\right\rangle}\left[x_{T}-\frac{1}{2}\left\langle x_{T}\right\rangle(1-2 p)\right]^{2}} d x_{T} \\
& =e^{\left\langle x_{T}\right\rangle}\left(p^{2}-p\right)
\end{aligned}
$$

Finally

$$
\begin{aligned}
E\left[e^{P x_{T}}\right] & =\int_{0}^{\infty}\left[\int_{-\infty}^{\infty} e^{P x_{T}} p\left(x_{T}\right) d x_{T}\right] p\left(\sigma_{t}\right) d \sigma_{t} \\
& =\int_{0}^{\infty} e^{\left\langle\frac{x_{T}}{\partial}\left(p^{2}-p\right)\right.} p\left(\sigma_{t}\right) d \sigma_{t} \\
& =E\left[e^{\left(x_{T}\right)\left(p^{2}-p\right)}\right]
\end{aligned}
$$

## Thus

$$
E\left[e^{p x_{T}}\right]=E\left[e^{\left\langle x_{T}\right\rangle\left(p^{2}-p\right)}\right]
$$

let $\lambda=\frac{1}{2}\left(p^{2}-p\right)$ then

$$
E\left[e^{P x_{T}}\right]=E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]
$$

solving the $\lambda$ equation for $P$ gives

$$
\begin{aligned}
& 2 \lambda=p^{2}-p \\
\Rightarrow \quad & p^{2}-p-2 \lambda=0
\end{aligned}
$$

The general solution of a quodratic equation

$$
\begin{aligned}
& a x^{2}+b x+c=0 \\
& x=\frac{-b \pm \sqrt{b^{2} \cdot 4 c c}}{2 a}
\end{aligned}
$$

Here $a=1, b=-1$ and $c=-2 \lambda$. It follows that

$$
\begin{aligned}
p & =\frac{1 \pm \sqrt{1+8 \lambda}}{2} \\
& =\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}
\end{aligned}
$$

Trues

$$
P=\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}
$$

Now it was previously shown that,

$$
\begin{aligned}
& E\left[S_{T}^{P}\right]=F^{P}\left\{1+2 p(p-1) \int_{0}^{\infty} e^{\frac{1}{2} k} \hat{c}(k)\right. \\
&\left.\cosh \left[\left(p-\frac{1}{2}\right) k\right] d k\right\} \\
& \Rightarrow \quad E\left[\left(\frac{S_{T}}{F}\right)^{P}\right]=1+2 p(p-1) \int_{0}^{\infty} e^{\frac{1}{2} k} \hat{c}(k) \\
& \cosh \left[\left(p-\frac{1}{2}\right) k\right] d k
\end{aligned}
$$

and it was just shown that

$$
\begin{gathered}
E\left[e^{P x_{T}}\right]=E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right] \\
P(\lambda)=\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}
\end{gathered}
$$

noting that

$$
\begin{aligned}
e^{P x_{T}} & =\left(e^{x_{T}}\right)^{P}=\left(e^{\ln \frac{S_{F}}{F}}\right)^{D} \\
& =\left(\frac{S_{I}}{F}\right)^{P}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]=E\left[e^{p x_{T}}\right]=E\left[\left(\frac{S_{T}}{F}\right)^{p}\right] \\
& =1+2 p(\lambda)(p(\lambda)-1) \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
& \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{aligned}
$$

but

$$
\begin{gathered}
p(\lambda)(p(\lambda)-1)=\left(\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}\right) \\
\left(\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}-1\right)
\end{gathered}
$$

$$
\begin{gathered}
=\left(\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}\right)\left(-\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}\right) \\
=-\frac{1}{4} \mp \frac{1}{2} \sqrt{\frac{1}{4}+2 \lambda} \pm \frac{1}{2} \sqrt{\frac{1}{4}+2 \lambda} \\
+\frac{\sqrt{t}}{4}+2 \lambda \\
=2 \lambda
\end{gathered}
$$

Thus

$$
\begin{aligned}
& E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]=1+4 \lambda \int_{0}^{\infty} e^{\frac{1}{\partial} k} \hat{c}(k) \\
& \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{aligned}
$$

Now $E\left[e^{\lambda\left\langle x_{1}\right\rangle}\right]$ is the moment generating function for the rardom variable $\left\langle x_{7}\right\rangle$. It is also the Laplace transform of the PDF.

It follows that

$$
E\left[\left\langle x_{T}\right\rangle\right]=\left.\frac{\partial}{\partial \lambda} E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]\right|_{\lambda=0}
$$

since $P(\lambda)$ is a function of $\lambda$ it follows that,

$$
\begin{aligned}
& \frac{\partial}{\partial \lambda} E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]=4 \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
& \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k+4 \lambda \int_{0}^{\infty} e^{i k} \hat{c}(k) \\
& k \frac{\partial p}{\partial \lambda} \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{aligned}
$$

Now

$$
\begin{aligned}
\frac{\partial P}{\partial \lambda} & =\frac{\partial}{\partial \lambda}\left[\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}\right] \\
& = \pm \frac{\partial}{\partial \sqrt{\frac{1}{4}+2 \lambda}} \\
& = \pm \frac{1}{\sqrt{\frac{1}{4}+2 \lambda}}
\end{aligned}
$$

Thus

$$
\frac{\partial}{\partial \lambda} E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]=4 \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k)
$$

$$
\begin{aligned}
& \cosh \left[\left(p-\frac{1}{2}\right) k\right] d k \pm \frac{4 \lambda}{\sqrt{t_{1}+\partial \lambda}} \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
& k \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{aligned}
$$

50

$$
\begin{aligned}
\frac{\partial}{\partial \lambda} & \left.E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]\right|_{\lambda=0} \\
& =4 \int_{0}^{\infty} e^{\partial k} \hat{c}(k) \cosh \left[\left(p(0)-\frac{1}{2}\right) k\right] d k
\end{aligned}
$$

but

$$
p(0)=\frac{1}{2} \text { or } 0
$$

so for the cosh term for $p=0$

$$
\cosh \left(-\frac{1}{2} k\right)
$$

and for $p=\frac{1}{2}$
$\cosh \left(\frac{1}{a} k\right)$
since

$$
\cosh \left(-\frac{1}{\partial} k\right)=\cosh \left(\frac{1}{\partial} k\right)
$$

The final result is given by

$$
\begin{aligned}
& \left.\frac{\partial}{\partial \lambda} E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]\right|_{\lambda=0}=E\left[\left\langle x_{T}\right\rangle\right]= \\
& \quad=4 \int_{0}^{\infty} e^{b k} \hat{c}(k) \cosh \left(\frac{1}{2} k\right) d k \\
& \Rightarrow E\left[\left\langle x_{T}\right\rangle\right]=4 \int_{0}^{\infty} e^{b k} \hat{c}(k) \cosh \left(\frac{1}{2} k\right) d k
\end{aligned}
$$

Recall that previouly it was shown the

$$
\begin{aligned}
E\left[x_{T}\right] & =E\left[\left\langle x_{T}\right\rangle\right] \\
& =2\left\{\int_{-\infty}^{0} p(k) d k+\int_{0}^{\infty} c(k) d k\right\}
\end{aligned}
$$

50

$$
\begin{aligned}
& E\left[\left\langle x_{T}\right\rangle\right]=4 \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{C}(k) \cosh \left(\frac{1}{\partial k}\right) d k \\
& =4 \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{C}(k) \frac{1}{\partial}\left(e^{\frac{1}{\partial k}}+e^{-\frac{1}{\partial k}}\right) d k \\
& =2 \int_{0}^{\infty} \hat{C}(k)\left(e^{k}+1\right) d k \\
& =2 \int_{0}^{\infty} \hat{C}(k) e^{k}+2 \int_{0}^{\infty} \hat{C}(k) d k
\end{aligned}
$$

recall that from put-call parity,

$$
\begin{aligned}
& \hat{p}(k)=e^{-k} \hat{c}(-k) \\
\Rightarrow & \hat{p}(-k)=e^{k} \hat{c}(k) \\
E\left[\left\langle x_{T}\right\rangle\right]= & 2\left\{\int_{0}^{\infty} \hat{p}(-k) d k+\int_{0}^{\infty} \hat{c}(k) d k\right\}
\end{aligned}
$$

$$
=2\left\{\int_{-\infty}^{0} \hat{p}(k) d k+\int_{0}^{\infty} \hat{c}(k) d k\right\}
$$

Thus the two results agree. The fair value of a variance swap is given by

$$
\begin{aligned}
E\left[\left\langle x_{T}\right\rangle\right] & =4 \int_{0}^{\infty} e^{b k} \hat{c}(k) \cosh \left(\frac{1}{2} k\right) d k \\
& =2\left\{\int_{-\infty}^{0} \hat{P}(k) d k+\int_{0}^{\infty} \hat{C}(k) d k\right\}
\end{aligned}
$$

## The Fair value of volatility under zero Correlation

The far value of volatility is given by,

$$
E\left[\sqrt{\left\langle x_{T}\right\rangle}\right]
$$

To compute this the following relation is used

$$
\sqrt{y}=\frac{1}{2 \sqrt{\pi}} \int_{0}^{\infty} \frac{1-e^{\lambda y}}{\lambda^{3 / 2}} d \lambda
$$

The book states this relation is well known. I am unable to find a reference to $t$. Verification also is not straight forward. It will be assumed to be true.
The argument disussed here is from (Friz and eatheral) valuation of volatility Derivatives as an Inverse Problem

If $y=\left\langle x_{1}\right\rangle$ and expectations are taken then

$$
E\left[\sqrt{\left\langle x_{T}\right\rangle}\right]=\frac{1}{2 \sqrt{\pi}} \int_{0}^{\infty} \frac{1-E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right]}{\lambda^{3 / 2}} d \lambda
$$

Now previously it was shown that

$$
\begin{aligned}
E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]=1+4 \lambda \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) & \\
& \cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{aligned}
$$

where

$$
p(\lambda)=\frac{1}{2} \pm \sqrt{\frac{1}{4}+2 \lambda}
$$

Here $\lambda$ is assumed negative of prevous analysis so

$$
\begin{gathered}
E\left[e^{p x_{T}}\right]=E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right] \\
E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right]=1-4 \lambda \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
\cosh \left[\left(p-\frac{1}{\partial}\right) k\right] d k
\end{gathered}
$$

$$
p(\lambda)=\frac{1}{2} \pm \sqrt{\frac{1}{4}-2 \lambda}
$$

Now since $\cosh (-x)=\cosh (x)$ it follows that

$$
\cosh \left[\left(\rho^{-\frac{1}{2}}\right) k\right]=\cosh \left(k \sqrt{\frac{1}{4}-2 \lambda}\right)
$$

Putting things together gives

$$
\begin{aligned}
& E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right]=1-4 \lambda \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
& \cosh \left(k \sqrt{t_{1} \cdot \partial \lambda}\right) d k \\
& \Rightarrow 1-E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right]= 4 \lambda \int_{0}^{\infty} e^{\frac{1}{\partial k}} \hat{c}(k) \\
& \cosh \left(k \sqrt{t_{1} \cdot 2 \lambda}\right) d k
\end{aligned}
$$

Also, recall that

$$
\begin{aligned}
E\left[S_{T}^{P}\right]=F^{P}+ & p(p-1) S_{0}^{F} \tilde{P}(K, T) K^{P-2} d K \\
& +p(p-1) \int_{0}^{F} \tilde{C}(K, T) K^{P-2} d K
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow E & {\left[\left(\frac{S_{T}}{F}\right)^{P}\right]-1=\frac{P(P-1)}{F^{P}}\{ } \\
& \left.\int_{0}^{F} \tilde{P}(K, T) K^{P-2} d K+\int_{F}^{\infty} \tilde{C}(K, T) K^{P-2} d K\right\}
\end{aligned}
$$

but

$$
e^{x_{T}}=\frac{S_{I}}{F}
$$

so

$$
E\left[\left(\frac{S_{T}}{F}\right)^{P}\right]=E\left[e^{P X_{T}}\right]=E\left[e^{-\lambda\left\langle X_{T}\right\rangle}\right]
$$

Where the last step follows from the zero correlation assumption, so

$$
\begin{gathered}
E\left[e^{\lambda\left\langle x_{T}\right\rangle}\right]-1=\frac{P(P-1)}{F^{P}}\left\{\int_{0}^{F} \tilde{P}(K, T) K^{P-2} d K\right. \\
\left.+\int_{F}^{\infty} \tilde{C}(K, T) K^{P-2} d K\right\}
\end{gathered}
$$

Note that the weight term is given by

$$
\frac{P(p-1)}{F^{p}} K^{p-2}
$$

In the at the money limit

$$
\left.\frac{P(P-1)}{F^{P}} K^{P-2}\right|_{K=F}=\frac{P(P-1)}{F^{2}}
$$

but here $\lambda>0$ so,

$$
p(p-1)=2 \lambda
$$

and

$$
\left.\frac{P(p-1)}{F^{P}} K^{P-2}\right|_{K=F}=\frac{\partial \lambda}{F^{2}}
$$

If zero dividends and risk-frce return are assumed $F=S_{0}$ so

$$
\left.\frac{P(p-1)}{F^{P}} K^{P-2}\right|_{K=F}=\frac{2 \lambda}{s_{0}^{2}}
$$

Returning to the integrat,

$$
E\left[\sqrt{\left\langle x_{T}\right\rangle}\right]=\frac{1}{2 \sqrt{\pi}} \int_{0}^{\infty} \frac{1-E\left[e^{-\lambda\left\langle x_{T}\right\rangle}\right]}{\lambda^{3 / 2}} d \lambda
$$

using

$$
\begin{aligned}
1-E\left[e^{-\lambda\left\langle x_{1}\right\rangle}\right]= & 4 \lambda \int_{0}^{\infty} e^{\frac{1}{2} k} \hat{c}(k) \\
& \cosh \left(k \sqrt{t_{1}-\partial \lambda}\right) d k
\end{aligned}
$$

gives

$$
\begin{aligned}
& E\left[\sqrt{\left\langle x_{T}\right\rangle}\right]=\frac{1}{2 \sqrt{\pi}} \int_{0}^{\infty} \lambda^{-3 / 2} 4 \lambda \int_{0}^{\infty} e^{k / 2} \hat{c}(k) \\
& \cosh \left(k \sqrt{t_{1}-2 \lambda}\right) d k d \lambda \\
& =\frac{2}{\sqrt{\pi}} \int_{0}^{\infty} \frac{1}{\sqrt{\lambda}} \int_{0}^{\infty} e^{k / 2} \hat{c}(k) \cosh \left(k \sqrt{\frac{1}{4}-2 \lambda}\right) d k d \lambda \\
& =\int_{0}^{\infty} \hat{C}(k) \omega(k) d k
\end{aligned}
$$

where $\omega(k)$ is the weight,

$$
\omega(k)=\frac{2}{\sqrt{\pi}} e^{k / 2} \int_{0}^{\infty} \frac{\cosh \left(k \sqrt{\frac{1}{4}-2 \lambda}\right)}{\sqrt{\lambda}} d \lambda
$$

It can be shown that

$$
\omega(k)=\sqrt{\frac{\pi}{2}} e^{k / 2} I_{1}(k / 2)+\sqrt{2 \pi} \delta(k)
$$

where $I_{1}(x)$ is the modified Bessel function of the first kind and $\delta(k)$ is the Dirac delta function.

At The Money value of Black-Sndes European Call option

Recall that the Block-Sondes solution for the price of a European Call option is given by,

$$
c=F\left\{N\left(-\frac{k}{\sqrt{\omega}}+\frac{\sqrt{\omega}}{2}\right)-e^{k} N\left(-\frac{k}{\sqrt{\omega}}-\frac{\sqrt{\omega}}{2}\right)\right\}
$$

where

$$
\begin{array}{r}
k=\ln \frac{k}{F} \quad \omega=\sigma_{B S}(k) \sqrt{T} \\
F=s_{0} e^{s_{0}^{T} \mu d t}
\end{array}
$$

Now At the money $k=0$ so

$$
C(0)=F\left\{N\left(\frac{\sqrt{\omega}}{2}\right)-N\left(-\frac{\sqrt{\omega}}{2}\right)\right\}
$$

Now

$$
\begin{aligned}
& N\left(\frac{\sqrt{\omega}}{2}\right)-N\left(-\frac{\sqrt{\omega}}{2}\right)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\sqrt{\omega} / 2} e^{-x^{2} / 2} d x \\
& \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-\sqrt{\omega} / 2} e^{-x^{2} / 2} d x \\
&= \frac{1}{\sqrt{2 \pi}} \int_{-\sqrt{\omega / 2}}^{\sqrt{\omega / 2}} e^{x^{2} / 2} d x
\end{aligned}
$$

If $\omega$ is small then

$$
\begin{aligned}
& N\left(\frac{\sqrt{\omega}}{2}\right)-N\left(-\frac{\sqrt{\omega}}{2}\right) \approx \frac{1}{2 \pi}\left(\frac{\sqrt{\omega}}{2}+\frac{\sqrt{\omega}}{2}\right) \\
& =\frac{\sqrt{\omega}}{\sqrt{2 \pi}}=\frac{\sigma_{B S} \sqrt{T}}{\sqrt{2 \pi}}
\end{aligned}
$$

Thus

$$
c(0) \approx F \frac{F G_{B S} \sqrt{T}}{\sqrt{2 \pi}}
$$

but the discounted option price is

$$
\hat{c}(k)=\frac{c\left(F e^{k}\right)}{F e^{k}}
$$

so At-the-money

$$
\hat{C}(0) \approx \frac{\sigma_{B S} \sqrt{T}}{\sqrt{2 \pi}}
$$

