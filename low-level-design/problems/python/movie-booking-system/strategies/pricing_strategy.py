from abc import ABC,abstractmethod
from core_classes.seat import Seat 
from core_classes.seat_type import SeatType
class PricingStrategy(ABC):

    @abstractmethod

    def calculate_price(self,seats:list[Seat])->float:
        pass 




