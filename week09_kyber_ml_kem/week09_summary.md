# Week 9 Summary

This week I studied the basic structure of Kyber and ML-KEM.

## Kyber and ML-KEM

Kyber is the lattice-based scheme that was selected by NIST and standardized
as ML-KEM.

ML-KEM is based on Module-LWE and uses polynomial arithmetic over a finite
modulus.

## Main components

I looked at:

- parameter sets
- polynomial operations
- the role of the NTT
- key generation
- encapsulation
- decapsulation
- noise, rounding and compression

## What I learned

The practical design of ML-KEM combines the mathematical ideas from earlier
weeks with efficient polynomial and matrix operations.

The scripts in this week are simplified learning examples. They do not
implement the NIST ML-KEM standard and should not be used for cryptographic
applications.
