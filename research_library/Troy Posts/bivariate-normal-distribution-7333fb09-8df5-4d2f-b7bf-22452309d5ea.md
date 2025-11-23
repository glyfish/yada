## Bivariate Normal Distribution

## Nov 18, 2018 • Troy Stribling

The Bivariate Normal Distribution is an often used multivariable distribution because it provides a simple model of correlated random variables. Here it is derived by application of a linear transformation and a multivariate change of variables to the distribution of two independent unit normal, Normal $(0,1)$, random variables. To provide background a general expression for change of variables of a bivariate integral is discussed and then used to obtain the Bivariate Normal Distribution. The Marginal and Conditional distributions are next computed and used to evaluate the first and seconds moments, correlation coefficient and conditional expectation and conditional variance. Finally, the variation in the shape of the distribution and transformation as the distribution parameters are varied is discussed.

## Bivariate Change of Variables

Consider the PDF of a single variable, $f(x)$, and the transformation, $x=x(y)$ which is assumed monotonically increasing. The PDF of the transformed variable is given by,

$$
g(y)=f(x(y)) \frac{d x}{d y} .
$$

This result follows by performing a change of variables to the CDF,

$$
\begin{aligned}
P(X \leq x) & =\int_{-\infty}^{x} f(w) d w \\
& =\int_{-\infty}^{y} f(x(w)) \frac{d x}{d w} d w \\
& =P(Y \leq y)
\end{aligned}
$$

where use was made of,

$$
d x=\frac{d x}{d y} d y
$$

The $d x / d y$ term scales $d y$ appropriately to conserve the differential length. In two dimensions a similar but more complicated thing happens.

Consider the bivariate PDF, $f(x, y)$, with CDF,

$$
\begin{equation*}
P(\{X, Y\} \in A)=\int_{A} f(x, y) d A \tag{1}
\end{equation*}
$$

which defines an integration over a region computing the probability that $X$ and $Y$ are both in the
region $A$. The figure below provides an illustration for a Cartesian Coordinate System where $d A=d x d y$.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-02.jpg?height=1025&width=1086&top_left_y=458&top_left_x=487)

To go further a geometric result relating the Cross Product of two vectors to the area of the parallelogram enclosed by the vectors is needed. This topic is discussed in the following section.

## Cross Product as Area

Consider two vectors $\mathbf{A}$ and $\mathbf{B}$ separated by an angle $\theta$ and rotated by and angle $\phi$ as shown in the following figure.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-03.jpg?height=1256&width=1253&top_left_y=140&top_left_x=436)

The vector components projected along the $\mathbf{x}$ and $\mathbf{y}$ unit vectors is given by,

$$
\begin{aligned}
& \mathbf{A}=A_{x} \mathbf{x}+A_{y} \mathbf{y} \\
& \mathbf{B}=B_{x} \mathbf{x}+B_{y} \mathbf{y}
\end{aligned}
$$

where,

$$
\begin{align*}
& A_{x}=|\mathbf{A}| \cos \phi \\
& A_{y}=|\mathbf{A}| \sin \phi \\
& B_{x}=|\mathbf{B}| \cos (\phi+\theta)  \tag{2}\\
& B_{y}=|\mathbf{B}| \sin (\phi+\theta) .
\end{align*}
$$

The cross product of two vectors is another vector perpendicular to both vectors. For the figure above, that direction is perpendicular to the plane of the page, call it $\mathbf{z}$. The cross product is then defined by the determinate computed from the components of the two vectors and projected along $\mathbf{z}$,

$$
\begin{align*}
\mathbf{A} \times \mathbf{B} & =\left|\begin{array}{ll}
A_{x} & A_{y} \\
B_{x} & B_{y}
\end{array}\right| \mathbf{z}  \tag{3}\\
& =\left(A_{x} B_{y}-A_{y} B_{x}\right) \mathbf{z}
\end{align*}
$$

Substituting equation (2) into (3) and making use of,

$$
\begin{gathered}
\sin (\theta+\phi)=\sin \theta \cos \phi+\cos \theta \sin \phi \\
\cos (\theta+\phi)=\cos \theta \cos \phi-\sin \theta \sin \phi \\
\sin ^{2} \phi+\cos ^{2} \phi=1
\end{gathered}
$$

results in,

$$
\begin{aligned}
|\mathbf{A} \times \mathbf{B}| & =\left|A_{x} B_{y}-B_{x} A_{y}\right| \\
& =|\mathbf{A}||\mathbf{B}|[\cos \phi \sin (\phi+\theta)-\sin \phi \cos (\phi+\theta)] \\
& =|\mathbf{A}||\mathbf{B}|\left(\cos ^{2} \phi \sin \theta+\sin \phi \cos \phi \cos \theta-\sin \phi \cos \phi \cos \theta+\sin ^{2} \phi \sin \theta\right) \\
& =|\mathbf{A}||\mathbf{B}| \sin \theta\left(\cos ^{2} \phi+\sin ^{2} \phi\right) \\
& =|\mathbf{A}||\mathbf{B}| \sin \theta,
\end{aligned}
$$

which is the area of the parallelogram indicated by orange in the figure above. $\sin \theta$ can be assumed positive since $\theta$ can always be chosen such that $0 \leq \theta \leq \pi$.

## Bivariate Jacobian

Consider the following coordinate transformation between two coordinate systems defined by the variables ( $x, y$ ) and ( $u, v$ ),

$$
\begin{align*}
& x=x(u, v) \\
& y=y(u, v) . \tag{4}
\end{align*}
$$

applied to the integral,

$$
\int_{A} f(x, y) d x d y
$$

where $A$ is an arbitrary area in ( $x, y$ ) coordinates. The following figure shows how area elements transform between $(u, v)$ coordinates and $(x, y)$ coordinates when equation $(4)$ is applied. The left side of the figure shows the $(u, v)$ Cartesian Coordinate System. In this system vertical lines of constant $u$ are colored orange and horizontal lines of constant $v$ blue. The right side of the figure illustrates how equation (4) maps lines of constant $u$ and $v$ onto $(x, y)$ coordinates. The lines of constant $u$ and $v$ can be curved and not aligned with the $(x, y)$ Cartesian coordinates as shown in the figure. The transformed $(u, v)$ coordinates in this case are Curvilinear.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-05.jpg?height=839&width=1348&top_left_y=238&top_left_x=357)

