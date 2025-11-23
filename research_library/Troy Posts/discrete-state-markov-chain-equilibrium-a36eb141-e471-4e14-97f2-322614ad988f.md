# Discrete State Markov Chain Equilibrium 

Aug 8, 2018 • Troy Stribling

A Markov Chain is a sequence of states where transitions between states occur ordered in time with the probability of transition depending only on the previous state. Here the states will be assumed a discrete finite set and time a discrete unbounded set. If the set of states is given by $\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$ the probability that the process will be in state $x_{i}$ at time $t$ is denoted by $P\left(X_{t}=x_{i}\right)$, referred to as the distribution. Markov Chain equilibrium is defined by $\lim _{t \rightarrow \infty} P\left(X_{t}=x_{i}\right)<\infty$, that is, as time advances
$P\left(X_{t}=x_{i}\right)$ becomes independent of time. Here a solution for this limit is discussed and illustrated with examples.

## Model

The Markov Chain model is constructed from the set of states $\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$ ordered in time. The process starts at time $t=0$ with state $X_{0}=x_{i}$. At the next step, $t=1$, the process will assume a state $X_{1}=x_{j}$ with probability $P\left(X_{1}=x_{j} \mid X_{0}=x_{i}\right)$ since it will depend on the previous state $x_{0}$ as defined for a Markov Process. At the next time step $t=2$ the process state will be $X_{2}=x_{k}$ with probability,

$$
P\left(X_{2}=x_{k} \mid X_{0}=x_{i}, X_{1}=x_{j}\right)=P\left(X_{2}=x_{k} \mid X_{1}=x_{j}\right),
$$

since by definition the probability of state transition depends only upon the state at the previous time step. For an arbitrary time the transition from a state $X_{t}=x_{j}$ to a state $X_{t+1}=x_{j}$ will occur with probability, $P\left(X_{t+1}=x_{j} \mid X_{t}=x_{i}\right)$ that is independent of $t$. Transition probabilities have the form of a matrix,

$$
P_{i j}=P\left(X_{t+1}=x_{j} \mid X_{t}=x_{i}\right) .
$$

$P$ will be an $N \times N$ matrix where $N$ is determined by the number of possible states. Each row represents the Markov Chain transition probability from that state at time $t$ and the columns the values at $t+1$. It follows that,

$$
\begin{gather*}
\sum_{j=1}^{N} P_{i j}=1  \tag{1}\\
P_{i j} \geq 0
\end{gather*}
$$

Equation (1) is the definition of a Stochastic Matrix.
The transition probability for a single step in the Markov Process is defined by $P$. The transition probability across two time steps can be obtained with use of the Law of Total Probability,

$$
\begin{aligned}
P\left(X_{t+2}=x_{j} \mid X_{t}=x_{i}\right) & =\sum_{k=1}^{N} P\left(X_{t+2}=x_{j} \mid X_{t}=x_{i}, X_{t+1}=x_{k}\right) P\left(X_{t+1}=x_{k} \mid X_{t}=x_{i}\right) \\
& =\sum_{k=1}^{N} P\left(X_{t+2}=x_{j} \mid X_{t+1}=x_{k}\right) P\left(X_{t+1}=x_{k} \mid X_{t}=x_{i}\right) \\
& =\sum_{k=1}^{N} P_{k j} P_{i k} \\
& =\sum_{k=1}^{N} P_{i k} P_{k j} \\
& =\left(P^{2}\right)_{i j}
\end{aligned}
$$

where the last step follows from the definition of matrix multiplication. It is straight forward but tedious to use Mathematical Induction to extend the previous result to the case of an arbitrary time difference, $\boldsymbol{T}$,

$$
\begin{equation*}
P\left(X_{t+\tau}=x_{j} \mid X_{t}=x_{i}\right)=\left(P^{\top}\right)_{i j} \tag{2}
\end{equation*}
$$

It should be noted that since $\left(P^{T}\right)_{i j}$ is a transition probability it must satisfy,

$$
\begin{gather*}
\sum_{j=1}^{N}\left(P^{\top}\right)_{i j}=1  \tag{3}\\
\left(P^{\top}\right)_{i j} \geq 0
\end{gather*}
$$

To determine the equilibrium solution of the distribution of states, $\left\{x_{1}, x_{2}, \ldots, x_{N}\right\}$, the distribution time variability must be determined. Begin by considering an arbitrary distribution at $t=0$, which can be written as a column vector,

