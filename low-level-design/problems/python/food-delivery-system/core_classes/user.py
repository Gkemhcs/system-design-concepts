from __future__ import annotations
from .location import Location

class User:

    def __init__(self,id:int,name:str,email:str,phone_number:int,location:Location)->User:
        self.__id=id 
        self.__name=name 
        self.__email=email 
        self.__location=location 
        self.__phone_number=phone_number
    def get_id(self)->int:
        return self.__id
    def get_name(self)->str:
        return self.__name 
    def get_email(self)->str:
        return self.__email
    def get_location(self)->Location:
        return self.__location 
    def get_phone_number(self)->int:
        return self.__phone_number 
    def set_location(self,location:Location):
        self.__location=location