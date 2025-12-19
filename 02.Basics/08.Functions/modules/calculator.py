def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    if num1 == 0 or num2 == 0:
        return "Division with 0 is not possible"
    else:
        return num1 / num2


# __name__ , __main__


if __name__ == "__main__":
    a = 10
    b = 20
    res = addition(a, b)
    print(f"From calculator module:{res}")


print(f"__name__ in calculator:{__name__}")
