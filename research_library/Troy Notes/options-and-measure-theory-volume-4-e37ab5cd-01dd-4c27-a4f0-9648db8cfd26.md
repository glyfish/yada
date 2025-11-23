## Metric Spaces

A metric on $a$ set $M$ is a mapping

$$
d(x, y): M \times M \rightarrow \mathbb{R}
$$

where $(x, y) \in M \times M$ that satisfies

1. $\quad d(x, y)=d(y, x)$
2. $d(x, y) \geqslant 0$
3. $d(x, y)=0$ if and onk, if $x=y$
4. $d(x, y) \leq d(x, z)+d(z, y)$

If $d$ is a metric on the set $\mu$ then the pair $(M, d)$ defines a metric space.

Now for sets $A, B \subset \bar{X}$ the distance from $A$ to $B$ by

$$
d(A, B)=\mu^{*}[S(A, B)]
$$

where $S(A, B)$ is the symetric

## difference

$$
S(A, B)=(A-B) \cup(B-A)
$$

As an example consider the two unit squares
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-002.jpg?height=809&width=997&top_left_y=687&top_left_x=338)

This set consists of the multi-intervals

$$
\begin{aligned}
A-B= & {[0,12) \times[0,1 / 2) \cup[1 / 2,1] \times[0,1 / 2] \cup } \\
& {[1 / 2,1] \times[0,1 / 2] }
\end{aligned}
$$

$$
\begin{aligned}
B-A= & {[1 / 2,1] \times[1,3 / 2] \cup(1,3 / 2] \times\left[\frac{1}{2}, 1\right] \cup } \\
& (1,3 / 2] \times(1,3 / 2]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& d(A, B)=\mu^{*}[(A-B) \cup(B-A)] \\
= & \mu([0, b) \times[0,1 / 2) \cup[1 / 21] \times[0,1 a] \cup \\
& \quad[1 / 2,1] \times[0,1 b] \cup[1 / 2,1] \times[1,3 / 2] \cup \\
& \quad(1,3 / 2] \times[1 a, 1] \cup(1,3 / 2] \times(1,3 / 2]) \\
= & \mu([0,1) \times[0,1 / 2))+\mu([1 / 2,1] \times[0,1 / 2]) \\
+ & \mu([1 / 2,1] \times[0,1 b])+\mu([1 / 2,1] \times[1,3 / 2]) \\
+ & \mu\left((1,3 / 2] \times\left[\frac{1}{2}, 1\right]\right)+\mu((1,3 / 2] \times(1,3 / 2]) \\
= & \quad(1 / 2)(1 / 2)+(1 / 2)(1 b)+(1 / 2)(1 / 2)+(1 b)(1 / 2) \\
& +(1 / 2)(1 / 2)+(1 / 2)(1 a) \\
= & \frac{6}{4}=\frac{3}{2}
\end{aligned}
$$

$d(A, B)$ may equal $+\infty$
In contrast to the definition of a metric space $d(A, B)=0$ does not necessarily imply trat $A=B$.

Proposition: $d(A, B)=d(B, A)$
Proof

$$
\begin{aligned}
d(A, B) & =S(A, B) \\
& =(A-B) \cup(B-A) \\
& =(B-A) \cup(A-B) \\
& =d(B, A)
\end{aligned}
$$

Proposition: $d(A, A)=0$
Proof:

$$
\begin{aligned}
d(A, A) & =(A-A) \cup(A-A) \\
& =\varnothing
\end{aligned}
$$

## Proposition: $d(A, B)+d(B, C) \geqslant d(A, C)$

Proof:

$$
\begin{gathered}
d(A, B)+d(B, C) \geqslant d(A, C) \\
\Rightarrow \quad S(A, B) \cup S(B, C) \subseteq S(A, C)
\end{gathered}
$$

Now,

$$
\begin{aligned}
& S(A, B)=(A-B) \cup(B-A) \\
& S(B, C)=(B-C) \cup(C-B)
\end{aligned}
$$

50

$$
\begin{aligned}
& S(A, B) \cup S(B, C) \\
& =(A-B) \cup(B-A) \cup(B-C) \cup(C-B) \\
& =[(A-B) \cup(B-C)] \cup[(B-A) \cup(C-B)]
\end{aligned}
$$

Now

$$
S(A, C)=(A-C) \cup(C-A)
$$

Consider

$$
A-C \text { and }(A-B) \cup(B-C)
$$

assume that $x \in A-C \Rightarrow x \in A$ and $x \notin C$. Assume that $x \in B$. Then

$$
x \notin A-B, x \in B-C
$$

so $x \in(A-B) \cup(B-C)$.
Similarly if $x \notin B$ then

$$
x \in A-B, \quad x \notin B-C
$$

so $x \in(A-B) \cup(B-C)$ thus

$$
A-C \subseteq(A-B) \cup(B-C)
$$

Similarly consider

$$
C-A \text { and }(B-A) \cup(C-B)
$$

Assume that $x \in C-A$ then
$x \in C$ and $x \notin A$. Furthur assume that $x \in B$ then

$$
x \in B-A \text { and } x \notin C-B
$$

Next assume that $x \notin B$ then

$$
x \notin B-A \text { and } x \in C-B
$$

thus

$$
C-A \subseteq(B-A) \cup(C-B)
$$

Now bringing things together

$$
\begin{aligned}
& S(A, B) \cup S(B, C) \\
& =[(A-B) \cup(B-C)] \cup[(B-A) \cup(C-B)] \\
& S(A, C)=(A-C) \cup(C-A) \\
& A-C \subseteq(A-B) \cup(B-C) \\
& C-A \subseteq(B-A) \cup(C-B)
\end{aligned}
$$

To complete the proof a final result is required.
$A \subseteq C$ and $B \subseteq D \Rightarrow A \cup B \subseteq C \cup D$ clearly if

$$
\begin{aligned}
& x \in A \Rightarrow x \in C \Rightarrow x \in C \cup D \\
& x \in B \Rightarrow x \in D \Rightarrow x \in C \cup D
\end{aligned}
$$

Thus

$$
A \cup B \subseteq C \cup D
$$

it follows that

$$
\begin{aligned}
& A-C \subseteq(A-B) \cup(B-C) \\
& C-A \subseteq(B-A) \cup(C-B)
\end{aligned}
$$

and using the previous result gives

$$
\begin{aligned}
& S(A, B) \cup S(B, C) \\
& =[(A-B) \cup(B-C)] \cup[(B-A) \cup(C-B)] \\
& S(A, C)=(A-C) \cup(C-A) \\
& \Rightarrow S(A, C) \subseteq S(A, B) \cup S(B, C)
\end{aligned}
$$

From the definition of measure it follows that

$$
\Rightarrow d(A, C) \leq d(A, B)+d(B, C)
$$

Now it needs to be noted that

$$
\begin{aligned}
& d(A, B)=0 \Rightarrow \mu^{*}[S(A, B)]=0 \\
& \Rightarrow \mu^{*}[(A-B) \cup(B-A)]=0 \\
& =\mu^{*}(A-B)+\mu^{*}(B-A) \\
& \Rightarrow \mu^{*}(A-B)=0 \text { and } \mu^{*}(B-A)=0
\end{aligned}
$$

since $\mu^{*}(A) \geqslant 0$. Thus $d(A, B)=0$ If the symetric difference of $A$ and $B$ is a set of measure zero.

Taking this into consideration the distance function can be used to define the notion of convergence in $2^{x}$. That is a sequence

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \in 2^{\bar{x}}
$$

converges to $A \in Q^{\bar{X}}$, written as $A_{i} \rightarrow A$, if $d\left(A_{i}, A\right) \rightarrow 0$ The set operations in $2^{\text {I }}$ are continous with respect to the distance function $d$. That is if

$$
A_{n} \rightarrow A \text { and } B_{n} \rightarrow B
$$

then

$$
\begin{gathered}
A_{n} \cup B_{n} \rightarrow A \cup B \\
A_{n} \cap B_{n} \rightarrow A \cap B \\
A_{n}-B_{n} \rightarrow A-B \\
A_{n}^{C} \rightarrow A^{C}
\end{gathered}
$$

Theorems: If $A_{1}, A_{2}, B_{1}$ and $B_{2} \in 2^{x}$

1. $S\left(A_{1}^{C}, B_{1}^{C}\right)=S\left(A_{1}, B_{1}\right)$
2. $\delta\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \subseteq \delta\left(A_{1}, B_{1}\right) \cup \delta\left(A_{2}, B_{2}\right)$
3. $S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$
4. $S\left(A_{1}-A_{2}, B_{1}-B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$

Proof: $S\left(A_{1}^{C}, B_{1}^{C}\right)=S\left(A_{1}, B_{1}\right)$
The following identities are required for the proof

$$
A-B=A \cap B^{C}
$$

Let $x \in A-B \Rightarrow x \in A=X \notin B$
$\Rightarrow x \in B^{C} \Rightarrow x \in A \cap B^{C}$
so

$$
A-B C A \cap B^{C}
$$

similarly $x \in A \cap B^{C} \Rightarrow x \in A$ and $x \in B^{c} \Rightarrow x \notin B \Rightarrow x \in A-B$ thus

$$
A-B=A \cap B^{C}
$$

Next consider

$$
A^{C}-B^{C}=A^{C} \cap B
$$

Let $x \in A^{c}-B^{c} \Rightarrow x \in A^{c}$ and $x \notin B^{c} \Rightarrow x \in B \Rightarrow x \in A^{c} \cap B$ thus

$$
A^{C}-B^{C} \subseteq A^{C} \cap B
$$

Similarly let $x \in A^{C} \cap B \Rightarrow x \in A^{C}$ and $x \in B \Rightarrow x \notin B^{c} \Rightarrow x \in A^{c}-B^{c}$ thus

$$
A^{C}-B^{C}=A^{C} \cap B
$$

Now

$$
\begin{aligned}
S\left(A_{1}^{C}, B_{1}^{C}\right) & =\left(A_{1}^{C}-B_{1}^{C}\right) \cup\left(B_{1}^{C}-A_{1}^{C}\right) \\
& =\left(A_{1}^{C} \cap B_{1}\right) \cup\left(B_{1}^{C} \cap A_{1}\right)
\end{aligned}
$$

and

$$
\begin{aligned}
S\left(A_{1}, B_{1}\right) & =\left(A_{1}-B_{1}\right) \cup\left(B_{1}-A_{1}\right) \\
& =\left(A_{1} \cap B_{1}^{C}\right) \cup\left(B_{1} \cap A_{i}^{C}\right) \\
& =\left(A_{i}^{C} \cap B_{1}\right) \cup\left(B_{1}^{C} \cap A_{i}\right) \\
& =S\left(A_{i}^{C}, B_{i}^{C}\right)
\end{aligned}
$$

Thus

$$
S\left(A_{1}, B_{1}\right)=S\left(A_{1}^{C}, B_{1}^{C}\right)
$$

Proof: $S\left(A, \cup A_{2}, B, \cup B_{2}\right) \subseteq$

$$
\begin{gathered}
S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right) \\
S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right)=\left[\left(A_{1} \cup A_{2}\right)-\left(B_{1} \cup B_{2}\right)\right] \\
\cup\left[\left(B_{1} \cup B_{2}\right)-\left(A_{1} \cup A_{2}\right)\right]
\end{gathered}
$$

using the following identity gives

$$
A-B=A \cap B^{C}
$$

$$
\begin{aligned}
S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right)=\left[\left(A_{1} \cup A_{2}\right)-\left(B_{1} \cup B_{2}\right)\right] & \\
\cup & {\left[\left(B_{1} \cup B_{2}\right)-\left(A_{1} \cup A_{2}\right)\right] } \\
= & {\left[\left(A_{1} \cup A_{2}\right) \cap\left(B_{1} \cup B_{2}\right)^{C}\right] \cup } \\
& {\left[\left(B_{1} \cup B_{2}\right) \cap\left(A_{1} \cup A_{2}\right)^{C}\right] }
\end{aligned}
$$

Next consider the terms of the form

$$
(A \cup B)^{C}=A^{C} \cap B^{C}
$$

To prove this assume $x \in(A \cup B)^{c}$

$$
\begin{aligned}
& \Rightarrow x \notin A \cup B \Rightarrow x \notin A \text { and } x \notin B \\
& \Rightarrow x \in A^{c} \text { and } x \in B^{c} \\
& \Rightarrow x \in A^{c} \cup B^{c}
\end{aligned}
$$

Next assume $x \in A^{c} \cap B^{c}$

$$
\begin{aligned}
& \Rightarrow x \in A^{c} \text { and } x \in B C \\
& \Rightarrow x \notin A \text { and } x \notin B \\
& \Rightarrow x \notin A \cup B \Rightarrow x \in(A \cup B)^{c}
\end{aligned}
$$

Thus

$$
(A \cup B)^{C}=A^{C} \cap B^{C}
$$

Applying this relation gives

$$
\begin{aligned}
S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right)=\left[\left(A_{1} \cup A_{2}\right)-\left(B_{1} \cup B_{2}\right)\right] & \\
\cup\left[\left(B_{1} \cup B_{2}\right)-\left(A_{1} \cup A_{2}\right)\right] & \\
= & {\left[\left(A_{1} \cup A_{2}\right) \cap\left(B_{1} \cup B_{2}\right)^{C}\right] \cup } \\
& {\left[\left(B_{1} \cup B_{2}\right) \cap\left(A_{1} \cup A_{2}\right)^{C}\right] } \\
= & {\left[\left(A_{1} \cup A_{2}\right) \cap\left(B_{1}^{C} \cap B_{2}^{C}\right)\right] \cup } \\
& {\left[\left(B_{1} \cup B_{2}\right) \cap\left(A_{1} \subset \wedge A_{2}^{C}\right)\right] }
\end{aligned}
$$

To complete this one final relationship is required.

$$
\begin{aligned}
& \left(A_{1} \cup A_{2}\right) \cap\left(B_{1}^{c} \cap B_{2}^{c}\right) \\
& \quad \leq\left(A_{1} \cap B_{1}^{c}\right) \cup\left(A_{2} \cap B_{2}^{c}\right)
\end{aligned}
$$

assume $x \in\left(A_{1} \cup A_{2}\right) \cap\left(B_{1}^{c} \cap B_{2}^{c}\right)$

$$
\begin{aligned}
\Rightarrow & x \in A_{1} \cup A_{2} \text { and } x \in B_{1}^{c} \cap B_{2}^{c} \\
\Rightarrow & x \in A_{1} \text { or } x \in A_{2} \text { and } x \in B_{1}^{c} \\
& \text { and } x \in B_{2}^{c}
\end{aligned}
$$

If $x \in A$, or $x \in A_{2}$ then

$$
x \in A_{1} \cap B_{1}^{C} \text { or } x \in A_{2} \cap B_{2}^{C}
$$

It follows that

$$
x \in\left(A_{1} \cap B_{1}^{c}\right) \cup\left(A_{2} \cap B_{2}^{c}\right)
$$

Equality does not hod since an corbitrary $x$ choosen from $\left(A_{1} \cap B_{1}^{c}\right) \cup\left(A_{2} \cap B_{2}^{c}\right)$ is not neccessarily in $B_{1} C$ and $B_{2} C$. It follows that

$$
\begin{aligned}
& S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \subseteq \\
& {\left[\left(A_{1} \cap B_{1}^{c}\right) \cup\left(A_{2} \cap B_{2}^{c}\right)\right] \cup} \\
& {\left[\left(B_{1} \cap A_{1}^{c}\right) \cup\left(B_{2} \cap A_{2}^{c}\right)\right]}
\end{aligned}
$$

The final result is obtained by using

$$
\begin{aligned}
& A_{1} \cap B_{1}^{C}=A_{1}-B_{1} \\
& A_{2} \cap B_{2}^{C}=A_{2}-B_{2} \\
& B_{1} \cap A_{1}^{C}=B_{1}-A_{1} \\
& B_{2} \cap A_{2}^{C}=B_{2}-A_{2}
\end{aligned}
$$

Pulling things together gives

$$
\begin{aligned}
S & \left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \subseteq \\
& \left(A_{1}-B_{1}\right) \cup\left(A_{2}-B_{2}\right) \cup\left(B_{1}-A_{1}\right) \cup\left(B_{2}-A_{2}\right) \\
= & \left(A_{1}-B_{1}\right) \cup\left(B_{1}-A_{1}\right) \cup\left(A_{2}-B_{2}\right) \cup\left(B_{2}-A_{2}\right) \\
= & S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
\end{aligned}
$$

which is the final result

Proof: $\quad S\left(A_{1} \cap A_{2}, B \cap \cap B_{2}\right) \subseteq$

$$
S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
$$

NOW

$$
\begin{aligned}
S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) & \\
= & {\left[\left(A_{1} \cap A_{2}\right)-\left(B_{1} \cap B_{2}\right)\right] \cup } \\
& {\left[\left(B_{1} \cap B_{2}\right)-\left(A_{1} \cap A_{2}\right)\right] }
\end{aligned}
$$

Consider

$$
\begin{aligned}
S\left(A_{1}^{c} \cup A_{2}^{c}, B_{1}^{c} \cup B_{2}^{c}\right) & \\
= & {\left[\left(A_{1}^{c} \cup A_{2}^{c}\right)-\left(B_{1}^{c} \cup B_{2}^{c}\right)\right] \cup } \\
& {\left[\left(B_{1}^{c} \cup B_{2}^{c}\right)-\left(A \subseteq \cup A_{2}^{c}\right)\right] }
\end{aligned}
$$

Assume that

$$
\begin{aligned}
x \in & {\left[\left(A_{1} \cap A_{2}\right)-\left(B_{1} \cap B_{2}\right)\right] \cup } \\
& {\left[\left(B_{1} \cap B_{2}\right)-\left(A_{1} \cap A_{2}\right)\right] }
\end{aligned}
$$

Then

$$
x \in\left(A_{1} \cap A_{2}\right) \text { and } x \notin\left(B_{1} \cap B_{2}\right)
$$

or
$x \in\left(B_{1} \cap B_{2}\right)$ and $x \notin\left(A_{1} \cap A_{2}\right)$

If first relation is true then

$$
\begin{aligned}
& x \in\left(A_{1} \cap A_{2}\right) \Rightarrow x \in A_{1} \text { and } x \in A_{2} \\
& x \notin\left(B_{1} \cap B_{2}\right) \Rightarrow x \notin B_{1} \text { and } x \notin B_{2}
\end{aligned}
$$

It follows that

$$
x \notin A_{1}^{C} \cup A_{2}^{C} \quad x \in B_{1}^{C} \cup C^{C}
$$

50

$$
x \in\left[\left(B_{1}^{C} \cup B_{2}^{C}\right)-\left(A_{1}^{C} \cup A_{2}^{C}\right)\right]
$$

SO

$$
x \in S\left(A_{1}^{c} \cup A_{2}^{c}, B_{1}^{c} \cup B_{2}^{c}\right)
$$

If instead $x \in\left[\left(B_{1} \cap B_{2}\right)-\left(A_{1} \cap A_{2}\right]\right.$ then

$$
\begin{aligned}
& x \in B_{1} \cap B_{2} \quad x \notin A_{1} \cap A_{2} \\
\Rightarrow & x \in B_{1}, x \in B_{2} \quad x \notin A_{1}, x \notin A_{2} \\
\Rightarrow & x \notin B_{1}^{c}, x \notin B_{2}^{c} \quad x \in A_{1}^{c}, x \in A_{2}^{c}
\end{aligned}
$$

Thus

$$
x \in\left[\left(A_{1}^{c} \cup A_{2}^{c}\right)-\left(B_{1}^{c} \cup B_{2}^{c}\right)\right]
$$

and

$$
x \in S\left(A_{1}^{C} \cup A_{2}^{C}, B_{1}^{C} \cup B_{2}^{C}\right)
$$

smilarly if

$$
\begin{aligned}
x \in & {\left[\left(A_{1}^{C} \cup A_{2}^{C}\right)-\left(B_{1}^{C} \cup B^{C}\right)\right] U } \\
& {\left[\left(B_{1}^{C} \cup B_{2}^{C}\right)-\left(A C \cup A_{2}^{C}\right)\right] }
\end{aligned}
$$

Then eitner

$$
x \in A_{1}^{C} \cup A_{2}^{C} \text { and } x \notin B_{1}^{C} \cup B_{2}^{C}
$$

or

$$
x \in B_{1}^{C} \cup B_{2}^{C} \text { and } x \notin A_{1}^{C} \cup A_{2}^{C}
$$

If first relation is true then

$$
\begin{aligned}
& x \notin B_{1}^{c} \text { and } x \in B_{2}^{c} \\
& \Rightarrow x \in B_{1} \text { and } x \in B_{2} \\
& \Rightarrow x \in B_{1} \wedge B_{2} \\
& x \in A_{1}^{c} \text { and/or } x \in A_{2}^{c} \\
& \Rightarrow x \notin A_{1} \text { and/or } x \notin A_{2}
\end{aligned}
$$

$$
\Rightarrow \quad x \in A_{1} \cap A_{2}
$$

Thus

$$
x \in\left[\left(B_{1} \cap B_{2}\right)-\left(A_{1} \cap A_{2}\right)\right]
$$

and

$$
x \in S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right)
$$

similarly if the second option is choosen

