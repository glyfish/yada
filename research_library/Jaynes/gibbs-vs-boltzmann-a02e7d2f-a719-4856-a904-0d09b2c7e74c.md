# Gibbs vs Boltzmann Entropies* 

E. T. Jaynes<br>Department of Physics, Washington University, St. Louis, Missouri

(Received 27 March 1964; in final form, 5 November 1964)


#### Abstract

The status of the Gibbs and Boltzmann expressions for entropy has been a matter of some confusion in the literature. We show that: (1) the Gibbs $H$ function yields the correct entropy as defined in phenomenological thermodynamics; (2) the Boltzmann $H$ yields an "entropy" that is in error by a nonnegligible amount whenever interparticle forces affect thermodynamic properties; (3) Boltzmann's other interpretation of entropy, $S=k \log W$, is consistent with the Gibbs II, and derivable from it; (4) the Boltzmann $H$ theorem does not constitute a demonstration of the second law for dilute gases; (5) the dynamical invariance of the Gibbs $H$ gives a simple proof of the second law for arbitrary interparticle forces; (6) the second law is a special case of a general requirement for any macroscopic process to be experimentally reproducible. Finally, the "anthropomorphic" nature of entropy, on both the statistical and phenomenological levels, is stressed.


## I. INTRODUCTION

IN the writer's 1962 Brandeis lectures ${ }^{1}$ on statistical mechanics, the Gibbs and Boltzmann expressions for entropy were compared briefly, and it was stated that the Gibbs formula gives the correct entropy, as defined in phenomenological thermodynamics, while the Boltzmann II expression is correct only in the case of an ideal gas. However, there is a school of thought which holds that the Boltzmann expression is directly related to the entropy, and the Gibbs' one simply erroncous. This belief can be traced back to the famous Ehrenfest review article, ${ }^{2}$ which severely criticized Gibbs' methods.

[^0]While it takes very little thought to see that objections to the Gibbs II are immediately refuted by the fact that the Gibbs canonical ensemble does yield correct thermodynamic predictions, discussion with a number of physicists has disclosed a more subtle, but more widespread, misconception. The basic inequality of the Gibbs and Boltzmann II functions, to be derived in Sec. II, was accepted as mathematically correct; but it was thought that, in consequence of the "laws of large numbers" the difference between them would be practically negligible in the limit of large systems.

Now it is true that there are many different entropy expressions that go into substantially the same thing in this limit; several examples were given by Gibbs. However, the Boltzmann expression is not one of them; as we prove in Sec. III, the difference is a direct measure of the effect of interparticle forces on the potential energy and pressure, and increases proportionally to the size of the system.

Failure to recognize the fundamental role of the Gibbs II function is closely related to a much deeper confusion about entropy, probability,
and irreversibility in general. For example, the Boltzmann $I I$ theorem is almost universally equated to a demonstration of the second law of thermodynamics for dilute gases, while ever since the Ehrenfest criticisms, it has been claimed repeatedly that the Gibbs $H$ cannot be related to the entropy because it is constant in time.

Closer inspection reveals that the situation is very different. Merely to exhibit a mathematical quantity which tends to increase is not relevant to the second law unless one demonstrates that this quantity is related to the entropy as measured experimentally. But neither the Gibbs nor the Boltzmann II is so related for any distribution other than the equilibrium (i.e., canonical) one. Consequently, although Boltzmann's $H$ theorem does show the tendency of a gas to go into a Maxwellian velocity distribution, this is not the same thing as the second law, which is a statement of experimental fact about the direction in which the observed macroscopic quantities $(P, V, T)$ change.

Past attempts to demonstrate the second law for systems other than dilute gases have generally tried to retain the basic idea of the Boltzmann $I I$ theorem. Since the Gibbs $H$ is dynamically constant, one has resorted to some kind of coarsegraining operation, resulting in a new quantity $\bar{H}$, which tends to decrease. Such attempts cannot achieve their purpose, because (a) mathematically, the decrease in $\bar{H}$ is due only to the artificial coarse-graining operation and it cannot, therefore have any physical significance; (b) as in the Boltzmann II theorem, the quantity whose increase is demonstrated is not the same thing as the entropy. For the fine-grained and coarsegrained probability distributions lead to just the same predictions for the observed macroscopic quantities, which alone determine the experimental entropy; the difference between $H I$ and $\bar{H}$ is characteristic, not of the macroscopic state, but of the particular way in which we choose to coarse-grain. Any really satisfactory demonstration of the second law must therefore be based on a different approach than coarse-graining.

