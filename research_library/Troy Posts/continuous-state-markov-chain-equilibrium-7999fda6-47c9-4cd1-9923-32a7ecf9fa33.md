# Continuous State Markov Chain Equilibrium 

Aug 16, 2018 • Troy Stribling

A Markov Chain is a sequence of states where transitions between states occur ordered in time with the probability of transition depending only on the previous state. Here the states will be assumed a continuous unbounded set and time a discrete unbounded set. If the set of states is given by, $x \in \mathbb{R}$, the probability that the process will be in state $x$ at time $t$, denoted by $\pi_{t}(y)$, is referred to as the distribution. Markov Chain equilibrium is defined by $\lim _{t \rightarrow \infty} \pi_{t}(y)<\infty$, that is, as time advances $\pi_{t}(y)$ becomes independent of time. Here a solution for this limit is discussed and illustrated with examples.

## Model

The Markov Chain is constructed from the set of states $\{x\}$, ordered in time, where $x \in \mathbb{R}$. The process starts at time $t=0$ with state $X_{0}=x$. At the next step, $t=1$, the process will assume a state $X_{1}=y, y \in\{x\}$, with probability $P\left(X_{1}=y \mid X_{0}=x\right)$ since it will depend on the state at $t=0$ by the definition of a Markov Process. At the next time step $t=2$ the process state will be $X_{2}=z$, where $z \in\{x\}$ with probability,

$$
P\left(X_{2}=z \mid X_{0}=x, X_{1}=y\right)=P\left(X_{2}=z \mid X_{1}=y\right),
$$

since by definition the probability of state transition depends only upon the state at the previous time step. For an arbitrary time the transition from a state $X_{t}=x$ to a state $X_{t+1}=y$ will occur with probability, $P\left(X_{t+1}=y \mid X_{t}=x\right)$ that is independent of $t$. The Transition Kernel, defined by,

$$
p(x, y)=P\left(X_{t+1}=y \mid X_{t}=x\right)
$$

plays the same role as the transition matrix plays in the theory of Discrete State Markov Chains. In general $p(x, y)$ cannot always be represented by a probability density function, but here it is assumed that it has a density function representation. This leads to the interpretation that for a known value of $x p(x, y)$ can be interpreted as a conditional probability density for a transition to state $y$ given that the process is in state $x$, namely,

$$
p(x, y)=f(y \mid x)
$$

Consequently, $p(x, y)$ is a family of conditional probability distributions each representing conditioning on a possible state of the chain at time step $t$. Since $p(x, y)$ is a conditional probability density for each value of $x$ it follows that,

$$
\begin{gather*}
\int_{-\infty}^{\infty} p(x, y) d y=1 \forall x  \tag{1}\\
p(x, y) \geq 0 \forall x, y
\end{gather*}
$$

The transition kernel for a single step in the Markov Process is defined by $p(x, y)$. The transition kernel across two time steps is computed as follows. Begin by denoting the process state at time $t$ by $X_{t}=x$, the state at $t+1$ by $X_{t+1}=y$ and the state at $t+2$ by $X_{t+2}=z$. Then the probability of transitioning to a state $X_{t+3}=z$ from $X_{t}=x$ in two steps, $p^{2}(x, z)$, is given by,

$$
\begin{aligned}
f(z \mid x) & =\int_{-\infty}^{\infty} f(z \mid x, y) f(y \mid x) d y \\
& =\int_{-\infty}^{\infty} f(z \mid y) f(y \mid x) d y \\
& =\int_{-\infty}^{\infty} p(y, z) p(x, y) d y \\
& =\int_{-\infty}^{\infty} p(x, y) p(y, z) d y
\end{aligned}
$$

where use was made of the Law of Total Probability, in the first step and second step used the Markov Chain property $f(z \mid x, y)=f(z \mid y)$. Now, the result obtained for the two step transition kernel is the continuous version of matrix multiplication of the single step
transitions probabilities. A operator inspired by matrix multiplication would be helpful. Make the definition,

