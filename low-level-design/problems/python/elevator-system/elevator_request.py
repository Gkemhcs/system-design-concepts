from direction import Direction

class ElevatorRequest:

    def __init__(self,floor:int=0,direction:Direction=None):
        self.__floor=floor 
        self.__direction=direction 

    def get_direction(self)->Direction:
        return self.__direction 
    def get_floor(self)->int:
        return self.__floor 
    
    