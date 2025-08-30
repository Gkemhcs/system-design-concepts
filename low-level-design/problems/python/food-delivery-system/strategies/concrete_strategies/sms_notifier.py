from ..notification_observer import NotificationObserver
from core_classes.order import Order

class SMSNotifier(NotificationObserver):

    def on_order_assigned(self,order:Order):
        customer=order.get_customer()
        delivery_agent=order.get_delivery_agent()
        print(f"[SMS]:- hey {customer.get_name()} your order {order.get_id()} has been assigned to {delivery_agent.get_name() }")
        print(f"[SMS] hey {delivery_agent.get_name()} you have a delivery request need to deliver to {customer.get_location().get_name()}")
    def on_order_out_for_delivery(self,order:Order):
        customer=order.get_customer()
        print(f"[SMS] hey {customer.get_name()} your order {order.get_id()} is out for delivery")
    def on_order_delivered(self,order:Order):
        customer=order.get_customer()
        print(f"[SMS] hey {customer.get_name()} your order {order.get_id()} has been delivered")
    def on_order_cancelled(self,order:Order):
        delivery_agent=order.get_delivery_agent()
        print(f"[SMS] hey {delivery_agent.get_name()} the order {order.get_id()} has been cancelled")