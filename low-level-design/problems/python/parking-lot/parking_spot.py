from vehicle_size import VehicleSize
from vehicle import Vehicle
from threading import Lock 
class ParkingSpot:
    def __init__(self,spotID:str,vehicleSize:VehicleSize):
        self._spotID=spotID
        self._isOccupied=False 
        self._vehicle=None
        self.vehicleSize=vehicleSize
        self._lock=Lock()
    def isOccupied(self):
        return self._isOccupied
    def park(self, vehicle: Vehicle):
        with self._lock:
            self._isOccupied = True
            self._vehicle = vehicle
            
    def remove(self):
        with self._lock:
            print(f"Spot {self._spotID} is now free")
            self._isOccupied = False
            self._vehicle = None
    def getSpotID(self):
        return self._spotID
    def getVehicle(self):
        return self._vehicle


