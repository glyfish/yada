Problems and Solutions in Mathematical Finance stochastic Calculus volume '1

$$
\begin{aligned}
& \text { Troy Stribling } \\
& \text { Feb. } 272017
\end{aligned}
$$

* Problem Set 1,2

1) De Morgan's Law. Let

$$
A_{i} \quad i \in I
$$

Show that

$$
\begin{aligned}
& \left(\bigcup_{i \in I} A_{i}\right)^{c}=\bigcap_{i \in I} A_{i}^{c} \\
& \left(\bigcap_{i \notin I} A_{i}\right)^{c}=\bigcup_{i \in I} A_{i}^{c}
\end{aligned}
$$

where $A_{i}^{c}$ is the complimet of $A_{i}$ let $a \in\left(\cup_{i \in I} A_{i}\right)^{c}$ then
$a \notin \bigcup_{i \in I} A_{i}$ so $a \notin A_{i} \forall i \in I$ it follows $a \in A_{i}^{c} \forall i \in I$
so $\quad\left(\bigcup_{i \in I} A_{i}\right)^{c} \subseteq \bigcap_{i \in I} A_{i}^{c}$
Like wise if $a \in \bigcap_{i \in I} A^{r} i$ then $a \in A_{i}^{c} \forall i \in I$ it follows that $a_{i} \in A_{i} \forall i \in I$. so

$$
\begin{aligned}
& a_{i} \notin \bigcup_{i \in I} A_{i} \Rightarrow a_{i} \in\left(\bigcup_{i \in I} A_{i}\right)^{c} \\
& \text { Thus } \bigcap_{i \in I} A_{i}^{c} \subseteq\left(\bigcup_{i \in I} A_{i}\right)^{c} \\
& \text { and } \bigcap_{i=I} A_{i}^{c}=\left(\bigcup_{i=I} A_{i}\right)^{c}
\end{aligned}
$$

To prove the second identity

$$
\left(\bigcap_{i \in I} A_{i}\right)^{c}=\bigcup_{i \in I} A_{i}^{c}
$$

use the first

$$
\bigcap_{i \in I} A_{i}^{c}=\left(\bigcup_{i \in I} A_{i}\right)^{c}
$$

replace $A_{i}$ with $A_{i}^{e}$

$$
\begin{aligned}
\bigcap_{i \in I}\left(A_{i}^{c}\right)^{c} & =\left(\bigcup_{i \in I} A_{i}^{c}\right)^{c} \\
\Rightarrow \bigcap_{i \in I} A_{i} & =\left(\bigcup_{i \in I} A_{i}^{c}\right)^{c}
\end{aligned}
$$

After taking the compliment of both sides

$$
\left(\bigcap_{i \in I} A_{i}\right)^{c}=\bigcup_{i \in I} A_{i}^{c}
$$

which is the desired result
2) Let $\mathfrak{F}$ be a $\sigma$-algebra of subsets of the sample space $\Omega$.

Show that if $A_{1}, A_{2}, A_{3} \ldots \in \mathcal{F}$ then

$$
\bigcap_{i=1}^{\infty} A_{i} \in \mathcal{F}
$$

A sample space $\Omega$ is a set of all possible outcomes of an experiement or random trial. A field is a collection $\mathcal{F}$ of subsets of $\Omega$ that satisfy,

1. $\phi \in \mathcal{F}$ where $\phi$ is the empty set
2. If $A \in \mathcal{F}$ then $A^{c} \in \mathcal{F}$ where $A^{c}$ is the complement of $A$ in $\Omega$
3. If $A_{1}, A_{2}, \ldots, A_{n} \in \mathcal{F}$, for $n>2$

$$
\bigcup_{i=1}^{n} A_{i} \in \tilde{F}
$$

$\mathcal{F}$ is closed under unions

* A $\sigma$-algebra on $\Omega$ is a field $F$ which contains a countably $/ \in \mathcal{F}$ infinite number of sets $A_{1}, A_{2} \ldots$
which are closed under countable unions

$$
\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{F}
$$

If $\mathcal{F}$ is a $\sigma$-algebra of subsets of the sample space $\Omega$ show that if $A_{1}, A_{2}, \ldots \in \mathcal{F}$ then

$$
\bigcap_{i=1}^{\infty} A_{i} \in \mathcal{F}
$$

From the definition of a $\sigma$-algebra

$$
\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{F}
$$

and

$$
\bigcup_{i=1}^{\infty} A_{i}^{c} \in \mathcal{F}
$$

and

$$
\left(\bigcup_{i=1}^{\infty} A_{i}^{c}\right)^{c} \in \mathcal{F}
$$

From De Morgarls Laws

$$
\begin{aligned}
\left(\bigcup_{i=1}^{\infty} A_{i}\right)^{c} & =\bigcap_{i=1}^{\infty} A_{i}^{c} \\
\Rightarrow\left(\bigcup_{i=1}^{\infty} A_{i}^{c}\right)^{c} & =\bigcap_{i=1}^{\infty}\left(A_{i}^{c}\right)^{c}=\bigcap_{i=1}^{\infty} A_{i}
\end{aligned}
$$

Trus

$$
\bigcap_{i=1}^{\infty} A_{i} \in \tilde{f}
$$

3) Show that if $\mathcal{F}$ is a 0 -algebra of subsets of $\Omega$ then

$$
\{\phi, \Omega\} \in \tilde{\mathcal{F}}
$$

From the definition of a $\sigma$-algebra

$$
A \in \mathcal{F} \Rightarrow A^{c} \in \mathcal{F}
$$

so since

$$
\phi \in \mathcal{F} \quad \Rightarrow \phi^{c}=\Omega \in \mathcal{F}
$$

it follows

$$
\phi \cup \Omega=\{\phi, \Omega\} \in \mathcal{F}
$$

4) Snow that if $A \subseteq \Omega$ then

$$
\tilde{\mathcal{F}}=\left\{\phi, \Omega, A, A^{c}\right\}
$$

is a $\sigma$-algebra
$\tilde{f}$ is a 6-algebra because of the following
a) $\phi \in \mathcal{F} \Rightarrow \phi^{c}=\Omega \in \mathcal{F}$
b) $\phi^{c}=\Omega \Rightarrow \phi=\Omega^{c}$
$\phi \in \mathcal{F}$ and $\Omega \in \mathcal{F}$,
$A \in \mathcal{F}$ and $A^{C} \in \mathcal{F}$,
$A C \in \mathcal{F}$ and $\left(A^{c}\right)^{c}=A^{\prime} \in \mathcal{F}$
c) show that $\left\{\varnothing, \Omega, A, A^{\prime}\right\}$ is closed under unions

$$
\begin{array}{ll}
\varnothing \cup \Omega=\Omega \epsilon \mathcal{F} & \varnothing \cup A=A \in \mathcal{F} \\
\varnothing \cup A^{c}=A^{c} \in & A \cup \Omega=\Omega \in \mathcal{F} \\
A^{c} \cup \Omega=\Omega \in \mathcal{F} & \varnothing \cup A \cup \Omega=\Omega \in \mathcal{F} \\
\varnothing \cup A^{c} \cup \Omega \in \mathcal{F} & \Omega \quad A \cup A^{c}=\Omega \in \mathcal{F} \\
A \cup A^{c} \in \Omega \in \mathcal{F} &
\end{array}
$$

5) Let $\left\{\mathfrak{F}_{i}\right\}_{i \in I} I \neq \varnothing$ be a famith of $\sigma$-algebras of subsets of the sample space $\Omega$.
Snow that $\tilde{f}=\bigcap_{i \in I} \widetilde{f}_{i}$ is also
a $\sigma$-clgebra of subsets of $\Omega$.
It will follow that $F=\bigcap_{i=I} F_{i}$ is a $\sigma$-algebra from
a) Since $\tilde{\mathcal{F}}_{i} c \in I$ is a $\delta$-algebra $\phi \in \mathcal{F}_{i} \quad \forall i \in I$
b) If $A \in \mathcal{F}_{i} \forall i \in I$ then $A^{c} \in \mathcal{F}_{i} \forall i \in I$ berause $\mathcal{F}_{i}$ is a $\sigma$-algebra that
c) If $A_{1}, A_{2}, \ldots \in \tilde{Э}_{i} \forall i \in I$
then $\bigcup_{j=1}^{\infty} A_{j} \in \mathcal{F}_{i}$ because $\mathcal{F}_{i}$ is a 6 algebra
$a, b$ and $c$ imply the

$$
J=\bigcap_{i \in I} \mathcal{F}_{i}
$$

is a $\sigma$-algebra
6) Let $\Omega=\{\alpha, \beta, \gamma\}$ and let

$$
\begin{aligned}
& \widetilde{F}_{1}=\{\phi, \Omega,\{\alpha\},\{\beta, r\}\} \\
& \widetilde{F}_{2}=\{\phi, \Omega,\{\alpha, \beta\},\{\gamma\}\}
\end{aligned}
$$

i) Show that $\mathfrak{F}_{1}$ and $\mathfrak{F}_{2}$ are - algebras

For $\mathfrak{J}_{1}$

$$
\begin{aligned}
& \{\alpha\}^{c}=\{\beta, \gamma\},\{\beta, \gamma\}^{c}=\{\alpha\} \\
& \{\alpha\} \cup\{\beta, \gamma\}=\{\alpha, \beta, \gamma\}=\Omega \\
& \varnothing \cup\{\alpha\}=\{\alpha\}, \phi \cup\{\beta, \gamma\}=\{\beta, r\} \\
& \{\alpha\} \cup \Omega=\Omega,\{\beta, \gamma\} \cup \Omega=\Omega
\end{aligned}
$$

Tnese taken together imply that $\mathcal{F}_{1}$ is a o-algebra
Similarly for $\mathfrak{F}_{2}$
$\{\gamma\}^{c}=\{\alpha, \beta\}, \quad\{\alpha, \beta\}^{c}=\{\gamma\}$
$\{\gamma\} \cup\{\alpha, \beta\}=\{\alpha, \beta, \gamma\}=\Omega$
$\varnothing \cup\{\gamma\}=\{r\}, \phi \cup\{\alpha, \beta\}=\{\alpha, \beta\}$
$\Omega \cup\{\gamma\}=\Omega, \Omega \cup\{\alpha, \beta\}=\Omega$
so $\tilde{F}_{2}$ is a $\sigma$-algebra.
ii) $\frac{\operatorname{Is}}{\text { of }} \mathcal{F}=\mathcal{F}_{1} \cup \mathcal{F}_{2}$ a 0 -algebra

$$
\begin{gathered}
\tilde{J}=\tilde{f}_{1} \cup \tilde{f}_{2}=\{\phi, \Omega,\{\alpha\},\{\beta, \gamma\}\} \cup \\
=\{\phi, \Omega,\{\alpha, \beta\},\{\gamma\}\} \\
=\{\phi,\{\alpha\},\{\gamma\},\{\beta, \gamma\},\{\alpha, \beta\}\}
\end{gathered}
$$

berify that $f$ is closed under union.

$$
\{\alpha\} \cup\{\gamma\}=\{\alpha, \gamma\} \notin \mathcal{F}
$$

Trus $\mathcal{F}$ is not a G-algebra of subsets of $\Omega$.

* The pair $(\Omega, F)$ is called a neasurable space. A probability mpasure $P$ on a measureable space $(\Omega, \mathcal{F})$ is a function

$$
P: \widetilde{F} \mapsto[0,1]
$$

such that
a) $P(\phi)=0$
b) $P(\Omega)=1$
$c)$ if $A_{1}, A_{2}, \ldots \in \mathcal{F}$ and $\left\{A_{i}\right\}_{i=1}^{\infty}$ is disjoint such that

$$
A_{i} \cap A_{j}=\varnothing \text { if } i \neq j
$$

then

$$
P\left(\cup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)
$$

The triple $(\Omega, 7, P)$ is called a probability space.
It is a complete probibility space if $\mathcal{F}$ also contains
subsets $B$ of $\Omega \quad P$ - outer measure, $P^{*}$, zero, namely

$$
P^{*}(B)=\inf [P(A): A \in \mathcal{F}, B(A)]=0
$$

inf is the infumum of a subset $A$ of a partially ordered set $B$ is the greatest element in $T$ that is less than or equal to all elemets in A.
The sup is the supremum of $a$ subset $B$ of $A$ is the smallest element in $B$ that is agreater than all elements in A

* Let $\Omega$ be a non-epty sample space and $T$ be a fixed positive numeber and assume that for each $t \in[0, T]$ there is a $\sigma$-algebra $\tilde{f}_{t}$ in addition assume that if sat the every set in $\tilde{f}_{s}$ is in $\tilde{\mathcal{F}} t$,

$$
\mathcal{F}_{s} \subseteq \mathcal{F}_{t}
$$

The collection of $\sigma$-algebras, $\mathcal{F}_{t}$, $0 \leqslant t \leqslant T$ is called a fitration

A random variable $x$ is defined by.
Let $\Omega$ be sample space at let $₹$ be a $\sigma$-algebra of subsets of $\Omega$. A real valued randan variable $X$ is a function

$$
X: \Omega \rightarrow \mathbb{R} \quad \mathbb{R}=\text { real numbers }
$$

such trat

$$
\{\omega \in \Omega: x(\omega) \leqslant x\}
$$

for each $x \in \mathbb{R}$ it is said that $X$ if $\mathcal{F}$ measurable.

A adaped stochcasiti process is one that cannot see into the future.

Let $\Omega$ be a non-empty sample space with a filtration $\mathcal{F}_{t}$ ) $t \in[0, T]$ and let $X$ be a collection of random variables indexed by $t \in[0, T]$. It is said trat $x_{t}$ is an adapted if for each $t \quad x_{t}$ is $F_{i}$ measurable
8) Let $(\Omega, F, P)$ be a probability space and let

$$
Q: \mathcal{F} \rightarrow[0,1]
$$

be defined by

$$
Q(A)=P(A \mid B)
$$

where $B \in \mathcal{F}$ such that $P(B)>0$.
Show that $(\Omega, F, Q)$ is
also a probability space.
A probability space is defined
by
$P(\phi)=0$
$P(\Omega)=1$
$A_{1}, A_{2}, \ldots \in \mathcal{F}$ and $A_{i} \cap A_{j}=\varnothing \quad i t j$
then $P\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} P\left(A_{i}\right)$
So

$$
Q(A)=P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

Now

$$
\Phi \cap B=\Phi \quad \Omega \cap B=B
$$

and
a) $Q(\phi)=\frac{P(\phi \cap B)}{P(B)}=\frac{P(\phi)}{P(B)}=0$
b) $Q(\Omega)=\frac{P(\Omega \cap B)}{P(B)}=\frac{P(B)}{P(B)}=1$
if $\quad A_{i} \cap A_{j}=\varnothing \quad$ if $\quad i \neq j$
$Q\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\frac{P\left[\left(\bigcup_{i=1}^{\infty} A_{i}\right) \cap B\right]}{P(B)}$
$=\frac{P\left[\bigcup_{i=1}^{\infty}\left(A_{i} \cap B\right)\right]}{P(B)}$
Consider $i \neq j$ where $A_{i} \cap A_{j}=\varnothing$

$$
\left(A_{i} \cap B\right) \cap\left(A_{j} \cap B\right)
$$

using $a_{i} \in A_{i}, a_{i} \in B, a_{i} \notin a_{j}$

$$
\begin{aligned}
& a_{i} \in\left(A_{i} \cap B\right) \\
& a_{i} \notin\left(A_{j} \cap B\right)
\end{aligned}
$$

thes

$$
\left(A_{i} \cap B\right) \cap\left(A_{j} \cap B\right)=\varnothing
$$

So

$$
P \frac{\left[\bigcup_{i=1}^{\infty}\left(A_{i} \cap B\right)\right]}{P(B)}=\sum_{i=1}^{\infty} \frac{P\left(A_{i} \cap B\right)}{P(B)}
$$

## Thus

c) $Q\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} Q\left(A_{i}\right)$

From $a, b$ and $c$ if follows trat

$$
(\Omega, \tilde{\mathcal{F}}, Q)
$$

is a probability space
9) Prove Bode's Inequality - Suppose

$$
\left\{A_{i}\right\}_{i \in L} \quad I=1,2,3, \ldots
$$

is a countable callection of events Show that

$$
P\left(\bigcup_{i \in I} A_{i}\right) \leq \sum_{i \in I} P\left(A_{i}\right)
$$

Let

$$
B_{i}=A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}
$$

It can be shown that

$$
B_{i} \cap B_{i}=\varnothing \quad i \neq y
$$

and

$$
\bigcup_{i \in I} B_{i}=\bigcup_{i \in I} A_{i}
$$

(see Probability of Set Difference in Micellaneass Mat)
then

$$
\begin{aligned}
& P\left(\bigcup_{i \in I}^{\cup} A_{i}\right)=P\left(\bigcup_{i \in I} B_{i}\right) \\
& \text { since } B_{i} \cap B_{j}=\varnothing \quad i \neq j \\
& P\left(\bigcup_{i \in I} B_{i}\right)=\sum_{i \in I} P\left(B_{i}\right) \\
&=\sum_{i \in I} P\left(A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right)
\end{aligned}
$$

but

$$
\begin{aligned}
& P\left(A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right) \\
& =P\left(A_{i}\right)-P\left[A_{i} \cap\left(A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right)\right]
\end{aligned}
$$

but

$$
P\left[A_{i} \cap\left(A_{1} \cup A_{2} \cup \cdots \cup A_{c-1}\right)\right] \geqslant 0
$$

from the definition of probability

## Thus

$$
\begin{aligned}
& P\left(\bigcup_{i \in I} A_{i}\right)=\sum_{i \in I} P\left(A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right) \\
& =\sum_{i \in I} P\left(A_{i}\right)-P\left[A_{i} \cap\left(A_{1} \cup A_{2} \cup \cdots \cup A_{i-1}\right)\right] \\
& \quad \leqslant \sum_{i \in I} P\left(A_{i}\right)
\end{aligned}
$$

ov

$$
P\left(\cup_{i \in I} A_{i}\right) \leqslant \sum_{i \in I} P\left(A_{i}\right)
$$

10) Prove Bonferroni's Inequality which is defined by

$$
P\left(\bigcap_{i \in I} A_{i}\right) \geqslant 1-\sum_{i \in I} P\left(A_{i}^{c}\right)
$$

where $\left\{A_{i}\right\}_{i \in I}$
Using De Morgan's Law

$$
\begin{aligned}
& \left(\bigcap_{i \in I} A_{i}\right)^{c}=\bigcup_{i \in I} A_{i}^{c} \\
\Rightarrow & \bigcap_{i \in I} A_{i}=\left(\bigcup_{i \in I} A_{i}^{c}\right)^{c}
\end{aligned}
$$

so

$$
\begin{aligned}
& P\left(\bigcap_{i \in I} A_{i}\right)=P\left[\left(\bigcup_{i \in I} A_{i}^{c}\right)^{c}\right] \\
& =1-P\left(\bigcup_{i \in I} A_{i}^{c}\right)
\end{aligned}
$$

From Bode's Inequality

$$
P\left(\bigcup_{i \in I} A_{i}\right) \leqslant \sum_{i \in I} P\left(A_{i}\right)
$$

The desired result follows

$$
P\left(\bigcup_{i \in I} A_{i}\right) \geqslant 1-\sum_{i \in I} P\left(A_{i}\right)
$$

11) Bayes Formula

Let $A_{1}, A_{2}, \ldots, A_{n}$ be a partion of $\Omega$ where

$$
\begin{aligned}
& \bigcup_{i=1}^{n} A_{i}=\Omega \\
& A_{i} \cap A_{j}=\varnothing \quad i \neq j
\end{aligned}
$$

and the probability $P\left(A_{i}\right)>0$ Show that

$$
P\left(A_{i} \mid B\right)=\frac{P\left(B \mid A_{i}\right) P\left(A_{i}\right)}{P(B)}
$$

where

$$
P(B)=\sum_{j=1}^{r} P\left(B \mid A_{j}\right) P\left(A_{j}\right)
$$

Conditional Probability is defined by

$$
P\left(A_{i} \mid B\right)=\frac{P\left(A_{i} \cap B\right)}{P(B)}
$$

SC

$$
P\left(B \mid A_{i}\right)=P\left(\frac{A_{i} \cap B}{P\left(A_{i}\right)}\right)
$$

$$
\Rightarrow P\left(A_{i} \cap B\right)=P\left(B \mid A_{i}\right) P\left(A_{i}\right)
$$

then

$$
P\left(A_{i} \mid B\right)=\frac{P\left(B \mid A_{i}\right) P\left(A_{i}\right)}{P(B)}
$$

Also since

$$
A_{i} \cap A_{j}=\varnothing \quad i \neq j
$$

and

$$
\begin{aligned}
& \bigcup_{i=1}^{n} A_{i}=\Omega \\
B= & B \cap \Omega=B \cap \bigcup_{i=1}^{n} A_{i} \\
= & \bigcup_{i=1}^{n}\left(B \cap A_{i}\right)
\end{aligned}
$$

50

$$
\begin{aligned}
P(B) & =P\left[\bigcup_{i=1}^{n}\left(B \cap A_{i}\right)\right] \\
& =\sum_{i=1}^{n} P\left(B \cap A_{i}\right)
\end{aligned}
$$

since

$$
A_{i} \cap A_{j}=\varnothing
$$

Using

$$
P\left(B \cap A_{i}\right)=P\left(B \mid A_{i}\right) P\left(A_{i}\right)
$$

gives

$$
P(B)=\sum_{i=1}^{n} P\left(B \mid A_{i}\right) P\left(A_{i}\right)
$$

12) Principle of Inclusion and Exclusion for Probability

* Show that

$$
P\left(A_{1} \cup A_{2}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)-P\left(A_{1} \cap A_{2}\right)
$$

Now using

$$
\begin{aligned}
& B_{i}=A_{i} \backslash A_{1} \cup A_{2} \cup \cdots \cup A_{i-1} \\
& B_{i} \cap B_{j}=\varnothing \quad i \neq j \\
& \bigcup_{i=1}^{n} B_{i}=\bigcup_{i=1}^{n} A_{i}
\end{aligned}
$$

( see Prologitily of set Difference in Micellaneous Math)
To rewrite $A_{1} \cup A_{2}$ as a union of disjoint sets

## gives

$$
\begin{aligned}
& B_{1}=A_{1} \\
& B_{2}=A_{2} \backslash A_{1}
\end{aligned}
$$

so

$$
A_{1} \cup A_{2}=B_{1} \cup B_{2}=A_{1} \cup\left(A_{2} \backslash A_{1}\right)
$$

It follows that

$$
\begin{aligned}
& P\left(A_{1} \cup A_{2}\right)=P\left[A_{1} \cup\left(A_{2} \backslash A_{1}\right)\right] \\
& =P\left(A_{1}\right)+P\left(A_{2} \backslash A_{1}\right)
\end{aligned}
$$

using

$$
A_{2} \backslash A_{1}=A_{2} \cap A_{1}^{c}
$$

( see Probability of set Difference in Micellaneous Math)

$$
P\left(A_{1} \cup A_{2}\right)=P\left(A_{1}\right)+P\left(A_{2} \cap A_{1}^{c}\right)
$$

but

$$
A_{2}=\left(A_{2} \cap A_{1}\right) \cup\left(A_{2} \cap A_{1}^{c}\right)
$$

so

$$
P\left(A_{2}\right)=P\left(A_{2} \cap A_{1}\right)+P\left(A_{2} \cap A_{1}^{c}\right)
$$

$\Rightarrow P\left(A_{2} \cap A_{1}^{c}\right)=P\left(A_{2}\right)-P\left(A_{1} \cap A_{2}\right)$
and

$$
P\left(A_{1} \cup A_{2}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)-P\left(A_{1} \cap A_{2}\right)
$$

* Using the previous result

$$
P\left(A_{1} \cup A_{2} \cup A_{3}\right)
$$

( see Probability Sum Rule in Micellaneous Math)

* Find

$$
P\left(\bigcup_{i=1}^{n} A_{i}\right)
$$

( see Probability Sum Rule in Micellaneous Math)

* Find

$$
P\left(\bigcap_{i=1}^{n} A_{i}\right)
$$

Using De Morgan's Law

$$
\begin{aligned}
\bigcup_{i=1}^{n} A_{i}^{c} & =\left(\bigcap_{i=1}^{n} A_{i}\right)^{c} \\
\Rightarrow \quad \bigcap_{i=1}^{n} A_{i} & =\left(\bigcup_{i=1}^{n} A_{1}{ }^{c}\right)^{c} \\
\Rightarrow \quad \bigcap_{i=1}^{n} A_{i}^{c} & =\left(\bigcup_{i=1}^{n} A_{i}\right)^{c}
\end{aligned}
$$

50

$$
\begin{aligned}
& P\left(\bigcup_{i=1}^{n} A_{i}^{c}\right)=P\left[\left(\bigcap_{i=1}^{n} A_{i}\right)^{c}\right] \\
& =1-P\left(\bigcap_{i=1}^{n} A_{i}\right)
\end{aligned}
$$

For $n=2$ the sum rule Sives

$$
\begin{aligned}
& P\left(A_{1}^{c} \cup A_{2}^{c}\right)=P\left(A_{1}^{c}\right)+P\left(A_{2}^{c}\right) \\
& -P\left(A_{1}^{c} \cap A_{2}^{c}\right)
\end{aligned}
$$

Using

$$
A_{1}^{c} \cap A_{0}^{c}=\left(A_{1} \cup A_{2}\right)^{c}
$$

and

$$
P\left(A^{c}\right)=1-P(A)
$$

$$
\begin{aligned}
P\left(A_{1}^{c} \cup A_{2}^{c}\right)= & 1-P\left(A_{1} \cap A_{2}\right) \\
= & {\left[1-P\left(A_{1}\right)\right]+\left[1-P\left(A_{2}\right)\right] } \\
& -\left[1-P\left(A_{1} \cup A_{2}\right)\right] \\
\Rightarrow & P\left(A_{1} \cap A_{2}\right)-1=\left[P\left(A_{1}\right)-1\right]+\left[P\left(A_{2}\right)-1\right] \\
& -\left[P\left(A_{1} \cup A_{2}\right)-1\right] \\
\Rightarrow & P\left(A_{1} \cap A_{2}\right)=1+P\left(A_{1}\right)+P\left(A_{2}\right)-2 \\
& -P\left(A_{1} \cup A_{2}\right)+1 \\
\Rightarrow & P\left(A_{1} \cap A_{2}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)-P\left(A_{1} \cup A_{2}\right)
\end{aligned}
$$

For $A_{1} \cap A_{2} \cap A_{3}=A_{1} \cap\left(A_{2} \cap A_{3}\right)$

