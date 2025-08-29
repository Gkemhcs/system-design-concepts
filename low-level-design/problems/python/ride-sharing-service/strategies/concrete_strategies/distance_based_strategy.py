from ..pricing_strategy import IPricingStrategy
from core_classes.ride import Ride 

class DistanceBasedPricing(IPricingStrategy):
    """
    Pricing strategy based purely on distance with base fare
    """
    
    def __init__(self, base_fare: float = 50.0, per_km_rate: float = 15.0):
        self.__base_fare = base_fare
        self.__per_km_rate = per_km_rate
    
    def calculate_fare(self, ride: Ride) -> float:
        distance = ride.get_distance()
        total_fare = self.__base_fare + (distance * self.__per_km_rate)
        print(f"Distance: {distance:.2f}km, Base: {self.__base_fare}, Per km: {self.__per_km_rate}")
        return round(total_fare, 2)
