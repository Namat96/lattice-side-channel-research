# Final Research Report

## Title

Side-Channel Leakage and Approximate-Hint LWE Secret Recovery in Lattice-Based Cryptography

## Abstract

This project explored selected mathematical and implementation-security aspects of lattice-based cryptography. It began with LWE and simple leakage models, then moved through secret recovery, correlation experiments, lattice mathematics, LLL reduction, Ring-LWE, Module-LWE, ML-KEM, and ML-DSA. The final weeks examined timing leakage, Hamming-weight leakage, performance, and implementation threats.

The experiments were intentionally small and educational. Their purpose was to understand concepts and relationships rather than to attack production cryptographic systems.

## Main conclusion

The project shows that studying a cryptographic construction requires both mathematical and implementation perspectives. Lattice-based constructions rely on difficult mathematical problems, while real implementations must also consider leakage, randomness, timing, memory behavior, faults, and performance.

## Method

The project used Python scripts and small controlled examples. Results were inspected through direct program output and simple comparisons.

## Key observations

- Approximate information can affect toy LWE secret recovery.
- Hamming-weight leakage can correlate with secret-dependent values.
- Noise reduces the clarity of leakage relationships.
- Lattice reduction provides important mathematical context for lattice cryptography.
- Ring-LWE and Module-LWE introduce structured algebraic representations.
- ML-KEM and ML-DSA illustrate modern standardized lattice-based cryptography.
- Implementation behavior can create security concerns even when the underlying mathematical construction is designed to resist known attacks.
- Naive polynomial arithmetic scales poorly compared with optimized approaches.

## Limitations

The project does not provide a practical attack against ML-KEM or ML-DSA. The experiments use simplified parameters and models and should not be interpreted as security evaluations of production software.

## Future direction

A natural continuation would be controlled side-channel experiments using real implementations, larger trace datasets, statistical analysis, and evaluation of countermeasures such as constant-time techniques and masking.

## Final note

This project was developed as a learning and research foundation for further study in post-quantum cryptography and implementation security.
