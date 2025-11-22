# list.py - Practical examples for lists

# Creating lists
fruits = ["apple", "banana", "mango"]
print("fruits:", fruits)

# Accessing and slicing
print("fruits[0]:", fruits[0])
print("fruits[1:]:", fruits[1:])

# Modifying lists (mutable)
fruits.append("orange")
print("after append:", fruits)
fruits.insert(1, "kiwi")
print("after insert:", fruits)
fruits.remove("banana")
print("after remove:", fruits)
popped = fruits.pop()
print("popped:", popped, "fruits now:", fruits)

# List comprehension
squares = [x*x for x in range(6)]
print("squares:", squares)

# Nested lists
matrix = [[1,2,3],[4,5,6]]
print("matrix:", matrix)
print("matrix[1][2]:", matrix[1][2])

# Converting from other types
print("list('abc'):", list('abc'))
print("list((1,2,3)):", list((1,2,3)))
print("list({1,2,3}):", list({1,2,3}))
