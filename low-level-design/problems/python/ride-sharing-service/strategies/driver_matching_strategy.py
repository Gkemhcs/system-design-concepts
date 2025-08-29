
from abc import ABC,abstractmethod
from core_classes.ride import Ride
from core_classes.driver import Driver

class IDriverMatchingStrategy(ABC):

    @abstractmethod
    def find_driver(self,ride:Ride)->list[Driver]:
        pass