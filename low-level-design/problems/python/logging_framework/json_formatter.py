from log_formatter import LogFormatter
from log import Log
class JSONFormatter(LogFormatter):

    def __init__(self):
        pass 
    def format(self,log:Log):
        return log.to_dict()
    
