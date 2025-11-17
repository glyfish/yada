$$
\sup A=\infty
$$

## Theorem

Even, non-empty subset of $\bar{R}$ has an infimum and supremum. If $\left\{a_{i}\right\}_{i=1}^{\infty}$ is a sequence in $\hat{k}$, then the limits sup $a_{i}$ and inf $a_{i}$ exist in $\hat{\mathbb{R}}$

## Definition

convergence of a sequence to include $\pm \infty$ is accomplisher in the following mater

A sequence $\left\{a_{i}\right\}_{i=1}^{\infty} \subset \hat{R}$ converges to $\infty$ if $\forall r \in \mathbb{R}$ there is an $m$ such that $a_{i} \geqslant r$ for $i \geqslant m$.
Likewise a sequence $\left\{a_{i}\right\}_{i=1}^{\infty} \subset \hat{R}$ converges to - $\infty$ if $\forall r \in \mathbb{R}$ there is an $m$ such that $a_{i} \leqslant r$ for $i \geqslant m$.

It follows that

1. If $\left\{a_{i}\right\}_{i=1}^{\infty}$ is an increasing sequence in $\hat{R}$ then $\left\{a_{i}\right\}_{i=1}^{\infty}$ converges to lim sup $a_{i}$.
2. If $\left\{a_{i}\right\}_{i=1}^{\infty}$ is a deoreasing sequence in $\hat{R}$ then $\left\{a_{i}\right\}_{i=1}^{\infty}$ converges to $\lim$ inf $a_{i}$
3. An arbitrary sequence $\left\{a_{i}\right\}_{i=1}^{\infty}$ in $\hat{R}$ converges in $\hat{R}$ if and only if $\lim \sup a_{i}=\lim \inf a_{i}$ in which case

$$
\lim a_{i}=\lim \sup a_{i}=\lim \inf a_{i}
$$

## Definition

An extended real ualued nonegative function on $a$ set $X$ is a function that maps $X$ to $\hat{\mathbb{R}}^{+}$.

## Probability model for a sequence of Coin Tosses

Consider an exprement with two possible outcomes where the probability of the atcomes is the same for each trial of the expirement. If a finite number of independent trials is perfomed it is called a Bernauli trial. If an infinite number of independent trials is performed it is called a Bernoulli sequence.
For the Bernoulli sequence the space of all sequences will be denoted by

$$
B=\{\text { all Berroulli sequences }\}
$$

Here a Bernoulli sequence is discussed. The experiment performed is tossing a fair coin. The two outcomes are denoted by
$H=$ heads and $T=$ tails since the com is far the probability of each outcome is the same. In general this assumption is not reguired.
It will be shown that a one-to-one (surjective) mapping from $\Omega=(0,1]$ to $B$ can be constructed which impies that $B$ is uncountable. $\Omega=0,1]$ is called the sample space of the probability model.
Consider an example experiment in the coin toss Bernoulli sequence where $T$ denotes a toss of tails and $H$ a toss of heads

HTTTHTHHHHTHTT…
A mapping between the expirement and $\Omega=[0,1]$ can be constructer
as follows. Let $\omega \in \Omega$ be given by a binary decimal number expansion,

$$
\omega=\sum_{n=1}^{\infty} \frac{a_{n}}{2^{n}} \text { where } a_{i} \in\{0,1\}
$$

The Bernoulli sequence expriment can be represented by letting $a_{i}=0$ if the i'th toss of the expiriment is $T$ and $a_{i}=1$ if the ith toss is $H$.
For the Bernoulli sequence expiriment

## HTTTHTHHHHTHTT…

the binary decimal representation is given by

## $0.10001011110100 \ldots$

The problem with this representation is that multiple binary sequences map to the same $\omega \in \Omega$.

For example a sequence where the frst toss is a head and all other tosses are tails is given by

$$
\begin{aligned}
& \omega=0.10000 \cdots=\frac{1}{2}+0+0+0 \cdots \\
& =\frac{1}{2}
\end{aligned}
$$

and for a sequence where the furst toss is tails and all other tosses are tails

$$
\begin{aligned}
\omega & =0.011111 \cdots \\
& =\sum_{i=2}^{\infty} \frac{1}{2} i
\end{aligned}
$$

Recall that the sum of a geometric series is given by

$$
\begin{aligned}
\sum_{n=0}^{\infty} r^{n} & =\frac{1}{1-r} \\
1+\sum_{n=1}^{\infty} r^{n} & =\frac{1}{1-r}
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow \sum_{n=1}^{\infty} r^{n} & =\frac{1}{1-r}-1 \\
& =\frac{1-1+r}{1-r}=\frac{r}{1-r}
\end{aligned}
$$

Thus

$$
\sum_{n=1}^{\infty} r^{n}=\frac{r}{1-r}
$$

it follows that

$$
\begin{aligned}
\omega & =0.011111 \\
& =\sum_{n=2}^{\infty} \frac{1}{2^{n}}=\sum_{n=1}^{\infty} \frac{1}{2^{n+1}} \\
& =\frac{1}{2} \sum_{n=1}^{\infty} \frac{1}{2^{n}} \\
& =\frac{1}{2} \frac{(1 / 2)}{1-1 / 2}=\frac{1}{2} \frac{(1 / 2)}{(1 / 2)}=\frac{1}{2}
\end{aligned}
$$

Thus

$$
0.100000 \cdots=0.01111111 \cdots
$$

as another example consider

$$
0.110000 \cdots=\frac{1}{2}+\frac{1}{4}=\frac{3}{4}
$$

and

$$
\begin{aligned}
0.10111111= & \frac{1}{2}+\sum_{n=3}^{\infty} \frac{1}{2^{n}} \\
= & \frac{1}{2}+\sum_{n=1}^{\infty} \frac{1}{2^{n+2}} \\
= & \frac{1}{2}+\frac{1}{2^{2}} \sum_{n=1}^{\infty} \frac{1}{2^{n}} \\
= & \frac{1}{2}+\frac{1}{4} \frac{(12)}{(12)} \\
= & \frac{1}{2}+\frac{1}{4}=\frac{3}{4}
\end{aligned}
$$

Thus

$$
0.1100000 \cdots=0.1011111 \cdots
$$

Finally consider

$$
0.10100000 \cdots=\frac{1}{2}+\frac{1}{8}=\frac{5}{8}
$$

and

$$
0.100111111 \ldots=\frac{1}{2}+\sum_{n=4}^{\infty} \frac{1}{2 n}
$$

$$
\begin{aligned}
& =\frac{1}{2}+\sum_{n=1}^{\infty} \frac{1}{2^{n+3}} \\
& =\frac{1}{2}+\frac{1}{2^{3}} \sum_{n=1}^{\infty} \frac{1}{2^{n}} \\
& =\frac{1}{2}+\frac{1}{8}=\frac{5}{8}
\end{aligned}
$$

## Thus

$$
0.1010000 \cdots=0.10011111 \cdots
$$

It follows that for a binary decimal that ends in o's after the $k^{\prime}$ th digit,

$$
\begin{aligned}
a_{1} a_{2} a_{3} & \cdots a_{k} 0000 \cdots \\
& =a_{1} a_{2} a_{3} \cdots a_{k-1} 01111 \cdots
\end{aligned}
$$

To prove this relation note that in the lefthand side it must be trat $a_{k}=1$ or the terminating zeros would start at $k-1$.
It follows that for the righthard side the k'th torm in the binary decimal expansion is given by
the sum of the trailing is starting at $k+l$, namely,

$$
\begin{aligned}
& \sum_{n=k+1}^{\infty} \frac{1}{2^{n}}=\sum_{n=1}^{\infty} \frac{1}{2^{n+k}} \\
& =\frac{1}{2^{k}} \sum_{n=1}^{\infty} \frac{1}{2^{n}}=\frac{1}{2^{k}}=\frac{a_{k}}{2^{k}}
\end{aligned}
$$

which is the k'th term in the binary decimal terminated in O's. This proves equality It follows that any binary decimal which terminates in os after the k'th digit maps to the some real number as a binary decimal terminating in is starting from the $k+l$ 'th digit with $a_{k}=0$ and the digits from $a_{1} a_{2} \cdots a_{k-1}$ the same as the binary decimal terminating in o's.

Here the binary decimal terminating in Os will be ignored allowing the infective, one-to-one, maping from $(0,1] \rightarrow B$ which proves that $B$ is uncountable. This is equivalent to discarding all Bernoulli sequences torminatins in T's to justify the ingroring these Berroulli sequences it must be shown that his set is countable.

Thus ignoring it's contribution is justified since a countable subset of an uncountable set is insignificant.

It is because of this that $\Omega=(0,1]$ since $O$ cound be represented if this convention is choosen.

Let $B_{k}^{\top}$ denote the set of all Bernoulli sequences which
have all $T$ 's after the $k$ 'th digit and let

$$
B^{\top}=\bigcup_{k=1}^{\infty} B_{k}^{\top}
$$

denote the set of all binary decimals terminating in $T$ 's.
Consider $k=3$ then $B_{3}^{\top}$ is given by
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-012.jpg?height=765&width=572&top_left_y=1001&top_left_x=229)

| $/^{\top} \lambda^{\top}$ |  |  |  |
| :---: | :---: | :---: | :---: |
| $H^{\prime}$ | $T$ | $H^{\prime}$ |  |
| $\mid$ | $\mid$ | $\mid$ | $\mid$ |
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $T$ | $T$ | $T$ |
| $T$ | $T$ | $T$ | $T$ |
| $\vdots$ | $\vdots$ | $\vdots$ | $\vdots$ |

Clearly the number of sequences
is finite with the total number of sequences equal to $2^{3}=8$ It follows that for every $K$ that $B_{k}^{T}$ is finite and thus countable. It follows that

$$
B^{\top}=\bigcup_{k=1}^{\infty} B_{k}^{\top}
$$

is countable since a countable union of countable sets is countable, thus BT can be discarded.
It follows that the binany decimal expansion of the Berroulli sequences provides a one-to-one, injective, mappins $\Omega \rightarrow B$ proung that $B$ is uncountable.

## Assignment of Probabilities

In this section the mapping
of events in the Bernoulli sequence $B$ to probabilities in $\Omega$ is discussed.

In the previous section it was shown that the mapping $\Omega \rightarrow \mathbb{B}$ is given by

$$
\omega=\sum_{i=1}^{\infty} \frac{a_{i}}{2^{i}}
$$

where $w \in \Omega$ and $a_{i} \in\{0,1\}$ where $a_{i}=0$ indicates that the ith toss is tails and $c_{i}=1$ indicates the ith toss is heads.

Consider an event $A \in \mathbb{B}$. It is desired to assign a probability to $A$ equal to the measerve of the subset $I_{A} \subset \Omega$.

As an example consider
the event consisting of all sequences in B where the first toss is heads and denote it by $A_{H}$. The corresponding set in $\Omega$ is given by
$I_{H}=\left\{\omega \in \Omega, \omega=0.1 a_{2} a_{3} a_{4} \cdots ; a_{i} \in\{0,1\}\right\}$
The smallest value of $\omega$, which is not in $I_{H}$ is

$$
\omega=0.10000 \cdots=1 / 2
$$

This value of $\omega$ is not in It since sequences which torminate is heads are not included in the mapping.
The largest value of $\omega$ which is in $I_{H}$ is given

$$
\omega=0.111111 \cdots=1
$$

It follows that $I_{H}$ is equal to the interval

$$
I_{H}=(0.5,1]
$$

similarly the event corresponding to all sequences in $B$ where the first toss is tails is given by
$I_{T}=\left\{\omega \in \Omega, \omega=0.0 a_{2} a_{3} a_{4} \cdots ; a_{i} \in\{0,1\}\right\}$
using the same reasoning the the smallest value which is not in $I_{T}$ is

$$
\omega=0.00000
$$

and the largest value is

$$
\omega=0.0111111 \cdots
$$

it follows that

$$
I_{T}=(0,0.5]
$$

one expects the probability of both events is 0.5 ,

$$
P\left(A_{T}\right)=P\left(A_{H}\right)=0.5
$$

Note that the length, measure,
of $I_{A}$ that gives the desired result is the length of the interval

$$
\begin{aligned}
& P\left(A_{\tau}\right)=0.5-0.0=0.5 \\
& P\left(A_{H}\right)=1.0-0.5=0.5
\end{aligned}
$$

This measure is the Lebesgue measure. If the measure is denoted by $\mu$ then

$$
\begin{aligned}
& P\left(A_{T}\right)=\mu((0,0.5]) \\
& P\left(A_{H}\right)=\mu((0.5,1.0])
\end{aligned}
$$

In this analysis it is noticable how nice deleting the set $B^{\top}$ worked out. Recall that B ${ }^{\top}$ was deleted to make the mapping $Q \rightarrow B$ one-to-one, injective and that it cosists of all Berroulli sequeces terminating in tails. Because of this $A_{T} \cap A_{H}=\varnothing$ so that the events do not overlap

Recall that a measure is a real valued function $\mu$ defined on a collection of subsets of a space I called the measureable sets. If $A$ is a measurable set $\mu(A)$ is the measure of A. A measure must satisfy,

1. $\mu(A) \geqslant 0$
2. If $\left\{A_{i}\right\}_{i=1}^{m}$ is a collection of measureable disjont sets the $U_{i=1}^{m} A_{i}$ is measurable
3. If $\left\{A_{i}\right\}_{i=1}^{m}$ is a collection of measureable disjoint sets then

$$
\mu\left(\bigcup_{i=1}^{m} A_{i}\right)=\sum_{i=1}^{m} \mu\left(A_{i}\right)
$$

These properties are the same as those of a probability function.
$\Delta$ Lebesgue measure is defined as follows.
If the space $X$ is a interval of real numbers and the measureable sets include interoals for which

$$
\begin{aligned}
\mu((a, b)) & =\mu([a, b])=\mu((a, b]) \\
& =\mu([a, b)) \\
& =b-a
\end{aligned}
$$

This defines a Lebesguse measure on I which is written as

$$
\mu=\mu_{2}
$$

Note that this definition implies that the measure of a point is given by

$$
\mu_{\alpha}(\{a\})=a-a=0
$$

As another example consider
the events $A_{H H}, A_{H T}, A_{T H}$ and $A_{T T}$ which denote the cuents where the first two tosses are $H H, H T, T H$ and $T T$ respectroly.
using the same proceedure used to compute

$$
\begin{aligned}
& P\left(A_{T}\right)=\mu_{\alpha}\left(I_{T}\right)=\mu_{\alpha}((0,0.5))=0.5 \\
& P\left(A_{H}\right)=\mu_{\alpha}\left(I_{H}\right)=\mu_{\alpha}((0.5,1])=0.5
\end{aligned}
$$

where

$$
\begin{aligned}
& I_{1}=\left\{\omega \in \Omega, \omega=0.0 a_{2} a_{3} a_{4} \cdots, a_{i} \in\{0,1\}\right\} \\
& I_{H}=\left\{\omega \in \Omega, \omega=0.1 a_{2} a_{3} a_{4} \cdots ; a_{i} \in\{0,1\}\right\}
\end{aligned}
$$

It follows that.
$I_{T \tau}=\left\{\omega \in \Omega, \omega=0.00 c_{3} a_{4} \cdots, a_{i} \in\{0,1\}\right\}$ the minimum and maximum values of $w$ in this set are

$$
\begin{aligned}
& \omega^{-}=0.0000 \cdots=0 \\
& \omega^{+}=0.00111 \cdots=\frac{1}{4}
\end{aligned}
$$

$\omega^{-}$is not in $B$ so
$I_{T T}=(0,0.25]$
similarly

$$
\begin{aligned}
I_{T H} & =\left\{\omega \in \Omega, \omega=0.01 a_{3} a_{4} \cdots, a_{i}=\{0,1\}\right\} \\
\omega^{-} & =0.01000 \cdots=\frac{1}{4} \\
\omega^{+} & =0.01111 \cdots=\frac{1}{2}
\end{aligned}
$$

since $\omega^{-}$is not in $B$

$$
\begin{aligned}
& I_{T H}=(0.25,0.5] \\
& I_{H T}=\left\{\omega \in R, \omega=0.10 a_{3} a_{4} \cdots ; a_{i} \in\{0,1\}\right\} \\
& \omega^{\prime}=0.10000 \cdots=\frac{1}{2} \\
& \omega^{+}=0.101111 \cdots=\frac{1}{2}+\frac{1}{4}=\frac{3}{4} \\
& I_{H T}=(0.5,0.75] \\
& I_{H H}=\left\{\omega \in \Omega, \omega=0.11 a_{3} a_{4} \cdots ; a_{i} \in\{0,1\}\right\} \\
& \omega^{\prime}=0.110000 \cdots=\frac{3}{4} \\
& \omega^{t}=0.111111=1
\end{aligned}
$$

$$
I_{H H}=(0.75,1]
$$

Thus

$$
\begin{array}{ll}
I_{T T}=(0,0.25] & I_{T H}=(0.25,0.5] \\
I_{H T}=(0.5,0.75] & I_{H H}=(0.75,1.0]
\end{array}
$$

The probabilities are

$$
\begin{aligned}
P\left(A_{T T}\right) & =\mu_{\mathcal{L}}\left(I_{T T}\right)=\mu_{\mathcal{L}}((0.0,0.25]) \\
& =0.25-0.0=0.25 \\
P\left(A_{T H}\right) & =\mu_{\mathcal{I}}\left(I_{T H}\right)=\mu_{\mathcal{L}}((0.25,0.5]) \\
& =0.5-0.25=0.05 \\
P\left(A_{H T}\right) & =\mu_{\mathcal{L}}\left(I_{H T}\right)=\mu_{\mathcal{L}}((0.5,0.75]) \\
& =0.75-0.5=0.25 \\
P\left(A_{T T}\right) & =\mu_{\mathcal{J}}\left(I_{T T}\right)=\mu_{\mathcal{L}}((0.75,1.0]) \\
& =1.0-0.75=0.25
\end{aligned}
$$

which agree with expectations.

Thus for the first two tosses, denoting the toss by, $m$

