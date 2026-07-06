# Simple educational signature verification example

public_value = 9
message_value = 4
signature_value = 13

expected = (public_value + message_value) % 17

print("Public value:", public_value)
print("Message value:", message_value)
print("Signature value:", signature_value)
print("Expected value:", expected)

if signature_value == expected:
    print("Toy verification: valid")
else:
    print("Toy verification: invalid")

print()
print("This is only a mathematical demonstration.")
print("It is not ML-DSA signature verification.")
