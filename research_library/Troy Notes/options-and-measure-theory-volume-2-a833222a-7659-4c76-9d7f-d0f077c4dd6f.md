## Problem 4: Protective Put

A protective put is a heaging strategy implemented by laying an asset and buying an OTM put option on the stock.
Explain why a put buyer would set up this portfolio trading strategy and show that this stratesy is undertaken for,

$$
P\left(S_{t}, t ; K, T\right) \geqslant K-S_{t}
$$

where $P\left(S_{t}, t ; K, T\right)$ is the put option price writen on esset $s_{t}$ with strike price $K$ at time $t$ and time $T>t$.

## Solution

An investor would implement a protective put hedging strategy to insure profits in a long position in an asset. If the price of the asset fails below
the option strike proce the put buyer can exercise the option to sell at the strike price at option expiny and meet the obligation with the long assets and thus cover loses in the asset price. If the asset price is above the strike price at option expiry the option buyer does not exercise the option to buy and thus loses the permium.
Let $t<T$ denote the time the contracts are written and let $s_{t}$ denote the asset price at $t$.
The payoff for the portlolio is the sum of the payoff or the long asset position and long put.
The payoff of the long asset position is given by

$$
\psi_{T}^{A}=S_{T}
$$

and the payoff of the long put is given by

$$
\psi_{T}^{P}=\max \left(K-s_{T}, 0\right)
$$

It follows that the portfolio payoff is given by

$$
\psi_{\tau}=\max \left(K-s_{T}, O\right)+s_{T}
$$

For $K \leqslant S_{T}$

$$
\psi_{T}=K-S_{T}+S_{T}=K
$$

and for $k>S_{T}$

$$
\psi_{T}=S_{T}
$$

Thus

$$
\psi_{T}= \begin{cases}K & K \leqslant S_{T} \\ S_{T} & K>S_{T}\end{cases}
$$

The payoff for the long asset position, long put and portfolio is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-004.jpg?height=851&width=1140&top_left_y=461&top_left_x=211)

The profit for the portfolio is the sum of the profit of the long asset position and the long put. The profit of the long
asset position is siven by asset position is given by

$$
\gamma_{T}^{A}=S_{T}-S_{t}
$$

and the profit of the lons put is given by

$$
\gamma_{T}^{D}=\max \left(K-S_{T}, 0\right)-P\left(S_{T}, t ; K, T\right)
$$

The portfolio profit is given by
$V_{T}=S_{T}-S_{t}+\max \left(K-S_{T}, 0\right)-P\left(S_{t}, t ; K, T\right)$
Consider $S_{T} \leqslant K$

$$
\begin{aligned}
\gamma_{T} & =S_{T}-S_{t}+K-S_{T}-P\left(S_{t, t} ; K, T\right) \\
& =K-S_{t}-P\left(S_{t, t} ; K, T\right)
\end{aligned}
$$

and for $S_{T}>K$

$$
\gamma_{\tau}=S_{\tau}-S_{t}-P\left(S_{t}, t ; K, T\right)
$$

trus

$$
\gamma_{T}= \begin{cases}K-S_{t}-P\left(S_{t}, t ; K, T\right) & S_{T}<K \\ S_{T}-S_{t}-P\left(S_{t}, t ; K, T\right) & S_{T} \geqslant K\end{cases}
$$

For $S_{T}<K \quad \gamma_{T}$ is constant
for $S_{T} \geqslant K \quad Y_{T}$ is a linearly increasing functon of $S_{T}$. It follows that the minimum value of of $r_{T}$ occurs for $S_{T}<K$,

$$
\gamma_{\tau}^{-}=K-S_{t}-P\left(S_{t}, t ; K, \tau\right)
$$

For $S_{T} \geqslant K \quad V_{T}$ is unbounded thus there is no maximum. The break even asset price is given by

$$
\begin{aligned}
& S_{T}-S_{t}-P\left(S_{t}, t ; K, T\right)=0 \\
\Rightarrow & S_{T}=S_{t}+P\left(S_{t}, t ; K, T\right)
\end{aligned}
$$

if

$$
S_{T}<S_{t}+P\left(S_{t}, t ; k, \tau\right)
$$

since it has been assumed that $S_{T} \geqslant K$ it follows that

$$
\begin{array}{cc} 
& K \leqslant S_{t}+P\left(S_{t}, t ; K, T\right) \\
\Rightarrow \quad & K-S_{t}-P\left(S_{t}, t ; K, T\right) \leqslant 0
\end{array}
$$

$$
\Rightarrow \quad r_{T}^{-} \leq 0
$$

This result also places abound on $5 t$

$$
S_{t} \geqslant K+P\left(S_{t}, t, K, T\right.
$$

In summary the portidio minionum protit is given by

$$
\gamma_{\tau}^{-}=K-S_{t}-P\left(S_{t}, t ; K_{1} \tau\right) \leqslant 0
$$

There is no maximum profit since the propit linearty indeases without bound.

The expression for $\gamma_{T}^{-}$leads to the following constraints,

$$
\begin{aligned}
& K-S_{t}-P\left(S_{t}, t ; K, T\right) \leq 0 \\
\Rightarrow & K \leq S_{t}+P\left(S_{t}, t ; K, T\right)
\end{aligned}
$$

$$
\Rightarrow K-P\left(S_{t}, t ; K, T\right) \leqslant S_{t}
$$

The break even point for the portfolio is given by,

$$
S_{\tau}=S_{t}+P\left(S_{t}, t, K, \tau\right)
$$

The following pot shows the profit for a protected put portfolio
Note that the protected put strategy has a bourded lose and unbowned gains
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-008.jpg?height=676&width=936&top_left_y=1318&top_left_x=326)

## Comparison of Covered and Protected Hedging strategies

A covered strategy is used by sellers of ptions to hedge the short option position. A put strategy is used by buyers of an option to hedge a long or short position in an asset.
It is teresting to compare the payoff of the covered call and protected call and the covered put and protected put. Fist consider the call hedging strategies
The first plot shows the covered call and the second the protected call.

The short and long calls are symmetric about the
$S_{T}$ axis indicating the relation betwen the payofts,

$$
\psi_{T}^{\text {lons }}=-\psi_{T}^{\text {short }}
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-010.jpg?height=588&width=684&top_left_y=521&top_left_x=100)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-010.jpg?height=561&width=716&top_left_y=556&top_left_x=826)

The same relation exists between payopts of the short and long positions in the asset. It follows that the payoffs of the covered and protected cals have the same relationship

$$
\psi_{T}^{\text {covered }}=-\psi_{T}^{\text {protected }}
$$

This is easily verified by
inspecting the payoff functions

$$
\begin{aligned}
& \psi_{T}^{\text {covered }}=S_{T}-\max \left(S_{T}-K, 0\right) \\
& \psi_{T}^{\text {Protected }}=\max \left(S_{T}-K, 0\right)-S_{T}
\end{aligned}
$$

The same relation holds for the profits.
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-011.jpg?height=1182&width=891&top_left_y=796&top_left_x=310)

$$
\begin{aligned}
r_{T}^{\text {covered }}=S_{t} & -S_{T}+\max \left(S_{T}-K, 0\right) \\
& -c\left(S_{t}, t ; K, T\right)
\end{aligned}
$$

$\gamma_{T}^{\text {Protected }}=S_{T}-S_{T}-\max \left(S_{T}-K, 0\right)$

$$
\begin{gathered}
+C\left(S_{t}, t ; K, T\right) \\
\gamma_{T}^{\text {covered }}=-\gamma_{T}^{\text {Protected }}
\end{gathered}
$$

The same relationships hold for covered and protected put strategies.
The following plots show the payoffs covered and protected put stratesy
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-012.jpg?height=535&width=602&top_left_y=1459&top_left_x=211)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-012.jpg?height=506&width=668&top_left_y=1455&top_left_x=874)

$$
\begin{aligned}
\psi_{T}^{\text {Covered }} & =-S_{T}-\max \left(K-S_{T}, 0\right) \\
\psi_{T}^{\text {Proteded }} & =\max \left(K-S_{T}, 0\right)+S_{T} \\
\psi_{T}^{\text {covered }} & =-\psi_{T}^{\text {Protected }}
\end{aligned}
$$

Fanally the profits are shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-013.jpg?height=553&width=1522&top_left_y=872&top_left_x=20)

$$
\begin{aligned}
\gamma_{T}^{\text {Covered }}= & S_{t}-S_{T}-\max \left(K-S_{T} 0\right) \\
& +P\left(S_{t}, t ; K, T\right) \\
\gamma_{T}^{\text {Protected }}= & S_{T}-S_{t}+\max \left(K-S_{T}, 0\right) \\
& -P\left(S_{t}, t ; K, T\right)
\end{aligned}
$$

## Problems 506: Covered Protected Examples

## Probem 5

At time $t$ consider a writer of a covered call on a $\$ 35$ stock with a strike price of $\$ 40$. The premium of the call option is $\$ 1.75$ Calculate the writer's maximum gain and loss at expiry time $T>t$.
Recall that a covered call has a bounded gain and loss. The maximum and minimum profits are given by

$$
\begin{aligned}
& \gamma_{T}^{+}=K-S_{t}+c\left(S_{t}, t ; K, T\right) \\
& \gamma_{T}^{-}=c\left(S_{t}, t ; K, T\right)-S_{t}
\end{aligned}
$$

Here

$$
\begin{array}{ll}
S_{t}=\$ 35 & k=\$ 40 \\
C\left(S_{t}, t ; k, T\right) & =\$ 1.75
\end{array}
$$

It follows that

$$
\begin{aligned}
\gamma_{\tau}^{+} & =\$ 40-\$ 35+\$ 1.75 \\
& =\$ 6.75 \\
\gamma_{\tau}^{-} & =\$ 1.25-\$ 35 \\
& =-\$ 33.25
\end{aligned}
$$

## Problem 6

At time $t$ a writer buys a stock for $\$ 33$ and buys a put option with strike price $\$ 25$ for $\$ 1.75$. What is the maximum gain and loss of this protective strategy.
Recall that a protective put has an unbounded gain and and a maximum loss of,

$$
\gamma_{\tau}^{-}=K-S_{t}-P\left(S_{t}, t ; K, \tau\right)
$$

It follows that

$$
\begin{aligned}
\gamma_{T}^{-}= & \$ 25-\$ 33-\$ 1.75 \\
= & -\$ 9.75
\end{aligned}
$$

## Properties of Option Prices

## Call Options

Consider a call option with expiry date $T$ and strike price $K$ writen on an asset $S_{T}$ at time $t$ with price $C\left(S_{t}, t ; K_{1} T\right)$
The price at maturity of the option is given by

$$
C\left(S_{T}, T ; K, T\right)=\max \left(S_{T}-K, 0\right)
$$

A lower bound on the option price at any time $t<T$ can be found by considering the present value of the strike price which is its discounted value, nomely

$$
P V(K)=K e^{-r(T-t)}
$$

where $r$ is the risk-free
interest rate. The proposed lower bound is given by,
$C\left(S_{t}, t ; K, T\right) \geqslant \max \left(S_{t}-K e^{-r(T-t)}, 0\right)$
This relation can be proven using a no-arbitrage argument.
Assume that

$$
C\left(S_{t}, t ; K, T\right)<\max \left(S_{t}-K e^{-r(T-t)}, 0\right)
$$

and as a counter example let

$$
\begin{gathered}
S_{t}=100 \quad K=80 \quad r=1090 \\
T-t=1
\end{gathered}
$$

for this case

$$
\begin{aligned}
& S_{t}-k e^{-r(T-t)}=100-80 e^{-0.1} \\
& =27.61
\end{aligned}
$$

assume that $c\left(s_{t, t}, k, T\right)=25$. Perform the following transaction

1. Buy the call option 2. Short sell the stock
2. use the proceeds from 1 and 2 to invest $P V$ cand earn the risk free interest rate

The net result is

1. Buy the call
2. Short sell
3. Invest PV Profit

Belance
. 25
$+100$
-72.39
+2.61

Next it will be shown that for any asset price at expiry the profit can be kept. consider both cases $S_{T} \leqslant K$ and $S_{T}>K$

$$
\begin{array}{lcc}
\text { Long Call Paroff } & \frac{S_{T}}{}=K & \frac{S_{T}}{}>K \\
\text { Short Sell } & 0 & S_{T}-80 \\
\text { Risk-free Investment } & \frac{80}{80} & \frac{80}{5} \\
\cline { 1 - 3 } \text { Cost } & 80-S_{T}>0 & 0
\end{array}
$$

Thus if the option expires worth less the risk-free profit is

$$
2.61+80-S_{T}
$$

and if it expires in-the-money the profit is 2.61. It flows that an arbitrage opportunity exist.
so to prevent arbitrage it must be trat

$$
C\left(S_{t}, t ; K, T\right) \geqslant \max \left(S_{T}-K e^{-r(T-t)}\right)
$$

An upper bound can also be placed on $C(S t, t ; K, T)$. Consder

$$
C\left(S_{t}, t ; K, T\right) \leqslant K e^{-r(T-t)}
$$

This relation can be proven using the no arbitrage argument Assume that

$$
C\left(S_{t}, t ; K, T\right)>K e^{-r(T-t)}
$$

A risk-free transaction can be constructed as follows.

1. Sell a call option
2. Buy a share of stock
3. Invest $C\left(S_{t, t} ; K, T\right)-S_{t}>0$

At option maturity the investment has value

$$
\left[c\left(S_{t}, t, K, T\right)-S_{T}\right] e^{r T}
$$

consider the cases $S_{T} \leqslant K$ and $S_{T}>K$
The portfolio payoff is given by

$$
\begin{aligned}
\psi_{T}=S_{T} & -\max \left(S_{T}-K, 0\right) \\
& +\left[C\left(S_{t}, t, K, T\right)-S_{T}\right] e^{r T}
\end{aligned}
$$

Assume $S_{T} \leqslant K$ then

$$
\psi_{T}=S_{T}+\left[C\left(S_{t}, t ; K T\right)-S_{T}\right] e^{r T}>0
$$

and for $S_{T}>K$

$$
\begin{aligned}
\psi_{T} & =S_{T}-\left(S_{T}-K\right)+\left[C\left(S_{t}, t ; K T\right)-S_{T}\right] e^{r T} \\
& =K+\left[C\left(S_{t}, t ; K T\right)-S_{T}\right] e^{r T}>0
\end{aligned}
$$

Now

$$
r_{T}=\psi_{T}+c\left(S_{t}, t, K, T\right)>0
$$

since $\psi_{t}>0$ and $c\left(S_{t}, t ; K, T\right)>0$. It follows that a risk free
profit is possible. Thus,

$$
C\left(s_{t}, t ; k, T\right) \leqslant K e^{-r(T-t)}
$$

and
$\max \left(S_{\tau}-K e^{-r(T-t)}\right) \leqslant C\left(S_{t}, t ; K, T\right) \leqslant K e^{-r(T-t)}$

Next consider two call options purchased at the same time, $t$, on the asset $s_{t}$ with the same expiry date $T$ but different strike prices

$$
K_{1}<K_{2}
$$

The payoff is shown below
It is easily seen that the payoff of the option with the smaller strike price is more profitable thus

$$
\max \left(S_{\tau}-k_{1}, 0\right)>\max \left(S_{\tau}-k_{2}, 0\right)
$$

$$
\Rightarrow C\left(S_{T}, T ; K_{1}, T\right)>C\left(S_{T}, T, K_{2}, T\right)
$$

![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-024.jpg?height=648&width=1217&top_left_y=346&top_left_x=245)

Using the assumption of no arbitrage it can be shown that

$$
c\left(s_{t}, t ; k_{1}, T\right)>c\left(s_{t}, t ; k_{2}, T\right)
$$

It follows that the call option price is a decreasing
function of the strike price.
Assume that

## $c\left(s_{t}, t, k_{1}, T\right) \leq c\left(s_{t}, t ; k_{2}, T\right)$

for $k_{1}<k_{2}$
Perform the following transaction

1. sell a call option at $K_{2}$
2. Buy a call option at $k_{1}$
3. Invest $C_{k_{2}}-C_{k_{1}}>0$ risk free interest rate

It follows that the portfolio payoff is given by

$$
\begin{aligned}
\psi_{T}= & \psi_{T}^{S}+\psi_{T}^{L}+\left(C_{k_{2}}-C_{k_{1}}\right) e^{r T} \\
= & \max \left(S_{T}-k_{1}, 0\right)-\max \left(S_{T} \cdot k_{2}, 0\right) \\
& +\left(C_{k_{2}}-C_{k_{1}}\right) e^{r T}
\end{aligned}
$$

Assume that $S_{T} \leq K_{1}$, then

$$
\psi_{T}=\left(C_{k_{2}}-C_{k_{1}}\right) e^{r t}>0
$$

Since $K_{2}>K_{1}$ and for $K_{1}<S_{T} \leqslant K_{2}$

$$
\psi_{T}=S_{T}-K_{1}+\left(C_{K_{2}}-C_{K_{1}}\right) e^{r T}>0
$$

and for $S_{T}>K_{2}$

$$
\begin{aligned}
\psi_{T}= & \left(S_{T}-K_{1}\right)-\left(S_{T}-K_{2}\right) \\
& +\left(C_{K_{2}}-C_{K_{1}}\right) e^{r T} \\
= & K_{2}-K_{1}+\left(C_{K_{2}}-C_{K_{1}}\right) e^{r T}>0
\end{aligned}
$$

The profit is given by
$\gamma_{T}=\psi_{T}+c\left(S_{t}, t, K_{2}, T\right)-c\left(S_{t} t ; K_{1}, T\right)$
Now

$$
\psi_{T}>0
$$

and it is assumed that

$$
C\left(S_{t}, t, K_{2}, T\right)-C\left(S_{t}, t ; K_{1}, T\right)>0
$$

thus

$$
\gamma_{\tau}>0
$$

It follows that a risk free profit is possible thus

$$
c\left(S_{t}, t, K_{1}, T\right)>c\left(S_{t}, t ; K_{2}, T\right)
$$

for $k_{1}<k_{2}$

## Put options

Consider a put option with expry date $T$ and strike price $k$ writen on an asset $s_{t}$ at time $t$ with price $P\left(S_{t}, t ; K, T\right)$ The price at maturily is given by

$$
P\left(S_{T}, T ; K, T\right)=\max \left(K-S_{T}, 0\right)
$$

A lower bound on the option price at any time $t<T$ can be found by considering the present value of the strike price which is its discounted value, namely

$$
P V(K)=K e^{-r(T-t)}
$$

where $r$ is the risk-free interest rate

The proposed lower bound is, $P\left(S_{t}, t ; K, T\right) \geqslant \max \left(K e^{-\Gamma(T-t)}-S_{t}, 0\right)$

This relation can be proven using a no-arbitrage argument. Assume that
$P\left(S_{t}, t ; K, T\right)<\max \left(K e^{-r(T-t)}-S_{t}, 0\right)$
and as a counter eample let

$$
\begin{aligned}
S_{t}=60 \quad K & =80 \quad r=1090 \\
T-t & =1
\end{aligned}
$$

for this case

$$
\begin{aligned}
& K e^{-r(T t)}-S_{t}=80 e^{-0.1}-60 \\
& =12.39
\end{aligned}
$$

Assume that $P\left(S_{t, t} ; K, \tau\right)=10$ and perform the following transactions

1. Borrow money at the risk free interest rate to purchase the stock. and buy the put.
2. Buy the put option
3. Buy the stock

The net result is

1. Borrow Money

Balance
2. Purchase Put
+70

3 Purchace stock

$$
-10
$$

$-\frac{60}{0}$

Next it will be shown that for any asset price at expiry the profit can be kept. consider both cases $S_{T} \leq K$ and $S_{T}>K$. The amount needed to pay off the loan is $\$ 77.36$

Long Put sell stock

$$
S_{T}=K \quad S_{T}>K
$$

Payoff Loan Profit
$80-S_{T}$
$+S_{T}$

$$
\frac{-77.36}{+2.64}
$$

0 $+S_{T}$
-77.36
$S_{T}-72.36>0$

