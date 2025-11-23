# THE MINIMUM ENTROPY PRODUCTION PRINCIPLE 

E. T. Jaynes<br>Arthur Holly Compton Laboratory of Physics, Washington University, St. Louis, Missouri 63130

## INTRODUCTION

It seems intuitively reasonable that Gibbs' variational principle determining the conditions of heterogeneous equilibrium can be generalized to nonequilibrium conditions. That is, a nonequilibrium steady state should be the one that makes some kind of generalized entropy production stationary; and even in the presence of irreversible fluxes, the condition for migrational equilibrium should still be the equality of some generalized chemical potentials.

We summarize progress to date toward this goal, reviewing ( $a$ ) the early history, ( $b$ ) work of Onsager and first attempts at generalization, (c) the new direction the field took after 1967 with the work of Tykodi and Mitchell, and (d) the present situation and prospects. Our conclusion will be, briefly, that the outlook is good in that the basic principles are believed known; but we do not yet know whether they can be reduced to simple rules immediately useful in practice, in the way that the Gibbs phase rule is useful. For this, we need more experience in the technique of applying them to particular cases, and more data to test some conjectures.

## EARLY HISTORY

In 1848, Kirchhoff (1) generalized Ohm's law to three dimensions, and noted an interesting fact. If the electric field is $E=-\nabla \phi$, the conductivity $\sigma(x)$, then when a steady state is reached the potential $\phi(x)$ must cause no accumulation of electric charge at any point:

$$
\nabla \cdot(\sigma \nabla \phi)=0 .
$$

But this is just the Euler-Lagrange equation stating that the rate of
production of Joule heat in a volume $V$

$$
\begin{equation*}
\int_{V} \sigma(\nabla \phi)^{2} d V \tag{2.}
\end{equation*}
$$

is stationary with respect to variations $\delta \phi(x)$ that vanish on the boundary of $V$. Thus the current distributes itself so as to dissipate the least possible heat for given voltages applied on its boundary. This is probably the first example of a steady nonequilibrium state determined by a variational principle.

In this respect, quantitative nonequilibrium thermodynamics may claim an earlier origin even than our conventional equilibrium theory, for Kirchhoff's discovery antedated by 27 years Gibbs' announcement (2) of the general variational principle for heterogeneous equilibrium, and even preceded Clausius' introduction (3) of the word "entropy" by 17 years. Yet 125 years after Kirchhoff's result, Girardeau \& Mazo (4) state: "Variational methods for nonequilibrium statistical mechanics are virtually nonexistent." Why, after such a promising head start, has nonequilibrium theory lagged so far behind thermostatics?

It was evident that Kirchhoff's result could be generalized, and quickly other laws of "least dissipation of energy" and the almost equivalent reciprocal relations were found. In particular, an 1859 work of Helmholtz (5), which contained some of his greatest mathematical achievements, gave the acoustical reciprocity theorem, later extended by Rayleigh (6) and Lorentz (7) to mechanics and electrodynamics.

These first applications (where the thermal aspect, although in the picture, was not in the foreground) all involved variational principles for energy dissipation. Gibbs surely had first-hand knowledge of them, for he had spent a post-doctoral year (1868-1869) with Kirchhoff and Helmholtz in Heidelberg. But in Gibbs' own work, which began to appear four years later, the thermal aspect was the primary thing, and he gave instead a variational principle for entropy.

Gibbs lived another 25 years after completing his monumental work on heterogeneous equilibrium. Why then, with his seemingly perfect background for it, did not Gibbs himself generalize the KirchhoffHelmholtz results, and announce the principle of minimum entropy production 100 years ago? Perhaps Gibbs saw at once the difficulty.

Anyone familiar with Kirchhoff's work might simplify the arrangement to this: two resistors $R_{1}, R_{2}$ are in thermal contact with two heat reservoirs at temperatures $T_{1}, T_{2}$. Connecting the resistors in parallel, we send a total current $I=I_{1}+I_{2}$ through them. How does it divide?

When a steady state is reached, the rates of production of heat and entropy are $\dot{Q}=R_{1} I_{1}^{2}+R_{2} I_{2}^{2}, \dot{S}=\left(R_{1} / T_{1}\right) I_{1}^{2}+\left(R_{2} / T_{2}\right) I_{2}^{2}$. The entropy
production is a minimum when the current distribution satisfies $R_{1} I_{1} / T_{1}=R_{2} I_{2} / T_{2}$. We know, of course, that the actual distribution will satisfy $R_{1} I_{1}=R_{2} I_{2}$, which is the condition for minimum heat production.

The example is admittedly oversimplified; but one can invent arbitrarily complicated networks with the resistors at different temperatures and again, given the existence of a potential field $\phi(x)$ and the phenomenological laws $\Delta \phi_{i}=R_{i} I_{i}$ connecting current and potential difference for the individual elements, the steady-state current distribution for any applied voltages or currents is completely determined by Kirchhoff's condition of charge conservation at the nodes; there is logically no room for any further principle.

Now there is nothing special about electric current; what is true for fluxes of electrons is surely true for fluxes of any kind of stable particles, or of anything else that is conserved (energy, momentum, etc). Given the phenomenological relations connecting fluxes and forces, the steady state is determined by the conservation laws, leaving no room for any other principle; but then, what are we to make of the recent discussions of it?

Prigogine (8) postulates the existence of fluxes $J_{i}$ and forces $X_{i}$, connected by the phenomenological relations $J_{i}=L_{i j} X_{j}$ (summation over repeated indices understood), so defined that the rate of entropy production is $\dot{S}=J_{i} X_{i}=L_{i j} X_{i} X_{j}$. Considering some of the forces to be fixed and others to be free, the condition that $\dot{S}$ be a minimum with respect to a free variable $X_{m}$ is $\partial \dot{S} / \partial X_{m}=\left(L_{m j}+L_{j m}\right) X_{j}=0$, if the $L_{i j}$ are constants. But if the reciprocal relations $L_{i j}=L_{j i}$ hold, this is the same as $J_{m}=0$, which is considered synonymous with "stationary state." This is the entire content of his theorem.
de Groot \& Mazur (9) generalize Prigogine's treatment by taking spatial variations (but not convection currents) into account. They undertake to show that in heat conduction, "the stationary state is characterized by a minimum of the entropy production, compatible with the imposed temperature distribution at the walls of the system." Their proof is a paraphrase of Kirchhoff's, and it requires the assumption that the phenomenological coefficient $L_{q q}$ defined by the heat current expression $J_{q}=L_{q q} \nabla\left(T^{-1}\right)$ is independent of temperature; i.e. that the thermal conductivity $\lambda$ defined by $J_{q}=-\lambda \nabla T$ varies with temperature as $T^{-2}$.

Since there is no known substance obeying this relation, there is no real situation involving heat conduction where the stationary state would be predicted quantitatively by minimizing entropy production. If $\lambda \propto T^{b}$, the steady state is the condition for minimum rate of production
of the quantity $F=\int T^{b+2} d S$. But for all $b$, the steady state is predicted correctly by energy conservation, $\nabla \cdot J_{q}=\nabla \cdot\left(T^{b} \nabla T\right)=0$. The same difficulty would have invalidated Kirchhoff's theorem if the electric conductivity $\sigma$ varied with the potential $\phi$.
de Groot \& Mazur then give a more general example involving simultaneous heat conduction, diffusion, and chemical reactions. Their argument must now assume all the phenomenological coefficients $L_{i j}$ involved to be independent of both temperature and the concentrations of the participating substances.

