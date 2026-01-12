from vehicles.car import Car


class ElectricCar(Car):

    def calculate_rent(self, days):
        return super().calculate_rent(days) * 0.9  # eco discount
