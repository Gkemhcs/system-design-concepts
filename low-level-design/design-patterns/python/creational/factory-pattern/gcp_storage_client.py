from storage_client import  StorageClient
class GCPStorageClient(StorageClient):

    def upload(self, content: str, path: str):
        print(f"Uploading {content} to GCP at {path}")

    def download(self, path: str):
        print(f"Downloading from GCP at {path}")
        return f"Content from {path} in GCP"
