## Probability Distributions

Troy stribling Feb. 52017 ]

## Transformation of univariate Random variable

Consider a random variable IX with prability density $p(x)$ and a transformation

$$
Z=g(X)
$$

that is invertable

$$
\Rightarrow \quad \begin{aligned}
\bar{x} & =g^{-1}(\underline{\eta}) \\
d x & =d g^{-1}(y)
\end{aligned}
$$

Assuming that the transformation conserves differential probability

$$
\begin{aligned}
p(x) d x & =p\left(g^{-1}(y)\right) d g^{-1}(y) \\
& =p\left(g^{-1}(y)\right) \frac{d g^{-1}}{d y} d y
\end{aligned}
$$

50

$$
p(y)=p\left(g^{-1}(y)\right) \frac{d g^{-1}}{d y}
$$

Now consider $P(I \leqslant y)$ where

$$
\begin{array}{ll}
y=h(x), & x=h^{-1}(y) \\
d y=d h(x), & d x=d h^{-1}(y)
\end{array}
$$

Now if $h(x)$ is monotonically increasing

$$
I \leqslant y \Rightarrow I \leqslant h(x) \Rightarrow h^{-1}(I) \leqslant x
$$

50

$$
\begin{aligned}
P(\bar{I} \leqslant y) & =P[\bar{I} \leqslant h(x)] \\
& =P\left[h^{-1}(\bar{I}) \leqslant x\right]
\end{aligned}
$$

As an example consider the log nonmal distribution defined by the transformation

$$
I=e^{\bar{X}}
$$

defines I as lognarmally distributed It follows that

$$
\begin{aligned}
y & =g(x) & =e^{x} \quad y>0 \\
\Rightarrow g^{-1}(y) & =x & =\ln y
\end{aligned}
$$

It follows that the density of I is given by

$$
p(x)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-(x-\mu)^{2} / 2 \sigma^{2}}
$$

using

$$
P(y)=P\left(g^{-1}(y)\right) \frac{d g^{-1}}{d y}
$$

sives the lognormal density

$$
P(y)=\frac{1}{\sigma_{y} \mid D \pi} \exp \left[\left(\frac{\ln y-\mu}{2 \sigma^{2}}\right)^{2}\right] y>0
$$

## Normal Distribution

The normal or gaussian distribution is defined by the density function

$$
P(x)=c e^{-x^{2}} \quad x \in(-\infty, \infty)
$$

The normalization factor $C$ is
$1=c \int_{-\infty}^{\infty} e^{-x^{2}} d x=c \sqrt{\int_{-\infty}^{\infty} e^{-x^{2}} d x \int_{-\infty}^{\infty} e^{-y^{2}} d y}$
$=c \sqrt{\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-\left(x^{2}+y^{2}\right)} d x d y}$
swith to polar coordinates

$$
\begin{aligned}
& r^{2}=x^{2}+y^{2} \\
& x=r \cos \phi \quad y=r \sin \phi
\end{aligned}
$$

The volume element becomes

$$
r d r d \varphi
$$

So the intergral becomes
$\sqrt{\int_{n}^{\infty} \int_{n}^{2 \pi} r e^{-r^{2}} d r d \varphi}=1$
$\Rightarrow \sqrt{2 \pi \int_{0}^{\infty} r e^{-r^{2}} d r}=1$
let

$$
u=r^{2} \Rightarrow d u=2 r d r \Rightarrow \frac{1}{2} d u=r d r
$$

so the integral becomes $\sqrt{\pi \int_{0}^{\infty} e^{-u} d u}=1$
$\Rightarrow \quad \sqrt{-\pi e^{-u}} \hat{l}_{0}=d-\overline{\pi(0-1)}=\sqrt{\pi}$
it follows that

$$
C=\frac{1}{\sqrt{\pi}}
$$

Trus the gaussian density
function is

$$
p(x)=\frac{1}{\sqrt{\pi}} e^{-x^{2}}
$$

let

$$
x=\frac{y-\mu}{\sqrt{2} G}
$$

then the normilzation integral becomes

$$
C \int_{-\infty}^{\infty} e^{-\frac{(y-\mu)^{2}}{2 \sigma^{2}}} d y
$$

let

$$
\begin{aligned}
z= & \frac{y-\mu}{\sqrt{2} \sigma} \Rightarrow y=\sqrt{2} z \sigma+\mu \\
\Rightarrow & d y=\sqrt{2} \sigma d z
\end{aligned}
$$

then

$$
\begin{aligned}
& C \int_{-\infty}^{\infty} \sqrt{2} \sigma e^{-z^{2}} d z \\
= & \sqrt{2} \cos \int_{-\infty}^{\infty} e^{-z^{2}} d z \Rightarrow c=\frac{1}{\sigma \sqrt{2 \pi}}
\end{aligned}
$$

so

$$
p(x)=\frac{1}{\sigma \sqrt{2 \pi}} e^{-\left(\frac{x-\mu}{2}\right)^{2}}
$$

The mean of the distribution is defined by
$\langle x\rangle=\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} x e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x$
let

$$
\begin{aligned}
& z=\frac{x-\mu}{\sqrt{2} \sigma^{2}} \Rightarrow x=\sqrt{2} \sigma z+\mu \\
& d x=\sqrt{2} \sigma d z
\end{aligned}
$$

then

$$
\begin{aligned}
\langle x\rangle= & \frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \sqrt{2} \sigma(\sqrt{2} \sigma z+\mu) e^{-z^{2}} d z \\
=\frac{\sqrt{2}}{\sigma \sqrt{2 \pi}} & {\left[\int_{-\infty}^{\infty} \sqrt{2} \sigma^{2} z e^{-z^{2}} d z\right.} \\
& \left.+\sigma \mu \int_{-\infty}^{\infty} e^{-z^{2}} d z\right]
\end{aligned}
$$

$=\frac{\sigma}{\sqrt{H}} \int_{-\infty}^{\infty} z e^{-z^{2}} d z+\frac{\mu}{\sqrt{\pi}} \int_{-\infty}^{\infty} e^{-z^{2}} d z$
The second integral is

$$
\int_{-\infty}^{\infty} e^{-z^{2}} d z=\sqrt{\pi}
$$

To evaluate the first let

$$
u=z^{2} \Rightarrow \frac{1}{2} d u=z d z
$$

then

$$
\begin{aligned}
& \int_{-\infty}^{\infty} 2 e^{-z^{2}} d z=\int_{-\infty}^{0} z e^{-z^{2}} d z \\
+ & \int_{0}^{\infty} z e^{-z^{2}} d z \\
= & \int_{\infty}^{0} e^{-u} d u+\int_{0}^{\infty} e^{-u} d u \\
= & -\int_{0}^{\infty} e^{-u} d u+\int_{0}^{\infty} e^{-u} d u \\
= & 0
\end{aligned}
$$

so the first term is 0, and

$$
\langle x\rangle=\frac{\mu}{\pi} \sqrt{\pi}=\mu
$$

The second moment is defined by 1

$$
\left\langle x^{2}\right\rangle=\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} x^{2} e^{-\frac{(x \cdot \mu)^{2}}{\sigma^{2}}} d x
$$

once again let

$$
\begin{aligned}
z & =\frac{x-\mu}{\sqrt{26}} \Rightarrow x=\sqrt{2} \sigma z+\mu \\
& \Rightarrow \quad d x=\sqrt{2} \sigma d z
\end{aligned}
$$

then

$$
\begin{aligned}
&\left\langle x^{2}\right\rangle= \frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty}(\sqrt{2} \sigma z+\mu)^{2} e^{-z^{2}} \sqrt{2} \sigma d z \\
&=\frac{1}{\pi} \int_{-\infty}^{\infty}\left(2 \sigma^{2} z^{2}+2 \sqrt{2} \mu \sigma z+\mu^{2}\right) e^{-z^{2}} d z \\
&=\frac{1}{\sqrt{\pi}} {\left[\int_{-\infty}^{\infty} 2 \sigma^{2} z^{2} e^{-z^{2}} d z+2 \sqrt{2} \mu \sigma \int_{-\infty}^{\infty} z e^{-z^{2}} d z\right.} \\
&\left.+\mu^{2} \int_{-\infty}^{\infty} e^{-z^{2}} d z\right]
\end{aligned}
$$

$=\frac{1}{\sqrt{\pi}}\left[\partial \sigma^{2} \int_{-\infty}^{\infty} z^{2} e^{-z^{2}} d z+0+\mu^{2} \sqrt{\pi}\right]$
$=\frac{2 \sigma^{2}}{\sqrt{\pi}} \rho_{-\infty}^{\infty} z^{2} e^{\cdot z^{2}} d z+\mu^{2}$
To solve the first integral use integration by parts

$$
\int u d v=u v-\int v d u
$$

let

$$
\begin{aligned}
& u=z=-\quad d u=d z \\
& d v=z e^{-z^{2}} d z
\end{aligned}
$$

Then

$$
v=\int 2 e^{-z^{2}} d z
$$

using

$$
y=z^{2} \Rightarrow \frac{1}{2} d y=z d z
$$

50

$$
V=\frac{1}{2} \int e^{-y} d y=-\frac{1}{2} e^{-y}=-\frac{1}{2} e^{-z^{2}}
$$

Bringing things together

$$
\int_{-\infty}^{\infty} z^{2} e^{-z^{2}} d z=-\left.\frac{1}{2} z e^{-z^{2}}\right|_{-\infty} ^{\infty}
$$

$$
\begin{aligned}
& +\frac{1}{2} \int_{-\infty}^{\infty} e^{-z^{2}} d z \\
= & 0+\frac{\sqrt{\pi}}{2}
\end{aligned}
$$

50

$$
\begin{aligned}
\left\langle x^{2}\right\rangle & =\frac{2 \sigma^{2}}{\sqrt{H}}\left(\frac{\sqrt{\pi}}{2}\right)+\mu^{2} \\
& =\sigma^{2}+\mu^{2}
\end{aligned}
$$

Thus the variance is

$$
\left\langle x^{2}\right\rangle-\mu^{2}=\sigma^{2}
$$

## Bimodal Normal Distribution

The Bimodal Normal Distribution is defined by the density
$f(x)=\frac{\alpha}{\sqrt{2 \pi \sigma_{1}^{2}}} e^{-\frac{\left(x-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}}+\frac{1-\alpha}{\sqrt{2 \pi \sigma_{2}^{2}}} e^{-\frac{\left(x-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}}$
where $\mu_{1}$ and $\sigma_{1}$ are the mean and standard deviation of the first normal density and $\mu_{2}$ and $S_{2}$ the medn and standard deviation of the second density. 2 is the coupling constant that must satisfy

$$
0 \leq \alpha \leq 1
$$

$$
\begin{aligned}
& \int_{-\infty}^{\infty} f(x) d x=\int_{-\infty}^{\infty} \frac{\alpha}{\sqrt{2 \pi \sigma_{1}^{2}}} e^{-\frac{\left(x-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}} d x \\
& +\int_{-\infty}^{\infty} \frac{1-\alpha}{\sqrt{2 \pi \sigma_{2}^{2}}} e^{-\frac{\left(x-\mu_{1}\right)^{2}}{2 \sigma_{2}^{2}}} d x \\
& =\frac{\alpha}{\sqrt{2 \pi} \sigma_{1}^{2}} \int_{-\infty}^{\infty} e^{-\left(\frac{x-\mu)^{2}}{2 \sigma_{1}^{2}}\right.} d x
\end{aligned}
$$

$$
\begin{aligned}
& +\frac{(1-\alpha)}{\sqrt{2 \pi \sigma_{2}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{\left(x-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}} d x \\
& =\frac{\alpha}{\sqrt{2 \pi \sigma_{2}^{2}}} \sqrt{2 \pi \sigma_{2}^{2}}+\frac{(1-\alpha)}{\sqrt{2 \pi \sigma_{2}^{2}}} \sqrt{2 \pi \sigma_{2}^{2}} \\
& =\alpha+1-\alpha=1
\end{aligned}
$$

Thus

$$
\int_{-\infty}^{\infty} f(x) d x=1
$$

Now the mean is given by

$$
\begin{aligned}
\mu & =\int_{-\infty}^{\infty} x f(x) d x \\
& =\alpha \mu_{1}+(1-\alpha) \mu_{2}
\end{aligned}
$$

and the second moment by

$$
\begin{gathered}
\left\langle x^{2}\right\rangle=\int_{-\infty}^{\infty} x^{2} f(x) d x=\alpha\left(\sigma_{1}^{2}+\mu_{1}^{2}\right) \\
+(1-\alpha)\left(\sigma_{2}^{2}+\mu_{2}^{2}\right)
\end{gathered}
$$

$$
\begin{aligned}
& \text { It follows that the variance } \\
& \begin{aligned}
\sigma^{2}= & \left\langle x^{2}\right\rangle-\mu^{2} \\
= & \alpha\left(\sigma_{1}^{2}+\mu_{1}^{2}\right)+(1-\alpha)\left(\sigma_{2}^{2}+\mu_{2}^{2}\right) \\
& -\left[\alpha \mu_{1}+(1-\alpha) \mu_{2}\right]^{2}
\end{aligned}
\end{aligned}
$$

## Log Normal Distribution

A log normal distribution is the distribution obtained when the logarthm of a random variable is normally diotributed. For example if $\bar{X}$ is log normally distributed then

$$
\bar{Y}=\ln (\bar{X})
$$

is normally distributed. Likewise if $\underline{I}$ is normally distributed then

$$
\underline{X}=e^{I}
$$

is los normal. If $\bar{I}$ has mean $\mu$ and standard deviation $\sigma$ then

$$
\underline{Y}=\mu+\sigma Z
$$

where $Z$ is the cunit normal distribution. Then

$$
\bar{x}=e^{\mu+\sigma z}=e^{\mu}\left(e^{z}\right)^{\sigma}
$$

Since the distribution of $\ln \bar{X}$ is normal ts distribution can be written as

$$
p(\ln x)=\frac{1}{\sigma \sqrt{2 \pi}} \operatorname{etp}\left[\frac{(\ln x-\mu)^{2}}{2 \sigma^{2}}\right]
$$

where

$$
\langle\ln x\rangle=\mu
$$

and

$$
\left\langle(\ln x)^{2}\right\rangle-\mu^{2}=\sigma^{2}
$$

Now compute the mean and varance of $x$, recall that

$$
\Delta=e^{\nabla}
$$

where $\bar{Y}$ is normally distributed with mean $\mu$ and standard deviation $\sigma$. , so

$$
\begin{aligned}
& \langle\underline{\underline{x}}\rangle=\left\langle e^{\underline{y}}\right\rangle=\frac{1}{\sigma \sqrt{2 \pi}} \int^{\infty}\left(e^{y}\right) e^{\frac{(y-\mu)^{2}}{2 \sigma^{2}}} d y \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left[y+\frac{(y-\mu)^{2}}{2 \sigma^{2}}\right] d y
\end{aligned}
$$

First change variables

$$
z=y-\mu \Rightarrow \quad d z=d y
$$

Substitubing gives

$$
\begin{aligned}
\langle\underline{x}\rangle & =\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp (z+\mu) \exp \left(\frac{z^{2}}{\partial \sigma^{2}}\right) d z \\
& =\frac{e^{\mu}}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left(z+\frac{z^{2}}{\partial \sigma^{2}}\right) d z
\end{aligned}
$$

Just considering the exponential term

$$
\begin{aligned}
& z+\frac{z^{2}}{2 \sigma^{2}}=\frac{2 \sigma^{2} z+z^{2}}{2 \sigma^{2}} \\
= & \frac{z^{2}+2 \sigma^{2} z+\sigma^{4}-\sigma^{4}}{2 \sigma^{2}} \\
= & \frac{\left(z+\sigma^{2}\right)^{2}}{2 \sigma^{2}}-\frac{\sigma^{2}}{2}
\end{aligned}
$$

Putting the pieces together

$$
\begin{aligned}
\langle\underline{x}\rangle & =\frac{e^{\mu}}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left[\frac{\left(z+\sigma^{2}\right)^{2}}{2 \sigma^{2}}\right] e^{-\frac{1}{b} \sigma^{2}} d z \\
& =\frac{e^{\mu-\frac{1}{2} \sigma^{2}}}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{\frac{\left(z+\sigma^{2}\right)^{2}}{\partial \sigma^{2}}} d z
\end{aligned}
$$

but

$$
\int_{-\infty}^{\infty} e^{\frac{(z+2 \sigma)^{2}}{2 \sigma^{2}}} d z=\sigma \sqrt{2 \pi}
$$

50

$$
\langle\bar{X}\rangle=e^{\mu-\frac{1}{2} \sigma^{2}}
$$

The variance is given by

$$
\sigma^{2}=\left\langle\nabla^{2}\right\rangle \cdot(\langle\nabla\rangle)^{2}
$$

So,

$$
\begin{aligned}
& \left\langle\underline{x}^{2}\right\rangle=\left\langle\left(e^{\underline{y}}\right)^{2}\right\rangle=\left\langle e^{2 \underline{y}}\right\rangle \\
= & \frac{1}{\sigma \sqrt{2} \pi} \int_{-\infty}^{\infty} e^{2 y} e^{(y-\mu)^{2}} \frac{d y}{2 \sigma^{2}}
\end{aligned}
$$

once again let

$$
z=y+\mu \Rightarrow \quad d z=d y
$$

then the integral becomes

$$
\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{2(z+\mu)} e^{z^{2} / 2 \sigma^{2}} d z
$$

$$
\begin{aligned}
& =\frac{1}{\sigma \sqrt{2 \pi}} e^{2 \mu} \int_{-\infty}^{\infty} e^{\partial z} e^{z^{2} / 2 \sigma^{2}} d z \\
& =\frac{1}{\sigma \sqrt{2 \pi}} e^{2 \mu} \int_{-\infty}^{\infty} \exp \left[2 z+\frac{z^{2}}{2 \sigma^{2}}\right] d z
\end{aligned}
$$

for the argument of the exponential

$$
\begin{aligned}
& 2 z+\frac{z^{2}}{2 \sigma^{2}}=\frac{4 z \sigma^{2}+z^{2}}{2 \sigma^{2}} \\
& =\frac{4 z \sigma^{2}+z^{2}+4 \sigma^{4}-4 \sigma^{4}}{2 \sigma^{2}} \\
& =\frac{\left(z^{2}+4 z \sigma+4 \sigma^{4}\right) \cdot 2 \sigma^{2}}{2 \sigma^{2}} \\
& =\frac{\left(z+2 \sigma^{2}\right)^{2}}{2 \sigma^{2}}-2 \sigma^{2}
\end{aligned}
$$

so the integral becomes

$$
\begin{aligned}
& \frac{1}{\sigma \sqrt{2 \pi}} e^{2 \mu} \int_{-\infty}^{\infty} e^{-2 \sigma} e^{\frac{\left(z+2 \sigma^{2}\right)^{2}}{2 \sigma^{2}}} d z \\
= & \frac{1}{\sigma \sqrt{2 \pi}} e^{2 \mu-2 \sigma^{2}} \int_{-\infty}^{\infty} e^{\frac{\left(z+2 \sigma^{2}\right)^{2}}{2 \sigma^{2}}} d z
\end{aligned}
$$

$=\frac{1}{\sigma \sqrt{2 \pi}} e^{2 \mu-2 \sigma^{2}} \sigma \sqrt{2 \pi}$
$=e^{2 \mu-2 \sigma^{2}}=e^{2\left(\mu-\sigma^{2}\right)}$
Thus

$$
\left\langle Z^{2}\right\rangle=e^{2\left(\mu-\sigma^{2}\right)}
$$

It follows that

$$
\begin{aligned}
\sigma^{2} & =\left\langle\underline{X}^{2}\right\rangle-(\langle\underline{X}\rangle)^{2} \\
& =e^{2\left(\mu-\sigma^{2}\right)}-e^{\mu-\frac{1}{2} \sigma^{2}}
\end{aligned}
$$

For the $n$ 'th momement is is easy to see

$$
\begin{aligned}
& \left\langle Z^{n}\right\rangle=\left\langle\left(e^{y}\right)^{n}\right\rangle=\left\langle e^{n y}\right\rangle \\
& =\frac{1}{8 \sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{n y} e^{(y-\mu)^{2} / 2 G^{2}} d y
\end{aligned}
$$

let

$$
z=y-\mu \Rightarrow d z=d y
$$

The integral becomes

$$
\begin{aligned}
& \frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{n(z+\mu)} e^{z^{2} / 2 \sigma^{2}} d z \\
& \frac{1}{\sigma \sqrt{2 \pi}} e^{n \mu} \int_{-\infty}^{\infty} \exp \left[n z+\frac{z^{2}}{2 \sigma^{2}}\right] d z
\end{aligned}
$$

For the exponential argument

$$
\begin{aligned}
& n z+\frac{z^{2}}{2 \sigma^{2}}=\frac{2 \sigma^{2} n z+z^{2}}{2 \sigma^{2}} \\
= & \frac{2 \sigma^{2} n z+z^{2}+\sigma^{4} n^{2}-\sigma^{4} n^{2}}{2 \sigma^{2}} \\
= & \frac{\left(\sigma^{2} n+z\right)^{2}}{2 \sigma^{2}}-\frac{\sigma^{2} n^{2}}{2}
\end{aligned}
$$

so the integral becomes

$$
\begin{aligned}
& \frac{1}{\sigma \sqrt{2} \pi} e^{n \mu} \int_{-\infty}^{\infty} e^{-\sigma^{2} n^{2} / 2} \exp \left[\frac{\left(\sigma^{2} n+2\right)^{2}}{2 \sigma^{2}}\right] d z \\
= & \frac{1}{\sigma \sqrt{2} \pi} e^{n \mu \cdot n^{2} \sigma^{2} / 2} \int_{-\infty}^{\infty} e^{\left(\sigma^{2} n+2\right)^{2} / 2 \sigma^{2}} d z
\end{aligned}
$$

$$
\begin{aligned}
\sigma \frac{1}{\sqrt{2 \pi}} & e^{n \mu-n^{2} \sigma^{2} / 2} \int_{-\infty}^{\infty} e^{\left(\sigma^{2} n+2\right)^{2} / 2 \sigma^{2}} d z \\
& =e^{n \mu-n^{2} \sigma^{2} / 2}
\end{aligned}
$$

Trus

$$
\left\langle\bar{X}^{n}\right\rangle=e^{n \mu-n^{2} \sigma^{2} / 2}
$$

## Normal Cumulative Astribution

The Normal Cumulative Distribution is defined by

$$
\Phi(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x} e^{-t^{2} / 2} d t
$$

Let

$$
t=\frac{y-\mu}{\sigma} \Rightarrow y=\sigma t+\mu
$$

and

$$
d t=\frac{d y}{\sigma}
$$

so

$$
\Phi(x)=\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\mu}^{\sigma x+\mu} \exp \left[\left(\frac{(y-\mu)^{2}}{2 \sigma^{2}}\right] d y\right.
$$

letting

$$
\begin{aligned}
z & =\sigma x+\mu \\
& \Rightarrow x=\frac{2-\mu}{\sigma}
\end{aligned}
$$

$\delta o$

$$
\Phi\left(\frac{2-\mu}{\sigma}\right)=\frac{1}{\sigma^{12} \pi} \int_{-\infty}^{2} \exp \left[\frac{(t-\mu)^{2}}{2 \sigma^{2}}\right] d t
$$

It is easy to see that

$$
\Phi(\infty)=1
$$

and because the normal density is symetric about $x=0$

$$
\Phi(-x)=\Phi(\infty)-\Phi(x)=1-\Phi(x)
$$

* The error function is defined by

$$
\operatorname{erf}(x)=\frac{1}{\sqrt{\pi}} \int_{-x}^{x} e^{-t^{2}} d t
$$

let

$$
t=\frac{y}{\sqrt{2}} \Rightarrow \quad d t=\frac{d y}{\sqrt{2}} \Rightarrow y=\sqrt{2} t
$$

50

$$
\operatorname{erf}(x)=\frac{1}{\sqrt{2 \pi}} \int_{-\sqrt{2} x}^{\sqrt{2} x} e^{-t_{12}^{2}} d t
$$

$$
\begin{aligned}
& =\frac{1}{2 \pi} \int_{-\infty}^{\sqrt{2} x} e^{-t^{2} / 2} d t-\int_{-\infty}^{-\sqrt{2} x} e^{-t^{2} / 2} d t \\
& =\Phi(\sqrt{2} x)-\Phi(-\sqrt{2} x) \\
& =\Phi(\sqrt{2} x)-1+\Phi(\sqrt{2} x) \\
& =2 \Phi(\sqrt{2} x)-1 \\
& \Rightarrow \Phi(\sqrt{2} x)=\frac{1}{2}[1-\operatorname{erf}(x)]
\end{aligned}
$$

letting

$$
z=\sqrt{2} x
$$

gives

$$
\Phi(z)=\frac{1}{2}\left[1-\operatorname{erf}\left(\frac{z}{\sqrt{2}}\right)\right]
$$

## Folded Normal Distribution

The folded normal distribution is defined by

$$
\underline{I}=|\underline{I}|
$$

where $\bar{X}$ is a Normal distribution

$$
\nabla \sim N\left(\mu, \sigma^{2}\right)
$$

For $y>0$

$$
\begin{aligned}
& P(I<y)=P(|\nabla|<y)=P(-y<x<y) \\
& =\int_{-y}^{y} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} d x \\
& =\int_{-\infty}^{y} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} d x \cdot \int_{-\infty}^{-y} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{1}{\sigma}\left(\frac{y-\mu}{\sigma}\right)^{2}} d x \\
& =\Phi\left(\frac{y-\mu}{\sigma}\right)-\Phi\left[-\left(\frac{y+\mu}{\sigma}\right)\right] \\
& =\Phi\left(\frac{y-\mu}{\sigma}\right)-\left[1-\Phi\left(\frac{y+\mu}{\sigma}\right)\right] \\
& =\Phi\left(\frac{y-\mu}{\sigma}\right)+\Phi(y+\mu)-1
\end{aligned}
$$

$$
\begin{aligned}
= & \int_{-\infty}^{y} \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{-\infty}^{y} \frac{1}{\sigma \sqrt{2}} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
- & \int_{-\infty}^{\infty} \frac{1}{\sigma \sqrt{2} \pi} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
= & \frac{1}{\sigma \sqrt{2 \pi}}\left\{\int_{0}^{y} e^{-\left(\frac{x-\mu)^{2}}{2 \sigma^{2}} d x\right.}+\int_{-\infty}^{0} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right. \\
& +\int_{0}^{y} e^{-\left(\frac{x+\mu}{2 \sigma^{2}} d x\right.}+\int_{-\infty}^{0} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x \\
& \left.-\left[\int_{-\infty}^{0} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}} d x} \int_{0}^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right]\right\} \\
= & \frac{1}{\sigma \sqrt{2} \pi} \int_{0}^{-\left(\int_{0}^{0} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\left[\int_{-\infty}^{0} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right.\right.} \\
& \left.-\int_{-\infty}^{0} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right] \\
& +\int_{c}^{y} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x+\left[\int_{-\infty}^{0} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x\right. \\
& \left.\left.-\int_{0}^{\infty} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
=\frac{1}{\sigma \sqrt{2} \pi} & \left\{\int_{0}^{y} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{0}^{y} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x\right. \\
& \left.+\left[\int_{-\infty}^{0} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x-\int_{0}^{\infty} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right]\right\}
\end{aligned}
$$

Now let

$$
z=-x \quad \Rightarrow \quad d x=-d z
$$

then

$$
\begin{aligned}
& \int_{0}^{\infty} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x=-\int_{0}^{\infty} e^{-\left(-\frac{2-\mu}{2 \sigma^{2}}\right)^{2}} d z \\
& =\int_{-\infty}^{0} e^{-\left(\frac{2+\mu}{2 \sigma^{2}}\right)^{2}} d z
\end{aligned}
$$

Putting things together

$$
\begin{gathered}
P(-y<x<y)=\frac{1}{\sigma \sqrt{2 \pi}}\left\{\int_{0}^{y} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x\right. \\
+\int_{0}^{y} e^{-\frac{(x+\mu)^{2}}{2 \sigma} d x}+\left[\int_{-\infty}^{0} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}} d x}\right. \\
\left.\left.-\int_{-\infty}^{0} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x\right]\right\}
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{1}{\sigma \sqrt{2 \pi}}\left[\int_{0}^{y} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x+\int_{0}^{y} e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}} d x\right] \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{0}^{y}\left[e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}}+e^{-\frac{(x+\mu)^{2}}{2 \sigma^{2}}}\right] d x
\end{aligned}
$$

The probability density is given
by

$$
\begin{aligned}
& f_{z}(y)=\frac{d}{d y} P(I<y) \\
= & \frac{1}{\delta \sqrt{2 \pi}}\left[e^{-\frac{(y-\mu)^{2}}{2 \sigma^{2}}}+e^{-\frac{(y+\mu)^{2}}{2 \sigma^{2}}}\right] \\
= & \frac{1}{\sigma \sqrt{2 \pi}}\left[e^{-\frac{\left(y^{2}-2 \mu y+\mu^{2}\right)}{2 \sigma^{2}}}+e^{-\frac{\left(y^{2}+2 \mu y-\mu^{2}\right)}{2 \sigma^{2}}}\right] \\
= & \frac{1}{\sigma \sqrt{2} \pi}\left[e^{-\left(y^{2}+\mu^{2}\right)} e^{\frac{2 \mu y}{2 \sigma^{2}}}+e^{-\frac{\left(y^{2}+\mu^{2}\right)}{2 \sigma^{2}}} e^{-\frac{2 \mu y}{\partial \sigma^{2}}}\right] \\
= & \frac{1}{\sigma \sqrt{2 \pi}} e^{-\left(y^{2}+\mu^{2}\right)}\left(e^{\frac{\mu y}{2 \sigma^{2}}}+e^{-\frac{\mu y}{\sigma^{2}}}\right) \\
= & \frac{1}{\sigma} \sqrt{\frac{2}{\pi}} e^{-\left(y^{2}+\mu^{2}\right)} \cosh \left(\frac{\mu y}{\sigma^{2}}\right)
\end{aligned}
$$

