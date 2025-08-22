from log_appender import LogAppender
from file_appender import FileAppender
from console_appender import ConsoleAppender
from log_formatter import LogFormatter
from json_formatter import JSONFormatter
class Config:

    def __init__(self,file_path:str="./demo.log"):
        self._file_path=file_path
        self.formatter=JSONFormatter()


class LogAppenderFactory:

    @staticmethod
    def create_appender(config:"Config",appender_type:str):

        if appender_type=="file":
            return FileAppender(file_path=config._file_path, formatter=config.formatter)
        elif appender_type=="console":
            return ConsoleAppender(formatter=config.formatter)
        else:
            raise NotImplementedError("the appender type you have passed isnt implemented yet")
        