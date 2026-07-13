# Melting, Frustration, and the Causal Web

*Resolutions of the three remaining problems of [forces.md](forces.md) §4 —
and the close of the arc.*

Summary of verdicts:

- **Q1 (melting of defended gaps).** There is an adiabatic theory: a
  defended gap tracks its drifting equilibrium with lag proportional to
  (rate of change)/(stiffness), and it dies in exactly three ways — *snap*
  (drift too fast), *tip* (saddle-node melting, with a universal
  $\epsilon^{2/3}$ overshoot law), or *leak* (noise-driven escape when the
  barrier falls to the noise temperature). All three deaths share one
  observable prodrome: rising fluctuation and slowing recovery — the
  variance of a defended gap inflates before it dies (§1).
- **Q2 (networks of gaps).** Local defense implies global rigidity on the
  line iff the interaction graph is connected; the obstruction to a
  *consistent* network of preferred gaps is cohomological (frustration =
  the cycle-space component of the preferred-gap cochain), and the original
  gap structures of theory.md are exactly the frustration-free case. Under
  noise, the fluctuation of any gap equals noise intensity times **effective
  resistance** — so chains lose long-range order, planar networks lose it
  logarithmically, and only well-connected (transient, expander-like)
  comparison networks keep a globally rigid order (§2).
- **Q3 (the Lorentzian ladder).** The tower in Minkowski space is exactly
  parallel to the Euclidean one — interval (2 points) → interval ratios
  (3 points, the twin-paradox observable) → interval cross-ratios (4 points,
  the invariants of conformal field theory) — and terminates by the
  Lorentzian Liouville theorem. The conjecture that the tower is *shorter*
  was wrong; the truth is stranger: by Zeeman's theorem the discrete bottom
  rung (causal order alone) already generates the entire group in dimension
  $\ge 3$. And causal set theory proposes the final inversion: the world
  does not *have* a gap structure — it *is* one (§3).

---

## 1. Melting: how defended gaps die

**1.1 Setup.** Take a defended gap (forces.md §2) whose potential drifts
slowly: $\dot\delta = \psi(\delta, s)$ with slow time $s = \epsilon t$,
equilibrium branch $\delta^\ast(s)$ (where $\psi = 0$), and stiffness
$k(s) = -\partial_\delta \psi(\delta^\ast(s), s) > 0$. The institution, the
force, the habit that defends the gap is itself changing.

**1.2 Lemma (tracking lag).** Writing $\delta(t) = \delta^\ast(\epsilon t) +
\eta(t)$ and linearizing, $\dot\eta = -k\eta - \epsilon\, {\delta^\ast}'(s)$,
whose quasi-stationary solution is