$$
P^{2}(x, z)=\int_{-\infty}^{\infty} p(x, y) p(y, z) d y
$$

Using this operator, with $X_{t+3}=w$, the three step transition kernel is given by,

$$
\begin{aligned}
f(w \mid x) & =\int_{-\infty}^{\infty} f(w \mid x, z) f(z \mid x) d z \\
& =\int_{-\infty}^{\infty} f(w \mid z)\left[\int_{-\infty}^{\infty} f(z \mid y) f(y \mid x) d y\right] d z \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(w \mid z) f(z \mid y) f(y \mid x) d y d z \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(z, w) p(y, z) p(x, y) d y d z \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(x, y) p(y, z) p(z, w) d y d z \\
& =P^{3}(x, w)
\end{aligned}
$$

where the second step substitutes the two step transition kernel and the remaining steps perform the decomposition to the single step transition kernel, $p(x, y)$. Use of Mathematical Induction is used to show that the transition kernel between two states in an arbitrary number of steps, $t$, is given by,

$$
P^{t}(x, y)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} p\left(x, z_{1}\right) p\left(z_{1}, z_{2}\right) \ldots p\left(z_{t-1}, y\right) d z_{1} d z_{2} \ldots d z_{t-1}
$$

The distribution of Markov Chain states $\pi(x)$ is defined by,

$$
\begin{gathered}
\int_{-\infty}^{\infty} \pi(x) d x=1 \\
\pi(x) \geq 0 \forall x
\end{gathered}
$$

To determine the equilibrium distribution, $\pi_{E}(x)$, the time variability of $\pi_{t}(x)$ must be determined. Begin by considering an arbitrary distribution at $t=0, \pi_{0}(x)$. The distribution
after the first step will be,

$$
\pi_{1}(y)=\int_{-\infty}^{\infty} p(x, y) \pi_{0}(x) d x
$$

The distribution after two steps is,

$$
\begin{aligned}
\pi_{2}(y) & =\int_{-\infty}^{\infty} p(x, y) \pi_{1}(x) d x \\
& =\int_{-\infty}^{\infty} p(x, y)\left[\int_{-\infty}^{\infty} p(z, x) \pi_{0}(z) d z\right] d x \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(z, x) p(x, y) \pi_{0}(z) d x d z
\end{aligned}
$$

The pattern becomes more apparent after the third step,

$$
\begin{aligned}
\pi_{3}(y) & =\int_{-\infty}^{\infty} p(x, y) \pi_{2}(x) d x \\
& =\int_{-\infty}^{\infty} p(x, y)\left[\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(w, x) p(z, w) \pi_{0}(z) d z d w\right] d x \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(x, y) p(w, x) p(z, w) \pi_{0}(z) d z d w d x \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(z, w) p(w, x) p(x, y) \pi_{0}(z) d w d x d z
\end{aligned}
$$

This looks similar to the previous result obtained for the time dependence of the transition kernel. Making use of the operator $P$ gives,

$$
\begin{aligned}
& \pi_{1}(y)=P \pi_{0}(y)=\int_{-\infty}^{\infty} p(x, y) \pi_{0}(x) d x \\
& \pi_{2}(y)=P^{2} \pi_{0}(y)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(z, x) p(x, y) \pi_{0}(z) d x d z \\
& \pi_{3}(y)=P^{3} \pi_{0}(y)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} p(z, w) p(w, x) p(x, y) \pi_{0}(z) d w d x d z
\end{aligned}
$$

Mathematical Induction can be used to prove the distribution at an arbitrary time $t$ is given
by,

$$
\begin{equation*}
\pi_{t}(y)=P^{t} \pi_{0}(y) \tag{2}
\end{equation*}
$$

## Equilibrium Distribution

The equilibrium distribution is defined as the invariant solution to equation (2) for arbitrary $t_{\text {, namely, }}$

