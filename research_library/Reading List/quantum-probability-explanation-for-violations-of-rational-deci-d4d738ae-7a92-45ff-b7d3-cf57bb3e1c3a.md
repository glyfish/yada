# A quantum probability explanation for violations of 'rational' decision theory 

Emmanuel M. Pothos ${ }^{1, *}$ and Jerome R. Busemeyer ${ }^{2, *}$<br>${ }^{1}$ Department of Psychology, Swansea University, Swansea SA2 8PP, UK<br>${ }^{2}$ Department of Psychology, Indiana University, 10th Street, Bloomington, IN 47405, USA


#### Abstract

Two experimental tasks in psychology, the two-stage gambling game and the Prisoner's Dilemma game, show that people violate the sure thing principle of decision theory. These paradoxical findings have resisted explanation by classical decision theory for over a decade. A quantum probability model, based on a Hilbert space representation and Schrödinger's equation, provides a simple and elegant explanation for this behaviour. The quantum model is compared with an equivalent Markov model and it is shown that the latter is unable to account for violations of the sure thing principle. Accordingly, it is argued that quantum probability provides a better framework for modelling human decision-making.


Keywords: Prisoner's Dilemma; quantum probability; decision-making; cognitive science

## 1. INTRODUCTION

Cognitive science is concerned with providing formal, computational descriptions for various aspects of cognition. Over the last few decades, several frameworks have been thoroughly examined, such as formal logic (e.g. St Evans et al. 1991), information theory (e.g. Chater 1999), classical (Bayesian) probability (e.g. Tenenbaum \& Griffiths 2001), neural networks (Rumelhart \& McClelland 1986) and a range of formal, symbolic systems (e.g. Anderson et al. 1997). Being able to establish an advantage of one computational approach over another is clearly a fundamental issue for cognitive scientists. Two criteria are needed to achieve this goal: one is to establish a striking empirical finding that provides a strong theoretical challenge and the other is to provide a rigorous mathematical argument that a theoretical class fails to meet this challenge. This paper reviews findings that challenge the classical (Bayesian) probability approach to cognition, and proposes to exchange this with a more generalized (quantum) probability approach.

The empirical challenge is provided by two experimental tasks in decision-making, the Prisoner's Dilemma and the two-stage gambling task, which have had an enormous influence on cognitive psychology (and econ-omics-there are over 31000 citations to Tversky's work, one of the researchers who first studied these tasks, e.g. Tversky \& Kahneman 1983; Shafir \& Tversky 1992; Tversky \& Shafir 1992). These experimental tasks are important because they show a violation of a fundamental law of classical (Bayesian) probability theory that, when applied to human decision-making, is called the 'sure thing' principle (Savage 1954).

The sure thing principle (Savage 1954) is fundamental to classical decision theory: if you prefer action A over B under state of the world $X$, and you also prefer A over B

[^0]under the complementary state $\sim X$, then you should prefer A over B when the state is unknown. This principle was tested by Tversky \& Shafir (1992) in a simple twostage gambling experiment: participants were told that they had just played a gamble (even chance to win $\$ 200$ or lose $\$ 100$ ), and then they were asked to choose whether to play the same gamble a second time. In one condition, they knew they won the first play; in a second condition, they knew they lost the first play; and in a third condition, they did not know the outcome. Surprisingly, the results violated the sure thing principle: following a win/loss, the participants chose to play again on $69 \%$ / $59 \%$, respectively, of the trials; but when the outcome was unknown, they chose only to play again on 36 per cent of the trials. This preference reversal was observed at the individual level of analysis with real money at stake.

Similar results were obtained using a two-person Prisoner's Dilemma game with pay-offs defined for each player as in table 1. The Nash equilibrium in standard game theory is for both parties to defect. Three conditions are used to test the sure thing principle: in an 'unknown' condition, you act without knowing your opponent's action; in the 'known defect' condition, you know your opponent will defect before you act; and in the 'known cooperate' condition, you know your opponent will cooperate before you act. According to the sure thing principle, if you prefer to defect, regardless of whether you know your opponent will defect or cooperate, then you should prefer to defect even when your opponent's action is unknown.

Once again, people frequently violate the sure thing principle (Shafir \& Tversky 1992)-many players defected knowing the opponent defected and knowing the opponent cooperated, but they switched and decided to cooperate when they did not know the opponent's action. This preference reversal by many players caused the proportion of defections for the unknown condition to fall below the proportions observed under the known conditions. This key finding of Shafir \& Tversky (1992) has been replicated in several subsequent studies (Croson 1999; Li \& Taplin 2002; Busemeyer et al. 2006a; table 2).

Table 1. Example pay-off matrix for a Prisoner's Dilemma game.
| you defect | you cooperate |
| :--- | :--- |
| other defects <br> other: 10 <br> you: 10 <br> other cooperates <br> other: 5 <br> you: 25 | other: 25 <br> you: 5 <br> other: 20 <br> you: 20 |


Table 2. Empirically observed proportion of defections in different conditions in the Prisoner's Dilemma game.
| study | known to defect | known to cooperate | unknown |
| :--- | :--- | :--- | :--- |
| Shafir \& Tversky (1992) | 97 | 84 | 63 |
| Croson (1999; avg. of first two experiments) | 67 | 32 | 30 |
| Li \& Taplan (2002) | 83 | 66 | 60 |
| Busemeyer et al. (2006a) | 91 | 84 | 66 |
| average | 84 | 66 | 55 |
| Q model | 81 | 65 | 57 |


Note that Prisoner's Dilemma is a task that has attracted widespread attention not just from decisionmaking scientists. For example, it has been intensely studied in the context of how altruistic and cooperative behaviour can arise in both humans and animals (e.g. Axelrod \& Hamilton 1981; Stephens et al. 2002; Kefi et al. 2007). Violations of the sure thing principle specifically have not been demonstrated in animal cognition. However, both Shafir (1994) and Waite (2001) showed that transitivity, another fundamental aspect of classical probability theory, can be violated in animal preference choice (with grey jays and bees, respectively). Also, it turns out that a core element of our model for human decision-making in the Prisoner's Dilemma has an analogue in animal cognition, raising the possibility that such a model may be applicable to animal cognition as well.

