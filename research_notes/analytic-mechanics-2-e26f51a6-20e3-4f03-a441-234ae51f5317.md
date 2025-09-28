Analytic Mechanics

Troy Stribling
Now. 12, 2018

## Kinematics

![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-002.jpg?height=820&width=834&top_left_y=222&top_left_x=328)

Consider a point mass, i.e a mass which has no spatial extent, located at a point in space specified by the vector $\vec{r}$.
The velocity and acceleration of the particle is given by

$$
\bar{v}=\frac{d \bar{r}}{d t} \quad \bar{a}=\frac{d \bar{v}}{d t}=\frac{d^{2} \bar{r}}{d t}
$$

Consider an acceleration that acts only in the $\hat{x}$ direction given by

$$
\bar{a}=-\frac{k}{m} \times \hat{x}
$$

Find an equation for $x(t)$ that satisfies the initial condition

$$
x(0)=A
$$

Now the equation of motion is given by

$$
\begin{aligned}
& a=\frac{d^{2} x}{d t^{2}}=-\frac{k}{m} x \\
\Rightarrow & \frac{d^{2} x}{d t^{2}}+\frac{k}{m} x=0
\end{aligned}
$$

Assume

$$
x(t)=A \cos (\omega t)
$$

then

$$
\begin{aligned}
& \frac{d^{2} x}{d t^{2}}+\frac{k}{m} x=-A \omega^{2} \cos (\omega t)+\frac{k}{m} A \cos (\omega t) \\
& =0 \\
& \Rightarrow-\omega^{2}+\frac{k}{m}=0 \\
& \Rightarrow \quad \omega=\sqrt{\frac{k}{m}} \\
& \text { so } \quad x(t)=A \cos \left(\sqrt{\frac{k}{m}} t\right) \\
& \text { and } \quad x(0)=A
\end{aligned}
$$

## Generalized Coordinates

Consider a system of $N$
point mass particles. Specification of the dynamics requires $3 N$ coordinates. In Cartesian coordinates this is

$$
\left(x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}, \ldots, x_{N}, y_{N}, z_{N}\right)
$$

To construct a representation that is irdependent of the choice of coordinate system define Generalized coordinates by the transformation equations from cartesian coordinates.

$$
\begin{aligned}
& q_{1}=q_{1}\left(x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}, \ldots, x_{N}, y_{N}, z_{N}\right) \\
& q_{2}=q_{2}\left(x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}, \ldots, x_{N}, y_{N}, z_{N}\right)
\end{aligned}
$$

$$
q_{3 N}=q_{3 N}\left(x_{1}, y_{1}, z_{1}, x_{2}, y_{2}, z_{2}, \ldots, x_{N}, y_{N}, z_{N}\right)
$$

The inverse transformation from the generalized coordinates to cartesian coordinates
is given by

$$
\begin{aligned}
& x_{1}=x_{1}\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right) \\
& y_{1}=y_{1}\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right) \\
& z_{1}=z_{1}\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right)
\end{aligned}
$$

$$
\begin{aligned}
x_{N}=x\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right) \\
y_{N}=y\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right) \\
z_{N}=2\left(q_{1}, q_{2}, q_{3}, \ldots, q_{3 N}\right) \\
\end{aligned}
$$

As an example consider the cylindrical coordinates
![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-006.jpg?height=491&width=481&top_left_y=1198&top_left_x=347)

$$
\begin{aligned}
& x=x(\rho, \phi, z)=\rho \cos \phi \\
& y=y(\rho, \phi, z)=\rho \sin \phi \\
& z=z(\rho, \phi, z)=z \\
& \rho=\rho(x, y, z)=\sqrt{x^{2}+y^{2}} \\
& \phi=\varphi(x, y, z)=\tan ^{-1} \frac{y}{x} \\
& z=z(x, y, z)=z
\end{aligned}
$$

Differential transformation for generalized coordinates
A more scalabe notation is needed to go further.
Denote cartesian coordinates by

$$
x_{1}=x_{1}, y_{1}=x_{2}, z_{1}=x_{3}, \ldots, z_{N}=x_{3 N}
$$

It then follows that the differentials for the generalized coordinates are given by

$$
d q_{i}=\sum_{j=1}^{3 N} \frac{\partial g_{i}}{\partial x_{j}} d x_{j}
$$

and the cartesian coordinale differentials are

$$
d x_{i}=\sum_{j=1}^{3 N} \frac{\partial x_{i}}{\partial q_{j}} d q_{j}
$$

the Jacobian Martix is defined by

$$
J_{i j}=\frac{\partial g_{i}}{\partial X_{j}}
$$

and the inverse by

$$
J_{i j}^{-1}=\frac{\partial x_{i}}{\partial q_{j}}
$$

consider
$\left(J J^{-1}\right)_{i j}=\sum_{k=1}^{3 N} J_{i k} J_{k}^{-1} j=\sum_{k=1}^{3 N} \frac{\partial q_{i}}{\partial x_{k}} \frac{\partial x_{k}}{\partial q_{j}}$
Now

$$
\begin{aligned}
d q_{i} & =\sum_{k=1}^{3 N} \frac{\partial q_{i}}{\partial x_{k}} d x_{k} \\
\Rightarrow \quad \frac{\partial q_{i}}{\partial q_{j}} & =\sum_{k=1}^{3 N} \frac{\partial q_{i}}{\partial x_{k}} \frac{\partial x_{k}}{\partial q_{j}}
\end{aligned}
$$

but

$$
\frac{\partial q_{i}}{\partial q_{j}}=\delta_{i j}
$$

since the $q_{i}$ are assumed to be linearly independent, $9 i$ does not depend on 91 unless $i=j$

Thus

$$
\begin{aligned}
& \left(J J^{-1}\right)_{i j}=\delta_{i j} \\
\Rightarrow & J J^{-1}=\underline{1}
\end{aligned}
$$

where $\underline{11}=$ identity matrix.

## Generalized Velocity

![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-010.jpg?height=495&width=988&top_left_y=239&top_left_x=228)

In Carlesian coordinates the trajectory of a point mass is given by

$$
\begin{aligned}
& x_{i}=x_{i}\left(q_{1}, q_{2}, \ldots, q_{3 N}, t\right) \\
& q_{i}=q_{i}\left(x_{1}, x_{2}, \ldots, x_{3 N}, t\right)
\end{aligned}
$$

The velocity of the particle in aurtesian coordainates is given by

$$
v_{i}=\frac{d x_{i}}{d t}
$$

But $x_{i}$ is a function of the $q_{i}$ so $v_{i}$ is the
derivative of $x_{i}$

$$
\begin{aligned}
v_{i}=\frac{d x_{i}}{d t} & =\sum_{j=1}^{3 N} \frac{\partial x_{i}}{\partial q_{j}} \frac{d q_{j}}{d t}+\frac{\partial x_{i}}{\partial t} \\
& =\sum_{j=1}^{3 N} \frac{\partial x_{i}}{\partial q_{j}} \dot{q}_{j}+\frac{\partial x_{i}}{\partial t}
\end{aligned}
$$

where

$$
\dot{G}_{1}=\frac{d g_{1}}{d t}
$$

Consider the partial derivative

$$
\frac{\partial}{\partial \dot{q}_{j}} \frac{\partial x_{i}}{\partial t}=\frac{\partial}{\partial t} \frac{\partial x_{i}}{\partial \dot{q}_{j}}
$$

which follows since the order of differentiation does not matter.

Since $x_{i}$ is independent of $i_{j}$

$$
\frac{\partial x_{i}}{\partial \dot{q}_{j}}=0
$$

Now,

$$
\frac{\partial v_{i}}{\partial \dot{q}_{i}}=\frac{\partial}{\partial \dot{q}_{i}}\left\{\sum_{j=1}^{3 N} \frac{\partial x_{i}}{\partial q_{j}} \dot{q}_{j}+\frac{\partial x_{i}}{\partial t}\right\}
$$

$$
=\sum_{j=1}^{3 N} \frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial q_{j}} \dot{q}_{j}\right)+\frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial t}\right)
$$

It was just shown that

$$
\frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial t}\right)=0
$$

and
$\frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial \dot{q}_{j}} \dot{q}_{j}\right)=\frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial q_{i}}\right) \dot{q}_{j}+\frac{\partial x_{i}}{\partial \dot{q}_{j}} \frac{\partial \dot{q}_{j}}{\partial \dot{q}_{i}}$
For the first term
$\frac{\partial}{\partial \dot{q}_{i}}\left(\frac{\partial x_{i}}{\partial q_{j}}\right)=\frac{\partial}{\partial q_{j}}\left(\frac{\partial x_{i}}{\partial \dot{q}_{i}}\right)=0$
and for the second term

$$
\frac{\partial \dot{G}_{g}}{\partial \ddot{q}_{i}}=\delta_{i j}
$$

Bringing things together

$$
\frac{\partial v_{i}}{\partial \dot{q}_{i}}=\sum_{j=1}^{3 N} \frac{\partial x_{i}}{\partial q_{j}} \delta_{i j}=\frac{\partial x_{i}}{\partial q_{i}}
$$

Thus

$$
\frac{\partial v_{i}}{\partial \dot{q}_{i}}=\frac{\partial x_{i}}{\partial q_{i}}
$$

## Generalized Forces

Conside a displacement of a Cartesian Coordinale

$$
d x_{i}=\sum_{k=1}^{3 N} \frac{\partial x_{i}}{\partial q_{k}} d q_{k}+\frac{\partial x_{i}}{\partial t} d t
$$

A virtual displacement, $\delta x_{i}$, is defined as an instantaneous inifitesimal displacement of the Cartesian Coordinate $x_{i}$. That is $d t=0$, so,

$$
\delta x_{i}=\sum_{k=1}^{3 N} \frac{\partial x_{i}}{\partial q_{k}} \delta q_{k}
$$

Where $\delta q_{k}$ is a virtual displacement of the generalized coordinate
Uirtual Work is defined by

$$
\delta \omega=\sum_{i=1}^{3 N} F_{i} \delta x_{i}
$$

Where $F_{i}$ is the component of the force acting on doordinate $\delta x_{i}$.

Substituting the expression for $\delta x_{i}$ into the equation for $\delta \omega$ gives

$$
\begin{aligned}
\delta \omega & =\sum_{i=1}^{3 N} F_{i} \sum_{k=1}^{3 N} \frac{\partial x_{i}}{\partial q_{k}} \delta q_{k} \\
& =\sum_{i=1}^{3 N} \sum_{k=1}^{3 N} F_{i} \frac{\partial x_{i}}{\partial q_{k}} \delta q_{k} \\
& =\sum_{k=1}^{3 N} \sum_{i=1}^{3 N} F_{i} \frac{\partial x_{i}}{\partial q_{k}} \delta q_{k}
\end{aligned}
$$

The genealized force is defined

$$
Q_{k}=\sum_{i=1}^{3 N} F_{i} \frac{\partial x_{i}}{\partial q_{k}}
$$

Then the virtual work becomes

$$
\delta \omega=\sum_{k=1}^{3 N} Q_{k} \delta q_{k}
$$

## Phase Space

The specification of all the position coordinates of a system is called Configuration Space. For a system of $N$ particles the configuration space has $3 N$ dimension.

The state of the system is represented by a single point in the 3 N dimesional configuration space.
Phase space in adition to the spatitial coordinates includes the 3 momentum components for each particle resulting in a GN dimensional space where the state of the system is represented by point in the space.

## Lagrange Equation

![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-017.jpg?height=491&width=556&top_left_y=233&top_left_x=445)

Consider a functional of the form

$$
\Phi(t, y, \dot{y})
$$

Find the function $y(t)$ that minimizes the integral

$$
\int_{t_{s}}^{t_{f}} \Phi(t, y, y) d t
$$

let $y(t)$ be the function that minimizes the integral. Define a new function that models all possible forms of functions that have values at $t_{1}$ and $t_{2}$ given by $y\left(t_{1}\right)$ and $y\left(t_{2}\right)$ by

$$
\bar{Y}(t, \epsilon)=y(t)+\epsilon \eta(t)
$$

where is a small scalar and $\eta(t)$ be an arbitrary function of $t$ that satifies

$$
\eta\left(t_{s}\right)=\eta\left(t_{f}\right)=0
$$

This is to ensure that

$$
\begin{aligned}
& \bar{Y}\left(t_{1}, t\right)=y\left(t_{1}\right) \\
& \bar{Y}\left(t_{2}, t\right)=y\left(t_{2}\right)
\end{aligned}
$$

Now consider the integral obtained by substituting I $(t, \epsilon)$ for $y(t)$ which is a function of $\epsilon$

$$
I(\epsilon)=\int_{t_{1}}^{t_{2}} \Phi(t, I, \dot{\bar{Y}}) d t
$$

Define the variation of the itegral by expanding $I(t)$ in a Taylor series for small $\epsilon$.
This is also called the first variation

$$
\begin{aligned}
& I(\epsilon)=I(0)+\left.\frac{d I}{d \epsilon}\right|_{\epsilon=0} ^{\epsilon}+0\left(\epsilon^{2}\right) \\
& \delta I=I(\epsilon)-I(0)=\left.\frac{d I}{d \epsilon}\right|_{\epsilon=0} ^{\epsilon}
\end{aligned}
$$

It follows that for
$\left.\frac{d I}{d \epsilon}\right|_{\epsilon=0}=0 \quad \Rightarrow \quad \delta I(t)=0$
since $\epsilon$ is arbitrary $\delta I(t)=0$
is a local extrema is a local extrema

Now
$\frac{d}{d t}\left\{\int_{t_{s}}^{t_{f}} \Phi(t, \bar{Y}, \dot{\bar{I}}) d t\right\}$
$=\int_{t_{s}}^{t_{s}} \frac{d}{d t} \Phi(t, \bar{Y}, \dot{\bar{I}}) d t$
$=\int_{t s}^{t_{f}} \frac{\partial \Phi}{\partial \bar{Y}} \frac{\partial \bar{Y}}{\partial t}+\frac{\partial \Phi}{\partial \dot{\bar{I}}} \frac{\partial \dot{\bar{Y}}}{\partial t} d t$
Consider the second term

$$
\begin{aligned}
& \int_{t_{s}}^{t_{f}} \frac{\partial \Phi}{\partial \dot{I}} \frac{\partial \dot{\bar{Y}}}{\partial t} d t=\int_{t_{f}}^{t_{s}} \frac{\partial \Phi}{\partial \dot{\bar{I}}} \frac{\partial}{\partial \epsilon}\left(\frac{d \overline{\bar{I}}}{d t}\right) d t \\
& =\int_{t_{s}}^{t_{f}} \frac{\partial \Phi}{\partial \dot{\bar{I}}} \frac{d}{d t}\left(\frac{\partial \bar{I}}{\partial t}\right) d t
\end{aligned}
$$

using integration by parts with

$$
\begin{aligned}
& d v=\frac{d}{d t}\left(\frac{\partial \bar{I}}{\partial t}\right) d t \Rightarrow v=\frac{\partial I}{\partial t} \\
& u=\frac{\partial \Phi}{\partial \bar{I}} \Rightarrow d u=\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \bar{I}}\right) d t \\
& \text { so } \\
& \int_{t_{s}}^{t_{f}} \frac{\partial \Phi}{\partial \dot{I}} \frac{d}{d t}\left(\frac{\partial \bar{I}}{\partial t}\right) d t=\left.\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\left(\frac{\partial \bar{I}}{\partial t}\right)\right|_{t f} ^{t s} \\
& -\int_{t s}^{t f} \frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right) \frac{\partial I}{\partial t} d t
\end{aligned}
$$

Recall that

$$
I(t, \epsilon)=y(t)+\epsilon \eta(t)
$$

SO

$$
\frac{\partial T}{\partial t}=\eta(t)
$$

substitution into the integral gives
$\int_{t_{s}}^{t_{f}} \frac{\partial \Phi}{\partial \dot{I}} \frac{d}{d t}\left(\frac{\partial \bar{I}}{\partial t}\right) d t=\left.\frac{\partial \Phi}{\partial \dot{I}} n(t)\right|_{t_{s}} ^{t_{f}}$

