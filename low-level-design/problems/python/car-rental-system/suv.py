from car import Car
from car_types import CarType

class SUV(Car):
    def __init__(self, model, vehicle_id):
        super().__init__(vehicle_id, 70.0, model, CarType.SUV)

