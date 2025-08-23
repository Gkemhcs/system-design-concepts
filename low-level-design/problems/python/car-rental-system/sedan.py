from car import Car 
from car_types import CarType

class Sedan(Car):
    def __init__(self, model, vehicle_id):
        super().__init__(vehicle_id, 50.0, model, CarType.SEDAN)