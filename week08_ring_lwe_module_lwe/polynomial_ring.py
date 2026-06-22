# Small polynomial ring operations

q = 17


def add_poly(a, b):
    size = max(len(a), len(b))
    result = [0] * size

    for i in range(size):
        av = a[i] if i < len(a) else 0
        bv = b[i] if i < len(b) else 0
        result[i] = (av + bv) % q

    return result


def multiply_poly(a, b):
    result = [0] * (len(a) + len(b) - 1)

    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            result[i + j] += av * bv

    return [value % q for value in result]


a = [1, 2, 3]
b = [4, 1, 2]

print("Modulus q:", q)
print("a =", a)
print("b =", b)
print("a + b =", add_poly(a, b))
print("a * b =", multiply_poly(a, b))
