# The evolution of Alfvénic perturbations in a three-dimensional MHD model of the inner heliospheric current sheet region 

T. Stribling, ${ }^{1}$ D. A. Roberts and M. L. Goldstein<br>Laboratory for Extraterrestrial Physics, NASA Goddard Space Flight Center, Greenbelt Maryland


#### Abstract

We investigate an idealized model of the evolution of magnetohydrodynamic (MHD) scale velocity and magnetic field fluctuations in the equatorial region of the inner heliosphere at solar minimum. In this model a three-dimensional current sheet is constructed from a sheared magnetic field embedded between two velocity shear layers. Simulations of the incompressible MHD equations are used to study the evolution of a variety of perturbations to this configuration. We also perform a linear stability analysis using the solutions of the Orr-Sommerfeld and related equations for the current sheet model. From simulations in which the model is perturbed with small amplitude Alfvén waves, we find that the perturbing velocity and magnetic fields become decorrelated in the region of velocity and magnetic shear during the linear evolution of the fluid instability. This result and similar results for large amplitude perturbations agree qualitatively with previous two-dimensional simulations and with observations made by the Helios spacecraft at current sheet crossings between 0.3 and 1 AU and gives further evidence that shear-driven fluid instabilities provide a mechanism for the destruction of velocity-magnetic field correlation. The simulations also show enhancement of the power in the radial components of the perturbing velocity and magnetic fields in regions where they are sheared, in agreement with observations. We show that the linear evolution of transverse perturbations to the sheared fields gives rise to these radial power enhancements. While these simulations elucidate the three-dimensional evolution of shear flows, they must be extended further to include compression and expansion of the wind.


## 1. Introduction

The solar wind is most simply described as a Parker spiral magnetic field embedded in a $400 \mathrm{~km} / \mathrm{s}$ average radial plasma flow upon which fluctuations are superposed. Ignoring transients, the largest departures from uniformity are the streams of high- and low-speed wind. Next in importance are the large-amplitude incompressive fluctuations that are predominantly seen as Alfvén waves in the inner heliosphere and that range in scale from the size of the streams down to periods of about a second in the spacecraft frame. There are also compressive fluctuations seen in variations in the density, pressure, and other quantities; at times these attain

[^0]Copyright 1996 by the American Geophysical Union.
Paper number 96JA02583.
0148-0227/96/96JA-02583\$09.00
fairly high amplitudes, but generally they contain relatively little energy except at the largest scales and where streams interact. All the above components of the wind-mean field, streams, incompressive fluctuations, and compressive fluctuations-interact dynamically, and all are affected by the overall expansion of the plasma as it recedes from the Sun. (See reviews by Tu and Marsch [1995] and Goldstein et al. [1995] for details on these and other points in this introduction.)

The general conclusion that the above interactions are fundamentally nonlinear and involve turbulent cascades is now generally accepted, but the relative role of some of these processes is still in dispute. It is clear that expansion has the dominant effect on fluctuation levels and the temperature of the wind, but the linear description of waves in an expanding medium fails to provide an adequate explanation for the observed evolution, including the anisotropies, Alfvénicity, and power spectral evolution of the fluctuations [see, e.g., Roberts, 1992]. Completely analytical approaches to the nonlinear problem of solar wind dynamics cannot describe even the simplest nonexpanding turbulent cas-
cade, and thus approximations must be made to understand the role of various processes. Two main approaches are used, both of them within the context of a standard magnetohydrodynamic (MHD) model. The first takes the mean Parker spiral structure, perhaps including the stream structure, as a fixed background in which the smaller-scale fluctuations evolve; this was used both in the earlier WKB approach [see Hollweg, 1978] and in more recent turbulence models [Marsch and Tu, 1993; Zhou and Matthaeus, 1990; Schmidt and Marsch, 1995; Schmidt, 1995; Oughton and Matthaeus, 1995]. This rather artificial scale division allows one to include a model of turbulent dynamics and the effects of expansion, while treating complications such as wind acceleration independently. In this approach the linear interaction of the fluctuations with the large-scale expanding plasma can be treated quite completely, while the nonlinear terms are usually treated as a diffusion or flux in Fourier space with transport coefficients determined empirically or by scaling arguments. The complications of compressibility have begun to be dealt with in the multiple-scales approach [Zank and Matthaeus, 1993, and references therein] which shows in homogeneous flows (i.e., in the absence of expansion) that incompressible fields are dominant at low Mach number [see also Roberts et al., 1991].

The second approach, and the one we focus on here, is that of direct simulation of the solar wind using the MHD equations with progressively more realistic approximations [Roberts et al., 1991, 1992; Roberts, 1992; Grappin et al. 1993; Grappin and Velli,1996]. This approach avoids the separation of scales between streams and other fluctuations, and calculates nonlinear cascades explicitly. Until relatively recently, the codes used were typically in two dimensions for both fields and space and used incompressible dynamics in a nonexpanding, periodic geometry. Three-dimensional, compressible, periodic codes are now being used, and the problem of expansion has been approached in an approximate but useful way by including terms that describe the transverse expansion of the box in a compressible code with two spatial dimensions and threedimensional fields [Grappin et al. 1993; Grappin and Velli,1996]. Results from the expanding box model have shown that expansion not only decreases the amplitudes of the fluctuations in the expected way but also can change the cascade rates. Solution of the selfconsistent problem of an expanding, compressible, accelerated three-dimensional plasma with an embedded field and an initial wave population has not yet been achieved. By systematically increasing the complexity and generality of the simulations, we can better understand the origin of effects in the more complex simulations and, more importantly, in the real solar wind.

For the present study we have extended the previous two-dimensional incompressible MHD simulations by adding a third dimension to both space and the field vectors, but we still retain incompressibility and peri-
odic geometry. This allows us to check the effects of the third dimension against the previous results, and it keeps the analysis sufficiently simple to allow us to make connections to a scale-separated approach. In particular, in addition to examining shear layer flows in the presence of a current sheet using the full MHD equations, we also both analytically and numerically solve for the evolution of three-dimensional perturbations to a fixed background sheared flow with a fixed current sheet. This work provides a different approach to attaining an analytical understanding of such problems as the origin of the anisotropies and decreases in Alfvénicity seen in previous observational and simulation work. The perturbation approach used here is based on, and thus provides connections to, previous work on three-dimensional instabilities in fluid flows. There may be a deeper significance in the linear approach: Grappin and Velli [1996] argue that in the expanding solar wind, nonlinear interactions are slowed, leading to the enhanced importance of the linear interaction between the small scales and the large-scale features. They also argue that, in fact, most of the simulations of solar wind "turbulence" published to date are dominated by such nonlocal interactions because the power spectra involved are very steep. It remains to be seen whether simulations with more realistic spectra behave in a qualitatively different manner from those run previously. Because we use standard dissipation models in this study, we cannot address this issue directly, and thus we must defer consideration of this point to future work.

The next section describes the MHD model and the initial conditions used. Section 3 examines small perturbations to the shear layers, and these are examined analytically in section 4. Section 5 reports on MHD simulations of small amplitude perturbations and relates them to linear theory and observed properties of the fluctuations. Section 6 presents results of a higherresolution simulation of a large-amplitude perturbation and relates the effects observed to the previous sections. The implications and limitations of the simulations are discussed in the final section.

## 2. Model Description

The main point of the present work is to extend previous studies to include the third dimension. This permits a more realistic representation of the three-dimensional structure of the current sheet as observed by the Helios spacecraft. For example, when a shear layer is embedded in a magnetic field parallel to the velocity shear layer, the most unstable wave modes will probably have wave vectors that are not parallel to the field because these will involve less bending of field lines. Most such modes can only be described in three dimensions. From a different viewpoint, to the extent the evolution of fluctuations involves a cascade of energy to wave vectors perpendicular to the mean field [see Oughton, et al.,

1994, and references therein] a two-dimensional simulation limits the perpendicular wave vectors to a line, whereas three dimensions allows a plane.

We make the assumption of incompressibility motivated by observations, theory, and simulations: relative density fluctuations are usually small [e.g. Roberts et al., 1987a] as is the energy associated with them [e.g. Tu et al., 1990]; in low turbulent Mach number flows, the incompressible description is correct to lowest order [Montgomery et al., 1987; Zank and Matthaeus, 1993]; and some two-dimensional simulations have shown that compressive effects do not fundamentally change the incompressive evolution [see, for example, Roberts et al., 1991; Roberts, 1992]. If compressibility is finally found to be of deeper significance than this discussion suggests [see, e.g., Bruno and Bavassano, 1993; Grappin and Velli, 1996], it will be through comparison with results such as those presented here that this will be determined.

As mentioned above, in this work we also neglect the expansion of the wind; this is certainly a serious restriction, but, in the spirit of most previous work, we assume that the basic processes seen here will be present in the more general case, although in modified form. A twodimensional expanding, periodic box model has been used recently by Grappin et al. [1993] and Grappin and Velli [1996], and their results indicate that the interactions we describe may be slowed substantially by the expansion. However, they considered very weak azimuthal shear layers (due principally to the two-dimensional restriction), whereas the observations show strong latitudinal gradients; it is the latter that we attempt to model here, within the limits of the code resolution. Only more general simulations and further analytical work will resolve the precise relative role played by expansion and nonlinear interactions.

### 2.1. Three-Dimensional MHD Equations

The unforced, three-dimensional, MHD equations for constant-density in dimensionless form are