In all the examples given in $(8,9)$, after these restrictive assumptions are made the final Euler-Lagrange equations expressing minimum entropy production reduce simply to the conservation laws, which were valid exactly without any restrictive assumptions. So if we have enough information to apply the principle with any confidence, then we have more than enough information to solve the steady-state problem without it. This same criticism was made by Klein (10).

Gibbs surely would not have given any principle unless it met his standards of logical precision and was of some constructive use; so we are no longer surprised at his failure to give this one.

Yet after all criticisms, there remains a feeling that the principle does at least hint at an important truth, however imperfectly expressed. If the principle had nothing in it but misdirection, there would be no reason to write a review article about it.

## REORIENTATION

There is a major part missing from our theoretical structure: On the one hand, the Kirchhoff-Helmholtz principles call out for generalization to thermodynamics; on the other, Gibbs' variational principle calls out for generalization to nonequilibrium cases. Surely, this gap can be filled; i.e. there must exist an exact variational principle for steady irreversible processes. It should include Gibbs' principle as a special case and be also (a) precise and general, requiring no restrictive assumptions like the above, and $(b)$ constructive, yielding useful information that we would not have without it. But to find such a principle we must reorient our thinking in two respects.

First, we note the backward direction of the logic in the aforementioned examples. One assumed phenomenological forms which were only approximate; then stated a principle which could be only an approximate substitute for the conservation laws. We should rather take the conservation laws as exact and given, and seek a principle which gives the correct phenomenological relations without our having to
assume them. It is reasoning in this direction that might lead to a precise, constructive principle.

But reversing the direction of the logic ought to reverse the principle. If the conservation laws represent the approximate condition of minimum entropy production for prescribed approximate phenomenological laws, then perhaps the exact phenomenology is the one that has maximum entropy production for prescribed exact conservation laws. Indeed, such a reversed principle would be much closer to the spirit of Gibbs' work.

Second, we need a verbal reorientation. The main difficulties that have retarded progress for a century are not mathematical, but conceptual; and these in turn are mainly artifacts of semantics. The words "irreversible," "entropy," "probability" are used indiscriminately with many different meanings, and the fact that the same word is used prevents many from seeing that the meanings are different.

Thus such a common phrase as "the paradox of how to reconcile the irreversibility of the second law with the reversibility of the equations of motion" records not a paradox but an abuse of language, the term "reversible" being used with two entirely different meanings. It is impossible to think and communicate rationally about these problems unless we use different words and symbols to convey different ideas.

By far the most abused word in science is "entropy." Confusion over the different meanings of this word, already serious 35 years ago, reached disaster proportions with the 1948 advent of Shannon's information theory, which not only appropriated the same word for a new set of meanings; but even worse, proved to be highly relevant to statistical mechanics. So it is necessary to insert at this point a short lexicon.

## ENTROPY

As befits a word with many mutually contradictory meanings, "entropy" has also a rich and varied folklore concerning its etymology. According to Prigogine (8) it comes "from the Greek $\varepsilon \nu T \rho o \pi \eta$ meaning 'evolution'." According to Clausius (3) it comes from $\tau \rho o \pi \eta$, meaning "a turning" or "a turning point" (the same root that appears in isotropic, phototropic, troposphere, etc). Clausius states that he added the en- only to make the word look and sound like "energy," although he might have noted that en- is in Greek, as in German and English, a standard modifying prefix, and $\varepsilon \nu \tau \rho o \pi \eta$ which (according to three Greek dictionaries and two Greek friends) means "to turn one's head aside," rather neatly expresses the one-sided character of $S$ that he had discovered. Because every

German noun is required to have a gender he also determined, by means unexplained, that "Die Entropie" is feminine.

Prigogine \& Mayné (11) consider a quantity $S_{P M}$ which they call "entropy," so defined that only near equilibrium can one express it in terms of macroscopic quantities. Their "second law" $\dot{S}_{P M} \geqslant 0$ is then to be a theorem in dynamics, and not in phenomenological physics.

The "entropies" with which we shall be concerned here are of a totally different nature. First is the experimental entropy $S_{E}$ of Clausius, Gibbs, and G. N. Lewis, which is by construction a function $S_{E}(T, P, M, \ldots)$ of the observed macroscopic quantities. For us, as for them, the term "second law" refers to a property of $S_{E}$ observed in laboratory experiments. It is therefore, by definition, a proposition of macroscopic phenomenology. Whether it might be also a theorem in dynamics was answered in the negative already by Gibbs (2) with a very vivid example of gas diffusion.

Second, we use the information entropy $S_{I}=-\sum p_{i} \log p_{i}$, a property of any probability distribution. In quantum theory, the $\left\{p_{i}\right\}$ are eigenvalues of a density matrix $\rho$, and $S_{I}(\rho)=-\operatorname{Tr}(\rho \log \rho)$.

If $S_{I}$ is maximized subject to certain constraints $\left\{A_{1} \ldots A_{n}\right\}$, the maximum attained defines a third entropy $S\left(A_{1} \ldots A_{n}\right)=\left(S_{I}\right)_{\text {max }}$, which is a function of those constraints. Since we may choose the constraints in many different ways, there are many different quantities $S(A)$, with different meanings. Just as Clausius' $S_{E}$ is undefined until we specify which macroscopic variables are to be used, one must also indicate in each case which constraints are used-and therefore become the independent variables-in defining $S(A)$. In our applications, the $\left\{A_{i}\right\}$ may be any macroscopic quantities about which we have some information.

To keep the distinctions clear, our $S_{E}$ is, as in conventional thermodynamics, a numerical multiple of Boltzmann's constant $k$, while $S_{I}$ and $S(A)$ are dimensionless, following Shannon. Being defined as the maximum in a constrained variational problem, $S(A)$ will have, like $S_{E}$, a tendency to increase whenever a constraint is removed, thus paralleling in our mathematics what is observed in the laboratory (12).

Many other entropies appear in the literature, among which we note the Boltzmann and Gibbs $S_{B}, S_{G}$ defined from the single-particle and $N$-particle distribution functions, and the quantity $S_{B E P}=k \log W$ of Boltzmann, Einstein, and Planck. The relations between these have been discussed in detail elsewhere (13a,b).

As should be evident, there is no possibility of finding the correct relations for irreversible processes unless one understands clearly the distinctions in meaning and the different properties of $S_{E}, S_{I}$, $S(A), S_{B}, S_{G}$, and $S_{B E P}$. We can hardly expect that the variational principle we seek can hold for all of them. While the properties of $S_{I}$
and $S(A)$ are mathematical theorems, those of $S_{E}$ are summaries of experimental facts.

For a closed system, Clausius defined $S_{E}$ by the integral of $d Q / T$ over a reversible path and stated that, in an adiabatic process from an initial equilibrium state ( $T_{1}, V_{1}$ ) to a final one ( $T_{2}, V_{2}$ ),

$$
\begin{equation*}
S_{E}(2) \geqslant S_{E}(1) \tag{3.}
\end{equation*}
$$

with equality if and only if the process is reversible. Of all the statements of the second law made by Clausius and Planck, only Eq. 3 meets our requirements of logical precision; given certain provisos that we have stressed before (13), its truth or falsity can be determined in the laboratory to an accuracy limited only by the accuracy of our measurements, and not by the accuracy of definition of the terms in the equation. But in applications it tells us only in what general direction a change of state will go-not how far, how fast, or along what path.

