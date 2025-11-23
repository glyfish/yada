Hamiltonan Monte Carlo
$\qquad$
Troy Stribling
March 23 2019

## Properties of Hamiltonian Dynamics

## Hamilton's Equations

Hamiltonian Monte Carlo is a Markov Chain Monte Carlo simulation method constructed from Hamiltonian mechanics. Consider a collection of particles descibed by $2 n$ phase space coordinates

$$
\begin{aligned}
& q=\left(q_{1}, q_{2}, \ldots, q_{n}\right)^{\top} \\
& p=\left(p_{1}, p_{2}, \ldots, p_{n}\right)^{\top}
\end{aligned}
$$

where $q$ and $p$ are column vectors. Hamilton's Canonical equation's of motion are given by

$$
\begin{gathered}
\frac{d p_{i}}{d t}=-\frac{\partial H(p, q)}{\partial q_{i}} \quad \frac{d q_{i}}{d t}=\frac{\partial H(p, q)}{\partial p_{i}} \\
\frac{d H}{d t}=\frac{\partial H}{\partial t}
\end{gathered}
$$

where the Hamiltonian, $H(p, q)$, is given by

$$
H(p, q)=k(p)+u(q)
$$

## Kinetic Energy

The Kinetic Energy in a cartesian coordinate system is given by

$$
K(p)=\sum_{i=1}^{n} \frac{p_{i}^{2}}{2 m_{i}}
$$

and $u(q)$ is a polential energy function. $K(p)$ is usually written as

$$
K(p)=\frac{1}{2} p^{\top} M^{-1} p
$$

where

$$
\begin{array}{r}
M=\left[\begin{array}{ccc}
m_{1} & m_{2} & 0 \\
0 & \ddots & \\
& & m_{n}
\end{array}\right] \\
\Rightarrow M^{-1}=\left[\begin{array}{ccc}
1 / m_{1} & & 0 \\
& 1 / m_{2} & \\
0 & & 1 / m_{n}
\end{array}\right]
\end{array}
$$

so that

$$
M M^{-1}=I=\left[\begin{array}{lll}
1 & & 0 \\
& 1 & \\
& 0 & \ddots \\
& & 1
\end{array}\right]
$$

$M$ is called the mass matrix. In general $M$ need not be diagonal. (This will be later investigated furthur)

Using the Hamiltonian

$$
H(p, q)=p^{\top} M^{-1} p+u(q)
$$

Hamilton's Canonical equations become

$$
\begin{aligned}
& \frac{d p_{i}}{d t}=-\frac{\partial H(p, q)}{\partial q_{i}}=-\frac{\partial u}{\partial q_{i}} \\
& \frac{d q_{i}}{d t}=\frac{\partial H(p, q)}{\partial p_{i}}=\left(M^{-1} p\right)_{i}
\end{aligned}
$$

Interesting properties of the Hamiltonan include the following.

## Conservation Laws

Recall that

$$
\frac{d H}{d t}(P, q)=\frac{\partial H}{\partial t}(P, q)
$$

thus if $H(p, q)$ has no explict time variabity with all changes in time resulting from changes in the coordinates it follows that

$$
\frac{d H}{d t}(p, q)=0
$$

thus $H(p, q)$ is conserved. Furthur if phase volume elements are denoted by

$$
\begin{aligned}
& d q=d q_{1} d q_{2} \cdots d q_{n} \\
& d p=d p_{1} d p_{2} \cdots d p_{n}
\end{aligned}
$$

so that a volume element is denoted by

$$
d q d p
$$

Consider a Canonical transformation that transforms $P$ and $q$ to new coordinates $P$ and $Q$,

$$
P=P(p, q) \quad Q=Q(p, q)
$$

It can be shown that volume elements are conserved, namely,

$$
d q d p=d Q d P
$$

Finally if a phase space density function is defined by the thermodynamic of the volume density of states

$$
\rho(p, q)=\frac{d N}{d V}
$$

where $N$ is the number states and $V$ is a phase space volume element

$$
d v=d p d q
$$

If the flux of phase space density is defined by

$$
\bar{J}=\rho(p, q)\left(\dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n}, \dot{p}_{1}, \dot{p}_{2}, \ldots, p_{n}\right)
$$

The conservation of phase space volume implies conservation the rate of change of densitiy in the volume and is discribed by the divergence theorem

$$
\frac{\partial \rho}{\partial t}+\nabla \cdot \bar{J}=0
$$

where the rate of change of phase space density in the volume is given by the

$$
\frac{\partial \rho}{\partial t}
$$

term and the flux through te volume surface by the

$$
\nabla \cdot \overline{\mathrm{J}}
$$

term. Consider the $\bar{v} \cdot \bar{J}$ term

$$
\begin{aligned}
\nabla \cdot \bar{J} & =\sum_{i=1}^{n}\left\{\frac{\partial}{\partial q_{i}}\left(\rho \dot{q}_{i}\right)+\frac{\partial}{\partial p_{i}}\left(\rho \dot{p}_{i}\right)\right\} \\
& =\rho \sum_{i=1}^{n}\left\{\frac{\partial \dot{q}_{i}}{\partial q_{i}}+\frac{\partial \dot{p}_{i}}{\partial p_{i}}\right\}
\end{aligned}
$$

Consider the i'th term

$$
\begin{aligned}
& \frac{\partial \dot{q}_{i}}{\partial q_{i}}=\frac{\partial}{\partial q_{i}}\left(\frac{\partial H}{\partial p_{i}}\right)=\frac{\partial^{2} H}{\partial q_{i} \partial p_{i}} \\
& \frac{\partial \dot{p}_{i}}{\partial p_{i}}=\frac{\partial}{\partial p_{i}}\left(-\frac{\partial H}{\partial q_{i}}\right)=-\frac{\partial^{2} H}{\partial p_{i} \partial q_{i}}
\end{aligned}
$$

which follows from Hamiton's equation. Thus

$$
\nabla \cdot \bar{J}=\sum_{i=1}^{n}\left\{\frac{\partial^{2} H}{\partial q_{i} \partial p_{i}}-\frac{\partial^{2} H}{\partial p_{i} \partial q_{i}}\right\}=0
$$

thus

$$
\frac{\partial e}{\partial t}=0
$$

so phase space volume is conseved.
Time Reversal Symmetry
Hamiltonian dynamics is time reversible that is the transformation

$$
t \rightarrow-t
$$

reverses the equations of motion,

$$
\frac{d p_{i}}{d t}=\frac{\partial H(p, q)}{\partial q_{i}} \quad \frac{d q_{i}}{d t}=-\frac{\partial H(p, q)}{\partial p_{i}}
$$

which represent a time reverseal of the dynamics. This transformation does not leave the equations of motion invariant but negates them. A transformation that leaves the equations of motion invariant is to reverse both $t$ and $P$,

$$
t \rightarrow-t \quad p_{i} \rightarrow-p_{i}
$$

giving

$$
\frac{d\left(-p_{i}\right)}{d(-t)}=\frac{d p_{i}}{d t}=-\frac{\partial H}{\partial q_{i}}(p, q)
$$

and

$$
\begin{aligned}
& \left.\frac{d q_{i}}{d(-t)}=\frac{\partial H}{\partial\left(p_{i}\right.}\right) \\
\Rightarrow & \frac{d q_{i}}{d t}=-\frac{\partial H}{\partial p_{i}}(p, q) \\
\Rightarrow & \frac{d q_{i}}{d t}=\frac{\partial H(p, q)}{\partial p_{i}}
\end{aligned}
$$

## Probability Distributions and Hamiltonian Dynamics

Recall that the Hamiltonian is given by

$$
H(p, q)=k(p)+u(q)
$$

If a canonical ensemble is assumed then the probability distribution in phase space is given by

$$
\rho(p, q)=\frac{1}{2} e^{-H(p, q) / T}
$$

where $T$ is the temperature and $z$ the partition function. It follows that

$$
e(p, q)=\frac{1}{2} e^{-k(p) / T} e^{-u(q) / T}
$$

When simulating Bayesian statics the intrest is in computing the posterior distribution p(910) which is defined by Bayes theorem

$$
p(q \mid D)=\frac{p(q) p(D \mid q)}{p(D)}
$$

where the random variable $D$ represents observed data. $p(q)$ is called the prior and p(D/q) is the liklinood. Usualy the normalization $P(D)$ is ignored and the problem solved is

$$
p(q \mid D) \propto p(q) p(D \mid q)
$$

For Hamiltonian Monte Carlo simulations it is assumed that the potential energy function $u(q)$ is related to the posterior distribution $p(q \mid D)$ by

$$
u(q)=-\ln p(q \mid D)
$$

Here $p(q)$ will be used to denote p(q1D). Now using the defintion conditional probability

$$
p(p, q)=p(p \mid q) p(q)
$$

and

$$
p(p, q) \propto e^{-H(p, q)}
$$

where it is assumed that $T=1$. It follows that

$$
\begin{aligned}
H(p, q) & =-\ln p(p, q) \\
& =-\ln p(p \mid q)-\ln p(q)
\end{aligned}
$$

using

$$
H(p, q)=K(p)+u(q)
$$

gives

$$
\begin{aligned}
& K(p)=-\ln p(p \mid q) \\
& u(q)=-\ln p(q)
\end{aligned}
$$

This gives the interpretation

$$
\begin{aligned}
& p(p \mid q) \propto e^{-k(p)} \\
& p(q) \propto e^{-u(q)}
\end{aligned}
$$

## Discription of Algorithm

## Momentum updates

The Hamiltonian Monte Carlo, HMC, algorithm consists of two steps. The first generates new momentum values by sampling $P$ using

$$
p(p \mid q) \propto e^{-k(p)}
$$

independent of the value of $q$. If a diagonal mass matrix is assumed where

$$
M=\left[\begin{array}{ccc}
m_{1} & & \\
& m_{2} & 0 \\
0 & & m_{n}
\end{array}\right]
$$

the $p_{i}$ are independent Normal distributions with mean zero and variance, $m_{i}$.
Note that since $p(p \mid q)$ does not depend on $q$ the conditional distribution is equal to the
marginal distribution for $P$,

$$
p(p)=p(p \mid q)
$$

## Generation of Proposal Samples

The Metropolis Hastings algorithm is used to generate samples which requires a proposal. In previous discussions of Metropolis Hastings proposal samples are generated using a proposal distribution different from the target distribution. In Hamiltonian Monte Carlo the proposal sample is gereated using Hamiltonian Mechanics. An itegration of the Hamiltonian equations of motion for $M$ steps with a time step $\varepsilon$ is performed. The intial momentum, $p$, used is the value generated at the previous step using the Kinetic energy and the coordinate used is the previous accepted sample.

The momentum and coordinate obtained at the end of the integration, $\left(p_{H}, q_{H}\right)$, is then converted to the sample proposa), $\left(p^{*}, q^{*}\right)$ by negating the momentum

$$
\left(p^{*}, q^{*}\right)=\left(-p_{H}, q_{H}\right) .
$$

The Metropolis Hastings acceptance function is computed using the current and proposal momentum and coordinate,

$$
\begin{aligned}
& \alpha\left(p^{*}, q^{*}, p, q\right) \\
& =\min \left[1, \exp \left(-H\left(-p^{*}, q^{*}\right)+H(p, q)\right)\right] \\
& =\min \left[1, \exp \left(u(q)-u\left(q^{*}\right)+K(p)-K\left(-p^{*}\right)\right)\right]
\end{aligned}
$$

Phase Space Traversal
A possible trajectory in phase space created as samples are generated is shown in the following
diagram diagram
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-016.jpg?height=879&width=1049&top_left_y=28&top_left_x=330)

The step begins with the result of the previous step indicated by state 0 in the diagram. State 0 is located on a surface of constant Hamiltonian defined by $H(p, q)=H_{0}$. The transition from state 0 to state 1 is a result of drawing a new momentum value from the Kinetic energy distribution. The state in phase space has transitioned to a new state in phase space on a different surface of
constant thamiltonian defined by $H(p, q)=H_{1}$. The next step in the algorithm is the transition from state 1 to 2 along the constant Hamiltonian surface $H(p, q)=H_{1}$. This is accomplished by integrating Hamilton's equations for $N$ steps with stepsize $\varepsilon$. The final step in the algorithm performs the transformation $(q, p) \rightarrow(q,-p)$. since the kinetic energy is quadratic in $P$ the Hamiltonian is conserved so the system remains on the surface defined by $H(p, q)=H_{1}$. The end result is state 3 indicated in the figure. state 3 is the proposal sample $\left(p^{*}, q^{*}\right)$ wich is accepted if

$$
\alpha\left(p^{*}, q^{*}, p, q\right) \leqslant 1
$$

## Detailed Balance

Detailed balance is a symmetry resulting from invariance under time reversal of a stochastic kernel. It is defined by

$$
\pi(x) S(x, y)=\pi(y) S(y, x)
$$

where $s(x, y)$ is the stochastic kernel representing transitions of a continuous state Markov chain and $\pi(x)$ is the equilibrium distribution of states. Detailed balance is required for Metropolise Hastings sampling to produce an equilibrium distribution equal to the target distribution, $f(x)$. Detailed balance is enforced through the sample acceptance function

$$
\alpha(x, y)=\min \left[1, \frac{f(y) s(y, x)}{f(x) s(x, y)}\right]
$$

Recall that the stochastic kemel $s(y, x)$ is a conditional distribution

$$
s(x, y)=p(y \mid x)
$$

so

$$
\alpha(x, y)=\min \left[1, \frac{f(y) p(x \mid y)}{f(x) p(y \mid x)}\right]
$$

## Metropolis Hastings Acceptance Function

The acceptance probability for the Metropolis Hastings step is given by

$$
\begin{aligned}
& \alpha\left(p^{*}, q^{*}, p, q\right)= \\
& \quad \min \left[1, \frac{f\left(p^{*}, q^{*}\right) p\left(p, q \mid p^{*}, q^{*}\right)}{f(p, q) p\left(p^{*}, q^{*} \mid p, q\right)}\right]
\end{aligned}
$$

the target distribution, $f(p,q)$ is given by the canonical distribution

$$
f(p, q) \propto e^{-H(p, q)}
$$

and

$$
f\left(p^{*}, q^{*}\right) \propto e^{-H\left(p^{*}, q^{*}\right)}
$$

The step begins by selecting $P$. The sample proposal is then deterministically determined by integrating Hamilton's equations for $M$ steps with stepsize $\varepsilon$ starting at intitial state $(P, G)$ to obtain $\left(p^{*}, q^{*}\right)$ thus

$$
p\left(p^{*}, q^{*} \mid p, q\right)=1
$$

To otain an expression for $p\left(p, q \mid p^{*}, q^{*}\right)$ it would be necessary to integrate Hamilton's equations backward in time startins at $\left(p^{*}, q^{*}\right)$ and ending at $(p, q)$ after $M$ steps. This not possible since Hamilton's equations are not time reversible. The result of the integration would be (-P, 9 ) not $(p, q)$. Previously it was shown that for the transformation

$$
\left(p^{*}, q^{*}\right) \rightarrow\left(-p^{*}, q^{*}\right)
$$

that a backwards in time integration will produce ( $p, q$ ). If the first step of the algorithm adds the trasformation $\left(p^{*}, q^{*}\right) \rightarrow \left(-p^{*}, q^{*}\right)$ then the intral state can be obtained deterministically from the proposed state.

$$
p\left(-p^{*}, q^{*} \mid p, q\right)=p\left(p, q \mid-p^{*}, q^{*}\right)=1
$$

thus

$$
\begin{aligned}
\alpha\left(p^{*}, q^{*}, p, q\right)=&\min \left[1, \frac{f\left(-p^{*}, q^{*}\right)}{f(p, q)}\right] \\
=&\min \left[1, \frac{e^{-H\left(-p^{*}, q^{*}\right)}}{e^{-H(p, q)}}\right] \\
=&\min \left[1, e^{H(p, q)-H\left(-p^{*}, q^{*}\right)}\right]
\end{aligned}
$$

## Integration of Hamilton's Equations

A crucial step in the generation of samples usins Hamiltonian Monte Carlo is integration of Hamilton's equation to obtain a proposal state $\left(p^{*}, q^{*}\right)$. The simpelest method is Euler's Method. An enhancement to Euler's Method called the Modified Euler Method is also discussed. Finally, integration method's called Symlectic Integrators are discussed. Results obtained by solving a sample problem using each of methods are compared.
Recall that Hamilton's equations are given by

$$
\begin{aligned}
& \frac{d p_{i}}{d t}=-\frac{\partial H}{\partial q_{i}}=-\frac{\partial u}{\partial q_{i}} \\
& \frac{d q_{i}}{d t}=\frac{\partial H}{\partial p_{i}}=\frac{\partial K}{\partial p_{i}}=\frac{p_{i}}{m_{i}}
\end{aligned}
$$

where the mass matrix has been assumed to be diagonal

$$
(M)_{i i}=m_{i}
$$

In the following discussion the total integration trme is defined by

$$
t_{N}=\varepsilon N
$$

where $\varepsilon$ is the stepsize and $N$ is the number of steps and it is assumed that

$$
t_{N} \gg \varepsilon
$$

## Euler's Method

Euler's Method is obtained by expanding Hamilton's Equations in a Taytor series in powers of the stepsize, $\varepsilon$, to first order.

