# Larger than One Probabilities in Mathematical and Practical Finance 

Mark Burgin<br>Department of Mathematics, University of California, Los Angeles<br>405 Hilgard Ave., Los Angeles, CA 90095, USA<br>E-mail: mburgin@math.ucla.edu<br>Gunter Meissner<br>MFE Program, Shidler College of Business, University of Hawaii<br>2404 Maile Way, Honolulu, HI 96822, USA<br>E-mail: meissner@hawaii.edu


#### Abstract

Traditionally probability is considered as a function that takes values in the interval [0, 1]. However, researchers found that negative, as well as larger than 1 probabilities could be a useful tool in making financial modeling more exact and flexible. Here we show how larger than 1 probabilities could be handy for financial modeling. First, we define and mathematically rigorously derive the properties of larger than 1 probabilities based on their frequency interpretation. We call these probabilities inflated probabilities because conventional probabilities are never larger than 1 . It is transparently demonstrated that inflated probabilities emerge in various real life situations. We then explain how inflated probabilities can be applied to modeling financial options such as Caps and Floors. In trading practice, these options are typically valued in a Black-Scholes-Merton framework, which assumes a lognormal distribution for the price of underlying assets. Since negative values are not defined in the lognormal framework, negative interest rates cannot be modeled. However interest rates have been negative several times in financial practice in the past. We show that applying inflated probabilities to the Black-Scholes-Merton model implies negative interest rates. Hence with this extension, Caps and Floors with negative interest rate can be conveniently modeled closed form.


JEL Classifications: C10, G15, E22, E43, F34
Keywords: Interest rate; Caps; Floors; Negative interest rate; Inflated probabilities; Negative probabilities; Black-Scholes-Merton model

## 1. Introduction

Traditionally probability is considered as a function that takes values in the interval [ 0,1 ] (Kolmogorov, 1933/1950). However, researchers found that probabilities values of which did not belong to this interval could be useful in various situations. For instance, negative probabilities have been applied to a number of theoretical and practical problems. At first, negative probabilities appeared in physics, where they have become rather popular (see, for example, (Wigner 1932; Dirac, 1942; 1943; Bartlett, 1945; Feynman 1950; 1987; Mückenheim, 1986; Krennikov, 1992; 2009)). Then negative probabilities came to finance (Haug, 2004; Székely, 2005; Burgin and Meissner, 2011; 2012).

At the same time, larger than 1 probabilities, also called above unity probabilities or bigger than one probabilities, i.e., probabilities values of which can be larger than 1 , have received less attention. One of the few to address them was Nobel Prize laureate Paul Dirac who wrote (1943):
> "The various parts of the wave function which referred to the existence of positive and negative-energy photons in the old interpretation now refer to the emissions and absorptions of photons. The probabilities, equal to 2 and -2 , are not physically understandable, but one can use them mathematically in accordance with the rules for working with a Gibbs ensemble."

However, even before Dirac used and contemplated larger than 1 probabilities, they were intrinsically brought into play by other physicists. In his fundamental review on extended probabilities, Mückenheim (1986) explains how such probabilities emerge by extending the quantum theoretical description of radiation given by Weisskopf and Wigner (1930). They calculated the natural linewidth of radioactive decay of an excited atom in which the normalized decay probability density $\rho(E, t)$ can take on negative values, as well as values exceeding unity. As a result, the corresponding normalized probability, which is an observable quantity, may violate both the lower and the upper limit in Kolmogorov's axioms (Mückenheim, 1986). It is important that these results were verified by experiments, demonstrating that utilization of larger than 1 probabilities well reflected physical reality (Holland, et al, 1960; Lynch, et al, 1960; Wu, et al, 1960).

Another Nobel Prize laureate Richard Feynman (1987) also argued that larger than 1 probabilities could be useful for probability calculations in different problems of quantum physics.

Later larger than 1 probabilities have been considered in physics, biology and finance in the works of Mack (2002), Sjöstrand (2006), Kovner and Lublinsky (2007), Venter (2007), and Nyambuya (2011). Some of the researchers did not want to accept meaningfulness of larger than 1 probabilities and tried to eliminate them by some artificial transformations. For instance, Mack (2002) tries to get rid of larger than 1 probabilities by reducing the probability mass at zero. Other researchers recognized larger than 1 probabilities as an inherent property of the studied phenomena. For instance, Haug (2004) argued that negative, as well as larger than 1 probabilities could be a useful tool in enhancing financial modeling. Even more, Kronz (2009) explains necessity of greater than one probabilities demonstrating that one can account for constructive quantum interference, if probability values greater than one are allowed.

Gell-Mann and Hartle (2012) extended probability ensemble interpretation by including real numbers that may be negative or greater than 1 as the probability values and providing an unconventional interpretation of such probabilities. According to them, such extended probabilities obey the usual rules of probability theory except that they can be negative or greater than one for an alternative for which it cannot be determined whether it occurs or not (as on the alternative histories in the two-slit experiment).

We also argue that larger than 1 (inflated) probabilities have sensible meaning, demonstrating that they are well defined concepts in mathematics and useful in finance. For instance, we show that larger than 1 probabilities can be applied to solving problems in financial modeling.

