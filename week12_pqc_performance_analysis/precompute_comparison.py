import time

def repeated_calculation(values, rounds):
    total = 0
    for _ in range(rounds):
        for value in values:
            total += value * value
    return total

def precomputed_calculation(values, rounds):
    squares = [value * value for value in values]
    total = 0
    for _ in range(rounds):
        for value in squares:
            total += value
    return total

values = list(range(64))
rounds = 5000

start = time.perf_counter()
result1 = repeated_calculation(values, rounds)
time1 = time.perf_counter() - start

start = time.perf_counter()
result2 = precomputed_calculation(values, rounds)
time2 = time.perf_counter() - start

print("repeated calculation")
print("result:", result1)
print("time:", round(time1, 6), "seconds")
print()
print("precomputed values")
print("result:", result2)
print("time:", round(time2, 6), "seconds")
print()
print("results equal:", result1 == result2)
