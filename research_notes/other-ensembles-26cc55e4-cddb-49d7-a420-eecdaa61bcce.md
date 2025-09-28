Other Ensembles

Troy
Stribling
Feb. 24,2019

## Thermodynamic Potentials

Previously the microcanonical ensemble was described. The miorocanonical ensemble is assumed to conserve the system internal energy for fixed values of pouticle number and volume state of the system to be solated to a hyperswrface in phase space. It is further asswed that the state of the system at any given time is uniformhy distributed over this hypersurface resultins in the microcanonical distribution.

Other ensembles are constructed be assuming different conservation laws that result from considering couplings between two systems.
The different conservation laws are derived by application of the Legendre transform to the First

Law of Thermodynamics. Recall that the legendre transform of a function $f\left(u_{1}, u_{2}, \ldots, u_{n}\right)$ to a function $g\left(v_{1}, v_{2}, \ldots, v_{n}\right)$ is defined by

$$
g=\sum_{i=1}^{n} u_{i} v_{i}-f
$$

where

$$
v_{i}=\frac{\partial f}{\partial u_{i}}
$$

similarly

$$
f=\sum_{i=1}^{n} u_{i} v_{i}-g
$$

Now the First Law of Thermodynamics is given by

$$
d u=\delta Q \cdot P d v
$$

Consider the $\delta Q$ term. Previdusly it was shown that in general

$$
T d S \leqslant \delta Q
$$

For a quasistatic process equality holds and the first law can be writen as

$$
d u=T d S-P d V
$$

Previously an entropy function of the form

$$
s=s(u, v)
$$

was considered where

$$
d s=\frac{\partial s}{\partial u} d u+\frac{\partial s}{\partial v} d v
$$

for temperature $T$ and pressure P

$$
\frac{\partial S}{\partial U}=\frac{1}{T} \quad \frac{\partial S}{\partial V}=\frac{P}{T}
$$

If $s(u, v)$ is solved for $u$ an equation of the form

$$
u=u(s, v)
$$

is obtained. It follows that

$$
d u=\frac{\partial u}{\partial S} d S+\frac{\partial u}{\partial v} d v
$$

Comparing with the first law gives

$$
\frac{\partial u}{\partial S}=T \quad \frac{\partial u}{\partial v}=P
$$

For the microcanonical ensemble $d u=0$ since for all quasistic processes $d s=0$ and since $v$ and $N$ are fixed.

* The first caditional ensemble to be considered is the Canonical ensemble. The canonical ensemble assumes that $V$ and $T$ are fixed and that $u$ is not conserved.
To accomplish this a Legendre transform is applied to U(s, V) to produce a new potential function

$$
F=F(T, V)
$$

using

$$
T=\frac{\partial u}{\partial s}
$$

Applying the Legendre transform to $u(s, v)$ gives

$$
F=-(T S-U)=U-T S
$$

It follows that

$$
\begin{aligned}
d F & =d U-T d S-S d T \\
& =T d S-P d V-T d S-S d T \\
& =-P d V-S d T
\end{aligned}
$$

but

$$
d F=\frac{\partial F}{\partial T} d T+\frac{\partial F}{\partial V} d V
$$

so

$$
\frac{\partial F}{\partial T}=-S \quad \frac{\partial F}{\partial V}=-P
$$

It follows that for fixed $T$ and

$$
d F=0
$$

$F(T, V)$ is referred to as the Helmholtz Free Energy.

* The next ensemble considered is the isobaric ensemble. As the name suggests this ensemble has constant pressure. Additionally it is assumed that $s$ is fixed The desired potential
is obtained by apphing the legendre transform to $u(s, v)$ and making the change of variables

$$
P=-\frac{\partial U}{\partial V}
$$

to produce a new potential

$$
H=H(S, P)
$$

Applying the legendre transform to $u(s, v)$ gives

$$
H=U+P V
$$

So

$$
\begin{aligned}
d H & =d u+P d V+V d P \\
& =T d S-P d V+P B V+V d P \\
& =T d S+V d P
\end{aligned}
$$

but

$$
d t=\frac{\partial H}{\partial S} d S+\frac{\partial H}{\partial P} d P
$$

So

$$
\frac{\partial H}{\partial S}=T \quad \frac{\partial H}{\partial P}=V
$$

It follows that for fixed $S$ and V

$$
d H=0
$$

$H(S, P)$ is referred to as the Enthalply.
In physical experiments maintaing constant entropy is imprecticat. This motivates consideration of the isobaric-isothermal ensemble.

* The final ensemble considered is the isobaric-isothermal ensemble. As suggested by the name this ensemble has both constant pressure and temperature. The desired potential will have be a function of both temperature and pressure. Previously it was shown that the Helmholtz Frce Energy, $F(T, V)$. The desired potential is obtained by applying the legendre transform to $F(T, V)$ and making the change of variables.

$$
P=-\frac{\partial F}{\partial V}
$$

to produce a new potential

$$
G=G(T, P)
$$

Applying the legendre transform to $F(T, V)$ gives

$$
G=F+P V
$$

It follows that

$$
\begin{aligned}
d E & =d F+P d V+V d P \\
& =-P d V-S d T+P d V+V d P \\
& =-S d T+V d P
\end{aligned}
$$

Now

$$
d G=\frac{\partial G}{\partial T} d T+\frac{\partial G}{\partial P} d P
$$

So

$$
\frac{\partial E}{\partial T}=-S \quad \frac{\partial E}{\partial P}=V
$$

## Canonical Ensemble