$$
\begin{aligned}
P & \left(A_{1} \cap A_{2} \cap A_{3}\right)=P\left(A_{1}\right)+P\left(A_{2} \cap A_{3}\right) \\
& -P\left[A_{1} \cup\left(A_{2} \cap A_{3}\right)\right] \\
= & P\left(A_{1}\right)+\left[P\left(A_{2}\right)+P\left(A_{3}\right)-P\left(A_{2} \cup A_{3}\right)\right] \\
& -P\left[\left(A_{1} \cup A_{2}\right) \cap\left(A_{1} \cup A_{3}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \quad P\left(A_{1} \cap A_{2} \cap A_{3}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)+P\left(A_{3}\right) \\
& -P\left(A_{2} \cup A_{3}\right)-\left[P\left(A_{1} \cup A_{2}\right)+P\left(A_{1} \cup A_{3}\right)\right. \\
& \left.-P\left(A_{1} \cup A_{2} \cup A_{3}\right)\right] \\
& \Rightarrow P\left(A_{1} \cap A_{2} \cap A_{3}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)+P\left(A_{3}\right) \\
& \text { - } P\left(A_{1} \cup A_{2}\right)-P\left(A_{1} \cup A_{3}\right)-P\left(A_{2} \cup A_{3}\right) \\
& +P\left(A_{1} \cup A_{2} \cup A_{3}\right) \\
& =>P\left(A_{1} \cap A_{2} \cap A_{3}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)+P\left(A_{3}\right) \\
& -\left[P\left(A_{1} \cup A_{2}\right)+P\left(A_{1} \cup A_{3}\right)+P\left(A_{2} \cup A_{3}\right)\right] \\
& +P\left(A_{1} \cup A_{2} \cup A_{3}\right) \\
& \text { To see the pattern one } \\
& \text { more step wowd be usefu } \\
& P\left(A_{1} \cap A_{2} \cap A_{3} \cap A_{4}\right)=P\left[A_{1} \cap\left(A_{2} \cap A_{3} \cap A_{4}\right)\right] \\
& =P\left(A_{1}\right)+P\left(A_{2} \cap A_{3} \cap A_{4}\right) \\
& -P\left[A_{1} \cup\left(A_{2} \cap A_{3} \cap A_{4}\right)\right] \\
& =P\left(A_{1}\right)+P\left(A_{2} \cap A_{3} \cap A_{4}\right) \\
& \text { - } P\left[\left(A_{1} \cup A_{2}\right) \cap\left(A_{1} \cup A_{3}\right) \cap\left(A_{1} \cup A_{4}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
&=P\left(A_{1}\right)+\left\{P\left(A_{2}\right)+P\left(A_{3}\right)+P\left(A_{4}\right)\right. \\
&- {\left[P\left(A_{2} \cup A_{3}\right)+P\left(A_{2} \cup A_{4}\right)+P\left(A_{3} \cup A_{4}\right)\right] } \\
&+\left.P\left(A_{2} \cup A_{3} \cup A_{4}\right)\right\}-\left\{P\left(A_{1} \cup A_{2}\right)\right. \\
&+ P\left(A_{1} \cup A_{3}\right)+P\left(A_{1} \cup A_{4}\right) \\
&- {\left[P\left(A_{1} \cup A_{2} \cup A_{3}\right)+P\left(A_{1} \cup \dot{A}_{2} \cup A_{4}\right)\right.} \\
&\left.+P\left(A_{1} \cup A_{3} \cup A_{4}\right)\right] \\
&\left.+P\left(A_{1} \cup A_{2} \cup A_{3} \cup A_{4}\right)\right\} \\
& \Rightarrow P\left(A_{1} \cap A_{2} \cap A_{3} \cap A_{4}\right)=P\left(A_{1}\right)+P\left(A_{2}\right)+P\left(A_{3}\right) \\
&+ P\left(A_{4}\right)-\left[P\left(A_{1} \cup A_{2}\right)+P\left(A_{1} \cup A_{3}\right)\right. \\
&+ P\left(A_{1} \cup A_{4}\right)+P\left(A_{2} \cup A_{3}\right)+P\left(A_{2} \cup A_{4}\right) \\
&+\left.P\left(A_{3} \cup A_{4}\right)\right]+\left[P\left(A_{1} \cup A_{2} \cup A_{3}\right)\right. \\
&+ P\left(A_{1} \cup A_{2} \cup A_{4}\right)+P\left(A_{1} \cup A_{3} \cup A_{4}\right) \\
&+\left.P\left(A_{2} \cup A_{3} \cup A_{4}\right)\right] \\
&- P\left(A_{1} \cup A_{2} \cup A_{3} \cup A_{4}\right)
\end{aligned}
$$

So for $n$ intersections

$$
\begin{aligned}
& P\left(\bigcap_{i=1}^{n} A_{n}\right)=\sum_{i=1}^{n} P\left(A_{i}\right)-\sum_{i=1}^{n-1} \sum_{j=i+1}^{n} P\left(A_{i} \cup A_{j}\right) \\
& +\sum_{i=1}^{n-2} \sum_{j=i+1}^{n-1} \sum_{k=j+1}^{n} P\left(A_{i} \cup A_{j} \cup A_{k}\right) \\
& +\sum_{i=1}^{n-3} \sum_{j=i+1}^{n-2} \sum_{k=j+1}^{n-1} \sum_{l=k+1}^{n} P\left(A_{i} \cup A_{j} \cup A_{k} \cup A_{l}\right) \\
& +\cdots+(-1)^{n+1} P\left(A_{1} \cup A_{2} \cup \cdots \cup A_{n}\right)
\end{aligned}
$$

## Weiner Process

A standard wiener process is defined by the following.
Let ( $\Omega, \mathcal{F}, P$ ) be a probability space. A stochartic process

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

is defined to be a standard wiener process if:
a) $\omega_{0}=0$ and has continous sample paths.
b) For each $t>0$ and $s>0$

$$
w_{t+s}-w_{t} \sim N(0, s)
$$

The increments are normally distributed and stationary with mean 0 and variance equal to the time increment.
c) For each $t>0$ and $s>0$

$$
\omega_{t+5}-\omega_{t} \Perp \omega_{t}
$$

The increments are independent

A wiener Process is constructed from the randow variable representing the increment

$$
z_{i}=\{-1,1\}
$$

where $P\left(z_{i}=1\right)=P\left(z_{i}=-1\right)=1 / 2$.
A symetric randsm walk is defined $b_{y}$,

$$
M_{k}=\sum_{i=1}^{k} Z_{i} \quad k=1,2,3, \ldots
$$

Where it has been assumed trat $M_{0}=0$ to satisfy the definition of a wiener process.
A scaled symetric random walk with increment

$$
\Delta t=\frac{t}{n}
$$

is defined by

$$
\omega_{t}^{n}=\frac{1}{\sqrt{n}} M_{n t}=\frac{1}{\sqrt{n}} \sum_{i=1}^{n t} Z_{i}
$$

The wiener process is btained in
$\omega_{t}^{n}$

$$
\begin{aligned}
w_{t}= & \lim _{n \rightarrow \infty} w_{t}^{n}=\lim _{n \rightarrow \infty} \frac{1}{\sqrt{n}} \sum_{i=1}^{n t} z_{i} \\
& \xrightarrow{D} N(0, t)
\end{aligned}
$$

thus the limiting distribution is normal with zeromean and Variance $t$.

A wiener process $\left\{\hat{\omega}_{t}: t \geqslant 0\right\}$ is defined from a standard wiener process by,

$$
\hat{\omega}_{i}=v+\mu t+\sigma \omega_{t}
$$

Where $v, \mu \in \mathbb{R}, \sigma>0$ and $\omega_{t}$ is a standard wiener process.

## Markou Property

Let $(\Omega, F, P)$ be a prabability space. The standard wiener process $\left\{\omega_{t}: t \geqslant 0\right\}$ is a Markov process such that the conditional distribution of $\omega_{t}$ given the filtration $F_{s}, s<t$ depends only upon $\omega_{s}$.

## Strons Markou Properly

Let $(\Omega, \mathcal{F}, P)$ be a probability space. If $\left\{\omega_{t}: t \geqslant 0\right\}$ is a standard wiener process and given $\mathcal{F}_{t}$ is a filtration upto time $t$, then

$$
\omega_{t+s} \cdot \omega_{t} \| \tilde{F}_{t}
$$

The increment occuring
$\tilde{F}_{t}{ }_{t}$ is independint or

## Problem Set 2.2

1) Let ( $\Omega, \mathcal{F}, P$ ) be a probability space. Conside a symetric random walk

$$
Z_{j}=\{1,-1\}
$$

where

$$
P\left(z_{j}=1\right)=P\left(z_{j}=-1\right)=1 / 2
$$

and the $z_{i}$ are independent

$$
z_{i} \Perp z_{j} \quad i \neq j
$$

Let

$$
0=k_{0}<k_{1}<k_{2}<\cdots<k_{i}
$$

then

$$
M_{k i}=\sum_{j=1}^{k i} z_{j} \quad i=1,2, \ldots, t
$$

where $M_{0}=0$.
Show that the symetric random walk has independent increments.

By definition

$$
M_{k_{i}}-M_{k_{i-1}}=\sum_{j=k_{i-1}}^{k_{i}} Z_{j}=S_{i}
$$

and for $m<n \quad m, n=1,2,3, \ldots, t$

$$
\begin{aligned}
& P\left(M_{k n}-M_{k n-1}=S_{n} \mid M_{k m}-M_{k m-1}=S_{m}\right) \\
= & \frac{P\left(M_{k n}-M_{k n-1}=S_{n}, M_{k m}-M_{k m-1}=S_{m}\right)}{P\left(M_{k m}-M_{k_{m-1}}=S_{m}\right)} \\
= & \frac{P\left(\sum_{j=k_{n-1}+1}^{K_{n}} Z_{j} \cap \sum_{j=k_{m-1}+1}^{K_{m}} Z_{j}\right)}{P\left(\sum_{j=k_{m-1}+1}^{K_{m}} Z_{j}\right)}
\end{aligned}
$$

Since $Z_{i} \| Z_{j} \quad i \neq j$ there are no overlapping events between $\left[K_{n-1}, K_{n}\right]$ and $\left[K_{m-1}, K_{m}\right]$
$P\left(\sum_{j=K_{n-1}}^{K_{n}} Z_{j} \cap \sum_{j=K_{m-1}}^{K_{m}} Z_{j}\right)$
$=P\left(\sum_{j=K_{n-1}}^{K_{n}} z_{j}\right) P\left(\sum_{j=K_{m-1}}^{K_{m}} z_{j}\right)$

50

$$
\begin{aligned}
& P\left(M_{k n}-M_{k n-1}=S_{n} \mid M_{k m}-M_{k m-1}=S_{m}\right) \\
& =P\left(M_{k_{n}}-M_{k_{n-1}}=S_{n}\right)
\end{aligned}
$$

Thus tre incement

$$
\begin{aligned}
& M_{K_{1}}-M_{K_{0}}, M_{K_{2}}-M_{K_{1}}, \ldots \\
& M_{K_{i}}-M_{K_{i-1}}
\end{aligned}
$$

are independent since they do not overlap.

* The mean of $\mu_{k j}-\mu_{k j-1}$
is given by

$$
E\left(M_{K_{j}}-M_{K_{j-1}}\right)=\sum_{i=K_{j-1}+1}^{K_{j}} E\left(Z_{i}\right)=0
$$

since by definition
$E\left(z_{i}\right)=0 \quad \forall i=k_{j-1}+1, k_{j-1}+2, \ldots, k_{,}$

* The variance is

$$
\operatorname{Var}\left(M_{k_{1}}-M_{k_{1}-1}\right)=\sum_{i=k_{1}+1}^{k_{1}} \operatorname{Var}\left(z_{i}\right)
$$

Sonce $Z_{i}$ is a unit normal

$$
\operatorname{Var}\left(z_{1}\right)=1
$$

80

$$
\begin{aligned}
& \operatorname{Var}\left(M_{K_{j}}-M_{K_{j-1}}\right)=\sum_{i=K_{j-1}+1}^{K_{j}}(l) \\
& =K_{j-1}-K_{j}
\end{aligned}
$$

Definition of Martingale
Let $(\Omega, \mathcal{F}, P)$ be a probability space. A stochastic process

$$
\left\{\bar{X}_{t}: t \geqslant 0\right\}
$$

is a continous time martingale if:
a) $E\left(Z_{t} \mid \tilde{J}_{s}\right)=Z_{s} \forall 0 \leqslant s \leqslant t$
b) $E\left(\left|\underline{Z}_{t}\right|\right)<\infty$
c) $X_{t}$ is $F_{t}$-adapted

## In words

A stochastic process is a martingale if the expected value at time $t>s$ conditioned on Ene time nistory at $s$, namely $\mathcal{F}_{s}$, is equal to the observation at $s$.

Let $(\Omega, \mathcal{F}, P)$ be a probability space. For a symetric random walk

$$
M_{k}=\sum_{i=1}^{k} Z_{i}
$$

with starting point $\mu_{0}=0$ and

$$
P\left(z_{i}=1\right)=P\left(z_{i}=-1\right)=1 / 2
$$

Show that $M_{k}$ is a martingale.
A martingale is defined by
a) $E\left(M_{t} \mid \tilde{F}_{s}\right)=M_{s}$
b) $E\left(\left(M_{t} \mid\right)<\infty\right.$
c) $M_{t}$ is $\mathcal{F}_{t}$ adapted
a) For $j<k, j, k \in \mathbb{Z}^{+}$(positive integer)
In problem 1 it was shown

$$
\begin{gathered}
E\left(M_{j}-M_{k}\right)=E\left(\sum_{i=k+1}^{j} Z_{i}\right) \\
=\sum_{i=k+1}^{j} E\left(Z_{i}\right) \\
=\sum_{i=j+1}^{k} \frac{1}{2}(-1)+\frac{1}{2}(1)=0
\end{gathered}
$$

Thus

$$
E\left(\mu_{k}-\mu_{j}\right)=0
$$

Now

$$
\begin{aligned}
& E\left(M_{k} \mid \tilde{f}_{j}\right)=E\left[\left(M_{k}-M_{j}+M_{j}\right) \mid \tilde{f}_{j}\right] \\
& =E\left(M_{k}-M_{j} \mid \tilde{f}_{j}\right)+E\left(M_{j} \mid \tilde{f}_{j}\right)
\end{aligned}
$$

From partial averaging property if $\mu_{j}$ is $\mathcal{F}_{j}$ measureable

$$
E\left(\mu_{j} \mid \mathcal{F}_{j}\right)=\mu_{j}
$$

By the strong Markou property

$$
\mu_{k}-\mu_{j} \Perp \mathcal{F}_{j}
$$

From independence property of conditional expectation

$$
E\left(M_{k}-M_{j} \mid F_{j}\right)=E\left(M_{k}-M_{i}\right)=0
$$

It follows that

$$
\begin{aligned}
& E\left(M_{k}\left(\mathcal{F}_{j}\right)=E\left(M_{k}-M_{j}+M_{j} \mid \mathcal{F}_{j}\right)\right. \\
& =E\left(M_{k}-M_{i}\left(\mathcal{F}_{j}\right)+E\left(M_{j} \mid \mathcal{F}_{j}\right)\right. \\
& =E\left(M_{k}-M_{j}\right)+M_{j} \\
& =M_{j}
\end{aligned}
$$

b) $E\left(\left|M_{k}\right|\right)=E\left(\left|\sum_{i=1}^{k} Z_{i}\right|\right)$

$$
\begin{aligned}
& \leq E\left(\sum_{i=1}^{k}\left|z_{i}\right|\right) \\
& =\sum_{i=1}^{k} E\left(\left|z_{i}\right|\right)
\end{aligned}
$$

This is a folded normal distribution, so for a normal distribution with mean $\mu$ and standar deviation 0 the mean of the folded Normal Astribution
$E(|\nabla|)=\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\mu\left[1-2 \Phi\left(-\frac{\mu}{\sigma}\right)\right]$
For the unit normal $z_{i} \mu=0$ and $\sigma=1$ so

$$
\begin{aligned}
& E\left(\left|z_{i}\right|\right)=\sqrt{\frac{2}{\pi}}+(0)[1-2(1 / 2)]=\sqrt{\frac{2}{\pi}} \\
& E\left(\left|M_{k}\right|\right)=\sum_{i=1}^{k} E\left(\left|z_{i}\right|\right)=k \sqrt{\frac{2}{\pi}} \leq \infty
\end{aligned}
$$

c) By definition $M_{t}$ is $\tilde{F}_{t}$ adopted since this was assumed in a .

## Change of Measure

Let $\Omega$ be a probability space and let $P$ and $Q$ be two probability measures on $\Omega$.
The Radon-Nikodym derivative is defined by

$$
Z(\omega)=\frac{Q(\omega)}{P(\omega)}
$$

such that

$$
P(z>0)=1
$$

By denoting $E^{P}$ and $E^{Q}$ as es expectations under measures $P$ and $Q$ respectively show that for any random variable I

$$
E^{Q}(\bar{X})=E^{P}(z \bar{X})
$$

and

$$
E^{p}(\overline{\underline{X}})=E^{\theta}\left(\frac{\bar{X}}{2}\right)
$$

From definition of expectation

$$
\begin{aligned}
E^{\theta}(\underline{Z}) & =\sum_{\omega \in \Omega} \underline{X}(\omega) Q(\omega) \\
& =\sum_{\omega \in \Omega} \underline{X}(\omega) z(\omega) P(\omega) \\
& =E^{P}(\Phi z)
\end{aligned}
$$

similarly

$$
\begin{aligned}
E^{P}(\underline{X}) & =\sum_{\omega \in \Omega} \underline{X}(\omega) P(\omega) \\
& =\sum_{\omega \in \Omega} \underline{X}(\omega) \frac{Q(\omega)}{Z(\omega)} \\
& =\sum_{\omega \in \Omega} \frac{X(\omega)}{\bar{Z}(\omega)} Q(\omega) \\
& =E^{\theta}\left(\frac{\bar{X}}{\bar{Z}}\right)
\end{aligned}
$$

## Conditional Probability

Let $(\Omega, F, P)$ be a probability space and let $\mathcal{D}^{\text {be }}$ a . in 2 ) are also ( $n$ ₹). If $\mathbb{I}_{A}$ is an indicator random variable for event $A$

$$
\Pi_{A}(\omega)= \begin{cases}1 & \text { if } \omega \in A \\ 0 & \text { otherwise }\end{cases}
$$

Show that

$$
E\left(\bar{I}_{A} \mid \mathscr{D}\right)=P(A \mid \mathscr{D})
$$

Let $B \in D$, then

$$
\begin{aligned}
& \Pi_{B}(\omega)= \begin{cases}1 & \omega \in B \\
0 & \text { otherwise }\end{cases} \\
& \Pi_{A}(\omega) \cap I_{B}(\omega)= \begin{cases}1 & \omega \in \text { AnB } \\
0 & \text { otherwise }\end{cases}
\end{aligned}
$$

From the partial averaging property with $B \in \&$ and $E\left(I_{A} \mid \otimes\right)$ \& measurable

$$
\int_{B} E\left(\Pi_{A} \mid \mathcal{A}\right) d P=\int_{B} I_{A} d P=\int_{\Omega} \Pi_{A} \cdot \Pi_{B} d P
$$

$$
=\int_{\Omega} \Pi_{A \cap B} d P=P(A \cap B)
$$

where use was made of

$$
\mathbb{I}_{A} \cdot \mathbb{I}_{B}=\mathbb{I}_{A \cap B}
$$

Now

$$
\begin{aligned}
P(A \cap B) & =P(A \mid B) P(B) \\
& =\int_{B} P(A \mid A) d P
\end{aligned}
$$

Trus

$$
\int_{B} E\left(I_{A} \mid \Delta\right) d P=\int_{B} P(A \mid \Delta) d P
$$

$$
E\left(\Pi_{A} \mid \mathcal{H}\right)=P(A \mid \mathcal{H})
$$

## Expectation

* Let $(\Omega, P, \mathcal{F})$ be a probability space and let $\$$ be a sub-6-algebra of 予.

If $Z_{1}, Z_{21} \ldots, \frac{X}{n}$ are integrable random variables and $c_{1}, c_{2}, \ldots, c_{n}$ are constants, show that

$$
\begin{aligned}
E & \left(c_{1} X_{1}+c_{2} X_{2}+\cdots+c_{n} \bar{\Delta}_{n} \mid \Delta\right) \\
= & c_{1} E\left(X_{1} \mid \Delta\right)+c_{2} E\left(X_{2} \mid \Delta\right)+\cdots+ \\
& c_{n} E\left(X_{n} \mid \Delta\right)
\end{aligned}
$$

Assume $E\left(c_{1} \bar{X}_{1}+c_{2} \bar{X}_{2}+\cdots+c_{n} \bar{Z}_{n} \mid \Delta\right)$ is $\mathcal{O}$ measurable and for $A \in \mathcal{A}$

