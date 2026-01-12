from core.vehicle import Vehicle


class Car(Vehicle):

    def vehicle_type(self):
        return "Car"

    def calculate_rent(self, days):
        return self._rate_per_day * days
