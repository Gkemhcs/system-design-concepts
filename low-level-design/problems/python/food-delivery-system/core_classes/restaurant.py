from .location import Location
from .food_item import FoodItem

from threading import Lock
class Restaurant:

    def __init__(self,id:int,name:str,location:Location):
        self.__id=id 
        self.__name=name 
        self.__location=location
        self.__menu:list[FoodItem]=[]

    def get_location(self)->Location:
        return self.__location
    def get_id(self)->int:
        return self.__id
    def get_name(self)->str:
        return self.__name
    def get_name(self)->str:
        return self.__name
    def add_food_item(self,food_item:FoodItem):
        self.__menu.append(food_item)
    def get_menu(self)->list[FoodItem]:
        return self.__menu
    def check_for_item(self,item:FoodItem):
        for food_item in self.__menu:
            if food_item==item:
                return True 
        return False
    def get_item_by_name(self,name:str)->FoodItem:
        for food_item in self.__menu:
            if food_item.get_name()==name:
                return food_item
        return None

    