$$
-\int_{t_{s}}^{t_{f}} \frac{d}{d t}\left(\frac{\partial \Phi}{\partial I}\right) \eta(t) d t
$$

for the first term

$$
\left.\frac{\partial \Phi}{\partial \dot{I}} n(t)\right|_{t_{s}} ^{-t_{p}}=\frac{\partial \Phi}{\partial \dot{I}}\left[\eta\left(t_{f}\right)-\eta\left(t_{s}\right)\right]=\partial
$$

since it is assumed that $\eta\left(t_{f}\right)=\eta\left(t_{s}\right)=0$.
Putting thing back together

$$
\frac{d I}{d t}=\int_{t s}^{t f} \frac{\partial \Phi}{d I} \eta(t)-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial I}\right) \eta(t) d t
$$

$$
=\int_{t_{s}}^{t_{f}}\left[\frac{\partial \Phi}{\partial \underline{I}}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\right] \eta(t) d t
$$

Now

$$
\begin{aligned}
\left.\frac{d I}{d \epsilon}\right|_{\epsilon=0} & =\int_{t_{s}}^{t_{f}}\left[\frac{\partial \Phi}{\partial \underline{I}}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\right]_{\epsilon=0} \eta(t) d t \\
& =0
\end{aligned}
$$

let

$$
\begin{aligned}
\left.f(t)\right|_{t=0} & =\left[\frac{\partial \Phi}{\partial \underline{I}}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\right]_{t=0} \\
& =\frac{\partial \Phi}{\partial y}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{y}}\right)
\end{aligned}
$$

So
$\left.\frac{d I}{d t}\right|_{t=0}=\int_{t_{s}}^{t_{f}} f(t) n(t) d t=0$
Since $\eta(t)$ is an arbitrary function to satisfy the equation
for all choices it must be that

$$
f(t)=0, t_{s} \leqslant t \leqslant t_{f}
$$

OV

$$
\frac{\partial \Phi}{\partial y}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{y}}\right)=C
$$

so the $y(t)$ that minimizes the integral,

$$
\int_{t_{s}}^{t_{f}} \Phi(t, y, y) d t
$$

must satisfy

$$
\frac{\partial \Phi}{\partial y}-\frac{d}{d t}\binom{\partial \Phi}{\partial \dot{y}}=d
$$

Trits is the Euler-Lagrange Equation.
Next consider the variation of the time derivative of an arbirary flunction of the coordinates

$$
\delta \int_{t_{s}}^{t_{f}} \frac{d F}{d t}(t, y) d t
$$

using

$$
I(t, \epsilon)=y(t)+\epsilon \eta(t)
$$

so

$$
\begin{aligned}
& \delta \int_{t_{s}}^{t_{f}} \frac{d F}{d t}(t, \bar{I}) d t=\delta\left[F\left(t_{f}, I\left(t_{f}, \epsilon\right)\right)\right. \\
& \left.-F\left(t_{s}, \bar{I}\left(t_{s}, \epsilon\right)\right)\right] \\
= & \left.\frac{d}{d t}\left[F\left(t_{f}, I\left(t_{f}, \epsilon\right)\right)-F\left(t_{s}, \bar{I}\left(t_{s}, \epsilon\right)\right)\right]\right|_{\epsilon=0} \\
= & \frac{\partial F\left(t_{f}\right)}{\partial \bar{I}} \frac{\partial \bar{I}}{\partial t}\left(t_{f}, t\right)-\left.\frac{\partial F\left(t_{s}\right)}{\partial \bar{I}} \frac{\partial \nabla}{\partial t}\left(t_{s}, t\right)\right|_{\epsilon=0} \\
= & \frac{\partial F\left(t_{f}\right) \eta\left(t_{f}\right)-\frac{\partial F\left(t_{s}\right) \eta\left(t_{s}\right)}{\partial y}}{} \\
= & 0
\end{aligned}
$$

Since $\eta\left(t_{f}\right)=\eta\left(t_{s}\right)=0$

Next consider the case where $\$$ has the form

$$
\Phi\left(y_{1}, y_{2}, \ldots, y_{n}, \dot{y}_{1}, \dot{y}_{2}, \ldots, \dot{y}_{n}, t\right)
$$

Then minimize

$$
I=\int_{t_{s}}^{r_{f}} \Phi\left(y_{1}, y_{2}, \ldots, y_{n}, \dot{y}_{1}, \dot{y}_{2}, \ldots, \dot{y}_{n}, t\right) d t
$$

Find the $y_{i}(t)$ such that

$$
\delta I=\left.\frac{d I}{d \epsilon}\right|_{t=0} \epsilon
$$

as before assume that

$$
\begin{aligned}
& \bar{I}_{i}(\epsilon)=y_{i}+\epsilon \eta_{i}(t) \\
& \dot{\bar{I}}_{i}(\epsilon)=\dot{y}_{i}+\epsilon \dot{\eta}_{i}(t)
\end{aligned}
$$

and

$$
\begin{aligned}
\delta \bar{I}_{i}(\epsilon) & =\left.\frac{\partial \bar{I}_{i}}{\partial \epsilon}\right|_{\epsilon=0} ^{\epsilon} \\
\delta \dot{\Psi}_{i}(\epsilon) & =\left.\frac{\partial \dot{I}_{i}}{\partial \epsilon}\right|_{\epsilon=0} ^{\epsilon}=\left.\frac{\partial}{\partial \epsilon} \frac{d \bar{I}_{i}}{d t}\right|_{\epsilon=0} ^{\epsilon} \\
& =\left.\frac{d}{d t} \frac{\partial \bar{I}_{i}}{\partial \epsilon}\right|_{\epsilon=0} ^{\epsilon}=\frac{d}{d t} \delta I_{i}(\epsilon)
\end{aligned}
$$

Now

$$
\begin{aligned}
\delta I & =\delta \int_{t_{s}}^{t_{f}} \Phi d t=\int_{t_{s}}^{t_{f}} \delta \Phi d t \\
& =\int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\frac{\partial \Phi}{\partial I_{i}} \delta I_{i}+\frac{\partial \Phi}{\partial \dot{I}_{i}} \delta \dot{I}_{i}\right\} d t
\end{aligned}
$$

$$
\begin{aligned}
& =\int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\frac{\partial \Phi}{\partial I_{i}} \delta I_{i}+\frac{\partial \Phi}{\partial \dot{I}_{i}} \frac{d}{d t} \delta I_{i}\right\} d t \\
& =\int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\frac{\partial \Phi}{\partial I_{i}}+\frac{\partial \Phi}{\partial \dot{I}_{i}} \frac{d}{d t}\right\} \delta I_{i} d t \\
& =\int_{t_{s}}^{t_{s}} \sum_{i=1}^{n}\left\{\left.\frac{\partial \Phi}{\partial I_{i}} \frac{\partial I_{i}}{\partial t}\right|_{\epsilon=0} ^{\epsilon}+\left.\frac{\partial \Phi}{\partial \bar{I}} \frac{d}{d t}\left(\frac{\partial I_{i}}{\partial t}\right)\right|_{\epsilon=0} ^{\epsilon}\right\} d t \\
& =\left.\int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\frac{\partial \Phi}{\partial I_{i}} \frac{\partial I_{i}}{\partial t}+\frac{\partial \Phi}{\partial \dot{I}} \frac{d}{d t}\left(\frac{\partial I_{i}}{\partial t}\right)\right\}\right|_{\epsilon=0} ^{\epsilon} d t
\end{aligned}
$$

The summation is over single variable terms which was previously considered
$\frac{\partial \Phi}{\partial I_{i}} \frac{\partial I_{i}}{\partial t}+\frac{\partial \Phi}{\partial \dot{I}} \frac{d}{d t}\left(\frac{\partial I_{i}}{\partial t}\right)=\left[\frac{\partial \Phi}{\partial \Psi}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\right] \eta_{i}(t)$
and

$$
\delta I=\left.\frac{d I}{d \epsilon}\right|_{\epsilon=0} ^{\epsilon}=\left.\int_{t_{s}}^{t_{f}} \sum_{i=1}^{N}\left[\frac{\partial \Phi}{\partial I}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{I}}\right)\right]\right|_{\epsilon=0} \eta_{i}(t) \epsilon d t
$$

$$
\begin{aligned}
\left.\frac{\partial I}{d t}\right|_{\epsilon=0} & =\left.\int_{t_{s}}^{t_{f}} \sum_{i=1}^{N}\left[\frac{\partial \Phi}{\partial Y_{i}}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{Y}_{i}}\right)\right]\right|_{t=0} \eta_{i}(t) d t \\
& =\int_{t_{s}}^{t_{f}} \sum_{i=1}^{N}\left[\frac{\partial \Phi}{\partial y_{i}}-\frac{d}{d t} \frac{\partial \Phi}{\partial \dot{Y}_{i}}\right] \eta_{i}(t) d t \\
& =0
\end{aligned}
$$

As in the single variable case since $\eta_{i}(t)$ is arbitray to satisfy the equation it must be that

$$
\frac{\partial \Phi}{\partial y_{i}}-\frac{d}{d t}\left(\frac{\partial \Phi}{\partial \dot{y}_{i}}\right) \quad \forall \quad i=1,2,3, \ldots, n
$$

## Principle of $d^{\prime}$ Alembert

The Principle of d'Alembert stapts from Neuton's second Law. Consider a force $\vec{F}$ actins on a particle of mass m . Neublons second law stades

$$
\bar{F}=\frac{d \bar{D}}{d t}=\bar{v} \frac{d m}{d t}+m \frac{d \bar{v}}{d t}=\bar{v} \frac{d m}{d t}+m \overline{\bar{v}}
$$

This form is move general in that it includes the possibility of changes in mass.
using the form

$$
\vec{F}=\dot{\bar{P}} \Rightarrow \quad \bar{F} \cdot \dot{\bar{P}}=0
$$

The total force acting on a system of $N$ particles.
Consider a virtual displacent in Cartesian coordinates for all particles in the system

$$
\sum_{i=1}^{n}\left(F_{i}-\dot{p}_{i}\right) \delta x_{i}=0
$$

since each term is zero by defintion and $n=3 N$ is
the total number of coordinates.
Assume there are $k$ constraints acting on the system so there will be $n-k$ generalized coordinates and that satisfy. the inverse transform.

$$
x_{i}=x_{i}\left(q_{1}, q_{2}, \ldots, q_{n-k}, t\right)
$$

it follows that the variation in $x_{i}$ is given $b y$,

$$
\delta x_{i}=\sum_{j=1}^{n-k} \frac{\partial x_{i}}{\partial q_{j}} \delta q_{j}
$$

Now

$$
\sum_{i=1}^{n}\left(F_{i}-\dot{p}_{i}\right) \delta x_{i}=\sum_{i=1}^{n} F_{i} \delta x_{i}-\sum_{i=1}^{n} \dot{p}_{i} \delta x_{i}=\partial
$$

Consider the first term

$$
\begin{aligned}
& \sum_{i=1}^{n} F_{i} \delta x_{i}=\sum_{i=1}^{n} \sum_{j=1}^{n-k} F_{i} \frac{\partial x_{i}}{\partial q_{j}} \delta q_{j} \\
& =\sum_{j=1}^{n-k}\left[\sum_{i=1}^{n} F_{i} \frac{\partial x_{i}}{\partial q_{j}}\right] \delta q_{j}=\sum_{j=1}^{n-k} Q, \delta q_{j}
\end{aligned}
$$

Where the genealized force $Q_{3}$ is given by

$$
Q_{j}=\sum_{i=1}^{n} F_{i} \frac{\partial x_{i}}{\partial q_{j}}
$$

The virtual work performed on the system is,

$$
\delta \omega=\sum_{j=1}^{n-k} Q_{j} \delta q_{j}
$$

Now consider the second term
$\sum_{i=1}^{n} \dot{p}_{i} \delta x_{i}=\sum_{i=1}^{n} \dot{p}_{i} \sum_{j=1}^{n-k} \frac{\partial x_{i}}{\partial q_{j}} \delta q_{j}$
$=\sum_{j=1}^{n-k} m_{i} \delta q_{j} \sum_{i=1}^{n} \dot{v}_{i} \frac{\partial x_{i}}{\partial q_{j}}$
where it was assumed the the mass is assumed constant.

Now

$$
\frac{d}{d t}\left(v_{i} \frac{\partial x_{i}}{\partial q_{j}}\right)=v_{i} \frac{\partial x_{i}}{\partial q_{j}}+v_{i} \frac{d}{d t}\left(\frac{\partial x_{i}}{\partial q_{j}}\right)
$$

$$
\Rightarrow \dot{v}_{i} \frac{\partial x_{i}}{\partial q_{j}}=\frac{d}{d t}\left(v_{i} \frac{\partial x_{i}}{\partial q_{j}}\right)-v_{i} \frac{d}{d t}\left(\frac{\partial x_{i}}{\partial q_{j}}\right)
$$

Recall that

$$
\frac{\partial x_{i}}{\partial q_{j}}=\frac{\partial \dot{x}_{i}}{\partial \dot{q}_{j}}=\frac{\partial v_{i}}{\partial \dot{q}_{j}}
$$

and the last term is given by

$$
\frac{d}{d t}\left(\frac{\partial x_{i}}{\partial q_{j}}\right)=\frac{\partial \dot{x}_{i}}{\partial q_{j}}=\frac{\partial v_{i}}{\partial q_{j}}
$$

Bringing things together

$$
\begin{aligned}
& \sum_{i=1}^{n} \dot{p}_{i} \delta x_{i}=\sum_{j=1}^{n-k} m_{i}\left[\frac{d}{d t}\left(v_{i} \frac{\partial v_{i}}{\partial \dot{q}_{j}}\right)\right. \\
& \left.-v_{i} \frac{\partial v_{i}}{\partial q_{j}}\right] \delta q_{j}
\end{aligned}
$$

Now Consider the Kinetic energy

$$
T_{i}=\frac{1}{2} m v_{i}^{2}
$$

so

$$
\frac{\partial T_{i}}{\partial q_{j}}=\frac{1}{2} m_{i}\left(\partial v_{i}\right) \frac{\partial v_{i}}{\partial q_{j}}=m_{i} v_{i} \frac{\partial v_{i}}{\partial q_{1}}
$$

$$
\frac{\partial T}{\partial \dot{q}_{j}}=\frac{1}{\partial} m_{i}\left(\partial v_{i}\right) \frac{\partial v_{i}}{\partial \dot{q}_{j}}=m v_{i} \frac{\partial v_{i}}{\partial \dot{q}_{j}}
$$

putting things together gives

$$
\sum_{i=1} P_{i} \delta x_{i}=\sum_{j=1}^{n-k}\left[\frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{j}}\right)-\frac{\partial T}{\partial q_{j}}\right] \delta q_{j}
$$

And finally,
$\sum_{i=1}^{n}\left(F_{i}-\dot{p}_{i}\right) \delta x_{i}=\sum_{j=1}^{n-k} Q, \delta q_{j}$
$-\sum_{j=1}^{n-k}\left[\frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{j}}\right)-\frac{\partial T}{\partial q_{j}}\right] \delta q_{j}$
$=\sum_{j=1}^{n-K}\left\{Q_{j}-\left[\frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{j}}\right)-\frac{\partial T}{\partial q_{j}}\right]\right\} \delta q_{j}=\partial$
but the $n-k$ 9, are linearly independent so

$$
\frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{j}}\right)-\frac{\partial T}{\partial q_{j}}=Q_{j}
$$

This equation is called the Nielsen form of Lagrange's equation.
If the generalized forces are assummed to be derivable from a potential energy function, $v$, that depends only on the $9 ;$

$$
Q=-\frac{\partial V}{\partial q_{j}} j
$$

and

$$
\begin{aligned}
& \frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{j}}\right)-\frac{\partial T}{\partial q_{j}}=\frac{\partial V}{\partial q_{j}} \\
\Rightarrow & \frac{d}{d t}\left[\frac{\partial}{\partial \dot{q}_{j}}(T-V)\right]-\frac{\partial}{\partial q_{j}}(T-V)=\partial
\end{aligned}
$$

let

$$
L=T-V
$$

then

$$
\frac{d}{\partial t}\left(\frac{\partial L}{\partial \dot{q}_{j}}\right)-\frac{\partial L}{\partial q_{j}}=0
$$

