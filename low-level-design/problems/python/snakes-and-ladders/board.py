from entity import Entity 
from errors import DuplicateEntityError
class Board:
    def __init__(self,n:int):
        self.__size:int=n
        self.__entities:dict[int:Entity]={}
    
    def set_entity(self,entity:Entity):
        if entity.get_start() in self.__entities:
            raise DuplicateEntityError("sorry the current start position has been already filled with another entity")
        self.__entities[entity.get_start()]=entity 
    
    def get_next_position(self,pos:int)->int:

        if pos in self.__entities:
            return self.__entities[pos].get_end()
        return pos 
    
    def get_size(self)->int:
        return self.__size