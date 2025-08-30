from restaurant_manager import RestaurantManager
from delivery_assignment_service import DeliveryAgentAssignmentService
from payment_service import PaymentService
from order_notifier_subject import OrderNotifierSubject

from strategies.pricing_strategy import PricingStrategy


from core_classes.customer import Customer
from core_classes.order import Order
from core_classes.food_item import FoodItem
from core_classes.order_item import OrderItem
from core_classes.order_status import OrderStatus
from core_classes.restaurant import Restaurant






class OrderManager:

    def __init__(self,restaurant_manager:RestaurantManager,delivery_assignment_service:DeliveryAgentAssignmentService,payment_service:PaymentService,pricing_strategy:PricingStrategy,order_notifier_subject:OrderNotifierSubject):
        self.__restaurant_manager=restaurant_manager
        self.__delivery_assignment_service=delivery_assignment_service
        self.__payment_service=payment_service
        self.__pricing_strategy=pricing_strategy
        self.__order_notifier_subject=order_notifier_subject
        self.__orders:dict[int,Order]={}
        self.__order_id_counter:int=1
    def validate_order_items(self,restaurant:Restaurant,items:dict[FoodItem,int])->list[FoodItem]:
            missing_food_items:list[FoodItem]=[]
            restaurant_menu=restaurant.get_menu()
            for food_item,quantity in items.items():
                if not restaurant.check_for_item(food_item):
                    missing_food_items.append(food_item)
                
            return missing_food_items
    def get_order_item_list(self,items:dict[int,int])->list[OrderItem]:
        order_items=[]
        for food_item,quantity in items.items():
            order_item=OrderItem(food_item,quantity)
            order_items.append(order_item)
        return order_items

    def create_order(self,restaurant_id:int,customer:Customer,items:dict[FoodItem,int])->Order:

        order_id=self.__order_id_counter
        restaurant=self.__restaurant_manager.get_restaurant(restaurant_id)
        missing_food_items=self.validate_order_items(restaurant,items)
        if missing_food_items:
            raise Exception(f"sorry some items are missing from restaurant menu ,{missing_food_items}")
        
        try:
            delivery_agent=self.__delivery_assignment_service.assign_delivery_agent(restaurant)
        except Exception as e:
            raise Exception(f"Delivery agent assignment failed: {e}")
        
        if delivery_agent is None:
            raise Exception("sorry not delivery agent is available at this time")
        else:
          
            order_items=self.get_order_item_list(items)
            amount=0
            for order_item in order_items:
                amount+=order_item.get_total_price()
            delivery_fee=self.__pricing_strategy.calculate_delivery_price(delivery_agent,restaurant,customer)
            order=Order(order_id,customer,delivery_agent,order_items,amount,delivery_fee)
            
            # Assign the order to delivery agent
            delivery_agent.assign_delivery(order)
            
            self.__orders[order_id]=order
            self.__order_id_counter+=1
            self.__order_notifier_subject.notify_order_assigned(order)
            return order
    def get_order(self,id:int)->Order:
        return self.__orders.get(id,None)
    def get_orders(self)->list[Order]:
        return list(self.__orders.values())
    def  start_delivery(self,order_id:int):
        order=self.get_order(order_id)
        delivery_agent=order.get_delivery_agent()
        delivery_agent.on_delivery()
        order.start_delivery()
        self.__order_notifier_subject.notify_order_out_for_delivery(order)
    def complete_delivery(self,order_id:int):
        order=self.get_order(order_id)
        if self.__payment_service.process_payment(order.get_total_amount()):
           
            delivery_agent=order.get_delivery_agent()
            delivery_agent.release_order(order)
            order.complete_delivery()
            self.__order_notifier_subject.notify_order_delivered(order)
        else:
            raise Exception("sorry cannot fulfill payment at this time try again")
    def cancel_delivery(self,order_id:int):
        order=self.get_order(order_id)
        delivery_agent=order.get_delivery_agent()
        delivery_agent.release_order(order)
        order.cancel_delivery()
        self.__order_notifier_subject.notify_order_cancelled(order)
    def get_order_status(self,order_id:int)->OrderStatus:
        order=self.get_order(order_id)
        return order.get_status()
    


