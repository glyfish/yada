Functions

Troy Fribling
Feb. 19, 2017
$\qquad$
$\qquad$
$\qquad$
$\qquad$

## Gamma Function

The Camma Function, $\Gamma(x)$, is defined by the impoper integral

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

* For $x \geqslant 1$ show that the integral converges.

Now

$$
\begin{aligned}
& \int_{0}^{\infty} t^{x-1} e^{-t} d t=\int_{0}^{a} t^{x-1} e^{-t} d t \\
& +\int_{a}^{\infty} t^{x-1} e^{-t} d t
\end{aligned}
$$

for the fist integral

$$
t^{x-1} e^{-t} \leq t^{x-1} \text { for } 0 \leq t \leq a
$$

so

$$
\begin{aligned}
& \int_{0}^{a} t^{x-1} e^{-t} d t \leq \int_{0}^{a} t^{x-1} d t \\
& =\left.\frac{t^{x}}{x}\right|_{0} ^{a}=\frac{a^{x}}{x}
\end{aligned}
$$

So the first intergl converges.
For the second if $a$ is large so that $t$ is large

$$
\begin{aligned}
& \frac{t^{x-1}}{e^{t / 2}} \ll 1 \\
= & t^{x-1} \ll e^{t / 2}
\end{aligned}
$$

This follows from

$$
e^{t / 2}=\sum_{n=0}^{\infty} \frac{1}{2^{n} n!} t^{n}
$$

since there will be some $m$ such that

$$
\sum_{n=0}^{m} \frac{1}{2^{n} n!} t^{n} \geqslant t^{x-1}
$$

So the second integral becomes

$$
\begin{aligned}
& \int_{a}^{\infty} t^{x-1} e^{-t} d t<\int_{a}^{\infty} e^{t / 2} e^{-t} d t \\
& =\int_{a}^{\infty} e^{-t / 2} d t=-\left.2 e^{-t / 2}\right|_{a} ^{\infty}
\end{aligned}
$$

$$
=0+2 e^{-a / 2}=2 e^{-a / 2}
$$

Thus both indegrals converge and

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

converges for $x \geqslant 1$.

* For $0<x<1$ show that $\Gamma(x)$ Converges.

$$
\Gamma(x)=\lim _{r \rightarrow 0^{+}} \int_{r}^{1} t^{x-1} e^{-t} d t
$$

Since $0<x<1$ and $0<t<1$

$$
t^{x-1}>1
$$

and

$$
e^{-t}<1
$$

50

$$
t^{x-1} e^{-t}<t^{x-1}
$$

and

$$
\lim _{r \rightarrow 0^{+}} \int_{r} t^{x-1} e^{-t} d t<\lim _{r \rightarrow 0^{+}} \int_{r} t^{x-1} d t
$$

$$
\begin{aligned}
& =\left.\lim _{r \rightarrow 0^{+}} \frac{t^{x}}{x}\right|_{r} ^{\prime}=\lim _{r \rightarrow 0^{+}}\left(\frac{1}{x}-\frac{r^{x}}{x}\right) \\
& =\frac{1}{x}
\end{aligned}
$$

thus

$$
\Gamma(x)<\frac{1}{x}
$$

and

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

is defined for all $x>0$.

* Show that for $x>0$

$$
\Gamma(x+1)=x \Gamma(x)
$$

Proof:

$$
\Gamma(x+1)=\int_{0}^{\infty} t^{x} e^{-t} d t
$$

using integration by parts

$$
\int u d v=u v-\int v d u
$$

let

$$
u=t^{x} \Rightarrow d u=x t^{x-1}
$$

and

$$
d v=e^{-t} d t \Rightarrow v=-e^{-t}
$$

So

$$
\begin{aligned}
\Gamma(x+1) & =-\left.t^{x} e^{-t}\right|_{0} ^{\infty}+\int_{0}^{\infty} x t^{x-1} e^{-t} d t \\
& =0-0+x \int_{0}^{\infty} t^{x-1} e^{-t} d t \\
& =x \Gamma(x)
\end{aligned}
$$

* Show that for

$$
\begin{aligned}
& x=n \quad n=1,2,3, \ldots \\
& \Gamma(n+1)=n!
\end{aligned}
$$

Proof

$$
\begin{aligned}
\Gamma(1) & =\int_{0}^{\infty} e^{-t} d t=-e^{-t} p_{0}^{\infty} \\
& =-0+1=0
\end{aligned}
$$

using the recurrence relation

$$
\Gamma(x+1)=x \Gamma(x)
$$

gives

$$
\begin{aligned}
& \Gamma(2)=\Gamma(1)=1 \\
& \Gamma(3)=2 \Gamma(2)=2 \\
& \Gamma(4)=3 \Gamma(3)=3 \cdot 2 \\
& \Gamma(5)=4 \Gamma(4)=4 \cdot 3 \cdot 2
\end{aligned}
$$

50

$$
\Gamma(n+1)=n!
$$

* Snow trat for a Normal distribution

$$
\int_{-\infty}^{\infty} e^{-x^{2}} d x=\Gamma\left(l_{2}\right)=\sqrt{\pi}
$$

using $u$ substitution with

$$
\begin{aligned}
& u=x^{2} \Rightarrow d u=2 x d x \\
& =2 u^{1 / 2} d x \Rightarrow d x=\frac{d u}{2 u^{1 / 2}}
\end{aligned}
$$

and using

$$
\int_{-\infty}^{\infty} e^{-x^{2}} d x=2 \int_{0}^{\infty} e^{-x^{2}} d x
$$

gives

$$
\begin{aligned}
& \int_{-\infty}^{\infty} e^{-x^{2}} d x=2 \int_{0}^{\infty} e^{-u}\left(\frac{1}{\partial u^{1 / 2}}\right) d u \\
& =\int_{0}^{\infty} u^{-1 / 2} e^{-u} d u \\
& =\int_{0}^{\infty} u^{1 / 2-1} e^{-u} d u=\Gamma(1 / 2)
\end{aligned}
$$