$$
\begin{aligned}
\int_{A} E\left(c_{1} \bar{X}_{1}+c_{2} \bar{X}_{2}+\cdots+c_{n} \bar{X}_{n}(\Delta) d P\right. \\
=\int_{A}\left(c_{1} \bar{X}_{1}+c_{2} \bar{X}_{2}+\cdots+c_{n} \bar{X}_{n}\right) d P \\
=c_{1} \int_{A} \bar{X}_{1} d P+c_{2} \int_{A} \bar{I}_{2} d P+\cdots+ \\
c_{n} \int_{A} \underline{X}_{n} d P
\end{aligned}
$$

$$
=c_{1} E\left(\nabla_{1}(D)+c_{2} E\left(Z_{2}(D)+\cdots\right.\right.
$$

$+C_{n} E\left(\bar{X}_{2}|x\rangle\right)$

* Let $(\Omega, P, F)$ be a probability space and let $\$$ be a sub-6-algebra

If $X$ is an interable random variable such that $\underline{X} \geqslant 0$ almost surely

$$
E(\underline{x} \mid \not D) \geqslant 0
$$

Let

$$
A=\{\omega \in \Omega: E(X(D)<0\}
$$

From the definition of conditional expectation

$$
\int_{A} E(\bar{x} \mid y) d P=\int_{A} \bar{x} d P
$$

Since $\bar{X} \geqslant 0$ almost swely

$$
\int_{\Delta} X d P \geqslant 0
$$

but the definition of $A$ implies

$$
\int_{A} E(X \mid D) d P<0
$$

which is a contradiction thus

$$
P(A)=0
$$

which implies $E(X(D) \geq 0$ almost surely.

* Let $(\Omega, P, \mathcal{F})$ be a probability space and let $\$$ be a sub-6-algebra of 予.

If $\bar{X}$ and I are raterable random variables such that

$$
\bar{x} \leqslant 1
$$

almost surely then

$$
E(\bar{X} \mid \mathscr{D}) \leqslant E(\bar{I} \mid \mathcal{D})
$$

Since $E(\Sigma-I \mid \theta)$ is $\theta$ measurable for $A \in \Omega$

$$
\int_{A} E\left(\bar{X}-\bar{I}(\otimes) d P=\int_{A}(\underline{X} \cdot \bar{I}) d P\right.
$$

Since $\quad \mathbb{Z} \leqslant \mathbb{Y}$

$$
\begin{aligned}
\int_{A} E(\underline{X}-\bar{Y} \mid D) d P & \leqslant 0 \\
& \Rightarrow E(\underline{X}-\underline{Y} \mid D) \leqslant 0
\end{aligned}
$$

From Linearity of expectation

$$
\begin{aligned}
& E(I \mid \mathscr{D})-E(I \mid \mathscr{L}) \leqslant 0 \\
& \Rightarrow E(\bar{X} \mid \mathscr{D}) \leqslant E(I \mid \otimes)
\end{aligned}
$$

## Computing Expectations by Conditioning

Let $(\Omega, P, \mathfrak{J})$ be a probability space and let $\&$ be a sub-6-algebra of 寻.

Show that

$$
E[E(x \mid y)]=E(x)
$$

From the definition of partial average for $A \in \mathbb{D}$

$$
\int_{A} E(X \mid D) d P=\int_{A} Z d P
$$

using the indicator function $\Pi_{A}(\omega)$ the integrals can be writen as integration over $\Omega$

$$
\int_{\Omega} \Pi_{A} E(\Phi \mid \mathcal{D}) d P=\int_{\Omega} \Pi_{A} \bar{X} d D
$$

but

$$
E\left[\mathbb{I}_{A} E(\mathbb{Z} \mid y)\right]=\int_{\Omega} \mathbb{I}_{A} E(\mathbb{Z}(\mu) d P
$$

$$
E\left(\mathbb{I}_{A} \nabla\right)=\int_{\Omega} \mathbb{I}_{A} \bar{X} d P
$$

50

$$
E\left[\mathbb{I}_{A} E(\mathbb{X} \mid \mathscr{D})\right]=E\left(\mathbb{I}_{A} \bar{X}\right)
$$

setting $A=\Omega \Rightarrow \llbracket_{A}=1 \forall \omega \in \Omega$ thus

$$
E[E(X \mid D)]=E(X)
$$

* Takins Out what is known

Let $(\Omega, P, \vec{J})$ be a probability space and let $\$$ be a sub-6-algebra of $f$.

If $I$ and $I$ are integrable random variables and if $\bar{X}$ and $E[D(A)$ are $D$ measurable, show

$$
E(X \perp(D))=\bar{X} E(\underline{I} \mid D)
$$

since $\Sigma$ is $\&$ measurable and 2 Is given I is given
let $A \in D$
$\int_{A} E(X I \mid S) d P=\int_{A} X I d P =\overline{\underline{X}} \int_{A} \underline{V} d P=\overline{\underline{V}} \int_{A} E(\bar{Y} \mid \mathcal{D}) d P =\int_{A} \bar{X} E(\underline{Y} \mid \Delta) d P \Rightarrow E(X Y \mid D)=X E(Y \mid D)$

## * Tower Property

Let $(\Omega, P, \tilde{J})$ be a probability space and let $A$ be a
sub-6-algebra of $\hat{f}$. If $H^{15}$
a sub-o-algelona of $A$ and $\bar{I}$ is an integral random wariable, show that

$$
E[E(X \mid D) \mid H]=E(X \mid q)
$$

For an integrable random variable $\frac{7}{9+}$, by defintion $E(719 t)$ is It measurable let

$$
I=E(8 \mid S)
$$

and for $A \in 9 t$ the partial averaging property gives

$$
\int_{A} E[E(X \mid y) \mid \mathcal{H}] d P=\int_{A} E(X \mid y) d P
$$

since $A \in q!$ and $q$ is a sub-6-clgebra $D$, $H \leq D$ it follows that $A \in \mathcal{I}$

$$
\int_{A} E(X \mid Q) d P=\int_{A} X d P=\int_{A} F(I(z) d P
$$

Thus

$$
\begin{aligned}
& \int_{A} E[E(X \mid D) \mid H] d P=\int_{A} E(X \mid N) d P \\
& \Rightarrow E[E(X \mid \Sigma) \mid H]=E(X \mid H)
\end{aligned}
$$

## * Measurability

Let $(\Omega, \tau, P)$ be a probability space and let $\mathcal{Y}$ be a sub-o-algebra of $\tilde{J}$. If $\bar{X}$ is a random variable that is $\delta$ measureable show that

$$
E(X \mid z)=\bar{x}
$$

From the partial averaging properly for $A \in \Omega$

$$
\begin{aligned}
& \int_{A} E(\bar{X} \mid \Delta) d P=\int_{A} \bar{X} d P \\
\Rightarrow & \int_{A}[E(\underline{X} \mid \Delta)-\underline{X}] d P=0 \\
\Rightarrow & E(\underline{X} \mid D)-\bar{X}=0 \\
\Rightarrow & E(\bar{X}(D)=\underline{\bar{X}}
\end{aligned}
$$

## * Independence

Let $(\Omega, \mathcal{F}, P)$ be a probability space and \& be a sub-s-algebra of $\mathcal{F}$. Let $\bar{I}=I_{B}$ where

$$
I_{B}(\omega)= \begin{cases}1 & \omega \in B \\ 0 & \text { otherwise }\end{cases}
$$

and $\Psi_{B}$ is independent of I show that

$$
E(\bar{X} \mid \mathscr{S})=E(\bar{X})
$$

Since $E(X)$ is not a random variable it is $\&$ measureable

For $A \in \mathcal{A}$ we need to show

$$
\int_{A} E(\underline{x}) d P=\int_{A} \underline{x} d P=\int_{A} E(\nabla(\Delta)) d P
$$

Let $X=\mathbb{I}_{B}$

$$
I_{B}(\omega)= \begin{cases}1 & \omega \in B \\ 0 & \text { otherwise }\end{cases}
$$

where $I_{B}$ is independent of $\mathcal{L}$. Additionally let

$$
\Pi_{A}(\omega)= \begin{cases}1 & \omega \in A \\ 0 & \text { otherwise }\end{cases}
$$

where $I_{A}$ is $\&$ measureable. For all $A \in \mathcal{N}$

Now
$\int_{A} \bar{X} d P=\int_{A} \Pi_{B} d P=\int_{\Omega} \Pi_{B} \Pi_{A} d P$
$=\int_{\Omega} \mathbb{I}_{A \cap B} d P=P(A \cap B)$
Since $A$ and $B$ are independent

$$
P(A \cap B)=P(A) P(B)
$$

and using
$E(X)=E\left(\mathbb{I}_{B}\right)=P(B)(1)+P\left(B^{c}\right)(0)=P(B)$

Thus

$$
\begin{aligned}
& \int_{A} E(\underline{X} \mid \mathcal{J}) d P=\int_{A} \bar{X} d P=P(A \cap B) \\
& =P(B) P(A)=E(\underline{X}) \int_{A} d P \\
& =\int_{A} E(\underline{X}) d P \\
& \Rightarrow \int_{A} E(\underline{X} \mid \Delta) d P=\int_{A} E(\bar{X}) d P \\
& =0 \quad E(\underline{X} \mid \mathscr{D})=E(\underline{X})
\end{aligned}
$$

## * Conditional Jensen's Inequality

Let $(\Omega, \vec{J}, P)$ be a probability space and 21 a subo S-algebra of $\mathfrak{F}$. If a convex function

$$
\varphi: \mathbb{R} \rightarrow \mathbb{R}
$$

and \& an integrable random variable show that

$$
E[\varphi(\bar{x}) \mid \Delta] \geqslant \varphi[E(\bar{x} \mid \mathscr{y})]
$$

Deduce that if I is independent of $I$ the above inequality becomes

$$
E[\varphi(X)] \geqslant \varphi[E(X)]
$$

Now given that $q(x)$ is a convex function

$$
\phi(x) \geqslant \varphi(y)+(y-x) \phi^{\prime}(y)
$$

let $x=\Phi$ and $y=E(X|S|)$
$\varphi(X) \geqslant \varphi[E(X \mid \nmid D)]+\varphi^{\prime}[E(X \mid \delta)][E(X \mid, d)-X]$
Taking expectations

$$
\begin{aligned}
& E[\varphi(X) \mid \delta] \geqslant E\{\varphi[E(X \mid \not y)] \mid \delta\} \\
& \quad+E\left\{\varphi^{\prime}[E(X \mid \nexists)][E(X \mid \forall)-X] \mid \ngtr\right\}
\end{aligned}
$$

For the first term

$$
E\{\phi[E(X \mid \Delta)] \mid \Delta\}=E[\phi(\delta) \mid \Delta]
$$

since $\bar{X}$ is $\Delta$ measurable $q(\bar{X})$ is measureable

$$
E[\varphi(X) \mid \Delta]=\varphi(\bar{X})=\varphi[E(X(J)]
$$

so

$$
E\{\varphi[E(X \mid \mathscr{D}) \mid \otimes\}=\varphi[E(X \mid D)]
$$

For the second term since X is $\Delta$ measurable

$$
E(X \mid A)=X
$$

so the second term vanishes, and the desired result follows

$$
\begin{aligned}
E[\phi(\underline{x}) \mid . D] & \geqslant E\{\phi[E(\underline{x} \mid \Delta)] \mid A\} \\
& =\phi[E(\underline{y} \mid \Omega)]
\end{aligned}
$$

If $X$ is independent of $A$ use

$$
y=E(\bar{X}) \quad y=\bar{X}
$$

and taking expectations gives

$$
\begin{aligned}
& \varphi(X) \geqslant \varphi[E(X)]+\varphi^{\prime}[E(X)][E(X)-X] \\
\Rightarrow & E[\varphi(X)] \geqslant E\{\varphi[E(X)]\} \\
& +E\left\{\varphi^{\prime}[E(X)][E(X)-X]\right\}
\end{aligned}
$$

since $E(\underline{x})$ is not a random variable

$$
E\{\phi[E(\Sigma)]\}=\varphi[E(\Sigma)]
$$

and

$$
\begin{gathered}
E\left\{\phi^{\prime}[E(X)][E(X)-X]\right\} \\
=\phi^{\prime}[E(X)][E(X)-E(X)]=0
\end{gathered}
$$

So

$$
E[\varphi(\bar{X})] \geqslant \varphi[E(\bar{X})]
$$

* Let $(\Omega, \tilde{f}, P)$ be a probability space and let $\$$ be a sub-6-algebra of $\mathfrak{F}$. If $\bar{X}$ is an integrable random variable and $E\left(x^{2}\right)<\infty$ show that

$$
E\left[E(X \mid \otimes)^{2}\right] \leqslant E\left(X^{2}\right)
$$

From the conditional Jenseris inequality

$$
E[\phi(x) \mid y] \geqslant \phi[E(x \mid y)]
$$

let

$$
q(x)=x^{2}
$$

Since $x^{2}$ is a convex function

$$
E\left(\nabla^{2} \mid D\right) \geqslant E(Z \mid \Delta)^{2}
$$

Taking expectations gives

$$
E\left[E\left(X^{2} \mid \mathcal{A}\right)\right] \geqslant E\left[E(X \mid \mathcal{D})^{2}\right]
$$

From Computing Expectations by Conditioning

$$
E\left[E\left(\bar{x}^{2} \mid \mathscr{s}\right)\right]=E\left(\underline{x}^{2}\right)
$$

Thus

$$
E\left(\Sigma^{2}\right) \geqslant E\left[E(X \mid y)^{2}\right]
$$

## Donsker Theorem

Let $(\Omega, F, P)$ be a probability space. For a symetric random walk

$$
M_{k}=\sum_{i=1}^{k} Z_{k}
$$

where

$$
\begin{aligned}
z_{k} & =\{-1,1\} \\
M_{0} & =0 \\
P\left(z_{k}\right. & =-1)=1 / 2 \quad D\left(z_{k}=1\right)=1 / 2
\end{aligned}
$$

By deflning

$$
\omega_{t}^{n}=\frac{1}{\sqrt{n}} M_{n_{t}}=\frac{1}{\sqrt{n}} \sum_{i=1}^{(n-1)} Z_{i}
$$

where $\lfloor$ nt $]$ is the floor function.
For a fixed time $t$ show that

$$
\lim _{n \rightarrow \infty} \omega_{t}^{n}=\lim _{n \rightarrow \infty} \frac{1}{\sqrt{n}} \sum_{i=1}^{n t} z_{i} \xrightarrow{D} N(0, t)
$$

Now

$$
\begin{aligned}
& E\left(Z_{k}\right)=1 / 2-1 / 2=0 \\
& \operatorname{Var}\left(Z_{k}\right)=E\left(Z_{k}^{2}\right) \cdot\left[E\left(Z_{k}\right)\right]^{2}=E\left(Z_{k}^{2}\right)
\end{aligned}
$$

$$
=(-1)^{2} 1 / 2+(1)^{2 / 2}=1 / 2+1 / 2=1
$$

since

$$
z_{i} \| z_{j} \quad i \neq j
$$

For $i \neq j$

$$
\begin{aligned}
& E\left(z_{i} z_{j}\right)=(-1)(-1)(1 / 2)(1 / 2)+(-1)(1)(1 / 2)(1 / 2) \\
& +(1)(-1)(1 / 2)(1 / 2)+(1)(1)(1 / 2)(1 / 2) \\
& =1 / 4-1 / 4-1 / 4+1 / 4=0
\end{aligned}
$$

50

$$
\begin{aligned}
E\left(\omega_{t}^{n}\right) & =E\left[\frac{1}{\sqrt{n}} \sum_{i=1}^{\left\lfloor n^{t}\right\rfloor} z_{i}\right] \\
& =\frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor n+\rfloor} E\left(z_{i}\right)=0
\end{aligned}
$$

and

$$
\begin{aligned}
\operatorname{Var}\left(\omega_{t}^{n}\right) & =E\left[\left(\omega_{t}^{n}\right)^{2}\right]-\left[E\left(\omega_{t}^{n}\right)\right]^{2} \\
& =E\left[\left(\omega_{t}^{n}\right)^{2}\right] \\
& =E\left[\left(\frac{1}{\sqrt{n}} \sum_{i=1}^{(n t)} z_{i}\right)\left(\frac{1}{\sqrt{n}} \sum_{j=1}^{\text {int }} z_{j}\right)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =E\left[\frac{1}{n} \sum_{i=1}^{(n+1)} \sum_{j=1}^{n+1} z_{i} z_{j}\right] \\
& =\frac{1}{n} \sum_{i=1}^{\ln 1} \sum_{j=1}^{(n+1)} E\left(z_{i} z_{j}\right) \\
& =\frac{1}{n} \sum_{i=1}^{(n+1)} \sum_{j=1}^{(n+1)} E\left(z_{i} z_{j}\right) \delta_{i j} \\
& =\frac{1}{n} \sum_{i=1}^{(n t)} E\left(z_{i}^{2}\right) \\
& =\frac{1}{n} \sum_{i=1}^{\lfloor n t)} 1=\frac{\operatorname{Lnt}\rfloor}{n} \\
& \text { so } \operatorname{for} n \rightarrow \infty \\
& \lim _{n \rightarrow \infty} E\left(\omega_{t}^{n}\right)=0 \\
& \lim _{n \rightarrow \infty} \operatorname{Var}\left(\omega_{t}^{n}\right)=\lim _{n \rightarrow \infty} \frac{\ln t\rfloor}{n}=t
\end{aligned}
$$

using the central limit theorem

The Central Limit Theorem states that the sum of random variables

$$
S_{n}=\frac{\bar{x}_{1}+\bar{x}_{2}+\cdots+\bar{x}_{n}}{n}
$$

approaches a unit normal distribution with random variable)

$$
\frac{1}{\sigma \sqrt{n}}\left(\sum_{i=1}^{n} \bar{x}_{i}-n \mu\right)
$$

Thus
$\underline{\lim _{n \rightarrow \infty} \omega_{n}^{t}=\lim _{n \rightarrow \infty} \frac{1}{\sqrt{n}} \sum_{i=1}^{\lfloor n t\rfloor} Z_{i} \xrightarrow{D} N(0,1)}$

## Covariance of Two Weiner Processes

Let $(\Omega, \mathfrak{F}, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner Process
() $\omega_{0}=0$
2) For each $t>0$ and $s>t$
$\omega_{t+s}-\omega_{t} \sim N(0, s)$.
Increments are stationary
3) $\omega_{t+s}-\omega_{t} \Perp \omega_{t}$. Increments

Show that

$$
\operatorname{Cov}\left(\omega_{s}, \omega_{t}\right)=\min (s, t)
$$

and deduce that the correlation coefficient is

$$
e=\sqrt{\frac{\min (s, t)}{\max (s, t)}}
$$

The covariance is defined by
$\operatorname{Cov}\left(\omega_{s}, \omega_{t}\right)=E\left(\omega_{s} \omega_{t}\right)-E\left(\omega_{s}\right) E\left(\omega_{t}\right)$
From the definition of a Wiener Process
$\omega_{t} \sim N(0, t) \quad \omega_{s} \sim N(0, s)$
So

$$
\begin{aligned}
& E\left(\omega_{s}\right)=0 \\
& E\left(\omega_{t}\right)=0
\end{aligned}
$$

and

$$
\operatorname{Cov}\left(\omega_{s}, \omega_{t}\right)=E\left(\omega_{s} \omega_{t}\right)
$$

Assume that $s \leq t$ so $\omega_{t}-\omega_{s} \| \omega_{s}$
$E\left(\omega_{s} \omega_{t}\right)=E\left[\omega_{s} \omega_{t}-\omega_{s}^{2}+\omega_{s}^{2}\right]$
$=E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right)+\omega_{s}^{2}\right]$
$=E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right)\right]+E\left(\omega_{s}{ }^{2}\right)$
$=0+s=s$
likewise for $s>t$ so
$\omega_{s}-\omega_{t} \| \omega_{t}$
$E\left(\omega_{s} \omega_{t}\right)=E\left[\omega_{s} \omega_{t}-\omega_{t}^{2}+\omega_{t}^{2}\right]$
$=E\left[\omega_{t}\left(\omega_{s} \cdot \omega_{t}\right)\right]+E\left(\omega_{t}^{2}\right)$
$=0+t=t$
Trus

$$
\operatorname{Cov}\left(\omega_{s} \omega_{t}\right)=\min (s, t)
$$

The correlation coefficient is defined by

$$
\rho=\frac{\operatorname{Cov}\left(\omega_{s} \omega_{y}\right)}{\operatorname{Var}\left(\omega_{s}\right) \operatorname{Uar}\left(\omega_{t}\right)}
$$

From the definition of the standard Weiner Process

$$
\begin{aligned}
& \operatorname{Var}\left(\omega_{s}\right)=s \\
& \operatorname{Uar}\left(\omega_{t}\right)=t
\end{aligned}
$$

so for $s \leqslant t$

$$
C=\frac{s}{\sqrt{s t}}=\sqrt{\frac{s}{t}}
$$

and for $s>t$

$$
c=\frac{t}{\sqrt{s t}}=\sqrt{\frac{t}{s}}
$$

Trus

$$
\rho=\sqrt{\frac{\min (t, s)}{\max (t, s)}}
$$

## The Markov Property

1. The standard Weiner Process

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner Process with respect to the filtration $f_{t}$, $t \geqslant 0$. Show that if $f$ is a continous function then there exists another continuous function $g$ such that

$$
E\left[f\left(\omega_{t}\right) \mid \mathcal{F}_{u}\right]=g\left(\omega_{u}\right)
$$

for $0 \leqslant u \leqslant t$.
Now
$E\left[f\left(\omega_{t}\right) \mid \tilde{\tau}_{u}\right]=E\left[f\left(\omega_{t}-\omega_{u}+\omega_{u}\right) \mid \tilde{\tau}_{u}\right]$
using

$$
\omega_{t}-\omega_{u} \Perp \mathcal{F}_{u}
$$

and $w_{u}$ is $f_{u}$ measureable by setting $w_{u}$ to a constant $x$

$$
x=\omega_{u}
$$

so (i.e. this is sketchy, seems a linear asscoption)

$$
\begin{aligned}
& E\left[f\left(\omega_{t}-\omega_{u}+\omega_{u}\right) \mid \tilde{f}_{u}\right] \\
= & E\left[f\left(\omega_{t}-\omega_{u}+x\right) \mid \tilde{f}_{u}\right] \\
= & E\left[f\left(\omega_{t}-\omega_{u}+x\right)\right]
\end{aligned}
$$

Since $\omega_{t} \cdot \omega_{u}$ is a Wiener Process

$$
\omega_{t}-\omega_{u} \sim N(0, t-u)
$$

$E\left[f\left(\omega_{t}-\omega_{a}+x\right)\right]$

$$
=\frac{1}{\sqrt{2 \pi(t-s)}} \int_{-\infty}^{\infty} f(\omega+x) e^{-\frac{\omega^{2}}{2(t-s)}} d \omega
$$

let $\tau=t-u$ and $y=\omega+x$ then $d y=d \omega$ and $\omega=y-x$

So

$$
\begin{gathered}
E\left[f\left(\omega_{t}-\omega_{u}+x\right)\right]=\frac{1}{\sqrt{2 \pi \tau}} \int_{-\infty}^{\infty} f(y) e^{-\frac{(y-x)^{2}}{\partial \tau}} d y \\
=\int_{-\infty}^{\infty} f(y) p\left(\tau, \omega_{u}, y\right)
\end{gathered}
$$

where

$$
P\left(\tau, \omega_{u}, y\right)=\frac{1}{\sqrt{2 \pi \tau}} e^{\left.-\frac{\left(y-\omega_{u}\right.}{2 \tau}\right)^{2}}
$$

is the transition density, so

$$
\begin{aligned}
E\left[f\left(\omega_{t}\right) \mid \tilde{f}_{u}\right] & =\int_{-\infty}^{\infty} f(y) p\left(\tau, \omega_{u}, y\right) d y \\
& =g\left(\omega_{u}\right)
\end{aligned}
$$

where

$$
g\left(\omega_{u}\right)=\int_{-\infty}^{\infty} f(y) p\left(\tau, \omega_{u}, y\right) d y
$$

and

$$
E\left[f\left(\omega_{t}\right) \mid \hat{F}_{u}\right]=g\left(\omega_{u}\right)
$$

## 2. The wiener process

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $\left\{\omega_{t}: t>0\right\}$ be a standard wiener process with respect to the filtration $\mathcal{F}_{t} t \geqslant 0$. The wiener process is defined by

$$
\hat{\omega}_{t}=a+b t+c \omega_{t} \quad a, b \in \mathbb{R}, c>0
$$

Show that if $f$ is a cortinous function there is a function $g\left(\hat{\omega}_{n}\right)$

$$
E\left[f\left(\hat{\omega}_{t}\right) \mid \tilde{F}_{u}\right]=g\left(\omega_{u}\right)
$$

for $0 \leqslant u \leqslant t$
As for the Standard Wiener process

$$
E\left[f\left(\hat{\omega}_{t}\right) \mid \tilde{F}_{u}\right]=E\left[f\left(\hat{\omega}_{t}+\hat{\omega}_{u}-\hat{\omega}_{u}\right)\right]
$$

since $\omega_{t}-\omega_{u} \Perp \tilde{\mathcal{F}}_{u} \Rightarrow \hat{\omega}_{t}-\hat{\omega}_{u} \Perp \tilde{\mathcal{F}}_{u}$ in addition berause, $\omega_{u}$ is $F_{u}$ measureable $\hat{w}_{u}$ is $f_{u}$ measureable By setting

$$
\hat{\omega}_{u}=x
$$

where $x$ is a constant

$$
\begin{aligned}
& E\left[f\left(\hat{\omega}_{t}-\hat{\omega}_{u}+\hat{\omega}_{u}\right)\left(\tilde{f}_{u}\right]\right. \\
& =E\left[f\left(\hat{\omega}_{t}-\hat{\omega}_{u}+x\right)\left(\tilde{f}_{u}\right]\right. \\
& =E\left[f\left(\hat{\omega}_{t}-\hat{\omega}_{u}+x\right)\right]
\end{aligned}
$$

For the wiener Process

$$
\begin{aligned}
\hat{\omega}_{t} \cdot \hat{\omega}_{u} & =\left(a+b t+c \omega_{t}\right)-\left(a+b u+c \omega_{\omega}\right) \\
& =b(t-u)+c\left(\omega_{t}-\omega_{u}\right)
\end{aligned}
$$

The mean of $\hat{\omega}_{t}-\hat{\omega}_{u}$ is given by

$$
\begin{aligned}
& E\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)=E\left[b(t-u)+c\left(\omega_{t}-\omega_{u}\right)\right] \\
& =E[b(t-u)]+E\left[c\left(\omega_{t}-\omega_{u}\right)\right] \\
& =b(t-u)+0 \\
& =b(t-u) \\
& \operatorname{Var}\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)=E\left[\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)^{2}\right] \\
& -\left[E\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)\right]^{2}
\end{aligned}
$$

Now

$$
\begin{aligned}
& E\left[\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)^{2}\right]=E\left\{\left[b(t-u)+c\left(\omega_{t}-\omega_{u}\right)^{2}\right\}\right. \\
&= E\left[b^{2}(t-u)^{2}+2 c b\left(\omega_{t}-\omega_{u}\right)+c^{2}\left(\omega_{t}-\omega_{u}\right)^{2}\right] \\
&= E\left[b^{2}(t-u)^{2}\right]+E\left[2 c b\left(\omega_{t}-\omega_{u}\right)\right] \\
&+E\left[c^{2}\left(\omega_{t}-\omega_{u}\right)^{2}\right] \\
&= b^{2}(t-u)^{2}+0+c^{2}(t-u) \\
&= b^{2}(t-u)^{2}+c^{2}(t-u) \\
& \text { so } \\
& \operatorname{Var}\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)=E\left[\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)^{2}\right] \cdot\left[E\left(\hat{\omega}_{t}-\hat{\omega}_{u}\right)\right]^{2} \\
&= b^{2}(t-u)^{2}+c^{2}(t-u) \cdot b^{2}(t-u)^{2} \\
&= c^{2}(t-u)
\end{aligned}
$$

Thus

$$
\hat{\omega}_{t}-\hat{\omega}_{u} \sim N\left[b(t-u), c^{2}(t-u)\right]
$$

Now

$$
\begin{aligned}
& E\left[f\left(\hat{\omega}_{t}\right) \mid \tilde{F}_{u}\right]=E\left[f\left(\hat{\omega}_{t}-\hat{\omega}_{u}+x\right)\right] \\
= & \frac{1}{\sqrt{2 \pi c^{2}(t-u)}} \int_{-\infty}^{\infty} f(\omega+x) \exp \left\{\frac{[\omega-b(t-\omega)]^{2}}{2 c^{2}(t-u)}\right\} d \omega
\end{aligned}
$$

let

$$
\tau=t-u \quad y=\omega+x \Rightarrow \quad d y=d \omega
$$

so the integral becomes
$\frac{1}{c \sqrt{2 \pi} \tau} \int_{-\infty}^{\infty} f(y) \exp \left[-\frac{(y-x-b \tau)^{2}}{2 c^{2} \tau}\right] d \omega$
so the transition density is

$$
p\left(\tau, \hat{\omega}_{u}, y\right)=\frac{1}{c \sqrt{2 \pi \tau}} \exp \left[-\left(y-\frac{\hat{\omega}_{u}-b \tau}{\partial c^{2} \tau}\right)^{2}\right]
$$

and

$$
\Sigma \sim N\left(\omega_{a}+b \tau, c^{2} \tau\right)
$$

so with

$$
\begin{aligned}
& g\left(\hat{\omega}_{u}\right)=\int_{-\infty}^{\infty} f(y) p\left(\tau, \hat{\omega}_{u}, y\right) d y \\
& E\left[f\left(\hat{\omega}_{t}\right)\left(f_{u}\right]=g\left(\hat{\omega}_{u}\right)\right.
\end{aligned}
$$

3. Markov Property of Geomedric

## Brownian Motion

Let $(\Omega, F, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard Wicher Process with respect to the filtration $F_{t} t \geqslant 0$. For the geomedric wrener process

$$
S_{t}=S_{0} \exp \left[\left(\mu-\frac{1}{d} \sigma^{2}\right) t+\sigma \omega_{t}\right]
$$

where

$$
\mu \in \mathbb{R}, \quad \sigma>0 \text { and } S_{0}>0
$$

Show that if $f$ is a continous function then there exists another continuous function g such trat

$$
E\left[f\left(s_{t}\right) \mid \mathcal{F}_{u}\right]=g\left(s_{u}\right)
$$

where $0 \leqslant u<t$

Now

$$
E\left[f\left(s_{t}\right) \mid \tilde{F}_{u}\right]=E\left[\left.f\left(\frac{S_{t}}{S_{u}} s_{u}\right) \right\rvert\, \mathcal{F}_{u}\right]
$$

for

$$
s_{t}=s_{0} \exp \left[\left(\mu-\frac{2}{a} \sigma^{2}\right) t+\sigma \omega_{t}\right]
$$

wher $e$

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

is a standard Wiener Process, so

$$
\log \left(\frac{\delta_{t}}{\delta_{0}}\right)=\left(\mu-\frac{1}{2} \sigma^{2}\right) t+\sigma \omega_{t}
$$

which is a Wiener Process. For $0 \leqslant u<t$

$$
\begin{aligned}
& \log \left(\frac{S_{t}}{S_{0}}\right)-\log \left(\frac{S_{u}}{S_{0}}\right)=\left[\left(\mu-\frac{1}{2} \sigma^{2}\right) t+\sigma \omega_{t}\right] \\
& -\left[\left(\mu-\frac{1}{2} \sigma^{2}\right) \mu+\sigma \omega_{u}\right] \\
& =\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-\mu)+\sigma\left(\omega_{t}-\omega_{u}\right)
\end{aligned}
$$

but

$$
\log \left(\frac{s_{1}}{s_{0}}\right)-\log \left(\frac{s_{u}}{s_{0}}\right)=\log \left(\frac{s_{t}}{s_{u}}\right)
$$

50

$$
\log \left(\frac{S_{t}}{S_{u}}\right)=\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u)+\sigma\left(\omega_{t}-\omega_{u}\right)
$$

and

$$
\begin{aligned}
E & {\left[\log \left(\frac{s_{t}}{s_{u}}\right)\right]=E\left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u)+\sigma\left(\omega_{t}-\omega_{u}\right)\right] } \\
& =E\left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u)\right]+E\left[\sigma\left(\omega_{t}-\omega_{u}\right)\right] \\
& =\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u)+d \\
& =\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u)
\end{aligned}
$$

also

$$
\begin{gathered}
\operatorname{Var}\left[\log \left(\frac{s_{t}}{s_{u}}\right)\right]=E\left\{\left[\log \left(\frac{s_{t}}{s_{u}}\right)\right]^{2}\right\} \\
-\left\{E\left[\log \left(\frac{s_{t}}{s_{u}}\right)\right]\right\}^{2}
\end{gathered}
$$

for the first term

$$
E\left\{\left[\log \left(\frac{S_{t}}{S_{u}}\right)\right]^{2}\right\}=E\left\{\left[\left(u-\frac{1}{2} \sigma^{2}\right)(t-u)+\sigma\left(\omega_{t}-\omega_{L}\right)^{2}\right]^{2}\right\}
$$

