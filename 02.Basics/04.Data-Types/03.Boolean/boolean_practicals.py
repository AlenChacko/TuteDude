
"""
boolean_practicals.py
Comprehensive practical examples for the Python `bool` type.
Covers: creation, truthiness, conversions, logical operators, short-circuit behavior,
custom boolean behavior, using booleans in arithmetic, practical recipes, and common pitfalls.
Run this file with: python boolean_practicals.py
"""

from typing import Any

# ---------- Basics ----------
a = True
b = False
print("Basics:")
print("a, b ->", a, b)
print("type(a) ->", type(a))
print("isinstance(True, bool) ->", isinstance(True, bool))
print("issubclass(bool, int) ->", issubclass(bool, int))
print("True + True ->", True + True)  # bool is subclass of int (True==1, False==0)
print("False * 10 ->", False * 10)

# ---------- Truthiness (truth value testing) ----------
print("\\nTruthiness:")
values = [0, 1, "", "text", [], [1], {}, {"k": "v"}, None, 0.0, 0.0001, (), (1,), set(), {1}]
for v in values:
    print(repr(v).ljust(12), "-> bool() =", bool(v))

# ---------- Conversions ----------
print("\\nConversions to bool:")
print("bool(0) ->", bool(0))
print("bool(42) ->", bool(42))
print("bool('') ->", bool(''))
print("bool('False') ->", bool('False'))
print("bool(None) ->", bool(None))

# ---------- Logical operators & short-circuit ----------
print("\\nLogical operators & short-circuiting:")
def f_true():
    print("f_true called")
    return True

def f_false():
    print("f_false called")
    return False

print("True and False ->", True and False)
print("True or False ->", True or False)
print("not True ->", not True)
print("Short-circuit AND (f_false() and f_true()):")
print(f_false() and f_true())   # f_true not called due to short-circuit
print("Short-circuit OR (f_true() or f_false()):")
print(f_true() or f_false())    # f_false not called due to short-circuit

# Return value of logical operators (not strictly bool)
print("Return value of 'and' with non-bools:", "'' and 'x' ->", '' and 'x')
print("Return value of 'or' with non-bools:", "'' or 'x' ->", '' or 'x')

# ---------- Comparisons & chaining ----------
print("\\nComparisons & chaining:")
print("3 < 4 ->", 3 < 4)
print("3 < 4 < 5 ->", 3 < 4 < 5)  # chaining comparisons
print("'a' == 'a' ->", 'a' == 'a')
print("'a' is 'a' ->", 'a' is 'a')  # identity vs equality (small strings interned)

# ---------- Using booleans in control flow ----------
print("\\nControl flow examples:")
x = 0
if x:
    print("x is truthy")
else:
    print("x is falsy")

# Ternary / conditional expression
y = "yes" if x else "no"
print("Ternary result ->", y)

# ---------- Custom truthiness (objects) ----------
print("\\nCustom truthiness:")
class AlwaysFalse:
    def __bool__(self):
        return False

class LenBased:
    def __len__(self):
        return 0

af = AlwaysFalse()
lb = LenBased()
print("bool(AlwaysFalse()) ->", bool(af))
print("bool(LenBased()) ->", bool(lb))

# ---------- Practical examples / small programs ----------
print("\\nPracticals:")

# 1) Predicate filter example: filter even numbers
nums = list(range(10))
evens = list(filter(lambda n: n % 2 == 0, nums))
print("Evens via filter:", evens)

# 2) any/all example for validation
passwords = ["secret", "", "pass123"]
print("any empty password ->", any(p == "" for p in passwords))
print("all non-empty ->", all(p != "" for p in passwords))

# 3) Using booleans as flags in loops
found = False
for i in range(5):
    if i == 3:
        found = True
        break
print("found flag ->", found)

# 4) Using boolean masks with lists (select elements)
mask = [True, False, True, False]
items = ['a', 'b', 'c', 'd']
selected = [it for it, m in zip(items, mask) if m]
print("Selected via mask:", selected)

# 5) Counting True values efficiently
trues = [True, False, True, True]
print("sum(trues) ->", sum(trues), " (treats True as 1)")

# 6) Using booleans for configuration toggles
DEBUG = False
if DEBUG and (1 / 0):  # will not evaluate division because DEBUG is False (short-circuit)
    print("debugging")

# ---------- Pitfalls & gotchas ----------
print("\\nPitfalls & gotchas:")
print("1) bool('False') is True -- strings are truthy unless empty.")
print("2) 'is' compares identity, not equality. Use '==' for equality checks.")
print("3) Be careful when overriding __len__ or __bool__ in your classes.")

# ---------- Performance & memory notes ----------
print("\\nPerformance & memory:")
print("Booleans are singletons (True/False). They are instances of bool, which is a subclass of int.")
print("Using sum(bool_list) is a fast way to count truthy values in Python.")

# ---------- Useful builtins ----------
print("\\nUseful builtins:")
print("all([True, True]) ->", all([True, True]))
print("any([False, False, True]) ->", any([False, False, True]))
print("bool('0') ->", bool('0'))

# ---------- Advanced / Niche ----------
print("\\nAdvanced:")

# 1) Custom objects with truthiness based on state
class Container:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)

c1 = Container([])
c2 = Container([1,2])
print("bool(Container([])) ->", bool(c1))
print("bool(Container([1,2])) ->", bool(c2))

# 2) Using boolean arrays/masks with numpy (commented out, shown as recipe)
# import numpy as np
# arr = np.array([1,2,3,4])
# mask = arr % 2 == 0
# print(arr[mask])  # selects even elements

# 3) Efficient predicate composition using functions
def negate(pred):
    return lambda *args, **kwargs: not pred(*args, **kwargs)

is_even = lambda x: x % 2 == 0
is_odd = negate(is_even)
print("is_odd(3) ->", is_odd(3))

# End of practical examples
if __name__ == '__main__':
    print("\\nRan boolean_practicals.py - examples above demonstrate bool usage.")
