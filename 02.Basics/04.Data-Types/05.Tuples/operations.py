# accessing tuple elments
colors = ("Red", "Green", "Blue")
print(colors[0])
print(colors[1])
print(colors[-1])

# slicing
nums = (10, 20, 30, 40, 50)
print(nums[1:3])
x = (1, 2, 3, 4, 5, 6)
print(x[2:5])

# concatenations
odd = (1, 3, 5, 7, 9)
even = (2, 4, 6, 8)
final = odd + even
print(final)

# repetetion
msg = ("hi",)
print(msg * 3)
hobbies = ("reading", "dancing", "cooking")
print(hobbies * 3)

cars = ("seltos", "creta", "fronx", "city", "virtus")
# length
print(len(cars))
# iterations
for car in cars:
    print(car)
# membership
print("virtus" in cars)
print("city" not in cars)
print("harrier" in cars)
print("ignis" not in cars)

numbers = (23, 45, 21, 45, 64, 34, 87, 44, 99, 67, 32)
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

mixed = (1, 2, "Alen", 32, 56, False, "Cherupuzha")
print(len(mixed))
# print(sum(mixed)) Type Error
# print(min(mixed)) Type Error
# print(max(mixed)) Type Error

# Immutability
# mixed[0] = "Amal" Doesn't support assignment
new = mixed + ("Alen",)
print(new)

# type changing
lst = [10, "Alen", True, 4.54]
print(type(lst))
new_lst = tuple(lst)
print(type(new_lst))

# tuple packing and unpacking
# packing
my_tuple = 1, 2, 3, 4, 5
# unpacking
a, b, c, d, e = my_tuple
print(e)
# extended unpacking
p, *q = my_tuple
print(p)
print(q)
print(type(q))

# nested tuples
nested_tuple = (1, 2, 3, (12, 14, 16), 4, 5, 6, (18, 20, 22, (7, 5, 3, 1)), 7, 8, 9)
print(nested_tuple)
# accessing nested tuple
print(nested_tuple[3])
print(nested_tuple[7])
print(nested_tuple[7][3])
