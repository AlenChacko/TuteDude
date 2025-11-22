# tuple.py - Practical examples for tuples

# Creating tuples
t = (10, 20, 30)
print("t:", t)
single = (5,)
print("single:", single)

# Accessing
print("t[1]:", t[1])

# Immutable behavior
try:
    t[0] = 100
except Exception as e:
    print("tuple modification error:", type(e).__name__, e)

# Unpacking
a, b, c = t
print("unpacked:", a, b, c)

# Tuple conversion
print("tuple([1,2,3]):", tuple([1,2,3]))
