# 1. Function Polymorphism
# eg: built-in functions
# the len() function has different behavior
print(len("Python"))  # string length
print(len((1, 2, 3)))  # tuple length
print(len([1, 2, 34, 5, 6]))  # list length

# 2. Operator Polymorphysm
# + operator
print(10 + 20)  # arithmetic addition
print("Alen" + " " + "Chacko")  # string concatenation


# 3. Method Overriding (Basic runtime polumorphysm)
class Animal:
    def speak(self):
        print("All Animals make a sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")


class Cat(Animal):
    def speak(self):
        print("Cat meows")


print("Runtime Polymorphysm")
# method decided at runtime
animals = [Cat(), Dog(), Animal()]
for animal in animals:
    animal.speak()


# 4. Polymorphism Using a Common Interface
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        return 10 * 5


class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5


shapes = [Rectangle(), Circle()]

# same method area() defferent implimentation
for shape in shapes:
    print(shape.area())


# 5. function accepts any objects as long as they have area()
def calculate_area(shape):
    print(shape.area())


calculate_area(Rectangle())


# 6. Duck Typing
# No inheritance


class Car:
    def start(self):
        print("Car started")


class Bike:
    def start(self):
        print("Bike started")


def start_vehicle(bike):
    bike.start()


start_vehicle(Bike())


# 7. Operator overloading
class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages


book1 = Book(100)
book2 = Book(200)
print(book1 + book2)


# 8. Method Overriding with super()
class Employee:
    def salary(self):
        print("Base salary")


class Developer(Employee):
    def salary(self):
        super().salary()
        print("Developer bonus added")


dev = Developer()
dev.salary()


# Polymorphism in Real Vehicle Rental System Style
class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid rupees {amount}, using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print(f"Paid rupees {amount}, via UPI")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paid rupees {amount}, through Cash")


payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay(1000)

# Polymorphism with Abstract Base Classes
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")


class Bike(Vehicle):
    def start(self):
        print("Bike started")


vehicles = [Car(), Bike()]

for v in vehicles:
    v.start()
