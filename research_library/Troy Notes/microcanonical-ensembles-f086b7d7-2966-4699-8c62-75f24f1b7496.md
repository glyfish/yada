## Microcanonical Ensembles

![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-001.jpg?height=258&width=480&top_left_y=1472&top_left_x=989)

## The Bottzmam Phinciple

## Heat Theorem

Recall the first law of thermodpnamics

$$
\delta Q=d U+P d V \leqslant T d S
$$

for reversible processes equality holds and the heat theorem is obtained

$$
d s=\frac{d u}{T}+\frac{P}{T} d v
$$

If $S$ is assumed to be a function of $u$ and $v$ then

$$
d s=\frac{\partial s}{\partial u} d u+\frac{\partial s}{\partial v} d v
$$

comparing with the previous result

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

One-Dimensional Mechanical Models of Thermodynamics
In this section a one-dimensional classical analog of thermodynamic entropy is consturted and bused
on the heat theorem. This argument was originally made by Helmoltz in the late $19^{\prime}$ th century and referred to as the Helmholtz theorem.

Consider a particle of mass $m$ constrained to move in a single dimension denoted by $x$ in a potential of the form $\varphi(x ; v)$ which has a $u$ shape so that the particle motion is periodic. The parameter $V$ controls the strength of the force acting on the particle.
The Hamiltonian for this system is given by

$$
H(x, p ; v)=\frac{p^{2}}{2 m}+\varphi(x ; v)
$$

where $P$ is the momentum and the Kinetre energy is given by

$$
K=\frac{p^{2}}{2 m}
$$

For a fixed value of $v$ the Hamittonanian is conserved. Denote its value by $u$

$$
H(x, p ; v)=\frac{p^{2}}{2 m}+\varphi(x ; v)=u
$$

Specifying $u$ and $v$ will completley determine the dinamics of the system. These varialdes are the assumed thermodymamic state varrables where $u$ is the interval energy and $v$ is a volume parameter. If go furter expressions for temperature and pressure are required.
If $\tau(u, v)$ is used to dende the period of the particle motion the temperature and pressure are defined by an average over a period of motion of the square of the momentum, which is realated to the kinetic energy, and - $\partial \varphi / \partial v$.

$$
T=\frac{2}{k_{B}}\langle k\rangle=\frac{2}{k_{B} \tau(u, v)} \int_{0}^{\tau(u, v)} K(p(t)) d t
$$

where $k_{B}$ is the Boltzmann constant which performs the correct unit conversion and the factor of 2 compenstates for the $1 / 2$ term in the Kinedic energy. And the pressure is given by

$$
P=-\frac{1}{\tau(u, v)} \int_{0}^{\tau(u, v)} \frac{\partial \varphi}{\partial v}(x(t) ; v) d t
$$

Recall that

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

It will be shown that a solution to these equations is given by

$$
S=k_{B} \ln \Phi(u, v)
$$

where $\Phi(u, v)$ is the area enclosed by the curve

$$
u=H(x, p ; v)
$$

namely

$$
\Phi(u, v)=\iint_{H(x, P ; v) \leqslant u} d x d p
$$

Ergodicity and Microcanical Ensemble in 1 Dimensional Model

To obtain the above expression two concepts are needed, ergodicity and microcannoical ensemble.

To understand ergodicity consider the one-dimensional system with

Hamiltonian

$$
H(x, p ; v)=\frac{p^{2}}{2 m}+\varphi(x ; v)=u
$$

and the phase space function

$$
f(x, p)=f(x(t), p(t))
$$

where $x(t)$ and $p(t)$ are periodic functions with perrod $\tau(u, v)$. The average of $f$ over one period, denoted by $\langle f\rangle_{t}$, is given by

$$
\langle f\rangle_{t}=\frac{1}{\tau} \int_{0}^{\tau} f(x(t), p(t)) d t
$$

Now the momentum is related to the time derivative of the position coordinate by

$$
\begin{aligned}
p(x) & =m \frac{d x}{d t} \\
\Rightarrow d t & =\frac{m}{p(x)} d x
\end{aligned}
$$

where it has been assumed
$P$ is a periodic function of the position coordinate, $x$.
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-007.jpg?height=499&width=980&top_left_y=213&top_left_x=169)

## an example is shown in the figure.

An equation for $P(x)$ can be found from

$$
\frac{p^{2}}{2 m}+\varphi(x ; v)=u
$$

$\Rightarrow p(x)= \pm \sqrt{2 m(u-\phi(x ; v))}$
The function of phase coordinates becomes

$$
f(x, p)=f(x, p(x))
$$

and the expression to the time average becomes

$$
\begin{aligned}
\langle f\rangle_{t} & =\frac{m}{\tau} \int_{x}^{x_{t}} \frac{f(x, p(x)) d x}{p(x)}+\frac{m}{\tau} \int_{x_{t}}^{x_{-}} \frac{f(x, p(x))}{(-p(x))} d x \\
& =\frac{2 m}{\tau} \int_{x_{-}}^{x_{+}} \frac{f(x, p(x))}{p(x)} d x
\end{aligned}
$$

Where the first integral is over the top curve and the second the bottom curve To go further consider the integral

$$
\int \delta\left[\frac{p^{2}}{2 m}+\varphi(x ; v)-u\right] d p
$$

where $\delta(x)$ is the Dirac detta function where the argument is the curve in phase space defined by the assumption the energy is conserved, namely)

$$
\begin{aligned}
& H(x, p: v)=\frac{p^{2}}{2 m}+\varphi(x ; v)=u \\
\Rightarrow & \frac{p^{2}}{2 m}+\varphi(x ; v)-u=0
\end{aligned}
$$

A properly of the Dirac detta function if for a function $f(x)$ where

$$
f\left(p_{i}\right)=0 \quad \forall \quad i=1,2, \ldots, n
$$

then

$$
\delta(f(p))=\sum_{i=1}^{n} \frac{1}{\left|f^{\prime}\left(p_{i}\right)\right|} \delta\left(p-p_{i}\right)
$$

Now consider the case

$$
f(p)=\frac{p^{2}}{2 m}+\phi(x, v)-u
$$

The zeros of this equation

$$
\begin{aligned}
& f\left(p_{0}\right)=0 \\
\Rightarrow & \frac{p_{0}^{2}}{2 m}+\phi(x, v)-u=0
\end{aligned}
$$

which has the solution

$$
P_{0}= \pm \sqrt{2 m(u-\phi(x ; v))}
$$

and

$$
f^{\prime}(p)=\frac{p}{m}
$$

$$
\begin{aligned}
\delta(f(p)) & =\frac{1}{\left|f^{\prime}\left(p_{0}\right)\right|} \delta\left(p-p_{0}\right)+\frac{1}{\left|f^{\prime}\left(-p_{0}\right)\right|} \delta\left(p+p_{0}\right) \\
& =\sum_{p_{0}}^{m}\left[\delta\left(p-p_{0}\right)+\delta\left(p+p_{0}\right)\right]
\end{aligned}
$$

it follows that

$$
\begin{aligned}
& \int \delta\left[\frac{p^{2}}{2 m}+\varphi(x ; v)-u\right] d p \\
& =\frac{m}{p_{0}} \int\left[\delta\left(p-p_{0}\right)+\delta\left(p+p_{0}\right)\right] d p \\
& =\frac{2 m}{p_{0}}
\end{aligned}
$$

Now

$$
P_{0}(x)=\sqrt{2 m(u-\varphi(x ; v))}
$$

defines the relationship in phase space used in the calculation of the time average,

$$
\begin{aligned}
& \langle f\rangle_{t}=\frac{\partial m}{\tau} \int_{x_{-}}^{x_{+}} \frac{f(x, p(x))}{p(x)} d x \\
& =\frac{1}{\tau} \iint \delta\left[\frac{p^{2}}{2 m}+\phi(x ; v)-u\right] f(x, p) d x d p
\end{aligned}
$$

The $x^{x}$ and $x_{+}$limits are no longer needed since Detta function
constrains integration to the thase space volume occupied by the system.

The period of the system is given by

$$
\begin{aligned}
\tau & =\int_{0}^{\tau} d t=\int_{x_{-}}^{x_{+}} \frac{2 m}{p(x)} d x \\
& =\iint \delta\left[\frac{p^{2}}{2 m}+\phi(x ; v)-u\right] d x d p
\end{aligned}
$$

If the micromechanical distribution is defined by

$$
e(x, p ; E, v)=\frac{1}{\tau} \delta\left[\frac{p^{2}}{2 m}+\phi(x ; v)-u\right]
$$

Then

$$
\langle f\rangle_{t}=\iint \rho(x, p ; E, v) f(x, p(x)) d x d p
$$

Thus $\tau(E, V)$ plays the role of a normalization constant and $e(x, P ; E, v)$ a probability density

## function.

It has been shown that the time average $\langle f\rangle_{t}$ is equal to the average obtained using $\ell(x, P ; V, E)$. This property is called ergodicity.
The microcononical density, $\rho(x, p ; E, v)$, represents distribution of states in phase space that are uniformly distributed over the curve defined by

$$
H(x, p ; v)=u
$$

This collection of states is referred to as microcononical ensemble and avereages of functions obtained using the micrononical density are called ensembe aveages.
Ergodicity can be stated as the equilatence of trme averages and ensemble averages.
It has been shown that all I dimensional systems with a potential $\varphi(x ; v)$ are ergodic.

Entropy, Pressure and Temperature
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-013.jpg?height=487&width=1086&top_left_y=219&top_left_x=120)

Recall that the volume enclosed by the curve

$$
u=H(x, p ; V)
$$

namely

$$
\Phi(u, v)=\iint_{H(x, p, v) \leqslant u} d x d p
$$

which is the orange area shown in the figure.
Consider the Heaviside function,

$$
\theta(f(x))= \begin{cases}0 & f(x)<0 \\ 1 & f(x) \geqslant 0\end{cases}
$$

and

$$
\frac{d \theta}{d x}(f(x))=\delta(f(x)) \frac{d f}{d x}
$$

where $\delta(f(x))$ is the Dirac delta function.

It follows that

$$
\Phi(u, v)=\iint \theta[u-H(x, p ; v)] d x d p
$$

and

$$
\begin{aligned}
\frac{\partial \bar{\phi}}{\partial u} & =\iint \frac{d \theta}{d u}[u-H(x, p ; v)] d x d p \\
& =\iint \delta[u-H(x, p ; v)] d x d p \\
& =\tau
\end{aligned}
$$

Where $\uparrow$ is the period of the system, thus

$$
\tau=\frac{\partial \bar{\Phi}}{\partial u}
$$

Similarly using

$$
\Phi(u, v)=\iint \theta[u-H(x, p ; v)] d x d p
$$

gives

$$
\frac{\partial \Phi}{\partial v}=\iint \frac{\partial}{\partial v}\{\theta[u-H(x, p ; v)]\} d x d p
$$

NOW

$$
\begin{aligned}
& \frac{\partial}{\partial v}\{\theta[u-H(x, p ; v)]\} \\
= & \frac{\partial}{\partial v}\left\{\theta\left[u-\frac{p^{2}}{2 m}-\phi(x ; v)\right]\right\} \\
= & \delta\left[u-\frac{p^{2}}{2 m}-\phi(x ; v)\right]\left(-\frac{\partial \varphi}{\partial v}\right) \\
\text { so } & \frac{\partial \Phi}{\partial v}=\iint \delta[u-H(x, p ; v)]\left(-\frac{\partial \varphi}{\partial v}\right) d x d p \\
= & -\left\langle\frac{\partial \Phi}{\partial v}\right\rangle^{\tau}
\end{aligned}
$$

Recall that the temperature, $T$, is defined by,

$$
T=\frac{2}{k_{B}}\langle K\rangle=\frac{2}{k_{B} \tau(u, v)} \int_{0}^{\tau(u, v)} K(p(t)) d t
$$

where the average kinetic energy is defined by

$$
\langle k\rangle=\frac{1}{\tau} \int_{0}^{\tau} k(p(t)) d t
$$

Using

$$
d t=\frac{m}{p(x)} d x
$$

and

$$
K=\frac{p^{2}}{2 m}
$$

gives