Gibbs (2) generalized this to open systems and showed that a stronger statement is more useful in practice, telling us precisely "how far" and thus leading to quantitative predictions of the final equilibrium state reached. Let us call Eq. 3 the Clausius weak form of the second law, and append to it the Gibbs strong form: $S_{E}$ not only "tends" to increase; it will increase, to the maximum value permitted by the constraints imposed. The exact constraints for which this is asserted (essentially the conservation laws) involve some standard technical discussion.

In the strong form we see entropy rising above its obscure beginnings and, so to speak, "presiding over" all of thermostatics; i.e. it determines, by its variational properties $\delta S=0$, the set of all possible equilibrium states. In a similar way, the Lagrangian $L$ presides over all of mechanics and electrodynamics, determining by its variational properties $\delta \int L d t=0$ all the equations of motion, in any coordinate system.

We seek a generalization of entropy with properties more like a Lagrangian, which can by its variational properties generate our "equations of motion," telling us how fast, and along what path, an irreversible process will take place. The first general attack on this problem was made by Onsager (14a, b), whose work we now survey.

## ONSAGER'S THEORY

Irreversible thermodynamics had its historical origins in Thomson's analysis of the thermocouple in 1854. For the effect of transporting a charge $q$ around the circuit, he assumed that one might apply Carnot's principle in the form $\Sigma Q_{i} / T_{i}=0$ to the reversible Peltier and Thomson heat effects even though irreversible heat conduction was also present.

Indeed, unless something like this were true, there would be few real applications in which one could ever apply Carnot engine arguments with any confidence. His assumption went beyond the principles of thermostatics and yielded, for the interaction of heat flow and electric current, the first example of an "Onsager reciprocal relation."

By 1931 many such relations had been noted, and Onsager (14) sought a general theoretical justification for them. His argument is still worth recalling because the formal relations survive, generalized and reinterpreted, in our present theory. We summarize it briefly, noting the four "serious" assumptions by Roman numerals and limiting comments to the square brackets.

A closed system is characterized by certain parameters $\left\{a_{1} \ldots a_{n}\right\}$, so defined that they vanish in the equilibrium state of maximum entropy. Then in a neighborhood of equilibrium we may expand:

$$
\begin{equation*}
S=S_{0}-(1 / 2) \sum G_{i j} a_{i} a_{j}+\ldots \tag{4.}
\end{equation*}
$$

where $G$ is a positive definite, symmetric matrix, $G=G^{T}$. The system is displaced from equilibrium by means unspecified, then released to find its way back to equilibrium. The derivatives

$$
\begin{equation*}
X_{i} \equiv \partial S / \partial a_{i}=-\Sigma G_{i j} a_{j} \tag{5.}
\end{equation*}
$$

are thought of as the "forces" which drive the system back according to

$$
\begin{equation*}
\text { I. } \quad \dot{a}_{i}=\sum_{j} L_{i j} X_{j} \tag{6.}
\end{equation*}
$$

where the $L_{i j}$ are the "Onsager phenomenological coefficients." Thus the $a$ 's relax to zero along a trajectory given in matrix notation by $\dot{a}=-L G a$, or

$$
\begin{equation*}
a(t+\tau)=\exp (-L G \tau) a(t), \quad \tau>0 . \tag{7.}
\end{equation*}
$$

Now we turn to situations very close to equilibrium and examine the small thermal fluctuations in the $a$ 's (which were neglected above). We postulate that the same entropy function $S\left(a_{i}\right)$ that supplied the forces $X_{i}$ is also to supply the probability distribution of these fluctuations, i.e. the equilibrium distribution of the $a$ 's at equal times is given by a density function

$$
\begin{equation*}
\text { II. } \quad f\left(a_{1} \ldots a_{n}\right) \propto \exp \left[k^{-1} S\left(a_{i}\right)\right] \tag{8.}
\end{equation*}
$$

where $k$ is Boltzmann's constant [at this point it appears that Onsager's entropy is most closely related to the $S_{B E P}$ noted above]. Denoting averages over this distribution by angular brackets, we have $\left\langle a_{i}\right\rangle=0$, while the matrix of second moments, $K_{i j} \equiv\left\langle a_{i} a_{j}\right\rangle$ is essentially the inverse of $G: K G=G K=k I$, where $I$ is the unit matrix; $K_{i j}$ is a
covariance indicating how far, but not how rapidly, the $a_{i}$ may be expected to fluctuate about zero.

We now make an assumption about this: that the average regression of these spontaneous fluctuations follows the same law, Eq. 7, as that assumed for forced deviations from equilibrium. That is, given the event $a(t)$, the conditional average of $a(t+\tau)$ at a later time, over many repetitions of the event, shall be
III. $\quad\langle a(t+\tau)\rangle=\exp (-L G \tau) a(t), \quad \tau>0$.
[This step is characteristic of the logic of stochastic theories; instead of asking what the microscopic equations of motion have to say about the matter, one simply ignores them and introduces intuitive "stochastic assumptions" at the macroscopic level.]

With this assumption we can define a time-dependent covariance matrix:

$$
\begin{equation*}
K_{i j}(\tau) \equiv\left\langle\left\langle a_{i}(t+\tau) a_{j}(t)\right\rangle\right\rangle \tag{10.}
\end{equation*}
$$

in which the double average is over the different motions averaged in Eq. 9, and then over the distribution, Eq. 8. Inserting Eq. 9 into Eq. 10, this means that the covariance matrix must also decay according to the macroscopic law, Eq. 7:

$$
\begin{equation*}
K(\tau)=\exp (-L G \tau) K(0)=K(0) \exp (-G L \tau), \quad \tau>0 \tag{11.}
\end{equation*}
$$

where $K(0)=k G^{-1}$ is the same matrix that we denoted by $K$ above, and we used an identity of any matrix function: $f(L G) G^{-1}=G^{-1} f(G L)$. $K(\tau)$ as defined by Eq. 10 is independent of $t ; K(-\tau)=K^{T}(\tau)$; or from Eq. 11,

$$
\begin{equation*}
K(-\tau)=K(0) \exp \left(-G L^{T} \tau\right), \quad \tau>0 \tag{12.}
\end{equation*}
$$

since the transposed matrix function is $f^{T}(L G)=f\left(G^{T} L^{T}\right)=f\left(G L^{T}\right)$.
Finally, we invoke the famous assumption that Onsager called "microscopic reversibility":

$$
\begin{equation*}
\text { IV. } \quad K(-\tau)=K(\tau) \tag{13.}
\end{equation*}
$$

Comparing Eq. 11 and 12 we have the grand result

$$
\begin{equation*}
L=L^{T} \tag{14.}
\end{equation*}
$$

Onsager's argument showed a remarkable instinct for sensing the right formal relations, which have stood the test of fifty years. But he chose a thorny path to them, ignoring the smooth path made by his predecessor at Yale. The relation he needed was Eq. 11; given that, the rest of the derivation is a two-line triviality. But to reach it he (a) assumed a phenomenological form that was (I $a$ ) linear, (I $b$ ) without
memory; (b) assumed that the average regression of fluctuations follows that same phenomenological law; ( $c$ ) from these deduced Eq. 11: the covariance function $K(t)$ also follows that phenomenological law.