$$
x \in B_{1}^{C} \cup B_{2}^{C} \text { and } x \notin A_{1}^{C} \cup A_{2}^{C}
$$

It will follow that

$$
x \in\left[\left(A_{1} \cap A_{2}\right)-\left(B_{1} \cap B_{2}\right)\right]
$$

Thus

$$
\begin{aligned}
S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) & = \\
& S\left(A_{1}^{c} \cup A_{2}^{c}, B_{1}^{c} \cup B_{2}^{c}\right)
\end{aligned}
$$

Now previously it was shown that

$$
S\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
$$

Using this result gives

$$
\begin{aligned}
& S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right)= \\
& S\left(A_{1}^{c} \cup A_{2}^{c}, B_{1}^{c} \cup B_{2}^{c}\right) \\
& \subseteq S\left(A_{1}^{c}, B_{1}^{c}\right) \cup S\left(A_{2}^{c}, B_{2}^{c}\right)
\end{aligned}
$$

Also, previously it was shown that

$$
S\left(A^{C}, B^{C}\right)=S(A, B)
$$

thus the final result is obtained
$S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$
Proof: $S\left(A_{1}-A_{2}, B_{1}-B_{2}\right) \subseteq$

$$
S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
$$

Recall that

$$
A-B=A \cap B^{C}
$$

so
$S\left(A_{1}-A_{2}, B_{1}-B_{2}\right)=S\left(A_{1} \cap A_{2}^{C}, B_{1} \cap B_{2}^{C}\right)$
Also, recall that

$$
\begin{aligned}
S\left(A_{1} \cap A_{2},\right. & \left.B_{1} \cap B_{2}\right) \subseteq \\
& S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
\end{aligned}
$$

so

$$
\begin{gathered}
S\left(A_{1}-A_{2}, B_{1}-B_{2}\right)=S\left(A_{1} \cap A_{2}^{C}, B_{1} \cap B_{2}^{C}\right) \\
\subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}^{C}, B_{2}^{C}\right) \\
=S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)
\end{gathered}
$$

where use was made of

$$
S\left(A_{2}^{C}, B_{2}^{C}\right)=S\left(A_{2}, B_{2}\right)
$$

Thus the following relations have been proven.

If $A_{1}, A_{2}, B_{1}$ and $B_{2} \in 2^{x}$

1. $S\left(A_{1}^{C}, B_{1}^{C}\right)=S\left(A_{1}, B_{1}\right)$
2. $\delta\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \subseteq \delta\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$
3. $S\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$
4. $S\left(A_{1}-A_{2}, B_{1}-B_{2}\right) \subseteq S\left(A_{1}, B_{1}\right) \cup S\left(A_{2}, B_{2}\right)$

Now since

$$
d(A, B)=\mu^{*}[S(A, B)]
$$

From the previous result it follows that

1. $d\left(A^{C}, B^{C}\right)=d(A, B)$
2. $d\left(A_{1} \cup A_{2}, B_{1} \cup B_{2}\right) \leq d\left(A_{1}, B_{1}\right)+d\left(A_{2}, B_{2}\right)$
3. $d\left(A_{1} \cap A_{2}, B_{1} \cap B_{2}\right) \leq d\left(A_{1}, B_{1}\right)+d\left(A_{2}, B_{2}\right)$
4. $d\left(A_{1}-A_{2}, B_{1}-B_{2}\right) \leq d\left(A_{1}, B_{1}\right)+d\left(A_{2}, B_{2}\right)$

Theorom: $\mu^{*}$ is continous in the in the following sense: Let $A, B \in 2^{8}$ and suppose cither $\mu^{*}(A)$ and $\mu^{*}(B)$ is finite, then

$$
\left|\mu^{*}(A)-\mu^{*}(B)\right| \leqslant d(A, B)
$$

Proof: Suppose $\mu^{*}(B)<\infty$ and assume $\mu^{*}(B) \leqslant \mu^{*}(A)$.
Recall the provous theorem

$$
d\left(A_{1}-A_{2}, B_{1}-B_{2}\right) \leq d\left(A_{1}, B_{1}\right)+d\left(A_{2}, B_{2}\right)
$$

Let $A_{1}=A, A_{2}=\phi, B_{1}=B_{2}=B$ then

$$
d(A, \phi) \leqslant d(A, B)+d(\phi, B)
$$

but

$$
\begin{gathered}
d(\varnothing, B)=d(B, \varnothing) \\
\Rightarrow d(A, \phi) \leqslant d(A, B)+d(B, \phi)
\end{gathered}
$$

Now from the definition of the distance function, $d$,

$$
d(A, B)=\mu^{*}[s(A, B)]
$$

it follows that

$$
\begin{aligned}
d(A, \varnothing) & =\mu^{*}[S(A, \varnothing)] \\
& =\mu^{*}[(A-\varnothing) U(\varnothing-A)]
\end{aligned}
$$

$$
=\mu^{*}(A)
$$

similarly

$$
d(B, \varnothing)=\mu^{*}(B)
$$

Thus the desired result is dotained

$$
\begin{array}{ll} 
& \mu^{*}(A) \leqslant d(A, B)+\mu^{*}(B) \\
\Rightarrow & \mu^{*}(A)-\mu^{*}(B) \leqslant d(A, B)
\end{array}
$$

since $\mu^{*}(B) \leqslant \mu^{*}(A)$ it follows trat

$$
\left|\mu^{*}(A)-\mu^{*}(B)\right| \leq d(A, B)
$$

Definition : Let $m_{F}$ be a closure of $R$ in $2^{X}$. That is $A \in M_{F}$ if and only if there exists a sequence of points $\left\{A_{i}\right\}_{i=1}^{\infty} \subset R$ such that $d\left(A_{i}, A\right) \rightarrow 0$ as $i \rightarrow \infty$

## Theorem

1. $m_{F}$ is a ring
2. For $A \in O_{F}, \mu^{*}(A)<\infty$ 3. $\mu^{*}$ is a measure on $n_{F}$

Proof 1: $m_{F}$ is a ring. Assume $A, B \in M_{F}$. It needs to be shown that $A \cup B$ and $A-B$ are in $m_{F}$.

Now since $A, B \in M_{F}$ there are sequences

$$
\left\{A_{c}\right\}_{i=1}^{\infty} \subset Q \quad\left\{B_{i}\right\}_{i=1}^{\infty} \subset R
$$

such that

$$
A_{i} \rightarrow A \quad B_{i} \rightarrow B
$$

Since $Q$ is a ring

$$
\begin{aligned}
& \left\{A_{i} \cup B_{i}\right\}_{i=1}^{\infty} \subset R \\
& \left\{A_{i}-B_{i}\right\}_{i=1}^{\infty} \subset R
\end{aligned}
$$

Since the Bookan set operations are continuous it follows that

$$
\begin{aligned}
& A_{i} \cup B_{i} \rightarrow A \cup B \\
& A_{i}-B_{i} \rightarrow A-B
\end{aligned}
$$

Thus

$$
\begin{aligned}
& A \cup B \in M_{F} \\
& A-T \in M_{F}
\end{aligned}
$$

so $m_{F}$ is a ring.
Proof 2: For $A \in M_{F}, \mu^{*}(A)<\infty$.
since $A \in M_{F}$ there is $a$ sequence

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \subset R
$$

with $A_{i} \rightarrow A$. From the definition of convergence it follows that for some $n$

$$
\begin{array}{ll} 
& d\left(A_{n}, A\right)<1 \\
\Rightarrow & \mu^{*}(A)-\mu^{*}\left(A_{n}\right)<1 \\
\Rightarrow & \mu^{*}(A)<\mu^{*}\left(A_{n}\right)+1
\end{array}
$$

Since $A_{n}$ is finite by the assumption $\mu^{*}$ continuity it follows that

$$
\mu^{*}(A)<\infty
$$

Proof 3: $\mu^{*}$ is a measure on $m_{F}$
To show the $\mu^{*}$ is a measure it must be shown that it is contably additive,

$$
\mu^{*}(A)=\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

nonegative set function on $m_{F}$ where $A \in M_{F}$.
First it will be shown that $\mu^{*}$ is additive by proving the lattice property, namely,

$$
\mu^{*}(A \cup B)+\mu^{*}(A \cap B)=\mu^{*}(A)+\mu^{*}(B)
$$

Consider the sequences

$$
\left\{A_{n}\right\}_{n=1}^{\infty},\left\{B_{n}\right\}_{n=1}^{\infty} \subseteq R
$$

where $A_{n} \rightarrow A$ and $B_{n} \rightarrow B$. Recall that on $Q \mu^{*}=\mu, \mu^{*}$ is $Q$ measure and additive on $Q$ so

$$
\begin{gathered}
\mu^{*}\left(A_{n} \cup B_{n}\right)+\mu^{*}\left(A_{n} \cap B_{n}\right)=\mu^{*}\left(A_{n}\right) \\
+\mu^{*}\left(B_{n}\right)
\end{gathered}
$$

Now

$$
\begin{aligned}
& A_{n} \cup B_{n} \rightarrow A \cup B \\
& A_{n} \cap B_{n} \rightarrow A \cap B
\end{aligned}
$$

so continuity of $\mu^{*}$ implies

$$
\mu^{*}(A \cup B)+\mu^{*}(A \cap B)=\mu^{*}(A)+\mu^{*}(B)
$$

Thus $\mu^{*}$ is countably additive for $A, B \in M_{F}$

To prove countable additivity let

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \subset M_{F}
$$

where $A_{i} \cap A_{j}=\varnothing$ for $i \neq j$. Also, assume

$$
A=\bigcup_{i=1}^{\infty} A_{i} \in M_{F}
$$

since $A_{i}$ are mutually disjoint the lattice property becomes for $i \neq j$

$$
\mu^{*}\left(A_{i} \cup A_{j}\right)=\mu^{*}\left(A_{i}\right)+\mu^{*}\left(A_{j}\right)
$$

Now, from subadditity of $\mu^{*}$

$$
\mu^{*}(A) \leq \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

For arbitrary $N$

$$
\bigcup_{i=1}^{N} A_{i} \subset A
$$

Thus

$$
\mu^{*}(A) \geqslant \mu^{*}\left(\bigcup_{i=1}^{N} A_{i}\right)=\sum_{i=1}^{N} \mu^{*}\left(A_{i}\right)
$$

$N$ can be arbitraily large, so

$$
\mu^{*}(A) \geqslant \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

combining this result with subadditivity gives the desired result

$$
\mu^{*}(A)=\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

where

$$
A \in M_{F} \quad\left\{A_{i}\right\}_{i=1}^{\infty} \subset M_{F}
$$

Definition: $A$ is a measurable set, $A \in M$, if there exisits,

$$
\left\{A_{i}\right\}_{i=1}^{\infty} c m_{F}
$$

such that

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

Theorem: If $A \in O$ then $A \in M_{F}$ if and only if $\mu^{*}(A)<\infty$.
Previously it was shown that if $A \in M_{F}$ then $\mu^{*}(A)<\infty$.

To prove this theorem it must be shown that if $\mu^{*}(A)<\infty$ and $A \in M$ then $A \in \prod_{F}$.

Since $A \in M$ there exists $A_{i} \in M_{F}$ such that

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

Without loss of generality it can be assumed that $A_{i}$ are disjoint since $M_{F}$ is a ring a disjout union can be constructed using the following proceedure

$$
\begin{aligned}
& A_{1}^{\prime}=A_{1} \\
& A_{2}^{\prime}=A_{2}-A_{1} \\
& A_{3}^{\prime}=A_{3}-A_{1} \cup A_{2}
\end{aligned}
$$

where $A_{i}^{\prime} \in M_{F}$ since $M_{F}$ is a ring. Previously it was shown that

$$
A=\bigcup_{i=1}^{\infty} A_{i}=\bigcup_{i=1}^{\infty} A_{i}^{\prime}
$$

so $A_{i} \in M_{F}$ can be assumed disjoint.
Now using subadditivity of $\mu^{*}(A)$ gives

$$
\mu^{*}(A) \leq \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

vext using the same trick used in the last theoram, fixing $N$ and then taking limit and the assumption that $A_{i}$ are mutually disjoint,

$$
\bigcup_{i=1}^{v} A_{i} \subset A
$$

$\Rightarrow \mu^{*}\left(\bigcup_{i=1}^{N} A_{i}\right)=\sum_{i=1}^{N} \mu^{*}\left(A_{i}\right) \leqslant \mu^{*}(A)$
since $N$ is arbitrary and can be arbitrarity large

$$
\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right) \leq \mu^{*}(A)
$$

This result and subadditivity give

$$
\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)=\mu^{*}(A)
$$

Now consider a fixed $\varepsilon>0$ arc let

$$
B_{N}=\bigcup_{i=1}^{N} A_{i}
$$

then $B_{N} \in M_{F}$ and

$$
\begin{aligned}
& d\left(A, B_{N}\right)=\mu^{*}\left(S\left(A, B_{N}\right)\right) \\
& =\mu^{*}\left[\left(A-B_{N}\right) \cup\left(B_{N}-A\right)\right] \\
& =\mu^{*}\left(A-B_{N}\right)
\end{aligned}
$$

since $B_{N} \subset A$, so

$$
\begin{aligned}
\mu^{*}\left(A-B_{N}\right) & =\mu^{*}\left(\bigcup_{j>N} A_{i}\right) \\
& \leqslant \sum_{j>N} \mu^{*}\left(A_{j}\right)<\varepsilon
\end{aligned}
$$

for sufficiently large $N$.

Thus $B_{n} \rightarrow A$ so $\mu^{*}(A)<\infty$ and $A \in m_{F}$.

Definition: Let $\mathcal{L}$ be a collection of subsets of a set $X$. $\mathcal{A}$ is called a $\sigma$-ning if

1. $\mathcal{L}$ is a ring
2. If $\left\{A_{i}\right\}_{i=1}^{\infty} \subset \mathcal{L}$ then $\cup_{i=1}^{\infty} A_{i} \in \mathcal{L}$

Theorem: on is a b-ring First property 2 will be proven. Suppose

$$
A_{1}, A_{2}, \ldots \in M
$$

Let

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

From the definition of $m$ if $A_{i} \in O n$ then

$$
\left\{A_{i j}\right\}_{j=1}^{\alpha} \subset M_{F}
$$

such that

$$
A_{i}=\bigcup_{j=1}^{\infty} A_{c j}
$$

It follows that

$$
A=\bigcup_{i, j=1}^{\infty} A_{i j}
$$

and since

