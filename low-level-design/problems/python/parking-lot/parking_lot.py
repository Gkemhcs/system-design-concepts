from parking_floor import ParkingFloor
from parking_fee_strategy import ParkingFeeStrategy
from payment_strategy import PaymentStrategy
from payment_processor import PaymentProcessor
from errors import VehicleNotFoundError,PaymentFailedError,ParkingLotFullError,VehicleAlreadyParkedError
from vehicle import Vehicle
from parking_ticket import ParkingTicket
import time 
from threading import Lock
class ParkingLot:
    def __init__(self,floors:list[ParkingFloor],parkingFeeStrategy:ParkingFeeStrategy,paymentProcessor:PaymentProcessor):
        self.floors=floors 
        self.activeTickets: dict[str, ParkingTicket] = {}
        self.parkingFeeStrategy=parkingFeeStrategy
        self.paymentProcessor=paymentProcessor
        self._lock=Lock()
    def changeStrategy(self, parkingFeeStrategy: ParkingFeeStrategy):
        self.parkingFeeStrategy = parkingFeeStrategy
        print("Parking fee strategy changed.")
    def changePaymentStrategy(self, paymentStrategy: PaymentStrategy):
        self.paymentProcessor.change_strategy(paymentStrategy)
        print("Payment strategy changed.")
    def addFloor(self, floor: ParkingFloor):
        self.floors.append(floor)
        print(f"Added new floor: {floor}")

    def parkVehicle(self, vehicle: Vehicle):
        with self._lock:
            if vehicle.get_license_plate() in self.activeTickets:
                raise VehicleAlreadyParkedError("Vehicle already parked")
            for floor in self.floors:
                ticket = floor.parkVehicle(vehicle)
                if ticket:
                    self.activeTickets[vehicle.get_license_plate()] = ticket
                    print(f"Vehicle {vehicle.get_license_plate()} parked. Ticket issued.")
                    return ticket
            else:
                print(f"No available spots for {vehicle.get_license_plate()}")
                raise ParkingLotFullError("No available spots")
                return None
    def removeVehicle(self, vehicle: Vehicle):
        ticket = self.activeTickets.get(vehicle.get_license_plate())
        
        if ticket is None:
            print(f"Vehicle {vehicle.get_license_plate()} not found in parking lot.")
            raise VehicleNotFoundError("Vehicle not found")
        with self._lock:
            fee = self.parkingFeeStrategy.calculate_fee(time.time() - ticket.getStartTime())
            
            print(f"Calculated parking fee for vehicle {vehicle.get_license_plate()}: {fee}")
            isPaid = self.paymentProcessor.pay(fee)
            if isPaid:
                print("Payment successful")
                ticket.getSpot().remove()
                ticket.setInactive()

                print(f"Vehicle {vehicle.get_license_plate()} removed from parking lot. {ticket.getSpot().getSpotID()}")
            else:
                print("Payment failed")
                raise PaymentFailedError("Payment failed")
            
            

           