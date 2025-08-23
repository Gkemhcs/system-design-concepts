from transaction_types import TransactionType
from transaction import Transaction
from errors import InvalidTransactionError
from observer import Observer
class TransactionManager:
    def __init__(self):
        self._transactions:dict[int,Transaction]={}
        self._nextTransactionID=1 
        self._observers:list[Observer]=[]
    def register_observer(self,observer:Observer):
        self._observers.append(observer)
    def unregister_observer(self,observer:Observer):
        self._observers.remove(observer)
    def _notify(self,transaction:Transaction):
        for observer in self._observers:
            observer.update(transaction)
    def record_transaction(self,transaction_type:TransactionType,card_number:int,account_number:int,amount=0):
        transaction=Transaction(self._nextTransactionID,account_number,card_number,transaction_type,amount)
        self._transactions[self._nextTransactionID]=transaction
        self._notify(transaction)
        self._nextTransactionID+=1
    def get_transaction(self,transaction_id:int)->Transaction:
        if transaction_id not in self._transactions:
            raise InvalidTransactionError("sorry the transaction you are trying to looking for is  not found")
        return self._transactions[transaction_id]   