$$
\begin{aligned}
\langle k\rangle & =\frac{2}{\tau} \int_{x_{-}}^{x_{+}}\left(p^{2}(x)\right. \\
& =\frac{1}{\tau} \int_{x_{-}}^{x_{+}} p(x) d x
\end{aligned}
$$

but

$$
\begin{aligned}
\Phi(u, v) & =\iint_{H\left(x_{1}, p_{i}\right) \leqslant u} d x d p \\
& =2 \int_{x_{-}}^{x_{+}} p(x) d x
\end{aligned}
$$

The abriviated action is defined by

$$
\oint p(x) d x=2 \int_{x}^{x+} p(x) d x
$$

thus

$$
\Phi(u, v)=\oint p(x) d x
$$

and

$$
2\langle k\rangle=\frac{\Phi}{\tau}
$$

It follows that the temperature, $\tau$, is given by

$$
T=\frac{\partial\langle k\rangle}{k_{B}}=\frac{\Phi}{k_{B} \tau}
$$

Recall that the pressure, $P_{1}$ is defined by

$$
\begin{aligned}
P & =-\frac{1}{\tau(u, v)} \int_{0}^{\tau(u, v)} \frac{\partial \varphi}{\partial v}(x(t) ; v) d t \\
& =-\frac{1}{\tau} \iint \delta\left[u-\frac{p^{2}}{2 m}-\varphi(x ; v)\right] \frac{\partial \varphi}{\partial v} d x d p \\
& =-\left\langle\frac{\partial \varphi}{\partial v}\right\rangle
\end{aligned}
$$

but

$$
\frac{1}{\tau} \frac{\partial \Phi}{\partial V}=-\left\langle\frac{\partial \Phi}{\partial V}\right\rangle
$$

thus

$$
P=\frac{1}{\tau} \frac{\partial \Phi}{\partial V}
$$

An expression for the Entropy, 5 , can be found using the following expressions

$$
\tau=\frac{\partial \Phi}{\partial u} \quad \tau P=\frac{\partial \Phi}{\partial V} \quad T=\frac{\Phi}{k_{B} \tau}
$$

and

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

Now

$$
\frac{\partial S}{\partial u}=\frac{1}{T}=k_{B} \frac{\tau}{\Phi}
$$

A solution to this equation is

$$
S=k_{B} \ln \Phi
$$

50

$$
\frac{\partial S}{\partial u}=k_{B} \frac{1}{\Phi} \frac{\partial \Phi}{\partial u}=k_{B} \frac{T}{\Phi}=\frac{1}{T}
$$

and

$$
\frac{\partial S}{\partial V}=k_{B} \frac{1}{\Phi} \frac{\partial \Phi}{\partial V}=k_{B} \frac{\tau}{\Phi} P=\frac{e}{T}
$$

thus

$$
S=k_{B} \ln \Phi
$$

## Mechanical Models for Multi-Particle Systems in Three-Dimensions

The one-dimensional single particle model discussed previously can be extended to a three-dimensional $N$ particle system.
The Hamiltonian for a three-dimesional $N$ particle sytem with a $u$ shaped potental producing periodic motion is given by

$$
H(\bar{q}, \bar{p} ; v)=K(\bar{p})+\varphi(\bar{q} ; v)
$$

where $\bar{q}$ and $\bar{p}$ are $3 N$-dimensional vectors for the position and momentum respectively which represent the state of the system in a GN-dimensional phase space.
The Kinetic energy is assumed to be of the form

$$
K(\bar{p})=\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 M}
$$

The microconical distribution
for this system is given by

$$
e(\bar{q}, \bar{p} ; u, v)=\frac{1}{\Omega(u, v)} \delta[u-H(\bar{q}, \bar{p} ; v)]
$$

where $\Omega(u, v)$ is the normalization factor

$$
\Omega(u, v)=\int \cdots \int \delta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
$$

where $d \Gamma$ is a phase space volume elemenent given by

$$
d \Gamma=d q_{1} d q_{2} \cdots d q_{3 N} d p_{1} d p_{2} \cdots d p_{3 N}
$$

$\Omega(u, v)$ is known as the Partition funtion. $\rho(\bar{q}, \bar{p} ; u, v)$ assumes that the system states are uniformly distributed over the volume defined $6 N-1$ dimensional space defined by

$$
H(\bar{a}, \bar{p} ; v)=u
$$

which has volume $\Omega(U, V)$.
Ergodicity is assumed, just as in the one-aimensional model, so that time averages are assumed equivalent to miorocononical
ensemble averges. So for a function of phase coordinates $f(\bar{q}, \bar{p})$ but unlike the one-dimensional proof is not simple and here remains an asscemption.

$$
\begin{aligned}
& \left\langle f(\bar{q}(t), \bar{p}(t)\rangle_{\tau}=\frac{1}{\tau} \int_{0}^{\tau} f(\bar{q}(t), \bar{p}(t)) d t\right. \\
& =\int S \cdots S \rho(\bar{q}, \bar{p} ; E, V) f(\bar{q}, \bar{p}) d \Gamma \\
& =\langle f(\bar{q}, \bar{p})\rangle
\end{aligned}
$$

where $\langle f(\bar{q}, \bar{p})\rangle$ denotes the ensemble averages.
The temperature is defined by in analogy with the one-dimesional case,

$$
T(u, v)=\frac{2}{3 N k_{B}}\langle K(\bar{p})\rangle
$$

Here the expression for $\langle K(\bar{p})\rangle$ is given by

$$
K(\bar{p})=\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 m}
$$

contains $3 N$ terms thus $T(u, v)$ represents average Kinetic per momentum coordinate component.
The pressure is defined by

$$
P(u, v)=-\left\langle\frac{\partial \phi}{\partial v}(\bar{x} ; v)\right\rangle
$$

Finally the entropy function must satisfy the equations satisfied by the one-dimensional model

$$
\frac{\partial S}{\partial u}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

In analogy the with the ane-dimensional case the volume enclosed by - lne curve

$$
H(\bar{q}, \bar{p} ; v)=u
$$

in the 6 N dimensional phase space is given by

$$
\begin{aligned}
\Phi(u, v) & =\iint \cdots \int d \Gamma \\
& =\iint(\bar{q}, \bar{p} ; v) \leqslant u \\
& =\int \theta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
\end{aligned}
$$

and

$$
\begin{aligned}
\frac{\partial \Phi}{\partial u}(u, v) & =\iint \cdots \int \frac{\partial \theta}{\partial E}[u-H(\bar{q}, \bar{p} ; v)] d \Gamma \\
& =\iint \cdots \int\delta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma \\
& =\Omega(u, v)
\end{aligned}
$$

thus

$$
\Omega=\frac{\partial \Phi}{\partial u}
$$

Similarly
$\frac{\partial \Phi}{\partial v}(u, v)=\iint \cdots \int \frac{\partial}{\partial v} \theta[u-H(\bar{q}, \bar{\rho} ; v)] d \Gamma$
so

$$
\begin{aligned}
& \frac{\partial \theta}{\partial v}[u-H(\bar{q}, \bar{p} ; v)]=\frac{\partial \theta}{\partial v}\left[u-\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{\partial m}-\phi(\bar{q} ; v)\right] \\
& =-\delta\left[u \cdot \sum_{i=1}^{3 N} \frac{p_{i}^{2}}{\partial m}-\phi(\bar{q} ; v)\right] \frac{\partial \phi}{\partial v}(\bar{q} ; v) \\
& =-\delta[u-H(\bar{q}, \bar{p} ; v)] \frac{\partial \phi}{\partial v}(\bar{q} ; v)
\end{aligned}
$$

50

$$
\begin{aligned}
& \frac{\partial \Phi}{\partial v}(u, v)= \\
& =\iint \cdots \int \delta[u-H(\bar{q}, \bar{p} ; v)] \frac{\partial \varphi}{\partial v}(\bar{q} ; v) d \Gamma \\
& =-\Omega\left\langle\frac{\partial \varphi}{\partial v}(\bar{q} ; v)\right\rangle
\end{aligned}
$$

tnus

$$
\frac{\partial \Phi}{\partial v}=-\Omega\left\langle\frac{\partial \varphi}{\partial v}(\bar{q} ; v)\right\rangle
$$

Next consider the ensemble averages

$$
\left\langle p_{i} \frac{\partial H}{\partial p_{i}}\right\rangle \quad\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle
$$

For the first

$$
\begin{aligned}
& \left\langle P_{i} \frac{\partial H}{\partial P_{i}}\right\rangle=\left\langle P_{i} \frac{d q_{i}}{d t}\right\rangle=\frac{1}{m}\left\langle P_{i} P_{i}\right\rangle \\
& =\frac{1}{m}\left\langle P_{i}^{2}\right\rangle=2\left\langle K_{i}\right\rangle
\end{aligned}
$$

Where $\left\langle K_{i}\right\rangle$ is the average
Kinetic energy. kinetic energy.

Now

$$
\begin{aligned}
& \left\langle P_{i} \frac{\partial H}{\partial P_{i}}\right\rangle=\frac{1}{\Omega} \iint \cdots \int \delta[u-H(\bar{p}, \bar{q} ; v)] P_{i} \frac{\partial H}{\partial p_{i}} d \Gamma \\
& =\frac{1}{\Omega} \iint \cdots \int \frac{\partial}{\partial u}\left[\theta[u-H(\bar{p}, \bar{q} ; v)] P_{i} \frac{\partial H}{\partial p_{i}}\right] d \Gamma \\
& =\frac{1}{\Omega} \frac{\partial}{\partial u}\left[\iint \cdots \int \theta[u-H(\bar{p}, \bar{q} ; v)] P_{i} \frac{\partial H}{\partial p_{i}}\right] d \Gamma \\
& =\frac{1}{\Omega} \frac{\partial}{\partial u}\left[\iint \cdots \int \theta(u-H) P_{i} \frac{\partial H}{\partial p_{i}}\right] d \Gamma
\end{aligned}
$$

Consider the integral

$$
\int S \cdots \int \theta(u-H) p_{i} \frac{\partial H}{\partial p_{i}} d \Gamma
$$

Now

$$
P_{i} \frac{\partial H}{\partial P_{i}}=P_{i} \frac{\partial}{\partial P_{i}}(H-u)
$$

since $E$ is independent of $p_{i}$. Tre product rule gives

$$
\left.\frac{\partial}{\partial P_{i}}\left(P_{i}(H-u)\right)=\frac{\partial P_{i}}{\partial P_{i}}(H-u)+P_{i} \frac{\partial(H}{\partial P_{i}}-u\right)
$$

$$
\begin{aligned}
\Rightarrow p_{i} \frac{\partial(H-u)}{\partial p_{i}} & =\frac{\partial}{\partial p_{i}}\left(p_{i}(H-u)\right)-(H-u) \\
& =\frac{\partial}{\partial p_{i}}\left(p_{i}(H-u)\right)+(u-H)
\end{aligned}
$$

thus

$$
P_{i} \frac{\partial H}{\partial P_{i}}=\frac{\partial}{\partial P_{i}}\left(P_{i}(u-H)\right)+(u-H)
$$

It follows that

$$
\begin{aligned}
& \iint \cdots \int \theta(u-H) p_{i} \frac{\partial H}{\partial p_{i}} d \Gamma \\
& =\iint \cdots \int \theta(u-H)\left[\frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right)+(u-H)\right] d \Gamma \\
& =\iint \cdots \int \theta(u-H) \frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right) d \Gamma \\
& \quad+\iint \cdots \int \theta(u-H)(u-H) d \Gamma
\end{aligned}
$$

thus

$$
\iint \cdots \int \theta(u-H) p_{i} \frac{\partial H}{\partial p_{i}} d \Gamma
=\iint \cdots \int \theta(u-H) \frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right) d \Gamma
+\iint \cdots \int \theta(u-H)(u-H) d \Gamma
$$

Consider the first integral

$$
\iint \cdots \int \theta(u-H) \frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right) d \Gamma
=\iint_{H \leqslant u} \cdots \int \frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right) d \Gamma
$$

For the $p_{i}$ integral the result is

$$
\left.P_{i}(u-H)\right|^{u=H}=0
$$

which is evaluated over time surface $u=H$ which vanishes.
It follows that

$$
\iint \cdots \int \theta(u-H) \frac{\partial}{\partial p_{i}}\left(p_{i}(u-H)\right) d \Gamma=0
$$

So

$$
\begin{aligned}
& \iint \cdots \int \theta(u-H) p_{i} \frac{\partial H}{\partial p_{i}} d \Gamma \\
& =\iint \cdots \int \theta(u-H)(u-H) d \Gamma
\end{aligned}
$$

Recall that

$$
\begin{aligned}
& \left\langle P_{i} \frac{\partial H}{\partial P_{i}}\right\rangle= \\
& \quad \frac{1}{\Omega} \frac{\partial}{\partial u}\left[\iint \cdots \int \theta(u-H) P_{i} \frac{\partial H}{\partial P_{i}}\right] d \Gamma \\
& =\frac{1}{\Omega} \frac{\partial}{\partial u}\left[\iint \cdots \int \theta(u-H)(u-H) d \Gamma\right]
\end{aligned}
$$

