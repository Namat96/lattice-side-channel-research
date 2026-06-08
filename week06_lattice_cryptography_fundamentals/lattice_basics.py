# Basic lattice example

basis = [
    [2, 1],
    [1, 2],
]

print("Basis vectors:")
for vector in basis:
    print(vector)

print()
print("Some lattice points:")

for x in range(-2, 3):
    for y in range(-2, 3):
        point_x = x * basis[0][0] + y * basis[1][0]
        point_y = x * basis[0][1] + y * basis[1][1]
        print("(", point_x, ",", point_y, ")")
