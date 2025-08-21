from threading import Lock
from file_system import FileSystem

class FileSystemSingleton:
    _instance=None 
    _lock=Lock()

    @classmethod
    def get_file_system(cls):
        if cls._instance is None:
            with cls._lock:
                cls._instance=FileSystem()
        return cls._instance 
    

