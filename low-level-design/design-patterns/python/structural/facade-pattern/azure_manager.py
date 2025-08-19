from resources import BlockStorageManager,NetworkManager,VMManager

class AzureBlockStorageManager(BlockStorageManager):
    def create(self):
        print("Azure Block Storage Created")
    def delete(self):
        print("Azure Block Storage Deleted")

class AzureNetworkManager(NetworkManager):
    def create(self):
        print("Azure Network Created")
    def delete(self):
        print("Azure Network Deleted")

class AzureVMManager(VMManager):
    def create(self):
        print("Azure VM Created")
    def delete(self):
        print("Azure VM Deleted")
    def start(self):
        print("Azure VM Started")
    def stop(self):
        print("Azure VM Stopped")
