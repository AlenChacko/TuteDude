# bytes.py - Practical examples for bytes

# Creating bytes from list of ints
b = bytes([65,66,67])
print("b:", b)
print("type:", type(b))

# Encoding string to bytes
s = "Hello"
b2 = s.encode('utf-8')
print("encoded:", b2)

# bytes are immutable
try:
    b[0] = 90
except Exception as e:
    print("bytes mutation error:", type(e).__name__, e)

# Iterating bytes
for by in b2:
    print(by, end=' ')
print()
