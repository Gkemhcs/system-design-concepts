from abc import ABC,abstractmethod


class IPaymentStrategy(ABC):

    def pay(amount:float):
        pass