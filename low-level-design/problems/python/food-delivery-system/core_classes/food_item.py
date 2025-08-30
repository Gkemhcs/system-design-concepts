from __future__ import annotations
from .food_item_type import FoodItemType

class FoodItem:


    def __init__(self,id:int,name:str,price:float,food_item_type:FoodItemType):
        self.__id=id 
        self.__name=name 
        self.__price=price 
        self.__food_item_type=food_item_type 
    def get_name(self)->str:
        return self.__name 
    def get_price(self)->float:
        return self.__price 
    def get_food_item_type(self)->FoodItemType:
        return self.__food_item_type
    def change_price(self,price:float)->float:
        self.__price=price 
        return self.__price 
    def get_id(self)->int:
        return self.__id
    def __eq__(self,item:FoodItem)->bool:
        if not isinstance(item,FoodItem):
            return False 
        return (self.__name==item.__name 
                and self.__price==item.__price 
                and self.__food_item_type==item.__food_item_type)
    
    def __hash__(self):
        # Make FoodItem hashable by using immutable attributes
        # Using name and food_item_type as they're more stable than price
        return hash((self.__id,self.__name, self.__food_item_type))
    