But had he taken the path of a Gibbsian statistical theory instead of a stochastic one, this result-including space dependences and all memory effects-would have been present from the start with no need to assume any phenomenological form or to mention regression of fluctuations at all. For in such a theory, the predicted space-time dependence of any macroscopic process is given by a covariance function $K\left(x, t ; x^{\prime}, t^{\prime}\right)$.

For example, in acoustics the sound pressure $\delta P(x, t)$ due to a source distribution $s\left(x^{\prime}, t^{\prime}\right) \mathrm{sec}^{-1}$ (i.e. $\mathrm{cm}^{3} \mathrm{sec}^{-1}$ per $\mathrm{cm}^{3}$ ) is given by a linear superposition

$$
\begin{equation*}
\delta P(x, t)=\int d^{3} x^{\prime} \int_{-\infty}^{t} d t^{\prime} G\left(x, t ; x^{\prime}, t^{\prime}\right) s\left(x^{\prime}, t^{\prime}\right) \tag{15.}
\end{equation*}
$$

At thermal equilibrium, Gibbsian statistical theory gives for the Green's function

$$
\begin{equation*}
G\left(x, t ; x^{\prime}, t^{\prime}\right)=(1 / k T)\left\langle\delta P(x, t) \delta P\left(x^{\prime}, t^{\prime}\right)\right\rangle, \tag{16.}
\end{equation*}
$$

i.e. just $(k T)^{-1}$ times the covariance of the thermal pressure fluctuations. This linear response kernel contains all memory effects, including propagation time delays, reflection from walls, "ringing" due to multiple scatterers and resonators, ultrasonic dispersion and attenuation due to relaxation in the medium, etc. Its obvious symmetry is just the Helm-holtz-Rayleigh reciprocity theorem.

Onsager's viewpoint fits in nicely with our conjectured reorientation. If, as stated by Eq. 5, the force driving the system back to equilibrium is the entropy gradient, then instead of minimizing entropy production, the system is maximizing it, trying to get to equilibrium as rapidly as it can, subject to whatever restraints are preventing this. But looking at the relations in this way suggests an additional conjecture.

It appears to us that Onsager might have obtained more useful results by making a different assumption, which seems no stronger than Eq. 13. Since $G$ is real and symmetric, it can be diagonalized by an orthogonal matrix $O$. In the coordinate system of the new variables $a_{k}^{\prime}=\sum_{i} O_{k i} a_{i}$, the matrix $G^{\prime}=O G O^{-1}$ is diagonal, and so the force $X_{k}^{\prime}$ is merely a numerical multiple of $a_{k}^{\prime}$. The $a_{k}^{\prime}$ are uncorrelated at equal times and the entropy function $S=\sum S\left(a_{k}^{\prime}\right)$ is the same as if we had $n$ separate, noninteracting systems. So it seems plausible that in the absence of magnetic or Coriolis forces the $a_{k}^{\prime}$ should relax independently; in other words, that the new phenomenological matrix $L^{\prime}=O L O^{-1}$ should also be diagonal. If so, then $L$ and $G$ must commute in the original coordinate system $\left[a_{i}\right]$.

But $L G=G L$ is a stronger condition than the Onsager symmetries $L=L^{T}$. For example, with $n=3$ fluxes, the Onsager relations reduce the number of independent phenomenological coefficients from $n^{2}=9$ to $n(n+1) / 2=6$. The condition $L G=G L$ yields these and three additional relations, leaving only $n=3$ independent coefficients. If the matrix $G$ were known from equilibrium measurements, one would then need only three nonequilibrium measurements: for example the self-conductances $L_{11}, L_{22}, L_{33}$; whereupon all six coupling coefficients $L_{i j}, i \neq j$, would be determined. In the case $n=2$, the coupling coefficients would reduce to $L_{12}=L_{21}=G_{12}\left(L_{11}-L_{22}\right) /\left(G_{11}-G_{22}\right)$.

We point this out in the hope that some readers may be in possession of enough experimental data to check the relation $L G=G L$. If this conjecture should be confirmed, irreversible thermodynamics would become more useful, since one could predict considerably more about irreversible processes from equilibrium data.

## INTERLUDE

In the 1940s and 1950s some attempts were made to generalize Onsager's treatment to a macroscopic continuum theory based on the notions of local equilibrium and local rate of entropy production. In 1962 this approach was summarized in the book of de Groot \& Mazur (9), where references to the vast literature it generated can be found.

This approach postulates the existence of a local entropy density $s(x, t)$ which plays the role of a field variable. It is to have also a flow rate $J_{s}$ and source strength $\sigma(x, t) \geqslant 0$, so as to obey the field equation $\dot{s}+\nabla \cdot J_{s}=\sigma(x, t)$. Entropy is thus conceived of as a kind of fluid which, once created, is conserved forever after.

Mathematically, the notion of entropy can be generalized to nonequilibrium conditions in many different ways. Basically, the issue is not which is "correct," but which ones have demonstrable and useful physical properties. We agree that a useful theory should be set up as a continuum field theory; but if we allow entropy to degrade into no more than one of many field variables, we shall lose just those properties that made entropy uniquely useful in the work of Gibbs and Onsager.

Therefore we shall seek, rather, to elevate entropy to a functional $S\left[A_{1}(x, t) \ldots A_{n}(x, t)\right]$ over the thermokinetic history of the field variables so that it can retain those properties, while acquiring a new generating power like a Lagrangian; only thus do we see the possibility of reaching our goal.

In any event, de Groot \& Mazur use, without defining, a local entropy density in an inhomogeneous nonequilibrium state. In addition they suppose that the equilibrium expressions for temperature and
chemical potentials can be used as local field variables, obeying the Gibbs equilibrium relation $T d S=d U+P d V-\sum \mu_{i} d n_{i}$ even when gradients and irreversible fluxes are present.

Now one expects that procedures of this kind should, like Thomson's, meet with some success very close to equilibrium; and of course de Groot and Mazur did not claim any more than this. But a "local equilibrium" approach has no criterion for judging its range of validity and provides no basis for further development, since it contains scarcely any quantity that has a precise meaning in a nonequilibrium state.

This approach, therefore, reached a dead end. The logic of using equilibrium relations in nonequilibrium situations was hardly an advance over that used by Thomson in 1854; indeed, we are unable to see wherein they differ at all. To make further progress beyond this point, it was necessary to go back to first principles and reason things out all over again, much more carefully, The coup de grace and final benedictions were administered by Wei (15) and Truesdell (16).

## RESURRECTION

In 1967, Tykodi (17) showed how entropy production theories might be not only salvaged, but made in a sense exact, using logic so simple and direct that one could not question any part of it without at the same time questioning a considerable part of established equilibrium theory. He simply abandoned altogether the notions of local equilibrium and local entropy production, and reasoned as follows.

There is one case where logically impeccable inferences about an irreversible process were drawn from the relations of equilibrium theory: the Joule-Thomson porous plug experiment of 1852. The inflowing gas is at thermal equilibrium with temperature and pressure ( $T_{1}, P_{1}$ ), and we measure the outflowing gas far enough downstream from the plug so that it has come back to thermal equilibrium, with new values $\left(T_{2}, P_{2}\right)$. By a simple argument given in all the textbooks we are persuaded at once that, however violent the irreversible process taking place in the plug (it might, for example, involve locally supersonic velocities, shock waves, chemical reactions catalyzed by the plug, etc), if the plug cannot communicate directly with the outside world, so it does no work and all the heat generated must be carried off by the effluent gas, then when a steady state is reached, the (enthalpy + kinetic energy of mass flow) of the incoming and outgoing gases must be the same.