Thus a risk-free profit is made regardless of the price at maturity of the option.
It follows that

$$
P\left(S_{t}, t ; K, \tau\right) \geqslant \max \left(K e^{-r(\tau-t)}-S_{t}, 0\right)
$$

An upper bound can also be placed on $P\left(S_{t}, t ; K, T\right)$. Consoler

$$
P\left(S_{t}, t ; k, T\right) \leqslant K e^{-r(T-t)}
$$

This relation can be proven using the no arbitrage argument Assume that

$$
P\left(S_{t}, t ; K, T\right)>K e^{-r(T-t)}
$$

A risk-free transaction can be constructed as follows.

1. sell a put option
2. Short sell $S_{T}$
3. Invest $P\left(S_{t, t} ; K, T\right)+S_{t}>0$

At option matwrity the investment has value

$$
\left[P\left(S_{t}, t ; K, T\right)+S_{T}\right] e^{r T}
$$

Consider the cases $S_{T} \leqslant k$ and $S_{T}>K$
The portfolio payoff is given by

$$
\begin{aligned}
\psi_{T}=-S_{T} & -\max \left(K-S_{T}, 0\right) \\
& +\left[P\left(S_{t}, t, K T\right)+S_{T}\right] e^{r T}
\end{aligned}
$$

Assume $S_{T} \leqslant K$ then

$$
\begin{aligned}
u_{T}=-S_{T}-\left(K-S_{T}\right)+ & {\left[P\left(S_{t}, t ; K T\right)+S_{T}\right] e^{r T} } \\
=-K+ & {\left[P\left(S_{t}, t ; K T\right)+S_{T}\right] e^{r T} }
\end{aligned}
$$

but it is assumed that

$$
\begin{aligned}
& P\left(S_{t}, t ; K, T\right)>K e^{-r(T-t)} \\
\Rightarrow & e^{r T} P\left(S_{t}, t ; K, T\right)>K e^{r t}>K
\end{aligned}
$$

thus

$$
\psi_{T}=-K+\left[P\left(S_{t}, t ; K T\right)+S_{T}\right] e^{r T}>0
$$

next consider $S_{T}>K$

$$
\begin{aligned}
\psi_{\tau} & =-S_{T}+\left[P\left(S_{t}, t ; K T\right)+S_{T}\right] e^{r T} \\
& =P\left(S_{t}, t ; K, T\right) e^{r T}+S_{T}\left(e^{r T}-L\right)>0
\end{aligned}
$$

The profit is given by

$$
\gamma_{T}=\psi_{T}+P\left(S_{T}, t ; K_{T} T\right)>0
$$

since $\psi_{\tau}>0$ and $P\left(S_{t}, t, K, T\right)>0$
Thus a risk free profit is possible it follows that

$$
P\left(S_{t}, t ; K, T\right) \leqslant K e^{-r(T-t)}
$$

and
$K e^{-r(T-t)} \geqslant P\left(S_{t, t}, K, T\right) \geqslant \max \left(K e^{-r(T-t)}-S_{t, 0}\right)$
Next consider two put options
purchased at the same time, $t$, on the asset $s_{t}$ with the same expiry date $T$ but different strike prices

$$
K_{2}>K_{1}
$$

The payoff is shown below.
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-035.jpg?height=597&width=819&top_left_y=699&top_left_x=338)

It is easily seen that the payoff of the option with the larger strike price is more profitable

$$
\begin{array}{r}
\max \left(K_{2}-S_{T}, 0\right)>\max \left(K_{1}-S_{T}, 0\right) \\
\Rightarrow P\left(S_{T}, T, K_{2}, T\right)>P\left(S_{T}, T ; K_{1}, T\right)
\end{array}
$$

Using the assumption of no arbitrage it can be shown that

$$
P\left(S_{t}, t ; K_{2}, T\right)>P\left(S_{t}, t ; K_{1}, T\right)
$$

It follows that the call option price is an increasing function of the strike price.

Assume that

$$
P\left(S_{t}, t ; K_{2}, T\right) \leqslant P\left(S_{t}, t ; K_{1}, T\right)
$$

for $K_{2}>K_{1}$
Perform the following transaction

1. sell a put option at
2. Buy a put option at
3. Invest $P_{k_{1}}-P_{k_{2}}$ at the risk free interest rate

It follows that the portfolid payoff is given by

$$
\begin{aligned}
\psi_{T}= & \psi_{T}^{S}+\psi_{T}^{L}+\left(P_{K_{1}}-P_{K_{2}}\right) e^{r T} \\
= & -\max \left(K_{1}-S_{T}, 0\right)+\max \left(K_{2}-S_{T}, 0\right) \\
& +\left(P_{L_{1}}-P_{K_{2}}\right) e^{r T}
\end{aligned}
$$

Assume that $S_{T} \leq K_{1}$, then

$$
\psi_{T}=-K_{1}+S_{T}+\left(K_{2}-S_{T}\right)+\left(P_{K_{1}}-P_{K_{2}}\right) e^{r T}
$$

Since $P_{K_{1}}>P_{K_{2}}$ and $K_{1}<K_{2}$

$$
\psi_{T}=k_{2}-k_{1}+\left(D_{k_{1}}-P_{k_{2}}\right) e^{r T}>0
$$

and for $K_{1}<S_{T} \leqslant K_{2}$

$$
\psi_{2}=k_{2}-S_{T}+\left(P_{k_{1}} \cdot P_{k_{2}}\right) e^{r T}>0
$$

and finally for $S_{7}>K_{2}$

$$
\psi_{T}=\left(P_{K_{1}}-P_{K_{2}}\right) e^{r T}>0
$$

The profit is given by
$r_{T}=\psi_{T}+P\left(s_{t}, t ; k_{1}, T\right)-P\left(s_{t}, t ; k_{2}, T\right)$
but it is assumed that
$P\left(s_{t}, t ; k_{1}, T\right)-P\left(s_{t}, t ; k_{2}, T\right)>0$
Thus

$$
\gamma_{T}>0
$$

It follows that a risk free profit is possible thus
$P\left(S_{t}, t ; K_{1}, T\right)<P\left(S_{t}, t ; K_{2}, T\right)$
for $k_{1}<k_{2}$

## Problem 7: Bull Call Spread

A bull call spread is a hedging position designed to buy a call option $C\left(S_{t}, t ; K_{1}, T\right)$ with strike price $K_{1}$ and smultaneously sell a call option $C\left(S_{t}, t ; K_{2}, T\right)$ with strike price $k_{2}$ where $k_{1} \leqslant k_{2}$ on the same underlying
asset $s_{t}$ and having the asset $s_{t}$ and having the same expry date $T<t$.
show that

$$
c\left(s_{t}, t ; k_{1}, T\right) \geqslant c\left(s_{t}, t ; k_{2}, T\right)
$$

and draw payoff and profit diagrams for a bull spread.

## Solution

At time $t$ the long call contract has price $C\left(s_{t}, t ; k_{1}, T\right)$ and the short call option
has price $C\left(S_{t}, t ; K_{2}, T\right)$.
In the "Properties of option Prices" it was shown that if $K_{1} \leqslant K_{2}$ then

$$
C\left(S_{t} t ; K_{1}, T\right) \geqslant C\left(S_{t}, t ; K_{2}, T\right)
$$

if it is assumed no anbitrage opportunities exist.
The payoff for the long call getion with strike price $k_{1}$ and the short call option with strike price $k_{2}$ are respectively given by

$$
\begin{aligned}
& \psi_{K_{1}, T}^{L}=\max \left(S_{T}-K_{1}, 0\right) \\
& \psi_{K_{2}, T}^{S}=-\max \left(S_{T}-K_{2}, 0\right)
\end{aligned}
$$

It follows that the partfolid payoff is given by

$$
\begin{aligned}
\psi_{T} & =\psi_{K_{1} T}^{L}+\psi_{K_{2}, T}^{S} \\
& =\max \left(S_{T}-K_{1}, 0\right)-\max \left(S_{T}-K_{2}, 0\right) \\
& =c\left(S_{t}, t ; K_{1}, T\right)-c\left(S_{t}, t ; K_{2}, T\right)
\end{aligned}
$$

The payaff is positive if

$$
c\left(S_{t, t} ; K_{1}, T\right) \geqslant c\left(S_{t}, t ; K_{2}, T\right)
$$

Now $k_{1} \leqslant k_{2}$ so if $k_{1} \leqslant S_{T}$

$$
\psi_{\tau}=0
$$

for $k_{1}<s_{T} \leqslant k_{2}$

$$
\psi_{T}=S_{T}-K_{1}
$$

and for $k_{2}<S_{T}$

$$
\begin{aligned}
\psi_{T} & =\left(S_{T}-K_{1}\right)-\left(S_{T}-K_{2}\right) \\
& =K_{2}-K_{1}
\end{aligned}
$$

thus

$$
u_{T}= \begin{cases}0 & S_{T} \leqslant K_{1} \\ S_{T}-K_{1} & K_{1}<S_{T} \leqslant K_{2} \\ K_{2}-K_{1} & K_{2}>S_{T}\end{cases}
$$

The payoff diagrams for the long and short culls and the ball call spread.

Payoff
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-042.jpg?height=831&width=1042&top_left_y=923&top_left_x=270)

Payoff
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-043.jpg?height=892&width=1221&top_left_y=128&top_left_x=130)

The profit for the long call option with strike price $k_{1}$ and the short call with strike price $k_{2}$ are respectively given by

$$
\begin{aligned}
& \gamma_{K_{1}, \tau}^{L}=\max \left(S_{T}-K_{1}, 0\right)-c\left(S_{t}, t ; K_{1}, \tau\right) \\
& V_{K_{2}, \tau}^{S}=-\max \left(S_{T}-K_{2}, 0\right)+c\left(S_{t}, t ; K_{2}, T\right)
\end{aligned}
$$

The bull call spread portfolio profit is given by

$$
\begin{aligned}
\gamma_{T}= & \gamma_{k_{1}, T}^{L}+\gamma_{k_{2}, T}^{s} \\
= & \max \left(s_{T}-k_{1}, 0\right)-\max \left(s_{T}-k_{2}, 0\right) \\
& c\left(s_{t}, t ; k_{2}, T\right)-c\left(s_{t}, t, k_{1}, T\right)
\end{aligned}
$$

For $S_{T} \leqslant K_{1}$

$$
\gamma_{T}=c\left(S_{t}, t ; K_{2}, T\right)-c\left(S_{t}, t ; K_{1}, T\right)
$$

and for $K_{1}<S_{1} \leqslant K_{2}$

$$
\begin{gathered}
V_{T}=S_{T}-K_{1}+C\left(S_{t}, t ; K_{2}, T\right) \\
-C\left(S_{t}, t ; K_{1}, T\right)
\end{gathered}
$$

and finally for $S_{T}>K_{2}$

$$
\begin{aligned}
\gamma_{T}= & \left(S_{T}-K_{1}\right)-\left(S_{T}-K_{2}\right)+c\left(S_{t}, t ; K_{2}, T\right) \\
& -c\left(S_{t}, t ; K_{1}, T\right)
\end{aligned}
$$

$$
\begin{gathered}
=K_{2}-K_{1}+C\left(S_{t}, t ; K_{2}, T\right) \\
-C\left(S_{t}, t ; K_{1}, T\right)
\end{gathered}
$$

## Thus

$$
\gamma_{T}=\left\{\begin{array}{cc}
c\left(S_{t}, t ; K_{2}, T\right)-c\left(S_{t}, t ; K_{1}, T\right) & S_{T} \leq K_{1} \\
S_{T}-K_{1}+c\left(S_{t}, t ; K_{2}, T\right) & K_{1}<S_{T} \leq K_{2} \\
-c\left(S_{t}, t ; K_{1}, T\right) & \\
K_{2}-K_{1}+c\left(S_{t}, t ; K_{2}, T\right) & S_{T}>K_{2} \\
-c\left(S_{t}, t ; K_{1}, T\right) &
\end{array}\right.
$$

Consider $\delta_{\tau} \leqslant K_{1}$
$V_{\tau}=c\left(s_{t}, t ; k_{2}, \tau\right)-c\left(s_{t}, t ; k_{1}, T\right) \leq 0$
since

$$
c\left(S_{t}, t ; K_{1}, T\right) \geqslant c\left(S_{t}, t ; K_{2}, T\right)
$$

Next consider $K_{1}<S_{T} \leqslant K_{2}$. The break even point occurs
on this interval
$S_{T}^{0}-K_{1}+C\left(S_{t}, t ; K_{2}, T\right)-C\left(S_{t}, t ; K_{1}, T\right)=0$
$\Rightarrow S_{T}^{0}=K_{1}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, \tau\right)$

Since $\gamma_{T}$ is a linearly increasing function of $S_{T}$ for $K_{1}<S_{T} \leqslant K_{2}$ if follows that for $S_{T} \geqslant S_{T}^{0}$ that $r_{T} \geqslant 0$. Thus for $S_{T}>K_{2} r_{7}$ is a constant.

$$
\begin{aligned}
& r_{T}= K_{2}-K_{1}+C\left(S_{t}, t ; K_{2}, T\right) \\
&-C\left(S_{t}, t ; K_{1}, T\right) \geqslant 0 \\
& \Rightarrow K_{2}-K_{1} \geqslant C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right) \\
& \text { using } C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right) \geqslant 0 \\
& \text { gives } \\
& K_{2}-K_{1} \geqslant C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right) \geqslant 0
\end{aligned}
$$

The profit diagrams for the long and short calls and the

## Bull call spread are shown below

![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-047.jpg?height=757&width=1088&top_left_y=298&top_left_x=128)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-047.jpg?height=674&width=1192&top_left_y=1144&top_left_x=56)

From an inspection of the profit diagram it is seen that the bull call strategy
has a bounded gain and has a bounded gain and provides leverage. The money risked by the investor is

$$
\Gamma=C\left(S_{t}, t ; K_{1}, T\right)
$$

For convience let

$$
\Delta=c\left(S_{t}, t ; K_{1}, T\right)-c\left(S_{t}, t ; K_{2}, T\right)
$$

It follows that the portfolio break even is given by

$$
K_{1}+\Delta
$$

it follows that for

$$
S_{T}>K_{1}+\Delta
$$

the investor makes a profit and for

$$
S_{T}<K_{1}+\Delta
$$

The investor bses money. The maximum lose is given by

$$
-\Delta
$$

and the maximum gain is given by

$$
\begin{aligned}
K_{2}-K_{1}-\Delta= & K_{2}-K_{1}-C\left(S_{t}, t ; K_{1}, T\right) \\
& +C\left(S_{t}, t, K_{2}, T\right)
\end{aligned}
$$

It follows that the fractional gain is given by

$$
\frac{K_{2}-K_{1}-\Delta}{\Gamma}=\frac{K_{2}-K_{1}+C\left(S_{t}, t, K_{2}, T\right)}{C\left(S_{t}, t, K_{1}, T\right)}-1
$$

## Problem 8: Bull Put Spread

A bull put spread is an investment strategy implemented by buying $a$ put option $P\left(S_{t}, t, K_{1}, T\right)$ and simultaneously selling a put option $P\left(S_{t}, t ; K_{2}, \tau\right)$ on the same underlying asset $s_{t}$ and having the same expiny time $T>t$
show trat

$$
P\left(S_{t}, t, K_{1}, T\right) \leqslant P\left(S_{t}, t ; K_{2}, T\right)
$$

draw the payoff and profit diagrams and disscuss why en investor would use this atratesy.

## Solution

Let $P\left(S_{t}, t, K, T\right)$ denote the long put option and $P\left(s_{t}, t ; K_{2}, T\right)$ denote the short put option.

In the "Properties of option Prices" it was shown that if $k_{1}<k_{2}$ then

$$
P\left(S_{t}, t ; K_{1}, T\right)<P\left(S_{t}, t ; K_{2}, T\right)
$$

If $i t$ is assumed that no arbitrage opportunitres exist. The payoff for the lons put is given by

$$
\psi_{k_{1} T}^{L}=\max \left(k_{1}-s_{T}, 0\right)
$$

and the payoff of the short put option is

$$
U_{K_{2} T}^{s}=-\max \left(K_{2}-S_{T}, 0\right)
$$

The bull put spread portfolio paipff is the sum of the long and short payofis, namely,

$$
\begin{aligned}
\psi_{T} & =\psi_{k_{T} T}^{c}+\psi_{k_{T} T}^{s} \\
& =\max \left(K_{1}-S_{T}, 0\right)-\max \left(K_{2}-S_{T}, 0\right)
\end{aligned}
$$

Thus for $S_{T} \leqslant K_{1}$

$$
\psi_{\tau}=\left(K_{1}-S_{T}\right)-\left(K_{2}-S_{T}\right)=K_{1}-K_{2}
$$

for $K_{1}<S_{T} \leqslant K_{2}$

$$
\psi_{T}=-\left(K_{2}-S_{T}\right)=S_{T}-K_{2}
$$

and for $S_{T}>K_{2}$

$$
\psi_{T}=0
$$

Thus

$$
\psi_{T}=\left\{\begin{array}{cc}
K_{1}-K_{2} & S_{T} \leqslant K_{1} \\
S_{T}-K_{2} & K_{1}<S_{T} \leqslant K_{2} \\
0 & S_{T}>K_{2}
\end{array}\right.
$$

The payoff dragrams for the long and short put options and the bull put spread are shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-053.jpg?height=789&width=885&top_left_y=495&top_left_x=270)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-053.jpg?height=636&width=901&top_left_y=1281&top_left_x=274)

The profit of the bull put spread is the sum of the lons and short put oplions. The profit of the long and short positions

$$
\begin{aligned}
& \psi_{K_{1} T}^{L}=\max \left(K_{1}-s_{T}, O\right)-P\left(s_{t}, t, K_{1}, T\right) \\
& \psi_{K_{2} T}^{S}=-\max \left(K_{2}-s_{T}, O\right)+P\left(s_{t}, t, K_{2}, T\right)
\end{aligned}
$$

It follows that the bull put spread profit is given by

$$
\begin{aligned}
\Psi_{T}= & \Psi_{k_{T}}^{2}+\Psi_{k_{2} T}^{S} \\
= & \max \left(k_{1}-s_{T}, 0\right)-\max \left(k_{2}-s_{T}, 0\right) \\
& +P\left(s_{t}, t ; k_{2}, T\right)-P\left(s_{t}, t ; k_{1}, T\right)
\end{aligned}
$$

It follows that for $s_{T} \leqslant k_{1}$

$$
\begin{aligned}
\psi_{\tau}= & \left(K_{1}-S_{T}\right)-\left(K_{2}-S_{T}\right)+P\left(S_{t}, t ; K_{2}, T\right) \\
& -P\left(S_{t, t} ; K_{1}, T\right)
\end{aligned}
$$

$$
=K_{1}-K_{2}+P\left(S_{t}, t ; K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right)
$$

and for $k_{1}<s_{2} \leqslant k_{2}$

$$
\psi_{T}=K_{2}-S_{T}+P\left(S_{t}, t ; K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right)
$$

and finally for $S_{T}>K_{2}$

$$
\psi_{T}=P\left(s_{t}, t ; k_{2}, T\right)-P\left(s_{t}, t ; k_{1}, T\right)
$$

## Thus

