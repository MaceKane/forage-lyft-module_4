# Importing the Engine class.
from engine.engine import Engine

# Defining a new class called "SternmanEngine" that inherits from the "Engine" class.
class SternmanEngine(Engine):

    # Initializes the "warning_light_is_on" attribute of the object.
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    # If the warning light is on, the engine needs to be serviced.
    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