Actually, a demonstration of the second law, in the rather specialized situation visualized in the aforementioned attempts, is much simpler than any II theorem. Once we accept the well-
established proposition that the Gibbs canonical ensemble does yield the correct equilibrium thermodynamics, then there is logically no room for any assumption about which quantity represents entropy; it is a question of mathematically demonstrable fact. But as soon as we have understood the relation between Gibbs' $H$ and the experimental entropy, Eq. (17) below, it is immediately obvious that the constancy of Gibbs' $H$, far from creating difficulties, is precisely the dynamical property we need for the proof.

It is interesting that, although this field has long been regarded as one of the most puzzling and controversial parts of physics, the difficulties have not been mathematical. Each of the above assertions is proved below or in the Brandeis lectures, using only a few lines of elementary mathematics, all of which was given by Gibbs. It is the enormous conceptual difficulty of this field which has retarded progress for so long. Readers not familiar with recent developments may, I hope, be pleasantly surprised to see how clear and basically simple these problems have now become, in several respects. However, as we will see, there are still many complications and unsolved problems.

Inspection of several statistical mechanics textbooks showed that, while most state the formal relations correctly, their full implications are never noted. Indeed, while all textbooks give extensive discussions of Boltzmann's II, some recent ones fail to mention even the existence of the Gibbs $I I .^{3}$ I was unable to find any explicit mathematical demonstration of their difference. It appeared, therefore, that the following note might be pedagogically useful.

## II. THE BASIC INEQUALITY

We consider, as usual, a monoatomic fluid of $N$ particles. The ensemble is defined by the $N$ particle distribution function, or Liouville function, $W_{N}\left(x_{1}, p_{1} ; x_{2}, p_{2} ; \cdots ; x_{N}, p_{N} ; t\right)$ which gives the probability density in the full phase space of

[^1]the system. The Gibbs $I I$ is then
$$
\begin{equation*}
I I_{\mathrm{G}}=\int W_{N} \log W_{N} d \tau \tag{1}
\end{equation*}
$$
and the corresponding Boltzmann $I I$ is
$$
\begin{equation*}
H_{\mathrm{B}}=N \int w_{1} \log w_{1} d \tau_{1} \tag{2}
\end{equation*}
$$
where $w_{1}\left(x_{1}, p_{1} ; t\right)$ is the single-particle probability density
$$
\begin{equation*}
w_{1}\left(x_{1}, p_{1} ; t\right)=\int W_{N} d \tau_{-1} \tag{3}
\end{equation*}
$$

Here and in the following, we use the notation: $d r \equiv d^{3} x_{1} \cdots d^{3} p_{N}, d \tau_{1} \equiv d^{3} x_{1} d^{3} p_{1}, d \tau_{-1} \equiv d^{3} x_{2} \cdots d^{3} p_{N}$ to stand for phase-volume elements in the full phase space, the space of one particle, and the space of all particles except one, respectively.

Both the Gibbs and Boltzmann $H$ functions are often defined in slightly different ways, in which one uses distribution functions with different normalizations. This changes the numerical values by additive constants which, for fixed $N$, are independent of the thermodynamic state and therefore not relevant to the present discussion. These additive constants are important, however, in connection with the "Gibbs paradox" about entropy of mixing, and the resolution of this paradox by quantum statistics is well known. The distribution functions used above are understood to be probability densities; i.e., normalized according to $\int W_{N} d \tau=\int w_{1} d \tau_{1}=1$.

Using (3) and the fact that $W_{N}$ is symmetric under permutations of particle labels, we can write $H_{\mathrm{B}}$ in a more symmetrical form

$$
\begin{aligned}
H_{\mathrm{B}} & =N \int W_{N} \log w_{1}\left(x_{1}, p_{1}\right) d \tau \\
& =\int W_{N} \log \left[w_{1}(1) \cdots w_{1}(N)\right] d \tau
\end{aligned}
$$

where we use the abbreviation : $(i) \equiv\left(x_{i}, p_{i}\right)$. We have, then,

