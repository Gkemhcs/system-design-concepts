from atm_system import ATMSystem
from threading import Lock
class ATMSystemSingleton:
    
    _instance:ATMSystem=None 
    _lock=Lock()
    def __init__():
        pass
    @classmethod
    def get_atm_system(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance=ATMSystem()
        return cls._instance
