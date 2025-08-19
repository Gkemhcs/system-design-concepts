from abc import ABC,abstractmethod


class StorageClient(ABC):
    @abstractmethod
    def upload_object(self,bucketName :str,file:str):
        pass 
    @abstractmethod
    def download_object(self,bucketName :str,file:str):
        pass 

class GCPAdapter(StorageClient):
    def __init__(self,adaptee):
        self.adaptee = adaptee
    def upload_object(self,bucketName :str,file:str):
        self.adaptee.PutObject(bucketName,file)
    def download_object(self,bucketName :str,file:str):
        self.adaptee.GetObject(bucketName,file)