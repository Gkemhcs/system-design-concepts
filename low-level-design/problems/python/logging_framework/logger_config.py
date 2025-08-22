from log_level import LogLevel
from log_appender import LogAppender

class LoggerConfig:

    def __init__(self,log_level=LogLevel.Info,appenders:list[LogAppender]=[]):
        self.log_level:LogLevel=log_level
        self._appenders:list[LogAppender]=appenders 
    def get_appenders(self)->list[LogAppender]:
        return self._appenders
    def get_log_level(self)->LogLevel:
        return self.log_level

    def add_appender(self,appender:LogAppender):
        self._appenders.append(appender)
    def remove_appender(self,appender:LogAppender):
        self._appenders.remove(appender)
    def set_log_level(self,log_level:LogLevel):
        self.log_level=log_level
    