from .food_item import FoodItem

class OrderItem:
    def __init__(self,food_item:FoodItem,quantity:int):
        self.__food_item=food_item
        self.__quantity=quantity
    def get_food_item(self)->FoodItem:
        return self.__food_item
    def get_quantity(self)->int:
        return self.__quantity
    def set_quantity(self,quantity:int):
        self.__quantity=quantity
    def get_total_price(self)->float:
        return self.__food_item.get_price()*self.__quantity