Looking into the history of mathematics and physics, we see that the evolution of negative, as well as larger than 1 probabilities is similar to the development of many new concepts in mathematics, which were initially met with skepticism. For instance, when negative numbers were introduced, critics dismissed their sensibility. Some of the European mathematicians, such as d'Alembert or Frend, rejected the sensibility of negative numbers until the $18{ }^{\text {th }}$ century and referred to them as 'absurd' or 'meaningless' (Kline, 1980; Mattessich, 1998). Even in the $19{ }^{\text {th }}$ century, it was a common practice to ignore any negative results derived from equations, on the assumption that they were meaningless (Martinez, 2005). For instance, Lazare Carnot (1753-1823) affirmed that the idea of something being less than nothing is absurd (Mattessich, 1998). Such outstanding mathematicians as William Hamilton (1805-1865) and August De Morgan (1806-1871) had similar opinions. In the same way, irrational numbers and later imaginary numbers were firstly rejected. Today these concepts are accepted and applied in numerous scientific and practical fields, such as physics, chemistry, biology and finance. This situation shows that negative, as well as larger than 1 probabilities are finding more and more practical applications. Here we consider their application to financial modeling, in particular, to option pricing.

The remaining paper is organized as follows. In section 2, we resolve the mathematical issue of inflated (larger than 1) probabilities, demonstrating experimental situations when inflated probabilities emerge and building mathematically grounded interpretations for inflated probabilities.

In section 3, we give examples of negative nominal interest rates in financial practice and explain problems of current financial modeling of negative interest rates. In Section 4, we build a mathematical model for Caps and Floors integrating inflated probabilities into the pricing model to allow for negative interest rates. In Section 5, we explain how inflated probabilities emerge in Duffie-Singleton model (Duffie and Singleton, 1999). Conclusions are given in Section 6.

## 2. Mathematical Foundations for Inflated Probability

In contrast to the wide-spread opinion, inflated, or larger than 1, probability has a natural interpretation. To show this, let us consider the following situations.

Example 1. In an experiment, three coins are tossed. The conventional question is: What is the probability of getting, at least, one head in one toss? To calculate this probability, we assume that all coins are without defects and all tosses are fair and independent. Thus, the probability of having heads $(h)$ for one toss of one coin is $p_{1}(h)=0.5$. The same is true for tails $(t)$. Thus, the probability of having no heads or what is the same, of having three tails, in this experiment is $p(0 h)=p(3 t)= 0.5 \times 0.5 \times 0.5=0.125$.

At the same time, we may ask the question: What is the probability of getting heads in one toss with 3 coins? To answer this question, let us suppose that probability reflects not only the average of getting of heads (which is 0.5 ) but also the average number of obtained heads in one toss (it may be 1.5 , for example). In this case, the probability of having heads in tossing three coins once is $p_{3}(h) =0.5+0.5+0.5=1.5$.

The difference between these two situations is that in the first case, getting one head and getting two heads are different events (outcomes of the experiment). In contrast to this, in the second case, getting one head and getting two heads are different parts of the same event, or better to say, the same multi-event (parts of the same outcome of the experiment). It means that an
outcome may have a weight, e.g., when two heads occur, the weight is 2 , while when three heads occur, the weight is 3 .

Note that with the growth of the number of the tossed coins, the probability of having heads also grows being larger than 1 when there are more than two coins.

Example 2. In an experiment, 10 dice are rolled. Let us ask the question: What is the probability of showing three spots in one experiment? To calculate this probability, we assume that all dice are without defects and all rollings are fair and independent. In this case, the probability of having three spots in one rolling is $p_{1}=1 / 6$ for one die and $p_{10}=10 / 6$.

Now we can describe a general schema for frequency interpretation of inflated or larger than 1 probability.

As usually, we start with elementary (random) events but instead of a set of these events, we consider a multiset $\Omega$ of elementary (random) events. Informally, a multiset is a collection that is like a set but can include identical or indistinguishable elements (Aigner, 1979; Knuth, 1997). Thus, we take a multiset $\Omega=\left\{n_{1} w_{1}, n_{2} w_{2}, n_{3} w_{3}, \ldots, n_{k} w_{k}\right\}$. In it, $w_{i}$ are elementary events, or more exactly, types of elementary events and $n_{i}$ is the multiplicity, i.e., the number, of copies of the elementary event $w_{i}$ in $\Omega$ for all $i=1,2,3, \ldots, k$. For instance, $\{3 a, 7 b\}$ is the multiset $\{a, a, a, b$, $b, b, b, b, b\}$, which contains three elements $a$ and seven elements $b$. To be exact, $\{3 a, 7 b\}$ is the multinumber (cardinality) of the multiset $\{a, a, a, b, b, b, b, b, b, b\}$ (Burgin, 2011), but many researchers used multinumbers as representations of multisets and for simplicity, we follow this tradition.

Subsets of the multiset $\Omega$ are called events. For instance, $\{a, 3 b\}$ and $\{5 b\}$ is the submultiset but not a subset of the multiset $\{3 a, 7 b\}$. At the same time, $\{a, b\}$ and $\{b\}$ are subsets of the multiset $\{3 a, 7 b\}$. In other words, a subset of a multiset $A$ are sets such that their elements are also elements of $A$.

We assume that the following axiom is true.
Decomposability Axiom. An event $A$ occurs in a trial if and only if some elementary event from $A$ occurs in this trial.

