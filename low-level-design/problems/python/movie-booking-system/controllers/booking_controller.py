from service.booking_service import BookingService
from service.theatre_service import TheatreService
from core_classes.show import Show 
from core_classes.user import User 
from core_classes.seat import Seat  
from core_classes.booking import Booking 


class BookingController:

    def __init__(self,booking_service:BookingService,theatre_service:TheatreService):

        self.__booking_service=booking_service
        self.__theatre_service=theatre_service
    def create_booking(self,show:Show,user:User,seat_ids:list[int])->Booking:
        seats:list[Seat]=[]

        for seat_id in seat_ids:
            seat=self.__theatre_service.get_seat_in_screen(show.get_screen().get_id(),seat_id)
            if seat:
                seats.append(seat)
        booked_seats=self.check_seats_booked_or_not(seats,show)
        if booked_seats:
            raise Exception(f"sorry the seats you are trying to book are already booked by other users{booked_seats}")
        else:
            return self.__booking_service.create_booking(show,user,seats)
    def check_seats_booked_or_not(self,seats:list[Seat],show:Show)->list[int]:

        already_booked_seats=self.get_booked_seats(show)
        booked_seats=[]
        for seat in seats:
            if seat in already_booked_seats:
                booked_seats.append(seat.get_id())
        return booked_seats
    def get_show_bookings(self,show:Show)->list[Booking]:
       return self.__booking_service.get_show_bookings(show)
    
    def get_booked_seats(self,show:Show)->list[Seat]:
        return self.__booking_service.get_booked_seats(show)
    
    def confirm_booking(self,booking_id:int)->bool: 
        return self.__booking_service.confirm_booking(booking_id)
    def cancel_booking(self,booking_id:int)->bool:
        return self.__booking_service.cancel_booking(booking_id)
    
