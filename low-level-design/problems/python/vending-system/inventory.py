from item import Item,ItemType 
class Inventory:
    def __init__(self):
        self.stockMap:dict[ItemType,int]={}
        self.itemMap:dict[ItemType,Item]={}
        self.outOfStock:bool=True 
    def fill_items(self,item:Item,quantity:int):
        item_type=item.get_item_type()
        if item_type in self.stockMap:
            self.stockMap[item_type]+=quantity 
        else:
            self.stockMap[item_type]=quantity 
            self.itemMap[item_type]=item 
        self.outOfStock=False 
        
    def get_item_price(self,itemType:ItemType)->int:
        return self.itemMap[itemType].get_price()
    def get_available_product_stock(self,item:ItemType)->int:
        return self.stockMap[item]
    def  get_products(self)->dict[ItemType,int]:
        return self.stockMap
    def select_product(self,item:ItemType):
        return self.itemMap[item]
    def sell_product(self,item:ItemType):
        self.stockMap[item]-=1