# dict.py - Practical examples for dictionaries

# Creating dict
student = {"name":"Alen","age":21}
print("student:", student)

# Accessing
print("name:", student["name"])
print("get:", student.get("age"))

# Add/update
student["course"] = "Python"
print("after add:", student)

# Keys, values, items
print("keys:", list(student.keys()))
print("values:", list(student.values()))
print("items:", list(student.items()))

# Iteration
for k, v in student.items():
    print(k, "->", v)

# dict from list of tuples
print("dict([('a',1),('b',2)]):", dict([('a',1),('b',2)]))
