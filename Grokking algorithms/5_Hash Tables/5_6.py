# A mapping from battery size to power. 
# The sizes are A, AA, AAA, and AAAA.

size_to_power = {}

# Use the length of the string as the index.
size_to_power["A"] = len("A")
size_to_power["AA"] = len("AA")
size_to_power["AAA"] = len("AAA")
size_to_power["AAAA"] = len("AAAA")

print(size_to_power)

# Map every letter to a prime number: a = 2, b = 3, c = 5, d = 7, e = 11, and so on. 
# For a string, the hash function is the sum of all the characters modulo the size of the hash. 
# For example, if your hash size is 10, and the string is “bag”, 
# the index is 3 + 2 + 17 % 10 = 22 % 10 = 2.
size_to_power["A"] = 2
size_to_power["AA"] = (2+2) % 10
size_to_power["AAA"] = (2+2+2) % 10
size_to_power["AAAA"] = (2+2+2+2) % 10

print(size_to_power)