but

$$
\int_{-\infty}^{\infty} e^{x^{2}} d x=\sqrt{\pi}
$$

so

$$
\Gamma\left(l^{\prime} 2\right)=\sqrt{\pi}
$$

* Find a product representation

Consider,

$$
e^{-t}=\lim _{n \rightarrow \infty}\left(1-\frac{t}{n}\right)^{n}
$$

and define

$$
\begin{aligned}
\Gamma(x) & =\lim _{n \rightarrow \infty} \Gamma(x, n) \\
& =\lim _{n \rightarrow \infty} \int_{0}^{n} t^{x-1}\left(1-\frac{t}{n}\right)^{n} d t
\end{aligned}
$$

let

$$
\begin{aligned}
& n z=t \\
\Rightarrow \quad & n d z=d t
\end{aligned}
$$

Substituting in the integral above gives

$$
\begin{aligned}
\Gamma(x, n) & =\int_{0}^{1} t^{x-1}\left(1-\frac{t}{n}\right)^{n} d t \\
& =\int_{0}^{1}(n z)^{x-1}(1-z)^{n} n d z \\
& =n^{x} \int_{0}^{1} z^{x-1}(1-z)^{n} d z
\end{aligned}
$$

$$
\begin{array}{r}
\text { Integrating by parts } \\
\text { Sudv }=u v-S v d u
\end{array}
$$

where

$$
\begin{aligned}
& d v=z^{x-1} d z \Rightarrow v=\frac{z^{x}}{x} \\
& u=(1-z)^{n} \Rightarrow d u=-n(1-z)^{n-1}
\end{aligned}
$$

so

$$
\begin{aligned}
& \int_{0}^{1} z^{x-1}(1-z)^{n} d z \\
= & \left.\frac{z^{x}}{x}(1-z)^{n}\right|_{0} ^{1}+\frac{n}{x} \int_{0}^{1} z^{x}(1-z)^{n-1} d z
\end{aligned}
$$

$$
=\frac{n}{x} \int_{0}^{1} z^{x}(1-z)^{n-1} d
$$

So

$$
\Gamma(x, n)=\frac{n^{x+1}}{x} \int_{0}^{1} z^{x}(1-z)^{n-1} d z
$$

using

$$
\Gamma(x, n)=n^{x} \int_{0}^{1} z^{x-1}(1-z)^{n} d z
$$

Sives

$$
\begin{aligned}
& \Gamma(x+1, n-1)=(n-1)^{x+1} \int_{0} z^{x}(1-z)^{n-1} d z \\
\Rightarrow & \left(\frac{n}{n-1}\right)^{x+1} \Gamma(x+1, n-1)=n^{x+1} \int_{0}^{1} z^{x}(1-z)^{n-1} d z
\end{aligned}
$$

and the recurrence relation

$$
\Gamma(x, n)=\frac{1}{x}\left(\frac{n}{n-1}\right)^{x+1} \Gamma(x+1, n-1)
$$

Now from the defintion of $\Gamma(x, n)$

$$
\begin{aligned}
\Gamma(x, 1) & =\frac{1}{x} \int_{0}^{1} z^{x} d z=\left.\frac{1}{x(x+1)} z^{x+1}\right|_{0} ^{1} \\
& =\frac{1}{x(x+1)}
\end{aligned}
$$

using the recurvence relation

$$
\Gamma(x, n)=\frac{1}{x}\left(\frac{n}{n-1}\right)^{x+1} \Gamma(x+1, n-1)
$$

we have

