# Small polynomial operations used to illustrate ML-DSA arithmetic

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
            result[i + j] = (result[i + j] + av * bv) % q

    return result


a = [1, 2, 1]
b = [2, 1, 3]

print("Modulus q:", q)
print("a =", a)
print("b =", b)
print("a + b =", add_poly(a, b))
print("a * b =", multiply_poly(a, b))
