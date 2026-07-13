Ancillary files for "Rating Gaps and Effective Resistance:
Exact Fluctuation Laws for Elo and Bradley-Terry Systems"

ratings_sim.py     - simulations verifying Theorems 1-3 and Prop. 4
                     (P1 estimation law, P2 isotropy, P3 grounded
                     tracking, P4 saturation). Pure numpy. ~1 min.
results.txt        - committed output of ratings_sim.py (Section 4).

arena_analysis.py  - dense-regime validation of Theorem 1 on the public
                     lmarena-ai/arena-human-preference-55k dataset
                     (Section 5.1). Input: battles.json, a list of
                     (model_a, model_b, winner) triples extracted from
                     the dataset's train.csv.
results_arena.txt  - committed output (slope 1.035, R^2 0.958).

arena_era.py       - clustered/two-era validation merging the 55k and
                     100k Arena datasets (Section 5.2). Inputs: the two
                     battle-triple JSON files.
results_era.txt    - committed output (slope 1.041; calibration split;
                     bridge analysis).

Full build pipeline, data-extraction snippets, and the companion
monograph: https://github.com/macrokit/fixed-gaps
