from abc import abstractmethod,ABC 


class Compute(ABC):
    
    @abstractmethod
    def Start():
        pass 
    def stop():
        pass 


class Storage(ABC):
    @abstractmethod
    def Create(bucketName:str):
        pass 


class Network(ABC):
    @abstractmethod
    def Configure(subnetName:str):
        pass