$$
\psi_{T}=\left\{\begin{aligned}
k_{1}-k_{2}+P\left(s_{t}, t ; k_{2}, T\right) & s_{T} \leq k_{1} \\
-P\left(s_{t}, t ; k_{1}, T\right) & k_{1}-s_{T}+P\left(s_{t}, t ; k_{2}, T\right) \\
-P\left(s_{t}, t ; k_{1}, T\right) & k_{1}<s_{T} \leq k_{2} \\
P\left(s_{t}, t ; k_{2}, T\right)-P\left(s_{t}, t ; k_{1}, T\right) & s_{T}>k_{2}
\end{aligned}\right.
$$

using,

$$
K_{2}>K_{1}
$$

and

$$
P\left(S_{t}, t ; K_{2}, T\right)>P\left(S_{t}, t ; K_{1}, T\right)
$$

It is seen that for $S_{T}>K_{2}$ that

$$
\begin{aligned}
Y_{T} & =P\left(S_{t}, t ; K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right) \\
& >0
\end{aligned}
$$

The break even point occurs for $k_{1}<\delta_{T} \leqslant k_{2}$ and is given by

$$
\begin{aligned}
\psi_{\tau}= & K_{1}-S_{T}^{0}+P\left(S_{t}, t ; K_{2}, T\right) \\
& -P\left(S_{t}, t ; K_{1}, T\right) \\
=0 & \\
\Rightarrow S_{\tau}^{0}= & K_{1}+P\left(S_{t}, t ; K_{2}, T\right) \\
& -P\left(S_{t}, t ; K_{1}, T\right)
\end{aligned}
$$

It follows that for $S_{T}<S_{T}^{0}$ that $4_{T}<0$, thus for $s_{T} \leqslant k_{1}$

$$
\begin{aligned}
& \psi_{\tau}=k_{1}-k_{2}+P\left(S_{t}, t ; K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right) \\
&\langle 0 \\
&=K_{2}-K_{1}> P\left(S_{t}, t, K_{2}, T\right) \\
&-P\left(S_{t}, t ; K_{1}, T\right) \\
&>0
\end{aligned}
$$

The profit diagrams for the long and short put options and bull put spread is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-057.jpg?height=708&width=829&top_left_y=1263&top_left_x=354)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-058.jpg?height=800&width=1102&top_left_y=126&top_left_x=196)

The bull put spread strategy has a profit smilar to the call put spread but uses put options. An investor would use this strategy if it is expected that the tock will increase. The profit and loss are both bounded and the strategy provides leverage. The cost of investing in a bull put spread is

$$
C=P\left(S_{t}, t ; K_{1}, T\right)
$$

This cost is much less than purchasing the stock which provides leverage.

To simplify let,

$$
\Delta=P\left(s_{t}, t ; k_{2}, T\right)-P\left(s_{t}, t ; k_{1}, T\right)>0
$$

The portfolio is profitable if

$$
S_{T}>K_{i}+\Delta
$$

and has a lose if

$$
S_{T}<K_{1}+\Delta
$$

The maximum lose occurs for

$$
S_{T} \leqslant K
$$

and is given by

$$
-\left(K_{2}-K_{1}-\Delta\right)
$$

The maximum profit occurs for $S_{7} \geqslant K_{2}$ and is given

$$
\Delta=P\left(S_{t}, t ; K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right)
$$

The maximum fractional gain

$$
\frac{\Delta}{c}=\frac{P\left(S_{t}, t ; K_{2}, T\right)}{P\left(S_{t}, t ; K_{1}, T\right)}-1
$$

## Problem 9: Bear Call Spread

A bear call spread is a hesfing strategy implemented by selling a call option $C\left(s_{t}, t, k_{1}, \tau\right)$ with strike price $k_{1}$ and simultaneously buy a call option $C\left(S_{t}, t ; K_{2}, T\right)$ with strike price $k_{2}$ with $k_{1} \leqslant k_{2}$ on the same underlying asset $S_{t}$ and having the same expiry time $T>t$. show that

$$
C\left(S_{t}, t ; K_{1}, T\right) \geqslant C\left(S_{t}, t ; K_{2}, T\right)
$$

Draw the payoff and profit diagrams for a bear call spread
Discuss under what conditions an investor should invest using the strategy.

## Solution

At time $t$ the short call contract has price $C\left(s_{t}, t ; k_{1}, T\right)$ and the long call option has proce $C\left(S_{t}, t ; K_{2}, T\right)$

In the "Properties of option Prices" it was shown that if $K_{1} \leqslant K_{2}$ then

$$
C\left(S_{t} t ; K_{1}, T\right) \geqslant C\left(S_{t}, t ; K_{2}, T\right)
$$

if it is assumed no arbitrage opportunities exist.

The payoff function for the bear call spread is the sum of payoff of the long call and short call options. Recall that the payoff of long and short call options is given by

$$
\begin{aligned}
& \psi_{K_{1} T}^{S}=-\max \left(S_{T}-K_{1}, 0\right) \\
& \psi_{K_{2} T}^{L}=\max \left(S_{T}-K_{2}, 0\right)
\end{aligned}
$$

It follaws that the paraff for the bear call spread is given by

$$
\psi_{T}=-\max \left(S_{T}-k_{1}, 0\right)+\max \left(S_{T}-k_{2}, 0\right)
$$

Recall that the payoff of the bull call spread is given by

$$
\Psi_{T}^{b u l}=\max \left(S_{T}-K_{1}, 0\right) \cdot \max \left(S_{T}-K_{2}, 0\right)
$$

Thus

$$
\psi_{T}^{\text {becr }}=-\psi_{T}^{\text {ball }}
$$

it follows that the pagoff of the bear call spread is given by

$$
u_{T}=\left\{\begin{array}{cl}
0 & s_{T} \leqslant k_{1} \\
-\left(s_{T}-k_{1}\right) & k_{1}<s_{T} \leqslant k_{2} \\
-\left(k_{2}-k_{1}\right) & k_{2}>s_{T}
\end{array}\right.
$$

The payoff diagrams are brown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-064.jpg?height=831&width=1281&top_left_y=832&top_left_x=114)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-065.jpg?height=963&width=1446&top_left_y=100&top_left_x=42)

For the pagoff it was shown that

$$
\psi_{T}^{\text {bear }}=\psi_{T}^{\text {bull }}
$$

The same relationship holds for profit

$$
\gamma_{T}^{\text {bear }}=-\gamma_{T}^{\text {but }}
$$

## So

$$
\gamma_{T}= \begin{cases}c\left(S_{t}, t ; K_{1}, T\right)-c\left(S_{t}, t ; K_{2}, T\right) & S_{T} \leq K_{1} \\ K_{1}-S_{T}+c\left(S_{t}, t ; K_{1}, T\right) & K_{1}<S_{T} \leq K_{2} \\ -c\left(S_{t}, t ; K_{2}, T\right) & \\ K_{1}-K_{2}+c\left(S_{t}, t, K_{1}, T\right) & S_{T}>K_{2} \\ -c\left(S_{t}, t ; K_{2}, T\right) & \end{cases}
$$

Consider $S_{T} \leqslant K_{1}$, since

$$
c\left(s_{t}, t ; k_{2}, T\right)<c\left(s_{t}, t ; k_{1}, T\right)
$$

for $k_{1}<k_{2}$ it follows that

$$
c\left(S_{t}, t ; K_{1}, T\right)-c\left(S_{t}, t ; K_{2}, T\right)>0
$$

The break point for the bear call spread occurs for $k_{1}<s_{1} \leq k_{2}$,

$$
K_{1}-S_{T}^{0}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)=0
$$

$\Rightarrow S_{T}^{0}=K_{1}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)$
thus for $s_{T}<s_{T}^{0} \quad \psi_{T}>0$ and for $S_{T}>S_{T}^{0} \psi_{T}<0$.
It follows that for $S_{T}>K_{2}$
$K_{1}-K_{2}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)<0$
$\Rightarrow K_{2}-K_{1}>C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)$
The profit diagram for the bear call spread is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-067.jpg?height=728&width=1021&top_left_y=1219&top_left_x=310)

The gam and boss of the bear call spread are both bounded. An investor implementing this stratesy thinks the asset price will decrease from its current price. The investor has a gain for

$$
S_{T}<K_{1}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t_{1}, K_{2}, T\right)
$$

and a loss for

$$
S_{T}>K_{1}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t_{1}, K_{2}, T\right)
$$

The maximum gain occurs for

$$
S_{T} \leq K_{1}
$$

and is given by

$$
C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)
$$

and the maxim loss occurs for

$$
S_{T} \geqslant K_{2}
$$

and is given by

$$
K_{1}-K_{2}+C\left(S_{t}, t ; K_{1}, T\right)-C\left(S_{t}, t ; K_{2}, T\right)
$$

## Problem 10: Bear Put Spread

A bear put spread is an investment strategy constructed by selling a put option with price $P\left(S_{t, t}, K_{1}, T\right)$ and strike price $k_{1}$ and buying a put option with price $P\left(S_{t}, t ; K_{2}, T\right)$ and strike price $k_{2}$ at the same time $t$ Both options have the same expiry of $T>t$.
show that for $k_{1}<k_{2}$

$$
P\left(S_{t}, t, K_{1}, T\right)<P\left(S_{t}, t ; K_{2}, T\right)
$$

Draw the paypff and profit diagrams and discuss under what conditions an muestor would invest using this strategy.

## Solution

In the "Properties of Option Prices" it was shown that
if $k_{1}<k_{2}$ then

$$
P\left(S_{t}, t ; K_{1}, T\right)<P\left(S_{t}, t ; K_{2}, T\right)
$$

if it is assumed no anbitrage opportunities exist.

The payoff function for the bear put spread is the sum of payoff of the long call and short call options Recall that the payoff of long and short call options is given by

$$
\begin{aligned}
& \psi_{K_{1} T}^{S}=-\max \left(K_{1}-S_{T}, 0\right) \\
& \psi_{K_{2} T}^{L}=\max \left(K_{2}-S_{T}, 0\right)
\end{aligned}
$$

It follows that the paraff for the bear put spread is given by

$$
\psi_{T}=-\max \left(K_{1}-S_{T}, 0\right)+\max \left(K_{2}-S_{T}, 0\right)
$$

Recall that the payoff of the bull put spread is given by

$$
\Psi_{T}^{b u l l}=\max \left(K_{1}-S_{T}, 0\right)-\max \left(K_{2}-S_{T}, 0\right)
$$

Thus

$$
\psi_{T}^{\text {bear }}=-\psi_{T}^{\text {ball }}
$$

it follows that the papoff of the bear put spread is given by

$$
\psi_{T}=\left\{\begin{array}{cc}
K_{2}-K_{1} & S_{T} \leqslant K_{1} \\
K_{2}-S_{T} & K_{1}<S_{T} \leqslant K_{2} \\
0 & S_{T}>K_{2}
\end{array}\right.
$$

The payoff dragrams for the long and short put options and the bull pat spread are shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-073.jpg?height=713&width=855&top_left_y=505&top_left_x=328)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-073.jpg?height=750&width=1013&top_left_y=1213&top_left_x=318)

The same relationship holds for profit

$$
\begin{gathered}
r_{T}^{\text {bear }}=-r_{T}^{\text {blut }} \\
\text { so }\left\{\begin{aligned}
k_{2}-k_{1}+P\left(s_{t}, t ; k_{1}, T\right) & s_{T} \leqslant k_{1} \\
-P\left(s_{t}, t ; k_{2}, T\right) & \\
k_{2}-s_{T}+P\left(s_{t}, t ; k_{1}, T\right) & k_{1}<s_{T} \leqslant k_{2} \\
-P\left(s_{t}, t ; k_{2}, T\right) & \\
P\left(s_{t}, t ; k_{1}, T\right)-P\left(s_{t}, t ; k_{2}, T\right) & s_{T}>k_{2}
\end{aligned}\right.
\end{gathered}
$$

First consider $S_{T}>K_{2}$ since

$$
P\left(S_{t}, t ; K_{1}, T\right)<P\left(S_{t}, t ; K_{2}, T\right)
$$

if $K_{2}>K_{1}$ it follows that

$$
P\left(S_{t}, t ; K_{1}, T\right)-P\left(S_{t}, t ; K_{2}, T\right)<0
$$

The portfolio break even occurs for $K_{1}<S_{T} \leqslant K_{2}$. It follows that
$k_{2}-S_{T}^{0}+P\left(S_{t}, t ; k_{1}, T\right)-P\left(S_{t}, t ; k_{2}, T\right)=0$
$\Rightarrow S_{T}^{O}=K_{2}+P\left(S_{t}, t, K_{1}, T\right)-P\left(S_{t}, t ; K_{2}, T\right)$
It follows that for $\delta_{\tau}^{0}<S_{T} \psi_{T}<0$ and for $S_{T}>S_{T} \psi_{T}>0$.
Thus for $S_{T} \leqslant K_{1}$

$$
\begin{aligned}
& K_{2}-K_{1}+P\left(S_{t}, t ; K_{1}, T\right)-P\left(S_{t, t} ; K_{2}, T\right)>0 \\
\Rightarrow & K_{2}-K_{1}>P\left(S_{t, t}, K_{2}, T\right)-P\left(S_{t}, t ; K_{1}, T\right)
\end{aligned}
$$

The profit diagram for the bear put spread is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-076.jpg?height=901&width=1270&top_left_y=151&top_left_x=153)

The gain and loss of a bear put spread are both bounded An investor implementing a bear put spread expects the price of an asset to decrease. The investor makes a profit for

$$
S_{T}<K_{2}+P\left(S_{t}, t ; K_{1}, T\right)-P\left(S_{t}, t ; K_{2}, T\right)
$$

and has a bos for
$S_{T}>K_{2}+P\left(S_{t}, t ; K_{1}, T\right)-P\left(S_{t}, t ; K_{2}, T\right)$
The maximum profit occurs for $S_{T}<K_{1}$ and is groen by

$$
K_{2}-K_{1}+P\left(S_{t}, t, K_{1}, T\right)-P\left(S_{t}, t, K_{2}, T\right)
$$

and the maximum loss of

$$
P\left(s_{t}, t ; k_{1}, T\right)-P\left(s_{t}, t ; k_{2}, T\right)
$$

occurs for $S_{1} \geqslant K_{2}$

## Measure Theory

An understarding of measure theor, is required to concerstand the theory of option proing. In this section the basics of measure theory will be reviewed. This includes the necessary background in set theory, the lebesgue integral and differentiation. The discussion will try to keep a focus on the appication to prabability theory.

## Sets and Functions

The power set of a set $\bar{X}$ is denoted by $P_{X}$ and is all possible subsets of $\bar{x}$. If

$$
\bar{x}=\{a, b, c\}
$$

then

$$
\begin{array}{r}
Q_{\Delta}=\{\phi,\{a\},\{b\},\{c\},\{c, b\}, \\
\{b, c\},\{a, c\},\{a, b, c\}\}
\end{array}
$$

Let $X$ and $I$ denote sets. A function $f$ from $\bar{X}$ to $\bar{Y}$ is denoted by

$$
f: \bar{X} \rightarrow I
$$

If this function assigns one element of $b \in I$ to each element $a \in X$ then

$$
b=f(a) \quad \forall a \in \bar{X}
$$

A set function $f$ is defined on the elements of the power set $P_{\text {E }}$ of $I$
The cardinality set function for the set $N$ is defined by
$|A|= \begin{cases}\infty & \text { if A has an infinite } \\ n & \text { number of elements } \\ n & \text { if A has a finite } \\ n & n \\ n & n\end{cases}$

## Example: Cardinatity of $P_{x}$

In this example a function that maps to any set will be defined and used to compute the size of the power set. consider a function defined on the domain set $\bar{X}$ that indicates if an element of $\bar{X}, x \in \mathbb{X}$, is a member of a subset of
I. Such a function would take on a value of $l$ if $x$ is in the subset and 0 if it is not in the set. More formally let $A \subseteq X$ then

$$
\mathbb{1}_{A}(x)= \begin{cases}1 & x \in A \\ 0 & x \notin A\end{cases}
$$

thus $\underline{11}_{A}(\bar{x}): \bar{x} \rightarrow\{0,1\}$. A function of this type is called a charaderistic function or indicator function.

Now the power set of the $n$ element set

$$
\bar{x}_{n}=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

denoted by $P_{x}$ is the set consisting of all possible subsets that can be constucted from the elements of $Z_{n}$. Let $A$ denote a subset of $P_{\bar{x}}, A \in P_{\bar{x}}$

The indicator function can be used to specify the elements of $I_{n}$ that are contained in $A$. For example if $n=3$ and $x_{1}, x_{2} \in A$ then the set

$$
\{1,1,0\}
$$

can be used to represnt membership of the set in A,

$$
\left\{x_{1}, x_{2}, 0\right\} \in P_{I}
$$

