# The Einstein Inference: What Fixed Gaps Force

*An addendum to the arc closed in [finale.md](finale.md), prompted by an
analogy: the constancy of the speed of light is a fixed gap, and Einstein
derived special relativity from it. We isolate the inference pattern he
used — postulate one invariant, compute what preserving it costs — show
that the monograph has been running this inference all along (the rigidity
theorem, Zeeman), and then run it once more in a place Einstein never did:
the noisy comparison network. There it yields a **dilation law**: observers
agree on every gap but provably disagree on its precision, and the
discrepancy is given exactly by effective resistance.*

Summary of claims:

- **The inference, isolated (§1).** Einstein's move is a closure operator.
  The maps *invariants → their symmetry group* and *group → its invariants*
  form a Galois connection; "postulate $c$" means: take the closure of one
  invariant and read the rest of physics off it. Everything outside the
  closure is not destroyed but *demoted* — from invariant to reading.
- **Three inferences already run (§2).** The rigidity theorem (theory.md
  2.3) is the inference on the line: keep all pairwise differences, and the
  symmetry group is forced to be translations, so absolute level is forced
  to be gauge. Zeeman's theorem is the inference on the cone. And 1905
  itself was not an enlargement of the group but a *renegotiation*:
  absolute simultaneity, the light cone, and the relativity of motion form
  an inconsistent triple — pick two. Lorentz's ether and Einstein's
  relativity are the two consistent resolutions; the physics was in
  choosing which item to demote.
- **The fourth inference: gap dilation (§3).** In a defended gap network
  under noise, the mean gap is invariant, but its *experienced precision*
  is position-dependent: the variance ratio between any two pairs equals
  their effective-resistance ratio — a dilation factor that is pure network
  geometry, exactly as the time-dilation factor is pure worldline geometry.
  The twin paradox has a network twin: among all comparison routes between
  the same two nodes, the *electrical flow* is the most certain (Thomson's
  principle), as the straight worldline is the oldest. And the fluctuation
  is itself a new fixed gap: effective resistance is a metric, additive
  precisely when the topology is chain-like.
- **The observer enters (§4).** What an observer *knows* acts electrically
  as a short circuit: conditioning the stationary field on a measured
  vantage $O$ replaces the network by the network with $O$ fused to a
  single node, so every conditional variance is again a resistance —
  in the observer's own, shorted, network. Three corollaries: a single
  absolute measurement teaches nothing about any gap (one reading is pure
  gauge — information begins with the first measured *gap*); learning is
  Rayleigh-monotone (the value of a measurement is the resistance drop it
  causes, and an archive is a *shared vantage*); and distinct observers
  can lawfully order the precisions of two gaps *oppositely* — the exact
  twin of the relativity of simultaneity, light cone analogue included.
  All three verified numerically to machine precision.

---

## 1. The inference, isolated

theory.md §5 defined the invariants of a given group: for $\Gamma$ acting
on a state space $S$, $\mathrm{Gaps}(\Gamma)$ is the set of pair functions
$g : S \times S \to V$ with $g(\gamma x, \gamma y) = g(x,y)$. Einstein's
inference runs the map in the *other* direction.

**Definition 1.1.** For a family $F$ of pair functions on $S$, the
**stabilizer** of $F$ is

$$\mathrm{Aut}(F) \;=\; \{\gamma \in \mathrm{Sym}(S) :
g(\gamma x, \gamma y) = g(x, y) \ \text{ for all } g \in F,\ x, y \in S\}.$$

**Proposition 1.2 (the Galois connection).** Both maps are antitone
($F \subseteq F' \Rightarrow \mathrm{Aut}(F) \supseteq \mathrm{Aut}(F')$,
and Prop 5.2 of theory.md for the other direction), and

$$F \subseteq \mathrm{Gaps}(\mathrm{Aut}(F)), \qquad
\Gamma \subseteq \mathrm{Aut}(\mathrm{Gaps}(\Gamma)).$$

Hence $\mathrm{cl}(F) := \mathrm{Gaps}(\mathrm{Aut}(F))$ is a closure
operator on families of pair functions.

*Proof.* Unwinding definitions: each map reverses inclusion because a
larger constraint set is preserved by fewer maps and a larger group
preserves fewer functions; the two composite inclusions hold because $F$
is by construction invariant under its own stabilizer, and $\Gamma$ by
construction stabilizes its own invariants. Closure-operator axioms
(extensive, monotone, idempotent) follow formally from any antitone Galois
pair. ∎

