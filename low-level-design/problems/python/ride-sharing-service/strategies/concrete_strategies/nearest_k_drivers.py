from ..driver_matching_strategy import IDriverMatchingStrategy
import heapq 
from core_classes.driver import Driver 
class NearestKDriversMatching(IDriverMatchingStrategy):

    def __init__(self, driver_manager, k):
        self.__driver_manager = driver_manager
        self.__k = k
    
    def find_driver(self, ride)->list[Driver]:
        available_drivers = self.__driver_manager.get_available_drivers()
        nearest_drivers = []
        
        for driver in available_drivers:
            distance = driver.get_location().calculate_distance(ride.get_pickup_location())
            # Use (distance, driver_id, driver) to avoid comparison issues
            # driver_id ensures unique ordering when distances are equal
            heapq.heappush(nearest_drivers, (distance, driver.get_id(), driver))
            
            if len(nearest_drivers) > self.__k:
                heapq.heappop(nearest_drivers)
        
        # Return only the drivers, sorted by distance (closest first)
        return [driver for _, _, driver in sorted(nearest_drivers)]