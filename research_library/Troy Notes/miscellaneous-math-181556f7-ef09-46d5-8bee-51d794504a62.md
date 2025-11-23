Micellaneaus Math

Troy Stribling
Feb. 25207
$\qquad$
$\qquad$
$\qquad$
$\qquad$

## Derivative of logarithm

Consider

$$
y(x)=a^{x}=\left(e^{\ln a}\right)^{x}=e^{x \ln a}
$$

so

$$
\begin{aligned}
\frac{d y}{d x} & =\frac{d}{d x}\left(a^{x}\right)=\frac{d}{d x}\left(e^{x \ln a}\right) \\
& =(\ln a) e^{x \ln a}=(\ln a)\left(e^{\ln a}\right) x \\
& =(\ln a) a^{x}
\end{aligned}
$$

## Probability Sum Rule

## Consider the events $A$ and $B$

![](https://cdn.mathpix.com/cropped/2025_09_20_b34515b8e69d257d8d0eg-03.jpg?height=378&width=640&top_left_y=298&top_left_x=306)
$A \cup B=$ union of $A$ and $B$ and defines the event where either $A$ or $B$ occur.
$A \cap B=$ Intersection of $A$ and $B$, indicated by red in the Uenn Diagram, defines the event where $A$ and $B$ occur.

Let

$$
\begin{aligned}
& P(A)=\text { Probability that cuent } A \\
& \text { occurs } \\
& P(B)=\begin{array}{c}
\text { Probability that event } B \\
\text { occurs }
\end{array}
\end{aligned}
$$

$P(A \cup B)=$ Probability the event $A$ or Bloccurs.
Indiceled be green in the venn Diagram

## $P(A \cap B)=$ Probability trat botn $A$ and $B$ occur. Indicated by red in the venn Diagram.

From inspection of the venn Diagram it can be seen that

$$
P(A \cup B)=P(A)+P(B)-P(A \cap B)
$$

Next consider

$$
P(x \cup y \cup z)
$$

let

$$
A=X \quad \text { and } \quad B=Y \cup Z
$$

The sum rule gives

$$
P(x \cup y \cup z)=P(x)+P(y \cup z) \cdot P[x \cap(y \cup z)]
$$

$$
=P(x)+P(y \cup z)-P[(x \cap y) \cup(x \cap z)]
$$

Apply the sum rule again
$P(x \cup y \cup z)=P(x)+P(y)+P(z)$
$-P(Y \cap Z)-\{P(X \cap Y)+P(X \cap Z)$
$-P[(x \cap y) \cap(x \cap z)] \xi$
$=P(x)+P(y)+P(z) \cdot P(y \cap z)$
$-P(x \cap y)-P(x \cap z)+P(x \cap y \cap z)$
visually
![](https://cdn.mathpix.com/cropped/2025_09_20_b34515b8e69d257d8d0eg-05.jpg?height=674&width=947&top_left_y=822&top_left_x=255)

$$
\begin{aligned}
& P(x \cup y \cup z)=P(x)+P(y)+P(z) \\
& -P(y \cap z)-P(y \cap x)-P(x \cap z) \\
& +P(y \cap x \cap z)
\end{aligned}
$$

To see the pattern one more union is required

$$
\begin{aligned}
& P(S \cup x \cup y \cup z)=P(S)+P(x \cup y \cup z) \\
& -P[S \cap(x \cup y \cup z)]
\end{aligned}
$$

Now

$$
\begin{aligned}
& P[S \cap(x \cup y \cup z)] \\
& =P[(S \cap x) \cup(S \cap y) \cup(S \cap z)]
\end{aligned}
$$

using the triple union sum rule

$$
\begin{aligned}
P & {[(S \cap x) \cup(S \cap y) \cup(S \cap z)] } \\
= & P(S \cap x)+P(S \cap y)+P(S \cap z) \\
- & P(S \cap x \cap y)-P(S \cap x \cap z) \\
- & P(S \cap y \cap z)+P(S \cap x \cap y \cap z)
\end{aligned}
$$

and

$$
\begin{aligned}
& P(x \cup y \cup z)=P(x)+P(y)+P(z) \\
& -P(x \cap y)-P(x \cap z)-P(y \cap z) \\
& +P(x \cap y \cap z)
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
& P(s \cup x \cup y \cup z)=P(s)+[P(x)+P(y)+P(z) \\
& -P(x \cap y)-P(x \cap z)-P(y \cap z) \\
& +P(x \cap y \cap z)]-[P(s \cap x)+P(s \cap y) \\
& +P(s \cap z)-P(s \cap x \cap y)-P(s \cap x \cap z) \\
& -P(s \cap y \cap z)+P(s \cap x \cap y \cap z)] \\
& =[P(s)+P(x)+P(y)+P(z)]-[P(x \cap y) \\
& +P(x \cap z)+P(y \cap z)+P(s \cap x)+P(s \cap y) \\
& +P(s \cap z)]+[P(x \cap y \cap z)+P(s \cap x \cap y) \\
& +P(s \cap x \cap z)+P(s \cap y \cap z)] \\
& -P(s \cap x \cap y \cap z)
\end{aligned}
$$

Now for unions of $n$ sets

$$
P\left(\bigcup_{i=1}^{n} X_{i}\right)
$$

we have

$$
\begin{aligned}
& P\left(\bigcup_{i=1}^{n} x_{i}\right)=\sum_{i=1}^{n} P\left(x_{i}\right)-\sum_{i=1}^{n-1} \sum_{j=i+1}^{n} P\left(x_{i} \cap x_{j}\right) \\
& +\sum_{i=1}^{n-2} \sum_{j=i+1}^{n-1} \sum_{k=j+1}^{n} P\left(x_{i} \cap x_{j} \cap x_{k}\right) \\
& +\sum_{i=1}^{n-3} \sum_{j=i+1}^{n-2} \sum_{k=j+1}^{n-1} \sum_{l=k+1}^{n} P\left(x_{i} \cap x_{j} \cap x_{k} \cap x_{l}\right) \\
& +\cdots+(-1)^{n+1} P\left(x_{1} \cap x_{2} \cap \cdots \cap x_{n}\right)
\end{aligned}
$$

## Probability of Compliment

Consider the set $A$ where $A C(\Omega, F, P)$
for the probability space

Now let $A^{c}$ denote the complement of $A$ then

$$
\begin{aligned}
& A \cap A^{C}=\varnothing \\
& A \cup A^{C}=\Omega
\end{aligned}
$$

and

$$
P(\Omega)=1 \quad P(\phi)=0
$$

so using the sum rule

$$
\begin{aligned}
& P\left(A \cup A^{c}\right)=P(A)+P\left(A^{c}\right)+P\left(A \cap A^{c}\right) \\
& \Rightarrow P(\Omega)=P(A)+P\left(A^{c}\right)+P(\phi) \\
& \Rightarrow \quad 1=P(A)+P\left(A^{c}\right) \\
& \Rightarrow P\left(A^{c}\right)=1-P(A)
\end{aligned}
$$

Probability of Set Difference Consider two sets $A$ and $B$
![](https://cdn.mathpix.com/cropped/2025_09_20_b34515b8e69d257d8d0eg-10.jpg?height=481&width=895&top_left_y=332&top_left_x=280)

## The difference of $A$ and <br> $A \backslash B$

where

$$
a \in A \backslash B \Rightarrow a \in A \text { and } a \notin B
$$

This is denoted by the green part of $A$ in the diagram

By inspection of the Uenn diagram it is seen that

$$
P(A \backslash B)=P(A)-P(A \cap B)
$$

* Show that

$$
A \backslash B=A \cap B^{C}
$$

Let $a \in A \backslash B \Rightarrow a \in A, a \notin B$ but $a \notin B \Rightarrow a \in B^{c}$ so, $a \in A \cap B^{c}$ and $A B \subseteq A \cap B$.
Let $a \in A \cap B^{c} \Rightarrow a \in A, a \in B^{c}$ so $a \in B$ and $a \in A \backslash B$ thus

$$
A \backslash B=A \cap B^{C}
$$

* Consider the set

$$
B_{i}=A_{i} \backslash A_{1} \cup A_{1} \cup \cdots \cup A_{i-1}
$$

Show that
i) $B_{i} \cap B_{j}=\Phi \quad i \neq j$
and

$$
\text { (i) } \bigcup_{i=1}^{n} A_{i}=\bigcup_{i=1}^{n} B_{i}
$$

Now

$$
B_{i}=A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}
$$

if

$$
b_{i} \in B_{i}
$$

implies

$$
b_{i} \in A_{i}
$$

but
$b_{i} \notin A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}$
$\delta 0$
$b_{i} \notin A_{k} \forall k=1,2, \ldots, i-1$
i) Consider
$B_{i} \cap B_{j}$
clearly if $i=j \quad B_{i} \cap B_{i}=B_{i}$
Without loss of generality

