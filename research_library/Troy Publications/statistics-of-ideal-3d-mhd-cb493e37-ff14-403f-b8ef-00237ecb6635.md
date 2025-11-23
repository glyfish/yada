# Statistical properties of ideal three-dimensional magnetohydrodynamics 

T. Stribling and W. H. Matthaeus<br>Bartol Research Institute, University of Delaware, Newark, Delaware 19716

(Received 8 February 1990; accepted 14 May 1990)


#### Abstract

Classical Gibbs ensemble methods are used to study the spectral structure of three-dimensional ideal magnetohydrodynamics (MHD) in periodic geometry. The intent of this work is to provide further detail and extensions to the work of Frisch et al. [J. Fluid Mech. 68, 769 (1975)], who used equilibrium ensemble methods to predict inverse spectral transfer of magnetic helicity. Here, the equilibrium ensemble incorporates constraints of total energy, magnetic helicity, and cross helicity. Several new results are proven for ensemble averages, including the constraint that magnetic energy equal or exceed kinetic energy, and that cross helicity represents a constant fraction of magnetic energy across the spectral domain, for arbitrary size systems. Two zero temperature limits are considered in detail, emphasizing the role of complete and partial condensation of spectral quantities to the longest wavelength states. The ensemble predictions are compared to direct numerical solution using a low-order truncation Galerkin spectral code. Implications for spectral transfer of nonequilibrium, dissipative turbulent MHD systems are discussed.


## I. INTRODUCTION

Because of the difficulty in obtaining tractable results for the statistical dynamics of dissipative hydrodynamic and magnetohydrodynamic (MHD) turbulence, it is of interest to investigate closely related nondissipative models of turbulence, for which an exactly solvable equilibrium statistical mechanics exists. ${ }^{1-7}$ This line of investigation into the absolute equilibrium statistical mechanics of fluids has been successfully employed to obtain qualitative insight concerning spectral transfer induced by nonlinear couplings in the presence of dissipation. ${ }^{1-6}$ This important aspect of the theory began following Kraichnan's suggestion ${ }^{1,8}$ that the tendencies of ideal spectra to peak in different regions of wave number space is an indicator of cascade direction in more general circumstances than those adopted in the equilibrium models. Applications of this approach to a variety of fluid systems has led, for example, to conjectures of the inverse cascades of mean square vector potential ${ }^{2}$ and of magnetic helicity ${ }^{3}$ in two-dimensional (2-D) and three-dimensional (3-D) MHD, respectively, as well as predictions of equilibrium and spectral transfer properties of guiding center plasmas, ${ }^{7,9}$ electron fluids, ${ }^{10}$ and drift wave turbulence. ${ }^{11,12}$ Similar arguments also form the basis of selective decay hypotheses, ${ }^{4,13}$ which have been extensively studied numerically. ${ }^{13,14}$ When applying ideas from the equilibrium theory to dissipative turbulence, it is important to bear in mind that only qualitative aspects of spectral transfer can be inferred, since dissipative turbulent transfer necessarily involves departures from the equilibrium Gaussian statistics.

In this paper we extend the work of previous authors on 3-D MHD absolute equilibrium. ${ }^{3,4}$ The focus is on the properties of the equilibrium ensembles, such as the condensation of rugged invariant spectra in wave number space,that are believed to be responsible for inverse spectral transfer. A notable feature of the present discussion is a detailed treatment of the equilibrium properties of the cross helicity, and its possible influence on spectral transfer, which have not
been clearly understood. A central motivation of this work is to provide a basis for better understanding of MHD spectral transfer for arbitrary ratios of the conserved rugged invariants and the influence of this on turbulent processes such as selective decay and dynamic alignment. ${ }^{4,13,14}$ We also hope to provide a basis for insights into future numerical studies of dissipative 3-D MHD.

The outline of the paper is as follows. In Sec. II the requisite background is developed, leading to a description of the basic results of the absolute equilibrium MHD theory in Sec. III. Next, in Secs. IV and V the properties of the rugged invariant spectra are determined for two limits that are believed to be relevant to the theory of MHD turbulence. In Sec. IV the rugged invariants are allowed to take on their maximal values and the equilibrium spectra are examined at the associated boundaries of the allowed parameter space of global invariants. In Sec.V the second limiting case is examined, in which the dimension of the solution phase space is taken to infinity, a situation that may be of interest in drawing inferences concerning high Reynolds number dissipative spectral transfer. In this section we also introduce the notion of "partial condensation" of the cross helicity spectrum. In Sec. VI we compare the ensemble-averaged rugged invariant spectra with the time-averaged spectra from a simulation of a Galerkin model of ideal 3-D MHD, in order to establish the accuracy of the ensemble predictions for even a system with just a moderate number of participating Fourier modes. In Sec. VII possible dynamical implications of the ensemble spectral predictions for dissipative MHD are discussed, emphasizing the implications of the partial condensation of the cross helicity spectrum.

## II. 3-D MAGNETOHYDRODYNAMICS, RUGGED INVARIANTS, AND THE EQUILIBRIUM ENSEMBLE

The equations of ideal, constant density, incompressible 3-D MHD in familiar dimensionless variables are given by

$$
\begin{align*}
& \frac{\partial \mathbf{v}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{v}=-\nabla p^{*}+\mathbf{b} \cdot \nabla \mathbf{b},  \tag{1a}\\
& \frac{\partial \mathbf{b}}{\partial t}+\mathbf{v} \cdot \nabla \mathbf{b}=\mathbf{b} \cdot \nabla \mathbf{v},  \tag{1b}\\
& \nabla \cdot \mathbf{v}=0,  \tag{1c}\\
& \nabla \cdot \mathbf{b}=0 . \tag{1d}
\end{align*}
$$

The velocity and magnetic fields, $\mathbf{v}$ and $\mathbf{b}$, are written in Alfvén speed units, $p^{*}$ is the total pressure, determined by a Poisson equation when use is made of incompressibility, Eq. (1c). The time unit is taken to be an eddy turnover time for the velocity field at unit length scale.

The $\mathbf{v}$ and $\mathbf{b}$ fields are assumed to be periodic in a 3-D box with sides of dimensionless length $2 \pi$. Thus we write

$$
\begin{align*}
& \mathbf{v}(\mathbf{x}, t)=\sum_{\mathbf{k} \in \mathbf{N}} \mathbf{v}(\mathbf{k}, t) \exp (i \mathbf{k} \cdot \mathbf{x})  \tag{2a}\\
& \mathbf{b}(\mathbf{x}, t)=\sum_{\mathbf{k} \in \mathbf{N}} \mathbf{b}(\mathbf{k}, t) \exp (i \mathbf{k} \cdot \mathbf{x}) \tag{2b}
\end{align*}
$$

where $N$ is a collection of 3-D wave vectors $\mathbf{k}$ with integer components such that $k_{\text {min }} \leqslant|\mathbf{k}| \leqslant k_{\text {max }}$. Vectors must be included in $\mathbf{N}$ so that the reality condition is satisfied, namely,

$$
\begin{align*}
& \mathbf{v}(\mathbf{k}, t)=v^{*}(-\mathbf{k}, t)  \tag{3a}\\
& \mathbf{b}(\mathbf{k}, t)=\mathbf{b}^{*}(-\mathbf{k}, t) \tag{3b}
\end{align*}
$$

In this paper the cases where $k_{\text {max }}$ is finite and infinite are both examined, and, in general, we will denote as $N$ the number of Fourier modes (vectors) retained in N. When (2) is inserted into (1) a system of first-order nonlinear equations for the Fourier coefficients is produced.

This ideal 3-D MHD model is believed to conserve only three quantities for arbitrary $\mathbf{N}$, which are referred to as the rugged invariants. The rugged invariants play an important role in interpretation of the qualitative and time-asymptotic behavior of the solutions to (1). They are the energy $E$, the cross helicity $H_{c}$, and the magnetic helicity $H_{m}$, each expressed as a "per unit mass" quantity and defined by

$$
\begin{align*}
E= & \frac{1}{2 V} \int\left(|\mathbf{v}|^{2}+|\mathbf{b}|^{2}\right) d^{3} x \\
= & \frac{1}{2} \sum_{\mathbf{k} \in \mathbb{N}\}}\left[|\mathbf{v}(\mathbf{k})|^{2}+|\mathbf{b}(\mathbf{k})|^{2}\right]=E_{v}+E_{b}  \tag{4a}\\
H_{c}= & \frac{1}{2 V} \int \mathbf{v} \cdot \mathbf{b} d^{3} x \\
= & \frac{1}{4} \sum_{\mathbf{k} \in\{\mathbb{N}\}}\left[\mathbf{v}(\mathbf{k}) \cdot \mathbf{b}^{*}(\mathbf{k})+\mathbf{v}^{*}(\mathbf{k}) \cdot \mathbf{b}(\mathbf{k})\right]  \tag{4b}\\
H_{m}= & \frac{1}{2 V} \int \mathbf{a} \cdot \mathbf{b} d^{3} x \\
= & \frac{1}{4} \sum_{\mathbf{k} \in\{\mathbb{N}\}} \frac{i}{k^{2}}\left\{[\mathbf{k} \times \mathbf{b}(\mathbf{k})] \times \mathbf{b}^{*}(\mathbf{k})\right. \\
& \left.-\left[\mathbf{k} \times \mathbf{b}^{*}(\mathbf{k})\right] \cdot \mathbf{b}(\mathbf{k})\right\} \tag{4c}
\end{align*}
$$

