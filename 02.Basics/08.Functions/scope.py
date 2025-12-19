"""
Variable scope means where the variables can be accessed in the code
LOCAL: a variable created inside a function is local scope, it cannot access outside the function
GLOBAL:a variable created outside a function is global, it can be access inside the functions
"""

from itertools import count


# Local scope
def show():
    x = 10
    print(x)


show()
# print(x) Error, name error x isn't defined


# Global scope
name = "Alen"


def show_2():
    print(name)


show_2()
print(name)


# local vs global same name

company = "Samsung"


def show_3():
    company = "Motorola"
    print(f"Inside:{company}")


show_3()
print(f"Outside:{company}")


# global keyword
"""
If you modify a global variable inside a function, python assumes it is local,
global keyword allows to modify global variables inside functions
"""

counter = 0


# def increment():
#     counter += 1
# increment()

print(f"Counter Before:{counter}")


def increment():
    global counter
    counter += 1


increment()
print(f"Counter After:{counter}")


# Enclosing scope
def outer():
    x = 10

    def inner():
        print(f"X from inner:{x}")

    inner()


# x is not local to inner, but still accessible
outer()


# problem with non local
def outer_one():
    y = 100

    def inner_one():
        nonlocal y
        y = y + 1
        print(f"Y from inner : {y}")

    inner_one()


outer_one()


# LEGB -> Local Enclosed Global Built-in
x = "global"


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()


outer()
