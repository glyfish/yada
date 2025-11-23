Linear Algebra

Troy
Stribling
aola/ol/30

## Left and Right Eigenvetors

The right eigenvedor is defined

$$
A x=\lambda x
$$

here $A$ is a square matrix and $x$ a column vector.

Now the right eigenvector is,

$$
A x=\lambda x=\Rightarrow(A-\lambda \text { 便 }) x=0
$$

Where Il is the identity Matrix. The ith component is

$$
\begin{aligned}
& \sum_{k}\left(A_{i k}-\lambda \delta_{i k}\right) x_{k}=0 \\
= & \sum_{k} A_{i k} x_{k}-\lambda x_{i}
\end{aligned}
$$

The left eigenvector is defined by

$$
x^{\top} A=\lambda x^{\top}
$$

here $x^{\top}$ is a row vector
and $A$ a square matrix so

$$
x^{\top} A=\lambda x^{\top} \Rightarrow x^{\top}\left(A-\lambda \mathbb{I}_{1}\right)=0
$$

the $j$ 'th component is

$$
\begin{aligned}
& \sum_{k} x_{k}^{\top}\left(A_{k j}-\lambda \delta_{k j}\right)=0 \\
= & \sum_{k} x_{k}^{\top} A_{k j}-\lambda x_{j}^{\top}
\end{aligned}
$$

Now

$$
\begin{aligned}
A_{k j} & =A_{j k}^{\top} \\
x_{k} & =x_{k}^{\top}
\end{aligned}
$$

80
$\sum_{k} A_{j k}^{\top} X_{k}-\lambda X_{j}$
$\Rightarrow \quad A^{\top} x=\lambda x$
Thus the right eigenvector is defined

$$
\begin{gathered}
A x_{L}=\lambda x_{L} \\
\text { and the left by } \\
A^{\top} x_{R}=\lambda x_{R}
\end{gathered}
$$

## Consider the example

$$
A=\left[\begin{array}{ll}
0.3 & 0.7 \\
0.1 & 0.9
\end{array}\right]
$$

The right eigenvalues are given by

$$
\begin{aligned}
& \operatorname{det}(A-\lambda \mathbb{1})=0 \\
& =\left|\begin{array}{cc}
0.3-\lambda & 0.7 \\
0.1 & 0.9-\lambda
\end{array}\right| \\
& =(0.3-\lambda)(0.9-\lambda)-(0.1)(0.7) \\
& =\left(\frac{3}{10} \frac{9}{10}-\frac{3}{10} \lambda-\frac{9}{10} \lambda+\lambda^{2}\right)-\frac{1}{10} \frac{7}{10}=0 \\
& =\frac{27}{100}-\frac{12}{10} \lambda+\lambda^{2}-\frac{7}{100}=0 \\
& =\frac{20}{100}-\frac{12}{10} \lambda+\lambda^{2}=0
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \lambda^{2}-\frac{12}{10} \lambda=-\frac{2}{10} \\
& \Rightarrow \lambda^{2}-2\left(\frac{6}{10}\right) \lambda=-\frac{2}{10} \\
& \Rightarrow \lambda^{2}-2\left(\frac{6}{10}\right)+\left(\frac{6}{10}\right)^{2}=\left(\frac{6}{10}\right)^{2}-\frac{2}{10} \\
& \Rightarrow\left(\lambda-\frac{6}{10}\right)^{2}=\frac{36}{100}-\frac{20}{100}=\frac{16}{100} \\
& \Rightarrow \lambda-\frac{6}{10}= \pm \sqrt{\frac{16}{100}}= \pm \frac{4}{10} \\
& \Rightarrow \lambda=\frac{6}{10} \pm \frac{4}{10} \\
& \Rightarrow \lambda=\frac{2}{10}, 1
\end{aligned}
$$

Now the eigenvectors are given by
For $\lambda=\frac{2}{10}$ the right eigenvetor is given by

