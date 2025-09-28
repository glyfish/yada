Stochastuc Calculus
for Finance

Troy Stribling
July 18, 2021

## Discrete-time Processes

Here discrete-time random processes are discussed. The processes are assumed to have an minite number of stops. The steps are all assumed to have the same length of $h>0$ so that,

$$
t=n h, \quad n=0,1,2,3, \ldots
$$

A probability space $(\Omega, \Im, P)$ is available. I has to be infinite to accomodate an infinite number of steps. F is a sigma-field and $P$ a probability measure.

A discrete-time stochastrc process is a sequence of random variables which are 7 measurable functions mapping $\Omega$ to $R$,

$$
\bar{X}(n): \Omega \rightarrow \mathbb{R} \quad n \geqslant 0
$$

it is assumed the $X(0)$ is a known constant. A process is denoted by

$$
\overline{\underline{x}}=(\overline{\underline{x}}(n))_{n \geqslant 0}
$$

## Example

Consider a binomial model determined by two single dep returns

$$
D<u
$$

The sequence of returns is the function,

$$
K(n):[0,1] \rightarrow \mathbb{R}
$$

$n=1,2, \ldots$. Show that

$$
\begin{gathered}
K(n, \omega)=U \underline{1}_{A_{n}}(\omega)+D_{[0,1] / A}(\omega) \\
A_{n}=\left[0, \frac{1}{2^{n}}\right) \cup\left[\frac{2}{2^{n}}, \frac{3}{2^{n}}\right) \cup \cdots\left[\frac{2^{n} \partial}{2^{n}}, \frac{2^{n}-1}{2^{n}}\right] \\
P(K(n)=u)=P(K(n)=0)=1 / 2
\end{gathered}
$$

## where

$$
[0,1] / A_{n}=A_{n}^{c}
$$

where $A_{n}^{c}$ is the compliment of $A_{n}$.

The asset price is given by the recombinent binomial tree expression

$$
S(n)=S(n-1)(1+K(n))
$$

## Solution

Use a binary decimal expansion to perform the mapping,

$$
\Omega \rightarrow \mathbb{R}
$$

A binany decimal expansion has the form

$$
0 . a_{1} a_{2} a_{3} \cdots
$$

