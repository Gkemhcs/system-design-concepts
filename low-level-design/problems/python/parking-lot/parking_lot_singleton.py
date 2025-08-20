class ParkingLot:
    _instance = None

    def __new__(cls, floors=None, parkingFeeStrategy=None, paymentProcessor=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.floors = floors if floors is not None else []
            cls._instance.activeTickets = {}
            cls._instance.parkingFeeStrategy = parkingFeeStrategy
            cls._instance.paymentProcessor = paymentProcessor
        return cls._instance

    