$$
\begin{aligned}
= & E\left[\left(\mu-\frac{1}{2} \sigma\right)^{2}(t-u)^{2}+\left(\mu-\frac{1}{2} \sigma\right)(t-\mu) \sigma\left(\omega_{t}-\omega_{u}\right)\right. \\
& \left.+\sigma^{2}\left(\omega_{t}-\omega_{u}\right)^{2}\right] \\
= & E\left[\left(\mu-\frac{1}{2} \sigma\right)^{2}(t-u)^{2}\right]+E\left[\sigma\left(\mu-\frac{1}{2} \sigma\right)(t-u)\left(\omega_{t}-\omega_{u}\right)\right] \\
+ & E\left[\sigma^{2}\left(\omega_{t}-\omega_{u}\right)^{2}\right] \\
= & \left(\mu-\frac{1}{2} \sigma\right)^{2}(t-u)^{2}+0+\sigma^{2}(t-u) \\
= & \left(\mu-\frac{1}{2} \sigma\right)^{2}(t-a)^{2}+\sigma^{2}(t-u)
\end{aligned}
$$

and

$$
\begin{aligned}
& \operatorname{Var}\left[\log \left(\frac{s_{b}}{s_{u}}\right)\right]=\left(\mu-\frac{1}{2} \sigma\right)^{2}(t-u)^{2} \\
& +\sigma^{2}(t-u)-\left(\mu-\frac{1}{2} \sigma\right)^{2}(t-u)^{2} \\
& =\sigma^{2}(t-u)
\end{aligned}
$$

Thus

$$
\log \left(\frac{S_{t}}{S_{u}}\right) \sim N\left[\left(\mu-\frac{1}{2} \sigma^{2}\right)(t-u), \sigma^{2}(t-u)\right]
$$

Back to the original problem

$$
E\left[f\left(s_{t}\right) \mid \tilde{f}_{u}\right]=E\left[\left.f\left(\frac{s_{t}}{s_{u}} s_{u}\right) \right\rvert\, \tilde{f}_{u}\right]
$$

using

$$
\frac{s_{t}}{s_{u}} \Perp \tilde{f}_{u}
$$

and $S_{u}$ is $F_{u}$ measurable let $s_{u}=x$ where $x$ is a constant

$$
\begin{aligned}
& E\left[f\left(s_{t}\right) \mid \mathfrak{F}_{u}\right]=E\left[\left.f\left(\frac{s_{t}}{s_{u}} s_{u}\right) \right\rvert\, \mathcal{F}_{u}\right] \\
& =E\left[f\left(\frac{s_{u}}{s_{u}} x\right)\right]
\end{aligned}
$$

let

$$
\nu=\mu-\frac{1}{2} \sigma^{2}
$$

since

$$
\log \left(\frac{S_{t}}{S_{u}}\right) \sim N\left[v(t-u), \sigma^{2}(t-u)\right]
$$

$$
\begin{aligned}
\frac{S_{t}}{S_{u}} & \sim \frac{1}{\sqrt{2 \pi \sigma^{2}(t-u)}} \exp \left\{-\frac{[\log \omega-\nu(t-u)]^{2}}{2 \sigma^{2}(t-\mu)}\right\} \\
& =\frac{1}{\sigma \sqrt{2 \pi(t-u)}} \exp \left\{\frac{[\log \omega-\nu(t-u)]^{2}}{2 \sigma^{2}(t-\mu)}\right\}
\end{aligned}
$$

So

$$
\begin{gathered}
E\left[f\left(\frac{s_{t}}{s_{u}} x\right)\right]= \\
\frac{1}{\sigma \sqrt{2 \pi(t-u)}} \int_{-\infty}^{\infty} f(\omega x) \exp \left\{-\left[\frac{\log \omega-J(t-u)}{2 \sigma^{2}(t-u)}\right]^{2}\right\} d \omega
\end{gathered}
$$

let

$$
\text { T=t-u } \quad \begin{aligned}
& y=\omega x=0 \quad \omega=\frac{y}{x} \\
& \Rightarrow \quad d \omega=\frac{d y}{x}
\end{aligned}
$$

then

$$
\begin{aligned}
& E\left[f\left(\frac{s_{t}}{s_{u}} x\right)\right]=\frac{1}{\Delta \sqrt{2 \pi} \tau} \int_{-\infty}^{\infty} f(y) \exp \left[\frac{-\left(\log \frac{y}{x}-\nu \tau\right)^{2}}{2 \sigma^{2} \tau}\right] \frac{d y}{x} \\
& =\frac{1}{\sigma x \sqrt{2 \pi \tau}} \int_{-\infty}^{\infty} f(y) \exp \left[-\frac{(\log y-\log x-\nu \tau)^{2}}{2 \sigma^{2} \tau}\right] d y
\end{aligned}
$$

define the transition probability by

$$
P\left(\tau, S_{u}, y\right)=\frac{1}{\sigma S_{u} \sqrt{2 \pi} \tau} \exp \left[\cdot \frac{\left(\log y \cdot \log S_{u}-v \tau\right)^{2}}{2 \sigma^{2} \tau}\right]
$$

and

$$
\begin{aligned}
& E\left[f\left(S_{t}\right) \mid \mathcal{F}_{u}\right]=E\left[f\left(\frac{S_{t}}{S_{u}} x\right)\right] \\
& =\int_{-\infty}^{\infty} f(y) p\left(\tau, S_{u, y}\right) d y
\end{aligned}
$$

letting

$$
g\left(S_{u}\right)=\int_{-\infty}^{\infty} f(y) p\left(\tau, S_{u}, y\right) d y
$$

gives the vesired result

$$
E\left[f\left(S_{t}\right) \mid F_{u}\right]=g\left(S_{u}\right)
$$

## Martigale Property

## * Wiener Proces.

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner process. Show that $\omega_{t}$ is a Martingale
A Martingale satifies the properties

1) For $0 \leq s<t \quad E\left(\omega_{t} \mid f_{s}\right)=\omega_{s}$
2) $E\left(\left|\omega_{t}\right|\right)<\infty$
3) Wt is $\mathcal{F}_{i}$ adapted

For 1 since $\omega_{t}-\omega_{s} \| \mathcal{F}_{s}$
$E\left(\omega_{t} \mid \mathcal{F}_{s}\right)=E\left(\omega_{t}-\omega_{s}+\omega_{s} \mid \mathcal{F}_{s}\right)$
$=E\left(\omega_{t}-\omega_{s} \mid \tilde{f}_{s}\right)+E\left(\omega_{s} \mid \tilde{f}_{s}\right)$
By definiton of a standard
weiner process

$$
\omega_{t}-\omega_{s} \Perp \text { ₹ }_{s}
$$

and from definition of conditional expectation

$$
E\left(\omega_{t}-\omega_{s} \mid \tilde{J}_{s}\right)=E\left(\omega_{t}-\omega_{s}\right)
$$

and finally from the defintion of a standard weiner process

$$
E\left(\omega_{t}-\omega_{s}\right)=0
$$

For the second term the detintion of conditional expectation sives

$$
E\left(\omega_{s} \mid F_{s}\right)=\omega_{s}
$$

Trus

$$
\begin{aligned}
E\left(\omega_{t} \mid \tilde{\jmath}_{s}\right) & =E\left(\omega_{t}-\omega_{s} \mid \tilde{\jmath}_{s}\right)+E\left(\omega_{s} \mid \tilde{f}_{s}\right) \\
& =0+\omega_{s} \\
& =\omega_{s}
\end{aligned}
$$

so propent 1 is satisfied.
For property $2 \mathrm{E}\left(\left|\omega_{t}\right|\right)$ is the mean of a folded normal distribrition. For a normally distributed random variable I with mean $\mu$ and standard deviation $\sigma$
$E(|\underline{X}|)=\sigma \sqrt{\frac{2}{\pi}} e^{-\mu^{2} / 2 \sigma^{2}}+\mu\left[1-2 \Phi\left(-\frac{\mu}{\sigma}\right)\right]$
For the standard weiner process

$$
\begin{gathered}
E\left(\omega_{t}\right)=0 \\
E\left(\omega_{t}^{2}\right)=t \\
\sigma=\sqrt{t} .
\end{gathered}
$$

It follows that

$$
\begin{aligned}
E\left(\left|\omega_{t}\right|\right) & =\sqrt{t} \sqrt{\frac{\partial}{\pi}}(1)+O\left[1-2\left(\frac{1}{2}\right)\right] \\
& =\sqrt{\frac{\partial t}{\pi}}<\infty
\end{aligned}
$$

thus proberty 2 is satisfied
3) Property 3 is clearly satisfied since proof of property 1 was proved using wt is $\mathcal{F}_{t}$ measurable since $t$ is abritrary $\omega_{t}$ is $f_{t}$ adapted.

## * Eeometric Browniar Motion

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard Wiener Process.
For $\lambda \in \mathbb{R}$ show that

$$
\bar{\Delta}_{t}=e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t}
$$

is a Martingale.
A Martingale satisfies

1) $E\left(\underline{X}_{t} \mid \tilde{f}_{s}\right)=\underline{X}_{s}$
2) $E\left(\left|\underline{x}_{t}\right|\right) \leqslant \infty$
c) $\underline{X}_{t}$ is $\mathcal{F}_{t}$ adapted

Given $\omega_{t} \sim N(0, t)$ we can write
$\log Z_{t}=\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t$
we have

$$
E\left(\log Z_{t}\right)=E\left(\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t\right)
$$

$$
\begin{aligned}
& =E\left(\lambda \omega_{t}\right)-E\left(\frac{1}{2} \lambda^{2} t\right) \\
& =0-\frac{1}{2} \lambda^{2} t=-1 / 2 \lambda^{2} t
\end{aligned}
$$

and

$$
\begin{aligned}
E\left[\left(\log \mathbb{X}_{t}\right)^{2}\right] & =E\left[\left(\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t\right)^{2}\right] \\
& =E\left(\lambda^{2} \omega_{t}^{2}-\lambda^{3} t \omega_{t}+\frac{1}{4} \lambda^{4} t^{2}\right) \\
& =E\left(\lambda^{2} \omega_{t}^{2}\right)-E\left(\lambda^{3} t \omega_{t}\right) \\
& +E\left(\frac{1}{4} \lambda^{4} t^{2}\right) \\
& =\lambda^{2} t-0+\frac{1}{2} \lambda^{4} t^{2} \\
& =\lambda^{2} t+\frac{1}{4} \lambda^{4} t^{2} \\
& =\lambda^{2} t\left(1+\frac{1}{4} \lambda^{2} t\right)
\end{aligned}
$$

so

$$
\begin{aligned}
\operatorname{Var}\left[\left(\log \bar{x}_{t}\right)^{2}\right] & =E\left(\bar{x}^{2}\right) \cdot[E(\bar{x})]^{2} \\
& =\lambda^{2} t\left(1+\frac{1}{4} \lambda^{2} t\right)-\left(-\frac{1}{2} \lambda^{2} t\right)^{2} \\
& =\lambda^{2} t+\frac{1}{4} \lambda^{4} t^{2}-\frac{1}{4} \lambda^{4} t^{2} \\
& =\lambda^{2} t
\end{aligned}
$$

Trus the distribution of $\log \bar{x}_{t}$ is

$$
\begin{aligned}
& \log \bar{X}_{t}=\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t \sim N\left(-\frac{1}{2} \lambda^{2} t, \lambda^{2} t\right) \\
& \Rightarrow \bar{X}_{t}=e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t} \sim \log \cdot N\left(\frac{1}{2} \lambda^{2} t, \lambda t\right)
\end{aligned}
$$

For Martingale property 1

$$
\begin{aligned}
& E\left(\bar{X}_{t} \mid \mathcal{F}_{s}\right)=E\left(\left.e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t} \right\rvert\, \mathcal{F}_{s}\right) \\
& =e^{-\frac{1}{2} \lambda^{2} t} E\left(e^{\lambda \omega_{t}} \mid \mathcal{F}_{s}\right) \\
& =e^{-\frac{1}{2} \lambda^{2} t} E\left[e^{\lambda\left(\omega_{t}-\omega_{s}+\omega_{s}\right)} \mid \mathcal{F}_{s}\right] \\
& =e^{-\frac{1}{2} \lambda^{2} t} E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)+\lambda \omega_{s}} \mid \mathcal{F}_{s}\right] \\
& =e^{\frac{1}{2} \lambda^{2} t} E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)} \mid \mathcal{F}_{s}\right] E\left(e^{\lambda \omega_{s}}\left[\mathcal{F}_{s}\right)\right.
\end{aligned}
$$

The last step follows from linearity of conditional expectation and independence of conditional expectation gives

$$
E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)} \mid \mathcal{F}_{s}\right]=E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)}\right]
$$

using the general result for expectation of the exponential of a gaussian random variable

$$
E\left(e^{\frac{Z}{2}}\right)=e^{\mu-\frac{1}{2} \sigma^{2}}
$$

Were $\Delta^{2}$ and $\mu$ are the variance and mean of the random variable $\bar{X}$.

For

$$
\begin{aligned}
& E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)}\right] \\
& \sigma^{2}=\lambda^{2}(t-s)
\end{aligned}
$$

and

$$
E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)}\right]=e^{1 / 2 \lambda^{2}(t-s)}
$$

and from the definition of conditional expectation

$$
E\left(e^{\lambda \omega_{s}} \mid \mathcal{F}_{s}\right)=e^{\lambda \omega_{s}}
$$

Bringing things together

$$
\begin{aligned}
& E\left(\bar{X}_{t} \mid \mathcal{F}_{s}\right)=E\left(\left.e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t} \right\rvert\, \mathcal{F}_{s}\right) \\
& =e^{-\frac{1}{2} \lambda^{2} t} E\left[e^{\lambda\left(\omega_{t}-\omega_{s}\right)} \mid \mathcal{F}_{s}\right] E\left(e^{\lambda \omega_{s}} \mid \mathcal{F}_{s}\right) \\
& =e^{-\frac{1}{2} \lambda^{2} t} e^{1 / 2 \lambda^{2}(t-s)} e^{\lambda \omega_{s}} \\
& =e^{\lambda \omega_{s}-\frac{1}{2} \lambda^{2} s}=\bar{X}_{s}
\end{aligned}
$$

For Martingale property 2

$$
E\left(\left|Z_{t}\right|\right)<\infty
$$

but

$$
\left|\underline{x}_{t}\right|=\left|e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t}\right|=e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t}
$$

and

$$
\begin{aligned}
E\left(\left|\underline{X}_{t}\right|\right) & =E\left(e^{\lambda \omega_{t}-\frac{1}{2} \lambda^{2} t}\right) \\
& =E\left(e^{\lambda \omega_{t}} e^{-\frac{1}{2} \lambda^{2} t}\right) \\
& =e^{-\frac{1}{2} \lambda^{2} t} E\left(e^{\lambda \omega_{t}}\right)
\end{aligned}
$$

From the definition of a standard Wiener process

$$
\begin{aligned}
\omega_{t} & \sim N(0, t) \\
E\left(e^{\lambda \omega_{t}}\right) & =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} e^{\lambda \omega} e^{-\frac{1}{2} \frac{\omega^{2}}{t}} d \omega \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} \exp \left[\lambda \omega-\frac{\omega^{2}}{2 t}\right] d \omega \\
& =\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} \exp \left[\frac{\left(2 \lambda \omega t-\omega^{2}\right)}{2 t}\right] d \omega
\end{aligned}
$$

$=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} \exp \left[\frac{\left(\lambda^{2} t^{2}-\lambda^{2} t^{2}+2 \lambda \omega t-\omega^{2}\right)}{2 t}\right] d \omega$
$=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\infty} e^{2 \lambda^{2} t} \exp \left[-\frac{\left.\omega^{2}+2 \lambda \omega t-\lambda^{2} t^{2}\right)}{2 t}\right] d \omega$
$=\frac{1}{\sqrt{2 \pi t}} e^{1 / 2 \lambda^{2} t} \int_{-\infty}^{\infty} \exp \left[-\frac{\left(\omega^{2}-2 \lambda \omega t+\lambda^{2} t^{2}\right)}{2 t}\right] \omega$
$=\frac{1}{\sqrt{2 \pi t}} e^{\frac{1}{2} \lambda^{2} t} \int_{-\infty}^{\infty} \exp \left[-\left(\frac{\omega-\lambda t}{2 t}\right)^{2}\right] d \omega$
$=\frac{1}{\sqrt{2 \pi t}} e^{\frac{1}{2} \lambda^{2} t} \sqrt{2 \pi t^{2}}=e^{\frac{1}{2} \lambda^{2} t}$
Trus

$$
E\left(e^{\lambda \omega_{t}}\right)=e^{\frac{1}{2} \lambda^{2} t}
$$

and

$$
E\left(\left|\bar{X}_{t}\right|\right)=e^{-\frac{1}{2} \lambda^{2} t} e^{\frac{1}{2} \lambda t}=1<\infty
$$

For property 3 $\bar{x}_{t}$ since it is a function of $\omega_{t}$ which is $F_{t}$ adapted.

* Show $I_{t}=\omega_{t}^{2}-t$ is a Martingale

Let $(\Omega, \mathcal{F}, P)$ be a probability space and

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner process. show that

$$
\bar{X}_{t}=\omega_{t}^{2}-t
$$

is a Martingale.
The properties of a Maringale are

1) $E\left(\bar{X}_{t}\left(F_{s}\right)=\bar{X}_{s}\right.$ for $0 \leq s<t$
2) $E\left(\left|\mathbb{X}_{t}\right|\right)<\infty$
3) $\bar{E}_{t}$ is $\tilde{F}_{t}$ adapted

For Martingale property 1

$$
\begin{aligned}
& E\left(\mathbb{t}_{t} \mid \mathcal{F}_{s}\right)=E\left(\omega_{t}^{2}-t \mid \mathcal{F}_{s}\right) \\
& =E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right]-t \\
& =E\left[\left(\omega_{t}-\omega_{s}\right)^{2}+2\left(\omega_{t}-\omega_{s}\right) \omega_{s}+\omega_{s}^{2} \mid \mathcal{F}_{s}\right]
\end{aligned}
$$

$=E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \mid \tilde{f}_{s}\right]+2 E\left[\left(\omega_{t}-\omega_{s}\right) \omega_{s} \mid \tilde{f}_{s}\right]$
$+E\left(\omega_{s}^{2} \mid f_{s}\right)-t$
For the first term

$$
\begin{aligned}
& E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \mid{f_{s}}\right]=E\left[\left(\omega_{t}-\omega_{s}\right)^{2}\right] \\
& =t-s
\end{aligned}
$$

since $\omega_{t}-\omega_{s} \Perp \widetilde{f}_{s}$
For the second term
$E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid f_{s}\right]=\omega_{s} E\left(\omega_{t}-\omega_{s} \mid f_{s}\right)$
$=\omega_{s} E\left(\omega_{t}-\omega_{s}\right)=0$
This follows from using the "Taking out what is know" property, of conditional expectation, $\omega_{t-} \omega_{s} \Perp f_{s}$ and from the definition of of the standard wiener process

$$
E\left(\omega_{t}-\omega_{s}\right)=0
$$

and for the last term the definition of conditional expectation

$$
E\left(\omega_{s}^{2} \mid \tilde{f}_{s}\right)=\omega_{s}^{2}
$$

puting things together

$$
\begin{aligned}
& \underline{\bar{x}}_{t}=\omega_{t}^{2}-t \\
& E\left(\underline{x}_{t} \mid \mathcal{F}_{s}\right)=E\left(\omega_{t}^{2}-t \mid \mathcal{F}_{s}\right) \\
= & E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right]+2 E\left[\left(\omega_{t}-\omega_{s}\right) \omega_{s} \mid \mathcal{F}_{s}\right] \\
& +E\left(\omega_{s}^{2} \mid \mathcal{F}_{s}\right)-t \\
= & t-s+0+\omega_{s}^{2}-t \\
= & \omega_{s}^{2} \cdot s=\bar{x}_{s}
\end{aligned}
$$

For Martingale property 2

$$
E\left(\left|\underline{x}_{t}\right|\right)<\infty
$$

$$
\text { since } \begin{aligned}
\left|\underline{x}_{t}\right| & =\left|\omega_{t}^{2}-t\right| \leq \omega_{t}^{2}+t \\
E\left(\left|\underline{x}_{t}\right|\right) & \leq E\left(\omega_{t}^{2}+t\right) \\
& =E\left(\omega_{t}^{2}\right)+t \\
& =t+t=2 t<\infty
\end{aligned}
$$

As usual since $X_{t}$ is a function of $\omega_{t}$ and $\omega_{t}$ is $F_{t}$ abapted $\bar{x}_{t}$ is $F_{t}$ adapled

* Show that $\underline{x}_{t}=\omega_{t}^{3}-3 t \omega_{t}$ is a Martin gale
Let $(\Omega, \mathcal{F}, P)$ be a probability space and

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard wiener process. Show that

$$
\bar{x}_{t}=\omega_{t}^{3}-3 t \omega_{t}
$$

is a Martingale.
A Martingale is defined by

1) $E\left(\bar{X}_{t}\left(\mathcal{F}_{s}\right)=\bar{X}_{s}\right.$ for $0 \leqslant s<t$
2) $E\left(\left|\underline{Z}_{t}\right|\right)<\infty$
3) $I_{t}$ is $F_{t}$ adapled.

For martingale property

$$
\begin{aligned}
E & \left(\mathbb{I}_{t} \mid \mathcal{F}_{s}\right)=E\left(\omega_{t}^{3}-3 t \omega_{t} \mid \mathcal{F}_{s}\right) \\
= & E\left[\omega_{t}\left(\omega_{t}^{2}-3 t\right) \mid \mathcal{F}_{s}\right] \\
= & E\left\{\omega_{t}\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)^{2} \cdot 3 t\right] \mid \mathcal{F}_{s}\right. \\
= & E\left\{\omega _ { t } \left[\left(\omega_{t}-\omega_{s}\right)^{2}+2 \omega_{s}\left(\omega_{t}-\omega_{s}\right)\right.\right. \\
& \left.\left.+\omega_{s}^{2}-3 t\right] \mid \mathcal{F}_{s}\right\} \\
= & E\left[\omega_{t}\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& +2 E\left[\omega_{t} \omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \mathcal{F}_{s}\right] \\
& +E\left(\omega_{t} \omega_{s}^{2} \mid \mathcal{F}_{s}\right)-3 E\left(\omega_{t} t \mid \mathcal{F}_{s}\right)
\end{aligned}
$$

For the first term

$$
\begin{aligned}
& E\left[\omega_{t}\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& =E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& =E\left[\left(\omega_{t}-\omega_{s}\right)\left(\omega_{t}-\omega_{s}\right)^{2}+\omega_{s}\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& =E\left[\left(\omega_{t}-\omega_{s}\right)^{3} \mid \mathcal{F}_{s}\right]+E\left[\omega_{s}\left(\omega_{t} \cdot \omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& =E\left[\left(\omega_{t}-\omega_{s}\right)^{3}\right]+\omega_{s} E\left[\left(\omega_{t}-\omega_{s}\right)^{2}\right] \\
& =E\left[\left(\omega_{t}-\omega_{s}\right)^{3}\right]+\omega_{s}(t-s)
\end{aligned}
$$

using

$$
E\left(\nabla^{3}\right)=\left.\frac{d^{3} \mu}{d t^{3}}\right|_{t=0}=\mu\left(36^{2}+\mu^{2}\right)
$$

For the standard wiener process

$$
\mu=E\left(\omega_{t}-\omega_{s}\right)=0
$$

50

$$
E\left[\left(\omega_{t} \cdot \omega_{s}\right)^{3}\right]=0
$$

and

$$
\begin{aligned}
& E\left[\omega_{t}\left(\omega_{t}-\omega_{s}\right)^{2} 1 f_{s}\right]=E\left[\left(\omega_{t}-\omega_{s}\right)^{3}\right] \\
& +\omega_{s}(t-s) \\
& =0+\omega_{s}(t-s)=\omega_{s}(t-s)
\end{aligned}
$$

For the second term
$2 E\left[\omega_{t} \omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \tilde{f}_{s}\right]$
$=2 \omega_{s} E\left[\omega_{t}\left(\omega_{t}-\omega_{s}\right) \backslash z_{s}\right]$
$=2 \omega_{s} E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)\left(\omega_{t}-\omega_{s}\right) \mid \xi_{s}\right]$

$$
\begin{aligned}
= & 2 \omega_{S} E\left[\left(\omega_{t}-\omega_{S}\right)^{2}+\omega_{S}\left(\omega_{t}-\omega_{S}\right) \mid \mathcal{F}_{S}\right] \\
= & 2 \omega_{S} E\left[\left(\omega_{t}-\omega_{S}\right)^{2} \mid \mathcal{F}_{S}\right] \\
& 2 \omega_{S} E\left[\omega_{S}\left(\omega_{t}-\omega_{S}\right) \mid \mathcal{F}_{S}\right] \\
= & 2 \omega_{S} E\left[\left(\omega_{t}-\omega_{S}\right)^{2}\right]+2 \omega_{S}^{2} E\left[\left(\omega_{t}-\omega_{S}\right) \mid \mathcal{F}_{S}\right] \\
= & 2 \omega_{S}(t-S)+2 \omega_{S}^{2} E\left[\left(\omega_{t}-\omega_{S}\right)\right] \\
= & 2 \omega_{S}(t-S)+0
\end{aligned}
$$

50

$$
2 E\left[\omega_{t} \omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \tilde{F}_{s}\right]=2 \omega_{s}(t-s)
$$

For the thind term

$$
\begin{aligned}
& E\left(\omega_{t} \omega_{s}^{2} \mid \mathcal{F}_{s}\right)=E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right) \omega_{s}^{2} \mid \mathcal{F}_{s}\right] \\
& =E\left[\omega_{s}^{2}\left(\omega_{t}-\omega_{s}| | \mathcal{F}_{s}\right]+E\left(\omega_{s}^{3} \mid \mathcal{F}_{s}\right)\right. \\
& =\omega_{s}^{2} E\left[\left(\omega_{t}-\omega_{s}\right) \mid \mathcal{F}_{s}\right]+\omega_{s}^{3} \\
& =\omega_{s}^{2} E\left(\omega_{t}-\omega_{s}\right)+\omega_{s}^{3} \\
& =0+\omega_{s}^{3} \\
& =\omega_{s}^{3}
\end{aligned}
$$

and finally for the fourth term

$$
\begin{array}{rl}
-3 & E\left(\omega_{t} t \mid \mathcal{F}_{s}\right)=-3 t E\left(\omega_{t} \mid \mathcal{F}_{s}\right) \\
& =-3 t E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right) \mid \mathcal{F}_{s}\right] \\
& =-3 t\left[E\left(\omega_{t}-\omega_{s} \mid \mathcal{F}_{s}\right)+E\left(\omega_{s} \mid \mathcal{F}_{s}\right)\right] \\
& =-3 t\left[E\left(\omega_{t}-\omega_{s}\right)+\omega_{s}\right] \\
& =-3 t\left(0+\omega_{s}\right) \\
& =-3 t \omega_{s}
\end{array}
$$