Evaluation of the derivative using the previous equation gives

$$
\frac{\partial}{\partial u}\{\iint \cdots \int \theta(u-H)(u-H) d \Gamma\}
$$

$$
\begin{aligned}
& =\iint \cdots \int \delta(u-\mathbb{H})(u-H) d \Gamma \\
& +\iint  \cdots \int \theta(u-H) d \Gamma \\
& =\iint \cdots \int \theta(u-H) d \Gamma
\end{aligned}
$$

where the first term vanishes because

$$
\delta(u-H) \neq 0
$$

is true only if

$$
u=H
$$

Thus

$$
\begin{aligned}
\left\langle P_{i} \frac{\partial H}{\partial P_{i}}\right\rangle & =2\left\langle K_{i}\right\rangle=\int S \cdots S \theta(u-H) d \Gamma \\
& =\frac{\Phi}{\Omega}
\end{aligned}
$$

The average kinetic enersy per momementim coordinate is distributed uniformly. This should be compared to the result obtained for the one dimensional model

$$
2\langle k\rangle=\frac{\Phi}{\tau}
$$

The result for an arbitrary number of particles in three-dimensions can be obtained bic the replacement.

$$
\tau \rightarrow \Omega
$$

It follows that the average kinetic energy for the system is given biy

$$
\begin{aligned}
\langle k\rangle & =\sum_{i=1}^{3 N}\left\langle k_{i}\right\rangle=3 N\left\langle k_{i}\right\rangle \\
& =3 N\left(\frac{1}{2} \frac{\Phi}{\Omega}\right) \\
\Rightarrow\langle k\rangle & =\frac{2}{3 N} \frac{\Omega}{\Phi}
\end{aligned}
$$

Recall that the temperature is a measure of the average Kinetrc energy per partic el so

$$
k_{B} T=2\left\langle K_{i}\right\rangle=\frac{\Phi}{\Omega}=\left\langle P_{i} \frac{\partial H}{\partial P_{i}}\right\rangle
$$

Which is the same as obtained in the one-dimensional model b) replacing is with $\Omega$.

And for the second average,

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle
$$

The following integral must be evaluated

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle=\frac{1}{\Omega} \iint \cdots \int \delta[u-H(\bar{p}, \bar{q} ; v)] q_{i} \frac{\partial H}{\partial q_{i}} d \Gamma
$$

The evaluation of the integral
is similar to the momentum
version and the result obtained just replaces $p_{i}$ with $q_{i}$, namely,

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle=\frac{\Phi}{\Omega}=k_{B} T
$$

Now

$$
H(\bar{G}, \bar{p} ; v)=\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 m}+\varphi(\bar{q} ; v)
$$

so

$$
\frac{\partial H}{\partial \varphi_{i}}=\frac{\partial \phi}{\partial \varphi_{i}}
$$

gives

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle=\left\langle q_{i} \frac{\partial \phi}{\partial q_{i}}\right\rangle=k_{B} T
$$

and for the system as a whole

$$
\bar{q} \cdot \nabla \phi=\sum_{i=1}^{3 N} q_{i} \frac{\partial q_{i}}{\partial q_{i}}=3 N k_{B} T
$$

Since the force acting on the ith particle is given by

$$
F_{i}=-\frac{\partial \phi}{\partial q_{i}}
$$

it follows that

$$
\left\langle q_{i} \frac{\partial q}{\partial q_{i}}\right\rangle=k_{B} T
$$

is the average work performed by the position coordinate qu by the potentral.
Also, using

$$
-\dot{p}_{i}=\frac{\partial H}{\partial q_{i}}
$$

gives

$$
\left\langle q_{i} \frac{\partial H}{\partial q_{i}}\right\rangle=-\left\langle q_{i} p_{i}\right\rangle=k_{B} T
$$

Since $F_{i}=p_{i}$ this expression represents the work performed on the position coordinate $9 i$. For the entre system

$$
\bar{F} \cdot \bar{q}=\sum_{i=1}^{3 N} F_{i} q_{i}=-3 N k_{B} T
$$

Recall that the pressure is defined by

$$
P=-\left\langle\frac{\partial \varphi}{\partial v}\right\rangle
$$

It was previously shown that

$$
\frac{\partial \Phi}{\partial v}=-\Omega\left\langle\frac{\partial \Phi}{\partial v}\right\rangle
$$

It follows that

$$
\frac{\partial \Phi}{\partial V}=\Omega P
$$

Bringing the results together gives

$$
T=\frac{1}{k_{B}} \frac{\Phi}{\Omega} \quad \Omega=\frac{\partial \Phi}{\partial u} \quad \frac{\partial \Phi}{\partial V}=\Omega P
$$

Recall that the entropy, temperature and pressure are related by

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

A solution to this equation in analogy with the one-dimensional case ${ }^{1}$ is

$$
S=k_{B} \ln \Phi
$$

To verify substitute into the equations above

$$
\begin{aligned}
\frac{\partial S}{\partial u} & =k_{B} \frac{1}{\Phi} \frac{\partial \Phi}{\partial u}=k_{B} \frac{1}{\Phi} \frac{\partial \Phi}{\partial u} \\
& =k_{B} \frac{\Omega}{\Phi}=\frac{1}{T}
\end{aligned}
$$

$$
\begin{aligned}
\frac{\partial S}{\partial V} & =k_{B} \frac{1}{\Phi} \frac{\partial \Phi}{\partial V}=k_{B} \frac{\Omega}{\Phi} P \\
& =\frac{P}{T}
\end{aligned}
$$

## Phase space Volume

It was previously shown that

$$
\begin{gathered}
2\left\langle K_{i}\right\rangle=k_{B} T=\frac{\Phi}{\Omega} \\
\left\langle q_{i} \frac{\partial \Phi}{\partial q_{i}}\right\rangle=k_{B} T=\frac{\Phi}{\Omega} \\
\Omega=\frac{\partial \Phi}{\partial u}
\end{gathered}
$$

Consider

$$
H(\bar{q}, \bar{p} ; v)=K+\phi(\bar{q} ; v)=u
$$

So

$$
\langle H\rangle=\langle K\rangle+\langle\varphi\rangle=u
$$

Now using the previous results

$$
\begin{aligned}
\langle K\rangle & =\left\langle\sum_{i=1}^{3 N} K_{i}\right\rangle=\sum_{i=1}^{3 N}\left\langle K_{i}\right\rangle \\
& =\sum_{i=1}^{3 N} \frac{1}{2} k_{B} T=\frac{3 N}{2} k_{B} T
\end{aligned}
$$

If it is assumed the $\Phi(\bar{q} ; v)$ is harmonic then

$$
\phi(\bar{q} ; v)=\sum_{i=1}^{3 N} \phi\left(q_{i} ; v\right)=\sum_{i=1}^{3 N} \frac{1}{2} m v^{2} q_{i}^{2}
$$

Now

$$
\begin{aligned}
\frac{\partial \phi}{\partial q_{i}}(\bar{q} ; v) & =\sum_{i=1}^{3 N} \frac{\partial}{\partial q_{i}} \phi\left(q_{i} ; v\right) \\
& =2 m v^{2} q_{i}
\end{aligned}
$$

and

$$
q_{i} \frac{\partial \varphi}{\partial q_{i}}(\bar{q} ; v)=2 m v^{2} q_{i}^{2}=2 \varphi\left(q_{i} ; v\right)
$$

but it has been shown that

$$
\begin{aligned}
\left\langle q_{i} \frac{\partial \phi}{\partial q_{i}}(\bar{q} ; v)\right\rangle & =k_{B} T \\
& =2\left\langle\varphi\left(q_{i} ; v\right)\right\rangle
\end{aligned}
$$

50

$$
\begin{aligned}
\langle\varphi(\bar{q} ; v)\rangle & =\sum_{i=1}^{3 N}\left\langle\varphi\left(q_{i} ; v\right)\right\rangle=\sum_{i=1}^{3 N} \frac{1}{2} k_{B} T \\
& =\frac{3 N}{2} k_{B} T
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\langle H\rangle & =\langle k\rangle+\langle\phi(\bar{q} ; v)\rangle \\
& =\frac{3 N}{2} k_{B} T+\frac{3}{2} N k_{B} T \\
& =3 N k_{B} T \\
& =u
\end{aligned}
$$

Trus

$$
u=3 N k_{B} T
$$

Now if the temperature $T$ is assumed fixed, which is equisalent to assuming the average Kinetic and average potential energy is uniform over the pootrcles. This results in a total energy that
is a function only of the number of particles in the system or equivalently the number of phase space dimensions.
Now recall that

$$
\begin{gathered}
k_{B} T=\frac{\Phi}{\Omega} \Rightarrow \Omega=\frac{\Phi}{k_{B} T} \\
\Omega=\frac{\partial \Phi}{\partial u}
\end{gathered}
$$

since $T$ is fixed a solution to these equations is

$$
\Phi(N)=A e^{U / k_{B} T}=A e^{3 N}
$$

where $A$ is an arbitrary constant.

Also

$$
\Omega(N)=\frac{A}{k_{B} T} e^{u / k_{B} T}=\frac{A}{k_{B} T} e^{3 N}
$$

This result is true for a microcanonical ensemble with a harmonic potential for a
system of arbitrary size but can be shown to be true for large systems in the canonical without restricting the Hamittonian to harmonic polentials.

## Boltzman Entropy Formula

The Boltaman definition of Entropy is gruen by

$$
S=k_{B} \ln \omega
$$

where $\omega$ is the number of states available to the system.
It has been shown that an entropy defined by

$$
S=k_{B} \ln \Phi
$$

where $\Phi$ is the phase space volume enclosed by the system

$$
\Phi(u, v)=\int S \cdots S \theta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
$$

is equivalent to the thermodynamic entropy defined the heat theorem

$$
d s=\frac{d u}{T}+\frac{P}{T} d v
$$

To determine the relationship between these definitions recall that phase space volume available to the system is given by

$$
\Omega(u, v)=\int S \cdots \int \delta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
$$

Also it has been shown that

$$
\Omega(u, v) \propto \Phi(u, v)
$$

$$
S=k_{B} \ln \Phi=k_{B} \ln \Omega+\text { constant }
$$

The constant can be ignored since $s$ is defined upte an arbitinary constant.
Now $\Omega$ is the volume in phase space specified by the

$$
H(\bar{\varphi}, \bar{p} ; v)=u
$$

Assuming that the probability of the system states is uniformly distributed over phase space volume the probability that the system is in a partrcular state is given by

To count the number of states available to the system phase space needs to be desntitized. It is usually assumed that the size of a phase spree volume that contains a single state is given by

$$
\begin{aligned}
\Delta & =(\Delta q)^{3 N}(\Delta p)^{3 N} \\
& =h^{3 N}
\end{aligned}
$$

where it is assumed that the Heisenbers uncetainty principal places a lower bound on the product

$$
\Delta q \Delta p=h
$$

Now the system phase space is 6N dimensional but the surface defined by

$$
u=H(\bar{q}, \bar{p} ; v)
$$

is $6 \mathrm{~N}-1$ dimensional. It follows that in the discretized phase space the surface must have a finite thickness. If this thickness is denoted by $\Delta u$ the volume the system occupies in phase space is given by

## $\Delta u \Omega$

It follows that the number of states is given by

$$
\omega=\frac{\Delta u}{h^{3 N}} \Omega
$$

Thus the Boltaman expression for entropy is obtained

$$
\delta=\ln \omega
$$

## Adibadic Invariance of $\Phi$

Adibedic invariane is the statement that a system undersoin a reversible quasistatic change of state from an initral state defined by the state variables us and vo to some state with state varrables $u_{f}$ and $v_{f}$ does not produce a chance in the phase space volume orcupied b) the system. That is

$$
\begin{aligned}
\frac{d \Phi}{d t}(u, v) & =\frac{\partial \Phi}{\partial u} \frac{d u}{d t}+\frac{\partial \Phi}{\partial v} \frac{d v}{d t} \\
& =0
\end{aligned}
$$

To prove this assume that both $v$ and $u$ are slowly varying function of time so that the Hamiltonian of the system

$$
\begin{aligned}
H(\bar{q}(t), \bar{p}(t) ; v(t)) & =K(\bar{p}(t))+\phi(\bar{q}(t) ; v(t)) \\
& =u(t)
\end{aligned}
$$

Now the total time derivative is given by

$$
\begin{aligned}
\frac{d H}{d t} & =\sum_{i=1}^{3 N}\left\{\frac{\partial H}{\partial q_{i}} \dot{q}_{i}+\frac{\partial H}{\partial p_{i}} \dot{p}_{i}\right\}+\frac{\partial H}{\partial V} \dot{v}+\frac{\partial H}{\partial t} \\
& =\frac{d E}{d t}
\end{aligned}
$$

