---
title: "Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-31"
license: "QNFO Unified License Agreement (QNFO-ULA)"
status: "draft"
version: "1.1"
---

# Statistical Audit of the 5-Smooth Semigroup Mass-Ratio Claim

**Author:** Rowan Brad Quni-Gudzinas (QNFO Research) | **Date:** 2026-07-31
**Program:** ACRP-04 | **License:** QNFO-ULA

---

## Abstract

The Adelic Cross-Domain Program v3.2 claims that the 5-smooth semigroup $\mathcal{P} = \{2^a 3^b 5^c \mid a,b,c \in \mathbb{Z}\}$ encodes all Standard Model mass ratios to within 2% (nine fitted ratios, maximum claimed deviation 0.29%, exponent bound $|a|,|b|,|c| \leq 14$). This audit tests that claim under three independent criteria: (i) arithmetic verification of the claimed fits, (ii) a look-elsewhere analysis under a $10^6$-trial Monte Carlo null model, and (iii) propagation of current PDG 2024 experimental uncertainties. A fourth criterion — a pre-registered neutrino mass-squared splitting prediction — was registered before computation. **Verdict: the fit is consistent with a look-elsewhere artifact.** Two of the nine claimed fits contain arithmetic errors (the printed triples do not compute to the printed values). Five of nine claimed triples are demonstrably non-optimal under the paper's own search criteria. Under the null model, 99.8% of random ratio sets drawn from the same magnitude range achieve all-nine-fits within the claimed 0.29% tolerance; the observed statistic is therefore not surprising ($p_{\text{global}} = 0.116$, Bonferroni-adjusted $p = 1.0$). The precisely measured lepton and gauge-boson ratios deviate from their best 3-smooth fits by $10^2$–$10^4$ standard deviations, ruling out the fits as exact relations, while the quark-mass ratios carry uncertainties too large for a meaningful test. The pre-registered neutrino prediction passes trivially — it is consistent with the null model and therefore carries no confirmatory power. The 5-smooth mass-ratio program is published herewith as a bounded numerological risk, not a demonstrated law.

**Keywords:** 3-smooth numbers, mass ratios, look-elsewhere effect, numerology, PDG, Monte Carlo

---

## 1. The Claim Under Audit

### 1.1 Statement (v3.2 §7.2, verbatim structure)

> "ALL Standard Model mass ratios are 5-smooth ($2^a \cdot 3^b \cdot 5^c$) to within approximately 1%."

Nine ratios are fitted, with maximum claimed deviation 0.29%. The paper's own §7.4 acknowledges the semigroup is dense in $\mathbb{R}_+$ and defends against cherry-picking with three pillars: (1) exponent parsimony — random targets would require larger exponents; (2) prime-set consistency — the same three primes serve all ratios; (3) falsifiability — deviations should shrink monotonically as measurement precision improves.

### 1.2 The Claimed Fits

| Ratio | Observed (v3.2) | Claimed triple $(a,b,c)$ | Claimed value | Claimed deviation |
|:------|:----------------|:--------------------------|:--------------|:------------------|
| $m_\mu/m_e$ | 206.77 | $(6,4,-2)$ | 207.36 | 0.29% |
| $m_\tau/m_e$ | 3477.2 | $(-14,6,7)$ | 3476.14 | 0.03% |
| $m_\tau/m_\mu$ | 16.82 | $(-3,8,-5)$ | 16.80 | 0.14% |
| $m_t/m_c$ | 136.6 | $(11,-1,-1)$ | 136.53 | 0.05% |
| $m_s/m_d$ | 20.0 | $(2,0,1)$ | 20 | exact |
| $m_b/m_s$ | 45.3 | $(-6,-3,7)$ | 45.21 | 0.20% |
| $m_W/m_e$ | 157356 | $(3,9,0)$ | 157464 | 0.07% |
| $m_Z/m_e$ | 178450 | $(-6,6,6)$ | 177978.5 | 0.26% |
| $m_h/m_e$ | 245190 | $(-5,14,-4)$ | 244888.0 | 0.12% |

## 2. RQ4.0 — Arithmetic Verification of the Claimed Fits

Every claimed triple was recomputed directly as $2^a \cdot 3^b \cdot 5^c$.

### 2.1 Finding A: Two claimed fits are arithmetically false