$$
\left[\begin{array}{ll}
3 / 10 & 7 / 10 \\
1 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\frac{2}{10}\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
& \frac{3}{10} x_{1}+\frac{7}{10} x_{2}=\frac{2}{10} x_{1} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{9}{10} x_{2}=\frac{2}{10} x_{2} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
& \frac{1}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
\Rightarrow & x_{1}=-7 x_{2} \Rightarrow \quad x_{2}=-\frac{x}{7}
\end{aligned}
$$

so the right eigenvector for $\lambda=2110$ is, with $\alpha$ an arbitrary scalar

$$
X_{R 1}=\alpha\left[\begin{array}{c}
1 \\
-1 / 7
\end{array}\right]
$$

The right eigenvector for $\lambda=1$

$$
\left[\begin{array}{ll}
3 / 10 & 7 / 10 \\
1 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{7}{10} x_{2}=x_{1} \\
& \frac{1}{10} x_{1}+\frac{9}{10} x_{2}=x_{2} \\
\Rightarrow \quad & -\frac{7}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
& -\frac{9}{10} x_{1}+\frac{9}{10} x_{2}=0 \\
\Rightarrow \quad & x_{1}=x_{1}
\end{aligned}
$$

so the right eigenvector for $\lambda=1$ is with $\beta$ an arbitrary scalar

$$
x_{R 2}=\beta\left[\begin{array}{l}
1 \\
1
\end{array}\right]
$$

Now the left eigenvectors are given by

$$
\operatorname{Cet}\left(A^{\top}-\lambda \mathbb{I}\right)=0
$$

where

$$
A^{\top}=\left[\begin{array}{ll}
0.3 & 0.1 \\
0.7 & 0.9
\end{array}\right]
$$

50

$$
\begin{aligned}
& \operatorname{det}\left(A^{\top}-\lambda \underline{1}\right)=\left|\begin{array}{cc}
3 / 10-\lambda & 1 / 10 \\
7 / 10 & 9 / 10-\lambda
\end{array}\right| \\
\Rightarrow & \left(\frac{3}{10}-\lambda\right)\left(\frac{9}{10}-\lambda\right)-\frac{7}{100}=0
\end{aligned}
$$

which is the same equation obtained for the right eigenvalues. Thus the left and right eigenvalues are the same
The left eigenvector for $\lambda=21,0$ is given by

$$
\begin{gathered}
A^{\top} x_{L 1}=\frac{2}{10} x_{L 1} \\
\Rightarrow\left[\begin{array}{ll}
3 / 10 & 1 / 10 \\
7 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\frac{2}{10}\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
\end{gathered}
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{1}{10} x_{2}=\frac{2}{10} x_{1} \\
& \frac{7}{10} x_{1}+\frac{9}{10} x_{2}=\frac{2}{10} x_{2} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{1}{10} x_{2}=0 \\
& \frac{7}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
\Rightarrow & x_{1}=-x_{2}
\end{aligned}
$$

so the left eigenvector for the eigenvalue $\lambda=2110$ is, with $\gamma$ an erbitrary scalar

$$
x_{L_{1}}=\gamma\left[\begin{array}{c}
1 \\
-1
\end{array}\right]
$$

The left eigenvector for $\lambda=1$

$$
\left[\begin{array}{ll}
3 / 10 & 1 / 10 \\
7 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{1}{10} x_{2}=x_{1} \\
& \frac{7}{10} x_{1}+\frac{9}{10} x_{2}=x_{2} \\
\Rightarrow & -\frac{7}{10} x_{1}+\frac{1}{10} x_{2}=0 \\
& \frac{7}{10} x_{1}-\frac{1}{10} x_{2}=0 \\
\Rightarrow & x_{1}=7 x_{2} \Rightarrow x_{2}=\frac{1}{7} x_{1}
\end{aligned}
$$

Thus the left eigenvedor for $\lambda=l$ is with $\rho$ and arbitrary $\begin{aligned} \text { scalar } & \\ x_{L_{2}} & =\varphi\left[\begin{array}{l}1 \\ 1 / 7\end{array}\right]\end{aligned}$

* In summary for the matrix

$$
A=\left[\begin{array}{ll}
\frac{7}{10} & \frac{3}{10} \\
\frac{1}{10} & \frac{9}{10}
\end{array}\right]
$$

The left and right eigenvalues are equal and given by

$$
\lambda_{1}=\frac{2}{10} \quad \lambda_{2}=1
$$

The right eigenvectors are

$$
x_{R_{1}}=\alpha\left[\begin{array}{c}
1 \\
-\frac{1}{7}
\end{array}\right] \quad x_{R_{2}}=\beta\left[\begin{array}{l}
1 \\
1
\end{array}\right]
$$

and the left eigenvectors are

$$
x_{L 1}=\gamma\left[\begin{array}{c}
1 \\
-1
\end{array}\right] \quad x_{L 2}=\varphi\left[\begin{array}{c}
1 \\
\frac{1}{7}
\end{array}\right]
$$

## Fourier Series

Let $f(x)$ be a function that is nonzero only on the interval

$$
-\frac{1}{2} T \leqslant x \leqslant \frac{1}{2} T
$$

The Fourler Series representation of $f(x)$ is defined by

$$
f(x)=\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n} e^{2 \pi i\left(\frac{n}{T}\right) x}
$$

where the functions $e^{2 \pi \dot{c}\left(\frac{\Delta}{T}\right) x}$ for $m \neq n$ satisfy

$$
\begin{aligned}
& \int_{-\frac{1}{2} T}^{\frac{1}{2} T} e^{2 \pi i\left(\frac{n-m}{T}\right) x} d x \\
= & \left.\frac{T}{2 \pi i(n-m)} e^{2 \pi i\left(\frac{n-m}{T}\right) x}\right|_{-\frac{1}{2} T} ^{\frac{1}{2} T} \\
= & \frac{T}{2 \pi i(n-m)}\left[e^{\pi i(n-m)}-e^{-\pi i(n-m)}\right]
\end{aligned}
$$

$$
\begin{aligned}
& \text { If } m-n \text { is even } \\
& e^{\pi i(n-m)}-e^{-\pi i(n-m)}=1-1=0 \\
& \text { and if } m-n \text { is odb } \\
& e^{\pi i(n-m)}-e^{-\pi i(n-m)}=-1+1=0 \\
& \text { so for } m \neq n \\
& \int_{-\frac{1}{2} T} e^{2 \pi i\left(\frac{n-m}{T}\right) x} d x=0 \\
& \text { if } m=n \\
& \frac{1}{2} T e^{2 \pi i(n-m) x} d x=\int_{-\frac{1}{2} T}^{\frac{1}{2} T} d x=T \\
& \int_{-\frac{1}{2} T} \\
& \text { Thus }
\end{aligned}
$$

The Kronecker $\delta$ function is defined by

$$
\delta_{m n}= \begin{cases}1 & m=n \\ 0 & m \neq n\end{cases}
$$

So
$\frac{1}{2} T$
$\int e^{2 \pi i\left(\frac{n-m}{T}\right) x} d x=T \delta_{m n}$
$-\frac{1}{2} T$
Using this epression and the definition of the Fourier series

$$
f(x)=\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n} e^{2 \pi i\left(\frac{n}{T}\right) x}
$$

Gives an expression for $C_{n}$
$\int_{-\frac{1}{2} T}^{\frac{1}{2} T} f(x) e^{-2 \pi i\left(\frac{m}{T}\right) x} d x$
$=\frac{1}{T} \int_{-\frac{1}{2} T}^{\frac{1}{2} T}\left[\sum_{n=-\infty}^{\infty} F_{n} e^{2 \pi i\left(\frac{n}{T}\right) x}\right] e^{-2 \pi i\left(\frac{m}{T}\right) x} d x$
$=\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n}\left[\int_{-\frac{1}{2} T}^{\frac{1}{2} T} e^{2 \pi i\left(\frac{n-m}{T}\right) x} d x\right]$
$=\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n} T \delta_{m n}=F_{m}$
Trus

