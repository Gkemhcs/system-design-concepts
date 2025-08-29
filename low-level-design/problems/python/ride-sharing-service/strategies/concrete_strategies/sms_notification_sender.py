from ..notification_observer import INotificationObserver
from core_classes.ride import Ride
from core_classes.driver import Driver

class SMSNotifier:
    def __init__(self):
        pass 

    def on_ride_created(self,ride:Ride,drivers:list[Driver]):
        for driver in drivers:
            message=f"""
                hello {driver.get_name()} you have recieved a ride request id:-{ride.get_id()} from
                {ride.get_rider().get_name()} and pickup_location is {ride.get_pickup_location()} 
                and drop_location is {ride.get_drop_location()}
                and fare is {ride.get_amount()}
            """
            print(message)
    def on_ride_accepted(self,ride:Ride):
        rider=ride.get_rider()
        message=f"""
              hello {rider.get_name()} your ride request has been accepted by 
              {ride.get_driver().get_name()} and   will pick you soon
              """
        print(message) 