$$
\left\{A_{i j} \xi_{j i=1}^{\infty} c n_{F}\right.
$$

it follows that $A \in M$
Now to show that on is a ring it must be shown that if $A, B \in M$ then $A-B \in M$ and $A \cup B \in M$. It was just shown that $M$ is closed wroter unions so only closure under set difference must be prooen.
First suppose $A \in M_{F}$ and let

$$
B=\bigcup_{i=1}^{\infty} B_{i}
$$

with $B_{i} \in M_{F}$. Since $M_{F}$ is a ring

$$
A \cap B_{i} \in M_{F}
$$

so

$$
A \cap B=\bigcup_{i=1}^{\infty} A \cap B_{i} \in M
$$

form the definition of $o n$. since

$$
A \cap B \subseteq A
$$

it follows that

$$
\mu^{*}(A \cap B) \leq \mu^{*}(A)
$$

so $A \cap B \in M_{F}$.
Now

$$
A \cdot B=A-(A \cap B)
$$

Since $A, A \cap B \in M_{F}$ and $M_{F}$ is a ring it follows that

$$
A-B \in \bigcap_{F}
$$

Now let $A$ be an arbitray element of $M$ and let

$$
A=\bigcup_{i=1}^{B} A_{i}
$$

where $A_{i} \in M_{F}$, low

$$
A-B=\bigcup_{i=1}^{0}\left(A_{i}-B\right)
$$

but $A_{i}-B \in M_{F}$ thus $A-B \in O$ so on is a ring.

Theorem : If $A_{1}, A_{2}, A_{3}, \ldots$ is a countable collection of disjoint sets in $m$

$$
\mu^{*}\left(\bigcup_{i=1}^{\infty} A_{i}\right)=\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

## Proof

Let $A=U_{i=1}^{\infty} A_{i}, A \in M$. Consider two cases.

1. $\mu^{*}(A)<\infty$

Since $A_{i} \subset A, \mu^{*}(A)<\infty$ so $A$ and all $A_{i}$ 's are elements of $M_{F}$. Since $\mu^{*}(A)$ is a measure on $M_{F}$, so

$$
\mu^{*}(A)=\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

2. $\mu^{*}(A)=\infty$

Subadditivity of $\mu^{*}(A)$ gives

$$
\begin{aligned}
& \infty=\mu^{*}(A) \leqslant \sum_{c=1}^{\infty} \mu^{*}\left(A_{c}\right) \\
& \Rightarrow \sum_{i=1}^{\infty} \mu^{*}(A)=\infty
\end{aligned}
$$

Example: $I=\mathbb{R}^{n}$ and $R=R_{\alpha}=$ finite unions of mutti-intervals

$$
a_{i} \leqslant x_{i} \leqslant b_{i} \quad c=1,2, \ldots, n
$$

and

$$
\mu(A)=\left(b_{1}-a_{1}\right)\left(b_{2}-a_{2}\right) \cdots\left(b_{n}-a_{n}\right)
$$

Here $m$ is called the set of

Lebesgue measurable sets in $\mathbb{R}^{n}$ and the extension of $\mu$ to $m$ is called lebesgue measure $\mu_{2}$
what ds these sets look like First

$$
\mathbb{R}^{n} \in \mathbb{O}
$$

Define an interval in $\mathbb{R}^{n}$
$I_{N}=\left\{x \in \mathbb{R}^{n} ;-N \leq X_{i} \leq N, i=1,2, \ldots, n\right\}$
Then

$$
\mathbb{R}^{n}=\bigcup_{N=1}^{\infty} I_{N}
$$

where

$$
I_{N} \in Q \subset \eta_{F}
$$

Theorem: Every open subset of $\mathbb{R}^{n}$ is in $M$.

Let,
$c=\left(a_{1}, a_{2}, \ldots, a_{n}, b_{1}, b_{2}, \ldots, b_{n}\right) \in \mathbb{R}^{2 n}$
where the $a_{i}$ s and $b_{i}$ s
rational and $a_{i}<b_{i}$. Let
$I_{e}=\left\{x \in \mathbb{R}^{n} ; a_{i}<x_{i}<b_{i}, i=1,2, \ldots, n\right\}$
The collection $\left\{I_{c}\right\}$ is countable since the endpoints of the intervals is coundable because the are rational.

Now let $\theta$ be any open set of $\mathbb{R}^{n} \theta$ is equal to the wrion of sets $I_{c}$ such that $I_{c} c \theta$, namely, If $x \in \theta$ there exists a $c$ such that $x \in I_{c} \subset \theta$. From the definition of on it follows that $\theta \in O n$.

Theorem: Every closed subset of $\mathbb{R}^{n}$ is in $M$.

Proof: A is closed so $A^{c}$ is open,

$$
A^{c}=\mathbb{R}^{n}-A \Rightarrow A=\mathbb{R}^{n}-A^{c}
$$

Now since on is a ring it
is closed under set union and set diffence and it was just shown that $A^{c} \in M$ and $\mathbb{R}^{n} \in M$ it follows that $A \in M$.

Definition: The Borel sets are the smallest 6 -ring containing the open sets.

Theorem: If $A \in M$ there exists a Borel set $B \subseteq A$ such that $\mu^{*}(A-B)=0$. That is $A$ can be written as

$$
A=(A-B) \cup B
$$

where $B$ is Borel and

$$
\mu^{*}(A-B)=0
$$

lemma: If $A \in M$ and if $\varepsilon>0$ is given, then there exists a Borel set $G$ such that

$$
A \subset G
$$

and

$$
\mu^{*}(E-A)<\varepsilon
$$

Proof: Finst suppose $\mu^{*}(A)<\infty$ Then by the definition of $\mu^{*}(A)$ a cover

$$
A C \bigcup_{i=1}^{\infty} A_{i}
$$

exists such that

$$
\mu^{*}(A)+\varepsilon>\sum_{i=1}^{\infty} \mu(A)
$$

where each $A_{i}$ is a mult-intercal. Let

$$
C=\bigcup_{i=1}^{\infty} A_{i}
$$

where $t$ is Borel.
More generally if $A \in M$ we can write,

$$
A=\bigcup_{i=1}^{\Delta} A_{i}
$$

where each $A_{i} \in M_{F}$, which follows
from the definition of on. There exists Borel sets $C_{i}$ with $A_{i} \subset E_{i}$ and

$$
\mu^{*}\left(e_{i}-A_{i}\right)<\frac{\varepsilon}{2^{i}}
$$

then from subaditivity of u* it follows that

$$
\begin{aligned}
\mu^{*}(C-A) & <\sum_{i=1}^{\infty} \mu^{*}\left(G_{i}-A_{i}\right) \\
& <\sum_{i=1}^{\infty} \frac{\varepsilon}{\partial^{i}}=\varepsilon \\
\Rightarrow \mu^{*}(C-A) & <\varepsilon
\end{aligned}
$$

Lemma: If $A \in O$ there exists a Borel set FCA with

$$
\mu^{*}(A-F)<\varepsilon
$$

Proof: Choose a Borel set $C$ such that $A^{c} c G$ and $\mu^{*}\left(G-A^{c}\right)<\varepsilon$ by the previous lemma.

Let $F=G^{c}$ then

$$
A-F=A \cdot C^{C}
$$

Consider the relation

$$
C-A^{C}=A-C^{C}
$$

to prove assume $x \in G \cdot A^{c}$
$\Rightarrow x \in G$ and $x \in A^{c}=\Rightarrow$
$x \notin G^{c}$ and $x \in A=0$

$$
x \in C-A^{C}
$$

$\Rightarrow \quad G-A^{C} \subseteq A-G^{C}$
similarly if $x \in A-\epsilon^{c}$
$=x \quad x \in A$ and $x \notin e^{c}$
$\therefore x \notin A^{c}$ and $x \in E$
$\Rightarrow x \in G-A^{c}$
$\Rightarrow A-G^{c} \leq C-A^{c}$
So

$$
C \cdot A^{c}=A \cdot C^{c}
$$

It follows that

$$
\mu^{*}\left(A-C^{C}\right)=\mu^{*}\left(C-A^{C}\right)<\varepsilon
$$

with these lemmas it has been shown that for $A \in M$ there exists a Borel set $G$ with $A C E$ such that

$$
\mu^{*}(G-A)<\varepsilon
$$

and if a Borel set $F$ with FCA

$$
\mu^{*}(A-F)<\varepsilon
$$

The original theorem was to show that for $A \in M$ there exists a Borel set $B \subseteq A$ where

$$
\mu^{\mu}(A-B)=0
$$

To prove this take $A \in M$ for every $N$ let choose a Borel set $F_{N} C A$ such that

$$
\mu^{*}\left(A-F_{N}\right)<\frac{1}{N}
$$

Where use was made of the previous lemma. Let $F=\bigcup_{N=1} E_{N}$ which is a Borel set.
It follows that

$$
A-F \subseteq A-F_{N}
$$

১০

$$
\mu^{*}(A-F) \leqslant \mu^{*}\left(A-F_{N}\right)<\frac{1}{N}
$$

since $i s$ can be arbitrarly large it follows that

$$
\mu^{*}(A-F)=0
$$

Definition $\bar{X}$ is $\sigma$-finite if there exists sels,

$$
x_{i} \in M_{F} \quad i=1,2,3, \ldots
$$

with

$$
I=\bigcup_{i=1}^{\infty} Z_{i}
$$

For example $\mathbb{R}^{n}$ is $\sigma$-finite since

$$
\mathbb{R}^{n}=\bigcup_{i=1}^{\infty} B_{i}
$$

where $B_{i}$ is a ball of radius $i$ centered at the orgin.

## Measure Theory Executive Summary

In this section a summary of the Theorems discussed in this section will be provided as a guide.

The purpose of the previous discussion was to develop the definition of a measurable set.

The following definitions are used to define the dea of a measureable set.
In enumerating the definitions and theorems the values used in "Measure Theory and Probability" will be used.

The definiton of a measureable set builds on a series of definitions.

Definition 1 A ring of sets in $\bar{X}$ is a nonempty collection, $R$, of subsets of $\bar{x}$ sotusfying the following two properties for any sels $A, B \in \mathbb{R}$.

$$
A \cup B \in R \quad A-B \in R
$$

Thus a ring is dosed under set wion and set difference.
From this definition it follows that

$$
A-A=\phi \in Q
$$

$Q$ is also closed under indersection since

$$
A \cap B=A-(A-B)
$$

Defintion 2 The powerset of $I$, denoted by $2 X$ is a ring.
As an example conside

$$
\bar{X}=\{1,2\}
$$

SO

$$
2^{\bar{x}}=\{\phi,\{1\},\{2\},\{1,2\}\}
$$

clearly

$$
\begin{aligned}
& \{1\} \cup\{2\}=\{1,2\}\{\phi\} \cup\{1\}=\{1\} \\
& \{\phi\} \cup\{2\}=\{2\}\{\phi\} \cup\{1,2\}=\{1,2\} \\
& \{1,2\}-\{2\}=\{1\}\{1,2\}-\{1\}=\{2\} \\
& \{1,2\}-\{\phi\}=\{1,2\} \\
& \{2\}-\{1,2\}=\{\phi\}\{1\}-\{1,2\}=\{\phi\}
\end{aligned}
$$

Definition 3: A set function $\mu$ is defined on elements of $R$. If $A, B \in R$ and $A \cap B=\varnothing \mu$ is additive,

$$
\mu(A \cup B)=\mu(A)+\mu(B)
$$

This idea is extentended to include finite catable wriohs. If $A_{i} \in R$ and $A=U_{i=1}^{N} \in R$ then

$$
\mu(A)=\mu\left(\bigcup_{i=1}^{N} A_{i}\right)=\sum_{i=1}^{N} \mu\left(A_{i}\right)
$$

Proposition 5: If $R$ is a ring of subsets of $\bar{x}$ and $\mu$ an additive, nonnegative set function of elements of $R$ then

1. $\mu(\phi)=0$
2. If $A, B \in R$ with $A \subseteq B$ then $\mu(A) \leqslant \mu(B)$. This property is called monotiaty
3. If $A_{1}, A_{2}, A_{3}, \ldots \in \mathbb{R}$ satisfy $A_{i} \cap A_{j}=\varnothing$ for $i \neq j$ then

$$
\mu\left(U_{i=1}^{N} A_{i}\right)=\sum_{i=1}^{N} \mu\left(A_{i}\right)
$$

This property is called Ponite additivity
4. If $A, B \in R$, then
$\mu(A \cup B)+\mu(A \cap B)=\mu(A)+\mu(B)$
This is called the lattice property
6. For any $A_{1}, \ldots, A_{n} \in R$

$$
\mu\left(U_{i=1}^{n} A_{i}\right) \leqslant \sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

Definition 6: Let $R$ be a ring of subsets of $\bar{x}$ and $\mu$ an additive set function on $R$. $\mu$ is called countably additive on $R$ if for any countable collection $\left\{A_{i}\right\}_{i=1}^{\infty} \subset R$ with $A_{i} \cap A_{j}=\varnothing$ and

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

with

$$
\begin{gathered}
A \in R \\
\mu(A)=\sum_{i=1}^{\infty} \mu\left(A_{i}\right)
\end{gathered}
$$

A coutably additive set function $\mu$ on a ring $R$ is called a measure.

Definition 9 : Let $A \subset \bar{X}$. A number $l \geqslant 0$ will be called an approximate outer measure of A if there exists a covering A by a countable collection of sets $A_{1}, A_{2}, A_{3}, \ldots$ with each $A_{i} \in R$ such that

$$
\sum_{i=1}^{\infty} \mu\left(A_{i}\right) \leq l
$$

where $0 \leqslant l<\infty$
Definition 10 : Let $A$ be a subset of $\bar{X}$. The outer measure of $A$, $\mu^{*}(A)$, is the greatest lower bound of the set,
$\mu^{*}(A)=\{l: l$ is an apporimate outer measure of $A\}$
If this set is emply then,

$$
\mu^{*}(A)=\infty
$$

## Proposition 11

1. If $A \in Q$ then $\mu^{*}(A)=\mu(A)$
2. If $A \subset B$ then $\mu^{*}(A)<\mu^{*}(B)$
3. $u^{*}$ is coutably subadditive, $A_{1}, A_{2}, A_{3}, \ldots \in R$ then

$$
\mu^{*}\left(\cup_{i=1}^{\Delta} A_{i}\right) \leq \sum_{i=1}^{\Delta} \mu^{*}\left(A_{i}\right)
$$

If $A=U_{i=1}^{\infty} A_{i}$ then

$$
u^{*}(A) \leqslant \sum_{i=1}^{\infty} u^{*}\left(A_{i}\right)
$$

Since $\mu^{*}(A)$ is defined as the greatest lower bound of the approximate outer measures, there exisls a covering $A \subseteq \cup_{i=1}^{\infty} A_{i}$ such that

$$
\mu^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

where $\varepsilon>0$. Since the opposite inequality holds equality can
be deduced Arguments like this are often used in proofs.

Definition: The distance function is defined by

$$
d(A, B)=\mu^{*}[s(A, B)]
$$

where $A, B \in R$ and $s(A, B)$ is the symetric difference

$$
S(A, B)=(A-B) \cup(B-A)
$$

Convergence of a sequence in $R$ can be defined in the following manner. For a sequence

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \subset R
$$

converges to $A \in Q$ if

$$
d\left(A-A_{i}\right) \rightarrow 0 \text { as } i \rightarrow \infty
$$

this is also written as

$$
A_{i} \rightarrow A \text { as } i \rightarrow \infty
$$

Proposition 14: The Boolean operations in $R$ are continuous with respect to $d$. That is if $A_{i} \rightarrow A$ and $B_{i} \rightarrow B$ in $\mathbb{R}$ then

$$
\begin{gathered}
A_{n} \cup B_{n} \rightarrow A \cup B \\
A_{n} \cap B_{n} \rightarrow A \cap B \\
A_{n}-B_{n} \rightarrow A-B \\
A_{n}^{c} \rightarrow A^{c}
\end{gathered}
$$

Definition: Let $m_{F}$ be the closure of $R$ in $2^{8}$. That is if $A \in M_{E}$ if and only if there exists a sequence of sets

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \subset R
$$

such that $d\left(A_{i}, A\right) \rightarrow 0$ as $i \rightarrow \infty$.
This definition covers the case where $R$ does not include all of its limits. For example $Q$ may only contain open sets and the sequence converges
to a closed sel.
Theorem 18:

1. $m_{F}$ is a ring
2. For $A \in M_{F}, \mu^{*}(A)<\infty$
3. $\mu^{*}$ is a measure on $m_{F}$

Definition 19: A is a measureable set, $A \in M$, if there exists $\left\{A_{i}\right\}_{i=1}^{\infty} \subset M_{F}$ such that,

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

where $m$ is the set of measurable sets

Theorem 20: If $A \in M$ then

$$
A \in M_{F} \Leftrightarrow \mu^{*}(A)<\infty
$$

Note that it is not required that $A \in M_{F}$. If $A \notin M_{F}$ then take
$\mu^{*}(A)=\infty$ so that $\mu^{*}(A)$ is a measure on $M$.

Definition 21: Let 2 be a collection
of subsets of $a \operatorname{set} \bar{x}$. $\mathscr{A}$ is called a s-ring if

1. It is a ring
2. Given $\left\{A_{i}\right\}_{i=1}^{\infty} \subset \mathcal{L}$ and

$$
\bigcup_{i=1}^{\infty} A_{i} \in \mathcal{L}
$$

Theorem 22: $m$ is a $\sigma$-ring
This definition extends $m_{F}$ to irclued infinite unions of sequences in $\mathrm{m} / \mathrm{F}$.

Theorem 23: If $A_{1}, A_{2}, \ldots$ is a coutable collection of disjoint sets in on then

$$
\mu^{*}\left(\bigcup_{i=1}^{0} A_{i}\right)=\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

## Measure Theoretic Modeling

Definition: Let $X$ be a sel and $\exists$ a ring of subsets of $\bar{X}$.

1. $\mathcal{F}$ is a fied if $\bar{X} \in \mathcal{F}$
2. Fis a $\sigma$-field if $\bar{X} \in \mathcal{F}$ and if $f$ is a b-ring.

Definition: Let $I$ be a set and $f$ a field of subsets of $\bar{X}$. Suppose $\mu$ is a measure defined of $j$. Then $\mu$ is a probability measure if

$$
\mu(x)=1
$$

For this case the triple $\{\bar{x}, F, \mu\}$ is called a probability space.

## Discrete Probability Theory

Suppose the sample space is finite or countable.

$$
X=\left\{x_{1}, x_{2}, x_{3}, \ldots\right\}
$$

and assume that each $x_{i}$ has probability $p_{i}$ of occuring where

$$
\sum_{i} P_{i}=1
$$

The probability of an event $A C D$ occuring is given by

$$
\mu(A)=\sum_{x_{i} \in A} P_{i} \quad A \subset \bar{D}
$$

where $A \in \mathcal{F}=2^{\bar{x}}$

## Analysis Digression

Limits superior and Inferror for sequences of Numbers

Consider the sequences

$$
\begin{aligned}
& 0,1,0,1,0,1,0, \ldots \\
& \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{3}{4}, \frac{1}{3}, \frac{4}{3}, \ldots
\end{aligned}
$$

Both series diverge but are bounded. At inforitity both series tend to 0 and 1.

Limits superior and inferior are used to describe these limits.
Recall that the supremium of an ordered set is smallest clement in the set that is greater than or equal to all elements in the set. Symbolically $i s$ is a supremum of $a$ set $S$ is written as

$$
b \geqslant x \quad \forall x \in S
$$

Consider the sequence $\left\{a_{n}\right\}$ the supremum for elements of the sequence for elements with $m \geqslant n$ is given by

$$
x_{n}=\sup \left\{a_{m}: m \geqslant n\right\}
$$

where
$\left\{a_{m}: m \geqslant n\right\}=\left\{a_{n}, a_{n+1}, a_{n+2}\right.$,

$$
\left.a_{n+3}, \ldots\right\}
$$

Clearly the suprimum of the set is $x_{1}$ and

$$
x_{n} \geq x_{n+1}
$$

Thus the sequence of supremums is given by

$$
\left\{x_{1}, x_{2}, x_{3}, \ldots\right\}
$$

is a decreasing sequence.
It follows that the limit supremium is given by

$$
\lim _{n \rightarrow \infty} \sup a_{n}=\lim _{n \rightarrow \infty} x_{n}
$$

The infimum of an ondered set is the largest element in the set less than all elements in the set. Symbolically $b$ is an infimum of $a$ set $s$ is written as

$$
b \leq x \quad \forall x \in S
$$

Consider the sequence $\left\{a_{n}\right\}$ the infimum for elements of the sequence for elements with $m \geqslant n$ is given by

$$
y_{n}=\inf \left\{a_{m}: m \geqslant n\right\}
$$

where

$$
\begin{aligned}
& \left\{a_{m}: m \geqslant n\right\}=\left\{a_{n}, a_{n+1}, a_{n+2},\right. \\
& \left.a_{n+3}, \ldots\right\}
\end{aligned}
$$

Clearly the infinum of the set set is $x_{1}$ and

$$
y_{n} \leqslant y_{n+1}
$$

Thus the sequence of intimums is given by

$$
\left\{y_{1}, y_{2}, y_{3}, \ldots\right\}
$$

is an increasing sequence.
It follows that the limit inferior is given by.

$$
\lim _{n \rightarrow \infty} \inf a_{n}=\lim _{n \rightarrow \infty} y_{n}
$$

Applying these definitions to the previous sequences

$$
\begin{aligned}
& 0,1,0,1,0,1,0, \ldots \\
& \frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{3}{4}, \frac{1}{5}, \frac{4}{5}, \ldots
\end{aligned}
$$

groes for the first sequence, $\{0,1,0,1,0,1, \ldots\}$
$\sup \left\{a_{m}: m \geqslant n\right\}=x_{n}=1$
inf $\left\{a_{m}: m \geqslant n\right\}=y_{n}=0$
thus

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \sup a_{n}=1 \\
& \lim _{n \rightarrow \infty} \inf a_{n}=0
\end{aligned}
$$

Analysis of the second sequence,

$$
\begin{aligned}
& \left\{\frac{1}{3}, \frac{2}{3}, \frac{1}{4}, \frac{3}{4}, \frac{1}{5}, \frac{4}{5}, \ldots\right\} \\
& 1 \leqslant \sup \left\{a_{m}: m \geqslant n\right\} \leqslant \frac{n-1}{n} \\
& 0 \leqslant \inf \left\{a_{m}: m \geqslant n\right\} \leqslant \frac{1}{n}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \sup a_{n}=\lim _{n \rightarrow \infty} \frac{n-1}{n}=1 \\
& \lim _{n \rightarrow \infty} \inf a_{n}=\lim _{n \rightarrow \infty} \frac{1}{n}=0
\end{aligned}
$$

## Cauchy Sequences

A sequence is Cauchy if and only if for every $\varepsilon>0$ there is a natural number $N$ such that for $m, n \geqslant N$

$$
\left|a_{m}-a_{n}\right|<\varepsilon
$$

This definition describes convergence as a decrease in difference between elements of the sequence for large $m$ and $n$.
This definition makes no reference to the limit of the sequence. It can be shown that if the limit is known that this definition is equivalent to

$$
\left|x_{n}-l\right|<\varepsilon
$$

for $\varepsilon>0$ and any $n \geqslant N$ where \& is the limit.

## Limit Superior and Inferior of sequences of sets

For the sequence of sets $\left\{A_{n}\right\}$ The superior limit of this sequence is defined as the set of points that belong to infinite many of those sets, $\lim \sup A_{n}=\{x$ : for all $k$ there is an $n \geqslant k$ such that

$$
\left.x \in A_{n}\right\}
$$

If $x \in \lim \sup _{n \rightarrow \infty} A_{n}$ the it is said that $x \in A_{n}$ infinitely often.
The inferior limit of $\left\{A_{n}\right\}$ is the set of points that belong to all but finitely many of those sets.
$\liminf A_{n}=\{x:$ there exists $k$ such

$$
\begin{array}{ll}
n \rightarrow \infty & \text { that } x \in A_{n} \text { for all } \\
& n \geqslant k \xi
\end{array}
$$

If $x \in \limsup _{n \rightarrow \infty} A_{n}$ it is said that $x \in A_{n}$ eventually. It should be
noted that the finite number of sets that do not contain $x$ must be exhausted before sets contributing to the limit are reached.
If the superior limit and inferior limit of $A_{n}$ are equal then

$$
\lim _{n \rightarrow \infty} A_{n}=\limsup _{n \rightarrow \infty} A_{n}=\lim _{n \rightarrow \infty} \inf _{n \rightarrow \infty}
$$

Now from the definition of union
$\bigcup_{n=k} A_{n}=\{x$ : there exists an $n \geqslant k$ such that $x \in A_{n} \xi$

It follows that if $x \in A_{n}$ for every $n \geqslant k$ then

$$
x \in \bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

thus

$$
\limsup _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

Similarly from the definition of intersection

$$
\bigcap_{n=k}^{\infty} A_{n}=\left\{x: x \in A_{n} \text { for all } n \geqslant k\right\}
$$

It follows that if for some $n \geqslant k$

$$
x \in \bigcap_{n=k}^{\infty} A_{n}
$$

then

$$
x \in \bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}
$$

Thus

$$
\liminf _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}
$$

In summary the set theoretic limits are given by,

$$
\limsup _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

$$
\liminf _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}
$$

Theorem: If $\left\{A_{n}\right\}$ is a monotone sequence of sets then it has a limit. If $\left\{A_{n}\right\}$ is in creasing then

$$
\lim _{n \rightarrow \infty} A_{n}=\bigcup_{n=1}^{\infty} A_{n}
$$

If $\left\{A_{n}\right\}$ is decreasing,

$$
\lim _{n \rightarrow \infty} A_{n}=\bigcap_{n=1}^{\infty} A_{n}
$$

## Proof

Recall that if $\left\{A_{n}\right\}$ is increasing

$$
A_{1} \subset A_{2} \subset A_{3} \subset \cdots
$$

and if $\left\{A_{n}\right\}$ is decreasing

$$
A_{1} \supset A_{2} \supset A_{3} \supset \cdots
$$

Now consider,

$$
\limsup _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

and for an increasing sequence

$$
\bigcup_{n=k}^{\infty} A_{n}=\bigcup_{n=1}^{\infty} A_{n}
$$

since

$$
A_{n} \subset A_{n+1} \Rightarrow A_{n} \cup A_{n+1}=A_{n+1}
$$

Thus

$$
\begin{aligned}
\limsup _{n \rightarrow \infty} A_{n} & =\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n} \\
& =\bigcap_{k=1}^{\infty} \bigcup_{n=1}^{\infty} A_{n} \\
& =\bigcup_{n=1}^{\infty} A_{n}
\end{aligned}
$$

since if

$$
A=\bigcup_{n=1}^{A} A_{n}
$$

then

$$
\bigcap_{k=1}^{\infty} A=A
$$

Now consider the inferior limit.

$$
\liminf _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}
$$

since $A_{n}$ is increasing

$$
\bigcap_{n=k}^{\infty} A_{n}=A_{k}
$$

50

$$
\liminf _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} A_{n}
$$

Thus for an increasing sequence of sels

$$
\lim _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} A_{n} .
$$

Next consider

$$
\liminf _{n \rightarrow \infty} A_{n}=\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}
$$

For a decreasing sequence,

$$
\bigcap_{n=k}^{\infty} A_{n}=\bigcap_{n=1}^{\infty} A_{n}
$$

since $A_{n}$ is decreasing

$$
\begin{aligned}
A_{n} \supset A_{n+1} & \Rightarrow A_{n} \cap A_{n+1}=A_{n+1} \\
\liminf _{n \rightarrow \infty} A_{n} & =\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n} \\
& =\bigcup_{k=1}^{\infty} \bigcap_{n=1}^{\infty} A_{n} \\
& =\bigcap_{n=1}^{\infty} A_{n}
\end{aligned}
$$

since if

