from .location import Location
from .driver import Driver 
from .rider import Rider 

from core_classes.driver_status import DriverStatus
from .ride_status import RideStatus
from threading import Lock 
from datetime import datetime 

class Ride:
    def __init__(self,id:int,rider:Rider,pickup_location:Location,drop_location:Location):
        self.__id=id 
        self.__rider=rider        
        self.__driver:Driver=None
        self.__pickup_location=pickup_location
        self.__drop_location=drop_location
        self.__distance=pickup_location.calculate_distance(drop_location)
        self.__start_time=None
        self.__end_time=None
        self.__amount=0.0
        self.__ride_status=RideStatus.CREATED
        self.__lock=Lock()
    def get_id(self)->int:
        return self.__id 
    def get_rider(self)->Rider:
        return self.__rider 
    def get_driver(self)->Driver:
        return self.__driver 
    def set_driver(self,driver:Driver):
        self.__driver=driver 
    def get_pickup_location(self)->Location:
        return self.__pickup_location
    def get_drop_location(self)->Location:
        return self.__drop_location
    def get_distance(self)->float:
        return self.__distance
    def get_amount(self)->float:
        return self.__amount
    def set_amount(self,amount:float):
        self.__amount=amount
    def get_ride_status(self)->RideStatus:
        return self.__ride_status
    def set_ride_status(self,status:RideStatus):
        self.__ride_status=status
    def accept_ride(self,driver:Driver)->bool:
        with self.__lock:
            if self.__driver is not None:
                raise Exception("Ride already accepted by another driver.")
            else:
                self.__driver=driver
                self.set_ride_status(RideStatus.ACCEPTED)
                driver.set_current_ride(self)
                driver.set_status(DriverStatus.BUSY)
                self.__rider.set_current_ride(self)
                print(f"Ride {self.__id} accepted by Driver {driver.get_id()}")
                return True 
    
    def accept_booking(self, driver: Driver) -> bool:
        """Alias for accept_ride to match the class diagram"""
        return self.accept_ride(driver)
    def start_ride(self):
        if self.__ride_status!=RideStatus.ACCEPTED:
            raise Exception("sorry cannot start the ride as it is not in accepted state")
        else:
            self.set_ride_status(RideStatus.STARTED)
            self.__start_time=datetime.now()
            print(f"Ride {self.__id} started by Driver {self.__driver.get_id()} and Rider {self.__rider.get_id()}")
    def complete_ride(self):
        if self.__ride_status!=RideStatus.STARTED:
            raise Exception("Ride cannot be completed as it's not in accepted state.")
        else:
            self.set_ride_status(RideStatus.COMPLETED)
            self.__driver.set_current_ride(None)
            self.__driver.set_location(self.__drop_location)
            self.__driver.set_status(DriverStatus.AVAILABLE)
            self.__end_time=datetime.now()
            print(f"Ride {self.__id} completed by Driver {self.__driver.get_id()} and Rider {self.__rider.get_id()}")
            self.__rider.set_current_ride(None)
    def cancel_ride(self):
        if self.__ride_status!=RideStatus.ACCEPTED:
            raise Exception("Ride cannot be cancelled as it's already completed or not accepted yet or already started")
        else:
            self.set_ride_status(RideStatus.CANCELLED)
            self.__driver.set_current_ride(None)
            self.__rider.set_current_ride(None)
            self.__driver.set_status(DriverStatus.AVAILABLE)
            print(f"Ride {self.__id} cancelled by Rider {self.__rider.get_id()}")