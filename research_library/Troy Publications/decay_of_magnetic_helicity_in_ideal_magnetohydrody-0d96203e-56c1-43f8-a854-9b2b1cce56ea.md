See discussions, stats, and author profiles for this publication at: https://www.researchgate.net/publication/252716761

## Decay of Magnetic Helicity in Ideal Magnetohydrodynamics with a DC Magnetic Field

Article in Geophysical Monograph Series • January 1995
DOI: 10.1029/GM086p0055

CITATIONS
5

2 authors:
![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-1.jpg?height=78&width=78&top_left_y=832&top_left_x=136)

Troy Stribling
University of Delaware
14 PUBLICATIONS 989 CITATIONS
SEE PROFILE

READS
86
![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-1.jpg?height=78&width=78&top_left_y=832&top_left_x=1032)
W. H. Matthaeus

University of Delaware
919 PUBLICATIONS 45,985 CITATIONS
SEE PROFILE

# Decay of Magnetic Helicity in Ideal Magnetohydrodynamics with a DC Magnetic Field 

Troy Stribling<br>National Research Council, NASA Goddard Space Flight Center, Greenbelt, Maryland<br>William H. Matthaeus<br>Bartol Research Institute, University of Delaware Newark, Delaware


#### Abstract

We show that the magnetic helicity associated with fluctuations in homogeneous threedimensional incompressible ideal magnetohydrodynamics (MHD) with a mean magnetic field decays in time due to nonlinear processes. Evidence is obtained numerically by use of nondissipative spectral method simulations. The process of nonlinear decay is described in terms of a generalized ideal helicity invariant, and is characterized by the transient production of a mean induced electric field aligned with the applied magnetic field. Dissipative simulations are also performed which suggest that the nonlinear decay process causes the magnetic helicity associated with fluctuations to decay at a much faster rate than it would by resistivity alone. The described effect stands in contrast to expectations based on studies of MHD turbulence without an applied mean field, in which magnetic helicity is transferred nonlinearly to long wavelengths, and is preserved in time due to selective decay when dissipation is present.


## 1. BACKGROUND

The magnetic helicity of a turbulent magnetofluid may be defined as,

$$
\begin{equation*}
H_{m}=\frac{1}{2}\langle\mathbf{a} \cdot \mathbf{b}\rangle \tag{1}
\end{equation*}
$$

where $\mathbf{b}$ is the magnetic field, $\mathbf{b}=\nabla \times \mathbf{a}$ defines the vector potential a and $\langle\cdots\rangle$ denotes a spatial average. A popular interpretation of $H_{m}$, suggested by Moffatt [1978], is that $H_{m}$ measures the linkage of magnetic flux tubes. Another interpretation, commonly used in turbulence applications, is obtained by considering the Fourier transform of $\mathbf{b}, \mathbf{b}(\mathbf{k})$. We can think of $H_{m}$ at wavenumber $\mathbf{k}$ as a measure of polarization of the $\mathbf{b}(\mathbf{k})$. Plane polarized $\mathbf{b}(\mathbf{k})$ have zero $H_{m}$ and circularly polarized $\mathbf{b}(\mathbf{k})$ have a maximal value of $H_{m}$ whose magni-

[^0]tude is equal to $|\mathbf{b}(\mathbf{k})|^{2} / k$. Thus $H_{m}$ defined by Eq. (1) gives a measure of the mean polarization of the $\mathbf{b}(\mathbf{k})$. It is this interpretation that is most convenient for this work. The principal result presented here is that when a DC magnetic field is present and $\mathbf{b}$ is defined so that (b) $=0, H_{m}$ defined by Eq. (1) decays from its initial value and fluctuates about zero in the absence of resistivity.

