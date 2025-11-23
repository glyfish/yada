See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/253704745

## The Evolution of Magnetic Helicity in Compressible Magnetohydrodynamics with a Mean Magnetic Field

Article in Geophysical Monograph Series • January 1995
DOI: 10.1029/GM086p0001

CITATIONS
4

4 authors, including:
![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-1.jpg?height=78&width=78&top_left_y=832&top_left_x=136)

Troy Stribling
University of Delaware
14 PUBLICATIONS 989 CITATIONS
SEE PROFILE
![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-1.jpg?height=72&width=76&top_left_y=1055&top_left_x=136)
W. H. Matthaeus

University of Delaware
919 PUBLICATIONS 45,985 CITATIONS

SEE PROFILE

READS
70
![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-1.jpg?height=84&width=84&top_left_y=832&top_left_x=1026)

Melvyn Goldstein
University of Maryland, Baltimore County
538 PUBLICATIONS 23,707 CITATIONS
SEE PROFILE

# The Evolution of Magnetic Helicity in Compressible Magnetohydrodynamics with a Mean Magnetic Field 

Sanjoy Ghosh<br>Applied Research Corporation, Landover, Maryland<br>W. Troy Stribling<br>National Research Council, NASA, Goddard Space Flight Center, Greenbelt, Maryland<br>Melvyn L. Goldstein<br>Laboratory for Extraterrestrial Physics, NASA, Goddard Space Flight Center, Greenbelt, Maryland<br>William H. Matthaeus<br>Bartol Research Institute, University of Delaware, Newark, Delaware


#### Abstract

The solar wind is often modeled as an incompressible magnetofluid. Such a description has been substantiated for two-dimensional (2-D) geometries through compressible magnetohydrodynamic (MHD) simulations which show that many features of incompressible 2-D MHD turbulent relaxation are preserved at subsonic, but non-negligible Mach numbers. However, analogous studies do not exist for three-dimensional (3-D) dynamics, and in particular, it is not known whether significant changes occur in the evolution of the magnetic helicity in going from the purely incompressible model to a low Mach number compressible model. Here we use a two and half dimensional (velocity and magnetic components in all three spatial directions, but functions of only two spatial variables) compressible MHD code to investigate the evolution of magnetic helicity in the presence of a mean magnetic field. The system is closed by assuming a polytropic equation of state. We consider the global and spectral features of magnetic helicity evolution, and discuss our results relative to incompressible 3-D decay simulations as well as to observations.


## 1. INTRODUCTION

Many features of the solar wind appear to be those of a turbulent magnetohydrodynamic (MHD) medium. This has prompted space physicists to study MHD turbulence using numerical simulations in an effort to better understand the inherent physics. Influenced largely by the limitations of computational resources as well as a reflection of increasing theoretical understanding,

[^0]MHD turbulence simulations have ranged from incompressible to ideal gas models, two-dimensions (2-D) to three-dimensions (3-D) models, and homogeneous to models containing an ambient magnetic field. Surprisingly, many solar wind features seem to be explainable using one of the simplest MHD models: the incompressible homogeneous 2-D system. The reasons why this is true is a matter of ongoing research [Zank and Matthaeus, 1992] .

An important aspect of MHD turbulent relaxation is the preferential decay of certain ideal invariants. For incompressible homogeneous 3-D geometries, these global invariants of the ideal (dissipation-free) system include the total energy $(E)$, the cross helicity $\left(H_{c}\right)$, and the
magnetic helicity $\left(H_{m}\right) . H_{c}$ is also an invariant of the 2-D system and has been shown through numerous 2D simulations to have a dynamical behavior that may explain certain highly Alfvénic states in the solar wind. The purely 3-D quantity, $H_{m}=\frac{1}{2}\langle\mathbf{A} \cdot \mathbf{B}\rangle$, where the brackets denote a spatial average, is a correlation measure between the vector potential and the fluctuating magnetic field. When an ambient magnetic field is present a new invariant,

