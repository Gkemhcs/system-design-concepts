from core_classes.item_types.dessert import Dessert
from core_classes.item_types.drink import Drink
from core_classes.item_types.main_course import MainCourse
from core_classes.item_types.starter import Starter

from core_classes.food_item_type import FoodItemType
from core_classes.food_item import FoodItem

class FoodItemFactory:

    @staticmethod
    def create_food_item(id:int,name:str,price:float,item_type:str)->FoodItem:
        if item_type.lower()=="main_course":
            return MainCourse(id,name,price)
        elif item_type.lower()=="starter":
            return Starter(id,name,price)
        elif item_type.lower()=="dessert":
            return Dessert(id,name,price)
        elif item_type.lower()=="drink":
            return Drink(id,name,price)
        else:
            raise NotImplementedError("sorry the requested food item type doesnt exist")
    