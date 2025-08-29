from core_classes.ride import Ride 
from strategies.driver_matching_strategy import IDriverMatchingStrategy

from strategies.pricing_strategy import IPricingStrategy
from core_classes.rider import Rider
from core_classes.driver import Driver
from core_classes.location import Location 
from ride_notifier_subject import NotifierSubject
from payment_service import PaymentService




class RideManager:

    def __init__(self,driver_matching_strategy:IDriverMatchingStrategy,pricing_strategy:IPricingStrategy,payment_service:PaymentService,notifier_subject:NotifierSubject):
        self.__rides:dict[int,Ride]={}
        self.ride_id_counter=1
        self.__driver_matching_strategy=driver_matching_strategy
        self.__pricing_strategy=pricing_strategy
        self.__payment_service=payment_service
        self.__notifier_subject=notifier_subject
   
    def change_pricing_strategy(self,pricing_strategy:IPricingStrategy):
        self.__pricing_strategy=pricing_strategy
    def change_driver_matching_strategy(self,strategy:IDriverMatchingStrategy):
        self.__driver_matching_strategy=strategy
    def change_payment_strategy(self,payment_strategy):
        self.__payment_service.change_payment_strategy(payment_strategy)

    def create_ride(self,rider:Rider,pickup_location:Location,drop_location:Location):
        ride_id=self.ride_id_counter
       
        ride=Ride(ride_id,rider,pickup_location,drop_location,)
        amount=self.__pricing_strategy.calculate_fare(ride)
        ride.set_amount(amount)
    
        
        matching_drivers=self.__driver_matching_strategy.find_driver(ride)
        if matching_drivers:
            for driver in matching_drivers:
                driver.add_pending_request(ride)

            self.__notifier_subject.notify_ride_created(ride,matching_drivers)
            self.__rides[ride_id]=ride 
            self.ride_id_counter+=1
            return ride 
        else:   
            raise Exception(f"sorry no  available drivers at {pickup_location.get_name()} at this time ")
            
    def get_ride(self,ride_id:int)->Ride:
        return self.__rides.get(ride_id,None)
    def get_rides(self)->list[Ride]:
        return list(self.__rides.values())
    def accept_ride(self,ride_id:int,driver:Driver):
        ride=self.get_ride(ride_id)
        is_true=ride.accept_ride(driver)

    def complete_ride(self,ride_id:int):
        ride=self.get_ride(ride_id)
        if self.__payment_service.process_payment(ride.get_amount()):
           
            ride.complete_ride()
        else:
            raise Exception("sorry cannot fulfill payment at this time try again")
    def cancel_ride(self,ride_id):
        ride=self.get_ride(ride_id)
        ride.cancel_ride()
    def start_ride(self,ride_id:int):
        ride=self.get_ride(ride_id)
        ride.start_ride()
        self.__notifier_subject.notify_ride_accepted(ride)

    def get_ride_status(self,ride_id:int):
        ride=self.get_ride(ride_id)
        return ride.get_ride_status()
    
