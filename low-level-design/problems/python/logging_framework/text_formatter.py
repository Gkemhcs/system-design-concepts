from log_formatter import LogFormatter
from log import Log

class TextFormatter(LogFormatter):

    def __init__(self):
        pass 
    def format(self,log:Log):
        return f"[{log.get_timestamp()}]:{log.log_level.name}: {log.get_message()}"