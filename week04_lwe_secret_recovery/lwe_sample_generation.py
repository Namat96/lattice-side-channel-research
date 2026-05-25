# Small LWE sample generation

q = 17
secret = [1, -1]

samples = [
    ([3, 5], 0),
    ([2, 7], 1),
    ([6, 4], -1),
]

print("Modulus q:", q)
print("Secret:", secret)
print()

for a, e in samples:
    b = (a[0] * secret[0] + a[1] * secret[1] + e) % q
    print("a =", a, "error =", e, "b =", b)
