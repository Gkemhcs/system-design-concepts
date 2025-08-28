from core_classes.booking import Booking 
from core_classes.booking_status import BookingStatus
from .payment_service import PaymentService
from core_classes.show import Show
from core_classes.user import User 
from core_classes.seat import Seat 
from strategies.iseat_lock_provider import ISeatLockProvider
from strategies.pricing_strategy import PricingStrategy


class BookingService:

    def __init__(self,payment_service:PaymentService,seat_lock_provider:ISeatLockProvider,pricing_strategy:PricingStrategy):
        self.__bookings:dict[int,Booking]={}
        self.__booking_counter=1
        self.__payment_service=payment_service
        self.__lock_provider=seat_lock_provider
        self.__pricing_strategy=pricing_strategy

    
    def calculate_amount(self,seats:list[Seat])->float:
        return self.__pricing_strategy.calculate_price(seats)

    
    def create_booking(self,show:Show,user:User,seats:list[Seat])->Booking:
        booking_id=self.__booking_counter
        amount=self.calculate_amount(seats)
        self.__lock_provider.lock_seats(show,user,seats)
        booking=Booking(booking_id,show,user,amount,seats)
        self.__bookings[booking_id]=booking 
        self.__booking_counter+=1
        print(f"booking of id {booking_id} got created for user {user.get_name()} ")
        return booking
    def get_show_bookings(self,show:Show)->list[Booking]:
        return [booking for booking in self.__bookings.values() if booking.get_show()==show]
    
    def get_booked_seats(self,show:Show)->list[Seat]:
        bookings=self.get_show_bookings(show)
        booked_seats=[]
        for booking in bookings:
            # Only consider confirmed bookings for seat availability
            if booking.get_status() == BookingStatus.CONFIRMED:
                booked_seats.extend(booking.get_seats())
        return booked_seats

    def confirm_booking(self,booking_id:int)->bool:
        if booking_id not in self.__bookings:
            raise Exception("sorry the booking you are trying to access doesn't exist")
        else: 
            booking=self.__bookings[booking_id]
            if booking.get_status()!=BookingStatus.PENDING:
                raise Exception(f"cannot confirm booking as current status is {booking.get_status().value}")

            else:
                show=booking.get_show()
                seats=booking.get_seats()
                user=booking.get_user()
                # for seat in seats:
                #     if not self.__lock_provider.validate_lock(show,seat,user):
                #         booking.expire_booking()
                #         self.__lock_provider.unlock_seats(show,user,seats)
                #         raise Exception(f"cannot confirm booking as seat {seat.get_id()} is not locked by user {user.get_id()} or lock has expired")
                if self.__lock_provider.are_seats_locked_by_others(show,seats,user):
                    booking.expire_booking()
                    self.__lock_provider.unlock_seats(show,user,seats)
                    raise Exception("the seats are already booked by someone else")
                elif self.__lock_provider.validate__seat_locks_not_expired(show,seats):
                    booking.expire_booking()
                    self.__lock_provider.unlock_seats(show,user,seats)
                    raise Exception("the timeout reached so please select again")
                amount=booking.get_amount()
                payment_successful=self.__payment_service.process_payment(amount)

                if payment_successful:
                    booking.confirm_booking()
                    # Don't unlock seats after confirmation - they should remain locked for the confirmed booking
                    print(f"booking confirmed for {booking_id}")
                    self.__lock_provider.unlock_seats(show,user,seats)
                    return True
                else:
                    return False
    def cancel_booking(self,booking_id:int)->bool:
        if booking_id not in self.__bookings:
            raise Exception("sorry the booking you are trying to access doesn't exist")
        else: 
            booking=self.__bookings[booking_id]
            if booking.get_status()!=BookingStatus.CONFIRMED:
                raise Exception(f"cannot cancel booking as current status is {booking.get_status().value}")
            else:
                booking.cancel_booking()
                print(f"booking cancelled for {booking_id}")
                return True
