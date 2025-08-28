from strategies.payment_strategy import PaymentStrategy

class PaymentService:


    def __init__(self, strategy:PaymentStrategy):
        self.__strategy=strategy
    
    def process_payment(self,amount:float)->bool:
        return self.__strategy.pay(amount)

    def change_strategy(self,strategy:PaymentStrategy):
        self.__strategy=strategy
    