For $n=3$ the sets contained in $P_{x}$ can be represented by the graph
$x_{1}$
$x_{2}$
$x_{3}$
<img class="imgSvg" id = "miazwtss33ph1dhw31m" src="data:image/svg+xml;base64,PHN2ZyBpZD0ic21pbGVzLW1pYXp3dHNzMzNwaDFkaHczMW0iIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDE2NiA4OS4yNTAwMTgzNjQ4OTAwMiIgc3R5bGU9IndpZHRoOiAxNjUuODM5MzkwMDU0NjMwNTRweDsgaGVpZ2h0OiA4OS4yNTAwMTgzNjQ4OTAwMnB4OyBvdmVyZmxvdzogdmlzaWJsZTsiPjxkZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1taWF6d3RzczMzcGgxZGh3MzFtLTEiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iOTYuNTU5NjAwNDM4NDA3MjciIHkxPSIyMS4wMDAwMzY3Mjk4MDE0OCIgeDI9IjEyMy44MzkzOTAwNTQ2MzA1NCIgeTI9IjM2Ljc1MDA1NTA5NDY5ODY1Ij48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1taWF6d3RzczMzcGgxZGh3MzFtLTMiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iNjkuMjc5Nzg5NjE2MjIzMjUiIHkxPSIzNi43NTAwMTgzNjQ4OTcxNyIgeDI9Ijk2LjU1OTYwMDQzODQwNzI3IiB5Mj0iMjEuMDAwMDM2NzI5ODAxNDgiPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIyMCUiPjwvc3RvcD48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMTAwJSI+PC9zdG9wPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lLW1pYXp3dHNzMzNwaDFkaHczMW0tNSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSI0MiIgeTE9IjIxIiB4Mj0iNjkuMjc5Nzg5NjE2MjIzMjUiIHkyPSIzNi43NTAwMTgzNjQ4OTcxNyI+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjIwJSI+PC9zdG9wPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9ImxpbmUtbWlhend0c3MzM3BoMWRodzMxbS03IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjY5LjI3OTc2ODQxMDI2MjQ4IiB5MT0iNjguMjUwMDE4MzY0ODkwMDIiIHgyPSI2OS4yNzk3ODk2MTYyMjMyNSIgeTI9IjM2Ljc1MDAxODM2NDg5NzE3Ij48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48bWFzayBpZD0idGV4dC1tYXNrLW1pYXp3dHNzMzNwaDFkaHczMW0iPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSIxMDAlIiBoZWlnaHQ9IjEwMCUiIGZpbGw9IndoaXRlIj48L3JlY3Q+PGNpcmNsZSBjeD0iMTIzLjgzOTM5MDA1NDYzMDU0IiBjeT0iMzYuNzUwMDU1MDk0Njk4NjUiIHI9IjcuODc1IiBmaWxsPSJibGFjayI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iOTYuNTU5NjAwNDM4NDA3MjciIGN5PSIyMS4wMDAwMzY3Mjk4MDE0OCIgcj0iNy44NzUiIGZpbGw9ImJsYWNrIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI2OS4yNzk3ODk2MTYyMjMyNSIgY3k9IjM2Ljc1MDAxODM2NDg5NzE3IiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjQyIiBjeT0iMjEiIHI9IjcuODc1IiBmaWxsPSJibGFjayI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNjkuMjc5NzY4NDEwMjYyNDgiIGN5PSI2OC4yNTAwMTgzNjQ4OTAwMiIgcj0iNy44NzUiIGZpbGw9ImJsYWNrIj48L2NpcmNsZT48L21hc2s+PHN0eWxlPgogICAgICAgICAgICAgICAgLmVsZW1lbnQtbWlhend0c3MzM3BoMWRodzMxbSB7CiAgICAgICAgICAgICAgICAgICAgZm9udDogMTRweCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAgICAgICAgIGFsaWdubWVudC1iYXNlbGluZTogJ21pZGRsZSc7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAuc3ViLW1pYXp3dHNzMzNwaDFkaHczMW0gewogICAgICAgICAgICAgICAgICAgIGZvbnQ6IDguNHB4IEhlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+PGcgbWFzaz0idXJsKCN0ZXh0LW1hc2stbWlhend0c3MzM3BoMWRodzMxbSkiPjxsaW5lIHgxPSI5Ni41NTk2MDA0Mzg0MDcyNyIgeTE9IjIxLjAwMDAzNjcyOTgwMTQ4IiB4Mj0iMTIzLjgzOTM5MDA1NDYzMDU0IiB5Mj0iMzYuNzUwMDU1MDk0Njk4NjUiIHN0eWxlPSJzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLXdpZHRoOjEuMjYiIHN0cm9rZT0idXJsKCcjbGluZS1taWF6d3RzczMzcGgxZGh3MzFtLTEnKSI+PC9saW5lPjxsaW5lIHgxPSI2OS4yNzk3ODk2MTYyMjMyNSIgeTE9IjM2Ljc1MDAxODM2NDg5NzE3IiB4Mj0iOTYuNTU5NjAwNDM4NDA3MjciIHkyPSIyMS4wMDAwMzY3Mjk4MDE0OCIgc3R5bGU9InN0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utd2lkdGg6MS4yNiIgc3Ryb2tlPSJ1cmwoJyNsaW5lLW1pYXp3dHNzMzNwaDFkaHczMW0tMycpIj48L2xpbmU+PGxpbmUgeDE9IjQyIiB5MT0iMjEiIHgyPSI2OS4yNzk3ODk2MTYyMjMyNSIgeTI9IjM2Ljc1MDAxODM2NDg5NzE3IiBzdHlsZT0ic3Ryb2tlLWxpbmVjYXA6cm91bmQ7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS13aWR0aDoxLjI2IiBzdHJva2U9InVybCgnI2xpbmUtbWlhend0c3MzM3BoMWRodzMxbS01JykiPjwvbGluZT48bGluZSB4MT0iNjkuMjc5NzY4NDEwMjYyNDgiIHkxPSI2OC4yNTAwMTgzNjQ4OTAwMiIgeDI9IjY5LjI3OTc4OTYxNjIyMzI1IiB5Mj0iMzYuNzUwMDE4MzY0ODk3MTciIHN0eWxlPSJzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLXdpZHRoOjEuMjYiIHN0cm9rZT0idXJsKCcjbGluZS1taWF6d3RzczMzcGgxZGh3MzFtLTcnKSI+PC9saW5lPjwvZz48Zz48dGV4dCB4PSIxMTkuOTAxODkwMDU0NjMwNTQiIHk9IjQyLjAwMDA1NTA5NDY5ODY1IiBjbGFzcz0iZWxlbWVudC1taWF6d3RzczMzcGgxZGh3MzFtIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IHdyaXRpbmctbW9kZTogaG9yaXpvbnRhbC10YjsgdGV4dC1vcmllbnRhdGlvbjogbWl4ZWQ7IGxldHRlci1zcGFjaW5nOiBub3JtYWw7IGRpcmVjdGlvbjogbHRyOyI+PHRzcGFuPk88L3RzcGFuPjx0c3BhbiBzdHlsZT0idW5pY29kZS1iaWRpOiBwbGFpbnRleHQ7Ij5IPC90c3Bhbj48L3RleHQ+PHRleHQgeD0iMTIzLjgzOTM5MDA1NDYzMDU0IiB5PSIzNi43NTAwNTUwOTQ2OTg2NSIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iOTYuNTU5NjAwNDM4NDA3MjciIHk9IjI4Ljg3NTAzNjcyOTgwMTQ4IiBjbGFzcz0iZWxlbWVudC1taWF6d3RzczMzcGgxZGh3MzFtIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IGdseXBoLW9yaWVudGF0aW9uLXZlcnRpY2FsOiAwOyB3cml0aW5nLW1vZGU6IHZlcnRpY2FsLXJsOyB0ZXh0LW9yaWVudGF0aW9uOiB1cHJpZ2h0OyBsZXR0ZXItc3BhY2luZzogLTFweDsgZGlyZWN0aW9uOiBydGw7IHVuaWNvZGUtYmlkaTogYmlkaS1vdmVycmlkZTsiPjx0c3Bhbj5PPC90c3Bhbj48L3RleHQ+PHRleHQgeD0iOTYuNTU5NjAwNDM4NDA3MjciIHk9IjIxLjAwMDAzNjcyOTgwMTQ4IiBjbGFzcz0iZGVidWciIGZpbGw9IiNmZjAwMDAiIHN0eWxlPSIKICAgICAgICAgICAgICAgIGZvbnQ6IDVweCBEcm9pZCBTYW5zLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAiPjwvdGV4dD48dGV4dCB4PSI2NS4zNDIyODk2MTYyMjMyNSIgeT0iNDIuMDAwMDE4MzY0ODk3MTciIGNsYXNzPSJlbGVtZW50LW1pYXp3dHNzMzNwaDFkaHczMW0iIGZpbGw9ImN1cnJlbnRDb2xvciIgc3R5bGU9InRleHQtYW5jaG9yOiBzdGFydDsgd3JpdGluZy1tb2RlOiBob3Jpem9udGFsLXRiOyB0ZXh0LW9yaWVudGF0aW9uOiBtaXhlZDsgbGV0dGVyLXNwYWNpbmc6IG5vcm1hbDsgZGlyZWN0aW9uOiBsdHI7Ij48dHNwYW4+UDwvdHNwYW4+PC90ZXh0Pjx0ZXh0IHg9IjY5LjI3OTc4OTYxNjIyMzI1IiB5PSIzNi43NTAwMTgzNjQ4OTcxNyIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iNDcuMjUiIHk9IjI2LjI1IiBjbGFzcz0iZWxlbWVudC1taWF6d3RzczMzcGgxZGh3MzFtIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IHdyaXRpbmctbW9kZTogaG9yaXpvbnRhbC10YjsgdGV4dC1vcmllbnRhdGlvbjogbWl4ZWQ7IGxldHRlci1zcGFjaW5nOiBub3JtYWw7IGRpcmVjdGlvbjogcnRsOyB1bmljb2RlLWJpZGk6IGJpZGktb3ZlcnJpZGU7Ij48dHNwYW4+TzwvdHNwYW4+PHRzcGFuIHN0eWxlPSJ1bmljb2RlLWJpZGk6IHBsYWludGV4dDsiPkg8L3RzcGFuPjwvdGV4dD48dGV4dCB4PSI0MiIgeT0iMjEiIGNsYXNzPSJkZWJ1ZyIgZmlsbD0iI2ZmMDAwMCIgc3R5bGU9IgogICAgICAgICAgICAgICAgZm9udDogNXB4IERyb2lkIFNhbnMsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICI+PC90ZXh0Pjx0ZXh0IHg9IjY0LjAyOTc2ODQxMDI2MjQ4IiB5PSI3My41MDAwMTgzNjQ4OTAwMiIgY2xhc3M9ImVsZW1lbnQtbWlhend0c3MzM3BoMWRodzMxbSIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0idGV4dC1hbmNob3I6IHN0YXJ0OyB3cml0aW5nLW1vZGU6IGhvcml6b250YWwtdGI7IHRleHQtb3JpZW50YXRpb246IG1peGVkOyBsZXR0ZXItc3BhY2luZzogbm9ybWFsOyBkaXJlY3Rpb246IGx0cjsiPjx0c3Bhbj5JPC90c3Bhbj48L3RleHQ+PHRleHQgeD0iNjkuMjc5NzY4NDEwMjYyNDgiIHk9IjY4LjI1MDAxODM2NDg5MDAyIiBjbGFzcz0iZGVidWciIGZpbGw9IiNmZjAwMDAiIHN0eWxlPSIKICAgICAgICAgICAgICAgIGZvbnQ6IDVweCBEcm9pZCBTYW5zLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAiPjwvdGV4dD48L2c+PC9zdmc+"/>
<img class="imgSvg" id = "miazwtt8mmtcpyhebk" src="data:image/svg+xml;base64,PHN2ZyBpZD0ic21pbGVzLW1pYXp3dHQ4bW10Y3B5aGViayIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgMTkzIDEyMC43NTAwMTgzNjQ4ODI4OSIgc3R5bGU9IndpZHRoOiAxOTMuMTE5MjAwODc2ODE0NTVweDsgaGVpZ2h0OiAxMjAuNzUwMDE4MzY0ODgyODlweDsgb3ZlcmZsb3c6IHZpc2libGU7Ij48ZGVmcz48bGluZWFyR3JhZGllbnQgaWQ9ImxpbmUtbWlhend0dDhtbXRjcHloZWJrLTEiIGdyYWRpZW50VW5pdHM9InVzZXJTcGFjZU9uVXNlIiB4MT0iMTIzLjgzOTQxMTI2MDU5MTI5IiB5MT0iNTIuNTAwMDM2NzI5Nzk0MzQiIHgyPSIxNTEuMTE5MjAwODc2ODE0NTUiIHkyPSI2OC4yNTAwNTUwOTQ2OTE1Ij48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1taWF6d3R0OG1tdGNweWhlYmstMyIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSI5Ni41NTk2MDA0Mzg0MDcyNyIgeTE9IjY4LjI1MDAxODM2NDg5MDAyIiB4Mj0iMTIzLjgzOTQxMTI2MDU5MTI5IiB5Mj0iNTIuNTAwMDM2NzI5Nzk0MzQiPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIyMCUiPjwvc3RvcD48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMTAwJSI+PC9zdG9wPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lLW1pYXp3dHQ4bW10Y3B5aGViay01IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9Ijk2LjU1OTU3OTIzMjQ0NjUiIHkxPSI5OS43NTAwMTgzNjQ4ODI4OSIgeDI9Ijk2LjU1OTYwMDQzODQwNzI3IiB5Mj0iNjguMjUwMDE4MzY0ODkwMDIiPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIyMCUiPjwvc3RvcD48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMTAwJSI+PC9zdG9wPjwvbGluZWFyR3JhZGllbnQ+PGxpbmVhckdyYWRpZW50IGlkPSJsaW5lLW1pYXp3dHQ4bW10Y3B5aGViay03IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjY5LjI3OTgxMDgyMjE4NDAyIiB5MT0iNTIuNDk5OTk5OTk5OTkyODYiIHgyPSI5Ni41NTk2MDA0Mzg0MDcyNyIgeTI9IjY4LjI1MDAxODM2NDg5MDAyIj48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjxsaW5lYXJHcmFkaWVudCBpZD0ibGluZS1taWF6d3R0OG1tdGNweWhlYmstOSIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiIHgxPSI0MiIgeTE9IjY4LjI0OTk4MTYzNTA4ODU1IiB4Mj0iNjkuMjc5ODEwODIyMTg0MDIiIHkyPSI1Mi40OTk5OTk5OTk5OTI4NiI+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjIwJSI+PC9zdG9wPjxzdG9wIHN0b3AtY29sb3I9ImN1cnJlbnRDb2xvciIgb2Zmc2V0PSIxMDAlIj48L3N0b3A+PC9saW5lYXJHcmFkaWVudD48bGluZWFyR3JhZGllbnQgaWQ9ImxpbmUtbWlhend0dDhtbXRjcHloZWJrLTExIiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgeDE9IjY5LjI3OTgxMDgyMjE4NDAyIiB5MT0iNTIuNDk5OTk5OTk5OTkyODYiIHgyPSI2OS4yNzk4MzIwMjgxNDQ3OCIgeTI9IjIxIj48c3RvcCBzdG9wLWNvbG9yPSJjdXJyZW50Q29sb3IiIG9mZnNldD0iMjAlIj48L3N0b3A+PHN0b3Agc3RvcC1jb2xvcj0iY3VycmVudENvbG9yIiBvZmZzZXQ9IjEwMCUiPjwvc3RvcD48L2xpbmVhckdyYWRpZW50PjwvZGVmcz48bWFzayBpZD0idGV4dC1tYXNrLW1pYXp3dHQ4bW10Y3B5aGViayI+PHJlY3QgeD0iMCIgeT0iMCIgd2lkdGg9IjEwMCUiIGhlaWdodD0iMTAwJSIgZmlsbD0id2hpdGUiPjwvcmVjdD48Y2lyY2xlIGN4PSIxNTEuMTE5MjAwODc2ODE0NTUiIGN5PSI2OC4yNTAwNTUwOTQ2OTE1IiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjEyMy44Mzk0MTEyNjA1OTEyOSIgY3k9IjUyLjUwMDAzNjcyOTc5NDM0IiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjxjaXJjbGUgY3g9Ijk2LjU1OTYwMDQzODQwNzI3IiBjeT0iNjguMjUwMDE4MzY0ODkwMDIiIHI9IjcuODc1IiBmaWxsPSJibGFjayI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iOTYuNTU5NTc5MjMyNDQ2NSIgY3k9Ijk5Ljc1MDAxODM2NDg4Mjg5IiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjxjaXJjbGUgY3g9IjY5LjI3OTgxMDgyMjE4NDAyIiBjeT0iNTIuNDk5OTk5OTk5OTkyODYiIHI9IjcuODc1IiBmaWxsPSJibGFjayI+PC9jaXJjbGU+PGNpcmNsZSBjeD0iNDIiIGN5PSI2OC4yNDk5ODE2MzUwODg1NSIgcj0iNy44NzUiIGZpbGw9ImJsYWNrIj48L2NpcmNsZT48Y2lyY2xlIGN4PSI2OS4yNzk4MzIwMjgxNDQ3OCIgY3k9IjIxIiByPSI3Ljg3NSIgZmlsbD0iYmxhY2siPjwvY2lyY2xlPjwvbWFzaz48c3R5bGU+CiAgICAgICAgICAgICAgICAuZWxlbWVudC1taWF6d3R0OG1tdGNweWhlYmsgewogICAgICAgICAgICAgICAgICAgIGZvbnQ6IDE0cHggSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZjsKICAgICAgICAgICAgICAgICAgICBhbGlnbm1lbnQtYmFzZWxpbmU6ICdtaWRkbGUnOwogICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgLnN1Yi1taWF6d3R0OG1tdGNweWhlYmsgewogICAgICAgICAgICAgICAgICAgIGZvbnQ6IDguNHB4IEhlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIDwvc3R5bGU+PGcgbWFzaz0idXJsKCN0ZXh0LW1hc2stbWlhend0dDhtbXRjcHloZWJrKSI+PGxpbmUgeDE9IjEyMy44Mzk0MTEyNjA1OTEyOSIgeTE9IjUyLjUwMDAzNjcyOTc5NDM0IiB4Mj0iMTUxLjExOTIwMDg3NjgxNDU1IiB5Mj0iNjguMjUwMDU1MDk0NjkxNSIgc3R5bGU9InN0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utd2lkdGg6MS4yNiIgc3Ryb2tlPSJ1cmwoJyNsaW5lLW1pYXp3dHQ4bW10Y3B5aGViay0xJykiPjwvbGluZT48bGluZSB4MT0iOTYuNTU5NjAwNDM4NDA3MjciIHkxPSI2OC4yNTAwMTgzNjQ4OTAwMiIgeDI9IjEyMy44Mzk0MTEyNjA1OTEyOSIgeTI9IjUyLjUwMDAzNjcyOTc5NDM0IiBzdHlsZT0ic3Ryb2tlLWxpbmVjYXA6cm91bmQ7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS13aWR0aDoxLjI2IiBzdHJva2U9InVybCgnI2xpbmUtbWlhend0dDhtbXRjcHloZWJrLTMnKSI+PC9saW5lPjxsaW5lIHgxPSI5Ni41NTk1NzkyMzI0NDY1IiB5MT0iOTkuNzUwMDE4MzY0ODgyODkiIHgyPSI5Ni41NTk2MDA0Mzg0MDcyNyIgeTI9IjY4LjI1MDAxODM2NDg5MDAyIiBzdHlsZT0ic3Ryb2tlLWxpbmVjYXA6cm91bmQ7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS13aWR0aDoxLjI2IiBzdHJva2U9InVybCgnI2xpbmUtbWlhend0dDhtbXRjcHloZWJrLTUnKSI+PC9saW5lPjxsaW5lIHgxPSI2OS4yNzk4MTA4MjIxODQwMiIgeTE9IjUyLjQ5OTk5OTk5OTk5Mjg2IiB4Mj0iOTYuNTU5NjAwNDM4NDA3MjciIHkyPSI2OC4yNTAwMTgzNjQ4OTAwMiIgc3R5bGU9InN0cm9rZS1saW5lY2FwOnJvdW5kO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utd2lkdGg6MS4yNiIgc3Ryb2tlPSJ1cmwoJyNsaW5lLW1pYXp3dHQ4bW10Y3B5aGViay03JykiPjwvbGluZT48bGluZSB4MT0iNDIiIHkxPSI2OC4yNDk5ODE2MzUwODg1NSIgeDI9IjY5LjI3OTgxMDgyMjE4NDAyIiB5Mj0iNTIuNDk5OTk5OTk5OTkyODYiIHN0eWxlPSJzdHJva2UtbGluZWNhcDpyb3VuZDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLXdpZHRoOjEuMjYiIHN0cm9rZT0idXJsKCcjbGluZS1taWF6d3R0OG1tdGNweWhlYmstOScpIj48L2xpbmU+PGxpbmUgeDE9IjY5LjI3OTgxMDgyMjE4NDAyIiB5MT0iNTIuNDk5OTk5OTk5OTkyODYiIHgyPSI2OS4yNzk4MzIwMjgxNDQ3OCIgeTI9IjIxIiBzdHlsZT0ic3Ryb2tlLWxpbmVjYXA6cm91bmQ7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS13aWR0aDoxLjI2IiBzdHJva2U9InVybCgnI2xpbmUtbWlhend0dDhtbXRjcHloZWJrLTExJykiPjwvbGluZT48L2c+PGc+PHRleHQgeD0iMTQ3LjE4MTcwMDg3NjgxNDU1IiB5PSI3My41MDAwNTUwOTQ2OTE1IiBjbGFzcz0iZWxlbWVudC1taWF6d3R0OG1tdGNweWhlYmsiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3R5bGU9InRleHQtYW5jaG9yOiBzdGFydDsgd3JpdGluZy1tb2RlOiBob3Jpem9udGFsLXRiOyB0ZXh0LW9yaWVudGF0aW9uOiBtaXhlZDsgbGV0dGVyLXNwYWNpbmc6IG5vcm1hbDsgZGlyZWN0aW9uOiBsdHI7Ij48dHNwYW4+TzwvdHNwYW4+PC90ZXh0Pjx0ZXh0IHg9IjE1MS4xMTkyMDA4NzY4MTQ1NSIgeT0iNjguMjUwMDU1MDk0NjkxNSIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iMTIzLjgzOTQxMTI2MDU5MTI5IiB5PSI2MC4zNzUwMzY3Mjk3OTQzNCIgY2xhc3M9ImVsZW1lbnQtbWlhend0dDhtbXRjcHloZWJrIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IGdseXBoLW9yaWVudGF0aW9uLXZlcnRpY2FsOiAwOyB3cml0aW5nLW1vZGU6IHZlcnRpY2FsLXJsOyB0ZXh0LW9yaWVudGF0aW9uOiB1cHJpZ2h0OyBsZXR0ZXItc3BhY2luZzogLTFweDsgZGlyZWN0aW9uOiBydGw7IHVuaWNvZGUtYmlkaTogYmlkaS1vdmVycmlkZTsiPjx0c3Bhbj5PPC90c3Bhbj48L3RleHQ+PHRleHQgeD0iMTIzLjgzOTQxMTI2MDU5MTI5IiB5PSI1Mi41MDAwMzY3Mjk3OTQzNCIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iOTIuNjIyMTAwNDM4NDA3MjciIHk9IjczLjUwMDAxODM2NDg5MDAyIiBjbGFzcz0iZWxlbWVudC1taWF6d3R0OG1tdGNweWhlYmsiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3R5bGU9InRleHQtYW5jaG9yOiBzdGFydDsgd3JpdGluZy1tb2RlOiBob3Jpem9udGFsLXRiOyB0ZXh0LW9yaWVudGF0aW9uOiBtaXhlZDsgbGV0dGVyLXNwYWNpbmc6IG5vcm1hbDsgZGlyZWN0aW9uOiBsdHI7Ij48dHNwYW4+STwvdHNwYW4+PC90ZXh0Pjx0ZXh0IHg9Ijk2LjU1OTYwMDQzODQwNzI3IiB5PSI2OC4yNTAwMTgzNjQ4OTAwMiIgY2xhc3M9ImRlYnVnIiBmaWxsPSIjZmYwMDAwIiBzdHlsZT0iCiAgICAgICAgICAgICAgICBmb250OiA1cHggRHJvaWQgU2Fucywgc2Fucy1zZXJpZjsKICAgICAgICAgICAgIj48L3RleHQ+PHRleHQgeD0iOTEuMzA5NTc5MjMyNDQ2NSIgeT0iMTA1LjAwMDAxODM2NDg4Mjg5IiBjbGFzcz0iZWxlbWVudC1taWF6d3R0OG1tdGNweWhlYmsiIGZpbGw9ImN1cnJlbnRDb2xvciIgc3R5bGU9InRleHQtYW5jaG9yOiBzdGFydDsgd3JpdGluZy1tb2RlOiBob3Jpem9udGFsLXRiOyB0ZXh0LW9yaWVudGF0aW9uOiBtaXhlZDsgbGV0dGVyLXNwYWNpbmc6IG5vcm1hbDsgZGlyZWN0aW9uOiBsdHI7Ij48dHNwYW4+STwvdHNwYW4+PC90ZXh0Pjx0ZXh0IHg9Ijk2LjU1OTU3OTIzMjQ0NjUiIHk9Ijk5Ljc1MDAxODM2NDg4Mjg5IiBjbGFzcz0iZGVidWciIGZpbGw9IiNmZjAwMDAiIHN0eWxlPSIKICAgICAgICAgICAgICAgIGZvbnQ6IDVweCBEcm9pZCBTYW5zLCBzYW5zLXNlcmlmOwogICAgICAgICAgICAiPjwvdGV4dD48dGV4dCB4PSI2OS4yNzk4MTA4MjIxODQwMiIgeT0iNDQuNjI0OTk5OTk5OTkyODYiIGNsYXNzPSJlbGVtZW50LW1pYXp3dHQ4bW10Y3B5aGViayIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0idGV4dC1hbmNob3I6IHN0YXJ0OyBnbHlwaC1vcmllbnRhdGlvbi12ZXJ0aWNhbDogMDsgd3JpdGluZy1tb2RlOiB2ZXJ0aWNhbC1ybDsgdGV4dC1vcmllbnRhdGlvbjogdXByaWdodDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7IGRpcmVjdGlvbjogbHRyOyI+PHRzcGFuPkk8L3RzcGFuPjwvdGV4dD48dGV4dCB4PSI2OS4yNzk4MTA4MjIxODQwMiIgeT0iNTIuNDk5OTk5OTk5OTkyODYiIGNsYXNzPSJkZWJ1ZyIgZmlsbD0iI2ZmMDAwMCIgc3R5bGU9IgogICAgICAgICAgICAgICAgZm9udDogNXB4IERyb2lkIFNhbnMsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICI+PC90ZXh0Pjx0ZXh0IHg9IjQ3LjI1IiB5PSI3My40OTk5ODE2MzUwODg1NSIgY2xhc3M9ImVsZW1lbnQtbWlhend0dDhtbXRjcHloZWJrIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IHdyaXRpbmctbW9kZTogaG9yaXpvbnRhbC10YjsgdGV4dC1vcmllbnRhdGlvbjogbWl4ZWQ7IGxldHRlci1zcGFjaW5nOiBub3JtYWw7IGRpcmVjdGlvbjogcnRsOyB1bmljb2RlLWJpZGk6IGJpZGktb3ZlcnJpZGU7Ij48dHNwYW4+TzwvdHNwYW4+PHRzcGFuIHN0eWxlPSJ1bmljb2RlLWJpZGk6IHBsYWludGV4dDsiPkg8L3RzcGFuPjwvdGV4dD48dGV4dCB4PSI0MiIgeT0iNjguMjQ5OTgxNjM1MDg4NTUiIGNsYXNzPSJkZWJ1ZyIgZmlsbD0iI2ZmMDAwMCIgc3R5bGU9IgogICAgICAgICAgICAgICAgZm9udDogNXB4IERyb2lkIFNhbnMsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICI+PC90ZXh0Pjx0ZXh0IHg9IjY0LjAyOTgzMjAyODE0NDc4IiB5PSIyNi4yNSIgY2xhc3M9ImVsZW1lbnQtbWlhend0dDhtbXRjcHloZWJrIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0eWxlPSJ0ZXh0LWFuY2hvcjogc3RhcnQ7IHdyaXRpbmctbW9kZTogaG9yaXpvbnRhbC10YjsgdGV4dC1vcmllbnRhdGlvbjogbWl4ZWQ7IGxldHRlci1zcGFjaW5nOiBub3JtYWw7IGRpcmVjdGlvbjogbHRyOyI+PHRzcGFuPkk8L3RzcGFuPjwvdGV4dD48dGV4dCB4PSI2OS4yNzk4MzIwMjgxNDQ3OCIgeT0iMjEiIGNsYXNzPSJkZWJ1ZyIgZmlsbD0iI2ZmMDAwMCIgc3R5bGU9IgogICAgICAgICAgICAgICAgZm9udDogNXB4IERyb2lkIFNhbnMsIHNhbnMtc2VyaWY7CiAgICAgICAgICAgICI+PC90ZXh0PjwvZz48L3N2Zz4="/>