We present an alternative probabilistic framework for modelling decision-making, based on quantum probability. Why consider a quantum probability model for decision-making? The original motivation for the development of quantum mechanics in physics was to explain findings that seemed paradoxical from a classical point of view. Similarly, paradoxical findings in psychology have made a growing number of researchers seek explanations that make use of the quantum formalism in cognitive situations. For example, Aerts \& Aerts (1994; see also Khrennikov 2004; La Mura in press; Mogiliansky et al. in press) modelled incompatibility and interference effects that arise in human preference judgements. Gabora \& Aerts (2002; see also Aerts \& Gabora 2005a,b; Aerts et al. in press) modelled puzzling findings found in human reasoning with conceptual combinations. Bordley (1998; see also Franco in press) modelled paradoxical results obtained with human probability judgements. Van Rijsbergen (2004; see also Widdows 2006; Bruza et al. 2008) showed that classical logic does not appear the right type of logic when dealing with classes of objects and a more appropriate representation for classes is possible
with mathematical tools from quantum theory. Such approaches can be labelled 'geometric' (cf. Aerts \& Aerts 1994) in that they use the geometric properties of Hilbert space representations and the measurement principles of quantum theory, but not the dynamical aspects of quantum theory (time evolution with Schrödinger's equation).

A much smaller number of applications have attempted to apply quantum dynamics to cognition. For example, Atmanspacher et al. (2002) modelled oscillations in human perception of impossible figures. Aerts et al. (2004) modelled how a human observer alternates between perceiving the statements in a liar's paradox situation as false and true. Busemeyer et al. (2006b) presented a quantum model for signal detection type of human decision processes. Our proposal builds on this latter work (and particularly that of Busemeyer et al. 2006a). We were interested in a model that would have implications for the time course of a decision, as well as accurately predicting choice probabilities in the Prisoner's Dilemma and two-stage gambling task. A novel aspect of our proposal is that we attempt to derive a relevant Hamiltonian a priori, on the basis of the psychological parameters of the decision-making situation.

Finally, note that the goal of models such as the above is to formulate a mathematical framework for understanding the behavioural findings from cognition and decision-making. This objective must be distinguished from related ones, such as constructing new game strategies using quantum game theory (Eisert et al. 1999), modelling the biology of the brain using quantum mechanics (Pribram 1993; Hameroff \& Penrose 1996) or developing new algorithms for quantum computation (Nielsen \& Chuang 2000).

The violation of the sure thing principle readily suggests that a classical probability model for Tversky and Shafir's results will fail. We go beyond intuition and develop a standard Markov model for the two-stage gambling task and the Prisoner's Dilemma, to prove that this model can never account for the empirical findings. In this way we motivate a more general model, based on quantum probability. Researchers have recently successfully explored applications of the quantum mechanics formalism outside physics (for example, notably computer science, e.g. Grover 1997). Explorations of how the quantum principles could apply in psychology have been slow, partly because of a confusion of whether such attempts implicate a statement that the operation of the brain is quantum mechanical (e.g. Hameroff \& Penrose 1996). This could be the case or not (cf. Marr 1982), but it is not the issue at stake: rather, we are asking whether quantum probability could provide an appropriate mathematical framework for understanding/modelling certain behavioural aspects of cognition. Key problems in such an endeavour are (i) what is an appropriate Hilbert space representation of the task, (ii) what is the psychological motivation for the corresponding Hamiltonian, and (iii) what is the meaning of time evolution in this context? We address all these problems in our quantum probability model of decision-making in the Prisoner's Dilemma task and the two-stage gambling task. The model is described with respect to the Prisoner's Dilemma task, but extension to the two-stage gambling task is straightforward.

## 2. DESCRIPTION OF THE MODEL

## (a) Step 1: representation of beliefs and actions

The Prisoner's Dilemma game involves a set of four mutually exclusive and exhaustive outcomes $\Omega=\left\{\mathrm{B}_{\mathrm{D}} \mathrm{A}_{\mathrm{D}}\right.$, $\left.B_{D} A_{C}, B_{C} A_{D}, B_{C} A_{C}\right\}$, where $B_{i} A_{j}$ represents your belief that your opponent will take the $i$ th action, but you intend to take the $j$ th action ( D , defect; C, cooperate). For both the Markov and quantum models, we assume that the probabilities of the four outcomes can be computed from a $4 \times 1$ state vector
$\psi=\left[\begin{array}{l}\psi_{\mathrm{DD}} \\ \psi_{\mathrm{DC}} \\ \psi_{\mathrm{CD}} \\ \psi_{\mathrm{CC}}\end{array}\right]$.
For the Markov model, $\psi_{i j}=\operatorname{Pr}$ [observe belief $i$ and action $j$ ], with $\sum_{i} \sum_{j} \psi_{i j}=1$. For the quantum model, $\psi_{i j}$ is an amplitude, so that $\left|\psi_{i j}\right|^{2}=\operatorname{Pr}$ [observe belief $i$ and action $j$ ], with $\sum_{i} \sum_{j}\left|\psi_{i j}\right|^{2}=1$. For both models, we assume that the individual begins the decision process in an uninformed state:
$\psi_{0}=\frac{1}{4}\left[\begin{array}{l}1 \\ 1 \\ 1 \\ 1\end{array}\right]$,
for the Markov model and
$\psi_{0}=\frac{1}{2}\left[\begin{array}{l}1 \\ 1 \\ 1 \\ 1\end{array}\right]$,
for the quantum model.

## (b) Step 2: inferences based on prior information

Information about the opponent's action changes the initial state $\psi_{0}$ into a new state $\psi_{1}$.

If the opponent is known to defect, the state changes to
$\psi_{1}=\frac{1}{2}\left[\begin{array}{l}1 \\ 1 \\ 0 \\ 0\end{array}\right]$,
for the Markov model, and
$\psi_{1}=\frac{1}{\sqrt{2}}\left[\begin{array}{l}1 \\ 1 \\ 0 \\ 0\end{array}\right]$,
for the quantum model; similarly, if the opponent is known to cooperate, the state changes to
$\psi_{1}=\frac{1}{2}\left[\begin{array}{l}0 \\ 0 \\ 1 \\ 1\end{array}\right]$,
for the Markov model and
$\psi_{1}=\frac{1}{\sqrt{2}}\left[\begin{array}{l}0 \\ 0 \\ 1 \\ 1\end{array}\right]$,
for the quantum model. If no information is provided, then the state remains unchanged so that $\psi_{1}=\psi_{0}$.

## (c) Step 3: strategies based on pay-offs

The decision-maker must evaluate the pay-offs in order to select an action, which changes the previous state $\psi_{1}$ into a final state $\psi_{2}$. We assume that the time evolution of the initial state to the final state corresponds to the thought process leading to a decision.

For the Markov model, we can model this change using a Kolmogorov forward equation $(\mathrm{d} \psi / \mathrm{d} t)=K_{\mathrm{A}} \cdot \psi$, which has a solution $\psi_{2}(t)=\mathrm{e}^{t \cdot K_{\mathrm{A}}} \cdot \psi_{1}$. The matrix $T(t)=\mathrm{e}^{t \cdot K_{\mathrm{A}}}$ is a transition matrix, with $T_{i j}(t)=\operatorname{Pr}[\operatorname{transiting}$ to state $i$ from state $j$ during time period $t$ ]. The transition matrix satisfies $\sum_{i} T_{i j}=1$ to guarantee that $\psi_{2}$ sums to unity. Initially, we assume
$K_{\mathrm{A}}=\left[\begin{array}{cc}K_{\mathrm{Ad}} & 0 \\ 0 & K_{\mathrm{Ac}}\end{array}\right], \quad$ where $\quad K_{\mathrm{A} i}=\left[\begin{array}{cc}-1 & \mu_{i} \\ 1 & -\mu_{i}\end{array}\right]$.

The intensity matrix $K_{\mathrm{A}}$ transforms the state probabilities to favour either defection or cooperation, depending on the parameters $\mu_{\mathrm{d}}$ or $\mu_{\mathrm{c}}$, which correspond to your gain if you defect, depending on whether you believe the opponent will defect or cooperate, respectively; these parameters depend on the pay-offs associated with different actions, and will be considered shortly. The intensity matrix requires $K_{i j}>0$ for $i \neq j$ and $\sum_{i} K_{i j}=0$ to guarantee that $\mathrm{e}^{t \cdot K_{\mathrm{A}}}$ is a transition matrix.

For the quantum model, the time evolution is determined by Schrödinger's equation $i \cdot(\mathrm{~d} \psi / \mathrm{d} t)=H_{\mathrm{A}} \cdot \psi$ with solution $\psi_{2}(t)=\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{A}}} \cdot \psi_{1}$. The matrix $U(t)=\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{A}}}$ is unitary with $\left|U_{i j}(t)\right|^{2}=\operatorname{Pr}[\operatorname{transiting}$ to state $i$ from state $j$ during time period $t$ ]. This matrix must satisfy $U^{\dagger} U=I$ (identity matrix) to guarantee that $\psi_{2}$ retains unit length ( $\mathrm{U}^{\dagger}$ is the adjoint of U). Initially, we assume that
$H_{\mathrm{A}}=\left[\begin{array}{cc}H_{\mathrm{Ad}} & 0 \\ 0 & H_{\mathrm{Ac}}\end{array}\right]$, where $H_{\mathrm{A} i}=\frac{1}{\sqrt{1+\mu_{i}^{2}}}\left[\begin{array}{cc}\mu_{i} & 1 \\ 1 & -\mu_{i}\end{array}\right]$.

The Hamiltonian $H_{\mathrm{A}}$ rotates the state to favour either defection or cooperation, depending on the parameters $\mu_{d}$ or $\mu_{\mathrm{c}}$, which (as before) correspond to your gain if you defect, depending on whether you believe the opponent will defect or cooperate, respectively. The Hamiltonian must be Hermitian ( $H_{\mathrm{A}}^{\dagger}=H_{\mathrm{A}}$ ) to guarantee that $U$ is unitary.

For both models, the parameter $\mu_{i}$ is assumed to be a monotonically increasing utility function of the differences in the pay-offs for each of your actions, depending on the opponent's action: $\mu_{\mathrm{d}}=u\left(x_{\mathrm{DD}}-x_{\mathrm{DC}}\right)$ and $\mu_{\mathrm{c}}=u\left(x_{\mathrm{CD}}-x_{\mathrm{CC}}\right)$, where $x_{i j}$ is the pay-off you receive if your opponent takes action $i$ and you take action $j$. For example, given the pay-offs in table $1, u_{\mathrm{DD}}=x(10,10)$, $u_{\mathrm{DC}}=x(25,5), u_{\mathrm{CD}}=x(5,25)$ and $u_{\mathrm{CC}}=x(20,20)$. Assuming that utility is determined solely by your own payoffs, then $\mu_{\mathrm{d}}=u\left(x_{\mathrm{DD}}-x_{\mathrm{DC}}\right)=u(5)=\mu=u\left(x_{\mathrm{CD}}-x_{\mathrm{CC}}\right)=\mu_{\mathrm{c}}$.

In other words, typically, $\mu_{i}$ can be set equal to the difference in the pay-offs (possibly multiplied by a constant, scaling factor), although more complex utility functions can be assumed.

For both models, a decision corresponds to a measurement of the state $\psi_{2}(t)$. For the Markov model, $\operatorname{Pr}$ [you defect $]=\operatorname{Pr}[\mathrm{D}]=\left(\psi_{\mathrm{DD}}+\psi_{\mathrm{CD}}\right)$; similarly, for the quantum model, $\operatorname{Pr}[$ you defect $]=\operatorname{Pr}[D]=\left(\left|\psi_{D D}\right|^{2}+\left|\psi_{C D}\right|^{2}\right)$.

Inserting equation (1.1a) into the Kolmogorov equation and solving for $\psi_{2}(t)$ yields the following probability when the opponent's action is known:
$\operatorname{Pr}[\mathrm{D}]=\left(\frac{\mu}{1+\mu}\right) \cdot\left(1-\mathrm{e}^{-(\mu+1) \cdot t}\right)+\frac{\mathrm{e}^{-(\mu+1) \cdot t}}{2}$.
This probability gradually grows monotonically from (1/2) at $t=0$ to $(\mu /(1+\mu))$ as $t \rightarrow \infty$. The behaviour of the quantum model is more complex. Inserting equation (1.1b) into the Schrödinger equation and solving for $\psi_{2}(t)$ yields:
$\operatorname{Pr}[\mathrm{D}]=\left(\frac{1}{2}+\frac{\mu}{1+\mu^{2}} \cdot \sin \left(\frac{\pi}{2} \cdot t\right)^{2}\right)$.
For $-1<\mu<+1$, this probability increases across time from (1/2) at $t=0$ to $\left((1 / 2)+\left(\mu /\left(1+\mu^{2}\right)\right)\right)$ at $t=1$, and subsequently it oscillates between the minimum and maximum values. Empirically, choice probabilities in laboratorybased, decision-making tasks monotonically increase across time (for short decision times, see Diederich \& Busemeyer 2006), and so a reasonable approach for fitting the model is to assume that a decision is reached within the interval $(0<t<1)$ for the quantum model ( $t=1$ would correspond to approx. 2 s for such tasks).

Equations (1.1a) and (1.1b) produce reasonable choice models when the action of the opponent is known. However, when the opponent's action is unknown, both models predict that the probability of defection is the average of the two known cases, which fails to explain the violations of the sure thing principle. The $K_{\mathrm{A}}$ and $H_{\mathrm{A}}$ components of each model can be understood as the 'rational' components of each model, whereby the decision-maker is simply assumed to try to maximize utility. In §2d we introduce a component in each model for describing an additional influence on the decision-making process, which can lead to decisions that do not maximize expected utility (and so could lead to violations of the sure thing principle). These two components in each model have to be separate since in many cases the behaviour of decision-makers can be explained (just) by an urge to maximize expected utility. The difference between the Markov model and the quantum one relates to how the two components are combined with each other. Importantly, we prove that the Markov model still cannot produce the violations of the sure thing principle even when this second, non-rational component is added. Only the quantum model explains the result.

## (d) Step 4: strategies based on evaluations of both beliefs and pay-offs

To explain violations of the sure thing principle, we introduce the idea of cognitive dissonance (Festinger 1957). People tend to change their beliefs to be consistent with their actions. In the case of the Prisoner's Dilemma game, this motivates a change of beliefs about what the opponent will do in a direction that is consistent with
the person's intended action. In other words, if a player chooses to cooperate he/she would tend to think that the other player will cooperate as well. The reduction in cognitive dissonance is an intriguing, and extensively supported, cognitive process. It has been shown with monkeys (Egan et al. 2007), suggesting that the applicability of our model might extend to such animals. Shafir \& Tversky (1992) explained it in terms of a personal bias for 'wishful thinking' and Chater et al. (2008) by considering a statistical approach based on Simpson's paradox (specifically, Chater et al. showed that, in a Prisoner's Dilemma game, the propensity to cooperate or defect would depend on assumptions about what the opponent would do, given whether the parameters of the game would encourage cooperation or defection). Such approaches may not be incompatible (for example, wishful thinking may have an underlying statistical explanation).

Although cognitive dissonance tendencies can be implemented in both the Markov and quantum models, we shall see that it does not help the Markov model, and only the quantum model explains the sure thing principle violations.

For the Markov model, an intensity matrix that produces a change of wishful thinking is
$K_{\mathrm{B}}=\left(\left[\begin{array}{cccc}-1 & 0 & +\gamma & 0 \\ 0 & 0 & 0 & 0 \\ +1 & 0 & -\gamma & 0 \\ 0 & 0 & 0 & 0\end{array}\right]+\left[\begin{array}{cccc}0 & 0 & 0 & 0 \\ 0 & -\gamma & 0 & +1 \\ 0 & 0 & 0 & 0 \\ 0 & +\gamma & 0 & -1\end{array}\right]\right)$.

The first/second matrix changes beliefs about the opponent towards defection/cooperation when you plan to defect/cooperate, respectively.

Note that
$\frac{\mathrm{d}}{\mathrm{d} t} \cdot\left[\begin{array}{l}\psi_{\mathrm{DD}} \\ \psi_{\mathrm{DC}} \\ \psi_{\mathrm{CD}} \\ \psi_{\mathrm{CC}}\end{array}\right]=\left[\begin{array}{cccc}-1 & 0 & +\gamma & 0 \\ 0 & -\gamma & 0 & +1 \\ +1 & 0 & -\gamma & 0 \\ 0 & +\gamma & 0 & -1\end{array}\right] \cdot\left[\begin{array}{l}\psi_{\mathrm{DD}} \\ \psi_{\mathrm{DC}} \\ \psi_{\mathrm{CD}} \\ \psi_{\mathrm{CC}}\end{array}\right]=\left[\begin{array}{l}\gamma \cdot \psi_{\mathrm{CD}}+\psi_{\mathrm{DD}} \\ \psi_{\mathrm{CC}}-\gamma \cdot \psi_{\mathrm{DC}} \\ \psi_{\mathrm{DD}}-\gamma \cdot \psi_{\mathrm{CD}} \\ \gamma \cdot \psi_{\mathrm{DC}}-\cdot \psi_{\mathrm{CC}}\end{array}\right]$.
If $\gamma>1$, then the rate of increase for the first and last rows is greater than that for the middle rows, leading to an increase in the probabilities that beliefs and actions agree. For example, setting $\gamma=10$ at $t=1$ produces
$\mathrm{e}^{t \cdot K_{\mathrm{B}}} \cdot \psi_{0}=\left[\begin{array}{l}0.45 \\ 0.05 \\ 0.05 \\ 0.45\end{array}\right]$,
where it can be seen that beliefs tend to match actions, achieving a reduction in cognitive dissonance. For the quantum model, a Hamiltonian that produces this change is
$H_{\mathrm{B}}=\frac{-\gamma}{\sqrt{2}} \cdot\left(\left[\begin{array}{cccc}+1 & 0 & +1 & 0 \\ 0 & 0 & 0 & 0 \\ +1 & 0 & -1 & 0 \\ 0 & 0 & 0 & 0\end{array}\right]+\left[\begin{array}{cccc}0 & 0 & 0 & 0 \\ 0 & -1 & 0 & +1 \\ 0 & 0 & 0 & 0 \\ 0 & +1 & 0 & +1\end{array}\right]\right)$.

The first/second matrix rotates beliefs about the opponent towards defection/cooperation when you plan to defect/cooperate, respectively. Note that

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{~d} t} \cdot\left[\begin{array}{c}
\psi_{\mathrm{DD}} \\
\psi_{\mathrm{DC}} \\
\psi_{\mathrm{CD}} \\
\psi_{\mathrm{CC}}
\end{array}\right] & =-i \cdot \frac{-\gamma}{\sqrt{2}} \cdot\left[\begin{array}{cccc}
+1 & 0 & +1 & 0 \\
0 & -1 & 0 & +1 \\
+1 & 0 & -1 & 0 \\
0 & +1 & 0 & +1
\end{array}\right] \cdot\left[\begin{array}{l}
\psi_{\mathrm{DD}} \\
\psi_{\mathrm{DC}} \\
\psi_{\mathrm{CD}} \\
\psi_{\mathrm{CC}}
\end{array}\right] \\
& =i \cdot \frac{\gamma}{\sqrt{2}} \cdot\left[\begin{array}{c}
\psi_{\mathrm{DD}}+\psi_{\mathrm{CD}} \\
\psi_{\mathrm{CC}}-\psi_{\mathrm{DC}} \\
\psi_{\mathrm{DD}}-\psi_{\mathrm{CD}} \\
\psi_{\mathrm{DC}}+\psi_{\mathrm{CC}}
\end{array}\right] \cdot
\end{aligned}
$$

If $\gamma>0$, then the rate of increase for the first and last rows is greater than that for the middle rows, so that, as before, there is an increase in the amplitudes for the states in which beliefs and actions agree. For example, setting $\gamma=1$ at $t=\pi / 2$ produces $\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{B}}} \cdot \psi_{0}$ which results in a vector of squared magnitudes
$=\left[\begin{array}{l}0.50 \\ 0.00 \\ 0.00 \\ 0.50\end{array}\right]$.
In both the Markov and quantum models, we can see that the above intensity matrix/Hamiltonian, respectively, makes beliefs and actions correlated.

