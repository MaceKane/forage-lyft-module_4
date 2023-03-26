# Importing the abstract base class (ABC) module from the abc package.
from abc import ABC

# Defining a new class called "Battery" that inherits from ABC.
class Battery(ABC):
    def needs_service(self):
        pass