where $a_{i}=\{0,1\}$
![](https://cdn.mathpix.com/cropped/2025_09_20_9148d6cedcaef87d8b1bg-005.jpg?height=416&width=1105&top_left_y=155&top_left_x=177)

Assume that $P=1 / 2$ so that in the binary decimal expansion assume that.

$$
u=0 \quad D=1
$$

Then for the first step The $u$ outcome will map to all binany decimal numbers of the form

$$
0.0 a_{2} a_{3} a_{4} \ldots
$$

and the D outcomes to

$$
0.1 a_{2} a_{3} a_{4} \cdots
$$

Now all numbers that map to
the $n=1$ u outcome will lie between the smallest and largest numbers of form $0.0 a_{2} a_{3} a_{4} \ldots$ The smallest is

$$
0=0.0000 \ldots
$$

the largest is

$$
\begin{aligned}
\frac{1}{2} & =0.011111 \ldots \\
& =0.100000 \ldots
\end{aligned}
$$

Similarly for the $n=1$ D outcomes the smallest number is

$$
\frac{1}{2}=0.100000
$$

and largest is

$$
1=0.111111 \cdots
$$

Notice that $1 / 2$ is in both outcomes. For this mapping to be brjective it can only be in one. It will be assumed
that those terminating in o's are in the set at three terminations in i's are not. It don be shown that the set discarded is countable and has zero measure.

So after one step

$$
K(1, \omega)= \begin{cases}u & \omega \in[0,1 / 2) \\ 0 & \omega \in[1 / 2,1)\end{cases}
$$

Graphically
![](https://cdn.mathpix.com/cropped/2025_09_20_9148d6cedcaef87d8b1bg-007.jpg?height=162&width=1067&top_left_y=1122&top_left_x=292)

Also,

$$
\begin{aligned}
& P(u)=1 / 2-0=1 / 2 \\
& P(D)=1-1 / 2=1 / 2
\end{aligned}
$$

and

$$
A_{1}=[0,1 / 2) \quad A_{1}^{C}=[1 / 2,1)
$$

50

$$
K(1, \omega)=U \underline{x}_{A_{1}}(\omega)+D \underline{1}_{A_{1}^{c}}(\omega)
$$

At $n=2$ there are $2^{2}=4$ possible outcomes
un: $0.00 a_{3} a_{4} a_{5} \cdots$
LD: $0.01 a_{3} a_{4} a_{5} \ldots$
DU: 0.10 $a_{3} a_{4} a_{5} \ldots$
$D D: 0.11 a_{3} a_{4} a_{5}$

Following the provious proceedure The whe interval is given by

$$
\begin{aligned}
\min : & 0.0000 \cdots \\
\max : & 0.00111111 \cdots \\
& 0.010000 \cdots \\
& 1 / 4
\end{aligned}
$$

## uD

$\min : 0_{1 / 4}^{0.01000}$
$\max : G .01111 \cdots$.
1/2
DU
min : $0.1000 \ldots$
1/2
$\max : 0.1011111 \cdots$
$0.110000 \ldots$
3/4
$\Delta D$

$$
\begin{aligned}
\min : & 0.110000 \cdots \\
& 3 / 4 \\
\max : & 0.1111 L
\end{aligned}
$$

Thus

$$
\begin{aligned}
& u(\omega)=\omega \in[0,1 / 4) \quad u D(\omega)=\omega \in[1 / 4,1 / 2) \\
& D u(\omega)=\omega \in[1 / 2,3 / 4) \quad D D(\omega)=\omega \in[3 / 4,1)
\end{aligned}
$$

and

$$
\begin{aligned}
& P(U U)=1 / 4-0=1 / 4 \\
& P(L D)=12-k /=1 / 4 \\
& P(D U)=3 / 4-1 / 2=14 \\
& P(D D)=1-3 / 4=1 / 4
\end{aligned}
$$

Graphically
![](https://cdn.mathpix.com/cropped/2025_09_20_9148d6cedcaef87d8b1bg-010.jpg?height=175&width=944&top_left_y=765&top_left_x=326)
finall.

$$
\begin{aligned}
A_{2} & =[0,1 / 4) \cup[1 / 2,3 / 4) \\
A_{2}^{c} & =(1 / 4,1 / 2) \cup[3 / 4,1) \\
K(2, \omega) & =u \mathbb{1}_{A_{2}}(\omega)+D \mathbb{1}_{A_{2}^{c}}(\omega)
\end{aligned}
$$

One more to see pattern.
An $n=3$ there are $a^{3}=8$ possible outcomes

$$
\begin{aligned}
& \text { unu }=0.000 a_{4} a_{5} a_{6} \cdots \\
& \text { und }=0.001 a_{4} a_{5} a_{6} \cdots \\
& \text { udu }=0.010 a_{4} a_{5} a_{6} \cdots \\
& \text { duu }=0.011 a_{4} a_{5} a_{6} \cdots \\
& d u d=0.100 a_{4} a_{5} a_{6} \cdots \\
& d d u=0.101 a_{4} a_{5} a_{6} \cdots \\
& d d d=0.111 a_{4} a_{5} a_{6} \cdots
\end{aligned}
$$

The intervals defoned $b_{1}$ these events is given by
whe

$$
\begin{aligned}
0.000000 \cdots & 0 \\
0.0001111 \cdots & =0.001000 \\
& =118
\end{aligned}
$$

und

$$
\begin{aligned}
0.001000 \cdots & =1 / 8 \\
0.0011111 \cdots & =0.01000 \cdots \\
& =1 / 4 \\
& =218
\end{aligned}
$$

udu

$$
\begin{aligned}
0.010000 \cdots \cdot & =1 / 4=2 / 8 \\
0.010111 \cdots \cdot= & 0.011000 \cdots \\
& =3 / 8
\end{aligned}
$$

## udd

$$
\begin{aligned}
0.011000 \cdots \cdot & =3 / 8 \\
0.011111 \cdots \cdot & =0.1000 \cdots \\
& =1 / 2 \\
& =4 / 8
\end{aligned}
$$

due

$$
\begin{aligned}
0.10000 \cdots & =1 / 2=418 \\
0.1001111 \cdots & =0.101000 \cdots \\
& =5 / 8
\end{aligned}
$$

dud

$$
\begin{aligned}
0.1010000 \cdots & =518 \\
0.1011111 \cdots & =0.110000 \cdots \\
& =3 / 4 \\
& =\frac{6}{8}
\end{aligned}
$$

ddu

$$
\begin{aligned}
0.1100000 \cdots & =6 / 8 \\
0.11011111 \cdots & =0.1110000 \cdots \\
& =7 / 8
\end{aligned}
$$

## ddd

$$
\begin{aligned}
& 0.1110000 \cdots=718 \\
& 0.1111111 \cdots=1
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
& u n(\omega)=\omega \in[0,1 / 8) \\
& u d(\omega)=\omega \in[1 / 8,2 / 8) \\
& u d u(\omega)=\omega \in[2 / 8,3 / 8] \\
& u d d(\omega)=\omega \in[3 / 8,4 / 8) \\
& d u u(\omega)=\omega \in[4 / 8,5 / 8) \\
& d u d(\omega)=\omega \in[5 / 8,6 / 8) \\
& d d u(\omega)=\omega \in[6 / 8,7 / 8) \\
& d d d(\omega)=\omega \in[7 / 8,1)
\end{aligned}
$$

$$
\text { so } \begin{aligned}
P(\text { mun }) & =1 / 8-0=1 / 8 \\
P(\text { und }) & =2 / 8-1 / 8=1 / 8 \\
P(\text { udu }) & =3 / 8-218=1 / 8 \\
P(\text { udd }) & =4 / 8-3 / 8=1 / 8 \\
P(\text { dule }) & =5 / 8-418=1 / 8 \\
P(\text { dud }) & =6 / 8-5 / 8=1 / 8 \\
P(\text { ddu }) & =7 / 8-6 / 8=1 / 8 \\
P(\text { ddd }) & =1-7 / 8=1 / 8
\end{aligned}
$$

## Graphically

![](https://cdn.mathpix.com/cropped/2025_09_20_9148d6cedcaef87d8b1bg-014.jpg?height=170&width=971&top_left_y=1257&top_left_x=380)

Finally

$$
\begin{gathered}
A_{n}=[0,1 / 8) \cup[2 / 8,3(8) \cup[4 / 8,5 / 8) \\
\cup[6 / 8,7 / 8) \\
A_{n}^{C}=[1 / 8,2 / 8) \cup[3 / 8,4 / 8) \cup[5 / 8,6 / 8) \\
\cup[7 / 8,1)
\end{gathered}
$$

$K(3, \omega)=u \mathbb{1}_{A_{3}}(\omega)+D \mathbb{1}_{A_{3}^{c}}^{c}(\omega)$
There is enough information to generalize.
The total number of intervals is $2^{n}$ and the width of each interval is $2^{-n}$. The number of intervals in $A_{n}$ and $A^{C_{n}}$ are equal and given by $2^{n-1}$.
From inspection of the graphical illestration of the intervals. It is seen that for arbitrary $n$ the intervals the ith interval is given $b$

$$
\left[\frac{i-1}{2^{n}}, \frac{i}{2^{n}}\right)
$$

for $i=1,2,3, \ldots, 2^{n}$.
It follows that the intervals are given by

$$
\begin{aligned}
& {\left[0, \frac{1}{\partial^{n}}\right) \cup\left[\frac{1}{\partial^{n}}, \frac{\partial}{\partial^{n}}\right) \cup\left[\frac{\partial}{\partial^{n}}, \frac{3}{\partial^{n}}\right) \cup} \\
& {\left[\frac{3}{\partial^{n}}, \frac{4}{\partial^{n}}\right] \cup \cdots \cup\left[\frac{\partial^{n}-3}{\partial^{n}}, \frac{\partial^{n}-2}{\partial^{n}}\right)} \\
& \cup\left[\frac{\partial^{n}-2}{\partial^{n}}, \frac{\partial^{n}-1}{\partial^{n}}\right) \cup\left[\frac{\partial^{n}-1}{\partial^{n}}, 1\right)
\end{aligned}
$$

Now the odd numbered interoals will have an outcome of $u$ and the even an outcome of $D$.
It follows that

$$
\begin{aligned}
A_{n}= & \left(0, \frac{1}{2 n}\right] \cup\left(\frac{2}{2 n}, \frac{3}{2 n}\right] \cup\left(\frac{4}{2 n}, \frac{5}{2 n}\right] \cup \\
& \cdots \cup\left(\frac{2 \frac{4}{2 n}}{2 n}, 2^{n} \frac{-3}{2 n}\right] \cup\left(\frac{2 n-2}{2 n}, 2^{n}-1\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
P(k(n)=u) & =P\left(\mathbb{1}_{A_{n}}(\omega)\right) \\
& =\left(2^{n-1}\right)\left(2^{-n}\right) \\
& =\frac{1}{2}
\end{aligned}
$$

and

$$
\begin{aligned}
P(K(n)=D) & =1-P(K(n)=u) \\
& =\frac{1}{2}
\end{aligned}
$$

Trues

$$
P(K(n)=u)=P(K(n)=D)=\frac{1}{2}
$$

## Exercise

Redesign the random variable $K(n)$ so that

$$
P(K(n)=u)=P \in(0,1)
$$

## Solution

The number of interoals in $A_{n}$ is $2^{n-1}$ and the length of each interval is $2^{-n}$ if the length of the intervals are scalled by $2 p$ then the interval lengths are,
$\partial^{-n+1} P$ Similary the intervals in $A_{n}$ need to be scalled by $2(1-p)$ so that the length of each interval is $2^{-n+1}(1-p)$
It follows that

$$
K(n, \omega)=2 \rho U \mathbb{1}_{A_{n}}(\omega)+2(1-\rho) D \mathbb{1}_{A_{n}}(\omega)
$$

## Definition Borel Sets

A Borel set is any set that can be formed by countable unions or intersections or relative compliment of open or closed intervals or the real number line.

The Borel 6-algebra is an example of such a set. Recall that the $\sigma$-algebra of a set $X$ is the set $\Sigma$ of subsets of $\bar{X}$ that includes

I itself the empty set $\varnothing$ and is closed under complement and coutable union. This means that the set contains the compliements of all its elements and all countalele unions of all its elements.

Probability distributions are defined as measures on the Borel \& algebra as shown in the previous example.

## Definition

The filtration generated by a discretetime process $(\dot{x}(n)) n \geqslant 0$ (also known as its natural filtration) is a family $\sigma$-fields,

$$
\mathcal{F}_{\bar{X}}^{n}=\sigma\left(\left\{\bar{X}(k)^{-1}(B): B \in \mathbb{B}(\mathbb{R}), k=0,1, \ldots, n\right\}\right)
$$

where $B(\mathbb{R})$ is the $\sigma$-field of Borel sets on the real-line.

All elements of $\bar{X}(n)$ are 7-measureable, i.e.

$$
E\left[\bar{x}(n) \mid \tilde{J}_{\bar{x}}^{n}\right]=\bar{x}(n)
$$

The sequence

$$
\mathcal{F}_{x}^{n} \subseteq \mathcal{F}_{x}^{n+1} \subseteq \mathcal{F}_{x}^{n+2} \subseteq \cdots \subset \mathcal{F}
$$

is the fittration formed by the random variable $\bar{x}(n)$.
Note that by definiton $\mathrm{I}_{x}^{n}$ forms an increasing sequence of sets.

## Definition

A filtration is a sequence of 6 -fields such that

$$
\mathcal{F}_{I}^{n} \subseteq \mathcal{F}_{I}^{n+1} \subseteq \mathcal{F}_{I}
$$

A process $\bar{X}$ is adapted if each $\bar{X}(n)$ is $\mathcal{F}_{\bar{X}}^{n}$ measureable

If an arbitrary filtration $\left(F_{n}\right)_{n \geqslant 0}$ is fixed a filtered probebrility space,

$$
\left(\Omega, F,(J)_{n \geqslant 0}, P\right)
$$

## Example

consider $k(n)$ from the previous exercise.

$$
\begin{gathered}
K(n, \omega)=U \underline{1}_{A_{n}}(\omega)+D \underline{1}_{[0,1] / A}(\omega) \\
A_{n}=\left[0, \frac{1}{2^{n}}\right) \cup\left[\frac{2}{2^{n}}, \frac{3}{2^{n}}\right) \cup \cdots\left[\frac{2^{n}-2}{2^{n}}, \frac{2^{n}-1}{2^{n}}\right] \\
P(K(n)=u)=P(K(n)=0)=1 / 2
\end{gathered}
$$

The natural filtration for $K(n)$ is given by

$$
\begin{aligned}
\mathcal{F}_{n}^{k} & =\sigma\left(\left\{K(n)^{-1}(B): B \in B(\mathbb{R})\right\}\right) \\
& =\left\{\phi, \Omega, A_{n}, A_{n}^{c}\right\}
\end{aligned}
$$

The $\sigma$-field $\mathcal{I}_{n}$ is the power set of the partition of $\Omega=[0,1)$ which is given by

$$
\left[\frac{i-1}{2^{n}}, \frac{i}{2^{n}}\right) \quad i=1,2,3, \ldots, 2^{n} .
$$

This is an example of a s-feild generated by atoms.

## Martingales

The conditional expectation of the random variable, $I$, given the fittration, $D$, is a random variable $E[I \mid D]$ which satisfies

1. I) - measureable
2. $\forall A \in \mathcal{H}$

$$
\int_{A} E[I \mid \Delta] d P=\int_{A} I d P
$$

Conditional expectation with respect to a filtration, $\mathcal{J}_{n}$, satisfies the tower property,

$$
E\left[I \mid \mathcal{F}_{n}\right]=E\left[E\left[I \mid \mathcal{F}_{n+1}\right] \mid \mathcal{F}_{n}\right]
$$

Let

$$
M(n)=E\left[I \mid \mathcal{F}_{n}\right]
$$

## Defintion

A process $M$ is a martingale with respect to a fittration, $F_{n}$, if for all $n \geqslant 0$ and $E[\mid M(n)]<\infty$

$$
M(n)=E\left[M(n+1) \mid \mathcal{F}_{n}\right]
$$

Note that a martingale is In-colapted by the defintion of conditional expectation.

## Exercise

For $\Omega=[0,1], I(\omega)=\omega^{2}$ an 3 ${ }_{n}^{8}$ generated by

$$
\bar{X}(n, \omega)=2 \omega \mathbb{1}[0,1-1 h](\omega)
$$

where
$\mathbb{1}_{[0,1-1 n]}(\omega)= \begin{cases}1 & \omega \in[0,1-1 / n] \\ 0 & \omega \in(1-1 n, 1]\end{cases}$

It follows that
$\mathcal{F}_{n}^{X}=\{\phi,[0,1],[0,1-1 / n],(1-1 / n, 1]\}$
Now

$$
\begin{aligned}
E\left[I(\omega) \mid \mathcal{F}_{n}^{I}\right] & =\frac{1}{D([0,1-1 / n])} \int_{[0,1-n]} I_{(\omega)} d P \\
& =\frac{1}{1-1 / n} \int_{0}^{1-1 / n} \omega^{2} d \omega \\
& =\left.\frac{1}{1-1 / n} \frac{1}{3} \omega^{3}\right|_{0} ^{1-1 / n} \\
& =\left(\frac{1}{1-1 / n}\right)\left(\frac{1}{3}\right)(1-1 / n)^{3} \\
& =\frac{1}{3}(1-1 / n)^{2}
\end{aligned}
$$

$$
E\left[I(\omega) \mid \mathcal{F}_{n}^{Z}\right](\omega)= \begin{cases}\frac{1}{3}(1-1 / n)^{2} & \omega \in[0,1-1 / n] \\ 0 & \omega \in(1-1 / n, 0)\end{cases}
$$

## Exercise

show that the expectation of a martingale is constant intime

## Solution

A martinegale is defined by

$$
M(n)=E\left[M(n+1) \mid F_{n}\right]
$$

where $z_{n}$ is a filtration and $E[M(n)]<\infty$.

Now taking expectations of the martingale definition gives

$$
\begin{aligned}
E[M(n)] & =E\left[E\left[M(n+1) \mid \mathcal{F}_{n}\right]\right] \\
& =E[M(n+1)]
\end{aligned}
$$

## inus

$$
E[M(n+1)]=E[M(n)]
$$

it follows that $E[M(n)]$ is intedependent of $n$ so is a constant.

## Exercise

show that the martingale property is preserved under linear combinations with constant coefficients and adding a constant.

## Solution

Recall that a martingale with respect to the filtration $J_{n}$ is defined bil

$$
M(n)=E\left[M(n+1) \mid \tilde{J}_{n}\right]
$$

Assume that

$$
M(n)=a S(n)+b T(n)
$$

and that $s(n)$ and $T(n)$ are martingales with respect to
In From linearity of conditional expectation it follows that

$$
\begin{aligned}
E & {\left[M(n+1) \mid \mathcal{F}_{n}\right]=E\left[a S(n+1)+b T(n+1) \mid \mathcal{F}_{n}\right] } \\
& =E\left[a S(n+1) \mid \mathcal{F}_{n}\right]+E\left[b T(n+1) \mid \mathcal{F}_{n}\right] \\
& =a E\left[S(n+1) \mid \mathcal{F}_{n}\right]+b E\left[T(n+1) \mid \mathcal{F}_{n}\right] \\
& =a S(n)+b T(n)
\end{aligned}
$$

Similarly, if for constant $b$

$$
\begin{gathered}
M(n)=S(n)+b \\
E\left[M(n+1) \mid \mathcal{F}_{n}\right]=E\left[S(n+1)+b \mid \mathcal{F}_{n}\right] \\
=E\left[S(n+1) \mid \mathcal{F}_{n}\right]+E\left[b \mid \mathcal{F}_{n}\right]
\end{gathered}
$$

Now let $A \in \mathcal{F}_{n}$ then

$$
\begin{aligned}
E[b \mid A] & =\frac{1}{P(A)} \sum_{\omega \in A} b P(\omega) \\
& =\frac{b}{P(A)} \sum_{\omega \in A} P(\omega)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{b}{P(A)} P(A) \\
& =b .
\end{aligned}
$$

Thus

$$
\begin{gathered}
E\left[S(n+1) \mid \mathcal{F}_{n}\right]+E\left[b \mid \mathcal{F}_{n}\right] \\
=S(n)+b
\end{gathered}
$$

## Theorem

The sequence oldained by sums of independent random variables with zero mean is a martingale with respect to the filtration it senerates.

## Proof

Assume $L(n)$ is an arbitrary sequence of independent random variables with

$$
E[L(n)]=0
$$

and let

$$
\begin{array}{r}
Z(n)=Z(0)+\sum_{j=1}^{n} L(j) \\
F_{n}=\sigma(Z(k): 0 \leq k \leq n)
\end{array}
$$

Now using

$$
Z(n+1)=Z(n)+L(n+1)
$$

$$
\begin{gathered}
E\left[2(n+1) \mid \mathcal{F}_{n}\right]=E\left[2(n)+L(n+1) \mid \mathcal{F}_{n}\right] \\
=E\left[2(n) \mid \mathcal{F}_{n}\right]+E\left[L(n+1) \mid \mathcal{F}_{n}\right]
\end{gathered}
$$

Now $2(n)$ is $I_{n}$ measurable 50

$$
E\left[z(n) \mid \mathcal{F}_{n}\right]=z(n)
$$

and since $L(n)$ are assumed independent, $L(n+1)$ and $\mathcal{F}_{n}$ independent, so

$$
\begin{aligned}
E\left[L(n+1) \mid \mathcal{F}_{n}\right] & =E[L(n+1)] \\
& =0
\end{aligned}
$$

Bringing things together gives the desired result

$$
E\left[z(n+1) \mid \mathcal{F}_{n}\right]=z(n)
$$

## Definition Predictable Random Variable

Recall that a self-financing stategy uses knowledge of asset prices at time $n$ to determine the asset holding for the next time-step, n+1, denoted by $x(n+1)$. It follows that $x(n+1)$ is $I_{n}$-measureable. It is said the $x(n+1)$ is predicatable. Formally,

$$
\bar{Z}=(\bar{X}(n))_{n \geqslant 1}
$$

is predictable with respect to a Pittration $\left(\tilde{f}_{n}\right)_{n \geqslant 0}$ if for every $n \geqslant 1, \bar{X}(n)$ is $F_{n-1}$ measure able.

## Theorem

A predictable martingale is constant.

## Proof

From the definition of a martingale

$$
M(n)=E\left[M(n+1) \backslash \mathcal{F}_{n}\right]
$$

If $M(n+1)$ is predictable it is $I_{n}$ - measurable, so

$$
\mu(n+1)=E\left[M(n+1) \mid \mathcal{F}_{n}\right]
$$

It follows that

$$
M(n+1)=M(n)
$$

Thus $M(n)$ is constant.

## Theorem

Let $\mu$ be a martingale and

It a predictable process. If It is bounded or if both $H$ and $M$ are square integrable then $I(0)=0$ and

$$
X(n)=\sum_{j=1}^{n} H(j)[M(j)-M(j-1)]
$$

is a martingale.

## Proof

Let $F_{n}$ be the filtration generated by $\mu(n)$ and let

$$
\Delta M(j)=M(j)-M(j-1)
$$

then

$$
\begin{aligned}
\Delta X(n)= & \sum_{j=1}^{n} H(j) \Delta M(j) \\
& -\sum_{j=1}^{n-1} H(j) \Delta M(j)
\end{aligned}
$$

$$
\begin{aligned}
= & H(n) \Delta M(n)+\sum_{j=1}^{n-1} H(j) \Delta M(j) \\
& -\sum_{j=1}^{n-1} H(j) \Delta M(j)
\end{aligned}
$$

$$
\Delta \underline{X}(n)=H(n) \Delta M(n)
$$

## Taking conditional expectation with respect In-1 gives

$$
\begin{aligned}
E[ & \left.\Delta \times(n) \mid \mathcal{F}_{n-1}\right]=E\left[H(n) \Delta M(n)\left(\mathcal{F}_{n-1}\right]\right. \\
& =E\left[H(n)(M(n)-M(n-1)) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[H(n) M(n) \mid \mathcal{F}_{n-1}\right]-E\left[H(n) M(n-1) \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

Now since $H(n)$ is predictable

$$
H(n)=E\left[H(n)\left(\xi_{n-1}\right]\right.
$$

so using taking at what is known,

$$
\begin{aligned}
E\left[H(n) M(n-1) \mid \mathcal{F}_{n-1}\right] \\
=H(n) E\left[M(n-1) \mid \mathcal{F}_{n-1}\right] \\
=H(n) M(n-1)
\end{aligned}
$$

The last step follows from the assumption that $M(n)$ is a martingale so $M(n)$ is $F_{n-1}$ measurable.

For the second term

$$
\begin{aligned}
E\left[H(n) M(n) \mid \mathcal{F}_{n-1}\right] & \\
& =H(n) E\left[M(n) \mid \mathcal{F}_{n-1}\right] \\
& =H(n) M(n-1)
\end{aligned}
$$

The last step follows from the assumption that $M(n)$ is a martingale.
Pulling things together gives

$$
E\left[\Delta x(n) \mid \Im_{n-1}\right]=0
$$

$$
\begin{aligned}
\Rightarrow E\left[\bar{X}(n)-\bar{X}(n-1) \mid \tilde{J}_{n-1}\right]=0 & \\
\Rightarrow E\left[\bar{X}(n) \mid \tilde{J}_{n-1}\right]-E\left[\bar{X}(n-1) \mid \tilde{J}_{n-1}\right]=0 & \\
\Rightarrow E\left[\bar{X}(n) \mid \tilde{J}_{n-1}\right] & =E\left[\bar{X}(n-1) \mid \tilde{J}_{n-1}\right] \\
& =\bar{X}(n-1)
\end{aligned}
$$

The last step will follow since $\bar{X}(n-1)$ is $\mathcal{F}_{n-1}$ - measureable. Thus the desired result is obtained,

$$
E\left[\bar{x}(n) \mid \tilde{\exists}_{n-1}\right]=\bar{x}(n-1)
$$

## Exercise

Recall a random walk is defined by

$$
\begin{aligned}
Z(n) & =Z(n-1)+L(n) \\
& =\sum_{i=1}^{n} L(n)
\end{aligned}
$$

where for simplicity it has been assumed that $2(0)=0$, and $L(n)$ is an arbitrary
sequence of independer random variables with zero mean.
Let $M$ be a martingale with respert to the filtration generated by $L(n)$ which is denoted by
$\exists_{n}$.

Show that there exists a predictable process $H(n)$ such that

$$
\begin{aligned}
M(n) & =\sum_{i=1}^{n} H(i) L(i) \\
& =\sum_{i=1}^{n} H(i)(Z(i)-Z(i-1)) \\
& =\sum_{i=1}^{n} H(i) \Delta Z(i)
\end{aligned}
$$

Solution

$$
\begin{aligned}
M(n)-M(n-1) & =\sum_{i=1}^{n} H(i) L(i)-\sum_{i=1}^{n-1} H(i) L(i) \\
& =H(n) L(n)
\end{aligned}
$$

$$
\Rightarrow \quad \Delta M(n)=H(n) L(n)
$$

Taking expectation with respect to $J_{n-1}$ gives

$$
E\left[\Delta M(n) \mid \tilde{F}_{n-1}\right]=E\left[H(n) L(n) \mid \tilde{F}_{n-1}\right]
$$

Now, since $M(n)$ is a martingale

$$
\begin{aligned}
& E\left[M(n)-M(n-1) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[M(n) \mid \mathcal{F}_{n-1}\right]-E\left[M(n-1)\left(\mathcal{F}_{n-1}\right]\right. \\
& =M(n-1)-M(n-1) \\
& =0
\end{aligned}
$$

So

$$
E\left[H(n) L(n) \mid \mathcal{F}_{n-1}\right]=0
$$

This is trivially solved if $H(n)=0 \quad \forall n$. Also, if $H(n)$ is predictable then

$$
E\left[H(n) \mid \mathcal{F}_{n-1}\right]=H(n)
$$

so using the "taking out what is known" property of conditional expectation gives

$$
H(n) E\left[L(n) \mid \mathcal{F}_{n-1}\right]=0
$$

but $L(n)$ are independent so $L(n)$ is independent of $I_{n-1}$,

$$
E\left[\left((n) \mid \Im_{n-1}\right]=E[L(n)]=0\right.
$$

## Thus the desired result is obtained.

It follows that

$$
M(n)=\sum_{i=1}^{n} H(i) \Delta Z(i)
$$

is a martinegale. If $H(i)$ is predictable with respect to the filtration senerated
by $\Delta Z(i)=L(i)$. This has the form of a stochastic integral and is considered a representation theorem since each martingale can be written as a stochastic integral over a sequence of independent random veriables

## Exercise

show that the process

$$
\begin{aligned}
Z^{2}(n) & =\left[\sum_{i=1}^{n} L(i)\right]^{2} \\
& =\sum_{i=1}^{n} \sum_{j=1}^{n} L(i) L(j)
\end{aligned}
$$

is not a martingale.
Solution
Recall that

$$
Z(n)=\sum_{i=1}^{n} L(i)
$$

where $L(i)$ are arbitrary indspendent random variables with zero mean.

Now

$$
\begin{aligned}
& 2(n+1)=2(n)+L(n+1) \\
\Rightarrow \quad & 2^{2}(n+1)=2^{2}(n)+2 L(n+1) Z(n)+c^{2}(n+1)
\end{aligned}
$$

Let $I_{n}$ denote the filtration generated $L(n)$. Taking expectation with respect to $J_{n}$ gives

$$
\begin{gathered}
E\left[Z^{2}(n+1) \mid \mathcal{F}_{n}\right]=E\left[Z^{2}(n)+2 L(n+1) Z(n)\right. \\
\left.+L^{2}(n+1) \mid \mathcal{J}_{n}\right] \\
=E\left[Z^{2}(n) \mid \mathcal{F}_{n}\right]+2 E\left[L(n+1) Z(n) \mid \mathcal{F}_{n}\right] \\
+E\left[L^{2}(n+1) \mid \mathcal{F}_{n}\right]
\end{gathered}
$$

Consider

$$
Z(n)=\sum_{i=1}^{n} L(i)
$$

since $J_{n}$ is generated by $L(n)$ it follows that $z(n)$ is $F_{n}$-measureable thus

$$
E\left[z(n) \mid \mathcal{F}_{n}\right]=z(n)
$$

## Thus

$$
\begin{aligned}
& E\left[z^{2}(n+1) \mid \mathcal{F}_{n}\right]=E\left[z^{2}(n) \mid \mathcal{F}_{n}\right] \\
& +2 E\left[L(n+1) z(n) \mid \mathcal{F}_{n}\right]+E\left[L^{2}(n+1) \mid \mathcal{F}_{n}\right] \\
& =z^{2}(n)+2 z(n) E\left[L(n+1) \mid \mathcal{F}_{n}\right] \\
& +E\left[L^{2}(n+1) \mid \Im_{n}\right]
\end{aligned}
$$

The $L(n)$ have zero mean and since the $L(n)$ are independent $L(n+1)$ and $I_{n}$ are independent,

$$
E\left[L(n+1) \mid \exists_{n}\right]=E[L(n+1)]=0
$$

and

$$
\begin{aligned}
E\left[L^{2}(n+1) \mid \tilde{J}_{n}\right] & =E\left[L^{2}(n+1)\right] \\
& =\sigma^{2}
\end{aligned}
$$

Putting trings together gives

$$
E\left[z^{2}(n+1) \mid \mathcal{F}_{n}\right]=z^{2}(n)+\sigma^{2}
$$

Thus the desired result is obtained, $2^{2}(n+1)$ is not a martingale.

## Conditional Jenser's Inequality

Let $(\Omega, D, P)$ be a probability space. If $\varphi: \mathbb{R} \rightarrow \mathbb{R}$ is a convex function and $I$ a random variable. Show that

$$
E[\varphi(X(Y)] \geqslant \varphi(E[\bar{x} \mid y])
$$

## Solution

For a convex function the following relation holds,

$$
\varphi(x) \geqslant \varphi(y)+\varphi^{\prime}(y)(y-x)
$$

Let $x=\Sigma$ and $y=E[\bar{x} \mid 2]]$

$$
\begin{gathered}
\varphi(\underline{x}) \geqslant \varphi(E[\underline{x} \mid \mathscr{y}])+\phi^{\prime}(E[\bar{x} \mid \mathscr{y}]) \\
(E[\bar{x} \mid \mathscr{y}]-\bar{x})
\end{gathered}
$$

Taking conditional expectations
gives

$$
\begin{aligned}
& E[\varphi(X) \mid \Delta] \geqslant E[\varphi(E[X \mid \Delta]) \mid g] \\
& +E\left[\varphi^{\prime}(E[X \mid \Delta])(E[X \mid \Delta]-X)\right]
\end{aligned}
$$

Now $E[\underline{x} \mid A], \varphi(E[\underline{x} \mid A])$ and $\phi^{\prime}(E[X \mid y])$ are both $y$-measureable. It follows that,

$$
\begin{aligned}
E[\varphi & (\bar{X}) \mid y] \geqslant \varphi(E[\bar{X} \mid \Delta]) \\
& +E\left[\varphi^{\prime}(E[\bar{X} \mid \Delta]) E[\bar{X} \mid \Delta] \mid \Delta\right] \\
& -E\left[\varphi^{\prime}(E[\bar{X} \mid \Delta]) \bar{X} \mid \Delta\right] \\
= & \varphi(E[\bar{X} \mid \Delta])+\varphi^{\prime}(E[\bar{X} \mid \Delta]) E[\bar{X} \mid \Delta] \\
& -\varphi^{\prime}(E[\bar{X} \mid \Delta]) E[\bar{X} \mid \Delta] \\
= & \varphi(E[\bar{X} \mid \Delta])
\end{aligned}
$$

## Thus

$$
E[\varphi(X) \mid y] \geqslant \varphi(E[x \mid y])
$$

Let $q(x)=x^{2}, y=\mathcal{F}_{n}$ and $\bar{X}=M(n+1)$. then

$$
E\left[M^{2}(n+1) \mid \mathcal{F}_{n}\right] \geqslant\left\{E\left[M(n+1) \mid \mathcal{F}_{n}\right]\right\}^{2}
$$

but since $M(n)$ is a martingale so,

$$
E\left[M(n+1) \mid \mathcal{F}_{n}\right]=M(n)
$$

It follows that

$$
E\left[M^{2}(n+1) \mid \Im_{n}\right] \geqslant M^{2}(n)
$$

which is consistent with result obtained in previous exercise.

## Definition

A process, $\bar{X}(n)$, that is $F_{n}$-adapted is $\hat{J}_{n}$-measureable for avery $n$.

## Definition

A $\mathcal{F}^{n}$-adapted process, X(n), integable for all $n$, is

1. a submartingale if,

$$
E\left[\bar{X}(n+1) \mid \mathcal{F}_{n}\right] \geqslant \bar{X}(n)
$$

2. a supermartingale if,

$$
E\left[X_{(n+1)} \mid{\xi_{n}}\right] \leqslant X_{(n)}
$$

It follows that the square of a martingale is a submartingale.

## Exerase

show that if $\bar{X}$ is a submartingale, then its
with in,

$$
E[\bar{x}(0)] \leqslant E[\bar{x}(1)] \leqslant E[\bar{x}(2)] \leqslant \cdots
$$

and if $I$ is a supermartingale

$$
E[\bar{x}(0)] \geqslant E[\bar{x}(1)] \geqslant E[\bar{x}(2)] \geqslant \cdots
$$

## Solution

If $X(n)$ is a submartingale it satisfies

$$
E\left[\bar{X}(n+1) \mid \mathcal{F}_{n}\right] \geqslant \bar{X}(n)
$$

> Taking expectations gives $E\left[E\left[X(n+1) \mid \mathcal{F}_{n}\right]\right] \geqslant E[(n)]$

but

$$
E\left[E\left[X(n+1) \mid \mathcal{F}_{n}\right]\right]=E[\bar{X}(n+1)]
$$

## Thus

$$
E[\bar{X}(n+1)] \geqslant E[\bar{X}(n)]
$$

the desired result follows

$$
E[\bar{x}(0)] \leqslant E[\bar{x}(0)] \leqslant E[\bar{x}(2)] \leqslant \cdots
$$

Similarly, for a supermartingale,

$$
E\left[\bar{X}(n+1)\left(\mathcal{F}_{n}\right] \leqslant \bar{X}(n)\right.
$$

taking expectations gives the desired result

$$
E[\bar{X}(n+1)] \leqslant E[\bar{X}(n)]
$$

80

$$
E[\Phi(0)] \geqslant E[\Phi(1)] \geqslant E[\bar{X}(2) \geqslant \cdots
$$

## Exercise

Let $I(n)$ martingale, submartingale, supermartingale. For a fixed $m$, consider the sequence

$$
\bar{X}^{\prime}(k)=\bar{X}(m+k) \cdot \bar{X}(m) \quad k \geqslant 0
$$

show that $I^{\prime}$ is a martingale, submartingale, supermartingale with respect to the filtration,

$$
\exists_{k}^{\prime}=\exists_{k+m}
$$

## Solution

First assume that $\Sigma(n)$ is a martingale, so taking conditional expectation with respect to $\mathcal{F}_{k}^{\prime}$ gives

$$
E\left[\bar{X}^{\prime}(k+1) \mid \mathcal{F}_{k}^{\prime}\right]=E\left[\bar{X}(m+k+1)-\bar{X}(m) \mid \mathcal{F}_{k}^{\prime}\right]
$$

$$
=E\left[\bar{X}(m+k+1) \mid \mathcal{F}_{k}^{\prime}\right]-E\left[\bar{X}(m) \mid \mathcal{F}_{k}^{\prime}\right]
$$

Now, since $X(n)$ is a martingale it follows that,

$$
\begin{gathered}
E\left[\bar{X}(m+k+1) \mid \tilde{J}_{k}^{\prime}\right]=E\left[\bar{X}(m+k+1) \mid \Psi_{m+k}\right] \\
=\bar{X}(m+k)
\end{gathered}
$$

and

$$
\begin{aligned}
E\left[\bar{x}(m) \mid \mathcal{F}_{k}^{\prime}\right] & =E\left[\bar{x}(m) \mid \mathcal{F}_{m+k}\right] \\
& =\bar{x}(m)
\end{aligned}
$$

Since X(m) will be $I_{m+k}$ measure able for $k \geqslant 0$. Bringing tnings together

$$
\begin{aligned}
E\left[\bar{X}^{\prime}(k+1) \mid \mathcal{F}_{k}^{\prime}\right] & =\bar{X}(m+k)-\bar{X}(m) \\
& =\bar{X}^{\prime}(k)
\end{aligned}
$$

Thus $X^{\prime}(k)$ is a martingale.

## Proofs for submartingal or submartingale are similar.

## The Doob Decomposition

The Dool decomposition is a method for representing submartingales and supermartigales as the sum of a martingale and a predictable process.

## Theorem Doob Decomposition

If $I(n)$ is a submartingale with respect to some filtration, then there evsts, for the same fittration, a martingale, $M(n)$, and a predictable, increasing process A(n) with $M(0)=A(0)=0$ such that

$$
\bar{I}(n)=\bar{I}(0)+M(n)+A(n)
$$

This decomposition is unique. The process A(n) is called the compensator of the submaringale I

To understand the deomposition
let $I(0)=M(0)=0$. Then

$$
\begin{aligned}
\bar{Y}(n) & =M(n)+A(n) \\
\Rightarrow M(n) & =\bar{I}(n)-\Delta(n)
\end{aligned}
$$

Now $A(0)=0$ and $A(n)$ is increasing so $A(h)>0$ and since $I(n)$ is a submartingale

$$
\bar{Y}(n) \geqslant M(n)
$$

Thus $A(n)$ is subtracting from $I(n)$ the amount needed to be a martingale.

## Proof

Since $A(1)$ is predictable it follows that it is $I_{0}$ measureable, so it must be a constant. From the defining relation

$$
I(1)=I(0)+M(1)+A(1)
$$

I(1) and MCI) are random.
so taking expectations gives

$$
E[I(1)]=I(0)+E[M(1)]+A(1)
$$

since $M(1)$ is a martingale and $M(0)=0$ it follows that

$$
E[M(0)]=E[M(1)]=E[M(2)]=\cdots=0
$$

Thus

$$
\begin{aligned}
& E[\Psi(1)]=\bar{I}(0)+A(1) \\
\Rightarrow & A(1)=E[\bar{I}(1)]-\bar{I}(0)
\end{aligned}
$$

Now from the defining relation

$$
\begin{aligned}
\underline{I}(1) & =\bar{I}(0)+M(1)+A(1) \\
\Rightarrow M(1) & =\underline{I}(1)-I(0)-A(1) \\
& =I(1)-\bar{I}(0)-E[I(1)]+\underline{I}(0) \\
& =I(1)-E[I(1)]
\end{aligned}
$$

In summary for $n=1$

$$
\begin{aligned}
& I(1)=I(0)+M(1)+A(1) \\
& A(1)=E[I(1)]-I(0) \\
& M(1)=I(1)-E[I(1)]
\end{aligned}
$$

Now for $n=2$

$$
\begin{aligned}
I(2)=I(0)+M(2)+A(2) \\
\Rightarrow \quad A(2)=I(2)-I(0)-M(2)
\end{aligned}
$$

Recall that $A(2)$ is $\Im_{1}$-predictable so

$$
E\left[A(2)\left(Y_{1}\right]=A(2)\right.
$$

It follows that

$$
A(2)=E\left[I(2) \mid \mathcal{F}_{1}\right]-I(0)-E\left[\mu(2) \mid \mathcal{F}_{l}\right]
$$

but $M(n)$ is a martigale with respect to $I_{n}$ so

$$
E\left[M(2) \mid \mathcal{F}_{1}\right]=M(1)
$$

So,

$$
A(2)=E\left[I(2) \mid \Im_{1}\right]-I(0)-M(1)
$$

but

$$
M(1)=I(1)-I(0)-A(1)
$$

so

$$
\begin{aligned}
A(2)= & E\left[\bar{I}(2) \mid J_{1}\right]-\bar{I}(0)-\bar{I}(1)+\bar{I}(0) \\
& +A(1) \\
= & E\left[\bar{I}(2) \mid J_{1}\right]-\bar{I}(0)+A(1) \\
& -[\bar{I}(1)-\bar{I}(0)]
\end{aligned}
$$

but I(1) is $\mathfrak{F}_{1}$-measurable, so

$$
I(1)=E\left[I(1) \mid \mathcal{F}_{1}\right]
$$

bringing things together

$$
\begin{gathered}
A(2)=A(1)+E\left[I(2)-I(1) \mid \mathcal{F}_{1}\right] \\
M(2)=I(2)-I(0)-A(2)
\end{gathered}
$$

This result sugserts the gereral result,

$$
\begin{gathered}
A(n)=A(n-1)+E\left[I(n)-I(n-1) \mid I_{n-1}\right] \\
M(n)=I(n)-I(0)-A(n)
\end{gathered}
$$

Next it is shown that $M(n)$ is a martingale.

$$
\begin{aligned}
& E\left[M(n) \mid \mathcal{F}_{n-1}\right]=E\left[I(n)-I(0)-A(n) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[I(n) \mid \mathcal{F}_{n-1}\right]-\bar{I}(0)-E\left[A(n) \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

but $A(n)$ is predictable so

$$
\begin{aligned}
& E\left[A(n) \mid \mathcal{F}_{n-1}\right]=A(n) \\
& =A(n-1)+E\left[\Psi(n)-I(n-1) \mid \mathcal{J}_{n-1}\right]
\end{aligned}
$$

Bringing things together gives the desired result.

$$
\begin{aligned}
& E\left[M(n) \mid \exists_{n-1}\right]=E\left[I(n) \mid F_{n-1}\right] \\
& -I(0)-A(n-1)-E\left[I(n)-I(n-1) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[I(n) \mid \exists_{n-1}\right]-I(0)-A(n-1) \\
& -E\left[I(n) \mid \exists_{n-1}\right]+E\left[I(n-1) \mid \exists_{n-1}\right]
\end{aligned}
$$

but $I(n-1)$ is $I_{n-1}$ measureable so

$$
\begin{aligned}
E\left[M(n) \mid \Im_{n-1}\right] & =\bar{I}(n-1)-I_{1}(0)-A(n-1) \\
& =M(n-1)
\end{aligned}
$$

Thus M(n) is a martingale In a similar manner the Doob decomposition for supermartangales is given by

$$
\begin{gathered}
A(n)=A(n-1)-E\left[I(n)-I(n-1) \mid I_{n-1}\right] \\
M(n)=A(n)+I(n)-I(0)
\end{gathered}
$$

## Exerase

Let $z(n)$ be a random walk where

$$
\begin{gathered}
Z(0)=0 \\
Z(n)=\sum_{j=1}^{n} L(j)=2(n-1)+L(j)
\end{gathered}
$$

and $L(j)$ are independent random variables with values $\pm 1$.
Let $I_{n}$ be the fittration generated by $L(n)$,

$$
F_{n}=\sigma(L(1), L(2), \ldots, L(n))
$$

verify that $z^{2}(n)$ is a submartingale and find the increasing process $A$ in its Doob decomposition.

## Solution

$$
\begin{aligned}
z^{2}(n)= & {[z(n-1)+L(n)]^{2} } \\
= & z^{2}(n-1)+2 L(n) z(n-1) \\
& +L^{2}(n)
\end{aligned}
$$

Now

$$
\begin{aligned}
E & {\left[z^{2}(n) \mid \Im_{n-1}\right]=E\left[z^{2}(n-1) \mid \Im_{n-1}\right] } \\
& +2 E\left[L(n) 2(n-1) \mid \Im_{n-1}\right] \\
& +E\left[L^{2}(n) \mid \Im_{n-1}\right]
\end{aligned}
$$

but $2(n-1)$ is $J_{n-1}$-measureatle 80,

$$
\begin{aligned}
& E\left[z^{2}(n-1) \mid \exists_{n-1}\right]=z^{2}(n-1) \\
& E\left[L(n) z(n-1) \mid \exists_{n-1}\right] \\
& \quad=z(n-1) E\left[L(n) \mid \exists_{n-1}\right]
\end{aligned}
$$

So

$$
\begin{aligned}
E & {\left[z^{2}(n) \mid \mathcal{F}_{n-1}\right]=2^{2}(n-1) } \\
& +2(n-1) E\left[L(n) \mid \mathcal{F}_{n-1}\right]+E\left[L^{2}(n) \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

Next, the $L(n)$ are independent so

$$
\begin{aligned}
& E\left[L(n) \mid \Im_{n-1}\right]=E[L(n)]=0 \\
& E\left[L^{2}(n) \mid \Im_{n-1}\right]=E\left[L^{2}(n)\right]=1
\end{aligned}
$$

Thus the final result is given by

$$
E\left[z^{2}(n) \mid \exists_{n-1}\right]=2^{2}(n-1)+1
$$

it follows that $z^{2}(n)$ is a submartingale,

$$
E\left[z^{2}(n) \mid \mathcal{F}_{n-1}\right] \geqslant z^{2}(n-1)
$$

For a submartingale the Doob decomposition is given by

$$
\begin{gathered}
A(n)=A(n-1)+E\left[Z^{2}(n)-Z^{2}(n-1) \mid \mathcal{I}_{n-1}\right] \\
M(n)=Z^{2}(n)-Z^{2}(0)-A(n)
\end{gathered}
$$

Now

$$
\begin{aligned}
Z^{2}(n)= & Z^{2}(n-1)+2 L(n) z(n-1) \\
& +L^{2}(n) \\
\text { so } & \\
Z^{2}(n) & -Z^{2}(n-1)=2 L(n) z(n-1)+L^{2}(n)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
E[ & \left.Z^{2}(n)-Z^{2}(n-1) \mid \mathcal{F}_{n-1}\right] \\
= & E\left[2 L(n) Z(n-1)+L^{2}(n) \mid \mathcal{F}_{n-1}\right] \\
= & 2 Z(n-1) E\left[L(n) \mid \mathcal{F}_{n-1}\right] \\
& +E\left[L^{2}(n) \mid \mathcal{F}_{n-1}\right] \\
= & 2 Z(n-1) E[L(n)]+E\left[L^{2}(n)\right] \\
= & 1
\end{aligned}
$$

Thus

$$
\begin{aligned}
A(n) & =A(n-1)+E\left[Z^{2}(n)-Z^{2}(n-1) \mid J_{n-1}\right] \\
& =A(n-1)+1
\end{aligned}
$$

and

$$
A(n)=A(n-1)+1
$$

since $A(0)=0$

$$
A(n)=n
$$

and

$$
\begin{aligned}
M(n) & =Z^{2}(n)-Z^{2}(0)-A(n) \\
& =Z^{2}(n)-n
\end{aligned}
$$

## Theorem

If $M(n) \in L^{2}(\Omega)$, is square integrable on $\Omega$, is a martingale with $M(0)=0$. Then for $n>m$

$$
\begin{aligned}
& E\left[(M(n)-M(m))^{2} \mid \Im_{m}\right] \\
& \quad=E\left[M^{2}(n)-M^{2}(m) \mid \Im_{m}\right]
\end{aligned}
$$

## Proof

$$
\begin{aligned}
E[ & \left.(M(n)-M(m))^{2} \mid \mathcal{F}_{m}\right] \\
= & E\left[M^{2}(n)-2 M(n) M(m)+M^{2}(m) \mid \mathcal{F}_{m}\right] \\
= & E\left[M^{2}(n) \mid \mathcal{F}_{m}\right]-2 E\left[M(n) M(m) \mid \mathcal{F}_{m}\right] \\
& +E\left[M^{2}(m) \mid \mathcal{F}_{m}\right]
\end{aligned}
$$

Now

$$
\begin{gathered}
E\left[M(n) M(m) \mid \Im_{m}\right]=M(m) E\left[M(n) \mid \mathcal{F}_{m}\right] \\
=M^{2}(m)
\end{gathered}
$$

since $M(n)$ is a martingale and since $M(m)$ is $\mathcal{F}_{m}$-measureable

$$
E\left[M^{2}(m) \mid J_{m}\right]=M^{2}(m)
$$

Bringing things together

$$
\begin{aligned}
E\left[(M(n)-M(m))^{2} \mid \Im_{m}\right] \\
E\left[M^{2}(n) \mid \exists_{m}\right]-2 M^{2}(m) \\
+M^{2}(m) \\
=E\left[M^{2}(n) \mid \exists_{m}\right]-M^{2}(m) \\
=E\left[M^{2}(n)-M^{2}(m) \mid \exists_{m}\right]
\end{aligned}
$$

Where the last step follows from $M^{2}(m)$ being $F_{m}$ - measurable.

## Thus

$$
\begin{aligned}
& E\left[(M(n)-M(m))^{2} \mid \mathcal{F}_{m}\right] \\
& \quad=E\left[M^{2}(n)-M^{2}(m) \mid \mathcal{F}_{m}\right]
\end{aligned}
$$

Recall that the discrete stochastic integral of a predictable process A with respect the the martingale $M$ is defined by

$$
\bar{X}(n)=\sum_{k=1}^{n} H(k)[\mu(k)-\mu(k-1)]
$$

where $\bar{I}(0)=0$. It was previously shown that $I(n)$ is a martingale.

## Theorem Discrete Its Isometry

If $I(n)$ is square integrable, then

$$
E\left[X^{2}(n)\right]=E\left[\sum_{k=1}^{n} H^{2}(k)[A(k)-A(k-1)]\right]
$$

where $A$ is the compensator of $M^{2}$

## Proof

Recall that,

$$
\bar{X}(n)=\sum_{k=1}^{n} H(k)[\mu(k)-\mu(k-1)]
$$

so

$$
\begin{gathered}
Z^{2}(n)=\sum_{i=1}^{n} \sum_{j=1}^{n} H(i)[M(i)-M(i-1)] \\
H(j)[M(j)-M(j-1)]
\end{gathered}
$$

and

$$
\begin{gathered}
E\left[X^{2}(n)\right]=E\left[\sum_{i=1}^{n} \sum_{j=1}^{n} H(i)[M(i)-M(i-1)]\right. \\
H(j)[M(j)-M(j-1)]] \\
=\sum_{i=1}^{n} \sum_{j=1}^{n} E[H(i) H(j)[M(i)-M(i-1)] \\
[M(j)-M(j-1)]]
\end{gathered}
$$

Now assume that $i<j$. This assumption is so that M(i) is $\mathrm{F}_{j-1}$ measureable. Also, recall that the expectation of conditional
expectation satisfies

$$
E[E[\bar{X} \mid \mathcal{F}]]=E[\bar{X}]
$$

It follows that,

$$
\begin{aligned}
& E[H(i) H(j)[M(i)-M(i-1)][M(j)-M(j-1)]] \\
= & E[E[H(i) H(j)[M(i)-M(i-1)] \\
& {\left.\left.[M(j)-M(j-1)] \mid \mathcal{F}_{j-1}\right]\right] }
\end{aligned}
$$

Now $H(j)$ and $H(i)$ are preditable by $\mathcal{F}_{j-1}$ and $M(i)$ and $M(i-1)$ are $J_{j-1}$ measureable, so

$$
\begin{array}{r}
E[E[H(i) H(j)[M(i)-M(i-1)] \\
\left.\left.[M(j)-M(j-1)] \mid \mathcal{J}_{j-1}\right]\right] \\
=E[H(i) H(j)[M(i)-M(i-1)] \\
\left.E\left[M(j)-M(j-1) \mid \mathcal{J}_{j-1}\right]\right]
\end{array}
$$

since $M(j)$ is a martingale it follows that

$$
\begin{aligned}
& E\left[M(j)-M(j-1) \mid j_{j-1}\right] \\
& =E\left[M(j) \mid \mathcal{F}_{j-1}\right]-E\left[M(j-1) \mid \mathcal{F}_{j-1}\right] \\
& =M(j-1)-M(j-1) \\
& =0
\end{aligned}
$$

$$
\text { Thus, for } c<j
$$

$$
\begin{array}{r}
\sum_{i=1}^{n} \sum_{j=1}^{n} E[H(i) H(j)[M(i)-M(i-1)] \\
[M(j)-M(j-1)]]=0
\end{array}
$$

A similiar argument can be made for $j<i$. Now consider $j=i$ the expectation becomes,

$$
\begin{aligned}
& E\left[H^{2}(i)[\mu(i)-\mu(i-1)]^{2}\right] \\
& \quad=E\left[E\left[H^{2}(i)[\mu(i)-\mu(i-1)]^{2} \mid \mathcal{F}_{i-1}\right]\right]
\end{aligned}
$$

but $H(i)$ is predictable so

$$
\begin{aligned}
& E\left[E\left[H^{2}(i)(M(i)-M(i-1))^{2} \mid \mathcal{F}_{i-1}\right]\right] \\
= & E\left[H^{2}(i) E\left[(M(i)-M(i-1))^{2} \mid \mathcal{F}_{i-1}\right]\right]
\end{aligned}
$$

Now previousiy it was shown that

$$
\begin{aligned}
& E\left[(M(i)-M(i-1))^{2} \mid \mathcal{F}_{i-1}\right] \\
& \quad=E\left[M^{2}(i)-M^{2}(i-1) \mid \mathcal{F}_{i-1}\right]
\end{aligned}
$$

Recall that $M^{2}(i)$ is a submartingal, so the recurrance relation for the compensator is given by

$$
\begin{aligned}
& A(n)=A(n-1)+E\left[M^{2}(i)-M^{2}(i-1) \mid \mathcal{F}_{i-1}\right] \\
\Rightarrow & A(n)-A(n-1)=E\left[M^{2}(i)-M^{2}(i-1) \mid \mathcal{F}_{i-1}\right]
\end{aligned}
$$

Bringing things together gives the desined result. For

$$
\begin{gathered}
\bar{X}(n)=\sum_{k=1}^{n} H(K)[\mu(K)-\mu(K-1)] \\
E\left[Z^{2}(n)\right]=\sum_{i=1}^{n} E\left[H^{2}(i) E\left[(M(i)-M(i-1))^{2} \mid \mathcal{F}_{i-1}\right]\right] \\
=\sum_{i=1}^{n} E\left[H^{2}(i)(A(n)-A(n-1)]\right. \\
=-E\left[\bar{X}^{2}(n)\right]=E\left[\sum_{i=1}^{n} H^{2}(i)(A(n)-A(n-1)]\right.
\end{gathered}
$$

## Exercise

Using the Doob decomposition show that if $I$ is a square integrable submartingale and It is predictable with bounded non-negative $H(n)$, then the stochastic integral of $H$ with
respect to $I$ is also a submartingale.

## Solution

Now the stochaster integral of $t t$ with respect to $\frac{1}{1}$ is given by.

$$
\sum_{i=1}^{n} H(i)[q(i)-\bar{I}(i-1)]
$$

since $H(i)$ is predictable it is $F_{n-1}$ measureable so

$$
H(i)=E\left[H(i) \mid \mathcal{F}_{n-1}\right]
$$

where $\bar{Y}(i)$ is a submartingale with respect to the fittration $\mathcal{F}_{i}$ and since $\bar{I}(i)$ is a submartingale

$$
E\left[\bar{Y}(i) \mid \mathcal{F}_{i-1}\right] \geqslant \bar{Y}(i-1)
$$

The Doob decomposition of $\bar{Y}(i)$
is given by

$$
\begin{gathered}
A(n)=A(n-1)+E\left[I(n)-I(n-1) \mid I_{n-1}\right] \\
M(n)=I(n)-I(0)-A(n) \\
\Rightarrow I(n)=M(n)+I(0)+A(n)
\end{gathered}
$$

where m(n) is a martingale and $A(n)$ is predicable wrth respect to $I_{n}$,

$$
\begin{aligned}
& E\left[M(n) \mid F_{n-1}\right]=M(n-1) \\
& E\left[A(n) \mid F_{n-1}\right]=A(n)
\end{aligned}
$$

Now let,

$$
\underline{X}(n)=\sum_{i=1}^{n} H(i)[\underline{I}(i)-\underline{I}(i-1)]
$$

50

$$
\bar{X}(n)-\bar{X}(n-1)=\sum_{i=1}^{n} H(i)[\bar{Y}(i)-\underline{Y}(i-1)]
$$

$$
\begin{aligned}
& -\sum_{i=1}^{n-1} H(i)[\bar{I}(i)-\bar{I}(i-1)] \\
= & H(i)[\bar{I}(i)-\bar{I}(i-1)] \\
\Rightarrow & \bar{X}(n)-\bar{X}(n-1)=H(n)[\bar{I}(n)-\bar{I}(n-1)]
\end{aligned}
$$

Taking expectation with respect to $\mathcal{F}_{n-1}$ gives

$$
\begin{aligned}
E[\bar{X}(n) & \left.-\underline{X}(n-1) \backslash \widetilde{J}_{n-1}\right] \\
& =E\left[H(n)[\bar{I}(n)-\underline{I}(n-1)] \mid \exists_{n-1}\right]
\end{aligned}
$$

Since $H(n)$ is pridictable

$$
E\left[H(n) \mid \exists_{n-1}\right]=H(n)
$$

using taking out what is known
gives

$$
\begin{aligned}
& E\left[H(n)[\bar{X}(n)-\underline{X}(n-1)] \mid \mathcal{F}_{n-1}\right] \\
& \quad=H(n) E\left[I(n)-I(n-1) \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

Now from the Doob expansion

$$
A(n)-A(n-1)=E\left[I(n)-I(n-1) \mid I_{n-1}\right]
$$

50

$$
\begin{aligned}
E[\bar{X}(n)- & \left.\bar{X}(n-1) \mid \mathcal{F}_{n-1}\right] \\
& =H(n)[A(n)-A(n-1)]
\end{aligned}
$$

now since A(0) is positive and $A(n)$ is increasing it follows that

$$
A(n)-A(n-1) \geqslant 0
$$

and it is asswmed that $H(n)$ is non-negative it follows that

$$
H(n) \geqslant 0
$$

50

$$
H(n)[A(n)-A(n-1)] \geqslant 0
$$

and

$$
E\left[\bar{X}(n)-\bar{X}(n-1) \mid \mathcal{F}_{n-1}\right] \geqslant 0
$$

$$
\Rightarrow E\left[\bar{X}(n) \mid \mathcal{F}_{n-1}\right] \geqslant E\left[\bar{X}(n-1) \mathcal{F}_{n-1}\right]
$$

now $\bar{x}(n-1)$ is $I_{n-1}$ measurable since the right-hand-side is so,

$$
E\left[\bar{X}(n-1) \mid \mathcal{F}_{n-1}\right]=\bar{X}(n-1)
$$

and the desired result follows

$$
E\left[\bar{X}(n-1) \mid \mathcal{F}_{n-1}\right] \geqslant \bar{I}(n-1)
$$

## Stopping Times

A random variable

$$
\tau: \Omega \rightarrow\{0,1,2, \ldots\} \cup\{\infty\}
$$

is a stopping time relative to a given filtration

$$
\left(J_{n}\right)_{n \geqslant 0}
$$

if for every $n \geqslant 0$ the event

$$
\{\omega: \tau(\omega)=n\} \in \Im_{n}
$$

this requirement is notationally equivalent to,

$$
\{t=n\} \in I_{n}
$$

Now since $\mathcal{J}_{k} \subset \mathcal{J}_{n}$ for $k<n$ it follows that,

$$
\{\tau=k\} \in \tilde{J}_{k}
$$

50

$$
\begin{aligned}
& \{\tau \leqslant n\}=\bigcup_{k \leqslant n}\{\tau=k\} \in \bigcup_{k \leqslant n} \mathcal{J}_{k}=\mathcal{J}_{n} \\
& \Rightarrow\{t \leqslant n\}=\bigcup_{k \leqslant n}\{\tau=k\} \in \mathcal{J}_{n}
\end{aligned}
$$

It follows that

$$
\{t>n\}=\{t \leq n\}^{c}
$$

Now

$$
\{\tau=n\}=\{t \leq n\} \mid\{t<n\} \in \mathcal{F}_{n}
$$

but

$$
\{t<n\}=\bigcup_{k<n}\{t=k\}
$$

80

$$
\{\tau=n\}=\{t \leqslant n\} / \bigcup_{k<n}\{\tau=k\}
$$

It is possible that $\tau=\infty$ so
to deal with the set,

$$
\{\tau=\infty\}
$$

introduce the set

$$
\mathcal{F}_{\infty}=\sigma\left(\bigcup_{n=0}^{n} \hat{\Xi}_{n}\right)
$$

since

$$
\{\tau=n\} \in \mathcal{F}_{n}
$$

for each finite $n$

$$
\{\tau=n\} \in \tilde{\partial}_{\infty}
$$

for every $n$. This then includes $t=\infty$. To see this consider the definition of the positive extended real number system,

$$
[0, \infty]=\mathbb{R}^{+} \cup\{\infty\}
$$

so

$$
\{\tau=\infty\}=\left[\bigcup_{n=0}^{\infty}\{\tau=n\}\right]^{c}
$$

From the defintion of a o-fied, since,

$$
\{\tau=n\} \in \mathcal{F}_{\alpha}
$$

it follows that

$$
\bigcup_{n=0}^{\infty}\{\tau=n\} \in \mathcal{F}_{\infty}
$$

and

$$
\{\tau=\infty\}=\left[\bigcup_{n=0}^{\infty}\{\tau=n\}\right]^{c} \in \mathcal{F}_{\alpha}
$$

## Example: Independent

Consider the case where $\tau$ is independent of $\exists_{n}$. This would be the case where $\tau$ is arbitrarly choosen without consideration of $\mathrm{J}_{n}$. For example if $\tau=10$ is choosen the the probability that $\tau=10$,

$$
P(\tau=10)=1
$$

## Example: First Artting Time

The first hitting time $\tau_{B}$ of a Borel set B CR by an adapted process $\bar{X}$ is defined by

$$
\tau_{B}(\omega)=\inf \{n: \bar{x}(n, \omega) \in B\}
$$

thus $\tau_{B}(\omega)$ is the first time $\bar{x}(\omega)$ is realized.
$\tau_{B}(\omega)$ is a stopping time since for every $n \geqslant 0$

$$
\left\{\tau_{B} \leqslant n\right\}=\bigcup_{k \leqslant n}\{X(k) \in B\} \in \Im_{n}
$$

on the other hard the last hitting time, defined by

$$
r_{B}(\omega)=\sup \{n: \bar{x}(n, \omega) \in B\}
$$

is not a stopping time since,

$$
\gamma_{B}(\omega)=n
$$

If and only if

$$
\omega \in\{\underline{x}(n, \omega) \in B\} \bigcap_{k>n}\{\bar{x}(k) \notin B\}
$$

The sets in the intersection will not in general be in $I_{n}$.

## Exercise

Let $\tau$ be a stopping time relative to the filtration In. Which of the random variables is also a stopping time

$$
\tau+1, \tau-1, \tau^{2}
$$

Solutions
Since $\tau$ is a stopping time,

$$
\{\omega: \tau(\omega)=n\} \in \mathcal{J}_{n}
$$

where $n \geqslant 0$
$\tau+1$ is not a stopping time since

$$
\{\omega: \tau(\omega)+1=n\} \notin \tilde{J}_{n}
$$

because

$$
\xi \omega: \tau(\omega)=n-1\} \in J_{n-1}
$$

similarly, $\tau^{2}$ is not a stopping time

$$
\left\{\omega: \tau^{2}(\omega)=n\right\} \notin \mathcal{J}_{n}
$$

since

$$
\{\omega: \tau(\omega)=\sqrt{n}\} \in \tilde{Э}_{\sqrt{n}}
$$

Finally $\tau-1$ is a stopping time since

$$
\{\omega: \tau(\omega)-1=n\} \in \mathcal{F}_{n}
$$

because,

$$
\{\omega: \tau(\omega)=n+1\} \in \mathcal{F}_{n+1}
$$

and

$$
\Im_{n} \subset \mathcal{F}_{n+1}
$$

Given two stopping times $\tau$ and $r$, define the notation

$$
\begin{aligned}
& \tau \vee r=\max \{\tau, r\} \\
& \tau \wedge r=\min \{\tau, v\}
\end{aligned}
$$

## Theorem

If $\tau$ and $\gamma$ are stopping times relative to the filtration $I_{n}$ the $\tau v r$ is also a stopping time relative to $I_{n}$.

## Proof

For the maximimum to be $m \leq n$, so

$$
\tau \vee r=m
$$

it follows that one of the conditions must hold

$$
\begin{array}{ll}
\tau=m, & r \leq m \\
\tau \leq m, & r=m
\end{array}
$$

it follows that

$$
\begin{aligned}
\{\tau \vee r=m\}= & \{\tau=m, r \leq m\} U \\
& \{\tau \leq m, r=m\}
\end{aligned}
$$

both the left and right hard sides are contained in $f_{n}$.
Thus $\tau v r=m$ is a stopping time.
Similarly for $\tau \wedge \gamma=m$

$$
\begin{aligned}
\{\tau \wedge r=m\}= & \{\tau=m, r \geqslant m\} \cup \\
& \{\tau \geqslant m, r=m\}
\end{aligned}
$$

both sides are contained
in $\mathcal{F}_{n}$ thus $\tau \wedge r$ is a stopping time.

## Theorem

Let $\tau_{k}, k=1,2,3, \ldots$ be a convergent sequence of stopping times then

$$
\tau=\lim _{k \rightarrow \infty} \tau_{k}
$$

is a stopping time.

## Stopping Times Review

To furthure develop an intuition of stopping time, here some basic examples will be worked in detail.

Consider an American put optron withe the following binomial payolf,

$$
\begin{array}{rrrrr}
4.51=1.23= & 0.20 & 0.00 & 0.00 & 0.00 \\
10.00 & 2.94 \equiv & 0.52 & 0.00 & 0.00 \\
& 19.00 & 6.94= & 1.37 & 0.00 \\
& 27.10 & 3.89 & 16.17 & 24.55 \\
& & 34.39 & 40.95
\end{array}
$$

Three exercise prices are indicated by the green highligt. These exercise prices define 3 stopping times.

$$
\frac{\text { Peyoff }}{10.00} \quad \frac{\omega}{D}
$$

$$
\begin{array}{ll}
16.17 & \text { UDDD } \\
3.59 & \text { ULDDD, UDLOD } \\
& \text { UDDGD } \\
0.00 & \text { Otherwise }
\end{array}
$$

There are three stopping times

$$
\tau= \begin{cases}1 & \omega=D \in B_{D} \\ 4 & \omega=\text { UDDD } \in \text { BUDDD } \\ \sigma & \text { otherwise }\end{cases}
$$

This leads to the definition,

## Definition

A random variable,

$$
\tau: \Omega \rightarrow\{1,2,3, \ldots, N\}
$$

is a stopping time if

$$
\{\omega: \tau(\omega) \leqslant n\} \in \widetilde{J}_{n}
$$

for all $n$.

Once again consider the American put option payoff and consider the case $\omega=$ udom. This outcome produces the sequence of payoffs
$P(n, \omega)=(4.51,1.23,2.94,6.94,16.17,3.59)$
for this case the choosen strategy
is to exercise at $n=4$. If this payoff carries over the future steps then
$P_{\tau}(n, \omega)=(4.51,1.23,2.94,6.94,16.17,16.17)$
for this $\omega, \tau(\omega)=4$ so the
sequence quits changing at $n=4$ and is constant for $n \geqslant 4$.
This motioates the following definition.

Definition: Stapped Process
For any sequence of random
variables X(n) and any stopping time $\tau$ the stopped process $\bar{X}_{\tau}(n)$ is defined by,

$$
\begin{aligned}
\bar{X}_{\tau}(n) & =\bar{X}(\min \{\tau, n\}) \\
& =\left\{\begin{array}{l}
\bar{X}(n, \omega) \quad \tau(\omega)<n \\
\bar{X}(\tau(\omega), \omega) \quad \tau(\omega) \geqslant n
\end{array}\right.
\end{aligned}
$$

## Stopped Processes

If the stopping time,

$$
\tau: \Omega \rightarrow N \cup\{\infty\}
$$

where $\mathbb{N}$ are the natural numbers $\{1,2,3, \ldots\}$, is P-a.s. Pinite, namely.

$$
P(\{\tau=\infty\})=0
$$

that is the probabilitiy of $\tau=\infty$ is zero, the following function can be considered

$$
X(\tau): \Omega \rightarrow \mathbb{R}
$$

with

$$
\omega \rightarrow \bar{\Delta}(\tau(\omega), \omega)
$$

for $\{\tau<\infty\}$ and zero for $\{\tau=\infty\}$ then

$$
\bar{X}(\tau)=\sum_{m \geqslant 0} \bar{X}(m) \mathbb{1}_{\{\tau=m\}}
$$

since the sets $\{\tau=m\}$ are parwise disjoint For each $m \geqslant 0, \quad \bar{X}(m) \nmid 1 \varepsilon \tau=m\}$ is
$\tilde{J}_{m}$ measurable and $\tilde{J}_{m} \in \tilde{J}_{\infty}=\tilde{J}$
To motroate discussion consider the following examples.
Recall that the value processes for a portfolio containing a risky asset and a risk free investment is given by
$U(n)=x(n) S(n)+y(n)(1+R)^{n}$
where $s(n)$ is the price of the risky asset, $R$ the risk-free interest rate and $X(n)$ and $y(n)$ the amount of the risky and risk-free investments respectively.
A stopped process is used to determine the time to

Iiquidate the investment at price M. It follows that the time the position will be liqudated is given by

$$
\tau=\min \{n: U(n) \geqslant M\}
$$

The investment is said to by frozen at $U_{\tau}(n)$ since

$$
U_{\tau}(n)= \begin{cases}U(n) & n<\tau \\ U(\tau) & n \geqslant \tau\end{cases}
$$

## Definition

For an adapted process I and a stopping time $\tau$ the stopped process denoted by

$$
\underline{Z}_{\tau}=\left(\underline{X}_{\tau}(n)\right)_{n \geqslant 0}
$$

and defined by

$$
\bar{X}_{\tau}(n, \omega)=\bar{X}(n \wedge \tau(\omega), \omega)
$$

Note that for each $\omega, \bar{X}_{\tau}$ truncates, freezes, the path,

$$
\{\bar{X}(n, \omega): n \geqslant 0\}
$$

at the level $\bar{X}(\tau(\omega))$.

## Theorem

if $\Im_{n}$ is the fittration generated by the adapted proccess X ( $n$ ), an adapted processes is $I_{n}$. measurable for each $n$, the process $\bar{X}_{\tau}(\omega)$ is $\tilde{I}_{n}$ adapted.

## Proof

For $\omega \in \Omega$ with $\tau(\omega)<\infty$ there are two possibility

1. $\tau(\omega)=m<n$, so

$$
\begin{aligned}
\bar{X}_{\tau}(n, \omega) & =\bar{X}(m, \omega) \\
& =\underline{X}(\tau(\omega), \omega)
\end{aligned}
$$

2. $\tau(\omega)=m \geqslant n$, so

$$
\underline{X}_{\tau}(n, \omega)=\underline{X}(n, \omega)
$$

The sets,

$$
\{\tau=m\}=\{\omega: \tau(\omega)=m\}
$$

are parwise disjoint Now

$$
\bar{X}_{\tau}(n)= \begin{cases}\bar{X}(n) & n<\tau \\ \bar{X}(m) & n \geqslant \tau=m\end{cases}
$$

This can be written more compactly as,

$$
\bar{X}_{\tau}(n)=\sum_{m<n} \bar{X}(m) \mathbb{1}_{\{\tau=m\}}+\bar{X}(n) \mathbb{1}_{\{\tau>n\}}
$$

Each term on the right hand side is $\mathcal{F}_{n}$-measurable since $\{\tau<n\}$ is $\mathfrak{J}_{n}$ - measureable and

$$
\{\tau \geqslant n\}=\Omega /\{\tau<n\} \in \mathcal{J}_{n}
$$

from the definition of a ofield which is $\mathfrak{F}_{n}$-measureable.

## Theorem

Let $M$ be a marlingale. If $\tau$ is a stopping time, then the stoped process $M_{\tau}$ is also a martingale.

## Proof

Recall trat
$M_{\tau}(n)=\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}}+M(n) \mathbb{1}_{\{\tau \geqslant n\}}$
Previously it was shown that $M_{\tau}(n)$ is $J_{n}$-adapted and since the sum is fonite $M_{\tau}(n)$ is finite. Now taking expectation with respect to $\exists_{n-1}$ gives

$$
E\left[M_{\tau(n)} \mid \widetilde{\Im}_{n-1}\right]=E\left[\sum_{m<n} M(m) \mathbb{1}_{\varepsilon \tau=m \xi}\right.
$$

$$
\begin{aligned}
+ & \left.M(n) \mathbb{1}_{\{\tau \geqslant n\}} \mid \mathcal{F}_{n-1}\right] \\
= & E\left[\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}} \mid \mathcal{F}_{n-1}\right] \\
& +E\left[M(n) \mathbb{1}_{\{\tau \geqslant n\}} \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

The first term is $\mathcal{F}_{n-1}$-measureable since the sum is over $m<n$,

$$
\begin{gathered}
E\left[\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}} \mid \mathcal{F}_{n-1}\right] \\
=\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}}
\end{gathered}
$$

Now for the second term

$$
\underline{11}_{\{\tau \geqslant n\}}=1-\underline{11}_{\{\tau<n\}}
$$

50

$$
E\left[M(n) \mathbb{1}_{\{\tau \geqslant n\}} \mid \mathcal{F}_{n-1}\right]
$$

$$
\begin{aligned}
& =E\left[M(n)\left(1-\mathbb{1}_{\{\tau<n\}}\right) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[M(n) \mid \mathcal{F}_{n-1}\right]-E\left[\mathbb{1}_{\{\tau<n\}} M(n) \mid \mathcal{F}_{n-1}\right\}
\end{aligned}
$$

Now $M(n)$ is a martingale so

$$
E\left[M(n) \mid \mathcal{F}_{n-1}\right]=M(n-1)
$$

and since $11\{\tau<n\}$ is $\mathcal{F}_{n-1}$ measure able, using the taking out what is known property of conditional expectation on the second term gives

$$
\begin{aligned}
E\left[\mathbb{1}_{\{ }\{<n\} M(n) \mid \mathcal{F}_{n-1}\right\} \\
=\mathbb{1}_{\{ }\{<n\} E\left[M(n) \mid \mathcal{F}_{n-1}\right] \\
=\mathbb{1}\{\tau<n\} M(n-1)
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
E[M(n) & \left.\mathbb{1}\{\tau \geqslant n\} \mid \mathcal{F}_{n-1}\right] \\
& =M(n-1)-\mathbb{1}_{\{\tau<n\}} M(n-1) \\
& =M(n-1)(1-\mathbb{1}\{\tau<n\}) \\
& =\mathbb{1}\{\tau \geqslant n\} M(n-1)
\end{aligned}
$$

Bringing everything together
gives

$$
\begin{aligned}
E\left[M_{\tau(n)} \mid \mathcal{F}_{n-1}\right] & =\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}} \\
& +\mathbb{1}_{\{\tau \geqslant n\}} M(n-1)
\end{aligned}
$$

Now for the first term

$$
\begin{array}{rl}
\sum_{m<n} & M(m) \mathbb{1}\{\tau=m\} \\
& =\sum_{m<n-1} M(m) \mathbb{1}\{\tau=m\}+M(n-1) \mathbb{1}_{\{\tau=n-1\}}
\end{array}
$$

so

$$
\begin{array}{r}
E\left[M_{\tau(n)} \mid \tilde{z}_{n-1}\right]=\sum_{m<n-1} M(m) \mathbb{1}\{\tau=m\}+ \\
M(n-1) \mathbb{1}_{\{\tau=n-1\}}+\mathbb{1}\{\tau \geq n\} M(n-1)
\end{array}
$$

But

$$
\begin{aligned}
& M(n-1) \mathbb{1}_{\{\tau=n-1\}}+\mathbb{1}_{\{\tau \geqslant n\}} M(n-1) \\
= & M(n-1)\left(\mathbb{1}_{\{\tau=n-1\}}+\mathbb{1}_{\{\tau \geqslant n\}}\right) \\
= & M(n-1)(\mathbb{1}\{\tau=n-1\}+\mathbb{1}\{\tau=n\} \\
& +\mathbb{1}\{\tau=n+1\}+\mathbb{1}\{\tau=n+2\}+\cdots \\
& \mathbb{1}\{\tau=n+m\} \\
= & \mathbb{1}\{\tau \geqslant n-1\} M(n-1)
\end{aligned}
$$

Thus the desired result is obtained

$$
\begin{aligned}
E\left[M_{\tau(n)} \mid \mathcal{F}_{n-1}\right] & =\sum_{m<n-1} M(m) \mathbb{1}_{\{\tau=m\}}+ \\
\mathbb{I}_{\{\tau \geqslant n-1\}} M(n-1) & \\
& =M(n-1)
\end{aligned}
$$

$$
\Rightarrow E\left[M_{\tau(n)} \mid \widetilde{J}_{n-1}\right]=M(n-1)
$$

## Theorem

For a martingale, the expectation is preserved under stopping. That is in general for a martingale $M$, a stopping time $\tau$ and $n \geqslant 0$

$$
E\left[\mu_{\tau}(n)\right]=E[M(0)]=E[M(n)]
$$

## Proof

Proviously it was shown that if $M(n)$ is a martingale $M_{\tau}(n)$ is a martingale, so

$$
E\left[\mu_{\tau}(n) \mid \mathcal{F}_{n-1}\right]=\mu_{\tau}(n-1)
$$

Taking expectation gives

$$
E\left[E\left[M_{\tau}(n) \mid \tilde{\theta}_{n-1}\right]\right]=E\left[M_{\tau}(n-1)\right]
$$

$$
\Rightarrow E\left[\mu_{\tau}(n)\right]=E\left[\mu_{\tau}(n-1)\right]
$$

It follows that,

$$
\begin{aligned}
E\left[\mu_{\tau}(n)\right] & =E\left[\mu_{\tau}(n-1)\right] \\
& =E\left[\mu_{\tau}(n-2)\right] \\
& \vdots E\left[\mu_{\tau}(1)\right] \\
& =E\left[\mu_{\tau}(0)\right]
\end{aligned}
$$

Thus

$$
E\left[\mu_{\tau}(n)\right]=E\left[\mu_{\tau}(0)\right]
$$

Recall that
$M_{\tau}(n)=\sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}}+M(n) \mathbb{1}_{\{\tau \geqslant n\}}$
Now
$M_{\tau}(0)=\sum_{m<0} M(m) \mathbb{1}\{\tau=m\}+M(0) \mathbb{1}\{\tau \geqslant 0\}$
The first term is zero and
by definition $\tau \geqslant 0$ so

$$
\mathbb{1}_{\{\tau \geqslant 0\}}=1
$$

It follows that

$$
M_{\tau}(0)=M(0)
$$

and since $\mu(n)$ is a martingale

$$
E[M(n)]=E[M(0)]=E\left[M_{\tau}(0)\right]
$$

and the desired result is obtained

$$
E\left[M_{\tau}(n)\right]=E[M(0)]=E[M(n)]
$$

## Theorem

If $M(n)$ is a submartingale/ supermartingale then the stoped process $M_{\tau}(n)$ is a submartingale/ supermartingale.

## Proof

First consider a submartingale,

$$
E\left[M(n) \mid J_{n-1}\right] \geqslant M(n-1)
$$

and consider the martingale $\bar{X}(n)$ and stopping time $\tau$. Previously it was shown that the stopped process is a martingale,

$$
E\left[\bar{X}_{\tau}(n) \mid \mathcal{F}_{n-1}\right]=\bar{X}_{\tau}(n-1)
$$

Also, recall that the Doob decomposition for a submaringale is given by,

$$
M(n)=M(0)+\bar{X}(n)+A(n)
$$

where $A(n)$ is a pridictable increasing process with

$$
\Phi(0)=A(0)=0
$$

$$
A(n)-A(n-1)=E\left[M(n)-M(n-1) \mid \mathcal{F}_{n-1}\right]
$$

Now, the stoped submartingale process is given by

$$
\begin{aligned}
M_{\tau}(n)= & \sum_{m<n} M(m) \mathbb{1}_{\{\tau=m\}}+M(n) \mathbb{1}_{\{\tau \geqslant n\}} \\
= & \sum_{m<n}[M(0)+\underline{\bar{X}}(m)+A(m)] \mathbb{1}_{\{\tau=m\}} \\
& +[M(0)+\bar{X}(n)+A(n)] \mathbb{1}_{\{\tau \geqslant n\}}
\end{aligned}
$$

Taking expectation with respect to $\Im_{n-1}$
$E\left[M_{\tau}(n) \mid F_{n-1}\right]$

$$
\begin{aligned}
= & \sum_{m<n} E\left[(M(0)+\bar{X}(m)+A(m)) \mathbb{1}_{\{\tau=m\}} \mid \mathcal{F}_{n-1}\right] \\
& +E\left[(M(0)+\bar{X}(n)+A(n)) \mathbb{1}_{\{\tau \geqslant n\}} \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

Now for the first term,

$$
m<n \Rightarrow m \leqslant n-1
$$

so $\bar{X}(m), A(m)$ and $\mathbb{1}\{\tau=m\}$ are $F_{n-1}$-measurable

$$
\begin{aligned}
& E\left[M(0)+\bar{X}(m)+A(m) \mathbb{1}_{\left.\{\tau=m\} \mid \mathcal{F}_{n-1}\right]}\right. \\
& \quad=(M(0)+\bar{X}(m)+A(m)) \mathbb{1}_{\{\tau=m\}}
\end{aligned}
$$

and for the second term, $\mathbb{1}_{\{\tau \geqslant n\}}$ is $\mathcal{F}_{n-1}$ measureable since,

$$
\left.\mathbb{1}_{\varepsilon} \varepsilon \tau \geqslant n\right\}=1-\mathbb{1}\{\tau<n\}
$$

it follows that,

$$
\begin{aligned}
E[ & \left.(M(0)+\bar{X}(n)+A(n)) \mathbb{1}_{\{\tau \geq n\}} \mid \mathcal{F}_{n-1}\right] \\
= & E\left[(M(0)+\bar{X}(n)+A(n))\left(1-\mathbb{1}_{\{ }\{\tau(n\}) \mid \mathcal{F}_{n-1}\right]\right. \\
= & E\left[M(0)+\bar{X}(n)+A(n) \mid \mathcal{F}_{n-1}\right] \\
& -E\left[(M(0)+\bar{X}(n)+A(n)) \mathbb{1}_{\{ }\left\{\tau(n\} \mid \mathcal{F}_{n-1}\right]\right.
\end{aligned}
$$

$$
\begin{aligned}
& =E\left[M(0)+\bar{X}(n)+A(n) \mid \mathcal{F}_{n-1}\right] \\
& -\mathbb{1}_{\{\tau<n\}} E\left[M(0)+\bar{X}(n)+A(n) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[M(0)+\bar{X}(n)+A(n) \mid \mathcal{F}_{n-1}\right]\left(1-\mathbb{1}_{\{\tau<n\}}\right) \\
& =E\left[M(0)+\bar{X}(n)+A(n) \mid \mathcal{F}_{n-1}\right] \mathbb{1}_{\{\tau \geqslant n\}} \\
& =\left[M(0)+E\left[\bar{X}(n) \mid \mathcal{F}_{n-1}\right]+E\left[A(n) \mid \mathcal{F}_{n-1}\right]\right] \mathbb{1}_{1}\{\tau \geqslant n\}
\end{aligned}
$$

but 又(n) is a martingale with respect to $\mathcal{F}_{n-1}$ and $A(n)$ is predicable with respect to $\mathfrak{F}_{n-1}$, so

$$
\begin{aligned}
& E\left[\bar{X}(n) \mid \tilde{J}_{n-1}\right]=\bar{X}(n-1) \\
& E\left[A(n) \mid \tilde{J}_{n-1}\right]=A(n)
\end{aligned}
$$

and firally for the second term

$$
\begin{aligned}
& E\left[(M(0)+\bar{X}(n)+A(n)) \mathbb{1}^{1}\{\tau \geqslant n\} \mid \mathcal{F}_{n-1}\right] \\
& \quad=[M(0)+\bar{X}(n-1)+A(n)] \text { 价 }\{\tau \geqslant n\}
\end{aligned}
$$

Bringing evenything together gives,

$$
\begin{aligned}
E & {\left[M_{\tau}(n) \mid F_{n-1}\right] } \\
= & \sum_{m<n}(M(0)+\bar{X}(m)+A(m)) \underline{1}\{\tau=m\} \\
& +[M(0)+\underline{X}(n-1)+A(n)] \underline{1}\{\tau \geq n\} \\
=\sum_{m<n-1} & (M(0)+\underline{X}(m)+A(m)) \underline{1}\{\tau=m\} \\
& +(M(0)+\underline{X}(n-1)+A(n-1)) \underline{1}\{\tau=n-1\} \\
& +[M(0)+\underline{X}(n-1)+A(n)] \underline{1}\{\tau \geq n\}
\end{aligned}
$$

Now $A(n)$ is increasing so $A(n) \geqslant A(n-1)$ it follows that

$$
\begin{aligned}
& E\left[M_{\tau}(n) \mid \mathcal{F}_{n-1}\right] \\
& =\sum_{m<n-1}(M(0)+\underline{X}(m)+A(m)) \mathbb{1}_{\{\tau=m\}}
\end{aligned}
$$

$$
\begin{aligned}
+ & (M(0)+\mathbb{X}(n-1)+A(n-1)) \mathbb{1}\{\tau=n-1\} \\
+ & {[M(0)+\mathbb{X}(n-1)+A(n)] \mathbb{1}\{\tau \geqslant n\} } \\
\geqslant & \sum_{m<n-1}(M(0)+\mathbb{X}(m)+A(m)) \mathbb{1}\{\tau=m\} \\
+ & (M(0)+\mathbb{X}(n-1)+A(n-1)) \mathbb{1}\{\tau=n-1\} \\
+ & {[M(0)+\mathbb{X}(n-1)+A(n-1)] \mathbb{1}\{\tau \geqslant n\} } \\
= & \sum_{m<n-1}(M(0)+\mathbb{X}(m)+A(m)) \mathbb{1}\{\tau=m\} \\
& +[M(0)+\mathbb{X}(n-1)+A(n-1)] \mathbb{1}\{\tau \geqslant n-1\} \\
= & \sum_{m<n-1} M(m) \mathbb{1}\{\tau=m\}+M(n-1) \mathbb{1}\{\tau \geqslant n-1\} \\
= & M \tau(n-1)
\end{aligned}
$$

and the desired result is dotained

$$
E\left[M_{\tau}(n) \mid \mathcal{J}_{n-1}\right] \geqslant M_{\tau}(n-1)
$$

and $M_{\tau}(n)$ is a submartingale. The argumed for a supermartingale is similar.

## Optonal sampling for Bownded stopping Times

Here the properties of the random variable

$$
\bar{X}(\tau)(\omega)=\bar{X}(\tau(\omega), \omega)
$$

where $\tau(\omega)$ is a stopping time are discussed. If $B$ is any Borel set, $B \subset \mathbb{R}$, let

$$
\begin{aligned}
& \{\bar{X}(m) \in B\}=\{\omega: \bar{X}(\tau(\omega)=m, \omega) \in B\} \\
& \{\tau=m\}=\{\omega: \tau(\omega)=m\}
\end{aligned}
$$

It follows that the events satisfying both conditions are given by

$$
\{\bar{X}(m) \in B\} \cap\{\tau=m\}
$$

Define the random variable $\bar{X}(\tau)$ by

$$
\{\bar{X}(\tau) \in B\}=\bigcup_{m \geqslant 0}\{\bar{X}(m) \in B\} \cap\{\tau=m\}
$$

## Definition

The $\sigma$-field of events known at time $\tau$ is defined by
$\mathcal{F}_{\tau}=\left\{A \in \mathcal{F}: A \cap\{\tau=m\} \in \mathcal{F}_{m} \forall m \in \mathbb{N}\right\}$
This fied clearly contains all events $A \in \mathcal{F}$ that intersect $\omega$ ith the cuent $\{\omega: \tau(\omega)=m\}$.

Properties of $\mathcal{J}_{\tau}$

1. For stopping times $Y$ and $\tau$ where $\tau \leqslant r \quad \mathcal{F}_{\tau} \subset \mathcal{F}_{r}$
2. From (1) it follows that

$$
\exists_{\tau \wedge \gamma} \subset \mathcal{F}_{\tau} \subset \mathcal{J}_{\tau \vee \gamma}
$$

3. $\tau$ is $\mathcal{F}_{\tau}$-measureable

## Theorem

Let $\tau$ be a finite stopping time and $\bar{X}(n)$ be a processes adapted to $I_{n}$. Then $\bar{X}(\tau)$ is
$\mathcal{F}_{\tau}$-measureable.

## Proof

To show that $\bar{X}(\tau)$ is $F_{\tau}$-measureable it must be shown that for eveny $s \in \mathbb{R}$ and $k \geqslant 0$

$$
u=\{X(\tau)<s\} \cap\{\tau \leqslant k\} \in \mathcal{F}_{k}
$$

Now

$$
u=\bigcup_{n=0}^{k}\{\bar{X}(n)<s\} \cap\{\tau=n\}
$$

For each $n \leqslant k$

$$
\{X(n)<s\} \cap\{\tau=n\} \in \mathcal{F}_{n}<\mathcal{F}_{k}
$$

and the desired result follows.

## Theorem

If $M$ is a martingale and $\tau \leqslant r$ are bounder stopping times then

$$
\mu(\tau)=E\left[\mu(\gamma) \mid \mathcal{F}_{\tau}\right]
$$

## Proof

Taking expectations of the expression to be proven gives

$$
E[M(\tau)]=E[M(\gamma)]
$$

Let $A \in \mathcal{F}_{\tau}$ then the above expression becomes

$$
\begin{aligned}
& \int_{A} M(\tau) d P=E\left[\mathbb{1}_{A} M(\tau)\right] \\
& \int_{A} M(r) d P=E\left[\mathbb{1}_{A} M(r)\right]
\end{aligned}
$$

Thus it must be shown that

$$
E\left[\mathbb{1}_{A}(M(r)-M(\tau))\right]=0
$$

Now

$$
\begin{aligned}
& M(\gamma)-M(\tau)=M(\gamma(\omega), \omega)-M(\tau(\omega), \omega) \\
& =\sum_{k=\tau(\omega)+1}^{\gamma(\omega)} M(k, \omega)-M(k-1, \omega)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E\left[\mathbb{1}_{A}(M(r)-M(\tau))\right] \\
& =\sum_{k=\tau(\omega)+1}^{r(\omega)} \mathbb{1}_{A}(\omega)[M(k, \omega)-M(k-l, \omega)] \\
& \left.=\sum_{k=0}^{r(\omega)} \mathbb{1}_{A}(\omega) \mathbb{1}_{\{ } \tilde{\tau}(\omega)<k\right\}[M(k, \omega)- \\
& M(k-l, \omega)]
\end{aligned}
$$

Recall that if $H$ is a pridictable
process and $M(k)$ is a martingale then $\mathrm{Z}(0)=0$

$$
\underline{X}(n)=\sum_{j=1}^{n} H(j)[M(j)-M(j-1)]
$$

is a martingale.
Thus if t can be shown that

$$
H(k)=\frac{1}{1}_{A}(\omega) \mathbb{1}\{\tau(\omega)<k\}
$$

is predictable then

$$
\bar{X}=M(r)-M(\tau)
$$

is a martingale with $\bar{x}(0)=0$ so that

$$
E\left[\mathbb{1}_{A}(M(r)-M(\tau))\right]=0
$$

prooing the theoron. $H(k)$ is predicatable if

$$
A \cap\{\tau<k\} \in \mathcal{F}_{k-1}
$$

but

$$
\{\tau<k\}=\bigcup_{m=0}^{k-1}\{\tau=m\}
$$

Thus since $A \in \mathcal{F}_{\tau}$ from the definition of $\mathcal{F}_{\tau}$,
$\mathcal{F}_{\tau}=\left\{A \in \mathcal{F}: A \cap\{\tau=m\} \in \mathcal{F}_{m} \forall m \in \mathbb{N}\right\}$
it follows that for each $m$

$$
A \cap\{\tau=m\} \in \mathcal{F}_{m}
$$

50

$$
A \cap\{\tau<k\}=\bigcup_{m=0}^{k-1} A \cap\{\tau=m\} \in \mathcal{F}_{k-1}
$$

so it is predictable.
Thus

$$
M(\tau)=E\left[M(r) \mid F_{\tau}\right]
$$

This is called the optional
sampling theorem. It states that the best prediction of the value of a stopped process is its current oalue.

## Doob's Inequalities and Martingale Convergence

## Theorem Doob's Maximal Inequality

If $M(n)$ is a nonegative submartngle, then for each $n \in N, \lambda>0$ and

$$
\begin{aligned}
A= & \left.\max _{k \leqslant n} \mu(k) \geqslant \lambda\right\} \\
P\left(\max _{k \leqslant n} \mu(k) \geqslant k\right) & \leqslant \frac{1}{\lambda} \int_{A} \mu(n) d P \\
& \leqslant \frac{1}{\lambda} E(\mu(n))
\end{aligned}
$$

## Proof

Now,

$$
A=\left\{\max _{k \leqslant n} \mu(k) \geqslant \lambda\right\}
$$

let $A_{k}$ consist of $\omega \in \Omega$ where
$M(K) \geqslant \lambda$ for the first time. For this to be the case $M(j)<\lambda$ for $j<k$ and $M(k) \geqslant \lambda$. This event is given by,

$$
A_{k}=\bigcap_{j=0}^{k-1}[\{M(j)<\lambda\} \cap\{M(k) \geqslant \lambda\}]
$$

Then

$$
\begin{aligned}
A & =\bigcup_{k=0} A_{k} \\
A_{0} & =\{\mu(0) \geqslant \lambda\}
\end{aligned}
$$

Since $M(k)$ is a martingale it is adapted so $A_{k} \in \mathcal{J}_{k}$. Since

$$
M(k) \geqslant \lambda \text { for } \omega \in A_{k}
$$

it follows that

$$
\lambda P\left(A_{k}\right) \leqslant \int_{A_{k}} M(k) d P
$$

since $M(n)$ is a submartingale for $k<n$

$$
E[M(n)] \geqslant E[M(k)]
$$

50

$$
\begin{aligned}
\lambda P\left(A_{k}\right) & \leqslant \int_{A_{k}} M(k) d P \\
& \leqslant \int_{A_{k}} M(n) d P
\end{aligned}
$$

By constructuation

$$
A_{i} \cap A_{j}=\varnothing \quad i \neq j
$$

since for $i<j \quad A_{i}$ will contain events where $M(i) \geqslant \lambda$ while $A_{j}$ will not contain these events it follows that

$$
P(A)=\sum_{k=0}^{n} P\left(A_{k}\right)
$$

and

$$
\int_{A} M(n) d P=\sum_{k=0}^{n} \int_{A_{k}} M(n) d P
$$

the desired result follows

$$
\begin{aligned}
\lambda P\left(\max _{k \leqslant n} M(k) \geqslant \lambda\right) & \leqslant \int_{A} M(n) d P \\
& =E[M(n)] \\
\Rightarrow P\left(\max _{k \leqslant n} M(k) \geqslant \lambda\right) & \leqslant \frac{1}{\lambda} E[M(n)]
\end{aligned}
$$

Jensen's nequality can be used to improve this estimate,

$$
P\left(\max _{k \leqslant n} \mu(k) \geqslant \lambda\right) \leqslant \frac{1}{\lambda P} E[\mu P(n)]
$$

Theorem: Doob's $L^{2}$-Inequality Let $M(n)$ be a non-negatue submartingale with,

$$
E\left[M^{2}(n)\right]<\infty
$$

for every $n \geq 0$, Then

$$
E\left[\max _{k \leqslant n} M(k)\right]^{2} \leqslant 4 E\left[M^{2}(n)\right]
$$

## Theorem

Let $M$ be an $L^{2}$-bounded martingale. That is for some $c \quad E\left[M^{2}(n)\right] \leqslant c$ for all $n \geqslant 0$. Then there exists a random variable II with $E\left[I^{2}\right] \leqslant c$ such that

1. $M(n)$ converges almost swrely to I

$$
P\left(\lim _{n \rightarrow \infty} \mu(n)=\Sigma\right)=1
$$

2. $M(n)$ converges to $I$ in $l^{2}$-norm,

$$
\lim _{n \rightarrow \infty} E\left[(M(n)-Y)^{2}\right]=0
$$

3. For each $n \geqslant 0$

$$
M(n)=E\left[I \mid \tilde{J}_{n}\right]
$$

This is the first of the

## martingate convergence theorems

This theorem says that if the $L^{2}$-norm of the martingale $M(n)$

$$
E\left[M^{2}(n)\right]<C
$$

for any real number $c \geqslant 0$ and for every $n$. Then

$$
\bar{Y}=\lim _{n \rightarrow \infty} M(n)
$$

almost scirely (with probability 1) and the $L^{2}$-norm converges

$$
\lim _{n \rightarrow \infty} E\left[(\mu(n)-\bar{I})^{2}\right]=0
$$

And finally that

$$
E\left[I \mid \mathcal{F}_{n}\right]=\mu(n)
$$

Intuitatively this makes sense since in general for $m>n$

$$
E\left[M(m) \mid \mathcal{F}_{n}\right]=M(n)
$$

and

$$
\bar{I}=\mu(\infty)
$$

This theorem allows the original optional sampling theorem, which assums $\tau<V$ are both bounded, to the wrownded case.

## Theorem: Optional Sampling

Let $M(n)$ be and $c^{2}$-bownded martingale with

$$
E\left[I \mid \mathcal{F}_{n}\right]=M(n)
$$

for every $n \geq 0$ and II squareintegrable. If $\tau \leqslant V$ are stapping times then

$$
E\left[M(r) \mid \mathcal{F}_{\tau}\right]=M(\tau)
$$

## Markov Process

Consider the symmetric random walk

$$
2(n+1)=2(n)+L(n+1)
$$

where $L(n+1)$ are independent random variables with,

$$
E[L(n+1)]=0
$$

$Z(n)$ is a martingale

$$
E\left[2(n+1) \mid \mathcal{F}_{n}^{2}\right]=2(n)
$$

Consider the 6-fields

$$
\begin{aligned}
& \mathcal{F}_{n}^{2}=\sigma[2(0), 2(1), \ldots, 2(n)] \\
& \mathcal{F}_{n}^{2}=\sigma[L(1), L(2), \ldots, L(n)] \\
& \mathcal{F}_{2(n)}=\sigma[2(n)]
\end{aligned}
$$

The wrderlying event space for $\mathcal{F}_{n}^{2}$ and $\mathcal{F}_{n}^{L}$ are clearly the same

$$
\mathcal{F}_{n}^{2}=\mathcal{F}_{n}^{2}
$$

This is also true for,

$$
\mathcal{F}_{2(n)}=\mathcal{F}_{n}^{2}=\mathcal{F}_{n}^{2}
$$

It follows that

$$
\begin{aligned}
& E\left[z(n+1) \mid \mathcal{J}_{n}^{2}\right]=z(n) \\
& E\left[z(n+1) \mid \mathcal{J}_{z(n)}\right]=z(n)
\end{aligned}
$$

So

$$
E\left[z(n+1) \mid \mathcal{F}_{n}^{2}\right]=E\left[z(n+1) \mid \mathcal{F}_{2(n)}\right]
$$

## Definition

A stochastic process $(\bar{X}(n))_{n \geqslant 0}$ is said to have the Markou property if for all bounded
functions $f: \mathbb{R} \rightarrow \mathbb{R}$

$$
\begin{aligned}
& E\left[f(\underline{\bar{X}}(n+1)) \mid \tilde{J}_{n}^{\bar{X}}\right] \\
& =E\left[f(\underline{\bar{X}}(n+1)) \mid \tilde{J}_{\bar{X}(n)}\right]
\end{aligned}
$$

where

$$
\begin{aligned}
& \mathcal{F}_{n}^{2}=\sigma[z(0), z(1), \ldots, z(n)] \\
& \mathcal{F}_{z(n)}=\sigma[z(n)]
\end{aligned}
$$

It is also said that $\bar{X}(n)$ is a Markou process.

Definition : Transition Probability The family of probability measures,

$$
\left\{\mu_{n}(x, B)\right\}
$$

where $x \in \mathbb{R}$ and $n \geqslant 0$ defined on Borel sets, measureable as functions of $x$ for each $B$,
such that

$$
\mu_{n}(\bar{X}(n), B)=P\left(\bar{X}(n+1) \in B \mid \mathcal{F}_{X(n)}\right)
$$

but

$$
\begin{gathered}
P\left(\bar{X}(n+1) \in B \mid \mathcal{F}_{\bar{X}(n)}\right) \\
E\left[\mathbb{1}_{B} \bar{X}(n+1) \mid \mathcal{F}_{\bar{X}(n)}\right] \\
\text { so } \\
\mu_{n}(\bar{X}(n), B)=E\left[\mathbb{1}_{B} \bar{X}(n+1) \mid \mathcal{F}_{\bar{X}(n)}\right]
\end{gathered}
$$

A Markou process is said to be homogenedus if the transition probability does not explicitly depend on $n$., so

$$
\mu(\bar{X}(n), B)=E\left[\mathbb{1}_{B} \bar{X}(n+1) \mid \mathcal{F}_{X(n)}\right]
$$

for every $n \geqslant 0$ and $B \in B$

Consecutuve distributions for a markou process are related,

$$
\begin{aligned}
P_{\bar{X}(n+1)}(B) & =E\left[\mathbb{1}_{B} \bar{X}(n+1)\right] \\
= & E\left[E\left[\mathbb{1}_{B} \bar{X}(n+1) \mid \exists_{\bar{X}(n)}\right]\right]
\end{aligned}
$$

From the definition of transition probability

$$
\mu(\bar{X}(n), B)=E\left[\underline{1}_{B} \bar{X}(n+1) \mid \mathcal{F}_{X(n)}\right]
$$

Thus

$$
\begin{aligned}
P_{\bar{X}(n+1)}(B) & =E[\mu(\bar{X}(n), B)] \\
= & \int_{\mathbb{R}} \mu(x, B) P_{\bar{I}(n)} d x
\end{aligned}
$$

## Weiner Process

Consider a sequence of independent random variables,

$$
L(k)= \pm 1
$$

where

$$
\begin{gathered}
P(L(k)=1)=P(L(k)=-1)=1 / 2 \\
E[L(k)]=0
\end{gathered}
$$

The symetric random walk is defined by

$$
\begin{aligned}
& Z(0)=0 \\
& Z(n)=\sum_{k=1}^{n} L(k)
\end{aligned}
$$

The sequence $(Z(n)) n \geqslant 0$ has the following properties

1) For $0 \leqslant j<k \leqslant m<n$ the increments,

$$
z(k)-z(j), z(n)-z(m)
$$

are independent, since

$$
\begin{aligned}
& 2(k)-2(j)=\sum_{i=5+1}^{k} L(i) \\
& 2(n)-2(m)=\sum_{i=m+1}^{n} L(i)
\end{aligned}
$$

and the vections

$$
\begin{aligned}
& (L(j+1), L(j+2), \ldots, L(k)) \\
& (L(m+1), L(m+2), \ldots, L(n))
\end{aligned}
$$

are indepent since the $L(k)$ are indeperdent and the intersection of the vectors is null because of the assumption.

$$
0 \leqslant j<k \leqslant m<n
$$

2) $E[Z(n)]=0$ since,

$$
E[Z(n)]=E\left[\sum_{i=1}^{n} L(i)\right]
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n} E[L(i)] \\
& =0
\end{aligned}
$$

since it is assumed that $E[L(i)]=0$ for every $i$.
$3) 2(n)$ is a Martingale. This follows from

$$
\begin{aligned}
Z(n) & =\sum_{i=1}^{n} L(i) \\
& =\sum_{i=1}^{n-1} L(i)+L(n) \\
& =2(n-1)+L(n)
\end{aligned}
$$

consider the natural filtration

$$
\begin{aligned}
& \mathcal{F}_{n}^{2}=\sigma\{2(k): k=0,1,2, \ldots, n\} \\
& 2(n) \text { is } \mathcal{F}_{n}^{2} \text {-adapted. }
\end{aligned}
$$

## Taking expectation gives

$$
\begin{aligned}
& E\left[Z(n) \mid \mathcal{F}_{n-1}^{2}\right]=E\left[Z(n-1)+L(n) \mid \mathcal{F}_{n-1}^{2}\right] \\
& =E\left[Z(n-1) \mid \mathcal{F}_{n-1}^{2}\right]+E\left[L(n) \mid \mathcal{F}_{n-1}^{2}\right]
\end{aligned}
$$

now $2(n-1)$ is $\mathcal{F}_{n-1}^{2}$ measured⿱le so

$$
E\left[2(n-1) \mid \mathcal{F}_{n-1}^{2}\right]=2(n-1)
$$

and $L(n)$ is independent of $J_{n-1}^{2}$ so

$$
\begin{aligned}
E\left[L(n) \mid \mathcal{F}_{n-1}^{2}\right] & =E[L(n)] \\
& =0
\end{aligned}
$$

Pulling things together gives the desired result.

$$
E\left[2(n) \mid \mathcal{F}_{n-1}^{2}\right]=2(n-1)
$$

4) The variance of increments with $0 \leq m \leq n$

$$
\begin{aligned}
\operatorname{Var} & {[Z(n)-Z(m)] } \\
& =\operatorname{Uar}\left[\sum_{i=m+1}^{n} L(i)\right]
\end{aligned}
$$

Now

$$
\begin{gathered}
\operatorname{Uar}\left[\sum_{i=m+1}^{n} L(i)\right]=E\left[\left(\sum_{i=m+1}^{n} L(i)\right)^{2}\right] \\
-E\left[\sum_{i=m+1}^{n} L(i)\right]^{2}
\end{gathered}
$$

but $E[L(i)]=0$ so the second term is zero,

$$
\begin{aligned}
E\left[\sum_{i=m+1}^{n} L(i)\right] & =\sum_{i=m+1}^{n} E[L(i)] \\
& =0
\end{aligned}
$$

and for the first term

$$
\begin{gathered}
E\left[\left(\sum_{i=m+1}^{n} L(i)\right)^{2}\right]=E\left[\sum_{i=m+1}^{n} \sum_{j=m+1}^{n} L(i)(j)\right] \\
=\sum_{i=m+1}^{n} \sum_{j=m+1}^{n} E[L(i) L(j)]
\end{gathered}
$$

for $i \neq j$ since $L(i)$ are independent it follows that

$$
\begin{aligned}
E[L(i) L(j)] & =E[L(i)] E[L(j)] \\
& =0 \\
E\left[\left(\sum_{i=m+1}^{n} L(i)\right)^{2}\right] & =\sum_{i=m+1}^{n} E\left[L(i)^{2}\right]
\end{aligned}
$$

now

$$
\begin{aligned}
E\left[L(i)^{2}\right] & =(1)^{2} P(L(i)=1)+(-1)^{2} P(L(i)=-1) \\
& =1 / 2+1 / 2=1
\end{aligned}
$$

Thus

$$
\begin{aligned}
E\left[\left(\sum_{i=m+1}^{n} L(i)\right)^{2}\right] & =\sum_{i=m+1}^{n}(1) \\
& =n-m
\end{aligned}
$$

Bringing things together sives

$$
\operatorname{Uar}[2(n)-2(m)]=n-m
$$

To take the continuous limit $n$ steps of duration $h$ are taken over a time interval $t$, so that

$$
t=n h
$$

taking $h=l$ gives $t \in(0, \infty]$. Now let

$$
L_{h}(k)=\sqrt{h} L(k)= \pm \sqrt{h}
$$

Define the scaled random walk by,

$$
Z_{n}(t)=\left\{\begin{array}{l}
\sum_{k=1}^{n} L_{n}(k) \quad t=k h \\
\text { linear } t \in(k h,(k+i) h)
\end{array}\right.
$$

here linear means $2 n(t)$ is a linear interpolation between points where $t=k h$. Note that

$$
\begin{aligned}
Z_{n}(n h) & =\sum_{k=1}^{n} L_{n}(k) \\
& =\sqrt{h} \sum_{k=1}^{n} L(k) \\
& =\sqrt{n} Z(n)
\end{aligned}
$$

The scalled random walk has the properties

1) None overlapping increments are indeperdent, for

$$
0 \leqslant r<s \leqslant t<u
$$

the intervals are independent.

$$
\left(Z_{h}(s)-Z_{h}(r)\right) \text { and }\left(Z_{h}(u)-Z_{h}(t)\right)
$$

$$
\text { a) } \begin{aligned}
E\left[Z_{n}(t)\right] & =E[\sqrt{h} Z(n)] \\
& =\sqrt{h} E[Z(n)] \\
& =0
\end{aligned}
$$

3) The varrance of scalled increments is given by

$$
\begin{aligned}
\operatorname{Uar} & {\left[Z_{n}(t)-Z_{n}(s)\right]=\sum_{i=m+1}^{n} E\left[L_{n}(i)^{2}\right] } \\
& =\sum_{i=m+1}^{n}(n) \\
& =n(n-m) \\
& =t-s
\end{aligned}
$$

since $t=h n$ and $s=h m$
The variation of the sequence.

$$
\left(Z_{h}(k h, \omega)\right)_{k \geqslant 1}
$$

on the interval $[s, t]$ with

$$
s=m h \quad t=n h
$$

by

$$
\begin{aligned}
U_{[s, t]}\left(Z_{h}, \omega\right) & =\sum_{k=m}^{n-1} \mid Z_{h}((k+1) h, \omega) \\
& -Z_{h}(k h, \omega) \mid
\end{aligned}
$$

Now

$$
\begin{aligned}
& Z_{n}((k+1) h, \omega)-Z_{n}(k h, \omega) \\
= & \sqrt{h}[2(k+1)-2(k)] \\
= & \sqrt{h} L(k+1)
\end{aligned}
$$

50

$$
\begin{aligned}
& U_{[s, t]}\left(z_{n}, \omega\right)=\sum_{k=m}^{n-1}|\sqrt{n} L(k+1)| \\
& =\sqrt{n} \sum_{k=m}^{n-1}|L(k+1)|
\end{aligned}
$$

but $L(k+1)= \pm 1$ so

$$
|L(K+1)|=1
$$

thus

$$
\begin{aligned}
& U_{[s, t]}\left(z_{n}, \omega\right)=\sqrt{h} \sum_{k=m}^{r-1}(1) \\
& =\sqrt{h}(n-m) \\
& \Rightarrow U_{[s, t]}\left(z_{n}, \omega\right)=\sqrt{h}(n-m)
\end{aligned}
$$

using

$$
\begin{aligned}
& t=n h \Rightarrow n=\frac{t}{h} \\
& m=\frac{s}{h}
\end{aligned}
$$

gives

$$
U_{[s, t]}\left(Z_{h}, \omega\right)=\frac{t-s}{\sqrt{h}}
$$

clearly $n \rightarrow 0 \Rightarrow U_{[s, t]}\left(Z_{n}, \omega\right) \rightarrow \infty$.

The quadratic variation is defined by

$$
\begin{gathered}
U_{[t, s]}^{2}\left(Z_{n}, \omega\right)=\sum_{k=m}^{n-1}\left[Z_{n}((k+1) h, \omega)\right. \\
\left.-Z_{n}(k h, \omega)\right]^{2}
\end{gathered}
$$

using

$$
z_{n}((k+1) h, \omega)-z_{n}(k h, \omega)=\sqrt{n} L(k+1)
$$

and

$$
L^{2}(k+1)=1
$$

gives

$$
\begin{aligned}
U_{[t, s]}^{2}\left(z_{n}, \omega\right) & =\sum_{k=m}^{n-1} h L^{2}(k+1) \\
& =n \sum_{k=m}^{n-1}(1)
\end{aligned}
$$

$$
=h(n-m)
$$

but

$$
t=n h \quad s=m h
$$

50

$$
U_{[t, s]}^{2}\left(z_{n}, \omega\right)=t-s
$$

## Theorem

The sequence

$$
\left(z_{n}^{2}(n h)-n h\right)_{n \geqslant 0}
$$

is a mortingale

## Proof

Recall the Doob decomposition for submartingale is given by

$$
\begin{gathered}
A(n)=A(n-1)+E\left[I(n)-I(n-1) \mid I_{n-1}\right] \\
M(n)=I(n)-I(0)-A(n)
\end{gathered}
$$

where $\bar{I}(n)$ is a submartingale A(n) the compensator function and $M(n)$ a martingale.
with $I(n)=Z_{n}^{2}(n t)$ and $Z_{n}(0)=0$ it is seen that

$$
\begin{aligned}
& E\left[Z_{h}^{2}(n h)-Z_{h}^{2}((n-1) h) \mid \mathcal{F}_{n-1}\right] \\
& =E\left[\left(Z_{n}(n h)-Z_{n}((n-1) h)\right)^{2} \mid \mathcal{F}_{n-1}\right] \\
& =E\left[L_{n}^{2}(n h) \mid \mathcal{F}_{n-1}\right]
\end{aligned}
$$

but $\operatorname{Ln}(n h)$ is independent of $\Im_{n-1}$ so

$$
\begin{aligned}
& E\left[L_{n}^{2}(n h) \mid J_{n-1}\right]=E\left[L_{n}^{2}(n h)\right] \\
& =n
\end{aligned}
$$

From the recursion relation for $A(n)$ and $A(0)=0$

$$
\begin{aligned}
& A(n)=A(n-1)+h \\
\Rightarrow & A(1)=h \\
\Rightarrow & A(2)=2 h \\
\Rightarrow & A(3)=3 h \\
\Rightarrow & A(n)=n h
\end{aligned}
$$

It follows that

$$
Z_{n}^{2}(n h)-n h
$$

is a martingale

## Definition of Wiener Process

In the previous section the scaled random walk was defined by

$$
Z_{h}(t)=\sqrt{h} \sum_{i=1}^{N} L(i)
$$

if $t=1$ then

$$
t=N h \Rightarrow h=\frac{1}{N}
$$

then

$$
Z_{h}(1)=\frac{1}{\sqrt{N}} \sum_{i=1}^{N} L(i)
$$

Recall the central limit theorem.
Let $\bar{X}(n)$ be independent identically distributed random variables with finite variance and mean. Let

$$
\Phi(n)=\sum_{i=1}^{n} \bar{X}(i)
$$

and let

$$
T(n)=\frac{I(n)-E[I(n)]}{\sqrt{\operatorname{Var}(I(n))}}
$$

Then
$\lim _{n \rightarrow \infty} P(a<T(n)<b)=\frac{1}{\sqrt{2 \pi}} \int_{a}^{b} e^{-x^{2} / 2} d x$
Now previously it was shown that
$\operatorname{Var}\left(\left(Z_{h}(t)-Z_{h}(s)\right)\right)=t-s$
letting $s=0$ and $t=1$ gives,

$$
\operatorname{Uar}\left(Z_{n}(1)\right)=1
$$

and recall that $E\left[Z_{n}(1)\right]=0$ so that

$$
T_{n}=Z_{n}(1)
$$

further let $n=1 / n$ then $h \rightarrow 0$ is equivalent to $h \rightarrow a$.
It follows trat in the limit $n \rightarrow \infty$ that 2(1) approaches a unit normal distribution.

## Definition Propenties of Wrener Process

Let $\omega(t)$ denote weiner process.

1) $\omega(0)=0$
2) For $0 \leqslant s<t<\infty$ the morement $\omega(t)-\omega(s)$ has a normal distribution with zero mean and standard deviation $\sqrt{t-s}$
3) For every $m \geqslant 0$ and $0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{m}$ the nonoverbipping increments

$$
\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)
$$

for $n=0,1,2, \ldots, m-1$ are ridependent.
4). $\omega(t)$ is continuous.

## Theorem

If $\omega(t)$ is a wiener process show that it has no derivatue

## Proof

The derivatue of the weiner process is given by

$$
\frac{d \omega(t)}{d t}=\lim _{h \rightarrow 0} \frac{\omega(t+h)-\omega(t)}{h}
$$

from the definition of waner process

$$
\operatorname{var}(\omega(t+h)-\omega(t))=h
$$

It follows that

$$
\omega(t+h)-\omega(t) \sim O(\sqrt{n})
$$

Thus as $h \rightarrow 0$

$$
\begin{aligned}
\frac{d \omega(t)}{d t} & \sim \frac{O(\sqrt{h})}{h} \sim O(1 / \sqrt{h}) \\
& \rightarrow \alpha
\end{aligned}
$$

so the derivative does not exist.

## Exerase

Show that the covariance of two weiner processes is guen by

$$
\operatorname{Cov}(\omega(s), \omega(t))=\min (s, t)
$$

Solution
Assume that $t \geqslant s$ then

$$
\begin{aligned}
\operatorname{Cov} & (\omega(s), \omega(t))= \\
& E[(\omega(s)-E[\omega(s)])(\omega(t)-E[\omega(t)])] \\
= & E[\omega(s) \omega(t)-E[\omega(s)] \omega(t) \\
& -\omega(s) E[\omega(t)]+E[\omega(s)] E[\omega(t)]] \\
= & E[\omega(s) \omega(t)]-E[\omega(s)] E[\omega(t)]
\end{aligned}
$$

Now from the definition of a weiner process

$$
E[\omega(s)]=E[\omega(t)]=0
$$

so

$$
\operatorname{Cov}(\omega(s) \omega(t))=E[\omega(s) \omega(t)]
$$

Now since $t \geqslant S$

$$
\begin{aligned}
& E[\omega(s) \omega(t)] \\
& =E[\omega(s)(\omega(t)-\omega(s)+\omega(s))] \\
& =E\left[\omega(s)(\omega(t)-\omega(s))+\omega^{2}(s)\right]
\end{aligned}
$$

$$
=E[\omega(s)(\omega(t)-\omega(s))]+E\left[\omega^{2}(s)\right]
$$

For the first term $s \leqslant t$. If follows that $\omega(s)$ and $\omega(t)-\omega(s)$ do not overlap so are independent form the definition of a weiner process. So

$$
\begin{aligned}
& E[\omega(s)(\omega(t)-\omega(s))] \\
& =E[\omega(s)] E[\omega(t)-\omega(s)] \\
& =0
\end{aligned}
$$

Bringing things together

$$
\begin{aligned}
\operatorname{Cov}(\omega(s) \omega(t)) & =E\left[\omega^{2}(s)\right] \\
& =s
\end{aligned}
$$

using a similar argument for $s \geqslant t$

$$
\operatorname{Cov}(\omega(s) \omega(t))=t
$$

Thus

$$
\operatorname{Cov}(\omega(s) \omega(t))=\min (s, t)
$$

## Definition Gaussian Process

A stochastic process,

$$
(X(t))_{t \geqslant 0}
$$

is a Gaussian process if for every choice of

$$
0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{n}
$$

The vector of increments

$$
\begin{aligned}
& \left(X\left(t_{2}\right)-\bar{x}\left(t_{1}\right)\right),\left(\bar{x}\left(t_{3}\right)-\bar{x}\left(t_{2}\right)\right), \ldots, \\
& \left(\bar{x}\left(t_{n}\right)-\bar{x}\left(t_{n-1}\right)\right)
\end{aligned}
$$

have a Gaussian distribution.
The $n$-dimensional Gaussian
random vector

$$
\bar{x}=\left(x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right)
$$

with mean

$$
\bar{\mu}=\left(\mu_{1}, \mu_{2}, \mu_{3}, \ldots, \mu_{n}\right)
$$

and covariance matrix,

$$
\begin{gathered}
\Sigma=\left(\sigma_{i j}\right)_{i, j} \leqslant n \\
\sigma_{i j}=E\left[\left(x_{i}-\mu_{i}\right)\left(x_{j}-\mu_{j}\right)\right]
\end{gathered}
$$

has density

$$
\begin{gathered}
f(\bar{x})=\frac{1}{(2 \pi)^{n / 2}} \frac{1}{|\bar{z}|^{1 / 2}} \exp \left[-\frac{1}{2}(\bar{x}-\bar{\mu})^{\top}\right. \\
\left.\Sigma^{-1}(\bar{x}-\bar{\mu})\right]
\end{gathered}
$$

Here $I \Sigma 1$ is the determinate
of the covariance matrix. Note that if the covariance matrix is diagonal the random variables are uncorrelated.

## Exercise

show from the definition of a weiner process that if $\omega(t)$ is a wiener process then so the processes $-\omega(t)$.

## Solution

Recall the weiner process is defined by
1.) $\omega(0)=0$
2) For $0 \leqslant s \leqslant t<\infty \quad \omega(t)-\omega(s)$ has normal distribution with zero mean and carrace,

$$
\operatorname{var}[\omega(t)-\omega(s)]=t-s
$$

3) For every $m \geqslant 0$ and $0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{m}$ the nonoverlopping increments

$$
\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)
$$

for $n=0,1,2, \ldots, m-1$ are rndependent.
4) $\omega(t)$ is continuous

