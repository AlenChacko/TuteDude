# Primitive -->
# 1.interger
b = -5
c = 0
a = 10
print(a, b, c)
print(type(a))

# 2.float
x = 3.14
y = 0.0
z = -10.55
print(x, y, z)
print(type(x))

# 3.complex
c1 = 3 + 4j
c2 = 5 - 2j
print(c1)
print(c1.real)
print(c1.imag)

# 4.bool
is_logged_in = True
is_raining = False
print(is_logged_in, is_raining)
print(10 > 5)     # True
print(3 == 10)    # False

# 5.str
name = "Alen"
message = 'Hello Python'
line = """This is a 
multiline string"""
print(name)
print(line)

# 6.NoneType
x = None
print(x)
print(type(x))



# Non-Primitive
# 1.list
fruits = ["apple", "banana", "mango"]
print(fruits)
fruits.append("orange")
print(fruits)

# 2.tuple
numbers = (10, 20, 30)
print(numbers)
print(numbers[1])   # accessing element

# 3.set
s = {10, 20, 30, 20}
print(s)   # duplicates removed
s.add(40)
print(s)

# 4.dict
student = {
    "name": "Alen",
    "age": 21,
    "course": "Python"
}
print(student)
print(student["name"])

# 5.range
r = range(0, 5)
print(list(r))   # convert to list to see the values


# DYNAMIC TYPING
x = 10
print(type(x))
x = "Hello"
print(type(x))
x = 3.5
print(type(x))

# CHECK DATATYPE
print(type(100))
print(type("Python"))
print(type([1, 2, 3]))

# TYPE CONVERSION
a = 10
print(float(a))
b = 10.9
print(int(b))
num = "50"
print(int(num))
text = "hello"
print(list(text))
lst = [1, 2, 2, 3]
print(set(lst))


# Mutable vs Immutable Behavior
# str,int immutable
x = 10
print(id(x))
x = 20
print(id(x))  # id changes (new object)

# mutable
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))  # same id, modified

