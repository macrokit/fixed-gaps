"""The era problem, measured: merge two Arena collections from disjoint
periods (55k: 2023 - early 2024; 100k: Jun-Aug 2024) whose model sets
overlap in only a few "bridge" models. The merged battle graph is the
clustered regime where application.md predicts the folk heuristic
(per-model battle counts) fails while the resistance law stays calibrated,
and where cross-era uncertainty is set by the bridge.

Usage: python3 arena_era.py battles.json battles100k.json
"""

import json
import sys
from collections import Counter

import numpy as np

rng = np.random.default_rng(7)
MIN_BATTLES = 200
BOOT = 200


def bt_mle(n, ei, ej, wins, tot, iters=100):
    r = np.zeros(n)
    for _ in range(iters):
        p = 1 / (1 + np.exp(-(r[ei] - r[ej])))
        g = np.zeros(n)
        np.add.at(g, ei, wins - tot * p)
        np.add.at(g, ej, -(wins - tot * p))
        w = tot * p * (1 - p)
        L = np.zeros((n, n))
        np.add.at(L, (ei, ei), w)
        np.add.at(L, (ej, ej), w)
        np.add.at(L, (ei, ej), -w)
        np.add.at(L, (ej, ei), -w)
        step = np.linalg.pinv(L) @ g
        r += step
        r -= r.mean()
        if np.abs(step).max() < 1e-10:
            break
    return r, L


def gapvar(M):
    d = np.diag(M)
    return d[:, None] + d[None, :] - 2 * M


def main(p1, p2):
    b1 = [(a, b, w) for a, b, w, *_ in json.load(open(p1)) if w in "ab"]
    b2 = [(a, b, w) for a, b, w, *_ in json.load(open(p2)) if w in "ab"]
    m1 = {m for x in b1 for m in x[:2]}
    m2 = {m for x in b2 for m in x[:2]}
    battles = b1 + b2
    cnt = Counter()
    for a, b, _ in battles:
        cnt[a] += 1
        cnt[b] += 1
    keep = {m for m, c in cnt.items() if c >= MIN_BATTLES}
    battles = [(a, b, w) for a, b, w in battles if a in keep and b in keep]
    models = sorted(keep)
    idx = {m: k for k, m in enumerate(models)}
    n = len(models)
    era = np.array([(m in m1) + 2 * (m in m2) for m in models])  # 1, 2, 3=bridge
    print(f"merged decisive battles: {len(battles)}   models: {n} "
          f"(era-1 only {sum(era==1)}, era-2 only {sum(era==2)}, "
          f"bridge {sum(era==3)})")

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
    tot = np.array([agg[e][0] for e in edges], float)
    wins = np.array([agg[e][1] for e in edges], float)

    _, LF = bt_mle(n, ei, ej, wins, tot)
    var_pred = gapvar(np.linalg.pinv(LF))

    # bootstrap
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
    var_boot = gapvar(np.cov(boots.T))

    iu = np.triu_indices(n, 1)
    x, y = var_pred[iu], var_boot[iu]
    slope = np.dot(x, y) / np.dot(x, x)
    r2 = 1 - ((y - slope * x) ** 2).mean() / y.var()
    print(f"\nglobal resistance law on the merged (clustered) graph: "
          f"slope = {slope:.3f}   corr = {np.corrcoef(x,y)[0,1]:.3f}   "
          f"R2 = {r2:.3f}")

    # groups: within-era vs cross-era (exclusive models only)
    gi, gj = era[iu[0]], era[iu[1]]
    within = ((gi == gj) & (gi != 3))
    cross = ((gi == 1) & (gj == 2)) | ((gi == 2) & (gj == 1))
    n_per = np.zeros(n)
    np.add.at(n_per, ei, tot)
    np.add.at(n_per, ej, tot)
    naive = (1 / n_per[iu[0]] + 1 / n_per[iu[1]])
    c = np.dot(naive[within], y[within]) / np.dot(naive[within], naive[within])
    print(f"\ncalibrate naive count predictor on within-era pairs "
          f"(c = {c:.2f}); median ratio boot/prediction:")
    for name, pred in [("resistance", x), ("naive counts", c * naive)]:
        for tag, sel in [("within-era", within), ("cross-era", cross)]:
            ratio = np.median(y[sel] / pred[sel])
            print(f"  {name:12s} {tag:11s} {ratio:6.2f}")
    print(f"  median boot sd: within-era {np.sqrt(np.median(y[within])):.3f}, "
          f"cross-era {np.sqrt(np.median(y[cross])):.3f} "
          f"(median min-battles: within {np.median(np.minimum(n_per[iu[0]],n_per[iu[1]])[within]):.0f}, "
          f"cross {np.median(np.minimum(n_per[iu[0]],n_per[iu[1]])[cross]):.0f})")

    # bridge dependence: delete one bridge model's battles -> cross-era R_eff
    print("\nbridge dependence (Fisher resistance, median over cross-era pairs):")
    base = np.median(x[cross])
    print(f"  full graph: {base:.4f}")
    for bm in [models[k] for k in range(n) if era[k] == 3]:
        k = idx[bm]
        mask = (ei != k) & (ej != k)
        _, L2 = bt_mle(n, ei[mask], ej[mask], wins[mask], tot[mask])
        # drop the now-isolated node for pinv stability
        keep2 = np.ones(n, bool)
        keep2[k] = False
        R2m = gapvar(np.linalg.pinv(L2[np.ix_(keep2, keep2)]))
        era2 = era[keep2]
        i2 = np.triu_indices(n - 1, 1)
        g2i, g2j = era2[i2[0]], era2[i2[1]]
        c2 = ((g2i == 1) & (g2j == 2)) | ((g2i == 2) & (g2j == 1))
        print(f"  without {bm:28s}: {np.median(R2m[i2][c2]):.4f}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
