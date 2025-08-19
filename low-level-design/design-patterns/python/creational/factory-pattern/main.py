from  factory import CloudStorageFactory


if __name__ == "__main__":
 
    aws_client = CloudStorageFactory.create_storage_client("AWS")
    azure_client = CloudStorageFactory.create_storage_client("Azure")   
    gcp_client=CloudStorageFactory.create_storage_client("GCP")
    aws_client.upload("this is file","dir/sample.txt")
    aws_client.download("dir/sample.txt")
    azure_client.upload("this is file","dir/sample.txt")
    azure_client.download("dir/sample.txt")
    gcp_client.upload("this is file","dir/sample.txt")
    gcp_client.download("dir/sample.txt")