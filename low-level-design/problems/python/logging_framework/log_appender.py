from abc import ABC,abstractmethod
from log import Log 
from log_formatter import LogFormatter
from  text_formatter import TextFormatter
class LogAppender(ABC):
    
    def __init__(self,formatter):
        self.formatter=formatter 

    @abstractmethod 
    def append(log:Log):
        pass 