First for $-\omega(t)$

1) $\omega(0)=0 \Rightarrow-\omega(0)=0$
2) $0 \leqslant s \leqslant t<\infty, \omega(t)-\omega(s)$

$$
\begin{aligned}
& E[\omega(t)-\omega(s)]=0 \\
& \operatorname{var}[\omega(t)-\omega(s)]=t-s \\
& \omega(t)-\omega(s) \sim N(0,1)
\end{aligned}
$$

for $-\omega(t)$ this implies

$$
\begin{aligned}
E[-\omega(t)+\omega(s)] & =-E[\omega(t)-\omega(s)] \\
& =0
\end{aligned}
$$

$$
\begin{aligned}
& \operatorname{var}[\omega(s)-\omega(t)] \\
& =E\left[(\omega(s)-\omega(t))^{2}\right] \\
& =E\left[(\omega(t)-\omega(s))^{2}\right] \\
& =t-s
\end{aligned}
$$

since the gaussian distribution depends on $\omega(t)-\omega(s)$ squared it is invariant wher reflection $\omega(t)-\omega(s) \rightarrow-\omega(t)+\omega(s)$. Thus -W(t) has normal incroments withe zero mean and variance $t-s$.
3) For all $m \geqslant 0$ and $0 \leqslant t_{1} \leqslant t_{2} \leqslant \cdots \leqslant t_{m}$ the increments $\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)$ are independent for $-\omega(t)$ tris becomes - $\left(\omega\left(t_{n+1}\right)-\omega\left(t_{n}\right)\right)$ which is also independent.
4) Continuity of $\omega(t)$ clearly implies continuity of $-\omega(t)$

