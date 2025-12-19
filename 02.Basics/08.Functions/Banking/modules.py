balance = 0.0


def show_balance():
    return f"Your current balance is {balance}"


def make_deposite(amout):
    if amout < 0 or amout == 0:
        return "Please enter a valid amount!"
    else:
        global balance
        balance = balance + amout
        return f"Congratulations, Your deposite has been credited\nYour new balance is {balance}"


def make_withdrawal(amount):
    global balance
    if amount > balance:
        return "Failed, Insufficient balance in account."
    else:

        balance = balance - amount
        return balance


def cancel_process():
    return "Thankyou for using our service, please visit again"
