# Relaxation processes in a low-order three-dimensional magnetohydrodynamics model 

Troy Stribling and William H. Matthaeus<br>Bartol Research Institute, University of Delaware, Newark, Delaware 19716

(Received 16 November 1990; accepted 2 April 1991)


#### Abstract

The selective decay and dynamic alignment relaxation theories are used to interpret the time asymptotic behavior of a Galerkin model of three-dimensional (3-D) magnetohydrodynamics (MHD). A large number of simulations are performed that scan a parameter space defined by the rugged ideal invariants: energy, cross helicity, and magnetic helicity. Ranges of the initial parameters are found where one or both of the relaxation theories are needed to describe the time asymptotic properties of the system, as previously found in analogous studies of twodimensional (2-D) MHD [Ting et al., Phys. Fluids 29, 3261 (1986)]. In many cases, the time asymptotic state can be interpreted as a relaxation to minimum energy. For certain parameter ranges spectral back transfer of cross helicity can lead to growth in velocity-magnetic field correlation [Stribling and Matthaeus, Phys. Fluids B 2, 1979 (1990)]. A simple decay model, based on absolute equilibrium theory, predicts a mapping of initial onto time asymptotic states, and accurately describes the long time behavior of the runs when magnetic helicity is present. We also discuss two processes, operating on time scales shorter than selective decay and dynamic alignment, in which the ratio of kinetic to magnetic energy relaxes to values $O(1)$. The faster of the two takes states initially dominant in magnetic energy to a state of nearequipartition between kinetic and magnetic energy through power law growth of kinetic energy. The other process takes states initially dominant in kinetic energy to the nearequipartitioned state through exponential growth of magnetic energy.


## I. INTRODUCTION AND BACKGROUND

While the study of magnetohydrodynamic (MHD) turbulence is far less well developed than its simpler hydrodynamic counterpart, ${ }^{1}$ there continues to be strong interest in its application to a variety of problems in laboratory plasma physics, ${ }^{2-5}$ astrophysics, ${ }^{6-9}$ space physics, ${ }^{10-13}$ and classical dynamo theory. ${ }^{14,15}$ A common feature of many of these studies is the central role played by relaxation processes, usually driven by turbulence, which are invoked to explain the evolution of the magnetofluid toward configurations or statistical states that are in some sense predictable. For homogeneous MHD turbulence, as well as MHD turbulence in certain bounded configurations, two such relaxation process have been particularly widely investigated, both in terms of application to physical systems, and in terms of fundamental MHD theory. These are the selective decay process, ${ }^{3,16}$ in which the magnetofluid evolves toward long wavelength states dominated by magnetic (and possibly helical) excitations, and the dynamic alignment process, ${ }^{12,17,18}$ in which the plasma flow velocity and magnetic field become highly correlated. ${ }^{17}$ For the case of two-dimensional (2-D) incompressible MHD, the balance between these effects has been studied extensively, using analytical arguments and both high and low spatial resolution direct numerical simulations. ${ }^{19}$ Simulations also indicate a similar interplay between selective decay and dynamic alignment in low Mach number compressible 2-D MHD. ${ }^{20}$

Current theoretical perspectives on three-dimensional (3-D) MHD turbulence are largely based on analogies with hydrodynamic theory, ${ }^{1}$ generalizations of extremal energy
principles, ${ }^{3,2,21}$ statistical mechanics considerations, ${ }^{22-24}$ closures, ${ }^{25,18}$ and extensions of Kolmogorov phenomenology. ${ }^{26,12}$ Numerical studies, which have played an increasingly important role in both discovery and testing of these ideas, have been employed to describe the essential properties of MHD decay, ${ }^{27}$ dynamic alignment, ${ }^{17.28,29}$ and turbulent dynamo action. ${ }^{30}$ Investigation of 3-D relaxation in laboratory devices also depended greatly on direct simulation. ${ }^{4,5,31,32}$ While specific relaxation mechanisms have been frequently invoked in a number of these studies, we are unaware of any investigations that have addressed the issue of the interplay of distinct relaxation processes in a single MHD system. Of particular importance is to identify the nature of the relaxation as the global parameters that govern the relative importance of each mechanism are varied. The difficulty in examining this issue is considerably greater in 3D than in 2D, owing to the need for much greater computing requirements. Even with the notable increase in available computing power in recent years, a parameter space scan of several hundred high Reynolds number 3-D MHD computations, with sufficient spatial resolution to accurately compute all relevant dynamically important spatial scales, appears to be beyond our current abilities. The expense of such a study remains prohibitive at present, even for the simplest MHD systems in periodic geometry and with simplifying assumptions such as incompressibility and scalar dissipation coefficients.

In the present paper, we address the issue of the balance between selective decay and dynamic alignment processes, as well as other turbulence processes, in 3-D MHD, by mak-
ing a severe, but perhaps necessary, compromise with the basic physics of turbulence. The system we consider is a loworder Fourier space truncation of the full dynamical representation of periodic MHD. The number of Fourier degrees of freedom retained (several hundred) is somewhat greater than the few modes often retained in "dynamical systems" treatments of convection ${ }^{33}$ and other systems, but is far less than the number that would be needed at even moderately large Reynolds number if the Kolmogorov dissipation scales ${ }^{1}$ are to be resolved. This strategy allows us to fully scan the relevant parameter space of initial values of the rugged invariants (see below), following a large number of runs from their initial states to their time asymptotic "relaxed" states in which dynamical evolution is either terminated or has become a simple linear decay problem. This approach has obvious limitations with regard to quantitative application to realistic systems involving plasma turbulence. However, since we are able to fully study this oversimplified model, we can hope to provide physical insights that may be useful in studying realistic MHD turbulence.

We investigate relaxation processes in a three-dimensional, decaying, constant density magnetohydrodynamics (MHD) model, which in an appropriate set of dimensionless units, takes the form

