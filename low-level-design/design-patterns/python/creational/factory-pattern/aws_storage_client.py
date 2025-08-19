from storage_client import StorageClient

class AWSStorageClient(StorageClient):

    def upload(self, content: str, path: str):
        print(f"Uploading {content} to AWS at {path}")

    def download(self, path: str):
        print(f"Downloading from AWS at {path}")