from .show import Show 
from .seat import Seat 
from .booking_status import BookingStatus
from .user import User 
class Booking:


    def __init__(self,id:id,show:Show,user:User,amount:float,seats:list[Seat]):

        self._id=id 
        self.__show=show 
        self.__seats=seats 
        self.__amount=amount
        self.__user=user
        self.__status=BookingStatus.PENDING
    def get_id(self)->int:
        return self._id 
    
    def get_show(self)->Show:
        return self.__show
    def get_seats(self)->list[Seat]:
        return self.__seats
    def get_user(self)->User:
        return self.__user

    def get_status(self)->BookingStatus:
        return self.__status 
    def get_amount(self)->float:
        return self.__amount
    def confirm_booking(self):
        if self.__status!=BookingStatus.PENDING:
            raise Exception(f"cannot confirm booking as current status is {self.__status.value}")
        else:
            self.__status=BookingStatus.CONFIRMED   
    def cancel_booking(self):
        self.__status=BookingStatus.CANCELLED
    
    def expire_booking(self):
        self.__status=BookingStatus.EXPIRED