**Definition 1.3 (the Einstein closure and the casualty list).** Call
$\mathrm{cl}(F)$ the **Einstein closure** of $F$: everything you are
forced to keep invariant once you insist on $F$. Pair functions *outside*
$\mathrm{cl}(F)$ are the **casualties**: quantities that cannot be
invariant under any world that preserves $F$. They are not abolished; they
are demoted to *readings* (theory.md §7) — real, observer-dependent
functions over the invariant substrate.

**Interpretation.** The 1905 derivation has exactly this shape. Postulate
$F = \{\text{the light cone}\}$; compute $\mathrm{Aut}(F)$ — by the
Alexandrov–Zeeman theorem (finale.md §3.2) it is the Poincaré group
extended by dilations, in dimension $\ge 3$; read off
$\mathrm{cl}(F)$ — causal order, interval ratios, proper-time comparisons;
and find on the casualty list: simultaneity, elapsed coordinate time,
spatial distance. Special relativity is one invariant plus bookkeeping.
The monograph's slogan — *the gap is fixed but its meaning is not* — is
the casualty half of an inference whose invariant half physics has been
using for a century.

---

## 2. Three inferences already run

**2.1 The line.** Take $F = \{\delta\}$, a separated gap structure on $A$
(theory.md 1.1). The rigidity theorem (theory.md 2.3) computes the
stabilizer: $\mathrm{Aut}(\delta)$ is exactly the group of uniform drifts —
translations by $G$. The closure is then everything determined by the gap
table (theory.md 3.1), and the casualty is the absolute level: Prop 1.3's
gauge freedom is not an accident of the formalism but the *forced demotion*
of absolute value by the decision to hold all pairwise differences
invariant. This is the oldest Einstein inference — older than Einstein:
keep the differences, lose the origin.

**2.2 The cone.** Take $F = \{\text{causal order}\}$, discarding even the
interval's magnitude. Zeeman: the stabilizer is Poincaré $\times$
dilations, so the closure already contains the interval ratios — the
twin-paradox observable — and the full conformal ladder above it
(finale.md §3.1). The weakest-looking invariant has the second-largest
closure in physics.

**2.3 The renegotiation of 1905.** The Galilean and Poincaré groups are
*not* nested — theory.md §5's phrase "relativity = enlarging the group" is
loose on this point, and the closure operator states it precisely. Both
groups extend the same static core (spatial isometries and time
translations); they differ in *which boosts* they admit, and that choice
is decided by the postulated invariant:

$$\text{absolute time gaps} \;\longmapsto\; \text{Galilei}, \qquad
\text{the light cone} \;\longmapsto\; \text{Poincaré}.$$

Insist on *both* invariants and the joint stabilizer contains no boosts at
all: it is the static group, a world with a preferred rest frame. So the
triple

$$\{\ \text{absolute simultaneity},\ \ \text{invariant cone},\ \
\text{relativity of motion}\ \}$$

is inconsistent — **pick two**. Lorentz's ether keeps the two invariants
and demotes the relativity principle (there is a true rest frame, merely
undetectable); Einstein keeps the cone and the relativity principle and
demotes simultaneity to a reading. Both are consistent closures of their
chosen postulates; the experiments could not distinguish them, and the
choice between them was made on the fixed-gap theorist's grounds: prefer
the closure whose casualties were never observable facts to begin with.
Every scientific revolution of this kind is a renegotiation of the ledger —
items move between the *invariant* column and the *reading* column, and
nothing is ever simply destroyed.

| postulated invariant | stabilizer | forced casualties |
|---|---|---|
| all pairwise differences $\delta$ | translations (Thm 2.3) | absolute level (→ gauge) |
| causal order | Poincaré × dilations (Zeeman) | simultaneity, duration, scale (→ readings) |
| light cone + relativity of motion | Poincaré | simultaneity (→ reading) |
| absolute time + cone | static group | relativity of motion (→ ether) |

---

## 3. The fourth inference: gap dilation

