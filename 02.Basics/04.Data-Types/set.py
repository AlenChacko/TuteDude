# set.py - Practical examples for sets

# Creating sets
s = {1, 2, 3, 2}
print("s (duplicates removed):", s)

# Add, remove
s.add(4)
print("after add:", s)
s.discard(2)
print("after discard:", s)

# Membership and operations
print("3 in s:", 3 in s)
t = {3,4,5}
print("union:", s | t)
print("intersection:", s & t)
print("difference:", s - t)

# set from string
print("set('hello'):", set('hello'))
