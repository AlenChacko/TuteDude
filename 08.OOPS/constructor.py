# __init__()
# It is the constructor method that runs automatically when an object is created
# It initialize the object data


def show_model():
    print(f"")


class Car:
    def __init__(self, brand, model, power, torque, price, fuel, transmission):
        self.brand = brand
        self.model = model
        self.power = power
        self.torque = torque
        self.fuel = fuel
        self.transmission = transmission
        self.price = price
        print("Calling the constructor")

    def show_car(self):
        print(f"Brand:{self.brand}\nModel:{self.model}")

    def show_specs(self):
        print(
            f"{self.brand} {self.model}\nPower:{self.power} BHP\nTorque:{self.torque} NM\nFuel:{self.fuel}\nTransmission:{self.transmission}\nPrice:{self.price} Lakhs"
        )


car_1 = Car("Kia", "Seltos", 160, 253, 27, ["Petrol", "Diesal"], ["DCT", "Manual"])
car_1.show_car()
car_1.show_specs()
car_1.type = "SUV"
print(car_1.type)

car_2 = Car("Volkswagon", "Virtus", 150, 250, 23, ["Petrol"], ["DSG", "Manual"])
car_2.show_car()
car_2.show_specs()

print(car_1.brand)
print(car_2.model)
