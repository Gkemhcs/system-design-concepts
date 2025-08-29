from __future__ import annotations
from .user import User 
from .driver_status import DriverStatus
from .location import Location
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ride import Ride 
class Driver(User):

    def __init__(self,id:int,name:str,email:str,driver_status:DriverStatus,location:Location):    
        super().__init__(id,name,email)
        self.__driver_status=driver_status
        self.__location:Location=location
        self.__current_ride:Ride=None
        self.__pending_requests:list[Ride]=[]

    def get_status(self)->DriverStatus:
        return self.__driver_status
    def set_status(self,status:DriverStatus):
        self.__driver_status=status
    def get_current_ride(self):
        return self.__current_ride 
    def set_current_ride(self,ride:Ride):
        self.__current_ride=ride
    def get_pending_requests(self)->list[Ride]:
        return self.__pending_requests
    def get_location(self)->Location:
        return self.__location
    def set_location(self,location:Location):
        self.__location=location
    def add_pending_request(self,ride:Ride):
        self.__pending_requests.append(ride)
    def accept_pending_request(self,ride_request_index:int):
        if ride_request_index==0 or ride_request_index>len(self.__pending_requests):
            raise Exception("invalid ride request index")
        ride=self.__pending_requests[ride_request_index-1]
        
        if self.__current_ride:
            raise Exception("cannot accept ride as you are already busy in ride")
        else:
            self.__current_ride=ride
            ride.accept_ride(self)
        self.__pending_requests.remove(ride)
    def reject_pending_request(self,ride_request_index:int):
        if ride_request_index==0 or ride_request_index>len(self.__pending_requests):
            raise Exception("invalid ride request index")
        ride=self.__pending_requests[ride_request_index-1]
        self.__pending_requests.remove(ride)
    