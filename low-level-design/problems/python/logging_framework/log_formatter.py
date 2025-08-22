from abc import ABC,abstractmethod
from log import Log 

class LogFormatter(ABC):
    
    @abstractmethod
    def format(log:Log):
        pass 