from car import Car
from car_types import CarType

class Luxury(Car):
    def __init__(self, model, vehicle_id):
        super().__init__(vehicle_id, 100.0, model, CarType.LUXURY)
