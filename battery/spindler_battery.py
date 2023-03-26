# Importing the Battery class.
from battery.battery import Battery

# Importing the add_years_to_date function from the utils module.
from utils import add_years_to_date

# Defining a new class called "SpindlerBattery" that inherits from the "Battery" class.
class SpindlerBattery(Battery):

    # This method initializes the "current_date" and "last_service_date" attributes of the object.
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    # If the battery was last serviced more than 3 years ago, it needs to be serviced.
    # The "add_years_to_date" function is used to calculate the date by which the battery should be serviced.
    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