$$
i>j \text { and } b_{j} \in B_{j}
$$

but

$$
b_{j} \in B_{i} \Rightarrow b_{j}^{\prime} \in A_{j}
$$

and

$$
b_{j} \notin A_{k} \quad \forall \quad k=1,2, \ldots j-1
$$

since $i>j$.

$$
b_{j} \in A_{1} \cup A_{2} \cup \cdots \cup A_{j} \cup \cdots \cup A_{i-1}
$$

So

$$
\begin{aligned}
& b_{j} \notin A_{i} \backslash A_{1}, A_{2}, \ldots, A_{i-1} \\
& \Rightarrow b_{j} \in B_{i}
\end{aligned}
$$

thus

$$
B_{i} \cap B_{j}=\varnothing \quad \forall \quad i \neq j
$$

ii) Snow

$$
\bigcup_{i=1}^{n} B_{i}=\bigcup_{i=1}^{n} A_{i}
$$

If

$$
b \in \bigcup_{i=1}^{n} B_{i}
$$

Since $B_{k} \cap B_{j}=\varnothing \quad \forall i \neq j$
There is one $B_{i}$, call it $B_{K}$ such that

$$
b \in B_{k}
$$

since

$$
B_{k}=A_{k} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{k-1}
$$

it follows that

$$
b_{k} \in A_{k}
$$