Magnetic helicity is an important measure in magnetohydrodynamics (MHD) because it is conserved in the absence of both dissipation and a DC magnetic field. This conservation law is believed responsible for back transfer of $H_{m}$ in turbulent MHD [Frisch et al., 1975]. Back transfer of $H_{m}$ has been invoked as a mechanism leading to efficient turbulent magnetic dynamo activity in forced [Pouquet et al., 1976; Meneguzzi et al., 1981] and freely decaying MHD [Pouquet and Patterson, 1978; Stribling and Matthaeus, 1991]. Selective decay relaxation, which describes some properties of RFP plasma devices, is also a consequence of $H_{m}$ back transfer in freely decaying three dimensional (3D) MHD [Taylor, 1974; Montgomery et al., 1978; Matthaeus and

Montgomery, 1980; Riyopoulos et al., 1982; Horiuchi and Sato, 1986; Stribling and Matthaeus, 1991]. The presence of magnetic helicity has been shown to slow down the energy decay rate in simulations 3D MHD decay as well [Stribling and Matthaeus, 1991].

On the other hand, particularly in space physics and astrophysics applications, homogeneous MHD turbulence concepts are applied to local samples of the fluid plasma, while externally supported magnetic fields can thread the region without closing in the region of interest. Thís alternative situation may eventually prove to be more relevant than the case of "isolated" homogeneous turbulence which is often modeled using periodic boundary conditions with zero volume averaged magnetic field. The basic underpinning of helicity dynamics in MHD turbulence theory, i.e., the ideal conservation of $H_{m}$, needs to be reconsidered in this case. In this paper we examine the conservation properties of $H_{m}$ for a simple model, in which the MHD turbulence is periodic but evolves in the presence of a specified, externally supported uniform magnetic field. We show, by considering the helicity conservation law, and by use of direct numerical solution of the 3D MHD equations, that helicity behaves dynamically in a somewhat different way than in the case of magnetically isolated MHD turbulence.

Investigation of magnetic helicity in a homogeneous MHD turbulence model with a mean magnetic field might prove relevant for interplanetary applications. In particular the homogeneous MHD turbulence model has been used to interpret MHD scale magnetic field field fluctuations in the solar wind [Matthaeus and Goldstein, 1982], motivating models using periodic boundaries. However, interplanetary space also contains the large scale solar magnetic field, which appears locally (on the scale of a correlation length) as a uniform field. For example at 1 AU the correlation length of the magnetic field fluctuations is of the order of .01 AU while the length scale for gradiants in the solar magnetic field is of the order of 1 AU [Matthaeus and Goldstein, 1982]. Fluctuations in $H_{m}$ have been observed in the solar wind [Matthaeus and Goldstein, 1982; Bieber et al., 1987a; Goldstein et al., 1991]. The inertial range fluctuations in these observations have been shown to be randomly distributed with zero mean, although there is evidence for a net magnetic helicity at the energy containing fluctuation scale [Bieber et al., 1987b; Bieber and Smith, 1992]. It is also believed that $H_{m}$ plays a role in cosmic ray transport in the heliosphere [Bieber et al., 1987a; Bieber et al., 1987b].

We investigate the time behavior of $H_{m}$ for con-
stant density unforced 3D MHD which written in Alfvén speed units has the form,