$$
\begin{align*}
\frac{\partial \mathbf{v}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{v} & =-\nabla p^{*}+\mathbf{b} \cdot \nabla \mathbf{b}+\nu \nabla^{2} \mathbf{v}  \tag{1}\\
\frac{\partial \mathbf{b}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{b} & =\mathbf{b} \cdot \nabla \mathbf{v}+\eta \nabla^{2} \mathbf{b}  \tag{2}\\
\nabla \cdot \mathbf{v} & =0  \tag{3}\\
\nabla \cdot \mathbf{b} & =0 \tag{4}
\end{align*}
$$

The fluctuating velocity and magnetic fields, $\mathbf{v}$ and $\mathbf{b}$, each have zero mean, and $\mathbf{b}$ is normalized by the squareroot of a typical density to make it have the same units as $\mathbf{v}$. The total (thermal plus magnetic) pressure, $p^{*}$, is determined by a Poisson equation when use is made of the incompressibility condition (3). The viscosity and resistivity are $\nu$ and $\eta$, respectively, and the inverses of these are the kinetic and magnetic Reynolds numbers. The time unit is taken to be an eddy turnover time for unit velocity field at unit length scale. A dealiased spec-
tral method is used in the numerical solution of (1)-(4) which assumes periodic boundary conditions in a cube with sides of length $2 \pi$. In the following sections sheared velocity and magnetic field profiles are perturbed with large and small amplitude Alfvénic perturbations, and (1)-(4) are integrated in time. The results are compared with observations and the predictions of the linear theory.

Only three quantities are believed to be conserved for arbitrary truncations of the Galerkin representations of (1)-(4) [Frisch et al., 1975; Stribling and Matthaeus, 1990]. These quantities are referred to as "rugged" invariants and are usually considered to be the relevant isolating invariants in a statistical mechanics treatment [Kraichnan, 1975]. They are the total energy, cross helicity and magnetic helicity; for periodic threedimensional MHD the rugged invariants are given respectively by

$$
\begin{align*}
E & =\frac{1}{2 V} \int|\mathbf{v}|^{2}+|\mathbf{b}|^{2} d^{3} x=E_{v}+E_{b}  \tag{5}\\
H_{c} & =\frac{1}{2 V} \int \mathbf{v} \cdot \mathbf{b} d^{3} x  \tag{6}\\
H_{m} & =\frac{1}{2 V} \int \mathbf{a} \cdot \mathbf{b} d^{3} x \tag{7}
\end{align*}
$$

where $V=8 \pi^{3}$ and $\mathbf{a}$ is the vector potential. Each rugged invariant is expressed per unit mass, and the integrals are evaluated over a cube with sides of length $2 \pi$. Note that these quantities are not conserved in expanding geometries, thus providing an additional rationale for first considering solutions in cartesian geometry.

The magnetic helicity $H_{m}$ is a measure of linkage of magnetic flux [Moffatt, 1978] and is also related to the polarization of the magnetic field. A maximum value for $H_{m}$ is obtained when the magnetic field fluctuations are circularly polarized and a minimum value when the fluctuations are plane polarized. Magnetic helicity is believed to be transferred from high to low wave numbers by the nonlinear couplings of (1)-(4) [Frisch et al., 1975]. Back transfer of $H_{m}$ has been invoked as a mechanism leading to efficient turbulent magnetic dynamo activity in forced [Pouquet et al., 1976; Meneguzzi et al., 1981] and freely decaying MHD [Pouquet and Patterson, 1978; Stribling and Matthaeus, 1991]. It is also thought that the presence of $H_{m}$ slows down the rate of spectral transfer of energy, but in the presence of a mean magnetic field the fluctuating helicity rapidly goes to zero [Stribling and Matthaeus, 1990, 1991], consistent with solar wind measurements [Goldstein et al., 1994]. We will take $H_{m}$ to be very small globally in all our simulations, although the perturbations are initially highly helical in each mode.

The cross helicity $H_{c}$ gives a measure of correlation between the velocity and magnetic fields. For Alfvénic fluctuations $H_{c}$ is maximum and equal to $E / 2$ because $\delta \mathbf{v}=\delta \mathbf{b}$. The presence of $H_{c}$ slows down the rate of spectral transfer of energy [Dobrowolny et al., 1980;

Grappin et al., 1983; Matthaeus and Zhou, 1989], at least for incompressible MHD. Both the cross and magnetic helicity are important in the characterization of velocity and magnetic field fluctuations in the solar wind [Matthaeus and Goldstein, 1982]. Measurements of both quantities and their radial evolution in the solar wind have been made [Matthaeus and Goldstein, 1982; Roberts et al., 1987a, b; Bruno and Bavassano, 1993; Grappin et al., 1990; Tu and Marsch, 1991; Goldstein et al., 1994, 1995]. We will use initial conditions that have high cross helicity in the fluctuations, consistent with observations of large, relatively undisturbed fast or slow streams, and with the viewpoint that nearly all the deviations from high Alfvénicity are due to dynamical evolution [Roberts et al., 1991].

### 2.2. Shear Field Model

We wish to study the temporal evolution of a plasma fluid parcel in the equatorial region of the inner heliosphere near solar minimum. To do this we constructed a model equilibrium state containing sheared velocity and magnetic fields that are perturbed by Alfvénic fluctuations of various amplitudes with varying distributions in wave number space. Integration in time of (1)-(4) models the advection of the fluid parcel away from the Sun. Previous numerical investigations of the dynamics of ve-

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-04.jpg?height=901&width=825&top_left_y=1368&top_left_x=159)
Figure 1. Hour-averaged data from Helios 2 near 0.3 AU starting at day 92 in 1976. From the top the panels are the solar wind speed, the magnitude of the magnetic field, the radial component of the magnetic field normalized by the field magnitude, the normalized cross helicity at the 3 -hour scale, the ratio or the energy in fluctuations in the radial component of the magnetic field to the total fluctuating magnetic energy, and, finally, same ratio for the velocity.

locity and magnetic shear in the inner heliosphere were in two spatial dimensions [Roberts et al., 1991, 1992; Malara et al., 1992, 1996; Veltri et al., 1992; Roberts, 1992; Grappin and Velli, 1996] in which the current sheet was a neutral line. The actual current sheet has a more complex three-dimensional structure as indicated in Figure 1, which shows the hour-averaged solar wind velocity and the magnitude and radial component of the magnetic field near 0.3 AU from the Helios mission. The current sheet is crossed at approximately hour 230 . The magnitude of the magnetic field in Figure 1 shows that there is no neutral point in the current sheet and (comparing the second and third panels from the top) that the solar magnetic field is predominately radial outside the region of magnetic shear, indicating that the magnetic field rotates through the sector boundary. The solar wind speed in Figure 1 also shows that the current sheet is in the middle of the low speed wind which is separated from the high-speed wind by two shear layers, one of them relatively sharp. (Note that the "shear layer" on the left is very weak; we presume that this region has been stretched, as the other shear layer has been compressed, and that a more symmetrical condition prevailed earlier.)

The current sheet we construct includes a magnetic shear with two vector components to model the rotation of the magnetic field through the sector boundary. (A very similar current sheet model, but one with different initial conditions, is considered by Malara et al. [1996].) We define the fields such that the $\hat{\mathbf{z}}$ direction corresponds to the direction of latitudinal variation ( $N$ in heliographic coordinates), the $\hat{\mathbf{y}}$ direction corresponds to the direction of longitudinal variation (the $T$ direction) and the $\hat{\mathbf{x}}$ direction corresponds to the radial the radial (R) direction. The initial profiles of the $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ components of the magnetic field and the $\hat{\mathbf{x}}$ component of the velocity field for a $32^{3}$ simulation are shown in Figure 2. The $\hat{\mathbf{x}}$ component of the sheared magnetic field $B_{x}(z)$ varies only in the $\hat{\mathbf{z}}$ direction and was constructed from the Fourier series for a step function joined smoothly by portions of a sine function. The $\hat{\mathbf{y}}$ component of sheared magnetic field $B_{y}(z)$ also varies only in the $\hat{\mathbf{z}}$ direction and is constructed from two unit impulse functions multiplied by portions of a cosine function. Two magnetic shear layers result from the assumption of periodic boundary conditions. The Fourier coefficients for the components of the sheared magnetic field are (for $k_{x}=k_{y}=0$ ),

$$
\begin{align*}
B_{x}\left(k_{z}\right)= & \frac{i b_{c}}{\pi} \cos \left(a_{b} k_{z}\right)\left[1-(-1)^{k_{z}}\right] \\
& \times\left[\frac{4 a_{b}^{2} k_{z}}{\pi_{c}^{2}-4 a_{b}^{2} k_{z}^{2}}+\frac{1}{k_{z}}\right]  \tag{8}\\
B_{y}\left(k_{z}\right)= & \frac{2 a_{b} b_{c}}{\pi^{2}-4 a_{b}^{2} k_{z}^{2}} \cos a_{b} k_{z}\left[1-(-1)^{k_{z}}\right] \tag{9}
\end{align*}
$$

where $a_{b}$ is the width of the shear layer, $k_{z}$ is the $\hat{\mathbf{z}}$ component of the three-dimensional wave vector $\mathbf{k}$, which

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-05.jpg?height=678&width=842&top_left_y=203&top_left_x=132)
b

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-05.jpg?height=633&width=849&top_left_y=937&top_left_x=119)
Figure 2. Typical initial conditions of the simulations. (a) The cut in the $y-z$ plane through the simulation box shows the $x$ component of the velocity which changes sign across the two light-colored symmetrically located shear layers. The $x$ - $z$ plane shows the $x$ component of the magnetic field, with a current sheet (magnetic shear layer) at the midplane and at the bottom of the box. Beside the magnetic field plane are vectors showing the magnetic field and its fluctuations. The case show here has large-amplitude fluctuations added. (b) The components of $\mathbf{B}$ and $\mathbf{v}$ for a line along the $z$ direction for the initial conditions without the fluctuations added.

has integer components, $b_{c}$ is the magnitude of the magnetic field, and $\mathbf{B}(-\mathbf{k})=\mathbf{B}^{*}(\mathbf{k})$. The initial fields satisfy the constraint

$$
\begin{equation*}
B_{x}^{2}(z)+B_{y}^{2}(z)=b_{c}=\mathrm{constant} \tag{10}
\end{equation*}
$$

Thus the magnitude of the sheared magnetic field remains constant and the magnetic field rotates by $\pi$ as the current sheet is crossed. Figure 1 suggests that this is a reasonable approximation for the average current sheet, but it still ignores the striated structure in part of the slow wind region. Effects due to the striations have been studied separately [Roberts et al., 1996]. This
approximately models the Helios observations shown in Figure 1. The sheared velocity field has only an $\hat{\mathbf{x}}$ component $V_{x}(z)$, varies only in the $\hat{\mathbf{z}}$ direction, and is constructed from the Fourier series for an impulse function. The Fourier coefficients are real and given by

$$
\begin{equation*}
V_{x}\left(k_{z}\right)=\frac{v_{2}(-1)^{k_{z}}}{\pi k_{z}} \sin \left(a_{v} k_{z}\right)\left(1-\frac{v_{1}}{v_{2}}\right) \tag{11}
\end{equation*}
$$

