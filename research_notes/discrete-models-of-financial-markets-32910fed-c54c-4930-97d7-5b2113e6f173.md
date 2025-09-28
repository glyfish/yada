## Discrete Models of Financial Markets

Troy Stribling May 2, 2021

## Single step Asset Pricing Models

In the simplest single stop model there are two time instants, $t=0$ and $t=T$, representing the present and future respectively. Typically time $T$ is denoted by $T=1$. The model assums two furture scenerios. One in which the asset prrce increases denoted by $u$ and another in which the stock price decreases dented by D

At time $t=0$ the current price of the asset is given by $s(0)>0$. This asset is referred to as the underlying. The future price of the asset denoted by $S(1)$ is unknown but assumed
to have two possible values which occur randomly with specified probabilities. The possible outcomes are specified as events in a sample space denoted by $\Omega$. Here $\Omega$ will always have a finite number of elements but in more sophisticated models there may be an infinite number of elements.

For the single stop madel the sample space is given by

$$
\Omega=\{u, d\}
$$

which specify the price of the asset going up and going down.
The asset price at $t=1$ is a function of the sample space.

$$
s(1): \Omega \rightarrow(0, \infty)
$$

In general any function

## defined on $\Omega$ is called a random variable.

The return is defined as the fractional change in the asset price between $t=0$ and $t=1$.

$$
K_{s}=\frac{s(1)-s(0)}{s(0)}
$$

it follows that

$$
s(1)=s(0)\left(1+k_{s}\right)
$$

The return will be specified for both events $u$ and $d$ by

$$
\begin{aligned}
& K_{s}(u)=u \\
& K_{s}(d)=D
\end{aligned}
$$

where

$$
-1<D<U
$$

It is seen that this constraint ensures that $S(1) \geqslant 0$

It follows that the two possible asset prrces at $t=1$ are given by

$$
\begin{aligned}
& s(1, u)=s(0)(1+u) \\
& s(1, d)=s(0)(1+D)
\end{aligned}
$$

To simplify notation let

$$
\begin{aligned}
s^{u} & =s(l, u) \\
s^{d} & =s(l, d)
\end{aligned}
$$

then

$$
s(1)=\left\{\begin{array}{l}
s^{u}=s(0)(1+u) \\
s^{d}=s(0)(1+D)
\end{array}\right.
$$

The probabilities are defined by specifing one number, $p$, on the interval $(0,1)$

$$
\begin{aligned}
& P(\{u\})=P \\
& P(\{d\})=1-P
\end{aligned}
$$

Additionally for a risk-free deterministic asset earning a fixed interest rate $R$, such as a money market account, The asset price at $t=0$ and $t=1$ are related by

$$
A(1)=A(0)(1+R)
$$

where $R>0$.
Consider a portfolio construded from $x$ units of a risky asset $S(t)$ and $y$ units of a risk free asset $A(t)$. The intial value of the portfolio is given by

$$
V_{(x, y)}(0)=x S(0)+y A(0)
$$

and the value of the portfolio at $t=1$ is given

$$
V_{(x, y)}(1)=x S(1)+y A(1)
$$

since there are two different
outcomes for s(1) it follows that

$$
v_{(x, y)}(1)=\left\{\begin{array}{l}
x s(0)(1+u)+y A(0)(1+R) \\
x s(0)(1+0)+y A(0)(1+R)
\end{array}\right.
$$

The following assumptions are made in the model.

1. The market is frictionless. Implying that there are no restrictions on the values of $x$ and $y$. This implies there is no limit to short selling. At $t=0$ an asset can be borrowed and sold. The money obtained can be used to purchase some other asset At $t=1$ the shorted asset can be purchased and returned to the owner.
2. The assets are asswmed to be arbitrarly divisible meaning $x$ and $y$ are any real

## number

3. No bownds are placed on $x$ and $y$ assuming unlimited liquidity. That is $x$ and $y$ can always be purchased and sold.
4. Transaction costs are assumed to be zero. This implies that assets have the same costs apply to long $(x>0)$ and short $(x<0)$
5. Risk-free investment ( $y>0$ ) and borrowing ( $y<0$ ) both use the same interest rate $R$.
6. The No Arbitrage Phinciple (NAP) which asserts that trading cannot yield a risk free profit.

## Definition

A portfolio $(x, y)$ chosen at time $t=0$ is an arbitrage opportunity
if

$$
U_{(x, y)}(0)=0 \quad U_{(x, y)}(1) \geqslant 0
$$

and with positive probability

$$
V_{(x, y)}(1)>0
$$

This is saying that with no initial investment, risk, a profit is made.

## Theorem

The No Arbitrage Principle implies that

$$
D<R<U
$$

where $D$ and $U$ are the down and up returns given by

$$
D=\frac{S(0)-S(1, d)}{S(1, d)}
$$

$$
u=\frac{S(0)-S(1, u)}{S(1, u)}
$$

and $R$ is the risk-free

## Proof

Recall that

$$
s(1)=\left\{\begin{array}{l}
s^{u}=s \cos (1+u) \\
s d=s(0)(1+D)
\end{array}\right.
$$

Now assume that $D \geqslant R$ so that $R \leqslant D<U$.
If this is true and $u \geqslant R$ then

$$
s(0)(1+R) \leqslant s^{d} \leqslant s^{u}
$$

Recall that the value of a portfolio at $t$ is given by

$$
U_{(x, y)}(t)=x S(t)+y A(t)
$$

assume that $x=1$ and

$$
y=-\frac{S(0)}{A(0)}
$$

with this assumption it follows that

$$
\begin{aligned}
U_{(x, y)}(0) & =S(0)-\frac{S(0)}{A(0)} A(0) \\
& =0
\end{aligned}
$$

This assumption is equivalent to borrowing and amount

$$
5(0)
$$

at the risk free interest rate and purchasing one share of an asset at price s(0).
It follows that the intral investment is zero.

Now at $t=1$ using $A(1)=A(0)(1+R)$ gives a portfolio salue of

$$
\begin{aligned}
U_{(x, y)}(1) & =S(1)-\frac{S(0)}{A(0)} A(0)(1+R) \\
& =S(1)-S(0)(1+R)
\end{aligned}
$$

Recall that $S(1)$ has two outcomes

$$
s(1)=\left\{\begin{array}{l}
s(0)(1+U) \\
s(0)(1+D)
\end{array}\right.
$$

It follows that
$v_{(x, y)}(1)=\left\{\begin{array}{l}s(0)(1+u)-s(0)(1+R) \\ s(0)(1+D)-s(0)(1+R)\end{array}\right.$

$$
\begin{aligned}
& =\left\{\begin{array}{l}
s(0)(1+u-1-R) \\
s(0)(1+D-1-R)
\end{array}\right. \\
& =\left\{\begin{array}{l}
s(0)(u-R)>0 \\
s(0)(D-R) \geqslant 0
\end{array}\right.
\end{aligned}
$$

but $R \leqslant D<u$ thus

$$
U_{(x, y)}(1) \geqslant 0
$$

with probability 1 since both outcomes are greater tran or equal to 0 .

It follows that $R \leqslant D$ leads to an arbitrage thus $R>0$.
Next assume that $R \geqslant U$ so that $0<u \leqslant R$ and that the portfolio takes the opposite position

$$
x=-1 \quad y=\frac{S(0)}{A(0)}
$$

so that

$$
\begin{aligned}
U_{(x, y)}(0) & =x S(0)+y A(0) \\
& =S(0)-\frac{S(0) A(0)}{A(0)} \\
& =0
\end{aligned}
$$

This position corresponds to short selling tre asset at $t=0$ for $S(0)$ and depositing the cash in a risk-free account until $t=1$. Now

$$
\begin{aligned}
U_{(x, y)}(1) & =x S(1)+y A(1) \\
& =-S(1)+\frac{S(0)}{A(0)} A(0)(1+R)
\end{aligned}
$$

$$
=-S(1)+S(0)(1+R)
$$

it follows that for both out comes

$$
\begin{aligned}
U_{(x, y)}(1) & =\left\{\begin{array}{l}
-s(0)(1+u)+s(0)(1+R) \\
-s(0)(1+D)+s(0)(1+R)
\end{array}\right. \\
& =\left\{\begin{array}{l}
s(0)(-1-u+1+R) \\
s(0)(-1-D+1+R)
\end{array}\right. \\
& =\left\{\begin{array}{l}
s(0)(R-u) \geqslant 0 \\
s(0)(R-D)>0
\end{array}\right.
\end{aligned}
$$

But it is assumed that $0<U \leqslant R$ thus both outcomes are greater than or equal to zero. It follows trat with probability 1 that

$$
V_{(x, y)}(1) \geqslant 0
$$

so an arbitrage is possible. It follows that

$$
D<R<U
$$

to prevent arbitrage.

## Theorem

The condition $D<R<U$ implies no arbitrage.

## Proof

Assume the $(x, y)$ portfolio has zero intial value, then

$$
\begin{aligned}
U_{(x, y)}(0) & =0=x S(0)+y A(0) \\
\Rightarrow y & =-\frac{x S(0)}{A(0)}
\end{aligned}
$$

This represents a portfolio finacer by borrowing or short selling borrowed shares.

Now at $t=1$

$$
\begin{aligned}
& U_{(x, y)}(1)=x S(1)-x \frac{S(0)}{A(0)} A(1) \\
= & x\left(S(1)-\frac{S(0)}{A(0)} A(1)\right)
\end{aligned}
$$

$$
\begin{aligned}
& =x\left(S(1)-\frac{S(0)}{A(0)} A(0)(1+R)\right) \\
& =x[S(1)-S(0)(1+R)]
\end{aligned}
$$

Recall that the two outcomes of $5(1)$ are given by

$$
s(1)=\left\{\begin{array}{l}
s^{u}=s(0)(1+u) \\
s^{d}=s(0)(1+D)
\end{array}\right.
$$

so
$U_{(x y)}(1)=\left\{\begin{array}{l}x[s(0)(1+u)-s(0)(1+R)] \\ x[s(0)(1+D)-s(0)(1+R)]\end{array}\right.$

$$
\begin{aligned}
& =\left\{\begin{array}{l}
x s(0)(1+u-1-R) \\
x s(0)(1+D-1-R)
\end{array}\right. \\
& =\left\{\begin{array}{l}
x s(0)(u-R) \\
x s(0)(D-R)
\end{array}\right.
\end{aligned}
$$

Now if $x>0$, which corresponds to financing the portfolio by borrowing an amount of $x S(0)$ at interect rate $R$ and purchasing $x$ units of an asset at price $S(D)$, and the inequality $D<R<U$ is satisfled

Then

$$
U_{(x, y)}(1)=\left\{\begin{array}{l}
x \operatorname{scos}(u-R)>0 \\
x s(0)(D-R)<0
\end{array}\right.
$$

similarly if $x<0$, which corresponds to financing the portfolio by short selling $x$ units of the asset and depositing the money in a money market account carming $R$ in interest, and $D<R<U$ it follows that
$U_{(x, y)}(1)=\left\{\begin{array}{l}x \operatorname{scos}(u-R)<0 \\ x s(0)(D-R)>0\end{array}\right.$
It follows that there is no arbatrage opportunity. Thus

$$
D<R<U
$$

ensures no arbatrage.
Note that in the $x<0$ case the investor loses money on the up price of the asset, since it was sold shorl and makes money on the down price.

## Definition: Discounting

Suppose an asset $x$ has value $x(1)$ at $t=1$. Its discounted value to time $t=0$ is given by

$$
\tilde{x}(1)=x(1)(1+R)^{-1}
$$

For a stock the discounted value is

$$
\tilde{s}(1)=s(1)(1+R)^{-1}
$$

The discounted value is the amount that would need the be invested at interest rate $R$ at $t=0$ to dotain the value at $t=1$, namely,

$$
\begin{aligned}
& \tilde{x}(1)(1+R)=x(1) \\
& \tilde{s}(1)(1+R)=S(1)
\end{aligned}
$$

Define the discounted stock price process by

$$
\tilde{S}=\{\tilde{S}(0), \tilde{S}(1)\}
$$

where

$$
\tilde{S}(0)=S(0)
$$

and clearly

$$
\tilde{A}(1)=A(0)
$$

since

$$
A(1)=A(0)(1+R)
$$

$$
\begin{aligned}
\Rightarrow A(0) & =A(1)(1+R)^{-1} \\
& =\tilde{A}(1)
\end{aligned}
$$

It follows that the discownted portfolio value is given by

$$
\begin{aligned}
\tilde{V}_{(x, y)}(0) & =x \tilde{S}(0)+y \tilde{A}(0) \\
& =x S(0)+y A(0) \\
\tilde{V}_{(x, y)}(1) & =x \tilde{S}(1)+y \tilde{A}(1) \\
& =x \tilde{S}(1)+y A(0)
\end{aligned}
$$

The change in portfolio value is given by

$$
\begin{aligned}
\tilde{V}_{(x, y)}(1) & -\tilde{V}_{(x, 1)}(0)=x \tilde{S}(1)+\bar{Y} A(0) \\
& -x S(0)-y \tilde{A}(0) \\
= & x \tilde{S}(1)-x S(0)
\end{aligned}
$$

which depends only on the
discounted value of the asset

## Option Pricing

Consider a long European Call option. The hoder of the option makes a profit if the price of the underlying asset at $t=1$ is above a pridetermined price $k$. Define the payoff of the long call position

$$
\begin{aligned}
c(1) & =\left\{\begin{array}{cc}
s(1)-k & \text { if } s(1)>k \\
0 & \text { otherwise }
\end{array}\right. \\
& =\max (s(1)-k) \\
& =(s(1)-k)^{+}
\end{aligned}
$$

The payoff of a long European put option is given by

$$
P(1)=(k \cdot S(1))^{+}
$$

Note that the payoff of the lons call and put options
is nonnegative using the No Arbitrage Phinciple it follows the the price of the options is greater than zero since if it were zero a risk-free profit can be made.

The price or premimum of European call or put option is denoted by $C(0)$ or $P(0)$ repectively.
In the following a method of determing the rational price within the single step asset price model will be discussed

For now assume that the strike price satisfies

$$
S(0)(1+D) \leqslant K \leqslant S(0)(1+U)
$$

Next a portfolio of assets is constructed that has
a value equal to the payoff of the ostion. For a call option

$$
U_{(x, y)}(1)=c(1)
$$

this portfolio is called the replicating port Eolio.
Recall that the value of a port folio at $t=1$ is given by
$U_{(x, y)}(1)=\left\{\begin{array}{l}x S(0)(1+u)+y A(0)(1+R) \\ x S(0)(1+0)+y A(0)(1+R)\end{array}\right.$
where the up outcome occurs with probability $P$ and the down outcome occurs with probability 1-p. Also,

$$
C(1)=\left\{\begin{array}{cc}
s(1)-k & \text { if } s(1)>k \\
0 & \text { otherwise }
\end{array}\right.
$$

using the assumption that

$$
s(0)(1+D) \leqslant K \leqslant s(0)(1+u)
$$

thus there is only payoff for the up outcome.
It follows that

$$
U_{(x, y)}(1)=C(1)
$$

yields the pair of equations
$x S(0)(1+u)+y A(0)(1+R)=S(0)(1+u)-K$
$x S(0)(1+0)+y A(0)(1+R)=0$
These can be solved for $x$ and y. From the secord equation

$$
x=-y \frac{A(0)(1+R)}{s(0)(1+D)}
$$

substituting into the first equation gives

$$
\begin{aligned}
& -y \frac{A(0)(1+R)}{s(0)(1+D)}(1+u)+y A(0)(1+R) \\
& =s(0)(1+u)-K \\
& =y\left[A(0)(1+R)-\frac{A(0)(1+R)(1+u)}{1+D}\right] \\
& =s(0)(1+u)-K \\
& =y A(0)(1+R)\left[1-\frac{(1+u)}{(1+D)}\right]=s(0)(1+u)-K \\
& \Rightarrow y A(0) \frac{(1+R)}{(1+D)}(1+D-1-u)=s(0)(1+u)-K \\
& \Rightarrow y A(0) \frac{1+R)}{(1+D)}(D-u)=s(0)(1+u)-K \\
& \Rightarrow y=\frac{[s(0)(1+u)-K](1+D)}{A(0)(1+R)(D-u)} \\
& =\frac{-[s(0)(1+u)-K](1+D)}{A(0)(1+R)(u-D)}
\end{aligned}
$$

substituting into the first equation gives

$$
\begin{aligned}
x & =-y \frac{A(0)(1+R)}{s(0)(1+D)} \\
& =\frac{[s(0)(1+U)-K](1+D)}{A(0)(1+R)(U-D)} \frac{A(0)(T+R)}{s(0)(1+D)} \\
& =\frac{[s(0)(1+U)-K]}{s(0)(U-D)}
\end{aligned}
$$

Thus the replicating portfolio is given by

$$
\begin{gathered}
x_{c}=\frac{[s(0)(1+U)-K]}{s(0)(U-D)} \\
y_{c}=-\frac{[s(0)(1+U)-K](1+D)}{A(0)(1+R)(U-D)}
\end{gathered}
$$

where

$$
U_{(x, y)}^{c}(1)=x_{c} S(1)+y_{c} A(1)
$$

Now the claim is that the price of the call option, i.e. the option primium, is the intral value of the replicating portfolio, $v_{(x, y)}^{c}(0)$. This claim is based in the intuition that two portfolios dentical at $t=1$ are identical at $t=0$. This claim is justified using the No Arbatrage Principle.
To prove this the definition of a portfolio is extended to include a call option position. A portfolio is represented by the tripple $(x, y, z)$, where $x$ is the number of stock units, y the risk-free position and $z$ the number of wits of the call option. Similar to the convention that $x<0$ represents a short position and $x>0$ a long position in the asset $s(t)$, the convention of
$2<0$ representing a short call position and $2>0 a$ long call is also assumed for $C(t)$ also y $<0$ represts borrowing a risk-free asset at interest rate $R$ and $y>0$ represents recieving interest payments of $R$
The portfolio value is given by
$U_{(x, y, z)}(0)=x S(0)+y A(0)+z C(0)$
$u_{(x, y, z)}(1)=x s(1)+y A(1)+z(1)$

## Definition

The portfolio $(x, y, z)$ is an arbitrage opportunity if

$$
U_{(x, y, z)}(0)=0
$$

and $U_{(x, y, z)}(1) \geqslant 0$ with probability one and $U_{(x, y, z)}(1)>0$ with non-zero probability.

## Defintion No Arbitrage Principle

Aribitrage opportunities do not exist in the extended market.

## Theorem

The vo Arbitrage Principle implies that the price of the European call with strike price $K$ is the value at time $t=0$ of the replicating portfolio.

$$
c(0)=U_{(x, y)}(0)=x_{c} s(0)+y_{c} A(0)
$$

where

$$
\begin{gathered}
x_{c}=\frac{[s(0)(1+u)-k]}{s(0)(u-D)} \\
y_{c}=-\frac{[s(0)(1+u)-k](1+D)}{A(0)(1+R)(u-D)} \\
c(1)=U_{(x, y)}(1)=x_{c} s(1)+y_{c} A(1)
\end{gathered}
$$

## Proof

Assume $C(0)>X_{c} S(0)+Y_{c} A(0)$. If this is the case then the option is selling for more than the replicating portfolio. If this is the case an investor at $t=0$ can sell a call option and use the proceeds to purchase the portfolio $\left(x_{c}, y_{c}\right)$. upon completing the transaction the investor holds a positive balance of

$$
C(0)-x_{c} S(0)-y_{c} A(0)>0
$$

This money is invested at the risk-free interest rate $R$ in addition to $Y_{c} A(0)$. This gives

$$
\begin{aligned}
Y_{c} A(0)= & C(0)-X_{c} S(0)-Y_{c} A(0) \\
& +Y_{c} A(0) \\
= & C(0)-X_{c} S(0)
\end{aligned}
$$

$$
\Rightarrow \quad y_{c}=\frac{c(0)-x_{c} s(0)}{A(0)}
$$

This produces the portfolio

$$
\left(x_{c}, \frac{C(0)-x_{c} S(0)}{A(0)},-1\right)
$$

Here the investment in the underlying risky asset is given by $x_{c}$, the risk-free investment

$$
\frac{c(0)-x_{c} s(0)}{A(0)}
$$

and 1 call option has been sold at ccos.

It follows that

$$
\begin{aligned}
U_{(x, y, z)}(0)= & x_{c} s(0)+[c(0)-x s(0)] \\
& -c(0) \\
= & 0
\end{aligned}
$$

Thus there is a zero intial investment

At $t=1$ the portfolio value is given by

$$
\begin{aligned}
U_{(x, y, z)}^{(1)=} & x S(1)+y A(1)+z(1) \\
= & x_{c} S(1)+\frac{C(0)-x_{c} S(0) A(1)}{A(0)} \\
& -C(1) \\
= & x_{c} S(1)+\left[C(0)-x_{c} S(0)\right](1+R) \\
& -C(1)
\end{aligned}
$$

From the replication portfolio

$$
\begin{gathered}
c(1)=x_{c} s(1)+y_{c} A(0)(1+R) \\
\Rightarrow c(1)-x_{c} s(1)=y_{c} A(0)(1+R) \\
s o \\
U_{(x, y, 2)}(1)=x_{c} s(1)-c(1) \\
+\left[c(0)-x_{c} s(0)\right](1+R) \\
=-y_{c} A(0)(1+R) \\
+\left[c(0)-x_{c} s(0)\right](1+R)
\end{gathered}
$$

$$
=\left[C(0)-X_{c} S(0)-Y_{c} A(0)\right](1+R)
$$

But it was intrally assumed that

$$
C(0)-X_{c} S(0)-y_{c} A(0)>0
$$

Thus

$$
U_{(x, y, z)}(1)>0
$$

It follows that $C(0)>x_{c} S(0)+y_{c} A(0)$ implies a risk free profit and violates the No Arbitrage assumption. Next assume that,

$$
C(0)<x_{c} S(0)+y_{c} A(0)
$$

For this case short sell the csset to obtain $\chi_{c} s(0)$ and borrow $Y_{C} A(O)$ at interst rate $R$. Thus an amount of money

$$
x_{c} S(0)+y_{c} A(0)
$$

is obtained and used to
purchase $c(0)$. It follows that the invester has a ballance of

$$
X_{c} S(0)+Y_{c} A(0)-c(0)>0
$$

This amount is invested at the risk-free interest rate $R$ in additio to the amount borrowed. It follows that the total amount in the risk-free interest rate is given by

$$
\begin{aligned}
y_{c} A(0)= & x_{c} S(0)+y_{c} A(0)-c(0) \\
& -y_{c} A(0) \\
= & x_{c} S(0)-c(0) \\
\Rightarrow \quad y_{c}= & \frac{x_{c} S(0)-c(0)}{A(0)}
\end{aligned}
$$

it follows that the portfolio is given by

$$
\left(-x_{c}, \frac{x_{c} s(0)-c(0)}{A(0)}, 1\right)
$$

bow since $S(0)$ is a short sell, and $C(O)$ is purchased it follows that

$$
x=-x_{c} \text { and } z=1
$$

Thus
$U_{(x, y, z)}(0)=-x_{c} S(0)+x_{c} S(0)-c(0) +C(0) =0$
Thus there is zero intral investment.

Now at $t=1$

$$
\begin{aligned}
U_{(x, y, z)}(1)= & -x_{s} s(1)+\left[x_{c} s(0)-c(0)\right] A(0) \\
& +c(1)
\end{aligned}
$$

$$
\begin{aligned}
& =-x_{s} s(1)+\left[x_{c} s(0)-c(0)\right](1+R) \\
& \quad+c(1)
\end{aligned}
$$

Now from the replication portfolio

$$
\begin{aligned}
& c(1)=x_{c} s(1)+y_{c} A(1) \\
\Rightarrow & c(1)-x_{s} s(1)=y_{c} A(0)(1+R)
\end{aligned}
$$

It follows that

$$
\begin{aligned}
U_{(x, y, z)}^{(1)}= & C(1)-x_{s} s(1) \\
& +\left[x_{c} s(0)-c(0)\right](1+R) \\
= & y_{c} A(0)(1+R)+ \\
& {\left[x_{c} s(0)-c(0)\right](1+R) } \\
= & {\left[x_{c} s(0)+y_{c} A(0)-c(0)\right](1+R) }
\end{aligned}
$$

but it was assumed that

$$
x_{c} S(0)-y_{c} A(0)>C(0)
$$

## Thus

$$
U_{(x, y, z)}(1)>0
$$

It follows that

$$
x_{c} S(0)+y_{c} A(0)>C(0)
$$

Leads to arbtrage opportuntes.
It follows that

$$
C(0)=X_{c} S(0)+y_{c} A(0)
$$

leaves no money available for indestment at the risk free intest rate and thus does not lead to an arbitrage.

## Option Pricing Examples

Show that the price of an option increases if $u$ increases and increases if $D$ decreases.
In the previous section it was shown that the price of a call option for an underlying asset $s(t)$ is given by

$$
C(0)=X_{c} S(0)+Y_{c} A(0)
$$

where

$$
\begin{gathered}
x_{c}=\frac{[S(O)(1+u)-K]}{S(O)(u-D)} \\
y_{c}=-\frac{[S(O)(1+u)-K](1+D)}{A(O)(1+R)(u-D)}
\end{gathered}
$$

and
$D<R<U$

$$
S(0)(1+D) \leqslant K<S(0)(1+U)
$$

To show that $C(0)$ increases as $u$ increases it is enough to shaw that the first derivature of $C(0)$ as a flonation of $u$ is postive for all oalues of $u$ implying that is a monotonically increasing function of $u$
$\frac{\partial x_{c}}{\partial u}=\frac{\partial}{\partial u}\left\{\frac{[s(0)(1+u)-k]}{s(0)(u-D)}\right\}$

$$
\begin{aligned}
& =\frac{\partial}{\partial u}\left\{\frac{s(0)(1+u)}{s(0)(u-D)}-\frac{k}{s(0)(u-D)}\right\} \\
& \left.=\frac{\partial}{\partial u} \frac{(1+u)}{(u-D)}-\frac{k}{s(0)} \frac{\partial}{\partial u} \frac{1}{u-D}\right\} \\
& =-\frac{(1+u)}{(u-D)^{2}}+\frac{1}{u-D}+\frac{k}{s(0)} \frac{1}{u-D)^{2}} \\
& =\frac{1}{(u-D)^{2}}\left\{-\left(1+u^{2}\right)+(u-D)+\frac{k}{s(0)}\right\}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{(G-D)^{2}}\left\{-1-D+\frac{K}{s(0)}\right\} \\
& =\frac{1}{s(0)(u-D)^{2}}[K-s(0)(1+D)]
\end{aligned}
$$

Now $\delta(0)>0$ and $(U-D)^{2}>0$ and it is assumed that

$$
k>\operatorname{scos}(1+0)
$$

thus

$$
\frac{\partial x_{c}}{\partial u}>0
$$

and

$$
\begin{aligned}
\frac{\partial y_{k}}{\partial u}= & \frac{\partial}{\partial u}\left\{\frac{[s(0)(1+u)-K](1+D)}{A(0)(1+R)(u-D)}\right\} \\
= & \frac{-(1+D)}{A(0)(1+R)} \frac{\partial}{\partial u}\left\{\frac{s(0)(1+u)}{u-D}\right. \\
& \left.-\frac{K}{u-D}\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{-s(0)(1+D)}{A(0)(1+R)} \frac{2}{\partial u}\left\{\frac{(1+u)}{u-D}-\frac{k}{s(0)} \frac{1}{u-D}\right\} \\
= & \frac{-s(0)(1+D)}{A(0)(1+R)}\left\{\frac{-(1+u)}{(u-D)^{2}}+\frac{1}{(u-D)}\right. \\
& \left.+\frac{k}{s(0)(u-D)^{2}}\right\} \\
= & \frac{-s(0)(1+D)}{A(0)(u-D)^{2}}\{-(1+k)+(u-D) \\
& \left.+\frac{k}{s(0)}\right\} \\
= & -\frac{(1+D)}{A(0)(u-D)^{2}}[-s(0)(1+D)+k] \\
= & \frac{(1+D)}{A(0)(u-D)^{2}}[s(0)(1+D)-k]
\end{aligned}
$$

but $k>s(0)(1+D)$ thus

$$
\frac{\partial y_{c}}{\partial u}>\partial
$$

It follows that

$$
\frac{\partial c(0)}{d u}=s(0) \frac{\partial x_{c}}{\partial u}+A(0) \frac{\partial y_{c}}{\partial u}>0
$$

thus c(0) increases as u increased $C(0)$ is a montonically increasing function of $u$.

To show that $C(0)$ increases with decreasing it is sufficient to show that $C(O)$ is montonically decreasing function of $u$.
Recall

$$
c(0)=x_{c} s(0)+y_{c} A(0)
$$

where

$$
\begin{gathered}
x_{c}=\frac{[s(0)(1+U)-K]}{s(0)(U-D)} \\
y_{c}=-\frac{[s(0)(1+U)-K](1+D)}{A(0)(1+R)(U-D)}
\end{gathered}
$$

and

$$
\begin{aligned}
D & <R<U \\
s(0)(1+D) & \leqslant K<s(0)(1+U)
\end{aligned}
$$

Now

$$
\frac{\partial}{\partial D} C(D)=S(0) \frac{\partial x_{c}}{\partial D}+A(0) \frac{\partial y_{c}}{\partial D}
$$

SO

$$
\frac{\partial x_{c}}{\partial D}=\frac{\partial}{\partial D} \frac{[s(0)(1+u)-k]}{s(0)(u-D)}
$$

$$
=\frac{s(0)(1+u)-k}{s(0)(u-0)^{2}}
$$

$$
\begin{aligned}
\frac{\partial y_{c}}{\partial D} & =-\frac{\partial}{\partial D}\left\{\frac{[S(O)(1+u)-K](1+D)}{A(O)(1+R)(u-D)}\right\} \\
& =-\frac{[S(O)(1+u)-K]}{A(O)(1+R)} \frac{\partial}{\partial D}\left\{\frac{1+D}{(u-D)}\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & -\frac{[s(0)(1+u)-k]}{A(0)(1+R)}\left\{\frac{1}{u-D}+\frac{1+D}{(u-D)^{2}}\right\} \\
= & -\frac{[s(0)(1+u)-k]}{A(0)(1+R)}\left\{\frac{u-D+1+D}{(u-D)^{2}}\right\} \\
= & -\frac{[s(0)(1+u)-k]}{A(0)(1+R)} \frac{(1+u)}{(u-D)^{2}} \\
s o & \frac{\partial}{\partial D} c(0)= \\
& s(0) \frac{\partial x c}{\partial D}+A(0) \frac{\partial y c}{\partial D} \\
= & s(0) \frac{[s(0)(1+u)-k]}{s(0)(u-D)^{2}} \\
& -\frac{A(0) \frac{[s(0)(1+u)-k]}{A(0)(1+R)}(1+u)}{(u-D)^{2}} \\
= & \frac{[s(0)(1+u)-k]}{(u-D)^{2}}-\frac{[s(0)(1+u)-k](1+u)}{(1+R)(u-D)^{2}}
\end{aligned}
$$

$=\frac{[S \cos (1+U)-K]}{(U-D)^{2}}\left\{1-\frac{1+U}{1+R}\right\}$
$=\frac{[s \cos (1+u)-K]}{(u-D)^{2}} \frac{(\hat{x}+R-T-u)}{1+R}$
$=-\frac{[S(x)(1+U)-K]}{(U-D)^{2}}(U-R)$
Now it is assumed that
$R<u, \quad K<s(0)(1+u)$
It follows that
$\frac{\partial C(0)}{\partial D}<0$
for all $D$ thus $C(0)$ is a monotonically decreasing function of $D$.

Show that the option proce does not necessarily increase if the
spread increases.
This will be shown by providing an example. Consider the parameter choces,

$$
R=0, \quad S(0)=1, \quad K=1, \quad A(0)=1
$$

Now

$$
\begin{aligned}
c(0) & =x_{c} s(0)+y_{c} A(0) \\
& =x_{c}+y_{c}
\end{aligned}
$$

where

$$
\begin{aligned}
x_{c} & =\frac{[s(0)(1+u)-k]}{s(0)(u-D)} \\
& =\frac{(1+u)-1}{u-D} \\
& =\frac{u}{u-D} \\
y_{c} & =-\frac{[s(0)(1+u)-K](1+D)}{A(0)(1+R)(u-D)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{-[(1+u)-1](1+D)}{(u-D)} \\
& =\frac{-u(1+D)}{u-D}
\end{aligned}
$$

Thus

$$
\begin{aligned}
C(D) & =\frac{u}{u-D}-\frac{u(1+D)}{u-D} \\
& =\frac{u-u-u D}{u-D} \\
& =\frac{-u D}{u-D}
\end{aligned}
$$

For this case if $u$ is fixd $c(0)$ decreases as the spread moreases. But consider the cased

$$
U=0.05 \quad D=-0.05
$$

and

$$
u=0.01 \quad D=-0.19
$$

For first case

$$
\begin{aligned}
C(0) & =-\frac{(0.05)(-0.05)}{0.05+0.05} \\
& =0.025
\end{aligned}
$$

and the second

$$
\begin{aligned}
c(0)= & -\frac{(0.01)(-0.19)}{0.01+0.15} \\
& =\frac{(0.01)(0.19)}{0.2} \\
& =0.0095
\end{aligned}
$$

Thus the price increases with increasing spread and does not increase

## General Derivatioe securities

A derivative security, also called a contigent clain, is a security whose payoff depends on the prices of some underlying asset, referred to as the underlying; which can be a stock, an index, an exchange rate, an interest rate or any other quanity that can be traded or observed in the market.
Here a derioative security is represented by a random payoff of the form

$$
H(1)=h(s(1))
$$

for a payoff function $h:(0, \infty) \rightarrow \mathbb{R}$ where s(i) is the asset price at $t=1$.

The payoff function for a call option is given by

$$
\begin{aligned}
h(x) & =\max (x-k, 0) \\
& =(x-k, 0)^{+}
\end{aligned}
$$

Recall that

$$
\begin{aligned}
& s^{u}=s \cos (1+u) \\
& s^{0}=s \cos (1+D)
\end{aligned}
$$

where

$$
D<R<U
$$

define the payoff of $s^{u}$ and so by $h\left(s^{u}\right)$ and $h\left(s^{0}\right)$ respectively.
The replication portfolio is given by
$H(1)=\left\{\begin{array}{l}h\left(S^{U}\right)=x S^{U}+y A(O)(1+R) \\ h\left(S^{D}\right)=x S^{D}+y A(O)(1+R)\end{array}\right.$
solung for $x$ and $y$ gives

$$
\begin{aligned}
& h(s u)=x s^{u}+y A(O)(1+R) \\
\Rightarrow & y=\frac{h(s u)-x s^{u}}{A \operatorname{cox}(1+R)}
\end{aligned}
$$

substituting into the second equation gives

$$
\begin{aligned}
& h\left(S^{D}\right)=x S^{D}+y A(O)(1+R) \\
&=x S^{D}+\frac{h(S u)-x S^{u}}{A(O)(1+R)} A(O)(1+R) \\
&=x S^{D}+h\left(S^{u}\right)-x S^{u} \\
& \Rightarrow h\left(S^{D}\right)-h\left(S^{u}\right)=x\left(S^{D}-S^{u}\right) \\
& \Rightarrow x=\frac{h\left(S^{u}\right)-h\left(S^{D}\right)}{S^{u}-S^{D}}
\end{aligned}
$$

Let

$$
X_{H}=\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{s^{u}-s^{D}}
$$

This ratio is called the detta of the derivative security
since it is a differential ratio for the derivative of a function using

$$
\begin{aligned}
S^{u}-S^{D} & =S(0)(1+U)-S(0)(1+D) \\
& =S(0)(1+U-1-D) \\
& =S(0)(U-D)
\end{aligned}
$$

gives

$$
x_{H}=\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{s(\Delta)(u-\Delta)}
$$

solving for $y_{H}$ gives

$$
\begin{aligned}
y_{H} & =\frac{h\left(s^{u}\right)-x_{H} s^{u}}{A(0)(1+R)} \\
& =\frac{1}{A(0)(1+R)}\left\{h\left(s^{u}\right)-s^{u}\left[\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{s(0)(u-D)}\right]\right\} \\
& =\frac{1}{A(0)(1+R) s(0)(u-D)}\left\{h\left(s^{u}\right) s(0)(u-D)\right.
\end{aligned}
$$

$$
\begin{aligned}
& \left.-s^{u}\left[h\left(s^{u}\right)-h\left(s^{D}\right)\right]\right\} \\
= & \frac{1}{A(o)(1+R) s(o)(u-D)}\left\{h\left(s^{u}\right)[s(o)(u-D)\right. \\
& \left.\left.-s^{u}\right]+s^{u} h\left(s^{D}\right)\right\}
\end{aligned}
$$

Now

$$
s^{u}=s \cos (1+u)
$$

Thus

$$
\begin{aligned}
y_{H}= & \frac{1}{A(D)(1+R) s(D)(u-D)}\left\{h\left(s^{u}\right)[s(0)(u-D)\right. \\
& \left.-s(0)(1+u)]+s(0)(1+u) h\left(s^{D}\right)\right\} \\
= & \frac{1}{A(0)(1+R) s(0)(u-D)}\left\{h\left(s^{u}\right) s(0)(u-D\right. \\
& \left.-1-u)+s(0)(1+u) h\left(s^{D}\right)\right\} \\
= & \frac{s(0)}{A(0)(1+R) s(0)(u-D)}\left\{h\left(s^{u}\right)(1+D)\right.
\end{aligned}
$$

$$
\begin{aligned}
+ & \left.h\left(s^{D}\right)(1+u)\right\} \\
= & \frac{1}{A \operatorname{cox}(1+R)(u-D)}\left[(1+u) h\left(s^{D}\right)\right. \\
- & \left.(1+D) h\left(s^{u}\right)\right]
\end{aligned}
$$

## Thus

$$
\begin{gathered}
x_{H}=\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{s(\Delta)(u-\Delta)} \\
y_{H}=\frac{1}{A(\Delta)(1+R)(u-\Delta)}\left[(1+u) h\left(s^{D}\right)-(1+\Delta) h\left(s^{u}\right)\right]
\end{gathered}
$$

Now it is claimed that the derivatie price is the present value of the portfolid $\left(x_{H}, y_{H}\right)$

$$
\begin{aligned}
H(0) & =U_{\left(x_{H}, y_{H}\right)}(0) \\
& =x_{H} S(0)+y_{H} A(0)
\end{aligned}
$$

$=\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{(U-D)}+\frac{(1+U) h\left(s^{D}\right)-(1+D) h\left(s^{u}\right)}{(1+R)(U-D)}$
Priviously the value of a European Call option C(0) was evaluated here the value of an arbotrary derivative searity is evaluated.
The expression obtained for $H(0)$ can be cleaned up as follows

$$
\begin{aligned}
H(0)= & \frac{h\left(S^{u}\right)-h\left(S^{D}\right)}{(U-D)} \\
& +\frac{(1+U) h\left(S^{D}\right)-(1+D) h\left(S^{u}\right)}{(1+R)(U-D)} \\
= & h\left(S^{u}\right)\left\{\frac{1}{u-D}-\frac{1+D}{(1+R)(U-D)}\right\} \\
& +h\left(S^{D}\right)\left\{-\frac{1}{u-D}+\frac{1+u}{(1+R)(U-D)}\right\}
\end{aligned}
$$

$$
\begin{aligned}
= & h\left(s^{u}\right)\left\{\frac{1+R-1-D}{(1+R)(u-D)}\right\} \\
+ & h\left(s^{d}\right)\left\{\frac{-1-R+1+u}{(1+R)(u-D)}\right\} \\
= & h\left(s^{u}\right)\left(\frac{R-D}{u-D}\right)(1+R)^{-1} \\
& +h\left(s^{d}\right)\left(\frac{u-R}{u-D}\right)(1+R)^{-1}
\end{aligned}
$$

Now note that

$$
\begin{aligned}
& \frac{R-D}{u-D}+\frac{u-R}{u-D}=\frac{u-D}{u-D}=1 \\
\Rightarrow & \frac{u-R}{u-D}=1-\frac{R-D}{u-D}
\end{aligned}
$$

let

$$
G=\frac{R-D}{u-D}
$$

then

$$
\frac{u-R}{u-D}=1-9
$$

Bringing things together gives
$H(0)=\left[h\left(s^{u}\right) q+h\left(s^{D}\right)(1-q)\right](1+R)^{-1}$
where

$$
q=\frac{R-D}{u-D}
$$

Now

$$
\begin{aligned}
& D<R<U=0<R-D<U-D \\
& \Rightarrow 0<\frac{R-D}{U-D}<1 \\
& \Rightarrow 0<9<1
\end{aligned}
$$

It follows that 9 can be interpreted as the probability that the asset price will change to the up price and 1-9 the probability that the asset price change to the down price. These probibilities define a probability distribution $Q$ on the sample space
$\Omega=\{u, d\}$ where $u$ and $d$ represent the events of the asset proce going up and down respective ly.
$Q$ is called the risk-neutral probability.

Now the payoff function $h(s(1))$ can take on two values, $h\left(s^{u}\right)$ and $h\left(s^{D}\right)$, with probabilities 9 and 1-9 respectively. It follows that the expectation of $h(s(1))$ with respect to the risk neutral probability $Q$ is given by
$E_{Q}[h(s(1))]=p h\left(s^{u}\right)+(1-p) h\left(s^{D}\right)$
Thus the price of the derivative security $H(D)$ is the discovented expectation value of the pay off function.
$h(s(1))$, with respect to the risk neutral probability, $Q$, namely

$$
H(0)=E_{a}[h(S(1))](1-R)^{-1}
$$

Next consider the the expectation value of the of the discouted future asset price with respect to the risk-neutral probability, $Q$.

Recall that the risk-neutral probability is given by

$$
\begin{aligned}
& p(u)=q=\frac{R-D}{u-D} \\
& p(d)=1-q=\frac{u-R}{u-D}
\end{aligned}
$$

and the future asset price is given by

$$
s(1)=\left\{\begin{array}{l}
s^{u}=s(0)(1+u) \\
s^{D}=s(0)(1+D)
\end{array}\right.
$$

The discounted fluture asset price is given by

$$
\tilde{s}(1)=s(1)(1+R)^{-1}
$$

It follows that the expectation of the discounted future asset price with respect to the risk neutral probability is given by

$$
\begin{gathered}
E_{Q}[\tilde{s}(1)]=q^{s^{u}}(1+R)^{-1}+ \\
(1-q) s^{D}(1+R)^{-1} \\
=\frac{(R-D)}{(u-D)} s(0) \frac{(1+u)}{(1+R)}+ \\
\frac{(u-R)}{(u-D)} s(0) \frac{(1+D)}{1+R}
\end{gathered}
$$

$$
\begin{aligned}
= & \frac{s(0)}{(u-D)(1+R)}[(R-D)(1+u) \\
& +(u-R)(1+D)] \\
= & \frac{s(0)}{(u-D)(1+R)}[(R-D+u R-u(D) \\
& +(u-R+\dot{u} D-R D)] \\
= & \frac{s(0)}{(u-D)(1+R)}[u-D+R u-R D] \\
= & \frac{s(0)}{(u-D)(1+R)}(u-D)(1+R) \\
= & s(0)=S(0)
\end{aligned}
$$

Since $S(0)$ is constant

$$
\begin{aligned}
E_{Q}[\tilde{s}(0)] & =E_{Q}[s(0)] \\
& =s(0)(q+1-q) \\
& =s(0)
\end{aligned}
$$

Thus the expectation of the discouted asset price with respect to the risk-neutral probability, $Q$, is the same at $t=0$ and $t=1$.

This property is referred to as a martingale under the risk-neutral probability, $Q$.
The reason $Q$ is called risk-neutral will become clear when the expected return with respect to this probability is calculated.

## Theorem

The expected return, with respect to $Q$, for an asset is equal to the risk-free return if and only if $Q$ is the risk-rentral probability. Proof

Recall that the return on an asset is

$$
K_{S}=\frac{S(1)-S(0)}{S(0)}
$$

which is equal to $u$ for the up outcome and $D$ for the down outcome.

If

$$
q=\frac{R-D}{u-D}
$$

Then

$$
\begin{aligned}
E_{Q}\left(k_{s}\right) & =q u+(1-q) D \\
& =\frac{(R-D)}{(u-D)} u+\frac{(u-R)}{(u-D)} \\
& =\frac{1}{u-D}\left(u R-u^{B}+a D-D R\right) \\
& =\frac{R(u-D)}{(u-D)}=R
\end{aligned}
$$

Thus the expected return under the risk-neutral probability is the risk-free return.

To prove the converse assume that the expected return is the risk-free return and solve for 9 ,

$$
\begin{aligned}
& q u+(1-q) D=R \\
\Rightarrow & q(u-D)+D=R \\
\Rightarrow & q=\frac{R-D}{u-D}
\end{aligned}
$$

which is the risk-neutral probability.

## Risk and Return

Here the return on an asset, $K_{s}$, will be compared with the return on a European derivative security, $K_{H}$, with payoft $H=h(s(1))$.
Denote the eppectation with respect to the probability, $P$, by $\mu_{k_{s}}$ and $\mu_{k_{H}}$.

Now

$$
\begin{aligned}
& K_{S}=\frac{S(1)-S(0)}{S(0)} \\
& K_{H}=\frac{H(1)-H(0)}{H(0)}
\end{aligned}
$$

where

$$
H(1)=h(s(1))
$$

Now using

$$
K_{s}^{u}=\frac{s^{u}-\delta(0)}{s(0)} \quad K_{s}^{D}=\frac{s^{D} \cdot s(0)}{\delta(0)}
$$

the expected return on the asset is given by

$$
\mu_{K_{s}}=p K_{s}^{u}+(1-p) K_{s}^{D}
$$

it follows that

$$
\begin{aligned}
& \mu_{k s}=p k_{s}^{u}+(1-p) k_{s}^{D} \\
& =p \frac{\left[s^{u}-s(0)\right]}{s(0)}+(1-p) \frac{\left[s^{D}-s(0)\right]}{s(0)} \\
& =\frac{1}{s(0)}\left\{p s^{u}-p s(0)+s^{D}-s(0)\right. \\
& \left.-p s^{D}+p^{s(0)}\right\} \\
& =\frac{1}{s(0)}\left[p s^{u}+(1-p) s^{D}-s(0)\right] \\
& =\frac{1}{s(0)}\left[p s^{u}+(1-p) s^{D}\right]-1 \\
& =\frac{1}{s(0)}[p s(0)(1+u)+(1-p) s(0)(1+D)]
\end{aligned}
$$

$$
\begin{aligned}
& =p(1+u)+(1-p)(1+D)-1 \\
& =p^{2}+p u+p+D-p-p D-q \\
& =p u-p D+D \\
& =p(u-D)+D
\end{aligned}
$$

The expected return on the European derivative security is groen by, using

$$
K_{H}=\frac{H(1)-H(0)}{H(0)}
$$

and

$$
\begin{gathered}
H^{u}=h\left(S^{u}\right) \quad H^{D}=h\left(S^{D}\right) \\
K_{H}^{u}=\frac{H^{u}-H(0)}{H(0)} \\
K_{H}^{D}=\frac{H^{D}-H(0)}{H(0)}
\end{gathered}
$$

It follows that the expected return of the derivative security is given

$$
\begin{aligned}
\mu_{K_{H}}= & P K_{H}^{u}+(1-P) K_{H}^{D} \\
= & P \frac{\left[H^{u}-H(0)\right]}{H(0)}+(1-P) \frac{\left[H^{D}-H(0)\right]}{H(0)} \\
= & \frac{1}{H(0)}\left[P H^{u}-P H^{2}(0)+H^{D}-H(0)\right. \\
& \left.-P H^{D}+P \hat{H}(0)\right] \\
= & \frac{1}{H(0)}\left[P H^{u}+(1-P) H^{D}\right]-1
\end{aligned}
$$

## Thus

$$
\begin{aligned}
& \mu_{k_{s}}=\rho(u-D)+D \\
& \mu_{k_{H}}=\frac{1}{H(0)}\left[p H^{u}+(1-p) H^{D}\right]-1
\end{aligned}
$$

The variability of the return is given by the variance

$$
\begin{aligned}
& \operatorname{Var}(\bar{X})=E\left[(\bar{X}-E[\bar{X}])^{2}\right] \\
& =E\left[\bar{X}^{2}-\bar{X} E[\bar{X}]-\bar{X} E[\bar{X}]\right. \\
& \left.\quad+(E[\bar{X}])^{2}\right] \\
& =E\left[\bar{X}^{2}\right]-2 E[\bar{X}] E[\bar{X}]+E[\bar{X}]^{2} \\
& =E\left[\bar{X}^{2}\right]-E[\bar{X}]^{2}
\end{aligned}
$$

Now consider the cuent space $\Omega=\{u, d\}$ with distribution $P$. It follows that

$$
\begin{aligned}
& E[\bar{x}]=p \bar{x}_{u}+(1-p) \bar{x}_{0} \\
& E\left[\bar{x}^{2}\right]=p \bar{x}_{u}^{2}+(1-p) \bar{x}_{D}^{2}
\end{aligned}
$$

50

$$
\begin{aligned}
\operatorname{var}(X) & =p \bar{X}_{u}^{2}+(1-p) \bar{X}_{D}^{2} \\
- & {\left[p \bar{X}_{u}+(1-p) \bar{X}_{0}\right]^{2} }
\end{aligned}
$$

$$
\begin{aligned}
= & p \bar{X}_{u}^{2}+(1-p) \bar{X}_{D}^{2}-p^{2} \bar{X}_{u}^{2} \\
& -(1-p)^{2} \bar{X}_{D}^{2}-\alpha_{p}(1-p) \bar{X}_{u} \bar{X}_{D} \\
= & p \bar{X}_{u}^{2}-p^{2} \bar{X}_{u}^{2}+(1-p) \bar{X}_{D}^{2} \\
& -(1-p)^{2} \bar{X}_{D}^{2}-2_{p}(1-p) \bar{X}_{u} \bar{X}_{D} \\
= & p \bar{X}_{u}^{2}(1-p)+(1-p) \bar{X}_{D}^{2}(1-1+p) \\
& -2 p(1-p) \bar{X}_{u} \bar{X}_{D} \\
= & (1-p)\left[p \bar{X}_{u}^{2}+p \bar{X}_{D}^{2} 2_{p} \bar{X}_{u} \bar{X}_{D}\right] \\
= & p(1-p)\left(\bar{X}_{u}^{2}-2 \bar{X}_{u} \bar{X}_{D}+\bar{X}_{D}^{2}\right) \\
= & p(1-p)\left(\bar{X}_{u}-\bar{X}_{D}\right)^{2}
\end{aligned}
$$

The standard deviation is defined by

$$
\sigma_{\underline{x}}=\sqrt{\operatorname{var}(\bar{x})}
$$

recall that

$$
\begin{aligned}
& K_{s}=\frac{S(1)-S(0)}{S(0)} \\
& K_{H}=\frac{H(1)-H(0)}{H(0)}
\end{aligned}
$$

Now

$$
\begin{aligned}
K_{S}^{u}-K_{S}^{D} & =\frac{S^{u}-S(0)}{S(0)}-\frac{S^{D}-S(0)}{S(0)} \\
& =\frac{S^{u}-S^{D}}{S(0)} \\
K_{H}^{u}-K_{H}^{D} & =\frac{H^{u}-H(0)}{H(0)}-\frac{H^{D}-H(0)}{H(0)} \\
& =\frac{H^{u}-H^{D}}{H(0)}
\end{aligned}
$$

It follows that

$$
\sigma_{k_{s}}^{2}=p(1-p)\left(k_{s}^{u}-k_{s}^{D}\right)^{2}
$$

$$
\begin{aligned}
& =p(1-p)\left(\frac{s^{u}-s^{D}}{s(0)}\right)^{2} \\
\sigma_{K_{1 t}}^{2} & =p(1-p)\left(K_{H}^{u}-K_{H}^{D}\right)^{2} \\
& =p(1-p)\left(\frac{H^{u}-H^{D}}{H(0)}\right)^{2}
\end{aligned}
$$

The covariance of two random variables is defined by

$$
\operatorname{COU}(\bar{X}, \bar{I})=E[(\bar{X}-E[X](I-E[I])]
$$

The couriance of $K_{s}$ and $K_{H}$ normalized by the varrance of $k_{s}$ is known as the beta, sometimes the elasticity, is grven by

$$
\beta_{H}=\frac{\operatorname{COU}\left(K_{S}, K_{H}\right)}{\sigma_{K_{S}}^{2}}
$$

To ecaluate $B_{H}$ consider

$$
\begin{aligned}
\operatorname{cov}(\bar{X}, \bar{I})= & E[(\bar{X}-E[\bar{X}](\bar{I}-E[\bar{I}])] \\
= & E[\bar{X} \bar{I}-\bar{I} E[\bar{X}]-\bar{\Delta} E[\bar{Y}] \\
& +E[\bar{X}] E[\bar{Y}]] \\
= & E[\bar{X} \bar{Y}]-2 E[\bar{X}] E[Y] \\
& +E[\bar{X}] E[Y] \\
= & E[\bar{X} \bar{Y}]-E[\bar{X}] E[\bar{Y}]
\end{aligned}
$$

Now consider the cuent space $\Omega=\{u, d\}$ with distribution $P$. Assume that both $\bar{I}$ and I have the same distribution. It folbows that

$$
\begin{aligned}
E[X] & =p X_{u}+(1-p) X_{D} \\
E[I] & =p I_{u}+(1-p) I_{D} \\
E[X I] & =p X_{u} I_{u}+(1-p) X_{D} I_{D}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\operatorname{cov}\left(Z_{1} \mp\right)=E\left[X_{I}\right]-E[X] E[I] \\
=p \bar{X}_{u} I_{u}+(1-p) \bar{I}_{0} I_{D} \\
-\left[p \bar{I}_{u}+(1-p) \bar{I}_{0}\right]\left[p I_{u}+(1-p) I_{D}\right] \\
=p \bar{X}_{u} I_{u}+(1-p) \bar{I}_{0} I_{D} \\
-\left[p^{2} \bar{I}_{u} \bar{I}_{u}+p(1-p) \bar{I}_{D} I_{u}\right. \\
\left.+p(1-p) \bar{X}_{u} \bar{I}_{D}+(1-p)^{2} \bar{I}_{D} I_{D}\right] \\
=p \bar{X}_{u} \bar{I}_{u}+(1-p) \bar{I}_{D} \bar{I}_{D} \bar{I}_{D} \\
-p^{2} \bar{X}_{u} \bar{I}_{u}-p(1-p) \bar{I}_{D} I_{u} \\
-p(1-p) \bar{X}_{u} \bar{X}_{D}-(1-p)^{2} \bar{X}_{D} I_{D} \\
=\bar{X}_{u} I_{u}\left(p-p^{2}\right)-p(1-p) \bar{I}_{D} I_{u} \\
-p(1-p) \bar{X}_{u} \bar{X}_{D}+\bar{X}_{D} I_{D}\left[(1-p)-(1-p)^{2}\right] \\
=p(1-p) \bar{X}_{u} I_{u}-p(1-p) \bar{I}_{D} I_{u} \\
-p(1-p) \bar{I}_{u} \bar{X}_{D}+(1-p) \bar{I}_{D} I_{D}(1-1+p)
\end{aligned}
$$

$$
\begin{aligned}
= & p(1-p) X_{u} I_{u}-p(1-p) X_{b} I_{u} \\
& -p(1-p) X_{u} X_{b}+p(1-p) X_{D} I_{0} \\
= & p(1-p)\left(X_{u} I_{u}-I_{D} I_{u}-X_{u} X_{D}+X_{D} I_{b}\right) \\
= & p(1-p)\left(X_{u}-Z_{D}\right)\left(I_{u}-I_{D}\right)
\end{aligned}
$$

In Summary

$$
\begin{aligned}
\operatorname{cov}(Z, I) & =p(1-p)\left(X_{U}-Z_{D}\right)\left(I_{U}-I_{D}\right) \\
\sigma_{D}^{2} & =p(1-p)\left(Z_{U}-Z_{D}\right)^{2}
\end{aligned}
$$

Now the covariance of $k_{s}$ and $K_{H}$ is given by

$$
\operatorname{cov}\left(K_{s}, K_{4}\right)=p(1-p)\left(K_{s}^{u}-K_{s}^{D}\right)\left(H_{s}^{u}-H_{s}^{D}\right)
$$

now

$$
K_{S}=\frac{S(1)-S(0)}{S(0)} \quad K_{H}=\frac{H(1)-H(0)}{H(0)}
$$

50

$$
\begin{aligned}
K_{s}^{u}-K_{s}^{D} & =\frac{s^{u}-S(0)}{s(0)}-\frac{s^{D}-S(0)}{s(0)} \\
& =\frac{s^{u}-s^{D}}{s(0)}
\end{aligned}
$$

Similarly

$$
\begin{aligned}
K_{H}^{u}-K_{H}^{D} & =\frac{H^{u}-H(0)}{H(0)}-\frac{H^{D}-H(0)}{H(0)} \\
& =\frac{H^{u}-H^{D}}{H(0)}
\end{aligned}
$$

It follows that

$$
\operatorname{cov}\left(K_{S}, K_{H}\right)=P(1-P)\left(\frac{s^{u}-s^{D}}{s(0)}\right) \frac{\left(H^{u}-H^{D}\right)}{H(0)}
$$

Now previously th was shown that

$$
\sigma_{K_{s}}^{2}=p(1-p) \frac{\left(s^{u}-s^{0}\right)^{2}}{s(0)^{2}}
$$

It follows that

$$
\begin{aligned}
\beta_{H}= & \frac{\operatorname{cov}\left(K_{S}, K_{H}\right)}{\sigma_{K_{S}}^{2}} \\
= & \frac{P(1-P)\left(\frac{S^{2}-S^{D}}{S(0)}\right) \frac{\left.H^{u}-H^{D}\right)}{H(0)}}{P(1-P) \frac{\left(S^{u}-S^{D}\right)^{2}}{S(0)^{2}}} \\
= & \frac{\frac{H^{u}-H^{D}}{H(0)}}{\frac{S^{u}-S^{D}}{S(0)}} \\
= & \frac{S(0)}{H(0)} \frac{H^{u}-H^{D}}{S u-S^{D}}
\end{aligned}
$$

but the delta of the derivative security

$$
\begin{aligned}
X_{H} & =\frac{h\left(s^{u}\right)-h\left(s^{D}\right)}{s^{u}-s^{D}} \\
& =\frac{H^{u}-H^{D}}{s^{u}-s^{D}}
\end{aligned}
$$

Thus

$$
\beta_{H}=X_{H} \frac{S(0)}{H(0)}
$$

Additionally, recall

$$
\begin{aligned}
\sigma_{k_{s}}^{2} & =p(1-p)\left(\frac{s^{u}-s^{D}}{s(0)}\right)^{2} \\
\sigma_{k_{H}}^{2} & =p(1-p)\left(\frac{H^{u}-H^{D}}{H(0)}\right)^{2} \\
\Rightarrow \quad \frac{\sigma_{k_{s}}^{2}}{\sigma_{k_{H}}^{2}} & =\frac{\left(\frac{s^{u}-s^{D}}{s(0)}\right)^{2}}{\left(\frac{H^{u}-H^{D}}{H(0)}\right)^{2}}
\end{aligned}
$$

$\Rightarrow \quad \frac{\sigma_{k s}}{\sigma_{k t}}=\frac{H(0)}{S(0)} \frac{\left(S^{u}-S^{D}\right)}{\left(H^{u}-H^{D}\right)}$
but

$$
X_{H}=\frac{H u-H^{D}}{\delta u-S^{D}}
$$

80

$$
\begin{aligned}
\frac{\sigma_{K_{S}}}{\sigma_{K_{H}}} & =\frac{H(O)}{\delta(O)} \frac{1}{x_{H}} \\
& =\frac{1}{\beta_{H}} \\
\Rightarrow \beta_{H} \sigma_{K_{S}} & =\sigma_{K_{H}}
\end{aligned}
$$

Excess Mean Return

The excess mean retworn is defined as the difference between the return on a risky asset and a riskless investment.

Here the riskless retwon is assumed to be $R>0$. Evaluating the riskless return inoolves comparing

$$
\mu_{K_{H}}-R
$$

and

$$
\mu_{k s}-R
$$

Show that the excess mean returns for a derivative $H=h(S(1))$ and the underlying asset $S$ are related by

$$
\mu_{k_{H}}-R=\beta_{H}\left(\mu_{k_{S}}-R\right)
$$

Recall that

$$
\begin{aligned}
\mu_{k_{s}} & =p(u-D)+D \\
\mu_{k_{H}} & =\frac{1}{H(0)}\left[p H^{u}+(1-p) H^{D}\right]-1 \\
\beta_{H} & =\frac{S(0)}{H(0)} \frac{H^{u}-H^{D}}{S u-S^{D}} \\
& =\frac{H^{u}-H^{D}}{H(0)(u-D)}
\end{aligned}
$$

and the risk-neutral probability is given by

$$
q=\frac{R-D}{u-D} \quad 1-q=\frac{u-R}{u-D}
$$

Now

$$
\mu_{k_{s}}-R=P(u-D)+D-R
$$

consider

$$
q=\frac{R-D}{u-D} \Rightarrow R-D=q(u-D)
$$

50

$$
\begin{aligned}
\mu_{k_{s}}-R & =p(u-D)-q(u-D) \\
& =(u-D)(p-q)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
\beta_{H}\left(\mu_{k_{s}}-R\right) & =(p-q) \frac{\left(\hat{u}_{-}-D\right) \frac{\left(H^{u}-H^{D}\right)}{H(0)(u-D)}}{H(0)} \\
& =(p-q) \frac{\left(H^{u}-H^{D}\right)}{H(0)}
\end{aligned}
$$

Now

$$
\begin{aligned}
\mu_{K_{H}}-R & =\frac{1}{H(0)}\left[P H^{u}+(1-P) H^{D}\right]-1-R \\
& =\frac{1}{H(0)}\left[P\left(H^{u}-H^{D}\right)+H^{D}\right]-(1+R) \\
& =P \frac{\left(H^{u}-H^{D}\right)}{H(0)}+\frac{H^{D}}{H(0)}-(1+R)
\end{aligned}
$$

$$
=P \frac{\left(H^{u}-H^{D}\right)}{H(0)}+\frac{H^{D}-H(0)(1+R)}{H(0)}
$$

To go forthur recall that

$$
\begin{aligned}
& H(0)=E_{Q}\left[(1+R)^{-1} h(S(D)]\right. \\
\Rightarrow & (1+R) H(0)=E_{Q}[h(S(1))] \\
= & q H^{u}+(1-q) H^{D} \\
= & q\left(H^{u}-H^{D}\right)+H^{D}
\end{aligned}
$$

Thus

$$
\begin{aligned}
\mu_{K_{H}}-R= & p\left(\frac{H^{u}-H^{D}}{H(0)}+\frac{H^{D}-H(0)(1+R)}{H(0)}\right. \\
= & p \frac{\left(H^{u}-H^{D}\right)}{H(0)}+\frac{H^{D^{D}}-q\left(H^{u}-H^{D}\right)-H^{D}}{H(0)} \\
& p \frac{\left(H^{u}-H^{D}\right)}{H(0)}-q \frac{\left(H^{u}-H^{D}\right)}{H(0)}
\end{aligned}
$$

$$
=(p-q) \frac{H^{u}-H^{D}}{H(0)}
$$

and the desired result is obtained

$$
\begin{aligned}
\beta_{H}\left(\mu_{k_{s}}-R\right) & =(p-q) \frac{\left(H^{u}-H^{D}\right)}{H(0)} \\
& =\mu_{k_{H}}-R \\
\Rightarrow \beta_{H}\left(\mu_{k_{s}}-R\right) & =\mu_{k_{H}}-R
\end{aligned}
$$

Next consider the difference between the expected retworn on the derivative with respect to $P$ and the risk-neutral distribution $Q$, namely

$$
\begin{aligned}
& E_{P}\left(K_{H}\right)-E_{Q}\left(K_{H}\right) \\
& \quad=P \frac{\left[H^{u}-H(0)\right]}{H(0)}+(1-P) \frac{\left[H^{0}-H(0)\right]}{H(0)}
\end{aligned}
$$

$$
\begin{aligned}
& -q \frac{\left[H^{u}-H(0)\right]}{H(0)}-(1-q) \frac{\left[H^{D}-H(0)\right]}{H(0)} \\
& =\frac{1}{H(0)}\left[P\left(H^{u}-H^{D}\right)+H^{D}-H(0)\right] \\
& -\frac{1}{H(0)}\left[q\left(H^{u}-H^{D}\right)+H^{D}-H(0)\right] \\
& =(p-q) \frac{\left(H^{u}-H^{D}\right)}{H(0)}
\end{aligned}
$$

Thus

$$
E_{P}\left(K_{H}\right)-E_{Q}\left(K_{H}\right)=(p-q) \frac{\left(H^{u}-H^{D}\right)}{H(0)}
$$

## Next consider

$$
E_{P}\left(K_{H}\right)-R
$$

and assume that $E_{P}\left(K_{H}\right)>R$. Show that

$$
E_{p}\left(K_{H}\right)=(p-q) \frac{\sigma_{K_{H}}}{\sqrt{p(1-p)}}
$$

Now previously it was shown that

$$
\mu_{K_{H}}-R=E_{p}\left(K_{H}\right)-R=(p-q) \frac{\left(H^{u}-H^{D}\right)}{H(0)}
$$

and

$$
\begin{aligned}
& \sigma_{K_{1 t}}^{2}=P(1-P)\left(\frac{H^{u}-H^{D}}{H(0)}\right)^{2} \\
\Rightarrow & \frac{\sigma_{K_{H}}}{\sqrt{P(1-P)}}=\frac{H^{u}-H^{D}}{H(0)}
\end{aligned}
$$

Thus the desired result is obtained

$$
E_{p}\left(k_{H}\right)-R=(p-q) \frac{\sigma_{k_{H}}}{\sqrt{p(1-p)}}
$$

It follows that if $E_{P}\left(K_{H}\right)>R$ then

$$
p>q
$$

since

$$
\frac{\sigma_{k_{H}}}{\sqrt{p(1-p)}} \geqslant 0
$$

Note that $p=9$ implies that

$$
E_{p}\left(K_{H}\right)=R
$$

thus the return is the risk-free interest rate.

The market price of risk is defined by

$$
m_{s}=\frac{\mu_{k_{s}}-R}{\sigma_{k_{s}}}
$$

determin the relation to the risk neutral probability Previously it was shown that

$$
\mu_{k_{s}}-R=(u-D)(p-q)
$$

$$
\begin{aligned}
\sigma_{K_{s}}^{2} & =p(1-p)\left(\frac{s^{u}-s^{D}}{s(0)}\right)^{2} \\
& =p(1-p)(u-D)^{2}
\end{aligned}
$$

Thus

$$
\begin{aligned}
m_{s}= & \frac{\mu_{k_{s}}-R}{\sigma_{k_{s}}}=\left.\frac{(u-D)(p-q)}{(u-D)}\right|_{p(1-p)} \\
= & \frac{(p-q)}{p(1-p)} \\
\text { so } & m_{s}=\frac{(p-q)}{p(1-p)}
\end{aligned}
$$

Next evaluate the market price of risk for a derivative security $H$ written on an asset S .

$$
m_{H}=\frac{\mu_{K_{H}}-R}{\sigma_{K_{H}}}
$$

previoushy it was shown

$$
\begin{aligned}
& \mu_{k_{H}}-R=(p-q)\left(\frac{H^{u}-H^{D}}{H(0)}\right) \\
& \sigma_{k_{H}}^{2}=p(1-p)\left(\frac{H^{u}-H^{D}}{H(0)}\right)^{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
m_{H} & =\frac{\mu_{k_{H}}-R}{\sigma_{k_{H}}} \\
& =\frac{(p-q) \frac{H^{u}-H D}{H(0)}}{\sqrt{p(1-p)} \frac{\left(H^{u}-H^{D}\right)}{H(0)}} \\
& =\frac{p-q}{p(1-p)} \\
& =m_{s}
\end{aligned}
$$

Find a random variable $G$ playing the role of a "density"
of $Q$ wth respect to $P$, considered on the event space $\Omega=\{u, d\}$.
Now to satisfy the problem constraints it must be that,

$$
\begin{gathered}
q=G(u) p \\
1-q=G(d)(1-p)
\end{gathered}
$$

Recall that the risk-neutral distribution is given by

$$
q=\frac{R-D}{u-D} \quad 1-q=\frac{u-R}{u-D}
$$

thus

$$
\begin{aligned}
G(u) & =\frac{q}{p} \\
& =\frac{(R-D)}{p(u-D)} \\
G(d) & =\frac{(1-q)}{(1-p)}
\end{aligned}
$$

$$
=\frac{u-R}{(1-p)(u-\Delta)}
$$

It follows that

$$
\begin{aligned}
E_{p}(\epsilon) & =G(u) p+G(d)(1-p) \\
& =\frac{(R-D)}{(u-D)}+\frac{(u-R)}{(u-D)} \\
& =1
\end{aligned}
$$

## Two underlying securities

Here extensions of the privious model, which considers a portfolio consisting of a single asset, is exterded to include two conderlying assets.
The initial values of the assels is denoted by $S_{1}(0)$ and $S_{2}(0)$. Their future prices are determined by the random returns $k_{1}$ and $k_{2}$ defined on the event space $\Omega=\{u, d\}$. It follows that the asset prices at $t=1$ are given by

$$
\begin{aligned}
& S_{1}^{u}=S_{1}(0)\left(1+K_{1}^{u}\right) \\
& S_{1}^{D}=S_{1}(0)\left(1+K_{1}^{D}\right) \\
& S_{2}^{u}=S_{2}(0)\left(1+K_{2}^{u}\right) \\
& S_{2}^{D}=S_{2}(0)\left(1+K_{2}^{D}\right)
\end{aligned}
$$

further let

$$
\begin{array}{ll}
u_{1}=K_{1}^{u} & D_{1}=K_{1}^{D} \\
u_{2}=K_{2}^{u} & D_{2}=K_{2}^{D}
\end{array}
$$

The correlation ceefficient between two random variables, $X$ and $I$, is given by

$$
e_{I I}=\frac{\operatorname{COU}(\bar{X}, \bar{I})}{\sigma_{I} \sigma_{I}}
$$

where $\left|e_{x y}\right| \leqslant 1$.
show that there exists numbers $a$ and $b$ such that

$$
k_{1}=a k_{2}+b
$$

using $K_{1}^{u}=u_{1}, K_{1}^{D}=D_{1}, K_{2}^{u}=u_{2}$ and $K_{2}^{D}=D_{2}$ sides two equations

$$
u_{1}=a u_{2}+b \quad D_{1}=a D_{2}+b
$$

from first equation $b=u_{1}-a u_{2}$ substitution into second equation
gives

$$
\begin{aligned}
& D_{1}=a D_{2}+u_{1}-a u_{2} \Rightarrow D_{1}-u_{1}=a\left(D_{2}-u_{2}\right) \\
& \Rightarrow a=\frac{u_{1}-D_{1}}{u_{2}-D_{2}} \\
& b=\frac{u_{1}-u_{2} \frac{\left(u_{1}-D_{1}\right)}{u_{2}-D_{2}}}{u_{2}-D_{2}}=\frac{u_{1} u_{2}-u_{1} D_{2}-u_{2} u_{1}+u_{2} D_{1}}{u_{2}-D_{2}} \\
& =\frac{u_{2} D_{1}-u_{1} D_{2}}{u_{2}}
\end{aligned}
$$

Determine the correlation between $k_{1}$ and $k_{2}$ assuming

$$
K_{1}=a K_{2}+b
$$

It follows that $p_{1}=p_{2}=p$ and

$$
E_{p}\left[k_{1}\right]=a E_{p}\left[k_{2}\right]+b
$$

Previously $t$ was shown that

$$
\sigma_{\Sigma}^{2}=p(1-p)\left(\Delta_{u}-\Delta_{D}\right)^{2}
$$

and for two dentically distributed random variables
$\operatorname{cov}(X, I)=p(1-p)\left(X_{u}-Z_{D}\right)\left(I_{u}-I_{D}\right)$
50

$$
\begin{aligned}
& \sigma_{k_{2}}^{2}=p(1-p)\left(k^{u}-k^{D}\right)^{2} \\
& \sigma_{k_{2}}=\left(k_{2}^{u}-k_{2}^{D}\right) \sqrt{p(1-p)}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
\sigma_{k_{2}} & =\left(k_{2}^{u}-k_{2}^{D}\right) \sqrt{p(1-p)} \\
\sigma_{k_{1}} & =\left(k_{1}^{u}-k_{1}^{D}\right) \sqrt{p(1-p)} \\
& =\left[\left(a k_{2}^{u}+b\right)-\left(a k_{2}^{D}+D\right)\right] \sqrt{p(1-p)} \\
& =\operatorname{lal}\left(k_{2}^{u}-k_{2}^{D}\right) \sqrt{p(1-p)} \\
& =|a| \sigma_{k_{2}}
\end{aligned}
$$

and

$$
\begin{aligned}
& \operatorname{cov}\left(K_{1}, K_{2}\right)=p(1-p)\left(K_{1}^{u}-K_{1}^{D}\right)\left(K_{2}^{u}-K_{2}^{D}\right) \\
& =p(1-p)\left[\left(a K_{2}^{u}+b\right)-\left(a K_{2}^{D}+b\right)\right]\left(K_{2}^{u}-K_{2}^{D}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =p(1-p) a\left(k_{2}^{u}-k_{2}^{D}\right)^{2} \\
& =a \sigma_{k_{2}}^{2}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
l_{k_{1} k_{2}} & =\frac{\operatorname{cov}\left(k_{1}, k_{2}\right)}{\sigma_{k_{1}} \sigma_{k_{2}}} \\
& =\frac{a \sigma_{k_{2}}^{2}}{|a| \sigma_{k_{2}}^{2}} \\
& =\frac{a}{|a|}
\end{aligned}
$$

thus

$$
e_{k_{1} k_{2}}=\left\{\begin{array}{cc}
1 & a>0 \\
-1 & a<0
\end{array}\right.
$$

for $a=0 \quad e_{k_{1} k_{2}}$ is undefined
Assumine $k_{1}=a k_{2}+b$ find the paypft function $s_{2}(1)=h(s,(1))$
since $k_{1}=a k_{2}+b$ it follows that

$$
\begin{aligned}
& u_{1}=a u_{2}+b \\
\Rightarrow & u_{2}=\frac{u_{1}-b}{a} \quad D_{1}=a D_{2}+b \\
& D_{2}=\frac{D_{1}-b}{a}
\end{aligned}
$$

It follows that

$$
h(s(1))=\frac{s(1)-b}{a}
$$

Find the replicating portfolio for

$$
h(s(1))=\frac{s(1)-b}{a}
$$

the replicating portfolio is given by

$$
h(S(1))=x S(1)+y A(1)
$$

but $h\left(s(1)=\frac{s(1)-b}{a}\right.$
80

$$
\frac{s(1)-b}{a}=x s(1)+y A(1)
$$

this expression is equioalent to the two equations

$$
\begin{aligned}
\frac{s^{u}-b}{a} & =x s^{u}+y A(0)(1+R) \\
\frac{s^{D}-b}{a} & =x s^{D}+y A(0)(1+R)
\end{aligned}
$$

From first equation

$$
\begin{aligned}
& s^{u}-b=a \times s^{u}+a y A(0)(1+R) \\
\Rightarrow & a y A(0)(1+R)=s^{u}-b-a \times s^{u} \\
\Rightarrow & y=\frac{1}{a A(0)(1+R)}\left[s^{u}-b-a \times s^{u}\right]
\end{aligned}
$$

substitution into second equation gives

$$
\begin{aligned}
& \frac{S^{D}-b}{a}=x S^{D}+A \cos (1+R)\{ \\
& \left.\frac{1}{a A(D)(1+R)}\left[s^{u}-b-a \times s^{u}\right]\right\}
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow \frac{s^{D}-b}{a}=x s^{D}+\frac{1}{a}\left[s^{U}-b-a \times s^{T}\right] \\
& =x\left(s^{D}-s^{U}\right)+\frac{s u^{-} b}{a} \\
& \Rightarrow x\left(s^{D}-s^{U}\right)=\frac{s^{D}}{a}-\frac{b^{1}}{a}-\frac{s^{4}}{a}+\frac{b}{a} \\
& =\frac{\left(s^{D}-s^{4}\right)}{a} \\
& \Rightarrow x=\frac{1}{a}
\end{aligned}
$$

substituting into the expression for y gives

$$
\begin{aligned}
y & =\frac{1}{a A(O)(1+R)}\left[s^{u}-b-a x s^{u}\right] \\
& =\frac{1}{a A(O)(1+R)}\left[s^{u}-b-s^{u}\right] \\
& =\frac{b}{a A(0)(1+R)}
\end{aligned}
$$

Thus the replicating portfolio is given by

$$
(x, y)=\left(\frac{1}{a}, \frac{-b}{a A(D)(1+R)}\right)
$$

Let $Q_{1}$ denote the risk-neutral probability with respect to $s_{1}$

$$
\begin{aligned}
& Q_{1}=\left\{q_{1}, 1-q_{1}\right\} \\
& q_{1}=\frac{R \cdot D_{1}}{u_{1}-D_{1}}
\end{aligned}
$$

Since $s_{2}$ is a derivative security with underlyling asset $s_{1}$ the no-arbitrage price is given by

$$
\begin{aligned}
S_{2}(0) & =E_{Q_{1}}\left[\tilde{S}_{2}(1)\right] \\
& =E_{Q}\left[(1+R)^{-1} S_{2}(1)\right]
\end{aligned}
$$

Consider the risk-neutral probability with respect to $S_{2}$,

$$
\begin{aligned}
Q_{2} & =\left\{q_{2}, 1-q_{2}\right\} \\
q_{2} & =\frac{R-D_{2}}{u_{2}-D_{2}}
\end{aligned}
$$

Recall the martingale property of the risk-neutral probobility.

$$
\begin{aligned}
S_{2}(0) & =E_{Q_{2}}\left[\tilde{S}_{2}(1)\right] \\
& =E_{Q_{2}}\left[(1+R)^{-1} S_{2}(1)\right]
\end{aligned}
$$

It follows that

$$
\begin{aligned}
& E_{Q_{1}}\left[\tilde{S}_{2}(1)\right]=E_{Q_{2}}\left[\tilde{S}_{2}(1)\right] \\
\Rightarrow & E_{Q_{1}}\left[(1+R)^{-1} S_{2}(1)\right]=E_{Q_{2}}\left[(1+R)^{-1} S_{2}(1)\right] \\
\Rightarrow & \left(1+R^{-1}\right) E_{Q_{1}}\left[S_{2}(1)\right]=(1+R)^{-1} E_{Q_{2}}\left[S_{2}(1)\right] \\
\Rightarrow & E_{Q_{1}}\left[S_{2}(1)\right]=E_{Q_{2}}\left[S_{2}(1)\right]
\end{aligned}
$$

Now

$$
K_{2}=\frac{S_{2}(1)-S_{2}(0)}{S_{2}(0)}
$$

and

$$
k_{2}^{u}=u_{2} \quad k_{2}^{D}=D_{2}
$$

so

$$
\begin{aligned}
E_{Q_{2}}\left(k_{2}\right) & =q_{2} u_{2}+\left(1-q_{2}\right) D_{2} \\
& =\frac{\left(R-D_{2}\right) u_{2}}{u_{2}-D_{2}}+\frac{\left(u_{2}-R\right)}{u_{2}-D_{2}} D_{2} \\
& =\frac{R u_{2}-D_{2} u_{2}+u_{2} D_{2}-R D_{2}}{u_{2}-D_{2}} \\
& =R \frac{\left(u_{2}-D_{2}\right)}{u_{2}-D_{2}} \\
& =R
\end{aligned}
$$

and

$$
E_{Q_{1}}\left[k_{2}\right]=q_{1} u_{2}+\left(1-q_{1}\right) D_{2}
$$

since previously it was shown that

$$
E_{Q_{2}}\left[K_{2}\right]=E_{Q_{1}}\left[K_{2}\right]
$$

it follows that

$$
\begin{aligned}
& q_{1} u_{2}+\left(1-q_{1}\right) D_{2}=R \\
\Rightarrow \quad & q_{1}=q_{2}
\end{aligned}
$$

Since $q_{1}$ and $q_{2}$ are risk neutral it follows that No arbitrage implies

$$
Q_{1}=Q_{2}
$$

The opposite can also be proven, namely, $Q_{1}=Q_{2}$ implies no-arbtrage. Recall that to prove no orbitrage it must be shown that

$$
\begin{aligned}
U_{x y 2}(0) & =0 \\
\Rightarrow U_{x y 2}(1) & =0
\end{aligned}
$$

## Consider the portfolio

$$
U_{x y z}(0)=x S_{1}(0)+y A(0)+z S_{2}(0)=0
$$

where $s_{2}$ is a derivative security with conderlying asset $S_{1}$.

Now

$$
\begin{aligned}
& E_{Q_{1}}\left[V_{x y z}(1)\right]=E_{Q_{1}}\left[x S_{1}(1)+y A(1)+2 S_{2}(1)\right] \\
& =E_{Q_{1}}\left[x S_{1}(1)\right]+E_{Q_{1}}[y A(1)]+E_{Q_{1}}\left[2 S_{2}(1)\right]
\end{aligned}
$$

since $Y A(1)$ is not random it follows that

$$
E_{Q_{1}}[y A(1)]=y A(1)=y A(0)(1+R)
$$

since $Q_{1}=Q_{2}$ it follows that

$$
E_{Q_{1}}\left[2 S_{2}(1)\right]=2 E_{Q_{2}}\left[S_{2}(1)\right]
$$

from the martigale property of the risk-neutral measure it follows that

$$
E_{Q_{2}}\left[S_{2}(D)\right]=(1+R) S_{2}(0)
$$

additionally from the martingale property of $Q_{1}$

$$
E_{Q_{1}}\left[S_{1}(1)\right]=(1+R) S_{1}(0)
$$

putting things together gives

$$
\begin{aligned}
E_{Q_{1}} & {\left[U_{x y z}(1)\right]=x(1+R) S_{1}(0) } \\
& +y(1+R) A(0)+z(1+R) S_{2}(0) \\
= & (1+R)\left[x S_{1}(0)+y A(0)+2 S_{2}(0)\right]
\end{aligned}
$$

but

$$
\begin{aligned}
U_{x y z}(0) & =x S_{1}(0)+y A(0)+2 S_{2}(0) \\
& =0
\end{aligned}
$$

Trus

$$
E_{Q_{1}}\left[U_{x / 2}(1)\right]=0
$$

and the desired result is obtained, $Q_{1}=Q_{2}$ implies no artsitrage.
what this result is saying is trad the binsmial, i.e two state, statisical model is inadequate to model for portfolios with two arbitrary assets. Here it was shoun that the two assets have identical probability distributions. Otner more general models, which include more possible atcomes must be developed.

## Exercise: Arbitrage opportionity

Find an arbitrage if

$$
\begin{gathered}
s_{1}(0)=50, u_{1}=20 \%, D_{1}=-10 \% \\
s_{2}(0)=80, u_{2}=15 \varphi_{0}, D_{2}=-5 \% \\
A(0)=10 \quad R=10 \%
\end{gathered}
$$

now no arbitrge implies that

$$
Q_{1}=Q_{2}
$$

50

$$
\begin{aligned}
& q_{1}=\frac{R-D_{1}}{u_{1}-D_{1}}=\frac{0.1+0.1}{0.2+01}=\frac{0.2}{0.3}=\frac{2}{3} \\
& q_{2}=\frac{R-D_{2}}{u_{2}-D_{2}}=\frac{0.1+0.05}{0.15+0.05}=\frac{0.15}{0.2}=\frac{3}{4}
\end{aligned}
$$

Thus $Q_{1} \neq Q_{2}$ so an arbitage is possible.

Recall that an artotrage is defined by

$$
\begin{aligned}
& U_{x y z}(0)=0 \\
& U_{x y z}(1) \geqslant 0
\end{aligned}
$$

where the last inequality holds with probability 1.

To construct an arbitrage a portfolio must be purchasal that satisfies
$U_{x y z}(0)=x S_{1}(0)+y A(0)+z S_{2}(0)=0$
$U_{x y z}(1)=x S(1)+y A(0)(1+R)+z S_{2}(1) \geqslant 0$
Putting the numbers in the first equation gives

$$
\begin{aligned}
& x 50+y 10+z 80=0 \\
\Rightarrow \quad & 5 x+y+8 z=0
\end{aligned}
$$

Next consider $U_{x y z}(1)$. solve for $x, y$ and 2 such that the poyoff of the down state is 0 . Recall that
$U_{x y z}(n)=\left\{\begin{array}{l}x S_{1}(0)\left(1+U_{1}\right)+y A(0)(1+R)+2 S_{2}(0)\left(1+U_{2}\right) \\ x S_{1}(0)\left(1+D_{1}\right)+y A(0)(1+R)+2 S_{2}(0)\left(1+D_{2}\right)\end{array}\right.$
for the down result

$$
x S_{1}(0)\left(1+D_{1}\right)+y A(0)(1+R)+2 S_{2}(0)\left(1+D_{2}\right)=0
$$

inserting parameters gives

$$
\begin{aligned}
& x(50)(0.9)+y(10 x(1.1)+z(80)(0.85)=0 \\
\Rightarrow & 45 x+11 y+762=0
\end{aligned}
$$

Thus two equations are available to eliminate two varriables

$$
\begin{aligned}
& 45 x+11 y+76 z=0 \\
& 5 x+y+8 z=0
\end{aligned}
$$

From second equation

$$
2=-\frac{(5 x+y)}{8}
$$

substituting into first equation to eluminate y gives

$$
\begin{aligned}
& 45 x+11 y-76\left(5 \frac{x+y}{8}\right)=0 \\
\Rightarrow & 45 x-\frac{76 x 5}{8} x-\frac{76 y}{8}+11 y=0 \\
\Rightarrow & x\left[45-\frac{(76)(5)}{8}\right]+\frac{y\left[11-\frac{76}{8}\right]=0}{} \\
\Rightarrow & \frac{5}{8} x[(8)(9)-76]+\frac{y}{8}[(8)(11)-76]=0 \\
\Rightarrow & \frac{5}{8} x(72-76)=-\frac{y}{8}(88-76) \\
\Rightarrow & -(5 x(4) x=-y(12) \\
\Rightarrow & 5 x=3 y \Rightarrow y=\frac{5}{3} x
\end{aligned}
$$

substituting into the first
equation gives

$$
\begin{aligned}
z & =-\frac{(5 x+y)}{8}=-\frac{5 x}{8}-\frac{y}{8} \\
& =-\frac{5 x}{8}-\frac{5 x}{24} \\
& =-\frac{x}{8}\left(5+\frac{5}{3}\right) \\
& =-\frac{x}{8}\left(\frac{15+5}{3}\right) \\
& =-\frac{20 x}{24}=-\frac{5}{6} x
\end{aligned}
$$

Inserting parameters into the up equation gives

$$
\begin{aligned}
& x S_{1}(0)\left(1+u_{1}\right)+y A(0)(1+R)+z S_{2}(0)\left(1+u_{2}\right) \\
\Rightarrow & x(50)(1+0.2)+y(10)(1+0.1)+z(80)(1+0.15) \\
\Rightarrow & x(5)(1.2)+y(10)(1.1)+z(80)(1.15) \\
\Rightarrow & 60 x+11 y+92 z
\end{aligned}
$$

so in summary for parameters

$$
\begin{aligned}
& S_{1}(0)=50, U_{1}=20 \%, D_{1}=-10 \% \\
& S_{2}(0)=80, U_{2}=15 \varphi_{0}, D_{2}=-5 \% \\
& A(0)=10 R=10 q_{0}
\end{aligned}
$$

An arbitrage is possible if

$$
\begin{aligned}
& U_{x y z}(0)=5 x+y+8 z=0 \\
& U_{x y z}(1)=\left\{\begin{array}{l}
60 x+11 y+92 z>0 \\
45 x+11 y+76 z=0
\end{array}\right.
\end{aligned}
$$

since

$$
q_{1}=\frac{2}{3} \neq q_{2}=\frac{3}{4}
$$

It was shown that using the equation for $U_{x y z}(0)$ and $U_{x y z}$ to find $y$ and $z$ as a function of $x$ gives

$$
y=\frac{5}{3} x \quad z=-\frac{5}{6} x
$$

These expressions can be valdated by insertion into $U_{x_{12}}(0)$ and $U_{x y z}^{D}$

$$
\begin{aligned}
U_{x y z}(0) & =5 x+y+8 z=0 \\
& =5 x+\frac{5}{3} x-\frac{(8)(5)}{6} x \\
& =5 x\left(1+\frac{1}{3}-\frac{8}{6}\right) \\
& =5 x\left(\frac{4}{3}-\frac{4}{3}\right) \\
& =0
\end{aligned}
$$

Similarly

$$
\begin{aligned}
U_{x / 2}^{D} & =45 x+11 y+762=0 \\
& \Rightarrow 45 x+11\left(\frac{5 x}{3}\right)+76\left(-\frac{5}{6} x\right) \\
& =45 x+\frac{55}{3} x-\frac{(38)(5)}{3} x
\end{aligned}
$$

$$
\begin{aligned}
& =5 x\left[9+\frac{11}{3}-\frac{38}{3}\right] \\
& =\frac{5 x}{3}(27+11-38) \\
& =0
\end{aligned}
$$

Thus the solutions are valid. Finally consider $U_{x y z}^{u}$

$$
\begin{aligned}
U_{x y z}^{u} & =60 x+11 y+92 z \\
& =60 x+11\left(\frac{5 x}{3}\right)+92\left(-\frac{5 x}{6}\right) \\
& =5 x\left[12+\frac{11}{3}-\frac{92}{6}\right] \\
& =5 x\left[\frac{(3 x(2)}{3}+\frac{11}{3}-\frac{46}{3}\right] \\
& =\frac{5}{3} x(36+11-46) \\
& =\frac{5}{3} x
\end{aligned}
$$

Thus for $x \geqslant 0 \quad \bigcup_{x y 2}^{u} \geqslant 0$

Finally, for the parameters

$$
\begin{aligned}
& S_{1}(0)=50, U_{1}=20 \%, D_{1}=-10 \% \\
& S_{2}(0)=80, U_{2}=15 \varphi_{0}, D_{2}=-5 \% \\
& A(0)=10 R=10 q_{0}
\end{aligned}
$$

an arbitrage opportunity exists since

$$
q_{1}=\frac{2}{3} \neq q_{2}=\frac{3}{4}
$$

It was shown that for

$$
y=\frac{5}{3} x \quad z=-\frac{5}{6} x
$$

and $x>0$

$$
\begin{gathered}
v_{x y z}(0)=5 x+y+8 z=0 \\
v_{x y z}(1)=\left\{\begin{array}{l}
60 x+11 y+92 z=\frac{5}{3} x>0 \\
45 x+11 y+76 z=0
\end{array}\right.
\end{gathered}
$$

Thus for the given parameters an arbitrage with risk-free profit of

## $\frac{5}{3} x$

is possible.
This profit would be dotained by short selling sicex units of the asset $S_{2}$ at price $\$ 80$, Raising $(80)(5 / 6) x$ in ash. with these funds
$\$ 10(5 / 3 x)$ is deposited at nisk. free rate and $\$ 50(5 / 3 x)$ is used to by $5 / 3 x$ units of the asset $s_{1}$.

## Exercise

Find an expression for $s_{2}^{d}$ as a function of the remaining parameters so there is no arbitrage.

## solution

No arbitrage implies that

$$
Q_{1}=Q_{2}
$$

50

$$
\frac{R-D_{2}}{U_{2}-D_{2}}=\frac{R-D_{1}}{U_{1}-D_{1}}
$$

soluing for $D_{2}$ gives

$$
\begin{aligned}
& \frac{R-D_{2}}{U_{2}-D_{2}}=\frac{R-D_{1}}{U_{1}-D_{1}} \\
\Rightarrow \quad R-D_{2}= & \frac{\left(R-D_{1}\right)\left(U_{2}-D_{2}\right)}{U_{1}-D_{1}} \\
= & \frac{R U_{2}-D_{1} U_{2}-R D_{2}+D_{1} D_{2}}{U_{1}-D_{1}} \\
= & \frac{R U_{2}-D_{1} U_{2}}{U_{1}-D_{1}}+\frac{D_{1} D_{2}-R D_{2}}{U_{1}-D_{1}}
\end{aligned}
$$

$$
\begin{aligned}
& =u_{2} \frac{\left(R-D_{1}\right)}{u_{1}-D_{1}}-D_{2} \frac{\left(R-D_{1}\right)}{u_{1}-D_{1}} \\
& \Rightarrow R-\frac{u_{2}\left(R-D_{1}\right)}{u_{1}-D_{1}}=D_{2}-\frac{D_{2}\left(R-D_{1}\right)}{u_{1}-D_{1}} \\
& =D_{2}\left[1-\frac{R-D_{1}}{u_{1}-D_{1}}\right] \\
& =D_{2}\left[\frac{\left(u_{1}-D_{1}\right)-\left(R-D_{1}\right)}{u_{1}-D_{1}}\right] \\
& =D_{2} \frac{\left(u_{1}-R\right)}{u_{1}-D_{1}} \\
& \Rightarrow D_{2}=\frac{\left(u_{1}-D_{1}\right)}{\left(u_{1}-R\right)}\left[R-\frac{u_{2}\left(R-D_{1}\right)}{u_{1}-D_{1}}\right] \\
& =\frac{\left(u_{1}-D_{1}\right)}{u_{1}-R}\left[R\left(\frac{\left.u_{1}-D_{1}\right)-u_{2}\left(R-D_{1}\right)}{u_{1}-D_{1}}\right]\right. \\
& =\frac{1}{u_{1}-R}\left(R u_{1}-R D_{1}-u_{2} R+u_{2} D_{1}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{u_{1}-R}\left[R\left(u_{1}-D_{1}\right)-u_{2}\left(R-D_{1}\right)\right] \\
& =\frac{R\left(u_{1}-D_{1}\right)}{u_{1}-R}-u_{2} \frac{\left(R-D_{1}\right)}{u_{1}-R}
\end{aligned}
$$

Thus a relationship between $D_{2}$ and the other parameters that insures no-arbitrage is given by

$$
D_{2}=R \frac{\left(u_{1}-D_{1}\right)}{u_{1}-R}-\frac{u_{2}}{\frac{\left(R-D_{1}\right)}{u_{1}-R}}
$$

It follows that

$$
\begin{aligned}
S_{2}^{d} & =S_{2}(0)\left(1+D_{2}\right) \\
& =S_{2}(0)\left[1+\frac{R\left(u_{1}-D_{1}\right)}{u_{1}-R}-u_{2} \frac{\left(R-D_{1}\right)}{u_{1}-R}\right]
\end{aligned}
$$

## Trinomial model

The step in generalizing the single step model is to add another outcome. This is called a trinomial model. The cuent space of the model is

$$
\Omega=\{u, m, d\}
$$

where $u$ and $d$ are the previous up and down outcomes used in the binomial model. Addionally an intermediate outcome is added and denoted by $m$.
The probabilities of the atcomes are denoted by

$$
P_{a}, P_{m}, P_{d} \in(0,1)
$$

and satisfy

$$
P_{u}+P_{m}+P_{d}=1
$$

It follows that the expectation of a random variable I
is given by
$E[X]=p_{u} \bar{X}(u)+p_{m} \bar{X}(m)+p_{c} \bar{X}(d)$
The rate of return for an asset with this model is given by

$$
K=\left\{\begin{array}{l}
K^{u}=u \text { with probability } p_{n} \\
K^{m}=M \text { with probability } p_{M} \\
K^{D}=D \text { with probability } p_{D}
\end{array}\right.
$$

It is assumed that

$$
D<M<U
$$

A derivative security is defined by

$$
H(1)=h(S(1))
$$

## Theorem

For the trinomial model no-arbitrage is equivalent
to $D<R<U$

## Proof

To prove that an arbitrage exits it must be shown that if

$$
U_{x y}(0)=0
$$

then

$$
U_{x y}(1) \geqslant 0
$$

with probability 1.
Assume that

$$
\begin{aligned}
U_{x y}(0) & =x S(0)+y A(0)=0 \\
\Rightarrow y & =-\frac{x S(0)}{A(0)}
\end{aligned}
$$

It follows that

$$
U_{x y}(1)=x S(1)-x \frac{S(0)}{A(0)} A(1)
$$

Now

$$
\begin{aligned}
& K_{S}=\frac{S(1)-S(0)}{S(0)} \\
& \Rightarrow S(1)=S(0)\left(1+K_{S}\right)
\end{aligned}
$$

50

$$
\begin{aligned}
U_{x y}(1) & =x S(1)-\frac{x S(0)}{A(0)} A(1) \\
& =x S(0)\left(1+K_{s}\right)-x \frac{S(0)}{A(0)} A(0)(1+R) \\
& =x S(0)\left(1+K_{s}\right)-x S(0)(1+R) \\
& =x S(0)\left(1+K_{s}-1-R\right) \\
& =x S(0)\left(K_{s}-R\right) \\
& =\left\{\begin{array}{l}
x S(0)(L-R) \\
x S(0)(M-R) \\
x S(0)(D-R)
\end{array}\right.
\end{aligned}
$$

Now is $R<D$ then since it is assumed that

## $D<M<R$

it follows that for $x>0$
$U_{x y}(1)=\left\{\begin{array}{l}x s(0)(L-R)>0 \\ x s(0)(M-R)>0 \\ x s(0)(D-R)>0\end{array}\right.$
Thus $U_{x y}(1)>0$ with probability one, so $R<D$ leads to an arbitrage. This portfolio corresponds to borrowing enough mohey to purchase the asset and then paying of the loan when the asset is sold.

Next assume that $R>U$ and $x<0$ then
$U_{x y}(1)=\left\{\begin{array}{l}x s(0)(L-R)>0 \\ x s(0)(M-R)>0 \\ x s(0)(D-R)>0\end{array}\right.$
so the portfolio makes
a profit with probability one, so $R>u$ leads to an arbitrage. This portfolio corresponds short selling the asset and investing the money at risk-free interest $R$. Then withrawing the money to purchase the asset for return to linder.
It follows the to prevent arbitrage in the frinomial model it must be that

$$
D<R<U
$$

then
$U_{x y}(1)=\left\{\begin{array}{l}x s(0)(L-R)>0 \\ x s(0)(M-R) 0 \\ x s(0)(D-R)<0\end{array}\right.$
which is not profitable with probability 1.

## Replicating Portfolid

In real life stocks Change price discretely it ticks. For example if $S(0)=\$ 30$ and a tick is $\$ 0.50$ then $s^{u}=\$ 30.50$ and $s^{D}=\$ 29.50$ and $s^{m}=\$ 30$. Hawns an intermediate price allows modeling the case where the price does not change.
Consider a derivative security, $H(1)=h(S(1))$, where $h$ is the payoff function for the security. For the trinomial model there are three payoffs

$$
H^{u}, H^{m}, H^{d}
$$

A single asset replicating portfolio is given by

$$
H(1)=x S(1)+y A(1)
$$

$$
H(1)=\left\{\begin{array}{l}
H^{u}=x S^{u}+y A(O)(1+R) \\
H^{m}=x S^{m}+y A(O)(1+R) \\
H^{d}=x S^{d}+y A(O)(1+R)
\end{array}\right.
$$

This equation is over dertermined and has no general solution Thus a single asset replicating portfolio does nat exist in general.

## Exercise

Given a trinomial single-asset model with parameters

$$
\begin{gathered}
R=0, \quad s(0)=10, \quad s^{u}=20 \\
s^{m}=15, \quad s^{d}=7.5
\end{gathered}
$$

show that the derivative security $H$ can be replicated only

$$
3 H^{4}-5 H^{m}+2 H^{d}=0
$$

## Solution

The equations for the replicating are given by

$$
\Rightarrow \quad \begin{aligned}
& H^{u}=x s^{u}+y A(0)(1+R) \\
& H^{m}=x s^{m}+y A(0)(1+R) \\
& H^{d}=x s^{d}+y A(0)(1+R) \\
& H^{u}=20 x+y A(0) \\
& H^{m}=15 x+y A(0) \\
& H^{d}=7.5 x+y A(0) \\
& \Rightarrow \quad 3 H^{u}=60 x+3 y A(0) \\
& 5 H^{m}=-75 x-5 y A(0) \\
& 2 H^{d}=15+2 y A(0)
\end{aligned}
$$

Adding the equations gives

$$
\begin{gathered}
3 H^{u}-5 H^{m}+2 H^{d}=x(60-75-15) \\
+A(0) y(3-5+2)
\end{gathered}
$$

$$
\begin{array}{cc} 
& =0 \\
\Rightarrow \quad & 3 H^{u}-5 H^{m}+2 H^{d}=0
\end{array}
$$

## Exercise

Let $S(0)=100, A(0)=1, u=20 \%$
$M=109_{0}, D=-159_{0}, R=5 \%_{0} \quad H^{4}=25$

$$
H^{m}=5
$$

Find $H^{d}$ such that there is a unique replicating portfolio.

## Solution

The replicating portfolio is given by

$$
\begin{aligned}
& H^{u}=x S^{u}+y A(0)=x S(0)(1+u)+y A(0)(1+R) \\
& H^{m}=x S^{m}+y A(0)=x S(0)(1+M)+y A(0)(1+R) \\
& H^{d}=x S^{d}+y A(0)=x S(0)(1+D)+y A(0)(1+R)
\end{aligned}
$$

$$
\begin{aligned}
\Rightarrow \quad 25 & =100(1+02) x+(1+0.05) y \\
\quad 5 & =100(1+0.1) x+(1+0.05) y \\
H^{d} & =100(1-0.15) x+(1+0.05) y \\
\Rightarrow \quad 25 & =120 x+1.05 y \\
\quad 5 & =110 x+1.05 y \\
H^{d} & =85 x+1.05 y
\end{aligned}
$$

The first set of equations can be used to solve for $x$ and $y$

$$
\begin{aligned}
25 & =120 x+1.05 y \\
\Rightarrow x & =\frac{25-1.05 y}{120}
\end{aligned}
$$

Substitution into the second equation grues

$$
\begin{aligned}
\Rightarrow \quad S & =110\left(\frac{25-1.05 y}{120}\right)+1.05 y \\
& =\frac{(110)(25)}{120}-\frac{(110)(1.05)}{120} y+1.05 y
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{(110)(25)}{120}+(1.05) y\left[1-\frac{110}{120}\right] \\
\Rightarrow & 5-\frac{(110)(25)}{120}=(1.05) y \frac{(120-110)}{120} \\
& \frac{1}{120}[(5)(120)-(110)(25)]=1.05 \frac{(10)}{120} y \\
& \frac{1}{120}(600-2750)=(1.05)(10) y \\
& -2150=(1.05)(10) y \\
& y=-\frac{215}{1.05}
\end{aligned}
$$

substitution into the expression for $x$ gives

$$
\begin{aligned}
x & =\frac{25-1.05}{120} \\
& =\frac{25}{120}-\frac{(1.05)}{120}\left(\frac{-215}{1.05}\right)
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{120}(25+215) \\
& =\frac{240}{120}=2
\end{aligned}
$$

## Thus

$$
x=2 \quad y=\frac{-215}{1.05}
$$

To verify substitute solutions into first two equations

$$
\begin{aligned}
25 & =120 x+1.05 y \\
5 & =110 x+1.05 y \\
25 & =(120)(2)+(1.05) \frac{-215}{1.05} \\
\Rightarrow \quad 5 & =(110)(2)+\left(1.05 \frac{(-215)}{1.05}\right. \\
\Rightarrow \quad 25 & =240-215 \\
5 & =220-215
\end{aligned}
$$

Thus the solutions are correct it follows that

$$
\begin{aligned}
H^{c} & =85 x+1.05 y \\
& =(85)(2)+(1.05)\left(-\frac{215}{1.05}\right) \\
& =170-215 \\
& =-45
\end{aligned}
$$

Thus

$$
H_{d}=-45
$$

## Exercise

For general $H^{u}, H^{m}, H^{d}$ find a relation between these three numbers so that there is a unique replicating portfolio with corbitrary $s(0), u, m, D, R$.

## Solution

The replicating portfdio is
defined by

$$
\begin{aligned}
H^{u} & =x s^{u}+y A(0)(1+R) \\
H^{m} & =x s^{m}+y A(0)(1+R) \\
H^{d} & =x s^{d}+y A(0)(1+R) \\
H^{u} & =x s(0)(1+u)+y A(0)(1+R) \\
H^{m} & =x s(0)(1+M)+y A(0)(1+R) \\
H^{d} & =x s(0)(1+D)+y A(0)(1+R)
\end{aligned}
$$

Following the proceedure used in the previous exercise, use the first two equations to solve for $x$ and $y$ and substitute the result into the third equation to determine the desired relation, so from the first equation

$$
H^{u}=x S(0)(1+u)+y A(0)(1+R)
$$

$$
\begin{aligned}
& \Rightarrow \quad x S(O)(1+u)=H^{u}-y A \cos (1+R) \\
& \Rightarrow \quad x=\frac{H^{u}-y A(O)(1+R)}{S(O)(1+u)}
\end{aligned}
$$

subtrluting this result into the second equation gives.

$$
\begin{aligned}
H^{m}= & x S(0)(1+M)+y A(0)(1+R) \\
= & {\left[\frac{H^{u}-y A(0)(1+R)}{S(0)(1+u)}\right] S(0)(1+M) } \\
& +y^{A(0)(1+R)} \\
= & H^{u} \frac{S(0)(1+M)}{S(0)(1+u)} \cdot y \frac{S(0)(1+M) A(0)(1+R)}{S(0)(1+u)} \\
& +y A(0)(1+R) \\
= & H^{u} \frac{(1+M)}{(1+u)}+y A(0)(1+R)[1 \\
& \left.-\frac{(1+m)}{(1+u)}\right]
\end{aligned}
$$

$$
\begin{aligned}
= & H^{u} \frac{(1+M)}{(1+U)}+Y A(0)(1+R)\left[\frac{1+U-1-M}{(1+U)}\right] \\
= & H^{u} \frac{(1+M)}{(1+U)}+Y A(0)(1+R) \frac{(U-M)}{(1+U)} \\
\Rightarrow y= & {\left[H^{M}-H^{u} \frac{(1+M)}{(1+U)}\right] \frac{(1+U)}{A(O)(1+R)(U-M)} } \\
= & \frac{1}{(1+U)}\left[(1+U) H^{M}-(1+M) H^{u}\right] \\
& \frac{(T+U)}{A(O X(1+R)(U-M)} \\
= & \frac{1}{A(O Y(1+R)(U-M)}\left[(1+U) H^{M}-(1+M) H^{u}\right]
\end{aligned}
$$

Returning to the expression for $x$ gives

$$
x=\frac{H^{u}-y A(\Delta)(1+R)}{s(\Delta)(1+u)}
$$

$$
\begin{aligned}
& =\frac{H^{u}}{s(0)(1+u)}-Y \frac{A(0)(1+R)}{s(0)(1+u)} \\
& =\frac{H^{u}}{s(0)(1+u)}-\frac{A(0)(1+R)}{s(0)(1+u)}\{ \\
& \left.\frac{1}{A(0)(1+R)(u-M)}\left[(1+u) H^{M}-(1+M) H^{u}\right]\right\} \\
& =\frac{H^{u}}{s(0)(1+u)}-\frac{\left[(1+u) H^{M}-(1+M) H^{u}\right]}{s(0)(1+u)(u-M)} \\
& =\frac{1}{s(0)(1+u)}\left[H^{u}-\frac{(1+u) H^{M}}{(u-M)}+\frac{(1+M) H^{u}}{(u-M)}\right] \\
& =\frac{1}{s(0)(1+u)(u-M)}\left[H^{u}(u-M)-(1+u) H^{M}\right. \\
& \left.+(1+M) H^{u}\right] \\
& =\frac{1}{s(0)(1+u)(u-M)}\left[H^{u}(u-M+1+M)\right. \\
& \left.-(1+u) H^{M}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{s(0)(1+u)(u-M)}\left[H^{u}(1+u)-(1+u) H^{m}\right] \\
& =\frac{(1+u)}{s(0)(1+u)(u-M)}\left(H^{u}-H^{m}\right) \\
& =\frac{H^{u}-H^{m}}{s(0)(u-M)}
\end{aligned}
$$

## Thus

$$
x=\frac{H^{u}-H^{M}}{S(O)(u-M)}
$$

$$
y=\frac{1}{A(O)(1+R)(u-M)}\left[(1+u) H^{M}-(1+M) H^{u}\right]
$$

substituting this result into the thirds equation gives

$$
H^{d}=x \operatorname{scos}(1+D)+y A(0)(1+R)
$$

$$
\begin{aligned}
= & S(O)(1+D)\left[\frac{H^{u}-H^{m}}{S(D)(u-M)}\right] \\
& +\frac{A(D)(1+R)}{A(\bar{D}(1+R)(u-M)}\left[(1+u) H^{m}-(1+M) H^{u}\right] \\
= & \frac{(1+D)}{(u-M)}\left(H^{u}-H^{m}\right)+\frac{(1+u) H^{m}-(1+M) H^{u}}{(u-M)} \\
= & \frac{1}{u-M}\left[(1+D)\left(H^{u}-H^{m}\right)+(1+u) H^{m}\right. \\
& \left.-(1+M) H^{u}\right] \\
= & \frac{1}{u-M}\left[(1+D) H^{u}-(1+D) H^{m}+(1+u) H^{m}\right. \\
= & \frac{1}{u-M}\left[H^{u}(1+M) H^{u}\right] \\
= & \frac{1}{u-M}\left[H^{u}(D-M)+H^{m}(u-D)\right]
\end{aligned}
$$

$$
\begin{aligned}
& \Rightarrow(U-M) H^{d}=(D-M) H^{u}+(U-D) H^{M} \\
& \Rightarrow(U-M) H^{d}+(M-D) H^{u}-(U-D) H^{M}=0
\end{aligned}
$$

## No-Arbitrage Interval

Since replication of $U_{x y}(1)=H(1)$ is not always possible in general modifications are made.
A portfolio super replicates the derivative security with payoff H(1) if

$$
U_{x y}(1) \geqslant H(1)
$$

An investor holding this portolio is protected against the option payoff since it is possible to cover the payoff with the portfolio.
The super-replictsion option price, itsup, is the minimal initial value of of a super-replicating portfolid,

$$
H^{\text {sup }}=\inf _{x y \in \mathbb{R}}\left\{U_{x y}(0): U_{x y}(1)>H(1)\right\}
$$

A portfolio sub-replicates a derivative security/with payoff
H(1) if

$$
H(1) \geqslant U_{x y}(1)
$$

and it is given by
$H^{\text {sub }}=\sup _{x y \in \mathbb{R}}\left\{U_{x y}(0): U_{x y}(1) \leqslant H(1)\right\}$
Thus the sub-replicating option price $H^{\text {sub }}$ is the maximum intral value of a sub-replicating portfolio.

## Exercise

Consider the parameters

$$
\begin{array}{ll}
S(0)=30, & A(0)=1,
\end{array} u=2090
$$

with pay off

$$
H(1)=(5(1)-32)^{+}
$$

Find the super-replication price. Solution

The super-replication price of a derivative security is defined by

$$
H^{\sup }=\inf _{x y \in \mathbb{R}^{2}}\left\{U_{x y}(0): U_{x y}(1) \geqslant H(1)\right\}
$$

where

$$
\begin{aligned}
U_{x y}(0) & =x s(0)+y A(0) \\
U_{x y}(1)= & \left\{\begin{array}{l}
x s^{u}+y A(0)(1+R) \geqslant H^{u} \\
x s^{m}+y A(0)(1+R) \geqslant H^{m} \\
x s^{d}+y A(0)(1+R) \geqslant H^{d}
\end{array}\right.
\end{aligned}
$$

low adding numbers

$$
\begin{aligned}
& s^{u}=s(0)(1+u)=(30)(1+0.2)=36 \\
& s^{m}=s(0)(1+m)=(30)(1+0.1)=33
\end{aligned}
$$

$$
s^{d}=s(0)(1+D)=(30)(1-0.1)=27
$$

Now the payoff is given by

$$
H(1)=(5(1)-32)^{+}
$$

so

$$
\begin{aligned}
H^{u} & =\left(s^{u}-32\right)^{+} \\
& =\max \left(s^{u}-32,0\right) \\
& =\max (4,0) \\
& =4 \\
H^{m} & =\left(s^{m}-32\right)^{+} \\
& =\max \left(s^{m}-32,0\right) \\
& =\max (1,0) \\
& =1 \\
H^{d} & =\left(s^{d}-32\right)^{+} \\
& =\max \left(s^{d}-32\right)^{+} \\
& =\max (-5,0)
\end{aligned}
$$

$$
=0
$$

thus

$$
H(1)= \begin{cases}4 & s(1)=s^{n} \\ 1 & s(1)=s^{m} \\ 0 & s(1)=s^{d}\end{cases}
$$

Plugging numbers in gives

$$
\begin{aligned}
U_{x y}(0) & =30 x+y \\
U_{x y}(1)= & \left\{\begin{array}{l}
36 x+1.05 y \geqslant 4 \\
33 x+1.05 y \geqslant 1 \\
27 x+1.05 y \geqslant 0
\end{array}\right.
\end{aligned}
$$

The problem to be solved is minimizing $U_{x y}(0)$ subject to the constraints on $x$ and $y$ specified by $U_{x y}(D)$. This is a linear programing problem that will be solved numerically.

## The python linear programming

library putp was used.

## unfortunately the problem

as stated has no solution.
Below is a listing of the code used
import pulp

```
model = pulp.LpProblem(name="super-replicating- portfolio", sense=pulp.LpMinimize)
$\mathrm{x}=\mathrm{pulp}$. LpVariable(name=" x ", lowBound = 0.0)
$\mathrm{y}=$ pulp.LpVariable(name=" y ", upBound = 0.0)
```

```
# Constraints
model += (36 * x + 1.05 * y >= 4, "up_constraint")
model += (33 * x + 1.05 * y >= 1, "mid_constraint")
model += (27 * x + 1.05 * y >= 0, "down_constraint")
# Objective Function
model += pulp.lpSum([30 * x, y])
status = model.solve()
```


## The solution is

$$
\begin{aligned}
& \text { status: 1, Optimal } \\
& \text { objective: } 1.9047622000000004 \\
& \text { x: } 0.44444444 \\
& \text { y: }-11.428571 \\
& \text { up_constraint: } 2.8999999912571184 \mathrm{e}-07 \\
& \text { mid_constraint: } 1.6666669699999996 \\
& \text { down_constraint: } 3.3000000065896984 \mathrm{e}-07
\end{aligned}
$$

Note that the constraint value is is the difference between the value of the constraint and the specified bound.

The solution given in the text is not the same

$$
\begin{gathered}
x=0.1135388 \quad y=-00832358 \\
U_{x y}(0)=3.3229286
\end{gathered}
$$

To get a third opmion the online solver was tried,
https://online-optimizer.appspot.com
The solution obtained is

$$
\begin{array}{cl}
x=0.4444 & y=-11.4285714 \\
U_{x y}(0) & =1,90476
\end{array}
$$

which is the same as dotained using pulp. It seems that the solution in the book is incorrect.

The Peasability region is shown below
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-149.jpg?height=680&width=802&top_left_y=133&top_left_x=390)

Similarly the sub-replicating portfolio is found by maximizons

$$
U_{x y}(0)=30 x+y
$$

subject to the constraint

$$
U_{x y}(1) \leqslant H(1)
$$

This gives the linear progonning problem

$$
\begin{gathered}
U_{x y}(0)=30 x+y \\
U_{x y}(1)=\left\{\begin{array}{l}
36 x+1.05 y \leqslant 4 \\
33 x+1.05 y \leqslant 1 \\
27 x+1.05 y \leqslant 0
\end{array}\right.
\end{gathered}
$$

```
The putp solution is given
by
import pulp
model = pulp.LpProblem(name="sub-replicating-
portfolio", sense=pulp.LpMaximize)
$\mathrm{x}=$ pulp.LpVariable(name="x", lowBound = 0.0)
$y=$ pulp.LpVariable(name=" $y$ ", upBound = 0.0)
\# Constraints
model += (36 * x + 1.05 * y <= 4, "up_constraint")
model += (33 * $\mathrm{x}+1.05 * \mathrm{y}<=1$, "mid_constraint")
model += (27 * $\mathrm{x}+1.05 * \mathrm{y}<=0$, "down_constraint")
\# Objective Function
model += pulp.lpSum([30 * x, y])
status = model.solve()
```

The solution is given by

```
status: 1, Optimal
objective: 0.714285799999999
x: 0.16666667
y: -4.2857143
up_constraint: -2.499999895000001
mid constraint: 9.499999897855105e-08
down_constraint: 7.499999910010047e-08
```

All constraints are satisfied.

This diffors from the solution given in the text which is

$$
\begin{gathered}
x=0.522876 \quad y=-14.117649 \\
v(0)=1.568628
\end{gathered}
$$

This solution is compared with the online solver,
https://online-optimizer.appspot.com
The solution is the same as obtained with pulp

$$
\begin{gathered}
x=0.166667 \quad y^{=-4.2857143} \\
v_{x y}(0)=0.2142
\end{gathered}
$$

and the feastble region is shown below
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-152.jpg?height=758&width=812&top_left_y=363&top_left_x=343)

It looks like text book answere is incorrect.

Thus in swmmary the superreplicating portfolio value is. given by

$$
H^{\text {super }}=1.90472
$$

and the sub-replicating portablio
value by

$$
H^{\text {sub }}=0.7143
$$

Thus the derivative security price H(0) satisfies

$$
0.7143 \leqslant H(0) \leqslant 1.90472
$$

In general it will be true that

$$
H^{\text {sub }} \leqslant H^{\text {super }}
$$

It follows that an interval of possible values of $H(0)$ is possible

$$
H^{\text {sub }} \leqslant H(0) \leqslant H^{\text {super }}
$$

The open interval $\left(H^{\text {sub }}, H^{\text {super }}\right)$ is called the no-arbitrage interval. This is justified by the following proof.

## Theorem

If $a \in\left(H^{\text {sub }}, H^{\text {super }}\right)$ then taking $H(0)=a$ does not lead to an arbitrage opportunity.

## Proof

Consider the portfolio $(x, y, z)$, where

$$
U_{x y z}(0)=x S(0)+y A(0)+z H(0)
$$

and assume there is an arbitrage such that,

$$
U_{x y z}(0)=x S(0)+y A(0)+z H(0)=0
$$

and

$$
U_{x y z}(1) \geqslant 0
$$

First asscone that $z>0$ then

$$
v_{x y z}(0)=0=x S(0)+y A(0)+z H(0)
$$

$$
\begin{aligned}
\Rightarrow H(0) & =-\frac{x}{2} S(0)-\frac{y}{2} A(0) \\
& =U_{\left(-\frac{x}{2},-\frac{y}{2}\right)}(0)
\end{aligned}
$$

From the no-arbitrage assumption

$$
\begin{aligned}
U_{x y 2}(1) & \geqslant 0 \\
\Rightarrow \quad x S(1) & +y A(1)+z H(1) \geqslant 0 \\
\Rightarrow \quad H(1) & \geqslant-\frac{x}{2} S(1)-\frac{y}{2} A(1) \\
& =U\left(-\frac{x}{2},-\frac{y}{2}\right)(1)
\end{aligned}
$$

Thus $U_{\left(-\frac{x}{2},-\frac{x}{2}\right)}(1)$ sub-replicates H(1). Recall that

$$
H^{\operatorname{sub}}=\sup \left\{U_{\left(-\frac{x}{2},-\frac{x}{2}\right)}(0) ; U_{\left(-\frac{x}{2},-\frac{x}{2}\right)}(1) \leqslant H(1)\right\}
$$

It follows that

$$
H^{s u b} \geqslant U_{\left(-\frac{x}{2},-\frac{y}{2}\right)}(0)
$$

Now it is assumed that

$$
a \in\left(H^{\text {sub }}, H^{\text {super }}\right)
$$

and $H(0)=a$ then

$$
H^{s u b}<H(0)<H^{s u p e r}
$$

It follows that

$$
U_{\left(-\frac{x}{2},-\frac{1}{2}\right)}(0) \leqslant H^{s u b}<H(0)
$$

This relation implies that

$$
\begin{aligned}
0 & <H(0)-U_{\left(-\frac{1}{2},-\frac{y}{2}\right)}(0) \\
& =U_{x y z}(0)
\end{aligned}
$$

and contradicts the assumption that

$$
U_{x y z}(0)=0
$$

similarly if $z<0$ then

$$
\begin{aligned}
U_{x y z}(0) & =0=x S(0)+y A(0)+z H(0) \\
\Rightarrow & 2 H(0)=-x S(0)-y A(0) \\
\Rightarrow & H(0)=\frac{x}{|2|} S(0)+\frac{y}{|2|} A(0)
\end{aligned}
$$

and

$$
\begin{aligned}
U_{x y z}(1) & \geqslant 0 \\
\Rightarrow \quad x S(1) & +y A(1)+z H(1) \geqslant 0 \\
\Rightarrow \quad 2 H(1) & \geqslant x S(1)+y A(1) \\
\Rightarrow \quad H(1) & \leqslant \frac{x}{|z|} S(1)+\frac{y}{|z|} A(1) \\
& =U_{\left(\frac{x}{|z|}, \frac{y}{|2|}\right)}(1)
\end{aligned}
$$

since $2<0$. It follows that $U_{\left(\frac{x}{12}, \frac{y}{12}\right)}(1)$ super replicates $H(1)$.
but

$$
H^{\text {super }}=\inf \left\{U_{\left(\frac{x}{12}, \frac{y}{12},\right)}(0): U_{\left(\frac{x}{12}, \frac{y}{12},\right)}(1) \geqslant H(1)\right\}
$$

it follows that

$$
H^{\text {super }} \leqslant U_{\left(\frac{x}{|2|}, \frac{y}{|2|}\right)}(0)
$$

Now if $a \in\left(H^{\text {sub }}, H^{\text {super }}\right)$ and $H(0)=a$ then

$$
\begin{aligned}
& H(0)<H^{\text {supper }} \leqslant U_{\left(\frac{x}{121}, \frac{y}{12}\right)}(0) \\
\Rightarrow & U_{\left(\frac{x}{21}, \frac{y}{121}\right)}(0)-H(0) \geqslant 0 \\
\Rightarrow & \frac{x}{121} S(0)+\frac{y}{121} A(0)-H(0) \geqslant 0
\end{aligned}
$$

since $z<0$ it follows

$$
\begin{aligned}
& x S(0)+y A(0)+-|z| H(0) \geqslant 0 \\
\Rightarrow & x S(0)+y A(0)+z H(0) \geqslant 0
\end{aligned}
$$

This contradicts the no-arbitrage assumption. It follows that if

$$
H(O) \in\left(H^{\text {sub }}, H^{\text {super }}\right)
$$

the no-arbitrage is possible.

## Risk-Nentral Probabilities

Recall that for a risk-neutral probability distribution, $Q=\left(q_{u}, q_{m}, q_{d}\right)$

$$
E_{Q}[S(1)]=S(0)(1+R)
$$

where $R$ is the risk-free return and $S$ is an asset price. Now since

$$
k=\frac{S(1)-S(0)}{S(0)}
$$

it follows that

$$
\begin{aligned}
& E_{Q}[k]=E_{Q}\left[\frac{s(1)-s(0)}{s(0)}\right] \\
& =\frac{1}{s(0)} E_{Q}[s(1)]-1 \\
& =\frac{1}{s(0)} s(0)(1+R)-1
\end{aligned}
$$

$$
=R
$$

## Trus

$$
E_{Q}[K]=R
$$

using this relation it follows that

$$
E_{Q}[K]=q_{u} u+q_{m} M+q_{d} D=R
$$

where

$$
q_{u}+q_{m}+q_{d}=1
$$

Since there are two equations with three wh knowns there is no single wrique solution.

## Excercise

Given a trinomial single-stock model with,

$$
R=109 \quad s(0)=10 \quad s^{u}=20 \quad s^{m}=15 \quad s^{c}=7.5
$$

find all risk neutral probabilities Solution

Now

$$
\begin{aligned}
& E_{Q}[S(1)]=S(0)(1+R) \\
\Rightarrow \quad & q_{u} S^{u}+q_{m} S^{m}+q_{d} S^{d}=S(0)(1+R)
\end{aligned}
$$

and

$$
q_{u}+q_{m}+q_{d}=1
$$

Plugging in the numbers gives

$$
\begin{aligned}
& 20 q_{u}+15 q_{m}+7.5 q_{d}=10(1+0.10) \\
\Rightarrow & 20 q_{u}+15 q_{m}+7.5 q_{d}=11
\end{aligned}
$$

using the second equation

$$
\begin{aligned}
& q_{u}+q_{m}+q_{c}=1 \\
\Rightarrow \quad & q_{d}=1-q_{u}-q_{m}
\end{aligned}
$$

50

$$
\begin{aligned}
& 20 q_{u}+15 q_{m}+\frac{15}{2}\left(1-q_{u}-q_{m}\right)=11 \\
\Rightarrow & 20 q_{u}-\frac{15}{2} q_{u}+15 q_{m}-\frac{15}{2} q_{m}=11-\frac{15}{2} \\
\Rightarrow & q_{u}(20-15 / 2)+q_{m}(15-15 / 2)=\frac{22-15}{2} \\
\Rightarrow & q_{u}\left(\frac{40-15}{2}+q_{m} \frac{(30-15)}{2}=\frac{7}{2}\right. \\
\Rightarrow & 25 q_{u}+15 q_{m}=7 \\
\Rightarrow & q_{m}=\frac{1}{15}\left(7-25 q_{u}\right) \\
= & \frac{7}{15}-\frac{5}{3} q_{u}
\end{aligned}
$$

since the $g^{\prime}$ s are probabilities it must be that

$$
0 \leqslant q_{u} \leqslant 1 \quad 0 \leqslant q_{m} \leqslant 1 \quad 0 \leqslant q_{d} \leqslant 1
$$

using the 9 m relation gives

$$
\begin{aligned}
& 0 \leqslant \frac{7}{15}-\frac{5}{3} q_{u} \leqslant 1 \\
\Rightarrow & -\frac{7}{15} \leqslant-\frac{5}{3} q_{u} \leqslant \frac{8}{15} \\
\Rightarrow & -\left(\frac{7}{15}\right)\left(-\frac{3}{5}\right) \geqslant 9 u \geqslant\left(\frac{8}{15}\right)\left(-\frac{3}{5}\right) \\
\Rightarrow & \frac{7}{25} \geqslant 9 u \geqslant-\frac{8}{25} \\
\Rightarrow & \frac{7}{25} \geqslant 9 u \geqslant 0 \\
\Rightarrow & 0 \leqslant 9 u \leqslant \frac{7}{25}
\end{aligned}
$$

It follows that

$$
0 \leq G_{m} \leq \frac{7}{15}
$$

and since

$$
c_{d d}=1-q_{u}-q_{m}
$$

The max value of $9 d$ will occur when $q_{u}=q_{m}=0$ and the min value when both $q_{u}$ and $q_{m}$ are maximum. So

$$
\begin{aligned}
& 1-\frac{7}{15}-\frac{1}{25} \leqslant 9 d \leqslant 1 \\
\Rightarrow & \frac{1}{5}\left(5-\frac{7}{3}-\frac{7}{5}\right) \leqslant 9 d \leqslant 1 \\
\Rightarrow & \frac{1}{5}\left[\frac{(5)(15)}{15}-\frac{35}{15}-\frac{21}{15}\right] \leqslant 9 d \leqslant 1 \\
\Rightarrow & \frac{1}{5}\left[\frac{75}{15}-\frac{35}{15}-\frac{21}{15}\right] \leqslant 9 d \leqslant 1 \\
\Rightarrow & \frac{19}{(5 \times 15)} \leqslant 9 d \leqslant 1 \\
\Rightarrow & \frac{19}{75} \leqslant 9 d \leqslant 1
\end{aligned}
$$

Thus the risk-neutral probabilities for a trinomial single asset mode with the given parameters must satisfy

$$
0 \leqslant q_{n} \leqslant \frac{7}{25} \quad 0 \leqslant q_{m} \leqslant \frac{7}{15}
$$

$$
\frac{19}{75} \leq 9 d \leq 1
$$

## Theorem

If no arbitrage is possible in a trinomial model then a risk-neutral probability distribution, Q, exists such that

$$
S(0)=E_{Q}[\tilde{S}(1)]
$$

## Proof

To prove the theorem a single $Q$ must be shown to exist.

Recall that previously it was shown that for the trimomial model that no-arbtrage implies trat

$$
\begin{aligned}
& \Rightarrow \quad D<R<U \\
& \Rightarrow \quad S(0) D<S(0) R<S(0) U \\
& \Rightarrow S(0)(1+D)<S(0)(1+R)<S(0)(1+U) \\
& \Rightarrow \quad S^{d}<S(0)(1+R)<S^{u} \\
& \Rightarrow \quad \frac{S^{d}}{1+R}<S(0)<\frac{S^{u}}{1+R} \\
& \Rightarrow \quad \tilde{S}^{d}<S(0)<\tilde{S}^{u}
\end{aligned}
$$

Now since it is assumed that

$$
\begin{aligned}
& s^{d}<s^{m}<s^{u} \\
\Rightarrow \quad & \tilde{\delta}^{d}<\tilde{s}^{m}<\tilde{s}^{u}
\end{aligned}
$$

it must be that erther $s(0)<\tilde{s}^{m}$ or $s(0) \geqslant \tilde{s}^{m}$

If $s(0)<\tilde{s}^{m}$ assume that

$$
A=\frac{1}{2}\left(\tilde{S}^{m}+\tilde{S}^{u}\right) \quad B=\tilde{S}^{d}
$$

it follows that

$$
B<\delta(0)<A
$$

and if $s(0) \geqslant \tilde{s}^{m}$ let

$$
A=\tilde{s}^{u} \quad B=\frac{1}{2}\left(\tilde{s}^{m}+\tilde{s}^{d}\right)
$$

it follows that

$$
B<s(0)<A
$$

Now since $s(0)$ lies between $A$ and $B$ it follows that there is a $C \in(0,1)$ such that

$$
S(0)=C A+(1-C) B
$$

substituting the values of $A$ and $B$ into the first equation gives

$$
S(0)=\frac{c}{2}\left(\tilde{S}^{m}+\tilde{J}^{u}\right)+(1-c) \tilde{S}^{d}
$$

$$
=\frac{c}{2} \tilde{s}^{n}+\frac{c}{2} \tilde{s}^{m}+(1-c) \tilde{s}^{d}
$$

letting $q_{u}=q_{m}=\frac{c}{2} \quad q_{d}=(1-c)$ gives

$$
\begin{aligned}
s(0) & =q_{u} \tilde{s}^{u}+q_{m} \tilde{s}^{m}+q_{d} \tilde{s}^{d} \\
& =E_{Q}[\tilde{s}(1)]
\end{aligned}
$$

similarly for the second equation

$$
\begin{aligned}
s(0) & =(1-c) \tilde{s}^{u}+\frac{c}{2}\left(\tilde{s}^{m}+\tilde{s}^{d}\right) \\
& =(1-c) \tilde{s}^{u}+\frac{c}{2} \tilde{s}^{m}+\frac{c}{2} \tilde{s}^{d}
\end{aligned}
$$

let

$$
q_{u}=1-c \quad q_{m}=q_{d}=\frac{c}{2}
$$

then

$$
S(0)=E_{Q}[S(1)]
$$

Thus it has been shown that if there is no-arbitrage a risk-neutral distribution can

## be found.

Since there is no conique risk-neutral distribution to compute a price for a derivative security multiple prices exist. This leads to the definition of a price range which consists of the prices computed for each of the risk-nentral distributions.

Recall that the price of a derivative security is discounted expectation of the future price with respect to the risk-neetral probability, namely,

$$
H(0)=(1+R)^{-1} E_{Q}[H(1)]
$$

The range of derivative security prices is defined by

$$
I=\left\{(1+R)^{-1} E_{Q}[H(1)]: E_{Q}[K]=R\right\}
$$

where the expectations are coaluated for all risk-neutral probabilities. This interval is also called the no-arbitrage interval.

## Theorem

Each number in the interval I is a price of the derivative security $A$ consistent with the no-arbitrage princule.

## Proof

Let $a \in I$ so that $H(0)=a$ wrth

$$
H(0)=(1+R)^{-1} E_{Q}[H(1)]
$$

for some risk-neutral probility distribution $Q$. Consider a portfolio ( $x, y, z$ ) in the exterded market, recall that in the
extended maket no opportunities for arbitrage exist, let

$$
U_{x y z}(0)=x s(0)+y A(0)+z(t(0)
$$

Assume that an arbitrage exists for the portfolio $(x, y, z)$

$$
\begin{aligned}
& U_{x / 2}(0)=0 \\
& U_{x y 2}(1) \geqslant 0
\end{aligned}
$$

The expection of the discounted portfolio value with respect to a risk-nentral distribution ts given by

$$
\begin{aligned}
E_{Q} & {\left[(1+R)^{-1} U_{x y 2}(1)\right]=E_{Q}\left[(1+R)^{-1}(x S(1)\right.} \\
& +y A(0 x(1+R)+2 H(1)] \\
= & x E_{Q}\left[(1+R)^{-1} S(1)\right]+y A(0) \\
& +2 E_{Q}\left[(1+R)^{-1} H(1)\right]
\end{aligned}
$$

but

$$
\begin{aligned}
& S(0)=E_{Q}\left[(1+R)^{-1} S(1)\right] \\
& H(0)=E_{Q}\left[(1+R)^{-1} H(1)\right]
\end{aligned}
$$

80

$$
\begin{aligned}
E_{Q}\left[(1+R)^{-1} U_{x y z}(1)\right] & =x S(0)+y A(0)+2 t(0) \\
& =U_{x y z}(0) \\
& =0
\end{aligned}
$$

but it was assumed that

$$
U_{x y z}(1) \geqslant 0
$$

Since $E_{Q}\left[(1+R)-1 U_{x_{y z}}(1)\right]=0$ it follows that

$$
U_{x_{1 / 2}}(1)=0
$$

since if the expectation of a positive random variable is zero the random variable is zero everywhere. It follows trat there is no-arbitrage since if there were

$$
E_{a}\left[(1+R)^{-1} U_{x_{y 2}}(1)\right]>0
$$

## Theorem

Let $H$ be a European dericative security in the single asset single-period trinomial market moder. Assume that,

$$
H^{\text {sub }}<H^{\text {super }}
$$

then

$$
I=\left(H^{\text {sub }}, H^{\text {super }}\right)
$$

## Proof

First it will be shown that $I$ is contained [ $H$ sub, $H$ super]. Assume that the portfolio $(x, y)$ is sub-replicating

$$
\begin{aligned}
U_{x y}(1) & \leqslant H(1) \\
\Rightarrow \quad & x S(1)+y A(0)(1+R) \leqslant H(1)
\end{aligned}
$$

Let $Q$ be any risk-neutral distribution. Then

$$
\begin{aligned}
& E_{Q}[x S(1)+y A(O)(1+R)] \leqslant E_{Q}[H(1)] \\
\Rightarrow & x E_{Q}[S(1)]+y A(O)(1+R) \leqslant E_{Q}[H(O)]
\end{aligned}
$$

From the martingale property of the risk-neutral distribution

$$
\begin{array}{lc} 
& E_{Q}[S(1)]=(1+R) S(0) \\
s o & x(1+R) S(0)+y A(0)(1+R) \leqslant E_{Q}[H(1)] \\
\Rightarrow & x S(0)+y A(0) \leqslant(1+R)^{-1} E_{Q}[H(1)]
\end{array}
$$

Get the largest lower bound by taking the supremum over all possible portfolios

$$
\sup [x \operatorname{s}(0)+y A(0)] \leqslant(1+R)^{-1} E_{Q}[H(0]
$$

but

$$
H^{S \omega b}=\sup [x S(0)+y A(0)]
$$

thus

$$
H^{s u b} \leqslant(1+R)^{-1} E_{Q}[H(1)]
$$

Next consider the case of a super-replicating portfolio

$$
x S(1)+y A(0) x(+R) \geqslant H(1)
$$

Taking expectation with respect to 8 gives

$$
x E_{Q}[S(1)]+y A \operatorname{CO}(1+R) \geqslant E_{Q}[H(C)]
$$

$\Rightarrow x(1+R) s(0)+y A \cos (1+R) \geqslant E_{Q}[H(0)]$
$\Rightarrow x S(0)+y A(0) \geqslant(1+R)^{-1} E_{Q}[H(1)]$
The smallest upper bound is found by taking the infimum of all super-replicating portfolios

$$
\inf [x S(0)+y A(0)] \geqslant(1+R)^{-1} E_{Q}[H(1)]
$$

but

$$
H^{\text {super }}=\inf [x s(0)+y A(0)]
$$

thus

$$
H^{\text {super }} \geqslant(1+R)^{-1} E_{Q}[H(1)]
$$

It follows that

$$
(1+R)^{-1} E_{Q}[H(1)] \in\left[H^{\text {sub }}, H^{\text {super }}\right]
$$

but

$$
I=\left\{E_{Q}[\tilde{H}(0)]: E_{Q}[k]=R\right\}
$$

50

$$
I C\left[H^{\text {sub }}, H^{\text {super }}\right]
$$

To go furthure make the following notational change. Define the event space

$$
\Omega=\left\{\omega_{1}, \omega_{2}, \omega_{3}\right\}
$$

and define a set of points in $\mathbb{R}^{2}$ by considering the pair
$\xi\left(1, \omega_{i}\right)$ and $\tilde{H}\left(1, \omega_{i}\right)$ and denote the set by $A$,
$A=\left\{\left(\tilde{\zeta}\left(1, \omega_{i}\right), \tilde{H}\left(1, \omega_{i}\right)\right): i=1,2,3\right\} \subset \mathbb{R}^{2}$
A couple of more definitions are needed to go furtner

## Definition: Convex set

A set is convex in $\mathbb{R}^{2}$ if any two points in the set can be connected by a line segment that is also contained in the set. Below is an example of a convex set
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-178.jpg?height=555&width=770&top_left_y=1414&top_left_x=397)

Below is an example of a set that is not convex
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-179.jpg?height=557&width=769&top_left_y=364&top_left_x=358)

## Definition: Convex thall

The convex hull of a set is the smallest conver set that contains the set.

As an example consider the set of points in $\mathbb{R}^{2}$ defined by

$$
A=\left\{A_{1}, A_{2}, A_{3}\right\}
$$

The convex hull of $A$ is

## a triangle as shown in the following figure.

![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-180.jpg?height=525&width=779&top_left_y=364&top_left_x=457)

## Definition: Convex Combination

The convex combination of a set of points is a linear combination of points $x_{1}, x_{2}, x_{3}$, with coefficients $c_{1}, c_{2}, c_{3} \ldots$ that ore nonegative and sum to 1.

$$
C_{1}+C_{2}+C_{3}+\cdots=1
$$

where $c_{i} \geqslant 0$. As an example consider the three points in
$\mathbb{R}^{2}, x_{1}, x_{2}$ and $x_{3}$
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-181.jpg?height=1045&width=1163&top_left_y=284&top_left_x=282)

Intuitively for two points the convex combination will lie on the line segment conecting the points since it is the weighted average of the points. It can be shown that any convex combination of ports
will lie inside the coven hull containg the points.

Now back to problem, recall that the cuent space is given

$$
\Omega=\left(\omega_{1}, \omega_{2}, \omega_{3}\right)
$$

denoting the probabilities of of the $u, m$ and $d$ states.
Consider the set $A$ in $\mathbb{R}^{2}$ defined by the pair $\boldsymbol{S}\left(1, \omega_{i}\right)$ and $\tilde{H}\left(1, \omega_{i}\right)$, namely,
$A=\left\{\left(\tilde{S}\left(1, \omega_{i}\right), \tilde{H}\left(1, \omega_{i}\right)\right): i=1,2,3\right\}$
Let $C$ denole the convex null of $A$. The closed set $C$ will be ether a line segment or a triangle. This is because A consits
of three points. If they fall on a line segment $c$ will be a line if not $c$ will be a triangle. Below are examples.
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-183.jpg?height=457&width=779&top_left_y=604&top_left_x=340)
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-183.jpg?height=454&width=779&top_left_y=1116&top_left_x=340)

From the no-arbitrage principle it is known that

$$
D<R<U
$$

This relation implies that

$$
\begin{aligned}
& S(O)(1+D)<S(O)(1+R)<S(O)(1+U) \\
\Rightarrow & S(O) \frac{(1+D)}{(1+R)}<S(O)<S(O) \frac{(1+U)}{(1+R)} \\
\Rightarrow & S\left(1, \omega_{3}\right) \leqslant S(O) \leqslant \tilde{S}\left(1, \omega_{1}\right)
\end{aligned}
$$

Also in the trinomial model it is assumed that

$$
D<M<u
$$

This relation implies that

$$
\tilde{S}\left(1, \omega_{3}\right)<\tilde{S}\left(1, \omega_{2}\right)<\tilde{S}\left(1, \omega_{1}\right)
$$

It follows that $S(0)$ must iie between the extreme values of $\tilde{s}(1)$.
First if it is asswed that $C$ is a triangle then the
vertical line ( $S(0), 0$ ) will intersect $C$ at two points, denoted by $(s(0), a)$ and ( $s(0), b$ ) which form a non-emply segment this is illustrated in the following figure.
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-185.jpg?height=1091&width=1311&top_left_y=705&top_left_x=98)

Let int (c) denole the interior of the convex hull $c$. Then the line segment $(a, b)$ is defined by

$$
(a, b)=\{u:(s(0), u) \in \operatorname{int}(c)\}
$$

Now any $(s(0), u)$ contained in int (c) can be written as a convex combination of the points of $a$, so

$$
(s(0), u)=\sum_{i=1}^{3} C_{i}\left(\hat{s}\left(1, \omega_{i}\right), \tilde{H}\left(1, \omega_{i}\right)\right)
$$

where

$$
\sum_{i=1}^{3} c_{i}=1
$$

These coefficients define a risk-neutral probability. if

$$
q_{n}=c_{1} \quad q_{m}=c_{2} \quad q_{c}=c_{3}
$$

Then

$$
\begin{aligned}
& (s(0), u)=q_{u}\left(\tilde{S}\left(1, \omega_{u}\right), \tilde{H}\left(1, \omega_{u}\right)\right) \\
& +q_{m}\left(s\left(1, \omega_{m}\right), \tilde{H}\left(1, \omega_{m}\right)\right) \\
& +q_{d}\left(s\left(1, \omega_{d}\right), \tilde{H}\left(1, \omega_{d}\right)\right)
\end{aligned}
$$

equating components gives

$$
\begin{aligned}
s(0)= & q_{u} \tilde{s}\left(1, \omega_{u}\right)+q_{m} \tilde{s}\left(1, \omega_{m}\right) \\
& +q_{d} \tilde{s}\left(1, \omega_{d}\right) \\
& =E_{Q}[\tilde{s}(1)]
\end{aligned}
$$

and

$$
\begin{aligned}
u= & q_{u} \tilde{H}\left(1, \omega_{u}\right)+q_{m} \tilde{H}\left(1, \omega_{m}\right) \\
& +q_{d} \tilde{H}\left(1, \omega_{d}\right) \\
& =E_{Q}[\tilde{H}(1)]
\end{aligned}
$$

Recall that

$$
I=\left\{(1+R)^{-1} E_{Q}[H(1)]: E_{Q}[K]=R\right\}
$$

it follows that

$$
u \in I
$$

50

$$
(a, b) \subset I
$$

Now since

$$
\tilde{S}\left(1, \omega_{3}\right)<\tilde{S}\left(1, \omega_{2}\right)<\tilde{S}\left(1, \omega_{3}\right)
$$

It follows that the triangle has no vertical edges.
A possible triangle is shown below. Since there are no vertical edges there exisits a line $l$ with slope $x$ and intercept y $A(0)$ passing through $(s(0), 6)$. From the figure it is seen that the set $A=\left\{A_{1}, A_{2}, A_{3}\right\}$ lies bebow the line $l$, which forms one sole of the triangle
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-189.jpg?height=1083&width=1303&top_left_y=56&top_left_x=251)
formed $b_{y} \quad A_{i}=\left(\tilde{s}\left(1, \omega_{i}\right), \tilde{H}\left(1, \omega_{i}\right)\right)$ This is cllustrated in the diagram. It follows that

$$
\begin{aligned}
& \tilde{H}(1) \leqslant x \tilde{S}(1)+y A(0) \\
\Rightarrow & H(1) \leqslant x S(1)+y A(0)(1+R)
\end{aligned}
$$

thus the portfolio $(x, y)$ is super replicating,

$$
H^{\text {super }} \leqslant x S(1)+y A \cos (1+R)
$$

since the line passes through $(s(0), 6)$ it follows that

$$
b=x S(0)+y \geqslant H^{\text {super }}
$$

since $(a, b) \in I$ it follows that

$$
a=\inf \partial I
$$

There is another line, $m$, shown in the figure connecting $A_{1}$ and $A_{3}$ trat passes through ( $s(0), a$ ). If $m$ has slope $X^{\prime}$ and intercept $Y^{\prime} A(0)$. The set $A=\left\{A_{1}, A_{2}, A_{3}\right\}$ lies above the line, $m$. It follows trat

$$
\begin{aligned}
& \tilde{H}(1) \geqslant x^{\prime} \tilde{S}(1)+y^{\prime} A(O)(1+R) \\
\Rightarrow \quad & H(1) \geqslant x^{\prime} S(1)+y^{\prime} A(O)(1+R)
\end{aligned}
$$

Thus $\left(x^{\prime}, y^{\prime}\right)$ is a subrepicating portfolio.

$$
H^{s u b} \geqslant x^{\prime} S(1)+y^{\prime} A(0)(1+R)
$$

sonce the line passes through $(s(0), a)$ it follows that

$$
H^{\text {sub }} \geqslant x^{\prime} S(0)+y^{\prime} A(0)(1+R)=a
$$

It follows that since

$$
\begin{aligned}
& H^{\text {super }} \leqslant b \\
& H^{\text {sub }} \geqslant a
\end{aligned}
$$

that

$$
\left(H^{\text {sub }}, H^{\text {super }}\right) \subset(a, b)
$$

but it was previously shown triat

$$
(a, b) \subset I \subset\left[H^{\text {sub }}, H^{\text {super }}\right]
$$

trues

$$
I=\left(H^{\text {sub }}, H^{\text {super }}\right)
$$

Special Case $H^{\text {sub }}=H^{\text {super }}$

Here the special case of where the sub-replicating and super replicating portfolio prices are equal is discussed
It will be seen that this case reduces to the binomial model.

Exercise: Show that if $H^{\text {sub }}=H^{\text {super }}$ the a replicating portfolio exists.

## Solution

The sub-replicating and superreplicating portfolios are given

$$
\begin{aligned}
& H^{\text {sub }}=x^{\text {sub }} s(0)+y^{\text {sub }} A(0) \\
& H^{\text {super }}=x^{\text {super }} s(0)+y^{\text {supper }} A(0)
\end{aligned}
$$

since $H^{\text {sub }}=H^{\text {super }}$ it follows that

$$
\begin{aligned}
& x^{\text {sub }} s(0)+y^{\text {sub }} A(0) \\
= & x^{\text {super }} s(0)+y^{\text {super }} A(0) \\
\Rightarrow & \left(x^{\text {sub }}-x^{\text {super }}\right) s(0) \\
= & \left(y^{\text {super }}-y^{\text {sub }}\right) A(0)
\end{aligned}
$$

Now from the definion of the super and sub replicating portfolios

$$
\begin{aligned}
H^{\text {super }}= & \inf _{x y \in \mathbb{R}}\left\{U_{x y}(0): U_{x y}(1)>H(1)\right\} \\
H^{\text {sub }}= & \sup _{x y \in \mathbb{R}}\left\{U_{x y}(0): U_{x y}(1) \leqslant H(1)\right\}
\end{aligned}
$$

It follows that

$$
U_{x y}^{\text {super }}(1) \geqslant U_{x y}^{\text {sub }}(1)
$$

this relation implies the
following relations

$$
\begin{aligned}
x^{\text {super }} s^{u} & +y^{\text {super }} A(0)(1+R) \\
& \leqslant x^{\text {sub }} s^{u}+y^{\text {sub }} A(0)(1+R) \\
\Rightarrow \quad x^{\text {super }} & \text { sco) }(1+u)+y^{\text {super }} A(0)(1+R) \\
& \leqslant x^{\text {sub }} s(0)(1+u)+y^{\text {sub }} A(0)(1+R) \\
\Rightarrow \quad x^{\text {super }} & \text { s(ox) } \frac{(1+u)}{(1+R)}+y^{\text {super }} A(0) \\
\leqslant & x^{\text {sub }} \text { s(o) } \frac{(1+u)}{1+R}+y^{\text {sub }} A(0)
\end{aligned}
$$

similarly for the other outcomes

$$
\begin{aligned}
x^{\text {super }} & \operatorname{sco} \frac{(1+M)}{(1+R)}+y^{\text {super }} A(0) \\
& \leqslant x^{\text {sub }} \operatorname{scos} \frac{(1+M)}{(1+R)}+y^{\text {sub }} A(0)
\end{aligned}
$$

$$
\begin{aligned}
x^{\text {super }} & \leqslant(O) \frac{(1+D)}{(1+R)}+y^{\text {super }} A(O) \\
& \leqslant x^{\text {sub }} s(O) \frac{(1+D)}{1+R}+y^{\text {sub }} A(O)
\end{aligned}
$$

Now reconsider the first relation

$$
\begin{array}{r}
x^{\text {super }} \text { s(ox) } \frac{(1+u)}{(1+R)}+y^{\text {super }} A(0) \\
\leqslant x^{\text {sub }} \operatorname{s(ox)} \frac{(1+u)}{1+R}+y^{\text {sub }} A(0) \\
=>\frac{\text { s(o) }(1+u)}{(1+R)}\left(x^{\text {super }}-x^{\text {sub }}\right) \\
\leqslant A(0)\left(y^{\text {sub }}-y^{\text {super }}\right)
\end{array}
$$

but previously it was shown that

$$
A(0)\left(y^{\text {sub }}-y^{\text {super }}\right)=S(0)\left(x^{\text {super }}-x^{\text {sub }}\right)
$$

50
$\frac{\operatorname{sco}(1+a)}{(1+R)}\left(x^{\text {super }}-x^{\text {sub }}\right) \leqslant \sin \left(x^{\text {super }}-x^{\text {sub }}\right)$
$=\frac{(1+u)}{(1+R)}\left(x^{\text {super }}-x^{\text {sub }}\right) \leqslant\left(x^{\text {super }}-x^{\text {sub }}\right)$
similarly for the other outcomes

$$
\begin{aligned}
& \frac{(1+M)}{(1+R)}\left(x^{\text {super }}-x^{\text {sub }}\right) \leqslant\left(x^{\text {super }}-x^{\text {sub }}\right) \\
& \frac{(1+D)}{(1+R)}\left(x^{\text {super }}-x^{\text {sub }}\right) \leqslant\left(x^{\text {super }}-x^{\text {sub }}\right)
\end{aligned}
$$

If it is assumed that

$$
x^{\text {super }}-x^{\text {sub }} \neq 0
$$

then the series of inequalities is obtained

$$
\frac{(1+U)}{(1+R)} \leqslant 1 \quad \frac{(1+M)}{(1+R)} \leqslant 1
$$

$$
\frac{(1+D)}{(1+R)} \leqslant 1
$$

Recall that for no arbitrage to exist it must be that

$$
D<R<u
$$

The first and last relations give

$$
\begin{aligned}
& \frac{1+U}{1+R} \leqslant 1=D U \leqslant R \\
& \frac{1+D}{1+R} \leqslant 1 \Rightarrow D \leqslant R
\end{aligned}
$$

Thus to not have the possibility of arbitrage the assumtion that

$$
x^{\text {super }}-x^{\text {sub }}=0
$$

must be invalid, so

$$
x^{\text {super }}-x^{\text {sub }}=0
$$

$$
\begin{aligned}
& \Rightarrow x^{\text {super }}=x^{\text {sub }} \\
& \text { but } H^{\text {sub }}=H^{\text {super }} \text { implies } \\
& \left(x^{\text {sub }}-x^{\text {super }}\right) s(0) \\
& =\left(y^{\text {super }}-y^{\text {sub }}\right) A(0) \\
& \text { so it must also be that } \\
& y^{\text {super }}=y^{\text {sub }} \\
& \text { It follows that } H^{\text {sub }}=H^{\text {super }} \\
& \text { implies there is } a \text { single } \\
& \text { replicating portfolio }
\end{aligned}
$$

Exercise: show that a replication strategy is unique

## solution

Suppose that for the denuatie security, i.e claim, $H$ there are two replicating portfolios

$$
\left(x_{1}, y_{1}\right) \quad\left(x_{2}, y_{2}\right)
$$

To have a unique price for $H$ it must be that the intral values of the portfolios are equal, so

$$
\begin{aligned}
x_{1} s(0)+y_{1} A(0) & =x_{2} s(0)+y_{2} A(0) \\
\Rightarrow s(0)\left(x_{1}-y_{2}\right) & =\left(y_{2}-y_{2}\right) A(0)
\end{aligned}
$$

Additionaly the values at $t=l$ must be equal, so

$$
\begin{aligned}
& x_{1} s(1)+y_{1} A(1)=x_{2} s(1)+y_{2} A(1) \\
= & \left(x_{1}-y_{2}\right) s(1)=\left(y_{2}-y_{1}\right) A(1) \\
\Rightarrow & \left(x_{1}-x_{2}\right) s(1)=\left(y_{2}-y_{1}\right) A(0)(1+R)
\end{aligned}
$$

but from the intral relation

$$
A \cos \left(y_{2}-y_{1}\right)=\operatorname{sco} x\left(x_{1}-x_{2}\right)
$$

50

$$
\left(x_{1}-x_{2}\right) s(1)=\left(x_{1}-x_{2}\right) \operatorname{scos}(1+R)
$$

for this relation to be calid it must be that either

$$
x_{1}-x_{2}=0
$$

or

$$
\delta(1)=S(0)(1+R)
$$

If the second relation is true then $S(1)$ is not random but deterministic. It follows that the first relation is true so

$$
x_{1}=x_{2}
$$

but

$$
\operatorname{scol}\left(x_{1}-x_{2}\right)=\left(y_{1}-y_{2}\right) A(0)
$$

since $A(D)$ can be anything it must also be that

$$
y_{1}=y_{2}
$$

Thus the portdios are identical and the desired result follows, namely, a derivative security, or contigent claim, H, has a conique replicating portfolio.

Exercise : show that the existence of a replicating strategy implies uniqueness of the risk-neutral probability.

## Solution

Recall that a risk-nentral probability distribution, $Q$, has the properties

$$
\begin{aligned}
E_{Q}[K] & =R \\
E_{Q}[H(1)] & =H(0)(1+R)
\end{aligned}
$$

For the trinomial model the risk-neutoral probability is
given by $Q=\left(q_{u}, q_{m}, q_{d}\right)$ wher

$$
\begin{aligned}
& q_{u}+q_{m}+q_{d}=1 \\
\Rightarrow & q_{d}=1-q_{u}-q_{m}
\end{aligned}
$$

using this with the previous relations gives

$$
\begin{aligned}
& E_{Q}[K]=R \\
\Rightarrow & u_{q u}+M_{q m}+D\left(1-q_{u}-q_{m}\right)=R \\
\Rightarrow & u_{q u}-D q_{u}+M q_{m}-D q_{m}+D=R \\
\Rightarrow & q_{u}(u-D)+q_{m}(M-D)+D=R \\
\Rightarrow & q_{u}=\frac{R-D+(D-M) q_{m}}{u-D}
\end{aligned}
$$

Now for the second relation

$$
E_{Q}[H(1)]=(H R) H(0)
$$

$$
\begin{aligned}
=H & (1, u) q_{u}+H(1, m) q_{m} \\
& +H(1, d)\left(1-q_{u}-q_{m}\right)=(1+R) H(0)
\end{aligned}
$$

using

$$
q_{u}=\frac{R-D+(D-M) q_{m}}{u-D}
$$

50

$$
\begin{aligned}
& 1-q_{u}-q_{m}=1-\frac{R-D+(D-M)}{u-D} q_{m} \\
& -q_{m} \\
& =(u-D)^{-1}\left\{(u-D)-\left[R-D+(D-M) q_{m}\right]\right. \\
& \left.\quad-(u-D) q_{m}\right\}
\end{aligned}
$$

gives

$$
\begin{aligned}
& H(1, u)(u-D)^{-1}\left[R-D+(D-M) q_{m}\right] \\
& +H(1, m) q_{m}+H(1, d)(u-D)^{-1}\{(u-D)
\end{aligned}
$$

$$
\begin{aligned}
& {\left.\left[R-D+(D-M) G_{m}\right]-(u-D) G_{m}\right\} } \\
& =H(O)(1+R) \\
\Rightarrow & H(O)(1+R)(u-D)=H(1, u)(R-D) \\
& +H(1, u)(D-M) G_{m}+H(1, m) G_{m}(u-D) \\
& +H(1, d)(u-D)-H(1, d)(R-D) \\
& -H(1, d)(D-M) G_{m}-H(1, d)(u-D) G_{m} \\
\Rightarrow & H(O)(1+R)(u-D)-H(1, u)(R-D) \\
& -H(1, d)(u-D)-H(1, d)(R-D) \\
= & G_{m}[H(1, u)(D-M)+H(1, m)(u-D) \\
& -H(1, d)(D-M)-H(1, d)(u-D)] \\
\Rightarrow & H(D)(1+R)(u-D)-H(1, u)(R-D) \\
& -H(1, d)(u-D-R+D) \\
= & G m[H(1, u)(D-M)+H(1, m)(u-D) \\
& -H(1, d)(D-M+u-D)]
\end{aligned}
$$

$$
\begin{array}{rl}
=H & H(O)(1+R)(u-D)-H(1, u)(R-D) \\
& -H(1, d)(u-R) \\
=9 m & {[H(1, u)(D-m)+H(1, m)(u-D)} \\
& -H(1, d)(u-m)]
\end{array}
$$

Now Gm is undefined if left and righthand side terms are zero.

$$
\begin{gathered}
H(O)(1+R)(U-D)-H(1, U)(R-D) \\
-H(1, d)(U-R)=0
\end{gathered}
$$

and

$$
\begin{array}{r}
H(1, u)(D-m)+H(1, m)(u-D) \\
-H(1, d)(u-M)=0
\end{array}
$$

From the first equation

$$
H(O)(1+R)=H(1, u) \frac{(R-D)}{u-D}+H(1, d) \frac{(u-R)}{u-D}
$$

This is the binomial model derivative security price estimate ignoring the middle outcome, since

$$
q_{u}=\frac{R-D}{u-D} \quad q_{d}=\frac{u-R}{u-D}
$$

is the binomial risk-neutral distribution.

From the second equation

$$
\begin{aligned}
& H(1, u)(D-m)+H(1, m)(u-D) \\
& -H(1, d)(u-m)=0 \\
& \Rightarrow H(1, m)=H(1, d) \frac{(u-m)}{u-D}-H(1, u) \frac{(D-m)}{u-D} \\
& =H(1, d) \frac{(u-m)}{(u-D)}+H(1, u) \frac{(m-D)}{(u-D)}
\end{aligned}
$$

Thus $H(l, m)$ is a function of the other outcomes.

Thus if $H^{\text {sub }}=H^{\text {super }}$ the risk-neutral distribution is equivalent to the binomial case.
Similarly if $H^{\text {sub }}=H^{\text {super }}$ then the conver hull containing A is a line segment. This is illustrated in the following figure
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-207.jpg?height=920&width=1065&top_left_y=957&top_left_x=326)

It follows that $(3(1, m), H(1, m))$ is a convex combination of the other two parts. which is consistent with the result just obtalined.

## Replication with Two stocks

The trinamial model with one asset does not have a unique replicating portfolio, risk-neutral or derivatio security price. This problem was caused because the model has three equations and two variables.
An obvious change that will correct this problem is to add a second asset to the replications portfolio.
Consider a portfolio with two assets, $s_{1}$ and $s_{2}$, with returns $k_{1}$ and $k_{2}$ where

$$
\begin{array}{ll}
k_{1}^{u}=u_{1} & k_{2}^{u}=u_{2} \\
k_{1}^{m}=M_{1} & k_{2}^{m}=M_{2} \\
k_{1}^{D}=D_{1} & k_{2}^{D}=D_{2}
\end{array}
$$

and assuming the event space is given by

$$
\Omega=\{u, m, d\}
$$

It follows that the asset price is given by,

$$
\begin{aligned}
& S_{1}(1)=S_{1}(0)\left(1+K_{1}\right) \\
& S_{2}(1)=S_{2}(0)\left(1+K_{2}\right)
\end{aligned}
$$

The model for a replication portfolio, $\left(x_{1}, x_{2}, y\right)$, for the claim $H$,

$$
\begin{aligned}
& H^{u}=x_{1} S_{1}^{u}+x_{2} S_{2}^{u}+y A(O)(1+R) \\
& H^{m}=x_{1} S_{1}^{m}+x_{2} S_{2}^{m}+y A(O)(1+R) \\
& H^{d}=x_{1} S_{1}^{d}+x_{2} S_{2}^{d}+y A(O)(1+R)
\end{aligned}
$$

In matrix form this becomes

$$
H=A X
$$

where

$$
\begin{gathered}
H=\left(H^{u} H^{m} H^{d}\right)^{\prime} \\
x=\left(x, x_{2} y\right)^{\prime} \\
A=\left(\begin{array}{lll}
S_{1}^{u} & S_{2}^{u} & A(O)(1+R) \\
S_{1}^{m} & S_{2}^{m} & A(O)(1+R) \\
S_{1}^{d} & S_{2}^{d} & A(O)(1+R)
\end{array}\right)
\end{gathered}
$$

This model has either one or no solution. The price of the securty derioative is given by

$$
H(0)=x_{1} S_{1}(0)+x_{2} S_{2}(0)+y(1+R) A(0)
$$

Definition: Complet Market Model A market model is compliete if every random payoff of a contigent daim, $H(D)$, can be replicated.

The risk-neutral probability is defined by the three equations

$$
\begin{gathered}
E_{Q}\left[k_{1}\right]=R \quad E_{Q}\left[k_{2}\right]=R \\
q_{u}+q_{n}+q_{d}=1
\end{gathered}
$$

which explicitly are given by

$$
\begin{gathered}
q_{u} u_{1}+q_{m} m_{1}+q_{d} D_{1}=R \\
q_{u} u_{2}+q_{m} m_{2}+q_{d} D_{2}=R \\
q_{u}+q_{m}+q_{d}=1
\end{gathered}
$$

This model still has problems since if $s_{1}$ is the underlying asset of the derivative security $H$ how is $S_{2}$ choosen? Any choosen asset will gue a different price for the derivative security so there still is no unique price.

## Multi-Step Binomial Model

Here the single step binomial model is extended to an arbitrary number of steps. To get started a two step model is considered

## Two-step Example

The two-step binomial model assumes two timesteps. The time is denoted by

$$
t=0, T, \partial T
$$

or shortened to

$$
t=0,1,2
$$

The asset price at cach step is denoted by

$$
s(0), s(1), s(2)
$$

At each step the asset price
may go up or down. These changes are denoted by $u$ and d respectively.
Assume that the probability to go up is $P$. It follows that the probability to go down is $1-p$.

The event space is given by

$$
\Omega=\{u u, u d, d d, d u\}
$$

where un reprents going up on both stops, ad up and down, dd down on both steps and du down and up.
If the steps are assumed to be independent then the probability of each event is given by

$$
P(n u)=p^{2} \quad P(d d)=(1 p)^{2}
$$

$$
P(u d)=P(d u)=P(1-P)
$$

The returns are identified by step.

$$
k_{n}= \begin{cases}u & \text { with probability } P \\ D & \text { with probability } l-P\end{cases}
$$

it follows that

$$
\begin{aligned}
& K_{1}(u u)=K_{1}(u d)=u \\
& K_{1}(d u)=K_{1}(d d)=D \\
& K_{2}(u u)=K_{2}(d u)=u \\
& K_{2}(u d)=K_{2}(d d)=D
\end{aligned}
$$

The asset price at each step is denoted by

$$
\begin{aligned}
& s(1)=s(0)\left(1+K_{1}\right) \\
& s(2)=s(1)\left(1+K_{2}\right)=s(0)\left(1+K_{1}\right)\left(1+K_{2}\right)
\end{aligned}
$$

It follows that

$$
\begin{array}{r}
s(1)=\left\{\begin{array}{l}
s^{u}=s \cos (1+u) \\
s^{d}=s(0)(1+D)
\end{array}\right. \\
s(2)=\left\{\begin{array}{l}
s^{u k}=s(0)(1+u)^{2} \\
s^{u d}=s(0)(1+u)(1+D) \\
s^{d u}=s(0)(1+D)(1+u) \\
s^{d d}=s(0)(1+D)^{2}
\end{array}\right.
\end{array}
$$

The return on the risk-free asset at each time-step is denoted by

$$
A(n)=A(0)(1+R)^{n} \quad n=1,2
$$

## Self Funding Trading strategy

Consider the example

$$
\begin{array}{lll}
u=20 \% & D=-10 q_{0} & P=0.6 \\
s(0)=100 & A(0)=100 & R=5 \%
\end{array}
$$

Recall that in the previous section it was shown

$$
\begin{aligned}
& s(1)=\left\{\begin{array}{l}
s^{u}=s \operatorname{co}(1+u) \\
s^{d}=s(0)(1+D)
\end{array}\right. \\
& s(2)=\left\{\begin{array}{l}
s^{u u}=s(0)(1+u)^{2} \\
s^{u d}=s(0)(1+u)(1+D) \\
s^{d u}=s(0)(1+D)(1+u) \\
s^{d d}=s(0)(1+D)^{2}
\end{array}\right. \\
& A(n)=A(0)(1+R)^{n}
\end{aligned}
$$

Apply the Grample parameters gives

$$
\begin{aligned}
& s^{u}=s(0)(1+u)=(100)(1.2)=120 \\
& s^{c}=s(0)(1+0)=(100)(0.9)=90 \\
& s^{u u}=s(0)(1+u)^{2}=(100)(1.2)^{2}=144 \\
& \left.s^{d u}=s u d=s 10\right)(1+0)(1+u) \\
& =(100)(1.2)(0.9)=108 \\
& s^{d d}=s(0)(1+0)^{2}=(100)(0.9)^{2}=81 \\
& A(1)=(100)(1.05)=105 \\
& A(2)=(100)(1.05)^{2}=110.25
\end{aligned}
$$

The asset prices can be graphically reprented by the binary tree where the value on the edges gives the probability of transition to that state
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-218.jpg?height=536&width=638&top_left_y=1442&top_left_x=388)

At the second step where $s^{\text {nd }}=s^{d u}$ a concrete recombining is said to have taken place.

Furthur assume that an investor has 50 and desires to invest in the market by purchasing one share.

Also, the investor may change the portfolio after the first step so the amount of the asset owned at each step is denoted by $(x(1), y(1))$ and $(x(2), y(2))$
Now the intial portfolio value is given by

$$
\begin{aligned}
& U(0)=x(1) S(0)+y(1) A(0) \\
\Rightarrow & y(1)=\frac{U(0)-x(1) S(0)}{A(0)}
\end{aligned}
$$

low since the investor purchacses one share, $x(1)=1$, and wishes to invest $v(0)=50$. It follows that

$$
\begin{aligned}
y(1) & =\frac{50-(1)(100)}{100} \\
& =\frac{-50}{100}=-0.5
\end{aligned}
$$

Thus the investor borrows 50 to purchase one share at 100 . Thus the portfolio is given by,

$$
(x(1), y(1))=(1,-0.8)
$$

Case 1: The price gpes up on the first step.

$$
\begin{aligned}
U^{u} & =x(1) S(0)(1+u)+y(1) A(0)(1+R) \\
& =(1 \times 120)+(-0.5)(100)(1.05) \\
& =120.52 .5
\end{aligned}
$$

$$
=67.5
$$

At the next step the investor decides to decides to decrease the asset position to $x(2)=0.8$ and use the returns to payoff some of the loan so the new portfolio is given by

$$
\begin{aligned}
& 67.5=(0.8)(120)+y(2)(105) \\
& \Rightarrow \quad y(2)=\frac{67.5-96}{105} \\
& =-0.271
\end{aligned}
$$

The two possible outcomes are

$$
\begin{aligned}
v^{\text {un }} & =(0.8)(120)(1.2)-(0.271)(105)(1.05) \\
& =115.2-29.88 \\
& =85.32 \\
v^{\text {ud }} & =(0.8)(120)(0.8)-29.88 \\
& =86.4-29.88
\end{aligned}
$$

$$
=56.52
$$

Case 2: The price goes down on the first stop.

$$
\begin{aligned}
U^{C} & =(1)(90)-(0.5)(100)(1.05) \\
& =37.5
\end{aligned}
$$

In this case the invester borrows more money and buys more of the asset on the second step. If $x(1)=1.2$ it follows that

$$
\begin{aligned}
37.5= & (1.2)(90)+y(1)(100)(1.05) \\
\Rightarrow y(1) & =\frac{37.5-108}{105} \\
& =-0.671
\end{aligned}
$$

It follows that the two final automes are given by

$$
\begin{aligned}
v^{d u} & =(1.2)(108)-(0.671)(105)(1.05) \\
& =55.62
\end{aligned}
$$

$$
\begin{aligned}
U^{d d} & =(1.2)(81)-(0.671)(105)(1.05) \\
& =23.22
\end{aligned}
$$

Notice that

$$
\begin{aligned}
& U^{\text {ud }}=56.52 \\
& U^{\text {du }}=58.67
\end{aligned}
$$

since $u^{\text {ud }} \neq v^{\text {du }}$ the portfolio is not recombaning
In general the value of a two step strategy

$$
\begin{aligned}
& U_{x y}(0)=x(1) S(0)+y(1) A(0) \\
& U_{x y}(1)=x(1) S(1)+y(1) A(1) \\
& U_{x y}(2)=x(2) S(2)+y(2) A(2)
\end{aligned}
$$

The self financing condition is given by

$$
U_{x y}(1)=x(2) S(1)+y(2) A(1)
$$

This condition represent
rebalancing the portfolio at $t=1$. All funds available at $t=l$ are used in the rebalanary step. This is where the self financing term comes from.

## Pricing

Pricing in the multi-step model assumes no -arbatrage. An arbitrage is an investment strategy where the portfolios $(x(n), y(n))$, $n=1,2$ satisfy

$$
U_{x y}(0)=0
$$

and

$$
U_{x y}(n) \geqslant 0 \quad n=1,2
$$

with probability 1

$$
U_{x y}(n)>0
$$

for at least one value of $n$.
A Euoropean style option with a payoff of the form

$$
H=h(s(2))
$$

for some real valued function $n$ defined on $[0, \infty)$ is called
path independent. A path-dependent derivative security has a payoff of the form

$$
H=h(s(1), s(2))
$$

for $h:[0, \infty) \times[0, \infty) \rightarrow \mathbb{R}$
The no-arbatrage prices of a security with pay off $H$ form a sequence $H(n), n=1,2$, such that $H=H(2)$. Since no arbitrage is assumed it follows that no strategy $(x(n), y(n), z(n)), n=1,2$, with
$U_{x y z}(0)=x(1) S(0)+y(1) A(0)+z(1) H(0)=0$
$U_{x y z}(n)=X(n) S(n)+Y(n) A(n)+Z(n) H(n) \geqslant 0$
where with probability 1

$$
U_{x y z}(n)>0
$$

for at least one $n$ exists.
The proceedwre for computing the derivative security is
illustrated in the following diagrams where the tree of outcomes are shown. The calculation proceeds by computing the replicating portfolio dt each step by starting at the latest and working bockward in time.

First two replicating portfolios are computed using the payout at $t=2$. The first shown in the left diagram computes a portfolio assuming at $t=1$ the up outcome occurs. The second computes a portfolio assuming that the down outcome occured at $t=1$.
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-227.jpg?height=356&width=466&top_left_y=1549&top_left_x=286)
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-227.jpg?height=380&width=460&top_left_y=1600&top_left_x=923)

These portfolios use (H(2) to compute the replicating portfolos for the two possible values of $H(1)$. These portfolios are then used to compute H(1). Next the two HCD outcomes are used to compute the replicating portfolio for $H(0)$. This porticlio is then used to compute the derivative security price $H(0)$. This step is illustrated in the following diagram.
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-228.jpg?height=301&width=448&top_left_y=1245&top_left_x=544)

The following example works through one of these calanlations.

## Example

Let $s(0)=100, u=20 \%, D=-10 \%, R=5 \%$. $A(0)=100$, Consder a call with exercise price $k=100$ at time 2.

The payoff of the option on the second step is

$$
c(2)=(s(2)-K)^{+}
$$

For each outcome it is seen that

$$
\begin{aligned}
c(2) & = \begin{cases}\left(5 \operatorname{cox}(1+u)^{2}-k\right)^{+} & \omega=u u \\
(50)(1+D)(1+u)-k)^{+} & \omega=u d=d u \\
\left.(50)(1+D)^{2}-k\right)^{+} & \omega=d d\end{cases} \\
& = \begin{cases}\left((100)(1+0.2)^{2}-100\right)^{+} & \omega=u u \\
((100)(1+0.2)(1-0.1)-100)^{+} & \omega=u d=d u \\
\left((100)(1-0.1)^{2}-100\right)^{+} & \omega=d d\end{cases} \\
& = \begin{cases}44 & \omega=u u \\
8 & \omega=u d=d u \\
0 & \omega=d d\end{cases}
\end{aligned}
$$

Also,

$$
\begin{aligned}
s^{u u} & =s(0)(1+u)^{2}=(100)(1.2)^{2}=144 \\
s^{u d}=s^{d u} & =s(0)(1+u)(1+D)=(100)(1.2)(0.9)=108 \\
s^{d d} & =s(0)(1+D)^{2}=(100)(0.9)^{2}=81
\end{aligned}
$$

and finally

$$
\begin{aligned}
& A(1)=A(0)(1+R)=(100)(1.05)=105 \\
& A(2)=A(0)(1+R)^{2}=(100)(1.05)^{2}=110.25
\end{aligned}
$$

Using these payouts compute the two possible replicating portfolios for C(1). For the ase where the first step is up the replicating portfolio ( $x^{u}(2), y^{u}(2)$ ) is given by

$$
\begin{aligned}
& u^{u u}=x^{u}(2) s^{u u}+y^{u}(2) A(2)=44 \\
& u^{u d}=x^{u}(2) s^{u d}+y^{u}(2) A(2)=8
\end{aligned}
$$

Now, consider the first equation

$$
\begin{aligned}
& v^{u k}=x^{u}(2) s^{u k}+y^{u}(2) A(2) \\
\Rightarrow & x^{u}(2) s^{u k}=v^{u k}-y^{u}(2) A(2) \\
\Rightarrow & x^{u}(2)=\frac{1}{s^{u k}}\left[U^{u k}-Y^{u}(2) A(2)\right]
\end{aligned}
$$

substrtuting into second equation

$$
\begin{aligned}
u^{u d} & =x^{u}(2) s^{u d}+y^{u}(2) A(2) \\
& =\frac{s^{u d}}{s^{u n}}\left[u^{u n}-y^{u}(2) A(2)\right]+y^{u}(2) A(2) \\
& =\frac{s^{u d}}{s^{u n}} u^{u k}-y^{u(2)} \frac{A(2) s^{u d}}{s^{u k}}+y^{u(2)} A(2) \\
& =s^{u d} \frac{u^{u k}}{s^{u k}}-y^{u}(2) A(2)\left[\frac{s^{u d}}{s^{u n}}-1\right] \\
& =s^{u d} \frac{u^{u k}}{s^{u k}}-y^{u} \frac{(2) A(2)}{s^{u k}}\left(s^{u d}-s^{u k}\right) \\
\Rightarrow y^{u}(2) \frac{A(2)}{s^{u k}}\left(s^{u d}-s^{u k}\right) & =\frac{s^{u d} v^{u k}-v^{u d}}{s^{u k}}
\end{aligned}
$$

$$
\begin{aligned}
&=\frac{1}{s^{u k}}\left(s^{u d} u^{u n}-s^{u n} u^{u d}\right) \\
& \Rightarrow y^{u}(2)=\frac{\left(s^{u d} u^{u n}-s^{u n} u^{u d}\right)}{A(2)\left(s^{u d}-s^{u k}\right)} \\
& s o \\
& x^{u}(2)=\frac{1}{s^{u k}}\left[u^{u k}-y^{u}(2) A(2)\right] \\
&=\frac{1}{s^{u n}}\left[u^{u k}-\left(s^{u d} u^{u k}-s^{u k} u^{u d}\right)\right] \\
&\left.=\frac{1}{s^{u k}-s^{u k}}\right] \\
&\left.=\frac{1}{s^{u k}-s^{u k}} u^{u k}+s^{u k} u^{u d}\right] \\
&=\frac{1}{s^{u k}\left(s^{u d}-s^{u k}\right)}\left(s^{u k} u^{u d}-s^{u k} u^{u k}\right) \\
& s^{u d}-s^{u k}
\end{aligned}
$$

Bringing things together gives

$$
x^{u}(2)=\frac{u^{n d}-u^{u h}}{s^{n d}-s^{u h}}
$$

$$
y^{4}(2)=\frac{\left(s^{\text {nd }} u^{\text {nh }}-s^{\text {nh }} u^{\text {nd }}\right)}{A(2)\left(s^{\text {nd }}-s^{\text {nh }}\right)}
$$

Now, using

$$
\begin{array}{lll}
\text { une }=44 & u^{\text {ud }}=8 & A(2)=10.25 \\
\text { sun }=144 & \text { sud }=108 &
\end{array}
$$

gives

$$
\begin{aligned}
x^{u}(2) & =\frac{44-8}{144-108}=1 \\
y^{u}(2) & =\frac{[(108)(44)-((44)(8)]}{A(2)(108-144)} \\
& =\frac{-100}{110.25}=-0.907
\end{aligned}
$$

Thus

$$
x^{u}(2)=1 \quad y^{u}(2)=-0.907
$$

Next consider the down case replecating portfolio $\left(x^{d}(1), y^{d(1)}\right)$ which is given by

$$
\begin{aligned}
& U^{d u}=x^{d}(2) S^{d u}+y^{d}(2) A(2)=8 \\
& U^{d d}=x^{d}(2) S^{d d}+y^{d}(2) A(2)=0
\end{aligned}
$$

The equations for the portflio are found from the previously obtained expressions

$$
\begin{gathered}
x^{d}(2)=\frac{U^{d u}-U^{d d}}{S^{d u}-S^{d d}} \\
y^{d}(2)=\frac{\left(S^{d u} U^{d d}-S^{d d} U^{d u}\right)}{A(2)\left(S^{d u}-S^{d d}\right)}
\end{gathered}
$$

using the parameters,

$$
\begin{aligned}
& U^{d u}=8 \quad U^{d d}=0 \quad S^{d u}=108 \\
& S^{d d}=81 \quad A(2)=110.25 \\
& X^{d}(2)=\frac{8}{108-81}=0.296 \\
& Y^{d}(2)=\frac{(108)(0)-(81)(8)}{(110.25)(108-81)} \\
& =\frac{-648}{(110.25)(27)} \\
& =-0.218
\end{aligned}
$$

Thus

$$
x^{d}(2)=0.296 \quad y^{d}(2)=-0.218
$$

Next these portfolios can be used to compute C(1) which has two outcomes

$$
\begin{aligned}
& C^{u}=x^{u}(2) S^{u}+y^{u}(2) A(1) \\
& C^{d}=x^{d}(2) S^{d}+y^{d}(2) A(1)
\end{aligned}
$$

using the parameters

$$
\begin{aligned}
& x^{u}(2)=1 \quad y^{u}(2)=-0.907 \\
& x^{d}(2)=0.296 \quad y^{d}(2)=-0.218 \\
& s^{u}=s(0)(1+u)=(100)(1.2)=120 \\
& s^{d}=s(0)(1+D)=(100)(0.9)=90 \\
& A(1)=(100)(1.05)=105 \\
& g^{i v e s} \\
& c^{u}=(1)(120)-(0.907)(105) \\
& =24.765 \\
& c^{d}=(0.296)(90)-(0.218)(105) \\
& =3.75
\end{aligned}
$$

Thus

$$
c^{u}=24.765 \quad c^{d}=3.75
$$

Now $C C D$ is the payout for the $(x(1), y(1))$ replicating portfolio, so

$$
\begin{aligned}
& c^{u}=x(1) s^{u}+y(1) A(1) \\
& c^{d}=x(1) s^{d}+y(1) A(1)
\end{aligned}
$$

using the previous portfolio solution gives

$$
\begin{gathered}
x(1)=\frac{c^{d}-c^{u}}{s^{d}-s^{u}} \\
y(1)=\frac{s^{d} c^{u}-s^{u} c^{d}}{A(1)\left(s^{d}-s^{u}\right)}
\end{gathered}
$$

using the parameters

$$
\begin{gathered}
s^{u}=120 \quad s^{d}=90 \quad A(1)=105 \\
c^{u}=24.765 \quad c^{d}=3.75
\end{gathered}
$$

So

$$
x(1)=\frac{3.75-24.75}{90-120}
$$

$$
\begin{aligned}
& =0.7 \\
y^{(1)} & =\frac{(90)(24.767)-(120)(3.75)}{(105)(90-120)} \\
& =-0.565
\end{aligned}
$$

The replicating portfolio at $t=1$ is given by

$$
x(1)=0.7 \quad y(1)=-0.565
$$

It follows that the derivative security price $C(0)$ is given by

$$
\begin{aligned}
C(0) & =x(1) S(0)+y(1) A(0) \\
& =(0.71,00)+(-0.565)(100) \\
& =13.5
\end{aligned}
$$

## Exercise

Find the tree of values of the derivative securities with the following paysffs

$$
H_{1}=(\max \{S(n): n=0,1,2\}-100)^{-1}
$$

## Solution

Assume the following parameters

$$
\begin{gathered}
S(0)=100 \quad U=20 \% \quad D=-10 \% \\
A(0)=100 \quad R=50 \%
\end{gathered}
$$

The asset prices are given by

$$
\begin{aligned}
& s(1)=\left\{\begin{array}{l}
s(0)(1+u)=120=s u \\
s(0)(1+D)=90=s d
\end{array}\right. \\
& s(2)=\left\{\begin{array}{l}
s(0)(1+u)^{2}=144=s u u \\
s(0)(1+u)(1+D)=108=s u d=s d u \\
s(0)(1+D)^{2}=81=s d d
\end{array}\right.
\end{aligned}
$$

Now the payouts at $s(2)$ are given by

$$
\begin{aligned}
H^{\text {un }} & =\left(\max \left(5^{u}, 5^{u k}\right)-100\right)^{+} \\
& =(\max (120,144)-100)^{+} \\
& =(144-100)^{+} \\
& =44 \\
H^{u d} & =\left(\max \left(5^{u}, 5^{u d}\right)-100\right)^{+} \\
& =(\max (120,108)-100)^{+} \\
& =(120-100)^{+} \\
& =20 \\
H^{d u} & =\left(\max \left(5^{d}, 5^{u d}\right)-100\right)^{+} \\
& =(\max (90,108)-100)^{+} \\
& =(108-100)^{+} \\
& =8 \\
H^{d d} & =\left(\max \left(5^{d}, 5^{d d}\right)-100\right)^{+} \\
& =(\max (90,81)-100)^{+}
\end{aligned}
$$

$$
\begin{aligned}
& =(90-100)^{+} \\
& =0
\end{aligned}
$$

Thus the leaves of the payout tree are gruen by

$$
\begin{array}{ll}
H^{44}=44 & H^{4 C}=20 \\
H^{c 4}=8 & H^{d C}=0
\end{array}
$$

and the risk-free investment is given by

$$
\begin{gathered}
A(0)=100 \\
A(1)=A(0)(1+R)=(100)(1.05)=105
\end{gathered}
$$

The roplicating portfolio for the up payouts is given

$$
\begin{aligned}
& H^{u u}=x^{u}(2) S^{u u}+Y^{u}(2) A(2) \\
& H^{u d}=x^{u}(2) S^{u d}+Y^{u}(2) A(2)
\end{aligned}
$$

using the results obtained
previoushy,

$$
\begin{gathered}
x^{u}(2)=\frac{H^{u d}-H^{u n}}{s^{u d}-s^{u n}} \\
y^{u}(2)=\frac{s^{u d} H^{u h}-s^{u h} H^{u d}}{A(2)\left(s^{u d}-s^{u h}\right)}
\end{gathered}
$$

using the parameters

$$
\begin{gathered}
H^{44}=44 \quad H^{4 C}=20 \\
\text { sun }=144 \quad s^{4 C}=108 \\
A(2)=110.25
\end{gathered}
$$

gives

$$
\begin{aligned}
x^{u}(2) & =\frac{H^{u d}-H^{u h}}{s^{u d}-S^{u h}} \\
& =\frac{20-44}{108-144}=\frac{24}{36}=\frac{2}{3}
\end{aligned}
$$

$$
\begin{aligned}
y^{u}(z) & =\frac{s^{u d} H^{u u}-s^{u n} H^{u d}}{A(z)\left(s^{u d}-s^{u u}\right)} \\
& =\frac{(108)(44)-(144)(20)}{(10.25)(108-144)} \\
& =\frac{1872}{3969}=-0.471
\end{aligned}
$$

So

$$
x^{u}(2)=2 / 3 \quad y^{u}(2)=-0.471
$$

These values can be verified as follows

$$
\begin{aligned}
H^{u k} & =x^{u}(2) S^{u u}+Y^{u}(2) A(2) \\
& =\left(\frac{2}{3}\right)(144)+(-0.471)(110.25) \\
& =96-51.93=44.07 \\
H^{u d} & =x^{u}(2) S^{L d}+Y^{u}(2) A(2)
\end{aligned}
$$

$$
\begin{aligned}
& =(2 / 3)(108)+(-0.471)(110.25) \\
& =20.07
\end{aligned}
$$

which is consistent with input values.

The replicating for the down outcomes is given by

$$
\begin{aligned}
& H^{d u}=x^{d}(2) S^{d u}+Y^{d}(2) A(2) \\
& H^{d d}=x^{d}(2) S^{d d}+Y^{d}(2) A(2)
\end{aligned}
$$

using the previous result

$$
\begin{gathered}
x^{d}(2)=\frac{H^{d d}-H^{d u}}{S^{d d}-S^{d u}} \\
y^{d}(2)=\frac{S^{d d} H^{d u}-S^{d u} H^{d d}}{A(2)\left(S^{d d}-S^{d u}\right)}
\end{gathered}
$$

using the parameters

$$
\begin{array}{ll}
H^{d d}=0 & H^{d u}=8 \\
S^{d d}=81 & S^{u d}=108
\end{array}
$$

$$
A(2)=110.25
$$

groes

$$
\begin{aligned}
x^{d}(2) & =H^{d d}-H^{d u} \\
& =\frac{-\delta}{81-108} \\
& =0.296
\end{aligned}
$$

$$
\begin{aligned}
y^{d}(2) & =\frac{s^{d d} H^{d u}-s^{d u} H^{d d}}{A(2)\left(s^{d d}-s^{d u}\right)} \\
& =\frac{(81)(8)-(108)(0)}{(110.25)(81-108)} \\
& =\frac{-2976.75}{-0.218} \\
& =-218
\end{aligned}
$$

Thus

$$
x^{c}(2)=0.296 \quad y^{d}(2)=-0.218
$$

These results can be verfied as follows

$$
\begin{aligned}
H^{d u} & =x^{d}(2) s^{d u}+y^{d}(2) A(2) \\
& =(0.296)(108)+(-0.218)(110.25) \\
& =31.97-24.03 \\
& =7.94 \\
H^{d d} & =x^{d}(2) s^{d d}+y^{d}(2) A(2) \\
& =(0.296)(81)+(-0.218)(110.25) \\
& =23.98-24.03 \\
& =-0.05
\end{aligned}
$$

This is consistent with the input values
Now $H^{4}$ and $H^{d}$ can be computed using

$$
\begin{aligned}
& H^{u}=x^{u}(2) s^{u}+y^{u}(2) A(1) \\
& H^{d}=x^{d}(2) s^{d}+y^{d}(2) A(1)
\end{aligned}
$$

## lesing

$$
\begin{aligned}
& x^{u}(2)=2 / 3 \quad y^{u}(2)=-0.471 \\
& x^{d}(2)=0.296 \quad y^{d}(2)=-0.218 \\
& s^{u}=120 \quad s^{c}=90 \quad A(1)=105
\end{aligned}
$$

gives

$$
\begin{aligned}
H^{u} & =x^{u}(2) 5^{u}+y^{u}(2) A(1) \\
& =(2 / 3)(120)+(-0.471)(105) \\
& =80-49.46 \\
& =30.55
\end{aligned}
$$

$$
\begin{aligned}
H^{d} & =x^{d}(2) S^{d}+y^{d}(2) A(1) \\
& =(0.296)(90)+(-0.218)(105) \\
& =26.64-22.89 \\
& =3.25
\end{aligned}
$$

Finally the replicating portfolio for the option price can be computed

$$
\begin{aligned}
& H^{u}=x(1) S^{u}+y(1) A(1) \\
& H^{d}=x(1) S^{d}+y(1) A(1)
\end{aligned}
$$

using previous results gives

$$
\begin{gathered}
x(1)=\frac{H^{d}-H^{u}}{S^{d}-S^{u}} \\
y(1)=\frac{S^{d} H^{u}-S^{u} H^{d}}{A(1)\left(S^{d}-S^{u}\right)}
\end{gathered}
$$

and the parameters

$$
\begin{aligned}
& H^{u}=30.55 \quad H^{d}=3.75 \\
& S^{u}=120 \quad S^{d}=90 \quad A(1)=105 \\
& \text { gives }
\end{aligned}
$$

$$
\begin{aligned}
x(1) & =\frac{H^{d}-H^{u}}{S^{d}-S^{u}} \\
& =\frac{3.75-30.55}{90-120} \\
& =\frac{26.8}{30}=0.89 \\
y(1) & =\frac{S^{d} H^{u}-S^{u} H^{d}}{A(1)\left(S^{d}-S^{u}\right)} \\
& =\frac{(90)(30.55)-(20)(3.75)}{(105)(90-120)} \\
& =\frac{2749.5-450}{-3150} \\
& =-0.73
\end{aligned}
$$

Thus

$$
x(1)=0.89 \quad y(1)=-0.73
$$

This result can be verified

$$
\begin{aligned}
H^{u} & =x(1) S^{u}+y(1) A(1) \\
& =(0.89)(120)+(-0.73 x(105) \\
& =106.8-76.65 \\
& =30.15
\end{aligned}
$$

$$
\begin{aligned}
H^{d} & =x(1) S^{d}+y(1) A(1) \\
& =(0.89)(90)-76.65 \\
& =80.1-76.65 \\
& =3.45
\end{aligned}
$$

which is consistent with input values. The security price is given by

$$
\begin{aligned}
H(0) & =x(1) S(0)+y(4) A(0) \\
& =(0.89)(100)+(-0.73)(100)
\end{aligned}
$$

$$
=16
$$

It follows that the payoff tree of the security is given by
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-251.jpg?height=424&width=620&top_left_y=602&top_left_x=388)

## Partitions and Information

In this section a three-step model is needed. First an overvew of the model is given then the problem to be solved is discussed.
If the outcomes at each step are denoted by $u$ for an up outcome and $d$ for a down outcome the three-step madel event space is given by
$\Omega=$ そune, und, udu, udd, duk, dud, ddu, ddd $\xi$
note that there are $2^{3}$ possible outcomes.

If

$$
P(u)=p \quad P(d)=1-p
$$

and the steps are assumed independent it follows that

$$
\begin{aligned}
P(\text { unu }) & =P^{3} \\
P(\text { und }) & =P(\text { udu })=P(\text { duu }) \\
& =P^{2}(1-P) \\
P(\text { udd }) & =P(\text { dud })=P(\text { ddu }) \\
& =P(1-P)^{2} \\
P(\text { ddd }) & =(1-P)^{3}
\end{aligned}
$$

The third stock price is given by

$$
\begin{aligned}
s(3) & =s(2)\left(1+k_{3}\right) \\
& =\left\{\begin{array}{l}
s \text { une }=s(0)(1+u)^{3} \\
s \text { und }=s \text { udu }=s d u=s(0)(1+w)^{2}(1+D) \\
s \text { udd }=s \text { dud }=s d u=s(0)(1+u)(1+D)^{2} \\
s \text { ddd }=s(0)(1+D)^{2}
\end{array}\right.
\end{aligned}
$$

## Assume

$$
\begin{array}{rrr}
S(0)=100 & u=20 q_{0} & D=-10 q_{0} \\
A(0)=100 & R=5 q_{0} & P=0.6
\end{array}
$$

This leads to the asset price tree

S(0) $5(1) \quad 5(2) \quad 5(3)$
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-254.jpg?height=799&width=944&top_left_y=777&top_left_x=213)

Consider the following random vomiable representing the payout of a European call option,

$$
H=(s(3)-k)^{+}
$$

where the strike price $k$ is given by,

$$
K=100
$$

The payoff for this option using the exsting parameters is given by
$H^{\text {men }}=(172.8-100)^{+}=72.8$
$H^{\text {und }}=H^{\text {udu }}=H^{\text {dule }}(129.6-100)^{-1}=29.6$
$H^{\text {udd }}=H^{\text {ddu }}=H^{\text {dud }}(97.2-100)^{t}=0$
$\mathrm{H}^{\text {ddd }}=(72.9-100)^{t}=0$
The expection of $H$ with respect to the probability $P$ is given by

$$
\begin{aligned}
E[H] & =H^{\text {unu }} P(\text { nnu })+H^{\text {nd }} P(\text { nud }) \\
& +H^{\text {ndu }} P(\text { ndu })+H^{\text {dun }} P(\text { dwa })
\end{aligned}
$$

$$
\begin{aligned}
& +H^{\text {udd }} P(\text { udd })+H^{\text {ddu }} P(\text { ddu }) \\
& +H^{\text {dud }} P(\text { dud })+H^{\text {dd }} P(\text { ddd }) \\
= & (72.8) P^{3}+(29.6)\left[P^{2}(1-P)+P^{2}(1-P)\right. \\
& \left.P^{2}(1-P)\right]+(0)\left[P(1-P)^{2}+P(1-P)^{2}\right. \\
& \left.+P(1-P)^{2}\right]+(0)(1-P)^{3} \\
= & (72.8)(0.6)^{3}+(29.6)(3)(0.6)^{2}(0.4) \\
= & 15.7248+12.7872 \\
= & 28.51
\end{aligned}
$$

It is interesting to compare this result to the value computed using the risk-neutral problability. An expression for the derivative security expectation with respect to the risk-newrbal probability is discussed in the next section

## Risk-neutral Probability for Three-

step model

The proceedure for calculating the option price in the two-step model can be exteded to the three step model.
Here a European call option is assumed with payoff

$$
H=(s(3)-k)^{+}
$$

since the payoff depends only on the final asset price it follows that the price is path independent so

$$
\begin{aligned}
H^{\text {ud }} & =H^{\text {du }} \\
H^{\text {und }} & =H^{\text {udu }}=H^{\text {duu }} \\
H^{\text {ddu }} & =H^{\text {dud }}=H^{\text {udd }}
\end{aligned}
$$

It follows that the derivative pricing tree is given by
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-258.jpg?height=822&width=956&top_left_y=118&top_left_x=227)

Recall that if 9 is a risk-neutral distribution tren

$$
\begin{aligned}
H(0) & =E_{Q}\left[(1+R)^{-1} H(1)\right] \\
& =(1+R)^{-1}\left[q H^{u}+(1-q) H^{d}\right]
\end{aligned}
$$

Following the proceedwe user for the two step model, stcort at the leaves of the tree and work backwords applying this expression at each step

## This proceedure is illustrated in the following diagrams

![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-259.jpg?height=825&width=971&top_left_y=326&top_left_x=245)
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-259.jpg?height=830&width=977&top_left_y=1164&top_left_x=243)

![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-260.jpg?height=679&width=944&top_left_y=114&top_left_x=316)
$\searrow H^{d d d}$

The price of the derivative security is the result of the third step
From the first step three equations are obtained

$$
\begin{aligned}
& H^{u u}=(1+R)^{-1}\left[q H^{u u u}+(1-q) H^{u d d}\right] \\
& H^{u d}=(1+R)^{-1}\left[q H^{u d}+(1-q) H^{u d d}\right] \\
& H^{d d}=(1+R)^{-1}\left[q H^{u d d}+(1-q) H^{d d d}\right]
\end{aligned}
$$

From the second two equations are dotained

$$
\begin{aligned}
& H^{u}=(1+R)^{-1}\left[q H^{u u}+(1-q) H^{u d}\right] \\
& H^{d}=(1+R)^{-1}\left[q H^{u d}+(1-q) H^{d d}\right]
\end{aligned}
$$

and finally for the firal step

$$
H(0)=(1+R)^{-1}\left[q H^{u}+(1-q) H^{c}\right]
$$

Now substituting the equations from the first step into the second step gives

$$
\begin{aligned}
H^{u}= & (1+R)^{-1}\left\{q(1+R)^{-1}\left[q H^{u n u}+(1-q) H^{u n d}\right]\right. \\
& \left.+(1-q)(1+R)^{-1}\left[q H^{u n d}+(1-q) H^{\text {udd }}\right]\right\} \\
= & (1+R)^{-2}\left[q^{2} H^{\text {unu }}+q(1-q) H^{\text {und }}\right. \\
& \left.+q(1-q) H^{\text {und }}+(1-q)^{2} H^{\text {udd }}\right]
\end{aligned}
$$

$$
\begin{gathered}
=(1+R)^{-2}\left[q^{2} H^{\text {unu }}+2 q(1-q) H^{\text {whed }}\right. \\
\left.+(1-q)^{2} H^{\text {udd }}\right]
\end{gathered}
$$

and

$$
\begin{aligned}
H^{d}= & (1+R)^{-1}\left\{q(1+R)^{-1}\left[q H^{\text {und }}+(1-q) H^{\text {udd }}\right]\right. \\
& \left.+(1-q)(1+R)^{-1}\left[q H^{\text {udd }}+(1-q) H^{\text {ddd }}\right]\right\} \\
= & (1+R)^{-2}\left[q^{2} H^{\text {und }}+q(1-q) H^{\text {udd }}\right. \\
& \left.+q(1-q) H^{\text {udd }}+(1-q)^{2} H^{\text {ddd }}\right] \\
= & (1+R)^{-2}\left[q^{2} H^{\text {und }}+2 q(1-q) H^{\text {udd }}\right. \\
& \left.+(1-q)^{2} H^{\text {dd }}\right]
\end{aligned}
$$

Thus

$$
\begin{aligned}
H^{u}=(1+R)^{-2} & {\left[q^{2} H^{u u u}+2 q(1-q) H^{\text {und }}\right.} \\
& \left.+(1-q)^{2} H^{\text {udd }}\right] \\
H^{d}=(1+R)^{-2} & {\left[q^{2} H^{\text {und }}+2 q(1-q) H^{\text {udd }}\right.} \\
& \left.+(1-q)^{2} H^{\text {ddd }}\right]
\end{aligned}
$$

The final result is obtained by substituting these equations into the equation for the first step

$$
\begin{aligned}
H(0)= & (1+R)^{-1}\left\{q ( 1 + R ) ^ { - 2 } \left[q^{2} H^{\text {unu }}\right.\right. \\
+ & \left.2 q(1-q) H^{\text {und }}+(1-q)^{2} H^{\text {udd }}\right] \\
+ & (1-q)(1+R)^{-1}\left[q^{2} H^{\text {und }}+2 q(1-q) H^{\text {ud }}\right. \\
& \left.+(1-q)^{2} H^{\text {ddd }}\right] \\
= & (1+R)^{-3}\left[q^{3} H^{\text {unu }}+2 q^{2}(1-q) H^{\text {und }}\right. \\
& +q(1-q)^{2} H^{\text {udd }}+q^{2}(1-q) H^{\text {und }} \\
& \left.+2 q(1-q)^{2} H^{\text {udd }}+(1-q)^{3} H^{\text {ddd }}\right] \\
= & (1+R)^{-3}\left[q^{3} H^{\text {unun }}+3 q^{2}(1-q) H^{\text {und }}\right. \\
& \left.+3 q(1-q)^{2} H^{\text {udd }}+(1-q)^{3} H^{\text {ddd }}\right]
\end{aligned}
$$

Thus

$$
\begin{aligned}
H(0)= & (1+R)^{-3}\left[q^{3} H^{\text {uhu }}+3 q^{2}(1-q) H^{\text {und }}\right. \\
& \left.+3 q(1-q)^{2} H^{\text {udd }}+(1-q)^{3} H^{\text {ddd }}\right] \\
= & (1+R)^{-3} E_{Q}[H(3)] \\
= & E_{Q}\left[(1+R)^{-3} H(3)\right]
\end{aligned}
$$

but

$$
H(3)=(s(3)-k)^{+}
$$

thus

$$
H(0)=E_{Q}\left[(1+R)^{-3}(s(3)-k)^{+}\right]
$$

Assuming the parameters

$$
\begin{array}{lll}
S(0)=100 & u=20 \% & D=-10 \% \\
A(0)=100 & R=5 \% & K=100
\end{array}
$$

It follows that

$$
q=\frac{R-D}{u-D}=\frac{0.05+0.1}{0.2+0.1}=\frac{0.15}{0.3}=\frac{1}{2}
$$

and

$$
1-9=\frac{1}{2}
$$

also

$$
\begin{array}{r}
s(3)=\left\{\begin{array}{l}
s^{\text {whe }}=s(0)(1+u)^{3} \\
s^{\text {wad }}=s(0)(1+u)^{2}(1+D) \\
s^{\text {udd }}=s(0)(1+u)(1+D)^{2} \\
s^{d d}=s(0)(1+D)^{3}
\end{array}\right. \\
\Rightarrow s(3)=\left\{\begin{array}{l}
(100)(1.2)^{3}=172.8 \\
(100)(1.2)^{2}(0.9)=129.6 \\
(100)(1.2)(0.9)^{2}=97.2 \\
(100)(0.9)^{3}=72.9
\end{array}\right.
\end{array}
$$

The payout at $t=3$ is given by

$$
H(3)=(S(3)-100)^{+}=\left\{\begin{array}{l}
H^{\text {wull }}=72,8 \\
H^{\text {und }}=29,6 \\
H_{\text {udd }}=0 \\
H^{\text {dd }}=0
\end{array}\right.
$$

It follows that

$$
\begin{aligned}
H(0)= & (1+R)^{-3}\left[q^{3} H^{\text {unh }}+3 q^{2}(1-q) H^{\text {und }}\right. \\
& \left.+3 q(1-q)^{2} H^{\text {udd }}+(1-q)^{3} H^{\text {ddd }}\right]
\end{aligned}
$$

$$
\begin{aligned}
= & (1.05)^{-3}\left[\left(\frac{1}{2}\right)^{3}(72.8)+3\left(\frac{1}{2}\right)^{3}(29.6)\right. \\
& \left.+3\left(\frac{1}{2}\right)^{3}(0)+(1 / 2)^{3}(0)\right] \\
= & (1.05)^{-3}\left(\frac{1}{2}\right)^{3}[(72.8)+(3)(29.6)] \\
= & \frac{(0.8638)}{8}(161.6) \\
= & 17.45
\end{aligned}
$$

## Conditional Expectation

Here the dea of conditional expectation is discussed Conditional expectation makes use of conditional probability which will be reviewed first.

Consider the event space $\Omega$ which contains all possible outcomes of the model. Let $\omega$ denote a single event so

$$
\omega \in \Omega
$$

Let $P(\omega)$ denote the probability that event $\omega$ occurs. P( $\omega$ ) is a measure on the event space $\Omega$. Consider the set of event $s, B$,

$$
B \subseteq \Omega
$$

and let $\omega \in B$. Now the probability that $\omega$ will
occur given that $B$ has occured is called the conditional probability of $\omega$ given $B$ and is defined by

$$
P(\omega \mid B)=\frac{P(\omega)}{P(B)}
$$

If $A \subseteq B$ then this becomes

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

It is easy to see that

$$
P(B \mid B)=\frac{P(B)}{P(B)}=1
$$

Thus $P(\omega \mid B)$ is a probability measure.
Now consider the three step model. The event space is given by
$\Omega=\{$ unu, und, udu, udd,
$d d d, d d u, d u d, u d d\}$

Consider the event where the first step is up.

$$
B_{u}=\{\text { mus, und, udu, udd }\}
$$

if $\omega \in B_{u}$ then

$$
P\left(\omega \mid B_{u}\right)=\frac{P(\omega)}{P\left(B_{u}\right)}
$$

For example if $P(u)=P$ and $P(d)=1-p$ then

$$
\begin{aligned}
P\left(B_{u}\right)= & P(\text { unu })+P(u d d)+P(u d u) \\
& +P(\text { und }) \\
= & P^{3}+p(1-p)^{2}+2 p^{2}(1-p) \\
= & p^{3}+p\left(1-2 p+p^{2}\right)+2 p^{2}-2 p^{3} \\
= & p^{3}+p-2 p^{2}+p^{3}+2 p^{2}-2 p^{3}
\end{aligned}
$$

$$
=P
$$

and

$$
P(u d u)=p^{2}(1-p)
$$

80

$$
\begin{aligned}
P\left(u d u \mid B_{u}\right) & =P^{2} \frac{(1-P)}{P} \\
& =P(1-P)
\end{aligned}
$$

Now consider the expectation of the derivative security H(3) with respect to this probability

$$
E\left[H(3) \mid B_{n}\right]=\sum_{\omega \in B_{n}} H(\omega) P\left(\omega \mid B_{n}\right)
$$

This is called the conditional expectation of $H(3)$ with respect to Bu .

Using parameters from the previoles section

$$
\begin{array}{rl}
H(\text { unu })=72.8 & H(\text { und })=29.6 \\
H(\text { udd })=0 & H(\text { dd })=0
\end{array}
$$

It follows that

$$
\begin{aligned}
E[ & \left.H(3) \mid B_{u}\right]=H(\text { unu }) P\left(\text { umu } \mid B_{u}\right) \\
& +H(\text { und }) P\left(\text { und } \mid B_{u}\right) \\
& +H(\text { udu }) P\left(\text { udu } \mid B_{u}\right) \\
& +H(\text { udd }) P\left(\text { udd } \mid B_{u}\right)
\end{aligned}
$$

Now

$$
\begin{aligned}
& P\left(\text { unu } \mid B_{u}\right)=P^{2} \\
& P\left(\text { und } \mid B_{u}\right)=P(1-P) \\
& P\left(\text { udu } \mid B_{u}\right)=P(1-P) \\
& P\left(\text { udd } \mid B_{u}\right)=(1-P)^{2}
\end{aligned}
$$

using $p=0.6$ gives

$$
\begin{aligned}
E\left[H(3) \mid B_{u}\right] & =(72.8)(0.6)^{2} \\
+(2)(29.6)(0.6)(0.4)+(0)(0.4)^{2} & \\
& =26.21+14.21 \\
& =40.414
\end{aligned}
$$

similarly, for the event where the first step is down is given by,

$$
B_{d}=\{d u u, d d u, d u d, d d d\}
$$

$$
\begin{aligned}
P\left(B_{d}\right)= & (1-p) p^{2}+(1-p)^{2} p+(1-p)^{2} p \\
& +(1-p)^{3} \\
= & (1-p)\left[p^{2}+(1-p) p+(1-p) p\right. \\
& \left.1-\partial p+p^{2}\right] \\
= & (1-p)\left(p^{2}+p-p^{2}+p-p^{2}+1\right. \\
& \left.-2 \bar{p}+p^{2}\right)
\end{aligned}
$$

$$
=(1-p)
$$

It follows that

$$
\begin{aligned}
& P\left(d \text { uu } \mid B_{d}\right)=P^{2} \\
& P\left(d d u \mid B_{d}\right)=P(1-P) \\
& P\left(d u d \mid B_{d}\right)=P(1-P) \\
& P\left(d d d \mid B_{d}\right)=(1-P)^{2}
\end{aligned}
$$

so the expected payout of the derivative security $H(\omega)$ given that the forst step is down is given by

$$
\begin{aligned}
E & {\left[H(3) \mid B_{d}\right]=H(d u h) P\left(\text { duul } B_{d}\right) } \\
& +H(d d u) P\left(d d u \mid B_{d}\right) \\
& +H(d u d) P\left(d u d \mid B_{d}\right) \\
& +H(d d d) P\left(d d d \mid B_{d}\right)
\end{aligned}
$$

$$
\begin{aligned}
= & (29.6)(0.6)^{2}+(2)(0)(0.6)(0.4) \\
& +(0)(0.4)^{2} \\
= & 10.66
\end{aligned}
$$

## Partitions and Information

A family of $P=\left\{B_{i}\right\}$ of subsets of $\Omega$ is a partition if the following conditions are met

$$
\begin{aligned}
B_{i} \cap B_{j} & =\varnothing \text { for } c \neq j \\
\Omega & =\cup B_{i}
\end{aligned}
$$

The sets discussed in the previous section, $B_{u}$ and $B_{d}$, which contain all events that have a first step of $u$ and $d$ respectively form a partition,

$$
P_{1}=\left\{B_{u}, B_{d}\right\}
$$

since this partion depends of the first step if follows that $P_{1}$ is determined by $S(1)$. It follows that

$$
\begin{aligned}
E[H \mid P,](\omega) & =E[H \mid S(1)](\omega) \\
& = \begin{cases}40.416 & \omega \in B_{1} \\
10.656 & \omega \in B_{2}\end{cases}
\end{aligned}
$$

Next consider all price movement in the first two steps. There are four posible outcomes

$$
\begin{aligned}
& B_{\text {uu }}=\{u u u, \text { und }\} \\
& B_{u d}=\{u d u, u d d\} \\
& B_{d u}=\{d u u, \text { dud }\} \\
& B_{d d}=\{d d u, d d d\}
\end{aligned}
$$

which define a partition,

$$
P_{2}=\left\{B_{u u}, B_{u d}, B_{d u}, B_{d d}\right\}
$$

Now

$$
\begin{aligned}
P\left(B_{w_{u}}\right) & =p^{3}+p^{2}(1-p) \\
& =p^{2}(p+1-p)
\end{aligned}
$$

$=\rho^{2}$

$$
\begin{aligned}
P\left(B_{u d}\right) & =p^{2}(1-p)+p(1-p)^{2} \\
& =p(1-p)(p+1-p) \\
& =p(1-p)
\end{aligned}
$$

$$
\begin{aligned}
P\left(B_{d u}\right) & =p^{2}(1-p)+p(1-p)^{2} \\
& =p(1-p)(p+1-p) \\
& =p(1-p)
\end{aligned}
$$

$$
P\left(B_{d d}\right)=p(1-p)^{2}+(1-p)^{3}
$$

$$
=(1-p)^{2}(p+1-p)
$$

$$
=(1-p)^{2}
$$

Thus

$$
\begin{gathered}
P\left(B_{w k}\right)=P^{2} \\
P\left(B_{u d}\right)=P\left(B_{d u}\right)=P(1-P) \\
P\left(B_{d d}\right)=(1-P)^{2}
\end{gathered}
$$

To compute the expected payout the probability of the outcomes
unn, und, udd, ddd
conditioned on the elements of $P_{2}$ are required

$$
\begin{aligned}
& P(\text { unul Bun })=\frac{P^{3}}{P^{2}}=P \\
& P(\text { und } \mid \text { Bun })=\frac{P^{2}(1-P)}{P^{2}}=(1-P)
\end{aligned}
$$

all other conditional probabilities are zero, similarly for Bud

$$
\begin{aligned}
& P(\text { udu| Bud })=\frac{P^{2}(1-P)}{P(1-P)}=P \\
& P(\text { udd| Bud })=\frac{P(1-P)^{2}}{P(1-P)}=1-P
\end{aligned}
$$

for Bdu,

$$
\begin{aligned}
& P\left(d u u \mid B_{d u}\right)=\frac{P^{2}(1-p)}{\rho(1-p)}=P \\
& P\left(d u d \mid B_{d u}\right)=\frac{p(1-p)^{2}}{p(1-p)}=1-P
\end{aligned}
$$

and finally for $B d d$,

$$
\begin{aligned}
& P\left(d d u \mid B_{d d}\right)=\frac{P(1-p)^{2}}{(1-p)^{2}}=P \\
& P\left(d d d \mid B_{d d}\right)=\frac{(1-p)^{3}}{(1-p)}=1-p
\end{aligned}
$$

Notice that this breaks the three step model into 4 single step models
If the payouts for H from the presious section are used

$$
\begin{array}{rl}
H(\text { unu })=72.8 & H(\text { und })=29.6 \\
H(\text { udd })=0 & H(\text { dd })=0
\end{array}
$$

$$
p=0.6 \quad 1-p=0.4
$$

Now the condition expectations of the payouts are given bil

$$
\begin{aligned}
E\left[H \mid B_{\text {un }}\right] & =\text { Hum } P(\text { unul Bu }) \\
+ \text { Hund } P & \left(\text { und } \mid B_{u}\right) \\
& =\text { Hunu } P+\text { Hud }(1-P) \\
& =(72,810.6)+(29,6)(0.4) \\
& =55,52 \\
E\left[H \mid B_{\text {ud }}\right] & =\text { Hudu } P \text { (udulBud) } \\
& + \text { Hudd } P \text { (udd } 1 \text { Bud ) } \\
& =\text { Hudu } P+\text { Hudd }(1-P) \\
& =(29,6)(0.6)+(0)(0.4) \\
& =17.76
\end{aligned}
$$

$E\left[H \mid B_{d u}\right]=H_{d u} u P\left(d m u \mid B_{d u}\right)$ + Hdud P (dud I Bdu)

$$
\begin{aligned}
& =H_{d u u} P+H_{d u d}(1-P) \\
& =(29.6)(0.6)+(0 \times 0.4) \\
& =17.6 \\
E\left[H \mid B_{d d}\right] & =H_{d d u} P\left(d d u \mid B_{d d}\right) \\
& +H_{d d d} P\left(d d d \mid B_{d d}\right) \\
& =H_{d d u}+H_{d d d}(1-P) \\
& =(0)(0.6)+(0)(0.4) \\
& =0
\end{aligned}
$$

Thus

$$
E\left[H \mid P_{2}\right](\omega)=\left\{\begin{array}{cl}
55,52 & \omega \in B_{u n} \\
17,6 & \omega \in B_{u d} \cup B_{d n} \\
0 & \omega \in B_{d d}
\end{array}\right.
$$

Notice that the conditional expectation is a random variable.

Consider the case where s(2) is known. There are three unique values,

$$
s^{u n}, s^{u d}=s^{c u}, s^{d d}
$$

This leads to three partitions

$$
B_{n 4}=\{n u n, u n d\} \quad B_{d d}=\{d d u, d d d\}
$$

$B_{d u} \cup B_{u d}=\{d u d, d u u, d d u, d d d\}$

$$
P_{s(2)}=\left\{B_{u u}, B_{d u} \cup B_{u d}, B_{d d}\right\}
$$

and

$$
E[H \mid S(2)]=\left\{\begin{array}{cl}
55.52 & \omega \in B_{u n} \\
17.6 & \omega \in B_{u d} \cup B_{d n} \\
0 & \omega \in B_{d d}
\end{array}\right.
$$

Thus

$$
E[H \mid s(2)]=E\left[H \mid P_{s(2)}\right]
$$

In general this is not true. Here the payout of the cortingent claim is path independent. If the payout is path dependent there would be no equality.
Finally consider the case where the result of all three steps is known. This leads to a partition where each set in the partition contains one cuent,

$$
\begin{array}{r}
P_{3}=\left\{B_{\text {um }},\right. \text { Bund, Budu, Budd } \\
\left.B_{\text {dun }}, B_{\text {ddu }}, B_{\text {dud }}, B_{\text {dd }}\right\}
\end{array}
$$

where

$$
\begin{array}{ll}
B_{\text {unu }}=\{\text { unk }\}, & B_{\text {und }}=\{\text { und }\} \\
B_{\text {udu }}=\{\text { udu }\}, & B_{\text {udd }}=\{\text { udd }\} \\
B_{\text {dun }}=\left\{d_{\text {uk }}\right\}, & B_{\text {ddu }}=\{d d u\} \\
B_{\text {dud }}=\{d u d\}, & B_{\text {ddd }}=\{d d d\}
\end{array}
$$

Clearly for $B \omega$ where $\omega \in \Omega$

$$
\begin{aligned}
P\left(\omega \mid B_{\omega}\right) & =\frac{P(\omega)}{P\left(B_{\omega}\right)} \\
& = \begin{cases}1 & \omega \in B_{\omega} \\
0 & \omega \notin B_{\omega}\end{cases} \\
& =\mathbb{1}_{B \omega}
\end{aligned}
$$

where $\mathbb{1}_{\text {Bw }}$ is the indicator function for Bw

It follows that

$$
\begin{aligned}
& E\left[H \mid P_{3}\right](\omega)=H(\omega) \\
\Rightarrow & E\left[H \mid P_{3}\right]=H
\end{aligned}
$$

Recall that the conditional expectation is defined by

$$
E[X \mid B]=\sum_{\omega \in \Omega} Z(\omega) P(\omega \mid B)
$$

where $\bar{X}$ is a random oariable $B$ is some event with $P(B) \neq 0$ and

$$
P(\omega \mid B)=\left\{\begin{array}{cc}
\frac{P(\omega)}{P(B)} & \omega \in B \\
0 & \omega \notin B
\end{array}\right.
$$

For a partion

$$
P=\left\{B_{i}\right\}
$$

The conditional expectation computed for each $B_{i}$ gives a function defined for all $w \in \Omega$ which has a constant value for each $B_{i}$.

$$
E[X \mid P]: \Omega \rightarrow \mathbb{R}
$$

Thus the conditional expection
of $\bar{X}$ with respect to $P$ is a simple function from measure theory

## Martingale Properties

Define the discounded asset price for the n'th step of the binomial model by

$$
\tilde{S}(n)=S(n)(1+R)^{-n}
$$

Now recall that for the single step model the expectation of $\xi(1)$ with respect to the risk-neutral probability,

$$
q=\frac{R-D}{u-D} \quad 1-q=\frac{u-R}{u-D}
$$

is given by

$$
\begin{aligned}
& E_{Q}[\tilde{S}(1)]=E_{Q}\left[(1+R)^{-1} s(1)\right] \\
& =\frac{1}{(1+R)}\left[\frac{R-D}{u-D} s^{u}+\frac{u-R}{u-D} s^{d}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{(1+R)(u-D)}[(R-D) s(0)(1+u) \\
& =\frac{s(0)}{(1+R)(u-D)}[(R-D)(1+u)+(u-R)(1+D)] \\
& =\frac{s(0)}{(1+R)(u-D)}(r R-D+u R-u D+u-R)^{\prime} \\
& \quad+\frac{\sigma D}{u D-R D)} \\
& =\frac{s(0)(u R-D+u-R D)}{(1+R)(u-D)} \\
& =\frac{s(0)[(u-D)+R(u-D]}{(1+R)(u-D)} \\
& =s(0)(u-D)(1+R) \\
& =s(0)
\end{aligned}
$$

Here this result is extended to the three-step model

For the three-step model it is also assumed that

$$
G=\frac{R-D}{u-D}
$$

where $g$ is the transition probatility between steps just like $p$.

For the three-step model recall that the sample space is given by

$$
\begin{array}{r}
\Omega=\{\text { unu, und, udu, udd, } \\
\text { dun, ddu, dud, ddd }
\end{array}
$$

So
$Q($ unu $)=q^{3} \quad Q($ und $)=q^{2}(1-q)$
$Q(u d u)=q^{2}(1-q) \quad Q(u d d)=q(1-q)^{2}$
$Q($ duu $)=q^{2(l-q)} Q($ dud $)=q(l-q)^{2}$

$$
Q(d d u)=q^{(1-q)^{2}} \quad Q(d d d)=(1-q)^{3}
$$

It follows that the partion defined by

$$
\begin{aligned}
B_{u} & =\{\omega: \operatorname{s}(x)(\omega)=s u\} \\
& =\{w u n, \text { und, udu, udd }\}
\end{aligned}
$$

Now

$$
\begin{aligned}
Q\left(B_{u}\right)= & Q(\text { uun })+Q(\text { und }) \\
+ & Q(u d u)+Q(u d d) \\
= & q^{3}+q^{2}(1-q)+q^{2}(1-q) \\
& +q(1-q)^{2} \\
= & q^{3}+q^{2}-q^{3}+q^{2}-q^{3} \\
& +q\left(1-2 q+q^{2}\right) \\
= & q^{3}+2 q^{2}-2 q^{3}+q \\
& -2 q^{2}+q^{3}
\end{aligned}
$$

$$
=9
$$

Consider the trivial partition

$$
B_{0}=\{\Omega\}
$$

This partition represents the case where nothing has happend
The conditional expectation of $\tilde{S}(1)$ with respect $Q_{0}$ and $Q$ is

$$
\begin{aligned}
E_{Q}\left[\tilde{S}(1) \mid P_{0}\right] & =E_{Q}[\tilde{S}(1) \mid \Omega] \\
& =\frac{(1+R)^{-1}}{P(\Omega)}\left[S^{u} Q\left(\omega+S^{d} Q(d)\right]\right.
\end{aligned}
$$

Now

$$
\begin{aligned}
Q(u)= & Q(\text { unu })+Q(\text { und })+Q(\text { udu }) \\
& +Q(\text { udd }) \\
= & q^{3}+q^{2}(1-q)+q^{2}(1-q)+q(1-q)^{2}
\end{aligned}
$$

$$
\begin{aligned}
& =q^{3}+q^{2}-q^{3}+q^{2}-q^{3}+q\left(1-2 q+q^{2}\right) \\
& =-q^{3}+2 q^{2}+q-2 q^{2}+q^{3} \\
& =q
\end{aligned}
$$

$$
\begin{aligned}
Q(d)= & Q(d d d)+Q(d d u)+Q(d u d) \\
& +Q(d u u) \\
= & (1-q)^{3}+2 q(1-q)^{2}+q^{2}(1-q) \\
= & (1-q)\left[(1-q)^{2}+2 q(1-q)+q^{2}\right] \\
= & (1-q)\left[1-2 \hat{q}+q^{2}+2 q-2 q^{2}+q^{2}\right] \\
= & (1-q)
\end{aligned}
$$

and

$$
P(\Omega)=1
$$

Thus

$$
\begin{aligned}
E_{Q} & {[\tilde{s}(1) \mid \Omega]=(1+R)^{-1}\left[q s^{u}+(1-q) s^{c}\right] } \\
& =(1+R)^{-1}\left[\frac{(R-D)}{u-D} \operatorname{s}(0)(1+u)+\frac{(u-R)}{u-D} \operatorname{scos}(1+D)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{(1+R)^{-1}}{u-D}{ }^{s(0)} \begin{array}{c}
{[(R-D)(1+u)+(u-R)(1+D)]} \\
=\frac{(1-R)^{-1}}{u-D} s(0)\left[\begin{array}{c}
(R-D)+u R-1 \\
+u D
\end{array}\right]+(u-R)
\end{array} \\
& =\frac{s(0)}{(1+R)(u-D)}[u-D+R(u-D)] \\
& =\frac{s(0)}{(1+R)(u-D)}(u-D)(1+R) \\
& =s(0)
\end{aligned}
$$

Thus

$$
E_{Q}\left[\tilde{\zeta}(1) 1 \_\Omega\right]=S(0)
$$

Next consider

$$
E_{Q}\left[\tilde{s}(2) \mid Q_{1}\right]
$$

which represents the situation after the first step
Now,

$$
\begin{gathered}
Q_{1}=\left\{B_{u}, B_{d}\right\} \\
B_{u}=\{u m u, u u d, u d u, u d d\} \\
B_{d}=\{d u n, d u d, d d u, d d d\}
\end{gathered}
$$

Now

$$
\begin{aligned}
& E_{Q}\left[\tilde{S}(2) \mid B_{1}\right]= \begin{cases}E_{Q}\left[\tilde{S}(2) \mid B_{u}\right] & \left\{E_{Q}\left[\tilde{S}(2) \mid B_{d}\right]\right.\end{cases} \\
& P\left(B_{u}\right)=q \\
& P\left(s^{\text {hu }}\right)=q^{2}
\end{aligned} \quad P\left(B_{d}\right)=(1-q)=q(1-q) \text { ( } s^{\text {hd }} \text { ) }
$$

So

$$
\begin{gathered}
E_{Q}\left[\tilde{s}(2)\left(B_{u}\right]=\frac{1}{P\left(B_{n}\right)(1+R)^{2}}\left[q^{2} s^{u u}\right.\right. \\
\left.+q(1-q) s^{u d}\right]
\end{gathered}
$$

$$
\begin{aligned}
& =\frac{1}{q(1+R)^{2}}\left[q^{2} s^{u}(1+u)+q(1-q) s^{u}(1+D)\right] \\
& =\frac{q s^{u}}{q(1+R)^{2}}[q(1+u)+(1-q)(1+D)] \\
& =\frac{s^{u}}{(1+R)^{2}}(1+R) \\
& =\frac{s^{u}}{(1+R)}
\end{aligned}
$$

and smilarly,

$$
\begin{aligned}
E_{Q}\left[\tilde{S}(2) \mid B_{d}\right]= & \frac{1}{P\left(B_{d}\right)(1+R)^{2}}\left[q(1-q) S^{d u}\right. \\
& \left.+(1-q)^{2} S^{d d}\right] \\
= & \frac{(1-q)}{(1-q)(1+R)^{2}}\left[q^{S d}(1+u)+(1-q) S^{d}(1+D)\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{s^{d}}{(1+R)^{2}}[q(1+u)+(1-q)(1+D)] \\
& =\frac{s^{d}}{(1+R)^{2}}(1+R) \\
& =\frac{s d}{(1+R)}
\end{aligned}
$$

It follows that

$$
\begin{aligned}
E_{Q}\left[\tilde{s}(2) \mid Q_{1}\right](\omega) & = \begin{cases}s^{u}(1+R)^{-1} & w \in B_{u} \\
s^{d}(1+R)^{-1} & w \in B_{d}\end{cases} \\
& =\tilde{s}(1)
\end{aligned}
$$

Finally consider the firal step. The partition contains four elements

$$
B_{m n}=\{\text { ume, und }\}
$$

$$
\begin{array}{r}
B_{u d}=\{u d u, u d d\} \\
B_{d u}=\{d u u, d u d\} \\
B_{d d}=\{d d u, d d d\} \\
P_{2}=\left\{B_{u m}, B_{u d}, B_{d u}, B_{d d}\right\}
\end{array}
$$

Now

$$
\begin{aligned}
P\left(B_{\text {un }}\right) & =P(\text { unu })+P(\text { und }) \\
& =q^{3}+q^{2}(1-q) \\
& =q^{2}(q 1-q) \\
& =q^{2} \\
P\left(B_{\text {ud }}\right) & =P(\text { udu })+P(\text { udd }) \\
& =q^{2}(1-q)+q(1-q)^{2} \\
& =q^{(1-q)}(q+1-q) \\
& =q(1-q)
\end{aligned}
$$

$$
\begin{aligned}
P\left(B_{d u}\right) & =P(d u u)+P(d u d) \\
& =q^{2}(1-q)+q(1-q)^{2} \\
& =q(1-q)(q+1-q) \\
& =q(1-q) \\
P\left(B_{d d}\right) & =P(d d u)+P(d d d) \\
& =q(1-q)^{2}+(1-q)^{3} \\
& =(1-q)^{2}(q+1-q) \\
& =(1-q)^{2}
\end{aligned}
$$

The conditional expectation of $\tilde{\mathcal{S}}(3)$ with respect to $P_{3}$ and $Q$ will have four terms, one for each element of the partition.

$$
\begin{aligned}
& E_{Q}\left[\tilde{S}(3) \mid B_{u u}\right]=(1+R)^{-3} E\left[S(3) \mid B_{u a}\right] \\
& =\frac{1}{(1+R)^{3} P\left(B_{u n}\right)}\left[q^{3} s^{\text {unu }}+q^{2}(1-q) s^{\text {ned }}\right]
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{q^{2}(1+R)^{3}} q^{2}\left[q^{s^{n u}}(1+u)\right. \\
& \left.\quad+(1-q) \operatorname{sun}^{n}(1+\Delta)\right] \\
& =\frac{s^{n u}}{(1+R)^{3}}[q(1+u)+(1-q)(1+D)] \\
& =\frac{s^{n u}}{(1+R)^{3}}(1+R) \\
& =\frac{s^{n u}}{(1+R)^{2}}
\end{aligned}
$$

Similarly

$$
\begin{aligned}
& E_{Q}\left[\tilde{S}(3) \mid B_{u d}\right]=\frac{S^{u d}}{(1+R)^{2}} \\
& E_{Q}\left[\tilde{S}(3) \mid B_{d u}\right]=\frac{S^{d u}}{(1+R)^{2}} \\
& E_{Q}\left[\tilde{S}(3) \mid B_{d d}\right]=\frac{S^{d d}}{(1+R)^{2}}
\end{aligned}
$$

It follows that

$$
E_{Q}\left[\tilde{S}(3) \mid P_{2}\right]=\tilde{S}(2)
$$

So it has been shown that

$$
\begin{aligned}
& E_{Q}\left[\tilde{S}(1) \mid Q_{0}\right]=S(0) \\
& E_{Q}\left[\tilde{S}(2) \mid Q_{1}\right]=\tilde{S}(1) \\
& E_{Q}\left[\tilde{S}(3) \mid P_{2}\right]=S(2)
\end{aligned}
$$

This result is actually general and can be summarized as follows.

For a sequence of random variables,

$$
\{M(n)\}_{n \leqslant N}
$$

defined on $\Omega$, is a martingale of the fittration

$$
\left\{P_{n}\right\}_{n \leqslant N}
$$

and distribution $P$ if

$$
E_{p}\left[M(n) \mid Q_{n-1}\right]=M(n)
$$

This definition call $\left\{p_{n} \xi_{n} \leqslant 1\right.$ a filtration. This does not allign with past definitions which require a Fitration to be a sequence of $\sigma$-fields. The $\beta_{n}$ discussed here cre subsets of a 6-field but the author appears to be simplifying the presentation by omitting this techicality

## Self Financing Portfolio

Suppose a portfolio is constructed with an investment of U(0) and $X(1)$ units of an asset $s(0)$ at $t=0$. It follows that

$$
\begin{aligned}
U(0)=x(1) S(0)+y(1) A(0) \\
\Rightarrow y(1)=\frac{U(0)-x(1) S(0)}{A(0)}
\end{aligned}
$$

so y(1)A(0) is borrowed or depositied depending on the sign of y(1).

At the second and third steps the portfolio is adjusted by choosing $x(2)$ and $x(3)$ and adjusting $y^{(1)}$ and $y(2)$ in the following manner

$$
y(2)=\frac{v_{x y}(1)-x(2) S(1)}{A(1)}
$$

$$
y(3)=\frac{U_{x y}(2)-x(3) S(2)}{A(2)}
$$

Here $y(n)$ and $x(n)$ are candows variables so there are two values $\left\{x^{u}(2), x^{l}(2)\right\},\left\{x^{u}(3), x^{c}(3)\right\}$ and $\left\{y^{u}(2), y^{d}(2)\right\},\left\{y^{u}(3), y^{d}(3)\right\}$

This portfolio is said to follow the self financing principle since no funds other than $U(0)$ are contributed to the portfolio and any subsequent adjustments to $x(n)$ are compensated by adjustments in $y(n)$.
Next it will be shown that the discounded portfolio that uses this strategy is a martingale wnder the risk-neutral distribution.

First consider the conditional
expectation of $\tilde{U}_{x y}(1)$ with respect to $P_{0}$ and $Q$, recall that

$$
\begin{aligned}
& \quad P\left(P_{0}\right)=P(\Omega)=1 \\
& \quad E_{Q}\left[\tilde{U}_{x y}(1)\left[P_{0}\right]=\frac{1}{P\left(Q_{0}\right)(1+R)}\left\{q \left[x(1) s^{u}\right.\right.\right. \\
& \left.+y(1) A(1)]+(1-q)\left[x(1) s^{d}+y(1) A(1)\right]\right\} \\
& =\frac{1}{(1+R)}\left\{x(1)\left[q s^{u}+(1-q) s^{d}\right]\right. \\
& \quad+y(1) A(1)[q+(1-q)] \\
& =\frac{x(1)}{1+R}[q s(0)(1+u)+(1-q) s(0)(1+0)] \\
& \quad+\frac{y(1)}{1+R} A(0)(1+R) \\
& =\frac{x(1) s(0)[q(1+u)+(1-q)(1+D)]+y(1) A(0)}{1+R} \\
& =x(1) s(0)+y(1) A(0)
\end{aligned}
$$

$$
=U(0)
$$

Thus

$$
E_{Q}\left[\tilde{U}_{x y}(1) \mid P_{0}\right]=U(0)
$$

Next consider

$$
Q_{1}=\left\{B_{n}, B_{d}\right\}
$$

where

$$
\begin{array}{ll}
P\left(B_{u}\right)=q & P\left(B_{d}\right)=1-q \\
P(u u)=q^{2} & P(u d)=q(1-q)
\end{array}
$$

The condional expectation of $\tilde{U}_{x y}(2)$ with respect to $P_{2}$ and $Q$ has two components, The $B_{u}$ component is given by,

$$
\begin{aligned}
& E_{Q}\left[\tilde{U}_{x y}(z) \mid B_{u}\right]=\frac{1}{P\left(B_{u}\right)(1+R)^{2}}\{ \\
& q^{2}\left[x^{u}(2) s^{u u}+y^{u}(2) A(2)\right] \\
& +q^{\left.(1-\varphi)\left[x^{u}(2) s^{u d}+y^{u}(2) A(2)\right]\right\}}
\end{aligned}
$$

$$
\begin{aligned}
= & \frac{1}{q(1+R)^{2}}\left\{x^{u}(2)\left[q^{2} s^{u n}+q(1-q) s^{u d}\right]\right. \\
= & \frac{1}{(1+R)^{2}} x^{u}(2)\left[q^{u}(2) A(2)\left[q^{2}+q(1-q)\right]\right\} \\
& +\frac{y^{u}(2)}{(1+R)^{2}} A(1)(1+R) \\
= & \frac{x^{u}(2)}{(1+R)^{2}} s^{u}\left[q(1+q) s^{u}(1+D)\right] \\
& +\frac{y^{u}(2)}{1+R} A(1) \\
= & \frac{1}{1+R}\left[x^{u}(2) s^{u}+y^{u}(2) A(1)\right] \\
= & \tilde{U}^{u}(1)
\end{aligned}
$$

The last step asswmes the portfolio is self firancing.

$$
E_{Q}\left[\tilde{U}_{x y}(2) \mid B_{u}\right]=\tilde{U}^{u}(1)
$$

## similarly

$$
E_{Q}\left[\tilde{U}_{x y}(z) \mid B_{d}\right]=\tilde{U}^{d}(1)
$$

so that

$$
E\left[\tilde{U}_{x y}(2) \mid P_{1}\right]=\tilde{U}_{x y}(1)
$$

The proceechre is similar for the third step. Thus it follows that

$$
E_{Q}\left[\tilde{U}_{x y}(n) \mid P_{n-1}\right]=\tilde{U}_{x y}(n-1)
$$

Thus the discounted self firancing portfolio is a martingale with respect to the risk-neutral distribution.

A final property of the discounted self financing portfolio that will be shown that for $n=0,1,2,3$

$$
E_{Q}\left[\tilde{U}_{x y}(n)\right]=U(0)
$$

This result will imply that tre price of a European call option is gruen by

$$
C(0)=\frac{1}{(1+R)^{3}} E_{Q}\left[(s(3)-k)^{+}\right]
$$

This result was shown previously for $n=1$, using $P\left(P_{0}\right)=1$

$$
\begin{aligned}
E_{Q} & {\left[\tilde{U}_{x y}(1) \mid P_{0}\right]=U(0) } \\
= & \frac{1}{P\left(Q_{0}\right)(1+R)}\left\{q\left[x(1) S^{u}+y(1) A(1)\right]\right. \\
& \left.+(1-q)\left[x(1) S^{d}+y(1) A(1)\right]\right\} \\
= & (1+R)^{-1}\left\{q\left[x(1) S^{u}+y(1) A(1)\right]\right. \\
& \left.+(1-q)\left[x(1) S^{d}+y(1) A(1)\right]\right\} \\
= & (1-R)^{-1}\left[q U^{u}+(1-q) U^{d}\right] \\
= & E_{Q}\left[\tilde{U}_{x y}(1)\right]
\end{aligned}
$$

Next it will be proven for $n=2$ to see the pattern followed by the general solution,

$$
\begin{aligned}
E_{Q} & {\left[\tilde{U}_{x y}(2)\right]=(1+R)^{-2}\left[P(u u) U^{u n}\right.} \\
+ & \left.P(u d) U^{d d}+P(d u) U^{d u}+P(d d) U^{d d}\right] \\
= & (1+R)^{-2}\left[q^{2} U^{u n}+q(1-q) U^{u d}\right. \\
& \left.+q(1-q) U^{d u}+(1-q)^{2} U^{d d}\right] \\
= & (1+R)^{-2} q\left[q U^{u n}+(1-q) U^{u d}\right] \\
& +(1+R)^{-2}(1-q)\left[q U^{d u}+(1-q) U^{d d}\right]
\end{aligned}
$$

Consider the first term,

$$
\begin{gathered}
q U^{u k}+(1-q) U^{u d}=q\left[x^{u}(2) s^{u n}\right. \\
\left.+y^{u}(2) A(2)\right]+(1-q)\left[x^{u}(2) s^{u d}\right. \\
+y^{u}(2) A(2) \\
=x^{u}(2)\left[q^{u k}+(1-q) s^{u d}\right] \\
+y^{u}(2) A(2)(q+1-q)
\end{gathered}
$$

$$
\begin{aligned}
= & x^{u}(2)\left[q S^{u}(1+u)+(1-q) S^{u}(1+D)\right] \\
& +y^{u}(2) A(2) \\
= & x^{u}(2) S^{u}[q(1+u)+(1-q)(1+D)] \\
& +y^{u}(2) A(1)(1+R) \\
= & x^{u}(2) S^{u}(1+R)+Y^{u}(2) A(1)(1+R) \\
= & (1+R)\left[x^{u}(2) S^{u}+Y^{u}(2) A(1)\right] \\
= & (1+R) U^{u}
\end{aligned}
$$

Next consider the second term

$$
\begin{aligned}
q^{U^{d u}} & +(1-q) U^{d d}=q\left[x^{d}(2) S^{d u}\right. \\
& +y^{d(2) A(2)]}+(1-q)\left[x^{d}(2) S^{d d}\right. \\
& \left.+y^{d}(2) A(2)\right] \\
= & x^{d}(2)\left[q s^{d u}+(1-q) s^{d d}\right] \\
& +y^{d}(2) A(2)(q+1-q) \\
= & x^{d}(2)\left[q^{d}(1+u)+(1-q) s^{d}(1+D)\right]
\end{aligned}
$$

$$
\begin{aligned}
+ & y^{d}(2) A(2) \\
= & x^{d}(2) S^{d}[q(1+u)+(1-q)(1+D)] \\
& +Y^{d}(2) A(1)(1+R) \\
= & x^{d}(2) S^{d}(1+R)+Y^{d}(2) A(1)(1+R) \\
= & (1+R)\left[x^{d}(2) S^{d}+Y^{d}(2) A(1)\right] \\
= & (1+R) U^{d}
\end{aligned}
$$

Putting things together

$$
\begin{aligned}
E_{Q}\left[\tilde{U}_{x y}(2)\right]= & (1+R)^{-2} q\left[q U^{u u}+(1-q) U^{u d}\right] \\
+ & (1+R)^{-2}(1-q)\left[q U^{d u}+(1-q) U^{d d}\right] \\
= & (1+R)^{-2}\left[q(1+R) U^{u}\right. \\
& \left.+(1-q) U^{d}(1+R)\right] \\
= & (1+R)^{-1}\left[q U^{u}+(1-q) U^{d}\right] \\
= & E_{Q}\left[\tilde{U}_{x y}(1)\right] \\
= & U(0)
\end{aligned}
$$

Trus

$$
E_{Q}\left[\tilde{U}_{x y}(2)\right]=U(0)
$$

Following this proceedure it can be shown that

$$
E_{Q}\left[\tilde{U}_{x y}(n)\right]=U(0)
$$

## The Cox-Ross-Rubinstein Model (CRR)

In this section the two and three step analysis developed in previous sections will be extended to $n$-steps.
For this model it is assumed that trading occurs at a finite number of dates. The time interval between trading dates is assumed to be a constant densted $b_{y} n$. It follows that the trading times are given by

$$
t=k h
$$

where $k=1,2,3, \ldots, n$.
The sample space for this model is given by

$$
\Omega=\{u, d\}^{n}
$$

the distribution for the
model is given by,

$$
P(\omega)=p^{k}(1-p)^{n-k}
$$

where $\omega \in \Omega$ and $k=0,1,2, \ldots, n$
Each w represents a Beronoull, trial which is a sequence from $\{u, d\}$ of length $n$, $k$ represents the number of $u$ 's in the sequence.
The total number of sequences in $\Omega$ is $2^{n}$. The number of sequences, $w$, with $k$ l's is given by the binomial coeficient.

$$
\binom{\hat{n}_{k}}{k}
$$

It follows that the probability of obtaining a sequence containg $K U^{\prime}$ s is given by

$$
\binom{n}{k} p^{k}(1-p)^{n-k}
$$

For $m \leqslant n$ a partition of $\Omega$ into $2^{m}$ disjoint sets is induced where the first $m$ steps of the trial are known. Each set is denoted by an $n$-tuple subscript of u's and d's.

For example the partition where the first step is known is given by

$$
Q_{1}=\left\{B_{u}, B_{d}\right\}
$$

Here Bu contains all Berroulli trials starting with $u$ and $B_{d}$ all trials starting with C
If the first two steps are known the portition

$$
P_{2}=\left\{B_{u u}, B_{n d}, B_{d u}, B_{d d}\right\}
$$

is created where each
set in the partition contains all Bernoulli trials where the first two steps are un, ud, du and dd respectively. Also, note that the elements of $P_{1}$ and $P_{2}$ are realated

$$
\begin{aligned}
& B_{u}=B_{u u} \cup B_{u d} \\
& B_{d}=B_{d u} \cup B_{d d}
\end{aligned}
$$

This relation is true in general, namely all elements in $P_{k}$ can be written as the which of two sets in $P_{k+1}$ This can be stated formaly as a sequence of sets

$$
\left\{B_{k}\right\}_{k} \leqslant n
$$

is refining if for each $k \leqslant N \theta_{k}$ is a fonite union of sets in $P_{k+1}$.

Fix two numbers

$$
-1<D<U
$$

and define the random returns at each step by

$$
K_{k}= \begin{cases}U & \text { with probability } P \\ D & \text { with probability } 1-P\end{cases}
$$

The random variables

$$
\left\{k_{k}: k=1,2,3, \ldots, n\right\}
$$

defined on the event space

$$
\Omega=\{u, d\}^{n}
$$

are assumed independent. This can be stated formally, for any subset of unique indices of $k,\left\{i_{1}, i_{2}, \ldots, i_{m}\right\}$ of the indices $\{1,2,3, \ldots, n\}$ and for any real numbers $\left\{x_{1}, x_{2}, \ldots, x_{k}\right\}$
$P\left[\bigcup_{j=1}^{m}\left\{k_{i j}=x_{j}\right\}\right]=\prod_{j=1}^{m} P\left(k_{i j}=x_{j}\right)$

It is assumed that the initral value of the asset, $S(0)$, is known then

$$
S(n)=S(n-1)\left(1+K_{n}\right)
$$

this means that the asset prices follow recombining binomial tree.

Similarly the risk-free investment is given by

$$
A(n)=A(n-1)(1+R)
$$

Where $A(0)$ is known. To avoid arbitrage it is assumed that

$$
D<R<u
$$

just as in the single step case.

## Theorem

sequence of asset prices in the binomial model is
a martingale with respect to the fittration $P_{n}$ and risk-neutral probability $Q$

## Proof

consider the fittration,

$$
P_{n}=\left\{B_{u u \ldots n}, \ldots, B_{d d \cdots d}\right\}
$$

To widerstand how knowledge of $P_{n}$ impacts the calculation consider $Q_{1}$

$$
B_{1}=\left\{B_{n}, B_{d}\right\}
$$

$\begin{array}{lllll}0 & 1 & 2 & 3\end{array}$
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-319.jpg?height=604&width=687&top_left_y=1418&top_left_x=519)

In the graph all outcomes which follow from knowledge of Bu are shown in red and knowledge of Bd are shown in green. Smilarly

$$
\theta_{2}=\left\{B_{u u}, B_{u d}, B_{d u}, B_{d d}\right\}
$$

$\begin{array}{llllll}t & 0 & 1 & 2 & 3 & 4\end{array}$
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-320.jpg?height=1094&width=973&top_left_y=884&top_left_x=386)

Here the outcomes resulting from knowledge of Bun are shown in red, Bud in green Bdu in blue and Bad in purple.
Note that the following relation exists betwen the howing knowledge of a partion element at a previous step and the rext step

$$
\begin{aligned}
& B_{u}=B_{w u} \cup B_{u d} \\
& B_{d}=B_{d u} \cup B_{d d}
\end{aligned}
$$

Also, note that at the next step for each element of the partition there are two possible outcomes and that

$$
P\left(B_{u}\right)=q \quad P\left(B_{c}\right)=1-q
$$

and

$$
\begin{array}{ll}
P\left(B_{\text {un }}\right)=q^{2} & P\left(B_{\text {ud }}\right)=q(1-q) \\
P\left(B_{\text {du }}\right)=q(1-q) & P\left(B_{\text {dd }}\right)=(1-q)^{2}
\end{array}
$$

Next nole that for probability 91

$$
\begin{gathered}
P\left(B_{u}\right)=P(u)=q \\
P\left(B_{d}\right)=P(d)=1-q \\
P\left(B_{w a}\right)=P(u u)=P\left(B_{u}\right) q \\
P\left(B_{u d}\right)=P(u d)=P\left(B_{u}\right)(1-q) \\
P\left(B_{d u}\right)=P(d u)=P\left(B_{d}\right) q \\
P\left(B_{d d}\right)=P(d d)=P\left(B_{d}\right)(1-q)
\end{gathered}
$$

Thus

$$
\begin{aligned}
& P\left(n u \mid B_{u}\right)=\frac{P(n \omega)}{P\left(B_{u}\right)}=9 \\
& P\left(n d \mid B_{u}\right)=\frac{P(n d)}{P\left(B_{u}\right)}=1-9
\end{aligned}
$$

To generalize this result let

$$
B_{n} \in P_{n}
$$

and let $s(n)$ denote the known asset price at the n'th step, then

$$
P(S(n))=P\left(B_{n}\right)
$$

At step $n+1$ there are two possible asset prices

$$
s(n+1)=\left\{\begin{array}{l}
s^{u}(n+1)=s(n)(1+u) \\
s^{d}(n+1)=s(n)(1+D)
\end{array}\right.
$$

where

$$
\begin{aligned}
P\left(s^{u}(n+1)\right) & =P(s(n)) q \\
& =P\left(B_{n}\right) q
\end{aligned}
$$

$$
\begin{aligned}
P\left(s^{d}(n+1)\right) & =P(s(n))(q-1) \\
& =P\left(B_{n}\right)(q-1)
\end{aligned}
$$

using these results groes

$$
\begin{aligned}
E_{Q} & {\left[s(n+1) \mid B_{n}\right]=P\left(s^{u}(n+1) \mid B_{n}\right) s^{u}(n+1) } \\
+ & P\left(s^{d}(n+1)\left(B_{n}\right) s^{d}(n+1)\right. \\
= & \frac{P\left(B_{n}\right) q}{P\left(B_{n}\right)} s(n)(1+u) \\
& +\frac{P\left(B_{n}\right)(q-1) s(n)(1+D)}{P\left(B_{n}\right)} \\
= & q s(n)(1+u)+(q-1) s(n)(1+D) \\
= & s(n)[q(1+u)+(q-1)(1+0)]
\end{aligned}
$$

using the risk-neutral probabilites

$$
q=\frac{R-D}{u-D} \quad 1-q=\frac{u-R}{u-D}
$$

$$
\begin{aligned}
& \text { gives } \\
& E_{Q}\left[S(n+1) \mid B_{n}\right]=S(n)\left[\frac{(1-u)(R-D)}{u-D}\right. \\
& \left.\quad+\frac{(1+D)(u-R)}{u-D}\right] \\
& =\frac{S(n)}{u-D}\left(R^{\prime}-D+R u-D \tilde{u}+u-R+L D-R D\right) \\
& =\frac{S(n)}{u-D}[(u-D)+R(u-D)] \\
& =\frac{S(n)(1+R)}{\operatorname{E}} \\
& \Rightarrow \frac{E_{Q}\left[S(n+1) \mid B_{n}\right]}{(1+R)^{n+1}}=\frac{S(n)(1+R)}{(1+R)^{n+1}} \\
& \Rightarrow E_{Q}\left[\tilde{S}(n+1)\left[B_{n}\right]=\tilde{S}(n)\right.
\end{aligned}
$$

Since $B_{n}$ is an arbitray element of $Q_{n}$ it follows
that

$$
E_{Q}\left[\tilde{S}(n+1) \mid Q_{n}\right]=\tilde{S}(n)
$$

which is the desired result that S(n+1)is a martigale with respect to the risk-neutral probability and filtration on

## Theorem

In the binomial model the discounted prices of a derivative security with pay off $H(n)$ are given, under tre matringale probability by the recursive relations

$$
\tilde{H}(n-1)=E_{Q}\left[\tilde{H}(n) \mid P_{n-1}\right]
$$

for $n=1,2, \ldots, N$ the intial price is given by

$$
H(O)=(1+R)^{-N} E_{Q}(H(N))
$$

## Proof

First consider the relation

$$
\tilde{H}(n-1)=E_{Q}\left[\tilde{H}(n) \mid P_{n-1}\right]
$$

let $B_{n-1} \in P_{n-1}$. The replicating
portfolio for $\tilde{H}(n)$ is given by,

$$
\tilde{H}(n)=x(n) \tilde{S}(n)+y(n) A(0)
$$

Now $x(n)$ and $y(n)$ are constant over $B_{n-1}$, so

$$
\begin{gathered}
E_{Q}\left[\tilde{H}(n) \mid B_{n-1}\right]=x(n) E_{Q}\left[\tilde{S}(n) \mid B_{n-1}\right] \\
+y(n) A(0)
\end{gathered}
$$

but provously it was shown

$$
E_{Q}\left[\tilde{S}(n) \mid B_{n-1}\right]=\tilde{S}(n-1)
$$

so

$$
\begin{gathered}
E_{a}\left[\tilde{H}(n) \mid B_{n-1}\right]=x(n) \tilde{S}(n-1) \\
+y(n) A(0)
\end{gathered}
$$

but

$$
\tilde{H}(n-1)=x(n) \tilde{S}(n-1)+y(n) A(0)
$$

thus

$$
E_{Q}\left[\tilde{H}(n)\left(B_{n-1}\right]=\tilde{H}(n-1)\right.
$$

Since $B_{n-1}$ is arbitrary it follows that

$$
E_{Q}\left[\tilde{H}(n) \mid P_{n-1}\right]=\tilde{H}(n-1)
$$

Next the relation

$$
H(0)=E_{Q}[\tilde{H}(n)]
$$

will be proven.
From the privides relation, let $B \in P_{n-1}$ then from the definition of condition expedation,

$$
\begin{aligned}
& E_{Q}[\tilde{H}(n)]=\sum_{B \in P_{n-1}} E_{Q}[\tilde{H}(n) \mid B] Q(B) \\
& =\sum_{B \in P_{n-1}} \tilde{H}(n-1, B) Q(B) \\
& =E_{Q}[\tilde{H}(n-1)]
\end{aligned}
$$

Thus

$$
E_{Q}[\tilde{t}(n)]=E_{Q}[\tilde{t} \mid(n-1)]
$$

Now if $n=1$

$$
\begin{aligned}
E_{Q}[\tilde{H}(1)] & =E_{Q}[\tilde{H}(0)] \\
& =H(0)
\end{aligned}
$$

and

$$
E_{Q}[\tilde{H}(2)]=E_{Q}[\tilde{H}(1)]=H(0)
$$

It follows that

$$
\begin{aligned}
E_{Q}[\tilde{H}(n)] & =E_{Q}[\tilde{H}(n-1)] \\
& =E_{Q}[\tilde{H}(n-2)] \\
& =\cdots \\
& =H(0)
\end{aligned}
$$

Thus

$$
E_{a}[\tilde{H}(n)]=H(0)
$$

From this relation a general expression for the for $H(0)$ can be denived.

If the random variable $H(n)$ is assumed to be a function of $s(n)$ then

$$
H(n)=h(S(n))
$$

If follows that

$$
H(n)=h\left(s(0)(1+u)^{\bar{x}}(1+D)^{n-\bar{x}}\right.
$$

where $\bar{X}$ is a random variable representing the number of upward price movements after $n$ steps.
using the previously derived relation the derivative security price is given by

$$
\begin{aligned}
H(0)= & E_{Q}[\tilde{H}(n)] \\
= & (1+R)^{-n} \sum_{m=1}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} \\
& h(s(0))(1+u)^{m}(1+D)^{n-m}
\end{aligned}
$$

## European Call option Prrce from CCR

Consider a European call option with stake price $K$. The payoff function is given by

$$
C(n)=(s(n)-k)^{+}
$$

The price of the option is given by

$$
\begin{aligned}
& c(0)=(1+R)^{-n} \sum_{m=1}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} \\
& {\left[\operatorname{scos}(1+u)^{m}(1+D)^{n-m}-k\right]^{+}} \\
& \text {If } \quad \operatorname{sox}(1+u)^{m}(1+D)^{n-m} \leqslant k
\end{aligned}
$$

the payoff will be zero. Let

$$
l=\min \left[m: \operatorname{sco}(1+u)^{m}(1+D)^{n-m}>k\right]
$$

then

$$
\begin{aligned}
c(0)= & (1+R)^{-n} \sum_{m=1}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} \\
& {\left[s(0)(1+u)^{m}(1+D)^{n-m}-k\right]^{+} } \\
= & (1+R)^{-n} \sum_{m=l}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} \\
& {\left[\operatorname{scox}(1+u)^{m}(1+D)^{n-m}\right]-k } \\
= & (1+R)^{-n} \sum_{m=l}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} \\
& \operatorname{scox}(1+u)^{m}(1+D)^{n-m} \\
& -(1+R)^{-n} k \sum_{m=l}^{n}\binom{n}{m} q^{m}(1-q)^{n-m}
\end{aligned}
$$

The cumulative distribution function for the binomial distribution is given by

$$
F_{q}^{n}(s)=\sum_{m=0}^{s}\binom{n}{m} q^{m}(1-q)^{n-m}
$$

it follows that

$$
\sum_{m=l}^{n}\binom{n}{m} q^{m}(1-q)^{n-m}=1-F_{q}^{n}(l-1)
$$

Consider the first term

$$
\begin{aligned}
(1+R)^{-n} \sum_{m=e}^{n}\binom{n}{m} q^{m}(1-q)^{n-m} & \\
& \operatorname{scox}(1+u)^{m}(1+\Delta)^{n-m} \\
= & \sum_{m=e}^{n}\binom{n}{m}\left[q \frac{(1+u)}{1+R}\right]^{m}\left[(1-q) \frac{(1+D)}{1+R}\right]^{n-m}
\end{aligned}
$$

let

$$
q_{1}=q \frac{(1+u)}{1+R}
$$

then

$$
1-q_{1}=\frac{(u-D)(1+R)}{(u-D)(1+R)}-\frac{(R-D)}{u-D} \frac{(1+C)}{1+R}
$$

$$
\begin{aligned}
& =\frac{U-D+\hat{R} U-R D-R+R-U R+U D}{(U-D)(1+R)} \\
& =\frac{U-R+U D-R D}{(U-D)(1+R)} \\
& =\frac{(U-R)(1+D)}{(U-D)(1+R)} \\
& =(1-9) \frac{(1+D)}{(1+R)}
\end{aligned}
$$

50

$$
\begin{aligned}
\sum_{m=l}^{n} & \binom{n}{m}\left[q \frac{(1+u)}{1+R}\right]^{m}\left[(1-q) \frac{(1+\Delta)}{1+R}\right]^{n-m} \\
& =\sum_{m=l}^{n}\binom{n}{m} q_{1}^{m}\left(1-q_{1}\right)^{n-m} \\
& =1-F_{q_{1}}^{n}(l-l)
\end{aligned}
$$

Bringing things together gives the price of a european call option

$$
\begin{aligned}
c(0)=s(0) & {\left[1-F_{q 1}^{n}(l-1)\right] } \\
& -K(1+R)^{n}\left[1-F_{q}^{n}(l-1)\right]
\end{aligned}
$$

Alternatively the complenentary or tail of the binomial distribution

$$
\begin{aligned}
\psi(l, n, r) & =1-F_{r}^{n}(l) \\
& =\sum_{k=l}^{n}\binom{n}{k} r^{k}(1-r)^{n-k}
\end{aligned}
$$

50

$$
\begin{aligned}
c(0)=s(0) & \psi\left(l-1, n, q_{1}\right) \\
& -k(1+R)^{n} \psi(l-1, n q)
\end{aligned}
$$

## Example Calculation

In this sectron an example calculation is performed for the price of a European call option using CRR.
In the previous section it was shown trat

$$
\begin{aligned}
c(0)=s(0) \psi\left(l-1, n, q_{1}\right) \\
-k(1+R)^{-n} \psi(l-1, n, q)
\end{aligned}
$$

where

$$
\begin{aligned}
& \psi(l, n, r)=\sum_{k=l}^{n}\binom{n}{k} r^{k}(1-r)^{n-k} \\
& q=\frac{R-D}{u-D} \quad q_{1}=q \frac{(1+u)}{1+R}
\end{aligned}
$$

The calculation is implimenters by the following python functions

```
def qrn(U, D, R):
    return (R - D) / (U - D)
def qrn1(q, U, R):
    return q*(1.0 + U) / (1.0 + R)
def binomial_tail_cdf(l, n, p):
    return 1.0 - binom.cdf(l, n, p)
def cutoff(S0, U, D, K, n):
    for i in range(0, n + 1):
        iU = (1.0 + U)**i
        iD = (1.0 + D)**(n - i)
        payoff = S0*iU*iD - K
        if payoff > 0:
            return i
    return n + 1
def european_call_payoff(U, D, R, S0, K, n):
    l = cutoff(S0, U, D, K, n)
    q = qrn(U, D, R)
    q1 = qrn1(q, U, R)
    \Psiq = binomial_tail_cdf(l - 1, n, q)
    \Psiq1 = binomial_tail_cdf(l - 1, n, q1)
    return S0*\Psiq1 - K*(1 + R)**(-n)*\Psiq
def delta(CU, CD, SU, SD):
    return (CU - CD) / (SU - SD)
def init_borrow(S0, C0, x):
    return C0 - S0 * x
def borrow(y, R, x1, x2, S):
    return y * (1 + R) + (x2 - x1) * S
```


## Using the following parameters

$$
\begin{array}{lll}
u=20 \% & D=-10 \% & R=10 \% \\
s(0)=100 & k=105 & n=3
\end{array}
$$

gives

$$
C(0)=23.31
$$

## Delta Hedging

Consider the position of a call option seller. For example if the parameters from the previous section are used. The option seller is given 23.31 at $t=0$ at $t=3$ if the asset price increases at each step the seller will have to pay

$$
\begin{aligned}
s \cos (1+u)^{3}-k & =(100)(1.2)^{3}-105 \\
& =67.80
\end{aligned}
$$

to the gotion buyer.
The option seller can mitigate this risk by puronasing the replicating portfolio. This strategy is called hedging.
Instead of computing the enture price tree for the option
by computing backwards from the payoff as done previously using a self finanaing portdiio.
The option prices arc computed after each step and the replicating portiolio is purchased using information from the previous step. This proceedure is more computationaly efficent since calculations are only performed as needed.

The first portfolio is computed at the first step. Recall that the amount of an asset purchase for a derivative security by replicating portfolio is given by.

$$
x(1)=\frac{c^{u}-c^{d}}{s^{u}-s^{d}}
$$

Also, recall that that the the righthand side of X(1)
is called the delta coefficient which is the namesoke of the hedging method.

Next funds are borrowed at the risk-free rate to purchace the asset at its initial price

$$
y(1)=c(0)-x(1) s(0)
$$

For the parameters used in the previous example,

$$
\begin{array}{lll}
u=20 \% & D=-10 \% & R=10 \% \\
s(0)=100 & k=105 & n=3
\end{array}
$$

The prices of the call option at $t=l$ can be computed using CRR and the possible values values of the asset at $t=1$

$$
s(1)=\left\{\begin{array}{l}
s^{u}=s(0)(1+u)=120 \\
s^{d}=s(0)(1+\Delta)=90
\end{array}\right.
$$

using the previously discused $C R R$ implementation.

$$
\begin{aligned}
& c(1)=\left\{\begin{array}{l}
c^{u}=33.94 \\
c^{d}=9.04
\end{array}\right. \\
& x(1)=0.83 \quad y(1)=-59.70
\end{aligned}
$$

The intial portfolio is given by,

$$
\begin{aligned}
U_{x y}(0) & =x(1) 5(0)+y(1) \\
& =(0.83)(100)-59.70 \\
& =23.31
\end{aligned}
$$

which is the cost of the call option. This portfolio has in effect purchased the option. Now,

The delta hedging strategy follows the asset price. so at $t=1$ assume that the price goes up, so that

$$
\begin{aligned}
s^{u} & =s(0)(1+u) \\
& =(100)(1,2) \\
& =120
\end{aligned}
$$

The option values are given by

$$
\begin{array}{ll}
\text { sule } 144 & \text { sud }=108 \\
c^{\text {ud }}=48.55 & c^{\text {ud }}=14.91
\end{array}
$$

The delta is given by

$$
x^{4}(2)=\frac{48.55-14.91}{144-108}=0.93
$$

This is an increase from the previous step of

$$
x^{4}(2)-x(1)=0.93-0.83=0.1
$$

so 0.1 units of the asset must be purchased so more money must be borrowed. This changes the form of the expression used to compute what shoud be borrowed to,
$y^{u}(2)=y\left(1 x(1+R)+\left[x(1)-x^{u}(2)\right] s^{u}\right.$
The frost term represents the loan value plus interest and the second amout of the asset purchased at the current value. It follows that

$$
y^{u}(2)=-78.18
$$

so an additional amount of

$$
\begin{aligned}
y(1)-y^{u}(2) & =-59.70+78.18 \\
& =18.48
\end{aligned}
$$

is borrowed.

The portfolio value at $t=2$ is given by

$$
U_{x y}(1)=33.94
$$

Next at $t=2$ assume that the price goes down.

$$
s^{u d}=10 \gamma
$$

The option values are given by

$$
\begin{array}{ll}
s^{\text {udu }}=129.6 & s^{\text {ndd }}=97.2 \\
c^{\text {udu }}=24.60 & c^{\text {lnd }}=0.0 \\
x^{\text {ud }}(3)=0.76 & y^{\text {ud }}(3)=-67.09
\end{array}
$$

At this step

$$
x^{4 c}(3)-x^{4 c}(2)=0.76-0.93=-0.17
$$

of the asset is sold at $s^{\text {ud }}=108$ and amount of the loan given by

$$
\begin{aligned}
y^{4}(2)-y^{4 d}(3) & =-78.18+67.09 \\
& =-11.09
\end{aligned}
$$

is paid off
The portfolio value is given by

$$
U_{x y}(2)=14.91
$$

At the next and final step assume the asset price increases

$$
\begin{aligned}
\text { sudu } & =(100)(1.2)^{2}(.9) \\
& =129.60
\end{aligned}
$$

Now the strike price for the option is given by

$$
K=105
$$

The payout of the option is

$$
\begin{aligned}
\text { sudu }-K & =129.60-105 \\
& =24.60
\end{aligned}
$$

so the option seller must pay the buyer of the option

$$
24.60
$$

The amount owed to the bank is

$$
(67.09)(1.1)=73,80
$$

so in total the option seller owes the bank and option owner

$$
24.60+73.80=98.40
$$

the amount of the asset owned is

$$
x^{4 d}(3)=0.76
$$

the value of the owned asset is

$$
(0.76)(129.60)=98.50
$$

This is enough to pay off the loan with 10 L to spare

## Detta Hedging Summary

In the previous section detta hedsing was introduced by working through an example numerically here the algorithm will be reviewed.

Detta hedging albus the seller of a derivative security to insure against a payout by borrowing money to purchase the underlying asset using the securitys replicating portfolio. In the event of an option payout the seller will lose no money.
The algorithm follows the trajectory of the asset through the event space rebalancing at each step using past information. An example trajectory through the event
space is shown in diagram below,
$t \quad 0$
$\begin{array}{lll}1 & 2 & 3\end{array}$
![](https://cdn.mathpix.com/cropped/2025_09_20_03ad84c40ec543a25ba3g-349.jpg?height=1196&width=1142&top_left_y=443&top_left_x=332)

The trajectory followed by the asset price is shown in green

An investor wishes to sell a European call option with strike price $K$ with $S(0), U, D$ and $R$ known.
At $t=0$ the option seller uses CRR to price the option with the given parameters. This price is denoted by $C(0)$. The option seller sells the option raising $C(0)$ in cash.

Next a replicating for the option is computed using $\delta$ to determine the amount of the asset to purchace,

$$
x(1)=\frac{c^{u}-c^{d}}{s^{u}-s^{d}}
$$

where $c^{u}$ and $c^{c}$ are computed using CRR over the partitions $B_{u}$ and $B_{d}$ respectively

Next an amout of money is borrowed so that $x(1)$ of the asset can be purchased at $t=0$ and price $S(0)$, also it is assumed that,

$$
y(1)=c(0)-x(1) s(0)
$$

Note that if $y(1)<0$ funds are borrowed at the risk free interest rate and deposited if $y(1)>0$.
Note that

$$
\begin{aligned}
U_{x y}(0) & =x(1) S(0)+y(1) \\
& =C(0)
\end{aligned}
$$

since this is the replicating portfolio.
Now at the step $t=1$. From the dagram it is seen that the asset price is $\mathrm{s}^{4}$.

CRR is used to compute chu and cud, so

$$
x(2)=\frac{c^{u m}-c^{u d}}{s^{u m}-s^{u d}}
$$

If $x(2)>x(1)$ more monely is borrowed at the risk-free interest rate to purchace $x(2)-x(1)$ of the asset at price $s^{u}$. If $x(1)>x(2)$ the difference $x(1)-x(2)$ is deposited at the risk-free interest rate The expression for $y(2)$ is
$y(2)=y(1)(1+R)+(x(1)-x(2)) s^{u}$
The first term accuonts for the terest from the first step.
The replicating portfolco for $t=1$ is given by

$$
U_{x y}(1)=x(2) s^{u}+y(2)
$$

At the next $s t e p, t=2$, the stock goes down to sud The portfolio is updated following the same proceedure used previously

$$
x(3)=\frac{c^{u d u}-c^{u d d}}{s^{u d u}-s^{u d d}}
$$

and
$y(3)=y(2)(1+R)+(x(2)-x(3)) s^{\text {ud }}$
the replicating portfolio is given by

$$
U_{x y}(2)=x(3) s^{\text {ud }}+y(3)
$$

At the final step, $t=3$, the option is execised at the price sudu. If

$$
c^{\text {ud } u}=\text { sudle }^{-k}>0
$$

an amount sudu $-k$ is paid to the buyer of the option. If

$$
s^{\text {udu }}-k<0
$$

then

$$
c^{\text {codu }}=0
$$

So the option buyer gets
nothing
The final value of the replicating portfolio is given by

$$
U_{x y}(3)=x(3) s^{u d u}+y(3)
$$

These assets are used to settle any obligations the option seller incurred diring the process.

## Multi-Step General models

## Partitions and Conditioning

Assume a finite sample space

$$
\Omega=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{n}\right\}
$$

Define a probability on $\Omega$ by

$$
P(\omega) \geqslant 0
$$

where

$$
P(A)=\sum_{\omega \in A} P(\omega)
$$

for $A \subset \Omega$. Also

$$
P(\Omega)=1
$$

Define a new probability

$$
P_{B}(\omega)=\frac{P(\omega)}{P(\beta)}
$$

for $\omega \in B$ and 0 if $\omega \notin B$

It follows that

$$
P_{B}(B)=\frac{P(B)}{P(B)}=1
$$

For any $A C \Omega$ the conditional probability of $A$ given $B$ is given by

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}
$$

Let $X$ be a random variable and $B C \Omega$ where $B \neq \phi$ be any event. The conditional expectation of I given B is defined by

$$
\begin{aligned}
E[\bar{x} \mid B] & =\sum_{\omega \in \Omega} \bar{x}(\omega) P_{B}(\omega) \\
& =\sum_{\omega \in \Omega} \bar{x}(\omega) \frac{P(\{\omega\} \cap B)}{P(B)} \\
& =\sum_{\omega \in B} \bar{x}(\omega) \frac{P(\omega)}{P(B)}
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{1}{P(B)} \sum_{\omega \in B} \bar{X}(\omega) P(\omega) \\
& =\frac{1}{P(B)} \sum_{\omega \in \Omega} \bar{X}(\omega) \underline{1}_{\sigma}(\omega) P(\omega) \\
& =\frac{1}{P(B)} E\left[\bar{X}(\omega) \underline{1}_{B}(\omega)\right]
\end{aligned}
$$

where $\underline{1}_{B}(\omega)$ is the indicator function

$$
\underline{I}_{B}(\omega)= \begin{cases}1 & \omega \in B \\ 0 & \omega \in B\end{cases}
$$

Thus

$$
E[X \mid B]=\frac{1}{P(B)} E\left[1_{B} X\right]
$$

Recall that a partition of the event space $\Omega$ is defined by

$$
P=\left\{B_{i}: i<k\right\}
$$

where

$$
B_{i} \cap B_{j}=\varnothing
$$

for $i \neq j$ and

$$
\bigcup_{c}^{k} B_{i}=\Omega
$$

It follows that the conditional expectation of the random variable I with respect to the partition $Q$ is a random variable defined by

$$
E[X \mid P]: \Omega \rightarrow \mathbb{R}
$$

with a constant value of $E\left[X \mid B_{i}\right]$ at $\omega \in B_{i}$ for each $i \leqslant k$.

For $\omega \in B_{i}$ for each $B_{i}$ it follows that

$$
\begin{aligned}
E[X \mid P J(\omega) & =E\left[X \mid B_{i}\right] \\
& =\frac{1}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} X\right]
\end{aligned}
$$

It follows that

$$
E[X \mid P]=\sum_{i=1}^{K} \frac{\mathbb{1}_{B_{i}}}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right]
$$

A G-field, F, can be constructed from the partition $P$ by forming all possible unions of the elements of $P$ and adding the empty set

$$
\mathcal{F}=\{\varnothing\} \cup\left\{\bigcup_{i} B_{i}:\left\{B_{i}\right\} \subset P\right\}
$$

This proceedure can be reversed The minimal non-empty elements of a field $f$ are its atoms which together form a partition $P$ of $R$.

If $\bar{X}$ is an arbitrary random variable on $\Omega$ and $I$ is another random variable with possible values $\left\{y_{1}, y_{2}, \ldots, y_{k}\right\}$ then the conditional expectation
$E[X \mid I]$ is the conditional expectation of X with respect to the partition

$$
P=\left\{B_{i}\right\}_{i \leqslant k}
$$

## where

$$
B_{i}=\left\{\omega: I(\omega)=y_{i}\right\}
$$

This is written as

$$
E[\bar{X} \mid \bar{Y}]=E\left[\bar{X} \mid \bar{I}=y_{i}\right]
$$

If $I=y_{i}$ for $c=1,2, \ldots, k$.
Note that if $\bar{I}$ is constant on a subset of $\Omega$ then $E[X \mid I]$ is constant on the subset, and the values of E[XIV] depent on the subsets on which I is constant and not on the actual values of $I$. It follows that if two random variables, $I$ and $W$, define the same
partition will have the same conditional expectations.

$$
E[\bar{X} \mid Y]=E[\bar{X} \mid \omega]
$$

Likewise for two random variables $U$ and $Z$ that define different partitions

$$
E[\bar{x} \mid \vee] \neq E[\bar{x} \mid Z]
$$

## Properties of Conditional Expectation

## Linearity

Define the random corrable,

$$
\bar{x}=a \bar{x}_{1}+a \bar{x}_{2}
$$

where $I_{1}$ and $I_{2}$ are random variables and $a, b \in \mathbb{R}$ then

$$
\begin{aligned}
E[X \mid \eta] & =E\left[a X_{1}+b X_{2} \mid \eta\right] \\
& =a E\left[X_{1} \mid I\right]+b E\left[X_{2} \mid I\right]
\end{aligned}
$$

Proof

$$
\begin{aligned}
E\left[a \bar{X}_{1}\right. & \left.+b \bar{X}_{2} \mid \bar{I}\right] \\
= & \sum_{\omega \in \Omega}\left(a \bar{X}_{1}(\omega)+b \bar{X}_{2}(\omega)\right) P_{B}(\omega) \\
= & a \sum_{\omega \in \Omega} \bar{X}_{1}(\omega) P_{B}(\omega) \\
& +b \sum_{\omega \in \Omega} \bar{X}_{2}(\omega) P_{B}(\omega)
\end{aligned}
$$

$$
=a E\left[\bar{X}_{1} \mid \bar{Y}\right]+b E\left[\bar{X}_{2} \mid \bar{Y}\right]
$$

## Expectation of Conditional Expectation

The expectation of the conditional expectation of a random variable I with respect to I is given by

$$
E[E[\Phi \mid \bar{y}]]=E[\bar{x}]
$$

## Proof

Let $B_{i}=\left\{\omega: I(\omega)=y_{i}\right\}$, then

$$
E[E[X \mid Y]]=\sum_{i} E\left[X \mid B_{i}\right] P\left(B_{i}\right)
$$

using the previous result

$$
E\left[\bar{X}\left(B_{i}\right]=\frac{1}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right]\right.
$$

groes

$$
\begin{aligned}
E[E[X \mid Y]] & =\sum_{i} E\left[X \mid B_{i}\right] P\left(B_{i}\right) \\
& =\sum_{i} \frac{1}{P\left(B_{i}\right)} E\left[I_{B_{i}} \bar{X}\right] P\left(B_{i}\right) \\
& =\sum_{i} E\left[I_{1} B_{i} \boxtimes\right]
\end{aligned}
$$

by linearity

$$
\begin{aligned}
\sum_{i} E\left[\mathbb{1}_{B i} \bar{X}\right] & =E\left[\sum_{i} \mathbb{1}_{B i} \bar{X}\right] \\
& =E\left[\mathbb{X} \sum_{i} \mathbb{1}_{B i}\right]
\end{aligned}
$$

but

$$
\sum_{c} 1_{B_{i}}=1
$$

thus the desired result is obtained

$$
E[E[\underline{x} \mid \bar{y}]]=E[\bar{x}]
$$

## Definition

Given two partitions $Q_{1}$ and $P_{2}$. $P_{2}$ is said to be finer than $P_{1}$ is $P_{1}$ and be written as a union of elements from $P_{2}$. Now $P_{1}$ is defined by $s(1)$ and $P_{2}$ by $s(2)$. If the price tree is not recombing then knowledge of $S(2)$ determines the value of s(i). Thus $B_{2}$ contains more information tran $P_{1}$.

If the asset price tree is recombing, the partition defined by $S(2)$ is not finer than the partition defined by $S(1)$. This is because there are two possible values for sa) given S(2). This can be corrected by defining the s(2) partition such that both $S(1)$ and $S(2)$ are constant.

This is not the case in previous discussions.

## Tower Property

Consider the descrete random variables $\bar{I}$ and $\mathbb{Z}$. Assume trat I defines a finer partition than $\mathbb{Z}$. Then

$$
E[E[\bar{x} \mid \bar{y}] \mid \mathbb{R}]=E[\bar{x} \mid \mathbb{R}]
$$

## Proof

Define the two partitions

$$
C_{i}=\left\{\mathbb{Z}=z_{i}\right\} \quad B_{i}=\left\{\bar{Y}=y_{i}\right\}
$$

The partition $\left\{B_{i}\right\}$ is finer so for each j we can find a collection of set $I_{j}$ indices such that

$$
C_{j}=\bigcup_{i \in I_{j}} B_{i}
$$

Now for $\omega \in C_{j}$

$$
E[E[X \mid Y] \mid Z](\omega)=\frac{1}{P\left(C_{j}\right)} E\left[\mathbb{1}_{C_{j}} E[X \mid Y]\right]
$$

But

$$
E[X \mid Y](\omega)=\frac{1}{P\left(B_{i}\right)} E\left[\underline{1}_{B_{i}} \bar{X}\right]
$$

Now since

$$
C_{j}=\bigcup_{i \in I_{j}} B_{i}
$$

it follows that,

$$
\begin{gathered}
\mathbb{1}_{c_{j}} E[\bar{X} \mid Y]=\mathbb{1}_{c_{j}} \sum_{i \in I_{j}} \frac{\mathbb{1}_{B_{i}}}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right] \\
=\sum_{i \in I_{j}} \frac{\mathbb{1}_{c_{j}} \mathbb{1}_{B_{i}}}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right]
\end{gathered}
$$

Since

$$
B_{i} \subset C_{j}
$$

it follows that

$$
\mathbb{1}_{C_{i}} \mathbb{1}_{B_{i}}=\mathbb{1}_{B_{i}}
$$

putting things together gives

$$
\begin{aligned}
\frac{1}{P\left(C_{j}\right)} E\left[\mathbb{1}_{C_{i}} E[X \mid Y]\right] & =\frac{1}{P\left(C_{j}\right)} E\left[\sum_{i \in I_{j}} \frac{\mathbb{1}_{B_{i}}}{P\left(B_{j}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right]\right] \\
& =\frac{1}{P\left(C_{j}\right)} \sum_{i \in I_{j}} E\left[\frac{\mathbb{1}_{B_{i}}}{P\left(B_{i}\right)} E\left[\mathbb{1}_{B_{i}} \bar{X}\right]\right]
\end{aligned}
$$

The last step follows from linearily of conditional expectation. Now $E\left[\mathbb{1}_{B_{i}} \bar{X}\right]$ is a real number so

$$
\begin{aligned}
\frac{1}{P\left(C_{j}\right)} E\left[\mathbb{1}_{C_{i}} E[\bar{X} \mid \bar{Y}]\right] & \\
& =\frac{1}{P\left(C_{j}\right)} \sum_{i \in I_{j}} E \frac{E\left[\mathbb{1}_{B_{i}} \bar{X}\right]}{P\left(B_{j}\right)} E\left[\mathbb{1}_{B_{i}}\right]
\end{aligned}
$$

## Consider

$$
E\left[\underline{1}_{B_{i}}\right]=\sum_{\omega \in B_{i}} P(\omega)=P\left(B_{i}\right)
$$

thes

$$
\begin{aligned}
\frac{1}{P\left(C_{j}\right)} E\left[\underline{1}_{C_{i}} E[X \mid \bar{Y}]\right] & \\
& =\frac{1}{P\left(C_{j}\right)} \sum_{i \in I_{j}} E\left[\underline{1}_{B_{i}}{ }^{X}\right] \\
& =\frac{1}{P\left(C_{j}\right)} E\left[\sum_{i \in I_{j}} \underline{1}_{B_{i}} \bar{X}\right] \\
& =\frac{1}{P\left(C_{j}\right)} E\left[\underline{X} \sum_{i \in I_{j}} \underline{1}_{B_{i}}\right]
\end{aligned}
$$

Finally since

$$
C_{j}=\bigcup_{i \in I_{j}} B_{j}
$$

it follows that

$$
\underline{1}_{C_{j}}=\sum_{i \in I_{j}} \underline{1}_{B_{i}}
$$

Thus

$$
\begin{aligned}
& E[E[X \mid Y] \mid Z](\omega)=\frac{1}{P\left(c_{j}\right)} E\left[\mathbb{1}_{c_{j}} E[X \mid Y]\right] \\
& =\frac{1}{P\left(c_{j}\right)} E\left[1 c_{i} \bar{X}\right] \\
& =E[\bar{X} \mid Z](\omega)
\end{aligned}
$$

which is the desired result.

## Taking Out what is known

Assume that the partition defined II is finer than the partition defined by $\mathbb{Z}$. Then

$$
E[\mathbb{Z} \bar{X} \mid \bar{Y}]=\mathbb{Z} E[\bar{X} \mid \eta]
$$

## Proof

Let $Q=\left\{B_{i}\right\}$ be the partion generated $\bar{I}$. since $Q$ is
finer than the partition genated by 2 it follows that 2 is a constant over each $B_{i}$. Assume that for $\omega \in B_{i}$

$$
\begin{aligned}
& Z=Z_{i} \\
& \begin{aligned}
E\left[Z X \mid B_{i}\right](\omega) & \\
& =\sum_{\omega \in B_{i}} 2(\omega) X(\omega) P_{B}(\omega) \\
& =Z_{i} \sum_{\omega \in B_{i}} \bar{X}(\omega) P_{B}(\omega) \\
& =Z_{i} E\left[X \mid B_{i}\right](\omega)
\end{aligned}
\end{aligned}
$$

since $B_{i}$ is arbitrary, the desired result is obtained.

$$
E[\mathbb{Z} \bar{X} \mid \bar{Y}]=\mathbb{Z} E[\bar{X} \mid \bar{Y}]
$$

Independent Random Varrables
If $I$ and $I$ are independent random variables

$$
E[X \mid Y]=E[X]
$$

## Proof

Let $P=\left\{B_{i}\right\}_{i}$ be the partition senerated by I and let $\left\{x_{1}, x_{2}, \ldots, x_{k}\right\}$ be the values $\mathbb{X}$ takes on $B_{i}$. It follows that

$$
\begin{aligned}
E\left[\bar{x} \mid B_{i}\right] & =\sum_{j=1}^{k} x_{j} P\left(\bar{x}=x_{j} \mid B_{i}\right) \\
& =\sum_{j=1}^{k} x_{j} \frac{P\left(\bar{x}=x_{j}, B_{i}\right)}{P\left(B_{i}\right)} \\
& =\sum_{j=1}^{k} x_{j} \frac{P\left(\bar{x}=x_{j}\right) P\left(B_{i}\right)}{P\left(B_{i}\right)} \\
& =\sum_{j=1}^{k} x_{j} P\left(\bar{x}=x_{j}\right) \\
& =E[\bar{x}]
\end{aligned}
$$

This will be true for each set in the partiton. Thus the desired result is abtained

$$
E[\bar{X} \mid \bar{Y}]=E[\bar{X}]
$$

## Filtrations and Martingale

Let $X$ be a random variable defined on $\Omega=\left\{\omega_{1}, \omega_{2}, \omega_{3}, \ldots, \omega_{m}\right\}$, taking on distunct values
$\left\{x_{1}, x_{2}, \ldots, x_{k}\right\}$ The partition defined by $\bar{X}$ is the family of sets

$$
\begin{gathered}
\theta_{z}=\left\{B_{i}\right\}_{i=1}^{k} \\
B_{i}=\left\{\omega: \bar{X}(\omega)=x_{i}\right\}
\end{gathered}
$$

where

$$
\begin{gathered}
B_{i} \cap B_{j} \neq \varnothing \quad i \neq j \\
\bigcup_{i=1}^{k} B_{i}=\Omega
\end{gathered}
$$

Consider two random variables I and I. To construct a partition on which both $\bar{X}$ and I have a constant value of each element of partition, first construct a partition
from $\bar{X}$. If $\bar{I}$ takes on the following values,

$$
\left\{x_{1}, x_{2}, \ldots, x_{k}\right\}
$$

then

$$
\begin{gathered}
P_{\bar{x}}=\left\{B_{i}\right\}_{i=1}^{k} \\
B_{i}=\left\{\omega: \bar{x}(\omega)=x_{i}\right\}
\end{gathered}
$$

Next if $\bar{I}$ is assumed to take on the values,

$$
\left\{y_{1}, y_{2}, \ldots, y_{m}\right\}
$$

then

$$
\begin{gathered}
P_{x q}=\left\{B_{i j}\right\}_{i=1, j=1}^{k, m} \\
B_{i j}=\left\{\omega ; \omega \in B_{i}, \bar{Y}(\omega)=y_{j}\right\}
\end{gathered}
$$

It follows that on $B_{i j}$

$$
\bar{X}(\omega)=x_{i} \quad \bar{Y}(\omega)=y_{j}
$$

A partition for an arbitrary number of random variables can be constructed following this proceedure
Let $\bar{X}_{1}, \bar{X}_{2}, \ldots, \bar{X}_{n}$ be a sequence of random variables and denote the partition defined by these variables as $P_{n}$ if the sequence is such that $Q_{n+1}$ is finer than $O_{n}$ the sequence of portitions is a filtration.
From the tower property for conditional expectations it follows that for $m>n$

$$
E\left[E\left[X \mid P_{m}\right] \mid P_{n}\right]=E\left[X \mid P_{n}\right]
$$

Define the random variable

$$
\underline{Y}(m)=E\left[\underline{X} \mid P_{m}\right]
$$

then

$$
E\left[\bar{I}(m) \mid Q_{n}\right]=\bar{I}(n)
$$

Thus the sequence of conditional expectations is a martingale

## Definition

A sequence $M(n)$ of random variables is a martigale with respect to the fittration $\left\{P_{n}\right\}$ if for every $n<m$

$$
E\left[M(m) \mid Q_{n}\right]=M(n)
$$

Recall that

$$
M(n)=E\left[X\left(P_{n}\right]\right.
$$

so the partition formed by $M(n), P_{M(n)}$, is a subpartition of $Q_{n}$,

$$
P_{m(n)} \subset P_{n}
$$

If this is the case it is said that $M(n)$ is $P_{n}$ measurable and it follows that

$$
E\left[M(n) \mid P_{n}\right]=M(n)
$$

This can be understaod by considering that because $M(n)$ is the conditional expectation with respect to $P_{n}$ it will be constant over the elements of $P_{n}$. It then follows that computing the conditional expectation with respect to $P_{n}$ will be the same as $P_{n}$.

## Theorem

If $E\left[M(n+1) \mid P_{n}\right]=M(n)$ then $M(n)$ is a martingale

## Proof

Assume $m>n$. To prove that $M(n)$ is a matingate it must shown that

$$
E\left[M(m) \mid P_{n}\right]=M(n)
$$

Follows from the assumption trat $E\left[M(n+1) \mid D_{n}\right]=M(n)$.
Now from the tower property of conditional expectation

$$
E\left[M(m) \mid P_{n}\right]=E\left[E\left[M(m) \mid P_{m-1}\right] \mid P_{n}\right]
$$

since $P_{m-1}$ is finer than $P_{n}$. From the assumption it follows that

$$
E\left[M(m) \mid P_{m-1}\right]=M(m-1)
$$

Thus

$$
E\left[M(m) \mid P_{n}\right]=E\left[M(m-1) \mid P_{n}\right]
$$

Application of the tower property again and assumption gives

$$
\begin{aligned}
E\left[M(m-1) \mid P_{n}\right] & = \\
E[ & \left.E\left[M(m-1) \mid P_{m-2}\right] \mid P_{n}\right] \\
& =E\left[M(m-2) \mid P_{n}\right] \\
\Rightarrow E\left[M(m) \mid P_{n}\right] & =E\left[M(m-2) \mid P_{n}\right]
\end{aligned}
$$

Continuing this proceedure $m-(n+1)$ times sives

$$
\begin{aligned}
E\left[M(m) \mid P_{n}\right] & =E\left[M(n+1) \mid P_{n}\right] \\
& =M(n)
\end{aligned}
$$

Thus $m$ is a martingale.

## Theorem

If $M(n)$ is $O_{n}$ measurable and $E\left[M(n+1)-M(n) \mid P_{n}\right]=O$ then $M(n)$ is a martingale

## Proof

To prove the theorem it must be shown that for $m>n$

$$
\begin{aligned}
& E\left[M(m) \mid P_{n}\right]=M(n) \\
\Rightarrow \quad & E\left[M(m) \mid P_{n}\right]-M(n)=O
\end{aligned}
$$

Now consider

$$
E\left[M(m) \mid P_{n}\right]-M(n)
$$

since $M(n)$ is $P_{n}$ measureable

$$
M(n)=E\left[M(n) \mid P_{n}\right]
$$

50

$$
\begin{array}{r}
E\left[M(m) \mid P_{n}\right]-E\left[M(n) \mid P_{n}\right] \\
=E\left[M(m)-M(n) \mid P_{n}\right]
\end{array}
$$

Consider the sum

$$
\begin{aligned}
& \sum_{k=n}^{m-1} M(k+1)-M(k) \\
& =(M(\hat{n}+1)-M(n))+(M(\hat{n}+2)-M(\hat{n}+1)) \\
& +(M(n+3)-M(\hat{n}+2))+\cdots \\
& +(M(\hat{m}-1)-M(\hat{m}-2)) \\
& +(M(m)-M(\hat{m}-1)) \\
& =M(m)-M(n)
\end{aligned}
$$

Thus

$$
\begin{aligned}
E & {\left[M(m)-M(n) \mid P_{n}\right] } \\
& =E\left[\sum_{k=n}^{m-1}(M(k+1)-M(k)) \mid P_{n}\right] \\
& =\sum_{k=n}^{m-1} E\left[M(k+1)-M(k) \mid P_{n}\right] \\
& =0
\end{aligned}
$$

Since it is assumed that

$$
E\left[M(K+1)-M(K) \mid P_{n}\right]
$$

Thus

$$
\begin{aligned}
& E\left[M(m)-M(n) \mid P_{n}\right]=0 \\
\Rightarrow & E\left[M(m) \mid P_{n}\right]=M(n)
\end{aligned}
$$

## Theorem

Let $I$ be a random variable and let $P_{0}, P_{1}, P_{2}$ be a filtration.

Then the sequence

$$
E\left[X \mid P_{0}\right], E\left[X \mid P_{1}\right], E\left[X \mid P_{2}\right], \ldots
$$

is a martingale.

## Proof

For the sequence to be a martingale it must satisfy

$$
E\left[E\left[X \mid P_{m}\right] \mid P_{n}\right]=E\left[X \mid P_{n}\right]
$$

for $m>n$. This relation follows from the tower property of conditional expectation since $P_{m}$ is finer then $P_{n}$.

## Theorem

If $\{M(n)\}_{n \geqslant 0}$ is a martingale with respect to a filtration $\left\{P_{n}\right\}_{n \geqslant 0}$ then

$$
E[M(0)]=E[M(1)]=E[M(2)]=\cdots
$$

## Proof

If $M(0), M(1), M(2), \ldots$ is a martigale then from a previous result it was shown trat

$$
M(n)=E\left[M(n+1) \mid P_{n}\right]
$$

For each $n$. Taking expectation gives

$$
\begin{aligned}
E[M(n)] & =E\left[E\left[M(n+1) \mid P_{n}\right]\right] \\
& =E[M(n+1)]
\end{aligned}
$$

trus for each $n$

$$
E[M(n)]=E[M(n+1)]
$$

and the desired result follows

$$
E[M(0)]=E[M(1)]=E[M(2)]=\cdots
$$

## Definition

A sequence $M(0), M(1), M(2), \ldots$ of random variables is a submartingale with respect to the filtration
$P_{0}, P_{1}, P_{2}, \ldots$ If the partition of $M(n)$ is coorser than $P_{n}$

$$
E\left[M(n+1) \mid P_{n}\right] \geqslant M(n)
$$

If

$$
E\left[M(n+1) \mid P_{n}\right] \leqslant M(n)
$$

it is a supermartingale.

## Definition

An increasing sequence of $\sigma$-fields

$$
\left\{\mathfrak{J}_{n}\right\}_{n \leqslant N}
$$

is called a fittration, where

$$
\mathcal{F}_{0}=\{\phi, \Omega\}
$$

$I_{n}$ is generated by the first $n$ elements of the sequence

$$
M(1), M(2), M(3), \ldots, M(n)
$$

The freld generated by a
random variable I is of the form

$$
\mathcal{F}_{\Delta}=\left\{\bar{X}^{-1}(B): B \subset \mathbb{R}\right\}
$$

where $B$ is a Borel set.

## Trading Strategies and Arbitrage

A trading strategy is a sequence of pairs or random varrables

$$
(x(n), y(n))
$$

where $n=1,2,3, \ldots, N$ and $x(n)$ gives the number of shares of an asset $S(n)$ and $y(n)$ the amout invested at the risk-free rate. $(x(n), y(n))$ are determined at step $n-1$ and held until step $n .(x(n), y(n))$ are $F_{n-1}$-measureable. Any sequence satisfying the measurability is called predictatole.

## Definitron

The value process of a strategy is a sequence

$$
U_{x y}(n)=x(n) S(n)+y(n) A(n)
$$

together with the initial investment

$$
U_{x y}(0)=x(1) S(0)+y(1) A(0)
$$

defined for $n=1,2,3, \ldots, N$

## Definition

A strategy is self-firancing if

$$
U_{x y}(n)=x(n+1) S(n)+y(n+1) A(n)
$$

The change in value of the port follo between $n-1$ and $n$ is given by

$$
\begin{aligned}
& \Delta U_{x y}(n)=U_{x y}(n)-U_{x y}(n-1) \\
& =x(n) S(n)+y(n) A(n) \\
& -x(n) S(n-1)+y(n) A(n-1) \\
& =x(n)[S(n)-S(n-1)] \\
& +y(n)[A(n)-A(n-1)]
\end{aligned}
$$

$$
=x(n) \Delta S(n)+y(n) \Delta A(n)
$$

$x(n)$ and $y(n)$ are constant since they are determined at $n-1$ and held until $n$.

The risk-free position is determined by the initial investment and the desired asset posttion, which can be anything. Soloing for $y(1)$ gives,

$$
\begin{aligned}
U_{x y}(0) & =x(1) S(0)+y(1) A(0) \\
\Rightarrow y(1) & =\frac{1}{A(0)}\left[U_{x y}(0)-x(1) S(0)\right]
\end{aligned}
$$

From the definition the self financing stratesy it follows that

$$
y(n+1)=\frac{1}{A(n)}\left[U_{x y}(n)-x(n+1) s(n)\right]
$$

The only funds contributed by the investor are $U_{x y}(0)$. All other transactions are funded with funds borrowed at the risk-free interest rate. In tris since the algorithm is considered self firancing.
wote that a metrial for determing $x(n)$ has not been specified.

## Exercise

Find $x(n)$ for a version of $a$ self firancing strategy where $y(n)$ and $U_{x y}(0)$ are given.

## Solution

From the definition of a self funancicing strategy
$U_{x y}(n)=x(n+1) S(n)+y(n+1) A(n)$

If $U(0)$ and $y(n+1)$ are given it follows that

$$
x(n+1)=\frac{1}{s(n)}\left[U_{x y}(n)-y(n+1) A(n)\right]
$$

## Theorem

Assume there exists a probability $Q$ such that the discounted conditional expectation of the asset price with respect to $Q$ and the filtration $J_{n}$ is given
by by

$$
E_{0}\left[\tilde{S}(n+1) \mid \tilde{F}_{n}\right]=\tilde{S}(n)
$$

for every $n \geqslant 0, \tilde{S}(n)$ is a martingale. Then the discounted values of a self-financing strategy form a martingale with respect to $Q$.

## Proof

Recall that the discounted
value proccess is given by,

$$
\tilde{U}_{x y}(n)=(1+R)^{-n} U_{x y}(n)
$$

So a discounded value strategy is defined by

$$
\tilde{U}_{x y}(n)=x(n) \tilde{S}(n)+y(n) \tilde{A}(n)
$$

and the discounted self-financing condition by

$$
\tilde{U}_{x y}(n)=x(n+1) \tilde{S}(n)+y(n+1) \tilde{A}(n)
$$

Now the conditional expectation of the discounted value strategy with respect to $Q$ and $\mathcal{F}_{n}$ is given by

$$
\begin{aligned}
E_{Q} & {\left[\tilde{U}_{x y}(n+1) \mid \tilde{J}_{n}\right] } \\
& =E_{Q}[x(n+1) \tilde{S}(n+1)+y(n+1) \tilde{A}(n+1)]
\end{aligned}
$$

$$
\begin{gathered}
=x(n+1) E_{Q}[\tilde{S}(n+1)] \\
+y(n+1) \tilde{A}(n+1)
\end{gathered}
$$

This step follows from the assumption that at a given time $x(n+1)$ is known and is the same for all possible outsomes of $\tilde{S}(n+1)$. The excetation is computed over the outcomes of $S(n+1)$. Also, $y(n+1) \tilde{A}(n+1)$ is not random, This assumption is called "predictability of the strategy!"
Now it is assumed that $\tilde{s}(n+1)$ is a martingale.

$$
E_{Q}\left[\tilde{S}(n+1) \mid \mathcal{F}_{n}\right]=\tilde{S}(n)
$$

and by definition

$$
A(n)=(1+R)^{n} A(0)
$$

So,

$$
\tilde{A}(n+1)=\frac{(1+R)^{n+1}}{(1+R)^{n+1}} A(0)=A(0)
$$

It follows that,

$$
\begin{aligned}
& x(n+1) E_{Q}\left[\tilde{S}(n+1) \mid \tilde{J}_{n}\right]+y(n+1) \tilde{A}(n+1) \\
= & x(n+1) \tilde{S}(n)+y(n+1) A(0) \\
= & (1+R)^{-n}\left[x(n+1) S(n)+y(n+1)(1+R)^{-n} A(0)\right] \\
= & (1+R)^{-n}[x(n+1) S(n)+y(n+1) A(n)]
\end{aligned}
$$

But a self-financing stratesy is defined by

$$
U_{x y}(n)=x(n+1) S(n)+y(n+1) A(n)
$$

Bringing things together gives the desired result

$$
\begin{aligned}
E_{Q}\left[\tilde{U}_{x y}(n+1) \mid \mathcal{F}_{n}\right] & =(1+R)^{-n} U_{x y}(n) \\
& =\tilde{U}_{x y}(n)
\end{aligned}
$$

Note that this proof did not assume a particular form for $\tilde{S}(n)$ only that it is a martingale.

## Definition

A strategy,

$$
(x(n), y(n))
$$

is an arbitrage opportunity if

$$
U_{x y}(0)=0 \quad U_{x y}(n) \geqslant 0
$$

for all $n$ and for some $n$ there is an $\omega c \Omega$ such that,

$$
U_{x y}(n)>0
$$

For the extended market the definition of an arbitrage
stratesy has to be modified to include postions in derivative securities.

## A General Multi-Step Model

In a general mutti-step model a derivative security defined on more than one underlying asset and a risk-free investment. Time is assumed to be discrete as in the binomial madel. The market consists of a risk-free investment and $d$ risky investments denonted by $S_{1}(n), S_{2}(n), \ldots, S_{d}(n)$. The risky assets form iRd valued vector

$$
\vec{S}(n)=\left(S_{1}(n), S_{2}(n), \ldots, S_{d}(n)\right)
$$

defined on the sample space

$$
\Omega=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{M}\right\}
$$

The risk-free return is $R$ and the risk-free investment is given by

$$
A(n)=A(O)(1+R)^{n}
$$

A portfolio is defined by the vector

$$
(\vec{x}, y)=\left(x_{1}, x_{2}, \ldots, x_{d}, y\right)
$$

a strategy is the sequence of portfolios
$(\bar{x}(n), y(n))=\left(x_{1}(n), x_{2}(n), \ldots, x_{d}(n), y(n)\right)$
where $n=1,2, \ldots, N$
The strategy is an $\mathbb{R}^{d+1}$ random vector.

The value of the strategy at time $n$ is given by

$$
\begin{array}{r}
U_{x y}(n)=\sum_{i=1}^{d} x_{i}(n) S_{i}(n)+y(n) A(n) \\
U_{x y}(0)=\sum_{i=1}^{d} x_{i}(1) S_{i}(0)+y(1) A(0)
\end{array}
$$

It is asscomed that

$$
(\bar{x}(n+1), y(n+1)
$$

is $I_{n}$ measurable. This follows from constructing the portfolio for time $n+1$ using furds and information about asset prices at time $n$.
The self-financing condition is defined by
$U_{x, y}(n)=\sum_{i=1}^{d} x_{i}(n+1) S_{i}(n)+y(n+1) A(n)$

## Definition

A strategy $(\bar{x}, y)$ is an arbitrage opportunity in the underlying market if its value process satisfies $U_{\bar{x}, y}(0)=0, U_{\bar{x}, y}(n) \geqslant 0$ for all $n$ there is an $w$ such that $U_{\bar{x}, y}(n, w)>0$

## Assumption

No arbitrage opportionities exst
in the market.
It will be shown that this is equivalent to the existence of a martigate probability $Q$ with $Q(\omega)>0$ for all $\omega \in \Omega$ such that the discounted asset process,

$$
\left\{\tilde{S}_{i}(n): i=1,2, \ldots, N\right\}
$$

is a martigale with respect to $Q$.

## Definition

The gains process generated by the strategy $(\bar{x}, y)$ is defined by

$$
\begin{aligned}
G_{\bar{x} y}(0)=0 & \\
G_{\bar{x} y}(n)= & \sum_{k=1}^{n}\left(\sum_{j=1}^{d} x_{j}(k) \Delta S_{j}(k)\right. \\
& +y(k) \Delta A(k))
\end{aligned}
$$

If the strategy is self firancing
$U_{\bar{x}, 1}(n-1)=\sum_{i=1}^{d} x_{i}(n) S_{i}(n-1)+y(n) A(n-1)$
and from the defintion of a value process

$$
U_{\bar{x}_{y}, y}(n)=\sum_{i=1}^{d} x_{i}(n) S_{i}(n)+y(n) A(n)
$$

thus

$$
\begin{array}{r}
\Delta U_{\bar{x}, y}(n)=U_{\bar{x}, y}(n)-U_{\bar{x}, y}(n-1) \\
=\sum_{i=1}^{d} X_{i}(n) \Delta S_{i}(n)+y(n) \Delta A(n)
\end{array}
$$

It follows that

$$
\Delta U_{\bar{x}, y}(n)=\Delta G_{\bar{x}, y}(n)
$$

Now

$$
\begin{aligned}
U_{\bar{x}, y}(0)+ & \sum_{i=1}^{n} \Delta U_{\bar{x}, y}(n) \\
= & U_{\bar{x}, y}(0)+\left[U \hat{x}_{\bar{x}, y}(1)-U_{\bar{x}, y}(0)\right] \\
+ & {\left[U_{\bar{x} \pi_{1}}(2)-\bar{U}_{\bar{x}, y}(1)\right]+\cdots+} \\
& {\left[U_{\bar{x}, y}(n-1)-U_{\bar{x}, y}(n-2)\right]+} \\
& {\left[U_{\bar{x}, y}(n)-U_{\bar{x}, y}[(n-1)]\right.} \\
= & U_{\bar{x}, y}(n)
\end{aligned}
$$

Thus

$$
U_{\bar{x}, y}(n)=U_{\bar{x}, y}(0)+\sum_{i=1}^{n} \Delta U_{\bar{x}, y}(n)
$$

It follows that

$$
U_{\bar{x}, y}(n)=U_{\bar{x}, y}(0)+G_{\bar{x}, y}(n)
$$

for $n=1,2, \ldots, N$
Theorem
Given $U(0)$ and a predictable
sequence

$$
\bar{x}=\left(x_{1}(n), \ldots, x_{d}(n)\right)
$$

there exists a unique predictable sequence $y(n)$ such that

1. $U_{\bar{x}, y}(0)=U(0)$
2. The strategy $(\bar{x}, y)$ is self-financing

## Proof

The proof is by induction. First let

$$
y(1)=\frac{U(0)-\bar{x}_{1}(1) \cdot \bar{S}(0)}{A(0)}
$$

it follows that

$$
\begin{aligned}
U_{\bar{x} y}(0) & =\bar{x}(1) \cdot \bar{s}(0)+\bar{y}(1) A(0) \\
& =\bar{x}(1) \cdot \bar{s}(0)+\frac{U(0)-\bar{x}(1) \cdot \bar{s}(0) A(0)}{A(0)} \\
& =U(0)
\end{aligned}
$$

also $y(1)$ is nat random since $U(0), \bar{X}(1)$. At the relization of the first stop

$$
U_{\bar{x} y}(1)=\bar{x}(1) \cdot \bar{S}(1)+y(1) A(1)
$$

For the raduction step it is assumed that $y(n)$ is known and is given by,

$$
y(n)=\frac{U_{\bar{x} y}(n)-\bar{x}(n) \cdot \bar{s}(n)}{A(n)}
$$

Since $y(n)$ is known $U_{\bar{x} y}(n)$ is known. From the self-finareing condition it follows that

$$
y(n+1)=\frac{U_{\bar{x} y}(n)-\vec{x}(n+1) \cdot \bar{S}(n)}{A(n)}
$$

Thus a pridictable self-fincing strategy, $(\bar{x}, y)$, exists anc $v(0)=v_{x y}(0)$ This completes the proof.

Recall that the definition of a discounted asset price is given by

$$
\tilde{\bar{x}}(n)=\frac{\bar{x}(n)}{(1+R)^{n}}
$$

The difference in the discounted asset price betwen eteps is given by,

$$
\Delta \tilde{\bar{x}}(n)=\frac{\bar{X}(n)}{(1+R)^{n}}-\frac{\bar{X}(n-1)}{(1+R)^{n-1}}
$$

This is not the discounted difference, which is given by

$$
\begin{aligned}
\tilde{\Delta} \bar{X}(n) & =\frac{\Delta \bar{X}(n)}{(1+R)^{n}} \\
& =\frac{\bar{X}(n)}{(1+R)^{n}}-\frac{\bar{X}(n-1)}{(1+R)^{n}}
\end{aligned}
$$

It is interesting to note that

$$
\begin{aligned}
\tilde{A}(n) & =\frac{A(n)}{(1+R)^{n}}=A(0) \frac{(1+R)^{n}}{(1+R)^{n}} \\
& =A(0)
\end{aligned}
$$

it follows that

$$
\begin{aligned}
\Delta \tilde{A}(n) & =A(0)-A(0) \\
& =0
\end{aligned}
$$

Recall that the gains process is given by
$G_{\bar{y} y}(n)=\sum_{j=1}^{n}\left(\sum_{i=1}^{d} x_{i}(n) \Delta S_{i}(n)+y(n) \Delta A(n)\right)$
It follows that the discounted is given by
$\tilde{G}_{\overline{x y}}(n)=\sum_{j=1}^{n}\left(\sum_{i=1}^{d} X_{i}(n) \Delta \tilde{S}_{i}(n)+y(n) \Delta \tilde{A}(n)\right)$
it was just shown that

$$
\Delta \tilde{A}(n)=0
$$

thus

$$
\begin{aligned}
\tilde{G}_{\bar{x}}(n) & =\sum_{j=1}^{n} \sum_{i=1}^{d} x_{i}(n) \Delta \tilde{S}_{i}(n) \\
& =\sum_{j=1}^{n}\langle\bar{x}(n), \Delta \tilde{\tilde{S}}(n)\rangle
\end{aligned}
$$

where the inner product is defined by

$$
\begin{aligned}
\langle\bar{x}(n), \Delta \tilde{\bar{S}}(n)\rangle & =\bar{x}(n) \cdot \Delta \tilde{\bar{S}}(n) \\
& =\sum_{i=1}^{\alpha} X_{i}(n) \Delta \tilde{S}_{i}(n)
\end{aligned}
$$

Theorem
If a strategy is self-firancing then

$$
\tilde{U}_{\bar{x} y}(n)=U_{\bar{x} y}(0)+\tilde{G}_{x}(n)
$$

## Proof

Fix $n \leqslant N$ and assume the strategy $(\bar{x}(n), y(n))$ is selffinancing.
The discounted value process for step it ( is given by

$$
\begin{aligned}
\widetilde{U}_{\bar{x} y}(i+1)= & (1+R)^{-(i+1)}[\langle\bar{x}(i+1), \bar{S}(i+1)\rangle \\
& +y(i+1) A(i+1)] \\
= & \langle\bar{x}(i+1), \tilde{\bar{S}}(i+1)\rangle+y(i+1) A(0)
\end{aligned}
$$

and similarly from the self-financing condition

$$
\tilde{U}_{\bar{x} y}(i)=\langle\bar{x}(i+1), \tilde{\tilde{s}}(i)\rangle+y(i+1) A(0)
$$

Subtracting the two gives

$$
\Delta \tilde{U}_{\bar{x} y}(i+1)=\tilde{U}_{\bar{x} y}(i+1)-\tilde{U}_{\bar{x} y}(i)
$$

$$
\begin{aligned}
& =\langle\bar{x}(i+1), \tilde{\bar{S}}(i+1)\rangle-\langle\bar{x}(i+1), \tilde{\bar{S}}(i)\rangle \\
& =\langle\bar{x}(i+1), \Delta \tilde{\bar{S}}(i+1)\rangle \\
& =\Delta G_{\bar{x}}(i+1)
\end{aligned}
$$

Now

$$
\begin{aligned}
U_{\bar{x} y}(n)-U_{\bar{x} y}(0) & =\sum_{i=1}^{n} \Delta \tilde{U}_{\bar{x} y}(i) \\
& =\sum_{i=1}^{n} \Delta \tilde{G}_{\bar{x}}(i) \\
& =\tilde{G}_{\bar{x}}(n)
\end{aligned}
$$

Thus the desired result is obtained

$$
\tilde{U}_{\bar{x} y}(n)=U_{\bar{x}_{l}}(0)+\tilde{G}_{\bar{x}}(n)
$$

## Definition

A probability $Q$ is risk-neutral (or a mootingale probability)

If the discounted stock prices are martingales

$$
E_{Q}\left[\tilde{S}_{j}(n+1) \mid \tilde{J}_{n}\right]=\tilde{S}_{j}(n) \quad \forall j
$$

Next it will be shown that the discovinted value process $\tilde{U}_{\bar{x} y}(n)$ is a mortingale.

## Definition

A process $\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$ is predicable with respect to the Piltration $\mathcal{F}_{n}$ if each element of the sequence is $\mathfrak{F}_{n}$ measurable That is

$$
\begin{gathered}
E\left[x_{0} \mid \mathcal{F}_{0}\right]=x_{0} \\
E\left[x_{1} \mid \mathcal{F}_{1}\right]=x_{1} \\
\vdots \\
E\left[x_{n} \mid \mathcal{F}_{n}\right]=x_{n}
\end{gathered}
$$

## Theorem

If $\mu_{j}(n)$ are martingales and the processes $H_{j}(n)$ are predictable, $j=1,2, \ldots, d$. Then the process, $\bar{x}_{n}$, defined by

$$
\begin{aligned}
\underline{X}(n) & =\bar{X}(0)+\sum_{k=1}^{n} \sum_{j=1}^{d} H_{j}(k) \Delta M_{j}(k) \\
& =\bar{X}(0)+\sum_{k=1}^{n}\langle\bar{H}(k), \Delta \bar{M}(k)\rangle
\end{aligned}
$$

is a martingale, where $\bar{X}(0)=X_{0}$, is an arbitrary real numbers.

## Proof

Now

$$
Z(n+1)=x_{0}+\sum_{k=1}^{n+1}\langle\bar{H}(k,), \Delta \bar{M}(k)\rangle
$$

it follows that

$$
\begin{aligned}
& \underline{X}(n+1)-\bar{X}(n)= X_{0}+\sum_{k=1}^{n+1}\langle\bar{H}(k,), \Delta \bar{M}(k)\rangle \\
&- X_{0}-\frac{n}{2}\langle\bar{H}(k,), \Delta \bar{M}(k)\rangle \\
&=\langle\bar{H}(n+1), \Delta \bar{M}(n+1)\rangle+\sum_{k=1}^{n}\langle\bar{H}(k,), \Delta \bar{M}(k)\rangle \\
&-\sum_{k=1}^{n+1}\langle\bar{H}(k,), \Delta \bar{M}(k)\rangle \\
& \Rightarrow \bar{X}(n+1)-\bar{X}(n)=\langle\bar{H}(n+1), \Delta \bar{M}(n+1)\rangle
\end{aligned}
$$

Now taking conditional expectation with respect to $\mathcal{F}_{n}$,

$$
\begin{aligned}
E\left[\bar{X}(n+1)-\bar{X}(n) \mid \mathcal{F}_{n}\right] \\
=E\left[\langle\bar{H}(n+1), \Delta \bar{M}(n+1)\rangle \mid \mathcal{F}_{n}\right] \\
=E\left[\sum_{i=1}^{d} H_{i}(n+1) \Delta M_{i}(n+1) \mid \mathcal{F}_{n}\right] \\
=\sum_{i=1}^{d} E\left[H_{i}(n+1) \Delta M_{i}(n+1) \mid \mathcal{F}_{n}\right]
\end{aligned}
$$

$$
=\sum_{i=1}^{d} H_{i}(n+1) E\left[\Delta M_{i}(n+1) \mid \mathcal{F}_{n}\right]
$$

The previous follows from the assumption that $H_{i}(n+1)$ is In measurable and using the taking out what is known property.

$$
\begin{aligned}
E\left[\bar{X}(n+1)-\bar{X}(n) \mid \mathcal{F}_{n}\right] \\
\quad=\sum_{i=1}^{d} H_{i}(n+1) E\left[\Delta M_{i}(n+1) \mid \mathcal{F}_{n}\right] \\
\quad=\sum_{i=1}^{d} H_{i}(n+1) E\left[M_{i}(n+1)-M_{i}(n) \mid \mathcal{F}_{n}\right] \\
\quad=\sum_{i=1}^{d} H_{i}(n+1)\left(E\left[M(n+1) \mid \mathcal{F}_{n}\right]\right. \\
\quad=\sum_{i=1}^{d} H_{i}(n+1)[M(n)-M(n)] \\
\quad=0
\end{aligned}
$$

The last step follows from tre assumption that $M(n+1)$ is a martingale and $M(n)$ is measualde with respect to $\xi_{n}$.
Finally

$$
\begin{aligned}
E\left[\bar{X}(n+1)-\bar{X}(n) \mid \mathcal{F}_{n}\right]=0 & \\
\Rightarrow E\left[\bar{X}(n+1) \mid \mathcal{F}_{n}\right] & =E\left[\bar{X}(n) \mid \mathcal{F}_{n}\right] \\
& =\bar{X}(n)
\end{aligned}
$$

Thus $\bar{X}(n)$ is a martingale with respect to $\hat{J}_{n}$.

## Theorem

For M(n) to be a martingale it is sufficient that for each predictable process $H(n)$

$$
E\left[\sum_{n=1}^{N} H(n) \Delta M(n)\right]=0
$$

## Proof

It will be shown that

$$
E\left[M(k+1) \mid \mathcal{F}_{k}\right]=M(k)
$$

follows from the theorem assumption
Let $A \in \mathcal{F}_{n}$ and let

$$
H(n)=\left\{\begin{array}{cc}
\mathbb{1}_{A} & \text { for } n=k+1 \\
0 & \text { otherwise }
\end{array}\right.
$$

then

$$
\begin{aligned}
& \sum_{n=1}^{N} H(n) \Delta M(n)=\mathbb{1}_{A} \Delta M(k+1) \\
& \text { so } \\
& E\left[\sum_{n=1}^{N} H(n) \Delta M(n)\right]=E\left[\underline{1}_{A} \Delta M(k+1)\right]
\end{aligned}
$$

It is assumed that

$$
E\left[\sum_{n=1}^{N} H(n) \Delta M(n)\right]=0
$$

50

$$
E\left[\mathbb{1}_{A} \Delta M(K+1)\right]=0
$$

Recoll the defintion of conditional expectation

$$
E[X \mid A]=\frac{1}{P(A)} E\left[I_{A} \bar{X}\right]
$$

Thus

$$
\begin{aligned}
& E\left[\mathbb{1}_{A} \Delta M(k+1)\right]=P(A) E[\Delta M(k+1) \mid A] \\
& =0 \\
\Rightarrow E[M(k+1)-M(k) \mid A] & =0 \\
\Rightarrow E[M(k+1) \mid A] & =E[M(k) \mid A]
\end{aligned}
$$

$\Rightarrow E[M(K+1) \mid A]=M(K)$
Since $A$ is an arbitrary element of $\mathcal{F}_{k}$ it follows that

$$
E\left[M(k+1) \mid \mathcal{F}_{k}\right]=M(k)
$$

Thus $M(K)$ is a martingale.

## Fundamental Theorems of Asset Pricing

Throughout this section it is asswered that the filtration $\left(I_{n}\right)_{n \leqslant N}$ generated by the tock prices satisfies

$$
\tilde{Э}_{N}=\tilde{J}=2^{\Omega}
$$

Two probabilities are equivalent if they have the same sets with probability zero. Equivalence between probability, distributions is denoted by

$$
P \sim Q
$$

The sample space is assumed finite,

$$
\Omega=\left\{\omega_{1}, \omega_{2}, \ldots, \omega_{N}\right\}
$$

and assume the $P$ is defined on $\mathcal{F}=2^{\Omega}$ and $P(\omega)>0 \quad \forall \omega \in \Omega$

## First Furdamental Theorem

## Theorem

Absence of arbitrage is equivalent to the existence of a risk-neutral prabability $Q$ equivalent to $P$, such that all discounted asset price processes $S_{j}(n), j=1,2 \ldots, d$ are martingales with respect to $Q$

## Proof

The proof requires showing that if there is a risk-neutral probability then there is no arbitrage

For the first assume a risk-neutral probability $Q, a$ trading strategy $(\bar{x}, y)$ and that an arbitrage exists so that the discounted value process satisfies,

$$
\begin{aligned}
& \tilde{U}_{\bar{x} y}(0)=U(0)=0 \\
& \tilde{U}_{\bar{x} y}(n) \geqslant 0
\end{aligned}
$$

since a risk-neutral probability exists it follows that $\tilde{U}_{x y}(n)$ is a martingale, so

$$
\begin{aligned}
E_{Q}\left[\tilde{U}_{\bar{x}_{y}}(n)\right] & =\tilde{U}_{x y}(0) \\
& =U(0) \\
& =0
\end{aligned}
$$

Now

$$
\begin{aligned}
& E_{Q}\left[\tilde{U}_{\bar{x} y}(n)\right]=\sum_{\omega \in \Omega} Q(\omega) \tilde{U}_{\bar{x} y}(\omega, n) \\
&=0 \\
& \Rightarrow \sum_{\omega \in \Omega} Q(\omega) U_{\bar{x} y}(\omega, n)=0
\end{aligned}
$$

Now $Q(\omega)>0 \quad \forall \omega \in \Omega$ and the assumption of arbitrage implies that

$$
U_{\bar{x} y}(\omega, n) \geqslant 0
$$

thus to satisfy the equality it must be that

$$
U_{\overline{x_{y}}}(\omega, n)=0
$$

Thus there is no cobitrage.

## Second Fundamental Theorem

## Definition

The payoff of a derivative security is a random variable it measurable with respect to the field $F_{N}$ generated by the underlying securities prices up to time $N$. The prices of $H$ form a sequence $H(n)$. The market is free of arbitrage
The basic market consists of $d$ assets and the risk-free asset. The extended market includes additional derivative securties

## Definition

A derivative security can be replicated if there exists a self-financing predictable strategy $(\bar{x}, y)$ such that

$$
H(N)=U_{\bar{x} y}(N)
$$

## Definition

A market is complete if eveny derivative security can be replicated.

## Theorem

An arbitrage free market model is complete if and only there is exactly one risk-neutral probability.

## Proof

To complete the proof it must be shown that if the market is complete then Q~P and conversly if QuP then the market is complete.
First assume that the market is complete and there are no opportionities for arbatrage and
that there are two risk-neutsal distributions $Q_{1} \nsim Q_{2}$. An example portfolio will be constructed that leads to $Q_{1} \sim Q_{2}$
the assumption that the market is arbitrage free let $A \in \mathcal{F}_{N}$ and define a derwative secumity with payoff off,

$$
H(N)=1_{A}= \begin{cases}1 & \omega \in A \\ 0 & \text { otherwise }\end{cases}
$$

From the assumption of completeness there exists a replicating portfolio such that

$$
H(N)=U_{\bar{x}_{y}}(N)=\mathbb{1}_{A}
$$

Taking expectations with respect $Q_{1}$ and $Q_{2}$ gives for $c=1,2$

$$
E_{Q_{i}}\left[U_{\bar{x} y}(N)\right]=E_{Q_{i}}\left[d_{A}\right]=Q_{i}(A)
$$

Now since $\tilde{U}_{x y}(N)$ is a martingate

$$
E_{Q_{l}}\left[\tilde{U}_{x y}(N)\right]=U(0)
$$

but

$$
\begin{aligned}
E_{Q_{i}} & {\left[\tilde{U}_{x y}(N)\right]=(1+R)^{-N} E_{Q_{i}}\left[U_{x y}(N)\right] } \\
& =(1+R)^{-N} E_{Q_{i}}\left[\mathbb{1}_{A}\right] \\
& =(1+R)^{-N} Q_{i}(A)
\end{aligned}
$$

trues

$$
Q_{i}(A)=U(D)(1+R)^{N}
$$

this is true for both $Q_{1}$ and $Q_{2}$ it follow that

$$
Q_{1} \sim Q_{2}
$$

The converse proof is a little more than I want to do right now

## Theorem

If the worderlying market of $d$ assets and a risk-free investment does not admit arbitrage and a derivative security with $H(N)$ is replicable by a stratesy $(\bar{x}, y)$ then for the exterded market to be arbitrage free, it must be that

$$
H(n)=U_{\bar{x}_{y}}(n)
$$

## Proof

To prove equality it must be shown if equality does not hold then a arbitrage opportunity exists. First assume The portfolio is cheaper. An investor could sell the option and use the funds to purchace the portfolio. The difference
is invested at the cisk-free interst rate. At option expry The portfolio can be used to payoff option and the intial difference and iterest kept as a risk-free profit.
Conversh, if the option were cheaper an irvestor can short sell the asset, use the proceeds to by the option and invest the differe at the risk-free rate. At exercise the option payoff can be used to purchace the asset to cover the short sell and the intial differce is a risk-free profit.
Now using that the asset price and Value process are martigates it follows that for the risk-neutral probability.

$$
\begin{aligned}
\tilde{U}_{x y}(n) & =E_{Q}\left[\tilde{U}_{x y}(N) \mid \mathcal{F}_{n}\right] \\
& =E_{Q}\left[\tilde{H}(N) \mid \mathcal{F}_{n}\right]
\end{aligned}
$$

but

$$
\begin{aligned}
H(n) & =U_{x y}(n) \\
\Rightarrow \quad \tilde{H}(n) & =\tilde{O}_{x y}(n)
\end{aligned}
$$

Thus

$$
\begin{aligned}
\tilde{H}(n) & =E_{Q}\left[\tilde{H}(N) \mid \mathcal{F}_{n}\right] \\
\Rightarrow \quad(1+R)^{-n} H(n) & =(1+R)^{-N} E_{Q}\left[H(N) \mid \mathcal{F}_{n}\right] \\
\Rightarrow \quad H(n) & =(1+R)^{n-N} E_{Q}\left[H(N) \mid \mathcal{F}_{n}\right]
\end{aligned}
$$

