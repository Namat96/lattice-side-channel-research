# Simple Hamming distance example

def hamming_distance(a, b):
    return bin(a ^ b).count("1")


value1 = 0b10101010
value2 = 0b10001110

distance = hamming_distance(value1, value2)

print("Value 1:", format(value1, "08b"))
print("Value 2:", format(value2, "08b"))
print("Hamming distance:", distance)
