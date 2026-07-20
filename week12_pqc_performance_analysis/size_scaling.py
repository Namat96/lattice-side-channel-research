import time

def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result

print("Polynomial size scaling")
for size in [8, 16, 32, 64, 128]:
    a = [1] * size
    b = [2] * size
    start = time.perf_counter()
    multiply(a, b)
    elapsed = time.perf_counter() - start
    print("size =", size, "| time =", round(elapsed, 7), "seconds")
