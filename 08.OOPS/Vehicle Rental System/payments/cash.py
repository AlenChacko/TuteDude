from payments.payment import Payment


class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} in Cash")
