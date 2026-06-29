# Small educational polynomial transformation demo

q = 17
polynomial = [1, 2, 3, 4]

print("Modulus q:", q)
print("Original polynomial:", polynomial)

# This is only a simple reversible coefficient rearrangement.
# It is NOT an implementation of the ML-KEM NTT.
transformed = polynomial[::2] + polynomial[1::2]

print("Transformed coefficients:", transformed)
print()
print("In ML-KEM, the actual NTT is a specific modular transform")
print("used to make polynomial multiplication more efficient.")