However, when we have a multiset of elementary events, it is natural to assume, as in the examples considered above, that it is possible that several elementary events from $A$ and even several elementary events of the same type from $A$ occur in one trial. To formalize this situation, we use the following axiom.

Boundary Axiom. The number of occurrences of an elementary event $w_{i}$ from $A$ in one trial cannot be larger than the multiplicity $n_{i}$ of this event in $\Omega$.

Taking an event $A=\left\{w_{i 1}, w_{i 2}, w_{i 3}, \ldots, w_{i r}\right\}$ and a sequence of $N$ trials, we denote by $N$ the number of events from $\Omega$ that occur during this sequence of trials and by $n$ the sum of multiplicities of events from $A$ that occur during this sequence of trials. Then we have the frequency

$$
r_{N}(A)=n / N
$$

In contrast to conventional trials it is possible that $r_{N}(A)>1$ because the same event can occur several times in one trial. For instance, if $A$ occurs 3 times in each of $N$ trials, then $r_{N}(A)=3$.

Let us consider the set $\boldsymbol{P}_{A}$ of all events $A$ such that limits $\lim _{N \rightarrow \infty} r_{N}(A)$ exist. We call these events quasirandom. Random events satisfy additional conditions considered by different authors. Then we define the inflated frequency probability of the event $A$ as

$$
p(A)=\lim _{N \rightarrow \infty} r_{N}(A)
$$

In other words, when the number $N$ of trials goes to infinity ( $N \rightarrow \infty$ ) the number $r_{N}(A)$ approaches the inflated frequency probability of the event $A$. The regularity of $r_{N}(A)$ converging to a proper fraction characterizes the meaning of the probability of the event $A$.

Note that the conventional frequency probability is a particular case of the inflated frequency probability when elementary events form a set, i.e., all their multiplicities are equal to 1 .

Let us study properties of inflated frequency probabilities. It is easy to see that they do not satisfy standard probability properties. For instance, in a general case, $p(\Omega)>1$.

However, some standard probability properties remain true. Properties of limits imply the following result.

Proposition 1. The inflated frequency probability $p$ of the union of two disjoint quasirandom events $A$ and $B$ is equal to $p(A \cup B)=p(A)+p(B)$, i.e., $A \cap B=\emptyset$ implies $p(A \cup B)=p(A)+p(B)$.

Usually it is assumed that $p(\varnothing)=0$. However, this property also depends on the initial axioms. Let us consider two such axioms.

Occurrence Axiom. In any trial, at least one elementary event occurs.
Weak Occurrence Axiom. In any trial, at least one event occurs.
Lemma 1. The Occurrence Axiom implies the Weak Occurrence Axiom.
Proposition 2. If the Occurrence Axiom is true, then the inflated frequency probability, probability $p$ of the empty event is equal to zero.

Lemma 2. The Decomposability Axiom and Weak Occurrence Axiom imply the Occurrence Axiom.

Corollary 1. If the Decomposability Axiom is true, then the inflated frequency probability $p$ of the empty event is equal to zero.

Trying to find a criterion, i.e., the necessary and sufficient conditions, for the equality $p(\varnothing)=0$, we come to the following axiom.

Finite Occurrence Axiom. In any sequence of trials, there is only a finite number of trials when at least one elementary event does not occur.

However, we also need a weaker condition.
Infinite Occurrence Axiom. In any sequence of trials, there are an infinitely many trials when at least one elementary event occurs.

This axiom allows us to prove the following result.
Proposition 3. The inflated frequency probability $p(\varnothing)$ is equal to zero if and only if the ratio of all trial in which nothing happened to all trials tends to 0 .

Corollary 2. The inflated frequency probability $p(\varnothing)$ is equal to zero only if the Infinite Occurrence Axiom is true.

Corollary 3. The inflated frequency probability $p(\varnothing)$ is equal to zero if the Finite Occurrence Axiom is true.

Finite Occurrence Condition. In any sequence of trials, there only a finite number of trials when an elementary event from $A$ occurs.

This condition allows us to prove the following result.
Proposition 4. The inflated frequency probability $p(A)$ of a quasirandom (random) event $A$ is equal to zero if the Finite Occurrence Condition is true.

Corollary 4. The inflated frequency probability $p(A)$ of a quasirandom (random) event $A$ is not equal to zero only if the Infinite Occurrence Axiom is true.

Many properties of inflated frequency probabilities are different from the standard probability properties.

Proposition 5. The inflated frequency probability $p(A)$ of a quasirandom (random) event $A$ cannot be larger than the sum of the multiplicities of the elements from $A$, i.e., if $A=\left\{w_{i 1}, w_{i 2}, w_{i 3}\right.$, $\left.\ldots, w_{i r}\right\}$, then

$$
p(A) \leq n_{i 1}+n_{i 2}+n_{i 3}+\ldots+n_{i r}
$$

where $n_{i 1}, n_{i 2}, n_{i 3}, \ldots, n_{i r}$ are multiplicities of the elements $w_{i 1}, w_{i 2}, w_{i 3}, \ldots, w_{i r}$ in the multiset $\Omega$.
The constructed interpretation is similar to the traditional frequency interpretation of probability. However, in our situation, several elementary events from $A$ can occur in one trial.