$$
A=\bigcap_{n=1}^{\infty} A_{n}
$$

then

$$
\bigcup_{k=1}^{\infty} A=A
$$

Now consider the superior limit.

$$
\limsup _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

since $A_{n}$ is decreasing

$$
\bigcup_{n=k}^{\infty} A_{n}=A_{k}
$$

so

$$
\limsup _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} A_{k}
$$

If follows that for a decreasing sequence of sets

$$
\lim _{n \rightarrow \infty} A_{n}=\bigcap_{k=1}^{\infty} A_{k}
$$

## Example

Consider the sequence of sets

$$
A_{n}=\left[0, \frac{n}{n+1}\right)
$$

The sequence is increasing since

$$
\begin{aligned}
& \frac{n+1}{n+2}-\frac{n}{n+1}=\frac{(n+1)^{2}-n(n+2)}{(n+2)(n+1)} \\
& =\frac{n^{2}+2 n+1-n^{2}-2 n}{(n+2)(n+1)} \\
& =\frac{1}{(n+2)(n+1)}>0
\end{aligned}
$$

trus

$$
\frac{n+1}{n+2}>\frac{n}{n+1}
$$

It follows that

$$
A_{n} \subset A_{n+1}
$$

## Now

$\sup _{k \geqslant n} A_{n}=\bigcup_{k=n}^{\infty} A_{n} \quad \inf _{k \geqslant n} A_{n}=\bigcap_{k=n}^{\infty} A_{n}$
so since $A_{n}$ is increasing

$$
\begin{aligned}
& \sup _{k \geqslant n} A_{n}=\sup _{k \geqslant n}\left(0, \frac{n}{n+1}\right] \\
& =\bigcup_{k=n}^{\infty}\left(0, \frac{n}{n+1}\right] \\
& =\lim _{m \rightarrow \infty} \bigcup_{k=n}^{m}\left(0, \frac{n}{n+1}\right] \\
& =\lim _{m \rightarrow \infty}\left(0, \frac{m}{m+1}\right] \\
& =(0,1]
\end{aligned}
$$

and

$$
\inf _{k \geqslant n} A_{n}=\bigcap_{k=n}^{\infty} A_{n}
$$

$$
\begin{aligned}
& =A_{k} \\
& =\left(0, \frac{n}{n+1}\right]
\end{aligned}
$$

since $A_{k}$ is thereasing. Thus

$$
\begin{aligned}
& \sup _{k \geqslant n} A_{n}=(0,1] \\
& \inf _{k \geqslant n} A_{n}=\left(0, \frac{n}{n+1}\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \sup _{n \rightarrow \infty} A_{n} & =(0,1] \\
\lim _{n \rightarrow \infty} A_{n} & =\lim _{n \rightarrow \infty}\left(0, \frac{n}{n+1}\right] \\
& =(0,1]
\end{aligned}
$$

It follows that

$$
\lim _{n \rightarrow \infty} A_{n}=(0,1]
$$

Theorem : Let $A_{n}, n \in \mathbb{N}$ be a sequence of subsets of $\Omega$.
$\lim _{n \rightarrow \infty} \sup A_{n}=\left\{\omega \in \Omega: \sum_{n=1}^{\infty} I_{A_{n}}(\omega)=\infty\right\}$
$\lim _{n \rightarrow \infty} \inf A_{n}=\left\{\omega \in \Omega: \sum_{n=1}^{\infty} I_{A_{n}}(\omega)<\infty\right\}$
where $I_{A_{n}}(\omega)$ is the indicator function

$$
I_{A_{n}}(\omega)= \begin{cases}1 & \omega \in A_{n} \\ 0 & \omega \in A_{n}\end{cases}
$$

This theorem is saying that if

$$
\omega \in \lim _{n \rightarrow \infty} \sup A_{n}
$$

then $w \in A_{n}$ for every $n$. This is stated as $\omega \in \Omega$ appears infintely often in the sets An. and if

## $\omega \in \lim _{n \rightarrow \infty} \inf A_{n}$

then $w \notin$ An for a tinite number of $A_{n}$.

## Proof

First it will be shown that $\lim _{n \rightarrow \infty} \sup A_{n}=\left\{\omega \in \Omega: \sum_{n=1}^{\infty} I_{A_{n}}(\omega)=\infty\right\}$

If

$$
\omega \in \lim _{n \rightarrow \infty} \sup A_{n}
$$

Then from the definition of limit supremum $\omega \in A_{n}$ for every $n$. It follows that

$$
\sum_{n=1}^{\infty} I_{A_{n}}(\omega)=\infty
$$

similary if,

$$
\sum_{n=1}^{\infty} I_{A_{n}}(\omega)=\infty
$$

Then $\omega \in A_{n}$ for every $A_{n}$. This proves that
$\lim _{n \rightarrow \infty} \sup A_{n}=\left\{\omega \in \Omega: \sum_{n=1}^{\infty} I_{A_{n}}(\omega)=\infty\right\}$
Now for the second relation if

$$
\omega \in \lim _{n \rightarrow \infty} \inf A_{n}
$$

then from the definition of the inferior limit there are a finite number of $A_{n}$ where $\omega \notin A_{n} \Rightarrow \omega \in A_{n}^{c}$ thus

$$
\sum_{n=1}^{\infty} I_{A_{n}^{c}}(\omega)<\infty
$$

similarly if

$$
\sum_{n=1}^{\infty} I_{A_{n}^{c}}(\omega)<\infty
$$

There are a Cinite number of $\omega \in A_{n}^{c}$ thus

$$
\omega \in \liminf _{n \rightarrow \infty} A_{n}
$$

Thus

$$
\lim _{n \rightarrow \infty} \inf A_{n}=\left\{\omega \in \Omega: \sum_{n=1}^{\infty} I_{A_{n}}(\omega)<\infty\right\}
$$

## Bernoulli sequences and Random walks

For this case it was previoushl shown that the sample space can be mapped to $(0,1]$. several example events, $E$, were mapped to a finite union of intervals on $(0,1]$ using the Borel principal. This proceedure created the Borel set BE where the probabiuty of the event is given by

$$
P(E)=\mu\left(B_{E}\right)
$$

In this section Borel sets will be constructed for more complex events.

## Finite Paterns

Let $E$ be the event that a presscribed finite pattern occurs infinitehy often. An example finte event would be the sequence HTTH.

This event can be modled as a finite number of conditions on Rademacher functions. For example for the pattern HTTH the event that the pattern occurs at the n'th step is given by,

$$
\begin{gathered}
B_{E_{n}}=\left\{\omega \in \Omega ; R_{n}(\omega)=1, R_{n+1}(\omega)=-1,\right. \\
\left.R_{n+2}(\omega)=-1, R_{n+3}(\omega)=1\right\}
\end{gathered}
$$

Consider $n=1$,

$$
\begin{gathered}
B_{E_{1}}=\left\{\omega \in \Omega ; R_{1}(\omega)=1, R_{2}(\omega)=-1\right. \\
R_{3}(\omega)=-1, R_{4}(\omega)=1
\end{gathered}
$$

It follows that the endpoints of the interval are given by

$$
\begin{aligned}
\omega_{1} & =0.1001000 \cdots \\
& =\frac{1}{2}+\frac{1}{24}=\frac{1}{2}\left(1+\frac{1}{8}\right) \\
& =\frac{9}{16}
\end{aligned}
$$

$$
\begin{aligned}
\omega_{2} & =0.100111111 \ldots \\
& =0.101000 \ldots \\
& =\frac{1}{2}+\frac{1}{2^{3}}=\frac{1}{2}\left(1+\frac{1}{4}\right) \\
& =\frac{5}{8}=\frac{10}{16}
\end{aligned}
$$

## Thus

$$
B_{E_{1}}=\left(\frac{9}{16}, \frac{10}{16}\right]
$$

For $B_{E_{2}}$ there will be two intervals. The endpoints are given by

$$
\begin{aligned}
\omega_{1,1} & =0.01001000 \\
& =\frac{1}{4}+\frac{1}{2^{5}}=\frac{1}{4}\left(1+\frac{1}{8}\right) \\
& =\frac{1}{4}\left(\frac{9}{8}\right)=\frac{9}{32} \\
\omega_{1,2} & =0.010011111 \\
& =0.0101000
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{4}+\frac{1}{24}=\frac{1}{4}\left(1+\frac{1}{4}\right) \\
& =\frac{1}{4}\left(\frac{5}{4}\right)=\frac{5}{16}=\frac{10}{32} \\
& \begin{aligned}
w_{2,1} & =0.11001000 \\
& =\frac{1}{2}+\frac{1}{4}+\frac{1}{25} \\
& =\frac{1}{2}+\frac{9}{32}=\frac{16}{32}+\frac{9}{32} \\
& =\frac{25}{32} \\
w_{2,2} & =0.110011111 \ldots \\
& =0.1101000 \ldots \\
& =\frac{1}{2}+\frac{10}{32}=\frac{10}{32}+\frac{10}{32} \\
& =\frac{26}{32}
\end{aligned}
\end{aligned}
$$

Thus

$$
B_{E_{2}}=\left(\frac{9}{32}, \frac{10}{32}\right] \cup\left(\frac{25}{32}, \frac{26}{32}\right]
$$

In summary

$$
\begin{aligned}
& B_{E_{1}}=\left(\frac{9}{16}, \frac{10}{16}\right] \\
& B_{E_{2}}=\left(\frac{9}{32}, \frac{10}{32}\right] \cup\left(\frac{25}{32}, \frac{26}{32}\right]
\end{aligned}
$$

seeing the pattern $B_{E_{n}}$ will consist of $2^{n-1}$ intervals of length $1 / 2^{3+n}$. Thus each $B_{E_{n}}$ will be a finite union of interoals
since $B_{E_{n}}$ occurs infinitely often

$$
\begin{aligned}
B_{E} & =\limsup _{n \rightarrow \infty} B_{E_{n}} \\
& =\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} B_{E_{n}}
\end{aligned}
$$

If follows that $B_{E}$ is a Borel set since it is a countable union of intervals.

## Law of Large Numbers

Let $E$ be the cuent that Bernouli sequences doey the law of large numbers. The number of heads obtained after $n$ tosses is given by

$$
S_{n}(\omega)=\sum_{k=1}^{n} R_{k}(\omega)
$$

then

$$
B_{E}=\left\{\omega \in \Omega: \frac{S_{n}(\omega)}{n} \rightarrow 0 \text { as } n \rightarrow 0\right\}
$$

Now

$$
\frac{S_{n}(\omega)}{n} \rightarrow 0 \text { as } n \rightarrow \infty
$$

means that for $r>0$ there is a $k>0$ such that

$$
\left|\frac{S_{n}(\omega)}{n}\right|<\frac{1}{r} \quad \text { whenever } n \geqslant k
$$

Let

$$
A_{n, r}=\left\{\omega \in \Omega:\left|\frac{s_{n}(\omega)}{n}\right|<\frac{1}{r}\right\}
$$

It can be shown that

$$
B_{E}=\bigcap_{r=1}^{\infty} \bigcup_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}, r
$$

which is Borel since An,r is a finite union of intervals

## Borel - Cantelli Lemma

Theorem : First Borel-Cantelli Lemma Given $B_{1}, B_{2}, \ldots \in \mathcal{F}$. Let $B$ occur occur infinitely often,

$$
B=\lim _{n \rightarrow \infty} \sup _{n} B_{n}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} B_{n}
$$

Then

$$
\sum_{i=1}^{\infty} \mu\left(B_{i}\right)<\infty
$$

implies

$$
\mu(B)=\partial
$$

## Proof

Let $A_{k}=U_{n=k}^{A} B_{n}$ so that

$$
B=\bigcap_{k=1}^{\infty} A_{k}
$$

It follows that $B \subseteq A_{k}$ for every $K$. Now from subadditivity of measure it follows that

$$
\mu\left(A_{k}\right) \leqslant \sum_{n=k}^{\infty} \mu\left(B_{n}\right)
$$

since it is assumed that

$$
\sum_{n=1}^{\infty} \mu\left(B_{n}\right)<\infty
$$

for $\varepsilon>0$ there is a $k>0$ such that

$$
\mu\left(A_{k}\right) \leq \sum_{n=k}^{\infty} \mu\left(B_{k}\right)<\varepsilon
$$

since $B \subseteq A_{k}$ for every $k$

$$
\mu(B)<\mu\left(A_{k}\right)<\varepsilon
$$

since $\varepsilon$ is arbitrary $\varepsilon=0$ is possible so

$$
\mu(B)=0
$$

Example: Run length For $\omega \in \Omega$ define the n'th run-length function $l_{n}(\omega)$ as the number of consecutive i's in the binary representation of $w$ after the n'th place.

That is $\ln (\omega)=k$ if
$R_{n}(\omega)=1, R_{n+1}(\omega)=1, \ldots, R_{n+k}(\omega)=1$
Consoder the sequence of non-negative integers $r_{1}, r_{2}, r_{3}, \ldots$ and let $E_{n}$ denote the event $\ln (\omega) \geqslant r_{n}$. Then

$$
\begin{gathered}
B_{E_{n}}=\left\{\omega \in \Omega: R_{n}(\omega)=R_{n+1}(\omega)=\right. \\
\left.\cdots=R_{n+r_{n}-1}(\omega)=1\right\}
\end{gathered}
$$

En will occur infinitely often so

$$
B_{E}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} B_{E_{n}}
$$

For each value of $n$ there will be $2^{n-1}$ runs length $l(\omega) \geqslant r_{n}$. The total number of out comes after $n+r_{n}-1$ trials will be $2^{n+r_{n}-1}$. It follows that fraction of outcomes with run length $r^{n}$ is given by

$$
\frac{2^{n-1}}{2^{n-1+r_{n}}}=\left(\frac{1}{2}\right)^{r_{n}}
$$

Thus

$$
\mu\left(B_{E_{n}}\right)=\left(\frac{1}{2}\right)^{r_{n}}
$$

Now the first Borel-Cantelli theorem states that if an event occurs infinitely often and if

$$
\sum_{n=1}^{\infty} \mu\left(B_{n}\right)<\infty
$$

the

$$
\mu(B)=0
$$

If follows that

$$
\sum_{n=1}^{\infty} \mu\left(B_{E_{n}}\right)=\sum_{n=1}^{\infty}\left(\frac{1}{2}\right)^{r_{n}}<\Delta
$$

Since $r_{n}>0 \forall n$. Thus

$$
\mu\left(B_{E}\right)=0 .
$$

Definition: Conditional Probability
Two events $E_{1}$ and $E_{2}$ are independent if the outcome of $E$ does not effect the outcome of $E_{2}$. If the outcome of $E_{1}$ dses effect the sutcome of $E_{2}$ knowledge that $E_{1}$ has occured means that elements from the sample space $B_{E}$, are known and may include $B_{E_{2}}$
The conditional probability is proportion of the elements in $B_{E_{1}}$ that are in $B_{E_{2}}$. A good choice for this measure is

$$
\frac{\mu\left(B_{E_{1}} \cap B_{E_{2}}\right)}{\mu\left(B_{E_{1}}\right)}
$$

This ratio is the conditional probability of $E_{2}$ given $E_{1}$. If $E_{1}$ and $E_{2}$ are independent the conditional propability should be the probability that
$E_{2}$ occurs with no prior knowledge that $E_{1}$ has occured,

$$
\mu\left(B_{E_{2}}\right)=\frac{\mu\left(B_{E_{1}} \cap B_{E_{2}}\right)}{\mu\left(B_{E_{1}}\right)}
$$

This will be the case if

$$
\mu\left(B_{E_{1}} \cap B_{E_{2}}\right)=\mu\left(B_{E_{1}}\right) \mu\left(B_{E_{2}}\right)
$$

Example
Let $X=\Omega, \mu=$ Lebesgue measure

$$
\begin{aligned}
& E_{1}=\left\{\omega \in \Omega ; R_{1}(\omega)=1\right\} \\
& E_{2}=\left\{\omega \in \Omega ; R_{2}(\omega)=1\right\}
\end{aligned}
$$

It folbws that

$$
\begin{gathered}
B_{E_{1}}=(1 / 2,1] \\
B_{E_{2}}=(4 / 1,1 / 2] \cup(3 / 4,1]
\end{gathered}
$$

Now

$$
\begin{aligned}
B_{E_{1}} \cap B_{E_{2}} & =(1 / 2,1] \cap\{(1 / 4,1 / 2] \cup(3 / 4,1\rceil\} \\
& =(3 / 4,1]
\end{aligned}
$$

It follows that

$$
\mu\left(B_{E_{1}} \cap B_{E_{2}}\right)=1 / 4
$$

bat

$$
\begin{aligned}
\mu\left(B_{E_{1}}\right) \mu\left(B_{E_{2}}\right) & =(12)\left(\frac{1}{4}+1 / 4\right) \\
& =(1 b)(12) \\
& =1 / 4
\end{aligned}
$$

thus

$$
\mu\left(B_{E_{1}} \cap B_{E_{2}}\right)=\mu\left(B_{E_{1}}\right) \mu\left(B_{E_{2}}\right)
$$

so $B_{E_{1}}$ and $B_{E_{2}}$ are independent as expected.

Theorem : If $A_{1}, A_{2}, \cdots \mathcal{F}$ and independent then $A^{c}, A^{c}, A_{3}^{c}, \ldots$
are independent.

## Proof

Let $A_{1}, A_{2}, A_{3}, \ldots \in \mathcal{F}$ and independent then

$$
\begin{aligned}
& \mu\left(A_{1} \cap A_{2} \cap A_{3} \cap \cdots\right) \\
& \quad=\mu\left(A_{1}\right) \mu\left(A_{2}\right) \mu\left(A_{3}\right) \cdots
\end{aligned}
$$

First consider $A_{1}$ and $A_{2}$,

$$
\mu\left(A_{1} \cap A_{2}\right)=\mu\left(A_{1}\right) \mu\left(A_{2}\right)
$$

Now

$$
A_{1}=\left(A_{1} \cap A_{2}\right) \cup\left(A_{1} \cap A_{2}^{C}\right)
$$

where $\left(A_{1} \cap A_{2}\right) \cap\left(A_{1} \cap A_{2}^{c}\right)=\varnothing i t$ follows that

$$
\begin{aligned}
\Rightarrow \mu\left(A_{1}\right)=\mu\left(A_{1} \cap A_{2}\right)+\mu\left(A_{1} \cap A_{2}^{c}\right) & \\
\Rightarrow \mu\left(A_{1} \cap A_{2}^{c}\right) & =\mu\left(A_{1}\right)-\mu\left(A_{1} \cap A_{2}\right) \\
& =\mu\left(A_{1}\right)-\mu\left(A_{1}\right) \mu\left(A_{2}\right)
\end{aligned}
$$

$$
=\mu\left(A_{1}\right)\left[1-\mu\left(A_{2}\right)\right]
$$

but

$$
\begin{aligned}
& \mu\left(A_{2}\right)+\mu\left(A_{2}^{c}\right)=1 \\
\Rightarrow & \mu\left(A_{2}^{c}\right)=1-\mu\left(A_{2}\right)
\end{aligned}
$$

Thus

$$
\mu\left(A_{1} \cap A_{2}^{c}\right)=\mu\left(A_{1}\right) \mu\left(A_{2}^{c}\right)
$$

Next let

$$
\begin{aligned}
A_{2}^{c}=\left(A_{2}^{c} \cap A_{1}\right) \cup\left(A_{2}^{c} \cap A_{1}^{c}\right) & \\
\Rightarrow \mu\left(A_{2}^{c}\right)=\mu\left(A_{2}^{c} \cap A_{1}\right)+\mu\left(A_{2}^{c} \cap A_{1}^{c}\right) & \\
\Rightarrow \mu\left(A_{2}^{c} \cap A_{1}^{c}\right) & =\mu\left(A_{2}^{c}\right)-\mu\left(A_{2}^{c} \cap A_{1}\right) \\
& =\mu\left(A_{2}^{c}\right)-\mu\left(A_{2}^{c}\right) \mu\left(A_{1}\right) \\
& =\mu\left(A_{2}^{c}\right)\left[1-\mu\left(A_{1}\right)\right] \\
& =\mu\left(A_{2}^{c}\right) \mu\left(A_{1}^{c}\right)
\end{aligned}
$$

since

$$
\mu\left(A_{1}\right)=1-\mu\left(A_{1}^{C}\right)
$$

trus

$$
\mu\left(A_{2}^{c} \cap A_{1}^{c}\right)=\mu\left(A_{2}^{c}\right) \mu\left(A_{1}^{c}\right)
$$

It can be shown that this holds arbitrary intersections. If

$$
\mu\left(\bigcap_{i=1}^{\infty} A_{i}\right)=\prod_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

Then

$$
\mu\left(\bigcap_{i=1}^{\infty} A_{i}^{c}\right)=\prod_{i=1}^{\infty} \mu\left(A_{i}^{c}\right)
$$

Theorem: Second Borel-Cantelli Theorem Let $A_{1}, A_{2}, \ldots$ be an independent collection of sets in $f$. From the previous theorem it follows that $A_{1}^{c}, A_{2}^{c}, \ldots$ are independent events in $\mathcal{F}$. If $A_{i}$ occurs infinitely often and

$$
\sum_{c=1}^{N} u\left(A_{i}\right)=\infty
$$

tren

$$
\mu(A)=1
$$

where

$$
A=\left\{A_{i} ; 1.0 .\right\}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

Now DeMorgan's law gives

$$
\begin{aligned}
A^{c} & =\left(\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}\right)^{c}=\bigcup_{k=1}^{\infty}\left(\bigcup_{n=k}^{\infty} A_{n}\right)^{c} \\
& =\bigcup_{k=1}^{\infty} \bigcap_{n=k}^{\infty} A_{n}^{c}
\end{aligned}
$$