Consider two systems with $N_{1}$ and $N_{2}$ particles, volumes $V_{1}$ and $V_{2}$ and energres $E_{1}$ and $E_{2}$ as shown in the figure below
![](https://cdn.mathpix.com/cropped/2025_09_14_fa26d1c751ba584f6ce3g-11.jpg?height=656&width=735&top_left_y=604&top_left_x=342)

Assume that

$$
\begin{array}{lll}
N_{2} & >N_{1} & v_{2} \gg v_{1}
\end{array} \quad u_{2} \gg u_{1}
$$

and that $N_{2}, N_{1}, V_{2}$ and $V_{1}$ are fixed but the systems can exchange energy while conseruing the
total energy. It is also assumed that both systems are in equilibrium at temperalure $T$. If the total energy is denoted by $u$, the total volume by $v$ and total particle number by N

$$
\begin{gathered}
u=u_{1}+u_{2} \\
v=v_{1}+v_{2} \quad N=N_{1}+N_{2}
\end{gathered}
$$

It follows that the Hamiltonian for the entire system is conserved and given by

$$
H(\bar{p}, \bar{q})=H_{1}\left(\bar{p}_{1}, \bar{q}_{1}\right)+H_{2}\left(\bar{p}_{2}, \bar{q}_{2}\right)
$$

where $H_{1}\left(\bar{p}_{1}, \bar{q}_{1}\right)$ and $H_{2}\left(\bar{p}_{2}, \bar{q}_{2}\right)$ are the system 1 and system 2 Hamiltonians respectively.
Recall that the miorocanonical phase space density is given by

$$
\rho(\bar{q}, \bar{p})=\frac{1}{\Omega} \delta[u-H(\bar{q}, \bar{p})]
$$

where $\bar{q}$ and $\bar{p}$ are $3 N$ dimensional vectors

$$
\begin{aligned}
& \bar{q}=\left(q_{1}, q_{2}, \ldots, q_{3 N}\right) \\
& \bar{p}=\left(p_{1}, p_{2}, \ldots, p_{3 N}\right)
\end{aligned}
$$

and $\Omega$ is the partition function which is given by

$$
\Omega=\iint \cdots \int \delta[u-H(\bar{q}, \bar{p})] d \Gamma
$$

where $d \Gamma$ is a phase space volume element given by

$$
d \Gamma=d q_{1} d q_{2} \cdots d q_{3 N} d p_{1} d p_{2} \cdots d p_{3 N}
$$

Here the phase space volume elements for systems 1 and 2 respectuely

$$
\begin{aligned}
& d \Gamma_{1}=d q_{1}^{1} d q_{2}^{1} \cdots d q_{3 N}^{1} d p_{1}^{1} d p_{2}^{1} \cdots d p_{3 N}^{1} \\
& d \Gamma_{2}=d q_{1}^{2} d q_{2}^{2} \cdots d q_{3 N}^{2} d p_{1}^{2} d p_{2}^{2} \cdots d p_{3 N}^{2}
\end{aligned}
$$

So

$$
d \Gamma=d \Gamma_{1} d \Gamma_{2}
$$

and

$$
H(\bar{q}, \bar{p})=H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)+H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)
$$

$$
\Omega(u, N, v)=
\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1} d \Gamma_{2}
$$

Consider the marginal distribution obtained by integrating over system I

$$
f\left(\bar{q}_{2}, \bar{p}_{2}\right)=\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}
$$

Now consider

$$
\ln f\left(\bar{q}_{2}, \bar{p}_{2}\right)=
\ln \left\{\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\}
$$

Since $E_{1} \gg E_{2}$ it follows that

$$
H_{1}\left(\bar{q}_{1}, \bar{P}_{1}\right) \gg H_{2}\left(\bar{q}_{2}, \bar{P}_{2}\right)
$$

Expanding the integral in a Taylor series to first order in $H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)$ about $H_{2}\left(\bar{q}, \bar{p}_{2}\right)=0$

$$
\begin{aligned}
\ln & \left\{f\left(\bar{q}_{2}, \bar{p}_{2}\right)\right\} \approx \ln \left\{\iint \ldots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right] d \Gamma_{1}\right\} \\
& +H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right) \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\{
\end{aligned}
$$

Now for the first term the integral can be evaluated to give

$$
\Omega_{1}\left(u, N_{1}, v_{1}\right)=\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right] d \Gamma_{1}
$$

but

$$
S=k \ln \Omega
$$

Let $S_{1}=S_{1}\left(N_{1}, V_{1} U\right)$ denote the entropy of the system I entropy at energy $u$. It follows that

$$
\begin{aligned}
& \ln \left\{\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right] d \Gamma_{1}\right\}=\ln \Omega_{1} \\
& =\frac{S_{1}}{R}
\end{aligned}
$$

Next consider the second integral

$$
\begin{aligned}
& \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \ln \{
\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)] d \Gamma_{1}\right\}\left.\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0}\\
&=\frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \ln \left[f\left(\bar{q}_{1}, \bar{p}_{2}\right)\right] \\
& =\frac{1}{f\left(\bar{q}_{2}, \bar{p}_{2}\right)} \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\left[f\left(\bar{q}_{1}, \bar{p}_{2}\right)\right] \\
& =\frac{1}{f\left(\bar{q}_{2}, \bar{p}_{2}\right)} \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\{
\end{aligned}
$$

$$
\left.\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\} \mid
$$

$$
H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0
$$

$$
\begin{aligned}
& =\frac{1}{f\left(\bar{q}_{2}, \bar{p}_{2}\right)} \iint \cdots \int \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\{ \\
& \left.\delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\}\left.\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0}
\end{aligned}
$$

Consider the integrand

$$
\begin{aligned}
& \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\left\{\delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right]\right\} \\
& =-\delta^{\prime}\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right]
\end{aligned}
$$

but consider

$$
\begin{aligned}
\frac{\partial}{\partial u} & \left\{\delta\left[u-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right]\right\} \\
& =\delta^{\prime}\left[u-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right]
\end{aligned}
$$

It follows that

$$
\begin{array}{r}
\frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}\left\{\delta\left[u-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right]\right\} \\
\quad=-\frac{\partial}{\partial u}\left\{\delta\left[u-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right]\right\}
\end{array}
$$

Putting the integral together gives

$$
\begin{aligned}
& \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \ln \{ \iint
\cdots \int \left. \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\}\left.\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0} \\
= & -\frac{\partial}{\partial u} \ln \left\{\iint \cdots \int
\delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\}\left.\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0} \\
= & -\frac{\partial}{\partial u} \ln\iint \cdots \int
& \left.\left.\delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right]\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0}\right\} \\
= & \left.-\frac{\partial}{\partial u} \ln \iint\ \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)\right] d \Gamma_{1}\right\} \\
= & -\frac{\partial}{\partial u} \ln \Omega_{1} \\
= &-\frac{\partial}{\partial u} \frac{S_{1}}{R}
\end{aligned}
$$

Recall that

$$
\frac{\partial S_{1}}{\partial U}=\frac{1}{T}
$$

Where both systems are assumed to have the same temperature $T$. It follows that

$$
\begin{aligned}
& \frac{\partial}{\partial H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \ln \{
& \left.\iint \cdots \int \delta\left[u-H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right] d \Gamma_{1}\right\}\left.\right|_{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)=0} \\
& \quad=-\frac{1}{k T}
\end{aligned}
$$

and finally the marginal distribution in system 2 phase space coordinates is given by

$$
\begin{aligned}
& \ln \left\{f\left(\bar{q}_{2}, \bar{p}_{2}\right)\right\}=\frac{S_{1}}{k}-\frac{H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}{k T} \\
\Rightarrow & f\left(\bar{q}_{2}, \bar{p}_{2}\right)=e^{s_{1} / k} e^{-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right) / k T}
\end{aligned}
$$

Now

$$
S_{1}=S_{1}\left(N_{1}, v_{1}, u\right)
$$

is a constant since $N_{1}, v_{1}$ and $u$ are assumed fixed. It follows that