$$
\begin{equation*}
\hat{H}_{m}=H_{m}+\mathbf{A}_{0} \cdot \mathbf{B}_{0} \tag{1}
\end{equation*}
$$

emerges in place of $H_{m}$ [Matthaeus and Goldstein, 1982]. $\hat{H}_{m}$ is a less well studied quantity. In fact, the work of Stribling and Matthaeus [1992] is perhaps the only study of its turbulence characteristics to date.

In this paper we compare the dynamics of $H_{m}$ and $\hat{H}_{m}$ as obtained by Stribling and Matthaeus [1992] for an incompressible 3-D system to those of a compressible system. In addition, we discuss the wavenumber distribution of normalized magnetic helicity from our simulations relative to observations. We employ a restricted 3-D formulation, the so-called two and half dimensional ( $2 \frac{1}{2}$-D) model. Here all spatial vectors have three components, but each component is a function of only two spatial directions, $(x, y)$. This model greatly reduces computational times over a full 3-D compressible model while preserving nonlinear couplings in the parallel direction and at least one perpendicular direction relative to the ambient magnetic field. Compressibility is incorporated in the form of a polytropic equation of state.

Our strategy is to introduce a random initial spectrum of fixed magnetic helicity and study the evolution of $H_{m}$ during the ensuing turbulent dynamics under a variety of conditions which include the presence of dissipation or lack thereof and the presence or absence of an ambient magnetic field. Our goals are two-fold. First, we seek to determine whether weak compressibility (low sonic Mach number) causes significant changes in magnetic helicity dynamics over the incompressible 3-D system. Second, we want to know how well $H_{m}$ measurements in the solar wind can be characterized by the behavior of $H_{m}$ in our polytropic $2 \frac{1}{2}$-D MHD model.

## 2. NUMERICAL METHOD AND INITIAL CONDITIONS

Our simulations are based on a standard dimensionless representation of the compressible MHD system [Ghosh and Matthaeus, 1990]. The polytropic $2 \frac{1}{2}$-D

MHD system of continuity, momentum, and magnetic induction equations is as follows.

$$
\begin{gather*}
\frac{\partial}{\partial t} \rho=-\nabla \cdot(\rho \mathbf{u}), \\
\frac{\partial}{\partial t} \mathbf{u}=\mathbf{u} \times \tilde{\omega}-\frac{1}{2} \nabla\left[\mathbf{u} \cdot \mathbf{u}+\frac{2}{M_{s 0}^{2}(\gamma-1)} \rho^{\gamma-1}\right]+\frac{\mathbf{J} \times \mathbf{B}}{M_{a 0}^{2} \rho} \\
+\frac{1}{\rho} \nu_{c} \nabla^{2} \mathbf{u}+\frac{1}{\rho}\left(\zeta_{c}+\frac{1}{3} \nu_{c}\right) \nabla(\nabla \cdot \mathbf{u}),  \tag{2b}\\
\frac{\partial}{\partial t} \mathbf{A}=\mathbf{u} \times \mathbf{B}+\mu_{c} \mathbf{J}+\nabla F .
\end{gather*}
$$

Here the vorticity, $\tilde{\omega}$, is derived from the velocity field by $\tilde{\omega}=\nabla \times \mathbf{u}$. The magnetic field, $\mathbf{B}$, is related to the current, $\mathbf{J}$, and the vector potential, $\mathbf{A}$, through $\mathbf{J}=\nabla \times \mathbf{B}$ and $\nabla \times \mathbf{A}=\mathbf{B}$, respectively. The system of equations is closed assuming a polytropic relation between pressure and density, $P=\rho^{\gamma}$, where we have chosen $\gamma=5 / 3$. The function $F$ in (2c) is chosen to preserve the Coulomb gauge condition, $\nabla \cdot \mathbf{A}=0$.