The integrals are evaluated over a box of volume $V=(2 \pi)^{3}$, and $E_{v}$ and $E_{b}$ are the kinetic and magnetic energy per unit mass, respectively. These quantities are conserved when summed over any interacting triad of wave vectors (i.e., any $\mathbf{m}, \mathbf{n}$, and $\mathbf{k}$ such that $\mathbf{m}+\mathbf{n}=\mathbf{k}$ ).

Lee ${ }^{15}$ showed that the periodic solutions of (1) satisfy a Liouville theorem in the phase space with coordinates that are the real and imaginary parts of $\mathbf{v}(\mathbf{k})$ and $\mathbf{b}(\mathbf{k})$. This allows one to use classical equilibrium statistical mechanics to investigate the statistical properties of these solutions. ${ }^{3,4,2}$ The generalized canonical distribution of states is

$$
\begin{equation*}
P=\exp \left[-\left(\beta E+\gamma H_{c}+\theta H_{m}\right)\right] / Z, \tag{5}
\end{equation*}
$$

where $\beta, \gamma$, and $\theta$ are generalized inverse temperatures corresponding to $E, H_{c}$, and $H_{m}$, respectively. The partition function $Z$ is given by

$$
\begin{align*}
Z & =\int_{\text {phase space }} \exp -\left(\beta E+\gamma H_{c}+\theta H_{m}\right) d \omega \\
& =\prod_{k \in \mathbb{N}} \frac{(2 \pi)^{4} k^{2}}{\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2} k^{2}-\theta^{2} \beta^{2}} \tag{6}
\end{align*}
$$

where $d \omega$ is a phase space volume element. The requirement that $Z$ be finite gives the following constraints on the inverse temperatures:

$$
\begin{align*}
& \beta>0  \tag{7a}\\
& |\gamma| / 2<\beta  \tag{7b}\\
& |\theta|<k_{\min }\left(\beta-\gamma^{2} / 4 \beta\right) \tag{7c}
\end{align*}
$$

The ensemble-averaged rugged invariant spectra can be found by integration over the phase space, or more easily by differentiation of the partition function. Upon doing this it is found that

$$
\begin{align*}
& \left\langle E_{v}(\mathbf{k})\right\rangle=\frac{2}{\beta}\left(1+\frac{\gamma^{2}}{4} \frac{\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right) k^{2}}{d(k)}\right),  \tag{8a}\\
& \left\langle E_{b}(\mathbf{k})\right\rangle=2 \beta\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right) k^{2} / d(k),  \tag{8b}\\
& \langle E(\mathbf{k})\rangle=2 \beta\left[2\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right) k^{2}-\theta^{2}\right] / d(k),  \tag{8c}\\
& \left\langle H_{c}(\mathbf{k})\right\rangle=-\gamma\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right) k^{2} / d(k),  \tag{8~d}\\
& \left\langle H_{m}(\mathbf{k})\right\rangle=-2 \theta \beta^{2} / d(k),  \tag{8e}\\
& d(k)=\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2} k^{2}-\theta^{2} \beta^{2} . \tag{8f}
\end{align*}
$$

From (7) it follows that $d(k)>0$ and $\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)>0$. It can now easily be shown that the energy spectrum is positive definite, as it must be, and that the helicity spectra do not change sign. This implies that the helicity inverse temperatures and their respective helicities have opposite signs, i.e.,

$$
\begin{align*}
& \gamma H_{c} \leqslant 0,  \tag{9a}\\
& \theta H_{m} \leqslant 0 . \tag{9b}
\end{align*}
$$

It also follows from (8) that $\theta=0$ if $H_{m}=0$, and that $\gamma=0$ if $H_{c}=0$. The inverse temperatures can be numerically solved for, and in certain limits analytically solved for (cf. Secs. IV and V), from the system of equations

$$
\begin{align*}
& E=\sum_{\mathbf{k} \in \mathbf{N}}\langle E(\mathbf{k})\rangle  \tag{10a}\\
& H_{c}=\sum_{\mathbf{k} \in \mathbf{N}}\left\langle H_{c}(\mathbf{k})\right\rangle  \tag{10b}\\
& H_{m}=\sum_{\mathbf{k} \in \mathbf{N}}\left\langle H_{m}(\mathbf{k})\right\rangle \tag{10c}
\end{align*}
$$

In Fig. 1 examples of rugged invariant spectra are given for a particular choice of parameters.

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-03.jpg?height=616&width=760&top_left_y=92&top_left_x=159)
FIG. 1. Modal rugged invariant spectra computed from absolute equilibrium theory for $N=226980, k_{\text {min }}=1, k_{\text {max }}=30 \sqrt{3}, E=1, H_{c}=0.25$, and $H_{m}=0.3$.

## III. USEFUL RELATIONS AT ABSOLUTE EQUILIBRIUM

From (8b) and (8d) it is easy to see that

$$
\begin{equation*}
\left\langle H_{c}(\mathbf{k})\right\rangle /\left\langle E_{b}(\mathbf{k})\right\rangle=-\gamma / 2 \beta . \tag{11}
\end{equation*}
$$

Since $\gamma / 2 \beta$ is independent of $\mathbf{k}$, the ratio is a constant over $\mathbf{k}$ space. This simple relation will play an important role in later discussions of the equilibrium spectra. The possible implications of this for spectral transfer of $H_{c}$ in the presence of dissipation will be discussed in Sec. VII.

Expressions that relate all the inverse temperatures and the rugged invariants are also readily found. They are

$$
\begin{align*}
& \beta E+\gamma H_{c}+\theta H_{m}=4 N,  \tag{12a}\\
& \gamma \beta E+4 \beta^{2} H_{c}-\gamma \theta H_{m}=0, \tag{12b}
\end{align*}
$$

where $N$ is the number of terms kept in the Galerkin representations of $\mathbf{v}$ and $\mathbf{b}$. The first equation can be shown to be analogous to the defining relation of the Helmholtz free energy of conventional thermodynamics.

Introducing the parameter $R=\left\langle E_{v}\right\rangle /\left\langle E_{b}\right\rangle$ and using (12) the following expressions for the inverse temperatures are found:

$$
\begin{align*}
& \beta=(8 N / E)\left[(1+R) / f\left(R, \sigma_{c}\right)\right]  \tag{13a}\\
& \gamma=-\left(8 N \sigma_{c} / E\right)\left[(1+R)^{2} / f\left(R, \sigma_{c}\right)\right]  \tag{13b}\\
& \theta=-\left(8 N / E \sigma_{m}\right)\left[(1-R) / f\left(R, \sigma_{c}\right)\right]  \tag{13c}\\
& f\left(R, \sigma_{c}\right)=4 R-\sigma_{c}^{2}(1+R)^{2} \tag{13~d}
\end{align*}
$$

where $\sigma_{c}=2 H_{c} / E$ and $\sigma_{m}=k_{\text {min }} H_{m} / E$ are convenient dimensionless normalized measures of the cross helicity and magnetic helicity satisfying $\left|\sigma_{c}\right| \leqslant 1$ and $\left|\sigma_{m}\right| \leqslant 1$. Moreover, one finds that $f\left(R, \sigma_{c}\right)>0$ since, if the mean angle between $\mathbf{v}$ and $\mathbf{b}$ is defined by $\cos \Theta=H_{c} / \sqrt{E_{v} E_{b}}$, then

