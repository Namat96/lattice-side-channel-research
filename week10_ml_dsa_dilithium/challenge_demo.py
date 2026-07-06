# Small challenge-value demonstration

message_value = 42
commitment_value = 15

challenge = (message_value + commitment_value) % 17

print("Message value:", message_value)
print("Commitment value:", commitment_value)
print("Toy challenge:", challenge)

print()
print("In a real signature scheme, the challenge is derived using")
print("a cryptographic hash and carefully defined encoding.")
