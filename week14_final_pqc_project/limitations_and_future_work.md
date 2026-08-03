# Limitations and Future Work

## Limitations

- The experiments use small toy parameters.
- The timing experiments run on a normal desktop and are affected by operating-system noise.
- The leakage models are simplified.
- The LWE recovery experiments are not attacks against real cryptographic systems.
- The ML-KEM and ML-DSA examples are structural demonstrations, not implementations of the standards.
- No physical power or electromagnetic measurements were collected.
- No real hardware fault-injection experiments were performed.

## Future work

Possible future research could include:

1. Implementing controlled leakage experiments with larger datasets.
2. Studying real constant-time cryptographic libraries in a safe research environment.
3. Comparing different leakage models.
4. Applying statistical techniques to noisy traces.
5. Studying side-channel countermeasures for lattice-based implementations.
6. Exploring NTT implementations and their side-channel behavior.
7. Testing experiments on dedicated hardware instead of only a desktop computer.
8. Studying recent post-quantum implementation-security research.
