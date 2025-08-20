from abc import ABC,abstractmethod

class AutoScalingStrategy(ABC):

    @abstractmethod
    def ScaleUP(serviceName:str):
        pass 
    @abstractmethod
    def ScaleDown(serviceName:str):
        pass    