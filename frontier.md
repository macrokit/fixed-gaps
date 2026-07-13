# The Frontier: Slow Recurrence, Noise, and the Invariant Tower

*Resolutions of the three open problems of [readings.md](readings.md) §7,
and of the $n$-ary question of [theory.md](theory.md) §8.5.*

Summary of verdicts:

- **Q1 (beyond BV).** *No*: bounded recurrent readings need not be
  asymptotically almost periodic — $\sin(\log t)$ is a counterexample
  (Thm 1.2). But the failure is structured: such readings are periodic under
  a *conjugate* flow (dilations), and every one-parameter symmetry group
  carries its own anniversary theory with its own frozen phase gaps (§1.3).
- **Q2 (noisy drift).** The conjectured form of the noisy fading law is
  correct — but the fluctuation term *dominates* the gap memory. Felt order
  between gaps survives only to a horizon **quadratic in the gap
  difference** (Thm 2.4), the only noise-proof readings are affine in the
  gap (Thm 2.5), and the present's information about a fixed gap decays like
  $1/t$ — unless records are kept (§2.6).
- **Q3 ($n$-ary invariants).** Gap, affine ratio, and cross-ratio are the
  same object at levels $k = 1, 2, 3$ of a single ladder (Thm 3.2), and by a
  theorem of Tits the ladder **provably terminates** at the cross-ratio
  (Thm 3.3). At maximal symmetry the only surviving invariant is birth
  order — the unkillable fixed gap (§3.4).

---

## 1. Slow recurrence: the answer to Q1 is no, and why that's good

**1.1 The question.** Readings.md classified tame readings and found four
signatures, with the recurrent class generated (in the examples) by periodic
structure. Q1 asked: is every *bounded recurrent* reading asymptotically
almost periodic (a.a.p.) under natural constraints on $F$ — i.e., is
recurrence always calendar-like?

**1.2 Theorem (counterexample).** The reading $m(t) = \sin(\log t)$ — from
$F(u,v) = \sin(\log u)$, continuous and bounded on the reachable states
$t \ge t_0 > 0$ — is bounded and recurrent but *not* asymptotically almost
periodic.

*Proof.* Recurrence: $m$ attains $\pm 1$ at $t = e^{\pi/2 + k\pi}$ for all
large $k$. For a.a.p., we use the compactness criterion: $m$ is a.a.p. iff
its translate family $\{m(\cdot + s)\}_{s \ge 0}$ is relatively compact in
$C_b([0,\infty))$ with the sup norm. Take $s_n = e^{2\pi n}$. On any compact
$[0, K]$,

$$m(t + s_n) = \sin\!\big(2\pi n + \log(1 + t/s_n)\big) = \sin\!\big(\log(1 + t/s_n)\big) \longrightarrow \sin 0 = 0$$

uniformly. So any sup-norm limit $g$ of a subsequence of translates
vanishes on every compact, hence $g \equiv 0$; but every translate has sup
norm $1$ (the oscillation through $\pm 1$ continues beyond any point), so no
subsequence converges to $0$ in sup norm. No convergent subsequence exists:
$m$ is not a.a.p. ∎

**1.3 Diagnosis: anniversaries under conjugate flows.** The counterexample
is not pathological — it is *periodic*, just not under the drift.
$F(u,v) = \sin(\log u)$ satisfies $F(\lambda_0 u, \lambda_0 v) = F(u,v)$
for $\lambda_0 = e^{2\pi}$: it is periodic under the **dilation flow**. In
additive time this appears as log-periodicity: recurrences at
$t, \lambda_0 t, \lambda_0^2 t, \ldots$ — return times growing
geometrically. These are the **doubling anniversaries**: the 1st, 2nd, 4th,
8th year; the celebrations that thin out forever.

The general principle (a time-change lemma): a reading periodic under a
one-parameter flow with clock $\theta(t)$ has the form
$m(t) = P(\theta(t))$ with $P$ periodic, hence is recurrent whenever
$\theta(t) \to \infty$, and is almost periodic in $t$ precisely when the
clock is (asymptotically) proportional to $t$ itself. Drift-periodic
readings ($\theta = t$): calendar anniversaries, a.p. Dilation-periodic
readings ($\theta = \log t$): slowing anniversaries, recurrent but never
a.p. Every one-parameter subgroup of the affine group yields its own
anniversary theory.

