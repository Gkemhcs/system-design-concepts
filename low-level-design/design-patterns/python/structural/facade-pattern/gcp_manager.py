from resources import BlockStorageManager,NetworkManager,VMManager

class GCPBlockStorageManager(BlockStorageManager):
    def create(self):
        print("GCP Block Storage Created")
    def delete(self):
        print("GCP Block Storage Deleted")

class GCPNetworkManager(NetworkManager):
    def create(self):
        print("GCP Network Created")
    def delete(self):
        print("GCP Network Deleted")

class GCPVMManager(VMManager):
    def create(self):
        print("GCP VM Created")
    def delete(self):
        print("GCP VM Deleted")
    def start(self):
        print("GCP VM Started")
    def stop(self):
        print("GCP VM Stopped")

