# ERRATA — ACRP-04 v1.3

**Date:** 2026-08-02
**DOI:** 10.5281/zenodo.21754151

## Correction 1: Terminology (v1.2, BP-2)

| Instance | Location | Original | Corrected |
|:---------|:---------|:---------|:----------|
| 1 | YAML title | "Pythagorean Semigroup" | "5-Smooth Semigroup" |
| 2 | H1 heading | "Pythagorean Semigroup" | "5-Smooth Semigroup" |
| 3-14 | Body text (12 occurrences) | "Pythagorean semigroup" | "5-smooth semigroup" |

**Root Cause (BP-2):** The set {2^a * 3^b * 5^c} consists of 5-smooth (Hamming/regular) numbers. "Pythagorean numbers" satisfy a^2 + b^2 = c^2 — a different property. The tag was a terminological misnomer with no impact on mathematical content.

## Correction 2: Headline Sigma (v1.3, BP-7/BP-10)

### Original (v1.2)
The headline muon-electron sigma was reported as **9,138sigma**.

### Correction
Independent recomputation under research v2.42 numeracy gates (BP-7: Sigma/Error Propagation Audit, BP-10: Independent Recompute) found the 9,138sigma figure unreproducible. Best reconstruction using PDG 2024 Live values and the paper's own cited uncertainties yields **8,943sigma**.

### Changes Applied
| Location | Old | New |
|:---------|:----|:----|
| Results table (m_mu/m_e row) | **9,138** | **8,943** |
| RQ4.1 prose (sec3) | 9,138sigma discrepancy | 8,943sigma discrepancy |
| Two-regime analysis (sec4) | 4-9,138sigma | 4-8,943sigma |
| RQ4.4 conclusion (sec7) | 4-9,138sigma | 4-8,943sigma |

### Impact
Qualitative conclusion unchanged. 8,943sigma still decisively rejects the null hypothesis.

### Audit Trace
- BP-7 Sigma Traceability Audit: research v2.42, 2026-08-02
- BP-10 Independent Recompute: PDG 2024 Live, m_mu/m_e = 206.76828 +/- 0.00001
- Session: DL50vO3ksO6NNUa8afJ8_ (parent-agent audit)
