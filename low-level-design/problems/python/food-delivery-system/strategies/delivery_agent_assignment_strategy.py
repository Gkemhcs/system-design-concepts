from abc import ABC,abstractmethod

from core_classes.restaurant import Restaurant
from core_classes.customer import Customer
from core_classes.delivery_agent import DeliveryAgent

class DeliveryAgentAssignmentStrategy(ABC):

    @abstractmethod
    def assign_delivery_agent(self,restaurant:Restaurant)->DeliveryAgent:
        pass