from core_classes.show import Show
from core_classes.screen import Screen 
from core_classes.movie import Movie
from core_classes.seat import Seat 
from service.seat_availability_service import SeatAvailabilityService

from datetime import datetime 


class ShowService:

    def __init__(self,seat_availability_service:SeatAvailabilityService):
        self.__shows:dict[int,Show]={}
        self.__seat_availability_service=seat_availability_service
        self.__show_counter=1
    def create_show(self,screen:Screen,movie:Movie,start_time:datetime,duration:int)->Show:
        show_id=self.__show_counter
        show=Show(show_id,screen,movie,start_time,duration)
        self.__shows[show_id]=show 
        self.__show_counter+=1
        print(f"show for movie {movie.get_name()} in screen{screen.get_id()} will start at {start_time}")
        return show 
    def get_show(self,show_id:int)->Show:
        if show_id not in self.__shows:
            raise Exception("sorry the show you are trying to access not exist")
        else:
            show=self.__shows[show_id]
            return show 
    def get_available_seats(self, show: Show) -> list[Seat]:
        return self.__seat_availability_service.get_available_seats(show)
   