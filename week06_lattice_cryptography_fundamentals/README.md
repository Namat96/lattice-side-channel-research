# Week 6 - Lattice Cryptography Fundamentals

This week I started working with the basic mathematical ideas behind lattice
based cryptography.

The aim is to understand how lattices can be represented using basis vectors
and matrices, and how problems such as SVP and CVP are related to lattice
cryptography.

## Files

- `lattice_basics.py` - creates a small lattice from basis vectors
- `lattice_matrix.py` - represents a lattice basis as a matrix
- `svp_basics.py` - checks short vectors in a small lattice
- `cvp_basics.py` - demonstrates a simple closest-vector search
- `lwe_lattice_connection.py` - shows a small connection between LWE and lattices
- `gram_schmidt.py` - performs Gram-Schmidt orthogonalization

## Main ideas

A lattice can be generated from integer combinations of basis vectors.

Two important lattice problems are:

- SVP (Shortest Vector Problem)
- CVP (Closest Vector Problem)

LWE can also be connected to lattice problems. In practical cryptography,
these problems are used with much larger dimensions and carefully chosen
parameters.

The examples in this week are small mathematical experiments for learning.
They are not implementations of a complete lattice attack.