$$
\begin{aligned}
P_{i}(t+\varepsilon) & =P_{i}(t)+\frac{d p_{i}}{d t} \varepsilon \\
& =P_{i}(t)-\frac{\partial u}{\partial q_{i}} \varepsilon
\end{aligned}
$$

and

$$
\begin{aligned}
q_{i}(t+\varepsilon) & =q_{i}(t)+\varepsilon \frac{d q_{i}}{d t} \\
& =q_{i}(t)+\varepsilon \frac{p_{i}}{m}(t)
\end{aligned}
$$

Thus Euler's Method is defined by the system of equations

$$
\begin{aligned}
& p_{i}(t+\varepsilon)=p_{i}(t)-\frac{\partial u}{\partial q_{i}} \varepsilon \\
& q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}(t)
\end{aligned}
$$

It will be shown that Euler's Method produces solutions with errors $o\left(\varepsilon^{2}\right)$ and that the method does not conserve phase space volume

## Euler-Cromer Method

The Euler-Cromer method is a modification of the Euler method where the $q_{i}(t+\varepsilon)$ update uses $p_{i}(t+\varepsilon)$ instead of the value at the previous slep $p_{i}(t)$

$$
\begin{aligned}
& p_{i}(t+\varepsilon)=p_{i}(t)-\varepsilon \frac{\partial u}{\partial q_{i}} \\
& q_{i}(t+\varepsilon)=q_{i}(t)+\frac{\varepsilon p_{i}(t-1 \varepsilon)}{m_{i}}
\end{aligned}
$$

This method has accuracy $O\left(\varepsilon^{2}\right)$ like the Euler method but unlike the Euler method the Euler-cromer method conserves phase space volume. This lecds to an improvement in performance over the Euler method.

## Leapfrog Method

The leapfros method is similar to the Euler-Gromer method in that it that the $q_{i}(t+\varepsilon)$ update does not use the privious value of $p_{i}(t)$, like the Euler method, but instead of using $p_{i}(t+\varepsilon)$ leapfrog uses $p_{i}\left(t+\frac{1}{2} \varepsilon\right)$. That is leapfrog evalutes $P_{i}(t)$ on intervals shifted by $\frac{1}{2} \varepsilon$. The update scheme is depicted below
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-026.jpg?height=265&width=1085&top_left_y=1132&top_left_x=195)

The resulting algorithm is given by

$$
P_{i}\left(t+\frac{3}{2} \varepsilon\right)=P_{i}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}
$$

$$
q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}\left(t+\frac{1}{2} \varepsilon\right)
$$

Intralization of this method is not clear since the momentum at $\frac{1}{\partial \varepsilon}$ is required and the algonithm produces $q_{i}$ and $p_{i}$ that differ in time by $\frac{1}{2} \varepsilon$ so how are calculations performed that require values at the same time. These problems are addressed by the Momentum verlet Method.

## Momentum Verlet

To start integration using the leapfrog method the first half step of the momentum $P_{i}\left(\frac{1}{2} \varepsilon\right)$ needs to be computed with knowledge only of $p_{0}$ and 90 . The simplest thing to do is to start with a half step calculation using the Euler method

$$
P_{i}(\partial \varepsilon)=P_{i}(0)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{0}
$$

subsequent steps are then computed using the following algorithm

1) $P_{i}\left(t+\frac{1}{2} \varepsilon\right)=P_{i}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t}$
2) $q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}\left(t+\frac{1}{2} \varepsilon\right)$
3) $p_{i}(t+\varepsilon)=p_{i}\left(t+\frac{1}{\partial} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}$

The Momentum Verlet algonthm differs from the variants of the Euler method. Instead of using differences where the integrated functions are exaluated at the begining and end of the time interval, as in the Euler methods, the Momentum verlet method evaluates the momentum differences at half interval steps using the position coaluated at the begining and end of the time interval and the position differences are evaluated at full trone interval steps using the half interval momentum.
This results in an accuracy $O\left(\varepsilon^{3}\right)$ for the integration of both momentum and position.

## Solution Accuracy

This section will estimate the error of the dissused numerical indegration methods. The algorithms fall into two catogories based on how derivatives are calculated. They are the Forward Difference Derivative and the Central Difference Derivative. Both approaches produce algorithms of equal computational complexity but to lowest order the Basic Forward Difference Method has errors $O\left(\varepsilon^{2}\right)$ while the Central Difference Method has errors $O\left(\varepsilon^{3}\right)$, where $\varepsilon$ is the step size. Both Euler and Euler-Cromer methods
are in the Forward Difference category and Leap Frog and Momentum verlet are Central Difference methods

## Forward Difference Derivative

The Forward Difference Devivative method is the most basic method of numerically evaluating the derivative of a function
Consider a function $f(t)$. The dirivative of $f(t)$ is defined by

$$
\frac{d f(t)}{d t}=\lim _{\varepsilon \rightarrow 0} \frac{f(t+\varepsilon)-f(t)}{\varepsilon}
$$

The Taylor series expansion of $f(t)$ about $t$ is given by

$$
f(t+\varepsilon)=\sum_{i=0}^{\infty} \frac{\varepsilon^{n}}{n!} f^{n}(t)
$$

where $f^{n}(t)$ is the n'th derivate of $f(t)$ with respect to $t$. It follows that

$$
\frac{f(t+\varepsilon)-f(t)}{\varepsilon}=f^{\prime}(t)+\sum_{i=2}^{\infty} \frac{\varepsilon^{n}}{n!} f^{n}(t)
$$

Let

$$
\Delta(\varepsilon, t)=\sum_{i=2}^{\infty} \frac{\varepsilon^{n}}{n!} f^{n}(t)
$$

then

$$
f^{\prime}(t)=\frac{f(t+\varepsilon)-f(t)}{\varepsilon}-\Delta(\varepsilon, t)
$$

The forward difference approximation to $f^{\prime}(t)$ is defined by

$$
f_{f d}^{\prime}(t)=\frac{f(t+\varepsilon)-f(t)}{\varepsilon}
$$

then

$$
f^{\prime}(t)-f_{f d}^{\prime}(t)=\Delta(\varepsilon, t)
$$

If it is assumed that $t \gg \varepsilon$ then to lowest order

$$
f^{\prime}(t)-f_{f d}^{\prime}(t) \approx \frac{\varepsilon^{2}}{2} f^{\prime \prime}(t)
$$

It follows that the accuracy of the forward difference appoximation
is $o\left(\varepsilon^{2}\right)$. Using the forward difference approximation it follows that to lowest order in $\varepsilon$

$$
\begin{aligned}
f^{\prime}(t) & \approx f_{f_{d}}^{\prime}(t) \\
& =\frac{f(t+\varepsilon)-f(t)}{\varepsilon} \\
\Rightarrow \quad f(t+\varepsilon) & \approx f(t)+\varepsilon f^{\prime}(t)
\end{aligned}
$$

which is the Euler method of integration. It follows that for a given stepsize that Euler Method has accuracy $O\left(\varepsilon^{2}\right)$.

## Central Difference Derivative

In Forward Difference Derivative the difference used to calculate the derivate of a function at time $t$ is consturcted from an evatuation of the function a time $t$ and $t+\varepsilon$, namely,

$$
\Delta f(t)=f(t+\varepsilon)-f(t)
$$

In the Central Difference Denivative the difference is constructed from evaluations of the function centered at $t$, namely,

$$
\Delta f(t)=f\left(t+\frac{1}{2} \varepsilon\right)-f\left(t-\frac{1}{2} \varepsilon\right)
$$

Now

$$
\begin{aligned}
& f\left(t+\frac{1}{2} \varepsilon\right)=\sum_{i=0}^{\infty} \frac{\left(\frac{1}{2} \varepsilon\right)^{n} f^{n}(t)}{n!} \\
& f\left(t-\frac{1}{2} \varepsilon\right)=\sum_{i=0}^{\infty} \frac{\left(-\frac{1}{2} \varepsilon^{n}\right)}{n!} f^{n}(t)
\end{aligned}
$$

it follows that the difference is
given by

$$
\begin{aligned}
& f\left(t+\frac{1}{2} \varepsilon\right)-f\left(t-\frac{1}{2} \varepsilon\right)=\left\{f(t)+\frac{1}{2} \varepsilon f^{\prime}(t)\right. \\
& \left.+\left(\frac{1}{2} \varepsilon\right)^{2} f^{\prime \prime}(t)+\left(\frac{1}{2} \varepsilon\right)^{3} f^{\prime \prime \prime}(t)+\cdots\right\} \\
& -\left\{\begin{array}{l}
f(t)-\frac{1}{2!} \varepsilon f^{\prime}(t)+\frac{\left(\frac{1}{2} \varepsilon\right)^{2}}{2!} f^{\prime \prime}(t) \\
\left.-\left(\frac{1}{2} \varepsilon\right)^{3} f^{\prime \prime \prime}(t)+\cdots\right\}
\end{array}\right. \\
& =\varepsilon f^{\prime}(t)+2\left(\frac{\frac{1}{2} \varepsilon}{3!}\right)^{3} f^{\prime \prime \prime}(t)+\cdots
\end{aligned}
$$

The even power terms cancel. It follows that the Centered difference approximation of the derivative is defined by

$$
f_{C D}^{\prime}(t)=\frac{f\left(t+\frac{1}{\partial} \varepsilon\right)-f\left(t-\frac{1}{\partial} \varepsilon\right)}{\varepsilon}
$$

The difference between the denvative
of $f(t)$ and the Centered Difference appoximation is given by

$$
f_{C D}^{\prime}(t)=f^{\prime}(t)+\frac{1}{(4)(3!)} \varepsilon^{2} f^{\prime \prime \prime}(t)+\cdots
$$

To lowest order the approximation error is given by

$$
f_{C D}^{\prime}(t)-f^{\prime}(t) \approx \sigma\left(\varepsilon^{2}\right)
$$

which is an order of magnitude better than the forward difference approximation obtained with no extra computational cost.
It follows that the Central Difference approximation to the derivative is given by

$$
\begin{aligned}
f^{\prime}(t)&=f_{C D}^{\prime}(t)=\frac{f\left(t+\frac{1}{2} \varepsilon\right)-f\left(t-\frac{1}{2} \varepsilon\right)}{\varepsilon} \\
&\Rightarrow f\left(t+\frac{1}{2} \varepsilon\right)=f\left(t-\frac{1}{2} \varepsilon\right)+\varepsilon f^{\prime}(t)
\end{aligned}
$$

Now consider the transformation

$$
t \rightarrow t+\frac{1}{2} \varepsilon
$$

then the Central Difference approximation becomes

$$
f(t+\varepsilon)=f(t)+\varepsilon f^{\prime}\left(t+\frac{1}{2} \varepsilon\right)
$$

Recall that the Momentum lerlet method for Hamiltoris equation

1) $P_{i}\left(t+\frac{1}{2} \varepsilon\right)=P_{i}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t}$
2) $q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon p_{i}\left(t+\frac{1}{2} \varepsilon\right)$
3) $P_{i}(t+\varepsilon)=P_{i}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}$

Clearly step 2 which evaluates position updates is using the Central Difference approximation to the derivative. The momentum update is split over steps 1 and 2
so that the half-step derivative is available for the position update in step 2. Combining steps 1 and 2 give
$p_{i}(t+\varepsilon)=p_{i}(t)-\frac{1}{2} \varepsilon\left[\left.\frac{\partial u}{\partial q_{i}}\right|_{t}+\left.\frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}\right]$
but
$\left.\frac{\partial u}{\partial q_{i}}\right|_{t}+\left.\frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}=\left.2 \frac{\partial u}{\partial q_{i}}\right|_{t+\frac{1}{\partial} \varepsilon}$
Thus

$$
p_{i}(t+\varepsilon)=p_{i}(t)-\left.\varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t+\frac{1}{\partial} \varepsilon}
$$

which is the result obtained using the Central Difference derivative approximation. Thus the Momentum Verlet has approximation error $O\left(\varepsilon^{3}\right)$.

## Conservation of Phase Space Volume

The conservation of phase space volume by Hamitton's Equations when the Hamiltonian time dependence is not expliat but depends only on the coordinates is a consequence of Liouville's Theorem. Both Euler-Cromer Integration and Momentum verlet Integration can be shown to exactly conserve phase space volume. Integration methods that conserve phase space volume are called symplectic Integrators. Both Euler-Cromer Integration and Momentum verlet Integration have superior performance because they are symplectic Integrators.
Consider a one-dimensional Hamiltonian that has a single momentum and position coordinate.

The evolution in time of a differential area element is shown in the following dragram.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-040.jpg?height=523&width=1148&top_left_y=392&top_left_x=181)

The left diagram shows a differential phase space area element at time $t$ and the right diagram the change in the differential area element due the the change in the phase space coordinates. At time $t$

$$
d A=d p d q
$$

at time $t^{\prime}$

$$
d A^{\prime}=|d \bar{a} \times d \bar{b}|
$$

Now solutions to Hamilton's equations can by writen as canonical transformations thus the phase space coordinates at time ' $t$ ' can be written as functions of the coordinates at time $t$,

$$
\begin{aligned}
& x^{\prime}=x^{\prime}(x, p) \\
& p^{\prime}=p^{\prime}(x, p)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
d \bar{a} & =\frac{\partial x^{\prime}}{\partial x} d x \hat{x}+\frac{\partial p^{\prime}}{\partial x} d x \hat{p} \\
& =\left(\frac{\partial x^{\prime}}{\partial x} \hat{x}+\frac{\partial p^{\prime}}{\partial x} \hat{p}\right) d x \\
d \bar{b} & =\frac{\partial x^{\prime}}{\partial p} d p \hat{x}+\frac{\partial p^{\prime}}{\partial p} d p \hat{p} \\
& =\left(\frac{\partial x^{\prime}}{\partial p} \hat{x}+\frac{\partial p^{\prime}}{\partial p} \hat{p}\right) d p
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& d A^{\prime}=|d \bar{a} \times d \bar{b}| \\
& =\left|\begin{array}{ll}
\frac{\partial x^{\prime}}{\partial x} d x & \frac{\partial p^{\prime}}{\partial x} d x \\
\frac{\partial x^{\prime}}{\partial p} d p & \frac{\partial p^{\prime}}{\partial p} d p
\end{array}\right| \\
& =\frac{\partial x^{\prime}}{\partial x} \frac{\partial p^{\prime}}{\partial p} d x d p-\frac{\partial p^{\prime}}{\partial x} \frac{\partial x^{\prime}}{\partial p} d x d p \\
& =\left(\frac{\partial x^{\prime}}{\partial x} \frac{\partial p^{\prime}}{\partial p}-\frac{\partial p^{\prime}}{\partial x} \frac{\partial x^{\prime}}{\partial p}\right) d x d p .
\end{aligned}
$$

Let

$$
J=\left(\begin{array}{ll}
\frac{\partial x^{\prime}}{\partial x} & \frac{\partial p^{\prime}}{\partial x} \\
\frac{\partial x^{\prime}}{\partial p} & \frac{\partial p^{\prime}}{\partial p}
\end{array}\right)
$$

then

$$
|J|=\left(\frac{\partial x^{\prime}}{\partial x} \frac{\partial p^{\prime}}{\partial p}-\frac{\partial p^{\prime}}{\partial x} \frac{\partial x^{\prime}}{\partial p}\right)
$$

and

$$
d A^{\prime}=J d x d p
$$

It follows that to conserve phase space volume

$$
\begin{aligned}
& d A=d A^{\prime} \\
\Rightarrow \quad & d x d y=|J| d x d y \\
\Rightarrow \quad & |J|=1
\end{aligned}
$$

This result is true for any number of dimensions. $J$ is called the Jacobian matrix.
Now to prove that Euler-Cromer and Momentum verlet integration conserve phase space volume it must be shown that the al gorithms produce changes in in the phase space coordinates such that $|S|=1$. To go furthur J1 must be determined for each algorithm.

## Momentum Verlet

The steps for Momentum Verlet are given by

1) $P_{i}\left(t+\frac{1}{2} \varepsilon\right)=P_{i}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t}$
2) $q_{i}(t+\varepsilon)=q_{i}(t)+\frac{\varepsilon p_{i}}{m_{i}}\left(t+\frac{1}{2} \varepsilon\right)$
3) $P_{i}(t+\varepsilon)=P_{i}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}$

since only a one-dimensional system is considered the notation can be simplified,

1) $P_{1 / 2}=P_{0}+\frac{1}{2} \varepsilon F\left(q_{0}\right)$
2) $q_{1}=q_{0}+\varepsilon p_{12}$
3) $p_{1}=p_{1 / 2}+\frac{1}{2} \varepsilon F\left(q_{1}\right)$

where

$$
F\left(q_{k}\right)=-\left.\frac{\partial u}{\partial q}\right|_{k} \quad m_{i}=1
$$

and the swascript denotes the step in a single teration of the algorithm.
Each step represents a seperate transformation that are sequentially applied.
For the first stop,

1) $P_{1 / 2}=P_{0}+\frac{1}{2} \varepsilon F\left(q_{0}\right)$

Consider an infinitesimal change in each coordinate

$$
p_{1 / 2}+\delta p_{1 / 2}=p_{0}+\delta p_{0}+\frac{1}{2} \varepsilon F\left(q_{0}+\delta q_{0}\right)
$$

but

$$
F\left(q_{0}+\delta q_{0}\right)=F\left(q_{0}\right)+F^{\prime}\left(q_{0}\right) \delta q_{0}
$$

