# IndexError
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index out of range")

# KeyError
try:
    data = {"name": "Alen"}
    print(data["age"])
except KeyError:
    print("Key not found")

# TypeError
try:
    print(10 + "5")
except TypeError:
    print("Type mismatch")


# NameError
try:
    print(x)
except NameError:
    print("Variable not defined")