Find the mean E[I] and $\operatorname{Var}($ I) using,

$$
f_{Y}(y)=\frac{1}{\sigma \frac{1}{2 \pi}}\left[e^{-\frac{(y-\mu)^{2}}{2 \sigma^{2}}}+e^{-\frac{(y+\omega)^{2}}{2 \sigma^{2}}}\right]
$$

Since $\quad \bar{Y}=|\bar{X}| \Rightarrow \quad y \geqslant 0$

$$
\begin{aligned}
E[\underline{Y}] & =\int_{0}^{\infty} y f_{I}(y) d y \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{0}^{\infty} y e^{-(y-\mu)^{2}} d y \\
& +\frac{1}{\sigma \sigma^{2}} \int_{0}^{\infty} y e^{-\left(y \frac{\mu}{2 \sigma^{2}}\right)^{2}} d y
\end{aligned}
$$

let

$$
\begin{array}{ll}
z=y=\frac{y}{\sigma} & \omega=\frac{y+\mu}{\sigma} \\
y=\sigma z+\mu & y=\sigma \omega-\mu \\
d y=\sigma d z & d y=\sigma d \omega
\end{array}
$$

$$
\begin{aligned}
E[I] & =\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty}(\sigma z+\mu) e^{-\frac{1}{2} z^{2}} d z \\
& +\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty}(\sigma \omega-\mu) e^{-\frac{1}{2} \omega^{2}} d \omega \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty} \sigma z e^{-\frac{1}{2} z^{2}} d z+\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \sigma \omega e^{-\frac{1}{2} \omega^{2}} d \omega \\
& +\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty} \mu e^{-\frac{1}{2} z^{2}} d z-\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \mu e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

Now for the first integrals use $u$ substitution

$$
u=\frac{1}{8} z^{2} \Rightarrow \quad d u=z d z
$$

then

$$
\begin{aligned}
& \frac{1}{2 \pi} \int_{-\frac{\mu}{0}}^{\infty} \sigma z e^{\frac{1}{2} z^{2}} d z=\frac{\sigma}{\sqrt{2 \pi}} \int_{\frac{\mu^{2}}{2 \sigma}}^{\infty} e^{-u} d u \\
& =-\left.\frac{\sigma}{\sqrt{2 \pi}} e^{-u}\right|_{\frac{\mu^{2}}{2 \sigma^{2}}} ^{\infty}=\frac{\sigma}{\sqrt{2 \pi}} e^{-\frac{\mu^{2}}{2 \sigma^{2}}}
\end{aligned}
$$

and

$$
\begin{aligned}
& \frac{1}{\sqrt{2} \pi} \int_{-\frac{\mu}{\sigma}}^{\infty} \mu e^{-\frac{1}{\sigma} z^{2}} d z \\
& =\mu\left[1-\int_{-\infty}^{-\frac{\mu}{\sigma}} e^{-\frac{1}{2} z^{2}} d z\right] \\
& =\mu\left[1-\Phi\left(-\frac{\mu}{\sigma}\right)\right]
\end{aligned}
$$

So

$$
\begin{aligned}
& E[\Phi]=\frac{G}{\sqrt{2 \pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\frac{\sigma}{\sqrt{2 \pi}} e^{-\mu^{2} / 2 \sigma^{2}} \\
& +\mu\left[\pi-\Phi\left(-\frac{\mu}{\sigma}\right)\right]-\mu\left[D-\Phi\left(\frac{\mu}{\sigma}\right)\right] \\
& =\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\mu\left[\Phi\left(\frac{\mu}{\sigma}\right)-\Phi\left(-\frac{\mu}{\sigma}\right)\right] \\
& =\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\mu\left[1-\Phi\left(-\frac{\mu}{\sigma}\right)-\Phi\left(-\frac{\mu}{\sigma}\right)\right] \\
& =\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\mu\left[1-2 \Phi\left(-\frac{\mu}{\sigma}\right)\right]
\end{aligned}
$$

and

$$
\begin{aligned}
E\left[Y^{2}\right] & =\int_{0}^{\infty} y^{2} f_{Y}(y) d y \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{0}^{\infty} y^{2} e^{-\left(\frac{(y-\mu)^{2}}{2 \sigma^{2}}\right.} d y \\
& +\frac{1}{\sigma \sqrt{2 \pi}} \int_{0}^{\infty} y^{2} e^{-\left(y \frac{\mu}{2 \sigma^{2}}\right)^{2}} d y
\end{aligned}
$$

let

$$
\begin{array}{ll}
z=y-\frac{\mu}{\sigma} & \omega=\frac{y+\mu}{\sigma} \\
y=\sigma z+\mu & y=\sigma \omega-\mu \\
d y=\sigma d z & d y=\sigma d \omega
\end{array}
$$

Then

$$
\begin{aligned}
E\left[I^{2}\right]= & \frac{1}{2 \pi} \int_{\frac{\mu}{\sigma}}^{\infty}(\sigma z-\mu)^{2} e^{-\frac{1}{2} z^{2}} d z \\
& +\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty}(\sigma \omega+\mu)^{2} e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty}\left(\sigma^{2} z^{2}-2 \mu \sigma z+\mu^{2}\right) e^{-\frac{1}{2} z^{2}} d z \\
& +\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty}\left(\sigma^{2} \omega^{2}+2 \mu \sigma \omega+\mu^{2}\right) e^{-\frac{1}{2} \omega^{2}} d \omega \\
& =\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \sigma^{2} z^{2} e^{-\frac{1}{2} z^{2}} d z+\frac{1}{\sqrt{2} \pi} \int_{-\frac{\mu}{\sigma}}^{\infty} \sigma^{2} \omega^{2} e^{-\frac{1}{2} \omega^{2}} d \omega \\
& -\frac{2}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty} \mu \sigma z e^{-\frac{1}{2} z^{2}} d z+\frac{2}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \mu \sigma e^{-\frac{1}{2} \omega^{2}} d \omega \\
& +\frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\sigma}}^{\infty} \mu^{2} e^{-\frac{1}{\partial} z^{2}} d z+\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \mu^{2} e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

Using the results from $E[x]$

$$
\begin{aligned}
& \frac{2}{\sqrt{2 \pi}} \int_{-\frac{\mu}{0}}^{\infty} \mu \sigma z e^{-\frac{1}{2} z^{2}} d z=\frac{2 \mu \sigma}{\sqrt{2 \pi}} e^{-\frac{\mu^{2}}{2 \sigma^{2}}} \\
& \frac{2}{\sqrt{2 \pi}} \int_{\mu_{0}}^{\infty} \mu \sigma z e^{-\frac{1}{2} z^{2}} d z=2 \mu \sigma e^{-\frac{\mu^{2}}{2 \sigma^{2}}}
\end{aligned}
$$

$$
\frac{1}{\sqrt{2} \pi} \int_{-\frac{\mu}{\sigma}}^{\infty} \mu^{2} e^{-\frac{1}{\sigma} z^{2}} d z=\mu^{2}\left[1-\Phi\left(-\frac{\mu}{\sigma}\right)\right]
$$

Now for

$$
\frac{1}{\sqrt{2} \pi} \int_{\frac{\mu}{0}}^{\infty} \sigma^{2} z^{2} e^{-\frac{1}{\partial} z^{2}} d z
$$

using intergartion ba, parts

$$
\int u d v=v u-\int v d u
$$

let

$$
\begin{aligned}
& u=z \Rightarrow d u=d v \\
& d v=z e^{-\frac{1}{\partial} z^{2}} d z \\
& v=\int_{\frac{u}{\sigma}}^{\infty} 2 e^{-\frac{1}{\partial} z^{2}} d z \\
& \omega=\frac{1}{2} z^{2} \Rightarrow d \omega=z d z
\end{aligned}
$$

then

$$
v=\int_{\frac{1}{2} \frac{\omega^{2}}{\sigma^{2}}}^{\infty} e^{-\omega} d \omega=-\left.e^{-\omega}\right|_{\frac{1}{2} \frac{\mu^{2}}{\sigma^{2}}} ^{\infty}
$$

$$
\Rightarrow v=-\left.e^{-\frac{1}{\partial} z^{2}}\right|_{\frac{\mu}{\sigma}} ^{\alpha}
$$

So

$$
\begin{aligned}
\frac{1}{\sqrt{\partial \pi}} & \int_{\frac{\mu}{\sigma}}^{\infty} \sigma^{2} z^{2} e^{-\frac{1}{\partial} z^{2}} d z \\
& -\left.\frac{2 \sigma^{2}}{\partial 2 \pi} e^{-\frac{1}{2} z^{2}}\right|_{\frac{\mu}{\sigma}} ^{\infty} \frac{\sigma^{2}}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} e^{-\frac{1}{\partial} z^{2}} d z \\
& =\frac{\mu \sigma}{\sqrt{2 \pi}} e^{-\frac{1}{2} \frac{\mu^{2}}{\sigma^{2}}}+\sigma^{2}\left[1-\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\frac{\mu}{\sigma}} e^{-\frac{1}{2} z^{2}} d z\right] \\
& =\frac{\mu \sigma}{\partial \pi} e^{-\frac{1}{2} \frac{\mu^{2}}{\sigma^{2}}} \cdot \sigma^{2}\left[1-\Phi\left(\frac{\mu}{\sigma}\right)\right]
\end{aligned}
$$

Bring thing together

