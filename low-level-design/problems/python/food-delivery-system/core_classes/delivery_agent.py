from __future__ import annotations
from .user import User 
from .location import Location
from .delivery_agent_status import DeliveryAgentStatus
from threading import Lock 
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from order import Order


class DeliveryAgent(User):

    def __init__(self,id:int,name:str,email:str,phone_number:int,location:Location,rating:float):
        super().__init__(id,name,email,phone_number,location)
        self.__status=DeliveryAgentStatus.AVAILABLE
        self.__rating=rating 
        self.__lock=Lock()
        self.__active_orders:list[Order]=[]
    def get_active_orders(self)->list[Order]:
        return self.__active_orders
    def assign_delivery(self,order:Order):
        with self.__lock:
            self.__active_orders.append(order)
            self.set_status(DeliveryAgentStatus.ASSIGNED_DELIVERY)
    def release_order(self,order:Order):
        with self.__lock:
            self.__active_orders.remove(order)
            if len(self.__active_orders)==0:
                self.set_status(DeliveryAgentStatus.AVAILABLE)
    def on_delivery(self):
        with self.__lock:
            self.set_status(DeliveryAgentStatus.ON_DELIVERY)
    def set_status(self,status:DeliveryAgentStatus):
        self.__status=status
    def get_status(self)->DeliveryAgentStatus:
        return self.__status
    def get_rating(self)->float:
        return self.__rating 
    def set_rating(self,rating:float):
        self.__rating=rating 

    