Now run the inference where the second half of the monograph lives:
defended gaps under noise (forces.md §2, finale.md §2). Here the invariant
we refuse to give up is the *defended mean gap*. What does keeping it
cost? The answer is a quantity Einstein's instance had no room for:
**precision**. Noise splits the pair's description into an invariant mean
and a fluctuating reading — and the *size* of the fluctuation turns out to
be a new invariant, not of the pair's gap, but of the pair's position.

**3.1 Setting.** As in finale.md §2.4: a connected comparison network $G$
with edge stiffnesses $k_e$, idiosyncratic noise of intensity $\sigma$ at
every node, stationary state the Gaussian free field, so that for *any*
pair,

$$\mathrm{Var}(x_i - x_j) \;=\; \frac{\sigma^2}{2}\, R_{\mathrm{eff}}(i,j),$$

with $R_{\mathrm{eff}}$ the effective resistance under conductances $k_e$.
The estimation-theoretic twin of this law (application.md, Law 1) says the
same of the *maximum-likelihood uncertainty* of a gap estimated from match
data, with Fisher-information conductances. Everything below applies to
both faces.

**3.2 Theorem (gap dilation).** Let $(i,j)$ and $(i',j')$ be any two pairs
in the network — possibly sharing the same mean gap, possibly the same
node. Then

$$\frac{\mathrm{Var}(x_i - x_j)}{\mathrm{Var}(x_{i'} - x_{j'})}
\;=\; \frac{R_{\mathrm{eff}}(i,j)}{R_{\mathrm{eff}}(i',j')},$$

independently of the gaps themselves, of the noise intensity, and of the
gauge.

*Proof.* Immediate from finale.md 2.4: $\sigma^2/2$ cancels. ∎

**Interpretation.** This is the fixed-gap twin of time dilation, clause
for clause. Two observers carry identical clocks (the same invariant);
their worldlines differ; each clock runs true, yet the accumulated times
differ by a factor — $\gamma$ — that depends *only on the geometry of the
worldlines*. Here: two pairs hold the same defended gap (the same
invariant); their network positions differ; each gap is defended
identically, yet the experienced fluctuation differs by a factor that
depends *only on the topology between them*. Same invariant,
position-dependent experience, exact formula for the discrepancy. The
casualty of admitting noise is not the gap — it is the *equality of
confidence*: certainty is relative, and its relativity is as lawful as
simultaneity's.

**3.3 Theorem (twin routes: certainty is extremal).** Suppose each edge
$e$ carries an independent measurement $y_e = \delta_e + \varepsilon_e$ of
its gap, $\mathrm{Var}(\varepsilon_e) = r_e = 1/k_e$. Call a **route
bundle** from $i$ to $j$ any unit flow $f$ on $G$ (a single path is the
special case $f \in \{0, \pm 1\}$). Then:

1. Every route bundle yields an unbiased estimate
   $\hat\delta_f = \sum_e f_e\, y_e$ of the fixed gap $\delta(i,j)$
   — by the cocycle identity, gaps telescope along any unit flow.
2. Its uncertainty is the flow's electrical energy:
   $\mathrm{Var}(\hat\delta_f) = \sum_e f_e^2\, r_e$. For a single path
   $P$ this is the series resistance $\sum_{e \in P} r_e$: **variance is
   additive along a chain of comparisons**, as proper time is additive
   along a worldline.
3. By **Thomson's principle**, the minimum over all route bundles is
   attained by the electrical current flow, and the minimum value is
   exactly $R_{\mathrm{eff}}(i,j)$ — the variance achieved by the optimal
   (maximum-likelihood) pooling of all routes.

*Proof.* (1) For a unit flow $f$ from $i$ to $j$ and exact $\delta_e =
x_v - x_u$, summation by parts gives $\sum_e f_e \delta_e = x_j - x_i$
regardless of the flow chosen; the noise terms have mean zero. (2) is
independence. (3) is Thomson's classical variational characterization of
effective resistance. ∎

**Interpretation.** The reverse triangle inequality made the straight
worldline the *oldest* path between two events (finale.md §3.3); Thomson's
principle makes the electrical flow the *most certain* route between two
nodes. Both are extremal principles over ways of connecting the same fixed
pair, and both say the invariant is experienced best by the "straightest"
connection available. Two analysts who compare the same two players
through different chains of intermediaries are twins in the paradox: they
estimate the *same* fixed gap and return with *different* — lawfully
different — confidences, and the one who routed through fewer, stiffer,
more parallel comparisons is the one who "aged less."

