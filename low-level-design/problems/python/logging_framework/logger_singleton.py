from threading import Lock 
from logger import Logger 
class LoggerSingleton:

    _instance=None 
    _lock=Lock()
    def __init__(self):
        pass 
    @classmethod
    def get_logger(cls)->Logger:
        if cls._instance is None :
          with cls._lock:
              cls._instance=Logger()
        return cls._instance
