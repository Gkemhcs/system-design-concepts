import time 
from log_level import LogLevel
class Log:


    def __init__(self,message,log_level=LogLevel.Info):
        self.log_level=log_level 
        self._message=message 
        self._timestamp=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def get_timestamp(self)->str:
        return self._timestamp
    def get_message(self)->str:
        return self._message
    def to_dict(self):
        return {
            "log_level":self.log_level.name ,
            "timestamp":self.get_timestamp(),
            "msg":self.get_message()
        }
    