Bringing things together

$$
\begin{aligned}
& E\left(I_{t} \mid \mathcal{F}_{t}\right)=E\left(\omega_{t}^{3}-3 t \omega_{t} \mid \mathcal{F}_{t}\right) \\
& =E\left[\omega_{t}\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right] \\
& +2 E\left[\omega_{t} \omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \mathfrak{F}_{s}\right] \\
& +E\left(\omega_{t} \omega_{s}^{2} \mid \mathfrak{F}_{s}\right)-3 E\left(\omega_{t} t^{3} \mid \mathfrak{F}_{s}\right) \\
& =\omega_{s}\left(t^{7}-s\right)+2 \omega_{s}\left(\hat{t}^{-s}\right)+\omega_{s}^{3}-3 t \omega_{s} \\
& =\omega_{s}^{3}-3 t \omega_{s}=I_{s}
\end{aligned}
$$

For Martingale property 2

$$
E\left(\left|\underline{z}_{T}\right|\right)<\infty
$$

NOW

$$
\begin{aligned}
& \left|\bar{\Delta}_{t}\right|=\left|\omega_{t}^{3}-3 \omega_{t} t\right| \leqslant\left|\omega_{t}^{3}\right|+3\left|t \omega_{t}\right| \\
\Rightarrow \quad & E\left(\left|\bar{x}_{t}\right|\right) \leqslant E\left(\left|\omega_{t}^{3}\right|\right)+3 E\left(\left|t \omega_{t}\right|\right)
\end{aligned}
$$

using Höblers inequality

$$
E[|\bar{X} Y|] \leqslant E\left[\left|X^{P}\right|\right]^{1 / P} E\left[\left|Y^{q}\right|\right]^{1 / a}
$$

where

$$
\frac{1}{p}+\frac{1}{q}=1 \quad p, q>1
$$

now let $p=q=2$

$$
\begin{aligned}
E\left(\left|\omega_{t}^{3}\right|\right) & =E\left(\left|\omega_{t}^{2} \omega_{t}\right|\right) \\
& \leqslant E\left(\left|\omega_{t}^{2}\right|^{2}\right)^{1 / 2} E\left(\left|\omega_{t}\right|^{2}\right)^{1 / 2} \\
& =\sqrt{E\left(\left|\omega_{t}^{2}\right|^{2}\right) E\left(\left|\omega_{t}\right|^{2}\right)}
\end{aligned}
$$

$$
\begin{aligned}
E\left(\left|X_{t}\right|\right) & \leqslant E\left(\left|\omega_{t}^{3}\right|\right)+3 t E\left(\left|\omega_{t}\right|\right) \\
& \leqslant \sqrt{E\left(\left|\omega_{t}^{2}\right|^{2}\right) E\left(\left|\omega_{t}\right|^{2}\right)}+3 t E\left(\left|\omega_{t}\right|\right) \\
& =\sqrt{E\left(\omega_{t}^{4}\right) E\left(\omega_{t}^{2}\right)}+3 t E\left(\left|\omega_{t}\right|\right)
\end{aligned}
$$

The cl'th moment of the Normal distribution is

$$
E\left(X^{4}\right)=36^{4}+\mu^{2}\left(66^{2}+\mu^{2}\right)
$$

so for the standard wiener process

$$
\mu=0 \quad \sigma^{2}=t
$$

50

$$
E\left(\omega_{t}^{4}\right)=3 t^{2}
$$

and

$$
E\left(\omega_{t}^{2}\right)=t
$$

So

$$
E\left(\left|\bar{x}_{t}\right|\right) \leqslant \sqrt{3 t^{3}}+3 t E\left(\left|\omega_{t}\right|\right)
$$

Once again using Hölders inequality

$$
E[|\bar{X} Y|] \leqslant E\left[\left|X^{p}\right|\right]^{1 / p} E\left[\left|Y^{q}\right|\right]^{1 / a}
$$

where

$$
\frac{1}{p}+\frac{1}{q}=1 \quad p, q>0
$$

once again let $p=q=2$

$$
\begin{aligned}
& E\left(\left|\omega_{t}\right|\right)=E\left(\left|\omega_{t}(1)\right|\right) \\
& \leqslant \sqrt{E\left(\omega_{t}^{2}\right)}=\sqrt{t}
\end{aligned}
$$

thus

$$
\begin{aligned}
E\left(\left|\underline{x}_{t}\right|\right) & \leqslant E\left(\left|\omega_{t}^{3}\right|\right)+3 E\left(\left|t \omega_{t}\right|\right) \\
& =\sqrt{3 t^{3}}+3 t \sqrt{t} \\
& =t \sqrt{t}(\sqrt{3}+3)<\infty
\end{aligned}
$$

For Martingale property $3 \Sigma_{t}$ is clearly $\exists_{t}$ adapled since it is a function of $\omega_{t}$ which is $\mathcal{F}_{t}$ adapated by definition.

## Submartingales and Supermartingales

Let $(\Omega, P, \mathcal{F})$ be a probability space and let

$$
\left\{X_{t}: t \geqslant 0\right\}
$$

be an $F_{t}$ adapted random variable
For a Martingale the definion of conditional expectation gives

$$
E\left(\mathbb{X}_{t} \mid \mathcal{F}_{t-1}\right)=\overline{\underline{X}}_{t-1}
$$

If

$$
E\left(\bar{x}_{t} \mid \mathcal{F}_{t-1}\right) \geqslant \bar{x}_{t-1}
$$

then $\overline{\bar{x}}_{t}$ is a submartingale

$$
E\left(\bar{x}_{t} \mid F_{t-1}\right) \leqslant \bar{x}_{t-1}
$$

then $\bar{X}_{t}$ is a Supermartingale.

Let $(\Omega, f, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner process with respect to the filtration $\mathcal{F}_{t}, t \geqslant 0$ 。

Show that if $\varphi$ is a convex function and

$$
E\left(\left|\varphi\left(\omega_{t}\right)\right|\right)<\infty
$$

for all $t \geqslant 0$ then $\phi\left(\omega_{t}\right)$ is a submartingale.
Assume that $s<t$, the a submartingale is defined by

$$
E\left(\bar{X}_{t} \mid \tilde{F}_{s}\right) \geqslant \bar{X}_{s}
$$

The Conditional Jensen Inequality is defined by 1

$$
E[\varphi(\underline{x}) \mid \cdot D] \geqslant \varphi[E(\underline{x} \mid \mathcal{M})]
$$

SO
$\underline{E\left[\varphi\left(\omega_{t}\right) \mid \mathcal{F}_{s}\right] \geqslant \varphi\left[E\left(\omega_{s} \mid \mathcal{F}_{s}\right)=\varphi\left(\omega_{s}\right)\right.}$

## Wiener Process Continity $\rightarrow$ Diffentication

Let $(\Omega, \Im, P)$ be a probability space. Show that sample paths of the standard wiener process

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

are continuous but not differentiable.
A process $\omega_{t} \sim N(0, t)$ is for continous in probability

$$
\lim _{\Delta t \rightarrow 0} P\left(\left|\omega_{t+\Delta t} \cdot \omega_{t}\right| \geqslant \delta\right)=0
$$

Recall the Chebysheu ineguality

$$
P(|\bar{X}-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

Since $w_{t}$ is a Martingale

$$
E\left(\omega_{t+\Delta t}\left(\tilde{f}_{t}\right)=\omega_{t}\right.
$$

and

$$
\begin{aligned}
& O^{2}=\operatorname{Var}\left(\omega_{t+\Delta t} \mid \mathcal{F}_{t}\right) \\
& k=\delta
\end{aligned}
$$

$$
\begin{aligned}
& P\left(\left|\omega_{t+\Delta t}-\omega_{t}\right| \geqslant \delta\right) \\
& =P\left(\left|\omega_{t+\Delta t}-E\left(\omega_{t+\Delta t} \mid f_{t}\right)\right| \geqslant \delta\right) \\
& \leqslant \frac{\operatorname{Var}\left(\omega_{t+\Delta t} \mid f_{t}\right)}{\delta^{2}} \\
& =\frac{\operatorname{Var}}{\delta^{2}}\left(\omega_{t+\Delta t}-\omega_{t}+\omega_{t}\left(f_{t}\right)\right. \\
& =\frac{\operatorname{Var}}{\delta^{2}}\left(\omega_{t+\Delta t}-\omega_{t} \mid f_{t}\right)+\frac{\operatorname{Var}}{\delta^{2}}\left(\omega_{t} \mid f_{t}\right) \\
& =\frac{\operatorname{Var}}{\delta^{2}}\left(\omega_{t+\Delta t}-\omega_{t} \mid f_{f}\right)+\frac{\operatorname{Var}}{\delta^{2}}\left(\omega_{t}\left(f_{t}\right)\right. \\
& =\frac{\Delta t}{\delta^{2}}+0
\end{aligned}
$$

since $\omega_{t+\Delta l}-\omega_{t} \| \mathcal{F}_{t}$ and since $\omega_{t}$ is $f_{t}$ adapted

$$
\begin{aligned}
\operatorname{Var}\left(\omega_{t} \mid \mathcal{F}_{t}\right) & =E\left(\omega_{t}^{2} \mid \mathcal{F}_{t}\right)-\left[E\left(\omega_{t} \mid \mathcal{F}_{t}\right)\right]^{2} \\
& =\omega_{t}^{2}-\omega_{t}^{2}=0
\end{aligned}
$$

$$
\lim _{\Delta t \rightarrow 0} P\left(\left|\omega_{t+\Delta t}-\omega_{t}\right| \geqslant \delta\right) \leqslant \lim _{\Delta t \rightarrow 0} \frac{\Delta t}{\delta^{2}}
$$

Thus $\omega_{t}$ is continuous.
consider the derivative

$$
\lim _{\Delta t \rightarrow 0} \frac{\omega_{t+\Delta t}-\omega_{t}}{\Delta t}=\frac{\Delta \omega_{t}}{\Delta t}
$$

Now if $\varphi \sim N(0, \Delta t)$

$$
\Delta \omega_{t}=\varphi \sqrt{\Delta t}
$$

50

$$
\begin{aligned}
& \lim _{\Delta t \rightarrow 0} \frac{\Delta \omega_{t}}{\Delta t}=\lim _{\Delta t \rightarrow 0} \varphi \frac{\sqrt{\Delta t}}{\Delta t} \\
& =\lim _{\Delta t \rightarrow 0} \frac{\varphi}{\sqrt{\Delta t}}= \pm \infty
\end{aligned}
$$

depending on the sign of $\varphi$.
Thus $\omega_{t}$ is not differentiable.

## First Time Passage

## 1. Doob's Maximal Inequality

Let $(\Omega, F, P)$ be a probability space and let

$$
\left\{X_{t}: 0 \leqslant t \leqslant T\right\}
$$

be a continous non-negative submartingale with respect to a fittration $F_{t} 0 \leqslant t \leqslant T$. Given that $\lambda>0$ and $\uparrow=\min \left[\dot{t}: \ddot{X}_{t} \geqslant \lambda\right]$ show that

$$
E\left(\mathbb{X}_{0}\right) \leqslant E\left(\mathbb{X}_{\min [r, T]}\right) \leqslant E\left(\mathbb{X}_{T}\right)
$$

By writing

$$
\bar{X}_{\min [\tau, \tau]}=\bar{X}_{\uparrow} \mathbb{I}_{\{\tau \leqslant \tau\}}+\bar{X}_{\tau} \mathbb{I}_{\{\tau>\tau\}}
$$

Show that

$$
P\left(\sup _{0 \leqslant t \leqslant T} I_{t} \geqslant \lambda\right) \leqslant \frac{E\left(X_{T}\right)}{\lambda}
$$

Now for $\lambda>0$ let $\tau=\min \left[\tau: \bar{x}_{t} \geqslant \lambda\right]$ so that $0 \leq \min (T, T) \leq T$.
Since $I_{t}$ is a nonegative submartingale

$$
E\left(\mathbb{X}_{T} \mid \mathcal{F}_{\min (\tau, T)}\right) \geqslant \bar{I}_{\min (\tau, T)}
$$

Taking expectation gives

$$
E\left[\mathbb{Z}_{\min (\tau, T)}\right] \leqslant E\left[E\left(\mathbb{Z}_{T}\left(\mathcal{F}_{\min (\tau, T)}\right)\right]\right.
$$

Now the expection is evaluated over the entire event space so from "Computing Expectation Dy Conditioning

$$
E\left[E\left(\underline{\bar{x}}_{T} \mid \mathcal{F}_{\min (\tau, T)}\right)\right]=E\left(\overline{\underline{x}}_{T}\right)
$$

50

$$
E\left[\bar{X}_{\min (\tau, T)}\right] \leqslant E\left(\bar{X}_{T}\right)
$$

similarly since $0 \leqslant \min (T, T)$ and since $\bar{X}_{t}$ is a submartingale

$$
E\left(\bar{X}_{\min (\tau, T)} \mid \mathcal{F}_{\min (\tau, T)}\right) \geqslant \bar{X}_{0}
$$

Taking expectation

$$
E\left(X_{\min (\tau, T)}\right) \geqslant E\left(X_{0}\right)
$$

so

$$
E\left(\bar{X}_{0}\right) \leqslant E\left(\underline{X}_{\text {min }}(\tau, T)\right) \leqslant E\left(\bar{X}_{T}\right)
$$

Define an indicator function

$$
\begin{aligned}
& \mathbb{I}_{(\tau \leqslant T)}= \begin{cases}1 & \tau \leqslant T \\
0 & \tau>T\end{cases} \\
& \mathbb{I}(\tau>\tau)= \begin{cases}1 & \tau>T \\
0 & \tau \leqslant T\end{cases}
\end{aligned}
$$

using the indicator functions

$$
\underline{X}_{\min (\tau, T)}=\underline{X}_{t} \underline{\Pi}(\tau \leqslant T)+\underline{X}_{t} \mathbb{I}_{(\tau>T)}
$$

taking expectation
$E\left(\underline{X}_{\min (\tau, \tau)}\right)=E\left[\underline{X}_{t} \underline{I}_{(t \leqslant \tau)}\right]+E\left[\underline{X}_{t} \underline{I}_{(t>\tau)}\right]$
since it is assumed that

$$
\tau=\min \left(t: \mathbb{Z}_{t} \geqslant \lambda\right)
$$

and

$$
\begin{aligned}
& E\left[X_{t} \mathbb{I}_{(t \leqslant T)}\right]=\int_{\Omega} \mathbb{X}_{t} \mathbb{I}_{(t \leqslant T)} d P \\
& \geqslant \int_{\Omega} \lambda \mathbb{I}_{(t \leqslant T)} d P=\lambda \iint_{\Omega}[(t \leqslant T) d P \\
& =\lambda P(t \leqslant T)
\end{aligned}
$$

so
$E\left[\bar{X}_{\min (\tau, \tau)}\right]=E\left[\bar{X}_{t} \bar{I}_{(t \leqslant \tau)}\right]+E\left[\bar{X}_{t} \bar{I}_{(t) \tau}\right] \geqslant \lambda P(t \leqslant \tau)+E\left[\mathbb{X}_{t} \mathbb{I}_{(t>\tau)}\right]$

Using

$$
E\left(\bar{X}_{0}\right) \leqslant E\left(\bar{X}_{\min (\tau, T)}\right) \leqslant E\left(\bar{X}_{\tau}\right)
$$

gives

$$
\begin{aligned}
& E\left(\underline{\bar{X}}_{T}\right) \geqslant \lambda P(t \leqslant T)+E\left[\bar{X}_{t} \mathbb{I}_{(t>T)}\right] \\
\Rightarrow & \lambda P(t \leqslant T) \leqslant E\left(\mathbb{X}_{T}\right)-E\left[\bar{X}_{t} \mathbb{I}_{(t) T)}\right]
\end{aligned}
$$

Since $\bar{X}_{t}$ is non-negatie

$$
E\left[\bar{X}_{t} \Pi_{(t, \tau)}\right] \geqslant 0
$$

and

$$
\lambda P(t \leq T) \leq E\left(\bar{X}_{T}\right)
$$

sence

$$
\begin{aligned}
\tau \leqslant T & \Rightarrow \min \left(t: \bar{X}_{t} \geqslant \lambda\right) \\
& \Rightarrow\left\{\sup _{0 \leqslant t \leqslant T} \bar{X}_{t} \geqslant \lambda\right\}
\end{aligned}
$$

so

$$
P\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t} \geqslant \lambda\right) \leqslant E \frac{E\left(\bar{X}_{T}\right)}{\lambda}
$$

Similarly if $\bar{\lambda}_{t}$ is a supermarlingale

$$
E\left[X_{T}\left(f_{\min (\tau, T)}\right] \leqslant \bar{X}_{\min (\tau, \tau)}\right.
$$

Following the steps used for the sub martingcle

$$
E\left(\underline{X}_{T}\right) \leqslant E\left[\underline{X}_{\min (\tau, T)}\right] \leqslant E\left(\underline{X}_{0}\right)
$$

and

$$
P\left(\sup _{0 \leqslant t \leqslant T} \bar{x}_{t} \geqslant \lambda\right) \leqslant \frac{E\left(\bar{x}_{0}\right)}{\lambda}
$$

## Doob's LP Maximal Inequality

Let $(\Omega, \mathcal{F}, P)$ be a probability space and let $\mathcal{Z}$ be a continuous non-negative random variable where for

$$
m>0, E\left(\mathbb{Z}^{m}\right)<\infty
$$

Show that

$$
E\left(\mathbb{Z}^{m}\right)=m \int_{0}^{\infty} \alpha^{m-1} P(z>a) d \alpha
$$

Let $\left\{X_{t}: 0 \leqslant t \leqslant T\right\}$ be a continaus non-negaive submartingale with respect to the filtraction $\mathcal{F}_{t}, 0 \leqslant t \leqslant T$ Using, the above result for $p>1$ and if

$$
E\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{D}\right)<\infty
$$

Show that

$$
E\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{P}\right) \leqslant\left(\frac{p}{p^{-}-1}\right)^{p} E\left(I_{T}^{P}\right)
$$

Deduce that if $\left\{I_{t}: 0 \leqslant t \leqslant T\right\}$ is a Continuous non-negatil supermartingale with respect to the filtration $\mathcal{F}_{t}$, $0 \leqslant t \leqslant T$, then

$$
E\left(\sup _{0 \leqslant t \leqslant T} \Sigma_{t}^{P}\right) \leqslant\left(\frac{p}{p-1}\right)^{P} E\left(I_{0}^{P}\right)
$$

Define the indicator function

$$
I_{(z>\alpha)}= \begin{cases}1 & z>\alpha \\ 0 & z \leqslant \alpha\end{cases}
$$

Tren
$\int_{0}^{\infty} m \alpha^{m-1} P(R>a) d \alpha=\int_{0}^{\infty} m \alpha^{m-1} E\left(\mathbb{1}_{(R)} a\right) d \alpha$
since

$$
E\left(\mathbb{I}_{(z>\alpha)}\right)=P(R>\alpha)
$$

The expectation is an integral ove 2 so $m$ and $\alpha$ can be considered constants with respent to arimation of the expectation. So
$\int_{0}^{\infty} m \alpha^{m-1} E\left(\mathbb{I}_{(R>\alpha)}\right) d d=E\left[\int_{0}^{\infty} m \alpha^{m-1} \mathbb{I}_{(2, \alpha)} d d\right]$
$=E\left[\int_{0}^{R} m \alpha^{m-1} d \alpha\right]=E\left(R^{m}\right)$
Let
$T=\min \left(t: I_{t} \geqslant \lambda\right), \lambda>0 \quad 0 \leqslant \min (t, T) \leqslant T$
then

$$
\{T \leqslant T\} \Leftrightarrow\left\{\sup _{0 \leqslant t \leqslant T} \bar{X}_{t} \geqslant \lambda\right\}
$$

Using the previous sesult

$$
E\left(\mathbb{Z}^{m}\right)=m \int_{0}^{\infty} \alpha^{m-1} P(z>a) d \alpha
$$

gives
$E\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)=\int_{0}^{\infty} m \lambda^{m-1} P\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}>\lambda\right) d \lambda$
and the result from "Doob's Maximal Inequalitil"

$$
P\left(\sup _{0 \leqslant t \leqslant T} Z_{t}>\lambda\right) \leqslant E \frac{\left(X_{T}\right)}{\lambda}
$$

gives

$$
\begin{aligned}
& \int_{0}^{\infty} m \lambda^{m-1} P\left(\sup _{0 \leqslant t \leqslant T} \bar{x}_{t}>\lambda\right) d \lambda \\
& \quad \leqslant \int_{0}^{\infty} m \lambda^{m-1} \frac{E}{\lambda}\left(\mathbb{X}_{T} \mathbb{I}_{\left\{\sup _{0 \leqslant t \leqslant T} \bar{I}_{t} \geqslant \lambda\right\}}\right) d \lambda \\
& =m E\left[\mathbb{I}_{T} \int_{0}^{\infty} \lambda^{m-2} \mathbb{I}_{\left\{\sup _{0 \leqslant t \leqslant T} \mathbb{X}_{t} \geqslant \lambda\right\}} d \lambda\right] \\
& =m E\left[\mathbb{Z}_{T} \int_{0}^{\sup _{0 \leqslant t \leqslant T} \mathbb{I}_{t}} \lambda^{m-2} d \lambda\right]
\end{aligned}
$$

$$
\begin{aligned}
& =m E\left\{\left.\bar{X}_{T}\left[\frac{\lambda^{m-1}}{m-1}\right]\right|_{0 \leqslant t \leqslant T} ^{\sup _{t}}\right\} \\
& =m E\left\{\bar{X}_{T}\left[\frac{1}{m-1}\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m-1}\right)\right]\right\} \\
& =\frac{m}{m \cdot 1} E\left[\underline{X}_{T}\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m-1}\right)\right] \\
& E\left(\sup _{0 \leqslant t \leqslant T} \underline{X}_{t}^{m}\right) \leqslant \frac{m}{m-1} E\left[\underline{X}_{T}\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m-1}\right)\right]
\end{aligned}
$$

using Höbers Inequality

$$
\begin{aligned}
& \quad E[|\bar{X} Y|] \leqslant E\left[\left|X^{p}\right|\right]^{1 / p} E\left[\left|Z^{q}\right|\right]^{1 / a} \\
& \quad \frac{1}{p}+\frac{1}{q}=1 \quad q \quad q=\frac{p}{p^{-1}} \\
& \text { let } \quad p=m \quad \text { then } \quad q=\frac{m}{m-1} \\
& E\left(\sup _{o \leqslant t \leqslant T} \underline{X}_{t}^{m}\right) \leqslant \frac{m}{m-1} E\left[\underline{X}_{T}\left(\sup _{o \leqslant t \leqslant X_{t}^{m-1}}\right)\right] \\
& =\frac{m}{m-1} E\left(\bar{X}_{T}^{m}\right)^{1 / m} E\left[\left(\sup _{o \leqslant t \leqslant T} \bar{X}_{t}\right)^{m}\right]^{\frac{m-1}{m}}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & E\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right) E\left[\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)\right]^{\frac{1-m}{m}} \\
& \leqslant \frac{m}{m-1} E\left(\bar{X}_{T}^{m}\right)^{\frac{1}{m}} \\
= & E\left[\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)^{1+\frac{(-m)}{m}} \leqslant \frac{m}{m-1} E\left(\bar{X}_{T}^{m}\right)^{\frac{1}{m}}\right. \\
\Rightarrow & E\left[\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)\right]^{1 / m} \leqslant \frac{m}{m-1} E\left(\underline{X}_{T}^{m}\right)^{\frac{1}{m}} \\
\Rightarrow & E\left[\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)\right] \leqslant\left(\frac{m}{m-1}\right)^{m} E\left(\bar{X}_{T}^{m}\right)
\end{aligned}
$$

If $\bar{X}_{t}$ is a supermartingale it was previously shown that

$$
P\left(\sup _{0 \leqslant t \leqslant T} \bar{x}_{t} \geqslant \lambda\right) \leqslant \frac{E\left(\bar{x}_{0}\right)}{\lambda}
$$

so $E\left(\bar{X}_{0}\right)$ will povide the upper bound so

$$
E\left[\left(\sup _{0 \leqslant t \leqslant T} \bar{X}_{t}^{m}\right)\right] \leqslant\left(\frac{m}{m-1}\right)^{m} E\left(\underline{X}_{0}^{m}\right)
$$

* Let $(\Omega, \mathcal{F}, P)$ be a probability space and let

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard weiner process. show that for every $T>O$ and $\lambda, \theta>0$
$P\left(\sup _{0 \leqslant t \leqslant T} e^{\theta \omega_{t}} \geqslant e^{\theta \lambda}\right) \leqslant e^{\frac{1}{2} \theta^{2} T-\theta \lambda}$
and then show that

$$
P\left(\sup _{0 \leqslant t \leqslant T} w_{t} \geqslant \lambda\right) \leqslant e^{-\frac{\lambda^{2}}{2 T}}
$$

and then show that

$$
P\left(\sup _{0 \leqslant t \leqslant T}\left|\omega_{t}\right| \geqslant \lambda\right) \leqslant 2 e^{-\frac{\lambda^{2}}{\partial T}}
$$

Now for $\lambda>0$ and $\theta>0$ "Doob's Maximal Inequality"

$$
\begin{aligned}
& P\left(\sup _{0 \leqslant t \leqslant T} \omega_{t}>\lambda\right) \leqslant \frac{E\left(\omega_{T}\right)}{\lambda} \\
\Rightarrow & P\left(\sup _{0 \leqslant t \leqslant T} \theta \omega_{t}>\theta \lambda\right) \leqslant E\left(\frac{\theta \omega_{T}}{\theta \lambda}\right)
\end{aligned}
$$

$$
=P\left(\sup _{0 \leqslant t \leqslant T} e^{\theta \omega_{t}} \geqslant e^{\theta \lambda}\right) \leqslant E \frac{\left(e^{\theta \omega_{T}}\right)}{e^{\theta \lambda}}
$$

Now

$$
\begin{aligned}
& E\left(e^{\theta \omega T}\right)=\frac{1}{\sqrt{2 \pi T}} \int_{-\infty}^{\infty} e^{\theta \omega} e^{-\frac{\omega}{\partial T}} d \omega \\
& =\frac{1}{\sqrt{2 \pi T}} \int_{-\infty}^{\infty} e^{\theta \omega-\frac{\omega^{2}}{\partial T}} d \omega
\end{aligned}
$$

for the exponential argument

$$
\begin{aligned}
& \theta \omega-\frac{\omega^{2}}{\partial T}=-\frac{1}{\partial T}\left(\omega^{2}-2 T \theta \omega+T^{2} \theta^{2}-T^{2} \theta^{2}\right) \\
& =-\frac{1}{\partial T}\left[\left(\omega^{2}-2 T \theta \omega+T^{2} \theta^{2}\right)-T^{2} \theta^{2}\right] \\
& =-\left(\frac{\omega-T \theta}{2 T}\right)^{2}+\frac{T \theta^{2}}{2}
\end{aligned}
$$