thus

$$
b_{k} \in \bigcup_{i=1}^{n} A_{i}
$$

so

$$
\bigcup_{i=1}^{n} B_{i} \subseteq \bigcup_{i=1}^{n} A_{i}
$$

Likewise if

$$
a \in \bigcup_{i=1}^{n} A_{i}
$$

There is at least one $A_{i}$ that contains a. Let $A_{k}$ be the first such $A_{i}$.
If $a$ is contained in all or the first $A_{i}$

$$
A_{1}=B_{1}
$$

50

$$
a \in B_{1}
$$

and

$$
a \in \bigcup_{i=1}^{n} B_{i}
$$

If $a \notin A$, but occurs first in some other $A_{k}$

$$
\begin{aligned}
& a \in A_{k} \\
& a \notin A_{1} \cup A_{2} \cup \cdots \cup A_{k-1}
\end{aligned}
$$

80

$$
a \in B_{k}=A_{k} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{k-1}
$$

and

$$
a \in \bigcup_{i=1}^{n} B_{i}
$$

it follows that

$$
\bigcup_{i=1}^{n} A_{i} \subseteq \bigcup_{i=1}^{n} B_{i}
$$

but

$$
\bigcup_{i=1}^{n} B_{i} \subseteq \bigcup_{i=1}^{n} A_{i}
$$

it follows that

$$
\bigcup_{i=1}^{n} B_{1}=\bigcup_{i=1}^{n} A_{i}
$$

## Moment Cenerating Function

The moment generating function for a random variabe $I$ is defined by,

$$
M(t)=E\left(e^{t \bar{X}}\right)
$$

Moments of $X$ can be found by taking derivatives of M(t) and letting $t=0$,

$$
\begin{aligned}
\frac{d^{n}}{d t^{n}} M(t) & =\frac{d^{n}}{d t^{n}} E\left(e^{t \bar{x}}\right) \\
& =E\left(\bar{x}^{n} e^{t \bar{x}}\right)
\end{aligned}
$$

and

$$
\left.\frac{d^{n}}{d t^{n}} M(t)\right|_{t=0}=E\left(X^{n}\right)
$$

## Central Limit Theorem

The Central Limit Theorem states that the sum of random variables

$$
S_{n}=\frac{\bar{X}_{1}+\bar{X}_{2}+\cdots+\bar{X}_{n}}{n}
$$

approaches a unit normal distribution with random variable)

$$
\frac{1}{\sigma \sqrt{n}}\left(\sum_{i=1}^{n} \bar{x}_{i}-n \mu\right)
$$

as $n \rightarrow \infty$ where $\mu$ is the mean and $\sigma$ the standard deviation of

$$
\bar{X}=\sum_{i=1}^{n} \bar{X}_{i}
$$

## Convergence in the mean

Convergence in the mean is defined by

$$
\lim _{n \rightarrow \infty} E\left[\left(X_{n}-c\right)^{2}\right]=0
$$

where $c$ is a constant Now

$$
\operatorname{Var}\left(x_{n}\right)=E\left(x_{n}^{2}\right)-\left[E\left(x_{n}\right)\right]^{2}
$$

