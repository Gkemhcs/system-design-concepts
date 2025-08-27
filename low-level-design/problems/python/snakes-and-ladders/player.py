class Player:


    def __init__(self,name:str):
        self.__name:str=name 
        self.__position:int=0
    
    def get_name(self)->str:
        return self.__name
    def set_position(self,position:int):
        self.__position=position
    def get_position(self)->int:
        return self.__position