# Simple Hamming weight experiment

secret = [1, 0, -1, 1, 0, 1, -1, 0]

weight = sum(1 for x in secret if x != 0)

print("Secret vector:", secret)
print("Hamming weight:", weight)
print("This only gives the number of non-zero values, not their positions.")
