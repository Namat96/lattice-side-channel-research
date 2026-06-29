# Example Kyber / ML-KEM parameter information

parameter_sets = {
    "ML-KEM-512": {
        "k": 2,
        "security_level": "Category 1",
    },
    "ML-KEM-768": {
        "k": 3,
        "security_level": "Category 3",
    },
    "ML-KEM-1024": {
        "k": 4,
        "security_level": "Category 5",
    },
}

print("Example ML-KEM parameter sets")
print()

for name, values in parameter_sets.items():
    print(name)
    print("  k =", values["k"])
    print("  security category =", values["security_level"])
    print()

print("The parameter k controls the dimension of the module structure.")
