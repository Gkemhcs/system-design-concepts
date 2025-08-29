from enum import Enum 


class RideStatus(Enum):

    CREATED="CREATED"
    ACCEPTED="ACCEPTED"
    STARTED="STARTED"
    COMPLETED="COMPLETED"
    CANCELLED="CANCELLED"