where $a_{v}$ is the distance separating the two shear layers, and $v_{1}$ and $v_{2}$ are the high and low speeds. The width of the shear layers is determined by the number of Fourier coefficients used to represent them. With no loss of generality, $V_{x}(z)$ has zero mean value (i.e. the model is solved in the zero momentum frame).

There are only three parameters that define the shear fields if use is made of the constraints that the mean value of $V_{x}(z)$ equals zero and $B_{x}^{2}(z)+B_{y}^{2}(z)=b_{c}$ and if it is assumed that the total energy in the shear layer equals 1. These parameters are the widths of the velocity and magnetic field shears which are $a_{v}$ and $a_{b}$, respectively, and the ratio of the energy in the velocity shear jump to the magnitude of the magnetic field, namely

$$
\begin{equation*}
r=\frac{\left(v_{1}-v_{2}\right)^{2}}{b_{c}^{2}} \tag{12}
\end{equation*}
$$

From Figure 1, with the magnetic field converted to Alfvén speed units, one finds that $r \sim O(1)$ in the inner heliosphere and (based on higher resolution data) that $a_{v} / a_{b} \sim O(100)$. In constructing the initial condition shown in Figure 2, we assumed that $r=1.6$ and $a_{v} / a_{b} \approx 1.5$; most of the simulations discussed below used similar values for these parameters. While we have set $r$ to values close to those observed in the solar wind, the requirement that the shear layers be resolved adequately restricts this work to unphysically small values of $a_{v} / a_{b}$ ranging from 0.4 to 2.5 ; however, we believe that the principal results reported here are independent of this ratio. We show below that major results such as the destruction of velocity-magnetic field correlation and the enhancement of energy in the radial component of the perturbing velocity and magnetic fields are consequences only of the presence of velocity or magnetic shear, and thus the particular values of $a_{v} / a_{b}$ should not be critical. This issue is still open because the solar wind shears are very steep, and it is difficult to propagate the information of their existence into the bulk of the slow flow where the cross helicity decreases. We discuss this further below.

## 3. The Evolution of a Small Amplitude Perturbation

To motivate the following sections, we will begin by examining the evolution in time of a small (i.e. $\delta E / E=10^{-5}$, where $E$ is the total energy) amplitude circularly polarized Alfvénic perturbation to the sheared velocity and magnetic fields described in section
2.2. In particular, we are interested in examining the time histories of measures of the distribution of energy over both wave number space and the vector components of the fields; this provides information about the influence of magnetofluid instabilities on specific modes of the system.

Four measures of the distribution of the perturbation energy over wave number space are

$$
\begin{align*}
E_{3 D} & =\sum_{k_{x} \neq 0} \sum_{k_{y} \neq 0} \sum_{k_{z} \neq 0} E(\mathbf{k})  \tag{13}\\
E_{2 D x z} & =\sum_{k_{x}} \sum_{k_{z}} E\left(k_{x}, 0, k_{z}\right)  \tag{14}\\
E_{2 D y z} & =\sum_{k_{y}} \sum_{k_{z}} E\left(0, k_{y}, k_{z}\right)  \tag{15}\\
E_{2 D x y} & =\sum_{k_{x}} \sum_{k_{y}} E\left(k_{x}, k_{y}, 0\right) \tag{16}
\end{align*}
$$

where $E(\mathbf{k})$ is the total energy spectrum indexed by the three-dimensional wave vector $\mathbf{k}$. Note that the "twodimensional" energy is that in the coordinate planes, and that $E\left(0,0, k_{z}\right)$ that defines the structures is not included. The quantity $E_{3 D}$ represents the total energy in modes with three-dimensional wave vectors. Increases in this quantity with time signify the development of three-dimensional structure in the fluid and could indicate the growth of three-dimensional linear fluid instabilities generated by the sheared fields defined by (8)-(10). Development of two-dimensional structures in which there is only radial and latitudinal variation is measured by $E_{2 D x z}$; these will be susceptible to twodimensional fluid instabilities generated by the shear fields $B_{x}(z)$ and $V_{x}(z)$ defined by (8) and (10). (Alternatively, these are the structures one would obtain by averaging over the longitudinal variation.) Similarly, increases in $E_{2 D y z}$ will be susceptible to two-dimensional fluid instabilities generated by the shear field $B_{y}(z)$ defined by (9). Also, as will be shown in a following section, modes of the $\hat{\mathbf{x}}$ components of the perturbing fields which lie in the $k_{x}=0$ plane can experience a rapid growth that is brought about by the shears in $B_{x}(z)$ and $V_{x}(z)$. Finally, changes in the quantity $E_{2 D x y}$ indicate the development of structures that vary only parallel to the ecliptic plane.

In Figure 3a the time histories of the four quantities defined by (13)-(16) are given for a $32^{3}$ simulation in which the shear fields defined by (8)-(10) were perturbed by circularly polarized Alfvén waves which were isotropically distributed over wave number with a power spectrum proportional to $k^{-3}$. The ratio of the perturbation energy to the total energy in the system is $\delta E / E=10^{-5}$ and the kinetic and magnetic Reynolds numbers (taken simply as the inverses of dimensionless dissipation coefficients) were both 100 . Most notable in this plot is that quite quickly the initial isotropic distribution of the system becomes dominated by energy in the two-dimensional structures which have wave num-

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-06.jpg?height=1186&width=858&top_left_y=197&top_left_x=1024)
Figure 3. (a) Time histories of measures of two- and three-dimensional modes (see equations. (13)-(16)) for a small-amplitude, isotropic perturbation of the initial shear conditions. (b) Time histories of the total energy in the components of the magnetic field for the same run as in Figure 3(a).

bers that lie in $\left(k_{x}, 0, k_{z}\right)$ and $\left(0, k_{y}, k_{z}\right)$ planes. There is no significant change in the three-dimensional energy or the energy in the ( $k_{x}, k_{y}, 0$ ) plane.

It is also interesting to examine the evolution of the total energy in the individual vector components of the perturbing field. In Figure 3b, in which $E_{i}$ is the total energy in the $i^{\text {th }}$ component of the magnetic field, one sees that from the initial isotropic state the system quickly evolves to a state in which the $\hat{\mathbf{x}}$ component of the perturbing field dominates the system energetically. Note that this is not due to compressive interactions, as we are solving the incompressible equations. This implies that if the incompressible model is vaild as a low-order description of the solar wind flucuations, then variances along the magnetic field and the associated variations in the magnitude of the field are not good indicators of an essential role for compressive dynamics, as is often held.

From Figure 3a we know that the majority of the system's energy lies in the $\left(0, k_{y}, k_{z}\right)$ and $\left(k_{x}, 0, k_{z}\right)$ planes. Figure 4 shows the time histories of the total energy in

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-07.jpg?height=1253&width=841&top_left_y=195&top_left_x=111)
Figure 4. Time histories of the energy in the components of the magnetic field for the same case as in Figure 3, for fluctuations in (a) the $k_{y}=0$ plane and (b) the $k_{x}=0$ plane.

the individual vector components for these two planes in wave number space. In Figure 4a we see that for the ( $k_{x}, 0, k_{z}$ ) plane (i.e. the plane in which structures vary radially and latitudinally) the $\hat{\mathbf{x}}$ component also dominates the system energetically, but there is also a noticeable growth of the $\hat{\mathbf{z}}$ component. In section 4 we will show that growth of energy in this plane arises from linear magnetofluid instabilities generated by the velocity and magnetic shears defined by (8) and (10). Also, one sees from Figure 4 b that in the $\left(0, k_{y}, k_{z}\right)$ plane (i.e. the plane in which structures vary only longitudinally and latitudinally) the system is energetically dominated by the $\hat{\mathbf{x}}$ component. In the following section it will be shown that the growth of energy in this plane arises from a different set of linear equations.

The results presented here suggest that linear fluid instabilities can lead to the development of significant anisotropies in the distribution of energy over both wave number and vector components. In following sections we will show that linear fluid instabilities can destroy velocity-magnetic field correlation. We will begin in section 4 by examining the solutions of the equations
obtained by linearizing (1)-(4) about the velocity and magnetic fields defined by (8)-(10).

## 4. Linear Theory

### 4.1. The MHD Orr-Sommerfeld Equations

It is well known that magnetic field shear is subject to growth of the tearing mode instability in resistive MHD [Furth et al., 1963]. Also, the velocity profile given by (10) is susceptible to the magnetic Kelvin-Helmholtz instability [Chandrasekhar, 1961]. Numerical investigations of MHD flows in which magnetic and velocity shear fields similar to those given by (8) and (10) coexist have also been carried out [Einaudi and Rubini, 1986, 1989; Ofman et al., 1991; Wang et al., 1988]. In the context of the Earth's magnetotail, Hesse and Birn [1990] studied the influence of a transverse magnetic field on a sheared magnetic field. Here we give a brief overview of the linear evolution of the perturbations defined by (8)-(10).

If (1)-(4) are linearized about velocity and magnetic fields given by

$$
\begin{align*}
\mathbf{B}(z) & =B_{x}(z) \hat{\mathbf{x}}+B_{y}(z) \hat{\mathbf{y}}  \tag{17}\\
\mathbf{V}(z) & =V_{x}(z) \hat{\mathbf{x}} \tag{18}
\end{align*}
$$

and perturbing velocity and magnetic fields are assumed to be of the form

$$
\begin{align*}
& \mathbf{b}^{\prime}(\mathbf{x}, t)=\hat{\mathbf{b}}(z) e^{i(\alpha x+\beta y+\omega t)}  \tag{19}\\
& \mathbf{v}^{\prime}(\mathbf{x}, t)=\hat{\mathbf{v}}(z) e^{i(\alpha x+\beta y+\omega t)} \tag{20}
\end{align*}
$$

one obtains the MHD Orr-Sommerfeld equations [Dahlbur et al., 1992], namely,

$$
\begin{align*}
\omega\left(k_{\perp}^{2}-D^{2}\right) \hat{v}_{z}= & \alpha V_{x}\left(k_{\perp}^{2}-D^{2}\right) \hat{v}_{z}  \tag{21}\\
& +i \nu\left(k_{\perp}^{2}-D^{2}\right)^{2} \hat{v}_{z} \\
& -\alpha \hat{v}_{z} D^{2} V_{x} \\
& +\left(\mathbf{k}_{\perp} \cdot \mathbf{B}\right)\left(k_{\perp}^{2}-D^{2}\right) \hat{b}_{z} \\
& +\hat{b}_{z} D^{2}\left(\mathbf{k}_{\perp} \cdot \mathbf{B}\right) \\
\omega \hat{b}_{z}= & \left(\mathbf{k}_{\perp} \cdot \mathbf{B}\right) \hat{v}_{z}  \tag{22}\\
& -\left[\alpha V_{x}-i \eta\left(k_{\perp}^{2}-D^{2}\right)\right] \hat{b}_{z}
\end{align*}
$$