$$
\pi=\left(\begin{array}{c}
\pi_{1} \\
\pi_{2} \\
\vdots \\
\pi_{N}
\end{array}\right)=\left(\begin{array}{c}
P\left(X_{0}=x_{1}\right) \\
P\left(X_{0}=x_{2}\right) \\
\vdots \\
P\left(X_{0}=x_{N}\right)
\end{array}\right),
$$

since it is a probability distribution $\pi_{i}$ must satisfy,

$$
\begin{gather*}
\sum_{i=1}^{N} \pi_{i}=1  \tag{4}\\
\pi_{i} \geq 0
\end{gather*}
$$

The distribution after the first step is given by,

$$
\begin{aligned}
P\left(X_{1}=x_{j}\right) & =\sum_{i=1}^{N} P\left(X_{1}=x_{j} \mid X_{0}=x_{i}\right) P\left(X_{0}=x_{i}\right) \\
& =\sum_{i=1}^{N} P_{i j} \pi_{i} \\
& =\sum_{i=1}^{N} \pi_{i} P_{i j} \\
& =\left(\pi^{T} P\right)_{j}
\end{aligned}
$$

where $\boldsymbol{\pi}^{T}$ is the transpose of $\boldsymbol{\pi}$. Similarly, the distribution after the second step is,

$$
\begin{aligned}
P\left(X_{2}=x_{j}\right) & =\sum_{i=1}^{N} P\left(X_{2}=x_{j} \mid X_{1}=x_{i}\right) P\left(X_{1}=x_{i}\right) \\
& =\sum_{i=1}^{N} P_{i j}\left(\pi^{T} P\right)_{i} \\
& =\sum_{i=1}^{N} P_{i j} \sum_{k=1}^{N} \pi_{k} P_{k i} \\
& =\sum_{k=1}^{N} \pi_{k} \sum_{i=1}^{N} P_{i j} P_{k i} \\
& =\sum_{k=1}^{N} \pi_{k} \sum_{i=1}^{N} P_{k i} P_{i j} \\
& =\sum_{k=1}^{N} \pi_{k}\left(P^{2}\right)_{k j} \\
& =\left(\pi^{T} P^{2}\right)_{j},
\end{aligned}
$$

A pattern is clearly developing. Mathematical Induction can be used to prove the distribution at an arbitrary time $t$ is given by,

$$
P\left(X_{t}=x_{j}\right)=\left(\pi^{T} P^{t}\right)_{j}
$$

or as a column vector,

$$
\begin{equation*}
\pi_{t}^{T}=\pi^{T} P^{t} \tag{5}
\end{equation*}
$$

Where $\pi$ and $\pi_{t}$ are the initial distribution and the distribution after $t$ steps respectively.

## Equilibrium Transition Matrix

The probability of transitioning between two states $x_{i}$ and $x_{j}$ in $t$ time steps was previously shown to be stochastic matrix $P^{t}$ constrained by equation ( 3 ). The equilibrium transition matrix is defined by,

$$
P^{E}=\lim _{t \rightarrow \infty} P^{t} .
$$

This limit can be determined using Matrix Diagonalization. The following sections will use diagonalization to construct a form of $P^{t}$ that will easily allow evaluation equilibrium limit.

## Eigenvectors and Eigenvalues of the Transition Matrix

Matrix Diagonalization requires evaluation of eigenvalues and eigenvectors, which are defined by the solutions to the equation,

$$
\begin{equation*}
P v=\lambda v \tag{6}
\end{equation*}
$$

where $v$ is the eigenvector and $\lambda$ eigenvalue. From equation (6) it follows,

$$
\begin{aligned}
P^{t} v & =P^{t-1}(P v) \\
& =P^{t-1} \lambda v \\
& =P^{t-2}(P v) \lambda \\
& =P^{t-2} \lambda^{2} v \\
& \vdots \\
& =(P v) \lambda^{t-1} \\
& =\lambda^{t} v .
\end{aligned}
$$

Since $P^{t}$ is a stochastic matrix it satisfies equation (3). As a result of these constraints the limit $t \rightarrow \infty$ requires,

$$
\lim _{t \rightarrow \infty} P^{t}=\lim _{t \rightarrow \infty} \lambda^{t} v \leq \infty .
$$

It follows that $\lambda \leq 1$. Next, it will be shown that $\lambda_{1}=1$ and that a column vector of $1^{\prime} s$ with $N$ rows,

