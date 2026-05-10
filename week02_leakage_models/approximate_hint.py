# Approximate hint experiment

secret = [1, -1, 0, 1, 0, -1, 1]

# Suppose an attacker learns only an approximate total.
true_sum = sum(secret)
hint = true_sum + 1

print("Secret vector:", secret)
print("True sum:", true_sum)
print("Approximate hint:", hint)

if abs(hint - true_sum) <= 1:
    print("The hint is close to the real value.")
    print("It gives some information about the secret.")
else:
    print("The hint is not useful in this small example.")
