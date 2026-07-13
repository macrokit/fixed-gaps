# The Worked Application: Rating Systems as Defended Gap Networks

*An external review of this monograph judged its main weakness to be the
absence of a "killer application" — a problem the framework explains or
predicts that is not naturally reached from existing viewpoints. This
chapter is the response: one domain worked end to end, from the framework's
concepts to falsifiable quantitative laws to numerical verification. The
simulation code is in [simulations/ratings_sim.py](simulations/ratings_sim.py);
all numbers below are from the committed runs
([simulations/results.txt](simulations/results.txt),
[simulations/results_arena.txt](simulations/results_arena.txt)).*

The domain is **pairwise-comparison rating systems** — chess Elo, sports
rankings, and LLM leaderboards such as Chatbot Arena — chosen because they
are, without any modeling license, the objects this theory is about: a
rating system is a defended gap network in the sense of finale.md §2, running
live on real data at scale.

The chapter's findings, in one paragraph: the framework's central
distinction — *where the noise enters* (nodes vs edges) versus *where the
defense acts* (edges) — cleanly splits rating systems into three regimes
with three different laws. Estimation error of a rating gap follows the
resistance law exactly (P1). The stationary churn of online Elo with static
skills is **graph-independent** — a surprise the framework forces you to
notice and the rating literature has little reason to ask about (P2). And
when true skills drift, the resistance law returns as the *tracking* error,
with a computable correction: mean reversion grounds the network (P3). Each
law is verified by simulation below — and P1 is additionally verified on
**real Chatbot Arena data** (39,241 battles, 60 models, 1,770 pairs) with a
zero-parameter fit: slope 1.035 against the theoretical 1.0, $R^2 = 0.958$
(§6). The third law also yields a matchmaking design rule and a derivation
of chess's era-comparison problem.

---

## 1. The mapping

The Bradley–Terry model: players $i$ have skills $s_i$, and $i$ beats $j$
with probability $\sigma(s_i - s_j)$ ($\sigma$ logistic). Every piece of the
monograph's apparatus lands on a native feature of this system:

