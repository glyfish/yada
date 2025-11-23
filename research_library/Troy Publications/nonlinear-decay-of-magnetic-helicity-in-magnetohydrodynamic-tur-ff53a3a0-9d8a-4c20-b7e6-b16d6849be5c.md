See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/23820855

## Nonlinear decay of magnetic helicity in magnetohydrodynamic turbulence with a mean magnetic field

Article in Journal of Geophysical Research Atmospheres • March 1994
DOI: 10.1029/93JA02962 • Source: NTRS

CITATIONS
36

3 authors, including:
![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-01.jpg?height=75&width=82&top_left_y=834&top_left_x=138)

Troy Stribling
University of Delaware
14 PUBLICATIONS 989 CITATIONS

SEE PROFILE

READS
43
![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-01.jpg?height=80&width=80&top_left_y=834&top_left_x=1062)
W. H. Matthaeus

University of Delaware
919 PUBLICATIONS 45,985 CITATIONS

SEE PROFILE

# Nonlinear decay of magnetic helicity in magnetohydrodynamic turbulence with a mean magnetic field 

Troy Stribling<br>Laboratory for Extraterrestrial Physics, NASA Goddard Space Flight Center, Greenbelt, Maryland<br>William H. Matthaeus<br>Bartol Research Institute, University of Delaware, Newark<br>Sanjoy Ghosh<br>Laboratory for Extraterrestrial Physics, NASA Goddard Space Flight Center, Greenbelt, Maryland


#### Abstract

We show that the magnetic helicity associated with fluctuations in homogeneous incompressible magnetohydrodynamic (MHD) turbulence with a mean magnetic field decays in time because of nonlinear processes. Evidence is obtained numerically, by use of both dissipative and nondissipative spectral method simulations. The described effect stands in contrast to expectations based on studies of MHD turbulence without an applied mean field, in which magnetic helicity is transferred nonlinearly to long wavelengths and is preserved in time because of selective decay when dissipation is present. The process of nonlinear decay is described in terms of a generalized ideal helicity invariant and is characterized by the transient production of a mean induced electric field aligned with the applied magnetic field, an effect reminiscent of the alpha effect in dynamo theory. A simple phenomenological model for the decay process is proposed.


## Introduction

Magnetic helicity ( $H_{m}$ ) is a particularly important measure of the mirror asymmetry of a magnetic field in magnetohydrodynamics (MHD), because it is conserved in the absence of ohmic dissipation for a variety of boundary conditions. This conservation law is central in the arguments given by Frisch et al. [1975] and coworkers for the inverse cascade phenomenon in three-dimensional incompressible MHD turbulence, an effect which is driven by spectral transfer of $H_{m}$ to long wavelengths. The same propensity for $H_{m}$ to be "back transferred" has been cited as a contributor to efficient magnetic dynamo activity in forced [Pouquet and Patterson, 1978; Meneguzzi et al., 1981] and freely decaying MHD [Pouquet et al., 1976; Stribling and Matthaeus, 1991]. In freely decaying MHD turbulence, relaxation through the selective decay process occurs because $H_{m}$ is back transferred to long wavelengths where dissipation is weak [Montgomery et al., 1978; Matthaeus and Montgomery, 1980; Riyopoulos et al., 1982; Taylor,

[^0]Paper number 93JA02962.
0148-0227/94/93JA-02962\$5.00

1974]. In these theoretical arguments, it is crucial that $H_{m}$ is a "rugged" invariant in the absence of dissipation [Frisch et al., 1975]. However, these arguments have generally been developed for magnetofluids that are, in effect, isolated, through the use of perfectly conducting boundary conditions or the use of periodic boundary conditions. For these cases, magnetic field lines either do not leave the volume containing the turbulence or, for the periodic case, close in a finite region of space.

On the other hand, particularly in space physics and astrophysics applications, homogeneous MHD turbulence concepts are applied to local samples of the fluid plasma, while externally supported magnetic fields can thread the region without closing in the region of interest. This alternative situation may eventually prove to be more relevant than the case of "isolated" homogeneous turbulence which is often modeled using periodic boundary conditions with zero volume averaged magnetic field. The basic underpinning of helicity dynamics in MHD turbulence theory, that is, the ideal conservation of $H_{m}$, needs to be reconsidered in this case.

In this paper we examine the conservation properties of $H_{m}$ for a simple model in which the MHD turbulence is periodic but evolves in the presence of a specified, externally supported uniform magnetic field. We show, by considering the helicity conservation law and by using a direct numerical solution of the three di-
mensional (3D) MHD equations, that helicity behaves dynamically in a somewhat different way than in the case of magnetically isolated MHD turbulence. Analogous changes in behavior of magnetic helicity have, for some time, been studied in current-carrying laboratory plasmas [e.g. Dahlburg et al., 1987a,b]. The dynamical properties of magnetic helicity that we find in these direct simulations of MHD have clear implications for approximate theoretical treatments of astrophysical MHD turbulence such as mean field electrodynamics [Krause and Radler, 1980; Moffatt, 1978; Zeldovich et al., 1983].

The magnetic helicity of a turbulent magnetofluid is defined as

$$
\begin{equation*}
H_{m}=\langle\mathbf{a} \cdot \mathbf{b}\rangle \tag{1}
\end{equation*}
$$

where $\mathbf{b}$ is the fluctuating magnetic field, $\mathbf{b}=\nabla \times \mathbf{a}$ defines the vector potential $\mathbf{a}$, and $\rangle$ denotes a spatial average. The fluctuation magnetic field $\mathbf{b}$ is assumed to have zero mean, and it is convenient to adopt the Coulomb gauge in which $\nabla \cdot \mathbf{a}=0$. Magnetic helicity can be interpreted, as suggested by Moffatt [1978], as a measure of linkage of magnetic flux tubes. Also, if one Fourier transforms b, with the Fourier coefficients indexed by wave vector $\mathbf{k}$, then $H_{m}$ provides a measure of the polarization of the Fourier amplitudes $\mathbf{b}(\mathbf{k})$. Useful background discussion of helicities of magnetic and velocity fields are found in the monograph by Moffatt [1978] and the recent review by Moffatt and Tsinober [1992].