So

$$
\begin{aligned}
& E\left[\left(x_{n}-c\right)^{2}\right]=E\left[x_{n}^{2}-2 c x_{n}+c^{2}\right] \\
& =E\left(x_{n}^{2}\right)-2 c E\left(x_{n}\right)+c^{2} \\
& =\operatorname{Var}\left(x_{n}\right)+\left[E\left(x_{n}\right)\right]^{2}-2 c E\left(x_{n}\right)+c^{2}
\end{aligned}
$$

If

$$
E\left(x_{n}\right)=C
$$

then

$$
\begin{aligned}
E\left[\left(x_{n}-c\right)^{2}\right] & =\operatorname{Var}\left(x_{n}\right)+c^{2} \\
-2 c^{2}+c^{2} & =\operatorname{Var}\left(x_{n}\right)
\end{aligned}
$$

thus if
$\operatorname{Var}\left(x_{n}\right)=0$
In summary

$$
\lim _{n \rightarrow \infty} E\left[\left(x_{n}-c\right)^{2}\right]=0
$$

if

$$
E\left(x_{n}\right)=c
$$

and

$$
\operatorname{Var}\left(x_{n}\right)=0
$$

## Laplace's Methad

Laplace's Method is a method for approximating integrals of the form

$$
\int_{a}^{b} e^{M f(x)} d x
$$

when $M \gg 1$ where it is
assumed that $f(x)$ is at least twice differentiable and has a global maximum at $x_{0}$.
since $f(x)$ has a global maximum at $x_{0}$

$$
f^{\prime}\left(x_{0}\right)=0
$$

and

$$
f^{\prime \prime}\left(x_{0}\right)<0
$$

If $f(x)$ is expanded in a Taylor series about $x_{0}$ gives

$$
\begin{aligned}
f(x) \approx & f\left(x_{0}\right)+f^{\prime}\left(x_{0}\right)\left(x-x_{0}\right) \\
& +\frac{1}{2} f^{\prime \prime}\left(x_{0}\right)\left(x-x_{0}\right)^{2}+0\left(\left(x-x_{0}\right)^{3}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =f\left(x_{0}\right)+\frac{1}{2} f^{\prime \prime}\left(x_{0}\right)\left(x-x_{0}\right)^{2} \\
& =f\left(x_{0}\right)-\frac{1}{2}\left|f^{\prime \prime}\left(x_{0}\right)\right|\left(x-x_{0}\right)^{2}
\end{aligned}
$$

since it is assumed that

$$
f^{\prime \prime}\left(x_{0}\right)<0
$$

It follows that for $x$ near $x_{0}$

$$
\begin{aligned}
& \int_{a}^{b} e^{M f(x)} d x \approx \int_{a}^{b} e^{\left.M\left[\left.f\left(x_{0}\right)-\frac{1}{2} \right\rvert\, f^{\prime \prime}\left(x_{0}\right)\right)\left(x_{0}-x\right)^{2}\right]} d x \\
& =e^{M f\left(x_{0}\right)} \int_{a}^{b} e^{-\frac{1}{2} M\left|f^{\prime \prime}\left(x_{0}\right)\right|\left(x_{0}-x\right)^{2}} d x
\end{aligned}
$$