Consider the differential area elements indicated by orange in the figure. In the $(u, v)$ Cartesian coordinates the differential area element is given by $d A=d u d v$ but in ( $x, y$ ) coordinates differentials defining the area are not orthogonal so the element is distorted. In the infinitesimal limit it will become a parallelogram with area given by the cross product of $d \mathbf{X}$ and $d \mathbf{Y}$ which are tangent vectors to the curves of constant $v$ and $u$ respectively at the origin point of the vectors. To compute the cross product expressions for the differentials are required. The components of the differentials are computed from transformation (4) by assuming $v$ is constant for $d \mathbf{X}$ and $u$ is constant for $d \mathbf{Y}$. It follows that,

$$
\begin{aligned}
d \mathbf{X} & =\frac{\partial x}{\partial u} d u \mathbf{x}+\frac{\partial y}{\partial u} d u \mathbf{y} \\
d \mathbf{Y} & =\frac{\partial x}{\partial v} d v \mathbf{x}+\frac{\partial y}{\partial v} d v \mathbf{y}
\end{aligned}
$$

The cross product of the differentials above is given by,

$$
\begin{aligned}
d \mathbf{X} \times d \mathbf{Y} & =\left|\begin{array}{ll}
\frac{\partial x}{\partial u} d u & \frac{\partial y}{\partial u} d u \\
\frac{\partial x}{\partial v} d v & \frac{\partial y}{\partial v} d v
\end{array}\right| \mathbf{z} \\
& =\left|\begin{array}{ll}
\frac{\partial x}{\partial u} & \frac{\partial y}{\partial u} \\
\frac{\partial x}{\partial v} & \frac{\partial y}{\partial v}
\end{array}\right| d u d v \mathbf{z} \\
& =\left(\frac{\partial x}{\partial u} \frac{\partial y}{\partial v}-\frac{\partial y}{\partial u} \frac{\partial x}{\partial v}\right) d u d v \mathbf{z}
\end{aligned}
$$

The bivariate Jacobian is defined by,

$$
\begin{aligned}
|J| & =\left|\frac{\partial(x, y)}{\partial(u, v)}\right| \\
& =\left|\begin{array}{ll}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{array}\right| \\
& =\left(\frac{\partial x}{\partial u} \frac{\partial y}{\partial v}-\frac{\partial y}{\partial u} \frac{\partial x}{\partial v}\right) .
\end{aligned}
$$

In general the determinate of a matrix equals the determinate of the transpose of the matrix. It follows that the area element in $(u, v)$ coordinates is given by,

$$
d A=|d \mathbf{X} \times d \mathbf{Y}|=|J| d u d v
$$

$|J|$ will scale the differential area $d u d v$ by the amount required by the transform to conserve the area in a manner similar to that seen for a single variable length is conserved.

Finally the transform of the bivariate integral in equation (1) is given by,

$$
\int_{A} f(x, y) d x d y=\int_{A^{\prime}} f(x(u, v), y(u, v))|J| d u d v
$$

where $A^{\prime}$ is the region obtained by applying (4) to $A$.

## Bivariate Normal Distribution

The Bivariate Normal Distribution with random variables $U$ and $V$ is obtained by applying the following linear transformation to two independent $\mathbf{N o r m a l}(0,1)$ random variables $X$ and $Y$,

$$
\binom{U-\mu_{u}}{V-\mu_{v}}=\left(\begin{array}{cc}
\sigma_{u} & 0  \tag{5}\\
\sigma_{v} \gamma & \sigma_{v} \sqrt{1-\gamma^{2}}
\end{array}\right)\binom{X}{Y},
$$

where $\mu_{u}, \mu_{v}, \sigma_{u}, \sigma_{v}$ and $\gamma$ are scalar constants named in anticipation of being the mean, standard deviation and correlation coefficient of the distribution.

An equation for $X$ and $Y$ in terms $U$ and $V$ is obtained by inverting the transformation matrix,

$$
\binom{X}{Y}=\frac{1}{\sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}}\left(\begin{array}{cc}
\sigma_{v} \sqrt{1-\gamma^{2}} & 0  \tag{6}\\
-\sigma_{v} \gamma & \sigma_{u}
\end{array}\right)\binom{U-\mu_{u}}{V-\mu_{v}},
$$

where it is assumed that $\gamma^{2}=1 /$. The distribution for $X$ and $Y$ is found by making use of the assumption that they are independent $\operatorname{Normal}(0,1)$, namely,

$$
\begin{equation*}
f(x, y)=f(x) f(y)=\frac{1}{2 \pi} e^{-\left(x^{2}+y^{2}\right) / 2} \tag{7}
\end{equation*}
$$

In the previous section it was shown that for transformation,

$$
\begin{aligned}
& x=x(u, v) \\
& y=y(u, v),
\end{aligned}
$$

the transformed PDF is given by,

$$
\begin{equation*}
g(u, v)=|J| f(x(u, v), y(u, v)) \tag{8}
\end{equation*}
$$

where $|J|$ is the Jacobian. The transformations $x(u, v)$ and $y(u, v)$ can be determined from equation (6),

$$
\begin{align*}
& x(u, v)=\frac{\left(u-\mu_{u}\right)}{\sigma_{u}} \\
& y(u, v)=\frac{1}{\sqrt{1-\gamma^{2}}}\left[\frac{1}{\sigma_{v}}\left(v-\mu_{v}\right)-\frac{\gamma}{\sigma_{u}}\left(u-\mu_{u}\right)\right] . \tag{9}
\end{align*}
$$

It follows that the Jacobian is given by,

$$
\begin{equation*}
|J|=\frac{1}{\sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} \tag{10}
\end{equation*}
$$

With the goal of keeping things simple in the evaluation of equation (8) the exponential argument term of equation (7), $x^{2}+y^{2}$, will first be considered. Use of the expressions for $x(u, v)$ and $y(u, v)$ from equation (9) gives,