$$
\begin{align*}
& \frac{\partial \mathbf{v}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{v}=-\nabla p^{*}+\mathbf{b} \cdot \nabla \mathbf{b}+\nu \nabla^{2} \mathbf{v},  \tag{1a}\\
& \frac{\partial \mathbf{b}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{b}=\mathbf{b} \cdot \nabla \mathbf{v}+\eta \nabla^{2} \mathbf{b},  \tag{1b}\\
& \nabla \cdot \mathbf{v}=0,  \tag{lc}\\
& \nabla \cdot \mathbf{b}=0 . \tag{ld}
\end{align*}
$$

The velocity and magnetic fields, $\mathbf{v}$ and $\mathbf{b}$, are written in Alfvén speed units, $p^{*}$ is the total pressure, determined by a Poisson equation when use is made of incompressibility, Eq. (1c). The viscosity $v$ and resistivity $\eta$ are the reciprocals of the nominal mechanical and magnetic Reynolds numbers, respectively. The time unit is taken to be an eddy turnover time for unit velocity field at unit length scale.

Using the Galerkin approximation, the $\mathbf{v}$ and $\mathbf{b}$ fields, assumed to be periodic in a 3-D box with sides of dimensionless length $2 \pi$, are expressed as

$$
\begin{align*}
& \mathbf{v}(\mathbf{x}, t)=\sum_{\mathbf{k} \in \mathbf{N}} \mathbf{v}(\mathbf{k}, t) \exp (i \mathbf{k} \cdot \mathbf{x})  \tag{2a}\\
& \mathbf{b}(\mathbf{x}, t)=\sum_{\mathbf{k} \in \mathbf{N}} \mathbf{b}(\mathbf{k}, t) \exp (i \mathbf{k} \cdot \mathbf{x}) \tag{2b}
\end{align*}
$$

where $\mathbf{N}$ is the truncation set of 3-D wave vectors $\mathbf{k}$ with integral components such that $k_{\text {min }} \leqslant|\mathbf{k}| \leqslant k_{\text {max }}$. The number of vectors in $\mathbf{N}$ will be denoted by $N$. The model studied is low order, in the sense that wave vectors in the truncation set all have magnitudes less than the dissipation wave number.

The rugged invariants are those quantities conserved by the nonlinear terms in Eq. (1) when summed over any interacting triad of wave vectors (i.e., any $m, n$, and $k$ such that $\mathbf{m}+\mathbf{n}=\mathbf{k}$ ). Thus the rugged invariants are conserved for arbitrary truncations of the discrete Fourier series representing the $\mathbf{v}$ and $\mathbf{b}$ fields when $v=\eta=0$ in Eq. (1). There are
believed to be only three rugged invariants for 3-D MHD. ${ }^{24}$ These quantities play a central role in interpretation of the qualitative and time asymptotic behavior of the solutions to Eq. (1). They are the energy $E$, the cross helicity $H_{c}$, and the magnetic helicity $H_{m}$, each expressed as a "per unit mass" quantity, and defined by

$$
\begin{align*}
E= & \frac{1}{2 V} \int\left(|\mathbf{v}|^{2}+|\mathbf{b}|^{2}\right) d^{3} x \\
= & \frac{1}{2} \sum_{\mathbf{k} \in \mathbf{N}}\left[|\mathbf{v}(\mathbf{k})|^{2}+|\mathbf{b}(\mathbf{k})|^{2}\right]=E_{v}+E_{b}  \tag{3a}\\
H_{c}= & \frac{1}{2 V} \int \mathbf{v} \cdot \mathbf{b} d^{3} x \\
= & \frac{1}{4} \sum_{\mathbf{k} \in \mathbf{N}}\left[\mathbf{v}(\mathbf{k}) \cdot \mathbf{b}^{*}(\mathbf{k})+\mathbf{v}^{*}(\mathbf{k}) \cdot \mathbf{b}(\mathbf{k})\right]  \tag{3b}\\
H_{m}= & \frac{1}{2 V} \int \mathbf{a} \cdot \mathbf{b} d^{3} x= \\
& \quad \frac{1}{4} \sum_{\mathbf{k} \in \mathbf{N}} \frac{i}{k^{2}}\left\{[\mathbf{k} \times \mathbf{b}(\mathbf{k})] \cdot \mathbf{b}^{*}(\mathbf{k})\right.  \tag{3c}\\
& \left.\quad-\left[\mathbf{k} \times \mathbf{b}^{*}(\mathbf{k})\right] \cdot \mathbf{b}(\mathbf{k})\right\}
\end{align*}
$$

The integrals are evaluated over a box of volume $V=(2 \pi)^{3}$, $E_{v}$ and $E_{b}$ are the kinetic and magnetic energy per unit mass, respectively, and * denotes complex conjugation.

## II. EXTREMAL ENERGY STATES AND THE GENERAL MHD RELAXATION PROBLEM

In ordinary hydrodynamic turbulence, energy spreads in wave number under the influence of nonlinear couplings, with the net transfer being toward shorter wavelengths, in view of the greater available phase space and the removal of energy at the high wave numbers. Significantly different possibilities exist for spectral transfer in systems such as 2-D hydrodynamics ${ }^{34}$ that have additional rugged invariants. Kraichnan advanced arguments, ${ }^{35}$ based on ideal absolute equilibrium statistical mechanics, to the effect that, in steady dissipative turbulence, the energy cascade is toward lower wave number, while the cascade of the enstrophy proceeds toward higher wave number. This basic idea, that two rugged invariants might admit distinct preferential directions of spectral transfer in nonequilibrium circumstances, has also been extended to other fluid systems, ${ }^{34,36}$ and to decaying turbulence. In fluid systems with two or more ruggedly conserved quantities, at least one of which is back-transferred, selective decay theory ${ }^{3,16}$ predicts that turbulence drives the system to a state in which the ratios of back-transferred to forward-transferred quantities are maximized. The properties of the time asymptotic state can be found by construction of a variational principle that minimizes the forwardtransferred quantity under the constraint that the back-transferred quantities are fixed.

For example, if cross helicity is taken to be zero, 3-D MHD ruggedly conserves $E$ and $H_{m}$, and the prediction, based on equilibrium ensemble theory ${ }^{24}$ is that $H_{m}$ is backtransferred and $E$ forward-transferred. In the selective decay picture, this notion of preferential directions of transfer in wave number space is extended to freely decaying flows, and the variational principle prescription ${ }^{3}$ for determining the time asymptotic state indicates that one minimizes $E$ while
constraining $H_{m}$ to be fixed. Thus one finds a uniquely defined time asymptotic rugged invariant ratio $\left|H_{m}\right| / E=1 / k_{\min }$ for periodic boundary conditions. The selective decay conjecture is that all initial conditions approach this ratio after a sufficiently long time when turbulence is active and the dissipation coefficients are very small. The original application of the selective decay idea ${ }^{3}$ was to provide a dynamical framework, based on turbulent spectral transfer, for the final states of MHD flow in cylindrical geometry with perfectly conducting boundary conditions conjectured by Taylor ${ }^{2}$ to explain properties of reversed-field pinch devices. Although selective decay predictions are typically phrased in terms of properties of the final states, an alternative view that emphasizes the dynamical character of the process is that turbulence causes a persistent inequality in the decay rates of the rugged invariants, so that $E^{-1}|d E / d t| \gg\left|H_{m}^{-1} d H_{m} / d t\right|$.

The dynamic alignment process causes an inequality in the relative decay rates of the other two rugged invariants $E$ and $H_{c}$, which will lead to growth of the normalized velocity and magnetic field correlation $2 H_{c} / E$ in both 2-D and 3-D MHD. ${ }^{12,17,18,28,29}$ Generally speaking, previous treatments have not considered $H_{c}$ to be back-transferred in wave number and have ignored $H_{m}$ back-transfer (i.e., have assumed $H_{m}=0$ ), but offered various arguments to the effect that the decay rate of $H_{c}$ is suppressed to values lower than $|d E / d t|$ by other MHD turbulence processes. ${ }^{12,17,18}$ Thus the minimum energy prescription can still be employed, somewhat trivially, to describe the time asymptotic properties of a dynamically aligning system without back transfer. Minimizing $E$ subject to constant $H_{c}$ results in the conclusion that $2\left|H_{c}\right| / E=1$ and $E_{v}=E_{b}$ in the postulated final state. When $H_{m} \neq 0$, so that its back-transfer strongly influences the systems dynamics, there is a possibility that $H_{c}$ is back-transferred. ${ }^{37}$ This also could lead to growth of $2 H_{c} / E$, which would occur in addition to any growth incurred by the $H_{m} \neq 0$ processes. This topic is discussed further in following sections.

The selective decay and dynamic alignment processes can act simultaneously, and drive the system to a minimal energy state. The general relaxation problem, which accounts for the contribution of both the processes in the determination of the time asymptotic state in 2-D MHD, was discussed by Ting et al. ${ }^{19}$ for periodic boundary conditions and unit magnetic Prandtl number. There are three rugged invariants in 2-D MHD, as in 3D, but magnetic helicity conservation is replaced by conservation of the mean square vector potential $A$, which is back-transferred. If the appropriate variational principle is constructed, one that minimizes $E$ with the constraints of constant $H_{c}$ and $A$, it is found that the states that minimize the energy lie on an ellipse in a parameter space with coordinates $A / E$ and $2 H_{c} / E .^{19}$ The states on the ellipse have in common that $A / E_{b}=1 / k_{\text {min }}^{2}$ and $H_{c}=\sqrt{E_{v} E_{b}} ; E_{v}$ and $E_{b}$ are the kinetic and magnetic energy, respectively. What differs in the one-parameter family of minimum energy states is the ratio $E_{v} / E_{b}$, which varies continuously from 0 to 1 . Thus there are an infinite number of final states, distinguished according to their spectral characteristics, and the theory does not determine a unique final
state. (Ambiguities associated with the phase of Fourier coefficients are not of concern here.) This is in contrast to the case with two rugged invariants, where the extremization theory determines uniquely the spectral properties of the final state.

Ting et al. ${ }^{19}$ examined 2-D MHD relaxation by scanning the $A / E, 2 H_{c} / E$ parameter space, performing a large number of runs with both low order and fully resolved codes. The simulations led to a classification of regions of the parameter space, according to the degree of influence of selective decay and dynamic alignment, and the nature of the computed time asymptotic states. For two of the described regions, the simulations led to final states accurately described by the minimum energy principle. They also found that initial states in one region of the $A / E, 2 H_{c} / E$ parameter space relaxed to states that maximized the constrained energy integral. This region appears not to exist in 3-D MHD. In a later section possible reasons for its disappearance will be discussed.

The general relaxation problem in 3D depends upon boundary conditions and the magnetic Prandtl number, and will be very difficult to solve if simplifying assumptions are not made. In this work periodic boundary conditions and unit magnetic Prandtl number will be assumed, as in the Ting et al. ${ }^{19}$ study. To determine the regions of influence of selective decay and dynamic alignment by numerically solving Eq. (1) for initial conditions that scan an appropriate parameter space with codes that resolve high Reynolds number flow is beyond the capability of present day computers. It is for this reason that we have chosen to investigate a loworder 3-D system to determine the applicability and possible extensions of relaxation theories that qualitatively describe the long time behavior of decaying 2-D MHD systems.

The properties of minimal energy states for 3-D MHD with periodic boundary conditions are determined by solving the variational problem

$$
\begin{equation*}
\delta \int\left(|\mathbf{v}|^{2}+|\mathbf{b}|^{2}-\frac{\alpha}{2} \mathbf{v} \cdot \mathbf{b}+\varphi \mathbf{a} \cdot \mathbf{b}\right) d^{3} x=0 \tag{4}
\end{equation*}
$$

where $-\alpha / 2$ and $\varphi$ are Lagrange multipliers and $\mathbf{b}=\nabla \times \mathbf{a}$. The Euler-Lagrange equations can readily be shown to give the field equations

$$
\begin{equation*}
\mathrm{v}=\alpha \mathrm{b}, \tag{5a}
\end{equation*}
$$

$$
\begin{equation*}
\varphi \mathbf{b}+\nabla \times \mathbf{b}-\alpha \nabla \times \mathbf{v}=0 . \tag{5b}
\end{equation*}
$$

Since $\alpha$ is real, Eq. (5a) implies that v and $\mathbf{b}$ are pointwise aligned or antialigned in the fluid. Combining Eqs. (5a) and (5b) gives

$$
\begin{equation*}
\nabla \times \mathbf{b}=\left[\varphi /\left(\alpha^{2}-1\right)\right] \mathbf{b} ; \tag{6}
\end{equation*}
$$

thus the current density is aligned or antialigned to b for $\alpha^{2} \neq 1$, since $\varphi$ is also real; hence the state is force-free. Equations similar to Eqs. (5) follow from extremization of energy integrals, like the one given by Eq. (4), for 2-D periodic MHD, ${ }^{19}$ 3-D MHD in a cylindrical geometry with infinitely conducting boundaries, ${ }^{2}$ and in force-free equilibria of 2-D two-fluid plasma models. ${ }^{38}$

If periodic boundary conditions are assumed two things
follow from Eq. (6): The only nonzero Fourier coefficients have wave vectors with magnitude $k_{o}$ given by

$$
\begin{equation*}
k_{o}=\left|\varphi /\left(\alpha^{2}-1\right)\right| ; \tag{7}
\end{equation*}
$$

and maximal magnetic helicity,

$$
\begin{equation*}
\left|H_{m}\right|=E_{b} / k_{o} . \tag{8}
\end{equation*}
$$

It is easily shown that

$$
\begin{align*}
& E=\left(1+\alpha^{2}\right) E_{b},  \tag{9a}\\
& H_{c}=\alpha E_{b} . \tag{9b}
\end{align*}
$$

Elimination of $E_{b}$ and $\alpha$ from Eqs. (8) and (9) gives

$$
\begin{equation*}
E=\left|H_{c}\right|\left[\left(k_{o}^{2}+h^{2}\right) / k_{o} h\right], \tag{10}
\end{equation*}
$$

where $h=\left|H_{c} / H_{m}\right|$.
Consider the set $\left\{k_{i}^{2}\right\}=\{1,2,3,4,5,6,8, \ldots\}$ consisting of the squares of wave-vector magnitudes in the set $\mathbf{N}$ of Fourier modes in the periodic box. Then we find that, for some $k_{i}^{2} \leftarrow\left\{k_{i}^{2}\right\}, k_{i}=k_{o}$, if

$$
\begin{equation*}
\sqrt{k_{i} k_{i-1}} \leqslant h \leqslant \sqrt{k_{i} k_{i+1} .} \tag{11}
\end{equation*}
$$

For $k_{o}=1$ to minimize $E$, Eq. (11) requires $\left|H_{c} / H_{m}\right| \leqslant 2^{1 / 4}$. Setting $k_{o}=1 \mathrm{in}$ Eq. (10) gives the two curves

$$
\begin{equation*}
\left(1-2\left|H_{m}\right| / E\right)^{2}+\left(2 H_{c} / E\right)^{2}=1, \tag{12}
\end{equation*}
$$

which are seen to be ellipses in a parameter space with coordinates $H_{m} / E$ and $2 H_{c} / E$ (see Fig. 1). The states that lie on the upper half of the $H_{m}>0$ ellipse and on the lower half of the $H_{m}<0$ ellipse minimize $E$ and have $E_{v} / E_{b} \leqslant 1$, with $H_{m}$ and $H_{c}$ constrained to be constant.

The ratio $E_{v} / E_{b}$ can be easily found as a function of $2 H_{c} / E$ on the two extremal energy ellipses by using the fact

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-04.jpg?height=819&width=830&top_left_y=1511&top_left_x=110)
FIG. 1. The rugged invariant parameter space is depicted. Special points on the boundary are labeled with the values of the rugged invariants at the respective points. The minimum energy curve is also indicated. The shaded region above the minimum energy curve is forbidden because of kinematic constraints on the rugged invariants.

that the velocity and magnetic fields are aligned (i.e., $H_{c} / \sqrt{E_{v} E_{b}}=1$ ). On the minimum energy portions of the ellipses with $E_{v} / E_{b} \leqslant 1$ it is found that

$$
\begin{equation*}
\frac{E_{v}}{E_{b}}=\frac{2}{\left(2 H_{c} / E\right)^{2}}\left[\left(1-\frac{\left(2 H_{c} / E\right)^{2}}{2}\right)+\sqrt{1-\left(2 H_{c} / E\right)^{2}}\right] . \tag{13}
\end{equation*}
$$

Thus the time asymptotic value of $E_{v} / E_{b}$ uniquely determines the location of the system on the minimum energy portions of the ellipses. However, at present we know of no method to determine this ratio apart from direct solution of the dynamical equations.

It should also be noted that the region of the $2 H_{c} / E$, $H_{m} / E$ parameter space that lies above the ellipses defined by Eq. (12), the shaded region in Fig. 1, is forbidden to the system because of kinematic constraints on the rugged invariants. Also, in the picture of the rugged invariant parameter space given in Fig. 1, values of the rugged invariants at special points on the boundary are indicated.

## III. LOW-ORDER TRUNCATION MHD MODEL

The model investigated had 62 independent wave vectors ( 496 independent degrees of freedom) that were distributed within a cube in $k$ space with $k_{\text {min }}=1$ and $k_{\text {max }}=\sqrt{12}$. Time integration was performed by a second-order RungeKutta method with a time step of 0.01 eddy turnover times. In an ideal run with unit energy and $v=\eta=0$, the system conserved total energy to four significant figures after 1000 eddy turnover times.

Approximately 160 runs were performed out to times $t_{\text {final }}$ ranging from 100 to 200 eddy turnover times. The initial condition for each run was determined by selecting values for $E_{v} / E_{b}, H_{m} / E$, and $2 H_{c} / E$ for fixed spectral shapes (see below). The parameter $E_{v} / E_{b}$ was chosen first; then $H_{m} / E$ and $2 H_{c} / E$ were selected from the range of values to which they were constrained by the spectral shapes of $E, H_{m}$, and $H_{c}$. The ratio $E_{v} / E_{b}$ had values ranging from $10^{-6}$ to $10^{4}$. The remaining undetermined phases and vector directions of the Fourier coefficients were chosen randomly. The initial rugged invariant spectra were taken to be

$$
\begin{align*}
& E(\mathbf{k})=1 / N,  \tag{14a}\\
& H_{c}(\mathbf{k})=H_{c} / N,  \tag{14b}\\
& H_{m}(\mathbf{k})=\frac{H_{m}}{k}\left(\sum_{\mathbf{k} \in \mathbf{N}} \frac{1}{k}\right)^{-1}, \tag{14c}
\end{align*}
$$

where $E=1$ and $N$ is the total number of wave vectors in the truncation. For all runs $\eta=v=0.01$.

## IV. RELAXATION TO NEAR-EQUIPARTITION STATE BETWEEN KINETIC AND MAGNETIC ENERGY

In addition to selective decay and dynamic alignment, which determine the time asymptotic properties of decaying MHD, two other processes have been investigated, which operate on much shorter time scales. These two processes share the property that they occur for runs in which $E_{v}$ and $E_{b}$ are initially of greatly different magnitudes. In each case

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-05.jpg?height=960&width=651&top_left_y=92&top_left_x=126)
FIG. 2. Time history of $E_{v}$ during the fast relaxation process that involves temporal growth of this quantity. (a) Two runs with an initial value of $E_{c} / E_{b}=10^{-4}$. The solid curve began with a smaller $H_{m}$ than the dashed curve (b) Linear least-squares fit of $E_{c}$ to $t^{m}$. The simulation data are indicated by the circles and the fitted curve by the solid line. For this run $E_{c} \propto t^{1.92}$.

