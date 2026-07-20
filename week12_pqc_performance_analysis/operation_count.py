def polynomial_multiply_with_count(a, b):
    result = [0] * (len(a) + len(b) - 1)
    multiplications = 0
    additions = 0

    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
            multiplications += 1
            additions += 1

    return result, multiplications, additions

for size in [4, 8, 16]:
    a = list(range(size))
    b = list(range(size))
    _, multiplications, additions = polynomial_multiply_with_count(a, b)
    print("size:", size)
    print("multiplications:", multiplications)
    print("additions:", additions)
    print()
