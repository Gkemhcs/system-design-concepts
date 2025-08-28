from service.theatre_service import TheatreService
from service.booking_service import BookingService
from service.movie_service import MovieService
from service.payment_service import PaymentService
from service.seat_availability_service import SeatAvailabilityService
from service.show_service import ShowService
from core_classes.user import User 

from controllers.booking_controller import BookingController
from controllers.movie_controller import MovieController
from controllers.show_controller import ShowController
from controllers.theatre_controller import TheatreController

from strategies.concrete_lock_strategies.seat_lock_provider import SeatLockProvider
from strategies.concrete_strategies.upi_payment_strategy import UpiPaymentStrategy
from strategies.concrete_strategies.simple_pricing_strategy import SimplePricingStrategy

from core_classes.seat_type import SeatType
from core_classes.screen_type import ScreenType
from datetime import datetime 

import threading
import time
def populate_seats(screen_id:int,theatre_controller:TheatreController):
    for i in range(1,7):
        if i<=4:
            seat_type=SeatType.REGULAR
        else:
            seat_type=SeatType.PREMIUM
        for j in range(10):
            theatre_controller.create_seat_in_screen(screen_id,seat_type,i,j)

def main():
    theatre_service=TheatreService()
    movie_service=MovieService()
    payment_service=PaymentService(UpiPaymentStrategy(upi_id="koti@ybl"))
    seat_lock_provider=SeatLockProvider(2)
    pricing_strategy=SimplePricingStrategy()
    booking_service=BookingService(payment_service,seat_lock_provider,pricing_strategy)
    seat_availability_service=SeatAvailabilityService(booking_service,theatre_service)
    show_service=ShowService(seat_availability_service)
    

    booking_controller=BookingController(booking_service,theatre_service)
    movie_controller=MovieController(movie_service)
    show_controller=ShowController(show_service)
    theatre_controller=TheatreController(theatre_service)

    user1=User(1,"koti","koti@gmail")
    user2=User(2,"eswar","eswar@gmail")

    movie1= movie_controller.create_movie("kalki",180)
    movie2=movie_controller.create_movie("peddi",170)
    theatre1=theatre_controller.create_theatre("sandya theatre","bengaluru")
    theatre2=theatre_controller.create_theatre("pvr_cinemas","bengaluru")

    screen1_1=theatre_controller.create_screen_in_theatre(theatre1,ScreenType.DOLBY)
    screen2_1=theatre_controller.create_screen_in_theatre(theatre1,ScreenType.IMAX)

    screen1_2=theatre_controller.create_screen_in_theatre(theatre2,ScreenType.THREE_D)
    screen2_2=theatre_controller.create_screen_in_theatre(theatre2,ScreenType.IMAX)

    populate_seats(screen1_1,theatre_controller)
    populate_seats(screen2_1,theatre_controller)
    populate_seats(screen1_2,theatre_controller)
    populate_seats(screen2_2,theatre_controller)
    show_1=show_controller.create_show(screen1_1,movie1,datetime.now(),180)
    show_2=show_controller.create_show(screen2_1,movie2,datetime.now(),170)
   
    for seat in show_controller.get_available_seats(show_1):
        print(seat)
    total_seats_before=show_controller.get_available_seats(show_1)
    seats=total_seats_before[0:5]+total_seats_before[-1:-6:-1]
    booking1=booking_controller.create_booking(show_1,user1,[1,2,3,51,52])
    booking_controller.confirm_booking(booking1.get_id())
    print("after booking")
    for booking in booking_controller.get_show_bookings(show_1):
        print(booking.get_user().get_name(),[str(seat) for seat in booking.get_seats()],booking.get_status().value)
    total_seats_after=show_controller.get_available_seats(show_1)
    for seat in total_seats_after:
        print(seat)
    print(len(total_seats_before),  len(total_seats_after))

    def user1_operation():
        try:
           
            booking2=booking_controller.create_booking(show_1,user1,[4,5,6,7,8 ])
            time.sleep(7)
            booking_controller.confirm_booking(booking2.get_id())
            print(f"booking successful for user {user1.get_name()}")
        except Exception as e:
            print(f"booking failed for user {user1.get_name()} due to {str(e)}")
    def user2_operation():
        try:
            time.sleep(3)

            booking3=booking_controller.create_booking(show_1,user2,[8,9,10])
        
            booking_controller.confirm_booking(booking3.get_id())
            
            booking_controller.cancel_booking(booking3.get_id())
            print(f"booking successful for user {user2.get_name()}")
        except Exception as e:
            print(f"booking failed for user {user2.get_name()} due to {str(e)}")
    

    thread1=threading.Thread(target=user1_operation)
    thread2=threading.Thread(target=user2_operation)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("after concurrent booking attempts")
    booking4=booking_controller.create_booking(show_1,user1,[8,9,10])
    booking_controller.confirm_booking(booking4.get_id())
    try:
     booking5=booking_controller.create_booking(show_1,user1,[11,12])
     time.sleep(4)
     booking_controller.confirm_booking(booking5.get_id())
    except Exception as e:
        print(e) 
   
    for booking in booking_controller.get_show_bookings(show_1):
        print(booking.get_id(),booking.get_status())
        for seat in booking.get_seats():
            print(seat)
    

if __name__=="__main__":
    main()