Let us consider the following axiom.
Outcome Axiom (OA). In each trial, exactly one elementary event happens.
Note that it can be several occurrences (copies) of one and the same elementary event in one trial.

We can see that when the Outcome Axiom is taken instead of the Boundary Axiom, we exactly obtain the traditional frequency interpretation of the classical probability.

This interpretation explains why larger than 1 (inflated) probabilities, at first, appeared in quantum physics and then proliferated to other disciplines. Indeed, according to modern quantum physics, all subatomic particles, such as electrons, protons or neutrons, are identical or indistinguishable. As a result, collections of subatomic particles are multisets and not sets because in sets according to the modern set theory all elements are distinguishable from one another (Fraenkel and Bar-Hillel, 1958; Kuratowski and Mostowski, 1967).

It is possible to construct another formalization of inflated (larger than 1) probabilities when instead of the Boundary Axiom, we use the following axiom.

Single Type Axiom. In each trial, elementary events of only one type happen and their number cannot be larger than the multiplicity of this element in the multiset $\Omega$.

Note that the Single Type Axiom implies the Boundary Axiom.
Proposition 6. If the Single Type Axiom is valid, then the inflated frequency probability $p(A)$ of a quasirandom (random) event $A$ cannot be larger than the maximum of the multiplicities of the elements from $A$, i.e., if $A=\left\{w_{i 1}, w_{i 2}, w_{i 3}, \ldots, w_{i r}\right\}$, then

$$
p(A) \leq \max \left\{n_{i 1}, n_{i 2}, n_{i 3}, \ldots, n_{i r}\right\}
$$

where $n_{i 1}, n_{i 2}, n_{i 3}, \ldots, n_{i r}$ are multiplicities of the elements $w_{i 1}, w_{i 2}, w_{i 3}, \ldots, w_{i r}$ in the multiset $\Omega$.
As the conventional frequency probability is a particular case of the inflated frequency probability when multiplicities of all elementary events are equal to 1 , we have the classical property of probability.

Corollary 5. If the Single Type Axiom is true, then the frequency probability $p(A)$ of the empty event is equal to zero.

Conventional probability also has a subjective interpretation, which is identified as a belief or measure of confidence in an outcome of a certain event. In some cases, an adequate treatment of subjective interpretations brings researchers to inflated probabilities. To show this, let us consider the following situation.

In a criminal investigation, the detective gets some evidence that strongly shows that the main suspect is not guilty. To express his confidence, the detective says: "Oh, I'm $70 \%$ sure that this woman is not guilty." According to the subjective interpretation, $70 \%$ mean that the probability of the woman's innocence is 0.7 .

After some time, the detective gets even more persuading evidence and when asked by his chief, the detective says: "Now I'm two times more confident that this woman is not guilty." However, two times $70 \%$ gives us $140 \%$ and according to the conventional probability theory, this is impossible because $140 \%$ mean that the probability of the woman's innocence is 1.4 , while larger than 1 probabilities are not permitted. However, if we allow larger than 1 probabilities, the statement of the detective becomes clear.

This situation and many other similar situations, for example, in financial decision making, show that inflated probabilities have a meaningful subjective interpretation and this interpretation allows people to explain not only phenomena in physics or finance but many situations in their everyday life.

## 3. Negative Interest Rates and the Problem of Their Modeling

### 3.1 Situations When Nominal Interest Rates Became Negative

Negative nominal interest rate are a seldom phenomenon in financial practice. However, they have occurred several times as in the 1970s in Switzerland. Investors had invested at negative interest rates in the safe haven Switzerland since they believed the Swiss Franc would increase. In addition, some investors avoided paying taxes in their home country. Negative interest rates also occurred in Japan in the 1990s, in 2003 in the USA and during the global financial crisis 2008/2009.

For instance, in Japan in the 1990s, banks lent Japanese Yen and were willing to receive a lower Yen amount back several days later. This means de facto a negative nominal interest rate. The reason for this unusual practice was that banks were eager to reduce their exposure to Japanese Yen, since confidence in the Japanese economy was low and the Yen was assumed to devalue.

Similarly, in the US, from August to November 2003, 'repos', i.e. repurchase agreements, were traded at negative interest rates. A repo is just a collateralized loan, i.e. the borrower of money gives collateral, for example a Treasury bond, to the lender for the time of the loan. When the loan is paid back, the lender returns the collateral. However, in 2003 in the US, settlement problems when returning the collateral occurred. Hence the borrower was only willing to take the risk of not having the collateral returned if he could pay back a lower amount than originally borrowed. This constituted a negative nominal interest rate.

A further example of the market expecting the possibility of negative nominal interest rates occurred in the worldwide 2008/2009 financial crisis, when strikes on options on Eurodollars Futures contracts were quoted above 100. A Eurodollar is a dollar invested at commercial banks outside the US. A Eurodollar futures price reflects the anticipated future interest rate. The rate is calculated by subtracting the Futures price from 100. For example, if the 3 month March Eurodollar future price is 98.5 , the expected interest rate from March to June is $100-98.5=1.5$, which is quoted in per cent, so $1.5 \%$. In March 2009, option strikes on Eurodollar future contracts were quoted above 100 on the CME, Chicago Mercantile Exchange. This means that market participants could buy the right to pay a negative nominal interest on US dollars in the future if desired. The reason for this unusual behavior is that investors wanted to invest in the safe haven currency US dollar even if they had to pay for it.

