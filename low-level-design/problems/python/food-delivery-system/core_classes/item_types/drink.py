from ..food_item import FoodItem
from ..food_item_type import FoodItemType


class Drink(FoodItem):

    def __init__(self,id:int,name:str,price:float):
        super().__init__(id,name,price,FoodItemType.DRINK)