Other transformations of the wener process that produce a wemer process are the shift transformation

$$
\omega^{u}(t)=\omega(t+u)-\omega(u)
$$

and the time inversion transformation

$$
I(t)=t \omega(1 / t) \quad t>0
$$

## Stochastic Processes

In this section the terminology of stochastic processes is revewed.
The wemer process is an example of a stochastic process which are a family of random variables

$$
(\bar{X}(t))_{t \in \mathbb{T}}
$$

where $t \in \pi$ is time with

$$
T=(0, \infty)
$$

or

$$
T=[0, T]
$$

with $0<T<\infty$.
If $\Omega$ is the event space a random variable is a function on the space

$$
\pi \times \Omega
$$

with the product $\sigma$-field

$$
\begin{aligned}
B(\bar{\pi}) \times \mathcal{F} & = \\
O & (\{B \times A: B \in B(\bar{\pi}), A \in \mathcal{F}\})
\end{aligned}
$$

where $B(\bar{\pi})$ is the Borel 6-algebra representing time.

## Definition

A mapping

$$
\underline{\bar{X}}(t, \omega): \bar{\pi} \times \Omega \rightarrow \mathbb{R}
$$

is called a stochastic process if it is measureable with respect to the product offeld

$$
B(\pi) \times F
$$

Let $\bar{X}$ be a stochastic process, Then, for all $t \in \bar{\pi}$ the mapping

