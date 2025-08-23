from enum import Enum 


class ReservationStatus(Enum):

    PENDING="pending"
    BOOKED="booked"
    STARTED="started"
    COMPLETED="completed"
    CANCELLED="cancelled"
    