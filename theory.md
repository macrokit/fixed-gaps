# A Mathematical Theory of Fixed Gaps

*Companion to [essay.md](essay.md). We formalize "fixed gaps" — relations
between entities that are invariant over time — and prove the essay's claims.*

The theory has three pillars:

1. **Gap structures** (§1–§4): quantitative gaps as torsor-like structures,
   where only differences are defined. Main results: absolute values exist
   only up to gauge (Prop 1.3), gaps are fixed *iff* everything drifts
   together (Thm 2.3), the gap table determines the world up to translation
   (Thm 3.1), and fixed additive gaps fade in relative terms (Thm 4.1).
2. **Gaps as group invariants** (§5): the Klein-program view. Which gaps are
   fixed depends on which transformations you admit; relativity is a change
   of group, not a refutation.
3. **Append-only worlds** (§6): qualitative gaps like kinship and causal
   order. Main result: positive existential facts are exactly the kind that,
   once true, stay true (Prop 6.2).

Throughout, $A$ is a nonempty set of *objects* and $(G, +)$ an abelian group
of *gap values* (typically $\mathbb{R}$; §8 drops commutativity).

---

## 1. Gap structures

**Definition 1.1 (gap structure).** A *$G$-gap structure* on $A$ is a map
$\delta : A \times A \to G$ satisfying the **cocycle identity**

$$\delta(a,c) = \delta(a,b) + \delta(b,c) \qquad \text{for all } a,b,c \in A.$$

It is *separated* if $\delta(a,b) = 0 \implies a = b$.

The cocycle identity is the essence of gap-ness: gaps compose along chains.
The age gap from you to your grandmother is your gap to your mother plus hers
to her mother.

**Lemma 1.2.** $\delta(a,a) = 0$ and $\delta(b,a) = -\delta(a,b)$.

*Proof.* Setting $a=b=c$ in the cocycle identity gives
$\delta(a,a) = 2\,\delta(a,a)$, so $\delta(a,a)=0$. Then
$\delta(a,b) + \delta(b,a) = \delta(a,a) = 0$. ∎

**Proposition 1.3 (gauge freedom — "the zero point is a convention").**
Fix any $a_0 \in A$ and define $f(x) := \delta(a_0, x)$. Then

$$\delta(a,b) = f(b) - f(a) \quad \text{for all } a, b.$$

Moreover, if $f'$ is any other function with $\delta(a,b) = f'(b) - f'(a)$,
then $f' - f$ is constant. Conversely, every $f : A \to G$ defines a gap
structure by $\delta(a,b) := f(b) - f(a)$.

*Proof.* $f(b) - f(a) = \delta(a_0,b) - \delta(a_0,a)
= \delta(a,a_0) + \delta(a_0,b) = \delta(a,b)$ by the cocycle identity and
Lemma 1.2. If $f'(b)-f'(a) = f(b)-f(a)$ for all $a,b$, then
$(f'-f)(b) = (f'-f)(a)$, i.e. $f'-f$ is constant. The converse is a direct
check of the cocycle identity. ∎

**Interpretation.** Gap structures on $A$ are exactly *potentials modulo
constants*. You can always assign absolute values (a birthdate coordinate, a
voltage, a height above sea level) consistent with the gaps — but never
canonically: the assignment is unique only up to a global constant. The
"absolute value" is real *as a gauge choice* and fictional *as a fact*. This
is precisely why the zero of potential energy, of voltage, and of longitude
are conventions, while their differences are physics.

Note that $\delta$ is separated iff $f$ is injective, so a separated gap
structure embeds $A$ into $G$; if $f$ is also surjective, $A$ is a
*$G$-torsor* — a copy of the group that has forgotten its identity element.
Time itself is the paradigm: instants form an $\mathbb{R}$-torsor; there is
no "instant zero," only durations.

---

## 2. Dynamics: when is a gap fixed?

**Definition 2.1.** An *evolution* of $A$ is a family of maps
$\varphi_t : A \to A$, $t \in T$ (time; any monoid acting on $A$). The gap
structure $\delta$ is **fixed under $\varphi$** if

$$\delta(\varphi_t a, \varphi_t b) = \delta(a, b) \qquad \text{for all } a, b \in A,\ t \in T.$$

**Proposition 2.2 (common drift $\Rightarrow$ fixed).** Suppose the evolution
is a *uniform drift*: there exist $g_t \in G$ with
$f(\varphi_t a) = f(a) + g_t$ for all $a$ (every object's potential advances
by the same amount). Then $\delta$ is fixed under $\varphi$.