By itself, equation (1.2a) and (1.2b) is an inadequate description of behaviour in the Prisoner's Dilemma, because it cannot explain how preferences vary with payoffs. We need to combine equations (1.1a), (1.1b) and (1.2a), (1.2b) to produce an intensity matrix $K_{\mathrm{C}}=K_{\mathrm{A}}+K_{\mathrm{B}}$ or a Hamiltonian $H_{\mathrm{C}}=H_{\mathrm{A}}+H_{\mathrm{B}}$, so that the time evolution of the initial state to the final state reflects the influences of both the pay-offs and the process of wishful thinking. Note that in this combined model, both beliefs and actions are evolving simultaneously and in parallel.

Accordingly, we suggest that the final state is determined by $\psi_{2}=\mathrm{e}^{t \cdot K_{\mathrm{C}}} \cdot \psi_{1}$ for the Markov model and $\psi_{2}=\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{C}}} \cdot \psi_{1}$ for the quantum model. Each model has two free parameters: one changes the actions using equation (1.1a) and (1.1b) and depends on pay-offs (i.e. $\mu$ ), and the other that corresponds to a psychological bias to assume the opponent will act as we do with equation (1.2a) and (1.2b) (i.e. $\gamma$ ).

## 3. MODEL PREDICTIONS

For the Markov model, probabilities for the unknown state can be related to probabilities for the known states by expressing the initial unknown state as a probability mixture of the two initial known states:

