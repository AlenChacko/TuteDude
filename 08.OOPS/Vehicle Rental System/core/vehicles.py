from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class for all vehicles
    """

    def __init__(self, brand, model, rate_per_day):
        self.brand = brand
        self.model = model
        self._rate_per_day = rate_per_day  # protected
        self.__available = True  # private

    # Encapsulation using getter/setter
    def is_available(self):
        return self.__available

    def set_availability(self, status):
        self.__available = status

    @abstractmethod
    def vehicle_type(self):
        pass

    @abstractmethod
    def calculate_rent(self, days):
        pass
