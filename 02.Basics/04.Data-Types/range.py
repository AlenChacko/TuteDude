# range.py - Practical examples for range

# Basic range
r = range(5)
print("list(r):", list(r))

# start, stop, step
r2 = range(2, 10, 2)
print("list(r2):", list(r2))

# iterate using range
for i in range(3):
    print("iter:", i)

# using range with len
arr = ['a','b','c']
for i in range(len(arr)):
    print(i, arr[i])
