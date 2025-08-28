from service.booking_service import BookingService
from service.theatre_service import TheatreService
from core_classes.seat import Seat 
from core_classes.show  import Show 

class SeatAvailabilityService:


    def __init__(self,booking_service:BookingService,theatre_service:TheatreService):
        self.__booking_service=booking_service
        self.__theatre_service=theatre_service
    
    def get_all_seats(self,screen_id:int)->list[Seat]:
        seats=self.__theatre_service.get_all_seats(screen_id)
        return seats
    
    def get_available_seats(self,show:Show)->list[Seat]:
        all_seats=self.get_all_seats(show.get_screen().get_id())
        
        booked_seats=self.__booking_service.get_booked_seats(show)
        
        # Get IDs of booked seats for comparison
        booked_seat_ids = {seat.get_id() for seat in booked_seats}
        
        # Filter out booked seats
        available_seats = [seat for seat in all_seats if seat.get_id() not in booked_seat_ids]
        
        return available_seats 
        
