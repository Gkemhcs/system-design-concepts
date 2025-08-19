package main

import (
	"factory-pattern/factory"
)
func main(){

	factory:=factory.NewCloudStorageFactory()
	awsClient,_:=factory.CreateStorageClient("aws")
	gcpClient,_:=factory.CreateStorageClient("gcp")
	azClient,_:=factory.CreateStorageClient("azure")

	awsClient.Upload("file1.txt", []byte("Hello AWS"))
	awsClient.Download("file1.txt")
	gcpClient.Upload("file2.txt", []byte("Hello GCP"))
	gcpClient.Download("file2.txt")
	azClient.Upload("file3.txt", []byte("Hello Azure"))		
	azClient.Download("file3.txt")


}

