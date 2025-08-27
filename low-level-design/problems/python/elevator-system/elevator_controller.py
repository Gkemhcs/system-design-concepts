from elevator import Elevator
from elevator_allocation_strategy import ElevatorAllocatorStrategy
from direction import Direction 
from external_request import ExternalRequest
from internal_request import InternalRequest
from elevator_request import ElevatorRequest
from errors import ElevatorAllocationError

class ElevatorController:

    def __init__(self, allocator: ElevatorAllocatorStrategy, elevators: list[Elevator] = []):
        self.__elevators:list[Elevator] = elevators
        self.__allocator:ElevatorAllocatorStrategy = allocator
    
    def get_elevator_by_id(self,id)->Elevator:
        for elevator in self.__elevators:
            if elevator.get_id()==id:
                return elevator 
        return None 
    def add_elevator(self,elevator):
        self.__elevators.append(elevator)
    def change_allocation_stratgey(self,strategy:ElevatorAllocatorStrategy):
        self.__allocator=strategy
    
    def __allocate_elevator(self,direction:Direction,requested_floor:int)->Elevator:
        elevator=self.__allocator.assign_elevator(self.__elevators,direction,requested_floor)
        if elevator is None:
            raise ElevatorAllocationError("sorry hold on no free elevators all are serving at max capacity")
       

        return elevator 

    def _request_elevator(self,direction:Direction,requested_floor:int)->Elevator:
        elevator=self.__allocate_elevator(direction,requested_floor)
        return elevator

    def make_external_request(self,request:ExternalRequest):
        elevator=self._request_elevator(request.get_direction(),request.get_floor())
        elevator.add_requests(request)
        return elevator 

    def make_internal_request(self,elevator:Elevator,request:InternalRequest):
        elevator.add_requests(request)
        return elevator

    def next_stop(self,elevator:Elevator):
        elevator.move_next()
    
    
