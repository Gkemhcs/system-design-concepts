from factory import Factory

from gcp import GCPCompute,GCPNetwork,GCPStorage

class GCPFactory(Factory):
    def createCompute(self):
        return GCPCompute()
    def createStorage(self):
        return GCPStorage()
    def createNetwork(self):
        return GCPNetwork()
