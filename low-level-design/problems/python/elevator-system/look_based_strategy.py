from next_stop_strategy import NextStopStrategy
from errors import NoActiveRequests
from elevator import Elevator
from direction import Direction
from external_request import ExternalRequest

class LookBasedStrategy(NextStopStrategy):


    def get_next_stop(self, elevator:Elevator)->int:
        # Implement the logic to find the next stop for the elevator
        primary_request=elevator.get_next_request().get_floor()
        if primary_request==elevator.get_current_floor():
            return elevator.get_current_floor()

        candidate=primary_request
        direction=Direction.UP if primary_request>elevator.get_current_floor() else Direction.DOWN
        for request in elevator.get_requests():
            if  isinstance(request,ExternalRequest) and request.get_direction()==direction:
                if direction==Direction.UP and   request.get_floor()>elevator.get_current_floor() and request.get_floor()<=candidate:
                    candidate=request.get_floor()
                elif direction==Direction.DOWN and request.get_floor()<elevator.get_current_floor() and request.get_floor()>=candidate:
                    candidate=request.get_floor()
            else:
                if  request.get_floor()>elevator.get_current_floor() and request.get_floor()<=candidate:
                    candidate=request.get_floor()
                elif request.get_floor()<elevator.get_current_floor() and request.get_floor()>=candidate:
                    candidate=request.get_floor()

        return candidate
            



    


        raise NoActiveRequests("No active requests for the elevator")