$$
\begin{equation*}
I I_{\mathrm{B}}-I I_{\mathrm{G}}=\int W_{N} \log \left[\frac{w_{1}(1) \cdots w_{1}(N)}{W_{N}(1 \cdots N)}\right] d \tau \tag{4}
\end{equation*}
$$

equality if and only if $x=1$. Therefore

$$
I I_{\mathrm{B}}-H_{\mathrm{G}} \leq \int W_{N}\left[\frac{w_{1}(1) \cdots w_{1}(N)}{W_{N}(1 \cdots N)}-1\right] d \tau=0
$$

and we have proved
Theorem 1: The Gibbs and Boltzmann II functions satisfy the inequality

$$
\begin{equation*}
H_{\mathrm{B}} \leq I I_{\mathrm{G}} \tag{5}
\end{equation*}
$$

with equality if and only if $W_{N}$ factors "almost everywhere" into a product of single-particle functions

$$
W_{N}(1 \cdots N)=w_{1}(1) \cdots w_{1}(N)
$$

## III. CANONICAL ENSEMBLE

Theorem 1 holds for any symmetrical $W_{N}$. The magnitude of the difference ( $H_{\mathrm{G}}-H_{\mathrm{B}}$ ) depends on the distribution function, and we are particularly interested in the case of thermal equilibrium, represented by the canonical distribution $W_{N} \sim \exp (-\beta I I)$, where $\beta=(k T)^{-1}$ and $H$ is the Hamiltonian, taken of the form

$$
\begin{equation*}
I I=\sum_{i=1}^{N} \frac{p_{i}^{2}}{2 m}+V\left(x_{1} \cdots x_{N}\right), \tag{6}
\end{equation*}
$$

where the potential-energy function $V\left(x_{1} \cdots x_{N}\right)$ is a symmetrical function of the particle coordinates, which we suppose for simplicity depends only the relative coordinates (relaxing this restriction by adding gravitational potential energy leads to a number of interesting results, but does not change the conclusions of this section). More explicitly, we have

$$
\begin{align*}
W_{N}=\left(\frac{\beta}{2 \pi m}\right)^{3 N / 2} Q^{-1} & \\
& \quad \times \exp \left\{-\beta V\left(x_{1} \cdots x_{N}\right)-\beta \sum_{i} \frac{p_{i}^{2}}{2 m}\right\}, \tag{7}
\end{align*}
$$

where

$$
\begin{align*}
Q(\beta, \Omega) & \equiv \int_{\Omega} \exp (-\beta V) d^{3} x_{1} \cdots d^{3} x_{N} \\
& =\Omega \int_{\Omega} \exp (-\beta V) d^{3} x_{2} \cdots d^{3} x_{N} \tag{8}
\end{align*}
$$

Now on the positive real axis, $\log x \leq(x-1)$, with
expression we have made use of the fact that $V$ depends only on relative coordinates, and supposed the range of interparticle forces negligibly small compared to the size of the container, so that the final integration supplies only a factor $\Omega$. From (3), the corresponding singleparticle function is then

$$
\begin{equation*}
w_{1}(x, p)=(\beta / 2 \pi m)^{3 / 2} \Omega^{-1} \exp \left(-\beta p^{2} / 2 m\right) . \tag{9}
\end{equation*}
$$

We therefore have

$$
\left[w_{1}(1) \cdots w_{1}(N)\right] / W_{N}(1 \cdots N)=Q \Omega^{-N} e^{\beta V}
$$

and (4) reduces to

$$
\begin{equation*}
H_{\mathrm{B}}-H_{\mathrm{G}}=\log Q-N \log \Omega+\beta\langle V\rangle \tag{10}
\end{equation*}
$$

where the angular brackets 〈〉 denote the canonical ensemble average. It is also true that

$$
\begin{align*}
\langle V\rangle & =-\partial \log Q / \partial \beta  \tag{11a}\\
\beta\langle P\rangle & =\partial \log Q / \partial \Omega \tag{11b}
\end{align*}
$$

where $P$ is the pressure; Eq. (11) are well-known identities of the canonical ensemble. From (10), (11), we thus find that on an infinitesimal change of state,

