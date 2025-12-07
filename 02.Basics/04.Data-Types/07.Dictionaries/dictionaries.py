# Creating dict

# empty dict
dummy = {}
# using {}
user = {"name": "Alen", "age": 26, "place": "Cherupuzha", "isActive": True}
print(user)
print(type(user))
# using dict() constructor
person = dict(name="Alen", age=26, place="Cherupuzha", isActive=True)
# From List,tuple pairs
pairs = [("name", "Alex"), ("city", "Kochi")]
person_2 = dict(pairs)
print(person_2)
# using zip()
keys = ["brand", "model", "price"]
values = ["Kia", "Seltos", 1899999]
car = dict(zip(keys, values))
print(car)


student = {"name": "Chethas", "age": 22, "place": "Mattannur"}
# accessing dict elements
print(student["name"])
print(student["age"])
# print(student["phone"]) key error

# safe access
print(student.get("name"))
print(student.get("phone"))
print(student.get("marks", "Not Provided"))

# check key exists
print("name" in student)
print("city" in student)
print("city" not in student)


# iterating
# to print keys
user = {"name": "Alen", "age": 23, "city": "Kochi"}
for key in user:
    print(key)

# to print values
for value in user.values():
    print(value)

# to print key and value together:
for key in user:
    for value in user.values():
        print(f"{key} = {value}")

# or
for key, value in user.items():
    print(f"{key} = {value}")