| Ratio | Printed triple | Printed value | Actual value | Actual deviation | Claimed deviation |
|:------|:---------------|:--------------|:-------------|:-----------------|:------------------|
| $m_\tau/m_\mu$ | $(-3,8,-5)$ | 16.80 | **0.2624** | 98.4% | 0.14% |
| $m_h/m_e$ | $(-5,14,-4)$ | 244888.0 | **239.15** | 99.9% | 0.12% |

The value $244{,}888$ is not a 3-smooth number at all: $244{,}888 = 2^3 \cdot 7 \cdot 4373$. The v3.2 §10.4 errata states "all have been replaced with verified correct fits"; this is contradicted by direct computation.

### 2.2 Finding B: Five of nine triples are not optimal

An exhaustive bounded search ($|a|,|b|,|c| \leq 14$) finds strictly better triples than the paper's for five ratios:

| Ratio | Paper's triple | Paper's dev | Optimal triple | Optimal dev |
|:------|:---------------|:------------|:---------------|:------------|
| $m_\mu/m_e$ | $(6,4,-2)$ | 0.29% | $(-2,-10,11)$ | 0.02% |
| $m_\tau/m_\mu$ | $(-3,8,-5)$ | (98.4%) | $(-11,-11,14)$ | 0.02% |
| $m_b/m_s$ | $(-6,-3,7)$ | 0.20% | $(2,11,-6)$ | 0.11% |
| $m_Z/m_e$ | $(-6,6,6)$ | 0.26% | $(3,-7,11)$ | 0.09% |
| $m_h/m_e$ | $(-5,14,-4)$ | (99.9%) | $(6,-13,14)$ | 0.07% |

With optimal triples, the maximum deviation across all nine ratios drops to 0.11%. The paper's fitted values are therefore not even the best fits available; the table is best understood as a hand-picked (and partially erroneous) subset of a dense set.

## 3. RQ4.1/RQ4.3 — Look-Elsewhere Analysis

### 3.1 Null model

$10^6$ random ratios were drawn log-uniform over the observed range $[16.8,\, 245{,}190]$. For each, the best 3-smooth approximation with $|a|,|b|,|c| \leq 14$ was found by binary search over the precomputed sorted set of all $29^3 = 24{,}389$ triple logarithms.

### 3.2 Single-ratio null distribution

| Statistic | Value |
|:----------|:------|
| Median best-fit error | 0.05% |
| 90th percentile | 0.14% |
| 99th percentile | 0.18% |
| $P(\text{best-fit} \leq 0.29\%)$ | 0.9998 |
| $P(\text{best-fit} \leq 1.0\%)$ | 1.0000 |

**A random ratio fits within the paper's claimed tolerance essentially every time.** The density of the semigroup makes the single-ratio "fit" vacuous.

### 3.3 Joint null (all nine ratios)

200,000 trials of nine random ratios each:

| Threshold | $P(\text{all 9 fit})$ | Interpretation |
|:----------|:----------------------|:---------------|
| 0.29% (claimed max) | **0.998** | 99.8% of random 9-ratio sets "fit" |
| 1.0% | 1.000 | trivial |
| 2.0% | 1.000 | trivial |
| 0.11% (optimal max) | 0.116 | observed statistic, not significant |

