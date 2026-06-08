# Lattice Fundamentals Summary

In Week 6 I worked with small lattice examples.

## Lattice basis

A few basis vectors can generate many lattice points by taking integer
combinations of the basis vectors.

## SVP and CVP

SVP looks for a short non-zero vector in a lattice.

CVP starts with a target point and looks for a lattice point close to it.

The scripts use brute-force searches because the examples are very small.

## Gram-Schmidt

Gram-Schmidt changes a set of linearly independent vectors into an
orthogonal set. This is an important mathematical tool in lattice reduction.

## LWE connection

The LWE equation from Week 4 can be related to lattice problems. This is one
of the reasons lattices are important in post-quantum cryptography.

These experiments are only for understanding the mathematics and do not
implement a practical lattice reduction attack.