Each layer of the graph represents membership of the element with the same index in a set. The total number of sets will be the number of leaf nodes. For $n=3$ this is

$$
\partial^{3}=8
$$

For $n$ elements the total number of elements in $P_{x}$ will be given by, the cardinality

$$
2^{n}
$$

Definition: set Function
For any function calso called, mapping, operators or tranformation)

$$
f: \underline{x} \rightarrow \underline{y}
$$

if $A C \bar{x}$ then

$$
f(A)=\{f(a): a \in A\} \subset I
$$

Thus any function definces a set function in a natural way

The domain of a function is the set of permissable inputs and the range the outputs of function Por the specified domain

Example: Reman Integral
Consider a continuous function on $\mathbb{R} f(x)$. The Riemann Integral defines a set function on finite intervals

$$
F([a, b])=\int_{a}^{b} f(x) d x
$$

A goal of measure theory is to extend the defintion of this integral to sets beyond
intervals on $\mathbb{R}$.

## Definition : Onto function

A function $f: \underline{x} \rightarrow I$ is onta (also carled a surjection or surjective function) if $\forall b \in I$ there exists $a \in \bar{X}$ where at least one

$$
f(a)=b
$$

The following diagram illustrates an onto function
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-085.jpg?height=416&width=819&top_left_y=1120&top_left_x=348)

An example onto continuous function is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-086.jpg?height=519&width=1065&top_left_y=193&top_left_x=227)

Definition: One-to-one function A function $f: \bar{X} \rightarrow \bar{Y}$ is one-to-one calso called an injuction or injective function) if $\forall a, b \in \mathbb{X}$

$$
a=b \Rightarrow f\left(a_{1}\right)=f\left(a_{2}\right)
$$

The following diagram illustrates a one-to-one function
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-087.jpg?height=442&width=863&top_left_y=84&top_left_x=294)

A function that is both onto and one-to-one is illustrated below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-087.jpg?height=445&width=872&top_left_y=906&top_left_x=328)

Thus $\forall a \in \bar{X} \Rightarrow f(a) \in \bar{I}$ and for $\forall a, b \in I$ if $a=b$ then $f(a)=f(b)$

A continuous function that is both one-to-one and onto is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-088.jpg?height=529&width=731&top_left_y=90&top_left_x=378)

## Example: All Mapping Fipes

All of the varieties of mappings are illustrated in the following diagrams

Diagram (1) shows an injective mapping also known as a one to-one mapping which is defined by

$$
\forall a, b \in \bar{x}, f(a)=f(b) \Rightarrow a=b
$$

Thus for an injection every element in the range of $f(x)$ maps to a unique element in the domain but not all elements in the domain are represented in the range.

(1)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-089.jpg?height=486&width=569&top_left_y=814&top_left_x=82)

injection one-to-one
(2)

![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-089.jpg?height=479&width=570&top_left_y=777&top_left_x=888)
surjective onto

Diagram (2) shows surjective mapping or onto mapping. A surjective is defined by
$\forall y \in I \quad \exists x \in I$ such that $y=f(x)$

In words every element in the domain of $f(\bar{x})$ is mappel to by at least one element in the range. Since it is possible trat mutiple elements of I can map to the same element in I it follows that $\forall a, b \in \bar{S} f(a)=f(b) \nRightarrow a=b$ thus $a$ surjection cannot be an injection unless every element of I is mapped to by a single element of $\bar{X}$. Later it will be seen that placing this constraint on a surject lecds to a bijection.

Diagram (3) illustrates a mapping that is both surjectur and injective. This type of mapping is called a bijection $\Delta$ bijection is invertable since every element of $\bar{x}$ maps to a single element
(3)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-091.jpg?height=473&width=567&top_left_y=209&top_left_x=82)
injective and surjective function bjection
(4)
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-091.jpg?height=475&width=565&top_left_y=209&top_left_x=878)
not surjective or injective
of I and every element of I is mapped to by one element of I. A bijectue mapping is injecture since it satisfies

$$
\forall a, b \in \bar{X}, f(a)=f(b) \Rightarrow a=b
$$

Recall that a surgetive map satisfies
$\forall y \in I \quad \exists x \in I$ such that $y=f(x)$

This relation leaves open the possibity that multiple elements of I dould map to the scme element in I. It follows that to aslo be surjective the additional constraint that only one element of $\bar{X}$ maps to an element of $y$,
$\forall y \in I \quad \exists 1 x \in I$ such that $y=f(x)$
Thus a bijection is both a surjection and injection
Finally diagram (4) illustrates a mapping that is not surjective or injective since it satisfies neither

$$
\forall a, b \in \bar{X}, f(a)=f(b) \Rightarrow a=b
$$

or
$\forall y \in I \quad \exists x \in I$ such that $y=f(x)$

The following condition can be seen to hod for all mapping $\forall x \in \overline{\underline{X}}, \exists 1, y \in I$ such that $y=f(x)$
In words the states that for every element of $\bar{x}$ there exists one element of I such trat $y=f(x)$

## Definition: Inverse Map

Let $f: \bar{X} \rightarrow I$ be a map from the domain $\bar{x}$ to the range I the inverse image of a point $y \in I$ is defined as

$$
f^{-1}(y)=\{x: x \in \bar{X} \text { and } f(x)=y\}
$$

The inverse map or muerse of $f$ is the map

$$
f^{-1}: I \rightarrow D_{\bar{X}}
$$

where $P_{E}$ is the power set of $X$.

As an example consider

$$
f(x)=x^{2}=y
$$

which is a mapping from $\mathbb{R}$ to $\mathbb{R}^{+}$. It follows that the inverse image is,

$$
f^{-1}(x)=\{-\sqrt{y}, \sqrt{y}\} \quad y \geqslant 0
$$

Consider the mapping from $\mathbb{R}^{2}$ to $\mathbb{R}^{+}$

$$
f(x, y)=x^{2}+y^{2}=2
$$

it follows that $f^{-1}(z)$ is a circle of radius $\sqrt{2}$ in $\mathbb{R}^{2}$. for $z>0$. That is for each 2 in $\mathbb{R}^{+}$the inverse is a circle in $\mathbb{R}^{2}$.

Next consider

$$
f(x)=\sin (x)=y
$$

Which is a maping from $\mathbb{R}$ to $[-1,1]$. The inverse is

$$
f^{-1}(y)=\arcsin (y)
$$

which is a mapping from $[-1,1]$ to $\mathbb{R}$.
Next consder the mapping from $\mathbb{R}$ to $\mathbb{R}$

$$
f(x)=x^{3}=y
$$

it follows trat

$$
f^{-1}(y)=y^{1 / 3}
$$

which also is a mapping from $\mathbb{R}$ to $\mathbb{R}$.

Finally consider the averaging
operator $c([a, b])$ mapping to $\mathbb{R}$

$$
c([a, b])=\frac{1}{b-a} \int_{a}^{b} f(x) d x
$$

$f^{-1}(c)$ is the set of continuous functions that have average c.

Definition: Partitions and Equivalence Classes

The partion of $a$ set $\bar{x}$ is a grouping of the elements of $\bar{x}$ into nonepty subsets such that each element is in only one subset.
An equivalence relation is a banary relation between elements of a set that is reflexive, symmetric and transitive. If the equivalence relation is denoted by ~ and $a, b, c \in \bar{X}$ The riquirments for an
equivalence relation can be writen in the following manner
reflexive: $a \sim a$
Symetric: $a \sim b$
transitive: $a \sim b$ and $b \sim c=a \sim c$
A partition is induced on a set by an equivatence relation. If all equivalent elements are placed in a subset each etement of $\bar{X}$ will be in only one subset creating the partition. Different equivalence relations will create different portions. A subset of $I$ which contains equivalent elements is called an equivalence class. Equivalence class of an element $a \in D$ is denoted by $[a]$ where

$$
[a]=\{b \in \bar{X} \mid a \sim b\}
$$

If $b \in[a]$ then $b$ is called the represenctive of the of the equivalence class $[a]$ any element of the equroatence class may be choosen as represenative.
The set of all equivatence classes of $\bar{X}$ is called the quotient set of $\bar{X}$ by the relation $\sim$ and is denoted by

$$
\bar{x} / \sim=\{[a] \mid a \in \bar{x}\}
$$

Properties of equivalence classes wre

1. $\forall a \in \mathbb{X}, a \in[a]$
2. $\forall a, b \in \mathbb{Z}, a \sim b \Rightarrow[a]=[b]$
3. Every pair of equivalence classes are either equal or disjoint
$\forall a, b \in \mathbb{X}$ either $[a]=[b]$ or $[a] \cap[b]=\varnothing$

Let $\bar{X}_{1}, I_{2}, \bar{X}_{3}, \ldots, \bar{I}_{n}$ be non-emply subsets of $I$. The subsets are a partition if

1. $\bigcup_{i=1}^{n} X_{i}=\bar{S}$
2. No sets in the partition are empty

$$
\forall i \quad \bar{x}_{i} \neq \varnothing
$$

3. All sets in the partition are disjoint

$$
A_{i} \cap A_{j}=\varnothing \quad i \neq j
$$

## Example: Partition Probems

1. List all of the partitions of the following sets $\{1,2\}$ and $\{1,2,3\}$
The partions of a set can be deduced by inspecting
the powerset to determine all combinates that satisfy the defintion of a partition. If $\underline{X}$ is the set under consideration the subsets $D_{i} \in P_{I}$ that satisfy

$$
\begin{gathered}
\bigcup_{i=1}^{n} X_{i}=\bar{X}, \quad \forall i \quad \bar{X}_{i} \neq \varnothing \\
A_{i} \cap A_{j}=\varnothing \quad i \neq j
\end{gathered}
$$

For the first set $\bar{X}=\{1,2\}$

$$
P_{\bar{x}}=\{\varnothing,\{1\},\{2\},\{1,2\}\}
$$

two partitions are aparent

$$
\begin{aligned}
& *\{\{1\},\{2\}\} \\
& *\{\{1,2\}\}
\end{aligned}
$$

For the second set $\bar{X}=\{1,2,3\}$

$$
\begin{array}{r}
Q_{x}=\{\varnothing,\{1\},\{2\},\{3\},\{1,2\}, \\
\{1,3\},\{2,3\},\{1,2,3\}\}
\end{array}
$$

The following are partitions

$$
\begin{aligned}
& *\{\{1\},\{2\},\{3\}\} \\
& *\{\{1,2\},\{3\}\} \\
& *\{\{1,3\},\{2\}\} \\
& *\{\{1\},\{2,3\}\} \\
& *\{\{1,2,3\}\}
\end{aligned}
$$

Thus there are $s$ partitions.
2. List the ordered pairs in the equivalence relation in duced by the partition

$$
\{\{a, b, c\},\{d\},\{e\}\}
$$

of the set $\{a, b, c, d, e\}$ The equivalence relations can be deduced by applying the definition of an equivalence relation to each element of the partition, namely,

$$
a \sim a, a \sim b
$$

## $a \sim b$ and $b \sim c=a \sim c$

so for the first element $\{a, b, c\}$

* $R=a \sim a, a \sim b, a \sim c, b \sim b b \sim a, b \sim c, c \sim a, c \sim b, c \sim c$
for the secord element $\{d\}$

$$
* \quad R=d \sim d
$$

and for the firal element $\{e\}$

$$
\text { * } R=e \sim e
$$

3. A relation $\sim$ on the set $\bar{X}=\{a, b, c, d, e\}$ is defined by the equivalence pairs
$a \sim a, a \sim b, b \sim a, b \sim b$, $c \sim c, c \sim d, c \sim e, d \sim c, d \sim d d \sim c$, $e \sim c$, end, eve
determine the equivalence
classes induced by the equivalence relation.
The equivalence classes can be infered from the definition of con equivalence relation and equivalence class, namely,

$$
a \sim a \quad a \sim b
$$

$a \sim b$ and $b \sim c \Rightarrow a \sim c$
cond for the equivalence class [a]

$$
\begin{gathered}
\forall a \in I, \quad a \in[a] \\
\forall a, b \in I, \quad a \sim b \Rightarrow[a]=[b]
\end{gathered}
$$

$\forall a, b \in D$ either $[a]=[b]$ or $[a] \cap[b]=\varnothing$
From inspection of the equivalence relation any set of mutually equivalent elements will form an
equivalence class.
The relations
$R=a \sim a, a \sim b, b \sim a, b \sim b$
induce the equivalence class

* $\{a, b\}$
and the relations
$R=c \sim c, c \sim d, c \sim e, d \sim c, d \sim d$
duc, enc, end, eve
induce the class
* $\{c, d, e\}$
clearly these equivalence classes form a partion of $\bar{X}$ since

1. $\{a, b\} \cup\{c, d, e\}=\{a, b, c, d, e\}$

$$
=\mathbb{Z}
$$

2. $\{a, b\} \neq \varnothing \quad\{c, d, e\} \neq \varnothing$
3. $\{a, b\} \cap\{c, d, e\}=\varnothing$
4. Define the following equivalence relation on the set of integers $z$

$$
\{a \sim b:|a+1|=|b+1|\}
$$

let

$$
\ln |=|a+1|=|b+1|
$$

To see the pattern let $n=0$ then

$$
\begin{aligned}
& |n|=0=|a+| | \\
\Rightarrow & a=-1
\end{aligned}
$$

and

$$
\begin{aligned}
& \ln 1=0=|b+1| \\
\Rightarrow & b=-1
\end{aligned}
$$

Thus there is only 1 equivalence relation

$$
\text { - } 1 \sim-1
$$

The equivalence class
has a single element given by

$$
[-1]=\{-1\}
$$

next assume that $n=1$ then

$$
\begin{aligned}
& \ln 1=1=|a+|1| \\
& \Rightarrow a=0,-2
\end{aligned}
$$

similarly for

$$
\begin{aligned}
& |n|=1=|b+1| \\
\Rightarrow & b=0,-2
\end{aligned}
$$

this leads to the following equivalence relations
$R=0 \sim 0,0 \sim-2,-2 \sim 0,-2 \sim-2$
These relations induce the following equivalence class,

$$
[-2]=\{-2,0\}
$$

for $n=2$

$$
\begin{aligned}
& |n|=2=|a+|1| \\
& \Rightarrow a=-3,1
\end{aligned}
$$

and

$$
\begin{aligned}
& |n|=2=|b+1| \\
\Rightarrow & b=-3,1
\end{aligned}
$$

this leads to the following equivalence relations
$R=-3 \sim-3,-3 \sim 1,1 \sim-3,1 \sim 1$
These relations lead to the following equivalence class

$$
[-3]=\{-3,1\}
$$

clearly for $n<0$ the equivalence sets are equal since

$$
\ln 1=|-n|
$$

Thus without loss of generality assume $n>0$.

$$
n=|a+1|
$$

This leads to the two equations

$$
\begin{array}{rlrlrl}
a+1 & =-n & a+1 & =n & =n-1 \\
\Rightarrow a & =-n-1 & \Rightarrow a & =n-n
\end{array}
$$

