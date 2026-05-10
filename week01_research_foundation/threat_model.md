# Threat Model

This project uses a simple experimental threat model.

## Attacker

The attacker is assumed to be able to run or observe a cryptographic operation many times and collect an observable value from the implementation.

For the timing experiments, the observable value is:

- execution time

For the approximate-hint experiments, the attacker is given controlled noisy or approximate information defined by the experiment.

## Attacker goal

The goal is to learn information about the secret, such as:

- Hamming weight
- coefficient values
- partial secret information
- or, in small experiments, the complete secret

## What the attacker does not have

The experiments do not assume access to:

- the source code of a real deployed target
- physical power measurements
- electromagnetic measurements
- protected hardware
- private keys from real users

## Experimental limitations

The project uses simplified Python implementations and small parameters. Python timing measurements can contain noise from the operating system and other processes.

Therefore, a successful experiment will demonstrate an experimental leakage effect, not automatically a practical attack on ML-KEM or another standardized scheme.

## Security goal

The main security goal is to understand whether a measurable relationship exists between secret-dependent behavior and an observable quantity, and then test whether a simple implementation change can reduce that relationship.