$$
V_{1}=\left(\begin{array}{c}
1  \tag{7}\\
1 \\
\vdots \\
1
\end{array}\right)
$$

are eigenvalue and eigenvector solutions of equation (6),

$$
\left(\begin{array}{cccc}
P_{11} & P_{12} & \cdots & P_{1 N} \\
P_{21} & P_{22} & \cdots & P_{2 N} \\
\vdots & \vdots & \ddots & \vdots \\
P_{N 1} & P_{N 2} & \cdots & P_{N N}
\end{array}\right)\left(\begin{array}{c}
1 \\
1 \\
\vdots \\
1
\end{array}\right)=\left(\begin{array}{c}
\sum_{j=1}^{N} P_{1 j} \\
\sum_{j=1}^{N} P_{2 j} \\
\vdots \\
\sum_{j=1}^{N} P_{N j}
\end{array}\right)=\left(\begin{array}{c}
1 \\
1 \\
\vdots \\
1
\end{array}\right)=\lambda_{1} V_{1},
$$

where use was made of the stochastic matrix condition from equation (1), namely, $\sum_{j=1}^{N} P_{i j}=1$.

To go further a result from the Perron-Frobenius Theorem is needed. This theorem states that a stochastic matrix will have a largest eigenvalue with multiplicity 1 . Here all eigenvalues will satisfy $\lambda_{1}=1>\left|\lambda_{i}\right|, \forall 1<i \leq N$.

Denote the eigenvector $V_{j}$ by the column vector,

$$
V_{j}=\left(\begin{array}{c}
v_{1 j} \\
v_{2 j} \\
\vdots \\
v_{N j}
\end{array}\right),
$$

and let $V$ be the matrix with columns that are the eigenvectors of $P$ with $V_{1}$ from equation (7) in the first column,

$$
V=\left(\begin{array}{cccc}
1 & v_{12} & \cdots & v_{1 N} \\
1 & v_{22} & \cdots & v_{2 N} \\
\vdots & \vdots & \ddots & \vdots \\
1 & v_{N 2} & \cdots & v_{N N}
\end{array}\right) .
$$

Assume that $V$ is invertible and denote the inverse by,

$$
V^{-1}=\left(\begin{array}{cccc}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}  \tag{8}\\
v_{21}^{-1} & v_{22}^{-1} & \cdots & v_{2 N}^{-1} \\
\vdots & \vdots & \ddots & \vdots \\
v_{N 1}^{-1} & v_{N 2}^{-1} & \cdots & v_{N N}^{-1}
\end{array}\right)
$$

If the identity matrix is represented by $I$ then $V V^{-1}=I$. Let $\Lambda$ be a diagonal matrix constructed from the eigenvalues of $P$ using $\lambda_{1}=1$,

$$
\Lambda=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & \lambda_{2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_{N}
\end{array}\right) .
$$

Sufficient information about the eigenvalues and eigenvectors has been obtained to prove some very general results for Markov Chains. The following section will work through the equilibrium limit using the using these results to construct a diagonalized representation of the matrix.

## Diagonalization of Transition Matrix

Using the results obtained in the previous section the diagonalized form of the transition matrix is given by,

$$
P=V \Lambda V^{-1}
$$

Using this representation of $P$ an expression for $P^{t}$ is obtained,

$$
\begin{aligned}
P^{t} & =P^{t-1} V \Lambda V^{-1} \\
& =P^{t-2} V \Lambda V^{-1} V \Lambda V^{-1} \\
& =P^{t-2} V \Lambda^{2} V^{-1} \\
& \vdots \\
& =P V \Lambda^{t-1} V^{-1} \\
& =V \Lambda^{t} V^{-1}
\end{aligned}
$$

Evaluation of $\Lambda^{t}$ is straight forward,

$$
\Lambda^{t}=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & \lambda_{2}^{t} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_{N}^{t}
\end{array}\right) .
$$

Since $\left|\lambda_{i}\right|<1, \forall 1<i \leq N$ in the limit $t \rightarrow \infty$ it is seen that,

$$
\Lambda^{E}=\lim _{t \rightarrow \infty} \Lambda^{t}=\lim _{t \rightarrow \infty}\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & \lambda_{2}^{t} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_{N}^{t}
\end{array}\right)=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{array}\right),
$$

so,

