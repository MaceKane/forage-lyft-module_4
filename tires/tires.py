# Importing the abstract base class (ABC) module from the abc package.
from abc import ABC

# Defining a new abstract base class called "Tires" that inherits from ABC.
class Tires(ABC):
    def needs_service(self):
        pass