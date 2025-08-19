package factory
import "fmt"

type StorageFactory interface {
	createStorageClient(provider string) (StorageClient, error)
}


func NewCloudStorageFactory() *CloudStorageFactory {
	return &CloudStorageFactory{}
}

type CloudStorageFactory struct {
}

func (f *CloudStorageFactory) CreateStorageClient(provider string) (StorageClient, error) {
	switch provider {
	case "aws":
		return NewAWSStorageClient(), nil
	case "gcp":
		return NewGCPStorageClient(), nil
	case "azure":
		return NewAzureStorageClient(), nil
	default:
		return nil, fmt.Errorf("unsupported cloud provider: %s", provider)
	}
}