$$
\begin{align*}
x^{2}+y^{2} & =[x(u, v)]^{2}+[y(u, v)]^{2} \\
& =\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{1}{1-\gamma^{2}}\left[\frac{1}{\sigma_{v}}\left(v-\mu_{v}\right)-\frac{\gamma}{\sigma_{u}}\left(u-\mu_{u}\right)\right]^{2} \\
& =\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\gamma^{2}}{1-\gamma^{2}} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{1}{1-\gamma^{2}} \frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-\frac{2 \gamma}{1-\gamma^{2}} \frac{\left(u-\mu_{u}\right)\left(v-\mu_{v}\right)}{\sigma_{u} \sigma_{v}}  \tag{11}\\
& =\frac{1}{1-\gamma^{2}}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}\left(1-\gamma^{2}+\gamma^{2}\right) \frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right] \\
& =\frac{1}{1-\gamma^{2}}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right] .
\end{align*}
$$

The first step expands the right most squared term and the last two steps aggregate ( $u-\mu_{u}$ ) and $\left(v-\mu_{v}\right)$ terms. The Bivariate Normal PDF follows by inserting equations (10) and (11) into equation (8),

$$
\begin{align*}
g(u, v) & =|J| f(x(u, v), y(u, v)) \\
& =\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]} \tag{12}
\end{align*}
$$

Extension of transform ( 5 ) to more than two dimensions is not clear. The following section will describe a form of the transformation that makes this more apparent.

## Matrix Form of Bivariate Normal Distribution

A matrix form for the Bivariate Normal Distribution PDF can be constructed that scales to higher dimensions. Here the version for two variables is compared with the results of the previous section and followed by a discussion of extension to an arbitrary number of dimensions. To begin consider the column vectors,

$$
\begin{gather*}
Y=\binom{y_{1}}{y_{2}} \mu=\binom{\mu_{1}}{\mu_{2}} \\
P=\left(\begin{array}{cc}
\sigma_{1}^{2} & \gamma \sigma_{1} \sigma_{2} \\
\gamma \sigma_{1} \sigma_{2} & \sigma_{2}^{2}
\end{array}\right) . \tag{13}
\end{gather*}
$$

$Y$ is the column vector of Bivariate Normal Random variables, $\mu$ the column vector of mean values and $P$ is called the Covariance Matrix. To continue the inverse of the covariance matrix and its determinate are required. The inverse is given by,

$$
P^{-1}=\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} \\
-\gamma \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right),
$$

and the determinate is,

$$
|P|=\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right) .
$$

Next, consider the product, where $(Y-\mu)^{T}$ is the transpose of $(Y-\mu)$,

$$
(Y-\mu)^{T} P^{-1}(Y-\mu) .
$$

The two rightmost terms evaluate to,

$$
\begin{aligned}
P^{-1}(Y-\mu) & =\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(\begin{array}{cc}
\sigma_{2}^{2} & -\gamma \sigma_{1} \sigma_{2} \\
-\gamma \sigma_{1} \sigma_{2} & \sigma_{1}^{2}
\end{array}\right)\binom{y_{1}-\mu_{1}}{y_{2}-\mu_{2}} \\
& =\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\binom{\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\gamma \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)}{-\gamma \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)} .
\end{aligned}
$$

Continuing the evaluation by including the left most term gives,

$$
\begin{aligned}
(Y-\mu)^{T} P^{-1}(Y-\mu) & =\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left(\begin{array}{ll}
y_{1}-\mu_{1} & \left.y_{2}-\mu_{2}\right)\binom{\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\gamma \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)}{-\gamma \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)} \\
& =\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left\{\left[\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)-\gamma \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)\right]\left(y_{1}-\mu_{1}\right)+\left[\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)-\gamma \sigma_{1} \sigma_{2}\left(y_{1}-\mu_{1}\right)\right]\right. \\
& =\frac{1}{\sigma_{1}^{2} \sigma_{2}^{2}\left(1-\gamma^{2}\right)}\left[\sigma_{2}^{2}\left(y_{1}-\mu_{1}\right)^{2}+\sigma_{1}^{2}\left(y_{2}-\mu_{2}\right)^{2}-2 \gamma \sigma_{1} \sigma_{2}\left(y_{2}-\mu_{2}\right)\left(y_{1}-\mu_{1}\right)\right] \\
& =\frac{1}{1-\gamma^{2}}\left[\frac{\left(y_{1}-\mu_{1}\right)^{2}}{\sigma_{1}^{2}}+\frac{\left(y_{2}-\mu_{2}\right)^{2}}{\sigma_{2}^{2}}-2 \gamma \frac{\left(y_{1}-\mu_{1}\right)}{\sigma_{1}} \frac{\left(y_{2}-\mu_{2}\right)}{\sigma_{2}}\right] .
\end{array} .\right.
\end{aligned}
$$

Which is the same as obtained using transform ( 9 ) in the previous section. Comparing the expression for $|P|$ with equation (12) gives,

$$
|J|=\frac{1}{\sqrt{|P|}}
$$

Putting things together produces the desired result,

$$
\begin{aligned}
g(u, v) & =|J| f(x(u, v), y(u, v)) \\
& =\frac{1}{2 \pi \sqrt{|P|}} e^{\left[-\frac{1}{2}(Y-\mu)^{T} P^{-1}(Y-\mu)\right]} .
\end{aligned}
$$

To extend to an arbitrary number of dimensions, $n$, the covariance matrix defined in equation (13) needs to written in a more general form,

$$
P_{i j}=\operatorname{Cov}\left(Y_{i}, Y_{j}\right) .
$$

After updating the normalization factor to account for the product of $n \mathbf{N o r m a l}(\mathbf{0}, \mathbf{1})$ distributions the Multivariate Normal PDF becomes,

$$
\begin{aligned}
g(u, v) & =|J| f(x(u, v), y(u, v)) \\
& =\frac{1}{(2 \pi)^{n / 2} \sqrt{|P|}} e^{\left[-\frac{1}{2}(Y-\mu)^{T} P^{-1}(Y-\mu)\right]}
\end{aligned}
$$

