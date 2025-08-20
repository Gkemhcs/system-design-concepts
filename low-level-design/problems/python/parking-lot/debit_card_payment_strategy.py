from payment_strategy  import PaymentStrategy

class DebitCardPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing debit card payment of ${amount:.2f}")
        return True