$$
P^{E}=\lim _{t \rightarrow \infty} P^{t}=\lim _{t \rightarrow \infty} V \Lambda^{t} V^{-1}=V \Lambda^{E} V^{-1} .
$$

Evaluation of the first two terms on the righthand side gives,

$$
V \Lambda^{E}=\left(\begin{array}{cccc}
1 & v_{12} & \cdots & v_{1 N} \\
1 & v_{22} & \cdots & v_{2 N} \\
\vdots & \vdots & \ddots & \vdots \\
1 & v_{N 2} & \cdots & v_{N N}
\end{array}\right)\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0
\end{array}\right)=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
1 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
1 & 0 & \cdots & 0
\end{array}\right) .
$$

It follows that,

$$
V \Lambda^{E} V^{-1}=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
1 & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
1 & 0 & \cdots & 0
\end{array}\right)\left(\begin{array}{cccc}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1} \\
v_{21}^{-1} & v_{22}^{-1} & \cdots & v_{2 N}^{-1} \\
\vdots & \vdots & \ddots & \vdots \\
v_{N 1}^{-1} & v_{N 2}^{-1} & \cdots & v_{N N}^{-1}
\end{array}\right)=\left(\begin{array}{cccc}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1} \\
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1} \\
\vdots & \vdots & \ddots & \vdots \\
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}
\end{array}\right) .
$$

Finally, the equilibrium transition matrix is given by,

$$
P^{E}=V \Lambda^{E} V^{-1}=\left(\begin{array}{cccc}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}  \tag{9}\\
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1} \\
\vdots & \vdots & \ddots & \vdots \\
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}
\end{array}\right)
$$

The rows of $P^{E}$ are identical and given by the first row of the inverse of the matrix of eigenvectors, $V^{-1}$, from equation (8). This row is a consequence of the location of the $\lambda=1$ eigenvalue and eigenvector in $\Lambda$ and $V$ respectively. Since $P^{E}$ is a transition matrix,

$$
\begin{gathered}
\sum_{j=1}^{N} v_{i j}^{-1}=1 \\
v_{i j}^{-1} \geq 0 .
\end{gathered}
$$

## Equilibrium Distribution

The equilibrium distribution is defined by a solution to equation (5) that is independent of time.

$$
\begin{equation*}
\pi^{T}=\pi^{T} P^{t} \tag{10}
\end{equation*}
$$

Consider a distribution $\boldsymbol{\Pi}_{E}$ that satisfies,

$$
\begin{equation*}
\pi_{E}^{T}=\pi_{E}^{T} P \tag{11}
\end{equation*}
$$

It is easy to show that $\boldsymbol{\pi}_{E}$ is an equilibrium solution by substituting it into equation (10).

$$
\begin{aligned}
\pi_{E}^{T} & =\pi_{E}^{T} P^{t} \\
& =\left(\pi_{E}^{T} P\right) P^{t-1} \\
& =\pi_{E}^{T} P^{t-1} \\
& =\pi_{E}^{T} P^{t-2} \\
& \vdots \\
& =\pi_{E}^{T} P \\
& =\pi_{E}^{T} .
\end{aligned}
$$

## Relationship Between Equilibrium Distribution and Transition Matrix

To determine the relationship between $\pi_{E}$ and $P^{E}$, begin by considering an arbitrary initial distribution states with $N$ elements,

$$
\pi=\left(\begin{array}{c}
\pi_{1} \\
\pi_{2} \\
\vdots \\
\pi_{N}
\end{array}\right),
$$

where,

$$
\begin{gathered}
\sum_{j=1}^{N} \pi_{j}=1 \\
\pi_{j} \geq 0
\end{gathered}
$$

The distribution when the Markov Chain has had sufficient time to reach equilibrium will be given by,

$$
\begin{aligned}
\pi^{T} P^{E} & =\left(\begin{array}{llll}
\pi_{1} & \pi_{2} & \cdots & \pi_{N}
\end{array}\right)\left(\begin{array}{cccc}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1} \\
v_{11}^{11} & v_{12}^{12} & \cdots & v_{1 N}^{1} \\
\vdots & \vdots & \ddots & \vdots \\
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}
\end{array}\right) \\
& =\left(\begin{array}{llll}
v_{11}^{-1} \sum_{j=1}^{N} \pi_{j} & v_{12}^{-1} \sum_{j=1}^{N} \pi_{j} & \cdots & v_{1 N}^{-1} \sum_{j=1}^{N} \pi_{j}
\end{array}\right),
\end{aligned}
$$

