def division(num1, num2):
    """
    num1 is the number to be divided(Numberator)
    num2 is the number that divides num1(Denominator)
    :return: float
    """
    result = num1 / num2
    return result


ans = division(100, 20)
print(ans)

print(division.__doc__)
