from abc import ABC,abstractmethod
from core_classes.ride import Ride
 
from core_classes.driver import Driver


class INotificationObserver(ABC):

    @abstractmethod
    def on_ride_created(self,ride:Ride,drivers:list[Driver]):
        pass 
    @abstractmethod
    def on_ride_accepted(self,ride:Ride):
        pass