since, $\sum_{j=1}^{N} \pi_{j}=1$,

$$
\pi^{T} P^{E}=\left(\begin{array}{llll}
v_{11}^{-1} & v_{12}^{-1} & \cdots & v_{1 N}^{-1}
\end{array}\right) .
$$

Thus any initial distribution $\pi$ will after sufficient time approach the distribution above. It follows that it will be the solution of equation (11) which defines the equilibrium distribution,

$$
\boldsymbol{\Pi}_{E}=\left(\begin{array}{c}
v_{11}^{-1} \\
v_{12}^{-1} \\
\vdots \\
v_{1 N}^{-1}
\end{array}\right) .
$$

## Solution of Equilibrium Equation

An equation for the equilibrium distribution, $\boldsymbol{\pi}_{E}$, can be obtained from equation (11),

$$
\pi_{E}^{T}(P-I)=0 \quad(12)
$$

where $I$ is the identity matrix. Equation (12) alone is insufficient to obtain a unique solution since the system of linear equations it defines is Linearly Dependent. In a linearly dependent system of equations some equations are the result of linear operations on the others. It is straight forward to show that one of the equations defined by (12) can be
eliminated by summing the other equations and multiplying by -1 . If the equations were linearly independent the only solution would be the trivial zero solution, $\left(\pi_{E}^{T}\right)_{i}=0, \forall i$. A unique solution to (12) is obtained by including the normalization constraint,

$$
\sum_{j=1}^{N}\left(\pi_{E}^{T}\right)_{j}=1 .
$$

The resulting system of equations to be solved is given by,

$$
\pi_{E}^{T}\left(\begin{array}{ccccc}
P_{11}-1 & P_{12} & \cdots & P_{1 N} & 1  \tag{13}\\
P_{21} & P_{22}-1 & \cdots & P_{2 N} & 1 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
P_{N 1} & P_{N 2} & \cdots & P_{N N}-1 & 1
\end{array}\right)=\left(\begin{array}{ccccc}
0 & 0 & 0 & 0 & 1
\end{array}\right)
$$

## Example

Consider the Markov Chain defined by the transition matrix,

$$
P=\left(\begin{array}{llll}
0.0 & 0.9 & 0.1 & 0.0  \tag{14}\\
0.8 & 0.1 & 0.0 & 0.1 \\
0.0 & 0.5 & 0.3 & 0.2 \\
0.1 & 0.0 & 0.0 & 0.9
\end{array}\right)
$$

