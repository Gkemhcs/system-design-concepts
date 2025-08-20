from abc import ABC,abstractmethod

class ParkingFeeStrategy(ABC):
    @abstractmethod
    def calculate_fee(self, parking_duration: int) -> float:
        pass


