# 1.Numeric literals

# Intergers
a = 10
b = -50
c = 0
print(a, b, c)
# float
x = 3.14
y = -0.67
z = 10.0
print(x, y, z)
# complex
comp = 3 + 4j
print(comp)
print(comp.real)   # real part
print(comp.imag)   # imaginary part

# 2. String Literals
name1 = 'Alen'
name2 = "Chacko"
print(name1, name2)
text = """This is
a multi-line
string literal."""
print(text)


# 3. Boolean Literals
a = True
b = False
print(a, b)
print(10 > 5)     # True
print(5 == 2)     # False


# 4. Special Literal – None
x = None
print(x)

def test():
    return None

print(test())


# 5. Collection Literals

# list
cars = ["Tata", "Hyundai", "Kia"]
print(cars)
# tuple
numbers = (1, 2, 3)
print(numbers)
# set
s = {10, 20, 30}
print(s)
# dict
student = {
    "name": "Alen",
    "age": 22,
    "course": "Python"
}
print(student)


# 6. Boolean from comparison
print(10 == 10)
print(15 < 3)
print(True + 5)     # True behaves like 1
print(False + 10)   # False behaves like 0


