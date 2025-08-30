from ..payment_strategy import PaymentStrategy

class DebiteCardPaymentStrategy(PaymentStrategy):

    def pay(self,amount:float)->bool:
        print(f"paying {amount} through DebitCard")
        return True