$$
F_{m}=\int_{-\frac{1}{2} T}^{\frac{1}{\partial} T} f(x) e^{-2 \pi i\left(\frac{m}{T}\right) x} d x
$$

with

$$
f(x)=\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n} e^{2 \pi i\left(\frac{n}{T}\right) x}
$$

## Discrete Fourier Transform

The Discrete Fourier Transform is derived from the defintion of the Fourier series by
assuming the transformed function $f(x)$ is not continuous but discrete and represented by the sequence

$$
\left(f_{n}\right)=\left(f_{0}, f_{1}, f_{2}, \ldots, f_{N-1}\right)
$$

Recall that the Fourier Series for the continuous case is given by

$$
\begin{aligned}
f(x) & =\frac{1}{T} \sum_{n=-\infty}^{\infty} F_{n} e^{2 \pi i\left(\frac{n}{T}\right) x} \\
F_{m} & =\int_{-\frac{1}{2} T}^{\frac{1}{2} T} f(x) e^{-2 \pi i\left(\frac{m}{T}\right) x} d x
\end{aligned}
$$

For the discret case the Fourier series is assumed to be

$$
f_{n}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{k}{N}\right) n}
$$

where

$$
n=0,1,2, \ldots, N-1
$$

To determine the expression for $F_{m}$ in the discrete case a proccedure similar to that used for the continuous case is used. Starting with

$$
f_{n}=\frac{1}{N} \sum_{K=0}^{N-1} F_{K} e^{2 \pi i\left(\frac{K}{N}\right) n}
$$

Multipling by $e^{-2 \pi i\left(\frac{K}{n}\right) n}$ and summing gives
N-1
$\sum f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k}$
$n=0$
$=\sum_{n=0}^{N-1}\left\{\frac{1}{N} \sum_{m=0}^{N-1} F_{m} e^{2 \pi i\left(\frac{m}{N}\right) n}\right\} e^{-2 \pi i\left(\frac{n}{K}\right) k}$
$=\frac{1}{N} \sum_{n=0}^{N-1} \sum_{m=0}^{N-1} F_{m} e^{2 \pi i\left(\frac{m-k}{N}\right)^{n}}$
$=\frac{1}{N} \sum_{m=0}^{N-1} F_{m} \sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right)^{n}}$
Now consider for $m \neq n$

$$
\sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right) n}
$$

using

$$
\sum_{n=0}^{N-1} r^{n}=\frac{1-r^{N}}{1-r}
$$

with

$$
r=e^{2 \pi i\left(\frac{m-k}{N}\right)}
$$

gives
$\sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right) n}=\frac{1-e^{2 \pi i(m-k)}}{1-e^{2 \pi i(m-k) / N}}$
Now, for numerator the exf.lent will always be a multiple of' $2 \pi$ so

$$
e^{2 \pi i(m-k)}=1
$$

and

$$
1-e^{2 \pi i(m-k)}=0
$$

For the denominator there is only a probem is

$$
e^{2 \pi i(n-k) / N}=1
$$

The two cases where this
will be satisfied

$$
\begin{aligned}
& 2 \pi i \frac{(m-k)}{N}=0 \\
& \left.2 \pi i \frac{(m-k}{N}\right)=l 2 \pi i \quad k \in \mathbb{Z}, k \neq 0
\end{aligned}
$$

where $l$ is a nonzero integer the first case will not occur since it is assumed that $m \neq n$. For the second case it must be the case that

$$
\frac{m-K}{N}=l=m-K=l N
$$

That is the difference between $m$ and $n$ is a multiple of $N$. Now

$$
\begin{aligned}
& m=0,1,2, \ldots N-1 \\
& k=0,1,2, \ldots, N-1
\end{aligned}
$$

If follows that

$$
-N-l \leqslant m-k \leqslant N-l
$$

So there is no $k$ that solves the equation. Petting things together gives

$$
\sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right) n}=0
$$

for $n \neq m$.
For $n=m$

$$
\sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right) n}=\sum_{n=0}^{N-1} 1=N
$$

Thus

$$
\sum_{k=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right)^{n}}=N \delta_{m k}
$$

where

$$
\delta_{m k}= \begin{cases}1 & k=m \\ 0 & k \neq m\end{cases}
$$

This condition rabresents orthgonality of the Fourier Basis Functions

$$
e^{2 \pi i\left(\frac{\tilde{N}}{N}\right) n}
$$

The sums in the expression for the Discrete Fourier coefficient can be evaluated
$\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)^{K}}=\frac{1}{N} \sum_{m=0}^{N-1} F_{m} \sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{m-k}{N}\right)^{n}}$
$=\frac{1}{N} \sum_{m=0}^{N-1} F_{m} N \delta_{k m}=F_{k}$
Thus

$$
\begin{aligned}
& F_{k}=\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k} \\
& f_{n}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k}
\end{aligned}
$$

## Discrete Fourier Transform Properties

