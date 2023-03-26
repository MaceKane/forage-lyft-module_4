# Importing the Tires class.
from tires.tires import Tires

# Defining a new class called "OctoprimeTires" that inherits from the "Tires" class.
class OctoprimeTires(Tires):

    # Setting the tire_wear attribute of the new object to the input value of tire_wear.
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    # Returning True if the sum of all values in the tire_wear attribute is greater than or equal to 3.0.
    def needs_service(self):
        return sum(self.tire_wear) >= 3.0