$$
\begin{aligned}
\psi_{2} & =\mathrm{e}^{t \cdot K_{\mathrm{C}}} \cdot \frac{1}{4}\left[\begin{array}{l}
1 \\
1 \\
1 \\
1
\end{array}\right]=\mathrm{e}^{t \cdot K_{\mathrm{C}}} \cdot \frac{1}{2}\left(\frac{1}{2}\left[\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right]+\frac{1}{2}\left[\begin{array}{l}
0 \\
0 \\
1 \\
1
\end{array}\right]\right) \\
& =\frac{1}{2}\left(\mathrm{e}^{t \cdot K_{\mathrm{C}}} \cdot \frac{1}{2}\left[\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right]+\mathrm{e}^{t \cdot K_{\mathrm{C}}} \cdot \frac{1}{2}\left[\begin{array}{l}
0 \\
0 \\
1 \\
1
\end{array}\right]\right)
\end{aligned}
$$

We see that the state probabilities in the unknown case must equal the average of the state probabilities for the two known cases. Therefore, the Markov model fails to reproduce the violations of the sure thing principle, regardless of what parameters, time point, initial state or intensity matrix we use. This conclusion reflects the fundamental fact that the Markov model obeys the law of total probability, which mathematically restricts the unknown state to remain a weighted average of the two known states. Note that this failure of the Markov model occurs even when we include the cognitive dissonance tendencies in the model.

