from abc import ABC,abstractmethod
from core_classes.show import Show 
from core_classes.user import User 
from core_classes.seat import Seat 

class ISeatLockProvider(ABC):

    @abstractmethod
    def lock_seats(self,show:Show,user:User,seats:list[Seat]):
        pass 

    @abstractmethod
    def unlock_seats(self,show:Show,user:User,seats:list[Seat]):
        pass 

    @abstractmethod
    def validate_lock(self,show:Show,seat:Seat,user:User)->bool:
        pass 

    @abstractmethod
    def get_locked_seats(self,show:Show)->list[Seat]:
        pass 

    @abstractmethod
    def are_seats_locked_by_others(self,show:Show,seats:list[Seat],user:User):
        pass 

    @abstractmethod
    def validate__seat_locks_not_expired(self,show:Show,seats:list[Seat]):
        pass 