from core.vehicle import Vehicle


class Truck(Vehicle):

    def vehicle_type(self):
        return "Truck"

    def calculate_rent(self, days):
        return (self._rate_per_day * days) + 500  # loading charge