$$
\bar{X}(t)=\bar{X}(t, *): \Omega \rightarrow \mathbb{R}
$$

## Definition

The maps from $\pi$ to $\mathbb{R}$ dented by

$$
t \rightarrow \underline{x}(t)(\omega)=\underline{x}(t, \omega)
$$

for each fixed $\omega \in \Omega$ are called sample paths of the stochastic process $\bar{X}$.
The finite-dimensional distributions of a stochastic process are the family of probabilities

$$
\begin{aligned}
P_{t_{1} t_{2} \cdots t_{n}} & \left(A_{1} \times A_{2} \times \cdots \times A_{n}\right) \\
= & P\left(\bar{X}\left(t_{1}\right) \in A_{1}, \bar{X}\left(t_{2}\right) \in A_{2}, \cdots,\right. \\
& \left.\underline{X}\left(t_{n}\right) \in A_{n}\right)
\end{aligned}
$$

For avery choice

$$
t_{1}, t_{2}, \ldots, t_{n} \in \Pi
$$

$$
A_{1}, A_{2}, \ldots, A_{n} \in B(\mathbb{R})
$$

Random variables are identical if they aggree on a set with probability one.

## Definition

Consider the two stochastic processes,

$$
\bar{X}=(\bar{X}(t))_{t \in \bar{\pi}} \quad \bar{I}=(\bar{I}(t))_{t \in \bar{\pi}}
$$

defined on the same probability space I is said to be a version, or modification, of $\bar{X}$ if for every $t \in \bar{\pi}$,

$$
P(\{\omega: \bar{X}(t, \omega)=I(t, \omega)\})=1
$$

It then follows that $\bar{X}$ and $\bar{I}$ have the same finite-dimensional distributions, that is

$$
\begin{aligned}
& P\left(X\left(t_{1}\right) \in A_{1}, X\left(t_{2}\right) \in A_{2}, \ldots, X\left(t_{k}\right) \in A_{k}\right) \\
& \quad=P\left(Y\left(t_{1}\right) \in A_{1}, I\left(t_{2}\right) \in A_{2}, \ldots, I\left(t_{k}\right) \in A_{k}\right)
\end{aligned}
$$

A stronger notion of equivalence of stochastic proccesses can be obtained by considering I as a random variable defined on $\Omega$ with values in the set of all paths

$$
\Omega \ni \omega \rightarrow(t \rightarrow \bar{X}(t, \omega)) \in \mathbb{R}^{\pi}
$$

For two processes to be considered equivalent with probability one all of their paths coincide.

## Properties of Paths

Here the properties of paths of a wener process are considered. A path is a mosping $t \in \pi$

$$
t \rightarrow \omega(t, \omega)
$$

by definition a weiner process path is continuous.

## Theorem

For every $t$ almost all paths of a weiner process, $\omega(t, \omega)$, are not differentiable at $t$.

## Proof

The proof consists of showing that for fixed $t$ the set
$A=\{\omega: s \rightarrow \omega(s, \omega)$ has derivative at $t\}$
has probability zero or more
precisely is a subset of a set of probability zero.
If a function has a derivative at $t$ then

$$
\frac{\omega(t+\varepsilon)-\omega(t)}{\varepsilon}
$$

has a limit as $\varepsilon \rightarrow 0$. It follows that this ratio is bounded for small $\varepsilon$. It follows that

$$
\begin{aligned}
A C \bigcup_{k=1}^{\infty} \bigcup_{n=1}^{\infty} A_{n}^{k} & \\
A_{n}^{k} & =\left\{\omega:-k \leqslant \frac{\omega(t+\varepsilon)-\omega(t)}{\varepsilon} \leqslant k, 0<\varepsilon<\frac{1}{n}\right\} \\
& =\left\{\omega:-\sqrt{\varepsilon} k \leqslant \frac{\omega(t+\varepsilon)-\omega(t)}{\varepsilon} \leqslant \sqrt{\varepsilon} k, 0<\varepsilon<\frac{1}{n}\right\}
\end{aligned}
$$

Fix $k$ and estimale the probability of $A_{n}^{k}$ using the fact that the
unit normal cumulative distribution function $N$ is increasing and continuous. Now from the definition of a weiner process

$$
\omega \frac{(t+\varepsilon)-\omega(t)}{\sqrt{\varepsilon}} \sim N(0,1)
$$

has a unit normal distribution. It follows that the probabilitity of $A_{n}^{k}$ is given by

$$
P\left(A_{n}^{k}\right)=N(k \sqrt{\varepsilon})-N(-k \sqrt{\varepsilon})
$$

using

$$
\begin{aligned}
0<\varepsilon<\frac{1}{n} \\
\Rightarrow \quad 0<\sqrt{\varepsilon}<\frac{1}{\sqrt{n}}
\end{aligned}
$$

gives

$$
P\left(A_{n}^{k}\right) \leqslant N\left(\frac{k}{\sqrt{n}}\right)-N\left(-\frac{k}{\sqrt{n}}\right)>0
$$

Since $N(x)$ is an increasing
function of $x$. Now

$$
\begin{aligned}
\lim _{n \rightarrow \infty} P\left(A_{n}^{k}\right) \rightarrow & N(0)-N(0) \\
= & \frac{1}{2}-\frac{1}{2} \\
= & 0
\end{aligned}
$$

From the definition of $A_{n}^{k}$

$$
\begin{aligned}
& A_{n+1}^{k} C A_{n}^{k} \\
\Rightarrow & \Omega / A_{n+1}^{k} \supset \Omega / A_{n}^{k}
\end{aligned}
$$

Thus $\Omega / A_{n}^{k}$ is increasing. It follows that

$$
\bigcup_{n=1}^{\infty} A_{n}^{k}=\Omega / \bigcap_{n=1}^{\infty}\left(\Omega / A_{n}^{k}\right)
$$

since $\Omega / A_{n}^{k}$ is increasing

$$
\bigcap_{n=1}^{\infty}\left(\Omega / A_{n}^{k}\right)=\lim _{n \rightarrow \infty} \Omega / A_{n}^{k}
$$

$$
\begin{aligned}
P\left(\hat{\bigcup}_{n=1} A_{n}^{k}\right) & =P\left(\Omega / \hat{n}_{n=1}^{n}\left(\Omega / A_{n}^{k}\right)\right) \\
= & \lim _{n \rightarrow \infty} P\left(\Omega /\left(\Omega / A_{n}^{k}\right)\right) \\
= & P(\Omega)-\lim _{n \rightarrow \infty} P\left(\Omega / A_{n}^{k}\right) \\
= & 1-1 \\
= & 0
\end{aligned}
$$

since

$$
\lim _{n \rightarrow \infty} P\left(A_{n}^{k}\right)=0
$$

and

$$
\begin{aligned}
\lim _{n \rightarrow \infty} P\left(\Omega / A_{n}^{k}\right) & =1-\lim _{n \rightarrow \infty} P\left(A_{n}^{k}\right) \\
& =1
\end{aligned}
$$

Finally bringing things together, the desire is to prove that
the weiner is not differentiable by prooring that the probability that the derivative exists is zero on the following set
$A=\{\omega: s \rightarrow \omega(s, \omega)$ has derivative at $t\}$
where

$$
\begin{gathered}
A \subset \bigcup_{k=1}^{\infty} \bigcup_{n=1} A_{n}^{k} \\
A_{n}^{k}=\left\{\omega: \sqrt{\varepsilon} K \leq \frac{W(t+\varepsilon)-W(t)}{\sqrt{\varepsilon}} \leq \sqrt{\varepsilon} k, 0<\varepsilon<\frac{1}{n}\right\}
\end{gathered}
$$

It has been shown that

$$
P\left(\bigcup_{n=1}^{\infty} A_{n}^{k}\right)=0
$$

The desired result follows

$$
P(A) \leqslant P\left(\bigcup_{k=1}^{\infty} \bigcup_{n=1}^{\infty} A_{n}^{k}\right)
$$

$$
\begin{aligned}
& \leqslant \sum_{k=1}^{\infty} P\left(\bigcup_{n=1}^{\infty} A_{n}^{k}\right) \\
& =0
\end{aligned}
$$

where the last step follows from subaditivity of probability measure.

In the following discussions partitions of time are assumed with the following properties

$$
\pi_{n}=\left\{t_{0}, t_{1}, t_{2}, \ldots, t_{n}\right\}
$$

where $\pi_{n}$ is a partition of $[0, t]$ satisfying

$$
0=t_{0}<t_{1}<\cdots<t_{n}=t
$$

ard

$$
\lim _{n \rightarrow \infty} \max _{j=1,2, \cdots, n}\left\{t_{j+1}-t_{j}\right\} \rightarrow 0
$$

## Definition

For any process I and $t \in[0, T]$ let

$$
\begin{aligned}
U_{[0, t]}^{2}(n) & =U_{[0, t]}^{2}\left(\left(\bar{X}\left(t_{k}\right)\right)_{k \leqslant n}\right) \\
& =\sum_{j=0}^{n-1}\left[\bar{X}\left(t_{j+1}\right)-\bar{X}\left(t_{j}\right)\right]^{2}
\end{aligned}
$$

If there evists a process

$$
[\bar{X}, \bar{X}]=\{[\bar{X}, \bar{X}](t) ; t \in[0, T]\}
$$

such that for all $t$

$$
U_{[0, t]}^{2}(n) \rightarrow[\bar{X}, \bar{X}](t)
$$

in probability for any sequence $[0, t]$, it is said that $[\bar{x}, \bar{x}]$ is the quadratic variation process of $\bar{X}$ in the interval $[0, t]$.

## Martingale Properties

Let $\bar{X}=(\bar{X}(t))_{t \in \pi}$ be a stochastic process on the probability space $\left(\Omega, \mathcal{F}_{1} P\right)$.

## Definition

A family of sub-cfields of $\mathfrak{F}$, denoted by,

$$
\left(\mathcal{F}_{t}\right)_{t \in \bar{\pi}}
$$

is called a fittration if

$$
F_{s} \subset F_{t}
$$

for $s \leq t$. The filtration

$$
\mathcal{F}_{t}^{\underline{x}}=\sigma(\bar{x}(s): s \leqslant t)
$$

with $t \in \bar{\pi}$ is called the natural fittoration for the stochastic process $\bar{X}$ or the filtration

## generated by X.

## Definition

A stochastic process $\bar{X}=(\bar{X}(t))_{t \in \pi}$ is adapted to the filtration $\left(\mathcal{F}_{t}\right)_{t \in \bar{\pi}}$ if for all $t \in \bar{\pi} \bar{X}(t)$ is $\mathcal{F}_{t}$-measurable, i.e.

$$
E\left[\bar{X}(t) \mid \mathfrak{F}_{t}\right]=\bar{X}(t)
$$

The natural fittration of $\bar{X}$ is the smallest fittration to which I is astepter

## Stochastic Integrals

Consider the scaled random walk previously discussed,

$$
Z_{n}(t)=\sqrt{h} \sum_{n=1}^{N} L(n)
$$

where $t>0$ let the tength of a single time step be defined by

$$
h=\frac{t}{N} \Rightarrow t=h N
$$

Now, recall that in the binomial model an asset price is given by

$$
S_{h}(n h)=S_{h}((n-1) h)(1+K(n))
$$

The returns, $k(n)$, are assumed to be independent.

$$
K(n)= \begin{cases}U & \text { with probability } \frac{1}{2} \\ D & \text { with probability } 1 \frac{1}{2}\end{cases}
$$

define the logarithmic rate of return by,

$$
k(n)=\log (1+K(n))
$$

assume that

$$
k(n)=\left\{\begin{array}{l}
m h+\sigma \sqrt{h} \\
m h-\sigma \sqrt{h}
\end{array}\right.
$$

for some constants $m$ and 6 which can be determined from $u$ and $D$.

Now

$$
\begin{aligned}
E[k(n)]= & (m n+6 \sqrt{n})\left(\frac{1}{2}\right) \\
& +(m n-6 \sqrt{n})\left(\frac{1}{2}\right)
\end{aligned}
$$

$$
=m h
$$

and

$$
\begin{aligned}
\operatorname{Var} & (k(n))=E\left[k^{2}(n)\right]-E^{2}[k(n)] \\
= & (m h+\sigma \sqrt{n})^{2}\left(\frac{1}{2}\right)+(m h-\sigma \sqrt{n})^{2}\left(\frac{1}{2}\right) \\
& -(m h)^{2} \\
= & {\left[(m h)^{2}+2 m \hbar \sigma \sqrt{n}+\sigma^{2} h\right]\left(\frac{1}{2}\right) } \\
+ & {\left[(m h)^{2}-2 m h \sigma \sqrt{n}+\sigma^{2} h\right]\left(\frac{1}{2}\right) } \\
& -(m h)^{2} \\
= & \sigma^{2} h
\end{aligned}
$$

using

$$
\begin{aligned}
& k(n)=\log (1+k(n)) \\
\Rightarrow & 1+k(n)=e^{k(n)}
\end{aligned}
$$

it follows that

$$
\begin{aligned}
S_{h}(n h) & =S_{h}((n-1) h) e^{k(n)} \\
& =S_{h}((n-2) h) e^{k(n)+k(n-1)} \\
& =S_{h}(0) e^{k(n)+k(n-1)+\cdots+k(1)}
\end{aligned}
$$

Now

$$
\begin{aligned}
\sum_{i=1}^{n} R(i) & =\sum_{i=1}^{n}[m h+\sigma \sqrt{h} L(i)] \\
& =m h n+\sigma \sqrt{h} \sum_{i=1}^{n} L(i) \\
& =m h n+\sigma Z_{h}(h n)
\end{aligned}
$$

using $t=h n$ gives

$$
S_{h}(t)=S_{h}(0) e^{m t+\sigma Z_{h}(t)}
$$

in the continuous $\lim$ it $h \rightarrow 0$ and

$$
z_{n}(t) \rightarrow \omega(t)
$$

thus

$$
S(t)=S(0) e^{m t+\sigma \omega(t)}
$$

Now consider

$$
S_{h}(t+h)=S(0) e^{m(t+h)+\sigma Z_{h}(t+h)}
$$

and

$$
\begin{aligned}
& Z_{h}(t+h)=\sqrt{h} \sum_{i=1}^{n+1} L(i) \\
& =\sqrt{h} \sum_{i=1}^{n} L(i)+\sqrt{h} L(n+1)
\end{aligned}
$$

then

$$
\begin{aligned}
& S_{h}(t+h)=S(0) e^{m(t+h)+\sigma Z_{h}(t+h)} \\
& =S(0) e^{m t+\sigma Z_{h}(t)+m h+\sigma \sqrt{h} L(n+1)} \\
& =S(0) e^{m t+\sigma Z_{h}(t)} e^{m h+\sigma \sqrt{h} L(n+1)} \\
& =S(0) e^{m t+\sigma Z_{h}(t)} e^{m h+\sigma \sqrt{h} L(n+1)}
\end{aligned}
$$

$=S_{h}(t) e^{m h+\sigma \sqrt{h} L(n+1)}$
since

$$
S_{h}(t)=S(0) e^{m t+\sigma Z_{n}(t)}
$$

So
$S_{h}(t+h)=S_{h}(t) e^{m h+\sigma \sqrt{h} L(n+1)}$
Now for $h \ll 1$ consider

$$
e^{x}=1+x+\frac{x^{2}}{2}+\frac{x^{3}}{3!}+\cdots+\frac{x^{n}}{n!}+\cdots
$$

It follows that

$$
\begin{aligned}
e^{m h}+\sigma \sqrt{h} L(n+1) & \approx 1+(m h+\sigma \sqrt{h} L(n+1)) \\
& +\frac{1}{2}(m h+\sigma \sqrt{h} L(n+1))^{2} \\
& =1+m h+\frac{\sigma \sqrt{h}}{2} L(n+1)+\frac{m^{2} h^{2}}{2}
\end{aligned}
$$

$$
+m(h)^{3 / 2} L(n+1)+\sigma^{2} h L^{2}(n+1)
$$

keeping only linear or greater terms and recalling that

$$
L^{2}(n+1)=1
$$

gives

$$
\begin{aligned}
e^{m h}+ & \sigma \sqrt{h} L(n+1) \approx 1+m h \\
+ & \frac{\sigma^{2} h}{2}+\sigma \sqrt{h} L(n+1) \\
= & 1+\left(m+\frac{1}{2} \sigma^{2}\right) h+\sigma \sqrt{h} L(n+1)
\end{aligned}
$$

Recalling that

$$
\begin{aligned}
Z_{h}(n h) & =\sum_{i=1}^{n} \sqrt{h} L(i) \\
\Rightarrow Z_{h}((n+1) h) & =\sum_{i=1}^{n+1} \sqrt{h} L(i) \\
\Rightarrow Z_{n}((n+1) h) & =Z_{n}(n h)+\sqrt{h} L(n+1)
\end{aligned}
$$

but

$$
\begin{aligned}
t=n h=>\quad t+h & =n h+h \\
& =(n+1) h
\end{aligned}
$$

it follows that

$$
Z_{n}(t+h)-Z_{n}(t)=\sqrt{h} L(n+1)
$$

Bringing thangs together gives,

$$
\begin{aligned}
& S_{h}(t+h)=S_{h}(t)\left[1+\left(m+\frac{1}{2} \sigma^{2}\right) h\right. \\
&\left.+\sigma\left(z_{h}(t+h)-z_{h}(t)\right)\right]
\end{aligned}
$$

let $\mu=m+\frac{1}{2} \sigma^{2}$, then

$$
\begin{aligned}
& S_{h}(t+h)= S_{h}(t)[1+\mu h \\
&+\left.\sigma\left(z_{h}(t+h)-z_{h}(t)\right)\right] \\
& \Rightarrow S_{h}(t+h)-S_{h}(t)=\mu S_{h}(t) h \\
&+\sigma\left(z_{h}(t+h)-z_{h}(t)\right)
\end{aligned}
$$

In the limit $h \rightarrow 0$ the frst inclination is to write

$$
\left.S_{n} \frac{(t+h)-S_{h}(t)}{h}=\mu S_{h}(t)+\sigma S_{h}(t) \frac{z_{h}(t+h)-z(t)}{h}\right)
$$

it was shown that the weiner process is not differentiable so the last term does not enst.

Taking the limit $h \rightarrow d t$ of the differential form gives

$$
\begin{aligned}
& \lim _{h \rightarrow 0} S_{h}(t+h)-S_{h}(t) \\
& =\lim _{h \rightarrow 0} \mu S_{h}(t) h \\
& +\sigma S_{h}(t)\left(z_{h}(t+h)-z(t)\right) \\
& \Rightarrow d S(t)=\mu S(t) d t \\
& +\sigma S(t) d \omega(t)
\end{aligned}
$$

Integrating gives

$$
\begin{aligned}
S(t)=S(0) & +\int_{0}^{t} \mu S(u) d u \\
& +\int_{0}^{t} \sigma S(u) d \omega(u)
\end{aligned}
$$

## Itô Integral

The space of $\mu^{2}$ of integrable functions is defined by
$\mu^{2}=\{f:[0, T] \times \Omega \rightarrow \mathbb{R}: f$ is adapled,

$$
E\left[\int_{0}^{T} f^{2}(t) d t\right]<\infty \xi
$$

## Definitron

A function $f \in M^{2}$ is simple, $f \in s^{2}$, if there exists a partition,

$$
0=t_{0}<t_{1}<t_{2}<\cdots<t_{n}=T
$$

and $\mathcal{F}_{t_{k}}$-measureable rardom variables $\beta_{k}$ with $E\left[\beta_{k}^{2}\right]<\infty$ for $k=0,1,2,3, \ldots, n-1$, such that

$$
f(t, \omega)=\beta_{0} \underline{11}_{\{0\}}+\sum_{k=0}^{n-1} \beta_{k}(\omega) \underline{1}\left(t_{k}, t_{k+1}\right](t)
$$

## Theorem

For even, random process $f \in M^{2}$ there is sequence $\left(f_{n}\right)_{n \geqslant 1}$, of simple processes $f_{n} \in 5^{2}$ such that

$$
\lim _{n \rightarrow \infty} \int_{0}^{T}\left[f(t)-f_{k}(t)\right]^{2} d t=0
$$

## Definition

The stochastic Its integral of a simple process $f \in s^{2}$ is siven by

$$
I(f)=\sum_{k=0}^{n-1} \beta_{k}\left[\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right]
$$

For any subiterval $[a, b] \subset[0, T]$ since

$$
\mathbb{1 1}_{[a, b]} f \in S^{2}
$$

then

$$
\int_{a}^{b} f(t) d \omega
$$

## Theorem (Linearity)

Given $f, g \in S^{2}$ and real numbers $\alpha, \beta$ and let

$$
h=\alpha f+\beta g
$$

Then $h \in s^{2}$ and

$$
I(h)=\alpha I(f)+\beta I(g)
$$

Thus for $[a, b] \subset[0, T]$

$$
\begin{aligned}
& \int_{a}^{b} h(t) d \omega(t)=\alpha \int_{a}^{b} f(t) d \omega(t) \\
&+\beta \int_{a}^{b} g(t) d \omega(t)
\end{aligned}
$$

## Theorem

If $f \in S^{2}$ and $0 \leqslant a<c<b \leqslant T$ then

$$
\begin{aligned}
\int_{a}^{c} f(t) d \omega(t) & +\int_{c}^{b} f(t) d \omega(t) \\
= & \int_{a}^{b} f(t) d \omega(t)
\end{aligned}
$$

## Theorem

For $f \in s^{2}$

$$
E\left[\int_{0}^{T} f(t) d \omega(t)\right]=0
$$

## Proof

By linearity of expectation

$$
E\left[\int_{0}^{T} f(t) d \omega(t)\right]
$$

$$
\begin{aligned}
& =E\left[\sum_{k=0}^{n-1} \beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right] \\
& =\sum_{k=0}^{n-1} E\left[\beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right]
\end{aligned}
$$

Now consider the summation torm and condition on $\mathcal{F}_{k}$.

$$
\begin{aligned}
& E\left[\beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right] \\
& =E\left[E\left[\beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right) \mid \mathcal{F}_{k}\right]\right]\right.
\end{aligned}
$$

since $\beta_{k}$ is $\mathcal{F}_{k}$-measureable and $\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)$ is irdependent of $f_{k}$ th follows that

$$
\begin{aligned}
& E\left[\beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right] \\
& =\beta_{k} E\left[\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right] \\
& =0
\end{aligned}
$$

Thus

$$
E\left[\int_{0}^{T} f(t) d \omega(t)\right]=0
$$

## Theorem

For $f \in s^{2}$

$$
\begin{aligned}
E\left[\left(\int_{0}^{T} f(t)\right.\right. & \left.d \omega(t))^{2}\right] \\
= & E\left[\int_{0}^{T} f^{2}(t) d t\right]
\end{aligned}
$$

Proof

$$
\begin{aligned}
E & {\left[\left(\int_{0}^{T} f(t) d \omega(t)\right)^{2}\right] } \\
= & E\left[\left(\sum_{k=0}^{n-1} \beta_{k}\left(\omega\left(t_{k+1}\right)-\omega\left(t_{k}\right)\right)\right)^{2}\right] \\
= & E\left[\sum_{i=1}^{n-1} \sum_{j=1}^{n-1} \beta_{i} \beta_{j}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)\right. \\
& \left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
=\sum_{i=1}^{n-1} E & {\left[\beta_{i}^{2}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2}\right] } \\
+\sum_{i \neq j}^{n-1} E & {\left[\beta_{i} \beta_{j}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)\right.} \\
& \left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right)\right]
\end{aligned}
$$

The first sum is over $c=j$ and the second $i \neq j$. Consider the first term and take the conditional expectation with respect to $\mathcal{F}_{i}$.

$$
\begin{aligned}
& \sum_{i=1}^{n-1} E\left[\beta_{i}^{2}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2}\right] \\
= & \sum_{i=1}^{n-1} E\left[E\left[\beta_{i}^{2}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2} \mid J_{i}\right]\right]
\end{aligned}
$$

Now $\beta_{i}$ is $\mathcal{F}_{i}$-measureable and $\omega\left(t_{i+1}\right)-\omega\left(t_{c}\right)$ is indepent cent of $\mathcal{F}_{i}$ so

$$
\sum_{i=1}^{n-1} E\left[E\left[B_{i}^{2}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2} \mid J_{i}\right]\right]
$$

$$
\begin{aligned}
& =\sum_{i=1}^{n-1} E\left[\beta_{i}^{2} E\left[\left(\omega\left(t_{c+1}\right)-\omega\left(t_{i}\right)\right)^{2}\right]\right] \\
& =\sum_{i=1}^{n-1} E\left[\beta_{i}^{2}\left(t_{i+1}-t_{i}\right)\right] \\
& =E\left[\sum_{i=1}^{n-1} \beta_{i}^{2}\left(t_{i+1}-t_{i}\right)\right] \\
& =E\left[\int_{0}^{T} f^{2}(s) d s\right]
\end{aligned}
$$

Next consider the second ferm and take the conditional expectation with respect to $\mathcal{F}_{j}$ for $i<j$

$$
\begin{aligned}
& \sum_{i<j}^{n-1} E\left[\beta_{i} \beta_{j}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)\right. \\
& \left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right)\right] \\
= & \sum_{c<j}^{n-1} E\left[E \left[\beta_{i} \beta_{j}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]\right.\right. \\
& \left.\left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right) \mid \xi_{j}\right]\right]
\end{aligned}
$$

since both $\beta_{i}$ and $\beta_{j}$ are $\mathcal{F}_{i}$-measureable and $\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)$ and $\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)$ are independent of $\tilde{\jmath}_{2}$ so

$$
\begin{array}{r}
\sum_{i<j}^{n-1} E\left[E \left[\beta_{i} \beta_{j}\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]\right.\right. \\
\left.\left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right) \mid \xi_{j}\right]\right] \\
=\sum_{i<j}^{n-1} E\left[\beta _ { i } \beta _ { j } E \left[\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)\right.\right. \\
\left.\left.\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right)\right]\right]
\end{array}
$$

bat $\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)$ and $\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)$ are independent so

$$
\begin{aligned}
& E\left[\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)\left(\omega\left(t_{j+1}\right)-\omega\left(t_{j}\right)\right)\right] \\
& =0
\end{aligned}
$$

Similarly assuming $j>i$ gives the same result. It follows that the desired result is obtained

$$
E\left[\left(\int_{0}^{T} f(t) d \omega(t)\right)^{2}\right]=E\left[\int_{0}^{T} f^{2}(t) d t\right]
$$

This result is also called Isometry. The stochastic Itô integral of $f$ is defined by

$$
\begin{aligned}
I(\rho) & =\int_{0}^{T} f(t) d \omega(t) \\
& =\lim _{n \rightarrow \infty} I\left(f_{n}\right)
\end{aligned}
$$

## Theorem

show that

$$
\int_{0}^{t} s d \omega(s)=t \omega(t)-\int_{0}^{t} \omega(s) d s
$$

## Proof

This result follows from
integration by parts using legal algebraic manipulatorns. Recall that integration by parts for the two functions $u$ and u

$$
\int_{a}^{b} u d v=\left.u v\right|_{a} ^{b}-\int_{a}^{b} u d u
$$

Let

$$
\begin{aligned}
& u=s \Rightarrow d u=d s \\
& d v=d \omega \Rightarrow v=\omega
\end{aligned}
$$

thus

$$
\begin{aligned}
\int_{0}^{t} s d \omega(s)=\left.s \omega(s)\right|_{0} ^{t} \\
-\int_{0}^{t} \omega(s) d s \\
\Rightarrow \int_{0}^{t} s d \omega(s)=t \omega(t) \cdot \int_{0}^{t} \omega(s) d s
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_09_20_9148d6cedcaef87d8b1bg-194.jpg?height=617&width=841&top_left_y=153&top_left_x=141)

## Itô Process

A process of the form

$$
\bar{X}(t)=\bar{X}(0)+\int_{0}^{t} a(s) d s+\int_{0}^{t} b(s) d \omega(s)
$$

Is called an Itô process and $a(s)$ and $b(s)$ are the characteristics of $\boxtimes$

Equivalently this can be written in differential form

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

$\bar{X}(t)$ has the following properties.

1) Almost all paths of $\bar{X}$ are continuous.
2) If $a(t)=0$ then $\bar{X}(t)$ is a martingale.
3) If

$$
\int_{0}^{t}|a(s)| d s<\infty
$$

then

$$
E[\bar{X}(t)]=\bar{X}(0)+\int_{0}^{t} E[G(s)] d s
$$

This is easily seen by taking
expectation of the definition
of $\bar{X}(t)$

$$
\begin{aligned}
E & {[\bar{X}(t)]=E\left[\underline{X}(0)+\int_{0}^{t} a(s) d s\right.} \\
& \left.+\int_{0}^{t} b(s) d \omega(s)\right] \\
= & E[\bar{X}(0)]+E\left[\int_{0}^{t} a(s) d s\right] \\
& +E\left[\int_{0}^{t} b(s) d \omega(s)\right]
\end{aligned}
$$

$$
E\left[\int_{0}^{t} a(s) d s\right]=\int_{0}^{t} E[a(s)] d s
$$

and it was previously shown that

$$
E\left[\int_{0}^{t} b(s) d \omega(s)\right]=0
$$

then

$$
E[\bar{X}(t)]=\bar{X}(0)+\int_{0}^{t} E[G(s)] d s
$$

Theorem Conditional ItS Isometry If $f \in \mu^{2},[a, b] \subset[0, T]$

$$
\begin{aligned}
& E\left[\left(\int_{a}^{b} f(s) d w(s)\right)^{2} \mid \mathcal{F}_{a}\right] \\
& \quad=E\left[\int_{a}^{b} f^{2}(s) d s \mid \mathcal{F}_{a}\right]
\end{aligned}
$$

## Theorem

If $I$ is $\mathcal{F}_{a}$ - measureable and bounded with $f \in M^{2}$, then

$$
\bar{X} \int_{a}^{b} f(s) d \omega(s)=\int_{a}^{b} \bar{I} f(s) d \omega(s)
$$

## Theorem

If $f \in M^{2}$ and

$$
M(t)=\int_{0}^{t} f(s) d \omega(s)
$$

then

$$
M^{2}(t)-\int_{0}^{t} f^{2}(s) d s
$$

is a martingale.
Proof
Assume $s<t$ then it must be shown that

$$
\begin{array}{r}
E\left[\mu^{2}(t)-\int_{0}^{t} f^{2}(u) d u \mid \mathcal{J}_{s}\right] \\
=M^{2}(s)-\int_{0}^{s} f^{2}(u) d u
\end{array}
$$

start by consilering

$$
E\left[M^{2}(t)-M^{2}(s) \mid \mathcal{F}_{s}\right]
$$

and

