# ERRATA — ACRP-04 Terminology Correction (v1.2)

**Date:** 2026-08-02
**Severity:** SOFT — terminology misnomer, no factual change

## Correction: Pythagorean → 5-smooth

| Instance | Location | Original | Corrected |
|:---------|:---------|:---------|:----------|
| 1 | YAML title | "Statistical Audit of the Pythagorean Semigroup..." | "Statistical Audit of the 5-Smooth Semigroup..." |
| 2 | H1 heading | "Statistical Audit of the Pythagorean Semigroup..." | "Statistical Audit of the 5-Smooth Semigroup..." |
| 3 | Abstract | "the Pythagorean semigroup $\mathcal{P}$" | "the 5-smooth semigroup $\mathcal{P}$" |
| 4 | Abstract | "The Pythagorean mass-ratio program" | "The 5-smooth mass-ratio program" |
| 5 | §1.1 Blockquote | "ALL Standard Model mass ratios are Pythagorean" | "ALL Standard Model mass ratios are 5-smooth" |
| 6 | §8 Conclusion | "The Pythagorean semigroup mass-ratio claim" | "The 5-smooth semigroup mass-ratio claim" |
| 7 | §11 Declarations | "github.com/QNFO/pythagorean-semigroup-audit" | "github.com/QNFO/acrp04-five-smooth-audit" |

## Rationale

Per BP-2 Terminology Audit Gate (research v2.39): "Pythagorean semigroup" for $\{2^a \cdot 3^b \cdot 5^c\}$ is a misnomer. The correct term is **5-smooth semigroup** (also known as Hamming numbers or regular numbers). Pythagorean numbers satisfy $a^2 + b^2 = c^2$ — every integer ≥ 3 is a leg of some Pythagorean triple, so "Pythagorean" is not a distinguishing property of the semigroup $\{2^a 3^b 5^c\}$.

The misnomer originated in the Adelic Cross-Domain Program v3.2 and propagated into this audit paper. The name alludes to the primes {2,3,5} forming the 3-4-5 Pythagorean triple, but this branding falsely implies number-theoretic significance for a density property.

## Impact

- No factual or numerical claims are altered
- No findings or conclusions change
- The correction is purely terminological
- The new version (v1.2) fully supersedes v1.1
- File renamed from `pythagorean-semigroup-audit.md` to `acrp04-five-smooth-audit.md`
- GitHub repo renamed to `QNFO/acrp04-five-smooth-audit`

**Cross-reference:** BP-2 (research v2.39), ACRP-01 (corresponding fix for cross-reference)
