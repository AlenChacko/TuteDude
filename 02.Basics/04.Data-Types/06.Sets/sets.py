# Creating a set

# using curly braces
fruits = {"apple", "banana", "orange"}
print(fruits)  # order may different

# using set()
nums = set([1, 2, 3, 4])
print(type(nums))
print(nums)

# empty set
empty_set = ()  # this is the right way
# empty_set={}

# no duplicates
names = {"Alen", "Amal", "Chethas", "Alen", "Binil", "Chethas"}
numbers = {1, 2, 3, 41, 2, 3, 1, 44, 56, 2}
print(names)
print(numbers)

# looping
for name in names:
    print(name)

# membership
print("Alen" in names)
print("Arjun" in names)

# length
print(len(names))

# sets are mutable but ,
new_set = {1, 2, 3, 4}
new_set.add(-5)
print(new_set)
fs = frozenset(["a", "b", "c", "d"])
# fs.add("e") Error