The resistivity and viscosity are given by $\eta$ and $\nu$ respectively, $D^{n}=d^{n} / d z^{n}$ and $\mathbf{k}_{\perp}=\alpha \hat{\mathbf{x}}+\beta \hat{\mathbf{y}}$. We assume that $\alpha$ and $\beta$ are integers.
It is interesting to note that the modes for which $\beta=0$ (i.e. the two-dimensional modes which lie in the $k_{x}, k_{z}$ plane that include "slab" Alfvén waves and the modes of the Roberts et al. [1991, 1992] simulations) are influenced only by the $B_{x}(z)$ and $V_{x}(z)$ shear fields and the modes with $\alpha=0$ (i.e. the "two-dimensional turbulence" modes which lie in the $k_{y}, k_{z}$ plane) are only affected by the $B_{y}(z)$ shear field. Only modes with three-dimensional wave vectors are affected by all three shear fields. In the following it will be shown that for the
shear fields defined by (8)-(10) the fastest growing unstable modes are two-dimensional and lie in the $\beta=0$ plane for some values of the parameters $r$ (see equation (12)) $a_{v}$, and $a_{b}$ (see equations (8)-(10)), while for others the fastest growing unstable modes can be threedimensional. The exact parameter dependence depends upon the profiles assumed for the sheared fields and possibly the boundary conditions, but we expect threedimensional modes to be dominant under a variety of conditions.

We solved (21) and (22) with periodic boundary conditions to facilitate comparison with simulations of (1)(4). We also only solved (21) and (22) for values of the viscosity and resistivity that we can accurately simulate, and we take the viscosity equal to the resistivity in dimensionless units. If $\hat{v}_{z}(z, t)$ and $\hat{b}_{z}(z, t)$ are assumed to be given by Fourier series, and (8)-(10) are used for $V_{x}$ and $\mathbf{B}$, then (17) and (18) yield a system of linear equations. In this section solutions of this system of equations are discussed for various values of the parameters that define the velocity and magnetic shears in (8)-(10). We will compare these solutions with ones obtained by numerical time integration of (1)-(4).

The low resolution assumed in the numerical solution of (21) and (22) prohibited a satisfactory scan of the parameters $a_{v}$ and $a_{b}$ in the determination of exactly under what conditions this transition between two- and three-dimensional instability occurs, but we were able to determine general regions in the phase space of the parameters. In Table 1 four values of $a_{v} / a_{b}, r$ (equation (12)), and $\gamma$ (the growth rate for the fastest growing mode, the negative imaginary part of $\omega$ in (21) and (22) expressed in units of eddy turnover time) are given for two modes at approximately the values for the transition. Both $\nu$ and $\eta$ were assumed to be 0.01 and 32 terms were kept in the Fourier series representing the fields. In Table 1, for each given value of $a_{v} / a_{b}$, if $r$ is larger than the value given in the second column then the fastest growing mode is two-dimensional, and if $r$ is smaller, the fastest growing mode is threedimensional. Our survey suggests that in general for very large values of $r$, when the system is dominated by the two-dimensional velocity shear, the fastest growing unstable mode is two dimensional. This is expected because in this limit Kelvin-Helmholtz type instabilities should develop, and for this type of flow Squire's theorem [Squire, 1933] states that the fastest growing modes are two dimensional. For very small values of $r$, when the system is dominated by the rotating magnetic shear,

Table 1. Shear Parameters and Growth Rate
| $a_{v} / a_{b}$ | $r$ | $\gamma$ |
| :---: | :---: | :---: |
| 2.0 | 2.0 | 0.275 |
| 1.5 | 2.5 | 0.325 |
| 1.0 | 1.7 | 0.38 |
| 0.5 | 0.5 | 0.28 |


![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-08.jpg?height=617&width=836&top_left_y=189&top_left_x=1040)
Figure 5. Time history of the energy in the magnetic field components for an initial perturbation in the $k_{x}=$ 0 plane. Note that $E_{x}=0$.

the fastest growing unstable mode appears to be three dimensional.

The numerical survey suggests that the fastest growing mode changes from a two-dimensional structure to a three-dimensional structure when the system is energetically dominated by the magnetic shear field. Here we give more details on this transition by examining both solutions to (21) and (22) and numerical simulations of (1)-(4) in the parameter regime $r \ll 1$. We begin with a discussion of the stability of two-dimensional perturbations. First, consider the evolution of the twodimensional modes for which $\beta=0$ and that therefore lie in the $\left(k_{x}, 0, k_{z}\right)$ plane. When $r \ll 1$ the only shear field profile appearing in (21) and (22) is the $B_{x}(z)$ profile defined by (8). Thus these modes are prone to development of the well-studied tearing mode instability [Furth et al., 1963]. A detailed numerical analysis of this instability in both two and three dimensions with both viscosity and resistivity is given in Dahlburg et al. [1983, 1992]. Though our boundary conditions differ from theirs (i.e. periodic as opposed to unbounded), our results are qualitatively the same: a parameter regime exists in which the growth rate increases with increasing resistivity [Furth et al., 1963], but decreases with increasing viscosity. Also, we find the same parity as they do for the velocity and magnetic eigenmodes (odd and even, respectively); see Dahlburg et al. [1983; 1992] for a more complete discussion. The modes which lie in the $\alpha=0$ plane will be affected only by the $B_{y}(z)$ profile defined by (9) for all values of $r$. These modes will lie in the ( $0, k_{y}, k_{z}$ ) plane. To our knowledge, the stability of this equilibrium magnetic field profile to perturbations has not been investigated. Numerically we find that it is stable for values of $\eta$ and $\nu$ as small as 0.001 . We tested this with a simulation in which $B_{y}(z)$ receives an isotropic two-dimensional perturbation with wave numbers lying in the ( $0, k_{y}, k_{z}$ ) plane. This simulation had $32^{3}$ modes and $\eta=\nu=0.01$. Figure 5 shows the time
history of the total energy in each component. For this two-dimensional perturbation there is no energy in the $x$ component ( $E_{x}=0$ ) and the other components decay, verifying the linear theory prediction of stability.

From the previous discussion it is known that under some conditions the fastest growing unstable mode can be three dimensional. To develop a more detailed picture of the influence of each of the magnetic field shears on the stability of three-dimensional perturbations we will relax the constraint that $B_{x}^{2}(z)+B_{y}^{2}(z)=$ constant and define the parameter

$$
\begin{equation*}
r_{b}=\frac{b_{y c}^{2}}{b_{x c}^{2}} \tag{23}
\end{equation*}
$$

where $b_{x c}$ and $b_{y c}$ are parameters which determine the amplitudes of $B_{x}(z)$ and $B_{y}(z)$, respectively. In Table 2 the growth rate of the fastest growing unstable mode with $\alpha=1$ and $\beta=1$ is given for values of $r_{b}$ ranging over 8 orders of magnitude. In this parameter scan, 32 terms were retained in the representation of the fields, $\eta=\nu=0.01$, and $r=10^{-7}$. For the first row of Table 2, $r_{b}=10^{-4}$ and for this three-dimensional mode $\gamma=0.166$. For this value of $r_{b}$, however, the system is energetically dominated by the $B_{x}(z)$ shear and the fastest growing mode is two dimensional ( $\alpha=1$ and $\beta=0$ ), with a growth rate $\gamma=0.276$. Note that for $r_{b}$ near zero, $\gamma$ approaches 0.166. As $r_{b}$ increases, $\gamma$ also increases, reaching a maximum at $r_{b}=10$. At $r_{b}=1$, the three-dimensional modes see an equal admixture of $B_{x}(z)$ and $B_{y}(z)$, and this $\alpha=1$ and $\beta=1$ mode is the fastest growing one in the system. When $r_{b}$ takes on values greater than 10 , the $B_{y}(z)$ shear begins to dominate the system and $\gamma$ begins to decrease. For $r_{b}=10$ the fastest growing two-dimensional mode has a growth rate of $\gamma=0.188$. The system eventually stabilizes for large values of $r_{b}$. For values of $r_{b}$ greater than 1 , the fastest growing mode is three dimensional until $r_{b}$ is large enough to stabilize the system. Thus we see that for both large and small limits, the growth rate of this three-dimensional mode asymptotes to the values characteristic of either $B_{x}(z)$ or $B_{y}(z)$ magnetic shears.

The rapidly growing two-dimensional modes for large $r$ lie in the ( $k_{x}, 0, k_{z}$ ) plane and are influenced only by the $V_{x}(z)$ and $B_{x}(z)$ shears defined by (8) and (10), re-

Table 2. Change in $\gamma$ With $r_{b}$ for a Three-Dimensional Mode
| $r_{b}$ | $\gamma$ |
| :---: | :---: |
| $10^{-4}$ | 0.166 |
| 0.01 | 0.167 |
| 0.1 | 0.184 |
| 1.0 | 0.28 |
| 10.0 | 0.362 |
| 100.0 | 0.125 |
| $10^{4}$ | stable |


![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-09.jpg?height=1389&width=847&top_left_y=197&top_left_x=986)
Figure 6. A two-dimensional eigenmode of the OrrSommerfeld equations. (a) Contours of $V_{z}$ in the $x-z$ plane. (b) Contours of $b_{z}$ in the $x-z$ plane.

spectively. Previous numerical work in which velocity and magnetic shears were simultaneously present [Einaudi and Rubini, 1986, 1989; Ofman et al., 1991; Wang et al., 1988] focused on a velocity shear of the form $\operatorname{sech}(z)$ and a magnetic shear of the form $\tanh (z)$. These shears are qualitatively similar to those studied in this work, and thus we find results in qualitative agreement with those discussed previously. The most relevant results from this work concern the influence of velocity shear on the growth of tearing modes. Numerically Einaudi and Rubini [1989] find that for $r^{2 / 3} a_{b} / a_{v}>1$ a resistive Kelvin-Helmholtz instability appears, as opposed to a tearing mode. For $r^{2 / 3} a_{b} / a_{v}<1$ a tearing mode grows with a growth rate that increases as the resistivity decreases. See Einaudi and Rubini [1986, 1989], Ofman et al. [1991], and Wang et al. [1988] for a more detailed discussion.

