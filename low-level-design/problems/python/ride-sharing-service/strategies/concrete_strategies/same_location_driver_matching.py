from ..driver_matching_strategy import IDriverMatchingStrategy
from driver_manager import DriverManager


class SameLocationDriverMatching(IDriverMatchingStrategy):

    def __init__(self, driver_manager: DriverManager):
        self.__driver_manager = driver_manager

    def find_driver(self, ride):
        # In a real scenario, this would involve more complex logic
        # For simplicity, we'll assume drivers at the same location are suitable
        available_drivers = self.__driver_manager.get_available_drivers()
        matching_drivers = []
        for driver in available_drivers:
            if driver.get_location().get_name() == ride.get_pickup_location().get_name():
                matching_drivers.append(driver)
        return matching_drivers