so,

$$
p / 12+\delta p / 22=p_{0}+\delta p_{0}+\frac{1}{2} \varepsilon\left\{F\left(q_{0}\right)+F^{\prime}\left(q_{0}\right) \delta q_{0}\right\}
$$

the change produced by the step is found by subracting this from equation (1), namely)

$$
\delta p_{1_{2}}=\delta p_{0}+\frac{1}{2} \varepsilon F^{\prime}\left(q_{0}\right) \delta q_{0}
$$

this transformation can be writen in matrix form using

$$
T_{1}=\left(\begin{array}{cc}
1 & 0 \\
\frac{1}{\partial \varepsilon} F^{\prime}\left(q_{0}\right) & 1
\end{array}\right)
$$

so,

$$
\left(\begin{array}{cc}
1 & 0 \\
\frac{1}{\partial} \varepsilon F^{\prime}\left(q_{0}\right) & 1
\end{array}\right)\binom{\delta q_{0}}{\delta p_{0}}=\binom{\delta q_{0}}{\delta p_{0}+\frac{1}{\partial} \varepsilon F^{\prime}\left(q_{0}\right) \delta q_{0}}
$$

thus

$$
\binom{\delta q_{0}}{\delta p_{1 / 2}}=T_{1}\binom{\delta q_{0}}{\delta p_{0}}
$$

For the second step,

$$
\text { 2) } q_{1}=q_{0}+\varepsilon p_{12}
$$

An infinitesimal change in each coordinate results in

$$
q_{1}+\delta q_{1}=q_{0}+\delta q_{0}+\varepsilon\left(p_{y_{2}}+\delta p_{y_{2}}\right)
$$

subtracting this from equation (2) gives the change produced by the step.

$$
\delta q_{1}=\delta q_{0}+\varepsilon \delta p_{1 / 2}
$$

in matrix form

$$
\binom{\delta q_{1}}{\delta p_{v_{2}}}=\left(\begin{array}{ll}
1 & \varepsilon \\
0 & 1
\end{array}\right)\binom{\delta q_{0}}{\delta p_{v_{2}}}
$$

Let

$$
T_{2}=\left(\begin{array}{ll}
1 & \varepsilon \\
0 & 1
\end{array}\right)
$$

So

$$
\binom{\delta q_{1}}{\delta p_{v_{2}}}=T_{2}\binom{\delta q_{0}}{\delta p_{v_{2}}}
$$

and finally for the third step

3) $\ p_{1}=p_{1 / 2}+\frac{1}{2} \varepsilon F\left(q_{1}\right)$

An infinitesimal change in each coordinate results in

$$
p_{1}+\delta p_{1}=p_{12}+\delta p_{12}+\frac{1}{2} \varepsilon\left\{F\left(q_{1}\right)+F^{\prime}\left(q_{1}\right) \delta q_{1}\right\}
$$

subtracting this from equation (3) gives the change produced by the step.

$$
\delta p_{1}=\delta p_{1 / 2}+\frac{1}{2} \varepsilon F^{\prime}\left(q_{1}\right) \delta q_{1}
$$

In matrix form

$$
\binom{\delta p_{1}}{\delta q_{1}}=\left(\begin{array}{cc}
\frac{1}{\partial} \varepsilon F^{\prime}\left(q_{0}\right) & 1 \\
1 & 0
\end{array}\right)\binom{\delta q_{1}}{\delta p_{42}}
$$

Let

$$
T_{3}=\left(\begin{array}{cc}
\frac{1}{\partial \varepsilon} F^{\prime}\left(q_{0}\right) & 1 \\
1 & 0
\end{array}\right)
$$

so

$$
\binom{\delta p_{1}}{\delta q_{1}}=T_{3}\binom{\delta q_{1}}{\delta p_{42}}
$$

Bringing things together

$$
\binom{\delta q_{0}}{\delta p_{1 / 2}}=T_{1}\binom{\delta q_{0}}{\delta p_{0}}\binom{\delta q_{1}}{\delta p_{12}}=T_{2}\binom{\delta q_{0}}{\delta p_{12}}
$$

$$
\binom{\delta p_{1}}{\delta q_{1}}=T_{3}\binom{\delta q_{1}}{\delta p_{42}}
$$

It follows that the transformation performed be one step of the algorithm is given by

$$
\begin{aligned}
\binom{\delta q_{1}}{\delta p_{1}} & =T_{3}\binom{\delta q_{1}}{\delta p_{12}} \\
& =T_{3} T_{2}\binom{\delta q_{0}}{\delta p_{12}} \\
& =T_{3} T_{2} T_{1}\binom{\delta q_{0}}{\delta p_{0}}
\end{aligned}
$$

The matrix $T_{3} T_{2} T_{1}$ is the transpore of the Jacdoian matrix.

$$
J^{\top}=T_{3} T_{2} T_{1}
$$

Now to prove that the algorithm conserves phase space volume it must be shown that

$$
|J|=1
$$

using the well known result

$$
|J|=|J T|
$$

and another well known result

$$
\left|T_{3} T_{2} T_{1}\right|=\left|T_{3}\right|\left|T_{2}\right|\left|T_{1}\right|
$$

thus

$$
|J|=\left|T_{3}\right|\left|T_{2}\right|\left|T_{1}\right|
$$

Recalling

$$
\begin{gathered}
T_{1}=\left(\begin{array}{cc}
1 & 0 \\
\frac{1}{\partial \varepsilon} F^{\prime}\left(q_{0}\right) & 1
\end{array}\right) \quad T_{2}=\left(\begin{array}{ll}
1 & \varepsilon \\
0 & 1
\end{array}\right) \\
T_{3}=\left(\begin{array}{cc}
\frac{1}{\partial \varepsilon} F^{\prime}\left(q_{0}\right) & 1 \\
1 & 0
\end{array}\right)
\end{gathered}
$$

It follows that

$$
\left|T_{1}\right|=\left|T_{2}\right|=\left|T_{3}\right|=1
$$

thus

$$
|J|=1
$$

so Momentum Verlet conserves phase space volume.

## Euler Method

The steps for Euler Method integration of Hamittoris equations is given by,

$$
\begin{aligned}
& p_{i}(t+\varepsilon)=p_{i}(t)-\frac{\partial u}{\partial q_{i}} \varepsilon \\
& q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}(t)
\end{aligned}
$$

using the notation from the Momentum Derlet anahysis, and

$$
F\left(q_{k}\right)=-\left.\frac{\partial u}{\partial q}\right|_{k} \quad m_{i}=1
$$

gives

$$
\begin{aligned}
& p_{1}=p_{0}+\varepsilon F\left(q_{0}\right) \\
& q_{1}=q_{0}+\varepsilon p_{0}
\end{aligned}
$$

consider an infintesimal change in the coordinates

$$
\begin{aligned}
& p_{1}+\delta p_{1}=p_{0}+\delta p_{0}+\varepsilon F\left(q_{0}+\delta q_{0}\right) \\
& q_{1}+\delta q_{1}=q_{0}+\delta q_{0}+\varepsilon\left(p_{0}+\delta p_{0}\right)
\end{aligned}
$$

Recall that

$$
F\left(q_{0}+\delta q_{0}\right)=F\left(q_{0}\right)+F^{\prime}\left(q_{0}\right) \delta q_{0}
$$

so,

$$
p_{1}+\delta p_{1}=p_{0}+\delta p_{0}+\varepsilon\left\{F\left(q_{0}\right)+F^{\prime}\left(q_{0}\right) \delta q_{0}\right\}
$$

$$
q_{1}+\delta q_{1}=q_{0}+\delta q_{0}+\varepsilon\left(p_{0}+\delta p_{0}\right)
$$

It follows that the differtials evolve by the equations

$$
\begin{aligned}
& \delta p_{1}=\delta p_{0}+\varepsilon F^{\prime}\left(q_{0}\right) \delta q_{0} \\
& \delta q_{1}=\varepsilon \delta p_{0}+\delta q_{0}
\end{aligned}
$$

In matrix form

$$
\begin{aligned}
\binom{\delta p_{1}}{\delta q_{1}} & =\left(\begin{array}{cc}
1 & \varepsilon F^{\prime}\left(q_{0}\right) \\
\varepsilon & 1
\end{array}\right)\binom{\delta p_{0}}{\delta q_{0}} \\
& =T\binom{\delta p_{0}}{\delta q_{0}}
\end{aligned}
$$

The Jacobian matrix is related to $T$ by

$$
J^{\top}=T
$$

using

$$
|J|=\left|J^{\top}\right|=|T|
$$

gives

$$
\begin{aligned}
|T| & =\left|\begin{array}{cc}
1 & \varepsilon F^{\prime}\left(q_{0}\right) \\
\varepsilon & 1
\end{array}\right| \\
& =1-\varepsilon^{2} F^{\prime}\left(q_{0}\right)
\end{aligned}
$$

Thus the Euler method does
not exactly conserve phase space volume like Momentum verlet.

## Euler - Cromer

The steps for the Euter-Cromer integration of Hamilton's equations is given by

$$
\begin{aligned}
& p_{i}(t+\varepsilon)=p_{i}(t)-\varepsilon \frac{\partial u}{\partial q_{i}} \\
& q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}(t-\varepsilon)
\end{aligned}
$$

using previously used notation and

$$
F\left(q_{k}\right)=-\left.\frac{\partial u}{\partial q}\right|_{k} \quad m_{i}=1
$$

gives

$$
\begin{aligned}
& P_{1}=P_{0}+\varepsilon F\left(q_{0}\right) \\
& q_{1}=q_{0}+\varepsilon P_{1}
\end{aligned}
$$

consider an infintesimal change in the coordinates

$$
\begin{aligned}
& p_{1}+\delta p_{1}=p_{0}+\delta p_{0}+\varepsilon F\left(q_{0}+\delta q_{0}\right) \\
& q_{1}+\delta q_{1}=q_{0}+\delta q_{0}+\varepsilon\left(p_{1}+\delta p_{1}\right)
\end{aligned}
$$

Recall that

$$
F\left(q_{0}+\delta q_{0}\right)=F\left(q_{0}\right)+F^{\prime}\left(q_{0}\right) \delta q_{0}
$$

so the equations that the differentials follow are given by

1) $\delta p_{1}=\delta p_{0}+F^{\prime}\left(q_{0}\right) \delta q_{0}$
2) $\delta q_{1}=\delta q_{0}+\varepsilon \delta p_{1}$

The steps need to be evaluted seperately in the manner used in the conalysis of Momentum berlet. The Matrix form of equations 1 and 2 are given by

$$
\binom{\delta q_{0}}{\delta p_{1}}=\left(\begin{array}{cc}
1 & 0 \\
F^{\prime}\left(q_{0}\right) & 1
\end{array}\right)\binom{\delta q_{0}}{\delta p_{0}}
$$

$$
\binom{\delta q_{1}}{\delta p_{1}}=\left(\begin{array}{ll}
1 & \varepsilon \\
0 & 1
\end{array}\right)\binom{\delta q_{0}}{\delta p_{1}}
$$

Let

$$
\begin{gathered}
T_{1}=\left(\begin{array}{cc}
1 & 0 \\
F^{\prime}\left(q_{0}\right) & 1
\end{array}\right) \\
T_{2}=\left(\begin{array}{ll}
1 & \varepsilon \\
0 & 1
\end{array}\right)
\end{gathered}
$$

It follows that

$$
\begin{aligned}
\binom{\delta q_{1}}{\delta p_{1}} & =T_{2}\binom{\delta q_{0}}{\delta p_{1}} \\
& =T_{2} T_{1}\binom{\delta q_{0}}{\delta p_{0}}
\end{aligned}
$$

The matrix $T_{2} T_{1}$ is the transpose of the Jacobian matrix JT

$$
J^{\top}=T_{2} T_{1}
$$

Now to prove that the algorithm conserves phase space volume it must be shown that

$$
|J|=1
$$

using the well known result

$$
|J|=|J T|
$$

thus

$$
|J|=\left|T_{2} T_{1}\right|
$$

and the other well known result on the product of determinates

$$
\left|T_{2} T_{1}\right|=\left|T_{2}\right|\left|T_{1}\right|
$$

From inspection

$$
\left|T_{2}\right|=\left|T_{1}\right|=l
$$

It follows that

$$
|J|=\left|T_{2}\right|\left|T_{1}\right|=l
$$

Thus the Euler-Cromer algorithm conserves phase space volume.

## Summay of Porfomance Analysis

The following results have been proven

1) The Euler method of integration of Hamilton's equations does not conserve phase space volume. This result is responsible for the poor performance of algorithm. Later it will be seen the Euler method is explosively unstable. Time integration of the equations does not conserve energy but integration errors caluse growth in energy and increase in phase space volume. In addition to not conserving errors were shown to be
$O\left(\varepsilon^{2}\right)$ since derivatives are evaluated using the forward difference algorithm.
2) The modification of the Euler method known as the Euler-Cromer method has been shown to exactly Conserve phase space volume. Integration errors have been shown to be $o\left(\varepsilon^{2}\right)$ since derivatives are evaluated using forward differences.
3) The Momentum Verlet method of integrating Hamilton's equations has been shown to conserve phase space volume and to have integration error $o\left(\varepsilon^{3}\right)$ since derivatives are evaluated using the Centered Difference method for evaluation of derivatives. In the evalution of example problems it
will be seen that Momertum verlet has the best performance.

## Hamilton's Equation Integration Examples

As an example consider a one-dimensional system with kinetic energy and potential energy given by

$$
K(p)=\frac{p^{2}}{2} \quad U(q)=\frac{q^{2}}{2}
$$

so that the Hamiltonian is given by

$$
H(p, q)=\frac{p^{2}}{2}+\frac{q^{2}}{2}
$$

It follows that Hamilton's equations

$$
\frac{d p}{d t}=-\frac{\partial H}{\partial q} \quad \frac{d g}{d t}=\frac{\partial H}{\partial p}
$$

using this Hamiltonian gives the following equations

$$
\frac{d p}{d t}=-q \quad \frac{d q}{d t}=p
$$

which can be solved in the following manner

$$
\begin{aligned}
& \frac{d^{2} a}{d t^{2}}-\frac{d p}{d t}=0 \\
\Rightarrow & \frac{d^{2} a}{d t^{2}}-a=0
\end{aligned}
$$

a solution to this equation is

$$
q(t)=A \cos (t)
$$

So

$$
p=\frac{d q}{d t}=-A \sin (t)
$$

It follows that

$$
H=\frac{A^{2}}{2}\left(\sin ^{2} t+\cos ^{2} t\right)
$$

so curves of constant Hamiltonian are circles with radius, $r$,

$$
r=\frac{A}{\sqrt{2}}
$$

The period of the motion, $\tau$, is given by

$$
\tau=2 \pi
$$

Now the canonical distribution is given by

$$
f(p, q) \propto e^{-\frac{p 2}{2}-\frac{q 2}{2}}
$$

Contours of constant probability for this distribution are shown in the following figure
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-066.jpg?height=807&width=808&top_left_y=1138&top_left_x=390)

In the following examples Hamiltons equations are integrated using each of the integration method's discussed along a contour where it is assumed that $A=1$ in the previously obtained solution, so that

$$
p^{2}+q^{2}=2
$$

the canonical distribution contow following this solution has value

$$
e^{-1}=0.37
$$

The initial values of $p$ and $q$ for all simulations are assumed to by

$$
q_{0}=1 \quad p_{0}=-1
$$

The first plots compare the error in the solutions obtained using each method integrated over about one period in the first plot and 5 periods in the second plot using a step size of

$$
\Delta t=0.1
$$

The integration error is computer using the equation

$$
\Delta_{\text {Error }}=\left|\sqrt{2}-\sqrt{p^{2}+q^{2}}\right|
$$

![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-068.jpg?height=590&width=802&top_left_y=608&top_left_x=388)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-068.jpg?height=565&width=797&top_left_y=1267&top_left_x=403)

The instability of the Euler method of inlegrating Hamilton's equations is apporent where it is seen that the error in the Hamiltonian increases rapidly. Both Momentum Verlet and Euler-Cromer methods are stable. This difference in behavior is a result of conservation of phase space volume of the Momentum verlet and Euler-Cromer integration methods. Euler. Cromer shows periodic error as large as 6\% while Momentum verlet errors are not visible at the chosen scale this difference is a consequence of the difference in accuracy of the methods. Recall that Euler-cromer has accuracy $O\left(\varepsilon^{2}\right)$ and Momentum verlet has accuracy $O\left(\varepsilon^{3}\right)$.
The following plots show the phase space trajectories of each

## integration method for different choices of stepsize.

Hamilton's Equations (Euler Method): $\Delta \mathrm{t}=0.1$, nsteps $=50$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-070.jpg?height=616&width=668&top_left_y=338&top_left_x=108)

Hamilton's Equations (Euler Method): $\Delta \mathrm{t}=0.1$, nsteps $=150$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-070.jpg?height=608&width=636&top_left_y=340&top_left_x=814)

![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-070.jpg?height=632&width=668&top_left_y=1007&top_left_x=467)

The first three plots show the trajectories obtained by integration using the Euler method. The contour

## of the Canonical distribution satisfing

$$
q^{2}+p^{2}=2
$$

is indicated by the blue circle. The trajectory rapidly diverges quickly for step size $\varepsilon=0.1$ shown in the first two plots. The third plots shows the trajectory obtained with step size $\varepsilon=0.01$. Even with this very small step size the Hamiltonian increases without bound
The following two plots show the trajectories obtained by integration using the Euler-Cromer method. The periodic deveations of the

