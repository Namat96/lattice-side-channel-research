# Week 9 - Kyber and ML-KEM

This week I studied the basic structure of Kyber and its standardized form,
ML-KEM, as an example of practical lattice-based post-quantum cryptography.

The focus is on understanding the main building blocks rather than
implementing the complete standardized algorithm.

## Files

- `kyber_parameters.py` - records example parameter sets and basic dimensions
- `polynomial_ntt_demo.py` - small demonstration of polynomial transformation
- `ml_kem_structure.py` - shows the main stages of the ML-KEM structure
- `noise_and_rounding.py` - demonstrates small noise and rounding ideas
- `week09_summary.md` - notes from the study

## Main idea

Kyber was selected by NIST as the basis for the ML-KEM standard. ML-KEM is
based on Module-LWE and uses polynomial and matrix operations.

A practical implementation contains many details such as the NTT, sampling,
compression, encoding, and carefully selected parameters.

The examples in this week are small educational demonstrations. They are not
a complete or interoperable implementation of ML-KEM.
