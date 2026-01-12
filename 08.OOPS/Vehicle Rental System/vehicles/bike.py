from core.vehicle import Vehicle


class Bike(Vehicle):

    def vehicle_type(self):
        return "Bike"

    def calculate_rent(self, days):
        return (self._rate_per_day * days) * 0.8  # cheaper than car
