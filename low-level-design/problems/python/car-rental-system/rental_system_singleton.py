from rental_system import RentalSystem
from threading import Lock

class RentalSystemSingleton:
    _instance=None
    _lock=Lock()

    @classmethod
    def get_rental_system(cls) -> 'RentalSystem':
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                   
                    cls._instance = RentalSystem()
        return cls._instance
    
    