The state transition diagram below provides a graphical representation of $P$.
![](https://cdn.mathpix.com/cropped/2025_11_22_6b0e9a70c1441efe454fg-12.jpg?height=1435&width=1132&top_left_y=162&top_left_x=460)

## Convergence to Equilibrium

Relaxation of both the transition matrix and distribution to their equilibrium values is easily demonstrated with the few lines of Python executed within ipython.

```
In [1]: import numpy
In [2]: t = [[0.0, 0.9, 0.1, 0.0],
    ...: [0.8, 0.1, 0.0, 0.1],
    ..: [0.0, 0.5, 0.3, 0.2],
    ...: [0.1, 0.0, 0.0, 0.9]]
In [3]: p = numpy.matrix(t)
In [4]: p**100
```

```
Out [ 4 ] :
matrix([[0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088495, 0.03982301, 0.38053098]])
```

Here the transition matrix from the initial state to states 100 time steps in the future is computed using equation (2). The result obtained has identical rows as obtained in equation (9).

$$
P^{100}=\left(\begin{array}{llll}
0.27876106 & 0.30088496 & 0.03982301 & 0.38053097  \tag{15}\\
0.27876106 & 0.30088496 & 0.03982301 & 0.38053097 \\
0.27876106 & 0.30088496 & 0.03982301 & 0.38053097 \\
0.27876106 & 0.30088495 & 0.03982301 & 0.38053098
\end{array}\right)
$$

For an initial distribution $\boldsymbol{\pi}$ the distribution after 100 time steps is evaluated using,

```
In [5]: c = [[0.1],
    ..: [0.5],
    ...: [0.35],
    ...: [0.05]]
In [6]: \pi = numpy.matrix(c)
In [8]: π.T*p**100
Out[8]: matrix([[0.27876106, 0.30088496, 0.03982301, 0.38053097]])
```

Here an initial distribution is constructed that satisfies $\sum_{i=0}^{3} \pi_{i}=1$. Then equation (5) is used to compute the distribution after 100 time steps. The result is that expected from the previous analysis. In the equilibrium limit the distribution is the repeated row of the equilibrium transition matrix, namely,

$$
\Pi_{100}=\left(\begin{array}{l}
0.27876106 \\
0.30088496 \\
0.03982301 \\
0.38053097
\end{array}\right) \quad(16) .
$$

The plot below illustrates the convergence of the distribution from the previous example. In the plot the components of $\pi_{t}$ from equation ( 5 ) are plotted for each time step. The convergence to the limiting value occurs rapidly. Within only 20 steps $\pi_{t}$ has reached
limiting distribution.

$\pi_{t}$ Relaxation to Equilibrium
![](https://cdn.mathpix.com/cropped/2025_11_22_6b0e9a70c1441efe454fg-14.jpg?height=1026&width=1714&top_left_y=357&top_left_x=203)

## Equilibrium Transition Matrix

In this section the equilibrium limit of the transition matrix is determined for the example Markov Chain shown in equation (14). It was previously shown that this limit is given by equation (9). To evaluate this equation the example transition matrix must be diagonalized. First, the transition matrix eigenvalues and eigenvectors are computed using the numpy linear algebra library.

```
In [9]: λ, v = numpy.linalg.eig(p)
In [10]: λ
Out[10]: array([-0.77413013, 0.24223905, 1. , 0.83189108])
In [11]: v
Out[11]:
matrix([[-0.70411894, 0.02102317, 0.5 , -0.4978592 ],
    [ 0.63959501, 0.11599428, 0.5 , -0.44431454],
    [-0.30555819, -0.99302222, 0.5 , -0.14281543],
```

$$
\text { [ 0.04205879, -0.00319617, } 0.5 \text {, 0.73097508]]) }
$$

It is seen that $\lambda=1$ is indeed an eigenvalue, as previously proven and that other eigenvalues have magnitudes less than 1. This is in agreement with Perron-Frobenius Theorem. The numpy linear algebra library normalizes the eigenvectors and uses the same order for eigenvalues and eigenvector columns. The eigenvector corresponding to $\lambda=1$ is in the third column and has all components equal. Eigenvectors are only known to an arbitrary scalar, so the vector of $1^{\prime} s$ used in the previous analysis can be obtained by multiplying the third column by 2 . After obtaining the eigenvalues and eigenvectors equation (9) is evaluated 100 after time steps and compared with the equilibrium limit.

```
In [12]: \Lambda = numpy.diag( λ)
In [13]: V = numpy.matrix(v)
In [14]: Vinv = numpy.linalg.inv(V)
In [15]: \Lambda_t = \Lambda**100
In [16]: ^_t
Out[16] :
array([[7.61022278e-12, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
    [0.00000000e+00, 2.65714622e-62, 0.00000000e+00, 0.00000000e+00],
    [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
    [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.01542303e-08]]
In [17]: V * ^_t * Vinv
Out[17]:
matrix([[0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088496, 0.03982301, 0.38053097],
    [0.27876106, 0.30088495, 0.03982301, 0.38053098]])
```

First, the diagonal matrix of eigenvalues, $\Lambda$, is created maintaining the order of $\lambda$. Next, the matrix $V$ is constructed with eigenvectors as columns while also maintaining the order of vectors in $v$. The inverse of $V$ is then computed. $\Lambda^{t}$ can now be computed for 100 time steps. The result is in agreement with the past effort where the limit $t \rightarrow \infty$ was evaluated giving a matrix that contained a 1 in the $(1,1)$ component corresponding to the position of the $\lambda=1$ component and zeros for all others. Here the eigenvectors are ordered differently but the only nonzero component has the $\lambda=1$ eigenvalue. Finally, equation (9) is evaluated and all rows are identical and equal to $\pi_{t}$ evaluated at $t=100$, in agreement with the
equilibrium limit determined previously and calculations performed in the last section shown in equations (15) and (16).

## Equilibrium Distribution

The equilibrium distribution will now be calculated using the system of linear equations defined by equation (9). Below the resulting system of equations for the example distribution in equation (14) is shown.

