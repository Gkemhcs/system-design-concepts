from ..pricing_strategy import IPricingStrategy
from core_classes.ride import Ride 
from core_classes.rider_type import RiderType

class RiderTypeBasedPricing(IPricingStrategy):
    """
    Pricing strategy based on rider type (Regular vs Premium)
    Premium users get discounted rates
    """
    
    def __init__(self, base_rate: float = 10.0, premium_discount: float = 0.2):
        self.__base_rate = base_rate
        self.__premium_discount = premium_discount
    
    def calculate_fare(self, ride: Ride) -> float:
        base_fare = ride.get_distance() * self.__base_rate
        
        # Apply premium discount if rider is premium
        if ride.get_rider().get_rider_type() == RiderType.PREMIUM:
            discount_amount = base_fare * self.__premium_discount
            base_fare -= discount_amount
            print(f"Premium discount applied: {discount_amount:.2f}")
        
        return round(base_fare, 2)
