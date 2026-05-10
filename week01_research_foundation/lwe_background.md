# LWE Background

## Learning With Errors

Learning With Errors (LWE) is a central problem used in many lattice-based cryptographic constructions.

A basic LWE sample can be written as:

b = <a, s> + e mod q

where:

- `a` is a public random vector
- `s` is the secret vector
- `e` is a small error value
- `q` is the modulus
- `b` is the resulting LWE value

The error is important because it makes recovering the secret harder.

## Sparse ternary secrets

For the experiments in this project, a useful secret distribution is a small ternary secret:

s_i in {-1, 0, +1}

A secret can be sparse when most coefficients are zero.

Example:

```text
s = [0, 1, 0, -1, 0, 0, 1, 0]
```

The Hamming weight is the number of non-zero coefficients. In this example:

```text
Hamming weight = 3
```

Changing the Hamming weight will be one of the variables studied later.

## Why this matters

The mathematical structure of the secret can affect how much information is present in an experiment. Sparse secrets are useful for small educational experiments because the search space can be kept manageable.

## Approximate information

Later in the project, I will give the recovery experiment controlled approximate information. The purpose is to study how extra information can change the difficulty of recovering a sparse secret.

This is a simplified research experiment. It is not intended to reproduce a complete cryptanalytic attack from a published paper.

## Connection to implementation security

The project later moves from the mathematical LWE model to implementation behavior.

The main idea is:

LWE secret
-> cryptographic operation
-> implementation behavior
-> observable information
-> statistical analysis

This gives the project a connection between lattice mathematics and practical implementation security.
