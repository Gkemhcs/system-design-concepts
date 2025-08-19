from frontend_client import FrontendClient
from adaptee import GCPAdaptee
from adapter import GCPAdapter

def main():
    adaptee = GCPAdaptee()
    adapter = GCPAdapter(adaptee)
    frontend_client = FrontendClient(adapter)
    frontend_client.upload_object("my-bucket","my-file")
    frontend_client.download_object("my-bucket","my-file")

if __name__ == "__main__":
    main()      