Consider a set of samples

$$
\left(f_{n}\right)=\left(f_{0}, f_{1}, f_{2}, \ldots, f_{N-1}\right)
$$

With Discrete Forward and Thuerse Fourier Transforms

$$
\begin{aligned}
& F_{k}=\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k} \\
& f_{n}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k}
\end{aligned}
$$

1) Linearity

$$
\begin{aligned}
& \left(h_{n}\right)=\left(f_{n}\right)+\left(g_{n}\right) \\
H_{k} & =\sum_{n=0}^{N-1} h_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k} \\
& =\sum_{n=0}^{N-1}\left(f_{n}+g_{n}\right) e^{-2 \pi i\left(\frac{n}{N}\right) k} \\
& =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k}+\sum_{n=0}^{N-1} g_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k} \\
& =F_{k}+C_{k}
\end{aligned}
$$

2) Periodicity

$$
\begin{aligned}
F_{k+N} & =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)(k+N)} \\
& =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k} e^{-2 \pi i n}
\end{aligned}
$$

but

$$
e^{-2 \pi i n}=1 \quad \forall n=0,1,2, \ldots
$$

so

$$
F_{k+N}=\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)_{k}}=F_{k}
$$

It is easy to see that for arbitrah shifts by muttiples of mN where

$$
\begin{aligned}
m=\ldots,-2,-1,0,1,2, \ldots & \\
F_{K+m N} & =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)(K+m N)} \\
& =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) K} e^{-2 \pi i m n}
\end{aligned}
$$

but $e^{-2 \pi i m n}=1 \quad \forall m, n$ Thus

$$
\begin{aligned}
& F_{k+m N}=\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)_{k}}=F_{k} \\
& \text { similarly for } f_{n}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k} \\
& f_{n+m N}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n+m N}{N}\right) k} \\
&=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k} e^{2 \pi i m k} \\
& \begin{aligned}
\text { but } \quad & e^{2 \pi i m k}=1 \quad \forall m, k \\
\text { so } & f_{n+m N}
\end{aligned}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k} \\
&=f_{n}
\end{aligned}
$$

3) If $\left(f_{n}\right)$ is real

$$
F_{N-K}=F_{K}^{*}
$$

Now,

$$
\begin{aligned}
F_{N-k} & =\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right)(N-k)} \\
& =\sum_{n=0}^{N-1} f_{n} e^{2 \pi i\left(\frac{n}{N}\right) k} e^{2 \pi i n}
\end{aligned}
$$

but $e^{2 \pi i n}=1 \quad \forall n$

$$
F_{N-K}=\sum_{n=0}^{N-1} f_{n} e^{2 \pi i\left(\frac{n}{N}\right) K}
$$

Now since $f n$ is real taking the complex conjugate gives

$$
\begin{aligned}
F_{k}^{*} & =\left\{\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{n}{N}\right) k}\right\}^{*} \\
& =\sum_{n=0}^{N-1} f_{n} e^{2 \pi i\left(\frac{n}{N}\right) k}
\end{aligned}
$$

so

$$
F_{N-K}=F_{K}^{*}
$$

$$
\begin{aligned}
F_{-k} & =\sum_{n=0}^{N-1} f_{n} e^{2 \pi i\left(\frac{n}{N}\right) k} \\
& =F_{k}^{*}
\end{aligned}
$$

## Discrele Focerier Transform Eample

Let

$$
\left(f_{n}\right)=(8,4,8,0), \quad N=4
$$

and recall that

$$
\begin{aligned}
& f_{k}=\frac{1}{N} \sum_{k=0}^{N-1} F_{k} e^{2 \pi i\left(\frac{n}{N}\right) k} \\
& F_{k}=\sum_{n=0}^{N-1} f_{n} e^{-2 \pi i\left(\frac{k}{N}\right)^{n}}
\end{aligned}
$$

The fourier Transform Basis can be represented by a matrix with and using $N=4$

$$
\begin{aligned}
& \left(T_{0}, k\right)=(1,1,1,1) \\
& \left(T_{1}, k\right)=\left(1, e^{-\frac{\pi}{2} i}, e^{-\pi i}, e^{-\frac{3}{2} \pi i}\right) \\
& \left(T_{2}, k\right)=\left(1, e^{-\pi i}, e^{-2 \pi i}, e^{-3 \pi i}\right) \\
& \left(T_{3}, k\right)=\left(1, e^{-\frac{3}{2} \pi i}, e^{-3 \pi i}, e^{-\frac{9}{2} \pi i}\right)
\end{aligned}
$$

Now

$$
e^{i \theta}=\cos \theta+i \sin \theta
$$

it Follows that

$$
\left(T_{n, k}\right)=\left(\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right)
$$

and

$$
\begin{aligned}
& \left(F_{k}\right)=(T n, k)\left(f_{n}\right) \\
\Rightarrow & \left(\begin{array}{l}
F_{1} \\
F_{2} \\
F_{3} \\
F_{4}
\end{array}\right)=\left(\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right)\left(\begin{array}{l}
8 \\
4 \\
8 \\
0
\end{array}\right) \\
& =\left(\begin{array}{l}
8+4+8+0 \\
8-i 4-8+8 \\
8-4+8+0 \\
8+4 i-8+0
\end{array}\right) \\
= & \left(\begin{array}{l}
20 \\
-4 i \\
12 \\
4 i
\end{array}\right)
\end{aligned}
$$

## Discrete Convolution Theorem

The convolution of two contenuous functions $f(t)$ and $g(t)$ is defined by

$$
f(t) * g(t)=\int_{-\infty}^{\infty} f(\omega) g(t-\omega) d \omega
$$

