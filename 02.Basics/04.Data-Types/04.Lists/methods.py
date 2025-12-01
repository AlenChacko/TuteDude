# append()
# adds at the end
names = ["Alen", "Chethas", "Shaikh"]
print(names)
names.append("Arjun")
print(names)

# insert()
# add at index
names.insert(1, "Binil")
print(names)

# extend()
# adds multiple items
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# remove()
# remove by value
names.remove("Chethas")
print(names)

# pop()
# remove by index
names.pop(2)
print(names)

# sort()
# sort in ascending
nums = [75, 66, 22, 86, 12, 54, 22, 23, 87, 56, 34, 22, ]
nums.sort()
names.sort()
print(names)
print(nums)

# reverse()
#  reverse a list
names.reverse()
nums.reverse()
print(nums)
print(names)

# count()
# count the occurance
print(nums.count(22))
print(names.count("Binil"))

# clear()
# empty list
names.clear()
print(names)
