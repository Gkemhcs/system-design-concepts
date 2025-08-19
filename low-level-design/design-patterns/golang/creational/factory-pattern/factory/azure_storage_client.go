package factory

import "fmt"

func NewAzureStorageClient() *AzureStorageClient {
	return &AzureStorageClient{}
}	

type AzureStorageClient struct {
}

func (client *AzureStorageClient) Upload(fileName string, data []byte) error {
	// Implementation for uploading to Azure Storage
	fmt.Println("Uploading to Azure Storage:", fileName, string(data))
	return nil
}

func (client *AzureStorageClient) Download(fileName string) error {
	// Implementation for downloading from Azure Storage
	fmt.Println("Downloading from Azure Storage:", fileName)
	return nil
}
