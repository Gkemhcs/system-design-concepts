from abc import ABC,abstractmethod
from elevator import Elevator
from direction import Direction

class ElevatorAllocatorStrategy(ABC):


    @abstractmethod
    def assign_elevator(self,elevators:list[Elevator],direction:Direction,requested_floor:int)->Elevator:
        pass 
