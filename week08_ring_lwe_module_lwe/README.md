# Week 8 - Ring-LWE and Module-LWE

This week I looked at how the basic LWE idea can be extended using polynomial
rings and modules.

The aim is to understand the main structure of Ring-LWE and Module-LWE and
why these forms are useful for practical lattice-based cryptography.

## Files

- `polynomial_ring.py` - basic polynomial addition and multiplication modulo q
- `ring_lwe_sample.py` - creates a small toy Ring-LWE sample
- `module_lwe_sample.py` - creates a small Module-LWE style sample
- `ring_module_comparison.py` - compares the structures of LWE, Ring-LWE and Module-LWE
- `week08_summary.md` - notes from the experiments

## Main idea

LWE works with vectors over a finite modulus.

Ring-LWE replaces the vector operations with operations on polynomials in a
polynomial ring.

Module-LWE uses vectors of ring elements, giving a structure between
Ring-LWE and ordinary LWE.

These examples use very small parameters so the arithmetic can be followed
easily. They are educational experiments and are not complete cryptographic
implementations.
