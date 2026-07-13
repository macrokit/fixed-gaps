# Readings over a Fixed-Gap Substrate

*Resolution of Conjecture 8.6 of [theory.md](theory.md).*

**Conjecture 8.6 (restated).** Under mild regularity, every reading of an
additively drifting pair decomposes into three time-signatures: decaying,
one-way switching, and accumulating.

**Verdict.** *False as stated, true as amended.* There is an unavoidable
fourth signature — **recurrent** readings (anniversary cycles) — exhibited by
an explicit counterexample (§4). But the amended classification is a theorem
(§5), and the fourth class strengthens rather than weakens the structuralist
thesis: every periodic reading factors through a *new fixed gap* valued in a
quotient group — the **phase gap** (§4.3). What looks like endless oscillation
is frozen structure in a smaller group.

Two byproducts are of independent interest: the **hyperbolic fading law**
(Thm B: the felt size of a fixed gap decays exactly like $d/t$, with a
universal constant), and the **pushforward lemma** (Lem 4.2: homomorphisms
manufacture new fixed gaps from old).

---

## 1. Setup and the drift-derivative lemma

As in theory.md §2, take a pair with fixed gap $d > 0$ under uniform additive
drift. Normalizing the gauge (Prop 1.3 there), the pair's state at time $t$ is

$$s(t) = (x(t),\, x(t) + d), \qquad x(t) = t,$$

a point moving along a line of slope $1$ in the potential plane
$\{(u,v)\}$. A **reading** is $m(t) = F(s(t))$ for some
$F : \Omega \subseteq \mathbb{R}^2 \to \mathbb{R}$ defined on the reachable
states. The four **time-signatures** of a reading:

- **frozen** — $m$ constant;
- **decaying** — $m(t)$ converges as $t \to \infty$ (but is not constant);
- **accumulating** — $m(t) \to +\infty$ or $-\infty$;
- **recurrent** — $\liminf m < \limsup m$: the reading revisits values
  forever.

These four are trivially exhaustive and mutually exclusive; the content of a
classification is in *computing* the signature from the structure of $F$, and
in identifying the building blocks of general readings. That is what follows.

**Lemma 1.1 (drift derivative).** If $F$ is differentiable along the flow
direction, then

$$\dot m(t) = (\mathcal{L}F)(s(t)), \qquad \mathcal{L} := \partial_u + \partial_v,$$

the derivative of $F$ along the drift. Consequently $m$ is frozen for every
pair and every time iff $\mathcal{L}F \equiv 0$ on $\Omega$, and the
signature of $m$ is the convergence class of
$\int^t (\mathcal{L}F)(s(\tau))\, d\tau$.

*Proof.* Chain rule along $s(t) = (t, t+d)$; the integral statement is the
fundamental theorem of calculus. ∎

**Proposition 1.2 (frozen = gap: closing the Klein circle).** $m$ is frozen
for every pair iff $F$ is invariant under the drift group (translations along
$(1,1)$), i.e. iff $F(u,v) = G(v - u)$ for some $G$ — iff $F$ is a function
of the gap alone.

*Proof.* Frozen for every pair means $F$ is constant on every line of slope
$1$ in $\Omega$; these lines are exactly the level sets of $v - u$. (With
differentiability, this is the method of characteristics for
$\mathcal{L}F = 0$; without it, the argument above is direct.) ∎

This closes a circle left open in theory.md: there, gaps were *defined*
structurally (§1) and characterized by symmetry (§5); here they reappear
dynamically — **the fixed gaps are exactly the frozen readings.** Definition
5.1's invariants and the constant observables of the flow are the same class.

---

## 2. The symmetry dictionary

The signature of a reading is computable from its behavior under two groups
acting on the potential plane: translations (the drift) and dilations. The
dictionary:

| $F$ invariant under / homogeneous of | signature | rate |
|---|---|---|
| translations along the drift | frozen | — |
| dilations, degree $0$ | decaying | gap memory $\sim d/t$ |
| dilations, degree $k > 0$ | accumulating | $\sim t^k$; gap relatively negligible |