$$
\begin{equation*}
d\left(H_{\mathrm{B}}-H_{\mathrm{G}}\right)=\beta d\langle V\rangle+\beta\left[\langle P\rangle-P_{0}\right] d \Omega \tag{12}
\end{equation*}
$$

where $P_{0} \equiv N k T / \Omega$ is the pressure of an ideal gas with the same temperature and density. Introducing the "entropies" $S_{i}=-k H_{i}$ and integrating (12) over a reversible path (i.e., a locus of equilibrium states), we see that the difference varies according to

$$
\begin{align*}
\quad\left(S_{\mathrm{G}}-S_{\mathrm{B}}\right)_{2}-\left(S_{\mathrm{G}}\right. & \left.-S_{\mathrm{B}}\right)_{1} \\
& \quad=\int_{1}^{2} \frac{d\langle V\rangle+\left[\langle P\rangle-P_{0}\right] d \Omega}{T} \tag{13}
\end{align*}
$$

Now from (9), using $\left\langle p^{2}\right\rangle=3 m k T$, we find that

$$
S_{\mathrm{B}}=\frac{3}{2} N k \log (2 \pi m k T)+N k \log \Omega+\frac{3}{2} N k
$$

from which

$$
\begin{aligned}
& \left(\frac{\partial S_{\mathrm{B}}}{\partial T}\right)_{\Omega} d T=\frac{3}{2} \frac{N k d T}{T}=\frac{d\langle K\rangle}{T} \\
& \left(\frac{\partial S_{\mathrm{B}}}{\partial \Omega}\right)_{T} d \Omega=\frac{N k}{\Omega} d \Omega=\frac{P_{0} d \Omega}{T}
\end{aligned}
$$

where $\langle K\rangle=\frac{3}{2} N k T$ is the total kinetic energy.

Over the reversible path (13) the Boltzmann entropy therefore varies according to

$$
\begin{equation*}
\left(S_{\mathrm{B}}\right)_{2}-\left(S_{\mathrm{B}}\right)_{1}=\int_{1}^{2} \frac{d\langle K\rangle+P_{0} d \Omega}{T} \tag{14}
\end{equation*}
$$

and from (13), (14) we finally have for the Gibbs entropy

$$
\begin{align*}
\left(S_{\mathrm{G}}\right)_{2}-\left(S_{\mathrm{G}}\right)_{1} & =\int_{1}^{2} \frac{d\langle K+V\rangle+\langle P\rangle d \Omega}{T} \\
& =\int_{1}^{2} \frac{d Q}{T} \tag{15}
\end{align*}
$$

Equations (14), (15) are the main results sought. From them it is clear that (a) the "Boltzmann entropy" is the entropy of a fluid with the same density and temperature, but without interparticle forces; it completely neglects both the potential energy and the effect of interparticle forces on the pressure; (b) the Gibbs entropy is the correct entropy as defined in phenomenological thermodynamics, which takes into account all the energy and the total pressure, and is therefore equally valid for the gas or condensed phases; (c) the difference between them is not negligible for any system in which interparticle forces have any observable effect on the thermodynamic properties. If the system exhibits an equation of state or heat capacity different from those of an ideal gas, the Boltzmann entropy will be in error by a corresponding amount.

## IV. THE SECOND LAW

We can now demonstrate the second law very easily, for the specialized case usually considered. The following argument can be greatly generalized, although we do not do so here.

It is well known ${ }^{1}$ that the canonical distribution (7) is uniquely determined by a variational property; over all distributions $W_{N}$ that agree with the experimental energy $U$, in the sense that the mean value of the Flamiltonian is

$$
\begin{equation*}
\langle I I\rangle \equiv \int W_{N} H d \tau=U \tag{16}
\end{equation*}
$$

the Gibbs $H$ attains an absolute minimum for the canonical distribution. For this case, we have
just shown that, if the arbitrary additive constant is properly adjusted at a single point, then the Gibbs entropy $S_{\mathrm{G}}=-k H_{\mathrm{G}}$ will be the same as the experimental entropy at all points. Therefore, the general relation between $S_{\mathrm{G}}$ and the experimental entropy $S_{\mathrm{e}}$ is : over all distributions $W_{N}$ that agree with the experimental energy in the sense of (16), we have

$$
\begin{equation*}
S_{\mathrm{G}} \leq S_{\mathrm{e}} \tag{17}
\end{equation*}
$$