$$
\begin{align*}
\frac{\partial \mathbf{v}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{v}= & -\nabla p^{*}+\mathbf{b} \cdot \nabla \mathbf{b}+\mathbf{B}_{0} \cdot \nabla \mathbf{b}  \tag{2}\\
& +\nu \nabla^{2} \mathbf{v}  \tag{3}\\
\frac{\partial \mathbf{b}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{b}= & \mathbf{b} \cdot \nabla \mathbf{v}+\mathbf{B}_{0} \cdot \nabla \mathbf{v}+\eta \nabla^{2} \mathbf{b}  \tag{4}\\
\nabla \cdot \mathbf{v}= & 0  \tag{5}\\
\nabla \cdot \mathbf{b}= & 0 \tag{6}
\end{align*}
$$

The fluctuating velocity and magnetic fields, $\mathbf{v}$ and $\mathbf{b}$, each have zero mean, and $\mathbf{B}_{0}$ is the mean magnetic field which is assumed to be constant. The total pressure, $p^{*}$, is determined by a Poisson equation when use is made of the incompressibility condition, Eq. (4). The viscosity and resistivity are $\nu$ and $\eta$, respectively. The time unit is taken to be an eddy turnover time for unit velocity field at unit length scale. A dealiased spectral method is used in the numerical solution of Eqs. (2-5) which assumes periodic boundary conditions in a cube with sides of length $2 \pi$.

Of particular importance in the following discussion are quantities known as "rugged" invariants. These invariants are conserved by arbitrary truncations of the Galerkin representations of Eqs. (2-5) when $\eta=\nu=0$, and are usually considered to be the relevant isolating invariants in a statistical mechanics treatment [Kraichnan, 1975]. When $\mathbf{B}_{0}=0$ there are believed to be only three rugged invariants [Frisch et al., 1975; Stribling and Matthaeus, 1990]. They are the total energy, cross helicity and magnetic helicity. For periodic 3D MHD the rugged invariants are explicitly given by,

$$
\begin{align*}
\boldsymbol{E} & =\frac{1}{2 V} \int|\mathrm{v}|^{2}+|\mathrm{b}|^{2} d^{3} x=E_{v}+E_{b}  \tag{7}\\
\boldsymbol{H}_{\boldsymbol{c}} & =\frac{1}{2 V} \int \mathrm{v} \cdot \mathbf{b} d^{3} x  \tag{8}\\
\boldsymbol{H}_{\boldsymbol{m}} & =\frac{1}{2 V} \int \mathbf{a} \cdot \mathbf{b} d^{3} x \tag{9}
\end{align*}
$$

where $V=8 \pi^{3}$. Each rugged invariant is expressed as a per unit mass quantity, and the integrals are evaluated over a cube with sides of length $2 \pi$. The cross helicity can be viewed as a measure of correlation between the velocity and magnetic fields, and possible interpretations of $H_{m}$ were previously mentioned. If $\mathbf{B}_{0} \neq 0$ the total energy and cross helicity remain rugged invariants. However, with $\mathbf{B}_{0} \neq 0$, magnetic helicity is not an ideal invariant; instead one now has an invariant
which we call the total magnetic helicity [Mattheaus and Goldstein, 1982], defined by

$$
\begin{equation*}
\hat{H}_{m}=H_{m}+\mathbf{B}_{0} \cdot \mathbf{A}_{0} \tag{10}
\end{equation*}
$$

Here $d \mathbf{A}_{0} / d t=\frac{1}{V} \int \mathbf{v} \times \mathbf{b} d^{\mathbf{3}} x=-\overrightarrow{\mathcal{E}}$ represents the time derivative of the $\mathbf{k}=0$ component of the vector potential. The mean induced electric field is given by $\overrightarrow{\mathcal{E}}$ and $H_{m}$ is the fluctuating magnetic helicity given by Eq. (8). It is unclear at present whether the ideal invariant $\hat{H}_{m}$ should be considered to be "rugged", since, although it is quadratic, it is nonlocal in time. A suggested interpretation of the $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ term of $\hat{H}_{m}$ is that it represents magnetic flux linkages associated with structures having scales much larger than the periodic box [Moffatt, 1978; Matthaeus and Goldstein, 1982]. Thus, $\hat{H}_{m}$ can be viewed as a superpositioning of the magnetic helicity of the fluctuating magnetic fields and the linkage of the fluctuating magnetic field with the uniform field. A proper accounting of both of these magnetic helicity contributions is necessary in the construction of the magnetic helicity invariant for homogeneous MHD turbulence in the presence of a DC magnetic field. It should also be noted that $\hat{H}_{m}$ is not the magnetic helicity one would compute using Eq. (1) and also including the DC contributions $\mathbf{A}_{0}$ and $\mathbf{B}_{0}$. The result so obtained would differ from $\hat{H}_{m}$ by an amount $\frac{1}{2} \mathbf{B}_{0} \cdot \mathbf{A}_{0}$.

In the ideal simulations discussed in the following paragraphs we show that $\hat{H}_{m}$ is conserved and that whatever initial $H_{m}$ is in the system decays and proceeds to fluctuate about zero. The decay of $H_{m}$ is concurrent with a growth in $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ in accordance with the conservation law given by Eq. (9). Thus the nonlinear decay process acting on $H_{m}$ is, in fact, a conversion of $H_{m}$ into $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$.

## 2. NUMERICAL RESULTS

Each of the contributions to $\hat{H}_{m}$ from an $32^{3}$ ideal simulation is given in Fig. (1). For this particular run $\mathbf{B}_{0}=1 \hat{\mathbf{z}}, \sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle} / B_{0}=1, E=1, H_{c}=10^{-3}$ and at $t=0, H_{m}=0.1$. The initial energy spectrum was flat with the kinetic and magnetic energy equipartitioned for wavenumbers in the band $1 \leq k \leq 5$. The ratio $\sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle} / B_{0} \sim 1$ is characteristic of the solar wind. The time history of $H_{m}$ is given in Fig. (1a). It is seen that $H_{m}$ decays very quickly to zero while $\hat{H}_{m}$ remains constant, see Fig. (1d). In Fig. (1b) the time history of the $\hat{\mathbf{z}}$ component of spatially averaged electric field $\mathcal{E}_{z}= -\frac{1}{V} \int(\mathbf{v} \times \mathbf{b})_{z} d^{3} x$ is given. Only the $\hat{\mathbf{z}}$ component of $\overrightarrow{\mathcal{E}}$,

