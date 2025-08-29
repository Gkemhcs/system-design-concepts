from ..payment_strategy import IPaymentStrategy

class DebitCardPayment(IPaymentStrategy):
    """
    Payment strategy using Debit Card
    """
    
    def __init__(self, card_number: str, cvv: str, expiry_date: str):
        self.__card_number = card_number
        self.__cvv = cvv
        self.__expiry_date = expiry_date
    
    def pay(self, amount: float) -> bool:
        print(f"Processing payment of {amount:.2f} using Debit Card ending with {self.__card_number[-4:]}")
        # In real implementation, this would integrate with payment gateway
        # For demo purposes, we'll simulate successful payment
        print(f"Payment successful! Amount: {amount:.2f}")
        return True