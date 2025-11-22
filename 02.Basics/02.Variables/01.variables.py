# creating and printing variables
name = "Alen"
age = 21
country = "India"

print(name)
print(age)
print(country)


# Changing the Value of a Variable
x = 10
print(x)

x = 20
print(x)

# Variables with Different Types of Values
a = 10
b = 5.5
c = "Python"
d = True

print(a, b, c, d)


# Multiple Assignment (One Line)
a, b, c = 1, 2, 3
print(a, b, c)


# Same Value to Multiple Variables
x = y = z = 100
print(x, y, z)


# Variables are Case-Sensitive
a = 10
A = 20

print(a)
print(A)


# Checking the Memory Address
x = 100
y = 100

print(id(x))
print(id(y))   # same memory (optimised)

# Dynamic Typing Example
x = 10
print(x)

x = "Hello"
print(x)

x = 3.14
print(x)


# Swapping Variables
x = 5
y = 10

x, y = y, x
print(x, y)


# Deleting a Variable
x = 50
print(x)

del x
# print(x)   # This will cause an error: NameError: x is not defined
