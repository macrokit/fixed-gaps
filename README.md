# fixed-gaps

**[fixed-gaps.pdf](fixed-gaps.pdf)** — the complete monograph (46 pages,
typeset), assembling all documents below with a preface. Rebuild with
`pandoc` + `tectonic` from the markdown sources.

**[paper/paper.pdf](paper/paper.pdf)** — a standalone, submission-ready
paper (7 pages): *Rating Gaps and Effective Resistance: Exact Fluctuation
Laws for Elo and Bradley–Terry Systems* — the three laws, proofs,
simulations, and the Arena validations, with related work and
bibliography. LaTeX source in [paper/](paper/).

An essay and a mathematical theory about **fixed gaps**: relations between
two entities — people or objects — that are frozen the moment they become
defined and never change afterward. Age differences, blood relations, causal
order, potential differences.

- **[essay.md](essay.md)** — the prose argument: the gap is fixed but its
  meaning is not; fixed relations remove negotiation; in physics only the
  gaps are measurable; relativity revises the inventory of fixed gaps without
  refuting the idea; structuralism as the payoff.
- **[theory.md](theory.md)** — the formalization, in three pillars:
  1. *Gap structures* (torsors): absolute values exist only up to gauge;
     gaps are fixed **iff** everything drifts together (rigidity theorem);
     the gap table determines the world up to translation (structuralism as
     a theorem); fixed additive gaps fade in ratio while fixed multiplicative
     gaps diverge in absolute terms.
  2. *Gaps as group invariants* (Klein view): which gaps are fixed depends
     on the admitted transformation group; relativity = enlarging the group.
  3. *Append-only worlds*: kinship and causal order are fixed because the
     past only accumulates — the stable facts are exactly the positive
     existential ones.
- **[readings.md](readings.md)** — resolution of the open conjecture on
  classifying "readings" (interpretations of a frozen gap): the conjectured
  trichotomy is false — there is a fourth, *recurrent* signature
  (anniversaries) — but the amended four-way classification is a theorem.
  Highlights: the *hyperbolic fading law* (the felt size of a fixed gap
  decays exactly like $d/t$, and felt gaps compress but never reorder), and
  the *phase gap* (anniversary structure is itself a fixed gap, valued in a
  circle group — ritual as the phenomenology of quotient torsors).
- **[frontier.md](frontier.md)** — resolutions of the next three open
  problems: recurrence is relative to a one-parameter group (calendar vs
  "doubling" anniversaries; $\sin(\log t)$ as counterexample); noise leaves
  gaps fixed in expectation but buries felt order past a horizon quadratic
  in the gap difference, collapses the frozen readings to affine ones, and
  makes the present forget the past at rate $\sqrt{t}$ — rituals keep gaps
  *felt*, records keep them *known*; and the invariant tower gap → ratio →
  cross-ratio is one sharp-transitivity construction that provably
  terminates (Tits), leaving **birth order** as the invariant that survives
  both maximal symmetry and maximal noise.
- **[forces.md](forces.md)** — the last three problems: heavy-tailed noise
  makes order strictly less durable (horizon $(\Delta d)^\alpha$, no safe
  period, inversions by single attributable shocks — erosion vs betrayal as
  tail regimes); interacting drifts replace inertia with **defense**
  (Lyapunov rigidity: fixed gaps as energy minima; defended gaps fluctuate
  but never dissolve — maintenance joins ritual and records); and in higher
  dimensions the ladder runs gap vector → angle → cross-ratio and stops
  (Liouville), while at maximal symmetry the survivors are the components
  of configuration space — so **order is the privilege of a
  one-dimensional time**: on a plane, no invariant survives at all.
- **[finale.md](finale.md)** — the close of the arc: defended gaps die in
  three ways (snap, tip, leak), all announced by rising variance — critical
  slowing down as a general early-warning theorem; gap networks reveal that
  frustration is cohomology (the original theory is the frustration-free
  case) and that a gap's noise-fluctuation equals effective resistance —
  hierarchies defended only locally drift apart, and archives are the
  long-range edges that hold networks rigid; and the Lorentzian ladder runs
  interval → twin-ratio → CFT cross-ratio, with Zeeman's theorem showing
  that **causal order alone generates the geometry**. Causal set theory
  supplies the ending: the world does not *have* a gap structure — it *is*
  one, and spacetime is its reading.

- **[application.md](application.md)** — the worked application, answering
  an external review's request for a "killer application": rating systems
  (chess Elo, LLM leaderboards) as defended gap networks. Three laws
  derived and verified in simulation ([simulations/](simulations/)):
  estimation error of any rating gap = effective resistance in the match
  graph — verified in simulation (slope ≈ 1.0, R² up to 0.99) **and on
  real Chatbot Arena data**: 39,241 battles, 60 models, all 1,770 pairs,
  zero-parameter fit with slope 1.035 and R² 0.958; stationary Elo churn with static
  skills is **graph-independent** (the isotropy surprise — noise and
  defense enter through the same edges); and tracking error under skill
  drift follows a *grounded* resistance law (verified to 3% on the path
  graph). Corollaries: chess's era problem as a theorem, resistance-based
  leaderboard confidence intervals, and a matchmaking design rule.
- **[review-response.md](review-response.md)** — an external review of the
  monograph (summarized) and the response, including what the review got
  right, where its correctness assessment fell short, and how
  application.md answers its main criticism.

Central slogan: **what persists between things are relations, not
conditions; what we experience as change is the drift of non-invariant
readings over an invariant substrate.**

Licensed under [CC BY 4.0](LICENSE).