In other words, established equilibrium theory does enable us to draw rigorous inferences about steady irreversible processes that begin and end in states of complete thermal equilibrium. This is just the conclu-
sion we noted already in Eq. 3, and which had been stressed in the writer's pedagogical article (13). But as soon as we recognize this the road is straight and we can see for miles, for the Joule-Thomson example can be generalized endlessly.

In the first place, the barrier need not be a simple "plug." It may contain apparatus of any complexity, and even if conditions in it never come to a steady state, but go into limit-cycle oscillations, if the apparatus contains suitable "mufflers" so that there is eventually uniform inflow and outflow, the conclusion still holds.

Furthermore, nothing restricts us to a system with only two channels, one for inflow and one for outflow. We can have any number of inflow channels, containing different chemical substances, or mixtures of them, at different pressures and temperatures, flowing at different rates; and any number of similar outflow channels. And nothing restricts us to gases; a channel could transport liquid, solids, plasma, electrons, radiation, etc. There need not be a single reaction region; the plumbing might be arranged to carry any number of substances to any number of reaction vessels in any sequence. In short, we may imagine an arbitrary continuous-flow processing plant.

For any such arrangement we can define an energy flux $H_{i}^{\prime}=$ (enthalpy + kinetic energy of mass flow) transported from the reaction region per unit time or per oscillation cycle in the $i$ th channel, and similar entropy flux $S_{i}$. The reaction region may communicate directly with the outside world, doing work $W$ per unit time or per oscillation cycle. Under these conditions the energy balance requirement gives rigorously $\sum H_{i}^{\prime}+W=0$, while at the same time the total rate of entropy production $\sum S_{i}$ is now unambiguously defined by equilibrium theory.

Only at this point is one in a position to discuss entropy production principles in a meaningful way. All ambiguities about the definition of temperature and entropy in a nonequilibrium state have been eliminated, since however such notions may or may not be defined eventually, at least in a steady state they are not changing. And we are not limited to near-equilibrium regimes with linear phenomenological laws; nor have we neglected fading memory effects.

If $J_{i}$ is the flux in the $i$ th channel in moles (grams) per second, then the rate of entropy production is

$$
\begin{equation*}
\dot{S}_{E}=k \sum_{i} \lambda_{i} J_{i} \tag{17.}
\end{equation*}
$$

where $k \lambda_{i}$ is the entropy per mole (gram) of the $i$ th substance. If it is a pure chemical substance, then $\lambda_{i}=-\mu_{i} / k T$ is essentially the chemical potential. The quantities $\lambda_{i}$, which we call simply the "potentials," are, however, the fundamental quantities of our theory.

Although Eq. 17 looks at first glance like the Onsager expression $\dot{S}=\sum X_{i} J_{i}$, it has a different meaning. In the first place, Eq. 17 is not a quadratic approximation holding near equilibrium; it is the exact rate of entropy production for any departure from equilibrium. Secondly, there are more terms in Eq. 17 and they are not independent. If particles of type $k$ enter via channel 3 and emerge unchanged but for pressure and temperature in channel 7, in Eq. 17 this contributes two terms $k\left(\lambda_{3} J_{3}+\right. \lambda_{7} J_{7}$ ), constrained by the conservation law $J_{3}+J_{7}=0$, but only one $X_{k} J_{k}$ in the Onsager form. Where Onsager took his forces as derivatives, $X_{k}=\partial S / \partial a_{k}$, we see that the exact "force" should be $X_{k}^{\prime}=k\left(\lambda_{7}-\lambda_{3}\right)$, a finite difference of potentials.

If we eliminate fluxes determined by the conservation laws and rewrite Eq. 17 in terms of independently variable fluxes we obtain the Onsager form $\dot{S}_{E}=\sum X_{k}^{\prime} J_{k}$. In these terms, Tykodi states a minimum entropy production principle that, close to equilibrium, is equivalent to the Onsager relations. He conjectures that this principle (varying $X_{m}$ while holding the other forces constant, minimum $\dot{S}$ occurs at $J_{m}=0$ ) should hold also far from equilibrium. It would be interesting to have experimental data which could check this.

Of course, other conjectures may be made. If we restate the phenomenology in differential form, $d J_{k}=\sum_{j} L_{k j}^{\prime} d X_{j}$, then the symmetries $L_{k j}^{\prime}= L_{j k}^{\prime}$ will hold in the nonlinear regime if and only if there exists a function $f\left(X_{1} \ldots X_{m}\right)$ such that $J_{k}=\partial f / \partial X_{k}$. Because it appears that this form may be obtained from a Gibbsian statistical theory, experiments to check the symmetry of $L_{k j}^{\prime}$ far from equilibrium would be of great interest.

In summary, progress to this point consists of some conjectured principles that, thanks to Tykodi, can at least be stated in precise and experimentally meaningful terms so that their correctness or incorrectness can be determined in the laboratory. But we set for ourselves a more ambitious goal than this.

Since the methods of analysis reviewed above were not powerful enough to guide us to the missing theoretical principle, we are driven finally to recognize what should have been obvious from the start. Only the Gibbs standards of logical reasoning were powerful enough to give us the first variational principle, on which physical chemistry has been feeding for a century; and only a Gibbsian statistical analysis is powerful enough to extend that principle to irreversible processes. But in recent years the field that is now called "statistical mechanics," with its reversion to kinetic theory, stochastic equations, and ergodicity, has deviated so widely from the program for which Gibbs introduced that term, that we need to coin a new name for Gibbs' program if we are not
to propagate still more semantic confusion. We now explain briefly an extension of Gibbs' work currently underway, set apart by a new descriptive word.

## PREDICTIVE STATISTICAL MECHANICS

Predictive statistical mechanics is not a physical theory, but a form of statistical inference. As such, it is equally applicable in other fields than physics (e.g. engineering, econometrics, etc). In fact, it is having its greatest current success in the new techniques for image reconstruction in optics and radio astronomy (18a, b). We emphasize the sharp distinction in purpose and content between these two methods of reasoning.

A physical theory asks bluntly, "How does the system behave?" and seeks to answer it by deductive reasoning from the known laws of physics. But, for example, the Onsager reciprocal relations cannot be proved by deductive logic from the equations of motion (they are not true for every possible initial state). Therefore, to obtain them in the manner of a physical theory requires that one make extra physical assumptions of an "ergodic" or "stochastic" nature, beyond what is contained in the equations of motion.

Predictive statistical mechanics, instead of seeking the unattainable, asks a more modest question: "Given the partial information that we do, in fact, have, what are the best predictions we can make of observable phenomena?" It does not claim deductive certainty for its predictions, but to ensure the "objectivity" of the predictions we do make, it explicitly forbids the use of extraneous assumptions beyond the data at hand. The formal device which accomplishes this is that we shall draw inferences only from that probability distribution whose sample space represents what is known about the structure of microstates, and that maximizes $S_{I}$ subject to the macroscopic data.

By this device, the probability is distributed as uniformly as possible over the class C of microstates compatible with our information. Therefore, we shall make sharp predictions only of those phenomena which are characteristic of each of the vast majority of the states in C. But those are just the reproducible phenomena which a physical theory had sought to predict.

