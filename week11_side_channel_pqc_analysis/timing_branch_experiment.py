import time
import random

def secret_dependent_operation(secret):
    total = 0
    for value in secret:
        if value == 1:
            total += 3
        else:
            total += 1
    return total

def measure(secret, repetitions=2000):
    start = time.perf_counter()
    result = 0
    for _ in range(repetitions):
        result += secret_dependent_operation(secret)
    elapsed = time.perf_counter() - start
    return elapsed, result

random.seed(11)

low_branch = [0] * 32
high_branch = [1] * 32
mixed = [random.randint(0, 1) for _ in range(32)]

for name, secret in [
    ("mostly zero", low_branch),
    ("mostly one", high_branch),
    ("mixed", mixed),
]:
    elapsed, result = measure(secret)
    print(name)
    print("time:", round(elapsed, 6), "seconds")
    print("result:", result)
    print()
