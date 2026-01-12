# Combination of 2 or more types inheritance


class Person:
    def speak(self):
        print("Person can speak")


class Employee(Person):
    def work(self):
        print("Employee works")


class Manager(Person):
    def manage(self):
        print("Manager manages team")


class TeamLead(Employee, Manager):
    def lead(self):
        print("TeamLead leads the team")


tl = TeamLead()

tl.speak()  # Person
tl.work()  # Employee
tl.manage()  # Manager
tl.lead()  # TeamLead