For the quantum model, the amplitudes for the unknown state can also be related to the amplitudes for the two known states:

$$
\begin{aligned}
\psi_{2} & =\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{C}}} \cdot \frac{1}{2}\left[\begin{array}{l}
1 \\
1 \\
1 \\
1
\end{array}\right]=\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{C}}} \cdot \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right]+\frac{1}{\sqrt{2}}\left[\begin{array}{l}
0 \\
0 \\
1 \\
1
\end{array}\right]\right) \\
& =\frac{1}{\sqrt{2}}\left(\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{C}}} \cdot \frac{1}{\sqrt{2}}\left[\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right]+\mathrm{e}^{-\mathrm{i} \cdot t \cdot H_{\mathrm{C}}} \cdot \frac{1}{\sqrt{2}}\left[\begin{array}{l}
0 \\
0 \\
1 \\
1
\end{array}\right]\right) .
\end{aligned}
$$

We see that the amplitudes in the unknown case equal the superposition of the amplitudes for the two known cases. However, here is precisely where the quantum model departs from the Markov model: probabilities are obtained from the squared magnitudes of the amplitudes. This last computation produces interference effects that can cause the unknown probabilities to deviate from the average of the known probabilities.

We initially fit the parameters of the quantum model at $t=1 \cdot(\pi / 2)$, which is the time when the choice probabilities produced by equation (1.1b) first reach their maximum. Note that the quantum model predicts that choice probabilities will oscillate with time. However, in modelling results from the Prisoner's Dilemma task, one needs to consider, first, that such tasks are very simple and, second, that respondents in such experiments are typically paid for their participation so that they are motivated (and indeed sometimes requested) to respond quickly. Both these considerations suggest that a decision will be made (the state vector collapses) as early as one course of action emerges as advantageous (Diederich \& Busemeyer 2006). Regarding the two-stage gambling task, setting $\mu=0.59$ and $\gamma=1.74$ produces probabilities for choosing to gamble equal to $(0.68,0.58,0.37)$ for the (known win, known loss, unknown) conditions, respectively. These predictions closely match the observed results $(0.69,0.59$, 0.36 , from Tversky \& Shafir 1992). For the Prisoner's Dilemma game, setting $\mu=0.51$ and $\gamma=2.09$ produces probabilities for defection equal to $(0.81,0.65,0.57)$ for the (known defect, known cooperate, unknown) conditions, respectively. Again, model predictions closely reproduce the average pattern ( $0.84,0.66,0.55$ ) in table 2. Figure 1 shows that model predictions are fairly robust as parameter values vary. An interference effect appears after $t=0.75 \cdot(\pi / 2)$ and is evident across a large section of the parameter space. Finally, note that we can