$$
\begin{aligned}
\Gamma(x, 2) & =\frac{1}{x} 2^{x+1} \Gamma(x+1,1) \\
& =2^{x+1} \frac{1}{x(x+1)(x+2)} \\
\Gamma(x, 3) & =\frac{1}{x}\left(\frac{3}{2}\right)^{x+1} \Gamma(x+1,2) \\
& =\frac{1}{x}\left(\frac{3}{2}\right)^{x+1}\left[2^{x+2} \frac{1}{(x+1)(x+2)(x+3)}\right] \\
& =2(3)^{x+1} \frac{1}{x(x+1)(x-12)(x+3)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{3^{x}(2)(3)}{x(x+1)(x+2)(x+3)} \\
& \Gamma(x, 4)=\frac{1}{x}\left(\frac{4}{3}\right)^{x+1} \Gamma(x+1,3) \\
& =\frac{1}{x}\left(\frac{4}{3}\right)^{x+1}\left[\frac{3^{x+1}(2 x(3)}{(x+1)(x+2 x x+3 x x+4)}\right] \\
& =\frac{4^{x+1}(2 x 3)}{x(x+1(x+2)(x+3)(x+4)} \\
& =\frac{4^{x}(2 x 3)(4)}{x(x+1)(x+2)(x+3)(x+4)} \\
& =\frac{4^{x} 4!}{x(x+1)(x+2)(x+3)(x+4)}
\end{aligned}
$$

Tuns

$$
\Gamma(x, n)=\frac{n^{x} n^{1}}{x(x+1)(x-2) \cdots(x+n)}
$$

and

$$
\Gamma(x)=\lim _{n \rightarrow \infty} n^{x} \frac{n!}{x(x+1)(x+2) \cdots(x+n)}
$$

* Derivatives of $\Gamma(x)$

Consider the recurrence relation

$$
\Gamma(x+1)=x \Gamma(x)
$$

so

$$
\begin{aligned}
\ln \Gamma(x+1) & =\ln [x \Gamma(x)] \\
& =\ln x+\ln \Gamma(x)
\end{aligned}
$$

and

$$
\frac{d}{d x} \ln \Gamma(x+1)=\frac{1}{x}+\frac{d}{d x} \ln \Gamma(x)
$$

$\Rightarrow \frac{1}{\Gamma(x+1)} \Gamma^{\prime}(x+1)=\frac{1}{x}+\frac{1}{\Gamma(x)} \Gamma^{\prime}(x)$
$\Rightarrow \frac{\Gamma^{\prime}(x+1)}{\Gamma(x+1)}=\frac{1}{x}+\frac{\Gamma^{\prime}(x)}{\Gamma(x)}$
Define the Digamma function by

$$
\psi(x)=\frac{\Gamma^{\prime}(x)}{\Gamma(x)}
$$

then

$$
\psi(x+1)=\frac{1}{x}+\psi(x)
$$

If $\quad x=n=1,2,3, \ldots$

$$
\begin{aligned}
& \psi(2)=1+\psi(1) \\
& \psi(3)=\frac{1}{2}+\psi(2)=1+\frac{1}{2}+\psi(1) \\
& \psi(4)=\frac{1}{3}+\psi(3)=1+\frac{1}{2}+\frac{1}{3}+\psi(1)
\end{aligned}
$$

and

$$
\psi(n+1)=\psi(1)+\sum_{k=1}^{n} \frac{1}{k}
$$

## Beta Function

The Beta Function is defined by

$$
B(a, b)=\int_{0}^{1} t^{a-1}(1-t)^{b-1} d t
$$

To show the rebutionship between $B(a, b)$ and $\Gamma(x)$ make the change of varibles

$$
\begin{aligned}
& u=\frac{t}{1-t} \\
\Rightarrow & u(1-t)=t \\
\Rightarrow & u=t(u+1) \\
\Rightarrow & t=\frac{u}{u t} \\
\Rightarrow & d t=\left[\frac{1}{u+1}-\frac{u}{(u+1)^{2}}\right] d u \\
& =\left[\frac{u+1-u}{(u+1)^{2}}\right] d u \\
& =\frac{1}{(u+1)^{2}} d u
\end{aligned}
$$

SO

$$
\begin{aligned}
& B(a, b)=\int_{0}^{1} t^{a-1}(1-t)^{b-1} d t \\
= & \int_{0}^{\infty}\left(\frac{u}{u+1}\right)^{a-1}\left(1-\frac{u}{u+1}\right)^{b-1} \frac{1}{(u+1)^{2}} d u \\
= & \int_{0}^{\infty}\left(\frac{u}{u+1}\right)^{a-1}\left(\frac{1}{u+1}\right)^{b-1} \frac{1}{(u+1)^{2}} d u \\
= & \int_{0}^{\infty} \frac{u^{a-1}}{(u+1)^{a+b}} d u
\end{aligned}
$$

Rerall that

$$
\Gamma(x)=\int_{0}^{\infty} t^{x-1} e^{-t} d t
$$

let

$$
t=p u \Rightarrow d t=p d u
$$

then

$$
\Gamma(x)=\int_{0}^{\infty}(p u)^{x-1} e^{-p u} p d u
$$

$$
\begin{aligned}
& =p^{x} \int_{0}^{\infty} u^{x-1} e^{-p u} d u \\
& \Rightarrow \frac{\Gamma(x)}{p^{x}}=\int_{0}^{\infty} u^{x-1} e^{-p u} d u
\end{aligned}
$$

Let

$$
p=1+z
$$

and

$$
x=a+b
$$

then

$$
\begin{aligned}
& \frac{\Gamma(a+b)}{(1+z)^{a+b}}=\int_{0}^{\infty} u^{a+b-1} e^{-(1+z) u} d u \\
\Rightarrow & \frac{1}{(1+z)^{a+b}}=\frac{1}{\Gamma(a+b)} \int_{0}^{\infty} u^{a+b-1} e^{-(1+z) u} d u
\end{aligned}
$$

50

$$
\begin{aligned}
& B(a, b)=\int_{0}^{\infty} \frac{u^{a-1}}{(1+u)^{a+b}} d u \\
& =\int_{0}^{\infty} u^{a-1} \frac{1}{\Gamma(a+b)} \int_{0}^{\infty} \omega^{a+b-1} e^{-(1+u) \omega} d \omega d u
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{\Gamma(a+b)} \int_{0}^{\infty} \int_{\partial}^{\infty} u^{a-1} w^{a+b-1} e^{-(1+w) w} d w d u \\
& =\frac{1}{\Gamma(a+b)} \int_{0}^{\infty} w^{a+b-1} e^{-w} \int_{0}^{\infty} u^{a-1} e^{-w w} d u d w \\
& =\frac{1}{\Gamma(a+b)} \int_{0}^{\infty} w^{a+b-1} e^{-w} \frac{\Gamma(a)}{w^{a}} d w
\end{aligned}
$$

using

$$
\frac{\Gamma(a)}{\omega^{a}}=\int_{0}^{\infty} u^{a-1} e^{u \omega} d \omega
$$

50

$$
\begin{aligned}
B(a, b) & =\frac{\Gamma(a)}{\Gamma(a+b)} \int_{0}^{\infty} w^{b-1} e^{-w} d w \\
& =\frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)}
\end{aligned}
$$

* Forms of Beta Function

$$
B(a, b)=\int_{0}^{1} t^{a-1}(1-t)^{b-1} d t
$$

it was just shown tat

$$
B(a, b)=\int_{0}^{\infty} \frac{t^{a-1}}{(t+1)^{a+b}} d t
$$

For the third form let

$$
\begin{aligned}
& t=\sin ^{2} \theta \\
\Rightarrow \quad & d t=2 \cos \theta \sin \theta d \theta
\end{aligned}
$$

So

$$
\begin{aligned}
B(a, b) & =\int_{0}^{\pi / 2}\left(\sin ^{2} \theta\right)^{a-1}\left(1-\sin ^{2} \theta\right)^{b-1} 2 \cos \theta \sin \theta d \theta \\
= & 2 \int_{0}^{\pi / 2} \sin ^{2(a-1)} \theta \cos ^{2(b-1)} \theta \cos \theta \sin \theta d \theta \\
= & 2 \int_{0}^{\pi / 2} \sin ^{2 a-1} \theta \cos ^{2 b-1} \theta d \theta
\end{aligned}
$$

The Beta function can be interpreted as the extension of the Binomial coefficent to real numbers.

Recall that the Binomial Coefficent is given by

$$
\binom{n}{m}=\frac{n!}{(n-m)!m!}
$$

where $n, m \in\{0,1,2, \ldots\}$. let

$$
\begin{aligned}
& a=m+1 \Rightarrow m=a-1 \\
& b=n-m+1 \Rightarrow n-m=b-1 \\
& a-1+b-1=n=a+b-2
\end{aligned}
$$

so

$$
\begin{aligned}
\binom{n}{m} & =\frac{n!}{(n-m)!m!}=\frac{(a+b-2)!}{(b-1)!(a-1)!} \\
& =\frac{(a+b-1)!}{(a+b-1)(b-1)!(a-1)!}
\end{aligned}
$$

and

$$
\begin{aligned}
& \Gamma(a)=(a-1)! \\
& \Gamma(b)=(b-1)! \\
& \Gamma(a+b)=(a+b-1)!
\end{aligned}
$$

50

$$
\binom{n}{m}=\binom{a+b-2}{a-1}=\frac{\Gamma(a+b)}{(a+b-1) \Gamma(a) \Gamma(b)}
$$

using

$$
B(a, b)=\frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)}
$$

