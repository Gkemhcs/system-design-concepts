from service.theatre_service import TheatreService
from core_classes.theatre import Theatre
from core_classes.screen import Screen
from core_classes.seat import Seat
from core_classes.screen_type import ScreenType
from core_classes.seat_type import SeatType
class TheatreController:

    def __init__(self,theatre_service:TheatreService):
        self.__theatre_service=theatre_service

    def create_theatre(self,name:str,location:str)->Theatre:
        return self.__theatre_service.create_theatre(name,location)

    def get_theatre(self,id:int)->Theatre:
        return self.__theatre_service.get_theatre(id)

    def create_screen_in_theatre(self,theatre:Theatre,screen_type:ScreenType)->Screen:
        return self.__theatre_service.create_screen_in_theatre(theatre,screen_type)
    
    def get_screen_in_theatre(self,screen_id:int)->Screen:  
        return self.__theatre_service.get_screen_in_theatre(screen_id)

    def create_seat_in_screen(self,screen:Screen,seat_type:SeatType,row:int,col:int)->Seat:
        return self.__theatre_service.create_seat_in_screen(screen.get_id(),seat_type,row,col)
    def get_seat_in_screen(self,screen:Screen,seat_id:int)->Seat:
        return self.__theatre_service.get_seat_in_screen(screen.get_id(),seat_id)
    def get_all_seats(self,screen:Screen)->list[Seat]:
        return self.__theatre_service.get_all_seats(screen.get_id())

    def get_all_screens_in_theatre(self,theatre:Theatre)->list[Screen]:
        return self.__theatre_service.get_all_screens_in_theatre(theatre)
    