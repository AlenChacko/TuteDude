def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculations(fun1, a, b, fun2, c, d):
    return fun1(a, b), fun2(c, d)


result = calculations(addition, 10, 20, subtraction, 30, 15)
print(result)