Our aim is not to "explain irreversibility," but to describe and predict the observable facts. If one succeeds in doing this correctly from first principles, he will find that philosophical questions about the "nature of irreversibility" will either have been answered automatically, or else will be seen as ill-considered and irrelevant.

The background and technical details of this approach have been explained in another recent review article (19). We recall here only what is needed for the immediate purpose.

On the space $\Gamma$ of all possible microstates there is defined a measure $d \Gamma$ which may be classical phase volume: $d \Gamma=d q_{1} \ldots d p_{N}$, or some appropriate generalization of this for quantum theory or any other microscopic theory that we might consider. Choosing some set of macroscopic variables $\left\{A_{1} \ldots A_{n}, n \lll N\right\}$, the set of their possible values defines a macrospace $\Omega$. The mapping of $\Gamma$ onto $\Omega$ defines a measure on $\Omega$ by projection:

$$
\begin{equation*}
d \Omega=W\left(A_{1} \ldots A_{n}\right) d A_{1} \ldots d A_{n}=\int_{R} d \Gamma \tag{18.}
\end{equation*}
$$

where the region $R$ of integration is all microstates for which $A_{i}$ is in $d A_{i}, 1 \leqslant i \leqslant n$.

Microscopic properties are relevant to macroscopic predictions only to the extent that certain aspects of the microstates "leak through" and appear at the macroscopic level. Most evident are the conservation laws for mass, energy, and momentum, which made it possible to discover the principles of mechanics at the macroscopic level long before they were recognized as equally valid microscopically, leading to the first law. Next in importance is the above measure $W$; through this the fantastically great variations in number of microscopic possibilities of realization manifest themselves at the macroscopic level, as the second law. At sufficiently low energies, $\log W$ becomes essentially independent of other parameters, leading to the third law.

These are the only microscopic properties involved in conventional equilibrium thermodynamics; the content of Gibbs' variational principle is that, given the measure $W$ as a function of certain macroscopic quantities (energy, volume, mole numbers, etc) the equilibrium properties of a system are determined. As a procedure for inference, his principle amounts to this: We shall predict that behavior that can happen in the greatest number of ways, consistent with our data.

Predictive statistical mechanics seeks to do no more than this, but only to do it more generally. All its mathematical formalism is nothing but a kind of bookkeeping system by which we may "count the number of ways" in which various conceivable events can happen, consistent with whatever macroscopic data we may have. If our data are of the kind considered by Gibbs (constant in time, piecewise homogeneous in space), then our principle will reduce to his. It is more general in that we must be prepared to deal, both in the information used and in the
predictions made, with arbitrary space-time dependences. Mathematically, this means that the functions of Gibbs are promoted to functionals.

Any probability distribution $w\left(q_{1} \ldots p_{N}\right)$ over microstates defines a macroscopic distribution $P\left(A_{1} \ldots A_{n}\right)$ on $\Omega$ by $w d \Gamma=P d A$. Its information entropy is then

$$
\begin{equation*}
S_{I}=-\int w \log w d \Gamma=-\int d A P(A) \log [P(A) / W(A)] \tag{19.}
\end{equation*}
$$

and so, given the measure $W(A)$, we may carry out the maximization in either space.

Direct evaluation of $W$ would be very difficult; much more manageable and equally informative is its $n$-fold Laplace transform, called the partition function:

$$
\begin{equation*}
Z\left(\lambda_{1} \ldots \lambda_{n}\right)=\int_{\Omega} W e^{-\lambda \cdot A} d A=\int_{\Gamma} e^{-\lambda \cdot A} d \Gamma \tag{20.}
\end{equation*}
$$

where we used the abbreviations $d A=d A_{1} \ldots d A_{n}, \lambda \cdot A=\Sigma_{i} \lambda_{i} A_{i}$. When the integral converges, it is because the rapidly increasing factor $W$ is overpowered by an even more rapidly decreasing factor $\exp (-\lambda \cdot A)$, so that the integrand $W \exp (-\lambda \cdot A)$ has an enormously sharp peak at some point $\left\{\hat{A}_{i}\right\}$. Most of the contribution to the integral then comes from the immediate neighborhood of this peak.

Now the probability density $P(A)$ which maximizes $S_{I}$ subject to prescribed mean values $\left\langle A_{i}\right\rangle$ is just the canonical distribution $P(A)= Z^{-1} W(A) \exp (-\lambda \cdot A)$, of which Gibbs gave several examples. The peak of this density in the macrospace $\Omega$ is so sharp that for all practical purposes the mode $\hat{A}_{i}$ and mean $\left\langle A_{i}\right\rangle$ are the same. Therefore we need only choose the $\left\{\lambda_{i}\right\}$ so as to place that peak at the experimentally observed values $\left\{A_{1}^{\prime} \ldots A_{n}^{\prime}\right\}$. The simplest way of doing this is to note that the first moments of $P(A)$ are given by

$$
\begin{equation*}
\left\langle A_{i}\right\rangle=-\partial \log Z / \partial \lambda_{i}, \quad 1 \leqslant i \leqslant n \tag{21.}
\end{equation*}
$$

so setting these equal to the experimental values $\left\langle A_{i}\right\rangle=A_{i}^{\prime}$, gives $n$ simultaneous equations for the $n$ unknowns $\lambda_{i}$.

In fact, all moments of $P(A)$ are determined by derivatives of $\log Z$; differentiating Eq. 21 with respect to $\lambda_{j}$, we find a combined reciprocitycovariance law:

$$
\begin{equation*}
\left\langle A_{i} A_{j}\right\rangle-\left\langle A_{i}\right\rangle\left\langle A_{j}\right\rangle=-\partial\left\langle A_{i}\right\rangle / \partial \lambda_{j}=-\partial\left\langle A_{j}\right\rangle / \partial \lambda_{i} \tag{22.}
\end{equation*}
$$

and we suspect already that reciprocal relations are going to appear rather trivial in this theory.

Note that these relations are perfectly general, whatever microscopic theory we imagine as underlying the macroscopic one. This is a point that was stressed by Einstein many years ago, and it is the reason that he was able to move so confidently in the transition from classical to quantum theory. He knew that Eq. 22 was trustworthy whatever our microscopic theory; as long as conservation of mass and energy were not being called into question, the only thing that could change was the underlying measure: $W_{\text {class }} \rightarrow W_{\text {quantum }}$. So he applied Eq. 22 to determine the energy fluctuations ( $\Delta E)^{2}$ of black-body radiation from the empirical Planck law $\partial\langle E\rangle / \partial T$, noted a term identical with the fluctuations of an ideal gas, and inferred the existence of photons.

Having noted this generality, we may equally well use the notation of quantum theory; the $A_{i}$ are then operators, the canonical density matrix $\rho=Z^{-1} \exp (-\lambda \cdot A)$ maximizes $S_{I}=-\operatorname{Tr}(\rho \log \rho)$ subject to given values of $A_{i}^{\prime}=\left\langle A_{i}\right\rangle=\operatorname{Tr}\left(\rho A_{i}\right)$, where the partition function is $Z(\lambda)=\operatorname{Tr} \exp (-\lambda \cdot A)$.