gives
$\binom{a+b-2}{a-1}=\frac{1}{(a+b-1) B(a, b)}$
finally using

$$
a=m+1 \quad b=n-m+1
$$

it is seen that
$\binom{a+b-2}{a-1}=\binom{n}{m}=\frac{1}{(n+1) B(m+1, n-m+1)}$

Thus $B(a, b)$ acan be rinterpreted in a manner similar to $\Gamma(a)$,
namely, as the extension of the Binomial coefficient to real numbers.

## * Identities

Consider

$$
B(a, b)=\int_{0}^{1} x^{a-1}(1-x)^{b-1} d x
$$

let

$$
u=1-x \Rightarrow x=1-u \Rightarrow d x=-d u
$$

then

$$
\begin{aligned}
& \int_{0}^{1} x^{a-1}(1-x)^{b-1} d x=-\int_{1}^{0}(1-u)^{a-1} u^{b-1} d u \\
& =\int_{0}^{1} u^{b-1}(1-u)^{a-1} d u=B(b, a)
\end{aligned}
$$

Thus

$$
B(a, b)=B(b, a)
$$

## Homogeneous Functions

A homogeneous function of degree $k g$ is defined by $f\left(\alpha x_{1}, \alpha x_{2}, \ldots, \alpha x_{n}\right)=\alpha^{k} f\left(x_{1}, x_{2}, \ldots, x_{n}\right)$
Consider

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j}
$$

Now

$$
\begin{aligned}
& f\left(\alpha x_{1}, \alpha x_{2}, \ldots, \alpha x_{n}\right)=\sum_{i=1}^{n} \sum_{j=1}^{n}\left(\alpha x_{i}\right)\left(\alpha x_{j}\right) \\
& =\alpha^{2} \sum_{i=1}^{n} \sum_{j=1}^{n} x_{i} x_{j}=\alpha^{2} f\left(x_{1}, x_{2}, \ldots, x_{n}\right)
\end{aligned}
$$

Thus $f$ is homogeneous of degree
Assume

$$
\begin{aligned}
& f\left(x_{1}, x_{2}\right)=\sum_{i=1}^{2} \sum_{j=1}^{n} x_{i} x_{j} \\
= & x_{1} x_{1}+x_{2} x_{1}+x_{1} x_{2}+x_{2} x_{2} \\
= & x_{1}^{2}+x_{2}^{2}+2 x_{1} x_{2}
\end{aligned}
$$

$$
\begin{aligned}
B(a, b+1) & =\frac{b}{a} B(a+1, b) \\
& =\frac{b}{a+b} B(a, b)
\end{aligned}
$$

So

$$
B(a+1, b)=\frac{a}{b} B(a, b+1)
$$

Also since

$$
B(a+1, b)=\frac{\Gamma(a+1) \Gamma(b)}{\Gamma(a+b+1)}
$$

and using

$$
\begin{aligned}
& \Gamma(a+1)=a \Gamma(a) \\
& \Gamma(a+b+1)=(a+b) \Gamma(a+b)
\end{aligned}
$$

gives

$$
\begin{aligned}
B(a+1, b) & =\frac{a}{a+b} \frac{\Gamma(a) \Gamma(b)}{\Gamma(a+b)} \\
& =\frac{a}{a+b} B(a, b)
\end{aligned}
$$

using the previous result

Next consider
$B(a+1, b)=\int_{0}^{1} x^{a}(1-x)^{b-1} d x$
using integration by parts

$$
S u d v=u v-S v d u
$$

with

$$
\begin{aligned}
& u=x^{a} \Rightarrow d u=a x^{a-1} d x \\
& d v=(1-x)^{b-1}=v=-\frac{(1-x)^{b}}{b} \\
& \delta o \text { 的 } x^{a}(1-x)^{b-1} d x=-\left.x^{a} \frac{(1-x)^{b}}{b}\right|_{0} ^{1} \\
& +\int_{0}^{1} a x^{a-1} \frac{(1-x)^{b}}{b} d x \\
& =\frac{a}{b} \int_{0}^{1} x^{a-1}(1-x)^{b} d x \\
& =\frac{a}{b} B(a, b+1)
\end{aligned}
$$

Now consider