let

$$
\gamma=t-\omega \Rightarrow \omega=t-\gamma \Rightarrow-d \gamma=d \omega
$$

then

$$
\begin{aligned}
& \int_{-\infty}^{\infty} f(\omega) g(t-\omega) d \omega=-\int_{\infty}^{-\infty} f(t-\gamma) g(\gamma) d \gamma \\
= & \int_{-\infty}^{\infty} f(t-\gamma) g(\gamma) d \gamma
\end{aligned}
$$

Thus

$$
\begin{aligned}
f(t) * g(t) & =\int_{-\infty}^{\infty} f(\omega) g(t-\omega) d \omega \\
& =\int_{-\infty}^{\infty} f(t-\omega) g(\omega) d \omega
\end{aligned}
$$

The descrete convolution is defined by

$$
\begin{aligned}
h_{n}=\left(f_{n}\right) *\left(g_{n}\right) & =\sum_{m=-\infty}^{\infty} f_{m} g_{n-m} \\
& =\sum_{m=-\infty}^{\infty} f_{n-m} g_{m}
\end{aligned}
$$

If $f_{n}$ and $g_{n}$ take on only a finite number of values N ,

$$
\begin{aligned}
& \left(f_{n}\right)=\left(f_{0}, f_{1}, f_{2}, \ldots, f_{N-1}\right) \\
& \left(g_{n}\right)=\left(g_{0}, g_{1}, g_{2}, \ldots, g_{n-1}\right)
\end{aligned}
$$

Then

$$
\begin{aligned}
& f_{n}=\sum_{k=0}^{N-1} f_{k} \delta(n-k) \\
& g_{n}=\sum_{k=0}^{N-1} g_{k} \delta(n-k)
\end{aligned}
$$

where

$$
\delta(n-k)= \begin{cases}1 & n-k=0 \\ 0 & n-k \neq 0\end{cases}
$$

SO,
so

$$
\begin{aligned}
& h_{n}=\sum_{m=-\infty}^{\infty} f_{m} g_{n-m} \\
= & \sum_{m=-\infty}^{\infty}\left\{\sum_{k=0}^{N-1} f_{k} \delta(m-k)\right\}\left\{\sum_{j=0}^{N-1} g_{j} \delta(n-m-j)\right\} \\
= & \left.\sum_{k=0}^{N-1} \sum_{j=0}^{N-1} \sum_{m=-\infty}^{\infty} f_{k} \delta(m-k) g_{j} \delta(n-m-j)\right\}
\end{aligned}
$$

For the $m$ sum the only nonzero terms are

$$
m=K \text { and } m=n-j
$$

50

$$
K=n-j
$$

and

$$
\begin{aligned}
h_{n} & =\sum_{k=0}^{N-1} \sum_{j=0}^{N-1} f_{k} g_{j} \delta(n-k-j) \\
& =\sum_{k=0}^{N-1} f_{k} g_{n-k}
\end{aligned}
$$

Now the Discrete Convolution Theorem states

$$
H_{k}=F_{k} E_{k}, \quad k=0,1,2, \ldots, N-1
$$

where

$$
H_{k}=\frac{1}{N} \sum_{n=0}^{N-1} h_{k} e^{-2 \pi i\left(\frac{n}{N}\right)^{k}}
$$

This can be seen from the definition of Discret convolution

$$
h_{k}=\sum_{n=0}^{N-1} f_{n} g_{k-n}
$$

and

$$
\begin{aligned}
f_{n} & =\frac{1}{N} \sum_{p=0}^{N-1} F_{p} e^{2 \pi i\left(\frac{P}{N}\right) n} \\
g_{k-n} & =\frac{1}{N} \sum_{l=0}^{N-1} f_{l} e^{2 \pi i\left(\frac{l}{N}\right)(k-n)}
\end{aligned}
$$

gives
$h_{k}=\sum_{n=0}^{N-1}\left\{\frac{1}{N} \sum_{p=0}^{N-1} F_{p} e^{2 \pi i\left(\frac{P}{N}\right) n}\right\}$

$$
\left\{\frac{1}{N} \sum_{l=0}^{N-1} G_{l} e^{2 \pi i\left(\frac{l}{N}\right)(k-n)}\right\}
$$

$=\frac{1}{N^{2}}\left\{\sum_{P=0}^{N-1} F_{P} \sum_{l=0}^{N-1} e_{l} e^{2 \pi i\left(\frac{l}{N}\right) k}\right\}$
$\left\{\sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{R}{N}\right) n} e^{-2 \pi i\left(\frac{l}{N}\right) n}\right\}$
$=\frac{1}{N^{2}} \sum_{P=0}^{N-1} F_{P} \sum_{l=0}^{N-1} G_{l} e^{2 \pi i\left(\frac{l}{N}\right) k} \sum_{n=0}^{N-1} e^{2 \pi i\left(\frac{P-l}{N}\right)^{n}}$
N-1 N-1
$=\frac{1}{N^{2}} \sum_{p=0}^{N-1} F_{p} \sum_{l=0}^{N-1} G_{l} e^{2 \pi i\left(\frac{l}{N}\right) K} N \delta_{p l}$
N-1
$=\frac{1}{N} \sum_{l=0}^{N} F_{l} G_{l} e^{2 \pi i\left(\frac{l}{N}\right) k}$
$\Rightarrow h_{k}=\frac{1}{N} \sum_{l=0}^{N-1} F_{l} G_{l} e^{2 \pi i\left(\frac{l}{N}\right) k}$

Now

