from ..payment_strategy import IPaymentStrategy


class UPIPayment(IPaymentStrategy):
    """
    Payment strategy using UPI (Unified Payments Interface)
    """
    
    def __init__(self, upi_id: str):
        self.__upi_id = upi_id
    
    def pay(self, amount: float) -> bool:
        print(f"Processing payment of {amount:.2f} using UPI ID: {self.__upi_id}")
        # In real implementation, this would integrate with UPI gateway
        # For demo purposes, we'll simulate successful payment
        print(f"UPI payment successful! Amount: {amount:.2f}")
        return True