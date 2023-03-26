# Importing the abstract base class (ABC) module from the abc package.
from abc import ABC, abstractmethod

# Defining a new abstract base class called "Serviceable" that inherits from ABC.
class Serviceable(ABC):

    # Defining an abstract method called "needs_service".
    @abstractmethod
    def needs_service(self):
        pass