$$
\begin{aligned}
= & \frac{1}{\sqrt{2} \pi} \int_{\frac{\mu}{\theta}}^{\infty} \sigma^{2} z^{2} e^{-\frac{1}{\partial} z^{2}} d z+\frac{1}{\sqrt{2} \pi} \int_{-\frac{\mu}{\theta}}^{\infty} \sigma^{2} \omega^{2} e^{-\frac{1}{\partial} \omega^{2}} d \omega \\
- & \frac{2}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\theta}}^{\infty} \mu \sigma z e^{-\frac{1}{\partial} z^{2}} d z+\frac{2}{\sqrt{\pi}} \int_{\frac{\mu}{\theta}}^{\infty} \mu \sigma \omega e^{-\frac{1}{\partial} \omega^{2}} d \omega \\
+ & \frac{1}{\sqrt{2 \pi}} \int_{-\frac{\mu}{\theta}}^{\infty} \mu^{2} e^{-\frac{1}{\partial z^{2}}} d z+\frac{1}{\sqrt{2 \pi}} \int_{\frac{\mu}{\sigma}}^{\infty} \mu^{2} e^{-\frac{1}{2} \omega^{2}} d \omega \\
= & \frac{\mu \sigma}{\sqrt{2 \pi}} e^{-\frac{1}{2} \frac{\mu^{2}}{\sigma^{2}}}+\sigma^{2}\left[1-\Phi\left(\frac{\mu}{\sigma}\right)\right] \\
& -\frac{\mu \sigma}{\sqrt{2 \pi}} e^{-\frac{1}{2} \frac{\mu^{2}}{\sigma^{2}}}+\sigma^{2}\left[1-\Phi\left(-\frac{\mu}{\sigma}\right)\right] \\
& \frac{2 \mu \sigma}{\sqrt{2 \pi}} e^{-\frac{\mu^{2}}{2 \sigma^{2}}}-\frac{2 \mu \theta}{\sqrt{2 \pi}} e^{2 \mu^{2} / 2 \sigma^{2}} \\
& +\mu^{2}\left\{\left[1-\Phi\left(-\frac{\mu}{\sigma}\right)\right]+\left[\left(-\Phi\left(\frac{\mu^{1}}{\sigma}\right)\right]\right\}\right.
\end{aligned}
$$

$$
\begin{aligned}
= & \mu^{2}\left[2-\Phi\left(-\frac{\mu}{0}\right)-\Phi\left(\frac{\mu}{0}\right)\right] \\
& +\sigma^{2}\left[2-\Phi\left(-\frac{\mu}{0}\right)-\Phi\left(\frac{\mu}{0}\right)\right] \\
= & \left(\mu^{2}+\sigma^{2}\right)\left[2-\Phi\left(-\frac{\mu}{0}\right)-\Phi\left(\frac{\mu}{0}\right)\right]
\end{aligned}
$$

Now

$$
\Phi\left(-\frac{\mu}{\sigma}\right)=1-\Phi\left(\frac{\mu}{\sigma}\right)
$$

SC

$$
\begin{aligned}
& E\left(\bar{x}^{2}\right)=\left(\mu^{2}+\sigma^{2}\right)\left[2-1+\Phi\left(\frac{\vec{\mu}}{\sigma}\right)-\Phi\left(\frac{\mu}{\sigma}\right)\right] \\
& =\mu^{2}+\sigma^{2}
\end{aligned}
$$

and

$$
\begin{aligned}
& \operatorname{Var}(\bar{X})=E\left(\bar{X}^{2}\right)-[E(\bar{X})]^{2} \\
& =\mu^{2}+\sigma^{2}-\left\{\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}\right. \\
& +\mu\left[1-2 \Phi\left(-\frac{\mu}{\sigma}\right)\right\}^{2}
\end{aligned}
$$

## Bernoulli Distribution

A Bernoulli Distribution is obtained for a discrete random variable

$$
\underline{X}=\{0,1\}
$$

with probability

$$
P(\underline{x}=1)=p \quad P(\underline{x}=0)=1-p
$$

where $p$ is called the probability mass function

$$
p \in[0,1]
$$

Now

$$
P(\underline{X}=x)=p^{x}(1-p)^{1-x} \quad x \in\{0,1\}
$$

So the mean value is

$$
\begin{aligned}
E(8) & =\sum_{x=0}^{1} x p^{x}(1-p)^{1-x} \\
& =0+p=p
\end{aligned}
$$

and the variance is

$$
\operatorname{Var}(\mathbb{Z})=E\left(\overline{\mathbb{Z}}^{2}\right)-[E(x)]^{2}
$$

and

$$
\begin{aligned}
E\left(\bar{x}^{2}\right) & =\sum_{x=0}^{1} x^{2} p^{x}(1-p)^{1-x} \\
& =P
\end{aligned}
$$

50

$$
\operatorname{Var}(X)=p-p^{2}=p(1-p)
$$

The Bernoulli Distribution is obtained by considering a sequence of $n$ independent Bernoulli random variales

$$
\left\{\underline{X}_{i}\right\}_{i=1}^{n}
$$

let

$$
\bar{X}=\sum_{i=1}^{n} \bar{X}_{i}
$$

The value of $\bar{X}$ measures the number of 1 's in the sequence

$$
\left\{\mathbb{X}_{i}\right\}_{i=1}^{n}
$$

The probability of an event
with $k$ I's in the sequence is

$$
P(E=k)=p^{k}(1-p)^{n-k}
$$

This follows from the independence of the $Z_{i}$.

There will be many events that howe $K$ I's the total number will be given by the binomial coefficient

$$
\binom{n}{k}
$$

It follows that the probability of $x$ having value $k$ is

$$
P(\underline{x}=k)=\binom{n}{k} p^{k}(1-p)^{n-k}
$$

The moment generating function is defined by

$$
E\left(e^{t 8}\right)
$$

So,

$$
E\left(e^{t \bar{x}}\right)=\sum_{k=0}^{n} e^{t k}\binom{n}{k} e^{k}(1-p)^{n-k}
$$

$$
=\sum_{k=0}^{n}\binom{n}{k}\left(p e^{t}\right)^{k}(1-p)^{n-k}
$$

This is just the expansion of the binomial

$$
\left[p e^{t}+(1-p)\right]^{n}
$$

thus

$$
\begin{aligned}
M(t) & =E\left(e^{t z}\right)=\sum_{k=0}^{n}\binom{n}{k}\left(p e^{t}\right)^{k}(1-p)^{n-k} \\
& =\left[p e^{t}+(1-p)\right]^{n} \\
& =\left[1+p\left(e^{t}-1\right)\right]^{n}
\end{aligned}
$$

The mean is given by

$$
\begin{aligned}
E(X) & =\left.\frac{d M(t)}{d t}\right|_{t=0} \\
& =\left.n\left[1+p\left(e^{t}-1\right)\right]^{n-1}\left(p e^{t}\right)\right|_{t=0} \\
& =n p
\end{aligned}
$$

The second moment by

$$
E\left(\bar{x}^{2}\right)=\left.\frac{d^{2} \mu(t)}{d t^{2}}\right|_{t=0}
$$

$$
\begin{aligned}
= & \frac{d}{d t}\left\{\left.n p e^{t}\left[1+p\left(e^{t}-1\right)\right]^{n-1}\right|_{t=0}\right. \\
= & \left\{n p e^{t}\left[1+p\left(e^{t}-1\right)\right]^{n-1}\right. \\
& \left.+n p e^{t}\left(p e^{t}\right)(n-1)\left[1+p\left(e^{t}-1\right)\right]^{n-2}\right\}\left.\right|_{t=0} \\
= & \left\{n p e^{t}\left[1+p\left(e^{t}-1\right)\right]^{n-1}\right. \\
& \left.+n(n-1)\left(p e^{t}\right)^{2}\left[1+p\left(e^{t}-1\right)\right]^{n-2}\right\}\left.\right|_{t=0} \\
= & n p+n(n-1) p^{2} \\
= & n p+n^{2} p^{2}-n p^{2} \\
= & n p(n p-p+1)
\end{aligned}
$$

It follows that the variance is

$$
\begin{aligned}
\operatorname{Var}(\underline{x}) & =E\left(q^{2}\right)-[E(x)]^{2} \\
& =n p\left(n p-p+()-(n p)^{2}\right. \\
& =(n p)^{2}-n p^{2}+n p-(n p)^{2} \\
& =n p(1-p)
\end{aligned}
$$

Tre sum

$$
\begin{aligned}
& \sum_{k=0}^{n} P(I=k) \\
= & \sum_{k=0}^{n}\binom{n}{k} P^{k}(1-p)^{n-k} \\
= & {[p+(1-p)]^{n}=1 }
\end{aligned}
$$

as expected.
The Central Limit Theorem states that the sum of random wariables

$$
\underline{X}=\sum_{i=1}^{n} \underline{X}_{n}
$$

appraches a unit normal distribution with random variable

$$
\frac{1}{\sigma \sqrt{n}}(\bar{x}-n \mu)
$$

as $n \rightarrow \infty$
So for large $n$ the Bernoull $i$ distribution approaches a unit normal destribution
with random variable

$$
\frac{1}{\sqrt{n p(1-p} \sqrt{n}}\left(x-n^{2} p\right)
$$

where

$$
\begin{aligned}
& \mu=n p \\
& o=\sqrt{n p(1-p)}
\end{aligned}
$$

## Poisson Distribution

A discrete Poisson Distribution with parameter $\lambda>0$ has the probability mass function

$$
P(\underline{X}=k)=\frac{\lambda^{k}}{k!} e^{-\lambda} \quad k=0,1,2, \ldots
$$

The moment generating function is given by

$$
\begin{aligned}
M_{X}(t) & =E\left(e^{\bar{x} t}\right)=\sum_{x} e^{x t} P(\bar{X}=x) \\
& =\sum_{k} e^{k t} \frac{\lambda^{k}}{k!} e^{-\lambda} \\
& =\sum_{k} \frac{\left(e^{t} \lambda\right)^{k}}{k!} e^{-\lambda} \\
& =e^{-\lambda} \sum_{k}\left(\frac{e^{t} \lambda}{k!}\right)^{k} \\
& =e^{-\lambda} e^{\lambda e^{t}}=e^{\lambda e^{t}-\lambda} \\
& =e^{\lambda\left(e^{t}-1\right)}
\end{aligned}
$$

The mean is

$$
\begin{aligned}
& \left.\frac{d M_{I}(t)}{d t}\right|_{t=0}=\left.\frac{d}{d t} e^{\lambda\left(e^{t}-1\right)}\right|_{t=0} \\
& =\left.\lambda e^{t} e^{\left(e^{t}-1\right)}\right|_{t=0} \\
& =\lambda
\end{aligned}
$$

The variance is

$$
\operatorname{Var}(\bar{X})=E\left({X^{2}}^{2}\right)-[E(x)]^{2}
$$

so

$$
\begin{aligned}
& E\left(x^{2}\right)=\left.\frac{d^{2} M_{I}(t)}{d t^{2}}\right|_{t=0}=\left.\frac{d^{2}}{d t^{2}} e^{\lambda\left(e^{t}-1\right)}\right|_{t=0} \\
& =\left.\frac{d}{d t}\left[\lambda e^{t} e^{\lambda\left(e^{t}-1\right)}\right]\right|_{t=0} \\
& =\left.\left[\lambda e^{t} e^{\left(e^{t}-1\right)}+\left(\lambda e^{t}\right)^{2} e^{\left(e^{t}-1\right)}\right]\right|_{t=0} \\
& =\lambda+\lambda^{2}
\end{aligned}
$$

80

$$
\operatorname{Var}(I)=\lambda+\lambda^{2}-\lambda^{2}=\lambda
$$

Show that as $n \rightarrow \infty$ with

$$
\cap p=\lambda=\text { constant }
$$

the binomial distribution appraches the Poisson distribution with parameter $\lambda$
The binomial distribution is given by

$$
\begin{aligned}
& P(x=k)=\binom{n}{k} P^{k} P^{n-k} \\
= & \frac{n!}{k!(n-k)!} P^{k}(1-p)^{n-k}
\end{aligned}
$$

Now using binomial expansion

$$
\begin{aligned}
& (1-p)^{n-k}=\sum_{j=0}^{n-k}(-1)^{j}\binom{n-k}{j} p^{j} \\
= & \binom{n-k}{0} p^{0}-\binom{n-k}{1} p^{1}+\binom{n-k}{2} p^{2}+ \\
\cdots & +(-1)^{n-k}\binom{n-k}{n-k} p^{n-k} \\
= & 1+\frac{(n-k)!}{(n-k-1)!1!} p-\frac{(n-k)!}{(n-k-2)!2!} p^{2}+\cdots+(-p)^{n-k}
\end{aligned}
$$

$$
\begin{aligned}
& =1-(n-k) p+\frac{(n-k-1)(n-k)}{2!} p^{2}+\cdots \\
& +(-1)^{j} \frac{(n-k)(n-k-1) \cdots(n-k-j+1)}{j!} p^{j}+\cdots+(-p)^{n-k}
\end{aligned}
$$

Then

$$
\begin{aligned}
& \quad P(x=k)=\binom{n}{k} P^{k}(1-p)^{n-k} \\
& =\binom{n}{k} P^{k}\left[1-(n-k) p+\frac{(n-k)(n-k-1)}{2!} p^{2}+\cdots\right. \\
& \left.+(-1)^{j} \frac{(n-k)(n-k-1) \cdots(n-k-j+1)}{j!} p^{j}+\cdots+(-p)^{n-k}\right]
\end{aligned}
$$

Now for $n \rightarrow \infty, n \gg k$

$$
\begin{aligned}
& \binom{n}{k}=\frac{n!}{k!(n-k)!}=\frac{(n-k+1)!}{k!} \\
& =\frac{n(n-1)(n-2) \cdots(n-k+1)}{k!} \\
& \rightarrow \frac{n}{k!}
\end{aligned}
$$

and

$$
\begin{aligned}
& 1-(n-k) p+\frac{(n-k-1)(n-k)}{2!} p^{2}+\cdots \\
+ & (-1)^{j} \frac{(n-k)(n-k-1) \cdots(n-k-j+1)}{j!} p^{j}+\cdots(-p)^{n-k} \\
\rightarrow & 1-n p+\frac{n^{2} p^{2}}{2!}-\frac{n^{3} p^{2}}{3!}+\cdots \\
= & 1-n p+\frac{(n p)^{2}}{2!}-\frac{(n p)^{3}}{3!}+\cdots \\
= & e^{-n p}
\end{aligned}
$$

Thus

$$
P(\bar{x}=k) \rightarrow \frac{(n p)^{k}}{k!} e^{-n p}
$$

let

$$
\lambda=n p
$$

gives the desired result

$$
P(\bar{x}=k) \approx \frac{\lambda^{k}}{k!} e^{-\lambda}
$$

## Exponential Distribution

For a continuaus random variable I the exponential distribution is defined by

$$
f_{I}(x)=\lambda e^{-\lambda x} \quad x \geqslant 0
$$

where $\lambda>0$

* Find tre mean and variance of $z$

The moment generating function

$$
\begin{aligned}
M_{\underline{x}}(t) & =E\left(e^{t \bar{x}}\right) \\
& =\int_{0}^{\infty} \lambda e^{t x} e^{-\lambda x} d x \\
& =\lambda \int_{0}^{\infty} e^{-x(\lambda-t)} d x \\
& =-\left.\frac{\lambda}{\lambda-t} e^{-x(\lambda-t)}\right|_{0} ^{\infty} \\
& =-\frac{\lambda}{\lambda-t}(0-1)=\frac{\lambda}{\lambda-t}
\end{aligned}
$$

so

$$
\begin{aligned}
E(\underline{x}) & =\left.\frac{d}{d t} \mu_{z}(t)\right|_{t=0} \\
& =\left.\frac{d}{d t}\left[\frac{\lambda}{\lambda-t}\right]\right|_{t=0} \\
& =\left.\frac{\lambda}{(\lambda-t)^{2}}\right|_{t=0} \\
& =\frac{\lambda}{\lambda^{2}}=\frac{1}{\lambda}
\end{aligned}
$$

and

$$
\begin{aligned}
E\left(\bar{x}^{2}\right) & =\left.\frac{d^{2}}{d t^{2}} M_{\bar{x}}(t)\right|_{t=0} \\
& =\left.\frac{d}{d t}\left[\frac{\lambda}{(\lambda-t)^{2}}\right]\right|_{t=0} \\
& =\left.\frac{2 \lambda}{(\lambda-t)^{3}}\right|_{t=0} \\
& =\frac{2}{\lambda^{2}}
\end{aligned}
$$

So the mean is

$$
E(\bar{x})=\frac{1}{\lambda}
$$

and the variance is

$$
\begin{aligned}
\operatorname{Var}(\bar{x}) & =E\left(\bar{\nabla}^{2}\right)-[E(\bar{x})]^{2} \\
& =\frac{2}{\lambda^{2}}-\frac{1}{\lambda^{2}} \\
& =\frac{1}{\lambda^{2}}
\end{aligned}
$$

* Find $P(\underline{X}>x)$ for $\bar{X} \sim \operatorname{Exp}(\lambda)$

$$
\begin{aligned}
P(\underline{\bar{X}} & >x)=\lambda \int_{x}^{\infty} e^{-\lambda z} d z \\
& =-\left.e^{\lambda z}\right|_{x} ^{\infty}=-\left(0-e^{-\lambda x}\right) \\
& =e^{-\lambda x}
\end{aligned}
$$

* Snow that X~Exp(N) has a memoryless property
$P(\underline{\bar{x}}>s+x \mid \underline{\bar{x}}>s)=P(\overline{\bar{x}}>x)=e^{-\lambda x}$
From the defintion of conditional probability

$$
P(\Sigma>s+x \mid \Sigma>s)=\frac{P(\Sigma>s+x, \bar{x}>s)}{P(x>s)}
$$

Now

$$
\begin{aligned}
& P(\bar{X}>s+x, \bar{X}>s)=P(\bar{X}>s+x) \\
& =\lambda \int_{s+x}^{\infty} e^{-\lambda z} d z \\
& =-\left.e^{-\lambda z}\right|_{s+x} ^{\infty}=-\left(0-e^{-\lambda(s+x)}\right) \\
& =e^{-\lambda(s+x)}
\end{aligned}
$$

and

$$
P(\bar{X}>s)=e^{-\lambda s}
$$

50
$P(\bar{X}>s+x \mid \bar{X}>s)=\frac{e^{-\lambda(s+x)}}{e^{-\lambda s}}=e^{-\lambda x}$

* For a sequence of Berroulli trials drawn from a distribution Bernoulli ( $P$ ) where $0 \leqslant P \leqslant 1$ perfomed at time $\Delta t, 2 \Delta t, \ldots$ where $\Delta t>0$ and if $I$ is the waiting time for the first success show that for

$$
\begin{gathered}
\Delta t \rightarrow 0 \text { and } p \rightarrow 0 \\
\sum_{\Delta t} \rightarrow \lambda
\end{gathered}
$$

then

$$
\bar{Y} \sim \operatorname{Exp}(\lambda)
$$

If $I$ is the waiting time. The probability of the first success after $k$ trials will be the probability of $k$ failures

$$
P(I>k \Delta t)=(1-P)^{k}
$$

let

$$
\begin{aligned}
& y=k \Delta t=>k=\frac{y}{A t} \\
& p=\lambda \Delta t
\end{aligned}
$$

$\delta s$

$$
\begin{aligned}
P(Y>Y)=(1-\lambda \Delta t)^{Y / \Delta t} \\
=\sum_{j=0}^{Y / \Delta t}\binom{Y / \Delta t}{j}(-\lambda \Delta t)^{j} \\
=\sum_{j=0}^{Y / \Delta t} \frac{(Y / \Delta t)!}{j!(Y / \Delta t-j)^{!}}(-\lambda \Delta t)^{j} \\
=1+\frac{(Y / \Delta t)^{\prime}}{(Y / \Delta t-1)!}(-\lambda \Delta t) \\
+\frac{(Y / \Delta t)^{!}}{2!(Y / \Delta t-2)!}(-\lambda \Delta t)^{2} \\
+\frac{(Y / \Delta t)!}{3!(Y / \Delta t-3)}(-\lambda \Delta t)^{3}+\cdots \\
=1+\frac{1}{1!}\left(\frac{Y}{\Delta t}\right)(-\lambda \Delta t) \\
+\frac{1}{2!}\left(\frac{Y}{\Delta t}\right)\left(\frac{Y}{\Delta t}-1\right)(-\lambda \Delta t)^{2} \\
+\frac{1}{3!}\left(\frac{Y}{\Delta t}\right)\left(\frac{Y}{\Delta t}-1 \gamma \frac{Y}{\Delta t}-2\right)^{(-\lambda \Delta t)^{3}}+\cdots
\end{aligned}
$$

$$
\begin{aligned}
= & 1-\lambda y+\frac{1}{2!}\left(\frac{y}{\Delta t}\right)^{2}\left(1-\frac{\Delta t}{y}\right)(-\lambda \Delta t)^{2} \\
& +\frac{1}{3!}\left(\frac{y}{\Delta t}\right)^{3}\left(1-\frac{\Delta t}{y}\right)\left(1-\frac{2 \Delta t}{y}\right)(-\lambda \Delta t)^{3}+\cdots \\
+ & \frac{1}{j!}\left(\frac{y}{\Delta t}\right)^{j}\left(1-\frac{\Delta t}{y}\right)\left(1-\frac{2 \Delta t}{y}\right) \cdots\left(1-\left(j-\frac{1) \Delta t}{y}\right)(-\lambda \Delta t)^{j}\right. \\
\cdots & +\cdots+\frac{1}{(y / \Delta t)!}\left(\frac{y}{\Delta t}\right)^{y / \Delta t}\left(1-\frac{\Delta t}{y}\right)\left(1-\frac{2 \Delta t}{y}\right) \cdots \\
& \left(1-\frac{(y / \Delta t-1) \Delta t}{y}\right)^{(-\lambda \Delta t)^{y-\Delta t}} \\
= & 1-\lambda y+\left(\frac{\lambda y}{2!}\left(1-\frac{\Delta t}{y}\right)\right. \\
- & \frac{1}{3!}(\lambda y)^{3}\left(1-\frac{\Delta t}{y}\right)(1-2 \Delta t)+\cdots \\
+ & \frac{1}{j!}(-\lambda y)^{j}\left(1-\frac{\Delta t}{y}\right)\left(1-\frac{2 \Delta t}{y}\right) \cdots(1-(j-1) \Delta t)+\cdots \\
+ & \frac{1}{y}(-\lambda y)^{y!}\left(1-\frac{\Delta t}{y}\right)\left(1-\frac{2 \Delta t}{y}\right) \cdots\left(\frac{\Delta t}{y}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \text { Now let } \Delta t \rightarrow 0 \text { with } y \\
& \text { fixed so that } \\
& \text { } \quad \frac{y}{\Delta t} \rightarrow \infty \\
& \begin{aligned}
P(I>y)= & 1-\lambda y+\frac{1}{2!}(\lambda y)^{2}-\frac{1}{3!}(\lambda y)^{3} \\
& +\cdots 2 \frac{1}{j!}(-\lambda y)^{j}+\cdots \\
= & \sum_{j=0}^{\infty} \frac{1}{j!}(\cdot \lambda y)^{j} \\
= & e^{-\lambda y}
\end{aligned}
\end{aligned}
$$

## Gamma Distribution

Let $U$ and $V$ be continuous independent random variables at let

$$
\underline{\underline{\omega}}=\underline{\underline{u}}+\underline{\underline{v}}
$$

Show that the probability densily function for $\omega$ can be written as convolution of the densities of $U$ and $V$

$$
f_{\underline{\underline{\omega}}}(\omega)=\int_{-\infty}^{\infty} f_{\underline{\underline{ }}}(u-\omega) f_{\underline{\underline{\omega}}}(u) d u
$$

where $f_{I}(u)$ and $f_{u}(u)$ are the probability densities for $u$ and $v$ respectivell.
True cumulative distribution function For $\underline{\underline{\omega}}$ is

$$
\begin{aligned}
& F_{\omega}(\omega)=P(\underline{\pi}+\underline{V} \leqslant \omega)= \\
& =\iint_{u+v \leqslant \omega} f_{\square \nabla}(u, v) d u d v
\end{aligned}
$$

Since $t$ and $V$ are independent

$$
P(\underline{a}+\bar{v} \leqslant \omega)=\iint_{u+v \leqslant \omega} f_{\underline{a}}(u) f_{\underline{I}}(v) d u d v
$$

but

$$
u+v=\omega \Rightarrow v=\omega-u
$$

so

$$
\begin{aligned}
& P(u+\underline{\nabla} \leqslant \omega)=\int_{-\infty}^{\infty} \int_{-\infty}^{\omega-u} f_{\underline{\square}}(u) f_{\underline{Y}}(v) d v d u \\
& =\int_{-\infty}^{\infty}\left[\int_{-\infty}^{\omega-u} f_{\underline{\nabla}}(v) d v\right] f_{\underline{\underline{L}}}(u) d u \\
& =\int_{-\infty}^{\infty} F_{\nabla}(\omega-u) f_{\square}(u) d u
\end{aligned}
$$

The density for $P(\bar{\omega} \leqslant \omega)$

$$
\begin{aligned}
& f_{\square}(\omega)=\frac{d}{d \omega} F_{\square}(\omega)=\frac{d}{d \omega} P(u+\underline{\nabla} \leqslant \omega) \\
& =\frac{d}{d \omega}\left[\int_{-\infty}^{\infty} F_{\square}(\omega-u) f_{\square}(u) d u\right] \\
& \left.=\int_{-\infty}^{\infty}\left[\frac{d}{d \omega} F_{\square}(\omega-\omega)\right)\right] f_{\square}(u) d u
\end{aligned}
$$

$$
=\int_{-\infty}^{\infty} f_{\bar{v}}(w-u) f_{u}(u) d u
$$

Let $\underline{x}_{1}, \underline{x}_{2}, \ldots, \underline{x}_{n} \sim E_{x p}(\lambda)$ be a sequence of independent and Dentically distributed random variables following an exponential distribution with common parameter $\lambda$
Show that

$$
\bar{I}=\sum_{i=1}^{n} \bar{X}_{i}
$$

has a Camma distribution

$$
\bar{I} \sim \operatorname{Gamma}(n, \lambda)
$$

with the density function

$$
f_{Y}(y)=\frac{(\lambda y)^{n-1}}{(n-1)!} \lambda e^{-\lambda y} \quad y \geqslant 0
$$

For $n=1$

$$
\underline{I}=\bar{X}
$$

50

$$
I \sim \lambda e^{-\lambda y}
$$

using the previous theorem

$$
f_{I}(y)=\int_{-\infty}^{\infty} f_{\nabla}(y-v) f_{u}(u) d u
$$

For $n=2$

$$
I=\underline{Z}_{1}+\underline{Z}_{2}
$$

50

$$
\begin{aligned}
& f_{x_{2}}\left(y-x_{1}\right)=\lambda e^{-\lambda\left(y-x_{1}\right)} \\
& f_{x_{1}}\left(x_{1}\right)=\lambda e^{-\lambda x_{1}}
\end{aligned}
$$

Since $\operatorname{Exp}(\lambda)$ is only defined for $x_{1}>0$ the integration is only defined for $0 \leqslant x_{1} \leqslant y$ so

$$
\begin{aligned}
f_{I}(y) & =\int_{0}^{y} \lambda e^{-\lambda\left(y \cdot x_{1}\right)} \lambda e^{-\lambda x_{1}} d x_{1} \\
& =\lambda^{2} e^{-\lambda y} \int_{0}^{y} d x_{1} \\
& =\lambda^{2} y e^{-\lambda y}
\end{aligned}
$$

and for

$$
I=\bar{X}_{1}+\underline{X}_{2}+\underline{X}_{3}
$$

let $Z=\underline{Z}_{1}+\underline{X}_{2}$ then

$$
I=Z_{1}+Z_{3}
$$

using the previous result

$$
f_{z}(z)=\lambda^{2} z e^{-\lambda z}
$$

ther

$$
\begin{aligned}
f_{\bar{y}}(y) & =\int_{0}^{y} f_{z_{3}}(y-z) f_{z}(z) d z \\
& =\int_{0}^{y} \lambda e^{-\lambda(y-z)} \lambda^{2} z e^{-\lambda z} d z \\
& =\lambda^{3} e^{-\lambda y} \int_{0}^{y} z d z \\
& =\frac{\lambda^{3}}{2} e^{-\lambda y} y^{2} \\
& =\frac{\lambda^{3} y^{2}}{2} e^{-\lambda y}
\end{aligned}
$$

and one more time with

$$
\begin{aligned}
\bar{Y} & =\bar{X}_{1}+\underline{X}_{2}+\bar{X}_{3}+\bar{X}_{4} \\
& =Z_{1}+\underline{X}_{4}
\end{aligned}
$$

where $\quad Z_{1}=Z_{1}+Z_{2}+\bar{X}_{3}$
so

$$
f_{z_{1}}(z)=\frac{\lambda^{3}}{2} z^{2} e^{-\lambda z}
$$

and

$$
\begin{aligned}
f_{I}(y) & =\int_{0}^{y} \lambda e^{-\lambda(y-z)} \frac{\lambda}{2}^{3} z^{2} e^{-\lambda z} d z \\
& =\frac{\lambda^{4}}{2} e^{-\lambda y} \int_{0}^{y} z^{2} d z \\
& =\frac{\lambda^{4}}{(2(3)} e^{-\lambda y} y^{3} \\
& =\frac{\lambda^{y}}{3!} y^{3} e^{-\lambda y}
\end{aligned}
$$

for a sum of $n \operatorname{Exp}(\lambda)$

$$
\bar{Y}=\sum_{i=1}^{n} \bar{X}_{i}
$$

and

$$
f_{\bar{y}}(y)=\frac{(\lambda y)^{n-1}}{(n-1)!} \lambda e^{-\lambda y}
$$

The mean and Gariance of 7 are

$$
\begin{aligned}
& E(\underline{I})=\sum_{i=1}^{n} E\left(\underline{x}_{i}\right) \\
& \operatorname{Var}(\underline{I})=\sum_{i=1}^{n} \operatorname{Var}\left(\underline{x}_{i}\right)
\end{aligned}
$$

Since the $\bar{x}_{i}$ are independent idenedically distributed Exp ( $\lambda$ )

$$
\begin{aligned}
& E(I)=\frac{n}{\lambda} \\
& \operatorname{Var}(I)=\frac{n}{\lambda^{2}}
\end{aligned}
$$

## Normal Distribution Properties

1) Show that for constants a, $L$ and $U$ such that $t>0$ and $L<U$

$$
\begin{aligned}
& \frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left(a w-\frac{w^{2}}{2 t}\right) d w \\
& =e^{\frac{1}{2} a^{2} t}\left[\Phi\left(\frac{u-a t}{\sqrt{t}}\right)-\Phi\left(\frac{L-a t}{\sqrt{t}}\right)\right]
\end{aligned}
$$

Now
u
$\frac{1}{\sqrt{2 \pi t}} \int_{L} \exp \left(a \omega \cdot \frac{\omega^{2}}{2 t}\right) d \omega$
$=\frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left[\frac{-1}{2 t}\left(\omega^{2}-2 a t \omega\right)\right] d \omega$
$=\frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left[\frac{-1}{2 t}\left(a^{2} t^{2}-a^{2} t^{2}-2 a t \omega+\omega^{2}\right)\right] d \omega$
$=\frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left[\frac{a^{2} t^{2}}{\partial t}-\frac{1}{\partial t}\left(a^{2} t^{2}-2 a t \omega+\omega^{2}\right)\right] d \omega$

$$
\begin{aligned}
& =\frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} e^{\frac{1}{2 a^{2} t}} \exp \left[\frac{1}{2 t}(\omega-a t)^{2}\right] d \omega \\
& =\frac{e^{\frac{1}{2 a^{2} t}}}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left[\frac{1}{2 t}(\omega-a t)^{2}\right] d \omega
\end{aligned}
$$

The normal cumulative distribution is defined bi

$$
\Phi\left(\frac{2-\mu}{0}\right)=\sigma_{0}^{\frac{1}{2} \pi} \int_{-\infty}^{2} \exp \left[\frac{(\omega-\mu)^{2}}{20^{2}}\right] d \omega
$$

let

$$
\mu=a t \quad s^{2}=t
$$

## then

$$
\begin{aligned}
& \Phi\left(\frac{u-a t}{\sqrt{t}}\right)=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{u} \exp \left[\frac{(\omega-a t)^{2}}{2 t}\right] d \omega \\
& \Phi\left(\frac{L-a t}{\sqrt{t}}\right)=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{L} \exp \left[\frac{(\omega-a t)^{2}}{2 t}\right] d \omega
\end{aligned}
$$

and

$$
\begin{aligned}
& \Phi\left(\frac{u-a t}{\sqrt{t}}\right)-\Phi\left(\frac{L-a t}{\sqrt{t}}\right) \\
= & \frac{1}{\sqrt{2 \pi} t} \int_{-\infty} \exp \left[\frac{(\omega-a t)^{2}}{t}\right] d \omega \\
- & \frac{1}{\sqrt{2 \pi} t} \int_{-\infty}^{L} \exp \left[\frac{(\omega-a t)^{2}}{t}\right] d \omega \\
= & \frac{1}{\sqrt{2 \pi} t} \int_{L}^{u} \exp \left[\frac{(\omega-a t)^{2}}{t}\right] d \omega
\end{aligned}
$$

Bringing things together gives, the desired result

$$
\begin{aligned}
& \frac{1}{\sqrt{2 \pi t}} \int_{L}^{u} \exp \left(a \omega-\frac{\omega^{2}}{2 t}\right) d \omega \\
& =e^{\frac{1}{2} a^{2} t}\left[\Phi\left(\frac{u-a t}{\sqrt{t}}\right)-\Phi\left(\frac{L-a t}{\sqrt{t}}\right)\right]
\end{aligned}
$$

II) Show that for

$$
\bar{X} \sim N\left(\mu, \sigma^{2}\right)
$$

and $\delta \in\{-1,1\}$

$$
\begin{aligned}
& E\left[\max \left[\delta\left(e^{\bar{x}}-k\right), 0\right]\right] \\
& =\delta e^{u+\frac{1}{2} \sigma^{2}} \Phi\left(\delta \frac{\left(\mu+\sigma^{2}-\log k\right)}{\sigma^{2}}\right) \\
& -\delta k \Phi\left(\delta \frac{(\mu-\log k)}{\sigma}\right)
\end{aligned}
$$

where $k>0$ and $\Phi$ is the normal cumulative distribution

First let $\delta=1$

$$
\begin{aligned}
& \max \left[e^{\bar{x}}-k, 0\right] \Rightarrow e^{\bar{x}}-k>0 \\
& \Rightarrow e^{\bar{x}}>k \\
& \Rightarrow \quad \bar{x}>\ln k
\end{aligned}
$$

so
$E\left[\max \left[\left(e^{\varepsilon}-k\right), 0\right]\right]=\frac{1}{\sigma \sqrt{2 \pi}} \int_{\ln k}^{\infty}\left(e^{x}-k\right) e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x$

$$
\begin{aligned}
=\frac{1}{\sigma \sqrt{2 \pi}} & \int_{\ln k}^{\infty} \exp \left[x-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x \\
& -\frac{k}{\sigma \sqrt{2 \pi}} \int_{\ln k}^{\infty} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x
\end{aligned}
$$

Let

$$
\begin{aligned}
& \omega=\frac{x-\mu}{\sigma} \Rightarrow x=\sigma \omega+\mu \\
& \Rightarrow d x=\sigma d \omega
\end{aligned}
$$

$$
\begin{aligned}
& E\left[\max \left[\left(e^{\bar{x}}-k, 0\right)\right]\right]=\frac{1}{\sigma \sqrt{2 \pi}} \int_{\ln \frac{k-\mu}{\sigma}}^{\infty} e^{\left(\sigma \omega+\mu-\frac{1}{2} \omega^{2}\right)} \sigma d \omega \\
& -\frac{k}{\sigma \sqrt{2 \pi}} \int_{\ln \frac{k-\mu}{\sigma}}^{\infty} e^{-\frac{1}{2 \omega^{2}} \sigma d \omega} \\
& =\frac{1}{2 \pi} \int_{\ln \frac{k-\mu}{\sigma}}^{\infty} e^{\mu} e^{-\frac{1}{2}\left(\omega^{2}-2 \sigma \omega+\sigma^{2}-\sigma^{2}\right)} \\
& -\frac{k}{\sqrt{2 \pi}} \int_{\ln \frac{k-\mu}{\sigma}} e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{e^{\mu-\frac{1}{2} \sigma^{2}} \int_{\ln \frac{k-\mu}{\sigma}}^{\infty} e^{-\frac{1}{2}(\omega-\sigma)^{2}} d \omega}{\sqrt{2 \pi}} \\
& =\frac{k}{\sqrt{2 \pi}} \int_{\ln \frac{k-\mu}{\sigma}}^{\infty} e^{-\frac{1}{a} \omega^{2}} d \omega
\end{aligned}
$$

Now let

$$
z=\omega-\sigma \Rightarrow \quad d z=d \omega
$$

then

$$
\begin{aligned}
& E\left[\max \left[\left(e^{\bar{x}}-k\right), 0\right]\right]=\frac{e^{\mu-\frac{1}{2} \sigma^{2}}}{\sqrt{2 \pi}} \int_{\frac{\ln k-\mu-\sigma^{2}}{\sigma}}^{\infty} e^{-\frac{1}{2} z^{2}} d z \\
& -\frac{k}{\sqrt{2 \pi}} \int_{\frac{\ln k-\mu}{\sigma}}^{\infty} e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

since the distribution is symmetric about 0

$$
\begin{aligned}
& =e^{\mu-\frac{1}{2} \sigma^{2}} \int_{\sqrt{2} \pi}^{-\left(\ln k-\mu-\sigma^{2}\right)} e^{-\frac{1}{2} z^{2}} d z \\
& \quad-\frac{k}{\sqrt{2} \pi} \int_{-\infty}^{-(\ln k-\mu)} e^{-\frac{1}{2} \omega^{2}} d \omega
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{e^{\mu-\frac{1}{2} \sigma^{2}} \int_{\frac{-\infty}{\sqrt{2 \pi}} \int^{\frac{\sigma^{2}+\mu-\ln k}{\sigma}} e^{-\frac{1}{2} z^{2}} d z}^{\mu-\frac{\ln k}{\sigma} e^{-\frac{1}{2} \omega^{2}} d \omega}}{} \quad-\frac{k}{\sqrt{2 \pi}} \int_{-\infty}^{0} e^{\mu-\frac{1}{2} \sigma^{2}} \Phi\left(\frac{\sigma^{2}+\mu-\ln k}{\sigma}\right)-k \Phi\left(\frac{\mu-\ln k}{\sigma}\right)
\end{aligned}
$$

now if $\delta=-1$ we have

$$
E\left[\max \left[\left(k-e^{\underline{X}}\right), 0\right]\right.
$$

So

$$
\begin{aligned}
& k-e^{\bar{x}}>0 \Rightarrow k>e^{\bar{x}} \\
& \Rightarrow \ln k>\underline{x}
\end{aligned}
$$

This will be the same a the first result with different integration limits

$$
\begin{aligned}
E\left[\max \left[\left(k-e^{\bar{x}}\right), 0\right]\right]= & \frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty} \exp \left[x-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x \\
& -\frac{k}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\ln k} \exp \left[\frac{-(x-\mu)^{2}}{2 \sigma^{2}}\right] d x
\end{aligned}
$$

making use of the previous result

$$
\begin{aligned}
& E\left[\max \left[\left(e^{\bar{x}}-k\right), 0\right]\right]=\frac{e^{\mu-\frac{1}{2} \sigma^{2}}}{\sqrt{2 \pi}} \int_{-\infty}^{\frac{\ln k-\mu}{\sigma} e^{-\frac{1}{2} z^{2}}} d z \\
& -\frac{k}{\sqrt{2 \pi}} \int_{-\infty}^{\ln \frac{k-\mu}{\sigma}} e^{-\frac{1}{2} \omega^{2}} d \omega \\
& =e^{\mu-\frac{1}{2} \sigma^{2}} \Phi\left(\frac{\ln k-\mu-\sigma^{2}}{\sigma}\right)-\frac{k}{\sqrt{2 \pi}} \Phi\left(\frac{\ln k-\mu}{\sigma}\right)
\end{aligned}
$$

Thus
$E\left[\max \left[\delta\left(e^{\bar{x}}-k\right), 0\right]=e^{\mu-\frac{1}{2} \sigma^{2}} \Phi\left[\frac{\delta\left(\sigma^{2}+\mu-\ln k\right)}{\sigma}\right]\right.$

$$
\left.-k \Phi\left[\delta\left(\frac{\mu-\ln k}{\sigma}\right)\right)\right]
$$

which is the desired result

## Properties of Indicator Functions

Suppose $\Omega$ is a set with

$$
\omega \in \Omega
$$

and let

$$
A \subseteq \Omega
$$

the indicator function of $A$ is defined by

$$
I_{A}(\omega)= \begin{cases}1 & \omega \in A \\ 0 & \omega \notin A\end{cases}
$$

That is $I_{A}(\omega)$ indicate if $\omega$ is an elelement of $A$.

Some properties of $I_{A}(w)$ are

1) $I_{A}(\omega)=1-I_{A^{c}}(\omega)$ where $A^{c}$ is the compliment of $A^{c}$.
2) $I_{A}^{2}(\omega)=I_{A}(\omega)$
3) $I_{A \cap B}(\omega)=I_{A}(\omega) \cdot I_{B}(\omega)$
4) $I_{A \cup B}(\omega)=I_{A}(\omega)+I_{B}(B)-I_{A \cap B}(\omega)$
5) $\left.I_{A_{1} \cup A_{2} \cup \ldots \cup A_{n}}=\max \left\{I_{A_{1}}(\omega), I_{A_{2}}(\omega), \ldots, I_{x_{n}(\omega)}\right)\right\}$

* Proof of 1 .

From the definition of the indicator function

$$
I_{A^{c}}(\omega)= \begin{cases}1 & \omega \in A^{c} \\ 0 & \omega \notin A^{c}\end{cases}
$$

from the definition of the compliement

$$
\omega \in A^{c} \Rightarrow \omega \notin A
$$

so

$$
I_{A}(\omega)= \begin{cases}1 & \omega \in A \\ 0 & \omega \notin A\end{cases}
$$

thus

$$
I_{A}(\omega)=1-I_{A^{c}}(\omega)
$$

* Proof of 2.
from the definition of $I_{A}(\omega)$ if $\omega \in A$
$I_{A}{ }^{2}=I_{A}(\omega) \cdot I_{A}(\omega)=(1)(1)=1=I_{A}(\omega)$
and if $\omega \notin A$
$I_{A}{ }^{2}(\omega)=I_{A}(\omega) \cdot I_{A}(\omega)=0=I_{A}(\omega)$
Trues

$$
I_{A}^{2}(\omega)=I_{A}(\omega)
$$

* Proof of 3 .

From the defintion of an indicator function

$$
I_{A \cap B}(\omega)= \begin{cases}1 & \omega \in A \cap B \\ 0 & \omega \notin A \cap B\end{cases}
$$

From the defintion of intersection

$$
\omega \in A \cap B \Rightarrow \omega \in A \text { and } \omega \in B
$$

and

$$
\omega \notin A \cap B \Rightarrow \omega \notin A \text { or } \omega \notin B
$$

Trus for $w \in A \cap B$

$$
I_{A \cap B}(\omega)=1=I_{A}(\omega) I_{B}(\omega)
$$

and for $\omega \notin A \cap B$

$$
I_{A \cap B}(\omega)=0=I_{A}(\omega) I_{B}(\omega)
$$

* Proof of 4 .

From the definition of the indicator function

$$
I_{A \cup B}(\omega)= \begin{cases}1 & \omega \in A \cup B \\ 0 & \omega \notin A \cup B\end{cases}
$$

From the detinition of union

$$
\begin{aligned}
& \omega \in A \cup B \Rightarrow \omega \in A \text { or } \omega \in B \\
& \omega \notin A \cup B \Rightarrow \omega \notin A \text { and } \omega \notin B
\end{aligned}
$$

so first assume that $\omega \in A$ and $\omega \in B$ then
$I_{A \cup B}(\omega)=1$
$I_{A}(\omega)+I_{B}(\omega)-I_{A \cap B}(\omega)=1+1-1=1$
if $\omega \in A$ and $\omega \notin B$
$I_{A \cup B}(\omega)=1$
$I_{A}(\omega)+I_{B}(\omega)-I_{A \cap B}(\omega)=1+0-0=1$
if $\omega \notin A$ and $\omega \in B$
$I_{A \cup B}(\omega)=1$
$I_{A}(\omega)+I_{B}(\omega)-I_{A \cap B}(\omega)=0+1-0=1$ and finally
if $\omega \notin A$ and $\omega \notin B$
$I_{A \cup B}(\omega)=0$
$I_{A}(\omega)+I_{B}(\omega)-I_{A \cap B}(\omega)=0+0-0=0$
Trues
$I_{A \cup B}(\omega)=I_{A}(\omega)+I_{B}(\omega)-I_{A \cap B}(\omega)$

* Proof of 4.

From the definition of the indicator function

$$
I_{A_{1} \cup A_{2} \cup \cdots \cup A_{n}}(\omega)= \begin{cases}1 & \omega \in A_{1} \cup A_{2} \cup \cdots \cup A_{n} \\ 0 & \omega \in A_{1} \cup A_{2} \cup \cdots \cup A_{n}\end{cases}
$$

From the defintion of union
$\omega \in A_{1} \cup A_{2} \cup \cdots \cup A_{n} \Rightarrow \omega \in A_{1}$ or $\omega \in X_{2}$ or $\ldots . . \omega \in A n$
$\omega \notin A_{1} \cup A_{2} \cup \cdots \cup A_{n} \Rightarrow \omega \notin A_{1}$ and $\omega \notin A_{2}$ and ... $\omega \in A_{n}$

So if $w \in A_{1} \cup A_{2} \cup \cdots A_{n}$
then $w$ is in at least 1 of
An So
$I_{A_{1} \cup A_{2} \cup \cdots \cup A_{n}}=\max \left[I_{A_{1}}(\omega), I_{A_{2}}(\omega), \ldots, I_{A_{n}}(\omega)\right]$
and if $\omega \notin A_{1} \cup A_{2} \cup \cdots A_{n}$ then
$\omega$ is not in any of $A_{1}, A_{0}, \ldots, A_{n}$
80

$$
I_{A_{n}}(\omega)=0 \quad \forall A_{n}
$$

and
$I_{A_{1} \cup A_{2} \cup \cdots A_{n}}(\omega)=0=\max \left[I_{A_{1}}(\omega), I_{A_{2}}(\omega), \ldots\right. \left.I_{A_{n}}\right]$

## Properties of Expectations

* Markou's Inequality

Let $\frac{X}{\text { be a non-negative random }}$ variable with mean $\mu$. For $a>0$ snow

$$
P(\bar{x} \geqslant a) \leqslant \frac{\mu}{a}
$$

Let

$$
I(x \geqslant a)= \begin{cases}1 & \Sigma \geqslant a \\ 0 & \text { otherwise }\end{cases}
$$

since $\bar{X} \geqslant 0$ and $a>0$

$$
I_{(X \geqslant a)} \leqslant \frac{X}{a}
$$

So

$$
E(\mathbb{I}(x \geqslant a)) \leqslant \frac{E(x)}{a}
$$

and

$$
\begin{aligned}
& E\left(\mathbb{I}_{\bar{x} \geqslant a}\right)=(1) P(\underline{x} \leqslant a)+(0) P(\bar{x}>a) \\
& =P(\underline{x} \leqslant a)
\end{aligned}
$$

50

$$
P(\underline{x} \geqslant a) \leqslant \frac{\mu}{a}
$$

and since

$$
P(\underline{x} \geqslant a)=1-F_{\underline{x}}(a) \leqslant \frac{\mu}{a}
$$

* Chebysheu's Inequality

Let $\bar{X}$ be a random variable with mean $\mu$ and variance $\sigma^{2}$. For $k>0$ show that

