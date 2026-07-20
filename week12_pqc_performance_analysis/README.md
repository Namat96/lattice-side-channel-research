# Week 12 — PQC Performance and Implementation Analysis

This week studies basic performance measurements for lattice-based cryptography operations.

The purpose is to understand how operation count, polynomial size, and repeated arithmetic can affect runtime. The experiments are small educational models and are not implementations of ML-KEM or ML-DSA.

## Objectives

- Measure simple polynomial arithmetic costs.
- Compare repeated multiplication with a precomputed approach.
- Study how polynomial size affects runtime.
- Connect performance measurements with practical PQC implementation work.
- Record observations for the final project report.

## Files

- `polynomial_performance.py` — measures simple polynomial multiplication for different sizes.
- `operation_count.py` — counts arithmetic operations in toy polynomial multiplication.
- `precompute_comparison.py` — compares repeated calculation with precomputed values.
- `size_scaling.py` — observes runtime as polynomial size changes.
- `week12_summary.md` — research observations.

These experiments are educational and are not security benchmarks of production cryptographic libraries.