50

$$
\begin{aligned}
E\left(e^{\theta \omega_{T}}\right) & =\frac{1}{\sqrt{2 \pi T}} \int_{-\infty}^{\infty} e^{\frac{T \theta^{2}}{2}} e^{-\left(\omega \cdot \frac{(\omega)^{2}}{2 T} d \omega\right.} d \omega \\
& =e^{\frac{1}{2} T \theta^{2}} \frac{1}{\sqrt{2 \pi} T} \int_{-\infty}^{\infty} e^{-\frac{(\omega-T \theta)^{2}}{2 T}} d \omega
\end{aligned}
$$

$$
\Rightarrow E\left(e^{\theta \omega_{T}}\right)=e^{\frac{1}{2} T \theta^{2}}
$$

so

$$
\begin{aligned}
& P\left(\sup _{0 \leqslant t \leqslant T} e^{\theta \omega_{t}} \geqslant e^{\theta \lambda}\right) \leqslant E \frac{\left(e^{\theta \omega_{T}}\right)}{e^{\theta \lambda}} \\
& =e^{\frac{1}{2} \tau \theta^{2}-\theta \lambda}
\end{aligned}
$$

Minnimizing with respect to $\theta$ gives

$$
\begin{aligned}
& \frac{d}{d \theta} e^{\frac{1}{2} T \theta^{2}} \cdot \lambda \theta=(T \theta \cdot \lambda) e^{\frac{1}{2} T \theta^{2} \cdot \lambda \theta} \\
& =0 \\
\Rightarrow & T \theta-\lambda=\theta=\frac{\lambda}{T}
\end{aligned}
$$

so the minimum value is
$e^{1 / 2 T(\lambda / T)^{2}-\lambda(\lambda / T)}=e^{\frac{1}{2} \lambda^{2} / T-\lambda^{2} / T}=e^{-\lambda^{2} / 2 T}$
The inequality becomes
$P\left(\sup _{0 \leqslant t \leqslant T} e^{\lambda \omega t / T} \geqslant e^{\lambda^{2} / T}\right) \leqslant e^{-\lambda^{2} / 2 T}$

$$
P\left(\sup _{0 \leqslant t \leqslant T} \omega_{t} \geqslant \lambda\right) \leqslant e^{-\lambda^{2} / \partial T}
$$

Now since $\omega_{t} \sim N(0, t)$
$P\left(\left|\omega_{4}\right| \geqslant \lambda\right)=P\left(\omega_{t} \geqslant \lambda\right)+P\left(\omega_{7} \leqslant-\lambda\right)$
since $N(0, t)$ is symetric about
0

$$
P\left(\omega_{t} \geqslant \lambda\right)=P\left(\omega_{t} \leqslant \lambda\right)
$$

80

$$
P\left(\sup _{0 \leqslant t \leqslant \tau}\left|\omega_{t}\right| \geqslant \lambda\right) \leqslant 2 e^{-\lambda^{2} h \tau}
$$

*Let $(\Omega, \mathcal{F}, P)$ be a probability space and

$$
\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a Wiener process with respect to the filtration $\mathcal{F}_{t} t \geqslant 0$.

By writing $I_{t}=x_{0}+\omega_{t}$ where $x \in \mathbb{R}$ show that is

$$
\left\{X_{t}: t \geqslant 0\right\}
$$

a continous Martingale. let

$$
T_{a}=\inf \left(t \geqslant 0: \mathbb{Z}_{t}=a\right)
$$

and

$$
T_{b}=\inf \left(t \geqslant 0: \bar{x}_{c}=b\right)
$$

where $a<b$
snow that

$$
P\left(T_{a}<T_{b}\right)=\frac{b-x_{0}}{a-x_{0}}
$$

A Martingale satisfies

1) $E\left(\underline{X}_{t} \mid \mathcal{F}_{s}\right)=\underline{I}_{s}$
$0 \leqslant s<t$
2) $E\left(\left|\bar{X}_{t}\right|\right) \leqslant \infty$
3) $\underline{\bar{X}}_{t}$ is $\mathcal{F}_{t}$ adabled

Since $w_{t}$ is a Mautingale

$$
\begin{aligned}
& E\left(\underline{x}_{t} \mid \mathcal{F}_{s}\right)=E\left(x_{0}+\omega_{t} \mid \mathcal{F}_{s}\right) \\
& =E\left(x_{0} \mid \mathcal{F}_{s}\right)+E\left(\omega_{t} \mid \mathcal{F}_{s}\right) \\
& =x_{0}+\omega_{s}=\bar{x}_{s}
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left(\left|x_{0}+\omega_{\perp}\right|\right) \leq E\left(\left|x_{0}\right|+\left|\omega_{t}\right|\right) \\
& =E\left(\left|x_{0}\right|\right)+E\left(\left|\omega_{t}\right|\right) \\
& =\left|x_{0}\right|+\sqrt{\frac{\partial t}{\pi}}<\infty
\end{aligned}
$$

$Z_{t}$ will be $\mathcal{F}_{t}$ adapted since it is a function of $\omega_{t}$ and $w^{\prime}$. is $\mathfrak{F}_{t}$ adapted.

Let $T=\inf \left\{t \geqslant 0: \bar{x}_{t} \in(a, b)\right\}$ define the first exit time of $X_{t}$ from the interval $(a, b)$ then the optional stoping theorem gives

$$
\begin{aligned}
& E\left(\bar{X}_{T} \mid \bar{X}_{0}=x_{0}\right)=E\left(x_{0}+\omega_{T} \mid \underline{X}_{0}=x_{0}\right) \\
= & E\left(x_{0} \mid \bar{X}_{0}=x_{0}\right)+E\left(\omega_{0} \mid \bar{X}_{0}=x_{0}\right)
\end{aligned}
$$

$=x_{0}+0=x_{0}$
If $a \leqslant x_{0} \leqslant b$ then $X_{t}$ will exit the interval when $\underline{X}_{T}=a$ or $\bar{x}_{T}=b$. If the probability of the two events is defined by

$$
P\left(\underline{X}_{T}=a \mid \underline{X}_{0}=x_{0}\right)+P\left(\underline{X}_{T}=b \mid \underline{X}_{0}=x_{0}\right)=1
$$

Then from the definition of expectation
$E\left(X_{T}\left(X_{0}=X_{0}\right)=a P\left(X_{T}=a \mid X_{0}=X_{0}\right)\right.$

$$
+b P\left(Z_{T}=b \mid \bar{X}_{0}=\chi_{0}\right)
$$

Then from the optional stopping theorem result

$$
\begin{aligned}
x_{0}= & a P\left(X_{T}=a \mid X_{0}=x_{0}\right) \\
& +b P\left(X_{T}=b \mid X_{0}=x_{0}\right)
\end{aligned}
$$

Now if the exit is through a

$$
T_{a}<T_{b}
$$

$$
P\left(X_{T}=a \mid \bar{X}_{0}=x_{0}\right)=P\left(T_{a}<T_{b}\right)
$$

and if the exit is through b

$$
T_{b} \geqslant T_{a}
$$

$$
P\left(Z_{T}=b \mid \bar{X}_{0}=x_{0}\right)=P\left(T_{b} \leqslant T_{a}\right)
$$

So

$$
x_{0}=a P\left(T_{a}<T_{b}\right)+b P\left(T_{b} \leqslant T_{a}\right)
$$

but

$$
P\left(T_{b} \leqslant T_{a}\right)=1-P\left(T_{a}<T_{b}\right)
$$

So

$$
\begin{aligned}
x_{0} & =a P\left(T_{a}<T_{b}\right)+b\left[1-P\left(T_{a}<T_{b}\right)\right] \\
& =(a-b) P\left(T_{a}<T_{b}\right)+b \\
\Rightarrow P\left(T_{a}<T_{b}\right) & =\frac{x_{0}-b}{a-b}=\frac{b-x_{c}}{b-a}
\end{aligned}
$$

* Let $(\Omega, F, P)$ be a probability space and let $w_{t}$ be a standard Wiener Process with respect to the filtration $\mathcal{F}_{t}, t \geqslant 0$.
By writing
$\bar{X}_{t}=x+\omega_{t} \quad x \in \mathbb{R}$ show that
$\bar{x}_{t}$ and $\left(\bar{x}_{t}-x\right)-t$ are contincious martingales
let

$$
T=\inf \left\{t \geqslant 0: \bar{X}_{t} \in(a, b)\right\}
$$

be the first exit time from the interval $(a, b), a<x<b$ and assume $T<\infty$ amost surely show, using the optional stopping theorem, that

$$
P\left(X_{T}=a \mid \bar{x}_{0}=x\right)=\frac{b-x}{b-a}
$$

and

$$
P\left(\bar{X}_{T}=b \mid \bar{X}_{0}=x\right)=\frac{x-a}{b-a}
$$

withe

$$
E\left(\bar{X}_{T}\right)=(b-x)(x-a)
$$

Show that $I_{T}=\left\{\left(Z_{t}-x\right)^{2}-t: t \geqslant 0\right\}$ is a martingale,

$$
\begin{aligned}
& E\left[\left(X_{t}-x\right)^{2}-t \mid \mathcal{F}_{s}\right]=E\left(\omega_{t}^{2}-t \mid \mathcal{F}_{s}\right) \\
= & E\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)^{2}-t \mid \mathcal{F}_{s}\right] \\
= & E\left[\left(\omega_{t}-\omega_{s}\right)^{2}+2 \omega_{s}\left(\omega_{t}-\omega_{s}\right)+\omega_{s}^{2} \cdot t \mid \mathcal{F}_{s}\right] \\
= & E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right]+2 E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \mathcal{F}_{s}\right] \\
& +E\left(\omega_{s}^{2} \mid \mathcal{F}_{s}\right)-E\left(t \mid \mathcal{F}_{s}\right) \\
= & t^{2}-s+2 E\left(\omega_{s} \omega_{t} \mid \mathcal{F}_{s}\right)-2 E\left(\omega_{s}^{2} \mid \mathcal{F}_{s}\right) \\
& +\omega_{s}^{2}-t^{2} \\
= & \omega_{s}^{2}-s+2 \omega_{s} E\left(\omega_{t} \mid \mathcal{F}_{s}\right)-2 \omega_{s}^{2} \\
= & \omega_{s}^{2}-s+2 \omega_{s}^{2}-2 \omega_{s}^{2}=\omega_{s}^{2}-s
\end{aligned}
$$

and

$$
\begin{aligned}
& E\left[\left|\left(X_{t}-x\right)^{2}-t\right|\right]=E\left(\left|\omega_{t}^{2}-t\right|\right) \\
& \leqslant E\left(\left|\omega_{t}^{2}\right|\right)=E\left(\omega_{t}^{2}\right)=t<\infty
\end{aligned}
$$

Finally since $\mathcal{W}_{t}$ is $\mathcal{F}_{t}$ adapted $\bar{I}_{t}$ is $f_{t}$ adapted.

Since $\bar{I}_{t}$ is a martingale

$$
\bar{Z}_{t} \Perp \bar{X}_{s} \quad 0 \leqslant s<t
$$

and $a \leqslant x \leqslant b$ the definition of expectation where the exit time $T$ is defined by either $X_{T}=a$ or $X_{T}=b$. If the probability of these events is denoted lby

$$
P\left(\bar{X}_{T}=a \mid \bar{X}_{0}=x\right)+P\left(\bar{X}_{T}=b \mid \bar{X}_{0}=x\right)=1
$$

$E\left(\bar{X}_{T} \mid \bar{X}_{0}=x\right)=a P\left(\bar{X}_{T}=a \mid \bar{X}_{0}=x\right)$
$+b P\left(X_{\tau}=b\left(X_{0}=x\right)\right.$
using the optional stopping time result from the previous problem

$$
E\left(\underline{\bar{x}}_{T} \mid \bar{x}_{0}=x\right)=x
$$

gives

$$
\begin{aligned}
& E\left(X_{T} \mid \bar{X}_{0}=x\right)=a P\left(\bar{X}_{T}=a \mid \bar{X}_{0}=x\right) \\
& +b P\left(\bar{I}_{T}=b \mid \bar{X}_{0}=x\right)=x
\end{aligned}
$$

Now by definition
$P\left(\bar{X}_{T}=a \mid \bar{X}_{0}=x\right)+P\left(X_{T}=b \mid \underline{X}_{0}=x\right)=1$
$=P \quad P\left(X_{T}=a \mid X_{0}=x\right)=1-P\left(X_{T}=b \mid X_{0}=x\right)$
50

$$
\begin{aligned}
& a P\left(\mathbb{X}_{T}=a \mid \mathbb{X}_{0}=x\right)+b\left[\left(-P\left(\mathbb{X}_{T}=a \mid \bar{X}_{d}=x\right)\right]\right. \\
& =x
\end{aligned}
$$

$\Rightarrow \quad x-b=(a-b) P\left(\Sigma_{T}=a \mid \Sigma_{0}=x\right)$
$\Rightarrow P\left(X_{T}=a\left(X_{0}=x\right)=\frac{b-x}{b-a}\right.$
and

$$
\begin{aligned}
& P\left(X_{T}=b \mid X_{0}=x\right)=1-P\left(X_{t}=a \mid X_{0}=x\right) \\
& =1-\frac{b-x}{b-a}=\frac{(b-a)-(b-x)}{b-a} \\
& =\frac{x-a}{b-a}
\end{aligned}
$$

Now from the optional stopping
Theorem with Theorem with

$$
\begin{aligned}
& \quad \bar{I}_{T}=\left(\overline{\underline{X}}_{T}-x\right)^{2}-T \\
& E\left(\underline{I}_{T} \mid \underline{Z}_{0}=x\right)=E\left[\left(\underline{X}_{T}-x\right)^{2}-T \mid \bar{X}_{0}=x\right] \\
& =E\left[\left(\bar{X}_{0}-x\right)^{2}-0 \mid \underline{X}_{0}=x\right] \\
& =E\left[(x-x)^{2} \mid \bar{S}_{0}=x\right]=0
\end{aligned}
$$

80

$$
\begin{aligned}
& E\left[\left(\underline{X}_{T}-x\right)^{2}-T \mid \underline{X}_{0}=x\right]=0 \\
\Rightarrow & E\left[\left(\bar{X}_{T}-x\right)^{2} \mid \underline{X}_{0}=x\right]-E\left(T \mid \underline{X}_{0}=x\right) \\
\Rightarrow & E\left[\left(\underline{X}_{T}-x\right)^{2} \mid \underline{X}_{0}=x\right]=E\left(T \mid \bar{X}_{0}=x\right)
\end{aligned}
$$

using the definition of expectation and the previously defined events $P\left(X_{T}=a \mid X_{0}=x\right)$ and $P\left(X_{T}=b \mid X_{0}=x\right)$
$E\left[\left(X_{T}-x\right)^{2} \mid X_{0}=x\right]=(a-x)^{2} P\left(X_{T}=a\left(\bar{X}_{0}=x\right)\right. +(b-x)^{2} P\left(\underline{X}_{T}=b \mid \underline{X}_{0}=x\right)$
$=(a-x)^{2} \frac{(b-x)}{b-a}+(b-x)^{2} \frac{(x-a)}{b-a}$

$$
\begin{aligned}
& =\frac{1}{b-a}\left[(x-a)^{2}(b-x)+(b-x)^{2}(x-a)\right] \\
& =\frac{1}{b-a}(x-a)(b-x)[(x-a)+(b-x)] \\
& =\frac{1}{b-a}(x-a)(b-x)(b-a) \\
& =(x-a)(b-x) \\
& \text { Thus } \\
& \quad E\left(T \mid E_{0}=x\right)=(x-a)(b-x)
\end{aligned}
$$

## Reflection Principle

Let $(\Omega, \mathfrak{F}, P)$ be a probability space and let

$$
X_{t}=\left\{\omega_{t}: t \geqslant 0\right\}
$$

be a standard wiener process. Let $T$ be a stopping time for $\omega_{t}$ a define

$$
\tilde{\omega}_{t}= \begin{cases}\omega_{t} & t \leqslant T \\ 2 \omega_{T}-\omega_{t} & t>T\end{cases}
$$

show that $\left\{\tilde{\omega}_{t}: t \geqslant 0\right\}$ is also a standard wiener process
![](https://cdn.mathpix.com/cropped/2025_09_20_fb52ce1b713208cb19bfg-132.jpg?height=751&width=1151&top_left_y=1101&top_left_x=164)

Thus $\tilde{\omega}_{t}$ is a process refected about $\omega_{\tau}$ starting at $T$.
If $T$ is finite the from the strong Morkou property of $\omega_{t}$, namely,

$$
\omega_{t}-\omega_{s} \| \omega_{s} \quad 0 \leqslant s<t
$$

then

$$
\begin{aligned}
I_{t} & =\left\{\omega_{t+T}-\omega_{T}: t \geqslant 0\right\} \\
-I_{t} & =\left\{-\left(\omega_{t+T}-\omega_{T}\right): t \geqslant 0\right\}
\end{aligned}
$$

It defines the increments between $\omega_{t}$ and $\omega_{T}$ and $-\underline{y}_{t}$ the increments between $\tilde{\omega}_{t}$ and $\tilde{\omega}_{T}$
are independent of,

$$
\begin{gathered}
\bar{X}_{t}=\left\{\omega_{t}: t \geqslant 0\right\} \\
\bar{X}_{t} \Perp \bar{I}_{t} \quad \text { and } \quad \bar{X}_{t} \Perp-\bar{I}_{t}
\end{gathered}
$$

Now

$$
\begin{aligned}
& I_{t} \sim N(0, t) \\
& -I_{t} \sim N(0, t)
\end{aligned}
$$

also

$$
\bar{X}_{t} \sim N(0, t)
$$

so the pairs

$$
\left(\bar{X}_{t}, \bar{I}_{t}\right) \text { and }\left(\bar{X}_{t},-\bar{I}_{t}\right)
$$

have the same distributions
Both $\bar{X}_{t}$ and $\bar{I}_{t}$ ave defined on the intervals $[O, T]$ and $[0, \infty)$
using the indicator functions

$$
\begin{aligned}
& \overline{I I}_{\{t \leqslant T\}}= \begin{cases}1 & t \leqslant T \\
0 & t>T\end{cases} \\
& \bar{I}_{\{t \geqslant T\}}= \begin{cases}0 & t<T \\
1 & t \geqslant T\end{cases}
\end{aligned}
$$

Consider the process obtained by pasting the processes together $\Phi(\mathbb{Z}: \bar{Y})=\left[\bar{X}_{t} \bar{I}_{\{-t \leqslant T\}}+\left(\underline{I}_{t-T}+\omega_{T}\right) \underline{I}_{\{t \geqslant T\}}\right]$
$\Phi(\mathbb{X}:-\mathbb{I})=\left[\bar{X}_{t} \mathbb{I}\{t \leqslant t\}^{+}\left(-\bar{I}_{t-T}+\omega_{T}\right) \mathbb{I}\{t \geqslant \tau\}\right]$

But

$$
I_{t-T}+\omega_{T}=\left(\omega_{t}-\omega_{T}+\omega_{T}\right)=\omega_{t}
$$

and

$$
\begin{aligned}
-I_{t-T}+\omega_{T} & =-\left(\omega_{t}-\omega_{T}\right)+\omega_{T} \\
& =2 \omega_{T}-\omega_{t} \\
& =\tilde{\omega}_{t}
\end{aligned}
$$

Since $\bar{y}_{t-T}$ and $-\underline{y}_{t-T}$ are standard wiener processes given $T \tilde{\omega}_{t}$ is a standard Wiener process.

## Reflection Equality

Let $(\Omega, F, P)$ be a probability space and let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process. By defining

$$
T_{m}=\inf \left\{-t \geqslant 0: \omega_{t}=m\right\} \quad m>0
$$

as the first passage time then for $\omega \leqslant m, m>0$ show that

$$
P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant 2 m \cdot \omega\right)
$$

From the Reflection Principle

$$
\tilde{\omega}_{t}= \begin{cases}\omega_{t} & t \leqslant T_{m} \\ 2 m-\omega_{t} & t>T_{m}\end{cases}
$$

It is known that $\tilde{\omega}_{t}$ when $t>T$ has the same distribution as $t \leqslant T_{m}$, so
$P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(T_{m} \leqslant t, 2 \omega_{T}-\omega_{t} \leqslant \omega\right)$
Now with $W_{T}=m$

$$
\begin{aligned}
& P\left(T_{m} \leqslant t, 2 m \cdot \omega_{t} \leqslant \omega\right)=P\left(2 m-\omega_{t} \leqslant \omega\right) \\
& -P\left(T_{m} \geqslant t, 2 m-\omega_{t} \leqslant \omega\right)
\end{aligned}
$$

$=P\left(\omega_{t} \geqslant 2 m-\omega\right)-P\left(T_{m} \geqslant t, \omega_{t} \geqslant 2 m \cdot \omega\right)$
now $\omega \leq m$ then

$$
2 m-\omega \geqslant 2 m-m=m
$$

50

$$
\omega_{t} \geqslant m
$$

But $\quad t \leqslant T_{m} \Leftrightarrow \omega_{t} \leqslant m$ so

$$
P\left(T_{m} \geqslant t, \omega_{t} \geqslant 2 m-\omega\right)=0
$$

and

$$
P\left(\tau_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant 2 m-\omega\right)
$$

## First Passage Time Densily Function

Let $(\Omega, F, P)$ be a probability space and let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process and define the stopping trme

$$
T_{\omega}=\operatorname{in} f\left\{t \geqslant 0: \omega_{t}=\omega\right\} \quad \omega \neq 0
$$

show using the reflection principal

$$
P\left(T_{\omega} \leqslant t\right)=1+\Phi\left(-\frac{|\omega|}{\sqrt{t}}\right) \cdot \Phi\left(\frac{|\omega|}{\sqrt{t}}\right)
$$

and the probability density function of $T_{\omega}$ is given by

$$
f_{T \omega}(t)=\frac{|\omega|}{t \sqrt{2 \pi t}} e^{-\omega^{2} / 2 t}
$$

Now consider the case $\omega>0$ b.) definition

$$
\begin{aligned}
P\left(T_{\omega} \leqslant t\right)= & P\left(T_{\omega} \leqslant t, \omega_{t} \leqslant \omega\right) \\
& +P\left(T_{\omega} \leqslant t, \omega_{t} \geqslant \omega\right)
\end{aligned}
$$

for the first term using the Reflection Equality

$$
P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant 2 m-\omega\right)
$$

with $m=\omega$ gives

$$
P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant \omega\right)
$$

For the second term

$$
\begin{gathered}
P\left(T_{m} \leqslant t, \omega_{t} \geqslant \omega\right)=P\left(\omega_{t} \geqslant \omega\right)- \\
P\left(T_{m} \geqslant t, \omega_{t} \geqslant \omega\right.
\end{gathered}
$$

but

$$
\omega_{t} \geqslant \omega \Rightarrow T_{m} \leqslant t
$$

80

$$
P\left(T_{m} \geqslant t, \omega_{t} \geqslant \omega\right)=0
$$

thus

$$
\begin{aligned}
P\left(T_{m} \leqslant t\right) & =2 P\left(\omega_{t} \geqslant \omega\right) \\
& =\frac{2}{\sqrt{2 \pi t}} \int_{\omega}^{\infty} e^{-x^{2} / \Delta t} d x
\end{aligned}
$$

for the integral using the change of variables

$$
y=\frac{x}{\sqrt{t}}=\sqrt{t} d y=d x
$$

$$
\begin{aligned}
& \frac{2}{\sqrt{2 \pi t}} \int_{\omega}^{\infty} e^{-x^{2} t t} d x=\frac{2}{\sqrt{2 \pi t}} \int_{\omega / t}^{\infty} \sqrt{t} e^{-y^{2} / 2} d y \\
& =\frac{2}{\sqrt{2 \pi}} \int_{\omega / \sqrt{t}}^{\infty} e^{-y^{2} / 2} d y \\
& =2 \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{-\omega / \sqrt{t}} e^{-y^{2} / 2} d y \\
& =2 \Phi\left(-\frac{\omega}{\sqrt{t}}\right)
\end{aligned}
$$

But

$$
\Phi\left(\frac{-\omega}{\sqrt{t}}\right)=1-\Phi\left(\frac{\omega}{\sqrt{t}}\right)
$$

so for $\omega>0$

$$
P\left(T_{m} \leqslant t\right)=1+\Phi\left(-\frac{\omega}{\sqrt{t}}\right)-\Phi\left(\frac{\omega}{\sqrt{t}}\right)
$$

Now for $\omega \leqslant 0$

$$
\begin{aligned}
P\left(T_{m} \leqslant t\right)= & P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right) \\
& +P\left(T_{m} \leqslant t, \omega_{t} \geqslant \omega\right)
\end{aligned}
$$

$=P\left(T_{m} \leqslant t,-\omega_{t} \geqslant-\omega\right)+P\left(T_{m} \leqslant T,-\omega_{t} \leqslant-\omega\right)$
but

$$
\omega_{t} \sim-\omega_{t}=\tilde{\omega}_{t} \sim N(0, t)
$$

as before using the Reflection Equality

$$
P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant \omega\right)
$$

gives

$$
P\left(T_{m} \leqslant t, \tilde{\omega}_{t} \leqslant-\omega\right)=P\left(\tilde{\omega}_{t} \geqslant-\omega\right)
$$

and

$$
P\left(\tau_{m} \leqslant t, \tilde{\omega}_{t} \geqslant-\omega\right)=P\left(\tilde{\omega}_{t} \geqslant \cdot \omega\right)
$$

since $\quad \tilde{\omega}_{t} \geqslant-\omega \Rightarrow T_{m} \leqslant t$
thus
$P\left(T_{m} \leqslant T\right)=2 P\left(\tilde{\omega}_{t} \geqslant-\omega\right)$
$=\frac{2}{\sqrt{2 \pi t}} \int_{-\omega}^{\infty} e^{-x_{2}^{2} t} d x$
using $y=\frac{x}{\sqrt{t}}$ gives

$$
\begin{aligned}
P\left(T_{m} \leqslant T\right) & =2 \frac{\sqrt{t}}{\sqrt{2 \pi t}} \int_{-\omega / \sqrt{t}}^{\infty} e^{-y^{2} / 2} d y \\
& =2 \frac{1}{\sqrt{a \pi}} \int_{-\infty}^{\omega / \sqrt{t}} e^{-y^{2} / 2} d y \\
& =2 \Phi\left(\frac{\omega}{\sqrt{t}}\right)
\end{aligned}
$$

but

$$
\Phi\left(\frac{\omega}{\sqrt{t}}\right)=1-\Phi\left(-\frac{\omega}{\sqrt{2}}\right)
$$

so for $\omega \leqslant 0$

$$
P\left(T_{m} \leqslant T\right)=1+\Phi\left(\frac{\omega}{\sqrt{t}}\right)-\Phi\left(-\frac{\omega}{\sqrt{2}}\right)
$$

but for $\omega \geqslant 0$

