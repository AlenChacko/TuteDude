
# Python `float` Data Type — Notes (Basics → Advanced)

## Overview
- `float` in Python is a double-precision (binary64) floating point number following the IEEE 754 standard.
- Useful for scientific computing and general fractional numbers, but has limitations in decimal precision.
- For exact decimal arithmetic (money), use `decimal.Decimal` or integer cents.

## Creation / Literals
- Decimal literal: `3.14`
- Scientific notation: `1e3` (1000.0), `1.23e-4`
- From string: `float("2.5")`
- Special values: `float('inf')`, `float('-inf')`, `float('nan')`

## Representation & Precision
- Floats are binary fractions; many decimal fractions cannot be represented exactly (e.g., 0.1).
- Use `repr()` or `format(x, '.17g')` to inspect underlying representation.
- `float.hex()` and `float.fromhex()` allow exact hexadecimal representation and reconstruction.

## Conversions
- `int(x)` truncates toward zero; use `round()` if you want rounding.
- `Decimal` and `Fraction` interact with floats; prefer constructing Decimal from string to avoid binary rounding issues.
- Use `struct.pack`/`unpack` or `int.from_bytes` to inspect the raw IEEE 754 bits.

## Arithmetic & Functions
- Standard arithmetic: `+ - * / // % **`.
- `/` gives floating division; `//` is floor division (result may be float).
- `math` module provides `isfinite`, `isnan`, `copysign`, `frexp`, `ldexp`, `isclose`, `nextafter`, and more.
- Use `math.isclose` for comparison with `rel_tol` and `abs_tol` parameters.

## Rounding & Formatting
- `round()` in Python 3 uses "bankers' rounding" (round ties to even).
- Decimal's `quantize()` allows precise control for financial rounding modes (ROUND_HALF_EVEN, ROUND_HALF_UP, etc.).
- Use format specifications: `:.2f`, `:.6g`, `:,` for thousands separators, etc.

## Special Values & Comparisons
- `nan` is unordered: `nan != nan` and `math.isnan(x)` should be used.
- `0.0` and `-0.0` are equal but have different signs (`math.copysign` to inspect).
- `math.isfinite(x)` checks for finite numbers.

## Numerical Stability & Algorithms
- Floating arithmetic accumulates rounding error; for summing many small values use compensated algorithms (Kahan summation).
- Avoid subtracting nearly equal numbers (catastrophic cancellation).
- Use `Fraction` for exact rational arithmetic, or `Decimal` for decimal-fixed arithmetic.

## Practical Tips
- For money: use `Decimal` or store integer cents.
- For comparisons: prefer `math.isclose` with appropriate tolerances.
- Use `float.hex()` when debugging precision issues.
- When parsing user input, sanitize separators and locale differences before `float()` conversion.

## Advanced
- Inspect IEEE 754 bits via `struct.pack('>d', x)` and `int.from_bytes(...)`.
- Use `math.nextafter` to move to the next representable float value.
- `sys.float_info` gives machine limits: `max`, `min`, `epsilon`, `mant_dig`, etc.
- For heavy numeric workloads, use `numpy` (vectorized arrays) which uses C-backed arrays and avoids Python-loop overhead.
- For extreme-precision computations use `decimal` with a controlled context, or arbitrary-precision libraries like `mpmath` or `gmpy`.

## Examples (quick)
```py
0.1 + 0.2               # -> 0.30000000000000004 (floating point)
float.fromhex('0x1.999999999999ap-4')  # exact conversion using hex float
Decimal('0.1') + Decimal('0.2')       # precise decimal addition
math.isclose(1e-9, 0.0, rel_tol=1e-9, abs_tol=1e-12)
struct.pack('>d', 0.1)                # bytes representation
```

## Common Pitfalls
- Expect small rounding errors; do not compare floats with `==` unless exactness is guaranteed.
- Avoid constructing `Decimal` from a float (use string input instead).
- Beware of locale-specific decimal separators when parsing user input.

## References & Further Reading
- Python docs: Floating point arithmetic — https://docs.python.org/3/tutorial/floatingpoint.html
- IEEE 754 standard overview
- `decimal` and `fractions` module documentation
