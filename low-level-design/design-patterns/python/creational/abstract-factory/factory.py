from abc import ABC,abstractmethod

from resources import Compute,Network,Storage
class Factory(ABC):

    @abstractmethod
    def createCompute(self)->Compute:
        pass

    @abstractmethod
    def createStorage(self)->Storage:
        pass

    @abstractmethod
    def createNetwork(self)->Network:
        pass