$$
P(|z-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

if $|\bar{X}-\mu| \geqslant k$ then $(X-\mu)^{2} \geqslant k^{2}$
using Markov's inequality

$$
P\left[(X-\mu)^{2} \geqslant k^{2}\right] \leqslant \frac{E\left[(\bar{X}-\mu)^{2}\right]}{k^{2}}
$$

but

$$
E\left[(\bar{x}-\mu)^{2}\right]=\sigma^{2}
$$

Since $k>0$

$$
(\bar{x}-\mu)^{2} \geqslant k^{2} \Rightarrow|\bar{x}-\mu|>k
$$

then

$$
P(|x-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

* Show that if $\bar{X}$ is a random variable greater than or equal to o then

$$
E(I)=\sum_{x=0}^{\infty} P(\mathbb{X}>x)
$$

If I is discrete, and

$$
E(\bar{X})=\int_{0}^{\infty} P(\bar{X}>x) d x
$$

if $I$ is continuous
Now

$$
E(X)=\sum_{y=0}^{\infty} y P(Z=y)
$$

using

$$
y=\sum_{x=0}^{y} 1
$$

so

$$
E(\bar{X})=\sum_{y=0}^{\infty} \sum_{x=0}^{y} P(\bar{X}=y)
$$

The summation indicies
satisfy The sum
satisfy

$$
0 \leq x \leq y
$$

where $y=1,2,3, \ldots$
switning the order of
summation

$$
\sum_{x=0}^{\infty} \sum_{y=x}^{\infty} P(\bar{x}=y)
$$

but

$$
P(\bar{X} \geqslant x)=\sum_{y=x}^{\infty} P(\underline{X}=y)
$$

50

$$
E(\bar{X})=\sum_{x=0}^{\infty} P(X \geqslant x)
$$

For the continous case

$$
E(\bar{x})=\int_{0}^{\infty} y f_{X}(y) d y
$$

using

$$
y=\int_{0}^{y} d x
$$

gives

$$
\begin{aligned}
E(\underline{x}) & =\int_{0}^{\infty}\left[\int_{0}^{y} d x\right] f_{\underline{z}}(y) d y \\
& =\int_{0}^{\infty} \int_{0}^{y} f_{x}(y) d x d y
\end{aligned}
$$

## using

$$
0 \leq x \leq y
$$

to change integration limits gives

$$
E(\Sigma)=\int_{0}^{\infty} \int_{x}^{\infty} f_{x}(y) d y d x
$$

but

$$
P(X \geqslant x)=\int_{x}^{\infty} f_{X}(y) d y
$$

so

$$
E(\bar{x})=\int_{0}^{\infty} P(\bar{x} \geqslant x) d x
$$

## Hölder's Inequality

Let $\alpha, \beta \geqslant 0$ and for $p, q \geqslant 1$ such that

$$
\frac{1}{p}+\frac{1}{q}=1
$$

Show the following inequality

$$
\alpha \beta \leqslant \frac{\alpha^{D}}{p}+\frac{\beta^{G}}{q}
$$

and then if $I$ and $I$ are a pair of jointly continuous variables

$$
E(|\underline{x}|) \leqslant\left[E\left(\left|\nabla^{p}\right|\right)\right]^{1 / p}\left[E\left(\left|y^{q}\right|\right)\right]^{1 / q}
$$

For $\alpha=\beta=0$ the inequality clearly hodds

$$
0 \leqslant 0+0=0
$$

let

$$
\alpha=e^{x / p} \quad \beta=e^{v / q}
$$

where $x, y \in \mathbb{R}$ then,

$$
\alpha \beta=e^{x / \rho+y / a}
$$

now since $\quad l=\frac{1}{p}+\frac{1}{q}$ let $\lambda=\frac{1}{p}$ then $\quad 1-\lambda=\frac{1}{9}$ where $\lambda<1$ so

$$
\alpha \beta=e^{x \lambda+y(1-\lambda)}
$$

since this is a convex function for an arbitrary pant $x \leqslant z \leqslant y$ parameterized by $\lambda$

$$
z=x \lambda+(1-\lambda) y=y-\lambda(y-x)
$$

![](https://cdn.mathpix.com/cropped/2025_09_18_5b0b83ca8a26677bce68g-087.jpg?height=682&width=926&top_left_y=879&top_left_x=272)
for the line between $f(x)$ and $f(y)$

$$
\begin{aligned}
& F(z)=f(x)+(z-x) \frac{[f(y)-f(x)]}{(y-x)} \\
= & f(x)+\frac{\{[y-\lambda(y-x)]-x\}}{y-x}[f(y)-f(x)] \\
= & f(x)+\frac{[(y-x)-\lambda(y-x)]}{y-x}[f(y)-f(x)] \\
= & f(x)+\frac{(y-x)(1-\lambda)}{y-x}[f(y)-f(x)] \\
= & f(x)+(1-\lambda)[f(y)-f(x)] \\
= & f(x)-(1-\lambda) f(x)+(1-\lambda) f(y) \\
= & \lambda f(x)+(1-\lambda) f(y)
\end{aligned}
$$

For a convex function

$$
f(2) \leqslant E(2)
$$

so
$\Rightarrow f(x \lambda-(1-\lambda) x) \leqslant \lambda f(x)+(1-\lambda) f(y)$
Now using

$$
f(z)=e^{z}
$$

$$
e^{x \lambda+y(\lambda-1)}=\lambda e^{x}+(1-\lambda) e^{y}
$$

vecalling that

$$
\lambda=\frac{1}{p} \quad 1-\lambda=\frac{1}{q}
$$

gives

$$
e^{x / p} e^{y / q} \leqslant \frac{e^{x}}{p}+\frac{e^{y}}{q}
$$

and

$$
\begin{array}{ll}
\alpha=e^{x / p} & \beta=e^{y / q} \\
e^{x}=\alpha^{p} & e^{y}=\beta^{q}
\end{array}
$$

the desired result is obtained

$$
\alpha \beta \leqslant \frac{\alpha^{p}}{p}+\frac{\beta^{q}}{q}
$$

show that

$$
E(|\underline{X}| \mid) \leqslant\left[E\left(\left|\nabla^{p}\right|\right)\right]^{1 / p}\left[E\left(\left|y^{q}\right|\right)\right]^{1 / q}
$$

Let

$$
\alpha=\frac{|\bar{x}|}{E\left[\left|x^{p}\right|\right]^{1 / p}} \quad \beta=\frac{|\bar{y}|}{E\left[\left|Y^{q}\right|\right]^{1 / q}}
$$

50

$$
\begin{aligned}
& \alpha \beta \leqslant \frac{\alpha^{p}}{p}+\frac{\beta^{q}}{q} \\
\Rightarrow & \frac{|\bar{X} I|}{E\left[\left|X^{p}\right|\right]^{1 / p} E\left[\left|I^{q}\right|\right]^{1 / q}} \leqslant p \frac{|\bar{I}|^{p}}{p\left[\left|X^{p}\right|\right]}+\frac{|\bar{I}|^{q}}{q E\left[\left|I^{q}\right|\right]}
\end{aligned}
$$

Taking expectation gives

$$
\begin{aligned}
& \frac{E[|\bar{X} \bar{Y}|]}{E\left[\bar{I}^{p} \mid\right]^{1 / p} E\left[\left|\bar{I}^{q}\right|\right]^{1 / q}} \leqslant \frac{E\left[|\bar{X}|^{p}\right]}{p E\left[\left|\bar{I}^{p}\right|\right]} \\
& +\frac{E\left[|\bar{Y}|^{q}\right]}{q E\left[|\bar{I}|^{q}\right]} \\
& =\frac{1}{p}+\frac{1}{q}=1
\end{aligned}
$$

50

$$
E[|\mathbb{Z} I|] \leqslant E\left[\left|\mathbb{D}^{p}\right|\right]^{1 / p} E\left[\left|\mathbb{Z}^{q}\right|\right]^{1 / a}
$$

## * Minkowski Inequality

Let I and I be a pair of jointly continuous random variables. snow that
$\left\{E\left(|\underline{x}+\bar{y}|^{p}\right)\right\}^{1 / p} \leqslant\left\{E\left(|\bar{x}|^{p}\right)\right\}^{1 / p}+\left\{E\left(|\bar{y}|^{p}\right)\right\}^{1 / p}$
since $\bar{X}$ and $\bar{I}$ can take on any values

$$
E(|\bar{X}+\bar{Y}|) \leqslant E(|\bar{X}|)+E(|Y|)
$$

Now

$$
\begin{aligned}
& E\left(|Z+I|^{P}\right)=E\left(|Z+I||Z+I|^{P-1}\right) \\
& \quad \leqslant E\left(|Z||Z+I|^{P-1}\right)+E\left(|Z||Z+I|^{P-1}\right)
\end{aligned}
$$

From Holder's inequality

$$
E(|\underline{x} \mp|) \leqslant\left[E\left(|\underline{x}|^{p}\right)\right]^{1 / p}\left[E\left(|I|^{q}\right)\right]^{1 / q}
$$

It is seen that
$E\left(|\underline{x}||\underline{x}+\underline{y}|^{p-1}\right) \leqslant\left[E\left(|\underline{x}|^{p}\right)\right]^{1 / p}\left[E\left(|\underline{x}+I|^{q(p-1)}\right]^{1 / q}\right.$ similarly
$E\left[|q||z+Z|^{p-1}\right] \leqslant\left[E\left(|I|^{p}\right]^{1 / p}\left[E\left(|x+\bar{Y}|^{q(p-1)}\right]^{1 / q}\right.\right.$
50
$E\left(|X+I|^{p}\right) \leqslant\left[E\left(|X|^{p}\right)\right]^{1 / p}\left[E\left(|X+I|^{q(p-1)}\right]^{1 / q}\right.$
$+\left[E\left(|I|^{p}\right]^{1 / p}\left[E\left(|X+Y|^{q(p-1)}\right]^{1 / q}\right.\right.$
$=\left[E\left(|\mathbb{X}|^{p}\right)\right]^{1 / p}$
using

$$
\begin{aligned}
& \frac{1}{p}+\frac{1}{q}=1 \Rightarrow \frac{1}{q}=1-\frac{1}{p} \\
\Rightarrow & \frac{p}{q}=p-1 \\
\Rightarrow & p=q(p-1)
\end{aligned}
$$

so

$$
\begin{aligned}
& E\left(|\bar{X}+\underline{Y}|^{P}\right) \leqslant\left[E\left(|\bar{X}|^{P}\right)\right]^{1 / P}\left[E\left(|\bar{I}+I|^{P}\right)\right]^{1 / q} \\
&+\left[E\left(|\mathbb{Y}|^{P}\right)\right]^{1 / P}\left[E\left(|\bar{X}+I|^{P}\right)\right]^{1 / q} \\
&=\left[E\left(|\bar{X}+\bar{Y}|^{P}\right)\right]^{1 / q}\left\{\left[E\left(|\bar{Y}|^{P}\right)\right]^{1 / P}+\left[E\left(|Y|^{P}\right)\right]^{1 / P}\right\}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & E\left(|\underline{Z}+I|^{P}\right)\left[E(\underline{X}+\underline{Y})^{P}\right]^{-1 / q} \leqslant \\
& E\left(|\underline{X}|^{P}\right)^{1 / P}+E\left(|I|^{P}\right)^{1 / P} \\
\Rightarrow & {\left[E\left(|\bar{X}+I|^{P}\right)\right]^{1-1 / q} \leqslant E\left(|\underline{X}|^{P}\right)^{1 / P} } \\
& +E\left(|I|^{P}\right)^{1 / P}
\end{aligned}
$$

but

$$
\frac{1}{p}=1-\frac{1}{q}
$$

50

$$
\left[E\left(|\bar{X}+\underline{Y}|^{D}\right)\right]^{1 / P} \leqslant E\left(|\bar{X}|^{P}\right)^{1 / P}+E(|I| P)^{1 / P}
$$

## Another Convex Function Inequality

![](https://cdn.mathpix.com/cropped/2025_09_18_5b0b83ca8a26677bce68g-094.jpg?height=695&width=1098&top_left_y=235&top_left_x=207)

Consider the convex function $\varphi(2)$ and the line tangent at $\varphi(y)$

$$
L(z)=\varphi(y)+(y-z) \varphi^{\prime}(y)
$$

at $z=x$

$$
L(x)=\varphi(y)+(y-x) \varphi^{\prime}(y)
$$

but

$$
\varphi(x) \geqslant L(x)
$$

So

$$
\varphi(x) \geqslant \varphi(y)+(y-x) \phi^{\prime}(y)
$$

## Moment Generating Function for Normal Distribution

The moment generating function for a distribution is defined

$$
M(t)=E\left(e^{t \underline{X}}\right)
$$

for a Normal distribution

$$
P(x)=\frac{1}{602 \pi} \exp \left[\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right]
$$

50

$$
\begin{aligned}
& \mu(t)=E\left(e^{t x}\right)=\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{t x} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left[t x-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right]^{1} x \\
& =\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left\{\frac{1}{2 \sigma^{2}}\left[2 \sigma^{2} t x-(x-\mu)^{2}\right]\right\} d x
\end{aligned}
$$

Consider the exponential term

$$
\begin{aligned}
& 2 \sigma^{2} t x-(x-\mu)^{2}=2 \sigma^{2} t x-x^{2}+2 \mu x-\mu^{2} \\
= & -x^{2}+2 x\left(\sigma^{2} t+\mu\right)-\mu^{2} \\
= & -x^{2}+2 x\left(\sigma^{2} t+\mu\right)-\mu^{2}+\left(\sigma^{2} t+\mu\right)^{2} \\
& -\left(\sigma^{2} t+\mu\right)^{2} \\
= & -x^{2}+2 x\left(\sigma^{2} t+\mu\right)-\left(\sigma^{2} t+\mu\right)^{2} \\
& -\mu^{2}+\left(\sigma^{2} t+\mu\right)^{2} \\
= & -x^{2}+2 x\left(\sigma^{2} t-\mu\right)-\left(\sigma^{2} t-\mu\right)^{2} \\
& -\mu^{2}+\left(\sigma^{2} t\right)^{2}+2 \mu \sigma^{2} t+\mu^{2} \\
= & -x^{2}+2 x\left(\sigma^{2} t-\mu\right)-\left(\sigma^{2} t-\mu\right)^{2} \\
& +\sigma^{2} t\left(\sigma^{2} t+2 \mu\right) \\
= & -\left(x-\sigma^{2} t+\mu\right)^{2}+\sigma^{2} t\left(\sigma^{2} t+2 \mu\right) \\
= & -\left(x+\mu-\sigma^{2} t\right)^{2}+\sigma^{2} t\left(\sigma^{2} t+2 \mu\right)
\end{aligned}
$$

so the integral beromes
$\frac{1}{\sigma \sqrt{2 \pi}} \int_{-\infty}^{\infty} \exp \left[\frac{\left(x+\mu-\sigma^{2} t\right)^{2}+\sigma^{2} t\left(\sigma^{2} t+2 \mu\right)}{2 \sigma^{2}}\right] d x$

$$
\begin{aligned}
& =\frac{1}{\sigma \sqrt{2} \pi} \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \int_{-\infty}^{\infty} \exp \left[\frac{\left(x+\mu-\sigma^{2} t\right)^{2}}{2 \sigma^{2}}\right] d x \\
& =\frac{1}{\sigma \sqrt{2} \pi} \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \sigma \sqrt{2 \pi} \\
& =\exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
\end{aligned}
$$

Thus the moment generating function

$$
M(t)=\exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
$$

So the first moment is

$$
E(x)=\left.\frac{d \mu(t)}{d t}\right|_{t=0}
$$

and

$$
\frac{d M}{d t}=\left[\frac{1}{2}\left(\sigma^{2} t+2 \mu\right)+\frac{\sigma^{2} t}{2}\right] \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
$$

so

$$
E(\bar{x})=\left.\frac{d \mu}{d t}\right|_{t=0}=\mu
$$

The second moment is

$$
\begin{aligned}
& \frac{d^{2} \mu}{d t^{2}}=\frac{d}{d t}\left(\sigma^{2} t+\mu\right) \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
& =\sigma^{2} \exp \left[\frac{t}{2}\left(\sigma^{2} t-2 \mu\right)\right] \\
& +\left(\sigma^{2} t+\mu\right)\left[\frac{1}{2}\left(\sigma^{2} t+2 \mu\right)+\frac{1}{2} \sigma^{2} t\right] \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
& =\left\{\sigma^{2}+\left(\sigma^{2} t+\mu\right)\left[\frac{1}{2}\left(\sigma^{2} t+2 \mu\right)+\frac{1}{2} \sigma^{2} t\right]\right\} \\
& \quad \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
& =\left[\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \exp \left[\frac{t}{2}\left(\sigma^{2}+2 \mu\right)\right] \\
& s o \\
& E\left(\pi^{2}\right)=\left.\frac{d \mu^{2}}{d t^{2}}\right|_{t=0}=\sigma^{2}+\mu^{2}
\end{aligned}
$$

and Finally the third moment is
$\frac{d^{3} M}{d t^{3}}=\frac{d}{d t}\left\{\left[\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \exp \left[\frac{t}{J}\left(\sigma^{2} t+\mu\right)\right]\right.$

$$
\begin{aligned}
= & {\left[2\left(\sigma^{2} t+\mu\right) \sigma^{2}\right] \exp \left[\frac{t}{2}\left(\sigma^{2}+2 \mu\right)\right] } \\
+ & {\left[\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\left[\sigma^{2} \frac{t+\mu}{2}+\frac{\sigma^{2} t}{2}\right] } \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
= & \left\{2 \sigma^{2}\left(\sigma^{2} t+\mu\right)+\left[\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\left(\sigma^{2} t+\mu\right)\right\} \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
= & \left\{2 \sigma^{2}\left(\sigma^{2} t+\mu\right)+\left(\sigma^{2} t+\mu\right)\left[\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\right\} \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
= & \left(\sigma^{2} t+\mu\right)\left[2 \sigma^{2}+\sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right] \\
= & \left(\sigma^{2} t+\mu\right)\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
\end{aligned}
$$

50

$$
\begin{gathered}
\frac{d^{3} \mu}{d t^{3}}=\left(\sigma^{2} t+\mu\right)\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \\
\exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
\end{gathered}
$$

$$
E\left(\nabla^{3}\right)=\left.\frac{d^{3} \mu}{d t^{3}}\right|_{t=0}=\mu\left(36^{2}+\mu^{2}\right)
$$

For

$$
\begin{aligned}
& E\left(\delta^{4}\right)=\left.\frac{d^{4} \mu}{d t^{4}}\right|_{t=0} \\
& =\frac{d}{d t}\left\{\begin{array}{l}
\left(\sigma^{2} t+\mu\right)\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right] \\
\left.\exp \left[\frac{1}{2}\left(\sigma^{2} t+2 \mu\right)\right]\right\}
\end{array}\right. \\
& =\left\{\sigma^{2}\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\right. \\
& +\left(\sigma^{2} t+\mu\right) 2\left(\sigma^{2} t+\mu\right) \sigma^{2} \\
& \left.+\left(\sigma^{2} t+\mu\right)\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\left[\frac{1}{2}\left(\sigma^{2} t+2 \mu\right)+\frac{1}{2} \sigma^{2} t\right]\right\} \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & \left\{\sigma^{2}\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]+2 \sigma^{2}\left(\sigma^{2}+\mu\right)^{2}\right. \\
& \left.+\left(\sigma^{2} t+\mu\right)^{2}\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\right\} \\
& \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right]\right. \\
= & \left\{\sigma^{2}\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]+\left(\sigma^{2} t+\mu\right)^{2}\left[2 \sigma^{2}\right.\right. \\
+ & \left.\left.3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]\right\} \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right]\right. \\
= & \left\{\sigma^{2}\left[3 \sigma^{2}+\left(\sigma^{2} t+\mu\right)^{2}\right]+\left(\sigma^{2} t+\mu\right)^{2}\left[5 \sigma^{2}\right.\right. \\
& \left.\left.+\left(\sigma^{2} t+\mu\right)^{2}\right]\right\} \exp \left[\frac{t}{2}\left(\sigma^{2} t+2 \mu\right]\right. \\
\text { So } & E\left(\sigma^{4}\right)=\left.d^{4} \mu\right|_{t=0}=\sigma^{2}\left(3 \sigma^{2}+\mu^{2}\right) \\
= & \mu^{2}\left(5 \sigma^{2}+\mu^{2}\right) \\
= & 3 \sigma^{4}+\sigma^{2} \mu^{2}+5 \mu^{2} \sigma^{2}+\mu^{(1} \\
= & 3 \sigma^{4}+6 \mu^{2} \sigma^{2}+\mu^{4} \\
= & 3 \sigma^{4}+\mu^{2}\left(6 \sigma^{2}+\mu^{2}\right)
\end{aligned}
$$

## Random Walk

A 1 dimensional Random Walk is defined by the random variable

$$
\begin{array}{r}
\underline{Z}_{i}=\{-1,1\} \quad i=0,1,2,3, \ldots, \cap \\
P\left(Z_{i}=1\right)=P \quad P\left(\underline{X}_{i}=-1\right)=1-P \quad \underline{X}_{0}=0
\end{array}
$$

Now

$$
\begin{aligned}
& \qquad \begin{aligned}
& E\left(\bar{x}_{i}\right)= p(1)+(1-p)(-1) \\
&= p-1+p \\
&= 2 p-1 \\
& E\left(\bar{x}_{i}^{2}\right)= p(1)+(1-p)(1) \\
&= p+1-p=1 \\
& \text { for } i \neq j \text { and } \bar{x}_{i} \Perp \bar{x}_{1} \\
& E\left(\bar{x}_{i} \bar{x}_{j}\right)=(1)(1) p^{2}+(-1)(1)(1-p) p \\
&+(1)(-1) p(1-p) \\
&+(-1)(-1)(1-p)(1-p)
\end{aligned}
\end{aligned}
$$

$$
\begin{aligned}
& =p^{2}-(1-p) p-p(1-p)+(1-p)^{2} \\
& =p^{2}-p+p^{2}-p+p^{2}+p^{2}-2 p+1 \\
& =4 p^{2}-4 p+1 \\
& =4 p(p-1)+1
\end{aligned}
$$

Let

$$
\begin{aligned}
& n_{+}=\text {number steps where } \bar{X}_{i}=1 \\
& n_{-}=\text {number steps where } \bar{X}_{i}=-1
\end{aligned}
$$

$$
n=n_{+}+n_{-}
$$

## and

$$
\begin{aligned}
x & =\sum_{i=1}^{n} \bar{x}_{i}=(1) n_{+}-(-1) n_{1} \\
& =n_{+}-n_{-}
\end{aligned}
$$

So

$$
\begin{aligned}
x & =n_{+}-n_{-}=n_{+}-\left(n-n_{+}\right) \\
& =2 n_{+}-n
\end{aligned}
$$

and

$$
\begin{aligned}
x=n_{+}-n_{-} & =n \cdot n_{-} \cdot n_{-} \\
& =n \cdot 2 n_{-}
\end{aligned}
$$

it follows that

$$
\begin{array}{ll}
x=2 n_{1}-n \Rightarrow & 2 n_{1}=x+n \\
x=n-2 n_{-} \Rightarrow & 2 n_{-}=x-n
\end{array}
$$

if $x+n$ is event

$$
\begin{aligned}
& n_{+}=\frac{x+n}{2} \\
& n_{-}=\frac{x-n}{2}
\end{aligned}
$$

Now consider a segunce of $n$ events the distribution of $n_{+}$ will be

$$
p\left(n_{+}\right)=\binom{n}{n_{+}} p^{n_{+}}(1-p)^{n_{-} n_{+}}
$$

and

$$
E\left(n_{+}\right)=\sum_{n_{+}=0}^{n} n_{+} p\left(n_{+}\right)
$$

$$
=\sum_{n_{+}=0}^{n} n_{+} \frac{n!}{n_{+}!\left(n-n_{+}\right)!} p^{n_{+}}(1-p)^{n_{-} n_{+}}
$$

The first term is 0 so,

$$
=\sum_{n_{+}=1}^{n} \frac{n!}{\left(n_{+}-1\right)!}\left(n-n_{+}\right)!P^{n_{+}}(1-P)^{n-n_{F}}
$$

## using

$$
n-n_{+}=(n-1)-\left(n_{+}-1\right)
$$

gives

$$
\begin{aligned}
E\left(n_{+}\right) & =\sum_{n_{+}=1}^{n} n \frac{(n-1)!}{\left(n_{+}-1\right)!\left(n-n_{+}\right)!} P P^{n_{+}-1}\left((-p)^{n-n_{+}}\right. \\
& =n p \sum_{n_{+}=1}^{n} \frac{(n-1)!}{\left(n_{+}-1\right)!\left(n-n_{+}\right)!} P^{n_{+}-1}(1-p)^{n-n_{+}}
\end{aligned}
$$

let

$$
m=n_{+}-1
$$

so

$$
\begin{gathered}
n-n_{+}=n-m-1=n-1-m \\
E\left(n_{+}\right)=n p \sum_{m=0}^{n-1} \frac{(n-1)!}{m!(n-1-m)!} P^{m}(1-p)^{n-1 \cdot m}
\end{gathered}
$$

$=n p \sum_{m=0}^{n-1}\binom{n-1}{m} p^{m}(1-p)^{n-1-m}$
using the binomial theorem
$\sum_{m=0}^{n-1}\binom{n-1}{m} p^{m}(1-p)^{n-1-m}$
$=[p-(1-p)]^{n-1}=1$
Thus

$$
E\left(n_{t}\right)=n p
$$

Next

$$
E\left(n_{+}^{2}\right)=\sum_{n_{+}=0}^{n} n_{+}^{2}\binom{n}{n_{+}} p^{n_{+}}(1-p)^{n-n_{+}}
$$

since the first term is 0
$=\sum_{n_{+}=1}^{n} n_{+} \frac{n!}{\left(n_{+}-1\right)!\left(n-n_{+}\right)!} p^{n_{+}}(1-p)^{n_{-} n_{+}}$
once again let

$$
m=n_{+}-l
$$

then

$$
\begin{aligned}
E\left(n_{+}^{2}\right)=n p \sum_{m=0}^{n-1}(m+1)\binom{n-1}{m} P^{m}(1-p)^{n-1-m} \\
=n p\left[\sum_{m=0}^{n-1} m\binom{n-1}{m} P^{m}(1-p)^{n-1-m}\right. \\
\left.+\sum_{m=0}^{n-1}\binom{n-1}{m} P^{m}(1-p)^{n-1-m}\right]
\end{aligned}
$$

but

$$
\sum_{m=0}^{n-1}\binom{n-1}{m} p^{m}(1-p)^{n-1-m}=1
$$

and using the $E\left(n_{+}\right)$result

$$
\sum_{m=0}^{n-1} m\binom{n-1}{m} p^{m}(1-p)^{n-1-m}=(n-1) p
$$

so

$$
\begin{aligned}
E\left(n_{+}^{2}\right) & =n p[(n-1) p+1] \\
& =n p\left(n_{p}-p+1\right) \\
& =n_{p}\left(n_{p}+1-p\right) \\
& =n^{2} p^{2}+n_{p}(1-p)
\end{aligned}
$$

and

$$
\begin{aligned}
\sigma_{n_{+}}^{2} & =E\left(n_{+}^{2}\right)-\left[E\left(n_{+}\right)\right]^{2} \\
& =n^{2} \rho^{2}+n p(l-\rho)-n^{2} p^{2} \\
& =n p(l-p)
\end{aligned}
$$

If use is made of

$$
\begin{aligned}
& x=2 n_{+}-n \\
E(x) & =E\left(2 n_{+}-n\right) \\
& =2 E\left(n_{+}\right)-E(n) \\
& =2 n p-n \\
& =n(2 p-1)
\end{aligned}
$$

$$
\begin{aligned}
E\left(x^{2}\right) & =E\left[\left(2 n_{+}-n\right)^{2}\right] \\
& =E\left(4 n_{+}^{2}-4 n_{+} n+n^{2}\right) \\
& =4 E\left(n_{+}^{2}\right)-4 n E\left(n_{+}\right)+n^{2} \\
& =4\left[n^{2} p^{2}+n p(1-p)\right] \\
& -4 n(n p)+n^{2} \\
& =4 n^{2} p^{2}+4 n p(1-p) \\
& -4 n^{2} p+n^{2} \\
\Rightarrow & 4 n p(1-p)+4 n^{2} p^{2}-4 n^{2} p+n^{2} \\
= & 4 n p(1-p)+4 n^{2} p^{2}+n^{2}(1-4 p) \\
= & 4 n p(1-p)+n^{2}\left[4 p^{2}+1-4 p\right] \\
= & 4 n p(1-p)+n^{2}[1+4 p(p-1)] \\
= & 4 n p(1-p)+n^{2}[1-4 p(1-p)]
\end{aligned}
$$

and

$$
\sigma_{x}^{2}=E\left(x^{2}\right)-[E(x)]^{2}
$$

$$
\begin{aligned}
= & 4 n p(1-p)+n^{2}[1-4 p(1-p)] \\
& -n^{2}(2 p-1)^{2} \\
= & 4 n p(1-p)+n^{2}[1-4 p(1-p)] \\
& -n^{2}\left(4 p^{2}-4 p+1\right) \\
= & 4 n p(1-p)+n^{2}-4 n^{2} p(1-p) \\
& -4 n^{2} p^{2}+4 n^{2} p-n^{2} \\
= & 4 n p(1-p)+x^{2}-4 n^{2} p(1-p) \\
& +4 n^{2} p(1-p)-n^{2} \\
= & \ln p(1-p)
\end{aligned}
$$

Recall that

$$
P\left(n_{+}, n\right)=\binom{n}{n_{+}} P^{n_{+}}(1-p)^{n_{-} n_{+}}
$$

and

$$
n_{+}=\frac{n+x}{2}
$$

substituting gives

$$
\begin{aligned}
p(x, n) & =\binom{n}{\frac{1}{2}(x+n)} p^{\frac{1}{2}(x+n)}(1-p)^{n-\frac{1}{2}(x+n)} \\
& =\binom{n}{\frac{1}{2}(x+n)} p^{\frac{1}{2}(x+n)}(1-p)^{\frac{1}{2}(n-x)}
\end{aligned}
$$

To compute the probability of returning to the origin assume the $n$ is even,

$$
\frac{n}{2}=m \Rightarrow 2 m=n
$$

and $x=0$

$$
\begin{aligned}
p(0,2 m) & =\binom{2 m}{m} p^{m}(1-p)^{m} \\
& =\frac{2 m!}{m!m!} p^{m}(1-p)^{m}
\end{aligned}
$$

for large $n$ sterling's a-ppoximation gives

$$
\begin{aligned}
n! & \sim \sqrt{2 \pi n} e^{-n} n^{n} \\
& =\sqrt{2 \pi} e^{-n} n^{n+12}
\end{aligned}
$$

So
$2 m!\sim \sqrt{2 \pi} e^{-2 m}(2 m)^{2 m+1 / 2}$
and

$$
m!\sim \sqrt{2 \pi} e^{-m} m^{m+1 / 2}
$$

thus

$$
\begin{aligned}
& \left.\frac{2 m!}{m!m!} \sim \frac{\sqrt{2 \pi} e^{-2 m}(2 m)^{2 m-1 / 2}}{\left(\sqrt{2 \pi e^{-m} m^{m+1 / 2}}\right)\left(\sqrt{2 \pi e^{-m}} m^{m+1 / 2}\right.}\right) \\
& \quad=\frac{1}{\sqrt{2 \pi}} \frac{e^{-2 m}(2 m)^{2 m+1 / 2}}{e^{-2 m} m^{2 m+1}} \\
& \quad=\frac{1}{\sqrt{2 \pi}} 2^{2 m+1 / 2} \frac{m^{2 m+1 / 2}}{m^{2 m+1}} \\
& \quad=\frac{1}{\sqrt{2 \pi}} 2^{2 m+1 / 2} m^{-1 / 2} \\
& \quad=\frac{2^{2 m+1 / 2}}{\sqrt{2 \pi m}}=\frac{2^{2 m}}{\sqrt{\pi m}}=\frac{4^{m}}{\sqrt{\pi m}}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
p(0,2 m) & \sim \frac{4 m}{\sqrt{\pi m}} p^{m}(1-p)^{m} \\
& =\frac{[4 p(1-p)]^{m}}{\sqrt{\pi m}}
\end{aligned}
$$

if

$$
\begin{aligned}
& 4 p(1-p)<1 \\
&= p(1-p)<\frac{1}{4} \\
& p(0,2 m) \rightarrow 0 \quad \text { as } m \rightarrow \infty
\end{aligned}
$$

this is saying that if $p(1-p) \leqslant k_{1}$ the probability of returning to the origin is 0 .
The number of returns to the origin after $N$ steps is

$$
\begin{aligned}
R(N) & =\sum_{m=0}^{\frac{1}{2} N} p(0,2 m) \\
& =\sum_{m=0}^{1 / 2 N} \frac{(2 m)!}{m!m!} p^{m}(1-p)^{m}
\end{aligned}
$$

let $p=1 / 2$

$$
\begin{aligned}
R(N) & =\sum_{m=0}^{\frac{1}{m} N} \frac{(2 m)^{!}}{m!m!}(1 / 2)^{2 m} \\
& =\sum_{m=0}^{\frac{1}{2} N} \frac{2 m!}{m!m!} 2^{-2 m}
\end{aligned}
$$

$u_{\text {using }}$ Sterling's approximation for large $N$

$$
\begin{aligned}
R(N) & \sim \sum_{m=0}^{\frac{1}{2} N} 4^{m} 2^{-2 m} \\
& =\sum_{m=0}^{\frac{1}{2 N} N} 4^{m} 4^{-m} \\
& =\sum_{m=0}^{1 / 2 N} \frac{1}{\sqrt{\pi m}}
\end{aligned}
$$

integrating gives

$$
\begin{aligned}
R(N) \sim & \left.\frac{1}{\sqrt{\pi}} 2 \sqrt{m}\right|_{0} ^{1 / 2 N} \\
= & \frac{1}{\sqrt{\pi}} 2 \sqrt{\frac{1}{2} N}=\sqrt{\frac{2 N}{\pi}}
\end{aligned}
$$

## Stopping Times

Given a stochastic process $\left\{\underline{X}_{n}: n \geqslant 0, n \in \mathbb{Z}\right\}$. A random time $\uparrow$ considered as a discrefe random variable taking values $i \in\{0,1,2, \ldots\}$. Let $X_{r}$ denote the state of the stochastic process at $\tau=n$ so that $Z_{\tau}=Z_{n}$. If the random process is stopped after $\tau$ sleps and the decision to stop is based only upon at most what has been observed $\tau$ is considered a stopping time.

## First Passage (Gambler's Ruin)

Consider $\left\{\bar{X}_{n}: n \geqslant 0\right\}$ and let

$$
i \in\left\{\bar{x}_{n}: n \geqslant 0\right\}
$$

defined by

$$
T=\min \left\{n \geqslant 0: \underline{X}_{n}=i\right\}
$$

here $\tau$ is called the first time passage of the process into state $i$. Also, called the hitting time of the process to state. $i$.

For the Eambler's Ruin the gambling stops at eitner

$$
\bar{x}_{n}=N \text { or } \bar{x}_{n}=0
$$

which ever comes first.

## Wald's Equation

If $\tau$ is a stoping time with respect to the sequence $\left\{I_{n}: n \geqslant 1\right\}$. consider the sum up to $\tau$

$$
\sum_{n=1}^{T} \bar{X}_{n}
$$

and if $E(\tau)<\infty$ and $E(|\bar{X}|)<\infty$ then show that

$$
E\left(\sum_{n=1}^{T} \bar{X}_{n}\right)=E(T) E(\bar{X})
$$

Define the indicator function

$$
I_{(\tau>n-1)}= \begin{cases}1 & \tau>n-1 \\ 0 & \tau \leqslant n-1\end{cases}
$$

Then

$$
\begin{aligned}
\sum_{n=1}^{T} X_{n} & =\sum_{n=1}^{T}(1) I_{n}+\sum_{n=\tau+1}^{\infty}(0) I_{n} \\
& =\sum_{n=1}^{\infty} I_{(\tau>n-1)} X_{n}
\end{aligned}
$$

Assuming $\bar{X}_{i} \| \bar{X}_{j} \quad i \neq j$ and that
$\underline{\Pi}(\tau>n-1)$ depends only on $\left\{X_{m}: m<n\right\}$ so

$$
I_{n} \Perp I I(\tau>n-1)
$$

and that $I_{n}$ are idenically distributed with

$$
E\left(\underline{X}_{n}\right)=E(\underline{X})
$$

then
$E\left[\sum_{n=1}^{r} \bar{X}_{n}\right]=E\left[\sum_{n=1}^{\infty} \mathbb{I}_{(\tau>n-1)} \bar{X}_{n}\right]$
$=\sum_{n=1}^{\infty} E\left[\mathbb{I}_{(\tau>n-1)} \mathbb{X}_{n}\right]$
$=\sum_{n=1}^{\infty} E\left[\Pi_{(\tau>n-1)}\right] E\left(Z_{n}\right)$

$$
\begin{aligned}
& \text { using } E(X)=E\left(X_{n}\right) \text { and } \\
& \text { gives } P(\tau>n-1)=E[\Pi(\tau>n-1)] \\
& =\sum_{n=1}^{\infty} P(\tau>n-1) E(\mathbb{X}) \\
& =E(\mathbb{X}) \sum_{n=0}^{\infty} P(\tau>n) \\
& =E(\mathbb{X}) E(\tau) \\
& \text { since } \\
& E(\tau)=\sum_{n=0}^{\infty} P(\tau>n)
\end{aligned}
$$

## Beta Distribution

The Beta distribution is defined for $0 \leqslant x \leqslant 1$ and $\alpha, \beta>0$ by

$$
\operatorname{Beta}(x, \alpha, \beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}
$$

Where $B(\alpha, \beta)$ is the Bela function which is defined by

$$
\begin{aligned}
B(\alpha, \beta) & =\int_{0}^{1} x^{\alpha-1}(1-x)^{\beta-1} d x \\
& =\frac{\Gamma(\alpha) \Gamma(\beta)}{\Gamma(\alpha+\beta)}
\end{aligned}
$$

and $\Gamma(\alpha)$ is the Camma function

$$
\Gamma(\alpha)=\int_{0}^{\infty} x^{\alpha-1} e^{-x} d x
$$

An interpretation of Beta $(x, \alpha, \beta)$ can be found by looking at the special case of
$\alpha$ and $\beta$ are positive non zero integers

$$
\begin{gathered}
\alpha, \beta \in\{1,2,3, \ldots\} \\
(\alpha-1+\beta-1)=\frac{1}{(\alpha+\beta-1) B(\alpha, \beta)}
\end{gathered}
$$

80

$$
\begin{aligned}
& \operatorname{Beta}(x, \alpha, \beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)} \\
& =\binom{\alpha-1+\beta-1}{\alpha-1}(\alpha+\beta-1) x^{\alpha-1}(1-x)^{\beta-1}
\end{aligned}
$$

The Binomial distribution is defined by
Binumial $(x, \alpha-1, \beta-1)=\binom{\alpha-1+\beta-1}{\alpha-1} x^{\alpha-1}(1-x)^{\beta-1}$
50
$\operatorname{Beta}(x, \alpha, \beta)=(\alpha+\beta-1)$ Binomial $(x, \alpha-1, \beta-1)$
Thus Beta $(x, \alpha, \beta)$ is the extension of the Binomial distribution to the Real numbers.

The expection of a random variable with a Beta distribution is given by

$$
\begin{aligned}
E(X) & =\int_{0} x \operatorname{Beta}(x, \alpha, \beta) d x \\
& =\frac{1}{B(\alpha, \beta)} \int_{0}^{1} x x^{\alpha-1}(1-x)^{\beta-1} d x \\
& =\frac{1}{B(\alpha, \beta)} \int_{0}^{1} x^{\alpha}(1-x)^{\beta-1} d x \\
& =\frac{B(\alpha+1 \beta)}{B(\alpha, \beta)}
\end{aligned}
$$

using the identity

$$
B(\alpha+1, \beta)=\frac{\alpha}{\alpha+\beta} B(\alpha, B)
$$

Gives

$$
E(\bar{x})=\mu=\frac{\alpha}{\alpha+\beta}
$$

Also,

$$
E\left(\bar{x}^{2}\right)=\int_{0} x^{2} \operatorname{Beta}(x, \alpha, \beta) d x
$$

$$
\begin{aligned}
& =\frac{1}{B(\alpha, \beta)} \int_{0}^{1} x^{2} x^{\alpha-1}(1-x)^{\beta-1} d x \\
& =\frac{1}{B(\alpha, \beta)} \int_{0}^{1} x^{\alpha+1}(1-x)^{\beta-1} d x \\
& =\frac{B(\alpha+2, \beta)}{B(\alpha, \beta)} \\
& \text { using the identity } \\
& B(\alpha+1, \beta)=\frac{\alpha}{\alpha+\beta} B(\alpha, \beta) \\
& \text { gives } \\
& B(\alpha+2, \beta)=\frac{\alpha+1}{d+\beta+1} B(\alpha+1, \beta) \\
& =\frac{\alpha(\alpha+1)}{(\alpha+\beta-1)(\alpha-1 \beta)} B(\alpha, \beta) \\
& \text { so } \\
& E\left(\underline{x}^{2}\right)=\frac{\alpha(\alpha+1)}{(\alpha+\beta+1)(\alpha+\beta)}
\end{aligned}
$$

so

$$
\begin{aligned}
& \operatorname{Var}(\bar{x})=\sigma^{2}=E\left(\bar{x}^{2}\right)-[E(\bar{x})]^{2} \\
& =\frac{\alpha(\alpha+1)}{(\alpha+\beta+1)(\alpha+\beta)}-\frac{\alpha^{2}}{(\alpha+\beta)^{2}} \\
& =\frac{\alpha(\alpha+1)(\alpha+\beta)-\alpha(\alpha+\beta+1)}{(\alpha+\beta+1)(\alpha+\beta)^{2}} \\
& =\frac{\alpha}{(\alpha+\beta+1)(\alpha+\beta)^{2}}[(\alpha+(x-\beta)-\alpha(\alpha+\beta-1)] \\
& =\frac{\alpha}{(\alpha+\beta+1)(\alpha+\beta)^{2}}\left(\alpha^{2}+\alpha+\alpha \beta+\beta-\alpha^{2}\right. \\
& =\frac{\alpha \beta-\alpha)}{(\alpha+\beta+1)(\alpha+\beta)^{2}} \\
& \text { so } \\
& \sigma^{2}=\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha+\beta)^{2}}
\end{aligned}
$$

* The made is the most probable value which is the maximum of probability density function, namely

$$
\operatorname{Beta}(x, \alpha, \beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}
$$

differentiatingwith respect to $x$ gives

$$
\begin{aligned}
& \frac{d}{d x} \operatorname{Bet} a(x, \alpha, \beta)=\frac{1}{B(\alpha, \beta)}\left[(\alpha-1) x^{\alpha-2}(1-x)^{\beta-1}\right. \\
& \left.\quad+x^{\alpha-1}(\beta-1)(-1)(1-x)^{\beta-2}\right] \\
& \quad=\frac{1}{B(\alpha, \beta)} x^{\alpha-2}(1-x)^{\beta-2}[(\alpha-1)(1-x) \\
& \quad-(\beta-1) x] \\
& \quad=\frac{1}{B(\alpha, \beta)} x^{\alpha-2}(1-x)^{\beta-2}[\alpha-1-x(\alpha-1) \\
& \quad=\frac{1}{B(\alpha, \beta)} x^{\alpha-2}(1-x)^{\beta-2}[(\alpha-1)-x(\alpha+\beta-2)]
\end{aligned}
$$

The second derivative is

$$
\begin{gathered}
\frac{d^{2}}{d x^{2}} B(x, \alpha, \beta)=\frac{1}{\beta(\alpha, \beta)}\{[(\alpha-1)-x(\alpha-\beta-2)] \\
{\left[(\alpha-2) x^{\alpha-3}(1-x) \beta-2+x^{\alpha-2}(-1)(\beta-2)(1-x)^{\beta-3}\right]} \\
+x^{\alpha-2}(1-x)^{\beta-2}(-1)(\alpha+\beta-2) \\
=\frac{1}{B(\alpha, \beta)}\left\{[(\alpha-1)-x(\alpha+\beta-2)]\left[x^{\alpha-3}(1-x)^{\beta-3}\right]\right. \\
{[(\alpha-2)(1-x)-x(\beta-2)]} \\
\left.-x^{\alpha-2}(1-x)^{\beta-2}(\alpha+\beta-2)\right\} \\
\frac{1}{B(\alpha, \beta)} \begin{array}{c}
x^{\alpha-3}(1-x)^{\beta-3}\{[(\alpha-1)-x(\alpha+\beta-2)] \\
{[(\alpha-2)(1-x)-x(\beta-2)]} \\
-x(1-x)(\alpha+\beta-2)\}
\end{array} \\
=\frac{1}{B(\alpha, \beta)} \begin{array}{c}
x^{\alpha-3}(1-x)^{\beta-3}\{[(\alpha-1)-x(\alpha-\beta-2)] \\
{[(\alpha-2)-x(\alpha-2)-x(\beta-2)]} \\
-x(1-x)(\alpha+\beta-2)\}
\end{array}
\end{gathered}
$$

$=\frac{1}{B(\alpha, \beta)} x^{\alpha-3}(1-x)^{\beta-3} \leqslant[(\alpha-1)-x(\alpha-\beta-2)]$

$$
[(\alpha-2)-x(\alpha+\beta-4)]-x(1-x)(\alpha+\beta-2)\}
$$

The extrema are $x$ where

$$
\frac{d}{d x} \operatorname{Beta}(x, \alpha, \beta)=0
$$

So,

$$
\begin{aligned}
& (\alpha-1)\left(1-x^{\prime}\right)-(\beta-1) x^{\prime}=0 \\
\Rightarrow & (\alpha-1)-x^{\prime}(\alpha-1)-x^{\prime}(\beta-1)=0 \\
\Rightarrow & (\alpha-1)=x^{\prime}(\alpha-1+\beta-1) \\
\Rightarrow & x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}
\end{aligned}
$$

Now
$0 \leqslant x^{\prime} \leqslant 1$ for $\alpha, \beta>1$
tris is clearly satisfied.
The numerator requires $2>1$ and the denomingtor places a constraint on $\beta$ for $\beta<1$

$$
\begin{aligned}
& \alpha+\beta-2>0 \\
\Rightarrow \quad & \beta>2-\alpha
\end{aligned}
$$

but $\beta>0 \Rightarrow \alpha<2$
for $x^{\prime}$ to be a maximum

$$
\frac{d^{2}}{d x^{2}} \operatorname{Beta}\left(x^{\prime}, \alpha, \beta\right)<0
$$

this implies

$$
\begin{aligned}
& {\left[(\alpha-1)-x^{\prime}(\alpha+\beta-2)\right]\left[(\alpha-2)-x^{\prime}(\alpha+\beta-4)\right]} \\
& -x^{\prime}\left(1-x^{\prime}\right)(\alpha+\beta-2)<0
\end{aligned}
$$

The first term vanishes since

$$
\begin{aligned}
& (\alpha-1)-x^{\prime}(\alpha+\beta-2)=\alpha-1-\frac{(\alpha-1)}{\alpha-\beta-2}(\alpha-\beta-2) \\
& =\alpha-1-(\alpha-1)=0
\end{aligned}
$$

for the second term

$$
\begin{aligned}
& -x^{\prime}\left(1-x^{\prime}\right)(\alpha+\beta-2) \\
= & -\frac{(\alpha-1)}{(\alpha+\beta-2)}(\alpha+\beta-2)\left(1-\frac{\alpha-1}{\alpha+\beta-2}\right) \\
= & \frac{-\alpha-1}{\alpha+\beta-2}(\alpha+\beta-2-\alpha+1)
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{(\alpha-1)}{\alpha+\beta-2}(\beta-1) \\
& =-\frac{(\alpha-1)(\beta-1)}{\alpha+\beta-2}=\left.\frac{d^{2}}{d x^{2}} \operatorname{Beta}(x, \alpha, \beta)\right|_{x=x^{\prime}}
\end{aligned}
$$

so
$\left.\frac{d^{2}}{d x^{2}} \operatorname{Beta}(x, \alpha, \beta)\right|_{x=x^{\prime}}=-\frac{(\alpha-1)(\beta-1)}{\alpha+\beta-2}<0$

* for $\alpha, \beta>1$ this is clearly satisfied so

$$
x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}
$$

is a maximum

* For $1<\alpha<2, \quad 0<\beta<2-\alpha<1$

$$
x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}<0
$$

Which is invalid so no extrema exists for $0<x<1$. Since $\beta<1$ the distribution has singularity at $x=1$.

* For $\alpha<1$ and $1<\beta<2-\alpha$

Now

$$
\begin{aligned}
& 1<\beta<2-\alpha=0 \quad 0<\beta-1<1-\alpha \\
& \Rightarrow \alpha-1<\alpha-1+\beta-1<0 \\
& \Rightarrow \frac{\alpha-1}{\alpha-1+\beta-1}>1
\end{aligned}
$$

since both terms are $<0$, so

$$
x^{\prime}=\frac{\alpha-1}{\alpha-1+\beta-1}=\frac{\alpha-1}{\alpha+\beta-2}>1
$$

so no extrema exists for $0<x<1$. The distribution has a singularity at $x=0$ since $\alpha<1$.

* For $\alpha<1$ and $\beta<1$

$$
x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}>0
$$

and
$\left.\frac{d^{2} \operatorname{Beta}}{d x^{2}}(x, \alpha, \beta)\right|_{x=x^{\prime}}=-\frac{(\alpha-1)(\beta-1)}{\alpha+\beta-2}>0$
so $x^{\prime}$ is a minimum. The distribution has singularities at
$x=0$ and $x=1$ since $\alpha<1$ and $\beta<1$.

* For $\alpha>1$ and $\beta<1$

$$
x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}
$$

$\beta<1 \Rightarrow \beta-2<-1 \Rightarrow \alpha+\beta-2<\alpha-1$
$\Rightarrow 1<\frac{\alpha-1}{\alpha+\beta-2}$
Trus no extrema exists for $0<x<1$. The distribution has a singularity at $x=1$ since $\beta<1$

* For $\alpha<1$ and $\beta>2$

$$
x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}<0
$$

Trus no extrema exists for $0<x<1$. The distribution has singularition at $x=0$ since $\alpha<1$.

* For $\alpha \gg \beta, \beta>1 \Rightarrow x \rightarrow 1$ and for $\beta>\alpha, \alpha>1 \Rightarrow x^{\prime} \rightarrow 0$
* For $\alpha=\beta$ and $\alpha, \beta>1$
$x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}=\frac{\alpha-1}{2 \alpha-2}=\frac{2-1}{2(\alpha-1)}=\frac{1}{2}$

$$
\begin{aligned}
\mu & =\frac{\alpha}{\alpha+\beta}=\frac{\alpha}{2 \alpha}=\frac{1}{2} \\
\sigma^{2} & =\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha-1 \beta)^{2}}=\frac{\alpha^{2}}{(2 \alpha+1)(2 \alpha)^{2}} \\
& =\frac{\alpha^{2}}{4 \alpha^{2}(2 \alpha+1)}=\frac{1}{4(2 \alpha+1)}
\end{aligned}
$$

Since

$$
\mu=x^{\prime}
$$

The distribution is symetic about $x^{\prime}$
and as 2 increases $0^{2}$ decreaces so the distribution becomes sharp

$$
\begin{aligned}
& \text { * For } \alpha=\beta \text { and } \alpha, \beta<1 \\
& x^{\prime}=\frac{\alpha-1}{\alpha+\beta-2}=\frac{\alpha-1}{2(\alpha-1)}=\frac{1}{2} \\
& \left.\frac{d^{2}}{d x^{2}} \operatorname{Beta}(x, \alpha, \beta)\right|_{x=x^{\prime}}=-\frac{(\alpha-1)(\beta-1)}{\alpha+\beta-2} \\
& =\frac{(\alpha-1)^{2}}{\partial(\alpha-1)}=-\frac{(\alpha-1)}{2}>0
\end{aligned}
$$

so $x^{\prime}$ is a minimum ard

$$
\mu=\frac{\partial}{\partial+\beta}=\frac{\partial}{\partial \alpha}=\frac{1}{2}
$$

$$
\begin{aligned}
\sigma^{2} & =\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha+\beta)^{2}}=\frac{\alpha^{2}}{(2 \alpha+1)(2 \alpha)^{2}} \\
& =\frac{\alpha^{2}}{4 \alpha^{2}(2 \alpha+1)}=\frac{1}{4(2 \alpha+1)} \\
\text { as } & 2 \rightarrow 0 \rightarrow \sigma^{2} \rightarrow 1 / 4
\end{aligned}
$$

* Summary of Results

$$
\operatorname{Beta}(x, \alpha, \beta)=\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}
$$

1) For $\alpha, \beta \in\{1,2,3, \ldots\}$

