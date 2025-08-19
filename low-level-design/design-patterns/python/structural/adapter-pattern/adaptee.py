
class GCPAdaptee:
    def __init__(self):
        pass 
    def PutObject(self,bucketName :str,file:str):
        print(f"uploading {file} to bucket {bucketName}")
        return None 
    def GetObject(self,bucketName :str,file:str):
        print(f"downloading {file} from bucket {bucketName}")
        return

