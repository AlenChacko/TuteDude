from payments.payment import Payment


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