soluing for $b$ leads to the same result. Thus the equivalence class contains two elements

$$
[-n-1]=\{-n-1, n-1\} \quad n>0
$$

6. Suppose $R$ is an equivalence relation on a finite set $A$ where every equivalence class has the same cardinality, $m$, show that the cardinatity of $R, I R L$, and the cardinality of $A,|A|$,
are related by

$$
|R|=|A| m
$$

If every equivalence class has the same cardinality, $m$, all elements are involved an equivalence relation. The number of relations will be the number of pairs which is given by

$$
m(m-1)
$$

Here because of the symetric relation both orderings are counted. Because of reflexive relation there will be an additional $m$ relations. It follows that for each equivalence class there will

$$
\begin{aligned}
\left|R_{i}\right| & =m(m-1)+m \\
& =m^{2}-m+m \\
& =m^{2}
\end{aligned}
$$

equivalence relations.

If $n$ is the number of equivalence classes and since each element of $A$ is in only one equivalence class it follows that the cardirality of $A$ is given by

$$
\begin{aligned}
& |A|=m n \\
\Rightarrow & n=\frac{|A|}{m}
\end{aligned}
$$

Since there are $n$ equivalence classes the cardinality of the equivalence relation set is given by

$$
|R|=n m^{2}=|A| m
$$

which is the desired result.

Example Bell Numbers
The Bell number of a set is the total number of
different partitions which is the same as the number of equivalence relations that can be applied to the set.
To derive the expression for the Bell numbers consider the set

$$
\bar{X}_{n}=\left\{x_{1}, x_{2}, x_{3}, \ldots, x_{n}\right\}
$$

with cardinality $n$. Let $B_{n}$ denote the n'th Bell number. It will be shown that

$$
B_{n+1}=\sum_{k=0}^{n}\binom{n}{k} B_{n}
$$

The argument to derive an expression for the n'th Bell number successively joins $x_{n}$ to all previous partitions for all possible permutations. In this way the defintion of a partition is satisfied. namely,

$$
\begin{gathered}
\bigcup_{i=1}^{n} \bar{X}_{i}=\bar{X}, \quad \forall i \quad \bar{X}_{i} \neq \varnothing \\
A_{i} \cap A_{j}=\varnothing \quad i \neq j
\end{gathered}
$$

The analysis of the calculation of Bell numbers uses the following approach.
Let

$$
\begin{aligned}
\mathbb{Z}_{n+1} & =\left\{x_{1}, x_{2}, \ldots, x_{n}, x_{n+1}\right\} \\
& =\mathbb{X}_{n} \cup\left\{x_{n+1}\right\}
\end{aligned}
$$

Assume there is a portition of Inti given by

$$
\bar{X}_{n+1}=A_{1} \cup A_{2} \cup \cdots A_{m}
$$

an further assume that

$$
x_{n+1} \in A_{1}
$$

and that $0 \leqslant k \leqslant n$ other elements of $Z_{n}$ are elements of $A_{1}$ such that

$$
\left|A_{1}\right|=K+1
$$

the number of elements in $A_{2} \cup A_{3} \cup \cdots \cup A_{m}$ will be

$$
n+1-(k+1)=n-k
$$

where $A_{2} \cup A_{3} \cup \cdots$. $A m$ is a partition of $\Sigma_{n-k}$

It is assumed that the Bell numbers for $\Sigma_{n-k}$ are known and denoted by $B_{n-k}$. Now for a given $K$ there will be

$$
\binom{n}{k}
$$

choices of the $k$ elements from $Z_{n}$ that are in $A_{1}$. The remaing elemements form the set $\bar{x}_{n-k}$ which has Bell number Bn-k

It follows that the total number of partitions for a given $k$ will be

$$
\binom{n}{k} B_{n-k}
$$

and the total number of partitions of $x_{n+1}$ is

$$
B_{n+1}=\sum_{k=0}^{n}\binom{n}{k} B_{n-k}
$$

Now

$$
\binom{n}{k}=\frac{n!}{k!(n-k)!}=\binom{n}{n-k}
$$

50

$$
\begin{aligned}
B_{n+1} & =\sum_{k=0}^{n}\binom{n}{n-k} B_{n-k} \\
& =\sum_{k=0}^{n}\binom{n}{k} B_{k}
\end{aligned}
$$

which is the desired result

In the following examples will be explatily worked out for $n=3,4$ and 5 .

Consder $n=0$ so that

$$
\bar{X}_{0}=\{\phi\}
$$

To obtain the correct answere for $B_{1}$ it is assumed that

$$
B_{0}=1
$$

for $n=1$

$$
I_{1}=\left\{x_{1}\right\}
$$

which has a single partition

$$
P_{1}=\left\{\left\{x_{1}\right\}\right\}
$$

so

$$
B_{1}=1
$$

Next consider,

$$
\begin{aligned}
\bar{x}_{2} & =\bar{x}_{1} \cup\left\{x_{2}\right\} \\
& =\left\{x_{1}, x_{2}\right\}
\end{aligned}
$$

There are two partitions

$$
\begin{array}{r}
P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\}\right\} \\
P_{2}=\left\{\left\{x_{1}, x_{2}\right\}\right\}
\end{array}
$$

so

$$
B_{2}=2
$$

Next consider

$$
\bar{X}_{3}=\left\{x_{1}, x_{2}, x_{3}\right\}
$$

The previous partions are

$$
\begin{aligned}
& P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\}\right\}
\end{aligned}
$$

First consider adding $\left\{x_{3}\right\}$ to $P_{1}$ and $P_{2}$

$$
\begin{aligned}
& P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{3}\right\},\left\{x_{3}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\}\right\}
\end{aligned}
$$

Next consider adding $\left\{x_{1}, x_{3}\right\}$ and $\left\{x_{2}, x_{3}\right\}$ this will give the partitions

$$
\begin{aligned}
& P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\}
\end{aligned}
$$

and finally

$$
P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\}\right\}
$$

so

$$
B_{3}=5
$$

Finally consider

$$
I_{4}=\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}
$$

The $I_{3}$ partitions are,

$$
P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\}
$$

$$
\begin{aligned}
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\}\right\} \\
& P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\} \\
& P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\}\right\}
\end{aligned}
$$

First add $\left\{x_{4}\right\}$ to each of the partitions

$$
\begin{aligned}
& P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\},\left\{x_{4}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\},\left\{x_{4}\right\}\right\} \\
& P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\},\left\{x_{4}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\},\left\{x_{4}\right\}\right\} \\
& P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\},\left\{x_{4}\right\}\right\}
\end{aligned}
$$

Next consider the pairs

$$
\begin{aligned}
& \left\{x_{1}, x_{4}\right\},\left\{x_{2}, x_{4}\right\},\left\{x_{3}, x_{4}\right\} \\
& P_{6}=\left\{\left\{x_{1}, x_{4}\right\},\left\{x_{2}, x_{3}\right\}\right\}
\end{aligned}
$$

$$
\begin{aligned}
& P_{7}=\left\{\left\{x_{1}, x_{4}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\} \\
& P_{8}=\left\{\left\{x_{2}, x_{4}\right\},\left\{x_{1}, x_{3}\right\}\right\} \\
& P_{9}=\left\{\left\{x_{2}, x_{4}\right\},\left\{x_{1}\right\},\left\{x_{3}\right\}\right\} \\
& P_{10}=\left\{\left\{x_{3}, x_{4}\right\},\left\{x_{1}, x_{2}\right\}\right\} \\
& P_{11}=\left\{\left\{x_{3}, x_{4}\right\},\left\{x_{1}\right\},\left\{x_{3}\right\}\right\}
\end{aligned}
$$

Next consider the triples

$$
\begin{aligned}
&\left\{x_{1}, x_{2}, x_{4}\right\}\left\{x_{1}, x_{4}, x_{3}\right\}\left\{x_{4}, x_{2}, x_{3}\right\} \\
& P_{12}=\left\{\left\{x_{1}, x_{2}, x_{4}\right\},\left\{x_{3}\right\}\right\} \\
& P_{13}=\left\{\left\{x_{1}, x_{4}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
& P_{14}=\left\{\left\{x_{4}, x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\}
\end{aligned}
$$

Finally

$$
P_{15}=\left\{\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}\right\}
$$

So

$$
B_{4}=15
$$

Thus in summary

$$
n=0 \quad k=0 \quad B_{0}=1 \quad \bar{x}_{0}=\{\phi\}
$$

$$
\begin{aligned}
& n=1 \quad B_{1}=1 \mathbb{X}_{1}=\left\{x_{1}\right\} \\
& K=0 \quad P_{1}=\left\{\left\{x_{1}\right\}\right\} \\
& n=2 B_{2}=2 \quad \mathbb{X}_{2}=\left\{x_{1}, x_{2}\right\} \\
& K=0 \quad P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\}\right\} \\
& K=1 \quad P_{2}=\left\{\left\{x_{1}, x_{2}\right\}\right\} \\
& n=3 B_{3}=5 \quad \mathbb{D}_{3}=\left\{x_{1}, x_{2}, x_{3}\right\} \\
& K=0 P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\}\right\}
\end{aligned}
$$

$$
\begin{aligned}
k=1 & P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\} \\
k=2 & P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\}\right\}
\end{aligned}
$$

and finally

$$
\begin{aligned}
n=4 \quad & B_{4}=15 \quad \bar{X}_{4}=\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\} \\
k=0 \quad & P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\},\left\{x_{4}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\},\left\{x_{4}\right\}\right\} \\
& P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\},\left\{x_{4}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\},\left\{x_{4}\right\}\right\} \\
& P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\},\left\{x_{4}\right\}\right\}
\end{aligned}
$$

$$
\begin{aligned}
k=1 P_{7} & =\left\{\left\{x_{1}, x_{4}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\} \\
P_{8} & =\left\{\left\{x_{2}, x_{4}\right\},\left\{x_{1}, x_{3}\right\}\right\} \\
P_{9} & =\left\{\left\{x_{2}, x_{4}\right\},\left\{x_{1}\right\},\left\{x_{3}\right\}\right\} \\
P_{10} & =\left\{\left\{x_{3}, x_{4}\right\},\left\{x_{1}, x_{2}\right\}\right\} \\
P_{11} & =\left\{\left\{x_{3}, x_{4}\right\},\left\{x_{1}\right\},\left\{x_{3}\right\}\right\} \\
k=2 P_{12} & =\left\{\left\{x_{1}, x_{2}, x_{4}\right\},\left\{x_{3}\right\}\right\} \\
P_{13} & =\left\{\left\{x_{1}, x_{4}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
P_{14} & =\left\{\left\{x_{4}, x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\} \\
k=3 P_{15} & =\left\{\left\{x_{1}, x_{2}, x_{3}, x_{4}\right\}\right\}
\end{aligned}
$$

As an example $B_{3}$ will be evaluted in some detail. The partions for $\bar{x}_{3}$ are siven by
To interpret results the Bell numer expression of the form

$$
B_{n+1}=\sum_{k=0}^{n}\binom{n}{k} B_{n-k}
$$

is used. All the partitions for $x_{3}$ are listed

$$
\begin{array}{ll}
k=0 & P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\} \\
& P_{2}=\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\}\right\} \\
k=1 & P_{3}=\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\}\right\} \\
& P_{4}=\left\{\left\{x_{2}, x_{3}\right\},\left\{x_{1}\right\}\right\} \\
k=2 & P_{5}=\left\{\left\{x_{1}, x_{2}, x_{3}\right\}\right\}
\end{array}
$$

Also, the partitions for $I_{2}$ are

$$
\begin{array}{ll}
k=0 & P_{1}=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\}\right\} \\
k=1 & P_{2}=\left\{\left\{x_{1}, x_{2}\right\}\right\}
\end{array}
$$

and the $\bar{X}_{1}$ partions

$$
K=0 \quad P_{1}=\left\{\left\{x_{1}\right\}\right\}
$$

and finally I $_{0}$ which is
not really a partition

$$
P_{0}=\{\varnothing\}
$$

Now $B_{3}$ is given by

$$
B_{3}=\binom{2}{0} B_{2}+\binom{2}{1} B_{1}+\binom{2}{2} B_{0}
$$

The frost term represents the partitions formed by the union of $\left\{x_{3}\right\}$ with the partions of $\bar{X}_{2}$. The second term the union of $\left\{x_{1}, x_{3}\right\}$ and $\left\{x_{2}, x_{3}\right\}$ with the partions of $\bar{I}_{1}$ and the last term the union of $\left\{x_{1}, x_{2}, x_{3}\right\}$.
For the first term using $\bar{X}_{2}^{P}$ to denote a partition of $\underline{X}_{2}$

$$
\begin{array}{r}
\left.\left\{x_{1}\right\},\left\{x_{2}\right\},\left\{x_{3}\right\}\right\}=\bar{X}_{2}^{P} \cup\left\{\left\{x_{3}\right\}\right\} \\
\left.=\left\{\left\{x_{1}\right\},\left\{x_{2}\right\}\right\} \cup\left\{x_{3}\right\}\right\}
\end{array}
$$

$$
\begin{array}{r}
\left\{\left\{x_{1}, x_{2}\right\},\left\{x_{3}\right\}\right\}=X_{2}^{P} \cup\left\{\left\{x_{3}\right\}\right\} \\
=\left\{\left\{x_{1}, x_{2}\right\}\right\} \cup\left\{\left\{x_{3}\right\}\right\}
\end{array}
$$

and for the second

$$
\begin{array}{r}
\left\{\left\{x_{1}, x_{3}\right\},\left\{x_{2}\right\}\right\}=\mathbb{D}_{1}^{p} \cup\left\{\left\{x_{1}, x_{3}\right\}\right\} \\
=\left\{\left\{x_{1}\right\}\right\} \cup\left\{\left\{x_{1}, x_{3}\right\}\right\}
\end{array}
$$

$$
\begin{aligned}
\left\{\left\{x_{2}, x_{3}\right\},\right. & \left.\left\{x_{1}\right\}\right\}=\mathbb{X}_{1}^{P} \cup\left\{\left\{x_{2}, x_{3}\right\}\right\} \\
& =\left\{\left\{x_{2}\right\}\right\} \cup\left\{\left\{x_{2}, x_{3}\right\}\right\}
\end{aligned}
$$

Here I. has two representations $\left\{\left\{x_{1}\right\}\right\}$ and $\left\{\left\{x_{2}\right\}\right\}$ this is accunted for by the combinotorral factor.

Firally for the last term

$$
\begin{aligned}
\left\{\left\{x_{1}, x_{2}, x_{3}\right\} \xi\right. & =X_{0}^{P} \cup\left\{\left\{x_{1}, x_{2}, x_{3}\right\} \xi\right. \\
& =\{\varnothing\} \cup\left\{x_{1}, x_{2}, x_{3}\right\} \xi
\end{aligned}
$$

Thus it has been demonstrated how

$$
\begin{aligned}
B_{3} & =\binom{2}{0} B_{2}+\binom{2}{1} B_{1}+\binom{2}{2} B_{0} \\
& =(1)(1)+(2)(1)+(1)(2) \\
& =5
\end{aligned}
$$

which is the same result obtained by a brute force calculation.

Definition: Inverse map and Equivalence class

Consider the map $f: X \rightarrow I$. The inverse map $f^{-1}$ defines a space of equivalence classes on $x$ where $x_{1}$ and $x_{2}$
are equivalent if

$$
f\left(x_{1}\right)=f\left(x_{2}\right)
$$

## Example

Consider differentiation on the set of quadratic polynomials with real coefficients withic is an onto mapping to the set of linear polynomicks with real coefficients. The inverse of the derivative is the indefinite integral or antiderivative
$\left(\frac{d}{d x}\right)^{-1}(a x+b)=\left\{\frac{1}{2} a x^{2}+b x+c: c \in \mathbb{R}\right\}$
It is seen that the antidervative of a linear polynamial is an equivalence class of quadratic functions which differ by a constant.

Note: Invertable function.
In the mathematics of real functions an invertable function must be one-to-one and onto In measure theory this is not the case. Inverse functions are defined as equivalence classes.

Definition: Inverse image
Let $f: \bar{x} \rightarrow \bar{I}$ be a map from the domain I to the range I. The inverse image of a subset of $I$

$$
A \subset I
$$

Is defined by

$$
f^{-1}(A)=\{x: x \in \bar{X}, f(x) \in A\}
$$

Since exvery subset of $I$ and $I$ are elements of the power sets $P_{I}$ and $P_{I}$ respectively the defintion implies that

$$
f^{-1}: P_{I} \rightarrow P_{I}
$$

Theorem : union and intersection

$$
\text { of } f^{-1}
$$

Let $f: X \rightarrow I$ be a map from domain $I$ to range $I$

$$
B=\left\{B_{\alpha}\right\}_{\alpha \in \Delta} C I
$$

be a collection of subsets of $I$, Then
a) $f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right)=\bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)$
b) $f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)$

Proof
To prove (a) it must be shown that

$$
f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

and

$$
f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

For first proof for some $x$ the defition of inverse image gives
$x \in f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \Rightarrow f(x) \in \bigcup_{\alpha \in A} B_{\alpha}$
From the definition of union for some $\alpha_{0}$

$$
f(x) \in B \alpha_{0}
$$

and again from the definition of inverse image

$$
x \in f^{-1}\left(B_{\alpha_{0}}\right)
$$

Thus

$$
x \in \bigcup_{\alpha \in A} f^{-1}\left(B_{0}\right)
$$

and

$$
f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

For the muerse relation for some $x$ the definition of union for some 20

$$
x \in \bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right) \Rightarrow x \in f^{-1}\left(B_{\alpha_{0}}\right)
$$

from the definition of inverse image

$$
f(x) \in B_{\alpha_{0}}
$$

and from the definition of union

$$
f(x) \in \bigcup_{\alpha \in A} B_{\alpha}
$$

and finally from the definition of inverse image

$$
x \in f^{-1}\left(\bigcup_{\alpha \in \Delta} B_{\alpha}\right)
$$

trues

$$
\bigcup_{\alpha \in A} f\left(B_{\alpha}\right) \subseteq f\left(\bigcup_{\alpha \in A} B_{\alpha}\right)
$$

and combing results gives

$$
f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right)=\bigcup_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

A similar proceedure can be used to prove

$$
f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

it must be shown that

$$
\begin{aligned}
& f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right) \\
& f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
\end{aligned}
$$

For the first
$x \in f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \Rightarrow f(x) \in \bigcap_{\alpha \in A} B_{\alpha}$ from the definition of intersection for every a

$$
f(x) \in B_{\alpha} \Rightarrow x \in f\left(B_{\alpha}\right)
$$

and

$$
x \in \bigcap_{\alpha \in A} f\left(B_{a}\right)
$$

thus

$$
f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

and for second relation

$$
\begin{aligned}
& x \in \cap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)=x \in f^{-1}\left(B_{\alpha}\right) \\
& \Rightarrow f(x) \in B_{\alpha} \Rightarrow f(x) \in \bigcup_{\alpha \in A} B_{\alpha} \\
& \Rightarrow x \in f^{-1}\left(\bigcup_{\alpha \in A} B_{\alpha}\right)
\end{aligned}
$$

$$
\Rightarrow f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

and the desired result is obtained.

$$
f^{-1}\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f^{-1}\left(B_{\alpha}\right)
$$

Theorem: union and intersection of $f$

Let $f: X \rightarrow$ I be a map from domain $I$ to range $I$

$$
B=\left\{B_{\alpha}\right\}_{\alpha \in \Delta} C I
$$

be a collection of subsets of $I$, Then
a) $f\left(\bigcup_{\alpha \in A} B_{\alpha}\right)=\bigcup_{\alpha \in A} f\left(B_{\alpha}\right)$
but only for a injective mapping (one-to-ohe) does
b) $f\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f\left(B_{\alpha}\right)$
while if the mapping is surjective equality does not hold.
c) $f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \neq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)$

## Proof

To prove (a) it must be shown that

$$
\begin{aligned}
& f\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcup_{\alpha \in A} f\left(B_{\alpha}\right) \\
& f\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
\end{aligned}
$$