$$
\begin{array}{lr}
m=1 & P\left(A_{T}\right)=\frac{1}{2} \\
m=2 & P\left(A_{H}\right)=\frac{1}{2} \\
P\left(A_{T T}\right)=\frac{1}{4} & P\left(A_{T H}\right)=\frac{1}{4} \\
P\left(A_{H T}\right)=\frac{1}{4} & P\left(A_{T T}\right)=\frac{1}{4}
\end{array}
$$

Thus for arbitrary values of
$m$

$$
\begin{array}{rl}
m=0 & 0 \\
m=1 & \underbrace{}_{m} \\
m=2 & \underbrace{x}_{x} \quad x \quad x \\
m=3 & \biguplus_{x}^{x} \times x \times x \times x \\
m=4 & (x \times x \times x \times x \times x \times x \times x \times x]
\end{array}
$$

It is seen that for an arbitrary $m$ that the number of interals is given by

$$
j^{+}=2^{m}
$$

since the total interval length is 1 it follows that the width of each interval is given by

$$
\frac{1}{j^{+}}=2^{-m}
$$

if the intervals are encomerated by

$$
J=1,2,3, \cdots 2^{m}
$$

the endpoints for an interval for an arbitrary $j$ and $m$ are given by
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-024.jpg?height=336&width=1160&top_left_y=1668&top_left_x=96)

$$
I_{m j}=\left((j-1) 2^{-m}, j 2^{-m}\right]
$$

Since $\Omega=(0,1]$ it follows that

$$
\Omega=\bigcup_{j=1}^{2^{m}} I_{m j}
$$

It follows that the probability of an event for a given $(m, j)$ pair is given by

$$
\begin{aligned}
P\left(A_{m j}\right) & =\mu_{\mathcal{L}}\left(I_{m j}\right) \\
& =\mu_{\mathcal{L}}\left(\left((j-1) 2^{-m}, j 2^{-m}\right]\right) \\
& =j^{-m}-(j-1) 2^{-m} \\
& =2^{-m}(j-j+1) \\
& =2^{-m}
\end{aligned}
$$

which is the expected value.

## Example

For an event $A$ in which $H$ is the m'th outcome what is its probabity of occurance. Now $I_{a}$ is given by

$$
\begin{gathered}
I_{A}=\left\{\omega \in \Omega, 0 \cdot a_{1} a_{2} \cdots a_{n-1} \mid a_{m+1} a_{m+2} \cdots ;\right. \\
\left.a_{i} \in\{0,1\}\right\}
\end{gathered}
$$

To solve this problem it must be noted that $I_{A}$ will consist of all intervals, events, obtained after $m$ tosses in which the last toss is heads one would expect that $P(A)=1 / 2$.
The solution to this problem can be obtained from the result of the previous problem. There it was shown that there are $2^{m}$ events in
which the first $m$ tosses are know. Since the events are equally probable the probability of each event is $2^{-m}$.
let

$$
s=0 . a_{1} a_{2} a_{3} \ldots a_{m-1} 1
$$

Each interval in $I_{A}$ will be given by

$$
\left(s, s+2^{-m}\right]
$$

where

$$
\mu_{\alpha}\left(\left(s, s+2^{-m}\right]\right)=2^{-m}
$$

The number of values of $s$ is equal to the number number of intervals which is given be the number of possible values of

$$
0 \cdot a_{1} a_{2} a_{3} \cdots a_{m-1}
$$

There are $2^{m-1}$ possible values. It follows that

$$
\begin{aligned}
P(A) & =\mu_{\mathcal{L}}\left(U_{s}\left(s, s+2^{-m}\right]\right) \\
& =\sum_{s} \mu_{\mathcal{L}}\left(\left(s, s+2^{-m}\right]\right) \\
& =2^{m-1} 2^{-m} \\
& =\frac{1}{2}
\end{aligned}
$$

which is the expected result. As an example consider the case where $m=3$. Then

$$
s=0 . a_{1} a_{2} l
$$

It follows that

$$
\begin{aligned}
I_{A}= & (1 / 8,1 / 4] \cup(3 / 8,1 / 2] \cup\left(5 / 8, \frac{3}{4}\right] \\
& \cup(7 / 8,1]
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-028.jpg?height=130&width=995&top_left_y=1882&top_left_x=259)

## Example

Let $A$ be the event that exactly $i$ of the first $m$ tosses are $H$.

Determine P(A) Let $B$ denote the event where the first $m$ tosses are known. It follows that,
$I_{B}=\left\{\omega \in \Omega ; \omega=0 . a_{1} a_{2} a_{3} \cdots a_{m} a_{m+1}\right.$

$$
\left.a_{m+2} \cdots ; a_{i} \in\{0,1\}\right\}
$$

Where $I_{B}$ is is the event where the first $m$ tosses are known

Let

$$
s=0 . a_{1} a_{2} a_{3} \cdots c_{\mathrm{m}}
$$

Previously it was shown that there $2^{\text {th }}$ possible ocalues of $s$ creating $2^{m}$ intervals of
length $2^{-m}$ where each interval is given by

$$
I_{j}=\left(S_{j}, S_{j}+2-m\right]
$$

where $j=1,2,3, \cdots, 2^{m}$.

$$
\mu_{\mathscr{L}}\left(\left(S_{j}, S_{j}+2-m\right]\right)=2^{-m}
$$

If exactly $i$ of the digits in $s$ are ones and $m-c$ are zero then the number of values of 5 is given
by the number of permutations of the digits. This is given by

$$
\binom{m}{i}
$$

since the probability of each permutation is given by $2-m$ it follows that

$$
P\left(A_{i m}\right)=\binom{m}{i} 2^{-m}
$$

## The weak law of large Numbers

This section will investigate the intuition that the probability of an outcome of heads, $H$, or tails, $T$, in a Bernoulli sequence, B, should be measureable by observing the outcome of a large number of exprements. If the com is fair then the probability of $H$ in an exprement is $1 / 2$. If $m$ expirements are performed and $S_{m}$ is the number of H's observed after $m$ tossed the exectation is that

$$
\lim _{m \rightarrow \infty} \frac{S_{m}}{m}=\frac{1}{2}
$$

This cannot be true since it is possible that all outcomes in the sequence are $T$ In the following sections the machinery needed to perform this analysis
is developed using the Bernoulli sequence as an example.

Definition: Random Nariable
A random variable is a function on the sample space, $\Omega$. For $\omega \in \Omega$ define the random variable

$$
S_{m}(\omega)=a_{1}+a_{2}+\cdots+a_{m}
$$

where $\omega=0 . a_{1} a_{2} a_{3} \cdots a_{m} \cdots$ and $a_{i} \in\{0,1\} . S_{m}(w)$ gives the number of heads in the first $m$ tosses of a Bernoulli sequence as a function of $w$.
Given $\delta>0$ define the event

$$
I_{\delta m}=\left\{\omega \in \Omega:\left|\frac{\delta_{m}(\omega)}{m}-\frac{1}{2}\right|>\delta\right\}
$$

This event consists of outcomes for which there are not
appoximately the same number of $H$ and $T$ after $m$ tosses where $\delta$ measures the bias.

The weak law of large numbers for Bernauli sequences can be stated as

* $\quad \mu_{y}\left(I_{\delta m}\right) \rightarrow 0$
as $m \rightarrow \infty$. This definition implies that for any fixed $\delta>0$ given any $\varepsilon>0$

$$
\mu_{z}\left(I_{\delta m}\right)<\varepsilon
$$

for all sufficiently large $m$.
To prove the Bernoulli sequence version the weak law of large Numbers more tools are needed.

Definition: Rademacher Function For $w \in \Omega$ the ith Rademacher function is defined by

$$
R_{i}(\omega)=2 a_{i}-1
$$

where

$$
\omega=0, a_{1} a_{2} a_{3} \cdots a_{i} \in\{0,1\}
$$

or equivalently

$$
R_{i}(\omega)=\left\{\begin{array}{cc}
1 & a_{i}=1 \\
-1 & a_{i}=0
\end{array}\right.
$$

Consider $R_{1}(\omega)=2 a_{1}-1$

$$
\begin{aligned}
& 0<\omega=0.0 a_{2} a_{3} a_{4} \cdots 1 / 2 \\
& 1 / 2<\omega=0.1 a_{2} a_{3} a_{4} \cdots \leqslant 1
\end{aligned}
$$

SO

$$
a_{1}= \begin{cases}0 & 0<\omega \leqslant 1 / 2 \\ 1 & 1 / 2 \omega \leqslant 1\end{cases}
$$

It follows that $R_{1}(\omega)$ is given by
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-035.jpg?height=723&width=712&top_left_y=96&top_left_x=439)

Next consider $R_{2}(\omega)=2 a_{2}-1$

$$
\begin{aligned}
0<0.00 a_{3} a_{4} a_{5} \cdots \leq 1 / 1 \\
1 / 4<0.01 a_{3} a_{4} a_{5} \cdots \leq 1 / 2 \\
1 / 2<0.10 a_{3} a_{4} a_{5} \cdots 3 / 4 \\
3 / 4<0.11 a_{3} a_{4} a_{5} \cdots \leqslant 1 \\
\text { so } \\
a_{2}= \begin{cases}0 & 0<\omega \leqslant 1 / 4 \\
1 & 1 / 4<\omega \leqslant 1 / 2 \\
0 & 1 / 2<\omega \leqslant 3 / 4 \\
1 & 3 / 4<\omega \leqslant 1\end{cases}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-036.jpg?height=743&width=664&top_left_y=88&top_left_x=360)

Next consider $R_{3}(\omega)=2 a_{3}-1$

$$
\begin{aligned}
& 0<0.000 a_{4} a_{5} \leq 1 / 8 \\
& 1 / 8<0.001 a_{4} a_{5} \cdots \leq 1 / 4 \\
& 1 / 4<0.010 a_{4} a_{5} \cdots \leq 3 / 8 \\
& 3 / 8<0.011 a_{4} a_{5} \cdots \leq 1 / 2 \\
& 4 / 2<0.100 a_{4} a_{5} \cdots \leq 8 / 8 \\
& 5 / 8<0.101 a_{4} a_{5} \cdots \leq 3 / 4 \\
& 3 / 4<0.110 a_{4} a_{5} \cdots \leq 7 / 8 \\
& 7 / 8<0.111 a_{4} a_{5} \cdots \leq 1
\end{aligned}
$$

## Thus

$$
R_{3}(\omega)\left\{\begin{array}{rl}
-1 & 0<\omega \leqslant 1 / 8 \\
1 & 1 / 8<\omega \leqslant 4 / 1 \\
-1 & 1 / 4<\omega \leqslant 3 / 8 \\
1 & 3 / 8<\omega \leqslant 12 \\
-1 & 12<\omega \leqslant 5 / 8 \\
1 & 5 / 8<\omega \leqslant 3 / 4 \\
-1 & 3 / 4<\omega \leqslant 7 / 8 \\
1 & 7 / 8<\omega \leqslant 1
\end{array}\right.
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-037.jpg?height=749&width=1091&top_left_y=1112&top_left_x=217)

Consider

$$
\omega_{m}(\omega)=\sum_{i=1}^{m} R_{i}(\omega)
$$

$R_{i}(\omega)$ can be considered as the amount won or lost in a betting game on the i'th toss. It follows that $\omega_{n}(\omega)$ is the total gain or loss after $m$ tosses for the Bernoulli sequence represented by $w$.
Now

$$
\begin{aligned}
\omega_{m}(\omega) & =\sum_{i=1}^{m} R_{i}(\omega) \\
& =\sum_{i=1}^{m}\left(2 a_{i}-1\right) \\
& =2 \sum_{i=1}^{m} a_{i}-m \\
& =2 S_{m}(\omega)-m
\end{aligned}
$$

where $S_{m}(\omega)$ is the number of H's in the Bernoculi
sequence represented by $w$
Recall that the intent of this exerase is to prove the weak law of large numbers for Bernoulli Sequences. The event where the number H's and T's are asymtotically equal is defined by

$$
I_{\delta m}=\left\{\omega \in \Omega:\left|\frac{S_{m}(\omega)}{m}-\frac{1}{2}\right|>\delta\right\}
$$

where $\delta>0$. The weak law of large numbers states that as $m \rightarrow \infty$

$$
\mu_{2}\left(I_{\delta m}\right) \rightarrow 0
$$

This is stating that for a fixed $\delta$ a sufficiently large $m$ exists such that

$$
\left|\frac{S_{m}(\omega)}{m}-\frac{1}{2}\right|<\delta
$$

then $I_{\delta m}=\phi$ so $\mu_{\alpha}\left(I_{\delta m}\right)=0$
Now using
$\omega_{m}(\omega)=2 \delta_{m}(\omega)-m$
consider

$$
\begin{aligned}
& \left|\frac{S_{m}(\omega)}{m}-\frac{1}{2}\right|>\delta \\
\Rightarrow & \left|2 S_{m}(\omega)-m\right|>2 m \delta \\
\Rightarrow & \left|\omega_{m}(\omega)\right|>2 m \delta
\end{aligned}
$$

Since $\delta$ is arbitrary the factor of 2 can be ignored.
Define the event

$$
A_{m}=\left\{\omega \in \Omega:\left|\omega_{m}(\omega)\right|>m \delta\right\}
$$

Note that $A_{m}$ is the inverse of $\omega_{m}(\omega)$ considered as a set function since

$$
\left|\omega_{m}(\omega)\right|>m \delta
$$

$\Rightarrow \omega_{m}(\omega)<-m \delta$ and $\omega_{m}(\omega)>m \delta$
$\Rightarrow \omega=\omega_{m}^{-1}(-m \delta)$ and

$$
\omega=\omega^{-1} m(m \delta)
$$

The weak law of large numbers can be proven by showing that

$$
\mu_{z}\left(A_{m}\right) \rightarrow 0
$$

as $m \rightarrow \infty$
To prove this the following result is needed

* $\mu_{\alpha}(\{\omega \in \Omega: f(\omega)>\alpha\})<\frac{1}{2} \int_{0}^{1} f(\omega) d \omega$ where the integral is the standerd Rieman integral, which is well defined for piecewise constant non-negative functions such as $\omega_{m}(\omega)$.
The set defined by

$$
\{\omega \in \Omega: f(\omega)>\alpha\}
$$

is illustrated in the following plot were the intervals included in Am are highlighted.
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-042.jpg?height=642&width=1263&top_left_y=362&top_left_x=241)

## Proof

Since $f$ is plecewise constant there is a mesh

$$
0=\omega_{1}<\omega_{2}<\omega_{3}<\cdots<\omega_{m+1}=1
$$

such that.

$$
f(\omega)=c_{i} \text { for } \omega_{i}<\omega<\omega_{i+1}
$$

for $1 \leqslant i \leqslant m$ so,

$$
\int_{0}^{1} f(\omega) d \omega=\sum_{i=1}^{m} c_{i}\left(\omega_{i+1}-\omega_{i}\right)
$$

Since $f(\omega) \geqslant 0 \quad \forall \omega$ it follows that

$$
\begin{gathered}
\sum_{i=1}^{m} c_{i}\left(\omega_{i+1}-\omega_{i}\right) \geqslant \sum_{i=1}^{m} c_{i}\left(\omega_{i+1}-\omega_{i}\right) \\
>\alpha \sum_{i=1}\left(\omega_{i+1}-\omega_{i}\right) \\
c_{i} \alpha \alpha \\
=\alpha \mu_{\alpha}(\xi \omega \in \Omega: f(\omega)>\alpha \xi)
\end{gathered}
$$

Thus, bringing things together gives the desired result,

$$
\frac{1}{\alpha} \int_{0}^{1} f(\omega) d \omega>\mu_{\alpha}(\xi \omega \in \Omega: f(\omega)>\alpha \xi)
$$

The desired result can now be proven, namely, for

$$
A_{m}=\left\{\omega \in \Omega:\left|\omega_{m}(\omega)\right|>m \delta\right\}
$$

$$
\mu_{2}\left(A_{m}\right) \rightarrow 0 \text { as } m \rightarrow \infty
$$

Now

$$
\begin{aligned}
A_{m} & =\left\{\omega \in \Omega:\left|\omega_{m}(\omega)\right|>m \delta\right\} \\
& =\left\{\omega \in \Omega: \omega_{m}^{2}(\omega)>m^{2} \delta^{2}\right\}
\end{aligned}
$$

where $\omega_{m}^{2}(\omega)$ is piecewise constant and non-negative. using the previoles result it follows that

$$
\mu_{\alpha}\left(A_{m}\right)<\frac{1}{m^{2} \delta^{2}} \int_{0}^{1} \omega_{m}^{2}(\omega) d \omega
$$

using

$$
\omega_{m}(\omega)=\sum_{i=1}^{m} R_{i}(\omega)
$$

where $R_{i}(w)$ is the cth Rademacher function. It follows that

$$
\begin{aligned}
& \int_{0}^{1} \omega_{m}^{2}(\omega) d \omega=\int_{0}^{1}\left(\sum_{i=1}^{m} R_{i}(\omega)\right)^{2} d \omega \\
& =\int_{0}^{1}\left(\sum_{i=1}^{m} R_{i}(\omega)\right)\left(\sum_{j=1}^{m} R_{j}(\omega)\right) d \omega \\
& =\int_{0}^{1}\left(\sum_{i=1}^{m} R_{i}^{2}(\omega)+\sum_{i=1}^{m} \sum_{i \neq j}^{m} R_{i}(\omega) R_{j}(\omega)\right) d \omega \\
& =\sum_{i=1}^{m} \int_{0}^{1} R_{i}^{2}(\omega)+\sum_{i=1}^{m} \sum_{j=1}^{m} \int_{0}^{1} R_{i}(\omega) R_{j}(\omega) d \omega
\end{aligned}
$$

Now for the first term

$$
\begin{aligned}
R_{i}^{2}(\omega) & =\left(2 a_{i}-1\right)^{2} \\
& =4 a_{i}^{2}-4 a_{i}+1 \\
& =4 a_{i}\left(a_{i}-1\right)+1
\end{aligned}
$$

now $a_{i}=\{0,1\}$ thus the first term is zero

It follows that,

$$
R_{i}^{2}(\omega)=1
$$

so the first term becomes