which is Lagrange's Equation

## Hamilton's Principle

A mechanical system of $N$ particles can be described by $n=3 \mathrm{~N}$ Cartiesian coordinates. These coordinates may not be independent if there are constriaints. If there are $k$ constrairts the number of molependent coordinates is $n-k$. So the state of the system can be represented by a poirt in a $n-k$ dimensional space.
The generalized coordinates $\left(q_{1}, q_{21} \ldots, q_{n-k}\right)$ are called configuratin space
The evolution of the system in time consists of changes in the position of the point describing the state of the system Jin configuration sprece Consider an initial state at time ts and a final state at time $t_{f}$. what poth does the system follow in configuration space as it
passes from the state at $t_{s}$ to the state at $t f$.
Hamilton's Principal assumes that the transition between the states minimize the Action which is defined by the integral

$$
I=\int_{t_{s}}^{t_{f}} L d t
$$

where $L$ is a function of the genelaized coordinates

$$
L=L\left(q_{1}, q_{2}, \ldots, q_{n-k} ; \dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n-k} ; t\right)
$$

called the Lagrangian.
Hamilton's Principal can be written as the variational calculation

$$
\delta I=\delta \int_{t_{s}}^{t_{f}} L d t=0
$$

If follows that the path that minimized I is given by the lagrange-Euler equation

$$
\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{j}}\right)-\frac{\partial L}{\partial \varphi_{j}}=0
$$

$L$ is called the Lagrangian
and the equation is called lagranges equation.

## Lagrange Mutipliers

The method of Lagrange multipliers used to determithe the constraing forces acting on a system.

Consider a system described by $n$ generalized coordinates $q_{1}, q_{2}, \ldots, q_{n}$. Furthure assume that the system has $k$ constraints acting on it. The constraints eleminate $k$ of the generalized coordinates leaving a total $n-k$ linearly independent coordinates.
The time behavior of the system is described by Hamilton's Principal

$$
\delta I=\delta \int_{t_{s}}^{t_{f}} L d t=\int_{t_{s}}^{t_{f}} \delta L d t=0
$$

with $k$ equations defining holonomic constraints,

$$
f_{j}\left(q_{1}, q_{2}, \ldots, q_{n}\right)=0 \quad \forall \quad j=1,2, \ldots, k
$$

consider the variation of the constraints

$$
\delta f_{j}=\sum_{l=1}^{n} \frac{\partial f_{j}}{\partial q_{l}} \delta q_{l}=0
$$

For each $f_{j}$ define a scalar parameter $\lambda_{j}$ such that

$$
\lambda_{j} \delta f_{j}=\sum_{l=1}^{n} \lambda_{j} \frac{\partial f_{j}}{\partial q_{l}} \delta q_{l}=0
$$

collecting all of the ce.istraints into a single term grues

$$
\sum_{j=1}^{k} \lambda_{j} \delta f_{j}=\sum_{j=1}^{k} \sum_{l=1}^{n} \lambda_{j} \frac{\partial f_{j}}{\partial q_{l}} \delta q_{l}=0
$$

Since this expression evalutes to zero its integral over time will also be zero so

$$
\int_{t_{s}}^{t_{f}} \sum_{j=1}^{k} \sum_{l=1}^{n} \lambda_{j} \frac{\partial f_{j}}{\partial q_{l}} \delta q_{l} d t=0
$$

## consider

$$
L\left(q_{1}, q_{2}, \ldots, q_{n} ; \dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n}, t\right)
$$

Previously it was shown that

$$
\int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left[\frac{\partial L}{\partial G_{i}}-\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)\right] \epsilon \eta_{i}(t) d t=0
$$

but

$$
\delta q_{i}=\epsilon \eta_{i}(t)
$$

SO

$$
\int_{t_{s}}^{t f} \sum_{i=1}^{n}\left[\frac{\partial L}{\partial G_{i}}-\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)\right] \delta G_{i} d t=0
$$

Adding the constraint to the equation above and noting that only $n-k$ of the terms are linearly independent yields

$$
\begin{aligned}
& \int_{t_{s}}^{t} \sum_{i=1}^{n-k}\left\{\left[\frac{\partial L}{\partial q_{i}}-\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)\right]+\sum_{j=1}^{k} \lambda_{j} \frac{\partial f_{j}}{\partial q_{i}}\right\} \delta q_{i} d t \\
& \quad=0
\end{aligned}
$$

since the $\delta 9 i$ are linearly independent for $n-k$ terms for those

$$
\begin{aligned}
& {\left[\frac{\partial L}{\partial q_{i}}-\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)\right]+\sum_{J=1}^{K} \lambda_{j} \frac{\partial f_{j}}{\partial q_{i}}=0 } \\
\Rightarrow & \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\frac{\partial L}{\partial q_{i}}=\sum_{j=1}^{K} \lambda_{j} \frac{\partial f_{j}}{\partial q_{i}} \forall i=1,2, \ldots, n-K
\end{aligned}
$$

Now $L=T-V$ and it was previously shown that

$$
\frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{i}}\right)-\frac{\partial T}{\partial q_{i}}=Q_{i}
$$

and that $Q_{j}$ was a force derivalde from a potential function $v$

$$
Q_{i}=-\frac{\partial v}{\partial q_{i}}
$$

assume another force exits that cannot be derived from a Potential function, $Q_{c}$, adding gives

$$
\begin{aligned}
& \frac{d}{d t}\left(\frac{\partial T}{\partial \dot{q}_{i}}\right)-\frac{\partial T}{\partial q_{i}}=Q_{i}+Q_{c} \\
\Rightarrow & \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\frac{\partial L}{\partial q_{i}}=Q_{c}
\end{aligned}
$$

domparing with the provious results gives

$$
Q_{c}=\sum_{j=1}^{k} \lambda_{j} \frac{\partial f_{j}}{\partial q_{i}}
$$

thus the constraints appear is forces in the model.
In equillibrium the virtual of the impressed forces is zero

$$
\delta \omega=0
$$

If the forces are derived from a potential

$$
F_{i}=-\frac{\partial v}{\partial q_{i}}
$$

then the virtual work is
equal to the negative of the variation of the potential energy fundron

$$
\delta \omega=\sum_{i} F_{i} \delta q_{i}=-\sum_{i} \frac{\partial v}{\partial q_{i}} \delta q_{i}=-\delta v
$$

If the system has a hdonomic

$$
f\left(q_{1}, q_{2}, \ldots, q_{n}\right)=0
$$

Then

$$
\begin{aligned}
& \quad \delta(L-\lambda f)=0 \\
& =\quad \delta(T-v-\lambda f)=0 \\
& \text { Then the potential is } \\
& \quad v+\lambda f \\
& \text { Therefore } \\
& \quad \delta \omega=0=\delta(v+\lambda f)
\end{aligned}
$$

if $\lambda f$ is a potential

The forces will be given by

$$
\begin{gathered}
F_{i}=-\frac{\partial(\lambda f)}{\partial q_{i}}=-\lambda \frac{\partial f}{\partial q_{i}}-\frac{\partial \lambda}{\partial q_{i}} f \\
\text { by definition } f=\gamma \text { so the } \\
\text { force of constraint } \\
F_{i}=-\lambda \frac{\partial f}{\partial q_{i}}
\end{gathered}
$$

## Conservation laws and symmeth/

The Lagrangian is given by

$$
L=T-V
$$

Generlized Momentum
For a free particle $v=0$
so

$$
L=\frac{1}{2} m\left(\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}\right)
$$

it follows that

$$
\frac{\partial x}{\partial \dot{x}}=m \dot{x}=p_{x}
$$

similarly

$$
\frac{\partial L}{\partial \dot{y}}=P_{y} \quad \frac{\partial L}{\partial \dot{z}}=P_{z}
$$

For a free rotating sbject with moment of inertia I

$$
L=\frac{1}{2} I \dot{\theta}^{2}
$$

then

$$
\frac{\partial L}{\partial \dot{\theta}}=I \dot{\theta}
$$

which is the angular momentum. In geneal

$$
P_{i}=\frac{\partial L}{\partial \dot{q}_{i}}
$$

is the genealized momentum

## Cyclic Coordinates

Consider the lagrangian

$$
L=\frac{1}{2} m\left(\dot{x}^{2}+\dot{y}^{2}+\dot{z}^{2}\right)-m g z
$$

which would represent a particle in a gravitational field.
$x$ and $y$ are cyclic since they do not appear in the Lagrangian
From Lagranges equation

$$
\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{\varphi}}\right)-\frac{\partial L}{\partial \varphi}=\partial
$$

if $9 i$ is cyclic then

$$
\frac{\partial L}{\partial q}=0
$$

## and

$$
\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)=d
$$

but the generalized momentum is given by

$$
P_{i}=\frac{\partial L}{\partial \dot{q}_{i}}
$$

50

$$
\begin{aligned}
& \frac{d}{d t} P_{i}=0 \\
& \Rightarrow P_{i}=\text { constant }
\end{aligned}
$$

Thus the generalizer momentum of a cyclic coordinate is conserved.
Conservation of Linear Momentum
Consider a Lagrangian for a sylem of $u$ partreles with $n=3 N$ obordinates,

$$
L\left(q_{1}, q_{2}, \ldots, q_{n} ; \dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n}, t\right)
$$

Assume that only the position coordinates are displaced.
then

$$
\delta L=\sum_{i=1}^{n} \frac{\partial L}{\partial q_{i}} \delta q_{i}
$$

furthur assume that all particles are displaced by the same constant amount

$$
\delta q_{i}=\epsilon \quad \forall i=1,2, \ldots, n
$$

then

$$
\delta L=\epsilon \sum_{i=1}^{n} \frac{\partial L}{\partial q_{i}}
$$

If it is assumed that the Lagrangian does not change when displaced, i.e. it is homogeneous in space,

$$
\delta L=0
$$

then

$$
\sum_{i=1}^{n} \frac{\partial L}{\partial \varphi_{i}}=0
$$

from Lagrange's equation

$$
\sum_{i=1}^{n}\left\{\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\frac{\partial L}{\partial q_{i}}\right\}=0
$$

$$
\begin{aligned}
& \Rightarrow \sum_{i=1}^{n} \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\sum_{i=1}^{n} \frac{\partial L}{\partial q_{i}}=0 \\
& \Rightarrow \sum_{i=1}^{n} \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)=0
\end{aligned}
$$

but

$$
P_{i}=\frac{\partial L}{\partial G_{i}}
$$

and

$$
\sum_{i=1}^{n} \frac{d}{d t} P_{i}=\frac{d}{d t} \sum_{i=1}^{n} P_{i}=\frac{d}{d t} P_{T O T}=0
$$

thus the total momentum of the system is conserved

$$
P_{\text {TOT }}=\text { constant }
$$

Furthur since $L=T-V$

$$
\begin{aligned}
& \frac{\partial L}{\partial q_{i}}=-\frac{\partial V}{\partial q_{i}}=F_{i} \\
\text { so } & \sum_{i=1}^{n} \frac{\partial L}{\partial q_{i}}=\sum_{i=1}^{n} F_{i}=0
\end{aligned}
$$

Trat is the sum of all forces acting on the system is zero.
Conservation of Angular Momentum
Consider the angular momentum of a particle of mass $m$

$$
\bar{l}=\bar{r} \times \bar{p}
$$

Where $\bar{l}$ is the angular momentum $\bar{r}$ a position vector and $\bar{p}$ the linear momentum.

Now

$$
\begin{aligned}
& \frac{d \bar{l}}{d t}=\frac{d(\bar{r} \times \bar{p})=}{d t} \frac{d \bar{r} \times \bar{p}+\bar{r} \times \frac{d \bar{p}}{d t}}{d t} \\
& =\bar{v} \times \bar{p}+\bar{r} \times \bar{F}
\end{aligned}
$$

for the first term

$$
\bar{v} \times \bar{p}=\bar{v} \times \bar{v} m=0
$$

since the cross product of a vector with itself is zero.

So

$$
\frac{d \bar{l}}{d t}=\bar{r} \times \bar{F}=\bar{T}
$$

where $\bar{T}$ is the torque.
From this equation it is seen

$$
\frac{d \bar{\ell}}{d t}=0
$$

if there is no net torque on the system and angular momentum!

Consider the case of an isotropic force.

$$
\bar{F}=f(r) \hat{r}
$$

in this case the force does not change for rotations about $r=0$ that keep $r=$ constant.
It follows that

$$
\frac{d \bar{l}}{d t}=\bar{r} \times \hat{r} f(r)=0
$$

so angular momentum is conserved

The gravitational and electrostatic forces are of this type.
![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-051.jpg?height=589&width=640&top_left_y=237&top_left_x=322)
![](https://cdn.mathpix.com/cropped/2025_09_16_07d8147159f6e50158a3g-051.jpg?height=665&width=1098&top_left_y=965&top_left_x=352)

Consider the diagram above representing one particle in the system. Assume that the particle is rotated through an angle $\delta \phi$ while $\left|\bar{r}_{i}\right|$ and $\theta$ are held constant. If it is assumed that the Lagrangian is invariant through this rotation

$$
\delta L=\sum_{i=1}^{N}\left(\frac{\partial L}{\partial \vec{r}_{i}} \cdot \delta \bar{r}_{i}+\frac{\partial L}{\partial \vec{V}_{i}} \cdot \delta \bar{V}_{i}\right)=0
$$

Here the sum is over $N$ particles not coordinates.
lagranges equation for a particle

$$
\frac{d}{d t}\left(\frac{\partial L}{\partial \bar{v}_{i}}\right)-\frac{\partial L}{\partial \bar{r}_{i}}=0
$$

but the generalized momentum is defined by

$$
\bar{p}_{i}=\frac{\partial l}{\partial \bar{v}_{i}}
$$

so from lagrances equation

$$
\frac{d}{d t}\left(\frac{\partial L}{\partial \bar{v}_{i}}\right)=\frac{d}{d t} \bar{p}_{i}=\dot{\bar{p}}_{i}=\frac{\partial L}{\partial \bar{r}} .
$$

the expression for $\delta L$ becomes

$$
\delta L=\sum_{i=1}^{N}\left(\dot{\bar{P}}_{i} \cdot \delta \bar{r}_{i}+\bar{P}_{i} \cdot \delta \bar{v}_{i}\right)=0
$$

from the figure it is seen that

$$
\begin{aligned}
\left|\delta \vec{r}_{i}\right| & =r_{i} \sin \theta \delta \phi_{i} \\
\Rightarrow \quad \delta \bar{r}_{i} & =\bar{r}_{i} \times \delta \bar{\varphi}_{c}
\end{aligned}
$$

similarly

$$
\delta \bar{v}_{i}=\bar{v}_{c} \cdot \delta \bar{\varphi}_{i}
$$

80
$\delta L=\sum_{i=1}^{N} \dot{\bar{p}}_{i} \cdot\left(\bar{r}_{i} \times \delta \bar{\varphi}_{i}\right)+\bar{p}_{i} \cdot\left(\bar{v}_{i} \times \delta \bar{\varphi}_{i}\right)$
using the identity

$$
\bar{a} \cdot(\bar{b} \times \bar{c})=\bar{c} \cdot(\bar{a} \times \bar{b})
$$

gives

$$
\begin{aligned}
\delta L & =\sum_{i=1}^{N} \delta \bar{\varphi}_{i} \cdot\left(\bar{p}_{i} \times \bar{r}_{i}\right)+\delta \bar{\varphi}_{i} \cdot\left(\bar{p}_{i} \times \bar{v}_{i}\right) \\
& =\sum_{i=1}^{N} \delta \bar{q}_{i} \cdot\left(\dot{\bar{p}}_{i} \times \bar{r}_{i}+\bar{p}_{i} \times \dot{\bar{r}}_{i}\right)
\end{aligned}
$$

$$
=\sum_{i=1}^{N} \delta \bar{\varphi}_{i} \cdot \frac{d}{d t}\left(\bar{p}_{i} \times \bar{r}_{i}\right)=0
$$

assume the $\left|\delta \bar{\varphi}_{i}\right|$ constant and note that the angular momentum is given by

$$
\bar{l}_{i}=\bar{r}_{i} \times \bar{p}_{i}
$$

$$
\delta L=\delta \bar{\varphi} \cdot\left(\sum_{i=1}^{N} \frac{d}{d t} \bar{l}_{i}\right)=0
$$

since $\delta \bar{\phi}$ is nn $^{\prime}$ - ry it must be that

$$
\begin{aligned}
& \sum_{i=1}^{N} \frac{d \bar{l}_{i}}{d t}=\frac{d}{d t} \sum_{i=1}^{N} \bar{l}_{i} \\
& =\frac{d}{d t} \bar{l}_{t a t}=0
\end{aligned}
$$

Trus the total angular momentum is conserved.

## Conservation of Energy

The total time derivative of the Lagrangian,

$$
L\left(q_{1}, q_{2}, \ldots, q_{n} ; \dot{q}_{1}, \dot{q}_{2}, \ldots, q_{n}, t\right)
$$

is given by

$$
\frac{d L}{d t}=\sum_{i=1}^{n} \frac{\partial L}{\partial q_{i}} \frac{d q_{i}}{d t}+\sum_{i=1}^{n} \frac{\partial L}{\partial \dot{q}_{i}} \frac{d \dot{q}_{i}}{d t}+\frac{\partial L}{\partial t}
$$

From Lagrange's equation

$$
\begin{aligned}
& \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\frac{\partial L}{d q_{i}}=0 \\
\Rightarrow & \frac{\partial L}{\partial q_{i}}=\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)
\end{aligned}
$$