Thus

$$
\begin{aligned}
A^{c} & =\liminf _{n \rightarrow \infty} A_{n}^{c} \\
& =\bigcup_{k=1}^{\infty} \bigcap_{n=c}^{\infty} A_{n}^{c}
\end{aligned}
$$

To show $\mu(A)=1$ it is sufficient to show $\mu\left(A^{c}\right)=0$.

By subadditivity

$$
\mu\left(A^{c}\right) \leq \sum_{k=1}^{\infty} \mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right)
$$

It follows that if

$$
\mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right)=0
$$

then

$$
\mu\left(A^{C}\right)=0
$$

Now from the assumed independence of $A_{n}{ }^{c}$ it follows
that

$$
\mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right)=\prod_{n=k}^{\infty} \mu\left(A_{n}^{c}\right)
$$

Now

$$
\mu\left(A_{n}^{c}\right)=1-\mu\left(A_{n}\right)
$$

Consider the relation

$$
1-x \leqslant e^{-x}
$$

To show this consider

$$
\begin{aligned}
1-x & -e^{-x}=1-x-\left(1-x+x^{2}-x^{3}+x^{4}-x^{5}\right) \\
& =x^{2}-x^{3}+x^{4}-x^{5}+\ldots \\
& =x^{2}\left(1-x+x^{2}-x^{3}\right) \\
& =x^{2} e^{-x} \geqslant 0
\end{aligned}
$$

## Thus

$$
1-x \leqslant e^{-x}
$$

using this relation gives

$$
\mu\left(A_{n}^{C}\right)=1-\mu\left(A_{n}\right) \leq e^{-\mu\left(A_{n}\right)}
$$

Thus

$$
\begin{aligned}
\mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right) & =\prod_{n=k}^{\infty} \mu\left(A_{n}^{c}\right) \\
& \leqslant \prod_{n=k}^{\infty} e^{-\mu\left(A_{n}\right)} \\
& =e^{-\sum_{n=k}^{\infty} \mu\left(A_{n}\right)}
\end{aligned}
$$

But it is assumed that

$$
\sum_{n=k}^{\infty} u\left(A_{n}\right)=\infty
$$

Thus

$$
e^{-\sum_{n=k}^{\infty} \mu\left(A_{n}\right)}=0
$$

and

$$
\mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right)=0
$$

and

$$
\begin{aligned}
& \mu\left(A^{c}\right) \leqslant \sum_{k=1}^{\infty} \mu\left(\bigcap_{n=k}^{\infty} A_{n}^{c}\right)=0 \\
& =\mu\left(A^{c}\right)=0 \\
& \Rightarrow \mu(A)=1-\mu\left(A^{c}\right)=1
\end{aligned}
$$

Thus if A occurs infinitely often,

$$
A=\left\{A_{i} ; 1.0 .\right\}=\bigcap_{k=1}^{\infty} \bigcup_{n=k}^{\infty} A_{n}
$$

and

$$
\sum_{i=1}^{n} \mu\left(A_{i}\right)=\infty
$$

and $\left\{A_{i}\right\}$ are uncorrelated then

$$
\mu(A)=1
$$

## Example

Let $H_{n}$ denote the cuent of a head on the n'th toss of a Berroulli sequence. The set is given by

$$
A_{n}=\left\{\omega \in \Omega ; R_{n}(\omega)=1\right\}
$$

show that the

$$
\mu\left(A_{n}\right)=1 / 2
$$

and that the $A_{n}$ are independent.
low for $n=1$ the end points of the interval containing the event are given by

$$
\begin{aligned}
& \omega_{1}=0.1000 \ldots=1 / 2 \\
& \omega_{2}=0.11111=1
\end{aligned}
$$

Thus

$$
A_{n}=(12,1]
$$

so

$$
\mu\left(A_{n}\right)=1-1 / 2=1 / 2
$$

for $n=2$ there will be two intervals. The end points of the intervals are given by

$$
\begin{aligned}
& \omega_{11}=0.01000 \cdots=1 / 4 \\
& \omega_{12}=0.011111=2 / 4=12 \\
& \omega_{21}=0.11000 \cdots=3 / 4 \\
& \omega_{22}=0.111111 \cdots=4 / 4=1
\end{aligned}
$$

Thus

$$
A_{2}=(1 / 4,1 / 2] \cup(3 / 4,1]
$$

and

$$
\mu\left(A_{2}\right)=(12-1 / 4)+(1-3 / 4)
$$

$$
=1 / 4+1 / 4=1 / 2
$$

For $n=3$ there will be 4 intervals with endpoints

$$
\begin{aligned}
& \omega_{11}=0.001000=1 / 8 \\
& \omega_{12}=0.001111 \cdots=218 \\
& \omega_{21}=0.011000 \cdots=318 \\
& \omega_{32}=0.01111 \cdots=418 \\
& \omega_{31}=0.101000=5 / 8 \\
& \omega_{32}=0.101111 \cdots=618 \\
& \omega_{42}=0.111000 \cdots=718 \\
& \omega_{41}=0.11111 \cdots=1
\end{aligned}
$$

Thus

$$
\begin{aligned}
A_{3}= & (1 / 8,2 / 8] \cup(3 / 8,4 / 8] \cup(5 / 8,6 / 8] \\
& \cup(7 / 8,1]
\end{aligned}
$$

The pattern is clear

$$
A_{n}=\bigcup_{i=1}^{\partial^{n-1}}\left(\frac{\partial i-1}{\partial^{n}}, \frac{\partial i}{\partial^{n}}\right]
$$

Now for the n'th event the endpoints of the intervals company the event have the form

$$
\begin{aligned}
& 0 . a_{1} a_{2} \cdots a_{n-1} 100 \ldots \\
& 0 . a_{1} a_{2} \cdots a_{n-1} 1111 \ldots
\end{aligned}
$$

The number of intervals will be the number of possible values of

$$
a_{1} a_{2} \cdots a_{n-1}
$$

which is given by $2^{n-1}$. The length of each interval is given by

$$
\begin{aligned}
& 0 . a_{1} a_{2} \cdots a_{n-1} 11111 \cdots \\
& -0 . a_{1} a_{2} \cdots a_{n-1} 1000 \\
& =0.00 \cdots 001111 \cdots \\
& =0.00 \cdots 01000 \cdots \\
& =1 / 2^{n}
\end{aligned}
$$

It follows that

$$
\mu\left(A_{n}\right)=\frac{2^{n-1}}{2^{n}}=\frac{1}{2}
$$

which is the desired result.
To develop an intuition of how intersections work consider the figure below which compars in for the first few values
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-109.jpg?height=598&width=1285&top_left_y=1035&top_left_x=82)

Assume $n<m$.

$$
\begin{aligned}
& A_{1} \cap A_{2}=(3 / 4,1] \\
& A_{1} \cap A_{3}=(5 / 8,6 / 8] \cup(7 / 8,1]
\end{aligned}
$$

$$
\begin{aligned}
A_{2} \cap A_{4}= & (5 / 16,6 / 16] \cup(7 / 16,8 / 16] \cup \\
& (13 / 16,14 / 16] \cup(15 / 16,1]
\end{aligned}
$$

Now using the previous resuls, the number of intervals in Am is groen by $2^{m-1}$ and the length of each interval is $2^{-m}$. Regardless of which sets are chosen the intersection will consist of $1 / 2$ the intervals in Am it follows that

$$
\begin{aligned}
\mu\left(A_{n} \cap A_{m}\right) & =\left(\frac{1}{2}\right) 2^{m-1}\left(\frac{1}{2^{m}}\right) \\
& =\left(\frac{1}{2}\right)\left(\frac{1}{2}\right) \\
& =\mu\left(A_{n}\right) \mu\left(A_{m}\right)
\end{aligned}
$$

similarly a third intersection will contain 1/4 of the intervals in the event with the larger number interval count and after the K'th intersection
the intersection will $1 / 2^{k-1}$ of the intervals in the set with the largest number of intervals. It follows that

$$
\begin{aligned}
\mu\left(\bigcap_{i=1}^{n} A_{i}\right) & =\left(\frac{1}{2^{k-1}}\right) 2^{k-1}\left(\frac{1}{2 k}\right) \\
& =\frac{1}{2^{k}} \\
& =\prod_{i=1}^{k} \mu\left(A_{i}\right)
\end{aligned}
$$

Thus $\left\{A_{n}\right\}_{n=1}^{\infty}$ are irdependent.
Now the event of a head occuring after the n'th toss occurs infinitely often,

$$
A=\left\{A_{i}: i, 0\right\}=\bigcap_{k=1}^{\infty} \bigcap_{n=k} A_{k}
$$

Using the second Borel-Cantelli theorem, If an event occurs infinitely often and $\sum_{i=1}^{\beta} \mu\left(A_{i}\right)=\infty$ then $\mu(A)=1$.

For the event of tossing heads on the n'th toss

$$
\sum_{i=1}^{A} \mu\left(A_{i}\right)=\sum_{i=1}^{\infty} \frac{1}{2}=\Delta
$$

It follows that a head occurs infonitely often in a Bernalli sequence with probalitity 1 ,

$$
\mu(A)=1
$$

## Integration

## Measureable Functions

In the study of integration functions are allowed to take on the values $\pm \infty$. This leads to the definition of the extended real number system

$$
\mathbb{R} \cup\{\infty\} \cup\{-\infty\}
$$

$\pm \infty$ have the following properties

1. $-\infty<a<\infty, \quad a \in \mathbb{R}$
2. $a+( \pm \infty)= \pm \infty, \quad a \in \mathbb{R}$
3. $a( \pm \infty)= \pm \infty, a \in \mathbb{R}, a>0$
4. $-1( \pm \infty)=\mp \infty$

Now let $(I, F, \mu)$ define a measure space. Let $f$ be a function on I with extended real number values.

## Defintion Measureable Function

A function $f$ is measurable if for all $a \in \mathbb{R}$ the set

$$
A=\{x \in \mathbb{X} ; f(x)>a\} \in \mathcal{F}
$$

Measurable functions have the following properties which are equivalent

1. $\forall a \in \mathbb{R},\{x: f(x)>a\} \in \mathcal{F}$
2. $\forall a \in \mathbb{R},\{x ; f(x) \geqslant a\} \in \mathcal{F}$
3. $\forall a \in \mathbb{R},\{x ; f(x)<a\} \in \mathcal{F}$
4. $\forall a \in \mathbb{R},\{x ; f(x) \leq a\} \in \mathcal{F}$

## Proof

Proposition 1 and 4 are equivalent since if

$$
A=\{x ; f(x)>a\}
$$

then

$$
A^{c}=\{x ; f(x) \leq a\}
$$

It follows that $A \in \mathcal{F} \Leftrightarrow A^{c} \in \mathcal{F}$
using a similar argument 2 ard 3 are equivalent,

$$
A=\{x ; f(x) \geqslant a\}
$$

then

$$
A^{C}=\{x ; f(x)<a\}
$$

It follows that $A \in \mathcal{F} \Leftrightarrow A^{c} \in \mathcal{F}$ To show that $1 \Rightarrow 2$ consider

$$
\bigcap_{n=1}^{\infty}\{x ; f(x)>a-\ln \}
$$

from proposition 1 for every value of $n$

$$
\{x ; f(x)>a-\ln \} \in \mathcal{F}
$$

and

$$
\begin{aligned}
\bigcap_{n=1}^{\infty} & \{x ; f(x)>a-\ln \} \\
= & \{x ; f(x)>a-1\} \cap\{x ; f(x)>a-1 / 2\} \\
& \cap\{x ; f(x)>a-1 / 3\} \cap \ldots
\end{aligned}
$$

$$
=\{x ; f(x) \geqslant a\}
$$

Thus $1 \Rightarrow 2$, similarly to show that $2 \Rightarrow 1$ consider

$$
\bigcup_{n=1}^{\infty}\{x ; f(x) \geqslant a+1 / n\}
$$

by tern 2 for every $n$

$$
\{x: f(x) \geqslant a+1 / n\} \in \mathcal{F}
$$

and

$$
\begin{aligned}
\bigcup_{n=1}^{\infty} & \{x ; f(x) \geqslant a+1 / n\} \\
= & \{x ; f(x) \geqslant a+1\} \cup\{x ; f(x) \geqslant a+b\} \\
& \cup\{x ; f(x) \geqslant a+1 / 3\} \cup \ldots \\
& =\{x ; f(x) \geqslant a\}
\end{aligned}
$$

thus $2 \Rightarrow 1 \Rightarrow 2 \Leftrightarrow 1$. It has been shown that

$$
1 \Leftrightarrow 4 \quad 2 \Leftrightarrow 3 \quad 1 \Leftrightarrow 2
$$

It follows that all statements
are equivalent.

## Definition Extended Borel sets

The extended Borel sets are the collection of subsets of

$$
\mathbb{R} \cup\{+\infty\} \cup\{-\infty\}
$$

Having one of the following forms

$$
\begin{gathered}
A, A \cup\{+\infty\}, A \cup\{-\infty\}, \\
A \cup\{+\infty,-\infty\}
\end{gathered}
$$

where $A$ is a Borel set. For every extended Borel set, $B$

$$
\{x ; f(x) \in B\}
$$

It can be seen that this statement is equivalent to the previous propositions since the inequalities define Borel sets.

## Example

Let $\bar{X}=\mathbb{R}^{n}$ and let $\mathcal{F}=m$ be the lebesgue measurable sets. If

$$
f: \mathbb{R}^{n} \rightarrow \mathbb{R}
$$

is continuous, then $f$ is measurable If $a \in \mathbb{R}$ then

$$
\left\{x \in \mathbb{R}^{n} ; f(x)>a\right\}
$$

is open and thus a Borel set since a Borel set is any countable union of open sets.

## Example

Let $X=B$, where $B$ is a Bernoulli sequence. Where $B$ is mapped to $\Omega=(0,1]$ using a fractional binary expansion.
Consider the n'th Rademacher function, $R_{n}(\omega)$. These are measurable because the are plecewise constant, namely for any subset

$$
A \in \mathbb{R} \cup\{+\infty\} \cup\{\alpha\}
$$

Then

$$
\left\{\omega \in \Omega ; R_{n}(\omega) \in A\right\}
$$

since $R_{n}(\omega)$ is a union of $2^{n}$ intervals

Smilary

$$
S_{n}(\omega)=\sum_{i=1}^{n} R_{n}(\omega)
$$

$s_{n}(\omega)$ is also piecewise constant consisting of a finite conion of intervals.
Recall that a random variable is defined by

$$
f: X \rightarrow \mathbb{R}
$$

when $(A, F, \mu)$ is a probability space. It follows the random variable can be considered synonymous with measurable
function.
Theorem : Let $P$ and $g$ be measurable functions on I. Let $\max (f, g)(x)$ be a function on $\bar{x}$ defined by

$$
\max (f, g)(x)=\max [f(x), g(x)]
$$

Then $\max (f, g)(x)$ is measurable. Similarly

$$
\min (f, g)=\min [f(x), g(x)]
$$

is measureable

## Proof

The proof follows from the definitions

