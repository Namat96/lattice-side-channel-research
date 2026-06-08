# Small brute-force experiment for SVP

basis = [
    [2, 1],
    [1, 2],
]

shortest = None
shortest_vector = None

for x in range(-3, 4):
    for y in range(-3, 4):
        if x == 0 and y == 0:
            continue

        vx = x * basis[0][0] + y * basis[1][0]
        vy = x * basis[0][1] + y * basis[1][1]
        length_squared = vx * vx + vy * vy

        if shortest is None or length_squared < shortest:
            shortest = length_squared
            shortest_vector = [vx, vy]

print("Shortest vector found in this small search:", shortest_vector)
print("Squared length:", shortest)
