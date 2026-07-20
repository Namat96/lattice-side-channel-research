import time

def polynomial_multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result

for size in [8, 16, 32, 64]:
    a = list(range(size))
    b = list(range(size))
    start = time.perf_counter()
    result = polynomial_multiply(a, b)
    elapsed = time.perf_counter() - start
    print("size:", size)
    print("result length:", len(result))
    print("time:", round(elapsed, 7), "seconds")
    print()
