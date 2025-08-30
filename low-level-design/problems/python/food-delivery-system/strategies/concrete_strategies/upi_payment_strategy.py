from ..payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):

    def pay(self,amount:float)->bool:

        print(f"paying {amount} through UPI")   
        return True 