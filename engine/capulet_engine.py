# Importing the Engine class.
from engine.engine import Engine

# Defining a new class called "CapuletEngine" that inherits from the "Engine" class.
class CapuletEngine(Engine):

    # Initializes the "current_mileage" and "last_service_mileage" attributes of the object.
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # If the current mileage minus the last service mileage is greater than 30,000 miles, the engine needs to be serviced.
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