from Hamilton's Equation

$$
\frac{\partial H}{\partial q_{i}}=-p_{i} \quad \frac{\partial H}{\partial p_{i}}=\dot{q}_{i}
$$

It follows that

$$
\sum_{i=1}^{3 N}\left\{\frac{\partial H}{\partial q_{i}} \dot{q}_{i}+\frac{\partial H}{\partial p_{i}} \dot{p}_{i}\right\}=\sum_{i=1}^{3 N}\{(-\dot{p}) \dot{q}+\dot{q} \dot{p}\}
$$

$$
=0
$$

also since $H$ does not depend explicitly on $t$

$$
\frac{\partial H}{\partial t}=0
$$

Thus

$$
\frac{d H}{d t}=\frac{\partial H}{\partial v} \frac{d v}{d t}=\frac{d u}{d t}
$$

Now $H$ is a function of $V(t), G(t)$ and $p(t)$. The rever sible quasistatic assumption only assumes that $U(t)$ changes slowly while $g(t)$ and $p(t)$ can change rapidly leading to rapid Chances in $H$. The time scale of the changes is assumed to be much shorter than changes in $v(t)$ and $u(t)$. To remove the changes an average is performed over the fast time scale while assuming Inis is an extension of the notion of the quasistatic process to the system microdynamics where microscopic changes occur on a fast enough timescale so that ensemble averages can be obtained for each value of $u(t)$ and $V(t)$ which are changing on a much slower timescale. It follows that
each value of $u(t)$ and $v(t)$ which are changing on a much slower timescale. It follows that

$$
\begin{aligned}
\left\langle\frac{d t}{d t}\right\rangle & =\left\langle\frac{\partial H}{\partial v}\right\rangle \frac{d v}{d t} \\
& =\frac{d u}{d t}
\end{aligned}
$$

Now

$$
\begin{aligned}
\left\langle\frac{\partial H}{\partial v}\right\rangle & =\iint \cdots S e(\bar{q}, \bar{p}, u, v) \frac{\partial H}{\partial v} d \Gamma \\
& =\int S \cdots S e(\bar{q}, \bar{p}, u, v) \frac{\partial \phi}{\partial v} d \Gamma \\
& =\left\langle\frac{\partial \phi}{\partial v}\right\rangle
\end{aligned}
$$

It was previously shown that

$$
\frac{\partial \Phi}{\partial v}=-\Omega\left\langle\frac{\partial \Phi}{\partial v}(\bar{q} ; v)\right\rangle
$$

and

$$
\Omega=\frac{\partial \Phi}{\partial u}
$$

50

$$
\left\langle\frac{\partial H}{\partial V}\right\rangle=-\frac{1}{\Omega} \frac{\partial \bar{\phi}}{\partial V}
$$

$$
\Rightarrow \frac{d u}{d t}=\left\langle\frac{\partial H}{\partial v}\right\rangle \frac{d v}{d t}=-\frac{1}{\Omega} \frac{\partial \Phi}{\partial v} \frac{d v}{d t}=\frac{d u}{d t}
$$

Bringing things together gives

$$
\begin{aligned}
\frac{d \Phi}{d t} & =\frac{\partial \Phi}{\partial u} \frac{d u}{d t}+\frac{\partial \Phi}{\partial v} \frac{d v}{d t} \\
& =(\Omega)\left(\frac{-1}{\Omega}\right) \frac{\partial \Phi}{\partial v} \frac{d u}{d t}+\frac{\partial \Phi}{\partial v} \frac{d v}{d t} \\
& =0
\end{aligned}
$$

Thus a reversible quasistatic process that takes the system between two macroccopic states $\left(u_{0}, v_{0}\right)$ to $\left(u_{f}, v_{f}\right)$ following $u(t)$ and $v(t)$ conserves phase space volume. This result is consistent with the result obtained in thermodynamics for the entropy defined by

$$
d s=\frac{d Q}{T}
$$

which is also invariant under a change in state following a reversible quasistatic process. The result that a reversible quasistatic process also does not change the phase space udume ensures
that the entrapy defined by

$$
S=k_{B} \ln \Phi
$$

also has this property.

## One-Dimensional Mechanical Example

Consider a particle with mass $m$ constrained to motion in one-dimension and acted on by a linear force which is zero at $q=0$

$$
F=-m v^{2} q^{2}
$$

Tre potential function is given by

$$
\begin{aligned}
\varphi(q ; v) & =-\int F d q \\
& =\frac{1}{2} m v^{2} q^{2}+c
\end{aligned}
$$

assuming $\varphi(0 ; v)=0 \Rightarrow c=0$ thus

$$
q(q ; v)=\frac{1}{2} m v^{2} q^{2}
$$

and the kinetic energy is given by

$$
k(p)=\frac{p^{2}}{2 m}
$$

where $P$ is the momentum.
Now the Hamiltonian of the system is given by

$$
H(q, p ; v)=\frac{p^{2}}{2 m}+\frac{m v^{2}}{2} q^{2}
$$

Hamiltons equation yield the equation of motions

$$
\dot{p}=-\frac{\partial H}{\partial q} \quad \dot{q}=\frac{\partial H}{\partial p}
$$

It follows that

$$
\begin{aligned}
& \dot{p}=-m v^{2} q \Rightarrow \ddot{p}=-m v^{2} \dot{q} \\
& \dot{q}=\underset{m}{p}
\end{aligned}
$$

substituting the second equation into the first gives

$$
\ddot{p}+v^{2} p=0
$$

It is easy to show that

$$
p=A \cos v t
$$

where $A$ is a constant defined by $t=0$

$$
P_{0}=A
$$

is a solution it follows that

$$
\dot{q}=\frac{p}{m} \Rightarrow q(t)=\frac{p_{0}}{v_{m}} \sin v t
$$

A has not yet been determined and $v$ is the frequency of motion of $P_{p}$ and $x$ in phase space and related to the strength of the force giving rise to $\varphi(x, v)$. Substituting the expressions for $x(t)$ and $p(t)$ into the Hamiltonian gives

$$
\begin{aligned}
H & =\frac{p_{0}^{2} \cos ^{2} v t}{2 m}+\frac{m v^{2}}{2}\left(\frac{p_{0}^{2}}{m^{2} v^{2}}\right) \sin ^{2} v t \\
& =\frac{p_{0}^{2}}{2 m}\left(\cos ^{2} v t+\sin ^{2} v t\right)=\frac{p_{0}^{2}}{2 m}
\end{aligned}
$$

which is independent of time. It follows that the lotal energy of the system is conserved. In anticlpation of making an association with thermodynamic variables let $u$ denote the total energy of the system then

$$
H=\frac{p_{0}^{2}}{2 m}=u \Rightarrow p_{0}=\sqrt{2 m u}
$$

thus

$$
\begin{aligned}
p(t) & =\sqrt{2 m u} \cos (v t) \\
q(t) & =\sqrt{\frac{2 m u}{m v}} \sin (v t) \\
& =\sqrt{\frac{2 u}{m v^{2}}} \sin (v t)
\end{aligned}
$$

It follows that the dynamics of the system is determined by $u$ and $V$ which are independent. $u$ impacts the amplitude of the motion and $v$ the frequency. $u$ and $\checkmark$ will be considered as thermodpnamic state variables.

To complete the association with the heat theorem expressions for $T$ and $P$ are also required.
Recall that for the one-dimesional model it was shown that

$$
\begin{gathered}
\tau=\frac{\partial \Phi}{\partial u} \quad P=\frac{1}{\tau} \frac{\partial \Phi}{\partial V} \quad k_{B} T=\frac{\Phi}{\tau} \\
\frac{\partial S}{\partial u}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
\end{gathered}
$$

where

$$
\begin{aligned}
T & =\frac{\partial}{k_{B} \tau} \int_{0}^{\tau} \frac{P^{2}(t)}{\partial m} d t \\
P & =\frac{-1}{\tau} \int_{0}^{\tau} \frac{\partial \varphi}{\partial V} d t \\
& =\frac{-1}{\tau} \int_{0}^{\tau} m V G^{2}(t) d t \\
& =-\frac{m V}{\tau} \int_{0}^{\tau} q^{2}(t) d t
\end{aligned}
$$

Now

$$
\begin{aligned}
& p(t)=\sqrt{2 m u} \cos (v t) \\
& q(t)=\sqrt{\frac{2 u}{m v^{2}}} \sin (v t)
\end{aligned}
$$

So

$$
\tau=\frac{2 \pi}{V}
$$

and

$$
\begin{aligned}
T & =\frac{2}{k_{B}} \int_{0}^{\tau} \frac{p^{2}(t)}{2 m} d t \\
& =\frac{V}{\pi k_{B}} \int_{0}^{2 \pi / V} \frac{2 m U}{2 m} \cos ^{2}(v t) d t
\end{aligned}
$$

$$
=\frac{u V}{\pi k_{B}} \int_{0}^{2 \pi / V} \cos ^{2}\left(V_{t}\right) d t
$$

Now

$$
\begin{aligned}
& \cos ^{2} x+\sin ^{2} x=1 \\
\Rightarrow & \sin ^{2} x=1-\cos ^{2} x
\end{aligned}
$$

and

$$
\begin{aligned}
\cos (2 x) & =\cos ^{2} x-\sin ^{2} x \\
& =\cos ^{2} x-\left(1-\cos ^{2} x\right) \\
& =2 \cos ^{2} x-1 \\
\Rightarrow \cos ^{2} x & =\frac{1}{2}(\cos (2 x)+1)
\end{aligned}
$$

so

$$
\begin{aligned}
T & =\frac{u V}{\pi k_{B}} \int_{0}^{2 \pi / V} \cos ^{2}\left(V_{t}\right) d t \\
& =\frac{u V}{\pi k_{B}} \int_{0}^{2 \pi / V} \frac{1}{2}[\cos (2 V t)+1] d t
\end{aligned}
$$

$$
\begin{aligned}
& =\left.\frac{u v}{\pi k_{B}}\left(\frac{1}{2}\right)\left[\frac{1}{2 v} \sin (2 v t)+t\right]\right|_{0} ^{2 \pi / v} \\
& =\frac{u v}{\pi k_{B}}\left(\frac{1}{2}\right)\left(\frac{2 \pi}{v}\right) \\
& =\frac{u}{k_{B}} \\
& \Rightarrow u=T k_{B}
\end{aligned}
$$

This result is consistent with equipartion of energy between kinetry energy and potential energy
and

$$
\begin{aligned}
P & =-\frac{m v}{\tau} \int_{0}^{\tau} q^{2}(t) d t \\
& =-\frac{m v^{2}}{2 \pi} \int_{0}^{2 \pi / v} \frac{2 u}{m v^{2}} \sin ^{2}(v t) d t
\end{aligned}
$$

Now

$$
\begin{aligned}
& \sin ^{2} x+\cos ^{2} x=1 \\
\Rightarrow & \cos ^{2} x=1-\sin ^{2} x
\end{aligned}
$$

and

$$
\begin{aligned}
\cos (2 x) & =\cos ^{2} x-\sin ^{2} x \\
& =1-2 \sin ^{2} x \\
\Rightarrow \sin ^{2} x & =\frac{1}{2}[1-\cos (2 x)]
\end{aligned}
$$

So

$$
\begin{aligned}
P & =\left(-\frac{m v^{2}}{2 \pi}\right)\left(\frac{\partial u}{m v^{2}}\right) \int_{0}^{2 \pi / v} \frac{1}{2}[1-\cos (2 v t)] d t \\
& =\left.\frac{-u}{2 \pi}\left[t-\frac{1}{2 v} \sin (2 v t)\right]\right|_{0} ^{2 \pi / v} \\
& =-\frac{u}{v}
\end{aligned}
$$

In summary

$$
U=k_{B} T \quad P=-\frac{U}{V}
$$

Now

$$
\begin{aligned}
& p(t)=\sqrt{2 m u} \cos (v t) \\
& q(t)=\sqrt{\frac{2 U}{m v^{2}}} \sin (v t)
\end{aligned}
$$

so

$$
\begin{aligned}
\frac{p(t)}{2 m u} & =\cos (v t) \\
q(t) \sqrt{\frac{m v^{2}}{\partial u}} & =\sin (v t)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \cos ^{2}(v t)+\sin ^{2}(v t)=1 \\
\Rightarrow & \frac{p^{2}(t)}{2 m u}+\left(\frac{m v^{2}}{2 u}\right) q^{2}(t)=1 \\
\Rightarrow & \left(\frac{1}{2 m}\right) p^{2}(t)+\left(\frac{m v^{2}}{2}\right) q^{2}(t)=u \\
\Rightarrow & H(q, p ; v)=u
\end{aligned}
$$