$$
\begin{equation*}
\pi_{E}(y)=P^{t} \pi_{E}(y) \tag{3}
\end{equation*}
$$

Consider,

$$
\begin{equation*}
\pi_{E}(y)=P \pi_{E}(y) \tag{4}
\end{equation*}
$$

substitution into equation (3) gives,

$$
\begin{aligned}
\pi_{E}(y) & =P^{t} \pi_{E}(y) \\
& =P^{t-1}\left(P \pi_{E}\right)(y) \\
& =P^{t-1} \pi_{E}(y) \\
& \vdots \\
& =P \pi_{E}(y) \\
& =\pi_{E}(y)
\end{aligned}
$$

Thus equation (4) defines the time invariant solution to equation (3).
To go further a particular form for the transition kernel must be specified. Unlike the discrete state model a general solution cannot be obtained since convergence of the limit $t \rightarrow \infty$ will depend on the assumed transition kernel. The following section will describe a solution to equation (4) arising from a simple stochastic processes.

## Example

To evaluate the equilibrium distribution a form for the transition kernel must be assumed. Here the AR(1) stochastic process is considered. AR(1) is a simple first order autoregressive model providing an example of a continuous state Markov Chain. In
following sections its equilibrium distribution is determined and the results of simulations are discussed.
$\mathrm{AR}(1)$ is defined by the difference equation,

$$
\begin{equation*}
X_{t}=\alpha X_{t-1}+\varepsilon_{t} \tag{5}
\end{equation*}
$$

where $t=0,1,2, \ldots$ and the $\varepsilon_{t}$ are identically distributed independent Normal random variables with zero mean and variance, $\sigma^{2}$. The $t$ subscript on $\varepsilon$ indicates that it is generated at time step $t$. The transition kernel for $\mathrm{AR}(1)$ can be derived from equation ( 5 ) by using, $\varepsilon_{t} \sim \operatorname{Normal}\left(0, \sigma^{2}\right)$ and letting $x=x_{t-1}$ and $y=x_{t}$ so that $\varepsilon_{t}=y-\alpha x$. The result is,

$$
\begin{equation*}
p(x, y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(y-\alpha x)^{2} / 2 \sigma^{2}} \tag{6}
\end{equation*}
$$

Now, consider a few steps,

$$
\begin{aligned}
& X_{1}=\alpha X_{0}+\varepsilon_{1} \\
& X_{2}=\alpha X_{1}+\varepsilon_{2} \\
& X_{3}=\alpha X_{2}+\varepsilon_{3}
\end{aligned}
$$

substituting the first equation into the second equation and that result into the third equation gives,

$$
X_{3}=\alpha^{3} X_{0}+\alpha^{2} \varepsilon_{1}+\alpha \varepsilon_{2}+\varepsilon_{3}
$$

If this process is continued for $t$ steps the following result is obtained,

$$
\begin{equation*}
X_{t}=\alpha^{t} X_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i} \tag{7}
\end{equation*}
$$

## Equilibrium Solution

In this section equation (7) is used to evaluate the the mean and variance of the $\mathrm{AR}(1)$ process in the equilibrium limit $t \rightarrow \infty$. The mean and variance obtained are then used to construct $\pi_{E}(x)$ that is shown to be a solution to equation (4).

The equilibrium mean is given by,

$$
\mu_{E}=\lim _{t \rightarrow \infty} E\left(X_{t}\right) .
$$

From equation (7) it is seen that,

$$
\begin{aligned}
E\left(X_{t}\right) & =E\left[\alpha^{t} X_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}\right] \\
& =\alpha^{t} x_{0}+\sum_{i=1}^{t} E\left(\varepsilon_{i}\right) \\
& =\alpha^{t} x_{0}
\end{aligned}
$$

where the last step follows from $E\left(\varepsilon_{i}\right)=0$. Now,