**Theorem A (translation-invariant readings).** Covered by Prop 1.2: they are
frozen, and they are precisely the gap functions.

**Theorem B (hyperbolic fading law).** Let $F$ be positively homogeneous of
degree $0$ (scale-invariant: $F(\lambda u, \lambda v) = F(u,v)$ for
$\lambda > 0$) and $C^1$ near $(1,1)$. Then for every gap $d$:

$$m(t) = F(1,1) \;+\; F_v(1,1)\,\frac{d}{t} \;+\; O\!\left(\frac{d^2}{t^2}\right).$$

In particular:

1. $m(t) \to F(1,1)$ — a **universal limit**, independent of the gap: all
   pairs read the same in the end.
2. The memory of the gap decays hyperbolically, as $d/t$, with a constant
   $F_v(1,1)$ depending on the reading but not the pair.

*Proof.* By degree-$0$ homogeneity, $F(t, t+d) = F(1, 1 + d/t)$. Taylor
expansion at $(1,1)$ gives the formula. (By Euler's relation
$u F_u + v F_v = 0$, at $(1,1)$ we have $F_u = -F_v$, so one derivative
controls everything.) ∎

*Example.* The ratio reading $F(u,v) = v/u$ gives
$m(t) = (t+d)/t = 1 + d/t$ exactly: the felt seniority of an elder is $d/t$,
i.e. Theorem 4.1 of theory.md with an explicit rate. The "generation gap"
does not fade linearly or exponentially — it fades **hyperbolically**: fast
at first, then ever more slowly, never quite gone.

**Corollary B′ (order rigidity of felt gaps).** To first order, two pairs
with gaps $d$ and $d'$ have felt-gap ratio $d/d'$ at *every* time. Fading is
uniform across pairs: the ordering of relationships by felt gap compresses
toward equality but **never inverts**. (Your two elders always feel unequal
in the same order; they just both fade.)

**Theorem C (homogeneity dictionary and drift duality).**

1. If $F$ is positively homogeneous of degree $k > 0$, continuous at
   $(1,1)$, with $F(1,1) \neq 0$, then $m(t) = t^k\, F(1, 1+d/t) \sim
   t^k F(1,1)$: **accumulating**, with the gap entering only at relative
   order $d/t$.
2. **Duality.** Under *exponential* drift ($x(t) = x_0 e^t$, multiplicative
   gap $v/u = \rho$ fixed — the compounding regime of theory.md §4.3), the
   roles swap: scale-invariant readings are frozen
   ($F(x, \rho x) = F(1,\rho)$), and translation-invariant readings
   accumulate ($G(v-u) = G((\rho - 1)x_0 e^t)$, divergent for monotone
   unbounded $G$).

*Proof.* (1) is the homogeneity identity plus continuity. (2) is direct
substitution; the two regimes are conjugate under $\exp$, which maps additive
drift to multiplicative drift and difference gaps to ratio gaps. ∎

**Interpretation.** Theorem C(2) generalizes the additive/multiplicative
dichotomy of theory.md §4 into a single principle: **a reading is frozen iff
it is invariant under the drift group** (Prop 1.2 in the additive case), and
the interesting long-run behavior belongs to readings invariant under the
*other* group. Age-world (additive drift): differences frozen, ratios decay.
Capital-world (multiplicative drift): ratios frozen, differences explode.
Same theorem, two one-parameter subgroups of the affine group.

---

## 3. Building blocks: the Jordan decomposition of readings

The symmetry dictionary handles structured readings. For *general* (tame)
readings, the three conjectured signatures appear as building blocks.

**Theorem D (decomposition of tame readings).** Let
$m : [t_0, \infty) \to \mathbb{R}$ be of locally bounded variation. Then:

1. $m = P - N$ where $P, N$ are nondecreasing (two **accumulating-type**
   components: the running positive and negative variation).
