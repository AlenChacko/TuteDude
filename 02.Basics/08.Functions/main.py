# A function is a block of reusable code that performs a specific task

# Built-in functions
print("Hello World")
len([1, 2, 3, 4])
type(10)
# input("Enter something: ")


# user defined fucntions
def greet():
    print("hello")


greet()


# functions with parameter
def message(name):
    print(f"Hello, {name}")


message("Alen")


# multiple parameters
def add(a, b):
    print(a + b)


add(10, 20)


# returning values
def odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = odd_even(11)
print(result)


# multiple returns
def mathematics(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    return addition, subtraction, multiplication, division


ans = mathematics(20, 5)
print(ans)
ans_1, ans_2, ans_3, ans4 = mathematics(70, 25)
print(f"Addition={ans_1}\nSubtraction={ans_2}\nMultiplication={ans_3}\nDivision={ans4}")