$$
\begin{aligned}
\mu_{E} & =\lim _{t \rightarrow \infty} E\left(X_{t}\right) \\
& =\lim _{t \rightarrow \infty} \alpha^{t} X_{0}
\end{aligned}
$$

this limit exists for $|\alpha| \leq 1$,

$$
\mu_{E}= \begin{cases}X_{0} & |\alpha|=1  \tag{8}\\ 0 & |\alpha| \leq 1\end{cases}
$$

The equilibrium variance is given by,

$$
\sigma_{E}^{2}=\lim _{t \rightarrow \infty} E\left(X_{t}^{2}\right)-\left[E\left(X_{t}\right)\right]^{2} .
$$

To evaluate this expression and equation for $X_{t}^{2}$ is needed. From equation (7) it follows that,

$$
\begin{aligned}
X_{t}^{2} & =\left[\alpha^{t} X_{0}+\sum_{i=1}^{t} \alpha^{t-i} \varepsilon_{i}\right]^{2} \\
& =\alpha^{2 t} X_{0}^{2}+2 \alpha^{t} X_{0} \sum_{i=1}^{t} \alpha^{t-1} \varepsilon_{i}+\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{t-i} \alpha^{t-j} \varepsilon_{i} \varepsilon_{j} .
\end{aligned}
$$

It follows that,

$$
\begin{aligned}
E\left(X_{t}^{2}\right) & =E\left[\alpha^{2 t} X_{0}^{2}+2 \alpha^{t} X_{0} \sum_{i=1}^{t} \alpha^{t-1} \varepsilon_{i}+\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{t-i} \alpha^{t-j} \varepsilon_{i} \varepsilon_{j}\right] \\
& =\alpha^{2 t} X_{0}^{2}+2 \alpha^{t} X_{0} \sum_{i=1}^{t} \alpha^{t-1} E\left(\varepsilon_{i}\right)+\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{t-i} \alpha^{t-j} E\left(\varepsilon_{i} \varepsilon_{j}\right) \\
& =\alpha^{2 t} X_{0}^{2}+\sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{t-i} \alpha^{t-j} E\left(\varepsilon_{i} \varepsilon_{j}\right)
\end{aligned}
$$

where the last step follows from $E\left(\varepsilon_{i}\right)=0$. Since the $\varepsilon_{t}$ are independent,

$$
E\left(\varepsilon_{i} \varepsilon_{j}\right)=\sigma^{2} \delta_{i j},
$$

where $\boldsymbol{\delta}_{i j}$ is the Kronecker Delta,

$$
\boldsymbol{\delta}_{i j}=\left\{\begin{array}{ll}
0 & i=j \\
1 & i=j
\end{array} .\right.
$$

Using these results gives,

$$
\begin{aligned}
E\left(X_{t}^{2}\right) & =\alpha^{2 t} X_{0}^{2}+\sigma^{2} \sum_{i=1}^{t} \sum_{j=1}^{t} \alpha^{2 t-i-j} \delta_{i j} \\
& =\alpha^{2 t} X_{0}^{2}+\sigma^{2} \sum_{i=1}^{t} \alpha^{2(t-i)} \\
& =\alpha^{2 t} X_{0}^{2}+\sigma^{2} \sum_{i=1}^{t}\left(\alpha^{2}\right)^{t-i} \\
& =\alpha^{2 t} X_{0}^{2}+\frac{\sigma^{2}\left[1-\left(\alpha^{2}\right)^{t-1}\right]}{1-\alpha^{2}},
\end{aligned}
$$

The last step follows from summation of a geometric series,

$$
\begin{aligned}
\sum_{i=1}^{t}\left(\alpha^{2}\right)^{t-1} & =\sum_{k=0}^{t-1}\left(\alpha^{2}\right)^{k} \\
& =\frac{1-\left(\alpha^{2}\right)^{t-1}}{1-\alpha^{2}}
\end{aligned}
$$

In the limit $t \rightarrow \infty E\left(X_{t}^{2}\right)$ only converges for $|\alpha|<1$. If $\alpha=1$ the denominator of the second term in of $E\left(X_{t}^{2}\right)$ is $0 E\left(X_{t}^{2}\right)$ is undefined. $\sigma_{E}^{2}$ is evaluated assuming $|\alpha|<1$ if this is the case (8) gives $\mu_{E}=0$, so,

$$
\begin{align*}
\sigma_{E}^{2} & =\lim _{t \rightarrow \infty} E\left(X_{t}^{2}\right)-\left(\mu_{E}\right)^{2} \\
& =\lim _{t \rightarrow \infty} \alpha^{2 t} X_{0}^{2}+\frac{\sigma^{2}\left[1-\left(\alpha^{2}\right)^{t-1}\right]}{1-\alpha^{2}}  \tag{9}\\
& =\frac{\sigma^{2}}{1-\alpha^{2}}
\end{align*}
$$

The equilibrium distribution, $\boldsymbol{\pi}_{E}$, is found by substituting the results from equation (8) and (9) into a $\mathbf{N o r m a l}\left(\mu_{E}, \sigma_{E}^{2}\right)$ distribution to obtain,

$$
\begin{equation*}
\pi_{E}(y)=\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-y^{2} / 2 \sigma_{E}^{2}} \tag{10}
\end{equation*}
$$

