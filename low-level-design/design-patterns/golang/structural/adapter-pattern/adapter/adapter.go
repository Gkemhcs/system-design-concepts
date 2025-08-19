package adapter

func NewGCPAdapter() *GCPAdapter {
	return &GCPAdapter{
		gcpClient: NewGCPAdaptee(),
	}
}

type GCPAdapter struct {
	gcpClient *GCPAdaptee
}

func(adapter *GCPAdapter) Upload(filename string) error {
	return adapter.gcpClient.PutObject("my-gcp-bucket", filename)
}

func(adapter *GCPAdapter) Download(filename string) error {
	return adapter.gcpClient.GetObject("my-gcp-bucket", filename)
}