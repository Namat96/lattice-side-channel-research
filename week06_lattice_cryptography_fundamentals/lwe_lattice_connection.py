# A small illustration of the LWE and lattice connection

q = 17
a = [3, 5]
secret = [1, -1]
error = 1

b = (a[0] * secret[0] + a[1] * secret[1] + error) % q

print("Modulus q:", q)
print("Public vector a:", a)
print("Secret:", secret)
print("Error:", error)
print("LWE sample b:", b)

print()
print("The LWE relation is:")
print("b = <a, s> + e (mod q)")
print()
print("LWE instances can be transformed into lattice problems.")
print("This example only shows the small arithmetic connection.")
