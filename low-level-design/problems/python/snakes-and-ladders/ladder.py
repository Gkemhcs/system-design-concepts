from entity import Entity
from errors import IllegalArgumentExceptionError

class Ladder(Entity):

    def __init__(self,start:int,end:int):
        if start>end:
            raise IllegalArgumentExceptionError("sorry for ladder the end always should be strictly greater than start")
        super().__init__(start,end)