from transaction_types import TransactionType
from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: int, account_number: int, card_number: int, transaction_type: TransactionType, amount: float):
        self._transaction_id = transaction_id
        self._account_number = account_number
        self._card_number = card_number 
        self._transaction_type = transaction_type
        self._amount = amount 
        self._timestamp = datetime.now()
    
    def get_transaction_id(self) -> int:
        return self._transaction_id
    
    def get_transaction_type(self) -> TransactionType:
        return self._transaction_type
    
    def get_card_number(self) -> int:
        return self._card_number
    
    def get_account_number(self) -> int:
        return self._account_number
    
    def get_timestamp(self) -> datetime:
        return self._timestamp
    
    def get_amount(self) -> float:
        return self._amount
    
