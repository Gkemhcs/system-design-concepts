from gcp_manager import  GCPBlockStorageManager,GCPNetworkManager,GCPVMManager
from azure_manager import AzureBlockStorageManager,AzureNetworkManager,AzureVMManager
from abc import ABC,abstractmethod 


class Facade(ABC):

    @abstractmethod
    def create():
        pass 
    
    @abstractmethod
    def destroy():
        pass


class GCPFacade(Facade):
    def __init__(self): 
        self.block_storage_manager = GCPBlockStorageManager()
        self.network_manager = GCPNetworkManager()
        self.vm_manager = GCPVMManager()

    def create(self):
        self.block_storage_manager.create()
        self.network_manager.create()
        self.vm_manager.create()
    def destroy(self):
        self.block_storage_manager.delete()
        self.network_manager.delete()
        self.vm_manager.delete  


class AzureFacade(Facade):
    def __init__(self): 
        self.block_storage_manager = AzureBlockStorageManager()
        self.network_manager = AzureNetworkManager()
        self.vm_manager = AzureVMManager()

    def create(self):
        self.block_storage_manager.create()
        self.network_manager.create()
        self.vm_manager.create()
    def destroy(self):
        self.block_storage_manager.delete()
        self.network_manager.delete()
        self.vm_manager.delete()



