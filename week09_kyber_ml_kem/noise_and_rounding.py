# Simple demonstration of noise and rounding

q = 17
values = [3.1, 3.8, 7.2, 7.9]

print("Modulus q:", q)
print("Values:", values)
print()

for value in values:
    rounded = round(value)
    reduced = rounded % q
    print("value =", value, "rounded =", rounded, "mod q =", reduced)

print()
print("Noise and rounding are important parts of lattice-based schemes.")
print("ML-KEM uses carefully defined compression and decompression procedures.")
