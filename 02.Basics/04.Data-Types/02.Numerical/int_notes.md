
# Python `int` Data Type — Notes (Basics → Advanced)

## Overview
- `int` is the integer numeric type in Python (immutable).
- Python `int` supports arbitrary precision: it can grow to have as many bits as memory allows.
- Created via integer literals (decimal, binary `0b`, octal `0o`, hex `0x`) or via `int()` constructor.

## Creation / Literals
- Decimal: `42`
- Binary: `0b101010`
- Octal: `0o52`
- Hexadecimal: `0x2A`
- Underscores allowed for readability: `1_000_000`

## Conversions
- `int(x)` converts from `float`, `str`, `Decimal`, `Fraction` (truncates floats toward zero).
- `int('123')` -> 123 ; `int('12.3')` raises `ValueError` (parse float first if needed).
- `int.from_bytes(bytes, byteorder)` and `int.to_bytes(length, byteorder)` for byte conversions.

## Arithmetic
- Standard ops: `+ - * / // % **`.
- `/` returns float. Use `//` for integer (floor) division.
- `divmod(a, b)` returns `(a // b, a % b)`.
- `pow(a, b, mod)` supports efficient modular exponentiation.

## Bitwise & Binary
- Bitwise ops: `<<`, `>>`, `&`, `|`, `^`, `~`.
- `int.bit_length()` returns the number of bits needed to represent the absolute value in binary (excluding sign bit).
- `bin(x)`, `hex(x)`, `oct(x)` convert to string representations.
- Use `int(str, base)` to parse integers in arbitrary base (2..36).

## Useful Functions & Modules
- `math.gcd(a, b)` for greatest common divisor.
- `math.isqrt(n)` for integer square root (floor).
- `math.factorial(n)` for factorials (returns `int`).
- `pow(x, y, mod)` for modular exponentiation.
- `fractions.Fraction` and `decimal.Decimal` interact with ints for precise math.

## Practical Patterns
- Check power of two: `(n & (n-1)) == 0` (for n > 0).
- Convert digits to number: `num = sum(d * 10**i for i, d in enumerate(reversed(digits)))` or accumulate using multiplication.
- Compute combinations without floating point using integer arithmetic to avoid rounding errors.

## Common Pitfalls
- `int(3.9)` truncates toward zero (not rounding to nearest).
- `int('12.0')` fails — parse to float then to int if you want `12`.
- `/` yields `float` even if perfectly divisible.
- Extremely large ints consume memory and slow down arithmetic.

## Performance
- Python `int` is implemented in C; small ints are cached (implementation detail).
- For heavy numeric work, consider specialized libraries (e.g., `numpy` for arrays, `gmpy2` for high-performance big integers) or algorithms that avoid enormous intermediate values.
- Use `math.isqrt`, `math.gcd` where possible — these are optimized C implementations.

## Advanced
- `int.to_bytes` and `int.from_bytes` are useful for cryptography, serialization, and network protocols.
- Extended Euclidean algorithm for modular inverses and CRT (Chinese remainder theorem).
- Bit operations and `bit_length` are useful for algorithms that rely on binary decomposition (FFT sizes, encryption parameters).

## Examples (quick)
```py
int('ff', 16)       # -> 255
pow(2, 1000)        # -> very large int
math.isqrt(10**12)  # -> integer square root
n.bit_length()      # -> number of bits needed
int.from_bytes(b'ABC', 'big')  # -> 4276803
```

## References & Further Reading
- Python docs: Built-in types — `int` (see official Python docs)
- `math` module documentation for `gcd`, `isqrt`, `factorial`.
- `fractions` and `decimal` module docs for exact arithmetic and conversions.
