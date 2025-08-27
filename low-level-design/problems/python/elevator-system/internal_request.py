from elevator_request import ElevatorRequest

class InternalRequest(ElevatorRequest):

    def __init__(self,floor:int):
        super().__init__(floor=floor)