![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-4.jpg?height=584&width=793&top_left_y=244&top_left_x=1093)
Fig. 1. Time histories of the quantities which form $\hat{H}_{m}$ for an ideal $32^{3}$ simulation with $E=1, H_{c}=10^{-3}, \sqrt{\left.\left.\langle | \mathrm{b}\right|^{2}\right\rangle} / B_{0}=$ 1 and $\hat{H}_{m}=.1$. The quantities depicted in each plot are: (a) magnetic helicity of fluctuating $\mathbf{b}$, (b) component of mean electric field parallel to $\mathrm{B}_{0}$, (c) component of mean vector potential parallel to $\mathbf{B}_{0}$, which is the time integral of the curve in Fig. (1b) and (b) the total magnetic helicity $\hat{H}_{m}$.

![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-4.jpg?height=511&width=717&top_left_y=1158&top_left_x=1112)
Fig. 2. Time history of $H_{m}$ for an ideal $8^{3}$ simulation with $E=1, H_{c}=0.2, \sqrt{\left.\left.\langle | \mathrm{b}\right|^{2}\right\rangle} / B_{0}=1$ and $\hat{H}_{m}=0.2$ which was integrated out to 1200 eddy turnover times.

which in the simulations lies along $\mathbf{B}_{0}$, enters into $\hat{H}_{m}$. Most noticeable is the pulse in $\mathcal{E}_{z}$ which coincides with the period of most rapid decay in $H_{m}$. The time integral of $\mathcal{E}_{z}$, the $\hat{\mathbf{z}}$ component of $\mathbf{A}_{0}$, is depicted in Fig. (1c). The pulse in $\mathcal{E}_{z}$ gives rise to rapid growth in $A_{0 z}$ which signifies the conversion of $H_{m}$ into $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$. Because $\hat{H}_{m}$ is conserved during this process, the fluctuations in $\mathcal{E}_{z}$ are perfectly correlated with the $d H_{m} / d t$ fluctuations.

