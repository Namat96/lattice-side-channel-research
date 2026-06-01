# Simple Hamming-weight leakage model

values = [1, 3, 7, 8, 12, 15, 16, 31]


def hamming_weight(value):
    return bin(value).count("1")


print("Value -> Hamming weight")
print()

for value in values:
    weight = hamming_weight(value)
    print(value, "->", weight)
