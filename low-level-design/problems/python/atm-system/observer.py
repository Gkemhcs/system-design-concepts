from abc import ABC,abstractmethod
from transaction import Transaction
class Observer(ABC):

    @abstractmethod
    def update(self, transaction:Transaction):
        pass