$$
\begin{aligned}
\sum_{i=1}^{m} \int_{0}^{1} R_{i}^{2}(\omega) d \omega & =\sum_{i=1}^{m} \int_{0}^{1} d \omega \\
& =\sum_{i=1}^{m} 1 \\
& =m
\end{aligned}
$$

For the second term consider the integral

$$
\int_{0}^{1} R_{i}(\omega) R_{j}(\omega) d \omega
$$

without loss of generality assume that $i<j$. Now $R_{i}(\omega)= \pm 1$ on the intervals

$$
L=\left(\frac{l}{2^{i}}, \frac{l+1}{2^{i}}\right]
$$

Where $l=0,1,2, \cdots 2^{i}-1$ and
$R_{i}(\omega)=1$ for $l=$ odd number and $R_{i}(\omega)=-1$ for $l=$ even number.

Similarly $R_{j}(\omega)= \pm 1$ on the intervals

$$
\left(\frac{k}{2^{j}}, \frac{k+1}{2^{j}}\right]
$$

The width of the intervals defining $R_{i}(\omega)$ is $2^{-i}$ and the intervals defining $R_{j}(\omega)$ is given by $2^{-1}$ since it is assumed that $i<j$ it follows that the number of $R_{j}(\omega)$ intervals within one $R_{i}(\omega)$ interval is given by

$$
\frac{2^{-i}}{2^{-j}}=2^{j-1}
$$

The following diagram illustrates the nesting of intervals for $R_{1}(\omega)$ to $R_{5}(\omega)$.
$R_{1}(\omega)$
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-048.jpg?height=118&width=1014&top_left_y=163&top_left_x=403)
$R_{2}(\omega)$
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-048.jpg?height=178&width=1022&top_left_y=292&top_left_x=403)
$R_{3}(\omega)$
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-048.jpg?height=164&width=1020&top_left_y=485&top_left_x=403)
$R_{4}(\omega)$
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-048.jpg?height=166&width=1022&top_left_y=677&top_left_x=399)
$R_{5}(\omega)$

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| -1 | 1 | -1 | 1 | -1 | 1 | -1 | -1 | 1 | -1 | 1 | -1 | 1 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | $1 / 2$ |  |
| 0 | $1 / 16$ | $1 / 8$ | $3 / 16$ | $1 / 4$ | $5 / 16$ | $1 / 8$ | $1 / 16$ | $1 / 2$ |  |  |  |  |

It is seen that for a given $R_{i}(\omega) R_{j}(\omega)$ will oscilate between -1 and $12^{j-1}$ times which is even. It follows that for a given interval

$$
L=\left(\frac{l}{\partial^{i}}, \frac{l+1}{\partial^{i}}\right]
$$

with $k=0,1,2, \cdots, 2^{j-i}-1$ the intervals for $R_{j}(\omega)$ within a single $R_{i}(\omega)$ interval are given
by

$$
\left(\frac{l}{2^{i}}+\frac{k}{2^{j}}, \frac{l}{2^{i}}+\frac{k+1}{2^{j}}\right]
$$

Checking $k=0$ and $k=2^{j-i}-1$ gives the expected results

$$
\begin{aligned}
& \left(\frac{l}{2^{i}}, \frac{l}{2^{i}}+\frac{1}{2^{j}}\right] \\
& \left(\frac{l}{2^{i}}+\frac{2^{j-i}-1}{2^{j}}, \frac{l}{2^{i}}+\frac{2^{j-1}-1}{2^{j}}\right] \\
= & \left(\frac{l}{2^{i}}+\frac{1}{2^{i}}-\frac{1}{2^{j}}, \frac{l}{2^{i}}+\frac{1}{2^{i}}\right] \\
= & \left(\frac{l+1}{2^{i}}-\frac{1}{2^{j}}, \frac{l+1}{2^{i}}\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& \int_{0}^{1} R_{i}(\omega) R_{j}(\omega) d \omega \\
& =\sum_{l=0}^{\frac{2 i}{2}-1} \sum_{k=0}^{j-i-1} \int_{\frac{l}{2 i}+\frac{k}{2 j}}^{\frac{l}{2 i}+\frac{k+1}{2 j}} R_{i}(\omega) R_{j}(\omega) d \omega
\end{aligned}
$$

The first sum is over the $R_{i}(\omega)$ intervals and the second is over the $R_{j}(\omega)$ intervals.
As an example consider $i=1$ and $j=2$ then

$$
\begin{aligned}
& \int_{0}^{1} R_{1}(\omega) R_{2}(\omega) d \omega \\
&=\sum_{l=0}^{1} \sum_{k=0}^{1} \int_{\frac{l}{2}+\frac{k}{4}}^{\frac{l}{4}+\frac{k+1}{4}} R_{1}(\omega) R_{2}(\omega) d \omega \\
&=\sum_{l=0}^{1} {\left[\int_{\frac{l}{2}}^{\frac{l}{2}+14} R_{1}(\omega) R_{2}(\omega) d \omega\right.} \\
&\left.\quad \int_{\frac{l}{2}+\frac{l}{2}+\frac{1}{4}} R_{1}(\omega) R_{2}(\omega) d \omega\right]
\end{aligned}
$$

For a fixed value of $\& R_{1}(\omega)$ is constant so the integral becomes

$$
\begin{aligned}
& \sum_{l=0}^{1}[ R_{1}(\omega) \int_{\frac{l}{2}}^{\frac{l}{2}+\frac{l}{4}} R_{2}(\omega) d \omega \\
&+R_{1}(\omega) \int_{\frac{l}{2}+\frac{l}{4}}^{\frac{l}{2}+\frac{1}{2}} R_{2}(\omega) d \omega \\
&=\sum_{l=0}^{1} R_{1}(\omega)\left[\int_{\frac{l}{2}}^{\frac{l}{2}+\frac{l}{4}} R_{2}(\omega) d \omega\right. \\
&\left.+\int_{\frac{l}{2}+\frac{l}{4}}^{\frac{l}{2}+\frac{l}{2}} R_{2}(\omega) d \omega\right]
\end{aligned}
$$

Now,
$R_{2}(\omega)= \begin{cases}-1 & \omega \in\left(\frac{l}{2}, \frac{l}{2}+\frac{1}{4}\right] \\ 1 & \omega \in\left(\frac{l}{2}+\frac{1}{4}, \frac{l}{2}+\frac{1}{2}\right]\end{cases}$
and

$$
d \omega=\frac{1}{4}
$$

it follows that,

$$
\begin{aligned}
& \sum_{\frac{l}{2}}^{l}+\frac{1}{4} \\
& =-1 / 4+1 / 4=0
\end{aligned}
$$

and thus

$$
\int_{0}^{1} R_{1}(\omega) R_{2}(\omega) d \omega=0
$$

The pattern follows for arbitrary $i$ and $j$. For a fired $l$ Ri $(\omega)$ will have a constant value of 1 or -1 and $R_{j}(\omega)$ will go through an coen number of cycles and the integrals will sum to zero. In general the the integral is given by,

$$
\begin{aligned}
& \sum_{k=0}^{2^{j-i}-1} \int_{\frac{l}{2 i}+\frac{k}{2 j}}^{\frac{l}{2 i}+\frac{k+1}{2 j}} R_{j}(\omega) d \omega=\int_{\frac{l}{2 i}}^{\frac{l}{2 i}+\frac{1}{2^{j}}} R_{i}(\omega) d \omega \\
& +\int_{\frac{l}{2 i}+\frac{2}{2^{j}}} R_{i}(\omega) d \omega+\int_{\frac{l}{2 j}}^{\frac{l}{2 i}+\frac{3}{2^{j}}} R_{i}(\omega) d \omega \\
& +\int_{\frac{l}{2 j}}^{\frac{l}{2 i}+\frac{4}{2^{j}}} R_{i}(\omega) d \omega+\cdots+\int_{\frac{l}{2 j}} \int_{\frac{l+1}{2 i}-\frac{1}{2 j}} R_{i}(\omega) d \omega \\
& +\int^{\frac{l}{2 j}} \\
& +\frac{l+1}{2^{j}} R_{i}(\omega) d \omega \\
& =-\frac{1}{2^{j}} \\
& =-\frac{1}{2^{j}}+\frac{1}{2^{j}}-\frac{1}{2^{j}}+\frac{1}{2^{j}}+\cdots-\frac{1}{2^{j}}+\frac{1}{2^{j}} \\
& =0+0+\cdots+0=0
\end{aligned}
$$

$$
\int_{0}^{1} R_{1}(\omega) R_{2}(\omega) d \omega=0
$$

Putting things together gives

$$
\begin{aligned}
& \int_{0}^{1} w_{m}^{2}(w) d w=\sum_{i=1}^{m} \int_{0}^{1} R_{i}^{2}(w) \\
& +\sum_{i=1}^{m} \sum_{i \neq j}^{m} \int_{0}^{1} R_{i}(w) R_{j}(w) d w \\
& =m
\end{aligned}
$$

This is interesting since it is the same result as obtained for a weiner process
The final result of proving the weak law of large numbers for the Bernoulli sequence which states that in the limit of an infinite number of tosses
that half are heads. This is stated in the following manner.
The event where the number of heads is greater than the number of tails after $m$ tosses by a fractional amount $\delta$ is given by
$I_{\delta m}=\left\{\omega \in \Omega:\left|\frac{S_{m}(\omega)}{m}-\frac{1}{2}\right|>\delta\right\}$
where $s_{m}(w)$ is the number of heads for a given $w$.
The weak law of large numbers states that as $m \rightarrow \infty$

$$
\mu_{2}\left(I_{\delta m}\right) \rightarrow 0
$$

using Rademacher function $R_{i}(\omega)$

$$
\omega_{m}(\omega)=\sum_{i=1}^{m} R_{i}(\omega)=2 S_{m}(\omega)-1
$$

Using $\omega_{m}(\omega)$ Ism can be convered to

$$
\begin{gathered}
A_{m}=\left\{\omega \in \Omega: \omega_{m}^{2}(\omega)>m^{2} \delta^{2}\right\} \\
\mu_{z}\left(A_{m}\right) \rightarrow 0 \text { as } m \rightarrow \infty
\end{gathered}
$$

Using the following theorem, which was previously proven
$\frac{1}{\alpha} \int_{0}^{1} f(\omega) d \omega>\mu_{\alpha}(\xi \omega \in \Omega: f(\omega)>\alpha \xi)$
It follows that to prove that Bernaulli sequences have equal probabilitues of a toss of heads or tails the following expression must be considered

$$
\mu_{\alpha}\left(A_{m}\right)<\frac{1}{m^{2} \delta^{2}} \int_{0}^{1} w_{m}^{2}(w) d w
$$

usins

$$
\int_{0} w_{m}^{2}(w) d w=m
$$

sives

$$
\mu_{1}\left(A_{m}\right)<\frac{1}{m \delta^{2}}
$$

since $b_{1}$ definition $\mu_{2}\left(A_{m}\right)>0$, it follows that as $m \rightarrow \infty$

$$
\mu_{\mathcal{L}}\left(A_{m}\right) \rightarrow 0
$$

which proves that for a Bernoulli sequence that It and T have equal probabities of occuring satisfying the weak law of large numbers.
In the following section it will be seen that $\mu_{1}\left(A_{m}\right)$ is a set of measure zero.

## Lebesgue Measure Zerd

An event in the Bernoulli sequence $B$ has probability zerd if the interoal of real numbers in $\Omega$ that the event maps to has lebesque measure zero.
In this section details of what lebesque measure zero means are discussed. To proceede the idea of a countable cover needs to be understood.

## Definition: Countoble Cover

Given a subset $A \subset \mathbb{R}^{n}$ a countable cover of $A$ is a countable collection of sets $\left\{A_{i}\right\}_{i=1}^{\infty}$ in $\mathbb{R}^{n}$ such that

$$
A \subset \bigcup_{i=1}^{\infty} A_{i}
$$

If the sets in a countable caver are open the cover is called
an open cover.
The following is a coutable cover of $\mathbb{R}^{S}$

$$
R \subset \bigcup_{i=0}^{\infty}((i-k / 4, i+1+k / 4) \cup(-i-1-k / 4,-i+4 / 4))
$$

The lengths of the intervals are equal and independent of: For the left torm

$$
i+1+14-i+1 / 4=1+1 / 2=3 / 2
$$

and for the right term

$$
-i+141+i+1+114=1+1 / 2=32
$$

Also, note that successive terms on the right and left overlap. For the left terms

$$
\begin{aligned}
& (i-1 / 4, i+1+1 / 4) \cap(i+1-1 / 4, i+1+1+1 / 4) \\
= & (i-1 / 4, i+5 / 4) \cap(i+3 / 4, i+9 / 4) \\
= & {[i+3 / 4, i+5 / 4] \quad i=0,1,2, \ldots }
\end{aligned}
$$

and similarly for the righthand side

$$
\begin{aligned}
& (-i-1-1 / 4,-i+14) \cap(-(i+1)-1-1 / 4,-(i+1)+k)) \\
= & (-i-5 / 4,-i+1 / 4) \cap(-i-9 / 4,-i-3 / 4) \\
= & {[-i-5 / 4,-i-3 / 4] }
\end{aligned}
$$

The length of the right and left successive overlar is the same and equal to $1 / 2$. consider a faw terms

$$
\begin{aligned}
& i=0 \underset{-2}{1} \underset{-1}{(1)} \underset{0}{(1)} \underset{2}{\longrightarrow} \mathbb{R} \\
& (-1 / 4,5 / 4) \cup(-5 / 4,1 / 4)=(-5 / 4,5 / 4) \\
& \tau=1 \longleftrightarrow t_{1} \cdots t_{-2} t_{1} t_{1} t_{2} \longrightarrow \mathbb{R} \\
& (3 / 4,9 / 4) \cup(-9 / 4,-3 / 4)
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-061.jpg?height=152&width=1152&top_left_y=133&top_left_x=173)

$$
(7 / 4,13 / 4) \cup(-3 / 4,-7 / 4)
$$

Now the left term covers $\mathbb{R}^{+}$ and the right term covers $\mathbb{R}^{-}$ and since the left and right terms overlap for $i=\Delta$ it follows that for every $r \in \mathbb{R}$ there will be some $i$ such the $r$ is contained be either the left or right interval or both, thus
$R \subset \bigcup_{i=0}^{\infty}((i-k / 4, i+1+k / 4) \cup(-i-1-k / 4,-i+k / 4))$
Definition: Lebesgue Measure Zero
For $A \subset R, A$ has lebesgue Measure zero if for every $\varepsilon>0$ there exists a contable cover $\left\{A_{i}\right\}_{i=0}^{\Delta}$ of A where each A consists of a finite union of spen intervals
such that

$$
\mu(A)<\sum_{i=1}^{\infty} \mu_{\alpha}\left(A_{i}\right)<\varepsilon
$$

It is said that $A$ has measure zero.

Example: Natural Numbers have Measure Zero

Consider the cover of the Natural numbers, $N$, Consider the open cover of $\mathbb{N}$

$$
\mathbb{N} \subset \bigcup_{i=0}^{\infty}\left(i-\frac{\varepsilon}{2^{i+2}}, i+\frac{\varepsilon}{2^{i+2}}\right)
$$

where $\varepsilon>0$. It follows that