the computations show rapid relaxation to states in which $E_{v} / E_{b} \sim O(1)$, a condition that we refer to as near-equipartition of $E_{v}$ and $E_{b}$ (spectral equipartition in any form is not implied). Relaxation of the low-order Galerkin model to $E_{v} / E_{b} \sim O(1)$ is studied by performing many runs that scan the accessible regions of the parameter space depicted in Fig. 1.

The faster of the $E_{b} / E_{b}$ relaxation processes takes a system initially dominated by $E_{b}$ to a near-equipartitioned state
through growth of $E_{v}$. Figure 2(a) shows $E_{v}$ plotted as a function of time for two runs with initial $E_{0} / E_{b}=10^{-4}$. It can be seen that $E_{v}$ grows rapidly, reaching its maximum in a time near an eddy turnover time before decay begins. For the run with the larger initial magnetic helicity [Fig. 2(a), dotted curve] the maximum value of $E_{v}$ attained is less than that seen in the less helical run [Fig. 2(a), solid curve], and $E_{v}$ oscillates about its maximum value for a brief period before decaying. The time for $E_{v}$ to reach maximum, $t_{\text {max }}$, initial parameter values and the values of these parameters at $t_{\text {max }}$ are listed for eight runs in Table I. For each of the runs $1<t_{\max }<2$. The parameters $2 H_{c} / E$ and $H_{m} / E$ change very little from their initial value during the period of kinetic energy growth. This indicates that selective decay and dynamic alignment have negligible influence on the fast process that produces near-equipartition of $E_{v}$ and $E_{b}$, presumably because of the contrast in time scales. Selective decay and dynamic alignment are much slower processes.

From the table $E_{v} / E_{b}$ at $t_{\text {max }}$ is seen to be a decreasing function of the initial value of $H_{m} / E$. In Sec.VII an explanation for this is suggested by interpreting the approach to near-equipartition as relaxation toward the absolute equilibrium value of $E_{v} / E_{b}$. The latter ratio is a decreasing function of $H_{m} / E$. The computed relaxation saturates at values of $E_{v} / E_{b}$ near the absolute equilibrium values $\left(E_{v} / E_{b}\right)_{\text {eq }}$, which are computed from the initial values of $2 H_{c} / E$ and $H_{m} / E$ and also tabulated in the last column of Table I. For some of the runs in the table the saturation $E_{v} / E_{b}$ is accurately predicted by ( $\left.E_{v} / E_{b}\right)_{\text {eq }}$, with errors ranging from $4 \%$ to $29 \%$. Rapid growth of $E_{0}$ has been previously reported in pseudospectral 3-D MHD decay simulations of sufficient size to resolve the dissipation wave number. ${ }^{9}$ A saturation value of $E_{v} / E_{b} \approx 0.11$ was reported in Ref. 9 for a run with initial ratios $2 H_{c} / E \approx 0$ and $H_{m} / E=0.707$, for which we estimate $\left(E_{v} / E_{b}\right)_{\text {eq }}=0.17$.

The time dependence of the growth of $E_{v}$ can be accurately described by a power law. This is illustrated in Fig. 2(b), where a linear least-squares fit of $E_{n}$, to $t^{n}$ yields $n=1.92$. The exponent for a power law growth curve is listed in the fifth column of Table I for the eight runs mentioned above. The solution $E_{v} \propto t^{1.9}$ is found to be independent of the initial state for the simulations performed.

TABLE I. System parameters for $E_{p}$ growth runs.
| Initial value |  |  | $t_{\text {max }}$ | Exponent | Value at $t_{\text {max }}$ |  |  | $\left(E_{b} / E_{b}\right)_{\text {eq }}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $E_{t} / E_{b}$ | $2 H_{\mathrm{c}} / E$ | $H_{m} / E$ |  |  |  |  |  |  |
| $10^{-4}$ | $5 \times 10^{-3}$ | 0.01 | 1.6 | 1.92 | 1.02 | $1.57 \times 10^{-3}$ | $1.01 \times 10^{-2}$ | 0.98 |
| $10^{-5}$ | $6 \times 10^{-3}$ | 0.1 | 1.5 | 1.93 | 0.957 | $2.02 \times 10^{-3}$ | 0.104 | 0.818 |
| $10^{-6}$ | $10^{-3}$ | 0.1 | 1.5 | 1.93 | 1.06 | $4.28 \times 10^{-3}$ | 0.104 | 0.818 |
| $10^{-4}$ | $5 \times 10^{-3}$ | 0.156 | 1.475 | 1.92 | 0.791 | $5.17 \times 10^{-3}$ | 0.163 | 0.731 |
| $10^{-5}$ | $6 \times 10^{-3}$ | 0.2 | 1.38 | 1.93 | 0.735 | $9.06 \times 10^{-3}$ | 0.208 | 0.667 |
| $10^{\text {6 }}$ | $10^{-3}$ | 0.2 | 1.44 | 1.93 | 0.704 | $1.78 \times 10^{-3}$ | 0.208 | 0.667 |
| $10^{-4}$ | $5 \times 10^{-3}$ | 0.254 | 1.325 | 1.93 | 0.584 | $2.75 \times 10^{-3}$ | 0.262 | 0.595 |
| $10^{-4}$ | $5 \times 10^{-3}$ | 0.4 | 1.3 | 1.92 | 0.333 | $3.08 \times 10^{-3}$ | 0.412 | 0.429 |


![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-06.jpg?height=996&width=623&top_left_y=100&top_left_x=105)
FIG. 3. Time history of $E_{b}$ during the fast relaxation process that involves temporal growth of this quantity. (a) A run with an initial value of $E_{\mathrm{c}} / E_{b}=10^{4}$. (b) Linear least-squares fit of $E_{b}$ to $\exp (n t)$. The simulation data are indicated by the circles and the fitted curve by the solid line. For this run $E_{b} \propto \exp (0.56 t)$.

The second of the rapid relaxation processes to nearequipartition takes states initially dominated by $E_{v}$ to a state of near-equipartition with $E_{b}$ through growth of $E_{b}$. In Fig. $3(\mathrm{a}), E_{b}$ is plotted as a function of time for a run with initial $E_{v} / E_{b}=10^{4}$. It is seen that $E_{b}$ rapidly increases to its maximum value in about 20 eddy turnover times before decay begins. The time for $E_{b}$ to saturate $t_{\text {max }}$, initial parameter values, and their values at $t_{\text {max }}$ are listed in Table II for eight runs. For each of these runs $15<t_{\text {max }}<20$, a time about an order of magnitude larger than that discussed above for re-
laxation of $E_{v} / E_{b}$ through $E_{v}$ growth. Again, the rugged invariant ratios change very little from their initial values during the evolution to near equipartition. In this case, the difference in time scales of selective decay/dynamic alignment and the equipartition relaxation process is less striking than in the previous case. However, because $H_{m}$ and $H_{c}$ must be small whenever $E_{b}$ is initially small, back-transfer processes are expected to be weak in these cases, and changes of the ratios $H_{m} / E$ and $H_{c} / E$ induced by systematic spectral transfer are small over the time scale of equipartition.

As in the $E_{v}$ growth process, the process through which $E_{b}$ grows to near equality with $E_{v}$ can also be thought of, evidently, as driven by the tendency of $E_{v} / E_{b}$ to seek its absolute equilibrium value. ${ }^{39}$ For $H_{m}$ and $H_{c}$ small, one finds generally that $\left(E_{v} / E_{b}\right)_{\text {eq }} \approx 1$. In Table II the value $E_{v} / E_{b}$ at $t_{\max }$ is seen to lie between 1 and 3 for each of the runs. In Sec. VII this topic is discussed in more detail.

Here $E_{b}$ grows exponentially until it reaches its saturation value. This is illustrated in Fig. 3(b), where a linear least-squares fit of $E_{b}$ to $\exp (n t)$ yields the growth rate $n=0.56$. The fifth column of Table II gives the growth rate for the listed runs. In each case the $E_{b}$ growth rate is near $\frac{1}{2}$, the average over the eight runs being 0.51 , so that $E_{b} \propto \exp (t / 2)$ during the rapid growth toward near-equipartition.

## V. LONG TIME BEHAVIOR: SELECTIVE DECAY AND DYNAMIC ALIGNMENT

In this section we summarize the results of over 100 runs of the low-order 3-D MHD model that was carried out to investigate selective decay and dynamic alignment. Four runs that are considered typical, designated as runs $\mathrm{A}, \mathrm{B}, \mathrm{C}$, and D below, are reviewed in detail. The initial conditions were chosen to illustrate the different relaxation processes and their mechanisms. Initial and final run parameters are listed in Table III. In each run, Eq. (1) was integrated out to a time $t_{\text {final }}=100$, a decay time for the largest scales.

## A. Run A

This run began with $H_{m}$ large enough to induce strong back-transfer, so that selective decay is expected to influence

