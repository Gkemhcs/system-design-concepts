from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from parking_ticket import ParkingTicket

class ParkingFloor:
    def __init__(self,floorID:str,parking_spots:list[ParkingSpot]):
        self._floorID=floorID
        self._parking_spots=parking_spots
    def addSpot(self, spot: ParkingSpot):
        self._parking_spots.append(spot)
        print(f"Spot {spot.getSpotID()} added to floor {self._floorID}")
    def checkAvailableSpots(self,size:VehicleSize):

        for spot in self._parking_spots:
            if spot.vehicleSize==size and not spot.isOccupied():
                return spot
        return None
    def getFloorID(self):
        return self._floorID
    def getParkingSpots(self):
        return self._parking_spots
    def parkVehicle(self, vehicle) -> ParkingTicket:
        spot = self.checkAvailableSpots(vehicle.get_vehicle_size())
        if spot:
            spot.park(vehicle)
            print(f"Vehicle {vehicle.get_license_plate()} parked successfully at spot {spot.getSpotID()} on floor {self._floorID}")
            ticket = ParkingTicket(vehicle, spot)
            return ticket
        else:
            
            return None
    def removeVehicle(self, vehicle):
        for spot in self._parking_spots:
            if spot.getVehicle() == vehicle:
                spot.remove()
                print(f"Vehicle {vehicle.get_license_plate()} removed from spot {spot.getSpotID()} on floor {self._floorID}")
                break