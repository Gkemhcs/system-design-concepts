from reservation_manager import ReservationManager
from payment_processor import PaymentProcessor
from payment_strategy import PaymentStrategy 
from rental_store_manager import RentalStoreManager
from user_manager import UserManager
from user import User 
from rental_store import RentalStore
from reservation import Reservation
from errors import NoCarsAvailableError 
from car_types import CarType
from datetime import date


class RentalSystem:

    def __init__(self):
        self._reservation_manager=ReservationManager()
        self._payment_processor=PaymentProcessor()
        self._rental_store_manager=RentalStoreManager()
        self._user_manager=UserManager()

    def create_user(self,name:str,location:str)->User:
        user=self._user_manager.create_user(name,location)
        print(f"✅ User '{name}' created successfully in {location}")
        return user 
        
    def create_rental_store(self,name:str,location:str)->RentalStore:
        store = self._rental_store_manager.create_store(location,name)
        print(f"🏪 Rental store '{name}' created successfully in {location}")
        return store
        
    def remove_user(self,userID:int):
        self._user_manager.delete_user(userID)
        print(f"🗑️ User with ID {userID} removed successfully")
        
    def remove_rental_store(self,storeID):
        self._rental_store_manager.remove_store(storeID)
        print(f"🏪 Store with ID {storeID} removed successfully")
        
    def check_cars_available(self,pickupStoreID:int,returnStoreID:int,car_type:CarType)->bool:
        return self._rental_store_manager.can_book(pickupStoreID,returnStoreID,car_type)
        
    def reserve_car(self,pickupStoreID:int,returnStoreID:int,user:User,car_type:CarType,pickup_date:date,return_date:date)->Reservation:
        if not self.check_cars_available(pickupStoreID,returnStoreID,car_type):
            raise NoCarsAvailableError(f"sorry no cars of type {car_type.value} available at this time, check after sometime")
        else:
            pickup_store=self._rental_store_manager.get_store(pickupStoreID)
            return_store=self._rental_store_manager.get_store(returnStoreID)
            
            car=self._rental_store_manager.book_car(pickupStoreID,car_type) 
            price=(return_date-pickup_date).days * car.get_price_per_day()
            
            reservation=self._reservation_manager.add_reservation(car,user,pickup_date,return_date,pickup_store,return_store,price)
            self._user_manager.add_reservation(reservation)
            
            print(f"🚗 Car '{car.get_model()}' ({car_type.value}) reserved successfully!")
            print(f"   📅 Pickup: {pickup_date} | Return: {return_date}")
            print(f"   💰 Total Price: ${price:.2f}")
            print(f"   🆔 Reservation ID: {reservation.get_reservation_id()}")
            
            return reservation
            
    def confirm_rental(self,reservationID:int,pick_up_store_id:int,paymentStrategy:PaymentStrategy):
        reservation=self._reservation_manager.get_reservation(reservationID)
        amount_to_be_paid=reservation.get_price()
        
        print(f"💳 Processing payment for reservation {reservationID}...")
        if self._payment_processor.process_payment(amount_to_be_paid,paymentStrategy):
            print(f"✅ Payment successful! Amount: ${amount_to_be_paid:.2f}")
            self._reservation_manager.confirm_reservation(reservationID)
            self._rental_store_manager.confirm_booking(reservation.get_car(),pick_up_store_id)
            print(f"🎉 Rental confirmed! Car '{reservation.get_car().get_model()}' is ready for pickup")
        else:
            print("❌ Payment failed! Cancelling reservation...")
            self._reservation_manager.cancel_reservation(reservationID)
            self._rental_store_manager.release_car(pick_up_store_id,reservation.get_car())
            
    def start_rental(self,reservationID:int):
        reservation = self._reservation_manager.get_reservation(reservationID)
        self._reservation_manager.start_reservation(reservationID)
        print(f"🚀 Rental started! Car '{reservation.get_car().get_model()}' is now in use")
        
    def get_reservations(self)->list[Reservation]:
        return self._reservation_manager.get_reservations()
        
    def complete_rental(self,reservationID:int):
        reservation = self._reservation_manager.get_reservation(reservationID)
        self._reservation_manager.complete_reservation(reservationID)
        reservation=self._reservation_manager.get_reservation(reservationID)
        self._rental_store_manager.release_car(reservation.get_return_store().get_store_id(),reservation.get_car())
        print(f"🏁 Rental completed! Car '{reservation.get_car().get_model()}' returned successfully")
        
    def cancel_rental(self,reservationID:int):
        reservation = self._reservation_manager.get_reservation(reservationID)
        self._reservation_manager.cancel_reservation(reservationID)
        reservation=self._reservation_manager.get_reservation(reservationID)
        self._rental_store_manager.release_car(reservation.get_return_store().get_store_id(),reservation.get_car())
        print(f"❌ Rental cancelled! Car '{reservation.get_car().get_model()}' is available again")