It can be shown that equation (10) is the equilibrium distribution by verifying that it is a solution to equation (4). Inserting equations (6) and (10) into equation (4) yields,

$$
\begin{aligned}
P \pi_{E}(y) & =\int_{-\infty}^{\infty} p(x, y) \pi_{E}(x) d x \\
& =\int_{-\infty}^{\infty}\left[\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{(y-\alpha x)^{2} / 2 \sigma^{2}}\right]\left[\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-y^{2} / 2 \sigma_{E}^{2}}\right] d x \\
& =\frac{1}{\sqrt{2 \pi \sigma^{2}}} \frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left[(y-\alpha x)^{2} / \sigma^{2}+x^{2} / \sigma_{E}^{2}\right]} d x \\
& =\frac{1}{\sqrt{2 \pi \sigma^{2}}} \frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2}\left[y^{2} / \sigma_{E}^{2}+(x-\alpha y)^{2} / \sigma^{2}\right]} d x \\
& =\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-y^{2} / 2 \sigma_{E}^{2}} \frac{1}{\sqrt{2 \pi \sigma^{2}}} \int_{-\infty}^{\infty} e^{-(x-\alpha y)^{2} / 2 \sigma^{2}} d x \\
& =\frac{1}{\sqrt{2 \pi \sigma_{E}^{2}}} e^{-y^{2} / 2 \sigma_{E}^{2}} \\
& =\pi_{E}(y)
\end{aligned}
$$

## Simulation

An $\mathrm{AR}(1)$ simulator can be implemented using either the difference equation definition, equation (5) or the transition kernel, equation (6). The result produced by either are statistically identical, An example implementation in Python using equation (5) is shown below.

```
def ar_1_difference_series(\alpha, \sigma, x0, nsample=100):
    samples = numpy.zeros(nsample)
    \varepsilon = numpy.random.normal(0.0, σ, nsample)
    samples[0] = x0
    for i in range(1, nsample):
        samples[i] = α * samples[i-1] + ɛ[i]
    return samples
```

The function ar_1_difference_series( $\alpha, \sigma, x 0$, nsamples) takes four arguments: $\alpha$ and $\sigma$, the initial value of $x, \mathrm{x} 0$ and the number of desired samples nsample. It begins by allocating storage for the sample output followed by generation of nsample values of $\varepsilon_{\sim} \mathbf{N o r m a l}\left(0, \sigma^{2}\right)$ with the requested standard deviation, $\sigma$. The samples are then created using the $\operatorname{AR}(1)$ difference equation, equation ( 5 ). A second implementation
using the transition kernel, equation (6) is shown below.

