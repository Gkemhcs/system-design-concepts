package adapter

func NewFrontendClient(storageClient StorageClient) *FrontendClient {
	return &FrontendClient{
		storageClient,
	}
}

type FrontendClient struct {
	storageClient StorageClient
}

func (fc *FrontendClient) UploadFile(filename string) error {
	return fc.storageClient.Upload(filename)
}
func (fc *FrontendClient) DownloadFile(filename string) error {
	return fc.storageClient.Download(filename)
}
