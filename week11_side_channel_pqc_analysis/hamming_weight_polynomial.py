def hamming_weight(value):
    return bin(value & 0xFF).count("1")

def polynomial_leakage(coefficients, q=17):
    reduced = [c % q for c in coefficients]
    weights = [hamming_weight(c) for c in reduced]

    print("coefficients:", reduced)
    print("hamming weights:", weights)
    print("total leakage proxy:", sum(weights))

samples = [
    [1, 2, 3, 4],
    [7, 8, 9, 10],
    [15, 16, 0, 1],
]

for sample in samples:
    polynomial_leakage(sample)
    print()
