# Compare correlation with different noise levels

import math

secret_values = [1, 2, 3, 4, 5, 6, 7, 8]


def correlation(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    numerator = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_part = sum((a - x_mean) ** 2 for a in x)
    y_part = sum((b - y_mean) ** 2 for b in y)

    if x_part == 0 or y_part == 0:
        return 0.0

    return numerator / math.sqrt(x_part * y_part)


noise_sets = [
    [0.0, 0.1, -0.1, 0.0, 0.2, -0.2, 0.1, -0.1],
    [0.0, 0.5, -0.6, 0.4, -0.3, 0.7, -0.5, 0.2],
    [1.0, -1.2, 0.8, -0.9, 1.3, -1.1, 0.7, -0.8],
]

for noise in noise_sets:
    leakage = [secret + error for secret, error in zip(secret_values, noise)]
    value = correlation(secret_values, leakage)

    print("Noise:", noise)
    print("Correlation:", round(value, 4))
    print()