$$
\begin{aligned}
& H_{m}=\sum_{k=0}^{N-1} h_{k} e^{-2 \pi i\left(\frac{m}{N}\right)^{k}} \\
= & \sum_{k=0}^{N-1}\left\{\frac{1}{N} \sum_{l=0}^{N-1} F_{l} G_{l} e^{-2 \pi i\left(\frac{l}{N}\right) k}\right\} e^{2 \pi i\left(\frac{m}{N}\right) k} \\
= & \frac{1}{N} \sum_{l=0}^{N-1} F_{l} G_{l} \sum_{k=0}^{N-1} e^{2 \pi i\left(\frac{m_{-}}{N}\right) k} \\
= & \frac{1}{N} \sum_{l=0}^{N-1} F_{l} G_{l} N \delta_{m l} \\
= & F_{m} G_{m}
\end{aligned}
$$

To verify

$$
\begin{aligned}
h_{n} & =\frac{1}{N} \sum_{K=0}^{N-1} H_{K} e^{2 \pi i\left(\frac{K}{N}\right) n} \\
& =\frac{1}{N} \sum_{m=0}^{N-1} F_{m} G_{m} e^{2 \pi i\left(\frac{m}{N}\right) n}
\end{aligned}
$$

using

$$
\begin{aligned}
& F_{m}=\sum_{k=0}^{N-1} f_{k} e^{-2 \pi i\left(\frac{m}{N}\right) k} \\
& G_{m}=\sum_{l=0}^{N-1} g_{l} e^{-2 \pi i\left(\frac{m}{N}\right) l}
\end{aligned}
$$

gives

$$
\begin{aligned}
n_{n} & =\frac{1}{N} \sum_{m=0}^{N-1}\left\{\sum_{k=0}^{N-1} f_{k} e^{-2 \pi i\left(\frac{m}{N}\right) k}\right\} \\
& \left\{\sum_{e=0}^{N-1} g_{l} e^{-2 \pi i\left(\frac{m}{N}\right) l}\right\} e^{2 \pi i\left(\frac{m}{N}\right) n} \\
& =\frac{1}{N} \sum_{k=0}^{N-1} f_{k} \sum_{l=0}^{N-1} g_{l} \sum_{m=0}^{N-1} e^{2 \pi i\left(\frac{n-k-l}{N}\right)^{m}} \\
& =\frac{1}{N} \sum_{k=0}^{N-1} f_{k} \sum_{l=0}^{N-1} g_{l} N \delta_{n-k-l} \\
& =\sum_{k=0}^{N-1} f_{k} g_{n-k}
\end{aligned}
$$

## Discrete Cenvolution Theorem Earmples

In the Discrete Fourier Transform Eample section the Fourier Transform Basis Matrix for $N=4$

$$
T_{n, k}=\left(\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -1 & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right)
$$

The transform for the vedor

$$
\begin{aligned}
& \left(f_{n}\right)=(8,4,8,0), N=4 \\
& \left(F_{k}\right)=\left(\begin{array}{c}
20 \\
-4 i \\
12 \\
4 i
\end{array}\right)
\end{aligned}
$$

Another is nceded to test the Convolution Theorem another example is needed. Consider,

$$
\left(g_{n}\right)=(6,3,9,3)
$$

The Discrete Fourier Transform $\left(G_{k}\right)$ is given loy

$$
\begin{aligned}
\left(\epsilon_{k}\right) & =(\operatorname{Tn}, k)\left(g_{n}\right) \\
& =\left(\begin{array}{cccc}
1 & 1 & 1 & 1 \\
1 & -i & -1 & i \\
1 & -i & 1 & -1 \\
1 & i & -1 & -i
\end{array}\right)\left(\begin{array}{l}
6 \\
3 \\
9 \\
3
\end{array}\right) \\
& =\left(\begin{array}{c}
6+3+9+3 \\
6-3 i-9+3 i \\
6-3+9-3 \\
6+3 i-9-3 i
\end{array}\right) \\
& =\left(\begin{array}{c}
21 \\
-3 \\
9 \\
-3
\end{array}\right)
\end{aligned}
$$

The Discrete Convolution is defined by

$$
N-1
$$

$n_{n}=\left(f_{n}\right) *\left(g_{n}\right)=\sum_{m=0}^{N-1} f_{m} g_{n-m}$
Now recall that

$$
\begin{aligned}
& \left(f_{n}\right)=(8,4,8,0) \\
& \left(g_{n}\right)=(6,3,9,3)
\end{aligned}
$$

so create a table of shifts of $g$ by rotating
(gm) about $m=0$ and shift right for each value of $n$. The convolution for each $n$ is computed from the overlap with (tm)

| $m$ |  |  |  | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $f_{m}$ |  |  |  | 8 | 4 | 8 | 0 |
| $g_{-m}$ | 3 | 9 | 3 | 6 |  |  |  |
| $g_{1-m}$ |  | 3 | 9 | 3 | 6 |  |  |
| $g_{2-m}$ |  |  | 3 | 9 | 3 | 6 |  |
| $g_{3-m}$ |  |  |  | 3 | 9 | 3 | 6 |

$$
\begin{aligned}
& h_{0}=6.8=48 \\
& h_{1}=3.8+6.4=48 \\
& h_{2}=9.8+3.4+6.8=132 \\
& h_{3}=3.8+9.4+3.8+0.6=84
\end{aligned}
$$

If the Piscrete convolution Treorem is use to evaluate ( $n_{n}$ ) the Discrele Fourier implicitly assumes the ( $f_{n}$ ) and ( $g n$ ) are periodic with period $N$.
A straight forward application will produce the result,