$$
\begin{aligned}
& \mu_{z}\left(\bigcup_{i=0}^{\infty}\left(i-\frac{\varepsilon}{2^{i+2}}, i+\frac{\varepsilon}{2^{i+2}}\right)\right) \\
= & \sum_{i=0}^{\infty} \mu_{z}\left(\left(i-\frac{\varepsilon}{2^{i+2}}, i+\frac{\varepsilon}{2^{i+2}}\right)\right) \\
= & \sum_{i=0}^{\infty}\left(i+\frac{\varepsilon}{2^{i+2}}-i+\frac{\varepsilon}{2^{i+2}}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\sum_{i=0}^{\infty} \frac{\varepsilon}{2^{i+1}}=\frac{\varepsilon}{2} \sum_{i=0}^{\infty} \frac{1}{2^{i}} \\
& =\frac{\varepsilon}{2} \frac{1}{1-1 / 2}=\frac{\varepsilon}{2}(2)=\varepsilon
\end{aligned}
$$

Thus

$$
\mu_{\alpha}\left(\bigcup_{i=0}^{\infty}\left(i-\frac{\varepsilon}{2 i+2}, i+\frac{\varepsilon}{2 i+2}\right)\right)=\varepsilon
$$

since $\varepsilon$ is arbitrary it follows that $N$ has measure zero.

Definition: Lebesgue Measure is monotone
Consider the intervals

$$
(c, d) \subset(a, b)
$$

This relation implies that

$$
a<c<b, a<d<b, c<d
$$

it follows that

$$
d-c<a-b
$$

$\Rightarrow \mu_{\alpha}((c, d))<\mu_{\alpha}((a-b))$
This relation is stated as the Lebesgue measure is monotone.
Theorem : Measure of subset of set of Measure zero

A measurable subset of a set of a set of measure zero has measure zero.

## Proof

This result follows from the definition of a set with measure zero. Recall that a set has measure zero if for $A \subset \mathbb{R}$ a contable cover of $A$ given $b_{1}\left\{A_{i}\right\}_{i=0}^{\infty}$ exists, where

$$
A C \bigcup_{i=0}^{\infty} A_{i}
$$

and

$$
\sum_{i=0}^{\infty} \mu_{z}\left(A_{i}\right)<\varepsilon
$$

where $\varepsilon>0$ and arbitrary
If $B \subset A$ then

$$
B \subset A C \bigcup_{i=0}^{\infty} A_{i}
$$

since measure is monotone it follows that

$$
\mu_{\mathcal{I}}(B)<\mu_{\mathcal{L}}(A)<\sum_{i=0}^{\Delta} \mu_{\mathcal{l}}\left(A_{i}\right)<\varepsilon
$$

Thus $B$ has measure zero.

Theorem : A countable union of sets with measure zero has measure zero.
Proof
Let $\left\{A_{i}\right\}_{i=0}^{\infty}$ be a countable collectcollection of sets each of measure zero. Since $A_{i}$ has measure zero a countable
of sets $\left\{B_{i j}\right\}_{j=0}^{A}$ exists such that

$$
A_{i} \subset \bigcup_{j=0}^{\infty} B_{i j}
$$

where for $\varepsilon>0$ and arbitrary

$$
\mu\left(A_{i}\right)<\sum_{j=0}^{\infty} \mu_{j}\left(B_{i j}\right)<\frac{\varepsilon}{2^{i+1}}
$$

It follows that
$\mu_{\alpha}\left(\vec{U}_{i=0}^{\infty} A_{i}\right)=\sum_{i=0}^{\infty} \mu_{\alpha}\left(A_{i}\right)$

$$
\begin{aligned}
& <\sum_{i=0}^{\infty} \sum_{j=0}^{\infty} \mu_{j}\left(B_{i j}\right) \\
& <\sum_{c=0}^{\infty} \frac{\varepsilon}{\partial^{c+1}}=\frac{\varepsilon}{2} \sum_{i=0}^{\infty} \frac{1}{\partial^{c}} \\
& =\varepsilon
\end{aligned}
$$

Thus $\bigcup_{i=0}^{\infty} A_{i}$ has measure zero

Theorem : Any finite or cantable set of numbers has measure zero.
Proof
Recall that a point on the number line has measure zero. Now any finite or countable set of numbers is a union of points. It follows from the previous theorem that any fonite or countable set of numbers has zero measure.

## Cantor set

In the previous section examples of sets of measure zero were discused. Here the cantor set is discussed. It is ofter used as an example of a set with zero measure. The set is constructed from an iterative process. Smilar proceedwes can be used to construct other sets.

The cantor set is constructed by iteratively dividing the interval $[0,1]$. If the ith step in the process is denoted by $C_{i}$ and the intial tep is given by

$$
C_{0}=[0,1]
$$

the first step is given by dividing $[0,1]$ into thirds an demouing the middle open interval

$$
c_{1}=[0,1 / 3] \cup[2 / 3,1]
$$

The second step performs the same proceedure on the two intervals from step 1.
$C_{2}=[0,1 / q] \cup[2 / q, 1 / 3] \cup[2 / 3,7 / q] \cup[8 / q, 1]$
and the same for step 3.

$$
\begin{aligned}
c_{3}= & {[0,1 / 27] \cup[2 / 27,1 / 9] \cup[2 / 9,7 / 27] \cup[8 / 27,1 / 3] \cup } \\
& {[2 / 3,19 / 27] \cup\left[20 \sigma_{7}, 7 / 9\right] \cup[8 / 9,25 / 27] \cup } \\
& {[20 / 27,1] }
\end{aligned}
$$

It is seen that the number of closed intervals after the ith step is given by

$$
n_{i}=2^{i}
$$

and the length of each intorval after the ith step is given by

$$
l_{i}=\frac{1}{3} i
$$

The following diagram illustrates the proceedure graphically
$\mathrm{C}_{0} \square \longrightarrow$
$c_{1}: c_{1 / 3}^{1}: 2 / 3 \quad$,
$\begin{array}{lllllllll}C_{2} & 0 & 1 / 9 & 2 / 9 & 1 / 3 & 4 / 9 & 5 / 9 & 2 / 3 & 6 / 7 \\ & 1 / 9 & & 1\end{array}$
$\begin{array}{llllllll}C_{3} & & 1 / 9 & 2 / 9 & 1 / 3 & 4 / 9 & 5 / 9 & 2 / 3 \\ & 0 & 6 / 7 & 7 / 9\end{array} \vdots$

Now the open set removed at each interation of the construction proceedure is given by

1) $(4 / 3,2 / 3)$
2) $(1 / 3,2 / 3) \cup(1 / 9,219) \cup(7 / 9,8 / 9)$
3) $(1 / 3,2 / 3) \cup(1 / 2,2 / 9) \cup(7 / 9,8 / 9)$
$U(1 / 27,2 / 27) \cup(7 / 27,8 / 27) \cup\left(19 / 27,2 q_{7}\right)$
$U(25 / 27,26 / 27)$
A closed form for $c_{i}$ as a union of open intervals can be obtained by considering

$$
\bigcup_{n=0}^{i-1} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)
$$

For $i=1$

$$
\bigcup_{n=0} \bigcup_{k=0}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)=(1 / 3,21 / 3)
$$

For $i=2$

$$
\begin{aligned}
& \bigcup_{n=0} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right) \\
& =\bigcup_{k=0}^{0}\left(\frac{3 k+1}{3}, \frac{3 k+2}{3}\right) \bigcup_{k=0}^{2}\left(\frac{3 k+1}{9}, \frac{3 k+2}{9}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & (1 / 3,2 / 3) \cup(1 / 9,2 / 9) \cup(4 / 9,5 / 9) \\
& \cup(7 / 9,8 / 9)
\end{aligned}
$$

$$
\begin{aligned}
= & (1 / q, 2 / q) \cup(1 / 3,2 / 3) \cup(4 / q, 5 / q) \\
& \cup(7 / q, 8 / q)
\end{aligned}
$$

but

$$
\begin{aligned}
(1 / 3,2 / 3) \cup(4 / 9,5 / 9) \\
=(3 / 9,6 / 9) \cup(4 / 9,5 / 9) \\
=(3 / 9,6 / 9)=(43,2 / 3)
\end{aligned}
$$

Thus

$$
\begin{aligned}
& \bigcup_{n=0}^{1} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right) \\
& =(1 / q, 21 q) \cup(1 / 3,2 / 3) \cup(7 / q, 8 / q)
\end{aligned}
$$

and forally consider $L=3$
$\bigcup_{n=0}^{2} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)$
$=\bigcup_{k=0}^{0}\left(\frac{3 k+1}{3}, \frac{3 k+2}{3}\right) \bigcup_{k=0}^{2}\left(\frac{3 k+1}{9}, \frac{3 k+2}{9}\right)$
$\sum_{k=0}^{8}\left(\frac{3 k+1}{27}, \frac{3 k+2}{27}\right)$
$=(19,219) \cup(43,213) \cup\left(71 q^{(3)}, 81 q\right) \cup$
$\left(b_{7}, a_{27}\right) \cup\left(a_{27}, 5_{27}\right) \cup\left(a_{27}, 8_{27}\right) \cup$
$(10127 \times 11 / 27) \cup\left(13 l_{27}^{2}, 14 / 27\right) \cup\left(1 \log _{27}, 1 l_{27}\right)$
$U\left(19 a_{7}, 20 a_{7}\right) \cup\left(22 a_{7} q^{8}, 23 a_{7}\right) \cup$ ( $25 /_{27}, 2 a_{27}$ )

Now

$$
(49,219)=(3 / 27,6 / 27)
$$

so

$$
(1 / q, 2 / q) \cup(4 / 27,5 / 27)=(1 / q, 2 / q)
$$

and

$$
(43,23)=(9 / 27,18 / 27)
$$

50

$$
\begin{aligned}
& (1 / 3,213) \cup(10127,1427) \cup(337,14127) \cup \\
& (16 / 27,17127)=(1 / 3,213)
\end{aligned}
$$

and finally

$$
(71 q, 81 q)=(21 / 27,24127)
$$

so

$$
(71 q, 81 q) \cup(22127,23 / 27)=(7 / q, 8 / q)
$$

It follows that
$\bigcup_{n=0}^{2} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)$

$$
\begin{aligned}
= & (1 / 27,2 / 27) \cup(1 / 9,2 / 9) \cup\left(7 / 27,8 l_{27}\right) \cup \\
& \left(1 / 3,2 l_{3}\right) \cup\left(19 l_{27}, 20 l_{27}\right) \cup\left(7 q_{1}, 8(9) \cup\right. \\
& \left(25 / 27,26 l_{27}\right)
\end{aligned}
$$

Thus the removed intervals for the i'th step in construction of the set is given by

$$
\bigcup_{n=0}^{i-1} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)
$$

It follows that for $i>0 \mathrm{ci}$ has the closed form

$$
C_{i}=[0,1] / \bigcup_{n=0}^{i-1} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)
$$

$C_{i}$ also has a closed form that is a which of closed intervals. consider
$\bigcap_{j=1}^{i} \bigcup_{k=0}^{j s-1}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right)$
For $i=1$
$\bigcap_{j=1}^{\prime} \bigcup_{k=0}^{0}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right)$

$$
=[0,1 / 3] \cup[2 / 3,1]
$$

For $j=2$

$$
\begin{aligned}
\cup_{k=0}^{2}\left(\left[\frac{3 k}{3^{2}}, \frac{3 k+1}{3^{2}}\right] \cup\left[\frac{3 k+2}{3^{2}}, \frac{3 k+3}{3^{2}}\right]\right) \\
= \\
{[0,1 / q] \cup[2 / q, 3 / q] \cup[3 / q, 4 / q] \cup } \\
{[5 / q, 6 / q] \cup[6 / q, 7 / q] \cup[8 / q, 1] } \\
=[0,1 / q] \cup[2 / q, 1 / 3] \cup[1 / 3,4 / q] \cup \\
{[5 / q, 2 / 3] \cup[2 / 3,7 / q] \cup[8 / q, 1] }
\end{aligned}
$$

and for $c=2$

$$
\begin{aligned}
\bigcap_{j=1}^{2} & \bigcup_{k=0}^{0}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right) \\
= & ([0,1 / 3] \cup[2 / 3,1]) \cap([0,1 / 9] \cup \\
& {[2 / 9,1 / 3] \cup[1 / 3,4 / 9] \cup[5 / 9,2 / 3] \cup } \\
& {[2 / 3,7 / 9] \cup[8 / 9,1]) }
\end{aligned}
$$

$$
=[0,1 / 9] \cup[2 / 9,1 / 3] \cup[2 / 3,7 / 9] \cup[8 / 9,1]
$$

thus
$c_{i}=\bigcap_{j=1}^{i} \bigcup_{k=0}^{3^{j}-1}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right)$

A recursive relation for $C_{i}$ is given by

$$
C_{i}=\frac{C_{i-1}}{3} \cup\left(\frac{2}{3}+\frac{C_{i-1}}{3}\right)
$$

Consider the case $i=1$ using

$$
C_{0}=[0,1]
$$

gives

$$
\begin{aligned}
c_{1} & =\frac{1}{3}[0,1] \cup\left(\frac{2}{3}+\frac{[0,1]}{3}\right) \\
& =[0,1 / 3] \cup[2 / 3,1]
\end{aligned}
$$

$$
\begin{aligned}
C_{2}= & \frac{1}{3}([0,1 / 3] \cup[2 / 3,1]) \cup \\
& \left(\frac{2}{3}+\frac{1}{3}[0,1 / 3] \cup[2 / 3,1]\right) \\
= & ([0,1 / 9] \cup[2 / 9,1 / 3]) \cup \\
& ([2 / 3,1 / 9] \cup[8 / 9,1]) \\
= & {[0,1 / 9] \cup[2 / 9,1 / 3] \cup[2 / 3,7 / 9] \cup } \\
& {[8 / 9,1] }
\end{aligned}
$$

and finally consider

$$
\begin{aligned}
C_{3}= & \frac{1}{3}([0,1 / 9] \cup[2 / 9,1 / 3] \cup[2 / 7 / 9] \cup \\
& {[8 / 9,1]) \cup\left(\frac{2}{3}+\frac{1}{3}[0,1 / 9] \cup\right.} \\
& {[2 / 9,1 / 3] \cup[2 / 7 / 9] \cup[8 / 9,1]) } \\
= & {[0,1 / 27] \cup[2 / 7,1 / 9] \cup[2 / 9,37] \cup } \\
& {[8 / 27 / 3] \cup\left[2 / 3,1 q_{2}\right] \cup\left[2 q_{2}, 2 q_{2}\right] \cup }
\end{aligned}
$$

$$
\left[x / 1_{27}, 25 / 27\right] \cup\left[\partial \%_{27}, 1\right]
$$

Let the collection of sets producer after the ith step of this proceedure be denoted by

$$
\left\{c_{i}\right\}_{i=0}^{\infty}
$$

Let $\mathbb{C}$ denote the cantor middle third set where,

$$
\begin{gathered}
\mathbb{C}=\bigcap_{i=1}^{\infty} C_{i} \\
C_{i}=\frac{C_{i-1}}{3} \cup\left(\frac{2}{3}+\frac{C_{i-1}}{3}\right)
\end{gathered}
$$

Using the other expressions for $c_{i}$ gives

$$
\mathbb{C}=[0,1] / \bigcup_{n=0}^{\infty} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right)
$$

and

$$
\mathbb{C}=\bigcap_{j=1}^{\infty} \bigcup_{k=0}^{3^{j-1}}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right)
$$

## Perfect Sets

Analysis of the cantor set requires other set theory concepts, such as perfect sets. Here the concepts are reviewed.

Definition: Limit of a sequence consider the sequence,

$$
\left\{x_{n}\right\}_{n \in \mathbb{N}}
$$

where $x_{n} \in \mathbb{R}$ and $n \in \mathbb{N} x$ is the limit of the sequence if the following condition holds. For every real number $\varepsilon>0$ there exists a natural number
$N \in \mathbb{N}$ such that for every $n>N$

$$
\left|x-x_{n}\right|<\varepsilon
$$

This is denoted by,

$$
x_{n} \rightarrow x \text { cs } n \rightarrow \infty
$$

$$
\begin{array}{r}
\lim _{n \rightarrow \infty} x_{n}=x \\
x=\left\{x_{n}\right\}_{n=1}^{\infty}
\end{array}
$$

symbolically the definition can be writen

$$
\begin{array}{r}
\forall \varepsilon>0, \exists N \in \mathbb{N} \text { such that } \\
\forall n>N \Rightarrow\left|x-x_{n}\right|<\varepsilon
\end{array}
$$

Theorem : A monotone bounded sequence of real numbers converges in $\mathbb{R}$

## Proop

Consider the real sequence

$$
\left\{x_{n}\right\}_{n=1}^{\infty} \in \mathbb{R}
$$

be monotone and bounded Since $\left\{x_{n}\right\}_{n=1}^{\infty}$ is monotone first assume that it is increasing so that

$$
x_{n} \geqslant x_{m} \Rightarrow n>m
$$

and since $\left\{x_{n}\right\}$ is bounded let

$$
x=\sup _{n \in \mathbb{R}}\left(x_{n}\right)
$$

It will be shown that

$$
x_{n} \rightarrow x \text { as } n \rightarrow \infty
$$

Let $\varepsilon>0$ then

$$
x-\varepsilon<x=\sup _{n \in \mathbb{N}}\left(x_{n}\right)
$$

since $\left\{x_{n}\right\}$ is increasing there must be some $N \in \mathbb{N}$ such that

$$
x-\varepsilon<x_{N}<x
$$

then for every $n>N$

$$
\begin{aligned}
& x-\varepsilon<x_{N}<x_{n}<x \\
\Rightarrow & x-\varepsilon<x_{n} \\
\Rightarrow & \left|x-x_{n}\right|<\varepsilon \quad \forall n>N
\end{aligned}
$$

From the defuntion of the limit of a sequence it
follows that

$$
x_{n} \rightarrow \sup _{n \in \mathbb{N}}\left(x_{n}\right)
$$

as $n \rightarrow \infty$
Similarly assume that $\left\{x_{n}\right\}$ is decreasing. It follows that $\left\{-x_{n}\right\}$ is increasing. From the previous result it follows that

$$
-x_{n} \rightarrow \sup _{n \in \mathbb{N}}\left(-x_{n}\right)
$$

Now

$$
\sup _{n \in \mathbb{N}}\left(-x_{n}\right)=-\inf _{n \in \mathbb{N}}\left(x_{n}\right)
$$

thus for $n \rightarrow \infty$

$$
\begin{aligned}
&-x_{n} \rightarrow-\inf _{n \in \mathbb{N}}\left(x_{n}\right) \\
& \Rightarrow \quad x_{n} \rightarrow \inf _{n \in \mathbb{N}}\left(x_{n}\right)
\end{aligned}
$$

Theorem : Nested Interval Theorem consider the sequence of closed bounded and non empty intervals in $\mathbb{R}$ denoted by

$$
\left\{I_{n}\right\}_{n=1}^{\infty}
$$

where $I_{n}$ are nested so that.

$$
I_{1} \supseteq I_{2} \supseteq I_{3} \supseteq \cdots
$$

Since $I_{n} \neq \varnothing$ for $\forall n$ it follows that

$$
\bigcap_{n=1}^{\infty} I_{n} \neq \phi
$$

If it is additionaly assumed that

$$
\mu_{\alpha}\left(I_{n}\right) \rightarrow 0 \text { as } n \rightarrow \infty
$$

Then

$$
\bigcap_{n=1}^{\infty} I_{n}
$$

consists of a single point.

## Proof

Let $I_{n}=\left[a_{n}, b_{n}\right] \Rightarrow a_{n}<b_{n}$ and since

$$
I_{n} \supseteq I_{n+1}
$$

it follows that

$$
a_{n} \leqslant a_{n+1} \leqslant b_{n+1} \leqslant b_{n}
$$

The nesting of intervals is illustrated bellow
$I_{1}$
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-086.jpg?height=118&width=1087&top_left_y=1116&top_left_x=296)
$I_{2}$

$$
a_{2} \quad b_{2}
$$

$I_{3}$

$$
\vec{a}_{3} \quad \vec{b}_{3}
$$

$I_{n}$

$$
a_{n} b_{n}
$$

It follows that $\left\{a_{n}\right\}_{n=1}^{\infty}$ is an increasing monotone sequence and $\left\{b_{n}\right\}_{n=1}^{\infty}$ is a decreasing monotone sequence.
From the previous theorem it follows that

$$
\begin{aligned}
& a=\lim _{n \rightarrow \infty} a_{n}=\sup _{n \in \mathbb{N}}\left(a_{n}\right) \\
& b=\lim _{n \rightarrow \infty} b_{n}=\inf _{n \in \mathbb{N}}\left(b_{n}\right)
\end{aligned}
$$

where $a \leqslant b$. Now it must be that

$$
\bigcap_{n=1}^{\infty} I_{n}=[a, b]
$$

To prove this assume that

$$
x \in \bigcap_{n=1}^{\infty} I_{n}
$$