TABLE II. System parameters for $E_{b}$ growth runs.
| Initial value |  |  | $t_{\text {max }}$ | Growth rate | Value at $t_{\text {max }}$ |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $E_{c} / E_{b}$ | $2 H_{c} / E$ | $H_{m} / E$ |  |  | $E_{v} / E_{b}$ | $2 H_{c} / E$ <br> $H_{m} / E$ <br> $H_{m} / E$ |  |
| $10^{4}$ | 0.01 <br> 0.01 <br> $10^{-6}$ 10 | $2.54 \times 10^{-5}$ | 18.2 | 0.55 | 2.04 | $-1.48 \times 10^{-3}$ | $-6.08 \times 10^{-4}$ |
| $10^{4}$ |  | $4.0 \times 10^{5}$ |  | 15.2 | 0.59 | 1.31 | $5.45 \times 10^{-3}$ | $8.73 \times 10^{-3}$ |
| $10^{4}$ | $3.75 \times 10^{-3}$ <br> $6.25 \times 10^{-3}$ <br> $\quad 6.25 \times 10^{-3}$ | $4.0 \times 10^{-5}$ | 18.2 | 0.50 | 1.99 | $-1.92 \times 10^{-2}$ | $3.13 \times 10^{-3}$ |
| $10^{4}$ |  | $4.0 \times 10^{-5}$ | 19.0 | 0.45 | 1.46 | $4.85 \times 10^{-3}$ | $-8.20 \times 10^{-4}$ |
| $10^{4}$ | 0.01 <br> 0.01 | $4.0 \times 10^{-5}$ | 17.0 | 0.53 | 2.13 | $7.28 \times 10^{-3}$ | $-1.45 \times 10^{-3}$ |
| $10^{4}$ | $3.8 \times 10^{-2}$ <br> $6.3 \times 10^{-2}$ <br> $3.8 \times 10^{-2}$ | $1.56 \times 10^{-5}$ | 17.4 | 0.47 | 1.85 <br> $-2.71 \times 10^{-3}$ <br> $-4.14 \times 10^{-3}$ |  |  |
| $10^{4}$ |  | $1.56 \times 10^{-5}$ | 17.8 | 0.51 |  |  |  |
| $10^{4}$ | 0.01 | $1.56 \times 10^{-5}$ | 19.4 | 0.45 | 2.10 |  | $3.63 \times 10^{-2}-2.08 \times 10^{-3}$ |


TABLE III. System parameters for decay runs.
| Run | Initial value |  |  | $t_{\text {final }}$ | Value at $t_{\text {final }}$ |  |  |  |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|  | $E_{v} / E_{b}$ | $2 H_{c} / E$ | $H_{m} / E$ |  | $E_{0} / E_{b}$ | $2 H_{c} / E$ | $H_{m} / E$ | E |
| A | 1.0 | 0.0 | 0.2 | 100.0 | $4.54 \times 10^{-3}$ | $-3.17 \times 10^{-2}$ | 0.992 | $1.36 \times 10^{-2}$ |
| B | 1.0 | 0.8 | 0.0 | 100.0 | 1.07 | 0.983 | $3.42 \times 10^{-2}$ | $1.88 \times 10^{-3}$ |
| C | 0.5 | 0.6 | 0.2 | 100.0 | 0.317 | 0.852 | 0.757 | $3.04 \times 10^{-2}$ |
| D | 1.0 | 0.0 | 0.0 | 100.0 | 0.945 | 0.2 | $7.16 \times 10^{-2}$ | $4.43 \times 10^{-4}$ |


the evolution of the system. The initial $H_{c}=0.0$, so that dynamic alignment has negligible dynamical influence. In Fig. 4 a parametric plot in the $2 H_{c} / E, H_{m} / E$ parameter is given. The ratio $H_{m} / E$ is seen to grow to near its maximum value of 1 prior to $t_{\text {final }}$, verifying the most obvious prediction of selective decay. The ratio $2 H_{c} / E$ changes very little from its initial value, remaining far from its extremal values of $\pm 1$, indicating the absence of dynamic alignment. Figure 5 illustrates the evolution of various global quantities. The minimum energy principle discussed in Sec. II predicts a value of unity for $\left|H_{m}\right| / E_{b}$, a consequence of condensation of $E_{b}$ and $H_{m}$ into $k_{\text {min }}$, forming a long wavelength perfectly helical magnetic field. Figure 5(a) illustrates the approach of run $A$ to this helical state.

The dynamical evolution of the fractions of $E_{v}$ and $E_{b}$ residing in $k_{\text {min }}$ is an indicator of the effectiveness of spectral back-transfer. The temporal behavior of these fractions, designated as $E_{v}\left(k_{\min }\right) / E_{v}$ and $E_{b}\left(k_{\min }\right) / E_{b}$, are shown in Fig. 6. The ratio $E_{p}\left(k_{\text {min }}\right) / E_{v}$ stays roughly constant and small, but $E_{b}\left(k_{\min }\right) / E_{b}$ undergoes substantial increase. This implies that a substantial amount of $E_{b}$ is accumulating in the large scales because of back-transfer of $H_{m}$, while for-ward-transfer of energy (kinetic and magnetic) feeds the dissipation at higher wave numbers. It follows that $E_{v}$ will decay at a faster rate than $E_{b}$, as seen in Fig. 5(c), where the time history of $E_{v} / E_{b}$ is given.

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-07.jpg?height=569&width=765&top_left_y=1783&top_left_x=119)
FIG. 4. Parametric plots in time of runs $\mathrm{A}, \mathrm{B}, \mathrm{C}$, and D in the rugged invariant parameter space. The initial positions in the plane are indicated by a cross.

The time history of mean alignment angle between the $\mathbf{v}$ and $\mathbf{b}$ fields $\cos \Theta=H_{c} / \sqrt{E_{v} E_{b}}$, given in Fig. 5(b), begins to decrease late in the run, but is not close to either of the values $\pm 1$ predicted by the minimum energy principle. This

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-07.jpg?height=1535&width=653&top_left_y=829&top_left_x=1031)
FIG. 5. Time histories of global quantities for runs $\mathrm{A}, \mathrm{B}, \mathrm{C}$, and D . The curves given are (a) $H_{m} / E_{b}$ versus time, (b) $\cos \Theta=H_{c} / \sqrt{E_{b} E_{b}}$ versus time, and (c) $E_{v} / E_{b}$ versus time.

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-08.jpg?height=1030&width=641&top_left_y=105&top_left_x=115)
FIG. 6. Time histories of fractions of $E_{v}$ and $E_{b}$ located in $k_{\text {min }}$ for runs A , $B, C$, and D.

is a consequence of the absence of dynamic alignment in the relaxation, since the constraint of constant $H_{c}$ produces alignment of the fields in the minimum energy principle.

This run can best be characterized as an example of pure selective decay, of the type invoked ${ }^{3}$ to explain Taylor relaxation ${ }^{2}$ in reversed-field pinch experiments. The time asymptotic state is well determined solely by the $H_{m}$ constraint in the minimum energy principle. It should also be noted that when the system begins in initial states dominated by $E_{b}$ with reasonably large levels of $H_{m}$, there is a rapid relaxation toward $E_{v} / E_{b}=O(1)$, as discussed in Sec. IV, but the long time asymptotic behavior is qualitatively the same as run A .

## B. Run B

This run began with a large amount of $H_{c}$ but with $H_{m}=0$. It follows that selective decay will have negligible influence on the system's dynamics, since no back-transfer will occur, and dynamic alignment will determine the gross features of the time asymptotic state. In Fig. 4 it is seen that $2 H_{c} / E$ grows to near its maximum value of 1 by $t_{\text {final }}$, indicating dynamic alignment, while $H_{m} / E$ is far from maximum, an indicator of the negligible influence of selective decay. High resolution 3-D simulations have also reported similar dynamic alignment dominated evolution. ${ }^{29}$

Because of the absence of selective decay, the ratio $H_{m} / E_{b}$ does not approach either of the values $\pm 1$ predicted
by the minimum energy principle, as seen in Fig. 5(a). Thus there is no condensation of $E_{b}$ into a large-scale helical magnetic field. This contrasts with the behavior of the mean angle between $\mathbf{v}$ and $\mathbf{b}, \cos \Theta$ is plotted in Fig. 5(b), which grows to values near 1 prior to $t_{\text {final }}$, in accord with the minimum energy principle. Hence the time asymptotic state is determined predominantly by the $H_{c}$ constraint on the energy integral.

In accordance with this interpretation, it is seen in Fig. 6 that neither $E_{v}\left(k_{\min }\right) / E_{v}$ nor $E_{b}\left(k_{\min }\right) / E_{b}$ increase with time. This is a consequence of the absence of any significant level of back-transfer induced by $H_{m}$ or $H_{c}$ on the wavenumber distribution of excitations. Since $H_{c}$ is not backtransferred in this region of the rugged invariant parameter space, any growth in $2 H_{c} / E$ will be due to mechanisms discussed in Refs. 12, 17, and 18. By $t_{\text {final }}, E_{v} / E_{b}$ is near unity [see Fig. 5(c) and Table III], a consequence of alignment of the $\mathbf{v}$ and $\mathbf{b}$ fields and maximal $2 H_{c} / E$. This run can be considered to consist almost entirely of dynamic alignment.

## C. Run C

Run C began with large $H_{m}$ and large $H_{c}$. Thus both selective decay and dynamic alignment will play a role in the determination of the time asymptotic state. In Fig. 4 it is seen that neither $H_{m} / E$ or $2 H_{c} / E$ are near their maximum values by $t_{\text {final }}$, but instead relax to near the ellipse [Eq. (12)] derived from the dual constraints of constant $H_{m}$ and $H_{c}$ in the minimization of the energy integral (cf. Sec. II and Fig. 1).

In view of the strong influence of selective decay, the ratio $H_{m} / E_{b}$ reaches values near 1 by $t_{\text {final }}$. Figure 5(a) depicts this behavior, and indicates that the time asymptotic state consists of a large-scale helical magnetic field, as predicted by minimum energy principle with nonzero $H_{m}$. Also by $t_{\text {final }}$, the $\mathbf{v}$ and $\mathbf{b}$ fields approach a perfectly aligned state, as indicated by the $\cos \Theta$ plot in Fig. 5(b). This is expected, in accordance with the $H_{c}$ constraint in the minimum energy principle.

The portions of the $E_{v}$ and $E_{b}$ spectra that reside in $k_{\text {min }}$ are seen to increase with time, in Fig. 6. The growth of the fraction of $E_{b}$ in $k_{\text {min }}$ is a product of back-transfer of $H_{m}$ and is a required consequence of the evolution toward the abovedescribed large-scale helical magnetic field. On the other hand, the increase in the fraction of $E_{v}$ in $k_{\text {min }}$ is an indicator of $H_{c}$ back-transfer. It is in this region of the rugged invariant parameter space that $H_{c}$ back-transfer is conjectured. ${ }^{37}$ Since $E_{v}$ and $E_{b}$ are accumulating in the largest scale at near equal rates, their decay rates must not differ as greatly as in run A , and the ratio $E_{v} / E_{b}$ will relax to larger values, but still $<1$, and the time asymptotic state contains significant mechanical pressure [cf. Fig. 5(c)]. If $H_{c}$ is transferred to low $k$, and $E$ to high $k, H_{c}$ is expected to decay more slowly than $E$, giving rise to the growth of the velocity-magnetic field correlation illustrated in Figs. 4 and 5(b). This contrasts run B , where growth in velocity-magnetic field correlation occurred without $H_{c}$ back-transfer.

The concurrence of selective decay and dynamic alignment processes in this type of run sharply contrasts the pre-
vious two cases, in which only one relaxation process dominated the dynamical evolution. However, in run C, neither process exhibited the purest form of its respective effects; instead a balance is struck between the two types of relaxation, the consequences of which appear to be accurately described by the energy minimization principle with both $H_{m}$ and $H_{c}$ constraints. The final states observed in this type of run are a trade-off between selective decay and dynamic alignment: The computations show essentially complete relaxation to a final state intermediate to the pure selective decay and dynamic alignment states. In Sec. VII a model is derived that predicts the time asymptotic states as a function of the initial rugged invariants for runs of this type.

## D. Run D

Run D begins with $H_{c}=0$ and $H_{m}=0$. One expects to see neither selective decay nor dynamic alignment have a significant effect in the evolution of the system. This is seen to be the case in Fig. 4, where, at $t_{\text {final }}$, both the ratios $H_{m} / E$ and $2 H_{c} / E$ are far from their respective maximum values.

