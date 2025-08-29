from rider_manager import RiderManager
from driver_manager import DriverManager
from core_classes.locations.bellandur import Bellandur
from core_classes.locations.marathalli import Marathalli
from core_classes.locations.koramangala import Koramangala
from core_classes.locations.silkboard import SilkBoard
from core_classes.driver import Driver
from core_classes.ride import Ride  
from core_classes.rider_type import RiderType
from strategies.concrete_strategies.same_location_driver_matching import SameLocationDriverMatching
from strategies.concrete_strategies.distance_based_strategy import DistanceBasedPricing
from strategies.concrete_strategies.rider_type_based_strategy import RiderTypeBasedPricing
from strategies.concrete_strategies.sms_notification_sender import SMSNotifier
from strategies.concrete_strategies.upi_payment_payment import UPIPayment
from strategies.concrete_strategies.debit_card_payment import DebitCardPayment
from strategies.concrete_strategies.nearest_k_drivers import NearestKDriversMatching
from ride_manager import RideManager
from payment_service import PaymentService
from ride_notifier_subject import NotifierSubject

def main():
    print("🚗 Welcome to Ride-Sharing Service Demo! 🚗\n")
    
    # Initialize managers
    rider_manager = RiderManager()
    driver_manager = DriverManager()
    
    # Create riders with different types
    print("👥 Creating Riders...")
    rider1 = rider_manager.create_rider("koti", "koti@gmail", RiderType.REGULAR)
    rider2 = rider_manager.create_rider("charan", "eswar@gmail", RiderType.PREMIUM)
    print(f"Created riders: {rider1.get_name()} ({rider1.get_rider_type().value}), {rider2.get_name()} ({rider2.get_rider_type().value})\n")
    
    # Create drivers
    print("🚘 Creating Drivers...")
    driver1 = driver_manager.create_driver("sanjay", "mani@gmail", Bellandur())
    driver2 = driver_manager.create_driver("hareesh", "hani@gmail", Marathalli())
    driver3 = driver_manager.create_driver("seshu", "seshu@gmail", Bellandur())
    print(f"Created drivers: {driver1.get_name()}, {driver2.get_name()}, {driver3.get_name()}\n")
    
    # Initialize services
    sms_notifier = SMSNotifier()
    notifier_subject = NotifierSubject()
    notifier_subject.add_observer(sms_notifier)
    
    # Create single ride manager with initial strategies
    print("💰 Creating Ride Manager with Initial Strategies...")
    ride_manager = RideManager(
        SameLocationDriverMatching(driver_manager),  # Initial: Same location strategy
        DistanceBasedPricing(base_fare=50.0, per_km_rate=15.0),  # Initial: Distance-based pricing
        PaymentService(UPIPayment("gkem@ybl")),  # Initial: UPI payment
        notifier_subject
    )
    
    # First ride with initial strategies
    print("\n--- First Ride (Distance-based + Same Location + UPI) ---")
    ride1 = ride_manager.create_ride(rider1, Bellandur(), Koramangala())
    print(f"Ride {ride1.get_id()} created with distance-based pricing: ₹{ride1.get_amount()}")
    
    # Change strategies for second ride
    print("\n🔄 Changing Strategies for Second Ride...")
    ride_manager.change_pricing_strategy(RiderTypeBasedPricing(base_rate=15.0, premium_discount=0.2))
    ride_manager.change_driver_matching_strategy(NearestKDriversMatching(driver_manager, 3))
    ride_manager.change_payment_strategy(DebitCardPayment("1234-5678-9012-3456", "123", "12/25"))
    
    print("✅ Changed to:")
    print("  - Rider-type-based pricing (Premium discount)")
    print("  - Nearest K drivers matching strategy")
    print("  - Debit card payment")

    # Accept ride1
    driver1.accept_pending_request(1)
    print(f"Driver {driver1.get_name()} accepted ride {ride1.get_id()}")

    # Second ride with new strategies
    print("\n--- Second Ride (Rider-type-based + Nearest K + Debit Card) ---")
    ride2 = ride_manager.create_ride(rider2, Bellandur(), Koramangala())
    print(f"Ride {ride2.get_id()} created with rider-type-based pricing: ₹{ride2.get_amount()}")
    
    # Test ride flow for first ride
    print("\n🚀 Testing Ride Flow for First Ride...")
    
   
    
    # Start ride1
    ride_manager.start_ride(ride1.get_id())
    
    # Complete ride1
    ride_manager.complete_ride(ride1.get_id())
    
    # Test ride flow for second ride
    print("\n🚀 Testing Ride Flow for Second Ride...")
    
    # Accept ride2
    driver2.accept_pending_request(1)
    print(f"Driver {driver2.get_name()} accepted ride {ride2.get_id()}")
    try:
        driver3.accept_pending_request(1)
    except Exception as e:
        print("----driver3 accepting second ride should fail as it is already accepted by driver2----")
        print(e)
   
    
    # Start ride2
    ride_manager.start_ride(ride2.get_id())
    
    # Complete ride2
    ride_manager.complete_ride(ride2.get_id())
    
    # Display final status
    print("\n📊 Final Status:")
    print(f"Ride {ride1.get_id()} status: {ride1.get_ride_status()}")
    print(f"Ride {ride2.get_id()} status: {ride2.get_ride_status()}")
    
    # Test pending requests
    print("\n📋 Testing Pending Requests...")
    display_pending_requests(driver3)
    
    print("\n✅ Demo completed successfully!")

def display_pending_requests(driver: Driver):
    pending_requests = driver.get_pending_requests()
    print(f"\n📋 Pending requests for driver: {driver.get_name()}")
    if not pending_requests:
        print("No pending requests")
        return
        
    for index, request in enumerate(pending_requests):
        print(f"\nRequest {index + 1}:")
        print(f"  Rider: {request.get_rider().get_name()}")
        print(f"  Pickup: {request.get_pickup_location().get_name()}")
        print(f"  Drop: {request.get_drop_location().get_name()}")
        print(f"  Amount: ₹{request.get_amount():.2f}")
        print(f"  Status: {request.get_ride_status()}")

if __name__ == "__main__":
    main()