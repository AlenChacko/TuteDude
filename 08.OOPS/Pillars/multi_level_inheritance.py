class Person:
    def show_identity(self):
        print("I am a person")


class Employee(Person):
    def show_role(self):
        print("I am an employee")


class Manager(Employee):
    def show_position(self):
        print("I am a manager")


m = Manager()

m.show_identity()
m.show_role()
m.show_position()
