# Week 4 - LWE Secret Recovery

This week I worked with small LWE examples and looked at how information from
LWE samples can be used to learn about a secret.

The examples are intentionally small so that the calculations are easy to
follow. They are for learning and do not represent a full attack on a real
lattice cryptosystem.

## Files

- `lwe_sample_generation.py` - creates small LWE samples
- `secret_recovery_toy.py` - searches for a small secret using known samples
- `noise_effect.py` - shows how error/noise affects recovery
- `recovery_summary.md` - notes from the experiments

## Main idea

A basic LWE sample can be written as:

    b = <a, s> + e (mod q)

where `a` is public, `s` is the secret, and `e` is a small error.

The goal is to see why the error term is important and why recovering a
secret becomes harder when the problem size grows.

These are toy experiments with very small parameters.