$$
\begin{equation*}
\cos ^{2} \theta=\sigma_{c}^{2}(1+R)^{2} / 4 R, \tag{14}
\end{equation*}
$$

and the desired result follows by comparison with (13d) using $\cos ^{2} \Theta \leqslant 1$. By the same reasoning, $f\left(R, \sigma_{c}\right)=0 \mathrm{im}$ plies and $\mathbf{v}$ and $\mathbf{b}$ are aligned or antialigned. Expressions similar to (13) have been given for 2-D MHD by Shebalin. ${ }^{16}$

It should be noted that $R$ is not an independent parameter in these expressions, but is a function of $N, \sigma_{c}$, and $\sigma_{m}$.

In the limits discussed in the following sections the inverse temperatures diverge, but certain ratios of them remain finite because of (7). So it is convenient to define

$$
\begin{align*}
& \beta_{\gamma}=\gamma / 2 \beta,  \tag{15a}\\
& \beta_{\theta}=\theta / \beta . \tag{15b}
\end{align*}
$$

The constraints placed on $\beta_{\theta}$ and $\beta_{\gamma}$ by (7) are

$$
\begin{align*}
& \left|\beta_{\gamma}\right|<1  \tag{16a}\\
& \left|\beta_{\theta}\right|<k_{\min }\left(1-\beta_{\gamma}^{2}\right) \tag{16b}
\end{align*}
$$

while one finds from (13) that

$$
\begin{align*}
& \beta_{\gamma}=-\left(\sigma_{c} / 2\right)(1+R)  \tag{17a}\\
& \beta_{\theta}=-\left(1 / \sigma_{m}\right)[(1-R) /(1+R)] \tag{17b}
\end{align*}
$$

In view of the fact that $\theta$ and $H_{m}$ have opposite signs [cf. (9)], it follows from (17b) that $R$ must satisfy the inequality

$$
\begin{equation*}
R \leqslant 1 . \tag{18}
\end{equation*}
$$

Consequently one sees that equilibrium 3-D MHD is characterized by a distribution of energy in which the magnetic ingredient always dominates, a result in contrast to the 2-D equilibrium theory. ${ }^{2}$ In a later section possible consequences of this inequality for spectral transfer of $E_{v}$ and $E_{b}$ in the presence of dissipation will be discussed.

The equilibrium spectra shown in Fig. 1 for a finite $N$ and moderate amounts of $H_{m}$ and $H_{c}$ are strongly peaked at the longest wavelength. It is of interest to describe the types of variation of the system parameters that lead to greater emphasis of this feature. Specifically, in the following sections we examine limiting forms of the spectra, associated with extremal values of the parameters $\sigma_{m}, \sigma_{c}$, and $N$, that lead to condensation of the rugged invariant spectra into the longest wavelength modes. For this purpose it will be convenient to define

$$
\begin{equation*}
E(K)=\sum_{|\mathbf{k}|>k_{\text {min }}}\langle E(\mathbf{k})\rangle, \tag{19a}
\end{equation*}
$$

so that

$$
\begin{equation*}
E=E\left(k_{\min }\right)+E(K), \tag{19b}
\end{equation*}
$$

where $E\left(k_{\text {min }}\right)$ is the energy in the modes with $|\mathbf{k}|=k_{\text {min }}$. Similar notation will be used for the analogous partitioning of $E_{v}, E_{b}$, and $H_{c}$, and $H_{m}$. In the next two sections we discuss two limits that generate singular behavior in the inverse temperatures, and describe properties of the rugged invariant spectra in each case.

In the first limiting procedure $N$ is kept fixed while the parameters $\sigma_{m}$ and $\sigma_{c}$ are varied. It will be shown that, when $\left|\sigma_{c}\right| \rightarrow 1$ with $\left|\sigma_{m}\right|<\frac{1}{2}$, the inverse temperatures $\gamma$ and $\beta \rightarrow \infty$ while $\theta$ remains finite. No condensation of the rugged invariant spectra into a single wavelength occurs. When $\left|\sigma_{m}\right| \geqslant \frac{1}{2}$ and $\sigma_{c}$ is maximal, all three inverse temperatures are shown to diverge. In this limit a condensation into the longest wavelength of all three rugged invariant spectra will be demonstrated.

The second singular limit is obtained as $N \rightarrow \infty$ for fixed values of the rugged invariants. When $H_{m}=0$ we will find that $\gamma \rightarrow \infty$ and $\beta \rightarrow \infty$ and that the energy and cross helicity
per degree of freedom go to zero in such a way that $E$ and $H_{c}$ remain finite. For nonzero $H_{m}$ it will be shown that all three of the inverse temperatures diverge and that the $H_{m}$ spectrum condenses to the longest wavelength. The presence of $H_{m}$ will be shown to induce a "partial condensation" of the $H_{c}$ spectrum to the longest wavelength, that is, the amount of $H_{c}$ in the longest wavelength is finite, in contrast to the $H_{m}=0$ situation, while a nonzero amount of $H_{c}$ remains in the high- $k$ portion of the spectrum. Also, the portion of $H_{c}$ that is partially condensed is not determined by kinematic constraints but by the maximum entropy principle that defines equilibrium, as is the condensation of $H_{m}$. A nonzero portion of the $E$ spectrum is also present in the longest wavelength, but this will be shown to be the minimum amount of energy needed to satisfy the kinematic constraints imposed by the quantities of $H_{c}$ and $H_{m}$ in the longest wavelengths. Next we show that the $N \rightarrow \infty$ expressions for $\beta_{\gamma}$ and $\beta_{\theta}$ approach the finite $N$ values as $\sigma_{m}$ and $\sigma_{c}$ approach their maximal values, so that the two types of limits are seen to be consistent with one another.

## IV. LIMITING FORMS OF RUGGED INVARIANT SPECTRA AT PARAMETER SPACE BOUNDARIES

On examination of (8) it is seen that the shapes of the rugged invariant spectra are determined by the parameters $\sigma_{m}$ and $\sigma_{c}$ for $N$ fixed, with the energy determining the scale of the remaining parameters. In this section the behavior of the rugged invariant spectra in the $\sigma_{m}$ and $\sigma_{c}$ parameter space will be examined. Here $N$ will be assumed fixed and finite and $E, H_{m}$, and $H_{c}$ will be constrained to be finite. The first limit that will be considered is $\sigma_{m}$ and $\sigma_{c} \rightarrow 0$, which implies that $\gamma$ and $\theta \rightarrow 0$. It follows from (8) that

$$
\begin{equation*}
\left\langle E_{v}(\mathbf{k})\right\rangle=\left\langle E_{b}(\mathbf{k})\right\rangle=2 / \beta ; \tag{20}
\end{equation*}
$$

thus the energy spectrum is flat and equipartitioned.
Now consider the case $\sigma_{m}=0$. With $\theta=0$, (8) gives

$$
\begin{align*}
& \left\langle E_{v}(\mathbf{k})\right\rangle=\left\langle E_{b}(\mathbf{k})\right\rangle=2 \beta /\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right),  \tag{21a}\\
& \left\langle H_{c}(\mathbf{k})\right\rangle=-\gamma /\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right) \tag{21b}
\end{align*}
$$

which describe flat, $k$-independent equilibrium spectra. From the expressions above it is easily seen that $\beta_{r}=-\sigma_{c}$. The same result can be obtained from (17a) by letting $R=1$; the expressions for $\gamma$ and $\beta$ are obtained by setting $R=1$ in (13). From (13) it is also found that if $\left|\sigma_{c}\right| \rightarrow 1$ then $\beta \sim|\gamma| \rightarrow \infty$ while $\left|\beta_{\gamma}\right| \rightarrow 1$. To satisfy the constraint that $E$ and $H_{c}$ remain finite and nonzero $\beta^{2}-\frac{1}{4} \gamma^{2} \sim \beta$ for $\left|\sigma_{c}\right|$ infinitesimally near 1. Upon an examination of (21), it is seen that $\langle E(\mathbf{k})\rangle$ and $\left\langle H_{c}(\mathbf{k})\right\rangle$ remain finite and nonzero for every $\mathbf{k}$, so there is no condensation of $E$ or $H_{c}$ in wave number space.

