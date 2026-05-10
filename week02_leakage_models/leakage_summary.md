# Leakage Summary

In these experiments I used very small vectors to understand leakage.

## Hamming weight

Hamming weight tells how many entries of a vector are non-zero. It does not
show the exact secret, but it can still give useful information.

## Noisy leakage

Real observations can contain noise. A noisy observation may be close to a
secret-related value without being exactly correct.

## Approximate hints

An approximate hint can reduce the possible values of a secret. More hints
could give an attacker more information.

## What I learned

Leakage does not always have to reveal a secret directly. Even small pieces of
information can become useful when combined with other observations.

The examples here are educational toy experiments. They do not model the
full behaviour of a physical side-channel attack.