For the first proof there evists $y \in I$

$$
y \in f\left(\bigcup_{\alpha \in A} B_{\alpha}\right)
$$

it follows from the definition of a set function there exists an $x$

$$
x \in \bigcup_{\alpha \in A} B_{\alpha}
$$

such that

$$
f(x)=y
$$

From the definition of union there is at least one $\alpha, \alpha_{0}$, such that

$$
x \in B_{\alpha_{0}}
$$

from the defintion of a set function it follows that

$$
y \in f\left(B_{\alpha_{0}}\right)
$$

and from the definition of union

$$
y \in \bigcup_{\alpha \in A} f\left(B_{\alpha_{0}}\right)
$$

Thus

$$
f\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
$$

For the second relation assume for some $y \in I$ that

$$
y \in \bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
$$

from the defintion of union it follows that there exists at least one $\alpha, \alpha_{0}$, such that

$$
y \in f\left(B_{\alpha_{0}}\right)
$$

and from the defintion of $a$ set function and the assumption

$$
x \in B_{\alpha_{0}}
$$

from the definition of union it follows that

$$
x \in \bigcup_{\alpha \in A} B_{\alpha}
$$

and from the defintion of a set function

$$
y \in f\left(\bigcup_{\alpha \in \Delta} B_{\alpha}\right)
$$

thus

$$
f\left(\bigcup_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
$$

and the firal result is obtained

$$
f\left(\bigcup_{\alpha \in A} B_{\alpha}\right)=\bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Next it will be shown that for an injective (one-to-one) mapping

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

To prove this it must be shown that

$$
\begin{aligned}
& f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right) \\
& f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \supseteq \underset{\alpha \in A}{\cap} f\left(B_{\alpha}\right)
\end{aligned}
$$

Recall trat for an injective (one-to-one) mapping, that $\forall x_{1}, x_{2} \in \bar{X} \quad f\left(x_{1}\right)=f\left(x_{2}\right) \Rightarrow x_{1}=x_{2}$

Now consider

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \subseteq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Now there exists a $y \in \bar{Y}$ such that

$$
y \in f\left(\bigcap_{\alpha \in A} B_{\alpha}\right)
$$

It follows that from the definition of a set function and the assustion that $f$ is mjective (one-to-one) that there exsits one $x$ such that

$$
y \in f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \Rightarrow x \in \bigcap_{\alpha \in A} B_{\alpha}
$$

from the definition of intersection it follows that

$$
x \in B_{\alpha} \quad \forall \alpha \in A
$$

From the definition of a set function

$$
y \in f\left(B_{\alpha}\right) \quad \forall \alpha \in \Delta
$$

and from the definition of intersection it follows that

$$
y \in \bigcup_{\alpha \in A} f\left(B_{\alpha}\right)
$$

and the desired result is
obtained

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \subset \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

next Consider

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

There exists a $y \in \bar{I}$ such that

$$
y \in \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

from the definition of intersection it follows the

$$
\forall \alpha \in A \quad y \in f\left(B_{\alpha}\right)
$$

From the definition of 8
set function and since $f$ is assumed to be injective (one-to-one) there is one $x \in \bar{X}$ such that

$$
x \in B_{\alpha} \quad \forall \alpha \in A
$$

where

$$
f(x)=y
$$

it follows that

$$
x \in \bigcap_{\alpha \in A} B_{\alpha}
$$

and from the definition of a set function

$$
y \in f\left(\bigcap_{\alpha \in A} B_{\alpha}\right)
$$

Thus

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \supseteq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Trus the desired result is obtained

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right)=\bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Next it will be shown that for a surjective map (onto) that

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \neq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Recall that a surjective (onto) mapping satisfies,
$\forall y \in I \quad \exists x \in \mathbb{X}$ such that $y=f(x)$

In words this is saying for every II in I the exists at least one $x \in X$ such that $y=f(x)$. Since $t$ is possible trat multiple elements of I can map to the same element in I it follows that $\forall a, b \in \bar{S} f(a)=f(b) \nRightarrow a=b$ thus $a$ surjection cannot be an injection unless every element of $I$ is mapped to by a single element of $\bar{x}$.

To prove the desired result it is assumed that multiple values of $x$ map to the same y using this assumpton an example an be constructer trat shows that

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \neq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

Let $\bar{X}=\{1,2\}$ and

$$
f(1)=f(2)=1
$$

thus $I=\{1\}$. Let $B_{1}=\{1\}$ and $B_{2}=\{2\}$. Then

$$
\begin{aligned}
& f\left(B_{1} \cap B_{2}\right)=f(\{1\} \cap\{2\}) \\
& =f(\phi)=\varnothing
\end{aligned}
$$

and

$$
\begin{aligned}
& f(\{1\}) \cap f(\{2\}) \\
= & \{1\} \cap\{1\}=\{1\}
\end{aligned}
$$

Thus the distred result is obtained

$$
f\left(\bigcap_{\alpha \in A} B_{\alpha}\right) \neq \bigcap_{\alpha \in A} f\left(B_{\alpha}\right)
$$

## Cardinality

Cardinalily of a set was previously described there move details will be discussed.

Two sets I and I are equivalent or have the same cardinality ( if there is a bijection cone-to-ore and onto), $f$,

$$
f: \bar{x} \rightarrow \bar{I}
$$

This relation is dended by

$$
\bar{X} \sim I
$$

If $\bar{x}=\emptyset$ or $\bar{x} \sim\{1,2,3, \ldots, n\}$ for some $n \in N$ is finite

If $\bar{X}$ is finite or $\bar{X} \sim N, \bar{X}$ is countable
If $I$ is not empty, finite or countable it is uncountable.

Example: Cardinality of integers, $z$ The integers, 2 have the following mapping onto $N$

$$
\begin{array}{ll}
0 \leftrightarrow 0, & 1 \leftrightarrow 1,-1 \leftrightarrow 2,2 \leftrightarrow 3, \\
-2 \leftrightarrow 4, & 3
\end{array}
$$

an expression for this mapping with, $z \in z$ and $n \in N$

$$
n=\left\{\begin{array}{cc}
0 & z=0 \\
2 z-1 & z>0 \\
-2 z & z<0
\end{array}\right.
$$

Example $e^{2}$ is countable
$\mathbb{Z}^{2}$ is the cartesion product space

$$
\mathbb{Z}^{2}=\{(x, y), x \in R, y \in R\}
$$

The product space can be represented by the infinite matrix
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-148.jpg?height=664&width=1281&top_left_y=52&top_left_x=128)

The numbers can be indexed in the manner indicated in the dragram.
Let the pair ( $i, j$ ) indicate the row and collumn of the cartesion product pair. Let $n \in \mathbb{N}$ be a natural number, $n=(1,2,3,4, \ldots) . \Delta$ mapping of the form

$$
f(c, j)=n
$$

can be derived in the following manner. consider
the triangular numbers which are defined by

$$
1,3,6,10,15,21,
$$

Note that the values of $n$ for $i=1$ and $j>1$ are the triaguar numbers.

The triangular numbers are defined by the number of matrix elements in a right triagle with hergt, $i$. For example the first 4 triangular number are given by
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-149.jpg?height=235&width=882&top_left_y=1422&top_left_x=324)

An expression for the number points can be obtained by constructing the following rectangles.

$$
\begin{array}{cccc}
1 & 3 & 6 & 10 \\
\because & \therefore \because & \therefore \because & \because \cdots \\
& & \because \ddots & \therefore
\end{array}
$$

It is seen that

$$
n=j \frac{(j+1)}{2}
$$

thus

$$
f(1, j)=\frac{j(j+1)}{2}
$$

Note that

$$
\binom{j+1}{2}=\frac{(j+1)!}{2!(j-2)!}=\frac{j(j+1)}{2}
$$

Thus the triangular numbers are the total number of ways two objects can be selected from $n+1$ It follows that the product
space matrix can be modted as an infinite triangular matrix.

To determine an expression for the other terms more information is needed.

Recall Pascal's triangle where the value of the n'throw and K'th column is given by

$$
\binom{n}{k}
$$

Pascal's triangle for $n=7$ is shown below
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-151.jpg?height=555&width=880&top_left_y=1382&top_left_x=453)

In terms of binomial coefficients Pascals triangle becomes
(8)
(1) (1)
(る) $\binom{2}{1}\binom{2}{2}$
$\binom{3}{0} \quad\binom{3}{1} \quad\binom{3}{2} \quad\binom{3}{3}$
(4) $\binom{4}{1} \quad\binom{4}{2} \quad\binom{4}{3}\binom{4}{4}$
$(5)\binom{5}{1}\binom{5}{2}\binom{5}{3}\binom{5}{4}\binom{5}{5}$
$\binom{6}{0}\binom{6}{1}\binom{6}{2}\binom{6}{3}\binom{6}{4}\binom{6}{5}\binom{6}{6}$
The second column is
highligted in yellow and is seen to be the triangular numbers which are given by ( $\begin{aligned} & n \\ & 2\end{aligned}$ )

To tie this in with the product matrix the matrix of cantor paring numbers is given by

$$
\begin{array}{llllllll}
J_{i} & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
0 & 0 & 1 & 3 & 6 & 10 & 15 & \\
1 & 2 & 4 & 7 & 11 & 16 & & \\
2 & 5 & 8 & 12 & 17 & & & \\
3 & 9 & 13 & 18 & & & & \\
4 & 14 & 19 & & & & & \\
6 & 20 & & & & & & \\
& & & & 1 & & & \\
& & & 1 & 2 & 1 & & \\
& & 1 & 3 & 3 & 1 & & \\
& & 1 & 4 & 6 & 4 & 1 & \\
& 1 & & 5 & 10 & 10 & 5 & 1
\end{array}
$$

To take into account the leading 0 in the product matrix the binomial coefficient must be offset by one

$$
\begin{aligned}
\binom{j+1}{2} & =\frac{(j+1)!}{2!(j+1-2)!}=\frac{(j+1)!}{2(j-1)!} \\
& =\frac{1}{2} j(j+1)
\end{aligned}
$$

which is the expression obtained using triangular numbers.
Now column 1 of Passals triangle is the loatual number $\mathbb{N}$. It $J_{\text {is }}$ indicated $b$, the blue nighlight

