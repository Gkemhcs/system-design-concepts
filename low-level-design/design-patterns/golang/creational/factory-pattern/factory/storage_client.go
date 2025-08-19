package factory

type StorageClient interface {	

	
	Upload(fileName string, data []byte) error
	Download(filename string) error 

}
