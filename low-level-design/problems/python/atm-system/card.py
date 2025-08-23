from card_status import CardStatus
from card_type import CardType 

from errors import CardBlockedError,CardIsNotBlockedError
class Card:

    def __init__(self,account_number:int,pin:int,card_type:CardType,card_number:int):
        self._account_number=account_number
        self._pin=pin
        self._card_number=card_number
        self._card_status=CardStatus.ACTIVE
        self._card_type=card_type
    def get_card_number(self)->int:
        return self._card_number
    def get_account_number(self)->int:
        return self._account_number
    def get_pin(self)->int:
        return self._pin 
    def change_pin(self,pin:int):
        self._pin=pin 
    def block_card(self):
        if self._card_status==CardStatus.BLOCKED:
            raise CardBlockedError("card is already blocked")
        self._card_status=CardStatus.BLOCKED
    def unblock_card(self):
        if self._card_status==CardStatus.ACTIVE:
            raise CardIsNotBlockedError("Card is already  active")
        self._card_status=CardStatus.ACTIVE
