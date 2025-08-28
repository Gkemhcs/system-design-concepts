from __future__ import annotations

class Movie:

    def __init__(self,id:int,name:str,duration:int)->Movie:
        self._id=id 
        self.__name=name 
        self.__duration_in_minutes=duration
    
    def get_id(self)->int:
        return self._id 
    def get_name(self)->str:
        return self.__name 
    def get_duration(self)->int:
        return self.__duration_in_minutes
    
        

