# Week 2 - Leakage Models

This week I looked at simple leakage models for lattice-based cryptography.

The main idea is that an attacker may not see the secret directly. Instead, some
information related to the secret can leak. In this week I used small examples
to understand how Hamming weight, noisy values, and approximate hints can give
partial information about a secret.

These are small experiments for learning. They are not attacks on a real
cryptographic implementation.

## Files

- `hamming_weight.py` - calculates Hamming weight of small vectors
- `noisy_leakage.py` - adds simple noise to secret-related values
- `approximate_hint.py` - shows how an approximate hint can reveal partial information
- `leakage_summary.md` - short notes from the experiments

## Goal

The goal is to understand what leakage can look like before studying more
advanced lattice side-channel attacks.