Examples of two- and three-dimensional eigenmodes are given in Figures 6 and 7, respectively. Notice that

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-10.jpg?height=1383&width=855&top_left_y=187&top_left_x=154)
Figure 7. Cuts in the $x-z$ plane of a three-dimensional eigenmode of the Orr-Sommerfeld equations. (a) Contours of $V_{z}$. (b) Contours of $b_{z}$.

the velocity and magnetic eigenmodes have odd and even parity respectively. In Figure 6 the contour plot of a two-dimensional eigenmode is given for the parameters $r=7, a_{v} / a_{b}=1.5, \nu=\eta=0.01, \alpha=1$ and $\beta=0$. The growth rate for this mode is $\gamma=0.42$. A slice through a three-dimensional eigenmode is shown in Figure 7. For this eigenmode $r=1, a_{v} / a_{b}=1.5$, $\nu=\eta=0.01, \alpha=1$, and $\beta=1$. The growth rate for this mode is $\gamma=0.28$.

The material presented in this section can be summarized as follows. As the value of the ratio of the shear kinetic energy to the magnetic energy, denoted by $r$ in (12), and the ratio of the kinetic to magnetic shear width, given by $a_{v} / a_{b}$, are varied, the dimensionality of the fastest growing unstable mode changes from two to three. For large values of $r$, when the system approaches the well studied Kelvin-Helmholtz instability, the fastest growing mode is two dimensional. For small values of $r$, when the system is dominated by the threedimensional magnetic shear, the fastest growing mode
is three dimensional. An indication of how the dimensionality of the unstable mode varies with these parameters can be seen in Table 1. It is shown that the shear field $B_{y}(z)$, defined by(9), is stable to small amplitude perturbations for values of $\eta$ and $\nu$ as small as 0.001 . Finally the growth rate of the fastest growing threedimensional mode was examined as ratio of the amplitudes of the $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ components of the magnetic shear fields, denoted by $r_{b}$ in (23), was varied. It was found that as $r_{b} \rightarrow 0$, the growth rate of the fastest growing three-dimensional mode asymptotes to a nonzero value. For the system studied here, that value was 0.166 . The maximum growth rate for a three-dimensional mode is obtained for a value of $r_{b}$ near 10 for the system described here and for large values of $r_{b}$ the system stabilizes.

### 4.2 A Linear Instability for Perturbed Fields Parallel to $\mathrm{B}_{0}$

In section 3 we showed that for a small-amplitude isotropic perturbation to the shear fields defined by (8)(10) there was substantial growth of the perturbation energy in the Fourier modes which lie in the $\left(0, k_{y}, k_{z}\right)$ plane (see Figures 3 and 4). However, in section 4 we showed that the MHD Orr-Sommerfeld equations (i.e. (21) and (22)) are stable to perturbations which lie in this $(\alpha=0)$ plane, but the equations given there only described eigenmodes with transverse perturbations. Figure 4 b , which gives the time histories of the energy in the vector components of the perturbation energy for modes which lie in the ( $0, k_{y}, k_{z}$ ) plane, shows that the $\hat{\mathbf{y}}$ and $\hat{\mathbf{z}}$ components of the perturbing velocity and magnetic fields experience no explosive growth, which verifies the analysis performed above. Instead, the $\hat{\mathbf{x}}$ component of the perturbing fields grows in time. To describe instabilities in longitudinal fluctuations analytically, it is useful to use a slightly different approximation from that used above. For simplicity, we assume that the $y$ component of the sheared magnetic field is zero, which is a case that yields decay for the transverse components in the above analysis. This section develops the linear theory based on this assumption.

Consider a two-and-a-half-dimensional MHD model in which the fields vary only with the variables $y$ and $z$. If this model is linearized about velocity and magnetic fields denoted by $B_{x}(z)$ and $V_{x}(z)$ one obtains from (1)(4) for the evolution of the perturbing fields

$$
\begin{align*}
\frac{\partial b_{x}}{\partial t} & =b_{z} \frac{d V_{x}}{d z}-v_{z} \frac{d B_{x}}{d z}+\eta \nabla^{2} b_{x}  \tag{24}\\
\frac{\partial v_{x}}{\partial t} & =b_{z} \frac{d B_{x}}{d z}-v_{z} \frac{d V_{x}}{d z}+\nu \nabla^{2} v_{x}  \tag{25}\\
\frac{\partial b_{y}}{\partial t} & =\eta \nabla^{2} b_{y}  \tag{26}\\
\frac{\partial v_{y}}{\partial t} & =\nu \nabla^{2} v_{y}  \tag{27}\\
\frac{\partial b_{z}}{\partial t} & =\eta \nabla^{2} b_{z} \tag{28}
\end{align*}
$$

$$
\begin{equation*}
\frac{\partial v_{z}}{\partial t}=\nu \nabla^{2} v_{z} \tag{29}
\end{equation*}
$$

If all fields are assumed to be periodic, this system of equations can be solved easily.

The $\hat{\mathbf{y}}$ and $\hat{\mathbf{z}}$ components of the velocity and magnetic fields will exponentially decay in time. At wave number $k$ the solution for the $\hat{\mathbf{z}}$ component will be of the form,

$$
\begin{equation*}
b_{z}(k, t)=b_{z}(k, 0) e^{-\eta k^{2} t} \tag{30}
\end{equation*}
$$

where $b_{z}(k, 0)$ is the initial value of $b_{z}(k)$ and $\eta$ is the resistivity. The solutions for $b_{y}(k), v_{y}(k)$ and $v_{z}(k)$ have a similar form. The solutions for $b_{x}(k)$ and $v_{x}(k)$ are also easily found. For simplicity we will assume that $\eta=\nu$. Substituting the expressions for $v_{z}(\mathbf{k}, t)$ and $b_{z}(\mathbf{k}, t)$ into (24) gives

$$
\begin{align*}
b_{x}(\mathbf{k}, t)= & b_{x}(\mathbf{k}, 0)+e^{-\eta k^{2} t}  \tag{31}\\
& \times \sum_{l+m=k_{z}} \frac{e^{\eta\left(2 k_{z} m-m^{2}\right) t}-1}{\eta\left(2 k_{z} m-m^{2}\right)} \\
& \times i\left[b_{z 0}\left(0, k_{y}, l\right) V_{x}(m)\right. \\
& \left.-m v_{z 0}\left(0, k_{y}, l\right) B_{x}(m)\right]
\end{align*}
$$

where $b_{z 0}$ and $v_{z 0}$ are the initial values of the $\hat{\mathbf{z}}$ components of the velocity and magnetic fields, respectively, and it is assumed that $2 k_{z} \neq m$. If $2 k_{z} \rightarrow m$, we have

$$
\begin{align*}
b_{x}(\mathbf{k}, t)= & b_{x}(\mathbf{k}, 0)  \tag{32}\\
& +i\left[b_{z 0}\left(0, k_{y},-k_{z}\right) V_{x}\left(2 k_{z}\right)\right. \\
& \left.-v_{z 0}\left(0, k_{y},-k_{z}\right) B_{x}\left(2 k_{z}\right)\right] t e^{-\eta k^{2} t}
\end{align*}
$$

The expression for $v_{x}(\mathbf{k}, t)$ can be obtained by interchanging $V_{x}(m)$ and $B_{x}(m)$ in (31). In Figure 8 the square of $b_{x}$ given by (31) is plotted for the $V_{x}(m)$ and $B_{x}(m)$ shown in Figure 2. These shear fields are perturbed by circularly polarized Alfvén waves. We also

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-11.jpg?height=630&width=838&top_left_y=1834&top_left_x=111)
Figure 8. The square of $b_{x}$ given by (31) for the $V_{x}(m)$ and $B_{x}(m)$ shown in Figure 2.

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-11.jpg?height=632&width=844&top_left_y=211&top_left_x=983)
Figure 9. A comparison between the time histories of $\sum_{\mathbf{k}}\left|b_{x}(\mathbf{k})\right|$ according to (33) and a $32^{3}$ ideal simulation (asterisks).

take $\eta=0.01$. For Alfvénic perturbations the growth curves for $b_{x}$ and $v_{x}$ will be identical.

It is interesting to examine (31) in the ideal limit $\eta \rightarrow 0$. In this limit the solution greatly simplifies to linear growth for all modes. One obtains

$$
\begin{align*}
b_{x}(\mathbf{k}, t)= & b_{x}(\mathbf{k}, 0)  \tag{33}\\
& +i \sum_{l+m=k_{z}}\left[b_{z 0}\left(0, k_{y}, l\right) V_{x}(m)\right. \\
& \left.-v_{z 0}\left(0, k_{y}, l\right) B_{x}(m)\right] t
\end{align*}
$$

A comparison between (33) and a $32^{3}$ ideal simulation is shown in Figure 9. To reproduce the linear calculations, the initial conditions for the run are Alfvénic fluctuations isotropically distributed in the ( $0, k_{y}, k_{z}$ ) plane, and with no $B_{y}$ shear. In the figure the time histories of $\sum_{\mathbf{k}}\left|b_{x}(\mathbf{k})\right|$ are shown. One sees that at early times the simulation and theory agree very well. At later times the linear growth begins to saturate in the simulation and the two curves diverge.

In a later section we will show that the energy generated in the $\hat{\mathbf{x}}$ component of the perturbing field is concentrated in the velocity and magnetic shear layers. Sufficient energy is generated by this process to cause alignment between the perturbing fields and the shear fields in the shear layers. It is also interesting to note that in (31) there is no coupling between the velocity and magnetic shears. Thus it is not necessary that both be present in the flow for this phenomenon to occur. As a final remark, one expects to see $b_{y}$ and $v_{y}$ grow in the $\left(k_{x}, 0, k_{z}\right)$ plane because of a similar interaction between the perturbing fields and the $B_{y}(z)$ shear. However, we do not see this for the $B_{y}(z)$ defined by (9). It is possible that the gradients in the shear layer for this choice of $B_{y}(z)$ are not of sufficient magnitude to produce a noticeable effect.

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-12.jpg?height=1421&width=695&top_left_y=200&top_left_x=189)
Figure 11. Contour plots of an initially Alfvénic perturbation showing the correlation of the (a) $V_{z}$ and (b) $B_{z}$ components.