### 3.2 Modeling Interest Rates

In finance, interest rates are typically modeled with a geometric Brownian motion,

$$
\begin{equation*}
\frac{d r}{r}=\mu_{r} d t+\sigma_{r} \varepsilon \sqrt{d t} \tag{1}
\end{equation*}
$$

$\mathrm{d} r$ is the change in the interest rate $r$, $\mu_{r}$ is the drift rate, which is the expected growth rate of $r$, assumed non-stochastic and constant, $\sigma_{r}$ is the expected volatility of the rate $r$, assumed nonstochastic and constant, $\varepsilon$ is a random drawing from a standardized normal distribution. All drawings at times $t$ are independent.

From equation (1), we can see that the relative change $\mathrm{d} r / r$ is normally distributed, since $\varepsilon$ is normally distributed. If the relative change of a variable is normally distributed, it follows that the variable itself is lognormally distributed with the probability distribution function (PDF)

$$
\begin{equation*}
\frac{1}{x \sigma \sqrt{2 \pi}} \exp \left\{-\frac{1}{2}\left(\frac{\ln (x)-\mu}{\sigma}\right)^{2}\right\} \tag{2}
\end{equation*}
$$

In the equation (2), $\mu$ and $\sigma$ are the mean and standard deviation of $\ln (x)$ respectively. Figure 1 shows a lognormal distribution.

The logarithm of a negative number is not defined, hence with the PDF defined by expression (2), negative values of interest rates cannot be modeled. However, as discussed above, negative interest rates do exist in the real financial world. Here negative probabilities come into play. We will explain this with options on interest rates.