**3.4 Proposition (fluctuation is itself a gap).** $R_{\mathrm{eff}}$ is a
metric on the nodes (the resistance distance), invariant under every
gap-preserving symmetry of the network. It is additive along a chain,
$R_{\mathrm{eff}}(i,k) = R_{\mathrm{eff}}(i,j) + R_{\mathrm{eff}}(j,k)$,
**iff** $j$ separates $i$ from $k$ (every path meets $j$) — so the
"cocycle identity" for precision holds exactly when the comparison
topology is chain-like, and fails by an amount measuring the routes around
$j$.

*Proof.* Symmetry and triangle inequality are the classical resistance-
distance facts; additivity iff separation is the series law together with
the strict variance reduction of any flow avoiding $j$ (Thomson). ∎

**Interpretation.** Admitting noise did not merely blur the old invariant.
It *minted a second one*: every pair now carries the invariant pair
$(\text{mean gap},\ \text{resistance})$ — where you stand, and how firmly.
The first is a gap in the original additive sense; the second is a metric
gap, additive only on tree-like topologies. The theory's own vocabulary
applies to it: a record spliced across the network (finale.md 2.4.4)
changes no mean gap but collapses resistances — it is an intervention
purely on the *second* invariant. Status and security are different
coordinates, and institutions that alter one without the other are acting
on a dimension the mean-gap description cannot even see.

**3.5 The era problem as dilation at historical scale.** application.md's
clustered experiment is this section performed on real data: two
collection eras of Chatbot Arena joined by five bridge models. Within-era
pairs are co-moving observers — low resistance, tight confidence.
Cross-era pairs hold gaps of exactly the same form, but every comparison
routes through the bridge bottleneck; their resistance — and by Theorem
3.2 their variance — is dilated by a factor the battle-count heuristic
cannot predict but the resistance law gets to within a few percent. Chess's
era problem (can Morphy be compared with Carlsen?) is not a sentimental
puzzle but a dilation statement: the cross-era gap exists and is fixed;
what has dilated, lawfully and computably, is the resistance through which
any observer must experience it.

---

## 4. The observer enters: knowledge shorts the network

§3's dilation law compares *pairs*; Einstein's question compares
*observers*. His question, transposed: **what must observers disagree
about, given that they agree on the defended gaps?** To answer it the
observer must be given a formal body.

**Definition 4.1 (observer, vantage, frame).** An **observer** is a node
$k$ together with a **vantage** $O \subseteq A$: the set of nodes whose
instantaneous values the observer has measured — their own trajectory,
their neighbors, whatever records they consult. The observer's **frame**
is the coordinate $x \mapsto x - X_k$: every quantity expressed as a gap
to self. Two frames differ by the fluctuating translation $X_k - X_{k'}$:
in expectation pure gauge, instantaneously a reading. Frames, as in
relativity, are cheap — they change no invariant. Vantages are not.

**Theorem 4.2 (conditional dilation — knowledge shorts the network).**
In the stationary network of §3.1, condition on the observed values
$X_O$. Then for every pair $i, j \notin O$,

$$\mathrm{Var}\!\left(X_i - X_j \,\middle|\, X_O\right)
\;=\; \frac{\sigma^2}{2}\; R_{\mathrm{eff}}^{\,G/O}(i,j),$$

where $G/O$ is the network with the vantage **identified to a single
node** (shorted; internal edges of $O$ become loops and are discarded).
What an observer knows behaves, electrically, as a superconducting island
spliced into the network.

*Proof.* The level of the field is free (only gaps are dynamical), so the
conditional law of the unobserved nodes given $X_O$ is the Gaussian with
covariance $(L_{\bar O \bar O})^{-1}$ — the Green function of the
Laplacian with Dirichlet boundary $O$. That matrix is entry-for-entry the
grounded Laplacian of $G/O$ with ground $s = O$ (identification does not
touch entries between unobserved nodes), and in any grounded network
$G(i,i) + G(j,j) - 2G(i,j) = R_{\mathrm{eff}}(i,j)$. ∎

**Corollary 4.3 (one reading is gauge).** A vantage of size one teaches
nothing: identifying a single node changes no resistance, so
$\mathrm{Var}(X_i - X_j \mid X_v) = \mathrm{Var}(X_i - X_j)$ for every
$v$ and every pair. An observer's first absolute measurement merely fixes
the gauge — Prop 1.3's "the zero point is a convention," now in dynamic
form. Information begins with the second node: with the first measured
*gap*. (Both this and Theorem 4.2 check out numerically to machine
precision on random weighted graphs.)

**Corollary 4.4 (learning is Rayleigh-monotone).** If $O \subseteq O'$,
then $R^{G/O'} \le R^{G/O}$ for every pair — shorting more is Rayleigh's
monotonicity law — so enlarging a vantage never increases any variance,
and the **value of a measurement** for any target gap is exactly the
resistance drop it causes. finale.md 2.4.4's slogan (archives are
long-range edges) sharpens accordingly: **a public record is a shared
vantage** — a short circuit available to every observer at once, which is
why institutions that publish measurements change every observer's
uncertainty about pairs the record never mentions.

**Proposition 4.5 (relativity of confidence order).** Distinct vantages
can order precisions oppositely: there exist networks, pairs $(i,j)$ and
$(i',j')$, and observers $\alpha, \beta$ with

$$\mathrm{Var}_\alpha(X_i - X_j) < \mathrm{Var}_\alpha(X_{i'} - X_{j'})
\quad\text{but}\quad
\mathrm{Var}_\beta(X_i - X_j) > \mathrm{Var}_\beta(X_{i'} - X_{j'}).$$

*Construction.* Two isomorphic well-connected clusters $A$ and $B$ joined
by a single long bridge; $(i,j)$ deep in $A$, $(i',j')$ its mirror image
in $B$; $\alpha$'s vantage two nodes of $A$, $\beta$'s their mirror in
$B$. By symmetry the unconditional precisions are equal. Each observer's
short strictly lowers the near pair's resistance (current does flow
through a vantage inside a well-connected cluster), while affecting the
far pair only through routes that cross the bridge, whose resistance
makes the effect arbitrarily small. The two orderings split oppositely. ∎