To determine the linear transformation, analogous to equation $(9), P_{i j}$ is factored using Cholesky Decomposition.

In a following section it will be shown that for two variables,

$$
\operatorname{Cov}\left(Y_{i}, Y_{j}\right)=\left\{\begin{array}{ll}
\gamma \sigma_{i} \sigma_{j} & i=\gamma \\
\sigma_{i}^{2} & i=j
\end{array} .\right.
$$

which is equivalent to equation (13).

## Bivariate Normal Distribution Properties

The previous sections discussed the derivation of the Bivariate Normal random variables as linear combinations of independent unit normal random variables. Linear combinations were constructed by application of a linear transformation that includes five independent parameters. In this section interpretations of the parameters are provided and variation in the distribution as the parameters are varied is described. First, the Marginal Distributions are calculated and it is shown that four of the distribution parameters correspond to marginal distribution means and standard deviations. Next, the Correlation Coefficient of the distribution is computed and shown to correspond to the remaining parameter. In remaining sections how changes in the parameters affect the distribution shape are considered. This includes an analysis of PDF contours and the linear transformation used to construct the distribution.

## Marginal Distributions

The Marginal Distributions for $u$ and $v$ are defined by,

$$
\begin{aligned}
& g(u)=\int_{-\infty}^{\infty} g(u, v) d v \\
& g(v)=\int_{-\infty}^{\infty} g(u, v) d u
\end{aligned}
$$

where $g(u, v)$ is defined by equation (12). First, consider evaluation of the integral for $g(u)$,

$$
\begin{aligned}
& g(u)=\int_{-\infty}^{\infty} g(u, v) d v \\
&=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]} d v \\
&=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]} d v \\
&=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}} \int_{-\infty}^{\infty} e^{-\frac{1}{2\left(1-\gamma^{2}\right)}}\left\{\left[\frac{\left(v-\mu_{v}\right)}{\sigma_{v}}-\gamma \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]^{2}-\gamma^{2} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}\right\} \\
& 1 \\
&=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{-\frac{1}{2\left(1-\gamma^{2}\right)} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}} e^{\frac{\gamma^{2}}{2\left(1-\gamma^{2}\right)} \frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}} \int_{-\infty}^{\infty} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(v-\mu_{v}\right)}{\sigma_{v}}-\gamma \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]^{2}} d v \\
&=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{-\frac{\left(u-\mu_{u}\right)^{2}}{2 \sigma_{u}^{2}}} \sqrt{2 \pi \sigma_{v}^{2}\left(1-\gamma^{2}\right)} \\
&=\frac{1}{\sqrt{2 \pi \sigma_{u}^{2}}} e^{-\frac{\left(u-\mu_{u}\right)^{2}}{2 \sigma_{u}^{2}}} \cdot
\end{aligned}
$$

In the first step the $u$ dependence is factored out for evaluation of the integral over $v$. The next step completes the square of the exponential followed by also factoring the introduced $u$ term from the $v$ integral. This is followed by simplification of the $u$ exponential argument. Finally, the integral over $v$ is evaluated yielding a $\mathbf{N o r m a l}\left(\mu_{u}, \sigma_{u}\right)$ distribution. Similarly, the marginal distribution $g(v)$ is given by,

$$
\begin{equation*}
g(v)=\int_{-\infty}^{\infty} g(u, v) d u=\frac{1}{\sqrt{2 \pi \sigma_{v}^{2}}} e^{-\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}} \tag{14}
\end{equation*}
$$

which is a $\mathbf{N o r m a l}\left(\mu_{v}, \sigma_{v}\right)$ distribution. The plot below shows examples of $\mathbf{N o r m a l}(\mu, \sigma)$ as $\mu$ and $\sigma$ are varied. The effect of $\mu$ is to translate the distribution along the $u$ axis and $\sigma$ scales the distribution width.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-11.jpg?height=906&width=1280&top_left_y=154&top_left_x=425)

The mean and variance are now readily determined for both $u$ and $v$,

$$
\begin{aligned}
\mathrm{E}[U] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u g(u, v) d v d u \\
& =\int_{-\infty}^{\infty} u \int_{-\infty}^{\infty} g(u, v) d v d u \\
& =\int_{-\infty}^{\infty} u g(u) d v d u \\
& =\mu_{u}
\end{aligned}
$$

and,

$$
\begin{aligned}
\operatorname{Var}[U] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(u-\mu_{u}\right)^{2} g(u, v) d v d u \\
& =\int_{-\infty}^{\infty}\left(u-\mu_{u}\right)^{2} \int_{-\infty}^{\infty} g(u, v) d v d u \\
& =\int_{-\infty}^{\infty}\left(u-\mu_{u}\right)^{2} g(u) d v d u \\
& =\sigma_{u}^{2}
\end{aligned}
$$

Similarly for $v$,

$$
\begin{aligned}
\mathrm{E}[V] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} v g(u, v) d u d v=\mu_{v} \\
\operatorname{Var}[V] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}\left(v-\mu_{v}\right)^{2} g(u, v) d u d v=\sigma_{v}^{2}
\end{aligned}
$$

## Conditional Distribution

The Conditional Distribution of a random variable is the distribution obtained by assuming the values of one or more correlated random variables are known. If the variables are uncorrelated, independent, the conditional distribution is equivalent to the marginal distribution. The conditional distribution is useful in the of the calculation of Correlation Coefficient performed in the following section and in simulation methods such as Gibbs Sampling.

For the bivariate case the conditional distributions are defined by,

$$
\begin{aligned}
& g(u \mid v)=\frac{g(u, v)}{g(v)} \\
& g(v \mid u)=\frac{g(u, v)}{g(u)}
\end{aligned}
$$

Using equations (12) and (14), $g(u \mid v)$ is evaluated as follows,