Beta $(x, \alpha, \beta)=(\alpha+\beta-1)$ Binomial $(x, \alpha-1, \beta-1)$
2) Distribution mean is given b/,

$$
\mu=\frac{\alpha}{\alpha+\beta}
$$

3) Distribution stardard deviation is given by,

$$
\sigma^{2}=\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha-1 \beta)^{2}}
$$

4) Distribution mode (most probable value)

For $\alpha, \beta>1$

$$
x_{\max }=\frac{\alpha-1}{\alpha+\beta-2}
$$

5) For $1<\alpha<2$ and $0<\beta<2-\alpha<1$ no extema exists for $0<x<1$. The distribution has a singularity at $x=1$ since $\beta<1$.
6) For $\alpha<1$ and $1<\beta<2-\alpha$ no extrema exists for $0<x<1$. The distribution has a singularity at $x=0$ since $\alpha<1$.
7) For $\alpha<1$ and $\beta<1 x^{\prime}$ is a minimum

$$
x_{\text {min }}=\frac{\alpha-1}{\alpha+\beta-2}
$$

The distribution has singularities at both $x=0$ and $x=1$ since $\alpha<1$ and $\beta<1$.
8) For $\alpha \gg \beta$ and $\beta>1$
$x_{\text {max }} \rightarrow 1$
9) For $\beta \gg \alpha$ and $\alpha>1$
$X_{\text {max }} \rightarrow 0$
10) For $\alpha>1$ a $\beta<1$ no extrema exists for $0<x<1$ so the maximum vale will be al

$$
x=0 \text { or } x=1
$$

11) For $\alpha<1 \quad \beta>2$ no extrema evists for $0<x<1$ so the maximum value will be al $x=0$ or $x=1$
12) For $\alpha=\beta$ with $\alpha, \beta>1$ the distribution is symmetric about a maximum $x^{\prime}$ with

$$
\mu=x^{\prime}=1 / 2
$$

and becoms sharper as $a$ increases since $a^{2}$ decreaces.
13) For $\alpha=\beta$ with $\alpha, \beta<1$
the distribution is symmetric about a minimum $x^{\prime}$ with

$$
\mu=x^{\prime}=1 / 2
$$

and becomes broader as $\alpha \rightarrow 0$ with $\sigma^{2} \rightarrow 1 / 4$.
14) For $\alpha \gg 1$ and $\beta \gg 1 \quad 0^{2} \rightarrow 0$ so the distribution is sharphy peaked.

$$
\sigma^{2}=\frac{\alpha \beta}{(\alpha+\beta+1)(\alpha+\beta)^{2}} \rightarrow 0
$$

Discrete Cross Correbtion Theorem The cross correlation of two discrete vectors

$$
\begin{aligned}
& \left(f_{n}\right)=\left(f_{0}, f_{1}, f_{2}, \ldots, f_{N-1}\right) \\
& \left(g_{n}\right)=\left(g_{0}, g_{1}, g_{2}, \ldots, g_{n-1}\right)
\end{aligned}
$$

is defined by

$$
\psi_{t}=\sum_{n=0}^{N-1} f_{n} g_{n+t}
$$

Now

$$
\begin{aligned}
f_{n} & =\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k} \\
g_{n+t} & =\frac{1}{N} \sum_{m=0}^{N-1} G_{k} e^{2 \pi i\left(\frac{n+t}{N}\right) m} \\
& =\frac{1}{N} \sum_{m=0}^{N-1} G_{k} e^{2 \pi i\left(\frac{n}{N}\right)^{m}} e^{2 \pi i\left(\frac{t}{N}\right) m}
\end{aligned}
$$

80

$$
\psi_{t}=\sum_{n=0}^{N-1} f_{n} g_{n+t}
$$

$$
\begin{aligned}
& =\sum_{n=0}^{N-1}\left\{\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k}\right\} \\
& \quad\left\{\frac{1}{N} \sum_{m=0}^{N-1} G_{m} e^{2 \pi i\left(\frac{n}{N}\right) m} e^{2 \pi i\left(\frac{t}{N}\right) m}\right\} \\
& =\frac{1}{N^{2}} \sum_{k=0}^{N-1} \sum_{m=0}^{N-1} e^{2 \pi i\left(\frac{t}{N}\right) m} F_{k} G_{m} \sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-1}{N}\right) n} \\
& =\frac{1}{N^{2}} \sum_{k=0}^{N-1} \sum_{m=0}^{N-1} e^{2 \pi i\left(\frac{t}{N}\right) m} F_{k} G_{m} N \delta(m-k) \\
& =\frac{1}{N} \sum_{k=0}^{N-1} F_{k} G_{-k} e^{-2 \pi i\left(\frac{t}{N}\right) k} \\
& N o \omega \\
& \text { so } G_{-k}=G_{k}^{*} \\
& \psi_{t}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} G_{k}^{*} e^{-2 \pi i\left(\frac{t}{N}\right) k}
\end{aligned}
$$

Now

$$
\Psi_{l}=\sum_{t=0}^{N-1} \psi_{t} e^{-2 \pi i\left(\frac{t}{N}\right) l}
$$

So

$$
\begin{aligned}
\Psi_{l} & =\sum_{t=0}^{N-1}\left\{\frac{1}{N} \sum_{k=0}^{N-1} F_{k} G_{k}^{*} e^{-2 \pi i\left(\frac{t}{N}\right) k}\right\} e^{-2 \pi i\left(\frac{t}{N}\right) l} \\
& =\frac{1}{N} \sum_{k=0}^{N-1} F_{k} G_{k}^{*} \sum_{t=0}^{N-1} e^{-2 \pi i\left(\frac{k+l}{N}\right) t} \\
& =\frac{1}{N} \sum_{k=0}^{N-1} F_{k} G_{k}^{*} N \delta(k+l) \\
& =F_{-l} G_{-l}^{*}=F_{l}^{*} G_{l} \\
\text { Thus } & \Psi_{l}=F_{l}^{*} G_{l}
\end{aligned}
$$

## Discrete Cross Correlation Theorem Examples

In the Disorete Convolution Examples section of Miscellaneous Math

$$
T_{n, k}=\left(\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right)
$$

The transform for the vedor

$$
\begin{aligned}
& \left(f_{n}\right)=(8,4,8,0), N=4 \\
& \left(F_{k}\right)=\left(\begin{array}{c}
20 \\
-4 i \\
12 \\
4 i
\end{array}\right) \\
& \left(g_{n}\right)=(6,3,9,3) \\
& \left(G_{k}\right)=\left(\begin{array}{c}
21 \\
-3 \\
9 \\
-3
\end{array}\right)
\end{aligned}
$$

The Discrete Cross Correlation is defined by

$$
\psi_{t}=\sum_{n=0}^{N-1} f_{n} g_{n+t}
$$