**Interpretation.** This is the exact twin of the relativity of
simultaneity: the invariant facts are common to all observers, but a
*derived ordering* proves frame-dependent. And the analogy extends to the
light cone. In Minkowski space, time order is absolute for timelike pairs
and conventional for spacelike ones. Here, each pair carries the
observer-invariant **resistance interval**

$$\left[\, R^{\,G/(V \smallsetminus \{i,j\})}(i,j),\; R^{\,G}(i,j) \,\right]$$

— its precision when everything else is known, and when nothing is. The
confidence order between two pairs is absolute exactly when their
intervals do not overlap; overlapping pairs are the "spacelike" case,
where which gap is better known is not a fact about the network but a
fact about where the asker stands.

**Einstein's question, answered in full.** What must observers disagree
about, given that they agree on the defended gaps? Three things, in
increasing depth: the instantaneous *readings* (they fluctuate;
trivially); the *precision* of any single gap (Theorem 4.2 — dilation
indexed by vantage, not merely by pair); and the *ordering of precisions*
across pairs (Prop 4.5 — the simultaneity twin). And two things no
observer can disagree on: the mean gaps, and the resistance intervals.
Those constitute the invariant substrate; everything else observers say
about the network is lawful motion over it.

---

## 5. Coda: the conservation of structure

Each run of the inference has the same double outcome: a closure and a
casualty list. Nothing on the casualty list is destroyed — simultaneity,
absolute level, felt order, equality of confidence all remain perfectly
real experiences; what they lose is invariance, and what they become is
readings. The ledger's columns are *invariant*, *reading*, *gauge*; a
revolution is a movement of items between columns, conserved in total.

The sequence of demotions now reads: keeping the differences demoted the
origin (theory.md); keeping the cone demoted simultaneity (1905); keeping
the causal order demoted everything but geometry itself (Zeeman, causal
sets); keeping defended gaps in a noisy world demoted the equality of
confidence — certainty became position (§3); and admitting observers
demoted even the *ordering* of certainties to perspective, while minting
the resistance interval as the new invariant beneath it (§4). The last
two entries are this monograph's own additions to the sequence, and they
inherit its practical moral: when an invariant is held fixed, look for
the law governing what was let go. Einstein found time dilation there. In
the world of defended gaps, what lives there is the resistance law — and
every leaderboard confidence interval, every bridge model, every archive
is an engineering decision about it.
