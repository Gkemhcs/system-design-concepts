from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from reservation import Reservation

class User:

    def __init__(self,user_id,name,location):
          self._name=name 
          self._user_id=user_id 
          self._location=location 
          self._reservations:dict[int,Reservation]={}
    
    def get_name(self)->str:
         return self._name 
    def get_user_id(self)->str:
         return self._user_id

    def get_location(self)->str:
         return self._location
    def add_reservation(self,reservation:Reservation):
         self._reservations[reservation.get_reservation_id()]=reservation
    def clear_reservation(self,reservation:Reservation):
        del self._reservations[reservation.get_reservation_id()]