$$
\begin{aligned}
g(u \mid v) & =\frac{g(u, v)}{g(v)} \\
& =\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]} \sqrt{2 \pi \sigma_{v}^{2}} e^{\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}} \\
& =\frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}\right]} e^{\left\{\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}+\frac{1}{2\left(1-\gamma^{2}\right)}\left[\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}\right]\right\}} \\
& =\frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left\{\frac{1}{\sigma_{u}}\left[u-\left(\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right]^{2}-\frac{\gamma^{2} \sigma_{v}^{2}}{\sigma_{v}^{2}}\left(v-\mu_{v}\right)\right)^{2}\right\}}\left\{\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}-\frac{1}{\left.2\left(1-\gamma^{2}\right)\left[\frac{\left(v-\mu_{v}\right)}{\sigma_{v}^{2}}\right]\right\}}\right. \\
& =\frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2\left(1-\gamma^{2}\right)}\left\{\frac{1}{\sigma_{u}}\left[u-\left(\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right)\right]^{2}\right\}} e^{\left.\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}\left[1-\frac{1-\gamma^{2}}{1-\gamma^{2}}\right]\right\}} \\
& =\frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2 \sigma_{u}^{2}\left(1-\gamma^{2}\right)}\left\{u-\left[\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right]\right\}^{2}} \cdot
\end{aligned}
$$

In the first step the $\left(v-\mu_{v}\right)^{2}$ terms are collected and then the square is completed for the remaining terms. Once again the $\left(v-\mu_{v}\right)^{2}$ terms are collected and the finial result obtained, a Normal distribution.

Similarly, $g(v \mid u)$ is given by,

$$
\begin{aligned}
g(v \mid u) & =\frac{g(u, v)}{g(u)} \\
& =\frac{1}{\sigma_{v} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2 \sigma_{u}^{2}\left(1-\gamma^{2}\right)}\left\{v-\left[\mu_{v}+\frac{\gamma \sigma_{v}}{\sigma_{u}}\left(u-\mu_{u}\right)\right]\right\}^{2}}
\end{aligned}
$$

The conditional mean and variance can now be easily evaluated,

$$
\begin{gathered}
\mathrm{E}[U \mid V]=\int_{-\infty}^{\infty} u g(u \mid v) d u \\
=\left[\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right], \\
\mathrm{E}[V \mid U]=\int_{-\infty}^{\infty} v g(v \mid u) d v \\
=\left[\mu_{v}+\frac{\gamma \sigma_{v}}{\sigma_{u}}\left(u-\mu_{u}\right)\right], \\
\operatorname{Var}[U \mid V]=\mathrm{E}\left[(U-\mathrm{E}[U \mid V])^{2}\right] \\
=\int_{-\infty}^{\infty}(u-\mathrm{E}[U \mid V])^{2} g(u \mid v) d u \\
=\sigma_{u}^{2}\left(1-\gamma^{2}\right), \\
\operatorname{Var}[V \mid U]=\mathrm{E}\left[(V-\mathrm{E}[V \mid U])^{2}\right] \\
=\int_{-\infty}^{\infty}(v-\mathrm{E}[V \mid U])^{2} g(v \mid u) d v \\
=\sigma_{v}^{2}\left(1-\gamma^{2}\right)
\end{gathered}
$$

For both $u$ and $v$ the conditional expectation is a linear function of the conditioned variable. This is illustrated in the following plot where $g(u \mid v)$ is plotted for several values of $v$. It is seen that $v$ translates the distribution along the $u$ axis.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-13.jpg?height=914&width=1275&top_left_y=1393&top_left_x=425)

Consider the variation of $\mathrm{E}[U \mid V], \mathrm{E}[V \mid U], \operatorname{Var}[U \mid V]$ and $\operatorname{Var}[U \mid V]$ with $\gamma$. For $\gamma=0$ each reduces to the values corresponding to its marginal distribution discussed in the previous section. For
both conditional distributions increasing $\gamma$ leads to decreasing variance resulting in a sharper peak for the distribution. Additionally, changing the sign of $\gamma$ causes reflection of the distribution about the mean. Each of these properties is illustrated on the plot below where $g(u \mid v)$ is plotted for values of $\zeta$ ranging from -1 to 1 .
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-14.jpg?height=917&width=1291&top_left_y=417&top_left_x=417)

## Correlation Coefficient

The Cross Correlation of the two random variables $U$ and $V$ is defined by,

$$
\begin{aligned}
\mathrm{E}[U V] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u v g(u, v) d v d u \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u v g(u \mid v) g(v) d v d u
\end{aligned}
$$

The last step follows from the definition of conditional probability. Now, substituting equations (15) and (14) into the equation above yields,

$$
\begin{aligned}
\mathrm{E}[U V] & =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u v g(u \mid v) g(v) d v d u \\
& =\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} u v \frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} e^{\frac{-1}{2 \sigma_{u}^{2}\left(1-\gamma^{2}\right)}\left\{u-\left[\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right]\right\}^{2}} \frac{1}{\sqrt{2 \pi \sigma_{v}^{2}}} e^{-\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}} d v d u \\
& =\frac{1}{\sigma_{u} \sqrt{2 \pi\left(1-\gamma^{2}\right)}} \frac{1}{\sqrt{2 \pi \sigma_{v}^{2}}} \int_{-\infty}^{\infty} v e^{-\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}} \int_{-\infty}^{\infty} u e^{\frac{-1}{2 \sigma_{u}^{2}\left(1-\gamma^{2}\right)}\left\{u+\left[\mu_{u}-\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right]\right\}^{2}} d u d v \\
& =\frac{1}{\sqrt{2 \pi \sigma_{v}^{2}}} \int_{-\infty}^{\infty} v e^{-\frac{\left(v-\mu_{v}\right)^{2}}{2 \sigma_{v}^{2}}}\left[\mu_{u}+\frac{\gamma \sigma_{u}}{\sigma_{v}}\left(v-\mu_{v}\right)\right] d v \\
& =\mu_{u} \mu_{v}+\frac{\gamma \sigma_{u}}{\sigma_{v}} \sigma_{v}^{2} \\
& =\mu_{u} \mu_{v}+\gamma \sigma_{u} \sigma_{v}
\end{aligned}
$$

It follows that the Covariance is given by,

