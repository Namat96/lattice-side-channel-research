# Lattice basis as a matrix

basis = [
    [2, 1],
    [1, 2],
]

print("Lattice basis matrix:")
for row in basis:
    print(row)

determinant = basis[0][0] * basis[1][1] - basis[0][1] * basis[1][0]

print()
print("Determinant:", determinant)
print("This gives the area of the fundamental parallelogram in 2D.")
