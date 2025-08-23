from car import Car 
from luxury import Luxury
from sedan import Sedan
from suv import SUV

class CarFactory:

    @staticmethod
    def create_car(car_type:str, model:str, vehicle_id:str) -> Car:
        if car_type.lower() == "sedan":
            print(f"creating sedan of model{model} with vehicle id {vehicle_id}")
            return Sedan(model, vehicle_id)
        elif car_type.lower() == "luxury":
            print(f"creating luxury car of model {model} with vehicle id {vehicle_id}")
            return Luxury(model, vehicle_id)
        elif car_type.lower() == "suv":
            print(f"creating suv of model {model} with vehicle id {vehicle_id}")
            return SUV(model, vehicle_id)
        else:
            raise ValueError(f"Unknown car type: {car_type}")   