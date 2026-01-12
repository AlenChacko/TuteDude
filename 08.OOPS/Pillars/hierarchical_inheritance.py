# multiple child classes inherits from one parent


class Account:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print(f"Your balance:{self.balance}")


class SavingsAccount(Account):
    def interest(self):
        print(f"Savings account earns interest")


class CurrentAccount(Account):
    def overdraft(self):
        print("Current account has overdraft facility")


sa = SavingsAccount(10000)
ca = CurrentAccount(5000)

sa.show_balance()
sa.interest()

ca.show_balance()
ca.overdraft()