Since selective decay and dynamic alignment are not operating to any significant extent, the distinctive properties predicted by the minimum energy principle do not appear in the final state. For example, condensation of $E_{b}$ into a largescale helical structure does not occur, as indicated by the failure of $\left|H_{m}\right| / E_{b}$ to reach values near 1 by $t_{\text {final }}$ in Fig. 5 (a). Alignment of the $\mathbf{v}$ and $\mathbf{b}$ fields also does not occur, as indicated by the failure of $\cos \Theta$ to reach values near $\pm 1$ by $t_{\text {final }}$ in Fig. 5(b). It follows that growth of large-scale $E_{v}$ or $E_{b}$ does not occur (cf. Fig. 6). Since back transfer is absent and therefore does not interfere with the forward $E$ transfer, no inequalities develop in the decay rates of $E_{v}$ and $E_{b}$. Thus the ratio $E_{v} / E_{b}$ maintains a value near unity, as seen in Fig. 5 (c).

This run is best characterized as Navier-Stokes-like, in the sense that the dynamics is dominated by forward energy transfer, and the $\mathbf{v}$ and $\mathbf{b}$ fields are virtually uncorrelated, and thus act independently. However, this description should not be confused with the description of certain 2-D states ${ }^{19}$ that become Navier-Stokes-like due to disappearance of magnetic excitations. It should also be noted that systems that experience rapid early $E_{b}$ growth due to initially large values of $E_{v} / E_{b}$ (see the discussion in Sec. IV) have time asymptotic behavior similar to this run.

## E. Comparison of energy decay rates

It is interesting to consider the relative rates of decay of $E$ for each of the runs $\mathrm{A}, \mathrm{B}, \mathrm{C}$, and D , by comparing time histories of the energy, shown in Fig. 7. The slowest decay rate is seen in run C in which back-transfer of both $H_{m}$ and $H_{c}$ occurs, and both $E_{v}$ and $E_{b}$ accumulate in the largest scale modes. In run A, back-transfer of $H_{m}$ causes $E_{b}$ to accumulate in the largest scale, but $H_{c}$ back-transfer is weak, and very little $E_{v}$ is spared rapid dissipation by appearance in the longest wavelength modes. Thus a slightly faster decay rate of $E$ is realized. For runs B and D back-transfer of $H_{m}$

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-09.jpg?height=548&width=712&top_left_y=97&top_left_x=1047)
FIG. 7. Time history of the total energy for runs $\mathrm{A}, \mathrm{B}, \mathrm{C}$, and D , illustrating the effects of spectral transfer on the decay rate of $E$.

is weak, and $H_{c}$ back-transfer is either weak or nonexistent. However, in run $B$ the presence of significant amounts of $H_{c}$ weakens spectral transfer directly through reduction in the strength of the nonlinear couplings, as discussed in Refs. 12, 17, and 18. In addition, $H_{c}$ itself has been argued in the same studies to decay at a rate slower than that of $E$, independent of any influence of back-transfer. These effects weaken net transfer to the high $k$ modes where dissipation is most efficient, explaining why run B decays slower than run D , but faster than both A and C .

The fastest $E$ decay rate occurs in run $D$, in which the effects of both $H_{m}$ and $H_{c}$ back-transfer are negligible, and nonlinearities are also undiminished by $H_{c}$. The dissipative high $k$ modes are rapidly fed by unimpeded transfer of $E$ to high $k$. Note that the value of $E$ at $t_{\text {final }}$ in run D is two orders of magnitude less than the same quantity in run C. Clearly the net influence of the initial rugged invariant ratios on the total dissipation rate of energy is quite substantial, and an understanding of what type of MHD turbulence is being discussed is essential to estimating the time scale for decay of the turbulence.

## VI. CLASSIFICATION OF RUGGED INVARIANT PARAMETER SPACE

In this section the different time asymptotic behavior and mechanisms that lead to this behavior for particular regions of the rugged invariant parameter space given in Fig. 1 will be summarized. Regions of the parameter space where past work has focused will be discussed. Also, a comparison of this work with 2-D MHD simulations will be made.

First, consider the properties of the time asymptotic states when only one selective decay or dynamic alignment are operating. Neglecting the effects of cross helicity, so that $\alpha=0$ in the variational principle given in Eq. (4), realizes a state of pure selective decay. The properties of this state are easily seen from Eq. (5) to be $E_{v}=0$ and $\left|H_{m}\right| k_{\text {min }} / E_{b}=1$. This corresponds to a force-free largescale helical magnetic field. In Fig. 8 the location of this

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-10.jpg?height=796&width=840&top_left_y=107&top_left_x=126)
FIG. 8. Schematic of the $H_{m} / E$ and $2 H_{c} / E$ plane, illustrating the minimum energy curve and qualitatively the locations of the boundaries of the four regions. The arrows indicate the general direction of trajectories in the plane.

point in the rugged invariant parameter space is given. Initial states that begin in the region labeled I in Fig. 8 typically relax to states with properties determined solely by the $H_{m}$ constraint in the minimum energy principle. An example of this type of relaxation in run A of the previous section. Another example is given in Fig. 9, where it is seen that the trajectory in the parameter space is basically parallel to the $H_{m} / E$ axis, indicating absence of growth in $2 H_{c} / E$ (i.e., the absence of dynamic alignment).

This type of decay (which we call region I decay) was first investigated by Taylor ${ }^{2}$ in a cylinder with conducting boundary conditions, and a dynamical explanation based on turbulent back-transfer of $H_{m}$ was proposed by Montgom-

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-10.jpg?height=567&width=772&top_left_y=1815&top_left_x=126)
FIG. 9. Five examples of runs that scan the $H_{m} / E$ and $2 H_{c} / E$ plane, illustrating the differing behavior as the initial parameters are varied. The initial position for each run is indicated by a cross.

ery et al. ${ }^{3}$ Simulations of decaying 3-D MHD by other researchers also show relaxation to the state predicted by the minimum energy principle. ${ }^{5,9,27,40}$

Second, if we now neglect the effects of $H_{m}$, so that $\varphi=0$ in the variational principle given in Eq. (4), a pure dynamic alignment time asymptotic state is realized. The properties of this state are easily seen from Eq. (5) to be $E_{v}=E_{b}$ and $2\left|H_{c}\right| / E=1$, a state of perfect "Alfvénic" fluctuations. In Fig. 8 the location of this point in the parameter space is indicated. Initial states that begin in the region labeled III in Fig. 8 typically relax to states with properties given solely by the $H_{c}$ constraint in the minimum energy principle. An example of this type of relaxation is run B of the previous section. Another example is given in Fig. 9, where it is seen that the trajectory in the parameter space principally follows the $2 H_{c} / E$ axis, and a substantial growth of this ratio toward its extremal value of unity is attained. Although there is growth in $H_{m} / E$ in the same run, it does not approach its maximal value prior to the late stages of the run. This illustrates the dominance of dynamic alignment over selective decay for this region.

This type of decay (here, "region III" decay) was first investigated by Dobrowolny et al., ${ }^{12}$ who proposed a dynamical explanation for growth of $H_{c} / E$ based on spectral transfer rates of the Elsässer fields. This was offered as an explanation for the appearance of Alfvénic fluctuations ${ }^{11}$ in interplanetary space. Variations and refinements of the mechanism for dynamic alignment have been developed by other authors. ${ }^{17,18}$ Simulations of decaying 3-D MHD in this region have exhibited growth in velocity-magnetic field correlations, ${ }^{29}$ and numerical solutions of two-point closures were found to relax to the minimum energy state. ${ }^{18}$ An important feature of the dynamics in this region of parameter space is the near complete absence of any back-transfer effects.

Now consider the relaxation problem when large amounts of $H_{m}$ and $H_{c}$ are present, so that both back-transfer and dynamic alignment mechanisms are expected to be operating. For this case it is necessary to include both the $H_{c}$ and $H_{m}$ constraints in the minimum cnergy principle. The properties of these states were found in Sec. II to be $\left|H_{m}\right| k_{\min } / E_{b}=1$ and $2\left|H_{c}\right| / \sqrt{E_{v} E_{b}}=1$. These relations define the minimum energy curve indicated in Fig. 8. Initial states that begin in the region labeled II in Fig. 8 relax to states that lie on the minimum energy curve. In this region selective decay and dynamic alignment will simultaneously influence the determination of the time asymptotic state, in contrast to both region I and III turbulence. An example of this "region II" relaxation is run C of the previous section. Three other examples are given in Fig. 9. Contrasting regions I and III, from the trajectories in Fig. 9 it is seen that region II systems experience substantial growth in both $H_{m} / E$ and $2 H_{c} / E$, and relax to a state that maximizes $\left|H_{m}\right| / E$ for a given $2\left|H_{c}\right| / E$. Also, note that as the initial $H_{c}$ is increased the time asymptotic state moves further to the right on the minimum energy curve, corresponding to an increasing admixture of $E_{v}$ in the final state (see Fig.9). The trajectory that begins with the largest initial $H_{c}$ in Fig. 9 relaxes to a state with $2 H_{c} / E$ near 1 , which is Alfvénic in
nature. This point and its properties are labeled in Fig. 8. Thus it is possible for a system to relax to an Alfvénic state (i.e., pure dynamic alignment state) when selective decay is operating.

In region II, $H_{m}$ back-transfer is responsible for $H_{m} / E$ growth. In addition, it is thought that $H_{c}$ back-transfer will strongly influence the growth of $2 H_{c} / E \cdot{ }^{37}$ A consequence of this is the noted appearance of large-scale $E_{v}$ in the time asymptotic state (cf. Sec. V), a feature absent in dynamic alignment theories ${ }^{12}$ that do not consider the possibility of back-transfer. In Sec. VII we suggest further that the mechanisms that are responsible for correlation growth in region III are less important in region II than are back-transferassociated effects.

Unlike regions I and III, which have been previously investigated by high resolution simulation and closure calculations, region II has not been previously studied in detail. This is possibly because this range of parameters has not seemed relevant for modeling fusion devices or space physics applications, and because closure schemes are barely tractable when only two rugged invariants are considered. To our knowledge the present investigations are the first to consider the dynamical consequences of spectral transfer of all three rugged invariants for 3-D MHD.

Finally, systems that lie very near the origin of the rugged invariant parameter space exhibit none of the time asymptotic properties characteristic of the three regions. This was noted in Sec. V, where it was seen in run D that during the lifetime of the dynamics (at least at the moderate Reynolds numbers we have used) neither $H_{m} / E$ nor $2 H_{c} / E$ evolved toward their maximum values. Thus minimum energy states, in the sense of the variational principle discussed in Sec. II, are not obtained. Selective decay and dynamic alignment are ineffective for these initial parameters, and the relevant area near the origin of Fig. 8 might be designated as region IV decay. Since the global value of the helicities is small, their value is of the same order as the spectral fluctuations. It follows that in this parameter regime there is no monotonic decay of either $H_{c}$ or of $H_{m}$. In this region the nonlinear couplings are strongest and the energy decay rates are greatest.

Though this classification of the rugged invariant parameter space is illustrative, the lines drawn in Fig. 8 indicating the boundaries should not be thought to indicate more than a qualitative demarcation. If there is a true boundary between the regions, instead of a continuous change in relaxation properties, its structure is quite complex, or it is possibly nonexistent, owing to the random effects of higher-order moments. This question is raised because runs that began near the boundary of the proposed regions would sometimes exhibit properties characteristic of a neighboring region.

