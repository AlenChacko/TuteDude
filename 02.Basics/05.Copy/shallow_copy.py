import copy

# It creates a new container object, but doesn't clone the inner object, it just copies the reference
l1 = [1, 2, 3, [4, 5, 6], "Python"]
l2 = l1.copy()
print(id(l1))  # different
print(id(l2))  # different
l2.append("Java")
print(l1)
print(l2)

l1[0] = "First"
print(l1)
print(l2)

# this will change in the both the objects, because it not clone the inner objects
l1[3][1] = 10
print(l1)
print(l2)
