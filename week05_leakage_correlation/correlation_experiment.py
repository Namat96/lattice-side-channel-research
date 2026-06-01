# Simple correlation experiment

import math

secret_values = [1, 2, 3, 4, 5, 6, 7, 8]
leakage = [1.2, 2.1, 3.2, 3.8, 5.1, 5.9, 7.2, 8.1]


def correlation(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    numerator = sum((a - x_mean) * (b - y_mean) for a, b in zip(x, y))
    x_part = sum((a - x_mean) ** 2 for a in x)
    y_part = sum((b - y_mean) ** 2 for b in y)

    return numerator / math.sqrt(x_part * y_part)


print("Secret-related values:", secret_values)
print("Simulated leakage:", leakage)
print("Correlation:", round(correlation(secret_values, leakage), 4))