It is interesting to compare the results of this study with previous work on 2-D MHD relaxation, ${ }^{19}$ which proposed an analogous (and equally roughly defined) classification scheme for 2-D MHD turbulence. Recall that 2-D MHD has no $H_{m}$ and the mean square vector potential $A$ becomes the magnetic rugged invariant. The most notable difference between 2-D and 3-D relaxation is the disappearance, in 3-D relaxation, of what Ting et al. ${ }^{19}$ referred to as Navier-Stokes
relaxation and transition region behavior (regions II and IV, respectively, in Ref. 19). The region of Navier-Stokes relaxation was characterized by large initial amounts of $E_{v}$, corresponding to small initial values of $A / E$ and $2 H_{c} / E$. The analogous portion of the 3-D parameter space is what we designated as region IV, a region circling the origin in Fig. 8. After long times, 2-D runs that begin in the Navier-Stokes region approach states that maximize the energy integral through a decrease in $A / E$ with time. This leads to time asymptotic states with $E_{v} \gg E_{b}$. This type of relaxation is not seen in 3-D MHD because initially dominant $E_{v}$ states experience rapid relaxation to states of near-equipartition between $E_{v}$ and $E_{b}$, as discussed in Sec. IV. The different time asymptotic behavior in 2D and 3D is possibly a consequence of the difference in the absolute equilibrium $E_{v} / E_{b}$ in this area of parameter space. In 2-D MHD absolute equilibrium, when $A / E$ is near minimal, states of high $E_{v}$ are obtained for systems with a finite number of $k$ modes, ${ }^{36}$ but in 3-D equilibrium, small $H_{m} / E$ yields $E_{v} \approx E_{b}$.

The transition region in 2-D MHD contains the boundary between the selective decay dominated region and the Navier-Stokes region. Initial states that begin here could follow either a Navier-Stokes or selective decay-type relaxation. One would not expect it to exist in 3D since there is no region of Navier-Stokes relaxation. Instead, one can easily form states with nearly equal $E_{b}$ and $E_{v}$, but $H_{m} \equiv 0$. Consequently, the 3-D case lacks the kind of erratic behavior seen in 2D when $A \approx 0$, and near-equipartition can be sought only by extreme stretching of magnetic field lines, which is thwarted for finite Reynolds number systems by high $k$ dissipation. In this regard, the presence of a Navier-Stokes-like and a transition region in 2-D turbulence may be associated with the 2-D antidynamo theorem, and at least some of the differences in 3-D relaxation can be interpreted as a consequence of dynamo action.

The comparison of the proposed 3-D classification with the 2-D classification of Ting et al. ${ }^{19}$ is completed by noting that the 3-D regions associated with selective decay (region I), dynamic alignment (region III), or a balance of the two (region II) are equivalent to the 2-D regions assigned the designations I (selective decay, actually a mixture with dynamic alignment) and III (near-perfect dynamic alignment). Here the relevant parameter regions were expanded to three in number to differentiate among nearly pure dynamic alignment, nearly pure selective decay, and the region in which selective decay and dynamic alignment have nearly equal influence.

## VII. ABSOLUTE EQUILIBRIUM THEORY AND RELATION TO DECAY SIMULATIONS

If $v=\eta=0$ in Eq. (1) the Galerkin representation in a periodic geometry can be shown to satisfy a Liouville theorem in a phase space whose coordinates are the real and imaginary parts of the Fourier coefficients $\mathbf{v}(\mathbf{k})$ and $\mathbf{b ( k )} .^{22}$ The rugged invariants, Eqs. (3), constrain the system to the hypersurfaces they define in this phase space. It follows that the generalized canonical distribution of states can be written as

$$
\begin{equation*}
P=\exp \left[-\left(\beta E+\gamma H_{c}+\theta H_{m}\right)\right] / Z, \tag{15}
\end{equation*}
$$

where $\beta, \theta$, and $\gamma$ play the role of generalized inverse temperatures for $E, H_{c}$, and $H_{m}$, respectively, and $Z$ is the normalizing factor. The rugged invariant spectra can be found by evaluation of the appropriate moments of the canonical distribution.

The tendency of certain absolute equilibrium rugged invariant spectra to experience a Bose-like condensation into $k_{\text {min }}$ in a thermodynamic like limit (i.e., $k_{\text {max }} \rightarrow \infty$ with the rugged invariants held fixed) is thought responsible for the back transfer of these quantities in dissipative turbulent flows. ${ }^{3,24,35,37}$ For 3-D ideal MHD absolute equilibrium, the $H_{m}$ spectrum condenses to $k_{\min }{ }^{24}$ while the $H_{c}$ spectrum experiences a weaker, partial condensation under some circumstances. ${ }^{37}$ A number of features of the dissipative relaxation processes studied in the present paper can be better understood by appeal to tendencies that can be inferred from the equilibrium theory. Here, we summarize some of the relevant equilibrium properties, which are discussed in detail in Ref. 37.

Inferences concerning directions of preferred spectral transfer in dissipative MHD can be most easily extracted from the equilibrium theory by considering an infinite mode system with fixed values of the rugged invariants. Thus we first summarize absolute equilibrium properties in the limit $k_{\text {max }} \rightarrow \infty$ with $E, H_{c}$, and $H_{m}$ fixed. In this limit, the $H_{m}$ spectrum condenses to $k_{\min }$, that is, with $H_{m}\left(k_{\min }\right)$ representing the magnetic helicity in all modes with $k=k_{\text {min }}=1$;

$$
\begin{equation*}
H_{m}\left(k_{\min }\right)=H_{m} . \tag{16}
\end{equation*}
$$

Similarly, the fractions of $E$ and $I_{c}$ that occupy $k_{\min }$ are given by

$$
\begin{align*}
& E\left(k_{\min }\right) / E=\left(1+\beta_{\gamma}^{2}\right)\left|\sigma_{m}\right|  \tag{17a}\\
& H_{c}\left(k_{\min }\right) / H_{c}=-2 \beta_{\gamma}\left|\sigma_{m}\right| / \sigma_{c}, \tag{17b}
\end{align*}
$$

where

$$
\begin{align*}
& \beta_{\gamma}=\gamma / 2 \beta \\
& \quad=\operatorname{sgn}\left(\sigma_{c}\right) \sqrt{\frac{1}{3}\left(1+\frac{1}{\left|\sigma_{m}\right|}\right)}\left(\sqrt{3} \sin \frac{\theta}{3}-\cos \frac{\theta}{3}\right)  \tag{18a}\\
& \quad \tan \theta=\sqrt{\frac{4}{27 \sigma_{c}^{2}\left|\sigma_{m}\right|}\left(\left|\sigma_{m}\right|+1\right)^{3}-1} \tag{18b}
\end{align*}
$$

with $\sigma_{m}=H_{m} / E$ and $\sigma_{c}=2 H_{c} / E$. Note that for $H_{m}=0$, Eqs. (17a) and (17b) are zero. It can also be shown that the energy in $k_{\text {min }}$ is the minimal amount necessary to satisfy the kinematic constraint imposed by the values of $H_{c}$ and $H_{m}$, namely,

$$
\begin{align*}
& \left|H_{m}\left(k_{\min }\right)\right|=E_{b}\left(k_{\min }\right)  \tag{19a}\\
& \left|H_{c}\left(k_{\min }\right)\right|=\sqrt{E_{b}\left(k_{\min }\right) E_{v}\left(k_{\min }\right)} \tag{19b}
\end{align*}
$$

Each of the rugged invariant spectra is seen to have a different character in this limit. In general, the $H_{m}$ spectrum totally condenses to $k_{\text {min }}$. Also, whenever $H_{m} \neq 0$, the equilibrium spectrum requires that portions of the $H_{c}$ and $E$ spectra condense to $k_{\text {min }}$. In Ref. 37, it is shown that the degree of
condensation of $H_{c}$, referred to as a partial condensation, is a property of the statistical equilibrium, and is not required for kinematic reasons.

Other properties that are relevant here are the kinetic to magnetic energy ratio, evaluated both globally (all $k$ modes) and for only excitations in $k_{\text {min }}$. In absolute equilibrium these are given by
$E_{v}\left(k_{\text {min }}\right) / E_{b}\left(k_{\text {min }}\right)=\beta_{\gamma}^{2}$,
$\left(E_{v} / E_{b}\right)_{\text {eq }}=\left[1-\left|\sigma_{m}\right|\left(1-\beta_{\gamma}^{2}\right)\right] /\left[1+\left|\sigma_{m}\right|\left(1-\beta_{\gamma}^{2}\right)\right]$.

It can be shown that the global ratio satisfies $E_{v} / E_{b} \leqslant 1 .^{37}$
Another interesting property of absolute equilibrium is that the inverse temperatures $\beta, \gamma$, and $\theta$ diverge ${ }^{37}$ along the boundaries of the parameter space shown in Fig. 1. For $\sigma_{m}<\frac{1}{2}, \beta$ and $\gamma$ diverge along the line $\left|\sigma_{c}\right|=2\left|H_{c}\right| / E=1$, while $\theta$ remains finite. There is no condensation of the rugged invariant spectra along this line. All three inverse temperatures diverge along the minimal energy curve in Fig. 1, and all three rugged invariant spectra condense to $k_{\text {min }}$. Consequently, these boundaries have importance in both the equilibrium theory and in the minimum energy theory used above to discuss dissipative relaxation processes.

The tendency of Eq. (1) to relax to absolute equilibrium in the absence of dissipation can be interpreted as the statistical force driving relaxation processes that occur in the presence of dissipation. This is because the nonlinear terms of Eq. (1) conserve the rugged invariants in triad interactions, even in the presence of dissipation, so the tendency for these couplings to cause the system to evolve toward an equilibrium is maintained. However, dissipation introduces a sink at high wave numbers that drains modal excitations, changing both the spectral shape and the values of the global rugged invariants. ${ }^{35}$ This prevents attainment of an equilibrium spectrum in which there would be no net spectral transfer. Nonetheless, it appears that in many situations the direction of net spectral transfer, and to some degree the character of the spectra themselves can be inferred from the equilibrium distributions the flow would like to approach if dissipation were absent.

A simple application of this idea can explain the "fast" relaxation of the ratio $E_{v} / E_{b}$ toward $O(1)$ values described in Sec. IV. Consider an initial state with a small magnetic energy. Necessarily, $2 H_{c} / E$ and $H_{m} / E$ will both be small. So, the system will lie near the origin of Fig. 1. If $\sigma_{c}$ and $\sigma_{m}$ are set equal to zero in Eq. (20b), the global absolute equilibrium kinetic to magnetic energy ratio is unity. Thus it is likely that for dissipative flow, there exists a dynamolike relaxation process that takes the kinetic to magnetic energy ratio to values near unity. ${ }^{39}$ This is seen in the Galerkin model simulations in Sec. IV: A perturbing magnetic field grew exponentially until a state of near-equipartition of kinetic and magnetic energy was reached. The force driving this "dynamo" does not involve specifically identified couplings, but is statistical in nature.

Similarly, if the initial state has small kinetic energy it is necessary that $2 H_{c} / E$ be small, but $H_{m} / E$ is unconstrained. So, the system will lie near the line $2 H_{c} / E=0$ in Fig. 1. For small values of $2 H_{c} / E$ the ratio $\left(E_{v} / E_{b}\right)_{\text {eq }}$ will lie near the
curve labeled 0.01 in Fig. 10. Thus for dissipative flow a relaxation process that takes $E_{v} / E_{b}$ to values that lie near this curve is likely. This equilibrium ratio is much less than unity only when $H_{m} / E$ is large, and the presence of any nonvanishing $H_{c}$ tends to raise the equilibrium $E_{v}$. Unlike the process of magnetic energy growth described in the previous paragraph, the kinetic energy growth process saturates before equipartition is achieved, due to the fact that some energy is locked into magnetic modes by the nonzero $H_{m}$. This is indeed seen to be the case for Galerkin model simulations presented in Sec. IV. The absolute equilibrium kinetic to magnetic energy ratio $\left(E_{v} / E_{b}\right)_{\text {eq }}$ is computed for several decay runs, in the last column of Table I, using the initial values of $H_{m} / E$ and $2 H_{c} / E$ for each run. Comparison of $\left(E_{v} / E_{b}\right)_{\text {eq }}$ and the value of $E_{v} / E_{b}$ at the time of maximum kinetic energy in the decay runs shows that kinetic energy growth terminates at values near to that which would be expected in absolute equilibrium. Thus, perhaps somewhat surprisingly, it appears that the infinite mode absolute equilibrium ensemble provides a reasonably accurate prediction of the maximum kinetic energy attained in dissipative runs with initially very low $E_{v}$.

