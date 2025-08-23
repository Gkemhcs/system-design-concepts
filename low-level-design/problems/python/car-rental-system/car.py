from abc import ABC,abstractmethod
from car_types import CarType
from car_status import CarStatus
from datetime import date 

class Car(ABC):
    def __init__(self,vehicle_id:str,price_per_day:float,model:str,car_type:CarType):
        self._vehicle_id:str=vehicle_id
        self._price_per_day=price_per_day
        self.model=model 
        self.car_type=car_type
        self._status=CarStatus.AVAILABLE
       
    
    def get_price_per_day(self)->float:
        return self._price_per_day
    
    def get_car_type(self)->CarType:
        return self.car_type
    def is_available(self)->bool:
        return self._status==CarStatus.AVAILABLE
    def get_model(self)->str:
        return self.model
    def get_vehicle_id(self)->str:
        return self._vehicle_id

    def book_car(self):
        self._status=CarStatus.PENDING
    def confirm_booking(self):
        
        self._status=CarStatus.BOOKED
    def relase_car(self):
        self._status=CarStatus.AVAILABLE
    