For given values of $u$ and $v$ this is an equation of an elipse with axis aligned along the $P$ and $q$ axis. The maximum $P$ values occur at

$$
V t=n \pi \quad n=0,1,2, \ldots
$$

with value

$$
p_{\max }=\sqrt{2 m u}
$$

and the maximum $q$ values at

$$
V t=\frac{n \pi}{2} \pi \quad n=0,1,2, \ldots
$$

with value

$$
q_{\text {max }}=\sqrt{\frac{2 U}{m v^{2}}}
$$

Also, $p$ as a function of 9 is given by

$$
\begin{aligned}
& H(q, p ; v)=u \\
\Rightarrow & \left(\frac{1}{2 m}\right) p^{2}+\left(\frac{m v^{2}}{2}\right) q^{2}=u \\
\Rightarrow p(q) & = \pm \sqrt{2 m\left[u-\left(\frac{m v^{2}}{2}\right) q^{2}\right]} \\
& = \pm \sqrt{2 m u\left[1-\left(\frac{m v^{2}}{2 u}\right) q^{2}\right]} \\
& = \pm \sqrt{2 m u} \sqrt{1-\left(\frac{m v^{2}}{2 u}\right) q^{2}}
\end{aligned}
$$

now

$$
\begin{aligned}
\tau & =\int_{0}^{\tau} d t=\int_{-\sqrt{\frac{\partial u}{m v^{2}}}}^{\sqrt{\frac{\partial u}{m v^{2}}}} \frac{\partial m}{\left.p^{( } q\right)} d q \\
& =\iint \delta\left[\frac{p^{2}}{2 m}+\phi(x ; v)-u\right] d x d p
\end{aligned}
$$

consider the integral

$$
\tau=\int_{-\sqrt{\frac{2 u}{m v^{2}}}}^{\sqrt{\frac{2 u}{m v^{2}}}} \frac{2 m}{p^{(q)}} d q
$$

now

$$
p(q)=\sqrt{2 m u} \sqrt{1-\left(\frac{m v^{2}}{2 u}\right) q^{2}}
$$

let

$$
\begin{aligned}
& \sin x=\sqrt{\frac{m v^{2}}{\partial u}} q \\
\Rightarrow \quad & \cos x d x=\sqrt{\frac{m v^{2}}{\partial u}} d q
\end{aligned}
$$

$\Rightarrow \sqrt{\frac{2 u}{m v^{2}}} \cos x d x=d q$
at the integration limits

$$
q= \pm \sqrt{\frac{2 u}{m v^{2}}}
$$

it is seen that

$$
\begin{aligned}
& \sin x= \pm 1 \\
\Rightarrow & x= \pm \frac{\pi}{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
p(x) & =\sqrt{2 m u} \sqrt{1-\sin ^{2} x} \\
& =\sqrt{2 m u} \cos x
\end{aligned}
$$

$\pi / 2$

$$
\begin{aligned}
\tau & =2 m \int_{-\pi / 2} \frac{1}{\rho(x)} \sqrt{\frac{2 u}{m v^{2}}} \cos x d x \\
& =2 m \sqrt{\frac{2 u}{m v^{2}}} \sqrt{2 m L} \int_{-\pi / 2}^{\pi / 2} \frac{1}{\cos x} \cos x d x
\end{aligned}
$$

$$
\begin{aligned}
& =\sqrt{\frac{4 m^{2}(2 u)}{v^{2}}} \frac{1}{\sqrt{2 m u}} \int_{-\pi / 2}^{\pi / 2} d x \\
& =\frac{2}{v}\left(\frac{\pi}{2}+\frac{\pi}{2}\right)=\frac{2 \pi}{v}
\end{aligned}
$$

thus

$$
\tau=\frac{2 \pi}{V}
$$

This is in agreement with the result obtraved by inspection from the solution to Homilton's equation.
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-063.jpg?height=600&width=1164&top_left_y=1031&top_left_x=294)

The arca of an ellipse is given by

## $a b \pi$

where ab are the axis lengths of the ellipse.
It follows that

$$
\begin{aligned}
\Omega(E, v) & =\sqrt{2 m u} \sqrt{\frac{2 u}{m v^{2}}} \\
& =2 \pi \frac{u}{v}=\tau u
\end{aligned}
$$

Bringing things together

$$
\begin{gathered}
T=\frac{\partial \Phi}{\partial u} \quad P=\frac{1}{T} \frac{\partial \Phi}{\partial V} \quad R_{B} T=\frac{\Omega}{T} \\
\frac{\partial S}{\partial u}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
\end{gathered}
$$

It has been shown that

$$
\begin{gathered}
\tau=\frac{2 \pi}{V} \quad U=k_{B} T \quad P=-\frac{U}{V} \\
\Omega=\tau U
\end{gathered}
$$

$$
\begin{aligned}
& \text { Verifing the relations gives } \\
& \begin{aligned}
* T=\frac{\partial \Phi}{\partial u} & =\frac{\partial}{\partial u}(\tau u)=\tau \\
* P=\frac{1}{\tau} \frac{\partial \Phi}{\partial V} & =\frac{1}{\tau} \frac{\partial}{\partial V}\left(\frac{2 \pi u}{V}\right) \\
& =\frac{1}{\tau} 2 \pi u\left(-\frac{1}{V^{2}}\right) \\
& =\frac{1}{\tau}\left(\frac{2 \pi}{V}\right)\left(-\frac{u}{V}\right) \\
& =\left(\frac{1}{\tau}\right)(\tau)\left(-\frac{u}{V}\right)=-\frac{u}{V}
\end{aligned} \\
& \\
& \Rightarrow \frac{\Omega}{\tau}=\frac{\tau u}{\tau}=u=k_{B} T
\end{aligned}
$$

It follows that the entropy is given by

$$
\begin{aligned}
* S(u, v)=k_{B} \ln \Omega & =k_{B} \ln \left(\frac{2 \pi u}{v}\right) \\
& =k_{B} \ln \left(\frac{u}{v}\right)
\end{aligned}
$$

$$
\text { * } \begin{aligned}
\frac{\partial S}{\partial u} & =\frac{\partial}{\partial u}\left[k_{B} \ln \left(\frac{u}{v}\right)\right]=\frac{k_{B}}{u}=\frac{1}{T} \\
* \frac{\partial S}{\partial v} & =\frac{\partial}{\partial v}\left[k_{B} \ln \left(\frac{u}{v}\right)\right]=-\frac{k_{B}}{v} \\
& =\left(\frac{u}{v}\right)\left(-\frac{k_{B}}{u}\right) \\
& =\left(-\frac{u}{v}\right)\left(\frac{k_{B}}{u}\right) \\
& =\frac{P}{T}
\end{aligned}
$$

Particle in a 1 Dimensional Box
Consider a single particle confined to the interval

$$
0 \leqslant q \leqslant L
$$

within this interval no forces act on the particle and the Hamittonian will be

$$
H(p, q)=\frac{p^{2}}{2 m}=u
$$

where $u$ is a fixed value of the total energy for $0 \leqslant q \leqslant L$.
The particle is confined to the interval $[0,1]$ by the potential

$$
q(q ; L)=4 u[1-\theta(q)+\theta(q-L)]
$$

![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-067.jpg?height=438&width=1083&top_left_y=1491&top_left_x=193)

This potential is a limit of the previousk discussed u-shaped potential where the gradients are infinite and model perfecth reflecting walls. It will be seen that perfect reflection is accomplished by the un factor in the potential.
Now Hamilton's equations are given by

$$
\dot{p}=-\frac{\partial H}{\partial q} \quad \dot{q}=\frac{\partial H}{\partial p}
$$

The Hamiltonian for all values of $q$ will be given by

$$
H(p, q)=\frac{p^{2}}{2 m}+\varphi(q)
$$

where for $0 \leqslant q \leqslant L$

$$
H(p, q)=u
$$

and for $q<0$ and $q>L$

$$
H(p, q)=4 u
$$

The variation of $H(p, q)$ as 9 is varied is shown below
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-069.jpg?height=511&width=1120&top_left_y=34&top_left_x=118)

Using the Hamitonian above gives

$$
\begin{aligned}
& \dot{p}=\frac{-\partial \varphi}{\partial \varphi}=4 u[\delta(q)-\delta(q-L)] \\
& \dot{q}=\frac{p}{m}
\end{aligned}
$$

Consider a $p(q)$ that has a constant value $P c$ for $0 \leqslant g \leqslant L$ and is zero otherwise. The following function would describe a solulion of this type.

$$
p(q)=p_{c}[\theta(q)-\theta(q-L)]
$$

An analysis of twis equation will probide intuition about how to constuct $p(t)$

For $0 \leqslant q \leqslant L, H(p, q)=u$ so Pe must satusfy

$$
\frac{D_{c}^{2}}{2 m}=u
$$

$$
\Rightarrow \quad P_{c}= \pm \sqrt{2 m u}= \pm P_{0}
$$

and from Hamilton's equation for 9

$$
q=p
$$

80

$$
q(t)= \pm \frac{p_{0}}{m} t+q_{0}= \pm \sqrt{\frac{2 u}{m}} t+q_{0}
$$

where it is assumed that $0 \leqslant q \leqslant L$
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-070.jpg?height=688&width=1011&top_left_y=1225&top_left_x=380)

The phase space volume occupied by the system is shown in the above figure.
This system represents a particle of mass $m$ moving back and forth between the two walls defined by the potential $\varphi$ which is assumed to perfectly reflect the particle in a collision. The result is that collisions with the wall will only produce a change in direction of the particle not a loss of energy. For example if the particle is moving right toward the wall at position $G=L$ with momentum ifo when it strikes the wall it is perfectly reflected reversing the momentum! The new momentum - $P_{0}$ in the apposite direction will next take the particle to the wall at $a=0$ where a collision will reverse the momentum to $P_{0}$. This sequence of events represents a perrodre motion that will ropeat indefinitly. The momentum as a function of time is given by a periodic square wave
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-072.jpg?height=587&width=1210&top_left_y=68&top_left_x=171)

The postuon as a function of time is given by the periodic triangular wave
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-072.jpg?height=473&width=1164&top_left_y=1031&top_left_x=195)

For $0 \leqslant t \leqslant \tau$
Now the speed of the particle is given by

$$
v_{0}=p_{0}
$$

The time for the particle to complete 1 period of motion is
the time required to traverse
the distance from the origin to
$L$ and then back to the origin
a total distance $2 L$ so

$$
\tau=\frac{2 L}{V_{0}}=\frac{2 L m}{\rho_{0}}
$$

At each collision with the wall the particle experiences a change in momentum of

$$
\Delta p= \pm 2 p_{0}
$$

Consider the wall at $q=L$. The change in momentum in a collision is

$$
\Delta p=2 p_{0}
$$

the collisions occur with a frequency

$$
\Delta t=\tau=\frac{2 m L}{P_{0}}
$$

It follows that the average force on the wall is

$$
\left\langle F_{L}\right\rangle=\frac{\Delta p}{\Delta t}=\left(\partial p_{0}\right)\left(\frac{p_{0}}{\partial m L}\right)=\frac{p_{0}^{2}}{m L}
$$

Similarly for the wall at $q=0$

$$
\left\langle F_{0}\right\rangle=\frac{-P_{0}^{2}}{m L}
$$

## Bringing things together gives

$$
\begin{gathered}
\frac{P_{0}= \pm \sqrt{2 m u}}{\tau=\frac{2 m L}{\sqrt{2 m u}}=L \sqrt{\frac{2 m}{u}}} \\
\langle F\rangle= \pm \frac{P_{0}^{2}}{m L}= \pm\left(\frac{2 m u}{m L}\right)= \pm \frac{2 u}{L}
\end{gathered}
$$

Now consider one period of motion, $0 \leqslant t \leqslant \tau$. $p(t)$ is given by

$$
p(t)=-p_{0}+2 p_{0} \theta(t)-2 p_{0} \theta\left(t-\frac{1}{2} \tau\right)
$$

From Hamiltoris equation

$$
\frac{d g}{d t}=\frac{p}{m}
$$

thus

$$
\begin{aligned}
& q(t)=\int_{0}^{t} p(\omega) d \omega \\
& =\int_{0}^{t}-p_{0}+2 p_{0} \theta(\omega)-2 p_{0} \theta\left(\omega-\frac{1}{2} \tau\right) d \omega \\
& =-\left.p_{0} \omega\right|_{0} ^{t}+\left.2 p_{0} R(\omega)\right|_{0} ^{t}-\left.2 p_{0} R\left(\omega-\frac{1}{2} \tau\right)\right|_{0} ^{t}
\end{aligned}
$$

