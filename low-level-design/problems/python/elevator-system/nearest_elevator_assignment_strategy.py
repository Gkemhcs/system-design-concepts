from elevator_allocation_strategy import ElevatorAllocatorStrategy
from direction import Direction
from elevator import Elevator 
from elevator_state import ElevatorState
class NearestElevatorAllocationStrategy(ElevatorAllocatorStrategy):
    
    def assign_elevator(self, elevators:list[Elevator],direction:Direction,requested_floor:int)->Elevator:
        best_elevator=None 
        min_dist=float("inf")
    
        for elevator in elevators:
            if elevator is None :
                continue 
            if elevator.get_current_state()==ElevatorState.IDLE:
                if min_dist>abs(elevator.get_current_floor()-requested_floor):
                    min_dist=abs(elevator.get_current_floor()-requested_floor)
                    best_elevator=elevator 

            elif  elevator.get_direction()==direction:
                if min_dist>abs(elevator.get_current_floor()-requested_floor):
                    min_dist=abs(elevator.get_current_floor()-requested_floor)
                    best_elevator=elevator 
        
        if best_elevator is None:
            for elevator in elevators:
                if elevator.get_current_state()==ElevatorState.IDLE:
                    return elevator
        return best_elevator