For a system of macroscopic size the measure $\log W\left(A_{i}^{\prime}\right)$ is $(13,19)$ essentially the maximum of $S_{I}$ thus attained: $\left(S_{I}\right)_{\text {max }}=S\left(A_{1}^{\prime} \ldots A_{n}^{\prime}\right) =\log Z+\lambda \cdot A^{\prime}$. For all purposes that could be relevant experimentally, $S\left(A^{\prime}\right)$ may be taken as the logarithm of the number of microstates compatible with the macroscopic data $A_{i}^{\prime}$. If this function is known, then the $\lambda$ 's (which arose as Lagrange multipliers in the maximization of $S_{I}$ ) are given simply by $\lambda_{i}=\partial S / \partial A_{i}^{\prime}$. They are, therefore, just the "potentials" appearing in Tykodi's entropy production rate, Eq. 17.

The potential $\lambda_{i}$ thus measures the rate at which the number of microscopic possibilities would change if $A_{i}^{\prime}$ were slightly different. According to Onsager's interpretation, Eq. 5, the "statistical force" that drives a system back to equilibrium is essentially a change in $\lambda$, given near equilibrium by the matrix $G$ of second derivatives of $S\left(A^{\prime}\right)$. Tykodi's Eq. 17 suggests that this may be, in fact, exact.

All the formal properties noted above-although perhaps not the interpretation we have just made-have been well known for many years; if the $A_{i}$ are energy and mole numbers, $P(A)$ reduces to the grand canonical ensemble of Gibbs. Predictive statistical mechanics applies this same formalism, with more general choices of the $A_{i}$ than Gibbs made. Two different stages of generalization, and therefore two different generalized entropies $S\left(A^{\prime}\right)$, are useful in present applications.

The quantity $A_{i}$ might be observed at different positions $A_{i}\left(x_{j}\right)$; for each such datum there would be a Lagrange multiplier $\lambda_{i j}$. In the limit as the points $x_{j}$ become dense, the scalar product $\lambda \cdot A$ then goes into $\lambda \cdot A \rightarrow \Sigma_{i} \int \lambda_{i}(x) A_{i}(x) d^{3} x$. If all this pertains to one time $t$, we indicate this by a subscript $t$ : the partition function and entropy then become functionals $Z_{t}=Z_{t}\left[\lambda_{i}(x)\right], S_{t}=S_{t}\left[A_{i}^{\prime}(x)\right]$.

The density matrix $\rho_{t}=Z_{t}^{-1} \exp (-\lambda \cdot A)$ is then, for certain choices of the $A \mathrm{~s}$, formally identical with what has been called a "local equilibrium" density matrix, but its meaning is here entirely different; in particular, it has nothing to do with equilibrium. $\rho_{t}$ represents information about the space distribution of the fields at one instant of time, and no other information whatsoever, because it has maximum $S_{I}$ subject to that constraint. The functional $S_{t}$ measures the number of microstates compatible with that information, and it generates the potential fields $\lambda_{i}(x)$ by what has now become functional differentiation: $\lambda_{i}(x)=\delta S_{t} / \delta A_{i}^{\prime}(x)$.

Note that $S_{t}$ measures the total number of all microstates compatible with the macrostate $A_{i}^{\prime}(x)$ at time $t$, regardless of the thermokinetic history by which the system came into that state. Thus it contains, with various relative weightings, a kind of mixture of every conceivable history. It is obvious, then, that in general $\rho_{t}$ cannot contain enough information to predict other quantities $B$, or the future evolution of the system; for the characteristic feature of irreversible processes is the appearance of fading memory effects, and in $\rho_{t}$ all memory of the past has been thrown away. This is the logical defect that makes any "local equilibrium" approach inadequate.

In 1964, Robertson (20) showed how, in spite of this, one can make predictions of later irreversible behavior from $\rho_{t}$ by adding corrective memory terms that accumulate as one integrates the equations of motion forward in time from $t$. This work developed and applied the continued fraction expansion, later given by Mori. If the important relaxation times are short compared to the time over which one can trust second-order perturbation theory, then one reaches a "plateau" at which transport coefficients may be calculated, as was indeed shown by Green and Kubo in the 1950s. Robertson's recent review (21) gives an extensive list of the many works to 1978 based on this approach.

But there is a more elegant and general way of incorporating memory effects into this theory. Let the $A_{i}(x)$ now become time-dependent operators in the Heisenberg representation, and suppose we add information about their values at various times $t_{j}$. Each of these will now acquire its Lagrange multiplier $\lambda_{i j}(x)$, and again in the limit of dense $t_{j}$ we have an integral over time. The dot product now goes into

$$
\begin{equation*}
\lambda \cdot A \rightarrow \Sigma_{i} \int_{R_{i}} d^{3} x d t \lambda_{i}(x, t) A_{i}(x, t) \tag{23.}
\end{equation*}
$$

in which $R_{i}$ is the space-time region in which we have information about $A_{i}^{\prime}(x, t)$. The new entropy functional $S\left[A_{i}^{\prime}(x, t)\right]$ is over all the known thermokinetic history of the system, and it measures the number of microstates consistent with that specific history.

Analogous to the world-lines of relativity theory, the evolution of a microstate may be visualized as a world-line in "phase space-time," and $S$ is the cross-section of a tube formed of all world-lines by which the given history could have been realized. Let us then call $S$ for any particular history the caliber of that history.

We have indicated recently (19) some of the technical details and results of this space-time theory, and applications to hydrodynamics are given by Grandy (22). If the specified history $\left\{A_{i}^{\prime}(x, t), x, t\right.$ in $\left.R_{i}\right\}$ includes all that is relevant in the laboratory for determining reproducible behavior, then the new ensemble based on Eq. 23 automatically includes all memory effects; the plateau phenomenon is eliminated and one now obtains transport coefficients by direct quadratures over the initial ensemble; they are the full "renormalized" ones.

The theory is freed from previous limitations to the quasi-stationary, long-wavelength case; when all memory effects are included, there is no longer any limitation on time scale or space scale. Thus, as shown in (19), a single equation for the predicted space-time dependence of particle density encompasses both static diffusion and ultrasonic dispersion and attenuation.

An important addition to the technique of applying this theory was added in 1967 by Mitchell (23) in his theory of macroscopic sources, which was identical in philosophy with Schwinger's source theory for quantum fields. From Mitchell's viewpoint, the acoustic Green's function formula Eq. 16 appears as an obvious triviality. He went on to some elegant theorems showing how variational properties of the caliber $S$ of a process determine the conditions for migrational equilibrium in nonequilibrium states, and reciprocity-response theorems about the effect of imposing a new constraint, by which any "renormalization" effects may be analyzed. In the course of this, he formulated what is now called "mode-mode coupling theory." We hope to present elsewhere a detailed account of the kind of results that may be obtained by Mitchell's methods.

The caliber $S$ of a space-time history determines by its variational properties most of the relevant physical information one would like to have. Its first variations determine the conditions of migrational equilibrium, while its second variations generate the "equations of motion." To see why this is so, suppose we have information $I_{A}$ from one space-time region $R_{A}$, which determines a caliber $S_{A}$; and we wish to predict-or retrodict-events in some other region $R_{B}$. Now we could imagine that someone had given to us a conjectured answer $I_{B}$ to this, so that we had the total information $I=I_{A}+I_{B}$. What would be the caliber $S$ of the combined process? Since $S$ is the result of maximization
subject to a further constraint $I_{B}$, we shall have $S \leqslant S_{A}$ with equality if and only if the new information is redundant; i.e. if it is what the theory would have predicted from the old information $I_{A}$. Thus the theory always predicts those events in $R_{B}$ for which the total thermokinetic process will have maximum caliber-an obvious generalization of Gibbs' variational principle.
Although the principle itself evidently holds far from equilibrium, the explicit form of the equations of motion is easily found close to equilibrium where we expect them to be linear. Let $S_{0}$ be the caliber corresponding to thermal equilibrium (it is just $k^{-1} S_{E}$ ); and let $\delta A= \left\{\delta A_{1}^{\prime}(x, t) \ldots \delta A_{n}^{\prime}(x, t)\right\}$ be some small departures from equilibrium conditions in $R_{A}$, while we wish to predict the similar departures $\delta B$ of some quantities $B$ (which may be the same as the $A s$ ) in $R_{B}$. Then the caliber determined by $I_{A}$ will be given by an expansion $S_{A}=S_{0}- (1 / 2) \delta A \cdot G_{A A} \cdot \delta A$, generalizing Onsager's Eq. 4. However, this is compact notation; we remind ourselves that $\delta A \cdot G_{A A} \cdot \delta A$ actually stands for

