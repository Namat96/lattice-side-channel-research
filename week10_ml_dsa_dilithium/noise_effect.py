# Simple experiment showing the effect of small noise

base_value = 20
noise_values = [-2, -1, 0, 1, 2]

print("Base value:", base_value)
print()

for noise in noise_values:
    observed = base_value + noise
    print("noise =", noise, "-> observed value =", observed)

print()
print("Small noise changes the value while keeping it close to the")
print("original value. Lattice-based signatures use carefully bounded")
print("noise and rejection procedures.")