it follows that $x \in \operatorname{In}$ for every $n \in \mathbb{N}$ so $a_{n} \leqslant x \leqslant b_{n}$ for every $n \in \mathbb{N}$ and finally $a \leqslant x \leqslant b$.

Converstey if $a \leqslant x \leqslant b$ then $a_{n} \leqslant x \leqslant b_{n}$ for every $n$ thus $x \in I_{n}$ for every $n$ and

$$
x \in \bigcap_{n=1}^{\infty} I_{n}
$$

Thus

$$
\bigcap_{n=1}^{\infty} I_{n}=[a, b]
$$

where

$$
I_{n}=\left[a_{n}, b_{n}\right]
$$

and

$$
a=\sup _{n \in \mathbb{N}}\left(a_{n}\right) \quad b=\inf _{n \in \mathbb{N}}\left(b_{n}\right)
$$

Finally if,

$$
\begin{aligned}
& \lim _{n \rightarrow \infty} \mu_{j}\left(I_{n}\right) \rightarrow 0 \\
\Rightarrow & \lim _{n \rightarrow \infty} b_{n}-a_{n} \rightarrow 0 \\
\Rightarrow & a_{n} \rightarrow b_{n} \\
\Rightarrow & a=b
\end{aligned}
$$

Thus the final result is obtained. If

$$
\lim _{n \rightarrow \infty} \mu_{y}\left(I_{n}\right)=0
$$

Then

$$
\bigcap_{i=1}^{\infty} I_{n}=\{a\}
$$

Definition: Perfect set
$A$ set $P$ is a perfect set if it is empty or if it is a closed set and every point or $P$ is a limit point of $P$.
Examples of perfect sets are

$$
\begin{aligned}
& {[a, b] \quad a<b} \\
& \mathbb{R}(-\infty, a] \quad[a, \infty)
\end{aligned}
$$

The following are examples of sets that are not perfect.
$\mathbb{Q} R \backslash Q(a, b)[a, b] \cup\{c\} \quad b<c$
$\mathbb{Q}$ is not open since if $q \in \mathbb{Q}$ there exists $\varepsilon>0$ such that $|q-\varepsilon|$ contains no rational numbers.
$[a, b] \cup\{c\}$ is nol perfect since $c$ is not a limit point of $[a, b] \cup\{c\}$

## Properties of the Cantor Set

In this section properties of the cantor set are discussed. Previously it was shown that the cantor set is defined by

$$
\begin{gathered}
\mathbb{C}=\bigcap_{i=1}^{\infty} C_{i} \\
C_{i}=\frac{C_{i-1}}{3} \cup\left(\frac{2}{3}+\frac{C_{i-1}}{3}\right) \\
C_{0}=[0,1]
\end{gathered}
$$

and

$$
\begin{array}{r}
\mathbb{C}=[0,1] / \bigcup_{n=0}^{\infty} \bigcup_{k=0}^{3^{n}-1}\left(\frac{3 k+1}{3^{n+1}}, \frac{3 k+2}{3^{n+1}}\right) \\
\mathbb{C}=\bigcap_{j=1}^{\infty} \bigcup_{k=0}^{3^{j-1}}\left(\left[\frac{3 k}{3^{j}}, \frac{3 k+1}{3^{j}}\right] \cup\left[\frac{3 k+2}{3^{j}}, \frac{3 k+3}{3^{j}}\right]\right)
\end{array}
$$

## Theorem $\mathbb{C}$ is closed.

## Proof

The closed interval $[0,1]$ is defined by the compliment of the union of the spen intervals

$$
[0,1]=((-\infty, 0) \cup(1, \infty))^{c}
$$

At the i'th step in the construction process $2^{i-1}$ open intervals are removed from $[0,1]$. Thus each step can be writeh as the compliment of the union of disjoint open sets which is open. From the definition of a dosed set it follows that $c_{i}$ is closed for all $i$.
From DeMorgan's law

$$
\left(\bigcap_{i=0}^{\infty} c_{i}\right)^{c}=\bigcup_{i=0}^{\infty} c_{i}^{c}
$$

$\Rightarrow \mathbb{C}=\bigcap_{i=0}^{\infty} C_{i}=\left(\bigcup_{i=0}^{\infty} C_{i}^{c}\right)^{c}$
since $C_{i}^{c}$ is open and a union of disjoint open sets is open it follows that $\mathbb{C}$ is closed.

Theorem Euery point in $\mathbb{C}$ is a limit of a sequence of points in $\mathbb{C}$

This follows from the previous Theorem that $\mathbb{C}$ is closed. In a previous section it was shown that closed intervals are perfect sets which contain all of their limit points.

Theorem © has measure zero Previously it was shown that the numer of sets for the
ith stop in construction of the cantor set is given by

$$
n_{i}=2^{i}
$$

and the length of each interval after the ith step is given by

$$
l_{i}=\frac{1}{3^{i}}
$$

It follows that the lebesgue measure of each interval after the ith step is given
$1 / 3 i$
Thus

$$
\mu_{\alpha}\left(c_{i}\right)=n_{i} l_{i}=\left(\frac{2}{3}\right)^{i}
$$

It follows that for any $\varepsilon>0$ there exists an $i \in \mathbb{N}$ such that

$$
\left(\frac{2}{3}\right)^{i}<\varepsilon
$$

Trues

$$
\lim _{i \rightarrow \infty} \mu_{\alpha}\left(C_{i}\right)=0
$$

Theorem: $\mathbb{C}$ is uncountable
Now

$$
\mathbb{C}=\bigcap_{i=1}^{\infty} C_{i}
$$

Previously it was shown that the first three stops of the cantor set are given by

$$
\begin{aligned}
C_{0}= & {[0,1] } \\
C_{1}= & {[0,1 / 3] \cup[2 / 3,1] } \\
C_{2}= & {[0,1 / 9] \cup[2 / 9,1 / 3] \cup[2 / 7 / 9] \cup } \\
& {[8 / 9,1] } \\
C_{3}= & {[0,1 / 27] \cup[2 / 27,1 / 9] \cup[2 / 9,37] \cup } \\
& {[87,1 / 3] \cup\left[2 / 3,18 / 27 \cup\left[2 q_{2}, 7 / 9\right] \cup\right.} \\
& {[8 / 9,25 / 27] \cup\left[2 q_{7}, 1\right] }
\end{aligned}
$$

The enpoints of the intervals are given by

$$
\begin{aligned}
E_{0}= & \{0,1\} \\
E_{1}= & \{0,1 / 3,2 / 3,1\} \\
E_{2}= & \{0,1 / 9,219,13,2 / 3,719,819,1\} \\
E_{3}= & \{0,127,21 / 27,19,219,7 / 27,8727,13,213, \\
& 19 / 27,29 / 27,719,819,25 / 27,26 / 27,1\}
\end{aligned}
$$

It is seen that

$$
E_{n} \supset E_{n+1}, \quad E_{n} \subset \mathbb{C}
$$

and that each endpoint of an interval is given by

$$
\frac{a}{3^{n}}
$$

where $a, n \in \mathbb{N}$ and that

$$
\bigcup_{n=0}^{\infty} E_{n} \subset \mathbb{C}
$$

clearly $\bigcup_{n=0}^{\infty} E_{n}$ is countable.
Thus one would expect that $\mathbb{C}$ is countable. It will now be shown that this is not the case by constructing a one-to-one, surfective, mapping

$$
f: c \rightarrow[0,1]
$$

Consider the following diagram
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-097.jpg?height=894&width=1228&top_left_y=973&top_left_x=133)

The green lines show possible
values of $x \in \mathbb{C}$. The closed intervals at each step are identified by $L$, indcating a left interval, and $R$, indicating a right interval. It follows that $x$ will be an element of one interval at each step The value of $x$ can be denoted be sequence of interval choices.

$$
\begin{aligned}
& x_{1}=L R L \ldots \\
& x_{2}=R L R \ldots \\
& x_{3}=R R R \ldots
\end{aligned}
$$

Thus for some $x \in \mathbb{C}$,

$$
x=L R L L R R L L R R \cdots
$$

This is similar to a Berroulli sequence which has cardinality $2^{N}$ which is uncountable.

To construct the mapping consider a base 3 decimal expension

$$
x=\sum_{i=1}^{\infty} \frac{a_{i i}}{3^{i}}
$$

where $a_{i} \in\{0,1,2\}$. Similar to the base 2 expansion previously discussed the representation of numbers is not unique. For example

$$
\frac{1}{3}=0.10000 \ldots
$$

but also

$$
\begin{array}{r}
0.0222222 \cdots=\sum_{i=2}^{\infty} \frac{2}{3^{i}} \\
=\frac{2}{3} \sum_{i=2}^{\infty} \frac{2}{3^{i-1}}=\frac{2}{3} \sum_{i=1}^{\infty} \frac{1}{3^{i}} \\
=\frac{2}{3}\left(\frac{13}{2 / 3}\right)=\frac{1}{3}
\end{array}
$$

Consider

$$
C_{1}=[0,1 / 3] \cup \begin{gathered}
R \\
{[2 / 3,1]}
\end{gathered}
$$

in base 3 this becomes

$$
[0,1 / 3]=[0,0.02222 \cdots]
$$

for the second interval

$$
[2 / 3,1]=[0.2,0.2222 \cdots]
$$

since

$$
\begin{aligned}
& \sum_{i=1}^{\infty} \frac{2}{3^{i}}=2 \sum_{i=1}^{\infty} \frac{1}{3^{i}} \\
& =2(1 / 3 / 2 / 3)=1
\end{aligned}
$$

Now for $c_{2}$

$$
\begin{aligned}
C_{2}= & {[0 / 19] \cup[2 / 9,1 / 3] \cup[2 b / 7 / 9] \cup } \\
& {\left[\begin{array}{l}
8 / 9,1] \\
R R
\end{array}\right.}
\end{aligned}
$$

$$
[0,1 \%]=[0,0.01]
$$

but

$$
0.01=0.00222
$$

so

$$
[0,1 / 9]=[0,0.002222]
$$

for the second interval

$$
[21 q, 1 / 3]=[0.02,0.02222]
$$

and

$$
\left[2_{3}, 7_{9}\right]=[0.2,0.20222 \ldots]
$$

Since

$$
\begin{aligned}
& \frac{7}{9}=\frac{6}{9}+\frac{1}{9}=\frac{2}{3}+\frac{1}{9} \\
& =0.2+0.00222 \\
& =0.202222 .
\end{aligned}
$$

and finally for the last interval

$$
[819,1]=[0.22,0.2222 \ldots]
$$

since

$$
\begin{aligned}
\frac{\delta}{9} & =\frac{6}{9}+\frac{2}{9}=\frac{2}{3}+\frac{2}{9} \\
& =0.22000
\end{aligned}
$$

Bringing things together makes the pattern obvious
$L$
$c_{1}=[0,0.02222] \quad U \quad[0.2,0.2222 \cdots]$
$\left.c_{2}=[0,0.002222] \cup[0.02,0.02222] \cup[0.2,0.20222 \cdots] \stackrel{\text { R }}{\text { R }}\right] \stackrel{\text { R }}{\text { R }}[0.22,0.2222 \cdots]$
If the interval is an $L$ interval on the i'th iteration the ith digit of the decimal expansion is $a O$ and if $i t$ is an $R$ interval the i'th digit is a 2 . It follows that the base 3 representation of $\mathbb{C}$ contains no i's. Thus
If $x \in \mathbb{C}$ then

$$
x=\sum_{i=1}^{\infty} \frac{a_{i}}{3^{i}} \text { where } a_{i} \in\{0,2\}
$$

Now let $2 b_{i}=a_{i}$ where $b_{i} \in\{0,1\}$ then,

$$
x=\sum_{i=1}^{\infty} \frac{2 b_{i}}{3^{i}}
$$

The desired mapping $f: \mathbb{C} \rightarrow[0,1]$ is given by

$$
\begin{aligned}
& f\left[\sum_{i=1}^{\infty} \frac{2 b_{i}}{3^{i}}\right]=\sum_{i=1}^{\infty} \frac{b_{i}}{2^{i}} \\
\Rightarrow & f\left[\partial \sum_{i=1}^{\infty} \frac{b_{i}}{3^{i}}\right]=\sum_{i=1}^{\infty} \frac{b_{i}}{2 i} \\
\Rightarrow & f\left[2\left(0 b_{1} b_{2} b_{3} \cdots\right)_{\text {base } 3}\right]=\left(0 b_{1} b_{2} b_{3} \cdots\right)_{\text {base } 2}
\end{aligned}
$$

This reprents a mapping from $\mathbb{C} \rightarrow B$ and it was previously shown that

$$
\sum_{i=1}^{\infty} \frac{b_{i}}{2 i}
$$

is a one-to-one mapping
from $B \rightarrow[0,1]$. It follows that $\mathbb{C}$ is uncountable.

This result implies that there are points in $\mathbb{C}$ that are not interval end points or it would be countable. A famous example is

$$
\begin{aligned}
& 0.0202020 \\
& =0+\frac{2}{9}+0+\frac{2}{81}+0+\cdots \\
& =\frac{2}{9}+\frac{2}{81}+\frac{2}{729}+\cdots \frac{2}{9^{i}} \\
& =2 \sum_{i=1}^{\infty} \frac{1}{9^{i}} \\
& =2\left(\frac{1 / 9}{819}\right)=\frac{2}{8}=\frac{1}{4}
\end{aligned}
$$

## Definition: Almost Everywhere

A property of sels that holds except on a set of measure zero is said to hold almost every where. It is said that a property holds for almost all points if all points have the property except for points in a set of measure 0 .

Strong law of Large Numbers

For the Bernoulli Sequence B, the number of heads realized in the first $m$ outcomes is given by,

$$
S_{m}(\omega)=\sum_{i=1}^{m} a_{i}
$$

for $\omega=0 . a_{1} a_{2} a_{3}$
The normal numbers are defined by,
$z=\left\{\omega \in \Omega: \frac{S_{m}(\omega)}{m} \rightarrow \frac{1}{2}\right.$ as $\left.m \rightarrow \infty\right\}$
Theorem: The strong law of large Num bers.

The strong law of large number for Bernoulli sequences is stated as,
$2^{c}$ is an uncountable set with zero measure were $z^{c}$ denotes the compliment of $z$.
This version is called strong, in contrast to the previous weak law of large numbers because the weak Law is a consequence of the strong law.

## Proof

First it will be shown that $2^{c}$ is uncountable and contains a "Cantor-like" set.

Now $2^{c}$ must consists of Bernoulli sequences where

$$
\frac{s_{m}(\omega)}{m} \nrightarrow \frac{1}{2}
$$

To construct such a sequence consider the map $f: \Omega \rightarrow \Omega$

$$
f(\omega)=0 . a_{1}\left\|a_{2}\right\| a_{3} \| \ldots
$$

for $\omega=0 . a_{1} a_{2} a_{3} \cdots$. The map is one-to-one, injective, thus the image $y=f(w)$ is uncountable. Since by constaction the number of i's in $y=f(\omega)$ is $2 / 3$ it follows that

$$
\frac{S_{3 m}(y)}{3 m}>\frac{2}{3}
$$

First consider $f(\omega)$. For some values of $w$ there are multiple fractional binary representations. For example

$$
\begin{aligned}
\frac{1}{2} & =0.10000 \\
& =0.011111 \cdots
\end{aligned}
$$

It follows that

$$
f(0.100000 \ldots)=0.111011011011 \ldots
$$

$$
f(0.0111111 \cdots)=0.011111111 \cdots
$$

To evaluate $f(\omega)$ the following expressions are needed,

$$
\begin{aligned}
& \sum_{i=n}^{\infty} \frac{1}{2^{i}}=\sum_{i=1}^{\infty} \frac{1}{2^{i+n}}=\frac{1}{2^{n}} \sum_{i=1}^{\infty} \frac{1}{2^{i}} \\
& =\frac{1}{2^{n}}\left(\frac{1 / 2}{1-1 / 2}\right)=\frac{1}{2^{n}}
\end{aligned}
$$

and consider,

$$
0 . a_{1}\left\|a_{2}\right\| a_{3} \cdots a_{m} 11011011 \cdots
$$

To determine the position of am in the sequence consider,

$$
\begin{array}{lllllllllllll}
a_{1} & 1 & 1 & a_{2} & 1 & 1 & a_{3} & 1 & 1 & a_{4} & 1 & 1 & a_{5} \\
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13
\end{array}
$$

$$
\begin{array}{llllll}
m: & 1 & 2 & 3 & 4 & 5 \\
i: & 1 & 4 & 7 & 10 & 13
\end{array}
$$

It follows that $c=3(m-1)+1$ and the tail sum is given by

$$
\begin{aligned}
& \frac{1}{2^{i+1}}+\frac{1}{2^{i+2}}+\frac{0}{2^{i+3}} \frac{1}{2^{i+4}}+\frac{1}{2^{i+5}}+\frac{0}{2^{i+6}} \\
+ & \frac{1}{2^{i+7}}+\frac{1}{2^{i+8}}+\frac{0}{2^{i+9}}+\frac{1}{2^{i+10}}+\frac{1}{2^{i+11}}+\cdots \\
= & \frac{1}{2^{i}}\left(\frac{1}{2}+\frac{1}{2^{2}}+\frac{0}{2^{3}}+\frac{1}{2^{4}}+\frac{1}{2^{5}}+\frac{0}{2^{6}}\right. \\
& \left.+\frac{1}{2^{7}}+\frac{1}{2^{8}}+\frac{0}{2^{q}}+\cdots\right)
\end{aligned}
$$

now the term in paretheses is given by

$$
\begin{aligned}
& 1-\left(\frac{1}{\partial^{3}}+\frac{1}{2^{6}}+\frac{1}{2^{9}}+\frac{1}{2^{12}}+\cdots\right) \\
= & \sum_{i=1}^{n} \frac{1}{2^{i}}-\left(\frac{1}{2^{3}}+\frac{1}{2^{6}}+\frac{1}{2^{9}}+\frac{1}{2^{12}} \cdots\right) \\
= & \frac{1}{2}+\frac{1}{2^{2}}+\frac{0}{2^{3}}+\frac{1}{2^{4}}+\frac{1}{2^{5}}+\frac{0}{2^{6}}+\frac{1}{2^{2}}+\frac{1}{2^{8}}
\end{aligned}
$$

