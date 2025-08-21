from enum import Enum

class ItemType(Enum):
        COKE="coke"
        SODA="soda"
        JUICE="juice"
        PEPSI="pepsi"


class Item:
    def __init__(self,type:ItemType,price:int):
          self.type=type 
          self._price=price
    def get_price(self)->int:
          return self._price
    def change_price(self,price:int):
          self._price=price 
    def get_item_type(self)->ItemType:
          return self.type
        
