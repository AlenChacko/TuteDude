class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Eligible")
except ValueError:
    print("Please enter a valid number")
except InvalidAgeError as e:
    print(e)
