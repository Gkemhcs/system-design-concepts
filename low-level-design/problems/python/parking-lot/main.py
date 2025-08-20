from vehicle_factory import VehicleFactory
from parking_floor import ParkingFloor
from parking_lot import ParkingLot
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from debit_card_payment_strategy import DebitCardPaymentStrategy
from upi_payment_strategy import UPIPaymentStrategy
from flat_rate_strategy import HourlyParkingFeeStrategy
from payment_processor import PaymentProcessor
from errors import VehicleNotFoundError,PaymentFailedError,ParkingLotFullError,VehicleAlreadyParkedError
import time 



def main():

    car1=VehicleFactory.create_vehicle("car","car-1")
    car2=VehicleFactory.create_vehicle("car","car-2")
    car3=VehicleFactory.create_vehicle("car","car-3")
    bike1=VehicleFactory.create_vehicle("bike","bike-1")
    bike2=VehicleFactory.create_vehicle("bike","bike-2")
    truck1=VehicleFactory.create_vehicle("truck","truck-1")
    truck2=VehicleFactory.create_vehicle("truck","truck-2")

    floor1=ParkingFloor("floor-1",[ParkingSpot("spot-1",VehicleSize.Large),ParkingSpot("spot-2",VehicleSize.Medium)])
    floor2=ParkingFloor("floor-2",[ParkingSpot("spot-3",VehicleSize.Small),ParkingSpot("spot-4",VehicleSize.Medium)])
    floor3=ParkingFloor("floor-3",[ParkingSpot("spot-5",VehicleSize.Small),ParkingSpot("spot-6",VehicleSize.Small)])

    hourBasedFeeStrategy=HourlyParkingFeeStrategy(100)
    debitCardPaymentStrategy=DebitCardPaymentStrategy()
    upiPaymentStrategy=UPIPaymentStrategy()
    paymentProcessor=PaymentProcessor()
    paymentProcessor.change_strategy(debitCardPaymentStrategy)

    parkingLot=ParkingLot([floor1,floor2,floor3],hourBasedFeeStrategy,paymentProcessor)

    parkingLot.parkVehicle(car1)
    time.sleep(1)
    parkingLot.parkVehicle(car2)
    time.sleep(1)
    parkingLot.parkVehicle(bike1)
    time.sleep(1)
    parkingLot.parkVehicle(truck1)
    time.sleep(1)
    parkingLot.removeVehicle(truck1)
    time.sleep(1)
    parkingLot.parkVehicle(truck2)
    paymentProcessor.change_strategy(upiPaymentStrategy)
    parkingLot.removeVehicle(bike1)
    try:
        parkingLot.parkVehicle(car1)
    except VehicleAlreadyParkedError as e:
        print(e)
    try: 
        parkingLot.parkVehicle(car3)
    except ParkingLotFullError as e:
        print(e)
    
    

   







 




    


if  __name__=="__main__":
    main()