Hamilton's Equations (Modified Euler Method): $\Delta t=0.1$, nsteps $=50$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-071.jpg?height=549&width=631&top_left_y=1388&top_left_x=147)

Hamilton's Equations (Modified Euler Method): $\Delta t=0.1$, nsteps $=300$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-071.jpg?height=543&width=636&top_left_y=1394&top_left_x=844)

of the Hamiltonian seen in the error plot are apparent in the trajectory where deviations along the line $p=q$ are visible.
The final plots show the trajectories obtained by interagration using the Momentum verlet method. Deviations of the tragectory from $q^{2}+p^{2}=2$ are not usible at the scale shown in the plot.

Hamilton's Equations (Momentum Verlet): $\Delta \mathrm{t}=0.1$, nsteps $=50$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-072.jpg?height=561&width=622&top_left_y=1005&top_left_x=195)

Hamilton's Equations (Momentum Verlet): $\Delta t=0.1$, nsteps $=300$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-072.jpg?height=565&width=608&top_left_y=1003&top_left_x=870)

As an illustration of the stability, of Momentum verlet integration a trasectory is computed using a very large step size of $I \varepsilon=0.5$.
this step size is about $10 \%$ of the tragectory period. Each step falls on the curve

$$
q^{2}+p^{2}=2
$$

at the resultion shown.

Hamilton's Equations (Momentum Verlet): $\Delta \mathrm{t}=0.5$, nsteps $=10$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-073.jpg?height=580&width=636&top_left_y=640&top_left_x=88)

Hamilton's Equations (Momentum Verlet): $\Delta \mathrm{t}=0.5$, nsteps $=60$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-073.jpg?height=574&width=597&top_left_y=648&top_left_x=830)

## Hamittonian Monte Carlo Examples

This section will investigate examples of samples generated using the Hamiltonian Monte Carlo method. The first example consider is a one dimensional Normal distribution. This example will be followed by simulation of of the Broariate Normal distributions. Three methods are used to generate samples, Hamiltonian Monte Carlo, Ciblss Sampling, and Metropolis Hastings and the results are compared.

## One - Dimensional Normal Distribution Simulated using Hamiltonin Monte Carlo

The Kinetic Energy and Potential Energy functions for the onedimensional Normal distribution are given by

$$
K(p)=\frac{p^{2}}{2 m} \quad u(q)=\frac{q^{2}}{2 \sigma^{2}}
$$

where $m$ is the mass, which is the variance of the momentum distribution and $\delta^{2}$ is the variance of the position cordinate.
For the first example consider the case $m=1$ and $0^{2}=1$. The target distribution will be

$$
f(q)=\frac{1}{\sqrt{2 \pi}} e^{-\frac{1}{2} q^{2}}
$$

Now Hamilton's equations are given by

$$
\begin{aligned}
& \frac{d p}{d t}=-\frac{\partial H(p, q)}{\partial q_{i}} \\
& \frac{d q}{d t}=\frac{\partial H(p, q)}{\partial p_{i}}
\end{aligned}
$$

The Hamiltonian is given by

$$
H(p, q)=\frac{1}{2} p^{2}+\frac{1}{2} q^{2}
$$

It follows that

$$
\begin{aligned}
& \frac{d p}{d t}=-q \\
& \frac{d q}{d t}=p
\end{aligned}
$$

The solution to these equations were discyssed in the previous section. Here the focus will be on the results obtained from similulation. The target distribution is the whitnormal gaussion which shown in the following plot

Normal Target PDF, $\sigma=1.0$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-077.jpg?height=618&width=926&top_left_y=96&top_left_x=312)

The parameters used in the integration of Hamilton's equation are

$$
\Delta t=0.1 \quad \text { nsteps }=50
$$

with initial condition

$$
q(0)=1.0
$$

The number of samples generated is 10,000 and for the following, results 99.990 of the samples were accepted. This should be compared with Metropolis Hastings simulations where good performing simulations have an acceptance
of $80 i_{0}$ of the samples.
The following plot compares a histogram computed from the simulation results with the target distribution favorably
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-078.jpg?height=678&width=942&top_left_y=570&top_left_x=298)

A slice of the generate time series between sample 9000 and 9500 is shown in the following plot. Neticable differences when compared with Metropolis Hasings simulations are the absence of constant runs created by rejection
of proposed samples and lack of autocorrelation naticable by the frequent changes in direction

HMC Normal Target: $\Delta \mathrm{t}=0.1$, nsteps $=50$, nsample $=10000$, accepted $=9992$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-079.jpg?height=420&width=1136&top_left_y=457&top_left_x=229)

> The following plots illustrate the convergence of the sample mean and standard deviation to the target values of 0 and 1 respectively
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-079.jpg?height=612&width=868&top_left_y=1382&top_left_x=354)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-080.jpg?height=579&width=814&top_left_y=52&top_left_x=376)

Both plots illustrate accepable convergence within only a few thousand samples.
The final plot shows the series autscorrelation as a function of time las. It is seen that very rapidly, within less than 5 samples, the auto correlation is zero.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-080.jpg?height=531&width=746&top_left_y=1438&top_left_x=439)

## Review of Bisariate Normal Distribution

Consider the random vector

$$
q^{\top}=\left(q_{1}, q_{2}, q_{3}, \ldots, q_{n}\right)
$$

if the vector distribution is a Multivariate Nomal then the probability density is given by
$f(q)=\frac{1}{(2 \pi)^{n / 2} \sqrt{|\Sigma|}} \exp \left[-\frac{1}{2}(q-\mu)^{\top} \Sigma^{-1}(q-\mu)\right]$
where is the mean vector for q)

$$
\mu^{\top}=\left(\mu_{1}, \mu_{2}, \mu_{3}, \ldots, \mu_{n}\right)
$$

and $\Sigma$ is the covariance matrix

$$
\Sigma_{i j}=\operatorname{cov}\left(q_{i} q_{j}\right)
$$

For the Bivariate case where

$$
\begin{array}{r}
q^{\top}=\left(q_{1}, q_{2}\right) \\
\mu^{\top}=\left(\mu_{1}, \mu_{2}\right) \\
\Sigma=\left(\begin{array}{ll}
\sigma_{1}^{2} & \gamma \sigma_{1} \sigma_{2} \\
\gamma \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right)
\end{array}
$$

where $\sigma_{i}$ is the standard deviation of $q_{i}$ and $\gamma$ is the correlation coeficient

$$
\gamma=\frac{\operatorname{Cov}\left(q_{1}, q_{2}\right)}{\sigma_{1} \sigma_{2}}=\frac{\operatorname{Cov}\left(q_{2}, q_{1}\right)}{\sigma_{1} \sigma_{2}}
$$

If $\gamma=0$ then $q_{1}$ and $q_{2}$ are independent and if $r=1$ then $q_{1}=q_{2}$. If $r \neq 1$ then

$$
\Sigma^{-1}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} \\
-\gamma \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right)
$$

The marginal distributions are given by

$$
\begin{aligned}
& f\left(q_{1}\right)=\frac{1}{\sqrt{2 \pi \sigma_{1}^{2}}} e^{-\frac{\left(q_{1}-\mu_{1}\right)^{2}}{2 \sigma^{2}}} \\
& f\left(q_{2}\right)=\frac{1}{\sqrt{2 \pi \sigma_{2}^{2}}} e^{-\frac{\left(q_{2}-\mu_{2}\right)^{2}}{2 \sigma_{2}^{2}}}
\end{aligned}
$$

The conditional distributions are given by

$$
\begin{aligned}
& f\left(q_{1} \mid q_{2}\right)=\frac{1}{\sigma_{1} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} \exp \{ \\
& \left.\frac{-1}{2 \sigma^{2}\left(1-\gamma^{2}\right)}\left[q_{1}-\left(\mu_{1}+\frac{\gamma \sigma_{1}}{\sigma_{2}}\left(q_{2}-\mu_{2}\right)\right)\right]^{2}\right\}
\end{aligned}
$$

$$
\begin{aligned}
& f\left(q_{2} \mid q_{1}\right)=\frac{1}{\sigma_{2} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} \exp \{ \\
& \frac{-1}{2 \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left[q_{2}-\left(\mu_{2}+\frac{\gamma \sigma_{2}}{\sigma_{1}}\left(q_{1}-\mu_{1}\right)\right]^{2}\right\}
\end{aligned}
$$

the conditional mean and variance are given by

$$
\begin{aligned}
& E\left[q_{1} \mid q_{2}\right]=\mu_{1}+\frac{\gamma \sigma_{1}}{\sigma_{2}}\left(q_{2}-\mu_{2}\right) \\
& E\left[q_{2} \mid q_{1}\right]=\mu_{2}+\frac{\gamma \sigma_{2}}{\sigma_{1}}\left(q_{1}-\mu_{1}\right) \\
& \operatorname{Var}\left[q_{1} \mid q_{2}\right]=\sigma_{1}^{2}\left(1-\gamma^{2}\right) \\
& \operatorname{Var}\left[q_{2} \mid q_{1}\right]=\sigma_{2}^{2}\left(1-\gamma^{2}\right)
\end{aligned}
$$

The determinate of the correlation matix is given by

$$
\begin{aligned}
|\Sigma| & =\left|\begin{array}{cc}
\sigma_{1}^{2} & \gamma \sigma_{1} \sigma_{2} \\
\gamma \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right| \\
& =\sigma_{1}^{2} \sigma_{2}^{2}-\gamma^{2} \sigma_{1}^{2} \sigma_{2}^{2} \\
& =\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)
\end{aligned}
$$

Finally the joint density is given by

$$
\begin{aligned}
& Q_{1}=\frac{\left(q_{1}-\mu_{1}\right)}{2 \sigma_{1}} \quad Q_{2}=\frac{\left(q_{2}-\mu_{2}\right)}{2 \sigma_{2}} \\
& f\left(q_{1}, q_{2}\right)=\frac{1}{2 \pi \sqrt{|\Sigma|}} \exp \left[-\frac{1}{2\left(1-\gamma^{2}\right)}\left(Q_{1}^{2}\right.\right. \\
& \left.\left.+Q_{2}^{2}-2 \gamma Q_{1} Q_{2}\right)\right]
\end{aligned}
$$

## Hamiltonian Monte Carlo Sampling of Bivariate Normal Distribution

The Kinetic Energy and Potential Energy functions for the Bivariate Normal distribution is given by

$$
\begin{aligned}
& K(p)=\frac{1}{2} P^{\top} M^{-1} P \\
& u(q)=\frac{1}{2} q^{\top} \Sigma^{-1} q \\
& \Sigma=\left(\begin{array}{ll}
\sigma_{1}^{2} & \gamma_{0} \sigma_{2} \\
\gamma_{0} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right)
\end{aligned}
$$

For the first example assume that

$$
\begin{gathered}
\mu=\left(\begin{array}{cc}
m_{1} & 0 \\
0 & m_{2}
\end{array}\right) \\
\Sigma^{-1}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} \\
-\gamma \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right)
\end{gathered}
$$

So

$$
k(p)=\frac{1}{2}\left(\frac{p_{1}^{2}}{m_{1}}+\frac{p_{2}^{2}}{m_{2}}\right)
$$

## and

$$
\begin{aligned}
& u(q)=\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1} q_{2}\right)\left(\begin{array}{cc}
\sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} \\
-\gamma \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right)\binom{q_{1}}{q_{2}} \\
& =\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1} q_{2}\right)\left(\begin{array}{ll}
q_{1} \sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} q_{2} \\
-\gamma \sigma_{1} \sigma_{2} q_{1}+\sigma_{1}^{2} q_{2}
\end{array}\right)
\end{aligned}
$$

$=\frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left\{q_{1}\left(q_{1} \sigma_{2}^{2}-q_{2} \gamma \sigma_{1} \sigma_{2}\right)\right.$

$$
\begin{aligned}
& \left.+q_{2}\left(\sigma_{1}^{2} q_{2}-q_{1} \gamma \sigma_{1} \sigma_{2}\right)\right\} \\
= & \frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1}^{2} \sigma_{2}^{2}+q_{2}^{2} \sigma_{1}^{2}-2 q_{2} q_{1} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

Now Hamitton's equation are given by

$$
\begin{aligned}
& \frac{d p_{i}}{d t}=-\frac{\partial H(p, q)}{\partial q_{i}} \\
& \frac{d q_{i}}{d t}=\frac{\partial H(p, q)}{\partial p_{i}}
\end{aligned}
$$

The Hamiltonian is given by

$$
\begin{aligned}
H(p, q) & =k(p)+u(q) \\
& =\frac{1}{2}\left(\frac{p_{1}^{2}}{m_{1}}+\frac{p_{2}^{2}}{m_{2}}\right)+ \\
& \frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1}^{2} \sigma_{2}^{2}+q_{2}^{2} \sigma_{1}^{2}-2 q_{2} q_{1} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\frac{d p_{1}}{d t}=-\frac{\partial H}{\partial q_{1}} & =\frac{-1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(2 q_{1} \sigma_{2}^{2}-2 q_{2} \gamma \sigma_{1} \sigma_{2}\right) \\
& =\frac{-1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1} \sigma_{2}^{2}-q_{2} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
\frac{d p_{2}}{d t}=\frac{\partial H}{\partial q_{2}} & =\frac{-1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(2 q_{2} \sigma_{1}^{2}-2 q_{1} \gamma \sigma_{1} \sigma_{2}\right) \\
& =\frac{-1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{2} \sigma_{1}^{2}-q_{1} \gamma \sigma_{1} \sigma_{2}\right) \\
\frac{d q_{1}}{d t}=\frac{\partial H}{\partial p_{1}} & =\frac{p_{1}}{m_{1}} \\
\frac{d q_{2}}{d t}=\frac{\partial H}{\partial p_{2}} & =\frac{p_{2}}{m_{2}}
\end{aligned}
$$

Recall the steps for the Momentum verlet method

1) $P_{i}\left(t+\frac{1}{2} \varepsilon\right)=P_{i}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t}$
2) $q_{i}(t+\varepsilon)=q_{i}(t)+\varepsilon \frac{p_{i}}{m_{i}}\left(t+\frac{1}{2} \varepsilon\right)$
3) $p_{i}(t+\varepsilon)=p_{i}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{i}}\right|_{t+\varepsilon}$

Let

$$
\begin{aligned}
& \frac{\partial u}{\partial q_{1}}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1} \sigma_{2}^{2}-q_{2} \gamma \sigma_{1} \sigma_{2}\right) \\
& \frac{\partial u}{\partial q_{2}}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{2} \sigma_{1}^{2}-q_{1} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

It follows that the integration steps are given by

1) $P_{1}\left(t+\frac{1}{2} \varepsilon\right)=P_{1}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial \varphi_{1}}\right|_{t}$
2) $q_{1}(t+\varepsilon)=q_{1}(t)+\varepsilon p_{1}\left(t+\frac{1}{2} \varepsilon\right)$
3) $p_{1}(t+\varepsilon)=p_{1}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{1}}\right|_{t+\varepsilon}$
4) $p_{2}\left(t+\frac{1}{2} \varepsilon\right)=p_{2}(t)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{2}}\right|_{t}$
5) $q_{2}(t+\varepsilon)=q_{2}(t)+\varepsilon \frac{p_{2}}{m_{2}}\left(t+\frac{1}{2} \varepsilon\right)$
6) $p_{2}(t+\varepsilon)=p_{2}\left(t+\frac{1}{2} \varepsilon\right)-\left.\frac{1}{2} \varepsilon \frac{\partial u}{\partial q_{2}}\right|_{t+\varepsilon}$

## Analytic Solution to Hamitton's Equations for Bivarite Normal Distribution

Hamilton's equations for the Bivariate Normal distribution are given by,

$$
\begin{aligned}
& \frac{d p_{1}}{d t}=-\frac{\partial H}{\partial q_{1}}=\frac{-1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1} \sigma_{1}^{2}-q_{2} \gamma \sigma_{1} \sigma_{2}\right) \\
& \frac{d p_{2}}{d t}=\frac{\partial H}{\partial q_{2}}=\frac{-1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{2} \sigma_{2}^{2}-q_{1} \gamma \sigma_{1} \sigma_{2}\right) \\
& \frac{d q_{1}}{d t}=\frac{\partial H}{\partial p_{1}}=\frac{p_{1}}{m_{1}} \\
& \frac{d q_{2}}{d t}=\frac{\partial H}{\partial p_{2}}=\frac{p_{2}}{m_{2}}
\end{aligned}
$$

To simplify things assume that

$$
\sigma_{1}=\sigma_{2}=1 \quad m_{1}=m_{2}=1
$$

and let

$$
\alpha=\frac{1}{1-\gamma^{2}}
$$

also swith to dot notation for time derivatives. It follows that

$$
\begin{aligned}
& \dot{p}_{1}=-\alpha\left(q_{1}-\gamma q_{2}\right) \\
& \dot{p}_{2}=-\alpha\left(q_{2}-\gamma q_{1}\right) \\
& \dot{q}_{1}=p_{1} \\
& \dot{q}_{2}=p_{2}
\end{aligned}
$$

In matrix form

$$
\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right]=\left[\begin{array}{cccc}
0 & 0 & -\alpha & \alpha \gamma \\
0 & 0 & \alpha \gamma & -\alpha \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{array}\right]\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right]
$$

