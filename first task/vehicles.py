from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)

class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str):
        self.make = make
        self.model = model
        self.spec = spec


    @abstractmethod
    def start_engine(self) -> None:
        pass

class Car(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Car engine started.")

class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} ({self.spec}): Motorcycle engine started.")
