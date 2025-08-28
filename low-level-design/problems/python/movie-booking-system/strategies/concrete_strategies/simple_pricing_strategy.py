from strategies.pricing_strategy import PricingStrategy
from core_classes.seat_type import SeatType

class SimplePricingStrategy(PricingStrategy):
    regular_seat_pricing=200.0
    premium_seat_pricing=300.0
    def __init__(self):
        pass 
    def calculate_price(self, seats)->float:
       
        total_amount=0
        for seat in seats:
           if seat.get_seat_type()==SeatType.REGULAR:
               total_amount+=self.regular_seat_pricing
           else:
               total_amount+=self.premium_seat_pricing
        return total_amount