"""
ACRP-04 — Pythagorean Semigroup Mass-Ratio Statistical Audit
RQ4.0: Verify the 9 claimed fits from Cross-Domain v3.2 §7.2
RQ4.1: Monte Carlo null model (10^6 trials)
RQ4.3: Look-elsewhere-corrected p-values

Claim (v3.2 §7.2): P = {2^a·3^b·5^c | a,b,c in Z} encodes all 9 SM mass ratios
to within 1% (max deviation 0.29%), with |a|,|b|,|c| <= 14.
"""
import numpy as np
from itertools import product

# ============================================================
# §0. THE CLAIMED FITS (from v3.2 §7.2 table)
# ============================================================
CLAIMS = [
    # (name, observed, a, b, c, claimed_deviation)
    ("m_mu/m_e",   206.77,    6,  4, -2, 0.29),
    ("m_tau/m_e",  3477.2,  -14,  6,  7, 0.03),
    ("m_tau/m_mu",  16.82,   -3,  8, -5, 0.14),
    ("m_t/m_c",    136.6,    11, -1, -1, 0.05),
    ("m_s/m_d",     20.0,     2,  0,  1, 0.00),
    ("m_b/m_s",     45.3,    -6, -3,  7, 0.20),
    ("m_W/m_e", 157356.0,     3,  9,  0, 0.07),
    ("m_Z/m_e", 178450.0,    -6,  6,  6, 0.26),
    ("m_h/m_e", 245190.0,    -5, 14, -4, 0.12),
]

B = 14  # exponent bound

def smooth_val(a, b, c):
    return (2.0**a) * (3.0**b) * (5.0**c)

def rel_err(x, fit):
    return abs(x - fit) / x * 100.0

print("=" * 80)
print("RQ4.0: VERIFY THE 9 CLAIMED FITS (v3.2 §7.2)")
print("=" * 80)
print(f"{'Ratio':<14}{'Observed':>12}{'Fit(a,b,c)':>16}{'ClaimedVal':>14}{'ActualVal':>14}{'ClaimDev%':>10}{'ActualDev%':>11}  VERDICT")
print("-" * 100)
errors_found = []
for name, obs, a, b, c, claim_dev in CLAIMS:
    val = smooth_val(a, b, c)
    dev = rel_err(obs, val)
    ok = "OK" if abs(dev - claim_dev) < 0.01 or (claim_dev == 0 and dev == 0) else "MISMATCH"
    # More precise check: does the claimed value match the triple?
    print(f"{name:<14}{obs:>12.2f}{f'({a},{b},{c})':>16}{smooth_val(a,b,c):>14.4f}{'--':>14}{claim_dev:>10.2f}{dev:>11.2f}  {ok}")
    if ok == "MISMATCH":
        errors_found.append(name)

print(f"\nClaimed-fit inconsistencies detected: {errors_found if errors_found else 'NONE'}")

# ============================================================
# §1. TRUE BEST-FIT TRIPLES (bounded search |a|,|b|,|c| <= 14)
# ============================================================
print("\n" + "=" * 80)
print("RQ4.0b: TRUE BEST-FIT TRIPLE FOR EACH OBSERVED RATIO")
print("=" * 80)
print("(The v3.2 table may not report the optimal triple for each ratio.)")
print(f"{'Ratio':<14}{'Observed':>12}{'Best(a,b,c)':>14}{'BestVal':>14}{'BestDev%':>10}")
print("-" * 70)

best_fits = {}
for name, obs, a0, b0, c0, claim_dev in CLAIMS:
    best = None
    for a in range(-B, B+1):
        for b in range(-B, B+1):
            # optimal c: round (ln(obs) - a ln2 - b ln3) / ln5
            c = round((np.log(obs) - a*np.log(2) - b*np.log(3)) / np.log(5))
            if abs(c) > B:
                continue
            val = smooth_val(a, b, c)
            d = rel_err(obs, val)
            if best is None or d < best[0]:
                best = (d, a, b, c, val)
    best_fits[name] = best
    print(f"{name:<14}{obs:>12.2f}{f'({best[1]},{best[2]},{best[3]})':>14}{best[4]:>14.4f}{best[0]:>10.2f}")

max_best = max(b[0] for b in best_fits.values())
print(f"\nMax best-fit deviation over all 9 ratios: {max_best:.2f}%")

# ============================================================
# §2. MONTE CARLO NULL MODEL (RQ4.1)
# ============================================================
print("\n" + "=" * 80)
print("RQ4.1: MONTE CARLO NULL MODEL — 10^6 random ratios")
print("=" * 80)
print("Null: mass ratios are random, log-uniform over the observed range")
print(f"[{min(obs for _,obs,_,_,_,_ in CLAIMS):.1f}, {max(obs for _,obs,_,_,_,_ in CLAIMS):.0f}]")
print("For each random ratio: best 3-smooth approximation with |a|,|b|,|c| <= 14")
print("-" * 70)

# Precompute all 3-smooth log-values in bound
rng = np.random.default_rng(20260731)
log_vals = []
for a in range(-B, B+1):
    for b in range(-B, B+1):
        for c in range(-B, B+1):
            log_vals.append(a*np.log(2) + b*np.log(3) + c*np.log(5))
log_vals = np.sort(np.array(log_vals))
N_TRIPLES = len(log_vals)
print(f"Exponent triples searched (trials space): {N_TRIPLES} (29^3)")

