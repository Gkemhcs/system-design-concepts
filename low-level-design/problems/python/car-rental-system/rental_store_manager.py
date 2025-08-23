from rental_store import RentalStore
from errors import InvalidRentalStoreError
from car_types import CarType
from car import Car
class RentalStoreManager:

    def __init__(self):
        self._stores:dict[int,RentalStore]={}
        self._nextStoreInt=1
    def create_store(self,location:str,name:str)->RentalStore:
        print(f"creating rental store in {location} with name {name}")
        store=RentalStore(location,name,self._nextStoreInt)
        self._stores[self._nextStoreInt]=store
        self._nextStoreInt+=1
        return store 
    def get_store(self,rentalStoreID:int)->RentalStore:
        if self._stores.get(rentalStoreID,None) is None:
            raise InvalidRentalStoreError("the rental store you are trying to access not exist")
        return self._stores.get(rentalStoreID,None)
    def remove_store(self,rentalStoreID:int):
        if rentalStoreID not in self._stores:
            raise InvalidRentalStoreError("sorry the rental store you are trying to delete not exist")
        else:
            print(f"removing rental store {rentalStoreID}")
            del self._stores[rentalStoreID]
    def  can_book(self,pickupStoreID:int, returnStoreID:int,car_type:CarType)->bool:
        if pickupStoreID not in self._stores:
            raise InvalidRentalStoreError("pickup rental location not available try using a valid rental store")
        if  returnStoreID not in self._stores:
            raise InvalidRentalStoreError("return rental store not available try using a another valid rental store")
        pickupStore=self._stores.get(pickupStoreID,None)
        if pickupStore is not None:
            return pickupStore.is_car_available(car_type=car_type)
        return False 
    def book_car(self,pickupStoreID:int,car_type:CarType)->Car:
        rentalStore=self._stores.get(pickupStoreID,None)
        if rentalStore  is not None:
        
            return rentalStore.book_car(car_type=car_type)
    def confirm_booking(self,car:Car,pick_up_store_id:int):
        rentalStore=self._stores.get(pick_up_store_id,None)
        if rentalStore is not None:
           
            rentalStore.confirm_car(car)

    def release_car(self,pickupStoreID:int,car:Car):
        rentalStore=self._stores.get(pickupStoreID,None)
        if rentalStore is not None:
            rentalStore.release_car(car)
    