nere $R(\omega)$ is the ramp function

$$
R(\omega)= \begin{cases}0 & \omega<0 \\ \omega & \omega \geqslant 0\end{cases}
$$

So

$$
q(t)=-\frac{p_{0}}{m} t+\frac{2 p_{0}}{m} R(t)-\frac{2 p_{0}}{m} R\left(t-\frac{1}{2} \tau\right)
$$

now for one period $0 \leqslant t \leqslant \uparrow$ each of the contributions to $q(t)$ is given by
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-076.jpg?height=688&width=904&top_left_y=306&top_left_x=157)
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-076.jpg?height=688&width=884&top_left_y=1092&top_left_x=179)
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-077.jpg?height=698&width=1202&top_left_y=18&top_left_x=147)

## Computing the sum of the $q(t)$ terms gives

$$
q(t)= \begin{cases}\frac{p_{0}}{m} & 0 \leqslant t \leqslant \frac{1}{2} \tau \\ -\frac{p_{0}}{m}\left(t-\frac{1}{2} \tau\right)+L & \frac{1}{2} \tau \leqslant t \leqslant \tau\end{cases}
$$

For the first half of the period, $0 \leqslant t \leqslant \frac{1}{2}$, $q(t)$ is
given by

$$
\begin{aligned}
q & =\frac{p_{0}}{m} t \\
t & =\frac{m}{p_{0}} q
\end{aligned}
$$

and for $\frac{1}{2} \tau \leqslant t \leqslant \tau$

$$
\begin{aligned}
& q=-\frac{p_{0}}{m}\left(t-\frac{1}{2} \tau\right)+L \\
\Rightarrow & t-\frac{1}{2} \tau=-\frac{m}{p_{0}}(q-L)
\end{aligned}
$$

so $t(a)$ is given by

$$
t= \begin{cases}\frac{m}{p_{0}} q & 0 \leqslant t \leqslant \frac{1}{2} \tau \\ -\frac{m}{p_{0}}(q-L)+\frac{1}{2} \tau & \frac{1}{2} \tau \leqslant t \leqslant \tau\end{cases}
$$

Now

$$
\begin{aligned}
\frac{d p}{d t} & =2 p_{0} \delta(t)-2 p_{0} \delta\left(t-\frac{1}{2} \tau\right) \\
& =2 p_{0}\left[\delta(t)-\delta\left(t-\frac{1}{2} \tau\right)\right]
\end{aligned}
$$

using the previous expressions for $t$ as a function of $q$ gives

$$
\begin{aligned}
\frac{d p}{d t} & =2 p_{0}\left[\delta\left(\frac{m}{p_{0}} q\right)-\delta\left(-\frac{m}{p_{0}}(q-L)\right)\right] \\
& =2 p_{0}\left[\frac{p_{0}}{m} \delta(q)-\frac{p_{0}}{m} \delta(q-L)\right] \\
& =\frac{2 p_{0}^{2}}{m}[\delta(q)-\delta(q-L)] \\
& =4 u[\delta(q)-\delta(q-L)]
\end{aligned}
$$

but

$$
\frac{d p}{d t}=-\frac{\partial H}{\partial q}=4 u[\delta(q)-\delta(q-L)]
$$

verifing, that $p(t)$ is a solution to Hamilton's equations. Cleary the second of Hamilton's equation is satisfied

$$
\frac{d g}{d t}=\frac{\partial H}{\partial p}=\frac{P}{m}
$$

The phase space volume occupied by the system is indicated by luated
yellow area and is easily evaluated

$$
\Phi(u, v)=2 P_{0} L=2 L \sqrt{2 m u}
$$

Recall that the period of the motion is related to the phase space volume by

$$
\tau(u, v)=\frac{\partial \bar{\phi}}{\partial u}
$$

so

$$
\begin{aligned}
\tau & =2 L\left(\frac{1}{2} \sqrt{\frac{2 m}{u}}\right) \\
& =L \sqrt{\frac{2 m}{u}}
\end{aligned}
$$

This is equivalent to the result obtained by soluing Hamilton's equation

A direct evaluation of the partition function gives

$$
\begin{aligned}
\tau(u, v) & =\int_{0}^{L} S \delta\left[\frac{p^{2}}{2 m}-u\right] d q d p \\
& =L S \delta\left[\frac{p^{2}}{2 m}-u\right] d p
\end{aligned}
$$

A convient property of the Dirac Detta function useful in evaluation of the integral is

$$
\delta(g(x))=\sum_{i=1}^{n} \frac{1}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)
$$

where

$$
g\left(X_{i}\right)=0 \quad \forall i=1,2, \ldots, n
$$

Here

$$
\begin{aligned}
& g(p)=\frac{p^{2}}{2 m}-u \\
& g^{\prime}(p)=\frac{p}{m}
\end{aligned}
$$

so

$$
g\left(p_{0}\right)=0=\frac{p_{0}^{2}}{2 m}-u
$$

$$
\begin{aligned}
\Rightarrow & p_{0}= \pm \sqrt{2 m u} \\
& g^{\prime}\left(p_{0}\right)= \pm \sqrt{\frac{2 u}{m}}
\end{aligned}
$$

it follows that

$$
\delta\left[\frac{p^{2}}{2 m}-u\right]=\sqrt{\frac{m}{2 u}}\{\delta(p-\sqrt{2 m u})
$$

$$
+\delta(p+\sqrt{2 m u})\}
$$

Substitution into the integral gives

$$
\begin{aligned}
& \uparrow(u, L)=L \int \delta\left[\frac{p^{2}}{2 m}-u\right] d p \\
& =L \int \sqrt{\frac{m}{2 u}}\{\delta(p-\sqrt{2 m u})+\delta(p+\sqrt{2 m u})\} d p \\
& L \sqrt{\frac{m}{2 u}}(2)=L \sqrt{\frac{\partial m}{u}}
\end{aligned}
$$

In agreement with previous results,

$$
\tau(u, L)=L \sqrt{\frac{2 m}{u}}
$$

Now the average kinetic energy is given by

$$
\begin{aligned}
\langle k\rangle & =\frac{1}{\tau} \int_{0}^{\tau} k(t) d t \\
& =\frac{1}{\tau} \int_{0}^{\tau} \frac{p^{2}(t)}{2 m} d t \\
& =\frac{1}{2 m \tau}\left\{\int_{0}^{1 / 2 \tau}\left(p_{0}\right)^{2} d t+\int_{1 / 2 \tau}^{\tau}\left(-p_{0}^{2}\right) d t\right\} \\
& =\frac{p_{0}^{2}}{2 m \tau}\left\{\int_{0}^{1 / 2 \tau} d t+\int_{1 / 2 \tau}^{\tau} d t\right\} \\
& =\frac{p_{0}^{2}}{2 m} \\
& =\frac{(\sqrt{2 m} u)^{2}}{2 m} \\
& =u
\end{aligned}
$$

thus

$$
\langle k\rangle=u
$$

Consider

$$
\underline{\Phi}=2 L \sqrt{2 m u} \quad T=L \sqrt{\frac{2 m}{u}}
$$

SO

$$
\begin{aligned}
\frac{\Phi}{\tau} & =2 L \sqrt{\partial m u}\left(\frac{1}{L} \sqrt{\frac{u}{\partial m}}\right) \\
& =2 u=2\langle K\rangle
\end{aligned}
$$

By definition

$$
2\langle k\rangle=k_{B} T
$$

$\Sigma O$

$$
\frac{\Phi}{\tau}=k_{B} T
$$

This is in agreement with the general result previasly dotained.

Previously the Kinetic energy was computed as a time avorage here it is computed as an ensomble average

$$
\begin{aligned}
& k_{B} T=2\langle k\rangle=\frac{2}{\tau} \int_{0}^{v} \int \frac{p^{2}}{2 m} \delta\left[\frac{p^{2}}{2 m}-u\right] d p \\
& =\frac{2 L}{\tau} \int \frac{p^{2}}{2 m} \delta\left[\frac{p^{2}}{2 m}-u\right] d p
\end{aligned}
$$

it was previously shown that
$\delta\left[\frac{p^{2}}{2 m} \cdot u\right]=$

$$
\sqrt{\frac{m}{2 u}}\{\delta(p-\sqrt{2 m u})+\delta(p+\sqrt{2 m u})\}
$$

So

$$
\begin{aligned}
& \int \frac{p^{2}}{2 m} \delta\left[\frac{p^{2}}{2 m}-u\right] d p \\
= & \sqrt{\frac{m}{2 u}} \int \frac{p^{2}}{2 m}[\delta(p-\sqrt{2 m u})+\delta(p+\sqrt{2 m u})] d p \\
= & \sqrt{\frac{m}{2 u}} 2 \frac{(2 m u)}{2 m}=\sqrt{\frac{m}{2 u}} 2 u=\sqrt{2 u m}
\end{aligned}
$$

Bringing things together

$$
k_{B} T=\frac{2 L}{\tau} \sqrt{2 U_{m}}
$$

but

$$
\Phi=2 L \sqrt{2 m u}
$$

thus

$$
k_{B} T=\frac{\Phi}{\tau}
$$

Which is equivalent to the results obtained by computing the time average.

The pressure is defined by

$$
P(u, L)=\frac{-1}{\tau} \int_{0}^{\tau} \frac{\partial \Phi}{\partial L} d t
$$

Now

$$
q(q ; L)=4 u[1-\theta(q)+\theta(q-L)]
$$

So

$$
\begin{aligned}
-\frac{\partial Q}{\partial L} & =-4 u \delta(q-L) \\
\Rightarrow \quad \frac{\partial \varphi}{\partial L} & =4 u \delta(q-L)
\end{aligned}
$$

It follows that

$$
P(u, L)=\left\langle\frac{\partial \varphi}{\partial L}\right\rangle=\frac{\partial u}{\tau} \int_{0}^{\tau} \delta(q(t)-L) d t
$$

Recall the identity

$$
\begin{gathered}
\delta(f(x))=\frac{1}{\left|f^{\prime}\left(x_{0}\right)\right|} \delta\left(x-x_{0}\right) \\
f\left(x_{0}\right)=0
\end{gathered}
$$

To apply the identity here consider

$$
q(t)-L=0 \Rightarrow t=\frac{1}{2} \tau
$$

Now the left and right derivatives of $q(t)$ are not equal. The derivative from the right is

$$
\left.\frac{d c^{+}}{d t}\right|_{t=\frac{1}{2} \tau}=\frac{p_{0}}{m}
$$

and the left derivative is

$$
\left.\frac{d g}{d t}\right|_{t=\frac{1}{2} \uparrow}=-\frac{p_{s}}{m}
$$

but the absoulte calue of the derivative is continuous,

$$
\left|\frac{d a^{+}}{d t}\right|=\left|\frac{d a^{-}}{d t}\right|=\frac{P_{s}}{m}
$$

justifying its use in the identity. It follows that

$$
\delta(q(t)-L)=\frac{m}{p_{0}} \delta\left(t-\frac{1}{2} \tau\right)
$$

$$
\begin{aligned}
\text { so, } & \begin{aligned}
P(u, L)=\left\langle\frac{\partial \varphi}{\partial L}\right\rangle & =\frac{4 u}{\tau} \frac{m}{P_{0}} \int_{0}^{\tau} \delta(t-12 \tau) d t \\
& =\frac{4 u}{\tau} \frac{m}{P_{0}} \\
& =\frac{4 u}{P_{0}} m\left(\frac{1}{L} \sqrt{\frac{u}{2 m}}\right) \\
& =\frac{4 u}{\sqrt{2 m \varphi^{2}}} m\left(\frac{1}{L} \sqrt{\frac{u^{2}}{2 \eta^{2}}}\right) \\
& =\frac{4 u}{2 L} \\
& =\frac{2 u}{L}
\end{aligned}
\end{aligned}
$$

Recall that the time average force deduced from applying perfect rellection and momentum conservation at $q=L$ was shown to be

$$
\langle F\rangle=\frac{2 U}{L}
$$

In a single dimension the avarage force and presswe are equivalent.
which is equivalent to the result obt ined by differentration of the phase space volume.
Also, a previous general result obtained for ensemble averages relates the pressure to the phase space volume and period to the pressure,

$$
P=\frac{1}{\tau} \frac{\partial \Phi}{\partial L}
$$

Now bringing previous results together groes

$$
\begin{gathered}
\Phi=2 L \sqrt{2 m u} \quad T=L \sqrt{\frac{2 m}{u}} \\
P=\frac{2 u}{L}
\end{gathered}
$$

So

