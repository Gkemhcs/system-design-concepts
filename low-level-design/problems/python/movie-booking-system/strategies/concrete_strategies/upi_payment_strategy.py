from strategies.payment_strategy import PaymentStrategy

class UpiPaymentStrategy(PaymentStrategy):

    def __init__(self,upi_id:str):
        self.upi_id=upi_id
    def pay(self, amount: float) -> bool:
        print(f"Paying {amount} using UPI with ID {self.upi_id}")
        return True