package factory

import "fmt"

func NewAWSStorageClient() *AWSStorageClient {
	return &AWSStorageClient{}
}

type AWSStorageClient struct {
}

func (client *AWSStorageClient) Upload(fileName string, data []byte) error {
	// Implementation for uploading to AWS S3
	fmt.Println("Uploading to AWS S3:", fileName, string(data))
	return nil
}
func (client *AWSStorageClient) Download(fileName string) error {
	fmt.Println("Downloading from AWS S3:", fileName)
	return nil
}
