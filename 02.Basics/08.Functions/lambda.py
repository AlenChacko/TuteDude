"""
it is an annonymous function without a name
lambda arguments: expression

"""


def add_nums(a, b):
    return a + b


print(add_nums(10, 20))


# same with lambda
addition = lambda a, b: a + b
print(addition(20, 30))


# without arguments
greet = lambda: "Hello Alen"
print(greet())

# with one argument
square = lambda x: x * x
print(square(5))
