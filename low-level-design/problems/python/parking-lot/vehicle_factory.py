from vehicle import Vehicle
from car import Car
from bike import Bike
from truck import Truck
from errors import InvalidVehicleTypeError
class VehicleFactory:

    @staticmethod 
    def create_vehicle(vehicle_type:str,license_number:str)->Vehicle:
        if vehicle_type=="car":
            return Car(license_number)
        elif vehicle_type=="bike":
            return Bike(license_number) 
        elif vehicle_type=="truck":
            return Truck(license_number)
        else:
            raise InvalidVehicleTypeError("Invalid vehicle type")

