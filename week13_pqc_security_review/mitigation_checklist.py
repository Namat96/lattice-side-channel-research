checks = {
    "Avoid secret-dependent branches": True,
    "Use secure randomness": True,
    "Validate inputs": True,
    "Avoid accidental secret logging": True,
    "Use standardized parameters": True,
    "Review memory handling": True,
}

passed = 0

for item, status in checks.items():
    mark = "PASS" if status else "REVIEW"
    print(f"[{mark}] {item}")
    if status:
        passed += 1

print()
print("Checklist:", passed, "/", len(checks), "items marked for review")
