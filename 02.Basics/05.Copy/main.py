# Identity, equality & mutability (foundation)
# == compares values
# is compares identity
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, same values
print(a is b)  # False, different objects
x = 10
y = 10
print(x == y)  # True,same values
print(x is y)  # Might be True

# check identity
print(id(a))  # different
print(id(b))  # different
print(id(x))  # same
print(id(y))  # same

nums = [1, 2, 3]
print(id(nums))
nums.append(5)
print(id(nums))  # same address, mutated in place


# assignment isn't a copy
n = [1, 2, 3]
m = n  # not copy,just another name
print(n == m)
print(n is m)
# same address
print(id(n))
print(id(m))

m.append(4)
print(n)  # 4 will be added to n, because it has same memory
