a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union -> All unique elements from both sets
# operator |
# method .union()
print(a | b)
print(a.union(b))

# Intersection ->Elements common in both sets
# operator &
# method .intersection()
print(a & b)
print(a.intersection(b))

# Difference ->Elements in one, but not in other
# operator -
# method .difference()
print(a - b)
print(a.difference(b))

# Symmetric difference -> Non-common elements in a or b
# operator ^
# method .symmetric_difference()
print(a ^ b)
print(a.symmetric_difference(b))
