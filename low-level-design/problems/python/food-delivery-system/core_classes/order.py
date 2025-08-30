from .order_item import OrderItem
from .order_status import OrderStatus
from .customer import Customer
from .delivery_agent import DeliveryAgent



class Order:
    def __init__(self,id:int,customer:Customer,delivery_agent:DeliveryAgent,order_items:list[OrderItem],amount:float,delivery_fee:float):
        self.__id=id 
        self.__customer=customer 
        self.__delivery_agent=delivery_agent 
        self.__order_items=order_items 
        self.__status=OrderStatus.ASSIGNED
        self.__amount=amount
        self.__delivery_fee=delivery_fee
        self.__total_amount=delivery_fee+amount
    def get_id(self)->int:
        return self.__id 
    def get_customer(self)->Customer:
        return self.__customer 
    def get_delivery_agent(self)->DeliveryAgent:
        return self.__delivery_agent 
    def get_order_items(self)->list[OrderItem]:
        return self.__order_items 
    def get_status(self)->OrderStatus:
        return self.__status 
    def set_status(self,status:OrderStatus):
        self.__status=status  
    def get_total_amount(self)->float:
        return self.__total_amount 
    def set_delivery_agent(self,delivery_agent:DeliveryAgent):
        self.__delivery_agent=delivery_agent 
    def start_delivery(self):
        if self.__status!=OrderStatus.ASSIGNED:
            raise Exception("cannot start delivery as order is not assigned yet or already has been delivered")
        else:
            self.set_status(OrderStatus.OUT_FOR_DELIVERY)
    def complete_delivery(self):
        if self.__status!=OrderStatus.OUT_FOR_DELIVERY:
            raise Exception("cannot complete delivery as order is not out for delivery yet or already has been delivered")
        else:
            self.set_status(OrderStatus.DELIVERED)
    def cancel_delivery(self):
        if self.__status!=OrderStatus.ASSIGNED:
            raise Exception("sorry cannot cancelled as the the order is already delivered or on the way for delivery")
        else:
            self.set_status(OrderStatus.CANCELLED)
    def get_delivery_fee(self)->float:
        return self.__delivery_fee 
    def get_amount(self)->float:
        return self.__amount
    