# Toy secret recovery by exhaustive search

q = 17

# Public LWE samples: (a, b)
samples = [
    ([3, 5], 15),
    ([2, 7], 13),
    ([6, 4], 1),
]

candidates = []

for s1 in range(-2, 3):
    for s2 in range(-2, 3):
        errors = []

        for a, b in samples:
            value = (a[0] * s1 + a[1] * s2) % q
            error = (b - value) % q

            if error > q // 2:
                error -= q

            errors.append(error)

        if all(abs(e) <= 1 for e in errors):
            candidates.append(([s1, s2], errors))

print("Possible secrets with small errors:")

for secret, errors in candidates:
    print("secret =", secret, "errors =", errors)