Properties of absolute equilibrium can also be used to motivate and describe the mechanisms that drive the longer time scale relaxation process, selective decay, and, for some cases, dynamic alignment. Dissipative back-transfer of $H_{m}$ can be interpreted as a consequence of a continually frustrated attempt to achieve the condensation of $H_{m}$ seen in the absolute equilibrium spectra. Back-transfer causes $H_{m}$ to have a slower decay rate than the forward-transferred $E$ for dissipative flows, an effect that drives the system to a state of minimum energy ${ }^{3}$ with finite magnetic helicity. The partial condensation of the absolute equilibrium $H_{c}$ spectrum, for $H_{m} \neq 0$, suggests that, in dissipative turbulence, $H_{c}$ can be back-transferred when $H_{m}$ is back-transferred. ${ }^{37}$ This effect causes $H_{c}$ to decay more slowly than $E$ in the presence of dissipation, and drives the system to a minimum energy state. In this scenario, the system evolves toward a point on

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-13.jpg?height=570&width=738&top_left_y=1773&top_left_x=115)
FIG. 10. Values of $E_{c} / E_{b}$ for absolute equilibrium in the infinite mode limit, for values of $H_{m} / E$ and $2 H_{c} / E$ that scan the parameter space given in Fig. 1. The five curves are labeled by their respective values of $2 H_{c} / E$.

the extremal energy ellipse described in Sec. II, as we have seen for many of the low-order runs described in Sec. V.

The dynamic alignment mechanism driven by backtransfer, which necessarily is accompanied by selective decay, is of entirely different origin than the mechanisms discussed by previous authors in which $H_{c}$ is neutrally transferred. ${ }^{12}$ When significant amounts of $H_{c}$ and $H_{m}$ are present, the absolute equilibrium spectrum displays a strong partial condensation of $H_{c}$, causing $E_{v}$ to accumulate in the largest scales of the system. This feature is illustrated in Fig. 11. Dissipative runs with initial data in the same region of the $2 H_{c} / E, H_{m} / E$ parameter space show growth of large-scale kinetic energy, as was discussed in Sec. V. Thus we see that the parameter regime in which back-transfer of $H_{c}$ has a significant effect corresponds well with the region in which the equilibrium theory admits significant partial condensation of the $H_{c}$ spectrum.

In the present perspective, turbulent relaxation processes are interpreted as consequences of a dissipative system evolving, in some sense, toward an equilibrium state, while being prevented by dissipation from achieving it. In the case of flows in which significant growth or decay of the ratio $E_{v} / E_{b}$ is required to achieve near-equipartition, the fluid starts from states that are very far from the absolute equilibrium state, since large fractions of the energetically available phase space are out of balance. Thus almost all randomly chosen modifications to the phase space distribution of excitations, including the average effect of the MHD nonlinear couplings, will invariably act to correct this imbalance. This kind of redistribution would be expected to occur on the time scale characteristic of the nonlinear couplings, of the order of an appropriately defined eddy turnover time. ${ }^{39}$ The loworder Galerkin simulations in Sec. IV showed an approach to near-equipartition on this fast time scale (cf. Tables I and II). This suggests using the terminology "fast relaxation process" for this type of approach to near-equipartition of $E_{v}$ and $E_{b}$.

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-13.jpg?height=572&width=743&top_left_y=1747&top_left_x=1023)
FIG. 11. The ratio of $E_{v}$ to $E$ in $k_{\min }$ for the infinite mode absolute equilibrium ensemble spectrum. The values of $H_{m} / E$ and $2 H_{c} / E$ scan the plane given in Fig. 1. Each curve is labeled by its value of $2 H_{c} / E$, which is held fixed as $H_{m} / E$ is varied through its range of possible values.

On the other hand, relaxation processes such as selective decay and dynamic alignment require the dissipation of the rugged invariant excitations (here, the energy) that are di-rect-transferred and dissipated. This renders the back-transferred quantities ever more dominant, and the fluid approaches a final state characterized by some balance between selective decay and dynamic alignment. It is clear that this evolution will occur on time scales on the order of the decay time of the direct-transferred quantity, here the decay time of the energy, adjusted to take into account kinematically required energy back-transfer. This time scale is much longer than an eddy turnover time, and the associated relaxation processes are "slow." The Galerkin simulation results presented in Sec. IV have shown that the selective decay/dynamic alignment relaxation is in fact much slower than the rapid adjustment to near-equipartition. A corollary is that, during relaxation of $E_{v} / E_{b} \rightarrow O(1)$, the ratios $2 H_{c} / E$ and $H_{m} / E$ change very little from their initial values and there is negligible magnetic back-transfer, because of the disparity in time scale between the fast and slow relaxation processes.

## VIII. A SIMPLE DECAY MODEL BASED ON ABSOLUTE EQUILIBRIUM THEORY

Having seen that the equilibrium ensemble theory provides appealing explanations for several features of the decaying solutions of low-order truncation MHD, it is natural to ask whether this connection can be refined into a more quantitative form. In this section a simple predictive model of 3-D MHD decay is discussed, based on equilibrium properties of the initial data. The model provides a mapping of initial rugged invariant ratios onto time asymptotic states in the $H_{m} / E, 2 H_{c} / E$ parameter space. The results agree well with the low-order Galerkin model simulations. In the construction of this mapping, properties of the infinite $k_{\text {max }}$ limit of the absolute equilibrium rugged invariant spectra (summarized in Sec. VII) are used.

The ad hoc assumptions of the model are (1) the decay time of the system is much longer than the time scale for spectral transfer. (2) Spectral transfer takes place as if $k_{\text {max }}$ were infinite. (3) Dissipation acts only on modes with $k>k_{\text {min }}$. As a consequence of the first two assumptions the system will rapidly relax to the $k_{\text {max }} \rightarrow \infty$ rugged invariant spectra defined by the initial values of its global rugged invariants before decay has had a significant effect. Having reached this absolute equilibrium state, dissipation destroys all excitations except those in $k_{\text {min }}$, so that the time asymptotic state is completely determined by the $k_{\min }$ portion of the absolute equilibrium rugged invariant spectra.

In general, positions on the minimum energy curve, given by Eq. (12), are specified by fixing the value of $E_{v} / E_{b}$. In the present simple model, the time asymptotic value of $E_{v} / E_{b}$ will be estimated as the value of the same ratio computed from the $k_{\min }$ portions of the equilibrium spectrum, using the rugged invariant values of the initial data of the dissipative run. Specifically, the model tests the hypothesis that

$$
\begin{equation*}
\left(E_{v} / E_{b}\right)_{t \rightarrow \infty} \approx \beta_{\gamma}^{2}\left(\sigma_{c i}, \sigma_{m i}\right) \tag{21}
\end{equation*}
$$

where $\beta_{\gamma}^{2}$ is the ratio of inverse temperatures defined by Eq. (18a), depending on the initial values of $\sigma_{c i}=2 H_{c} / E$ and $\sigma_{m i}=H_{m} / E$.

In Fig. 12 cross sections through the surface of the mapping $\left(E_{v} / E_{b}\right)_{t \rightarrow \infty}\left(\sigma_{c i}, \sigma_{m i}\right)$ are plotted. It can be seen that qualitatively it behaves as expected from the intuition acquired from the simulations. The $E_{v}$ in the time asymptotic state decreases as the initial $H_{m}$ in the initial state increases, and the time asymptotic $E_{v}$ and $E_{b}$ become equipartitioned as the initial $H_{c}$ is increased. Figure 13 compares the predictions of the model with the low-order Galerkin simulations for many initial values of $2 H_{c} / E$ and $H_{m} / E$. The comparison is seen to be favorable for decay simulations that relaxed to positions close to the minimum energy ellipse. In Sec. V it was seen that if the initial value of $H_{m}$ is small, back-transfer is weak, the system does not relax to the minimum energy curve in a time of the order the decay time for $k_{\text {min }}$. Thus the model only gives good predictions of the time asymptotic behavior when back-transfer has a significant influence in the systems dynamics, since the model maps every initial state onto the minimum energy ellipse. Also, in this model, the total increase in the normalized velocity-magnetic field correlation $2 H_{c} / E$ is due to the transfer of $H_{c}$ to the large

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-14.jpg?height=1173&width=682&top_left_y=1136&top_left_x=1034)
FIG. 12. The time asymptotic value of $E_{0} / E_{b}$ predicted by the model for decay (based on equilibrium theory), plotted for values of $H_{m} / E$ and $2 H_{c} / E$ that scan the rugged invariant parameter space. (a) The value of $2 H_{c} / E$ is held fixed for each curve and $H_{m} / E$ is varied. (b) The value of $H_{m} / E$ is held fixed for each curve and $2 H_{c} / E$ is varied.

