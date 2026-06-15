# Small educational LLL-style reduction in two dimensions

basis = [
    [7, 2],
    [3, 1],
]


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def norm_squared(a):
    return dot(a, a)


def gram_schmidt(b1, b2):
    denominator = norm_squared(b1)

    if denominator == 0:
        return b1, b2, 0.0

    mu = dot(b2, b1) / denominator
    b1_star = b1[:]
    b2_star = [
        b2[0] - mu * b1[0],
        b2[1] - mu * b1[1],
    ]

    return b1_star, b2_star, mu


def reduce_basis(b1, b2):
    changed = True

    while changed:
        changed = False

        _, _, mu = gram_schmidt(b1, b2)

        if abs(mu) > 0.5:
            k = round(mu)
            b2 = [
                b2[0] - k * b1[0],
                b2[1] - k * b1[1],
            ]
            changed = True
            continue

        b1_star, b2_star, _ = gram_schmidt(b1, b2)

        if norm_squared(b2_star) < 0.75 * norm_squared(b1_star):
            b1, b2 = b2, b1
            changed = True

    return b1, b2


print("Original basis:")
print("b1 =", basis[0])
print("b2 =", basis[1])

reduced = reduce_basis(basis[0][:], basis[1][:])

print()
print("Reduced basis:")
print("b1 =", reduced[0])
print("b2 =", reduced[1])