| $m$ | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| $f_{m}$ | 8 | 4 | 8 | 0 |
| $g_{-m}$ | 6 | 3 | 9 | 3 |
| $g_{1-m}$ | 3 | 6 | 3 | 9 |
| $g_{2-m}$ | 9 | 3 | 6 | 3 |
| $g_{3-m}$ | 3 | 9 | 3 | 6 |

$h_{0}=6.8+3.4+9.8+3.0=132$
$n_{1}=3 \cdot 8+6 \cdot 4+3 \cdot 8+9 \cdot 0=72$
$n_{2}=9.8+3.4+6.8+3.0=132$
$n_{3}=3 \cdot 8+9 \cdot 4+3 \cdot 8+6 \cdot 0=84$

This problem can be overcome by padding the end of ( $f_{n}$ ) and (gn) with N-1 zeros producins vectors of length $2 \mathrm{~N}-1$

| $m$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $f_{m}$ | 0 | 0 | 0 | 8 | 4 | 8 | 0 |
| $g_{-m}$ | 3 | 9 | 3 | 6 | 0 | 0 | 0 |
| $g_{1-m}$ | 0 | 3 | 9 | 3 | 6 | 0 | 0 |
| $g_{2-m}$ | 0 | 0 | 3 | 9 | 3 | 6 | 0 |
| $g_{3-m}$ | 0 | 0 | 0 | 3 | 9 | 3 | 6 |
| $g_{4-m}$ | 6 | 0 | 0 | 0 | 3 | 9 | 3 |
| $g_{5-m}$ | 3 | 6 | 0 | 0 | 0 | 3 | 9 |
| $g_{6-m}$ | 9 | 3 | 6 | 0 | 0 | 0 | 3 |

$h_{0}=8.6+4.0+8.0+0.0=48 n_{1}=8.3+4.6+8.0+0.0=48 h_{2}=8.9+4.3+8.6+0.0=132 n_{3}=8.3+4.9+8.3+0.6=84$
$h_{4}=8.0+4.3+8.9+0.3=84$
$h_{5}=8.0+4.0+8.3+0.9=24$
$n_{6}=8.0+4.0+8.0+0.3=0$

The answere is contained in the first $N$ elements. The last N-1 elements contain percodicity errors.

## Left and Right Eigenvetors

The right eigenvedor is defined

$$
A x=\lambda x
$$

here $A$ is a square matrix and $x$ a column vector.

Now the right eigenvector is,

$$
A x=\lambda x=\Rightarrow(A-\lambda \text { 便 }) x=0
$$

Where Il is the identity Matrix. The ith component is

$$
\begin{aligned}
& \sum_{k}\left(A_{i k}-\lambda \delta_{i k}\right) x_{k}=0 \\
= & \sum_{k} A_{i k} x_{k}-\lambda x_{i}
\end{aligned}
$$

The left eigenvector is defined by

$$
x^{\top} A=\lambda x^{\top}
$$

here $x^{\top}$ is a row vector
and $A$ a square matrix so

$$
x^{\top} A=\lambda x^{\top} \Rightarrow x^{\top}\left(A-\lambda \mathbb{I}_{1}\right)=0
$$

the $j$ 'th component is

$$
\begin{aligned}
& \sum_{k} x_{k}^{\top}\left(A_{k j}-\lambda \delta_{k j}\right)=0 \\
= & \sum_{k} x_{k}^{\top} A_{k j}-\lambda x_{j}^{\top}
\end{aligned}
$$

Now

$$
\begin{aligned}
A_{k j} & =A_{j k}^{\top} \\
x_{k} & =x_{k}^{\top}
\end{aligned}
$$

80
$\sum_{k} A_{j k}^{\top} X_{k}-\lambda X_{j}$
$\Rightarrow \quad A^{\top} x=\lambda x$
Thus the right eigenvector is defined

$$
\begin{gathered}
A x_{L}=\lambda x_{L} \\
\text { and the left by } \\
A^{\top} x_{R}=\lambda x_{R}
\end{gathered}
$$

## Consider the example

$$
A=\left[\begin{array}{ll}
0.3 & 0.7 \\
0.1 & 0.9
\end{array}\right]
$$

The right eigenvalues are given by

$$
\begin{aligned}
& \operatorname{det}(A-\lambda \mathbb{1})=0 \\
& =\left|\begin{array}{cc}
0.3-\lambda & 0.7 \\
0.1 & 0.9-\lambda
\end{array}\right| \\
& =(0.3-\lambda)(0.9-\lambda)-(0.1)(0.7) \\
& =\left(\frac{3}{10} \frac{9}{10}-\frac{3}{10} \lambda-\frac{9}{10} \lambda+\lambda^{2}\right)-\frac{1}{10} \frac{7}{10}=0 \\
& =\frac{27}{100}-\frac{12}{10} \lambda+\lambda^{2}-\frac{7}{100}=0 \\
& =\frac{20}{100}-\frac{12}{10} \lambda+\lambda^{2}=0
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \lambda^{2}-\frac{12}{10} \lambda=-\frac{2}{10} \\
& \Rightarrow \lambda^{2}-2\left(\frac{6}{10}\right) \lambda=-\frac{2}{10} \\
& \Rightarrow \lambda^{2}-2\left(\frac{6}{10}\right)+\left(\frac{6}{10}\right)^{2}=\left(\frac{6}{10}\right)^{2}-\frac{2}{10} \\
& \Rightarrow\left(\lambda-\frac{6}{10}\right)^{2}=\frac{36}{100}-\frac{20}{100}=\frac{16}{100} \\
& \Rightarrow \lambda-\frac{6}{10}= \pm \sqrt{\frac{16}{100}}= \pm \frac{4}{10} \\
& \Rightarrow \lambda=\frac{6}{10} \pm \frac{4}{10} \\
& \Rightarrow \lambda=\frac{2}{10}, 1
\end{aligned}
$$

