from parking_fee_strategy import ParkingFeeStrategy

class HourlyParkingFeeStrategy(ParkingFeeStrategy):
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_fee(self, parking_duration: int) -> float:
        return self.hourly_rate * parking_duration