The solution is given by

$$
\left[\begin{array}{l}
P_{1} \\
P_{2} \\
q_{1} \\
q_{2}
\end{array}\right]=\sum_{i=1}^{4} c_{i} E^{i} e^{-\lambda_{i} t}
$$

where the $c_{i}$ are constants, the $E_{i}$ are eigen vectors, and $\lambda_{i}$ the eigen values of the matrix.

$$
\left[\begin{array}{cccc}
0 & 0 & -\alpha & \alpha \gamma \\
0 & 0 & \alpha \gamma & -\alpha \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{array}\right]
$$

The eigenoales are found by soloing the equation

$$
\left|\begin{array}{cccc}
-\lambda & 0 & -\alpha & \alpha \gamma \\
0 & -\lambda & \alpha \gamma & -\alpha \\
1 & 0 & -\lambda & 0 \\
0 & 1 & 0 & -\lambda
\end{array}\right|=0
$$

Now expanding to $3 \times 3$ determinates gives

$$
\begin{aligned}
& \left|\begin{array}{cccc}
\lambda & 0 & -\alpha & \alpha \gamma \\
0 & -\lambda & \alpha \gamma & -\alpha \\
1 & 0 & -\lambda & 0 \\
0 & 1 & 0 & \lambda
\end{array}\right|= \\
& -\lambda\left|\begin{array}{ccc}
-\lambda & \alpha \gamma & -\alpha \\
0 & -\lambda & 0 \\
1 & 0 & -\lambda
\end{array}\right|-0\left|\begin{array}{ccc}
0 & \alpha \gamma & -\alpha \\
1 & -\lambda & 0 \\
0 & 0 & -\lambda
\end{array}\right| \\
& -\alpha\left|\begin{array}{ccc}
0 & -\lambda & -\alpha \\
1 & 0 & 0 \\
0 & 1 & -\lambda
\end{array}\right|-\alpha \gamma\left|\begin{array}{ccc}
0 & -\lambda & \alpha \gamma \\
1 & 0 & -\lambda \\
0 & 1 & 0
\end{array}\right|
\end{aligned}
$$

Now

$$
\begin{aligned}
& \left|\begin{array}{ccc}
-\lambda & \alpha \gamma & -\alpha \\
0 & -\lambda & 0 \\
1 & 0 & -\lambda
\end{array}\right|=-\lambda\left(\lambda^{2}-0\right)-\alpha \gamma(0-0) \\
& =-\lambda^{3}-\alpha \lambda \\
& \left|\begin{array}{ccc}
0 & \alpha \gamma & -\alpha \\
1 & -\lambda & 0 \\
0 & 0 & -\lambda
\end{array}\right|=0\left(\lambda^{2}-0\right)-\alpha \gamma(-\lambda-0) \\
& =-\alpha(0-0) \\
& \left|\begin{array}{ccc}
0 & -\lambda & -\alpha \\
1 & 0 & 0 \\
0 & 1 & -\lambda
\end{array}\right|=0(0-0)+\lambda(-\lambda-0) \\
& =-\lambda^{2}-\alpha
\end{aligned}
$$

$$
\begin{aligned}
& \left|\begin{array}{ccc}
0 & -\lambda & \alpha \gamma \\
1 & 0 & -\lambda \\
0 & 1 & 0
\end{array}\right|=\alpha(0+\lambda)+\lambda(0-0) \\
& =\alpha \gamma
\end{aligned}
$$

Putting things together gives the characterstic equation

$$
\begin{aligned}
-\lambda\left(-\lambda^{3}-\alpha \lambda\right)-O(\alpha \gamma \lambda)-\alpha\left(-\lambda^{2}-\alpha\right)
-\alpha \gamma(\alpha \gamma)=& 0 \\
\Rightarrow& \lambda^{4}+\alpha \lambda^{2}+\alpha \lambda^{2}+\alpha^{2}-\alpha^{2} \gamma^{2}=0 \\
\Rightarrow& \lambda^{4}+2 \alpha \lambda^{2}+\alpha^{2}\left(1-\gamma^{2}\right)=0
\end{aligned}
$$

But

$$
\alpha=\frac{1}{1-\gamma^{2}}
$$

so the characteristic equation becomes

$$
\lambda^{4}+2 \alpha \lambda^{2}+\alpha=0
$$

This is a quadratic equation
for $\lambda^{2}$. Completing the square gives

$$
\begin{aligned}
& \lambda^{4}+2 \alpha \lambda^{2}+\alpha+\alpha^{2}-\alpha^{2}=0 \\
\Rightarrow & \lambda^{4}+2 \alpha \lambda^{2}+\alpha^{2}=\alpha^{2}-\alpha \\
\Rightarrow & \left(\lambda^{2}+\alpha\right)^{2}=\alpha(\alpha-1) \\
\Rightarrow & \lambda^{2}+\alpha= \pm \sqrt{\alpha(\alpha-1)} \\
\Rightarrow & \lambda^{2}=-\alpha \pm \sqrt{\alpha(\alpha-1)}
\end{aligned}
$$

This expression can be simplified furthur using

$$
\alpha=\frac{1}{1-\gamma^{2}}
$$

gives

$$
\begin{gathered}
\alpha(\alpha-1)=\frac{1}{1-\gamma^{2}}\left[\frac{1}{1-\gamma^{2}}-1\right] \\
=\frac{1}{1-\gamma^{2}}\left[\frac{1}{1-\gamma^{2}}-\frac{1-\gamma^{2}}{1-\gamma^{2}}\right]=\frac{1}{1-\gamma^{2}}\left[\frac{1-1+\gamma^{2}}{1-\gamma^{2}}\right]
\end{gathered}
$$

$$
=\frac{1}{1-\gamma^{2}}\left(\frac{\gamma^{2}}{1-\gamma^{2}}\right)=\frac{\gamma^{2}}{\left(1-\gamma^{2}\right)^{2}}=\alpha^{2} \gamma^{2}
$$

thus

$$
\begin{aligned}
\lambda^{2} & =-\alpha \pm \sqrt{\alpha(\alpha-1)} \\
& =-\alpha \pm \alpha \gamma \\
& =-\alpha(1 \pm \gamma)
\end{aligned}
$$

It follows that the four eigenvalues are given by

$$
\pm \sqrt{-\alpha(1+\gamma)} \pm \sqrt{-\alpha(1-\gamma)}
$$

definition

$$
0 \leqslant \gamma<1 \quad \alpha>0
$$

thus all the eigen values are pure imaginary so

$$
\pm i \sqrt{\alpha(1+\gamma)} \pm i \sqrt{\alpha(1-\gamma)}
$$

The eigen vectors are the solution to the equation

$$
\left[\begin{array}{cccc}
-\lambda & 0 & -\alpha & \alpha \gamma \\
0 & -\lambda & \alpha \gamma & -\alpha \\
1 & 0 & -\lambda & 0 \\
0 & 1 & 0 & -\lambda
\end{array}\right]\left[\begin{array}{l}
E_{1} \\
E_{2} \\
E_{3} \\
E_{4}
\end{array}\right]=0
$$

Multiplying the matrices gives the equations

$$
\begin{aligned}
& -\lambda E_{1}-\alpha E_{3}+\alpha \gamma E_{4}=0 \\
& -\lambda E_{2}+\alpha \gamma E_{3}-\alpha E_{4}=0 \\
& E_{1}-\lambda E_{3}=0 \\
& E_{2}-\lambda E_{4}=0
\end{aligned}
$$

The last two equations give

$$
\begin{aligned}
& E_{1}=\lambda E_{3} \\
& E_{2}=\lambda E_{4}
\end{aligned}
$$

Eliminating $E_{1}$ and $E_{2}$ from the first equations gives

$$
\begin{aligned}
& -\lambda^{2} E_{3}-\alpha E_{3}+\alpha \gamma E_{4}=0 \\
& -\lambda^{2} E_{3}+\alpha \gamma E_{3}-\alpha E_{4}=0
\end{aligned}
$$

From the first equation

$$
E_{4}=\frac{1}{\alpha \gamma} E_{3}\left(\lambda^{2}+\alpha\right)
$$

$E_{3}$ is arbitrary assume that

$$
E_{3}=1
$$

then

$$
\begin{aligned}
& E_{3}=1 \\
& E_{4}=\frac{1}{\alpha \gamma}\left(\lambda^{2}+\alpha\right) \\
& E_{1}=\lambda \\
& E_{2}=\frac{\lambda}{\alpha \gamma}\left(\lambda^{2}+\alpha\right)
\end{aligned}
$$

For the first eigenvalue

$$
\begin{aligned}
\lambda_{1} & =i \sqrt{\alpha(1+\gamma)} \\
\frac{1}{\alpha \gamma}\left(\lambda_{1}^{2}+\alpha\right) & =\frac{1}{\alpha \gamma}[-\alpha(1+\gamma)+\alpha]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\alpha \gamma}(-\alpha \gamma)=-1 \\
& E^{\prime}=\left[\begin{array}{c}
i \sqrt{\alpha(1+\gamma)} \\
-i \sqrt{\alpha(1+\gamma)} \\
1 \\
-1
\end{array}\right]
\end{aligned}
$$

for the second eigenvalue

$$
\begin{aligned}
\lambda_{2} & =-i \sqrt{\alpha(1+\gamma)} \\
\frac{1}{\alpha \gamma}\left(\lambda_{2}^{2}+\alpha\right) & =-1 \\
E^{2} & =\left[\begin{array}{c}
-i \sqrt{\alpha(1+\gamma)} \\
i \sqrt{\alpha(1+\gamma)} \\
1 \\
-1
\end{array}\right]
\end{aligned}
$$

for the third

$$
\lambda_{3}=i \sqrt{\alpha(1-\gamma)}
$$

$$
\begin{aligned}
& \frac{1}{\alpha \gamma}\left(\lambda_{3}^{2}+\alpha\right)=\frac{1}{\alpha \gamma}[-\alpha(1-\gamma)+\alpha] \\
&=1 \\
& E^{3}=\left[\begin{array}{c}
i \sqrt{\alpha(1-\gamma)} \\
i \sqrt{\alpha(1-\gamma)} \\
1 \\
1
\end{array}\right]
\end{aligned}
$$

and finally for the last eigenvalue

$$
\begin{gathered}
\lambda_{4}=-i \sqrt{\alpha(1-\gamma)} \\
\frac{1}{\alpha \gamma}\left(\lambda_{4}^{2}+\alpha\right)=1 \\
E^{4}=\left[\begin{array}{c}
-i \sqrt{\alpha(1-\gamma)} \\
-i \sqrt{\alpha(1-\gamma)} \\
1
\end{array}\right]
\end{gathered}
$$

Let

$$
\omega_{ \pm}=\sqrt{\alpha(1 \pm \gamma)}
$$

then

$$
\begin{array}{cc}
\lambda_{1}=i \omega_{+} & \lambda_{2}=-i \omega_{+} \quad \lambda_{3}=i \omega_{-} \\
\lambda_{4}=-i \omega_{-} &
\end{array}
$$

It follows that

$$
\left[\begin{array}{l}
P_{1} \\
P_{2} \\
q_{1} \\
q_{2}
\end{array}\right]=\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]\left[\begin{array}{l}
c_{1} e^{i \omega_{+} t} \\
c_{2} e^{-i \omega_{+} t} \\
c_{3} e^{i \omega_{-} t} \\
c_{4} e^{-i \omega_{-} t}
\end{array}\right]
$$

let

$$
P Q=\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right] \quad C=\left[\begin{array}{l}
c_{1} \\
c_{2} \\
c_{3} \\
c_{4}
\end{array}\right]
$$

$$
E=\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]
$$

where $C_{i}$ are constants determined by intial conditions. To detormine the $C_{i}$ let $t=0$ and denote the initial values of $p_{i}$ and $q_{i}$ by

$$
\begin{gathered}
P_{1}^{0}, P_{2}^{0}, q_{1}^{0}, q_{2}^{0} \\
C=E^{-1} P_{0} Q_{0}
\end{gathered}
$$

where

$$
P_{0} Q_{0}=\left[\begin{array}{l}
p_{1}^{0} \\
p_{2}^{0} \\
q_{1}^{0} \\
q_{2}^{0}
\end{array}\right]
$$

## Solution Evaluation

## Consider the initial condition

$$
(P Q)_{0}=\left[\begin{array}{l}
1 \\
1 \\
1 \\
1
\end{array}\right]
$$

with parameters

$$
\gamma=0,9 \quad \alpha=\frac{1}{\left(1-0,9^{2}\right)}=5.2631
$$

The eigenvalues are given by

$$
\begin{aligned}
\omega_{ \pm}=\sqrt{\alpha(1 \pm \gamma)} \\
\lambda_{1}=i \omega_{+} \quad \lambda_{2}=-i \omega_{+} \\
\lambda_{4}=-i \omega_{-}
\end{aligned} \quad \lambda_{3}=i \omega_{-}
$$

so

$$
\omega_{+}=3.1623 \quad \omega_{-}=0.7255
$$

and

$$
\begin{array}{ll}
\lambda_{1}=i 3.1623 & \lambda_{2}=-i 3.1623 \\
\lambda_{3}=i 0.7255 & \lambda_{4}=-i 0.7255
\end{array}
$$

The eigenvector matrix is given by

$$
\begin{aligned}
E &=\left[\begin{array}{cccc}i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\ -i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\ 1 & 1 & 1 & 1 \\ -1 & -1 & 1 & 1\end{array}\right] \\
&=\left[\begin{array}{cccc}i 3.1623 & -i 3.1623 & i 0.7255 & -i 0.7255 \\ -i 3.1623 & i 3.1623 & i 0.7255 & -i 0.7255 \\ 1 & 1 & 1 & 1 \\ -1 & -1 & 1 & 1\end{array}\right]
\end{aligned}
$$

The solution coefficients determined by the initial condition are given by

$$
C=E^{-1}(P Q)_{0}
$$

$$
\begin{aligned}
C & =\left[\begin{array}{c}
0 \\
0 \\
0.5-i 6.892 \\
0.5+i 6.892
\end{array}\right] \\
& =\left[\begin{array}{l}
0 \\
0 \\
\psi \\
\psi^{*}
\end{array}\right]
\end{aligned}
$$

where

$$
\begin{aligned}
& \psi=0.5-i 6.892 \\
& \psi^{*}=0.5+i 6.892
\end{aligned}
$$

It follows that the time evolution vector is given by

$$
T=\left[\begin{array}{l}
0 \\
0 \\
\psi e^{i \omega}-t \\
\psi^{*} e^{-i \omega}-t
\end{array}\right]
$$

The solution vector $P Q$ is given by

$$
\begin{aligned}
& P Q=E T \\
& =\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]\left[\begin{array}{c}
0 \\
0 \\
4 e^{i \omega_{-} t} \\
\psi^{*} e^{-i \omega_{-} t}
\end{array}\right] \\
& =\left[\begin{array}{c}
i \omega_{-} \psi e^{i \omega_{-} t}-i \omega_{-} \psi^{*} e^{-i \omega_{-} t} \\
i \omega_{-} \psi e^{i \omega_{-} t}-i \omega_{-} \psi^{*} e^{-i \omega_{-} t} \\
\psi e^{i \omega_{-} t}+\psi^{*} e^{-i \omega_{-} t} \\
\psi e^{i \omega_{-} t}+\psi^{*} e^{-i \omega_{-} t}
\end{array}\right]
\end{aligned}
$$

tt is seen that

$$
p=p_{1}=p_{2} \quad q=q_{1}=q_{2}
$$

where

$$
\begin{aligned}
& p=i \omega_{-} \psi e^{i \omega_{-} t}-i \omega_{-} \psi^{*} e^{-i \omega_{-} t} \\
& q=\psi e^{i \omega_{-} t}+\psi^{*} e^{-i \omega_{-} t}
\end{aligned}
$$

Now

$$
\begin{aligned}
& \psi=\psi_{R}+i \psi_{I} \quad \psi^{*}=\psi_{R}-i \psi_{I} \\
& e^{i \omega_{I} t}=\cos \left(\omega_{t}\right)+i \sin \left(\omega_{t}\right) \\
& e^{-i \omega_{t} t}=\cos \left(\omega_{t}\right)-i \sin \left(\omega_{t}\right)
\end{aligned}
$$

so

$$
\begin{aligned}
P= & i \omega_{-}\left(\psi_{R}+i \psi_{I}\right)[\cos (\omega t)+i \sin (\omega t)] \\
& -i \omega_{-}\left(\psi_{R}-i \psi_{I}\right)[\cos (\omega t) \cdot i \sin (\omega t)] \\
= & i \omega_{-}\left[\psi_{R} \cos (\omega t)+i \psi_{I} \cos (\omega t)\right. \\
& \left.+i \psi_{R} \sin (\omega t)-\psi_{I} \sin ^{2}(\omega t)\right] \\
& -i \omega_{-}\left[\psi_{R} \cos (\omega t)-i \psi_{I} \cos (\omega t)\right. \\
& \left.-i \psi_{R} \sin (\omega t)-\psi_{I} \sin ^{2}(\omega t)\right]
\end{aligned}
$$

