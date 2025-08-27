from elevator_controller import ElevatorController
from elevator import Elevator
from nearest_elevator_assignment_strategy import NearestElevatorAllocationStrategy
from look_based_strategy import LookBasedStrategy
from display import Display
from direction import Direction
from external_request import ExternalRequest
from internal_request import InternalRequest


def main():
    lookup_strategy=LookBasedStrategy()
    elevator1=Elevator(1,strategy=lookup_strategy)
    elevator2=Elevator(2,strategy=lookup_strategy)
    display=Display()
    elevator1.register_observer(display)
    elevator2.register_observer(display)
    
    allocator=NearestElevatorAllocationStrategy()
    controller=ElevatorController(allocator=allocator)
    controller.add_elevator(elevator1)
    controller.add_elevator(elevator2)
    controller.make_external_request(ExternalRequest(3,Direction.UP))
    controller.make_external_request(ExternalRequest(2,Direction.UP))
    controller.make_internal_request(elevator1,InternalRequest(5))
    controller.next_stop(elevator1)
 
 

if __name__=="__main__":
    main()