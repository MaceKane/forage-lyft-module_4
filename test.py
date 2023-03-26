import unittest
from datetime import datetime
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.octoprime_tires import OctoprimeTires
from tires.carrigan_tires import CarriganTires

class TestBattery(unittest.TestCase):

    def test_nubbin_battery_needs_service(self):
        # Last service date of January 1, 2020 and a current date of January 2, 2024.
        battery = NubbinBattery(datetime(2024, 1, 2), datetime(2020, 1, 1))
        # Assert that the needs_service method returns True.
        self.assertTrue(battery.needs_service())

        # Last service date of January 1, 2020 and a current date of December 31, 2022.
        battery = NubbinBattery(datetime(2022, 12, 31), datetime(2020, 1, 1))
        # Assert that the needs_service method returns False.
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service(self):
        # Last service date of January 1, 2020 and a current date of January 1, 2024.
        battery = SpindlerBattery(datetime(2024, 1, 1), datetime(2020, 1, 1))
        # Assert that the needs_service method returns True.
        self.assertTrue(battery.needs_service())

        # Last service date of January 1, 2020 and a current date of December 31, 2022.
        battery = SpindlerBattery(datetime(2022, 12, 31), datetime(2020, 1, 1))
        # Assert that the needs_service method returns False.
        self.assertFalse(battery.needs_service())


class TestEngine(unittest.TestCase):

    def test_capulet_engine_needs_service(self):
        # Last service mileage of 10000 and a current mileage of 40001.
        engine = CapuletEngine(40001, 10000)
        # Assert that the needs_service method returns True.
        self.assertTrue(engine.needs_service())

        # Last service mileage of 10000 and a current mileage of 15000.
        engine = CapuletEngine(15000, 10000)
        # Assert that the needs_service method returns False.
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        # Warning light on.
        engine = SternmanEngine(True)
        # Assert that the needs_service method returns True.
        self.assertTrue(engine.needs_service())

        # Warning light off.
        engine = SternmanEngine(False)
        # Assert that the needs_service method returns False.
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        # Last service mileage of 10000 and a current mileage of 70001.
        engine = WilloughbyEngine(70001, 10000)
        # Assert that the needs_service method returns True.
        self.assertTrue(engine.needs_service())

        # Last service mileage of 10000 and a current mileage of 15000.
        engine = WilloughbyEngine(15000, 10000)
        # Assert that the needs_service method returns False.
        self.assertFalse(engine.needs_service())

class TestTires(unittest.TestCase):

    def test_octoprime_tires_needs_service_true(self):
        tires = OctoprimeTires([0.9, 0.9, 0.7, 0.6])
        # Assert that the needs_service method returns True.
        self.assertTrue(tires.needs_service())

    def test_octoprime_tires_needs_service_false(self):
        tires = OctoprimeTires([0.6, 0.7, 0.8, 0.9])
        # Assert that the needs_service method returns False.
        self.assertFalse(tires.needs_service())

    def test_carrigan_tires_needs_service_true(self):
        tires = CarriganTires([0.8, 0.9, 0.7, 0.6])
        # Assert that the needs_service method returns True.
        self.assertTrue(tires.needs_service())

    def test_carrigan_tires_needs_service_false(self):
        tires = CarriganTires([0.6, 0.7, 0.8, 0.8])
        # Assert that the needs_service method returns False.
        self.assertFalse(tires.needs_service())

if __name__ == '__main__':
    unittest.main()
