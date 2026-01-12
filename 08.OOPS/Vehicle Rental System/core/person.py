from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class for all people in the system
    """

    def __init__(self, name, age):
        self.name = name  # public
        self._age = age  # protected
        self.__id = id(self)  # private

    # Getter for private attribute
    def get_id(self):
        return self.__id

    @abstractmethod
    def get_role(self):
        pass