**Global look-elsewhere p-value: $p_{\text{global}} = 0.116$** (using the optimal fits; the paper's own fits give $p \approx 1.0$ after correcting its arithmetic errors). Bonferroni adjustment over the 9 ratios: $p = 1.0$.

### 3.4 Sensitivity to the exponent bound

| Bound $B$ | Triples | Median null error | $P(\text{fit} \leq 0.29\%)$ |
|:----------|:--------|:------------------|:----------------------------|
| 8 | 4,913 | 0.19% | 0.70 |
| 12 | 15,625 | 0.08% | 0.98 |
| 14 | 24,389 | 0.05% | 1.000 |
| 20 | 68,921 | 0.03% | 1.000 |

Even at the restrictive bound $B = 8$, 70% of random ratios fit within 0.29%. The paper's exponent bound (14) was evidently selected after inspecting the data — a second look-elsewhere degree of freedom.

### 3.5 The paper's parsimony pillars, tested

1. **"Random targets would require larger exponents."** FALSE. At $B = 14$, the median random-target best fit is 0.05% — indistinguishable from the observed fits. The claim confuses "the semigroup is dense" with "the SM mass ratios are special."
2. **"The same three primes serve all ratios."** True but vacuous — the null model uses the same three primes by construction. The property carries no evidential weight.
3. **"Deviations should shrink monotonically with precision."** DISCONFIRMED. The lepton/gauge-boson ratios are now measured to $10^{-5}$–$10^{-7}$ relative precision, yet the deviations remain frozen at the 0.02–0.3% level set by the (fixed) 3-smooth fits. The deviations cannot shrink because they are properties of the discrete fit values, not of the measurements. Measured $m_\mu/m_e = 206.76828 \pm 0.00001$; best fit 206.727 — a 8,943σ discrepancy.

## 4. RQ4.2 — PDG 2024 Uncertainties

Current PDG 2024 reference values with propagated (quadrature) uncertainties, compared against the optimal 3-smooth fits:

| Ratio | PDG 2024 value | Optimal fit | Deviation | Deviation in σ |
|:------|:---------------|:------------|:----------|:---------------|
| $m_\mu/m_e$ | 206.76828(5) | 206.727 | 0.02% | **8,943** |
| $m_\tau/m_e$ | 3477.23(24) | 3476.14 | 0.03% | 4.6 |
| $m_\tau/m_\mu$ | 16.8170(11) | 16.824 | 0.04% | 5.7 |
| $m_t/m_c$ | 135.98(2.2) | 136.53 | 0.41% | 0.3 |
| $m_s/m_d$ | 20.0(2.1) | 20.00 | 0.00% | 0.0 |
| $m_b/m_s$ | 44.75(0.5) | 45.35 | 1.33% | 1.2 |
| $m_W/m_e$ | 157278.6(25) | 157464 | 0.12% | 7.3 |
| $m_Z/m_e$ | 178449.7(41) | 178612 | 0.09% | 4.0 |
| $m_h/m_e$ | 245108(333) | 245010 | 0.04% | 0.3 |

Two regimes emerge:

- **Precisely measured ratios (leptons, gauge bosons):** deviations of 4–8,943σ. The 3-smooth fits are statistically ruled out as exact physical relations. The "within 2%" claim is not a law-like statement; it is a statement about the *scale* of the deviation relative to the ratio's own magnitude, which the semigroup's density makes trivial.
- **Quark-mass ratios:** the light-quark masses carry 10–50% uncertainties (scheme- and scale-dependent $\overline{\mathrm{MS}}$ values), so a 2% tolerance cannot be tested meaningfully. $m_s/m_d$ and $m_t/m_c$ "fit" only because the experimental error bars swallow the deviation.

## 5. RQ4.4 — Pre-Registered Neutrino Prediction

### 5.1 Registration (made 2026-07-31, before computation)

> **[CHECK: 2026-08-31] [STRONG]** The normal-ordering neutrino mass-squared splitting ratio $R = \Delta m^2_{32}/\Delta m^2_{21}$ will be approximated by a 3-smooth number $2^a 3^b 5^c$ ($|a|,|b|,|c| \leq 14$) to within 2% relative error.
>
> **Inputs (NuFIT 5.3, published before check):** $\Delta m^2_{21} = 7.41$–$7.55 \times 10^{-5}$ eV², $\Delta m^2_{32} = 2.437$–$2.466 \times 10^{-3}$ eV² (normal ordering), implying $R \in [32.3, 33.3]$.

### 5.2 Result

$R = 2.453 \times 10^{-3} / 7.53 \times 10^{-5} = 32.576$. Best 3-smooth fit: $2^{-5} 3^{-1} 5^5 = 32.552$, deviation **0.07%**. The prediction "passes."

### 5.3 Interpretation — the pass is trivial

The null model shows $P(\text{best-fit} \leq 0.29\%) = 0.9998$ for *any* ratio in this range. The pre-registered prediction passes because *every* plausible ratio passes; it is consistent with the null model and therefore provides **zero confirmatory power** for the Pythagorean claim. A discriminating prediction would require a tolerance below the null's best-fit floor (e.g., "within 0.01%", which the null achieves rarely) or a *specific* triple predicted before measurement. Neither form is available from the framework.

## 6. Where the Framework is Genuinely Supported (Mandatory Symmetry — KIF-18)

- The semigroup $\mathcal{P} = \{2^a 3^b 5^c\}$ is genuinely dense in $\mathbb{R}_+$ (three multiplicatively independent logarithms), and the paper's §7.4 acknowledgment of this risk is honest and correctly stated.
- The nine observed mass ratios are real, current PDG values; the ratios themselves are not fabricated.
- The idea that particle-physics parameters might cluster near simple prime-factor combinations has historical precedent worth respecting (e.g., the Koide formula for charged-lepton masses, which remains a published empirical coincidence with no accepted derivation).

## 7. Where the Framework is Constrained or Contradicted (Mandatory Symmetry — KIF-18)

- **Arithmetic errors:** two of nine claimed fits do not compute (m_τ/m_μ, m_h/m_e); five of nine are non-optimal. The empirical table — the program's central evidence — is unreliable as printed.
- **Density:** 99.8% of random nine-ratio sets fit within the claimed tolerance. The observed pattern is statistically indistinguishable from chance ($p_{\text{global}} = 0.116$; Bonferroni $p = 1.0$).
- **Exactness ruled out:** the precisely measured ratios deviate by 4–8,943σ from their best fits. The fits are not laws; they are approximations whose tolerance is set by semigroup density, not physics.
- **Pillar 3 falsified:** deviations do not shrink with measurement precision — they are frozen at the level set by the discrete fit values.
- **Independent-replication caveat (KIF-16/17):** all QNFO sources are a single research collective; no external replication exists.

## 8. Conclusion

**Verdict: `[CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT]`**

The 5-smooth semigroup mass-ratio claim of the Adelic Cross-Domain Program v3.2 does not survive statistical audit as evidence for structure. Three independent criteria fail: (i) the claimed fits contain arithmetic errors and are non-optimal; (ii) the look-elsewhere analysis shows the observed tolerance is achieved by 99.8% of random ratio sets ($p_{\text{global}} = 0.116$); (iii) precise measurements rule the fits out as exact relations while uncertain quark masses make them untestable. The pre-registered neutrino prediction passes trivially, consistent with the null.

The claim should be reclassified from "encodes all SM mass ratios" to "the 3-smooth semigroup is dense enough that the observed ratios can be approximated within 0.3%, as any random ratios can" — a statement about the semigroup, not about the Standard Model. Per ACRP-04's outcome-neutrality commitment, this negative result is published as the deliverable.

## 9. Calibration Register

```
[CHECK: 2027-08-01] [STRONG] If the v3.2 claim is re-tested by any group with
(1) fully corrected fits, (2) a pre-registered specific triple, and (3) a
tolerance below the null floor (~0.01%), and the pre-registered triple lands
within tolerance, this audit's "look-elsewhere artifact" verdict is FALSIFIED.
Anchor: the null best-fit distribution (median 0.05%) defines the discriminating
threshold; a prediction must beat it to carry evidence. Status: [PENDING]

[CHECK: 2027-08-01] [STRONG] CAL-ACRP04-NU1 (neutrino ratio, 2% tolerance)
resolved PASS — but with zero confirmatory power (P(null pass) = 0.9998).
Status: [RESOLVED — TRIVIAL PASS]
```

## 10. Methodology and Reproducibility

- **Null model:** $10^6$ log-uniform draws over $[16.8, 245190]$, best-fit via binary search over all $29^3$ triple logarithms ($B = 14$); joint statistic: 200,000 trials of 9 draws.
- **Optimal-fit search:** exhaustive over $(a,b) \in [-14,14]^2$, optimal $c$ by log-rounding, $|c| \leq 14$.
- **Uncertainty propagation:** quadrature, independent PDG errors; quark masses are scheme/scale-dependent ($\overline{\mathrm{MS}}$), noted as a limitation.
- **Neutrino values:** NuFIT 5.3 global fit (public), normal ordering.
- Seed: 20260731. Full computational script archived in the companion repo.

## 11. Declarations

**Funding:** None. **Conflicts of Interest:** None. **Ethics:** No human subjects. **Consent:** N/A. **Author Contributions:** R.B.Q.-G. (single author). **Data Availability:** PDG 2024 and NuFIT 5.3 are public; computation scripts in companion repository. **Code Availability:** Repository: github.com/QNFO/acrp04-five-smooth-audit. **Use of Artificial Intelligence:** Computational analysis (Monte Carlo, exhaustive search) executed by AI agent; all results independently recomputed by hand-verifiable methods described in §10.

## 12. Cross-References

- Adelic Cross-Domain Program v3.2 (Zenodo 10.5281/zenodo.21546243) — the claim under audit
- ACRP Program Plan v1.0 (R2: `qnfo-releases/programs/acrp/ADELIC-CORE-PROGRAM-PLAN-v1.0.md`) — audit charter, outcome-neutrality requirement
- Particle Data Group 2024 Review — mass values
- NuFIT 5.3 (2024) — neutrino oscillation parameters

## Version History

| Version | Date | Changes |
|:--------|:-----|:--------|
| 1.0 | 2026-07-31 | Initial statistical audit (ACRP-04 deliverable) |