$$
\begin{aligned}
= & i \omega_{-}\left[i \psi_{I} \cos \left(\omega_{-} t\right)+i \psi_{R} \sin \left(\omega_{-} t\right)\right. \\
& \left.i \psi_{I} \cos \left(\omega_{-} t\right)+i \psi_{R} \sin \left(\omega_{-} t\right)\right] \\
=-2 \omega_{-} & {\left[\psi_{I} \cos \left(\omega_{-} t\right)+\psi_{R} \sin \left(\omega_{-} t\right)\right] }
\end{aligned}
$$

and

$$
\begin{aligned}
q= & \psi e^{i \omega_{-} t}+\psi^{*} e^{-i \omega_{-} t} \\
= & \left(\psi_{R}+i \psi_{I}\right)\left[\cos \left(\omega_{-} t\right)+i \sin \left(\omega_{-} t\right)\right] \\
& -\left(\psi_{R}-i \psi_{I}\right)\left[\cos \left(\omega_{-} t\right)-i \sin \left(\omega_{-} t\right)\right] \\
= & {\left[\psi_{R} \cos \left(\omega_{-} t\right)+i \psi_{I} \cos ^{\prime}\left(\omega_{-} t\right)\right.} \\
& \left.i \psi_{R} \sin ^{2}\left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right] \\
+ & {\left[\psi_{R} \cos \left(\omega_{-} t\right)-i \psi_{I} \cos ^{\prime}\left(\omega_{-} t\right)\right.} \\
& \left.-i \psi_{R} \sin ^{2}\left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right] \\
= & 2 \psi_{R} \cos \left(\omega_{-} t\right)-2 \psi_{I} \sin \left(\omega_{-} t\right) \\
= & 2\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right]
\end{aligned}
$$

so the solutions are

$$
P=-2 \omega_{-}\left[\psi_{I} \cos \left(\omega_{-} t\right)+\psi_{R} \sin \left(\omega_{-} t\right)\right]
$$

$$
q=2\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right]
$$

Now the Hamiltonian is given by

$$
\begin{aligned}
H(p, q) & =k(p)+u(q) \\
& =\frac{1}{2}\left(\frac{p_{1}^{2}}{m_{1}}+\frac{p_{2}^{2}}{m_{2}}\right)+ \\
& \frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1}^{2} \sigma_{2}^{2}+q_{2}^{2} \sigma_{1}^{2}-2 q_{2} q_{1} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

For this example

$$
\begin{aligned}
m_{1} & =m_{2}=1 \quad \sigma_{1}=\sigma_{2}=1 \\
H(p, q)= & \frac{1}{2}\left(p_{1}^{2}+p_{2}^{2}\right)+ \\
& \frac{1}{2\left(1-r^{2}\right)}\left(q_{1}^{2}+q_{2}^{2}-2 \gamma q_{1} q_{2}\right)
\end{aligned}
$$

For the obtained solution

$$
p=p_{1}=p_{2} \quad q=q_{1}=q_{2}
$$

$$
\begin{aligned}
H(p, q) & =p^{2}+\frac{1}{2\left(1-\gamma^{2}\right)} 2 q^{2}(1-\gamma) \\
& =p^{2}+q^{2} \frac{(1-\gamma)}{\left(1-\gamma^{2}\right)}
\end{aligned}
$$

Hamilton's equations are given by

$$
\begin{aligned}
& \dot{p}_{1}=\frac{-1}{1-\gamma^{2}}\left(q_{1}-\gamma q_{2}\right) \\
& \dot{p}_{2}=\frac{-1}{1-\gamma^{2}}\left(q_{2}-\gamma q_{1}\right) \\
& \dot{q}_{1}=p_{1} \\
& \dot{q}_{2}=p_{2}
\end{aligned}
$$

using $p=p_{1}=p_{2}$ and $q_{1}=q_{1}=q_{2}$

$$
\begin{aligned}
& \dot{p}=\frac{(1-\gamma)}{\left(1-\gamma^{2}\right)} q \\
& \dot{q}=p
\end{aligned}
$$

First that $p$ and $q$ are solutions to Hamilton's equations, recall

$$
\begin{aligned}
& P=-2 \omega_{-}\left[\psi_{I} \cos \left(\omega_{-} t\right)+\psi_{R} \sin \left(\omega_{-} t\right)\right] \\
& q=2\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
\dot{q} & =2\left[-\psi_{R} \omega_{-} \sin \left(\omega_{-} t\right)-\psi_{I} \omega_{-} \cos \left(\omega_{-} t\right)\right] \\
& =-2 \omega_{-}\left[\psi_{R} \sin \left(\omega_{-} t\right)+\psi_{I} \cos \left(\omega_{-} t\right)\right] \\
& =P
\end{aligned}
$$

and

$$
\begin{aligned}
\dot{p} & =-2 \omega_{-}\left[-\omega_{-} \psi_{I} \sin \left(\omega_{-} t\right)+\omega_{-} \psi_{R} \cos \left(\omega_{-} t\right)\right] \\
& =2 \omega_{-}^{2}\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right] \\
& =\omega_{-}^{2} q
\end{aligned}
$$

Now

$$
\begin{aligned}
\omega_{-}^{2} & =\alpha(1-\gamma) \\
& =\frac{(1-\gamma)}{\left(1-\gamma^{2}\right)}
\end{aligned}
$$

thus

$$
\dot{p}=\frac{(1-\gamma)}{\left(1-\gamma^{2}\right)} q
$$

verifying that $p$ and $q$ are solutions to Hamilton's equations.
Now the Hamiltonian is given by

$$
\begin{aligned}
H(p, q) & =p^{2}+q^{2} \frac{(1-\gamma)}{\left(1-\gamma^{2}\right)} \\
& =p^{2}+q^{2} \omega_{-}^{2}
\end{aligned}
$$

$$
\begin{aligned}
& P=-2 \omega_{-}\left[\psi_{I} \cos \left(\omega_{-} t\right)+\psi_{R} \sin \left(\omega_{-} t\right)\right] \\
& q=2\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
H & =\left\{2 \omega_{-}\left[\psi_{I} \cos \left(\omega_{-} t\right)+\psi_{R} \sin \left(\omega_{-} t\right)\right]\right\}^{2} \\
& +\omega_{-}^{2}\left\{2\left[\psi_{R} \cos \left(\omega_{-} t\right)-\psi_{I} \sin \left(\omega_{-} t\right)\right]\right\}^{2} \\
& =4 \omega_{-}^{2}\left\{\psi_{I}^{2} \cos ^{2}\left(\omega_{-} t\right)+\psi_{R}^{2} \sin ^{2}\left(\omega_{-} t\right)\right. \\
& +2 \psi_{I} \psi_{R} \cos \left(\omega_{-} t\right) \sin \left(\omega_{-} t\right)+\psi_{R}^{2} \cos ^{2}\left(\omega_{-} t\right) \\
& \left.+\psi_{I}^{2} \sin ^{2}\left(\omega_{-} t\right)-2 \psi_{R} \psi_{I} \cos \left(\omega_{I} t\right) \sin \left(\omega_{-} t\right)\right\} \\
& =4 \omega_{-}^{2}\left\{\psi_{I}^{2}\left[\cos ^{2}\left(\omega_{-} t\right)+\sin ^{2}\left(\omega_{-} t\right)\right]\right. \\
& \left.+\psi_{R}^{2}\left[\sin ^{2}\left(\omega_{-} t\right)+\cos ^{2}\left(\omega_{-} t\right)\right]\right\} \\
= & 4 \omega_{-}^{2}\left(\psi_{I}^{2}+\psi_{R}^{2}\right)
\end{aligned}
$$

which is a constat. Thus the Hamiltonian is conserved

$$
H=4 \omega_{-}^{2}\left(\psi_{I}^{2}+\psi_{I}^{2}\right)
$$

Next consider the initial condition

$$
(P Q)_{0}=\left[\begin{array}{r}
-1 \\
-2 \\
1 \\
-1
\end{array}\right]
$$

with parameters

$$
\gamma=0.2 \quad \alpha=\frac{1}{\left(1-0 . q^{2}\right)}=1.0417
$$

The eigenvalues are given by

$$
\begin{aligned}
\omega_{ \pm} & =\sqrt{\alpha(1 \pm \gamma)} \\
\lambda_{1}=i \omega_{+} \quad \lambda_{2} & =-i \omega_{+} \\
\lambda_{4} & =-i \omega_{-}
\end{aligned} \quad \lambda_{3}=i \omega_{-}
$$

where

$$
\omega_{+}=1.1181 \quad \omega_{-}=0.9128
$$

and the eigenvector matrix is given by

$$
E=\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]
$$

The solution coefficients determined by the initial condition are given by

$$
C=E^{-1}(P Q)_{0}
$$

soluing the equalion gives

$$
C=\left[\begin{array}{r}
0.5-i 0.2236 \\
0.5+i 0.2236 \\
i 0.8216 \\
-i 0.8216
\end{array}\right]
$$

Let

$$
\begin{aligned}
& \psi=0.5+i 0.2236=4 R+i 4 I \\
& \phi=i 0.8216=i \varphi I
\end{aligned}
$$

then

$$
C=\left[\begin{array}{l}
\psi \\
\psi^{*} \\
\phi \\
\varphi^{*}
\end{array}\right]=\left[\begin{array}{c}
\psi_{R}+i \psi_{I} \\
\psi_{R}-i \psi_{I} \\
i \varphi_{I} \\
i \varphi_{I}
\end{array}\right]
$$

The solution vector $P Q$ is given by

$$
\begin{aligned}
& P Q=E T \\
= & {\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]\left[\begin{array}{l}
\gamma e^{i \omega_{+} t} \\
\gamma^{*} e^{-i \omega_{+} t} \\
q e^{i \omega_{-} t} \\
\varphi^{*} e^{-i \omega_{-} t}
\end{array}\right] } \\
= & {\left[\begin{array}{c}
i \omega_{+} y e^{i \omega_{+} t}-i \omega_{+} \varphi^{*} e^{-i \omega_{+} t}+i \omega_{-} \varphi e^{i \omega_{-} t}-i \omega_{-} \varphi^{*} e^{-i \omega_{+}} \\
-i \omega_{+} y e^{i \omega_{+} t}+i \omega_{+} \psi^{*} e^{-i \omega_{+} t}+i \omega_{-} \varphi e^{i \omega_{-} t}-i \omega_{-} \varphi^{*} e^{-i \omega_{-} t} \\
y e^{i \omega_{+} t}+\psi^{*} e^{-i \omega_{+} t}+\phi e^{i \omega_{-} t}+\varphi^{*} e^{-i \omega_{-} t} \\
-4 e^{i \omega_{+} t}-\psi^{*} e^{-i \omega_{+} t}+\phi e^{i \omega_{-} t}+\varphi^{*} e^{-i \omega_{-} t}
\end{array}\right] }
\end{aligned}
$$

Now

$$
\begin{aligned}
P_{1} & =i \omega_{+} y e^{i \omega_{+} t}-i \omega_{+} 4^{*} e^{-i \omega_{+} t}+i \omega_{-} \varphi e^{i \omega_{-} t}-i \omega_{-} \varphi^{*} e^{-i \omega_{t}} \\
& =i \omega_{+}\left[\psi e^{i \omega_{+} t}-\psi^{*} e^{-i \omega_{+} t}\right]+i \omega_{-}\left[\varphi e^{i \omega_{-} t}\right. \\
& \left.-\varphi^{*} e^{-i \omega_{-} t}\right] \\
& =i \omega_{+}\left[\left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}-\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t}\right] \\
& +i \omega_{-}\left(i \varphi_{I} e^{i \omega_{-} t}+i \varphi_{I} e^{-i \omega_{-} t}\right) \\
& =i \omega_{+}\left[\psi_{R}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right)+i \psi_{I}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)\right] \\
& +\left(i \omega_{-} x\left(\varphi_{I}\right)\left(e^{i \omega_{-} t}+e^{i \omega_{-} t}\right)\right.
\end{aligned}
$$

recall that

$$
\begin{aligned}
& e^{i \omega_{+} t}-e^{-i \omega_{+} t}=\left[\cos \left(\omega_{+} t\right)+i \sin \left(\omega_{+} t\right)\right] \\
& -\left[\cos \left(-\omega_{+} t\right)+i \sin \left(-\omega_{+} t\right)\right] \\
& =\cos \left(\omega_{+} t\right)+i \sin \left(\omega_{+} t\right)-\cos \left(\omega_{+} t\right) \\
& +i \sin \left(\omega_{+} t\right)=2 i \sin \left(\omega_{+} t\right)
\end{aligned}
$$

and

$$
\begin{aligned}
& \quad e^{i \omega_{+} t}+e^{-i \omega_{+} t}=\left[\cos \left(\omega_{+} t\right)+i \sin \left(\omega_{+} t\right)\right] \\
& +\left[\cos \left(-\omega_{+} t\right)+i \sin \left(-\omega_{+} t\right)\right] \\
& =\cos \left(\omega_{+} t\right)+i \sin \left(\omega_{+} t\right)+\cos \left(\omega_{+} t\right) \\
& -i \sin \left(\omega_{+} t\right)=2 \cos \left(\omega_{+} t\right)
\end{aligned}
$$

so

$$
\begin{aligned}
& i \omega_{+}\left[\psi_{R}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right)+i \psi_{I}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)\right] \\
& +\left(i \omega_{-}\right)\left(i \varphi_{I}\right)\left(e^{i \omega_{-} t}+e^{i \omega_{-} t}\right) \\
& =i \omega_{+}\left[\psi_{R}(2 i) \sin \left(\omega_{+} t\right)+i \psi_{I}(2) \cos \left(\omega_{+} t\right)\right] \\
& +\left(i \omega_{-}\right)\left(i \varphi_{I}\right)(2) \cos \left(\omega_{-} t\right) \\
& =-2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right)
\end{aligned}
$$

Next

$$
\begin{aligned}
P_{2}= & -i \omega_{+} y e^{i \omega_{+} t}+i \omega_{+} 4^{*} e^{-i \omega_{+} t}+i \omega_{-} \varphi e^{i \omega_{-} t}-i \omega_{-} \varphi^{*} e^{-i \omega_{-} t} \\
= & i \omega_{+}\left[-y e^{i \omega_{+} t}+4^{*} e^{-i \omega_{+} t}\right]+i \omega_{-}\left[\varphi e^{i \omega_{-} t}\right. \\
& \left.-\varphi^{*} e^{-i \omega_{-} t}\right]
\end{aligned}
$$

$$
\begin{aligned}
= & i \omega_{+}\left[-\left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}+\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t}\right] \\
& +i \omega_{-}\left[i \varphi_{I} e^{i \omega_{-} t}+i \varphi_{I} e^{-i \omega_{-} t}\right] \\
= & i \omega_{+}\left[-\psi_{R}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right)-i \psi_{I}\left(e^{i \omega_{+} t}\right.\right. \\
& \left.\left.+e^{-i \omega_{+} t}\right)+i \omega_{-}\left(i \varphi_{I}\right)\left(e^{i \omega_{-} t}+e^{-i \omega_{-} t}\right)\right] \\
= & i \omega_{+}\left[-2 i \psi_{R} \sin \left(\omega_{+} t\right)-2 i \psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& +i \omega_{-}\left(i \varphi_{I}\right)\left[2 \cos \left(\omega_{-} t\right)\right] \\
= & 2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right)
\end{aligned}
$$

And

$$
\begin{aligned}
q_{1}= & y e^{i \omega_{+} t}+\psi^{*} e^{-i \omega_{+} t}+\phi e^{i \omega_{-} t}+\varphi^{*} e^{-i \omega_{-} t} \\
= & \left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}+\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t} \\
& +i \varphi_{I} e^{i \omega_{-} t}-i \varphi_{I} e^{-i \omega_{-} t} \\
= & \psi_{R}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)+i \psi_{I}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right) \\
& +i \varphi_{I}\left(e^{i \omega_{-} t}-e^{-i \omega_{-} t}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & \psi_{R}(2) \cos \left(\omega_{+} t\right)+i \psi_{i}(2 i) \sin \left(\omega_{+} t\right) \\
& +i \varphi_{I}(2 i) \sin \left(\omega_{-} t\right) \\
= & 2 \psi_{R} \cos \left(\omega_{+} t\right)-2 \psi_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right)
\end{aligned}
$$

And finally

$$
\begin{aligned}
\varphi_{2}= & -4 e^{i \omega_{+} t}-\psi^{*} e^{-i \omega_{+} t}+\phi e^{i \omega_{-} t}+\varphi^{*} e^{-i \omega_{-} t} \\
= & -\left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}-\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t} \\
& i \varphi_{I} e^{i \omega_{-} t}-i \varphi_{I} e^{-i \omega_{-} t} \\
= & -\psi_{R}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)-i \psi_{I}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right) \\
& +i \varphi_{I}\left(e^{i \omega_{-} t}-e^{-i \omega_{-} t}\right) \\
= & -\psi_{R}(2) \cos \left(\omega_{+} t\right)-i \psi_{i}(2 i) \sin \left(\omega_{+} t\right) \\
& +i \varphi_{I}(2 i) \sin \left(\omega_{-} t\right) \\
= & -2 \psi_{R} \cos \left(\omega_{+} t\right)+2 \psi_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right)
\end{aligned}
$$

In summary

$$
\begin{aligned}
P_{1}= & -2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right) \\
P_{2}= & 2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right) \\
q_{1}= & 2 \psi_{R} \cos \left(\omega_{+} t\right)-2 \psi_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right) \\
q_{2}= & -2 \psi_{R} \cos \left(\omega_{+} t\right)+2 \psi_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right)
\end{aligned}
$$

