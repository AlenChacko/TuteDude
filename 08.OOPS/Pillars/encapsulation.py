# Without encapsulation
class BankAccount:
    def __init__(self, name, balance):

        # public attributes
        self.name = name
        self.balance = balance


# creating object
account = BankAccount("Alen", 10000)

# direct access
print(account.balance)

# direct modification
account.balance = -192343
print(account.balance)


# protected attributes
class SecureBank:
    def __init__(self, name, balance):
        self.name = name

        # protected
        self._balance = balance

    def deposite(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        else:
            self._balance += amount
            print(f"Money has been credited")

    def withdrawal(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print("Money has been debited")

    def show_balance(self):
        return self._balance


secure = SecureBank("Chethas", 55000)
bal = secure.show_balance()
secure.deposite(12000)
print(f"Your current balance: {bal}")
secure.withdrawal(5000)
# direct access
print(f"Direct access balance:{secure._balance}")

# # Allowed but discouraged ❌
secure._balance = 3000
print(f"After changing:{secure._balance}")
print()


# private attributes
class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary

    def show_employee(self):
        print(f"Name:{self.name}\nRole:{self.role}\nSalary:{self.__salary}")


emp = Employee("Arjun", "Developer", 35000)
emp.show_employee()

# accessing or changing salary
# print(emp.salary)
# print(emp.__salary)
# emp.__salary = 78000
emp.show_employee()


# Getter and Setter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter
    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age <= 0:
            print("Invalid age")
        else:
            self.__age = new_age


p = Person("Amal", 32)
print(p.get_age())
p.set_age(52)
print(p.get_age())
# not recommended
# print(p._Person__age)


# Pythonic Encapsulation
class Product:
    def __init__(self, item, price):
        self.item = item
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            print("Invalid price")
        else:
            self.__price = new_price


pr = Product("OIL", 45)
print(f"Getter:{pr.price}")
pr.price = 67
print(f"After Setting:{pr.price}")


# read only
class Demo:
    def __init__(self, sample):
        self.__sample = sample

    @property
    def sample(self):
        return self.__sample


d = Demo(55)
print(d.sample)

# not possible
# d.sample = 67


# Complete Banking System
class MalayoraBank:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposite(self, amount):
        if amount <= 0:
            print(f"Hey {self.holder}, this amount is invalid")
        elif not isinstance(amount, int):
            print(f"Hey {self.holder}, Enter valid integers")
        else:
            self.__balance += amount
            print(
                f"Hey {self.holder}, your deposit of amount {amount} has been credited to your account."
            )

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Hey {self.holder}, this amount is invalid")
        elif amount > self.__balance:
            print(f"Hey {self.holder}, You don't have enough balance in your acconut")
        elif not isinstance(amount, int):
            print(f"Hey {self.holder}, Enter valid integers")
        else:
            self.__balance -= amount
            print(
                f"Hey {self.holder}, your withdrawal of amount {amount} has been debited to your account."
            )


h1 = MalayoraBank("Alen")
bal = h1.balance
print(f"Your account balance is {bal}")

h1.deposite(55000)
bal = h1.balance
print(f"Your account balance is {bal}")

h1.withdraw(4533)
bal = h1.balance
print(f"Your account balance is {bal}")