with equality if, and only if, $S_{\mathrm{G}}$ is computed from the canonical distribution (7).

At time $t=0$, let our system be in complete thermal equilibrium so that all its reproducible macroscopic properties are represented by the canonical distribution; then the equality holds in (17). Now force the system to carry out an adiabatic change of state (i.e., one involving no heat flow to or from its environment), by appyling some time-dependent term in the Hamiltonian (such as moving a piston or varying a magnetic field). It is well known that the $N$ particle distribution function varies according to the Liouville equation $\dot{W}_{N}=\left\{H(t), W_{N}\right\}$ where the right-hand side is the Poisson bracket; and in consequence $H I_{\mathrm{G}}$ remains constant.

At a later time $t^{\prime}$, the system is allowed to come once more, but still adiabatically, to equilibrium (which means experimentally that macroscopic quantities such as pressure or magnetization are no longer varying), so that a new experimental entropy $S_{\mathrm{e}}{ }^{\prime}$ can be defined. If the time-developed distribution function $W_{N}\left(t^{\prime}\right)$ leads to a correct prediction of the new energy $U^{\prime}$ in the sense of (16), then the inequality (17) still holds. The fact that $H_{\mathrm{G}}$ is a constant of the motion then gives $S_{\mathrm{e}} \leq S_{\mathrm{e}}{ }^{\prime}$, which is the second law.

## V. INTUITIVE MEANING OF THE SECOND LAW

The above proof has the merit of being almost unbelievably short, but partly for that reason, the physical basis of the second law is not made clear. In the following we are not trying to give a rigorous mathematical demonstration; that has just been done. We are trying rather to exhibit the basic intuitive reason for the second law. We recall Boltzmann's original conception of entropy as measuring the logarithm of phase volume associated with a macroscopic state. If Boltz-
mann's interpretation $S=k \log W$ is to be compatible with Gibbs' $S=-k H_{\mathrm{G}}$, it must be true that the quantity $W \equiv \exp \left(-H_{\mathrm{G}}\right)$ measures, in some sense, the phase volume of "reasonably probable" microstates.

Such a connection can be established as follows. Define a "high-probability" region $R$ of phase space, consisting of all points where $W_{N} \geq C$, and choose the constant $C$ so that the total probability of finding the system somewhere in this region is $(1-\epsilon)$, where $0<\epsilon<1$. Call the phase volume of this region $W(\epsilon)$; in equations,

$$
\begin{aligned}
\int_{R} W_{N} d \tau & =1-\epsilon \\
\int_{R} d \tau & =W(\epsilon)
\end{aligned}
$$

Evidently, with a continuously varying probability density $W_{N}$, it is not strictly meaningful to speak of the "phase volume of an ensemble," without qualifications; but the "minimum phase volume of $50 \%$ probability" or the "minimum phase volume of $99 \%$ probability" do have precise meanings.

A remarkable limit theorem first noted by Shannon ${ }^{5}$ shows that for most purposes the particular probability level $\epsilon$ is unimportant. We quote the result without proof; it is an adaptation of the fundamental "asymptotic equipartition property" (AEP) of Information Theory. ${ }^{6}$ We suppose that the distribution function $W_{N}$ from which $H_{\mathrm{G}}$ and $W(\epsilon)$ are computed is either a canonical distribution or a timedeveloped version of one resulting from some dynamical perturbation; and that the system is such that the canonical ensemble predicts relative fluctuations in energy which tend to zero as $N^{-1 / 2}$ in the "thermodynamic limit" as $N \rightarrow \infty$ at constant density. The Gibbs $H$ per particle, $H_{\mathrm{G}} / N$, then approaches a definite limit, and

$$
\begin{equation*}
\lim _{N \rightarrow \infty}\left\{\left[H_{\mathrm{G}}+\log W(\epsilon)\right] / N\right\}=0 \tag{18}
\end{equation*}
$$

[^2]provided $\epsilon$ is not zero or unity. The principal feature of this theorem, at first sight astonishing, is that the result is independent of $\epsilon$. Changing $\epsilon$ does, of course, change $W(\epsilon)$; and generally by an enormous factor. But the change in $\log W(\epsilon)$ grows less rapidly than $N$, and in the limit it makes no difference.