$$
+\frac{0}{\partial^{4}}+\frac{1}{2^{10}}+\frac{1}{2^{11}}+\frac{0}{2^{12}}+\cdots
$$

and

$$
\begin{aligned}
& 1-\left(\frac{1}{2^{3}}+\frac{1}{2^{6}}+\frac{1}{2^{9}}+\frac{1}{2^{12}}+\cdots\right) \\
& 1-\left(\frac{1}{2^{3}}+\frac{1}{\left(2^{3}\right)^{2}}+\frac{1}{\left(2^{3}\right)^{3}}+\frac{1}{\left(2^{3}\right)^{4}}+\cdots\right) \\
& =1-\left(\frac{1}{8}+\frac{1}{8^{2}}+\frac{1}{8^{3}}+\frac{1}{8^{4}}+\cdots\right) \\
& =1-\sum_{i=1}^{\infty} \frac{1}{8^{i}} \\
& =1-\frac{1 / 8}{1-1 / 8}=1-\frac{1 / 8}{7 / 8}=1-1 / 7 \\
& =\frac{6}{7}
\end{aligned}
$$

Thus the tail sum is given by

$$
\begin{aligned}
\frac{1}{2^{i}} & \left(\frac{1}{2}+\frac{1}{2^{2}}+\frac{0}{2^{3}}+\frac{1}{2^{4}}+\frac{1}{2^{5}}+\frac{0}{2^{6}}\right. \\
& \left.+\frac{1}{2^{7}}+\frac{1}{2^{8}}+\frac{0}{2^{9}}+\cdots\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{6}{7} \frac{1}{2^{i}} \\
& \text { using } i=3(m-1)+1 \text { gives } \\
& \frac{6}{7} \frac{1}{2^{3(m-1)+1}}=\frac{3}{7} \frac{1}{2^{3(m-1)}}
\end{aligned}
$$

and finally

$$
\begin{aligned}
f(\omega)= & f\left(0 . a_{1} a_{2} a_{3} \cdots a_{m} 0000 \cdots\right) \\
& 0 a_{1}\left\|a_{2}\right\| a_{3} \cdots a_{m} 11011011 \cdots \\
= & \frac{a_{1}}{2}+\frac{1}{2^{2}}+\frac{1}{2^{4}}+\frac{a_{2}}{2^{5}}+\frac{1}{2^{6}}+\frac{1}{2^{7}}+\frac{a_{3}}{2^{8}} \\
& +\cdots+\frac{a_{m}}{2^{3(m-1)+1}}+\frac{3}{7} \frac{1}{2^{3(m-1)}}
\end{aligned}
$$

Now does

$$
f(0.100000 \ldots)=f(0.0111111 \ldots)
$$

For the first term

$$
\begin{aligned}
& f(0.100000 \cdots)=0.111011011011011 \cdots \\
& =\frac{1}{2}+\frac{3}{7} \\
& =\frac{7}{14}+\frac{6}{14}=\frac{13}{14} \\
& f(0.0111111 \cdots)=0.0111111 \cdots \\
& =\frac{1}{2}
\end{aligned}
$$

thus

$$
f(0.100000 \ldots) \neq f(0.0111111 \ldots)
$$

for most cases values of $\omega$ terminating in o's will be used with the exception of $w=1$. Which will be used since only fractional binary numbers can be used in the mapping. The neglected sequences form a countable set as shown
in the proof that the Bernoulli sequence is uncountchble so can be ignored.

First consider the endpoints of the interval $[0,1]$

$$
\begin{aligned}
f(0.000000 \cdots) & =0.011011011011 \cdots \\
& =\frac{3}{7} \\
f(0.11111 \cdots) & =0.11111111 \cdots \\
& =1
\end{aligned}
$$

The next set of interval endpoints is given by incrementing $a_{2}$ for each value of $a_{1}$.

$$
\begin{aligned}
& f(0.00000 \cdots)=\frac{3}{7} \\
& f(0.010000 \cdots)=0.01111101101100 \\
& =\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{4}}+\frac{3}{7} \frac{1}{8}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{4}+\frac{1}{8}+\frac{1}{16}+\frac{3}{56} \\
& =\frac{4}{16}+\frac{2}{16}+\frac{1}{16}+\frac{3}{56} \\
& =\frac{7}{16}+\frac{3}{56} \\
& f(0.10000 \ldots)=0.1110110110 \ldots \\
& =\frac{1}{2}+\frac{3}{7} \\
& f(0.110000 \ldots)=0.1111110110 \ldots \\
& =\frac{1}{2}+\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{4}}+\frac{3}{7} \frac{1}{8} \\
& =\frac{8}{16}+\frac{4}{16}+\frac{2}{16}+\frac{1}{16}+\frac{3}{7} \frac{1}{8} \\
& =\frac{15}{16}+\frac{3}{56}
\end{aligned}
$$

and finally the next level of intervals
$f(0.00000 \cdots)=\frac{3}{7}$

$$
\begin{aligned}
& f(0.00100 \cdots)=0.0110111110110 \cdots \\
& =\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{5}}+\frac{1}{2^{6}}+\frac{1}{2^{7}}+\frac{3}{7} \frac{1}{2^{6}} \\
& =\frac{1}{4}+\frac{1}{8}+\frac{1}{32}+\frac{1}{64}+\frac{1}{128}+\frac{3}{7}\left(\frac{1}{64}\right) \\
& =\frac{32}{128}+\frac{16}{128}+\frac{4}{128}+\frac{2}{128}+\frac{1}{128}+\frac{3}{7}\left(\frac{1}{64}\right) \\
& =\frac{55}{128}+\frac{3}{448} \\
& f(0.010000 \cdots)=0.011111011011011 \cdots \\
& =\frac{7}{16}+\frac{3}{56} \\
& f(0.011000 \cdots)=0.011111111011011 \cdots \\
& =\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{4}}+\frac{1}{2^{5}}+\frac{1}{2^{6}}+\frac{1}{2^{7}}+\frac{3}{7} \frac{1}{2^{6}} \\
& =\frac{32}{128}+\frac{16}{128}+\frac{8}{128}+\frac{4}{128}+\frac{2}{128}+\frac{1}{128}+\frac{3}{7}\left(\frac{1}{64}\right) \\
& =\frac{63}{128}+\frac{3}{448}
\end{aligned}
$$

$$
\begin{aligned}
& f(0.10000 \cdots)=0.1110110110 \\
& =\frac{1}{2}+\frac{3}{7} \\
& f(0.101000 \cdots)=0.1110111110110 \ldots \\
& =\frac{1}{2}+\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{5}}+\frac{1}{2^{6}}+\frac{1}{2^{7}}+\frac{3}{7} \frac{1}{26} \\
& =\frac{64}{128}+\frac{32}{128}+\frac{16}{128}+\frac{4}{128}+\frac{2}{128}+\frac{1}{128} \\
& +\frac{3}{7}\left(\frac{1}{64}\right) \\
& =\frac{119}{128}+\frac{3}{448} \\
& f(0.110000 \ldots)=0.1111110110 \ldots \\
& =\frac{13}{16}+\frac{3}{56} \\
& f(0.111000 \ldots)=0.111111110110110110 \ldots
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{2}+\frac{1}{2^{2}}+\frac{1}{2^{3}}+\frac{1}{2^{4}}+\frac{1}{2^{5}}+\frac{1}{2^{6}}+\frac{1}{2^{7}}+\frac{3}{7} \frac{1}{2^{6}} \\
= & \frac{64}{128}+\frac{32}{128}+\frac{16}{128}+\frac{8}{128}+\frac{4}{128}+\frac{2}{128}+\frac{1}{128} \\
& +\frac{3}{7}\left(\frac{1}{64}\right) \\
= & \frac{127}{128}+\frac{3}{448}
\end{aligned}
$$

Bringing things together gives

$$
\begin{aligned}
& \frac{i=1}{f(0.000000 \cdots)}=0.011011011011 \cdots=\frac{3}{7} \\
& f(0.11111 \cdots)=0.11111111 \cdots=1 \\
& \frac{i=2}{f(0.00000 \cdots)=\frac{3}{7}}
\end{aligned}
$$

$$
\begin{aligned}
f(0.010000 \cdots) & =0.01111101101100 \\
& =\frac{7}{16}+\frac{3}{56} \\
& =\frac{7}{2^{4}}+\frac{3}{7}\left(\frac{1}{2^{3}}\right) \\
f(0.10000 \cdots) & =0.1110110110 \cdots \\
& =\frac{1}{2}+\frac{3}{7} \\
f(0.110000 \cdots) & =0.1111110110 \cdots \\
& =\frac{15}{16}+\frac{3}{56} \\
& =\frac{15}{2^{4}}+\frac{3}{7}\left(\frac{1}{2^{3}}\right) \\
i=3 & \\
f(0.00000 \cdots) & =\frac{3}{7}
\end{aligned}
$$

$$
\begin{aligned}
f(0.00100 \cdots) & =0.0110111110110 \cdots \\
& =\frac{55}{128}+\frac{3}{448} \\
& =\frac{55}{2^{7}}+\frac{3}{7}\left(\frac{1}{2^{6}}\right) \\
f(0.010000 \cdots) & =0.0111101101100 \\
& =\frac{7}{16}+\frac{3}{56} \\
& =\frac{7}{2^{4}}+\frac{3}{7}\left(\frac{1}{2^{3}}\right) \\
f(0.011000 \cdots) & =0.01111111011011 \cdots \\
& =\frac{63}{128}+\frac{3}{448} \\
& =\frac{63}{2^{7}}+\frac{3}{7}\left(\frac{1}{2^{6}}\right) \\
f(0.110000 \cdots) & =0.111110110 \cdots \\
& =\frac{15}{16}+\frac{3}{56}
\end{aligned}
$$

$$
=\frac{15}{2^{4}}+\frac{3}{7}\left(\frac{1}{2^{3}}\right)
$$

$$
\begin{aligned}
f(0.111000 \cdots) & =0.1111111110110110110 \cdots \\
& =\frac{127}{128}+\frac{3}{448} \\
& =\frac{127}{2^{7}}+\frac{3}{7}\left(\frac{1}{2^{6}}\right)
\end{aligned}
$$

The following illustrates the intervals created at each step.
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-121.jpg?height=238&width=1342&top_left_y=1202&top_left_x=146)

At the next step the following points are added.

$$
\begin{aligned}
& 0.0111101101100 \cdots=\frac{7}{16}+\frac{3}{56}= \\
& =\frac{1}{8}\left(\frac{7}{2}+\frac{3}{7}\right)=\frac{1}{8}\left(\frac{49}{14}+\frac{6}{14}\right)
\end{aligned}
$$

$$
\begin{aligned}
=\frac{55}{(8)(k)}= & \frac{55}{112} \\
0.1110110110 \cdots & =\frac{1}{2}+\frac{3}{7}=\frac{7}{14}+\frac{6}{14}=\frac{13}{14} \\
0.1111110110 \cdots & =\frac{15}{16}+\frac{3}{56}=\frac{1}{8}\left(\frac{15}{2}+\frac{3}{7}\right) \\
=\frac{1}{8}\left(\frac{105}{14}+\frac{6}{11}\right) & =\frac{111}{(8)(14)}=\frac{111}{112}
\end{aligned}
$$

The distance of the first point from the left endpoint is given by,

$$
\begin{aligned}
& \frac{7}{16}+\frac{3}{56}-\frac{3}{7}=\frac{1}{8}\left(\frac{7}{2}+\frac{3}{7}\right)-\frac{3}{7} \\
& =\frac{1}{8}\left(\frac{49}{14}+\frac{6}{14}\right)-\frac{3}{7}=\frac{1}{8}\left(\frac{55}{14}\right)-\frac{3}{7} \\
& =\frac{1}{8}\left(\frac{1}{7}\right)\left(\frac{55}{2}\right)-\frac{3}{7}=\left(\frac{1}{7}\right)\left[\left(\frac{1}{8}\right)\left(\frac{55}{2}\right)-3\right] \\
& =\left(\frac{1}{7}\right)\left[\left(\frac{1}{8}\right)\left(\frac{55}{2}\right)-\left(\frac{8}{8}\right)\left(\frac{2}{2}\right)(3)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)\left(\frac{1}{2}\right)(55-48) \\
& =\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)\left(\frac{1}{2}\right)(7) \\
& =\frac{1}{16}
\end{aligned}
$$

The distance of the last point from the right endpoint is
given by

$$
\begin{aligned}
& 1-\frac{15}{16}-\frac{3}{56}=\frac{1}{8}\left(8-\frac{15}{2}-\frac{3}{7}\right) \\
& =\frac{1}{16}\left(16-15-\frac{6}{7}\right) \\
& =\frac{1}{16}\left(1-\frac{6}{7}\right)=\frac{1}{16}\left(\frac{1}{7}\right)=\frac{1}{112}
\end{aligned}
$$

and the distance of the midpoint from the leftmost point is

$$
\left(\frac{1}{2}+\frac{3}{7}\right)-\left(\frac{7}{16}+\frac{3}{56}\right)
$$

$$
\begin{aligned}
& =\frac{8}{16}-\frac{7}{16}+\frac{3}{7}-\frac{3}{56}=\frac{1}{16}+\frac{1}{7}\left(3-\frac{3}{8}\right) \\
& =\frac{1}{16}+\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)(24-3) \\
& =\frac{1}{16}+\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)(21) \\
& =\frac{1}{16}+\frac{3}{8}=\frac{1}{16}
\end{aligned}
$$

and the distance from the rightmost point is

$$
\begin{aligned}
& \left(\frac{15}{16}+\frac{3}{56}\right)-\left(\frac{1}{2}+\frac{3}{7}\right) \\
& =\left(\frac{15}{16}-\frac{8}{16}\right)+\frac{1}{7}\left(\frac{3}{8}-3\right) \\
& =\frac{7}{16}+\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)(3-24) \\
& =\frac{7}{16}-\left(\frac{1}{7}\right)\left(\frac{1}{8}\right)(21)=\frac{7}{16}-\frac{3}{8} \\
& =\frac{7}{16}-\frac{6}{16}=\frac{1}{16}
\end{aligned}
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-125.jpg?height=273&width=1426&top_left_y=118&top_left_x=70)

$$
\begin{aligned}
f(0.00100 \cdots) & =0.0110111110110 \cdots \\
& =\frac{55}{128}+\frac{3}{448} \\
f(0.010000 \cdots) & =0.01111101101100 \\
& =\frac{7}{16}+\frac{3}{56} \\
f(0.011000 \cdots) & =0.011111111011011 \cdots \\
& =\frac{63}{128}+\frac{3}{448} \\
f(0.110000 \cdots) & =0.1111110110 \cdots \\
& =\frac{15}{16}+\frac{3}{56}
\end{aligned}
$$

$$
\begin{aligned}
f(0.111000 \cdots) & =0.1111111110110110110 \cdots \\
& =\frac{127}{128}+\frac{3}{448}
\end{aligned}
$$

## Randomness

In the previous section it was shown that the set $B$ of Bernoulli sequences can be mapped to the set of points on the unit interval $\Omega=(0,1]$.
$A$ probabalistic event $B C B$ is mapped to an interval

$$
[a, b] \subset \Omega
$$

Using the Borel principle of mapping the binary fraction representing a Bernoulli sequence to a real number $\omega \in \Omega$ leads to the representation of the probability of an event as a lebesgue,

$$
P(B)=\mu_{\alpha}([a, b])
$$

In this section more complicated probabilistic events will be described using measure theory

## Event Examples

Some examples of more complex events are the Gambler's ruin where the gambler's intial stake is $x$ in a game betting 1 that the toss of a fair com is heads. What is the probability of ruin, i.e. that the gambler loses all of his money.
This event is given by

$$
E=\bigcup_{k=1}^{\infty} E_{k}
$$