If $M \gg 1$ contributions to the integral will fall off quickly as $x$ departs from values near $x_{0}$ resulting in a sharp peak.
It follows that for $M \gg 1$
$e^{\mu f(x)} \approx e^{\mu f\left(x_{0}\right)} e^{-\frac{1}{\partial} \mu\left(f^{\prime \prime}\left(x_{0}\right)\left(x_{0}-x\right)^{2}\right.}$

Thus $e^{\mu f(x)}$ appraches a gaussion with scale paramefer

$$
\sigma^{2}=\frac{1}{M\left(f^{\prime \prime}\left(x_{0}\right)\right)}
$$

Laplace's Method states that for MSS I

$$
\int_{a}^{b} e^{\mu f(x)} d x \approx \sqrt{\frac{2 \pi}{\mu\left|f^{\prime \prime}\left(x_{0}\right)\right|}} e^{\mu f\left(x_{0}\right)}
$$

This result can be obtained from the previous result by utilizing the knowledge that for $M \gg 1 e^{M f(x)}$ becomes shardly peaked at $x=x_{0}$. It follows that contributions to the integral will be dominated by $x$ near $x_{0}$ so the integration limits can be taken to $\pm \infty$ thus

$$
\begin{aligned}
& \int_{a}^{b} e^{\mu f(x)} d x \approx \int_{-\infty}^{\infty} e^{\mu f(x)} d x \\
\approx & e^{\mu f\left(x_{0}\right)} \int_{-\infty}^{\infty} e^{-\frac{1}{2} \mu\left|f^{\prime \prime}\left(x_{0}\right)\right|\left(x_{0}-x\right)^{2}} d x \\
= & e^{\mu f\left(x_{0}\right)} \sqrt{\frac{2 \pi}{\mu\left|f^{\prime \prime}\left(x_{0}\right)\right|}}
\end{aligned}
$$

## Examples

Consider the $\sin c(x)$ function

$$
\sin c(x)=\frac{\sin (x)}{x}
$$

Laplace's Method will be used to approximate

$$
e^{M \sin c(x)}
$$

for $\quad \mu \gg 1$.
$x=0$ is a global maximum of $\sin c(x)$

Now at $x=0 \sin c(x)$ is undefined the limit can be evaluate using L'tlopitals rule

$$
\lim _{x \rightarrow 0} \sin (x)=\lim _{x \rightarrow 0} \cos (x)=1
$$

To show that $x=0$ is a global maximum it must be shown that

$$
\lim _{x \rightarrow 0} \sin c^{\prime}(x)=0
$$

and that

$$
\lim _{x \rightarrow 0} \sin c^{\prime \prime}(x)<0
$$

also

$$
\lim _{x \rightarrow 0} \sin c^{\prime \prime}(x)
$$

is needed to evaluate the scale parameter in the approximation obtained using Laplace's Method. To evaluate the limits consider
the Taylor series for $\sin (x)$ expanded about $x=0$ is gruen by

$$
\sin (x)=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2 k+1)!} x^{2 k+1}
$$

It follows that

$$
\begin{aligned}
& \sin c(x)=\frac{\sin (x)}{x}=\sum_{k=0}^{\infty} \frac{(-1)^{k}}{(2 k+1)!} x^{2 k} \\
& =1-\frac{1}{3!} x^{2}+\frac{1}{5!} x^{4}-\frac{1}{9!} x^{6}+\cdots
\end{aligned}
$$

Now the derivatives are given by

$$
\begin{aligned}
& \sin c^{\prime}(x)=-\frac{2}{3!} x+\frac{4}{5!} x^{3}-\frac{6}{9!} x^{5} \\
& \sin c^{\prime \prime}(x)=-\frac{2}{3!}+\frac{(4)(3)}{5!} x^{2}-\frac{(6)(5)}{9!} x^{4}
\end{aligned}
$$

so

$$
\lim _{x \rightarrow 0} \sin ^{\prime}(x)=0
$$

and

$$
\lim _{x \rightarrow 0} \operatorname{sinc}^{\prime \prime}(x)=-\frac{2}{3!}=-\frac{2}{6}=-\frac{1}{3}
$$

Thus $x=0$ is an extremum since

$$
\lim _{x \rightarrow 0} \operatorname{sinc}^{\prime}(x)=0
$$

and a maximum since

$$
\lim _{x \rightarrow 0} \sin c^{\prime \prime}(x)=-\frac{1}{3}<0
$$

It follows that the laplace method approximation to

$$
e^{M \sin c(x)}
$$

for $M \gg 1$

$$
e^{\mu \sin c(x)} \approx e^{\mu} e^{-\frac{\mu}{6} x^{2}}
$$

$$
\lim _{n \rightarrow \infty}\left(\frac{A}{n}\right)^{\frac{n}{B}}
$$

Consider the function

$$
f(n)=\left(\frac{A}{n}\right)^{\frac{n}{B}}
$$

where $A$ and $B$ are constant. Now consider

$$
f(n)=e^{\ln f(n)}
$$

so first consider

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \ln f(n)=\lim _{n \rightarrow \infty} \ln \left[\left(\frac{A}{n}\right)^{\frac{n}{B}}\right] \\
= & \lim _{n \rightarrow \infty} \frac{n}{B} \ln \left(\frac{A}{n}\right) \\
= & \lim _{n \rightarrow \infty} \frac{n}{B}(\ln A-\ln n) \\
= & -\infty
\end{aligned}
$$

Thus

$$
\lim _{n \rightarrow \infty} f(n)=\lim _{n \rightarrow \infty} e^{\ln f(n)}=0
$$

So

$$
\lim _{n \rightarrow \infty}\left(\frac{A}{n}\right)^{n}=0
$$