$$
\begin{aligned}
& \{x ; \max (f ; g(x)>a\} \\
& \quad=\{x ; f(x)>a\} \cup\{x ; g(x)>a\} \\
& \{x ; \min (f ; g(x)>a\} \\
& \quad=\{x ; f(x)>a\} \cap\{x ; g(x)>a\}
\end{aligned}
$$

Since $f(x)$ and $g(x)$ are measurabe,

$$
\begin{aligned}
& \{x ; f(x)>a\} \in \mathcal{F} \\
& \{x ; g(x)>a\} \in \mathcal{F}
\end{aligned}
$$

It follows that the union and intersection will be elements of $\mathcal{F}$.

An intutive understanding of these definitions is obtained by considering the case where

$$
\{x ; g(x)>a\}=\{\phi\}
$$

It follows that

$$
\begin{aligned}
& \{x ; \max (f, g(x)>a\} \\
& =\{x, f(x)>a\} \\
& \begin{aligned}
\{x ; \min (f, g)(x)>a\} \\
=\{\phi\}
\end{aligned}
\end{aligned}
$$

The max gives the largest
set of exlements satisting the inequality and min the minimum set.

Theorem : Let $f$ be a measurable function on $\bar{X}$ and define

$$
\begin{aligned}
& f_{+}(x)=\left\{\begin{array}{cc}
f(x) & \text { if } f(x) \geqslant 0 \\
0 & \text { if } f(x)<0
\end{array}\right. \\
& f_{-}(x)=\left\{\begin{array}{cc}
-f(x) & \text { if } f(x) \leqslant 0 \\
0 & \text { if } f(x)>0
\end{array}\right.
\end{aligned}
$$

Then $f_{+}(x)$ and $f_{-}(x)$ are measurable.
Proof

$$
\begin{aligned}
& f_{t}(x)=\max (f, 0) \\
& f_{-}(x)=\min (f, 0)
\end{aligned}
$$

since $f(x)$ is measurable the desired result follows.
Note that

$$
f(x)=f_{+}(x)-f_{-}(x)
$$

trus an arbitrary measurable function can be written as the difference of two positive functions

## Definition Superior and Inferior Limits.

If $f_{1}, f_{2}, \ldots$ are measurable functions on $X$ define
$\sup _{i \geqslant 1} f_{i}(x)=\sup \left\{f_{i}(x) ; 1 \leqslant i<\infty\right\}$

$$
\inf _{c \geqslant 1} f_{i}(x)=\inf \left\{f_{i}(x): 1 \leqslant i<\infty\right\}
$$

For $a \in \mathbb{R}$

$$
\begin{aligned}
\{x ; & \left.\sup _{i}(x)>a\right\} \\
& =\bigcup_{i=1}^{\infty}\left\{x ; f_{i}(x)>a\right\} \in \mathcal{F}
\end{aligned}
$$

and

$$
\begin{aligned}
\{x ; & \left.\inf f_{i}(x) \geqslant a\right\} \\
& =\bigcap_{i=1}^{\infty}\left\{x ; f_{i}(x) \geqslant a\right\} \in \mathcal{F}
\end{aligned}
$$

since $f_{i} \in \mathcal{F} \forall i$.
Now if $f_{1}, f_{2}, \ldots$ is a sequence of functions and let

$$
g_{k}=\sup _{n \geqslant k} E_{n}
$$

note that

$$
g_{1} \geqslant g_{2} \geqslant g_{3} \geqslant \cdots
$$

since $g_{1}$ is the sup of all fi so as $k$ moreases so will sup.
It follows that

$$
\lim _{k \rightarrow \infty} g_{k}=\inf _{k>0} g_{k}
$$

This is a result of $g k$ being
a decreasing sequence. It follows that the superior limit is given by

$$
\limsup _{k \rightarrow \infty} f_{i}=\inf _{k>0} g_{k}
$$

similark the inferror limit is given by

$$
\begin{gathered}
\liminf _{k \rightarrow \infty} f_{i}=\sup _{k>0} h_{k} \\
h_{k}=\inf _{n \geqslant k} f_{n}
\end{gathered}
$$

Both the limits are measurable functions.

## Definition

If $f_{1}, f_{2}, f_{3}, \ldots$ are a sequence of measurable functions on $\bar{X}$. If the sequence of functions converges to a function $P$,
then $f$ is a measurable function.
The result follows by noting that

$$
\begin{aligned}
f=\lim _{n \rightarrow \infty} f_{n} & =\limsup _{n \rightarrow \infty} f_{n} \\
& =\liminf _{n \rightarrow \infty} f_{n}
\end{aligned}
$$

trus $f$ is a countable union and intersection of measurable functions.
Thus measurable functions can be constructed from limits of functions

Theorem
measurable functions can also be constructed by function composition.
If $f: X-\mathbb{R}$ is measurable
and $g$ is a continuous function on $\mathbb{R}$ then

$$
g \circ f=g(f(x))
$$

is a measurable function.

## Proof

For $a \in \mathbb{R}$ let

$$
\theta_{a}=\{t \in \mathbb{R} ; g(t)>a\}
$$

Then

$$
\begin{aligned}
& \{x \in \mathbb{Z} ; g \circ f(x)>a\} \\
& =\left\{x \in \mathbb{Z} ; f(x) \in \theta_{a}\right\}
\end{aligned}
$$

$\theta_{a}$ is a Borel set since $S$ is continuous, so

$$
\left\{x \in \bar{X} ; f(x) \in \theta_{a}\right\} \in \mathcal{F}
$$

## Example

If $f: \bar{X} \rightarrow \mathbb{R}$ is measurable then

$$
e^{i \lambda f}, e^{-f^{2} / 2}, \sin f|f|
$$

are measurable fundtions

This result can be extended to functions of muttiple variables.
If $f_{1}, f_{2}, \ldots, f_{n}$ are measurable flendtions and $C: \mathbb{R}^{n} \rightarrow \mathbb{R}$ is continuous then

$$
G\left(f_{1}, f_{2}, \ldots, f_{n}\right)
$$

is measurable.

Example
If $f_{c}: \bar{x} \rightarrow \mathbb{R}, i=1,2$ and since $S(x, y)=x+y$ or $x y$ it follows trat

## $f_{1}+f_{2}$ and $f_{1} f_{2}$

are measurable

## Lebesgue Integral

Let $(\bar{X}, \mathcal{F}, \mu)$ be a measure space and $s: X \rightarrow R$ be a measurable function. The function $s$ is a simple function if it takes on a Pinite number of values

## Example

let $E \in \mathcal{F}$ and define

$$
\mathbb{1}_{E}(x)=\left\{\begin{array}{lll}
1 & \text { if } & x \in E \\
0 & \text { if } & x \notin E
\end{array}\right.
$$

$\mathbb{1}_{E}(x)$ is called a charaderistic function or indection function of $E$.

In general if $s$ is a simple function taking on values $c_{1}, c_{2}, \ldots, c_{n}$, let

$$
E_{i}=S^{-1}\left(C_{i}\right)=\left\{x \in \bar{X}, S(x)=C_{i}\right\}
$$

where $c=1,2, \ldots, n$. It follows that

$$
S(x)=\sum_{i=1}^{n} c_{i} \mathbb{1}_{E_{i}}(x)
$$

clearly the $E_{i}$ will form a cover of I

A possible simple function is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-131.jpg?height=851&width=1190&top_left_y=848&top_left_x=189)
$1 \bar{X} 1$

## Definition

Let $s: X \rightarrow \mathbb{R}$ be a nonnegative simple function and let $E \in \mathcal{F}$. Let $c_{1}, c_{2}, \ldots, c_{n}$ be the distinct nonzero values of $s$ and let

$$
E_{i}=s^{-1}\left(c_{i}\right), 1 \leqslant i \leqslant n
$$

Define the integral of $s$ over $E$ with respect to $\mu$ as the sum

$$
I_{E}(s)=\sum_{i=1}^{n} c_{i} \mu\left(E \cap E_{i}\right)
$$

The value of $I_{E}(S)$ can be $+\infty$ because $\mu\left(E \cap E_{i}\right)$ can be $+\infty$.
The integral is illustrated in the following figure. The event, $E$, is indicated on the horizontal axis. The integral is illustrated by the highligt
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-133.jpg?height=830&width=1170&top_left_y=104&top_left_x=179)

$$
|\quad E \quad|
$$

$$
1
$$

## Theorem

Let $s_{i}: \mathbb{Z} \rightarrow \mathbb{R}, i=1,2$ be simple functions and let $E \in \mathcal{F}$.

1. linearity
a. $I_{E}\left(C S_{1}\right)=C I_{E}\left(S_{1}\right)$
b. $I_{E}\left(S_{1}+S_{2}\right)=I_{E}\left(S_{1}\right)+I_{E}\left(S_{2}\right)$
2. monotonicity

If $S_{1} \leqslant S_{2} \Rightarrow I_{E}\left(S_{1}\right) \leqslant I_{E}\left(S_{2}\right)$

Proof 1

$$
\begin{aligned}
I_{E}\left(C S_{1}\right) & =\sum_{i=1}^{n} C C_{i} \mu\left(E \cap E_{i}\right) \\
& =C \sum_{i=1}^{n} C_{i} \mu\left(E \cap E_{i}\right) \\
& =C I_{E}\left(S_{1}\right)
\end{aligned}
$$

To prove part $b$ let $c_{1}, c_{2}, \ldots, c_{m}$ be the distinct values of $s_{1}$ and $d_{1}, d_{2}, \ldots, d_{n}$ the distanct values of $S_{2}$. Let

$$
\begin{array}{ll}
E_{i}=s_{1}^{-1}\left(c_{i}\right), & 1 \leqslant i \leqslant m \\
F_{j}=s_{2}^{-1}\left(d_{i}\right), & 1 \leqslant i \leqslant n
\end{array}
$$

Now the $E_{i}$ 's are a mutually disjant cover of $\bar{X}$ and so do $F_{j}{ }^{\prime} s$
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-135.jpg?height=733&width=1039&top_left_y=84&top_left_x=259)
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-135.jpg?height=801&width=1039&top_left_y=894&top_left_x=257)

$$
\begin{aligned}
& \left|F_{1} \cap E_{1}\right| F_{1} \cap E_{2}\left|F_{2} \cap \varepsilon_{3}\right| F_{2} \cap E_{3}\left|E_{3} \cap E_{3}\right| F_{3} \cap E_{4} \mid \\
& \bar{X}
\end{aligned}
$$

The figures above illustrate the simple fundtions $s(x)$ and $s_{2}(x)$.
From the figure it is seen that since both the $E_{i}$ 's and $F_{j}$ 's are disjoint covers of $\bar{X}$ so $E_{i} \cap E_{j}$ for $1 \leqslant i \leqslant m$ and $1 \leqslant j \leqslant n$ is also a disjoint cover of $I$. It is also seen that $C_{i}+C_{j}$ is constant over $E_{i} \cap F_{j}$. It follows that

$$
\begin{aligned}
I_{E} & \left(S_{1}+S_{2}\right)=\sum_{i=1}^{m} \sum_{j=1}^{n}\left(C_{i}+d_{j}\right) \mu\left(E_{i} \cap F_{j} \cap E\right) \\
=\sum_{i=1}^{m} & \sum_{j=1}^{n} C_{i} \mu\left(E_{i} \cap F_{j} \cap E\right) \\
& +\sum_{i=1}^{m} \sum_{j=1}^{n} d_{j} \mu\left(E_{i} \cap F_{j} \cap E\right) \\
=\sum_{i=1}^{m} C_{i} \sum_{j=1}^{n} \mu\left(E_{i} \cap F_{j} \cap E\right) & +\sum_{j=1}^{n} d_{j} \sum_{i=1}^{n} \mu\left(E_{i} \cap F_{j} \cap E\right)
\end{aligned}
$$

$$
\begin{aligned}
=\sum_{i=1}^{n} & c_{i} \mu\left(\bigcup_{j=1}^{n} E_{i} \cap F_{j} \cap E\right) \\
& +\sum_{j=1}^{n} d_{j} \mu\left(\bigcup_{i=1}^{n} E_{i} \cap F_{j} \cap E\right)
\end{aligned}
$$

Now for the first term

$$
\begin{aligned}
\hat{\bigcup} & E_{i} \cap F_{j} \cap E=\left(E_{i} \cap F_{1} \cap E\right) \cup \\
& \left(E_{i} \cap F_{2} \cap E\right) \cup\left(E_{i} \cap F_{3} \cap E\right) \cup \\
& \cup\left(E_{i} \cap F_{n} \cap E\right) \\
= & E_{i} \cap\left\{\hat{\bigcup}_{j=1} F_{j}\right\} \cap E \\
= & E_{i} \cap F \cap E \\
= & E_{i} \cap E
\end{aligned}
$$

since $E_{i} \cap F=E_{i}$ because $E_{i} \subseteq F$ and $F$ is a cover of $X$. similarly,

$$
\bigcup_{c=1} E_{i} \cap F_{j} \cap E=F_{j} \cap E
$$

Bringing things together gives the desired result.

$$
\begin{aligned}
& I_{E}\left(S_{1}+S_{2}\right)=\sum_{i=1}^{m} \sum_{j=1}^{n}\left(C_{i}+d_{j}\right) \mu\left(E_{i} \cap F_{j} \cap E\right) \\
& =\sum_{i=1}^{m} C_{i} \mu\left(E_{i} \cap E\right)+\sum_{j=1}^{n} d_{j} \mu\left(F_{j} \cap F\right) \\
& =I_{E}\left(S_{1}\right)+I_{E}\left(S_{2}\right)
\end{aligned}
$$

Now for the last theorem, Monotonicity If $s_{1} \leq s_{2} \Rightarrow I_{E}\left(S_{1}\right) \leqslant I_{E}\left(S_{2}\right)$.

## Proof

Since $s_{2} \geqslant s_{1}$ it follows that $S_{2}-S_{1}$ is a nonegative simple function low

$$
S_{2}=S_{2}-S_{1}+S_{1}
$$

since $s_{2}, s_{1}$ and $s_{2}-s_{1}$ are nonnegative simple functions It follows that

$$
\begin{aligned}
& I_{E}\left(S_{2}\right)=I_{E}\left(S_{2}-S_{1}\right)+I_{E}\left(S_{1}\right) \\
& \Rightarrow I_{E}\left(S_{2}\right) \geqslant I_{E}\left(S_{1}\right)
\end{aligned}
$$

## Definition

Let $f$ be a nonnegative measurable function from I orto the nonnegative extended real numbers and let $E \in \mathcal{F}$. Then the integral of $f$ on $E$ with respect to $\mu$ is defined by
$\int_{E} f d \mu=\sup \left\{I_{E}(s) ; 0 \leqslant s \leqslant f, s\right.$ simple $\}$
This is saying there is a sequence of simple functions that converge to $f$ and in this limit the definition above is satisfied.
Theorem $I_{E}(s)=S_{E} s d \mu$ if $s$ is a non negative simple function.

## Proof

From the definition of the integral of $s$,

$$
\int_{E} s d \mu=\sup \left\{I_{E}(S) ; 0 \leqslant S \leqslant S\right\}
$$

It follows that

$$
I_{E}(s) \leq \int_{E} s d s
$$

since $0 \leqslant s \leqslant s$. To show equality it must also be shown that $I_{E}(s)>S_{E} s d s$. Let $s^{\prime}$ be a simple function satisfying $0 \leqslant \delta^{\prime} \leqslant s$ by montoniaty of $I_{E}(S)$ this inequality implies that

$$
I_{E}\left(S^{\prime}\right) \leqslant I_{E}(S)
$$

It follows that

$$
\begin{aligned}
\int_{E} s d \mu & =\sup \left\{I_{E}\left(s^{\prime}\right) ; 0 \leqslant s^{\prime} \leqslant s\right\} \\
& \leqslant I_{E}(s)
\end{aligned}
$$

Thus

$$
\int_{E} s d u=I_{E}(s)
$$

## Theorem

Let $f$ be a nonnegative measurable function on $\bar{X}$ with values in the nonnegative extended real numbers. There exists a sequence of nonnegative simple function satisfying

$$
0 \leqslant s_{1} \leqslant s_{2} \leqslant \cdots \leqslant f
$$

such that $S_{i} \rightarrow f$ pointwise. Moreover, if $P$ is bounded then $s_{i} \rightarrow f$ uniformly.

Before starting the proof pointuse and uniform convergence are reviewed. First consider pointwise convergence for the sequence of flanctions $\left\{f_{n}\right\}$. The sequence
converges pointwise if for a given $x$,

$$
\lim _{n \rightarrow \infty} f_{n}(x)=f(x)
$$

This means that for a given $x$ and $\varepsilon$ there exists an $N$ such that $\forall n, n \geqslant N$

$$
\left|f(x)-f_{n}(x)\right|<\varepsilon
$$

A sequence converges uniformly If $\forall x$ given $\varepsilon>0$ there exists an $N$ such that $\forall n$ satisfing $n>N$

$$
\left|f(x)-f_{n}(x)\right|<\varepsilon \quad \forall x
$$

## Proof

First define $s_{n}$. Consider the interval $[0, n)$ on $\mathbb{R}$. Diride this interval into $n 2^{n}$ subintervals of length $2^{-n}$, namely
$I_{i}=\left\{t \in \mathbb{R} ; \frac{i-1}{2^{n}} \leqslant t \leqslant \frac{i}{2^{n}}\right\} \quad 1 \leqslant i \leqslant n 2^{n}$
Consider the leftmost point of the interval, $2^{-n}(i-1)$. If the simple function $s_{n}$ is assumed to have this value over the interval $I_{n}$. It follows that for the measure space $(I, \mathcal{F}, \mu)$ the disjoint covering of $I$ generated by the simple function in is given by

$$
\begin{aligned}
E_{i} & =\sin ^{-1}\left[2^{-n}(c-1)\right] \\
& =\left\{x \in \mathbb{Z} ; S_{n}(x)=2^{-n}(i-1)\right\}
\end{aligned}
$$

where $1 \leqslant i \leqslant n 2^{n}$. Also, for each $E_{i}$

$$
\frac{i-1}{2^{n}} \leqslant f<\frac{i}{2^{n}}, \quad S_{n}(x)=\frac{i-1}{2^{n}}
$$

It follows that

$$
s_{n}(x)<f(x)
$$

for $x \in E_{i}, 1 \leqslant i \leqslant n 2^{n}$.
Next consider the interval defining the remainder of nonnegative $\mathbb{R},[n, \infty]$. Following the lead taken previously of assuming the leftmost value of the interval is the calue of the simple function over the interal it follows that the covering for the remainder of I be defined by

$$
F_{n}=\left\{x \in \bar{X} ; S_{n}(x)=n\right\}
$$

It follows that for $x \in F_{n}$

$$
n \leqslant f(x) \quad s_{n}(x)=n
$$

and thus $\forall x \in \mathbb{X} \quad s_{n} \leqslant f(x)$.

Bring things together gives the following expression for $s_{n}(x)$,
$\operatorname{sn}(x)=\sum_{i=1}^{n 2^{n}}\left(\frac{i-1}{2^{n}}\right) \underline{1}_{E_{i}}(x)+n \underline{1}_{F_{n}}(x)$
To wrderstand this approximation consider the following figure. The first shows the simple function approximation used here and the
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-145.jpg?height=1053&width=1256&top_left_y=920&top_left_x=187)
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-146.jpg?height=1097&width=1275&top_left_y=171&top_left_x=130)
lower plot shows the appoximation of $f(x)$ used in the Riemann integral. The Riemann integral partions $\bar{X}$, the domain of $f(x)$, into columns which more dosely approximates $f(x)$ as the number of partitions increases and converging to
$f(x)$ as $n \rightarrow \infty$. Also, the Riemann approximation assumes $\bar{X} \leq \mathbb{R}$. In constrast the simple function approximation partions the domain of values of $f(x)$, which are elements of $R$ and does not assume that I is real. It should be noted that if $f(x)$ does not lie within a partion $E_{i}=\varnothing$ so it does not contribuite to $f(x)$. Also, it is not assumed trat $I$ is real in the simple function approximation. This allows the use of any measureable space.
Now back the showing that

$$
\lim _{n \rightarrow \infty} s_{n}=f(x) .
$$

Now from the definition of $s_{n}(x)$ it follows that

$$
s_{n} \leqslant s_{n+1}
$$

