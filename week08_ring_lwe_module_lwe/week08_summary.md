# Week 8 Summary

In Week 8 I studied Ring-LWE and Module-LWE as structured forms of LWE.

## Ring-LWE

Ring-LWE works with polynomial elements instead of ordinary vectors. This
allows polynomial arithmetic to represent the LWE relation.

The small experiment uses coefficient lists to represent polynomials.

## Module-LWE

Module-LWE uses vectors of ring elements. It keeps more structure than
ordinary LWE while being less structured than the single-ring setting.

## Why this matters

Structured LWE problems are important in practical post-quantum cryptography.
They can make implementations more efficient while keeping a lattice-based
security foundation.

## What I learned

The main difference is the algebraic structure used for the secret, public
values and operations.

The scripts in this week are only small educational examples. They do not
implement a standardized cryptographic scheme.
