from .seat_type import SeatType


class Seat:

    def __init__(self,id:int,row:int,col:int,seat_type:SeatType):

        self._id=id 
        self.__type=seat_type
        self.__row=row 
        self.__col=col 
    def get_id(self)->int:
        return self._id 
    def get_seat_type(self)->SeatType:
        return self.__type 
    def get_row(self)->int:
        return self.__row 
    def get_col(self)->int:
        return self.__col 
    
    def __str__(self)->str:
        return f"Row:{self.__row}, Col:{self.__col}, Id:{self._id}, Type:{self.__type}"