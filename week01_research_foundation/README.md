# Week 01 - Research Foundation

This week starts the research part of the project.

The main topic is leakage-aware lattice cryptography. I will study how information from an implementation, such as execution timing, may reveal something about a secret. I will also study how approximate information can help with recovery of a sparse LWE secret.

## Main topics

- LWE basics
- Sparse ternary secrets
- Hamming weight
- Side-channel leakage
- Timing leakage
- Approximate hints
- Threat models
- Experimental research questions

## Goal

The goal is not to attack a real production cryptographic system. I will first build small experiments that are easy to understand and measure.

The later weeks will use these ideas for experiments on LWE secret recovery and implementation leakage.

## Files

- `research_questions.md` - questions that guide the experiments
- `threat_model.md` - attacker model and assumptions
- `lwe_background.md` - short background on LWE and sparse secrets

## Note

The experiments in this project are educational and research-oriented. Small parameters and simplified implementations will be used where needed.
