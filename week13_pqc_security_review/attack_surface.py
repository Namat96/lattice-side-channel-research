attack_surfaces = {
    "key generation": [
        "randomness",
        "secret-dependent operations",
        "temporary secret data"
    ],
    "encapsulation": [
        "polynomial arithmetic",
        "noise sampling",
        "memory access"
    ],
    "decapsulation": [
        "secret-key operations",
        "error handling",
        "verification logic"
    ],
    "digital signature": [
        "secret-dependent arithmetic",
        "randomness",
        "signature generation"
    ],
}

for stage, surfaces in attack_surfaces.items():
    print(stage)
    for item in surfaces:
        print("  -", item)
    print()