![](https://cdn.mathpix.com/cropped/2025_11_22_4af52cdcaca0c62e2ff2g-08.jpg?height=550&width=1104&top_left_y=1237&top_left_x=543)
Figure 1. Lognormal distribution with $\mu=0$ and $\sigma=1$

## 4. How Inflated Probabilities Allow More Adequate Interest Rate Modeling

### 4.1 Modeling Interest Rate Options

In the interest rate market, the main types of options are Caps and Floors, Bond options, and Swap options. A Cap is a series of Caplets and a Floor is a series of Floorlets. We will discuss Caplets and Floorlets in this paper.

Caplets and Floorlets are typically valued in the Black-Scholes-Merton framework (Black and Scholes, 1973; Merton, 1973; Black, 1976):

$$
\begin{equation*}
\text { Caplet }_{t_{s}, t l}=m \mathrm{PA} e^{-r_{l} t} l \quad\left\{r_{f} \mathrm{~N}\left(d_{1}\right)-r_{k} \mathrm{~N}\left(d_{2}\right)\right\} \tag{3}
\end{equation*}
$$

$$
\begin{equation*}
\text { Floorlet }_{t_{s}, t_{l}}=m \text { PA } e^{-r_{l} t_{l}}\left\{r_{k} \mathrm{~N}\left(-d_{2}\right)-r_{f} \mathrm{~N}\left(-d_{1}\right)\right\} \tag{4}
\end{equation*}
$$

where $d_{1}=\frac{\ln \left(\frac{\mathrm{r}_{\mathrm{f}}}{\mathrm{r}_{\mathrm{k}}}\right)+\frac{1}{2} \sigma^{2} \mathrm{t}_{\mathrm{x}}}{\sigma \sqrt{\mathrm{t}_{\mathrm{x}}}}$, and $d_{2}=d_{1}-\sigma \sqrt{\mathrm{t}_{\mathrm{x}}}$.
Caplet ${ }_{t_{s}, t l}$ is the option on an interest rate from time $t_{s}$ to time $t_{l}$, where $t_{l}>t_{s}$, i.e., it means the right but not the obligation to pay the rate $r_{K}$ at time $t_{1}$.

Floorlet ${ }_{t_{S}, t_{l}}$ is the option on an interest rate from time $t_{s}$ to time $t_{l}$, where $t_{l}>t_{s}$, i.e., it means the right but not the obligation to receive the rate $r_{K}$ at time $t_{1}$. Here $m$ is time between $t_{s}$ and $t_{l}$, expressed in years; $t_{x}$ is the option maturity time; $t_{x} \leq t_{s}<t_{l}$; PA is the principal amount; $r_{K}$ is the strike rate, i.e., the interest rate that the Caplet buyer may pay and the Floorlet buyer may receive from time $t_{s}$ to time $t_{l}$; and $\mathrm{r}_{\mathrm{f}_{\mathrm{s}}, \mathrm{t}_{\mathrm{l}}}$ is the forward interest rate from $t_{s}$ to $t_{l}$, derived as

$$
\begin{equation*}
\mathrm{r}_{\mathrm{t}_{\mathrm{t}_{\mathrm{s}}, \mathrm{t}}}=\left(\frac{\mathrm{df}_{\mathrm{t}_{\mathrm{s}}}}{\mathrm{df}_{\mathrm{tl}}}-1\right)\left(\frac{1}{\mathrm{t}_{1}-\mathrm{t}_{\mathrm{s}}}\right) \tag{5}
\end{equation*}
$$

where $\mathrm{d} f$ is a discount factor, i.e. $\mathrm{d} f_{t y}=1 /\left(1+r_{y}\right)$.

### 4.2 Applying Inflated Probabilities to Caplets and Floorlets

As it is demonstrated above, the market applied lognormal distribution, which is underlying the valuation of interest rate derivatives, cannot model negative interest rates. One seeming solution would be to add a location parameter to the lognormal distribution. Hence equation (1) $\frac{1}{x \sigma \sqrt{2 \pi}} \mathrm{e}^{-\frac{1}{2}\left(\frac{\ln (x)-\mu}{\sigma}\right)^{2}}$ becomes $\frac{1}{(x-\alpha) \sigma \sqrt{2 \pi}} \mathrm{e}^{-\frac{1}{2}\left(\frac{\ln (x-\alpha)-\mu}{\sigma}\right)^{2}}$, where $\alpha$ is the location parameter. For $\alpha>0$, the lognormal distribution is shifted to the right. As a result, the probabilities to the right of the mean would increase, which gives the desired result (see below for details). However, probabilities to the left of the mean would decrease, which is undesired. Hence this solution is inapplicable.

A consistent way to model options on negative interest rates is to apply inflated probabilities to equations (3) and (4). We add a parameter $\beta$ to equations (3) and (4) and for simplicity, we set $m=$ 1 and $\mathrm{PA}=1$. Hence we derive

$$
\begin{align*}
& \text { Caplet }_{t_{s}, t_{l}}=\mathrm{e}^{-r_{l} t}\left\{r_{f}\left[\mathrm{~N}\left(d_{1}\right)-\beta\right]-r_{k}\left[\mathrm{~N}\left(d_{2}\right)-\beta\right]\right\} \quad \beta \in \Re  \tag{6}\\
& \text { Floorlet }_{t_{s}, t l}=\mathrm{e}^{-r_{l} t}\left\{r_{k}\left[\mathrm{~N}\left(-d_{2}\right)-\beta\right]-r_{f}\left[\mathrm{~N}\left(-d_{1}\right)-\beta\right]\right\} \tag{7}
\end{align*}
$$

where $d_{1}=\frac{\ln \left(\frac{\mathrm{r}_{\mathrm{f}}}{\mathrm{r}_{\mathrm{k}}}\right)+\frac{1}{2} \sigma^{2} \mathrm{t}_{\mathrm{x}}}{\sigma \sqrt{\mathrm{t}_{\mathrm{x}}}}$ and $d_{2}=d_{1}-\sigma \sqrt{\mathrm{t}_{\mathrm{l}}}$.
This brings us to inflated probabilities which can imply negative interest rates. Let's show this. From basic option theory we know that the value of a Floorlet is divided into intrinsic value IV and time value TV:

$$
\begin{equation*}
\text { Floorlet } t_{\mathrm{s},} t_{l}=\mathrm{IV}_{\text {Floorlet }}+\mathrm{TV}_{\text {Floorlet }} \geq 0 \tag{8}
\end{equation*}
$$

The intrinsic value is defined $\mathrm{IV}_{\text {Floorlet }}=\max \left(r_{k}-r_{f}, 0\right)$, where $r_{f}$ is derived by equation (5). For simplicity we assume that the yield curve is flat. It follows that $r=r_{f}$ and we derive

$$
\begin{equation*}
\mathrm{IV}_{\text {Floorlet }}=\max \left(r_{k}-r, 0\right) \tag{9}
\end{equation*}
$$

Let's investigate the case of the Floorlet being in-the-money and the Caplet being out-of-themoney i.e. $r_{k}>r$. Hence equation (9) changes to

$$
\begin{equation*}
\mathrm{IV}_{\text {Floorlet }}=r_{k}-r \tag{10}
\end{equation*}
$$

Since a Floorlet does not pay a return, the time value of a Floorlet is bigger than 0 ,

$$
\begin{equation*}
\mathrm{TV}_{\text {Floorlet }} \geq 0 \tag{11}
\end{equation*}
$$

With a negative $\beta$, inflated probabilities can emerge for certain input parameter constellations of equations (6) and (7). In particular, the probabilities $\mathrm{N}\left(d_{1}\right)-\beta, \mathrm{N}\left(d_{2}\right)-\beta, \mathrm{N}\left(-d_{2}\right)-\beta$ and $\mathrm{N}\left(-d_{1}\right)-\beta$ may become larger than 1 . In this case, from equation (7), the resulting Floorlet price can become, especially for low implied volatility, smaller than the intrinsic value, i.e. Floorlet $t_{s}, t l<\mathrm{IV}_{\text {Floorlet }}$. From equations (8), (10), and (11), this implies that $r<0$ for small values of $r_{K}$. Hence we have an extension of the lognormal distribution with inflated probabilities associated with negative values for $r$. Graphically this can be expressed by an upward shift of the lognormal distribution (see Figure 1), which creates a PDF function with a probability area larger than one.

The lower the value of $\beta$, the more likely it is that inflated probabilities with associated negative interest rates will emerge. This lowers Caplet prices and increases the Floorlet price, which is a desired result, since it adjusts the Caplet and Floorlet prices for the possibility of negative interest rates. The magnitude of the parameter $\beta$, that a trader applies, reflects a trader's opinion on the possibility of negative rates. The lower, including negative interest rates, a trader expects, the lower is the beta she will input in equations (6) and (7).

Let us combine these results with the results derived for negative probabilities in the paper on negative interest rates, Burgin and Meissner (2011). We observe that depending on the parameter constellations of the Black-Scholes-Merton model in some cases negative probabilities and in some cases inflated probabilities imply negative interest rates. In particular, in the case of $r_{k}<r$, negative probabilities imply negative interest rates. In this case the lognormal distribution is extended to the left as seen in Figure 2:

![](https://cdn.mathpix.com/cropped/2025_11_22_4af52cdcaca0c62e2ff2g-10.jpg?height=676&width=1435&top_left_y=1707&top_left_x=346)
Figure 2: An extension of the lognormal distribution with $\mu=0$ and $\sigma=1$

In the case when $r<r_{k}$, inflated probabilities imply negative interest rates, as derived above. In this case the lognormal distribution of Figure 1 is shifted upwards to create a probability space of bigger than 1 .

## 5. Duffie-Singleton Model and Inflated Probabilities

We find a further application of inflated probabilities in the seminal Duffie-Singleton model (Duffie and Singleton, 1999). They prove that a defaultable claim can be priced "if it were default free by replacing the usual short-term interest rate process $r$ with the default-adjusted short-term process $\mathrm{R}_{\mathrm{t}}=r+h_{t} L$ ", where $L$ is the loss in default, i.e. $L=1-\mathrm{RR}$ where RR is the recovery rate and $h_{t}$ is the hazard rate at $t$, i.e. the default probability from $t$ to $t+\mathrm{d} t$ assuming no default until $t$.

Discounting with $\mathrm{R}_{\mathrm{t}}$ results in the value of the defaultable claim V at time $0, \mathrm{~V}_{0}$.

$$
\begin{equation*}
\mathrm{V}_{0}=\mathrm{E}_{0}^{\mathrm{Q}}\left[\exp \left(-\int_{0}^{\mathrm{T}} \mathrm{R}_{\mathrm{t}} \mathrm{dt}\right)\right] \tag{12}
\end{equation*}
$$

where $\mathrm{E}_{0}^{\mathrm{Q}}$ is the risk-neutral expectation under the equivalent martingale measure Q at date 0 .
For ease of explanation, let us set $r=0$ and $\mathrm{RR}=0$ so, that $L=1$. As a result $R_{t}=h_{t}$ and equation (12) changes to

$$
\begin{equation*}
\mathrm{V}_{0}=\mathrm{E}_{0}^{\mathrm{Q}}\left[\exp \left(-\int_{0}^{\mathrm{T}} \mathrm{~h}_{\mathrm{t}} \mathrm{dt}\right)\right] \tag{13}
\end{equation*}
$$

Utilization of the conventional probability theory creates a discrepancy between the equation (13) and extreme values of the hazard rate $h_{t}$. By the conventional probability definition, the value $h_{t}$ is limited to 1 . However, in the extreme case of $h_{t}=1$, i.e., when there is a certain default, the defaultable claim $V_{0}$ should be zero. However equation (13) implies $V_{0}>0$ when $h_{t} \leq 1$. Rather than discarding the whole model, we suggest a solution, namely, introduction of a possibility that the hazard rate $h_{t}$ can be larger than 1 . Then taking the limit $\lim _{t \rightarrow \infty} h_{t} \rightarrow \infty$, we see that equation (13) gives the correct value of the defaultable claim $V_{0}$ of 0 .

## 6. Concluding Summary

We defined generalized probabilities, which include inflated probabilities, build their interpretations and derived their general properties. Then we applied generalized probabilities to financial modeling demonstrating that negative nominal interest rates have occurred several times in the past in financial practice, for example, in the 2008/2009 global financial crisis. This is inconsistent with the conventional theoretical models of interest rates, which typically apply a lognormal distribution. In particular, when Caps and Floors are valued in a lognormal Black-Scholes-Merton framework, then the probability of negative interest rates is zero. Here larger than 1 probabilities come into play. We demonstrated that for in-the-money Floors and out-of-the-money Caps, i.e., with the parameter constellation $r<r_{k}$, integrating inflated probabilities into the Black-Scholes-Merton framework allows one to consistently model negative nominal interest rates, which occur in financial practice.

## References

[1] Aigner, M.(1979), Combinatorial Theory, Springer Verlag, New York/Berlin.
[2] Bartlett, S.( 1945), "Negative Probability", Math Proc Camb Phil Soc, 41: 71-73.
[3] Black F. and M. Scholes (1973), "The Pricing of Options and Corporate Liabilities", The Journal of Political Economy, 81(3): 637-654.
[4] Black, F. (1976), "The Pricing of Commodity Contracts", Journal of Financial Economics, 3(12): 167-179.
[5] Burgin, M. (2011), Theory of Named Sets, Nova Science Publishers, New York.
[6] Burgin, M. and Meissner, G. (2011), "Negative Probabilities in Modeling Random Financial Processes", Integration, 2(3): 305-322.
[7] Burgin, M. and G. Meissner (2012), "Negative Probabilities in Financial Modeling", Wilmott Journal, 2012(58): 60-65.
[8] Dirac, P.A.M. (1942), "The Physical Interpretation of Quantum Mechanics", Proc. Roy. Soc. London, 180(980): 1-39.
[9] Dirac, P.A.M. (1943), Quantum Electrodynamics, Communications of the Dublin Institute for Advanced Studies.
[10] Duffie, D. and Singleton, K. ( 1999), "Modeling Term Structures of Defaultable Bonds", Review of Financial Studies, 12(4): 687-720.
[11] Feynman, R. P. (1950), "The Concept of Probability Theory in Quantum Mechanics", In: The Second Berkeley Symposium on Mathematical Statistics and Probability Theory, University of California Press, Berkeley, California.
[12] Feynman, R. (1987), "Negative Probability", In: Quantum Implications: Essays in Honour of David Bohm, Routledge \& Kegan Paul Ltd, London \& New York, pp. 235-248.
[13] Fraenkel, A.A. and Bar-Hillel, Y. (1958), Foundations of Set Theory, North Holland P.C., Amsterdam.
[14] Gell-Mann, M. and Hartle, J. B. (2012), "Decoherent Histories Quantum Mechanics with One 'Real' Fine-Grained History", Physical Review A, 85(6): 21-31.
[15] Haug, E.G.(2004), "Why so Negative to Negative Probabilities?", Wilmott Magazine, Sep/Oct 2004: 34-38.
[16] Holland, R. E. , F. J. Lynch, G. J. Perlow and S. S. Hanna (1960), "Time Spectra of Filtered Resonance Radiation of $\mathrm{Fe}^{57}$," Phys. Rev Let., 4(4): 181-182.
[17] Khrennikov, A.(1992), "p-adic probability and statistics", Dokl. Akad. Nauk, v.322, p.10751079.
[18] Khrennikov, A. (2009), Interpretations of Probability, Walter de Gruyter, Berlin/New York.
[19] Kline, M. (1980), Mathematics: The Loss of Certainty, Oxford University Press, New York.
[20] Knuth, D. (1997), The Art of Computer Programming, v.2: Semi-numerical Algorithms, Addison-Wesley, Reading, Mass.
[21] Kolmogorov, A. N. (1933), Grundbegriffe der Wahrscheinlichkeitrechnung, Ergebnisse Der Mathematik (English translation: Foundations of the Theory of Probability, Chelsea P.C., 1950).
[22] Kovner, A. and M. Lublinsky (2007), "Odderon and seven Pomerons: QCD Reggeon field theory from JUMWLK evolution", Journal of High Energy Physics, 58(1):1-61.
[23] Kronz, F. (2009), "Actual and Virtual Events in the Quantum Domain", Ontology Studies, 9(9): 209-220.
[24] Kuratowski, K. and Mostowski, A. (1967), Set Theory, North Holland P.C., Amsterdam.
[25] Lynch, F. J., R. E. Holland, and M. Hamermesh (1960), "Time dependence of resonantly filtered gamma rays from $\mathrm{Fe}^{57}$," Phys. Rev. 120(2): 513-520.
[26] Mack, T.(2002), Schadenversicherungsmathematik, $2{ }^{\text {nd }}$ ed. Verlag Versicherungswirtschaft.
[27] Martinez, A.A. (2005), Negative Math: How Mathematical Rules Can Be Positively Bent, Princeton University Press, Boston.
[28] Mattessich, R. (1998), "From accounting to negative numbers: A signal contribution of medieval India to mathematics", Accounting Historians Journal, 25(2): 129-145.
[29] Meissner, G.(1998), Trading Financial Derivatives - Futures, Swaps, and Options in Theory and Application, Pearson.
[30] Meissner. G.(1999), Arbitrage Opportunities in Fixed Income Markets, Derivatives Quarterly, 5(1): 1-8.
[31] Merton R. (1973), "Theory of Rational Option Pricing", Bell Journal of Economics and Management Science, 4(1): 141-183.
[32] Mückenheim, W. (1986), "A review of extended probabilities", Physics Reports, 133(6): 337401.
[33] Nyambuya, G.(2011), Deciphering and Fathoming Negative Probabilities in Quantum Mechanics?(viXra.org > Quantum Physics > viXra:1102.0031).
[34] Sjöstrand, T. (2007), "Monte Carlo Generators", In: 2006 European School of High-Energy Physics, Ed. R. Fleischer, CERN-2007-005, p. 51-73.
[35] Székely, G.J.(2005), "Half of a Coin: Negative Probabilities", Wilmott Magazine, July: 66-68.
[36] Venter G. (2007), "Generalized Linear Models Beyond the Exponential Family with Loss Reserve Applications", Astin Bulletin, 37(2): 345-364.
[37] Weisskopf V., and E. Wigner (1930), "Berechnung der nat urlichen Linienbreite auf Grund der Diracschen Lichttheorie", Z. Phys., 63(1-2): 54-73.
[38] Wigner, E. P. (1932), "On the quantum correction for thermodynamic equilibrium", Phys. Rev., 40(5): 749-759.
[39] Wu, C. S. , Y. K. Lee, N. Benczer-Koller, and P. Simms (1960), "Frequency Distribution of Resonance Line Versus Delay Time", Physical Review Letters, 5(9): 432-435.