The sum is computed by creating a table of $\left(f_{n}\right)$ and the shifted values of (gn) and summing the product of the nuevlapping values

| $n$ |  |  |  | 0 | 1 | 2 | 3 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f_{n}$ |  |  |  | 8 | 4 | 8 | 0 |
| $g_{n}$ |  |  | 6 | 3 | 9 | 3 |  |
| $g_{n+1}$ |  | 6 | 3 | 9 | 3 |  |  |
| $g_{n+2}$ | 6 | 3 | 9 | 3 |  |  |  |
| $g_{n+3}$ | 6 | 3 | 9 | 3 |  |  |  |

$$
\begin{aligned}
& \psi_{0}=8 \cdot 6+4 \cdot 3+8 \cdot 9+0 \cdot 3=132 \\
& \psi_{1}=8 \cdot 3+4 \cdot 9+8 \cdot 3=84 \\
& \psi_{2}=8 \cdot 9+4 \cdot 3=84 \\
& \psi_{3}=8 \cdot 3=24
\end{aligned}
$$

If the Discrete Cross Correlation Tneorem is used to evaluate
$\left(\gamma_{t}\right)$ the Discrete Fourier implicatly assumes the ( $f_{n}$ ) and ( $g_{n}$ ) are periodic with period $N$.
A straight forward application will produce the result,

$$
\begin{array}{c|l|l|l|l|}
n & 0 & 1 & 2 & 3 \\
\hline f n & 8 & 4 & 8 & 0 \\
\hline g_{n} & 6 & 3 & 9 & 3 \\
g_{n+1} & 3 & 9 & 3 & 6 \\
g_{n+2} & 9 & 3 & 6 & 3 \\
g_{n+3} & 3 & 6 & 3 & 9
\end{array} \left\lvert\, \begin{gathered}
8 \cdot 6+4 \cdot 3+8 \cdot 9+0 \cdot 3=132 \\
\psi_{0}=8 \cdot 3+4 \cdot 9+8 \cdot 3+0 \cdot 6=84 \\
\psi_{1}=8 \cdot 9+4 \cdot 3+8 \cdot 6+0 \cdot 3=132 \\
\psi_{2}=8 \cdot 9+4 \cdot 6+8 \cdot 3+0 \cdot 9=72 \\
\psi_{3}=8 \cdot 3+4 \cdot 6
\end{gathered}\right.
$$

This problem can be overcome by padding the end of ( $f_{n}$ ) and (gh) with N-1 zeros producing vectors of length

| $n$ |  |  |  | 0 | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f_{n}$ | 0 | 0 | 0 | 8 | 4 | 8 | 0 |
| $g_{n}$ | 0 | 0 | 0 | 6 | 3 | 9 | 3 |
| $g_{n+1}$ | 0 | 0 | 6 | 3 | 9 | 3 | 0 |
| $g_{n+2}$ | 0 | 6 | 3 | 9 | 3 | 0 | 0 |
| $g_{n+3}$ | 6 | 3 | 9 | 3 | 0 | 0 | 0 |
| $g_{n+4}$ | 3 | 9 | 3 | 0 | 0 | 0 | 6 |
| $g_{n+5}$ | 9 | 3 | 0 | 0 | 0 | 6 | 3 |
| $g_{n+6}$ | 3 | 0 | 0 | 0 | 6 | 3 | 9 |

$$
\begin{aligned}
& 4_{0}=8 \cdot 6+4 \cdot 3+8 \cdot 9+0 \cdot 3=132 \\
& 4_{1}=8 \cdot 3+4 \cdot 9+8 \cdot 3+0 \cdot 0=84 \\
& 4_{2}=8 \cdot 9+4 \cdot 3+8 \cdot 0+0 \cdot 0=84
\end{aligned}
$$

$\psi_{3}=8.3+4.0+8.8+0.0=24$
$\psi_{4}=8.0+4.0+8.0+0.6=0$
$4_{5}=8 \cdot 0+4 \cdot 0+8 \cdot 6+0 \cdot 3=48$
$\psi_{6}=8 \cdot 0+4 \cdot 6+8 \cdot 3+0 \cdot 9=48$

The answere is contained in the first $N$ elements. The last N-1 elements contain percenicity errors.

## Discrete Autocorrelation

Autocorrelation is the time lagged correlation of series with itself. It time series with itself It dependendence of the future on the present. A timo series with zero autocorrelation has a future that obes not deperd on its past.
Let

$$
\left(f_{n}\right)=\left(f_{0}, f_{1}, f_{2}, \ldots, f_{N-1}\right)
$$

be a vector of $N$ values. using the defintion cross correlation discussed in, from previous section, the autocorrelation is defined as

$$
r_{t}=\sum_{n=0}^{N-1} f_{n} f_{n+t}
$$

The Cross Correlation Theorem gives the following relationship between the Discrete tourier Transforms of $\left(r_{t}\right)$ and $\left(f_{n}\right)$

$$
R_{k}=F_{k} F_{k}^{*}
$$

where $F_{k}^{*}$ is the complex ronjugate of $F_{k}$ and

$$
\begin{aligned}
& r_{t}=\frac{1}{N} \sum_{k=0}^{N-1} R_{k} e^{2 \pi i\left(\frac{k}{n}\right) t} \\
& R_{k}=\sum_{t=0}^{N-1} r_{t} e^{-2 \pi i\left(\frac{t}{N}\right) k}
\end{aligned}
$$

and

$$
\begin{aligned}
& F_{n}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{k}{N}\right) n} \\
& F_{k}=\sum_{n=0}^{N-1} F_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k}
\end{aligned}
$$

Properties of $r_{t}$

1) $r_{0}=\sum_{n=0}^{N-1} f_{n}^{2}$
is the variace and is used to normalize $\left(r_{t}\right)$

## Autocorrelation Example AR(1)

The first order autoregressive process AR(1) is defined by the difference equation

$$
x_{t}=\alpha x_{t-1}+\varepsilon_{t}
$$

where $\varepsilon_{t+1}$ is Normal with, mean of zero and constant variance, that are independent and identically distributed,

$$
\varepsilon_{t} \stackrel{I \pm D}{\sim} N\left(0, \sigma^{2}\right)
$$

From the difference equation

$$
x_{t}=\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}
$$

The equillibrium distribution, $t \rightarrow \infty$, is normal with mean and vaniance

$$
\begin{aligned}
& \mu_{E}=\lim _{t \rightarrow \infty} E\left(x_{t}\right)=0 \\
& \sigma_{E}^{2}=\lim _{t \rightarrow \infty} E\left(x_{t}^{2}\right)=\frac{\sigma^{2}}{1-\alpha^{2}}
\end{aligned}
$$

## The autocorrelation is defined by

$$
r_{n}=\lim _{t \rightarrow \infty} E\left(x_{t} x_{t-1 n}\right)
$$

To evaluate ru an expression
is needed for $x_{t+h}$
From the difference equation for AR(1) it is seen that

$$
\begin{aligned}
& x_{t+1}=\alpha x_{t}+\varepsilon_{t+1} \\
& x_{t+2}=\alpha x_{t+1}+\varepsilon_{t+2} \\
& x_{t+3}=\alpha x_{t+2}+\varepsilon_{t+3} \\
& \vdots \\
& x_{t+n}=\alpha x_{t+n-1}+\varepsilon_{t+n}
\end{aligned}
$$

putting the pieces logether

$$
\begin{aligned}
x_{t+2} & =\alpha\left(\alpha x_{t}+\varepsilon_{t+1}\right)+\varepsilon_{t+2} \\
& =\alpha^{2} x_{t}+\alpha \varepsilon_{t+1}+\varepsilon_{t-12}
\end{aligned}
$$

$$
\begin{aligned}
x_{t+3} & =\alpha x_{t+2}+\varepsilon_{t+3} \\
& =\alpha\left(\alpha^{2} x_{t}+\alpha \varepsilon_{t+1}+\varepsilon_{t-12}\right)+\varepsilon_{t+3} \\
& =\alpha^{3} x_{t}+\alpha^{2} \varepsilon_{t+1}+\alpha \varepsilon_{t+2}+\varepsilon_{t+3} \\
& =\alpha^{3} x_{t}+\sum_{l=1}^{3} \alpha^{l-1} \varepsilon_{t+l}
\end{aligned}
$$

Finally

$$
x_{t+n}=\alpha^{n} x_{t}+\sum_{l=1}^{n} \alpha^{l-1} \varepsilon_{t+l}
$$

Now
$E\left(x_{t} x_{t+n}\right)=E\left[\alpha^{n} x_{t} x_{t}+\sum_{l=1}^{n} \alpha^{l-1} x_{t} \varepsilon_{t+l}\right]$
$=\alpha^{n} E\left(x_{t}^{2}\right)+\sum_{l=1}^{n} \alpha^{l-1} E\left(x_{t} \varepsilon_{t+l}\right)$
using

$$
x_{t}=\alpha^{t} x_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}
$$

gives with $l>1$
$E\left(x_{t} \varepsilon_{t+l}\right)=E\left[\alpha^{t} x_{0} \varepsilon_{t+l}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i} \varepsilon_{t+l}\right]$

$$
=\alpha^{t} x_{0} E\left(\varepsilon_{t+l}\right)+\sum_{i=1}^{t} \alpha^{t-i} E\left(\varepsilon_{i} \varepsilon_{t+l}\right)
$$

Since

$$
\begin{aligned}
& \varepsilon_{t} \stackrel{\text { ItD }}{\sim} N\left(0, \sigma^{2}\right) \\
& E\left(\varepsilon_{t+l}\right)=0
\end{aligned}
$$

and

$$
E\left(\varepsilon_{i} \varepsilon_{t+l}\right)=0
$$

since $\varepsilon_{i}$ are independent and $i \leq t$ and $l>1$.

So

$$
E\left(X_{t} X_{t+n}\right)=\alpha^{n} E\left(X_{t}^{2}\right)
$$

taking the equilibrium limit $t \rightarrow \infty$
sives

$$
r_{n}=\alpha^{n} \sigma_{E}^{2}
$$

Normalizing gives the autocorrelation coefficient

$$
\gamma_{n}=\frac{r_{n}}{\sigma_{E}^{2}}=2^{n}
$$

## Wiebull Distribution

The Wiebull Distribution is defined by the density
$f(x ; \lambda, k)= \begin{cases}\frac{k}{\lambda}\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x / \lambda)^{k}} & x \geqslant 0 \\ 0 & x<0\end{cases}$
where $\lambda>$ is the scale parameter and $k>0$ is the shape parameter. The cummulative distribution is defined by $x$

$$
\begin{aligned}
& F(x ; \lambda, k)=\int_{0}^{x} f(y, \lambda k) d y \\
& =\int_{0}^{x} \frac{k}{\lambda}\left(\frac{y}{\lambda}\right)^{k-1} e^{-(y / \lambda)^{k}} d y
\end{aligned}
$$

let

$$
\omega=\frac{y}{\lambda} \Rightarrow \lambda d \omega=d y
$$

$$
\begin{aligned}
& \text { So } \\
& \begin{aligned}
F(x ; \lambda, k) & =\frac{k}{\lambda} \int_{0}^{x / \lambda} \omega^{k-1} e^{-\omega^{k}} \lambda d \omega \\
& =k \int_{0}^{x / \lambda} \omega^{k-1} e^{-\omega^{k}} d \omega \\
\text { Now let } & d z=k \omega^{k-1} d \omega \\
z=\omega^{k} \Rightarrow & \\
\text { So } & \begin{aligned}
F(x ; \lambda, k) & =\int_{0}^{\left(\frac{x}{\lambda}\right)^{k}} e^{-2} d z \\
& =-\left.e^{-2}\right|_{0} ^{\left(\frac{x}{\lambda}\right)^{k}} \\
& =-\left[e^{-\left(\frac{x}{\lambda}\right)^{k}}-1\right] \\
& =1-e^{-\left(\frac{x}{\lambda}\right)^{k}}
\end{aligned}
\end{aligned}
\end{aligned}
$$

This CDF is invertable so the Inverse CDF method can be used to generate samples.
Let $u$ be a value of the Cumlative Distribution with
$0 \leqslant u \leqslant 1$, then

$$
\begin{aligned}
& u=1-e^{-(x / \lambda)^{k}} \\
\Rightarrow & e^{-(x / \lambda)^{k}}=1-u \\
\Rightarrow & \ln (1-u)=-\left(\frac{x}{\lambda}\right)^{k} \\
\Rightarrow & -\ln (1-u)=\left(\frac{x}{\lambda}\right)^{k} \\
\Rightarrow & \ln \left(\frac{1}{1-u}\right)=\left(\frac{x}{\lambda}\right)^{k} \\
\Rightarrow & x=\lambda\left[\ln \left(\frac{1}{1-u}\right)^{1 / k}\right. \\
\text { The } & \operatorname{mean} \text { is } \int^{i v e n} b y \\
E & (\lambda, k)=\int_{0}^{\infty} x f(x ; \lambda, k) d x \\
= & \int_{0}^{\infty} x\left(\frac{k}{\lambda}\right)\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x / \lambda)^{k}} d x \\
= & \int_{0}^{\infty} k\left(\frac{x}{\lambda}\right)^{k} e^{-(x / \lambda)^{k}} d x
\end{aligned}
$$

$$
\text { let } \omega=\frac{x}{\lambda} \Rightarrow \lambda d \omega=d x
$$

then

$$
E_{x}(\lambda, k)=\int_{0}^{\infty} \lambda k \omega^{k} e^{-\omega^{k}} d \omega
$$

Consider the crange of variable

$$
z=\omega^{k} \Rightarrow d z=k \omega^{k-1} d \omega
$$

but

$$
\omega=z^{1 / k}
$$

50

$$
\begin{aligned}
d z & =k z^{\frac{k-1}{k}} d \omega \\
\Rightarrow \quad d \omega & =\frac{1}{k} z^{-\left(\frac{k-1}{k}\right)} d z
\end{aligned}
$$

Then

$$
\begin{aligned}
& E_{x}(\lambda, k)=\int_{0}^{-\infty} \lambda k z e^{-z}\left[\frac{1}{k} z^{-\left(\frac{k-1}{k}\right)}\right] d z \\
& =\int_{0}^{\infty} \lambda z^{1-\left(\frac{k-1}{k}\right)} e^{-z} d z
\end{aligned}
$$

$$
\begin{aligned}
& =\lambda \int_{0}^{\infty} z^{(k-k+1) k} e^{-z} \\
& =\lambda \int_{0}^{\infty} z^{1 / k} e^{-z} d z
\end{aligned}
$$

Now the Eamma Function is defined by $\infty$

$$
\Gamma(l)=\int_{0}^{\infty} x^{l-1} e^{-z} d z, k>0
$$

80

$$
E_{x}(\lambda, k)=\lambda \int_{0}^{\infty} z^{\left(\frac{k}{k}+1\right)-1} e^{-z} d z
$$

$$
=\lambda \Gamma\left(1+V_{k}\right)
$$

The variance is given by

$$
\operatorname{Var}_{x}(\lambda, k)=E_{x}^{2}(\lambda, k)-\left[E_{x}(\lambda, k)\right]
$$

Now

$$
\begin{aligned}
& E_{x^{2}}(\lambda, k)=\int_{0}^{-\infty} x^{2} f(x ; \lambda, k) d x \\
& =\int_{0}^{\infty} x^{2}\left(\frac{k}{\lambda}\right)\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x / \lambda)^{k}} d x
\end{aligned}
$$

$$
\begin{aligned}
& =\int_{0}^{\infty}\left(x^{2} \frac{\lambda}{\lambda}\right)\left(\frac{k}{\lambda}\right)\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x / \lambda)^{k}} d x \\
& =\int_{0}^{\infty} \lambda k\left(\frac{x}{\lambda}\right)^{2}\left(\frac{x}{\lambda}\right)^{k-1} e^{-(x / \lambda)^{k}} d x \\
& =\int_{0}^{\infty} \lambda k\left(\frac{x}{\lambda}\right)^{k+1} e^{-(x / \lambda)^{k}} d x
\end{aligned}
$$

let

$$
\begin{aligned}
& \omega=\frac{x}{\lambda} \Rightarrow \lambda d \omega=d x \\
& \text { so } \\
& E_{x^{2}}(\lambda, k)=\int_{0}^{\infty} \lambda^{2} k \omega^{k+1} e^{-\omega^{k}} d \omega \\
& \text { using anothe change of } \\
& \text { variables } \\
& z=\omega^{k} \Rightarrow d z=k \omega^{k-1} d \omega
\end{aligned}
$$

but

$$
\omega=z^{1 / k}
$$

so

$$
\begin{aligned}
d z & =k\left(z^{1 / k}\right)^{k-1} d \omega \\
& =k z^{k-1 / k} d \omega \\
\Rightarrow d \omega & =\frac{1}{k} z^{1-k / k} d z \\
& =\frac{1}{k} z^{1 / k-1} d z
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E_{x^{2}}(\lambda, k)=\int_{0}^{\infty} \lambda^{2} k\left(z^{1 / k}\right)^{k+1} e^{-2}\left(\frac{1}{k} z^{1 / k-1}\right) d z \\
= & \lambda^{2} \int_{0}^{\infty} z^{k+1 / k} z^{1 / k-1} e^{-2} d z \\
= & \lambda^{2} \int_{0}^{\infty} z^{1+1 / k+1 / k-1} e^{-2} d z \\
= & \lambda^{2} \int_{0}^{\infty} z^{2 / k} e^{-2} d z
\end{aligned}
$$

Now the Camma Function is defined by $\infty$

$$
\Gamma(l)=\int_{0}^{\infty} x^{l-1} e^{-z} d z, \quad k>0
$$

50

$$
\begin{aligned}
E_{x^{2}}(\lambda, k) & =\lambda^{2} \int_{0}^{\infty} z^{1+2 / k-1} e^{-2} d z \\
& =\lambda^{2} \Gamma(1+2 / k)
\end{aligned}
$$

So

$$
\begin{aligned}
& \operatorname{Var} x(\lambda, k)=E_{x}^{2}(\lambda, k)-\left[E_{x}(\lambda, k)\right] \\
& =\lambda^{2} \Gamma(1+2 / k)-[\lambda \Gamma(1+1 / k)]^{2} \\
& =\lambda^{2}\left\{\Gamma(1+2 / k)-[\Gamma(1+1 / k)]^{2}\right.
\end{aligned}
$$

Sum of Two Normal Random Variables
Consider the sam of two
Nermal random variables

$$
I=Z_{1}+\underline{X}_{2}
$$

where

$$
\begin{aligned}
& \mu_{i}=E\left(\bar{Z}_{i}\right) \\
& \sigma_{i}^{2}=E\left(\bar{X}_{i}^{2}\right)-\mu_{i}^{2} \\
& f_{X_{i}}\left(x_{i}\right)=\frac{1}{\sqrt{2 \pi \sigma_{i}^{2}}} e^{-\left(x_{i}-\mu_{i}^{2}\right)^{2} / 2 \sigma_{i}^{2}}
\end{aligned}
$$

In general the distribution for a sum of $N$ random variables

$$
f_{I}(y)=\iint \ldots \int \prod_{y=\sum_{i=1}^{N} x_{i}}^{N} f_{I_{i}}\left(x_{i}\right) d x_{1} d x_{2} \cdots d x_{N}
$$

For two random variables this becomes

$$
f_{Z}(y)=\int f_{\underline{1}_{1}}\left(y-x_{2}\right) f_{\bar{x}_{2}}\left(x_{2}\right) d x_{2}
$$

where

$$
\overline{\underline{Y}}=\underline{\underline{X}}_{1}+\underline{\underline{X}}_{2}
$$

and

$$
y=x_{1}+x_{2} \Rightarrow \quad x_{1}=y-x_{2}
$$

Now

$$
\begin{gathered}
f_{\Pi}(y)=\int_{-\infty}^{\infty}\left[\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} e^{-\left(y-x_{2}-\mu_{1}\right)^{2} / 2 \sigma_{1}^{2}}\right] \\
{\left[\frac{1}{2 \pi \sigma_{2}^{2}} e^{-\left(x_{2}-\mu_{2}\right)^{2} / 2 \sigma_{2}^{2}}\right] d x_{2}}
\end{gathered}
$$

Consider the exponential orgument

$$
\begin{aligned}
& -\left(y-x_{2}-\mu_{1}\right)^{2} \frac{1}{2 \sigma_{1}^{2}}-\left(x_{2}-\mu_{2}\right)^{2} \frac{1}{2 \sigma_{2}^{2}} \\
& =-\frac{\sigma_{2}^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left(y^{2}+x_{2}^{2}+\mu_{1}^{2}-2 y x_{2}-2 y_{1} \mu_{1}+2 x_{2} \mu_{1}\right) \\
& \quad-\frac{\sigma_{1}^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left(x_{2}^{2}+\mu_{2}^{2}-2 x_{2} \mu_{2}\right) \\
& =-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left[\sigma_{2}^{2}\left(x_{1}^{2}+x_{2}^{2}+\mu_{1}^{2} \cdot 2 y_{1} x_{2}-2 y \mu_{1}+2 x_{2} \mu_{1}\right)\right. \\
& \left.\sigma_{1}^{2}\left(x_{2}^{2}+\mu_{2}^{2}-2 x_{2} \mu_{2}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}} \begin{aligned}
\left\{\sigma_{2}^{2} y^{2}+x_{2}^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right) \cdot 2 x_{2}\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)\right.\right. & \left.\left.+\sigma_{1}^{2} \mu_{2}\right]+\sigma_{2}^{2}\left(\mu_{1}^{2}-2 y_{1} \mu_{1}\right)+\sigma_{1}^{2} \mu_{2}^{2}\right\}
\end{aligned} \\
& =-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}} \begin{aligned}
\{ & x_{2}^{2}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)-2 x_{2}\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right] \\
& \left.+\sigma_{2}^{2}\left(y^{2}+\mu_{1}^{2}-2 y \mu_{1}\right)+\sigma_{1}^{2} \mu_{2}^{2}\right\}
\end{aligned} \\
& \text { let } \quad \sigma^{2}=\sigma_{1}^{2}+\sigma_{2}^{2}
\end{aligned}
$$

then

$$
\begin{aligned}
-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}} & \left\{\sigma^{2} x_{2}^{2}-2 x_{2}\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]\right. \\
& \left.+\sigma_{2}^{2}\left(y^{2}+\mu_{1}^{2}-2 y \mu_{1}\right)+\sigma_{1}^{2} \mu_{2}^{2}\right\} \\
=\frac{-\sigma^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}} & \left\{x_{2}^{2}-2 x_{2} \frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right. \\
& \left.+\frac{\sigma_{2}^{2}\left(y^{2}+\mu_{1}^{2}-2 y \mu_{1}\right)+\sigma_{1}^{2} \mu_{2}}{\sigma^{2}}\right\} \\
= & -\frac{\sigma^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left\{x_{2}^{2}-2 x_{2}\left[\frac{\left.\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right]\right. \\
& +\left(\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right)^{2} \\
& \left.-\left(\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}^{2}\right]}{\sigma^{2}}\right]\right)^{2}
\end{aligned}
$$

$$
\begin{aligned}
+ & \left.\frac{\sigma_{2}^{2}\left(y^{2}+\mu_{1}^{2}-2 y \mu_{1}\right)+\sigma_{1}^{2} \mu_{2}^{2}}{\sigma^{2}}\right\} \\
= & -\frac{\sigma^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left\{\left(x_{2}-\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right)^{2}\right. \\
& -\left(\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right)^{2} \\
& \left.+\frac{\sigma_{2}^{2}\left(y-\mu_{1}\right)^{2}+\sigma_{1}^{2} \mu_{2}^{2}}{\sigma^{2}}\right\}
\end{aligned}
$$

Consider the last two terms.

$$
\begin{aligned}
& \frac{\sigma_{2}^{2}\left(y-\mu_{1}\right)^{2}+\sigma_{1}^{2} \mu_{2}^{2}}{\sigma^{2}}-\left(\frac{\left.\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]\right)^{2}}{\sigma^{2}}\right. \\
& =\frac{1}{\sigma^{2}}\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)^{2}+\sigma_{1}^{2} \mu_{2}^{2}\right]-\frac{1}{\sigma^{4}}\left[\sigma_{2}^{4}\left(y-\mu_{1}\right)^{2}\right. \\
& \left.+2 \sigma_{1}^{2} \sigma_{2}^{2} \mu_{2}\left(y-\mu_{1}\right)+\sigma_{1}^{4} \mu_{2}^{2}\right] \\
& \frac{1}{\sigma^{4}}\left[\sigma^{2} \sigma_{2}^{2}\left(y-\mu_{1}\right)^{2}-\sigma_{2}^{4}\left(y-\mu_{1}\right)^{2}+\sigma^{2} \sigma_{1}^{2} \mu_{2}^{2}\right. \\
& \left.-\sigma_{1}^{4} \mu_{2}^{2}-2 \sigma_{1}^{2} \sigma_{2}^{2} \mu_{2}\left(y-\mu_{1}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
=\frac{1}{\sigma^{4}} & {\left[\left(y-\mu_{1}\right)^{2} \sigma_{2}^{2}\left(\sigma^{2}-\sigma_{2}^{2}\right)+\sigma_{1}^{2} \mu_{2}^{2}\left(\sigma^{2}-\sigma_{1}^{2}\right)\right.} \\
& \left.-2 \sigma_{1}^{2} \sigma_{2}^{2} \mu_{2}\left(y-\mu_{1}\right)\right]
\end{aligned}
$$

using $\sigma_{1}^{2}=\sigma^{2}-\sigma_{2}^{2}$ and $\sigma_{2}^{2}=\sigma^{2}-\sigma_{1}^{2}$ gives

$$
\begin{aligned}
=\frac{1}{\sigma^{4}} & {\left[\sigma_{1}^{2} \sigma_{2}^{2}\left(y-\mu_{1}\right)^{2} \cdot 2 \sigma_{1}^{2} \sigma_{2}^{2} \mu_{2}(y-\mu)\right.} \\
& \left.+\sigma_{1}^{2} \sigma_{2}^{2} \mu_{2}^{2}\right]
\end{aligned}
$$

$=\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma^{4}}\left[\left(y-\mu_{1}\right)^{2}-2 \mu_{2}\left(y-\mu_{1}\right)+\mu_{2}^{2}\right]$
$=\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma^{4}}\left[\left(y-\mu_{1}\right)-\mu_{2}\right]^{2}$
$=\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{4}^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}$
Bringing things logether
$-\frac{\sigma^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left\{\left(x_{2}-\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right)^{2}+\right.$

$$
\left.\frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{4}^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}\right\}
$$

$$
\begin{gathered}
=-\frac{\sigma^{2}}{2 \sigma_{1}^{2} \sigma_{2}^{2}}\left(x_{2}-\frac{\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]}{\sigma^{2}}\right)^{2} \\
-\frac{1}{2 \sigma^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}
\end{gathered}
$$

Returning to the integral

$$
\begin{aligned}
f_{I}(y) & =\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}} \frac{1}{2 \pi \sigma_{2}^{2}} \int_{-\infty}^{\infty} \exp \left\{-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2} / \sigma^{2}}\left(x_{2}\right.\right.} \\
- & {\left.\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]\right)^{2} } \\
- & \left.\frac{1}{2 \sigma^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}\right\} d x_{2} \\
=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} & \frac{1}{2 \pi \sigma_{2}^{2}} \exp \left[-\frac{1}{2 \sigma^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}\right] \\
& \int_{-\infty}^{\infty} \exp \left\{-\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2} / \sigma^{2}}\left(x_{2}\right.\right. \\
& \left.\left.-\left[\sigma_{2}^{2}\left(y-\mu_{1}\right)+\sigma_{1}^{2} \mu_{2}\right]\right)^{2}\right\} d x_{2}
\end{aligned}
$$

$$
\begin{aligned}
= & \exp \left[\frac{-1}{2 \sigma^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}\right] \frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} \frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \\
& \left(\sqrt{\frac{2 \pi \sigma_{1}^{2} \sigma_{2}^{2}}{\sigma^{2}}}\right) \\
= & \frac{1}{2 \pi \sigma^{2}} \exp \left[\frac{1}{2 \sigma^{2}}\left(y-\mu_{1}-\mu_{2}\right)^{2}\right]
\end{aligned}
$$

Which is a Normal distribution with mean and standard deviation

$$
\begin{aligned}
& \mu=\mu_{1}+\mu_{2} \\
& \sigma^{2}=\sigma_{1}^{2}+\sigma_{2}^{2}
\end{aligned}
$$

Moment Eenerating Function
The moment generating function for a random variable $\bar{x}$ is defined by

$$
M(s)=E\left[e^{s x}\right]
$$

where

$$
E\left[\bar{X}^{n}\right]=\left.\frac{d^{n} \mu}{d s}\right|_{s=0}
$$

If $\bar{X}$ is Normal then

$$
\begin{aligned}
\mu(s) & =\frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{s x} e^{-(x-\mu)^{2} / 2 \sigma^{2}} d x \\
& =\frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{-(x-\mu)^{2} / 2 \sigma^{2}+s x} d x
\end{aligned}
$$

