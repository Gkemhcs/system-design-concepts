from azure_factory import AzureFactory

from gcp_factory import GCPFactory

def main():
    print("\n--------azure factory--------\n")
    azure_factory = AzureFactory()
    azure_compute = azure_factory.createCompute()
    azure_storage = azure_factory.createStorage()
    azure_network = azure_factory.createNetwork()
    azure_storage.Create("storage-account-1")
    azure_network.Configure("vnet-1")
    azure_compute.Start()       
    azure_compute.stop()
    print("\n--------gcp factory--------\n")

    gcp_factory = GCPFactory()
    gcp_compute = gcp_factory.createCompute()
    gcp_storage = gcp_factory.createStorage()
    gcp_network = gcp_factory.createNetwork()
    gcp_storage.Create("storage-account-1")
    gcp_network.Configure("vnet-1")
    gcp_compute.Start()       
    gcp_compute.stop()

if __name__=="__main__":
    main()      



