# INDEXING
# +ve indexing
fruits = ['apple', 'banana', 'orange']
print(fruits[0])
print(fruits[1])

# -ve indexing
print(fruits[-1])
print(fruits[-2])

# SLICING
# list[start:end:step]
nums = [23, 54, 65, 23, 75, 89, 23, 65, 76, 33, 23]
print(len(nums))
print(nums[2:8:1])
print(nums[2:8:2])

# concatenation
lst_1 = [1, 2, 3, 4, 5]
lst_2 = ["alen", "malan", "kulan"]
lst_3 = lst_1 + lst_2
print(lst_3)

# repetition
colors = ["red", "green", "blue"]
print((colors * 3))

# changing list items
cars = ["seltos", "crysta", "creta"]
print(cars)
cars[1] = "Hycross"
print(cars)
cars[2] = "brezza"
print(cars)
# cars[20]="hector" fails

# looping through lists
# for loop
for fruit in fruits:
    print(fruit)

# using index
for fruit in range(len(fruits)):
    print(fruit, fruits[fruit])

# while

i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
