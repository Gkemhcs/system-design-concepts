from abc import ABC,abstractmethod
from core_classes.ride import Ride
from core_classes.driver import Driver
from core_classes.rider import Rider


class IPricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self,ride:Ride)->float:
        pass 
