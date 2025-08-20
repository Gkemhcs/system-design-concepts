from payment_strategy import PaymentStrategy

class PaymentProcessor:
    def __init__(self):
        self.payment_strategy=None 
    def change_strategy(self,payment_strategy:PaymentStrategy):
        self.payment_strategy=payment_strategy
    def pay(self,amount:float):
        if self.payment_strategy.process_payment(amount):
            
            return True
        else:
           return False 