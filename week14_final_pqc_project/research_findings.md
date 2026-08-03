# Research Findings

## LWE and leakage

The project showed how approximate information about an LWE computation can make secret recovery easier in a small toy setting. Noise affects how directly the secret can be inferred.

## Correlation

Hamming-weight style leakage can have a strong correlation with an underlying secret-dependent value in controlled experiments. Adding noise reduces the quality of the observed relationship.

## Lattices

Lattice bases, SVP, CVP, Gram-Schmidt, and LLL provided the mathematical background for understanding lattice-based cryptography.

## Modern PQC

Ring-LWE and Module-LWE extend the basic LWE setting using structured polynomial and module representations. ML-KEM and ML-DSA demonstrate how lattice-based ideas are used in standardized post-quantum cryptography.

## Implementation security

Mathematical security does not automatically prevent implementation leakage. Timing, power, electromagnetic effects, memory behavior, and faults are implementation-level concerns.

## Performance

Naive polynomial arithmetic becomes more expensive as the polynomial size increases. Practical PQC implementations therefore use optimized arithmetic rather than the simple educational multiplication used in this project.
