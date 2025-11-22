# int.py - Practical examples for integers

# Basic integer assignments
a = 10
b = -5
c = 0
print("a, b, c:", a, b, c)

# Arithmetic operations
print("Addition:", a + 5)
print("Subtraction:", a - 3)
print("Multiplication:", a * 2)
print("Integer division:", 9 // 2)   # floor division
print("True division:", 9 / 2)       # gives float
print("Modulus:", 9 % 2)
print("Exponent:", 2 ** 5)

# Using int in expressions
x = 5
y = 3
print("Expression:", x * (y + 2))

# Converting from other types to int (explicit)
print("int(float):", int(7.9))
print("int(bool True):", int(True))
print("int(bool False):", int(False))
# NOTE: int("10") works, int("10.5") raises ValueError
print("int('10'):", int("10"))

# Large integers
big = 10 ** 20
print("Large int:", big)

# id() and mutability note
n = 1000
print("id before:", id(n))
n = n + 1
print("id after:", id(n))  # new object created (ints are immutable)
