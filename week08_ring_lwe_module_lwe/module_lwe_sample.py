# Small Module-LWE style sample

q = 17

a1 = [2, 1]
a2 = [1, 3]

s1 = [1, -1]
s2 = [2, 1]

e = [1, 0]


def multiply_poly(a, b):
    result = [0] * (len(a) + len(b) - 1)

    for i, av in enumerate(a):
        for j, bv in enumerate(b):
            result[i + j] += av * bv

    return [value % q for value in result]


def add_poly(a, b):
    size = max(len(a), len(b))
    result = [0] * size

    for i in range(size):
        av = a[i] if i < len(a) else 0
        bv = b[i] if i < len(b) else 0
        result[i] = (av + bv) % q

    return result


part1 = multiply_poly(a1, s1)
part2 = multiply_poly(a2, s2)
combined = add_poly(part1, part2)
combined = add_poly(combined, e)

print("Modulus q:", q)
print("A row 1 =", a1)
print("A row 2 =", a2)
print("Secret polynomial 1 =", s1)
print("Secret polynomial 2 =", s2)
print("Error =", e)
print("Toy Module-LWE result =", combined)

print()
print("The structure uses vectors of ring elements.")