where
$E_{k}=\{\omega \in \Omega ; \omega(\omega)>-x$, for $l<k$ and

$$
w_{k}(\omega)=-x \xi
$$

where

$$
\omega_{k}(\omega)=\sum_{i=1}^{k} R_{k}(\omega)
$$

with $R_{k}(\omega)$ is the k'th Rademacher function. It will be seen that after developing the tools to analyze this problem that

$$
\mu_{\alpha}(E)=\sum_{k=1}^{\infty} \mu_{\alpha}\left(E_{k}\right)=1
$$

Another problem to be solved is the probability of occurance of a finite sequence THHT in a Bernoulli seguence. This event is defined by
$E=\{\omega \in \Omega$; where the n'th toss satisfies $R_{n}(\omega)=-1, R_{n+1}(\omega)=1 R_{n+2}(\omega)=1$ and $\left.R_{n+3}(\omega)=-1\right\}$

Where $R_{n}(\omega)$ is the n'th Rademacher function. It will be seen trat $P(E)=1$.

## Random Variables

The n'th Rademacher function, $R_{n}(\omega)$, gives the total winnings on the ith toss. Rn ( $\omega$ ) is a function over $B$ through the mapping $B \leftrightarrow \Omega$ using binary fractions. Rn (w) is an example of a rendom variable. Another example is

$$
\omega_{n}(\omega)=\sum_{i=1}^{n} R_{i}(\omega)
$$

which is the total winnings after $n$ tosses of the com toss game.

## Expectation Values

A random variable associated with $B$ is a function $f: B \rightarrow \mathbb{R}$. Since $B$ is mapped to $\Omega$ by the Borel mapping a random
variable can be viewed as a function over $\Omega$.
The expectation of $f$ is define b. 1

$$
E[f]=\int_{\Omega} f d \mu_{\alpha}
$$

For the Rademacher fanction $R_{n}(w)$ this becomes a Riemann integral

$$
\int_{0} R_{n}(\omega) d \omega=0
$$

## Random walks

A Bernoulli sequence that is a sequence of com tosses describes a randow walk on the real line is if a runnis sum is kept where a toss of tails subtracts 1 from the sum and a toss of tails subtracts 1. It follows that for each Bernoulli sequence there is a random walk. Let $R$ represent the space of all random walks then there is a correspondence between $R$ and $B$, namely.

$$
\omega_{n}(\omega)=\sum_{i=1}^{n} R_{n}(\omega)
$$

Random walk with Pause
A random walk with a pause has 3 states instead of two. At each step,

$$
-1,0,+1
$$

is added to the sum with equal probability. This process can be modeled using the ternay fraction expansion

$$
\omega=\sum_{i=1}^{\infty} \frac{a_{i}}{3^{i}} \quad a_{i} \in\{0,1,2\}
$$

and making the association

$$
\begin{aligned}
& 1 \leftrightarrow+1 \\
& 0 \leftrightarrow 0 \\
& 2 \leftrightarrow-1
\end{aligned}
$$

This association maps each relization of the processe to a terrary fraction.
Random walk in a Plane
A random walk in a plane is four state model. Which is illustrated in the following figure. A few steps of a
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-134.jpg?height=632&width=747&top_left_y=58&top_left_x=310)
random walk are shown in the Eigure Every realization of a Step in the walk corresponds to a coordinate $(x, y)$. Let

$$
\begin{aligned}
& N \leftrightarrow(0,1) \\
& S \leftrightarrow(0,-1) \\
& E \leftrightarrow(1,0) \\
& \omega \leftrightarrow(-1,0)
\end{aligned}
$$

The walk is constructed by choosing a direction with equal probcbility and maintains a sum for each coordinate.

This processe can be represented by the base four fractional expansion

$$
\omega=\sum_{i=0}^{\infty} \frac{a_{c}}{4^{i}} \quad a_{i} \in\{0,1,2,3\}
$$

where

$$
\begin{aligned}
& 0 \leftrightarrow N \\
& 1 \longleftrightarrow S \\
& 2 \leftrightarrow E \\
& 3 \leftrightarrow \omega
\end{aligned}
$$

Example 1
Using the ternay fraction model of a random walk with pauses compute the probability of the following events

1. A pause at $t=1$
2. A pause at $t=2$
3. Forward motion at $t=1,2,3, \ldots, n$.
4. Forward motion at $t=k, k+1, k+2$, $k+n$

The ternary fraction model is given by

$$
\omega=\sum_{i=1}^{\infty} \frac{a_{i}}{B^{c}} \quad c_{i}=\{0,1,2\}
$$

where

$$
\begin{aligned}
& 0 \leftrightarrow 0 \\
& 1 \leftrightarrow+1 \\
& 2 \leftrightarrow-1
\end{aligned}
$$

Also, if terminating and non-terminating sequences are equal the non-terminating sequence is chosen,

$$
0.10000 \cdots=0.02222 \cdots
$$

Now for the forct problem all events starting with a pause lie on the interval

$$
[0.0000 \cdots, 0.02222 \cdots]
$$

it follows that

$$
\begin{aligned}
P\left(a_{1}=0\right) & =\mu_{\alpha}([0.0000 \cdots, 0.02222 \cdots]) \\
& =\mu_{\alpha}([0,1 / 3])=\frac{1}{3}
\end{aligned}
$$

For the second problem the probability of a pause at time $n$ will be all events of the form

$$
\omega=0, a_{1} a_{2} a_{3} \cdots a_{n-1}, \Delta a_{n+1} a_{n+2} \cdots
$$

The first interval containing an event will be

$$
\begin{aligned}
& {[0.0000 \cdots, 0.000 \cdots 022 \cdots]} \\
& =\left[0,1 / 3^{n}\right]
\end{aligned}
$$

the next will be

$$
\begin{aligned}
& {[0.000 \cdots 100 \cdots, 0.000 \cdots 10222 \cdots] } \\
= & {\left[1 / 3^{n-1}, 1 / 3^{n-1}+1 / 3^{n}\right] }
\end{aligned}
$$

and the next

$$
\begin{aligned}
& {[0.000200 \cdots, 0.000 \cdots 20222 \cdots] } \\
= & {\left[2 / 3^{n-1}, 2 / 3^{n-1}+1 / 3^{n}\right] }
\end{aligned}
$$

From this it is seen that the width of each interval is

$$
\frac{1}{3^{n}}
$$

There will be $3^{n-1}$ intervals of this length. It follows that

$$
P\left(a_{n}=0\right)=\frac{3^{n-1}}{3^{n}}=\frac{1}{3}
$$

For the third problem of the probability that the first $n$ moves are forward the event lies on the interval

$$
[0.111 \cdots 022 \cdots, 0.1111 \cdots 122 \cdots]
$$

Now

$$
\begin{aligned}
& P\left(a_{1}=\left(, a_{2}=1, \cdots, a_{n}=1\right)\right. \\
& =\mu_{2}([0.111 \cdots 100 \cdots, 0.1111 \cdots 122 \cdots]) \\
& =0.111 \cdots 122 \cdots-0.111 \cdots 100 \cdots \\
& =0.000 \cdots 0222 \cdots \\
& =\sum_{i=n+1}^{\infty} \frac{2}{3^{i}} \\
& =2 \sum_{i=1}^{\infty} \frac{1}{3^{n+i}} \\
& =\frac{2}{3^{n}} \sum_{i=1}^{\infty} \frac{1}{3^{i}} \\
& =\frac{2}{3^{n}}\left(\frac{1 / 3}{1-1 / 3}\right)=\frac{2}{3^{n}}\left(\frac{1}{2}\right) \\
& =\frac{1}{3^{n}}
\end{aligned}
$$

And finally the last problem the probability of forward
motion for $t=k, k+l, \ldots, k+n$ the event lies on $3^{k-1}$ intervals.

Each interval will have the form

$$
\begin{gathered}
{\left[0 . a_{1} a_{2} \cdots a_{k-1} \mid 1 \cdots 022 \cdots,\right.} \\
\left.0 . a_{1} a_{2} \cdots a_{k-1} \mid 1 \cdots 22 \cdots\right]
\end{gathered}
$$

It follows that

$$
\begin{aligned}
& P\left(a_{k}=1, a_{k+1}=1, \ldots, a_{k+n}=1\right) \\
& =\mu_{2}\left(\left[0, a_{1} a_{2} \cdots a_{k-1} \mid 1 \cdots 022 \cdots,\right.\right. \\
& \left.\left.0, a_{1} a_{2} \cdots a_{k-1} \mid 1 \cdots 122 \cdots\right]\right) \\
& \left.=0, a_{1} a_{2} \cdots a_{k-1} \mid 1 \cdots 1222 \cdots 1000 \cdots\right] \\
& \quad 0 . a_{1} a_{2} a_{k-1} \mid 1 \cdots 1000 \cdots 22 \\
& =0.000 \cdots 2222 \\
& =\sum_{i=k+n}^{\infty} \frac{2}{3^{i}} \\
& =2 \sum_{i=1}^{\infty} \frac{1}{3^{i+k+n}}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{2}{3^{k+n}} \sum_{i=1}^{\infty} \frac{1}{3^{i}} \\
& =\frac{2}{3^{k+n}} \frac{1 / 3}{213} \\
& =\frac{1}{3^{k+n}}
\end{aligned}
$$

Since there are $3^{k-1}$ intervas it follows that the probability of the event is given by

$$
\frac{3^{k-1}}{3^{k+n}}=\frac{1}{3^{n+1}}
$$

Measure Theory
This section will go into details of measure theory which have previously been touched upon.
The notation used is reviewed below. It is assumed that sets $A$ and $B$ satisfy $A \subseteq X$ and $B \subseteq \bar{X}$

Empty Set : $\varnothing$
union of sets $A$ and $B$ :

$$
A \cup B=\{x \in \mathbb{X} ; x \in A \text { or } x \in B\}
$$

Intersection of sets $A$ and $B$ :

$$
A \cap B=\{x \in \mathbb{X} ; x \in A \text { and } x \in B\}
$$

compliment:

$$
A^{c}=\{x \in \bar{X} ; x \notin A\}
$$

$B$ minus $A$

$$
B-A=\{x \in \mathbb{Z} ; x \in B \text { and } x \notin A\}
$$

Symetric Difference of $A$ and $B$ :

$$
S(A, B)=(A-B) \cup(B-A)
$$

The following figure illustrates $S(A, B)$ which is high lighted in yellow.
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-143.jpg?height=453&width=1008&top_left_y=606&top_left_x=294)

An interesting relation between set intersection and difference is given by

$$
A \cap B=A-(A-B)
$$

This is illustrated in the following figure
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-143.jpg?height=364&width=470&top_left_y=1616&top_left_x=572)

$$
A \cap B=A-(A-B)
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-144.jpg?height=286&width=492&top_left_y=243&top_left_x=552)

Proof: $\quad A \cap B=A-(A-B)$
Assume that $x \in \bar{X}$ and $x \in A \cap B$ it follows that $x \in A$ and $x \in B$. From the definition of $A-B$ it follows that

$$
X \notin A-B
$$

and since $x \in A$ and $x \notin A-B$ tt follows that

$$
x \in A-(A-B)
$$

Next assume that $x \in A-(A-B)$ it follows that $x \in A$ and $x \notin A-B$ but $x \notin A-B \Rightarrow x \in A$ and $x \in B$. From the definition of intersection

$$
x \in A \cap B
$$

and thus

$$
A \cap B=A-(A-B)
$$

Definition: Ring of sets.
Consider a set $X$. A ring of sets in $X$ is denoted by $\mathbb{R}$ and consists of subsets of $X$ which sctisfy,

1. $A \cup B \in R$ if $A \in R$ and $B \in R$
2. $A-B \in R$ if $A \in R$ and $B \in R$

Notice that since $A \in \mathbb{R}$ that $A-A \in \mathbb{R} \Rightarrow \phi \in \mathbb{R}$. It is because of this that (2) is choosen instead of the alternative $A \cap B \in Q . \quad A \cap B \in Q$ follows from $A-B \in Q$ and $A \cap B=A-(A-B)$.

Example: Power Set is Ring Consider the set $\bar{X}=\left\{x_{1}, x_{2}, x_{3}\right\}$.

The power set of $I$ is the set of all subsets of $\bar{X}$.

The power set is computed using an indicator function to determine membership
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-146.jpg?height=326&width=1194&top_left_y=608&top_left_x=102)

The members of the powerset are determined by traversing the tree and placing the element in the power set if the node is 1. It follows that the number of sets in the power set will be the number of leaf nodes which is groen by $2^{3}=8$

$$
\begin{aligned}
P_{\mathbb{X}}= & \left\{\left\{x_{1}, x_{2}, x_{3}\right\},\left\{x_{1}, x_{2}\right\},\left\{x_{1}, x_{3}\right\},\right. \\
& \left.\left\{x_{1}\right\},\left\{x_{2}, x_{3}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}, \triangle\right\}
\end{aligned}
$$

It is easy to verify the $P_{x}$ is a ring.

Example: Multi-interoal
Let $\bar{x}=\mathbb{R}^{n}$ and suppose that $\left(a_{1}, a_{2}, \ldots, a_{n}\right)$ and $\left(b_{1}, b_{2}, \ldots, b_{n}\right)$ are given with

$$
a_{i} \leqslant b_{i} \quad i=1,2, \ldots, n
$$

Let $A$ be the set of points $x \in \mathbb{R}^{n}$ such that

$$
a_{i} \leqslant x_{i} \leqslant b_{i} \quad i=1,2,3, \ldots, n
$$

$A$ is called a multi-interval. A multi-interval may be defined usine < or $\leqslant$.
Define the ring $R_{\alpha}$ by

$$
A \in Q_{\mathscr{L}} \Leftrightarrow A=\bigcup_{i=1}^{n} A_{i}
$$

where the $A_{i}$ are disjoint collections of multi-intoroals.

Now, consider a ring $R$ of
subsets of $\bar{x}$. Let $\mu$ be a non-negative set function on $R$, that is for each $A \in R$ y assigns cssigns a non-negative number $\mu(A)$.
$\mu$ is additive if

$$
\mu(A \cup B)=\mu(A)+\mu(B)
$$

is $A, B \in R$ setisf, $A \cap B=\varnothing$
Example: Let $Q=Q_{2}$ and suppose that $A \in Q_{f}$ is a multi-interval described by the inequalities

$$
a_{i} \leqslant x_{i} \leqslant b_{i} \quad i=1,2, \ldots, n
$$

define
$\mu(A)=\left(b_{1}-a_{1}\right)\left(b_{2}-a_{2}\right) \cdots\left(b_{n}-a_{n}\right)$
More generally if $A=U_{i=1}^{n} A_{i}$ is a disjont union of mult-intervals then

$$
\mu(A)=\sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

Proposition : Let $Q$ be a ning of subsets of $\bar{X}$ and $\mu$ an advitive non-negative set functon on $\mathbb{R}$ then

1) $\mu(\phi)=0$
2) If $A, B \in R$ with $A S B$ then $\mu(A) \leqslant \mu(B)$. This property is called monotonicity.
3) If $A_{1}, A_{2}, \ldots, A_{n} \in R$ are mutually disjoint then

$$
\mu\left(\cup_{i=1}^{n} A_{i}\right)=\sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

This property is called finite additivity.
4) If $A, B \in G$ then
$\mu(A \cup B)+\mu(A \cap B)=\mu(A)+\mu(B)$
This property is called the
lattice property.
5) If $A_{1}, A_{2}, \ldots, A_{n} \in R$ but not neccessarily dispoint then

$$
\mu\left(\bigcup_{i=1} A_{i}\right) \leq \sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

This property is called the finite additive property.

Proof: $\mu(\phi)=0$
Let $A \in R$ then

$$
\begin{aligned}
& \mu(A)=\mu(A \cup \varnothing)=\mu(A)+\mu(\Phi) \\
& \Rightarrow \mu(\phi)=0
\end{aligned}
$$

Proof: $A \subseteq B \Rightarrow \mu(A) \leqslant \mu(B)$
Let $A, B \in Q$ then since $A \subseteq B$

$$
\begin{aligned}
B & =(B-A) \cup A \\
\Rightarrow \mu(B) & =\mu(B-A)+\mu(A)
\end{aligned}
$$

but $\mu(B-A) \geqslant 0$ thus

$$
\mu(B) \geqslant \mu(A)
$$

Proof: $\mu\left(U_{i=1}^{n} A_{i}\right)=\sum_{i=1}^{n} \mu\left(A_{i}\right)$ if
$A_{i}$ are mutually disjoint
From the definition of the advitive property for $A_{1}, A_{2} \in R$ where $A_{1}$ and $A_{2}$ are disjoint

$$
\mu\left(A_{1} \cup A_{2}\right)=\mu\left(A_{1}\right)+\mu\left(A_{2}\right)
$$

using mathematical induction essume

$$
\mu\left(U_{i=1}^{n} A_{i}\right)=\sum_{i=1}^{n} \mu\left(A_{1}\right)
$$

thus

$$
\begin{aligned}
& \mu\left(U_{i=1}^{n+1} A_{i}\right)=\mu\left(\left(U_{i=1}^{n} A_{i}\right) \cup A_{n+1}\right) \\
& =\mu\left(U_{i=1}^{n} A_{i}\right)+\mu\left(A_{n+1}\right) \\
& =\sum_{i=1}^{n} \mu\left(A_{i}\right)+\mu\left(A_{n+1}\right) \\
& =\sum_{i=1}^{n+1} \mu\left(A_{i}\right)
\end{aligned}
$$

$$
\text { Proof: } \begin{aligned}
& \mu(A \cup B)+\mu(A \cap B) \\
& =\mu(A)+\mu(B) \text { for } \\
& \wedge B \neq \varnothing
\end{aligned}
$$

Let $A, B \in Q$, now

$$
\begin{aligned}
& A=(A-B) \cup(A \cap B) \\
& B=(B-A) \cup(B \cap A)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
A \cup B= & (A-B) \cup(A \cap B) \cup(B-A) \\
& \cup(B \cap A) \\
= & (A-B) \cup(B-A) \cup(A \cap B)
\end{aligned}
$$

Now using the additive property

$$
\begin{aligned}
& \mu(A)=\mu(A-B)+\mu(A \cap B) \\
& \mu(B)=\mu(B-A)+\mu(B \cap A)
\end{aligned}
$$

and
$\mu(A \cup B)=\mu(A-B)+\mu(B-A)$

## $+\mu(B \cap A)$

using the previous result
gives

$$
\begin{gathered}
\mu(A \cup B)=\mu(A)+\mu(B) \\
-\mu(A \cap B) \\
=\mu(A \cup B)+\mu(A \cap B)=\mu(A)+\mu(B)
\end{gathered}
$$

This relation is well known from probobility.

Proof : $\mu\left(\bigcup_{i=1} A_{i}\right) \leq \sum_{i=1}^{n} \mu\left(A_{i}\right)$
From the previous proof of the lattice property
$\mu\left(A_{1} \cup A_{2}\right)+\mu\left(A_{1} \cap A_{2}\right)=\mu\left(A_{1}\right)+\mu\left(A_{2}\right)$
$\Rightarrow \mu\left(\bigcup_{i=1}^{2} A_{1}\right) \leqslant \sum_{i=1}^{2} \mu\left(A_{i}\right)$
using induction assume that,

$$
\mu\left(\bigcup_{i=1}^{n} A_{i}\right) \leqslant \sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

Thus

$$
\begin{gathered}
\mu\left(\bigcup_{i=1}^{n+2} A_{i}\right)=\mu\left(\left(\bigcup_{i=n+1}^{n+2} A_{i}\right) U\left(\bigcup_{i=1}^{n} A_{i}\right)\right) \\
=\mu\left(\bigcup_{i=n+1}^{n+2} A_{i}\right)+\mu\left(\bigcup_{i=1}^{n} A_{i}\right) \\
\leqslant \sum_{i=n+1}^{n+2} \mu\left(A_{i}\right)+\sum_{i=1}^{n} \mu\left(A_{i}\right) \\
=\sum_{i=1}^{n+2} \mu\left(A_{i}\right)
\end{gathered}
$$

Thus the final result is obtained

$$
\mu\left(\bigcup_{i=1}^{n} A_{i}\right) \leqslant \sum_{i=1}^{n} \mu\left(A_{i}\right)
$$

## Definition: Measure