$$
P\left(T_{m} \leqslant T\right)=1+\Phi\left(\frac{-\omega}{\sqrt{t}}\right)-\Phi\left(\frac{\omega}{\sqrt{2}}\right)
$$

SO

$$
P\left(T_{m} \leqslant T\right)=1+\frac{\Phi}{}\left(-\frac{|\omega|}{\sqrt{t}}\right)-\Phi\left(\frac{|\omega|}{1 t}\right)
$$

The density is given by

$$
\begin{aligned}
f_{T_{m}}(t) & =\frac{d}{d t} P\left(T_{m} \leqslant t\right) \\
& =\frac{d}{d t}\left[1+\Phi\left(-\left\lvert\, \frac{|\omega|}{\sqrt{t}}\right.\right)-\Phi\left(\frac{|\omega|}{\sqrt{t}}\right)\right]
\end{aligned}
$$

let

$$
y=-\frac{|\omega|}{\sqrt{t}}
$$

then

$$
\begin{aligned}
f_{T_{m}}(t) & =\frac{d}{d t}[1+\Phi(y(t))-\Phi(-y(t))] \\
& =\frac{d}{d t}[2 \Phi(y(t))] \\
& =2 \frac{d y}{d t} \frac{d \Phi(y)}{d y}
\end{aligned}
$$

but for $\omega \geqslant 0$
$\frac{d y}{d t}=\frac{d}{d t}\left(-\frac{\omega}{t}\right)=-\frac{1}{2 t^{3 / 2}}(-\omega)=\frac{\omega}{2 t}^{3 / 2}$ and for $\omega \leqslant 0$

$$
\frac{d y}{d t}=\frac{d}{d t}\left(\frac{\omega}{\sqrt{t}}\right)=-\frac{1}{2 t^{3 / 2}}(\omega)=-\frac{\omega}{2 t^{3 / 2}}
$$

theses for $-\infty<\omega<\infty$

$$
\frac{d y}{d t}=\frac{|\omega|}{2 t^{3 / 2}}
$$

Now

$$
\begin{aligned}
\frac{d}{d y} \Phi(y) & =\frac{d}{d y} \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{y} e^{-x^{2} / 2} d x \\
& =\frac{1}{\sqrt{2 \pi}} e^{-y^{2} / 2}
\end{aligned}
$$

so

$$
\begin{aligned}
f T_{m}(t) & =2\left(\frac{|\omega|}{2 t^{3 / 2}}\right) \frac{1}{\sqrt{2 \pi}} e^{-\omega^{2} / 2 t} \\
& =\frac{|\omega|}{t \sqrt{2 \pi t}} e^{-\omega^{2} / 2 t}
\end{aligned}
$$

* Let $\left(\Omega, \mathcal{F}, P_{\text {let }}\right)$ be a probability space and let

$$
M_{t}=\max _{0 \leqslant s \leqslant t} \omega_{s}
$$

be a maximum value reached by the wiener process $\left\{\omega_{t}: t \geqslant 0\right\}$ on the time interval $[0, t]$.
Show using the Reflection Principal
$P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)=$

$$
\begin{cases}\Phi\left(\frac{x}{\sqrt{t}}\right)-\Phi\left(\frac{x-2 a}{\sqrt{t}}\right) & a \geqslant 0, x \leqslant a \\ \Phi\left(\frac{a}{\sqrt{t}}\right)-\Phi\left(\frac{-a}{\sqrt{t}}\right) & a \geqslant 0, x \geqslant a \\ 0 & a \leqslant 0\end{cases}
$$

The Reflection Equality is given by
$P\left(T_{m} \leqslant t, \omega_{t} \leqslant \omega\right)=P\left(\omega_{t} \geqslant 2 \omega_{\tau}-\omega\right)$

Now for $a \geqslant 0$ and $x \leqslant a \quad \mu_{t} \geqslant a$ can be computed from the Reflection Equality
$P\left(M_{t} \geqslant a, \omega_{t} \leqslant x\right)=P\left(T_{a} \leqslant t, \omega_{t} \leqslant x\right)$
Since

$$
M_{t} \geqslant a \Leftrightarrow T_{a} \leqslant t
$$

so

$$
\begin{aligned}
& P\left(T_{a} \leqslant t, \omega_{t} \leqslant x\right)=P\left(\omega_{t} \geqslant 2 a-x\right) \\
= & \frac{1}{2 \pi t} \int_{2 a-x}^{\beta} e^{-z^{2} / 2 t} d z \\
= & \frac{1}{2 \pi t}\left[1-\int_{-\infty}^{2 a-x} e^{-z^{2} / 2 t} d z\right]
\end{aligned}
$$

let

$$
y=\frac{z}{\sqrt{t}} \Rightarrow \sqrt{t} d y_{1}=d z
$$

so
$\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{2 a-x} e^{-z^{2} / 2 t}=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{\frac{2 a-x}{\sqrt{t}}} \sqrt{t} e^{-y^{2} / 2} d y$
$=\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{2 a-x} e^{-y^{2} / 2} d y=\Phi\left(\frac{\partial a-x}{\partial t}\right)$

50

$$
\begin{aligned}
& P\left(M_{t} \geqslant a, \omega_{t} \leqslant x\right)=1-\Phi\left(\frac{2 a-x}{\sqrt{t}}\right) \\
& =\Phi\left(\frac{x-2 a}{\sqrt{t}}\right)
\end{aligned}
$$

The desired result can now be determined

$$
\begin{aligned}
& P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)=P\left(\omega_{t} \leqslant x\right) \\
& -P\left(M_{t} \geqslant a, \omega_{t} \leqslant x\right)
\end{aligned}
$$

But

$$
\begin{aligned}
& P\left(\omega_{t} \leq x\right)=\frac{1}{\sqrt{2 \pi t}} \int_{-\infty}^{x} e^{-z^{2} / 2 t} d z \\
& =\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x / t} e^{-y^{2} / 2} d y=\Phi\left(\frac{x}{t}\right)
\end{aligned}
$$

So

$$
P\left(\mu_{z} \leqslant a, \omega_{t} \leqslant x\right)=\Phi\left(\frac{x}{\sqrt{2}}\right)-\Phi\left(\frac{x-2 a}{\sqrt{t}}\right)
$$

For $a \geqslant 0$ and $x \geqslant a$
$P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)=P\left(M_{t} \leqslant a\right)$

- $P\left(M_{t} \leqslant a, \omega_{t} \geqslant x\right)$

Now by definition
$M_{t}=\max _{0 \leqslant s \leqslant t} \omega_{s} \Rightarrow M_{t} \geqslant \omega_{t}$
and since $a \geqslant 0, x \geqslant a$ and $M_{t} \geqslant \omega_{t}$

$$
\omega_{t} \leqslant M_{t} \leqslant a \leqslant x
$$

50

$$
P\left(M_{t} \leqslant a, \omega_{t} \geqslant x\right)=0
$$

so

$$
P\left(m_{t} \leqslant a, \omega_{t} \leqslant x\right)=P\left(m_{t} \leqslant a\right)
$$

Now

$$
P\left(\mu_{t} \leqslant a\right)=1-P\left(\mu_{t} \geqslant a\right)
$$

but

$$
\mu_{t} \geqslant a \Rightarrow T a \leqslant t
$$

so

$$
P\left(M_{t} \leqslant a\right)=1-P\left(T_{a} \leqslant t\right)
$$

Previoushy it was shown that

$$
P\left(T_{a} \leqslant t\right)=1+\Phi\binom{-a}{\sqrt{t}}-\Phi\left(\frac{a}{\sqrt{t}}\right)
$$

50

$$
\begin{aligned}
P\left(M_{t} \leqslant a\right) & =1-\left[1+\Phi\left(-\frac{a}{\sqrt{t}}\right)-\Phi\left(\frac{a}{\sqrt{2}}\right)\right] \\
& =\Phi\left(\frac{a}{\sqrt{t}}\right)-\Phi\left(-\frac{a}{\sqrt{t}}\right)
\end{aligned}
$$

and

$$
P\left(M_{t} \leqslant a, w_{t} \leqslant x\right)=\Phi\left(\frac{a}{\sqrt{t}}\right)-\Phi\left(-\frac{a}{\sqrt{t}}\right)
$$

And finally when $a \leqslant 0$ and
since

$$
\mu_{t} \geqslant \omega_{0}=0
$$

$$
P\left(M_{t} \leqslant a, \quad \omega_{t} \leqslant x\right)=0
$$

$$
\begin{aligned}
& P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)= \\
& \begin{cases}\Phi\left(\frac{x}{\sqrt{t}}\right)-\Phi\left(\frac{x-2 a}{\sqrt{t}}\right) & a \geqslant 0, x \leqslant a \\
\Phi\left(\frac{-a}{\sqrt{t}}\right)-\Phi\left(\frac{a}{\sqrt{t}}\right) & a \geqslant 0, x \geqslant a \\
0 & a \leqslant 0\end{cases}
\end{aligned}
$$

The joint density function is given by
$f_{M_{t}, \omega_{t}}(a, x)=\frac{\partial^{2}}{\partial a \partial x} P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)$
Since $P\left(\mu_{t} \leqslant a, \omega_{t} \leqslant x\right)$ is a function of $a$ and $x$ only for $a \geqslant 0, x \leqslant a$ it is the only crteroal for which the density is nonzero, so with

$$
\begin{gathered}
u=\frac{x}{\sqrt{t}} \quad v=\frac{x-2 a}{\sqrt{t}} \\
\frac{\partial^{2}}{\partial a \partial x}\left[\Phi\left(\frac{x}{\sqrt{t}}\right)-\Phi\left(\frac{x-2 a}{\sqrt{t}}\right)\right] \\
=\frac{\partial^{2}}{\partial a \partial y}[\Phi(u(x))-\Phi(v(x, a))]
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{\partial}{\partial a}\left[\frac{\partial u}{\partial x} \frac{d}{d u} \Phi(u)-\frac{\partial v}{\partial x} \frac{d}{d v} \Phi(v)\right] \\
& =\frac{\partial}{\partial a}\left[\frac{1}{\sqrt{t}} \frac{1}{\sqrt{2 \pi}} e^{-u^{2} / 2} \cdot \frac{1}{\sqrt{t}} \frac{1}{\sqrt{2 \pi}} e^{-v^{2} / 2}\right] \\
& =0-\frac{1}{\sqrt{2 \pi t}} \frac{\partial}{\partial a} e^{-v^{2} / 2} \\
& \left.=\left(-\frac{1}{\sqrt{2 \pi t}}\right) \frac{\partial v}{\partial a}(-v) e^{-v^{2} / 2}\right) \\
& =\left(-\frac{1}{\partial \pi t}\right)\left(-\frac{2}{\sqrt{t}}\right)\left[\frac{(x-2 a)}{\sqrt{t}}\right] e^{-(x-2 a)^{2} / 2 t} \\
& =\frac{2}{\sqrt{2 \pi t}}(2 a-x) e^{-(x-2 a)^{2} / 2 t} \\
& =\frac{\partial(2 a-x)}{t \sqrt{2 \pi t}} e^{-(x-2 a)^{2} / 2 t} \\
& \operatorname{Thus}^{f_{m_{t}} \omega_{t}(a, x)=\left\{\begin{array}{cc}
2 \frac{(2 a-x)}{t / 2 \pi t} & e^{-(x-2 a)^{2} / 2 t} \\
0 & \text { otherwise }
\end{array}\right.}
\end{aligned}
$$

* Let $(\Omega, F, P)$ be a probobility space and let

$$
m_{t}=\min _{0 \leqslant s \leqslant t} \omega_{t}
$$

be the minimum value recched by the standard wiener process $\left\{\omega_{t}: t \geqslant 0\right\}$ on the inerval $0 \leq s \leq t$.
Show that for $t \geqslant 0$

$$
P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)= \begin{cases}\Phi\left(\frac{-x}{\sqrt{t}}\right)-\Phi\left(\frac{2 b-x}{\sqrt{t}}\right) & b \leqslant 0, b \leqslant x \\ \Phi\left(\frac{-b}{\sqrt{t}}\right)-\Phi\left(\frac{b}{\sqrt{t}}\right) & b \leqslant 0, b \geqslant x \\ 0 & b \geqslant 0\end{cases}
$$

and the joint probability density function is

Now using

$$
m_{t}=\min _{0 \leqslant s \leqslant t} \omega_{s}=-\max _{0 \leqslant s \leqslant t}\left(-\omega_{s}\right)
$$

Which can be seen from considering $\omega_{s} \geqslant 0$ the max negative value will have the smallest magnitude. and multiplying by -1 will be the minimum value. Likewise if $\omega_{s}$ ' 0 the max negative value will have the largest magnitude and multiplying by -1 will give the minimum value

So subititreting into the desired probability gives
$P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)$
$=P\left(-\max _{0 \leqslant s \leqslant t}\left\{-\omega_{s}\right\} \geqslant b, \omega_{t} \geqslant x\right)$
$=P\left(\max _{0 \leqslant s \leqslant t}\left\{\cdot \omega_{s}\right\} \leqslant-b,-\omega_{t} \leqslant-x\right)$
Now
$\omega_{t} \sim N(0, t)$
and from the symmetry of ture

## Normal distribution

## $-\omega_{t} \sim N(0, t)$

letting $\tilde{\omega}_{t}=-w_{t}$ and making a change of variables gives
$P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)$
$=P\left(\max _{0 \leqslant s \leqslant t} \tilde{\omega}_{s} \leqslant-b, \tilde{\omega} \leqslant-x\right)$
Let

$$
\tilde{M}_{t}=\max _{0 \leqslant s \leqslant t} \tilde{\omega}_{s}
$$

then
$P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)=P\left(\tilde{\mu}_{t} \leqslant-b, \tilde{\omega} \leqslant-x\right)$
This has the form of the previous problem, namely
$P\left(M_{t} \leqslant a, \omega_{t} \leqslant x\right)=$

$$
\begin{cases}\Phi\left(\frac{x}{\sqrt{t}}\right)-\Phi\left(\frac{x-2 a}{\sqrt{t}}\right) & a \geqslant 0, x \leqslant a \\ \Phi\left(\frac{-a}{\sqrt{t}}\right)-\Phi\left(\frac{a}{\sqrt{t}}\right) & a \geqslant 0, x \geqslant a \\ 0 & a \leqslant 0\end{cases}
$$

for the first term letting

$$
\begin{gathered}
a=-b \text { and } x \rightarrow-x \text { gives } \\
-b \geqslant 0 \Rightarrow b \leqslant 0 \\
-x \leqslant-b \Rightarrow x \geqslant b
\end{gathered}
$$

and

$$
\begin{aligned}
P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right) & =\Phi\left(\frac{-x}{\sqrt{t}}\right) \cdot \Phi\left(-\frac{x+2 b}{\sqrt{t}}\right) \\
& =\Phi\left(-\frac{x}{\sqrt{t}}\right)-\Phi\left(\frac{2 b-x}{\sqrt{t}}\right)
\end{aligned}
$$

Now the second term

$$
\begin{array}{ll}
-b \geqslant 0=> & b \leqslant 0 \\
-x \geqslant-b=> & x \leqslant b
\end{array}
$$

## and

$P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)=\Phi\left(\frac{b}{\sqrt{t}}\right)-\Phi\left(\frac{-b}{\sqrt{t}}\right)$
Finally $-b \leqslant 0 \Rightarrow b \geqslant 0$
$P\left(m_{t} \geqslant b, \omega_{t} \geqslant x\right)=0$
putting things together gives
$P\left(m_{t} \geqslant b, w_{t} \geqslant x\right)=$

$$
\begin{array}{ll}
\Phi\left(\frac{-x}{\sqrt{t}}\right)-\Phi\left(\frac{2 b-x}{\sqrt{t}}\right) & b \leqslant 0, x \geqslant b \\
\Phi\left(\frac{b}{\sqrt{t}}\right)-\Phi\left(\frac{-b}{\sqrt{t}}\right) & b \leqslant 0, x \leqslant b \\
0 & b>0
\end{array}
$$

For the probability dencity using the result from the previous problem for

$$
P\left(M_{t} \leq a, w_{t} \leq x\right)
$$

$$
f_{\mu_{t}, \omega_{t}}(a, x)=\left\{\begin{array}{cc}
\frac{\partial(\partial a-x)}{t \partial a \pi t} e^{-(x-2 a)^{2} / \partial t} & a \geqslant 0, \\
0 & \text { otherwise }
\end{array}\right.
$$

Makins the same change of
variables

$$
x \rightarrow-x \quad a \rightarrow-b
$$

$f_{m_{t}, \omega_{t}}(b, x)= \begin{cases}-\frac{2(2 b-x) e^{-(2 b-x)^{2} / 2 t}}{t \sqrt{2 \pi t}} & b \leqslant 0 \\ 0 & x \geqslant b \\ 0 & \text { otherwise }\end{cases}$

## Quadratic Variation

Let $(\Omega, 7, P)$ be a probability space and let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process. Show that it has finite quadratic variation
$\langle\omega, \omega\rangle_{t}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t_{i+1}} \cdot \omega_{t_{i}}\right)^{2}=t$
where

$$
t_{i}=\frac{i t}{n} \quad t_{0}<t_{1}<\cdots<t
$$

and finally deduce that

$$
d \omega_{t} d \omega_{t}=d t
$$

Let

$$
\Delta \omega_{t_{i}}=\omega_{t_{i+1}}-\omega_{t_{i}} \sim N\left(0, t_{/ n}\right)
$$

so

$$
\begin{gathered}
E\left(\Delta \omega_{t_{i}}\right)=0 \quad E\left(\Delta \omega_{t_{i}}^{2}\right)=\frac{t}{n} \\
E\left(\Delta \omega_{t_{i}}^{4}\right)=3 \frac{t^{2}}{n^{2}}
\end{gathered}
$$

taking expectations gives
$E\left(\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta \omega_{t_{i . i}}^{2}\right)=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} E\left(\Delta \omega_{t_{i}}^{2}\right)$
$=\lim _{n \rightarrow \infty} \sum_{c=0}^{n-1} \frac{t}{n}=\lim _{n \rightarrow \infty} \frac{n t}{n}=t$
The expectation can be palled inside the sum berause

$$
\Delta \omega_{t_{i}} \Perp \Delta \omega_{t_{j}} \quad i \neq 1
$$

and

$$
E\left(\Delta \omega_{t i}\right)=0
$$

so the cross terms will vanish

$$
E\left(\Delta \omega_{t_{i}} \Delta \omega_{t_{j}}\right)=0 \quad i \neq j
$$

To show convergence of

$$
\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t_{i+1}} \cdot \omega_{t_{i}}\right)^{2}=t
$$

it must be shown that

$$
\lim _{n \rightarrow \infty} P\left(\left|\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}}^{2}\right)-t\right|>\delta\right)=0
$$

using the Onebysher inequality
gives

$$
P(|Z-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

$$
\begin{aligned}
& P\left(\left|\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}}^{2}\right)-t\right|>\delta\right) \\
& \leqslant \frac{1}{\delta^{2}} \operatorname{Var}\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}}^{2}\right)
\end{aligned}
$$

50
$\operatorname{Var}\left(\sum_{i=0}^{n-1} \Delta \omega_{t i}^{2}\right)=E\left[\left(\sum_{i=0}^{n-1} \Delta \omega_{i}^{2}-t\right)^{2}\right]$
$=E\left\{\left[\sum_{i=0}^{n-1}\left(\Delta \omega_{i}^{2}-\frac{t}{n}\right)\right]^{2}\right\}$
$=E\left[\sum_{j=0}^{n-1} \sum_{i=0}^{n-1}\left(\Delta \omega_{i}^{2}-\frac{t}{n}\right)\left(\Delta \omega_{j}^{2} \cdot \frac{t}{n}\right)\right]$
$=\sum_{j=0}^{n-1} \sum_{i=0}^{n-1} E\left[\left(\Delta \omega_{i}^{2}-\frac{t}{n}\right)\left(\Delta \omega_{j}^{2}-\frac{t}{n}\right)\right]$
$=\sum_{j=0}^{n-1} \sum_{i=0}^{n-1} E\left[\Delta \omega_{i}^{2} \Delta \omega_{i}^{2}-\frac{t}{n}\left(\Delta \omega_{i}^{2}+\omega_{j}^{2}\right)+\frac{t^{2}}{n^{2}}\right]$
now for $i \neq j$

$$
\begin{aligned}
& E\left[\Delta \omega_{i}^{2} \Delta \omega_{j}^{2}-\frac{t}{n}\left(\Delta \omega_{i}^{2}+\Delta \omega_{i}^{2}\right)+\frac{t^{2}}{n^{2}}\right] \\
& =E\left(\Delta \omega_{i}^{2} \Delta \omega_{j}^{2}\right) \cdot \frac{t}{n}\left[E\left(\Delta \omega_{i}^{2}\right)+E\left(\Delta \omega_{j}^{2}\right)\right] \\
& +\frac{t^{2}}{n^{2}} \\
& \text { since } \Delta \omega_{i}+\Delta \omega_{j} \text { for } c \neq j \\
& E\left(\Delta \omega_{i}^{2} \Delta \omega_{j}^{2}\right)=E\left(\Delta \omega_{i}^{2}\right) E\left(\Delta \omega_{j}^{2}\right) \\
& =\left(\frac{t}{n}\right)\left(\frac{t}{n}\right)=\frac{t^{2}}{n^{2}}
\end{aligned}
$$

so the cross terms vanish. If follows that
$\operatorname{Var}\left(\sum_{i=0}^{n-1} \Delta \omega_{t i}^{2}\right)=\sum_{i=0}^{n-1} E\left[\left(\Delta \omega_{i}^{2}-t\right)^{2}\right]$

$$
\begin{aligned}
& =\sum_{i=0}^{n-1} E\left[\Delta \omega_{i}^{4}-\frac{2 t \Delta \omega_{i}^{2}}{n}+\frac{t^{2}}{n^{2}}\right] \\
& =\sum_{i=0}^{n-1} E\left(\Delta \omega_{i}^{21}\right)-\frac{2 t}{n} E\left(\Delta \omega_{i}^{2}\right)+\frac{t^{2}}{n^{2}} \\
& =\sum_{i=0}^{n-1} \frac{3 t^{2}}{n^{2}}-\frac{2 t^{2}}{n^{2}}+\frac{t^{2}}{n^{2}} \\
& =\sum_{i=0}^{n-1} \frac{2 t^{2}}{n^{2}}
\end{aligned}
$$

It follows that
$\lim _{n \rightarrow \infty} P\left(\left|\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}}^{2}\right)-t\right|>\delta\right)$
$=\frac{1}{\delta^{2}} \lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{2 t^{2}}{n^{2}}=\frac{1}{\delta} \lim _{n \rightarrow \infty} \frac{2 t^{2}}{n}=0$
Thus

$$
\lim _{n \rightarrow \infty} \sum_{i=1}^{n-1} \Delta \omega_{t_{i}}^{2}=\int_{0}^{t} d \omega_{s} d \omega_{s}=t
$$

but

$$
t=\int_{0}^{t} d s
$$

$$
\int_{0}^{t} d \omega_{s} d \omega_{s}=\int_{0}^{t} d s
$$

differeniating with respect to $t$
gives

$$
d \omega_{i} d \omega_{t}=d t
$$

* Let ( $\Omega, \mathcal{F}, P$ ) be a probability space and let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard weiner process. Show that

$$
n-1
$$

$\lim _{n \rightarrow \infty} \sum_{i=0}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)\left(t_{i+1}-t_{i}\right)=0$
n-1
$\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(t_{i+1}-t_{i}\right)=0$

$$
t_{i}=\frac{i t}{n} \quad t_{0}<t_{1}<\cdots<t
$$

Let $\Delta w_{t_{i}}=w_{t_{i+1}}-w_{t_{i}}$ and
$\Delta t_{i}=t_{i+1}-t_{i}=t_{/ n}$
Also, let

$$
\begin{aligned}
& \mu_{\Delta \omega \Delta t}=E\left(\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta \omega_{t_{i}} \Delta t_{i}\right) \\
& \mu_{\Delta t^{2}}=E\left(\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)
\end{aligned}
$$

It must be shown that two expressions above converge to 0 as $n \rightarrow \infty$. Therefore it must be shown that
$\lim _{n \rightarrow \infty} P\left(\left|\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}} \Delta t_{i}\right)-\mu_{\Delta \omega \Delta t}\right| \geqslant \delta\right)=0$
and

$$
\lim _{n \rightarrow \infty} P\left(\left|\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)-\mu_{\Delta t^{2}}\right| \geqslant \delta\right)=0
$$

using the Chebyshev inequality
gives

$$
P(|Z-\mu| \geqslant k) \leqslant \frac{\sigma^{2}}{k^{2}}
$$

grues

$$
\begin{aligned}
& P\left(\left|\left(\sum_{i=0}^{n-1} \Delta w_{t_{i}} \Delta t_{i}\right)-\mu_{\Delta w_{\Delta t}}\right| \geqslant \delta\right) \\
& \leqslant \frac{1}{\delta^{2}} \operatorname{Var}\left(\sum_{i=0}^{n-1} \Delta w_{t_{i}} \Delta t_{i}\right)
\end{aligned}
$$

and
$P\left(\left\lvert\,\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}-\mu_{\Delta t^{2}} \mid \geqslant \delta\right) \leqslant \frac{1}{\delta} \operatorname{Var}\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)\right.\right.$
Now

$$
\begin{aligned}
\mu_{\Delta w_{\Delta t}} & =E\left(\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta w_{t_{i}} \Delta t_{i}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} E\left(\Delta w_{t_{i}} \Delta t_{i}\right)
\end{aligned}
$$

$$
=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta t_{i} E\left(\Delta \omega_{t_{i}}\right)=0
$$

since $\quad \Delta \omega_{t_{i}} \sim N(0, t)$

## and

$$
\begin{aligned}
\mu \Delta t^{2}= & E\left(\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \Delta t_{i}^{2}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} E\left(\Delta t_{i}^{2}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{t^{2}}{n^{2}} \\
& =\lim _{n \rightarrow \infty} \frac{t^{2}}{n}=0
\end{aligned}
$$

and

$$
\begin{aligned}
\operatorname{Var} & \left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}} \Delta t_{i}\right)=E\left[\left(\sum_{i=0}^{n-1} \Delta \omega_{t_{i}} \Delta t_{i}\right)^{2}\right] \\
& -\mu_{\Delta \omega \Delta t}^{2} \\
=E & {\left[\left(\sum_{i=0}^{n-1} \Delta \omega_{i} \Delta t\right)^{2}\right]=\sum_{i=0}^{n-1} E\left[\left(\Delta \omega_{i} \Delta t_{i}\right)^{2}\right] }
\end{aligned}
$$

Expectation can be brought inside
the summation since

$$
\Delta \omega_{t_{i}} \Perp \Delta \omega_{t_{j}} \quad i \neq j
$$