Now let $\sigma_{m}$ be nonzero and fixed. When $N$ and $\sigma_{m}$ are both fixed, $R$ is a function only of $\sigma_{c}$ and, from (13), the inverse temperatures diverge when $f\left(R, \sigma_{c}\right)=0$. This is equivalent to a situation in which the $\mathbf{v}$ and $\mathbf{b}$ are aligned or antialigned. First, let $\left|\sigma_{c}\right| \rightarrow 1$, its maximum value, so that $R \rightarrow 1$ and thus $f\left(R, \sigma_{c}\right) \rightarrow 0$. From (13) it follows that $\beta \sim 1 / f\left(R, \sigma_{c}\right) \sim|\gamma|$ since all other parameters are fixed and finite and the numerators of (13a) and (13b) do not vanish. This limit leaves $\theta$ undetermined since both the numerator
and denominator of (13c) vanish. However, from (17) it is seen that for nonzero $\sigma_{m}, \beta_{\theta} \rightarrow 0$ and $\left|\beta_{\gamma}\right| \rightarrow 1$. This implies that $|\theta|<1 / f\left(R, \sigma_{c}\right)$, so that $|\theta|<\beta \sim|\gamma|$. In order to maintain finite values for $E, H_{c}$, and $H_{m}$, both $\beta$ and $|\gamma| \rightarrow \infty$ in such a way that $\beta^{2}-\frac{1}{4} \gamma^{2} \sim \beta$. Combined with the constraint that the $E$ spectrum be positive definite [i.e., $d(k)>0$ ], this implies that $\theta$ must be finite. So for each $k$, $\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2} k^{2} / \beta^{2}-\theta^{2}$ is finite. Thus there is no condensation of $E, H_{c}$, or $H_{m}$ in a wave number space for the limit of fixed $N$ and $\sigma_{m}$ with $\sigma_{c} \rightarrow 1$.

Once again let $\sigma_{m}$ be nonzero and fixed, so that $R$ depends only upon $\sigma_{c}$, but in distinction to the previous paragraph, this time let $\sigma_{c}$ approach a value so that $f\left(R, \sigma_{c}\right) \rightarrow 0$ with $R \neq 1$. An examination of $f\left(R, \sigma_{c}\right)$ in (13d) shows that for every fixed $\left|\sigma_{c}\right|<1$ there is an $R<1$ that is a root of $f$, so the previously derived constraint on $R$ is satisfied. When $R<1$, (13c) no longer leaves $\theta$ undetermined, but rather this expression is seen to go to infinity. Consequently, when $\sigma_{c}$ approaches a values such that $f\left(R, \sigma_{c}\right) \rightarrow 0$ with $R<1$, all the inverse temperatures diverge with $|\theta| \sim \beta \sim|\gamma| \sim 1 / f\left(R, \sigma_{c}\right)$. Now note that, from (17b), $\left|\beta_{\theta}\right|$ is nonzero whenever $R<1$. Also, since neither $\left|\sigma_{c}\right|$ nor $R$ are approaching 1 , it can be seen from (17a) that $\beta_{\gamma}$ is no longer infinitesimally near 1. Thus, $\beta^{2}-\frac{1}{4} \gamma^{2} \sim \beta^{2}$. To maintain finite and nonzero values of $E, H_{c}$, and $H_{m}$ and satisfy (7) with infinite values for the inverse temperatures, $d\left(k_{\text {min }}\right)$ must satisfy

$$
\begin{equation*}
d\left(k_{\min }\right)=\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2} k_{\min }^{2}-\theta^{2} \beta^{2} \sim \beta^{3} . \tag{22}
\end{equation*}
$$

The behavior of $d(k)$ for $k>k_{\text {min }}$ can now be deduced to be

$$
\begin{equation*}
d\left(k>k_{\min }\right) \approx\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2} k^{2} \sim \beta^{4} \tag{23}
\end{equation*}
$$

The $k>k_{\text {min }}$ portions of the rugged invariant spectra can now be easily evaluated. They are

$$
\begin{equation*}
E(K)=4 \beta(N-n) /\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right), \tag{24a}
\end{equation*}
$$

$$
\begin{align*}
& H_{c}(K)=-\gamma(N-n) /\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right),  \tag{24b}\\
& H_{m}(K)=-\left[2 \theta \beta^{2} /\left(\beta^{2}-\frac{1}{4} \gamma^{2}\right)^{2}\right] g(N), \tag{24c}
\end{align*}
$$

where $g(N)=\Sigma_{k>k_{\text {min }}} k^{-2}$ and $n$ is the number of degrees of freedom in $k_{\text {min }}$. It follows from (23) that each of (24) goes to 0 as $f\left(R, \sigma_{c}\right) \rightarrow 0$, while (22) implies that the $k_{\text {min }}$ portions of the spectrum remain finite and nonzero. Consequently, there is a condensation of $E, H_{c}$, and $H_{m}$ into $k_{\text {min }}$ when $\sigma_{c}$ is varied so that $f\left(R, \sigma_{c}\right) \rightarrow 0$ for $R<1$ with $\sigma_{m}$ and $N$ fixed.

The region of parameter space in which the above-described condensation occurs can be established as follows; if (22) is divided by $\beta^{4}$ and then $f\left(R, \sigma_{c}\right) \rightarrow 0$, which implies that $\beta \rightarrow \infty$. An expression for $\beta_{\theta}$ can be determined, namely,

$$
\begin{equation*}
\beta_{\theta}=-\operatorname{sgn}\left(\sigma_{m}\right) k_{\min }\left(1-\beta_{\gamma}^{2}\right) . \tag{25}
\end{equation*}
$$

It follows from (25), (8b), and (8e) that

$$
\begin{equation*}
\left|H_{m}\right| / E_{b}=1 / k_{\min } . \tag{26}
\end{equation*}
$$

Thus the system is in a state of maximal magnetic helicity. Since $f\left(R, \sigma_{c}\right)=0$ the $\mathbf{v}$ and $\mathbf{b}$ fields are aligned or antialigned (cf. Sec. III), so that the system is also in a state of maximal cross helicity, i.e.,

$$
\begin{equation*}
\left|H_{c}\right|=\sqrt{E_{v} E_{b}} . \tag{27}
\end{equation*}
$$

Equations (26) and (27) can be combined to give

$$
\begin{equation*}
4\left(\left|\sigma_{m}\right|-\frac{1}{2}\right)^{2}+\sigma_{c}^{2}=1 . \tag{28}
\end{equation*}
$$

This equation defines two ellipses in the $\sigma_{m}$ and $\sigma_{c}$ parameter space, which are illustrated in Fig. 2. Only the upper portion of the $\sigma_{m}>0$ ellipse and lower portion of the $\sigma_{m}<0$ ellipse are consistent with the constraint $R \leqslant 1$. These two curves define the region of the parameter space where all three inverse temperatures simultaneously diverge for a fixed system size. The curves also define the region of the parameter space where $\sigma_{m}$ and $\sigma_{c}$ are maximal for a given energy. (This can be proven with a 3-D minimum energy variational calculation, which is a straightforward extension of the 2-D result given by Ting, Matthaeus, and Montgomery. ${ }^{14}$ ) The region above the $\sigma_{m}>0$ ellipse and below the $\sigma_{m}<0$ ellipse is kinematically disallowed. Expressions for $\beta_{\theta}$ and $\beta_{\gamma}$ can now be easily found from (8) if use is made of (23) and the information that the spectra are condensed in $k_{\text {min }}$. They are

$$
\begin{align*}
& \beta_{\theta}=-\operatorname{sgn}\left(\sigma_{m}\right) k_{\min }\left(2-1 /\left|\sigma_{m}\right|\right)  \tag{29a}\\
& \beta_{\gamma}=-\sigma_{c} / 2\left|\sigma_{m}\right| \tag{29b}
\end{align*}
$$

