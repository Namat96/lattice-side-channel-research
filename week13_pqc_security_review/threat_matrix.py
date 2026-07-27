threats = [
    ("Timing leakage", "Secret-dependent execution time", "Use constant-time techniques"),
    ("Power/EM leakage", "Physical leakage from computation", "Use implementation-level side-channel protections"),
    ("Fault injection", "Induced computation errors", "Use validation and fault detection"),
    ("Weak randomness", "Predictable secret values", "Use a secure random source"),
    ("Parameter misuse", "Incorrect or unsafe parameters", "Follow standardized parameter sets"),
]

print("PQC Threat and Mitigation Matrix")
print("-" * 72)

for threat, effect, mitigation in threats:
    print("Threat:", threat)
    print("Effect:", effect)
    print("Mitigation:", mitigation)
    print()
