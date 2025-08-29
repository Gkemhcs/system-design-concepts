from __future__ import annotations
class Location:

    def __init__(self,latitude:float,longitude:float,name:str):
        self.__name=name 
        self.__latitude=latitude
        self.__longitude=longitude
    def get_name(self)->str:
        return self.__name
    def get_latitude(self)->float:
        return self.__latitude
    def get_longitude(self)->float:
        return self.__longitude
    
    def calculate_distance(self,other:Location)->float:
        return abs(self.__latitude-other.get_latitude())+abs(self.__longitude-other.get_longitude())
    def __str__(self)->str:
        return f"Name:{self.__name}, Latitude:{self.__latitude}, Longitude:{self.__longitude}"