# Week 12 Summary

This week focused on basic performance analysis of operations related to polynomial arithmetic.

## Main observations

1. Naive polynomial multiplication uses nested loops, so the number of coefficient multiplications grows quickly as polynomial size increases.
2. Operation counting shows this growth without depending on a particular computer.
3. Precomputing repeated values can reduce repeated arithmetic work.
4. Runtime measurements vary between computers and runs, so one timing result is not a reliable benchmark.
5. Practical PQC implementations use optimized arithmetic and algorithms such as NTT-based polynomial multiplication.

## Research connection

Earlier weeks covered Ring-LWE, Module-LWE, ML-KEM, ML-DSA, and side-channel leakage. Performance is another important implementation consideration. Practical implementations need efficient arithmetic while also considering constant-time behavior and side-channel resistance.

## Limitation

These scripts are educational models. They do not benchmark or implement production ML-KEM or ML-DSA.