$$
\operatorname{Cov}(U, V)=\mathrm{E}[U V]-\mathrm{E}[U] E[V]=\gamma \sigma_{v} \sigma_{u},
$$

and Correlation Coefficient by,

$$
\gamma=\frac{\operatorname{Cov}(U, V)}{\sigma_{v} \sigma_{u}}
$$

## Distribution Parameter Limits

In previous sections it was shown that the free parameters used in the definition of the Bivariate Normal distribution, equation (12), are its the mean, variance and correlation coefficient. Here a sketch of the change in shape of the distribution as these parameters are varied is discussed by evaluating limits of the parameters for the equation defining the PDF contours. The following section will describe the convergence to the limits using a numerical analysis.

The equation satisfied by the contours is obtained by setting the argument of the exponential in equation (12) to a constant, $C^{2}$,

$$
C^{2}=\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}},
$$

where $C^{2}$ is related to the value of the contour. To develop an expectation of the behavior the following limits of this equation are considered, $\gamma \rightarrow 0, \gamma \rightarrow \pm 1, \sigma_{v} / \sigma_{u} \rightarrow 1, \sigma_{v} / \sigma_{u} \rightarrow 0$ and $\sigma_{v} / \sigma_{u} \rightarrow \infty$. The variation with $\mu_{u}$ and $\mu_{v}$ produces a translation which is not as interesting.

First, consider the limit $\gamma \rightarrow 0$ which is easily evaluated using the equation above,

$$
C^{2}=\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}
$$

This is the equation of an ellipse with axes of length $2 C \sigma_{u}$ and $2 C \sigma_{v}$. The aspect ratio of the ellipse is given by $\sigma_{v} / \sigma_{u}$. It follows that in the limit $\sigma_{v} / \sigma_{u} \rightarrow 1$ the contour approaches a circle with radius $C$ and in the limits $\sigma_{v} / \sigma_{u} \rightarrow 0$ or $\sigma_{v} / \sigma_{u} \rightarrow \infty$ the contour approaches a line along the $u$ or $v$ axes respectively.

To evaluate the limit $\gamma \rightarrow \pm 1$ it must be noted that $\gamma^{2}=1 /$ was assumed in the derivation of inverse of the Bivariate Transformation, equation (6). To evaluate the limit it should be evaluated before inverting the transformation defining the distribution, equation (5). Taking the limit results in a transformation that is valid for $\gamma^{2}=1$,

$$
\binom{U-\mu_{u}}{V-\mu_{v}}=\left(\begin{array}{cc}
\sigma_{u} & 0 \\
\pm \sigma_{v} & 0
\end{array}\right)\binom{X}{Y} .
$$

Evaluation of the equation above gives,

$$
\left(V-\mu_{v}\right)= \pm \frac{\sigma_{v}}{\sigma_{u}}\left(U-\mu_{u}\right) .
$$

It follows that as the limit is approached contours will approach a line with slope $\pm \sigma_{v} / \sigma_{u}$. The slope is positive for positive correlation and negative for negative correlation. In the limit $\sigma_{v} / \sigma_{u} \rightarrow 1$ the contour slope approaches a line with slope $\pm 1$ and in the limit $\sigma_{v} / \sigma_{u} \rightarrow 0$ or $\sigma_{v} / \sigma_{u} \rightarrow \infty$ the contour approaches a line along the $u$ or $v$ axes respectively which is the same as obtained in the limit $\gamma \rightarrow 0$.

The following two plots show the surface an contour plots for a distribution with $\sigma_{v} / \sigma_{u}=1$ and $\gamma=0$, which is the case where $u$ and $v$ are uncorrelated with equal variances. The contours are circles are previously described. The surface plot is included to show how poor it is at giving a sense of the distribution shape though it does assist in imagining the how the contour plot would be projected into the third dimension.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-16.jpg?height=1028&width=1031&top_left_y=1263&top_left_x=550)

Bivariate Normal Distribution: $\gamma=0.0, \sigma_{u}=1.0, \sigma_{v}=1.0$
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-17.jpg?height=1132&width=1028&top_left_y=205&top_left_x=520)

The next plot also has $\gamma=0$ but $\sigma_{v} / \sigma_{u}=2$. The contours become ellipses with the axis aligned with the $v$ axis.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-18.jpg?height=1025&width=1034&top_left_y=157&top_left_x=547)

The final plot has $\gamma=0.5$ and $\sigma_{v} / \sigma_{u}=1$. The contours are symmetric about the line $v=u$ as expected for the limit $\gamma \rightarrow \pm 1$. If the correlation were negative the contours would be reflected about the $v$ axis and symmetric about the line $v=-u$.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-18.jpg?height=1023&width=1029&top_left_y=1477&top_left_x=552)

## Probability Density Contours

This section will describe a more detailed analysis of parameter limits of the Bivariate Normal PDF contours consisting of plots of a larger range of values for the parameters $\gamma$ and $\sigma_{v} / \sigma_{u}$.

The equation satisfied by the contours is obtained by setting the argument of the exponential in equation (12) to a constant $C^{2}$,

$$
\begin{aligned}
C^{2} & =\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}} \\
& =\frac{\left(u-\mu_{u}\right)^{2}}{\sigma_{u}^{2}}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}-2 \gamma \frac{\left(v-\mu_{v}\right)}{\sigma_{v}} \frac{\left(u-\mu_{u}\right)}{\sigma_{u}}+\frac{\gamma^{2}}{\sigma_{v}^{2}}\left(v-\mu_{v}\right)^{2}-\frac{\gamma^{2}}{\sigma_{v}^{2}}\left(v-\mu_{v}\right)^{2} \\
& =\left[\frac{\left(u-\mu_{u}\right)}{\sigma_{u}}-\frac{\gamma}{\sigma_{v}}\left(v-\mu_{v}\right)\right]^{2}+\frac{\left(v-\mu_{v}\right)^{2}}{\sigma_{v}^{2}}\left(1-\gamma^{2}\right)
\end{aligned}
$$

Here the equation is put into a form that is more easily evaluated by completing the square of the original equation. If both sides are divided by $C^{2}$ the equation below is obtained,