$$
f\left(\bar{q}_{2}, \bar{p}_{2}\right) \propto e^{-H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right) / k T}
$$

which is the distribution in the system 2 phase space which is in equillibrium with system $I$ at temeperature $T$.
This result is true in general for a system in thermal equilibrium with a larger system. Thus

$$
f(\bar{q}, \bar{p}) \propto e^{-H(\bar{q}, \bar{p}) / k T}
$$

The normalization factor is given by the canonical ensemble partition function

$$
\begin{aligned}
Q(N, V, T) & =\iint \cdots \int f(\bar{q}, \bar{p}) d \Gamma \\
& =\iint \cdots \int e^{-H(\bar{q}, \bar{p}) / k T} d \Gamma
\end{aligned}
$$

Thus the normalized probability density is given by

$$
f(\bar{q}, \bar{p})=\frac{1}{Q(N, V, T)} e^{-H(\bar{q}, \bar{p}) / k T}
$$

The cansnical partition function, $Q$, and the microcanonical partition function, $\Omega$, can be related in the following manner. Consider
$e^{-H(\bar{q}, \bar{p}) / k T}=\int_{0}^{\infty} \delta[H(\bar{q}, \bar{p})-u] e^{-u / k T} d u$

It follows that

$$
\begin{aligned}
Q(N, V, T)&=\iint \cdots \int e^{-H(\bar{G}, \bar{P}) / k T} d \Gamma \\
&=\iint \cdots \int\left[\int_{0}^{\infty} \delta[H(\bar{q}, \bar{p})-u] e^{-u / k T} d u\right] d \Gamma \\
&=\int_{0}^{\infty} e^{-u / k T}\left\{\iint \cdots \int \delta[H(\bar{q}, \bar{p})-u] d \Gamma\right\} d u \\
\end{aligned}
$$

but the micocanonical partition function is defined by
\Omega(u, N, v)=\iint \cdots \int \delta[H(\bar{q}, \bar{p})-u] d \Gamma

$$
thus
$$

Q(T, N, v)=\int_{0}^{\infty} e^{-u \mid k T} \Omega(u, N, v) d u

\$\$

## Canonical Ensemble Average Energy

The total energy of a canonical ensemble system is not fixed but fluctuates. The average value of the total energy is given by the ensemble average of the Hamiltonian,
$u=\langle H(\bar{q}, \bar{p})\rangle=\frac{1}{Q(T, N, V)} \int S \cdot S H(\bar{q}, \bar{p}) e^{-H(\bar{q}, \bar{p}) / k T} d \Gamma$
let

$$
\beta=\frac{1}{R T}
$$

then

$$
Q(T, N, V)=\iint \cdots \int e^{-\beta H(\bar{a}, \bar{p})} d \Gamma
$$

Now

$$
\begin{aligned}
\frac{\partial Q}{\partial \beta} & =\frac{\partial}{\partial \beta}\left\{\iint \cdots \int e^{-\beta H(\bar{q}, \bar{p})} d \Gamma\right\} \\
& =\iint \cdots \int \frac{\partial}{\partial \beta} e^{-\beta H(\bar{q}, \bar{p})} d \Gamma \\
& =-\iint \cdots \int H(\bar{q}, \bar{p}) e^{-\beta H(\bar{q}, \bar{p})} d \Gamma
\end{aligned}
$$

It follows that

$$
\begin{aligned}
u & =\langle H\rangle=\frac{1}{Q} S S \cdots S H(\bar{q}, \bar{p}) e^{-H(\bar{q}, \bar{p}) / k T} d \Gamma \\
& =-\frac{1}{Q} \frac{\partial Q}{\partial \beta} \\
& =-\frac{\partial}{\partial \beta}(\ln Q) \\
\text { so } \quad u & =-\frac{\partial}{\partial \beta}(\ln Q)
\end{aligned}
$$

since

$$
\beta=\frac{1}{R T}
$$

it follows that

$$
\begin{aligned}
& \frac{\partial}{\partial T}[\ln Q(\beta(T))]=\frac{\partial}{\partial \beta}(\ln Q) \frac{\partial \beta}{\partial T} \\
= & -\frac{1}{k T^{2}}\left[\frac{\partial}{\partial \beta}(\ln Q)\right] \\
\Rightarrow & \frac{\partial}{\partial \beta}(\ln Q)=-k T^{2} \frac{\partial}{\partial T}(\ln Q)
\end{aligned}
$$

It follows that

$$
u=k T^{2} \frac{\partial}{\partial T}(\ln Q)
$$

## Thermodynamics of Canonical Ensemble

Recall that the Helmholtz Free energy is conserved for revesible thermodynamic processes with fixed temperature and volume. The Helmholtz free is defined by

$$
F=U-T S
$$

where

$$
d F=-(P d V+S d T)
$$

and

$$
\frac{\partial F}{\partial T}=-S \quad \frac{\partial F}{\partial V}=-P
$$

Previously it was shown that

$$
u=k T^{2} \frac{\partial}{\partial T}(\ln Q)
$$

Now

$$
F=U-T S=U+T \frac{\partial F}{\partial T}
$$

$$
\Rightarrow F-T \frac{\partial F}{\partial T}=u
$$

Consider the solution

$$
F=-k T \ln Q
$$

then

$$
\frac{\partial F}{\partial T}=-k \ln Q-k T \frac{\partial}{\partial T}(\ln Q)
$$

so

$$
\begin{aligned}
& F-T \frac{\partial F}{\partial T}=-k T \ln Q-T\left[-k \ln Q-k T \frac{\partial}{\partial \tau}(\ln Q)\right] \\
& =-k T \ln Q+T k \ln Q+k T^{2} \frac{\partial}{\partial T}(\ln Q) \\
& =k T^{2} \frac{\partial(\ln Q)}{\partial T}=U
\end{aligned}
$$

but

$$
U=k T^{2} \frac{\partial}{\partial T}(\ln Q)
$$

verifying that

$$
F=-k T \ln Q
$$

The entropy and pressure are given by

$$
\begin{aligned}
& S=-\frac{\partial F}{\partial T}=\frac{\partial}{\partial T}(R T \ln Q) \\
& =k \ln Q+k T \frac{\partial(\ln Q)}{\partial T}
\end{aligned}
$$

and

$$
\begin{aligned}
P & =-\frac{\partial F}{\partial V}=\frac{\partial}{\partial V}(k T \ln Q) \\
& =k T \frac{\partial}{\partial V}(\ln Q)
\end{aligned}
$$

In summary the realtionship of the thermodyramic variables to the microconical partition are given by

$$
\begin{aligned}
u & =k T^{2} \frac{\partial}{\partial T}(\ln Q) \\
& =\frac{k T^{2}}{Q} \frac{\partial Q}{\partial T}
\end{aligned}
$$