To satisfy the constraints $\theta H_{m} \leqslant 0$ and $\left|\beta_{\gamma}\right|<1$ in (29) we must have $\left|\sigma_{m}\right| \geqslant \frac{1}{2}$. The point on the minimum energy ellipse where $\left|\sigma_{m}\right|=\frac{1}{2}$ is associated with $\left|\sigma_{c}\right|=1$ and $R=1$. This is the transition point where $\theta$ changes from a finite quantity to an infinite one on the parameter space boundary and is also the point of maximal magnetic helicity for $\left|\sigma_{c}\right|=1$. This important point ( $\sigma_{m}=\frac{1}{2}, \sigma_{c}=1$, designated by a "B" in Fig 2) separates the elliptical portion of the parameter space

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-05.jpg?height=624&width=600&top_left_y=1520&top_left_x=154)
FIG. 2. The $\sigma_{m}$ and $\sigma_{c}$ parameter space. The shaded regions are kinematically inaccessible. At point $\mathrm{A} ; \gamma$ and $\beta \rightarrow \infty$. At point $\mathrm{B}, \sigma_{m}$ is maximal for $\sigma_{c}=1$ and it is the transition point on the parameter space boundary where $\theta$ changes from a finite quantity to an infinite one for $N$ fixed and finite. Along the line joining $\mathbf{A}$ and $\mathbf{B}, \gamma$ and $\beta$ are infinite. All three inverse temperatures are infinite along the portions of the two ellipses that join points $B$ and C , and all three rugged invariant spectra condense to $k_{\text {min }}$. These curves are defined by Eq. (28). The curves also define the points where $\sigma_{m}$ is maximal for a given $\sigma_{c}$. Point C is the Taylor state. The above interpretation also applies to points obtained by reflections of $\mathrm{A}, \mathrm{B}$, and C .

boundary (e.g., the curve $\overline{\mathbf{B C}}$ in Fig. 2) on which condensation does occur from the portion (e.g., $\overline{\mathrm{BA}}$ ) on which it does not.

It is instructive to note that the limiting process used to demonstrate condensation in the paragraph containing Eq. (25) corresponds to approaching the boundary ellipse in Fig. 2 along a horizontal path, with $\sigma_{m}>\frac{1}{2}$ and fixed, and $\sigma_{c}$ increasing until $f\left(\sigma_{c}, R\right)=0$. Having established the character of this proces,it is clear that the same limiting points could also be approached by fixing $\sigma_{c}$ and letting $\sigma_{m}$ increase until the ellipse is reached. We do not carry out the analysis associated with this exercise here. However, a numerical evaluation of the degree of condensation along this path is portrayed in Fig. 3, which shows the fraction of each of $E, H_{m}$, and $H_{c}$ in $k_{\text {min }}$ for fixed $N=4192$ and $\sigma_{c}=\frac{1}{2}$, while varying the value of $\sigma_{m}$. It is clear that $H_{m}$ becomes condensed most rapidly, $E$ is condensed at the slowest rate, with $H_{c}$ condensing at an intermediate rate.

Another interesting point on the minimum energy ellipse is $\left|\sigma_{m}\right|=1$ and $\sigma_{c}=0$, designated, as point " C " in Fig. 2. From (29) it follows that $\left|\boldsymbol{\beta}_{\theta}\right|=1$ and $\boldsymbol{\beta}_{\gamma}=0$. At this point we can see from (8a) that for $\beta \rightarrow \infty$ the kinetic energy vanishes, i.e., $R=0$. This point is usually referred to as the "Taylor state." ${ }^{17}$ Along the line $\sigma_{c}=0$ the kinetic energy spectrum is flat and the magnetic energy spectrum has a peak at $k_{\text {min }}$ whose magnitude is an increasing function of $\sigma_{m}$. Note that $R$ has its maximum value of 1 at $\sigma_{m}=0$ and decreases monotonically to its minimum value of 0 at $\left|\sigma_{m}\right| =1$.

## V. INFINITE PHASE SPACE DIMENSION LIMIT

In this section we consider the limit $N \rightarrow \infty$ while $E, H_{c}$, and $H_{m}$ remain fixed, which differs somewhat from the conventional thermodynamic limit. ${ }^{7}$ In the thermodynamic limit one lets the volume of the system and the particle number go to infinity, while maintaining a constant energy density. That is, a nonzero energy per degree of freedom is maintained in the limiting process. This leads to a total energy

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-05.jpg?height=625&width=792&top_left_y=1772&top_left_x=1046)
FIG. 3. Condensation of the three rugged invariant spectral to $k_{\text {min }}$ as the upper portion of the ellipse defined by (28) is approached by increasing $H_{m} / E$, for $N=4912$ and $\sigma_{c}=0.5$.

that diverges while the temperature remains finite, a limit not of relevance for the present purposes. The limiting process of interest here is the one for which the rugged invariants are held constant, with constant system periodicity length. At the same time the number of Fourier modes contributing to the dynamics is allowed to diverge, by increasing $k_{\text {max }}$. Since the values of wave vector act in the role of conventional "particles," one has, in this case, a limit of zero energy per particle, corresponding to divergent inverse temperatures. The two cases have in common that they investigate the statistical properties of the system as the number of phase space coordinates goes to infinity, while maintaining constant average spatial densities of the invariant "energies." Kraichnan ${ }^{5}$ has suggested that the infinite $\mathbf{k}$-space volume limit at constant energy is the limit of interest for hydrodynamic statistical ensembles, occupying a role analogous to the well known classical thermodynamic limit. Specifically, we will be able to draw inferences from this limit concerning tendencies for spectral quantities to be preferentially transferred to the long or short wavelengths. Such tendencies, in the equilibrium ensemble statistics, have often contributed to the body of evidence supporting related conjectures for dissipative, high Reynolds number turbulence, ${ }^{3,2,4,7}$ which also involves an extremely large number of dynamically involved Fourier modes.

The behavior of the inverse temperatures as $N \rightarrow \infty$ can be deduced from an examination of (13). A technical complication is that the behavior of $R$ as $N$ increase has yet to be determined. In a numerical evaluation of $R$ as a function of $N$, the result of which is illustrated in Fig. 4, it is seen that $R$ changes smoothly as $N$ increases. So it will be assumed that there are no discontinuous changes in $R$ as $N \rightarrow \infty$, and that $f\left(R, \sigma_{c}\right)$ does not vanish, provided that $\sigma_{c}$ and $\sigma_{m}$ are not near the borders of the parameter space where the inverse temperatures diverge (as in Sec. IV). After evaluation of the $N \rightarrow \infty$ limiting forms of $\beta_{\theta}$ and $\beta_{\gamma}$ it will be shown that these results are compatible with the finite $N$ limits obtained in Sec. IV as the parameter space boundaries are approached, e.g., by maximizing $\left|\sigma_{c}\right|$ for fixed $\left|\sigma_{m}\right|$. Thus the finite $N$ and infinite $N$ results are consistent.

First consider the case $H_{m}=0$ for which $\theta=0$. From

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-06.jpg?height=519&width=662&top_left_y=1891&top_left_x=200)
FIG. 4. Values of $E_{v} / E_{b}$ as a function of the normalized cross helicity. The finite $N$ curves approach the infinite mode limit. For each of the curves $\sigma_{m} =0.2$.

(13), with $f\left(R, \sigma_{c}\right)$ not near zero, $\beta \sim|\gamma| \sim N$ as $N \rightarrow \infty$. As in the finite $N$ case, the $E$ and $H_{c}$ spectra are given by (21), while $\beta_{\gamma}=-\sigma_{c}$. If it is assumed that $\left|\sigma_{c}\right|$ is not near 1 then neither is $\left|\beta_{\gamma}\right|$, so that $\beta^{2}-\frac{1}{4} \gamma^{2} \sim \beta^{2} \sim N^{2}$. It follows that as $N \rightarrow \infty,\langle E(\mathbf{k})\rangle$ and $\left\langle H_{c}(\mathbf{k})\right\rangle \rightarrow 0$ for every $\mathbf{k}$. Consequently, there is no condensation into $k_{\text {min }}$ of $E$ or $H_{c}$ for this case.

For the general case ( $H_{m}$ and $H_{c} \neq 0$, cf. Fig. 5), again avoiding parameter space (maximal $\sigma_{\mathrm{c}}$ ) boundaries, (13) implies that $\beta \sim|\theta| \sim|\gamma| \sim N$ as $N \rightarrow \infty$. To maintain finite values of $E, H_{c}$, and $H_{m}$ the inverse temperatures must diverge in a way such that (22) and (23) are satisfied. By inspection of (24c) the $k>k_{\text {min }}$ portion of the $H_{m}$ spectrum goes to 0 since $g(N) \sim N^{1 / 3}$, but, from (8e), it can be shown for each $\mathbf{k}$ having $|\mathbf{k}|=k_{\text {min }}$ that $\left\langle H_{m}(\mathbf{k})\right\rangle$ is finite and

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-06.jpg?height=1624&width=655&top_left_y=794&top_left_x=1086)
FIG. 5. Variation of the rugged invariant spectra as $N$ increases with total $E$, $H_{c}$, and $H_{m}$ fixed. For each plot $E=1, H_{c}=0.25$, and $H_{m}=0.3$ (a) Magnetic helicity spectra, (b) energy spectra, (c) cross helicity spectra.

