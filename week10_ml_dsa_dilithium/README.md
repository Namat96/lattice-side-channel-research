# Week 10 - ML-DSA and Dilithium

This week I studied ML-DSA, the NIST standardized lattice-based digital
signature scheme that was developed from CRYSTALS-Dilithium.

The focus is on understanding the structure of lattice-based signatures,
polynomial operations, signing and verification, and the role of noise and
challenge values.

## Files

- `signature_structure.py` - simplified signing and verification flow
- `polynomial_operations.py` - small polynomial arithmetic examples
- `challenge_demo.py` - demonstrates a small challenge value
- `noise_effect.py` - shows how small noise changes a value
- `verification_demo.py` - simple educational verification example
- `week10_summary.md` - notes from the study

## Main idea

ML-DSA is a lattice-based digital signature standard. It is based on the
Module-LWE and related lattice assumptions and uses structured polynomial
operations.

A real ML-DSA implementation contains carefully specified sampling,
polynomial transforms, hints, packing, rejection sampling, and cryptographic
hash functions.

The examples in this week are simplified learning experiments. They are not
an implementation of the ML-DSA standard and should not be used to create
real signatures.