$$
F=-k T \ln Q
$$

$$
\begin{aligned}
S & =k \ln Q+k T \frac{\partial}{\partial T}(\ln Q) \\
& =k \ln Q+\frac{k T}{Q} \frac{\partial Q}{\partial T}
\end{aligned}
$$

$$
\begin{aligned}
P & =k T \frac{\partial}{\partial V}(\ln Q) \\
& =\frac{k T}{Q} \frac{\partial Q}{\partial V}
\end{aligned}
$$

## Canonical Ensemble Energy Fluctations

In the canonical ensemble enenergy is not conserved so the Hamittonian is not constant. Previously it was shown that the average energy is given by

$$
\begin{aligned}
\langle H(\bar{q}, \bar{p})\rangle & =u=k T^{2} \frac{\partial}{\partial T} \ln Q(T, N, V) \\
& =\frac{\partial}{\partial \beta} \ln Q(\beta, N, V)
\end{aligned}
$$

where the partition function is given by

$$
Q=Q(T, N, V)=S S \cdots S e^{-\beta H(\bar{q}, \bar{p})} d \Gamma
$$

The energy fluctuations are defined by the Hamiltonian standard deviation

$$
\begin{aligned}
\Delta u^{2} & =\left\langle[H(\bar{q}, \bar{p})-\langle H(\bar{q}, \bar{p})\rangle]^{2}\right\rangle \\
& =\left\langle H^{2}(\bar{q}, \bar{p})\right\rangle-\langle H(\bar{q}, \bar{p})\rangle^{2}
\end{aligned}
$$

Consider the first term

$$
\begin{aligned}
\left\langle H^{2}(\bar{q}, \bar{p})\right\rangle & =\frac{1}{Q(\beta, V, N)} \iint \cdots \int H^{2}(\bar{q}, \bar{p}) e^{-\beta H(\bar{p}, \bar{q})} d \Gamma \\
& =\frac{1}{Q(\beta, V, N)} \iint \cdots \int \frac{\partial^{2}}{\partial \beta^{2}} e^{-\beta H(\bar{p}, \bar{q})} d \Gamma \\
& =\frac{1}{Q(\beta, V, N)} \frac{\partial^{2}}{\partial \beta^{2}}\left\{\iint \cdots \int e^{-\beta H(\bar{p}, \bar{q})} d \Gamma\right\} \\
& =\frac{1}{Q(\beta, V, N)} \frac{\partial^{2}}{\partial \beta^{2}} Q(\beta, V, N)
\end{aligned}
$$

Now consider

$$
\begin{aligned}
& \frac{\partial^{2}}{\partial \beta^{2}} \ln Q(\beta, V, N)=\frac{\partial}{\partial \beta}\left\{\frac{1}{Q(\beta, V, N)} \frac{\partial Q(\beta, V, N)}{\partial \beta}\right\} \\
& =-\frac{1}{Q^{2}(\beta, V, N)} \frac{\partial Q}{\partial \beta}(\beta, V, N) \frac{\partial Q(\beta, V, N)}{\partial \beta} \\
& +\frac{1}{Q(\beta, V, N)} \frac{\partial^{2} Q(\beta, V, N)}{\partial^{2} \beta}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{Q(\beta, V, N)} \frac{\partial^{2} Q(\beta, V, N)}{\partial^{2} \beta} \\
& -\left[\frac{1}{Q(\beta, V, N)} \frac{\partial Q(\beta, V, N)}{\partial \beta}\right]^{2} \\
& =\frac{1}{Q(\beta, V, N)} \frac{\partial^{2} Q(\beta, V, N)}{\partial^{2} \beta}-\left[\frac{\partial \ln Q(\beta, V, N)}{\partial \beta}\right]^{2} \\
& =\left\langle H^{2}(\bar{G}, \bar{p})\right\rangle-\langle H(\bar{G}, \bar{p})\rangle^{2}
\end{aligned}
$$

Thus

$$
\Delta L^{2}=\frac{\partial^{2}}{\partial \beta^{2}} \ln Q(\beta, V, N)
$$

## Ideal Gas in Canonical Ensemble

Consider a free particle of mass $m$ moving in a single dimension of length $L$. The Hamiltonian is given by

$$
H(p, q)=\frac{p^{2}}{2 m}
$$

If the particle is in thermal equillibrium with a heat reservoir it can be modeled by the Canonical Ensemble. It follows that the canonical ensemble partition function

$$
\begin{aligned}
Q(L, T) & =\int_{0}^{L} \int_{-\infty}^{\infty} e^{-p^{2} / 2 m k T} d q d p \\
& =L \int_{-\infty}^{\infty} e^{-p^{2} / 2 k T} d p \\
& =L \sqrt{2 \pi m k T}
\end{aligned}
$$

If a three dimensional $N$ particle system is considered the Hamittonian
is given by

$$
H(\bar{p}, \bar{q})=\sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 m}
$$

Now let

$$
\begin{aligned}
& d q^{3 N}=d q_{1} d q_{2} \cdots d q_{3 N} \\
& d p^{3 N}=d p_{1} d p_{2} \cdots d p_{3 N}
\end{aligned}
$$

Then the partition function is given by

$$
\begin{aligned}
Q(N, L, T)= & \int_{0}^{L} d q^{3 N} \int \exp \left[-\frac{1}{2 m k T} \sum_{i=1}^{3 N} \frac{p_{i}^{2}}{2 m}\right] d p^{3 N} \\
=L^{3 N} & \int \exp \left(-\frac{1}{2 m k T} P_{1}^{2}\right) d p_{1} \\
& \int \exp \left(-\frac{1}{2 m k T} P_{2}^{2}\right) d P_{2} \\
& \int \exp \left(-\frac{1}{2 m k T} P_{3 N}^{2}\right) d P_{3 N} \\
=L^{3 N} & \left\{\int \exp \left(-\frac{1}{2 m k T} P^{2}\right) d p\right\}^{3 N} \\
=L^{3 N} & (\sqrt{2 \pi m k T})^{3 N}
\end{aligned}
$$

Now the three dimensional volume is given by

$$
V=L^{3}
$$

80

$$
Q(N, V, T)=V^{N}(2 \pi m k T)^{3 N / 2}
$$

The thermodyramics for the canonical ensemble is given by

$$
\begin{gathered}
F=-k T \ln Q \\
U=k T^{2} \frac{1}{Q} \frac{\partial Q}{\partial T} \\
S=k \ln Q+\frac{k T}{Q} \frac{\partial Q}{\partial T} \\
P=\frac{k T}{Q} \frac{\partial Q}{\partial V}
\end{gathered}
$$

So

$$
F=-k T \ln \left[V^{N}(2 \pi m k T)^{3 N / 2}\right]
$$