$O(1)$. Thus $H_{m}$ condenses to the longest wavelength as $N \rightarrow \infty$. On the other hand, the high- $k$ contributions to the total $E$ and $H_{c}$, given by the expressions in (24a) and (24b), are finite and nonzero even though for each wave vector with $k>k_{\text {min }}$ one find that $\langle E(\mathbf{k})\rangle$ and $\left\langle H_{c}(\mathbf{k})\right\rangle \rightarrow 0$. However, by again inspecting ( 8 c ) and ( 8 d ) we see that the contributions to $\langle E(\mathbf{k})\rangle$ and $\left\langle H_{c}(\mathbf{k})\right\rangle$ at $k=k_{\text {min }}$ are nonzero. Although we have not yet established the fraction of the total $E$ and $H_{c}$ that reside in $k_{\text {min }}$, we can already see an important contrast to the $H_{m}=0$ case where $E\left(k_{\text {min }}\right)$ and $H_{c}\left(k_{\text {min }}\right)$ vanished as $N \rightarrow \infty$.

Expressions will now be found for $\beta_{r}$ and $\beta_{\theta}$. This will in turn allow expressions for the condensed fractions of $E$ and $H_{c}$ to be determined as well as some additional properties of the $N \rightarrow \infty$ spectra. For simplicity it will be assumed that $k_{\text {min }}=1$.

Since (22) is also a consequence of $N \rightarrow \infty$, (25) will follow for similar reasons. An equation for $\beta_{\gamma}$ can now be found by using (25) to eliminate $\beta_{\theta}$ from (12b). It is

$$
\begin{equation*}
\left|\sigma_{c}\right|+\beta_{\gamma}\left(1+\left|\sigma_{m}\right|\right)-\left|\sigma_{m}\right| \beta_{\gamma}^{3}=0 \tag{30}
\end{equation*}
$$

By numerical tests we have verified that the only solution to (30) to satisfies $\left|\beta_{r}\right|<1$ for $\left|\sigma_{m}\right|$ and $\left|\sigma_{c}\right| \leqslant 1$ is

$$
\begin{align*}
\beta_{\gamma}= & -\operatorname{sgn}\left(\sigma_{c}\right) \sqrt{\frac{1}{3}\left(1+1 /\left|\sigma_{m}\right|\right)} \\
& \times[\sqrt{3} \sin (\theta / 3)-\cos (\theta / 3)], \tag{31}
\end{align*}
$$

where $\theta$ is defined by

$$
\tan \theta=\sqrt{\left(4 / 27 \sigma_{c}^{2}\left|\sigma_{m}\right|\right)\left(\left|\sigma_{m}\right|+1\right)^{3}-1}
$$

One also needs to examine solutions to (30) when the parameter space boundary is approached. It is easily shown that the expressions in (29), previously obtained for finite $N$, are also solutions to (30) when $\sigma_{c}$ and $\sigma_{m}$ are chosen so that the system resides on the extremal ellipse given in (28). In addition, $\left|\beta_{\gamma}\right|=1$ solves (30) when $\left|\sigma_{c}\right|=1$, and the system resides on the line $\overline{\mathbf{A B}}$ in Fig. 2. Thus the infinite $N$ value of $\beta_{\gamma}$ and $\beta_{\theta}$ go over to the finite $N$ values in the limits where $\sigma_{c}$ and $\sigma_{m}$ become maximal. In detail, we find for large $N$, as $\left|\sigma_{c}\right| \rightarrow 1$ with $\left|\sigma_{m}\right|<\frac{1}{2}$, that $\beta \sim|\gamma| \sim N / f\left(R, \sigma_{c}\right)$ while $|\theta| \sim N$, and, when $\sigma_{c}$ and $\sigma_{m}$ satisfy (28) (i.e, on the ellipse in Fig. 2), that $\beta \sim|\gamma| \sim|\theta| \sim N / f\left(R, \sigma_{c}\right)$.

We are now in a position to determine, for general solutions to (30), the fractions of the rugged invariant spectra condensed to the longest wavelength, as function of the parameters $\sigma_{c}$ and $\sigma_{m}$. From (25) and (8), with $k_{\text {min }}=1$, we find that

$$
\begin{align*}
& E\left(k_{\min }\right) / E=\left(1+\beta_{\gamma}^{2}\right)\left|\sigma_{m}\right|,  \tag{32a}\\
& H_{c}\left(k_{\min }\right) / H_{c}=-2 \beta_{\gamma}\left|\sigma_{m}\right| / \sigma_{c},  \tag{32b}\\
& H_{m}\left(k_{\min }\right) / H_{m}=1 . \tag{32c}
\end{align*}
$$

To arrive at the expressions in (32) it is necessary to make use of three additional properties of the long wavelength modes, namely, that the $k_{\text {min }}$ modes are in state of maximal magnetic helicity, i.e.,

$$
\begin{equation*}
\left|H_{m}\left(k_{\min }\right)\right|=E_{b}\left(k_{\min }\right), \tag{33}
\end{equation*}
$$

which follows from (25), that the long wavelength velocity and magnetic fields are aligned, i.e.,

$$
\begin{equation*}
\left|H_{c}\left(k_{\min }\right)\right|=\sqrt{E_{b}\left(k_{\min }\right) E_{v}\left(k_{\min }\right)}, \tag{34}
\end{equation*}
$$

and that the ratio of kinetic to magnetic energy in $k_{\text {min }}$ modes is given by

$$
\begin{equation*}
E_{v}\left(k_{\min }\right) / E_{b}\left(k_{\min }\right)=\beta_{\gamma}^{2} . \tag{35}
\end{equation*}
$$

Note that the short wavelength ( $k>k_{\text {min }}$ ) spectra are characterized by equipartition of kinetic and magnetic energies,

$$
\begin{equation*}
E_{v}(K) / E_{b}(K)=1 \tag{36}
\end{equation*}
$$

while the normalized cross helicity in the short wavelengths is

$$
\begin{equation*}
2 H_{c}(K) / E(K)=-\beta_{\gamma} . \tag{37}
\end{equation*}
$$

Simple expressions for the global (including contributions from all wave numbers) quantities $R, \cos \theta$, and $H_{m} / E_{b}$ can also be found. They are

$$
\begin{align*}
& R=\left[1-\left|\sigma_{m}\right|\left(1-\beta_{\gamma}^{2}\right)\right] /\left[1+\left|\sigma_{m}\right|\left(1-\beta_{\gamma}^{2}\right)\right]  \tag{38a}\\
& \cos \Theta=-\beta_{\gamma} / \sqrt{R}  \tag{38b}\\
& H_{m} / E_{b}=\sigma_{m} /\left[1+\left|\sigma_{m}\right|\left(1-\beta_{\gamma}^{2}\right)\right] \tag{38c}
\end{align*}
$$

From an examination of (32) it can be seen that only when $H_{m} \neq 0$ are there nonzero fractions $E$ and $H_{c}$ occupying $k_{\text {min }}$. Moreover, it can be shown that (32a) and (32b) approach unity as the elliptical curve in the $\sigma_{c}$ and $\sigma_{m}$ parameter space defined by (28) is approached. Also, from (33) and (34) it is seen that the energy in $k_{\text {min }}$ is the minimum amount that need to be present to give the appropriate $H_{c}\left(k_{\text {min }}\right)$ and $H_{m}\left(k_{\text {min }}\right)$. The condensed portion of the $H_{c}$ spectrum behaves in a manner similar to that of the condensed $H_{m}$ spectrum in that both are determined by the equilibrium distribution. No kinematic constraints that require either to have any portion of their spectra condense to $k_{\text {min }}$ were found, except, of course, of the parameter space boundary. This is in contrast to the energy that occupies $k_{\text {min }}$, which must reside in the longest wavelength modes to kinematically account for $H_{c}\left(k_{\min }\right)$ and $H_{m}\left(k_{\min }\right)$, and we have seen that $E\left(k_{\text {min }}\right)$ takes on the minimum value satisfying that constraint. This suggests that, when $H_{m} \neq 0$, both $H_{c}$ and $H_{m}$ have an affinity for the long wavelengths, though this tendency of $H_{c}$ depends upon the condensation of $H_{m}$ and is generally incomplete. On the other hand, $E$ prefers to be spread uniformly over the spectrum. This "weaker" attraction of the $H_{c}$ spectrum to $k_{\text {min }}$ is what has been referred to as partial condensation in earlier sections.