$\frac{S_{0}}{d t}=\sum_{i=1}^{n} \dot{q}_{i} \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)+\sum_{i=1}^{n} \frac{\partial L}{\partial \dot{q}_{i}} \frac{d \dot{q}_{i}}{d t}+\frac{\partial L}{\partial t}$

$$
=\sum_{i=1}^{n}\left\{\dot{q}_{i} \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)+\frac{\partial L}{\partial \dot{q}_{i}} \frac{d \dot{g}_{i}}{\partial t}\right\}+\frac{\partial L}{\partial t}
$$

Now

$$
\begin{aligned}
& \frac{d}{d t}\left(\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)=\sum_{i=1}^{n} \frac{d}{d t}\left(\dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right) \\
& =\sum_{i=1}^{n}\left\{\dot{q}_{i} \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)+\frac{d \dot{q}_{i}}{d t} \frac{\partial L}{\partial \dot{q}_{i}}\right\}
\end{aligned}
$$

substitution into the original expression gives

$$
\begin{aligned}
& \frac{d L}{d t}=\frac{d}{d t}\left(\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)+\frac{\partial L}{\partial t} \\
& \Rightarrow \frac{\partial L}{\partial t}=\frac{d}{d t}\left(L-\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)
\end{aligned}
$$

If it is assumed the $L$ does not explicitly depend on time

$$
\frac{\partial L}{\partial t}=0
$$

then

$$
\frac{d}{d t}\left(L-\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)=0
$$

Trues

$$
L-\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}
$$

is conservered. To interpret this result let

$$
\begin{aligned}
h & =h\left(q_{1}, q_{2}, \ldots, q_{n}, \dot{q}_{1}, \dot{q}_{2}, \dot{q}_{3}, \ldots, \dot{q}_{n}, t\right) \\
& =\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}-L
\end{aligned}
$$

for now call $h$ the energy function

Now the Lagrangian is assumed to have the form

$$
L=T-V
$$

where $v$ is a function only of cosvdinates

$$
V=V\left(q_{1}, q_{2}, \ldots, q_{n}\right)
$$

To go furthwr an expression for $T$ is required

General Expression for Kinetic Energy A general expression for kinetic energy is found by considering the generalized coordinate transformation from Cartesian coodinates

$$
T=\sum_{i=1}^{n} \frac{1}{2} m_{i} \dot{x}_{i}^{2}
$$

Now the total time derivative of $x_{i}$ is given by

$$
\begin{aligned}
& x_{i}=x_{i}\left(q_{1}, q_{2}, \ldots, q_{n}, t\right) \\
& \dot{x}_{i}=\frac{d x_{i}}{d t}=\sum_{j=1}^{n} \frac{\partial x_{i}}{\partial q_{j}} \dot{q}_{j}+\frac{\partial x_{i}}{\partial t}
\end{aligned}
$$

inserting this expression into the equation for $T$ gives
$\sum_{i=1}^{n} \frac{1}{2} m_{i} \dot{x}_{i}^{2}=\sum_{i=1}^{n} \frac{1}{2} m_{i}\left\{\sum_{j=1}^{n} \frac{\partial x_{i}}{\partial q_{j}} \dot{q}_{j}+\frac{\partial x_{i}}{\partial t}\right\}$

$$
\left\{\sum_{k=1}^{n} \frac{\partial x_{i}}{\partial q_{k}} \dot{q}_{k}+\frac{\partial x_{i}}{\partial t}\right\}
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n} \frac{1}{2} m_{i}\left\{\sum_{j=1}^{n} \sum_{k=1}^{n} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial q_{k}} \dot{q}_{j} \dot{q}_{k}\right. \\
& +\sum_{k=1}^{n} \frac{\partial x_{i}}{\partial q_{k}} \frac{\partial x_{i}}{\partial t} \dot{q}_{k}+\sum_{j=1}^{n} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial t} \dot{q}_{j} \\
& \left.+\left(\frac{\partial x_{i}}{\partial t}\right)^{2}\right\} \\
& =\sum_{j=1}^{n} \sum_{k=1}^{n}\left\{\sum_{i=1}^{n} \frac{1}{2} m_{i} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial q_{k}}\right\} \dot{q}_{j} \dot{q}_{k} \\
& +\sum_{j=1}^{n}\left\{\sum_{i=1}^{n} m_{i} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial t}\right\} \dot{q}_{j} \\
& +\sum_{i=1}^{n} \frac{1}{2} m_{i}\left(\frac{\partial x_{i}}{\partial t}\right)^{2} \\
& \text { Let } \quad T_{0}=\sum_{i=1}^{n} \frac{1}{2} m_{i}\left(\frac{\partial x_{i}}{\partial t}\right)^{2} \\
& \quad T_{1 j}=\sum_{i=1}^{n} m_{i} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial t} \\
& \quad T_{2 j k}=\sum_{i=1}^{n} \frac{1}{2} m_{i} \frac{\partial x_{i}}{\partial q_{j}} \frac{\partial x_{i}}{\partial q_{k}}
\end{aligned}
$$

50

$$
T=T_{0}+\sum_{j=1}^{n} T_{1,} \dot{q}_{j}+\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}
$$

Now that a general expression for $T$ is availabe, recall trat

$$
L=T-V
$$

where $v$ is a function only of coordinates

$$
V=V\left(q_{1}, q_{2}, \ldots, q_{n}\right)
$$

using the expression for $\tau$

$$
\begin{aligned}
L & =T-V \\
& =T_{0}+\sum_{j=1}^{n} T_{1,} \dot{q}_{j}+\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}-V \\
& =T_{0}-V+\sum_{j=1}^{n} T_{1,} \dot{q}_{j}+\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}
\end{aligned}
$$

This is a form of the Lagransion as an expansion in powers of $9 i$ has many applications.

Now consider the energy function

$$
h=\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}-L
$$

Evaluation of the first term using the expression for $l$ gives

$$
\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial}{\partial q_{i}}\left(T_{0}-v\right)=0
$$

since, neither $T_{0}$ or $U$ depend on $q_{i}$

$$
\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial}{\partial q_{i}}\left\{\sum_{j=1}^{n} T_{1}, \dot{q}_{j}\right\}=\sum_{j=1}^{n} T_{1 j} \dot{q}_{j}
$$

and finally (Euler's Theorem of Homogeneous Functions)

$$
\begin{aligned}
& \sum_{i=1}^{n} \dot{q}_{i} \frac{\partial}{\partial q_{i}}\left\{\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}\right\} \\
& =2 \sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}
\end{aligned}
$$

Thus

$$
\begin{aligned}
& n=\sum_{j=1}^{n} T_{1 j} \dot{q}_{j}+2 \sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}- \\
& T_{0}-\sum_{j=1}^{n} T_{1 j} \dot{q}_{j}-\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}+v \\
& =T_{0}+\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}+v
\end{aligned}
$$

This is not the lotal energy since the term linear in 91 is missing,
In addition to the assumption that $U$ depends only on the $g_{i}$ in must also be assumed that the cartesian coordinates do not explictly depend on $t$ but have time dependence only through the generalized coordinats.

$$
x_{i}=x_{i}\left(q_{1}(t), q_{2}(t), \ldots, q_{n}(t)\right)
$$

then

$$
\frac{\partial x_{i}}{\partial t}=\partial
$$

it follows that the first two terms of $T$ vanish yielding the Lagranian

$$
L=\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}-v
$$

It follows that

$$
\begin{aligned}
h & =2 \sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}-\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}+v \\
& =\sum_{j=1}^{n} \sum_{k=1}^{n} T_{2 j k} \dot{q}_{j} \dot{q}_{k}+v
\end{aligned}
$$

Thus $h$ is the total energy which is conserved under the following
conditions conditions

1. $\frac{\partial L}{\partial t}=0$
2. $\frac{\partial x_{i}}{\partial t}=0$
3. $V=V\left(q_{1}, q_{2}, \ldots, q_{n}\right)$

## Lengendre Transform

Consider a function of the
form

$$
f=f\left(u_{1}, u_{2}, \ldots, u_{n}\right)
$$

Define a new function variable by

$$
v_{i}=\frac{\partial f}{\partial u_{i}}
$$

A new function of the $v_{i}$ is defined by

$$
g=\sum_{i=1}^{n} u_{i} v_{i}-f
$$

This is not obviously a function of only $v_{i}$. To see this Consider

$$
\begin{aligned}
d g & =\sum_{i=1}^{n}\left(u_{i} d v_{i}+v_{i} d u_{i}\right)-\sum_{i=1}^{n} \frac{\partial f}{\partial u_{i}} d u_{i} \\
& =\sum_{i=1}^{n} u_{i} d v_{i}+\sum_{i=1}^{n}\left(v_{i}-\frac{\partial f}{\partial u_{i}}\right) d u_{i}
\end{aligned}
$$

by definition

$$
\frac{\partial f}{\partial u_{i}}=v_{i}
$$

Now, if $g$ is assumed to depend only on the $v_{i}$

$$
g=g\left(v_{1}, v_{2}, \ldots, v_{n}\right)
$$

$$
\begin{aligned}
d g & =\sum_{i=1}^{n} u_{i} d v_{i} \\
& =\sum_{i=1}^{n} \frac{\partial g}{\partial v_{i}} d v_{i}
\end{aligned}
$$

Comparing terms gives

$$
u_{i}=\frac{\partial g}{\partial v_{i}}
$$

In summary

$$
\begin{array}{r}
f=f\left(u_{1}, u_{2}, \ldots, u_{n}\right) \\
v_{i}=\frac{\partial f}{\partial u_{i}} \quad u_{i}=\frac{\partial g}{\partial V_{i}} \\
g=\sum_{i=1}^{n} u_{i} v_{i}-f \quad f=\sum_{i=1}^{n} u_{i} v_{i}-g
\end{array}
$$

Next assume that in addition to $u_{i} f$ depends on variables $w_{i}$ independent of $u_{i}$,

$$
f=f\left(u_{1}, u_{2}, \ldots, u_{n} ; w_{1}, w_{2}, \ldots, w_{n}\right)
$$

where the $w_{i}$ are ignored by the transform. In this case the $w_{i}$ are called passive.
low, as before let

$$
\begin{gathered}
v_{i}=\frac{\partial f}{\partial u_{i}} \\
g=\sum_{i=1}^{n} u_{i} v_{i}-f\left(u_{1}, u_{2}, \ldots, u_{n} ; w_{1}, w_{2}, \ldots, w_{n}\right)
\end{gathered}
$$

and just as in the previous case

$$
\begin{aligned}
d g= & \sum_{i=1}^{n} u_{i} d v_{i}+v_{i} d u_{i}+d f \\
= & \sum_{i=1}^{n}\left(u_{i} d v_{i}+v_{i} d u_{i}\right)- \\
& \sum_{i=1}^{n}\left(\frac{\partial f}{\partial u_{i}} d u_{i}+\frac{\partial f}{\partial \omega_{i}} d \omega_{i}\right)
\end{aligned}
$$

$$
\begin{aligned}
&=\sum_{i=1}^{n}\left\{u_{i} d v_{i}-\frac{\partial f}{\partial w_{i}} d w_{i}\right. \\
&+ {\left.\left[v_{i}-\frac{\partial f}{\partial u_{i}}\right] d u_{i}\right\} } \\
&=\sum_{i=1}^{n} u_{i} d v_{i}-\frac{\partial f}{\partial w_{i}} d w_{i}
\end{aligned}
$$

form $g$ is assumed to have the

$$
\begin{array}{r}
g\left(v_{1}, v_{2}, \ldots, v_{n} ; \omega_{1}, \omega_{2}, \ldots, \omega_{n}\right) \\
d g=\sum_{i=1}\left\{\frac{\partial g}{\partial v_{i}} d v_{i}+\frac{\partial g}{\partial \omega_{i}} d \omega_{i}\right\}
\end{array}
$$

comparing terms gives

$$
u_{i}=\frac{\partial g}{\partial v_{i}} \quad \frac{\partial g}{\partial \omega_{i}}=-\frac{\partial f}{\partial \omega_{i}}
$$

In summary for

$$
f=f\left(u_{1}, u_{2}, \ldots, u_{n} ; w_{1}, w_{2}, \ldots, w_{n}\right)
$$

$$
\begin{aligned}
& g\left(v_{1}, v_{2}, \ldots, v_{n} ; \omega_{1}, \omega_{2}, \ldots, \omega_{n}\right) \\
& v_{1}=\frac{\partial f}{\partial u_{i}} \quad u_{i}=\frac{\partial g}{\partial v_{i}} \quad \frac{\partial g}{\partial \omega_{i}}=-\frac{\partial f}{\partial \omega_{i}} \\
& g=\sum_{i=1}^{n} u_{i} v_{i}-f \\
& f=\sum_{i=1}^{n} u_{i} v_{i}-g
\end{aligned}
$$

## The Hamiltonian

Previously it was shown that for a lagrangian defined by

$$
\begin{gathered}
L=L\left(q_{1}, q_{2}, \ldots, \dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n}, t\right) \\
\frac{d}{d t}\left(L-\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)=\frac{\partial L}{\partial t}
\end{gathered}
$$

if

1. $\frac{\partial L}{\partial t}=0$
2. $\frac{\partial x_{i}}{\partial t}=0$
3. $V=V\left(q_{1}, q_{2}, \ldots, q_{n}\right)$
then the total energy is

$$
E=\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}-L
$$

where

$$
E=T+V
$$

Recall that the generalized momentum is definied by,

$$
P_{i}=\frac{\partial L}{\partial \dot{q}_{i}}
$$

It follows that

$$
E=\sum_{i=1}^{n} \dot{q}_{i} p_{i}-L
$$

This has the form of a Legendre Transform between the variables $q_{i}$ and $p_{i}$
Define the Hamittonian by

$$
H=H\left(q_{1}, q_{2}, \ldots, q_{n} ; p_{1}, p_{2}, \ldots, p_{n}, t\right)
$$

then using the Legendre Transform

$$
H=\sum_{i=1}^{n} \dot{q}_{i} p_{i}-L
$$

## where the $q_{i}$ and $t$ are treated as passive variables.

with this definition it follows that

$$
\begin{array}{rlr}
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t} & \text { and } & \frac{\partial H}{\partial q_{i}}
\end{array}=-\frac{\partial L}{\partial q_{i}}
$$

So

$$
\frac{d}{d t}\left(L-\sum_{i=1}^{n} \dot{q}_{i} \frac{\partial L}{\partial \dot{q}_{i}}\right)=\frac{\partial L}{\partial t}
$$

implies that

$$
\frac{d H}{d t}=\frac{\partial H}{\partial t}
$$

and if

$$
\frac{\partial H}{\partial t}=0
$$

t) is conserved since

$$
\frac{d t}{d t}=0
$$

## Hamilton's Canonical Equations

