from factory import Factory
from azure import AzureCompute,AzureStorage,AzureNetwork


class AzureFactory(Factory):

    def createCompute(self)->AzureCompute:
        
        return AzureCompute()

    def createStorage(self)->AzureStorage:
        
        return AzureStorage()

    def createNetwork(self)->AzureNetwork:
        
        return AzureNetwork()
