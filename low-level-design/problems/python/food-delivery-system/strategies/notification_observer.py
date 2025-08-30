from abc import ABC,abstractmethod
from core_classes.order import Order
class NotificationObserver(ABC):

    @abstractmethod
    def on_order_assigned(self,order:Order):
        pass 
    @abstractmethod
    def on_order_out_for_delivery(self,order:Order):
        pass 
    @abstractmethod
    def on_order_delivered(self,order:Order):
        pass 
    @abstractmethod
    def on_order_cancelled(self,order:Order):
        pass