$$
\begin{equation*}
\sum_{j k} \int_{R_{j}} d^{3} x d t \int_{R_{k}} d^{3} x^{\prime} d t^{\prime} \delta A_{j}^{\prime}(x, t) G_{j k}\left(x, t ; x^{\prime}, t^{\prime}\right) \delta A_{k}^{\prime}\left(x^{\prime}, t^{\prime}\right) \tag{24.}
\end{equation*}
$$

Now if we add a small variation $\delta B$, the caliber acquires more terms: $S=S_{A}-(1 / 2) \delta B \cdot G_{B B} \cdot \delta B-\delta B \cdot G_{B A} \cdot \delta A$, where we have used $G_{A B}=G_{B A}$. For fixed $\delta A$, the caliber is maximum when

$$
\begin{equation*}
G_{B B} \cdot \delta B+G_{B A} \cdot \delta A=0 \tag{25.}
\end{equation*}
$$

which is a set of simultaneous linear integral equations determining the $\delta B$. Had we been given $\delta B$ and predicted $\delta A$, the result would have been $G_{A A} \cdot \delta A+G_{A B} \cdot \delta B=0$, and $G_{A B}=G_{B A}$ implies a mass of reciprocal relations. Thus the $G$ s generated by second variations of $S$ are the kernels of the equations of motion.
$S$ usually possesses a convexity property expressed by the inequality of any two neighboring ensembles: $\delta \lambda \cdot \delta A^{\prime} \leqslant 0$. This is a generalization of the condition given by Gibbs (Reference (2), Eq. 171) from which he deduced all his stability conditions, and leads in the present theory to the positive definite character of $G$. Then $G$ can be inverted, and the inverse kernels $K=G^{-1}$ are the set of space-time covariance functions generalizing Onsager's Eq. 10, of which the acoustic Green's function Eq. 16 is an example. When the convexity fails, the theory predicts bifurcations or other instabilities, a generalization of Gibbs' condition for phase transitions.

## CONCLUSION

As the reader will have sensed, our title is a play on words; logical economy minimizes the principles, not the entropy production. We started by seeking an exact variational property characterizing the nonequilibrium steady state. One such is now apparent, although there may be others more useful. Consider a system evolving according to its equations of motion. Because the caliber $S$ of its history up to time $t$ embodies further constraints beyond those defining the local equilibrium $S_{t}$, we have $S \leqslant S_{t}$, with equality if and only if that history is the one retrodicted from $\rho_{t}$. Now at each instant $t^{\prime}<t$ there is an $S_{t^{\prime} \mid t}$ defined as was $S_{t}$ by maximizing $S_{I}$, but subject to the retrodicted values $A_{i}^{\prime}\left(x, t^{\prime}\right)$. For reasons explained before (13), a retrodicted history could not be reproduced in the laboratory unless $S_{t^{\prime} \mid t} \leqslant S_{t}$; but it is a theorem (invariance of $S_{I}$ under unitary transformations) that $S_{t^{\prime} \mid t} \geqslant S_{t}$.

These inequalities yield the theorem: Of all reproducible histories terminating at a given state, that one which corresponds to constant $S_{t}$ throughout the past has the greatest caliber: $S=S_{t}$. At present it is not known whether this is a pragmatically useful principle in applications; it is, however, of some theoretical importance.

Readers of Truesdell's fresh and fascinating new approach to thermodynamics (16) will resonate at once to this statement. It is a paraphrase of what he calls a "major assertion" in need of proof, from which many other desired results will follow [Reference (16), pp. 22,43]. There is, evidently a close correspondence between these approaches; but to understand it fully and combine them into a single unified theory is a task for the future.

## Acknowledgment

It is a pleasure to thank Professor W. Güttinger, Director, for the hospitality of the Institut für Informationsverarbeitung, Universität Tübingen, where a part of this article was written-and where it finally became possible to unravel the mystery about the historical origin of the word "entropy."

## Literature Cited

1. Kirchhoff, G. D. 1848. Ann. Phys. 75:189
2. Gibbs, J. W. 1876-1878. In The Scientific Papers of J. Willard Gibbs. New York: Longmans, Green, 1906; New York: Dover, 1961
3. Clausius, R. 1865. Memoir read at the Philos. Soc. Zürich, April 24. Pogg. Ann. 125:353
4. Girardeau, M. D., Mazo, R. M. 1973. Adv. Chem. Phys. 24:187-255
5. Helmholtz, H. 1859. Crelle's J. 57:1132
6. Lord Rayleigh. 1877. Theory of Sound. London: Macmillan
7. Lorentz, H. A. 1895. Amsterdam Akad. Wetens. 4:176
8. Prigogine, I. 1961. Thermodynamics of

Irreversible Processes. New York: Interscience
9 . de Groot, S. R., Mazur, P. 1962. NonEquilibrium Thermodynamics. Amsterdam: North-Holland
10. Klein, M. J. 1960. In Rend. Sc. Int. Fis. Enrico Fermi. 10:198-204
11. Prigogine, I., Mayné, F. 1974. In Transport Phenomena, Lecture Notes in Physics, Vol. 31, ed. G. Kirczenow, J. Marro, Berlin: Springer
12. Jaynes, E. T. 1963. In Statistical Physics, ed. K. W. Ford, 3:181-218. New York: Benjamin
13a. Jaynes, E. T. 1965. Am. J. Phys. 33:391-98
13b. Jaynes, E. T. 1971. Phys. Rev. A 4:747-50
14a. Onsager, L. 1931. Phys. Rev. 37:40526
14b. Onsager, L. 1931. Phys. Rev. 38: 2265-79
15. Wei, J. 1966. Ind. Eng. Chem. 58:

55-60
16. Truesdell, C. 1969. Rational Thermodynamics. New York: McGraw-Hill
17. Tykodi, R. J. 1967. Thermodynamics of Steady States. New York: Macmillan
18a. Gull, S. F., Daniell, G. J. 1978. Nature 272:686-90
18b. Frieden, B. R. 1980. In Computer Graphics and Image Processing. In press
19. Jaynes, E. T. 1978. In The Maximum Entropy Formalism ed. R. D. Levine, M. Tribus, pp.15-118. Cambridge: MIT Press
20. Robertson, B. 1964. PhD thesis. Stanford Univ., Calif.
21. Robertson, B. 1978. See Ref. 19, pp. 289-320
22. Grandy, W. T. 1980. Phys. Rep. In press
23. Mitchell, W. C. 1967. PhD thesis. Washington Univ., St. Louis, Mo.

