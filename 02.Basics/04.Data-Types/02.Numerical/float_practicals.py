
"""
float_practicals.py
Comprehensive practical examples for the Python `float` type.
Covers: creation, representation, arithmetic, precision issues, formatting, rounding, IEEE 754 behavior,
special values (inf, -inf, nan), conversions, Decimal vs float, struct packing, and practical recipes.
Run this file with: python float_practicals.py
"""

import math
import struct
from decimal import Decimal, getcontext, ROUND_HALF_EVEN
from fractions import Fraction

# ---------- Basics ----------
# Creation
a = 3.14
b = float(10)           # from int
c = float("2.71828")    # from str
d = 1e3                 # scientific notation (1000.0)
e = 1.23e-4             # small numbers

print("Basics:")
print("a, b, c, d, e:", a, b, c, d, e)
print("Type check: type(a) ->", type(a))

# Special float values
pos_inf = float('inf')
neg_inf = float('-inf')
nan_val = float('nan')
print("inf, -inf, nan:", pos_inf, neg_inf, nan_val)
print("math.isfinite(pos_inf):", math.isfinite(pos_inf))
print("math.isnan(nan_val):", math.isnan(nan_val))

# ---------- Representation & Precision ----------
print("\nRepresentation & Precision:")
x = 0.1 + 0.2
print("0.1 + 0.2 ->", x)  # shows floating point rounding
print("repr(0.1) ->", repr(0.1))
print("format(0.1, '.17g') ->", format(0.1, '.17g'))  # shows underlying binary rounding

# Using Decimal for precise decimal arithmetic
print("\nDecimal vs float:")
getcontext().prec = 28
dec_sum = Decimal('0.1') + Decimal('0.2')
float_sum = 0.1 + 0.2
print("Decimal('0.1') + Decimal('0.2') ->", dec_sum)
print("0.1 + 0.2 ->", float_sum)

# ---------- Conversions ----------
print("\nConversions:")
print("int(3.9) ->", int(3.9))    # truncates toward zero
print("float(7) ->", float(7))
print("float.fromhex('0x1.999999999999ap-4') ->", float.fromhex('0x1.999999999999ap-4'))
print("0.1.hex() ->", (0.1).hex())

# ---------- Arithmetic ----------
print("\nArithmetic:")
print("5.0 + 3.2 =", 5.0 + 3.2)
print("5.0 - 3.2 =", 5.0 - 3.2)
print("5.0 * 3.2 =", 5.0 * 3.2)
print("5.0 / 2.0 =", 5.0 / 2.0)
print("5.0 // 2.0 =", 5.0 // 2.0)   # floor division -> float or int depending
print("divmod(5.3, 2.0) ->", divmod(5.3, 2.0))

# ---------- Rounding & Formatting ----------
print("\nRounding & Formatting:")
print("round(2.5) ->", round(2.5))   # ties to even in Python 3
print("round(3.5) ->", round(3.5))
print("round(2.675, 2) ->", round(2.675, 2))  # surprising due to binary rep
print("format(1234.5678, ',.2f') ->", format(1234.5678, ',.2f'))
print("f-string: f'{math.pi:.6f}' ->", f"{math.pi:.6f}")

# Decimal rounding for financial use
print("\nDecimal rounding example:")
getcontext().rounding = ROUND_HALF_EVEN
d = Decimal('2.675')
print("Decimal('2.675').quantize(Decimal('0.01')) ->", d.quantize(Decimal('0.01')))

# ---------- Comparisons & Equality ----------
print("\nComparisons & Equality:")
print("0.0 == -0.0 ->", 0.0 == -0.0)
print("math.copysign(1.0, -0.0) ->", math.copysign(1.0, -0.0))
print("NaN comparisons: nan == nan ->", nan_val == nan_val, "; math.isnan(nan) ->", math.isnan(nan_val))

# Use math.isclose for robust comparisons
print("math.isclose(0.1 + 0.2, 0.3) ->", math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=0.0))