The definintion of $H$ by the Legendre Transform

$$
H=\sum_{i=1}^{n} \dot{q}_{i} p_{i}-L
$$

implies that

$$
p_{i}=\frac{\partial L}{\partial \dot{\varphi}_{i}} \text { and } \dot{\varphi}_{i}=\frac{\partial H}{\partial p_{i}}
$$

and by the passive variable

$$
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t} \text { and } \frac{\partial H}{\partial q_{i}}=-\frac{\partial L}{\partial q_{i}}
$$

From lagranges equation

$$
\begin{aligned}
& \frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}_{i}}\right)-\frac{\partial L}{\partial q_{i}}=0 \\
\Rightarrow & \frac{\partial L}{\partial q_{i}}=\frac{d}{d t}\left(\frac{\partial L}{\partial \dot{q}}\right)=\frac{d}{d t} p_{i}=\dot{p}_{i}
\end{aligned}
$$

so

$$
\frac{\partial H}{\partial q_{i}}=-\frac{\partial L}{\partial q_{i}}=-\dot{p}_{i}
$$

Bringing these results together detines Hamilton's Cannonical equations

$$
\dot{p}_{i}=-\frac{\partial H}{\partial q_{i}}, \dot{q}_{i}=\frac{\partial H}{\partial p_{i}}, \frac{d H}{d t}=\frac{\partial H}{\partial t}
$$

Using these quations it is seen that for

$$
\begin{aligned}
H & =H\left(q_{1}, q_{2}, \ldots, q_{n} i p_{1}, p_{2}, \ldots, p_{n}, t\right) \\
\frac{\partial H}{\partial t} & =\sum_{i=1}^{n}\left\{\frac{\partial H}{\partial q_{i}} \dot{q}_{i}+\frac{\partial H}{\partial p_{i}} \dot{p}_{i}\right\}+\frac{\partial H}{\partial t} \\
& =\sum_{i=1}^{n}\left\{-\dot{p}_{i} / \dot{q}_{i}+\dot{q}_{i} \dot{p}_{i}\right\}+\frac{\partial H}{\partial t} \\
& =\frac{\partial H}{\partial t}
\end{aligned}
$$

Thus if

$$
\frac{\partial H}{\partial t}=0 \Rightarrow \frac{d H}{d t}=0
$$

## the flamiltonian is conserved

In the Hamiltonian fomalisim The Lagrangian model of $n$ second order differential equations has been converted to an first order equations.
Anothe difference between the Lagrangran and Hamittonian formalism is that the Hamittonian fomelisim introduces the momentum $\mathrm{p}_{i}$ as a coordinate.

The Lagrangian formalism only uses spatial coordinates $q_{1}, q_{2}, \ldots, q_{n}$ refered to as configuration space
The Hamiltonian tórmalism uses both $q_{1}, q_{2}, \ldots, q_{n}$ and $p_{1}, p_{2}, \ldots, p_{n}$ referred to as phase space
If the Hamiltonian is conserved

$$
H\left(q_{1}, q_{2}, \ldots, q_{n} ; p_{1}, p_{2}, \ldots, p_{n}\right)=\text { constant }
$$

defines a surface in phase space which contains all possible states accessible by the system.

The Hamiltonian contains no derivatives unlike the Lagrangian
which contains both first and second derivatives.

## Hamitton's Equations from Hamiton's Principal

Now

$$
\begin{aligned}
H & =\sum_{i=1}^{n} \dot{q}_{i} p_{i}-L \\
\Rightarrow L & =\sum_{i=1}^{n} \dot{q}_{i} p_{i}-H
\end{aligned}
$$

Hamitor's Pricipal becomes

$$
\begin{aligned}
\delta I & =\delta \int_{t_{s}}^{t_{f}} L d t \\
& =\delta \int_{t_{s}}^{t_{f}}\left\{\sum_{i=1}^{n} \dot{q}_{i} P_{i}-H\left(q_{i}, P_{i}, t\right)\right\} d t
\end{aligned}
$$

Let
$f\left(q_{i}, \dot{q}_{i}, p_{i}, \dot{p}_{i}, t\right)=\dot{q}_{i} p_{i}-H\left(q_{i}, p_{i}, t\right)$
Since $q_{i}$ and $p_{i}$ are independent The Lagrange - Euler equations are seperate equatrons for $q_{i}$ and pc

$$
\begin{aligned}
& \frac{d}{d t}\left(\frac{\partial f}{\partial \dot{q}_{i}}\right)-\frac{\partial f}{\partial q_{i}}=0 \\
& \frac{d}{d t}\left(\frac{\partial f}{\partial \dot{p}_{i}}\right)-\frac{\partial f}{\partial p_{i}}=0
\end{aligned}
$$

Evaluation of the first equation with

$$
f=\dot{q}_{i} p_{i}-H\left(q_{i}, p_{i}, t\right)
$$

gives

$$
\frac{d}{d t}\left\{P_{i}-\frac{\partial H}{\partial \dot{q}_{i}}\right\}+\frac{\partial H}{\partial q_{i}}=0
$$

since

$$
\begin{gathered}
\frac{\partial H}{\partial \dot{q}_{i}}=0 \\
\frac{d p_{i}}{d t}=\dot{p}_{i}=-\frac{\partial t}{\partial q i}
\end{gathered}
$$

and for the last equations

$$
\frac{d}{d t}\left\{-\frac{\partial H}{\partial p_{i}}\right\}-\left\{q_{i}-\frac{\partial H}{\partial p_{i}}\right\}=0
$$

Since

$$
\begin{aligned}
& \frac{\partial H}{\partial \dot{p}_{i}}=0 \\
& \dot{q}_{i}=\frac{\partial H}{\partial p_{i}}
\end{aligned}
$$

Thus Hamilton's equations were
obtained

$$
\begin{aligned}
& \dot{p}_{i}=-\frac{\partial H}{\partial q_{i}} \\
& \dot{q}_{i}=\frac{\partial H}{\partial p_{i}}
\end{aligned}
$$

## Canonical Tranformations

A Canonical transformation is a phase space transformation from a set of coordinates
$\left(p_{i}, q_{i}\right)$ to a new set of coordinates
$\left(P_{i}, Q_{i}\right)$ that preserve the form of Hamilton's equations.
For coordinates $\left(p_{i}, q_{i}\right)$ Hamilton's equations are

$$
\dot{q}=\frac{\partial H}{\partial p_{i}} \quad \dot{p}_{i}=-\frac{\partial H}{\partial q_{i}}
$$

In the new coordinates $\left(P_{i}, Q_{i}\right)$ the Hamiltonian could have a different form so it will be dended by $K\left(P_{i}, Q_{i}, t\right)$ and Hamilton's canonical equations produced by the transform are

$$
\dot{Q}_{i}=\frac{\partial K}{\partial P_{i}} \quad \dot{P}_{i}=-\frac{\partial K}{\partial Q_{i}}
$$

Recall that the Hamiltonian and Lagrangian are related b) the legendre transform

$$
H=\sum_{i=1}^{n} \dot{q}_{1} P_{i}-L
$$

where

$$
P_{i}=\frac{\partial L}{\partial \dot{q}_{i}}
$$

and

$$
L=\sum_{i=1}^{n} \dot{q}_{i} p_{i}-H\left(q_{i}, p_{i}, t\right)
$$

It follows from Hamilton's principal that

$$
\begin{aligned}
& \delta \int_{t_{s}}^{t_{f}} L d t=0 \\
\Rightarrow \quad & \delta \int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\dot{q}_{i} p_{i}-H\left(q_{i}, p_{i}, t\right)\right\} d t
\end{aligned}
$$

The requirement that canonical transformation preserves Hamilton's equation leads to

$$
\delta \int_{t_{s}}^{t_{f}} \sum_{i=1}^{n}\left\{\dot{Q}_{i} P_{i}-K\left(Q_{i}, P_{i}, t\right)\right\} d t
$$

This requirement can be relaxed somewhat be noting that the time derivative of an arbitrary function of the coordinates can be added because it does not

Charge the result since the variation at the endpoint must vanish. $F$ is called the generating function. A choice which will later be clear

$$
\begin{aligned}
& \delta \int_{t_{s}}^{t_{f}} \frac{d F}{d t}\left(Q_{i}, P_{i}, q_{i}, P_{i}, t\right) \\
& =\delta\left[F\left(Q_{i}, P_{i}, q_{i}, P_{i}, t_{f}\right)-\right. \\
& \left.F\left(Q_{i}, P_{i}, q_{i}, P_{i}, t_{s}\right)\right]
\end{aligned}
$$

It follows that Hamilton's Principal becomes
$\delta \int_{t_{s}}^{-t f} \sum_{i=1}^{n}\left\{\dot{Q}_{i} \dot{P}_{i}-K\left(Q_{i}, P_{i}, t\right)-\right.$

$$
\frac{\left.d F\left(Q_{i}, P_{i}, q_{i}, P_{i}, t\right)\right\} d t}{d t}
$$

Now the variational calculation for $H\left(q_{i}, p_{i}, t\right)$ produces the correct dynamical equations. So assume that

$$
\begin{aligned}
\dot{q}_{i} P_{i}-H\left(q_{i}, P_{i}, t\right)= & \dot{Q}_{i} P_{i}-K\left(Q_{i}, P_{i}, t\right)+ \\
& \frac{d F}{d t}\left(Q_{i}, P_{i}, q_{i}, P_{i}, t_{f}\right)
\end{aligned}
$$

So far it has been assumed trat $F$ has the form

$$
F\left(Q_{i}, P_{i}, q_{i}, P_{i}, t\right)
$$

A more convient form to continue with is

$$
F_{1}\left(q_{i}, Q_{i}, t\right)
$$

It follows that

$$
\frac{d F_{1}}{d t}=\frac{\partial F_{1}}{\partial Q_{i}} \dot{Q}_{i}+\frac{\partial F_{1}}{\partial q_{i}} \dot{\varphi}_{i}+\frac{\partial F}{\partial t}
$$

so
$\dot{q}_{i} \bar{P}_{i}-H=\dot{Q}_{i} \bar{P}_{i}-K+\frac{\partial F_{1}}{\partial Q_{i}} \dot{Q}_{i}+\frac{\partial F_{1}}{\partial q_{i}} \dot{q}_{i}+\frac{\partial F}{\partial t}$
$\Rightarrow\left(P_{i}-\frac{\partial F_{1}}{\partial q_{i}}\right) \dot{q}_{i}-\left(P_{i}+\frac{\partial F_{1}}{\partial Q_{i}}\right) \dot{Q}_{i}$
$=H-K+\frac{\partial E_{1}}{\partial t}$
A solution to this equation is
$p_{i}-\frac{\partial F_{1}}{\partial q_{i}}=0 \Rightarrow p_{i}=\frac{\partial F_{1}}{\partial q_{i}}$
$P_{i}+\frac{\partial F_{1}}{\partial Q_{i}}=0 \Rightarrow P_{i}=-\frac{\partial F_{1}}{\partial Q_{i}}$
$H-K+\frac{\partial F_{1}}{\partial t}=0 \Rightarrow K=H+\frac{\partial F_{1}}{\partial t}$
The first equation will have a solution of the form

$$
P_{i}=P_{i}\left(q_{i}, Q_{i}, t\right)
$$

Assume this equation is invertable

$$
Q_{i}=Q_{i}\left(p_{i}, q_{i}, t\right)
$$

The second equation gives

$$
P_{i}=P_{i}\left(q_{i}, Q_{i}, t\right)
$$

using the expression for $Q_{i}$

$$
P_{i}=P_{i}\left(p_{i}, q_{i}, t\right)
$$

To get a sense of how this works consider the following generating function

$$
F_{1}\left(q_{i}, Q_{i}, t\right)=q_{i} Q_{i}
$$

So the tranformed Hamiltonian is equal to the original Hamiltonian

$$
K=H+\frac{\partial F_{1}}{\partial t}=H
$$

and

$$
\begin{aligned}
& P_{i}=-\frac{\partial F_{1}}{\partial Q_{i}}=-q_{i} \\
& P_{i}=\frac{\partial F_{1}}{\partial q_{i}}=Q_{i}
\end{aligned}
$$

Thus the generated transformation interchances the momentum into the coordinate.

Consider the following addional forms of generating function

$$
\begin{aligned}
& F_{1}\left(q_{i}, Q_{i}, t\right) \\
& F_{2}\left(q_{i}, P_{i}, t\right) \\
& F_{3}\left(p_{i}, Q_{i}, t\right) \\
& F_{4}\left(p_{i}, P_{i}, t\right)
\end{aligned}
$$

Using

$$
\begin{aligned}
\dot{q}_{i} p_{i}-H\left(q_{i}, p_{i}, t\right)= & \dot{Q}_{i} P_{i}-K\left(Q_{i}, P_{i}, t\right)+ \\
& \frac{d F}{d t}\left(Q_{i}, P_{i}, q_{i}, P_{i}, t_{f}\right)
\end{aligned}
$$

and

$$
\begin{array}{ll}
\dot{q}=\frac{\partial H}{\partial P_{i}} & \dot{P}_{i}=-\frac{\partial H}{\partial q_{i}} \\
\dot{Q}_{i}=\frac{\partial K}{\partial P_{i}} & \dot{P}_{i}=-\frac{\partial K}{\partial Q_{i}}
\end{array}
$$

Find solutions for each assumed form for the generating function. Arbitrary prodets of the coordinates can be subtracted the generating function since it has zero variation.

1) $F_{2}\left(q_{i}, P_{i}, t\right)-P_{i} Q_{i}$

$$
\begin{aligned}
\frac{d F_{2}}{d t} & =\frac{\partial F_{2}}{\partial q_{i}} \dot{q}_{i}+\frac{\partial F_{2}}{\partial P_{i}} \dot{P}_{i}+\frac{\partial F_{2}}{\partial t}-\dot{P}_{i} Q_{i}-P_{i} \dot{Q}_{i} \\
& =\frac{\partial F_{2}}{\partial q_{i}} \dot{q}+\left(\frac{\partial F_{2}}{\partial P_{i}}-Q_{i}\right) \dot{P}_{i}+\frac{\partial E_{2}}{\partial t}-P_{i} \dot{Q}_{i}
\end{aligned}
$$

inserting into the transform equation and collecting terms gives
$=\left(P_{i}-\frac{\partial F_{2}}{\partial q_{i}}\right) \dot{q}_{i}+\left(Q_{i}-\frac{\partial F_{2}}{\partial P_{i}}\right) \dot{P}_{i}-H+k-\frac{\partial F_{2}}{\partial t}=0$
The solution were the components vanish is given by,

$$
\begin{aligned}
& P^{i}=\frac{\partial F_{3}}{\partial q_{i}} \\
& Q_{i}=\frac{\partial F_{2}}{\partial P_{i}} \\
& K=H+\frac{\partial F_{2}}{\partial t}
\end{aligned}
$$

2) $F_{3}\left(p_{i}, Q_{i}, t\right)+p_{i} q_{i}$

$$
\begin{aligned}
\frac{d F_{3}}{d t}= & \frac{\partial F_{3}}{\partial p_{i}} \dot{p}_{i}+\frac{\partial F_{3}}{\partial Q_{i}} \dot{Q}_{i}+\frac{\partial F_{3}}{\partial t}+\dot{p}_{i} q_{i} \\
& +p_{i} \dot{q}_{i}
\end{aligned}
$$

Inserting into the transformation equation and collecting terms gives

$$
\begin{aligned}
-H= & \left(\frac{\partial F_{3}}{\partial Q_{i}}+P_{i}\right) \dot{Q}_{i}+\left(\frac{\partial F_{3}}{\partial P_{i}}+q_{i}\right) \dot{P}_{i} \\
& -K+\frac{\partial F_{3}}{\partial t}
\end{aligned}
$$

the solution where components vanish is given b/.

$$
\begin{aligned}
& P_{i}=-\frac{\partial F_{3}}{\partial Q_{i}} \\
& q_{i}=-\frac{\partial F_{3}}{\partial P_{i}} \\
& K=H+\frac{\partial F_{3}}{\partial t}
\end{aligned}
$$

3) $F_{4}\left(p_{i}, P_{i}, t\right)+p_{i} q_{i}-P_{i} Q_{i}$

