from ..delivery_agent_assignment_strategy import DeliveryAgentAssignmentStrategy
from  delivery_agent_manager import DeliveryAgentManager
from core_classes.delivery_agent import DeliveryAgent


class NearestDeliveryAgentAssignment(DeliveryAgentAssignmentStrategy):
    def __init__(self,delivery_agent_manager:DeliveryAgentManager):
        self.__delivery_agent_manager=delivery_agent_manager
    
    def assign_delivery_agent(self,restaurant)->DeliveryAgent:
        delivery_agents=self.__delivery_agent_manager.get_available_delivery_agents()
        
        nearest_delivery_agent:DeliveryAgent=None
        min_distance:float=float('inf')
        
        for delivery_agent in delivery_agents:
            distance=delivery_agent.get_location().calculate_distance(restaurant.get_location())
            if distance<min_distance:
                min_distance=distance
                nearest_delivery_agent=delivery_agent
                print(f"Selected {delivery_agent.get_name()} as nearest")
        
        if nearest_delivery_agent is None:
            raise Exception("No delivery agent available or all agents are at capacity")
            
        return nearest_delivery_agent