```
def ar1_kernel_series(\alpha, \sigma, x0, nsample=100):
    samples = numpy.zeros(nsample)
    samples[0] = x0
    for i in range(1, nsample):
        samples[i] = numpy.random.normal(\alpha * samples[i-1], \sigma)
    return samples
```

The function ar1_kernel_series( $\alpha, \sigma, \mathrm{x} 0$, nsamples $)$ also takes four arguments: $\alpha$ and $\sigma$ from equation (6), the initial value of $x_{1} \mathrm{x} 0$ and the number of desired samples, nsample. It begins by allocating storage for the sample output and then generates samples using the transition kernel with distribution $\mathbf{N o r m a l}\left(\alpha *\right.$ samples $\left.[i-1], \sigma^{2}\right)$.

The plots below show examples of time series generated using ar_1_difference_series with $\sigma=1$ and values of $\alpha$ satisfying $\alpha<1$. It is seen that for smaller $\alpha$ values of the series more frequently change direction and have smaller variance. This is expected from equation (9), where $\sigma_{E}=1 / 1-\alpha^{2}$.

AR(1) Time Series: $\sigma=1.00$
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-12.jpg?height=1164&width=1681&top_left_y=216&top_left_x=222)

If $\alpha$ is just slightly larger than 1 the time series can increase rapidly as illustrated in the plot below.
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-13.jpg?height=1071&width=1698&top_left_y=157&top_left_x=203)

For $\alpha<1 \sigma_{E}$ is bounded and the generated samples are constrained about the equilibrium mean value, $\mu_{E}=0$, but for $\alpha \geq 1 \sigma_{E}$ is unbounded and the samples very quickly develop very large deviations from $\mu_{E}$.

## Convergence to Equilibrium

For sufficiently large times samples generated by the $\mathrm{AR}(1)$ process will approach the equilibrium values for $\alpha<1$. In the plots following the cumulative values of both the mean and standard deviation computed from simulations, using ar_1_difference_series with $\sigma=1$, are compared with the equilibrium vales $\mu_{E}$ and $\sigma_{E}$ from equations (8) and (9) respectively. The first plot illustrates the convergence $\mu$ to $\mu_{E}$ for six different simulations with varying initial states, $X_{0}$, and $\alpha$. The rate of convergence is seen to decrease as $\alpha$ increases. For smaller $\alpha$ the simulation $\mu$ is close to $\mu_{E}$ within $10^{2}$ samples and indistinguishable from $\mu_{E}$ by $10^{3}$. For larger values of $\alpha$ the convergence is mush slower. After $10^{5}$ samples there are still noticeable oscillations of the sampled $\mu$ about $\mu_{E}$.
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-14.jpg?height=1080&width=1725&top_left_y=165&top_left_x=197)

Since $\sigma_{E}$ varies with $\alpha$ for clarity only simulations with varying $\alpha$ are shown. The rate of convergence $\sigma$ to $\sigma_{E}$ is slightly slower than the rate seem for $\mu$. For smaller $\alpha$ simulation $\sigma$ computations are indistinguishable form $\sigma_{E}$ by $10^{3}$ samples. For larger $\alpha$ after $10^{4}$ sample deviations about the $\sigma_{E}$ are still visible.
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-15.jpg?height=1105&width=1731&top_left_y=140&top_left_x=197)

The plot below favorably compares the histogram produced from results of a simulation of $10^{6}$ samples and the equilibrium distribution, $\pi_{E}(y)$, from equation (10).
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-16.jpg?height=1234&width=1706&top_left_y=157&top_left_x=211)

A more efficient method of estimating $\boldsymbol{\pi}_{E}(y)$ is obtained from equation (4) by noting that for sufficiently large number of samples equation (4) can be approximated by the expectation of the transition kernel, namely,