$$
\begin{aligned}
& E\left[M(s) M(t) \mid \mathcal{F}_{s}\right] \\
& =M(s) E\left[M(t) \mid \mathcal{F}_{s}\right] \\
& =M^{2}(s) M^{2}(s) \\
& =E\left[M^{2}(s) \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

Since $M^{2}(s)$ is $\mathcal{F}_{s}$ - measureable
It follows that

$$
\begin{aligned}
& E\left[(M(t)-M(s))^{2} \mid \mathcal{F}_{s}\right] \\
& \quad=E\left[M^{2}(t)-2 M(s) M(t)+M^{2}(s) \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =E\left[M^{2}(t)-2 M^{2}(s)+M^{2}(s) \mid \mathcal{F}_{s}\right] \\
& =E\left[M^{2}(t)-M^{2}(s) \mid \mathcal{F}_{s}\right] \\
& \text { Thus } \\
& E\left[M^{2}(t)-M^{2}(s) \mid \mathcal{F}_{s}\right] \\
& =E\left[(M(t)-M(s))^{2} \mid \mathcal{F}_{s}\right] \\
& \text { Now } \\
& M(t)-M(s)=\int_{0}^{t} f(u) d \omega(u) \\
& -\int_{0}^{s} f(u) d \omega(u) \\
& =\int_{s}^{t} f(u) d \omega(u) \\
& s o \int_{E\left[(M(t)-M(s))^{2} \mid \mathcal{F}_{s}\right]} \\
& =E\left[\left(\int_{s}^{t} f(u) d \omega(u)\right)^{2} \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

$$
=E\left[\int_{s}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right]
$$

where the last stop follows from conditional Itô isometry.
Bringing things together

$$
\begin{aligned}
E\left[M^{2}(t)\right. & \left.-M^{2}(s) \mid \mathcal{F}_{s}\right] \\
= & E\left[\int_{s}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

rearranging and subtracting

$$
E\left[\int_{0}^{t} f^{2}(u) d u \mid J_{s}\right]
$$

from both sides gives

$$
\begin{aligned}
& E\left[\mu^{2}(t) \mid \mathcal{F}_{s}\right]-E\left[\int_{0}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right] \\
& \quad=E\left[\mu^{2}(s) \mid \mathcal{F}_{s}\right]+E\left[\int_{s}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

$$
-E\left[\int_{0}^{t} f^{2}(u) d u \mid f_{s}\right]
$$

Now
$\int_{s}^{t} f^{2}(u) d u=\int_{0}^{t} f^{2}(u) d u-\int_{0}^{s} f^{2}(u) d u$

Pulling trings together gives the final result

$$
\begin{aligned}
& E\left[M^{2}(t)-\int_{0}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right] \\
& =E\left[M^{2}(s) \mid \mathcal{F}_{s}\right]-E\left[\int_{0}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right] \\
& E\left[\int_{0}^{t} f^{2}(u) d u-\int_{0}^{s} f^{2}(u) d u \mid \mathcal{F}_{s}\right] \\
& =E\left[M^{2}(s)-\int_{0}^{s} f^{2}(u) d u \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

$$
=M^{2}(s)-\int_{0}^{s} f^{2}(u) d u
$$

where the last step follows from $\mu^{2}(s)-\int^{5} f^{2}(u) d u$ being $\mathcal{F}_{s}$-measureable. Thus

$$
\begin{aligned}
E\left[M^{2}(t)\right. & \left.-\int_{0}^{t} f^{2}(u) d u \mid \mathcal{F}_{s}\right] \\
& =M^{2}(s)-\int_{0}^{s} f^{2}(u) d u
\end{aligned}
$$

## Quadratic Variation of Itô Process

## Theorem

If $M(t)$ is a martingale with continuous paths and

$$
|M(t)| \leqslant c \leqslant \infty
$$

then

$$
E\left[\sum_{i=0}^{n-1}\left(\mu\left(t_{i+1}\right)-\mu\left(t_{i}\right)\right)^{4}\right] \rightarrow 0
$$

as $\max \left(t_{i+1}-t_{i}\right) \rightarrow 0$ where

$$
0=t_{0}<t_{1}<t_{2}<\cdots<t_{n}=t
$$

## Theorem

Suppose $f \in M^{2}$ then for some positue numbers $C$ and $D$, where

$$
\int_{0}^{t} f^{2}(s) d s \leqslant C
$$

and

$$
M(t)=\int_{0}^{t} f(s) d \omega(s)
$$

satisfies

$$
|M(t)|<D
$$

then

$$
[m, m](t)=\int_{0}^{t} f^{2}(s) d s
$$

## Proof

Recall that the quadratic variation of the process $M(t)$ is given by

$$
[M, M](t)=\sum_{i=0}^{n-1}\left[M\left(t_{i+1}\right)-M\left(t_{i}\right)\right]^{2}
$$

It will be shown that
$\sum_{i=0}^{n-1}\left[M\left(t_{i+1}\right)-M\left(t_{i}\right)\right]^{2} \rightarrow \int_{0}^{t} f^{2}(s) d s$
as the width of the mesh goes to zero,

$$
\max \left(t_{i+1}-t_{i}\right) \rightarrow 0
$$

Let
$\bar{X}_{n}=\sum_{i=0}^{n-1}\left[\mu\left(t_{i+1}\right)-\mu\left(t_{i}\right)\right]^{2}-\int_{0}^{t} f^{2}(s) d s$
then it must be shown that

$$
\bar{X}_{n} \rightarrow 0
$$

as

$$
\max \left(t_{i+1}-t_{i}\right) \rightarrow 0
$$

start be writing the integral as a sum over the mesh.

$$
\int_{0}^{t} f^{2}(s) d s=\sum_{i=0}^{n-1} \int_{t_{i}}^{t_{i+1}} f^{2}(s) d s
$$

Then let
$\bar{Y}_{i}=\left[\mu\left(t_{i+1}\right)-\mu\left(t_{i}\right)\right]^{2}-\int_{t_{i}}^{t_{i+1}} P^{2}(s) d s$

Then

$$
\bar{X}_{n}=\sum_{i=0}^{n-1} \bar{Y}_{i}
$$

It will be shown that

$$
\bar{X}_{n} \rightarrow 0
$$

in $L^{2}$. Previously it was shown that for a bounded martingale $L^{2}$ convergence implies almost surely convergence. Now consider,

$$
\begin{aligned}
& E\left[X_{n}^{2}\right]=E\left[\left(\sum_{i=0}^{n-1} Y_{i}\right)^{2}\right] \\
& =E\left[\sum_{i=0}^{n-1} Y_{i}^{2}+2 \sum_{i<j} I_{i} Y_{j}\right] \\
& =\sum_{i=0}^{n-1} E\left(Y_{i}\right)^{2}+2 \sum_{i<j} E\left[Y_{i} Y_{j}\right]
\end{aligned}
$$

For the second term since $i<j$ it follows that

$$
\begin{aligned}
& E\left[I_{i} \bar{Y}_{j}\right]=E\left[E\left[q_{i} \bar{Y}_{j} \mid \tilde{J}_{j}\right]\right. \\
& =E\left[\bar{Y}_{i} E\left[\bar{Y}_{j} \mid \mathcal{J}_{j}\right]\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
& \bar{Y}_{j}=\left[M\left(t_{j+1}\right)-M\left(t_{j}\right)\right]^{2}-\int_{t_{j}}^{t_{j+1}} P^{2}(s) d s \\
& \text { so } \\
& E\left[\bar{I}_{j}\left(\mathcal{F}_{i}\right]=E\left[\left(M\left(t_{j+1}\right)-M\left(t_{j}\right)\right)^{2}\right.\right. \\
& \left.-\int_{t_{j}}^{t_{j+1}} f^{2}(s) d s \mid \mathcal{F}_{j}\right]
\end{aligned}
$$

For the first term

$$
\begin{aligned}
& E\left[\left(M\left(t_{j+1}\right)-M\left(t_{j}\right)\right)^{2} \mid \mathcal{J}_{j}\right] \\
& =E\left[M^{2}\left(t_{j+1}\right)-2 M\left(t_{j+1}\right) M\left(t_{j}\right)+M^{2}\left(t_{j}\right) \mid \mathcal{F}_{j}\right]
\end{aligned}
$$

Now

$$
\begin{aligned}
E & {\left[M\left(t_{j+1}\right) M\left(t_{j}\right) \mid \mathcal{F}_{j}\right] } \\
& =M\left(t_{j}\right) E\left[M\left(t_{j+1}\right) \mid \mathcal{F}_{j}\right] \\
& =M^{2}\left(t_{j}^{-}\right) \\
& =E\left[M^{2}\left(t_{j}\right) \mid \mathcal{F}_{j}\right]
\end{aligned}
$$

50

$$
\begin{aligned}
& E\left[\left(M\left(t_{j+1}\right)-M\left(t_{j}\right)\right)^{2} \mid J_{j}\right] \\
& \quad=E\left[M^{2}\left(t_{j+1}\right)-M^{2}\left(t_{j}\right) \mid \widetilde{J}_{j}\right]
\end{aligned}
$$

Now for the integral

$$
\begin{aligned}
\int_{t_{j}}^{t_{j+1}} & f^{2}(s) d s=\int_{0}^{t_{j+1}} f^{2}(s) d s \\
& -\int_{0}^{t_{j}} f^{2}(s) d s
\end{aligned}
$$

Pulling things together gives

$$
\begin{aligned}
E\left[I_{j}\right. & \left.\mid \mathcal{F}_{i}\right]=E\left[\mu^{2}\left(t_{j+1}\right)-\mu^{2}\left(t_{j}\right)\right. \\
& \left.-\int_{0}^{t_{j+1}} f^{2}(s) d s+\int_{0}^{t_{j}} \rho^{2}(s) d s \mid \mathcal{J}_{j}\right] \\
= & E\left[\mu^{2}\left(t_{j+1}\right)-\int_{0}^{t_{j+1}} f^{2}(s) d s \mid \mathcal{F}_{j}\right] \\
& -E\left[\mu^{2}\left(t_{j}\right)-\int_{0}^{t_{j}} f^{2}(s) d s \mid \mathcal{F}_{j}\right]
\end{aligned}
$$

Previously it was shown that

$$
M^{2}\left(t_{j+1}\right)-\int_{0}^{t_{j+1}} f^{2}(s) d s
$$

is a martingale and the second term is is $f_{j}$ mesureable so

$$
\begin{gathered}
E\left[I_{j}\left(\mathcal{F}_{i}\right]=\mu^{2}\left(t_{j}\right)-S_{0}^{t_{j}} f^{2}(s) d s\right. \\
-\mu^{2}\left(t_{j}\right)+S_{0}^{t_{j}} f^{2}(s) d s=0
\end{gathered}
$$

thues

$$
E\left[I_{i} \bar{I}_{j}\right]=0
$$

So

$$
E\left[X_{n}^{2}\right]=\sum_{j=0}^{n-1} E\left[Y_{j}^{2}\right]
$$

Now recall that

$$
\bar{Y}_{j}=\left[M\left(t_{j+1}\right)-M\left(t_{j}\right)\right]^{2}-\int_{t_{j}}^{t_{j+1}} P^{2}(s) d s
$$

Consider the relation for two numbers $a$ and $b_{1}$

$$
\begin{aligned}
& 2\left(a^{2}+b^{2}\right)-(a-b)^{2} \\
= & 2\left(a^{2}+b^{2}\right)-a^{2}-b^{2}+2 a b \\
= & a^{2}+b^{2}+2 a b \\
= & (a+b)^{2} \geqslant 0 \\
= & \quad 2 a^{2}+2 b^{2} \geqslant(a-b)^{2}
\end{aligned}
$$

using this relation

$$
\begin{aligned}
E\left[x_{n}^{2}\right] & =\sum_{j=0}^{n-1} E\left[Y_{j}^{2}\right] \\
\leqslant \sum_{j=0}^{n-1} 2 E & {\left[\left(\mu\left(t_{j+1}\right)-\mu\left(t_{j}\right)\right)^{4}\right] } \\
& -\sum_{j=0}^{n-1} 2 E\left[\left(S_{t_{j}}^{t_{j+}} l^{2}(s) d s\right)^{2}\right]
\end{aligned}
$$

From a previous theorem it is known that

$$
2 E\left[\left(M\left(t_{j+1}\right)-M\left(t_{j}\right)\right)^{4}\right] \rightarrow 0
$$

in the continuoles limit. It own also be shown that in the continuous limit

$$
\sum_{j=0}^{n+1}\left(\int_{t_{j}}^{t_{j+1}} \rho^{2}(s) d s\right)^{2} \rightarrow 0
$$

since it is assumed that

$$
\int_{t_{j}}^{t_{j+1}} f^{2}(s) d s \leqslant C
$$

Thus the desired result is obtained the quadratic vertation of the Itô integral is given by

$$
\begin{aligned}
& {[M, M](t)=\int_{0}^{t} f^{2}(s) d s} \\
& M(t)=\int_{0}^{t} f(s) d \omega(s)
\end{aligned}
$$

## Theorem

If

$$
\bar{x}(t)=\bar{x}(0)+\int_{0}^{t} a(s) d s
$$

then

$$
[\bar{x}, \bar{x}](t)=0
$$

## Theorem

For an Its process

$$
d \underline{x}(t)=a(t) d t+b(t) d \omega(t)
$$

where for some finite constant C

$$
\int_{0}^{T} b(s) d \omega(s) \leqslant c<\infty
$$

It follows that

$$
[\bar{x}, \underline{x}](t)=\int_{0}^{t} b^{2}(s) d s
$$

## Proof

Let

$$
\begin{aligned}
& I(t)=\bar{X}(0)+\int_{0}^{t} a(s) d s \\
& z(t)=\int_{0}^{t} b(s) d \omega(s)
\end{aligned}
$$

Then

$$
\begin{aligned}
& {[\bar{X}, \bar{X}](t)=\sum_{i=0}^{n-1}\left[\bar{Y}\left(t_{i+1}\right)+z\left(t_{i+1}\right)\right.} \\
& \left.-\bar{Y}\left(t_{i}\right)-z\left(t_{i}\right)\right]^{2} \\
& =\sum_{i=0}^{n-1}\left[\bar{Y}\left(t_{i+1}\right)-\bar{Y}\left(t_{i}\right)+z\left(t_{i+1}\right)\right. \\
& \left.-z\left(t_{i}\right)\right]^{2} \\
& =\sum_{i=0}^{n-1}\left[\bar{I}\left(t_{i+1}\right)-\bar{I}\left(t_{i}\right)\right]^{2} \\
& +\sum_{i=0}^{n-1}\left[z\left(t_{i+1}\right)-z\left(t_{i}\right)\right]^{2} \\
& +2 \sum_{i<j}\left[\bar{I}\left(t_{i+1}\right)-\bar{Y}\left(t_{i}\right)\right]\left[z\left(t_{i+1}\right)-z\left(t_{i}\right)\right]
\end{aligned}
$$

For the first term from the previous theorem

$$
\sum_{i=0}^{n-1}\left[I\left(t_{i+1}\right)-I\left(t_{i}\right)\right]^{2} \rightarrow 0
$$

and from the theorem before that

$$
\sum_{i=0}^{n-1}\left[z\left(t_{i+1}\right)-z\left(t_{i}\right)\right]^{2} \rightarrow \int_{0}^{t} f^{2}(s) d s
$$

For the last term

$$
\begin{gathered}
\sum_{i<j} \sum_{j}\left[Y\left(t_{i+1}\right)-\bar{Y}\left(t_{i}\right)\right]\left[z\left(t_{i+1}\right)-z\left(t_{i}\right)\right] \\
\leqslant \sqrt{\sum_{i<j}\left(Y\left(t_{i+1}\right)-\bar{Y}\left(t_{i}\right)\right)^{2}} \\
\sqrt{\sum_{i<j}\left(z\left(t_{i+1}\right)-z\left(t_{i}\right)\right)^{2}}
\end{gathered}
$$

Inequality follows from the Cauchy-Schwarts inequality. The righthand side approaches zero in the continuous limit since the first term is zero and the secord is finite. It follows that the quadratic carration of the Itô process is given
by

$$
\begin{aligned}
& d \bar{x}(t)=a(t) d t+b(t) d \omega(t) \\
& {[\bar{x}, \bar{x}](t)=\int_{0}^{t} b^{2}(s) d s}
\end{aligned}
$$

## Theorem

The Its process defined by

$$
d \underline{X}(t)=a(t) d t+b(t) d \omega(t)
$$

is conique.

## Itô Formula

The theory of stochastic integration is concerned with soluing the following problem. Given an Itś process

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

and a smooth flenction of two variables,

$$
F(t, x)
$$

is

$$
\Psi(t)=F(t, \underline{X}(t))
$$

an Itố process? If so what are its characteristics, $a_{y}(t)$ and $b_{y}(t)$,

$$
\bar{I}(t)=a_{y}(t) d t+b_{y}(t) d \omega(t)
$$

Consider the case where
$F$ is only a function of $\bar{x}$ and that

$$
d \bar{X}(t)=d \omega(t)
$$

i.e. $\quad a(t)=0, \quad b(t)=1$. Then

$$
\begin{aligned}
\bar{Y}(t)= & F(\omega(t)) \\
= & F(\omega(0))+\int_{0}^{t} a_{y}(s) d s \\
& +\int_{0}^{t} b_{y}(s) d \omega(s)
\end{aligned}
$$

To find an expression for $a_{y}(t)$ and $b_{y}(t)$ approximale $F(\omega(t))$ over a short time interval. For some $h>0$

$$
\begin{aligned}
F(\omega(t+h))= & F(\omega(t))+\int_{t}^{t+h} a_{y}(s) d s \\
& +\int_{t}^{t+h} b_{y}(s) d \omega(s)
\end{aligned}
$$

Consider the Taylor expansion of $F(x+y)$ where $y \ll x$

$$
F(x+y) \approx F(x)+\frac{d F}{d x} y+\frac{1}{2} \frac{d^{2} F}{d x^{2}} y^{2}
$$

let

$$
x=\omega(t) \quad y=\omega(t+h)-\omega(t)
$$

It follows that

$$
\begin{aligned}
F(\omega(t+h)) & \approx F(\omega(t)) \\
& +\frac{d F}{d \omega(t)}[\omega(t+h)-\omega(t)] \\
& +\frac{1}{2} \frac{d^{2} F}{d \omega^{2}(t)}[\omega(t+h)-\omega(t)]^{2}
\end{aligned}
$$

Now
$d \omega(t) \approx \omega(t+h)-\omega(t) \sim \sqrt{h}$

$$
d t \approx[\omega(t+h)-\omega(t)]^{2} \sim h
$$

using tris and rearranging
gives

$$
\begin{aligned}
d \bar{Y}=d F & (\omega(t))=\frac{1}{2} \frac{d^{2} F(\omega(t))}{d t^{2}} d t \\
& +\frac{d F(\omega(t))}{d t} d \omega(t)
\end{aligned}
$$

Thus

$$
\begin{aligned}
& a_{y}(t)=\frac{1}{2} \frac{d^{2} F(\omega(t))}{d \omega(t)} \\
& b_{y}(t)=\frac{d F(\omega(t))}{d t}
\end{aligned}
$$

## Functions of the Waner Process

## Theorem

If $f \in \mu^{2}$ has continuals paths, then for eveny $t \in[0, T]$ and any sequence $\left(t_{k}^{n}\right)_{k \geqslant 0}$ of partitions of $[0, t]$ with mesh max

$$
\max _{k}\left|t_{k+1}^{n}-t_{k}^{n}\right| \rightarrow 0
$$

as $n \rightarrow \infty$ then

$$
\begin{aligned}
E & {\left[\left(\int_{0}^{t} f(s) d \omega(s)\right.\right.} \\
& \left.\left.-\sum_{i=0}^{n-1} f\left(t_{i}^{n}\right)\left(\omega\left(t_{i+1}^{n}\right)-\omega\left(t_{i}^{n}\right)\right)\right)^{2}\right] \\
& \rightarrow 0
\end{aligned}
$$

as $n \rightarrow \infty$

## Proof

It was previously shown that $f$ has the simple flunation
exponsion

$$
f_{n}(s)=f(0) \mathbb{1}_{\{0\}}+\sum_{k=0}^{n-1} f\left(t_{i}^{n}\right) \mathbb{1}_{\left(t_{k, t_{k+1}^{n}}^{n}\right]}(s)
$$

and that
$\lim _{n \rightarrow \infty} E\left[\int_{0}^{t}\left(f(s)-f_{n}(s)\right)^{2} d s\right]=0$
Now by Its rometry it follows trat

$$
\begin{aligned}
& E\left[\left(\int_{0}^{t} f(s) d \omega(s)-\int_{0}^{t} f_{n}(s) d \omega(s)\right)^{2}\right] \\
& =0
\end{aligned}
$$

By definition
$\int_{0}^{t} f_{n}(s) d \omega(s)=\sum_{i=0}^{n-1} f_{n}(s)\left[\omega\left(t_{i+1}^{n}\right)-\omega\left(t_{i}^{n}\right)\right]$
Thus the desired result is
obtained.

$$
\begin{aligned}
E[ & \left(\int_{0}^{t} f(s) d \omega(s)\right. \\
& \left.\left.-\sum_{i=0}^{n-1} f\left(t_{i}^{n}\right)\left(\omega\left(t_{i+1}^{n}\right)-\omega\left(t_{i}^{n}\right)\right)\right)^{2}\right] \\
& \rightarrow 0
\end{aligned}
$$

## Theorem

Assume $G: \mathbb{R} \rightarrow \mathbb{R}$ is continuous and $Q(x)=0$ for $x \notin[-\mu, \mu]$, then

$$
\begin{aligned}
E[ & \int_{0}^{t} e(\omega(s)) d \omega(s) \\
& -\sum_{i=0}^{n-1} G\left(\omega\left(t_{i+1}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]
\end{aligned}
$$

## Proof

By definition $\ell$ is bounded so $G(\omega(t)) \in \mu^{2}$ so that

$$
\int_{0}^{T} E(t) d \omega(t)
$$

is defined. Letting $f(t)=G(\omega(t))$ in the previous theorem gives the desired result.

## Theorem

Assume that $F: \mathbb{R} \rightarrow \mathbb{R}$ is continuous, twice differentiable and $F(x)=0$ for $x \notin[-M, M]$ for some $M$.
Then the Itô formula holds in the form

$$
\begin{aligned}
& F(\omega(t))-F(0)=\int_{0}^{t} F^{\prime}(\omega(s)) d \omega(s) \\
&+\frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
\end{aligned}
$$

## Proof

Fix $t$ and assume the partition $\left(t_{i}\right)_{i \leqslant n}$ with

$$
t_{i}=\frac{i t}{n} \quad i=0,1,2, \ldots, n
$$

Note that

$$
\lim _{n \rightarrow \infty} t_{i+1}-t_{i}=\lim _{n \rightarrow \infty} \frac{i}{n}=0
$$

$$
\begin{gathered}
F(\omega(t))-F(0)=\sum_{i=0}^{n-1}\left[F\left(\omega\left(t_{i+1}\right)\right)\right. \\
\left.-F\left(\omega\left(t_{i}\right)\right)\right]
\end{gathered}
$$

Now by the Taylor formula for $x<y$ there exists $z \in[x, y]$ such that

$$
F(y)-F(x)=F^{\prime}(x)(y-x)+\frac{1}{2} F^{\prime \prime}(2)(y-x)^{2}
$$

using $x=\omega\left(t_{i}\right)$ and $y=\omega\left(t_{i+1}\right)$ gives

$$
\begin{aligned}
& F\left(\omega\left(t_{i+1}\right)\right)-F\left(\omega\left(t_{i}\right)\right) \\
& =F^{\prime}\left(\omega\left(t_{i}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right] \\
& +F^{\prime \prime}\left(z_{i}\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}
\end{aligned}
$$

for some $z_{i} \in\left[\omega\left(t_{i+1}\right), \omega\left(t_{i}\right)\right]$. Inserting this into the previous expession gives

$$
\begin{aligned}
F(\omega(t))- & F(0) \\
=\sum_{i=0}^{n-1} & F^{\prime}\left(\omega\left(t_{i}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right] \\
+ & F^{\prime \prime}\left(z_{i}\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}
\end{aligned}
$$

First consider the $F^{\prime}\left(\omega\left(t_{i}\right)\right)$ term

$$
\sum_{i=0}^{n-1} F^{\prime}\left(\omega\left(t_{i}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]
$$

In a previous theorem it was shown that as $n \rightarrow \infty$

$$
\begin{aligned}
\sum_{i=0}^{n-1} F^{\prime} & \left(\omega\left(t_{i}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right] \\
& \rightarrow \int_{0}^{t} F^{\prime}(\omega(s)) d \omega(s)
\end{aligned}
$$

To get the desired result it
must be shown that as $n \rightarrow \infty$

$$
\begin{aligned}
\frac{1}{2} \sum_{i=0}^{n-1} F^{\prime \prime} & \left(z_{i}\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
& \rightarrow \frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
\end{aligned}
$$

almost surely,
First it will be shown that

$$
z_{i}=\omega\left(t_{i}\right)
$$

It will be seen to follow from the assumed uniform contanuily of $F(x)$ and $\omega(t)$. Recall that
a function $F(x)$ is uniformly continuous if given $\varepsilon>0$ a $\delta>0$ can be found such that for any $x$ and $y,|x-y|<\delta$ implies

$$
|F(x)-F(y)|<\varepsilon
$$

Also uniform continuty of $\omega(t, \omega)$ implies that for almost all $\omega$ given $\delta>0$ we can find $n(\omega)>0$ such that for every $s$ and $t,|s-t|<\eta(\omega)$ such that

$$
|\omega(s, \omega)-\omega(t, \omega)|<\delta
$$

Now fix $\omega \in \Omega$ and take an arbitrary $\varepsilon>0$ and choose $\delta$ such that uniform continity is satisfied for $F(x)$. For this $\delta$ find $\eta(\omega)$ from the condition continity places on $\omega(t, \omega)$. Let $N=N(\omega)$ be such that

$$
\eta>\frac{t}{N}
$$

All of this implies the following relations for $\omega$ and $F^{\prime \prime}$.

Choose $\varepsilon$ and then determine $\eta>N$ such that

$$
\left|\omega\left(t_{i}\right)-\omega\left(z_{i}\right)\right|<\delta
$$

and

$$
\left|F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)-F^{\prime \prime}\left(z_{i}\right)\right|<\varepsilon
$$

Now the desire is to show that

$$
\begin{aligned}
\frac{1}{2} \sum_{i=0}^{n-1} F^{\prime \prime} & \left(z_{i}\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
& \rightarrow \frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
\end{aligned}
$$

If $z_{i}=\omega\left(t_{i}\right)$ then

$$
\begin{aligned}
\frac{1}{2} \sum_{i=0}^{n-1} F^{\prime \prime} & \left(w\left(t_{i}\right)\right)\left[w\left(t_{i+1}\right)-w\left(t_{i}\right)\right]^{2} \\
& \rightarrow \frac{1}{2} \int_{0}^{t} F^{\prime \prime}(w(s)) d s
\end{aligned}
$$

Combining this with the previous relation gives

$$
\begin{aligned}
& \sum_{i=0}^{n-1}\left[F^{\prime \prime}\left(z_{i}\right)-F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\right]\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
& \quad \rightarrow 0 \\
& \text { as } n \rightarrow \infty \\
& \text { Now for } i \leqslant n \\
& \quad\left|F^{\prime \prime}\left(z_{i}\right)-F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\right|<\varepsilon
\end{aligned}
$$

It follows that

$$
\begin{gathered}
\sum_{i=0}^{n-1}\left[F^{\prime \prime}\left(z_{i}\right)-F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\right]\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
\leqslant \sum_{i=0}^{n-1} \varepsilon\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
=\varepsilon \sum_{i=0}^{n-1}\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}
\end{gathered}
$$

For finite $t$ it follows that

$$
\sum_{i=0}^{n-1}\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}
$$

is finite since

$$
\begin{aligned}
& E\left[\sum_{i=0}^{n-1}\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}\right] \\
& =\sum_{i=0}^{n-1} E\left[\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2}\right] \\
& =\sum_{i=0}^{n-1} t_{[+1}-t_{i} \\
& =t
\end{aligned}
$$

since $\varepsilon$ is arbitrary the desired result follows

$$
z_{i}=\omega\left(t_{i}\right)
$$

To complete the proof it must be shown that as $n \rightarrow \infty$

$$
\frac{1}{2} \sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{c}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2}
$$

$$
\rightarrow \frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
$$

Now the righthand side is equivalent to the limit

$$
\begin{aligned}
\sum_{i=0}^{n-1} F^{\prime \prime} & \left(\omega\left(t_{i}\right)\right)\left(t_{i+1}-t_{i}\right) \\
& ->\int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
\end{aligned}
$$

Combing this with the provous result gives

$$
\begin{aligned}
& \sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\left[\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right]^{2} \\
& -\sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\left(t_{i+1}-t_{i}\right) \\
\Rightarrow & \sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)\left[\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2}\right. \\
& -\left(t_{i+1}-t_{i}\right) \rightarrow 0
\end{aligned}
$$

Let

$$
\underline{\bar{X}}_{i}=\left(\omega\left(t_{i+1}\right)-\omega\left(t_{i}\right)\right)^{2}-\left(t_{i+1}-t_{i}\right)
$$

Then it must be shown that

$$
\sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right) \bar{X}_{i} \rightarrow 0
$$

as $n \rightarrow \infty$ almos surely. This is equivalent to showing that

$$
E\left[\left(\sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{0}\right)\right) \bar{X}_{i}\right)^{2}\right] \rightarrow 0
$$

as $n \rightarrow \infty$

Now

$$
\begin{gathered}
E\left[\left(\sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{j}\right) \bar{X}_{i}\right)^{2}\right]\right. \\
=E\left[\sum_{i=0}^{n-1} \sum_{j=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right) F^{\prime \prime}\left(\omega\left(t_{j}\right)\right)\right. \\
\left.\bar{X}_{i} \bar{X}_{j}\right]
\end{gathered}
$$

$$
\begin{aligned}
&=E {\left[\sum_{i=0}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)^{2} \bar{X}_{i}^{2}\right.} \\
&\left.+\sum_{i<j}^{n-1} F^{\prime \prime}\left(\omega\left(t_{i}\right)\right) F^{\prime \prime}\left(\omega\left(t_{j}\right)\right) \bar{X}_{i} \bar{X}_{j}\right] \\
&=\sum_{i=0}^{n-1} E\left[F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)^{2} \bar{X}_{i}^{2}\right] \\
&+\sum_{i<j}^{n-1} E\left[F^{\prime \prime}\left(\omega\left(t_{i}\right)\right) F^{\prime \prime}\left(\omega\left(t_{j}\right)\right) \bar{X}_{i} \bar{X}_{j}\right]
\end{aligned}
$$

It can be shown that both

$$
\begin{aligned}
& \sum_{i=0}^{n-1} E\left[F^{\prime \prime}\left(\omega\left(t_{i}\right)\right)^{2} \underline{X}_{i}^{2}\right] \rightarrow 0 \\
& \sum_{i<j}^{n-1} E\left[F^{\prime \prime}\left(\omega\left(t_{i}\right)\right) F^{\prime \prime}\left(\omega\left(t_{j}\right)\right) \bar{X}_{i} \bar{X}_{j}\right] \rightarrow 0 \\
& \text { as } n \rightarrow \infty
\end{aligned}
$$

## Functions of Itô Procsses

Here the Itś formula will be extended by both allowing more general forms of $F$ and including more general stochastic processes.
Finst the case where $F$ is independent of $t$ and the weiner process is replaced by a bounded Itô process X.
Recall that an Itsी process is defined by

$$
X(t)=X(0)+\int_{0}^{t} a(s) d s+\int_{0}^{t} b(s) d w(s)
$$

or in differential form,

$$
d \underline{X}(t)=a(t) d t+b(t) d \omega(t)
$$

Consider a continuous function $F(x)$ where $x=X(t)$. The Itô
formula for for $F(\bar{X}(t))$ is given by

$$
\begin{aligned}
& F(\bar{X}(t))-F(\bar{X}(0))=\int_{0}^{t} F^{\prime}(\bar{X}(s)) a(s) d s \\
& +\int_{0}^{t} F^{\prime}(\bar{X}(s)) b(s) d \omega(s) \\
& +\frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\bar{X}(s)) b^{2}(s) d s
\end{aligned}
$$

In differental form

$$
\begin{aligned}
d F(\bar{X}(t))= & {\left[F^{\prime}(\bar{X}(t)) a(t)\right.} \\
& \left.+\frac{1}{2} F^{\prime \prime}(\bar{X}(t)) b^{2}(t)\right] d t \\
+ & F^{\prime}(\bar{X}(t)) b(t) d \omega(t)
\end{aligned}
$$

The proof is long and tedious. Here it will be sketched out to understand the origin of terms in the formula.

The proof assurves that $F: \mathbb{R} \rightarrow \mathbb{R}$ is twice differentiable with a continuous second derivative $F^{\prime \prime}(x)$ (this is written as $F \in C^{2}$ ). It is assumed the $F(x)$ is bounded, $F(x)=0$ is $x \notin[-M,-M]$ for some $\mu$.

Now,

$$
\begin{aligned}
F(\bar{X}(t)) & -F(\bar{X}(0)) \\
= & \sum_{i=0}^{n-1}\left[F\left(\bar{X}\left(t_{i+1}\right)\right)-F\left(\bar{X}\left(t_{i}\right)\right)\right]
\end{aligned}
$$

Now by the Taylor formula for $x<y$ there exists $z \in[x, y]$ such that

$$
F(y)-F(x)=F^{\prime}(x)(y-x)+\frac{1}{2} F^{\prime \prime}(2)(y-x)^{2}
$$

where

$$
y=\underline{X}\left(t_{i+1}\right) \quad x=\underline{X}\left(t_{i}\right)
$$

it is seen that

$$
\begin{aligned}
F\left(\bar{x}\left(t_{i+1}\right)\right)-F\left(\bar{x}\left(t_{i}\right)\right) \\
=F^{\prime}\left(\bar{x}\left(t_{i}\right)\left(\bar{x}\left(t_{i+1}\right)-\bar{x}\left(t_{i}\right)\right)\right. \\
+\frac{1}{2} F^{\prime \prime}\left(z_{i}\right)\left(\bar{x}\left(t_{i+1}\right)-\bar{x}\left(t_{i}\right)\right)^{2}
\end{aligned}
$$

substituting this into the previous expression gives

$$
\begin{aligned}
F(\bar{X}(t))-F(\bar{X}(0)) \\
=\sum_{i=0}^{n-1} F^{\prime}\left(\bar{X}\left(t_{i}\right)\right)\left(\bar{X}\left(t_{i+1}\right)-\bar{X}\left(t_{i}\right)\right) \\
+\frac{1}{2} \sum_{i=0}^{n-1} F^{\prime \prime}\left(Z_{i}\right)\left(\bar{X}\left(t_{i+1}\right)-\bar{X}\left(t_{i}\right)\right)
\end{aligned}
$$

since X $(t)$ is an Itô process

$$
\begin{aligned}
& \bar{X}(t)=\bar{X}(0)+\int_{0}^{t} a(s) d s+\int_{0}^{t} b(s) d w(s) \\
\Rightarrow & \bar{X}\left(t_{i+1}\right)-\bar{X}\left(t_{i}\right)=\int_{t_{i}}^{t_{i+1}} a(s) d s+\int_{t_{i}}^{t_{i+1}} b(s) d w(s)
\end{aligned}
$$

For the first term

$$
\begin{aligned}
& \sum_{i=0}^{n-1} F^{\prime}\left(\bar{X}\left(t_{i}\right)\right)\left(\bar{X}\left(t_{i+1}\right)-\bar{X}\left(t_{i}\right)\right) \\
= & \sum_{i=0}^{n-1} F^{\prime}\left(\underline{X}\left(t_{i}\right)\right)\left[\int_{t_{i}}^{t_{i+1}} a(s) d s+\int_{t_{i}}^{t_{i+1}} b(s) d \omega(s)\right]
\end{aligned}
$$

It can be shown that as $n \rightarrow \infty$

$$
\begin{aligned}
\sum_{i=0}^{n-1} F^{\prime} & \left(\underline{X}\left(t_{i}\right)\right) \int_{t_{i}}^{t_{i+1}} a(s) d s \\
& \rightarrow \int_{0}^{t} F^{\prime}(\underline{X}(s)) a(s) d s
\end{aligned}
$$

and

$$
\begin{aligned}
\sum_{i=0}^{n-1} & F^{\prime}\left(\underline{x}\left(t_{i}\right)\right) \int_{t_{i}}^{t_{i+1}} b(s) d \omega(s) \\
& \rightarrow \int_{0}^{t} F^{\prime}\left(\underline{x}\left(t_{i}\right)\right) b(s) d \omega(s)
\end{aligned}
$$

For the second term it can be shown

$$
\begin{aligned}
\sum_{i=0}^{n-1} & F^{\prime \prime}\left(z_{i}\right)\left(\bar{x}\left(t_{i+1}\right)-\bar{x}\left(t_{i}\right)\right)^{2} \\
& \rightarrow \int_{0}^{t} F^{\prime \prime}(\bar{x}(s)) b^{2}(s) d s
\end{aligned}
$$

bringing things together gives the desired result

$$
\begin{aligned}
& F(\bar{X}(t))-F(\bar{X}(0))=\int_{0}^{t} F^{\prime}(\bar{X}(s)) a(s) d s \\
& +\int_{0}^{t} F^{\prime}(\bar{X}(s)) b(s) d \omega(s) \\
& +\frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\bar{X}(s)) b^{2}(s) d s
\end{aligned}
$$

In differental form

$$
\begin{gathered}
d F(\bar{X}(t))=\left[F^{\prime}(\bar{X}(t)) a(t)+\frac{1}{2} F^{\prime \prime}(\bar{X}(t)) b^{2}(t)\right] d t \\
+F^{\prime}(\bar{X}(t)) b(t) d \omega(t)
\end{gathered}
$$

## Extension to General F

The most general form of the Its formula assumes $F$ has the form

$$
F(t, \bar{X}(t))
$$

where $\bar{X}(t)$ is a Itô process

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

Denote the partial derivatives of $F$ by

$$
\begin{gathered}
F_{t}=\frac{\partial F}{\partial t} \quad F_{x}=\frac{\partial F}{\partial x} \\
F_{x x}=\frac{\partial^{2} F}{\partial x^{2}}
\end{gathered}
$$

It is assumed that $F(t, x) \in C^{1,2}$, has continuous first and second derivatives, and $F(t, x)=0$ for $x \notin[-M, M]$.

The Itô formula is given by

$$
\begin{aligned}
F & (t, \bar{X}(t))-F(0,0)=\int_{0}^{t} F_{t}(s, \bar{X}(s)) d s \\
& +\int_{0}^{t} F_{x}(s, \bar{X}(s)) a(s) d s \\
& +\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s) \\
& +\frac{1}{2} \int_{0}^{t} F_{x x}(s, x(s)) b^{2}(s) d s
\end{aligned}
$$

## Localized Stopping Times

Consider a stochartic process $\bar{X}(t)$ with continous paths, with $t \in[0, T]$. In proofs it is usually assumed that the process is bounded,

$$
|\bar{x}(t)|<M
$$

for every $t$ and almost all $\omega$. This is a restrictive assumption. To allow unbounded processes in a situation where a bound was assumed in a proof a stopping time can be used,
$\tau_{m}(\omega)=\inf \{t \leqslant T:|\bar{X}(\omega, t)| \geqslant M\}$
The convention inf $\{\phi\}=T$. This prevents the process from inoreasing in magnitude beyord $M$.
The stopped process is defined by

$$
\begin{aligned}
\bar{X}_{M}(t) & =\bar{X}\left(t \wedge \tau_{M}\right) \\
& =\left\{\begin{array}{cl}
\bar{X}(t) & t<\tau_{M} \\
M & t \geqslant \tau_{M}
\end{array}\right.
\end{aligned}
$$

Clearly $\bar{I}_{M}(t)$ is bounded. It follows that all tools associated with bounded processes can be used. As $\mu \rightarrow \infty$ it follows that $\underline{X}_{M}(t) \rightarrow \underline{X}(t)$.

It is possible to use more complicated stepping criteria

$$
\tau_{m}=\inf \left\{t: \int_{0}^{t}|f(s)| d s \geqslant M\right\}
$$

Definition: Localizing stopping Time
A sequence $\tau_{n}$ of stopping times is localizing for $\bar{X}$ in $M^{2}$ if,

1. It is increasing: for every $n \geqslant 1$
2. For each $n \geqslant 1$; $\mathbb{1}_{\left\{t \leqslant \tau_{n}\right\}} \bar{X} \in M^{2}$
3. $P\left(U_{n=1}^{\infty}\left\{\omega: \tau_{n}(\omega)=T\right)=1\right.$

## Extensions of the stochastic Integral

Recall the definitions of $L^{2}$ and $M^{2}$,
$L^{2}=\left\{f:[0, T] \times \Omega \rightarrow \mathbb{R}, \int_{0}^{\top} f^{2}(t) d t<\infty\right\}$
$M^{2}=\{f:[0, T] \times \Omega \rightarrow \mathbb{R}: f$ is adapted,

$$
\left.E\left[\int_{0}^{T} \rho^{2}(t) d t\right]<\infty\right\}
$$

Now define,

$$
\begin{gathered}
P^{2}=\{f:[0, T] \times \Omega \rightarrow \mathbb{R}: f \text { is adapted } \\
\left.\int_{0}^{T} f^{2}(t) d t<\infty\right\}
\end{gathered}
$$

## Theorem

If $f \in P^{2}$ then the sequence of stopping times defined for $n \geqslant 1$ by

$$
\tau_{n}=\inf \left\{s: \int_{0}^{s} f^{2}(u) d u \geqslant n\right\}
$$

with the convention that

$$
\inf \{\Phi\}=T
$$

is a boalizing sepuence for $f$ in $\mathrm{M}^{2}$.

## Proof

Recall that a stopping time is localising for $\bar{X}$ in $\mu^{2}$ if,

1. It is increasing: for every $n \geqslant 1 \tau_{n}<\tau_{n+1}$
2. For each $n \geqslant 1 ; \mathbb{1}_{\left\{t \leqslant \tau_{n}\right\}} \bar{X} \in M^{2}$
3. $P\left(U_{n=1}^{\infty}\left\{\omega: \tau_{n}(\omega)=T\right)=1\right.$

For the first property, $\tau_{n+1} \geqslant \tau_{n}$

$$
\tau_{n}=\inf \left\{s: \int_{0}^{s} f^{2}(u) d u \geqslant n\right\}
$$

$$
\tau_{n+1}=\inf \left\{s: \int_{0}^{s} f^{2}(u) d u \geqslant n+1\right\}
$$

clearly the integrand is positive so,

$$
\int_{0}^{5} f^{2}(u) d u
$$

is an increasing function of $s$.
It follows that

$$
\begin{aligned}
\int_{0}^{S_{n+1}} f^{2}(u) d u=\int_{0}^{S_{n}} f^{2}(u) d u \\
+\int_{S_{n}}^{S_{n+1}} f^{2}(u) d u \\
\Rightarrow \int_{0}^{S_{n+1}} f^{2}(u) d u \geqslant \int_{0}^{S_{n}} f^{2}(u) d u
\end{aligned}
$$

it follows that

$$
\tau_{n+1} \geqslant \tau_{n}
$$

For term 2 it must be shown that $\mathbb{I}_{\left\{t \leqslant \tau_{n}\right\}} \bar{X} \in M^{2}$. It is
assumed that $0 \leqslant \tau_{n} \leqslant T$.

$$
\begin{aligned}
& \int_{0}^{\tau_{n}(\omega)} f^{2}(s, \omega) d s \\
= & \int_{0}^{\top} \mathbb{1}_{\left\{s \leqslant \tau_{n}(\omega)\right\}} f^{2}(s, \omega) d s \\
\leqslant & n
\end{aligned}
$$

It follows that

$$
E\left[\int_{0}^{T} \mathbb{1}_{\left\{s \leq \tau_{n}(\omega)\right\}} f^{2}(s, \omega) d s\right] \leqslant n
$$

Thus

$$
\mathbb{1}_{\left\{t \leqslant r_{n}\right\}} f(t, \omega) \in M^{2}
$$

For the final item it must be shown that

$$
P\left(U_{n=1}^{\infty}\left\{\omega: \tau_{n}(\omega)=T\right\}\right)=1
$$

If for some $\omega \in \Omega$

$$
\int_{0}^{T} f^{2}(s, \omega)<\infty
$$

this represents a possible path for the process. This follows from $f \in P^{2}$. Now for some $n$,

$$
\int_{0}^{T} f^{2}(s, \omega) d s \leq n
$$

Where $n \in \mathbb{N}$, so that $\tau_{n}(\omega)=T$. It follows that

$$
\begin{aligned}
\left\{\omega: \int_{0}^{T} f^{2}(s, \omega) d s\right. & <\infty\} \\
c \bigcup_{n=1}^{\infty}\left\{\omega: \tau_{n}(\omega)\right. & =T\}
\end{aligned}
$$

but

$$
\left\{\omega: \int_{0}^{T} f^{2}(s, \omega) d s<\alpha\right\}
$$

occurs with probability since
$f \in Q^{2}$.

To extend the stochastic integral to a larger space. Let $f \in P^{2}$ and take a localizing sequence for $f \in M^{2}$. There exist continuous martingales $M_{n}(t)$ such that

$$
M_{n}(t)=\int_{0}^{T} \mathbb{1}_{[0, t]}(s) f(s) \mathbb{1}_{\left[0, \tau_{n}\right]}(s) d \omega(s)
$$

## Definition

The stochastic integral of a process $f \in P^{2}$ is the process

$$
\lim _{n \rightarrow \infty} M_{n}(t)=\int_{0}^{t} f(s) d \omega(s)
$$

## Theorem

There exists a continuous process $I(t)$ such that

$$
\bar{X}(t)=\lim _{n \rightarrow \infty} M_{n}(t)
$$

To prove this it will be
shown that for some $\omega \in \Omega$ if the values of two processes remain equal up to a stopping time, $\tau$, then for almost all such w the same will hold for their shochastic integrals up to anytrme $t<\tau(\omega)$

## Theorem

If $f, g \in M^{2}$ and $\tau$ is a stapping time such that,

$$
f(t, \omega)=g(t, \omega)
$$

whenever $t \leqslant \tau(\omega)$, then

$$
\int_{0}^{t} f(s) d w(s)=\int_{0}^{t} g(s) d w(s)
$$

for almost all $\omega$ satisfying

$$
t \leqslant \tau(\omega)
$$

With the use of these theorems The It's process can be extorded
to more general integrands.

## Definition

Given processes $a, b$ with

$$
\begin{aligned}
& \int_{0}^{T}|a(s)| d s<\infty \\
& \int_{0}^{T}|b(s)| d s<\infty
\end{aligned}
$$

almost surely, the process

$$
\bar{x}(t)=\bar{x}(0)+\int_{0}^{t} a(s) d s+\int_{0}^{t} b(s) d \omega(s)
$$

where $\bar{X}(t)$ is the limit of the stopped process,

$$
\begin{aligned}
M_{n}(t) & =\int_{0}^{T} \mathbb{1}_{[0, t]} f(s) \mathbb{1}_{\left[0, \tau_{n}\right]} d \omega(s) \\
\bar{X}(t) & =\lim _{n \rightarrow \infty} M_{n}(t)
\end{aligned}
$$

and $f \in \rho^{2}$
$P^{2}=\{f:[0, T] \times \Omega \rightarrow R, f$ - adapted,

$$
\left.\int_{0}^{T} f^{2}(s) d s<\infty \text { almost surely }\right\}
$$

In differential form

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

Now if $a(s)=0 \quad \bar{x}(t)$ is not a martingale wriess in addition to

$$
\begin{gathered}
\int_{0}^{T} f^{2}(s) d s<\infty \\
E\left[\int_{0}^{T} f^{2}(s) d s\right]<\infty
\end{gathered}
$$

thus $f \in M^{2}$

## Theorem

If $r$ is a stopping time and $g, h \in P^{2}$ and

$$
g(t, \omega)=h(t, \omega)
$$

for $t \leqslant \tau(\omega)$, then

$$
\int_{0}^{t} g(s) d \omega(s)=\int_{0}^{t} h(s) d \omega(s)
$$

for almost all $\omega$ satisfying $t \leqslant \tau(\omega)$

This result can be summarized as follows.

If certain paths of the integrands are equal then the same paths of the stochastic integral are equal.

The denvation of the Its process previously discussed did not use this property

Before giving the general versions of the Itj formula the current situation will be reviewed to point out the relevance of the new space of integrands.
For a given $a(t)$ and $b(t)$ sactisfying

$$
\int_{0}^{T}|a(s)| d s<\infty
$$

and $b(t) \in P^{2}$ the Itó process I takes the form

$$
\bar{X}(t)=\bar{X}(0)+\int_{0}^{t} a(s) d s+\int_{0}^{t} b(s) d \omega(s)
$$

To use the Itô formula the stochastic integral

$$
\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s)
$$

must be well defined. The function space $\mu^{2}$ is not convenient since if $b \in M^{2} F_{x}(t, \bar{x}(t)) b(t)$ does not need to be in $M^{2}$. The restriction that that it be in $M^{2}$ is not practicle since many of the $F$ that arise in models do not sastisty this praperty.
The fonction space $P^{2}$ is less restinctive and more usefull but the $p_{2}$ price pad is that for $b \in P^{2}$ in genearl

$$
\int_{0}^{t} b(s) d w(s)
$$

is not a martingale.

## The Itó Formula for General Integrands

Theorem : Itô formula for function of wiener Process
The Itô process for a function $F: \mathbb{R} \rightarrow \mathbb{R}$ where $F \in C^{2}$, (twice differentrable continuous functions) of a wiener process is given by

$$
\begin{gathered}
F(\omega(t))-F(0)=\int_{0}^{t} F^{\prime}(\omega(s)) d \omega(s) \\
+\frac{1}{2} \int_{0}^{t} F^{\prime \prime}(\omega(s)) d s
\end{gathered}
$$

where $F(t) \in P^{2}$
Theorem : Itô formula for function of Itô process
Assume $F:[0, T] \times \mathbb{R} \rightarrow \mathbb{R}$ where $F \in C^{2}$ (twice differentiable functions)
and let $\bar{X}(t)$ be an ItS process

$$
d \bar{X}(t)=a(t) d t+b(t) d \omega(t)
$$

with

$$
\int_{0}^{T} a(s) d s<\infty
$$

almost surely and $b \in P^{2}$.
Then the process $F(t, \omega(t))$ is an Itô process and the Its formula holds

$$
\begin{aligned}
F(t, \bar{X}(t))-F(0,0) \\
=\int_{0}^{t} F_{t}(s, \bar{X}(s)) d s+\int_{0}^{t} F_{x}(s, \bar{X}(s)) a(s) d s \\
+\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s) \\
+\frac{1}{2} \int_{0}^{t} F_{x x}(s, \bar{X}(s)) b^{2}(s) d s
\end{aligned}
$$

## Local Martingales

Having relaxed the constraint of a function $f$ from $f \in M^{2}$ to $f \in P^{2}$ the stochastic integral,

$$
\int_{0}^{t} f(s) d w(s)
$$

is no longer a martingale. Here it will be seen that localized stopping time provide a solution to the problem.
Recall that a stopping trme, $\tau$, is a random varrable defined by,

$$
\tau: \Omega \rightarrow\{0,1,2, \ldots\} \cup\{\infty\}
$$

where for every $n \geqslant 0$ the event

$$
\{\omega: \tau(\omega)=n\} \in J_{n}
$$

for a given filtration $\exists n . c$ is
said to be a stopping time relative to the filtration $\Im_{n}$.
A localized stopping time is defined by

A sequence $\tau_{n}$ of stopping times is localizing for $\bar{X}(t) \in M^{2}$ if,

1. It is increasing: for every $n \geqslant 1 \tau_{n}<\tau_{n+1}$
2. For each $n \geqslant 1$; $\mathbb{1}_{\left\{t \leqslant \tau_{n}\right\}} \bar{X} \in M^{2}$
3. $P\left(U_{n=1}^{\infty}\left\{\omega: \tau_{n}(\omega)=T\right)=1\right.$

## Definition: Local Martingale

The process $\bar{X}(t)$ adapted to $F_{t}$ is a local martingale if there exists a sequence

$$
\left(\tau_{n}\right)_{n \geqslant 1}
$$

of stopping times such that for each $\omega$ there is $N(\omega)$ so that
$n \geqslant N(\omega)$ implies that $\tau_{n}(\omega) \geqslant T$. It is said $\tau_{n} \geqslant T$ almost surely eventually. For each $n$, the stopped process is a martingale with respect to $f_{t}$.

## Theorem

For $f \in P^{2}$

$$
\bar{X}(t)=\int_{0}^{t} f(s) d \omega(s)
$$

is a local martingale.

## Proof

Recall that the stochastic integral in the space $P^{2}$ is constructed as the limit

$$
\bar{x}(t)=\lim _{n \rightarrow \infty} M_{n}(t)
$$

where
$M_{n}(t)=\int_{0}^{T} \mathbb{1}_{[0, t]}(s) f(s) \mathbb{1}_{\left[0, \tau_{n}\right]}(s) d \omega(s)$
are martingales. This holds for any localizing sequence, for example

$$
\tau_{n}=\inf \left\{t \leqslant T: \int_{0}^{t} f^{2}(s) d s \geqslant n\right\}
$$

with the convention

$$
\inf \{\varnothing\}=T
$$

In words if,

$$
\int_{0}^{t} f^{2}(s) d s<n
$$

there is no need to stop the process.

To prove that $\bar{x}(t)$ is a local martingale it must be shown that each of the
stopped processes

$$
\bar{X}_{\tau_{n}}(t)=\bar{X}\left(t \wedge \tau_{n}\right)
$$

is a martingale.
Now,

$$
\begin{aligned}
& \bar{X}_{k}(t)=\bar{X}\left(t \wedge \tau_{k}\right) \\
= & \lim _{n \rightarrow \infty} \mu_{n}\left(t \wedge \tau_{k}\right) \\
= & \lim _{n \rightarrow \infty} \int_{0}^{\top} \mathbb{1}_{\left[0, t \wedge \tau_{k}\right]}(s) f(s) \mathbb{1}_{\left[0, \tau_{n}\right]}(s) d \omega(s)
\end{aligned}
$$

Now

$$
11\left[0, t \wedge \tau_{k}\right](s)= \begin{cases}1 & s \leq t \wedge \tau_{k} \\ 0 & s>t \wedge \tau_{k}\end{cases}
$$

but

$$
\mathbb{1}_{[0, t]}(s)= \begin{cases}1 & s \leqslant t \\ 0 & s>t\end{cases}
$$

$$
\underline{11}\left[0, \tau_{k}\right](s)= \begin{cases}1 & s \leqslant \tau_{k} \\ 0 & s>\tau_{k}\end{cases}
$$

so

$$
\underline{11}[0, t](s) \underline{1}\left[0, \tau_{k}\right](s)= \begin{cases}1 & s \leqslant t \wedge \tau_{k} \\ 0 & s>t>\tau_{k}\end{cases}
$$

and
$\lim _{n \rightarrow \infty} \int_{0}^{T} \mathbb{1}_{\left[0, t n \tau_{k}\right]}(s) f(s) \underline{1}\left[0, \tau_{n}\right](s) d \omega(s)$
$=\lim _{n \rightarrow \infty} \int_{0}^{\top} \mathbb{1}_{[0, t]}(s) \mathbb{1}_{\left[0, \tau_{k}\right]}(s) f(s) \mathbb{1}_{\left[0, \tau_{n}\right]}(s) d \omega_{(s)}$
Now stopping times are increasing
so,

$$
n \geqslant k \Rightarrow \tau_{n} \geqslant \tau_{k}
$$

thus

$$
\mathbb{1}_{\left[0, \tau_{k}\right]} \mathbb{1 1}_{\left[0, \tau_{n}\right]}=\mathbb{1}\left[0, \tau_{k}\right]
$$

$$
\begin{aligned}
& \operatorname{Th} u s \\
& \lim _{n \rightarrow \infty} \int_{0}^{T} \underline{11}_{[0, t]}(s) \underline{1}_{\left[0, \tau_{k}\right]}(s) f(s) \underline{1}_{\left[0, \tau_{n}\right]}(s) d w(s) \\
& =\int_{0}^{T} \underline{1}_{[0, t]}(s) f(s) \mathbb{1}_{\left[0, \tau_{k}\right]}(s) d w(s) \\
& =M_{k}(t)
\end{aligned}
$$

Thus $\bar{X}(t)$ is a local martingale.

## Theorem

> Any bounded local martingale is a martingale

## Theorem : Conditional Fatou

If $I_{n} \geqslant 0$, then for any sub-sigma field of of $f$

$$
E\left[\lim _{n \rightarrow \infty} \inf I_{n} \mid \infty\right] \leqslant \lim _{n \rightarrow \infty} \inf E\left[I_{n} \mid \mathcal{H}\right]
$$

## Theorem

Any non-negatie local martingale is a super-martingale

## Proof

Let $\bar{X}(t)$ be a local martingale. There exists a sequence of stopping times such that eventually $\tau_{n} \geqslant T$ almost surely and

$$
\bar{X}_{\tau_{n}}(t)=\bar{X}\left(t \wedge \tau_{n}\right)
$$

is a martingale. It follows trat for $s<t \leq T$

$$
E\left[X\left(t \wedge \tau_{n}\right) \mid \mathcal{F}_{s}\right]=\bar{X}\left(s \wedge \tau_{n}\right)
$$

low for large $n$

$$
t \wedge \tau_{n} \rightarrow t
$$

so that almost surely,

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \inf \bar{X}\left(t \wedge \tau_{n}\right)=\bar{X}(t) \\
& \lim _{n \rightarrow \infty} \inf \bar{X}\left(s \wedge \tau_{n}\right)=\bar{X}(s)
\end{aligned}
$$

So

$$
E\left[\bar{x}(t) \mid \tilde{J}_{s}\right]=E\left[\lim _{n \rightarrow \infty} \inf \bar{x}\left(t \wedge \tau_{n}\right) \mid \tilde{J}_{s}\right]
$$

From the conditional Faton theorem it follows that

$$
\begin{aligned}
& E\left[\lim _{n \rightarrow \infty} \inf \bar{X}\left(t \wedge \tau_{n}\right) \mid \mathcal{J}_{s}\right] \\
& \quad \leqslant \lim _{n \rightarrow \infty} \inf E\left[\bar{X}\left(t \wedge \tau_{n}\right) \mid \mathcal{J}_{s}\right]
\end{aligned}
$$

Since $\bar{x}\left(t \wedge \tau_{n}\right)$ is a martingale

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \inf E\left[\underline{\bar{x}}\left(t \wedge \tau_{n}\right) \mid \mathcal{F}_{\delta}\right] \\
=\lim _{n \rightarrow \infty} \inf \underline{\bar{x}}\left(s \wedge \tau_{n}\right)
\end{aligned}
$$

$$
=\bar{X}(s)
$$

Binging things together gives the desired result

$$
E\left[\bar{x}(t) \mid \mathcal{J}_{s}\right] \leqslant \bar{x}(s)
$$

## Theorem

Any non-negative local martingale with

$$
E[\bar{X}(T)]=\bar{X}(0)
$$

is a martingale

## Proof

From the previous theorem it is known that $X(t)$ is a super-martingale so for $s<t$

$$
E\left[\bar{X}(t) \mid \widetilde{J}_{s}\right] \leqslant \bar{X}(s)
$$

taking expectation sives

$$
\begin{aligned}
& E\left[E\left[X(t) \mid \mathcal{F}_{s}\right]\right] \leqslant E[\bar{X}(s)] \\
\Rightarrow \quad & E[\bar{X}(t)] \leqslant E[\bar{X}(s)]
\end{aligned}
$$

For $T \leq t \leq s \leq 0$ it follows that

$$
\begin{gathered}
E[\bar{X}(T)] \leqslant E[\bar{X}(t)] \leqslant E[\bar{X}(S)] \\
\leqslant E[\bar{X}(0)]=\bar{X}(0)
\end{gathered}
$$

Since it is asswer that

$$
E[\bar{X}(T)]=\bar{X}(0)
$$

it follows that

$$
E[I(t)]=E[\bar{X}(s)]
$$

This excludes the possibility of inequality for the super-martingale So

$$
E\left[\bar{X}(t) \mid \mathcal{J}_{s}\right]=\bar{X}(s)
$$

## Theorem

Any local martingale with

$$
E\left[\sup _{t \in[0, T]}\left|\bar{X}_{t}\right|\right]<\infty
$$

## Applications of the Itô Formula

## Theorem

If

$$
d \bar{x}=a d t+b d \omega(t)
$$

with deterministic, not random, $a$ and $b$ and $F(t, x) \in c^{1,2}$, functions with continuous first and second derivatives that satisfies the PDE

$$
F_{t}=-\frac{1}{2} b^{2} F_{x x}-a F_{x}
$$

then $F(t, \bar{X}(t))$ is a local martingale. If additionally $F_{x}(t, \bar{x}(t)) \in M^{2}$ then $F(t, X(t))$ is a martingale.

## Proof

If $F(t, \bar{X}(t)) \in P^{2}$ then previolesly it was shown that,

$$
F(t, \bar{X}(t))-F(0,0)=\int_{0}^{t} F_{t}(s, \bar{X}(s)) d s
$$

$$
\begin{aligned}
& +\int_{0}^{t} F_{x}(s, \bar{x}(s)) a(s) d s \\
& +\int_{0}^{t} F_{x}(s, \bar{x}(s)) b(s) d w(s) \\
& +\frac{1}{2} \int_{0}^{t} F_{x x}(s, \bar{x}(s)) b^{2}(s) d s
\end{aligned}
$$

Now consider the terms

$$
\begin{aligned}
\int_{0}^{t} & F_{t}(s, \bar{X}(s)) d s+\frac{1}{2} \int_{0}^{t} F_{x x}(s, \bar{X}(s)) b^{2}(s) d s \\
& +\int_{0}^{t} F_{x}(s, \bar{X}(s)) a(s) d s \\
= & \int_{0}^{t}\left[F_{t}(s, \bar{X}(s))+\frac{1}{2} F_{x x}(s, \bar{X}(s)) b^{2}(s)\right. \\
& \left.+F_{x}(s, \bar{X}(s)) a(s)\right] d s \\
= & 0
\end{aligned}
$$

This follows from the assumption that

$$
F_{t}=-\frac{1}{2} b^{2} F_{x x}-a F_{x}
$$

## Thus

$$
\begin{aligned}
& F(t, \bar{\Delta}(t))-F(0,0) \\
& =\int_{0}^{t} F_{x}(s, \bar{\Delta}(s)) b(s) d s
\end{aligned}
$$

since $b(s)$ is deterministic and $F_{x} \in M^{2}$ it follows that $F(t, X(t))$ is a modingale.

## Exerase

show that

$$
M(t)=\sigma e^{\sigma \omega(t)-\frac{1}{2} \sigma^{2} t}
$$

is a martingale.

## Solution

To prove that $M(t)$ is a martingale it is sufficient to show that $\mu(t) \in \mu^{2}$, which requires showing that

$$
E\left[M^{2}(t)\right]<\infty
$$

50

$$
\begin{aligned}
& E\left[\mu^{2}(t)\right]=E\left[\int_{0}^{T}\left(\sigma e^{\sigma \omega(s)-2 \sigma^{2} s}\right)^{2} d s\right] \\
& =\int_{0}^{T} E\left[\left(\sigma e^{\sigma \omega(s)-2 \sigma^{2} s}\right)^{2}\right] d s \\
& =\int_{0}^{T} E\left[\sigma^{2} e^{2 \sigma \omega(s)-\sigma^{2} s}\right] d s
\end{aligned}
$$

Now

$$
e^{2 \sigma \omega(s)-\sigma^{2} s}<e^{2 \sigma \omega(s)}
$$

since $\sigma^{2} s>0$, so

$$
\begin{aligned}
\int_{0}^{T} E\left[\sigma^{2} e^{2 \sigma \omega(s)-\sigma^{2} s}\right] d s & \\
& \leqslant \int_{0}^{T} E\left[\sigma^{2} e^{2 \sigma \omega(s)}\right] d s
\end{aligned}
$$

Now for fixed s,

## $\omega(s) \sim \operatorname{Normal}(0, s)$

It follows that

$$
\begin{aligned}
& E\left[e^{2 \sigma \omega(s)}\right]=\frac{1}{2 \pi s} \int_{-\infty}^{\infty} e^{2 \sigma x} e^{-x^{2} / 2 s} d x \\
& =\sqrt{2 \pi s} \int_{-\infty}^{-\infty} e^{2 \sigma x-2 x^{2} / s} d x
\end{aligned}
$$

consider the orgument

$$
\begin{aligned}
& 26 x-\frac{1}{2} x^{2} / s \\
= & -\frac{1}{2 s}\left(x^{2}-4 s \sigma x\right) \\
= & -\frac{1}{2 s}\left(x^{2}-4 s \sigma x+4 s^{2} \sigma^{2}-4 s^{2} \sigma^{2}\right) \\
= & -\frac{1}{2 s}\left[x^{2}-45 \sigma x+(25 \sigma)^{2}\right]+25 \sigma^{2}
\end{aligned}
$$

$$
\begin{aligned}
& =-\frac{1}{2 s}(x-2 s \sigma)^{2}+2 s \sigma^{2} \\
& s \sigma \\
& \int_{-\infty}^{-\infty} e^{2 \sigma x-2 x^{2} / s} d x \\
& =\int_{-\infty}^{\infty} e^{(x-2 s \sigma)^{2} / 2 s} e^{2 s \sigma^{2}} d x \\
& =e^{2 s \sigma^{2}} \frac{1}{2 \pi s} \int_{-\infty}^{\infty} e^{(x-2 s \sigma)^{2} / 2 s} d x \\
& =e^{2 s \sigma^{2}}
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
E\left[M^{2}(t)\right] & =\int_{0}^{T} E\left[\sigma^{2} e^{2 \sigma \omega(s)-\sigma^{2} s}\right] d s \\
& \leqslant \int_{0}^{T} E\left[\sigma^{2} e^{2 \sigma \omega(s)}\right] d s
\end{aligned}
$$

$$
\begin{aligned}
& =\sigma^{2} \int_{0}^{T} E\left[e^{2 \sigma \omega(s)}\right] d s \\
& =\sigma^{2} \int_{0}^{T} e^{2 \sigma^{2} s} d s \\
& \leqslant \infty
\end{aligned}
$$

## Thus $M(t)$ is a martingale since $M(t) \in M^{2}$

## Fyman - Kac Formula

Assume that for a given function $\varphi(x)$ and an Itरे process, $\bar{X}(t)$, with

$$
\begin{gathered}
d \bar{x}(t)=a(t) d t+b(t) d \omega(t) \\
F_{t}(t, x)=-\frac{1}{2} b^{2}(t) F_{x x}(t, x)-a(t) F_{x}(t, x) \\
F(T, x)=\varphi(x)
\end{gathered}
$$

with

$$
F_{x}(t, \bar{x}(t)) b(t) \in M^{2}
$$

Then

$$
F(t, \bar{X}(t))=E\left[\varphi(\bar{X}(T)) \mid \mathcal{J}_{t}\right]
$$

Proof
Recall the Its formula for
for a function, $F(t, x)$, of an 比s process is given by

$$
\begin{aligned}
F(t, \bar{X}(t))-F(0,0) \\
=\int_{0}^{t} F_{t}(s, \bar{X}(s)) d s+\int_{0}^{t} F_{x}(s, \bar{X}(s)) a(s) d s \\
+\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s) \\
+\frac{1}{2} \int_{0}^{t} F_{x x}(s, \bar{X}(s)) b^{2}(s) d s
\end{aligned}
$$

since it is assumed that $F(t, x)$ satisfies the PDE,
$F_{t}(t, x)=-\frac{1}{2} b^{2}(t) F_{x x}(t, x)-a(t) F_{x}(t, x)$
The Its formula becomes,

$$
\begin{aligned}
F(t, \bar{X}(t) & )-F(0,0) \\
= & \int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s)
\end{aligned}
$$

Now at $t=\tau$ it is assumed that

$$
F(T, x)=\varphi(x)
$$

using $x=\bar{X}(T)$ gives

$$
F(T, X(T))=\varphi(X(T))
$$

substituting into the Itô formula gives

$$
\begin{aligned}
\varphi(\bar{X}(T)) & -F(0,0) \\
= & \int_{0}^{T} F_{x}(s, \bar{X}(s)) b(s) d \omega(s)
\end{aligned}
$$

Subtracting the previous equation from this expression gives

$$
\begin{aligned}
q(\bar{X}(T))-F(t, \bar{X}(t))=\int_{0}^{T} F_{x}(s, \bar{X}(s)) b(s) d \omega(s) \\
-\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d \omega(s)
\end{aligned}
$$

$$
=\int_{t}^{T} F_{x}(s, X(s)) b(s) d w(s)
$$

Taking conditional expectation with respect to $\mathfrak{F}_{t}$ gives

$$
\begin{aligned}
E & {\left[q(\bar{X}(T))-F(t, \bar{X}(t)) \mid \mathcal{F}_{t}\right] } \\
& =E\left[\int_{t}^{T} F_{x}(s, \bar{X}(s)) b(s) d w(s) \mid \mathcal{F}_{t}\right]
\end{aligned}
$$

Now the integral is independent of $\mathfrak{F}_{t}$ so

$$
\begin{aligned}
& E\left[\int_{t}^{T} F_{x}(s, X(s)) b(s) d \omega(s) \mid \mathcal{F}_{t}\right] \\
&= E\left[\int_{t}^{T} F_{x}(s, Z(s)) b(s) d \omega(s)\right] \\
&= 0 \\
& \text { since } F_{x}(s, Z(s)) b(s) \in \mu^{2}
\end{aligned}
$$

thus

$$
E\left[q(\bar{X}(T))-F(t, \bar{X}(t)) \mid \mathcal{F}_{t}\right]=0
$$

but $F(t, I(t))$ is $\mathcal{F}_{t}$-measureable so

$$
E\left[\phi(\bar{X}(T)) \mid \mathcal{F}_{t}\right]=F(t, \bar{X}(t))
$$

which is the desired result.

## Itô Formula Exercises

## Theorem Integration by Parts

If $g^{\prime}(t) \in C^{\prime}$ (functions with a continuous first derivative), then

$$
\begin{gathered}
\int_{a}^{b} g^{\prime}(t) w(t) d t=\left.g(t) w(t)\right|_{a} ^{b} \\
-\int_{a}^{b} g(t) d w(t)
\end{gathered}
$$

## Proof

Consider the Its formula for functions of an Itô process

$$
d \bar{x}(t)=a(t) d t+b(t) d \omega(t)
$$

$$
\begin{aligned}
F(t, \bar{X}(t))-F(0,0) \\
=\int_{0}^{t} F_{t}(s, \bar{X}(s)) d s+\int_{0}^{t} F_{x}(s, \bar{X}(s)) a(s) d s \\
+\int_{0}^{t} F_{x}(s, \bar{X}(s)) b(s) d w(s) \\
+\frac{1}{2} \int_{0}^{t} F_{x x}(s, \bar{X}(s)) b^{2}(s) d s
\end{aligned}
$$

Consider the case $a(t)=0$ and $b(t)=1$ so that

$$
\begin{aligned}
d \bar{X}(t) & =d \omega(t) \\
\Rightarrow \quad \bar{X}(t) & =\omega(t)
\end{aligned}
$$

then

$$
\begin{aligned}
& F(t, \omega(t))-F(0,0)=\int_{0}^{t} F_{t}(t, \omega(t)) d t \\
& +\int_{0}^{t} F_{x}(t, \omega(t)) d \omega(s) \\
& +\int_{0}^{t} F_{x x}(t, \omega(t)) d s
\end{aligned}
$$

Now consider the case

$$
F(t, \omega(t))=g(t) \omega(t)
$$

then

$$
\begin{aligned}
& F_{t}(t, \omega(t))=g^{\prime}(t) \omega(t) \\
& F_{x}(t, \omega(t))=g(t) \\
& F_{x_{x}}(t, \omega(t))=0
\end{aligned}
$$

Substitution into the Itoी formula and changins the integration limits to $a \rightarrow b$ gives

$$
\begin{aligned}
& g(t) \omega(t)\left.\right|_{a} ^{b}=\int_{a}^{b} g^{\prime}(t) \omega(t) d t \\
&+ \int_{a}^{b} g(t) d \omega(s) \\
&=\int_{a}^{b} g^{\prime}(t) \omega(t) d t=g(t)\left(\left.\omega(t)\right|_{a} ^{b}\right. \\
&-\int_{a}^{b} g(t) d \omega(s)
\end{aligned}
$$

## Theorem

If $d \bar{X}(t)=a(t) d t+b(t) d \omega(t)$, then

$$
d \bar{X}^{2}(t)=2 \bar{X}(t) d \bar{X}(t)+b^{2}(t) d t
$$

## Proof

The differential form of the Its process form of the Its formula is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

let $F(t, \bar{X}(t))=\bar{X}^{2}(t)$, then

$$
F_{t}=0 \quad F_{x}=2 \bar{X}(t)
$$

$$
F_{x x}=2
$$

It follows that

$$
\begin{aligned}
d \underline{X}^{2}(t)= & 2 \underline{X}(t) a(t) d t+2 \bar{X}(t) b(t) d \omega(t) \\
& +b^{2}(t) d t \\
= & 2 \underline{X}(t)[a(t) d t+b(t) d \omega(t)] \\
& +b^{2}(t) d t \\
= & 2 \underline{X}(t) d \underline{X}(t)+b^{2}(t) d t
\end{aligned}
$$

which is the desired result.

## Theorem

Given Itś processes $\bar{X}(t)$ and $\bar{I}(t)$ with

$$
\begin{aligned}
& d \bar{x}(t)=a_{x}(t) d t+b_{x}(t) d \omega(t) \\
& d \bar{I}(t)=a_{y}(t) d t+b_{y}(t) d \omega(t)
\end{aligned}
$$

Then the product is an Itô
process with

$$
d(\bar{X} \bar{I})=\bar{X} d \bar{I}+I d \bar{X}+b_{x} b_{y} d t
$$

Proof
Recall trat the Itó formula for a genereal function of an Itô process is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here two Its processes are considered.

$$
\begin{aligned}
& d \bar{x}(t)=a_{x}(t) d t+b_{x}(t) d \omega(t) \\
& d \underline{I}(t)=a_{y}(t) d t+b_{y}(t) d \omega(t)
\end{aligned}
$$

and consider the functions

$$
\bar{X}^{2}(t), \bar{I}^{2}(t) \text { and }(X(t)+Y(t))^{2}
$$

with

$$
\begin{aligned}
\bar{x}(t)+\bar{y}(t)= & \left(a_{x}(t)+a_{y}(t)\right) d t \\
& +\left(b_{x}(t)+b_{y}(t)\right) d \omega(t)
\end{aligned}
$$

In the previous theorem it was shown that

$$
d \bar{X}^{2}(t)=2 \bar{X}(t) d \bar{X}(t)+b_{x}^{2}(t) d t
$$

It follows that

$$
d \Psi^{2}(t)=2 I(t) d I(t)+b_{y}^{2}(t) d t
$$

and,

$$
\begin{aligned}
d(\bar{X}(t) & +\bar{Y}(t))^{2} \\
= & 2(\bar{X}(t)+\bar{Y}(t)) d(\bar{I}(t)+\bar{Y}(t)) \\
& +\left(b_{x}(t)+b_{y}(t)\right)^{2} d t
\end{aligned}
$$

Consider

$$
\begin{aligned}
& d(\bar{X}(t)+\bar{Y}(t))^{2}-d \bar{X}^{2}(t)-d \bar{Y}^{2}(t) \\
&= 2(\bar{X}(t)+\bar{I}(t)) d(\bar{X}(t)+\bar{Y}(t)) \\
&+\left(b_{x}(t)+b_{y}(t)\right)^{2} d t \\
&-\left(2 \bar{I}(t) d \bar{X}(t)+b_{x}^{2}(t) d t\right) \\
&-\left(2 \bar{I}(t) d \bar{I}(t)+b_{y}^{2}(t) d t\right)
\end{aligned}
$$

Finst consider the lefthand side

$$
d(\bar{X}(t)+\bar{Y}(t))^{2}-d \overline{\underline{X}}^{2}(t)-d \bar{I}^{2}(t)
$$

$$
\begin{aligned}
= & d\left(\bar{X}^{2}(t)+2 \bar{X}(t) I(t)+\bar{I}^{2}(t)\right) \\
& -d \bar{X}^{2}(t)-d \bar{Y}^{2}(t) \\
= & d \bar{X}^{2}(t)+2 d(\bar{X}(t) \Psi(t))+d \bar{Y}^{2}(t) \\
& -d \bar{X}^{2}(t)-d \bar{I}^{2}(t) \\
= & 2 d(\bar{X}(t) I(t))
\end{aligned}
$$

Now for the righthard sole

$$
\begin{aligned}
2 & (\bar{x}(t)+\bar{y}(t)) d(\bar{x}(t)+\bar{y}(t)) \\
+ & \left(b_{x}(t)+b_{y}(t)\right)^{2} d t \\
- & \left(2 \bar{x}(t) d \bar{x}(t)+b_{x}^{2}(t) d t\right) \\
- & \left(2 \bar{I}(t) d \bar{I}(t)+b_{y}^{2}(t) d t\right) \\
= & 2 \bar{x}(t) d \bar{x}(t)+2 \bar{I}(t) d \bar{x}(t)+2 \bar{x}(t) d \bar{y}(t) \\
& +b_{x}^{2}(\bar{t}) d t+b_{x}^{2}(t) d t+2 b_{x}(t) b_{y}(t) d t \\
& +2 \bar{I}(t) d \bar{I}(t)-2 \bar{I}(t) d \bar{x}(t)
\end{aligned}
$$

$$
\begin{aligned}
- & b_{x}^{2} \overline{(t)} d t-2 \bar{I}(t) d \eta(t)-\overline{b_{y}^{2}}(t) d t \\
= & 2 \bar{I}(t) d \bar{x}(t)+2 \bar{I}(t) d \bar{I}(t) \\
& +2 b_{x}(t) b_{y}(t) d t
\end{aligned}
$$

putting things together gives the desired result

$$
\begin{aligned}
d & (\underline{X}(t) I(t))=\bar{X}(t) d \bar{I}(t) \\
& +I(t) d \underline{X}(t)+b_{x}(t) b_{y}(t) d t
\end{aligned}
$$

which is extension of the product rule from calculus to functions of a random variable.

## Stochastic Differential Equations

Stochastic differential equalions are an extension of troditional differential equations of calculus to include coditional random terms modeled by a weiner process, $\omega(t)$.
Examples of stochastic differential equations are

$$
\begin{aligned}
d \bar{X}(t)=a(t, \bar{X}(t)) d t+b(t, \underline{X}(t)) d \omega(t) \\
\underline{X}(t)=\bar{X}(0)+\int_{0}^{t} a(s, \bar{X}(s)) d s \\
+\int_{0}^{t} b(s, \bar{X}(s)) d \omega(s)
\end{aligned}
$$

An example of a stochastic differential equation from finance is the Black-Scholes equation

$$
d s(t)=\mu s(t) d t+\sigma s(t) d \omega(t)
$$

where $s(t)$ is the price of an asset.

Consider the strohastic process

$$
s(t)=s(0) \exp \left\{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right\}
$$

Show $s(t) \in M^{2}$. This requires showing that

$$
E\left[\int_{0}^{T} s^{2}(t) d t\right]<\infty
$$

50

$$
\begin{aligned}
& E\left[\int_{0}^{T}\left(S(0) \exp \left\{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right\}\right)^{2} d t\right] \\
& =\int_{0}^{T} E\left[\left(S(0) \exp \left\{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right\}\right)^{2}\right] d t \\
& =S^{2}(0) \int_{0}^{T} \exp \left(2 \mu t-\sigma^{2} t\right) E\left[e^{2 \sigma \omega(t)}\right] d t
\end{aligned}
$$

previolesly it was shown that

$$
E\left[e^{2 \sigma \omega(t)}\right]=e^{2 t \sigma^{2}}
$$

So

$$
\begin{aligned}
& E\left[\int_{0}^{T}\left(S(0) \exp \left\{\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right\}\right)^{2} d t\right] \\
= & S^{2}(0) \int_{0}^{T} \exp \left(2 \mu t-\sigma^{2} t\right) E\left[e^{2 \sigma \omega(t)}\right] d t \\
= & S^{2}(0) \int_{0}^{T} \exp \left(2 \mu t-\sigma^{2} t\right) \exp \left(2 t \sigma^{2}\right) d t \\
= & S^{2}(0) \int_{0}^{T} e^{\left(2 \mu+\sigma^{2}\right) t} d t \\
& <\infty
\end{aligned}
$$

which is clearly finite. Thus

$$
S(t) \in M^{2}
$$

## Proposition

show that

$$
S(t)=S(\sigma) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]
$$

solves the Black-sholes equation,

$$
d s(t)=\mu s(t) d t+\sigma s(t) d \omega(t)
$$

## solution

Recall the It's formla for a function of the form $F(t, \bar{X}(t))$

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Now let,

$$
S(t, \omega(t))=F(t, \omega(t))
$$

It follows that

$$
\begin{aligned}
& d \bar{x}(t)=d \omega(t) \\
\Rightarrow \quad & a(t)=0 \quad b(t)=1
\end{aligned}
$$

The Itó formula becomes

$$
\begin{aligned}
& d F(t, \omega(t))=F_{t}(t, \omega(t)) d t \\
& +F_{x}(t, \omega(t)) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \omega(t)) d t
\end{aligned}
$$

Now

$$
\begin{aligned}
& F_{t}(t, \omega(t))=\frac{\partial S(t)}{\partial t} \\
& =\frac{\partial}{\partial t}\left\{S(0) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
=s(\sigma) & \left(\mu-\frac{1}{2} \sigma^{2}\right) \\
& \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
= & \left(\mu-\frac{1}{2} \sigma^{2}\right) s(t)
\end{aligned}
$$

next

$$
\begin{gathered}
F_{x}(t, \omega(t))=\frac{\partial}{\partial \omega(t)} S(t) \\
=\sigma S(t)
\end{gathered}
$$

and finally

$$
\begin{gathered}
F_{x x}(t, \omega(t))=\frac{\partial^{2}}{\partial \omega(t)^{2}} S(t) \\
=\sigma^{2} S(t)
\end{gathered}
$$

bringing things together gives

$$
\begin{aligned}
d S(t) & =\left(\mu-\frac{1}{2} \sigma^{2}\right) s(t) d t \\
& +\sigma S(t) d \omega(t)+\frac{1}{2} \sigma^{2} S(t) d t
\end{aligned}
$$

$\Rightarrow \quad d s(t)=\mu s(t) d t+\sigma s(t) d \omega(t)$
which is the desired result.
Exerase
Find $E[s(t)]$ and $\operatorname{Var}[s(t)]$
Solution
Recall that
$\omega(t) \sim$ Normal $(0, t)$
it follows that

$$
\begin{aligned}
E[s(t)] & =\int_{-\infty}^{\infty} s(\omega) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
\frac{1}{2 \pi t} & \exp \left[-\frac{1}{\partial t} \omega^{2}(t)\right] d \omega(t)
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{\partial \pi t} s(0) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right) t\right] \\
& \int_{-\infty}^{\alpha} \exp \left[\sigma \omega(t)-\frac{1}{\partial t} \omega^{2}(t)\right] d \omega(t)
\end{aligned}
$$

Consider the argument of the exponential,

$$
\begin{aligned}
& \sigma x-\frac{1}{\partial t} x^{2}=-\frac{1}{\partial t}\left(x^{2}-2 \sigma t x\right) \\
& =-\frac{1}{\partial t}\left(x^{2}-2 \sigma t x+\sigma^{2} t^{2}-\sigma^{2} t^{2}\right) \\
& =-\frac{1}{\partial t}(x-\sigma t)^{2}+\frac{1}{2} \sigma^{2} t
\end{aligned}
$$

It follows that

$$
\int_{-\infty}^{\infty} \exp \left(\sigma x-\frac{1}{\partial t} x^{2}\right) d x
$$

$$
\begin{aligned}
& =\int_{-\infty}^{\infty} \exp \left[-\frac{1}{\partial t}(x-\sigma t)^{2}+\frac{1}{2} \sigma^{2} t\right] d x \\
& =e^{\frac{1}{2} \sigma^{2} t} \int_{-\infty}^{\infty} \exp \left[-\frac{1}{2 t}(x-\sigma t)^{2}\right] d x
\end{aligned}
$$

but

$$
\int_{-\infty}^{\infty} \exp \left[-\frac{1}{2 t}(x-\sigma t)^{2}\right] d x=\sqrt{2 \pi t}
$$

bringing things together gives

$$
\begin{aligned}
E[s(t)]= & \frac{1}{\sqrt{2 \pi t}} s(0) \exp \left[\left(\mu-\frac{1}{2} \sigma^{2}\right) t\right] \\
& e^{\frac{1}{2} \sigma^{2} t} \sqrt{2 \pi t} \\
= & s(0) e^{\left(\mu-\frac{1}{2} \sigma^{2}\right) t+\frac{1}{2} \sigma^{2} t} \\
= & s(0) e^{\mu t}
\end{aligned}
$$

Now for variance

$$
\operatorname{var}(s(t))=E\left[s^{2}(t)\right]-E^{2}[s(t)]
$$

ounsider
$E\left[s^{2}(t)\right]$
$=\int_{-\infty}^{\infty} S^{2}(t) \frac{1}{\sqrt{2 \pi t}} \exp \left[-\frac{1}{\partial t} \omega^{2}(t)\right] d \omega(t)$

Now
$\delta^{2}(t)=\delta^{2}(0) \exp \left\{2\left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right]\right\}$

$$
=s^{2}(0) \exp \left[2 \mu t-0^{2} t+2 \sigma \omega(t)\right]
$$

so let $x=\omega(t)$ then

$$
E\left[s^{2}(t)\right]=\int_{-\infty}^{\infty} s^{2}(0) \exp [2 \mu t
$$

$$
\begin{aligned}
& \left.-\sigma^{2} t+2 \sigma x\right] \frac{1}{\sqrt{2 \pi t}} \exp \left(-\frac{1}{2 t} x^{2}\right) d x \\
= & \frac{s^{2}(v)}{\sqrt{2 \pi t}} e^{\left[\left(2 \mu-\sigma^{2}\right) t\right]} \int_{-\infty}^{\infty} e^{26 x-\frac{1}{2 t} x^{2}} d x
\end{aligned}
$$

Completing the square of the exponential argument gives

$$
\begin{aligned}
& 26 x-\frac{x^{2}}{2 t}=-\frac{1}{2 t}\left(-46 t x+x^{2}\right) \\
& =-\frac{1}{2 t}\left(x^{2}-46 t x+46^{2} t^{2}-46^{2} t^{2}\right) \\
& =-\frac{1}{2 t}(x-26 t)^{2}+26^{2} t
\end{aligned}
$$

evaluation of the integral gives $\int_{-\infty}^{\infty} e^{2 \sigma x-\frac{1}{\partial t} x^{2}} d x=\int_{-\infty}^{\infty} e^{-\frac{1}{\partial t}(x-2 \sigma t)^{2}+2 \sigma^{2} t} d x$

$$
\begin{aligned}
& =e^{2 \sigma^{2} t} \rho_{-\infty}^{\infty} e^{-\frac{1}{2 t}(x-2 \sigma t)^{2}} d x \\
& =\sqrt{2 \pi t} e^{2 \sigma^{2} t}
\end{aligned}
$$

bringing things together gives

$$
\begin{aligned}
E\left[\delta^{2}(t)\right] & \\
& =\frac{\delta^{2}(0)}{\sqrt{2 \pi t}} e^{\left[\left(2 \mu-\sigma^{2}\right) t\right]} e^{2 \sigma^{2} t} \frac{\pi}{\sqrt{2 \pi t}} \\
& =s^{2}(0) e^{2 \mu t-\sigma^{2} t+2 \sigma^{2} t} \\
& =s^{2}(0) e^{2 \mu t+\sigma^{2} t}
\end{aligned}
$$

Now
$\operatorname{Var}(s(t))=E\left[s^{2}(t)\right] \cdot E^{2}[s(t)]$

$$
\begin{aligned}
& =s^{2}(0) e^{2 \mu t+\sigma^{2} t}-s^{2}(0) e^{2 \mu t} \\
& =s^{2}(0) e^{2 \mu t}\left(e^{\sigma^{2} t}-1\right)
\end{aligned}
$$

Thus for

$$
\begin{aligned}
& S(t)=S(0) \exp \left[\mu t-\frac{1}{2} \sigma^{2} t+\sigma \omega(t)\right] \\
& E[S(t)]=S(0) e^{\mu t} \\
& \operatorname{var}[S(t)]=S^{2}(0) e^{2 \mu t}\left(e^{\sigma^{2} t}-1\right)
\end{aligned}
$$

## Exercise

Find an equation satisfied by

$$
s(t)=s(0) e^{\mu t+\sigma \omega(t)}
$$

solution
Recall that the Itô formula
for a function of an It 6 process $F(t, \bar{X}(t))$ is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here $a(t)=0$ and $b(t)=1$ so that

$$
\begin{aligned}
& d F(t, \omega(t))=F_{t}(t, \omega(t)) d t \\
& +F_{x}(t, \omega(t)) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \omega(t)) d t
\end{aligned}
$$

