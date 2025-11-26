
"""
int_practicals.py
Comprehensive practical examples for the Python `int` type.
Covers: creation, conversion, arithmetic, bitwise, performance, utilities, and common pitfalls.
Run this file with: python int_practicals.py
"""

import math
from fractions import Fraction
from decimal import Decimal

# ---------- Basics ----------
# Creation: integer literals (decimal, binary, octal, hexadecimal).
a = 42                 # decimal
b = 0b101010           # binary (42)
c = 0o52               # octal (42)
d = 0x2A               # hexadecimal (42)
e = 1_000_000          # underscores allowed for readability (PEP 515)

print("Basics:")
print("a, b, c, d, e:", a, b, c, d, e)
print("All equal? ", a == b == c == d)

# Type & large integers (arbitrary precision)
huge = 10 ** 50        # Python supports arbitrarily large integers
print("huge bit_length:", huge.bit_length())

# ---------- Conversions ----------
print("\nConversions:")
print("int(3.9) ->", int(3.9))              # truncates toward zero
print("int(-3.9) ->", int(-3.9))            # truncates toward zero (gives -3)
print("int('123') ->", int("123"))
# Handling invalid conversion
try:
    int("12.3")  # ValueError: cannot convert string with decimal point directly
except ValueError as ve:
    print("int('12.3') raises:", ve)

# Convert from float safely (round first if intended)
print("int(round(12.7)) ->", int(round(12.7)))

# From Decimal and Fraction
print("int(Decimal('12.99')) ->", int(Decimal('12.99')))
print("int(Fraction(7,2)) ->", int(Fraction(7,2)))

# from_bytes / to_bytes
x = 1024
byte_len = (x.bit_length() + 7) // 8 or 1
bts = x.to_bytes(byte_len, byteorder='big')
print("1024 -> bytes:", bts, " -> int.from_bytes ->", int.from_bytes(bts, 'big'))

# ---------- Arithmetic ----------
print("\nArithmetic:")
print("5 + 3 =", 5 + 3)
print("5 - 3 =", 5 - 3)
print("5 * 3 =", 5 * 3)
print("5 / 2 =", 5 / 2)      # float division
print("5 // 2 =", 5 // 2)    # floor division producing int
print("5 % 2 =", 5 % 2)
print("pow(2, 10) =", pow(2, 10))
print("pow(2, 10, 1000) -> modular pow =", pow(2, 10, 1000))

# divmod
print("divmod(17, 5) -> (quotient, remainder):", divmod(17, 5))

# ---------- Bitwise operations ----------
print("\nBitwise operations:")
print("5 << 2 =", 5 << 2)
print("20 >> 2 =", 20 >> 2)
print("~5 =", ~5)             # bitwise NOT (two's complement)
print("5 & 3 =", 5 & 3)
print("5 | 3 =", 5 | 3)
print("5 ^ 3 =", 5 ^ 3)

# Useful bit functions
n = 0b101100
print("n bit_length:", n.bit_length())
print("Is power of two check (fast):", (n & (n - 1)) == 0)

# ---------- Useful built-ins and math ----------
print("\nMath & builtins:")
print("abs(-7) ->", abs(-7))
print("math.gcd(48,18) ->", math.gcd(48, 18))
print("math.isqrt(10**6) -> integer sqrt:", math.isqrt(10**6))
print("int.bit_length example:", (123456).bit_length())

# Factorial (big ints):
print("math.factorial(20) ->", math.factorial(20))

# ---------- Practical examples / small programs ----------
print("\nPracticals:")

# 1) Check prime (simple deterministic for small n)
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

print("is_prime(97):", is_prime(97))
print("is_prime(100):", is_prime(100))

# 2) GCD and LCM
def lcm(a: int, b: int) -> int:
    return abs(a // math.gcd(a, b) * b)

print("lcm(12, 15):", lcm(12, 15))

# 3) Modular inverse (uses extended Euclid). Returns None if not invertible.
def egcd(a: int, b: int):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def modinv(a: int, m: int):
    g, x, _ = egcd(a, m)
    if g != 1:
        return None  # inverse doesn't exist
    return x % m

print("modinv(3, 11):", modinv(3, 11))

# 4) Fast modular exponentiation (built-in pow supports it)
print("pow(7, 128, 13):", pow(7, 128, 13))

# 5) Convert list of digits to int and back
digits = [1,2,3,4]
num = 0
for d in digits:
    num = num * 10 + d
print("digits->int:", digits, "->", num)
print("int->digits via string:", list(str(num)))

# 6) Binary digit count and parity check
def popcount(n: int) -> int:
    return bin(n).count('1')
print("popcount(0b101101):", popcount(0b101101))

# 7) Swap two integers without temp (Pythonic way uses tuple unpacking)
x, y = 5, 9
x, y = y, x
print("Swapped via tuple:", x, y)

# 8) Working with negative numbers and shifts
neg = -8
print("neg >> 2 (arithmetic shift):", neg >> 2)

# 9) Efficiently compute combinations using integers only
def nCr(n: int, r: int) -> int:
    if r < 0 or r > n: return 0
    r = min(r, n - r)
    num = 1
    den = 1
    for i in range(1, r+1):
        num *= n - r + i
        den *= i
    return num // den

print("nCr(20, 6):", nCr(20, 6))

# 10) Working with bytes for crypto-ish examples
message = b'ABC'
m_int = int.from_bytes(message, 'big')
print("message bytes -> int:", m_int, "-> back to bytes:", m_int.to_bytes(len(message), 'big'))

# ---------- Performance tips & pitfalls ----------
print("\nPerformance & Pitfalls:")
print("1) / returns float even for divisible ints (use // for integer division).")
print("2) ints are arbitrary precision but very large ints cost CPU & memory.")
print("3) converting floats to int truncates toward zero (not round).")
print("4) be careful with int('12.0') -> ValueError; parse as float first or strip decimals.")

# ---------- Formatting & representation ----------
print("\nFormatting:")
n = 255
print("bin(n):", bin(n))
print("hex(n):", hex(n))
print("oct(n):", oct(n))
print("format(n, 'b') ->", format(n, 'b'))
print(f"f-string format: {n:#04x}")

# ---------- Advanced / Niche ----------
print("\nAdvanced:")
# Using int with custom base parsing
print("int('1011', 2) ->", int('1011', 2))
print("int('ff', 16) ->", int('ff', 16))

# Negative base example (rare) - Python's int doesn't support negative bases directly in int(str, base)
# but you can parse using custom logic if needed (left as exercise).

# Use-case: implement a fast integer sqrt check (perfect square)
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n

print("is_perfect_square(10**6):", is_perfect_square(10**6))
print("is_perfect_square(10**6 + 1):", is_perfect_square(10**6 + 1))

# End of practical examples
if __name__ == '__main__':
    print("\nRan int_practicals.py - examples above demonstrate int usage.")
