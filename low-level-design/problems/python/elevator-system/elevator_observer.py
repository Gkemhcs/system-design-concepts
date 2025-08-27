from abc import ABC,abstractmethod
from direction import Direction
from elevator_state import ElevatorState
class ElevatorObserver(ABC):


    @abstractmethod
    def on_floor_change(self,elevator_id:int,floor:int):
        pass 
    def on_state_change(self,elevator_id:int,from_state:ElevatorState,to_state:ElevatorState):
        pass 