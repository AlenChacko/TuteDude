# Creating a class
class Test:
    pass


# Creating an object
tst = Test()

# Attribtes and methods


class Student:
    # Class Attributes -> variables inside class, shared by all objects
    name = "Rahul"
    age = 18


# creating object and calling methods
std1 = Student()
std2 = Student()
print(std1.name)
print(std2.name)
print(type(std1))

# Creating instance attributes, unique to each object
std1.roll_no = 1001
print(std1.roll_no)  # prints
print(std1.__dict__)
# print(std2.roll_no) # AttributeError


# Instance methods
class Car:
    def show_car(self):
        print("This functions shows the car")


car1 = Car()
car1.show_car()
car2 = Car()
car2.show_car()


# arguments in instance methods
class Laptop:
    def show_laptop(self, brand, model):
        print(f"This show the laptop:{brand,model}")

    def show_specs(self, ram, rom):
        print(f"This shows the spces:{ram},{rom}")


lp_1 = Laptop()
lp_1.show_laptop("DELL", "Latitude")
lp_2 = Laptop()
lp_2.show_laptop("HP", "Pavilion")
lp_1.show_specs(8, 512)
