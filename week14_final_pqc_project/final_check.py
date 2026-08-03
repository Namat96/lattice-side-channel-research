from pathlib import Path

expected = [
    "README.md",
    "project_overview.md",
    "research_findings.md",
    "limitations_and_future_work.md",
    "final_report.md",
    "final_check.py",
]

print("Week 14 final project check")
print("-" * 40)

passed = 0

for name in expected:
    exists = Path(name).is_file()
    print(f"[{'PASS' if exists else 'MISSING'}] {name}")
    if exists:
        passed += 1

print()
print(f"Files found: {passed}/{len(expected)}")

if passed == len(expected):
    print("Final Week 14 structure check: PASS")
else:
    print("Final Week 14 structure check: REVIEW")
