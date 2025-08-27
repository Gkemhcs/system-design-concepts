from elevator_request import ElevatorRequest
from direction import Direction 
class ExternalRequest(ElevatorRequest):

    def __init__(self,floor,direction:Direction):
        super().__init__(floor=floor,direction=direction)
        