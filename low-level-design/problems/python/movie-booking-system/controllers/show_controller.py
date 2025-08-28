from service.show_service import ShowService
from core_classes.show import Show 
from core_classes.screen import Screen 
from core_classes.movie import Movie
from core_classes.seat import Seat 
from datetime import datetime 

class ShowController:

    def __init__(self,show_service:ShowService):
        self.__show_service=show_service
    
    def create_show(self,screen:Screen,movie:Movie,start_time:datetime,duration:int)->Show:
        return self.__show_service.create_show(screen,movie,start_time,duration)

    def get_show(self,show_id:int)->Show:
        return self.__show_service.get_show(show_id)
    
    def get_available_seats(self, show:Show) -> list[Seat]:
        return self.__show_service.get_available_seats(show)

    