consider the argument of the
$\frac{1}{2 \sigma^{2}}(x-\mu)^{2}-s x=\frac{1}{2 \sigma^{2}}\left(x^{2}-2 x \mu+\mu^{2}\right)-s x$
$=\frac{1}{2 \sigma^{2}}\left(x^{2}-2 x \mu+\mu^{2}-2 \sigma^{2} s x\right)$
$=\frac{1}{2 \sigma^{2}}\left[x^{2}-2 x\left(\mu+\sigma^{2} s\right)+\mu^{2}\right]$
$=\frac{1}{2 \sigma^{2}}\left[x^{2}-2 x\left(\mu+\sigma^{2} s\right)+\left(\mu+\sigma^{2} s\right)^{2}\right. \left.-\left(\mu+\sigma^{2} s\right)^{2}+\mu^{2}\right]$
$=\frac{1}{2 \sigma^{2}}\left[\left(x-\mu-\sigma^{2} s\right)^{2}-\left(\mu+\sigma^{2} s\right)^{2}+\mu^{2}\right]$

$$
\begin{aligned}
& =\frac{1}{2 \sigma^{2}}\left(x-\mu-\sigma^{2} s\right)^{2}-\frac{1}{2 \sigma^{2}}\left(\mu^{2}+2 \mu \sigma^{2} s+\sigma^{4} s^{2}\right. \\
& \left.-\mu^{2}\right) \\
& =\frac{1}{2 \sigma^{2}}\left(x-\mu-\sigma^{2} s\right)^{2}-\frac{1}{2 \sigma^{2}}\left(\sigma^{4} s^{2}+2 \mu \sigma^{2} s\right) \\
& =\frac{1}{2 \sigma^{2}}\left(x-\mu-\sigma^{2} s\right)^{2}-\left(\frac{1}{2} \sigma^{2} s^{2}+\mu s\right)
\end{aligned}
$$

Putting things together

$$
\begin{aligned}
& \mu(s)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} \exp \left\{\frac{-1}{2 \sigma^{2}}\left(x-\mu+\sigma^{2} s\right)^{2}\right\} \\
& \exp \left(\frac{1}{2} \sigma^{2} s^{2}+\mu s\right) d x \\
& =\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-\frac{1}{2} \sigma^{2} s^{2}+\mu s} \int_{-\infty}^{\infty} \exp \left\{\frac{1}{2 \sigma^{2}}\left(x-\mu \cdot \sigma^{2} s\right)^{2}\right\} d x \\
& =e^{\frac{1}{2} \sigma^{2} s^{2}+\mu s} \frac{1}{\sqrt{2 \pi \sigma^{2}}} \sqrt{2 \pi \sigma^{2}} \\
& =e^{\frac{1}{2} \sigma^{2} s^{2}+\mu s}
\end{aligned}
$$

For the sum of independent normal
random variables

$$
\underline{Y}=\underline{X}_{1}+\underline{X}_{2}
$$

where I has mean and variace

$$
\begin{aligned}
& \mu=\mu_{1}+\mu_{2} \\
& \sigma^{2}=\sigma_{1}^{2}+\sigma_{2}^{2}
\end{aligned}
$$

the moment
is the senerating function

## Bivarite Gaussian

Let, $I_{1}$ and $\bar{X}_{2}$ be independent unt Normal random variables. Define $I_{1}$ and $I_{2}$ as linear combinations of ${ }^{2} \bar{I}_{1}$ and $\bar{I}_{2}$

$$
\binom{I_{1}-\mu_{1}}{I_{2}-\mu_{2}}=\left(\begin{array}{cc}
\sigma_{1} & 0 \\
\sigma_{2} \rho & \sigma_{2} \sqrt{1-\rho^{2}}
\end{array}\right)\binom{\bar{X}_{1}}{\bar{X}_{2}}
$$

where $\sigma_{1}, \sigma_{2}$ and $\rho$ are scalars with

$$
\sigma_{1}>0, \quad \sigma_{2}>0, \quad-1 \leqslant e \leqslant 1
$$

let

$$
P=\left(\begin{array}{cc}
\sigma_{1} & 0 \\
\sigma_{2} \rho & \sigma_{2} \sqrt{1-\rho^{2}}
\end{array}\right)
$$

then

$$
\binom{\bar{I}_{1}}{\bar{I}_{2}}=P^{-1}\binom{\bar{I}_{1}-\mu_{1}}{\bar{I}_{2}-\mu_{2}}
$$

where $P^{-1}$ is the inverse of $P$ which is given by

$$
P^{-1}=\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\left(\begin{array}{cc}
\sigma_{2} \sqrt{1-\rho^{2}} & 0 \\
-\sigma_{2} \rho & \sigma_{1}
\end{array}\right)
$$

Now since $X_{1}$ and $X_{2}$ are independent unit Normal random variables the joint PDF is given by

$$
f\left(x, x_{2}\right)=\frac{1}{2 \pi} e^{-\frac{1}{2}\left(x_{1}^{2}+x_{2}^{2}\right)}
$$

if

$$
\begin{aligned}
& x_{1}=s_{1}\left(y_{1}, y_{2}\right) \\
& x_{2}=s_{2}\left(y_{1}, y_{2}\right)
\end{aligned}
$$

the joint PDF of $I_{1}$ and $I_{2}$ is given by

$$
g\left(y_{1}, y_{2}\right)=|J| f\left(s_{1}\left(y_{1}, y_{2}\right), s_{2}\left(y_{1}, y_{2}\right)\right)
$$

where $J$ is the Jacobian matrix

$$
J=\left(\begin{array}{ll}
\frac{\partial s_{1}}{\partial y_{1}} & \frac{\partial s_{1}}{\partial y_{2}} \\
\frac{\partial s_{2}}{\partial y_{1}} & \frac{\partial s_{2}}{\partial y_{2}}
\end{array}\right)
$$

using

$$
\begin{gathered}
\binom{\bar{I}_{1}}{\bar{I}_{2}}=P^{-1}\binom{\bar{I}_{1}-\mu_{1}}{\bar{I}_{2}-\mu_{2}} \\
P^{-1}=\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\left(\begin{array}{cc}
\sigma_{2} \sqrt{1-\rho^{2}} & 0 \\
-\sigma_{2} \rho & \sigma_{1}
\end{array}\right)
\end{gathered}
$$

gives

$$
\mathbb{I}_{1}=\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\left[\sigma_{2} \sqrt{1-\rho^{2}}\left(I_{1}-\mu_{1}\right)\right]
$$

$$
\bar{Z}_{2}=\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\left[-\rho \sigma_{2}\left(\bar{y}_{1}-\mu_{1}\right)+\sigma_{1}\left(\bar{I}_{2}-\mu_{2}\right)\right]
$$

so that

$$
\begin{aligned}
S_{1}\left(y_{1}, y_{2}\right)= & \frac{1}{\sigma_{1} \sigma_{2} 1-\rho^{2}}\left[\sigma_{2} \sqrt{1-\rho^{2}}\left(y_{1}-\mu_{1}\right)\right] \\
= & \frac{1}{\sigma_{1}}\left(y_{1}-\mu\right) \\
S_{2}\left(y_{1}, y_{2}\right)= & \frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}\left[\sigma_{1}\left(y_{2}-\mu_{2}\right)\right. \\
& \left.-\rho \sigma_{2}\left(y_{1}-\mu_{1}\right)\right]
\end{aligned}
$$

The terms of the Jacobian are given by
$\frac{\partial S_{1}}{\partial y_{1}}=\frac{1}{\sigma_{1}} \quad \frac{\partial S_{1}}{\partial y_{2}}=0$

$$
\frac{\partial S_{2}}{\partial y_{1}}=\frac{-}{\sigma_{1} \sqrt{1-\rho^{2}}} \quad \frac{\partial S_{2}}{\partial y_{2}}=\frac{1}{\sigma_{2} \sqrt{1-\rho^{2}}}
$$

then

$$
\begin{aligned}
|J| & =\frac{\partial S_{1}}{\partial y_{1}} \frac{\partial S_{2}}{\partial y_{2}}-\frac{\partial S_{1}}{\partial y_{2}} \frac{\partial S_{2}}{\partial y_{1}} \\
& =\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}
\end{aligned}
$$

Next consider the exponential argument of the $\bar{X}_{1}, \bar{X}_{2}$ PDF

$$
\begin{aligned}
& x_{1}^{2}+x_{2}^{2}=s_{1}\left(y_{1}, y_{2}\right)^{2}+s_{2}\left(y_{1}, y_{2}\right)^{2} \\
= & {\left[\frac{1}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)\right]^{2}+\left\{\frac { 1 } { \sigma _ { 1 } \sigma _ { 2 } \sqrt { 1 - \rho ^ { 2 } } } \left[\sigma_{1}\left(y_{2}-\mu_{2}\right)\right.\right.} \\
- & \left.\left.\rho \sigma_{2}\left(y_{1}-\mu_{1}\right)\right]\right\}^{2} \\
= & \frac{1}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}+\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left[\sigma_{1}\left(y_{2}-\mu_{2}\right)\right. \\
& \left.-\rho \sigma_{2}\left(y_{1}-\mu_{1}\right)\right]^{2}
\end{aligned}
$$

$$
\begin{aligned}
&= \frac{1}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}+\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left\{\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)^{2}\right. \\
&-2 \rho \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right) \\
&\left.+\rho^{2} \sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)^{2}\right\} \\
&= \frac{1}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}+\frac{1}{1-\rho^{2}}\left\{\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right. \\
&\left.-\frac{2 \rho}{\sigma_{1} \sigma_{2}}\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right)+\frac{\rho^{2}}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}\right\} \\
&= \frac{1}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}+\frac{\rho^{2}}{1-\rho^{2}} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}} \\
&+ \frac{1}{1-\rho^{2}}\left(y_{2}-\mu_{2}\right)^{2}-\frac{2 \rho}{\sigma_{2}^{2}}\left(\frac{y_{2}-\mu_{2}}{\sigma_{1} \sigma_{2}} y_{1}-\mu_{1}\right) \\
&=\left(y_{1}-\mu_{1}\right)^{2}\left(1+\frac{\rho^{2}}{\sigma_{1}^{2}}\right)+\frac{1}{1-\rho^{2}}\left(y_{2}-\mu_{2}\right)^{2} \\
&-\frac{2 \rho}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right) \\
& \sigma_{1} \sigma_{2}
\end{aligned}
$$

$$
\begin{aligned}
= & \left(y_{1}-\mu_{1}\right)^{2}\left(\frac{1-\rho^{2}}{\sigma_{1}^{2}}+\frac{\rho^{2}}{1-\rho^{2}}\right)+\frac{1}{1-\rho^{2}} \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
& -\frac{2 \rho}{1-\rho^{2}} \frac{\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right)}{\sigma_{1} \sigma_{2}} \\
= & \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}} \frac{1}{1-\rho_{2}}+\frac{1}{1-\rho^{2}} \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
= & \frac{2 \rho}{1-\rho_{2}} \frac{\left.\left(y_{2}-\mu_{2}\right) y_{1}-\mu_{1}\right)}{\sigma_{1} \sigma_{1}} \\
= & \frac{1}{1-\rho^{2}}\left\{\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right. \\
& \left.-2 \rho\left(y_{1}-\mu_{1}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right\}
\end{aligned}
$$

It follows that the jointly vormal density of two variables is given by

$$
\begin{aligned}
& g\left(y_{1}, y_{2}\right)=1 J \mid f\left(s_{1}\left(y_{1}, y_{2}\right), s_{2}\left(y_{1}, y_{2}\right)\right) \\
& \text { where } \\
& |J|=\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}} \\
& \text { so, } \\
& g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[ \right. \\
& \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
& \left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\}
\end{aligned}
$$

A more compact method of
writing this facilitates extension to nigher dimensions is obtained by letting

$$
\begin{gathered}
y=\binom{y_{1}}{y_{2}} \quad \mu=\binom{\mu_{1}}{\mu_{2}} \\
P=\left(\begin{array}{cc}
\sigma_{1}^{2} & \rho \sigma_{1} \sigma_{2} \\
\rho \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right)
\end{gathered}
$$

Where $P$ is referred to as the correlation matrix

Now

$$
\begin{aligned}
|D| & =\sigma_{1}^{2} \sigma_{2}^{2}-\rho^{2} \sigma_{1}^{2} \sigma_{2}^{2} \\
& =\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)
\end{aligned}
$$

and

$$
P^{-1}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\rho \sigma_{1} \sigma_{2} \\
-\rho \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right)
$$

Next consider

$$
(y-\mu)^{\top} P^{-1}(y-\mu)
$$

for the two rightmost terms

$$
\begin{aligned}
& P^{-1}(y-\mu) \\
= & \frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\rho \sigma_{1} \sigma_{2} \\
-\rho \sigma_{1} \sigma_{2} & \sigma_{1} 2
\end{array}\right)\binom{y_{1}-\mu_{1}}{y_{2}-\mu_{2}} \\
= & \frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\binom{\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\rho \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)}{-\rho \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)}
\end{aligned}
$$

Including the leftmost terms

$$
\begin{aligned}
& \text { gives } \\
& \qquad(y-\mu)^{\top} P^{-1}(y-\mu)
\end{aligned}
$$

$$
\begin{array}{r}
=\left(y_{1}-\mu_{1} y_{2}-\mu_{2}\right) \frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)} \\
\binom{\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\rho \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)}{-\rho \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)}
\end{array}
$$

$$
\begin{aligned}
= & \frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left\{\left[\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\rho \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)\right]\right. \\
& \left(y_{1}-\mu_{1}\right)+\left[-\rho \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)\right] \\
& \left.\left(y_{2}-\mu_{2}\right)\right\} \\
= & \frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left[\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)^{2}\right. \\
- & \rho \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)\left(y_{2}-\mu_{2}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)^{2} \\
- & \left.\rho \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)\left(y_{2}-\mu_{2}\right)\right] \\
= & \frac{\sigma_{1}^{2} \sigma_{2}^{2}}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\left(y_{2}-\mu_{2}\right)^{2}\right. \\
& \left.-2 \rho\left(y_{1}^{2}-\mu_{1}\right)\left(y_{2}-\mu_{2}\right)\right]
\end{aligned}
$$

Comparing with the previous
result

$$
\begin{aligned}
& g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[ \right. \\
& \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
& \left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\}
\end{aligned}
$$

gives

$$
\frac{1}{\sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}=\frac{1}{\sqrt{|D|}}
$$

and

$$
\begin{aligned}
& \frac{1}{1-\rho^{2}}\left\{\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right. \\
& \left.-2 \rho\left(y_{1}-\mu_{1}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right\} \\
& =(y-\mu)^{\top} P^{-1}(y-\mu)
\end{aligned}
$$

So

$$
\begin{aligned}
& g\left(y_{1}, y_{2}\right)= \\
& \frac{1}{2 \pi||P|} \exp \left[-\frac{1}{2}(y-\mu)^{\top} P^{-1}(y-\mu)\right]
\end{aligned}
$$

For a distribution with an arbitrary number of dimensions the covariance Matrix is defined by

$$
P_{i j}=\operatorname{Cov}\left(\bar{I}_{i}, \bar{I}_{j}\right)
$$

where the diagonal is given by

$$
\begin{aligned}
P_{i i} & =\operatorname{Cov}\left(\bar{I}_{i}, \bar{I}_{i}\right) \\
& =\operatorname{Var}\left(\bar{I}_{1}\right)=\sigma_{i}^{2}
\end{aligned}
$$

The linear transformation corresponding to a given couariance matrix is fount using Cholesky decomposition.

* Marsinal Distributions

The $y_{1}$ marginal distribution is given by
$g\left(y_{1}\right)=\int_{-\infty}^{\infty} g\left(y_{1}, y_{2}\right) d y_{2}$

$$
=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \int_{-\infty}^{\infty} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[\right.
$$

$\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}$
$\left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\} d y_{2}$

$$
\begin{aligned}
= & \frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right\} \\
& \int_{-\infty}^{\infty} \exp \left\{\frac { - 1 } { \partial ( 1 - \rho ^ { 2 } ) } \left[\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right.\right. \\
- & \left.\left.2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\} d / 2
\end{aligned}
$$

Consider the argument of the exponential

$$
\begin{aligned}
& \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}} \\
& =\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}} \\
& +\rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}-\rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}} \\
& =\left[\frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}-\rho \frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}}\right]^{2}-\rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}
\end{aligned}
$$

so the integral becomes

$$
\begin{aligned}
& \frac{1}{2 \pi \sigma_{1} \sigma_{2} d\left(-\rho^{2}\right.} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right\} \\
& \exp \left\{\frac{1}{\partial\left(1-\rho^{2}\right)} \rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right\} \\
& \int_{-\infty}^{\infty} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}\left[\frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}-\rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right)\right]^{2}\right\} d y_{2}
\end{aligned}
$$

considering just the integral
$\int_{-\infty}^{\infty} \exp \left\{\frac{-1}{a\left(1-e^{2}\right)}\left[\frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}-\rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right)\right]^{2}\right\} d / 2$
$=\int_{-\infty}^{\infty} \exp \left\{\frac{-1}{2 \sigma_{2}^{2}\left(1-\rho^{2}\right)}\left[y_{2}-\mu_{2}-\frac{\rho \sigma_{2}}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)\right]^{2}\right\} d y_{2}$
$=\sqrt{2 \pi \sigma_{2}^{2}\left(1-\rho^{2}\right)}$
It follows that the marginal distribution for $y_{1}$ is

$$
\begin{aligned}
g\left(y_{1}\right)= & \frac{1}{2 \pi \sigma_{1} \sigma_{2} 11-\rho^{2}} \exp \left\{\frac{-1}{2\left(1-\rho^{2}\right)} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right\} \\
& \exp \left\{\frac{1}{2\left(1-\rho^{2}\right)} \rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right\} \\
& \sqrt{2 \pi \sigma_{2}^{2}\left(1-\rho^{2}\right)} \\
= & \frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} \exp \left\{\frac{-1}{2\left(1-\rho^{2}\right)}\left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\left(1-\rho^{2}\right)\right]\right\} \\
= & \frac{1}{2 \pi \sigma_{1}^{2}} \exp \left[\frac{-\left(y_{1}-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}\right]
\end{aligned}
$$

It follows the $g\left(y_{1}\right)$ is Normal with mean $\mu$, and standard deviation $\sigma$,
Similary the margiral distribution for $y_{2}$ is given by
$g\left(y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left[-\frac{\left(y_{2}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}\right]$
which is Normal with mean $\mu_{2}$ and standar deviation $\sigma_{2}$.

* Conditional Distribution

The conditional PDF of $I_{1}$, given $I_{2}$ is defined

$$
g\left(y_{1} \mid y_{2}\right)=\frac{g\left(y_{1}, y_{2}\right)}{g\left(y_{2}\right)}
$$

Now

$$
\begin{aligned}
& g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d\left(-\rho^{2}\right.} \exp \left\{\frac{-1}{2\left(1-\rho^{2}\right)}[ \right. \\
& \quad \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
& \left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\}
\end{aligned}
$$

and

$$
g\left(y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left[-\frac{\left(y_{2}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}\right]
$$

50

$$
\begin{aligned}
& g\left(y_{1} \mid y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[ \right. \\
& \left.\left.\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-\partial \rho \frac{\left.\left(y_{1}-\mu_{1}\right) x_{y_{2}-\mu_{2}}\right)}{\sigma_{1}}\right]\right\} \\
& \exp \left[\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\partial \sigma_{2}^{2}}\right] \\
& =\frac{1}{\partial \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)} \exp \left\{\frac { - 1 } { \partial ( 1 - \rho ^ { 2 } ) } \left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}\right.\right. \\
& \left.\left.-\partial \rho \frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}} \frac{\left.y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)} \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right. \\
& \left.+\left(\frac{y_{2}-\mu_{2}}{\partial \sigma_{2}^{2}}\right)^{2}\right\}
\end{aligned}
$$

Consider the argument of the first exponential

$$
\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}-2 \rho \frac{\left(y_{1}-\mu_{1} x_{y_{2}-\mu_{2}}\right)}{\sigma_{1}}+\frac{\rho^{2}\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}
$$

$$
\begin{aligned}
- & \rho^{2} \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
= & \frac{1}{\sigma_{1}^{2}}\left\{\left(y_{1}-\mu_{1}\right)^{2}-\frac{2 \rho \sigma_{1}}{\sigma_{2}}\left(y_{1}-\mu_{1}\right)\left(y_{2}-\mu_{2}\right)\right. \\
& \left.+\frac{\rho^{2} \sigma_{1}^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}-\rho^{2} \frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}\right\} \\
= & \frac{1}{\sigma^{2}}\left\{\left[y_{1}-\mu_{1}-\frac{\rho \sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right]^{2}-\frac{\rho \sigma_{1}^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}\right\} \\
= & \frac{1}{\sigma_{1}^{2}}\left\{\left[y_{1}-\left(\mu_{1}+\frac{\rho \sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right]^{2}-\frac{\rho \sigma_{1}^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}\right\}\right.
\end{aligned}
$$

Next consider the second exponential argument with as ( $y_{2}-\mu_{2}$ ) term above

$$
\begin{aligned}
& \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-\frac{1}{\left(1-\rho^{2}\right)}\left\{\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-\frac{\rho^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}\right\} \\
= & \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}\left(1-\rho^{2}\right)}\left(1-\rho^{2}\right) \\
= & \frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-\left(y_{2}-\frac{\mu_{2}}{\sigma_{2}^{2}}\right)^{2}=0
\end{aligned}
$$

putting things together

$$
\begin{aligned}
& g\left(y_{1} \mid y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac{-1}{2\left(1-\rho^{2}\right)}\right. \\
& \left.\frac{1}{\sigma_{1}^{2}}\left[y_{1}-\left(\mu_{1}+\frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right)\right]^{2}\right\} \\
& =\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac { - 1 } { 2 \sigma _ { 1 } ^ { 2 } ( 1 - \rho ^ { 2 } ) } \left[y_{1}\right.\right. \\
& \left.\left.-\left(\mu_{1}+e \frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right)\right]^{2}\right\}
\end{aligned}
$$

similary
$g\left(y_{2} \mid y_{1}\right)=\frac{g\left(y_{1}, y_{2}\right)}{g\left(y_{1}\right)}$
using
$g\left(y_{1}\right)=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} \exp \left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}\right]$ gives

$$
\begin{aligned}
& g\left(y_{2} \mid y_{1}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[ \right. \\
& \left.\left.\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \rho \frac{\left(y_{1}-\mu_{1} x_{1} y_{2}-\mu_{2}\right)}{\sigma_{1}}\right]\right\} \\
& \sqrt{2 \pi \sigma_{1}^{2}} \exp \left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}\right] \\
& =\sqrt{2 \pi \sigma_{2}^{2}\left(1-\rho^{2}\right)} \exp \left\{\frac { - 1 } { 2 ( 1 - \rho ^ { 2 } ) } \left[\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}\right.\right. \\
& \left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}} x_{y_{2}-\mu_{2}}\right)\right]\right\} \exp \left\{-\frac{1}{\sigma_{2}}\left(y_{1}-\mu_{1}\right)^{2}\right. \\
& \left.+\left(y_{1}-\mu_{1}\right)^{2}\right\}
\end{aligned}
$$

Consider the first exponential argument

$$
\begin{aligned}
& \left.\left(y_{2}-\mu_{2}\right)^{2}-2 \rho\left(y_{1}-\mu_{1}\right) \frac{x_{y_{2}}-\mu_{2}}{\sigma_{1}}\right) \\
& +\rho^{2}\left(y_{\frac{1}{\sigma_{1}}} \sigma_{1}^{2}\right)^{2}-\rho^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{\sigma_{2}^{2}}\left[\left(y_{2}-\mu_{2}\right)^{2}-2 e_{1} \frac{\sigma_{2}}{\sigma_{1}}\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right)\right. \\
& \left.+e^{2} \frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\left(y_{1}-\mu_{1}\right)^{2}\right]-e^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}} \\
= & \frac{1}{\sigma_{2}^{2}}\left[y_{2}-\mu_{2}-\rho \frac{\sigma_{2}}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)\right]^{2} \\
& -e^{2} \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}} \\
= & \frac{1}{\sigma_{2}^{2}}\left[y_{2}-\left(\mu_{2}+\rho \frac{\sigma_{2}}{\sigma_{1}}\left(y_{1}-\mu_{2}\right)\right)\right]^{2} \\
& -e^{2}\left(y_{1}-\mu_{1}\right)^{2}
\end{aligned}
$$

Now consider the second exponential argument and add the $\left(y_{1}-u_{1}\right)^{2}$ term above
$\frac{1}{2\left(1-\rho^{2}\right)}\left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}-\rho^{2} \frac{V}{\sigma_{1}-\mu_{1}{ }^{2}}{ }^{2}\right]-\frac{\left(y_{1}-\mu_{1}\right)^{2}}{2 \sigma_{1}^{2}}$

$$
\begin{aligned}
& =\frac{1}{2\left(1-\rho^{2}\right)}\left(\frac{y-\mu_{1}}{\sigma_{1}^{2}}\right)^{2}\left(1-\rho^{2}\right)-\left(\frac{y_{1}-\mu_{1}}{2 \sigma_{1}^{2}}\right)^{2} \\
& =0
\end{aligned}
$$

Trus

$$
\begin{aligned}
& g\left(y_{2} / y_{1}\right)=\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac{1}{2 \sigma_{1}^{2}\left(1-\rho^{2}\right)}\right. \\
& \left.\left[y_{2}-\left(\mu_{2}+\rho \frac{\sigma_{2}}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)\right)\right]^{2}\right\}
\end{aligned}
$$

Which is the same as $g\left(y_{1} \mid y_{2}\right)$
with

$$
\mu_{1} \rightarrow \mu_{2} \quad \sigma_{1} \rightarrow \sigma_{2} \quad y_{1} \rightarrow y_{2}
$$

## * Conditional Expectalion

The conditional expection of $I_{1}$ given $I_{2}$ is defined by
$E\left[I_{1} \mid I_{2}=y_{2}\right]=\int_{-\infty}^{\infty} y_{1} g\left(y_{1} \mid y_{2}\right) d y_{1}$
but

$$
\begin{aligned}
g\left(y_{1} \mid y_{2}\right)= & \frac{1}{\sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac{-1}{2 \sigma_{1}^{2}\left(1-\rho^{2}\right)}\right. \\
& {\left.\left[y_{1}-\left(\mu_{1}+\frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right)\right]^{2}\right\} }
\end{aligned}
$$

is Normal with mean

$$
\mu_{1}+\rho \frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)
$$

thus

$$
E\left[I_{1}, I_{2}=y_{2}\right]=\mu_{1}+e \frac{\theta_{1}}{\theta_{2}}\left(y_{2}-\mu_{2}\right)
$$

similarly
$E\left[I_{2} \mid I_{1}=y_{1}\right]=\mu_{2}+\rho \frac{\sigma_{2}}{\sigma_{1}}\left(y_{1}-\mu_{2}\right)$

## * Covariance

## The cross correlation is given by

$$
E\left(I_{1} I_{2}\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y_{1} y_{2} g\left(y_{1}, y_{2}\right) d y_{1} d y_{2}
$$

using the definition of conditional probability

$$
g\left(y_{1}, y_{2}\right)=g\left(y_{1} \mid y_{2}\right) g\left(y_{2}\right)
$$

50

$$
\begin{aligned}
& E\left(I_{1} I_{2}\right)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y_{1} y_{2} S\left(y_{1} \mid y_{2}\right) g\left(y_{2}\right) d y_{1} d y_{2} \\
= & \int_{-\infty}^{\infty} y_{2} g\left(y_{2}\right) \int_{-\infty}^{\infty} y_{1} g\left(y_{1} \mid y_{2}\right) d y_{1} d y_{2}
\end{aligned}
$$

Now

$$
g\left(y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left[-\frac{\left(y_{2}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}\right]
$$

and

$$
\begin{aligned}
& g\left(y_{1} \mid y_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)}} \exp \left\{\frac{-1}{2 \sigma_{1}^{2}\left(1-\rho^{2}\right)}\right. \\
& \left.\left[y_{1}-\left(\mu_{1}+\operatorname{e} \frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right)\right]^{2}\right\} \\
& E\left(I_{1} I_{2}\right)=\int_{-\infty}^{\infty} y_{2} \frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} \exp \left[-\left(\frac{y_{2}-\mu_{2}}{2 \sigma_{2}^{2}}\right)^{2}\right] \\
& \int_{-\infty}^{\infty} y_{1} \sqrt{2 \pi \sigma_{1}^{2}\left(1-\rho^{2}\right)} \exp \left\{\frac{-1}{2 \sigma_{1}^{2}\left(1-\rho^{2}\right)}\right. \\
& \left.=\int_{-\infty}^{\infty}\left[y_{1}-\left(\mu_{1}+\frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right)\right]^{2}\right\} d y_{1} d y_{2} \\
& {\left[\mu_{1}+e \frac{\sigma_{1}}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right] d y_{2}} \\
& =\frac{1}{2 \pi \sigma_{2}^{2}} \int_{-\infty}^{\infty} \mu_{1} y_{2} \exp \left[-\left(y_{2}-\mu_{2}\right)^{2}\right] d y_{2}
\end{aligned}
$$