$$
=-k T N \ln V-\frac{3 N}{2} k T \ln (2 \pi m k T)
$$

The energy is given by

$$
\begin{aligned}
u & =\frac{k T^{2}}{x^{3 N}(2 \pi m k T)^{3 N / 2}} v^{N}(2 \pi m k)^{\frac{3 N}{2}}\left(\frac{3 N}{2}\right)^{T^{\frac{3 N}{2}-1}} \\
& =k T^{2}(T)^{-3 N / 2}\left(\frac{3 N}{2}\right) T^{\frac{3 N}{2}-1} \\
& =\frac{3 N}{2} k T
\end{aligned}
$$

The entropy is given by

$$
\begin{aligned}
s & =k N \ln V+\frac{3 N}{2} k \ln (2 \pi m k T) \\
1 & \frac{k T^{2}}{x^{N}(2 \pi n k T)^{3 N / 2}} V^{N^{2}}(2 \pi m k)^{\frac{3 N}{2}}\left(\frac{3 N}{2}\right)^{x^{\frac{3 N}{2}-1}} \\
& =k N \ln V+\frac{3 N}{2} k \ln (2 \pi m k T)+\frac{3 N k}{2}
\end{aligned}
$$

The pressure is given by

$$
\begin{aligned}
P & =\frac{k T}{V^{N}(2 \pi m k T)^{3 N / 2}} N V^{N-1}(2 \pi m k T)^{3 N / 2} \\
& =N k T V^{-1} \\
\Rightarrow P V & =N k T
\end{aligned}
$$

which is the ideal gas law.
In Summary

$$
\begin{gathered}
\frac{Q(N, V, T)}{F=-k T N \ln V-\frac{3 N}{2} k T \ln (2 \pi m k T)} \\
\frac{u=\frac{3 N}{2} k T}{\frac{5=k N \ln V+\frac{3 N}{2} k \ln (2 \pi m k T)+\frac{3 N k}{2}}{2 N / 2}} \\
\frac{S V}{P V}=N k T
\end{gathered}
$$

## Isobaric - Isothermal Ensembles

Consider two systems with coupled volumes as shown in the following diagram.
![](https://cdn.mathpix.com/cropped/2025_09_14_fa26d1c751ba584f6ce3g-38.jpg?height=603&width=809&top_left_y=532&top_left_x=342)

The Volume $v_{1}$ contains $N_{1}$ particles with energy $u_{1}$ and satisties Hamiltonian $H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)$ where the number of partrcles $N_{1}$, pressure $P$ and temperature $T$ are fixed. The volume $v_{2}$ contains $N_{2}$ particles with energy $u_{2}$ and satusfles Hamiltonian $\mathrm{H}_{2}\left(\bar{q}_{2}, \bar{P}_{2}\right)$ where the number of particles $N_{2}$ is fixed

A piston that moves without friction seperates volume $v_{1}$ from volume $v_{2}$ and maintains a constant pressure, $P$ in for both $v_{1}$ and $v_{2}$ so that the volumes are in mechanical equilibrium Additionalh the volumes are asswmed to be in thermal equilibrium so that both have a fixed temperature $T$. Also, it is assumed that both $V_{1}$ and $N_{1}$ are much larger than $V_{2}$ and $N_{2}$ so that

$$
\begin{array}{r}
V_{1} \gg V_{2} \quad N_{1} \gg N_{2} \quad U_{1} \gg U_{2} \\
H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right) \gg H\left(\bar{q}_{2}, \bar{p}_{2}\right) \quad \forall \quad \text { and } \bar{p}
\end{array}
$$

The thermodynamic parameters that can change are assumed to satisfy

$$
v=v_{1}+v_{2} \quad u=u_{1}+u_{2}
$$

$$
H\left(\bar{q}_{1}, \bar{q}_{2}, \bar{p}_{1}, \bar{p}_{2}\right)=H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)+H\left(\bar{q}_{2}, \bar{p}_{2}\right)
$$

Begin by assumins that $V_{1}$ and $v_{2}$ are fixed so that the combined system is in thermal equilibruim at temperature $T$. It follows that the combined system is described by the canonical ensemble.
It follows that the partition function for the entire system is given by

$$
\begin{aligned}
& Q(T, N, V)=\iint \cdots S e^{-\beta H\left(\bar{q}_{1}, \bar{p}_{1}, \bar{q}_{2}, \bar{p}_{2}\right)} d r_{1} d r_{2} \\
& =\iint \cdots \int e^{\left.-\beta\left[H_{1}\left(\bar{q}_{1}\right), \bar{p}_{1}\right)+H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)\right]} d r_{2} d r_{2} \\
& =\iint \cdot \int e^{-\beta H\left(\bar{q}_{1}, \bar{p}_{1}\right)} d r_{1} \iint \cdots \int e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} d r_{2} \\
& =Q_{1}\left(T, N_{1}, V_{1}\right) Q_{2}\left(T, N_{2}, V_{2}\right)
\end{aligned}
$$

where $\beta=1 / k T$
Thus for fixed $v_{1}$ and $v_{2}$

$$
Q(T, N, V)=Q_{1}\left(T, N_{1}, V_{1}\right) Q_{2}\left(T, N_{2}, V_{2}\right)
$$

To determine the partition function for the case where $v_{1}$ and $v_{2}$ can vary while satisfying the relation

$$
\begin{aligned}
& V_{1}+V_{2}=V \\
\Rightarrow & V_{1}=V-V_{2}
\end{aligned}
$$

the canonical ensemble must be integrated over all values of $V_{1}$ and $V_{2}$. Thus

$$
Q(N, V, T)=\int_{0}^{V} Q_{1}\left(N_{1}, V-V_{2}, T\right) Q_{2}\left(N_{2}, V_{2}, T\right) d V_{2}
$$

It follows that the phase space density function for the combined system is given by

$$
f\left(\bar{q}_{1}, \bar{p}_{1}, \bar{q}_{2}, \bar{p}_{2}\right)=\frac{e^{-\beta H\left(\left(\bar{q}_{1}, \bar{p}_{1}, \bar{q}_{2}, \bar{p}_{2}\right)\right.}}{Q(N, V, T)}
$$

The marginal distribution for system 2 as a function of the volume $v_{2}$ is obtained from

$$
\begin{aligned}
& f\left(\bar{q}_{1}, \bar{p}_{1}, \bar{q}_{2}, \bar{p}_{2}\right) \text { as follows, } \\
& f\left(\bar{q}_{2}, \bar{p}_{2}, V_{2}\right)=\iint \cdots \int f\left(\bar{q}_{1}, \bar{p}_{1}, \bar{q}_{2}, \bar{p}_{2}\right) d \Gamma_{1} \\
& =\frac{1}{Q\left(N_{1}, V_{1} T\right)} \iint \cdots \int e^{-\beta H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} d \Gamma_{1} \\
& =\frac{1}{Q\left(N_{1}, T\right)} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \iint \cdots \int e^{-\beta H_{1}\left(\bar{q}_{1}, \bar{p}_{1}\right)} d \Gamma_{1} \\
& =\frac{Q_{1}\left(N_{1}, V_{1}, T\right)}{Q(N, V, T)} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \\
& =\frac{Q_{1}\left(N-N_{2}, V-V_{2}, T\right)}{Q\left(N, V_{1} T\right)} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}
\end{aligned}
$$

