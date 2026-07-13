# Week 11 — Side-Channel Analysis of Lattice Operations

This week connects the earlier lattice and PQC work with practical side-channel analysis.

The goal is to study how simple implementation choices can create measurable leakage. The experiments use toy arithmetic rather than real ML-KEM or ML-DSA implementations.

## Objectives

- Understand why secret-dependent operations can leak information.
- Compare a branch-based operation with a fixed-operation version.
- Measure simple timing differences over repeated executions.
- Study Hamming-weight leakage in polynomial-style coefficient operations.
- Relate these observations to lattice-based cryptography.

## Files

- `timing_branch_experiment.py` — toy timing experiment with secret-dependent branching.
- `fixed_operation_demo.py` — fixed-operation alternative for comparison.
- `hamming_weight_polynomial.py` — coefficient leakage experiment.
- `leakage_comparison.py` — compares simple leakage measurements.
- `week11_summary.md` — observations and research notes.

These are educational experiments and are not implementations of ML-KEM, ML-DSA, or a real attack.
