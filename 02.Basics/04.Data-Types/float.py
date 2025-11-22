# float.py - Practical examples for floats

# Basic float assignments
x = 3.14
y = -0.5
z = 10.0
print("x, y, z:", x, y, z)

# Arithmetic with floats
print("Addition:", x + 2.0)
print("Subtraction:", x - 1.14)
print("Multiplication:", x * 2)
print("Division:", 7 / 2)
print("Floor division (float result floored):", 7.0 // 2)
print("Modulus:", 7.5 % 2)

# float with int
print("float + int:", x + 2)

# Conversions
print("float(10):", float(10))
print("float('10.5'):", float("10.5"))
print("float(True):", float(True))

# Rounding and formatting
a = 2.6789
print("round(a, 2):", round(a, 2))
print("format {:.2f}:".format(a), "{:.2f}".format(a))

# Floating point precision demonstration
print("0.1 + 0.2 == 0.3 ?", (0.1 + 0.2) == 0.3)
print("0.1 + 0.2:", 0.1 + 0.2)
