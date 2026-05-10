# Research Questions

This project is based on a few simple research questions.

## Main question

Can observable information from a lattice-based cryptographic implementation reveal useful information about a secret?

## LWE questions

1. How does the Hamming weight of a sparse ternary secret affect LWE samples?
2. How does the amount of noise affect recovery of a small secret?
3. How does the number and quality of approximate hints affect recovery?
4. Under what small experimental conditions can a sparse LWE secret be recovered?

## Side-channel questions

1. Can a secret-dependent operation produce measurable timing differences?
2. Can statistical analysis distinguish different secret properties from timing measurements?
3. How much does a simple constant-operation style implementation reduce the observed leakage?
4. What performance overhead is introduced by the countermeasure?

## Research approach

I will start with small and controlled experiments. Results will be recorded in tables and plots. The aim is to understand the relationship between mathematical properties, implementation behavior, and observable leakage.

The results will not be treated as evidence that a real-world standardized implementation is vulnerable unless the experiment actually supports that claim.