Constants present in (2) include a characteristic sonic Mach number, $M_{30}$, and a characteristic Alfvénic Mach number, $M_{a 0}$. The last two terms in (2b) represent a standard model of viscous dissipation, involving viscosity coefficients $\zeta_{c}$ and $\nu_{c}$. The dimensionless dynamic viscosity, $\nu_{c}$, and resistivity, $\mu_{c}$, are related to the mechanical ( $R$ ) and magnetic ( $R_{m}$ ) Reynolds numbers, respectively, by $R=u_{r m s} / \nu_{c}$ and $R_{m}=u_{r m s} / \mu_{c}$ where $\left.u_{r m s}=\left[\left.\langle | \mathbf{u}\right|^{2}\right\rangle\right]^{1 / 2}$ is the root-mean-square value of the velocity.

The simulations were performed on the Cray Y-MP at NASA-Goddard using a pseudospectral algorithm. The grid resolution is $64^{2}$. This implies a wavenumber range of $0 \leq\left|k_{i}\right| \leq 32$ for each component, $i=x, y$.

The initial condition is a flat spectrum of random kinetic and magnetic fluctuations between $1 \leq|\mathbf{k}| \leq \mathbf{5}$. The total energy is unity and is equipartitioned between kinetic and magnetic fluctuations. The cross helicity is low, $H_{c}=0.001$, signifying that the velocity and magnetic fields are essentially uncorrelated. The magnetic helicity is fixed at $H_{m}=0.1$. The sonic Mach number is set to $M_{s 0}=0.3$ while the Alfvénic Mach number is $M_{a 0}=1.0$. The density is $\rho=1.0+\delta \rho$ where $\delta \rho$ is a pseudosound correction [Ghosh and Matthaeus, 1990] that minimizes the influence of acoustic waves in the initial state and maintains a nearly incompressible ordering. We set the Reynolds numbers to $R=R_{m}=250$ for the dissipative runs, and the ambient magnetic field is $\mathbf{B}_{0}=1.0 \hat{x}$ when present. These are basically the
same initial conditions used by Stribling and Matthaeus [1992] for their incompressible 3-D simulations after neglecting fluctuations along the $\hat{z}$ direction and including the pseudosound correction in the density.

## 3. SIMULATION RESULTS

Four simulations were run using the initial condition described above. All the simulations were run to approximately ten eddy turnover times, $T_{E} \approx 10$. The first run, Run (a), contains an ambient magnetic field and dissipation. The second run, Run (b), contain no ambient magnetic field, but retains dissipation. The third run, Run (c), contains an ambient magnetic field, but is ideal (non-dissipative). Finally, the last run, Run (d), is both ideal and lacks an ambient magnetic field.

As expected, $H_{m}$ is constant in Run (d), the ideal, homogeneous case. However, the mere introduction of dissipation as in Run (b) does not lead to a significant decrease in $H_{m}$. We find that $H_{m}$ decays monotonically to about sixty percent of the initial value after $T_{E} \approx 7$ in Run (b). On the other hand, the presence of an ambient magnetic field, as in Runs (a) and (c), causes substantial decreases in $H_{m}$. In both these cases, $H_{m}$ decays abruptly to about twenty percent of the initial value by $T_{E} \approx 0.5$. Eventually, less than ten percent of the initial $H_{m}$ is remains after $T_{E} \approx 10$. The time history of $H_{m}$ from Runs (a), (b) and (c) are shown in Figure 1. It is clear that for the adopted values of $R_{m}$ and $\mathbf{B}_{0}$, the presence of an ambient magnetic field is a much stronger influence on the decay of $H_{m}$ than the presence of dissipation. This result is consistent with Fig. 4 of Stribling and Matthaeus [1992] and implies that weak compressibility ( $M_{\mathbf{s 0}}=0.3$ ) does not substantially alter the dynamics of $H_{m}$ from the incompressible 3-D model for the selected initial state.

Although $H_{m}$ decays rapidly from its initial value, the change in $\hat{H}_{m}$ is much more gradual in our simulations. $\hat{H}_{m}$ retains more than eighty percent of its original value at $T_{E} \approx 10$ in Run (a). As is evident from (1), this results in a rapid buildup of $\mathbf{A}_{0}$. The growth of $\mathbf{A}_{0}$ is associated with a mean electric field pulse, $\vec{E}$, which can be derived by taking the spatial average of (2c):

