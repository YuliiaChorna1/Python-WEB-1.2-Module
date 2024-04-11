# Абстрактні класи та інтерфейси. Різниця

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def __init__(self) -> None:
        self.property_one = None
        self.property_two = None

    def method_three(self):
        self.method_one()
        self.method_two()

    @abstractmethod
    def method_one(self):
        pass

    @abstractmethod
    def method_two(self):
        pass


class InterfaceClass(ABC):

    @abstractmethod
    def method_a(self):
        pass

    @abstractmethod
    def method_b(self):
        pass