$$
\begin{aligned}
& \sum_{i=1}^{2} x_{i} \frac{\partial f}{\partial x_{i}}=x_{1} \frac{\partial f}{\partial x_{i}}+x_{2} \frac{\partial f}{\partial x_{2}} \\
& =x_{1}\left(2 x_{1}+2 x_{2}\right)+x_{2}\left(2 x_{2}+2 x_{1}\right) \\
& =\partial\left(x_{1}^{2}+x_{1} x_{2}+x_{2}^{2}+x_{2} x_{1}\right) \\
& =2\left(x_{1}^{2}+x_{2}^{2}+2 x_{1} x_{2}\right)=2 f
\end{aligned}
$$

## Dirac Delta Function Identities

The Heaviside step function is defined by

$$
\begin{aligned}
& \theta(x)= \begin{cases}0 & x<0 \\
1 / 2 & x=0 \\
1 & x<0\end{cases} \\
& \theta(x-a)= \begin{cases}0 & x<a \\
1 / 2 & x=0 \\
1 & x>a\end{cases}
\end{aligned}
$$

and the Delta function is defined by

$$
\delta(x)= \begin{cases}0 & x \neq 0 \\ \infty & x=0\end{cases}
$$

such that the following integrals are finite

$$
\begin{aligned}
& \int_{-\infty}^{\infty} \delta(x) d x=1 \\
& \int_{-\infty}^{\infty} f(x) \delta(a-x) d x=f(a)
\end{aligned}
$$

The theaviside function can be defined in terms of the Delta function

$$
\theta(x-a)=\int_{-\infty}^{x} \delta(y-a) d y
$$

taking the derivative gives

$$
\frac{d \theta}{d x}(x-a)=\theta^{\prime}(x-a)=\delta(y-a)
$$

Consider the result obtaing by scalling the Heaviside function for $a^{3} 0$

$$
\theta(a x)= \begin{cases}0 & a x<0 \\ 1 / 2 & a x=0 \\ 1 & a x>0\end{cases}
$$

clearly

$$
\theta(a x)=\theta(x)
$$

and taking the derivative gives

$$
\begin{aligned}
& a^{\theta^{\prime}(a x)}=\theta^{\prime}(x) \\
= & \theta^{\prime}(a x)=\frac{\theta^{\prime}(x)}{a}
\end{aligned}
$$

but

$$
\theta^{\prime}(x)=\delta(x)
$$

80

$$
\delta(a x)=\frac{1}{a} \delta(x)
$$

Now if $a<0$

$$
\begin{aligned}
\theta(a x)= & \begin{cases}0 & a x<0 \\
1 / 2 & a x=0 \\
1 & a x>0\end{cases} \\
= & \left\{\begin{array}{ll}
0 & x>0 \\
1 / 2 & x=0 \\
1 & x<0
\end{array}= \begin{cases}1 & x<0 \\
1 / 2 & x=0 \\
0 & x>0\end{cases} \right. \\
= & 1- \begin{cases}0 & x<0 \\
1 / 2 & x=0 \\
1 & x>0\end{cases} \\
& 1-\theta(x)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
a \theta^{\prime}(a x) & =-\theta^{\prime}(x) \\
\theta^{\prime}(a x) & \Rightarrow-\frac{1}{a} \theta^{\prime}(x)
\end{aligned}
$$

since $a<0$ both cases are
satisfied by

$$
\delta(a x)=\frac{1}{|a|} \delta(x)
$$

Next consider the function

$$
g(x)=x^{2}-a^{2}=(x+a)(x-a)
$$

Then

$$
\theta(g(x))= \begin{cases}0 & g(x)<0 \\ 1 & g(x)>0\end{cases}
$$

Now from an inspection of the following plot
The left part of $\theta\left(x^{2}-a^{2}\right)$ is given by

$$
1-\theta(x+a)
$$

and the right part is given by

$$
\theta(x-a)
$$

![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-33.jpg?height=831&width=1010&top_left_y=58&top_left_x=147)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-33.jpg?height=390&width=928&top_left_y=955&top_left_x=229)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-33.jpg?height=392&width=1001&top_left_y=1410&top_left_x=229)
it follows that

$$
\begin{aligned}
\theta\left(x^{2}-a^{2}\right) & =1-\theta(x+a)+\theta(x-a) \\
& =1-[\theta(x+a)-\theta(x-a)]
\end{aligned}
$$

Now

$$
\begin{aligned}
\frac{d}{d x} \theta(g(x)) & =g^{\prime}(x) \frac{d \theta}{d x}(g(x)) \\
& =g^{\prime}(x) \delta(g(x))
\end{aligned}
$$

and

$$
\begin{aligned}
& \frac{d}{d x} \theta\left(x^{2}-a^{2}\right)=\frac{d}{d x}\{1-[\theta(x+a)-\theta(x-a)]\} \\
& =-\delta(x+a)+\delta(x-a)=\delta(x-a)-\delta(x+a)
\end{aligned}
$$

Bringins the results together

$$
\begin{aligned}
\delta\left(x^{2}-a^{2}\right) & =\frac{1}{g^{\prime}(x)}[\delta(x-a)-\delta(x+a)] \\
& =\frac{1}{g^{\prime}(a)} \delta(x-a)-\frac{1}{g^{\prime}(-a)} \delta(x+a)
\end{aligned}
$$

Now from an inspection of the plot

$$
\begin{array}{ll}
g^{\prime}(a)>0 & g^{\prime}(a)=2 a \\
g^{\prime}(-a)<0 & g^{\prime}(-a)=-2 a
\end{array}
$$

It follows that

$$
\begin{aligned}
\delta\left(x^{2}-a^{2}\right) & =\frac{1}{g^{\prime}(a)} \delta(x-a)-\frac{1}{g^{\prime}(-a)} \delta(x+a) \\
& =\frac{1}{g^{\prime}(a)} \delta(x-a)+\frac{1}{g^{\prime}(-a)} \delta(x+a) \\
& =\frac{1}{\left|g^{\prime}(a)\right|} \delta(x-a)+\frac{1}{\left|g^{\prime}(-a)\right|} \delta(x+a) \\
& =\frac{1}{2|a|}[\delta(x-a)+\delta(x+a)]
\end{aligned}
$$

