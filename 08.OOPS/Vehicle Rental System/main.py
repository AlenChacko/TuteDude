from core.person import Person
from core.rental import RentalService
from vehicles.car import Car
from vehicles.electric import ElectricCar
from payments.upi import UPIPayment


class Customer(Person):

    def get_role(self):
        return "Customer"


customer = Customer("Alen", 25)
vehicle = ElectricCar("Tesla", "Model 3", 5000)
payment = UPIPayment()

rental_service = RentalService()
rental_service.rent_vehicle(customer, vehicle, 3, payment)