Spatially periodic MHD without a uniform applied magnetic field, that is, $\mathbf{B}_{0}=0$, is a model frequently used to represent a sample of spatially homogeneous turbulence. For this case, there are three known rugged invariants, conserved by arbitrary truncations of the Galerkin representations of the incompressible MHD equations [Frisch et al., 1975; Stribling and Matthaeus, 1990]. In terms of the fluctuating magnetic field $\mathbf{b}$ and the fluctuating velocity field $\mathbf{v}$, these are the total energy (per unit mass) $\left.E=\left.\langle | \mathbf{v}\right|^{2}+|\mathbf{b}|^{2}\right\rangle / 2$, the cross helicity $H_{c}=\langle\mathbf{v} \cdot \mathbf{b}\rangle$, and the magnetic helicity $H_{m}=\langle\mathbf{a} \cdot \mathbf{b}\rangle$, where the volume average is over the periodic cube. For the case of present interest, with $\mathbf{B}_{0} \neq 0$ and the entire magnetic field denoted by $\mathbf{B}=\mathbf{B}_{0}+\mathbf{b}$, the total energy and cross helicity remain rugged invariants. As defined above, $H_{m}$ is gauge invariant in periodic geometry, but it refers only to the helicity associated with the magnetic fluctuation. However, one can easily verify that the magnetic helicity is no longer an invariant. Instead, the ideal magnetic induction equation $\partial \mathbf{B} / \partial t=\nabla \times(\mathbf{v} \times \mathbf{B})=-\nabla \times \mathbf{E}$ implies ideal conservation of a quantity that might be called the "total magnetic helicity" [Matthaeus and Goldstein, 1982] defined by

$$
\begin{equation*}
\hat{H}_{m}=H_{m}+2 \mathbf{B}_{0} \cdot \mathbf{A}_{0} \tag{2}
\end{equation*}
$$

Constancy of $\hat{H}_{m}$ is demonstrated in the appendix. The quantity $d \mathbf{A}_{0} / d t=\langle\mathbf{v} \times \mathbf{b}\rangle=-\mathbf{E}_{0}$ is the negative of the volume-averaged induced electric field and can be interpreted as the time derivative of the $\mathbf{k}=0$ component of the vector potential, $\mathbf{A}_{0}=\langle\mathbf{a}\rangle$. However, note that $\nabla \times \mathbf{A}_{0}=0 \neq \mathbf{B}_{0}$, since $\mathbf{A}_{0}$ is a property
of the fluctuating magnetic field only. Nevertheless, it may be possible to interpret the $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ term of $\hat{H}_{m}$ as a local dynamical contribution to the magnetic flux linkages that might exist at scales much larger than the periodicity length of $\mathbf{b}$ [Moffatt, 1978; Matthaeus and Goldstein, 1982]. Although such an interpretation goes beyond the purely periodic model we use here, it will presently become clear that the theoretical issues we address are related closely to mean field theories involving locally homogeneous turbulence and its effect upon larger-scale inhomogeneous MHD structures. Some issues that arise in relating periodic results to weakly inhomogeneous systems are discussed in the appendix.

Our principal purpose here is to examine how the change from nondissipative invariance of $H_{m}$ to invariance of $\hat{H}_{m}$ when $\mathbf{B}_{0} \neq 0$ influences the character of the turbulence. We concentrate, in this preliminary report, on the global behavior of the helicity, deferring discussion of the spectral properties of the turbulence to a later time. There would appear to be three possibilities with regard to the nonlinear nondissipative evolution of $\hat{H}_{m}$, which have not been distinguished in the previous literature as far as we are aware. First, the new term $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ might tend to average to zero over time, a possibility that might not produce great changes to mechanisms that depend upon inverse transfer processes. Second, one might suspect that $2 \mathbf{B}_{0} \cdot \mathbf{A}_{0}$ might tend to become statistically equipartitioned with $H_{m}$, with concomitant effects on spectral transfer. Finally, $H_{m}$ might decay in favor of $2 \mathbf{B}_{0} \cdot \mathbf{A}_{0}$. The difficulty in distinguishing these possible outcomes on the basis of theoretical arguments is compounded by the nature of the new ideal conservation law, which is of a type that differs from previous experience with rugged invariants in MHD. Specifically, the time evolution of $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ depends upon the time history of the turbulence, since $\mathbf{A}_{0}(\mathbf{x}, t)=\mathbf{A}_{0}(\mathbf{x}, 0)-\int_{0}^{t} \mathbf{E}_{0}\left(\mathbf{x}, t^{\prime}\right) d t^{\prime}$. Consequently, we have appealed to numerical simulations to provide guidance, arriving at the conclusion that the third possibility cited best describes the tendencies seen in both dissipative and nondissipative 3D incompressible MHD flows. The implications of this result for inhomogeneous MHD in a mean field electrodynamic treatment is clear: in order for local turbulence to produce a nonzero $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$, one must have what amounts to an "alpha effect," in which $\mathbf{B}_{0} \cdot \mathbf{E}_{0} \neq 0$. We are aware of no first-principle arguments that imply this result, which appears to support findings of mean field electrodynamics. We now summarize some of this numerical evidence.

## Simulation Results: Nonlinear Decay of Magnetic Helicity

We consider here the incompressible unforced 3D MHD equations in a familiar set of "Alfvén speed units":