Now for fixed values of $U$ and $U_{2} Q\left(N-N_{2} V-V_{2}, T\right)$ and $Q(N, V, T)$ are partion functions for canonical ensembles. Previously it was shown that for the caronical enseforble the partion function and Helmholtz Free energy are related by

$$
\begin{gathered}
F(N, V, T)=-k T \ln Q(N, V, T) \\
=-\frac{1}{\beta} \ln Q(N, V, T) \\
\Rightarrow Q(N, V, T)=e^{-\beta F(N, V, T)}
\end{gathered}
$$

It follows that

$$
\frac{Q_{1}\left(N-N_{2}, V-V_{2}, T\right)}{Q(N, V, T)} \frac{e^{-\beta F\left(N-N_{2}, V-V_{2}, T\right)}}{e^{-\beta F(N, V, T)}}
=e^{-\beta\left[F\left(N-N_{2}, V-V_{2}, T\right)-F(N, V, T)\right]}
$$

Recall that $v \gg v_{2}$ and $N \gg N_{2}$ so $F\left(N-N_{2}, V-V_{2}, T\right)$ can be approximated to first order by a Taylor series expansion about $v_{2}=0$ and $v_{2}=0$ so

$$
\begin{aligned}
& F\left(N-N_{2}, V-V_{2}, T\right) \approx F(N, V, T) \\
& -\left.N_{2} \frac{\partial F}{\partial N}\right|_{V_{2}=0}-\left.V_{2} \frac{\partial F}{\partial V}\right|_{V_{2}=0}
\end{aligned}
$$

but

$$
\frac{\partial F}{\partial V}=-P \quad \frac{\partial F}{\partial N}=M
$$

where $P$ is the pressure and $\mu$ the chemical potentral. The chemical potential is used to model energy changes due to change in particle number, which typically occur through chemical reactions. Here it is assumed that $\mathrm{N}_{2}$ is fixed so the chemical potential term is constant producing no changes in the Helmholtz free energy and does not contribute to system thermodynamics.

$$
F\left(N-N_{2}, V-V_{2}, T\right)-F\left(N, V_{1} T\right) \approx-\mu N_{2}+P V_{2}
$$

So

$$
\begin{aligned}
\frac{Q_{1}\left(N-N_{2}, V-V_{2}, T\right)}{Q\left(N_{1}, V, T\right)} & =e^{-\beta\left[F\left(N-N_{2}, V-V_{2}, T\right)-F(N, V, T)\right]} \\
& =e^{-\beta\left(P V_{2}-\mu N_{2}\right)} \\
& =e^{-\beta P V_{2}} e^{B \mu N_{2}}
\end{aligned}
$$

It follows that the phase space probability density is given by

$$
\begin{aligned}
f\left(\bar{q}_{2}, \bar{p}_{2}, V_{2}\right) & =\frac{Q_{1}\left(N-N_{2}, V-V_{2}, T\right)}{Q\left(N, V_{1} T\right)} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)} \\
& =e^{-\beta P V_{2}} e^{B \mu N_{2}} e^{-\beta H_{2}\left(\bar{q}_{2}, \bar{p}_{2}\right)}
\end{aligned}
$$

$f\left(\bar{q}_{2}, \bar{P}_{2}, v_{2}\right)$ now depends only on system 2 parameters so the syslem identifier can be dropped.

$$
\begin{aligned}
& f(\bar{q}, \bar{p}, v)=e^{\beta \mu N} e^{-\beta[H(\bar{q}, \bar{p})+P V]} \\
\Rightarrow & e^{-\beta \mu N} f(\bar{q}, \bar{p}, v)=e^{-\beta[H(\bar{q}, \bar{p})+P V]}
\end{aligned}
$$

This relationship defines a mi orocanonical ensemble with fixed $V$ and $N$. The isobaric-isothermal ensemble
partition function is obtained by Keeping $N$ fixed and integrating over values of $U$, Here it will be furthure assumed that $v \rightarrow \infty$ which models a system with a fluctuating volume and energy in thermal and isobanc equilibrium with an arbitrarily reservoir.
Integrating and taking limit $v \rightarrow \infty$ gives

$$
\begin{aligned}
& e^{-\beta \mu N} \int_{0}^{\infty} \int f(\bar{q}, \bar{p}, v) d v d \Gamma \\
& =\int_{0}^{\infty} \int e^{-\beta[H(\bar{q}, \bar{p})+P v]} d v d \Gamma
\end{aligned}
$$

The isobaric-isothermal ensemble partition function is defined by

$$
\Delta(N, P, T)=\int_{0}^{\infty} \int e^{-\beta[H(\bar{q}, \bar{p})+P V]} d V d \Gamma
$$

$\Delta(N, P, T)$ has a form similar to the canonical ensemble where the Hamiltonian, which defines
the instantaneous energy, with the instantaneous enthalpy

$$
H=H(\bar{q}, \bar{p})+P V
$$

Recall that the isothermal, canonical ensemble, partition function is defined by

$$
Q\left(N, v_{1} T\right)=\int e^{-\beta H(\bar{q}, \bar{p})} d \Gamma
$$

thes the isobaric-isothermal partition function is related to the canonical ensemble $m$ the following manner

$$
\Delta(N, P, T)=\int_{0}^{\infty} e^{-\beta V P} Q(N, V, T) d V
$$

Furthur realize that the canonical ensemble partition function is related to the microcanonical partition function by

$$
\Omega(N, V, u)
$$ by

$$
\Omega(N, v, u)=\iint \cdots \int \delta[H(\bar{q}, \bar{\varphi})-u] d \Gamma
$$

thus

$$
Q(N, V, T)=\int_{0}^{\infty} e^{-B u} \Omega(N, V, u) d u
$$

so finally

$$
\begin{aligned}
\Delta(N, P, T)&=\int_{0}^{\infty} \int_{0}^{\infty} e^{-\beta(u+v P)} \Omega(N, v, u) d u d  \\
&=\int_{0}^{\infty} \int_{0}^{\infty} \int e^{-B(u+v p)} \delta[H(\bar{q}, \bar{p})-u] d u d v d \Gamma \\
&=\int_{0}^{\infty} \int_{0}^{\infty} \int e^{-(u+v P) / k T} \delta[H(\bar{q}, \bar{p})-u] d u d v d \Gamma
\end{aligned}
$$

