from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog Barks")


class Cat(Animal):
    def sound(self):
        print("Cat Meows")


dog = Dog()
cat = Cat()
dog.sound()


class Bank(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SBI(Bank):
    def deposit(self, amount):
        print(f"SBI: Deposited {amount}")

    def withdraw(self, amount):
        print(f"SBI: Withdrawn {amount}")


class HDFC(Bank):
    def deposit(self, amount):
        print(f"HDFC: Deposited {amount}")

    def withdraw(self, amount):
        print(f"HDFC: Withdrawn {amount}")


bank_accounts = [SBI(), HDFC()]

for bank in bank_accounts:
    bank.deposit(1000)
    bank.withdraw(500)


class Nofifications(ABC):
    def send(self, message):
        pass


class SMS(Nofifications):
    def send(self, message):
        print(f"SMS:{message}")


class Email(Nofifications):
    def send(self, message):
        print(f"EMAIL:{message}")


class Push(Nofifications):
    def send(self, message):
        print(f"Push:{message}")


sms = SMS()
sms.send("This message is via sms")
email = Email()
email.send("This message is via EMAIL")
push = Push()
push.send("This message is via push notification")


notifications = [SMS(), Email(), Push()]

for notify in notifications:
    notify.send("Message")
