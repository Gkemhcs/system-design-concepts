from azure_storage_client import AzureStorageClient
from aws_storage_client import AWSStorageClient
from gcp_storage_client import GCPStorageClient
from abc   import ABC,abstractmethod

class IStorageFactory(ABC):
    @abstractmethod
    def create_storage_client(self):
        pass

class CloudStorageFactory(IStorageFactory):
    @staticmethod
    def create_storage_client( cloud_provider: str):
        if cloud_provider == "AWS":
            return AWSStorageClient()
        elif cloud_provider == "Azure":
            return AzureStorageClient()
        elif cloud_provider == "GCP":
            return GCPStorageClient()
        else:
            raise ValueError("Invalid cloud provider")