$$
\begin{equation*}
\frac{\partial \mathbf{v}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{v}=-\nabla p^{*}+\mathbf{b} \cdot \nabla \mathbf{b}+\mathbf{B}_{0} \cdot \nabla \mathbf{b}+\nu \nabla^{2} \mathbf{v} \tag{3}
\end{equation*}
$$

$$
\begin{equation*}
\frac{\partial \mathbf{b}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{b}=\mathbf{b} \cdot \nabla \mathbf{v}+\mathbf{B}_{0} \cdot \nabla \mathbf{v}+\eta \nabla^{2} \mathbf{b}, \tag{4}
\end{equation*}
$$

along with the constraints $\nabla \cdot \mathbf{v}=0$ and $\nabla \cdot \mathbf{b}=0$. The fluctuating velocity and magnetic fields, $\mathbf{v}$ and $\mathbf{b}$, respectively, each have zero mean, $\mathbf{B}_{0}$ is the uniform mean magnetic field, $p^{*}$ is the total pressure (determined by the incompressibility condition), and $\nu$ and $\eta$ are the viscosity and resistivity respectively. The time unit is taken to be an eddy turnover time for unit velocity field at unit length scale.

We use a Fourier Galerkin spectral method code to solve equations (3) and (4) as an unforced initial value problem with periodic boundary conditions in a cube of side $2 \pi$. The simulations discussed here have either $8^{3}$ or $32^{3}$ independent wave vectors that are advanced in time. Temporary arrays with larger numbers of independent Fourier modes are used in the elimination of aliasing errors [Orszag, 1971]. The viscosity and resistivity, respectively, $\nu$ and $\eta$, are taken to be equal, with values of either 0.01 or zero. The errors in conservation of the relevant nondissipative invariants (including $E$ and either $H_{m}$ or $\hat{H}_{m}$ ) are easily controlled using this method by adjusting the time step in the secondorder Runge Kutta time integrator. In the simulations discussed below these errors are regulated to less than $0.01 \%$ by using a time step $\Delta t=10^{-2}$ for the $8^{3}$ runs and time steps in the range of $\Delta t=1 \times 10^{-3}$ to $2 \times 10^{-3}$ for the $32^{3}$ runs.

To show the time asymptotic tendencies of the nonlinear effects on the helicity, we first examine an $8^{3}$ run with zero dissipation. This kind of simulation, ordinarily used to examine predictions of the Gibbs absolute equilibrium ensemble, [Frisch et al., 1975; Fyfe and Montgomery, 1976; Stribling and Matthaeus, 1990] depends critically upon selection of the correct set of ideal
invariants. This particular run has $\mathbf{B}_{0}=1.0 \hat{\mathbf{z}}$, and at $t=0.0$, fluctuating magnetic strength $\delta b / B_{0}=1$, $E=1.0, H_{c}=0.1$, and $H_{m}=0.4$. The four panels of Figure 1 show the main features of this run. In Figure 1a $H_{m}$ is seen to decay from its initial value to zero in approximately 25 characteristic time units (Alfvén transit times of unit distance) and then proceeds to fluctuate about zero with an amplitude significantly less than the initial value. In Figure 1b the time history of the $\hat{\mathbf{z}}$ component of spatially averaged electric field $E_{0 z}=-\langle\mathbf{v} \times \mathbf{b}\rangle_{z}$ is given. Figure 1c depicts the time history of the $\hat{\mathbf{z}}$ component of $\mathbf{A}_{0}$ obtained from integration of $E_{0 z}$. (The initial value of $\mathbf{A}_{0}$ was arbitrarily taken to be 0.) Finally, Figure 1d illustrates conservation of $\hat{H}_{m}$ in the run, which enforces perfect anticorrelation of $E_{0 z}$ and $d H_{m} / d t$.

Figure 1 shows clearly that the initial $H_{m}$ disappears through nonlinear processes alone (since there is no dissipation) by several tens of characteristic time. The time asymptotic state is characterized by values of $H_{m}$ and $E_{0 z}$ that oscillate about zero. On the other hand, it is clear from the conservation law, equation (2), that the induced electric field $E_{0 z}$ cannot be zero during the early time period in which the helicity is decreasing. The time asymptotic state also includes a value of $A_{0 z}=\hat{\mathbf{z}} \cdot \mathbf{A}_{0}$ that oscillates about a constant nonzero value, indicating a "memory" of the magnetic helicity lost in the early decay process.

It is worthwhile to examine more closely the early phase of this nonlinear decay. We do this by using a higher resolution, $32^{3}$ simulation, again with zero dissipation and with initial magnetic helicity $H_{m}=0.2$. Figure 2 shows, in four panels, the time histories of $H_{m}$; the induced electric field $E_{0 z}$; the spatial mean of the z -component of the vector potential $A_{0 z}$; and the invari-

![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-04.jpg?height=750&width=1036&top_left_y=1724&top_left_x=458)
Figure 1. Time histories from an $8^{3}$ magnetohydrodynamics simulation with initial values $\delta b / B_{0}=1, E=1.0$, $H_{c}=0.1$, and $H_{m}=0.4$. (a) Magnetic helicity of the fluctuations $H_{m}$ versus time, (b) mean induced electric field component in the $\hat{\mathbf{z}}$ direction (parallel to the applied magnetic field), (c) $\hat{\mathbf{z}}$ component of the mean vector potential $\mathbf{A}_{0}$, and (d) the invariant $\hat{H_{m}}$.

![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-05.jpg?height=751&width=1015&top_left_y=201&top_left_x=503)
Figure 2. Time histories of (a) $H_{m}$, (b) $E_{0 z}$, (c) $A_{0 z}$, and (d) $\hat{H_{m}}$ from a $32^{3}$ magnetohydrodynamics simulation with initial magnetic helicity $H_{m}=0.2$

![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-05.jpg?height=613&width=822&top_left_y=1101&top_left_x=160)
Figure 3. Time histories of $H_{m}$, showing relative effects of $B_{0}$ and resistive decay. (curve $A$ ) run with $B_{0}=1$ and $\nu=\eta=0.01$, (curve B) run with $B_{0}=0.0$ and $\nu=\eta=0.01$, and (curve C ) run with $B_{0}=1$ and $\nu=\eta=0.0$.

ant helicity $\hat{H}_{m}$. Here we clearly see the rapid decrease of $H_{m}$, Figure 2a, along with the pulse of induced electric field, Figure 2b, that is responsible for the decay. Once again, $A_{0 z}$ builds up to a near-constant value, but in this run the entire process is essentially completed by about $t=8$. We suspect that the more rapid decay of $H_{m}$ in this $32^{3}$ run, relative to the $8^{3}$ run shown in Figure 1, is due to the availability of larger wavenumbers that participate in the dynamics. Subsequently, the evolution (not shown) is described by oscillations of $H_{m}$ and $E_{0 z}$ about zero, and oscillations of $A_{0 z}$ about a nonzero value. Throughout the run, $\hat{H}_{m}$ is conserved to high precision, as is demonstrated for the early part of the run in Figure 2d.

This nonlinear decay process is also seen in dissipative runs. In Figure 3 we compare time histories of $H_{m}$
from three runs: (curve A$)$ a run with $B_{0}=1$ and $\nu=\eta=0.01$, (curve B) a run with $B_{0}=0.0$ and $\nu=\eta=0.01$, and (curve C) a run with $B_{0}=1$ and $\nu=\eta=0.0$. Apart from these differences, runs A, B, and C are identical at $t=0$. Another run (not shown) with $B_{0}=0.0$ and $\nu=\eta=0.0$ conserves $H_{m}$ to high precision, in view of the rugged conservation law applicable in that case [Stribling and Matthaeus, 1990]. Figure 3 shows, for run B , that $H_{m}$ decays, although not at a rapid pace. In such cases, one expects "selective decay" [Montgomery et al., 1978; Matthaeus and Montgomery, 1980; Riyopoulos et al., 1982] to be operative and the helicity to decay slowly with respect the decay of energy. The results for runs A and C are quite similar. The mean magnetic field is nonzero in these runs, and $H_{m}$ decays more rapidly than in run B , for which $B_{0}=0$. Run A has the same values of dissipation coefficients as run B , but $H_{m}$ decays much more rapidly nonetheless. In fact, the presence of nonzero dissipation in run A only slightly increases the rate of decay of $H_{m}$ relative to run C , which is identical but without dissipation. This again strongly suggests that the decay of magnetic helicity is mainly a consequence of $B_{0} \neq 0$ and has little to do with linear resistive dissipation.

This latter point can be made more clear by examining run A a bit further. In Figure 4 we show separately the contributions to the time rate of change of $H_{m}$ due to resistivity and due to the mean induced electric field. It is seen clearly that a large "pulse" of electric field early in the run is responsible for the largest and most rapid decreases in the value of $H_{m}$.

While we have performed a variety of other simulations to investigate this process, our perspective has remained consistent with the brief overview given above. In the presence of an order $1\left(\delta b / B_{0} \approx 1\right)$ mean magnetic field, an initial value of magnetic helicity tends to decrease toward zero on the timescale of several to several tens of Alfvén times. This decrease is mediated by a

![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-06.jpg?height=606&width=836&top_left_y=218&top_left_x=160)
Figure 4. Contributions to the time derivative of $H_{m}$ due to resistive decay (dotted line) and the nonlinear decay term (solid line) from a simulation with $B_{0}=1$ and $\nu=\eta=0.01$ (run A in Figure 3).

well-defined "pulse" of mean magnetic-field-aligned induced electric field that is produced dynamically. This characterization provides a clear answer to the question posed earlier concerning the preferred apportionment of the contributions to $\hat{H}_{m}=H_{m}+2 \mathbf{A}_{0} \cdot \mathbf{B}_{0}$ : periodic 3D turbulence with a mean magnetic field $B_{0}$ proceeds, through nonlinear interactions, to eliminate an initial value of magnetic helicity $H_{m}$ in favor of an enhanced value of $2 \mathbf{A}_{0} \cdot \mathbf{B}_{0}$. Moreover, at the Reynolds numbers we have used, resistive dissipation is a small effect compared to the nonlinear decay process.

## Phenomenology and the "Alpha Effect"

One can estimate the magnitude of the induced electric field that accompanies the nonlinear magnetic helicity decay process in a straightforward manner by assuming that a typical field-aligned electric field pulse of average magnitude $E_{0 z}$ persists for a duration $\tau_{E}$, at which time the initial magnetic helicity has decayed to zero. Then, ignoring dissipation, using the conservation law, equation (2), and assuming that other components of mean electric field vanish, we estimate the characteristic value of $\mathbf{E}_{0}$ during the helicity decay, designated $\hat{\mathbf{E}}$, as

$$
\begin{equation*}
\hat{\mathbf{E}} \approx-\frac{H_{m}}{2 B_{0}^{2} \tau_{E}} \mathbf{B}_{0} \tag{5}
\end{equation*}
$$

which persists for the time $\tau_{E}$. This is reminiscent of the alpha effect [Parker, 1955; Krause and Radler, 1980; Moffatt, 1978], familiar in dynamo theory, in which a mean electric field due to turbulence is approximated as $\hat{\mathbf{E}}=-\alpha \mathbf{B}_{0}$. In the present case, $\alpha \approx H_{m} / 2 \tau_{E} B_{0}^{2}$, although here the effect is not a steady state phenomenon.

It is also straightforward to construct a simple but possibly useful phenomenology for the dynamics of the helicity decay process, making use of various arguments developed in closure theory by Pouquet et al. [1976]. First we define a normalized magnetic helic-
ity $\tilde{H}=k_{H} H_{m}$ in terms of a "helicity-containing" wavenumber $k_{H}$ and in terms of $E_{0 z}$, the component of mean induced electric field parallel to $\mathbf{B}_{0}$. Next, we denote by $\tau_{I I}$ the characteristic timescale for the evolution of $H_{m}$ under the influence of the mean induced electric field. In view of the oscillations seen in the simulations, we suspect that $\tau_{H}$ may be of the order of the timescale for Alfvénic oscillations at the helicitycontaining wavenumber, in which case we would have $\tau_{H}=\left(k_{H} B_{0}\right)^{-1}$. (Recall that $B_{0}$ has dimensions of Alfvén speed in these units.) From the conservation law, equation (2), and the above definitions, we write

$$
\begin{equation*}
\frac{d \tilde{H}}{d t}=\frac{2 E_{0 z}}{\tau_{H}} . \tag{6}
\end{equation*}
$$

To form a closed set of simple equations, we need a simple phenomenology for $E_{0 z}$. Because of the nature of the effects observed in the simulations, it appears that we require two terms in an approximate expression for $d E_{0 z} / d t$. First, we assume a simple direct decay of mean electric field in the form $d E_{0 z} / d t \sim-E_{0 z} / \tau_{E}$, where $\tau_{E}$ is the characteristic decay time. This timescale may be associated with decay due to both spectral transfer and effects that are local in wavenumber, in view of the fact that $E_{0 z}$ is not an ideally conserved global quantity. Consequently, we expect that $\tau_{E}$ may be shorter than or of the order of the spectral transfer time for the energy or the appropriate MHD eddy turnover time. In this simple treatment, we assume that the decay time for the electric field is identified with the "lifetime" of the electric field pulse in the decay runs. Second, we couple the mean electric field to the magnetic helicity by examining the dynamical equation for $\langle\mathbf{v} \times \mathbf{b}\rangle$, extracting a relevant term that is approximately $\mathbf{B}_{0}\langle(\nabla \times \mathbf{b}) \cdot \mathbf{b}\rangle=H_{j} \mathbf{B}_{0}$, where $H_{j}$ is the "current helicity" [Keinigs, 1983]. A reasonable definition of $k_{H}$, the helicity-containing wavenumber, is that it satisfies $\langle(\nabla \times \mathbf{b}) \cdot \mathbf{b}\rangle \approx k_{H}^{2} H_{m}$. This indicates we should include a contribution to the time rate of change of mean electric field of the form $d E_{0 z} / d t \approx-\tilde{H} / \tau_{H}$. Assembling the two contributions, we arrive at the expression

$$
\begin{equation*}
\frac{d E_{0 z}}{d t}=-\frac{\tilde{H}}{\tau_{H}}-\frac{E_{0 z}}{\tau_{E}}, \tag{7}
\end{equation*}
$$

which along with equation (6) forms a closed twoequation model for the behavior of the magnetic helicity and the mean electric field.

This two-equation model leads, in a steady state driven by a supply of magnetic helicity, to a value of mean induced electric field $\hat{\mathbf{E}}=-\tau_{E} k_{H}^{2} H_{m} \mathbf{B}_{0}$. This is equivalent to an "alpha coefficient" of $\alpha=\tau_{E} k_{H}^{2} H_{m}= \tau_{E} \tau_{H}^{-2}\left|\mathbf{B}_{0}\right|^{2} H_{m}$. The steady result differs from the nonsteady estimate given above, in the way the timescales enter. In addition, we also note that the $\alpha$ effect seen in the simulations or in the phenomenological model could be expressed equally well in terms of "current helicity" $H_{j}=\langle\mathbf{b} \cdot \nabla \times \mathbf{b}\rangle$. Keinigs [1983] has emphasized that in mean field electrodynamics, it is often most appropriate to express $\alpha$ in terms of $H_{j}$.

If we choose the timescales $\tau_{H}$ and $\tau_{E}$ to be constants independent of $H_{m}, \mathbf{E}_{0}$, and time, the pair of equations (6) and (7) are linear with constant coefficients. In the nonsteady decay situation with initial data $E_{0 z}=0$ and specified $\tilde{H}$, the solution is readily seen to be

$$
\begin{gathered}
E_{z}(t)=-\frac{2 \tilde{H}(0)}{\omega \tau_{H}^{2}} \sin \omega t e^{-t / 2 \tau_{E}} \\
\tilde{H}(t)=\tilde{H}(0)\left(\cos \omega t+\frac{\sin \omega t}{2 \omega t_{E}}\right) e^{-t / 2 \tau_{E}}
\end{gathered}
$$

where $\omega^{2}=2 / \tau_{H}^{2}-1 / 4 \tau_{E}^{2}$. This solution admits an initial "pulse" of electric field that dies off exponentially in time and a magnetic helicity that damps exponentially. For the "underdamped case" $\tau_{H}>\sqrt{8} \tau_{E}$, the solutions also display an oscillatory envelope, but for choices of parameters corresponding to overdamped $\left(\omega^{2}<0\right)$ and critically damped ( $\omega^{2}=0$ ) behavior, the exponentially damped pulses evolve without oscillations. This simplified picture is qualitatively in accord with the simulations, but we also have found that the solutions to equations (6) and (7) give reasonable quantitative approximations to at least some of our simulation results, especially at early times.

This correspondence is demonstrated first for nondissipative run C , discussed in section 2 and Figure 3. We investigated fits of the solutions to the model equations (6) and (7) to the time histories of $H_{m}$ and $E_{0 z}$ from the simulation as follows: First, we determined the time of maximum $\left|E_{0 z}\right|$ and used this to constrain the timescale parameters $\tau_{H}$ and $\tau_{E}$. The undetermined one of this pair was then selected to minimize the difference between the simulated and model values of the electric field pulse height. The results of this comparison are shown in Figure 5. The first plot shows $E_{0 z}$ vs. time for the simulation (solid line) and for the optimized model (dotted line). The parameters selected for the optimization are $\tau_{H}=\left(k_{H} B_{0}\right)^{-1}=0.4$ and $\tau_{E} \approx .15$, representing a value of $k_{H}=2.7$ for the helicity-containing wavenumber. In addition, these parameters correspond to the critically damped solution (or very close to it), so there are no late time oscillations in the fit. This value of $k_{H}$ is reasonably compatible with values of mean helicity-containing wavenumber computed from the simulation by evaluating the second ( $k^{2}$ ) moment of the magnetic helicity spectrum. The simulation valwes ranged from about 3.5 to 4.5 during the time of the electric field pulse, from $t=0$ to about 0.5 . It is also clear from Figure 5 that this is the time during which the fit to the model represents the simulation behavior reasonably well. Other fits, with different initial MHD parameters, were done to other simulations. The timescales $\tau_{H}$ and $\tau_{E}$ are seen to vary according to global and spectral properties of the initial turbulence in a way that is sufficiently complex that we have not been able to unravel it based on the simulations we have analyzed so far. However, we have seen in one other fit (for a case with high cross helicity) that the optimal model fit is overdamped and not critically damped, as was the result shown in Figure 5.

![](https://cdn.mathpix.com/cropped/2025_11_22_a06d7d0506c69ada59cbg-07.jpg?height=1228&width=856&top_left_y=187&top_left_x=1020)
Figure 5. Fit of the solutions of equations (6) and (7) to the idcal simulation run C of Figure 3. (top) The time histories of $E_{0 z}$ are compared for the model (dotted line) and simulation (solid line); (bottom) a similar comparison of the time history of $H_{m}$ is given.

This simple phenomenological model may help provide some insight into the simulation results. It remains to provide a better definition for several of the estimated quantities, especially timescales such as the electric field spectral transfer time $\tau_{E}$. Nevertheless, we can see clearly that the nonlinear decay process we have described predicts a dynamical relationship between mean induced electric field and the nonmirror symmetric features of the turbulent fields, as measured by $H_{m}$ or $H_{j}$. One can see easily that this turbulent and possibly nonsteady "alpha effect" bears a strong resemblance to the well known theoretical results [Parker, 1955; Krause and Radler, 1980; Moffatt, 1978] in mean field electrodynamic treatments of the dynamo. However, here we have had to make no assumptions such as low Reynolds number (our treatment is, if anything, for high Reynolds number), and the "alpha" we obtain appears to be independent of viscosity and resistivity. In fact, the picture we have described of decay of $H_{m}$ and an associated pulse of $\mathbf{E}_{0}$ can be extracted readily from mean field electrodynamics models [e.g., Zeldovich et al., 1983, pp. 182-187]. However, such a conclusion requires the present dynamical verification, since the
mean field models have already assumed an alpha effect relationship $\mathbf{E}_{0}=-\alpha \mathbf{B}_{0}$ with the usual mean field expressions for $\alpha$ in terms of isotropic helicities.

## Discussion and Conclusions

In a periodic system with an externally applied field, we find that the magnetic helicity $H_{m}$ associated with the fluctuations behaves quite differently than in the well-studied case in which there is no mean magnetic field. The latter case, for which $H_{m}$ is nondissipatively conserved, leads to a helicity that is transferred to long wavelength fluctuations [Frisch et al., 1975], where it can survive in the selective decay scenario [Montgomery] et al., 1978; Matthaeus and Montgomery, 1980] for long times in the presence of dissipation. In the presence of mean applied magnetic field, on the other hand, we have identified a nonlinear decay process that causes $H_{m}$ to depart from its initial value rapidly, reaching oscillatory values near zero in a time period comparable to a few characteristic times of the turbulence, when the applied field is reasonably strong (i.e., $\delta b / B_{0} \approx 1$ ). The decay can be readily understood in terms of the conservation law for $\hat{H}_{m}=H_{m}+2 \mathbf{B}_{0} \cdot \mathbf{A}_{0}$, which replaces $H_{m}$ conservation when there is an applied field. Helicity decay is therefore accompanied by a "pulse" of mean induced electric field that mediates the transition to near-zero helicity in the fluctuations.

The timescales for this process are, as yet, incompletely documented. The duration of the electric field pulse $\tau_{E}$, also a measure of the $H_{m}$ decay timescale, is almost certain to depend upon the strength of the applied field and upon other parameters, such as cross helicity, that regulate MHD turbulence transfer rates. Other preliminary simulation studies (not shown here) bear out this anticipated complexity. Although we can construct a simple two-equation phenomenology that qualitatively reproduces the helicity decay process, this model remains to be tested and refined by comparison with more complete simulation studies. A similar phenomenology can be extracted from the mean field electrodynamics equations using suitable approximations, as can be seen in the work by Zeldovich et al. [1983, pp. 182-187].

The $H_{m}$ decay process, as described here, appears to be equivalent to a nonsteady turbulent alpha effect, independent of Reynolds number. Moreover, in the simulations there is no enforcement of isotropy, and indeed, one can show [Oughton, 1993] that for strictly isotropic turbulence $\mathbf{E}_{0}=-\langle\mathbf{v} \times \mathbf{b}\rangle \equiv 0$, independent of the existence of mirror-asymmetric properties such as various helicities. While this technical deficiency afflicts standard mean field theories and appears not to have been noticed previously, the present simulation results indicate that the basic conclusions of alpha effect theory nevertheless survive the transition to anisotropic turbulence. Although here we have seen a connection of this type only between the mean electric field and the magnetic or current helicity, it seems quite plausible that a more complete theory might also involve helicities of
the velocity field, as do similar results in mean field electrodynamics. For example, closure theories [Pouquet et al., 1976] indicate that there should exist couplings that tend to bring the kinetic and magnetic helicities into near equipartition in a timescale very nearly like the Alfvénic timescale for the helicity-containing structures $\tau_{H}$ that we used above. As a final observation in this regard, we recall that our estimate of $\alpha$ obtained from the steady version of equation (7) is $\alpha=\tau_{E} k_{H}^{2} H_{m}$. Under the above assumption of temporal equipartition of magnetic and velocity helicities, we would then approximate $k_{H}^{2} H_{m} \approx\langle\mathbf{v} \cdot \nabla \times \mathbf{v}\rangle$. Moreover, from our first simulation, which represented a critically damped solution to the model equations, we found that $\tau_{H} \approx \sqrt{8} \tau_{E}$, from which our estimate becomes $\alpha \approx\langle\mathbf{v} \cdot \nabla \times \mathbf{v}\rangle \tau_{H} / \sqrt{8}$. This compares remarkably well in magnitude with the mean field electrodynamics estimate for alpha in the high conductivity limit obtained by Krause and Radler [1980], $\alpha=-\langle\mathbf{v} \cdot \nabla \times \mathbf{v}\rangle \tau_{c} / 3$, where $\tau_{c}$ is the correlation time of the velocity helicity. The fact that the sign of $\alpha$ is opposite in our case relative to the classic results appears to be connected with the fact that our initial value problem with specified $H_{m}$ corresponds more closely to the steady case that is driven by magnetic forces rather than by forcing of the momentum equation. (See for example the comparison of the two cases given by Matthaeus et al. [1986].) In fact, from the time derivative of equation (2) and the alpha effect approximation, one can see immediately that $\partial H_{m} / \partial t \approx-2 \alpha B_{0}^{2}$, so that $\alpha \propto+H_{m}$ leads to magnetic helicity decay, as we have seen in the present problem. The above-cited result of Zeldovich et al. [1983] apparently also corresponds to magnetic helicity decay and, along with our result, differs in the sign of $\alpha$ relative to the results of [Keinigs, 1983], who made the assumption of a driven momentum equation. In contrast, for $\alpha \propto-H_{m}$, a case having greater similarity to the classical $\alpha$ effect results, one would expect to see growth of the magnetic helicity of the fluctuations.

Use of direct numerical simulation has proved to be a useful approach in uncovering basic MHD processes that underlie dynamo mechanisms and MHD turbulence phenomena. Further simulations will also be useful in establishing the validity of better phenomenological models of these complex MHD turbulence processes. In addition, we suggest that magnetic helicity decay processes might have observable consequences for magnetic helicity spectra [Matthaeus and Goldstein, 1982], magnetic helicity distributions [Bieber et al., 1987b; Goldstein et al., 1991], and induced electric field [Marsch and Tu, 1992] observations in the interplanetary medium and the scattering of cosmic rays [Bieber et al., 1987a], although the complexities of these possibilities mandate that they be deferred until a later time.

## Appendix

Although the simulation results in this paper are cast entirely in the context of periodic geometry, we have made various allusions to the application of these ideas
to cases in which local homogeneous (or periodic) turbulence exists in a medium that admits nontrivial structure at much larger scales. This is also the picture adopted in mean field electrodynamics [e.g., Krause and Radler, 1980; Moffatt, 1978; Zeldovich et al., 1983]. The usual perspective is that a separation of lengthscales (and possibly timescales) is required for these models. For the periodic case, however, one might be particularly concerned that a volume-averaged electric field $\mathbf{E}_{0}$ is generated, which might either violate the assumptions of MHD (i.e., neglect of the displacement current) or otherwise be inconsistent with the periodic boundary conditions. These concerns can be alleviated by a multiple scales expansion.

Faraday's law and Ampere's law can be cast in dimensionless units by adopting dimensional scales $B^{\prime}, V^{\prime}, L^{\prime}$, and $T^{\prime}$ for the magnetic field, velocity field, length, and time, respectively. The electric current density is measured in units $J^{\prime}=c B^{\prime} / 4 \pi L^{\prime}$ where $c$ is the light speed, while the electric field is cast in units of $E^{\prime}=V^{\prime} B^{\prime} / c$. The type of unit for the electric field is determined by choice of the unit of speed: $V^{\prime}=c$ represents radiation units, while $V^{\prime}=V_{a}=B^{\prime} / \sqrt{4 \pi \rho}$, the Alfvén speed, is appropriate for MHD. (The typical mass density is ρ.) It is natural also to select lengths and times so that $L^{\prime} / T^{\prime}=V^{\prime}$. For the MHD case this amounts to a timescale which is the "Alfvén transit time of unit distance." For the choice of MHD units it is now simple to verify that the relevant pair of Maxwell equations becomes, in dimensionless form,

$$
\begin{align*}
\nabla \times \mathbf{B} & =\mathbf{J}+\epsilon^{2} \frac{\partial \mathbf{E}}{\partial t}  \tag{A1}\\
\frac{\partial \mathbf{B}}{\partial t} & =-\nabla \times \mathbf{E} \tag{A2}
\end{align*}
$$

where $\mathbf{J}$ is the electric current density and $\epsilon \equiv V_{a} / c$ is typically a small parameter. For MHD to be a legitimate model, we will need to see that $\nabla \times \mathbf{B}=\mathbf{J}$ emerges in a consistent way at the relevant orders of expansion. This will allow us to employ Ohm's law, which will determine the space and time dependence of the electric field. Use of Ohm's law requires a separate justification, one that may influence some higher-order terms in the expansion below. For the present we assume that $\mathbf{E}=-\mathbf{v} \times \mathbf{B}+\mu \mathbf{J}$, where $\mathbf{v}$ is the plasma fluid velocity and $\mu$ is the resistivity.

Relying on the smallness of $\epsilon$, we introduce two physically motivated coordinate scales for space and for time. The order 1 or "fast" scales will be $\mathbf{x}_{f}=\mathbf{x}$ and $t_{f}=t$, where $\mathbf{x}$ and $t$ are the dimensionless position and time, respectively, in the units selected above. The slowly varying length and time coordinates are $\mathbf{x}_{s}=\epsilon \mathbf{x}$ and $\boldsymbol{t}_{s}=\epsilon t$. Derivatives are expanded according to $\partial / \partial t=\partial / \partial t_{f}+\epsilon \partial / \partial t_{s}$ and $\nabla=\nabla_{f}+\epsilon \nabla_{s}$. All of the relevant variables are taken to be functions of fast and slow coordinates and are expanded in powers of $\epsilon$. For example, $\mathbf{B}=\mathbf{B}^{(0)}+\epsilon \mathbf{B}^{(1)}+\epsilon^{2} \mathbf{B}^{(2)}+\ldots$. To help separate fast and slow properties, a spatial averaging operator < > is introduced, having the properties that
$\left\langle F\left(\mathbf{x}_{f}, \mathbf{x}_{s}, t_{f}, t_{s}\right)\right\rangle=G\left(\mathbf{x}_{s}, t_{f}, t_{s}\right)$ and $\left\langle\nabla_{f} F\right\rangle \equiv 0$, where $F$ is any of the functions of fast and slow coordinates and $G$ depends only upon slow spatial coordinates.

The multiple-scale expansion is carried out by inserting these definitions into equations (A1) and (A2). At leading order $\left(O\left(\epsilon^{0}\right)\right)$ we find from equation (A1), that

$$
\begin{equation*}
\nabla_{f} \times \mathbf{B}^{(0)}=\mathbf{J}^{(0)} \tag{A3}
\end{equation*}
$$

and, according to the averaging procedure, that $\left\langle\mathbf{J}^{(0)}\right\rangle=$ 0 , since $\left\langle\nabla_{f} \times \mathbf{B}^{(0)}\right\rangle=0$. Moreover, from equation (A2) at leading order, $\partial \mathbf{B}^{(0)} / \partial t_{f}=-\nabla_{f} \times \mathbf{E}^{(0)}$, so that $\partial\left\langle\mathbf{B}^{(0)}\right\rangle / \partial t_{f}=0$. Using Ohm's law, we see now that the leading order fields obey equation (A3) and

$$
\begin{equation*}
\frac{\partial \mathbf{B}^{(0)}}{\partial t_{f}}=\nabla_{f} \times\left(\mathbf{v}^{(0)} \times \mathbf{B}^{(0)}\right)+\mu \nabla_{f}^{2} \mathbf{B}^{(0)} \tag{A4}
\end{equation*}
$$

along with the constraint that

$$
\begin{equation*}
\left\langle\mathbf{J}^{(0)}\right\rangle=0 . \tag{A5}
\end{equation*}
$$

In addition, the requirement that the magnetic field be solenoidal leads to the conditions that $\nabla_{f} \cdot \mathbf{B}^{(0)}=0$ and $\nabla_{s} \cdot\left\langle\mathbf{B}^{(0)}\right\rangle=0$, from which we can write the leadingorder magnetic field as

$$
\begin{equation*}
\mathbf{B}^{(0)}=\left\langle\mathbf{B}^{(0)}\right\rangle+\mathbf{b}^{(0)}=\nabla_{s} \times\left\langle\mathbf{A}^{(-1)}\right\rangle+\nabla_{f} \times \mathbf{A}^{(0)} \tag{A6}
\end{equation*}
$$

where we have introduced a suitable leading-order expansion of the magnetic vector potential. The leadingorder magnetic fluctuations $\mathbf{b}^{(0)}$ are determined solely by $\mathbf{a}^{(0)}=\mathbf{A}^{(0)}-\left\langle\mathbf{A}^{(0)}\right\rangle$. Both $\mathbf{b}^{(0)}$ and $\mathbf{B}^{(0)}$ are insensitive to the volume average vector potential $\left\langle\mathbf{A}^{(0)}\right\rangle$. Note that in order to represent the large-scale magnetic field $\mathbf{B}^{(0)}$, the vector potential expansion must admit a "misordered" or "singular" component at order $\epsilon^{-1}$. However, $\mathbf{A}^{(-1)}$ can be chosen to have no fast space dependence without loss of generality.

The second-order equations also provide some useful information. For example, we find that the spaceaveraged leading-order magnetic field obeys

$$
\begin{equation*}
\frac{\partial\left\langle\mathbf{B}^{(0)}\right\rangle}{\partial t_{s}}=\nabla_{s} \times\left\langle\mathbf{v}^{(0)} \times \mathbf{B}^{(1)}+\mathbf{v}^{(1)} \times \mathbf{B}^{(0)}\right\rangle+\mu \nabla_{s}^{2}\left\langle\mathbf{B}^{(0)}\right\rangle \tag{A7}
\end{equation*}
$$

with

$$
\begin{equation*}
\nabla_{s} \times\left\langle\mathbf{B}^{(0)}\right\rangle=\left\langle\mathbf{J}^{(1)}\right\rangle \tag{A8}
\end{equation*}
$$

provided that Ohm's law holds to this order. The divergence condition on the magnetic field implies that

$$
\begin{equation*}
\left\langle\mathbf{B}^{(1)}\right\rangle=\nabla_{s} \times\left\langle\mathbf{A}^{(0)}\right\rangle . \tag{A9}
\end{equation*}
$$

Higher-order terms will involve new effects, such as $\partial \mathbf{E}^{(0)} / \partial t_{f}$ which appears at $O\left(\epsilon^{2}\right)$. In addition, solvability conditions are expected to emerge, providing constraints among various higher-order terms that are needed for a convergent expansion. These are not addressed here.

By comparison with the notation used in the main body of the paper for the periodic case, it is clear that various terms in the leading-order expansion can be identified with the variables in the periodic problem. For example, to the accuracy of the leading order, we can identify the mean magnetic field $\mathbf{B}^{(0)} \rightarrow \mathbf{B}_{0}$, the fluctuating magnetic field $\mathbf{b}^{(0)} \rightarrow \mathbf{b}$, the electric current density $\mathbf{J}^{(0)} \rightarrow \nabla \times \mathbf{b}$, the leading order vector potential that generates local magnetic fluctuations $\mathbf{a}^{(0)} \rightarrow \mathbf{a}$, and the time-varying volume-averaged vector potential $\left\langle\mathbf{A}^{(0)}\right\rangle \rightarrow \mathbf{A}_{0}$. In both the expansion and the periodic problem, these fields obey the MHD equations. The periodic case violates none of the conditions found here, and in fact, periodic boundary conditions automatically satisfy the constraint in equation (A5) that is needed for the perturbation expansion to exist.

Naturally, the periodic problem addresses only the "fast" or local behavior, and the dynamics of the largescale magnetic field are relegated to equations not solved in the model turbulence problem we have addressed. Locally, the large-scale magnetic field appears as a specified uniform constant. Slowly varying behavior of the locally averaged magnetic field, as seen in equation (A8), would also follow ordinary MHD equations, if we were examining the problem at those scales. The buildup of local average vector potential, associated with the decay of magnetic helicity, is found in equation (A9) to produce higher-order changes to the large-scale magnetic field. The only physical variable that is not locally represented in the periodic problem is the vector potential associated with the local averaged field $\mathbf{B}_{0}$. However, we used a vector potential representation only for the fluctuating magnetic field. The perturbation expansion shows clearly how the periodic problem can be used to investigate leading-order local behavior of a scale-separated (weakly inhomogeneous) MHD system. In fact, from the correspondence of equation (A4) to the periodic variables, we find for the ideal case that

$$
\begin{equation*}
\frac{\partial \mathbf{b}}{\partial t}=\nabla \times(\mathbf{v} \times \mathbf{B}), \tag{A10}
\end{equation*}
$$

which is equivalent to equation (4). Uncurling, we find

$$
\begin{equation*}
\frac{\partial \mathbf{a}}{\partial t}=\mathbf{v} \times \mathbf{B}+\nabla \Psi \tag{A11}
\end{equation*}
$$

where $\Psi$ is a periodic gauge function. We can now compute the time derivative of the fluctuating magnetic helicity $\langle\mathbf{a} \cdot \mathbf{b}\rangle$ as

$$
\begin{equation*}
\frac{d H_{m}}{d t}=\langle\mathbf{a} \cdot \nabla \times \mathbf{v} \times \mathbf{B}\rangle+\langle\mathbf{b} \cdot \mathbf{v} \times \mathbf{B}\rangle+\langle\mathbf{b} \cdot \nabla \Psi\rangle \tag{A12}
\end{equation*}
$$

which, upon use of $\mathbf{B}=\mathbf{B}_{0}+\mathbf{b}$, the periodic boundary conditions, and the cyclic property of the triple scalar product, becomes

$$
\begin{equation*}
\frac{d H_{m}}{d t}=-2 \mathbf{B}_{0} \cdot\langle\mathbf{v} \times \mathbf{b}\rangle \tag{A13}
\end{equation*}
$$

If we now volume average equation (A11) and note that the average value of the gradient is zero for a periodic
function, we see that equation (A13) is equivalent to the statement that $H_{m}+2 \mathbf{B}_{0} \cdot\langle\mathbf{a}\rangle=$ constant, that is, that the expression in equation (2) of the main text is an ideal invariant in periodic geometry.

Acknowledgments. We would like to thank D. Montgomery, D. A. Roberts, M. L. Goldstein, and G. Zank for helpful discussions and the NASA Center for Computational Sciences for computer time. We are grateful to a referee for pointing out the Zeldovich et al. [1983] reference and to D. Montgomery for raising some of the issues addressed in the appendix. T. S. is supported by the National Academy of Sciences through the NRC associateship program at Goddard Space Flight Center. This research has been supported in part by NASA grant NAG5-1573 and NSF grant ATM8913627 at Bartol and Solar Terrestrial Theory Program grants at Goddard Space Flight Center and at Bartol.

The Editor thanks E. Marsch and another referee for their assistance in evaluating this paper.

## References

Bieber, J. W., P. Evenson, and W. H. Matthaeus, Magnetic helicity of the IMF and the solar modulation of cosmic rays, Geophysical Res. Lett., 14, 864, 1987a.
Bieber, J. W., P. Evenson, and W. H. Matthaeus, Magnetic helicity of the Parker field, Astrophys. J., 315, 700, 1987b.
Dahlburg, J., D. Montgomery, G. Doolen, and L. Turner, Turbulent relaxation of a confined magnetofluid to a force-free state, J. Plasma Phys., 37, 299, 1987a.
Dahlburg, J., D. Montgomery, G. Doolen, and L. Turner, Driven steady state RFP computations, $J$. Plasma Phys., 40, 39, 1987b.
Frisch, U., A. Pouquet, J. Léorat, and A. Mazure, Possibility of an inverse cascade of magnetic helicity in magnetohydrodynamic turbulence, J. Fluid Mech., 68, 769, 1975.
Fyfe, D., and D. Montgomery, High beta turbulence in two dimensional magnetohydrodynamics, J. Plasma Phys., 16, 181, 1976.
Goldstein, M. L., D. A. Roberts, and C. A. Fitch, The structure of helical interplanetary magnetic fields, Geophys. Res. Lett., 18, 1505, 1991.
Keinigs, R. K., A new interpretation of the alpha effect, Phys. Fluids, 26, 2558, 1983.
Krause, F., and K.-H. Radler, Mean Field Electrodynamics and Dynamo Theory, Pergamon, New York, 1980.

Marsch, E., and C. Y. Tu, Electric field fluctuations and possible dynamo effects in the solar wind, Solar Wind Seven, edited by E. Marsch and R. Schwenn, pp. 505-509, Pergammon, New York, 1992.
Matthaeus, W. H., and M. L. Goldstein, Measurement of the rugged invariants of magnetohydrodynamic turbulence in the solar wind, J. Geophys. Res., 87, 6011, 1982.
Matthaeus, W. H., and D. Montgomery, Selective decay hypotheses at high mechanical and magnetic reynolds number, Ann. N. Y. Acad. of Sci., 357, 203, 1980.

Matthaeus, W. H., M. L. Goldstein, and S. Lantz, The alpha dynamo parameter and measureability of helicities in magnetohydrodynamic turbulence, Phys. Fluids, 29, 5, 1986.
Meneguzzi, M., U. Frisch, and A. Pouquet, Helical and nonhelical turbulent dynamos, Phys. Rev. Lett., 47, 1069, 1981.
Moffatt, H. K., Magnetic Field Generation in Electrically Conducting Fluids, Cambridge University Press, New York, 1978.
Moffatt, H. K., and A. Tsinober, Helicity in laminar and turbulent flow, Annu. Rev. Fluid Mech., 24, 281, 1992.

Montgomery, D., L. Turner, and G. Vahala, Most probable states in magnetohydrodynamics, Phys. Fluids, 21, 757, 1978.
Orszag, S. A., Numerical simulations of incompressible flows within simple boundaries: I. galerkin (spectral) representations, Stud. Appl. Math., 50, 293, 1971.
Oughton, S., Transport of Solar Wind Fluctuations: A Turbulence Approach, Ph. D. Thesis, University of Delaware, 1993.
Parker, E. N., The formation of sunspots from the solar toroidal field, Astrophys. J., 121, 491, 1955.
Pouquet, A., and G. S. Patterson, Numerical simulation of helical magnetohydrodynamic turbulence, J. Fluid Mech., 85, 305, 1978.
Riyopoulos, S., A. Bondeson, and D. Montgomery, Re-
laxation toward states of minimum energy in a compact torus, Phys. Fluids, 25, 107, 1982.
Pouquet, A., U. Frisch and J. Léorat, Strong MHD helical turbulence and the nonlinear dynamo effect, $J$. Fluid Mech,, 77, 321, 1976.
Stribling, T., and W. H. Matthaeus, Statistical properties of ideal three-dimensional magnetohydrodynamics, Phys. Fluids B, 2, 1979, 1990.
Stribling, T., and W. H. Matthaeus, Relaxation processes in a low-order three-dimensional magnetohydrodynamics model, Phys. Fluids B, 8, 1848, 1991.
Taylor, J. B., Relaxation of toroidal plasma and generation of reverse magnetic fields, Phys. Rev. Lett., 33, 1139, 1974.
Zeldovich, Y. B., A. A. Ruzmaikin, and D. D. Sokoloff, Magnetic Fields in Astrophysics, Gordon and Breach, New York 1983.
S. Ghosh and T. Stribling, NASA Goddard Space Flight Center, Code 692, Greenbelt Road, Greenbelt, MD 20771 (email: xlsxg@cascade.gsfc.nasa.gov; troy.stribling@gsfc.nasa. gov).
W. H. Matthaeus, Bartol Research Institute, University of Delaware, Newark, DE 19716 (e-mail: yswhm@bripv1. bartol.udel.edu).
(Received June 24, 1993; revised August 19, 1993; accepted October 12, 1993.)


[^0]:    Copyright 1994 by the American Geophysical Union.