In Fig. (2) the time history of $H_{m}$ is given for an $8^{3}$ simulation integrated for 1200 eddy turn over times. This is much longer than the time history given in Fig. (1a) and illustrates the fluctuating character of $H_{m}$ af-
ter the nonlinear decay process has converted the majority of $H_{m}$ into $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$. For this run $\mathbf{B}_{0}=1 \hat{\mathbf{z}}$, $\sqrt{\left.\left.\langle | \mathrm{b}\right|^{2}\right\rangle} / B_{0}=1, E=1, H_{c}=0.2$ and at $t=0$, $H_{m}=0.2$. This longer simulation is used to compute long time averages of the $H_{m}$ spectrum. A convenient measure of the polarization of the $\mathbf{b}$ fluctuations at a wavenumber $\mathbf{k}$ is given by $\sigma_{m}(\mathbf{k})=k H_{m}(\mathbf{k}) / E_{b}(\mathbf{k})$, where $E_{b}(\mathbf{k})$ is the magnetic energy in wavenumber k. A value of $\pm 1$ for $\sigma_{m}(\mathbf{k})$ indicates that the fluctuations are circularly polarized with handedness determined by the sign. A value of zero indicates plane polarization. Fig. (3) depicts the omnidirectional spectrum of $\boldsymbol{k}\left\langle H_{m}(\mathbf{k})\right\rangle /\left\langle E_{b}(\mathbf{k})\right\rangle$. Here $(\cdots)$ represents a time average. This quantity gives a measure of the mean polarization of the $\mathbf{b}$ fluctuations at wavenumbers with magnitude $k$. We see that the mean polarization is near zero across the spectrum which is consistent with the behavior of the time history of $H_{m}$ depicted in Fig. (3). This differs significantly from the $B_{0}=0$ case in which $H_{m}$ is conserved and thus a nonzero mean polarization at each wavenumber is obtained in nondissipative simulations [Stribling and Matthaeus, 1990]. In the analysis of interplanetary magnetic field fluctuations investigators have generally found that the high wavenumber magnetic field polarizations average to zero Matthaeus and Goldstein, 1982; Goldstein et al., 1991]. The present result is in qualitative agreement with the observations, suggesting that the MHD scales of the interplanetary environment may be consistent with a model which in which $\hat{H}_{m}$ is the relevant ideal invariant instead of $H_{m}$. However, this feature may not be a sensitive discriminator, since higher wavenumber fluctuations in dissipative MHD without an applied magnetic field may share this characteristic.

An interesting consequence of the conservation of $\hat{H}_{m}$ and the subsequent decay of $H_{m}$ is the previously mentioned transient $\mathcal{E}_{z}$ which persists while $H_{m}$ is decaying. If $\hat{H}_{m}$ is examined and it is assumed that $H_{m}$ goes to zero some properties of the $\mathcal{E}_{z}$ pulse can be determined. First, assume that $H_{m}(t=0)>0$. Since $H_{m}$ decays as time progresses, in order to conserve $\hat{H}_{m}$ the $\mathbf{B}_{0} \cdot \mathbf{A}_{0}$ term must be positive and increasing while $H_{m}$ is decreasing. This in turn requires that the component of the electric field along $\mathbf{B}_{0}, \mathcal{E}_{\|}$, have the sign opposite of $\mathbf{B}_{0}$ as $H_{m}$ decreases (recall that $d \mathbf{A}_{0} / d t=-\overrightarrow{\mathcal{E}}$ ). In a similar vein if $H_{m}(t=0)<0$ then a transient $\mathcal{E}_{\|}$is generated in the same direction of $\mathbf{B}_{0}$. The transient $\mathcal{E}_{\|}$for the $32^{3}$ ideal simulation can be seen in Fig. (1b).

To verify that ideal magnetic helicity decay process is not significantly modified in dissipative MHD, we performed two $32^{3}$ dissipative simulations with $\eta=\nu=$

![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-5.jpg?height=514&width=712&top_left_y=390&top_left_x=1163)
Fig. 3. Time averaged normalized magnetic helicity spectrum for the $8^{3}$ simulation.

![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-5.jpg?height=516&width=703&top_left_y=1028&top_left_x=1161)
Fig. 4. Comparison of $H_{m}$ time histories for Runs (a), (b) and (c).

0.01. In particular we are interested in examining the dissipative and nondissipative contributions to the time rate of change of $H_{m}$, namely,

$$
\begin{equation*}
\frac{d H_{m}}{d t}=-\mathbf{B}_{0} \cdot\langle\mathbf{v} \times \mathbf{b}\rangle-\eta\langle\mathbf{j} \cdot \mathbf{b}\rangle \tag{11}
\end{equation*}
$$

