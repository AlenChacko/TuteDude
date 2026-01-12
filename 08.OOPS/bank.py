class Bank:
    def __init__(self, customer_name, account_no, balance=0):
        self.costomer_name = customer_name
        self.account_no = account_no
        self.balance = balance
        self.transactions = []

    def deposite(self, amount):
        if amount <= 0:
            print("Enter a valid amount to deposite")
            return
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(
            f"Congrats {self.costomer_name} an amount of rupees {amount} creadited to your accout"
        )

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Enter a valid amount")
        elif amount > self.balance:
            print(f"Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn {amount}")
            print(
                f"{self.costomer_name}, an amount of rupees {amount} debited to your accout"
            )

    def show_balance(self):
        print(
            f"Hello {self.costomer_name}, your balance for account {self.account_no} is {self.balance}"
        )

    def show_transactions(self):
        if len(self.transactions) == 0:
            print("You don't have any transactions")
        print(f"Here is your complete transaction history {self.costomer_name}\n")
        for transactions in self.transactions:
            print(f"{transactions}\n")


customer_1 = Bank("Alen", 2345123879)
customer_1.show_balance()
customer_1.withdraw(0)
customer_1.deposite(45000)
customer_1.show_balance()
customer_1.withdraw(12000)
customer_1.show_balance()
customer_1.show_transactions()
