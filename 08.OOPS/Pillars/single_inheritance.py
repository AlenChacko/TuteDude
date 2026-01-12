# Single Inheritance


# parent class
class Person:
    def __init__(self, name, age):
        # common attributes for all person
        self.name = name
        self.age = age
        print("Parent constructor")

    def introduce(self):
        # common behavior
        print(f"My name is {self.name} and  I am {self.age} years old")


class Student(Person):
    def study(self):
        print(f"{self.name} is studying")


st1 = Student("Alen", 26)
st1.introduce()


# using child constructor


class Employee(Person):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}\nRole:{self.role}")


emp1 = Employee("Arjun", 34, "Technition")
emp1.display()


# method overriding
# same method name, child replaces parent logic


class Workers:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def introduction(self):
        print(f"I am a Worker\nName:{self.name}\nCompany:{self.company}")


class Manager(Workers):
    def __init__(self, name, company, experience):
        super().__init__(name, company)
        self.experience = experience

    def introduction(self):
        print(
            f"I am a Manager\nName:{self.name}\nCompany:{self.company}\nExperience:{self.experience} Years"
        )


# wr = Workers("Chethas", "IBM")
mr = Manager("Alen", "TCS", 6)
# wr.introduction()
mr.introduction()


# extending parent method
class Person:
    def introduce(self):
        print("I am a person")


class Student(Person):
    def introduce(self):
        # Call parent method first
        super().introduce()

        # Extend behavior
        print("I am also a student")


st = Student()
st.introduce()
