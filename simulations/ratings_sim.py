"""Numerical tests of the three predictions of application.md:

P1 (estimation): the variance of the Bradley-Terry MLE of a rating gap
    equals (4/m) * R_eff(i,j) in the match graph (m matches per edge).
P2 (isotropy): online Elo with STATIC skills has stationary gap variance
    = K for every pair, independent of graph structure (edge noise and
    edge defense cancel the resistance dependence).
P3 (tracking): when true skills drift idiosyncratically (node noise, std
    sigma_d per step, weakly mean-reverting so the system stays in Elo's
    linear regime), the stationary tracking-error variance of a gap is
    K + (2|E| sigma_d^2 / K) * R_eff(i,j).
    (With a PURE random walk, skill gaps grow without bound, saturate the
    logistic, and Elo's restoring signal collapses -- tracking error
    diverges on sparse graphs. Run sim_P3 with theta=0 to reproduce.)

Run: python3 ratings_sim.py            (~1 minute)
"""

import numpy as np

rng = np.random.default_rng(7)


def graph_edges(kind, n):
    if kind == "path":
        return [(i, i + 1) for i in range(n - 1)]
    if kind == "cycle":
        return [(i, (i + 1) % n) for i in range(n)]
    if kind == "complete":
        return [(i, j) for i in range(n) for j in range(i + 1, n)]
    if kind == "two-cluster":  # two cliques of n//2, two bridges
        h = n // 2
        e = [(i, j) for i in range(h) for j in range(i + 1, h)]
        e += [(h + i, h + j) for i in range(h) for j in range(i + 1, h)]
        e += [(0, h), (h - 1, n - 1)]
        return e
    if kind == "3-regular":  # random 3-regular via configuration retries
        while True:
            stubs = np.repeat(np.arange(n), 3)
            rng.shuffle(stubs)
            pairs = stubs.reshape(-1, 2)
            e = {tuple(sorted(p)) for p in pairs}
            if len(e) == 3 * n // 2 and not any(a == b for a, b in e):
                lap = laplacian(sorted(e), n)
                if np.linalg.matrix_rank(lap) == n - 1:  # connected
                    return sorted(e)


def laplacian(edges, n, w=None):
    L = np.zeros((n, n))
    for k, (i, j) in enumerate(edges):
        c = 1.0 if w is None else w[k]
        L[i, i] += c
        L[j, j] += c
        L[i, j] -= c
        L[j, i] -= c
    return L


def r_eff(edges, n):
    Lp = np.linalg.pinv(laplacian(edges, n))
    d = np.diag(Lp)
    return d[:, None] + d[None, :] - 2 * Lp


def bt_mle(edges, n, wins, m, iters=50):
    """Newton's method for Bradley-Terry MLE (logistic scale 1), mean-0 gauge."""
    r = np.zeros(n)
    E = np.array(edges)
    for _ in range(iters):
        d = r[E[:, 0]] - r[E[:, 1]]
        p = 1 / (1 + np.exp(-d))
        g = np.zeros(n)
        np.add.at(g, E[:, 0], wins - m * p)
        np.add.at(g, E[:, 1], -(wins - m * p))
        H = laplacian(edges, n, w=m * p * (1 - p))
        step = np.linalg.pinv(H) @ g
        r = r + step
        r -= r.mean()
        if np.abs(step).max() < 1e-10:
            break
    return r


def sim_P1(kind, n=16, m=40, trials=600):
    """MLE gap-error variance vs (4/m) R_eff, all pairs."""
    edges = graph_edges(kind, n)
    errs = np.empty((trials, n))
    for t in range(trials):
        wins = rng.binomial(m, 0.5, size=len(edges))
        errs[t] = bt_mle(edges, n, wins, m)
    V = np.cov(errs.T, bias=False)
    dV = np.diag(V)
    var_gap = dV[:, None] + dV[None, :] - 2 * V
    R = r_eff(edges, n)
    iu = np.triu_indices(n, 1)
    x, y = (4 / m) * R[iu], var_gap[iu]
    slope = np.dot(x, y) / np.dot(x, x)
    resid = y - slope * x
    r2 = 1 - resid.var() / y.var()
    return slope, r2


def elo_run(edges, n, K, steps, burn, thin, sigma_d=0.0, theta=0.0):
    """Online Elo; returns samples of r (sigma_d=0) or r - s (tracking)."""
    E = np.array(edges)
    ne = len(E)
    r = np.zeros(n)
    s = np.zeros(n)
    out = []
    for t in range(steps):
        if sigma_d > 0:
            s += -theta * s + rng.normal(0, sigma_d, n)
            s -= s.mean()
        k = rng.integers(ne)
        i, j = E[k]
        p_true = 1 / (1 + np.exp(-(s[i] - s[j])))
        w = rng.random() < p_true
        p_hat = 1 / (1 + np.exp(-(r[i] - r[j])))
        upd = K * (w - p_hat)
        r[i] += upd
        r[j] -= upd
        if t >= burn and t % thin == 0:
            e = r - s
            out.append(e - e.mean())
    return np.array(out)


