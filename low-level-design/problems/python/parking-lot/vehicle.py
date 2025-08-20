from vehicle_size import VehicleSize

class Vehicle:
    def __init__(self, license_number: str, vehicle_size: VehicleSize):
        self._license_number = license_number
        self.vehicle_size = vehicle_size
        

    def get_license_plate(self) -> str:
        return self._license_number

    def get_vehicle_size(self) -> VehicleSize:
        return self.vehicle_size
    
