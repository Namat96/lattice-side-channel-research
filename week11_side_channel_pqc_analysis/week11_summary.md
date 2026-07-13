# Week 11 Summary

This week focused on the implementation side of lattice-based cryptography.

## Main observations

1. A secret-dependent branch can make the amount of executed work depend on secret data.
2. Repeated measurements can make small timing differences easier to observe, although the toy experiment is affected by normal system noise.
3. Replacing a branch with fixed-style arithmetic can reduce one obvious source of control-flow leakage.
4. Hamming weight gives a simple model for studying data-dependent leakage from coefficient values.
5. Real ML-KEM and ML-DSA implementations require much stronger constant-time and side-channel protections than these toy examples.

## Research connection

The earlier weeks studied LWE, lattices, LLL, Ring-LWE, Module-LWE, ML-KEM, and ML-DSA. Week 11 connects those mathematical topics to implementation security: a mathematically secure construction can still be vulnerable if an implementation leaks information about secret-dependent values.

## Limitation

These experiments are educational models. Timing measurements on a normal computer are not evidence of a practical attack against a real cryptographic implementation.
