# Leakage Correlation Summary

In Week 5 I experimented with a simple statistical view of side-channel
leakage.

## Correlation

The first experiment used secret-related values and simulated leakage values.
The correlation was high because the leakage was intentionally close to the
secret-related value.

## Hamming weight

I also used Hamming weight as a simple leakage model. Different integer
values can have different numbers of set bits, which gives a basic example of
how an internal value can be represented by a measurable quantity.

## Noise

The last experiment added different amounts of artificial noise. As the
noise becomes larger, the relationship between the secret-related value and
the leakage can become less clear.

## What I learned

A side-channel experiment does not only depend on the secret. The leakage
model, measurement noise, and statistical method also affect what can be
observed.

These experiments are only educational and use artificial data.
