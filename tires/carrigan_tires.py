# Importing the Tires class.
from tires.tires import Tires

# Defining a new class called "CarriganTires" that inherits from the "Tires" class.
class CarriganTires(Tires):
    
    # Setting the tire_wear attribute of the new object to the input value of tire_wear.
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        
    def needs_service(self):
        # Looping through each tire in the tire_wear attribute.
        for tire in self.tire_wear:
            # Checking if the wear level of the tire is greater than or equal to 0.9.
            if tire >= 0.9:
                # Returning True if any tire needs to be serviced according to the Carrigan tire wear sensor criteria.
                return True
        # Returning False if no tire needs to be serviced according to the Carrigan tire wear sensor criteria.
        return False