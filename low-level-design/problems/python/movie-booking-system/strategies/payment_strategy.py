from abc import ABC,abstractmethod

class PaymentStrategy(ABC):


    @abstractmethod
    def pay(amount:float)->bool:
        pass