as $\mathbf{B}_{0}$ and $\eta$ are varied. Here $\mathbf{j}=\nabla \times \mathbf{b}$ is the current and $(\cdots)$ represents a spatial average. The $-\mathbf{B}_{0} \cdot\langle\mathbf{v} \times \mathbf{b}\rangle$ term represents the ideal contribution and the $-\eta\langle\mathbf{j} \cdot \mathbf{b}\rangle$ term the resistive contribution of the $H_{m}$ time derivative. The initial conditions for two dissipative runs are identical to the initial condition of the $32^{3}$ ideal simulation previously discussed. The values given to $\mathbf{B}_{0}$ and $\eta$ for this parameter space scan are: Run (a), $\mathbf{B}_{0}=1 \hat{\mathbf{z}}$, $\eta=0.01 ;$ Run (b) $\mathbf{B}_{0}=0, \eta=0.01$; Run (c) $\mathbf{B}_{0}=1 \hat{\mathbf{z}}$, $\eta=0$. The time histories of $H_{m}$ are compared for the three runs in Fig. (4). The slowest decay rate occurs in the simulation where there is only resistive decay of $H_{m}$, Run (b). A much faster decay rate for $H_{m}$ is real-

![](https://cdn.mathpix.com/cropped/2025_11_22_7be5c362c244896beb0eg-6.jpg?height=505&width=720&top_left_y=263&top_left_x=244)
Fig. 5. Comparison of time histories of nonlinear and resistive decay terms (see Eq. 10) for Run (a).

ized in the presence of a mean magnetic field, Runs (a) and (c). It is also interesting to note that the contribution of the resistive term in the time evolution of $H_{m}$ is quite small for nonzero $\mathbf{B}_{0}$, since there is little difference in the $H_{m}$ time histories for Runs (a) and (c). In Fig. (5) the time histories of the nonlinear and resistive contributions to $d H_{m} / d t$ are shown for Run (a). Upon examination of Fig. (5) it can be seen that the suspicion that resistive decay contributes little compared to the ideal decay term in the time evolution of $H_{m}$ was correct. It should be kept in mind that here only the strong $\mathbf{B}_{0}$, (i.e. $\mathbf{B}_{0} \approx \sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle}$ the parameter regime most relevant to interplanetary plasmas) limit has been investigated. If $\mathbf{B}_{0}$ is small relative to $\sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle}$ it is possible that resistive decay will dominate.

## 3. CONCLUSIONS

The principal results of this paper can be summarized as follows. Simulations of ideal and dissipative 3D MHD with a mean magnetic field have been presented. We have shown the magnetic helicity defined by Eq. (8) decays from its initial value and fluctuates about zero in the ideal simulations. The decay of $H_{m}$ is concurrent with a pulse in the component of the mean electric field parallel to $\mathbf{B}_{0}$. The time average of the magnetic helicity spectrum also has properties qualitatively similar to the average helicity spectrum measured for $b$ fluctuations in the solar wind. This result raises the possibility that the MHD scales of the solar wind may be described by a model in which $\hat{H}_{m}$ is the relevant ideal invariant as opposed to $H_{m}$.

The dissipative simulations suggest that when $B_{0} \sim \sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle}, H_{m}$ decays at a faster rate that it would in the absence of $\mathbf{B}_{0}$. This could lead to quite significant dif-
ferences in the structure of high Reynolds number turbulence for systems with and without a mean magnetic field. Most notable is that the presence of $\mathbf{B}_{0}$ could cause a diminution of $H_{m}$ back transfer effects, such as selective decay [Matthaeus and Montgomery, 1980], upon the long wavelength fluctuations. It is possible that for this reason no conclusive evidence of $H_{m}$ back transfer has been found in interplanetary magnetic field fluctuations [Goldstein et al., 1984].

Our work thus far, though not discussed here, indicates that the rate of $H_{m}$ decay by the nonlinear decay process varies greatly with $H_{c}$ and $\sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle} / B_{0}$. Hence, it is likely that for some values of $H_{c}$ and $\sqrt{\left.\left.\langle | \mathbf{b}\right|^{2}\right\rangle} / B_{0}$, different from those chosen here, the strength of the nonlinear decay process in dissipative MHD could lessen.