*Proof.* $\delta(\varphi_t a, \varphi_t b) = f(\varphi_t b) - f(\varphi_t a)
= (f(b) + g_t) - (f(a) + g_t) = \delta(a,b)$. ∎

Ages are the motivating case: with birthdates $b_i$ and $f = $ age,
$f_t(i) = t - b_i$ advances at rate $1$ for everyone, so all age gaps are
conserved.

The converse is the substantive theorem: uniform drift is not just *a* way to
keep gaps fixed — it is the *only* way.

**Theorem 2.3 (rigidity).** Let $\delta$ be a separated gap structure and
$\varphi : A \to A$ any map with
$\delta(\varphi a, \varphi b) = \delta(a,b)$ for all $a,b$. Then
$h(a) := \delta(a, \varphi a)$ is constant in $a$ — i.e. $\varphi$ is a
uniform drift.

*Proof.* For any $a, b$:

$$\delta(a, \varphi a) = \delta(a,b) + \delta(b, \varphi b) + \delta(\varphi b, \varphi a)
= \delta(a,b) + \delta(b,\varphi b) - \delta(\varphi a, \varphi b)
= \delta(b, \varphi b),$$

using the cocycle identity, Lemma 1.2, and gap-preservation. ∎

**Corollary 2.4.** The symmetry group of a separated gap structure — all
invertible gap-preserving self-maps — is exactly the group of uniform drifts,
a subgroup of $G$ acting by translation. For a torsor it is all of $G$.

**Interpretation.** Fixed gaps and lockstep motion are *equivalent*. Age gaps
are frozen because everyone ages at the same rate; Theorem 2.3 says any
frozen quantitative gap forces an "equal aging rate" for the quantity behind
it. Conversely, gaps break exactly when drift stops being uniform — which is
precisely what special relativity discovered about elapsed time (§5). This is
a small Noether principle: the conserved quantity (all pairwise differences)
corresponds exactly to the symmetry (global translation).

---

## 3. Reconstruction: structuralism as a theorem

**Theorem 3.1.** Let $\delta$ be a separated $G$-gap structure on $A$. Then
the potential $f : A \hookrightarrow G$ of Prop 1.3 is determined by the gap
data uniquely up to a single additive constant. Consequently:

1. The full gap table $\{\delta(a,b)\}_{a,b \in A}$ determines the
   configuration of all objects up to one global translation of $G$.
2. Any two gap structures with the same gap table are isomorphic via a unique
   gap-preserving bijection matching corresponding objects.

*Proof.* Immediate from Prop 1.3 (existence and uniqueness-up-to-constant of
potentials) and Theorem 2.3 (gap-preserving maps are translations). ∎

**Interpretation.** The relations *are* the reality: the complete table of
gaps pins down everything about the configuration except an absolute origin —
which is exactly the datum that was never observable in the first place. This
is the essay's structuralist claim (Leibniz contra Newton) in theorem form.
Nothing about the objects' "positions" exceeds the gap data plus one
unphysical choice.

---

## 4. The convergence theorem: why fixed gaps fade

Additive invariance and multiplicative invariance behave oppositely, and the
human phenomenology of age gaps falls out of the additive case.

**Theorem 4.1 (relative fading).** Let $x(t), y(t) \to \infty$ with
$x(t) - y(t)$ bounded. Then $x(t)/y(t) \to 1$.

*Proof.* $x/y = 1 + (x - y)/y$, and the numerator is bounded while
$y \to \infty$. ∎

**Corollary 4.2 (ages).** For ages $a_i(t) = t - b_i$, every pairwise gap
$a_i - a_j = b_j - b_i$ is exactly conserved, while every ratio
$a_i / a_j \to 1$. All beings become contemporaries in the limit.

**Contrast 4.3 (multiplicative gaps diverge).** If instead the *ratio* is
invariant, $x(t) = \lambda\, y(t)$ with $\lambda > 1$ and $y \to \infty$,
then $x - y = (\lambda - 1)\, y \to \infty$: fixed relative gap, exploding
absolute gap. Compound growth (wealth, populations, citation counts) lives in
this regime.

**Interpretation.** "Which kind of gap does the domain conserve?" is the
first question to ask of any inequality. Domains with additive conservation
(age, seniority) *equalize in proportion* over time; domains with
multiplicative conservation (compounding capital) *diverge in absolute terms*
while looking statically "fair" in ratio. The lived softening of the
parent–child hierarchy and the widening of compounding wealth are the two
branches of the same dichotomy.

---

## 5. Gaps as invariants of a group: the Klein view

