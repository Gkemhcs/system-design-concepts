from logger_singleton import LoggerSingleton
from log_level import LogLevel
from log_appender_factory import Config 
def main():
    logger=LoggerSingleton.get_logger()

    logger.set_log_level(LogLevel.Error)
    console_appender=logger.create_appender(Config(),"console")
    file_appender=logger.create_appender(Config(),"file")
    logger.add_appender(console_appender)
    logger.add_appender(file_appender)
    logger.debug("this is debug message")

    logger.warn("hello this is info message")
    
    logger.set_log_level(LogLevel.Debug)
    logger.debug("this is debug message")


if __name__=="__main__":
    main()