from vehicle import Vehicle
from parking_spot import ParkingSpot
import time 

class ParkingTicket:
    def __init__(self,vehicle:Vehicle,parking_spot:ParkingSpot):
        self._is_active=True 
        self._vehicle=vehicle
        self._spot=parking_spot
        self.startTime=time.time()
        self.endTime=None
    def is_active(self)->bool:
        return self._is_active
    def getVehicle(self)->Vehicle:
        return self._vehicle
    def getSpot(self)->ParkingSpot:
        return self._spot
    def getStartTime(self)->float:
        return self.startTime
    def getEndTime(self)->float:
        return self.endTime
    def setEndTime(self):
        self.endTime=time.time()
    def setInactive(self):
        self._is_active=False 