![](https://cdn.mathpix.com/cropped/2025_11_22_41da03fd1699ba433c95g-6.jpg?height=1308&width=1492&top_left_y=194&top_left_x=262)
Figure 1. $(a-f)$ The probability of defection under the unknown condition minus the average for the two known conditions, at six time points (note that time incorporates a factor of $\pi / 2$; (a) time $=0.75$, (b) time $=1.00$, (c) time $=1.25$, (d) time $=1.50$, (e) time $=1.75$, $(f)$ time $=2.00$ ). Negative values (blue) typically indicate an interference effect in the predicted direction.

relax the assumption that participants will make a decision at the same time point (we thank a reviewer for this observation). To allow for this possibility, we assumed a gamma distribution of decision times with a range from $t=0.50 \cdot(\pi / 2)$ to $2 \cdot(\pi / 2)$ and a mode at $t=1 \cdot(\pi / 2)$. We refitted the model using the mean choice probability averaged over this distribution, and this produced very similar predicted results: $(0.77,0.64,0.58)$ for the known defect, known cooperate and unknown conditions, respectively, in a Prisoner's Dilemma (with $\mu=0.47$ and $\gamma=2.10$ ).

Classical probability theory has been widely applied in understanding human choice behaviour. Accordingly, one can naturally wonder whether it is possible to salvage the Markov model. First, recall that the classical Markov model fails even when we allow for cognitive dissonance effects in this model. Second, the analyses above hold for any initial state, $\psi_{0}$, and any intensity matrix, $K$ (not just the ones used above to motivate the model), but they are based on two main assumptions: the same initial state and the same intensity matrix are used across both known and unknown conditions. However, we can relax even these assumptions. Even if the initial state is not the same across conditions, the Markov model must predict that the marginal probability of defecting in the unknown condition (whatever mixture is used) is a convex combination of the two probabilities conditioned on the
known action of the opponent. This prediction is violated in the data of table 2. Furthermore, even if we change intensity matrices across conditions (using the $K_{\mathrm{A}}$ intensity matrix for known conditions and using the $K_{\mathrm{C}}$ matrix for the unknown condition), the Markov model continues to satisfy the law of total probability because this change has absolutely no effect on the predicted probability of defection (the $K_{\mathrm{B}}$ matrix does not change the defection rate). Thus our tests of the Markov model are very robust.

## 4. CONCLUDING COMMENTS

In this work, we considered empirical results that have been a focal point in the controversy over whether classical probability theory is an appropriate framework for modelling cognition or not. Tversky, Shafir, Kahneman and colleagues have argued that the cognitive system is generally sensitive to environmental statistics, but is also routinely influenced by heuristics and biases that can violate the prescription from probability theory (Tversky \& Kahneman 1983; Tversky \& Shafir 1992; cf. Gigerenzer 1996). This position has had a massive influence not only on psychology, but also on management sciences and economics, culminating in a Nobel Prize award to Kahneman. Moreover, findings such as the violation of the sure thing principle in the Prisoner's Dilemma have led researchers to raise fundamental questions about the nature
of human cognition (for example, what does it mean to be rational? Oaksford \& Chater 1994).

In this work, we adopted a different approach from the heuristics and biases advocated by Tversky, Kahneman and Shafir. We propose that human cognition can and should be modelled within a probabilistic framework, but classical probability theory is too restrictive to fully describe human cognition. Accordingly, we explored a model based on quantum probability, which can subsume classical probability, as a special case. The main problems in developing a convincing cognitive quantum probability model are to determine an appropriate Hilbert space and Hamiltonian. We attempted to present a satisfactory prescriptive approach to deal with these problems and so encourage the development of other quantum probability models in cognitive science. For example, the Hamiltonian is derived directly from the parameters of the problem (e.g. the pay-offs associated with different actions) and known general principles of cognition (e.g. reducing cognitive dissonance). Importantly, our model works: it is able to account for violations of the sure thing principle in the Prisoner's Dilemma and the two-stage gambling task and leads to close fits to empirical data.

Quantum probability provides a promising framework for modelling human decision-making. First, we can think of the set of basis states as a set of preference orders over actions. According to a Markov process, an individual is committed to exactly one preference order at any moment in time, although it can change from time to time. According to a quantum process, an individual experiences a superposition of all these orders, and at any moment the person remains uncommitted to any specific order. This is an intriguing perspective on human cognition, which may shed light on the functional role of different modes of memory and learning (cf. Atallah et al. 2004). Second, Schrödinger's equation predicts a periodic oscillation of the propensity to perform one action (assuming that the decision-maker can be persuaded to extend the decision time beyond the first cycle of the process), which is broadly analogous to the electroencephalography signals recorded from participants engaged in choice tasks (cf. Haggard \& Eimer 1999). Only after preferences are revealed does the process collapse onto exactly one preference order. This contrasts with time development in the Markov model, whereby the system monotonically converges to its final state. Third, quantum probability models allow interference effects that can make the probability of the disjunction of two events to be lower than the probability of either event individually (see also Khrennikov 2004). Such interference effects are ubiquitous in psychology, but incompatible with Markov models, which are constrained by classical probability laws. Fourth, 'back-to-back' measurements on the same decision will produce the same result in a quantum system (because of state reduction), which agrees with what people do (Atmanspacher et al. 2004). However, back-to-back choices remain probabilistic in classical random utility models, which is not what people do. Finally, recent results in computer science have shown quantum computation to be fundamentally faster compared with classical computation, for certain problems (Nielsen \& Chuang 2000). Perhaps the success of human cognition can be partly explained by its use of quantum principles.

This research was partly supported by ESRC grant R000222655 to E.M.P. and NIMH R01 MH068346 and NSF MMS SES 0753164 to J.R.B. We would like to thank Chris Isham, Smaragda Kessari and Tim Hollowood.

## REFERENCES

Aerts, D. \& Aerts, S. 1994 Applications of quantum statistics in psychological studies of decision processes. Found. Sci. 1, 85-97.
Aerts, D. \& Gabora, L. 2005a A theory of concepts and their combinations I: the structure of the sets of contexts and properties. Kybernetes 34, 151-175. (doi:10.1108/ 03684920510699972)

Aerts, D. \& Gabora, L. 2005b A theory of concepts and their combinations II: a Hilbert space representation. Kybernetes 34, 192-220. (doi:10.1108/03684920510575807)
Aerts, D., Broekaerst, J. \& Smets, S. 2004 A quantum structure description of the liar paradox. Int. I. Theor. Phys. 38, 3231-3239. (doi:10.1023/A:1026686316673)
Aerts, D., Broekaert, J. \& Gabora, L. In press. A case for applying an abstracted quantum formalism to cognition. New Ideas Psychol.
Anderson, J. R., Matessa, M. \& Lebiere, C. 1997 ACT-R: a theory of higher level cognition and its relation to visual attention. Hum. Comput. Interact. 12, 439-462. (doi:10. 1207/s15327051hci1204_5)
Atallah, H. E., Frank, M. J. \& O'Reilly, R. C. 2004 Hippocampus, cortex, and basal ganglia: insights from computational models of complementary learning systems. Neurobiol. Learn. Mem. 82, 253-267. (doi:10. 1016/j.nlm.2004.06.004)
Atmanspacher, H., Römer, H. \& Walach, H. 2002 Weak quantum theory: complementarity and entanglement in physics and beyond. Found. Phys. 32, 379-406.
Atmanspacher, H., Filk, T. \& Römer, H. 2004 Quantum Zeno features of bistable perception. Biol. Cybern. 90, 33-40. (doi:10.1007/s00422-003-0436-4)
Axelrod, R. \& Hamilton, W. D. 1981 The evolution of cooperation. Science 211, 1390-1396. (doi:10.1126/ science.7466396)
Bordley, R. F. 1998 Quantum mechanical and human violations of compound probability principles: toward a generalized Heisenberg uncertainty principle. Oper. Res. 46, 923-926. (doi:10.1287/opre.46.6.923)
Bruza, P., Widdows, D. \& Woods, J. 2008 A quantum logic of down below. In Handbook of quantum logic, quantum structures, and quantum computation, vol. 2 (eds K. Engesser, D. Gabbay \& D. Lehmann), pp. 625-660. Amsterdam, The Netherlands: Elsevier.
Busemeyer, J. R., Matthew, M. \& Wang, Z. A. 2006a Quantum game theory explanation of disjunction effects. In Proc. 28th Annual Conf. of the Cognitive Science Society (eds R. Sun \& N. Miyake), pp. 131-135. Mahwah, NJ: Erlbaum.
Busemeyer, J. R., Wang, Z. \& Townsend, J. T. 2006b Quantum dynamics of human decision-making. 7. Math. Psychol. 50, 220-241. (doi:10.1016/j.jmp.2006.01.003)
Chater, N. 1999 The search for simplicity: a fundamental cognitive principle? Q. 7. Exp. Psychol. A 52, 273-302. (doi:10.1080/027249899391070)
Chater, N., Vlaev, I. \& Grinberg, M. 2008 A new consequence of Simpson's paradox: stable cooperation in one-shot Prisoner's Dilemma from populations of individualistic learners. F. Exp. Psychol. Gen. 137, 403-421. (doi:10.1037/0096-3445.137.3.403)
Croson, R. 1999 The disjunction effect and reason-based choice in games. Organ. Behav. Hum. Decis. Process. 80, 118-133. (doi:10.1006/obhd.1999.2846)

Diederich, A. \& Busemeyer, J. R. 2006 Modeling the effects of payoffs on response bias in a perceptual discrimination task: threshold bound, drift rate change, or two stage processing hypothesis. Percept. Psychophys. 97, 51-72.
Egan, L. C., Santos, L. R. \& Bloom, P. 2007 The origins of cognitive dissonance: evidence from children and monkeys. Psychol. Sci. 18, 978-983. (doi:10.1111/j.14679280.2007.02012.x)

Eisert, J., Wilkens, M. \& Lewenstein, M. 1999 Quantum games and quantum strategies. Phys. Rev. Lett. 83, 3077-3080. (doi:10.1103/PhysRevLett.83.3077)
Festinger, L. 1957 A theory of cognitive dissonance. Stanford, CA: Stanford University Press.
Franco, R. In press. The conjunction fallacy and interference effects. 7. Math. Psychol. (Special issue on Quantum cognition and decision making).
Gabora, L. \& Aerts, D. 2002 Contextualizing concepts using a mathematical generalization of the quantum formalism. F. Exp. Theor. Artif. Intell. 14, 327-358. (doi:10.1080/ 09528130210162253)

Gigerenzer, G. 1996 Reasoning the fast and frugal way: models of bounded rationality. Psychol. Rev. 103, 650-669. (doi:10.1037/0033-295X.103.4.650)
Grover, L. 1997 Quantum mechanics helps in searching for a needle in a haystack. Phys. Rev. Lett. 79, 325. (doi:10. 1103/PhysRevLett.79.325)
Haggard, P. \& Eimer, M. 1999 On the relation between brain potential and the awareness of voluntary movements. Exp. Brain Res. 126, 128-133. (doi:10.1007/s002210050722)
Hameroff, S. R. \& Penrose, R. 1996 Conscious events as orchestrated space-time selections. 7. Conscious. Stud. 3, 36-53.
Kefi, S., Bonnet, O. \& Danchin, E. 2007 Accumulated gain in Prisoner's Dilemma: which game is carried out by the players? Anim. Behav. 74, e1-e6. (doi:10.1016/j.anbehav. 2006.11.025)

Khrennikov, A. 2004 Information dynamics in cognitive, psychological, social and anomalous phenomena. Fundamental theories of physics, vol. 138. Dordrecht, The Netherlands: Kluwer Academic Publishers.
La Mura, P. In press. Projective expected utility. F. Math. Psychol.
Li, S. \& Taplin, J. 2002 Examining whether there is a disjunction effect in Prisoner's Dilemma games. Chin. 7. Psychol. 44, 25-46.

Marr, D. 1982 Vision: a computational investigation into the human representation and processing of visual information. San Francisco, CA: W. H. Freeman.

Mogiliansky, A. L., Zamir, S. \& Zwirn, H. In press. Type indeterminacy: a model of the KT (Kahneman Tversky)-man. F. Math. Psychol. (Special issue on Quantum cognition and decision making).
Nielsen, M. A. \& Chuang, L. L. 2000 Quantum computation and quantum information. Cambridge, UK: Cambridge University Press.
Oaksford, M. \& Chater, N. 1994 A rational analysis of the selection task as optimal data selection. Psychol. Rev. 101, 608-631. (doi:10.1037/0033-295X.101.4.608)
Pribram, K. H. 1993 Rethinking neural networks: quantum fields and biological data. Hillsdale, NJ: Erlbaum.
Rumelhart, D. E. \& McClelland, J. L. 1986 Parallel distributed processing, foundations, vol. 1. Cambridge, MA: MIT Press.
Savage, L. J. 1954 The foundations of statistics. New York, NY: Wiley.
Shafir, E. \& Tversky, A. 1992 Thinking through uncertainty: nonconsequential reasoning and choice. Cogn. Psychol. 24, 449-474. (doi:10.1016/0010-0285(92)90015-T)
Shafir, S. 1994 Intransitivity of preferences in honey bees: support for 'comparative' evaluation of foraging options. Anim. Behav. 48, 55-67. (doi:10.1006/anbe.1994.1211)
Stephens, D. W., McLinn, C. M. \& Stevens, J. R. 2002 Discounting and reciprocity in an iterated Prisoner's Dilemma. Science 298, 2216-2218. (doi:10.1126/science. 1078498)

St Evans, B. T. J., Newstead, S. E. \& Byrne, R. J. M. 1991 Human reasoning: the psychology of deduction. Hove, UK: Lawrence Erlbaum Associates.
Tenenbaum, J. \& Griffiths, T. L. 2001 Generalization, similarity, and Bayesian inference. Behav. Brain Sci. 24, 629-641. (doi:10.1017/S0140525X01000061)
Tversky, A. \& Kahneman, D. 1983 Judgment under uncertainty: heuristics and biases. Science 185, 1124-1131. (doi:10.1126/science.185.4157.1124)
Tversky, A. \& Shafir, E. 1992 The disjunction effect in choice under uncertainty. Psychol. Sci. 3, 305-309. (doi:10.1111/ j.1467-9280.1992.tb00678.x)

Van Rijsbergen, C. J. 2004 The geometry of information retrieval. Cambridge, UK: Cambridge University Press.
Waite, T. 2001 Intransitive preferences in hoarding gray jays (Perisoreus Canadensis). Behav. Ecol. Sociobiol. 50, 116-121. (doi:10.1007/s002650100346)
Widdows, D. 2006 Geometry and meaning. Stanford, CA: CSLI Publications; Chicago, IL: University of Chicago Press.


[^0]:    *Authors for correspondence (e.m.pothos@swansea.ac.uk; jbusemey@indiana.edu).
    The work was carried out equally between the two institutions. Electronic supplementary material is available at http://dx.doi.org/10. 1098/rspb.2009.0121 or via http://rspb.royalsocietypublishing.org.

