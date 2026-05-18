# Week 03 Notes

## Hamming distance

Hamming distance tells us how many bits are different between two values.

For example:

```text
1010
1001
```

Two bits are different, so the Hamming distance is 2.

## Why it matters

In some side-channel attacks, an attacker studies changes in data during
a computation. More changing bits can sometimes mean more physical
leakage.

This does not mean that the secret can always be found directly.
Real devices also have noise and other effects.

## My small experiment

I used Python to calculate Hamming distance and to make a small
simulated leakage trace.

The experiment is only for learning the basic idea. It is not a real
power or electromagnetic measurement.
