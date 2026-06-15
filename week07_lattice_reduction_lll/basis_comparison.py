# Compare vector lengths before and after reduction

original = [
    [7, 2],
    [3, 1],
]

reduced = [
    [3, 1],
    [1, 0],
]


def length(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


print("Original basis lengths:")
for vector in original:
    print(vector, "->", round(length(vector), 4))

print()
print("Reduced basis lengths:")
for vector in reduced:
    print(vector, "->", round(length(vector), 4))

print()
print("The reduced basis contains shorter vectors in this toy example.")