of Fourier modes that lie along $k_{z}$ with $k_{x}=1$ and $k_{y}=0$ and $\delta E / E=10^{-5}$. (The particular choice of two-dimensional modes was made arbitrarily, but agreement with the analytical results in this case increases our confidence that the results would be the same for other cases.) Also, the viscosity and resistivity are given by $\nu=\eta=0.01$. The magnetic and velocity shear profiles are shown in Figure 12 at $t=0.5$ eddy turnover times. The initial parametrizations of these fields are $r=7.8$ and $a_{v} / a_{b}=1.5$. For these parameters the fastest growing mode is two dimensional with $\alpha=1$ and $\beta=0$ (see (21) and (22)) and has a growth rate $\gamma=0.35$ reciprocal eddy-turnover-times. In Figure 13 the time history of the averaged modal kinetic and magnetic energy are compared with the linear theory predictions. One sees that the simulation follows the linear theory prediction quite closely for the entire simulation. Profiles of the velocity-magnetic field correlation coefficient

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-12.jpg?height=633&width=855&top_left_y=200&top_left_x=986)
Figure 12. The magnetic and velocity shear profiles at $t=0.5$ eddy turnover times for the case shown in Figure 11.

$\sigma_{c}$ averaged over the $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$ directions for three different times (i.e. $t=0.0,0.2$ and 0.4 eddy turnover times) are plotted in Figure 14. During this period of linear evolution one sees that quite rapidly $\sigma_{c}$ decreases from the initial value of 1 in the regions of velocity and magnetic shear about $z=\pi$ and at the other magnetic shear that extends through the periodic boundary (compare with the magnetic and velocity field profiles shown in Figure 12). In the regions outside the shear layer the flow remains highly Alfvénic. This structure in the $\sigma_{c}$ profile is qualitatively similar to the Helios data shown in Figure 1 and the simulation results of Roberts et al. [1991, 1992].

A similar experiment was performed using a threedimensional Alfvénic perturbation in the Fourier modes which lie along $k_{z}$ with $k_{x}=1$ and $k_{y}=1$ and $\delta E / E=10^{-5}$. In this simulation $32^{3}$ Fourier coefficients were retained in the representations of the fields and $\eta=\nu=0.01$. The profiles of the velocity and magnetic shears at $t=0.5$ turnover times are shown

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-12.jpg?height=535&width=843&top_left_y=1951&top_left_x=992)
Figure 13. The time history of the averaged modal kinetic and magnetic energy are compared with the linear theory predictions for the case shown in Figure 11.

will be destroyed. The destruction of Alfvénicity in the shear layer will allow a turbulent cascade to develop rapidly, since the rate of turbulent spectral transfer is faster for nonAlfvénic flows than for Alfvénic ones [Dobrowolny et al., 1980; Grappin et al., 1982; Matthaeus et al., 1984; Matthaeus and Zhou, 1989], at least for incompressible turbulence. The presence of well-developed turbulent spectra in the regions near the current and velocity shear layers may be due to this, as discussed by Roberts et al. [1991]; we plan to extend their spectral studies to three dimensions in future simulations, but we expect the results to be similar. It may be that the regions of low cross helicity and well-developed spectra in the solar wind would need to have been sheared by many small "microstreams" for this scenario to work, as will be discussed in the final section.

### 5.3 Parallel Energy Enhancement in Linear Simulations

In the previous section we showed that for small amplitude perturbations a two-and-a-half-dimensional fluid instability leads to growth in the component of the perturbing field parallel to the shear fields $(\hat{\mathbf{x}})$, corresponding to the radial component in the inner heliosphere. Here we show that for the two-and-a-halfdimensional instability discussed in the previous section, the growth in perturbation energy parallel to the velocity and magnetic shear fields is concentrated in the shear layers.

First, consider the small-amplitude simulations discussed in section 3. (The large amplitude case will be discussed in the next section.) There the velocity and magnetic shears defined by (8)-(10) were perturbed with both two- and three-dimensional fields which were the solutions of the eigenvalue problem defined by (21) and (22). In Figure 17 the profile of the ratio of the magnetic energy in the $\hat{\mathbf{x}}$ component averaged over $x$ and $y$ directions to total magnetic energy similarly averaged

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-13.jpg?height=551&width=841&top_left_y=1867&top_left_x=130)
Figure 17. The ratio of the magnetic energy in the $\hat{\mathbf{x}}$ component averaged over $\hat{\mathbf{y}}$ and $\hat{\mathbf{z}}$ directions to total magnetic energy similarly averaged for the two dimensional eigenmode perturbation of section 3 after 1 eddy turnover time (see Figures 6 and 10a).

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-13.jpg?height=543&width=838&top_left_y=200&top_left_x=1000)
Figure 18. The same as Figure 17, but for the threedimensional eigenmode (also see section 4 and Figures 7 and 10).

( $E_{b x} / E_{b}$ ), is given for the two-dimensional eigenmode perturbation after one eddy-turnover-time (see Figures 6 and 10a). Also in Figure 17 a similar plot is given for the perturbing kinetic energy ( $E_{v x} / E_{v}$ ). One sees enhancements in the $\hat{\mathbf{x}}$ energy for both the velocity and magnetic fields. For the magnetic field, energy in $\hat{\mathbf{x}}$ dominates nearly uniformly across the box, with the exception of the points on the lines of symmetry of the shear layers at which there is no $\hat{\mathbf{x}}$ energy. Enhancements in the $\hat{\mathbf{x}}$ kinetic energy are also present. Moreover, at the shear layers the $\hat{\mathbf{x}}$ kinetic energy contains most of the energy in the perturbation (compare Figures 12 and 17). This is in contrast to these ratios for perturbations with the three-dimensional eigenmode shown in Figure 18 (also see section 4 and Figures 7 and 10). For this simulation, at nearly every point the energy ratio is near the line indicating an isotropic distribution over the vector components for both the velocity and magnetic fields with the exception of the points on the line of symmetry of the shear layers for the magnetic energy ratio (compare Figures 15 and 18). There the $\hat{\mathbf{x}}$ magnetic energy dominates the other components.

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-13.jpg?height=543&width=839&top_left_y=1932&top_left_x=1002)
Figure 19. The ratios $E_{b x} / E_{b}$ and $E_{v x} / E_{v}$ for the simulation of the two-and-a-half-dimensional longitudinal instability discussed in section 4.2.

For the simulation of the two-and-a-half-dimensional shear instability discussed in section 4.2, we also investigated the energy ratios $E_{b x} / E_{b}$ and $E_{v x} / E_{v}$; the results are plotted in Figure 19. We see that the energy in the $\hat{\mathbf{x}}$ components of the velocity generated by the instability is concentrated in the shear layers (compare Figures 2 and 19). For both the velocity and magnetic fields in the shear layers, the ratios are above the line indicating isotropy. Also, the structure of both profiles is very similar. This is in contrast to the simulations discussed in the previous paragraph.

Figure 1 (lower panels) includes time series of the ratio of fluctuating energy in the radial component to total fluctuating energy for both the velocity and magnetic fields computed using fluctuations about 3 -hour running averages of the hour-averaged data. The horizontal line passing through the value of $1 / 3$ for the ratios in the plots corresponds to an isotropic distribution of fluctuating energy over the vector components of the fields. Values of the ratio above this line indicate a preponderance of fluctuating energy in the radial components of the fields (the mean field is essentially radial for this case), and values below the line indicate a preponderance of fluctuating energy in the transverse plane. The region of shear layers in the data set lies approximately between 120 and 270 hours; there is a clear enhancement of radial power for the fluctuating fields in this interval, and especially near the strong shear near hour 260. Outside this interval, the power ratio lies for the most part below the line indicating a minimum variance along the field, as is common in Alfvénic intervals. Moreover, in the interval from 200 to 300 hours the radial power enhancements are quite strong and $\sigma_{c}$ is generally smaller. This suggests that both phenomena may be the result of shear driven processes.

## 6. Evolution of a Large-Amplitude Perturbation

Because the low resolution of our model results in a rapid decay of energy, we were unable to follow linear perturbations to nonlinear saturation and the development of turbulence. The highest resolution simulation we performed had $128^{3}$ grid points and mechanical and magnetic Reynolds numbers of 1000 . Even at this Reynolds number the energy decays relatively rapidly. Moreover, a $128^{3}$ model is computational demanding: a simulation of five eddy turnover times required 32 hours of CPU time on a Cray C90/16. To study the nonlinear turbulent evolution of our model, we perturbed the shear fields with large-amplitude (i.e. $\delta E / E=0.1$ ) isotropically distributed circularly polarized Alfvén waves. The results previously discussed for the small amplitude perturbations provide the leading order description of the evolution for larger amplitudes. Thus one anticipates seeing an impact of the lower-order processes on the system's dynamics. Here we will re-

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-14.jpg?height=622&width=847&top_left_y=200&top_left_x=1013)
Figure 20. Profiles of $\sigma_{c}$ for three different times ( $t=0.0,0.75$, and 1.50) for the large-amplitude, highresolution simulation.

view the results of a $128^{3}$ simulation within the context of the ideas previously developed in this work and by Roberts et al. [1991, 1992].

The shear field parameters (see (8)-(10)) for this $128^{3}$ simulation are $r=7$ and $a_{v} / a_{b}=2.5$. The region of velocity shear lies approximately between $z=2.3$ to 4.3 and the two magnetic shear layers have a width of 0.8 with one centered at $z=\pi$ and the other at $z=2 \pi$ (Figure 2a). Also, $\nu=\eta=0.001$, and the perturbation consists of circularly polarized Alfvén waves with $\delta E / E=0.1$. We begin by reviewing the evolution of the velocity-magnetic field correlation coefficient for the perturbing fields across the shear layers. In Figure 20 the profile of $\sigma_{c}$ is shown for three different times, $t=0.0,0.75$, and 1.50 . One sees that within the regions of velocity and magnetic shear $\sigma_{c}$ is depleted, whereas outside the shear layers the flow remains highly Alfvénic. This result is in qualitative agreement with the decrease of $\sigma_{c}$ due to the growth of linear instabilities as previously discussed. Comparison of Figures 20 and 1, shows qualitative agreement between the simulation and the Helios observations near 0.3 AU, namely, nominally "high-speed" steams consist predominately of outward propagating Alfvén waves and nominally "low-speed" streams contain equal mixtures of inward and outward propagating waves. We find deeper agreement by comparing the observations with a two-dimensional cut through the simulation box showing $\sigma_{c}$ (Figure 21); strongly striated behavior is seen in both cases. Averages and spectral analysis imply low Alfvénicity, but the detailed observations (and simulations) show that the decrease is not uniform. The three-dimensional simulations also agree with the twodimensional results by Roberts et al. [1991, 1992]. The similarity between the three- and two-dimensional results supports the idea that the processes leading to the destruction of velocity-magnetic field correlation may involve the growth of linearly unstable modes. Re-

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-15.jpg?height=844&width=879&top_left_y=192&top_left_x=86)
Figure 21. Cuts through the three-dimensional, largeamplitude simulation in the physical space. The $x-y$ plane shows the local Alfvénicity correlation ( $\sigma_{c}$ ) with the large scale shear modes removed. The $x-y$ plane shows the $x$-component of the velocity, showing "fluting" perpendicular to the flow.