$$\eta_{\mathrm{qs}} = -\,\epsilon\,\frac{{\delta^\ast}'(s)}{k(s)}.$$

A defended gap follows its moving equilibrium with a lag equal to *(speed of
the target) / (stiffness of the defense)*, scaled by the melting rate. Slow
change is tracked gracefully; the tradition bends.

**1.3 The three deaths.** The lemma fails in three distinct ways, which
exhaust the phenomenology:

1. **Snap** — the lag exceeds the basin: if
   $\epsilon\, |{\delta^\ast}'|/k > R$ (the basin half-width), the gap
   detaches from its equilibrium and the dynamics carries it elsewhere.
   Critical melting rate: $\epsilon_c \approx k R / |{\delta^\ast}'|$. Yes,
   there is a critical rate — reform faster than $\epsilon_c$ and the gap
   does not adapt; it breaks.
2. **Tip** — the equilibrium itself is annihilated: as $V$ drifts, a
   minimum can merge with the adjacent maximum (saddle-node), $k(s) \to 0$
   at some $s_c$. No slowness saves the gap here, but its death is
   *delayed*: by the classical dynamic saddle-node analysis
   ($\dot x = \mu(\epsilon t) + x^2$), the gap survives past the static
   melting point by a parameter overshoot of order $\epsilon^{2/3}$ —
   the universal lag of tipping points. Institutions outlive the conditions
   that sustained them, by a computable margin.
3. **Leak** — noise preempts geometry: with noise intensity $\sigma$, the
   Kramers escape rate $\sim e^{-2\Delta V(s)/\sigma^2}$ becomes order-one
   when the shrinking barrier reaches the noise temperature,
   $\Delta V(s) \sim \sigma^2$. The gap dies *before* the static or dynamic
   melting point — turbulent worlds melt their defended gaps early. (Under
   heavy-tailed noise, by forces.md 2.4.3, the leak is polynomial-fast and
   happens by one identifiable shock.)

**1.4 The early-warning theorem.** All three deaths are preceded by the same
observable signature. Near melting, $k(s) \to 0$ (tip) or the effective
barrier shrinks (leak), and the stationary fluctuation of the defended gap
is $\sigma^2/(2k)$ with autocorrelation time $1/k$: **the variance of a
defended gap inflates, and its recovery from perturbations slows, before it
dies.** This is critical slowing down, familiar as the early-warning signal
of tipping points in climate and ecosystems — here derived as a general fact
about *any* defended invariant. A relationship, a norm, a peg, a spacing
that starts fluctuating more and recentering slower is not "still fine but
noisy"; it is announcing the death of its restoring force. Watch the
variance, not the mean: the mean is the last thing to move.

---

## 2. Networks: frustration is cohomology, defense is resistance

**2.1 Setup.** Objects $1, \ldots, n$ on the line; an interaction graph $G$
with edge set $E$; only adjacent pairs defend their gap, with preferred
(signed) gaps $g_e$ and quadratic energy
$\mathcal{U}(x) = \sum_{e = (i,j) \in E} \tfrac{k_e}{2}\big((x_j - x_i) -
g_e\big)^2$. When does local defense pin the *global* configuration —
including the gaps of non-adjacent pairs?

**2.2 Theorem (connectivity is rigidity; frustration is cohomology).**

1. The configuration modulo translation is determined by the edge gaps iff
   $G$ is connected: gaps propagate along paths by the cocycle identity, so
   a spanning tree of defended edges pins every pairwise gap.
2. The preferred gaps $\{g_e\}$ are simultaneously realizable iff the
   1-cochain $g$ is **exact** ($g_e = f_j - f_i$ for node values $f$), iff
   its sum around every cycle vanishes. The obstruction lives in the cycle
   space $\cong H^1(G; \mathbb{R})$: each independent cycle carries a
   **frustration number** (the sum of preferred gaps around it).
3. In general the equilibrium realizes the ($k_e$-weighted) orthogonal
   projection of $g$ onto the exact cochains — a discrete Hodge
   decomposition. The residual cycle component is never realized; it is
   distributed as permanent strain, with minimum energy
   $\tfrac{1}{2}\|g_{\mathrm{cyc}}\|_k^2$.

*Proof.* (1): differences telescope along paths; connectivity makes every
pair joined. (2): exactness $\Leftrightarrow$ vanishing cycle sums is the
elementary homology of graphs. (3): minimizing a quadratic in $dx$ over the
space of exact cochains is the stated projection. ∎

**2.3 The origin story of the cocycle identity.** Part (2) reframes the
entire theory: theory.md's Definition 1.1 — a gap structure is a $\delta$
satisfying the cocycle identity — is precisely the statement that $\delta$
is an *exact cochain on the complete graph*, and Prop 1.3 (gauge freedom)
is its potential. So the original theory was, from the start, the
**frustration-free case** of a general theory of gap networks. Real social
and physical networks need not be frustration-free: A wants a certain gap to
B, B to C, and C to A, and the three preferences may not sum to zero. Then
*no* configuration satisfies everyone; the equilibrium is the Hodge
projection — the closest consistent world — and the frustration numbers
measure, cycle by cycle, how much relational preference is structurally
unsatisfiable. Some conflict is not misunderstanding; it is cohomology.

**2.4 Theorem (defense is resistance).** Add idiosyncratic noise of
intensity $\sigma$ to each node of a connected defended network (Langevin
dynamics on $\mathcal{U}$). The stationary fluctuation of the gap between
*any* two nodes — adjacent or not — is

$$\mathrm{Var}(x_i - x_j) = \frac{\sigma^2}{2}\, R_{\mathrm{eff}}(i, j),$$

the **effective resistance** between $i$ and $j$ in the network with edge
conductances $k_e$ (the stationary law is the Gaussian free field on $G$).

*Consequences (with the classical asymptotics of $R_{\mathrm{eff}}$):*

1. **Chains lose order.** On a path/1-D lattice (each rank comparing only
   to its neighbors), $R_{\mathrm{eff}}(i,j) = |i - j|/k$: gap variance
   grows *linearly* with separation. A hierarchy defended only by
   adjacent-rank comparisons drifts unboundedly at long range — rank
   inflation as the social instance of the Landau–Peierls theorem (no 1-D
   crystalline long-range order).
2. **Planar networks are marginal.** On a 2-D lattice,
   $R_{\mathrm{eff}} \sim \log|i - j|/k$: order decays, but only
   logarithmically.
3. **Well-connected networks keep global order.** On transient graphs
   (3-D lattices) and expanders, $R_{\mathrm{eff}}$ is uniformly bounded:
   every gap in the network, however distant, fluctuates within a fixed
   band. Global rigidity of a defended order is a *connectivity* property —
   it requires comparison paths that are numerous and short.
4. **Records are long-range edges.** A written record fixing the gap
   between two distant nodes is an edge of enormous conductance spliced
   across the network, collapsing $R_{\mathrm{eff}}$ for every pair whose
   paths route through it. The epistemic role of archives (frontier.md
   §2.6) acquires a structural counterpart: archives are the shortcuts that
   make a comparison network transient.

**2.5 Rigidity percolation.** If each potential comparison edge exists
independently with probability $p$, global rigidity on the line is exactly
connectivity of the random graph, so the rigidity threshold is the
connectivity threshold (for $G(n, p)$: $p = \log n / n$). In genuinely
$d \ge 2$-dimensional embeddings, rigidity requires more than connectivity
(Laman-type counting; generic rigidity percolation has a strictly higher
threshold) — pinning *shapes* is harder than pinning *lines*, consistent
with §3's theme that dimension changes what invariants cost.

---

## 3. The Lorentzian ladder: order generates geometry

**3.1 The ladder.** Compute the fundamental-invariant tower of Minkowski
space $\mathbb{R}^{1, n-1}$ ($n \ge 3$), group by group, exactly as in
forces.md §3.1:

| group | first nontrivial arity | fundamental invariant |
|---|---|---|
| Poincaré | 2 | the **spacetime interval** $I(x,y)$ — the gap |
| causal group (Poincaré $\times$ dilations) | 2 (discrete), 3 (continuous) | the **causal type** of a pair (before / after / elsewhere / lightlike); then **interval ratios** |
| Lorentzian conformal group $O(2, n)$ | 4 | the **interval cross-ratios** $\dfrac{I_{13}\, I_{24}}{I_{14}\, I_{23}}$ |

Reading the rungs: the Poincaré-level invariant of a pair is the interval —
the gap, as theory.md §5 already tabulated. Adding dilations (the causal
group) kills the interval's magnitude, leaving a *discrete* pair invariant —
the causal relation itself — with the first continuous invariant appearing
at three points as ratios of intervals: for three causally related events,
the ratio of proper times along the two legs. This is precisely the
twin-paradox observable — *how much more one path ages than another* — the
Lorentzian "shape," standing exactly where the angle stood in Euclidean
space and the ratio stood on the line. At four points, the conformal group
leaves the interval cross-ratios: exactly the variables on which conformal
field theory correlators depend. The tower terminates by the Lorentzian
Liouville theorem: for $n \ge 3$ the conformal transformations of Minkowski
space form the finite-dimensional group $O(2, n)$; there is nothing above.

**3.2 Scoring the conjecture.** Forces.md §4.3 conjectured that proper time
plays the gap's role (correct, at the Poincaré rung) and that the tower is
*shorter* than the conformal one (wrong). The tower has the same three
rungs — gap, shape, cross-ratio. What is genuinely different in Lorentzian
signature is the *bottom*:

**Theorem (Zeeman, 1964).** For $\dim \ge 3$, every bijection of Minkowski
space preserving the causal order (in both directions) is an orthochronous
Poincaré transformation composed with a dilation.

The discrete arity-2 invariant — mere order, the weakest-looking rung —
already pins the entire group, hence the entire ladder above it. In
Euclidean space, order was the last survivor of maximal symmetry
(forces.md 3.3); in Lorentzian signature it is promoted to *generator*:
preserve who-can-influence-whom, and you have preserved the geometry, the
intervals up to scale, everything. (Dimensional wrinkle, mirroring the
privilege of the line: in $1{+}1$ dimensions Zeeman fails — the causal
automorphisms $(u, v) \mapsto (f(u), g(v))$ on null coordinates form an
infinite-dimensional group. Order generates geometry only when spacetime is
wide enough for light cones to interlock.)

**3.3 Age as the longest chain.** In Minkowski space the reverse triangle
inequality holds: for timelike-related events,
$\tau(x, z) \ge \tau(x, y) + \tau(y, z)$ — the straight path through
spacetime is the *oldest*. Proper time, the relativistic age, is the length
of the longest causal chain between two events. The essay's opening
quantity — age — reappears at the foundation of physics not as a coordinate
but as an extremal statistic of the order itself.

**3.4 The final inversion.** Causal set theory (Bombelli–Lee–Meyer–Sorkin)
takes the last step: it proposes that spacetime *is* a locally finite
partial order — a discrete web of fixed precedence-gaps — from which
geometry is recovered as bookkeeping: volume from counting elements,
proper time from longest chains, dimension and curvature from order
statistics. Its slogan: *order plus number equals geometry.*

If anything like this is right, the arc of these documents closes on an
inversion. We began with gaps as frozen facts *between* things — ages,
kinships — held in place by a world. Every document since has stripped the
things of standing: only gaps are measurable (theory), objects are
recoverable from gaps up to gauge (theory), what changes is only readings
(readings), what survives symmetry and noise is order (frontier, forces).
The causal-set endpoint is the limit of that progression: there is no world
holding the gaps in place. The web of fixed gaps is the world, and
spacetime, matter, and we ourselves are its readings.

---

## 4. Coda: the arc, complete

Each document's slogan, in order:

1. **[essay.md](essay.md)** — between people and objects alike, what
   persists are relations, not conditions.
2. **[theory.md](theory.md)** — gaps are fixed iff everything drifts
   together; the gap table is the world up to gauge; append-only worlds fix
   their positive facts.
3. **[readings.md](readings.md)** — meaning is a reading over a frozen
   substrate: four signatures, hyperbolic fading, and anniversaries as
   quotient gaps.
4. **[frontier.md](frontier.md)** — recurrence is relative to a group;
   noise buries felt order at a quadratic horizon; the invariant tower ends
   at the cross-ratio, leaving birth order.
5. **[forces.md](forces.md)** — heavy tails break order attributably;
   forces replace inertia with defense; order is the privilege of a
   one-dimensional time.
6. **finale.md** — defended gaps die by snap, tip, or leak, announced by
   rising variance; frustration is cohomology and defense is resistance;
   and in the deepest description we have, the world is not a place where
   gaps happen to be fixed — it is the fixed gaps, being read.

The program as originally posed — formalize the observation that some
relations never change, and see how far it goes — is complete. What remains
is no longer this theory's to settle: whether causal-set recovery of
geometry can be made quantitative is working physics; whether entanglement
structure admits a gap-theoretic reading is quantum information; whether
frustration numbers of real social networks predict where their conflicts
concentrate is empirical sociology. The mathematics has carried the
observation to the borders of three sciences, which is where an essay's idea
should hope to end up.
