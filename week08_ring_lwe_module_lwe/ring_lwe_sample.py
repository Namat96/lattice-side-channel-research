# Small toy Ring-LWE sample

q = 17

# Polynomials are stored as coefficient lists.
a = [2, 1, 3]
secret = [1, -1, 1]
error = [0, 1, -1]


def multiply_poly(a, b):
    result = [0] * (len(a) + len(b) - 1)

    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            result[i + j] += av * bv

    return [value % q for value in result]


product = multiply_poly(a, secret)
b = [
    (product[i] if i < len(product) else 0)
    + (error[i] if i < len(error) else 0)
    for i in range(len(product))
]
b = [value % q for value in b]

print("Modulus q:", q)
print("a =", a)
print("secret =", secret)
print("error =", error)
print("Ring-LWE style sample b =", b)

print()
print("The toy relation is:")
print("b = a * s + e (mod q)")
