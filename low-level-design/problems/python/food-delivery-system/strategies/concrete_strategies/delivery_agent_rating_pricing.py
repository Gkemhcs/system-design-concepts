from ..pricing_strategy import PricingStrategy
from core_classes.restaurant import Restaurant
from core_classes.customer import Customer
from core_classes.delivery_agent import DeliveryAgent

class DeliveryAgentRatingPricing(PricingStrategy):

    def calculate_delivery_price(self,delivery_agent:DeliveryAgent,restaurant:Restaurant,customer:Customer)->float:
        delivery_fee=10.0
        if delivery_agent.get_rating() > 4.5:
            delivery_fee+=30  # Lower delivery fee for highly-rated agents
        elif delivery_agent.get_rating() > 4.0:
            delivery_fee+=20
        else:
            delivery_fee+=10
        restaurant_location=restaurant.get_location()
        customer_location=customer.get_location()
        distance=restaurant_location.calculate_distance(customer_location)
        delivery_fee+=distance*1.5
        return delivery_fee