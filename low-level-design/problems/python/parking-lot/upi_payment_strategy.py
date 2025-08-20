from payment_strategy import PaymentStrategy

class UPIPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing UPI payment of ${amount:.2f}")
        return True 