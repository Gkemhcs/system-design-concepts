from adapter import StorageClient

class FrontendClient:
    def __init__(self,storage_client:StorageClient):
        self.storage_client = storage_client
        return None 
    def upload_object(self,bucketName :str,file:str):
        return self.storage_client.upload_object(bucketName,file)
    def download_object(self,bucketName :str,file:str):
        return self.storage_client.download_object(bucketName,file)