$$
\pi_{E}^{T}\left(\begin{array}{ccccc}
-1.0 & 0.9 & 0.1 & 0.0 & 1.0 \\
0.8 & -0.9 & 0.0 & 0.1 & 1.0 \\
0.0 & 0.5 & -0.7 & 0.2 & 1.0 \\
0.1 & 0.0 & 0.0 & -0.1 & 1.0
\end{array}\right)=\left(\begin{array}{ccccc}
0.0 & 0.0 & 0.0 & 0.0 & 1.0
\end{array}\right)
$$

This system of equations is solved using the least squares method provided by the numpy linear algebra library, which requires the use of the transpose of the above equation. The first line below computes it using equation (14).

```
In [18]: E = numpy.concatenate((p.T - numpy.eye(4), [numpy.ones(4)]))
In [19]: E
Out[19]:
matrix([[-1. , 0.8, 0. , 0.1],
    [ 0.9, -0.9, 0.5, 0.],
    [ 0.1, 0. , -0.7, 0. ],
    [ 0. , 0.1, 0.2, -0.1],
    [ 1. , 1. , 1. , 1. ]])
In [20]: πe, _, _, _ = numpy.linalg.lstsq(E, numpy.array([0.0, 0.0, 0.0,
In [21]: πe
Out[21]: array([0.27876106, 0.30088496, 0.03982301, 0.38053097])
```

Next, the equilibrium distribution is evaluated using the least squares method. The result obtained is consistent with previous results shown in equation (16).

## Simulation

This section will use a direct simulation of equation (14) to calculate the equilibrium distribution and compare the result to those previously obtained. Below a Python implementation of the calculation is shown.

```
import numpy
def sample_chain(t, x0, nsample):
    xt = numpy.zeros(nsample, dtype=int)
    xt[0] = x0
    up = numpy.random.rand(nsample)
    cdf = [numpy.cumsum(t[i]) for i in range(4)]
    for t in range(nsample - 1):
        xt[t] = numpy.flatnonzero(cdf[xt[t-1]] >= up[t])[0]
    return xt
# Simulation parameters
\pi_nsamples = 1000
nsamples = 10000
c = [[0.25],
    [0.25],
    [0.25],
    [0.25] ]
# Generate \pi_nsamples initial state samples
\pi = numpy.matrix(c)
\pi_cdf = numpy.cumsum(c)
\pi_samples = [numpy.flatnonzero(\pi_cdf >= u)[0] for u in numpy.random.rand
# Run sample_chain for nsamples for each of the initial state samples
chain_samples = numpy.array([])
for x0 in \pi_samples:
    chain_samples = numpy.append(chain_samples, sample_chain(t, x0, nsamp]
```

The function sample_chain performs the simulation and uses Inverse CDF Sampling on the discrete distribution obtained from the transition matrix defined by equation (14). The transition matrix determines state at step $t+1$ from the state at step $t$. The following code uses sample_chain to generate and ensemble of simulations with the initial state also
sampled from an assumed initial distribution. First, simulation parameters are defined and the initial distribution is assumed to be uniform. Second, $\pi \_$nsamples of the initial state are generated using Inverse CDF sampling with the initial distribution. Finally, simulations of length nsamples are performed for each initial state. The ensemble of samples are collected in the variable chain_samples and plotted below. A comparison is made with the two other calculations performed. The first is $\pi_{t}$ for $t=100$ shown in equation (16) and the second the solution to equation (9). The different calculations are indistinguishable.
![](https://cdn.mathpix.com/cropped/2025_11_22_6b0e9a70c1441efe454fg-18.jpg?height=1071&width=1687&top_left_y=783&top_left_x=219)

## Conclusions

Markov Chain equilibrium for discrete state processes is a general theory of the time evolution of transition probabilities and state distributions. It has been shown that equilibrium is a consequence of assuming the transition matrix and distribution vector are both stochastic. Expressions were derived for the time evolution of any transition matrix and distribution and the equilibrium solutions were then obtained analytically by evaluating
the limit $t \rightarrow \infty$. A calculation was performed using the obtained equations for the equilibrium solutions and the numpy linear algebra libraries using an example transition matrix. These results were compared to ensemble simulations. The time to relax from an arbitrary state to the equilibrium distributions was shown to occur within $O(10)$ time steps.
![](https://cdn.mathpix.com/cropped/2025_11_22_6b0e9a70c1441efe454fg-19.jpg?height=123&width=259&top_left_y=580&top_left_x=937)
© gly.fish 2018
Powered by Jekyll