and $E\left(\Delta \omega_{t_{i}}\right)=0$
Thus
$\sum_{i=0}^{n-1} E\left[\left(\Delta \omega_{L_{i}} \Delta t_{i}\right)^{2}\right]=\sum_{i=0}^{n-1} \Delta t_{i}^{2} E\left(\Delta \omega_{i}^{2}\right)$
$=\frac{t^{2}}{n^{2}} \sum_{i=0}^{n-1} \frac{t}{n}=\frac{t^{2}}{n^{2}} t=\frac{t^{3}}{n^{2}}$
and
$\operatorname{var}\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)=E\left[\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)^{2}\right]-\mu_{\Delta-t^{2}}^{2}$
$=\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2}\right)^{2}=\left(\frac{t^{2}}{n}\right)^{2}=\frac{t^{4}}{n^{2}}$
so
$\lim _{n \rightarrow \infty} P\left(\mid\left(\sum_{i=0}^{n-1} \Delta w_{t_{i}} \Delta t_{i}\right) \geqslant \delta\right)=0$
and
$\lim _{n \rightarrow \infty} P\left(\mid\left(\sum_{i=0}^{n-1} \Delta t_{i}^{2} \mid \geqslant \delta\right)=0\right.$
$\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)\left(t_{i+1}-t_{i}\right)=\int_{0}^{t} d \omega_{s} d s$
$=0$
$\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(t_{i+1}-t_{i}\right)=\int_{0}^{t} d s d s=0$
Taking the derivative with respect to $t$ gives the
desived result
desired
result

$$
\begin{aligned}
d w_{t} d t & =0 \\
d t d t & =0
\end{aligned}
$$

## Stochastic Diffential Equations

A one dimensional stochastic fiefferential equation has the form

$$
d \underline{X}_{t}=\mu\left(\bar{X}_{t}, t\right) d t+\sigma\left(\bar{X}_{t}, t\right) d \omega_{t}
$$

Where $\left\{\omega_{t}: t \geqslant 0\right\}$ is a standard
Wiener process. $\mu\left(\bar{x}_{t}, t\right)$ is defined as the drift and $G\left(X_{t}, t\right)$ is the volatility.
If at $t=0, \Sigma_{0}=x_{0}$ a constant the integrated form can be writen as
$\bar{x}_{t}=\bar{x}_{0}+\int_{0}^{t} \mu\left(\bar{x}_{s}, s\right) d s+\int_{0}^{t} \sigma\left(\bar{x}_{s}, s\right) d \omega_{s}$
where

$$
\int_{0}^{t}\left[\left|\mu\left(\boxtimes_{s}, s\right)\right|+\sigma^{2}\left(\bar{X}_{s}, s\right)\right] d s<\infty
$$

A solution of the integral
equation is alled an Ito process or Itō diffusion.

Conside an itegral with respect to a wiener process

$$
I_{t}=\int_{0}^{t} f\left(\omega_{s}, s\right) d \omega_{s}
$$

That is square integrable

$$
E\left[\int_{0}^{t} f\left(\omega_{s}, s\right)^{2} d \omega_{s}\right]<\infty
$$

for all $t \geqslant 0$
Let $t$ be a positive constant and assume $f\left(\omega_{l_{i}}, t_{i}\right)$ is constant over the interval $\left[t_{i}, t_{i+1}\right)$ where

$$
\frac{i t_{i}}{n} \quad 0=t_{0}<t_{1}<t_{2}<\cdots<t \quad n \in \mathbb{N}
$$

Here such a process $f$ is an elementary process. For this process the Ito integral It can be defined

$$
\begin{aligned}
I_{t} & =\int_{0}^{t} f\left(\omega_{s}, s\right) d \omega_{s} \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} f\left(\omega_{t_{i}}, t_{i}\right)\left(\omega_{t i+1}-\omega_{t i}\right)
\end{aligned}
$$

Properties of the Ito integral
can be specified for a standard wiener Process $\left\{\omega_{t}: t \geqslant 0\right\}$ on a Probability space $(\Omega, \mathcal{F}, P)$ and let $f_{t} t \geqslant 0$ be the associale $d$ fituration.
The Ito integral define by

$$
\begin{aligned}
I_{t} & =\int_{0}^{t} f\left(\omega_{s}, s\right) d \omega_{s} \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} f\left(\omega_{t i}, t_{i}\right)\left(\omega_{t i+1} \omega_{t_{i}}\right)
\end{aligned}
$$

where $f$ is a simple process and

$$
t_{i}=\frac{i f}{n} \quad 0=t_{0}<t_{1}<t_{2}<\cdots<t
$$

which has the following properties

1) The paths of $I_{t}$ are continuous.
2) For each $t, I_{t}$ is $F_{t}$ measurable.
3) If $I_{t}=\int_{0}^{t} f\left(\omega_{s}, s\right) d \omega_{s}$ and
$J_{t}=\int_{0}^{t} g\left(\omega_{s}, s\right) d \omega_{s}$ where $f$
and is are simple functions then

$$
I_{t} \pm J_{t}=\int_{0}^{t}\left|f\left(\omega_{s}, s\right) \pm g\left(\omega_{s}, s\right)\right| d \omega_{s}
$$

and for a constant $c$

$$
c I_{t}=\int_{0}^{t} c f\left(\omega_{s}, s\right) d \omega_{s}
$$

(1) It is a marlingale
5) $E\left(I_{t}^{2}\right)=E\left[\int_{0}^{t} f\left(\omega_{s}, s\right)^{2} d \omega_{s}\right]$
6) The quadratic variation

$$
\langle I, I\rangle_{t}=\int_{0}^{t} f\left(\omega_{s}, s\right)^{2} d s
$$

## The one dimensiona Ito formula

let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process on the probability space $(\Omega, F, P)$ and let $F_{t}, t \geqslant 0$ be the associale filtration. Consider a stocnastic process It satisfying

$$
d \bar{X}_{t}=\mu\left(\bar{X}_{t}, t\right) d t+\sigma\left(\bar{I}_{t}, t\right) d \omega_{t}
$$

or in integral form

$$
\underline{x}_{t}=\underline{x}_{0}+\int_{0}^{t} \mu\left(\underline{x}_{s}, s\right) d s+\int_{0}^{t} \sigma\left(z_{s}, s\right) d w_{s}
$$

with $\int_{0}^{t}\left[\left|\mu\left(\bar{x}_{s}, s\right)\right|+\sigma\left(\bar{x}_{s, s}\right)^{2}\right] d s<\infty$
Consider a twice diffenentable function

$$
\bar{I}_{t}=g\left(\bar{X}_{t}, t\right)
$$

Tren expanding in a Taylor series to order $d t$ gives, recalling that $\left(d \omega_{t}\right)^{2}=d t$
$d \bar{Y}_{t}=\frac{\partial g}{\partial t} d t+\frac{\partial g}{\partial X_{t}} d X_{t}+\frac{1}{2} \frac{\partial g^{2}}{\partial X_{t}^{2}}\left(d I_{t}\right)^{2}$
using

$$
d \bar{x}_{t}=\mu d t+\sigma d \omega_{t}
$$

$$
\begin{aligned}
d I_{t}= & \frac{\partial g}{\partial t} d t+\frac{\partial g}{\partial I_{t}}\left(\mu d t+\sigma d \omega_{t}\right) \\
& +\frac{1}{2} \frac{\partial g^{2}}{\partial \underline{x}_{t}^{2}}\left(\mu d t+\sigma d \omega_{t}\right)^{2}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{\partial g}{\partial t} \partial t^{7}+\frac{\partial g}{\partial X_{t}} \mu \overline{d t}+\frac{\partial g}{\partial X_{t}} \sigma d \omega_{t} \\
+ & \frac{1}{2} \frac{\partial^{2} g}{\partial X_{t}^{2}}\left[\mu^{2}(d t)^{2}+2 \mu \sigma d t d \omega_{t}\right. \\
& +\sigma^{2}\left(d\left(\omega_{t}\right)^{2}\right]
\end{aligned}
$$

bet

$$
\begin{gathered}
(d t)^{2}=0 \quad d t d \omega_{t}=0 \\
\left(d \omega_{t}\right)^{2}=d t
\end{gathered}
$$

So

$$
\begin{aligned}
d \bar{y}_{t}= & \left(\frac{\partial g}{\partial t}+\mu \frac{\partial g}{\partial \bar{y}_{t}}+\frac{\partial^{2}}{\partial} \frac{\partial^{2} g_{2}}{\partial \bar{y}_{t}}\right) d t \\
& +\sigma \frac{\partial g}{\partial \mathbb{I}_{t}} d \omega_{t}
\end{aligned}
$$

## Ito Integral

Let $(\Omega, P, \tau)$ be a probability spece and let $\left\{\omega_{t}: \geqslant 0\right\}$ be Ito integral is defined by
$I(t)=\int_{0}^{t} \omega_{s} d \omega_{s}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t_{i}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)$
where

$$
t_{i}=\frac{i t}{n}, \quad 0=t_{0}<t_{1}<t_{2}<\cdots<t
$$

Show that the quadratic variation of $\omega_{t}$ is

$$
\langle\omega, \omega\rangle_{t}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t_{i+1}} \cdot \omega_{t_{i}}\right)^{2}=t
$$

and hence

$$
I(t)=\frac{1}{2}\left(\omega_{t}^{2}-t\right)
$$

and that $I(t)$ is a martingle
In "Quadratic Naviation" it was shown that

$$
\langle\omega, \omega\rangle_{t}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)^{2}=t
$$

Now given that

$$
\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t+i}-\omega_{t i}\right)^{2}=t
$$

for

$$
I(t)=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t_{i}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)
$$

using

$$
\begin{aligned}
& \left(\omega_{t+1}-\omega_{t i}\right)^{2}=\omega_{t i+1}\left(\omega_{t i+1}-\omega_{t i}\right) \\
& -\omega_{t i}\left(\omega_{t i+1}-\omega_{t i}\right) \\
& =\omega_{t i}\left(\omega_{t i+1}-\omega_{t i}\right)=\omega_{t i+1}\left(\omega_{t i+1}-\omega_{t i}\right) \\
& -\left(\omega_{t i+1}-\omega_{t i}\right)^{2} \\
& =\omega_{t i+1}^{2} \cdot \omega_{t i+1} \omega_{t i}-\left(\omega_{t i+1}-\omega_{t i}\right)^{2}
\end{aligned}
$$

Also

$$
\begin{aligned}
& \left(\omega_{-l i+1}-\omega_{t i}\right)^{2}=\omega_{t i+1}^{2}-2 \omega_{t i+1} \omega_{t i} \\
& +\omega_{t i}^{2}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow & \omega_{t i+1} \omega_{t i}=\frac{1}{2}\left[\omega_{t(t)}^{2}+\omega_{t i}^{2}\right. \\
& \left.-\left(\omega_{t i+1}-\omega_{t i}\right)^{2}\right]
\end{aligned}
$$

SG

$$
\begin{aligned}
& \omega_{t i}\left(\omega_{t i+1}-\omega_{t i}\right)=\omega_{t i+1}^{2} \cdot\left(\omega_{t i+1}-\omega_{t i}\right)^{2} \\
& -\omega_{t i+1} \omega_{t i} \\
= & \omega_{t i+1}^{2}-\left(\omega_{t i+1}-\omega_{t i}\right)^{2}-\frac{1}{2}\left[\omega_{t i+1}^{2}+\omega_{t}^{2}\right. \\
& \left.-\left(\omega_{t i+1}-\omega_{t i}\right)^{2}\right] \\
= & \frac{1}{2} \omega_{t i+1}^{2}-\frac{1}{2} \omega_{t i}^{2}-\frac{1}{2}\left(\omega_{t i+1}-\omega_{t i}\right)^{2} \\
= & \frac{1}{2}\left(\omega_{t i+1}^{2}-\omega_{t i}^{2}\right)-\frac{1}{2}\left(\omega_{t i+1}-\omega_{t i}\right)^{2}
\end{aligned}
$$

so

$$
\begin{aligned}
& I(t)=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} w_{t i}\left(w_{t i+1}-w_{t i}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{1}{2}\left(w_{t i+1}^{2}-w_{t i}^{2}\right)-\frac{1}{2}\left(w_{t+1}-w_{t i}\right)^{2} \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{1}{2}\left(w_{t i+1}^{2}-w_{t i}^{2}\right) \\
& -\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{1}{2}\left(w_{t i+1}-w_{t i}\right)^{2}
\end{aligned}
$$

But for the seond term

$$
\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1}\left(\omega_{t i+1}-\omega_{t i}\right)^{2}=t
$$

and for the second term

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t_{i+1}}^{2}-\omega_{t_{i}}^{2} \\
= & \lim _{n \rightarrow \infty}\left[\left(\omega_{t_{1}}^{2}-\omega_{t_{0}}^{2}\right)+\left(\omega_{t_{2}}^{2}-\omega_{t_{1}}^{2}\right)\right. \\
& \left.+\left(\omega_{t_{3}}^{2}-\omega_{t_{2}}^{2}\right)+\cdots+\left(\omega_{t_{n}}^{2}-\omega_{t_{n-1}}^{2}\right)\right] \\
= & \lim _{n \rightarrow \infty} \omega_{t_{n}}^{2}-\omega_{t_{0}}^{2}
\end{aligned}
$$

but by definition of a standard wiener process

$$
\omega_{t_{0}}=\omega_{0}=0
$$

and from

$$
t_{i}=\frac{i t}{n} \quad \rightarrow \quad t_{n}=t
$$

so

$$
\lim _{n \rightarrow \infty} \omega_{t_{n}}^{2} \cdot \omega_{t_{0}}^{2}=\omega_{t}^{2}
$$

SO

$$
\begin{aligned}
I(t) & =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t i}\left(\omega_{t i+1}-\omega_{t i}\right) \\
& =\frac{1}{2}\left(\omega_{t}^{2}-t\right)
\end{aligned}
$$

without goins through first principles Ito's formual can be used with

$$
\begin{aligned}
& \quad \bar{x}_{t}=\frac{1}{2} \omega_{t}^{2}, \quad\left(d \omega_{t}\right)^{2}=d t \\
& d \bar{x}_{t}=\frac{\partial \bar{x}_{t}}{\partial t} d t+\frac{\partial \bar{x}_{t}}{\partial \omega_{t}} d \omega_{t}+\frac{1}{\partial} \frac{\partial^{2} \bar{x}_{t}}{\partial \omega_{t}^{2}}\left(d \omega_{t}\right)^{2} \\
& =\left(\frac{\partial \bar{x}_{t}}{\partial t}+\frac{1}{\partial} \frac{\partial \bar{x}^{2}}{\partial \omega_{t}^{2}}\right) d t+\frac{\partial \bar{x}_{t}}{\partial \omega_{t}} d \omega_{t} \\
& =\frac{1}{2} d t+\omega_{t} d \omega_{t} \\
& \text { Integrating gives } \\
& \quad \int_{0}^{t} d \bar{x}_{s}=\frac{1}{2} \int_{0}^{t} d s+\int_{0}^{t} \omega_{s} d \omega_{s} \\
& \Rightarrow \quad \bar{x}_{t}-\bar{x}_{0}=\frac{1}{2} t+\int_{0}^{t} \omega_{s} d \omega_{s} \\
& \Rightarrow \quad \int_{0}^{t} \omega_{s} d \omega_{s}=\bar{x}_{t}-\bar{x}_{0}-\frac{1}{2} t
\end{aligned}
$$

using

$$
\underline{X}_{t}=\frac{1}{2} \omega_{t}^{2}
$$

and from the defintion of a standard wiener process

$$
\omega_{0}=0 \Rightarrow \bar{X}_{0}=0
$$

the desired result is obtained

$$
I(t)=\int_{0}^{t} \omega_{s} d \omega_{s}=\frac{1}{2}\left(\omega_{t}^{2}-t\right)
$$

Show that $I(t)$ is a martingale.
A maringale in a probabilit y space $\left(x_{1} P, f_{t}\right)$ with fittration ft satisfies

1) $E\left[I(t) \mid \mathcal{F}_{s}\right]=I(s) \quad 0 \leqslant s<t$
2) $E[|I(t)|]<\infty$
3) I(t) is $\mathcal{F}_{t}$ adopted since it is a function $\left\{\omega_{t}: t \geqslant 0\right\}$ which is $f_{t}$ adapted

For property

$$
\begin{aligned}
& E\left[I(t) \mid \mathcal{F}_{s}\right]=E\left[\left.\frac{1}{2}\left(\omega_{t}^{2}-t\right) \right\rvert\, \mathcal{F}_{s}\right] \\
= & E\left[\left.\frac{1}{2}\left[\left(\omega_{t}-\omega_{s}+\omega_{s}\right)^{2}-t\right] \right\rvert\, \mathcal{F}_{s}\right] \\
= & \frac{1}{2} E\left[\left(\omega_{t}-\omega_{s}\right)^{2}+\omega_{s}^{2}+2 \omega_{s}\left(\omega_{t}-\omega_{s}\right) \left\lvert\, \frac{1}{3}\right.\right] \\
& -\frac{1}{2} E\left(t \mid \mathcal{F}_{s}\right) \\
= & \frac{1}{2} E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \left\lvert\, \mathcal{F}_{s}+\frac{1}{2} E\left(\omega_{s}^{2} \mid \mathcal{F}_{s}\right)\right.\right. \\
& =E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \mathcal{F}_{s}\right]-\frac{1}{2} t \\
= & \frac{1}{2}(t-s)+\frac{1}{2} \omega_{s}^{2}+0-\frac{1}{2} t \\
= & \frac{1}{2} \omega_{s}^{2}-\frac{1}{2} s=I(s)
\end{aligned}
$$

For property 2

$$
E[|I(t)|]=\frac{1}{2} E\left(\left|w_{t}^{2}-t\right|\right)
$$

using

$$
\left|\omega_{t}^{2}-t\right| \leq \omega_{t}^{2}+t
$$

gives
$E[|I(t)|] \leq 2 E\left(\omega_{t}^{2}+t\right)=\frac{1}{2}(t+t)=t$

$$
<\infty
$$

## Stratonovich Integral

Let ( $\Omega, P, F$ ) be a probability space and let $\left\{\omega_{t}: t \geqslant 0\right\}$ be a standard wiener process. The Stratonouich Integral is defined by
$s(t)=\int_{0}^{t} \omega_{s} 0 d \omega_{s}=\lim _{n \rightarrow \infty} \sum_{i=0}^{\infty} \frac{1}{2}\left(\omega_{t_{i+1}}+\omega_{t_{i}}\right)\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)$
Where

$$
t_{i}=\frac{i t}{n}, \quad 0=t_{0}<t_{1}<t_{2}<\cdots<t
$$

Show that

$$
S(t)=\frac{1}{2} \omega_{t}^{2}
$$

and that $S(t)$ is not a martingale.
Now
$S(t)=\int_{0}^{t} \omega_{s} \cdot d \omega_{s}=\lim _{n \rightarrow \infty} \sum_{i=0}^{\infty} \frac{1}{2}\left(\omega_{t_{i+1}}+\omega_{t_{i}}\right)\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)$
$=\lim _{n \rightarrow \infty} \sum_{i=c}^{\infty} \frac{1}{2}\left(\omega_{t_{i+1}}^{2}-\omega_{t_{i}}^{2}\right)$

$$
\begin{aligned}
=\lim _{n \rightarrow \infty} \frac{1}{2} & {\left[\left(\varphi_{t_{1}}^{7^{2}}-\omega_{t_{0}}^{2}\right)+\left(\omega_{t_{2}}^{2^{7}}-\varphi_{t_{1}}^{2}\right)\right.} \\
& +\left(\omega_{t_{3}}^{2}-\omega_{t_{2}^{2}}^{2}\right)+\left(\omega_{t_{4}}^{2}-\varphi_{t_{3}^{2}}^{2}\right) \\
& \left.+\cdots+\left(\omega_{t_{n}}^{2}-\omega_{t_{n-1}}^{2}\right)\right] \\
=\lim _{n \rightarrow \infty} \frac{1}{2} & \left(\omega_{t_{n}}^{2}-\omega_{t_{0}}^{2}\right)
\end{aligned}
$$

Using

$$
t_{i}=\frac{i t}{n}=>\quad t_{n}=t
$$

and for a standard Wiener process

$$
\omega_{t_{0}}=0
$$

then

$$
\begin{aligned}
S(t) & =\lim _{n \rightarrow \infty} \frac{1}{2}\left(\omega_{t_{n}}^{2}-\omega_{t_{0}}^{2}\right) \\
& =\lim _{n \rightarrow \infty} \frac{1}{2}\left(\omega_{t}^{2}-0\right) \\
& =\frac{1}{2} \omega_{t}^{2}
\end{aligned}
$$

Recall that a martingale is defined by

1) $E\left[S(t) \mid \mathcal{F}_{s}\right]=S(s) \quad 0 \leqslant s<t$
2) $E(|S(t)|)<\infty$
3) $S(t)$ is It adaped since it is
a function of $\left\{\omega_{t}: t \geqslant 0\right\}$ which is $\mathcal{F}_{t}$ adapted.
For 1

$$
\begin{aligned}
E & {\left[s(t) \mid \mathcal{F}_{s}\right]=E\left(\left.\frac{1}{2} \omega_{t}^{2} \right\rvert\, \mathcal{F}_{s}\right) } \\
= & E\left[\left.\frac{1}{2}\left(\omega_{t}-\omega_{s}+\omega_{s}\right)^{2} \right\rvert\, \mathcal{F}_{s}\right] \\
= & \frac{1}{2} E\left[\left(\omega_{t}-\omega_{s}\right)^{2}+\omega_{s}^{2}+2 \omega_{s}\left(\omega_{t}-\omega_{s}\right)\left(\mathcal{F}_{s}\right]\right. \\
= & \frac{1}{2} E\left[\left(\omega_{t}-\omega_{s}\right)^{2} \mid \mathcal{F}_{s}\right]+\frac{1}{2} E\left(\omega_{s}^{2} \mid \mathcal{F}_{s}\right) \\
& +E\left[\omega_{s}\left(\omega_{t}-\omega_{s}\right) \mid \mathcal{F}_{s}\right] \\
= & \frac{1}{2} E\left[\left(\omega_{t}-\omega_{s}\right)^{2}\right]+\frac{1}{2} \omega_{s}^{2}+\frac{1}{2} \omega_{s} E\left[\left(\omega_{t}-\omega_{s}\right)\right] \\
= & \frac{1}{2}(t-s)+\frac{1}{2} \omega_{s}^{2}+0 \\
= & \frac{1}{2}\left(\omega_{s}^{2}+t-s\right) \neq s(s)
\end{aligned}
$$

Thus $S(t)$ is not a martingale.

## Yet Another Stochastic Integral

Let $\left(\Omega, P, \mathcal{F}_{s}\right)$ be a probability space and let $\left\{\omega_{4}: t \geqslant 0\right\}$ be a standard wiener process. Define the integral of

$$
\omega_{t} * d \omega_{t}
$$

by

$$
J(t)=\int_{0}^{t} \omega_{t} * d \omega_{t}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t_{i+1}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)
$$

where

$$
t_{i}=\frac{i t}{n}, \quad 0=t_{0}<t_{1}<t_{2}<\cdots<t
$$

show that

$$
J(t)=\frac{1}{2}\left(\omega_{t}^{2}+t\right)
$$

and that $J(t)$ is not a martingale.
Now
$J(t)=\int_{0}^{t} \omega_{t} * d \omega_{i}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t_{i+1}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)$

Now

$$
\begin{aligned}
& \left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)^{2}=\omega_{t_{i+1}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right) \\
& +\omega_{t_{i}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right) \\
& \Rightarrow \omega_{t_{i+1}}\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)=\left(\omega_{t_{i+1}}-\omega_{t_{i}}\right)^{2} \\
& -\omega_{t_{i}} \omega_{t_{i+1}}+\omega_{t_{i}}^{2}
\end{aligned}
$$

and

$$
\begin{aligned}
& \left(\omega_{t i+1}-\omega_{t i}\right)^{2}=\omega_{t i+1}^{2}-2 \omega_{t_{i}} \omega_{t i+1}+\omega_{t e}^{2} \\
& \Rightarrow \omega_{t_{i}} \omega_{t(t)}=\frac{1}{2}\left[\omega_{t i+1}^{2}+\omega_{t i}^{2}-\left(\omega_{t i+1}-\omega_{t i}\right)^{2}\right] \\
& \delta 0 \\
& \omega_{t i+1}\left(\omega_{t i+1}-\omega_{t i}\right)=\left(\omega_{t i+1}-\omega_{t i}\right)^{2} \\
& +\omega_{t i}^{2}-\frac{1}{2}\left[\omega_{t i+1}^{2}+\omega_{t i}^{2}-\left(\omega_{t i+1}-\omega_{t i}^{2}\right)^{2}\right] \\
& =\frac{1}{2}\left(\omega_{t i+1}-\omega_{t i}\right)^{2}+\frac{1}{2}\left(\omega_{t i+1}^{2}-\omega_{t_{i}}^{2}\right) \\
& \text { thas } \\
& J(t)=\int_{0}^{t} \omega_{t}^{2} d \omega_{t}=\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \omega_{t i+1}\left(\omega_{t i+1}-\omega_{t i}\right) \\
& =\lim _{n \rightarrow \infty} \sum_{i=0}^{n-1} \frac{1}{2}\left(\omega_{t i+1}-\omega_{t i}\right)^{2}+\frac{1}{2}\left(\omega_{t i+1}^{2}-\omega_{t i}^{2}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & \lim _{n \rightarrow \infty}\left[\sum_{i=0}^{n-1} \frac{1}{2}\left(w_{t_{i+1}}-w_{t_{i}}\right)^{2}+\sum_{i=0}^{n-1} \frac{1}{2}\left(w_{t_{i+1}}^{2} \cdot w_{t_{i}}^{2}\right)\right] \\
= & \lim _{n \rightarrow \infty} \frac{1}{2} \sum_{i=0}^{n-1}\left(w_{t i+1}-w_{t_{i}}\right)^{2}+\lim _{n \rightarrow \infty} \frac{1}{2} \sum_{i=0}^{n-1}\left(w_{t_{i+1}}^{2} \cdot w_{t_{i}}^{2}\right) \\
= & \frac{1}{2} t^{2}+\lim _{n \rightarrow \infty} \frac{1}{2}\left[\left(w_{t_{1}}^{2}-w_{t_{0}}^{2}\right)+\left(w_{t_{2}}^{2}-\left(x_{t_{1}}^{2}\right)\right.\right. \\
& \left.+\left(w_{t_{3}}^{2}-w_{t_{2}}^{2}\right)+\cdots+\left(w_{t_{n}}^{2}-w_{t_{n-1}}^{2}\right)\right] \\
= & \frac{1}{2} t^{2}+\lim _{n \rightarrow \infty} \frac{1}{2}\left(w_{t_{n}}^{2}-w_{t_{0}}^{2}\right)
\end{aligned}
$$

But for a standard wiene process

$$
w_{t_{0}}=0
$$

and

$$
t_{i}=\frac{i t}{n} \Rightarrow \quad t_{n}=t
$$

tnces

$$
J(t)=\frac{1}{2}\left(\omega_{t}^{2}+t^{2}\right)
$$

A martingale has the properties

