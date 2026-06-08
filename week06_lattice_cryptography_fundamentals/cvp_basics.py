# Small brute-force experiment for CVP

basis = [
    [2, 1],
    [1, 2],
]

target = [3, 2]

closest_point = None
closest_distance = None

for x in range(-3, 4):
    for y in range(-3, 4):
        px = x * basis[0][0] + y * basis[1][0]
        py = x * basis[0][1] + y * basis[1][1]

        distance_squared = (target[0] - px) ** 2 + (target[1] - py) ** 2

        if closest_distance is None or distance_squared < closest_distance:
            closest_distance = distance_squared
            closest_point = [px, py]

print("Target:", target)
print("Closest lattice point:", closest_point)
print("Squared distance:", closest_distance)