2. $m = m_{\mathrm{cont}} + \sum_i h_i\, \mathbf{1}[t \ge \theta_i]$, where
   the sum is a countable, locally finite superposition of **threshold
   readings** (the jump part) and $m_{\mathrm{cont}}$ is continuous; the
   decomposition is unique.
3. If the total variation of $m$ is finite, then $P$ and $N$ are bounded
   monotone, hence convergent, hence $m$ converges: **decaying** signature.
4. If $m$ is eventually monotone with infinite total variation, then (since
   local variation is finite) the tail variation is infinite, so the
   monotone tail is unbounded: **accumulating** signature.

*Proof.* (1) is the Jordan decomposition. (2) is the standard splitting of a
BV function into its continuous part and its (countable, locally summable)
jumps. (3): bounded monotone functions converge. (4): a monotone function
with infinite variation on $[T, \infty)$ is unbounded there. ∎

So the conjecture's three types are exactly the atoms of tame readings:
every locally-BV reading is *built from* thresholds and accumulating parts,
and *converges* precisely when its total variation is finite. What Theorem D
cannot rule out is a reading whose variation is infinite while it remains
bounded and non-monotone — and that case is real:

---

## 4. The fourth signature: recurrence, and the gaps hiding inside it

**4.1 Counterexample to the strict trichotomy.** Take
$F(u, v) = \sin(2\pi u / p)$: the reading "where is $a$ in its yearly
cycle" — a birthday clock. Then $m(t) = \sin(2\pi t/p)$ is bounded,
non-convergent, non-monotone, with infinite total variation: **recurrent**,
and not a locally finite superposition of the three conjectured types with a
convergent remainder. Conjecture 8.6 as stated is false. Anniversaries are
not decaying, not one-way, not accumulating — they *return*.

**4.2 Lemma (pushforward of gaps).** Let $\delta$ be a $G$-gap structure on
$A$ (theory.md Def 1.1) and $h : G \to H$ a group homomorphism. Then
$h \circ \delta$ is an $H$-gap structure, and it is fixed under any evolution
that fixes $\delta$.

*Proof.* $h$ preserves the cocycle identity because it preserves addition;
fixedness is immediate. ∎

Pushforwards manufacture derived fixed gaps: the parity of an age gap in
whole years ($\mathbb{Z} \to \mathbb{Z}/2$), and — the case we need — the
**phase gap** $\bar d := d \bmod p \in \mathbb{R}/p\mathbb{Z}$, the gap
pushed into the circle group by $\mathbb{R} \to \mathbb{R}/p\mathbb{Z}$.
The phase gap is the answer to "how far apart in the *calendar* are their
birthdays?" — and it is as frozen as the gap itself.

**4.3 Theorem E (recurrent readings factor through quotient gaps).** Suppose
$F$ is *jointly $p$-periodic along the drift*: $F(u + p, v + p) = F(u, v)$.
Then:

1. Every reading $m(t) = F(t, t+d)$ is $p$-periodic in $t$: pure recurrent
   signature (unless constant).
2. The orbit function $O_d : \mathbb{R}/p\mathbb{Z} \to \mathbb{R}$,
   $O_d(s) = F(s, s + d)$, is well defined, and $m(t) = O_d(t \bmod p)$.
