from parking_fee_strategy import ParkingFeeStrategy

class VehicleBasedFeeStrategy(ParkingFeeStrategy):
    def __init__(self, rates: dict):
        self._rates = rates

    def calculate_fee(self, parking_duration: int, vehicle_type: str) -> float:
        rate = self._rates.get(vehicle_type, 0)
        return rate * parking_duration