Next consider a cubic equation

$$
g(x)=g_{0}\left(x-x_{1}\right)\left(x-x_{2}\right)\left(x-x_{3}\right)
$$

where

$$
x_{1}<x_{2}<x_{3}
$$

and

$$
\lim _{x \rightarrow-\infty} g(x)=-\infty \quad \lim _{x \rightarrow \infty} g(x)=\infty
$$

![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-36.jpg?height=543&width=1156&top_left_y=50&top_left_x=171)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-36.jpg?height=327&width=994&top_left_y=570&top_left_x=173)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-36.jpg?height=320&width=1010&top_left_y=918&top_left_x=173)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-36.jpg?height=323&width=1051&top_left_y=1251&top_left_x=171)

Inspection of the plots on the previous page gives

$$
\theta(g(x))=\theta\left(x-x_{1}\right)-\theta\left(x-x_{2}\right)+\theta\left(x-x_{3}\right)
$$

Next consider the case

$$
\lim _{x \rightarrow-\infty} f(x)=\infty \quad \lim _{x \rightarrow \infty} f(x)=-\infty
$$

where $f(x)=-g(x)$
Inspection of the plots on the next page gives

$$
\begin{aligned}
\theta(f(x)) & =1-\theta\left(x-x_{1}\right)+\theta\left(x-x_{2}\right)-\theta\left(x-x_{3}\right) \\
& =1-\left[\theta\left(x-x_{1}\right)-\theta\left(x-x_{2}\right)+\theta\left(x-x_{3}\right)\right]
\end{aligned}
$$

Now taking the derivative of the first case

$$
\frac{d \theta}{d x}(g(x))=\frac{d \theta}{d g} g^{\prime}(x)=g^{\prime}(x) \delta(g(x))
$$

and

$$
\frac{d \theta}{d x}(g(x))=\frac{d}{d x}\left[\theta\left(x-x_{1}\right)-\theta\left(x-x_{2}\right)+\theta\left(x-x_{3}\right)\right]
$$

![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-38.jpg?height=946&width=1321&top_left_y=68&top_left_x=56)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-38.jpg?height=382&width=1279&top_left_y=1031&top_left_x=114)
![](https://cdn.mathpix.com/cropped/2025_09_20_bcc5d4c73624e0ab4654g-38.jpg?height=390&width=1323&top_left_y=1422&top_left_x=114)

$$
=\delta\left(x-x_{1}\right)-\delta\left(x-x_{2}\right)+\delta\left(x-x_{3}\right)
$$

thus

$$
\begin{aligned}
g^{\prime}(x) \delta(g(x))= & \delta\left(x-x_{1}\right)-\delta\left(x-x_{2}\right)+\delta\left(x-x_{3}\right) \\
\Rightarrow \delta(g(x))= & \frac{1}{g^{\prime}(x)}\left[\delta\left(x-x_{1}\right)-\delta\left(x-x_{2}\right)+\delta\left(x-x_{2}\right)\right] \\
= & \frac{1}{g^{\prime}\left(x_{1}\right)} \delta\left(x-x_{1}\right)-\frac{1}{g^{\prime}\left(x_{2}\right)} \delta\left(x-x_{2}\right) \\
& +\frac{1}{g^{\prime}\left(x_{3}\right)} \delta\left(x-x_{3}\right)
\end{aligned}
$$

from an examination of the plot $\theta(g(x))$

$$
g^{\prime}\left(x_{1}\right)>0, \quad g^{\prime}\left(x_{2}\right)<0, \quad g^{\prime}\left(x_{3}\right)>0
$$

It follows that

$$
\begin{aligned}
\delta(g(x)) & =\frac{1}{\left|g^{\prime}\left(x_{1}\right)\right|} \delta\left(x-x_{1}\right)+\frac{1}{\left|g^{\prime}\left(x_{2}\right)\right|} \delta\left(x-x_{2}\right) \\
& +\frac{1}{\left|g^{\prime}\left(x_{3}\right)\right|} \delta\left(x-x_{3}\right)
\end{aligned}
$$

and the final result is obtained

$$
\delta(g(x))=\sum_{i=1}^{3} \frac{1}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)
$$

For $\theta(f(x))$

$$
\frac{d \theta}{d x}(f(x))=f^{\prime}(x) \frac{d \theta}{d f}=f^{\prime}(x) \delta(f(x))
$$

and

$$
\begin{aligned}
& \frac{d}{d x} \theta(f(x))=\frac{d}{d x}\left\{1-\left[\theta\left(x-x_{1}\right)-\theta\left(x-x_{2}\right)\right.\right. \\
& \left.\left.+\theta\left(x-x_{3}\right)\right]\right\} \\
& =-\delta\left(x-x_{1}\right)+\delta\left(x-x_{2}\right)-\delta\left(x-x_{3}\right)
\end{aligned}
$$

so

$$
\begin{aligned}
\delta(f(x))= & \frac{1}{f^{\prime}(x)}\left[-\delta\left(x-x_{1}\right)+\delta\left(x-x_{2}\right)\right. \\
= & \left.-\frac{1}{f^{\prime}\left(x_{1}\right)} \delta\left(x-x_{1}\right)\right] \frac{1}{f^{\prime}\left(x_{2}\right)} \delta\left(x-x_{2}\right) \\
& -\frac{1}{f^{\prime}\left(x_{1}\right)} \delta\left(x-x_{3}\right)
\end{aligned}
$$

From an inspection of the plot