$$
\begin{aligned}
\frac{d F_{y}}{d t}= & \frac{\partial F_{4}}{\partial P_{i}} \dot{P}_{i}+\frac{\partial F_{4}}{\partial P_{i}} \dot{P}_{i}+\frac{\partial F_{4}}{\partial t}+\dot{P}_{i} q_{i}+p_{i} / \dot{q}^{7} \\
& -\dot{P}_{i} Q_{i}-P_{i} \dot{Q}_{i}
\end{aligned}
$$

Inserting into the transformation equation and collecting terms gives

$$
\begin{aligned}
-H=-K & +\left(\frac{\partial F_{4}}{\partial P_{i}}+q_{i}\right) \dot{P}_{i}+\left(\frac{\partial F_{4}}{\partial P_{i}}-Q\right) P_{i} \\
& +\frac{\partial F_{4}}{\partial t}
\end{aligned}
$$

The solution were the components vanish is given by,

$$
\begin{aligned}
& q_{i}=-\frac{\partial F_{y}}{\partial P_{i}} \\
& Q_{i}=\frac{\partial F_{y}}{\partial P_{i}} \\
& K=H+\frac{\partial F_{u}}{\partial t}
\end{aligned}
$$

An interesting example of the $F_{2}$ type generating function is

$$
F_{2}=\sum_{i=1}^{n} q_{i} P_{i}
$$

Show that this generating function produces the identity transform

$$
\begin{aligned}
& Q_{i}=q_{i} \\
& P_{i}=p_{i}
\end{aligned}
$$

For $F_{2}$ type generating function

$$
\begin{aligned}
& P_{i}=\frac{\partial F_{2}}{\partial q_{i}} \\
& Q_{i}=\frac{\partial F_{2}}{\partial P_{i}} \\
& K=H+\frac{\partial F}{\partial t}
\end{aligned}
$$

For $P_{i}$

$$
\begin{aligned}
P_{i}=\frac{\partial F_{2}}{\partial q_{i}} & =\frac{\partial}{\partial q_{i}} \sum_{j=1}^{n} q_{j} P_{j} \\
& =\sum_{j=1} P_{j} \delta_{i j} \\
& =P_{i}
\end{aligned}
$$

and for $Q_{i}$

$$
\begin{aligned}
Q_{i}=\frac{\partial F_{2}}{\partial P_{c}} & =\frac{\partial}{\partial P_{l}} \sum_{j=1}^{n} q_{j} P_{j} \\
& =\sum_{j=1}^{n} q_{j} \delta_{i j} \\
& =q_{i}
\end{aligned}
$$

Thus

$$
F_{2}=\sum_{i=1}^{n} q_{i} P_{i}
$$

is the identity transform

$$
\begin{aligned}
& P_{i}=P_{i} \\
& Q_{i}=q_{i} \\
& K=H
\end{aligned}
$$

## Poisson Brackets

Let $P$ and 9 be cannonical variables with Hamittonian, H

$$
\begin{aligned}
& \dot{q}=\frac{\partial H}{\partial p} \\
& \dot{p}=-\frac{\partial H}{\partial q}
\end{aligned}
$$

Then the Porsson Bracket of two functions of the canonical variables is defined by,

$$
[u, v]_{p, q}=\frac{\partial u}{\partial q} \frac{\partial v}{\partial p}-\frac{\partial u}{\partial p} \frac{\partial v}{\partial q}
$$

for a sustem with $2 n$ degrees of freedom

$$
[u, v]=\sum_{i=1}^{n} \frac{\partial u}{\partial q_{i}} \frac{\partial v}{\partial p_{i}}-\frac{\partial u}{\partial p_{i}} \frac{\partial v}{\partial q_{i}}
$$

From the definition of the Poisson Bracket

$$
\left[q_{i}, q_{j}\right]=\sum_{k=1}^{n} \frac{\partial q_{i}}{\partial q_{k}} \frac{\partial q_{j}}{\partial p_{k}}-\frac{\partial q_{i}}{\partial p_{k}} \frac{\partial q_{j}}{\partial q_{k}}
$$

$$
=\sum_{k=1}^{n} \delta_{i k}-\delta_{j k}=1-1=0
$$

similarly

$$
\begin{aligned}
{\left[p_{i}, p_{j}\right] } & =\sum_{k=1}^{n} \frac{\partial p_{i}}{\partial q_{k}} \frac{\partial p_{j}}{\partial p_{k}}-\frac{\partial p_{i}}{\partial p_{k}} \frac{\partial p_{j}}{\partial q_{k}} \\
& =\sum_{k=1}^{n} \delta_{j k}-\delta_{i k}=1-1=0
\end{aligned}
$$

and

$$
\begin{aligned}
{\left[q_{i}, p_{j}\right] } & =\sum_{k=1}^{n} \frac{\partial q_{i}}{\partial q_{k}} \frac{\partial p_{j}}{\partial p_{k}}-\frac{\partial q_{i}}{\partial p_{k}} \frac{\partial p_{j}}{\partial q_{k}} \\
& =\sum_{k=1}^{n} \delta_{i k} \delta_{j k} \\
& =\delta_{i j} \\
{\left[p_{j}, q_{i}\right] } & =\sum_{k=1}^{n} \frac{\partial p_{j}}{\partial q_{k}} \frac{\partial q_{i}}{\partial p_{k}}-\frac{\partial p_{j}}{\partial p_{k}} \frac{\partial q_{i}}{\partial q_{k}} \\
& =\sum_{k=1}^{n}-\delta_{j k} \delta_{i k} \\
& =-\delta_{i j}
\end{aligned}
$$

in summar/

$$
\begin{aligned}
& {\left[q_{i}, q_{j}\right]=0} \\
& {\left[p_{i}, p_{j}\right]=0} \\
& {\left[q_{i}, p_{j}\right]=\delta_{i j}} \\
& {\left[p_{j}, q_{i}\right]=-\delta_{i j}}
\end{aligned}
$$

Prove the following relations for the Poisson Brackets of the functions of cannonical variables $u$ and $v$

1) $[u, u]=0$
2) $[u, v]=-[v, u]$

If $a$ and $b$ are arbitrary fundions that do not contain the canonical variables
3) $[a u+b v, \omega]=a[u, \omega]+b[v, \omega]$
4) $[u v, \omega]=[u, \omega] v+u[v, \omega]$
5) $[u,[v, w]]+[v,[w, u]]+[w,[u, v]]=0$

## Proof (1)

$$
[u, u]=\frac{\partial u}{\partial q} \frac{\partial u}{\partial p}-\frac{\partial u}{\partial q} \frac{\partial u}{\partial p}=0
$$

Proof (2) Anticommunitation

$$
\begin{aligned}
{[u, v] } & =\frac{\partial u}{\partial q} \frac{\partial v}{\partial p}-\frac{\partial v}{\partial q} \frac{\partial u}{\partial p} \\
& =-\left\{\frac{\partial v}{\partial q} \frac{\partial u}{\partial p}-\frac{\partial u}{\partial q} \frac{\partial v}{\partial p}\right\} \\
& =-[u, v]
\end{aligned}
$$

Proof (3)

$$
\begin{aligned}
& {[a u+b v, \omega]=\frac{\partial}{\partial q}(a u+b v) \frac{\partial \omega}{\partial p}} \\
& -\frac{\partial \omega}{\partial q} \frac{\partial(a u+b v)}{\partial p} \\
& =\frac{\partial(a \omega)}{\partial q} \frac{\partial \omega}{\partial p}+\frac{\partial(b v)}{\partial q} \frac{\partial \omega}{\partial p}-\frac{\partial \omega}{\partial q} \frac{\partial(a u)}{\partial p} \\
& -\frac{\partial \omega}{\partial q} \frac{\partial(b v)}{\partial p}
\end{aligned}
$$

$$
\begin{aligned}
= & a \frac{\partial u}{\partial q} \frac{\partial w}{\partial p}+b \frac{\partial v}{\partial q} \frac{\partial w}{\partial p}-a \frac{\partial w}{\partial q} \frac{\partial u}{\partial p} \\
& -b \frac{\partial v}{\partial q} \frac{\partial u}{\partial p} \\
= & a\left\{\frac{\partial u}{\partial q} \frac{\partial w}{\partial p}-\frac{\partial w}{\partial q} \frac{\partial u}{\partial p}\right\}+b\left\{\frac{\partial v}{\partial q} \frac{\partial w}{\partial p}\right. \\
& \left.-\frac{\partial w}{\partial q} \frac{\partial v}{\partial p}\right\} \\
= & a[u, w]+b[v, w]
\end{aligned}
$$

Proof 4

$$
\begin{aligned}
& {[u v, \omega]=\frac{\partial(u v)}{\partial q} \frac{\partial \omega}{\partial p}-\frac{\partial \omega}{\partial q} \frac{\partial(u v)}{\partial p}} \\
& =\left\{\frac{\partial u}{\partial q} v+u \frac{\partial v}{\partial q}\right\} \frac{\partial \omega}{\partial p}-\frac{\partial \omega}{\partial q}\left\{\frac{\partial u}{\partial p} v\right. \\
& \left.+u \frac{\partial v}{\partial p}\right\} \\
& =\frac{\partial u}{\partial q} \frac{\partial \omega}{\partial p} v+u \frac{\partial v}{\partial q} \frac{\partial \omega}{\partial p}-\frac{\partial \omega}{\partial q} \frac{\partial u}{\partial p} v \\
& -u \frac{\partial \omega}{\partial q} \frac{\partial v}{\partial p}
\end{aligned}
$$

$$
\begin{aligned}
= & \left\{\frac{\partial u}{\partial q} \frac{\partial w}{\partial p}-\frac{\partial w}{\partial q} \frac{\partial u}{\partial p}\right\} v+u\left\{\frac{\partial v}{\partial q} \frac{\partial w}{\partial p}\right. \\
& \left.\frac{\partial w}{\partial q} \frac{\partial v}{\partial p}\right\} \\
= & {[u, w] v+u[v, w] }
\end{aligned}
$$

## Proof (5)

Consider

$$
\begin{aligned}
& {[u,[v, w]]=\frac{\partial u}{\partial q} \frac{\partial}{\partial p}\left\{\frac{\partial v}{\partial q} \frac{\partial w}{\partial p} \cdot \frac{\partial w}{\partial q} \frac{\partial v}{\partial p}\right\}} \\
& -\frac{\partial}{\partial q}\left\{\frac{\partial v}{\partial q} \frac{\partial w}{\partial p} \cdot \frac{\partial w}{\partial q} \frac{\partial v}{\partial p}\right\} \frac{\partial u}{\partial p} \\
& =\frac{\partial u}{\partial q}\left\{\frac{\partial^{2} v}{\partial p \partial q} \frac{\partial w}{\partial p}+\frac{\partial v}{\partial q} \frac{\partial^{2} w}{\partial p^{2}}-\frac{\partial^{2} w}{\partial p \partial q} \frac{\partial v}{\partial p}\right. \\
& \left.-\frac{\partial w}{\partial q} \frac{\partial^{2} v}{\partial p^{2}}\right\}-\left\{\frac{\partial^{2} v}{\partial q^{2}} \frac{\partial w}{\partial p}+\frac{\partial v}{\partial q} \frac{\partial^{2} w}{\partial q \partial p}\right. \\
& \left.-\frac{\partial w}{\partial q^{2}} \frac{\partial v}{\partial p}-\frac{\partial w}{\partial q} \frac{\partial^{2} v}{\partial q \partial p}\right\} \frac{\partial u}{\partial p}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{\partial u}{\partial \varphi} \frac{\partial^{2} v}{\partial p \partial q} \frac{\partial w}{\partial p}+\frac{\partial u}{\partial \varphi} \frac{\partial v}{\partial \varphi} \frac{\partial^{2} w}{\partial p^{2}}-\frac{\partial u}{\partial q} \frac{\partial^{2} w}{\partial p \partial q} \frac{\partial v^{2}}{\partial p} \\
& -\frac{\partial u}{\partial q} \frac{\partial \omega^{3}}{\partial q} \frac{\partial^{2} v}{\partial p^{2}}-\frac{\partial^{2} v}{\partial q^{2}} \frac{\partial \omega^{4}}{\partial p} \frac{\partial u}{\partial p}-\frac{\partial v}{\partial q} \frac{\partial^{2} u v^{5}}{\partial q \partial p} \frac{\partial u}{\partial p} \\
& +\frac{\partial^{2} w}{\partial q^{2}} \frac{\partial v}{\partial p} \frac{\partial u}{\partial p}+\frac{\partial w}{\partial q} \frac{\partial^{2} w}{\partial q \partial p} \frac{\partial u}{\partial p} \\
& \text { and } \\
& \text { и } \cup \text { w } \\
& 12 \\
& {[v,[\omega, u]]=\frac{\partial v}{\partial q} \frac{\partial^{2} \omega}{\partial p} \frac{\partial u}{\partial p}+\frac{\partial v}{\partial v} \frac{\partial^{2} u}{\partial p}} \\
& \frac{\partial q}{\partial p \partial q} \overline{\partial p} \quad \overline{\partial q} / \overline{\partial q} \quad \overline{\partial p^{2}} \\
& -\frac{\partial v}{\partial g} \frac{\partial^{2} u}{\partial p \partial g} \frac{\partial w}{\partial p}-\frac{\partial^{2} w}{\partial q^{2}} \frac{\partial u}{\partial p} \frac{\partial v}{\partial p}-\frac{\partial w}{\partial q} \frac{\partial^{2} u^{9}}{\partial q \partial p} \frac{\partial v}{\partial p} \\
& +\frac{\partial^{2} u}{\partial q^{2}} \frac{\partial \omega^{10}}{\partial p} \frac{\partial v}{\partial p}+\frac{\partial u}{\partial q} \frac{\partial^{2} \omega}{\partial q p} \frac{\partial v}{\partial p}-\frac{\partial v}{\partial q} \frac{\partial u}{\partial q} \frac{\partial^{2} \omega}{\partial p^{2}} \\
& \text { and } \\
& {\left[\begin{array}{c}
u \\
n^{7}
\end{array}[u, v]\right]=\frac{\partial \omega^{1}}{\partial \varphi} \frac{\partial^{2} u}{\partial p} \frac{\partial v}{\partial p}+\frac{\partial \omega}{\partial \varphi} \frac{\partial u}{\partial \varphi} \frac{\partial^{2} v}{\partial p^{2}}} \\
& -\frac{\partial \omega}{\partial q} \partial^{2} v \frac{\partial u}{\partial p}-\partial^{2} u \partial^{10} \partial w-\partial u^{1} \partial^{2} v \partial w \\
& \overline{\partial q} \overline{\partial p} \partial q \overline{\partial p} \quad \frac{\partial q^{2}}{\partial p} \overline{\partial p} \quad \partial q \quad \partial q \partial p \quad \partial p \\
& +\left.\frac{\partial^{2} v^{n}}{\partial q^{2}}\right|^{\frac{\partial u}{\partial p}} \frac{\partial w}{\partial p}+\frac{\partial v^{r}}{\partial q} \frac{\partial^{2} u}{\partial q \partial p} \frac{\partial w}{\partial p}-\frac{\partial w^{12}}{\partial q} \frac{\partial v^{2}}{\partial q} \frac{\partial^{2} u}{\partial p^{2}}
\end{aligned}
$$

Collecting terms gives the desired result
$[u,[v, w]]+[v,[w, u]]+[w,[u, v]]=0$ Equations of Motion
Consider a function of canonical coordinates u

$$
\begin{aligned}
\frac{d u}{d t} & =\left\{\sum_{i=1}^{n} \frac{\partial u}{\partial q_{i}} \frac{d q}{d t}+\frac{\partial u}{\partial p_{i}} \frac{d p}{d t}\right\}+\frac{\partial u}{\partial t} \\
& =\left\{\sum_{i=1}^{n} \frac{\partial u}{\partial q_{i}} \dot{q}_{i}+\frac{\partial u}{\partial p_{i}} \dot{p}_{i}\right\}+\frac{\partial u}{\partial t}
\end{aligned}
$$

but from the equations of motion

$$
\dot{q}_{i}=\frac{\partial H}{\partial p_{i}} \quad \dot{p}_{i}=-\frac{\partial H}{\partial q_{i}}
$$