| framework (chapter) | rating system |
|---|---|
| potentials, gauge freedom (theory.md 1.3) | ratings; only rating *differences* predict anything — the anchor and scale (Elo's "400 points", the initial 1500) are pure convention, which is why ratings are notoriously incomparable across pools |
| gap structure on the complete graph | the true skill differences $s_i - s_j$ |
| defended gaps, restoring force (forces.md §2) | matches: each game pulls the rating gap toward the observed outcome — Elo's update is stochastic gradient descent on the Bradley–Terry log-likelihood |
| the comparison network (finale.md §2) | the match graph: who has actually played whom, with edge weights = match counts |
| idiosyncratic node noise (frontier.md §2) | true skill drift: players improve and decline individually |
| edge noise | outcome randomness: a match is a coin flip biased by the gap |

The dynamics, linearized about small gaps (details in §2): with $n$ players,
match graph Laplacian $L$, matches arriving uniformly on $|E|$ edges, and
update factor $K$,

$$dr = a\,L\,(s - r)\,dt + \text{edge noise}, \qquad a = \frac{K}{4|E|},
\qquad \mathrm{Cov}(\text{edge noise}) = \frac{K^2}{4|E|}\,L .$$

The structural fact that drives everything: **the noise covariance and the
restoring force are built from the same Laplacian**, because in a rating
system every observation is also a defense — you cannot watch a gap without
tugging on it.

---

## 2. Three laws

**P1 (estimation: the resistance law).** With $m$ matches per edge and
static skills, the Fisher information of the Bradley–Terry model at equal
skills is $(m/4)L$, so the MLE of any rating gap — between *any* two
players, whether or not they ever met — has

$$\mathrm{Var}\big(\widehat{\,r_i - r_j\,}\big) \;=\; \frac{4}{m}\,
R_{\mathrm{eff}}(i,j),$$

the effective resistance in the match graph. The Fisher computation is
classical; the point is the identification: this is finale.md's
resistance law ($\mathrm{Var} = (\sigma^2/2) R_{\mathrm{eff}}$), reached
here through statistics rather than Langevin dynamics — the two derivations
are the same Laplacian inverse wearing different clothes. Uncertainty about
a gap is a property of the *network between* the pair, not of the pair.

**P2 (dynamics with static skills: the isotropy surprise).** Run online Elo
forever with static, equal skills. The stationary covariance solves the
Lyapunov equation $2aL\Sigma = \frac{K^2}{4|E|}L$, giving
$\Sigma = \frac{K}{2}P$ (P the centering projector), hence

$$\mathrm{Var}\big(r_i - r_j\big) \;=\; K \qquad \text{for every pair,
on every connected graph.}$$

The resistance dependence *cancels*: because noise and defense enter through
the same edges, poorly connected pairs get less restoring force but also
less noise, in exactly compensating amounts. Online Elo's stationary churn
is graph-independent — a path and a complete graph produce identical
long-run gap fluctuation. We are not aware of this being stated in the
rating literature; it is invisible unless one asks the framework's question
(*where does the noise enter relative to the defense?*), and it sharpens
frontier.md's noise dichotomy into a trichotomy: common noise (gaps exact),
node noise (resistance law), edge noise (isotropy).

**P3 (dynamics with drifting skills: the tracking resistance law).** Now
let true skills drift idiosyncratically — node noise of strength
$\sigma_d$, the frontier.md §2 regime. The tracking error $e = r - s$
receives isotropic node noise but only edge defense, and the mode-by-mode
stationary solution gives

$$\mathrm{Var}\big(e_i - e_j\big) \;=\; \underbrace{K}_{\text{edge part
(P2)}} \;+\; \underbrace{\frac{2|E|\,\sigma_d^2}{K}\,
R_{\mathrm{eff}}(i,j)}_{\text{node part: the resistance law}} .$$

Refinement: if the drift is weakly mean-reverting with rate $\theta$
(necessary for a stationary regime — see P4), the node noise is high-pass
filtered and the exact linear theory replaces $R_{\mathrm{eff}}$ by the
**grounded resistance** — the resistance of the network in which every node
additionally leaks to ground through conductance $\theta/a$, i.e. the
quadratic form of $(L + (\theta/a) I)^{-1}$. Mean reversion is literally a
grounding wire on every player.

**P4 (saturation: the era catastrophe).** If skills random-walk *without*
mean reversion, skill gaps grow without bound, the logistic saturates,
$\sigma'(s_i - s_j) \to 0$, and Elo's restoring signal collapses
exponentially: tracking error diverges on every graph. A bounded-update
rating system cannot follow unboundedly diverging skills at all — the
strongest form of the era problem.

---

## 3. Numerical verification

All from one committed run of `ratings_sim.py` ($n = 12$–$16$ players;
graphs: path, cycle, two clusters joined by two bridges, random 3-regular,
complete; $K = 0.1$):

**P1** — regress empirical MLE gap-error variance (600 trials, 40 matches
per edge) on $(4/m) R_{\mathrm{eff}}$, all pairs:

| graph | slope (theory 1) | $R^2$ |
|---|---|---|
| path | 1.006 | 0.992 |
| cycle | 1.024 | 0.964 |
| two-cluster | 1.020 | 0.994 |
| 3-regular | 1.027 | 0.927 |
| complete | 1.017 | — (all resistances equal; no variance to explain) |

**P2** — online Elo, static skills, 4M steps: mean stationary gap variance
0.1055–0.1060 against the predicted $K = 0.1$ (the few-percent excess is
the expected nonlinear correction), and *flat in resistance*: on the path,
the low-resistance half of pairs shows 0.1056 and the high-resistance half
0.1064 — adjacent and distant pairs churn identically, as predicted and
contrary to the naive guess.

**P3** — drifting skills ($\sigma_d = 0.004$, $\theta = 10^{-4}$, 8M
steps): gap tracking-error variance is linear in $R_{\mathrm{eff}}$
(path $R^2 = 0.95$, two-cluster $R^2 = 0.90$) with intercept 0.106 / 0.105
against the predicted $K = 0.1$. Measured slopes: path 0.00206 vs exact
grounded theory 0.00213 (3%; the naive ungrounded value 0.00352 is
clearly rejected), two-cluster 0.00964 vs 0.00812 (within 20%; the
grounded correction accounts for most of the gap to the naive 0.01024).

**P4** — with $\theta = 0$ the path-graph tracking variance explodes
(≈ 6.3 at the same parameters, sixty times the defended level, still
growing), confirming saturation escape.

**Design corollary** — in the two-cluster graph, adding *one* cross-cluster
match reduces the worst-pair resistance from 1.000 to 0.778; adding one more
within-cluster match reduces it to 0.995. Per match, the bridge is ~44×
more informative about the rankings that matter.

---

## 4. Predictions for real systems

1. **Chess's era problem is a theorem, not an accident.** The temporal
   comparison graph of chess is a chain: players of 1880 never played
   players of 1990, so the match graph across eras is path-like and
   $R_{\mathrm{eff}}$ grows linearly with era distance. By P3, cross-era
   rating gaps drift with variance linear in the separation — rating
   inflation and the impossibility of comparing Morphy with Carlsen are
   finale.md's Landau–Peierls chain instability, realized in data
   everyone already has. The known remedies map exactly to the theory's:
   anchoring to a fixed reference (an engine, a rule) is grounding;
   longitudinal careers spanning eras are long-range edges.
2. **Leaderboard confidence intervals should be resistance-based.** By P1,
   the uncertainty of "model A vs model B" on an arena-style leaderboard is
   $(4/m$-weighted$)$ effective resistance between them in the battle
   graph — not a function of how many battles each has fought. Two models
   each with thousands of battles but no common opponents can have an
   arbitrarily uncertain relative rank. This is testable against
   bootstrap CIs on public battle data: the framework predicts bootstrap
   variance of rating gaps is proportional to match-graph resistance.
3. **Resistance-optimal matchmaking.** The design corollary generalizes:
   to sharpen a leaderboard fastest, schedule the comparison that most
   reduces the (grounded) resistance of the pairs you care about — in
   practice, bridges between weakly connected clusters (new vs
   established models, different leagues, different eras) dominate
   yet another match between household names. Rating systems that
   matchmake for entertainment systematically overspend on low-resistance
   edges.
4. **A falsifiable oddity.** By P2, the long-run *churn* of a
   constant-$K$ Elo pool with stable skills should show gap fluctuation
   $\approx K$ (in logistic units) for all pairs, independent of the match
   graph — measurable in any stable online pool, and a direct test of the
   edge-noise isotropy that the framework predicts and intuition does not.

---

## 5. What is new here, honestly

The Bradley–Terry Fisher information and Elo-as-SGD are classical; effective
resistance as statistical leverage appears across network statistics. The
contributions specific to this chapter are: (i) the **noise-location
trichotomy** (common / node / edge) as the organizing question for rating
dynamics, and its consequence P2 — the graph-independence of stationary Elo
churn — which we have not found stated elsewhere; (ii) the **grounded
resistance law** P3 for tracking error under mean-reverting drift,
quantitatively verified; (iii) the identification of the era problem,
anchoring, and matchmaking design as instances of the monograph's chain
instability, grounding, and bridge theorems — the same mathematics that
governed crystals and kinship hierarchies in finale.md, now producing
numbers in a domain with abundant public data.

Limitations, plainly: P2–P4 are verified in simulation, not yet on live
rating pools; the derivations are linearizations (the few-percent excesses
in §3 are the visible nonlinear corrections). P1, however, has now been
tested on real data:

---

## 6. The empirical run: Chatbot Arena

Prediction 2 of §4 was tested against real leaderboard data: the public
Arena human-preference dataset (`lmarena-ai/arena-human-preference-55k`;
57,477 battles). Filtering to decisive battles and models with at least
200 of them leaves **39,241 battles among 60 models** over 1,145 distinct
model pairings (65% of possible pairs — a dense but far from complete
graph). Procedure ([simulations/arena_analysis.py](simulations/arena_analysis.py),
output in [simulations/results_arena.txt](simulations/results_arena.txt)):
fit Bradley–Terry ratings by maximum likelihood; compute the *predicted*
variance of every pairwise rating gap as the effective resistance in the
battle graph with Fisher conductances $c_e = n_e\, p_e (1 - p_e)$; compare
against the *empirical* variance from 200 bootstrap resamples of the
battles. The theory has **no free parameters**: the predicted regression
slope is exactly 1.

Result, over all $\binom{60}{2} = 1{,}770$ model pairs:

$$\text{slope} = 1.035 \quad (\text{theory } 1.0), \qquad
\text{corr} = 0.979, \qquad R^2_{\text{through origin}} = 0.958 .$$

The resistance law is not approximately right on Arena — it is
quantitatively right, at the few-percent level, across every pair of
models simultaneously, including the majority of pairs that never fought
each other directly.

Two honest observations. First, on this graph the naive predictor
$1/n_i + 1/n_j$ (per-model battle counts) also correlates well with the
bootstrap variance (log–log correlation 0.956, versus 0.987 for
resistance): Arena's battle graph is dense, and in dense graphs the
resistance *reduces to* approximately the naive formula — the framework
explains why the folk heuristic works there, and predicts exactly where it
fails: clustered or chain-like comparison graphs (new-model clusters,
cross-era chess, cross-league sport), where resistance and battle counts
decouple. That decoupled regime is where the design rule of §4.3 pays.
Second, the few-percent slope excess (1.035) has the expected sign:
bootstrap variance includes the mild extra dispersion that the Fisher
lower bound does not.

With this, the chapter's ledger stands: P1 verified on real data with a
zero-parameter fit; P2–P4 verified in controlled simulation; the remaining
open empirical item is catching P3's grounded-resistance drift in a
longitudinal rating pool (chess federation data across decades is the
natural target).