Now usins $s(t, \omega(t))=F(t, \omega(t))$

$$
\begin{aligned}
& F_{t}(t, \omega(t))=\frac{\partial}{\partial t} s(t, \omega(t)) \\
& =\frac{\partial}{\partial t} s(0) e^{\mu t+\sigma \omega(t)} \\
& =\mu s(0) e^{\mu t+\sigma \omega(t)} \\
& =\mu s(t) \\
& F_{x}(t, \omega(t))=\frac{\partial}{\partial \omega(t)} s(t, \omega(t)) \\
& =\frac{\partial}{\partial \omega(t)} s(0) e^{\mu t+\sigma \omega(t)} \\
& =\sigma s(0) e^{\mu t+\sigma \omega(t)} \\
& =\sigma s(t) \\
& F_{x x}(t, \omega(t))=\frac{\partial^{2}}{\partial \omega^{2}(t)} s(t, \omega(t)) \\
& =\frac{\partial^{2}}{\partial \omega^{2}(t)} s(0) e^{\mu t+\sigma \omega(t)}
\end{aligned}
$$

$$
\begin{aligned}
= & \sigma^{2} s(\sigma) e^{\mu t+\sigma \omega(t)} \\
= & \sigma^{2} s(t) \\
s o, & \\
d s(t)= & \mu s(t) d t+\sigma s(t) d \omega(t) \\
& +\sigma^{2} s(t) d t \\
= & \left(\mu+\sigma^{2}\right) s(t) d t+\sigma s(t) d \omega(t) \\
\text { Finally, } & \\
d s(t)= & \left(\mu+\sigma^{2}\right) s(t) d t+\sigma s(t) d \omega(t)
\end{aligned}
$$

