# Simple size-reduction step for a 2D basis

basis = [
    [7, 2],
    [3, 1],
]

b1 = basis[0]
b2 = basis[1]

dot = b2[0] * b1[0] + b2[1] * b1[1]
norm = b1[0] * b1[0] + b1[1] * b1[1]

mu = round(dot / norm)

reduced_b2 = [
    b2[0] - mu * b1[0],
    b2[1] - mu * b1[1],
]

print("Original basis:")
print("b1 =", b1)
print("b2 =", b2)

print()
print("mu =", mu)
print("Reduced b2 =", reduced_b2)
