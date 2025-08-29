from __future__ import annotations
from .user import User 
from .rider_type import RiderType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .ride import Ride 
class Rider(User):

    def __init__(self,id:int,name:str,email:str,rider_type:RiderType):
        super().__init__(id,name,email)
        self.__rider_type=rider_type
        self.__pending_requests:list[Ride]=[]
        self.__current_ride:Ride=None 
    
    def get_current_ride(self):
        return self.__current_ride
    
    def set_current_ride(self,ride:Ride):
        self.__current_ride=ride
    
    def get_rider_type(self)->RiderType:
        return self.__rider_type
    
    def get_pending_requests(self)->list[Ride]:
        return self.__pending_requests
    
    def add_pending_request(self, ride: Ride):
        self.__pending_requests.append(ride)
    
    def remove_pending_request(self, ride: Ride):
        if ride in self.__pending_requests:
            self.__pending_requests.remove(ride)
    
    def get_active_requests(self)->list[Ride]:
        return [ride for ride in self.__pending_requests if ride.get_ride_status().value in ['CREATED', 'ACCEPTED']]