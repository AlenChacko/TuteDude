# bool.py - Practical examples for booleans

# Basic booleans
t = True
f = False
print("t, f:", t, f)

# Boolean operations
print("and:", True and False)
print("or:", True or False)
print("not:", not True)

# Booleans in comparisons
print("10 > 5:", 10 > 5)
print("5 == 5:", 5 == 5)

# Booleans as ints
print("True + 5:", True + 5)
print("False + 10:", False + 10)
print("int(True):", int(True), "int(False):", int(False))
print("bool(0):", bool(0), "bool(1):", bool(1), "bool(''):", bool(''))

# Using booleans in if
if True:
    print("This runs because condition is True")
