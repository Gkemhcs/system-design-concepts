from payment_strategy import PaymentStrategy


class UPIPayment(PaymentStrategy):

    def __init__(self,upi_id:str):
        self._upi_id=upi_id
    

    def pay(self,amount:float)->bool :
        print(f"paying {amount}rupess  using upi id {self._upi_id}")
        return True 
        

