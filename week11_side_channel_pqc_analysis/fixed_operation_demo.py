import time

def fixed_operation(secret):
    total = 0
    for value in secret:
        # Both paths perform the same basic arithmetic work.
        add_value = 1 + (value & 1) * 2
        total += add_value
    return total

def measure(secret, repetitions=2000):
    start = time.perf_counter()
    result = 0
    for _ in range(repetitions):
        result += fixed_operation(secret)
    elapsed = time.perf_counter() - start
    return elapsed, result

samples = {
    "all zero": [0] * 32,
    "all one": [1] * 32,
    "mixed": [0, 1] * 16,
}

for name, secret in samples.items():
    elapsed, result = measure(secret)
    print(name)
    print("time:", round(elapsed, 6), "seconds")
    print("result:", result)
    print()
