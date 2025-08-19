from abc import ABC ,abstractmethod 


class StorageClient(ABC):

    @abstractmethod
    def upload(self,content:str,path:str):
        pass 
    @abstractmethod
    def download(self,path:str):
        pass 
