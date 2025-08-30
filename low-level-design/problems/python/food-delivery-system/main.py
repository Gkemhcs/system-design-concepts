from delivery_agent_manager import DeliveryAgentManager
from customer_manager import CustomerManager
from restaurant_manager import RestaurantManager
from payment_service import PaymentService
from order_notifier_subject import OrderNotifierSubject
from delivery_assignment_service import DeliveryAgentAssignmentService
from order_manager import OrderManager

from strategies.concrete_strategies.nearest_delivery_agent_assignment_strategy import NearestDeliveryAgentAssignment
from strategies.concrete_strategies.sms_notifier import SMSNotifier
from strategies.concrete_strategies.upi_payment_strategy import UPIPayment
from strategies.concrete_strategies.delivery_agent_rating_pricing import DeliveryAgentRatingPricing

from core_classes.location import Location
from core_classes.locations.bellandur import Bellandur
from core_classes.locations.koramangala  import Koramangala
from core_classes.locations.marathalli  import Marathalli
from core_classes.locations.silkboard import SilkBoard
from core_classes.restaurant import Restaurant
from core_classes.food_item import FoodItem
from core_classes.food_item_type import FoodItemType



def main():
    print("🍕" + "="*80 + "🍕")
    print("🎯 WELCOME TO FOOD DELIVERY SYSTEM - LLD DEMONSTRATION 🎯")
    print("🍕" + "="*80 + "🍕\n")
    
    # === SYSTEM INITIALIZATION ===
    print("📋 STEP 1: SYSTEM INITIALIZATION")
    print("-" * 50)
    
    customer_manager=CustomerManager()
    delivery_agent_manager=DeliveryAgentManager()
    
    print("🚚 Creating Delivery Agents...")
    delivery_agent1=delivery_agent_manager.create_delivery_agent("varun","varun@gmail",9090990009,Bellandur())
    delivery_agent2=delivery_agent_manager.create_delivery_agent("harish","harish@gmail",9090990009,Marathalli())
    print(f"   ✅ Varun (Location: Bellandur)")
    print(f"   ✅ Harish (Location: Marathalli)")
    
    print("\n👥 Creating Customers...")
    cust1=customer_manager.create_customer("koti","koti@gmail",9090990009,Bellandur())
    cust2=customer_manager.create_customer("charan","charan@gmail",9090990009,Marathalli())
    print(f"   ✅ Koti (Location: Bellandur)")
    print(f"   ✅ Charan (Location: Marathalli)")
    
    print("\n🏪 Creating Restaurants...")
    restaurant_manager=RestaurantManager()
    restaurant1=restaurant_manager.create_restaurant("GreenLand NorthIndian Restaurant",Bellandur())
    restaurant2=restaurant_manager.create_restaurant("Madhura Restaurant",Koramangala())
    print(f"   ✅ GreenLand Restaurant (Location: Bellandur)")
    print(f"   ✅ Madhura Restaurant (Location: Koramangala)")
  
    print("\n🍽️ Adding Menu Items...")
    restaurant_manager.add_food_item_to_menu(restaurant1.get_id(),"kaju curry",150,"main_course")
    restaurant_manager.add_food_item_to_menu(restaurant1.get_id(),"mushroom curry",180,"main_course")
    
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"coca-cola",20,"drink")
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"pepsi",20,"drink")
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"vanilla icecream",40,"dessert")
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"chocolate icecream",40,"dessert")
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"spring rolls",120,"starter")
    restaurant_manager.add_food_item_to_menu(restaurant2.get_id(),"tomato soup",100,"starter")
    
    print("\n📋 STEP 2: RESTAURANT MENUS")
    print("-" * 50)
    display_menu(restaurant1)
    display_menu(restaurant2)
    
    # Verify menu item exists
    food1=restaurant1.check_for_item(FoodItem(1,"kaju curry",150,FoodItemType.MAIN_COURSE))
    print(f"✅ Menu validation: Item exists = {food1}")

    print("\n🔧 STEP 3: SERVICE INITIALIZATION")
    print("-" * 50)
    payment_service=PaymentService(UPIPayment())
    order_notifier_subject=OrderNotifierSubject()
    order_notifier_subject.add_observer(SMSNotifier())
    delivery_assignment_service=DeliveryAgentAssignmentService(NearestDeliveryAgentAssignment(delivery_agent_manager))
    order_manager=OrderManager(restaurant_manager,delivery_assignment_service,payment_service,DeliveryAgentRatingPricing(),order_notifier_subject)
    print("✅ Payment Service initialized with UPI")
    print("✅ Notification Service initialized with SMS")
    print("✅ Delivery Assignment Service initialized with Nearest Agent Strategy")
    print("✅ Order Manager initialized with Rating-based Pricing")

    print("\n📦 STEP 4: ORDER CREATION & ASSIGNMENT")
    print("-" * 50)
    
    item_list1={restaurant2.get_item_by_name("vanilla icecream"):2,restaurant2.get_item_by_name("chocolate icecream"):1}
    item_list2={restaurant1.get_item_by_name("kaju curry"):2,restaurant1.get_item_by_name("mushroom curry"):1}
    
    print("🛒 Creating Order 1 (koti -> Madhura Restaurant)...")
    print(f"   📍 Customer: Koti (Bellandur) → Restaurant: Madhura (Koramangala)")
    print(f"   🍨 Items: 2x Vanilla Ice Cream, 1x Chocolate Ice Cream")
    order1=order_manager.create_order(restaurant2.get_id(),cust1,item_list1)
    print(f"   ✅ Order {order1.get_id()} created! Amount: ₹{order1.get_total_amount():.2f}")
    
    print("\n🛒 Creating Order 2 (koti -> GreenLand Restaurant)...")
    print(f"   📍 Customer: Koti (Bellandur) → Restaurant: GreenLand (Bellandur)")
    print(f"   🍛 Items: 2x Kaju Curry, 1x Mushroom Curry")
    order2=order_manager.create_order(restaurant1.get_id(),cust1,item_list2)
    print(f"   ✅ Order {order2.get_id()} created! Amount: ₹{order2.get_total_amount():.2f}")
    
    print("\n📊 STEP 5: AGENT STATUS TRACKING")
    print("-" * 50)
    print(f"🚚 Agent Status After Order Assignment:")
    print(f"   • Varun: {delivery_agent1.get_status().value} (Active Orders: {len(delivery_agent1.get_active_orders())})")
    print(f"   • Harish: {delivery_agent2.get_status().value} (Active Orders: {len(delivery_agent2.get_active_orders())})")
    
    print("\n🚀 STEP 6: STARTING DELIVERIES")
    print("-" * 50)
    
    print("🚀 Starting delivery for Order 2 (Kaju Curry)...")
    order_manager.start_delivery(order2.get_id())
    print(f"   📍 Agent transitioned to ON_DELIVERY status")
    
    print("\n📊 Agent Status After Starting One Delivery:")
    print(f"   • Varun: {delivery_agent1.get_status().value}")
    print(f"   • Harish: {delivery_agent2.get_status().value}")
    
    print("\n🛒 STEP 7: TESTING MULTIPLE ORDERS PER AGENT")
    print("-" * 50)
    print("🛒 Creating Order 3 (charan -> Madhura Restaurant)...")
    print(f"   📍 Customer: Charan (Marathalli) → Restaurant: Madhura (Koramangala)")
    print(f"   🍨 Items: 2x Vanilla Ice Cream, 1x Chocolate Ice Cream")
    print("🔍 Testing if ASSIGNED_DELIVERY agents can accept new orders...")
    
    order3=order_manager.create_order(restaurant2.get_id(),cust2,item_list1)
    print(f"   ✅ Order {order3.get_id()} created! Amount: ₹{order3.get_total_amount():.2f}")
    print("🎯 SUCCESS: ASSIGNED_DELIVERY agents can accept new orders!")
    
    print("\n🚀 Starting delivery for Order 1 (Ice Cream)...")
    order_manager.start_delivery(order1.get_id())
    
    print(f"\n📊 Final Agent Status After All Orders:")
    print(f"   • Varun: {delivery_agent1.get_status().value} (Active Orders: {len(delivery_agent1.get_active_orders())})")
    print(f"   • Harish: {delivery_agent2.get_status().value} (Active Orders: {len(delivery_agent2.get_active_orders())})")
    
    print("\n💳 STEP 8: PAYMENT PROCESSING & COMPLETION")
    print("-" * 50)
    
    print("💳 Completing delivery for Order 1...")
    order_manager.complete_delivery(order1.get_id())
    print(f"   ✅ Order 1 delivered and payment processed!")
    
    print("\n💳 Completing delivery for Order 2...")
    order_manager.complete_delivery(order2.get_id())
    print(f"   ✅ Order 2 delivered and payment processed!")
    
    print("\n❌ STEP 9: ORDER CANCELLATION")
    print("-" * 50)
    print("❌ Cancelling Order 3...")
    order_manager.cancel_delivery(order3.get_id())
    print(f"   ✅ Order 3 cancelled successfully!")
    
    print("\n🎉 STEP 10: SYSTEM DEMONSTRATION COMPLETE")
    print("-" * 50)
    print("✅ Successfully demonstrated:")
    print("   🔹 Order creation and assignment")
    print("   🔹 Delivery agent status management")
    print("   🔹 Multiple orders per agent")
    print("   🔹 Payment processing")
    print("   🔹 Order lifecycle management")
    print("   🔹 SMS notifications")
    print("   🔹 Strategy pattern implementations")
    print("   🔹 Observer pattern notifications")
    print("\n🍕" + "="*80 + "🍕")
    print("🎯 FOOD DELIVERY SYSTEM LLD DEMONSTRATION COMPLETE! 🎯")
    print("🍕" + "="*80 + "🍕")


def display_menu(restaurant:Restaurant):
    menu=restaurant.get_menu()
    print(f"\n🍽️  Menu for {restaurant.get_name()}:")
    print("   " + "-" * 60)
    for food_item in menu:  
        print(f"   🍽️  {food_item.get_name()} - ₹{food_item.get_price()} ({food_item.get_food_item_type().value})")


if __name__=="__main__":
    main()