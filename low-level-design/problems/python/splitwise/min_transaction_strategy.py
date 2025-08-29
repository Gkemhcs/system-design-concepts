from abc import ABC,abstractmethod
from user_pair import UserPair
from transaction import Transaction
class MinTransactionStrategy(ABC):


    @abstractmethod
    def calculate_min_transactions(self,balances:dict[UserPair,float])->int:
        pass 