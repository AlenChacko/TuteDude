# none.py - Practical examples for None (NoneType)

# None as a placeholder
x = None
print("x:", x)
print("type(x):", type(x))

# Functions returning None
def no_return():
    a = 5  # no explicit return

def explicit_none():
    return None

print("no_return():", no_return())
print("explicit_none():", explicit_none())

# None in conditionals
value = None
if value is None:
    print("value is None (use 'is' for identity checks)")
else:
    print("value has something")
