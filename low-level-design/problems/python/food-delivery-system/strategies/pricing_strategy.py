from abc import ABC, abstractmethod
from  core_classes.restaurant import Restaurant
from core_classes.customer import Customer
from core_classes.delivery_agent import DeliveryAgent

class PricingStrategy(ABC):


    def calculate_delivery_price(self,delivery_agent:DeliveryAgent,restaurant:Restaurant,customer:Customer)->float:
        pass 