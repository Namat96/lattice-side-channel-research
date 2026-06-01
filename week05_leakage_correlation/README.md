# Week 5 - Leakage Correlation Experiments

This week I looked at a simple way of connecting simulated side-channel
leakage with secret-dependent values.

The experiments use small artificial examples. The purpose is to understand
the idea of correlation and see how noise can make a leakage signal harder to
observe.

## Files

- `correlation_experiment.py` - compares a secret-related value with simulated leakage
- `hamming_weight_leakage.py` - creates simple Hamming-weight based leakage
- `noise_correlation.py` - checks how added noise changes the correlation
- `leakage_summary.md` - notes from the experiments

## Main idea

A side-channel signal can sometimes contain information related to an internal
value. In a simple model, leakage can be written as:

    leakage = secret_value + noise

If the leakage is related to a secret-dependent quantity, statistical
correlation can help show that relationship.

These are small educational experiments and are not an implementation of an
attack against a real cryptographic device.
