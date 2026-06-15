# Lattice Reduction Summary

In Week 7 I looked at how lattice reduction changes a basis into a more
useful form.

## Gram-Schmidt

Gram-Schmidt gives orthogonal vectors that can be used to study the geometry
of a lattice basis.

## Size reduction

A basis vector can be changed by subtracting an integer multiple of another
basis vector. This can make the vector shorter.

## LLL

LLL repeatedly uses size reduction and basis swaps according to a Lovasz-type
condition. The result is usually a shorter and more balanced basis.

The `lll_toy.py` script is a small educational implementation for two
dimensions. It is not a full optimized LLL library.

## Connection to cryptography

Lattice reduction is important in lattice-based cryptography and in the study
of attacks on lattice problems. Understanding the geometry of reduced bases
helps explain why algorithms such as LLL and stronger reduction methods are
useful.

These experiments use tiny parameters only for learning.
