# Relaxation in two dimensions and the "sinh-Poisson" equation 

D. Montgomery<br>Department of Physics, Dartmouth College, Hanover, New Hampshire 03755-3528<br>W. H. Matthaeus, W. T. Stribling, D. Martinez, and S. Oughton<br>Bartol Research Institute, University of Delaware, Newark, Delaware 19716

(Received 30 May 1991; accepted 4 September 1991)


#### Abstract

Long-time states of a turbulent, decaying, two-dimensional, Navier-Stokes flow are shown numerically to relax toward maximum-entropy configurations, as defined by the "sinhPoisson" equation. The large-scale Reynolds number is about 14000 , the spatial resolution is $(512)^{2}$, the boundary conditions are spatially periodic, and the evolution takes place over nearly 400 large-scale eddy-turnover times.


Two-dimensional Navier-Stokes (2-D NS) turbulence, though a somewhat artificial construct, has continued to generate interest for almost 50 years. ${ }^{1-3}$ Suitably elaborated, it contains implications for areas as diverse as meteorology, oceanography, and liquid helium; it exhibits in uncluttered form effects that are important in all those subjects. In addition, its dynamics are isomorphic to those of the electrostatic guiding-center plasma, which have been widely extended to describe strongly magnetized plasmas.

What we wish to report here is an additional conclusion from some recently reported ${ }^{4,5}$ high-resolution (512 ${ }^{2}$ ) 2-D NS spectral-method computations at very long times (many large-scale eddy-turnover times). Since Refs. 4 and 5 were prepared, the data have led us to an additional conclusion which we could previously only entertain as a hypothesis. Namely, after a few hundred large-scale eddyturnover times, decaying 2-D NS turbulence, at high largescale Reynolds number (initially 14286 ) in periodic boundary conditions, relaxes to a state quite close to the maximum entropy, or "most probable," state described by the $\sinh$-Poisson equation. ${ }^{6,7}$

The sinh-Poisson equation derives from a continuum (or "mean field") limit of a very large number of interacting, ideal, parallel line vortices. It is not necessary to review in detail the rather large literature that has accumulated around it. ${ }^{8-21}$ A good bibliography has recently been collected by Smith. ${ }^{20}$ The conclusion we report here, without being able wholly to explain it, is that the decay of viscous 2-D NS turbulence is rather well fit by this ideal theory: far better than any alternative theory to date.

Our computations ${ }^{4,5}$ are of a type that have been extensively reported: Orszag-Patterson, fully dealiased, spec-tral-method computations ${ }^{22}$ inside a square box of edge $2 \pi$. A considerably more detailed description of the computa-
tions may be found in Refs. 4 and 5. An initially highly turbulent velocity distribution decays with a dimensionless characteristic energy-decay time at the largest scales of the order of 14000 . By 1979, it had become clear ${ }^{23}$ that likesign vortex capture was the most striking dynamical process involved and that it led to a streamline topology that could be ultimately dominated by a single large convection cell of either sense of rotation. A "selective decay" hypothesis, ${ }^{23}$ based on unequal decay rates of enstrophy and energy, was offered as the explanation.

In 1984, McWilliams ${ }^{24}$ (and later Brachet et al. ${ }^{25}$ ) produced 2-D NS decay computations that were both more highly resolved and of higher Reynolds number and that suggested to them the eventual cessation of like-sign vortex merger. They proposed a relaxed state consisting of dense highly symmetric cores of vorticity wandering about randomly, with a negligible amount of interaction and spectral transfer.

Our recent computation ${ }^{4,5}$ has been chosen to have initial conditions as close as possible to those of McWilliams, differing mainly in the absence of any smallscale smoothing and in the presence of slightly higher spatial resolution. The only significant difference has been in the duration of the run (almost 400 large-scale eddy-turnover times, compared to 40 ). During the times overlapping in the two sets of computations, no significant differences appeared. However, we found that at long times like-sign vortex capture did not cease, but only slowed down. By $t=220$, all possible like-sign vortex captures had occurred, and only one vortex and associated convection cell of either sign remained.