The intuitive meaning of this theorem is that the Gibbs II does measure the logarithm of phase volume of reasonably probable microstates and, remarkably, for a large system the amount per particle, $\log W(\epsilon) / N$, becomes independent of just what we mean by "reasonably probable." We are thus able to retain Boltzmann's original formula, $S=k \log W$, which is seen to be precisely related to the Gibbs II, not the Boltzmann one.

With this interpretation of entropy, let us reconsider the above experiment. At time $t=0$, we measure a number of macroscopic parameters $\left\{X_{1}(0), \cdots, X_{n}(0)\right\}$ adequate to define the thermodynamic state. The corresponding canonical distribution determines a high-probability region $R_{0}$, of phase volume $W_{0}$. The aforementioned variational property of the canonical ensemble now implies that, of all ensembles agreeing with this initial data in the sense of (16), the canonical one defines the largest high-probability region. The phase volume $W_{0}$ therefore describes the full range of possible initial microstates; and not some arbitrary subset of them; this is the basic justification for using the canonical distribution to describe partial information.

On the "subjective" side, we can therefore say that $W_{0}$ measures our degree of ignorance as to the true unknown microstate, when the only information we have consists of the macroscopic thermodynamic parameters; a remark first made by Boltzmann.

But, and perhaps more pertinent, we can also say on the "objective" side, that $W_{0}$ measures the degree of control of the experimenter over the microstate, when the only parameters he can manipulate are the usual macroscopic ones. On successive repetitions of the experiment, the initial microstate will surely not be repeated ; it will vary at random over the high-probability region $R_{0}$.

When we carry out an adiabatic change of state, the region $R_{0}$ is transformed, by the equations of motion, into a new region $R_{t}$. From
either the constancy of $H_{\mathrm{Q}}$, or directly from Liouville's theorem, the phase volume remains unchanged; $W_{\imath}=W_{0}$. Each possible initial microstate in $R_{0}$ uniquely determines a possible final one in $R_{t}$, and on successive repetitions of the experiment, the final state varies over $R_{i}$ at random.

At the end of this experiment, under the new equilibrium conditions, we note the new values $\left\{X_{1}(t), \cdots, X_{n}(t)\right\}$ of the thermodynamic quantities. Now consider the region $R^{\prime}$, consisting of all microstates that are compatible with these new $X_{i}(t)$, whether or not they could have resulted from the experiment just described; i.e., whether or not they also lie in $R_{t}$. By (17) and (18), the final experimental entropy is $S_{e}{ }^{\prime}=k \log W^{\prime}$, where $W^{\prime}$ is the phase volume of $R^{\prime}$; the experimental entropy is a measure of all conceivable ways in which the final macrostate can be realized, and not merely of all ways in which it could be produced in one particular experiment.

Now it is obvious that, if the observed change of state $X_{i}(0) \rightarrow X_{i}(t)$ is to be experimentally reproducible, the region $R_{t}$ resulting from the experiment must be totally contained in $R^{\prime}$. But this is possible only if the phase volumes satisfy $W_{t} \leq W^{\prime}$, which is again the second law!

At this point, we finally see the real reason for the second law; since phase volume is conserved in the dynamical evolution, it is a fundamental requirement on any reproducible process that the phase volume $W^{\prime}$ compatible with the final state cannot be less than the phase volume $W_{0}$ which describes our ability to reproduce the initial state.

But this argument has given us more than the second law; in the past the notion "experimental entropy" has been defined, in conventional thermodynamics, only for equilibrium states. It is suddenly clear that the second law is only a very special case of a general restriction on the direction of any reproducible process, whether or not the initial and final states are describable in the language of thermodynamics; the expression $S=k \log W$ gives a generalized definition of entropy applicable to arbitrary nonequilibrium states, which still has the property that it can only increase in a reproducible experiment. This can be shown directly from Liouville's theorem, without any consideration of canonical distributions or the asymptotic equipartition theorem.

Finally, it is clear that this extension of the second law can be subjected to experimental tests.

Returning to the case of equilibrium thermodynamics, these considerations (which are easily extended ${ }^{1}$ to quantum statistics) lead us to state the conventional second law in the form: The experimental entropy cannot decrease in a reproducible adiabatic process that starts from a state of complete thermal equilibrium.

