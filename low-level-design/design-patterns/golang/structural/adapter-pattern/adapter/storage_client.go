package adapter

type StorageClient interface {
	Upload(filename string)error
	Download(filename string)error 
}