$$
\frac{1}{C^{2}}\left[\frac{\left(u-\mu_{u}\right)}{\sigma_{u}}-\frac{\gamma}{\sigma_{v}}\left(v-\mu_{v}\right)\right]^{2}+\frac{\left(v-\mu_{v}\right)^{2}}{C^{2} \sigma_{v}^{2}}\left(1-\gamma^{2}\right)=1 .
$$

This equation is equivalent the equation of a unit circle which satisfies the equation,

$$
\sin ^{2} \theta+\cos ^{2} \theta=1
$$

If $\theta$ is assumed a parametric parameter satisfying $0 \geq \theta \geq 2 \pi$ a parametric equation for the contours is obtained by making the following change of variables,

$$
\begin{aligned}
\sin \theta & =\frac{1}{C}\left[\frac{\left(u-\mu_{u}\right)}{\sigma_{u}}-\frac{\gamma}{\sigma_{v}}\left(v-\mu_{v}\right)\right] \\
\cos \theta & =\frac{\left(v-\mu_{v}\right)}{C \sigma_{v}} \sqrt{\left(1-\gamma^{2}\right)}
\end{aligned}
$$

Solving these equations for $u$ and $v$ yields the parametric equations,

$$
\begin{align*}
u & =C \sigma_{u}\left[\sin \theta+\frac{\gamma}{\sqrt{1-\gamma^{2}}} \cos \theta\right]+\mu_{u}  \tag{16}\\
v & =\frac{C \sigma_{v}}{\sqrt{1-\gamma^{2}}} \cos \theta+\mu_{v}
\end{align*}
$$

To plot the actual contours a relation between the constant $C$ and the the value of the PDF along the contour is required. This relation is obtained by replacing the argument of the exponential in equation (12) with $C^{2}$,

$$
K=\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}} e^{\frac{-C^{2}}{2\left(1-\gamma^{2}\right)}}
$$

where $K$ is the PDF value along the contour. Solving this equation for $C$ gives,

$$
C=\left[-2\left(1-\gamma^{2}\right) \ln \left(2 K \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}\right)\right]^{\frac{1}{2}} .
$$

If $C$ is assumed to be real the following constraint must be satisfied,

$$
K<\frac{1}{2 \pi \sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}},
$$

which places an upper bound on the value of the peak of the distribution. The following two plots of the parametric equations defined by (16) should be compared to the contour plots from the previous section fo validation.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-20.jpg?height=1028&width=1034&top_left_y=704&top_left_x=547)
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-21.jpg?height=1028&width=1034&top_left_y=154&top_left_x=547)

To get a sense of how the contour shape varies with the distribution parameters the following two plots scan a range of $\sigma_{v} / \sigma_{u}$ with $\gamma=0$ to illustrate the limits $\sigma_{v} / \sigma_{u} \rightarrow 0$ and $\sigma_{v} / \sigma_{u} \rightarrow \infty$. This result agrees with the expectation obtained in the previous analysis. The $\sigma_{v} / \sigma_{u} \rightarrow 0$ series of contours approaches the $u$ axis and the $\sigma_{v} / \sigma_{u} \rightarrow \infty$ contours approach the $v$ axis.

Bivariate Normal Distribution: $\gamma=0.0, \sigma_{v}=1.0, K=0.02$
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-22.jpg?height=920&width=1031&top_left_y=265&top_left_x=547)

Bivariate Normal Distribution: $\gamma=0.0, \sigma_{u}=1.0, K=0.02$
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-22.jpg?height=979&width=1031&top_left_y=1306&top_left_x=547)

The next two plots illustrate the limit $\gamma \rightarrow 1$ and $\gamma \rightarrow-1$ with $\sigma_{v} / \sigma_{u}=1$. The $\gamma \rightarrow 1$ plot is converging to the line $v=u$ and the $\gamma \rightarrow-1$ plot to the line $v=-u$ as described in the previous section. Note that as $\gamma$ approaches the limit the semi-major axis of the contour increases along the appropriate limiting
line without any rotation of the contour.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-23.jpg?height=1031&width=1063&top_left_y=265&top_left_x=531)
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-23.jpg?height=1028&width=1059&top_left_y=1371&top_left_x=533)

The final two plots also look at the $\gamma \rightarrow 1$ limit but this time the first plot has $\sigma_{v} / \sigma_{u}=0.5$ and the
second $\sigma_{v} / \sigma_{u}=2$. The first is converging to the line $v=u / 2$ and the second converges to the line $v=2 u$ in agreement with the previous analysis. The behavior of the contour as the limit is approached is more interesting since the ellipse has to rotate to reach the limit. This is caused by the $\gamma=0$ contour also being an ellipse which introduces and asymmetry that must be eliminated in the limit. If the $\gamma=0$ contour were a symmetric circle no initial asymmetry need to be erased.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-24.jpg?height=1031&width=1034&top_left_y=471&top_left_x=547)
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-25.jpg?height=1025&width=1029&top_left_y=157&top_left_x=544)

## Coordinate Transformation

In this section contours of constant $u$ and $v$ are plotted in the $(x, y)$ coordinate system using equation (6) to understand how the transform distorts area elements as the distribution parameters are varied.

Contours of constant $u=C_{u}$ in ( $x, y$ ) coordinates are defined by,

$$
\begin{aligned}
x & =\frac{1}{\sigma_{u}}\left(C_{u}-\mu_{u}\right) \\
y & \left.=\frac{1}{\sqrt{1-\gamma^{2}}}\left[\frac{1}{\sigma_{v}}\left(v-\mu_{v}\right)-\frac{\gamma}{\sigma_{u}}\left(C_{u}-\mu_{u}\right)\right)\right] .
\end{aligned}
$$

This set of equations defines contours which are lines of constant $x$ since the equation for $x$ is constant.

The contours of constant $v=C_{v}$ are defined by,

$$
\begin{aligned}
x & =\frac{1}{\sigma_{u}}\left(u-\mu_{u}\right) \\
y & =\frac{1}{\sqrt{1-\gamma^{2}}}\left[\frac{1}{\sigma_{v}}\left(C_{v}-\mu_{v}\right)-\frac{\gamma}{\sigma_{u}}\left(u-\mu_{u}\right)\right) .
\end{aligned}
$$

