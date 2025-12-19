# map() applies a function to every element in an iterable

# without lambda
numbers = [1, 2, 3, 4]


def square(n):
    return n * n


result = map(square, numbers)
print(list(result))

# with lambda
nums = [2, 4, 6, 8]
result_2 = map(lambda x: x * x, nums)
print(list(result_2))


# map with multiple iterables
seq_1 = [1, 2, 3]
seq_2 = [9, 8, 7]
result_3 = map(lambda x, y: x + y, seq_1, seq_2)
print(list(result_3))


# filter() selects elements based on conditions
seq_3 = [23, 65, 78, 34, 55, 79, 34, 27, 88, 54, 73]


# without lambda
def is_even(n):
    return n % 2 == 0


result_4 = filter(is_even, seq_3)
print(list(result_4))


# with lambda
result_5 = filter(lambda x: x % 2 == 0, seq_3)
print(list(result_5))

# filtering strings
names = ["Alen", "Charu", "Chethas", "Arjun", "Abin", "Shaikh"]
res = filter(lambda name: name.startswith("A"), names)
print(list(res))


# reduce() reduces multiple values into one value
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)
print(result)