## Average Enthalpy in IsobaricIsothermal Ensemble

The Enthalpy is defined by

$$
H=u+P v
$$

While the enthalpy is conserved for the isobaric ensemble it fluctuates in the isobaric-isothermal ensemble. The avorage enthalpy is important in the thermodynamics of the isobaric-1sothermal ensemble and is define by

$$
\begin{aligned}
\langle H\rangle & =\langle U+P V\rangle \\
& =\langle H(\bar{q}, \bar{p})+P V\rangle
\end{aligned}
$$

where use was made of

$$
H(\bar{q}, \bar{p})=u
$$

Now

$$
\begin{aligned}
& \langle H(\bar{q}, \bar{p})+P V\rangle \\
& =\frac{\int_{0}^{\infty} \int[H(\bar{q}, \bar{p})+P V] e^{-\beta[H(\bar{q}, \bar{p})+P V]} d V d \Gamma}{\Delta(N, P, \beta)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-1}{\Delta(N, P, T)} \frac{\partial}{\partial \beta} \Delta(N, P, \beta) \\
& =-\frac{\partial}{\partial \beta} \ln \Delta(N, P, T) \\
& \text { since } \quad \beta=\frac{1}{k T} \\
& \frac{\partial}{\partial T} \ln \Delta(N, P, \beta(T))=\frac{\partial}{\partial \beta} \ln \Delta(N, P, \beta(T)) \frac{\partial \beta}{\partial T} \\
& =-\frac{1}{k T^{2}} \frac{\partial}{\partial \beta} \ln \Delta(N, P, \beta) \\
& \Rightarrow \frac{\partial}{\partial \beta} \ln \Delta(N, P, \beta)=-k T^{2} \frac{\partial}{\partial T} \ln \Delta(N, P, T)
\end{aligned}
$$

Thus

$$
\langle H\rangle=k T^{2} \frac{\partial}{\partial T} \ln \Delta(N, P, T)
$$

## Isobaric - Isothermal Ensemble Thermodynamics

The Gibbs Free Energy is conserved for a quasistatic thermodynamic process that has a fixed temperature and pressure. The Gibbs Free Energy is defined by

$$
G=F-P V
$$

where

$$
d G=\frac{\partial G}{\partial T} d T+\frac{\partial G}{\partial P} d P
$$

so

$$
\frac{\partial G}{\partial T}=-S \quad \frac{\partial G}{\partial P}=V
$$

and $F$ is the Helmholtz Free Energy which is defined by

$$
F=U-T S
$$

A differential equation for the Gibbs Free Energy in the following manner

$$
\begin{aligned}
G & =F+P V \\
& =u-T S+P V \\
& =u+P V+T \frac{\partial E}{\partial T}
\end{aligned}
$$

For the isobaric-isothermal ensemble $G$ is conserved, $P$ and $T$ are
fixed and $u$ and $v$ fluctuate, so thermodynamically their ensemble average is considered. Previously it was shown that the average enthalpy was given by

$$
\langle H\rangle=\langle U+P V\rangle=k T^{2} \frac{\partial}{\partial T} \ln \Delta(N, P, T)
$$

so

$$
G-T \frac{\partial G}{\partial T}=u+P v
$$

Consider the solution

$$
G=-k T \ln \Delta(N, P, T)
$$

It follows that

$$
\frac{\partial G}{\partial T}=-k \ln \Delta(N, P, T)-k T \frac{\partial}{\partial T} \ln \Delta(N, P, T)
$$

substitution into the differential equation for $G$ gives

$$
\begin{aligned}
G-\frac{T \partial G}{\partial T}= & -k T \ln \bar{\Delta}(N, P, T) \\
+ & k \ln \bar{\Delta}(N, P, T)+k T \frac{\partial}{\partial T} \ln \Delta(N, P, T) \\
= & k T \frac{\partial}{\partial T} \ln \Delta(N, P, T)
\end{aligned}
$$

This is the same result as obtained by direct calculation of the ensembe averaged enthalpy
Thus

$$
G=-k T \ln \Delta(N, P, T)
$$

The thermodynamic variables of the isobaric-isothermic ensemple are given by,

$$
\begin{aligned}
V & =\frac{\partial G}{\partial P}=-\frac{\partial}{\partial P}[k T \ln \Delta(N, P, T)] \\
& =-k T \frac{\partial}{\partial P}[\ln \Delta(N, P, T)] \\
& =\frac{-k T}{\Delta(N, P, T)} \frac{\partial}{\partial P} \Delta(N, P, T)
\end{aligned}
$$

and

$$
\begin{array}{r}
S=-\frac{\partial G}{\partial T}=\frac{\partial}{\partial T}[k T \ln \Delta(N, P, T)] \\
=k \ln \Delta(N, P, T)+\frac{k T}{\Delta(N, P, T)} \frac{\partial}{\partial T} \Delta(N, P, T)
\end{array}
$$

In summary

$$
\begin{gathered}
\langle H\rangle=\langle H(\bar{q}, \bar{P})+P V\rangle=k T^{2} \frac{\partial}{\partial T} \ln \Delta(N, P, T) \\
\frac{G(N, P, T)}{\partial(N, P, T)} \\
V(N, P, T)=\frac{-k T}{\Delta(N, P, T)} \frac{\partial}{\partial P} \Delta(N, P, T) \\
S(N, P, T)=k \ln \Delta(N, P, T)+\frac{k T}{\Delta(N, P, T)} \frac{\partial}{\partial T} \Delta(N, P, T)
\end{gathered}
$$

## Ideal Gas in Isobaric-Isothermal

## Ensemble

Recall that the Isobaric-Isothermal portition function is related to canonical partition function by

$$
\Delta(N, P, T)=\int_{0}^{\infty} e^{-V P / k T} Q(N, V, T) d V
$$

For a system of $N$ particles in three dimension in the canonical ensemble it was previously shown that the partition function is given by

$$
Q(N, V, T)=V^{N}(2 \pi m k T)^{3 N / 2}
$$

It follows that

$$
\begin{gathered}
\Delta(N, P, T)=\int_{0}^{\infty} e^{-V P / k T} V^{N}(2 \pi m k T)^{3 N / 2} d V \\
=(2 \pi m k T)^{3 N / 2} \int_{0}^{\infty} V^{N} e^{-V P / k T} d V
\end{gathered}
$$

Consider the integral and let

$$
\begin{array}{r}
\alpha=\frac{V P}{k T} \Rightarrow V=\frac{\alpha k T}{P} \\
d \alpha=\frac{P}{k T} d V \Rightarrow d V=\frac{k T}{P} d \alpha
\end{array}
$$

then

