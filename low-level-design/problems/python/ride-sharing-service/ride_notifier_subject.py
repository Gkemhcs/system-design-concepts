from strategies.notification_observer import INotificationObserver
from core_classes.ride import Ride
from core_classes.driver import Driver

class NotifierSubject:

    def __init__(self):
        self.__observers:list[INotificationObserver]=[]
    def add_observer(self,observer:INotificationObserver):
        self.__observers.append(observer)
    def remove_observer(self,observer:INotificationObserver):
        self.__observers.remove(observer)
    def notify_ride_created(self,ride:Ride,driver:Driver):
        for observer in self.__observers:
            observer.on_ride_created(ride,driver)
    def notify_ride_accepted(self,ride:Ride):
        for observer in self.__observers:
            observer.on_ride_accepted(ride)