Next Consider the Initial Condition

$$
(P Q)_{0}=\left[\begin{array}{c}
1 \\
-1 \\
1 \\
-1
\end{array}\right]
$$

with parameters

$$
\gamma=0,9 \quad \alpha=\frac{1}{\left(1-0,9^{2}\right)}=5,2632
$$

The eigenvalues are given by

$$
\begin{aligned}
\omega_{ \pm} & =\sqrt{\alpha(1 \pm \gamma)} \\
\lambda_{1}=i \omega_{+} \quad \lambda_{2} & =-i \omega_{+} \\
\lambda_{4} & =-i \omega_{-}
\end{aligned} \quad \lambda_{3}=i \omega_{-}
$$

where

$$
\omega_{+}=3.1623 \quad \omega_{-}=0.7255
$$

and the eigen vector matrix is given by

$$
E=\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]
$$

The solution coefficients determined by the initial condition are given by

$$
C=E^{-1}(P Q)_{0}
$$

solving the equalion gives

$$
C=\left[\begin{array}{c}
0.5-i 0.1581 \\
0.5+i 0.1581 \\
0 \\
0
\end{array}\right]
$$

Let

$$
\psi=0.5+i 0.1581=\psi_{R}+i 4 I
$$

The solution vector $P Q$ is given by

$$
\begin{aligned}
& P Q=E T \\
= & {\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]\left[\begin{array}{c}
\psi e^{i \omega_{+} t} \\
\psi^{*} e^{-i \omega_{+} t} \\
0 \\
0
\end{array}\right] } \\
= & {\left[\begin{array}{l}
i \omega_{+} \psi e^{i \omega_{+} t}-i \omega_{+} \psi^{*} e^{-i \omega_{+} t} \\
-i \omega_{+} \psi e^{i \omega_{+} t}+i \omega_{+} \psi^{*} e^{-i \omega_{+} t} \\
\psi e^{i \omega_{+} t}+\psi^{*} e^{-i \omega_{+} t} \\
-\psi e^{i \omega_{+} t}-\psi^{*} e^{-i \omega_{+} t}
\end{array}\right] }
\end{aligned}
$$

Clearly

$$
p=p_{1}=-p_{2} \quad q=q_{1}=-q_{2}
$$

Now

$$
\begin{aligned}
P= & i \omega_{+} \psi e^{i \omega_{+} t}-i \omega_{+} \psi^{*} e^{-i \omega_{+} t} \\
= & i \omega_{+}\left[\left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}-\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t}\right] \\
= & i \omega_{+}\left[\psi_{R}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right)\right. \\
& \left.+i \psi_{I}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)\right] \\
= & i \omega_{+}\left[\psi_{R}(2 i) \sin \left(\omega_{+} t\right)+i \psi_{I} 2 \cos \left(\omega_{+} t\right)\right] \\
= & 2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
q= & 4 e^{i \omega_{+} t}+\psi^{*} e^{-i \omega_{+} t} \\
= & \left(\psi_{R}+i \psi_{I}\right) e^{i \omega_{+} t}+\left(\psi_{R}-i \psi_{I}\right) e^{-i \omega_{+} t} \\
= & \psi_{R}\left(e^{i \omega_{+} t}+e^{-i \omega_{+} t}\right)+i \psi_{I}\left(e^{i \omega_{+} t}-e^{-i \omega_{+} t}\right) \\
= & \psi_{R}(2) \cos \left(\omega_{+} t\right)+i \psi_{I}(2 i) \sin \left(\omega_{+} t\right) \\
= & 2\left[\psi_{R} \cos \left(\omega_{+} t\right)-\psi_{I} \sin \left(\omega_{+} t\right)\right]
\end{aligned}
$$

In summary

$$
\begin{gathered}
P=P_{1}=-P_{2} \quad q=q_{1}=-q_{2} \\
P=\frac{2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right]}{q=2\left[\psi_{R} \cos \left(\omega_{+} t\right)-\psi_{I} \sin \left(\omega_{+} t\right)\right]} \\
q=
\end{gathered}
$$

Finally Consider the Example

$$
(P Q)_{0}=\left[\begin{array}{r}
1 \\
-1 \\
1 \\
-1
\end{array}\right]
$$

with parameters

$$
\gamma=0,0 \quad \alpha=1,0
$$

The eigenvalues are given by

$$
\begin{gathered}
\omega_{ \pm}=1 \\
\lambda_{1}=i \quad \lambda_{2}=-i \quad \lambda_{3}=i \quad \lambda_{4}=-i \\
{\left[\begin{array}{cccc}
i & -i & i & -i \\
-i & i & i & -i \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]}
\end{gathered}
$$

The solution coefficients determined by the initial condition are given by

$$
C=E^{-1}(P Q)_{0}
$$

solving the equation gives

$$
C=\left[\begin{array}{c}
0.5-i 0.5 \\
0.5+i 0.5 \\
0 \\
0
\end{array}\right]
$$

Let

$$
\psi=0.5+i 0.5=\psi_{R}+i 4 I
$$

This solution has a form previously encountered

$$
p=p_{1}=-p_{2} \quad q=q_{1}=-q_{2}
$$

$P=-2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right]$
$q=2\left[4_{R} \cos \left(\omega_{+} t\right)-4_{I} \sin \left(\omega_{+} t\right)\right]$

## Summary of Analytic Solutions to Bivariate Normal tlamiltons Equations

The Hamiltonian for the Birariate Normal distribution is given by

$$
\begin{aligned}
H(p, q) & =K(p)+u(q) \\
& =\frac{1}{2}\left(\frac{p_{1}^{2}}{m_{1}}+\frac{p_{2}^{2}}{m_{2}}\right)+ \\
& \frac{1}{2 \sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(q_{1}^{2} \sigma_{2}^{2}+q_{2}^{2} \sigma_{1}^{2}-2 q_{2} q_{1} \gamma \sigma_{1} \sigma_{2}\right)
\end{aligned}
$$

Here an analysis of the solutions to Hamilton's equations for the Bivariate Normal Hamiltonian are discussed. Analytic solutions are determined and compared with solutions obtained by numerical integration. The purpose of the analysis is to determine the accuracy of the numerical integration method and determing the behavior of solutions as correlation
is varied, so it is assumed that

$$
m_{1}=m_{2}=1 \quad \sigma_{1}=\sigma_{2}=1
$$

also let

$$
\alpha=\frac{1}{1-\gamma^{2}}
$$

Then Hamilton's equations becomes

$$
\begin{array}{ll}
\dot{p}_{1}=-\alpha\left(q_{1}-\gamma q_{2}\right) & \dot{q}_{1}=p_{1} \\
\dot{p}_{2}=-\alpha\left(q_{2}-\gamma q_{1}\right) & \dot{q}_{2}=p_{2}
\end{array}
$$

in matrix form

$$
\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right]=\left[\begin{array}{cccc}
0 & 0 & -\alpha & \alpha \gamma \\
0 & 0 & \alpha \gamma & -\alpha \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{array}\right]\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right]
$$

where the Hamiltonian matrix
is given by

$$
H=\left[\begin{array}{cccc}
0 & 0 & -\alpha & \alpha \gamma \\
0 & 0 & \alpha \gamma & -\alpha \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{array}\right]
$$

The solution is,

$$
\left[\begin{array}{l}
p_{1} \\
p_{2} \\
q_{1} \\
q_{2}
\end{array}\right]=\sum_{i=1}^{4} c_{i} E^{i} e^{-\lambda_{i} t}
$$

where the $c_{i}$ are constants, the $E_{i}$ are eigen vectors, and $\lambda_{i}$ the eigen values of the matrix $H$. The matrix of eigenvectors is given by

$$
E=\left[\begin{array}{cccc}
i \omega_{+} & -i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
-i \omega_{+} & i \omega_{+} & i \omega_{-} & -i \omega_{-} \\
1 & 1 & 1 & 1 \\
-1 & -1 & 1 & 1
\end{array}\right]
$$

where

$$
\omega_{ \pm}=\sqrt{\alpha(1 \pm \gamma)}
$$

the eigenvalues are given by

$$
\begin{gathered}
\lambda_{1}=i \omega_{+} \lambda_{2}=-i \omega_{+} \quad \lambda_{3}=i \omega_{-} \\
\lambda_{4}=-i \omega_{-}
\end{gathered}
$$

The constants $C_{i}$ are determined by soluing the equation

$$
C=E^{-1}\left(P^{\circ} Q^{\circ}\right)
$$

Where $E^{-1}$ is the inverse of the materix of eigenvectors and (POQO) is a column vector containg the
intial values of $p$ and $q$. It is seen that the solution consits of a linear combination of two pairs of waves with frequencies

$$
\omega_{ \pm}=\sqrt{\alpha(1 \pm \gamma)}
$$

the fast pair of waves have frequency $w_{+}$and the slow pair have frequency $\omega_{\text {- }}$. If it is assumed that ( $P^{\circ} Q^{\circ}$ ) is real the column vector $C$ will have the form

$$
C=\left[\begin{array}{l}
\psi \\
\psi^{*} \\
\varphi \\
\varphi^{*}
\end{array}\right]
$$

where $\varphi^{*}$ and $\varphi^{*}$ are the complex conjugates of 4 and $\varphi$ respectively.

Example $r=0$

For $\gamma=0$ the fast and slow frequencies are equal.

$$
\omega_{ \pm}=1
$$

and the eigenvalues are degenerate

$$
\lambda_{i}= \pm i
$$

The eigenvectors are given byl

$$
E=\left[\begin{array}{cccc}i & -i & i & -i \\ -i & i & i & -i \\ 1 & 1 & 1 & 1 \\ -1 & -1 & 1 & 1\end{array}\right]
$$

An example numerical integration is shown in the following plots where it is seen that for the intral condition

$$
\begin{aligned}
& \left(P^{0} Q^{0}\right)=\left[\begin{array}{c}
1 \\
-1 \\
1 \\
-1
\end{array}\right] \\
& C=\left[\begin{array}{c}
1 / 2-1 / 2 i \\
1 / 2+1 / 2 i \\
0 \\
0
\end{array}\right]
\end{aligned}
$$

50

$$
\begin{array}{ll}
\psi_{R}=1 / 2 & \psi_{I}=1 / 2 \\
\varphi_{R}=0 & \varphi_{I}=0
\end{array}
$$

The solution is

$$
\begin{gathered}
p_{1}(t)=-p_{2}(t)=p(t) \\
q_{1}(t)=-q_{2}(t)=q(t) \\
p(t)=\frac{2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right]}{q(t)=2\left[\psi_{R} \cos \left(\omega_{+} t\right)-\psi_{I} \sin \left(\omega_{+} t\right)\right]}
\end{gathered}
$$

The position and momentum as functions of time are shown in the following plot
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-138.jpg?height=662&width=799&top_left_y=364&top_left_x=423)

Conservation of energy is illustrated in the following plot where $H(t) k(t)$ and $u(t)$ are plotted.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-138.jpg?height=589&width=798&top_left_y=1338&top_left_x=390)

The following plots show the results of an integration of Hamitons equations using the same distribution parameters and initial condition. The integration uses a stepsize of $\Delta t=0.01$ and is run for 1256 steps. The first two plots show position and momentum as functions of time and the final plot the energy as a function of time is Conserved.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-139.jpg?height=584&width=799&top_left_y=1160&top_left_x=423)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-140.jpg?height=575&width=795&top_left_y=137&top_left_x=390)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-140.jpg?height=591&width=795&top_left_y=798&top_left_x=395)

By inspection it is seen that the conalytic solution and the solution obtained by numerical are comparable. The following plots confirm this where the
difference between the solutions is shown. It is interesting that the integration error increases in time while the total evergy is maintained. This is likely caused by phase errors so should eventually reach a maximum.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-141.jpg?height=575&width=803&top_left_y=725&top_left_x=382)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-141.jpg?height=567&width=800&top_left_y=1322&top_left_x=388)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-142.jpg?height=570&width=799&top_left_y=128&top_left_x=382)

Example $r=0.9$

For $\gamma=0,9$ the fast and slow frequencies are given by

$$
\begin{aligned}
& \omega_{+}=3.1623 \\
& \omega_{-}=0.7255
\end{aligned}
$$

The eigen values are given by

$$
\begin{array}{ll}
\lambda_{1}=i 3.1623 & \lambda_{2}=-i 3.1623 \\
\lambda_{3}=i 0.7255 & \lambda_{4}=-i 0.7255
\end{array}
$$

The eigenvectors are given by

$$
E=\left[\begin{array}{cccc}i 3.1623 & -i 3.1623 & i 0.7255 & -i 0.7255 \\ -i 3.1623 & i 3.1623 & i 0.7255 & -i 0.7255 \\ 1 & 1 & 1 & 1 \\ -1 & -1 & 1 & 1\end{array}\right]
$$

An example numerical integration is shown in the following plots where it is seen that for the intral condition

$$
\begin{aligned}
& \left(P^{0} Q^{0}\right)=\left[\begin{array}{c}
-1 \\
-2 \\
1 \\
-1
\end{array}\right] \\
& C=\left[\begin{array}{c}
0.5-i 0.7906 \\
0.5+i 0.7906 \\
i 1.0338 \\
-i 1.0338
\end{array}\right]
\end{aligned}
$$

50

$$
\begin{array}{ll}
\psi_{R}=0.5 & \psi_{I}=0,7906 \\
\varphi_{R}=0 & \varphi_{I}=1.0338
\end{array}
$$

The solution is

$$
\begin{aligned}
P_{1}= & -2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right) \\
P_{2}= & 2 \omega_{+}\left[\psi_{R} \sin \left(\omega_{+} t\right)+\psi_{I} \cos \left(\omega_{+} t\right)\right] \\
& -2 \omega_{-} \varphi_{I} \cos \left(\omega_{-} t\right)
\end{aligned}
$$

$$
\begin{aligned}
q_{1}= & 2 u_{R} \cos \left(\omega_{+} t\right)-2 u_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right) \\
q_{2}= & -2 u_{R} \cos \left(\omega_{+} t\right)+2 u_{i} \sin \left(\omega_{+} t\right) \\
& -2 \varphi_{I} \sin \left(\omega_{-} t\right)
\end{aligned}
$$

The position and momentum as functions of time are shown in the followin plot
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-145.jpg?height=666&width=808&top_left_y=957&top_left_x=382)

Conservation of energy is illustrated in the following plot where $H(t) K(t)$ and $u(t)$ are plotted.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-146.jpg?height=531&width=787&top_left_y=153&top_left_x=388)

The following plots show the results of an integration of Hamiltons equations using the same distribution parameters and initial condition. The integration uses a stepsize of $\Delta t=0.01$ and is run for 1732 steps. The first two plots show position and momentum as functions of time and the final plot the energy as a function of time is Conserved.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-147.jpg?height=572&width=787&top_left_y=116&top_left_x=437)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-147.jpg?height=572&width=789&top_left_y=759&top_left_x=437)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-147.jpg?height=583&width=791&top_left_y=1378&top_left_x=439)

By inspection it is seen that the cinalytic solution and the solution obtained by numerical are comparable. The following plots confirm this where the difference between the solutions is shown. In the previous example the integration error increase in time while conserving energy. This is not the case for this example where the integration error is otable while conserving energy.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-148.jpg?height=579&width=803&top_left_y=1237&top_left_x=378)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-149.jpg?height=571&width=797&top_left_y=145&top_left_x=411)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-149.jpg?height=564&width=789&top_left_y=785&top_left_x=419)

## Hamittonian Monte Carlo Simulation of Bivariate-Normal Distribution

Here the results of a simulation which generated Bivariate normal random variables using Hemittonian Monte carlo are discribed. The parameters used to specify the target distribution are given by

$$
\sigma_{1}=\sigma_{2}=1 \quad \gamma=0.90
$$

The parameters desoribing the Kinetic Energy are

$$
m_{1}=m_{2}=1
$$

The integration time step used in soluing Hamitton's equations is

$$
\Delta t=0.01
$$

The amount of time themitton's equations are integrated is a uniform random variable with maximum and minimum values of 0 and $t_{\text {max }}$ where

$$
t_{\max }=\frac{\partial \pi}{\partial(1+\gamma)}
$$

and

$$
\alpha=\frac{1}{1-\gamma^{2}}
$$

The integration time is assumet random to present simulations from oscillating between periodic values.
The intial condition is

$$
q_{0}=(1,-1)
$$

These results are later compared with simulations for the same target distributions using component wise Metroplis Hastengs and eiblys sampling.
The target distribution is shown in the following plot

Bivariate Normal Distribution: $\gamma=0.90, \sigma_{u}=1.00, \sigma_{v}=1.00$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-152.jpg?height=896&width=958&top_left_y=197&top_left_x=330)

The results of a 10,000 sample simulation are presented in the following plots. The first plot compares a histogram of the position samples with the target distribution. The sample accestance is $100 \%$ and compares well with the target distribution
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-153.jpg?height=825&width=932&top_left_y=56&top_left_x=362)

The next plots compare histograms of the position samples with the target marginal distributions

HMC Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-153.jpg?height=664&width=973&top_left_y=1279&top_left_x=346)

HMC Normal $q_{2}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-154.jpg?height=698&width=1033&top_left_y=133&top_left_x=324)