Acknowledgments. The authors would like to thank S. Ghosh, M. L. Goldstein, S. Oughton and D. A. Roberts for helpful comments, the NASA Center for Computational Sciences for computer time and the National Academy of Sciences for financial support.

## REFERENCES

Bieber, J. W., P. Evenson and W. H. Matthaeus, Magnetic Helicity of the Parker Field, Astrophysical J., 315, 700 (1987a).
Bieber, J. W., P. Evenson and W. H. Matthaeus, Magnetic Helicity of the IMF and the Solar Modulation of Cosmic Rays, Geophysical Res. Lett., 14, 864 (1987b).
Bieber, J. W. and C. W. Smith Magnetic Helicity in the Solar Wind: Radial Variation and Cosmic Ray Effects, EOS, 73, 247 (1992).
Frisch, U., A. Pouquet, J. Léorat and A. Mazure, Possibility of an Inverse Cascade of Magnetic Helicity in Magnetohydrodynamic Turbulence, J. Fluid Mech., 68, 769 (1975).

Goldstein, M. L., L. F. Burlaga and W. H. Matthaeus, Power Spectra of Interplanetary Corotating and Transient Flows, J. Geophys. Res., 89, 3747 (1984).
Goldstein, M. L., D. A. Roberts and C. A. Fitch, The Structure of Helical Interplanetary Magnetic Fields, GRL, 18, 1505 (1991).
Horiuchi, R. and T, Sato, Self-Organization and Energy Relaxation in a Three-Dimensional Magnetohydrodynamic Plasma, Phys. Fluids, 29, 1161 (1986).
Kraichnan, R. H., Statistical Dynamics of Two-Dimensional Flow, J. Fluid Mech., 67, 155 (1975).
Matthaeus, W. H. and D. Montgomery, Selective Decay Hypotheses at High Mechanical and Magnetic Reynolds Numbers, Ann. N.Y. Acad. Sci., 357, 202 (1980).
Matthaeus, W. H., and M. L. Goldstein, Measurement of the Rugged Invariants of Magnetohydrodynamic Turbulence in the Solar Wind, J. Geophys. Res., 87, 6011 (1982).

Meneguzzi, M., U. Frisch and A. Pouquet, Helical and Nonhelical Turbulent Dynamos, Phys. Rev. Lett., 47, 1069
(1981).

Moffatt, H. K., Magnetic Field Generation in Electrically Conducting Fluids, Cambridge University Press, Cambridge (1978).
Montgomery, D., L. Turner and G. Vahala, ThreeDimensional Magnetohydrodynamic Turbulence in Cylindrical Geometry, Phys. Fluids, 21 , 757 (1978).
Pouquet, A., U. Frisch and J. Léorat, Strong MHD Helical Turbulence and the Nonlinear Dynamo Effect, J. Fluid Mech., 77, 321 (1976).
Pouquet, A. and G. S. Patterson, Numerical Simulation of Helical Magnetohydrodynamic Turbulence, J. Fluid Mech., 85, 305 (1978).
Riyopoulos, S., A. Bondeson and D. Montgomery, Relaxation toward States of Minimum Energy in a Compact Torus, Phys. Fluids, 25, 107 (1982).

Stribling, T. and W. H. Matthaeus, Relaxation Processes in a Low-Order Three-Dimensional Magnetohydrodynamics Model, Phys. Fluids B, 8, 1848 (1991).
Stribling, T. and W. H. Matthaeus, Statistical Properties of Ideal Three-Dimensional Magnetohydrodynamics, Phys. Fluids B, 2, 1979 (1990).
Taylor, J. B., Relaxation of Toroidal Plasma and Generation of Reverse Magnetic Fields, Phys. Rev. Lett., 33, 1139 (1974).
T. Stribling, NASA Goddard Space Flight Center, Code 692, Greenbelt Rd., Greenbelt MD 20771
W. H. Matthaeus Bartol Research Institute, University of Delaware, Newark, Delaware 19716


[^0]:    Space Plasmas: Coupling Between Small
    and Medium Scale Processes
    Geophysical Monograph 86
    Copyright 1995 by the American Geophysical Union

