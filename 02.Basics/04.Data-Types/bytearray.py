# bytearray.py - Practical examples for bytearray

# Creating bytearray
ba = bytearray([65,66,67])
print("ba:", ba)

# Mutating bytearray
ba[0] = 90
print("after mutation:", ba)

# from string with encoding
ba2 = bytearray("ABC", "utf-8")
print("ba2:", ba2)
ba2.extend(b"DEF")
print("after extend:", ba2)
