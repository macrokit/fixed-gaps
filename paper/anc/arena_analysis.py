"""Real-data test of P1 (application.md): on Chatbot Arena battles, the
bootstrap variance of any Bradley-Terry rating gap should equal the
effective resistance between the two models in the battle graph, with
conductances c_e = n_e p_e (1 - p_e) (the Fisher information).

Data: lmarena-ai/arena-human-preference-55k (public, ungated), train.csv,
reduced to (model_a, model_b, winner) triples; decisive battles only.

Usage: python3 arena_analysis.py /path/to/battles.json
"""

import json
import sys

import numpy as np

rng = np.random.default_rng(7)
MIN_BATTLES = 200  # per-model decisive-battle floor
BOOT = 200


def bt_mle(n_models, ei, ej, wins, tot, iters=100):
    """Newton MLE for Bradley-Terry on aggregated edges, mean-zero gauge."""
    r = np.zeros(n_models)
    for _ in range(iters):
        d = r[ei] - r[ej]
        p = 1 / (1 + np.exp(-d))
        g = np.zeros(n_models)
        np.add.at(g, ei, wins - tot * p)
        np.add.at(g, ej, -(wins - tot * p))
        w = tot * p * (1 - p)
        L = np.zeros((n_models, n_models))
        np.add.at(L, (ei, ei), w)
        np.add.at(L, (ej, ej), w)
        np.add.at(L, (ei, ej), -w)
        np.add.at(L, (ej, ei), -w)
        step = np.linalg.pinv(L) @ g
        r += step
        r -= r.mean()
        if np.abs(step).max() < 1e-10:
            return r, L
    return r, L


def main(path):
    battles = json.load(open(path))
    battles = [(a, b, w) for a, b, w in battles if w in ("a", "b")]

    # filter to models with enough decisive battles
    from collections import Counter
    cnt = Counter()
    for a, b, _ in battles:
        cnt[a] += 1
        cnt[b] += 1
    keep = {m for m, c in cnt.items() if c >= MIN_BATTLES}
    battles = [(a, b, w) for a, b, w in battles if a in keep and b in keep]
    models = sorted(keep)
    idx = {m: k for k, m in enumerate(models)}
    n = len(models)
    print(f"decisive battles: {len(battles)}   models kept (>= {MIN_BATTLES}): {n}")

    # aggregate to edges (unordered pairs)
    agg = {}
    for a, b, w in battles:
        i, j = idx[a], idx[b]
        if i > j:
            i, j, w = j, i, ("a" if w == "b" else "b")
        t, ww = agg.get((i, j), (0, 0))
        agg[(i, j)] = (t + 1, ww + (w == "a"))
    edges = sorted(agg)
    ei = np.array([e[0] for e in edges])
    ej = np.array([e[1] for e in edges])
    tot = np.array([agg[e][0] for e in edges], dtype=float)
    wins = np.array([agg[e][1] for e in edges], dtype=float)
    print(f"battle-graph edges: {len(edges)} of {n*(n-1)//2} possible "
          f"(density {2*len(edges)/(n*(n-1)):.2f})")

    # full-data MLE and Fisher prediction
    r_hat, L_fisher = bt_mle(n, ei, ej, wins, tot)
    Lp = np.linalg.pinv(L_fisher)
    dg = np.diag(Lp)
    var_pred = dg[:, None] + dg[None, :] - 2 * Lp  # = R_eff in Fisher graph

    # bootstrap over battles
    bi = np.array([min(idx[a], idx[b]) for a, b, _ in battles])
    bj = np.array([max(idx[a], idx[b]) for a, b, _ in battles])
    bw = np.array([1.0 if ((w == "a") == (idx[a] < idx[b])) else 0.0
                   for a, b, w in battles])
    eid = {e: k for k, e in enumerate(edges)}
    beid = np.array([eid[(i, j)] for i, j in zip(bi, bj)])
    m_batt = len(battles)
    boots = np.empty((BOOT, n))
    for t in range(BOOT):
        take = rng.integers(m_batt, size=m_batt)
        tt = np.bincount(beid[take], minlength=len(edges)).astype(float)
        ww = np.bincount(beid[take], weights=bw[take], minlength=len(edges))
        live = tt > 0
        boots[t], _ = bt_mle(n, ei[live], ej[live], ww[live], tt[live])
    V = np.cov(boots.T, bias=False)
    dv = np.diag(V)
    var_boot = dv[:, None] + dv[None, :] - 2 * V

    # regression over all pairs
    iu = np.triu_indices(n, 1)
    x, y = var_pred[iu], var_boot[iu]
    slope = np.dot(x, y) / np.dot(x, x)
    r2 = 1 - ((y - slope * x) ** 2).mean() / y.var()
    corr = np.corrcoef(x, y)[0, 1]
    print(f"\nP1 on real data: bootstrap Var(gap) vs Fisher resistance, "
          f"{len(x)} pairs")
    print(f"  slope = {slope:.3f} (theory 1.0)   corr = {corr:.3f}   "
          f"R2(through origin) = {r2:.3f}")

    # comparison: does resistance beat the naive battle-count predictor?
    n_per = np.zeros(n)
    np.add.at(n_per, ei, tot)
    np.add.at(n_per, ej, tot)
    naive = 1 / n_per[:, None] + 1 / n_per[None, :]
    for name, pred in [("resistance", x), ("naive 1/n_i + 1/n_j", naive[iu])]:
        c = np.corrcoef(np.log(pred), np.log(y))[0, 1]
        print(f"  log-log corr with bootstrap variance: {name:22s} {c:.3f}")

    # decoupling exhibit: high-count high-resistance pair vs low-count low-R
    counts_pair = np.minimum(n_per[iu[0]], n_per[iu[1]])
    hi = np.argmax(x * (counts_pair > np.median(counts_pair)))
    lo = np.argmin(x + 1e9 * (counts_pair > np.median(counts_pair)))
    for tag, k in [("well-fought yet uncertain", hi), ("lightly-fought yet certain", lo)]:
        i, j = iu[0][k], iu[1][k]
        print(f"  {tag}: {models[i]} vs {models[j]}  "
              f"min battles = {counts_pair[k]:.0f}, "
              f"pred sd = {np.sqrt(x[k]):.3f}, boot sd = {np.sqrt(y[k]):.3f}")


if __name__ == "__main__":
    main(sys.argv[1])