$$
\begin{aligned}
\frac{1}{\tau} \frac{\partial \Phi}{\partial L} & =\left(\frac{1}{L} \sqrt{\frac{U}{\partial m}}\right) 2 \sqrt{\partial m u} \\
& =\frac{\partial U}{L}=P
\end{aligned}
$$

Recall that the pressure is groen by

$$
P=\frac{2 U}{L}
$$

Now consider the work performed when increasing the size of the potential infitesimally from $L$ to $L+d L$ While maintaing the system temperature as show in the diagram

$$
|\stackrel{\bullet \overrightarrow{\mathrm{P}}(t)}{\longrightarrow} \quad \stackrel{\mid\langle F\rangle}{\longrightarrow}|
$$

This is equivalent to an isothermal expansion of a gas. The work done on the system is given by

$$
\delta \omega=-F d L
$$

Recall that

$$
u=\langle K\rangle=\frac{1}{2} k_{B} T
$$

thles an isothermal expansion conserves energy.
The entropy is given by

$$
S=S(u, L)=k_{B} \ln \Phi(u, L)
$$

where

$$
\frac{\partial S}{\partial u}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

Here the pressure is given by

$$
P=\langle F\rangle=\frac{\partial u}{L}
$$

The phase space volume is given by

$$
\Phi=\Phi(u, L)=2 L \sqrt{2 m u}
$$

so

$$
\delta=k_{B} \ln (2 L \sqrt{2 m U})
$$

This solution is verified as follows

$$
\begin{aligned}
\frac{\partial S}{\partial u} & =k_{B}(\sqrt{2 m u})\left(\frac{1}{2} \sqrt{\frac{2 m}{u}}\right) \\
& =k_{B}\left(\frac{1}{2 u}\right)=\frac{k_{B}}{\partial u}
\end{aligned}
$$

but

$$
u=\frac{1}{2} k_{B} T \Rightarrow \frac{1}{T}=\frac{k_{B}}{2 u}
$$

50

$$
\frac{\partial S}{\partial U}=\frac{1}{T}
$$

and

$$
\frac{\partial S}{\partial L}=k_{B}\left(\frac{1}{L}\right)=\frac{k_{B}}{L}
$$

but

$$
\frac{P}{T}=\left(\frac{\partial U}{L}\right)\left(\frac{k_{B}}{\partial U}\right)=\frac{k_{B}}{L}
$$

thus

$$
\frac{\partial S}{\partial L}=\frac{P}{T}
$$

An equation of state analogous to the ideal cas law can be found by considering the relation

$$
\frac{P}{T}=\frac{k_{B}}{L} \Rightarrow P L=k_{B} T
$$

To determine the relationship between the thermodynamic variables for the isothermal process can be determined by considering the neat equation

$$
\begin{aligned}
d s & =\frac{d u}{T}+\frac{P}{T} d L \\
\Rightarrow T d s & =d u+P d L
\end{aligned}
$$

Now

$$
P=\frac{2 U}{L} \quad U=\frac{1}{2} k_{B} T
$$

so for $T$ fixed $U$ is constant it is seen that

$$
P=\frac{k_{B} T}{L}
$$

and

$$
d u=0
$$

so

$$
\begin{aligned}
T d S & =\delta Q=P d L \\
& =\frac{k_{B} T}{L} d L
\end{aligned}
$$

This is stating that to maintain
the constant temperature $T$ during the process an amount of heat equal to the work petormed must be absorbed. It follows that the heat absorbed by the process is given by

$$
\begin{aligned}
Q & =\int_{L_{1}}^{L_{2}} \frac{k_{B} T}{L} d L \\
& =k_{B} T\left(\ln L_{2}-\ln L_{1}\right) \\
& =k_{m} T \ln \left(\frac{L_{2}}{L_{1}}\right)
\end{aligned}
$$

## Ideal Gas

An ideal gas is an extension of the 1 dimensional single particle in a box to an arbitrary number of particles confined to a volume $v$ by perfectly reflecting walls that only cause a change in a particles momentum and no change in energy.
Assume that the volume is a cube with sides of length $L$,

$$
V=L^{3}
$$

The model assumes that the particles do not interact with each other but only interact with the confining walls.

The system Hamittonian will have the form

$$
H(\bar{p}, \bar{q})=\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 m}+\varphi(\bar{q})=u
$$

where $\bar{p}$ and $\bar{q}$ are $3 N$ dimensional phase space vectors

$$
\bar{p}=\left(p_{1}, p_{2}, \ldots, p_{3 N}\right) \quad \bar{q}=\left(q_{1}, q_{2}, \ldots, q_{3 N}\right)
$$

$u$ is a fixed value of the system energy. The potentual function that confines the particles to the volume $v$ is given by

$$
\begin{aligned}
& \varphi(\bar{q} ; v)=\sum_{i=1}^{3 N} \varphi\left(q_{i} ; v\right) \\
& \varphi\left(q_{i} ; v\right)=\frac{4 u}{3 N}\left[1-\theta\left(q_{i}\right)+\theta\left(q_{i}-v^{1 / 3}\right)\right]
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-097.jpg?height=439&width=1001&top_left_y=757&top_left_x=189)

This potential is a limit of the previousky discussed u-shaped potential where the gradients are infinite and model perfecthy reflecting walls.
Since the particles do not interact Hamilton's equations for each coordinate are dentical to the equations obtained for the single particle system, namely,

Hamiltor's equations for each coordinate are given by,
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-098.jpg?height=521&width=1109&top_left_y=312&top_left_x=133)

$$
\dot{p}_{i}=-\frac{\partial H}{\partial q_{i}} \quad \dot{q}_{i}=\frac{\partial H}{\partial p_{i}}
$$

It follows that

$$
\begin{aligned}
& \dot{p}_{i}=-\frac{\partial \varphi}{\partial q_{i}}=(4 u)^{1 / 3 N}\left[\delta\left(q_{i}\right)-\delta\left(q_{i}-L\right)\right] \\
& \dot{q}_{i}=\frac{p_{i}}{m}
\end{aligned}
$$

The solution to these equations will be the same as obtained for the single particle case. The momentum is a periodic square wave
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-099.jpg?height=587&width=1213&top_left_y=68&top_left_x=120)

The postion as a function of time is given by the periodic triangular wave
![](https://cdn.mathpix.com/cropped/2025_09_16_e4f297b83a36f95d42b7g-099.jpg?height=481&width=1181&top_left_y=1025&top_left_x=133)

The system is modeled as $N$ non-interactin particles where each particle has a random constant phase shift. For $a_{i}$ single period $p_{i}(t)$ and

$$
\begin{aligned}
& p_{i}(t)=-p_{0}+2 p_{0} \theta\left(t+t_{i}\right)+2 p_{0} \theta\left(t+t_{i}-\frac{1}{2} \tau\right) \\
& q_{i}(t)=-\frac{p_{0}}{m} t+\frac{2 p_{0}}{m} R\left(t+t_{i}\right)-\frac{2 p_{0}}{m} R\left(t+t_{i}-\frac{1}{2} \tau\right)
\end{aligned}
$$

where $t_{i}$ is a constant and

$$
\tau=v^{1 / 3} \sqrt{\frac{6 m N}{u}} \quad p_{0}=\sqrt{\frac{2 m U}{3 N}}
$$

## Phase space volume

The phase space volume is defined by

$$
\begin{aligned}
\Phi(u, v) & =\iint_{H(\bar{q}, \bar{p} ; v) \leqslant u} d \Gamma \\
& =\iint \cdots \int \theta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
\end{aligned}
$$

The partition function is given

$$
\Omega=\frac{\partial \Phi}{\partial u}
$$

$$
\begin{aligned}
& \text { The temperature and pressure } \\
& \text { by } \\
& T=\frac{1}{k_{B}} \frac{\Phi}{\Omega} \quad \frac{1}{\Omega} \frac{\partial \Phi}{\partial V}=P
\end{aligned}
$$

The entropy is given by

$$
S=k_{B} \ln \Phi
$$

and

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

Now the phase space volume is given by

$$
\Phi(u v)=\iint \cdots \int \theta[u-H(\bar{q}, \bar{p} ; v)] d \Gamma
$$

Assuming that $0 \leqslant q_{i} \leqslant L$ and $p_{i}=0$ for $q_{i}<0$ and $q_{i}>L$.

$$
\begin{aligned}
\Phi(u v)= & \int_{0}^{L} \int_{0}^{L} \cdot S_{0}^{L} d q_{1} d q_{2} \cdots d q_{3} \\
& \iint \cdots S \theta\left[\sum_{i=1}^{3 N} \sum_{2 m}^{2} \leqslant u\right] d p_{1} d p_{2} \cdots d p_{2} \\
= & L^{3 N} S \int \cdots S \theta\left[\sum_{i=1}^{3 N} p_{i}^{2} \leqslant 2 m u\right] d p_{1} d p_{2} \cdots d p_{2}
\end{aligned}
$$

Now the momentum integral is the volume of a 30 dimensional hypersphere with radius $\sqrt{u}$.

The volume of an $n$-dimensional hypersphere of rodous $R$ is gruen by

$$
V_{n}(R)=\frac{\pi^{n / 2}}{\Gamma\left(\frac{n}{2}+1\right)} R^{n}
$$

where the Eamma function is defined by

$$
\Gamma(n+1)=\int_{0}^{\infty} x^{n} e^{-x} d x
$$

with

$$
R=\sqrt{2 m u}
$$

$$
\begin{aligned}
& \iint \cdots \int d \bar{p}=\frac{\pi^{3 N / 2}(2 m U)^{3 N / 2}}{\Gamma\left(\frac{3 N}{2}+1\right)} \\
& \sum_{i=1}^{3 N} p_{i}^{2} \leq 2 m U
\end{aligned}
$$

Putting things together gives

$$
\Phi=\frac{L^{3 N} \pi^{3 N / 2}(2 m)^{3 N / 2}}{\Gamma\left(\frac{3 N}{2}+1\right)} u^{3 N / 2}
$$

using

$$
V=L^{3}
$$

gives

$$
\Phi=v^{N} \frac{(2 m \pi u)^{3 N / 2}}{\Gamma\left(\frac{3 N}{2}+1\right)}
$$

For $1 \ll N$ sterling's Approximation can be used to approximate the gamma function

$$
\Gamma(n+1) \approx \sqrt{2 \pi n}\left(\frac{n}{e}\right)^{n}
$$

so

$$
\Gamma\left(\frac{3 N}{2}+1\right) \approx \sqrt{2 \pi\left(\frac{3 N}{2}\right)}\left(\frac{3 N}{2 e}\right)^{\frac{3 N}{2}}
$$

It follows that for $1 \ll N$ the phase space volume is given

$$
\begin{aligned}
\Phi & =v^{N}(2 m \pi u)^{3 N / 2} \frac{1}{\sqrt{3 \pi N}}\left(\frac{2 e}{3 N}\right)^{\frac{3 N}{2}} \\
& =v^{N}\left(\frac{4 m \pi}{3 N}\right)^{\frac{3 N}{2}} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}
\end{aligned}
$$

$$
=\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}
$$

Thus

$$
\Phi=\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}
$$

## Partition Function

Now the partition function is groen by

$$
\begin{aligned}
\Omega & =\frac{\partial \Phi}{\partial u} \\
& =\frac{\partial}{\partial u}\left\{\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}} u^{\frac{3 N}{2}}\right\} \\
& =\frac{3 N}{2} u^{\frac{3 N}{2}-1}\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}} \\
& =\frac{3 N}{2} \frac{1}{\sqrt{3 \pi N}}\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2} \\
& =\sqrt{\frac{9 N^{2}}{(4)(3) \pi N}}\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2}
\end{aligned}
$$

$$
\begin{aligned}
& =\sqrt{\frac{3 N}{4 \pi}}\left[V\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2} \\
& \Omega=\sqrt{\frac{3 N}{4 \pi}}\left[V\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2}
\end{aligned}
$$

Ensemble Average Temperature and Pressure

$$
\begin{aligned}
R_{B} T=\frac{\Phi}{\Omega} & =\frac{\left[v\left(\frac{4 / m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}}{\sqrt{\frac{3 N}{4 \pi}}\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2}} \\
& =\frac{u^{3 N / 2}}{\sqrt{\frac{3 N}{4 \pi}} u^{3 N / 2}-1} u^{7} u^{1-3 N / 2} \\
& =\sqrt{\frac{4 \pi^{2}}{3 N} \frac{1}{\sqrt{3 N N}}} u^{3 N / 2} \\
& =\frac{2 u}{3 N}
\end{aligned}
$$

Thus

$$
\begin{aligned}
& k_{B} T=\frac{2 U}{3 N} \\
\Rightarrow & u=\frac{3}{2} k_{B} N T
\end{aligned}
$$

Next consider

$$
\frac{1}{\Omega} \frac{\partial \Phi}{\partial V}=P
$$

Now

$$
\begin{aligned}
\frac{\partial \Phi}{\partial V} & =\frac{\partial}{\partial V}\left\{\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}\right\} \\
& =\frac{\partial}{\partial V}\left\{\left(\frac{4 m \pi}{3 N}\right)^{3 N / 2} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}} v^{N}\right\} \\
& =\left(\frac{4 m \pi}{3 N}\right)^{3 N / 2} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}} N v^{N-1}
\end{aligned}
$$