The necessity of the last proviso is clear from a logical standpoint in our derivation of the second law in Sec. IV; for if the preparation of the system just before $t=0$ imposes any constraints other than those implied by the canonical distribution, the manifold of possible initial states will be reduced below $W_{0}$, and we shall not have an equality in Eq. (17) initially. This necessity is also shown strikingly from an experimental standpoint in the phenomenon of spin echos, ${ }^{7,8}$ which is a gross violation of any statement of the second law that fails to specify anything about the past history of the system. This proviso has not been particularly emphasized before, but it has always been obvious that some such condition would be needed before we had a really air-tight statement of the second law, which could not be violated by a clever experimenter. The future behavior of the system is uniquely determined, according to the laws of mechanics, only when one has specified perhaps $10^{24}$ microscopic coordinates and momenta; it could not possibly be determined merely by the values of the three or four quantities measured in typical thermodynamic experiments.

Specifying "complete thermal equilibrium" is still not as precise a statement as we might wish. Experimentally, the only criterion as to whether it is satisfied seems to be that the system is "aged," i.e., that it is quiescent, the macroscopic quantities $X_{i}$ unchanging, for a sufficiently long time; and only experience can tell the experimenter how long is "sufficiently long."

Theoretically, we can understand this requirement as meaning that, for purposes of prediction, lack of knowledge of the present microstate can be, in part, compensated by knowledge of the past history of the macroscopic state. As we

[^3]observe the system to be quiescent for a longer and longer time, we become more and more confident that it is not in an atypical microstate that will lead to "abnormal" behavior in the future. In Hahn's experiment ${ }^{7}$ the spin system, having no observable net magnetization at time $t=0$, is nevertheless able to develop, spontaneously and almost magically, a large and reproducible magnetization at a later time only because it "remembers" some very atypical things that were done to it before $t=0$.

In this observation lies the clue that shows how to extend the mathematical methods of Gibbs to a general formalism for predicting irreversible phenomena; we must learn how to construct ensembles which describe not only the present values of macroscopic quantities, but also whatever information we have about their past behavior. The details of this generalization will be given elsewhere.

## VI. THE "ANTHROPOMORPHIC" NATURE OF ENTROPY

After the above insistence that any demonstration of the second law must involve the entropy as measured experimentally, it may come as a shock to realize that, nevertheless, thermodynamics knows of no such notion as the "entropy of a physical system." Thermodynamics does have the concept of the entropy of a thermodynamic system ; but a given physical system corresponds to many different thermodynamic systems.

Consider, for example, a crystal of Rochelle salt. For one set of experiments on it, we work with temperature, pressure, and volume. The entropy can be expressed as some function $S_{\mathrm{c}}(T, P)$. For another set of experiments on the same crystal, we work with temperature, the component $e_{x y}$ of the strain tensor, and the component $P_{z}$ of electric polarization; the entropy as found in these experiments is a function $S_{\mathrm{c}}\left(T, e_{x y}, P_{z}\right)$. It is clearly meaningless to ask, "What is the entropy of the crystal?" unless we first specify the set of parameters which define its thermodynamic state.

One might reply that in each of the experiments cited, we have used only part of the degrees of freedom of the system, and there is a "true" entropy which is a function of all these
parameters simultaneously. However, we can always introduce as many new degrees of freedom as we please. For example, we might expand each element of the strain tensor in a complete orthogonal set of functions $\varphi_{k}(x, y, z)$

$$
e_{i j}(x, y, z)=\sum_{k} a_{i j k} \varphi_{k}(x, y, z)
$$

and by a sufficiently complicated system of levels, we could vary each of the first 1000 expansion coefficients $a_{i j k}$ independently. Our crystal is now a thermodynamic system of over 1000 degrees of freedom ; but we still believe that the laws of thermodynamics would hold. So, the entropy must be a function of over 1000 independent variables. There is no end to this search for the ultimate "true" entropy until we have reached the point where we control the location of each atom independently. But just at that point the notion of entropy collapses, and we are no longer talking thermodynamics!

From this we see that entropy is an anthropomorphic concept, not only in the well-known statistical sense that it measures the extent of human ignorance as to the microstate. Even at the purely phenomenological level, entropy is an anthropomorphic concept. For it is a property, not of the physical system, but of the particular experiments you or I choose to perform on it.

