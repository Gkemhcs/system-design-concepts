from abc import ABC,abstractmethod

class UptimeAlert:

    def __init__(self,serviceName):
        self.service_name=serviceName


class Observer(ABC):
    
    @abstractmethod
    def update(self,alert:UptimeAlert):
        pass    
