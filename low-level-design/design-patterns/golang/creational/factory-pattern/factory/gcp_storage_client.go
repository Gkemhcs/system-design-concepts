package factory

import "fmt"

func NewGCPStorageClient() *GCPStorageClient {	

	return &GCPStorageClient{}
}

type GCPStorageClient struct {
}

func (client *GCPStorageClient) Upload(fileName string, data []byte) error {
	// Implementation for uploading to GCP Storage
	fmt.Println("Uploading to GCP Storage:", fileName, string(data))
	return nil
}

func (client *GCPStorageClient) Download(fileName string) error {
	// Implementation for downloading from GCP Storage
	fmt.Println("Downloading from GCP Storage:", fileName)
	return nil
}