def gap_var(samples, n):
    V = np.cov(samples.T, bias=False)
    d = np.diag(V)
    return d[:, None] + d[None, :] - 2 * V


def sim_P2(kind, n=12, K=0.1):
    edges = graph_edges(kind, n)
    samp = elo_run(edges, n, K, steps=4_000_000, burn=400_000, thin=200)
    vg = gap_var(samp, n)
    R = r_eff(edges, n)
    iu = np.triu_indices(n, 1)
    near = vg[iu][R[iu] <= np.median(R[iu])].mean()
    far = vg[iu][R[iu] > np.median(R[iu])].mean()
    return vg[iu].mean(), near, far  # theory: all = K


def sim_P3(kind, n=12, K=0.1, sigma_d=0.004, theta=1e-4):
    edges = graph_edges(kind, n)
    samp = elo_run(edges, n, K, steps=8_000_000, burn=800_000, thin=300,
                   sigma_d=sigma_d, theta=theta)
    vg = gap_var(samp, n)
    R = r_eff(edges, n)
    iu = np.triu_indices(n, 1)
    x, y = R[iu], vg[iu]
    A = np.vstack([np.ones_like(x), x]).T
    (icpt, slope), *_ = np.linalg.lstsq(A, y, rcond=None)
    r2 = 1 - ((y - A @ [icpt, slope]) ** 2).mean() / y.var()
    naive_slope = 2 * len(edges) * sigma_d**2 / K
    # exact linear theory: mean reversion grounds the network, so the node
    # noise sees the resistance of (L + (theta/a) I); regress the exact
    # prediction on plain R_eff to get the theory value of `slope`
    a = K / (4 * len(edges))
    M = np.linalg.inv(laplacian(edges, n) + (theta / a) * np.eye(n))
    d = np.diag(M)
    Rg = d[:, None] + d[None, :] - 2 * M
    yth = (sigma_d**2 / (2 * a)) * Rg[iu]
    (_, exact_slope), *_ = np.linalg.lstsq(A, yth, rcond=None)
    return icpt, slope, naive_slope, exact_slope, r2  # icpt = K expected


def sim_P3_design(n=12):
    """Marginal value of a bridge vs an intra-cluster edge (max-pair R_eff)."""
    base = graph_edges("two-cluster", n)
    R0 = r_eff(base, n).max()
    h = n // 2
    bridge = base + [(1, h + 1)]
    Rb = r_eff(bridge, n).max()
    # add an intra-cluster edge where none is free: clusters are cliques,
    # so double an existing intra edge (weight 2) instead
    w = np.ones(len(base))
    w[0] = 2.0
    Lp = np.linalg.pinv(laplacian(base, n, w))
    d = np.diag(Lp)
    Ri = (d[:, None] + d[None, :] - 2 * Lp).max()
    return R0, Rb, Ri


if __name__ == "__main__":
    print("P1: Var(MLE gap error) vs (4/m) R_eff  [theory: slope 1, R2 ~ 1]")
    for kind in ["path", "cycle", "two-cluster", "3-regular", "complete"]:
        slope, r2 = sim_P1(kind)
        print(f"  {kind:12s}  slope = {slope:.3f}   R2 = {r2:.3f}")

    print("\nP2: static skills, online Elo  [theory: Var(gap) = K = 0.1, flat in R_eff]")
    for kind in ["path", "two-cluster", "complete"]:
        mean, near, far = sim_P2(kind)
        print(f"  {kind:12s}  mean = {mean:.4f}   low-R_eff pairs = {near:.4f}"
              f"   high-R_eff pairs = {far:.4f}")

    print("\nP3: drifting skills  [theory: Var = K + slope * R_eff]")
    for kind in ["path", "two-cluster"]:
        icpt, slope, naive, exact, r2 = sim_P3(kind)
        print(f"  {kind:12s}  intercept = {icpt:.4f} (K = 0.1)"
              f"   slope = {slope:.5f}"
              f" (naive {naive:.5f}, exact grounded {exact:.5f})   R2 = {r2:.3f}")

    R0, Rb, Ri = sim_P3_design()
    print(f"\nP3 design: worst-pair R_eff  base = {R0:.3f}"
          f"   +1 bridge = {Rb:.3f}   +1 intra = {Ri:.3f}")
