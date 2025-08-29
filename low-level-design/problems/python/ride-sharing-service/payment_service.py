from strategies.payment_strategy import IPaymentStrategy

class PaymentService:

    def __init__(self,payment_strategy:IPaymentStrategy):
        self.__payment_strategy=payment_strategy
    def process_payment(self,amount:float)->bool:
        return self.__payment_strategy.pay(amount)
    def change_payment_strategy(self,payment_strategy:IPaymentStrategy):
        self.__payment_strategy=payment_strategy