call that we showed in section 4 that for the threedimensional system, the fastest growing unstable modes can be two dimensional, and in section 5, that growth of the two-dimensional eigenmodes destroyed velocitymagnetic field correlation in the shear layers.

Next we will consider the development of anisotropies in the distribution of energy for this simulation. The time histories of total energy in the individual vector components of the perturbing velocity and magnetic fields are shown in Figure 22. One sees that from the

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-15.jpg?height=628&width=844&top_left_y=1853&top_left_x=124)
Figure 22. The time histories of total energy in the individual vector components of the perturbing velocity and magnetic fields for the large-amplitude simulation.

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-15.jpg?height=548&width=846&top_left_y=184&top_left_x=992)
Figure 23. Profiles of both $E_{b x} / E_{b}$ and $E_{v x} / E_{v}$ are given for the large amplitude perturbation at $t=3.0$ eddy turnover times (compare with Figures 19, 18 and 20).

initial isotropic distribution the energy in the $\hat{\mathbf{x}}$ component in the perturbation eventually dominates the system. This is the same result seen in the evolution of the small-amplitude perturbation discussed in sections 3 and Figure 4. Just as in the small-amplitude simulations, we find that the $\hat{\mathbf{x}}$ energy dominates in the shear layers. This is illustrated in Figure 23 where the profile of both $E_{b x} / E_{b}$ and $E_{v x} / E_{v}$ are given for the large amplitude perturbation at $t=3.0$ eddy turnover times (see also Figures 18, 19, 18 and 20).

The distribution of energy in wave number space for the large amplitude simulation is shown in Figure 24. In this figure gray scale plots of the logarithm of the total energy spectra for the individual vector components are shown in the coordinate planes of Fourier space for $t=2.25$ eddy turnover times. (The "holes" along various axes in these plots result from $\nabla \cdot \mathbf{B}=0$.) All the components show anisotropies, each with different characteristics. In our investigations to date, we only have a simple explanation for the anisotropy in the energetically dominant $\hat{\mathrm{x}}$ component of the magnetic field. Figure 24a shows that its energy is concentrated in the region near the ( $0, k_{y}, k_{z}$ ) plane where the small amplitude simulations showed that the $\hat{\mathbf{x}}$ components of the perturbing velocity and magnetic fields were subject to growth by the two-and-a-half-dimensional instability discussed in section 4.2. For the $\hat{\mathbf{z}}$ component, one might expect the two dimensional shear driven instability, discussed in section 4.1, to lead to the accumulation of energy in the ( $k_{x}, 0, k_{z}$ ) plane, but this is not evident in this nonlinear stage of the evolution. The $\hat{\mathbf{y}}$ component distribution is relatively isotropic in the ( $0, k_{y}, k_{z}$ ) plane. This could be a result of the apparent dominance of dynamics in the ( $k_{x}, 0, k_{z}$ ) and ( $0, k_{y}, k_{z}$ ) planes, but we have no explanation for the enhanced power along the $\left(0,0, k_{z}\right)$ axis. Finally, Figure 24 d shows that if we were to have simply examined the trace of the spectral matrix, we might have concluded that the evolution was a simple generalization of the two-dimensional case

