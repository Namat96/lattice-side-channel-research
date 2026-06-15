# Gram-Schmidt values for a small lattice basis

import math

basis = [
    [4.0, 1.0],
    [1.0, 3.0],
]

b1 = basis[0]
b2 = basis[1]

dot_b2_b1 = b2[0] * b1[0] + b2[1] * b1[1]
dot_b1_b1 = b1[0] * b1[0] + b1[1] * b1[1]

mu21 = dot_b2_b1 / dot_b1_b1

b1_star = b1
b2_star = [
    b2[0] - mu21 * b1[0],
    b2[1] - mu21 * b1[1],
]

length_b1_star = math.sqrt(b1_star[0] ** 2 + b1_star[1] ** 2)
length_b2_star = math.sqrt(b2_star[0] ** 2 + b2_star[1] ** 2)

print("Original basis:", basis)
print("mu_21:", round(mu21, 4))
print("b1*:", b1_star)
print("b2*:", [round(x, 4) for x in b2_star])
print("||b1*||:", round(length_b1_star, 4))
print("||b2*||:", round(length_b2_star, 4))