Next slices of position time series for samples between 9000 and 9500 are shown. The series exhibit low autocorrelation, noticiable by the frequency in change of direction. Also, note the high correlation since the targed distribution has $\gamma=0.9$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-154.jpg?height=490&width=1164&top_left_y=1481&top_left_x=211)

HMC Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-155.jpg?height=434&width=1164&top_left_y=173&top_left_x=217)

Convergence of the first and second moments to the target distribution values are shown in the following plots. The first show convergence of the position means to the target means of zero. within a few thausand samples the sample means are close. to the target means.
The second two plots show convergence of the position sample standard deviations to the target distribution values of 1 . The convergence for the standard deviations is slower than for
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-156.jpg?height=708&width=1029&top_left_y=137&top_left_x=312)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-156.jpg?height=688&width=1001&top_left_y=951&top_left_x=326)

## the means. More samples will be required to approach an acceplable value.

HMC Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-157.jpg?height=614&width=960&top_left_y=461&top_left_x=300)

HMC Bivariate Normal $q_{2}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-157.jpg?height=599&width=942&top_left_y=1243&top_left_x=310)

The neyt plot shows the convergence of the sample position correlation coefficient to the target value $\gamma=0.9$ The sample value rapidly converges to the target distribution value, closek approaching the value within a few hundred steps
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-158.jpg?height=771&width=1166&top_left_y=725&top_left_x=197)

The final plots show the autocorrelation of position samples as a function of tim lag. The samples very
contrast to methods discussed later which produce samples withe autocorrelation since they are Markou chain based.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-159.jpg?height=684&width=998&top_left_y=423&top_left_x=294)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-159.jpg?height=674&width=996&top_left_y=1209&top_left_x=298)

## Gibbs sampling of the Bioariate Normal Distribution

For a Bivariate distribution, $p(x, y)$, if both conditional didributions $p(x \mid y)$ and $p(y \mid x)$ are sampalable the Gibbs sampling algorithm can be used to generate a Markou chain of samples. The algorithm is intialized by choosing intial values for $x$ and $y$ denoted by $X_{0}$ and $Y 0$. The following steps are executed in a loop to generate samples at time stee

$$
\begin{aligned}
& x_{t} \sim p\left(x \mid y_{t-1}\right) \\
& y_{t} \sim p\left(y \mid x_{t}\right)
\end{aligned}
$$

After $N$ stops the Markoo chain

$$
\left(x_{0}, y_{0}\right),\left(x_{1}, y_{1}\right),\left(x_{2}, y_{2}\right), \ldots,\left(x_{N}, y_{N}\right)
$$

is produced.
For the Bivariat Normal distribution
the conditional distributions are given by

$$
\begin{aligned}
& P(x \mid y)=\frac{1}{\sigma_{1} \partial \pi\left(1-\gamma^{2}\right)} \exp \{ \\
& \left.\frac{-1}{2 \sigma_{1}^{2}\left(1-\gamma^{2}\right)}\left[x-\left(\mu_{1}+\frac{\gamma \sigma_{1}}{\sigma_{2}}\left(y-\mu_{2}\right)\right)\right]^{2}\right\} \\
& P(y \mid x)=\frac{1}{\sigma_{2} \partial \pi\left(1-\gamma^{2}\right)} \exp \{ \\
& \frac{-1}{2 \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left[y-\left(\mu_{2}+\frac{\gamma \sigma_{2}}{\sigma_{1}}\left(x-\mu_{1}\right)\right]^{2}\right\}
\end{aligned}
$$

## Simulation of Bivarite-Normal Distribution using Gibbs Sampling

The target distribution is shown in the following plot. The following parameterization is assumed

$$
\begin{gathered}
\sigma_{1}=\sigma_{2}=r \quad \mu_{1}=\mu_{2}=\partial \\
\gamma=0.90
\end{gathered}
$$

![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-162.jpg?height=862&width=872&top_left_y=1047&top_left_x=376)

The results of a 10,000 sample simulation are presented in the following plots. The first plot compares a histogram of the position samples with the target distribution. The sample acceptance is $100 \%$ since Gibbs sampling accepts all proposal samples. The simulation results compare well with the target distribution.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-163.jpg?height=908&width=1017&top_left_y=967&top_left_x=310)

The next plots compare histograms of the position samples with the target marginal distributions
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-164.jpg?height=746&width=1010&top_left_y=419&top_left_x=292)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-164.jpg?height=728&width=988&top_left_y=1211&top_left_x=308)

The fit of the histograms to the target marginal distributions is notricably better tran the results obtained with Hamiltonian Monte Carlo.
Next slices of position time series for samples between 9000 and 9500 are shown. Autocorrelation is visible when compared to the Hamiltonian Monte Carlo results. Drrection changes are less frequent.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-165.jpg?height=481&width=1176&top_left_y=918&top_left_x=183)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-165.jpg?height=487&width=1166&top_left_y=1442&top_left_x=199)

Convergence of the first and second moments to the target distribution values are shown in the following plots. The first show convergence of the position means to the target means of zero. within a few thousand samples the sample means are close. to the target means.
The second two plots show convergence of the position sample standard deviations to the target distribution values of 1 . The convergence for the standard deviations occurs on a time scale similar to trat seen for the mean.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-167.jpg?height=858&width=1212&top_left_y=116&top_left_x=199)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-167.jpg?height=850&width=1210&top_left_y=1033&top_left_x=203)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-168.jpg?height=857&width=1174&top_left_y=147&top_left_x=211)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-168.jpg?height=827&width=1140&top_left_y=1086&top_left_x=243)

The neyt plot shows the convergence of the sample position correlation coefficient to the target value $\gamma=0.9$ The sample value rapidly converges to the target distribution value, closely approaching the value within hundreds of steps
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-169.jpg?height=725&width=1065&top_left_y=741&top_left_x=253)

The final plots show the autocorrelation of position samples as a function of tm lag. These results are in contrast with those obtained for the HMC simulations which rapidly

## decorrelate. Here significant autocorrelation persists for tons of samples.

Gibbs Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-170.jpg?height=628&width=940&top_left_y=443&top_left_x=362)

Gibbs Bivariate Normal $q_{2}: \gamma=0.9$, nsample $=10000$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-170.jpg?height=623&width=930&top_left_y=1217&top_left_x=378)

## Component-wise Metropolis-Hastings

sampling of Bivarite Normal Distribution

Previous investications of Metropolis Hastings sampling considered only univariate targe distributions The algorithm can easily be extended to multivariate distributions. This extension is called Component. wise Metropolis Hastings sampling. Consider an n-dimensional random vector

$$
x=\left(x_{1}, x_{2}, \ldots, x_{n}\right)
$$

with density $f(x)$. componet-wise Metropolis Hastings produces samples for components one at a time for each tume step. As each component sample is senerated it is used in subsequent component samples for the time step. The proceedure is similar to that used by Gibbs sampling.

Component-wise Metropolis Aastings also requires specification of target and proposal distributions. Let $P(x)$ denote the target destribution. The proposal distribution is assumed to be univariate and is denoted by $q\left(y, x_{i}\right)$ where $x_{i}$ denotes the c'th component at the previous time step and $y$ the proposal sample. Firthure let $x_{i}^{t}$ denote the sample of the i'th comoponent at time $t$. The steps peformed can be summarized as follows

* For each time step denoted by $t$ * For each component dended by $i$
* Eenerate a proposal sample using the proposal distribution

$$
y \sim q\left(y, x_{t}^{t-1}\right)
$$

* Compute the proposal sample
acceptance probability as follows

$$
\begin{aligned}
& \text { accept }=\text { uniform }(0,1) \\
& p y=p\left(y, x_{j \neq i}^{t} \mid x_{j \neq i}^{t-1}\right) \\
& p x=p\left(x_{j}^{t-1}, x_{j \neq i}^{t} \mid x_{j \neq i}^{t-1}\right) \\
& \alpha=\frac{p y}{p x} \frac{q\left(y, x_{j}^{t-1}\right)}{q\left(x_{j}^{t-1}, y\right)}
\end{aligned}
$$

where $x_{j \neq i}^{t} \mid x_{j \neq i}^{t-1}$ indicates that the most recent samples available are used for the other components

* In the final sters the acceptance condition is evaluated. If the proposat is accepted $y$ becomes the curvent sample if it is not accepled the previous sample becomes the current sample

$$
\begin{gathered}
\text { if accept }<2 \\
x_{i}^{t}=y \\
\text { else } \\
x_{i}^{t}=x_{i}^{t-1}
\end{gathered}
$$

Component-Wise Metropolis Hastings reduces to Cibbs Sampling if the target distribution component contional distributions are used as targets for each component and $\alpha=1$.
The example investigated uses a Normal proposal distribution,

$$
q(x, y)=\frac{1}{\sqrt{2 \pi \sigma^{2}}} e^{-(x-y)^{2} / 2 \sigma^{2}}
$$

The target distribution is the previously discussed buariate normal distribution. The parameter $\sigma$ is in the proposal distribution is the stepsize which is adjusted to achive a desired acceptance.

## Simulation of Bivariate-Normal Distribution using Component. wise Metropolis Hastings

The target distribution is shown in the following plot. The following parameterization is assumed

$$
\begin{gathered}
\sigma_{1}=\sigma_{2}=1 \quad \mu_{1}=\mu_{2}=\partial \\
\gamma=0.90
\end{gathered}
$$

![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-175.jpg?height=924&width=938&top_left_y=1017&top_left_x=312)

The results of a 10,000 sample simulation are presented in the following plots. The performance of a Metropolis-Hastings simulation of this size is significanty degraded as compared to tlamittanian Monte Carls and Eilbs sampling. To achive a similar level performance of Metropolis. Hastings would require 5 to 10 times the samples.
In this simulation the proposal distribution stepsize is assumed to be 0.25 to obtain an acceptance percentage of 809 . The first plot compares a histogram of samples with the target distribution. The results dotained are inferior to those of the other methods but are acceptable. In practice a larger number of samples would be used
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-177.jpg?height=936&width=1053&top_left_y=104&top_left_x=276)

The next plots compare histograms of the position samples with the target marginal distributions. The results are acceptable but more samples are required.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-178.jpg?height=828&width=1093&top_left_y=98&top_left_x=264)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-178.jpg?height=812&width=1067&top_left_y=1035&top_left_x=266)

Next slices of position time series for samples between 9000 and 9500 are shown. Autocorrelation is visible when compared to the Hamiltonian Monte Carlo results. Drection changes are less frequent and the rejected samples are apparent giving the series a blocky 100 k .

MH Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=82 \%$

![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-179.jpg?height=439&width=1192&top_left_y=945&top_left_x=200)
MH Bivariate Normal $q_{2}: \gamma=0.9$, nsample $=10000$, accepted $=82 \%$

MH Bivariate Normal $q_{2}: \gamma=0.9$, nsample $=10000$, accepted $=82 \%$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-179.jpg?height=412&width=1182&top_left_y=1505&top_left_x=208)

Convergence of the first and second moments to the target distribution values are shown in the following plots. The first show convergence of the mean. The tendency is the right direction but more samples are required to obtain a level of convergence seen in the other methods.

The second two plots show convergence of the position sample standard deviations to the target distribution values of 1 . The convergence for the standard deviations occurs on a time scale about an order of magnitude slower than seen for the other methods.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-181.jpg?height=828&width=1134&top_left_y=98&top_left_x=227)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-181.jpg?height=800&width=1138&top_left_y=1047&top_left_x=229)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-182.jpg?height=797&width=1136&top_left_y=102&top_left_x=213)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-182.jpg?height=837&width=1152&top_left_y=997&top_left_x=205)

The next plot shows the convergence of the sample position correlation coefficient to the target value $\gamma=0.9$ The sample correlation is near the target correlation after thousands of samples. This is about an order of magnitude slower than seen in the other methods
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-183.jpg?height=830&width=1180&top_left_y=892&top_left_x=195)

The final plots show the autocorrelation of position samples as a function of timelag. These results are by for the worst obtained. After 25 samples there is still significant correlation in the timeseries. To obtain better results a larger number of samples is required and methods such as Burn-in and thinning are required to improve the results
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-184.jpg?height=845&width=1162&top_left_y=1068&top_left_x=201)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-185.jpg?height=848&width=1168&top_left_y=211&top_left_x=209)

## Comparison of Performance of simulation methods

This section will perform a direct comparison of the simulation of Bivariate-Normal random variables where the target Bivariate-Normal distribution has the following parameters

$$
\begin{gathered}
\sigma_{1}=\sigma_{2}=1 \quad \mu_{1}=\mu_{2}=0 \\
r=0.9 .
\end{gathered}
$$

The target distribution with these parameters is given by
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-186.jpg?height=662&width=674&top_left_y=1291&top_left_x=477)

Metropolis Hastings samplers require processing of the result by Burn-in, discard some portion of the begining samples, and thining, only acepting
samples that satisfy $n \% \mathrm{~m}=0$, where $n$ is the sample number and $m$ is an integer. Both of these proceedures could reduce the number of samples by more than an order of magnitude but the do increase the rate of convergence of moments and reduce autocorrelation with in the samples. Here this processing has not beon performed to highlight the better innate performance of Gibbs and thmittonian Monte carlo samplers.
The first plots compare the histograms computed from the samples for each method with the target distribution. Gibbs and HMC give similar results. An
assymetry in the MH samples is apporent and not present in the eibbs and HMC samples.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-188.jpg?height=597&width=676&top_left_y=415&top_left_x=70)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-188.jpg?height=591&width=666&top_left_y=421&top_left_x=824)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-188.jpg?height=620&width=696&top_left_y=1116&top_left_x=437)

The next plots compore the $q_{1}$ marginal distributions for each method with histograms computed from the samples. Gibbs samples are slightly better performing than HMC samples and both of these methods are superior to the MH samples which exhibit the previously noted asymmetry.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-189.jpg?height=533&width=708&top_left_y=751&top_left_x=68)

Gibbs Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-189.jpg?height=486&width=712&top_left_y=798&top_left_x=826)

MH Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=82 \%$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-189.jpg?height=519&width=759&top_left_y=1428&top_left_x=445)

The next plots show time series for $q_{1}$ samples between sample number 9000 to 9500 . It is desirable for random number generators to
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-190.jpg?height=492&width=1186&top_left_y=405&top_left_x=197)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-190.jpg?height=486&width=1168&top_left_y=937&top_left_x=211)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-190.jpg?height=484&width=1170&top_left_y=1477&top_left_x=213)
produce samples that are uncorrelated with previous samples. From inspection of these plots HMC is superior in this regard. Since the samples frequently crange direction. The Gibbs samples are clearly better than the MH samples but in both auto correlation in the samples is apparent from the persistence in the direction of subsequent samples.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-191.jpg?height=527&width=1497&top_left_y=858&top_left_x=57)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-191.jpg?height=576&width=793&top_left_y=1402&top_left_x=380)

The next plots show the autocorrelation as a function of lag. The superior performance of HMC in this regard is obvious. The autocorrelation quickly goes to zero. The Gibbs samples require 20 samples to become uncomrelated and MH samples hundreds of samples are required. Since Gibbs and MH samplers are Markou Chain based this result is expected.

HMC Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=100 \%, t_{\text {max }}=5.77$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-192.jpg?height=487&width=680&top_left_y=894&top_left_x=840)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-192.jpg?height=503&width=710&top_left_y=1438&top_left_x=455)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-193.jpg?height=466&width=1476&top_left_y=149&top_left_x=68)

MH Bivariate Normal $q_{1}: \gamma=0.9$, nsample $=10000$, accepted $=90 \%$
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-193.jpg?height=471&width=721&top_left_y=725&top_left_x=475)

The next plots show convergence of the mean and standard deviation to the target values. HMC converges most rapidly. The mean is near the target value of zero within hundrals of samples and the standar deviation thousands. Gibbs is next showing convergence of both with
thousands of samples and MH the worst in taking more the 10,000 samples to reach a similar stade.
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-194.jpg?height=486&width=729&top_left_y=407&top_left_x=70)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-194.jpg?height=486&width=684&top_left_y=407&top_left_x=826)
![](https://cdn.mathpix.com/cropped/2025_09_16_999c6fe6f78ecac6edafg-194.jpg?height=529&width=756&top_left_y=969&top_left_x=425)

The final set of plots illustrate convergence of the correlation coefficient to the target value of $\gamma=0.9$. The HMC samples converge to the target value
within hundreds of samples. Gibbs sampling requires about 1000 samples and MH nearly 10,000 samples.

## Conclusions

It has been shown that in metrics of data quality HMC is the best performing overall. The improved data quality is mostly a consequence of lack of autocorrelation in the samples. This is a result of the algorithm not using the previous state in determination of the next state. This is not the case for Gibbs and MH which explicitly use the previous state in determing tir next state. The improved data quality of thic comes at a computational cost since Hamitton's equations must be integrated for hundreds of steps for each sample. The data qualty of Gibbs and MH samplets an be improved by using Burn-in and thinning but these methods can reduce the number of samples
by an order of magnitude, thus requiring that an order of magnitude more samples be produced.
Though Hamiltonian Monte Carlo is the best performing it may not be practical to use it since it it is more computationally demanding and requires that the logarithm of the target distribution be differentiable which may not be the case. If Hamiltonian Monte carlo is not feasable then Gibbs sampling would be the next choice. Gibbs sampling is has a simple implementation but requires that the conditional distributions of the target distribution be known and sampleable. If this is not possible then Metropolis Hastings is the only choice. It is also possible to construct hybrid methods that leverge advantages of each methor.