$$
\begin{aligned}
& +\frac{1}{2 \pi \sigma_{2}^{2}} \int_{-\infty}^{\infty} e \frac{\sigma_{1}}{\sigma_{2}} y_{2}\left(y_{2}-\mu_{2}\right) \exp \left[-\frac{\left(y_{2}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}\right] d y_{2} \\
& =\mu_{1} \mu_{2}+e \frac{\sigma_{1}}{\sigma_{2}}\left(\sigma_{2}^{2}+\mu^{2}-\mu^{2}\right) \\
& =\mu_{1} \mu_{2}+e^{\sigma_{1} \sigma_{2}}
\end{aligned}
$$

The covariarce is given by

$$
\begin{aligned}
& \operatorname{Cov}\left(I_{1} I_{2}\right)=E\left(I_{1} I_{2}\right)-E\left(I_{1}\right) E\left(\bar{I}_{2}\right) \\
& =\mu_{1} \mu_{2}+\rho O_{1} O_{2}-\mu_{1} \mu_{2} \\
& =\rho \sigma_{1} \sigma_{2}
\end{aligned}
$$

The correlation coefficent is given by

$$
\rho=\frac{\operatorname{Cov}\left(\bar{Y}_{1} \bar{Y}_{2}\right)}{\sigma_{1} \sigma_{2}}
$$

## * Probability Contours

$$
\begin{aligned}
& g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{1}{2\left(1-\rho^{2}\right)}[ \right. \\
& \frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}} \\
& \left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\}
\end{aligned}
$$

The contours of costant probability are defined constant values of the exponental argument which defines an ellipse.
$\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \rho \frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}} \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}=c$
where $c$ is a constant.
Consider the equation obtained by completing the square

$$
\begin{aligned}
& \left(y_{1}-\mu_{1}\right)^{2}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \rho \frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}} \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}} \\
& +\frac{\rho^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}-\frac{\rho^{2}}{\sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}=c^{2} \\
& =\left[\frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}}-\frac{\rho}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right]^{2} \\
& +\left(y_{\frac{2}{\sigma_{2}^{2}}}\right)^{2}\left(1-\rho^{2}\right)=c^{2} \\
& \Rightarrow \frac{1}{c^{2}}\left[\frac{1}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)-\frac{\rho}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right]^{2} \\
& +\frac{\left(1-\rho^{2}\right)}{c^{2} \sigma_{2}^{2}}\left(y_{2}-\mu_{2}\right)^{2}=1
\end{aligned}
$$

Let

$$
\begin{aligned}
& \sin \theta=\frac{1}{C}\left[\frac{1}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)-\frac{f}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right] \\
& \cos \theta=\frac{\sqrt{1-\rho^{2}}}{C \sigma_{2}}\left(y_{2}-\mu_{2}\right)
\end{aligned}
$$

then

$$
\sin ^{2} \theta+\cos ^{2} \theta=1
$$

Now

$$
y_{2}=\frac{c \sigma_{2}}{\sqrt{1-e^{2}}} \cos \theta+\mu_{2}
$$

and

$$
\sin \theta=\frac{1}{C}\left[\frac{1}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)-\frac{f}{\sigma_{2}}\left(y_{2}-\mu_{2}\right)\right]
$$

$$
=\frac{1}{C}\left[\frac{1}{\sigma_{1}}\left(y_{1}-\mu_{1}\right)-\frac{\rho}{\sigma_{2}} \frac{C \sigma_{2}}{\sqrt{1-\rho^{2}}} \cos \theta\right]
$$

$$
=\frac{1}{c \sigma_{1}}\left(y_{1}-\mu_{1}\right)-\frac{\rho}{\sqrt{1-\rho^{2}}} \cos \theta
$$

$\Rightarrow y_{1}=\cos ,\left[\sin \theta+\frac{\rho}{r^{1-\rho^{2}}} \cos \theta\right]+\mu_{1}$
In summary

$$
y_{1}=\operatorname{co} \sigma_{1}\left[\sin \theta+\frac{f}{\sqrt{1-}^{2}} \cos \theta\right]+\mu_{1}
$$

$$
y_{2}=\frac{c \sigma_{2}}{\sqrt{1-e^{2}}} \cos \theta+\mu_{2}
$$

Consider the limit

$$
\begin{aligned}
& \mu_{1}=\mu_{2}=0 \\
& \rho=0
\end{aligned}
$$

Which is the case of zero mean uncorrelate $y_{1}$ and $y_{2}$

$$
\begin{aligned}
& y_{1}=c \sigma_{1} \sin \theta \\
& y_{2}=c \theta_{2} \cos \theta
\end{aligned}
$$

This is the parametic equation of an ellipse. Furthur

$$
\sigma_{1}=\sigma_{2}=\sigma
$$

$$
\begin{aligned}
& y_{1}=c \sigma \sin \theta \\
& y_{2}=c \sigma \cos \theta
\end{aligned}
$$

which is the parametic
equation of a circle with radius trat is a multiple of the standard deviation.

The values of the contours is given by

$$
\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left[\frac{-c^{2}}{\partial\left(1-\rho^{2}\right)}\right]=v
$$

where $U$ is the contour value. so

$$
\begin{aligned}
& \exp \left[\frac{-c^{2}}{2\left(1-\rho^{2}\right)}\right]=2 \pi \sigma_{1} \sigma_{2} V \sqrt{1-\rho^{2}} \\
\Rightarrow & c=\left[-2\left(1-\rho^{2}\right) \ln \left(2 \pi \sigma_{1} \sigma_{2} V \sqrt{1-\rho^{2}}\right)\right]^{1 / 2}
\end{aligned}
$$

To satisfy the equation above $\checkmark$ must satisfy

$$
\begin{aligned}
& 2 \pi \sigma_{1} \sigma_{2} v \sqrt{1-\rho^{2}}<1 \\
\Rightarrow \quad & v<\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}
\end{aligned}
$$

* Angle of Rotation

Compute the distance to the edge of the ellipse.
Let,

$$
\begin{aligned}
r^{2}= & \left(y_{1}-\mu_{1}\right)^{2}+\left(y_{2}-\mu_{2}\right)^{2} \\
= & \left\{c \sigma_{1}\left[\sin \theta+\frac{\rho}{1-\rho^{2}} \cos \theta\right]\right\}^{2} \\
& +\left\{\frac{\sigma_{2}}{\sqrt{1-\rho^{2}}} \cos \theta\right\}^{2} \\
= & c^{2} \sigma_{1}^{2}\left(\sin \theta+\frac{\rho}{\sqrt{1-\rho^{2}}} \cos \theta\right)^{2} \\
& \quad c^{2} \sigma_{l_{2}}^{2} \cos ^{2} \theta \\
= & c^{2}\left[\sigma_{1}^{2} \sin ^{2} \theta+2 \sigma_{1}^{2} \frac{\rho}{1-\rho^{2}} \sin \theta \cos \theta\right. \\
& \quad+\frac{\sigma_{1}^{2} \rho^{2}}{\left(1-\rho^{2}\right)} \cos ^{2} \theta+\left(\frac{\sigma_{2}^{2}}{1-\rho^{2}} \cos ^{2} \theta\right]
\end{aligned}
$$

$$
\begin{aligned}
=c^{2} & \left\{\sigma_{1}^{2} \sin ^{2} \theta+2 \frac{\sigma_{1}^{2} \rho}{\sqrt{1-\rho^{2}}} \sin \theta \cos \theta\right. \\
& \left.+\frac{\cos ^{2} \theta}{\left(1-\rho^{2}\right)}\left[\sigma_{1}^{2} \rho^{2}+\sigma_{2}^{2}\right]\right\} \\
=\sigma_{1}^{2} c^{2} & \left\{\sin ^{2} \theta+\frac{\partial \rho}{\sqrt{1-\rho^{2}}} \sin \theta \cos \theta\right. \\
& \left.+\frac{\cos ^{2} \theta}{\left(1-\rho^{2}\right)}\left[\rho^{2}+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\right]\right\}
\end{aligned}
$$

To find extrema consider

$$
\begin{aligned}
r(\theta)= & \sigma_{1} c\left\{\sin ^{2} \theta+\frac{\partial \rho}{\sqrt{1-\rho^{2}}} \sin \theta \cos \theta\right. \\
& \left.+\frac{\cos ^{2} \theta}{\left(1-\rho^{2}\right)}\left[\rho^{2}+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\right]\right\}^{1 / 2} \\
\frac{d r(\theta)}{d \theta}= & \frac{\sigma_{1} c}{21 r(\theta)}\left\{2 \sin \theta \cos \theta+\frac{2 \rho}{\sqrt{1-\rho^{2}}}\left(\cos ^{2} \theta\right.\right. \\
& \left.\left.-\sin ^{2} \theta\right)-2 \frac{\sin \theta \cos \theta}{1-e^{2}}\left[e^{2}+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\right]\right\}
\end{aligned}
$$

recall the identities

$$
\sin (2 \theta)=2 \sin \theta \cos \theta
$$

$$
\cos (2 \theta)=\cos ^{2} \theta-\sin ^{2} \theta
$$

So

$$
\begin{aligned}
\frac{d r(\theta)}{d \theta}= & \frac{\sigma_{1} c}{\partial r(\theta)}\left\{\sin (2 \theta)+\frac{2 \rho}{\sqrt{1-\rho^{2}}} \cos (2 \theta)\right. \\
& \left.-\frac{\sin (2 \theta)}{1-\rho^{2}}\left[\rho^{2}+\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right]\right\} \\
= & \frac{\sigma_{1} c}{2 r(\theta)}\left\{\sin (2 \theta)\left[1-\frac{1}{1-\rho^{2}}\left(\rho^{2}+\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right)\right]\right. \\
& \left.+\frac{2 \rho}{\sqrt{1-\rho^{2}}} \cos (2 \theta)\right\} \\
= & \frac{\sigma_{1} c}{2 \sqrt{r(\theta)}}\left\{\frac{\sin (2 \theta)}{1-\rho^{2}}\left(1-\rho^{2}-\rho^{2}-\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right)\right. \\
& \left.+\frac{\partial \rho}{\sqrt{1-\rho^{2}}} \cos (2 \theta)\right\} \\
= & \frac{\sigma_{1} c}{2 \operatorname{lr}(\theta)}\left\{\frac{\sin (2 \theta)}{1-\rho^{2}}\left(1-2 \rho^{2}-\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right)\right. \\
& \left.+\frac{2 \rho}{1-\rho^{2}} \cos (2 \theta)\right\}
\end{aligned}
$$

Now to find extrema for $\rho \neq 0$

$$
\begin{aligned}
& \frac{d r(\theta)}{d \theta}=0 \\
\Rightarrow & \left\{\frac{\sin (2 \theta)}{\left(1-e^{2}\right)}\left(1-2 e^{2}-\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right)\right. \\
& \left.+\frac{\partial \rho}{1-\rho^{2}} \cos (2 \theta)\right\}=0 \\
\Rightarrow & \frac{\partial \rho}{1-\rho^{2}} \cos (2 \theta)=\frac{\sin (2 \theta)}{\left(1-\rho^{2}\right)}\left[\frac{\theta_{1}^{2}}{\sigma_{2}^{2}}+2 \rho^{2}-1\right] \\
\Rightarrow & \frac{\cos \left(2 \theta^{\prime}\right)}{\sin \left(2 \theta^{\prime}\right)}=\frac{1}{2 \rho^{1-\rho^{2}}}\left[\frac{\theta_{1}^{2}}{\sigma_{2}^{2}}+2 \rho^{2}-1\right]
\end{aligned}
$$

for $\rho=0$ and $\sigma_{1} \neq \sigma_{2}$
$\frac{d r(\theta)}{d \theta}=0$
$\Rightarrow \sin \left(2 \theta^{\prime}\right)\left(1-\frac{\sigma_{1}^{2}}{\sigma_{2}^{2}}\right)=0$
Since it is assumed that
$0 \leqslant \theta<2 \pi$
Solutions are

$$
\theta^{\prime}=0, \pi / 2, \pi, 3 / 2 \pi
$$

if further $\sigma_{1}=\sigma_{2}$ then there are no extrema intrating that the contour is a circle.

Finally consider the case
$\rho \neq 0 \quad \sigma_{1}=\sigma_{2}$

$$
\begin{aligned}
\cot \left(2 \theta^{\prime}\right) & =\frac{1}{2 \rho \sqrt{1-\rho^{2}}}\left(1-2 \rho^{2}-1\right) \\
& =\frac{\rho}{\sqrt{1-\rho^{2}}}
\end{aligned}
$$

To compule the rotation angle compute its cosine using

$$
\begin{aligned}
& \cos \varphi=\frac{u\left(\theta^{\prime}\right)}{r\left(\theta^{\prime}\right)} \\
& \begin{aligned}
r(\theta)=\sigma_{1} c\left\{\sin ^{2} \theta^{\prime}+\frac{\partial \rho}{\sqrt{1-\rho^{2}}} \sin \theta^{\prime} \cos \theta^{\prime}\right. \\
\left.+\frac{\cos ^{2 \theta^{\prime}}}{\left(1-\rho^{2}\right)}\left[\rho^{2}+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\right]\right\}^{1 / 2}
\end{aligned} \\
& u\left(\theta^{\prime}\right)=\operatorname{co} \sigma_{1}\left[\sin \theta+\frac{\rho}{\sqrt{1-\rho^{2}}} \cos \theta\right]
\end{aligned}
$$

Now for the first case, for $\rho=0$ and $\sigma_{1} \neq \sigma_{2}$

$$
\begin{aligned}
\theta^{\prime} & =0, \pi / 2, \pi, 3 / 2 \pi \\
r(\theta) & =\sigma_{1} c\left[\sin ^{2} \theta+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}} \cos ^{2} \theta\right]^{1 / 2} \\
u(\theta) & =c \sigma_{1} \sin \theta \\
r(0) & =\sigma_{1} c\left(\frac{\sigma_{2}}{\sigma_{1}}\right)=\sigma_{2} c
\end{aligned}
$$

$$
\begin{array}{ll}
v(\pi / 2)=\sigma_{1} c & \\
v(\pi)=\sigma_{2} c & r(3 / 2 \pi)=\sigma_{1} c \\
v(0)=0 & v(\pi / 2)=c \sigma_{1} \\
v(\pi)=0 & v(3 / 2 \pi)=0
\end{array}
$$

50

$$
\cos \varphi=1 \Rightarrow \varphi=0
$$

Consider the case $\rho \neq 0, \sigma_{1}=\sigma_{2}$

$$
\cot \left(2 \theta^{\prime}\right)=\frac{\rho}{\sqrt{1-\rho^{2}}}=\frac{\cos \left(2 \theta^{\prime}\right)}{\sin (2 \theta)}
$$

for this case

$$
\begin{aligned}
r(\theta)= & \sigma_{1} c\left\{\sin ^{2} \theta+\frac{\partial \rho}{\sqrt{1-\rho^{2}}} \sin \theta \cos \theta+\right. \\
& \left.\frac{\cos ^{2} \theta}{\left(1-\rho^{2}\right)}\left(\rho^{2}+1\right)\right\}^{1 / 2} \\
u(\theta)=\sigma_{1} c & {\left[\sin \theta+\frac{\rho}{\sqrt{1-\rho^{2}}} \cos \theta\right] }
\end{aligned}
$$

using

$$
\sin 2 \theta^{\prime}=2 \cos \theta^{\prime} \sin \theta^{\prime}
$$

$$
\begin{aligned}
& \frac{\rho}{1-\rho^{2}}=\frac{\cos \left(2 \theta^{\prime}\right)}{\sin (2 \theta)}=\frac{\cos \left(2 \theta^{\prime}\right)}{2 \cos \theta^{\prime} \sin \theta^{\prime}} \\
\Rightarrow \quad & \cos \left(2 \theta^{\prime}\right)=2 \cos \theta^{\prime} \sin \theta^{\prime} \frac{\rho}{\sqrt{1-\rho^{2}}}
\end{aligned}
$$

## * Equations for contours of constant $I_{1}$ and $I_{2}$

The transformation from the indendent and identically variables
discribuded vormal random Uariables ${ }_{X_{1}}$ and ${I_{2}}$ Normal to random the Jointly $X_{1}$ and $\bar{X}_{2}$ to the Jointly
oormal random variables $\bar{Y}_{1}$ and $I_{2}$ is defined by

$$
\binom{I_{1}-\mu_{1}}{I_{2}-\mu_{2}}=\left(\begin{array}{cc}
\sigma_{1} & 0 \\
\sigma_{2} \rho & \sigma_{2} \sqrt{1-\rho^{2}}
\end{array}\right)\binom{\bar{x}_{1}}{\bar{x}_{2}}
$$

Now

$$
\begin{aligned}
& \left(\bar{Y}_{1}-\mu_{1}\right)=\sigma_{1} \bar{X}_{1} \\
& \Rightarrow \quad \bar{X}_{1}=\frac{1}{\sigma_{1}}\left(\bar{I}_{1}-\mu_{1}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
\left(\bar{I}_{2}-\mu_{2}\right)= & \sigma_{2} \rho \bar{x}_{1}+\sigma_{2} \sqrt{1-\rho_{2}} \bar{x}_{2} \\
= & \sigma_{2} \rho\left[\frac{1}{\sigma_{1}}\left(\bar{I}_{1}-\mu_{1}\right)\right] \\
& +\sigma_{2} \sqrt{1-\rho^{2}} \underline{x}_{2}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow \bar{X}_{2} & =\frac{1}{\sqrt{1-\rho^{2}}}\left\{{\frac{\rho}{\delta_{1}}}\left(\bar{I}_{1}-\mu_{1}\right)\right. \\
& \left.-\frac{1}{\sigma_{2}}\left(\bar{Y}_{2}-\mu_{2}\right)\right\}
\end{aligned}
$$

In summary

$$
\begin{aligned}
\bar{X}_{1}= & \frac{1}{\sigma_{1}}\left(I_{1}-\mu_{1}\right) \\
\bar{X}_{2}= & \frac{1}{\sqrt{1-e^{2}}}\left\{\frac{f_{1}}{\sigma_{1}}\left(I_{1}-\mu_{1}\right)\right. \\
& \left.-\frac{1}{\sigma_{2}}\left(\bar{Y}_{2}-\mu_{2}\right)\right\}
\end{aligned}
$$

In the $\left(\bar{x}_{1}, \bar{x}_{2}\right)$ space contours of constant

$$
\bar{I}_{1}=C_{1}
$$

are defined by

$$
\bar{X}_{1}=\frac{1}{\sigma_{1}}\left(c_{1}-\mu_{1}\right)
$$

$$
\bar{X}_{2}=\frac{1}{\sqrt{1-e^{2}}}\left\{\frac{f}{\delta_{1}}\left(C_{1}-\mu_{1}\right)-\frac{1}{\delta_{2}}\left(\bar{Y}_{2}-\mu_{2}\right)\right\}
$$

and contours of constant $I_{2}=C_{2}$

$$
\begin{gathered}
\bar{X}_{1}=\frac{1}{\sigma_{1}}\left(I_{1}-\mu_{1}\right) \\
\bar{X}_{2}=\frac{1}{\sqrt{1-\rho^{2}}}\left\{\frac{\rho}{\sigma_{1}}\left(I_{1}-\mu_{1}\right)-\frac{1}{\sigma_{2}}\left(c_{2}-\mu_{2}\right)\right\}
\end{gathered}
$$

substituting the expression for
$\bar{X}_{1}$ into $\bar{X}_{2}$

$$
\begin{aligned}
\bar{X}_{2} & =\frac{1}{\sigma_{2} \sqrt{1-\rho^{2}}}\left[\sigma_{2} \rho \bar{X}_{1}-\left(c_{2}-\mu_{2}\right)\right] \\
& =r_{1-\rho^{2}} \bar{X}_{1}-\frac{1}{\sigma_{2} \sqrt{1-\rho^{2}}}\left(c_{2}-\mu_{2}\right)
\end{aligned}
$$

* Test calculations


## Recall that

$g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi \sigma_{1} \sigma_{2} d 1-\rho^{2}} \exp \left\{\frac{-1}{\partial\left(1-\rho^{2}\right)}[\right.$
$\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}$
$\left.\left.-2 \rho\left(\frac{y_{1}-\mu_{1}}{\sigma_{1}}\right) \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right]\right\}$
and the parametric equations for cotours of constant density are given by

$$
\begin{aligned}
& y_{1}=c \sigma_{1}\left[\sin \theta+\frac{\rho}{1-\rho^{2}} \cos \theta\right]+\mu_{1} \\
& y_{2}=\frac{c \sigma_{2}}{\sqrt{1-\rho^{2}}} \cos \theta+\mu_{2}
\end{aligned}
$$

where the constant $C$ is related
to the contour value $v$ by
$c=\left[-2\left(1-\rho^{2}\right) \ln \left(2 \pi \sigma_{1} \sigma_{2} v \sqrt{1-\rho^{2}}\right)\right]^{1 / 2}$
To satisfy the equation above $\checkmark$ must satisfy

$$
\begin{aligned}
& 2 \pi \sigma_{1} \sigma_{2} v \sqrt{1-\rho^{2}}<1 \\
\Rightarrow \quad & v<\frac{1}{2 \pi \sigma_{1} \sigma_{2} \sqrt{1-\rho^{2}}}
\end{aligned}
$$

* Assume the following values for the parameters.

$$
\begin{aligned}
& \mu_{1}=\mu_{2}=0 \\
& \sigma_{1}=\sigma_{2}=1 \\
& \rho=0
\end{aligned}
$$

then

$$
g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi} \exp \left[-\frac{1}{2}\left(y_{1}^{2}+y_{2}^{2}\right)\right]
$$

and
and for the density contours

$$
\begin{aligned}
y_{1} & =c \sin \theta \\
y_{2} & =c \cos \theta \\
c & =[-2 \ln (2 \pi v)]^{1 / 2} \\
v & <\frac{1}{2 \pi}
\end{aligned}
$$

let $v=0,10$ so that

$$
\begin{aligned}
c^{2} & =\{-2 \ln [2 \pi(0.10)]\} \\
& =0.93
\end{aligned}
$$

and for the density with

$$
y_{1}^{2}+y_{2}^{2}=c^{2}
$$

and

$$
\begin{aligned}
g\left(y_{1}, y_{2}\right) & =\frac{1}{2 \pi} \exp \left(-\frac{c^{2}}{2}\right) \\
& =0.1
\end{aligned}
$$

* Now Consider the case with Correlation

$$
\begin{gathered}
\mu_{1}=\mu_{2}=0 \\
\sigma_{1}=\sigma_{2}=1 \\
\rho=0,5
\end{gathered}
$$

then

$$
g\left(y_{1}, y_{2}\right)=\frac{1}{2 \pi} \exp \left[-\frac{1}{2}\left(y_{1}^{2}+y_{2}^{2}-y_{1} y_{2}\right)\right]
$$

and for the density contours

$$
\begin{aligned}
& y_{1}=c(\sin \theta+2 / 3 \cos \theta) \\
& y_{2}=c \sqrt{\frac{4}{3}} \cos \theta=\frac{2 c}{\sqrt{3}} \cos \theta \\
c= & {[-2(1-1 / 4) \ln (2 \pi v \sqrt{1-1 / 4})]^{1 / 2} } \\
= & {[-2(3 / 4) \ln (2 \pi v \sqrt{3 / 4})]^{1 / 2} } \\
= & {[-3 / 2 \ln (2 \pi \sqrt{3 / 4} v)]^{1 / 2} } \\
v & \frac{1}{2 \pi \sqrt{3 / 4}}=0.18
\end{aligned}
$$

let $v=0,10$ so that

$$
\begin{aligned}
c & =[-3 / 2 \ln (2 \pi \sqrt{3 / 4}(0.1))]^{1 / 2} \\
& =0.91
\end{aligned}
$$

$$
\begin{aligned}
& y_{1}=0,9(\sin \theta+2 / 3 \cos \theta) \\
& y_{2}=\frac{1,8}{\sqrt{3}} \cos \theta
\end{aligned}
$$

$$
\begin{aligned}
\left.g\left(y_{1}\right) y_{2}\right) & =\frac{1}{2 \pi} \exp \left(-\frac{c^{2}}{2}\right) \\
& =0.1
\end{aligned}
$$

$g(1,1)=\frac{1}{2 \pi} \exp (-1 / 2)=0.096$

* Bivariate Trasformation Excmple

Contours of constant $\bar{I}_{1}=c_{1}$ are defined by

$$
\bar{X}_{1}=\frac{1}{\sigma_{1}}\left(c_{1}-\mu_{1}\right)
$$

$$
\begin{aligned}
\bar{X}_{2}= & \frac{1}{\sigma_{2} \sqrt{1-\rho^{2}}}\left\{\sigma_{2} \rho\left[\frac{1}{\sigma_{1}}\left(c_{1}-\mu_{1}\right)\right]\right. \\
& \left.-\left(\bar{y}_{2}-\mu_{2}\right)\right\}
\end{aligned}
$$

and contours of constant $I_{2}=C_{2}$

$$
\begin{aligned}
\bar{X}_{1} & =\frac{1}{\sigma_{1}}\left(I_{1}-\mu_{1}\right) \\
\bar{X}_{2}= & \frac{1}{\sigma_{2} \sqrt{1-\rho^{2}}}\left\{\sigma_{2} \rho\left[\frac{1}{\sigma_{1}}\left(I_{1}-\mu_{1}\right)\right]\right. \\
& \left.-\left(C_{2}-\mu_{2}\right)\right\}
\end{aligned}
$$

Consider the case

$$
\begin{aligned}
& \mu_{1}=\mu_{2}=0 \\
& \sigma_{1}=\sigma_{2}=1 \\
& \rho=0,5 \\
& c_{1}=c_{2}=1
\end{aligned}
$$

It follows that for $\bar{y}_{1}=c_{1}=1$

$$
\begin{aligned}
\frac{\bar{x}_{1}}{\bar{x}_{2}} & =\frac{1}{1 \sqrt{1-0,25}}\left[0,5(1)-\bar{y}_{2}\right] \\
& =\frac{1}{\sqrt{0,75}}\left(0,5-\bar{y}_{2}\right) \\
& =1.15\left(0.5-\bar{y}_{2}\right)
\end{aligned}
$$

and for $I_{2}=C_{2}=1$

$$
\begin{aligned}
& Z_{1}=I_{1} \\
& I_{2}=1.15\left(0.5 I_{1}-1\right)
\end{aligned}
$$

* Test Calculations

Recall that
$r(\theta)=\sigma, c\left\{\sin ^{2} \theta+\frac{\partial \rho}{1-e^{2}} \sin \theta \cos \theta\right.$

$$
\left.+\frac{\cos ^{2} \theta}{\left(1-e^{2}\right)^{2}}\left[e^{2}+\frac{\sigma_{2}^{2}}{\sigma_{1}^{2}}\left(1-e^{2}\right)\right]\right\}^{1 / 2}
$$

to the contour value $v$ by
$c=\left[-2\left(1-\rho^{2}\right) \ln \left(2 \pi \sigma_{1} \sigma_{2} v \sqrt{1-\rho^{2}}\right)\right]^{1 / 2}$
assume that $\rho=0, \sigma_{1}=\sigma_{2}=1$ and $v=0.1$

$$
r(\theta)=c\left(\sin ^{2} \theta+\cos ^{2} \theta\right)^{1 / 2}=c
$$

## $C=-\sqrt{-2 \ln (2 \pi v)}=0.96^{\circ}$

Next assume $\rho=0, \sigma_{1}=1, \sigma_{2}=2 v=0.02$

$$
\begin{aligned}
& r(\theta)=c\left(\sin ^{2} \theta+4 \cos ^{2} \theta\right)^{1 / 2} \\
& c=\sqrt{-2 \ln (4 \pi v)}=1.66
\end{aligned}
$$

Next assume $\rho=0, \sigma_{1}=2, \sigma_{2}=1$

$$
\begin{aligned}
& v=0.02 \\
& r=2 c\left(\sin ^{2} \theta+4 \cos ^{2} \theta\right)^{1 / 2} \\
& c=\sqrt{-2 \ln (4 \pi v)}=1.66
\end{aligned}
$$

Next asseme $\rho=0.5, \sigma_{1}=1, \sigma_{2}=1$

$$
\begin{aligned}
v= & 0.1 \\
C= & \sqrt{-2(1-1 / 4) \ln [2(0.1) \pi \sqrt{1-1 / 4}]} \\
= & \sqrt{-3 / 2 \ln (0.2 \pi \sqrt{3} / 2)}=0.955 \\
r=C & {\left[\sin ^{2} \theta+\frac{2(1 / 2)}{1-1 / 4} \sin \theta \cos \theta\right.} \\
& \left.+\frac{\cos ^{2} \theta}{(1-1 / 4)^{2}}(1 / 4+3 / 4)\right]^{1 / 2} \\
=C & {\left[\sin ^{2} \theta+\frac{1}{3 / 4} \sin \theta \cos \theta+\frac{\cos ^{2} \theta}{(3 / 4)^{2}}\right]^{1 / 2} } \\
=C & \left(\sin ^{2} \theta+4 / 3 \sin \theta \cos \theta+16 / 9 \cos ^{2} \theta\right)^{1 / 2}
\end{aligned}
$$

$y_{1}=c\left[\sin \theta+\frac{1 / 2}{1-1 / 4} \cos \theta\right]$

$$
\begin{aligned}
& =c(\sin \theta+2 / 3 \cos \theta) \\
& y_{2}=\frac{c}{\sqrt{1-k 1}} \cos \theta \\
& =\frac{c}{\sqrt{3 / 4}} \cos \theta=\frac{2 c}{\sqrt{3}} \cos \theta
\end{aligned}
$$

Next assume $\rho=0.9, \sigma_{1}=1, \sigma_{2}=1 v=0.1$

$$
\begin{aligned}
c & =\left\{-2\left(1-0.9^{2}\right) \ln \left[2 \pi(0.1) \sqrt{1-0.9^{2}}\right]\right\}^{1 / 2} \\
& =\{(-2)(0.19) \ln [0.2 \pi \sqrt{0.19}]\}^{1 / 2} \\
& =0.7015
\end{aligned}
$$

