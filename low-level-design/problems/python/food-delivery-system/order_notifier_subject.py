from strategies.notification_observer import NotificationObserver
from core_classes.order import Order

class OrderNotifierSubject:

    def __init__(self):
        self.__observers:list[NotificationObserver]=[]
    def add_observer(self,observer:NotificationObserver):
        self.__observers.append(observer)   
    def remove_observer(self,observer:NotificationObserver):
        self.__observers.remove(observer)
    def notify_order_assigned(self,order:Order):
        for observer in self.__observers:
            observer.on_order_assigned(order)
    def notify_order_out_for_delivery(self,order:Order):
        for observer in self.__observers:
            observer.on_order_out_for_delivery(order)
    def notify_order_delivered(self,order):
        for observer in self.__observers:
            observer.on_order_delivered(order)
    def notify_order_cancelled(self,order):
        for observer in self.__observers:
            observer.on_order_cancelled(order)