3. Two pairs with gaps $d, d'$ and the same birth phase have identical
   readings for all time iff $O_d = O_{d'}$; pairs with equal gap and
   different birth dates have identical readings *up to the fixed time
   shift* given by their phase gap.

*Proof.* (1) $m(t + p) = F(t + p, t + p + d) = F(t, t + d) = m(t)$.
(2) Well-definedness is exactly joint $p$-periodicity. (3) is (2) applied to
both pairs, with the shift read off from the pushforward gap of 4.2. ∎

**Interpretation.** The recurrent class does not escape the fixed-gap
framework — it *exposes more of it*. A periodic reading carries no new
degrees of freedom beyond (i) a frozen orbit-shape determined by the gap and
(ii) a frozen circle-valued phase. Whether two people's birthdays fall in the
same season, whether two commemorations collide, whether two cycles are in or
out of phase: all frozen at inception, all pushforward gaps. **Anniversaries
are how frozen structure stays perceptible**: a fixed gap is invisible in any
single moment, but a recurrent reading parades it past the observer once per
period, forever. Ritual is the phenomenology of the quotient torsor.

---

## 5. The amended classification theorem

Assembling §§1–4:

**Theorem (Reading Classification).** Let $m(t) = F(t, t + d)$ be a reading
of a fixed-gap pair under uniform additive drift.

1. **(Frozen = invariant.)** $m$ is frozen for every pair iff $F$ is
   drift-invariant iff $F$ is a function of the gap alone (Prop 1.2). The
   frozen readings are exactly the fixed gaps.
2. **(Symmetry determines signature.)** If $F$ is homogeneous of degree $0$
   and $C^1$ near $(1,1)$: decaying, with universal limit and hyperbolic gap
   memory $F_v(1,1)\, d/t$ (Thm B). If homogeneous of degree $k > 0$ with
   $F(1,1) \neq 0$: accumulating like $t^k$ (Thm C). If jointly periodic
   along the drift: recurrent, factoring through the phase gap (Thm E).
3. **(Building blocks.)** Every locally-BV reading is a locally finite
   superposition of threshold readings plus a difference of two continuous
   accumulating components; it is decaying iff its total variation is finite,
   accumulating if eventually monotone with infinite variation, and
   recurrent otherwise (Thm D).
4. **(Exactly four.)** The signature classes {frozen, decaying,
   accumulating, recurrent} are exhaustive and mutually exclusive, and none
   is empty: the conjectured trichotomy misses precisely the recurrent
   class, which is nonempty (§4.1) but adds no unfrozen structure (Thm E).

**Resolution of Conjecture 8.6:** false as a trichotomy; true as the
tetrachotomy above, with the conjectured three types recovered as the atoms
of all tame readings (part 3) and the fourth type revealed as frozen
structure in a quotient group (part 2, Thm E).

---

## 6. What this says about the essay's claims

- **"The gap is fixed but its meaning is not"** now has a rate: for every
  smooth scale-invariant meaning, the felt gap is $c \cdot d / t$. Meaning
  decay is hyperbolic — steep in youth, asymptotically flat, never complete.
  And by Corollary B′, felt gaps compress but never reorder: time equalizes
  proportions while preserving every comparison.
- **The two worlds of §4 (theory.md) are one theorem:** what a domain
  freezes is the drift-invariant readings; what it lets run is the readings
  invariant under the conjugate group. Age-world freezes differences and
  bleeds ratios; capital-world freezes ratios and bleeds differences.
- **Ritual earns a mathematical role:** recurrent readings are the unique
  signature class that keeps a frozen gap *perceptible* indefinitely (frozen
  readings are imperceptible as change; decaying ones fade; accumulating
  ones drown the gap at relative order $d/t$). A culture that wants its
  fixed relations felt must institutionalize periodic readings — birthdays,
  memorials, festivals. The mathematics did not know it was going to say
  that, which is the best sign it is saying something.

## 7. What remains open

1. **Beyond BV:** classify readings of bounded mean oscillation or almost
   periodic type; is every bounded recurrent reading asymptotically almost
   periodic under natural constraints on $F$?
2. **Noisy drift:** with $x(t)$ a random walk with drift, which parts of the
   classification survive in distribution? (Conjecture: Thm B holds with
   $d/t$ replaced by $d/\mathbb{E}x(t)$ plus a $O(t^{-1/2})$ fluctuation
   term.)
3. **Multi-pair readings:** signatures of functions of $n$ objects' states
   under the diagonal drift — where the cross-ratio and birth-order
   invariants of theory.md §8.5 should reappear as the frozen class.