$$
\begin{aligned}
f^{\prime}\left(x_{1}\right) & <0, f\left(x_{2}\right)>0, f\left(x_{3}\right)<0 \\
\delta(f(x)) & =\frac{1}{\left|f^{\prime}\left(x_{1}\right)\right|} \delta\left(x-x_{1}\right)>\frac{1}{\left|f^{\prime}\left(x_{2}\right)\right|} \delta\left(x-x_{2}\right) \\
& +\frac{1}{\left|f^{\prime}\left(x_{3}\right)\right|} \delta\left(x-x_{3}\right) \\
& =\sum_{i=1}^{3} \frac{1}{\left|f^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)
\end{aligned}
$$

Recall that

$$
\begin{aligned}
& g(x)=-f(x) \\
& \Rightarrow \quad\left|g^{\prime}(x)\right|=\left|f^{\prime}(x)\right|
\end{aligned}
$$

trus
$\delta(g(x))=\delta(f(x))=\sum_{i=1}^{3} \frac{1}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)$
In general, for an n'th order poly nomia' $g(x)$ the expression above becomes

$$
\delta(g(x))=\sum_{i=1}^{n} \frac{1}{\left|g^{\prime}\left(x_{i}\right)\right|} \delta\left(x-x_{i}\right)
$$

where

$$
g\left(x_{i}\right)=0 \quad \forall i=1, \ldots, n
$$

Next consider

$$
\delta^{\prime}\left(x-x_{0}\right)=\frac{d}{d x} \delta\left(x-x_{0}\right)
$$

and the integral

$$
\int \delta^{\prime}\left(x-x_{0}\right) f(x) d x
$$

using integration by parts

$$
\begin{gathered}
u=f(x) \Rightarrow d u=f^{\prime}(x) d x \\
d v=\delta^{\prime}\left(x-x_{0}\right) d x \Rightarrow v=\delta\left(x-x_{0}\right)
\end{gathered}
$$

$\int \delta^{\prime}\left(x-x_{0}\right) f(x) d x=\delta\left(x-x_{0}\right) f(x)$
$-\int \delta\left(x-x_{0}\right) f^{\prime}(x) d x$

## Binomial Coefficient

Given a set of $n$ objects the number of unique orderings is given by $n!$

How many ways can $k$ the objects los removed trom of the objects does not matter.

Consider the case where $n=4$.

$$
\begin{aligned}
& \begin{array}{r}
3-4 \\
2-4-3 \\
1-3-2-4 \\
1-4-2 \\
4-2-3 \\
3-2
\end{array} \\
& 1_{3-1}^{1-2}-4-3 \\
& \frac{3-2-1-3}{3-1} \\
& \frac{3-2}{2-1}
\end{aligned}
$$

$1-3-4$
$1-4-3$
$2-3-1-4$
$14-1$
$4-1-3$
$3-1$

$$
\begin{gathered}
1_{1}^{2}-4 \\
1 / 4-2 \\
3-2-1 / 4 \\
1 / 4-1 \\
4-1-2 \\
12-1
\end{gathered}
$$

The number of ways $k=2$
own be selected is
$1-3 \quad 2-3 \quad 3-2 \quad 4-2$
or

$$
4.3
$$

There are 2 selections which contain the same ebjects but in a different order so the desired result is

$$
\frac{4.3}{2}
$$

In seneral

$$
\begin{aligned}
& \frac{(n)(n-1)(n-2) \cdots(n-k+1)}{k!} \\
& =\frac{n!}{k!(n-k)!}=\binom{n}{k}
\end{aligned}
$$

using the more common

Now consider the binomial

$$
(a+b)^{n}
$$

for $n=1$

$$
a+b
$$

for $n=2$

$$
(a-b)^{2}=a^{2}+2 a b+b^{2}
$$

for $n=3$

$$
\begin{aligned}
& (a+b)^{3}=\left(a^{2}+2 a b+b^{2}\right)(a+b) \\
= & a^{3}+2 a^{2} b+a b^{2}+a^{2} b+2 a b^{2} \\
& +b^{3} \\
= & a^{3}+3 a^{2} b+3 a b^{2}+b^{3}
\end{aligned}
$$

for $n=4$

$$
\begin{aligned}
&(a+b x)^{4}=\left(a^{3}+3 a^{2} b+3 a b^{2}+b^{3}\right) \\
&(a+b) \\
&=a^{4}+3 a^{3} b+3 a^{2} b^{2}+a b^{3} \\
&+a^{3} b+3 a^{2} b^{2}+3 a b^{3}+b^{4}
\end{aligned}
$$

$$
=a^{4}+4 a^{3} b+6 a^{2} b^{2}+4 a b^{3}
$$

Now there are $n+1$ terms in the expansion so

$$
(a+b)^{n}=\sum_{k=0}^{n} c_{k}^{n} a^{n-k} b^{k}
$$

To delermine $C_{k}^{n}$ the number of terms in the expansion with specified powers of $a$ and $b$. There are $n$ expressions in the expansion

$$
(a+b)^{n}=(a+b)(a+b) \cdots(a+b)
$$

If powers of a are considered there is only one term containing $a^{n}$ since it will be the product The number of terms with $a^{n-1}$ will be formed by all of the ways a can be muttiplied by $b$ without consideration of order. This will be the number of ways $n-1$ exprension can be selecten from the
n expressions. Namely

$$
\binom{n}{n-1}
$$

for the k'th term

$$
\binom{n}{n-k}
$$

But

$$
\binom{n}{n-k}=\frac{n!}{(n-k)!k!}=\binom{n}{k}
$$

so

$$
C_{k}^{n}=\binom{n}{k}
$$

and

$$
(a+b)^{n}=\sum_{k=0}^{n}\binom{n}{k} a^{n-k} b^{k}
$$

## Series Representation of Exponelial

Consider

$$
\left(1+\frac{x}{n}\right)^{n}
$$

using

$$
(a+b)^{n}=\sum_{k=0}^{n}\binom{n}{k} a^{n-k} b^{k}
$$

