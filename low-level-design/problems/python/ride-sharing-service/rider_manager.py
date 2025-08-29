from core_classes.rider import Rider 
from core_classes.rider_type import RiderType

class RiderManager:

    def __init__(self):
        self.__riders:dict[int,Rider]={}
        self.rider_id_counter=1
    def create_rider(self,name:str,email:str,rider_type:RiderType=RiderType.REGULAR)->Rider:
        rider_id=self.rider_id_counter
        
        rider=Rider(rider_id,name,email,rider_type)
        self.__riders[rider_id]=rider 
        self.rider_id_counter+=1
        print(f"rider of name {name} created with id {rider_id}")
        return rider
    def get_rider(self,rider_id:int)->Rider:
        return self.__riders.get(rider_id,None)