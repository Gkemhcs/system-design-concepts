from  payment_strategy import PaymentStrategy


class DebitCardPayment(PaymentStrategy):

    def __init__(self,cardNumber="2450 9499 9499",cardType="visa",userName="gkem"):
        self._card_number=cardNumber
        self._card_type=cardType
        self._user_name=userName

    def pay(self,amount:float)->bool :

        print(f"paying through debit card of number {self._card_number} of type {self._card_type}") 
        return True 