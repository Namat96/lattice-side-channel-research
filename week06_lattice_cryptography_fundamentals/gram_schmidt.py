# Gram-Schmidt orthogonalization for two vectors

import math

v1 = [2.0, 1.0]
v2 = [1.0, 2.0]

dot_v2_v1 = v2[0] * v1[0] + v2[1] * v1[1]
dot_v1_v1 = v1[0] * v1[0] + v1[1] * v1[1]

coefficient = dot_v2_v1 / dot_v1_v1

u1 = v1
u2 = [
    v2[0] - coefficient * v1[0],
    v2[1] - coefficient * v1[1],
]

length_u2 = math.sqrt(u2[0] ** 2 + u2[1] ** 2)

print("First orthogonal vector:", u1)
print("Second orthogonal vector:", u2)
print("Length of second vector:", round(length_u2, 4))
