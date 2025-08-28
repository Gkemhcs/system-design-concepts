from enum import Enum 


class BookingStatus(Enum):

    CONFIRMED="CONFIRMED"
    CANCELLED="CANCELLED"
    PENDING="PENDING"
    EXPIRED="EXPIRED"
