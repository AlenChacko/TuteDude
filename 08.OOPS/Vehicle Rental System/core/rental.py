from utils.discounts import apply_discount


class RentalService:

    def rent_vehicle(self, customer, vehicle, days, payment_method):
        if not vehicle.is_available():
            raise Exception("Vehicle not available")

        rent = vehicle.calculate_rent(days)
        final_amount = apply_discount(rent, 10)

        vehicle.set_availability(False)

        print(f"{customer.name} rented {vehicle.vehicle_type()}")
        payment_method.pay(final_amount)
