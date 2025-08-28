from strategies.iseat_lock_provider import ISeatLockProvider
from core_classes.seat import Seat 
from core_classes.user import User 
from core_classes.show import Show 
from core_classes.seat_lock import SeatLock

from datetime import datetime 

class SeatLockProvider(ISeatLockProvider):

    def __init__(self,timeout_in_seconds:int=60):

        self.__timeout_in_seconds=timeout_in_seconds
        self.__locked_seats:dict[Show,dict[Seat,SeatLock]]={}
    
    def lock_seats(self,show:Show,user:User,seats:list[Seat]):
        
        if show not in self.__locked_seats:
            self.__locked_seats[show] = {}
        
        show_lock=show.get_lock()
        
        with show_lock:
            locked_seats=self.__locked_seats.get(show,{})
            for seat in seats:
                if seat in locked_seats:
                    seat_lock=locked_seats.get(seat,None)

                    if seat_lock and seat_lock.locked_by()!=user and not seat_lock.is_expired():
                        raise Exception(f"cannot lock seat{seat.get_id()}  as it is already locked by someone else")

            for seat in seats:
                locked_seats[seat]=SeatLock(user,show,seat,datetime.now(),self.__timeout_in_seconds)
                print(f"successfully locked the seat {seat.get_id()}")
    def unlock_seats(self,show:Show,user:User,seats:list[Seat]):
        
        show_lock=show.get_lock()

        with show_lock:
            locked_seats=self.__locked_seats.get(show,{})
            for seat in seats:
                if seat in locked_seats and locked_seats.get(seat,None).locked_by()==user:
                    del locked_seats[seat]
                    print(f"successfully unlocked the seat {seat.get_id()}")
    
    def validate_lock(self,show:Show,seat:Seat,user:User)->bool:
        
        if show not in self.__locked_seats:
            return False 
        else:
            show_lock=show.get_lock()
            with show_lock:
                locked_seats=self.__locked_seats.get(show,None)
                if seat in locked_seats:
                    seat_lock=locked_seats.get(seat,None)
                    if seat_lock and seat_lock.locked_by()==user and not seat_lock.is_expired():
                        return True 
        return False

    def get_locked_seats(self,show:Show)->list[Seat]:
        if show not in self.__locked_seats:
            return []
        else:
            show_lock=show.get_lock()
            seats:list[Seat]=[]
            with show_lock:
                locked_seats=self.__locked_seats.get(show,None)
                if locked_seats:
                    seats.extend(locked_seats.keys())
        return seats

    def are_seats_locked_by_others(self,show:Show,seats:list[Seat],user:User):
        show_lock=show.get_lock()
        with show_lock:
            locked_seats=self.__locked_seats.get(show,{})
            for seat in seats:
                if seat in locked_seats:
                    seat_lock=locked_seats.get(seat,None)
                    if seat_lock and seat_lock.locked_by()!=user:
                        return True 
        return False 
    def validate__seat_locks_not_expired(self,show:Show,seats:list[Seat]):
        show_lock=show.get_lock()
        with show_lock: 
            locked_seats=self.__locked_seats.get(show,{})
            for seat in seats:
                if seat in locked_seats:
                    seat_lock=locked_seats.get(seat,None)
                    if seat_lock and seat_lock.is_expired():
                        return True 
        return False 