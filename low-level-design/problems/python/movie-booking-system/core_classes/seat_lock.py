from core_classes.user import User 
from core_classes.seat import Seat
from core_classes.show import Show 
from datetime import datetime,timedelta 

class SeatLock:

    def __init__(self,user:User,show:Show,seat:Seat,locked_time:datetime,lock_timeout:60):
        self.__seat=seat
        self.__show=show 
        self.__locked_by:User=user 
        self.__locked_time=locked_time 
        self.__lock_timeout=lock_timeout 
    def is_expired(self)->bool:
        expiry_time= self.__locked_time+timedelta(seconds=self.__lock_timeout)
        return expiry_time<datetime.now()

    def locked_by(self)->User:
        return self.__locked_by
    def get_seat(self)->Seat:
        return self.__seat
    def get_show(self)->Show:
        return self.__show 
    