So

$$
\begin{aligned}
\frac{d u}{d t} & =\left\{\sum_{i=1}^{n} \frac{\partial u}{\partial q_{i}} \frac{\partial H}{\partial p_{i}}-\frac{\partial u}{\partial p_{i}} \frac{\partial H}{\partial q_{i}}\right\}+\frac{\partial H}{\partial t} \\
& =[u, H]+\frac{\partial H}{\partial t}
\end{aligned}
$$

if $u$ is constant

$$
\begin{aligned}
& \frac{d u}{d t}=0=[u, H]+\frac{\partial u}{\partial t} \\
& \Rightarrow[u, H]=-\frac{\partial u}{\partial t}
\end{aligned}
$$

furthur if $u$ does not deperd
explicitly on $t$ explicitly on $t$

$$
[u, H]=0
$$

Now consider the Poission brackets

$$
\begin{aligned}
{[q, H] } & =\frac{\partial q}{\partial q} \frac{\partial H}{\partial p}+\frac{\partial q}{\partial p} \frac{\partial H}{\partial q} \\
& =\frac{\partial H}{\partial p} \\
& =\dot{q}
\end{aligned}
$$

since

$$
\begin{gathered}
\frac{\partial q}{\partial q}=1 \quad \frac{\partial q}{\partial q}=0 \\
\dot{q}=[q, H]
\end{gathered}
$$

similarly

$$
\begin{aligned}
{[p, H] } & =\frac{\partial p}{\partial q} \frac{\partial H}{\partial p}-\frac{\partial p}{\partial p} \frac{\partial H}{\partial q} \\
& =-\frac{\partial H}{\partial q} \\
& =\dot{p}
\end{aligned}
$$

Thes

$$
\dot{p}=[p, H]
$$

Now

$$
\begin{aligned}
\frac{d H}{d t} & =\frac{\partial H}{\partial q} \dot{q}+\frac{\partial H}{\partial p} \dot{p}+\frac{\partial H}{\partial t} \\
& =\frac{\partial H}{\partial q} \frac{\partial H}{\partial p}+\frac{\partial H}{\partial p}\left(-\frac{\partial H}{\partial q}\right)+\frac{\partial H}{\partial t} \\
& =\frac{\partial H}{\partial q} \frac{\partial H}{\partial p}-\frac{\partial H}{\partial p} \frac{\partial H}{\partial q}+\frac{\partial H}{\partial t} \\
& =[H, H]+\frac{\partial H}{\partial t}
\end{aligned}
$$

but

$$
[H, H]=0
$$

sc

$$
\frac{d H}{d t}=\frac{\partial H}{\partial t}
$$

## Infinitesimal Canonical Transformations

In an Infinitsimal canonical transformalion the new coordinate differ only infinitesimally from the old coordinates.
It follows that

$$
\begin{aligned}
& Q_{i}=q_{i}+\delta q_{i} \\
& P_{i}=p_{i}+\delta p_{i}
\end{aligned}
$$

Here $\delta$ should be interpreted as used in variatronal calculations not as virtual displocement.
Now recall the identity transformation

$$
F_{2}=\sum_{i=1}^{n} q_{i} P_{i}
$$

$P_{i}=\frac{\partial F_{2}}{\partial q_{i}} \quad Q_{i}=\frac{\partial F_{2}}{\partial P_{i}} \quad K=H+\frac{\partial F}{\partial t}$
Let $G\left(q_{1}, q_{2}, \ldots, q_{n} ; P_{1}, P_{2}, \ldots, P_{n}, t\right)$ be
an arbitrary type 2 transfomation.
It follows that the infintesimal canonical transformation that differs
infinitesimally from the identity transformation has a generating function given by
$F_{2}\left(q_{1}, q_{2}, \ldots, q_{n} ; P_{1}, P_{2}, \ldots, P_{n}, t\right)$
$=\sum_{i=1}^{n} q_{i} P_{i}+\epsilon G\left(q_{1}, q_{2}, \ldots, q_{n}, P_{1}, P_{2}, \ldots, P_{n}, t\right)$
where $\epsilon$ is abritraly small, infintesimal, quantity.
Now using the transformation equations

$$
\begin{aligned}
& P_{i}=\frac{\partial F_{3}}{\partial q_{i}}=P_{i}+\epsilon \frac{\partial f}{\partial q_{i}} \\
& Q_{i}=\frac{\partial F_{3}}{\partial P_{i}}=q_{i}+\epsilon \frac{\partial f}{\partial P_{i}}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
& \delta q_{i}=Q_{i}-q_{i}=\epsilon \frac{\partial G}{\partial p_{i}} \\
& \delta p_{i}=P_{i}-P_{i}=-\frac{\epsilon \partial G}{\partial q_{i}}
\end{aligned}
$$

If $G=H$ then

$$
\begin{aligned}
& \delta q_{i}=\epsilon \frac{\partial H}{\partial p_{i}}=\epsilon \dot{q}_{i} \\
& \delta p_{i}=-\frac{\epsilon \partial H}{\partial q_{i}}=\epsilon \dot{p}_{i}
\end{aligned}
$$

Thus the transformation advances the canonical variables in time. This type of transformation is called a "contact" transformation.

Consider a function of Canonical variables $u(q, p)$ when a canonical transform is applied to new coordinates $Q$ and $P$ the form of the function may change but the value does not. This follows from $(q, p)$ and $(Q, P)$ defining the same point in phase space using different doordinate systems. that describe the position.

$$
u(q, P)=u(Q, P)
$$

This point of view is considered passibe.

For example a transformation that preserves the Energy or Angular momentum would be consider passive.
In contrast a consideration from the active pornt of view the system is translated from points $\left(q_{A}, p_{A}\right)$ to $\left(q_{B}, p_{B}\right)$ in time which are different points in phase space. In this case the form of $u(q, p)$ does not change in the tranformation but its value does. This type of transformation is called active.
Denote the change in the function by an active topansformation from phase space point $A$ to point $B$ by

$$
\partial u=u(B)-u(A)
$$

since $u(q, p)$

$$
\partial u=\sum_{i=1}^{n}\left\{\frac{\partial u}{\partial q_{i}} \delta q_{i}+\frac{\partial u}{\partial p_{i}} \delta p_{i}\right\}
$$

$$
\begin{aligned}
& =\epsilon \sum_{i=1}^{n}\left\{\frac{\partial u}{\partial q_{i}} \frac{\partial \epsilon}{\partial p_{i}}-\frac{\partial u}{\partial p_{i}} \frac{\partial \epsilon}{\partial q_{i}}\right\} \\
& =\epsilon[u, \epsilon]
\end{aligned}
$$

When considering the change in the Hamiltonian wroter a Canonical tranformation that explicitly depends on time,

$$
K=H+\frac{\partial F}{\partial t}
$$

The value of the Hamittonian will be changed by the partial time derivative of the canonical transformation. For example the value at point A will be changed to

$$
K\left(A^{\prime}\right)=H(A)+\frac{\partial F}{\partial t}
$$

It follows that the change in the Hamiltonian between points A and B due soley to
adve effects is active effects is

$$
\partial H=H(B)-K\left(A^{\prime}\right)
$$

Now an irfinitesimal conical transformation differs from the identily transformation by an infinitesimal amount

$$
F=\sum_{i=1}^{n} q_{i} P_{i}+\epsilon 6
$$

then

$$
\begin{aligned}
K= & H+\frac{\partial}{\partial t}\left\{\sum_{i=1}^{n} q_{i} P_{i}+\epsilon E\right\} \\
& =H+\epsilon \frac{\partial G}{\partial t}
\end{aligned}
$$

Now the change in $H$ under the canonical transformation
is
$\partial H=H(B)-K\left(A^{\prime}\right)=H(B)-H(A)-\epsilon \frac{\partial G}{\partial t}$
but

$$
H(B)-H(A)=\epsilon[H, G]
$$

50

$$
\partial H=\epsilon\left\{[H, G]-\frac{\partial G}{\partial t}\right\}
$$

and the tolal derivative of the canonical transformation is given by

$$
\begin{aligned}
\frac{d G}{d t} & =[G, H]+\frac{\partial G}{\partial t} \\
& =\frac{\partial G}{\partial t}-[H, G]
\end{aligned}
$$

thus

$$
\partial H=\epsilon\left\{[H, \epsilon]-\frac{\partial \epsilon}{\partial t}\right\}=-\epsilon \frac{d \epsilon}{d t}
$$

It follows that if the generating function of the canonical tranformation is conserved

$$
\frac{d \epsilon}{d t}=0
$$

then

$$
\partial H=0
$$

so H is invariat wroter the transformation.

## Conservation of Phase Space Volume

Consider a phase space volume element

$$
d \eta=d q_{1} d q_{2} \cdots d q_{n} d p_{1} d p_{2} \cdots d p_{n}
$$

under a canonical transformation to $P_{i}$ and $Q_{i}$ the volume element becomes

$$
d \rho=d Q_{1} d Q_{2} \cdots d Q_{n} d P_{1} d P_{2} \cdots d P_{n}
$$

In general volume elements transformed between cooridinate systems differ in scale by the Jacobian, IJI

$$
|J|=\frac{\partial\left(Q_{1}, Q_{2}, \ldots, Q_{n}, P_{1}, P_{2}, \ldots P_{n}\right)}{\partial\left(q_{1}, q_{2}, \ldots, q_{n}, P_{1}, P_{2}, \ldots, P_{n}\right)}
$$

$$
=\left|\begin{array}{cccc}
\frac{\partial Q_{1}}{\partial q_{1}} & \frac{\partial Q_{1}}{\partial q_{2}} & \cdots & \frac{\partial Q_{1}}{\partial P_{n}} \\
\frac{\partial Q_{2}}{\partial q_{1}} & \frac{\partial Q_{2}}{\partial q_{2}} & \cdots & \frac{\partial Q_{2}}{\partial P_{n}} \\
\vdots & & & \\
\frac{\partial P_{n}}{\partial q_{1}} & \frac{\partial P_{n}}{\partial q_{2}} & \cdots & \frac{\partial P_{n}}{\partial P_{n}}
\end{array}\right|
$$

$$
d \eta=|J| d \rho
$$

For simplicity consider a one dimensional system. It follows that

$$
\begin{aligned}
& d \eta=d q d P \\
& d e=d Q d P
\end{aligned}
$$

It follows that

$$
\begin{aligned}
|J| & =\left|\begin{array}{ll}
\frac{\partial Q}{\partial q} & \frac{\partial Q}{\partial p} \\
\frac{\partial P}{\partial q} & \frac{\partial P}{\partial P}
\end{array}\right| \\
& =\frac{\partial Q}{\partial q} \frac{\partial P}{\partial P}-\frac{\partial Q}{\partial P} \frac{\partial P}{\partial q} \\
& =[Q, P]
\end{aligned}
$$

If the transformation generating finction is assumed to have the form
then

$$
F(q, P)
$$

$$
P=\frac{\partial F}{\partial G} \quad Q=\frac{\partial F}{\partial P}
$$

The transformations $P$ and $Q$ have the general form

$$
Q=Q(q, p) \quad P=P(q, p)
$$

From the form of the assumed generating function, $F(q, P)$, it follows that the transformation equations can be inverted to yield

$$
\begin{aligned}
& Q=\varphi(q, P) \\
& P=\psi(q, P)
\end{aligned}
$$

The generating function equations

$$
\begin{aligned}
& P=\frac{\partial F}{\partial q} \Rightarrow \frac{\partial \psi}{\partial P}=\frac{\partial^{2} F}{\partial P \partial q} \\
& Q=\frac{\partial F}{\partial P} \Rightarrow \frac{\partial \varphi}{\partial q}=\frac{\partial^{2} F}{\partial q \partial P}
\end{aligned}
$$

It follows that

$$
\begin{equation*}
\frac{\partial \psi}{\partial P}=\frac{\partial \varphi}{\partial q} \tag{1}
\end{equation*}
$$

Now using $p=\psi(q, p)$

$$
P=P(q, P)=P(q, \psi(q, P))
$$

It follows that

$$
\begin{equation*}
l=\frac{\partial P}{\partial P}=\frac{\partial P}{\partial P} \frac{\partial \varphi}{\partial P} \tag{2}
\end{equation*}
$$

Making use of (1) and (2) gives

$$
\begin{equation*}
\frac{\partial P}{\partial P} \frac{\partial \varphi}{\partial \varphi}=1 \tag{3}
\end{equation*}
$$

similarly

$$
Q=\varphi(q, P)=\varphi(q, P(q, p))
$$

So

$$
\begin{equation*}
\frac{\partial Q}{\partial P}=\frac{\partial \varphi}{\partial P} \frac{\partial P}{\partial P} \tag{4}
\end{equation*}
$$

and

$$
\frac{\partial Q}{\partial q}=\frac{\partial \varphi}{\partial q}+\frac{\partial \Phi}{\partial P} \frac{\partial P}{\partial q}
$$

There is now enouch information to evaluate $[Q, P]$,

$$
\begin{aligned}
{[Q, P] } & =\frac{\partial Q}{\partial q} \frac{\partial P}{\partial P}-\frac{\partial Q}{\partial P} \frac{\partial P}{\partial q} \\
& =\left(\frac{\partial q}{\partial q}+\frac{\partial \varphi}{\partial P} \frac{\partial P}{\partial q}\right) \frac{\partial P}{\partial P}-\left(\frac{\partial \varphi}{\partial p} \frac{\partial P}{\partial p}\right) \frac{\partial P}{\partial q} \\
& =\frac{\partial q}{\partial q} \frac{\partial P}{\partial p}+\frac{\partial q}{\partial P} \frac{\partial P}{\partial q} \frac{\partial P}{\partial p}-\frac{\partial Q}{\partial p} \frac{\partial P}{\partial p} \frac{\partial P}{\partial q} \\
& =\frac{\partial q}{\partial q} \frac{\partial P}{\partial P}=1
\end{aligned}
$$

Where use was made of equation (3). It follows that

$$
\begin{aligned}
d q d P & =|J| d Q d P \\
& =[Q, P] d Q d P \\
& =d Q d P
\end{aligned}
$$

Thus conoinal transformation conserve phass space volume.

## Liouville's Theorem

If all possible states in a volume of phase space are considered a uniform density can be defined by

$$
\rho=\frac{N}{V}
$$

Where $N$ is the number of points and $v$ is phase space volume.
In the limit as $N \rightarrow \infty$ and $v \rightarrow 0$ as $e$ remains constant the phase space density is defined.

$$
\rho=\frac{d N}{d v}
$$

Now the flux of phase space desity is defined by the vector

$$
\bar{J}=\rho\left(\dot{q}_{1}, \dot{q}_{2}, \ldots, \dot{q}_{n}, \dot{p}_{1}, \dot{p}_{2}, \ldots, \dot{p}_{n}\right)
$$

The conservation of mass implies that the rate of change of phase space density is lequal to the flux out of a differentral volume. This is called the divergence theorem.

For phase space the divergence theorem is written as

$$
\frac{\partial \rho}{\partial t}+\bar{\nabla} \cdot \bar{J}=0
$$

Now

$$
\begin{aligned}
\nabla \cdot \bar{J} & =\sum_{i=1}^{n}\left\{\frac{\partial}{\partial q_{i}}\left(\rho \dot{q}_{i}\right)+\frac{\partial}{\partial p_{i}}\left(\rho \dot{p}_{i}\right)\right\} \\
& =\sum_{i=1}^{n}\left\{\frac{\partial \rho}{\partial q_{i}} \dot{q}_{i}+\rho \frac{\partial \dot{q}_{i}}{\partial q_{i}}+\frac{\partial \rho}{\partial \dot{p}_{i}} \dot{p}_{i}+\rho \frac{\partial \dot{p}_{i}}{\partial p_{i}}\right\} \\
& =\sum_{i=1}^{n}\left\{\frac{\partial \rho}{\partial q_{i}} \dot{q}_{i}+\frac{\partial \rho}{\partial p_{i}} \dot{p}_{i}\right\}+ \\
& \rho \sum_{i=1}^{n}\left\{\frac{\partial \dot{q}_{i}}{\partial q_{i}}+\frac{\partial \dot{p}_{i}}{\partial p_{i}}\right\}
\end{aligned}
$$

