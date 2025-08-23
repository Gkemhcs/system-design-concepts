from payment_strategy import PaymentStrategy


class PaymentProcessor:

    def __init__(self):
        pass 

    def process_payment(self, amount:float, payment_strategy:PaymentStrategy) -> bool:
        return payment_strategy.pay(amount)