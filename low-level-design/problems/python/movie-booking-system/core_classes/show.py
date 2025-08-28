from __future__ import annotations

import threading 
from .movie import Movie
from .screen import Screen 
from .seat import Seat
from datetime import datetime
from strategies.pricing_strategy import PricingStrategy


class Show:

    def __init__(self,id:int,screen:Screen,movie:Movie,start_time:datetime,duration:int)->Movie:
        
        self._id=id
        self.__movie=movie 
        self.__screen=screen 
        self.__start_time=start_time
        self.__duration_in_minutes=duration
       
        self.__lock=threading.Lock()
    def get_id(self)->int:
        return self._id 
    def get_movie(self)->Movie :
        return self.__movie 
    def get_screen(self)->Screen:
        return self.__screen 
    def get_start_time(self)->datetime:
        return self.__start_time
    def get_duration(self)->int:
        return self.__duration_in_minutes
    def get_pricing_strategy(self)->PricingStrategy:
        return self.__pricing_strategy
    def change_strategy(self,strategy:PricingStrategy):
        self.__pricing_strategy=strategy
    def get_lock(self)->threading.Lock:
        return self.__lock 
 
    