# ---------- Bit-level & Binary Formats ----------
print("\nBit-level & binary formats:")
# Pack/unpack using struct to see IEEE 754 binary layout (double precision)
def float_to_bits(f: float) -> int:
    packed = struct.pack('>d', f)   # big-endian double
    return int.from_bytes(packed, 'big')

def bits_to_float(b: int) -> float:
    packed = b.to_bytes(8, 'big')
    return struct.unpack('>d', packed)[0]

val = 0.1
bits = float_to_bits(val)
print("float_to_bits(0.1) ->", hex(bits))
reconstructed = bits_to_float(bits)
print("reconstructed ->", reconstructed)
print("0.1.hex() ->", val.hex())

# ---------- Practical examples / small programs ----------
print("\nPracticals:")

# 1) Simple interest calculator (float OK for display, use Decimal for money)
def simple_interest(principal: float, rate: float, years: int) -> float:
    return principal * (1 + rate * years)

print("Simple interest (1000, 0.05, 3):", simple_interest(1000.0, 0.05, 3))

# 2) Simpson's rule approximate integral (floating arithmetic heavy)
def simpson(f, a, b, n=1000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        coef = 4 if i % 2 else 2
        s += coef * f(a + i * h)
    return s * h / 3

print("Simpson integrate sin from 0 to pi:", simpson(math.sin, 0, math.pi, 1000))

# 3) Convert float to rational approximation using Fraction.limit_denominator
f = 3.141592653589793
print("Fraction(f).limit_denominator(10000) ->", Fraction(f).limit_denominator(10000))

# 4) Numeric stability example: naive vs Kahan summation
def naive_sum(arr):
    s = 0.0
    for v in arr:
        s += v
    return s

def kahan_sum(arr):
    s = 0.0
    c = 0.0
    for v in arr:
        y = v - c
        t = s + y
        c = (t - s) - y
        s = t
    return s

small = [1e-8] * 1000000 + [1.0]
print("naive_sum small list ->", naive_sum(small))
print("kahan_sum small list ->", kahan_sum(small))

# 5) Parsing user input robustly (strip, handle commas)
def parse_float(s: str) -> float:
    s = s.strip().replace(',', '')
    return float(s)

print("parse_float(' 1,234.56 ') ->", parse_float(' 1,234.56 '))

# ---------- Performance tips & pitfalls ----------
print("\nPerformance & Pitfalls:")
print("1) floats are 64-bit doubles by default (IEEE 754).")
print("2) For monetary calculations, prefer Decimal or integer cents.")
print("3) Floating comparisons should use math.isclose.")
print("4) Be aware of catastrophic cancellation and accumulation error.")

# ---------- Formatting & Localization ----------
print("\nFormatting & Localization:")
# Locale-specific formatting is available via locale module (not shown to keep example simple)
print("format(1234567.89, ',.2f') ->", format(1234567.89, ',.2f'))

# ---------- Advanced / Niche ----------
print("\nAdvanced:")

# 1) Handle binary64 edge-cases using hex floats
x = float.fromhex('0x1.0000000000000p+0')  # 1.0
y = float.fromhex('0x1.0000000000001p+0')  # smallest representable double > 1.0
print("x, y, y - x:", x, y, y - x)

# 2) Use Decimal with context for bankers rounding or specific precision
getcontext().prec = 10
getcontext().rounding = ROUND_HALF_EVEN
d1 = Decimal('1.23456789')
print("Decimal with context:", d1.quantize(Decimal('0.0001')))

# 3) Converting floats to integer safely when appropriate
def safe_int_from_float(f):
    if not math.isfinite(f):
        raise ValueError("cannot convert infinite/NaN to int")
    return int(round(f))

print("safe_int_from_float(3.6) ->", safe_int_from_float(3.6))

# 4) Financial rounding examples with Decimal
getcontext().prec = 28
money = Decimal('2.675')
rounded_money = money.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
print("rounded_money ->", rounded_money)

# 5) Use numpy for vectorized float ops (example shown as comment)
# import numpy as np
# arr = np.linspace(0.0, 1.0, 1000000)
# print("numpy mean:", arr.mean())

# End of practical examples
if __name__ == '__main__':
    print("\nRan float_practicals.py - examples above demonstrate float usage.")
