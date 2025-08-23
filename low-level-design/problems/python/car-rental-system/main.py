from rental_system_singleton import RentalSystemSingleton 
from car_factory import CarFactory
from upi_payment import UPIPayment
from debit_card_payment import DebitCardPayment 
from datetime import date

def main():
    print("🚗 Starting Car Rental System...\n")
    
    # Initialize the rental system
    rental_system=RentalSystemSingleton.get_rental_system()
    
    # Create user
    user=rental_system.create_user("koti","anantapur")
    
    # Create cars
    print("\n🏭 Creating cars...")
    car1=CarFactory.create_car("sedan","honda city","SED001")
    car2=CarFactory.create_car("luxury","audi a6","LUX001")
    car3=CarFactory.create_car("suv","toyota fortuner","SUV001")
    car4=CarFactory.create_car("sedan","maruti suzuki dzire","SED002")
    print("✅ All cars created successfully!\n")
    
    # Create rental store
    anantapur_store=rental_system.create_rental_store("anantapur","anantapur")
    bengaluru_store=rental_system.create_rental_store("bengaluru","bengaluru")



    # Add cars to store
    print("📦 Adding cars to store...")
    anantapur_store.add_car(car1)
    anantapur_store.add_car(car2)
    bengaluru_store.add_car(car4)
    print("✅ Cars added to store!\n")
    
    # Make a reservation
    print("📋 Making a reservation...")
    reservation1=rental_system.reserve_car(anantapur_store.get_store_id(), anantapur_store.get_store_id(), user, car1.get_car_type(), date(2023, 10, 1), date(2023, 10, 5))
    
    # Confirm the rental with payment
    print("\n💳 Confirming rental with payment...")
    upi_payment=UPIPayment("s2e9102022@ybl")
    rental_system.confirm_rental(reservation1.get_reservation_id(), anantapur_store.get_store_id(), upi_payment)
    
    rental_system.start_rental(reservation1.get_reservation_id())
    rental_system.cancel_rental(reservation1.get_reservation_id())
    try:
        reservation_2=rental_system.reserve_car(pickupStoreID=anantapur_store.get_store_id(), returnStoreID=bengaluru_store.get_store_id(), user=user, car_type=car4.get_car_type(), pickup_date=date(2023, 10, 1), return_date=date(2023, 10, 5))

    except Exception as e:
        print(f"❌ Error during reservation: {e}")
    reservation_2=rental_system.reserve_car(pickupStoreID=bengaluru_store.get_store_id(), 
                                            returnStoreID=anantapur_store.get_store_id(), 
                                            user=user, car_type=car4.get_car_type(),
                                            pickup_date=date(2023, 10, 1), 
                                            return_date=date(2023, 10, 5))
    debit_card=DebitCardPayment("8200 0200 9200",cardType="VISA",userName="koti eswar mani")
    rental_system.confirm_rental(reservation_2.get_reservation_id(), bengaluru_store.get_store_id(), debit_card)
    rental_system.complete_rental(reservation_2.get_reservation_id())
    print("\n🎉 Car rental system demo completed successfully!")


    # trying the invalid reservation id
    try:
        rental_system.start_rental(999)  # Invalid ID
    except Exception as e:
        print(f"❌ Error during starting rental: {e}")
    # trying to pass invalid pickup_store_id

    try:
        reservation_3=rental_system.reserve_car(pickupStoreID=24,
                                                 returnStoreID=anantapur_store.get_store_id(), user=user, 
                                                 car_type=car4.get_car_type(), pickup_date=date(2023, 10, 1), 
                                                 return_date=date(2023, 10, 5))
    except  Exception as e:
        print(f"❌ Error during reservation: {e}")
    
    # trying to pass invalid return_store_id

    try:
        reservation_3=rental_system.reserve_car(pickupStoreID=anantapur_store.get_store_id(),
                                                 returnStoreID=56, user=user, 
                                                 car_type=car4.get_car_type(), pickup_date=date(2023, 10, 1), 
                                                 return_date=date(2023, 10, 5))
    except  Exception as e:
        print(f"❌ Error during reservation: {e}")


if __name__ == "__main__":
    main()

