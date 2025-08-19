from resources import Compute,Network,Storage

class AzureCompute(Compute):
    def __init__(self):
        pass
    def Start(self):
        print("Azure Compute instance started")
    def stop(self):
        print("Azure Compute instance stopped")

class AzureStorage(Storage):
    def __init__(self):
        pass
    def Create(self,bucketName:str):
        print(f"Azure Storage bucket {bucketName} created")

class AzureNetwork(Network):
    def __init__(self):
        pass
    def Configure(self,subnetName:str):
        print(f"Azure Network subnet {subnetName} configured")
