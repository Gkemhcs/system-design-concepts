from core_classes.driver import Driver
from core_classes.driver_status import DriverStatus
from core_classes.location import Location


class DriverManager:

    def __init__(self):
        self.__drivers:dict[int,Driver]={}
        self.driver_id_counter=1
    def create_driver(self,name:str,email:str,location:Location,driver_status:DriverStatus=DriverStatus.AVAILABLE)->Driver:
        driver_id=self.driver_id_counter
        
        driver=Driver(driver_id,name,email,driver_status,location)
        self.__drivers[driver_id]=driver 
        self.driver_id_counter+=1
        print(f"driver of name {name} created with id {driver_id}")
        return driver
    def get_driver(self,driver_id:int)->Driver:
        return self.__drivers.get(driver_id,None)
    def get_drivers(self)->list[Driver]:
        return list(self.__drivers.values())
    def get_available_drivers(self)->list[Driver]:
        return [driver for driver in self.__drivers.values() if driver.get_status()==DriverStatus.AVAILABLE]