![](https://cdn.mathpix.com/cropped/2025_11_22_ae6f91c92cf53ffcdee6g-16.jpg?height=1432&width=1733&top_left_y=181&top_left_x=140)
Figure 24. The distribution of energy in wave number space for the large amplitude simulation. The log of the magnetic power in the coordinate planes of Fourier space is shown, monotonically decreasing from the origin, for the (a) $x$ component, (b) $y$ component, (c) $z$ component, and (d) and the trace of the spectral tensor.

[Shebalin et al, 1983] in which the mean magnetic field leads to a faster nonlinear transfer perpendicular to the field than parallel to it, but the rest of the figure shows that this is a great oversimplification of the situation.

## 7. Summary and Conclusions

This paper presents a first attempt to construct a fully three-dimensional simulation of the inner heliosphereic current sheet region, including stream shear layers. We have examined the three-dimensional instabilities associated with such sheared conditions and related the results to observations. One major result is that the accelerated decay of cross helicity near the current sheet found in two dimensions occurs in a very similar way in three dimensions, and that this decay is, at least, in part a natural result of the linear instability
of the sheared configuration. The agreement with the two-dimensional simulations is important because it is only in three dimensions that the proper geometric relationship between the local mean magnetic field and the shear layers can be obtained. We also note that the anisotropies found here in $k$ space are qualitatively similar to those found in two dimensions, although in here we can examine many more possibilities than in the two-dimensional case.

This work also emphasizes that strong magnetic field fluctuations along the mean field do not necessarily indicate a causal role for compressibility; shear can give rise to such variations, in rough qualitative agreement with observations. The simulations here use incompressible MHD, and thus no density fluctuations are present. Nonetheless, variations in the magnitude of the magnetic field occur, implicitly matched by varia-
tions in pressure, and there are associated variations of the field along the mean field direction.

The present work sheds some light on a question that has been raised on numerous occasions (especially by J . Hollweg, private communications, 1987-1995), namely to what extent the evolution in cross helicity represents a nonlinear interaction as opposed to a linear interaction in a nonuniform background. The answer is partly one of point of view. In the simulations presented here, the "nonuniform background" is nothing more than the coherent superposition of particular modes, and thus all interactions leading to evolution of the Alfvénic population are nonlinear. However, on short timescales, on which the modes describing the shear fields are relatively unchanged, we can use the linearized descriptions presented here to show that two- and three-dimensional instabilities of the fluid due to inhomogeneities are important to the dynamics and lead to such observed phenomena as an anisotropic variance and decreasing cross helicity. Thus both viewpoints are useful. Ultimately, the waves react back on the flow and interact with each other, and these processes are fully nonlinear, but important aspects of the evolution may be understood from the linear standpoint. A related issue is that of whether the interactions are local or nonlocal in wave number [see Grappin and Velli, 1996]. We have not addressed this isue directly both because our shear layers are relatively sharp, and thus involve higher wave numbers, and because higher Reynold's numbers than we use are needed to properly deal with this issue.

Finally, we discuss some significant limitations of this work. First, while we have made the shear layers in the simulations as sharp as reasonably possible given numerical limitations, they are still not sharp enough. In particular, there is potentially a causality problem with the scenario for the cross helicity evolution in the region around the current sheet and between the stream shears. As pointed out by Bruno and Bavassano [1993], there may well not be enough time for the information about the existence of the shears to propagate into the interior of the region by the time the plasma reaches the spacecraft, and thus evolution in the interior of the observed slow wind would not be explicable on the basis of the large shears put into the initial conditions. This does not immediately invalidate our picture, however, first, because the evolution of the cross helicity is very nonuniform, as shown in Figures 1 and 21, and, second, because it is quite likely that the striated regions where the cross helicity is depleted had strong shears within them near the Sun. Woo [1995] has found that regions above the streamer belt (the origin of the heliospheric current sheet) are not uniformly slow, but exhibit much wider speed variability than do the nearby flows. These strong shears could well have produced the observed low cross helicity and highly developed turbulence spectra observed in the striated regions, in the process using up the free energy of the speed differences while not completely obliterating the flux tube structure.

The other main limitations of the simulations here are that they ignore compression and expansion. The importance of compression is a matter of debate. In the two-dimensional simulations by Roberts et al. [1991] little change was found in the "incompressive" fields when compression is included [Roberts et al., 1991]. However, when expansion and rotation are taken into account, both the expansion and the shear flow generate a compressive component which appears to dominate the small scales in the simulations by Grappin and Velli [1996]. It reamins to be seen whether these conclusions remain valid in light of kinetic or other effects; examining these issues will require more detailed simulations. The expansion produces significant effects which are not a matter of debate: it produces major changes in the amplitude of the fluctuations, it is the probable origin of low cross helicity at large scales, and almost certainly produces anisotropies transverse to the flow. Expansion may also have an effect on the cascade rates of inertial range fluctuations, as suggested by Grappin et al. [1993] and Grappin and Velli [1996], and, indeed, these authors maintain that the expansion also enhances compressive effects relative to incompressive cascades. Despite the clear need for (very computationally demanding) threedimensional turbulence codes for expanding media, we believe that the simulations and linearized theory reported here provide insights that will be modified, but not entirely changed by future work.

Acknowledgments. The authors would like to thank S. Ghosh, E. Siregar, M. Verma, W. H. Matthaeus and Z. Agim for helpful comments, J. Abeles for assistance in code optimization, both the NASA Center for Computational Sciences and Cray Research for computer time and both the National Academy of Sciences and the NASA Space Physics Theory Program for financial support.
The Editor thanks B. Bavassano, T. J. Linde, and another referee for their assistance in evaluating this paper.

## References

Bruno, R., and B. Bavassano, Cross-helicity depletions in the inner heliosphere, and magnetic field and velocity fluctuation decoupling, Planet. Space Sci., 41, 677, 1993.
Chandrasekhar, S., Hydrodynamic and Magnetohydrodynamic Stability, Oxford U., New York, 1961.
Dahlburg, R. B., T. A. Zang, D. Montgomery and M. Y. Hussani, Viscous resistive magnetohydrodynamic stability computed spectral techniques, Proc. Natl. Acad. Sci., 80, 5798, 1983.
Dahlburg, R. B., S. K. Antiochos and T. A. Zang, Secondary instability in 3-D magnetic reconnection, Phys. Fluids B, 4, 3902, 1992.
Dobrowolny, M., A. Mangeney and P. Veltri, Fully developed anisotropic hydromagnetic turbulence in interplanetary space, Phys. Rev. Lett., 45, 144, 1980.
Einaudi, G. and F. Rubini, Resistive instabilities in a flowing plasma: I. Inviscid case, Phys. Fluids, 29, 2563, 1986.
Einaudi, G. and F. Rubini, Resistive instabilities in a flowing plasma: II. Effects of viscosity, Phys. Fluids B, 1, 2224, 1989.

Frisch, U., A. Pouquet, J. Léorat and A. Mazure, Possibility
of an inverse cascade of magnetic helicity in magnetohydrodynamic turbulence, J. Fluid Mech., 68, 769, 1975.
Furth, H. P., J. Killeen and M. N. Rosenbluth, Finiteresistivity instabilities of a sheet pinch, Phys. Fluids, 6, 459, 1963.
Goldstein, M. L., D. A. Roberts, and C. A. Fitch, Properties of the fluctuating magnetic helicity in the inertial and dissipation ranges of solar wind turbulence, J. Geophys. Res., 99, 11,519, 1994.
Goldstein, M. L., D. A. Roberts, and W. H. Matthaeus, Magnetohydrodynamic turbulence in the solar wind, Ann. Rev. Astron. Astrophy., 33, 283, 1995.
Grappin, R., and M. Velli, Waves and streams in the expanding solar wind, J. Geophys. Res., 101, 425, 1996.
Grappin, R., U. Frisch, J. Léorat, and A. Pouquet, Alfvénic fluctuations as asymptotic states of MHD turbulence, $A s$ tron. Astrophys., 105, 6, 1982.
Grappin, R., A. Pouquet, and J. Lorat, Dependence of MHD turbulence spectra on the velocity field-magnetic field correlation, Astron. and Astrophys., 126, 51, 1983.
Grappin, R., A. Mangeney and E. Marsch, On the origin of solar wind MHD turbulence: Helios data revisited, $J$. Geophys. Res., 95, 8197, 1990.
Grappin, R., M. Velli, and A. Mangeney, Nonlinear wave evolution in the expanding solar wind, Phys. Rev. Lett., 70, 2190, 1993.
Hesse, M., and J. Birn, Magnetic reconnection in the magnetotail current sheet for varying cross-tail magnetic field, Geophys. Res. Lett., 17, 2019-2022, 1990.
Hollweg, J. V., Some physical processes in the solar wind, Rev. Geophys., 16, 689, 1978.
Klein, L., R. Bruno, B. Bavassano, and H. Rosenbauer, Anisotropy and minimum variance of magnetohydrodynamic fluctuations in the inner heliosphere, J. Geophys. Res., 98, 17,461, 1993.
Kraichnan, R. H., Statistical dynamics of two-dimensional flow, J. Fluid Mech., 67, 155, 1975.
Malara, F., P. Veltri, C. Chiuderi, and G. Einaudi, Energy dissipation by Alfvén waves propagating in an inhomogeneous magnetic field, in Solar Wind 7, COSPAR Colloq. Ser., vol. 3, edited by E. Marsch and R. Schwenn, p. 487, Pergamon, New York, 1992.
Malara, F., L. Primavera, P. Veltri, Compressive fluctuations generated by time evolution of Alfvénic perturbations in the solar wind current sheet, J. Geophys. Res., in press, 1996.
Marsch, E., and C.-Y. Tu, Modeling results on spatial transport and spectral transfer of solar wind Alfvénic turbulence, J. Geophys. Res., 98, 21,045-21,060, 1993.
Matthaeus, W. H., and M. L. Goldstein, Measurement of the rugged invariants of magnetohydrodynamic turbulence in the solar wind, J. Geophys. Res., 87, 6011, 1982.
Matthaeus, W. H. and Y. Zhou, Extended inertial range phenomenology of magnetohydrodynamic turbulence, Phys. Fluids B 1, 1929, 1989.
Matthaeus, W. H., M. L. Goldstein, and D. Montgomery, Turbulent generation of outward traveling interplanetary Alfvénic fluctuation, Phys. Rev. Lett., 51, 1484, 1984.
Meneguzzi, M., U. Frisch, and A. Pouquet, Helical and nonhelical turbulent dynamos, Phys. Rev. Lett., 47, 1069, 1981.

Moffatt, H. K., Magnetic Field Generation in Electrically Conducting Fluids, Cambridge University Press, New York, 1978.
Montgomery, D., M. Brown, and W. H. Matthaeus, Density fluctuation spectra in magnetohydrodynamic turbulence, J. Geophys. Res., 92, 282, 1987.

Ofman, L., X. L. Chen, P. J. Morrison and R. S. Steinolfson, Resistive tearing mode instability with shear flow and viscosity, Phys. Fluids B, 3, 1364, 1991.

Oughton, S., and W. H. Matthaeus, Linear transport of solar wind fluctuations, J. Geophys. Res., 100, 14,783-14,800, 1995.

Oughton, S., E. Priest, and W. H. Matthaeus, The influence of a mean magnetic field on three dimensional MHD turbulence, J. Fluid Mech., 280, 95, 1994.
Pouquet, A. and G. S. Patterson, Numerical simulation of helical magnetohydrodynamic turbulence, J. Fluid Mech., 85, 305, 1978.
Pouquet, A., U. Frisch and J. Léorat, Strong MHD helical turbulence and the nonlinear dynamo effect, J. Fluid Mech., 77, 321, 1976.
Roberts, D. A., Observation and simulation of the radial evolution and stream structure of solar wind turbulence, in Solar Wind Seven, COSPAR Colloq. Ser., Vol. 3, edited by E. Marsch and R. Schwenn, p. 533, Pergamon Press, New York, 1992.
Roberts, D. A., L. W. Klein, M. L. Goldstein, and W. H. Matthaeus, The nature and evolution of magnetohydrodynamic fluctuations in the solar wind: Voyager observations, J. Geophys. Res., 92, 11021, 1987a.
Roberts, D. A., M. L. Goldstein, L. W. Klein and W. H. Matthaeus, Origin and evolution of fluctuations in the solar wind: Helios observations and Helios-Voyager comparisons, J. Geophys. Res., 92, 12023, 1987b.
Roberts, D. A., M. L. Goldstein, and L. W. Klein, The amplitudes of interplanetary fluctuations: stream structure, heliocentric distance, and frequency dependence, J. Geophys. Res., 95, 4203, 1990.
Roberts, D. A., S. Ghosh, M. L. Goldstein, and W. H. Matthaeus, Magnetohydrodynamic simulation of the radial evolution and stream structure of solar-wind turbulence, Phys. Rev. Lett., 67, 3741, 1991.
Roberts, D. A., M. L. Goldstein, W. H. Matthaeus and S. Ghosh, Velocity shear generation of solar wind turbulence, J. Geophys Res., 97, 17115, 1992.

Roberts, D. A., S. Ghosh, and M. L. Goldstein, Nonlinear evolution of interplanetary Alfvénic fluctuations with convected structures, Geophys. Res. Lett., 23, 591, 1996.
Schmidt, J. M., Spatial transport and spectral transfer of solar wind turbulence composed of Alfvén waves and convective structures II: Numerical results, Ann. Geophys., 13, 475-493, 1995.
Schmidt, J. M., and E. Marsch, Spatial transport and spectral transfer of solar wind turbulence composed of Alfvén waves and convective structures I: The theoretical model, Ann. Geophys., 13, 459-474, 1995.
Shebalin, J. V., W. H. Matthaeus, and D. Montgomery, Anisotropy in MHD turbulence due to a mean magnetic field, J. Plasma Phys., 29, 525, 1983.
Stribling, T. and W. H. Matthaeus, Statistical properties of ideal three-dimensional magnetohydrodynamics, Phys. Fluids B, 2, 1979, 1990.
Stribling, T. and W. H. Matthaeus, Relaxation processes in a low-order three-dimensional magnetohydrodynamics model, Phys. Fluids B, 8, 1848, 1991.
Squire, H. B., On the stability of three-dimensional distribution of viscous fluid between parallel walls, Proc. Roy. Soc. London A, 142, 621, 1933.
Tu, C.-Y., and E. Marsch, A case study of very low crosshelicity fluctuations in the solar wind, Ann. Geophys., 9, 319, 1991.
Tu, C. -Y. and E. Marsch, A model of solar wind fluctuations with two components: Alfvén waves and convective structures, J. Geophys Res., 98, 1257, 1993.
Tu, C.-Y., and E. Marsch, MHD Structures, Waves and Turbulence in the Solar Wind: Observations and Theories, Kluwer Acad., Norwell, Mass., 1995.
Tu, C.-Y., E. Marsch, and H. Rosenbauer, The dependence of MHD turbulence spectra on the inner solar wind stream
structure near solar minimum, Geophys. Res. Lett., 17, 283, 1990.
Veltri, P., F. Malara, and L. Primavera, Correlation, anisotropy, and compressibility of low frequency fluctuations in solar wind, in Solar Wind 7, COSPAR Colloq. Ser., vol. 3, edited by E. Marsch and R. Schwenn, p. 559, Pergamon, New York, 1992.
Wang, S., L. C. Lee and C. Q. Wei, Streaming tearing instability in the current sheet with super-Alfvénic Flow, Phys. Fluids, 31, 1544, 1988.
Woo, R. Solar wind speed structure in the inner corona at 3-12 $\mathrm{R}_{o}$, Geophys. Res. Lett., 22, 1393, 1995.
Zank, G., and W. Matthaeus, Nearly incompressible fluids,

II, Magnetohydrodynamics, turbulence and waves, Phys. Fluids A, 5, 257, 1993.
Zhou, Y., and W. H. Matthaeus, Models of inertial range spectra of interplanetary magnetohydrodynamic turbulence, J. Geophys. Res., 95, 14881, 1990.

[^1](Received October 4, 1995; revised August 19, 1996; accepted August 19, 1996.)


[^0]:    ${ }^{1}$ Now at Laboratory for Hydrospheric Processes, NASA Goddard Space Flight Center, Greenbelt, Maryland

[^1]:    M. L. Goldstein and D. A. Roberts, NASA-Goddard Space Flight Center, Code 692, Greenbelt, MD 20771
    W. T. Stribling, NASA-Goddard Space Flight Center, Code 971, Greenbelt, MD 20771

