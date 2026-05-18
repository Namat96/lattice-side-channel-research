# Small simulated leakage example

values = [3, 7, 7, 2, 5, 1, 6, 4]

print("Simulated leakage values:")

for value in values:
    leakage = bin(value).count("1")
    print("Value:", value, "Leakage:", leakage)
