from core_classes.delivery_agent import DeliveryAgent
from core_classes.location import Location  
from core_classes.delivery_agent_status import DeliveryAgentStatus

class DeliveryAgentManager:


    def __init__(self):
        self.__delivery_agents:dict[int,DeliveryAgent]={}
        self.delivery_agent_id_counter=1
    def create_delivery_agent(self,name:str,email:str,phone_number:int,location:Location,rating:float=4.0)->DeliveryAgent:
        delivery_agent_id=self.delivery_agent_id_counter
        delivery_agent=DeliveryAgent(delivery_agent_id,name,email,phone_number,location,rating)
        self.__delivery_agents[delivery_agent_id]=delivery_agent
        self.delivery_agent_id_counter+=1
        print(f"delivery agent {name} created successfully") 
        return delivery_agent
    def get_delivery_agent(self,id:int)->DeliveryAgent:
        if id not in self.__delivery_agents:
            raise Exception("sorry the delivery agent doesnt exist")
        else:
            return self.__delivery_agents.get(id,None)
    def get_delivery_agents(self)->list[DeliveryAgent]:
        delivery_agents=list(self.__delivery_agents.values())
        return delivery_agents
    def get_available_delivery_agents(self)->list[DeliveryAgent]:
        # Agents can accept new orders if they are AVAILABLE, ASSIGNED_DELIVERY, or ON_DELIVERY
        # ON_DELIVERY agents are actively delivering but can still accept more orders
        available_agents = []
        for delivery_agent in self.__delivery_agents.values():
            if delivery_agent.get_status() in [DeliveryAgentStatus.AVAILABLE, DeliveryAgentStatus.ASSIGNED_DELIVERY]:
                available_agents.append(delivery_agent)
        return available_agents
    
    def set_delivery_agent_status(self,id:int,status:DeliveryAgentStatus):
        delivery_agent=self.get_delivery_agent(id)
        delivery_agent.set_status(status)
        