Consider the last term

$$
\begin{aligned}
& \frac{\partial \dot{q}_{i}}{\partial q_{i}}=\frac{\partial}{\partial q_{i}}\left(\frac{\partial H}{\partial p_{i}}\right)=\frac{\partial^{2} H}{\partial q_{i} \partial p_{i}} \\
& \frac{\partial \dot{p}_{i}}{\partial p_{i}}=\frac{\partial}{\partial p_{i}}\left(-\frac{\partial H}{\partial q_{i}}\right)=-\frac{\partial^{2} H}{\partial p_{i} \partial q_{i}}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
& e \sum_{i=1}^{n}\left\{\frac{\partial \dot{q}_{i}}{\partial q_{i}}+\frac{\partial \dot{p}_{i}}{\partial p_{i}}\right\}=e \sum_{i=1}^{n}\left\{\frac{\partial^{2} H}{\partial q_{i} \partial p_{i}}-\frac{\partial^{2} H}{\partial p_{i} \partial q_{i}}\right\} \\
& \quad=0
\end{aligned}
$$

The first term can be simplified as follows
$\sum_{i=1}^{n}\left\{\frac{\partial p}{\partial q_{i}} \dot{q}_{i}+\frac{\partial p}{\partial p_{i}} \dot{p}_{i}\right\}=\sum_{i=1}^{n}\left\{\frac{\partial p}{\partial q_{i}} \frac{\partial H}{\partial p_{i}}-\frac{\partial p}{\partial p_{i}} \frac{\partial H}{\partial q_{i}}\right\}$
$=[e, H]$
Bringing things together

$$
[\rho, t)]+\frac{\partial \rho}{\partial t}=0
$$

But this is the total derivative SC

$$
\frac{d e}{d t}=0
$$

## Hamitton - Jacobi Equation

Hamitton - Jacobi theory provides a method for obtaining solutions to Hamilton's equations by converting the $2 n$ first order equations to a partial differential with $2 n$ variables for "Hamitton's Principle Function" denoted by $s$.

The Hamilton-Jacobi equation is theoretically important because it provides an opticalmechanical analogy between optical rays and phase space paths.
The initial conditions for the canonical coordinates are identified by 90 and po which define the coordinate values at $t=0$. The solution to the problem is the given by

$$
\begin{aligned}
& q=q\left(q_{0}, p_{0}, t\right) \\
& p=p\left(q_{0}, p_{0}, t\right)
\end{aligned}
$$

These equations can be thought of as a set of transformation
equations beteen the canonical variables 9 and $P$ and 90 and Po. The solution is equivalent to finding the transformation from $q, p t_{0} q_{0}, p_{0}$. But $q_{0}, p_{0}$ are constants therefore we need to find a transformation from AG to to constants.

A canonical transformation produces the transformation

$$
\begin{aligned}
& Q_{i}=\frac{\partial K}{\partial P_{i}} \\
& \dot{P}_{i}=-\frac{\partial K}{\partial Q_{i}} \\
& K=H+\frac{\partial F}{\partial t}
\end{aligned}
$$

and
since the new variables are constants

$$
\dot{Q}=0 \text { and } \dot{P}=0
$$

The new variables will be constant if $k=0$ it follows that

$$
\begin{gathered}
\dot{Q}_{i}=\frac{\partial K}{\partial P_{i}}=0, \quad P_{i}=-\frac{\partial K}{\partial Q_{i}}=0 \\
K=0=H+\frac{\partial F}{\partial t}
\end{gathered}
$$

This defines a differential equation for the generating function $F$. Assume that $F$ has the form

$$
F=F_{2}(q, P, t) .
$$

Then

$$
\begin{aligned}
P_{i} & =\frac{\partial F_{2}}{\partial q_{i}} \\
Q_{i} & =\frac{\partial F_{3}}{\partial P_{i}} \\
K & =H+\frac{\partial F_{2}}{\partial t}
\end{aligned}
$$

For historical reasons $F_{2}$ is denoted by $s$ and called Hamilton's principal function

$$
S=S(q, P, t)
$$

it follows that the equations of motion are given by

$$
\begin{aligned}
& \begin{array}{l}
p_{i}=\frac{\partial S}{\partial q_{i}} \\
Q_{i}=\frac{\partial S}{\partial p_{i}} \\
k=H+\frac{\partial S}{\partial t}
\end{array} \\
& \text { Assuming } k=0 \quad \text { gives } \\
& H\left(q_{1}, q_{2}, \ldots, q_{n} ; p_{1}, p_{2}, \ldots, p_{n}, t\right)+\frac{\partial S}{\partial t} \\
& \text { but } \\
& \qquad p_{i}=\frac{\partial S}{\partial q_{i}} \\
& \text { so } \\
& H\left(q_{1}, q_{2}, \ldots, q_{n} ; \frac{\partial S}{\partial q_{i}}, \frac{\partial S}{\partial q_{2}}, \ldots, \frac{\partial S}{\partial q_{n}}, t\right)+\frac{\partial S}{\partial t}=0 \\
& \hline \text { This is the Hamilton - Jacobbi } \\
& \text { equation which is solved for } s . \\
& \text { since the transformed coord(nates } \\
& \text { are constant let } \\
& \text { are } p_{i} \quad \beta_{i}=Q_{i}
\end{aligned}
$$

then

$$
S=S\left(q_{i}, \alpha_{i}, t\right)
$$

and generator equations become

$$
\begin{array}{r}
p_{i}=\frac{\partial S}{\partial q_{i}}=\frac{\partial S}{\partial q_{i}}\left(q_{i}, \alpha_{i}, t\right) \\
\beta_{i}=Q_{i}=\frac{\partial S}{\partial d_{i}}=\frac{\partial S}{\partial \alpha_{i}}\left(q_{i}, \alpha_{i}, t\right)
\end{array}
$$

Jusl because $\alpha_{i}$ is constant in time does not mean that it is not differentrable. Inversion of this equation gives

$$
q_{i}=q_{i}\left(\alpha_{i}, \beta_{i}, t\right)
$$

In summary the Hamilton-Jacbbi and solution is
$H\left(q_{1}, q_{2}, \ldots, q_{n} ; \frac{\partial S}{\partial q_{i}}, \frac{\partial S}{\partial q_{2}}, \ldots, \frac{\partial S}{\partial q_{n}}, t\right)+\frac{\partial S}{\partial t}=\gamma$

$$
\begin{aligned}
& p_{i}=\frac{\partial S}{\partial q_{i}}\left(q_{i}, \alpha_{i}, t\right) \\
& q_{i}=q_{i}\left(\alpha_{i}, \beta_{i}, t\right)
\end{aligned}
$$

## Interpretation of Hamitton's Principal Function

Hamittons Principal Function is the genearating

$$
S=S\left(q_{1}, q_{2}, \ldots q_{n} ; \alpha_{1}, \alpha_{2}, \ldots, \alpha_{n}, t\right)
$$

The total time derivative is given

$$
\frac{d s}{d t}=\sum_{i=1}^{n}\left\{\frac{\partial s}{\partial q_{i}} \frac{d q_{i}}{d t}+\frac{\partial s}{\partial \alpha_{i}} \frac{d \alpha_{i}}{d t}\right\}+\frac{\partial s}{\partial t}
$$

but
and

$$
\begin{aligned}
& \rho_{i}=\frac{\partial S}{\partial q_{i}} \\
& \frac{\partial \alpha_{i}}{d t}=0
\end{aligned}
$$

then

$$
\frac{d S}{d t}=\sum_{i=1}^{n} p_{i} \dot{q}_{i}+\frac{\partial S}{\partial t}
$$

Recall that twe Hamittonian and Lagrangian are related by the legendre transform,

$$
H=\sum_{i=1}^{n} P_{i} \dot{q}_{i}-L
$$

thus

$$
\frac{d S}{d t}=H+L+\frac{\partial S}{\partial t}
$$

Recall that the generating function $s$ produces the transform

$$
K=0, \dot{Q}=0, \dot{P}=0
$$

where

$$
K=H+\frac{\partial F}{\partial t}
$$

so using $s=F$ and $K=0$

$$
O=H+\frac{\partial S}{\partial t}
$$

so

$$
\frac{d s}{d t}=L
$$

and

$$
S=\int L d t+C
$$

where $C$ is an arbritrary constant. Thus Hamilton's Principal function is equal to the action to within a constant.

Note that this is an indefinite in tegral not a definite intlegral For another point of view, once again consider consider the total derivative of Hamiltoris Principal function

$$
\frac{d S}{d t}=\sum_{i=1}^{n} p_{i} \dot{q}_{i}+\frac{\partial S}{\partial t}
$$

and recall that the Hamiltonian is derived as the Legendre transform of the Lagrangian

$$
\begin{aligned}
H & =\sum_{i=1}^{n} p_{i} \dot{q}_{i}-L \\
\Rightarrow L & =\sum_{i=1}^{n} p_{i} q_{i}-H
\end{aligned}
$$

and the Hamitton-Jacobi equation is defined by

$$
H+\frac{\partial S}{\partial t}=0 \Rightarrow H=-\frac{\partial S}{\partial t}
$$

50

$$
\frac{d s}{d t}=\sum_{i=1}^{n} p_{i} q_{i}-H=L
$$

once again

## $S=S L d t+$ constant

Thus $s$ is the indeffinite integral of the Lagrangian not the definite integral used in Hamilton's principal.
If the Hamiltonian is independent of time

$$
H=-\frac{\partial S}{\partial t}
$$

implies that

$$
S(q, \alpha, t)=\omega(q, \alpha)+a t
$$

Where $\omega(q, \alpha)$ is independent of time and called Hamilton's Characteristic function and a is an arbitrary constant. It follows that

$$
H=a
$$

Now the total time derivative of $w$ is given by
$\frac{d \omega}{d t}=\sum_{i=1}^{n}\left\{\frac{\partial \omega}{\partial q_{i}} \frac{d q_{i}}{d t}+\frac{\partial \omega}{\partial \alpha_{i}} \frac{d \alpha_{i}}{d t}\right\}+\frac{\partial \omega}{\partial t}$
but

$$
\dot{q}_{i}=\frac{d q_{i}}{d t}, \quad \frac{d d_{i}}{d t}=0, \quad \frac{\partial \omega}{\partial t}=0
$$

so

$$
\frac{d \omega}{d t}=\sum_{i=1}^{n} \frac{\partial \omega}{\partial q_{i}} \dot{q}_{i}
$$

To go furthur recall that from the definition of $s$

$$
p_{i}=\frac{\partial S}{\partial q_{i}}
$$

so from

$$
\begin{array}{ll} 
& s(q, \alpha, t)=\omega(q, \alpha)+a t \\
\Rightarrow \quad & \frac{\partial S}{\partial q_{i}}=\frac{\partial \omega}{\partial q_{i}}=p_{i} \\
\text { Thus } & \frac{d \omega}{d t}=\sum_{i=1}^{n} p_{i} \dot{q}_{i}
\end{array}
$$

and

$$
\begin{aligned}
w & =S \sum_{i=1}^{n} p_{i} \dot{q}_{i} d t \\
& =\sum_{i=1}^{n} S p_{i} d q_{i}
\end{aligned}
$$

## Shrodingers Equation from Hamilton- Jacobi Jacobi

consider a wave function of the form

$$
\psi=\psi_{0} e^{i s / \hbar}
$$

Where $\hbar=12 \pi$ is a constant use to make the argument dimensionless an $s$ is Hamiton's Principal function which satisfies the equations for a 1 dimensional system

$$
\begin{gathered}
\frac{d S}{d t}=q P+\frac{\partial S}{\partial t} \\
\frac{\partial S}{\partial t}+H=0 \quad P=\frac{\partial S}{\partial q} \\
H=T+V \\
T=\frac{p^{2}}{2 m} \quad V=V(q)
\end{gathered}
$$

where $T$ is the Kinetic Energay $U$ the potential energy

Now

$$
\begin{aligned}
& \frac{\partial S}{\partial t}+H=0=\frac{\partial S}{\partial t}+\frac{D^{2}}{\partial m}+V=0 \\
& =\frac{\partial S}{\partial t}+\frac{1}{\partial m}\left(\frac{\partial S}{\partial q}\right)^{2}+V=0
\end{aligned}
$$

But since

$$
\psi=\psi_{0} e^{i S / K}
$$

Il is seen that

$$
\begin{aligned}
\frac{\partial \psi}{\partial q} & =\psi_{0} e^{i s / \hbar}\left(\frac{i}{\hbar} \frac{\partial s}{\partial q}\right) \\
& =\frac{i \eta}{\hbar} \frac{\partial s}{\partial q} \\
\Rightarrow \frac{\partial s}{\partial q} & =\frac{\hbar}{i} \frac{1}{\psi} \frac{\partial \psi}{\partial q}=-i \hbar \frac{1}{\psi} \frac{\partial \psi}{\partial q}
\end{aligned}
$$

Now since

$$
\frac{\partial S}{\partial t}+H=\frac{\partial S}{\partial t}+\frac{1}{\partial m}\left(\frac{\partial S}{\partial q}\right)^{2}+V
$$

$$
\begin{aligned}
& H=\frac{1}{\partial m}\left(\frac{\partial S}{\partial q}\right)^{2}+V \\
\Rightarrow & \frac{1}{\partial m}\left(\frac{\partial S}{\partial q}\right)^{2}+V-H=0
\end{aligned}
$$

but

$$
\begin{aligned}
\left(\frac{\partial s}{\partial q}\right)^{2} & =\left(-i \hbar \frac{1}{\psi} \frac{\partial \psi}{\partial \xi}\right)\left(-i \hbar \frac{1}{\psi} \frac{\partial \psi}{\partial \xi}\right)^{*} \\
& =\hbar^{2} \frac{1}{\psi \psi^{*}} \frac{\partial \psi}{\partial q} \frac{\partial \psi^{*}}{\partial \xi}
\end{aligned}
$$

50

$$
\frac{\hbar^{2}}{\partial m}\left(\frac{1}{\psi \psi^{*}}\right)\left(\frac{\partial \psi}{\partial q} \frac{\partial \psi^{*}}{\partial q}\right)+v-H=0
$$

$\Rightarrow \frac{\hbar^{2}}{\partial m}\left(\frac{\partial y}{\partial q} \frac{\partial y^{*}}{\partial q}\right)+(V-H) y y^{*}=0$
Let

$$
M=\frac{\hbar^{2}}{2 m}\left(\frac{\partial y}{\partial q} \frac{\partial y^{*}}{\partial q}\right)+(V-H) y y^{*}
$$

Now
$M$ is a function of

$$
\psi, \psi^{*}, \frac{\partial \psi}{\partial q}, \frac{\partial \psi^{*}}{\partial q}
$$

Shrödinger treated $M$ as a Lagrangian so that

$$
\int_{q_{1}}^{q_{2}} \mu d q
$$

is minimized. The Lagrange equation for $M$ for the $7^{*}$ coordinat is given by

$$
\frac{\partial M}{\partial \psi^{*}}-\frac{d}{d q}\left(\frac{\partial M}{\partial\left(\partial \psi^{*} / \partial q\right)}\right)=0
$$

Now

$$
\begin{aligned}
& \frac{\partial M}{\partial \psi^{*}}=(V-H) \psi \\
& \frac{\partial M}{\partial\left(\partial \psi^{*} \partial q\right)}=\frac{\hbar^{2}}{\partial m} \frac{\partial \psi}{\partial q} \\
& \frac{d}{d q}\left(\frac{\partial M}{\partial\left(\partial \psi^{*} \partial q\right)}\right)=\frac{\hbar^{2}}{\partial m} \frac{\partial^{2} u}{\partial q^{2}}
\end{aligned}
$$

Thus

$$
\begin{aligned}
& (V-H) \psi-\frac{\hbar^{2}}{\partial m} \frac{\partial^{2} \psi}{\partial q^{2}}=0 \\
\Rightarrow & -\frac{\hbar^{2}}{\partial m} \frac{\partial^{2} \psi}{\partial q^{2}}+V \psi=H \psi
\end{aligned}
$$

Which is the time indepent Shrödinger equation which assumes

$$
y=y(9)
$$