## and

$$
\begin{aligned}
\frac{1}{\Omega} \frac{\partial \Phi}{\partial V} & =\frac{\left(\frac{4 m \pi}{3 N}\right)^{3 N / 2} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}} N v^{N-1}}{\sqrt{\frac{3 N}{4 \pi}}\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{\frac{3 N}{2}-1} e^{3 N / 2}} \\
& =\frac{u^{3 N / 2} N v^{N-1}}{\sqrt{3 \pi N} v^{N} u^{3 N / 2-1}} \\
& =\frac{u^{3 N / 2}}{\sqrt{3 \pi N}} N v^{N-1} x^{-N} u^{1-3 N / 2} \sqrt{\frac{4 \pi}{3 N}} \\
& =\sqrt{\frac{4}{3 N}} \frac{1}{\sqrt{3 N}} N u v^{-1} \\
& =\frac{2}{3} \frac{u}{v}
\end{aligned}
$$

Thus

$$
P=\frac{2}{3} \frac{u}{v}
$$

but previously it was shown

$$
\begin{aligned}
u= & \frac{3}{2} k_{B} N T \\
\Rightarrow & \frac{2}{3} u=k_{B} N T
\end{aligned}
$$

So

$$
P V=\frac{2}{3} U=k_{B} N T
$$

which is the ideal gas law

$$
P V=k_{B} N T
$$

In summary for an $N$ particle system

$$
\begin{array}{r}
R_{B} T=\frac{\Phi}{\Omega}=\frac{\partial U}{3 N} \\
\frac{1}{\Omega} \frac{\partial \Phi}{\partial V}=P=\frac{2}{3} \frac{U}{V}
\end{array}
$$

combining these results gives the ideal gos law

$$
P V=k_{B} N T
$$

## Trme Averaged Kinetic Energy

The time averaged kinetic energy is defined by

$$
\langle K\rangle_{\tau}=\frac{1}{\tau} \int_{0}^{\tau} K(t) d t
$$

For an $N$ particle system the temperature is defined by

$$
k_{B} T=\frac{2}{3 N}\langle K\rangle_{\tau}
$$

This definition has the interpretation of temperature as a measure of the average kinetic energy per momentum coordinate or 14 equivalently the variance of the momentum coordinate.

Since the $p_{i}(t)$ terms are all periodic with perrod $\tau$ the time averaged Kinetic energy is given ba

$$
\begin{aligned}
\langle k\rangle_{\tau} & =\frac{1}{\tau} \int_{0}^{\tau} K(t) d t \\
& =\frac{1}{\tau} \int_{0}^{\tau} \sum_{i=1}^{3 N} \frac{P_{1}^{2}(t)}{2 m} d t
\end{aligned}
$$

$$
=\sum_{i=1}^{3 N} \frac{1}{\tau} \int_{0}^{\tau} \frac{P_{i}^{2}(t)}{2 m} d t
$$

Now $P_{i}^{2}(t)$ is a constant independent of the coordinate

$$
p_{i}^{2}(t)=p_{0}^{2}=\frac{2 m u}{3 N}
$$

so the integral becomes

$$
\begin{aligned}
\frac{1}{\tau} \int_{0}^{\tau} P_{\frac{i}{2 m}(t)}^{2} d t & =\frac{u}{3 N} \frac{1}{\tau} \int_{0}^{\tau} d t \\
& =\frac{u}{3 N}
\end{aligned}
$$

Thus the time averaged Kinetre energy is given by

$$
\langle K\rangle_{\tau}=\sum_{i=1}^{3 N} \frac{u}{3 N}=u
$$

The temperature is defined by

$$
k_{B} T=\frac{2}{3 N}\left\langle K_{T}\right\rangle=\frac{2 U}{3 N}
$$

## which is the same obtained from the ensemble average

Time Averaged Pressure

The pressure for an $N$ particle system is defined as the trme average of the derivative of the potential function

$$
P=-\left\langle\frac{\partial \phi}{\partial v}\right\rangle_{\uparrow}
$$

Now

$$
\varphi(\bar{q} ; v)=\sum_{i=1}^{3 N} \frac{4 u}{3 N}\left[1-\theta\left(q_{i}\right)+\theta\left(q_{i}-v^{1 / 3}\right)\right]
$$

It follows that

$$
\frac{\partial \varphi}{\partial v}=\frac{4 U}{3 N} \sum_{i=1}^{3 N} \frac{-1}{3 v^{2 / 3}} \delta\left(q_{i}-v^{1 / 3}\right)
$$

The $q_{i}(t)$ are all triangwar waves with phases offset by random constants and period

$$
\tau=v^{1 / 3} \sqrt{\frac{6 m N}{u}}
$$

It follows that

$$
\begin{aligned}
& P=-\left(\frac{\partial \varphi}{\partial V}\right)_{\tau}=-\frac{1}{\tau} \int_{0}^{\tau} \frac{\partial \varphi}{\partial V} d t \\
& =-\frac{1}{\tau} \int_{0}^{\tau} \frac{4 u}{3 N} \sum_{i=1}^{3 N} \frac{-1}{3 V^{2 / 3}} \delta\left(q_{i}-V^{1 / 3}\right) \\
& =\frac{1}{\tau} \frac{4 u}{3 N} \frac{1}{3 V^{2 / 3}} \sum_{i=1}^{3 N} \int_{0}^{\tau} \delta\left(q_{i}-V^{1 / 3}\right) d t
\end{aligned}
$$

Now consider the integral and let

$$
t^{\prime}=t+t_{i} \Rightarrow \quad d t^{\prime}=d t
$$

then

$$
\begin{aligned}
& \int_{0}^{\tau} \delta\left(q_{i}\left(t+t_{i}\right)-v^{1 / 3}\right) d t \\
= & \int_{t_{i}}^{\tau+t_{i}} \delta\left(q_{i}\left(t^{\prime}\right)-v^{1 / 3}\right) d t^{\prime}
\end{aligned}
$$

$$
=\int_{0}^{\tau} \delta\left(q_{i}\left(t^{\prime}\right)-v^{1 / 3}\right) d t^{\prime}
$$

The last step follows because $\varphi_{i}\left(t^{\prime}\right)$ is periodic with period $\tau$.

Recall the identity

$$
\delta(g(x))=\sum_{i=1}^{n} \frac{1}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)
$$

where

$$
g\left(x_{i}\right)=0
$$

Here

$$
g\left(x_{i}\right)=q_{i}\left(t^{\prime}\right)-v^{1 / 3}
$$

and

$$
g(1 / 2 \tau)=q_{i}(1 / 2 \tau)-v^{1 / 3}=0
$$

Now the left and right derivatives of $q\left(t^{\prime}\right)$ are not equal. The derivative from the right is

$$
\left.\frac{d c^{+}}{d t^{\prime}}\right|_{t^{\prime}=\frac{1}{2} \tau}=\frac{p_{0}}{m}
$$

and the left derivative is

$$
\left.\frac{d g^{-}}{d t^{\prime}}\right|_{t^{\prime}=\frac{1}{2} \uparrow}=-\frac{p_{s}}{m}
$$

but the absoulte calue of the derivative is continuous,

$$
\left|\frac{d g^{+}}{d t}\right|=\left|\frac{d g^{-}}{d t}\right|=\frac{P_{s}}{m}
$$

justifying its use in the identity. It follows that

$$
\begin{aligned}
& \delta\left(q\left(t^{\prime}\right)-v^{\prime} 3\right)=\frac{m}{p_{0}} \delta\left(t^{\prime}-\frac{1}{2} \tau\right) \\
& \int_{0}^{\tau} \delta\left(q_{i}\left(t^{\prime}\right)-v^{\prime / 3}\right) d t^{\prime} \\
&= \frac{m}{p_{0}} \int_{0}^{\tau} \delta\left(t^{\prime}-\frac{1}{2} \tau\right) d t^{\prime} \\
&= \frac{m}{p_{0}}
\end{aligned}
$$

and the pressure is given by

$$
\begin{aligned}
P & =\frac{1}{\tau} \frac{4 u}{3 N} \frac{1}{3 v^{2 / 3}} \sum_{i=1}^{3 N} \int_{0}^{\tau} \delta\left(q_{i}-v^{1 / 3}\right) d t \\
& =\frac{1}{\tau} \frac{4 u}{3 N} \frac{1}{3 v^{2 / 3}} \sum_{i=1}^{3 N} \frac{m}{p_{0}} \\
& =\frac{1}{\tau} \frac{4 u}{3 N} \frac{1}{3 v^{2 / 3}} 3 N \frac{m}{p_{0}} \\
& =\frac{1}{\tau} \frac{4 u}{3 v^{2 / 3}} \frac{m}{p_{0}}
\end{aligned}
$$

but

$$
\tau=v^{1 / 3} \sqrt{\frac{6 m N}{u}} \quad p_{0}=\sqrt{\frac{2 m U}{3 N}}
$$

and

$$
\begin{aligned}
P & =\left(\sqrt{\frac{b^{2}}{6 m s^{2}}} \frac{1}{v^{1 / 3}}\right) \frac{4 U}{3 v^{2 / 3}} m\left(\sqrt{\frac{3 A^{2}}{2 m l^{2}}}\right) \\
& =\sqrt{\frac{1}{2 m}}\left(\frac{1}{v^{1 / 3}}\right) \frac{4 U}{3 v^{2 / 3}} m\left(\sqrt{\frac{1}{2 m}}\right) \\
& =\frac{A R}{\operatorname{srn}}\left(\frac{A^{2} U}{3 v}\right)=\frac{2 U}{3 v}
\end{aligned}
$$

Thus

$$
P=\frac{2 u}{3 v}
$$

This result is equivalent to what was obtainge using an ensemble average calculation.

## Entropy

The entropy is given by

$$
S=S(u, v)=k_{B} \ln \Phi(u, v)
$$

where

$$
\frac{\partial S}{\partial u}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

The following results were obtained preciously

$$
\begin{aligned}
& R_{B} T=\frac{2 u}{3 N} \quad P=\frac{2}{3} \frac{u}{v} \\
& \Phi=\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}
\end{aligned}
$$

Now

$$
\begin{aligned}
S & =k_{B} \ln \Phi \\
& =k_{B} \ln \left\{\left[v\left(\frac{4 m \pi}{3 N}\right)^{3 / 2}\right]^{N} u^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}\right\} \\
& =k_{B} \ln \left\{v^{N} u^{3 N / 2}\left(\frac{4 m \pi}{3 N}\right)^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & k_{B} \ln \left(v^{N} u^{3 N / 2}\right) \\
& +k_{B} \ln \left\{\left(\frac{4 m \pi}{3 N}\right)^{3 N / 2} \frac{e^{3 N / 2}}{\sqrt{3 \pi N}}\right\}
\end{aligned}
$$

Thus

$$
\begin{array}{rl}
S=R_{B} & N \ln \left(v u^{3 / 2}\right) \\
& +R_{B} N \ln \left\{\left(\frac{4 m \pi}{3 N}\right)^{3 / 2} \frac{e^{3 / 2}}{\sqrt{3 \pi N}}\right\}
\end{array}
$$

Now

$$
\begin{aligned}
\frac{\partial S}{\partial u} & =k_{B} N \frac{3}{2} u^{1 / 2} \frac{1}{u^{3 / 2}} \\
& =\frac{3 k_{B} N}{2 u}
\end{aligned}
$$

but

$$
T=\frac{2 u}{3 k_{B} N}
$$

thus

$$
\frac{\partial S}{\partial U}=\frac{1}{T}
$$

Next consider

$$
\frac{\partial S}{\partial V}=\frac{k_{B} N}{V}
$$

but

$$
\begin{aligned}
\frac{P}{T} & =\left(\frac{3 k_{B} N}{2 a C}\right)\left(\frac{2}{3} \frac{\vec{u}}{v}\right) \\
& =\frac{k_{B} N}{v}
\end{aligned}
$$

thus

$$
\frac{\partial S}{\partial V}=\frac{P}{T}
$$

