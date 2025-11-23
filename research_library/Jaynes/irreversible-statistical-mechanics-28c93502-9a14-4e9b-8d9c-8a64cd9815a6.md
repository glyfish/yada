# Irreversible Statistical Mechanics 

E. T. Jaynes

Department of Physies, washington University, St. Louis, Missouri

## D. J. Scalapino

Department of Physica, University of California, Santa Barbara, California


#### Abstract

A general formalism for calculation of irreversible processes, analogous to the paxtition sum algorithe of equilibrium theory, is presented. Mathematically, it is a generalization of the procedure by which Gibbs constructed his amonical and grand canonical ensembles, in which the partition function is witended to a partition functional. Conceptually, it has a simple interprotation in texms of Information Theory. 3y this means, ensembles can be constructed in which macroscopic quantities have sny space-time dependence compatible with the Hamiltonian of the system. We illustrate its use by Saveloping a theory of transport phencmena, in which the following features ewergos (1) Dissipative effects are obtained by direct quadratures over the Naw ensembles, with no need for the forward integration and coarse-graining operations characteristic of previous treatments. In consequence, the theory is not restricted to the quasi-stationary, long-wavelength limit, it applies equally mell to phenwena such as ultrasonic attenuation. (2) The formalism leads to \& nonlocal theory, and to expressions for linear transport coefficients close Iy related to those of Kubo. Ensembles are exhibited in which Kubo's formulas are axact. (3) The statistical analog of the Cauchy initial-value problem is incladed as special case. In linear approximation it is found to be mathematically equivalent to Norbert Wiener's theory of optial prediction of the


future of random function whose past is given. (4) The statistical analog at the Dirichlet-Neumann boundary-value problem, often a more realistic detcription of experimental conditions, is also indluded as a special case. I contains a "statistical Kirchoff-Huygens principle", according to which uso of certain information about the macroscopic state can make other kinds of information redundant for certain predictions. (5) The theory yialds a mathematically ummbiguous rule for calculation of nonlinear effects, such se these due to extremely large temperature or concentration gradients, which nze not easily described in terms of dynmical perturbation on the system.

## 1. INTRODUCTION

In recent years the theory of nonequilibrium statistical mechanics has made great progress in the sense of successful calculation of several particular effects. Many workers have speculated on the possibility that we may eventually learn how to formulate this theory with a generality comparible to that of the partition sum algorithm of equilibrium theory, in which a single formal rule applies to all cases. The basic principles have, however, remained so obscure that one has not seen how to carry out this generalization, and doubt has even been expressed ${ }^{1}$ as to whether such a development is possible. It now appears that the missing formal principle
has long been known, and special cases of it have been used by almost every worker in statistical mechanics; but conceptual difficulties have prevented us from seeing its generality.

The calculation of an irreversible process usually Involves three distinct stages: (1) Setting up an "ensemble," i.e. choosing a density matrix $P(0)$, or an $N$-particle distribution function, which is to describe the initial state of the system of interest; (2) Solving the dynamical problem; i.e. applying the microscopic equations of motion to obtain the time-evolution of the system $\rho(t)$; (3) Extracting the final physical predictions from the time-developed ensemble p(t).

Stage (3) has never presented any procedural difficulty; to prodict the quantity $F$ from the ensemble $P$, one computes the expectation value $\langle p\rangle=\operatorname{Tr}(\rho p)$. While the ultimate justification of this rule has been much discussed (ergodic theory), no alternative procedure has been widely used.

In this connection, we note the following. Suppose we are to choose a number $f$, representing our estimate of the physical quantity $F$, based on the ensemble $P$. A reasonable criterion for the "best" estimate is that the expected square of the error, $\left\langle(F-f)^{2}\right\rangle$ shall be made a minimum. The solution of this simple variational problem is: $f=\langle F\rangle$. Thus if we rogard statistical mechanics as an example of statistical estimation theory based on the mean square error criterion, the usual procedure is uniquely determined as the optimal one, independently of ergodic theory. A justification not
depending on ergodic theory is, of course, necessary as soon as we try to predict time-varying quantities. This point, and the reason for the reliability of the predictions made by the present theory, are discussed further in Appendix A.