Exercise
snow that

$$
\begin{aligned}
& s(t)=s(0) \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
& \left.+\int_{0}^{t} \sigma(s) d \omega(s)\right\}
\end{aligned}
$$

is a solution to the equation

$$
d s(t)=\mu(t) s(t) d t+\sigma(t) s(t) d \omega(t)
$$

## Solution

Recall that the Its formula for a function of an It $\hat{b}$ process $F(t, \bar{X}(t))$ is given by

$$
\begin{aligned}
& d \bar{X}(t)=a(t) d t+b(t) d \omega(t) \\
& d F(t, \bar{X}(t))=F_{t}(t, \bar{X}(t)) d t \\
& +F_{x}(t, \bar{X}(t)) a(t) d t \\
& +F_{x}(t, \bar{X}(t)) b(t) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \bar{X}(t)) b^{2}(t) d t
\end{aligned}
$$

Here $a(t)=0$ and $b(t)=1$ so that

$$
d F(t, \omega(t))=F_{t}(t, \omega(t)) d t
$$

$$
\begin{aligned}
& +F_{x}(t, \omega(t)) d \omega(t) \\
& +\frac{1}{2} F_{x x}(t, \omega(t)) d t
\end{aligned}
$$

Now usins $s(t, \omega(t))=F(t, \omega(t))$

$$
\begin{aligned}
& F_{t}(t, \omega(t))=\frac{\partial}{\partial t} s(t, \omega(t)) \\
& =\frac{\partial}{\partial t} s(t) \\
& =\frac{\partial}{\partial t} s(0) \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
& \left.\quad+\int_{0}^{t} \sigma(s) d \omega(s)\right\}
\end{aligned} \quad \begin{aligned}
& s(0)\left(\mu(t)-\frac{1}{2} \sigma^{2}(t)\right) \\
& \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s+\int_{0}^{t} \sigma(s) d \omega(s)\right\} \\
& =\left(\mu(t)-\frac{1}{2} \sigma^{2}(t)\right) s(t)
\end{aligned}
$$

and

$$
\begin{aligned}
& \frac{\partial s(t)}{\partial \omega(t)}= \frac{\partial}{\partial \omega(t)} \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
&\left.+\int_{0}^{t} \sigma(s) d \omega(s)\right\} \\
&=s(0) \sigma(t) \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \sigma^{2}(s)\right) d s\right. \\
&+\left.\int_{0}^{t} \sigma(s) d \omega(s)\right\} \\
&=\sigma(t) s(t)
\end{aligned}
$$

and finally

$$
\begin{aligned}
\frac{\partial^{2}}{\partial \omega^{2}(t)} s(t) & =\frac{\partial^{2}}{\partial \omega^{2}(t)} s(0) \exp \left\{\int_{0}^{t}\left(\mu(s)-\frac{1}{2} \theta^{2}(s)\right) d s\right. \\
& \left.+\int_{0}^{t} \sigma(s) d \omega(s)\right\}
\end{aligned}
$$

$$
=\sigma^{2}(t) s(t)
$$

bringing things together gives

$$
\begin{aligned}
& d s(t)=\left(\mu(t)-\frac{1}{2} \sigma^{2}(t)\right) s(t) d t \\
& \quad+\sigma(t) s(t) d \omega(t)+\frac{1}{2} \sigma^{2}(t) s(t) d t \\
& \quad=\mu(t) s(t) d t+\sigma(t) s(t) d \omega(t)
\end{aligned}
$$

Thus the desired result is ditained.

## Exercise

A solution to the langevine equation,

$$
d \bar{X}(t)=\mu \bar{X}(t) d t+\sigma d \omega(t)
$$

show that the Ornstein-unlenbeck process

$$
\bar{X}(t)=\bar{X}(0)+\int_{0}^{t} e^{\mu(t-s)} \sigma d \omega(s)
$$

is a solution to the langivine equation.

## Solution

Consider

$$
\begin{gathered}
d\left(e^{-\mu t} \bar{X}(t)\right)=-\mu e^{-\mu t} \bar{X}(t) d t \\
+e^{-\mu t} d \bar{X}(t)
\end{gathered}
$$

but

$$
d \bar{x}(t)=\mu \bar{x}(t) d t+\sigma d \omega(t)
$$

SO

$$
\begin{aligned}
& d\left(e^{-\mu t} \bar{x}(t)\right)=-\mu e^{-\mu t} \bar{x}(t) d t \\
& +e^{-\mu t}(\mu \bar{x}(t) d t+\sigma d \omega(t) \\
& =-\mu e^{-\mu t} \bar{x}(t) d t+e^{-\mu t} \mu \bar{x}(t) d t \\
& \quad+\sigma e^{-\mu t} d \omega(t)
\end{aligned}
$$

$\Rightarrow d\left(e^{-\mu t} \bar{x}(t)\right)=\sigma e^{-\mu t} d \omega(t)$
integrating gives
$\int_{0}^{t} d\left(e^{-\mu t} \bar{X}(t)\right)=\int_{0}^{t} \sigma e^{-\mu s} d \omega(s)$
$\Rightarrow e^{-\mu t} \bar{x}(t)-\bar{x}(0)=\int_{0}^{t} \sigma e^{-\mu s} d \omega(s)$
$\Rightarrow \bar{X}(t)=\bar{X}(0) e^{\mu t}+\sigma \int_{0}^{t} e^{\mu(t-s)} d \omega(s)$
which is the desired result.

