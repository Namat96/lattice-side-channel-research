# LWE Secret Recovery Summary

In Week 4 I used small LWE examples to understand the secret recovery problem.

## LWE samples

The basic relation is:

    b = <a, s> + e (mod q)

The secret `s` is hidden, while `a` and `b` are available as samples.

## Toy recovery

I used a small exhaustive search over possible secret values. This works only
because the example is very small.

With larger parameters, searching every possible secret quickly becomes
impractical.

## Effect of noise

The error term is important in LWE. It hides the exact relation between the
public values and the secret.

Increasing the noise can make simple recovery methods less reliable.

## What I learned

These experiments helped me connect the mathematical LWE equation with a
simple secret-recovery experiment.

The code is only for study. It does not implement a practical cryptanalytic
attack.
