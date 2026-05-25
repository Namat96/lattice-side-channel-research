# Simple experiment showing the effect of larger noise

q = 17
secret = [1, -1]
a = [5, 3]

print("Secret:", secret)
print("Public vector a:", a)
print()

for error in [0, 1, -1, 2, -2, 4]:
    b = (a[0] * secret[0] + a[1] * secret[1] + error) % q
    print("error =", error, "-> observed b =", b)

print()
print("Small errors are easier to handle in this toy example.")
print("Larger errors make the observation less direct.")
