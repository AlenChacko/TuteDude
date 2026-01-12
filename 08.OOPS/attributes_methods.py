# class variables, shared with all objects
class Company:
    name = "Brototype"
    pass


cmp_1 = Company()
cmp_2 = Company()
print(f"Company 1:{cmp_1.name}")
print(f"Company 2:{cmp_2.name}")


# instance variables, shared with each object
class Car:
    pass


car_1 = Car()
car_1.brand = "Kia"
car_1.model = "Seltos"
print(f"Printing Car 1:{car_1.brand},{car_1.model}")


# instance methods, defined in class and shared with all objects,self->current object as first paramter
class Student:
    def goal(self):
        print("The goal of a student is to study")


std_1 = Student()
std_1.goal()
std_2 = Student()
std_2.goal()


# passing arguments to instance methods
class Laptop:
    def show_device(self, brand, model):
        print(f"Brand:{brand}\nModel:{model}")


lp_1 = Laptop()
lp_1.show_device("DELL", "Latitude")
lp_2 = Laptop()
lp_2.show_device("LENOVO", "Thinkpad")


# class methods
# works with class level data, uses @classmethod decorator, first parameter is cls, doesn't depend on objects
class Collage:
    collage_name = "Vimal Jyothi"

    @classmethod
    def change_collage_name(cls):
        cls.collage_name = "Amal Jyothi"

    def show_collage(self):
        print(self.collage_name)


col = Collage()
col.show_collage()
col.change_collage_name()
col.show_collage()


# static methods
# Doesn't depend on class or object
# Uses decorator @staticmethod
# Doesn't take by default paramters like self, cls
# used for utilities


class Maths:
    @staticmethod
    def add(a, b):
        return a + b


mts = Maths()
res = mts.add(10, 20)
print(res)