**1.4 Phase gaps follow the drift, not the reading.** The pushforward lemma
(readings.md 4.2) applies in each regime *to that regime's own drift group*:
in age-world (additive drift), calendar anniversaries carry the frozen phase
gap $d \bmod p$ — two people's birthdays keep the same calendar distance
forever. In capital-world (multiplicative drift), it is the *octave gap*
$\rho \bmod \lambda_0^{\mathbb{Z}} \in \mathbb{R}_{+}/\lambda_0^{\mathbb{Z}}$
(a circle again, via the homomorphism
$(\mathbb{R}_+, \times) \to \mathbb{R}_+/\lambda_0^{\mathbb{Z}}$) that is
frozen. Mismatched pairs drift: in age-world, two people's *doubling*
anniversaries come into and out of alignment, their coincidences thinning
out forever, while their calendar birthdays stay locked. Which recurrences
stay synchronized is itself a fixed-gap phenomenon — and it is decided by
which group is doing the drifting.

**Amended answer to Q1.** Bounded recurrent readings are asymptotically
almost periodic iff their recurrence is driven by the drift group itself
(calendar-type); recurrence driven by conjugate flows is genuinely slower
than any almost-periodic pattern. The classification of recurrent readings
is *by which one-parameter group they are periodic under* — recurrence, like
fixedness, is relative to a group.

---

## 2. Noisy drift: martingale gaps, the felt-order horizon, and records

**2.1 The model.** Discrete time keeps every proof elementary. Objects
$i \in \{a, b, \ldots\}$ with potentials

$$x_i(t+1) = x_i(t) + \mu_i(t) + w(t+1) + \xi_i(t+1),$$

where $\mu_i(t)$ is object $i$'s predictable drift rate, $w$ is a **common**
shock (the same for all objects; arbitrary, even heavy-tailed or
adversarial), and $\xi_i$ are **idiosyncratic** shocks: martingale
differences, independent across objects, with variance $\sigma^2$.

**2.2 Proposition (noise dichotomy).** Common noise, however wild, preserves
every gap exactly: $\delta_{ab}(t) = x_b(t) - x_a(t)$ is unchanged by $w$.
Under idiosyncratic noise, the gap satisfies

$$\delta_{ab}(t) = d + \sum_{s \le t} \big(\mu_b - \mu_a\big)(s) + M(t),$$

with $M$ a martingale of variance $2\sigma^2 t$; hence $\delta_{ab}$ is a
martingale (**fixed in expectation**) iff $\mu_a \equiv \mu_b$.

*Proof.* The common term cancels in every difference — this is the rigidity
theorem (theory.md 2.3) applied pathwise: common noise is still uniform
drift, just a random one. The decomposition and the martingale criterion are
immediate; the variance adds because the $\xi_i$ are independent. ∎

So the rigidity principle survives noise in sharpened form: *gaps are
immune to any amount of shared turbulence; only asymmetric shocks move
them, and equal mean drift keeps them fixed on average with $\sqrt{t}$
fluctuation.* Wars, recessions, pandemics — everything that hits both
members of a pair alike — leaves every gap untouched.

**2.3 The noisy fading law.** For the ratio reading, with
$\delta(t) = d + M(t)$ as above,

$$m(t) = \frac{x_b}{x_a} = 1 + \frac{d}{t} + \frac{M(t)}{t} + O_p(t^{-3/2}),$$

and the fluctuation term has typical size
$\sqrt{2\sigma^2 t}/t = \sigma\sqrt{2/t}$. The conjectured form (readings.md
§7.2) is thus correct — but note which term wins: the noise floor
$\sigma\sqrt{2/t}$ **dominates** the gap memory $d/t$ as $t \to \infty$. The
signal-to-noise ratio of the felt gap is

$$\mathrm{SNR}(t) = \frac{d/t}{\sigma\sqrt{2/t}} = \frac{d}{\sigma\sqrt{2t}} \longrightarrow 0.$$

In the deterministic world the felt gap fades but remains exact; in the
noisy world it fades *into the noise* — past a horizon, the gap is still
there (in expectation) but can no longer be felt above the turbulence.

**2.4 Theorem (felt-order horizon).** Let two pairs have gaps $d > d'$, all
four objects carrying independent idiosyncratic noise. The probability that
their felt gaps are observed in inverted order at time $t$ is

