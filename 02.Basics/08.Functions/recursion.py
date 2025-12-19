"""
It is a technique that a function calles itself to solve a problem
It breaks the problem into smaller subproblems of the same type

Every recursive function has:
BASE CASE: condition where recursion stops
RECURSIVE CASE: function calls itself

Basic Syntax:

def function_name(parameters):
    if base_condition:
        return result
    else:
        return function_name(smaller_input)

"""


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)


countdown(5)


# factorial of a number
# without recursion
def fact(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n - 1
    return factorial


print(fact(5))


# With recursion
def recursive_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_fact(n - 1)


print(recursive_fact(10))


# recursion vs loop
def fact_loop(n):
    res = 1
    for i in range(1, n + 1):
        if n == 0 or n == 1:
            return 1
        else:
            res = res * i
    return res


print(fact_loop(5))


# sum of n numbers using recursion
def sum_of_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)


print(sum_of_numbers(5))
