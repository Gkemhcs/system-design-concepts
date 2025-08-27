from entity import Entity 
from errors import IllegalArgumentExceptionError
class Snake(Entity):

        def __init__(self,start:int,end:int):
                if start<end:
                        raise IllegalArgumentExceptionError("sorry not a valid snake as start is always should be greater than end")
                super().__init__(start,end)