Substituting the expression for $x$ into the expression for $y$ gives,

$$
y=\frac{-\gamma}{\sqrt{1-\gamma^{2}}} x+\frac{1}{\sigma_{v} \sqrt{1-\gamma^{2}}}\left(C_{v}-\mu_{v}\right)
$$

which is the equation of a line with slope $-\gamma / \sqrt{1-\gamma^{2}}$.
First, consider the case $\gamma=0, \mu_{u}=\mu_{v}=0$ and $\sigma_{u}=\sigma_{v}=1$ which results in the transform,

$$
\begin{aligned}
& x=C_{u} \\
& y=C_{v},
\end{aligned}
$$

and the Jacobian, equation (10), is given by,

$$
|J|=\frac{1}{\sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}}=1
$$

It follows that area elements satisfy,

$$
d x d y=|J| d u d v=d u d v
$$

Thus, for this particular choice of transform parameters area elements are preserved. Inspection of the following plot confirms that this is the case since the transform exactly maps $(u, v)$ coordinates onto ( $x, y$ ) coordinates.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-26.jpg?height=1143&width=1147&top_left_y=1067&top_left_x=493)

The next plot has parameters $\gamma=0$ and $\sigma_{u}=1$ and $\sigma_{v}=2$. The transform associated this parameter choice is given by,

$$
\begin{aligned}
x & =C_{u} \\
y & =\frac{1}{2} C_{v},
\end{aligned}
$$

with Jacobian,

$$
|J|=\frac{1}{\sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}}=\frac{1}{2}
$$

Once again the $u$ contours are aligned with lines of constant $x$ but the $v$ contours are compressed by a factor of 2 relative to lines of constant $y$. If follows that the transform reduces the size of $(u, v)$ area elements by a factor of $1 / 2$ when transformed, namely,

$$
d x d y=|J| d u d v=\frac{1}{2} d u d v
$$

What this is saying is that for an arbitrary area element $d u d v$ in the $(u, v)$ coordinates when transformed to the $(x, y)$ coordinates the $d x d y$ element has $1 / 2$ the area. This is seen to be the case in the plot where the area of a $(u, v)$ rectangle is reduced by a factor of 2 .
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-27.jpg?height=1143&width=1147&top_left_y=1067&top_left_x=493)

The final plot considers the impact of correlation on the transform by using the parameters $\gamma=0.5$ and $\sigma_{u}=\sigma_{v}=1$. The transform corresponding to this parameter choice is given by,

$$
\begin{aligned}
& x=C_{u} \\
& y=\left(-\frac{1}{\sqrt{3}} x+\frac{2}{\sqrt{3}} C_{v}\right)
\end{aligned}
$$

with Jacobian,

$$
|J|=\frac{1}{\sigma_{u} \sigma_{v} \sqrt{1-\gamma^{2}}}=\frac{2}{\sqrt{3}}
$$

The $u$ contours are aligned again but now since there is correlation the $v$ contours are lines with a negative slope so rectangular area elements in ( $u, v$ ) are transformed into parallelograms in ( $x, y$ ) coordinates. The area of one of the parallelograms is $\Delta y \Delta x$, where $\Delta y$ is the spacing between contours of constant $v$ and $\Delta x$ is the spacing between contours of constant $u$. Now, from the transform above it is seen that,

$$
\begin{aligned}
& \Delta x=\Delta C_{u} \\
& \Delta y=\frac{2}{\sqrt{3}} \Delta C_{v}
\end{aligned}
$$

but $\Delta C_{u}=\Delta C_{v}=1$, so the area of the parallelogram is given by,

$$
\Delta y \Delta x=\frac{2}{\sqrt{3}},
$$

which is equal to the Jacobian. It follows that for this choice of parameters the transformation area elements are increased in size by a factor of $2 / \sqrt{3}$,

$$
d x d y=|J| d u d v=\frac{2}{\sqrt{3}} d u d v
$$

![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-29.jpg?height=1139&width=1150&top_left_y=157&top_left_x=490)

## Conclusions

The Bivariate Normal distribution provides a simple model of correlated random variables. It is interesting to study because it is modeled as a linear transform of independent $\mathbf{N o r m a l}(0,1)$ random variables that can serve as an introduction to the concepts used in transformations of multivariate integrals. Here the background needed to understand transformations of bivariate integrals was developed by starting with a discussion of the interpretation of the vector cross product as an area. This idea was then applied to the derivation of the Jacobian Matrix for an arbitrary bivariate transformation of differential area elements. Next, the transformation used to define the Bivariate Normal distribution was introduced and applied to a distribution of two independent $\mathbf{N o r m a l}(0,1)$ random variables. The Jacobian matrix was then computed and the Bivariate Normal PDF derived. A matrix form of the Bivariate Normal PDF based the covariance matrix was introduced and shown to be equivalent to the linear transform version first discussed. The covariance matrix form more easily extends to higher dimensions. The linear transform used to define the Bivariate Normal PDF introduced five parameters. It was next shown that these parameters are the means, $\mu_{u}, \mu_{v}$, variance, $\sigma_{u}, \sigma_{v}$ and correlation coefficient, $\gamma$, of the distribution. The conditional distributions were also discussed. The change in shape of the distribution as the parameters were varied was then investigated by evaluating limits for the PDF contours that included $\gamma \rightarrow 0, \gamma \rightarrow \pm 1, \sigma_{v} / \sigma_{u} \rightarrow 1$, $\sigma_{v} / \sigma_{u} \rightarrow 0$ and $\sigma_{v} / \sigma_{u} \rightarrow \infty$. This was followed by numerically investigating the convergence to these limits using a parametric form of the PDF contour equation. The last topic discussed was the variation of the linear coordinate transformation with the distribution parameters. It was shown that resulting changes in transformed area elements were accounted for by the Jacobian.
![](https://cdn.mathpix.com/cropped/2025_11_22_0ae799072a5a7290762cg-30.jpg?height=231&width=288&top_left_y=200&top_left_x=921)