$$
\begin{aligned}
& \int_{0}^{\infty} v^{N} e^{-v P / k T} d v \\
= & \int_{0}^{\infty}\left(\frac{\alpha k T}{P}\right)^{N} e^{-\alpha}\left(\frac{k T}{P}\right) d \alpha \\
= & \left(\frac{k T}{P}\right)^{N+1} \int_{0}^{\infty} \alpha^{N} e^{-\alpha} d \alpha
\end{aligned}
$$

Recall that the Camma function is defined by

$$
\Gamma(n)=\int_{0}^{\infty} x^{n-1} e^{-x} d x
$$

which is related to the factorial
function by

$$
n!=\Gamma(n+1)=\int_{0}^{\infty} x^{n} e^{-x} d x
$$

It follows that

$$
\begin{aligned}
& \int_{0}^{\infty} V^{N} e^{-V P / k T} d V=\left(\frac{k T}{P}\right)^{N+1} \int_{0}^{\infty} \alpha^{N} e^{-\alpha} d \alpha \\
& =\left(\frac{k T}{D}\right)^{N+1} N!
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
\Delta(N, P, T) & =(2 \pi m k T)^{3 N / 2} \int_{0}^{\infty} V^{N} e^{-V P / k T} d V \\
& =(2 \pi m k T)^{3 N / 2}\left(\frac{k T}{D}\right)^{N+1} N!
\end{aligned}
$$

thus

$$
\Delta(N, P, T)=(2 \pi m k T)^{3 N / 2}\left(\frac{k T}{P}\right)^{N+1} N!
$$

Recall that the thermodynamics of the isobaric-isothermal ensemble
is given by

$$
\begin{aligned}
& H(N, P, T)=\frac{k T^{2}}{\Delta(N, P, T)} \frac{\partial}{\partial T} \Delta(N, P, T) \\
& G(N, P, T)=-k T \ln \Delta(N, P, T)
\end{aligned}
$$

$$
\begin{gathered}
V(N, P, T)=-\frac{k T}{\Delta(N, P, T)} \frac{\partial}{\partial P} \Delta(N, P, T) \\
S(N, P, T)=k \ln \Delta(N, P, T)+\frac{k T}{\Delta(N, P, T)} \frac{\partial}{\partial T} \Delta(N, P, T) \\
U(N, P, T)=H(N, P, T)-P(N, P, T) V(N, P, T)
\end{gathered}
$$

using

$$
\Delta(N, P, T)=(2 \pi m k T)^{3 N / 2}\left(\frac{k T}{P}\right)^{N+1} N!
$$

gives

$$
\begin{aligned}
& H=k T^{2} \frac{\partial}{\partial T} \ln \Delta \\
& =k T^{2} \frac{\partial}{\partial T} \ln \left[(2 \pi m k T)^{3 N / 2}\left(\frac{k T}{P}\right)^{N+1} N!\right] \\
& =k T^{2} \frac{\partial}{\partial T}\left\{\frac{3 N}{2} \ln (2 \pi m k T)\right. \\
& +(N+1) \ln \left(\frac{k T}{P}\right)+\ln N! \\
& =k T^{2}\left\{\frac{3 N}{2} \frac{1}{T}+(N+1) \frac{1}{T}\right\} \\
& =k T\left(\frac{3 N}{2}+N+1\right)
\end{aligned}
$$

Since $N \gg 1$

$$
H=\frac{5}{2} k T N
$$

Next the Gilabs Free Energy is given by

$$
\begin{aligned}
G= & -k T \ln \Delta \\
= & -k T\left\{\frac{3 N}{2} \ln (2 \pi m k T)\right. \\
& \left.+(N+1) \ln \left(\frac{k T}{P}\right)+\ln N!\right\}
\end{aligned}
$$

The volume is given by

$$
\begin{aligned}
& V=\frac{-k T}{\Delta} \frac{\partial \Delta}{\partial P} \\
= & \frac{-k T}{(2 \pi m k T)^{3 N / 2}\left(\frac{k T}{P}\right)^{N+1} N+7} \\
& (2 \pi m k T)^{3 N / 2} N!(k T)^{N+1} \frac{\partial}{\partial P}\left(\frac{1}{P}\right)^{N+1} \\
= & -k T\left(\frac{1}{P}\right)^{-N-1} \frac{\partial}{\partial P}\left(\frac{1}{P}\right)^{N+1} \\
= & -k T\left(\frac{1}{P}\right)^{-(N+1)} \frac{\partial}{\partial P} P^{-(N+1)} \\
= & -k T P^{N+1}(-(N+1)) P^{-(N+1)-1} \\
= &\ (N+1) \frac{k T}{P}
\end{aligned}
$$

summarizing

$$
\begin{aligned}
V & =(N+1) \frac{k T}{P} \\
\Rightarrow P V & =(N+1) k T
\end{aligned}
$$

since $N \gg 1$

$$
P V=N R T
$$

which is the ideal gas law. The ideal gas law has thus far been obtained in four different statisical models

1. Microcanonical ensemble
2. Time average of periodic function madeling partale in a box
3. Canonical ensembe
4. Isobaric - Isothermal ensemble

The entropy is given by

$$
\begin{aligned}
& S(N, P, T)=k \ln \Delta(N, P, T)+\frac{k T}{\Delta(N, P, T)} \frac{\partial}{\partial T} \Delta(N, P, T) \\
&= \frac{3 N}{2} \ln (2 \pi m k T)+(N+1) \ln \left(\frac{k T}{P}\right) \\
&+\ln N!+k T\left\{\frac{3 N}{2} \frac{1}{T}+(N+1) \frac{1}{T}\right\} \\
&= \frac{3 N}{2} k \ln (2 \pi m k T)+k(N+1) \ln \left(\frac{k T}{P}\right) \\
&+k \ln N!+\frac{5}{2} k N+k
\end{aligned}
$$

And finally the internal energy

$$
\begin{aligned}
U(N, P, T) & =H(N, P, T)-P(N, P, T) V(N, P, T) \\
& =\frac{5}{2} k T N-N k T \\
& =\frac{3}{2} N k T
\end{aligned}
$$

which is the well known result for an ideal gas
In summary

$$
\begin{aligned}
H & =\frac{5}{2} k T N \\
G=- & k T\left\{\frac{3 N}{2} \ln (2 \pi m k T)\right. \\
& \left.+(N+1) \ln \left(\frac{k T}{P}\right)+\ln N^{1}\right\}
\end{aligned}
$$

$$
\begin{aligned}
S= & \frac{3 N}{2} k \ln (2 \pi m k T)+k(N+1) \ln \left(\frac{k T}{P}\right) \\
& +k \ln N!+\frac{5}{2} k N+k
\end{aligned}
$$

$$
\begin{aligned}
& P V=N k T \\
& U=\frac{3}{2} N k T
\end{aligned}
$$

