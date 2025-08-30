from core_classes.restaurant import Restaurant
from core_classes.food_item import FoodItem
from factories.food_item_factory import FoodItemFactory
from core_classes.location import Location


class RestaurantManager:

    def __init__(self):
        self.__restaurants:dict[int,Restaurant]={}
        self.__restaurant_id_counter=1
        self.__food_item_id_counter=1
    def create_restaurant(self,name:str,location:Location)->Restaurant:
        restaurant_id=self.__restaurant_id_counter
        restaurant=Restaurant(restaurant_id,name,location)
        self.__restaurants[restaurant_id]=restaurant
        self.__restaurant_id_counter+=1
        print(f"Restaurant {name} created successfully")
        return restaurant
    def get_restaurant(self,id:int)->Restaurant:
        if id not in self.__restaurants:
            raise Exception("sorry the restaurant doesnt exist")
        else:
            return self.__restaurants.get(id,None)
    def get_restaurants(self)->list[Restaurant]:
        restaurants=list(self.__restaurants.values())
        return restaurants
    def add_food_item_to_menu(self,restaurant_id:int,name:str,price:float,item_type:str):
        restaurant=self.get_restaurant(restaurant_id)
        food_item_id=self.__food_item_id_counter
        
        food_item=FoodItemFactory.create_food_item(food_item_id,name,price,item_type)
        print(f"{name} added to menu successfully in {restaurant.get_name()}")
        self.__food_item_id_counter+=1
        restaurant.add_food_item(food_item)
    