# Draw 10^6 random ratios log-uniform over observed range
lo, hi = min(obs for _,obs,_,_,_,_ in CLAIMS), max(obs for _,obs,_,_,_,_ in CLAIMS)
log_r = rng.uniform(np.log(lo), np.log(hi), 1_000_000)
r_vals = np.exp(log_r)

# Best 3-smooth fit via binary search on log-space
idx = np.searchsorted(log_vals, log_r)
idx = np.clip(idx, 0, N_TRIPLES-1)
best_log = log_vals[idx]
# Also check neighbor below
alt = np.maximum(idx-1, 0)
best_log2 = log_vals[alt]
d1 = np.abs(np.exp(best_log) - r_vals) / r_vals
d2 = np.abs(np.exp(best_log2) - r_vals) / r_vals
best_err = np.minimum(d1, d2)

# Distribution of best-fit errors
pct = np.percentile(best_err*100, [50, 75, 90, 95, 99])
print(f"\nNull distribution of best-fit relative error:")
print(f"  Median:    {pct[0]:.2f}%")
print(f"  P75:       {pct[1]:.2f}%")
print(f"  P90:       {pct[2]:.2f}%")
print(f"  P95:       {pct[3]:.2f}%")
print(f"  P99:       {pct[4]:.2f}%")

# Single-ratio p-values
for threshold in [0.29, 1.0, 2.0]:
    frac = np.mean(best_err*100 <= threshold)
    print(f"  P(best-fit error <= {threshold}%) = {frac:.6f}  (1 in {1/frac if frac>0 else float('inf'):.1f})")

# ============================================================
# §3. JOINT NULL — ALL 9 RATIOS (RQ4.3 look-elsewhere)
# ============================================================
print("\n" + "=" * 80)
print("RQ4.3: LOOK-ELSEWHERE — JOINT NULL (all 9 ratios simultaneously)")
print("=" * 80)
print("Draw 9 random ratios per trial; check if ALL 9 best-fits are within threshold.")
print(f"Observed max deviation: {max_best:.2f}% (claimed max: 0.29%)")
print("-" * 70)

N_JOINT = 200_000
log_r9 = rng.uniform(np.log(lo), np.log(hi), (N_JOINT, 9))
r9 = np.exp(log_r9)
idx9 = np.searchsorted(log_vals, log_r9)
idx9 = np.clip(idx9, 0, N_TRIPLES-1)
best_log9 = log_vals[idx9]
alt9 = np.maximum(idx9-1, 0)
best_log9b = log_vals[alt9]
d1_9 = np.abs(np.exp(best_log9) - r9) / r9
d2_9 = np.abs(np.exp(best_log9b) - r9) / r9
best_err9 = np.minimum(d1_9, d2_9) * 100

max_err9 = best_err9.max(axis=1)
for threshold in [0.29, 1.0, 2.0]:
    frac = np.mean(max_err9 <= threshold)
    print(f"  P(all 9 ratios fit within {threshold}%) = {frac:.6f}  (1 in {1/frac if frac>0 else float('inf'):.1f})")

# The observed statistic: max deviation across the 9 TRUE best-fits
obs_max = max_best
frac_obs = np.mean(max_err9 <= obs_max)
print(f"\n  Observed statistic (max true best-fit dev = {obs_max:.2f}%):")
print(f"  P(all 9 <= {obs_max:.2f}%) = {frac_obs:.6f} (1 in {1/frac_obs if frac_obs>0 else float('inf'):.1f})")
print(f"  -> Global look-elsewhere p-value for the joint fit: {frac_obs:.6f}")

# Bonferroni: per-ratio best p × 9
print(f"\n  Bonferroni (per-ratio worst-case): P_single({max_best:.2f}%) × 9 ratios")
frac_single = np.mean(best_err*100 <= max_best)
print(f"    P_single = {frac_single:.6f}  Bonferroni-adjusted = {min(1, frac_single*9):.6f}")

# ============================================================
# §4. EXPONENT-BOUND SENSITIVITY
# ============================================================
print("\n" + "=" * 80)
print("SENSITIVITY: how does the null depend on the exponent bound B?")
print("=" * 80)
for B2 in [8, 12, 14, 20, 30]:
    log_vals2 = []
    for a in range(-B2, B2+1):
        for b in range(-B2, B2+1):
            for c in range(-B2, B2+1):
                log_vals2.append(a*np.log(2) + b*np.log(3) + c*np.log(5))
    log_vals2 = np.sort(np.array(log_vals2))
    idx2 = np.searchsorted(log_vals2, log_r[:200000])
    idx2 = np.clip(idx2, 0, len(log_vals2)-1)
    bl = log_vals2[idx2]
    alt2 = np.maximum(idx2-1, 0)
    bl2 = log_vals2[alt2]
    e1 = np.abs(np.exp(bl) - r_vals[:200000]) / r_vals[:200000]
    e2 = np.abs(np.exp(bl2) - r_vals[:200000]) / r_vals[:200000]
    be = np.minimum(e1, e2)*100
    med = np.percentile(be, 50)
    p29 = np.mean(be <= 0.29)
    print(f"  B={B2:3d}: {len(log_vals2):7d} triples | median err {med:.2f}% | P(<=0.29%) = {p29:.6f}")

print("\n" + "=" * 80)
print("RQ4.1/4.3 PRELIMINARY COMPLETE — see next phase for PDG uncertainties")
print("=" * 80)
