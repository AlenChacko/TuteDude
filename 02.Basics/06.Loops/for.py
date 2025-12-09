# for loops are used to iterate over strings,lists,sets,dicts,range()
# range() basics
# range(stop) 0 to stop-1
# range(start,stop) start to stop-1
# range(start,stop,step) start to stop-1 by skipping the step
for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)


# looping over list
fruits = ["banana", "apple", "grapes"]
for fruit in fruits:
    print(fruit)

# looping over string
text = "Python"
for ch in text:
    print(ch)

# excercise
for i in range(1, 11):
    print(i * i)

nums = [2, 5, 8, 10]
for num in nums:
    print(num * 3)

# break, continue and pass
# break, exits the loop when condition met
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# continue, skips the current iteration and moves to the next one
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# pass , do nothing
for i in range(1, 11):
    pass  # do nothing


# else with loops
target = 25
for i in range(1, 30, 3):
    if i == target:
        print("Found")
        break
    else:
        print("Not Found")
    print(i)


# tasks

for i in range(1, 6):
    user_input = int(input("Enter a number between 1 to 5: "))

    check = 1 <= user_input <= 5

    if check:
        print("Thankyou!!")
        break
else:
    print("You tried 5 times! Exiting.")


for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
