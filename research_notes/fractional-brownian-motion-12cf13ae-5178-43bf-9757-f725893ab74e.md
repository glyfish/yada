## Fractional Brownian Motion

![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-001.jpg?height=339&width=466&top_left_y=1472&top_left_x=993)

## Gaussian Random Walks

## Brownian Motion

Consider a stochasic process B(tn) where

$$
t_{n}=(\Delta t) n
$$

The increments of the process are defined by

$$
\Delta B_{n}=B\left(t_{n}\right)-B\left(t_{n-1}\right)
$$

Brownian motion is defined by

1. $\quad B\left(t_{0}\right)=0$
2. The $\Delta B_{n}$ are independently distributed Gaussian random variables with zero mean and variance $\Delta t$.

If $z_{n}$ is a unit normal random variable

$$
\Delta B_{n}=\sqrt{\Delta t} Z_{n}
$$

It follows that

$$
\begin{aligned}
B\left(t_{n}\right) & =\sum_{i=1}^{n} \sqrt{\Delta t} Z_{n} \\
& =\sqrt{\Delta t} \sum_{i=1}^{n} Z_{n}
\end{aligned}
$$

Now

$$
\begin{aligned}
\left\langle B\left(t_{n}\right)\right\rangle & =\sqrt{\Delta t}\left|\sum_{i=1}^{n} z_{i}\right\rangle \\
& =\sqrt{\Delta t} \sum_{i=1}^{n}\left\langle z_{i}\right\rangle \\
& =0
\end{aligned}
$$

and

$$
\begin{aligned}
\left\langle B^{2}\left(t_{n}\right)\right\rangle & =\left\langle\left[\sqrt{\Delta t} \sum_{i=1}^{n} z_{i}\right]^{2}\right\rangle \\
& =\Delta t\left\langle\sum_{i=1}^{n} \sum_{j=1}^{n} z_{i} z_{j}\right\rangle \\
& =\Delta t \sum_{i=1}^{n} \sum_{j=1}^{n}\left\langle z_{i} z_{j}\right\rangle
\end{aligned}
$$

Now from the definition of Brownian motion the $z_{i}$ are
independent

$$
\left\langle z_{i} z_{j}\right\rangle=\delta_{i j}
$$

thus

$$
\begin{aligned}
\left\langle B^{2}\left(t_{n}\right)\right\rangle & =\Delta t \sum_{i=1}^{n} \sum_{j=1}^{n} \delta_{i j} \\
& =\Delta t \sum_{i=1}^{n} 1 \\
& =\Delta t n
\end{aligned}
$$

The covariance is defind by

$$
\left\langle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle
$$

Now for $t_{n}>t_{m}$

$$
\begin{aligned}
\left\langle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle= & \\
& \left\langle\left[B\left(t_{n}\right)-B\left(t_{m}\right)+B\left(t_{m}\right)\right] B\left(t_{m}\right)\right\rangle \\
= & \left\langle\left[B\left(t_{n}\right)-B\left(t_{m}\right)\right] B\left(t_{m}\right)\right\rangle+\left\langle B\left(t_{m}\right) B\left(t_{m}\right)\right\rangle
\end{aligned}
$$

For the second term
$\left\langle B\left(t_{m}\right) B\left(t_{m}\right)\right\rangle=t_{m}$
and for the first term

$$
\begin{aligned}
& B\left(t_{n}\right)-B\left(t_{m}\right)=\sqrt{\Delta t} \sum_{i=m+1}^{n} z_{i} \\
& B\left(t_{m}\right)=\sqrt{\Delta t} \sum_{j=0}^{m} z_{j}
\end{aligned}
$$

So

$$
\begin{aligned}
& \left\langle\left[B\left(t_{n}\right)-B\left(t_{m}\right)\right] B\left(t_{m}\right)\right\rangle \\
& =\Delta t \sum_{j=0}^{m} \sum_{i=m+1}^{n}\left\langle Z_{i} Z_{j}\right\rangle
\end{aligned}
$$

By definition

$$
\left\langle Z_{i} Z_{j}\right\rangle=\delta_{i j}
$$

But $i \neq j$ for any terms in the sum so

$$
\left\langle\left[B\left(t_{n}\right)-B\left(t_{m}\right)\right] B\left(t_{m}\right)\right\rangle=0
$$

It follows that

$$
\begin{aligned}
& \left.\angle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle=t_{m} \\
& \text { Similarly if } t_{m}>t_{n} \\
& \left.\angle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle=t_{n} \\
& \text { Thus } \\
& \left.\angle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle=\min \left(t_{n}, t_{m}\right)
\end{aligned}
$$

Thus for Brownian motion

$$
\begin{gathered}
\left\langle B\left(t_{n}\right)\right\rangle=0 \\
\left\langle B^{2}\left(t_{n}\right)\right\rangle=n \Delta t \\
\left\langle B\left(t_{n}\right) B\left(t_{m}\right)\right\rangle=\min \left(t_{n}, t_{m}\right)
\end{gathered}
$$

The following plot shows 8 simulations of Brownian motion. The mean and standard deviation computed from the simulations is shown in the upper left corner. For all the simulations 10,000 steps
where performed with a timstep of $\Delta t=0.01$. By defunition Brownian motion has a mean of

$$
\mu=0
$$

and for the given $\Delta t$ and number of steps

$$
\theta=10
$$

The first plot shows 8 simulations to get a sense of the form of the simulated curves. The number of simulations is too small to compare with the conalytic mean and standard deviation.

Brownian Motion; $\Delta \mathrm{t}=0.01$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-007.jpg?height=718&width=1087&top_left_y=1215&top_left_x=242)

The next plot shows 1000 simulations. The computed mean and standard deviation agree well withe the analytic results.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-008.jpg?height=912&width=1327&top_left_y=501&top_left_x=120)

## Brownian Motion with Drift

Brownian Motion with Drift is defined by

$$
x\left(t_{n}\right)=\sigma B\left(t_{n}\right)+\mu t_{n}
$$

where $B\left(t_{n}\right)$ is Brownian Motion. since by definition $B(0)=0$ it follows that

$$
x(0)=0 .
$$

The increment is defined by

$$
\begin{aligned}
\Delta x_{n} & =x\left(t_{n}\right)-x\left(t_{n-1}\right) \\
& =6 \Delta B_{n}+\mu \Delta t
\end{aligned}
$$

Now

$$
\Delta B_{n}=\sqrt{\Delta t} Z_{n}
$$

where $Z_{n}$ is a whit normal random variable. Thus

$$
\Delta x_{n}=\sigma \sqrt{\Delta t} Z_{n}+\mu \Delta t
$$

Since

$$
\begin{aligned}
& \left\langle z_{n}\right\rangle=0 \\
& \left\langle z_{n}^{2}\right\rangle=1
\end{aligned}
$$

Thus

$$
\left\langle\Delta x_{n}\right\rangle=\Delta t_{\mu}
$$

$$
\begin{aligned}
& \left\langle\Delta x_{n}^{2}\right\rangle=\left\langle\left[\left(\sigma \sqrt{\Delta t} z_{n}+\mu \Delta t\right)\right]^{2}\right\rangle \\
& =\left\langle\sigma^{2} \Delta t z_{n}^{2}+2 \mu(\Delta t)^{3 / 2} z_{n}+\mu^{2} \Delta t^{2}\right\rangle \\
& =\sigma^{2} \Delta t+\mu^{2} \Delta t^{2}=\Delta t\left(\sigma^{2}+\mu^{2} \Delta t\right)
\end{aligned}
$$

it follows that the standard deviation of $\Delta x_{n}$ is given by

$$
\begin{aligned}
\sigma_{\Delta x}^{2} & =\left\langle\Delta x_{n}^{2}\right\rangle-\left\langle\Delta x_{n}\right\rangle^{2} \\
& =\Delta t \sigma^{2}+\mu^{2} \Delta t^{2}-\mu^{2} \Delta t^{2} \\
& =\Delta t \sigma^{2}
\end{aligned}
$$

Thus $\Delta X_{n}$ are identically distributed normal random variables with
mean and variance

$$
\begin{aligned}
& \mu_{\Delta x}=\left\langle\Delta x_{n}\right\rangle=\Delta t \mu \\
& \sigma_{\Delta x}^{2}=\Delta t \sigma^{2}
\end{aligned}
$$

Now

$$
x\left(t_{n}\right)=\sum_{i=1}^{n} \Delta x_{i}
$$

so

$$
\begin{aligned}
\left\langle x\left(t_{n}\right)\right\rangle & =\sum_{i=1}^{n}\left\langle\Delta x_{i}\right\rangle \\
& =\sum_{i=1}^{n} \Delta t \mu \\
& =(n \Delta t) \mu
\end{aligned}
$$

and

$$
\begin{aligned}
& \left\langle x^{2}(\ln )\right\rangle=\left\langle\left[\sum_{i=1}^{n} \Delta x_{i}\right]^{2}\right\rangle \\
& =\left\langle\sum_{i=1}^{n} \sum_{j=1}^{n} \Delta x_{i} \Delta x_{j}\right\rangle
\end{aligned}
$$

$$
=\sum_{i=1}^{n} \sum_{j=1}^{n}\left\langle\Delta x_{i} \Delta x_{j}\right\rangle
$$

## using

$$
\Delta x_{i}=\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t
$$

and that the $z_{i}$ are indeperdent so

$$
\left\langle z_{i} z_{j}\right\rangle=\delta_{i j}
$$

it follows that

$$
\begin{aligned}
& \left\langle\Delta x_{i} \Delta x_{j}\right\rangle=\left\langle\left(\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t\right)\right. \\
& \left.\left(\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t\right)\right\rangle \\
= & \left\langle\sigma^{2} \Delta t z_{i} z_{j}+\sigma \sqrt{\Delta t} \mu(\Delta t) z_{i}\right. \\
& \left.+\sigma \sqrt{\Delta t} \mu(\Delta t) z_{j}+\mu^{2} \Delta t^{2}\right\rangle \\
= & \sigma^{2} \Delta t\left\langle z_{i} z_{j}\right\rangle+\mu^{2} \Delta t^{2} \\
= & \sigma^{2} \Delta t \delta_{i j}+\mu^{2} \Delta t^{2}
\end{aligned}
$$

$$
\begin{aligned}
\sum_{i=1}^{n} \sum_{j=1}^{n}\left\langle\Delta x_{i} \Delta x_{j}\right\rangle & =\sum_{i=1}^{n} \sum_{j=1}^{n}\left(\sigma^{2} \Delta t \delta_{i j}+\mu^{2} \Delta t^{2}\right) \\
= & (n \Delta t) \sigma^{2}+(n \Delta t)^{2} \mu^{2}
\end{aligned}
$$

Thus

$$
\begin{aligned}
\left\langle x^{2}\left(t_{n}\right)\right\rangle & =\sum_{i=1}^{n} \sum_{j=1}^{n}\left\langle\Delta x_{i} \Delta x_{j}\right\rangle \\
& =(n \Delta t) \sigma^{2}+(n \Delta t)^{2} \mu^{2}
\end{aligned}
$$

In summary

$$
\begin{aligned}
\left\langle x\left(t_{n}\right)\right\rangle & =(n \Delta t) \mu \\
\left\langle x^{2}\left(t_{n}\right)\right\rangle & =(n \Delta t) \theta^{2}+(n \Delta t)^{2} \mu^{2}
\end{aligned}
$$

Finally it follows that

$$
\mu_{x}=(n \Delta t) \mu
$$

and

$$
\sigma_{x}^{2}=\left\langle x^{2}\left(t_{n}\right)\right\rangle-\left\langle x\left(t_{n}\right)\right\rangle^{2}
$$

$$
\begin{aligned}
& =(n \Delta t) \sigma^{2}+(n \Delta t)^{2} \mu^{2}-(n \Delta t)^{2} \mu^{2} \\
& =(n \Delta t) \sigma^{2}
\end{aligned}
$$

Thus Brownian Motion with drift has mean and variance

$$
\begin{aligned}
& \mu_{x}=(n \Delta t) \mu \\
& \sigma_{x}=(n \Delta t) \sigma^{2}
\end{aligned}
$$

The following plots show the results of 8 simulations of Brownian motion with drift where the following parameterization was assumed

$$
\begin{array}{cc}
\Delta t=0.01 & \text { nsteps }=10,000 \\
\mu=0.1 & \sigma=0.1
\end{array}
$$

for these parameters the mean and standard deviation are given by

$$
u_{x}=10 \quad \sigma_{x}=1
$$

The results obtained from 8 simulations are shown below to get a sense of the results. Even with a small number of simulations the mean and standard deviations computed from smulations are close to the analytic results

Brownian Motion with Drift; $\Delta \mathrm{t}=0.01, \mu=0.1, \sigma=0.1$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-015.jpg?height=737&width=1130&top_left_y=733&top_left_x=249)

The following plot shows the results of 1000 simulations. The computed mean and standard deviations agree will with the analyfic values.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-016.jpg?height=881&width=1266&top_left_y=147&top_left_x=153)

## Geometric Brownian Motion

Geometric Brownian Motion is defined by

$$
s\left(t_{n}\right)=s_{0} e^{x\left(t_{n}\right)}
$$

where $x\left(t_{n}\right)$ is Brownian Motion with Drift.

$$
x\left(t_{n}\right)=\sigma B\left(t_{n}\right)+\mu t_{n}
$$

and

$$
S_{0}=S(0)
$$

since

$$
x(0)=0
$$

The increments in Brownian motion with Drift are given by

$$
\Delta x_{i}=\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t
$$

and

$$
x\left(t_{n}\right)=\sum_{i=1}^{n} \Delta x_{i}
$$

50

$$
\begin{aligned}
& s\left(t_{n}\right)=s_{0} e^{\sum_{i=1}^{n} \Delta x_{i}}=s_{0} \prod_{i=1}^{n} e^{\Delta x_{i}} \\
& =s_{0} \prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t} \\
& =s_{0} \prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} z_{i}} e^{\mu \Delta t} \\
& =s_{0} e^{(n \Delta t) \mu \prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} z_{i}}}
\end{aligned}
$$

Now

$$
\begin{aligned}
& \left\langle S\left(t_{n}\right)\right\rangle=\left\langle S_{0} e^{(n \Delta t) \mu} \prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} Z_{i}}\right\rangle \\
& =S_{0} e^{(n \Delta t) \mu}\left\langle\prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} Z_{i}}\right\rangle
\end{aligned}
$$

Now the $z_{i}$ are independently unit normal random variables, so

$$
\left\langle\prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} z_{i}}\right\rangle=\prod_{i=1}^{n}\left\langle e^{\sigma \sqrt{\Delta t} z_{i}}\right\rangle
$$

Now

$$
\begin{aligned}
& \left\langle e^{\sigma \sqrt{\Delta t} z}\right\rangle=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{\sigma \sqrt{\Delta t} z} e^{-\frac{z^{2}}{2}} d z \\
= & \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2} z^{2}+\sigma \sqrt{\Delta t} z} d z
\end{aligned}
$$

Consider the expsnentral argument

$$
\begin{aligned}
& -\frac{1}{2} z^{2}+\sigma \sqrt{\Delta t} z=-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t} z\right) \\
& =-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t} z+\sigma^{2} \Delta t-\sigma^{2} \Delta t\right) \\
& =-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t} z+\sigma^{2} \Delta t\right)+\frac{1}{2} \sigma^{2} \Delta t \\
& =-\frac{1}{2}(z-\sigma \sqrt{\Delta t})^{2}+\frac{1}{2} \sigma^{2} \Delta t
\end{aligned}
$$

so

$$
\left\langle e^{6 \sqrt{\Delta t} z}\right\rangle=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(z-6 \sqrt{\Delta t})^{2}+\frac{1}{2} \gamma^{2} \Delta t} d z
$$

$$
\begin{aligned}
& =\frac{1}{\sqrt{2 \pi}} e^{\frac{1}{2} \sigma^{2} \Delta t} \int_{-\infty}^{\infty} e^{-\frac{1}{2}(z-\sigma \sqrt{\Delta t})^{2}} d z \\
& =e^{\frac{1}{2} \sigma^{2} \Delta t}
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
\left\langle S\left(t_{n}\right)\right\rangle & =S_{0} e^{(n \Delta t) \mu} \prod_{i=1}^{n}\left\langle e^{\sigma \sqrt{\Delta t} z_{i}}\right\rangle \\
& =S_{0} e^{(n \Delta t) \mu} \prod_{i=1}^{n} e^{\frac{1}{2} \sigma^{2} \Delta t} \\
& =S_{0} e^{(n \Delta t) \mu} e^{\frac{1}{2} \sigma^{2}(n \Delta t)} \\
& =S_{0} e^{(n \Delta t)\left(\mu+\frac{1}{2} \sigma^{2}\right)}
\end{aligned}
$$

Next consider

$$
\begin{aligned}
& \left\langle s^{2}\left(t_{n}\right)\right\rangle=\left\langle\left[s_{0} \prod_{i=1}^{n} e^{\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t}\right]^{2}\right\rangle \\
& =s_{0}^{2}\left\langle\left[e^{\sum_{i=1}^{n}\left(\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t\right)}\right]^{2}\right\rangle
\end{aligned}
$$

$$
\begin{aligned}
& =s_{0}^{2}\left\langle e^{\sum_{i=1}^{n}\left(\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t\right)}\right. \\
& \left.e^{\sum_{j=1}^{n}\left(\sigma \sqrt{\Delta t} z_{j}+\mu \Delta t\right)}\right\rangle \\
& =s_{0}^{2}\left\langle e^{2 \sum_{j=1}^{n}\left(\sigma \sqrt{\Delta t} z_{i}+\mu \Delta t\right)}\right\rangle \\
& =s_{0}^{2} e^{2 \mu(n \Delta t)}\left\langle e^{2 \sum_{j=1}^{n} \sigma \sqrt{\Delta t} z_{i}}\right\rangle \\
& =s_{0}^{2} e^{2 \mu(n \Delta t)}\left\langle\prod_{j=1}^{n} e^{2 \sigma \sqrt{\Delta t} z_{i}}\right\rangle \\
& =s_{0}^{2} e^{2 \mu(n \Delta t)} \prod_{j=1}^{n}\left\langle e^{2 \sigma \sqrt{\Delta t} z_{i}}\right\rangle
\end{aligned}
$$

Now

$$
\begin{aligned}
& \left\langle e^{2 \sigma \sqrt{\Delta t} z}\right\rangle=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{2 \sigma \sqrt{\Delta t} z} e^{-\frac{z^{2}}{2}} d z \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{2 \sigma \sqrt{\Delta t} z-z^{2} / 2} d z
\end{aligned}
$$

consider the argument of the exponentia 1

$$
\begin{aligned}
& 2 \sigma \sqrt{\Delta t} z-\frac{1}{2} z^{2}=-\frac{1}{2}\left(z^{2}-4 \sigma \sqrt{\Delta t} z\right) \\
& =-\frac{1}{2}\left(z^{2}-4 \sigma \sqrt{\Delta t} z+4 \sigma^{2} \Delta t-4 \sigma^{2} \Delta t\right)
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{2}\left(z^{2}-4 \sigma \sqrt{\Delta t} z+4 \sigma^{2} \Delta t\right)+2 \sigma^{2} \Delta t \\
& =-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t}\right)^{2}+2 \sigma^{2} \Delta t
\end{aligned}
$$

Continuing

$$
\begin{aligned}
& \left\langle e^{2 \sigma \sqrt{\Delta t} z}\right\rangle=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t}\right)^{2}} e^{2 \sigma^{2} z t} d z \\
& =\frac{1}{\sqrt{2 \pi}} e^{2 \sigma^{2} \Delta t} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left(z^{2}-2 \sigma \sqrt{\Delta t}\right)^{2}} d z \\
& =e^{2 \sigma^{2} \Delta t} \\
& \text { and } \\
& \begin{aligned}
\left\langle s^{2}\left(t_{n}\right)\right\rangle & =s_{0}^{2} e^{2 \mu(n \Delta t)} \prod_{j=1}^{n}\left\langle e^{2 \sigma \sqrt{\Delta t} z_{i}}\right\rangle \\
& =s_{0}^{2} e^{2 \mu(n \Delta t)} e^{2 \sigma^{2}(n \Delta t)} \\
& =s_{0}^{2} e^{2(n \Delta t)\left(\mu+\sigma^{2}\right)}
\end{aligned}
\end{aligned}
$$

It follows that the variance is given by

$$
\begin{aligned}
& \sigma_{s}^{2}=\left\langle s^{2}\left(t_{n}\right)\right\rangle-\left\langle s\left(t_{n}\right)\right\rangle^{2} \\
= & s_{0}^{2} e^{2(n \Delta t)}\left(\mu+\sigma^{2}\right)-s_{0}^{2} e^{2(n \Delta t)}\left(\mu+\frac{1}{2} \sigma^{2}\right) \\
= & s_{0}^{2} e^{(n \Delta t)\left(2 \mu+2 \sigma^{2}\right)}-s_{0}^{2} e^{(n \Delta t)} e^{\left(2 \mu+\sigma^{2}\right)} \\
= & s_{0}^{2} e^{(n \Delta t)(2 \mu)}\left[e^{(n \Delta t)\left(2 \sigma^{2}\right)}-e^{(n \Delta t) \sigma^{2}}\right] \\
= & s_{0}^{2} e^{(n \Delta t)(2 \mu)} e^{(n \Delta t) \sigma^{2}}\left[e^{(n \Delta t) \sigma^{2}}-1\right] \\
= & s_{0}^{2} e^{(n \Delta t)\left(2 \mu+\sigma^{2}\right)}\left[e^{(n \Delta t) \sigma^{2}}-1\right]
\end{aligned}
$$

Thus in summary the mean and variance of Deometric Brownian motion are given by

$$
\begin{gathered}
\mu_{s}=s_{0} e^{(n \Delta t)\left(\mu+\frac{1}{2} \sigma^{2}\right)} \\
\sigma_{s}^{2}=s_{\sigma^{2}}^{2} e^{(n \Delta t)\left(2 \mu+\sigma^{2}\right)}\left[e^{(n \Delta t) \sigma^{2}}-1\right]
\end{gathered}
$$

The following plot shows the results of 8 simulations of lean etric Brownian motion

$$
8,4878
$$

where the following parameters were assumed

$$
\begin{gathered}
\Delta t=0.01 \quad \text { nsteps }=10,000 \\
\mu=0.025 \quad \sigma=0.15 \\
s_{0}=1.0
\end{gathered}
$$

For this parameter cholce

$$
\mu_{s}=37.5 \quad \sigma_{s}=109
$$

The following plot shows the results obtained from simulations performed using the parameters
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-024.jpg?height=739&width=1067&top_left_y=1176&top_left_x=268)

The range of values is much greater than obtained for Brownian Motion and Brownian motion with drift. Geometric Brownian Motion can experience very rapid exponential growth. The descrepency between the analytic mean and standard deuration is large.
The following plot shows the results of 1000 smulations and the next 5000 simulations.

Geometric Brownian Motion; $\Delta \mathrm{t}=0.01, \mu=0.025, \sigma=0.15, S_{0}=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-025.jpg?height=717&width=1118&top_left_y=1182&top_left_x=217)

Geometric Brownian Motion; $\Delta \mathrm{t}=0.01, \mu=0.025, \sigma=0.15, S_{0}=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-026.jpg?height=732&width=1138&top_left_y=213&top_left_x=229)

The range of values obtained in an ensemble of simulations moreases greatly as the number of simulations increase
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-026.jpg?height=351&width=1434&top_left_y=1354&top_left_x=100)

Recall that analytically $\mu_{s}=37.5$ and $\sigma_{s}=109$. While the means obtained
are all close to the analytic value but the standard deviations increase significantly with the size of the ensemble with the largest ensemble haung both mean and standard deviation near the canalytic values for this choice of parameters the convergence of the ensemble moments is slow.
A better result is obtained with the parameters

$$
\begin{gathered}
\Delta t=0.01 \quad \text { nsteps }=100 \\
M=0.0 \quad \sigma=1.0 \\
s_{0}=1.0
\end{gathered}
$$

where

$$
\mu_{s}=1.649 \quad \sigma_{s}=2.161
$$

The results of an ensemble of simulations using the parameters is shown in the followin plot where it is seen that the
mean and stanard deviation computed from the ensemble are close to analytic values.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-028.jpg?height=891&width=1282&top_left_y=423&top_left_x=155)

## Fractional Calculus

Fractional Brownian motion is an extension of Brownian motion which prourdes a time series model that has been successfully applied to the aralysis of financial time series. To understand Fractional Brownian Motion an understanding of Fractional calculus is required. Here the basics of Fractional Calculus are described

## Cauchy Formula for Repeated Integration

Repeated integration is defined as follows. Consder a function $f(x)$ defined for $x>0$. The first integration of $f(x)$ is defined by

$$
(\text { If })(x)=\int_{0}^{x} f(t) d t
$$

The second integral is defined by

$$
\begin{aligned}
\left(I^{2} f\right)(x) & =\int_{0}^{x}(I f)(t) d t \\
& =\int_{0}^{x}\left[\int_{0}^{t} f(s) d s\right] d t \\
& =\int_{0}^{x} \int_{0}^{t} f(s) d s d t
\end{aligned}
$$

The third integral of $f(x)$ is given by

$$
\begin{aligned}
& \left(I^{3} f\right)(x)=\int_{0}^{x}\left(I^{2} f\right)(t) d t \\
= & \int_{0}^{x}\left[\int_{0}^{t} \int_{0}^{s} f(u) d u d s\right] d t \\
= & \int_{0}^{x} \int_{0}^{t} \int_{0}^{s} f(u) d u d s d t
\end{aligned}
$$

As an example consider the function

$$
f(x)=x^{k}
$$

The first integral is given by

$$
\begin{aligned}
& (\text { If })(x)=\int_{0}^{x} t^{k} d t \\
& =\left.\frac{1}{k+1} t^{k+1}\right|_{0} ^{x} \\
& =\frac{x^{k+1}}{k+1}
\end{aligned}
$$

The second integral by

$$
\begin{aligned}
& \left(I^{2} f\right)(x)=\int_{0}^{x} \frac{t^{k+1}}{k+1} d t \\
& =\left.\frac{t^{k+2}}{(k+1)(k+2)}\right|_{0} ^{x} \\
& =\frac{x^{k+2}}{(k+1)(k+2)}
\end{aligned}
$$

It is clear that the n'th integral

$$
\left(I^{n} f\right)(x)=\frac{x^{k+n}}{(k+1)(k+2) \cdots(k+n)}
$$

now

$$
\begin{aligned}
& \frac{1}{(k+1)(k+2) \cdots(k+n)}=\frac{k!}{k!(k+1)(k+2) \cdots(k+n)} \\
& =\frac{k!}{(k+n)!}
\end{aligned}
$$

So

$$
\left(I^{n} f\right)(x)=\frac{k!}{(k+n)!} x^{k+n}
$$

Recall that the Gamma function and the factorial function are related by

$$
\Gamma(k+1)=k!
$$

thus

$$
\left(I^{n} f\right)=\frac{\Gamma(k+1)}{\Gamma(k+n+1)} x^{k+n}
$$

This form of the result is not only valid for integer values of $n$ but also for non integer
values of $n$. This is the motivation of the fractional calculus.
The Cauchy formula is a general expression for the n'th integral of a function $f(x)$ with $x>0$, namely,

$$
\left(I^{n} f\right)(x)=\frac{1}{(n-1)!} \int_{0}^{x}(x-t)^{n-1} f(t) d t
$$

To prove this relation consider $n=1$

$$
\begin{aligned}
g(x) & =\frac{1}{0!} \int_{0}^{x}(x-t)^{0} f(t) d t \\
& =\int_{0}^{x} f(t) d t=(I f)(x)
\end{aligned}
$$

for $n=2$

$$
\begin{aligned}
g(x) & =\frac{1}{1!} \int_{0}^{x}(x-t) f(t) d t \\
& =\int_{0}^{x} x f(t) d t-\int_{0}^{x} t f(t) d t
\end{aligned}
$$

$$
=x \int_{0}^{x} f(t) d t-\int_{0}^{x} t f(t) d t
$$

Now

$$
\begin{aligned}
g^{\prime}(x)= & {\left[\int_{0}^{x} f(t) d t+x f^{\prime}(x)\right] } \\
& -x f(x) \\
= & \int_{0}^{x} f(t) d t=(I f)(x)
\end{aligned}
$$

so

$$
g^{\prime}(x)=(I f)(x)
$$

and

$$
\begin{aligned}
g(x) & =\int_{0}^{x} g^{\prime}(t) d t=\int_{0}^{x}(I f)(t) d t \\
& =\left(I^{2} f\right)(x)
\end{aligned}
$$

for $n=3$

$$
g(x)=\frac{1}{2} \int_{0}^{x}(x-t)^{2} f(t) d t
$$

$$
\begin{aligned}
= & \frac{1}{2} \int_{0}^{x}\left(x^{2}-2 x t+t^{2}\right) f(t) d t \\
= & \frac{1}{2} \int_{0}^{x} x^{2} f(t) d t-\frac{1}{2} \int_{0}^{x} 2 x t f(t) d t \\
& +\frac{1}{2} \int_{0}^{x} t^{2} f(t) d t \\
= & \frac{1}{2} x^{2} \int_{0}^{x} f(t) d t-x \int_{0}^{x} t f(t) d t \\
& +\frac{1}{2} \int_{0}^{x} t^{2} f(t) d t
\end{aligned}
$$

Now

$$
\begin{aligned}
& g^{\prime}(x)=\frac{1}{2}\left[2 x \int_{0}^{x} f(t) d t+x^{2} f(x)\right] \\
& -\left[\int_{0}^{x} t f(t)+x^{2} f(x)\right]+\frac{1}{2} x^{2} f(x) \\
& =x \int_{0}^{x} f(t) d t+\frac{1}{2} x^{2} f^{2}(x)-\int_{0}^{x} t f(t) d t \\
& -x^{2} f(x)+\frac{1}{2} x^{2} f^{2}(x)
\end{aligned}
$$

$$
\begin{aligned}
& =x \int_{0}^{x} f(t) d t-\int_{0}^{x} t f(t) d t \\
& =\int_{0}^{x}(x-t) f(t) d t
\end{aligned}
$$

previously it was shown that

$$
\left(I^{2} f\right)(x)=\int_{0}^{x}(x-t) f(t) d t
$$

50

$$
g^{\prime}(x)=\left(I^{2} f\right)(x)
$$

and

$$
\begin{aligned}
g(x) & =\int_{0}^{x}\left(I^{2} f\right)(t) d t \\
& =\left(I^{3} f\right)(x)
\end{aligned}
$$

In light of this result a proof of the Cauchy formula for an arbitrary $n$ can be obtained using mathimatical induction.
To prove this using mathematical induction it must be shown
that the Cauchy formula is true for $n=1$. Then if we assume that the formula is true for $n-1$ the it is true for $n$. So for $n-1$ it is assumed that

$$
\left(I^{n-1} f\right)(x)=\frac{1}{(n-2)!} \int_{0}^{x}(x-t)^{n-2} f(t) d t
$$

To get started consider

$$
g(x)=\frac{1}{(n-1)!} \int_{0}^{x}(x-t)^{n-1} f(t) d t
$$

Now using the binomial theorem

$$
(x-t)^{n-1}=\sum_{k=0}^{n-1} \frac{(n-1)^{!}}{(n-1-k)!k!}(-1)^{k} x^{n-1-k} t^{k}
$$

it follows that
$g(x)=\frac{1}{(k-1)!} \int_{0}^{x}\left[\sum_{k=0}^{n-1} \frac{(-1)^{k}(n-1)!}{(n-1-k)!k!} x^{n-1-k} t^{k}\right] f(t) d t$
$=\sum_{k=0}^{n-1} \frac{(-1)^{k}}{(n-1-k)!k!} x^{n-1-k} \int_{0}^{x} t^{k} f(t) d t$
$=\sum_{k=0}^{n-2} \frac{(-1)^{k}}{(n-1-k)!k!} x^{n-1-k} \int_{0}^{x} t^{k} f(t) d t$
$+\frac{(-1)^{n-1}}{(n-1)!} \int_{0}^{x} t^{n-1} f(t) d t$
Here the term independent of $x$ is seperated from those dependent of $x$ to facilitate differentiation.

Now

$$
\begin{aligned}
& g^{\prime}(x)=\sum_{k=0}^{n-2} \frac{(-1)^{k}}{(n-1-k)!k!}\left[(n-1-k) x^{n-2-k}\right. \\
& \left.\int_{0}^{x} t^{k} f(t) d t+x^{n-1-k} x^{k} f(x)\right] \\
& +\frac{(-1)^{n-1}}{(n-1)!} x^{n-1} f(x)
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{k=0}^{n-2} \frac{(-1)^{k}}{(n-2-k)!k!} x^{n-2-k} \int_{0}^{x} t^{k} f(t) d t \\
& +\sum_{k=0}^{n-2} \frac{(-1)^{k}}{(n-1-k)!k!} x^{n-1} f(x)+\frac{(-1)^{n-1}}{(n-1)!} x^{n-1} f(x)
\end{aligned}
$$

The last term can be brought into the sum to dotain

$$
\begin{aligned}
& =\frac{1}{(n-2)!} \int_{0}^{x}\left[\sum_{k=0}^{n-2} \frac{(n-2)!(-1)^{k}}{(n-2-k)!k!} x^{n-2-k} t^{k}\right] f(t) d t \\
& +x^{n-1} f(x) \sum_{k=0}^{n-1} \frac{(-1)^{k}}{(n-1-k)!k^{!}} \\
& =\frac{1}{(n-2)!} \int_{0}^{x}(x-t)^{n-2} f(t) d t \\
& +x^{n-1} f(x) \sum_{k=0}^{n-1} \frac{(-1)^{k}}{(n-1-k)!k!}
\end{aligned}
$$

Consider the last term

$$
S(n)=\sum_{k=0}^{n-1} \frac{(-1)^{k}}{(n-1-k)!k^{\prime}}
$$

But

$$
\begin{aligned}
(1-1)^{n-1} & =\sum_{k=0}^{n-1} \frac{(n-1)!}{(n-1-k)!k!}(-1)^{k}(1)^{n-1-k} \\
& =(n-1)!\sum_{k=0}^{n-1} \frac{(-1)^{k}}{(n-1-k)!k!} \\
& =(n-1)!S(n)
\end{aligned}
$$

Thus

$$
s(n)=\frac{(1-1)^{n-1}}{(n-1)!}=0
$$

It follows that

$$
g^{\prime}(x)=\frac{1}{(n-2)!} \int_{0}^{x}(x-t)^{n-2} f(t) d t
$$

From the mathematical induction assumption
$\left(I^{n-1} f\right)(x)=\frac{1}{(n-2)!} \int_{0}^{x}(x-t)^{n-2} f(t) d t$
50

$$
g^{\prime}(x)=\left(I^{n-1} f\right)(x)
$$

$$
\text { and } \begin{aligned}
g(x) & =\int_{0}^{x} g^{\prime}(t) d t=\int_{0}^{x}\left(I^{n-1} f\right)(t) d t \\
& =\left(I^{n} f\right)(x)
\end{aligned}
$$

which proves the Cauchy formula

$$
\left(I^{n} f\right)(x)=\frac{1}{(n-1)!} \int_{0}^{x}(x-t)^{n-1} f(t) d t
$$

## Fractional Integral

The fractional integral is defined with use of the Cauchy formula by allowing the number of iterations to be a positive real number. For this case $n$, which has been assumed, is replaced by 2 which can be any positive real number. This change also requires that the factorial be replaced by the Gamma function using the relation,

$$
\Gamma(n)=(n-1)!
$$

It follows that the fractional integral of a function $f(x)$ for $x>0$ is defined by

$$
\left(I^{\alpha} f(x)=\frac{1}{\Gamma(\alpha)} \int_{0}^{x}(x-t)^{\alpha-1} f(t) d t\right.
$$

Recall the previous example where it was shown that for

$$
f(x)=x^{k}
$$

the repected integral is given by

$$
\left(I^{\alpha} f\right)(x)=\frac{\Gamma(K+1)}{\Gamma(\alpha+K+1)} x^{\alpha+K}
$$

This result was sbtained by explicit evaluation of the integral $n$ times. If the Cauchy formula is used it is found that

$$
\left(I^{\alpha} f\right)(x)=\frac{1}{\Gamma(\alpha)} \int_{0}^{x} t^{k}(x-t)^{\alpha-1} d t
$$

to evaluate the integral make the following change of variables

$$
u=\frac{t}{x} \quad \Rightarrow \quad d t=x d u
$$

gives

$$
\begin{aligned}
\left(I^{\alpha} f\right)(x) & =\frac{1}{\Gamma(\alpha)} \int_{0}^{x} t^{k}(x-t)^{\alpha-1} d t \\
& =\frac{1}{\Gamma(\alpha)} \int_{0}^{1}(x u)^{k}(x-x u)^{\alpha-1} x d u \\
& =\frac{1}{\Gamma(\alpha)} \int_{0}^{1} x^{k} u^{k} x^{\alpha-1}(1-u)^{\alpha-1} x d u \\
& =\frac{1}{\Gamma(\alpha)} \int_{0}^{1} x^{k+\alpha} u^{k}(1-u)^{\alpha-1} d u \\
& =\frac{x^{k+\alpha}}{\Gamma(\alpha)} \int_{0}^{1} u^{k}(1-u)^{\alpha-1} d u
\end{aligned}
$$

Now the Beta function is defined by

$$
B(x, y)=\int_{0} t^{x-1}(1-t)^{y-1} d t
$$

and the Beta and Gamma function are related by

$$
B(x, y)=\frac{\Gamma(x) \Gamma(y)}{\Gamma(x+y)}
$$

It follows that

$$
B(k+1, \alpha)=\int_{0}^{1} u^{k}(1-u)^{\alpha-1}
$$

so

$$
B(k+1, \alpha)=\frac{\Gamma(k+1) \Gamma(\alpha)}{\Gamma(\alpha+k+1)}
$$

Returning to the repeated integral gives

$$
\begin{aligned}
\left(I^{\alpha} f\right)(x) & =\frac{1}{\Gamma(\alpha)} \int_{0}^{x} t^{k}(x-t)^{\alpha-1} \\
& =\frac{x^{k+\alpha}}{\Gamma(\alpha)} \frac{\Gamma(k+1) \Gamma(\alpha)}{\Gamma(\alpha+k+1)} \\
& =\frac{\Gamma(k+1)}{\Gamma(\alpha+k+1)} x^{k+\alpha}
\end{aligned}
$$

which is the same result obtained by repeate integration.

## Algebra of Repeated Integration

Now consider $f(x)=x^{k}$ where, $\alpha$, is a positive real number. It was previously shown that,

$$
\left(I^{\alpha} f\right)(x)=\frac{\Gamma(k+1)}{\Gamma(\alpha+k+1)} x^{\alpha+k}
$$

Now if $\beta$ is a real number

$$
\begin{aligned}
& \left(I^{\beta}\left(I^{\alpha} f\right)\right)(x)=\frac{\Gamma(k+1)}{\Gamma(\alpha+k+1)} \frac{\Gamma(\alpha+k+1)}{\Gamma(\alpha+\beta+k+1)} x^{\alpha+\beta+k} \\
& =\frac{\Gamma(k+1)}{\Gamma(\alpha+\beta+k+1)} x^{\alpha+\beta+k} \\
& =\left(I^{\alpha+\beta} f\right)(x)
\end{aligned}
$$

Thus for $f(x)=x^{k}$

$$
\begin{aligned}
\left(I^{\beta}\left(I^{\alpha} f\right)\right)(x) & =\left(I^{\alpha+\beta} f(x)\right. \\
& =\left(I^{\alpha}\left(I^{\beta} f\right)\right)(x)
\end{aligned}
$$

which is the familiar addition algebra
of exponents. This result was easy to show for this case but is true in general but much more difficurt to prove.

## Derivatives and Integrals

Repected integration of a function $f(x)$ is a new concept but repeated differentiation is
familiar from elementary calculus. As and example of repeated differentiation consider the function $f(x)=x^{2}$

$$
\begin{aligned}
\frac{d^{2}}{d x^{2}} f(x) & =\frac{d}{d x}\left(\frac{d f}{d x}\right) \\
& =\frac{d}{d x}(2 x) \\
& =2
\end{aligned}
$$

In previous sections the repeated integration of $f(x)$ discussed. Next mixing repeated integration and diffentiation are considered. Furst consider the integration of a function followed by differentiation

$$
\begin{aligned}
\frac{d}{d x}(I f)(x) & =\frac{d}{d x} \int_{0}^{x} f(t) d t \\
& =f(x)
\end{aligned}
$$

which is the expected result that differentiation and integration are inverse operations. This result was actuall used in the proof of the cauchy formula.
If the operations are applied in the opposite order is the result the same? Consider the function

$$
f(x)=e^{x}
$$

so

$$
\begin{aligned}
& \left(I\left(\frac{d f}{d x}\right)\right)(x)=\left(I\left(e^{x}\right)\right)(x) \\
& =\int_{0}^{x} e^{t} d t=\left.e^{x}\right|_{0} ^{1}=e^{x}-1 \\
& \neq f(x)
\end{aligned}
$$

The result follows because repeated integration is defined by a definite integral not an indefinite integral. It follows that repeated integration and diffentiation do not commute and if differentiation is followed by integration the result is not as expected. In this case integration and differentiation are not inverse operations. If integration is applied before differtation the operations are inverse.

## Repeated Derivatives of Repeated Integrals

since repeated diffentiation and repedied integration are inverse opperations on a function $f(x)$ only if integration is perfored first. This will be assumed in the following discussion.
suppose $p$ and $q$ are positive and that $p>q$. The $q$ th derivative of the pth integral is given by

$$
\begin{aligned}
& \frac{d^{q}}{d x^{q}}\left(I^{P} f\right)(x)=\frac{d^{q-1}}{d x^{q-1}}\left[\frac{d}{d x}\left(I^{P} f\right)(x)\right] \\
= & \frac{d^{q-1}}{d x^{q-1}}\left[\frac{d}{d x}\left(I\left(I^{P-1} f\right) x(x)\right]\right. \\
= & \frac{d^{q-1}}{d x^{q-1}}\left(I^{P-1} f\right)(x) \\
= & \left(I^{P-q} f\right)(x)
\end{aligned}
$$

This is a straight forward result since $p>q$ but what is done if $p<q$. In this case integration is done $p-q<0$ times. Intuitively negative integration should be interpreted as differentiation. If this is assumed then for $q>0$

$$
\frac{d^{9}}{d x^{9}} f(x)=\left(I^{-9} f\right)(x)
$$

Furthur if the canstraint that $q$ is an integer is relaxed how is a fractional derivative interpreted. Assume that $\alpha$ is a positive real number

$$
\frac{d^{\alpha}}{d x^{\alpha}} f(x)=\left(I^{-\alpha} f\right)(x)
$$

This relation is intuitive but there is no way to evaluate the repeated integral a negaive number of times. This problem can be overcome by noting that
for and positive integer $k$

$$
\frac{d^{k}}{d x^{k}}\left(I^{k} f\right)(x)=f(x)
$$

If furthure $t$ is assumed that

$$
\alpha<k
$$

then

$$
\frac{d^{\alpha}}{d x^{\alpha}} f(x)=\frac{d^{k}}{d x^{k}}\left(I^{k-\alpha} f\right)(x)
$$

## Fractional Deriuative

In the previous section an expression to compute the fractional derivative of a function $f(x)$ was derived,

$$
\frac{d^{\alpha}}{d x^{\alpha}} f(x)=\frac{d^{k}}{d x^{k}}\left(I^{k-\alpha} f\right)(x)
$$

where $\alpha>0$ is a real number and $k>0$ is an integer. As an example what is the $1 / 2$ derivative of $f(x)=x$. using the formula with $k=1$

$$
\frac{d^{1 / 2}}{d x^{1 / 2}} f(x)=\frac{d}{d x}\left(I^{1 / 2} f\right)(x)
$$

Recall that the Cauchy formula is given by

$$
\left(I^{\alpha} f(x)=\frac{1}{\Gamma(\alpha)} \int_{0}^{x}(x-t)^{\alpha-1} f(t) d t\right.
$$

Now for $f(x)=x$

$$
\left(I^{1 / 2} f\right)(x)=\frac{1}{\Gamma(1 / 2)} \int_{0}^{x}(x-t)^{-1 / 2} t d t
$$

using

$$
\Gamma(1 / 2)=\sqrt{\pi}
$$

The integral can be evaluated by making the change of variables,

$$
u=x-t \Rightarrow d u=-d t
$$

gives

$$
\begin{aligned}
& \int_{0}^{x}(x-t)^{-1 / 2} t d t=\int_{0}^{x} u^{-1 / 2}(x-u) d u \\
& =\int_{0}^{x}\left(x u^{-1 / 2}-u^{1 / 2}\right) d u \\
& =\left.\left(2 x u^{1 / 2}-2 / 3 u^{3 / 2}\right)\right|_{0} ^{x} \\
& =2 x^{3 / 2}-\frac{2}{3} x^{3 / 2} \\
& =\frac{4}{3} x^{3 / 2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\frac{d^{1 / 2}}{d x^{1 / 2}} f(x) & =\frac{4}{3 \sqrt{\pi}} \frac{d}{d x}\left(x^{3 / 2}\right) \\
& =\frac{2}{\sqrt{\pi}} \sqrt{x}
\end{aligned}
$$

Next consider $f(x)=x^{-1 / 2}$. The $1 / 2$ integral is given by

$$
\left(I^{1 / 2} f\right)(x)=\frac{1}{\Gamma(1 / 2)} \int_{0}^{x}(x-t)^{-1 / 2} t^{-1 / 2} d t
$$

Making the change of variables

$$
t=x u \Rightarrow d t=x d u
$$

then

$$
\begin{aligned}
& \int_{0}^{x}(x-t)^{-1 / 2} t^{-1 / 2} d t=\int_{0}^{1} x(x-x u)^{-1 / 2}(x u)^{-1 / 2} d u \\
& =x\left(x^{-1 / 2}\right)\left(x^{-1 / 2}\right) \int_{0}^{1}(1-u)^{-1 / 2} u^{-1 / 2} d u
\end{aligned}
$$

$$
\begin{aligned}
& =\int_{0}^{1}(1-u)^{-1 / 2} u^{-1 / 2} d u \\
& =\int_{0}^{1} \frac{1}{\sqrt{u(1-u)}} d u
\end{aligned}
$$

Consider the additional change of variables

$$
\begin{gathered}
u=\sin ^{2} \theta \Rightarrow \quad d u=2 \sin \theta \cos \theta \\
1-u=1-\sin ^{2} \theta=\cos ^{2} \theta
\end{gathered}
$$

then

$$
\begin{aligned}
& \int_{0}^{1} \frac{1}{\sqrt{u(l-u)}} d u=2 \int_{0}^{\pi / 2} \frac{\sin \theta \cos \theta}{\sqrt{\sin ^{2} \theta \cos ^{2} \theta}} d \theta \\
& =2 \int_{0}^{\pi / 2} d \theta=\pi
\end{aligned}
$$

Thus

$$
\frac{d^{1 / 2}}{d x^{1 / 2}}\left(x^{1 / 2}\right)=\frac{d}{d x}\left(I^{1 / 2}\left(x^{1 / 2}\right)\right)(x)
$$

$$
=\frac{d}{d x}(\sqrt{\pi})=0
$$

It is worth noting here that

$$
\frac{d\left(x^{1 / 2}\right)}{d x}=\frac{1}{\partial \sqrt{x}}
$$

But

$$
\begin{aligned}
\frac{d}{d x}\left(x^{1 / 2}\right) & =\frac{d^{1 / 2}}{d x^{1 / 2}}\left(\frac{d^{1 / 2}}{d x^{1 / 2}} x^{1 / 2}\right) \\
= & 0
\end{aligned}
$$

Thus it is not always true that

$$
\frac{d^{\alpha}}{d x^{\alpha}} \frac{d^{\beta}}{d x^{\beta}}=\frac{d^{\alpha+\beta}}{d x^{\alpha+\beta}}
$$

if $\alpha$ and $\beta$ are not integers.
to complete this exercise consider

$$
f(x)=1
$$

The $1 / 2$ integral of $f(x)$ is given by

$$
\left(I^{1 / 2} f\right)(x)=\frac{1}{\Gamma(1 / 2)} \int_{0}^{x}(x-t)^{-1 / 2} d t
$$

Making the change of variables

$$
\begin{aligned}
& t=x u \Rightarrow d t=x d u \\
& \int_{0}^{x}(x-t)^{-1 / 2} d t=\int_{0}^{1}(x-x u)^{-1 / 2} x d u \\
& =x^{1 / 2} \int_{0}^{1}(1-u)^{-1 / 2} d u
\end{aligned}
$$

Consider the additional change of variables

$$
\begin{gathered}
u=\sin ^{2} \theta \Rightarrow d u=2 \sin \theta \cos \theta \\
1-u=1-\sin ^{2} \theta=\cos ^{2} \theta
\end{gathered}
$$

Making the change of variables

$$
\begin{aligned}
& \int_{0}^{x}(x-t)^{-1 / 2} d t=\sqrt{x} \int_{0}^{1}(1-u)^{-1 / 2} d u \\
& =\sqrt{x} \int_{0}^{\pi / 2}\left(1-\sin ^{2} \theta\right)^{-1 / 2}(2 \sin \theta \cos \theta) d \theta \\
& =\sqrt{x} \int_{0}^{\pi / 2} 2 \sin \theta d \theta=\left.2 \sqrt{x}(-\cos \theta)\right|_{0} ^{\pi / 2} \\
& =2 \sqrt{x}
\end{aligned}
$$

thus

$$
\begin{aligned}
& \frac{d^{1 / 2}}{d x^{1 / 2}}(1)=\frac{d}{d x}\left(I^{1 / 2}(1)\right)(x) \\
& =\frac{d}{d x}\left(\frac{2 \sqrt{x}}{\sqrt{\pi}}\right)=\frac{1}{\sqrt{\pi x}}
\end{aligned}
$$

In summary the 1/2 derivative of the following functions was evaluated

$$
\begin{gathered}
f(x)=x \quad f(x)=x^{-1 / 2} \\
f(x)=1
\end{gathered}
$$

using the expression

$$
\frac{d^{1 / 2}}{d x^{1 / 2}} f(x)=\frac{d}{d x}\left(I^{1 / 2} f\right)(x)
$$

with the results.

$$
\frac{d^{1 / 2}}{d x^{1 / 2}}(x)=\frac{2}{\sqrt{\pi}}
$$

$d^{1 / 2}\left(x^{-1 / 2}\right)=0$
$d x^{1 / 2}$

$$
\frac{d^{1 / 2}}{d x^{1 / 2}}(1)=\frac{1}{\sqrt{\pi x}}
$$

## Left and Right Forms of Repeated Integration

Repeated integration was first defined by the following form of the cauchy formula

$$
\left(I^{\alpha} f(x)=\frac{1}{\Gamma(\alpha)} \int_{0}^{x}(x-t)^{\alpha-1} f(t) d t\right.
$$

for this definition $x-t>0$ over the the range of integration $[0, x]$.
Consider the case where $a<t<b$ and $t-x \geqslant 0$. Let

$$
(t-x)_{+}^{\alpha-1}=0
$$

for $t-x \geqslant 0$. using this notation the cauchy formula with integration over the interval $[a, b]$ becomes

$$
(I-f)(x)=\frac{1}{\Gamma(\alpha)} \int_{a}^{b}(t-x)_{+}^{\alpha-1} f(t) d t
$$

$$
=\frac{1}{\Gamma(\alpha)} \int_{x}^{b}(t-x)^{\alpha-1} f(t) d t
$$

This form of the Cauchy formula is called the right integral since the integration interval is $[x, b]$. similarly the left form of the integral is denuted by

$$
\begin{aligned}
\left(I_{+}^{\alpha} f\right)(x) & =\frac{1}{\Gamma(\alpha)} \int_{a}^{b}(x-t)_{+}^{\alpha-1} f(t) d t \\
& =\frac{1}{\Gamma(\alpha)} \int_{a}^{x}(x-t)^{\alpha-1} f(t) d t
\end{aligned}
$$

where $x-t \geqslant 0$.

## Summary

The foundation of the fractional calculus has been discussed. The big idea at the foundation is the repeated integral of a function $f(x)$ for $x>0$ and the Cauchy formula. The repeated first integral of $f(x)$ is defined by

$$
(\text { If })(x)=\int_{0}^{x} f(t) d t
$$

If $n>0$ is an integer the n'th integral is defined by

$$
\left(I f^{n}\right)(x)=\int_{0}^{x} \int_{0}^{t_{n-1}} \cdots \int_{0}^{t_{1}} f(s) d s d t_{1} \cdots d t_{n-1}
$$

It was shown that this integral is equal to the single integral called the Cauchy Formula,

$$
\left(I f^{n}\right)(x)=\frac{1}{(n-1)!} \int_{0}^{x}(x-t)^{n-1} f(t) d t
$$

This result was generalized to $\alpha>0$ for $\alpha$ a real number,

$$
\left(I f^{\alpha}\right)(x)=\frac{1}{\Gamma(\alpha)} \int_{0}^{x}(x-t)^{\alpha-1} f(t) d t
$$

It was shown that for $\alpha>0$ and $\beta>0$ where both are real

$$
\left(I^{\beta}\left(I^{\alpha} f\right)\right)(x)=\left(I^{\alpha+\beta} f\right)(x)
$$

Next repeated integration and diffentiation were discussed. It was shown that if integration is performed first differentiation and repeated integration are inverse operations

$$
\frac{d}{d x}(I f)(x)=f(x)
$$

but if differentiation is peformed first followed by integration that

$$
\left(I\left(\frac{d f}{d x}\right)\right)(x) \neq f(x)
$$

Thus repeated integration and repeated differention do not commute.
An interpetation of repeated differentiation as negative repeated integration was suggested

$$
\frac{d^{n}}{d x^{n}} f(x)=\left(I^{-n} f\right)(x)
$$

This result was used to defive a formula for the repeeted derivative to fractional values,

$$
\frac{d^{\alpha}}{d x^{\alpha}} f(x)=\frac{d^{k}}{d x^{k}}\left(I^{k-\alpha} f\right)(x)
$$

where $\alpha$ is real and satisfies
$\alpha>0$ and $k$ is an integer satisfying $k>\alpha$.
It was shown that for fractional derivatives

$$
\frac{d^{\alpha}}{d x^{\alpha}} \frac{d^{\beta}}{d x^{\beta}}=\frac{d^{\alpha+\beta}}{d x^{\alpha+\beta}}
$$

sereral examples of the fractional derivative were cralleated. The results were

$$
\begin{aligned}
& \frac{d^{1 / 2}}{d x^{1 / 2}}(x)=\frac{2}{\sqrt{\pi}} \\
& \frac{d^{1 / 2}}{d x^{1 / 2}}\left(x^{-1 / 2}\right)=0 \\
& \frac{d^{1 / 2}}{d x^{1 / 2}}(1)=\frac{1}{\sqrt{\pi} x}
\end{aligned}
$$

Finally the left and right forms of the Cauchy formula were
shown to be

$$
\begin{aligned}
(I \alpha f)(x) & =\frac{1}{\Gamma(\alpha)} \int_{a}^{b}(x-t)_{+}^{\alpha-1} f(t) d t \\
& =\frac{1}{\Gamma(\alpha)} \int_{x}^{b}(x-t)^{\alpha-1} f(t) d t \\
\left(I_{+}^{\alpha} f\right)(x) & =\frac{1}{\Gamma(\alpha)} \int_{a}^{b}(t-x)_{+}^{\alpha-1} f(t) d t \\
& =\frac{1}{\Gamma(\alpha)} \int_{a}^{x}(t-x)^{\alpha-1} f(t) d t
\end{aligned}
$$

where for ( $I^{\alpha} f(x) \quad x-t \geqslant 0$ and for $\left(I_{+}^{2} f(x)\right.$ t-x $\geqslant 0$.

## Stochastic Calculus

Recall that Brownian Motion with drift is defined by

$$
x\left(t_{j}\right)=\mu t_{j}+\sigma B\left(t_{j}\right)
$$

where $B\left(t_{j}\right)$ is Brownian motion

$$
B\left(t_{j}\right)=\Delta t \sum_{i=0}^{j} z_{i}
$$

and $z_{i}$ are independent unit normal random variables.
To simplify notation let

$$
X_{j}=X\left(t_{j}\right) \quad B_{j}=B\left(t_{j}\right)
$$

then

$$
\begin{aligned}
\Delta x_{j}=x_{j}-x_{j-1} & =\mu \Delta t+\sigma\left(B_{j}-B_{j}\right) \\
& =\mu \Delta t+\sigma \Delta B_{j}
\end{aligned}
$$

but

$$
\Delta B_{j}=\Delta t z_{j}
$$

thus

$$
\Delta x_{j}=\mu \Delta t+\sigma \Delta t z_{j}
$$

Here $\mu$ and $\sigma$ are constants. This expression can be generalized by assuming that $\mu$ and $\sigma$ are functions of $t_{n}$ and $x_{n}$, thus

$$
\begin{aligned}
\Delta x_{j} & =\mu\left(t_{j}, x_{j}\right) \Delta t+\sigma\left(t_{j}, x_{j}\right) \Delta t Z_{j} \\
& =\mu\left(t_{j}, x_{j}\right) \Delta t+\sigma\left(t_{j}, x_{j}\right) \Delta B_{j}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& x_{n}-x_{0}=\sum_{j=0}^{n} \Delta x_{j} \\
& =\sum_{j=0}^{n} \mu\left(t_{j}, x_{j}\right) \Delta t+\sum_{j=0}^{n} \sigma\left(t_{j}, x_{j}\right) \Delta B_{j}
\end{aligned}
$$

Consider the limit $\Delta t \rightarrow 0$ and $n \rightarrow \infty$ so that $t_{n} \rightarrow t$, then

$$
\begin{aligned}
x_{t}=x_{0} & +\int_{0}^{t} \mu\left(s, x_{s}\right) d s \\
& +\int_{0}^{t} \sigma\left(s, x_{s}\right) d B_{s}
\end{aligned}
$$

The first integral is one of the tipical variety. The second is a new type of integral where the differential is Brownian noise. The following sections will consider this integral in more detail.

## General Probability Theory

## Definition of Sample space and Field

A sample space, denoted by $\Omega$, is the set of all possibe dutcomes of an experiment.
A field, denoted by 7 , is a
collection of subsets of events
belonging to $\Omega$ that satisfy the following conditions

1. $\phi \in \mathcal{F}$ where $\phi$ is the empty set
2. If $A \in \mathcal{F}$ then $A^{c} \in \mathcal{F}$ where $A^{c}$ is the compliment of $A$ in $\Omega$. That is all events that are not $A$.
3. If $A_{1}, A_{2}, A_{3}, \ldots, A_{n} \in \mathcal{F}$ then
$\because A_{i} \in \mathcal{F}$. That is $\mathcal{F}$ is closed $i=1$
under finite unions of elements.

## Definition of $\gamma$-Algebra

If $\Omega$ is a given sample space, then a $\sigma$-algebra $\mathcal{F}$ on $\Omega$ with the following properties

1. $\varnothing \in \mathcal{F}$
2. If $A \in \mathcal{F}$ then $A^{C} \in \mathcal{F}$ where $A^{C}$ is the compliment of $A$ in $\Omega$.
3. If $A_{1}, A_{2}, \ldots \in \mathcal{F}$ then i $A_{i} \in \mathcal{F}$. That is $\mathcal{F}$ is closed $i=1$

## under countable unions.

## Measurable Space

The pair $(\Omega, \mathcal{F})$ is called a measure able spoce. A probability measure $P$ on a measureable space is a function $P: \mathcal{F} \rightarrow[0,1]$ such that

1. $P(\phi)=0$
2. $P(\Omega)=1$
3. If $A_{1}, A_{2}, A_{3}, \ldots \in \mathcal{F}$ and $\left\{A_{i}\right\}_{i=1}^{\infty}$
is disjoint such that $A_{i} \cap A_{j}=\varnothing \quad i \neq j$ then

$$
P\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)
$$

The triple $(\Omega, F, P)$ is called a probability space. It is called a complete probability space if $\mathcal{F}$ aslo contains subsets $B$ of $\Omega$ with P-outer measure zero, that is

$$
P^{*}(B)=\inf \{P(A): A \in \mathcal{J}, B \subset A\}=0
$$

## Filtration

Let $\Omega$ be a non-empty sample space and let $T$ be a fired positive number, and assume for each $t \in[0, T]$ there is a o-algebra $\mathcal{F}_{t}$. In addition, assume that if $s \leqslant t$ then every set in $\mathcal{F}_{s}$
is atso in $\mathcal{F}_{t}, \mathcal{F}_{s} \subset \mathcal{F}_{t}$. The oolledion of $\sigma$-algebras $\mathcal{F}_{t}, 0 \leqslant t \leqslant T$ is called a filtration.

## F Measurable

Let $\Omega$ be a non-empty sample space and let $\mathcal{F}$ be a G-abebra of subsets of $\Omega$. A real-valued random variable $X$ is a function

$$
\bar{X}: \Omega \rightarrow \mathbb{R}
$$

such that

$$
\{\omega \in \Omega: \bar{x}(\omega) \leqslant x\} \in \mathcal{F}
$$

for each $x \in \mathbb{R}$ and we say $I$ is F measureable.

## Adapted Stochastic Process

Let $\Omega$ be a non-emply sample space with filtration $\mathcal{F}_{t}, t \in[0, T]$ and let $X_{t}$ be a collection of

Random variables indexed by $t \in[0, \tau]$. We therefore say that this collection of random varicebles is an adapted stochastic process if for each $t$ the random variable $I_{t}$ is $F_{t}$ measurable.

## Conditional Expectation and Partial Averaging Property

Let $(\Omega, \Im, P)$ be a probability space and let \& be a sub-6-abetira of $\mathcal{F}, \mathcal{z} \in \mathcal{F}$. Let $\bar{X}$ be an integrable and non-negative random variable, $E[|x|]<\infty$. Then the conditional expectation of $\underline{X}$ given $\Delta$, denoted $E[\bar{x} \mid 2)]$, is any random variable that satisfies:

1. $E[x \mid \mathcal{D}]$ is $\neq$ measurable
2. For every set $A \in$ I the partial averaging property is satisfied

$$
\int_{A} E[\bar{X} \mid \mathcal{D}] d P=\int_{A} \bar{X} d P
$$

This expression can be derived by considering $\Delta$ can be generated by a finite number of disjoint sets $A_{j}$. Assume $E[X \mid A]$ is constant on $A_{j}$. Then,

$$
\begin{aligned}
E[X \mid A] & =\frac{1}{P\left(A_{j}\right)} \int_{A_{j}} Z d P \\
& =\frac{1}{P\left(A_{j}\right)} E\left[\underline{1}_{A_{j}} \bar{X}\right]
\end{aligned}
$$

Intuitively this makes sense. It is the conditional average of $\bar{I}$ assuming A; happened with conditional density

$$
\frac{d P}{P\left(A_{j}^{\prime}\right)}
$$

Now let

$$
A=A_{1} \cup A_{2} \cup \cdots \cup A_{n}
$$

where the $A_{i}$ are disjoint. It follows that

$$
\begin{aligned}
& \int_{A} E[X \mid \Delta] d P=\sum_{i=1}^{n} P\left(A_{i}\right) \int_{A_{i}} E[X \mid \Delta] d P \\
& =\sum_{i=1}^{n} P\left(A_{i}\right) \frac{1}{P\left(A_{i}\right)} \int_{A_{i}} X d P \\
& =\sum_{i=1}^{n} \int_{A_{i}} X d P \\
& =\int_{A} Z d P
\end{aligned}
$$

Thus

$$
\int_{A} E[X \mid A] d P=\int_{A} \bar{X} d P
$$

As an alterative definition consider the probability space $(\Omega, \mathcal{F}, P)$ and let $\forall C \mathcal{F}$ and $\bar{X}$ be a random variable, then denote the o-fied generated $\bar{X}$ by $\sigma(\bar{X})$, then

$$
E[\bar{X} \mid \Delta]=\frac{1}{P(A)} \int_{A} \bar{X}(\omega) d P(\sigma(\bar{X}) \cap A)(\omega)
$$

Converting the integration to a sum gives a form similar to that obtained for continuous random variables with a joint probability density

$$
\begin{aligned}
E[\bar{X} \mid \Delta] & =\sum_{\omega \in A} \bar{X}(\omega) \frac{P(\sigma(\bar{X}) \cap A)(\omega)}{P(A)} \\
& =\sum_{\omega \in A} \bar{X}(\omega) P(\sigma(\bar{X}) \mid A)(\omega)
\end{aligned}
$$

## Standard Wiener Process

Let $(\Omega, F, P)$ be a probability space. A stochastic process

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

is defined to be a standard wemer process if

1. $\omega_{0}=0$
2. For each $t>0$ and $s>0$
$\omega_{t+s}-\omega_{s}$ is a normal random variale with zero mean and variance $s$,

$$
\omega_{t+s}-\omega_{s} \sim N(0, s)
$$

3. For each $t>0$ and $s>0 \omega_{t+s}-\omega_{t}$ is independent of $\omega_{t}$

$$
\omega_{t+s}-\omega_{s} \Perp \omega_{t}
$$

## Wiener Process

A wiener process is defined by

$$
\hat{\omega}_{t}=v+\mu t+\sigma \omega_{t}
$$

where $\nu$ and $\mu \in \mathbb{R}, \sigma>0$ and $\omega_{t}$ is a standard wiener process.

## Markov Property

Let $(\Omega, \mathcal{F}, P)$ be a probability space. The standard Weiner process $\left\{\omega_{t}: t \geqslant 0\right\}$ is a Markov process such that the conditional distribution of $\omega_{t}$ given the fittration $f_{s}, s<t$ depends only on $\omega_{s}$.

## strong Markou Property

Let $(\Omega, F, P)$ be a probility space. If $\left\{\omega_{t}: t \geqslant 0\right\}$ is a standard

Wiener process and given $\mathfrak{F}_{t}$ is the fituration up to time $t$, then for $s>0 \quad \omega_{t+s}-\omega_{t}$ is independent of $\omega_{t}$

$$
\omega_{t+s}-\omega_{t} \Perp \omega_{t}
$$

## Martingale Property (Continuous Process)

Let $(\Omega, \Im, P)$ be a probability space. A stochastic process $\left\{\dot{X}_{t}: t \geqslant 0\right\}$ is a continuous-time martingale if:

1. $E\left[\bar{x}_{t} \mid \mathcal{F}_{s}\right]=\bar{x}_{s}$ for all $0 \leqslant s \leqslant t$
2. $E\left[\left|X_{t}\right|\right]<\infty$
3. $\bar{x}_{t}$ is $\mathcal{F}_{t}$-adapted. This means that for $t>0$ a filtration $f_{t}$ exists such that

$$
\left\{\omega \in \Omega: Z_{t}(\omega) \leq x_{t}\right\} \in \mathcal{F}_{t}
$$

Property 1 can be relaxed to produce a submartingale for
$E\left[X_{t} \mid \mathcal{F}_{s}\right] \geqslant \bar{I}_{s}$ and a supermartingale for $E\left[\bar{X}_{t} \mid \mathcal{F}_{s}\right] \leqslant \underline{I}_{s}$ where $0 \leqslant s \leqslant t$.

## Martingal Property (Discrete Process)

A discrete process,

$$
\underline{X}=\left\{\bar{X}_{n}: n=0,1,2, \ldots\right\}
$$

is a martingale relative to $(\Omega, \mathcal{F}, P)$ if for all $n$

1. $E\left[\underline{Z}_{n+1} \mid F_{n}\right]=\bar{X}_{n}$
2. $E\left[\left|X_{n}\right|\right]<\infty$
3. $\bar{X}_{n}$ is $\mathcal{J}_{n}$ adapted.

Property 1 can be relaxed to produce a submartingale for
$E\left[X_{n+1} \mid I_{n}\right] \geqslant Z_{n}$ and $a$
supermartingale $E\left[X_{n+1} \mid F_{n}\right] \leqslant I_{n}$ for every $n$.

## Properties of Expectations

## Expectation as Tail Probapility

show that if $x$ is a positive integer

$$
E[X]=\sum_{x=0}^{\infty} P(\bar{\Delta}>x)
$$

Proof:

$$
E[\bar{x}]=\sum_{y=0}^{\infty} y P(\bar{x}=y)
$$

Now

$$
y=\sum_{x=0}^{y} 1
$$

so

$$
\begin{aligned}
E[\bar{x}] & =\sum_{y=0}^{\infty}\left(\sum_{x=0}^{y} 1\right) P(\bar{x}=y) \\
& =\sum_{y=0}^{\infty} \sum_{x=0}^{y} P(\bar{x}=y)
\end{aligned}
$$

The summation indices satisfy

$$
0 \leqslant x \leqslant y
$$

so swithing the order of summation gives

$$
\begin{aligned}
\sum_{y=0}^{\infty} & \sum_{x=0}^{y} P(\bar{x}=y)=\sum_{x=0}^{\infty} \sum_{y=x}^{\infty} P(\underline{x}=y) \\
& =\sum_{x=0}^{\infty} P(\bar{x} \geqslant x)
\end{aligned}
$$

since

$$
P(\underline{x} \geqslant x)=\sum_{y=x}^{A} P(\underline{x}=y)
$$

Thus

$$
E[\bar{x}]=\sum_{x=0}^{\infty} P(\bar{x} \geqslant x)
$$

similarly for the continuous case

$$
\begin{aligned}
E[\bar{x}] & =\int_{0}^{\infty} y P(\bar{x}=y) d y \\
& =\int_{0}^{\infty} \int_{0}^{y} P(\bar{x}=y) d x d y \\
& =\int_{0}^{\infty} \int_{x}^{\infty} P(\bar{x}=y) d y d x \\
& =\int_{0}^{\infty} P(\bar{x} \geqslant x) d x
\end{aligned}
$$

## Minkowski Inequality

Show that for random variable $\bar{X}$ with mean

$$
\mu=E[X]
$$

where $\alpha>0$ that

$$
P(\bar{x} \geqslant \alpha) \leqslant \frac{\mu}{2}
$$

Now let

$$
\mathbb{I}_{[x \geqslant \alpha]}= \begin{cases}1 & x \geqslant \alpha \\ 0 & x<\alpha\end{cases}
$$

since $\bar{X} \geqslant 0$ and $\alpha>0$

$$
\mathbb{I}_{[x \geqslant \alpha]}<\frac{x}{\alpha}
$$

Taking expectations gives

$$
E[\mathbb{I}[x \geqslant \alpha]] \leqslant E\left[\frac{x}{\alpha}\right]=\frac{\mu}{\alpha}
$$

but

$$
\begin{aligned}
E[I[x \geqslant \alpha]] & =(1) P(\bar{x} \geqslant \alpha)+(0) P(\bar{x}<\alpha) \\
& =P(\bar{x} \geqslant \alpha)
\end{aligned}
$$

Thus

$$
P(x \geqslant \alpha) \leqslant \frac{\mu}{\alpha}
$$

## Chebysheu's Inequality

show that for a random variable $\bar{x}$ with mean $\mu$ and variance $\sigma^{2}$ for $k>0$

$$
P(|\bar{x}-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

Note that

$$
(\bar{x}-\mu)^{2} \geqslant k^{2} \Rightarrow|\bar{x}-\mu| \geqslant k
$$

From the minkowski inequality

$$
\begin{aligned}
P\left[(\bar{x}-\mu)^{2} \geqslant k^{2}\right) & \leqslant E\left[\frac{(\bar{x}-\mu)^{2}}{k^{2}}\right] \\
& =\frac{\sigma^{2}}{k^{2}} \\
\Rightarrow P\left(|\bar{x}-\mu|^{2} \geqslant k\right) & \leqslant \frac{\sigma^{2}}{k^{2}}
\end{aligned}
$$

## Conditional Probability

Let $(\Omega, F, P)$ be a probability space and let is be a sub-6-algebra of $\mathcal{F}, y \leq \mathcal{F}$. If $I_{A}$ is an indicator random variable for an event $A$ defined as

$$
I_{A}(\omega)= \begin{cases}1 & \text { if } \omega \in A \\ 0 & \text { otherwise }\end{cases}
$$

show that

$$
E\left[\mathbb{I}_{A}(\omega) \mid \mathscr{L}\right]=P(A \mid \mathscr{D})
$$

Since $E\left[\Pi_{A}(\omega) \mid y\right]$ is $\neq y$ measurable a real valued function $\Pi_{A}(\omega)$ exists to determine membership in $y^{\text {but does not imply the }} A \in D$. It may be that no events or some events in $A$ are in $A$.

Consider a set of events $B$ where $B \in D$. Then by the partial aweraging property

$$
\int_{B} E\left[\mathbb{I}_{A} \mid z\right] d P=\int_{B} \mathbb{I}_{\Delta} d P
$$

The desired result is obtained by showing

$$
\int_{B} I_{A} d P=\int_{B} P(A \mid \Delta) d P
$$

Let

$$
I_{B}(\omega)= \begin{cases}1 & \text { if } \omega \in B \\ 0 & \text { otherwise }\end{cases}
$$

Then

$$
\mathbb{I}_{A \cap B}(\omega)= \begin{cases}1 & \text { if } \omega \in A \cap B \\ 0 & \text { otherwise }\end{cases}
$$

Now since $B \in \mathscr{A}$

$$
\int_{B} P(A \mid A) d P=P(A \cap B)
$$

and

$$
P(A \cap B)=\int_{\Omega} \mathbb{1}_{A \cap B} d P
$$

$$
\begin{aligned}
& =\int_{\Omega} \mathbb{1}_{A} \mathbb{1}_{B} d P \\
& =\int_{B} \mathbb{1}_{A} d P
\end{aligned}
$$

Thus the desired result is obtained

$$
\int_{B} E\left[\mathbb{I}_{A} \mid \mathcal{D}\right] d P=\int_{B} P(A \mid \mathcal{D}) d P
$$

and

$$
E\left[\Pi_{A} \mid x\right]=P(A \mid x)
$$

## Linearity

Let $(\Omega, \Im, P)$ be a probability space $a$ let $\forall$ be a sub-6-algebra.
If $I_{1}, Z_{2}, \ldots, I_{n}$ are integrable random vorriables and $c_{1}, c_{2}, \ldots, c_{n}$ are constants

$$
\begin{aligned}
& E\left[C_{1} X_{1}+C_{2} X_{2}+\cdots+C_{n} X_{n} \mid \Delta\right] \\
= & C_{1} E\left[X_{1} \mid \Delta\right]+C_{2} E\left[X_{2} \mid \Delta\right]+\cdots+C_{n} E\left[X_{n} \mid \Delta\right]
\end{aligned}
$$

From the partial averaging property
given that $E\left[c_{1} \Sigma_{1}+c_{2} Z_{2}+\cdots+c_{n} Z_{n}|\Delta|\right]$ is $A$ measurable and for $A \in \mathcal{A}$,

$$
\begin{aligned}
\int_{A} E & {\left[C_{1} X_{1}+C_{2} Z_{2}+\cdots+C_{n} Z_{n} \mid \Delta\right] d P } \\
= & \int_{A}\left(C_{1} Z_{1}+C_{2} Z_{2}+\cdots+C_{n} Z_{n}\right) d P \\
= & C_{1} \int_{A} I_{1} d P+C_{2} \int_{A} I_{2} d P+\cdots+C_{n} \int_{A} Z_{n} d P \\
= & C_{1} \int_{A} E\left[X_{1} \mid \Delta\right] d P+C_{2} \int_{A} E\left[X_{2} \mid \mathcal{A}\right] d P \\
& +\cdots+C_{n} \int_{A} E\left[Z_{n} \mid \mathcal{D}\right] d P
\end{aligned}
$$

Thus the desired result is obtained

$$
\begin{aligned}
& \left.E\left[C_{1} Z_{1}+C_{2} Z_{2}+\cdots+C_{n} Z_{n} \mid \Delta\right]\right] \\
& =C_{1} E\left[X_{1} \mid \Delta\right]+C_{2} E\left[X_{2} \mid \nmid\right]+\cdots+C_{n} E\left[X_{n} \mid(y]\right.
\end{aligned}
$$

## Positionty

Let $(\Omega, 7, P)$ be a probability space and let $\$$ be a sub-o-algebra. If $I$ is an integral random variable
such that $\bar{x} \geq 0$ almost surely then show
\$\$

E[X \mid y] \geqslant 0

\$\$

Let

$$
A=\{\omega \in \Omega: E[X \mid D]<0\}
$$

and assume that $A \in \mathcal{H}$. It follows from the partial averaging property

$$
\int_{A} E[x \mid y] d P=\int_{A} \bar{x} d P
$$

since $X>0$ almost surely

$$
\int_{A} I d P \geqslant 0
$$

But

$$
\int_{A} E[X \mid E] d P<0
$$

since it was assumed that $E[X \mid D]<0$ in the construction of A. To resolve this it must be that $P(A)=0$ which implies that
$E[\bar{X} \mid x] \geqslant 0$.

## Monoticity

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $\ngtr$ be a sub-6-algebra of $\mathcal{F}$. If $\mathbb{X}$ and $\mathcal{I}$ are integrable random variables such that $X \leqslant I$ are integrable random variables such that $\bar{X} \leqslant I$ almost surely then show that

$$
E[X \mid y] \leqslant E[I \mid y]
$$

Since $E[X-I \mid \otimes]$ is 2 measurealole, that is $E[X-I \mid D]$ a real valued function of $\omega \in \Omega$ such that $\omega \in \mathscr{A}$. It follows that for $A \in \mathscr{A}$

$$
\int_{A} E[X-I(\Delta)] d P=\int_{A}(X-I) d P
$$

since $\bar{X} \leqslant I$ it follows that

$$
\int(\bar{x}-\bar{y}) d P \leqslant 0
$$

## Thus

$$
\int E[\bar{X}-\bar{I} \mid \mathcal{D}] d P \leqslant 0
$$

and

$$
E[X-I \mid x] \leqslant 0
$$

From linearity it follows that

$$
E[X \mid \otimes] \leqslant E[I \mid \otimes]
$$

## Computing Expectations by Conditioning

Let $(\Omega, F, P)$ be a probability space and let $\theta$ be a sub-6-atgebra of $\mathcal{F}$. show that

$$
E[E[X \mid \Delta]]=E[X]
$$

From the definition of the partial average, with $A \in \mathcal{H}$

$$
\int_{A} E[X(A)] d P=\int_{A} \bar{X} d P
$$

Next the expectation of the portial awerage must be taken which requires an integral over $\Omega$. To evaluate the integral let,

$$
\mathbb{I}_{A}(\omega)= \begin{cases}1 & \text { if } \omega \in A \\ 0 & \text { otherwise }\end{cases}
$$

By definition $\Pi_{A}(\omega)$ I measurable, then the integrals can be tranformed to integrals $\Omega$.

$$
\int_{\Omega} \mathbb{I}_{A} E[\bar{X} \mid \neq] d P=\int_{\Omega} \mathbb{I}_{A} \bar{X} d P
$$

From the definition of expectation it follows that

$$
\begin{aligned}
& E\left[\mathbb{I}_{A} E[\Phi \mid \mathcal{S}]\right]=\int_{\Omega} \mathbb{I}_{A} E[\bar{X} \mid \mathcal{D}] d P \\
& =\int_{\Omega} \llbracket_{A} \bar{X} d P
\end{aligned}
$$

The desired result is obtained by letting $A=\Omega$ then $I_{A}=1$ for all $\omega$.

$$
E[E[\bar{X} \mid A]]=\int_{\Omega} \bar{I} d P=E[\bar{X}]
$$

## Taking Out what is known

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $\mathcal{A}$ be a sub-o-algebra of $\mathcal{F}$.

If $\bar{X}$ and $I$ are integrable random variables and if $\bar{X}$ is $A$ measurable show that

$$
E[\Phi I \mid \delta]=\bar{X} E[I \mid \infty]
$$

Now

$$
\int_{A} E[X I \mid \theta] d P=\int_{A} \bar{X} I d P
$$

But I is $D$ measureable so it is a constant over the integral and can be taken outside, so

$$
\int_{A} \bar{X} I d P=\underline{X} \int_{A} I d P
$$

$$
\begin{aligned}
& =\bar{X} \int_{A} E[I \mid \mathcal{D}] d P \\
& =\int_{A} X E[I \mid \mathcal{S}] d P
\end{aligned}
$$

Thus

$$
\int_{A} E[\bar{X} I \mid \Delta] d P=\int_{A} X E[I \mid \Delta] d P
$$

but $X E[I \mid A]$ is $A$ measureable since both $\bar{X}$ and $E[I \mid \delta]$ are $t$ measurable and the desired result follows

$$
E[\Phi I(x)]=\bar{X} E[I \mid \Delta]
$$

## Tower Property

Let $(\Omega, F, P)$ be a probability space and let \& be a sub-Galgebra Further if $M$ is a sub-6-algebra and $\bar{X}$ is an integrable random variable, show that

$$
E[E[X \mid \mathcal{H}] \mid \mathcal{H}]=E[X \mid \mathcal{H}]
$$

For an integrable random variable I by definition of Partial Averaging $E[$ I 191$]$ is 91 measurable, so $\bar{y}=E[X 15]$ is also $H$ measurable for $A \in \mathcal{H}$, so

$$
\int_{A} E[E[\bar{X} \mid \otimes]|\xi|] d P=\int_{A} E[X \mid \Delta] d P
$$

Like wise since $A \in \mathcal{H}$ and $M \in D$ it follows that

$$
\int_{A} E[X \mid H] d P=\int_{A} E[\bar{x} \mid y] d P
$$

It follows that

$$
\int_{A} E\left[E[X|(D]| \psi] d P=\int_{A} E[X \mid \psi] d P\right.
$$

By definition $E[E[X, Y]|\psi|]$ and $E\left[X\left[I^{\prime}\right]\right.$ are it measurable, so the desired result follows

$$
E[E[X \mid \otimes]|\mathcal{N}|]=E[X|2|]
$$

## Measurability

Let $(\Omega, 7, P)$ be a probability space and let $\phi$ be a sub-6-algebra of 7 . If a random variable $I$ is $\phi$ measureable show that

$$
E[X \mid D]=X
$$

From the definition, for $\Delta \in D$

$$
\int_{A} E[X \mid S] d P=\int_{A} I d P
$$

If $X$ is $\&$ measurable then

$$
\xi \omega \in \Omega: x(\omega) \leqslant x\} \in \mathcal{H}
$$

for each $x \in \mathbb{R}$.
It follows that for some $x$ in $\mathbb{R}$

$$
A=\{\omega \in \Omega: x(\omega)=x\} \in \mathcal{N}
$$

where both $E[x \mid y]$ and $X(\omega)$ are constant in A. Thus

$$
\begin{aligned}
& E[X \mid A] P(A)=X P(A) \\
\Rightarrow & E[X \mid A]=X
\end{aligned}
$$

Alternatively, consider the discrete expression for con ditional expectation found previously,

$$
\begin{aligned}
E[x \mid y] & =\sum_{\omega \in A} x(\omega) P(\sigma(x) \mid A)(\omega) \\
& =\sum_{\omega \in A} x(\omega) \frac{P(\sigma(x) \cap A)(\omega)}{P(A)}
\end{aligned}
$$

since $X$ is $D$ measureable

$$
A=\{\omega \in \Omega: X(\omega)=X\} \in \mathcal{D}
$$

$x(\omega)=x$ which is constant and

$$
A \in \sigma(x)
$$

50

$$
\sigma(x) \cap A=A
$$

and

$$
P(\sigma(x) \cap A)=P(x)
$$

It follows that

$$
\begin{aligned}
E[x \mid y] & =\frac{x P(\sigma(x) \cap A)}{P(A)} \\
& =x \frac{P(A)}{P(A)} \\
& =x
\end{aligned}
$$

## Measureability of Non-Random Fundions

Let $(\Omega, F, P)$ be a probability space. A non-random function is defined by

$$
\bar{X}(\omega)=c
$$

where $c$ is a constant. That is the value of the function is independent of the event $\omega$.
low a function is defined as I measurable if

$$
\{\omega \in \Omega: \bar{X}(\omega) \leqslant b\} \in \mathcal{F}
$$

for $I(\omega)=c$ if $c \leqslant b$ then

$$
\{\omega \in \Omega: c \leqslant b\}=\Omega
$$

and if $c>b$ then

$$
\{\omega \in \Omega: c \leqslant b\}=\phi
$$

which is the empty set. Thus for $c \in \mathbb{R}$

$$
\mathcal{F}=\{\Phi, \Omega\}
$$

$\mathcal{F}$ is a 6 -algebra since it is closed under complement

$$
\Omega^{c}=\varnothing \quad \phi^{c}=\Omega
$$

It contains the empty set $\phi \in \mathcal{F}$
and $t$ is closed under union.

$$
\Omega \cup \emptyset=\Omega \in \mathcal{F}
$$

It follows that

$$
X(\omega)=c \in \mathbb{R}
$$

is $₹$ measurable for

$$
\mathcal{F}=\{\phi, \Omega\}
$$

## Independence

Let $(\Omega, F, P)$ be a probability space and let $\&$ be a sub-6-abgebra

$$
I_{B}= \begin{cases}1 & \text { if } \omega \in B \\ 0 & \text { otherwise }\end{cases}
$$

If $\mathbb{I}_{B}$ is independent of $\&$ show that

$$
E[X \mid O]=E[X]
$$

Now since $E[X]$ is not random it is $\&$ measurable. To prove the desired result it is sufficient
to show that for $A \in D$

$$
\int_{A} E[\bar{X} \mid \phi] d P=\int_{A} \bar{X} d P=\int_{A} E[X] d P
$$

Now let

$$
\mathbb{1}_{A}= \begin{cases}1 & \text { if } \omega \in \Omega \\ 0 & \text { otherwise }\end{cases}
$$

50

$$
\int_{A} \bar{X} d P=\int_{A} \mathbb{1}_{B} d P=\int_{\Omega} \mathbb{1}_{B} \mathbb{1}_{A} d P
$$

but

$$
\|_{B} \underline{1}_{A}=\underline{1}_{A \cap B}
$$

where

$$
\|_{A \cap B}= \begin{cases}1 & \text { if } \omega \in A \cap B \\ 0 & \text { otherwise }\end{cases}
$$

It follows that

$$
\int_{A} \bar{X} d P=\int_{\Omega} \mathbb{1}_{A \cap B} d P=P(A \cap B)
$$

Since $A \in \mathcal{H}$ and $B$ is indepent of y if follows that $A$ and $B$ are independent

$$
P(A \cap B)=P(A) P(B)
$$

Now

$$
\int_{A} E[\underline{X}] d P=E[\bar{X}] \int_{A} d P=E[X] P(A)
$$

but

$$
\begin{aligned}
& E[X]=E\left[\mathbb{1}_{B}\right]=\int_{\Omega} \mathbb{1}_{B} d P \\
& =\int_{B} d P=P(B)
\end{aligned}
$$

Thus

$$
\int_{A} E[\bar{X}] d P=P(A) P(B)
$$

Bringing things together

$$
\int_{A} I d P=P(A) P(B)=\int_{A} E[X] d P
$$

and the desired result is obtained

$$
\begin{aligned}
\int_{A} E[Z \mid \Delta] d P & =\int_{A} I d P \\
& =\int_{A} E[\nabla] d P
\end{aligned}
$$

finally

$$
E[X \mid y]=E[X]
$$

## Radon-Nikodým Derivative

Let $\Omega$ be a probability space and let $P$ and $Q$ be two measures on $\Omega$. Define the Radon-Nikodym derivative, $z(\omega)$, by

$$
Z(\omega)=\frac{Q(\omega)}{P(\omega)}
$$

where $P(z>0)=1$. Let $E^{P}$ indicate the expectation with respect to measure $P$ and $E^{Q}$ the expectation with respect to $Q$. Show that for any random variable $X$,

$$
\begin{aligned}
& E^{Q}(\bar{X})=E^{P}(\bar{X} Z) \\
& E^{P}(\bar{X})=E^{Q}\left(\frac{\bar{X}}{Z}\right)
\end{aligned}
$$

Now

$$
\begin{aligned}
E^{Q}(\bar{x}) & =\sum_{\omega \in \Omega} \bar{x}(\omega) Q(\omega) \\
& =\sum_{\omega \in \Omega} \bar{x}(\omega) Z(\omega) Q(\omega) \\
& =E^{P}(\bar{x} Z)
\end{aligned}
$$

and

$$
\begin{aligned}
E^{P}(\bar{X}) & =\sum_{\omega \in \Omega} \bar{X}(\omega) P(\omega) \\
& =\sum_{\omega \in \Omega} \bar{X}(\omega) \frac{Q(\omega)}{z(\omega)}
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{\omega \in \Omega} \frac{\bar{X}(\omega)}{Z(\omega)} Q(\omega) \\
& =E^{Q}\left(\frac{X}{Z}\right)
\end{aligned}
$$

## Conditional Expectation for continus Distribution

Here many results proven in the previous section will be derived for the case of continuous rardom variables. It makes some of the concepts more transporent since the addidional baggage of measure theory can be ignored.
For real random variables I and I the conditional probability density for $I$ given $I=y$ is defined by

$$
f_{X \mid Z}(x \mid y)=\frac{f_{X I}(x, y)}{f_{Y}(y)}
$$

where $f_{X I}(x, y)$ is the joint density of $X$ and $I$ and $f_{Y}(y)$ is the marginal density for $I$. It follows that the prabability that I satisfies

$$
a \leq \underline{\bar{x}} \leq b
$$

given that $I=y$ is given by
$P(a \leqslant \Sigma \leqslant b \mid I=y)=\int_{a}^{b} f_{X \mid I}(x \mid y) d x$
The conditional expectation of I given $I=y$

$$
E[z \mid I=y]=\int_{-\infty}^{\infty} x f_{x \mid Y}(x \mid y) d x
$$

Letting

$$
d P(x \mid y)=f_{x \mid y}(x \mid y) d x
$$

gives a definition that looks like that used in the measure theory, namely,

$$
E[Z \mid Z]=\int_{-\infty}^{\infty} x d P(x \mid y)
$$

The following seetions will discuss properties of Conditional expections similar to those discussed previously.

## Computing Expectration by Conditioning

The continous anales for computing expectation by Conditioning discussed in the previous setion can be proven for the continuous case by noting that the conditional expectation is a random function of the variable II.
Consider

$$
\begin{aligned}
& E[E[\bar{X} \mid \bar{Y}]] \\
= & \int_{-\infty}^{\infty} E[\bar{X} \mid \bar{I}=y] f_{Y}(y) d y \\
= & \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x f_{I \mid Y}(x \mid y) f_{Y}(y) d x d y \\
= & \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x f_{I I}(x, y) d y d x
\end{aligned}
$$

$$
=\int_{-\infty}^{\infty} x f_{\bar{x}}(x) d x=E[\bar{x}]
$$

Thus

$$
E[E[\bar{x} \mid \bar{I}]]=E[\bar{x}]
$$

## Conditional Expectation of Constant

Let $I=C$ where $C$ is a constant. It follows that I and I are independent, so

$$
f_{\Sigma I}(x, y)=f_{I}(y) \delta(x-c)
$$

where $\delta(x-c)$ is the Dirac detta function. It follows that

$$
f_{X I Y}(x \mid y)=\frac{f_{X I}(x, y)}{f_{I}(y)}=\delta(x-c)
$$

thus

$$
E[c \mid I]=\int_{-\infty}^{\infty} x \delta(x-c) d x
$$

$$
\Rightarrow E[C \mid Y]=C
$$

## Linearty

Linearity of Conditional expections follow from linearity of integration, consider

$$
\begin{aligned}
& E\left[a \bar{X}+b Z_{1} \mid I\right] \\
& f_{X Z_{1} I}(x, z \mid y)=\frac{f_{X I Z_{2}}(x, z, y)}{f_{I}(y)} \\
& \delta 0 \\
& E\left[a \bar{X}+b Z_{1} \mid I\right] \\
& =\frac{1}{f_{I}(y)} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty}(a x+b y) f_{X I Z_{1}}(x, z, y) d x d z \\
& =\frac{1}{f_{I}(y)}\left\{a \int_{-\infty}^{\infty} x f_{X I}(x, y) d x\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.+b \int_{-\infty}^{\infty} z f_{z, I}(z, y) d z\right\} \\
= & a \int_{-\infty}^{\infty} x f_{I \mid I}(x \mid y) d x+b \int_{-\infty}^{\infty} y f_{z, I I}(z \mid y) d z \\
= & a E[X \mid I]+b E[z \mid y]
\end{aligned}
$$

Thus conditional expectation is linear

$$
\begin{aligned}
& E\left[a \bar{X}+b Z_{1} \mid I\right]= \\
& a E[X \mid I]+b E[Z \mid I]
\end{aligned}
$$

## Positivity

show that

$$
E[\bar{X} \mid I] \geqslant 0
$$

if $\bar{x} \geqslant 0$
since $\bar{x} \geqslant 0$ it follows that

$$
E[x \mid y]=\int_{0}^{\infty} x f_{x \mid I}(x \mid y) d x
$$

since $x \geqslant 0$ and $f_{\bar{I} \mid \mathcal{Y}}(x \mid y) \geqslant 0$ it follows that

$$
E[\bar{x} \mid \mathbb{I}] \geqslant 0
$$

## Independence

If $X$ are independent $I$ then

$$
E[X \mid Y]=E[X]
$$

since $I$ and $I$ are independent

$$
\begin{aligned}
& f_{X \mid Y}(x \mid y)=\frac{f_{X Y}(x, y)}{f_{Y}(y)} \\
= & \frac{f_{I}(x) f_{Y}(y)}{f_{Y}(y)} \\
= & f_{X}(x)
\end{aligned}
$$

$$
E[X \mid I]=\int_{-\infty}^{\infty} x f_{X}(x) d x=E[X]
$$

thus

$$
E[X \mid Y]=E[X]
$$

## Tower Property

The continuous version of the Tower Property from measure theory is given by

$$
E[E[\bar{X} \mid \bar{Y}, Z] \mid Y]=E[\bar{X} \mid \bar{Y}]
$$

Now $E[X \mid I, Z]$ is a random function of the random variables $I$ and 2 . It follows that

$$
\begin{aligned}
& E[E[X \mid I, Z] \mid I] \\
& =\int_{-\infty}^{\infty} E[X \mid I, Z] f_{z \mid I}(Z \mid y) d z
\end{aligned}
$$

$$
\begin{aligned}
& =\int_{-\infty}^{\infty}\left\{\int_{-\infty}^{\infty} x f_{\bar{x} \mid I z_{1}}(x \mid y, z) d x\right\} \\
& f_{z_{1} \bar{I}}(z \mid y) d z \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x f_{\bar{x} \mid I z_{1}}(x \mid y, z) f_{z_{1} \bar{I}}(z \mid y) d x d z
\end{aligned}
$$

Now

$$
\begin{aligned}
& f_{\overline{X \mid I} Z_{1}}(x \mid y, z) f_{Z_{1} I}(z \mid y) \\
& =\frac{f_{\overline{X I} Z_{2}}(x, y, z) f_{Z_{I} I}(z, y)}{f_{Z_{I} I}(z, y) f_{I}(y)} \\
& =\frac{f_{\overline{X I} Z_{I}}(x, y, z)}{f_{I}(y)}
\end{aligned}
$$

It follows that
$E[E[X \mid I, Z] \mid Y]$
$=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x \frac{f_{X I Z}(x, y, z)}{f_{I}(y)} d z d x$
$=\int_{-\infty}^{\infty} x \frac{f_{X Y}(x, y)}{f_{Y}(y)} d x$
$=\int_{-\infty}^{\infty} x f_{x \mid I}(x \mid y) d x$
$=E[X \mid Y]$
thus

$$
E[E[\underline{X} \mid I, z] \mid I]=E[\underline{X} \mid I]
$$

## Probability Theory Examples

## Example 1: Tossing Two Coins

A probability space has three components, $(\Omega, \mathcal{F}, P)$, respectively the sample space, the event space and the probability function. The following will provole examples for each component by considering the toss of two coins.

## Sample Space

The sample space is the set of all possible outcomes of an experiment. For the two coin toss experiment there are $a^{2}$ possible outcomes. Denote the 2 possible outcomes of a coin toss by

$$
\begin{aligned}
& H=\text { outcome is heads } \\
& T=\text { outcome is tails }
\end{aligned}
$$

It follows that the sample space is given by

$$
\Omega=\{H T, H H, T H, T T\}
$$

## Event space

An event is a subset of the sample space $\Omega$. Examples of events are

1. $\{H T, T T\}$, the secont toss is tails.
2. $\{H T, T H, T T\}$, at least one toss is tails

The event space is defined as an 6 -algebra. A 6 -algebra has the following properties

1) $\phi \in \mathcal{F}$ (The event space must contain the empty set)
2) If an event $A \in \mathcal{F}$ then $A^{c} \in \mathcal{F}$ (If $f$ contains an event $A$ than
it must also contain the compliment of A)
3) If $\mathcal{F}$ contains a countable number of sets $A_{1}, A_{2}, \ldots \in \mathcal{F}$ then $\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{F}$ ( $\mathcal{F}$ is closed under courtably infinite whions)
(4) Now (1) and (2) imply that

$$
\Omega^{c}=\varnothing
$$

then

$$
\Omega \in \mathcal{F}
$$

(5) Recall De Morgan's Laus
a) $\left(\bigcup_{i=1}^{\infty} A_{i}\right)^{c}=\bigcap_{i=1}^{\infty} A_{i}^{c}$
b) $\left(\bigcap_{i=1}^{\infty} A_{i}\right)^{C}=\bigcup_{i=1}^{\infty} A_{i}^{c}$

From (2) and (3) since

$$
\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{J}
$$

and $A_{i}^{C} \in \mathcal{F}$

It follows that

$$
\bigcup_{i=1}^{\infty} A_{i}^{c} \in \mathcal{F}
$$

From the (b) version of De Morgan's law it follows that

$$
\left(\bigcap_{i=1}^{\infty} A_{i}\right)^{c} \in \mathcal{F}
$$

and applying (2) again gives

$$
\bigcap_{i=1}^{\infty} A_{i} \in \mathcal{F}
$$

Thus $f$ is also closed under countable intersections.

These assumptions are sufficient to ensure the existance of a probability function on $\mathcal{F}$. This will be seen in the following section.

As an example the minimal event space is

$$
\mathcal{F}=\{\phi, \Omega\}
$$

The evont space that contains all possible events from $\Omega$ is the power set of $\Omega$

$$
\mathcal{F}=2^{\Omega}
$$

Consider the two coin toss example where

$$
\Omega=\{H T, H H, T H, T T\}
$$

and the event of throwing tails for the second toss.

$$
A=\{H T, T T\}
$$

It follows that the event space is given by

$$
F=\{\phi, \Omega,\{H T, T T\},\{H H, T H\}\}
$$

$\mathcal{F}$ is also closed under union

$$
\{H T, T T\} \cup\{H H, T H\}=\Omega
$$

$$
\begin{aligned}
& \Omega \cup \varnothing=\Omega \\
& \{H T, T T\} \cup \Omega=\Omega \\
& \{H H, T H\} \cup \Omega=\Omega \\
& \{H T, T T\} \cup \varnothing=\{H T, T T\} \\
& \{H H, T H\} \cup \varnothing=\{H H, T H\}
\end{aligned}
$$

## Probabillty Function

A probability function assigns an probability value to each element of $\mathcal{F}$. The probability value is a real number on the closed interoal [0,1]. Denole the probability function by $P$ which must satisfy the following properties.

1) $P(A) \geqslant 0$ for all $A \in \mathcal{F}$
2) $P(\Omega)=1$
3) For $A_{1}, A_{2}, \ldots \in \mathcal{F}$ where $A_{i} \cap A_{j}=\varnothing$ for $i \neq j$

$$
P\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)
$$

From (1) and (2) it follows that for $A \in \mathcal{F}$

$$
0 \leqslant P(A) \leqslant 1
$$

and from (2) and (3) using

$$
\begin{aligned}
& A \cap A^{C}=\varnothing \\
& A \cup A^{C}=\Omega
\end{aligned}
$$

it follows that

$$
\begin{aligned}
& P\left(A \cup A^{C}\right)=P(\Omega)=1 \\
& \Rightarrow P(A)+P\left(A^{C}\right)=1
\end{aligned}
$$

If $A=\Omega$ then

$$
\begin{aligned}
& P(\Omega)+P(\phi)=1 \\
& \Rightarrow P(\phi)=0
\end{aligned}
$$

Consider two events $A \in \mathcal{F}$ and $B \in \mathcal{F}$. It is straight forward to sow that

$$
\begin{gathered}
A \cup B=A \cup(B \backslash A) \\
B \cap A^{C}=B \backslash A
\end{gathered}
$$

and

$$
B=(B \cap A) \cup\left(B \cap A^{C}\right)
$$

Now

$$
(B \cap A) \cap\left(B \cap A^{C}\right)=\varnothing
$$

it follows that

$$
\begin{aligned}
& P(B)=P(B \cap A)+P\left(B \cap A^{c}\right) \\
\Rightarrow & P(B \cap A)=P(B)-P\left(B \cap A^{c}\right)
\end{aligned}
$$

Now using $A \cap(B \backslash A)=\varnothing$ it follows that

$$
P(A \cup B)=P(A)+P(A \backslash B)
$$

but

$$
B \cap A^{C}=A \backslash B
$$

so

$$
P(A \cup B)=P(A)+P\left(B \cap A^{C}\right)
$$

using the previous result
to eliminate $P\left(B \cap A^{c}\right)$ gives

$$
P(A \cup B)=P(A)+P(B)-P(B \cap A)
$$

Since $P(B \cap A) \geqslant 0$ it follows that

$$
P(A \cup B) \leqslant P(A)+P(B)
$$

This result is valid for an corbitrary number of events and is called Boole's Inequality

$$
P\left(\bigcup_{i=1}^{\infty} A_{i}\right) \leqslant \sum_{i=1}^{\infty} P\left(A_{i}\right)
$$

If $A \subseteq B$ then

$$
A=B U(A \backslash B)
$$

where

$$
B \cap(A \backslash B)=\varnothing
$$

It follows that

$$
P(A)=P(B)+P(A \backslash B)
$$

but $P(A \backslash B) \geqslant 0$ thus

$$
P(A) \geqslant P(B)
$$

Consider a partition of $A$

$$
A=\bigcup_{i=1}^{\infty} A \cap C_{i}
$$

where for $i \neq j$

$$
\left(A \cap C_{j}\right) \cap\left(A \cap C_{i}\right)=\varnothing
$$

It follows that

$$
P(A)=\sum_{i=1}^{\infty} P\left(A \cap C_{i}\right)
$$

## Probability Calculation for Two Coin Toss

Consider the two coin toss example. If the com is fair,

$$
P(H)=P(T)=1 / 2
$$

If the coin tosses are assumed to be independent

$$
P(H T)=P(T H)=P(H H)=P(T T)=1 / 4
$$

Also the fundamental events $H T, T H, H H$ and $T T$ are disjoint so that

$$
\begin{aligned}
& P(\Omega)=P(\{H T, T H, H H, T T\}) \\
& =P(H T)+P(T H)+P(H H)+P(T T) \\
& =\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}=1
\end{aligned}
$$

Furthur consider the event space previously discussed, which models throwing tails on the second toss,

$$
\mathcal{F}=\{\phi, \Omega,\{H T, T T\},\{H H, T H\}\}
$$

The probabilities are

$$
\begin{array}{ll}
P(\phi)=0 & P(\{H T, T T\})=1 / 2 \\
P(\Omega)=1 & P(\{H H, T H\})=1 / 2
\end{array}
$$

These probability definitions are
sufficient to compute the probability of the events of tossing tails on the second toss and not fossing tails on the second toss. For the first event of throwing tails on the second toss

$$
P(\{H T, T T \xi)=1 / 2
$$

and of not tossing tails on the second toss

$$
\begin{aligned}
P(\{H, T H\}) & =P(\Omega)-P(\{H T, T T\}) \\
& =1-1 / 2 \\
& =1 / 2
\end{aligned}
$$

## Random variables

A random variable is a function from the event space of to the real numbers.
consider the two con toss example, let

$$
t_{i}= \begin{cases}1 & \text { if } H \text { on ith toss } \\ 2 & \text { if } T \text { on ith toss }\end{cases}
$$

where $i=1,2$
A possible random variable is

$$
x=t_{1}+t_{2}
$$

The mapping from $\Omega$ to $\mathbb{R}$ is giving

| $\Omega$ | $X$ |
| :---: | :---: |
| $H H$ | 2 |
| $H T$ | 3 |
| $T H$ | 3 |
| $T T$ | 4 |

It follows that

$$
\begin{aligned}
& P(x=2)=1 / 4 \\
& P(x=3)=1 / 2 \\
& P(x=4)=1 / 2
\end{aligned}
$$

and for $x \neq 2,3$ or $4 \quad P(x)=0$

Another example let

$$
x=\text { number of Heads }
$$

| $\Omega$ | $x$ |
| :---: | :---: |
| $H H$ | 2 |
| $H T$ | 1 |
| $T H$ | 1 |
| $T T$ | 0 |

It follows that

$$
\begin{aligned}
& P(x=0)=1 / 4 \\
& P(x=1)=1 / 2 \\
& P(x=2)=14
\end{aligned}
$$

and for $x \neq 0,1,2 \quad P(x)=0$
F Measurable Random Variables
Consider the event previously discussed where the second toss is tails

$$
\mathcal{F}=\{\phi, \Omega,\{H T, T T\},\{H H, T H\}\}
$$

where

$$
\Omega=\{H T, T H, H H, T T\}
$$

Define the random variable

$$
x= \begin{cases}1 & \text { if second toss is tails } \\ 0 & \text { if second toss is heads }\end{cases}
$$

It follows that $x$ is $\xi$ measurable since,

$$
\begin{aligned}
& \{\omega \in X(\omega)=1\} \in \mathcal{F} \\
& \{\omega \in X(\omega)=0\} \in \mathcal{F}
\end{aligned}
$$

## Independence of Euents

consider the probability space $(\Omega, \Im, P)$ composed of the sample space $\Omega$, event space $\mathcal{F}$ and probability function P. Consder the events $A \in \mathcal{F}$ and $B \in \mathcal{F}$. If $A$ and $B$ are independent
the joint distribution $A$ and $B$ has the form

$$
P(A \cap B)=P(A) P(B)
$$

Consider the two corn toss example with sample space

$$
\Omega=\{H T, H H, T H, T T\}
$$

and consider the events

$$
A=\{H T, H H\} \quad B=\{H T, T T\} \quad C=\{H T\}
$$

where $A$ is the event of tossing a heads on the first toss, $B$ the event of tossing tails on the second toss and $c$ the event of tossing a heads followed by tails. Now recall that

$$
P(H T)=P(H H)=P(T H)=P(T T)=1 / 4
$$

So

$$
P(A)=1 / 2 \quad P(B)=1 / 2 \quad P(C)=1 / 4
$$

first consider

$$
A \cap B=\{H T\}
$$

It follows that

$$
P(A \cap B)=P(\{H T\})=1 / 4
$$

but

$$
P(A) P(B)=(1 / 2)(1 / 2)=1 / 4
$$

thus

$$
P(A \cap B)=P(A) P(B)
$$

it follows that $A$ and $B$ are indeperdent.
Now consider

$$
B \cap C=\{H T\}
$$

80

$$
P(B \cap C)=P(\{H T \xi)=1 / 4
$$

But

$$
P(B) P(C)=(1 / 2)(1 / 4)=1 / 8
$$

thus

$$
P(B \cap C) \neq P(B) P(C)
$$

so $B$ and $C$ are not independent

## Conditional Probability

Consider a probibility space $(\Omega, \mathcal{F}, P)$ and $d$ two events $A$ and $B$ where $A \in \mathcal{F}$ and $B \in \mathcal{F}$. Then the conditional probability that the event $A$ occurs given that the event $B$ has occured is defined by

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

If $P(A)$ is interpretted as the probability that the event $A$ occurs then $P(A \mid B)$ is the probability that the event occurs if it is known that event $B$ has occurred.

Intuition about $P(A \mid B)$ can be developed by considering the following cases.

1) If $A$ and $B$ are disjoint,

$$
A \cap B=\varnothing
$$

then

$$
P(A \cap B)=P(\phi)=0
$$

50

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}=0
$$

2) If $A C B$ then,

$$
A \cap B=A
$$

then

$$
P(A \cap B)=P(A)
$$

50

$$
P(A \mid B)=\frac{P(A)}{P(B)}<1
$$

3) If $B \subset A$ then,

$$
A \cap B=B
$$

then

$$
P(A \cap B)=P(B)
$$

50

$$
P(A \mid B)=\frac{P(B)}{P(B)}=1
$$

4) If $A$ and $B$ are independent

$$
P(A \cap B)=P(A) P(B)
$$

then

$$
\begin{aligned}
P(A \mid B) & =\frac{P(A \cap B)}{P(B)} \\
& =P(A)
\end{aligned}
$$

Consider the following events from the two coin toss expiriment. The first event, $A$, represents the event that the first toss is heads. The second event, $B$, represents the event that the second toss is tails and the final event, $c$, represents the event that the first toss is heads and the second toss is tails,
$A=\{H T, H H\} \quad B=\{H T, T T\} \quad C=\{H T\}$
Now

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

Proviously it was shown that $A$ and $B$ are independent so

$$
P(A \cap B)=P(A) P(B)
$$

it follows that

$$
\begin{aligned}
P(A \mid B) & =P(A) P(B) \\
& =P(A) \\
& =1 / 2
\end{aligned}
$$

Next consider $P(C \mid B)$ in light of the previous result that $B$ and $C$ are not independent, so

$$
P(C \mid B)=\frac{P(C \cap B)}{P(B)}
$$

$$
\begin{aligned}
& =\frac{P(\{H T\})}{P(\{H T, T T\})} \\
& =\frac{1 / 4}{1 / 2}=1 / 2
\end{aligned}
$$

Similarly

$$
\begin{aligned}
P(B \mid C) & =\frac{P(C \cap B)}{P(C)} \\
& =\frac{P(C)}{P(C)} \\
& =1
\end{aligned}
$$

Both of these results are intuitive. For the first $B$ is given and $C \in B$ and one of the two elements in $B$ gioling $P(C \mid B)=1 / 2$. Likewse, if $C$ is given then since $C \in B$ event $B$ has also occured thus $P(B \mid C)=1$.

Theorem Let ( $\Omega, F, P$ ) be a probability space and assume that $B \in \mathcal{F}$ is and event with $P(B)>0$. The function $Q: F \rightarrow[0,1]$ defined by

$$
Q(A)=P(A \mid B)
$$

is a probability measure on $(\Omega, \hat{f})$ Recall that a function is a probability measure if
(1) $P(\Omega)=\varnothing=1$
2) If $A_{i} \cap A_{j}=\varnothing$ for $i \neq j$ then $P\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)$
To prove that $Q$ is a probability measure it must be shown that 1 and 2 are satisfied.
Now for (1)

$$
Q(\Omega)=P(\Omega \mid A)=\frac{P(\Omega \cap A)}{P(A)}
$$

$$
=\frac{P(A)}{P(A)}=1
$$

thus condition 1 is satisfied. To prove condition 2 let $A_{1}, A_{2}, \ldots \in F$ where $A_{i} \cap A_{j}=\phi$ for $i \neq j$.

$$
\begin{aligned}
Q\left(\bigcup_{i=1}^{\infty} A_{i}\right) & =\frac{P\left(\bigcup_{i=1}^{\infty} A_{i} \mid B\right)}{P(B)} \\
& =\frac{1}{P(B)} P\left[\left(\bigcup_{i=1}^{\infty} A_{i}\right) \cap B\right]
\end{aligned}
$$

but

$$
\left(\bigcup_{i=1}^{\infty} A_{i}\right) \cap B=\bigcup_{i=1}^{\infty}\left(A_{i} \cap B\right)
$$

and

$$
(A i \cap B) \cap\left(A_{j} \cap B\right)=\varnothing \text { for } i \neq j
$$

50

$$
\begin{aligned}
Q\left(\bigcup_{i=1}^{\infty} A_{i}\right) & =\frac{1}{P(B)} P\left[\left(\bigcup_{i=1}^{\infty} A_{i}\right) \cap B\right] \\
& =\frac{1}{P(B)} P\left[\bigcup_{i=1}^{\infty}\left(A_{i} \cap B\right)\right]
\end{aligned}
$$

$$
=\frac{1}{P(B)} \sum_{i=1}^{\infty} P\left(A_{i} \cap B\right)
$$

But

$$
\begin{aligned}
Q\left(A_{i}\right) & =P\left(A_{i} \mid B\right) \\
& =P\left(\frac{A_{i} \cap B}{P(B)}\right. \\
\Rightarrow P\left(A_{i} \cap B\right) & =P(B) Q\left(A_{i}\right)
\end{aligned}
$$

thus

$$
\begin{aligned}
Q\left(\bigcup_{i=1}^{\infty} A_{i}\right) & =\frac{1}{P(B)} \sum_{i=1}^{\infty} P(B) Q\left(A_{i}\right) \\
& =\sum_{i=1}^{\infty} Q\left(A_{i}\right)
\end{aligned}
$$

Thus $Q(A)$ is a probability measure that is referred to as a conditional measure given $B$.

Theorem Let $(\Omega, \mathcal{F}, P)$ be a probability space. A collection of events $\left\{E_{n}\right\}$ is called a
partition of $\Omega$ if $P\left(E_{n}\right)>0$ for all $n$ and the $\left\{E_{n}\right\}$ are pairwise disjoint, $E_{n} \cap E_{m}=\varnothing$ for $m \neq n$ and

$$
U_{n} E_{n}=\Omega
$$

The partition theorem states that given a partition $\left\{E_{n}\right\}$ of $\Omega$ and if $A \in \mathcal{F}$ then

$$
P(A)=\sum_{n} P\left(A \mid E_{n}\right) P\left(E_{n}\right)
$$

Proof: Now

$$
\begin{aligned}
A=A \cap \Omega & =A \cap\left(\bigcup_{n} E_{n}\right) \\
& =U\left(A \cap E_{n}\right)
\end{aligned}
$$

The desired result ${ }^{n}$ is obtained

$$
\begin{aligned}
P(A) & =P\left[\bigcup_{n}\left(A \cap E_{n}\right)\right] \\
& =\sum_{n} P\left(A \cap E_{n}\right) \\
& =\sum_{n} P\left(A \mid E_{n}\right) P\left(E_{n}\right)
\end{aligned}
$$

## Bayes Theorem

Consider a probability space $(\Omega, F, P)$ and two events $A \in \mathcal{F}$ and $B \in \mathcal{F}$. Now set intersection commutes

$$
A \cap B=B \cap A
$$

50

$$
\begin{aligned}
P(A \cap B) & =P(B \cap A) \\
\Rightarrow \quad P(A \mid B) P(B) & =P(B \mid A) P(A)
\end{aligned}
$$

if $P(A)>0$

$$
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A)}
$$

Now $\left\{B, B^{C}\right\}$ is a partition of -2 since

$$
B \cup B^{C}=\Omega
$$

it follows that

$$
P(A)=P(A \mid B) P(B)+P\left(A \mid B^{C}\right) P\left(B^{C}\right)
$$

So

$$
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A \mid B) P(B)+P\left(A \mid B^{C}\right) P(B C)}
$$

Bayes theoreom is obtaind by assuming a partition $\left\{E_{n}\right\}$

$$
P\left(E_{j} \mid A\right)=\frac{P\left(A \mid E_{j}\right) P\left(E_{j}\right)}{\sum_{n} P\left(A \mid E_{n}\right) P\left(E_{n}\right)}
$$

Intuitively Bayes theorem states that for a given event $A \in \mathcal{F}$ and a partition $\left\{E_{n}\right\}$ of $\Omega P\left(E_{j} \mid A\right)$ is portion of $P\left(A \mid E_{j}\right) P\left(E_{j}\right)$ relative to $P(A)$.

## Conditional Probability Example: Monte Hall Problem

The Monte Hall problem is a classic conditional probability problem with a nonintuitive result. It is based on an event that occurs in the 1970's game
show "Let's Make a Deal". Morte Hall is the host of the show. The problem can be stated as follows

1) A prize is placed behind one of three doors.
2) The participant in the game chooses door 1 in an attempt win the prize
3) Monte Hall opens door 2 and reveals that there is no prize.
4) He offers the participant the choice to change his choice to door 3.
should the participant take the offer?
A conditional probability analysis will show that the participant should take the offer.
The information in the problem
can be summarized as follows. In step 1 when the particupale makes the choice of door 1 there were 3 choices so the probability of winning the prize is $1 / 3$. Then in step 3 Mante Hall reveals that the prize is not behind door 2. How does this change the probability of which door is hiding the prize?
When monte Hall revealled that the prize is not behond door 2 there are two possibilities.
5) The prize is behind door 1
6) The prize is behind door 3

For these cases what is the probability of monte Hall opening door 2? If the probability is not the same the participant should make the chorce for which the choice is most
probable. If Monte Hall's choice of door 2 is more probable if the prize is behind door I the participant should not change his choice. If his choice of door 2 has a greater probability if the prize is behind door 3 the participant should changl his choice.
To analze the problem define two rardom varibles.

$$
\begin{aligned}
D= & \text { The door hiding the } \\
& \text { prize. } \\
M= & \text { Morite Hall's choice of } \\
& \text { door at step } 3 \text { in the } \\
& \text { game }
\end{aligned}
$$

It is assumed that the participant choose door 1. The desired probabilities are

$$
P(D=1 \mid M=2) \quad P(D=3 \mid M=2)
$$

since these are the only two
outcomes it must be that

$$
P(D=1(M=2)+P(D=3 \mid M=2)=1
$$

From Baye's Theorem

$$
P(D=1 \mid M=2)=\frac{P(M=2 \mid D=1) P(D=1)}{P(M=2)}
$$

and

$$
P(D=3 \mid M=2)=\frac{P(M=2 \mid D=3) P(D=3)}{P(M=2)}
$$

where

$$
\begin{aligned}
P(M=2)= & P(M=2 \mid D=3) P(D=3) \\
& +P(M=2 \mid D=1) P(D=1)
\end{aligned}
$$

Now $P(D=3)$ and $P(D=1)$ are the prior probabilities that the prize is behind door 3 and door 1 before Monte Hall reveals door 2 does not hide the prize. So,

$$
P(D=3)=P(D=1)=1 / 3
$$

$P(M=2 \mid D=1)$ and $P(M=2 \mid D=3)$ are the conditional probabilities the monte Hall choose door 2 given that the prize is behind doors 1 and 3 respectively.
Now the participant choose door 1 so $D=1$ is the case where the participant wins. It follows that $M=2$ and $M=3$ are the only chocces for Monte Hall it follows that
$P(M=2 \mid D=1)=P(M=3 \mid D=1)=1 / 2$
For $D=3$ Monte Hall must choose door 2 since the participant choose door 1. This is the case where the participant looses. since there is a single choice it follows that

$$
P(M=2 \mid D=3)=1
$$

To summarize

$$
\begin{gathered}
P(D=3)=P(D=1)=1 / 3 \\
P(M=2 \mid D=1)=P(M=3 \mid D=1)=1 / 2 \\
P(M=2 \mid D=3)=1
\end{gathered}
$$

Plugging these colues into the expressions obtained using Baye's theorem gives

$$
\begin{aligned}
& P(M=2)=P(M=2 \mid D=3) P(D=3) \\
& +P(M=2 \mid D=1) P(D=1) \\
& =(1)(1 / 3)+(1 / 2)(1 / 3) \\
& =1 / 3+1 / 6=1 / 2 \\
& P(D=1 \mid M=2)=\frac{P(M=2 \mid D=1) P(D=1)}{P(M=2)} \\
& =\frac{(1 / 2)(1 / 3)}{(1 / 2)}=1 / 3
\end{aligned}
$$

$$
\begin{aligned}
P(D=3 \mid M=2) & =\frac{P(M=2 \mid D=3) P(D=3)}{P(M=2)} \\
& =\frac{(1)(1 / 3)}{1 / 2}=\frac{2}{3}
\end{aligned}
$$

Thus

$$
P(D=3 \mid M=2)>P(D=1 \mid M=2)
$$

It follows that the participant should change his choice to door 3.

## Example 2: Throwing a Single Dice

Let $(\Omega, F, P)$ be a probability space where. The event space is given by all possible outcomes for throwing a single dice

$$
\Omega=\{1,2,3,4,5,6\}
$$

It is also assumed the each throw is independent of the previous throws. $\mathcal{F}$ is the power set of $\Omega$

$$
F=2^{\Omega}
$$

Let

$$
P(\{\omega\})=1 / 6 \quad \omega=1,2, \ldots, 6
$$

and define two events that are subsets of $\Omega$ by

$$
A_{1}=\{1,2,3\} \quad A_{2}=\{2,5\}
$$

Show that $A_{1}$ and $A_{2}$ are independent.

To show independence it must shown that

$$
P\left(A_{1} \cap A_{2}\right)=P\left(A_{1}\right) P\left(A_{2}\right)
$$

Now
so

$$
\begin{gathered}
A_{1} \cap A_{2}=\{2\} \\
P\left(A_{1} \cap A_{2}\right)=P(\{2\})=1 / C_{e}
\end{gathered}
$$

Now $P\left(A_{1}\right)$ is just the sum of of the base probabilities

$$
\begin{aligned}
P\left(A_{1}\right) & =P(1)+P(2)+P(3) \\
& =\frac{1}{6}+\frac{1}{6}+\frac{1}{6} \\
& =\frac{1}{2}
\end{aligned}
$$

similarly for $A_{2}$

$$
\begin{aligned}
P\left(A_{2}\right) & =P(2)+P(5) \\
& =\frac{1}{6}+\frac{1}{6} \\
& =\frac{1}{3}
\end{aligned}
$$

Thus

$$
P\left(A_{1}\right) P\left(A_{2}\right)=(1 / 2)(1 / 3)=1 / 6
$$

and the desired result is obtained

$$
P\left(A_{1} \cap A_{2}\right)=P\left(A_{1}\right) P\left(A_{2}\right)
$$

so $A_{1}$ and $A_{2}$ are independent.

## Borel Sets

Borel sets proude a set theory decription of open and closed intervals on the continuous real number line and are used to constuct probability spaces defined on the real number line.

## Open and Closed Intervals

An example of an open interval is defined by the inequality
$0<x<1$ for $x \in \mathbb{R}$
Here $x$ is any real number greater than but not equal to 0 and less than but not equal to 1. An open interval does not include the end poils in the interval. Open intervals are denoted by
$(0,1)$
A more rigorous defintion of an open interval it that if $x \in(0,1)$ then there exists some $\epsilon>0$ such that the interval $(x-\epsilon, x+\epsilon) \subset(0,1)$. This is a cosequence of the end points not belonging to the interval.

An example of a closed interval $I^{s}$ defined by the inequality $0 \leqslant x \leqslant 1$ for $x \in \mathbb{R}$
tere $x$ is any real number greater tran or equal to 0 or less than or equal to: A closed interval includes the end points in the interval. closed intervals are denoted by

$$
[0,1]
$$

A more rigorous definition of a closed interval is that if an interval $I$ is closed the compliment
of $I$, denoted by $I^{C}$, is open. Also that the interval can be seen to not be onen by considering the end points of the interval.
if $x=0$ then $(-\epsilon, \epsilon) \notin[0,1]$ and if $x=1$ then $(1-t, 1+\epsilon) \notin[0,1]$.
Examples of closed intervals are $[a, \infty)$ and $(-\infty, b]$ since the compliments are open $(-\infty, a)$ and $(b, \infty)$ and $\{a\}$ is closed since its compliment $(-\infty, a) \cup(a, \infty)$ is open.
Itervals can be half open and closed

$$
\begin{aligned}
& 0<x \leqslant 1 \quad \Rightarrow \quad(0,1] \\
& 0 \leqslant x<1 \quad \Rightarrow \quad[0,1)
\end{aligned}
$$

Intervals of this type are neither open or closed. This can be seen for $(0,1]$ since $(1-\epsilon, 1+\epsilon) \nless(0,1]$ and the compliment $\in \infty, 0] \cup(1, \infty)$.

## Union and Intersection of open and Closed Intervals

Let $A_{i}$ be an epen interval. so that if $x \in A_{i}$ then $(x-\epsilon, x+\epsilon) \subset A_{i}$ for some $\epsilon>0$. Snow that $\bigcup_{i=1}^{\infty} A_{i}$ is open and $\bigcap_{i=1} A_{i}$ is epen.

* For the first proof since $A_{i}$ is open for any value of $i$ there exists on $x$ such that

$$
(x-\epsilon, x+\epsilon) \subset A_{i}
$$

it follows that

$$
(x-t, x+\epsilon) \subset \bigcup_{i=1}^{\Delta} A_{i}
$$

Thus $\bigcup_{i=1}^{\infty} A_{i}$ is open since $x$ is arbitrary.

* Next consider $\bigcap_{i=1}^{n} A_{i}$. Let $x \in \bigcap_{i=1}^{n} A_{i}$ It follows that

$$
x \in A_{i} \forall i=1,2, \ldots, n
$$

but each $A_{i}$ is open so there is some $\epsilon>0$ such that

$$
(x-\epsilon, x+\epsilon) \subset A_{i} \quad \forall i=1,2, \ldots, n
$$

It follows that

$$
(x-\epsilon, x+\epsilon) \subset \bigcap_{i=1}^{n} A_{i}
$$

thus $\bigcap_{i=1}^{n} A_{i}$ is open.

* Next show that $\cap A_{i}$ is not necessarily open.
This result will be proven by constructing an example where $\bigcap_{i=1} A_{i}$ is closed.
consider the interoals

$$
\left(-\frac{1}{i}, \frac{1}{i}\right) \text { where } i=1,2,3, \ldots
$$

and the infinite intersection

$$
\bigcap_{i=1}^{\infty}\left(-\frac{1}{i}, \frac{1}{i}\right)
$$

show that

$$
\bigcap_{i=1}^{\infty}\left(\frac{-1}{i}, \frac{1}{i}\right)=\{0\}
$$

This intersetion produces the sequence
$(-1,1) \supset(-1 / 2,1 / 2) \supset(-1 / 3,1 / 3) \supset \cdots \supset\left(-\frac{1}{i}, \frac{1}{i}\right)$
where each subseguent interval is a subset of the previous interval. A sequence of this type is called monotonic.

For each interval the following inequality is satisfied

$$
-1 / i<x<1 / i
$$

Below intervals are shown graphically
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-164.jpg?height=664&width=1099&top_left_y=294&top_left_x=181)

To prove the desired result it must be shown that

$$
\bigcap_{i=1}^{\infty}\left(\frac{-1}{i}, \frac{1}{i}\right) \supset\{0\}
$$

and

$$
\bigcap_{i=1}^{\infty}\left(\frac{-1}{i}, \frac{1}{i}\right) \subset\{0\}
$$

For the first consider

$$
0 \in\{0\}
$$

for each interval $(-1 / i, 1 / i)$ the following inequality is satisfied

$$
-1 / i<x 1_{i}
$$

thus

$$
0 \in(-1 / i, 1 / i) \quad i=1,2,3, \ldots
$$

and

$$
\left.0 \in \bigcap_{i=1}^{\infty}(-1 / i) 1 / i\right)
$$

but $O$ is the only element in $\{0\}$ sc

$$
\left.0 \in\{0\} \subset \bigcap_{i=1}^{\infty}(-1 / i) 1 / i\right)
$$

To prove the second subset relation consider some value of $x$ where

$$
x \in \bigcap_{i=1}^{\infty}(-1 / i, 1 / i)
$$

it follows that

$$
x \in(-1 / i, 1 / i)
$$

so

$$
-1 / i<x<1 / i \text { for } i=1,2,3, \ldots
$$

if $x \neq 0$ then values of $i$ can be choosen such that

$$
x<-1 / i \text { or } x>1 / i
$$

thus $x=0$ and it follows that

$$
0 \in\{0\}
$$

and

$$
\bigcap_{i=1}^{\infty}(-1 / i, 1 / i) \subset\{0\}
$$

thus

$$
\bigcap_{i=1}^{\infty}(-1 / i, 1 / i)=\{0\}
$$

* Next consider the intersection

$$
\bigcap_{n=1}^{\infty}(a-1 / n, b+1 / n)=[a, b] \quad n=\underset{a<b}{1,2,3} \ldots
$$

The sequence of intervals generated b) the intersection is
$(a-1, b+1) \supset(a-1 / 2, b+1 / 2) \supset(a-1 / 3, b+1 / 3)$
つ...つ ( $a-1 / n, b+1 / n)$
This sequence is monotonic. Also for each interval the following inequality is satisfied

$$
a-1 / n<x<b+1 / n
$$

A ursinal presentation is also interesting to consider. The containment of the interval $[a, b]$ in each interval is apparent.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-168.jpg?height=799&width=1438&top_left_y=114&top_left_x=70)

To prove

$$
\bigcap_{n=1}^{\infty}(a-1 / n, b+1 / n)=[a, b]
$$

it must be shown that

$$
\bigcap_{n=1}^{\infty}(a-1 / n, b+1 / n) \supset[a, b]
$$

and

$$
\bigcap_{n=1}^{\infty}(a-1 / n, b+1 / n) \subset[a, b]
$$

To prove the first relation assume that

$$
x \in[a, b]
$$

it follows that

$$
a \leqslant x \leqslant b
$$

it follows that for $n=1,2,3, \ldots$

$$
a-1 / n<x<b+1 / n
$$

thus

$$
x \in(a-1 / n, b+1 / n)
$$

and

$$
x \in \bigcap_{i=1}^{\infty}(a-1 / n, b+1 / n)
$$

so the first relation is proven

$$
[a, b] \subset \bigcap_{i=1}^{\infty}(a-1 / n, b+1 / n)
$$

To prove the second relation assume that

$$
x \in \bigcap_{i=1}^{\infty}(a-1 / n, b+1 / n)
$$

it follows that

$$
x \in(a-1 / n, b+1 / n) \text { for } n=1,2,3 \ldots
$$

and

$$
x \in[a, b]
$$

thus

$$
\bigcap_{l=1}^{\infty}(a-1 / n, b+1 / n) \subset[a, b]
$$

and the desired result is obtained

$$
\bigcap_{i=1}^{\infty}(a-1 n, b+1 / n)=[a, b]
$$

* Next Consider unions and intersections of closed intervals.
If $F_{j}$ is a closed intercal show that

$$
\bigcap_{j=1}^{\infty} F_{j}
$$

is closed. To prove this recall De Morgan's Law

$$
\left(\bigcap_{j=1}^{\infty} F_{j}\right)^{c}=\bigcup_{j=1}^{\infty} F_{j}^{c}
$$

It follows that

$$
\bigcap_{j=1}^{\infty} F_{j}=\left(\bigcup_{j=1}^{\infty} F_{j}^{c}\right)^{c}
$$

Now since $F_{j}$ is a closed interval $F_{j}^{c}$ is an open interval. It was previously shown that the union of an infinite number of open intervals is open. Thus

$$
\bigcup_{j=1}^{\infty} F_{j}^{c}
$$

is spen. It follows that

$$
\left(\bigcup_{j=1}^{\infty} F_{j}^{c}\right)^{c}
$$

is closed. Thus the desired result is obtained, namely

$$
\bigcap_{j=1}^{\infty} F_{j}
$$

## is closed.

* Next consider a finite union of closed sets, $F_{j}$. Show that

$$
\bigcup_{i=1}^{n} F_{i}
$$

is closed.
Recall the other De Norgan's Law

$$
\left(\bigcup_{i=1}^{n} F_{i}\right)^{c}=\bigcap_{i=1}^{n} F_{i}^{c}
$$

50

$$
\bigcup_{i=1}^{n} F_{i}=\left(\bigcap_{i=1}^{n} F_{i}^{c}\right)^{c}
$$

Now since $F_{i}$ is closed $F_{i}^{c}$ is open. It was previously shown that a finite intersection of open sets is open thus

$$
\bigcap_{i=1}^{n} F_{i}^{c}
$$

is open. It follows that

$$
\left(\bigcap_{i=1}^{n} F_{i}^{c}\right)^{c}
$$

is closed. Thus the desired result is obtained

$$
\bigcup_{i=1}^{n} F_{i}=\left(\bigcap_{i=1}^{n} F_{i}^{c}\right)^{c}
$$

is closed.

* Consider an infinite union of closed sets. It will be seen with an example that it is not neccessarily closed.
$\bigcup_{i=1}^{n}[a+1 / n, b-1 / n]=(a, b) \quad a<b$
the sequence of intervals generated by the union is

$$
\begin{aligned}
& {[a+1, b-1] \subset[a+1 / 2, b-1 / 2] c} \\
& {[a+1 / 3, b-1 / 3] c \cdots c[a+1 / n, b-1 / n]}
\end{aligned}
$$

This sequence is monotonic. Also for each interval the following inequality is satisfied

$$
a+1 / n \leqslant x \leqslant b-1 / n \quad n=1,2,3, \ldots
$$

A ursival presentation is also interesting to consider. The containment of the interval $(a, b)$ in
apparent.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-174.jpg?height=723&width=1202&top_left_y=1273&top_left_x=147)

To prove

$$
\bigcup_{i=1}^{n}[a+1 / n, b-1 / n]=(a, b)
$$

It must be shown that

$$
\begin{aligned}
& \bigcup_{l=1}^{n}[a+1 / n, b-1 / n] \supset(a, b) \\
& \bigcup_{l=1}^{n}[a+1 / n, b-1 / n] \subset(a, b)
\end{aligned}
$$

To prove the first statement assume that

$$
x \in(a, b)
$$

It follows that

$$
x \in \bigcup_{l=1}^{n}\left[a+y_{n}, b-y_{n}\right]
$$

For this to be true it must be the case that for some value of $n$

$$
a+1 / n \leqslant x \leqslant b-1 / n
$$

Now it is assumed that

$$
a<x<b
$$

so for any $x$ it follows that
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-176.jpg?height=231&width=763&top_left_y=652&top_left_x=378)
where

$$
\begin{aligned}
& \Delta a=x-a \\
& \Delta b=b-x
\end{aligned}
$$

a value of $n$ that such that

$$
a+1 / n \leqslant x \leqslant b-1 / n
$$

is given by one of two possibilities

$$
\frac{1}{n_{a}} \leqslant x-a \quad \frac{1}{n_{b}} \leqslant b-x
$$

these expressions can be solved for $n_{a}$ and $n_{b}$ to give

$$
\frac{1}{x-a} \leqslant n_{a} \quad \frac{1}{b-x} \leqslant n_{b}
$$

The smallest of $n_{a}$ and $n_{b}$ that will satisfy both inequalities is given by

$$
n=\max \left\{\left\lceil\frac{1}{x-a}\right\rceil,\left\lceil\frac{1}{b-x}\right\rceil\right\}
$$

where $[\cdots]$ denotes the ceiling function, thus

$$
\bigcup_{l=1}^{n}[a+1 n, b-1 / n] \supset(a, b)
$$

Now to prove the second relation assume that

$$
x \in \bigcup_{i=1}^{n}\left[a+y_{n}, b-y_{n}\right]
$$

it follows that for some value of $n$ and any values larger that

$$
x \in[a+1 / n, b-1 / n]
$$

it follows that

$$
a+1 / n \leqslant x \leqslant b-1 / n
$$

now

$$
1 / n>0 \quad \forall n
$$

it follows that

$$
a<a+1 / n \quad b>b-1 / n
$$

thus

$$
a<x<b
$$

and

$$
x \in(a, b)
$$

so the desired result is proven

$$
\bigcup_{i=1}^{n}[a+1 / n, b-1 / n]=(a, b)
$$

* A theorem that will be useful later is trat between two distinct real numbers there is a rational

Consider a rational of the form

$$
\frac{p}{q}
$$

where $q$ is a fired integer and $P$ is an integer that can vary. The proof of the theorem will use contradiction. Let $x$ and $y$ be two real numbers with $x<y$. Assume that there are no rational numbers between $x$ and $y$. Let $P l q$ be the largest rational number satisfying

$$
\frac{p}{q}<x
$$

since there are no rationals between $x$ and $y(p+1) / q$ will be greater than $y$

$$
\frac{p+1}{q}>y
$$

It follows that

$$
P \frac{+1}{q}-\frac{P}{q}>y-x
$$

$$
\Rightarrow \frac{1}{9}>y-x
$$

Now $x, y$ and $q$ are arbitrary so it is possibe to choose values that do not satisfy the inequality. It follows that there is a rational number between $x$ and $y$

## * Finally consider the following theorem.

If $E \subseteq \mathbb{R}$ is an open set, then there exist at most countably many disjoint open intervals $I_{j}, j=1,2,3, \ldots$, such that

$$
E=\bigcup_{j=1}^{\infty} I_{j}
$$

To get a sense of what this theorem is attempting consider consider two open intervals

$$
\begin{aligned}
& \left(x_{1}, y_{1}\right)=I_{1} \\
& \left(x_{2}, y_{2}\right)=I_{2}
\end{aligned}
$$

that are not disjoint so that

$$
I_{1} \cap I_{2} \neq \phi
$$

a new open interoal can be constructed from the union of $I_{1}$ and $I_{2}$ since it was previously shown that the union of open intervals is open. The new interval costructed from the union is

$$
I_{1} \cup I_{2}=\left(\min \left(x_{1}, x_{2}\right), \max \left(y_{1}, y_{2}\right)\right)
$$

It follows any intersecting open intervals can be considered as a single interval. Because of this property any open interval will be a union of disjoint open intervals. Examples of open intervals are

$$
(0,1)
$$

$$
(0,2) \cup(2,5) \cup(10,12)
$$

$$
\bigcup_{n=1}^{\infty}(n, n+1)
$$

## Borel 6-Algebra

Let $O$ denote the set of all open sets of $\mathbb{R}$. The Borel 0-algerba, denoted by $B$ is the o-abebra generated by 0 .

$$
B=\sigma(\theta)
$$

$B$ will contain all open and closed sets and all unions and intersections of both open and closed sets.
Alteratively $B$ can be defined as the 6-algebra generated by all closed sets of $\mathbb{R}$.

## Conditional Expectation

## Conditioning on an Event

Consider a probability space $(\Omega, F, P)$ where $\omega \in \Omega$. A random variable is a function $X(\omega) \rightarrow \mathbb{R}$. Consider an event $B \in \mathcal{F}$ such that $P(B) \neq 0$. The conditional expectation of $x$ given $B$ is defined by

$$
E(x \mid B)=\frac{1}{P(B)} \int_{B} x(\omega) d P(\omega)
$$

## Example: Investing

An investor plans to invest $\$ 10$ in an asset. According to his estimate the asset value in the coming two years can be represented by the following diagram.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-185.jpg?height=531&width=1293&top_left_y=650&top_left_x=116)

The number along the arrow represents the probability that the event indicated by the arrow occurs. Let $\bar{X}$ be the value of the asset at the end of the second year.
Let $\omega_{t}=\left\{z_{1}, z_{2}, \ldots, z_{t}\right\}$ where $z_{i}= \pm 1$ indicate if the price went up or
down for the for the year. The sample space for $\omega_{2}=\left\{z_{1}, z_{2}\right\}$ is given by

$$
\Omega=\{(1,1),(1,-1),(-1,1),(-1,-1)\}
$$

If $z_{1}$ and $z_{2}$ are assumed to be independent the probability for each event can be detorminey by inspection of the diagram

$$
\begin{aligned}
& P(1,1)=\left(\frac{2}{3}\right)\left(\frac{1}{4}\right)=\frac{2}{12}=\frac{1}{6} \\
& P(1,-1)=\left(\frac{2}{3}\right)\left(\frac{3}{4}\right)=\frac{6}{12}=\frac{1}{2} \\
& P(-1,1)=\left(\frac{1}{3}\right)\left(\frac{1}{4}\right)=\frac{1}{12} \\
& P(-1,-1)=\left(\frac{1}{3}\right)\left(\frac{3}{4}\right)=\frac{3}{12}=\frac{1}{4}
\end{aligned}
$$

The event space is the powerset of $2^{\Omega}$.
If the random variable $x(\omega)$ is defined the value of the
asset it is seen that

$$
\begin{array}{ll}
x(1,1)=12.1 & x(1,-1)=10.45 \\
x(-1,1)=10.45 & x(-1,-1)=9.025
\end{array}
$$

Consider the event where the price increased the first year

$$
B=\{(1,1),(1,-1)\}
$$

what is the expected return given that the price increased the first year.

$$
E(x \mid B)=\frac{1}{P(B)} \int_{B} x(\omega) d P(\omega)
$$

Now

$$
\begin{aligned}
P(B) & =P(1,1)+P(1,-1) \\
& =1 / 6+1 / 2=\frac{4}{6}=\frac{2}{3}
\end{aligned}
$$

so

$$
\begin{aligned}
E(X \mid B) & =\frac{3}{2}\left\{(12,1)\left(\frac{1}{6}\right)+(10.45)\left(\frac{1}{2}\right)\right\} \\
& =\frac{3}{2}(7,24)=10.8625
\end{aligned}
$$

## Conditioning on a Discrete Random variable

Consider the probability space $(\Omega, \mathcal{F}, P)$ and let 2 be a function from $\Omega \rightarrow \mathbb{R}$,

$$
\left\{\omega \in \Omega: z(\omega)=z_{i}\right\}
$$

such that it takes on $m$ values

$$
z: \Omega \rightarrow\left\{z_{1}, z_{2}, \ldots, z_{m}\right\}
$$

2 defines a discrete random variable.
If $x(\omega)$ is a random variable on the probability space $(\Omega, J, P)$ then the conditional expectation of $x$ given $z$ is a random variable that can take on $m$ values. The conditional expectation of $X(\omega)$ given that $z=z i$ is given by

$$
E\left(X \mid Z=Z_{i}\right)=\frac{1}{P\left(Z=Z_{i}\right)} \int_{Z=Z_{i}} X(\omega) d P(\omega)
$$

## Example: Three Coin Toss Game

Three coins with values $10 \phi$, $20 \phi$ and 50 d are tossed. The value of the coins with heads are summed to produce the random variable $x$. Let 2 be the sum of the $10 \$$ and $20 \$$ coms. what is $E(x \mid z)$ ?

To construct the sample space assume conis are tossed in the order 104, 204 and 504 and denole the 104 tossed by green, the 20 k by red and 50 t blue
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-189.jpg?height=348&width=1180&top_left_y=1309&top_left_x=243)

There are $2^{3}=8$ different outcomes The sample space is given by
$\Omega=\{H H H, H H T, H T H, H T T$,

$$
T H H, T H T, T T H, T T T \xi
$$

The event space is given by the power set of $\Omega$

$$
\xi=2^{\Omega}
$$

The probability of each outcome in the sample space are assumed equal so

$$
\begin{array}{ll}
P(H H H)=1 / 8 & P(H T H)=1 / 8 \\
P(T H H)=1 / 8 & P(T T H)=1 / 8 \\
P(H H T)=1 / 8 & P(H T T)=1 / 8 \\
P(T H T)=1 / 8 & P(T T T)=1 / 8
\end{array}
$$

It follows that

$$
\begin{array}{ll}
X(H H H)=80 \mathrm{~d} & X(H T H)=604 \\
X(T H H)=704 & X(T T H)=504 \\
X(H H T)=304 & X(H T T)=104 \\
X(T H T)=204 & X(T T T)=04
\end{array}
$$

and
$P(H H)=P(H H H)+P(H H T)=1 / 8+1 / 8=1 / 4$
$P(H T)=P(H T H)+P(H T T)=18+18=44$
$P(T H)=P(T H H)+P(T H T)=48+18=14$
$P(T T)=P(T T H)+P(T T T)=1 / 8+1 / 8=1 / 4$

$$
\begin{aligned}
& Z(H H)=304 \\
& Z(H T)=104 \\
& Z(T H)=204 \\
& Z(T T)=04
\end{aligned}
$$

Since 2 has 4 values cualuating $E(x \mid z)$ will have 4 values, now

$$
E(x \mid z=a)=\frac{1}{P(z=a)} \int_{z=a} x d P(x)
$$

so

* $E(x \mid z=30)=\frac{1}{P(H H)}\{P(H H H) 80+$
$P(H H T) 30\}$

$$
\begin{aligned}
& \begin{aligned}
= & \frac{1}{1 / 4}\left\{\frac{80}{8}+\frac{80}{8}\right\} \\
= & 4\left(10+\frac{15}{4}\right)=40+15=55
\end{aligned} \\
& * E(X \mid Z=10)=\frac{1}{P(H T)}\{P(H T H) 60+ \\
& \quad P(H T T) 10\} \\
& =4\left(\frac{60}{8}+\frac{10}{8}\right)=4\left(\frac{30}{4}+\frac{5}{4}\right)=35 \\
& * E(X / Z=20)=\frac{1}{P(T H)}\{P(T H H) 70+ \\
& \quad P(T H T) 20\} \\
& =4\left(\frac{70}{8}+\frac{20}{8}\right)=35+10=45 \\
& * E(X / Z=0)=\frac{1}{P(T T)}\{P(T T H) 50+ \\
& \quad P(T T T) 0\}
\end{aligned}
$$

$$
=4\left(\frac{50}{8}\right)=25
$$

In summary

$$
\begin{aligned}
& E(x \mid z=30)=55 \\
& E(x \mid z=20)=45 \\
& E(x \mid z=10)=35 \\
& E(x \mid z=0)=25
\end{aligned}
$$

## Definition of Conditional Expectation

Consider the probability space $(\Omega, F, P)$ a random voriable $X(\omega)$ and a discrele random variable that takes on $m$ values

$$
\left\{\omega \in \Omega: z(\omega)=z_{i}\right\}
$$

such that it takes on $m$ values

$$
z: \Omega \rightarrow\left\{z_{1}, z_{2}, \ldots, z_{m}\right\}
$$

The condition expectation of $x(w)$ given $z=z_{i}$ is defined by

$$
E\left(X \mid Z=Z_{c}\right)=\frac{1}{P\left(Z=Z_{i}\right)} \int_{Z=Z_{i}} x d P
$$

$z=z_{i}$. It follows that

$$
\int_{z=z_{i}} E(x \mid z) d P=\int_{z=z_{i}} E\left(x \mid z=z_{i}\right) d P
$$

$$
=E\left(X \mid z=z_{i}\right) \int_{z=z_{i}} d P
$$

Now

$$
E\left(x \mid z=z_{i}\right)=\frac{1}{P\left(z=z_{i}\right)} \int_{z=z_{i}} x d P
$$

and

$$
P\left(z=z_{i}\right)=\int_{z=z_{i}} x d P
$$

thus

$$
\int_{z=z_{i}} E(x \mid z) d P=\int_{z=z_{i}} x d P
$$

For any event $A$ that is an element of the $\sigma$-algebra generated by $z=\left\{z_{1}, z_{2}, \ldots, z_{m}\right\}$

$$
A \in \sigma(z)
$$

which will be a countable union of disjoint sets of the form $\left\{\Sigma_{i}\right\}$ it follows that

$$
\begin{aligned}
& \int_{A} E(x \mid z) d P=\sum_{z_{i} \in A} \int_{z=z_{i}} E(x \mid z) d P \\
& =\sum_{z_{i} \in A} \int_{z=z_{i}} x d P \\
& =\int_{A} x d P
\end{aligned}
$$

Thus

$$
\int_{A} E(x \mid z) d P=\int_{A} x d P
$$

## Example: Verification of Defintion of Conditional Expectation

Consider a probability space $(\Omega, \mathcal{F}, P)$ if $Z$ is a discrete random variable then $E(X I Z)$ is $G(Z)$ measureable. For any $A \in S(z)$ it follows that

$$
\int_{A} E(\bar{x} \mid z) d P=\int_{A} \bar{x} d P
$$

Using the coin toss game from the previous example consider the sample spaces induced by the random variables $X$ and $Z$,

$$
\begin{aligned}
& \Omega_{x}=\{0,10,20,30,50,60,70,80\} \\
& \Omega_{2}=\{0,10,20,30\}
\end{aligned}
$$

All events in each event space are equally probable so,

$$
\left\{\omega \in \Omega_{x}: P(\omega)=1 / 8\right\}
$$

and

$$
\left\{\omega \in \Omega_{2}: P(\omega)=1 / 4\right\}
$$

Consider the events

$$
A_{1}=\{z=20\}
$$

and

$$
A_{2}=\{z=10, z=30\}
$$

Now previously it was shown that for

$$
\begin{gathered}
z=20 \quad x=\{70,20\} \\
E(x / z=20)=45
\end{gathered}
$$

and for

$$
\begin{gathered}
Z=\{10,30\} \quad X=\{10,60,80,30\} \\
E(X \mid Z=30)=55 \\
E(X \mid Z=10)=35
\end{gathered}
$$

It follows that for $A_{1}$

$$
\begin{aligned}
& \int_{A_{1}} X d P=(70)\left(\frac{1}{8}\right)+(20)\left(\frac{1}{8}\right) \\
& =\frac{35}{4}+\frac{10}{4}=\frac{45}{4} \\
& \int_{A_{1}} E(X \mid Z) d P=\frac{45}{4}
\end{aligned}
$$

and for $A_{2}$

$$
\begin{aligned}
& \int_{A_{2}} X d P=(10)\left(\frac{1}{8}\right)+(60)\left(\frac{1}{8}\right) \\
& +(50)\left(\frac{1}{8}\right)+(38)\left(\frac{1}{8}\right) \\
& =\frac{5}{4}+\frac{30}{4}+\frac{40}{4}+\frac{25}{4} \\
& =\frac{90}{4}=\frac{45}{2} \\
& \int_{A_{2}} E(x \mid 2) d P=(35)\left(\frac{1}{4}\right)+(55)\left(\frac{1}{4}\right) \\
& =\frac{90}{4}=\frac{45}{2}
\end{aligned}
$$

## Relation Between Defintions of Conditional Expectation

Consider a probability space $(\Omega, F, P)$ with random variables $X(\omega)$ and $z \omega)$ if an event $A$ is an event in the 6 -agebra generated by $z$

$$
A \in \sigma(z)
$$

then the conditional expectation of $X$ given $z$ over $A$ is given by

$$
\int_{A} E(x \mid z) d P=\int_{A} x d P
$$

Assume that a joint probability density function for $X$ and $Z$ exists and is given by

$$
f(x, 2)
$$

Now the conditional probability density is defined by

$$
f(x / z)=\frac{f(x, z)}{f(z)}
$$

where

$$
f(z)=\int f(x, z) d x
$$

it also follows that

$$
d P=f(x, y) d x d y
$$

Now using

$$
\begin{aligned}
& \int_{z=z_{i}} E(x \mid z) d P=\int_{z=z_{i}} x d P \\
\Rightarrow & E\left(x \mid z=z_{i}\right) \int_{z=z_{i}} d P=\int_{z=z_{i}} x d P \\
\Rightarrow & E\left(x \mid z=z_{i}\right) \iint_{z=z_{i}} f(x, y) d x d z \\
= & \iint_{z=z_{i}} x f(x, y) d x d z
\end{aligned}
$$

$$
\begin{array}{r}
\Rightarrow E\left(x \mid z=z_{i}\right) \int_{z=z_{i}}\left\{\int f(x, y) d x\right\} d z \\
=\iint_{z=z_{i}} x f(x, y) d x d z \\
\Rightarrow E\left(x \mid z=z_{i}\right) \int_{z=z_{i}} f(z) d z \\
=\iint_{z=z_{i}} x f(x, y) d x d z \\
\Rightarrow E\left(x \mid z=z_{i}\right) f\left(z_{i}\right)=\int x f\left(x, z_{i}\right) d x \\
\Rightarrow E\left(x \mid z=z_{i}\right)=\frac{1}{f\left(z_{i}\right)} \int x f\left(x, z_{i}\right) d x \\
=\int x f \frac{\left(x, z_{i}\right)}{f\left(z_{i}\right)} d x \\
=\int x f\left(x \mid z_{i}\right) d x
\end{array}
$$

Thus

$$
E(x \mid z)=\int x f(x \mid z) d x
$$

## Expectation Conditioned on a G-Field

Consider the probability space $(\Omega, \mathcal{F}, P)$ and let $\mathcal{J}(\mathcal{F}$ be a 6 -field. If $x$ is a random variable and if $A C \&$

$$
\int_{A} E(x \mid \Delta) d P=\int_{A} x d P
$$

Example 1: $\mathcal{J}=\{\phi, \Omega\}$
Let $A=\Omega$ then

$$
E(x \mid \Omega)=\frac{1}{P(\Omega)} \int_{\Omega} x d P
$$

but by definition

$$
\begin{gathered}
P(\Omega)=1 \\
E(x)=\int_{\Omega} x d P
\end{gathered}
$$

thus

$$
E(x \mid \Omega)=E(x)
$$

Let $A=\varnothing$, by definition

$$
P(\phi)=0
$$

Thus $E(X \mid \phi)$ is undefined
It follows that

$$
E(X \mid A)=E(X)
$$

Example 2: $E(E(x|\forall| B)=E(x \mid A)$
Consider the probability space $(\Omega, \mathcal{F}, P)$ where $\triangle C \mathcal{F}$ and $B \in \mathcal{H}$. Recall that for a random variable X

$$
\int_{B} E(x \mid y) d P=\int_{B} x d P
$$

Now

$$
\begin{aligned}
& E(E(x \mid \Delta) \mid B)=\frac{1}{P(B)} \int_{B} E(x \mid D) d P \\
= & \frac{1}{P(B)} \int_{B} x d P=E(x \mid B)
\end{aligned}
$$

## Example 3: Fair Dice

Consider the probability space $(\Omega, 7, P)$ for a fair dice,

$$
\begin{aligned}
& \Omega=\{1,2,3,4,5,6\} \\
& \{\omega \in \Omega: P(\omega)=1 / 6\} \\
& \}=2^{\Omega}
\end{aligned}
$$

where $\Omega$ is the possible values for a single throw. Let

$$
\begin{gathered}
\mathcal{F}_{1}=\{\varnothing, \Omega\} \\
\mathcal{F}_{2}=\{\varnothing,\{1,2,3\},\{4,5,6\}, \Omega\} \\
\mathcal{F}_{3}=2^{\Omega}
\end{gathered}
$$

define the random variable

$$
\begin{gathered}
x: \Omega \rightarrow \mathbb{R} \\
x(\omega)=(\omega-4)^{+}=\max (1, \omega-4)
\end{gathered}
$$

It follows the values of $x$ are members of

$$
\{1,2\}
$$

The 6 -fied generated by $x$ is produced by the valid samples,

$$
\begin{aligned}
\sigma(x)= & \{\varnothing,\{5\},\{6\},\{1,2,3,4,6\} \\
& \{1,2,3,4,5\},\{5,6\}, \\
& \{1,2,3,4\}, \Omega\}
\end{aligned}
$$

Clearly

$$
x \in \mathcal{F}_{3}
$$

but

$$
x \notin \mathcal{F}_{1}, \quad x \notin \mathcal{F}_{2}
$$

Now since $F_{1}=\{\varnothing, \Omega\}$

$$
\begin{aligned}
& E\left(x \mid \mathcal{F}_{1}\right)=E(x)=(1)\left(\frac{1}{6}\right)+2\left(\frac{1}{6}\right) \\
& =\frac{1}{2}
\end{aligned}
$$

Next consider conditioning on $\mathcal{F}_{2}$, this requires evaluating the expectation for each value of $\mathcal{F}_{2}$, 50

$$
E(x \mid \Omega)=E(x)=1 / 2
$$

For $\{1,2,3\} \quad \sigma(x) \cap\{1,2,3\}=\varnothing$ it follows that

$$
\begin{aligned}
E(x \mid\{1,2,3\}) & =\frac{1}{P(\{1,2,3\})} \int_{\{1,2,3\}} x d P \\
& =0
\end{aligned}
$$

For $\{4,5,6\} \quad \sigma(x) \cap\{4,5,6\}=\{5,6\}$

$$
\begin{aligned}
E(x \mid\{4,5,6\}) & =\frac{1}{P(\{4,5,6\})} \int x d P \\
& =\frac{1}{(1 / 2)}\left\{(1)\left(\frac{1}{6}\right)+(2)\left(\frac{1}{6}\right)\right\} \\
& =2\left(\frac{1}{2}\right)=1
\end{aligned}
$$

Finally conditioning on $\mathcal{F}_{3}$ and noting that $x \in \mathcal{F}_{3}$

## Example 4: Conditional Expectation as Random variable

Consider a probability space $(\Omega, F, P)$ where $\forall \subset \mathcal{F}$ is a $\sigma$-field and let $A \in A$ denote an event and $x$ a random variable. The random variable $\Gamma$ is said to be the "conditional expectation of $x$ with respect to $y^{\prime \prime}$ and is denoled by

$$
\Gamma=E(X \mid A)
$$

if
D) $\Gamma$ is $\star$ measurable,

$$
\{\omega \in \Omega: \Gamma(\omega) \leqslant \gamma\} \in \mathscr{H}
$$

2) $E\left(\Gamma \mathbb{I}_{A}\right)=E\left(X \mathbb{I}_{A}\right) \quad \forall A \in \mathcal{H}$

Condition 2 implies

$$
\int_{A} \Gamma d P=\int_{A} x d P
$$

Now assume that for $\omega \in A$

$$
\Gamma(\omega)=\text { constant }
$$

It follows that

$$
\int_{A} \Gamma d P=\Gamma(A) P(A)
$$

so

$$
\Gamma(A)=\frac{1}{P(A)} \int_{A} x d P
$$

## Example 1

Consider the probability space $(\Omega, F, P)$ where the sample space is given by

$$
\Omega=\{a, b, c, d, e, f\}
$$

and probability measure

$$
\{\omega \in \Omega: P(\omega)=1 / \eta\}
$$

Let $X, Y$ and $Z$ given by

$$
\begin{aligned}
& x \sim\left(\begin{array}{llllll}
a & b & c & d & e & f \\
1 & 3 & 3 & 5 & 5 & 7
\end{array}\right) \\
& y \sim\left(\begin{array}{llllll}
a & b & c & d & e & f \\
2 & 2 & 1 & 1 & 7 & 7
\end{array}\right) \\
& z \sim\left(\begin{array}{llllll}
a & b & c & d & e & f \\
3 & 3 & 3 & 3 & 2 & 2
\end{array}\right)
\end{aligned}
$$

Now the 6 -fieds generated by the random variable $y$
and $z$ are given by

$$
\begin{aligned}
& \sigma(y)=\{\{a, b\},\{c, d\},\{e, f\} \\
& \{c, d, e, f\},\{a, b, e, f\},\{a, b, c, d\}, \\
& \phi,\{a, b, c, d, e, f\}\} \\
& \sigma(z)=\{\{a, b, c, d\},\{e, f\}, \varnothing \\
& \{a, b, c, d, e, f\}\}
\end{aligned}
$$

First consider the case where $A=\sigma(1)$ so that

$$
\Gamma=E(x \mid \sigma(y))
$$

The set of disjoint "atomic events" from which the remaining elements of $\sigma(y)$ are constructed are

$$
\{a, b\},\{c, d\},\{e, f\}
$$

each of these events maps to
a unique value of $y$,

$$
\begin{array}{ll}
y(\{a, b\})=2, & P(y=2)=1 / 3 \\
y(\{c, d\})=1, & P(y=1)=1 / 3 \\
y(\{e, f\})=7, & P(y=7)=1 / 3
\end{array}
$$

For each value of $y, x$ takes on the values

$$
\begin{aligned}
& \begin{aligned}
y & =2: x(\{a, b\}) \\
y & =1: x(\{c, d\})=\{1,3\} \\
y=7: x(\{e, f\}) & =\{3,5\} \\
u \sin g & \\
E(x \mid \sigma(I))(\omega \in A) & =\frac{1}{P(A)} \int_{A} x d P \\
\text { let } \quad A & =\{\omega \in Q: Y(\omega)=2\} \\
& =\{a, b\}
\end{aligned}
\end{aligned}
$$

then

$$
\begin{aligned}
& E(X \mid \sigma(Y))(\omega \in A)=\frac{1}{P(A)} \int_{A} X d P \\
& =\frac{1}{1 / 3}\left[(1)\left(\frac{1}{6}\right)+(3)(1 / 6)\right] \\
& =\frac{1}{2}(1+3)=2
\end{aligned}
$$

Next let

$$
\begin{gathered}
A=\{\omega \in Q: Y(\omega)=1\} \\
=\{C, d\} \\
E(X \mid \sigma(Y))(\omega \in A)=\frac{1}{P(A)} \int_{A} X d P \\
=\frac{1}{1 / 3}\left[(3)\left(\frac{1}{6}\right)+(5)(1 / 6)\right] \\
=\frac{1}{2}(3+5)=4
\end{gathered}
$$

Finally let

$$
\begin{aligned}
A= & \{\omega \in \Omega: V(\omega)=7\} \\
& =\{e, f\}
\end{aligned}
$$

then

$$
\begin{aligned}
& E(x \mid \sigma(y))(\omega \in A)=\frac{1}{P(A)} \int_{A} x d P \\
& =\frac{1}{v_{3}}\left[(5)\left(\frac{1}{6}\right)+(7)\left(\frac{1}{6}\right)\right] \\
& =\frac{1}{2}(5+7)=6
\end{aligned}
$$

In summary

$$
E(x \mid G(y))(\omega)= \begin{cases}2 & \omega \in\{a, b\} \\ 4 & \omega \in\{c, d\} \\ 6 & \omega \in\{c, P\}\end{cases}
$$

Next Consider

$$
y=\sigma(z)
$$

then

$$
\Gamma=E(x \mid \sigma(2))
$$

The atoms of $\sigma(z)$ are,

$$
\{a, b, c, d\},\{e, f\}
$$

Each of these maps to uniqe value of $z$,
$z(\{a, b, c, d\})=3, \quad P(z=3)=2 / 3$
$z(\{e, f\})=2, \quad P(z=2)=1 / 3$
For each value of $2, x$ takes on the values
$2=3: \quad X(\{a, b, c, d\})=\{1,3,5\}$
$z=2: x(\{e, f \xi)=\{5,7\}$
using

$$
E(x \mid \sigma(z))(\omega \in A)=\frac{1}{P(A)} \int_{A} x d P
$$

let

$$
\begin{aligned}
A & =\{\omega \in Q: 2(\omega)=3\} \\
& =\{a, b, c, d\} \\
E(X \mid \sigma(2))(\omega \in A) & =\frac{1}{P(A)} \int_{A} X d P \\
= & \frac{1}{(23)}\left[(1)\left(\frac{1}{6}\right)+(3)\left(\frac{1}{3}\right)+(5)\left(\frac{1}{6}\right)\right] \\
= & \left(\frac{3}{2}\right)\left(\frac{1}{6}\right)(1+6+5) \\
= & \frac{1}{4}(12)=3
\end{aligned}
$$

Next let

$$
\begin{aligned}
A & =\left\{\omega \in \_Q: 2(\omega)=2\right\} \\
& =\{e, f\}
\end{aligned}
$$

$$
\begin{aligned}
& E(x \mid \sigma(2))(\omega \in A)=\frac{1}{P(A)} \int_{A} x d P \\
& =\frac{1}{(1 / 3)}\left[(5)\left(\frac{1}{6}\right)+(7)\left(\frac{1}{6}\right)\right] \\
& =\frac{1}{2}(5+7)=6
\end{aligned}
$$

In summary

$$
E\left(x \left\lvert\, 6(2)(\omega)= \begin{cases}3 & \omega \in\{a, b, c d\} \\ 6 & \omega \in\{e, f\}\end{cases}\right.\right.
$$

Example: Conditional Expectation of Measurable Random Variable

It this section the conditional expectation of a measurable random variable is computed to verify the relation

$$
E(x \mid F)=x
$$

where $x$ is $f$ measureable. This result is compared with a calculation of the conditional expectation of a random variable that is not $\mathcal{F}$ measureable.
Consider a coin toss game consisting of two tosses. The probability space $(\Omega, \mathcal{F}, P)$ is given by

$$
\begin{aligned}
& \Omega=\{H H, H T, T H, T T\} \\
& F=2^{\Omega}=\{H H, H T, T H, T T,\{H H, H T\}, \\
&\{H H, T H\},\{H H, T T\},\{H T, T H\}, \\
&\{T H, T I\},\{H H, H T, T H\}, \\
&\{H H, H T, T T\},\{H T, T H, T T\}, \\
&\{H H, T H, T T\}, \Phi, \Omega\}
\end{aligned}
$$

and $P$ is uniform on $\Omega$, for every $\omega \in \Omega, P(\omega)=k l$.
Define two random variables, $x$ which is 1 if second toss is heads an -1 if the second toss is tails and 2 which is 1 if first toss is heads and -1 if first toss is tails. More explicitly,

$$
\begin{aligned}
& X(\omega)=\left\{\begin{aligned}
1 & \text { if } \omega \in\{H H, T H\} \\
-1 & \text { if } \omega \in\{H T, T T\}
\end{aligned}\right. \\
& Z(\omega)=\left\{\begin{aligned}
1 & \text { if } \omega \in\{H H, H T\} \\
-1 & \text { if } \omega \in\{T H, T T\}
\end{aligned}\right.
\end{aligned}
$$

Now consider the $\sigma$-field generated by $X$,

$$
F_{x}=\sigma(x)=\{\phi,\{H H, T H\},\{H T, T T\}, \Omega\}
$$

It follows $x$ is $\mathcal{F}_{x}$ measureable. First compute the conditional expectation

$$
E\left(x \mid \mathcal{F}_{x}\right)
$$

The expectation can take on two values

$$
\{H H, T H\},\{H T, T T\}
$$

and for $A \in \mathcal{F}_{x}$ the expectation is given by

$$
E\left(x \mid \mathcal{F}_{x}\right)=\frac{1}{P(A)} \int_{A} x d P
$$

Now

$$
\begin{aligned}
& P(\{H H, T H\})=1 / 2 \\
& P(\{H T, T T\})=1 / 2
\end{aligned}
$$

and

$$
\begin{aligned}
& P(x=1)=P(\{H H, T H \xi)=1 / 2 \\
& P(x=-1)=P(\{H T, T T \xi)=1 / 2
\end{aligned}
$$

Now for $A=\{H H, T H\}$ and $X=1$

$$
E\left(x \mid \mathcal{F}_{x}\right)(\{H H, T H\})=\frac{1}{P(\{H H, T H\})} \int_{\{H H, T H\}} x d P
$$

$$
\begin{aligned}
& =\frac{1}{P(\{H H, T H\})}[P(X=1) \times(\{H H, T H)] \\
& =\frac{1}{(12)}[(12)(1)]=1
\end{aligned}
$$

and for $A=\{H T, T T\}$ and $x=-1$

$$
\begin{aligned}
& E\left(x \mid \mathcal{F}_{x}\right)(\{H T, T T\})=\frac{1}{P(\{H T, T T\})} \int_{\{H T, T T\}} x d P \\
& =\frac{1}{P(\{H T, T T \xi)}[P(x=-1) x(\{H T, T T\})] \\
& =\frac{1}{(1 / 2)}[(1 / 2)(-1)]=-1
\end{aligned}
$$

Thus the relation for the conditional expectation for an $\mathcal{F}$ mewsurable random variable is verifled,

$$
E\left(x \mid F_{y}\right)=x
$$

Next consider the conditional expection of $z$ which is not $\mathcal{F}_{x}$ measureable. Once again the possible values are of $\mathcal{F}_{x}$ are

$$
\{H H, T H\},\{H T, T T\}
$$

Now

$$
Z(\omega)=\left\{\begin{aligned}
1 & \text { if } \omega \in\{H H, H T\} \\
-1 & \text { if } \omega \in\{T H, T T\}
\end{aligned}\right.
$$

where $x$ takes on a single value for each value of $\exists_{x}$ 2 takes on multiple values.

Thus for $A=\{H H, T H\}$

$$
2(H H)=1 \quad 2(T H)=-1
$$

and

$$
\begin{aligned}
& P(z=1)=1 / 4 \\
& P(z=-1)=44
\end{aligned}
$$

similarly for $A=\{H T, T T\}$

$$
Z(H T)=1 \quad Z(T T)=-1
$$

and

$$
\begin{aligned}
& P(z=1)=44 \\
& P(z=-1)=44
\end{aligned}
$$

It follows that for $A=\{H H, T H\}$

$$
\begin{aligned}
& E\left(Z \mid \mathcal{F}_{x}\right)(\{H, H, T H\})=\frac{1}{P(\{H H, T H\})} \int_{\{H H, T H\}} 2 d P \\
& =\frac{1}{P(\{H H, T H\})}[P(Z=1) Z(H H)+P(Z=-1) Z(T H)] \\
& =\frac{1}{(1 / 2)}[(1 / 4)(1)+(1 / 4)(-1)] \\
& =(1 / 2)(1-1)=0
\end{aligned}
$$

and for $A=\{H T, T T\}$

$$
\begin{aligned}
& E\left(z \mid \mathcal{F}_{x}\right)(\{H T, T T\})=\frac{1}{P(\{H T, T T\})} \int_{\{H T, T T\}} x d P \\
& =\frac{1}{P(\{H T, T T\})}[P(z=1) z(H T)+P(z=-1) z(T T)] \\
& =\frac{1}{(1 / 2)}[(4 / 4)(1)+(1 / 4)(-1)] \\
& =\frac{1}{2}(1-1)=0
\end{aligned}
$$

Trues

$$
E\left(z \mid \mathcal{F}_{x}\right)=0
$$

Note also that the following expression based on conctitional probability can be used. For

$$
A \in \mathcal{F}_{x}
$$

where

$$
Z(\omega)=\left\{\begin{aligned}
1 & \text { if } \omega \in\{H H, H T\} \\
-1 & \text { if } \omega \in\{T H, T T\}
\end{aligned}\right.
$$

The entire 2 sample space is given by

$$
\{H H, H T\} \cup\{T H, T T\}
$$

It follows that

$$
E\left(z \mid \mathcal{F}_{x}\right)(A)=
$$

$$
\frac{1}{P(A)} \omega \in A \cap \sum P(\omega) Z(\omega)
$$

so for $A=\{H T, T T\}$

$$
\begin{aligned}
& A \cap(\{H H, H T\} \cup\{T H, T T\}) \\
& =\{H H, T T\} \cap(\{H H, H T\} \cup\{T H, T T\}) \\
& =\{H H, T T\}
\end{aligned}
$$

so

$$
\begin{aligned}
E & \left(Z \mid \mathcal{F}_{x}\right)(\{H T, T T\}) \\
& =\frac{1}{P(\{H T, T T\})} \sum_{\omega \in\{H, T, T\}} Z(\omega) P(\omega) \\
& =\frac{1}{P(\{H T, T T\})}[P(H H) Z(H H)+P(T T) Z(T T)] \\
& =\frac{1}{(1 / 2)}[(4 k)(1)+(1 / 4)(-1)] \\
& =0
\end{aligned}
$$

## Martingales in Discrete Time

A countable sequence of random variables $z_{1}, z_{2}, z_{3}, \ldots$ representing the outcomes of random prenamena is called a discrete time stochastic process. The random variables are indexed by natural numbers $i=1,2,3, \ldots$ which are not necessarily evenly spaced in time.
Let $S$ represent a set of atomic samples used to costruct the sequence sample space. For a discrete time stochastic of length $n$ the sample space, $\Omega$, is constructed by taking $n$ cartesian products of $s$, for $n=3$

$$
\Omega=5 \times 5 \times 5
$$

Further let $(\Omega, \Im, P)$ denote the probability space supporting the sequence of randsm variables where the $\sigma$-field, $F_{1}$ is the power set
of $\Omega$,

$$
F=2^{\Omega}
$$

A filtration is a sequence of 6 -fields indexed by a natural number that satisty

$$
\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \mathcal{F}_{3} \cdots \subset \mathcal{F}
$$

Now the discrete time stochastic process

$$
z_{1}, z_{2}, z_{3}, \ldots
$$

is said to be adapted to a fittration if the $n$ 'th member of the sequence is $I_{n}$ measwreable, namelys

$$
\left\{\omega \in \Omega: z_{n}(\omega) \leqslant 2\right\} \in \mathcal{F}_{n}
$$

A $\sigma$-algebra in a filtration represents all knowledge up to $n$. If $A \in \mathcal{F}_{n}$ and

$$
\underline{11}_{A}= \begin{cases}1 & \omega \in A \\ 0 & \omega \notin A\end{cases}
$$

then

$$
P\left(A \mid \mathcal{F}_{n}\right)=E\left(\mathbb{1}_{A} \mid \mathcal{F}_{n}\right)=\mathbb{1}_{A}
$$

where the last step follows since $A \in \mathcal{F}_{n}$ implies that $\underline{1}_{A}$ is $\hat{F}_{n}$ measureable. thus if $\omega \in A$

$$
P\left(A \mid \xi_{n}\right)=1
$$

Finally a Martingale can be defined as follows.

A discrete time stochastic process

$$
z_{1}, z_{2}, z_{3}, \ldots
$$

is a Martingale if the following
conditions are satisfied conditions are solustied

1) $E\left(\left|Z_{n}\right|\right)<\infty$ for each $n=1,2,3, \ldots$
2) $z_{1}, z_{2}, z_{3}, \ldots$ is adapted to the filtration $\mathcal{F}_{1}, \mathcal{F}_{2}, \mathcal{F}_{3}, \ldots$
3) $E\left(z_{n+1} \mid F_{n}\right)=z_{n}$ for each $n=1,2,3, \ldots$

## Example: Symetric Random walk

As an example of a Martingale consider a symetric random walk which can be difined by a coin toss game in the following manner. Toss a fair coin $n$ times to produce a sequence of heads, denoted by H, and tails, denoled by $T$. Define a random variable $z_{i}$ for the ith coin toss by

$$
z_{i}=\left\{\begin{array}{cc}
1 & \text { ith toss is } H \\
-1 & \text { ith toss is } T
\end{array}\right.
$$

Then define another random variable $x_{n}$ as the sum of the $z_{i}$ if $n$ tosses are performed,

$$
x_{n}=\sum_{i=1}^{n} z_{i}
$$

For example consider 3 coin tosses in which the first toss is heads the second tails and the third
heads. Denote this event by

$$
\{H, T, H\}
$$

It follows that

$$
\begin{aligned}
Z(\{H, T, H \xi) & =Z_{1}(H)+Z_{2}(T)+Z_{3}(H) \\
& =1-1+1 \\
& =1
\end{aligned}
$$

The probability space for the symetric random walk depends on the number of tosses. The following sections will discuss each component of ( $\Omega_{n}, \mathcal{F}_{n}, P_{n}$ ).

## Sample space

The elements of the sample space for the symetric random walk will denote a possible result of $n$ tosses of the con. It follows that the sample space, $\Omega$, will consist of all possible atcomes of a game which stops after $n$ tosses. This will allow the calculation of all
possible realizations of the events that produce each possible value of $X_{n}$.

The atomic sample space for the symetric randan walk is given by

$$
S=\{H, T\}
$$

The sample space depends on the number tosses. For a single toss the sample space is given by

$$
\Omega_{1}=S=\{H, T\}
$$

for two tosses

$$
\Omega_{2}-S \times S=\{\{H, H\},\{H, T\},\{T, H\},\{T, T\}\}
$$

for three tosses

$$
\begin{aligned}
\Omega_{3} & =S \times S \times S=\{\{H, H, H\},\{H, H, T\},\{H, T, H\}, \\
& \{H, T, T\},\{T, H, H\},\{T, T, H\},\{T, H, T\}, \\
& \{T, T, T\}\}
\end{aligned}
$$

for $n$ tosses the sample space, $\Omega_{n}$, will contain $2^{n}$ elemements.
For simplicitly let

$$
H H=\{H, H\}
$$

so that

$$
\begin{aligned}
& \Omega_{1}=\{H, T\} \\
& \Omega_{2}=\{H H, H T, T H, T T\} \\
& \Omega_{3}=\left\{\begin{array}{l}
\text { } H H H, H H T, H T H, H T T, T H H, T T H, \\
T H T, T T T\}
\end{array}\right.
\end{aligned}
$$

## Probability Measure

The symmetric random walk assumes a fair coin toss so that

$$
P_{1}(H)=P_{1}(T)=1 / 2
$$

It is also assumed that each toss is independent of the previous so that

$$
P_{2}(H H)=P_{1}(H) P_{1}(H)=(1 / 2)(1 / 2)=1 / 4
$$

Because of this it follows that for any number of con tosses the probability is uniform across the sample space. In fact for $n$ tosses

$$
P_{n}(\omega)=(1 / 2)^{n} \text { for every } \omega \in \Omega_{n}
$$

## 6- Algebra

The $\sigma$-algebra for the symetric random walk will depend on the number of tosses since the sample space has this dependence. $I_{n}$ is the power set of $\Omega_{n}$. Here the $\sigma$-algebra for $n=1$ and 2 are computed manually. For barger $n$ the calculation starts to get involved.
so for a single toss

$$
F_{1}=\{\phi, H, T, \Omega, \xi
$$

and for $n=2$

$$
\begin{aligned}
\mathcal{F}_{2}= & \{\Phi, H H, H T, T H, T T,\{H T, T H, T T\}, \\
& \{H H, T H, T T\},\{H H, H T, T T\}, \\
& \{H H, H T, T H\},\{H H, H T\},\{T H, T T\} \\
& \{H H, T H\},\{H T, T T\},\{H H, T T\}, \\
& \{H T, T H\}, \Omega\}
\end{aligned}
$$

In general for $n$ tosses In is the power set

$$
F_{n}=2^{\Omega_{2}}
$$

## Filtration

In the prevolus section the 0 - algebras were computed for $n=1$ and $n=2$. Here the fittration for the two toss symetric randsm walk is computed, namely

$$
\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2}
$$

In a previous section it was
shown that

$$
\begin{aligned}
\mathcal{F}_{2}= & \{\Phi, H, H, H, T H, T T,\{H T, T H, T T\}, \\
& \{H H, T H, T T\},\{H H, H T, T T\}, \\
& \{H H, H T, T H\},\{H H, H T\},\{T H, T T\} \\
& \{H H, T H\},\{H T, T T\},\{H H, T T\}, \\
& \{H T, T H\}, \Omega\}
\end{aligned}
$$

Now at $t=0$ there is no information that any event in $\hat{f}_{2}$ has occured, so all that can be said is that $\omega \in \Omega_{2}$ thus

$$
\mathcal{F}_{0}=\left\{\phi, \Omega_{2}\right\}
$$

At $t=1$ the result of the first toss is available. This state is captured by constructing $\mathcal{F}_{1}$ from all events in $f_{2}$ in which the first toss is $H$ or $T$, namely

$$
\{H H, H T\},\{T H, T T\}
$$

also note that

$$
\{H H, H T\}^{C}=\{T H, T T\}
$$

thus

$$
\mathcal{F}_{1}=\left\{\varnothing,\{H H, H T\},\{T H, T T\}, \Omega_{2}\right\}
$$

It follows that the filtration for $n=2$ is given by

$$
\begin{aligned}
\mathcal{F}_{0}= & \left\{\phi, \Omega_{2}\right\} \\
\mathcal{F}_{1}= & \left\{\phi,\{H H, H T\},\{T H, T T\}, \Omega l_{2}\right\} \\
\mathcal{F}_{2}= & \{\phi, H H, H T, T H, T T,\{H T, T H, T T\}, \\
& \{H H, T H, T T\},\{H H, H T, T T\}, \\
& \{H H, H T, T H\},\{H H, H T\},\{T H, T T\} \\
& \{H H, T H\},\{H T, T T\},\{H H, T T\}, \\
& \{H T, T H\}, \Omega\}
\end{aligned}
$$

where

$$
\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2}
$$

After noticing the pattern the fitration can be deduced trat for $n=3$, where

$$
\begin{gathered}
\Omega_{3}=\{H H H, H H T, H T H, H T T, T H H, T T H, \\
T H T, T T T\}
\end{gathered}
$$

and

$$
\mathcal{F}_{3}=2^{\Omega_{3}}
$$

which contains cell possible atcomes of a 3 toss walk.
Now $\mathcal{F}_{2}$ will contain all possible 3 toss outcomes after 2 tosses are performed. Now all 2 toss outcomes are given by

$$
\Omega_{2}=\{H H, H T, T H, T T\}
$$

It follows that all possible 3 toss outcomes are given by \{HHH, HHT\}, \{HTH, HTT\}, \{THH, THT\}, \{TTH, TTT\}

The 6 -algbra for $\mathcal{F}_{2}$ must be closed wrder compliment and union so more elements must be considered when costructing $\mathrm{F}_{2}$. To close under compliment four more elements are required, namely,
§HHH,HHT ${ }^{\text {C }}=$ \&HTH,HTT,THH,TTH, THT, TTT系
\{HTH,HTT $\}^{\text {C }}=$ \&HHH,HHT,THH,TTH, THT, TTTZ
\{THH, THT\} ${ }^{\text {C }}=$ \{HHH, HHT, HTH, HTT, THT, TTTZ
\{TTH, TT T $\}^{\text {C }}$ = \{HHH, HHT, HTH, HTT, THH, TTH 3
To be closed under union

$$
\begin{aligned}
\binom{4}{2}=\frac{4!}{(2!)(2!)} & =\frac{(4)(3)(2)(1)}{4} \\
& =6
\end{aligned}
$$

more elements are required,

$$
\begin{aligned}
& \{H H H, H H T\} \cup\{H T H, H T T\} \\
& =\{H H H, H H T, H T H, H T T\} \\
& \{H H H, H H T\} \cup\{T H H, T H T\} \\
& =\{H H H, H H T, T H H, T H T\} \\
& \{H H H, H H T\} \cup\{T T H, T T T\} \\
& =\{H H H, H H T, T T H, T T T\} \\
& \{H T H, H T T\} \cup\{T H H, T H T\} \\
& =\{H T H, H T T, T H H, T H T\} \\
& \{H T H, H T T\} \cup\{T T H, T T T\} \\
& =\{H T H, H T T, T T H, T T T\} \\
& \{T H H, T H T\} \cup\{T T H, T T T\} \\
& =\{T H H, T H T, T T H, T T T\}
\end{aligned}
$$

These additional elements are sufficient to close $\mathcal{F}_{2}$ under compliment and union, it follows that
$\mathcal{F}_{2}=\{\phi,\{H H H, H H T\},\{H T H, H T T\}$, $\{T T H, T T T\},\{T H H, T H T\}$,
$\{H T H, H T T, T H H, T T H, T H T, T T T\}$,
\{HHH, HHT, THH, TTH, THT, TTT 3 ,
\{HHH, HHT, HTH, HTT, THT, TTT \},
\{HHH, HHT, HTH, HTT, THH, TTH\},
\{HHH, HHT, HTH, HTT\},
\{HHH, HHT, THH, THT\},
\{HHH, HHT, TTH, TTT\},
\{HTH, HTT, THH, THT\},
\{HTH, HTT, TTH, TTT\},
$\left\{\right.$ THH, THT, TTH, TTT\}, $\left.\Omega_{3}\right\}$

Now F, will contain all possible outcomes for 3 tosses after 1 toss where

$$
\Omega_{1}=\{H, T\}
$$

It follows that all possible 3 toss outcomes are given by

$$
\begin{aligned}
& \{H H H, H H T, H T H, H T T\}, \\
& \{T H H, T H T, T T H, T T T\}
\end{aligned}
$$

Now

$$
\begin{aligned}
& \{H H H, H H T, H T H, H T T\}^{C} \\
& =\{T H H, T H T, T T H, T T T\} \\
& \{H H H, H H T, H T H, H T T\} \cup \\
& \{T H H, T H T, T T H, T T T\}=\Omega_{3}
\end{aligned}
$$

so $\hat{f}_{1}$ is closed under union and compliment

$$
\begin{array}{r}
\mathcal{F}_{1}=\{\varnothing,\{H H H, H H T, H T H, H T T\}, \\
\left.\{T H H, T H T, T T H, T T T\}, \Omega_{3}\right\}
\end{array}
$$

Thus in summary

$$
\exists_{0} \subset \exists_{1} \subset \exists_{2} \subset \exists_{3}
$$

where

$$
\mathcal{F}_{0}=\left\{\phi, \Omega_{3}\right\}
$$

$\mathcal{F}_{1}=\{\varnothing,\{\mathrm{H} H H, H H T, H T H, H T T\}$, $\left\{T H H, T H T, T T H, T T T \xi, \Omega_{3}\right\}$
$\mathcal{F}_{2}=\{\phi,\{H H H, H H T\},\{H T H, H T T\}$, $\{T T H, T T T\},\{T H H, T H T\}$, $\{H T H, H T T, T H H, T T H, T H T, T T T\}$,
\{HHH, HHT, THH, TTH, THT, TTT\},
\{HHH, HHT, HTH, HTT, THT, TTT \},
\{HHH, HHT, HTH, HTT, THH, TTH\},
\{HHH, HHT, HTH, HTT\},
\{HHH, HHT, THH, THT\},
\{HHH, HHT, TTH, TTT\},
\{HTH, HIT, THH, THT\}, \{HTH, HTT, TTH, TTT\}, \{THH, THT, TTH, TTT\}, $\Omega_{3}$ \}

$$
\mathcal{F}_{3}=2^{\Omega_{3}}
$$

## Basic Properties

Recall the definition of the symmetric random walk. A fair coin,

$$
P(H)=P(T)=1 / 2
$$

is tossed $n$ times with each toss independent of the previoles. The outcomes of the $n$ tosses define a probability space ( $\Omega_{n}, \exists_{n}, P_{n}$ ) where $\Omega_{n}$ cuntains $2^{n}$ samples, $F_{n}=2^{\Omega n}$ and $P_{n}$ is uniform with value

$$
P_{n}(\omega)=(1 / 2)^{n} \quad \forall \omega \in \Omega_{n}
$$

Two random variables are defined

$$
x_{n}(\omega)=\sum_{i=1}^{n} z_{i}(\omega)
$$

where

$$
Z_{i}= \begin{cases}1 & \text { ith toss } H \\ -1 & i \text { th toss } T\end{cases}
$$

and

$$
x_{0}=0
$$

## Independence of Increments

Consider a symmetric random walk of length $n$ where

$$
x_{n}=\sum_{i=0}^{n} z_{i}
$$

where

$$
x_{0}=0
$$

Define an interval of length $m<n$ starting at element $i=0$

$$
x_{n}^{m}=\sum_{i=0}^{m} z_{i}=s_{m}
$$

and an interval of length $R$ where

$$
m+R=n
$$

starting at $i=m+1$ by

$$
X_{n}^{R}=\sum_{i=m+1}^{n} z_{i}=S_{k}
$$

It follows that $x_{n}^{m}$ and $x_{n}^{k}$ do not aorlap.
The desire is to show that

$$
P\left(x_{n}^{m}=s_{m}\right)
$$

and

$$
P\left(X_{n}^{R}=S_{k}\right)
$$

are independent.
Now for each interval the value of the sum will depend on the number of heads and tails in the intersal not the order in which they occur. Let

$$
\begin{aligned}
& m_{H}+m_{T}=m \\
& k_{H}+k_{T}=k
\end{aligned}
$$

It follows that for each interval the number of ways a value of the sum can occur for each interual are given by the binomial coefficients

$$
\begin{aligned}
& \binom{m}{m_{H}}=\frac{m!}{m_{H}!\left(m-m_{H}\right)!}=\frac{m!}{m_{H}!m_{T}!} \\
& \binom{k}{k_{H}}=\frac{k!}{k_{H}!\left(k-k_{H}\right)!}=\frac{k!}{k_{H}!k_{T}!}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& P\left(x_{n}^{m}=s_{m}\right)=\frac{m!}{m_{H}!m_{T}!}\left(\frac{1}{2}\right)^{m} \\
& P\left(x_{n}^{k}=s_{k}\right)=\frac{k!}{k_{H}!k_{T}!}\left(\frac{1}{2}\right)^{k}
\end{aligned}
$$

Since the intersals that define $S_{m}$ and $S_{k}$ do not over lap and the under lying coin tosses are independent it follows that $P\left(x_{n}^{m}=s_{m}\right)$ and $P\left(x_{n}^{k}=s_{k}\right)$ are independent. It follows that

$$
\begin{aligned}
P\left(x_{n}^{m}=s_{m},\right. & \left.x_{n}^{k}=s_{k}\right)= \\
& P\left(x_{n}^{m}=s_{m}\right) P\left(x_{n}^{k}=s_{k}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& P\left(x_{n}^{k}=s_{k} \mid x_{n}^{m}=s_{m}\right)=\frac{P\left(x_{n}^{m}=s_{m}, x_{n}^{k}=s_{k}\right)}{P\left(x_{n}^{m}=s_{m}\right)} \\
& =\frac{P\left(x_{n}^{m}=s_{m}\right) P\left(x_{n}^{k}=s_{k}\right)}{P\left(x_{n}^{m}=s_{m}\right)} \\
& =P\left(x_{n}^{k}=s_{m}\right)
\end{aligned}
$$

Thus the intervals $x_{n}^{m}$ and $x_{n}^{k}$ are independent random variables. This result is true for any non-sverlaping intervals.

## Mean and Variance

In this section the mean and variance of the symetric random walk.

First

$$
E\left(x_{n}\right)=E\left[\sum_{i=0}^{n} z_{n}\right]=\sum_{i=0}^{n} E\left(z_{n}\right)
$$

Now

$$
E\left(Z_{n}\right)=\left(\frac{1}{2}\right)(1)+\left(\frac{1}{2}\right)(-1)=0
$$

Thus

$$
E\left(X_{n}\right)=0
$$

Further the variance is given by

$$
\begin{aligned}
\operatorname{Var}\left(x_{n}\right) & =E\left(x_{n}^{2}\right)-\left[E\left(x_{n}\right)\right]^{2} \\
& =E\left(x_{n}^{2}\right)
\end{aligned}
$$

Since it was previdusly shown that

$$
E\left(X_{n}\right)=0
$$

So

$$
\begin{aligned}
& E\left(X^{2} n\right)=E\left[\left(\sum_{i=1}^{n} z_{i}\right)^{2}\right] \\
& =E\left[\left(\sum_{i=1}^{n} z_{i}\right)\left(\sum_{j=1}^{n} z_{j}\right)\right] \\
& =E\left(\sum_{i=1}^{n} \sum_{j=1}^{n} z_{i} z_{j}\right)
\end{aligned}
$$

$$
=\sum_{i=1}^{n} \sum_{j=1}^{n} E\left(Z_{i} Z_{j}\right)
$$

Now for $i=j$

$$
E\left(Z_{c}^{2}\right)=(1 / 2)(1)+(1 / 2)(1)=1
$$

Now for $i \neq j$

$$
\begin{aligned}
& E\left(z_{i} z_{j}\right)=P\left(z_{i}=1, z_{j}=1\right)(1)(1) \\
+ & P\left(z_{i}=1, z_{j}=-1\right)(1)(-1)+P\left(z_{i}=-1, z_{j}=1\right)(-1)(1) \\
+ & P\left(z_{i}=-1, z_{j}=-1\right)(-1)(-1)
\end{aligned}
$$

Since $Z_{i}$ and $Z_{j}$ are independent for $i \neq j$

$$
\begin{aligned}
P\left(z_{i}=1, z_{j}=1\right) & =P\left(z_{i}=1\right) P\left(z_{j}=1\right) \\
& =(1 / 2)(1 / 2) \\
& =1 / 4 \\
P\left(z_{i}=1, z_{j}=-1\right) & =(1 / 2)(1 / 2)=1 / 4 \\
P\left(z_{i}=-1, z_{j}=1\right) & =(1 / 2)(1 / 2)=1 / 4 \\
P\left(z_{i}=-1, z_{j}=-1\right) & =(1 / 2)(1 / 2)=1 / 4
\end{aligned}
$$

Thus

$$
\begin{aligned}
E\left(z_{i} z_{j}\right) & =(1 / 4)+(-1 / 4)+(-1 / 4)+(1 / 4) \\
& =0
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
E\left(x_{n}^{2}\right) & =\sum_{i=1}^{n} E\left(z_{i}\right)+\sum_{i \neq j}^{n} E\left(z_{i} z_{j}\right) \\
& =\sum_{i=1}^{n} 1 \\
& =n
\end{aligned}
$$

In summary

$$
\begin{aligned}
& E\left(x_{n}\right)=0 \\
& \operatorname{Var}\left(x_{n}\right)=n
\end{aligned}
$$

## Conditional Expectation for $n=2$

In this section the conditional expectation of the symmetric random walk will be explicitly evaluated for $n=2$ using the results previously obtained for $\Omega_{1}$ and $\Omega_{2}$

$$
\begin{aligned}
& \Omega_{1}=\{H, T\} \\
& \Omega_{2}=\{H H, H T, T H, T T\}
\end{aligned}
$$

and the filtration,

$$
\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2}
$$

where

$$
\begin{aligned}
& \mathcal{F}_{0}=\left\{\phi, \Omega_{2}\right\} \\
& \mathcal{F}_{1}=\left\{\phi,\{H H, H T\},\left\{T H_{1} T T\right\}, \Omega_{2}\right\}
\end{aligned}
$$

$$
\begin{aligned}
\mathcal{F}_{2}= & \{\Phi, H H, H T, T H, T T,\{H T, T H, T T\}, \\
& \{H H, T H, T T\},\{H H, H T, T T\}, \\
& \{H H, H T, T H\},\{H H, H T\},\{T H, T T\} \\
& \{H H, T H\},\{H T, T T\},\{H H, T T\}, \\
& \{H T, T H\}, \Omega\}
\end{aligned}
$$

The conditional expectation calculation to be performed is the expected value of $X_{2}$ given the $\sigma$-fied $\hat{J}_{1}$ which is part of $\mathcal{F}_{2}$ filtration, namely

$$
E\left(x_{2} \mid \mathcal{F}_{1}\right)=\frac{1}{P(A)} \int_{A} x d P
$$

where

$$
A \in \mathcal{F}_{1}
$$

Now $F_{1}$ has two atomic events so the expectation takes on two values

$$
\{H H, H T\},\{T H, T T\}
$$

It is seen that

$$
\{H H, H T\} \cup\{T H, T T\}=\Omega_{2}
$$

The first event represents tossing heads on first toss and the second tossing tails on first toss.
Also for, $\omega \in \Omega_{2} \quad P(\omega)=1 / 4$, so

$$
\begin{aligned}
& P(\{H H, H T \xi)=1 / 2 \\
& P(\{T H, T T \xi)=1 / 2
\end{aligned}
$$

and

$$
\begin{array}{ll}
X_{2}(H H)=2 & X_{2}(H T)=0 \\
X_{2}(T H)=0 & X_{2}(T T)=-2
\end{array}
$$

For the first event let

$$
A=\{H H, H T\}
$$

This event represents the case where

$$
X_{1}(H)=1
$$

$$
\begin{aligned}
& E\left(X_{2} \mid \xi_{1}\right)(\{H H, H T\})= \\
& \frac{1}{P(\{H H, H T \xi)} \frac{\left[X_{2}(H H) P\left(X_{2}=2 \mid \xi H H, H T \xi\right)\right.}{\left.\quad+X_{2}(H T) P\left(X_{2}=0 \mid \xi H H, H T \xi\right)\right]} \\
& =\frac{1}{(1 / 2)}[2(14)+O(44)] \\
& =1=X_{1}(H)
\end{aligned}
$$

And for the second event

$$
A=\left\{T H_{1} T T\right\}
$$

this event represents the case where

$$
\begin{gathered}
X_{1}(T)=-1 \\
E\left(X_{2} \mid F_{1}\right)(\{T H, T T\}) \\
=\frac{1}{P(\{T H, T T\})}\left[X_{2}(T H) P\left(X_{2}=0 \mid\{T H, T T\}\right)\right. \\
\left.+X_{2}(T T) P\left(X_{2}=-2 \mid\{T H, T T\}\right)\right] \\
=\frac{1}{(1 / 2)}[O(14)-2(1 / 4)]
\end{gathered}
$$

$$
=-1=X_{1}(T)
$$

In summary

$$
\begin{aligned}
& E\left(X_{2} \mid \mathcal{F}_{1}\right)(\{H H, H T\})=1=X_{1}(H) \\
& E\left(X_{2} \mid \mathcal{F}_{1}\right)(\{T H, T T\})=-1=X_{1}(T)
\end{aligned}
$$

Thus

$$
E\left(x_{2} \mid \mathcal{F}_{1}\right)=x_{1}
$$

## Conditional Expectation $n=3$

In this sections the conditional expectation for the symetric random walk will be evaluated for $n=3$. Using the previously obtained results for $\Omega_{1}, \Omega_{2}$ and $\Omega_{3}$

$$
\begin{aligned}
& \Omega_{1}=\{H, T\} \\
& \Omega_{2}=\{H H, H T, T H, T T\} \\
& \Omega_{3}=\{H H H, H H T, H T H, H T T, \\
& T H H, T H T, T T H, T T T\}
\end{aligned}
$$

and the filtration

$$
\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \mathcal{F}_{3}
$$

where

$$
\begin{gathered}
\mathcal{F}_{0}=\left\{\phi, \Omega_{3}\right\} \\
\mathcal{F}_{1}=\{\phi,\{H H H, H H T, H T H, H T T\}, \\
\left.\{T H H, T H T, T T H, T T T\}, \Omega_{3}\right\}
\end{gathered}
$$

$$
\begin{aligned}
\mathcal{F}_{2}= & \{\phi,\{H H H, H H T\},\{H T H, H T T\}, \\
& \{T T H, T T T\},\{T H H, T H T\}, \\
& \{H T H, H T T, T H H, T T H, T H T, T T T\}, \\
& \{H H H, H H T, T H H, T T H, T H T, T T T\}, \\
& \{H H H, H H T, H T H, H T T, T H T, T T T\}, \\
& \{H H H, H H T, H T H, H T T, T H H, T T H\}, \\
& \{H H H, H H T, H T H, H T T\}, \\
& \{H H H, H H T, T H H, T H T\}, \\
& \{H H H, H H T, T T H, T T T\}, \\
& \{H T H, H T T, T H H, T H T\}, \\
& \{H T H, H T T, T T H, T T T\}, \\
& \left.\{T H H, T H T, T T H, T T T\}, \Omega_{3}\right\} \\
& \mathcal{F}_{3}=2^{\Omega}
\end{aligned}
$$

The conditional expectation calculation to be performed is the expected value of $x_{3}$ given
the 6 -field $\mathcal{F}_{2}$ which is part of $\mathcal{F}_{3}$ filtration, namely

$$
E\left(x_{3} \mid F_{2}\right)=\frac{1}{P(A)} \int_{A} x d P
$$

where

$$
A \in \mathcal{F}_{2}
$$

Now $F_{2}$ has four atomic events so the expectation takes on four values
\{HHH, HHT\}, \{HTH, HTT\}, \{TTH, TTT\}, \{THH, THT\}
These events describe every outcome of three tosse given that two tosses have been performed. Now for every $\omega \in \Omega_{3} \quad P(\omega)=1 / 8$. It follows that

$$
\begin{aligned}
& P(\{H H H, H H T\})=1 / 4 \\
& P(\{H T H, H T T\})=1 / 4
\end{aligned}
$$

$$
\begin{aligned}
& P(\{T T H, T T T\})=1 / 4 \\
& P(\{T H H, T H T\})=1 / 4
\end{aligned}
$$

For each wt $\Omega_{3} \quad X_{3}(\omega)$ has the values

$$
\begin{array}{ll}
X_{3}(H H H)=3 & X_{3}(H H T)=1 \\
X_{3}(H T H)=1 & X_{3}(H T T)=-1 \\
X_{3}(T T H)=-1 & X_{3}(T T T)=-3 \\
X_{3}(T H \mid H)=1 & X_{3}(T H T)=-1
\end{array}
$$

For the first element let

$$
\begin{gathered}
A=\{H H H, H H T\} \\
E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{H H H, H H T \xi)= \\
P\left(\frac{1}{\{H H H, H H T \xi)} \int x d P\right. \\
=\frac{1}{(1 / c l)}\left[(1 / 8) X_{3}(H H H H, H H T\}+(1 / 8) X_{3}(H H T)\right]
\end{gathered}
$$

$=(1 / 2)(3+1)=2=X_{2}(H H)$
Next let

$$
\begin{gathered}
A=\{H T H, H T T\} \\
E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{H T H, H T T\})= \\
P\left(\frac{1}{\{H T H, H T T\}} \iint_{\{H T H, H T T\}} x d P\right. \\
=\frac{1}{(1 / 4)}\left[(1 / 8) X_{3}(H T H)+(1 / 8) X_{3}(H T T)\right] \\
=(1 / 2)(1-1)=0=X_{2}(H T)
\end{gathered}
$$

and next let

$$
\begin{gathered}
A=\{T T H, T T T\} \\
E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{T T H, T T T\})= \\
P\left(\frac{1}{\{T T H, T T T\}} \int S_{T T H, T T T\}} x d P\right.
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{1}{(1 / 4)}\left[(1 / 8) X_{3}(T T H)+(1 / 8) X_{3}(T T T)\right] \\
& =(1 / 2)(-1-3)=-2=X_{2}(T T)
\end{aligned}
$$

and finally let

$$
\begin{aligned}
& A=\{T H H, T H T\} \\
& E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{T H H, T H T\})= \\
& P\left(\frac{1}{\{T H H, T H T\}} \iint_{\{T H, T H T\}} x d P\right. \\
& =\frac{1}{\left(1 / c_{1}\right)}\left[(1 / 8) X_{3}(T H H H)+(1 / 8) X_{3}(T H T)\right] \\
& =(1 / 2)(1-1)=0=X_{2}(T H)
\end{aligned}
$$

In summary

$$
\begin{aligned}
& E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{H H H, H H T\})=2=X_{2}(H H) \\
& E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{H T H, H T T\})=0=X_{2}(H T)
\end{aligned}
$$

$E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{T T H, T T T\})=-2=X_{2}(T T)$
$E\left(X_{3} \mid \mathcal{F}_{2}\right)(\{T H H, T H T\})=0=X_{2}(T H)$

$$
E\left(x_{3} \mid \mathcal{F}_{2}\right)=x_{2}
$$

Finally consider

$$
E\left(x_{3} \mid \mathcal{F}_{1}\right)=\frac{1}{P(A)} \int_{A} x d P
$$

where

$$
A \in \mathcal{F}_{1}
$$

Now $F_{1}$ has two atomic events

$$
\begin{aligned}
& \{H H H, H H T, H T H, H T T\} \\
& \{T H H, T H T, T T H, T T T\}
\end{aligned}
$$

where

$$
\begin{aligned}
& P(\{H H H, H H T, H T H, H T T \xi)=1 / 2 \\
& P(\{T H H, T H T, T T H, T T T \xi)=1 / 2
\end{aligned}
$$

First let

$$
A=\{H H H, H H T, H T H, H T T\}
$$

then
$E\left(X_{3} \mid \mathcal{F}_{1}\right)(\xi H H H, H H T, H T H, H T T \xi)=$

$$
\begin{aligned}
& \frac{1}{P(\{H H H, H H T, H T H, H T T \xi)} \int_{A} X d P \\
& =\frac{1}{(1 / 2)}\left[(1 / 8) X_{3}(H H H)+(1 / 8) X_{3}(H H T)\right. \\
& \left.+(1 / 8) X_{3}(H T H)+(1 / 8) X_{3}(H T T)\right] \\
& =\left(\frac{1}{4}\right)(3+1+1-1)=1=X_{1}(H)
\end{aligned}
$$

Next let

$$
A=\{T H H, T H T, T T H, T T T\}
$$

then
$E\left(X_{3} \mid \mathcal{F}_{1}\right)(\{T H H, T H T, T T H, T T T\})=$
$P(\{T H H, T H T, T T H, T T T \xi)$ A $\mathrm{A} d \mathrm{l}$

$$
\begin{aligned}
=\frac{1}{(1 / 2)}\left[(1 / 8) X_{3}(T H H)+(1 / 8) X_{3}(T H T)\right. \\
\left.+(1 / 8) X_{3}(T T H)+(1 / 8) X_{3}(T T T)\right]
\end{aligned}
$$

$=(1 / 4)(1-1-1-3)=-1=X_{1}(T)$
In summary

$$
\begin{gathered}
E\left(X_{3} \mid \mathcal{F}_{1}\right)(\{H H H, H H T, H T H, H T T \xi)=1 \\
=X_{1}(H) \\
E\left(X_{3} \mid \mathcal{F}_{1}\right)(\xi T H H, T H T, T T H, T T T \xi)=-1 \\
=X_{1}(T) \\
E\left(X_{3} \mid \mathcal{F}_{1}\right)=X_{1}
\end{gathered}
$$

## Martingale Property

To show that the symmetric random walk is a martingale it must be shown that

1) $E\left(\left|X_{n}\right|\right)<$ For each $n=1,2,3 \ldots$.
2) $x_{1}, x_{2}, x_{3}, \ldots$ is adapted to the fittration $\mathcal{F}_{1}, \mathcal{F}_{2}, \mathcal{F}_{3}, \ldots$
3) $E\left(x_{n+1} \mid F_{n}\right)=x_{n}$ for each
$n=1,2,3, \ldots$
Now for (1)

$$
\begin{aligned}
E\left(\left|X_{n}\right|\right) & =E\left(\left|\sum_{i=1}^{n} Z_{n}\right|\right) \\
& \leqslant E\left(\sum_{i=1}^{n}\left|Z_{n}\right|\right) \\
& =\sum_{i=1}^{n} E\left(\left|Z_{n}\right|\right) \\
& =\sum_{i=1}^{n} 1=n
\end{aligned}
$$

Thus

$$
E\left(\left|x_{n}\right|\right) \leq n<\infty
$$

so property (1) is satisfied.
For property (2) for each $i=1,2,3, \ldots$ by defintion of the process for $\omega \in \Omega_{n}, X_{n}(\omega)=X$ is defined thus

$$
\left\{\omega \in \Omega_{n}: X_{n}(\omega) \leqslant x\right\} \in \mathcal{F}_{n}
$$

thus for each sample in $\Omega_{n} x_{n}(\omega) \leqslant x$ defines events $\omega$ such that $\omega \in \mathcal{F}_{n}$. It follows that for each value of $X_{n}$ has a probability measure defaned on an event in $F_{n}$. Thus $x_{n}$ is $F_{n}$ adapled for each $n$ so property (2) is satisfied.
Finally for property (3)

$$
E\left(x_{n+1} \mid \mathcal{F}_{n}\right)=E\left(x_{n+1}-x_{n}+x_{n} \mid \mathcal{F}_{n}\right)
$$

$$
=E\left(X_{n+1}-X_{n} \mid I_{n}\right)+E\left(X_{n} \mid I_{n}\right)
$$

Now from property (2) since $X_{n}$ is $\mathcal{F}_{n}$ adapted

$$
E\left(X_{n} \mid \mathcal{F}_{n}\right)=X_{n}
$$

Previously it was shown that non overlapping intervals of the symmetric rardom walk are independent. Thus the interval $x_{n+1}-x_{n}$ is independent of $F_{n}$. It follows that

$$
\begin{aligned}
& E\left(X_{n+1}-X_{n} \mid F_{n}\right)=E\left(X_{n+1}-X_{n}\right) \\
& =E\left(X_{n+1}\right)-E\left(X_{n}\right) \\
& =0
\end{aligned}
$$

thus

$$
\begin{aligned}
& E\left(x_{n}+1\right)\left(\Im_{n}\right) \\
&=E\left(x_{n+1}-x_{n}\left(\Im_{n}\right)+E\left(x_{n} \mid \Im_{n}\right)\right. \\
&=0+x_{n}
\end{aligned}
$$

and

$$
E\left(x_{n+1} \mid F_{n}\right)=x_{n}
$$

This general result is consistent with the explicit calculation for $n=2$ and $n=3$ performed in a previous section.
It follows that the symetric random walk satisfres all three matingale properties so it is a martingale.

## Simple Random Walk

A simple random walk is a discrete time stochastic processes defined is a more general version of the symetric random walk previously discussed. For the symmetric random walk a random variable can take on values 1 or - 1 with equal probabilities. In the more general version the probabilities are not equal. consider the random variable

$$
Z_{i}=\{1,-1\} \quad i=0,1,2,3, \ldots
$$

where

$$
P\left(z_{i}=1\right)=p \quad P\left(z_{i}=-1\right)=1-p=9
$$

let

$$
x_{n}=\sum_{i=0}^{n} z_{i}
$$

where

$$
x_{0}=0
$$

and the $z_{i}$ are independent.
The simple random walk can be visualized as a tree that grows with each step.
The following plot shows all possible paths with the probability of realizing the path labeled
$\begin{array}{lllllllll}-4 & -3 & -2 & -1 & 0 & 1 & 2 & 3 & 4\end{array}$
$n=0$
$n=1 \quad q^{2} \quad q p \quad p q \quad p^{2}$
$n=2 \quad q^{3} \quad q^{2} p q^{2} p \quad p^{2} q p^{2} q$
$n=3 \quad q^{4} \quad q^{3} p q^{3} p \quad q^{2} p^{2} p^{2} q^{2} \quad p^{3} q p^{3} q \quad p^{4}$
$n=4 \quad q^{4} p q^{4} p \quad q^{3} p q^{3} p \quad q^{2} p^{3} p^{3} q^{2} \quad p^{4} q p^{4} q$
$n=5$
$n=6$

## Passage Probabilities

A passage probabilitly is the probability that $X_{n}$ will reach some value eventualy. For exaple what is the probability that $x_{n}=1$. All poths to $x_{n}=1$ with in $n=5$ are shown in the figure

$$
\begin{array}{lllllllll}
-4 & -3 & -2 & -1 & 0 & 1 & 2 & 3 & 4
\end{array}
$$

$n=0$
$n=1$
$n=2$
$n=3 \quad q^{4} \quad q^{3} p \quad q^{3} p \quad q^{2} p^{2} p^{2} q^{2} \quad p^{3} q p^{3} q \quad p^{4}$
$n=4 \quad q^{4} p q^{4} p \quad q^{3} p q^{3} p \quad q^{2} p^{3} p^{3} q^{2} \quad p^{4} q p^{4} q$
$n=5$
$n=6$

The process can reach $x_{n}=1$ in 1,3 and 5 steps and there are 2 ways to reach $x_{n}=1$ in 5 steps. The probability of reaching $x_{n}=1$ in 5 steps is given by,

$$
P_{1}=p+p^{2} q+2 p^{3} q^{2}
$$

## Quadradic Variation of Brownian Motion

Consider a probability space $\left.(\Omega,\}_{1} P\right)$ and let $\left\{B_{t}: t \geqslant 0\right\}$ be a Brownian Motion stochastic process. Show that Brownian motion has a finite quadratic variation

$$
\langle B, B\rangle_{t}=\lim _{n \rightarrow \infty} \sum_{i=1}^{\infty}\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2}=t
$$

where

$$
t_{i}=\frac{i t}{n} \quad t_{0}=0<t_{1}<t_{2}<\cdots<t
$$

and show that

$$
\left(d B_{t}\right)^{2}=d t
$$

Now Brownian Motion is defined by independent Normally distributed increments

$$
\Delta B_{t_{i}}=B_{t_{i}}-B_{t_{i-1}} \sim N(0, t / n)
$$

It follows that

$$
\begin{aligned}
& E\left(\Delta B_{t_{i}}\right)=0 \\
& E\left(\Delta B_{t_{i}}^{2}\right)=\frac{t}{n} \\
& E\left(\Delta B_{t_{i}}^{4}\right)=\frac{3 t^{2}}{n^{2}}
\end{aligned}
$$

Now the expectation of the quadratic variation is given by

$$
\begin{aligned}
& E\left[\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right]=\lim _{n \rightarrow \infty} \sum_{i=1}^{n} E\left(\Delta B_{t_{i}}^{2}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \frac{t}{n}=\lim _{n \rightarrow \infty} \frac{n t}{n} \\
& =t
\end{aligned}
$$

To show convergence of the quadratic variation to expectation value it must be shown that it converges in probability, namely

$$
\lim _{n \rightarrow \infty} P\left[\left|\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right)-t\right|>\delta\right]=0
$$

That is the probability that the absolute value of the difference between the quadratic variation and its expectation value is greater than an arbitrary positive number is zero
Now recall the chebyshes inequality

$$
P(|\bar{x}-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

Let

$$
\bar{X}=\sum_{i=1}^{n} \Delta B_{i}^{2}
$$

then

$$
\begin{aligned}
\mu & =E(\underline{X})=E\left[\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right] \\
& =t
\end{aligned}
$$

Plugging this into the Chelbyshev gives

$$
\begin{aligned}
& P\left(\left|\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}-t\right|>\delta\right) \\
& \quad \leqslant \frac{1}{\delta^{2}} \operatorname{Var}\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right)
\end{aligned}
$$

To go flortur the righthand side must be evaluated,

$$
\begin{aligned}
& \operatorname{var}\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right)=E\left[\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}-t\right)^{2}\right] \\
& =E\left[\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}-t\right)\left(\sum_{j=1}^{n} \Delta B_{t_{j}}^{2}-t\right)\right] \\
& =E\left[\sum_{i=1}^{n} \sum_{j=1}^{n} \Delta B_{t_{i}}^{2} \Delta B_{t_{j}}^{2}-2 t \sum_{i=1}^{n} \Delta B_{t_{i}}^{2}+t^{2}\right] \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n} E\left(\Delta B_{t_{i}}^{2} \Delta B_{t_{j}}^{2}\right)-2 t \sum_{i=1}^{n} E\left(\Delta B_{t_{i}}^{2}\right) \\
& \quad+E\left(t^{2}\right)
\end{aligned}
$$

Now

$$
E\left(\Delta B_{t_{i}}^{2}\right)=\frac{t}{n}
$$

and

$$
E\left(t^{2}\right)=t^{2}
$$

For the first term consider $i \neq j$ and use the cossumption that $\Delta B_{t_{i}}$ is independent of $\Delta B_{t j}$ so that

$$
\begin{aligned}
E\left(\Delta B_{t_{i}}^{2} \Delta B_{t_{j}}^{2}\right) & =E\left(\Delta B_{t_{i}}^{2}\right) E\left(\Delta B_{t_{j}}^{2}\right) \\
& =\left(\frac{t}{n}\right)\left(\frac{t}{n}\right) \\
& =\frac{t^{2}}{n^{2}}
\end{aligned}
$$

next for $i=j$

$$
E\left(\Delta B_{t_{i}}^{4}\right)=\frac{3 t^{2}}{n^{2}}
$$

Putting things together

$$
\begin{aligned}
\operatorname{Var} & \left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right)=\sum_{i=1}^{n} \sum_{j=1}^{n} E\left(\Delta B_{t_{i}}^{2} \Delta B_{t_{j}}^{2}\right) \\
- & 2 t \sum_{i=1}^{n} E\left(\Delta B_{t_{i}}^{2}\right)+E\left(t^{2}\right) \\
= & \sum_{i=1}^{n} \sum_{i \neq j}^{n} E\left(\Delta B_{t_{i}}^{2} \Delta B_{t_{j}}^{2}\right)+\sum_{i=1}^{n} E\left(\Delta B_{t_{i}}^{4}\right) \\
- & 2 t \sum_{i=1}^{n} E\left(\Delta B_{t_{i}}^{2}\right)+E\left(t^{2}\right) \\
= & \sum_{i=1}^{n} \sum_{j=1}^{n}\left(\frac{t^{2}}{n^{2}}\right)+\sum_{i=1}^{n}\left(\frac{3 t^{2}}{n^{2}}\right)-2 t \sum_{i=1}^{n}\left(\frac{t}{n}\right) \\
& +t^{2} \\
= & \left(\frac{t^{2}}{n^{2}}\right) n(n-1)+\frac{3 t^{2}}{n}-2 t^{2}+t^{2} \\
= & t^{2}\left[\frac{n(n-1)}{n^{2}}+\frac{3}{n}-1\right] \\
= & t^{2}\left(\frac{n^{2}}{n^{2}}-\frac{1}{n}+\frac{3}{n}-1\right)
\end{aligned}
$$

$$
\begin{aligned}
& =t^{2}\left(1+\frac{2}{n}-1\right) \\
& =\frac{2 t^{2}}{n}
\end{aligned}
$$

thus

$$
\operatorname{Var}\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right)=\frac{2 t^{2}}{n}
$$

Returning to the Cheloysher inequality

$$
\begin{aligned}
P(\mid & \left.\left|\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}-t\right|>\delta\right) \\
& \leqslant \frac{1}{\delta^{2}} \operatorname{Var}\left(\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}\right) \\
& =\frac{1}{\delta^{2}}\left(\frac{2 t^{2}}{n}\right)
\end{aligned}
$$

and finally to prove convergence in probability in the Imit $n \rightarrow \infty$ for fixed $\delta$

$$
\begin{gathered}
\lim _{n \rightarrow \infty} P\left(\left|\sum_{i=1}^{n} \Delta B_{t_{i}}^{2}-t\right|>\delta\right) \\
\leqslant \lim _{n \rightarrow \infty} \frac{1}{\delta^{2}}\left(\frac{2 t^{2}}{n}\right) \\
=0
\end{gathered}
$$

Thus

$$
\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \Delta B_{t_{i}}^{2}=t
$$

converges in probability.
Now

$$
\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \Delta B_{t_{i}}^{2}=\int_{0}^{t} d B_{t}^{2}=t
$$

but

$$
\begin{aligned}
& t=\int_{0}^{t} d s=\int_{0}^{t} d B_{t}^{2} \\
& \Rightarrow \int_{0}^{t}\left(d s-d B_{t}^{2}\right)=0 \\
& \Rightarrow d t=d B_{t}^{2}
\end{aligned}
$$

## The Its Inlegral

Consider the integral

$$
I_{[a, b]}(f)=\int_{a}^{b} f\left(s, B_{s}\right) d B_{s}
$$

where $B_{t}$ is Brownian Motion Now $B_{t}$ is not differentiable so it is not possible to write

$$
d B_{t}=\frac{d B_{1}}{d t} d t
$$

To interpret the integral approximate $f(t)$ as a simple function expansion over the partition

$$
\left(t_{0}, t_{1}, \ldots, t_{n-1}, t_{n}\right)
$$

where

$$
\begin{aligned}
0 \leqslant t_{1} & \leqslant \cdots \leqslant t_{n-1} \leqslant t_{n} \\
t_{i} & =\frac{i t}{n}
\end{aligned}
$$

and define the indicator function

$$
\mathbb{1}_{\left[t_{j-1}, t_{j}\right]}=\left\{\begin{array}{ll}
1 & t_{j-1} \leqslant t \leqslant t_{j} \\
0 & t<t_{j-1},
\end{array} t>t_{j}\right.
$$

then the simple function exponsion appoximating $f(t)$ is given by

$$
f\left(t, B_{t}\right)=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} e\left(B_{t j}\right) \mathbb{1}_{\left[t_{j-1}, t_{j}\right]}
$$

where $e\left(B_{t_{j}}\right)$ is a constant value of $f\left(t, B_{j}\right)$ over the interval $t_{j-1} \leqslant t \leqslant t_{j}$ Exactly which value of $t_{j-1} \leqslant t \leqslant t_{j}$ is unspecified. Thus for each intervat

$$
\begin{aligned}
& \int_{t_{j-1}}^{t_{j}} f\left(s, B_{s}\right) d B_{s}=\int_{t_{j-1}}^{t_{j}} e\left(B_{t_{j}}\right) d B_{s} \\
& =e\left(B_{t_{j}}\right) \int_{t_{j-1}}^{t_{j}} d B_{s} \\
& =e\left(B_{t_{j}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)
\end{aligned}
$$

$$
\begin{aligned}
& I_{[0, t]}(f)=\int_{0}^{t} f\left(s, B_{s}\right) d B_{s} \\
& =\lim _{n \rightarrow \infty} \int_{0}^{t}\left[\sum_{j=1}^{n} e\left(B_{t_{j}}\right) I_{1}\left[t_{j-1}, t_{j}\right]\right] d B_{s} \\
& =\lim _{n \rightarrow \infty} \sum_{j=1}^{n}\left[\int_{t_{j-1}}^{t_{j}} e\left(B_{t_{j}}\right) d B_{s}\right] \\
& =\lim _{n \rightarrow \infty} \sum_{j=0}^{n-1} e\left(B_{t_{j}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)
\end{aligned}
$$

To go furthur e( $B_{t_{j}}$ ) needs to be determined. By definition it is a value of $f\left(t, B_{t}\right)$ on the interval $t_{j-1} \leqslant t \leqslant t_{j}$. There are two popular choices. The first assumes the left most value on the interval,

$$
e\left(B_{t_{j-1}}\right)=f\left(t_{j-1}, B_{t_{j-1}}\right)
$$

and the second assumes the mid point of the interval

$$
e\left(B_{t_{j}}, B_{t_{j-1}}=f\left(\frac{1}{2}\left(t_{j}-t_{j-1}\right), \frac{1}{2}\left(B_{t_{j}}-B_{t_{j-1}}\right)\right.\right.
$$

The first is the Itco integral and the second the stratonouich integral. Here the bous is on the Itरी integral.
As an example consider

$$
f\left(t, B_{t}\right)=B_{t}
$$

then

$$
f\left(t, B_{t}\right)=B_{t}=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} B_{t j} \mathbb{1}_{\left[t_{j-1}, t_{j}\right]}
$$

It follows that
$\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}=\int_{0}^{t} B_{s} d B_{s}$
$=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right)$

Now

$$
\begin{aligned}
& \left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}=B_{t_{j}}\left(B_{t_{j}}-B_{t_{j-1}}\right)-B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right) \\
& \Rightarrow B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right)=B_{t_{j}}\left(B_{t_{j}}-B_{t_{j-1}}\right)-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2} \\
& =B_{t_{j}}^{2}-B_{t_{j}} B_{t_{j-1}}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2} \\
& A l s o, \\
& \left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}=B_{t_{j}}^{2}+B_{t_{j-1}}^{2}-2 B_{t_{j}} B_{t_{j-1}} \\
& B_{t_{j}} B_{t_{j-1}}=\frac{1}{2}\left[B_{t_{j}}^{2}+B_{t_{j-1}}^{2}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}\right] \\
& \text { It follows that } \\
& B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right)=B_{t_{j}}^{2}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2} \\
& -\frac{1}{2}\left[B_{t_{j}}^{2}+B_{t_{j-1}}^{2}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}\right] \\
& =\frac{1}{2}\left[B_{t_{j}}^{2}-B_{t_{j-1}}^{2}-\left(B_{t_{j}}-B t_{j-1}\right)^{2}\right]
\end{aligned}
$$

Thus

$$
\begin{aligned}
\lim _{n \rightarrow \infty} & \sum_{j=1}^{n} B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right) \\
= & \lim _{n \rightarrow \infty} \sum_{j=1}^{n} \frac{1}{2}\left[B_{t_{j}}^{2}-B_{t_{j-1}}^{2}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}\right]
\end{aligned}
$$

Now for the first two terms

$$
\begin{aligned}
\sum_{j=1}^{n} & B_{t_{j}}^{2}-B_{t j-1}^{2}=B^{2} t_{t_{1}}-B_{t_{0}}^{2}+B_{t_{2}}^{2}-B_{t_{1}}^{2} \\
& +B_{t_{3}}^{2}-B_{t_{2}}^{2}+\cdots B_{t_{n-1}}^{21}-B_{t_{n-2}}^{2} \\
& +B_{t_{n}}^{2}-B_{t_{n-1}}^{2} \\
& =B_{t_{n}}^{2}-B_{t_{0}}^{2}
\end{aligned}
$$

From the definition of Brownian motion

$$
B_{t_{0}}=0
$$

and

$$
t_{n}=t
$$

so

$$
\sum_{j=1}^{n} B_{t_{j}}^{2}-B_{t_{j-1}}^{2}=B_{t}^{2}
$$

The last term is the quadratic variation which was evaluated in the prevous section

$$
\lim _{n \rightarrow \infty} \sum_{j=1}^{n}\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}=t
$$

Bringing things together gives

$$
\begin{aligned}
& \int_{0}^{t} B_{s} d B_{s}=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} B_{t_{j-1}}\left(B_{t_{j}}-B_{t_{j-1}}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \frac{1}{2}\left[B_{t_{j}}^{2}-B_{t_{j-1}}^{2}-\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}\right] \\
& =\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \frac{1}{2}\left(B_{t_{j}}^{2}-B_{t_{j-1}}^{2}\right) \\
& \quad-\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \frac{1}{2}\left(B_{t_{j}}-B_{t_{j-1}}\right)^{2}
\end{aligned}
$$

$$
=\frac{1}{2}\left(B_{t}^{2}-t\right)
$$

Thus

$$
\int_{0}^{t} B_{s} d B_{s}=\frac{1}{2}\left(B_{t}^{2}-t\right)
$$

## Itô Isometry

Next a general relation for the second moment will be derived. This property is reforred to as Itô Isometry, namely

$$
\begin{aligned}
& E\left[\left(\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right] \\
& =E\left[\int_{0}^{t} f\left(s, B_{s}\right)^{2} d s\right]
\end{aligned}
$$

To prove this consides the second moment of the Itरे integral,

$$
\begin{aligned}
& E\left[\left(\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right] \\
= & \lim _{n \rightarrow \infty} E\left[\left(\sum_{j=1}^{n} \int_{t_{j}-1}^{t_{j}} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right]
\end{aligned}
$$

$$
\begin{aligned}
&=\lim _{n \rightarrow \infty} E {\left[\left(\sum_{j=1}^{n} e\left(B_{t_{j-1}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)\right)^{2}\right] } \\
&=\lim _{n \rightarrow \infty} E {\left[\sum_{j=1}^{n} \sum_{i=1}^{n} e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\right.} \\
&\left.\left(B_{t_{j}}-B_{t_{j-1}}\right)\left(B_{t_{i}}-B t_{i-1}\right)\right] \\
&=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \sum_{i=1}^{n} E\left[e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\right. \\
&\left.\left(B_{t_{j}}-B_{t_{j-1}}\right)\left(B_{t_{i}}-B t_{i-1}\right)\right]
\end{aligned}
$$

Consider the case $j<i-1$
$E\left[e\left(B_{t j-1}\right) e\left(B_{t i-1}\right)\left(B_{t j}-B t_{j-1}\right)\left(B_{t i}-B t_{i-1}\right)\right]$
and consider the 6 -algebra at $t_{i-1}, \mathcal{F}_{t i-1}$, and since $j<i-1$ it follows that

$$
\mathcal{F}_{t_{j-1}} \subset \mathcal{F}_{t_{j}} \subset \mathcal{F}_{t_{i-1}}
$$

Now conditioning on $\mathfrak{F}_{t i-1}$ gues

$$
\begin{aligned}
& E\left[E\left[e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right) \mid \mathcal{F}_{t_{i-1}}\right]\right] \\
& =E\left[e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right)\right]
\end{aligned}
$$

Eualuation of the conditional expectation gives
$E\left[e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right)\left(B_{t_{i}-} B_{t_{i-1}}\right) \mid \mathcal{F}_{t_{i-1}}\right]$
$=e\left(B_{t_{j-1}}\right) e\left(B_{t_{i-1}}\right)\left(B_{t_{j}}-B_{t_{j-1}}\right) E\left[\left(B_{t_{i}}-B_{t_{i-1}}\right) 1 \mathcal{F}_{t_{i-1}}\right]$ which follows since $B_{t_{j-1}}$, $B_{t-1}$ and $B_{t j}$ are $\mathcal{F}_{t i-1}$ measurable.
Now for the remaining expectation

$$
\begin{gathered}
E\left[\left(B_{t_{i}}-B_{t_{i-1}}\right) \mid \mathcal{F}_{t_{i-1}}\right] \\
=E\left[\left(B_{t_{i}}-B_{t_{i-1}}\right)\right] \\
=0
\end{gathered}
$$

where the first step follows from independence of increments of Brownian Motion and
the last from the definition of Brownian motion which assume the increments have zero mean. Thus for $j \leq i-1$

$$
\begin{aligned}
& E\left[e\left(B_{t j-1}\right) e\left(B_{t i-1}\right)\left(B_{t j}-B_{t j-1}\right)\left(B_{t i} \cdot B_{t i-1}\right)\right] \\
& =0
\end{aligned}
$$

similarly for $i<j-1$

$$
\begin{aligned}
& E\left[e\left(B_{t j-1}\right) e\left(B_{t i-1}\right)\left(B_{t j}-B_{t j-1}\right)\left(B_{t i}-B_{t i-1}\right)\right] \\
& =0
\end{aligned}
$$

It follows that the only nonzero terms in the sum have
$i-1=j-1 \Rightarrow i=j$, so now conside those terms

$$
E\left[e^{2}\left(B_{t_{i-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2}\right]
$$

once again conditioning on $\exists_{t_{i-1}}$ gives

$$
\begin{aligned}
E & {\left[e^{2}\left(B_{t_{i-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2}\right] } \\
& =E\left[E\left[e\left(B_{t_{i-1}}\right)^{2}\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2} \mid F_{t_{i-1}}\right]\right.
\end{aligned}
$$

Now

$$
\begin{aligned}
& E\left[e^{2}\left(B_{t_{i-1}}\right)\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2} \mid \mathcal{F}_{t_{i-1}}\right] \\
& =e^{2}\left(B_{t_{i-1}}\right) E\left[\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2} \mid \mathcal{F}_{t_{i-1}}\right] \\
& =e^{2}\left(B_{t_{i-1}}\right) E\left[\left(B_{t_{i}}-B_{t_{i-1}}\right)^{2}\right] \\
& =e^{2}\left(B_{t_{i-1}}\right)\left(t_{i}-t_{i-1}\right)
\end{aligned}
$$

where the first step follows from $B_{t-1}$ being $\mathcal{F}_{t-1}$ measurable, the second from independence of Brownian motion increments and the last from the definition of Brownian motion.
Now bringing things together
gives

$$
\begin{aligned}
& E\left[\left(\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right] \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} E\left[e^{2}\left(B_{t_{i-1}}\right)\left(t_{i}-t_{i-1}\right)\right] \\
& =\lim _{n \rightarrow \infty} E\left[\sum_{i=1}^{n} e^{2}\left(B_{t i-1}\right)\left(t_{i}-t_{i-1}\right)\right] \\
& =E\left[\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t i-1}\right)\left(t_{i}-t_{i-1}\right)\right]
\end{aligned}
$$

Now for the final step. Recall that

$$
f\left(t, B_{t}\right)=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} e\left(B_{t j}\right) \mathbb{I}_{\left[t_{j-1}, t_{j}\right]}
$$

where

$$
\mathbb{1}_{\left[t_{j-1}, t_{j}\right]}=\left\{\begin{array}{ll}
1 & t_{j-1} \leqslant t \leqslant t_{j} \\
0 & t<t_{j-1},
\end{array} \quad t>t_{j}\right.
$$

so

$$
\begin{gathered}
f^{2}\left(t, B_{t}\right)=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \sum_{i=1}^{n} e\left(B_{t_{j}}\right) e\left(B_{t_{i}}\right) \\
\underline{1}_{\left[t_{j-1}, t_{j}\right]} \underline{1}_{\left[t_{i-1}, t_{i}\right]}
\end{gathered}
$$

Since the intervals defining the indicator function do not overlap for $i \neq j$ it follows that

$$
\mathbb{X}_{\left[t_{j-1}, t_{j}\right]}=1 \Rightarrow t_{j-1} \leqslant t \leqslant t_{j}
$$

implies that either $t<t_{i-1}$ or $t>t_{i}$ thus

$$
\mathbb{1}_{\left[t_{i-1}, t_{i}\right]}=0
$$

thus for $i \neq j$

$$
\mathbb{1}_{\left[t_{j-1}, t_{j}\right]} \mathbb{1}_{\left[t_{i-1}, t_{i}\right]}=0
$$

and for $i=j$

$$
\mathbb{1}_{\left[t_{j-1}, t_{j}\right]} \mathbb{1}_{\left[t_{i-1}, t_{i}\right]}=\mathbb{1}_{\left[t_{i-1}, t_{i}\right]} \delta_{i j}
$$

thus

$$
\begin{aligned}
f^{2}(t, & \left.B_{t}\right)=\lim _{n \rightarrow \infty} \sum_{j=1}^{n} \sum_{i=1}^{n} e\left(B_{t_{j}}\right) e\left(B_{t_{i}}\right) \\
& \mathbb{1}_{\left[t_{j-1}, t_{j}\right]} \underline{1}_{\left[t_{i-1}, t_{i}\right]} \\
= & \lim _{n \rightarrow \infty} \sum_{j=1}^{n} \sum_{i=1}^{n} e\left(B_{t_{j}}\right) e\left(B_{t_{i}}\right) \\
& \underline{1}_{\left[t_{i-1}, t_{i}\right]} \delta_{i j} \\
= & \lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t_{i}}\right) \underline{1}_{\left[t_{i-1}, t_{i}\right]}
\end{aligned}
$$

Recalling that
$\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t_{i-1}}\right)\left(t_{i}-t_{i-1}\right)$

$$
=\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t_{i-1}}\right) \int_{t_{i-1}}^{t i} d s
$$

$$
\begin{aligned}
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \int_{t_{i-1}}^{t i} e^{2}\left(B_{t_{i-1}}\right) d s \\
& =\int_{0}^{t}\left\{\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t_{i-1}}\right) \mathbb{1}\left[t_{i-1}, t_{i}\right]\right\} d s \\
& =\int_{0}^{t} f^{2}\left(s, B_{s}\right) d s
\end{aligned}
$$

Finally bringing things together gives the desired result.

$$
\begin{aligned}
& E\left[\left(\int_{0}^{t} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right] \\
& =E\left[\lim _{n \rightarrow \infty} \sum_{i=1}^{n} e^{2}\left(B_{t i-1}\right)\left(t_{i}-t_{i-1}\right)\right] \\
& =E\left[\int_{0}^{t} f^{2}\left(s, B_{s}\right) d s\right]
\end{aligned}
$$

## The Itô Formula

The most general one-dimensional first order stochastic differential equation has the form

$$
d x_{t}=\mu\left(x_{t}, t\right) d t+\sigma\left(x_{t}, t\right) d B_{t}
$$

where $B_{t}$ is Brownian Motion, $\mu\left(x_{t}, t\right)$ is called the drift and $\sigma\left(x_{t}, t\right)$ the odatility.
This equation can be integrated to produce ${ }_{t}$

$$
\begin{aligned}
x_{t}= & x_{0}+\int_{0}^{t} \mu\left(x_{t}, t\right) d t \\
& +\int_{0}^{t} \sigma\left(x_{t}, t\right) d B_{t}
\end{aligned}
$$

where $x_{0}$ is the initial value of $x_{t}$. It is assumed that

$$
\int_{0}^{t} \mu\left(x_{s}, s\right)+\sigma^{2}\left(x_{s}, s\right) d s<\infty
$$

Consider a twice differentiable function

$$
z_{t}=f\left(x_{t}, t\right)
$$

Expand $z_{t}$ to second order in $d x_{t}$ and linear in $d t$. Expanding to second order in $d x_{t}$ is in articipation of the relation

$$
\left(d B_{t}\right)^{2}=d t
$$

Now,

$$
d z_{t}=\frac{\partial f}{\partial t} d t+\frac{\partial f}{\partial x_{t}} d x_{t}+\frac{1}{2} \frac{\partial^{2} f}{\partial x_{t}^{2}} d x_{t}^{2}
$$

But

$$
d x_{t}=\mu d t+\gamma d B_{t}
$$

and to lowest order

$$
\begin{aligned}
d X_{t}^{2} & =\left(\mu d t+\sigma d B_{t}\right)^{2} \\
& =\mu^{2} d t^{2}+2 \mu \sigma d t d B_{t}+\sigma^{2} d B_{t}^{2}
\end{aligned}
$$

$$
\begin{aligned}
& =\sigma^{2} d B_{t}^{2} \\
& =\sigma^{2} d t
\end{aligned}
$$

The Itó formula is obtained by substituting the expressions for the differentials into the Taylor expansion for $f\left(x_{t}, t\right)$

$$
\begin{aligned}
d z_{t}= & \frac{\partial f}{\partial t} d t+\frac{\partial f}{\partial x_{t}}\left(\mu d t+\sigma d B_{t}\right) \\
& +\frac{1}{\partial} \frac{\partial^{2} f}{d x_{t}^{2}}\left(\sigma^{2} d t\right) \\
= & \frac{\partial f}{\partial t} d t+\mu \frac{\partial f}{\partial x_{t}} d t+\sigma \frac{\partial f}{\partial x_{t}} d B_{t} \\
& +\frac{\sigma^{2}}{\partial} \frac{\partial^{2} f}{\partial x_{t}^{2}} d t \\
= & {\left[\frac{\partial f}{\partial t}+\mu \frac{\partial f}{\partial x_{t}}+\frac{\sigma^{2}}{2} \frac{\partial^{2} f}{\partial x_{t}^{2}}\right] d t } \\
& +\sigma \frac{\partial f}{\partial x_{t}} d B_{t}
\end{aligned}
$$

The Itô formula can by used to evaluate integrals of stochastc processes. Consider the example from the prevous section,

$$
Z_{t}=\frac{1}{2} B_{t}^{2}
$$

substitution into the Itô formula with

$$
\mu=0 \quad \sigma^{2}=1
$$

gives

$$
d Z_{t}=\frac{1}{2} d t+B_{t} d B_{t}
$$

and integrating gives the desired result

$$
\begin{aligned}
\int_{0}^{t} B_{t} d B_{t} & =\int_{0}^{t} d z_{t}-\frac{1}{2} \int_{0}^{t} d t \\
& =z_{t}-z_{0}-\frac{1}{2} t
\end{aligned}
$$

using

$$
Z_{t}=V_{2} B_{t}^{2}
$$

and

$$
Z_{0}=y_{2} B_{0}^{2}=0
$$

since $B_{0}=0 \quad b_{1}$ definition of Brownian motion.

Thus

$$
\int_{0}^{t} B_{t} d B_{t}=\frac{1}{2}\left(B_{t}^{2}-t\right)
$$

which is the result obtained by direct evaluation of the Itó integral.

## Fractional Brownian Motion

Fractional Brownian Motion is defined by the stochastic integral
$Z^{H}(t)=\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s)$
Where $0<H<1$ is referred to as the Hurst index or Hurst exponent, $d B(s)$ is Brownian Motion and where,

$$
\begin{aligned}
& (t-s)_{+}=\left\{\begin{array}{cc}
t-s & \text { if } t>s \\
0 & \text { if } t \leqslant s
\end{array}\right. \\
& (-s)_{+}=\left\{\begin{array}{cc}
-s & \text { if } s<0 \\
0 & \text { if } s \geqslant 0
\end{array}\right.
\end{aligned}
$$

and
$C(H)=\left\{\int_{-\infty}^{0}\left[(1-s)^{H-1 / 2}-(-s)^{H-1 / 2}\right]^{2} d s+\frac{1}{2 H}\right\}^{1 / 2}$

Now $z^{H}(t)$ is defined by an Itô integral, namely

$$
I_{[a, b]}(f)=\int_{a}^{b} f\left(s, B_{s}\right) d B_{s}
$$

For Fractional Brownian motion

$$
f\left(s, B_{6}\right)=(t-s)_{+}^{1+-1 / 2}-(-s)_{+}^{H-1 / 2}
$$

From the definition of $Z^{H}(t)$ it is seen that

$$
2^{H}(0)=0
$$

Fractional Brownian motion is a Gaussian process which means that the distribution of realizations obtained affer time $t$ has a Gaussian distribution charaterized by the first two moments. In the following sections the first two moments are evaluated and othe properties are discussed.

## Mean Value of Fractional Brownian Motion

The mean value of Fractional Brownian motion is given by
$E\left[Z^{H}(t)\right]$
$=E\left[\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-4 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s)\right]$
$=\frac{1}{C(H)} E\left[\int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s)\right]$
Performing a simple function expansion gives

$$
\begin{aligned}
& \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s) \\
= & \lim _{n \rightarrow \infty} \sum_{i=-n+1}^{n}\left[\left(t-s_{i-1}\right)_{+}^{H-1 / 2}-\left(-s_{i-1}\right)^{H-1 / 2}\right] \Delta B_{i}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[Z^{H}(t)\right]=E\left[\operatorname { l i m } _ { n \rightarrow \infty } \sum _ { i = - n + 1 } ^ { n } \left[\left(t-s_{i-1}\right)_{+}^{H-1 / 2}\right.\right. \\
& \left.\left.-\left(-s_{i-1}\right)^{H-1 / 2}\right] \Delta B_{i}\right] \\
& =\lim _{n \rightarrow \infty} \sum_{i=-n+1}^{n}\left[\left(t-s_{i-1}\right)_{+}^{H-1 / 2}-\left(-s_{i-1}\right)^{H-1 / 2}\right] E\left(\Delta B_{i}\right)
\end{aligned}
$$

But by definition

$$
E\left(\Delta B_{i}\right)=0
$$

Thus

$$
E\left[2^{H}(t)\right]=0
$$

## Expectation of Second Moment of Fractional Brownian Motion

The expectation of the second moment of $z^{H}(t)$ can be computed using the isometry property of the Itô integral,

$$
\begin{aligned}
& E\left[\left(\int_{-\infty}^{\infty} f\left(s, B_{s}\right) d B_{s}\right)^{2}\right] \\
& \quad=E\left[\int_{-\infty}^{\infty} f^{2}\left(s, B_{s}\right) d s\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[\left(2^{H}(t)\right)^{2}\right]= \\
& E\left[\frac{1}{c^{2}(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right]^{2} d s\right] \\
& =\frac{1}{c^{2}(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right]^{2} d s
\end{aligned}
$$

where last step follows from the integrand being independent of $B(s)$. To evaluate the integral let

$$
s=t u \Rightarrow \quad d s=t d u
$$

then

$$
\begin{aligned}
& \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right]^{2} d s \\
= & \int_{-\infty}^{\infty}\left[(t-t u)_{+}^{H-1 / 2}-(-t u)_{+}^{H-1 / 2}\right]^{2} t d u \\
= & t \int_{-\infty}^{\infty}\left[t^{H-1 / 2}(1-u)_{+}^{H-1 / 2} \cdot t^{H-1 / 2}(-u)_{+}\right]^{2} d u \\
= & t \int_{-\infty}^{D} t^{2(H-1 / 2)}\left[(1-u)_{+}^{H-1 / 2}-(-u)_{+}^{H-1 / 2}\right]^{2} d u \\
= & t^{2 H} \int_{-\infty}^{\infty}\left[(1-u)_{+}^{H-1 / 2}-(-u)_{+}^{H-1 / 2}\right]^{2} d u
\end{aligned}
$$

Now to evaluate the integral the range integration must be determined to satisfy

$$
1-u \geqslant 0 \text { and }-u \geqslant 0
$$

Both inequalities are satfied on the interval $(-\infty, 0]$ and the first inequality is also satisfied on the interval $[0,1]$. It follows that the integral becomes
satisfied on the interval $[0,1]$. It follows that the integral becomes

$$
\begin{aligned}
=t^{2 H} & \left\{\int_{-\infty}^{0}\left[(1-u)^{H-1 / 2}-(-u)^{H-1 / 2}\right]^{2} d u\right. \\
+ & \left.\int_{0}^{1}\left[(1-u)^{H-1 / 2}\right]^{2} d u\right\}
\end{aligned}
$$

Consider the second integral

$$
\int_{0}^{1}\left[(1-u)^{H-1 / 2}\right]^{2} d u=\int_{0}^{1}(1-u)^{2 H-1} d u
$$

let

$$
\omega=1-u \Rightarrow \quad d \omega=-d u
$$

then

$$
\begin{aligned}
& \int_{0}^{1}(1-u)^{2 H-1} d u=-\int_{1}^{0} w^{2 H-1} d w \\
& =\int_{0}^{1} w^{2 H-1} d w=\left.\frac{1}{2 H} w^{2 H}\right|_{0} ^{1} \\
& =\frac{1}{2 H}
\end{aligned}
$$

Bringing the results together
gives gues

$$
\int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right]^{2} d s
$$

$$
\begin{gathered}
=t^{2 H}\left\{\int_{-\infty}^{0}\left[(1-u)^{H-1 / 2}-u^{H-1 / 2}\right]^{2} d u\right. \\
\left.+\frac{1}{2 H}\right\}
\end{gathered}
$$

The desired expectation of the second moment is given by

$$
\begin{aligned}
& E\left[\left(z^{H}(t)\right)^{2}\right]= \\
& =\frac{1}{c^{2}(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right]^{2} d s \\
& =\frac{t^{2 H}}{c^{2}(H)}\left\{\int_{-\infty}^{0}\left[(1-u)^{H-1 / 2}-u^{H-1 / 2}\right]^{2} d u\right. \\
& \left.=\frac{1}{2 H}\right\}
\end{aligned}
$$

since

$$
\begin{gathered}
c^{2}(H)=\left\{\int_{-\infty}^{0}\left[(1-u)^{H-1 / 2}-u^{H-1 / 2}\right]^{2} d u\right. \\
\left.+\frac{1}{2 H}\right\}
\end{gathered}
$$

Thus

$$
E\left[\left(z^{H}(t)\right)^{2}\right]=t^{2 H}
$$

## Expectation of the square of Increments of Fractional Brownian Motion

Next Consider the expectation of the square of the difference of Fractional Brownian motion at times $t>s$, namely

$$
E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]
$$

First consider,

$$
\begin{aligned}
z^{H}(t) & -z^{H}(s) \\
= & \frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-L_{2}}-(-u)_{+}^{H-1 / 2}\right] d B(u) \\
& -\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(s-u)_{+}^{H-L_{2}}-(-u)_{+}^{H-1 / 2}\right] d B(u)
\end{aligned}
$$

$$
\begin{aligned}
=\frac{1}{C(H)} & \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(\psi)_{+}^{H-1 / 2}\right. \\
& \left.-(S-u)_{+}^{H-1 / 2}+(-u)_{+}^{H-1 / 2}\right] d B(u) \\
=\frac{1}{C(H)} & \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}(S-u)_{+}^{H-1 / 2}\right] d B(u)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right] \\
= & E\left[\left\{\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(s-u)_{+}^{H-1 / 2}\right] d B(u)\right\}^{2}\right] \\
= & E\left[\left\{\frac{1}{C^{2}(H)} \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}(s-u)_{+}^{H-1 / 2}\right]^{2} d u\right\}\right] \\
= & \frac{1}{C^{2}(H)} \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(s-u)_{+}^{H-1 / 2}\right]^{2} d u
\end{aligned}
$$

where the next to last follows from Isometry of the

Itô Integral and the last slep follows because the integral is not random
To go furtur make the change of variables

$$
\begin{aligned}
-\omega=s-u & \Rightarrow u=s+\omega \\
d \omega & =d u
\end{aligned}
$$

then

$$
\begin{aligned}
& \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(s-u)_{+}^{H-1 / 2}\right]^{2} d u \\
& =\int_{-\infty}^{\infty}\left[(t-(s+\omega))_{+}^{H-1 / 2}-(-\omega)_{+}^{H-1 / 2}\right]^{2} d \omega \\
& =\int_{-\infty}^{\infty}\left[(t-s-\omega)_{+}^{H-1 / 2}-(-\omega)_{+}^{H-1 / 2}\right]^{2} d \omega
\end{aligned}
$$

Make another change of variables

$$
\begin{aligned}
& \omega=(t-s) v \\
\Rightarrow & d \omega=(t-s) d v
\end{aligned}
$$

then

$$
\begin{aligned}
& \int_{-\infty}^{\infty}\left[(t-s-\omega)_{+}^{H-1 / 2}-(-\omega)_{+}^{H-1 / 2}\right]^{2} d \omega \\
= & \int_{-\infty}^{\infty}\left[(t-s-(t-s) v)_{+}^{H-1 / 2}-(-(t-s) v)_{+}^{H-1 / 2}\right]^{2}(t-s) d v \\
= & (t-s) \int_{-\infty}^{\infty}(t-s)^{2(H-1 / 2)}\left[(1-v)_{+}^{H-1 / 2}-(-v)_{+}^{H-1 / 2}\right]^{2} d v \\
= & (t-s)^{2 H} \int_{-\infty}^{\infty}\left[(1-v)_{+}^{H-1 / 2}-(-v)_{+}^{H-1 / 2}\right]^{2} d v
\end{aligned}
$$

Previosly it was shown that

$$
c^{2}(H)=\int_{-\infty}^{\infty}\left[(1-v)_{+}^{H-1 / 2}-(-v)_{+}^{H-1 / 2}\right]^{2} d v
$$

thus

$$
\begin{gathered}
\int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(s-u)_{+}^{H-1 / 2}\right]^{2} d u \\
=(t-s)^{2 H} C^{2}(H)
\end{gathered}
$$

It follows that the desired expectation is given by
$E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]$
$=\frac{1}{c^{2}(H)} \int_{-\infty}^{\infty}\left[(t-u)_{+}^{H-1 / 2}-(s-u)_{+}^{H-1 / 2}\right]^{2} d u$
$=\frac{1}{c^{2}(H)}(t-s)^{2 H} c^{2}(H)$
$=(t-s)^{2 H}$
Thus

$$
E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]=(t-s)^{2 H}
$$

## Covariance of Fractional Brownian motion

## The covariance of Fractional

Brownian motion is defined by

$$
R^{H}(t, s)=E\left[z^{H}(t) z^{H}(s)\right]
$$

where $t>s$.
Consider the previous result obtained for the expectation of the square of an inorement between $t>s$

$$
E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]=(t-s)^{2 H}
$$

and for the expectation of the second moment of $Z^{H}(t)$

$$
E\left[\left(z^{H}(t)\right)^{2}\right]=t^{2 H}
$$

From the first expression

$$
\begin{aligned}
E & {\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right] } \\
& =E\left[\left(z^{H}(t)\right)^{2}+\left(z^{H}(s)\right)^{2}-2 z^{H}(t) z^{H}(s)\right] \\
\Rightarrow & E\left[z^{H}(t) z^{H}(s)\right]=\frac{1}{2}\left\{E\left[\left(z^{H}(t)\right)^{2}\right]\right. \\
& \left.+E\left[\left(z^{H}(s)\right)^{2}\right]-E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]\right\}
\end{aligned}
$$

Thus the desired result for the covariance for fractional Brownian motion can be obtained from the previous results, namely

$$
\begin{aligned}
& R^{H}(t, s)=E\left[z^{H}(t) z^{H}(s)\right] \\
& =\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

Self Similarity of Fractional Brownian Motion

A self similar stochastic process satisfies, for any $a>0$

$$
a^{-H} z^{H}(a t) \sim z^{H}(t)
$$

That is the distribution of $z^{H}(t)$ is invariant under a scaling transformation.
To prove this it is sufficent to show that all of the moments are scale invarient. Since Fractional Brownian motion is Caussion showing that the first two moments are scale invariant is sufficient.
For the first moment this is trivial since

$$
a^{-H} E\left[Z^{H}(a t)\right]=0
$$

For the second moment,

$$
\begin{aligned}
& R^{H}(t, s)=E\left[z^{H}(t) z^{H}(s)\right] \\
& =\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

show that

$$
a^{-2 H} R^{H}(a t, a s)=R^{H}(t, s)
$$

Now,

$$
\begin{aligned}
& E\left[a^{-H} z^{H}(a t) a^{-H} z^{H}(a s)\right] \\
& =a^{-2 H} E\left[z^{H}(a t) z^{H}(a s)\right] \\
& =a^{-2 H} R^{H}(a t, a s) \\
& =\frac{1}{2} a^{-2 H}\left[(a t)^{2 H}+(a s)^{2 H}-(a t-a s)^{2 H}\right] \\
& =\frac{1}{2} a^{-2 H}\left[a^{2 H} t^{2 H}+a^{2 H} s^{2 H}+a^{2 H}(t-s)^{2 H}\right] \\
& =\frac{1}{2} a^{-2 H} a^{2 H}\left[t^{2 H}+s^{2 H}+(t-s)^{2 H}\right] \\
& =\left[t^{2 H}+s^{2 H}+(t-s)^{2 H}\right] \\
& =R^{H}(t, s)
\end{aligned}
$$

thus

$$
a^{-2 H} R^{H}(a t, a s)=R^{H}(t, s)
$$

so Fractional Brownian Motion is scale invariant.

## Stationarity of Increments of Fractional Brownian Motion

Stationarity of increments of of Fractional Brownian motion implies that, for $s$ and $t \geqslant 0$

$$
2^{H}(t+s)-2^{H}(s) \sim 2^{H}(s)
$$

This property can be stated as that adding an increment to Fractional Brownian motion does not change the distribution. Since Fractional Brownian motion is Gaussian showing invartace of the first two moments are invariant when a increment is added.
For the first moment this is torivial since

$$
E\left[Z^{H}(S)\right]=0
$$

50

$$
\begin{aligned}
E & {\left[z^{H}(t+s)-z^{H}(s)\right]=E\left[z^{H}(t-1 s)\right] } \\
& +E\left[z^{H}(s)\right] \\
= & 0
\end{aligned}
$$

For the second moment consider the covariance with $s, r, t \geqslant 0$

$$
\begin{aligned}
E & {\left[\left(2^{H}(t+s)-2^{H}(s)\right)\left(2^{H}(r+s)-2^{H}(s)\right)\right] } \\
= & E\left[2^{H}(t+s) 2^{H}(r+s)\right]-E\left[2^{H}(t+s) 2^{H}(s)\right] \\
& -E\left[2^{H}(s) 2^{H}(r+s)\right]+E\left[\left(2^{H}(s)\right)^{2}\right]
\end{aligned}
$$

Now using

$$
\begin{aligned}
& R^{H}(t, s)=E\left[z^{H}(t) z^{H}(s)\right] \\
& =\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

for each term sives

$$
\begin{aligned}
E & {\left[2^{H}(t+s) 2^{H}(r+s)\right]=\frac{1}{2}\left[(t+s)^{2 H}\right.} \\
& \left.+(r+s)^{2 H}-(t-r)^{2 H}\right]
\end{aligned}
$$

$$
\begin{aligned}
E & {\left[z^{H}(t+s) z^{H}(s)\right]=\frac{1}{2}\left[(t+s)^{2 H}+s^{2 H}\right.} \\
& \left.-t^{2 H}\right] \\
E & {\left[z^{H}(s) z^{H}(r+s)\right]=\frac{1}{2}\left[s^{2 H}+(r+s)^{2 H}\right.} \\
& \left.-r^{2 H}\right] \\
E & {\left[\left(z^{H}(s)\right)^{2}\right]=s^{2 H} }
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
E & {\left[\left(z^{H}(t+s)-z^{H}(s)\right)\left(z^{H}(r+s)-z^{H}(s)\right)\right] } \\
= & E\left[z^{H}(t+s) z^{H}(r+s)\right]-E\left[z^{H}(t+s) z^{H}(s)\right] \\
& -E\left[z^{H}(s) z^{H}(r+s)\right]+E\left[\left(z^{H}(s)\right)^{2}\right] \\
= & \frac{1}{2}\left[(t+s)^{2 H}+\left(r^{2}+s\right)^{2 H}-(t-r)^{2 H}\right] \\
- & \frac{1}{2}\left[(\bar{t}+s)^{2 H}+\delta^{2 H}-t^{2 H}\right] \\
- & \frac{1}{2}\left[z^{2 H}+\left(r^{2 H}\right)^{2 H}-r^{2 H}\right]+\hat{s}^{2 H}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{2}\left[t^{2 H}+r^{2 H}-(t-r)^{2 H}\right] \\
& =E\left[2^{H}(t) 2^{H}(r)\right] \\
& =R^{H}(t, r)
\end{aligned}
$$

Thus the distribution of $z^{H}(t)$ is invariant under shifts in $t$.

## Autocouariance of Fractional Brownian Noise

Fractional Brownian Noise is an increment of Fractional Brownian Motion. Let

$$
\begin{aligned}
\Delta z_{k}^{H} & =z^{H}\left(t_{k}\right)-z^{H}\left(t_{k-1}\right) \\
& =z_{k}^{H}-z_{k-1}^{H}
\end{aligned}
$$

denste Fractional Brownian Noise, then Fractional Brownian Motion is constructed by summing the noise increments,

$$
Z_{n}^{H}=\sum_{k=1}^{n} \Delta Z_{k}^{H}
$$

where $t=n \Delta t$ and $t_{k}=k \Delta t$.
The autocouariace of Fractional Brownian Doise is defined by

$$
\begin{aligned}
\gamma_{n}^{H} & =E\left(\Delta z_{k}^{H} \Delta z_{k+n}^{H}\right) \\
& =E\left[\left(z_{k}^{H}-z_{k-1}^{H}\right)\left(z_{k+n}^{H}-z_{k-1 n-1}^{H}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & E\left(Z_{k}^{H} Z_{k+n}^{H}-Z_{k}^{H} Z_{k+n-1}^{H} Z_{k-1}^{H} Z_{k+n}^{H}+\right. \\
& \left.Z_{k-1}^{H} Z_{k+n-1}^{H}\right) \\
= & E\left(Z_{k}^{H} Z_{k+n}^{H}\right)+E\left(Z_{k-1}^{H} Z_{k+n-1}^{H}\right)- \\
& E\left(Z_{k}^{H} Z_{k+n-1}^{H}\right)-E\left(Z_{k-1}^{H} Z_{k+n}^{H}\right)
\end{aligned}
$$

Considering each term seperately and using the expression for covariance,

$$
\begin{aligned}
& E\left(z_{k}^{H} z_{k+n}^{H}\right)=\frac{1}{2} \Delta t^{2 H}\left[k^{2 H}+(k+n)^{2 H}\right. \\
&\left.-(k+n-k)^{2 H}\right] \\
&= \frac{1}{2} \Delta t\left[k^{2 H}+(k+n)^{2 H}-n^{2 H}\right] \\
& E\left(z_{k-1}^{H} z_{k+n-1}^{H}\right)=\frac{1}{2} \Delta t^{2 H}\left[(k-1)^{2 H}\right. \\
&\left.+(k+n-1)^{2 H}-(k+n-1-k+1)^{2 H}\right] \\
&= \frac{1}{2 \Delta t^{2 H}\left[(k-1)^{2 H}+(k+n-1)^{2 H}-n^{2 H}\right]} \\
& E\left(z_{k}^{H} z_{k+n-1}^{H}\right)=\frac{1}{2} \Delta t^{2 H}\left[k^{2 H}+(k+n-1)^{2 H}\right. \\
&\left.-(k+n-1-k)^{2 \pi}\right]
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2} \Delta t^{2 H}\left[K^{2 H}+(K+n-1)^{2 H}-(n-1)^{2 H}\right] \\
E( & \left.Z_{K-1}^{H} Z_{K+n}^{H}\right)=\frac{1}{2} \Delta t^{2 H}\left[(K-1)^{2 H}+(K+n)^{2 H}\right. \\
& \left.-(K+n-K+1)^{2 H}\right] \\
= & \frac{1}{2} \Delta t^{2 H}\left[(K-1)^{2 H}+(K+n)^{2 H}-(n+1)^{2 H}\right]
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
\gamma_{n}^{H}= & E\left(Z_{k}^{H} Z_{k+n}^{H}\right)+E\left(Z_{k-1}^{H} Z_{k+n-1}^{H}\right)- \\
& E\left(Z_{k}^{H} Z_{k+n-1}^{H}\right)-E\left(Z_{k-1}^{H} Z_{k+n}^{H}\right) \\
= & \frac{1}{2} \Delta t^{2 H}\left[K^{2 H}+(K+\tilde{n})^{2 H}-n^{2 H}\right]+ \\
& \frac{1}{2} \Delta t^{2 H}\left[(K-1)^{2 H}+(K+n-1)^{2 H}-n^{2 H}\right]- \\
& \frac{1}{2} \Delta t^{2 H}\left[K^{2 H}+(K+n-1)^{2 H}-(n-1)^{2 H}\right]- \\
& \frac{1}{2} \Delta t^{2 H}\left[(K-1)^{2 H}+\left(K^{2 H}\right)^{2 H}-(n+1)^{2 H}\right] \\
= & \frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
\end{aligned}
$$

Thus

$$
\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

where

$$
\Delta t=\frac{t}{n}
$$

Note that $\gamma_{n}^{H}$ is independent of $k$. This is a consequence of stationarity of Fractional Brownian motion.

## Variance of Fractional Gaussian Noise

The variance of Fractional Gaussian Noise is defined by

$$
\begin{aligned}
\gamma_{0}^{H}= & E\left[\left(\Delta Z_{k}^{H}\right)^{2}\right] \\
= & E\left[\left(Z_{k}^{H}-Z_{k-1}^{H}\right)^{2}\right] \\
= & E\left[\left(Z_{k}^{H}\right)^{2}-2 Z_{k}^{H} Z_{k-1}^{H}+\left(Z_{k-1}^{H}\right)^{2}\right] \\
= & E\left[\left(Z_{k}^{H}\right)^{2}\right]-2 E\left(Z_{k}^{H} Z_{k-1}^{H}\right) \\
& +E\left[\left(Z_{k-1}^{H}\right)^{2}\right]
\end{aligned}
$$

Considering each term seperately

$$
\begin{aligned}
& E\left[\left(Z_{k}^{H}\right)^{2}\right]=(\Delta t k)^{2 H} \\
& E\left[\left(Z_{k-1}^{H}\right)^{2}\right]=[\Delta t(k-1)]^{2 H} \\
& E\left(Z_{k}^{H} Z_{k-1}^{H}\right)=\frac{1}{2}\left\{(\Delta t k)^{2 H}+[\Delta t(k-1)]^{2 H}\right. \\
& \left.-[\Delta t(k-k+1)]^{2 H}\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2}\left\{(\Delta t k)^{2 H}+[\Delta t(k-1)]^{2 H}\right. \\
& \left.-\Delta t^{2 H}\right\}
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
\gamma_{0}^{H}= & E\left[\left(\Delta z_{k}^{H}\right)^{2}\right] \\
= & E\left[\left(z_{k}^{H}\right)^{2}\right]+E\left[\left(z_{k-1}^{H}\right)^{2}\right] \\
& -2 E\left(z_{k}^{H} z_{k-1}^{H}\right) \\
= & \left.(\Delta \hat{t} k)^{2 H}+[\Delta t / \hat{k}-1)\right]^{2 H} \\
& -\left\{\overline{(\Delta t k)^{2 H}}+[\Delta \hat{t}(k-1)]^{2 H}-\Delta t^{2 H}\right\} \\
= & \Delta t^{2 H}
\end{aligned}
$$

thus

$$
\gamma_{0}^{H}=\Delta t^{2 H}
$$

## Relation Between Fractional Calculus and Fractional Brownian Mostion

The Left Fractional integral of a function $f(x)$ is defined by

$$
\begin{aligned}
(I-f)(x) & =\frac{1}{\Gamma(\alpha)} \int_{a}^{b}(s-x)_{+}^{\alpha-1} f(s) d s \\
& =\frac{1}{\Gamma(\alpha)} \int_{x}^{b}(s-x)^{\alpha-1} f(s) d s
\end{aligned}
$$

Consider the indicator function

$$
\mathbb{1}_{[0, t]}(s)= \begin{cases}1 & 0 \leqslant s \leqslant t \\ 0 & \text { otherwise }\end{cases}
$$

then consider the $H-1 / 2$ integration of $\mathbb{1}_{[0, t]}(s)$ where $x \leqslant 0<t$

$$
\begin{aligned}
\left(I^{H-1 / 2} \mathbb{1}_{[0, t]}(x)=\right. & \\
& \frac{1}{\Gamma(H-1 / 2)} \int_{x}^{\infty}(S-x)^{H-3 / 2} \mathbb{1}_{[0, t]}(S) d s \\
= & \frac{1}{\Gamma(H-1 / 2)} \int_{0}^{t}(S-x)^{H-3 / 2} d s \\
= & \left.\frac{1}{\Gamma(H-1 / 2)} \frac{1}{H-1 / 2}(S-x)^{H-1 / 2}\right|_{0} ^{t} \\
= & \frac{1}{\Gamma(H-1 / 2)} \frac{1}{H-1 / 2}\left[(t-x)^{H-1 / 2}-(-x)^{H-1 / 2}\right]
\end{aligned}
$$

Now a property of the $\Gamma(\omega)$ function is

$$
\Gamma(\omega+1)=\omega \Gamma(\omega)
$$

thus

$$
\Gamma(H+1 / 2)=(H-1 / 2) \Gamma(H-1 / 2)
$$

and finally

$$
\begin{aligned}
\left(I^{H-1 / 2} \mathbb{1}_{[0, t]}\right)(x) & =\frac{1}{\Gamma(H+1 / 2)}\left[(t-x)^{H-1 / 2}-(-x)^{H-1 / 2}\right] \\
\Rightarrow\left[(t-x)^{H-1 / 2}-(-x)^{H-1 / 2}\right] & \\
= & \Gamma(H+1 / 2)\left(I_{-}^{H-1 / 2} \mathbb{1}_{[0, t]}\right)(x)
\end{aligned}
$$

Recall that
$Z^{H}(t)=\frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-M_{2}}-(-s)_{+}^{H-1 / 2}\right] d B(s)$
Thus

$$
z^{H}(t)=\frac{\Gamma(H+1 / 2)}{C(H)} \int_{-\infty}^{\infty}\left(I_{-}^{H-1 / 2} \mathbb{1}_{[0, t]}\right)(s) d B(s)
$$

The integral can be evaluated using fractional integration by parts. The formula for fractional integration by parts is groen without proof,

$$
\begin{aligned}
\int_{a}^{b} f(u)\left(I^{\alpha}\right. & -g)(u) d u \\
& =\int_{a}^{b}\left(I^{\alpha}+f\right)(u) g(u) d u
\end{aligned}
$$

To use this formula a sketchy assumption must made and recovered from later, the assumplion is $B(s)$ is differentable so that

$$
d B(S)=B^{\prime}(S) d S
$$

This allows application of the formula

$$
\begin{aligned}
Z^{H}(t) & =\frac{\Gamma(H+1 / 2)}{C(H)} \int_{-\infty}^{\infty}\left(I_{-}^{H-1 / 2} \mathbb{1}_{[0, t]}^{\infty}\right)(s) d B(s) \\
& =\frac{\Gamma(H+1 / 2)}{C(H)} \int_{-\infty}^{\infty} \mathbb{1}_{[0, t]}(s)\left(I_{+}^{H-1 / 2} B^{\prime}\right) d s \\
& =\frac{\Gamma(H+1 / 2)}{C(H)} \int_{0}^{t}\left(I_{+}^{H-1 / 2} B^{\prime}\right) d s
\end{aligned}
$$

$$
=\frac{\Gamma(H+1 / 2)}{C(H)}\left(I_{+}^{H+1 / 2} B^{\prime}\right)(t)
$$

Now

$$
B^{\prime}(t)=\left(D_{+}^{\prime} B\right)(t)
$$

It follows that

$$
\begin{aligned}
Z^{H}(t) & =\frac{\Gamma(H+1 / 2)}{C(H)}\left(I_{+}^{H+1 / 2} D_{+}^{1} B\right)(t) \\
& =\frac{\Gamma(H+1 / 2)}{C(H)}\left(I_{+}^{H-1 / 2} B\right)(t)
\end{aligned}
$$

The assume derivative of $B(t)$ has been absorbed into the fractional integral which can be evaluated to give the result the Fractional Brownian motion with parameter $H$ is the $\mathrm{H}^{-1 / 2}$ fractional integral of Brownian motion, justifying the name Fractionat Brownian motion.

## Alterate Definitions of Fractional Brownian Motion

Here Fractional Brownian Motion is defined by

$$
\begin{aligned}
Z^{H}(t)= & \frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(t) \\
= & \frac{1}{C(H)}\left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}(-s)^{H-1 / 2}\right] d B(t)\right. \\
& \left.+\int_{0}^{t}(t-s)^{H-1 / 2} d B(t)\right\}
\end{aligned}
$$

where $0<H<1, B(t)$ is Brownian motion and

$$
C(H)=\left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}-(-s)^{H-1 / 2}\right]^{2} d s+\frac{1}{2 H}\right\}^{1 / 2}
$$

An atternative definition used in the finacial literature and by Benoit Mandelbrot is

$$
\begin{aligned}
z^{H}(t)=\frac{1}{\Gamma(H+1 / 2)} & \left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}-(-s)^{H-1 / 2}\right] d B(t)\right. \\
+ & \left.\int_{0}^{t}(t-s)^{H-1 / 2} d B(t)\right\}
\end{aligned}
$$

This form is more in line with the scaling obtained from the ralationship with the fractional derivative. This normalization changes the results obtained for the second moments

$$
\begin{aligned}
& E\left[\left(Z^{H}(t)^{2}\right]=(C(H))^{2} t^{2 H}\right. \\
& E\left[\left(Z^{H}(t)-Z^{H}(s)\right)^{2}\right]=(C(H))^{2}(t-s)^{2 H} \\
& E\left[Z^{H}(t) Z^{H}(s)\right]= \\
& (C(H))^{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

Another definition is called trucate Fractional Brownian Motion which ignores the integral over negative values in the other definitions,

$$
\hat{Z}^{H}(t)=\frac{1}{\Gamma(H+1 / 2)} \int_{0}^{t}(t-s)^{H-1 / 2} d B(s)
$$

This form is sometimes used in financial models. Mandelbrot criticizes this form as giving too much weight "to the location of the orign".

## Fractional Brownian Motion Summary

The following results have been obtained for Fractional Brownian motion. Fractional Brownian Motion is defined b/

$$
\begin{aligned}
Z^{H}(t)= & \frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s) \\
= & \frac{1}{C(H)}\left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}-(-s)^{H-1 / 2}\right] d B(s)\right. \\
& \left.+\int_{0}^{t}(t-s)^{H-1 / 2} d B(s)\right\}
\end{aligned}
$$

Where $0<H<1$ is the Hurst exponent, $d B(s)$ is Brownian Motion.

The mean and variance are given by

$$
E\left[z^{H}(t)\right]=0
$$

$$
E\left[\left(z^{H}(t)\right)^{2}\right]=t^{2 H}
$$

The covariance for $s<t$ is grven by

$$
\begin{aligned}
& R^{H}(t, s)=E\left[z^{H}(t) z^{H}(s)\right] \\
& =\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
\end{aligned}
$$

The variace of a increment for $s \leqslant t$ is given by

$$
E\left[\left(z^{H}(t)-z^{H}(s)\right)^{2}\right]=(t-s)^{2 H}
$$

Both the covariance function and variance are invarient to a shift in time $s>0$

$$
\begin{gathered}
E\left[\left(z^{H}(t+s)-z^{H}(s)\right)\left(z^{H}(r+s)-z^{H}(s)\right)\right] \\
=\frac{1}{2}\left[t^{2 H}+r^{2 H}-(t-r)^{2 H}\right]
\end{gathered}
$$

$$
\begin{aligned}
= & E\left[z^{H}(t) z^{H}(r)\right] \\
= & R^{H}(t, r) \\
E[ & \left.\left(z^{H}(t+s)-z^{H}(s)\right)^{2}\right] \\
= & E\left[\left(z^{H}(t+s)\right)^{2}\right]-2 E\left[z^{H}(t+s) z^{H}(s)\right] \\
& +E\left[\left(z^{H}(s)\right)^{2}\right] \\
= & (t \hat{t} s)^{2 H}-\left[(t+s)^{2 H}+s^{2 H}-t^{2 H}\right] \\
& +s^{2 H} \\
= & t^{2 H}
\end{aligned}
$$

This result is equivalent to stationarity of the distribution. Brownian Motion is obtaing for $H=1 / 2$. For this case $]$

$$
\begin{aligned}
C(1 / 2) & =1 \\
2^{1 / 2}(t) & =\int_{0}^{t} d B(S) \\
& =B(t)
\end{aligned}
$$

$$
E\left[\left(z^{1 / 2}(t)\right)^{2}\right]=t
$$

The covariance is given by

$$
\begin{aligned}
R^{1 / 2}(t, s) & =E\left[z^{1 / 2}(t) z^{1 / 2}(s)\right] \\
& =\frac{1}{2}\left[t^{2}+s-(t-s)\right] \\
& =\frac{1}{2}(2 s) \\
& =s
\end{aligned}
$$

where it is assumed that $t>s$.

## Limits of second Moments

The linear result for the second moments of Brownican Motion is well known.

The qualtative behavior of fractional Brownian motion has three regimes

$$
\begin{aligned}
& \text { I) } 0<H<1 / 2 \\
& \text { II) } H=1 / 2 \text { (Brownian motion) } \\
& \text { III) } 1 / 2<H<1
\end{aligned}
$$

Consider regime I. For the lower bound of $\mathrm{H} \rightarrow \mathrm{O}$ it is
seen that

$$
\begin{aligned}
& \lim _{H \rightarrow 0} E\left[\left(2^{H}(t)\right)^{2}\right] \\
= & \lim _{H \rightarrow 0} t^{2 H} \\
= & 1
\end{aligned}
$$

Thus the variance is bounded as $t \rightarrow \infty$, and

$$
\begin{aligned}
& \lim _{H \rightarrow 0} R^{H}(t, s)=\lim _{H \rightarrow 0} E\left[Z^{H}(t) Z^{H}(s)\right] \\
= & \lim _{H \rightarrow 0} \frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right] \\
= & \frac{1}{2}(1+1-1) \\
= & 1 / 2
\end{aligned}
$$

Similarly the covariance remains bounded as $t \rightarrow \infty$.
It summary for regime $I, 0<H<1 / 2$, Fractional Brownian motion is
bounded from the left by random motion with bounded variance and covariance function and bounded from the right by Brownian with variance and courcriance that are linear in tume
Next consider Regime III, $1 / 2<H<1$, where for the upper bound of $H \rightarrow 1$ it is seen that,

$$
\begin{aligned}
& \lim _{H \rightarrow 1} E\left[\left(z^{H}(t)\right)^{2}\right]=\lim _{H \rightarrow 1} t^{2 H} \\
&=t^{2} \\
& \lim _{H \rightarrow 1} R^{H}(t, s)=\lim _{H \rightarrow 1} E\left[z^{H}(t) z^{H}(s)\right] \\
&=\lim _{H \rightarrow 1} \frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right] \\
&=\frac{1}{2}\left[t^{2}+s^{2}-(t-s)^{2}\right] \\
&=\frac{1}{2}\left(t^{2}+s^{2}-t^{2}-s^{2}+2 t s\right)
\end{aligned}
$$

$$
=t_{s}
$$

Thus in Regime III, where $12<H<1$, Fractional Brownian motion is bounded from the left by Brownian motion and on the right by variance by covariance of $t^{2}$ and $t s$ respectiviely.
Next the limit of the covariance $R^{H}(t, s)$, for $t \gg s$ will be evaluated

$$
R^{H}(t, s)=\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]
$$

For the last term assume $s$ is fixed while $t$ is varied

$$
\begin{aligned}
(t-s)^{2 H} & =t^{2 H}\left(1-s_{4}\right)^{2 H} \\
& \approx t^{2 H}\left[1-2 H\left(s_{4}\right)\right] \\
& =t^{2 H}(1-2 H S / t)
\end{aligned}
$$

Bringing things together,

$$
R^{H}(t, s) \approx \frac{1}{2}\left[t^{2 H}+s^{2 H}-t^{2 H}(y-2 H s(t)]\right.
$$

$$
=\frac{1}{2}\left(s^{2 H}+2 H s t^{2 H-1}\right)
$$

Thus for $t \gg s$

$$
R^{H}(t, s) \approx \frac{1}{2}\left(s^{2 H}+2 H s t^{2 H-1}\right)
$$

The following plot shows the the variance,

$$
E\left[\left(z^{H}(t)\right)^{2}\right]=t^{2 H}
$$

for a range of values of $H$.

Fraction Brownian Motion Variance, $t^{2 H}$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-350.jpg?height=718&width=1099&top_left_y=1211&top_left_x=217)

Notable are for $H=1 / 2$ the variance is a linear function of time ant the limiting form for $H \rightarrow 0$ of a constant value of 1 and for $H \rightarrow 1$ of $t^{2}$ are also apparent.
The next plots show the covariance as a function of $t$ for fixes $s$ For a range of values of $H$. Recall that the covariance function is given by
$R^{H}(t, s)=\frac{1}{2}\left[t^{2 H}+s^{2 H}-(t-s)^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-351.jpg?height=789&width=1188&top_left_y=1166&top_left_x=211)

Fraction Brownian Motion Autocovariance, $\frac{1}{2}\left[t^{2 H}+s^{2 H}-|t-s|^{2 H}\right], s=1.00$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-352.jpg?height=714&width=1118&top_left_y=163&top_left_x=231)

In the first plot the change in sign of the $|t-s|^{2 H}$ as $t=s$ is apparent as well as the limiting linear form of $R^{\prime}(t, s)=s t$, The next plot shows the case for $t<s$.
The final two plots show the behavior of $R^{H}(t, s)$ for $t \gg s$. It was previously shown that for this limit

$$
R^{H}(t, s) \approx \frac{1}{2}\left(s^{2 H}+2 H s t^{2 H-1}\right)
$$

Fraction Brownian Motion Autocovariance, $\frac{1}{2}\left[t^{2 H}+s^{2 H}-|t-s|^{2 H}\right], \mathrm{s}=1.00$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-353.jpg?height=743&width=1132&top_left_y=183&top_left_x=211)
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-353.jpg?height=761&width=1136&top_left_y=1003&top_left_x=213)

The first plot shows a range of values of $0<H \leqslant 1 / 2$ and the second a range of values for $1 / 2<H \leqslant 1$.
In the first plot the $t \rightarrow \infty$ limit of $1 / 2$ for $0<H<1 / 2$ is apparent. For values of $H$ close to 12 the convergence is slower.

In the second plot the limiting linear form is apparent cend for $H=0.9$ the formula can be verified by inspection.

$$
\begin{aligned}
R^{0,9}(1,1000) & \approx(0,8)(1000)^{0,8} \\
& =226
\end{aligned}
$$

## Autocovariance of Fractional Brownian Noise

Previously it was shown that that the autocouariance is given by,

$$
\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

where

$$
\Delta t=t \ln
$$

First consider the Brownian Motion regime, II, where $H=1 / 2$

$$
\begin{aligned}
\gamma_{n}^{1 / 2} & =\frac{1}{2} \Delta t[(n-1)+n+1-2 n] \\
& =0
\end{aligned}
$$

which is expected since Brownian Motion has independent increments.
Next Consider $H \rightarrow 0$,

$$
\lim _{H \rightarrow 0} \gamma_{n}^{H}=0
$$

and now consider

$$
\begin{aligned}
\lim _{H \rightarrow 1} r_{n}^{H}= & \frac{1}{2} \Delta t^{2}\left[(n-1)^{2}+(n+1)^{2}-2 n^{2}\right] \\
= & \frac{1}{2} \Delta t^{2}\left[\left(n^{2}-2 n^{2}+1\right)+\right. \\
& \left.\left(n^{2}+2 n+1\right)-2 n^{2}\right] \\
= & (\Delta t)^{2}
\end{aligned}
$$

Finally consder the limit $n \gg 1$

$$
\begin{aligned}
\gamma_{n}^{H}= & \frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right] \\
= & \frac{1}{2} \Delta t^{2 H} n^{2 H}\left[\left(1-\frac{1}{n}\right)^{2 H}+\right. \\
& \left.(1+1 / n)^{2 H}-2\right]
\end{aligned}
$$

To obtain an approximation for $n \gg 1$ to leading order both $(1-4 n)^{2 H}$ and $(1+1 n)^{2 H}$ must be approximated to second order since the linear terms cancel, thus for $\left(1-y_{n}\right)^{2 H}$,

$$
\begin{aligned}
& \frac{d}{d(1 / n)}(1-1 / n)^{2 H}=2 H(1-1 / n)^{2 H-1} \\
& \frac{d^{2}}{d^{2}(1 / n)}(1-1 / n)^{2 H}=2 H(2 H-1)(1-1 / n)^{2 H-1} \\
& \text { Now } n \gg 1 \Rightarrow 1 / n \rightarrow 0,50 \\
& \begin{aligned}
(1-1 / n)^{2 H} & \approx 1+\left.\frac{d}{d(1 / n)}(1-1 / n)^{2 H}\right|_{1 / n=0}(1 / n) \\
+ & \left.\frac{1}{2} \frac{d^{2}}{d^{2}(1 / n)}(1-1 / n)^{2 H}\right|_{1 / n=0}(1 / n)^{2} \\
& =1-\frac{2 H}{n}+\frac{H(2 H-1)}{n^{2}}
\end{aligned}
\end{aligned}
$$

Similarly for the $(1+1 / n)^{2 H}$ term

$$
(1-1 / n)^{2 H} \approx 1+\frac{2 H}{n}+\frac{H(2 H-1)}{n^{2}}
$$

Putting things together gives for $n \gg 1$

$$
\begin{aligned}
\gamma_{n}^{H} & =\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right] \\
& \approx \frac{1}{2} \Delta t^{2 H} n^{2 H}\left\{\left[-\frac{2 H}{n}+\frac{H(2 H-1)}{n^{2}}\right]\right. \\
& \left.+\left[r^{2}+\frac{2 H}{n}+\frac{H(2 H-1)}{n^{2}}\right]-2\right\} \\
& =\frac{1}{2} \Delta t^{2 H} n^{2 H}\left(\frac{2 H(2 H-1)}{n^{2}}\right. \\
& =\Delta t^{2 H} H(2 H-1) n^{2 H-2}
\end{aligned}
$$

Thus for large $n$ the Fractional Brownian Noise covariance is given by

$$
\gamma_{n}^{H} \approx \Delta t^{2 H} H(2 H-1) n^{2 H-2}
$$

Consider the value of $\gamma_{n}^{H}$ as a function of $H$ for

$$
H=1 / 2 \quad H=1 \quad 0<H<1 / 2 \quad 1 \quad 2<H<1
$$

for $H<1 / 2$

$$
2 H-1<0
$$

so

$$
\gamma_{n}^{H}<0
$$

and for $1 / 2<H<1$

$$
2 H-1>0
$$

$\delta 0$

$$
\gamma_{n}^{H}>0
$$

For $H=1 / 2$

$$
\underline{\gamma}_{n}{ }^{H}=0
$$

and Finally $H=l$

$$
\gamma_{n}^{H}=1
$$

The notion of long range dependence considers the finitness of the sum

$$
\sum_{n=1}^{\infty}\left|\gamma_{n}^{H}\right|
$$

A process has long range dependence if

$$
\sum_{n=1}^{\infty}\left|\gamma_{n}^{H}\right|=\infty
$$

Now

$$
\begin{aligned}
& \sum_{n=1}^{\infty}\left|\gamma_{n}^{H}\right|=\sum_{n=1}^{\infty}\left|\Delta t^{2 H} H(2 H-1) n^{2 H-2}\right| \\
= & \Delta t^{2 H}|H(2 H-1)| \sum_{n=1}^{\infty} n^{2 H-2} \\
= & \lim _{n \rightarrow \infty} \Delta t^{2 H}|H(2 H-1)| \int_{1}^{n} x^{2 H-2} d x \\
= & \left.\lim _{n \rightarrow \infty} \Delta t^{2 H}|H(2 H-1)| \frac{1}{2 H-1} x^{2 H-1}\right|_{1} ^{n} \\
= & \lim _{n \rightarrow \infty} \Delta t^{2 H} \frac{|H(2 H-1)|\left(n^{2 H-1}-1\right)}{2 H-1}
\end{aligned}
$$

for $0<H<1 / 2 \quad 2 H-1<0$ so the first term is $O$ and

$$
\sum_{n=1}^{\infty}\left|\gamma_{n}^{H}\right|=\Delta t^{2 H} \frac{|H(2 H-1)|}{1-2 H}<\infty
$$

and for $1 / 2<H<1 \quad 2 H-1>0$ so

$$
\sum_{n=1}^{\infty}\left|\gamma_{n}^{H}\right|=\infty
$$

so the process only has long range dependence for $12<1<1$.
In the following plots the autocorrelation crefficinent as shown for ranges of values. The autocorrelation coefficient is defined by

$$
r_{n}^{H}=\frac{\gamma_{n}^{H}}{\gamma_{0}^{H}}
$$

using
$\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$

$$
\begin{aligned}
& \text { and } \frac{\gamma_{0}^{H}=\Delta t^{2 H}}{\text { gives for } n=0} \\
& \text { and for } n>0 \\
& r_{0}^{H}=1 \\
& \text { and for } \frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right] \\
& r_{n}^{H} \approx H(2 H-1) n^{2 H-2}
\end{aligned}
$$

The first plot shows $1 \leqslant n \leqslant 10$ and $O<H \leqslant 1 / 2$

Fraction Brownian Motion Autocovariance, $r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-362.jpg?height=585&width=926&top_left_y=1348&top_left_x=310)
$r_{n}^{H}<0$ is apparent and $r_{n}^{H} \rightarrow 0$ very rapidly as $n \rightarrow \infty$. The next plot also has $0<H \leqslant 1 / 2$ but $n$ covers a larger range to illustrate the rapidity of convergence to zero for large $n$

Fraction Brownian Motion Autocovariance, $r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-363.jpg?height=683&width=1087&top_left_y=785&top_left_x=209)

The next plot shows the $n \gg 1$ approximation to $r_{n}^{H}$ for comparison to the previous plot. The plots are indistinguishable

Fraction Brownian Motion Autocorrelation for $n \gg 1, r_{n}^{H}=H(2 H-1) n^{2 H-2}$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-364.jpg?height=724&width=1166&top_left_y=165&top_left_x=179)

The next plot shows $r_{n}^{H}$ for $1 / 2<H<1$ and $1 \leqslant n \leqslant 10$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-364.jpg?height=735&width=1069&top_left_y=1178&top_left_x=266)
and the next plot shows a much larger range for $n$,

Fraction Brownian Motion Autocovariance, $r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-365.jpg?height=755&width=1169&top_left_y=380&top_left_x=164)

For $H>0,8$ the decay of $r_{n}^{H}$ for large $n$ decreased rapidly with $r_{n}^{H}$ still significant out to values of $n$ as large as 1000. This is because as $H \rightarrow 1 \quad r_{n}^{H} \rightarrow 1$ and for large $n$

$$
r_{n}^{H} \alpha n^{2 H-2}
$$

as $H \rightarrow 1 \quad 2 H-2 \rightarrow 0$ so the
exponent of $n$ becomes small. for $t=0.8$

$$
r_{n}^{0.8} \alpha n^{-0.4}
$$

This slow decay leads to long range depenerdence is this range of values of $H$.

The final plot shows the $n \gg 1$ appoximation to $r_{n}^{H}$ for comparison with the prevides plot. The plots are seen to be indistinguishable

Fraction Brownian Motion Autocorrelation for $n \gg 1, r_{n}^{H}=H(2 H-1) n^{2 H-2}$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-366.jpg?height=775&width=1194&top_left_y=1136&top_left_x=183)

## Simulation of Fractional Brownian Motion

Fractional Brownian Motion is defined by the integral,

$$
\begin{aligned}
z^{H}(t)= & \frac{1}{C(H)} \int_{-\infty}^{\infty}\left[(t-s)_{+}^{H-1 / 2}-(-s)_{+}^{H-1 / 2}\right] d B(s) \\
=\frac{1}{C(H)} & \left\{\int_{-\infty}^{0}\left[(t-s)^{H-1 / 2}-(-s)^{H-1 / 2}\right] d B(s)\right. \\
& \left.+\int_{0}^{t}(t-s)^{H-1 / 2} d B(s)\right\}
\end{aligned}
$$

where $B(s)$ is Brownian Motion, $0<H<1$ and

$$
\begin{gathered}
c(H)=\left\{\int_{-\infty}^{0}\left[(1-u)^{H-1 / 2}-(-w)^{H-1 / 2}\right]^{2} d u\right. \\
\left.+\frac{1}{2 H}\right\}^{1 / 2}
\end{gathered}
$$

## The Stochastic Representation Method

The integral defining Fractional Brownian Motion can be approximated by a Riemann sum. Let

$$
\Delta t=\frac{t}{n} \quad n=1,2,3, \ldots
$$

then

$$
t_{i}=\Delta t i
$$

then for $b_{n}>0$ and $n>0$

$$
\begin{aligned}
& Z^{H}(n)=\frac{\Delta t^{H-1 / 2}}{C^{H}(n)}\left\{\sum _ { K = - b _ { n } } ^ { 0 } \left[(n-K)^{H-1 / 2}\right.\right. \\
& \left.\left.\quad-(-K)^{H-1 / 2}\right] \Delta B_{K}^{1}+\sum_{K=0}^{n}(n-K)^{H-1 / 2} \Delta B_{K}^{2}\right\}
\end{aligned}
$$

and for $c(t)$ using

$$
s=u t \Rightarrow u=\frac{s}{t}=\frac{k \Delta t}{n \Delta t}=\frac{k}{n}
$$

gives

$$
\begin{gathered}
C^{H}(n)=\left\{\sum_{k=-b_{n}}^{0}\left[(1-k / n)^{H-1 / 2}-(-k / n)^{H-1 / 2}\right]^{2}\right. \\
\left.+\frac{1}{2 H}\right\}^{1 / 2}
\end{gathered}
$$

A suggested value for $b$ is

$$
b_{n}=n^{3 / 2}
$$

To simplify numerical calculations consider

$$
\begin{aligned}
\frac{Z^{H}(n) C^{H}(n)}{\Delta t^{H-1 / 2}}= & \sum_{k=-b_{n}}^{0}\left[(n-k)^{H-1 / 2}-(-k)^{H-1 / 2}\right] \Delta B_{k}^{1} \\
& +\sum_{k=0}^{n}(n-k)^{H-1 / 2} \Delta B_{k}^{2}
\end{aligned}
$$

Let

$$
M^{H}(n)=\frac{z^{H}(n) C^{H}(n)}{\Delta t^{H-1 / 2}}
$$

Then

$$
\begin{aligned}
M^{\prime H}(n)=\sum_{k=-b_{n}}^{0} & {\left[(n-k)^{H-1 / 2}-(-k)^{H-1 / 2}\right] \Delta B_{k}^{1} } \\
& +\sum_{k=0}^{n}(n-k)^{H-1 / 2} \Delta B_{k}^{2}
\end{aligned}
$$

where

$$
\begin{gathered}
C^{H}(n)=\left\{\sum_{K=-b_{n}}^{0}\left[(1-K / n)^{H-1 / 2}-(-K / n)^{H-1 / 2}\right]^{2}\right. \\
\left.+\frac{1}{2 H}\right\}^{1 / 2} \\
Z^{H}(n)=M^{H}(n) C^{H}(n) \Delta t^{H-1 / 2}
\end{gathered}
$$

## Cholesky Method

The Cholesky Method is a general method for the simulation of Gaussian processes. When Simulating Fractional Brownian Motion the Cholesky Method is used to generate fractional Caussian Norse which is summed to creat Fractional Cassian Motion. The Cholesky Method models Fractional Brownian Norse as a Multivariate Caussian distribution with covariance Matrix generated by Fractronal Brownian noise,

$$
\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

for $n>0$ and for $n=0$

$$
\gamma_{0}^{H}=\Delta t^{2 H}
$$

Let define the covariance matrix

$$
\Gamma_{n}^{H}=\left[\begin{array}{ccccc}
\gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} & \cdots & \gamma_{n}^{H} \\
\gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} & \cdots & \gamma_{n-1}^{H} \\
\gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H} & \cdots & \gamma_{n-2}^{H} \\
\vdots & \vdots & \vdots & & \\
\gamma_{n}^{H} & \gamma_{n-1}^{H} & \gamma_{n-2}^{H} & \cdots & \gamma_{0}^{H}
\end{array}\right]
$$

and let

$$
B_{n}=\left[\begin{array}{c}
\Delta B_{1} \\
\Delta B_{2} \\
\Delta B_{3} \\
\vdots \\
\Delta B_{n}
\end{array}\right]
$$

denote Brownian Noise column vector and let

$$
Z_{n}^{H}=\left[\begin{array}{c}
\Delta Z_{1}^{H} \\
\Delta Z_{2}^{H} \\
\Delta Z_{3}^{H} \\
\vdots \\
\Delta Z_{n}^{H}
\end{array}\right]
$$

Notable properties of the covariance matrix $\Gamma_{n}^{H}$ are that it is symmetric

$$
\Gamma_{n}^{H}=\left(\Gamma_{n}^{H}\right)^{\top}
$$

and square and positive definite. A positive definite matrix satusfies

$$
x^{\top} A x>0
$$

for every column vector $X$ Consider the linear transformation

$$
Z_{n}^{H}=L_{n} B_{n}
$$

Now let $\left(Z_{n}^{H}\right)^{\top}$ denote the transpose of $\left(R_{n}^{H}\right)^{\top}$ which is a row vector it follows that

$$
\mathbb{Z}_{n}^{H}\left(\mathbb{Z}_{n}^{H}\right)^{\top}
$$

is a square matrix cosisting of every possible product of the elements of $R_{n}^{H}$. It follows
that

$$
\begin{aligned}
& \operatorname{Cov}\left(Z_{n}^{H}\right)=E\left[Z_{n}^{H}\left(Z_{n}^{H}\right)^{\top}\right] \\
& =E\left[\left(\operatorname{Ln} B_{n}\right)\left(L_{n} B_{n}\right)^{\top}\right] \\
& =E\left[\left(L_{n} B_{n}\right)\left(B_{n}\right)^{\top} L_{n}^{\top}\right] \\
& =\operatorname{Ln} E\left[B_{n}\left(B_{n}\right)^{\top}\right] L_{n}^{\top}
\end{aligned}
$$

Now by defition

$$
E\left[\mathbb{B}_{n}\left(\mathbb{B}_{n}\right)^{\top}\right]=\mathbb{1}
$$

where $x_{1}$ is the idenity matrix. It follows that

$$
\operatorname{Cov}\left(Z_{n}^{H}\right)=L_{n} L_{n}^{\top}
$$

and thus

$$
\operatorname{Cov}\left(Z_{n}^{H}\right)=\Gamma_{n}^{H}=L_{n} L_{n}^{\top}
$$

In summary, given a random vector of Brownican vore a
vector of Fractional Brownian Noise is computed by soluing the system of equations

$$
\begin{gathered}
\mathbb{Z}_{n}^{H}=L_{n} B_{n} \\
\Gamma_{n}^{H}=L_{n} L_{n}^{\top}
\end{gathered}
$$

where

$$
\left(\Gamma_{n}^{H}\right)_{i, j}= \begin{cases}\gamma_{i(-j)}^{H} & \text { for } i \neq j \\ \gamma_{0}^{H} & \text { for } i=j\end{cases}
$$

To go furthwr the covariance matrix must be farctored into $I_{n}$ and $L_{n}^{\top}$. This is accomplished using Cholskey Decomposition.

## Cholesky Decomposition

Cholskey decomposition takes advantage of the symetry

$$
\Gamma_{n}^{H}=\left(\Gamma_{n}^{H}\right)^{\top}
$$

to write $\Gamma_{n}^{H}$ as the product of a lower trangular matrix and its transpose. This decreases the computational cost of eveluating

$$
\mathbb{Z}_{n}^{H}=\Gamma_{n}^{H} \mathbb{B}_{n}
$$

and lays the ground work for an application of an FFT method that reduces the computational cost from $O\left(N^{2}\right)$ to $O(N \ln N)$.
Let $L$ denote a lower triangular matrix that satisfies

$$
\Gamma_{n}^{H}=L_{n}^{H}\left(L_{n}^{H}\right)^{T}
$$

where,

$$
L_{n}^{H}=\left[\begin{array}{ccccc}
l_{00} & 0 & 0 & \cdots & 0 \\
l_{10} & l_{11} & 0 & \cdots & 0 \\
l_{20} & l_{21} & l_{22} & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots \\
l_{n 0} & l_{n 1} & l_{n 2} & \cdots & l_{n n}
\end{array}\right]
$$

To get a sense of how the calculation proceeds consider a simpler problem with $n=4$

$$
\begin{aligned}
& \Gamma_{4}^{H}=\left[\begin{array}{llll}
\gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} & \gamma_{3}^{H} \\
\gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} \\
\gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} \\
\gamma_{3}^{H} & \gamma_{2}^{H} & \gamma_{3}^{H} & \gamma_{0}^{H}
\end{array}\right] \\
& L_{4}^{H}=\left[\begin{array}{llll}
l_{00} & 0 & 0 & 0 \\
l_{10} & l_{11} & 0 & 0 \\
l_{20} & l_{21} & l_{22} & 0 \\
l_{30} & l_{31} & l_{32} & l_{33}
\end{array}\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
& L_{4}^{H}\left(L_{4}^{H}\right)^{T}=\left[\begin{array}{llll}
l_{00} & 0 & 0 & 0 \\
l_{10} & l_{11} & 0 & 0 \\
l_{20} & l_{21} & l_{22} & 0 \\
l_{30} & l_{31} & l_{32} & l_{33}
\end{array}\right] \times \\
& {\left[\begin{array}{cccc}
l_{00} & l_{10} & l_{20} & l_{30} \\
0 & l_{11} & l_{21} & l_{31} \\
0 & 0 & l_{22} & l_{32} \\
0 & 0 & 0 & l_{33}
\end{array}\right]} \\
& =\left[\begin{array}{llll}
l_{00}^{2} & l_{00} l_{11} & l_{00} l_{20} & l_{0} l_{30} \\
l_{10} l_{00} & l_{10}^{2}+l_{11}^{2} & l_{20} l_{10}+l_{21} l_{11} & l_{30} l_{10}+l_{31} l_{11} \\
l_{20} l_{00} & l_{20} l_{10}+l_{11} l_{21} & l_{20}^{2}+l_{21}^{2}+l_{22}^{2} & l_{30} l_{20}+l_{31} l_{21} \\
l_{30} l_{00} & l_{30} l_{10}+l_{31} l_{11} & l_{30} l_{30}+l_{21} l_{31} & l_{30}^{2}+l_{31}^{2} \\
& +l_{22} l_{32} & +l_{32}^{2}+l_{33}^{2}
\end{array}\right]
\end{aligned}
$$

So

$$
\left[\begin{array}{cccc}
\gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} & \gamma_{3}^{H} \\
\gamma_{H}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} \\
\gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} \\
\gamma_{3}^{H} & \gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H}
\end{array}\right]
$$

$$
=\left[\begin{array}{cccc}
l_{00}^{2} & l_{00} l_{11} & l_{00} l_{20} & l_{0} l_{30} \\
l_{10} l_{00} & l_{10}^{2}+l_{11}^{2} & l_{20} l_{10}+l_{21} l_{11} & l_{30} l_{10}+l_{31} l_{11} \\
l_{20} l_{00} & l_{20} l_{10}+l_{11} l_{21} & l_{20}^{2}+l_{21}^{2}+l_{22}^{2} & l_{30} l_{20}+l_{31} l_{21} \\
l_{30} l_{00} & l_{30} l_{10}+l_{31} l_{11} & l_{30} l_{30}+l_{21} l_{31} & l_{30}^{2}+l_{31}^{2} \\
& & +l_{22} l_{32} & +l_{32}^{2}+l_{33}^{2}
\end{array}\right]
$$

Comparing terms in first column and row

$$
\begin{aligned}
& l_{00}^{2}=\gamma_{0}^{H} \\
& l_{10} l_{00}=\gamma_{1}^{H} \\
& l_{20} l_{00}=\gamma_{2}^{H} \\
& l_{30} l_{08}=\gamma_{3}^{H}
\end{aligned}
$$

this can be genera lized to give

$$
l_{i 0}=\frac{\gamma_{i}^{H}}{l_{00}}
$$

Next consider the diagonal terms

$$
l_{10}^{2}+l_{11}^{2}=\gamma_{0}^{H}
$$

$$
\begin{gathered}
l_{20}^{2}+l_{21}^{2}+l_{22}^{2}=\gamma_{0}^{H} \\
l_{30}^{2}+l_{31}^{2}+l_{32}^{2}+l_{33}^{2}=\gamma_{0}^{H}
\end{gathered}
$$

gives

$$
\begin{gathered}
l_{11}^{2}=\gamma_{0}^{H}-l_{10}^{2} \\
l_{22}^{2}=\gamma_{0}^{H}-l_{20}^{2}-l_{21}^{2} \\
l_{33}^{2}=\gamma_{0}^{H}-l_{30}^{2}-l_{31}^{2}-l_{32}^{2}
\end{gathered}
$$

which can be generalized to give for $i>0$

$$
l_{i i}^{2}=\gamma_{0}^{H}-\sum_{j=0}^{i-1} l_{i j}^{2}
$$

Next consider the off diagonal terms not in first column or row. Since the matrix is symmetric only the $i>j$ terms need to be considered

$$
\gamma_{1}^{H}=l_{20} l_{10}+l_{11} l_{21}
$$

$$
\begin{gathered}
r_{2}^{H}=l_{30} l_{10}+l_{31} l_{11} \\
r_{3}^{H}=l_{20} l_{30}+l_{21} l_{31}+l_{22} l_{32}
\end{gathered}
$$

Now for the first expression all terms are known from previous relation except $l_{21}$

$$
l_{21}=\frac{1}{l_{11}}\left(\gamma_{1}^{H}-l_{20} l_{10}\right)
$$

and $l_{31}$ is the only whknown in the second expression

$$
l_{31}=\frac{1}{l_{11}}\left(\gamma_{2}^{H}-l_{30} l_{10}\right)
$$

and finally in the third term only $l_{32}$ is unknown

$$
l_{32}=\frac{1}{l_{22}}\left(r_{1}^{H}-l_{30} l_{20}-l_{31} l_{21}\right)
$$

This can be generalized to give for $j<i$

$$
l_{i j}=\frac{1}{l_{j j}}\left[\gamma^{H}(i-j)-\sum_{k=0}^{j-1} l_{i k} l_{j k}\right]
$$

Is summary
I) $\quad l_{i_{0}}=\frac{\gamma_{i}^{H}}{l_{00}}$
II) $l_{i i}^{2}=\gamma_{0}^{4}-\sum_{j=0}^{i-1} l_{i j}^{2}$
III) $\ell_{i j}=\frac{1}{\ell_{j j}}\left[\gamma^{H}(i-j)-\sum_{k=0}^{j-1} \ell_{i k} \ell_{j k}\right]$

Since $\operatorname{Ln}$ is lower triangular

$$
l_{i j}=0 \text { for } j>1
$$

The expressions should be evaluated in the following order, recalling that $L_{n}$ is lower triangular. Define an $(n+1) \times(n+1)$ array and a function to
compute the autocorrelation by

$$
\begin{aligned}
& l(n+1, n+1) \\
& \gamma^{H}(n)=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
\end{aligned}
$$

Then the elements of array are given by

$$
\begin{aligned}
& j=0, i=0 \\
& l(0,0)=\sqrt{\gamma^{H}(0)} \\
& j=0, i=1 \\
& l(1,0)=\frac{\gamma^{H}(1)}{l(0,0)}=\frac{\gamma^{H}(1)}{\sqrt{\gamma^{H}(0)}} \\
& j=1, i=1 \\
& l(1,1)=\gamma^{H}(0)-l^{2}(1,0) \\
& =\gamma^{H}(0)-\frac{\left(\gamma^{H}(1)\right)^{2}}{\gamma^{H}(0)} \\
& j=0, i=2 \\
& l(2,0)=\frac{\gamma^{H}(2)}{l(0,0)}=\frac{\gamma^{H}(2)}{\sqrt{\gamma^{H}(0)}}
\end{aligned}
$$

$$
\begin{aligned}
& j=1, i=2 \\
& l(2,1)=\frac{1}{l(1,1)}\left[\gamma^{H}(1)-l(2,0) l(1,0)\right] \\
& j=2, l=2 \\
& l(2,2)=\gamma^{H}(0)-l^{2}(2,0)-l^{2}(2,1)
\end{aligned}
$$

This is enough to write pseudo code for evaluation of $L_{n}$
for $i=0$ to $n+1$
for $j=0$ to $i+1$
if $j=0$ and $i=0$
$l(i, j)=\sqrt{\gamma^{H}(0)}$
else if $j=0$

$$
l(i, j)=\frac{\gamma^{H}(i)}{l(0,0)}
$$

else if $i=j$

$$
l(i, j)=\gamma^{H}(0)-\sum_{k=0}^{i-1} l^{2}(i, k)
$$

else

$$
\begin{aligned}
l(i, j)= & \frac{1}{l(j, j)}\left[\gamma^{H}(i-j)\right. \\
& \left.-\sum_{k=0}^{j-1} l(i, k) l(j, k)\right]
\end{aligned}
$$

## Cholesky Decomposition Example

The autocorrelation for Fractional Brownian Noise is given by

$$
r_{n}^{H}=\frac{1}{2}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

The cholesky decomposed matrix $L$ is lower triangular with elements given by

$$
\begin{gathered}
l_{00}=1 \\
l_{i 0}=\frac{r_{i}^{H}}{l_{00}} \\
l_{i i}^{2}=r_{0}^{H}-\sum_{j=0}^{i-1} l_{i j}^{2} \\
l_{i j}=\frac{1}{l_{j i}}\left[r_{i-j}^{H}-\sum_{k=0}^{j-1} l_{i k} l_{j k}\right]
\end{gathered}
$$

Consider the case $n=3$ and $H=9 / 10$ autocovariance values are given by

$$
\begin{aligned}
& r_{0}=\frac{1}{1}\left(2^{18 / 10}-2\right)=\underline{0.741} \\
& r_{1}=\frac{1}{2}\left(2^{18 / 10}\right]=0.63 \\
& r_{2}=\frac{1}{2}\left[1+3^{18 / 10}-(2) 2^{18 / 10}+4^{18 / 10}-(2) 3^{18 / 10}\right]=0.58 \\
& r_{3}=\frac{1}{2}\left[2^{18 / 10}\right.
\end{aligned}
$$

The autocovariance matrix is given by

$$
R=\left[\begin{array}{cccc}
1 & 0.741 & 0.63 & 0.58 \\
0.741 & 1 & 0.741 & 0.63 \\
0.63 & 0.741 & 1 & 0.241 \\
0.58 & 0.63 & 0.741 & 1
\end{array}\right]
$$

The cholesky decomposed matrix is given by

$$
\begin{aligned}
l_{00} & =1 \\
l_{10} & =\frac{r_{1}}{l_{00}}=0.741 \\
l_{20} & =\frac{r_{2}}{l_{00}}=0.63 \\
l_{30} & =\frac{r_{3}}{l_{10}}=0.58 \\
l_{11} & =\sqrt{1.0}-l_{10}^{2}=\sqrt{1.0-0.55} \\
& =\sqrt{0.45}=0.671 \\
l_{21} & =\frac{1}{l_{11}}\left(r_{1}-l_{20} l_{10}\right) \\
& =\frac{1}{0.671}[0.741-(0.63)(0.741)] \\
& =0.408 \\
l_{22} & =\left[1-l_{20}^{2}-l_{21}^{2}\right]^{1 / 2}
\end{aligned}
$$

$$
\begin{aligned}
= & {\left[1-0.63^{2}-0.408^{2}\right]^{1 / 2} } \\
= & 0.661 \\
l_{31}= & \frac{1}{l_{11}}\left[r_{2}-l_{30} l_{10}\right] \\
= & \frac{1}{0.671}[0.63-(0.58)(0.741)] \\
= & 0.298 \\
l_{32}= & \frac{1}{l_{22}}\left[r_{1}-l_{30} l_{20}-l_{31} l_{21}\right] \\
= & \frac{1}{0.661}[0.741-(0.58)(0.63) \\
= & 0.384 \quad(0.298)(0.408)] \\
l_{33}= & {\left[r_{0}-l_{30}^{2}-l_{31}^{2}-l_{32}^{2}\right]^{1 / 2} } \\
= & {\left[1-(0.58)^{2}-(0.298)^{2}-(0.384)^{2}\right]^{1 / 2} } \\
= & 0.654
\end{aligned}
$$

Thus

$$
L=\left[\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0.741 & 0.671 & 0 & 0 \\
0.63 & 0.408 & 0.661 & 0 \\
0.58 & 0.298 & 0.384 & 0.654
\end{array}\right]
$$

## Cholesky Method Simulation Results

The following plots give a sense of how Fractional Brownian motion varies with the Hurst parameter $H$.
The first plots show simulations of Fractional Brownian noise for values of $H=0.2,0.5,0.9$. Each of the simulations used the same input Brownian nolse which is shown in the plot below.

## Brownian Noise

![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-391.jpg?height=747&width=1104&top_left_y=1176&top_left_x=215)

Since the input Brownian noise is the same for each simulation the only difference between the simulations is the autocorrelation matrix

Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.5$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-392.jpg?height=736&width=1104&top_left_y=566&top_left_x=245)

In the above plot $H=0.5$ so the output of the algorithm is the same as the input Brownian noise. In the next plots $H=0.9$ for the first and $H=0,2$ for the last
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-393.jpg?height=821&width=1162&top_left_y=100&top_left_x=203)
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-393.jpg?height=783&width=1130&top_left_y=1019&top_left_x=213)

For $H=0,9$ the high degree of correlation over long timescales is apparent. There is a notrcable bias in the noise toward negative values indicating a preference for positive noise morements lecding to a larger stan dard deviation over time. In the second plot there is even less structure tran seen in the input Brownian Noise. It will be seen that this leads to an even smaller standard deviation over time.
The following two plots show realizations of Fractional Brownian motion for a range of values of $H$. The first plot samples values of $1 / 2<H<1$ and the second the range $0<H \leqslant 1 / 2$. Recall that the standard deviation for Fractional Brownian motion is given by

$$
\sigma_{H}=n^{H}
$$

Fractional Brownian Motion Comparison
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-395.jpg?height=814&width=1221&top_left_y=126&top_left_x=209)

Fractional Brownian Motion Comparison
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-395.jpg?height=781&width=1186&top_left_y=1088&top_left_x=211)

For each of the simulations in the first plot

$$
\begin{aligned}
& \sigma_{0.95}=1000^{0.95}=708 \\
& \sigma_{0.9}=1000^{0.9}=501 \\
& \sigma_{0.8}=1000^{0.8}=251 \\
& \sigma_{0.7}=1000^{0.7}=126 \\
& \sigma_{0.6}=1000^{0.6}=63 \\
& \sigma_{0.55}=1000^{0.65}=45
\end{aligned}
$$

By inspection these values are seen to be cosistent with the simulation results.
For the second plot

$$
\begin{aligned}
& \sigma_{0.5}=1000^{0.5}=32 \\
& \sigma_{0.45}=1000^{0.45}=22 \\
& \sigma_{0.4}=1000^{0.4}=16 \\
& \sigma_{0.3}=1000^{0.3}=8
\end{aligned}
$$

$$
\begin{aligned}
& \sigma_{0.2}=1000^{0.2}=4 \\
& \sigma_{0.1}=1000^{0.1}=2
\end{aligned}
$$

Also these oalues are seen to be cosistent with simulation. Recall that for $0<H<1 / 2$ the autocorrelation is negative and decays very rapidly with increasing time. This anticorrelation leads to frequent changes in direction of the motion with the result that any deviations are quickly reverted This is in contrast to $1 / 2<H<1$ where deviadions accumulate because of the strong temporal correlation.
In a later section a more rigorus comporison will be prodided.

## Fast Fourier Transform Method

The cholesky Metod for generating Fractional Brownian Motion using the Multivariate Gaussian Distribution is straight forward but has computational complexity $O\left(n^{2}\right)$. In this section a method based on the FFT of circulant matrix is discussed. This method reduces the computational complexity to $O(N \ln N)$.

Eenerating Fractional Brownian Motion involves embeding the Covariance motix for Fractional Brownian motion in a circulant matrix then doing the decomposition

$$
\Gamma_{n}^{H}=G_{n} G_{n}^{\top}
$$

So that

$$
2_{n}^{H}=C_{n} B_{n}
$$

where $B_{n}$ is Brownian Norse and $Z_{n}^{H}$ Fractional Brownian soise.

## Circulant Matrix

A circulant matrix has the form

$$
C=\left[\begin{array}{ccccc}
c_{0} & c_{n-1} & c_{n-2} & \cdots & c_{1} \\
c_{1} & c_{0} & c_{n-1} & \cdots & c_{2} \\
c_{2} & c_{1} & c_{0} & \cdots & c_{3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_{n-1} & c_{n-2} & c_{n-3} & \cdots & c_{0}
\end{array}\right]
$$

Each row is the right shift of the preceeding row.
The Generating Circulant Matrix is defined by

$$
G=\left[\begin{array}{llllll}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \cdots & & 1 \\
0 & 0 & 0 & \cdots & \cdots & 0
\end{array}\right]
$$

Now

$$
\begin{aligned}
& G^{2}=\left[\begin{array}{llllll}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 & 0 \\
\vdots & \ddots & \cdots & \cdots & \vdots \\
0 & 0 & 0 & \cdots & 1 & 0
\end{array}\right] \\
& {\left[\begin{array}{llllll}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & - & \vdots \\
0 & 0 & 0 & \cdots & 1 & 0
\end{array}\right]} \\
& {\left[\begin{array}{lllll}
0 & 0 & 0 & \cdots & 1 \\
0 & 0 & 0 & \cdots & 0 \\
1 & 0 & 0 & \cdots & 0 \\
\vdots & \vdots & \cdots & 0 \\
0 & 0 & \cdots & 1 & 0 \\
1
\end{array}\right]}
\end{aligned}
$$

Squaring the generating matrix performs a left shift of the original matrix. It is straight forward to see that $G^{3}$ shifts each row left twice and
that

$$
G^{n}=G
$$

Each power of $C$ selects a different column in each row or likewise a different row in each column. consider the polynomial

$$
p(x)=c_{0}+c_{1} x+c_{2} x^{2}+\cdots c_{n-1} x^{n-1}
$$

It follows that the circulent matrix $c$ can be written as

$$
C=\rho(\epsilon)=c_{0} \underline{1}+c_{1} C+c_{2} C^{2}+\cdots+c_{n-1} C^{n-1}
$$

## Discret Fourier Transform

The discrete Fow ier Transform of a sequence of points

$$
\left\{f_{0}, f_{1}, f_{2}, \ldots, f_{n-1}\right\}
$$

is defined by

$$
\begin{aligned}
& f_{m}=\frac{1}{\sqrt{n}} \sum_{k=0}^{n-1} F_{k} e^{2 \pi i(k / n) m} \\
& F_{k}=\frac{1}{\sqrt{n}} \sum_{m=0}^{n-1} f_{m} e^{-2 \pi i\left(\frac{m}{n}\right) k}
\end{aligned}
$$

In matrix form

$$
\begin{aligned}
& F=T f \\
& f=T^{-1} F
\end{aligned}
$$

where

$$
\begin{aligned}
T_{m k} & =e^{-2 \pi i\left(\frac{m}{n}\right)^{k}} \quad 0<m, k<n \\
& =\left(e^{-2 \pi i \frac{1}{n}}\right)^{m k}
\end{aligned}
$$

It is easy to see that $T$ is Symmetric

50
let

$$
T_{k m}=T_{m k}
$$

$$
\begin{gathered}
T=T^{T} \\
\omega=e^{2 \pi i \frac{1}{n}} \\
\varepsilon=\omega^{*}=e^{-2 \pi i \frac{1}{n}}
\end{gathered}
$$

Thus

$$
T=\frac{1}{\sqrt{n}}\left[\begin{array}{ccccc}
1 & 1 & 1 & \cdots & 1 \\
1 & \varepsilon & \varepsilon^{2} & \cdots & \varepsilon^{n-1} \\
1 & \varepsilon^{2} & \varepsilon^{4} & \cdots & \varepsilon^{2(n-1)} \\
\vdots & \vdots & & \\
1 & \varepsilon^{n-1} & \varepsilon^{2(n-1)} & \cdots & \varepsilon^{(n-1)^{2}}
\end{array}\right]
$$

by definition

$$
\varepsilon^{n}=1
$$

thus

$$
\begin{aligned}
\varepsilon^{m(n-1)} & =\varepsilon^{(m n-m)} \\
& =\varepsilon^{(m-1) n+n-m}
\end{aligned}
$$

$$
\begin{aligned}
& =\varepsilon^{(m-1) n} \varepsilon^{n-m} \\
& =\left(\varepsilon^{n}\right)^{m-1} \varepsilon^{n-m} \\
& =\varepsilon^{n-m}
\end{aligned}
$$

Thus

$$
T=\frac{1}{\sqrt{n}}\left[\begin{array}{ccccc}
1 & 1 & 1 & \cdots & 1 \\
1 & \varepsilon & \varepsilon^{2} & \cdots & \varepsilon^{n-1} \\
1 & \varepsilon^{2} & \varepsilon^{4} & \cdots & \varepsilon^{n-2} \\
1 & \varepsilon^{3} & \varepsilon^{6} & \cdots & \varepsilon^{n-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \varepsilon^{n-1} & \varepsilon^{n-2} & \cdots & \varepsilon^{2}
\end{array}\right]
$$

Taking the complex conjugate and traspose

$$
T^{*}=\frac{1}{\sqrt{n}}\left[\begin{array}{ccccc}
1 & 1 & 1 & \cdots & 1 \\
1 & \omega & \omega^{2} & \cdots & \omega^{n-1} \\
1 & \omega^{2} & \omega^{4} & \cdots & \omega^{n-2} \\
1 & \omega^{3} & \omega^{6} & \cdots & \omega^{n-3} \\
\vdots & \vdots & \ddots & \ddots & \omega^{2} \\
1 & \omega^{n-1} & \omega^{n-2} & \cdots & \omega^{\prime}
\end{array}\right]
$$

Now from orthoganality of the Fowier basis and the definition of the inverse of $T$, namely)

$$
T T^{-1}=\mathbb{1}
$$

It follows that

$$
T^{-1}=T^{*}
$$

thus $T$ is unitany

## Fourier Decomposition of Circulant Matrix

Consider the circulant matrix generator

$$
G=\left[\begin{array}{llllll}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & \ddots & \cdots & & \vdots \\
0 & 0 & 0 & \cdots & \cdots & 0
\end{array}\right]
$$

Muttiplying by the Fourier matrix gues

$$
T G=\frac{1}{\sqrt{n}}\left[\begin{array}{ccccc}
1 & \varepsilon & \varepsilon^{2} & \cdots & \varepsilon^{n-1} \\
1 & \varepsilon^{2} & \varepsilon^{4} & \cdots & \varepsilon^{n-2} \\
1 & \varepsilon^{3} & \varepsilon^{6} & \cdots & \varepsilon^{n-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \varepsilon^{n-1} & \varepsilon^{n-2} & \cdots & \varepsilon^{2}
\end{array}\right]
$$

$$
\begin{aligned}
& {\left[\begin{array}{cccccc}
0 & 0 & 0 & \cdots & 0 & 1 \\
1 & 0 & 0 & \cdots & 0 & 0 \\
0 & 1 & 0 & \cdots & 0 & 0 \\
0 & 0 & 1 & & & \\
\vdots & \vdots & \ddots & \cdots & \vdots \\
0 & 0 & 0 & \cdots & \cdots & 0
\end{array}\right]} \\
& =\frac{1}{\sqrt{n}}\left[\begin{array}{cccccc}
1 & 1 & 1 & \cdots & 1 & 1 \\
\varepsilon & \varepsilon^{2} & \varepsilon^{3} & \varepsilon^{n-1} & 1 \\
\varepsilon^{2} & \varepsilon^{4} & \varepsilon^{6} & \cdots & \varepsilon^{n-2} & 1 \\
\varepsilon^{3} & \varepsilon^{6} & \varepsilon^{9} & \cdots & \varepsilon^{n-3} & 1 \\
\varepsilon^{n-1} & \varepsilon^{n-2} & \varepsilon^{n-3} & \cdots & \varepsilon & 1
\end{array}\right]
\end{aligned}
$$

This matrix can be factored to give

$$
T G=\frac{1}{\sqrt{n}}\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \varepsilon^{n-1}
\end{array}\right]
$$

$$
\left[\begin{array}{ccccc}
1 & 1 & 1 & \cdots & 1 \\
1 & \varepsilon & \varepsilon^{2} & \cdots & \varepsilon^{n-1} \\
1 & \varepsilon^{2} & \varepsilon^{4} & \cdots & \varepsilon^{2(n-1)} \\
\vdots & \vdots & & & \\
1 & \varepsilon^{n-1} & \varepsilon^{2(n-1)} & \cdots & \varepsilon^{(n-1)^{2}}
\end{array}\right]
$$

Thus

$$
T G=\Lambda
$$

and

$$
T G T^{-1}=\Lambda
$$

where $\triangle$ is the diagonal matrix

$$
\Lambda=\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{2} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \varepsilon^{n-1}
\end{array}\right]
$$

Thus the Fourier Transform diagonalizes the circulant matrix generator $G$

Consider the circulant Matrix

$$
\begin{aligned}
& C=\left[\begin{array}{ccccc}
c_{0} & c_{n-1} & c_{n-2} & \cdots & c_{1} \\
c_{1} & c_{0} & c_{n-1} & \cdots & c_{2} \\
c_{2} & c_{1} & c_{0} & \cdots & c_{3} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_{n-1} & c_{n-2} & c_{n-3} & \cdots & c_{0}
\end{array}\right] \\
& C=p(E)=c_{0} \underline{1}+c_{1} G+c_{2} G^{2}+\cdots+c_{n-1} G^{n-1} \\
& \text { It } \text { follows that } \\
& T C T^{-1}=T\left[c_{0} \underline{1}+c_{1} C+c_{2} G^{2}+\cdots+\right. \\
& \left.c_{n-1} G^{n-1}\right] T^{-1} \\
& =c_{0} T \underline{11} T^{-1}+c_{1} T G T^{-1}+c_{2} T G^{2} T^{-1} \\
& +\cdots+c_{n-1} T G^{n-1} T^{-1} \\
& =c_{0} \underline{1}+c_{1} T G T^{-1}+c_{2}\left(T G T^{-1}\right)\left(T G T^{-1}\right) \\
& +\cdots+c_{n-1}\left(T \in T^{-1} X T G T^{-1}\right) \cdots\left(T G T^{-1}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & C_{0} 11+C_{1} \Lambda+C_{2}\left(T C T^{-1}\right)^{2}+\cdots+ \\
& C_{n-1}\left(T \in T^{-1}\right)^{n-1} \\
= & C_{0} 11+C_{1} \Lambda+C_{2}(\Delta)^{2}+\cdots+C_{n-1}(\Delta)^{n-1}
\end{aligned}
$$

Now

$$
\begin{aligned}
& \Delta^{2}=\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon^{2} & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{4} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & & \varepsilon^{2(n-1)}
\end{array}\right] \\
& \Delta^{n-1}=\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon^{n-1} & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{2(n-1)} & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots \\
0 & 0 & 0 & \varepsilon^{(n-1)^{2}}
\end{array}\right]
\end{aligned}
$$

It follows that

$$
\begin{array}{rl}
T C T^{-1} & =C_{0}\left[\begin{array}{lllll}
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{array}\right] \\
+ & C_{1}\left[\begin{array}{lllll}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{2} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \varepsilon^{n-1}
\end{array}\right] \\
+ & C_{2}\left[\begin{array}{ccccc}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon^{2} & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{4} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \varepsilon^{2(n-1)}
\end{array}\right] \\
+\cdots+C_{n-1} & 0 \\
{\left[\begin{array}{lllll}
1 & 0 & 0 & \cdots & 0 \\
0 & \varepsilon^{n-1} & 0 & \cdots & 0 \\
0 & 0 & \varepsilon^{2(n-1)} & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots \\
0 & 0 & 0 & \varepsilon^{(n-1)^{2}}
\end{array}\right]}
\end{array}
$$

This result is a diagonal matrix

$$
\begin{aligned}
\left(T C T^{-1}\right)_{0,0}= & C_{0}+C_{1}+C_{2}+\cdots+C_{n-1} \\
= & P(1) \\
\left(T C T^{-1}\right)_{1,1}= & C_{0}+C_{1} \varepsilon+C_{2} \varepsilon^{2}+\cdots+C_{n-1} \varepsilon^{n-1} \\
= & P(\varepsilon) \\
\left(T C T^{-1}\right)_{2,2}= & C_{0}+C_{1} \varepsilon^{2}+C_{2} \varepsilon^{4}+\cdots+C_{n-1} \varepsilon^{2(n-1)} \\
= & P\left(\varepsilon^{2}\right) \\
\left(T C T^{-1}\right)_{n-1, n-1}= & C_{0}+C_{1} \varepsilon^{n-1}+C_{2} \varepsilon^{2(n-1)}+ \\
& \cdots+C_{n} \varepsilon^{(n-1)^{2}} \\
= & P\left(\varepsilon^{n-1}\right)
\end{aligned}
$$

Thus the Fowrier Decomposition of a circulant matrix is given by

$$
T C T^{-1}=\left[\begin{array}{ccccc}
p(1) & 0 & 0 & \cdots & 0 \\
0 & p(\varepsilon) & 0 & \cdots & 0 \\
0 & 0 & p\left(\varepsilon^{2}\right) & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & p\left(\varepsilon^{n-1}\right)
\end{array}\right]
$$

## Embedding of Fractional Brownian Motion Couariance Matrix in a Circulant Matrix

Recall that the Fractional Brownian Moution autocovariance function is given by
$\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]$
where

$$
\gamma_{0}^{H}=\Delta t^{2 H}
$$

and the covariance matrix is given by

$$
\Gamma_{n-1}^{H}=\left[\begin{array}{ccccc}
\gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} & \cdots & \gamma_{n-1}^{H} \\
\gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} & \cdots & \gamma_{n-2}^{H} \\
\gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H} & \cdots & \gamma_{n-3}^{H} \\
\vdots & \vdots & \vdots & & \\
\gamma_{n-1}^{H} & \gamma_{n-2}^{H} & \gamma_{n-3}^{H} & \cdots & \gamma_{0}^{H}
\end{array}\right]
$$

Now $\Gamma_{n}^{H}$ is not a circulant matrix but a circulant matrix can be constructed in the following manner,

The autocovariance matrix, $\Gamma_{n}^{H}$, is embedded in the upper left corner of $c$ as indicated also note that

$$
C_{0, k}= \begin{cases}\gamma_{k}^{H} & k=0,1, \ldots, n-1 \\ \gamma_{2 n-k}^{H} & k=n+2, \ldots, 2 n-1\end{cases}
$$

$C$ is square $M \times M$ matrix. Here $M=2 n$. The minimal embedding has $M=2(n-1)$ but any $M \geqslant 2(n-1)$ will do. Here a single column of O padding is used but more are possible. Here $M=2 n$ will be used.

In the previals section it was shown that any circulant matrix has a Fourier pecomposition

$$
C=T \Delta T^{-1}
$$

where $T$ is a Fourie Transform matrix,

$$
T_{j, k}=\frac{1}{\sqrt{2 n}} e^{-2 \pi i\left(\frac{j K}{2 n}\right)} \quad j, K=0,1,2, \cdot \cdot 2 n-1
$$

and $\Delta$ is a diagonal matrix with elements

$$
\lambda_{k}=\sum_{j=0}^{2 n-1} c_{0, j} e^{-2 \pi i\left(\frac{j k}{2 n}\right)}
$$

If it is assumed that $C$ is positive definite and symetric the $\lambda_{k}$ are positive and real.

Next consider

$$
S=T \Lambda^{1 / 2} T^{-1}
$$

where $\Delta^{1 / 2}$ is a diagonal matrix with elements

$$
\left(\Lambda^{1 / 2}\right)_{k}=\sqrt{\lambda_{k}}
$$

Now $\tau$ is unitary so,

$$
T^{-1}=T^{*}
$$

so

$$
\begin{aligned}
S^{*} & =\left(T \Lambda^{1 / 2} T^{*}\right)^{*} \\
& =T \Lambda^{1 / 2} T^{*} \\
& =S
\end{aligned}
$$

since $\Lambda^{1 / 2}$ is real. It follows that

$$
S S^{*}=\left(T \Lambda^{1 / 2} T^{*}\right)\left(T \Lambda^{1 / 2} T^{*}\right)
$$

continuing the calculation

$$
\begin{aligned}
S S^{*} & =\left(T \Lambda^{1 / 2} T^{*} T \Lambda^{1 / 2} T^{*}\right) \\
& =T \Lambda^{1 / 2} \Lambda^{1 / 2} T^{*} \\
& =T \Lambda^{*} \\
& =T \Delta T^{-1} \\
& =C
\end{aligned}
$$

Thus

$$
C=S S^{*}
$$

is the decomposition of the couariance matrix needed to solve

$$
R_{n}^{H}=S B_{n}
$$

## Implementation of Algorithm

It has been shown that given the autocavariance function for Fractional Brownican motion,

$$
\gamma_{n}^{H}=\frac{1}{2} \Delta t^{2 H}\left[(n-1)^{2 H}+(n+1)^{2 H}-2 n^{2 H}\right]
$$

where

$$
\gamma_{0}^{H}=\Delta t^{2 H}
$$

and the autocovariace matrix

$$
\Gamma_{n-1}^{H}=\left[\begin{array}{ccccc}
\gamma_{0}^{H} & \gamma_{1}^{H} & \gamma_{2}^{H} & \cdots & \gamma_{n-1}^{H} \\
\gamma_{1}^{H} & \gamma_{0}^{H} & \gamma_{1}^{H} & \cdots & \gamma_{n-2}^{H} \\
\gamma_{2}^{H} & \gamma_{1}^{H} & \gamma_{0}^{H} & \cdots & \gamma_{n-3}^{H} \\
\vdots & \vdots & \vdots & & \\
\gamma_{n-1}^{H} & \gamma_{n-2}^{H} & \gamma_{n-3}^{H} & \cdots & \gamma_{0}^{H}
\end{array}\right]
$$

that $\Gamma_{n-1}^{H}$ can be embedded in a circulant matrix,

Where $c$ is diagonalized by the Fourier matrix,

$$
T_{j, k}=\frac{1}{\sqrt{2 n}} e^{-2 \pi i\left(\frac{j k}{2 n}\right)} \quad j, k=0,1,2, \ldots 2 n-1
$$

Let $\Lambda$ denote the diagonal matrix which has elements

$$
\lambda_{k}=\sum_{j=0}^{2 n-1} c_{0, j} e^{-2 \pi i\left(\frac{j k}{2 n}\right)}
$$

The circulant matrix, $c$, can be decomposed

$$
C=s s^{*} \quad \text { conjugate }
$$

where $s^{*}$ is the conjugate transpose of $S$ which is given

$$
S=T \Lambda^{1 / 2} T^{*}
$$

It follows that Fractional Brownian Noise can be computed frow Browian Norse by evaluating

$$
\begin{aligned}
Z^{H} & =S B \\
& =T \Lambda^{1 / 2} T^{*} B
\end{aligned}
$$

The steps needed to perform this calculation are as follows.
I) Compute the eigenvalues using

$$
\lambda_{k}=\sum_{j=0}^{2 n-1} C_{0, j} e^{-2 \pi i\left(\frac{j k}{2 n}\right)}
$$

where $C_{0, j}$ is the first row of the circulant matrix $c$ in which $\Gamma_{n}^{\prime t}$ is embeded,

$$
C_{0, k}= \begin{cases}\gamma_{k}^{H} & k=0,1, \ldots, n-1 \\ \gamma_{2 n-k}^{H} & k=n+2, \ldots, 2 n-1\end{cases}
$$

Define the column vectors

$$
C_{0}=\left[\begin{array}{c}
C_{0,0} \\
C_{0,1} \\
C_{0,2} \\
\vdots \\
C_{0,2 n-1}
\end{array}\right] \quad \lambda=\left[\begin{array}{c}
\lambda_{0} \\
\lambda_{1} \\
\lambda_{2} \\
\vdots \\
\lambda_{2 n-1}
\end{array}\right]
$$

Then

$$
\lambda=T C_{0}
$$

Thus the eigenvalues are the Fourler transform of the vector Co which can be evaluated using an FFT.

Then

$$
\Lambda^{1 / 2}=\left[\begin{array}{ccccc}
\sqrt{\lambda_{0}} & 0 & 0 & \cdots & 0 \\
0 & \sqrt{\lambda_{1}} & 0 & \cdots & 0 \\
0 & 0 & \sqrt{\lambda_{2}} & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \\
0 & 0 & 0 & \sqrt{\lambda_{2 n-1}}
\end{array}\right]
$$

## II) Compute $T^{*} \mathbb{B}$

This matrix multiplication can be shown to have the same distribution as using the following scheme to generate T* (B)

Consider the vector of Brownian Norse of length $2 n$, denoted by $\mathbb{B}_{2 n}$ the inverse Fourier transform of $B_{2 n}$ is given by

$$
\omega=T^{*} \mathbb{B}
$$

the covariance of $\omega$ is given by

$$
\begin{aligned}
\operatorname{Cov}(\omega) & =E\left(\omega \omega^{*}\right) \\
& =E\left[\left(T^{*} B\right)\left(T^{*} B\right)^{*}\right] \\
& =E\left[\left(T^{*} B\right)\left(\mathbb{B}^{\top} T\right)\right] \\
& =E\left(T^{*} \mathbb{B} B^{\top} T\right)
\end{aligned}
$$

$$
=T^{*} E\left(\mathbb{B} \mathbb{B}^{\top}\right) T
$$

By definition

$$
\operatorname{COO}(B)=E\left(B B^{T}\right)=\underline{1}
$$

thus

$$
\operatorname{Cov}(\omega)=T^{*} T=\mathbb{1}
$$

Now consider the following process

1. Generate two independent unit normal random variables, $D_{0}$ and $D_{n}$ and set

$$
\begin{aligned}
& \omega_{0}=D_{0} \\
& \omega_{n}=D_{n}
\end{aligned}
$$

2. For each $1 \leqslant j<n$ generate two independent unit normal random variables $D_{j}$ and $E_{j}$

$$
\begin{aligned}
& \omega_{j}=\frac{1}{\sqrt{2}}\left(D_{j}+i E_{j}\right) \\
& \omega_{2 n-j}=\frac{1}{\sqrt{2}}\left(D_{j}-i E_{j}\right)
\end{aligned}
$$

Then $\omega$ is given by the vector

$$
\omega=\left[\begin{array}{c}
D_{0} \\
\frac{1}{2}\left(D_{1}+i E_{2}\right) \\
\frac{1}{2}\left(D_{2}+i E_{2}\right) \\
\vdots \\
\frac{1}{2}\left(D_{n-1}+i E_{n-1}\right) \\
D_{n} \\
\frac{1}{2}\left(D_{n-1}-i E_{n-1}\right) \\
\vdots \\
\frac{1}{2}\left(D_{2}-i E_{2}\right) \\
\frac{1}{\sqrt{2}}\left(D_{1}-i E_{1}\right)
\end{array}\right]
$$

It follows that
$\omega \omega^{*}=\left[\begin{array}{c}D_{0} \\ \frac{1}{\sqrt{2}}\left(D_{1}+i E_{2}\right) \\ \frac{1}{2}\left(D_{2}+i E_{2}\right) \\ \vdots \\ \frac{1}{2}\left(D_{n-1}+i E_{n-1}\right) \\ D_{n} \\ \frac{1}{2}\left(D_{n-1}-i E_{n-1}\right) \\ \vdots \\ \frac{1}{2}\left(D_{2}-i E_{2}\right) \\ \frac{1}{\sqrt{2}}\left(D_{1}-i E_{1}\right)\end{array}\right]$

$$
\begin{aligned}
& {\left[D_{0} \frac{1}{12}\left(D_{1}-i E_{1}\right) \quad \frac{1}{12}\left(D_{2}-i E_{2}\right) \cdots\right.} \\
& \frac{1}{12}\left(D_{n-1}-i E_{n-1}\right) D_{n} \frac{1}{12}\left(D_{n-1}+i E_{n-1}\right) \cdots \\
& \left.\frac{1}{12}\left(D_{2}+i E_{2}\right) \frac{1}{12}\left(D_{1}+i E_{1}\right)\right]
\end{aligned}
$$

$$
\left[\begin{array}{cccc}
D_{0}^{2} & \frac{1}{2}\left(D_{0} D_{1}-i D_{0} E_{1}\right) & \cdots & D_{0} D_{n} \\
\frac{1}{2}\left(D_{0} D_{1}-i D_{0} D_{1}\right) & \frac{1}{2}\left(D_{1}^{2}+E_{1}^{2}\right) & \cdots & \frac{1}{2}\left(D_{n} D_{1}-i D_{n} E_{1}\right) \\
\vdots & \vdots & \vdots \\
D_{0} D_{n} & \frac{1}{2}\left(D_{n} D_{1}+i D_{n} E_{1}\right) & \cdots & D_{n}^{2} \\
\vdots & \vdots & & \vdots \\
\frac{1}{2}\left(D_{0} D_{1}+i D_{0} E_{i}\right) & \frac{1}{2}\left(D_{1}^{2}-E_{1}^{2}+2 i E_{1} D_{1}\right) & \frac{1}{2}\left(D_{n} D_{1}+i D_{n} E_{1}\right)
\end{array}\right.
$$

$$
\left.\begin{array}{l}
\cdots \frac{1}{2}\left(D_{0} D_{1}+i D_{0} E_{1}\right) \\
\cdots \frac{1}{2}\left(D_{1}^{2}-E_{1}^{2}+2 i E_{1} D_{1}\right) \\
\vdots \\
\cdots \frac{1}{2}\left(D_{n} D_{1}-i D_{n} E_{1}\right) \\
\cdots \frac{1}{2}\left(D_{1}^{2}+E_{1}^{2}\right)
\end{array}\right]
$$

Since $D_{i}$ and $E_{i}$ are indipendent wnit normal random variables the coveriance of the elements of $\omega^{*}$ is given by

$$
\begin{aligned}
& E\left(D_{0}^{2}\right)=E\left(D_{1}^{2}\right)=1 \\
& \frac{1}{2} E\left(D_{i}^{2}+E_{i}^{2}\right)=1 \\
& E\left[\frac{1}{2}\left(D_{n} D_{i}-i D_{n} E_{i}\right)\right]=0 \\
& E\left[\frac{1}{2}\left(D_{0} D_{i}-i D_{0} E_{i}\right)\right]=0 \\
& E\left[\frac{1}{2}\left(D_{i}^{2}-E_{i}^{2}+2 i E_{i} D_{i}\right)\right] \\
& =\frac{1}{2}(1-1+0)=0
\end{aligned}
$$

and for i7 $j$ the terms will be of the form

$$
\begin{aligned}
& E\left[\frac{1}{2}\left(D_{i}+i E_{i}\right)\left(D_{j}-i E_{j}\right)\right] \\
= & E\left[\frac{1}{2}\left(D_{i} D_{j}+E_{i} E_{j}+i E_{i} D_{j}-i E_{j} D_{i}\right)\right] \\
= & 0 \\
E & {\left[\frac{1}{2}\left(D_{i}-i E_{i}\right)\left(D_{j}+i E_{j}\right)\right] } \\
= & E\left[\frac{1}{2}\left(D_{i} D_{j}+E_{i} E_{j}-i E_{i} D_{j}+i E_{j} D_{i}\right)\right] \\
= & 0
\end{aligned}
$$

$$
\begin{aligned}
& E\left[\frac{1}{2}\left(D_{i}+i E_{i}\right)\left(D_{j}+i E_{j}\right)\right] \\
& \left.=\frac{1}{2} E\left(D_{i} D_{j}-E_{i} E_{j}+i E_{i} D_{j}+i D_{i} E_{j}\right)\right] \\
& =0 \\
& E\left[\frac{1}{2}\left(D_{i}-i E_{i}\right)\left(D_{j}-i E_{j}\right)\right] \\
& =\frac{1}{2} E\left(D_{i} D_{j}-E_{i} E_{j}-i E_{i} D_{j}-i E_{j} D_{i}\right) \\
& =0
\end{aligned}
$$

thus only the off diagonal elements are not zero and the diggonal elements are 1. so

$$
\operatorname{Cov}(\omega)=E\left(\omega \omega^{*}\right)=1
$$

Thus the vector $w$ constucted bil the process described has the same distribution as ( $T^{*} B$ ) since both are gaussian processes.
It follows that

$$
\left(T^{*} B\right)_{i}=\frac{1}{\sqrt{2 n}} \omega_{i}
$$

where $\sqrt[1 / a n]{a n}$ is the normalization term for $\tau^{*}$.

## III) Compute the final result <br> $$
Z=F \Delta^{\prime 2}\left(T^{*} \mathbb{B}\right)
$$

Frow the previous steps both $\Lambda^{1 / 2}$ and ( $T^{*} B$ ) are known and since ( $T * B$ ) is a column vector and $\Lambda^{1 / 2}$ is dragonal the matrix multiplic ation can be readily performed producing a column vector

$$
J=\Lambda^{1 / 2}\left(T^{*} \mathbb{B}\right)
$$

So

$$
\begin{aligned}
(J)_{i} & =\left(\Lambda^{1 / 2}\right)_{i}\left(T^{*} \mathbb{B}\right)_{i} \\
& =\frac{\lambda_{i}}{\sqrt{2 n}} \omega_{i}
\end{aligned}
$$

It follows that the final result producing $\mathbb{Z}$ is the Fourier transform of $J$, namely,

$$
R=T J
$$

which can be computed using ansther FFT.
Discard all but the first $n$ elements of 2 since only these will have the desired cooartance structure.

Finally Fractional Brownian Motion is computed from the cumulative summation

$$
Z_{m}^{H}=\sum_{i=0}^{m}\left(Z^{H}\right)_{i}
$$

which is equivalent to the recursion relation

$$
\begin{aligned}
z_{0}^{H} & =0 \\
z_{i}^{H} & =z_{i-1}^{H}+\left(z^{H}\right)_{i} \quad i=1,2,3, \ldots, n
\end{aligned}
$$

## FFT Method Simulation Results

## The FFT Method assumes that

the eigenvales of the circulant autocovariance matrix are real and positive. For values of $H \geqslant 0.9$ and $n=1024$ this assumption is invalid. Simulations for $A \leqslant 0.915$ can be performed by increasing $n$ to 8196. For larger values of A another method is required.
First simulations that scan values of $0<H<0.89$ with $n=1024$ are compared. Then ensembles of simulations are performed and the mean, standard deviation and autocorrelation coefficent are computed from the simulations and compared with the results obatined analytically, namely

$$
\mu=0 \quad o=t^{H}
$$

and

$$
r(t)=\frac{1}{2}\left[(t-1)^{2 H}+(t+1)^{2 H} \cdot 2 t^{2 H}\right]
$$

Now for the following simulations the input Brownian noise is the same for each simulation the only difference between the the autocorrelation matrix
The following plot shows the input Browhian noise used for simulations with $H=0.5,0.89$ and 0.2 .

Brownian Noise
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-435.jpg?height=757&width=1150&top_left_y=1225&top_left_x=245)

![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-436.jpg?height=690&width=1033&top_left_y=199&top_left_x=310)

In the above plot $H=0.5$. For the cholesky algorithm the input noise is left unchanged by the algorthm but for the FFT algorithm this is not the case because of the calculation of $T^{*} B$ is step II which is not computed as the Inverse Focier trasform of the input noise but is constructed using an algorithm that produces a result that with the saml distribution. The norse can
still be seen to stucturally similar to the input. This is not the case in the following two plots where in the forst $H=0.89$ and for the second $H=0,2$

FFT Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.89$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-437.jpg?height=776&width=1198&top_left_y=665&top_left_x=201)

For $H=0.89$ case the high degree of correlation over long timescales is apparent from the decressed frequency in change of sigh for noise inorements when compored
to the $H=0.5$ and $t=0.2$ cases. This inturn leads to a larger varlance.

FFT Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.2$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-438.jpg?height=783&width=1186&top_left_y=445&top_left_x=223)

In the second plot there is even less structure tran seen in the input Brownian Noise. It will be seen that this leads to an even smaller standard deviation over time.

The following two plots show realizations of Fractional Brownian motion for a range of values of $H$. The first plot samples values of $1 / 2<H<1$ and the second the range $0<H \leqslant 1 / 2$. Recall that the standard deviation for Fractional Brownian motion is given by

$$
\sigma_{H}=t^{H}
$$

FFT Fractional Brownian Motion Comparison
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-439.jpg?height=828&width=1248&top_left_y=1051&top_left_x=167)

![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-440.jpg?height=863&width=1226&top_left_y=133&top_left_x=197)

For each of the simulations in the first plot

$$
\begin{aligned}
& \sigma_{0.89}=1024^{0.89}=470 \\
& \sigma_{0.8}=1024^{0.8}=251 \\
& \sigma_{0.7}=1024^{0.7}=126 \\
& \sigma_{0.6}=1024^{0.6}=63 \\
& \sigma_{0.55}=1024^{0.65}=45
\end{aligned}
$$

By inspection these values are seen to be cosistent with the simulation results.
For the second plot

$$
\begin{aligned}
& \sigma_{0.5}=1024^{0.5}=32 \\
& \sigma_{0.45}=1024^{0.45}=22 \\
& \sigma_{0.4}=1024^{0.4}=16 \\
& \sigma_{0.3}=1024^{0.3}=8 \\
& \sigma_{0.2}=1024^{0.2}=4 \\
& \sigma_{0.1}=1024^{0.1}=2
\end{aligned}
$$

Also these oalues are seen to be cosistent with simulation. Recall that for $0<H<1 / 2$ the autocorrelation is negative and decays very rapidly with increasing time. This anticorrelation leads to frequent changes in direction of the
motion with the result that any deviations are quickly reverted This is in contrast to $1 / 2<H<1$
where deviations accumulate because of the strong temporal correlation.
The following plot shows the result of a simulation with $H=0.91$ and $n=8196$. It is seen to be consistent with

$$
\sigma_{0.91}=3642
$$

FFT Fractional Brownian Noise: $\Delta \mathrm{t}=1.0, \mathrm{H}=0.91$
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-442.jpg?height=834&width=1256&top_left_y=1039&top_left_x=187)

In the remainder of this section the results of ensembles of simulations are used to evaluate the mean, standard deviation and autocorrelation coefficient and compared with the analytic results of

$$
\begin{gathered}
\mu=0 \\
\sigma_{H}=t^{H} \\
r_{H}=\frac{1}{2}\left[(t-1)^{2 H}+(t+1)^{2 H}-2 t^{2 H}\right]
\end{gathered}
$$

For the first $H=0,5$ producing Brownian motion with

$$
\begin{aligned}
& \mu=0 \quad \sigma_{0.5}=\mathbb{E} \\
& r_{H}=0
\end{aligned}
$$

The ensemble of 500 simulations used in the analysis are shown in the following plot

Fractional Brownian Motion Ensemble, Ensemble Size=500, H=0.5
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-444.jpg?height=760&width=1174&top_left_y=161&top_left_x=199)

and $\mu$, Sos and $r_{0.5}$ are shown in the following plots

Fractional Brownian Motion Ensemble $\mu$, Ensemble Size $=500$, H=0.5
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-444.jpg?height=680&width=1020&top_left_y=1245&top_left_x=280)

Fractional Brownian Motion Ensemble $\sigma$, Ensemble Size=500, H=0.5
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-445.jpg?height=779&width=1146&top_left_y=153&top_left_x=217)
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-445.jpg?height=797&width=1164&top_left_y=1060&top_left_x=233)

All results are seen to be cosistent with the analytic results
For the next ensemble of 500 simulations with $H=0.3$ is shown below and are consistent with the analytic results.

Fractional Brownian Motion Ensemble, Ensemble Size=500, H=0.3
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-446.jpg?height=896&width=1358&top_left_y=874&top_left_x=116)
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-447.jpg?height=841&width=1208&top_left_y=70&top_left_x=203)
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-447.jpg?height=874&width=1230&top_left_y=1009&top_left_x=209)

Fractional Brownian Noise Ensemble $\gamma$, Ensemble Size=500, H=0.3
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-448.jpg?height=761&width=1126&top_left_y=130&top_left_x=233)

Finally results of several ensembles scanning high values of H. For the first $H=0,8$ and consists of 500 simulations.
The first plots show the simulations, mean and standar deviation. The results are in agreement with the analytic results and consistent with prevides results.

Fractional Brownian Motion Ensemble, Ensemble Size=500, H=0.8
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-449.jpg?height=762&width=1156&top_left_y=149&top_left_x=245)

Fractional Brownian Motion Ensemble $\mu$, Ensemble Size=500, H=0.8
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-449.jpg?height=744&width=1120&top_left_y=1056&top_left_x=257)

Fractional Brownian Motion Ensemble $\sigma$, Ensemble Size $=500$, H=0.8
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-450.jpg?height=718&width=1110&top_left_y=187&top_left_x=225)

The following plot shows the autocorrelation. For 4 close to 1 the decay with time becomes slow and is not accuratly captured by the simulation. The simulated actocorrelation decays more rapidly than the analytic result as seen in the following pot. This behaviour was anfurmed using a sqerate implimentation from the python fbm package. This behavior is also seen in the Cholesky implementation.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-451.jpg?height=689&width=1006&top_left_y=112&top_left_x=278)

The next plot shows the result obtained for $t=0,7$ where the simulation and analytic results are closer.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-451.jpg?height=775&width=1124&top_left_y=1138&top_left_x=257)

Finally the result of a sim ulation with $H=0,9$ are shown and a larger departwre between simulation and the analytic result is soserved.
![](https://cdn.mathpix.com/cropped/2025_09_20_e14e4cad607554a269f4g-452.jpg?height=769&width=1116&top_left_y=624&top_left_x=233)

