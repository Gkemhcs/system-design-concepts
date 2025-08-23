
from __future__ import annotations
from typing import TYPE_CHECKING
from car import Car 
from rental_store import RentalStore
from reservation_status import ReservationStatus
from datetime import date

if TYPE_CHECKING:
    from user import User

class Reservation:

    def __init__(self,car:Car,user:User,reservation_id:int,price:float,pickup_date:date,return_date:date,pickup_store:RentalStore,return_store:RentalStore):
        self._reservation_id=reservation_id
        self._car=car
        self._pickup_date=pickup_date
        self._user=user
        self._return_date=return_date
        self._pick_up_store=pickup_store
        self._return_store=return_store
        self._status=ReservationStatus.PENDING
        self._price=price
    def get_pickup_store(self)->RentalStore:
        return self._pick_up_store
    def get_return_store(self)->RentalStore:
        return self._return_store
    def get_reservation_id(self)->int:
        return self._reservation_id
    def get_price(self)->float:
        return self._price
    def confirm_rent(self):
        self._status=ReservationStatus.BOOKED
    def  start_rent(self):
        self._status=ReservationStatus.STARTED
    def complete_rent(self):
        self._status=ReservationStatus.COMPLETED
    def get_car(self)->Car:
        return self._car
    def cancel_rent(self):
        self._status=ReservationStatus.CANCELLED
    def get_reservation_status(self)->ReservationStatus:
        return self._status