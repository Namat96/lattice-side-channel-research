# Lattice Side-Channel Research

This repository contains my 14-week research project on lattice-based cryptography and side-channel security.

The main focus of the project is to understand how side-channel leakage can give useful information about secret values in lattice-based cryptographic systems. I also studied LWE, lattice mathematics, Ring-LWE, Module-LWE, ML-KEM, and ML-DSA.

The project was developed mainly using Python. Most of the experiments are small and educational examples that helped me understand the concepts step by step.

## Project Goals

The main goals of this project were:

- Understand the basic ideas of lattice-based cryptography.
- Study the Learning With Errors (LWE) problem.
- Understand different types of side-channel leakage.
- Experiment with Hamming-weight and timing leakage.
- Study simple LWE secret recovery using approximate information.
- Learn basic lattice reduction and LLL.
- Understand Ring-LWE and Module-LWE.
- Study the structure of ML-KEM and ML-DSA.
- Look at performance and implementation security.
- Review possible security problems and countermeasures.

## Weekly Work

### Week 1 — Research Foundation
Introduced lattice-based cryptography, LWE, side-channel attacks, and the basic research questions of the project.

### Week 2 — Leakage Models
Studied simple leakage models such as Hamming weight and approximate information.

### Week 3 — Side-Channel Basics
Learned the basic ideas behind timing, power, and other side-channel attacks.

### Week 4 — LWE Secret Recovery
Created small LWE examples and tested simple secret recovery using limited information about the error.

### Week 5 — Leakage Correlation
Used simple experiments to study the relationship between secret-dependent values and simulated leakage.

### Week 6 — Lattice Cryptography Fundamentals
Studied lattice bases, matrices, SVP, CVP, Gram-Schmidt, and the connection between LWE and lattices.

### Week 7 — Lattice Reduction and LLL
Studied lattice basis reduction and created small examples to understand the basic idea of the LLL algorithm.

### Week 8 — Ring-LWE and Module-LWE
Studied polynomial rings and the basic structure of Ring-LWE and Module-LWE.

### Week 9 — Kyber / ML-KEM
Studied the main structure of Kyber and the standardized ML-KEM key encapsulation mechanism.

### Week 10 — ML-DSA / Dilithium
Studied the main ideas behind ML-DSA and its connection with the CRYSTALS-Dilithium design.

### Week 11 — Side-Channel PQC Analysis
Studied simple timing and leakage examples related to lattice-based operations.

### Week 12 — PQC Performance Analysis
Looked at basic performance and implementation considerations for post-quantum cryptography.

### Week 13 — PQC Security Review
Reviewed possible attack surfaces, security threats, and basic mitigation ideas.

### Week 14 — Final Project Review
Collected the main findings, limitations, and future research directions of the project.

## Tools Used

- Python
- NumPy
- VS Code
- Git
- GitHub

## Important Note

The experiments in this repository are mainly for learning and research practice. They use small parameters and simplified examples.

They are **not** intended to be attacks against real ML-KEM, ML-DSA, or other production cryptographic systems.

The ML-KEM and ML-DSA examples are also simplified demonstrations of their structure and should not be used for real cryptographic applications.

## Main Things I Learned

During this project, I learned that cryptographic security has more than one side.

The mathematical problem can be difficult to solve, but the implementation can still leak information through timing, power consumption, memory behavior, or other physical effects.

I also learned how LWE connects with lattices and how modern post-quantum schemes use structured versions of these ideas.

The experiments helped me understand these topics better than studying the theory alone.

## Limitations

This project has some limitations:

- The experiments use small toy parameters.
- The timing experiments are affected by the normal computer environment.
- No real power or electromagnetic measurements were collected.
- The project does not attack a real cryptographic implementation.
- The ML-KEM and ML-DSA examples are simplified.
- More advanced statistical and hardware experiments would be needed for deeper research.

## Future Work

In the future, I would like to study:

- Real side-channel traces.
- More advanced leakage models.
- Statistical analysis of noisy traces.
- Constant-time implementations.
- Side-channel countermeasures.
- NTT implementations used in lattice cryptography.
- Hardware-based experiments.
- More advanced attacks and defenses for post-quantum cryptography.

## Author

**Namat Ullah**

BS Mathematics Student

This project was developed as part of my learning and research work in post-quantum cryptography, lattice-based cryptography, and side-channel security.
