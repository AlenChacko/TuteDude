# Basic syntax

# This throw an error that ZeroDivisionError
# print(10 / 0)

# fixing it
try:
    print(10 / 0)
except ZeroDivisionError as err:
    print(f"Error:{err}")

try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError as err:
    print(f"Error:{err}")


# multiple except block
try:
    num = int(input("Enter another number: "))
    print(10 / num)
except ValueError as err:
    print(f"Error:{err}")
except ZeroDivisionError as err:
    print(f"Error:{err}")


# multiple exception in one except

try:
    num = int(input("Again, enter a new number: "))
    print(10 / num)
except ValueError, ZeroDivisionError:
    print(f"Error: Invalid input or entered 0")


# else block
try:
    num = int(input("Enter next number: "))
    print(10 / num)
except ValueError as err:
    print(f"Error:{err}")
except ZeroDivisionError as err:
    print(f"Error:{err}")
else:
    print("Completed")
