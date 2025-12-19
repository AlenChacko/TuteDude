# default parameters
def say_hello(name="Guest"):
    print(f"Hello, {name}")


say_hello("Alen")


def calculate(a, b, c=10):
    print(f"a:{a},b:{b},c:{c}")
    return a + b + c


result = calculate(1, 2)
print(result)


# keyword arguments
def student(name, age):
    print(f"Name:{name},age:{age}")


student(age=26, name="Alen")  # order doesn't matter


# positional arguments
def show_data(name, age, place, job):
    print(f"Name:{name},Age:{age},Place:{place},Job:{job}")  # positional, order matters


show_data("Alen", 26, "Cherupuzha", "Developer")


# Variable length arguments
def unknown(*nums):
    print(type(nums))
    return sum(nums)


res = unknown(1, 2, 3, 4, 5)
print(res)


# kwargs(Keyword Arguments)
def data(**info):
    print(info, type(info))


data(name="Alen", age=26, place="Cherupuzha")