Sections 1–4 assumed the gap values were differences in an abelian group.
The general notion drops that: a gap is *anything about a pair that the
admissible transformations cannot touch*.

**Definition 5.1.** Let a group $\Gamma$ act on a state space $S$. A
*$\Gamma$-gap* with values in a set $V$ is a map $g : S \times S \to V$
invariant under the diagonal action:

$$g(\gamma x, \gamma y) = g(x, y) \qquad \text{for all } \gamma \in \Gamma,\ x, y \in S.$$

Write $\mathrm{Gaps}(\Gamma)$ for the set of such invariants.

**Proposition 5.2 (more symmetry, fewer gaps).** If
$\Gamma \subseteq \Gamma'$ then
$\mathrm{Gaps}(\Gamma') \subseteq \mathrm{Gaps}(\Gamma)$.

*Proof.* Invariance under every element of $\Gamma'$ includes invariance
under every element of $\Gamma$. ∎

**Examples.**

| Admissible group $\Gamma$ | Surviving gaps | Casualties |
|---|---|---|
| time translations | age differences, order of birth | absolute dates |
| Euclidean isometries | distances, angles | absolute positions, orientations |
| Galilean group | relative velocities; distances at a common instant | absolute velocity ("the ether") |
| Poincaré group | spacetime interval, proper time, causal order | simultaneity, elapsed coordinate time, spatial distance |

**Interpretation.** "Is this gap fixed?" is not absolute — it is relative to
the group of transformations the world (or the observer) is allowed to apply.
Special relativity did not refute the fixed-gap thesis; it *enlarged
$\Gamma$*, which by Prop 5.2 shrank the inventory of invariant gaps, leaving
the deeper ones (the interval, the causal order). The research program of
physics can be read as: find nature's true $\Gamma$, then compute
$\mathrm{Gaps}(\Gamma)$ — and Theorem 2.3 is the special case saying that
for one-dimensional additive quantities, conserving all pairwise gaps *is*
translation symmetry.

---

## 6. Append-only worlds: kinship, causality, ledgers

Kinship gaps ("she is my sister") are not numbers, and their fixedness has a
different mechanism: not lockstep drift, but the *append-only* character of
the past. We model it logically.

**Definition 6.1.** Fix a relational signature $\sigma$ (e.g. binary
$\mathrm{parent}(x,y)$). A *history* is a chain of $\sigma$-structures

$$M_0 \subseteq M_1 \subseteq M_2 \subseteq \cdots$$

where each inclusion is *append-only*: the universe may gain elements and
relations may gain tuples, but no element or atomic fact is ever removed. A
property $P(\bar a)$ is **stable** (a fixed gap) if
$M_s \models P(\bar a)$ implies $M_t \models P(\bar a)$ for all $t \ge s$.

**Proposition 6.2.** Every *existential-positive* formula — built from
atomic formulas using only $\wedge$, $\vee$, and $\exists$ — is stable.
Formulas involving negation or universal quantification need not be.

*Proof.* Induction on formula structure. Atomic facts persist by the
append-only condition. Conjunction and disjunction preserve persistence. For
$\exists x\, \psi$: a witness in $M_s$ still exists and still satisfies
$\psi$ in $M_t$ by the inductive hypothesis. For the negative claim, two
counterexamples: $\neg\exists y\, \mathrm{parent}(x,y)$ ("$x$ is childless")
is destroyed by appending a child; $\forall y\, (\mathrm{parent}(x,y) \to
\mathrm{parent}(z,y))$ is destroyed by appending a child of $x$ alone. ∎

**Application (kinship).** Parenthood edges are appended at birth and never
deleted. Hence *sibling* ($\exists z\,\mathrm{parent}(z,x) \wedge
\mathrm{parent}(z,y)$), *grandparent*, *cousin*, and *ancestor* (a monotone
transitive closure, an increasing union of existential-positive formulas) are
all stable — fixed forever once true. The asymmetry of family life falls out
of the syntax: **positive kinship facts are fixed; negative ones ("childless,"
"unmarried," "only child") are not.** Blood relations are fixed gaps not
because of biology per se, but because the world never un-happens an event.

**Application (causality and ledgers).** Causal precedence is a partial order
to which history only ever *adds* comparable pairs; an existing pair
$a \prec b$ is never reversed — order facts are atomic, hence stable. A
blockchain is this proposition turned into engineering: an append-only
structure whose entire security model is making retro-deletion of facts
computationally infeasible. It is a machine for *manufacturing* fixed gaps
(confirmed precedence of transactions) in an adversarial environment.

**Remark.** Prop 6.2 is the finger-exercise version of preservation theorems
in model theory (Łoś–Tarski; the homomorphism-preservation theorem of
Rossman), which characterize stable properties as *exactly* the
existential-positive ones under suitable hypotheses. In slogan form: *the
fixed gaps of an append-only world are precisely its positive existential
facts.*

---

## 7. The meaning layer: readings over a frozen substrate

The essay claims: "the gap is fixed, but its meaning is not." Formally:

**Definition 7.1.** Given a gap structure with potential $f_t$ evolving by
uniform drift (so all gaps are fixed), a *reading* is any function
$m(a, b, t)$ of the pair's full state — not required to be invariant.

Readings vary even though gaps do not, because they can depend on the
absolute potentials, not just their difference. Three canonical readings of
an age pair with fixed gap $d = f(b) - f(a) > 0$:

- **Ratio reading** $m = f_t(b)/f_t(a)$: decays monotonically to $1$
  (Thm 4.1). *Authority, era-membership, "different generations."* Fades on
  schedule.
- **Threshold reading** $m = \mathbf{1}[f_t(a) \ge \theta]$: flips once,
  permanently, at a computable time. *Adulthood, retirement, outliving.*
- **Positional reading** $m = $ the pair's location in a fixed order
  lattice: never changes, but each object's *other* relations accumulate
  around it (§6 appends). *Becoming a parent while remaining a child.*

**Claim (informal).** The dynamics of long-term relationships is exhausted by
the motion of readings over the frozen gap substrate. Nothing structural
moves; everything interpretive does — and the three reading types above
(decaying ratios, one-way thresholds, accumulating positions) are the three
characteristic time-signatures of that motion.

---

## 8. Extensions and open problems

1. **Non-abelian gaps.** Replace $(G,+)$ with any group and the cocycle
   identity with $\delta(a,c) = \delta(a,b)\cdot\delta(b,c)$. Everything in
   §1–§3 survives with care about sides. Example: relative orientation
   between rigid bodies ($G = SO(3)$) — a fixed gap when bodies rotate in
   lockstep.
2. **Categorical form.** A gap structure is exactly a functor from the pair
   groupoid of $A$ (objects $A$, one isomorphism between each pair) to $G$
   viewed as a one-object groupoid; the cocycle identity is functoriality.
   Fixedness of $\delta$ under an evolution is naturality. What do gap
   structures valued in a general groupoid buy?
3. **Noisy gaps.** Gaps fixed only in expectation, or as martingales:
   $\mathbb{E}[\delta_{t+1} \mid \mathcal{F}_t] = \delta_t$. Which of
   Theorems 2.3 and 3.1 survive in distribution? (Candidate domain: relative
   skill ratings, exchange rates.)
4. **Almost-fixed gaps.** Slowly varying invariants
   ($|\dot\delta| \le \epsilon$, adiabatic invariants): quantify how much of
   the reconstruction theorem (Thm 3.1) degrades with $\epsilon$ — a
   stability-of-structuralism question.
5. **$n$-ary gaps.** Invariants of triples and $n$-tuples under the diagonal
   action (Def 5.1 with $S^n$): birth-order permutations, angles,
   cross-ratios. The cross-ratio — the fixed gap of projective geometry — is
   a 4-ary example, suggesting a hierarchy: which geometries have no fixed
   binary gaps at all, only higher-arity ones?
   **Resolved in [frontier.md](frontier.md) §3:** the hierarchy is the
   sharp-transitivity ladder — a sharply $k$-transitive group has its first
   invariant at arity $k+1$ (gap, ratio, cross-ratio at $k = 1, 2, 3$) —
   and by Tits's theorem on sharply 4-transitive groups the ladder
   terminates at the cross-ratio, leaving order type as the sole invariant
   of maximal symmetry.
6. **Classifying readings.** Given a fixed-gap substrate, classify all
   readings by asymptotic behavior. Conjecture (informal): under mild
   regularity, every reading of an additively drifting pair decomposes into
   the three time-signatures of §7 — decaying, one-way switching, and
   accumulating components.
   **Resolved in [readings.md](readings.md):** false as a trichotomy — there
   is an unavoidable fourth signature, *recurrent* readings (anniversary
   cycles) — but true as an amended tetrachotomy. The three conjectured
   types are recovered as the building blocks of all locally-BV readings,
   the signature is computable from the reading's symmetry (with a
   quantitative *hyperbolic fading law*: gap memory decays as $d/t$), and
   the recurrent class factors through a new fixed gap valued in a quotient
   group (the *phase gap*), strengthening the structuralist thesis.