Let $Q$ be a ring of subsets of $\bar{x}$ and $\mu$ an additive set function on $Q$. It is said that
$\mu$ is countably additive on $R$ if, given any countable collection

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \subset Q
$$

with $A_{i} \cap A_{j}=\varnothing$ for $i \neq j$ and

$$
A=\bigcup_{i=1}^{\infty} A_{i} \in R
$$

then

$$
\mu(A)=\sum_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

A countably additive, non-negative set function $\mu$ on a ring $R$ in $\bar{X}$ is called a measure.

Theorem: If $\bar{x}=\mathbb{R}^{n}$ and $R=Q_{f}$ and $\mu$ is the set function

$$
\mu(A)=\left(b_{1}-a_{1}\right)\left(b_{2}-a_{2}\right) \cdots\left(b_{n}-a_{n}\right)
$$

where $A$ is the multi-interval which is the set of pants $x \in \mathbb{R}^{n}$ such that

$$
a_{i} \leqslant x_{i} \leqslant b_{i} \quad i=1,2,3, \ldots, n
$$

Consider the set of multi-intervals $\left\{A_{i} \xi_{i=1}^{\infty}\right.$ where $A_{i}$ is the set of points satisfying $x_{i j} \in \mathbb{R}^{n}$

$$
a_{i j} \leqslant x_{i j} \leqslant b_{i j} \quad j=1,2, \ldots, n
$$

it follows that

$$
\mu\left(A_{i}\right)=\prod_{j=1}^{n}\left(b_{i j}-a_{i j}\right)
$$

Clearly $\mu\left(A_{i}\right)$ represents a generatization of a volume element.

Now $\mu$ is a measure if,

$$
\begin{aligned}
\mu(A) & =\sum_{i=1}^{\infty} \mu\left(A_{i}\right) \\
& =\sum_{i=1}^{\infty} \prod_{j=1}^{n}\left(b_{i j}-a_{i j}\right)
\end{aligned}
$$

To prove this the following lemma is required
Lemma: Let $A \in R_{x}$ and let $\varepsilon>0$ be given. There exists $f, \in \in R_{z}$ such that $F$ is closed $G$ is open
where $F \subseteq A \subseteq G$, and

$$
\begin{aligned}
& \mu(F) \geqslant \mu(A)-\varepsilon \\
& \mu(B) \leqslant \mu(A)+\varepsilon
\end{aligned}
$$

Proof: Assume $A$ is a multi-intercal given by the inequalities

$$
a_{i} \leqslant x_{i} \leqslant b_{i} \quad i=1,2, \ldots, n
$$

I's can be replaced by is.
We can find a $\delta$ such that

$$
\begin{aligned}
\prod_{i=1}^{n} & {\left[\left(b_{i}-\delta\right)-\left(a_{i}+\delta\right)\right] } \\
& =\prod_{i=1}^{n}\left(b_{i}-a_{i}-2 \delta\right) \geqslant \prod_{i=1}^{n}\left(b_{i}-a_{i}\right)-\varepsilon
\end{aligned}
$$

and

$$
\begin{aligned}
\prod_{i=1}^{n} & {\left[\left(b_{i}+\delta\right)-\left(a_{i}-\delta\right)\right] } \\
= & \prod_{i=1}^{n}\left(b_{i}-a_{i}+2 \delta\right) \leqslant \prod_{i=1}^{n}\left(b_{i}-a_{i}\right)+\varepsilon
\end{aligned}
$$

Let $F$ be given by the inequalities

$$
a_{i}+\delta \leqslant x_{i} \leqslant b_{i}-\delta
$$

and $c$ by the inequalities

$$
a_{i}-\delta<x_{i}<b_{i}+\delta
$$

This is illustrated graphically
bebw

A
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-158.jpg?height=154&width=897&top_left_y=624&top_left_x=413)

F
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-158.jpg?height=148&width=889&top_left_y=862&top_left_x=413)

G
![](https://cdn.mathpix.com/cropped/2025_11_16_2659cbbb0350fbd4504cg-158.jpg?height=191&width=903&top_left_y=1082&top_left_x=419)

It follows that

$$
F \subseteq A \subseteq C
$$

so

$$
\mu(F) \leqslant \mu(A) \leqslant \mu(C)
$$

Now $\delta$ is chosen such that

$$
\mu(F) \geqslant \mu(A)-\varepsilon
$$

and

$$
\mu(G) \leqslant \mu(A)+\varepsilon
$$

Now, if

$$
A=\bigcup_{i=1}^{k} A_{i}
$$

where $A_{i}$ are disjoint multi-intervals, so that $A$ is a union of disjoint multi-intervals.

For each $A_{i}$ find $a_{n} F_{i}$ and $G_{i}$ such that

$$
\begin{aligned}
& \mu\left(F_{i}\right) \geqslant \mu\left(A_{i}\right)-\frac{\varepsilon}{k} \\
& \mu\left(E_{i}\right) \leqslant \mu\left(A_{i}\right)+\frac{\varepsilon}{k}
\end{aligned}
$$

Let

$$
F=\bigcup_{i=1}^{k} F_{i} \quad G=\bigcup_{i=1}^{k} G_{i}
$$

Then

$$
\mu(F)=\mu\left(\bigcup_{i=1}^{k} F_{i}\right)=\sum_{i=1}^{k} \mu\left(F_{i}\right)
$$

$$
\geqslant \sum_{i=1}^{k}\left[\mu\left(A_{i}\right)-\frac{\varepsilon}{k}\right]=\mu(A)-\varepsilon
$$

and

$$
\begin{aligned}
\mu(E) & =\mu\left(\bigcup_{i=1}^{k} G_{i}\right)=\sum_{i=1}^{k} \mu\left(G_{i}\right) \\
& \leqslant \sum_{i=1}^{k}\left[\mu\left(A_{i}\right)+\frac{\varepsilon}{k}\right] \\
& =\mu(A)+\varepsilon
\end{aligned}
$$

Next consider a countable collection of disjoint mult-intervals

$$
\left\{A_{i}\right\}_{i=1}^{\infty} \text { where } A_{i} \in R_{y}
$$

and let

$$
A=\bigcup_{i=1}^{\infty} A_{i} \text { where } A \in R_{\mathcal{L}}
$$

Note that $U_{i=1}^{N} A_{i} \subset A$. It follows the

$$
\begin{aligned}
\mu(A) & \geqslant \mu\left(U_{i=1}^{N} A_{i}\right) \\
& =\sum_{i=1}^{N} \mu\left(A_{i}\right)
\end{aligned}
$$

for any value of $N$. If $N$ is arbitrally large

$$
\mu(A) \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

loow

$$
\begin{aligned}
\mu(A)-\varepsilon & \leqslant \mu(F) \\
& \leqslant \mu(G) \\
& \leqslant \mu\left(\bigcup_{i=1}^{N} G_{i}\right) \\
& \leqslant \sum_{i=1}^{N} \mu\left(G_{i}\right) \\
& \leqslant \sum_{i=1}^{N}\left[\mu\left(A_{i}\right)+\frac{\varepsilon}{2 i}\right] \\
& \leqslant \sum_{i=1}^{N}\left[\mu\left(A_{i}\right)+\frac{\varepsilon}{2 i}\right] \\
& =\sum_{i=1}^{N} \mu\left(A_{i}\right)+\frac{\varepsilon}{2}\left(\frac{1}{1 / 2}\right) \\
& =\sum_{i=1}^{N} \mu\left(A_{i}\right)+\varepsilon
\end{aligned}
$$

since $\varepsilon$ is arbitrary assume $\varepsilon=0$ then

$$
\mu(A) \leqslant \sum_{i=1}^{\Delta} \mu\left(A_{i}\right)
$$

but previously it was shown that

$$
\mu(A) \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

It follows that

$$
\mu(A)=\sum_{i=1}^{\infty} \mu\left(A_{i}\right)
$$

Recall the previous definition of measure zero. A set $A C R$ has measure zero if for every $\varepsilon>0$ the exists a countable covering $\left\{A_{i}\right\}$ of $A$ where

$$
A \subseteq \bigcup_{i=1}^{\infty} A_{i}
$$

such trat

$$
\begin{aligned}
\mu(A) & \leqslant \mu\left(\bigcup_{i=1}^{\infty} A_{i}\right) \\
& =\sum_{i=1}^{\infty} \mu\left(A_{i}\right)<\varepsilon
\end{aligned}
$$

Definition: Approximate Outer Measure Let $A \subset \bar{X}$. The number $m \geqslant 0$ will be called an approximate outer measure of $A$ if there exists a covering of by a countable union of sets $\left\{A_{i}\right\}_{i=1}^{\infty}$ with each $A_{i} \in R$ such that

$$
\sum_{i=1}^{\infty} \mu\left(A_{i}\right) \leq m
$$

## Definition: Outer Measure

Let $A$ be a subset of I. The outer measure of $A, \mu^{*}(A)$, is the greatest lower bound of the set
\{m: $m$ is an approximate outer measure of $A\}$

If this set is emply $\mu^{*}(A)=+\infty$
The outer measure is a set function

$$
\mu^{*}: 2^{8} \rightarrow[0, \infty]
$$

where $2^{X}$ is the power set of $\bar{X}$.

Proposition: If $A \in R$ then

$$
\mu^{*}(A)=\mu(A)
$$

Proof: Covering A by the sequence

$$
A_{1}=A, A_{2}=\phi, A_{3}=\phi, \ldots
$$

It follows that

$$
\mu^{+}(A) \leqslant \mu(A)
$$

To prove equality it must also be shown that $\mu^{*}(A) \geqslant \mu(A)$.
To prove this let $\varepsilon>0$ be given. Because $u^{*}(A)$ is the greatest lower bound of all approximate outer measures of A, a cover $\left\{A_{i}\right\}_{i=1}^{\infty} \subset R$ must exist such that

$$
u^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} u\left(A_{i}\right)
$$

Since $A \in R \Rightarrow A_{i} \in R \Rightarrow A_{i}-A_{j} \in R$ and $A_{i} \cup A_{j} \in R$. Let $A_{1}^{\prime}=A_{1}, A_{2}^{\prime}=A_{2}-A_{1}$, $A_{3}^{\prime}=A_{3}-\left(A_{1} \cup A_{2}\right) \cdots a$ sequence of sets constructed in this fashion will be mutually disjoint,

$$
A_{i}^{\prime} \cap A_{j}^{\prime}=\varnothing \quad i \neq j
$$

Next it will be shown that

$$
\bigcup_{i=1}^{\infty} A_{i}^{\prime}=\bigcup_{i=1}^{\infty} A_{i}
$$

If $x \in \cup_{i=1}^{\infty} A_{i}^{\prime}$ then since the $A_{i}^{\prime}$ are mutually disjoint there exists a $j$ such that $x \in A_{j}^{\prime}$. From the defonition of $A_{j}^{\prime} j$ it follows that $x \in A_{j}$ thus

$$
\bigcup_{i=1}^{\infty} A_{i}^{\prime} \subseteq \bigcup_{i=1}^{\infty} A_{i}
$$

Now if $x \in \cup_{i=1}^{\infty} A_{i}$ then there is at least one value of $i$, denoted by $_{j}$, such that $x \in A_{j}$.

It follows that $x \in A_{i \leqslant j}^{\prime}$.
That is $x$ will be an element of some $A_{i}^{\prime}$ with $i \leqslant j$. It follows that

$$
\bigcup_{i=1}^{\infty} A_{i}^{\prime}=\bigcup_{i=1}^{\infty} A_{i}
$$

so,

$$
\mu^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime}\right)
$$

Furthur assume that

$$
A_{i}^{\prime \prime}=A_{i}^{\prime} \cap A
$$

then $A_{i}^{\prime \prime} \subseteq A$ for all $i$. For $[7]$ it follows that,

$$
A_{i}^{\prime \prime} \cap A_{j}^{\prime \prime}=\left(A_{i}^{\prime} \cap A\right) \cap\left(A_{j}^{\prime} \cap A\right)=\varnothing
$$

since $A_{i}^{\prime} \cap A_{j}^{\prime}=\phi \Rightarrow X \in A_{i}^{\prime} \neq X \notin A_{j}^{\prime}$ so

$$
x \in A_{i}^{\prime} \cap A \Rightarrow x \notin A_{j}^{\prime} \cap A .
$$

and

$$
A_{i}^{\prime \prime} \cap A_{j}^{\prime \prime}=\left(A_{i}^{\prime} \cap A\right) \cap\left(A_{j}^{\prime} \cap A\right)=\varnothing
$$

pext it will be shown that

$$
\bigcup_{i=1}^{\infty} A_{i}^{\prime \prime} \subseteq \bigcup_{i=1}^{\infty} A_{i}^{\prime}
$$

Assume that $x \in \bigcup_{i=1}^{\infty} A_{i}^{\prime \prime}$ since $A^{\prime \prime}$ are mutually disjoint there is one value of $i$ where $x \in A^{\prime \prime} i$. Recall the definition of $A_{i}^{\prime \prime}$

$$
A_{i}^{\prime \prime}=A_{i}^{\prime} \cap A
$$

thus $x \in A_{i}^{\prime \prime} \Rightarrow x \in A_{i}^{\prime}$ and $x \in A$. it follows that $x \in \cup_{i=1}^{\infty} A_{i}^{\prime}$ so

$$
\bigcup_{i=1}^{\infty} A_{i}^{\prime \prime} \subseteq \bigcup_{i=1}^{\infty} A_{i}^{\prime}
$$

follows that

$$
\sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime \prime}\right) \leqslant \sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime}\right)
$$

Thus

$$
\mu^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime}\right)
$$

$$
\Rightarrow \mu^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime \prime}\right)
$$

Next it will be shown that

$$
A=\bigcup_{i=1}^{\infty} A_{i}^{\prime \prime}
$$

Now since $\left\{A_{i} \xi_{i=1}^{\infty}\right.$ is a covering of $A$

$$
A \subset \bigcup_{i=1}^{\infty} A_{i}
$$

so $x \in A \Rightarrow x \in A_{i}$ for at least one value of ${ }^{\prime}$ c and $x \in A^{\prime} ;$ for one value of $j$ and finally $x \in A_{j}^{\prime \prime}=A_{j}^{\prime} \cap A$ thus

$$
A \subseteq \bigcup_{i=1}^{\infty} A_{i}^{\prime \prime}
$$

Now assume the $x \in \bigcup_{i=1}^{\infty} A_{i}^{\prime \prime}$ since $A^{\prime \prime} i$ are mutually disjoint it follows that for one value
of $c$ that $x \in A_{i}^{\prime \prime}=A_{i}^{\prime} \cap A$ thus $x \in A_{i}^{\prime}$ and $x \in A$ it follows that

$$
A=\bigcup_{i=1}^{\infty} A_{i}^{\prime \prime}
$$

and

$$
\mu(A)=\sum_{i=1}^{\alpha} \mu\left(A_{i}^{\prime \prime}\right)
$$

Thus

$$
\begin{aligned}
& \mu^{*}(A)+\varepsilon \geqslant \sum_{i=1}^{\infty} \mu\left(A_{i}^{\prime \prime}\right) \\
& =\mu^{*}(A)+\varepsilon \geqslant \mu(A)
\end{aligned}
$$

since $\varepsilon$ is arbitrary and the opposite inequality is true it follows that

$$
\mu^{*}(A) \geqslant \mu(A)
$$

Previously it was shown that

$$
\mu^{*}(A) \leqslant \mu(A)
$$

Thus the desired result is
coltained

$$
\mu^{*}(A)=\mu(A)
$$

for $A \in R$

## Proposition: If $A \subseteq B$ then $\mu^{*}(A)<\mu^{*}(B)$

## Proof:

if $l$ is an approximate outter measure of $B$ then

$$
\sum_{i=1}^{\infty} \mu\left(B_{i}\right) \leq \ell
$$

where

$$
B C \sum_{i=1}^{\infty} B_{i}
$$

If $A \subseteq B$ then a covering of $A$ exists.

$$
A \subset \sum_{i=1}^{\infty} A_{i} \subseteq \sum_{i=1}^{\infty} B_{i}
$$

It follows that

$$
\begin{aligned}
& \sum_{i=1}^{\infty} \mu\left(A_{i}\right) \leqslant \sum_{i=1}^{\infty} \mu\left(B_{i}\right) \leqslant l \\
& \Rightarrow \mu^{*}(A) \leqslant \mu^{*}(B)
\end{aligned}
$$

Proposition: $\mu^{*}$ is courtaldy subadditive that is if $A_{1}, A_{2}, A_{3}, \ldots$ are subsets of $X$ then

$$
\mu^{*}\left(\bigcup_{i=1}^{\infty} A_{i}\right) \leq \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

## Proof:

Given $\varepsilon>0$ for each $A_{i}$ a cover of the form

$$
\left\{A_{i j}\right\}_{j=1}^{\infty} \subset R \text { of } A_{i}
$$

where

$$
A_{i} \subset \bigcup_{j=1}^{\infty} A_{i j}
$$

such shat

$$
\mu^{*}\left(A_{i}\right)+\frac{\varepsilon}{2^{i}} \geqslant \sum_{j=1}^{\infty} \mu\left(A_{i j}\right)
$$

since $\left\{A_{i}\right\}_{i=1}^{\Delta}$ covers $A$,

$$
A \subset \bigcup_{i=1}^{\infty} A_{i}
$$

So

$$
A \subset \bigcup_{i=1}^{\infty} \bigcup_{j=1}^{\infty} A_{i j}
$$

and from the definition of approximate outer measure it follows that

$$
\begin{aligned}
\mu^{*}(A) & \leqslant \sum_{i=1}^{\infty} \sum_{j=1}^{\infty} \mu\left(A_{i j}\right) \\
& \leqslant \sum_{i=1}^{\infty}\left[\mu^{*}\left(A_{i}\right)+\frac{\varepsilon_{i}}{\partial^{i}}\right] \\
& =\varepsilon+\sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
\end{aligned}
$$

since $\varepsilon>0$ and arbitrary it follows that

$$
\mu^{*}(A) \leqslant \sum_{i=1}^{\infty} \mu^{*}\left(A_{i}\right)
$$

