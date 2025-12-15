# for loops are used to iterate over strings,lists,sets,dicts,range()
# range() basics
# range(stop) 0 to stop-1
# range(start,stop) start to stop-1
# range(start,stop,step) start to stop-1 by skipping the step

print("With range() method")
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

print("With List")
# looping over list
fruits = ["banana", "apple", "grapes"]
for fruit in fruits:
    print(fruit)

# access values with index
for index, fruit in enumerate(fruits):
    print(index, fruit)

print("With String")
# looping over string
text = "Python"
for ch in text:
    print(ch)

for index, ch in enumerate(text):
    print(index, "=", ch)

print("With tuples")
std = ("Alen", 26, True)
for i in std:
    print(i)
for i, val in enumerate(std):
    print(i, val)

print("With Dict")
person = {"name": "Alen", "age": 26, "place": "Kannur"}
for key in person:
    print(key)  # this will print keys only

for i in person.values():
    print(i)  # this will print values only

for i in person:
    print(f"{i}={person[i]}")

for key, val in person.items():
    print(f"{key}:{val}")

print("With sets")
s = {10, 20, "alen", True}
for i in s:
    print(i)  # orders not guranteed

# in other way

# # excercise
# for i in range(1, 11):
#     print(i * i)
#
# nums = [2, 5, 8, 10]
# for num in nums:
#     print(num * 3)
#
# # break, continue and pass
# # break, exits the loop when condition met
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)
#
# # continue, skips the current iteration and moves to the next one
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
#
# # pass , do nothing
# for i in range(1, 11):
#     pass  # do nothing
#
#
# # else with loops
# target = 25
# for i in range(1, 30, 3):
#     if i == target:
#         print("Found")
#         break
#     else:
#         print("Not Found")
#     print(i)
#
#
# # tasks
#
# for i in range(1, 6):
#     user_input = int(input("Enter a number between 1 to 5: "))
#
#     check = 1 <= user_input <= 5
#
#     if check:
#         print("Thankyou!!")
#         break
# else:
#     print("You tried 5 times! Exiting.")
#
#
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)
