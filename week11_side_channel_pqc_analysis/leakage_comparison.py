def hamming_weight(value):
    return bin(value & 0xFF).count("1")

def leakage_score(values):
    return sum(hamming_weight(v) for v in values)

datasets = {
    "small coefficients": [1, 1, 2, 2, 3, 3],
    "larger coefficients": [7, 8, 9, 10, 11, 12],
    "mixed coefficients": [1, 8, 3, 12, 5, 15],
}

for name, values in datasets.items():
    score = leakage_score(values)
    average = score / len(values)
    print(name)
    print("values:", values)
    print("total Hamming weight:", score)
    print("average Hamming weight:", round(average, 3))
    print()
