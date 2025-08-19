from resources import Compute,Storage,Network

class GCPCompute(Compute):
    def __init__(self)  :
        pass 
    def Start(self):
        print("GCP Compute instance started")
    def stop(self):
        print("GCP Compute instance stopped")

class GCPStorage(Storage):
    def __init__(self):
        pass
    def Create(self,bucketName:str):
        print(f"GCP Storage bucket {bucketName} created")

class GCPNetwork(Network):
    def __init__(self):
        pass 
    def Configure(self,subnetName:str):
        print(f"GCP Network subnet {subnetName} configured")