## VI. NUMERICAL SIMULATIONS

Numerical simulations of (1) were performed using a Galerkin spectral method code that exactly conserves $E$, $H_{m}$, and $H_{c}$, apart from roundoff and time integration errors. Here we present results for a Galerkin simulation of a system with $N=124$, having 496 independent real degrees of freedom and $k_{\text {max }}^{2}=12$. Based on comparisons of spectral moments computed from the canonical ensemble, the microcanonical ensemble, and time averages of low truncations of 2-D hydrodynamics, ${ }^{18}$ the number of modes retained here might be expected to give a reasonable level of agreement with the absolute equilibrium rugged invariant spectra.

The initial conditions were chosen with flat $E$ and $H_{c}$ spectra and an $H_{m}$ spectrum $\propto 1 / k$. All undetermined phases were randomly chosen. Time integrations were performed out to 1000 eddy turnover times using a time step $\Delta t=0.01$. This was sufficient to allow the system to go through many transient fluctuations so that adequate timeaveraged spectra are obtained. The integration error for the energy after 1000 turnover times was $\sim 10^{-4}$.

From Fig. 6 it can be seen that there is good agreement between simulated and theoretical values of the time-averaged $\langle E(k)\rangle,\left\langle H_{m}(k)\right\rangle$, and $\left\langle H_{c}(k)\right\rangle$ spectra. This sup-

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-08.jpg?height=1671&width=684&top_left_y=623&top_left_x=187)
FIG. 6. Comparison of time-averaged simulated rugged invariant spectra and ensemble-averaged spectra, for a Galerkin simulation with $N=124$, as described in Sec. VI. The squares (solid line) represent the time-averaged (equilibrium theory) spectra. For this run $E=1, H_{c}=0.2$, and $H_{m}=0.2$. (a) Total energy spectra, (b) cross helicity spectra, (c) magnetic helicity spectra.

ports the belief that the only quantities ruggedly conserved by Galerkin representations of (1) are the energy, cross helicity, and magnetic helicity. Conclusions concerning the ergodicity of the solutions on the phase space hypersurfaces defined by these quantities [cf. Eq. (4)] must be drawn with greater caution. For example, there is some recent evidence ${ }^{16}$ in 2-D MHD computations that subtle deviations from ergodicity may be realized even for very long time averages. However, evidence such as Fig. 6 points to the suggestion that the solutions may be at least approximately treated as weakly ergodic in the sense that second-order moments (rugged invariant spectra) are accurately given by the ensemble predictions. Fourth-order moments may require a microcanonical treatment. ${ }^{18}$

## VII. DISCUSSION

In the previous sections we have described the statistical properties of ideal, inviscid three-dimensional MHD in periodic geometry, extending the work of Frisch et al. ${ }^{3}$ and Montgomery, Turner, and Vahala. ${ }^{4}$ Our approach is entirely based on the absolute equilibrium ensemble method of Lee ${ }^{15}$ and Kraichnan, ${ }^{1,5,6,8}$ which has previously been used to develop inverse cascade ${ }^{3}$ and selective decay conjectures ${ }^{4,13}$ for three-dimensional MHD and to extensively study the statistical dynamics of two-dimensional MHD. ${ }^{2}$ Our main extension is to elaborate on the effects of cross helicity $H_{c}$ in the equilibrium static, leading to a number of conclusions regarding the behavior of the full set of three known rugged invariants, $E, H_{m}$, and $H_{c}$ and their spectra, as well as several general conclusions, apparently unnoticed previously, that have implications for arbitrary values of the invariants.

Our emphasis has been on the spectral distribution of the invariants over wave number, dependent upon the invariant ratios $H_{c} / E$ and $H_{m} / E$ as well as upon the number of Fourier modes in the system $N$. Of special interest were the limits associated with extremal values of the invariant ratios and the infinite phase space dimension ( $N \rightarrow \infty$ ) limit, which have appealing, if not rigorous, relationships to dissipative turbulence. ${ }^{5,8}$ Appearance of spectral peaks at the longest wavelength in the equilibrium statistics is a distinctive feature of 3-D MHD and other systems with more than one rugged invariant, and one that plays an important role in establishing the connection to realistic dissipative turbulence.

One often speaks of a fluid quantity as experiencing condensation if in certain limits, especially the zero temperature limit, it resides entirely in modes of a particular wavelength. An example of this phenomenon, noted here and in previous work, ${ }^{3}$ is the condensation of magnetic helicity to the longest wavelength modes, in both the $N \rightarrow \infty$ (Sec.V) and maximal $H_{m} / E$ (Sec. IV) limits. Interpreted as an indicator of the time-asymptotic or average tendencies of the nonlinear MHD couplings to transfer $H_{m}$ to the longest allowed scales, the equilibrium condensation of $H_{m}$ suggests that $H_{m}$ is "back-transferred" in wave number in more general circumstances, including driven or decaying dissipative turbulence. This extrapolation of ensemble properties has motivated inverse cascade ${ }^{1-3}$ and selective decay ${ }^{4}$ hypotheses. For pur-
poses of the present discussion, we refer to the above-described behavior of $H_{m}$ as complete condensation. Analogous behavior is experienced by the energy in 2-D Na -vier-Stokes flow. ${ }^{5}$

The role of the cross helicity in MHD turbulence has been debated for some time, with regard to both its spectral transfer characteristics and its influence on magnetic spectral back-transfer. For example, in two dimensions the pure form of the dynamic alignment conjecture ${ }^{19-20}$ predicts an increase of $2 H_{c} / E$, while the selective decay hypothesis ${ }^{4,14}$ indicates relative growth of the magnetic invariant (increase of $A / E$ in two dimensions, $H_{m} / E$ in three dimensions). The mutual exclusion of the predicted final states of these processes had led to a study of their inherent dynamical competition in two dimensions. ${ }^{21}$ The balance achieved between these tendencies in dissipative turbulence (e.g., Ref. 14) depends upon the strength of spectral transfer of $H_{c}$ to both higher and lower wave number, relative to the corresponding transfer rates of the other rugged invariants. To a certain extend one may attempt to address these questions through the equilibrium ensemble theory, by comparison of the spectral forms of $H_{m}, H_{c}$, and $E$, and, in particular, by examining the relative tendencies of the invariants to peak or condense in the longest wavelength modes.

Evidence has been presented in the present work that the cross helicity undergoes a condensation to the longest wavelengths. It is a partial condensation, in the sense that the entirety of the system $H_{c}$ generally does not appear at the lowest wave number. However, the strength of the condensation effect is also not minimal, indicating a tendency for back-transfer of $H_{c}$ that may have broader dynamical implications.

Consider the following heuristic construction of the equilibrium spectrum in the $N \rightarrow \infty$ limit. First, place the entirety of $H_{m}$ and a concomitant amount of $E_{b}$ into $k_{\text {min }}$ in a state of maximal $H_{m}$. We initially spread the remaining energy $E-k_{\text {min }} H_{m}$ equally over all modes with wave number $k>k_{\text {min }}$. We add cross helicity to the ensemble spectrum according to the "rule" given in Eq. (11), that $H_{c}(k) / E_{b}(k)$ is a constant independent of wave number, the constant being determined by the specified total $H_{c}, H_{m}$, and $E$. Thus we do not expect, in general, that the entirety of the cross helicity will reside in the longest scales (i.e., no complete condensation), but $H_{c}(k)$ will have a strong peak at $k_{\text {min }}$ (i.e., partial condensation) when $E_{b}(k)$ does, the latter in the minimal amount necessary to satisfy the kinematic constraint imposed by the magnetic helicity condensation. We now note that a nonzero $E_{v}\left(k_{\text {min }}\right)$ is needed in $k_{\text {min }}$, since $H_{c}(k) \leqslant \sqrt{E_{v}(k) E_{b}(k)}$, requiring that we move a certain amount of energy out of the $k>k_{\text {min }}$ reservoir at high wave number. Figure 7 illustrates how kinetic energy is forced to reside in the longest wavelength at equilibrium. The effect requires nonzero $H_{m}$ and is strongly dependent on the amount of $H_{c}$ present. In conjunction with moving the requisite amount of kinetic energy of $k_{\text {min }}$, we must rearrange the high- $k$ energies to maintain equipartition of $E_{b}(k)$ and $E_{v}(k)$. The above procedure is completely equivalent to the exact $N \rightarrow \infty$ ensemble spectrum described in Sec. V. To quantify the procedure while maintaining constant total $E$,