To prove this consider the following figure which shows a comparison of $s_{n}$ and $s_{n+1}$ where
![](https://cdn.mathpix.com/cropped/2025_11_16_28d50f16ede1b3fd3e97g-148.jpg?height=1164&width=1424&top_left_y=735&top_left_x=64)

$$
\left|F_{1}\right| F_{2}\left|F_{3}\right| F_{4}\left|F_{5}\right|
$$

The change in area under the curve between the approximations is colored red. It is seen that the $s_{n+1}$ approximation has a spacing between coefficients of $2^{-(n+1)}$ and $s_{n}$ a spacing of $2^{-n}$. Thus the $s_{n+1}$ spacing is \& the $s_{n}$ spacing. From inspection of the plot it is seen that each of the $s_{n}$ coefficents is equal to the odd $s_{n+1}$ coefficients and less than the even coefficiens. It follows that,

$$
c_{i}=\frac{i-1}{2^{n}}
$$

so

$$
d_{2 i-1}=\frac{2 i-1-1}{2^{n+1}}=\frac{i-1}{2}=c_{i}
$$

and

$$
d_{\partial i}=\frac{2 i-1}{\partial^{n+1}}
$$

but

$$
\begin{aligned}
d_{\partial i}-c_{c} & =\frac{\partial i-1}{\partial^{n+1}}-\frac{i-1}{\partial^{n}} \\
& =\frac{1}{\partial^{n+1}}[\partial \hat{i}-1-\tilde{2}(i-1)] \\
& =\frac{1}{\partial^{n+1}}(\partial-1) \\
& =\frac{1}{\partial^{n+1}}>0
\end{aligned}
$$

thus

$$
c_{i}<d_{2 i}
$$

and

$$
\begin{aligned}
d_{2 i}-C_{i+1} & =\frac{2 i-1}{2^{n+1}}-\frac{(i+1)-1}{2^{n}} \\
& =\frac{1}{2^{n+1}}[2 i-1-2(i)] \\
& =-\frac{1}{2^{n+1}}<0
\end{aligned}
$$

thus

$$
d_{\partial i}<C_{i+1}
$$

so

$$
C_{i}<d_{2 i}<C_{i+1}
$$

It follows that for every $i$

$$
c_{i} \leq d_{2 i}
$$

since $c_{c}>0$ and $d_{j}>0$ for every $i$ and $j$ the desired result is obtained,

$$
S_{n} \leqslant S_{n+1}
$$

Now a more rigorus proof can be constructed in the following manner. Let,

$$
I=\left[\frac{i-1}{2^{n}}, \frac{i}{2^{n}}\right)
$$

which is an arbitrary $s_{n}$ coefficient terval and

$$
\begin{aligned}
& I^{\prime}=\left[\frac{2 i-2}{\partial^{n+1}}, \frac{2 i-1}{\partial^{n+1}}\right) \\
& I^{\prime \prime}=\left[\frac{2 i-1}{\partial^{n+1}}, \frac{2 i}{\partial^{n+1}}\right)
\end{aligned}
$$

where $I^{\prime}$ is an arbitrary odd interval for $S_{n+1}$ and I an arbitrary even enterval clearly

$$
I^{\prime} \cap I^{\prime \prime}=\varnothing
$$

and

$$
\begin{aligned}
I^{\prime} \cup I^{\prime \prime} & =\left[\frac{2 i-2}{2^{n+1}}, \frac{2 i-1}{2^{n+1}}\right) \cup\left[\frac{2 i-1}{2^{n+1}}, \frac{2 i}{\partial^{n+1}}\right) \\
& =\left[\frac{i-1}{\partial^{n}}, \frac{\partial i-1}{\partial^{n+1}}\right) \cup\left[\frac{2 i-1}{\partial^{n+1}}, \frac{i}{\partial^{n}}\right) \\
& =\left[\frac{i-1}{\partial^{n}}, \frac{i}{2^{n}}\right) \\
& =I
\end{aligned}
$$

Thus

$$
I=I^{\prime} \cup I^{\prime \prime}
$$

which is saying that the intervals on which the sn coefficients are defined is the union of the odd and even intervals at the same index $i$ of
$S_{n+1}$ coefficients.
Let

$$
\begin{aligned}
& E=\left\{x \in \mathbb{X} ; s_{n}(x)=\frac{i-1}{2 n}\right\} \\
& F^{\prime}=\left\{x \in \mathbb{X} ; s_{n+1}(x)=\frac{i-1}{2 n}\right\} \\
& F^{\prime \prime}=\left\{x \in \mathbb{X} ; s_{n+1}(x)=\frac{2 i-1}{2 n+1}\right\}
\end{aligned}
$$

since $I=I^{\prime} \cup I^{\prime \prime}$ it follows that

$$
E=F^{\prime} \cup F^{\prime \prime}
$$

and since

$$
\frac{i-1}{2^{n}}<2 \frac{i-1}{2^{n+1}}
$$

It follows that

$$
s_{n} \leqslant s_{n+1} \text { for } x \in E
$$

Similarly for the conbounded interval where $s_{n}=n \leqslant f=0 f \in[n, \infty)$ and where

$$
\begin{gathered}
S_{n+1}=n+1<f \Rightarrow f \in[n+1, \infty) \text {. Now } \\
{[n, \infty)=[n, n+1) \cup[n+1, \infty)}
\end{gathered}
$$

The number of terms in $s_{n+1}$ is given by

$$
(n+1) 2^{n+1}=2 n 2^{n}+2^{n+1}
$$

It follows that the final $a^{n+1}$ terms lie on the interval $[n, n+1)$ the lower bound on this interval is given by

$$
\left(\frac{2 n \partial^{n}}{\partial^{n+1}}\right)=n
$$

and the upperbound is

$$
\frac{(n+1) 2^{n+1}}{2^{n+1}}=n+1
$$

If follows that for $f \in[n, \infty)$

$$
S_{n} \leqslant S_{n+1}
$$

Now that it is settled that
$s_{n} \leqslant s_{n+1}$. It can be shown that $s_{n} \rightarrow f$ as $n \rightarrow \infty$.

The proof deals with three cases. For the first $f(x)=\infty$ Recall that

$$
S_{n}(x)=\sum_{i=1}^{n 2^{n}} \frac{i-1}{2^{n}} \mathbb{1}_{E_{n}}(x)+n \mathbb{1}_{F_{n}}(x)
$$

since $f(x)=\infty$ it follows that $x \in F_{n} \forall x$ thus

$$
s_{n}(x)=n
$$

It follows that

$$
\lim _{n \rightarrow \infty} S_{n}(x)=\lim _{n \rightarrow \infty} n=\infty
$$

For case 2 it is assumed that $f(x)$ is finite. Since $f(x)$ is finite for every value of $x \quad f(x)$ has a finite value. It follows that given an $x$ there
exists an $n_{0}$ such that

$$
f(x)<n_{0}
$$

The assumption that $f(x)$ is finite implies that for all $x f(x)$ lies on some interval. So for all $n>n_{0} f(x)$ lies on one of the intervals

$$
\frac{i-1}{2^{n}} \leqslant f(x) \leqslant \frac{i}{2^{n}}
$$

where

$$
S_{n}(x)=\frac{i-1}{2^{n}}
$$

so using

$$
f(x) \leqslant \frac{i}{2^{n}}
$$

gives

$$
\left|S_{n}(x)-f(x)\right|<\left|\frac{i-1}{2 n}-\frac{i}{2 n}\right|<\frac{1}{2^{n}}
$$

it follows that for the given $x$ that

$$
\lim _{n \rightarrow \infty}\left|s_{n}(x)-f(x)\right|<\lim _{n \rightarrow \infty} \frac{1}{a^{n}}=0
$$

Thus

$$
\lim _{n \rightarrow \infty} s_{n}(x)=f(x)
$$

This proves pointwise convergence For the final case assume that $f(x)$ is bounded. If $f(x)$ is bounded then for every $x \in \bar{X} \quad f(x)<n_{0}$ for some $n_{0}$ The previous argument the implies that $s_{n} \rightarrow f(x)$ as $n \rightarrow \infty$ uniformly.

## Properties of the Lebesgue Integral

Let $E, F \in \mathcal{F}$ and let $f$ and $g$ be nonnegative measurable function. Then the following properties hod The following properties will be stated without proof since they are intuitive.

1. (montonicity) if $f \leqslant g$ then

$$
\int_{E} f d u \leqslant \int_{E} g d u
$$

a. (subset Rule) If $E C F$

$$
\int_{E} f d \mu \leqslant \int_{F} f d \mu
$$

3. If $\mu(E)=0$

$$
\int_{E} f d u=0 .
$$

4. (Linearity)

$$
\int_{E}(f+g) d u=\int_{E} f d u+\int_{E} g d u
$$

Using these properties the following theorem can be proven
Chebysheo Inequality
Let $f$ be a nonnegative measurable function. For $E \in \mathcal{F}$ and $c>0$, let

$$
E_{c}=\{x \in E ; f(x) \geqslant c\}
$$

Then

$$
\mu\left(E_{c}\right) \leq \frac{1}{c} \int_{E} f d \mu
$$

Proof
since $f(x) \geqslant c$ from montonicity it follows that

$$
\int_{E_{c}} c d \mu \leqslant \int_{E_{c}} f d \mu
$$

low

$$
\int_{E_{c}} c d \mu=I_{E_{c}}(c)=c \mu\left(E_{c}\right)
$$

so

$$
c \mu\left(E_{c}\right) \leq \int_{E_{c}} f d \mu
$$

but from the definition of $E_{c}$ it follows that

$$
E_{c} \subseteq E
$$

and the desired result follows from the subset rule

$$
\begin{aligned}
c \mu\left(E_{c}\right) & \leqslant \int_{E_{c}} f d u \\
& \leqslant \int_{E} f d u \\
\Rightarrow \mu\left(E_{c}\right) \leqslant & \frac{1}{c} \int_{E} f d u
\end{aligned}
$$

Definition Almost Everywhere
If a property holds on a set $E \in \mathcal{F}$ except for a subset of measure zero, it is said to hold almost everywhere on $E$. It is abbriviated as a.e.
Theorem If $f$ is a nonegative measurable function with

$$
\int_{E} f d u<\infty
$$

then $\{x \in E ; f(x)=\infty\}$ has zero measure implying that
$\int_{E} f d \mu<\infty \Rightarrow f(x)<\infty$ a.e. on $E$
Prool
Let $A_{n}=\{x \in E ; f(x) \geqslant n\}$ and let $A=\{x \in E ; f(x)=\infty\}$.
using the chebyshev inequality

$$
\mu\left(A_{n}\right) \leq \frac{1}{n} \int_{E} f d \mu
$$

But $A \subset A_{n}$ so

$$
\mu(A) \leqslant \mu\left(A_{n}\right) \leqslant \frac{1}{n} \int_{E} f d \mu
$$

and it is assumed that

$$
\int_{E} f d \mu<\infty
$$

and $n$ is arbitrary so can be arbitrarly large it folbows that

$$
\mu(A)=0
$$

Theorem Let $f$ be a nonegative measurable function and let $E \in \mathcal{F}$. If

$$
\int_{E} f d \mu=0
$$

then $f=0$ ae. on $E$
Proof
Let $A=\{x \in E ; f(x) \neq 0\}$ and $A_{n}=\{x \in E ; f(x) \geq 1 / n\}$.

To prove the theorem it must be shown that the set on which $f(x) \neq 0$, which is defined by $A$, has measure zero
Now

$$
A=\widehat{\bigcup}_{n=1} A_{n}
$$

by subadditivity

$$
\mu(A) \leq \sum_{n=1}^{\infty} \mu\left(A_{n}\right)
$$

To prove that $\mu(A)=0$ it is sufficient to show that $\mu\left(A_{n}\right)=0$ Using the chebysheu inequality
gives

$$
\begin{aligned}
& \mu(A) \leqslant \mu\left(A_{n}\right) \leqslant n \int_{E} f d u=0 \\
& \Rightarrow \mu(A)=0
\end{aligned}
$$

Thus

$$
\int_{E} f d u=0 \Rightarrow f(x)=0 \text { a.e. }
$$

Theorem let $f$ be a nonnegation measurable function on $\bar{X}$.
Let $A_{1}, A_{2}, \ldots$ be a sequence of pair wrse disjoint elements of年. Let

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

where $A_{i} \cap A_{j}=\phi$. Then

$$
\int_{A} f d u=\sum_{i=1}^{\infty} \int_{A_{i}} f d u
$$

Proof
First the theorem will be proven for $f(x)=\mathbb{1}_{E}(x)$. Now

$$
\begin{aligned}
& \int_{A} \mathbb{1}_{E} d u=u(E \cap A) \\
& \int_{A_{i}} \mathbb{1}_{E} d u=u\left(E \cap A_{i}\right)
\end{aligned}
$$

By countable additivity it
follows that

$$
\mu(E \cap A)=\sum_{i=1}^{\infty} \mu\left(E \cap A_{i}\right)
$$

it follows that

$$
\begin{aligned}
& \int_{A} \mathbb{1}_{E} d \mu=\mu(E \cap A) \\
& =\sum_{i=1}^{\infty} \mu\left(E \cap A_{i}\right) \\
& =\sum_{i=1}^{\infty} \int_{A_{i}} \mathbb{1}_{E} d \mu
\end{aligned}
$$

Consider the simple function

$$
S(x)=\sum_{i=1}^{\infty} c_{i} \mathbb{1}_{E_{i}}(x)
$$

so

$$
\begin{aligned}
& I_{A}(s)=\sum_{i=1}^{\infty} c_{i} \mu\left(A \cap E_{i}\right) \\
& I_{A_{n}}(s)=\sum_{i=1}^{\infty} c_{i} \mu\left(A_{n} \cap E_{i}\right)
\end{aligned}
$$

Now

$$
\begin{aligned}
I_{A}(s) & =\sum_{i=1}^{\infty} c_{i} \mu\left(U_{n=1}^{\infty} A_{n} \cap E_{i}\right) \\
& =\sum_{i=1}^{\infty} c_{i} \mu\left[U_{n=1}^{\infty}\left(A_{n} \cap E_{i}\right)\right] \\
& =\sum_{i=1}^{\infty} c_{i} \sum_{n=1}^{\infty} \mu\left(A_{n} \cap E_{i}\right) \\
& =\sum_{n=1}^{\infty} \sum_{i=1}^{\infty} c_{i} \mu\left(A_{n} \cap E_{i}\right) \\
& =\sum_{n=1}^{\infty} I_{A_{n}}(s) \\
\Rightarrow \quad \int s d \mu & =\sum_{n=1}^{\infty} \int S_{A_{i}} s d \mu
\end{aligned}
$$

Thus the theorem is true for any simple function.
To exterd the proof to any nonnegative measureable function recall that for a simple function satisfying $s \leqslant f$ that from monotonicity

$$
\int_{A} f d \mu \geqslant \int_{A} s d \mu=I_{A}(s)
$$

Now choose an $\varepsilon>0$ such shat

$$
\int_{A} f d \mu \leqslant I_{A}(s)+\varepsilon
$$

Now, it was just shown that

$$
I_{A}(s)=\sum_{n=1}^{\infty} I_{A_{n}}(s)
$$

but since $s(x) \leqslant f(x)$ t follows that

$$
I_{A_{n}}(s) \leqslant \int_{A_{n}} f d u
$$

Thus

$$
I_{A}(S) \leqslant \sum_{n=1}^{\infty} \int_{A_{n}} f d \mu
$$

substituting into the equation
above gives

$$
\int_{A} f d u \leqslant \sum_{n=1}^{\infty} \int_{A_{n}} f d u+\varepsilon
$$

since $\varepsilon$ is arbitrary it follows that,

$$
\int_{A} f d \mu \leqslant \sum_{n=1}^{\infty} \int_{A_{n}} f d \mu
$$

To prove the opposite inequality consider two disjoint sets $A_{1}, A_{2} \in \mathcal{F}$. Let $s_{1}$ and $s_{2}$ be simple functions with $0 \leqslant s_{i} \leqslant f$ where $i=1,2$, that satisfy

$$
\int_{\Delta_{i}} s_{i} d u \geqslant \int_{A_{i}} f d u-\frac{\varepsilon}{2}
$$

let $s=\max \left(s_{1}, s_{2}\right)$ so $s_{1} \leqslant s$ and $s_{2} \leqslant s$ it follows that

$$
\int_{A_{i}} s d u \geqslant \int_{A_{i}} f d u-\frac{\varepsilon}{2}
$$

## summing gives

$\int_{A_{1}} s d \mu+\int_{A_{2}} s d \mu \geqslant \int_{A_{1}} f d \mu+\int_{A_{2}} f d \mu-\frac{\varepsilon}{2}$
Now for simple functions

$$
\begin{aligned}
& \int_{A_{1}} s d \mu+\int_{A_{2}} s d \mu \\
= & \int_{A_{1} \cup A_{2}} s d \mu=\int_{A} s d \mu
\end{aligned}
$$

since $s \leqslant f$ it follows that

$$
\int_{A} f d u \geqslant \int_{A} s d u
$$

so since $\varepsilon$ is arbitrary it follows that

$$
\int_{A} f d u \geqslant \int_{A_{1}} f d u+\int_{A_{2}} f d u
$$

This proves the inequality for two disjoint sets.

An induction argument an be used to complete proof,

$$
\int_{A} f d u \geqslant \sum_{n=1}^{\infty} \int_{A_{n}} f d u
$$

and the desired result is obtarned

$$
\int_{A} f d u=\sum_{n=1}^{\infty} \int_{A_{n}} f d u
$$

## Application

This theorem can be used to construct new measures from the lebesgue measure.
for example the laussian measure is defined by

$$
\mu_{C}(A)=\frac{1}{\sqrt{2 \pi}} \int_{A} e^{-x^{2} / 2} d \mu_{z}
$$

In light of the previous theorem if

$$
A=\bigcup_{n=1}^{\infty} A_{n}
$$

where $A_{n} \cap A_{n}=\phi$ for $n \neq m$. Then

$$
\mu_{\epsilon}(A)=\sum_{n=1}^{\infty} \mu_{\epsilon}\left(A_{n}\right)
$$

and since

$$
\frac{1}{2 \pi} \int_{A} e^{-x^{2} / 2} d u_{z}=1
$$

$\mu_{6}(A)$ satisfies the properties of a measure

## Theorem

suppose $f$ and $g$ are nonnegative measurable functions and $E \in \mathcal{F}$. Then if $f=s$ a.e on $E$

$$
\int_{E} f d u=\int_{E} g d u
$$

## Proof

Let $A_{1}=\{x \in E ; f(x)=g(x)\}$ and $A_{2}=\{x \in E ; f(x) \neq g(x)\}$ clearly

$$
A_{1} \cap A_{2} \neq \varnothing
$$

Moreover it is assumed that $f=g$ a.e on $E$ so

$$
\mu\left(A_{2}\right)=0
$$

It follows that

$$
u\left(A_{2}\right)=\int_{A_{2}} f d u=\int_{A_{2}} g d u=0
$$

and since on $A_{1} f(x)=g(x)$

$$
\int_{A_{1}} f d u=\int_{A_{1}} g d u
$$

It follows that

$$
\int_{E} f d \mu=\int_{A_{1}} f d u+\int_{A_{2}} f d u
$$

$$
\begin{aligned}
& =\int_{A_{1}} g d u+\int_{A_{2}} g d u \\
& =\int_{E} g d u
\end{aligned}
$$

which is the desired result

Lebesgue Integral Convergence Theorems

Evaluating Lebesgue Integrals has not really been discussed. In this section theorems useful in evaluation of integrals will be discussed.

Montone Convergence Theorem
Let $f_{1}, f_{2}, f_{3}, \ldots$ be a sequence of measureable functions which converges to a function $f$,

$$
f=\lim _{n \rightarrow \infty} f_{n}
$$

The Monotone Convergence Theorem states that

$$
\int_{E} f d \mu=\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

where $E \in \mathcal{F}$.

Before proving this theorem the following lemma is needed.

## Lemma

Let $f$ be a nonnegative measurable function on $\bar{X}$ and let $E_{1}, E_{2}, E_{3}, \ldots$ be a sequence of sets in $\mathfrak{F}$ satisfying $E_{1} \subset E_{2} \subset E_{3} \subset \cdots$. Let

$$
E=\bigcup_{C=1}^{0} E_{i}
$$

then

$$
\int_{E} f d u=\lim _{c \rightarrow \Delta} \int_{E_{i}} f d u
$$

## Proof

Let

$$
\begin{aligned}
& A_{1}=E_{1} \\
& A_{2}=E_{2}-E_{1} \\
& A_{3}=E_{3}-E_{2}
\end{aligned}
$$

Since $E_{1} \subset E_{2} \subset E_{3} c \cdots$, The $A_{i}$ 's
are pairwse disjoint and

$$
\bigcup_{i=1}^{\infty} A_{i}=E \quad \bigcup_{i=1}^{n} A_{i}=E_{n}
$$

Since the $A_{i}$ are mutually disjoint contable additivity of the lesbesgue integral it follows that

$$
\begin{aligned}
\int_{E} f d \mu & =\sum_{i=1}^{\infty} \int_{A_{i}} f d \mu \\
& =\lim _{n \rightarrow \infty} \sum_{i=1}^{n} \int_{A_{i}} f d \mu
\end{aligned}
$$

but

$$
\bigcup_{i=1} A_{i}=E_{n}
$$

so a second application of countable additivity gives

$$
\sum_{i=1}^{n} \int_{A_{i}} f d \mu=\int_{E_{n}} f d \mu
$$

and the desired result is
obtained,

$$
\int_{E} f d u=\lim _{n \rightarrow \infty} \int_{E_{n}} f d u
$$

Using this result the mondone convergence.

## Proof

It has been assumed that

$$
0 \leqslant f_{1} \leqslant f_{2} \leqslant \cdots \leqslant f=\lim _{n \rightarrow \infty} f_{n}
$$

using the montonicity of the lesbesgue integral it follows that

$$
0 \leq \int_{E} f_{1} d u \leq \int_{E} f_{2} d u \leq \cdots \leq \int_{E} f d u
$$

It follows that

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

exists and must be less than or equal to $\int_{E} f d \mu$. So

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d u \leqslant \int_{E} f d u
$$

Let

$$
a=\lim _{n \rightarrow \infty} \int_{E} f_{n} d u
$$

since montonicity of the Lesbesgue integral implies

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d u \leqslant \int_{E} f d u
$$

It must be shown that

$$
a \geqslant \int_{E} f d u
$$

Let $s$ be any simple function satisfying

$$
0 \leqslant s \leqslant f
$$

Let $C \in \mathbb{R}$ with $0<c<1$ and

$$
E_{n}=\left\{x \in E ; f_{n}(x) \geqslant c s(x)\right\}
$$

Notice that it follows that

$$
f_{1} \leqslant f_{2} \leqslant f_{3} \leqslant \cdots \leqslant f
$$

implies that if $x \in E_{n}$ then

$$
f_{n}(x) \geqslant \operatorname{cs}(x)
$$

but

$$
f_{n+1}(x) \geqslant f_{n}(x)
$$

it follows that $x \in E_{n+1}$ thus

$$
E_{n} \subset E_{n+1}
$$

and

$$
E_{1} \subset E_{2} \subset E_{3} C \cdots
$$

So $E_{n}$ is an increasing sequence.
Also, consider

$$
E=\bigcup_{n=1}^{\infty} E_{n}
$$

first assume $s(x)=0$. Then $x \in E_{n}$ for every $n$, similarly if $x \in E$ with $s(x)>0$, then because $c<1$ it follows,
that

$$
f(x) \geqslant s(x)>c s(x)
$$

since

$$
0 \leqslant f_{1} \leqslant f_{2} \leqslant \cdots \leqslant f
$$

There is some $n$ such that

$$
f_{n}(x) \geqslant c s(x)
$$

this implies that $x \in E_{n}$ so

$$
x \in \bigcup_{i=1}^{\infty} E_{n}
$$

Now since

$$
\begin{aligned}
& 0 \leqslant f_{1} \leqslant f_{2} \leqslant \cdots \leqslant f \\
\Rightarrow \quad & f_{n} \rightarrow f \text { as } n \rightarrow \infty
\end{aligned}
$$

It follows that

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d u \geqslant \int_{E} f_{n} d u
$$

further since $E_{n} \subset E$ it follows that

$$
\int_{E} f_{n} d \mu \geqslant \int_{E_{n}} f_{n} d \mu
$$

From the defanition of $E_{n}$

$$
E_{n}=\left\{x \in E ; f_{n}(x) \geqslant c s(x)\right\}
$$

it follows that

$$
\int_{E_{n}} f_{n} d u \geqslant \int_{E_{n}} \operatorname{csd} u
$$

Since $f_{n}(x) \geqslant c s(x)$ on $x \in E_{n}$ bringing things together

$$
a=\lim _{n \rightarrow \infty} \int_{E} f_{n} d u \geqslant \int_{E_{n}} \operatorname{csd} u
$$

low stepping back a bit

$$
a=\lim _{n \rightarrow \infty} \int_{E} f_{n} d u \geqslant \int_{E} f_{n} d u
$$

using the lemma

$$
\int_{E} f_{n} d u=\lim _{n \rightarrow \infty} \int_{E_{n}} f d u
$$

where $E_{n} \subset E_{n+1}, E=\bigcup_{n=1}^{\infty} E_{n}$, gives

$$
\begin{aligned}
a= & \lim _{n \rightarrow \infty} \int_{E} f_{n} d u \geqslant \int_{E} f_{n} d u \\
& =\lim _{n \rightarrow \infty} \int_{E_{n}} f_{n} d u
\end{aligned}
$$

but from the definition of $E_{n}$ it follows that on $E_{n}$

$$
f_{n}(x) \geqslant \csc (x)
$$

Thus

$$
\begin{aligned}
a & \geqslant \lim _{n \rightarrow \infty} \int_{E_{n}} c s d u \\
& =\int_{E} c s d u \\
& =c \int_{E} s d u
\end{aligned}
$$

This inequality is true for all values of $C$ since $0 \leqslant C \leqslant 1$ the maximum value of the integral is given by

$$
a \geqslant \int_{E} s d u
$$

also $0 \leqslant s \leqslant f$ taking supremum gives

$$
a \geqslant \int_{E} f d u
$$

Thus, since provously it was shown

$$
a=\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu \leqslant \int_{E} f d \mu
$$

it follows that

$$
\lim _{n \rightarrow \infty} \int_{E} f_{n} d u=\int_{E} f d u
$$

The monotone convergence theorem combined with the previous theorem which showed that the simple function defined by,

$$
S_{n}(x)=\sum_{i=1}^{n 2^{n}}\left(\frac{i-1}{2^{n}}\right) \mathbb{1}_{E_{i}}(x)+n \mathbb{1}_{E_{n}}(x)
$$

where

$$
\begin{aligned}
E_{i} & =S_{n}^{-1}\left[2^{-n}(c-1)\right] \\
& =\left\{x \in \mathbb{X} ; S_{n}(x)=2^{-n}(i-1)\right\}
\end{aligned}
$$

for $x \in E_{i}$

$$
\frac{i-1}{2^{n}} \leqslant f(x)<\frac{i}{2^{n}}, \quad S_{n}(x)=\frac{i-1}{2^{n}}
$$

and satisfies

$$
S_{1} \leqslant S_{2} \leqslant S_{3} \leqslant \cdots \leqslant f
$$

converges to $f(x)$.

$$
\lim _{n \rightarrow \infty} s_{n}=f(x)
$$

It then follows from the monotone convergence theorem

$$
\lim _{n \rightarrow \infty} \int_{E} S_{n} d \mu=\int_{E} f d \mu
$$

What this is seying is that the integral of a nonnegative measurable function $f(x)$ over the set $E$ is the limit of the sequence of simple functions defined by $s_{n}(x)$ above.
This result is used in proofs by noting that

$$
\int_{E} S_{n} d \mu=I_{E}\left(S_{n}\right)=\sum_{i=1}^{n \partial^{n}} C_{i} \mu\left(E \cap E_{i}\right)
$$

where

$$
c_{i}=\frac{i-1}{2^{n}}
$$

To illustrate the method a couple of theorems will be proven using it.

Theorem Let $f$ and $g$ be nomegative measurable functions and let $c>0$ be any real number. Then for $E \in \mathcal{F}$

1. $\int_{E} c f d \mu=c \int_{E} f d \mu$
2. $\int_{E}(f+g) d u=\int_{E} f d u+\int_{E} g d u$

Proof
For the first theorem define a sequence of simple function functions

$$
0 \leqslant s_{1} \leqslant s_{2} \leqslant s_{3} \leqslant \cdots \leqslant f
$$

From the monotone convergence theorem

$$
\lim _{n \rightarrow \infty} \int_{E} c S_{n} d \mu=\int_{E} c f d \mu
$$

Now

$$
\begin{aligned}
& \int_{E} c s_{n} d \mu=I_{E}\left(c s_{n}\right) \\
= & \sum_{i=1}^{n 2 n} c c_{i} \mu\left(E \cap E_{i}\right) \\
= & c \sum_{i=1}^{n 2 n} c_{i} \mu\left(E \cap E_{i}\right) \\
= & c I_{E}\left(s_{n}\right) \\
= & c \int_{E} s_{n} d \mu
\end{aligned}
$$

It follows that

$$
\int_{E} c f d u=\lim _{n \rightarrow \infty} \int_{E} c s_{n} d u
$$

$$
\begin{aligned}
& =\lim _{n \rightarrow \infty} C \int_{E} S_{n} d \mu \\
& =c\left\{\lim _{n \rightarrow \infty} \int_{E} S_{n} d \mu\right\} \\
& =c \int_{E} f d \mu
\end{aligned}
$$

Thus

$$
\int_{E} c f d \mu=c \int_{E} f d \mu
$$

A similar argument can be used to prove the second theorem

$$
\int_{E}(f+g) d \mu=\int_{E} f d \mu+\int_{E} g d \mu
$$

This theorem can be generalized to arbitrary sums

$$
\int_{E}\left(\sum_{n=1}^{\infty} f_{n}\right) d u=\sum_{n=1}^{\infty} \int_{E} f_{n} d u
$$

If $f$ be an arbitrary measurable function from $I$ to the exterded real numbers, $f: \mathbb{Z} \rightarrow \mathbb{R} \cup\{-\infty, \Delta\}$. Recall that

$$
\begin{aligned}
& f_{+}=\max (f, 0) \\
& f_{-}=\min (f, 0)
\end{aligned}
$$

where

$$
f=f_{t}+f_{-}
$$

Theorem The following two conditions are equivalent.

1. $\int_{E}|f| d \mu<\Delta$
2. $\int_{E} f_{+} d u<\infty$ and $\int_{E} f_{-} d u<\infty$

Proof
Notice that,

$$
|f|=f_{+}+f_{-}
$$

Now

$$
\begin{aligned}
\int_{E}|f| d \mu & =\int_{E}\left(f_{+}+f_{1}\right) d \mu \\
& =\int_{E} f_{+} d \mu+\int_{E} f \cdot d \mu
\end{aligned}
$$

The desired result follows
$\int_{E} f_{1} d u<\infty$ and $\int_{E} f_{-} d u<\infty$
if and only if

$$
\int_{\infty} i f l d u<\infty
$$

Defonition
A measurable function $f$ is integrable over $E$ if ether of the equivalent conditions proven in the previous theorem hold.

If this is the case then it is written that $f \in \mathcal{L}(\mu, E)$ or $f \in \mathcal{L}(\mu)$ on $E$. If $E=\bar{x}$ it is written that $f \in \mathcal{L}(\mu)$. For $f \in \mathscr{L}(\mu, E)$ define

$$
\int_{E} f d u=\int_{E} f_{+} d u-\int_{E} f d u
$$

Thus any integrable function can be writen as a linear combination of nonnegative measurable functions.

## Theorem

(Linearity) Let $f, g \in \mathcal{L}(\mu, E)$ and $c \in \mathbb{R}$ Then

1. $c f \in \alpha(\mu, E)$ and $\int_{E} c f d \mu=c \int_{E} f d \mu$
2. $f+g \in \mathcal{Z}(\mu, E)$

$$
\int_{E}(f+g) d u=\int_{E} f d u+\int_{E} g d u
$$

To show a fundion is integrable it must be shown that it can be written as a linear combination of nonnegative functions so for 1

If $c \geqslant 0$ then from previous theorems for nonnegative measurable function

$$
\begin{aligned}
& c\left(f_{+}\right)=(c f)_{+} \\
& c\left(f_{-}\right)=(c f)_{-}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\int_{E} c f d u & =\int_{E} c f_{+} d u-\int_{E} c f_{-} d u \\
& =c \int_{E} f_{+} d u-c \int_{E} f d u \\
& =c\left(\int_{E} f_{+} d u-\int_{E} f_{-} d u\right) \\
& =c \int_{E} f d u
\end{aligned}
$$

Thus $c f \in \mathcal{L}(\mu, E)$

If $c<0$ then $-c\left(f_{t}\right)=-\left(c f_{t}\right)$ and $-c\left(f_{-}\right)=-\left(c f_{-}\right)$so

$$
\begin{aligned}
-\int c f d u & =\int_{E}\left(-c f_{+}\right) d u-\int_{E}\left(-c f_{-}\right) d \mu \\
= & -c\left(\int_{E} f_{+} d u-\int_{E} f_{-} d u\right) \\
& =-c \int_{E} f d u
\end{aligned}
$$

Thus for $c<0 \quad c f \in \mathcal{L}(\mu, E)$
Now for tem 2 let

$$
n=f+g
$$

If it is assumed that neither $n$, $f$ or $g$ change sign on $E$ tre six cases need to be considered

1. $f \geqslant 0, g \geqslant 0, h \geqslant 0$ on $E$
2. $f \leqslant 0, g \leqslant 0, h \leqslant 0$ on $E$
3. $f \geqslant 0, g \leqslant 0, h \geqslant 0$ on $E$
4. $f \geqslant 0, g \leqslant 0, h \leqslant 0$ on $E$
5. $f \leqslant 0, g \geqslant 0, h \geqslant 0$ on $E$
6. $f \leqslant 0, g \geqslant 0, h \leqslant 0$ on $E$

Condition 1 has already been proven for nonnegative measurable functions. case 2 can be transformed to case 1 in the following manner

$$
-n=-f-g
$$

where $-h,-f$ and- $g$ are nonnegative measurable functions Thus

$$
\int_{E}(-h) d u=\int_{E}(-f) d u+\int_{E}(-g) d u
$$

The other conditions can be proven using the same proceedure Thus

$$
\begin{aligned}
& f+g \in \mathcal{L}(\mu, E) \\
& \text { if } f \in \mathcal{L}(\mu, E) \text { and } g \in \mathcal{L}(\mu, E)
\end{aligned}
$$

## Theorem

(Monotonicity) Let $f, g \in \mathcal{L}(\mu, E)$ with $f \leqslant g$ Then

$$
\int_{E} f d \mu=\int_{E} g d \mu
$$

Proof
Since $f \leqslant g \Rightarrow g-f \geqslant 0$ then
from linearity

$$
\begin{aligned}
0 & \leqslant \int_{E}(g-f) d \mu=\int_{E} g d \mu-\int_{E} f d \mu \\
& \Rightarrow \int_{E} f d \mu \leqslant \int_{E} g d \mu
\end{aligned}
$$

## Theorem

If $f \in \mathcal{L}(\mu, E)$ then

$$
\left|\int_{E} f d u\right| \leqslant \int_{E} \text { if } \mid d u
$$

Proof
since $f \leqslant|f|$ by monotonicity it follows that

$$
\int_{E} f d u \leqslant \int_{E} \operatorname{lf} i d u
$$

and $-f \leqslant|f|$ so

$$
\text { - } \int_{E} f d u \leqslant \int_{E}|f| d u
$$

it follows that

$$
\left|\int_{E} f d u\right| \leqslant \int_{E}|f| d u
$$

Limits of Sequences of Functions
In this section limits of sequences of functions are reviewed. consider the sequence of functions

$$
\left\{f_{1}(x), f_{2}(x), f_{3}(x), \ldots\right\}
$$

defined on the set $x \in E$ suppose that the sequence converges for every $x \in E$. Then a function $f$ can be defined by

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x) \quad \forall x \in E
$$