$$
\begin{align*}
\Pi_{E}(y) & =P \Pi_{E}(y) \\
& =\int_{-\infty}^{\infty} p(x, y) \Pi_{E}(x) d x  \tag{11}\\
& \approx \frac{1}{N} \sum_{i=0}^{N-1} p\left(x_{i}, y\right)
\end{align*}
$$

A Python implementation of the solution to equation (11) for the average transition kernel is listed below where two functions are defined.

```
def ar_1_kernel( } <, \sigma, x, y)
    p = numpy.zeros(len(y))
```

```
    for i in range(0, len(y)):
        \varepsilon = ((y[i] - \alpha * x)**2) / (2.0 * \sigma**2)
        p[i] = numpy.exp(-\varepsilon) / numpy.sqrt(2 * numpy.pi * \sigma**2)
    return p
def ar_1_equilibrium_distributions(\alpha, \sigma, x0, y, nsample=100):
    py = [ar_1_kernel(\alpha, \sigma, x, y) for x in ar_1_difference_series(\alpha, \sigma,
    pavg = [py[0]]
    for i in range(1, len(py)):
        pavg.append((py[i] + i * pavg[i-1]) / (i + 1))
    return pavg
```

The first function ar_1_kernel( $\alpha, \sigma, x, y$ ) computes the transition kernel for a range of values and takes four arguments as input: $\alpha$ and $\sigma$ from equation (5) and the value of x and an array of $y$ values where the transition kernel is evaluated. The second function ar_1_equilibrium_distributions( $\alpha, \sigma, \mathrm{x} 0, \mathrm{y}$, nsample) has five arguments as input:
$\alpha$ and $\sigma$, the initial value of $x, \mathrm{x} 0$, the array of y values used to evaluate the transition kernel and the number of desired samples nsample.
ar_1_equilibrium_distributions begins by calling ar_1_difference_series to generate nsample samples of x . These values and the needed inputs are then passed to ar_1_kernel providing nsample evaluations of the transition kernel. The cumulative average of the transition kernel is then evaluated and returned.

In practice this method gives reasonable results for as few as $10^{2}$ samples. This is illustrated in the following plot where the transition kernel mean value computed with just 50 samples using ar_1_equilibrium_distributions is compared $\pi_{E}(y)$ from equation (10).
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-18.jpg?height=1237&width=1712&top_left_y=157&top_left_x=208)

The following plot shows intermediate values the calculation in the range of 1 to 50 samples. This illustrates the changes in the estimated equilibrium distribution as the calculation progresses. By 500 samples a distribution near the equilibrium distribution is obtained.
![](https://cdn.mathpix.com/cropped/2025_11_22_b89c2ecf93408b87bc5eg-19.jpg?height=1083&width=1641&top_left_y=159&top_left_x=216)

## Conclusions

Markov Chain equilibrium for continuous state processes provides a general theory of the time evolution of stochastic kernels and distributions. Unlike the case for the discrete state model general solutions cannot be obtained since evaluation of the obtained equations depends of the form of the stochastic kernel. Kernels will exist which do not have equilibrium solutions. A continuous state process that has an equilibrium distribution that can be analytically evaluated is $\mathrm{AR}(1)$. The stochastic kernel for $\mathrm{AR}(1)$ is derived from its difference equation representation and the first and second moments are evaluated in the equilibrium limit, $t \rightarrow \infty$. It is shown that finite values exists only for values of the $\operatorname{AR}(1)$ parameter that satisfy $|\boldsymbol{\alpha}|<1$. A distribution is then constructed using these moments and shown to be the equilibrium distribution. Simulations are performed using the difference equation representation of the process and compared with the equilibrium calculations. The rate of convergence of simulations to the equilibrium is shown to depend on $\alpha$. For values not near 1 convergence of the mean occurs with $O\left(10^{3}\right)$ time steps and convergence of the standard deviation with $O\left(10^{4}\right)$ time steps. For values of $\alpha$ closer to 1 convergence has not occurred by $10^{4}$ time steps.

