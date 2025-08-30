from strategies.delivery_agent_assignment_strategy import DeliveryAgentAssignmentStrategy

from core_classes.delivery_agent import DeliveryAgent
from core_classes.restaurant import Restaurant

class DeliveryAgentAssignmentService:

    def __init__(self,delivery_agent_assignment_strategy:DeliveryAgentAssignmentStrategy):
    
        self.__strategy=delivery_agent_assignment_strategy
    def assign_delivery_agent(self,restaurant:Restaurant)->DeliveryAgent:
        return self.__strategy.assign_delivery_agent(restaurant)
    def change_strategy(self,strategy:DeliveryAgentAssignmentStrategy):
        self.__strategy=strategy