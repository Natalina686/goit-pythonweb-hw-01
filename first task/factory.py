from abc import ABC, abstractmethod
from vehicles import Vehicle, Car, Motorcycle

class VehicleFactory(ABC):
    @abstractmethod

    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass

class USVehicycleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")
    
    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "US Spec")

class EUVehicycleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")
    
    def create_motorcycle(self, make: str, model: str):
        return Motorcycle(make, model, "EU Spec")