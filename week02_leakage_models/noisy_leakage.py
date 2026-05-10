# Simple noisy leakage example

secret = [1, -1, 0, 1, 0, -1]

# A small leakage value based on the secret.
leakage = [abs(x) for x in secret]

# Add a fixed small error pattern to make the observation noisy.
noise = [0, 1, 0, -1, 0, 0]
observed = [a + b for a, b in zip(leakage, noise)]

print("Secret:", secret)
print("Basic leakage:", leakage)
print("Noise:", noise)
print("Observed leakage:", observed)

print()
print("The observed values are not the secret itself.")
print("Noise can make recovery harder.")
