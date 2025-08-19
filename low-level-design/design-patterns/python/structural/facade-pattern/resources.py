from  abc import ABC,abstractmethod

class BlockStorageManager(ABC):
    @abstractmethod
    def create():
        pass 
    @abstractmethod
    def delete():
        pass



class NetworkManager(ABC):
    @abstractmethod
    def create():
        pass 
    @abstractmethod
    def delete():
        pass

class VMManager(ABC):

    @abstractmethod
    def create():
        pass 
    @abstractmethod
    def delete():
        pass

    @abstractmethod
    def start():
        pass
    @abstractmethod
    def stop():
        pass