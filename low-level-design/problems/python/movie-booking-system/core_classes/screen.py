from __future__ import annotations
from .screen_type import ScreenType
from .seat import Seat 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .theatre import Theatre

class Screen:

    def __init__(self,id:int,type:ScreenType,theatre:Theatre,seats:list[Seat]=[])->Screen:
        self._id=id 
        self.__type=type 
        self.__theater=theatre
        self.__seats:list[Seat]=[]
    def get_id(self)->int:
        return self._id 
    def get_type(self)->ScreenType:
        return self.__type 
    def get_theater(self)->Theatre:
        return self.__theater
    def get_seats(self)->list[Seat]:
        return self.__seats
    def add_seats(self,seat:Seat):
        self.__seats.append(seat)
    def get_seat_by_id(self,id:int)->Seat:
        for seat in self.__seats:
            if seat.get_id()==id:
                return seat 
            
        raise Exception("the seat you are looking for is not found")
