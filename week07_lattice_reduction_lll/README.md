# Week 7 - Lattice Reduction and LLL

This week I worked on the basic idea of lattice reduction and the LLL
algorithm.

The goal is to understand why a lattice basis can be changed into a more
useful basis containing shorter and more nearly orthogonal vectors.

## Files

- `gram_schmidt_lattice.py` - Gram-Schmidt values used during reduction
- `size_reduction.py` - simple size-reduction step
- `lll_toy.py` - small educational LLL-style reduction
- `basis_comparison.py` - compares the original and reduced basis
- `reduction_summary.md` - notes from the experiments

## Main idea

LLL (Lenstra-Lenstra-Lovasz) is a polynomial-time lattice reduction algorithm.
It does not solve SVP exactly in general, but it can produce a much better
basis for many lattice problems.

This week uses very small two-dimensional examples so the steps can be
followed directly.

The code is educational and is not intended to reproduce a production
cryptographic implementation.
