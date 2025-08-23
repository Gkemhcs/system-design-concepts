from reservation import Reservation
from car import Car 
from user import User 
from datetime import date
from rental_store import RentalStore
from errors import ReservationNotFoundError

class ReservationManager:

    def __init__(self):
        self._reservations:dict[int,Reservation]={}
        self._next_reservation_id:int=1  
    def add_reservation(self,car:Car,user:User,pickup_date:date,
                        return_date:date,pickup_store:RentalStore,
                        return_store:RentalStore,price:float)->Reservation:
        reservation=Reservation(
            car,
            user,
            self._next_reservation_id,
            price,
            pickup_date,
            return_date,
            pickup_store,
            return_store,
        )
        
        self._reservations[self._next_reservation_id]=reservation
        print(f"adding reservation {reservation.get_reservation_id()}")
        self._next_reservation_id+=1
        return reservation
    def start_reservation(self,reservationID:int):
        if reservationID not in self._reservations:
            raise ReservationNotFoundError("the reservation is not found make sure to pass the correct reservation_id")
        else:    
            reservation=self._reservations[reservationID]
            print(f"starting reservation {reservation.get_reservation_id()}")
            reservation.start_rent()
    def get_reservation(self,reservationID:int)->Reservation:
        if reservationID not in self._reservations:
            raise ReservationNotFoundError("the reservation is not found make sure to pass the correct")
        return self._reservations[reservationID]
    def confirm_reservation(self,reservationID:int):
        if reservationID not in self._reservations:
            raise ReservationNotFoundError("the reservation is not found make sure to pass the correct")
        else:
            print(f"confirming reservation {reservationID}")
            reservation=self._reservations[reservationID]
            reservation.confirm_rent()
    def complete_reservation(self,reservationID:int):

        if reservationID not in self._reservations:
            raise ReservationNotFoundError("the reservation is not found make sure to pass the correct reservation_id")
        else:    
            
            reservation=self._reservations[reservationID]
            if reservation._pick_up_store!=reservation._return_store:
                print("car is being returned to a different location")
                pick_up_store=reservation.get_pickup_store()
                return_store=reservation.get_return_store()
                print(f"the car will be sent to its original rental store {pick_up_store.get_name()} from the returned place {return_store.get_name()}")
            reservation.complete_rent()
    def get_reservations(self)->list[Reservation]:
        return list(self._reservations.values())
    def get_reservation_by_id(self,reservationID:int)->Reservation:
        return self._reservations.get(reservationID,None)
    def cancel_reservation(self,reservationID:int):
        if reservationID not in self._reservations:
            raise ReservationNotFoundError("the reservation is not found make sure to pass the correct reservation_id")
        else:    

            reservation=self._reservations[reservationID]
            reservation.cancel_rent()
