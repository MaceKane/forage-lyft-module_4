# Importing the Serviceable class from the serviceable module.
from serviceable import Serviceable

# Defining a new class called "Car" that inherits from the "Serviceable" class.
class Car(Serviceable):

    # Initializes the "engine" and "battery" attributes of the object.
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    # Defining a method called "needs_service" that overrides the method of the same name in the "Serviceable" class.
    # This method checks whether the car needs to be serviced or not.
    # It does this by calling the "needs_service" method of the engine and battery objects, and returning True if either of them needs to be serviced.
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