$$
\vec{E}=-\langle\mathbf{u} \times \mathbf{B}\rangle=-\frac{\partial}{\partial t} \mathbf{A}_{0} .
$$

The time histories of $H_{m}, \hat{H}_{m}$, and $\vec{E}$ from Run (2) are shown in Figure 2. Again, the similarity of our compressible $2 \frac{1}{2}$-D result to the incompressible 3-D model [Stribling and Matthaeus, 1992] is clear.

The spectral distribution of magnetic helicity in the
solar wind has been considered by Goldstein, Roberts and Fitch [1991, 1992] in studying the wavenumber distribution of the normalized reduced magnetic helicity. The normalized magnetic helicity distribution can be studied from our compressible $2 \frac{1}{2}$-D simulations as well. We define the normalized magnetic helicity as

$$
\sigma_{m}(k)=k H_{m}(k) / E_{B}(k)
$$

![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-4.jpg?height=671&width=804&top_left_y=678&top_left_x=1087)
Fig. 1. Time history of $H_{m}$ from a simulation with dissipation and an ambient magnetic field, Run (a) (solid line), a simulation with dissipation and no ambient magnetic field, Run (b) (dashed line), and a simulation with a ambient magnetic field but no dissipation, Run (c) (dotted line).

![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-4.jpg?height=679&width=809&top_left_y=1565&top_left_x=1096)
Fig. 2. Time histories of $\hat{H}_{m}$ (solid line), $H_{m}$ (dashed line), and $\vec{E}$ (dotted line) from Run (a), the simulation with dissipation and an ambient magnetic field.

where $E_{B}(k)$ is the magnetic power spectrum. The distribution of $\sigma_{m}(k)$ over three time intervals from Run (a) is shown in Figure 3. The time intervals are $0 \leq T_{E} \leq 3$ (solid line), $3 \leq T_{E} \leq 6$ (dashed line), and $6 \leq T_{E} \leq 9$ (dotted line). For these simulations the initial state would appear as a delta function at $\sigma_{m}(k)=0.1$. Hence, it is interesting that the distribution covers the entire range of $\sigma_{m}(k)$ after only a few eddy turnover times. The $\sigma_{m}(k)$ distribution is biased towards positive values during the early time interval. The biase changes and lists towards negative values during the intermediate times. Finally, a peaked distribution, centered on zero, emerges during the late time interval. A similar change from positive to negative biase with increasing heliocentric distance, followed by a distribution centered on zero, is seen in the normalized reduced helicity distribution of certain solar wind data [Goldstein et al., 1992].

This result is not necessarily in contradiction with other studies which indicate the persistence of $H_{m}$ at large heliocentric distances [Bieber et al., 1987; Bieber and Smith, 1992]. In the presence of a Kolmogorovlike magnetic energy spectrum as in the solar wind, $H_{m}$ will reflect the magnetic helicity of the large-scale energy-containing eddies while $\sigma_{m}(k)$ will tend to emphasize the magnetic helicity of the turbulent inertialand dissipation-range eddies. It is possible for $H_{m}$ to retain a non-zero value due to the same sign of magnetic helicity among the large-scale eddies while the $\sigma_{m}(k)$ distribution is still centered approximately on zero.

In contrast to the above, the normalized helicity distribution from a simulation where no ambient magnetic field is present shows a somewhat different evolution. The $\sigma_{m}(k)$ distribution between the time intervals $0 \leq T_{E} \leq 3$ (solid line) and $3 \leq T_{E} \leq 8$ (dotted line) from Run (b) is shown in Figure 4. Here the distribution remains biased toward positive values at late times during the simulation.