gives

$$
\begin{aligned}
\left(1+\frac{x}{n}\right)^{n} & =\sum_{k=0}^{n}\binom{n}{k}(1)^{n-k}\left(\frac{x}{n}\right)^{k} \\
& =\sum_{k=0}^{n}\binom{n}{k} \frac{x^{k}}{n^{k}} \\
& =\sum_{k=0}^{n} \frac{(n)(n-1) \cdots(n-k+1)}{k!n^{k}} x^{k} \\
& =1+\frac{n}{1!n} x+\frac{(n)(n-1)}{2!n^{2}} x^{2} \\
& +\frac{(n)(n-1)(n-2)}{3!n^{3}} x^{3}+\cdots \\
& +\frac{n!}{n!n^{n}} x^{n}
\end{aligned}
$$

$$
\begin{aligned}
= & 1+x+\frac{n(n-1)}{2!n} x^{2}+\frac{n(n-1)(n-2)}{3!n^{3}} x^{3} \\
& +\cdots+\frac{n!}{n!} \frac{x^{n}}{n^{n}} \\
= & 1+x+\frac{x^{2}}{2!} \frac{(n-1)}{n}+\frac{x^{3}}{3!} \frac{(n-1)(n-2)}{n^{2}} \\
+\cdots & \frac{x^{n}}{n!} \frac{(n-1)(n-2) \cdots(1)}{n^{n-1}} \\
= & 1+x+\frac{x^{2}}{2!}\left(1-\frac{1}{n}\right)+\frac{x^{3}}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \\
& +\cdots+\frac{x^{n}}{n!}\left(1-\frac{1}{n}\right)\left(\frac{1}{n}\right) \cdots \frac{1}{n}
\end{aligned}
$$

Taking the limit

$$
\begin{aligned}
\lim _{n \rightarrow \infty} & \left(1-\frac{x}{n}\right)^{n}=\lim _{n \rightarrow \infty}\left[1+x+\frac{x^{2}}{2!}\left(1-\frac{1}{n}\right)\right. \\
& +\frac{x^{3}}{3!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right)+\cdots+ \\
& \left.\frac{x^{n}}{n!}\left(1-\frac{1}{n}\right)\left(1-\frac{2}{n}\right) \cdots \frac{1}{n}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots+ \\
& =\sum_{k=0}^{\infty} \frac{x^{k}}{k!}
\end{aligned}
$$

but $e^{x}$ the is Taylor series expansion

$$
e^{x}=\sum_{k=0}^{\infty} \frac{x^{k}}{k!}
$$

Thus

$$
e^{x}=\lim _{n \rightarrow \infty}\left(1+\frac{x}{n}\right)^{n}
$$

## Sterling's Approximation

The Gamma Function is defined by

$$
\begin{aligned}
\Gamma(n+1) & =\int_{0}^{\infty} x^{n} e^{-x} d x \\
& =\int_{0}^{\infty} e^{\ln \left(x^{n} e^{-x}\right)} d x \\
& =\int_{0}^{\infty} e^{\left(\ln x^{n}+\ln e^{-x}\right)} d x \\
& =\int_{0}^{\infty} e^{(n \ln x-x)} d x
\end{aligned}
$$

Now let

$$
x=n y \Rightarrow d x=n d y
$$

then

$$
\begin{aligned}
{[(n+1)} & =\int_{0}^{\infty} e^{[n \ln (n y)-n y]} n d y \\
= & n \int_{0}^{\infty} e^{[n(\ln n+\ln y)-n y]} d y
\end{aligned}
$$

$$
\begin{aligned}
& =n \int_{0}^{\infty} e^{n \ln n} e^{n(\ln y-y)} d y \\
& =n e^{n \ln n} \int_{0}^{\infty} e^{n(\ln y-y)} d y \\
& =n^{n+1} \int_{0}^{\infty} e^{n(\ln y-y)} d y
\end{aligned}
$$

Now if $n \gg 1$ the integral can be approximated using Laplace's Method.
Laplace's Method states that for $M \gg 1$ and if $f(x)$ is an arbitrary function that is at least twice differentiable with a global maximum then

$$
\int_{a}^{b} e^{\mu f(x)} d x \approx e^{\mu f\left(x_{0}\right)} \sqrt{\frac{2 \pi}{\mu\left|f^{\prime \prime}\left(x_{0}\right)\right|}}
$$

here

$$
f(x)=\ln x-x
$$

So

$$
f^{\prime}(x)=\frac{1}{x}-1
$$

and

$$
f^{\prime \prime}(x)=-\frac{1}{x^{2}}
$$

the maximum is given by

$$
\begin{aligned}
& f^{\prime}\left(x_{0}\right)=0=\frac{1}{x_{0}}-1 \\
& \Rightarrow x_{0}=1
\end{aligned}
$$

$X_{0}$ is a maximum since

$$
f^{\prime \prime}\left(x_{0}\right)=-1<0
$$

and

$$
f\left(x_{0}\right)=-1
$$

it follows that for $n \gg 1$

$$
\int_{0}^{\infty} e^{n(\ln y-y)} d y \approx e^{-n} \sqrt{\frac{2 \pi}{n}}
$$

50

$$
\begin{aligned}
\Gamma(n+1) & \approx n^{n+1} e^{-n} \sqrt{\frac{2 \pi}{n}} \\
& =n^{n+1} e^{-n} \sqrt{\frac{2 \pi n}{n^{2}}} \\
& =n^{n+1} \frac{e^{-n}}{n} \sqrt{2 \pi n} \\
& =n^{n} e^{-n} \sqrt{2 \pi n} \\
& =\sqrt{2 \pi n}\left(\frac{n}{e}\right)^{n}
\end{aligned}
$$

Thus

$$
\Gamma(n+1)=\sqrt{2 \pi n}\left(\frac{n}{e}\right)^{n}
$$

