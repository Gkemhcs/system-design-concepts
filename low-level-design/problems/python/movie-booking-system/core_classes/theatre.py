from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .screen import Screen 


class Theatre:

    def __init__(self,id:int,name:str,location:str):
        self._id=id 
        self.__name=name 
        self.__location=location
        self.__screens:list[Screen]=[]
    def get_id(self)->int:
        return self._id 
    def get_name(self)->str:
        return self.__name 
    def get_location(self)->str:
        return self.__location 
    def get_screens(self)->list[Screen]:
        return self.__screens
    def add_screen(self,screen:Screen):
        self.__screens.append(screen)
    def get_screen(self,id:int)->Screen:
        for screen in self.__screens:
            if screen.get_id()==id:
                return screen 
        raise Exception("sorry the screen you are looking for not exist")
 