![](https://cdn.mathpix.com/cropped/2025_11_22_9966b54b1d10e0a3bf06g-09.jpg?height=510&width=622&top_left_y=100&top_left_x=1062)
FIG. 7. The tendency for increasing cross helicity to bring greater amounts of kinetic energy into the large scales is illustrated by plotting the kinetic energy in the longest wavelength modes (normalized by the total energy) as a function of the normalized magnetic helicity, for values of the normalized cross helicity $\sigma_{m}=0.001,0.5$, and 0.95 . The curves are labeled by their $\sigma_{c}$ value. These results are for a large $N$, and are virtually indistinguishable from the $N \rightarrow \infty$ case.

$H_{c}$, and $H_{m}$ one arrives at a cubic constraint equation analogous to (30).

An important point to emphasize (see the discussion following Eq. (32)[ is that equilibrium establishes a values of $E_{v}\left(k_{\text {min }}\right)$ that is minimal for the specified $H_{c}\left(k_{\text {min }}\right)$. This is a consequence of the fact that the velocity and magnetic fields in $k_{\text {min }}$ are perfectly aligned, in the sense that $\cos \Theta\left(k_{\text {min }}\right) \equiv H_{c}\left(k_{\text {min }}\right) / \sqrt{E_{b}\left(k_{\text {min }}\right) E_{v}\left(k_{\text {min }}\right)}=1$, although $\sigma_{c}\left(k_{\text {min }}\right) \equiv 2 H_{c}\left(k_{\text {min }}\right) / E\left(k_{\text {min }}\right)$ is not maximal, since the energy in $k_{\text {min }}$ is not necessarily equipartitioned. On the other hand, one cannot argue that the $E_{v}\left(k_{\text {min }}\right)$ is maximal relative to $H_{c}\left(k_{\text {min }}\right)$, since $E_{v}\left(k_{\text {min }}\right)$ could be increased beyond the value found without influencing $H_{c}\left(k_{\text {min }}\right)$. Thus we see that the condensation of $H_{c}$ is weaker than the complete condensation of $H_{m}$, but it is stronger than the condensation of $E$. In fact, the amount of $E$ in $k_{\text {min }}$ is the minimum amount needed to account for the dual constraints of a fixed amount of $H_{m}\left(k_{\text {min }}\right)$ and $H_{c}\left(k_{\text {min }}\right)$.

We are led to the conclusion that the local peaking of $E$ at $k_{\text {min }}$ for 3-D MHD is analogous to the similar behavior of enstrophy at $k_{\text {min }}$ in 2-D Navier-Stokes flow. ${ }^{1}$ In the latter case the amount appearing at the longest wavelengths is the amount needed to kinematically satisfy other independent dynamical constraints. Our analysis has indicated that there are no kinematic constraints that determine the condensed amount of $H_{c}$ or $H_{m}$. The intermediate strength of the tendency for condensation of $H_{c}$ is easily seen. A stronger effect would be realized if the condensation were complete. A weaker condensation would be obtained if, for example, the high- $k$ cross helicity were maximal [see Eq. (35b)]. The actual strength of the cross helicity condensation, indicated by the ensemble value of $H_{c}\left(k_{\text {min }}\right)$, appears to be solely determined by the maximum entropy condition underlying the equilibrium spectrum itself, and thus is interpreted a product of the statistical equilibrium. Another important feature of the partial condensation of $H_{c}$ is that it occurs entirely as a result of the complete condensation of magnetic helicity, which determines $E_{b}\left(k_{\text {min }}\right)$, and thus $H_{c}\left(k_{\text {min }}\right)$ through the
crucial relation (11). Consequently, we see that the partial condensation of $H_{c}$ is an important feature of the equilibrium when there is condensation of magnetic helicity. We suggest that, in the more general circumstance of dissipative MHD turbulence, whenever there is back-transfer of magnetic helicity, there is a weaker but possibly significant tendency for back-transfer of cross helicity.

As a final note we recall that the inequality $R \leqslant 1$ derived in Sec. III implies that in the absence of dissipation there are no time-asymptotic 3-D MHD states that are kinetic energy dominated. This could be relevant to the turbulent dynamo problem in that the time-averaged exchange of kinetic and magnetic energy by the nonlinear terms is such that it produces states that are dominated by magnetic energy. Consider an initial condition with a weak magnetic field, i.e., $R \gg 1$. This initial state will lie near the origin of the $\sigma_{m}$ and $\sigma_{c}$ parameter space. In Sec. IV it was shown that, to reach absolute equilibrium, the magnetic energy must grow until at least equipartitioning with the kinetic energy is achieved. Moreover, numerical evidence such as that given in Sec. VI supports the belief that arbitrary initial condition will relax toward this absolute equilibrium property. When dissipation is added to the system, the cascade of energy to high $k$ will compete with the process that energetically equipartitions the system. As pointed out by Kraichnan and Nagarajan, ${ }^{22}$ both processes occur on times that are the same order of magnitude, an eddy turnover time. Thus qualitative theories are incapable of predicting which process will have the greater influence. Consequently, the fact that $R \leqslant 1$ for absolute equilibrium systems by itself is insufficient to prove the existence of the turbulent dynamo.

## ACKNOWLEDGMENTS

Some of our computational resources were provided by the National Science Foundation San Diego Supercomputing Center.

This research was supported by the National Science Foundation, Grant No. ATM8913627 and by NASA, under Grant No. NGT-50338 and the Space Physics Theory Program. TS is supported by the NASA Graduate Student Researchers Program.
${ }^{1}$ R. H. Kraichnan, Phys. Fluids 10, 1457 (1967).
${ }^{2}$ D. Fyfe and D. Montgomery, J. Plasma Phys. 16, 181 (1976); D. Fyfe, D. Montgomery, and G. Joyce, J. Plasma Phys. 17, 369 (1977).
${ }^{3}$ U. Frisch, A. Pouquet, J. Léorat, and A. Mazure, J. Fluid Mech. 68, 769 (1975).
${ }^{4}$ D. Montgomery, L. Turner, and G. Vahala, Phys. Fluids 21, 757 (1978).
${ }^{5}$ R. H. Kraichnan, J. Fluid Mech. 67, 155 (1974).
${ }^{6}$ R.H. Kraichnan and D. Montgomery, Rep. Prog. Phys. 43, 547 (1980).
${ }^{7}$ C. E. Seyler, Y. Salu, D. Montgomery, and G. Knorr, Phys. Fluids 18, 803 (1975).
${ }^{8}$ R. H. Kraichnan and S. Chen, Physica D 37, 160 (1989).
${ }^{9}$ M. C. Kelly and P. M. Kintner, J. Astrophys. 220, 339 (1978).
${ }^{10}$ D. Fyfe and D. Montgomery, Phys. Fluids 21, 316 (1978).
${ }^{11}$ A. Hasegawa and K. Mima, Phys. Fluids 21, 87 (1978).
${ }^{12}$ D. Fyfe and D. Montgomery, Phys. Fluids 22, 246 (1979).
${ }^{13}$ W. H. Matthaeus and D. Montgomery, Ann. N.Y. Acad. Sci. 357, 203 (1980).
${ }^{14}$ A. C. Ting, W. H. Matthaeus, and D. Montgomery, Phys. Fluids 29, 3261 (1986).
${ }^{15}$ T. D. Lee, Quart. Appl. Math. 10, 69 (1952).
${ }^{16}$ J. V. Shebalin, Ph.D thesis, College of William and Mary, 1989.
${ }^{17}$ J. B. Taylor, Phys. Rev. Lett. 33, 1139 (1974).
${ }^{18}$ L. C. Kells and S. A. Orszag, Phys. Fluids 21, 162 (1978).
${ }^{19}$ M. Dobrowolny, A. Mangeney, and P. L. Veltri, Phys. Rev. Lett. 45, 144 (1988).
${ }^{20}$ W. H. Matthaeus, M. Goldstein, and D. Montgomery, Phys. Rev. Lett. 51, 1484 (1983).
${ }^{21}$ W. H. Matthaeus and D. Montgomery, in Statistical Physics and Chaos in Fusion Plasmas, edited by C. W. Horton and L. E. Riechel (Wiley, New York, 1984), pp. 285-291.
${ }^{22}$ R. H. Kraichnan and S. Nagarajan, Phys. Fluids 10, 859 (1967).