Now consider the points $(1,0)$ and ( 1,1 )
![](https://cdn.mathpix.com/cropped/2025_11_16_eda3966748165449413dg-154.jpg?height=656&width=1408&top_left_y=1324&top_left_x=118)

If the first fow elements of row $i=1$ are examined it is seen that for $j=0$ the calue of the cantor paring function is given be the sum of the value at $(0,0)$ and the value of of the first column on the next row which is 2 . The remaing columns follow the same pattern

$$
\begin{array}{ll}
j=1 & 1+3=4 \\
j=2 & 3+4=7 \\
j=3 & 6+5=11
\end{array}
$$

Consider the first few colums of the next row, which is shown below. The pattern is similar to the $\tau=1$ case but the offset into column I is 2 instead of 1.

| $j_{i}$ | 0 | 1 | 2 | 3 | 4 |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0 | 0 | 1 | 3 | 6 | 10 | 0 |  |  |
| 1 | 2 | 4 | 7 | 11 |  | $1^{\circ}$ |  |  |
| 2 | 5 | 8 | 12 |  | $1^{\prime}$ | $1^{\prime}$ |  |  |
| 3 | 9 | 13 |  | $1^{\prime}$ | 3 | $3^{\prime}$ | $1^{3}$ |  |
|  |  |  |  | $1^{\prime}$ | $4^{3}$ | 6 | $1^{4}$ | $1^{4}$ |
|  |  |  |  | $1^{5}$ | 10 | $10^{5}$ | $5^{\prime 5}$ |  |

As a possible pairing function consider adding the row offset to the epression obtained for row $i=0$.

$$
\begin{aligned}
f(i, j)=\binom{i+j+1}{2} & =\frac{(i+j+1)!}{2!(i+j+1-2)!} \\
=\frac{(i+j+1)!}{2(i+j-1)!} & =\frac{1}{2}(i+j)(i+j+1)
\end{aligned}
$$

This expression gives

| $(i, j)$ |  | $f(i, j)$ |  |
| :--- | :--- | :--- | :--- |
| $(1,0)$ | 1 |  | difference |
| $(1,1)$ | 3 | 1 | 1 |
| $(1,2)$ | 6 | 1 |  |
| $(1,3)$ | 10 | 1 |  |
| $(2,0)$ | 3 | 2 |  |
| $(2,1)$ | 6 | 2 |  |
| $(2,2)$ | 10 | 2 |  |

It is seen that adding $i$ to the proposed pairing function gives the desired result. Thus the cantor pairing function trat does the mapping,

$$
\begin{aligned}
f: \mathbb{Z}^{2} \rightarrow \mathbb{N} \\
\text { is given } b y \\
f(i, j)=\binom{i+j+1}{2}+i \\
=\frac{(i+j+1)!}{2!(i+j+1-2)!}+i
\end{aligned}
$$

$$
\begin{aligned}
& =\frac{(i+j+1)!}{2(i+j-1)!}+i \\
& =\frac{1}{2}(i+j)(i+j+1)+i
\end{aligned}
$$

Thus the product space $R^{2}$ is countable since a mapping to the natural numbers $\mathbb{N}$ exists

Theorem : Enumeration of Countable
A countable set X can be written as $\left\{x_{1}, x_{2}, x_{3}, x_{4}, \ldots\right\}$ where $x_{1}, x_{2}, x_{3}, \ldots$ enumerate the points in $\bar{X}$

$$
\begin{aligned}
& \text { Theorem : A Countable Which of } \\
& \text { Countable sels is } \\
& \text { Countable }
\end{aligned}
$$

Proof
Let $\bar{X}=\left\{X_{1}, X_{2}, \bar{X}_{3}, \ldots\right\}$ where each $\underline{X}_{i}$ is countable. Since
the $X_{i}$ are countable it follows that

$$
x_{i}=\left\{x_{i, 1}, x_{i, 2}, x_{i, 3}, \ldots\right\}
$$

then

$$
\begin{aligned}
\bigcup_{i=1}^{\infty} \bar{X}_{i} & =\left\{X_{i j}, i \in N, j=N\right\} \\
& =\left\{X_{i j},\left(i_{i j}\right) \in N^{2}\right\}
\end{aligned}
$$

Previously it was shown that $\mathbb{Z}^{2}$ is countable it follows that

$$
\bigcup_{i=1}^{\infty} Z_{i}
$$

is countable.
Definition: Axom of Choice
The Axiom of Choice can be stated in several equivalent ways. The first is,

1. The Cartesian product of a collection of non-empty
sets is not empty
2. This statement is equivalent to the statement, Given any collection collection of bins, each containing at least one object, it is possible to make a selection of one object from each bin, even if the collection is infinite
3. The most formal statement is that for every indexed family of non-empty sets

$$
\left\{S_{i}\right\} \quad i \in \mathbb{N}
$$

there exists an indexed set of elements

$$
\left\{x_{i}\right\} \quad i \in \mathbb{N}
$$

such that

$$
x_{i} \in S_{i} \forall i \in \mathbb{N}
$$

The axim of choice is not
needed if a choice function is well defined. A choice function can be defined if a distinguishing property holds for one elelement in each set allowing it to be chosen. As an example consider the set of Natural numbers

$$
\{\{1,4,7\},\{2,8,100\},\{200,300,10\}\}
$$

If the choce function is the smallest number this leads to the set

$$
\{1,2,10\}
$$

Even if this set is constucted from all Notural numbers and infinite the choice function is well defined. In general for all collections of sets this is not possible, so, the axim of choice must be invoked.
other variants are

* Given any set $X$ of pairwise disjont non-empty sets (i.e. a partition) there exists at least one set $C$ that contains exactly one element from each of the sets of $\bar{X}$.
* For any set A the powers set, $P_{A}$, (with the empty set removed, has a choice function.
* For any set A there is a function $f$ such that for cony non-empty subset $B \subseteq A f(B) \subseteq B$

Theorem: The set of real numbers $(0,1]$ is uncountable
Proof
Proof by contradiction is used. It is cossumed that the set is countable and the cantor

Diagonal argument is used to construct an element not in the set.
Previously it was shown that the rational numbers $Q$ are countable. It will be shown that for the rational numbers on the interval $(0,1]$
that a bijective mapping to $\mathbb{R}$ does not exist and the $\mathbb{R}$ has more elements than $Q$.

The positive rational numbers are the ordered pairs

$$
(i, j), i \in \mathbb{N}, j \in \mathbb{N}
$$

and can be enwernerated by the infinite matrix shown below. The elements that are elements of $(0,1]$ are highligted in yellow. A traversal of the rational
numbers is indicated by the red arrows

| $(1,1)$ | $(1,2)$ | $(1,3)$ | $(1,4)$ | $(1,5)$ | $(1,6)$ | $\ldots$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $(2,1)$ | $(2,2)$ | $(2,3)$ | $(2,4)$ | $(2,5)$ | $(2,6)$ | $\ldots$ |
| $(3,1)$ | $(3,2)$ | $(3,3)$ | $(3,4)$ | $(3,5)$ | $(3,6)$ | $\ldots$ |
| $(4,1)$ | $(4,2)$ | $(4,3)$ | $(4,4)$ | $(4,5)$ | $(4,6)$ | $\ldots$ |

$(5,1)(5,2)(5,3)(5,4)(5,5)(5,69) \ldots \begin{array}{cccccc}(6,1) & (6,2) & (6,3) & (6,4) & (6,5) & (6,6) \\ \vdots & \vdots & \vdots & \vdots & \vdots & \ddots\end{array}$

In the mapping to $(0,1] \subset \mathbb{R}$ the decimal expansion of the rational number is used. For example

$$
\begin{aligned}
& (1,2)=\frac{1}{2}=0.5000 \ldots \\
& (1,3)=\frac{1}{3}=0.3333 \ldots
\end{aligned}
$$

Some rational numbers have multiple decimal expansions. These numbers end in
an infinte sequence of $O$ 's or I's. For example
$(1,1)=\frac{1}{1}=1.000 \ldots=0.9999 \ldots$
$(1,2)=\frac{1}{2}=0.5000 \ldots=0.49999 \ldots$
This relation is an equivalence class. The o's terminating representative of the equivalence class will be chosen as representative of the class. Another equivalence class is given by

$$
\begin{aligned}
& (1,2)=\frac{1}{2}=\frac{3}{4}=\frac{3}{6}=\frac{n}{2 n} \\
& (1,3)=\frac{1}{3}=\frac{n}{3 n} \\
& (2,3)=\frac{2}{3}=\frac{2 n}{3 n}
\end{aligned}
$$

where $n=1,2,3, \ldots$

For this class the representative has $n$ canceled, thus

$$
(1,3)=\frac{1}{3} \quad(1,2)=\frac{1}{2}
$$

Applying these relations and the traversal indicated in the matrix representation gives a list of all rational numbers which are elements of $(0,1]$
$1.000000000000 \cdots$
$0.500000000000 \cdots$
$0.333333333333 \ldots$
0.666666666666
0.250000000000
$0.750000000000 \cdots$
$0.200000000000 \ldots$
$0.400000000000 \cdots$
$0.600000000000 \ldots$
0.800000000000
0. $166066666666 \ldots$.
0.833333333333 .

The cantor diagonal argument will now be applied to construct a real number that is not rational. Consider the diagonal disits of the number list which are high lighted in yellow. A decimal representation of a number is constructed using the following proceedure. If the nighligted digit is 3 the digit at the same position in the constructed number is 7. If the digit is not 3 a 3 is placed at the same position in the constructed number. This proceedure leads to the real number

$$
0.337333333337
$$

This number will be different from each number in the list since each differs from the constructed number by at least the digit on the
diagonal. Since the list contains all rational numbers that are elements of the interval $(0,1]$ it follows that the constructed real number is not rational and that there are more real numbers tran rational numbers. Thus the constructed mapping of the rational numbers onto the real numbers is not brective. Thus the desired result follows the real numbers on the interval $(0,1]$ is uncountable.

Theorem: Cardinality of Product
Set.
If $\bar{X}$ and $I$ are finite then

$$
|\bar{X} \times I|=|\bar{X}||I|
$$

If either $\bar{X}$ or $\bar{I}$ or both are countable then $\underline{X} \times \underline{I}$
is cocontable. If either I or II or both are uncountable then $I \times I$ are wrowntable.

## Sequences of sets

Measure theory makes use of countable collections of sets.
Let $\left\{A_{i}\right\}_{i=1}^{\infty}$ be an infinite countable collection of subsets of a set $I$. If

$$
A_{1} \subset A_{2} \subset A_{3} \cdots
$$

and

$$
\bigcup_{i=1}^{\infty} A_{i}=A
$$

It is said that $\left\{A_{i}\right\}_{i=1}^{\infty}$ is a monotone moreasing sequence of sets and that $A_{i}$ converges to $A$. This is denoted by

$$
A_{i} \uparrow A \quad A_{i} \uparrow A
$$

If

$$
A_{1} \supset A_{2} \supset A_{3} \supset \cdots
$$

and

$$
\bigcap_{i=1}^{\infty} A_{i}=A
$$

It is said that $\left\{A_{i}\right\}_{i=1}^{D}$ is a monotone decreasing seguence of sets and $A_{i}$ converges to $A$. This is denoted by

$$
A_{i} \downarrow A \quad A_{i} \downarrow A
$$

In either case the sequence is called monotone.

## Open and Closed Intervals

An interval $a<x<b$ denoted by $(a, b)$ is open if

$$
\forall x \in(a, b)
$$

there exists an $\varepsilon>0$ such that

$$
x \pm \varepsilon \in(a, b)
$$

An open interval does not contain its end points.
An intoroal is cosed if it contains its end points,

$$
a \leqslant x \leqslant b
$$

It is denoted by $[a, b]$.
The interval is not open since if $x=a, a-\varepsilon$ is not contained in the interval

$$
x-\varepsilon \otimes[a, b]
$$

A more formal definition is that a closed interval is the compliment of an open interval. Consider the intervat

$$
x \in(-\infty, a) \text { or } x \in(b, \infty)
$$

The compliment of the interoal
is $[a, b]$. Note that the unbounded interval is denoted by

$$
x \in \mathbb{R} \Rightarrow x \in(-\infty, \infty)
$$

Interoals can be half open,

$$
[a, b) \text { or }(a, b]
$$

## Example

Define the open intorval

$$
A_{i}=(0,1-1 / i) \quad i \geqslant 2
$$

Then

$$
\begin{aligned}
A_{2}=(0,1 / 2) \subset A_{3} & =(0,2 / 3) \\
& \left(A_{4}=(0,3 / 4) \cdots\right.
\end{aligned}
$$

and

$$
\bigcup_{i=2}^{\infty}(0,1-1 / i)=(0,1)
$$

## Example

Define the open interval

$$
(0,1+1 / i) \quad i=2,3,4,
$$

It follows that

$$
\begin{aligned}
& A_{2}=(0,3 / 2) \supset A_{3}=(0,4 / 3) \\
& \supset A_{4}=(0,5 / 4) \cdots
\end{aligned}
$$

so

$$
(0,1]=\bigcap_{i=2}^{\infty}(0,1+1 / i)
$$

## Theorem

Let $\left\{A_{i}\right\}_{i=1}^{\infty}$ where $A_{i} \subseteq \bar{X}$. Then

1. If $A_{i} / A$ then $A_{i}=\bigcup_{j=1}^{i} A_{j}$
2. If $A_{i}>A$ then $A_{i}=\lambda_{i}^{r} A_{j}$
3. If $A_{i}>A$ then $A_{i}^{c} \searrow A^{j} C^{i}$
4. If $A_{i}$ y $A$ then $A^{c}$, $A^{c}$

For the first theorem since $A_{i} \rightarrow A$ it follows that

$$
A_{1} \subset A_{2} \subset A_{3} \subset \cdots \subset A_{i}
$$

so
$\bigcup_{j=1}^{i} A_{i}=A_{1} \cup A_{2} \cup A_{3} \cup \cdots \cup A_{i}=A_{i}$
since if $x \in A_{i} \Rightarrow x \in \bigcup_{j=1}^{i} A_{j}$ and if $x \in \bigcup_{j=1}^{i} A_{j}$ then $x \in A_{i}$ since $A_{i} \uparrow A$

Smilarly if $A_{i} \searrow A$

$$
A_{1} \supset A_{2} \supset A_{3} \supset \cdots \supset A_{i}
$$

then

$$
\begin{aligned}
\bigcap_{j=1}^{i} A_{j} & =A_{1} \cap A_{2} \cap A_{3} \cap \cdots \cap A_{i} \\
& =A_{i}
\end{aligned}
$$

since if $x \in A_{i} \Rightarrow x \in \bigcap_{j=1}^{i} A_{j}$ and if $x \in \bigcap_{j=1}^{i} A_{j}$ the $x \in A_{j} \quad \forall_{j}$ thus $x \in A_{i}$

50

$$
\bigcap_{j=1}^{i} A_{j}=A_{j}
$$

To prove the third theorem recall DeMorgan's Law

$$
\left(\bigcup_{i=1}^{\infty}, A_{i}\right)^{c}=\bigcap_{i=1}^{\infty} A_{i}^{c}=A^{c}
$$

Since $A_{i}>A$

$$
A_{1} \subset A_{2} \subset A_{3} \subset \cdots
$$

In the forst theorem it was shown that for a
finite number of increasing sets that

$$
\begin{aligned}
& \bigcup_{i=1}^{n} A_{i}=A_{n} \\
\Rightarrow & \left(\bigcup_{i=1}^{n} A_{i}\right)^{C}=A_{n}^{c}
\end{aligned}
$$

applying De Morgan's Law

$$
\left(\bigcup_{i=1}^{n} A_{i}\right)^{c}=\bigcap_{i=1}^{n} A_{i}^{c}=A_{n}^{c}
$$

From the second theorem it follows that

$$
A_{1}^{c} \supset A_{2}^{c} \supset A_{3}^{c} \supset \cdots \supset A_{i}^{c}
$$

thus if $A_{i}>A$ then $A_{i}^{c}$ y $A^{c}$.
To prove the final theorem recall the other version of De Morgan's law

$$
\left(\hat{\mathrm{N}}_{i=1}^{\infty} A_{i}\right)^{c}=\bigcup_{i=1}^{\infty} A_{i}^{c}=A^{c}
$$

since $A_{i} \searrow A$,

$$
A_{1} \supset A_{2}>A_{3}>\cdots
$$

was shown that for a fanite sequence of decreasing sits that

$$
\bigcap_{j=1}^{i} A_{j}=A_{i}
$$

$$
\Rightarrow\left(\bigcap_{j=1}^{i} A_{j}\right)^{C}=A_{i}^{C}
$$

applying De Morgan's Law gives

$$
\left(\bigcap_{j=1}^{i} A_{j}\right)^{C}=\bigcup_{j=1}^{i} A_{j}^{c}=A_{i}^{c}
$$

From the first theorem it follows that

$$
A_{1}^{c} \subset A_{2}^{c} \subset A_{3}^{c} c \cdots c A_{1}^{c}
$$

thus if $A_{i}>A$ then $A_{i}^{c}>A^{c}$
useful set Relations
In the previous section use was made of De Morgan's laws in the proof of theoroms, namely

$$
\begin{aligned}
& \left(\bigcup_{\alpha \in B} A_{\alpha}\right)^{c}=\bigcup_{\alpha \in B} A_{\alpha}^{c} \\
& \left(\bigcap_{\alpha \in B} A_{\alpha}\right)^{c}=\bigcup_{\alpha \in B} A_{\alpha}^{c}
\end{aligned}
$$

I proved these relations in "Problem and Solutions in Finance volume I"

Another relation if for any $B \in B$

$$
\bigcap_{\alpha \in B} A_{\alpha} \subset A_{\beta} \subset \bigcup_{\alpha \in B} A_{\alpha}
$$

This relation is apparent from the definition of intersection and union. The intersection of two sets is defined by, $\forall a \in A_{\alpha}$ and $a \in A_{\beta}$ then

$$
a \in A_{\alpha} \cap A_{\beta} \subset A_{\beta}
$$

and simitarly from the defintion of union $\forall a \in A_{B}$

$$
a \in A_{\alpha} \cup A_{\beta}
$$

thles

$$
A_{\beta} \subset A_{\alpha} \cup A_{B}
$$

The next relations are analogis to the distributive
laws
$A \cup\left(\bigcap_{\alpha \in B} A_{\alpha}\right)=\bigcap_{\alpha \in B}\left(A \cup A_{\alpha}\right)$
$A \cap\left(\cup_{\alpha \in B} A_{\alpha}\right)=\cup_{\alpha \in B}\left(A \cap A_{\alpha}\right)$
For the first relation let

$$
a \in A \cup\left(\cap_{\alpha \in B} A_{\alpha}\right)
$$

then $a \in A$ or $a \in \bigcap_{\alpha \in B} A_{\alpha}$
or $a$ is in both using the definition of intersection. If $a \in A$ then $a \in A \cup A \alpha \quad \forall \alpha \in A$ thus $a \in \bigcap_{d \in B}\left(A \cup A_{2}\right)$. So

$$
A \cup\left(\cup_{\alpha \in B} A_{\alpha}\right) \subset \cap_{\alpha \in B}\left(A \cup A_{\alpha}\right)
$$

Now smilarly if $a \in \bigcap_{\alpha \in B} A_{\alpha}$ then $a \in A_{\alpha} \forall \alpha \in B$ and $a \in A \cup A_{\alpha} \forall \alpha \in B$ then $a \in \bigcap_{\alpha \in B}\left(A \cup A_{\alpha}\right)$ and

$$
A \cup\left(\cup_{\alpha \in B} A_{\alpha}\right) \subset \cap_{\alpha \in B}\left(A \cup A_{\alpha}\right)
$$

To prove equality let $a \in \bigcap_{\alpha \in B}\left(A \cup A_{\alpha}\right)$ then $a \in A \cup A_{\alpha} \forall \alpha \in B$ and $a \in A$ or $a \in A_{\alpha}$ or both. If $a \in A$ then $a \in A \cup\left(U_{E B} A_{A}\right)$ and if $a \in A_{2}$ the relatin. holds and the final result is obtained

$$
A \cup\left(\bigcap_{\alpha \in B} A_{\alpha}\right)=\bigcap_{\alpha \in B}\left(A \cup A_{\alpha}\right)
$$

A similar argument is used to show the second relation

$$
A \cap\left(\cup_{\alpha \in B} A_{\alpha}\right)=\cup_{\alpha \in B}\left(A \cap A_{\alpha}\right)
$$

Finally

$$
A C B \Rightarrow B^{C} C A^{C}
$$

This is easily demonstrated using the definition of intersection. If $A C B$ then

$$
\begin{aligned}
A \cap B & =A \\
\Rightarrow \quad(A \cap B)^{C} & =A^{C}
\end{aligned}
$$

From De Morgans laws

$$
(A \cap B)^{C}=A^{C} \cup B^{C}
$$

trus

$$
A^{C} \cup B^{C}=A^{C}
$$

This relation implies that

$$
B^{c} \subset A^{c}
$$

which is the desired result.

Disjont union
A collection of sets $\left\{\bar{X}_{i}\right\}_{i=1}^{\infty}$ of sets of $\forall \underline{X}_{c}, \underline{\Delta}_{i} \subset \underline{X}$ is pairwise disjoint if for $i \neq j$

$$
\bar{X}_{i} \cap \underline{X}_{j}=\varnothing
$$

If $\left\{\bar{X}_{i} \xi_{l=1}^{\infty}\right.$ is pairwise disjouint then

$$
\bigcup_{i=1}^{\infty} \Sigma_{i}
$$

is called a conion of disjont sets or a disjoint union.

## Example

$$
\begin{gathered}
(0,1]=(0,1 / 2] \cup\left(1 / 2, \frac{3}{4}\right] \cup\left(\frac{3}{4}, \frac{7}{8}\right] \\
\cup\left(\frac{7}{8}, \frac{15}{10}\right] .
\end{gathered}
$$

A disjont union of any two set $\bar{I}_{1}, \bar{I}_{2} \subset \bar{X}$ as

$$
\bar{X}_{1} \cup \bar{X}_{2}=\bar{X}_{1} \cup\left(\bar{X}_{2} \cap \bar{X}_{1}^{c}\right)
$$

The proof of this relation is striagt forward. If $x \in I$, and $x \notin \bar{X}_{2}$ then equality dearly holds. If $x \in I_{2}$ and $x \in I_{1}$ then $x \in \underline{X}_{2} \cap \underline{X}_{1}^{c}$ and $x \in \underline{X}_{1} \cup\left(\underline{X}_{2} \cap \underline{X}_{1}^{c}\right)$. similarly if $x \in E_{1} \cup\left(E_{2} \cap E_{1}^{c}\right)$ The case $x \in I$, has been covered.
If $x \in Z_{1}$ and $x \in Z_{2}$ then $x \in X_{2} \cap Z_{1}^{c}$ and $x \in I_{1} \cup\left(X_{2} \cap X_{1}^{c}\right)$ and $x \in X_{1} \cup X_{2}$ so

$$
\bar{X}_{1} \cup \bar{X}_{2}=\bar{X}_{1} \cup\left(\bar{X}_{2} \cap \bar{X}_{1}^{c}\right)
$$

Let $\left\{A_{i}\right\}_{i=1}^{\infty}$ be a collection of subsets of $X$ and

$$
A=\bigcup_{i=1}^{\infty} A_{i}
$$

In the following a proceedure for constutting an increasing sequence of sets from an orbitrary collection of sets which may not be increasing is disclesed.

Define the sequence of sets $\left\{B_{i}\right\}_{i=1}^{\infty}$ by

$$
B_{1}=A_{1} \quad B_{j}=\bigcup_{i=1}^{j} A_{i} \text { for } j>1
$$

Show that $B_{j} / A$. First It must be stown that

$$
\bigcup_{j=1}^{\infty} B_{j}=A
$$

so

$$
\begin{aligned}
\bigcup_{j=1}^{\infty} B_{j}= & B_{1} \cup B_{2} \cup B_{3} \cdots \\
= & \left(A_{1} \cup\left(A_{1} \cup A_{2}\right) \cup\left(A_{1} \cup A_{2} \cup A_{3}\right) \cdots\right. \\
= & \left(A_{1} \cup\left(A_{3} \cup A_{3} \cup \cdots\right) \cdots\left(A_{2} \cup A_{2} \cdots\right)\right. \\
= & A_{1} \cup A_{2} \cup A_{3} \cdots \\
= & \bigcup_{i=1}^{\infty} A_{i} \\
= & A
\end{aligned}
$$

Next it must be shown that

$$
B_{1} \subset B_{2} \subset B_{3} \subset \cdots
$$

This follows easily from the definition of $B$

$$
\begin{aligned}
& B_{1}=A_{1} \\
& B_{2}=A_{1} \cup A_{2} \\
& B_{3}=A_{1} \cup A_{2} \cup A_{3}
\end{aligned}
$$

Thus

$$
B_{1} \subset B_{2} \subset B_{3} \subset \cdots
$$

So

## $B_{j}>A$

Next a proceclure for constructing a union of disjoint sets from an arbitrary collection of sets is discussed

Consider the collection of subsets of $I,\left\{A_{i}\right\}_{i=1}^{\infty}$. Let

$$
B_{1}=A_{1} \quad B_{j}=A_{j} \backslash\left(\bigcup_{i=1}^{j-1} A_{i}\right)
$$

where the set difference is given by,

$$
A \backslash B=\{x \in A, x \in B\}
$$

First consider

$$
\begin{aligned}
\bigcup_{j=1}^{\infty} B_{j}= & B_{1} \cup B_{2} \cup B_{3} \cdots \\
= & A_{1} \cup\left(A_{2} \backslash A_{1}\right) \cup\left(A_{3} \backslash A_{1} \cup A_{2}\right) \\
& \cup\left(A_{4} \backslash A_{1} \cup A_{2} \cup A_{2}\right)
\end{aligned}
$$

For the first two terms where it will be shown that

$$
A_{1} \cup\left(A_{2} \backslash A_{1}\right)=A_{1} \cup A_{2}
$$

if $x \in A_{1}$ then $x \in A_{2} \backslash A_{1}$ and equality clearly holds. If $x \in A_{2} \backslash A_{1}$ then $x \in A_{1}$ so $x \in A_{2}$ then $x \in A_{1} \cup A_{2}$ and if $x \in A_{1} \cup A_{2}$ and $x \in A_{2}, x \in A_{1}$ then $x \in A_{1} \cup\left(A_{2} \mid A_{1}\right)$ so

$$
A_{1} \cup\left(A_{2} \backslash A_{1}\right)=A_{1} \cup A_{2}
$$

Intuititiely $B_{j}$ consists of the elements in $A_{j}$ but not in $\bigcup_{i=1} A_{i}$ from this observation $i=1$ it follows that

$$
\bigcup_{j=1}^{\infty} B_{j}=\bigcup_{i=1}^{\infty} A_{i}
$$

Next it must be shown that

$$
B_{i} \cap B_{j}=\varnothing \quad \text { if } i \neq j
$$

without loss of generality
assume that $m>j$ then
$B_{m} \cap B_{j}=\left(A_{m} \backslash \bigcup_{i=1}^{m-1} A_{i}\right) \cap\left(A_{j} \backslash \bigcup_{i=1}^{j-1} A_{i}\right)$
if $x \in B_{m}$ then $x \in A_{m}$ and $x \notin \cup \bigcup_{i=1}^{m-1} A_{i}$ since $m>j$ it follows that $x \notin A_{j} \backslash \cup_{i=1}^{j-1} A_{i}$ thus

$$
B_{n} \cap B_{j}=\varnothing \text { for } i \neq j
$$

it follows that for any colection of sets $\left\{A_{i}\right\}_{i=1}^{\infty}$ where AiCD trat

$$
B_{1}=A_{1} \quad B_{j}=A_{j} \backslash\left(\bigcup_{i=1}^{j-1} A_{i}\right)
$$

is a disjoint union with

$$
\bigcup_{j=1}^{\infty} B_{j}=\bigcup_{i=1}^{\infty} A_{i}
$$

## Extended Real Number System

The exterded real number system defines the aritmatic maxiputations for the $\infty$ symbol. Let $\mathbb{R}$ denote the extended real number system then

$$
\hat{\mathbb{R}}=\mathbb{R} \cup\{-\infty, \infty\}
$$

The following relations hold

$$
\begin{aligned}
& -\infty \leqslant x \leqslant \infty \Rightarrow x \in \hat{\mathbb{R}} \\
& -\infty<x<\infty \Rightarrow x \in \mathbb{R} \\
& x \pm \infty= \pm \infty \quad \forall x \in \mathbb{R} \\
& \infty+\infty=-\infty \\
& -\infty-\infty=-\infty \\
& x( \pm \infty)= \pm \infty \quad \forall x>0, x \in \mathbb{R} \\
& x(\mp \infty)= \pm \infty \quad \forall x<0, x \in R \\
& 0( \pm \infty)=0
\end{aligned}
$$

Definition

$$
\begin{aligned}
& \hat{\mathbb{R}}^{+}=[0, \infty]=\{x \in \mathbb{R}: 0 \leqslant x \leqslant \infty\} \\
& \hat{\mathbb{R}}^{n}=\left\{\left(x_{1}, x_{2} \cdots x_{n}\right): x_{i} \in \mathbb{R}, 1 \leqslant i \leqslant n\right\}
\end{aligned}
$$

For $\hat{\mathbb{R}}^{n} n>1$

$$
\begin{aligned}
\infty & =(\infty, \infty, \cdots, \infty) \\
-\infty & =(-\infty,-\infty, \ldots,-\infty)
\end{aligned}
$$

It should be noted the $\hat{R}$ is not a field. Recall that a field is a set where addition, subtraction, division and multiplication behave as defined on the real and rational numbers

## Definition

If $A C \hat{R}$ is nonempty and not bounded from below

$$
\inf A=-\infty
$$

If $A \subset \hat{R}$ is nonempty and not bounded from above

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