$f(x)$ is called the limit function of the sequence $\left\{f_{n}(x)\right\}$. If

$$
f(x)=\lim _{n \rightarrow \infty} \sum_{i=1}^{n} f_{i}(x) \quad \forall x \in E
$$

Then $f(x)$ is called the sum of the series.

An example of a sequence of functions

$$
f_{n}(x)=\frac{x^{2}}{\left(1+x^{2}\right)^{n}} \quad n=1,2,3, \ldots
$$

if

$$
\begin{aligned}
f(x) & =\sum_{n=1}^{\infty} \frac{x^{2}}{\left(1+x^{2}\right)^{n}} \\
& =x^{2} \sum_{n=1}^{\infty} \frac{1}{\left(1+x^{2}\right)^{n}}
\end{aligned}
$$

clearly $f_{n}(0)=0$ for eveny $n$ so $f(0)=0$ low

$$
1+x^{2}>1 \quad \forall \quad x \neq 0
$$

so the series is geometric and converges to

$$
\begin{aligned}
f(x) & =\sum_{n=1}^{\infty} \frac{x^{2}}{\left(1+x^{2}\right)^{n}}=x^{2} \frac{\left(1+x^{2}\right)}{x^{2}} \\
& =1+x^{2}
\end{aligned}
$$

Now consider the limits
$\limsup _{n \rightarrow \infty} f_{n}(x)=\lim _{n \rightarrow \infty} \sup _{m \geqslant n} f_{m}(x)$
$\liminf _{n \rightarrow \infty} f_{n}(x)=\lim _{n \rightarrow \infty} \inf _{m \geqslant n} f_{m}(x)$

To understand these limits consider

$$
g_{n}(x)=\sup _{m \geqslant n} f_{m}(x)
$$

for $n=1$ this is the supremum of the entire set. For $n=2 f_{1}(x)$ is exclude and for arbitrary $n$ the first $n$ elements of the set are excluded from the supremum. It follows that $g_{n}(x)$ will Nerrease with $n$.

$$
g_{1}(x) \geqslant g_{2}(x) \geqslant g_{3}(x) \geqslant \cdots
$$

in a similar manner

$$
h_{n}(x)=\inf _{m \geqslant n} h_{n}(x)
$$

$h_{n}(x)$ will be an increasing sequence

$$
h_{1}(x) \geqslant h_{2}(x) \geqslant h_{3}(x) \geqslant \cdots
$$

so

$$
\begin{aligned}
& \limsup _{n \rightarrow \infty} f_{n}(x)=\lim _{n \rightarrow \infty} g_{n}(x) \\
& \liminf _{n \rightarrow \infty} f_{n}(x)=\lim _{n \rightarrow \infty} h_{n}(x)
\end{aligned}
$$

As an example consider

$$
f_{n}(x)=(-1)^{n} x^{n}
$$

first evaluate $g_{n}(x)$, and consider the case $x \leqslant 0$ so

$$
f_{n}(-x)=(-1)^{n}(-x)^{n}=(-1)^{n}(-1)^{n} x^{n}
$$

$$
=x^{n}
$$

$$
g_{n}(x)=\sup _{m \geqslant n} f_{n}(x)=x^{n}
$$

for $x>0$

$$
f_{n}(x)=(-1)^{n} x^{n}
$$

so

$$
g_{n}(x)=\sup _{m \geqslant n} f_{n}(x)=x^{n}
$$

and similary for $x \leqslant 0$

$$
h_{n}(x)=\inf _{m \geqslant n} f_{n}(x)=(-x)^{n}
$$

and for $x \geqslant 0$

$$
h_{n}(x)=\inf _{m \geqslant n} f_{n}(x)=-x^{n}
$$

It follows that

$$
\lim \sup _{n \rightarrow \infty} f_{n}(x)=\left\{\begin{array}{cc}
\infty & x<-1 \\
\infty & x>1 \\
0 & -1<x<1 \\
1 & x=-1 \\
1 & x=1
\end{array}\right.
$$

$$
\liminf _{n \rightarrow \infty} f_{n}(x)=\left\{\begin{array}{rl}
\infty & x<-1 \\
\infty & x>1 \\
0 & -1<x<1 \\
1 & x=-1 \\
-1 & x=1
\end{array}\right.
$$

Fatou's Lemma

Let $f_{1}, f_{2}, f_{3}, \ldots$ be a sequence of nonegative measurable functions.
Let, Let, $f=\liminf _{n \rightarrow \infty} f_{n}$
then

$$
\int_{E} f d \mu \leqslant \liminf _{n \rightarrow \infty} \int f_{n} d \mu
$$

## Proof

Let

$$
g_{k}=\inf _{n \geqslant k} f_{n}
$$

and

$$
a_{k}=\inf _{n \geqslant k} \int f_{n} d u
$$

it follows that both $g_{k}$ and
$a_{k}$ are increasing sequences,

$$
\begin{aligned}
& g_{1} \leq g_{2} \leq g_{3} \leq \cdots \\
& a_{1} \leq a_{2} \leq a_{3} \leq \cdots
\end{aligned}
$$

from the defintion of limit inferior it follows that

$$
\begin{gathered}
f=\lim _{k \rightarrow \infty} g_{k} \\
\lim _{n \rightarrow \infty} \inf \int f_{n} d \mu=\lim _{k \rightarrow \infty} a_{k}
\end{gathered}
$$

From the montone convergence Theorem and since it is assumed that

$$
f=\lim _{k \rightarrow \infty} S_{k}
$$

it follows that

$$
\int_{E} f d \mu=\lim _{k \rightarrow \infty} \int_{E} g_{k} d \mu
$$

low from the defintion of infimum for $n \geqslant k$ it follows that

$$
g_{k} \leqslant f_{n}
$$

monotonicity of integral gives for $n \geqslant k$

$$
\begin{aligned}
& \int_{E} g_{k} d u \leqslant \int_{E} f_{n} d u \\
\Rightarrow & \int_{E} g_{k} d u \leqslant \inf _{n \geqslant k} \int_{E} f_{n} d u=a_{k}
\end{aligned}
$$

since

$$
\inf _{n \geqslant k} \int_{E} f_{n} d u
$$

will equal some $\int_{E} f_{n} d \mu$
Taking limits gives the desired result

$$
\begin{aligned}
\int_{E} f d \mu & =\lim _{k \rightarrow \infty} \int_{E} g_{k} d \mu \leqslant \lim _{k \rightarrow \infty} a_{k} \\
& =\lim _{n \rightarrow \infty} \inf _{E} f_{n} d \mu \\
\Rightarrow \int_{E} f d \mu & \leqslant \liminf _{k \rightarrow \infty} \int_{E} f_{k} d \mu
\end{aligned}
$$

Note that this is equivalent to $\int_{E} \liminf _{k \rightarrow \infty} f_{k} d \mu \leqslant \liminf _{k \rightarrow \infty} \int_{E} f_{k} d \mu$
which moves the inferiour lamit outside of the integral.

## Lesbegue Dominated Convergance Theorem

Let $f_{1}, f_{2}, f_{3}, \ldots$ be a sequence of of measureable functions. Let $E \in \mathcal{F}$ and make the following assumptions

1. $\lim _{n \rightarrow \infty} f_{n}(x)$ exists for all $x \in E$.
2. There is a nonegative measureable function $g \in \mathcal{L}(\mu, E)$ with $g \geqslant\left|f_{n}\right|$ on $E$ where $n=1,2,3, \ldots$
Then the function

$$
f(x)=\lim _{n \rightarrow \infty} f_{n}(x)
$$

is integrable and

$$
\int_{E} \lim _{n \rightarrow \infty} f_{n} d u=\lim _{n \rightarrow \infty} S_{E} f_{n} d u
$$

## Proof

By Fatou's lemma,

$$
\begin{aligned}
\int_{E}|f| d \mu & =\int_{E} \liminf _{n \rightarrow \infty}\left|f_{n}\right| d \mu \\
& \leqslant \lim _{n \rightarrow \infty} \inf _{\infty} \int_{E}\left|f_{n}\right| d \mu
\end{aligned}
$$

Since it is assumed that $g \geqslant\left|f_{n}\right|$ it follows that

$$
\liminf _{n \rightarrow \infty} \int_{E}\left|f_{n}\right| d \mu \leqslant \int_{E} g d \mu
$$

Thus

$$
\int_{E}|f| d u \leqslant \int_{E} g d u
$$

Recall that a function is integrable if

$$
\int_{E}|f| d u<\infty
$$

Since $g$ is integrable

$$
\int_{E}|g| d u<\infty
$$

but $S$ is nonregative so

$$
|g|=g
$$

thus

$$
\int_{E}|f| d u<\infty
$$

and $f(x)$ is integrable, $f \in \mathcal{L}(\mu, E)$.
This completes the first part of the theorem.

Now since

$$
S \geqslant\left|f_{n}\right|
$$

it follows that

$$
g+f_{n} \geqslant 0
$$

Using Fatou's lemma

$$
\begin{aligned}
\int_{E} \lim _{n \rightarrow \infty} \inf \left(g+f_{n}\right) d u & \\
& \leqslant \liminf _{n \rightarrow \infty} \int_{E}\left(g+f_{n}\right) d u
\end{aligned}
$$

now

$$
\begin{aligned}
\lim _{n \rightarrow \infty} \inf \left(g+f_{n}\right) & =g+\liminf _{n \rightarrow \infty} f_{n} \\
& =g+f
\end{aligned}
$$

50

$$
\begin{aligned}
& \liminf _{n \rightarrow \infty} \int_{E}\left(g+f_{n}\right) d u \\
& =\int_{E} g d u+\liminf _{n \rightarrow \infty} \int_{E} f_{n} d u
\end{aligned}
$$

bringing things together gives

$$
\begin{gathered}
\int_{E} \lim _{n \rightarrow \infty} \inf _{\infty}\left(g+f_{n}\right) d \mu \leqslant \rho_{g} d \mu \\
+\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu
\end{gathered}
$$

$\Rightarrow \int_{E} g d u+\int_{E} \lim _{n \rightarrow \infty} \inf f_{n} d u$

$$
\leqslant \int_{E} \rho d \mu+\liminf _{n \rightarrow \alpha} \int_{E} f_{n} d \mu
$$

but

$$
f=\liminf _{n \rightarrow \infty} f_{n}
$$

Thus

$$
\int_{E} f d \mu \leqslant \liminf _{n \rightarrow \alpha} \int_{E} f_{n} d \mu
$$

Next consider

$$
g-f_{n} \geqslant 0
$$

since $g \geqslant\left|f_{n}\right|$. Applying Fatoris lemma

$$
\begin{aligned}
\int_{E} \lim _{n \rightarrow \infty} \inf \left(g-f_{n}\right) d u & \\
& \leqslant \liminf _{n \rightarrow \infty} \int_{E}\left(g-f_{n}\right) d u
\end{aligned}
$$

Following the previous proceedure gives

$$
-\int_{E} f d u \leqslant \liminf _{n \rightarrow \infty} f\left(-f_{n}\right) d u
$$

$$
\begin{aligned}
& =-\limsup _{n \rightarrow \infty} \int_{E} f_{n} d u \\
& \Rightarrow \int_{E} f d u \geqslant \limsup _{n \rightarrow \infty} \int_{E} f_{n} d u
\end{aligned}
$$

Combing this with the prevides result gives
$\limsup _{n \rightarrow \infty} \int_{E} f_{n} d u \leqslant \int_{F} f d u$

$$
\leqslant \lim _{n \rightarrow \infty} \inf _{\infty} \int_{E} f_{n} d u
$$

but it is always true that

$$
\lim \inf \leqslant \lim \sup
$$

Thus

$$
\begin{aligned}
\limsup _{n \rightarrow \infty} \int_{E} f_{n} d u & =\lim _{n \rightarrow \infty} \inf _{\infty} \int_{E} f_{n} d u \\
& =\lim _{n \rightarrow \infty} \int_{E} f_{n} d u
\end{aligned}
$$

and

$$
\int_{E} f d \mu=\lim _{n \rightarrow \infty} \int_{E} f_{n} d \mu
$$

Note that this is an extension of the montone convergence theorem to integrable functions which can be negative.

## Theorem

Let $f_{1}, f_{2}, f_{3}, \ldots$ be a sequence in $\mathcal{L}(\mu, E)$ with

$$
\sum_{c=1}^{\infty} \int_{E}\left|f_{n}\right| d \mu<\infty
$$

then

1. $\sum_{n=1}^{\infty} f_{n}$ converges absoluthy almost everywhere on $E$ and is integrable on $E$
2. $\quad \int_{E} \sum_{n=1}^{\infty} f_{n} d \mu=\sum_{n=1}^{\infty} S_{E} f_{n} d \mu$

This is the generalization of a result previously proven for nornegative fundions.

