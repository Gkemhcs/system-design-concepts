from log_appender import LogAppender
from log import Log
from log_formatter import LogFormatter
from text_formatter import TextFormatter
import json 
class ConsoleAppender(LogAppender):
    def __init__(self,formatter:LogFormatter):
        super().__init__(formatter=formatter)
    def append(self,log:Log):
        formatted_log=self.formatter.format(log)

        print(formatted_log)
