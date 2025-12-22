def check_age(a):
    if a == 0:
        raise ValueError("0 cannot be an age")
    elif a < 0:
        raise ValueError("Age cannot be negative")
    elif a < 18:
        print(f"You are not an adult. Wait {18 - a} years to become an adult")
    else:
        print("Congrats, You can make your vote!!!")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)


try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as err:
    print("Error:", e)
