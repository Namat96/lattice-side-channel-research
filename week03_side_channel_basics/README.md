# Week 03 - Side-Channel Basics

## Goal

This week I studied a simple side-channel idea.

A program can give information about secret data through its behavior.
One simple example is the change between two values. This is called
Hamming distance.

I used small Python examples so the idea is easy to see.

## Files

- `hamming_distance.py` - calculates the Hamming distance between two bit values.
- `leakage_trace.py` - makes a small simulated leakage trace.
- `notes.md` - short notes about what I learned.

## What I learned

Hamming distance counts how many bits change from one value to another.

This can be useful in side-channel research because the number of
changing bits can be related to physical leakage in some devices.

The examples in this week are only simulations. They are not real
measurements from a device.