$$p(t) = \Phi\!\left(-\frac{d - d'}{2\sigma\sqrt{t}}\right) \nearrow \tfrac{1}{2},$$

(Gaussian shocks; in general by the CLT). Thus the order-rigidity corollary
of readings.md (felt gaps compress but never reorder) survives noise only up
to a **crossover horizon**

$$t^\ast \asymp \frac{(d - d')^2}{\sigma^2},$$

beyond which the comparison degenerates to a coin flip.

*Proof.* Inversion means $d + M_1(t) < d' + M_2(t)$ with $M_1, M_2$
independent, each of variance $2\sigma^2 t$; $M_2 - M_1$ has variance
$4\sigma^2 t$, giving the stated probability, which is increasing in $t$
with limit $1/2$. ∎

The horizon is **quadratic in the gap difference**: relationships whose
gaps differ by twice as much keep their felt order four times longer. This
is the noisy world's replacement for order rigidity — order is not
preserved forever, but its half-life is computable.

**2.5 Theorem (the noise-proof readings are affine).** Let
$\delta(t) = d + M(t)$ be a martingale gap with nondegenerate idiosyncratic
noise. For a frozen reading $G(\delta)$ (frozen in the deterministic world
by Prop 1.2 of readings.md):

1. If $G$ is convex, $G(\delta(t))$ is a submartingale:
   $\mathbb{E}\, G(\delta(t))$ is nondecreasing, strictly increasing if $G$
   is strictly convex — **noise systematically inflates convex readings**
   even though the gap itself is fixed in expectation.
2. $\mathbb{E}\, G(\delta(t))$ is constant for all $t$ (and all noise laws
   with full support) iff $G$ is affine.

*Proof.* (1) is conditional Jensen plus the martingale property. (2):
constancy for Gaussian noise forces $G$ to be harmonic for the heat
semigroup, i.e. affine; conversely affine $G$ composed with a martingale is
a martingale. ∎

Deterministically, *every* function of the gap is frozen; noise collapses
this algebra to its affine part. Any convex "cost of distance" — squared
separation, penalties, worry — grows in expectation under symmetric noise.
The gap doesn't move on average; its convex readings do. This is a fixed-gap
version of a familiar phenomenon: volatility is invisible to linear
functionals and taxes all convex ones.

**2.6 Epistemic fading, and what records are for.** Observing only the
present state, the gap estimate is $\delta(t) \sim \mathcal{N}(d, 2\sigma^2 t)$:
the Fisher information about $d$ carried by the present is
$1/(2\sigma^2 t) \to 0$. **Under idiosyncratic noise, the present forgets
the past at rate $\sqrt{t}$.** Ontologically the gap is still fixed in
expectation; epistemically it dissolves — unless the birth values were
*recorded*, in which case estimating $d$ is reading, not inference.

This gives the append-only theme of theory.md §6 an epistemic twin, and
completes a triptych:

- **Ontology:** append-only worlds make gaps fixed (facts are never
  deleted).
- **Phenomenology:** recurrent readings keep gaps *felt* (readings.md §6 —
  ritual).
- **Epistemology:** append-only records keep gaps *known* against the
  $1/t$ information decay (archives, genealogies, ledgers).

A civilization's rituals and its archives are solutions to two different
decay laws attacking the same invariants.

---

## 3. The invariant tower: gap, ratio, cross-ratio — and why it ends

**3.1 $n$-ary frozen readings.** For $n$ objects under uniform additive
drift, state $(x_1, \ldots, x_n) = (t - b_1, \ldots, t - b_n)$: a reading
$F(x_1, \ldots, x_n)$ is frozen for every configuration iff $F$ is constant
on the orbits of the diagonal translation action, iff $F$ factors through
the gap vector $(x_2 - x_1, \ldots, x_n - x_1)$. (Same level-set argument as
Prop 1.2 of readings.md.) The reconstruction theorem extends verbatim: the
gap matrix of $n$ objects determines the configuration up to one global
translation.

**3.2 Theorem (the first-invariant ladder).** Let $\Gamma$ act **sharply
$k$-transitively** on a line-like space $X$ (uniquely mapping any ordered
$k$-tuple of distinct points to any other). Then:

1. There are no nonconstant $\Gamma$-invariants of $j$-tuples of distinct
   points for $j \le k$.
2. The invariants of $(k+1)$-tuples are exactly the functions of a single
   **fundamental invariant**: the coordinate of the last point after the
   unique $\gamma \in \Gamma$ sending the first $k$ points to a fixed
   standard frame.

Applied to the three classical actions on the line / projective line:

| $k$ | group $\Gamma$ | standard frame | fundamental invariant of $(k{+}1)$ points |
|---|---|---|---|
| 1 | translations | $u \mapsto 0$ | the **gap** $\;v - u$ |
| 2 | affine $u \mapsto au + b$ | $(u,v) \mapsto (0,1)$ | the **ratio** $\;\dfrac{w - u}{v - u}$ |
| 3 | projective $PGL_2(\mathbb{R})$ | $(u,v,w) \mapsto (0,1,\infty)$ | the **cross-ratio** $\;[u,v;w,z]$ |

*Proof.* (1): sharp $k$-transitivity makes distinct $j$-tuples ($j \le k$) a
single orbit, on which any invariant is constant. (2): the map
"(tuple) $\mapsto$ image of the last point under the unique frame-fixing
$\gamma$" is well defined by sharpness, invariant by construction, and
complete (two tuples with the same value are matched by composing the two
frame maps). Computing it in each row gives gap, ratio, cross-ratio. ∎

So the gap of theory.md §1, the ratio of the capital-world, and the
cross-ratio of projective geometry are **one construction at three levels**:
each is the first thing the symmetry group cannot destroy, appearing at
arity $k + 1$ — one point beyond what the group can normalize away.

**3.3 Theorem (the tower terminates).** There is no sharply 4-transitive
group acting on an infinite set (Tits, 1952; the sharply 4- and
5-transitive groups are the finite Mathieu groups $M_{11}$, $M_{12}$, plus
small symmetric/alternating cases). Hence on the line the ladder of
fundamental invariants is complete at three rungs:

$$\text{gap} \longrightarrow \text{ratio} \longrightarrow \text{cross-ratio} \longrightarrow \varnothing.$$

The cross-ratio is not just *a* higher invariant — it is provably the
**last** of its kind, even allowing arbitrarily wild (discontinuous) group
actions.

**3.4 The far end: order, the unkillable invariant.** Past the projective
group lies the full order-automorphism group $\mathrm{Homeo}_+(\mathbb{R})$
— every continuous, order-preserving reparameterization of the timeline,
including clocks that run unevenly. It is $k$-transitive for every $k$ (not
sharply), so *all* numerical invariants die; what survives of an $n$-tuple
is exactly its **order type**: who came before whom. And this invariant is
also immune to the noise of §2 — birth *values* fluctuate in felt terms, but
recorded birth *order* is an append-only fact (theory.md §6).

This closes the arc with an explanation the essay could only gesture at:
**birth order is the most robust fixed gap in existence** — the invariant
that survives maximal symmetry (any re-reading of time whatsoever) *and*
maximal noise. Cultures disagree about calendars, i.e. about gap values;
they cannot disagree about order. That the most institutionalized kinship
invariants across human societies — seniority, primogeniture, elder/younger
kin terms — are precisely the ordinal ones is what this theorem would
predict: institutions crystallize around the invariants that require the
least shared measurement to verify.

---

## 4. State of the theory

| question | answer | where |
|---|---|---|
| Are all recurrent readings calendar-like? | No — each one-parameter group has its own anniversary theory; a.p. iff drift-driven | §1 |
| Does the fading law survive noise? | In form yes; but noise dominates past $t^\ast \asymp (\Delta d)^2/\sigma^2$, and only affine readings stay E-fixed | §2 |
| What freezes for $n$ objects, and how far does the invariant tower go? | Functions of the gap matrix; the tower gap → ratio → cross-ratio terminates (Tits), leaving order as the final invariant | §3 |

Remaining genuinely open:

1. **Heavy-tailed noise.** Thm 2.4's horizon assumed finite variance; under
   $\alpha$-stable idiosyncratic shocks the felt-order horizon should scale
   as $(\Delta d)^{\alpha}/\sigma^{\alpha}$ — is order *more* or less
   durable in a world of rare large shocks?
2. **Interacting drifts.** Objects whose drift rates depend on their gaps
   (attraction/repulsion): when do fixed gaps survive as relative
   equilibria, and is there a Lyapunov version of the rigidity theorem?
3. **Higher dimensions.** On $\mathbb{R}^n$ or curved spaces the sharp
   transitivity ladder differs (isometries, conformal maps); compute the
   fundamental-invariant tower for the conformal group — the angle should
   appear where the ratio did.