Now the eigenvectors are given by
For $\lambda=\frac{2}{10}$ the right eigenvetor is given by

$$
\left[\begin{array}{ll}
3 / 10 & 7 / 10 \\
1 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\frac{2}{10}\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
& \frac{3}{10} x_{1}+\frac{7}{10} x_{2}=\frac{2}{10} x_{1} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{9}{10} x_{2}=\frac{2}{10} x_{2} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
& \frac{1}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
\Rightarrow & x_{1}=-7 x_{2} \Rightarrow \quad x_{2}=-\frac{x}{7}
\end{aligned}
$$

so the right eigenvector for $\lambda=2110$ is, with $\alpha$ an arbitrary scalar

$$
X_{R 1}=\alpha\left[\begin{array}{c}
1 \\
-1 / 7
\end{array}\right]
$$

The right eigenvector for $\lambda=1$

$$
\left[\begin{array}{ll}
3 / 10 & 7 / 10 \\
1 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{7}{10} x_{2}=x_{1} \\
& \frac{1}{10} x_{1}+\frac{9}{10} x_{2}=x_{2} \\
\Rightarrow \quad & -\frac{7}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
& -\frac{9}{10} x_{1}+\frac{9}{10} x_{2}=0 \\
\Rightarrow \quad & x_{1}=x_{1}
\end{aligned}
$$

so the right eigenvector for $\lambda=1$ is with $\beta$ an arbitrary scalar

$$
x_{R 2}=\beta\left[\begin{array}{l}
1 \\
1
\end{array}\right]
$$

Now the left eigenvectors are given by

$$
\operatorname{Cet}\left(A^{\top}-\lambda \mathbb{I}\right)=0
$$

where

$$
A^{\top}=\left[\begin{array}{ll}
0.3 & 0.1 \\
0.7 & 0.9
\end{array}\right]
$$

50

$$
\begin{aligned}
& \operatorname{det}\left(A^{\top}-\lambda \underline{1}\right)=\left|\begin{array}{cc}
3 / 10-\lambda & 1 / 10 \\
7 / 10 & 9 / 10-\lambda
\end{array}\right| \\
\Rightarrow & \left(\frac{3}{10}-\lambda\right)\left(\frac{9}{10}-\lambda\right)-\frac{7}{100}=0
\end{aligned}
$$

which is the same equation obtained for the right eigenvalues. Thus the left and right eigenvalues are the same
The left eigenvector for $\lambda=21,0$ is given by

$$
\begin{gathered}
A^{\top} x_{L 1}=\frac{2}{10} x_{L 1} \\
\Rightarrow\left[\begin{array}{ll}
3 / 10 & 1 / 10 \\
7 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\frac{2}{10}\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
\end{gathered}
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{1}{10} x_{2}=\frac{2}{10} x_{1} \\
& \frac{7}{10} x_{1}+\frac{9}{10} x_{2}=\frac{2}{10} x_{2} \\
\Rightarrow & \frac{1}{10} x_{1}+\frac{1}{10} x_{2}=0 \\
& \frac{7}{10} x_{1}+\frac{7}{10} x_{2}=0 \\
\Rightarrow & x_{1}=-x_{2}
\end{aligned}
$$

so the left eigenvector for the eigenvalue $\lambda=2110$ is, with $\gamma$ an erbitrary scalar

$$
x_{L_{1}}=\gamma\left[\begin{array}{c}
1 \\
-1
\end{array}\right]
$$

The left eigenvector for $\lambda=1$

$$
\left[\begin{array}{ll}
3 / 10 & 1 / 10 \\
7 / 10 & 9 / 10
\end{array}\right]\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]=\left[\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right]
$$

$$
\begin{aligned}
\Rightarrow & \frac{3}{10} x_{1}+\frac{1}{10} x_{2}=x_{1} \\
& \frac{7}{10} x_{1}+\frac{9}{10} x_{2}=x_{2} \\
\Rightarrow & -\frac{7}{10} x_{1}+\frac{1}{10} x_{2}=0 \\
& \frac{7}{10} x_{1}-\frac{1}{10} x_{2}=0 \\
\Rightarrow & x_{1}=7 x_{2} \Rightarrow x_{2}=\frac{1}{7} x_{1}
\end{aligned}
$$

Thus the left eigenvedor for $\lambda=l$ is with $\rho$ and arbitrary $\begin{aligned} \text { scalar } & \\ x_{L_{2}} & =\varphi\left[\begin{array}{l}1 \\ 1 / 7\end{array}\right]\end{aligned}$

* In summary for the matrix

$$
A=\left[\begin{array}{ll}
\frac{7}{10} & \frac{3}{10} \\
\frac{1}{10} & \frac{9}{10}
\end{array}\right]
$$

The left and right eigenvalues are equal and given by

$$
\lambda_{1}=\frac{2}{10} \quad \lambda_{2}=1
$$

The right eigenvectors are

$$
x_{R_{1}}=\alpha\left[\begin{array}{c}
1 \\
-\frac{1}{7}
\end{array}\right] \quad x_{R_{2}}=\beta\left[\begin{array}{l}
1 \\
1
\end{array}\right]
$$

and the left eigenvectors are

$$
x_{L 1}=\gamma\left[\begin{array}{c}
1 \\
-1
\end{array}\right] \quad x_{L 2}=\varphi\left[\begin{array}{c}
1 \\
\frac{1}{7}
\end{array}\right]
$$