The various details of the two-vortex final state are displayed in the previous papers, ${ }^{4,5}$ to which we refer the reader for details. We describe here evidence for what

![](https://cdn.mathpix.com/cropped/2025_11_22_6388833752692ff3189cg-2.jpg?height=500&width=700&top_left_y=121&top_left_x=162)
FIG. 1. Scatter plot of the streamfunction $\psi$ versus the vorticity $\omega$ at time $t=374$. The curve drawn through the plotted points is $c^{-1} \sinh (|\beta| \psi)$. (For a "selectively decayed" state, there is a simple proportionality between $\psi$ and $\omega$.)

![](https://cdn.mathpix.com/cropped/2025_11_22_6388833752692ff3189cg-2.jpg?height=570&width=760&top_left_y=116&top_left_x=1078)
FIG. 2. Evolving spatially averaged cross-correlations between $\omega$ and $\sinh (|\beta| \psi)$ and $\psi$ (upper and lower curves), computed as a function of time. $C=1$ would indicate a pointwise proportionality between its arguments. (The lower curve is $C$ for the "selective decay" hypothesis, which can be considered the best existing alternative theory.)

![](https://cdn.mathpix.com/cropped/2025_11_22_6388833752692ff3189cg-2.jpg?height=1527&width=1787&top_left_y=975&top_left_x=157)
FIG. 3. Three-dimensional perspective plot of the computed vorticity versus $x$ and $y$ at four different times. (For clarity, the origin of coordinates has been consistently translated so that both the large vortices in the final state will lie entirely within the basic periodic box.)

![](https://cdn.mathpix.com/cropped/2025_11_22_6388833752692ff3189cg-3.jpg?height=1543&width=1785&top_left_y=92&top_left_x=181)
FIG. 4. Three-dimensional perspective plot of the computed streamfunction versus $x$ and $y$ at four different times.

could previously only be suggested. Namely, between $t \cong$ 292 and $t=374$, and presumably on to the large-scale en-ergy-decay time of $t \cong 14000$, the streamfunction and vorticity obey, to a good approximation, a local relationship

$$
\begin{equation*}
c \omega=\sinh (|\beta| \psi), \tag{1}
\end{equation*}
$$

where $\omega$ is the vorticity and $\psi$ is the streamfunction. The constants $c$ and $|\beta|$ are determined, at $t=374$, by a leastsquares fit, to be $c \cong 7.7$ and $\beta \cong-2.1$. This is the necessary and sufficient condition that a sinh-Poisson equilibrium has been reached.

Figure 1 is a scatter plot of the computed $\psi$ versus the computed $\omega$, taken pointwise over $(x, y)$ space. The solid curve drawn through the points is Eq. (1). (A "selectively decayed" state would have exhibited a simple proportionality between $\psi$ and $\omega$.)

It is easy to multiply evidence of the kind displayed in Fig. 1, which changes little from one instant to the next. We may consider, for example, cross-correlations of func-
tions involving $\psi$ and $\omega$ as measures of the extent to which solutions of the sinh-Poisson equation have been reached. We may define

$$
C(f, g) \equiv \frac{\langle(f-\langle f\rangle)(g-\langle g\rangle)\rangle}{\left[\left\langle(f-\langle f\rangle)^{2}\right\rangle\left\langle(g-\langle g\rangle)^{2}\right\rangle\right]^{1 / 2}},
$$

where the angle brackets indicate a spatial average. Figure 2 is a computed plot of the cross-correlations $C[\omega, \sinh (|\beta| \psi)]$ and $C(\omega, \psi)$ versus time; $C=1$ would indicate a perfect proportionality for the two arguments of $C$. It is seen that $C[\omega, \sinh (|\beta| \psi)]$ increases with time to $\cong 0.97$ and is throughout a significantly better predictor than $C(\omega, \psi)$, becoming particularly good after the final vortex merger. The values of $c$ and $\beta$ drift only a little. It is also possible to make the fit even better by permitting a slight asymmetry between the positive and negative vorticity regions, ${ }^{10,11}$ but we have not done that here. In partic-
ular, the slight separation of the curve and the scatter plot at the largest values of $\psi$ can be significantly reduced in Fig. 1.

Figures 3 and 4 provide a less quantitative but perhaps nonetheless valuable picture of the evolution toward the quasistationary final state. Figure 3 shows several threedimensional perspective plots of vorticity versus $x$ and $y$ at times ranging from early ones, in which the initially random turbulence is present, to late ones in which the two dominant vortices have assumed what seem to be their late-time profiles. Figure 4 is a similar sequence of plots of the streamfunction. The visual displays perhaps make more vivid and accessible the information implicit in the $\mathbf{9 7 \%}$ correlation level of Fig. 2.

The more difficult problem is how to account convincingly for the result. The sinh-Poisson equation is derived in the simplest way by assuming statistical-mechanical behavior, of an information-theoretic or Jaynesian ${ }^{26}$ kind, for a system which conserves energy, total amount of positive and negative vorticity separately, and nothing else. If we define two non-negative vorticity fields $\omega^{+}, \omega^{-}$with 2-D equations of evolution

$$
\begin{equation*}
\frac{\partial \omega^{ \pm}}{\partial t}+v \cdot \nabla \omega^{ \pm}=v \nabla^{2} \omega^{ \pm} \tag{2}
\end{equation*}
$$

then $\omega \equiv \omega^{+}-\omega^{-}$obeys the 2-D NS vorticity equation if $\mathbf{v}=\boldsymbol{\nabla} \psi \times \widehat{e}_{z}$ and $\boldsymbol{\nabla}^{2} \psi=-\omega^{+}+\omega^{-}=-\omega$. (The geometry is the conventional one with the activity lying in the $x-y$ plane.)

In periodic boundary conditions, Eqs. (2) conserve $\int \omega^{ \pm} d x d y$ separately, and these two integrals need not vanish (only their difference vanishes). In 2-D NS flow, energy is not conserved, but decays very slowly at high Reynolds numbers. For instance, in the run reported, over $80 \%$ of the initial energy remains after $t=292$, while less than $2 \%$ of the enstrophy remains.

Thus, with these three constants of the motion, two rigorous ( $\int \omega^{ \pm} d x d y$ ) and one approximate [energy $=(1 /$ 2) $\int \omega \psi d x d y$ ], the conservation conditions for the applicability of the maximum entropy theory are met. What is missing is a clear sense of the quasiergodic, or "mixing," behavior that the continuous, viscous Navier-Stokes fluid must exhibit. Some such behavior would appear to provide a basis for the entropy maximization which leads to the sinh-Poisson equation. The behavior is not familiar, and may require time to elucidate. But is appears to us as a fact of life which the theory of decaying 2-D Navier-Stokes turbulence will hereafter need to deal with.

It would be desirable to investigate the details of the relaxation process's dependence on a variety of initial conditions, and to some extent this has been done, but only at significantly lower resolution. ${ }^{4,5}$ The single run reported here consumed over 600 h of Cray YMP time and required three years to complete. Extensive exploration of the effects of a wide variety of initial turbulence must await the development of a great deal more computational capacity.

## ACKNOWLEDGMENTS

This research has been supported in part by National Science Foundation Grant No. ATM-89131627 and NASA Grant No. NGT-50338 at Bartol, and NASA Grant No. NAG-W-710 and U. S. Department of Energy Grants No. DE-FG02-85ER-53194 and No. DE-FG02-85ER-53298 at Dartmouth. The computations were supported by the National Science Foundation San Diego Supercomputing Center.
${ }^{1}$ C. C. Lin, On the Motion of Vortices in Two Dimensions (University of Toronto Press, Toronto, 1943).
${ }^{2}$ L. Onsager, "Statistical Hydrodynamics," Nuovo Cimento Suppl. 6, 279 (1949).
${ }^{3}$ R. H. Kraichnan and D. Montgomery, "Two-Dimensional Turbulence," Rep. Prog. Phys. 43, 547 (1980).
${ }^{4}$ W. H. Matthaeus, W. T. Stribling, D. Martinez, S. Oughton, and D. Montgomery, "Selective decay and coherent vortices in two-dimensional incompressible turbulence," Phys. Rev. Lett. 66, 2731 (1991).
${ }^{5}$ W. H. Matthaeus, W. T. Stribling, D. Martinez, S. Oughton, and D. Montgomery, "Decaying two-dimensional, Navier-Stokes turbulence at very long times," Physica D (in press).
${ }^{6}$ G. Joyce and D. Montgomery, "Negative temperature states for a twodimensional guiding-centre plasma," J. Plasma Phys. 10, 107 (1973).
${ }^{7}$ D. Montgomery and G. Joyce, "Statistical mechanics of negative temperature states," Phys. Fluids 17, 1139 (1974).
${ }^{8}$ B. E. McDonald, "Numerical calculation of nonunique solutions of a two-dimensional sinh-Poisson equation," J. Comput. Phys. 16, 630 (1974).
${ }^{9}$ D. L. Book, B. E. McDonald, and S. Fisher, "Steady-state distributions of interacting discrete vortices," Phys. Rev. Lett. 34, 4 (1975).
${ }^{10}$ Y. B. Pointin and T. S. Lundgren, "Statistical mechanics of two-dimensional vortices in a bounded container," Phys. Fluids 19, 1459 (1976).
${ }^{11}$ T. S. Lundgren and Y. B. Pointin, "Non-Gaussian probability distributions for a vortex fluid," Phys. Fluids 20, 356 (1977).
${ }^{12}$ T. S. Lundgren and Y. B. Pointin, "Statistical mechanics of two-dimensional vortices," J. Stat. Phys. 17, 323 (1978).
${ }^{13}$ J. H. Williamson, "Statistical mechanics of a guiding-centre plasma," J. Plasma Phys. 17, 85 (1977).
${ }^{14}$ D. Montgomery, L. Turner, and G. Vahala, "Most probable states in magnetohydrodynamics," J. Plasma Phys. 21, 239 (1979).
${ }^{15}$ J. Ambrosiano and G. Vahala, "Most-probable magnetohydrodynamic tokamak and reversed-field pinch equilibria," Phys. Fluids 24, 2253 (1981).
${ }^{16}$ A. C. Ting, H. H. Chen, and Y. C. Lee, "Exact solutions of nonlinear boundary value problem: the vortices of the two-dimensional sinh-Poisson equation," Physica D 26, 37 (1987).
${ }^{17}$ R. A. Smith, "Phase transition behavior in a negative-temperature guid-ing-center plasma," Phys. Rev. Lett. 63, 1479 (1989).
${ }^{18}$ R. A. Smith and T. O'Neil, "Nonaxisymmetric thermal equilibria of a cylindrically bounded guiding-center plasma or discrete vortex system," Phys. Fluids B 2, 2961 (1990).
${ }^{19}$ D. Montgomery and Y. C. Lee, "Statistical-mechanical selection of the shapes of disk galaxies," Astrophys. J. 368, 380 (1990).
${ }^{20}$ R. A. Smith, "Maximization of vortex entropy as an organizing principle in intermitent, decaying, two-dimensional turbulence," Phys. Rev. A 43, 1126 (1991).
${ }^{21}$ L. J. Campbell and K. O'Neil, "Statistics of 2-D point vortices and high energy vortex states," J. Stat. Phys. (in press).
${ }^{22}$ D. Gottlieb and S. A. Orszag, Numerical Analysis of Spectral Methods: Theory and Application, NSF-CBMS Monograph No. 26 (SIAM, Philadelphia, 1977).
${ }^{23}$ W. H. Matthaeus and D. Montgomery, "Selective decay hypothesis at high mechanical and magnetic Reynolds numbers," Ann. N.Y. Acad. Sci. 357, 203 (1980).
${ }^{24}$ J. C. McWilliams, "The emergence of isolated vortices in turbulent flow," J. Fluid Mech. 146, 21 (1984).
${ }^{25}$ M. Brachet, M. Meneguzzi, H. Politano, and P. Sulem, "The dynamics of freely decaying two-dimensional turbulence," J. Fluid Mech. 194, 333 (1988).
${ }^{26}$ E. T. Jaynes, "Information theory and statistical mechanics: I and II," Phys. Rev. 106, 620 (1957); 108, 171 (1957).

