from logger_config import LoggerConfig
from log_level import LogLevel
from log_appender import LogAppender
from log import Log
from log_appender_factory import LogAppenderFactory,Config
class Logger:
    
    def __init__(self,logger_config:LoggerConfig=LoggerConfig()):
        self._logger_config=logger_config
    
    def set_log_level(self,log_level:LogLevel):
        self._logger_config.set_log_level(log_level)

    def create_appender(self,config:Config,appender_type:str):
        return LogAppenderFactory.create_appender(config,appender_type=appender_type)
    def add_appender(self,appender:LogAppender):
        self._logger_config.add_appender(appender)
    def remove_appender(self,appender:LogAppender):
        self._logger_config.remove_appender(appender)
    
    def _log(self,message:str,severity:LogLevel):
        current_log_level=self._logger_config.get_log_level()
        if current_log_level.value<=severity.value:
            log=Log(message,log_level=severity)
            for appender in self._logger_config.get_appenders():
                appender.append(log)
    def info(self,message:str):
        self._log(message,LogLevel.Info)
    def warn(self,message:str):
        self._log(message,LogLevel.Warn)
    def debug(self,message:str):
        self._log(message,LogLevel.Debug)
    def error(self,message:str):
        self._log(message,LogLevel.Error)
    def fatal(self,message:str):
        self._log(message,LogLevel.Fatal)
    