"""Upload the paper to Zenodo.

Usage:
    export ZENODO_TOKEN=<your-personal-access-token>
    python3 zenodo_upload.py

Get a token at: https://zenodo.org/account/settings/applications
  -> Personal access tokens -> New token -> scopes: deposit:write, deposit:actions

The script creates a draft deposition, uploads paper.pdf and
arxiv-submission.tar.gz, sets metadata, and prints the draft URL.
It does NOT publish — you review and click Publish on Zenodo.
"""

import json
import os
import sys
import pathlib
import requests

TOKEN = os.environ.get("ZENODO_TOKEN", "")
if not TOKEN:
    sys.exit("Set ZENODO_TOKEN environment variable first.")

BASE = "https://zenodo.org/api"
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

ABSTRACT = (
    "A rating system is a network: players are nodes, matches are edges, and "
    "ratings are node potentials whose differences predict outcomes. We show "
    "that the fluctuation behavior of rating gaps is governed by a single "
    "question — where noise enters the network relative to where matches "
    "defend it — and that the answer splits rating systems into three regimes "
    "with three different laws. (i) Estimation: the variance of the "
    "maximum-likelihood estimate of any rating gap equals the effective "
    "resistance between the two players in the match graph, with Fisher "
    "conductances. (ii) Dynamics with static skills: the stationary gap "
    "fluctuation of online Elo is K (the update factor) for every pair on "
    "every connected graph — outcome noise and restoring force enter through "
    "the same edges and their graph dependence cancels exactly. "
    "(iii) Dynamics with drifting skills: idiosyncratic skill drift restores "
    "the resistance law as the tracking error, with mean reversion acting as "
    "a grounding conductance on every node. All three laws are verified in "
    "simulation; the estimation law is additionally confirmed on up to 104,419 "
    "real Chatbot Arena battles with a zero-parameter fit (slope 1.035–1.041 "
    "against the theoretical 1, R² ≥ 0.958), in both dense and clustered "
    "battle graphs. The clustered experiment — two collection eras joined by "
    "five bridge models — confirms the framework's distinctive prediction: the "
    "resistance law stays calibrated where the battle-count heuristic drifts "
    "by 17%, and quantifies how the comparability of 103 models across a year "
    "of LLM history rests on five survivors. Applications include "
    "resistance-based leaderboard confidence intervals, a matchmaking design "
    "rule, and a structural explanation of chess's era problem."
)

METADATA = {
    "metadata": {
        "upload_type": "publication",
        "publication_type": "preprint",
        "title": (
            "Rating Gaps and Effective Resistance: "
            "Exact Fluctuation Laws for Elo and Bradley–Terry Systems"
        ),
        "creators": [{"name": "Qian, Cheng"}],
        "description": ABSTRACT,
        "access_right": "open",
        "license": "cc-by-4.0",
        "keywords": [
            "Bradley-Terry model",
            "Elo rating",
            "effective resistance",
            "pairwise comparisons",
            "LLM evaluation",
            "Chatbot Arena",
            "gap structures",
            "network statistics",
        ],
        "notes": (
            "Simulation code and empirical data pipelines are available as "
            "ancillary files (arxiv-submission.tar.gz) and at "
            "https://github.com/macrokit/fixed-gaps"
        ),
        "related_identifiers": [
            {
                "identifier": "https://github.com/macrokit/fixed-gaps",
                "relation": "isSupplementedBy",
                "resource_type": "software",
                "scheme": "url",
            }
        ],
    }
}

HERE = pathlib.Path(__file__).parent

FILES = [
    HERE / "paper.pdf",
    HERE / "arxiv-submission.tar.gz",
]

# ── 1. Create deposition ──────────────────────────────────────────────────────
print("Creating deposition...")
r = requests.post(f"{BASE}/deposit/depositions", json={}, headers=HEADERS)
r.raise_for_status()
dep = r.json()
dep_id = dep["id"]
bucket_url = dep["links"]["bucket"]
print(f"  deposition id: {dep_id}")

# ── 2. Upload files ───────────────────────────────────────────────────────────
for path in FILES:
    if not path.exists():
        print(f"  WARNING: {path} not found — skipping")
        continue
    print(f"  uploading {path.name} ({path.stat().st_size // 1024} KB)...")
    with open(path, "rb") as fh:
        r = requests.put(
            f"{bucket_url}/{path.name}",
            data=fh,
            headers=HEADERS,
        )
        r.raise_for_status()
    print(f"    ok: {r.json().get('links', {}).get('self', '')}")

# ── 3. Set metadata ───────────────────────────────────────────────────────────
print("Setting metadata...")
r = requests.put(
    f"{BASE}/deposit/depositions/{dep_id}",
    json=METADATA,
    headers={**HEADERS, "Content-Type": "application/json"},
)
r.raise_for_status()

# ── 4. Print draft URL ────────────────────────────────────────────────────────
draft_url = r.json()["links"]["html"]
print(f"\nDraft ready for review:\n  {draft_url}\n")
print("Review, edit if needed, then click Publish on Zenodo.")
print("DO NOT run this script again — it creates a new deposition each time.")
