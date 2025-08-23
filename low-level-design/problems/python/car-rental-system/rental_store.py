from car import Car 
from car_types import CarType
from errors import NoCarsAvailableError ,CarIsAlreadyAvailableError
class RentalStore:
    def __init__(self,location:str,name:str,storeID:int):
        self._storeID=storeID
        self._name=name
        self._location=location 
        self._available_cars:list[Car]=[]
    def get_name(self)->str:
        return self._name
    def add_car(self,car:Car):
        self._available_cars.append(car)
    def remove_car(self,car:Car):
        self._available_cars.remove(car)
    def is_car_available(self,car_type:CarType)->bool:
        for car in self._available_cars:
            if car.get_car_type()==car_type  and car.is_available():
                return True 
        return False 
    def book_car(self,car_type:CarType):
        for car in self._available_cars:
            if car.get_car_type()==car_type and car.is_available():
                car.book_car()
                return car 
        raise NoCarsAvailableError(f"no cars  available of type{car_type.value} at this time")
    def confirm_car(self,car_to_be_confirmed:Car):
        for car in self._available_cars:
            if car==car_to_be_confirmed:
              
                car.confirm_booking()
                return
       
    def release_car(self,car_to_be_released:Car):
        for car in self._available_cars:
            if car==car_to_be_released:
                if car.is_available():
                    raise CarIsAlreadyAvailableError("the car cannot be relased as it in't booked by anyone")
                else:
                    car.relase_car()
                    
    def get_location(self)->str:
        return self._location
    def get_store_id(self)->int:
        return self._storeID