from elevator_request import ElevatorRequest
from elevator_state import ElevatorState
from direction import Direction
from elevator_state import ElevatorState
from elevator_observer import ElevatorObserver
from next_stop_strategy import NextStopStrategy

class Elevator:

    def __init__(self,elevator_id:int,strategy:NextStopStrategy):
        self._id=elevator_id
        self.__direction=Direction.UP
        self.__current_floor=0
        self.__current_state:ElevatorState=ElevatorState.IDLE
        self.__strategy=strategy
        self.__active_requests:list[ElevatorRequest]=[]
        self.__observers:list[ElevatorObserver]=[]
    def get_id(self)->int:
        return self._id 
    def get_direction(self)->Direction:
        return self.__direction
    def get_current_floor(self)->int:
        return self.__current_floor
    def get_current_state(self)->ElevatorState:
        return self.__current_state
    def get_requests(self)->list[ElevatorRequest]:
        return self.__active_requests
    def __notify_floor_change(self,floor:int):
        for observer in self.__observers:
            observer.on_floor_change(self.get_id(),floor)
    def __notify_state_change(self,from_state:ElevatorState,to_state:ElevatorState):
        for observer in self.__observers:
            observer.on_state_change(self.get_id(),from_state,to_state)
    def change_state(self,state:ElevatorState):
        from_state=self.get_current_state()
        self.__current_state=state 
        self.__notify_state_change(from_state,state)
    def set_direction(self,direction:Direction):
        self.__direction=direction
    
    def get_next_request(self)->ElevatorRequest:
        if self.__active_requests:
            return self.__active_requests[0]
        return None 
    def register_observer(self,observer:ElevatorObserver):
        self.__observers.append(observer)
    def unregister_observer(self,observer:ElevatorObserver):
        self.__observers.remove(observer)
    def add_requests(self,request:ElevatorRequest):
        self.__active_requests.append(request)
    
        
    
    def set_current_floor(self,floor:int):
        self.__current_floor=floor
    def move_next(self):
        next_floor=self.__strategy.get_next_stop(self)
        current_floor=self.get_current_floor()
        if next_floor!=current_floor:
            
            if current_floor>next_floor and self.get_direction()!=Direction.DOWN:
                self.set_direction(Direction.DOWN)
            elif current_floor<next_floor  and self.get_direction()!=Direction.UP:
                self.set_direction(Direction.UP)
        
        while next_floor==current_floor:
            if next_floor>current_floor:
                current_floor+=1
            else:
                current_floor-=1         
        self.set_current_floor(current_floor)
        self.change_state(ElevatorState.STOPPED)
        self.__complete_arrival(next_floor)
    def __complete_arrival(self,floor:int):
        index=-1
        self.__notify_floor_change(floor)
        for i,request in enumerate(self.__active_requests):
                if request.get_floor()==floor:
                    index=i 
                    break 
        self.__active_requests.pop(i)
        if len(self.__active_requests)==0:
            self.change_state(ElevatorState.IDLE)
        else:
            self.change_state(ElevatorState.RUNNING)

    
