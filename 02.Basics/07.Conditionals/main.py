# Conditionals allows to make decisions based on True/False expressions

# if
age = 18
if age >= 18:
    print("You are an adult")


# if-else
user_age = int(input("Enter age: "))
if user_age >= 18:
    print("You can vote")
else:
    print(f"You need to wait {18-user_age} years")

# if-elif-else
num = 1
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")


# nested
number = 0
if number > 0:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

else:
    print("Not a valid number")