![](https://cdn.mathpix.com/cropped/2025_11_22_01b55a8eb5b78892b809g-15.jpg?height=1531&width=573&top_left_y=108&top_left_x=113)
FIG. 13. The predictions of the equilibrium-based decay model are compared with results from the dissipative Galerkin model simulations. The final values of $E_{v} / E_{b}$ are plotted versus the initial $2 H_{c} / E$ for the simulated results, and for the predictions of the model. The curves shown are (a) initial $H_{m} / E=0.15$, (b) initial $H_{m} / E=0.23$, and (c) initial $H_{m} / E=0.3$.

scales, thereby neglecting forward-transfer processes such as the minority species effect ${ }^{17}$ and those discussed in Dobrowolny et al. ${ }^{12}$ and Grappin et al., ${ }^{18}$ which can also lead to growth of $2 H_{c} / E$. Since the predictions of the model seem to reliably account for the growth of $2 H_{c} / E$ when back-transfer is operating, it is possible that the other dynamic alignment processes play a diminishing role as the initial $H_{m} / E$ is increased.

## IX. DISCUSSION AND CONCLUSIONS

In this paper we have attempted to provide a fairly comprehensive picture of homogeneous 3-D MHD turbulence in
a highly simplified low-order Galerkin model. The two aspects of the turbulent evolution that have been our main focus are the "fast processes" that drive the flows toward near-equipartition of kinetic and magnetic energies, and the balance that is struck between selective decay and dynamic alignment processes, occurring on slower time scales and giving rise to a rough classification of the types of time asymptotic states that emerge.

We have found that certain features of the time asymptotic behavior of decaying 3-D MHD in this model can be reasonably well understood, particularly when magnetic helicity is present, by appeal to minimal energy principles. In addition, the systematic spectral transfer of the rugged invariants that plays a central role in driving the system toward organized final states occurs in a manner consistent with inferences drawn from the absolute equilibrium ensemble theory for ideal 3-D MHD. By appeal to these wellknown methods, we have been able to at least approximately uncover the nature of the competition between selective decay and dynamic alignment processes in this model of decaying 3-D MHD turbulence. This "classification" of types of 3-D MHD turbulence in accordance with initial rugged invariant data has a direct precedent in previous studies of the competition between the selective decay and dynamic alignment processes ${ }^{19}$ performed for decaying 2-D MHD turbulence. In addition, two other mechanisms of 3-D MHD turbulent relaxation have been presented in this work. The first of these depends upon spectral back-transfer of $H_{c}$, recently conjectured by Stribling and Matthaeus ${ }^{37}$ for dissipative flows, and amounts to a new mechanism for growth of veloc-ity-magnetic field correlation. The second is the "fast" relaxation of $E_{v} / E_{b}$ toward $O(1)$ values, driven by the tendency of spectral transfer to reach the absolute equilibrium $E_{v} / E_{b}$.

In our analysis of the decay runs, we made extensive use of absolute equilibrium theory, which provides information about time asymptotic ideal spectral shapes, as a function of the initial rugged invariant ratios $H_{m} / E$ and $2 H_{c} / E$. This enabled a qualitative determination of the degree of influence of selective decay, dynamic alignment, and the $E_{v} / E_{b}$ equipartitioning relaxation processes as our ensemble of decay runs scanned the space of initial values of $H_{m} / E$ and $2 H_{c} / E$. We found that this approach was reasonably successful in the context of this low-order 3-D MHD Galerkin model: The equilibrium ensemble-based theories for early time $E_{v} / E_{b}$ saturation (Sec. IV) and for long time decay (Sec. VIII) were seen to have a certain level of predictive power. Extrapolation of these results to high Reynolds number MHD turbulence is yet another matter, and one must be extremely cautious in any attempts to draw detailed or quantitative inferences about these more realistic types of MHD turbulence (or their requisite high resolution simulations) on the basis of the present results.

There are actually several impediments to the direct application of low-order Galerkin decay results to more realistic MHD turbulence with high Reynolds numbers. An obvious limitation is that the present truncation would fall far short of permitting dynamical resolution of structures near the dissipation scales for flows with much smaller dissipation coefficients. The present numerical results will entirely
miss effects, such as those associated with small-scale coherent structures, that may appear only in systems with many greater degrees of freedom. In addition, coherent structures could form in systems with a large number of degrees of freedom in which periodic boundary conditions are not assumed. The coherent structures could give rise to regions in the fluid where the Lagrange multipliers, $\alpha$ and $\varphi$ in the minimum energy integral of Eq. (5), are constant, separated by regions where they are not. ${ }^{4}$ However, even in the runs presented we have made no attempt to completely resolve structures at all scales that might appear with the values of the dissipation coefficients we have used. This is responsible for a systematic effect in the present simulation results: Energy (and other rugged invariants) is "reflected" from the high wave-number boundary of the Galerkin domain, and additional excitations remain in the dynamical system that would otherwise be dissipated at unretained smaller scales. This produces an artificial enhancement to the separation between the decay and spectral transfer time scales, and the possibility that a greater degree of agreement with absolute equilibrium theory than might occur if many more Fourier modes were included. For example, in similar low-order simulations of Navier-Stokes turbulence with codes of this type, ${ }^{41}$ it was found that the rugged invariant spectra had shapes characteristic of absolute equilibrium instead of the Kolmogorov type.

On the other hand, though spectra of the type expected in high Reynolds number turbulence are not achieved in the dissipative low-order Galerkin model, certain essential features of spectral transfer can be expected to be in the same sense as that in high Reynolds number flow. The most important of these is that dissipation is progressively more effective at shorter wavelength in the low-order case, as it also is in a well-resolved high Reynolds number case. Thus there is a net flow of direct-transferred excitations (e.g., energy) to shorter scales, and a relative absence of dissipation at the longest wavelengths. (The problem is, of course, that this disparity is not great enough in the low-order model.) Since the rugged conservation laws, and the differences in transfer direction inferred from them, operate in the same sense regardless of the truncation size, the same sort of segregation into back-transferred and direct-transferred excitations is expected in the low-order model, as in the high-resolution model. In fact, the long-wavelength condensation effects seen in the ideal absolute equilibrium model become more pronounced when more Fourier modes are retained. Consequently, if back-transfer effects, such as selective decay or dynamic alignment, are observed in a low-order dissipative model, they can be reasonably expected, as well in high resolution models with similar global parameters. The outstanding question for such cases is whether the enhanced dissipation expected in a high-resolution model would allow the system to survive long enough to permit the back-transfer effects to be realized.

Similar criticisms can also be developed regarding the cases of the "fast" processes described here by which $E_{v} / E_{b} \rightarrow O(1)$ at early times in the low-order decay runs. One may legitimately question whether high Reynolds number turbulence runs would display these same characteris-
tics, in view of the potential for spectral transfer artifices in the present runs, especially at high wave number. For example, magnetic field line stretching may make important high wave-number contributions to magnetic energy amplification in high initial kinetic energy runs. However, various theories, some relying on nonunit magnetic Prandtl number, have envisioned exponential magnetic energy growth in such cases. ${ }^{42,43}$ "Fast" kinematic dynamos ${ }^{44}$ are another example where this behavior is expected. In the present cases, we attributed the rapid evolution toward order-one equipartition to the statistical tendencies embodied in the ideal absolute equilibrium ensemble, which again may influence both low-order and high-resolution simulations in qualitatively similar fashion. The equilibrium ensemble basis for dynamo processes was previously discussed in some detail by Kraichnan and Nagarajan. ${ }^{39}$ Early time growth of kinetic energy for initially magnetic-energy-dominated MHD turbulence has been a relatively less well-studied situation, although a number of simulation studies have reported such effects, ${ }^{9}$ which are sometimes seen to be transient. Generically, magnetic reconnection is frequently cited as a process that converts magnetic energy into flow energy and heat.

In summary, the study of MHD turbulence in the present low-order Galerkin model, despite its limitations, provides an overview of both the fast and slow relaxation processes that can occur. A qualitative, and to some degree, predictive, perspective has been developed regarding the tendency toward near-equipartition between magnetic and kinetic energies at early times, and the balance between selective decay and dynamic alignment that is expected at later times. The overall viewpoint developed here for the low-order model may fall short of providing quantitative or predictive information regarding high Reynolds number MHD turbulence involving many more degrees of freedom, but may nevertheless provide important guidance for understanding qualitative features of MHD turbulence in various parameter regimes. The utility of these results remains to be determined by future extensive high-resolution MHD computations.

## ACKNOWLEDGMENTS

We would like to thank S. Oughton for a careful reading of the manuscript.

This research has been supported by NASA through Grant No. NGT-50338, and through the Space Physics Theory Program grants at NASA-GSFC and at Bartol, and by the National Science Foundation (NSF) under Grant No. ATM-8913627. Computational facilities were provided by the NSF-supported San Diego Supercomputing Center.

[^0]${ }^{6}$ J. C. Higdon, Astrophys. J. 285, 109 (1984).
${ }^{7}$ J. Heyvarts and E. Priest, Astron. Astrophys. 137, 63 (1984).
${ }^{8}$ E. Parker, Cosmical Magnetic Fields: Their Origin and Activity (Oxford U.P., Oxford, England, 1979).
${ }^{9}$ R. B. Dahlburg. J. P. Dahlburg, and J. T. Mariska, Astron. Astrophys. 198, 300 (1988).
${ }^{10}$ P. J. Coleman, Astrophys. J. 153, 371 (1968).
${ }^{11}$ J. W. Belcher and L. Davis, J. Geophys. Res. 76, 3534 (1971).
${ }^{12}$ M. Dobrowolny, A. Mangeney, and P. L. Veltri, Phys. Rev. Lett. 45, 144 (1980).
${ }^{13}$ W. H. Matthaeus and M. L. Goldstein, J. Geophys. Res. 87, 6011 (1982).
${ }^{14}$ F. Krause and K.-H. Rädler, Mean-Field Magnetohydrodynamics and Dynamo Theory (Academy-Verlag, Berlin, 1980).
${ }^{15}$ H. K. Moffatt, Magnetic Field Generation in Electrically Conducting Fluids (Cambridge, U.P., Cambridge, 1978).
${ }^{16}$ W. H. Matthaeus and D. Montgomery, Ann. N.Y. Acad. Sci. 357, 203 (1980).
${ }^{17}$ W. H. Matthaeus, M. Goldstein, and D. Montgomery, Phys. Rev. Lett. 51, 1484 (1983).
${ }^{18}$ R. Grappin, U. Frisch, J. Léorat, and A. Pouquet, Astron. Astrophys. 105, 6 (1982).
${ }^{19}$ A. C. Ting, W. H. Matthaeus, and D. Montgomery, Phys. Fluids 29, 3261 (1986).
${ }^{20}$ S. Ghosh and W. H. Matthaeus, Phys. Fluids B 2, 1520 (1990).
${ }^{21}$ L. Woltjer, Proc. Nat. Acad. Sci. 44, 489 (1958); 44, 833 (1958); 45, 769 (1959).
${ }^{22}$ T. D. Lee, Q. Appl. Math. 10, 69 (1952).
${ }^{23}$ R. H. Kraichnan, Phys. Rev. A 109, 1407 (1958).
${ }^{24}$ U. Frisch, A. Pouquet, J. Léorat, and A. Mazure, J. Fluid Mech. 68, 769 (1975).
${ }^{25}$ A. Pouquet, U. Frisch, and J. Léorat, J. Fluid Mech. 77, 321 (1976).
${ }^{26}$ R. H. Kraichnan, Phys. Fluids 8, 1385 (1965).
${ }^{27}$ A. Pouquet and G. S. Patterson, J. Fluid Mech. 85, 305 (1978).
${ }^{28}$ W. H. Matthaeus and D. Montgomery, in Statistical Physics and Chaos in Fusion Plasmas, edited by C. W. Horton and L. E. Reichel (Wiley, New York, 1984), p. 285.
${ }^{29}$ A. Pouquet, M. Meneguzzi, and U. Frisch, Phys. Rev. A 33, 4266 (1986).
${ }^{30}$ M. Meneguzzi, U. Frisch, and A. Pouquet, Phys. Rev. Lett. 47, 1069 (1981).
${ }^{31}$ D. D. Schnack, D. C. Baxter, and E. J. Caramana, J. Comput. Phys. 55, 108 (1985).
${ }^{32}$ A. Y. Aydemir and D. C. Barnes, J. Comput. Phys. 59, 108 (1985).
${ }^{33}$ E. N. Lorenz, J. Atmos. Sci. 20, 130 (1963).
${ }^{34}$ R. H. Kraichnan and D. Montgomery, Rep. Prog. Phys. 43, 35 (1980).
${ }^{35}$ R. H. Kraichnan, Phys. Fluids 10, 1457 (1967).
${ }^{36}$ D. Fyfe and D. Montgomery, J. Plasma Phys. 16, 181 (1976).
${ }^{37}$ T. Stribling and W. H. Matthaeus, Phys. Fluids B 2, 1979 (1990).
${ }^{38}$ R. N. Sudan, Phys. Rev. Lett. 42, 1277 (1979); in Modern Plasma Physics (IAEA, Vienna, 1981).
${ }^{39}$ R. H. Kraichnan and S. Nagarajan, Phys. Fluids 10, 859 (1967).
${ }^{40}$ S. Riyopoulos, A. Bondeson, and D. Montgomery, Phys. Fluids 25, 107 (1982).
${ }^{4!}$ A. F. Bennett and D. B. Haidvogel, J. Atmos. Sci. 40, 738 (1983).
${ }^{42}$ G. K. Batchelor, Proc. R. Soc. London Ser. A 201, 405 (1950).
${ }^{43}$ Y.-H. Pao, Phys. Fluids 6, 632 (1963).
${ }^{44}$ J. M. Finn and E. Ott, Phys. Fluids B 2, 916 (1990).


[^0]:    ${ }^{1}$ G. K. Batchelor, The Theory of Homogeneous Turbulence (Cambridge U.P., Cambridge, 1953).
    ${ }^{2}$ J. B. Taylor, Phys. Rev. Lett. 33, 1139 (1974).
    ${ }^{3}$ D. Montgomery, L. Turner, and G. Vahala, Phys. Fluids 21, 757 (1978).
    ${ }^{4}$ J. Dahlburg, D. Montgomery, G. Doolen, and L. Turner, Phys. Rev. Lett. 57, 428 (1986); J. Plasma Phys. 37, 299 (1987).
    ${ }^{5}$ R. Horiuchi and T. Sato, Phys. Rev. Lett. 55, 211 (1985); Phys. Fluids 29, 1161 (1986).

