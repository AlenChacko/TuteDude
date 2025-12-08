# It recursively copies the container and its inner objects and inside those objects, it will be a
# tree of independent objects
import copy

original = [1, 2, [3, 4], 5, 6, [7, 8], 9]
deep = copy.deepcopy(original)
print(original is deep)
print(original[0] is deep[0])
print(original[2][0] is deep[2][0])

original[0] = 10
print(original is deep)
print(original[0] is deep[0])
print(original[2][0] is deep[2][0])
original[2][0] = "True"
print(original is deep)
print(original[0] is deep[0])
print(original[2][0] is deep[2][0])
print(original)
print(deep)