We do not attempt a more rigorous comparison with observations here. Nevertheless, a similarity between Run (a) and the outwardly expanding solar wind does appear to exist. One difficulty with establishing a closer comparison is that our $\sigma_{m}(k)$ has not been derived from reduced spectra as in the observations. The lack of multi-spacecraft observations means that spectra derived from observations are typically reduced onedimensional functions in the direction of the outwardly expanding solar wind. A careful study would require establishing an angle, $\theta$, between the direction of the solar wind flow and the direction of the mean magnetic field. One could then return to the simulations, select
this direction $\theta$ relative to the $\mathbf{B}_{0}$-direction, and calculate the equivalent one-dimensional spectra of $H_{m}\left(k_{\theta}\right)$ and $E_{B}\left(k_{\theta}\right)$ for comparison with the observations. We defer this detailed study to a future paper.

## 4. DISCUSSION

We have studied the time evolution of $H_{m}$ and $\hat{H}_{m}$

![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-5.jpg?height=676&width=777&top_left_y=781&top_left_x=1128)
Fig. 3. The distribution of $\sigma_{m}(k)$ in the time intervals: $0 \leq T_{E} \leq 3$ (solid line), $3 \leq T_{E} \leq 6$ (dashed line), and $6 \leq T_{E} \leq 9$ (dotted line), from Run (a), the simulation with dissipation and an ambient magnetic field.

![](https://cdn.mathpix.com/cropped/2025_11_22_cc4511b57fe03ea16deag-5.jpg?height=698&width=785&top_left_y=1660&top_left_x=1112)
Fig. 4. The distribution of $\sigma_{m}(k)$ in the time intervals: $0 \leq T_{E} \leq 3$ (solid line) and $3 \leq T_{E} \leq 8$ (dotted line) for Run (b), the simulation with dissipation and no ambient magnetic field.

and have found virtually no difference in their behavior between an incompressible 3-D model presented elsewhere [Stribling and Matthaeus, 1992] and the compressible $2 \frac{1}{2}$-D model presented here. For the chosen set of parameters, $H_{m}$ decays rapidly relative to $\hat{H}_{m}$ whenever an ambient magnetic field is present. In addition, a strong electric field pulse is associated with the initial decay of $H_{m}$.

Our study of the $\sigma_{m}(k)$ distribution indicates that normalized helicity distributions in the solar wind evolve more in accord with turbulent MHD where an ambient magnetic field is present than with turbulent dynamics where it is absent.

Acknowledgments. This research has been supported by NASA through the Solar Terrestrial Theory Programs at the Goddard Space Flight Center and at the Bartol Research Institute.

## REFERENCES

Bieber, J.W., P. Evenson and W.H. Matthaeus, Magnetic Helicity of the IMF and the Solar Modulation of Cosmic

Rays, Geophys. Res. Lett., 14, 864, 1987.
Bieber, J.W., and C.W. Smith, Magnetic Helicity in the Solar Wind: Radial Variation and Cosmic Ray Effects, EOS, 79, 247, 1992.
Ghosh, S., and W.H. Matthaeus, Relaxation processes in a turbulent compressible magnetofluid, Phys. Fluids B, 2, 1520, 1990.
Goldstein, M.L., D.A. Roberts, and C.A. Fitch, The structure of helical interplanetary magnetic fields, Geophys. Res. Lettr., 18, 1505, 1991.
Goldstein, M.L., D.A. Roberts, and C.A. Fitch, Observed properties of helical interplanetary magnetic fields, (this publication).
Matthaeus, W.H., and M.L. Goldstein, Measurement of the rugged invariants of magnetohydrodynamic turbulence, J. Geophys. Res., 87, 6011, 1982.

Stribling, T., and W.H. Matthaeus, Decay of magnetic helicity in ideal magnetohydrodynamics with a DC magnetic field, (this publication).
Zank, G.P., and W.H. Matthaeus, Waves and turbulence in the solar wind, J. Geophys. Res., 97, 17189, 1992.
S. Ghosh, W.T. Stribling and M.L. Goldstein, Code 692, NASA - Goddard, Greenbelt, MD 20771.
W.H. Matthaeus, Bartol Research Institute, Univ. of Delaware, DE 19716.


[^0]:    Space Plasmas: Coupling Between Small
    and Medium Scale Processes
    Geophysical Monograph 86
    This paper is not subject to U.S. copyright. Published in 1995 by the American Geophysical Union

