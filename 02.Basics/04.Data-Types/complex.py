# complex.py - Practical examples for complex numbers

# Basic complex numbers
a = 3 + 4j
b = 2 - 1j
print("a, b:", a, b)

# Real and imaginary parts
print("a.real:", a.real)
print("a.imag:", a.imag)

# Operations
print("Addition:", a + b)
print("Multiplication:", a * b)
print("Conjugate of a:", a.conjugate())

# Combining with ints/floats
print("a + 5:", a + 5)
print("2.5 + b:", 2.5 + b)

# Invalid conversions to int/float will raise
try:
    int(a)
except Exception as e:
    print("int(complex) error:", type(e).__name__, e)