The dynamical problem of stage (2) is the most difficult to carry out, but it is also the one in which most recent progress has been booked (Green's function methods). While the present paper is not primarily concerned with these techniques, they are available, and needed, in carrying out the calculations indicated here for all but the simplest problems.

It is curious that stage (1), which must logically precede all the others, has received virtually no attention since the pionearing mank of Gibbs, in which the problem of ensemble construction was first recognized. Most recent discussions of irreversible processes concentrate all attention on stage (2); some fail to note even the existence of stage (1). One consequence of this is that the resulting theories apply unambiguously only to the case of "response functions", in which the nonequilibrium state is one resulting from a dynamical perturbation (i.e., an explicitly given term in the Hamiltonian), starting from thermal equilibrium in the remote past; the initial density matrix is then given by conventional equilibrium theory.

If, however, the nonequilibrium state is defined (as it usually is from the experimental standpoint) in terms of
temperature or concentration gradients, rate of heat flow, shearing stress, sound wave amplitudes, etc., such a procedure does not apply -- at least, not unambiguously. An extreme example is provided by some problems in astrophysics, in which it is clear that the system of interest has never, in the age of the universe, been in a state approximating thermal equilibrium. Such cases, which have been well recognized ${ }^{2}, 3$ as presenting special difficulties of principle, are just the ones in which the problem of stage (1) cannot be evaded,

The main result of the present work is this: recognition of the existence of the stage (1) problem, and that its general solution is available, can remove the aforementioned ambiguties and reduce the labor of stage (2). In the case of the nonequilibrium steady state, stage (2) can be dispensed with entirely if stage (1) has been properly treated.

In the following Section we survey previous methods of transport theory related to our work, and in Sec. 3 the generalization of Gibbs' algorithm is given. The special case of dynamical perturbations is discussed briefly in Sec. 4, while Sec. 5 is a mathematical digression to collect the basic formulas needed for applications. In Sections 6, 7 the general prediction formulas are obtained in linear approximation and the relation to the Wiener prediction theory established. Sections 8, 9, 10 apply the resulting theory to the problems of diffusion, thermal conductivity, and ultrasonic attentuation;
and in the final Sec. 11 nonlinear problems are discussed. A number of points essential for understanding of the theory, but not needed for the actual manipulations, are relegated to Appendices.

## 2. BACKGROUND OF THE PROBLEA

Because of the great diversity of possible nonequilibrium states, a full wieroscopic theory sesms ${ }^{1}$ st first glance hopeiessly complicated; yet from an experimental standpoint irreversible processes are basically simple, in the sense that controlling only a few macroecopic quantities suffices to determine a reproducible outcome. Thus, nost of the microscopic details nust be irreievant for the predicticas of Interest, and with proper understanding we should be able to aliminate them mathematically.

An important clue as to the manner in which one separates relevant and irrelevant details was provided in the work of Kirkwood, ${ }^{4}$ in which diffusion coefficients were shown to depend only on the correlation function of forces acting on particle. Kirkwood's final formulas are very similar to those now believed to be exact, but the mathmatical technique used would be difficult to generalize. Furthermors, it made it appear that a certain time-averaging operation is necensary in order to obtain dissipative effects: but by this process one loses ostain observable high-frequency effects that clearly must be ratuinad in a general theory.

A decisive step in the direction of simplicity and generality was made by Callen and co-workers in a series of articles ${ }^{5-8}$ in which the problem was attacked from both the microscopic and macroscopic standpoints. Generalizing the wellknow theorem by Nyquist ${ }^{9}$ on electrical noise, they
showed that linear responses of a system initially in thermal equilibrium depend on microscopic details only through the coupled equilibrium fluctuations of the macroscopic quantities involved. Callen and Welton ${ }^{5}$ conjectured that the theory of. linear irreversible processes in general could be approached via study of equilibrium fluctuations. Developments in the field since then, particularly those of Green, ${ }^{10}$ Mori, ${ }^{11}$ Kubo, ${ }^{12}$ and their co-workers, represent a series of confirmations of this idea. Bernard and Callen ${ }^{13}$ showed that the case of nonlinear response of a driven system can also be reduced to the theory of higher moments of equilibrium fluctuations. The present paper may be regarded as still another confimation of Callen and Welton's prediction, in which we extand the theory to sonequilibrium states whose representative ensembles are not the result of any dynamical perturbation starting from equilibrium.

In previous transport theories of the aforementioned types, dissipative-irreversible effects did not appear in the ensemble initially set up. For example, a system of N particles of mass m, distributed with macroscopic density $\rho(x)$, local temperature $T(x)$, is often described in classical theory by an N-particle distribution function, or Liouville function, of the form:

$$
\begin{equation*}
W_{N}\left(x_{2} p_{2} \ldots x_{N} l_{N}\right)=\prod_{i_{3},}^{W} \frac{\rho^{\left(x_{i}\right)}}{N(m)}\left[2 \pi k A T\left(x_{i}\right)\right]^{2} \operatorname{enp}\left\{-\frac{p_{i}^{2}}{2 m d T\left(x_{i}\right)}\right\} \tag{2.1}
\end{equation*}
$$

But, although this distribution represents nonvanishing density and temperature gradients op, o T, the diffusion current or hest flow computed from (2.1) is zero.

Likewise, in quantum theory such a physical situation has been described ${ }^{11}$ by the "local equilibrium", or "frozenstate " density matrix:

$$
\begin{equation*}
P_{t}=\frac{1}{z} \exp \left\{-\int d_{x}(x)[H(x)-\infty(x) n(x)]\right\} \tag{2.2}
\end{equation*}
$$

where $H(x), n(x)$ are the Hamiltonian density and number density operators. Again, although (2.2) describes gradients of temperature, concentration, and chemical potential, the fluxes computed from (2.2) are zero.

Mathematically, it was found that dissipative effects appear in the equations only after one has carried out the following operations: (a) approximate forward integration of the equations of motion for a short "induction time", and (b) time smoothing or other coarse-graining of distribution functions or Heisenberg operators.

Physically, it has always been somewhat of a mystery why either of these operations is needed; for one can argue that, in most experimentally reslizable cases, dissipative effects (A) are already "in progress" at the time the experiment is started, and (B) take place slowly, so that the low-order distribution functions and expectation values of measurable quantities must already be slowly-varying functions
of time and position; and thus not affected by coarse-graining. In cases where this is not true, coarse-graining would result in loss of the physical effects of interest. This point is discussed further in Appendix B.

It appears, therefore, that the real nature of the forward integration and coarse-graining operations has not yet been explained; in a correctly formulated theory neither should be required. We are led to suspect the choice of initial ensemble; i.e. that ensembles such as (2.1) and (2.2) do not fully describe the conditions under which irreversible phenomena are observed, and therefore do not represent the correct solution of the stage (1) problem. [We note that (2.1) and (2.2) have never been "derived" from anything more fundamental; they have been written down intuitively, by analogy with the grand canonical ensemble of equilibrium theory]. The forward integration and coarse-graining operations would, on this view, be regarded as corrective measures which in some way compensate for the error in the initial ensemble.

This conclusion is in agreement with that of Mori, Oppenheim, and Ross ${ }^{14}$ (hereafter denoted MOR), who have provided a useful review of this field. These authors never claimed that $P_{t}$ in (2.2) was the correct density matrix, but supposed that it differed by only a small amount from another matrix $P(t)$, which they designate as the "actual distribution". They further supposed that after a short induction time, $\rho_{t}$ relaxes into $\rho(t)$, which would
explain the need for forward integration. Some such relaxation undoubtedly takes place in the low-order distribution functions derived from $P$, as was first suggested by Bogoliubov ${ }^{15}$ for the analogous classical problem. However, . tais is not possible for the full "global" density matrix; if $\rho_{t}$ and $\rho(t)$ differ at $t=0$ and undergo the same unitary transformation in their time development, they cannot be equal at any other time. Furthermore, . $\rho(t)$ was never uniquely defined; given two different candidates $p_{1}(t)$, $\rho_{2}(t)$ for this role, MOR give no criterion by which one could decide which is indeed the "actual" distribution.

For reasons explained in Appendix A, we believe that such criteria do not exist; i.e.; that the notion of an "actual disteibution" is illusory, the result of a persistent semantic confusion that has long plagued statistical mechanics. In the following section we approach the problem in a different way, which yields a definite procedure for constructing a density matrix which is to replace $\rho_{t}$, and will play approximately the same role in our theory as the $P(t)$ of MOR.

## 3. THE GIBBS ALGORITHM

If the above reasoning is correct, a re-examination of the procedures by which ensembles are set up in statistical mechanics is indicated. If we can find an algorithm for constructing density matrices which fully describe nonequilibrium conditions, we should rind that transport and other dissipative effects are obtainable by direct quadratures over the initial ensemble.

This algorithm, we suggest, was given already by Gibbs. ${ }^{16}$ The great power and generality of the methods he introduced have not yet been appreciated; until recently it was scarcely possible to understand the process by which he constructed his ensembles. This was (loc. cit., p. 143) to assign that probability distribution wich, while agreeing with what is known, "gives the least value of the average index of probability of phase," or as we would describe it today, maximizes the entropy. This process led Gibbs to his canonical ensemble for describing closed systems in thermal equilibrium, the grand canonical ensemble for open systems, and (10c. cit., p. 38), an ensemble to represent a system rotating at angular velocity $\omega$, in which the probability density is proportional to

$$
\begin{equation*}
\exp [-\beta(H-\omega \cdot M)] \tag{3.1}
\end{equation*}
$$

where $H$, $M$ are the phase functions representing Hamiltonian
and total angular momentum.
A few years later, the Ehrenfests ${ }^{17}$ dismissed these ensembles as mere "analytical tricks", devoid of any real significance, and stressed the physical superiority of Boltmann's methois, thereby initiating a school of thought in statistical mechanics which persists to this day. The mathematical superiority of the canonical and grand canonical ensembles for calculating equilibrium properties has since become firmly established. Furt ermore, although Gibbs gave no applications of the rotitional ensemble (3.1), it has been shown recently ${ }^{18}$ that this ensemble provides a straightforward method of calculating the gyromagnetic effects of Barnett and Einstein-de Haas. At the present time, therefore, the Gibbs methods stand in a poultion of proven success in applications, independent of all the conceptual problems regarding their justification, which are still being debated. As a result, Statistical Me whanics has taken on a peculiar hybrid character, in which the practical calculations are always based on the methods a Qibbs, while the pedagogy has tended to concentrate instead ne ergodic theory. ${ }^{19}$

The recent development of Information Theory ${ }^{20}$ has made 11 possible to see the method of Gibbs as a general procedure for inductive reasoning, independent of ergodic theory or any other physical hypotheses, and whose range of validity is therefore not restricted to equilibrium problems; or inceed to physics. The significance of the principle of maximum entropy, in the light of Information Theory, has
been described in detail elsewhere ${ }^{21,22}$ and applications to statistical problems outside of physics have been sketched. ${ }^{23}$ In the following we show that this principle is sufficient to construct ensembles representing a wide variety of nonequilibrium conditions, and that these new ensembles yield transport coefficients by direct quadratures.

The general rule for constructing ensembles is as follows. The available information about the state of a system consists of results of various macroscopic measurements. Tret the quantities measured be represented by the operators $\mathrm{F}_{1}, \mathrm{~F}_{2}$, $\ldots F_{m}$. The results of the measurements are, of course, simply a set of numbers: $\left\{f_{1}, \ldots, f_{m}\right\}$ which makes no reference to any probability distribution. The ensemble is then a mental construct which we invent in order to describe the range of possible microscopic states, compatible with the measured values of the $\mathrm{F}_{\mathrm{k}}$.

If we say that a density matrix $\rho$ "contains" certain information, we mean by this that, if we communicate the density matrix to another person he must be able, by applying. the usual procedure of stage (3) above, to recover this information from it. Thus we say that the density matrix "agrees" with the given information if and only if it is adjusted to yield expectation values equal to the measured numbers:

$$
\begin{equation*}
f_{k}=\operatorname{Tr}\left(\rho F_{k}\right)=\left\langle F_{k}\right\rangle, k=1, \ldots, m \tag{3.2}
\end{equation*}
$$

and in order to ensure that the density matrix describes the full range of possible microscopic states compatible with (3.2),
and not Just some arbitrary subset of them (in other words, that it describes only the information given, and contains no hidden arbitrary assumptions about the microscopic state), we demand that, while satisfying the constraints (3.2), it shall maximize the quantity

$$
\begin{equation*}
S_{I}=-\operatorname{Tr}(\rho \log \rho) \tag{3.3}
\end{equation*}
$$

A great deal of confusion has resulted from the fact that, for three decades, the single word "entropy" has been used interchangeably to stand for either the quantity (3.3), or the quantity measured experimentally (in the case of clased systems) by the integral of dQ/T over a reversible path. We will try to maintain a clear distinction here by saterring to S as the "information entropy" and denoting the experimentally measured entropy by $S_{E}$. These quantities are different in general; in the equilibrium case (which is the only one for which $S_{E}$ is defined in conventional thermodynamics) the relation between them has been shown ${ }^{22}$ to be: for all density matrices which agree with the macroscopic information that defines the thermodynamic state,

$$
\begin{equation*}
k S_{\mathbf{I}} \leq S_{\mathbf{E}} \tag{3.4}
\end{equation*}
$$

where $k$ is Boltzmann's constant, with equality in (3.4) if and only if $S_{I}$ is computed from the canonical density matrix ${ }^{24}$

$$
\begin{equation*}
\rho \frac{1}{2\left[\lambda_{1} \cdots \lambda_{m}\right.} \operatorname{esp}\left[\lambda_{1} F_{1}+\ldots+\lambda_{m} F_{m}\right] \tag{3.5}
\end{equation*}
$$

where the $\lambda_{k}$ are unspecified real constants, and for normalization (Tr $\mathrm{P}=1$ ) we have

$$
\begin{equation*}
z\left(\lambda_{1} \cdots \lambda_{m}\right)=\operatorname{Tr} \exp \left[\lambda_{1} F_{1}+\ldots+\lambda_{m} F_{m}\right] \tag{3.6}
\end{equation*}
$$

which quantity will be called the partition function. It remains only to choose the $\lambda_{k}$ [which appear as Lagrange. multipliers in the derivation of (3.5) from a variational principle] so that (3.2) is satisfied. This is the case if

$$
\begin{equation*}
f_{k}=\left\langle F_{k}\right\rangle=\frac{\partial}{\partial \lambda_{k}} \log z_{g}, k=1,2, \ldots, m \tag{3.7}
\end{equation*}
$$

These relations are just sufficient to determine all the unknowns. $\lambda_{k}$ in terms of the given data $\left\{f_{1} \ldots f_{m}\right\}$; indeed, we can solve (3.7) explicitly for the $\lambda_{k}$ as follows. The maximum attainable value of $S_{X}$ is, from (3.5), (3.6),

$$
\left(s_{I}\right)_{\max }=\log z-\sum_{k=1}^{m} \lambda_{k}\left\langle p_{k}\right\rangle
$$

If this quantity is expressed as a function of the given data, $S\left(f_{1} \ldots f_{m}\right)$, it is easily shown ${ }^{22,24}$ from the above relations that

$$
\lambda_{k}=-\frac{\partial s}{\partial f_{k}}
$$

A number of other general formal properties of maximum-entropy distributions are iisted elsewhere ${ }^{22}$ and it has been shown ${ }^{22,25}$ that the second law of thermodynamics is a simple consequence of the inequality (3.4) and the dynamical invariance of $S_{I}$.

Further mathematical details concerning the process of entropy maximization have been given by von Neumann, ${ }^{26}$ Wichmann, ${ }^{27}$ and Wannier. ${ }^{28}$ In Appendix C, we point out an important property of the maximum entropy ensemble, which is helprul in gaining an intuitive understanding of this theory. Qiven any density matrix $\rho$ and any $\varepsilon$ in $0<c<1$, there is defined a "high-probability manifold" (HPM) of finite dimensionality $W(E)$, consisting of all state vectors to which ? assigns an "array probability" as defined in Ref. 21b, Sec. 7, greater than a certain amount $\delta(\epsilon)$, and such that the eigenvectors of $\rho$ spanning the complementary manifold have total probability less than $\epsilon$. As $\epsilon$ varies, any density matrix $\rho$ thus defines a nested sequence of HPMis. For macroscopic system, the information entropy $S_{I}$ may be identified with $\log w(C)$ in the following sense: If $N$ is the number of particles in the system, then as $N \rightarrow \infty$ with the intensive parameters held constant, $N^{-1} S_{I}$ and $N^{-1} \log W(\epsilon)$ approach the same limit independently of 6 . This is a form of the asymptotic equipartition theorem ${ }^{20}$ of Information Theory. The process of entropy maximization therefore amounts, for all practical purposes, to the same thing as finding the density matrix which, while agreeing with the available information, defines the largest possible HPM; this is the basis of the remark following (3.2). An analogous result holds in classical theory ${ }^{25}$ in which W ( E ) becomes the phase volume of the "high-probability region" of phase space, as defined by the N-particle distribution function.

The above procedure is sufficient to construct the density matrix representing equilibrium conditions, provided the quantities $F_{k}$ are chosen to be constants of the motion. The extension to nonequilibrium cases, and to equilibrium problems In which we wish to incorporate information about quantities which are not intrinaic constants of the motion (such as stress or magnetization ${ }^{22}$ ) requires mathematical generalization which we give in two steps.

It is a common experience that the course of a physical process does not in general depend only on the present values of the observed macroscopic quantities, it depends also on the past history of the system. The phenomenon of spin echoes ${ }^{29}$ is a particularly striking example of this. Correspondingly, we mast expect that, If the $\mathrm{F}_{\mathrm{k}}$ are not constants of the motion, an ensemble constructed as above using only the present values of the $\left\langle F_{k}\right\rangle$ will not in general suffice to predict either equilibrium or nonequilibrium behavior. As we will see presently, it is just this fact which causes the error in the "frozen state" density matrix $\rho_{t}$ of Eq. (2.2).

In order to describe time variations, we extend the $\mathrm{F}_{\mathrm{k}}$ to the Reisenberg operators

$$
\begin{equation*}
F_{k}(t)=U^{-1}(t) F_{k}(0) U(t) \tag{3.8}
\end{equation*}
$$

in which the time-development matrix $U(t)$ is the solution of the Schrödinger equation

$$
\begin{equation*}
\hbar \tilde{U}(t)=H(t) U(t) \tag{3.9}
\end{equation*}
$$

With initial conditions $U(O)=1$, and $H(t)$ is the Hamiltonian If we are fiven values of the $\left\langle F_{k}\left\langle t_{1}\right\rangle\right.$ at various times $t_{1}$. then each of these date must be considered a separate piece of information, to be given its Lagrange multiplier $\lambda_{k i}$ and included in the sum of (3.5). In the limit where we inagine information given over a continuous time interval, - $\ll O_{3}$ the summation over the time index $i$ becomes an integration and the canonical density matrix (3.5) becomes

$$
\begin{equation*}
\rho=\frac{1}{z} \exp \left\{\sum_{k=1}^{\infty} \int_{-z}^{0} \lambda_{k}(\theta) F_{k}(t) d t\right\} \tag{3.10}
\end{equation*}
$$

whare the partition function has been generalized to a

## Partition Anctiond

$$
\begin{equation*}
Z\left[\lambda_{1}(t) \cdots \lambda_{n}(t)\right]=T_{n} \operatorname{erp}\left\{\sum_{k=1}^{\infty} \int_{-\infty}^{+} \lambda_{k}(t) F_{k}(t) d t\right\} \tag{3.11}
\end{equation*}
$$

and the unknom Lagrange multiplier functions $\lambda_{k}(t)$ are Getermined from the condition that the density matrix agree with the given data $\left\langle\mathcal{F}_{\kappa}(t)\right\rangle$ over the "information-gathering" time interval:

$$
\begin{equation*}
\left\langle F_{k}(t)\right\rangle=T_{1}\left[p F_{k}(t)\right]=f_{k}(A), \quad-2 \leq t \leq 0 \tag{3.12}
\end{equation*}
$$

By the perturbation methods developed in Sec. 5 below, we find that (3.12) reduces to the natural generalization of (3.7):

$$
\begin{equation*}
\left\langle F_{x}(t)\right\rangle=\frac{\int}{\int \lambda_{x} \theta t} \log z,-\tau \leq t \leq 0 . \tag{3.13}
\end{equation*}
$$

where denotes the functional derivative.
Finally, if the operators $F_{k}$ depend on position as well as lime, as in (2.2), Eq. (3.8) is changed to

$$
\begin{equation*}
F_{k}(x, t)=U^{-1}(t) F_{k}(x, 0) U(t) \tag{3.14}
\end{equation*}
$$

and the values of these quantities at each point of space and time now constitute the independent pieces of information, which are coupled into the density matrix via the Lagrange mitiplier function $\lambda_{k}(x, t)$. If we are given information abult $F_{k}(x, t)$ throughout a space-time region $R_{k}$ (which can be different for different quantities $F_{k}$ ), the ensemble which incorporates all this information, while locating the largest possible HPM, is

$$
\begin{equation*}
\rho=\frac{1}{2} \exp \left\{\sum_{k} \int_{R_{k}} d t d^{3} x \quad \lambda_{k}(x, t) F_{k}(x, t)\right\} \tag{3.15}
\end{equation*}
$$

ulth the partition functional

$$
\begin{equation*}
z=\operatorname{Tr} \exp \left\{\sum_{x} \int_{R_{k}} d t d^{3} x \lambda_{k}(x, t) F_{k}(x, t)\right\} \tag{3.16}
\end{equation*}
$$

and the

$$
\lambda_{k}(x, t) \text { determined from }
$$

$$
\begin{equation*}
\left\langle F_{k}(x, t)\right\rangle=\frac{\delta}{\delta \lambda_{k}(x, t)} \log Z_{,}(x, t) \text { in } R_{k} \tag{3.17}
\end{equation*}
$$

Prediction of any quantity $J(x, t)$ is then accomplished by calculating

$$
\begin{equation*}
\langle J(x, t)\rangle=\operatorname{Tr}[\rho \quad J(x, t)] \tag{3.18}
\end{equation*}
$$

In equations (3.15) - (3.18) we have the general algorithm for calculating irreversible processes. We emphasize that the basic physical and conceptual formulation of the theory is complete at this point; what follows represents only the working out of some mathematical consequences of this algorithm. A simple example of an exactly soluble problem using these relations, is given in Appendix D.

The form of equations (3.15) - (3.18) makes it appear at first glance that stages (1) and (2), discussed in the Introduction, are now fused into a single stage. However, this is only a consequence of our using the Heisenberg representation. According to the usual conventions, the Schrodinger and Heisenberg representations coincide at time $t=0$; thus we may regard the steps (3.15) - (3.17) equally well as determining the density matrix $\rho(0)$ in the Schrodinger representation; i.e. as solving the stage (1) problem. If, having found this initial ensemble, we switch to the Schrbdinger representation, Eq. (3.18) is then replaced by

$$
\begin{equation*}
\langle J(x)\rangle_{t} * \operatorname{Tr}[J(x) \rho(t)] \tag{3.19}
\end{equation*}
$$

in which the problem of stage (2) now appears explicitly as that of finding the time-evolution of $\rho(t)$. The form (3.19) will be more convenient if a number of different
quantities $J_{1}, J_{2}, \ldots$ are to be predicted.
Byidently, our arguments leading to the rule (3.15), (3.17) for converting experimental measurements into a density matrix can be further refined by applying the quantummechanical theory of measurement. We have not done this, for several reasons. In the first place, the theory of measurement is itself being subjected to renewd scrutiny, ${ }^{30}$ and fundamental modifications appear likely as a result. Secondly, the formalism here presented is capable of other interpretations which give it a meaning independent of the theory of measurement. Questions concerning predictions made by ensembles which have maximum phase volume for prescribed expectation values are mathematically well-posed and physically interesting in their own right. Finally, it will appear that the above formalism already yields the results of usual practical interest without these further elaborations.

## 4. DNNAMICAL PERTURBATIONS

If the irreversible process is the result of a dynamical perturbation on what would otherwise be an equilibrium condition -- in other words, where it is caused entirely by an explicitly given term $V(t)$ in the Hamiltonian -- the above equations reduce to a familiar form. If we remain in the Iull Heisenberg representation, Eq. (3.18), then if the available information concerning the state of the system consists solely of the fact that it was in thermal equilibrium in the remote past, the density matrix (3.15) remains the equilibrium one for all time. The full content of the theory then resides in (3.18).

Suppressing the coordinate $x$ for brevity, the Heisenberg operator $J(t)$ is found by a perturbation expansion of (3.8). If $V(t)=Q v(t)$, where $Q$ is an operator and $v(t)$ a specified numerical function, the first-order effect is given by

$$
\begin{equation*}
\langle J(t)\rangle-\langle J(-\infty)\rangle=\int_{-\infty}^{t} \varphi_{J Q}\left(t-t^{\prime}\right) v\left(T^{\prime}\right) d t^{\prime} \tag{4.1}
\end{equation*}
$$

where $\langle J(-\infty)\rangle$ is the thermal equilibrium value, and

$$
\begin{equation*}
f_{J Q}\left(t-t^{\prime}\right) \equiv \frac{1}{i n} \quad\left[Q^{\circ}\left(t^{\prime}\right), J^{\circ}(t)\right] \tag{4,2}
\end{equation*}
$$

is the impulse-response function, or "aftereffect function" described by Kubo, ${ }^{12}$ and by Bernard and Callen, ${ }^{13}$ who also
give higher order nonlinear terms. The superseripts in (4.2) denote time development according to the unperturbed Mamiltonian $\mathrm{H}_{\mathrm{o}}$.

This aspect of the theory, which is adequate to treat such problems as magnetic resonance line shape and electrical conductivity, has already been developed by many authors ${ }^{31}$ into an elegant, and undoubtedly final, form. Among specific calculations based on it, one may note the treatments of normal metal conductivity by Langer, ${ }^{32}$ and the Meissner effect by Mastis and Bardeen ${ }^{33}$ and Nambu. ${ }^{34}$

The case of non-dynamical perturbations, such as temperature or concentration gradients, or shearing stress of a fluid is, as already noted, fundamentally different and presents peculiar difficulties both mathematical and conceptual. In some cases, as Feynman and Montroll ${ }^{35}$ have shown, one can use physical reasoning to restore the appearance of a dynamical problem by inventing a fictitious "effective Hamiltonian" $H_{e}(t)$ which would, if present, produce a similar nonequilibrium state starting from equilibrium; or as Luttinger ${ }^{3}$ has shown, one can find the equilibrium distribution under the action of a fictitious force field and use "balancing" arguments based on such relations as the Einstein equation connecting diffusion coefficient and mobility. However, these are clearly artificial devices, and there seems to be no general, unique prescription for finding $H_{e}$ (see, however, Appendix $E_{s}$ in which we show that under certain conditions a $1: 1$ correspondence can be set up between statistical problems of the
present theory and a class of fictitious dynamical problems). Most writers on transport theory have recognized that existing treatments of diffusion, thermal conductivity, and viscosity are not fully satisfactory for this reason. This has been stressed particularly in the recent review article of Chester, ${ }^{2}$ who gives many more details and references, and concludes that "mo it would be very satisfying to have a quite different approach to these problems".

The above algorithm evidently provides one such approach: to investigate its suitability we note that the aforementioned problems all involved near-equilibrium conditions, and so in treating them by (3.15) - (3.18) we can make the corresponding approximation. In the following section we collect the basic perturbation formulas needed for this.
5. PERTURBATION THEORY FOR EXPECTATION VALUES

We denote an "unperturbed" density matrix $\rho_{o}$, by

$$
\begin{equation*}
\rho_{0}=\frac{e^{A}}{Z_{0}}, \quad Z_{0}=\operatorname{Tr}\left(e^{A}\right), \tag{5.1}
\end{equation*}
$$

a "perturbed" one by

$$
\begin{equation*}
\rho=\frac{e^{A+\epsilon B}}{Z}, \quad Z=\operatorname{Tr}\left(e^{A+\epsilon B}\right)_{s} . \tag{5.2}
\end{equation*}
$$

where $A, B$ are Hermitian. The expectation values of any operator C over these ensembles are respectively

$$
\begin{equation*}
\langle c\rangle\rangle_{o}=\operatorname{Tr}\left(\rho{ }_{o} c\right), \quad\langle c\rangle=\operatorname{Tr}(\rho c) \tag{5.3}
\end{equation*}
$$

The expansion of $<C>$ to all orders in 6 has been derived in Ref. 18, Appendix B. The $n$ 'th order contribution is the covariance, in the unperturbed ensemble, of $C$ with an operator $Q_{n}$ :

$$
\begin{equation*}
\left.\langle C\rangle-\langle C\rangle=\sum_{n=1}^{\infty} \epsilon^{n}\left\langle Q_{n} c\right\rangle-\left\langle Q_{n}\right\rangle\langle C\rangle\right] \tag{5,4}
\end{equation*}
$$

Here, $Q_{n}$ is defined by $Q_{1} \equiv S_{1}$, and

$$
\begin{equation*}
Q_{n} \equiv S_{n}-\sum_{k=1}^{n-1}\left\langle Q_{k}\right\rangle_{0} S_{n-k}, \quad n>1 . \tag{5.5}
\end{equation*}
$$

in which $S_{n}$ are the operators appearing in the well-known expansion

$$
\begin{equation*}
e^{A+E B}=e^{A}\left[1+\sum_{n=1}^{\infty} \epsilon^{n} S_{n}\right] \tag{5.6}
\end{equation*}
$$

More explicitly,

$$
\begin{equation*}
S_{n}=\int_{0}^{1} \alpha x_{1} \int_{0}^{x_{1}} d x_{2} \cdots \int_{0}^{x_{n-1}} d x_{n} B\left(x_{1}\right) \cdots B(x) \tag{5.7}
\end{equation*}
$$

where

$$
\begin{equation*}
B(x)=e^{-x A} B e^{x A} . \tag{5.8}
\end{equation*}
$$

The first-order term is

$$
\langle c\rangle-\langle c\rangle_{0}=\left\langle\int_{0}^{1} d x\left[\left\langle e^{-x A_{B e^{x A}}} c\right\rangle_{0}-\langle B\rangle o\langle c\rangle_{0}\right]\right.
$$

and it will appear below that all relations of linear transport theory are special cases of (5.9).

For a more condensed notation, define the average of any operator $B$ over the sequence of similarity transformations as

$$
\begin{equation*}
\bar{B}=\int_{0}^{1} d x e^{-x A} B e^{x A} \tag{5.10}
\end{equation*}
$$

which we will call the Kubo transform of. B. Then (5.9) becomes

$$
\begin{equation*}
\langle c\rangle-\langle c\rangle\rangle_{0}=\epsilon \kappa_{C B} \tag{5.11}
\end{equation*}
$$

in which, for various choices of $C$, $B$, the quantities

$$
\begin{equation*}
\mathrm{I}_{\mathrm{CB}} \equiv\langle\overline{\mathrm{~B}} C\rangle_{0}-\langle\overline{\mathrm{B}}\rangle{ }_{0}\langle\mathrm{C}\rangle{ }_{0} \tag{5.12}
\end{equation*}
$$

are the basic covariance functions of the linear theory.
We list a few userul properties of these quantities; in all cases, the result is easily proved by writing out the expressions in the representation where $A$ is diagonal. Let F $G$ be sny two operators; then

$$
\begin{align*}
& \langle\bar{F}\rangle \odot=\langle F\rangle  \tag{5.13}\\
& K_{F G}=K_{G F} \tag{5.14}
\end{align*}
$$

If $F, G$, are Hermitian, then

$$
\begin{equation*}
K_{F G} \text { is real, } T_{F F} \geq 0 \tag{5.15}
\end{equation*}
$$

If $\rho_{0}$ is s projection operator representing a pure state, then $K_{F G}=0, I r \quad \rho_{0}$ is not a pure state density matrix, then with Hernitian $F, G$,

$$
\begin{equation*}
K_{F F} K_{G G}-K_{F G} 2 \geq 0 \tag{5.16}
\end{equation*}
$$

with equality if and only if $F$ - $q G_{\text {, }}$ where $q$ is a real number. Ir a 1s of the form

$$
\begin{equation*}
G(u)=e^{-u A} G(0) e^{u A} \tag{$(5.17$.}
\end{equation*}
$$

then

$$
\begin{equation*}
\frac{d}{d u} K_{F G}=\langle[F, G]\rangle_{\circ} \tag{5.18}
\end{equation*}
$$

## 6. APPLICATION TO NEAR-EQUILIBRIUM ENSEMBLES

A closed system in thermal equilibrium is described, as usual, by the density matrix

$$
\begin{equation*}
p_{0}=\frac{e^{-\beta H}}{Z_{0}(\beta)}=\frac{e^{-\beta H}}{\operatorname{Tr}\left(e^{-\beta H}\right)} \tag{6.1}
\end{equation*}
$$

which maximizes $S_{I}$ for prescribed $\langle H\rangle$, and is a very special case of (3.15). The thermal equilibrium prediction for any quantity F is, as usual,

$$
\begin{equation*}
\langle F\rangle_{0}=\operatorname{Tr}\left(P_{0} F\right) \tag{6.2}
\end{equation*}
$$

But suppose we are now given the value of $\langle F(t)\rangle$ throughout the "information-gathering" interval $-\tau<t<0$. The ensemble which includes this new information in addition to information about $\langle H\rangle$ as in (6.1) is of the form (3.15), which now maximizes $s_{I}$ for prescribed $\langle H\rangle$ and $\langle F(t)\rangle$ in $-\tau<t<0$. It corresponds to the partition functional

$$
\begin{equation*}
Z[\beta, \lambda(t)]=T r \exp \left[-\beta H+\int_{-\tau}^{\theta} \lambda(t) F(t) d t\right] \tag{6.3}
\end{equation*}
$$

which is a special case of (3.11). If, during the informationgathering interval, this new information was simply $\langle F(t)\rangle=$
$\langle F\rangle$ o, it is easily shown from (3.13) that we have identically (see Appendix D for an explicit example)

$$
\begin{equation*}
\int_{\sigma}^{0} \lambda(t) F(t) d t=0 \tag{6.4}
\end{equation*}
$$

In words: if the new information is redundant (in the sense that it is only what we would have predicted from the old information), then it will drop out of the equations and the ensemble is unchanged. As shown in Appendix $F$, this is a general property of the formalism here presented. In applications this means that there is never any need, when setting up an ensemble, to ascertain whether the different pieces of information used are independent; any redundant parts will cancel out automatically.

Ir, therefore, we treat the integral in (6.3) as a small perturbation, we are expanding in powers of the departure from equilibrium. For validity of the perturbation scheme it is not necessary that $\lambda(t) r(t)$ be everywhere small; it is sufficient if the integral is small. First-order effects in the departure from equilibrium, such as linear diffusion or heat flow, are then predicted using the general formula (5.9), with the choices $A=-3 H$, and

$$
\begin{equation*}
B=\int_{-\pi}^{0} \lambda(t) F(t) d t \tag{6.5}
\end{equation*}
$$

With constant $H$, the Heisenberg operator $P(t)$ reduces to

$$
\begin{equation*}
F(t)=\exp (1 H t / h) F(0) \exp (-1 H t / h) \tag{6.6}
\end{equation*}
$$

and its Kubo transform (5.10) becomes

$$
\begin{equation*}
F(t)=\frac{1}{B} \int_{0}^{\infty} d u F(t-1 h u), \tag{6.7}
\end{equation*}
$$

the characteristic quantity of the Kubo ${ }^{12}$ theory.
In the notation of (5.11), the first-order expectation value of any quantity $C(t)$ will then be given by

$$
\begin{equation*}
\langle c(t)\rangle-\langle c\rangle_{0}=\int_{-\tau}^{0} K_{C F}\left(t, t^{\prime}\right) \lambda\left(t^{\prime}\right) d t^{\prime} \tag{6.8}
\end{equation*}
$$

where $K_{C F}$ is now indicated as a function of the parameters $t_{\text {, }} t$ contained in the operators:

$$
\begin{equation*}
K_{C F}\left(t, t^{\prime}\right)=\left\langle F\left(t^{\prime}\right) C(t)\right\rangle o^{-\left\langle\sum\right\rangle 。\langle C\rangle}{ }_{o} \tag{6.9}
\end{equation*}
$$

Remembering that the parameters $t, t^{\prime}$ are part of the operators $C, F$, the general reciprocity law (5.14) now becomes

$$
\begin{equation*}
K_{C F}\left(t, t^{\prime}\right)=K_{F C}\left(t^{\prime}, t\right) \tag{6.10}
\end{equation*}
$$

When $H$ is constant, it follows also from (6.6) that

$$
\begin{equation*}
K_{C F}\left(t, t^{\prime}\right)=K_{C F}\left(t-t^{\prime}\right) \tag{6.11}
\end{equation*}
$$

More generally, take the unperturbed ensemble as the grand canonical distribution (3.1) corresponding to the choice

$$
\begin{equation*}
A=-\beta\left[\mathcal{L}-\mu_{1} N_{1}-\cdots-\mu_{p} N_{r}\right] \tag{6,12}
\end{equation*}
$$

where

$$
\begin{align*}
& \mathcal{H}^{\prime} \equiv \int \operatorname{se}^{\prime} x H(x)  \tag{6,13}\\
& N_{1} \equiv \int d^{\prime} x n_{i}(x) \tag{6.14}
\end{align*}
$$

are the total Hamiltonian, and number operator for the $i$ 'th type of particle, and $H(x), n_{1}(x)$ the corresponding density operators. If $\sum \mathcal{N}_{i} N_{i}$ commutes with $H$ and $F(t)$, then (6.7) remains valid; otherwise the kubo transforms $\bar{F}(t)$ must be defined by (5.10).

In the unperturbed (equilibrium) ensemble, expectation values are independent of time, so for any operator $J(x, t)$ we have

$$
\begin{equation*}
\langle J(\Psi, t)\rangle=\langle J(x)\rangle \tag{6.15}
\end{equation*}
$$

Often, this will be independent of $x$ also. Now suppose we are given additional information consisting of the expectation values of several functions of position and time $F_{k}(x, t)$ [which may include the above operators $H(x)$ and $\left.N_{1}(x)\right]$ throughout the space-time regions $\mathrm{R}_{\mathrm{k}}$ of (3.15). The new ensemble is of the form (5.2) with the choice

$$
\begin{equation*}
\epsilon B=\sum_{k=1}^{n} \int_{R_{k}} d t d^{3} k \quad \lambda_{k}(k, t) F_{k}(k, t) \tag{6.16}
\end{equation*}
$$

which is a small perturbation if the given $\left\langle\mathrm{F}_{\mathrm{k}}(\mathrm{x}, \mathrm{t})\right\rangle$ are not appreciably different from their equilibrium values
$\left\langle F_{k}(x)\right\rangle_{0^{\circ}}$ In this new ensemble, the predicted value of any quantity $J(x, t)$ is given by another special case of (5.11):

$$
\begin{equation*}
\langle J(x, t)\rangle-\langle J(n)\rangle_{0}=\sum_{k=1}^{\infty} \int_{\mathbb{R}_{k}} s^{\prime} d t^{\prime} K_{J F_{k}}\left(x, t ; x^{\prime}, t^{\prime}\right) \lambda_{k}\left(x^{\prime}, t^{\prime}\right) \tag{6.17}
\end{equation*}
$$

with

$$
\begin{equation*}
K_{J F_{F}}\left(x, t ; x^{\prime}, t^{\prime}\right) \equiv\left\langle F_{k}(x, t) J(x, t)\right\rangle_{0}-\left\langle F_{k}\left(x^{\prime}\right)\right\rangle_{0}\langle J(x)\rangle \tag{6.18}
\end{equation*}
$$

From (6.17) the nonlocal character of the theory is apparent.
The problem of predicting effects of first order in the departure from equilibrium is now reduced to that of finding the Lagrange multiplier functions $\lambda_{k}(x, t)$ from (3.17).
This problem is treated, in the linear approximation, in the following section.

