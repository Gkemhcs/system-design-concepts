from storage_client import StorageClient

class AzureStorageClient(StorageClient):
    def upload(self, content: str, path: str):
        print(f"Uploading {content} to Azure at {path}")    
    def download(self, path: str):
        print(f"Downloading from Azure at {path}")