This points up still another qualification on the statement of the second law without which it is, strictly speaking, no law at all. If we work with a thermodynamic system of $n$ degrees of freedom, the experimental entropy is a function $S_{\mathrm{e}}\left(X_{1} \cdots X_{n}\right)$ of $n$ independent variables. But the physical system has any number of additional degrees of freedom $X_{n+1}, X_{n+2}$, etc. We have to understand that these additional degrees of freedom are not to be tampered with during the experiments on the $n$ degrees of interest; otherwise one could easily produce apparent violations of the second law.

For example, the engineers have their "steam tables," which give measured values of the entropy of superheated steam at various temperatures and pressures. But the $\mathrm{H}_{2} \mathrm{O}$ molecule has a large electric dipole moment; and so the entropy of steam depends appreciably on the
electric field strength present. It must always be understood implicitly (because it is never stated explicitly) that this extra thermodynamic degree of freedom was not tampered with during the experiments on which the steam tables are based; which means, in this case, that the electric field was not inadvertently varied from one measurement to the next.

Recognition that the "entropy of a physical system" is not meaningful without further qualifications is important in clarifying many questions concerning irreversibility and the second law. For example, I have been asked several times whether, in my opinion, a biological system, say a cat, which converts inanimate food into a highly organized structure and behavior, represents a violation of the second law. The answer I always give is that, until we specify the set of parameters which define the thermodynamic state of the cat, no definite question has been asked!

It seems apparent, in view of complications which we have encountered in the attempt to give a complete statement of the second law, that much more work needs to be done in this field. Glib, unqualified statements to the effect that "entropy measures randomness" are in my opinion totally meaningless, and present a serious barrier to any real understanding of these problems. A full resolution of all the questions that can be raised requires a much more careful analysis than any that has been attempted thus far. Perhaps the most difficult problem of all is to learn how to state clearly what is the specific question we are trying to answer? However, I believe that in the above arguments we have been able to report some progress in this direction.

## VII. ACKNOWLEDGMENTS

I have profited from discussions of these problems, over many years, with Professor E. P. Wigner, from whom I first heard the remark, "Entropy is an anthropomorphic concept." It is a pleasure to thank Professor Wm. C. Band for reading a preliminary draft of this article, and suggesting an important clarification of the argument.


[^0]:    * Supported by the National Science Foundation Grant NSF G23778.
    ${ }^{1}$ Statistical Physics (1962 Brandeis Theoretical Physics Lectures, Vol. 3), edited by K. W. Ford (W. A. Benjamin, Inc., New York, 1963), Chap. 4. Note that typographical errors occur in Eqs. 20, 49, 74, 78, 94, and the inequality preceding Eq. 90.
    ${ }^{2}$ P. Ehrenfest and T. Ehrenfest, Encykl. Math. Wiss., IV 2, II, Issue 6 (1912). Reprinted in Paul Ehrenfest, Collected Scientific Papers, edited by M. J. Klein (NorthHolland Press, Amsterdam, 1959). English translation by M. J. Moravcsik, The Conceptual Foundations of the Statistical Approach in Mechanics (Cornell University Press, Ithaca, New York, 1959).

[^1]:    ${ }^{3}$ A notable exception is the monumental work of R. C. Tolman, The Principles of Statistical Mechanics (Oxford University Press, London, 1938). Tolman repeatedly stresses the superiority of Gibbs' approach, although he still attempts to base the second law on coarse-graining.

[^2]:    ${ }^{4}$ E. T. Jaynes, Phys. Rev. 108, 171 (1957).
    ${ }^{5}$ C. E. Shannon, Bell Syst. Tech. J. 27, 379, 623 (1948) ; reprinted in C. E. Shannon and W. Weaver, The Mathematical Theory of Communication (University of Illinois Press, Urbana, Illinois, 1949). See, particularly, Sec. 21.
    ${ }^{6}$ A. Feinstein, Foundations of Information Theory (McGraw-Hill Book Company, Inc., New York, 1958), Chap. 6.

[^3]:    ${ }^{7}$ E. L. Hahn, Phys. Rev. 80, 580 (1950).
    ${ }^{8}$ A. L. Bloom, Phys. Rev. 98, 1104 (1955).

