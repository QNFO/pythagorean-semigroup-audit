# ERRATA — ACRP-04 v1.3

**Date:** 2026-08-02
**DOI:** 10.5281/zenodo.21748008

## Correction 1: Sigma Value

### Original (v1.2)
The headline muon-electron sigma was reported as **9,138σ**.

### Correction
Independent recomputation under the research v2.42 numeracy gates (BP-7: Sigma/Error Propagation Audit, BP-10: Independent Recompute) found that the 9,138σ figure does not reproduce. The best reconstruction using PDG 2024 Live values and the paper's own cited uncertainties yields **8,943σ**.

### Changes Applied
| Location | Old | New |
|:---------|:----|:----|
| Results table (m_μ/m_e row) | **9,138** | **8,943** |
| RQ4.1 prose (§3) | 9,138σ discrepancy | 8,943σ discrepancy |
| Two-regime analysis (§4) | 4–9,138σ | 4–8,943σ |
| RQ4.4 conclusion (§7) | 4–9,138σ | 4–8,943σ |

### Impact
The qualitative conclusion — that the 3-smooth fits are statistically ruled out as exact physical relations — is **unchanged**. 8,943σ still decisively rejects the null hypothesis. The correction only fixes an unreproducible arithmetic error in the specific sigma value.

### Audit Trace
- BP-7 Sigma Traceability Audit: research v2.42, 2026-08-02
- BP-10 Independent Recompute: PDG 2024 Live, m_μ/m_e = 206.76828 ± 0.00001
- Session: DL50vO3ksO6NNUa8afJ8_ (parent-agent audit)
