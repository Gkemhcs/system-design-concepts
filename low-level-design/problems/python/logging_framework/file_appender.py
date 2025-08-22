from log_appender import LogAppender,Log
from text_formatter import TextFormatter
from log_formatter import LogFormatter
import json 
from threading import Lock
class FileAppender(LogAppender):

    def __init__(self,formatter:LogFormatter,file_path="./demo.log"):
        super().__init__(formatter)
        self._lock=Lock()
        self._file_path=file_path
    def append(self,log:Log):
        formatted_log=self.formatter.format(log)
        with self._lock:
            with open(self._file_path,mode="a+") as file :
                if isinstance(formatted_log, dict):
                    file.write(json.dumps(formatted_log, indent=2) + "\n")
                else:
                    file.write(formatted_log + "\n")

