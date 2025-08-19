package abstractfactory

import "fmt"


func NewGCPCompute()*GCPCompute{
	return &GCPCompute{}
}

type GCPCompute struct{

}


func(c *GCPCompute) Start() error {
	fmt.Println("Starting GCP compute resources")
	return nil
}

func(c *GCPCompute) Stop() error {
	fmt.Println("Stopping GCP compute resources")
	return nil
}

func NewGCPStorage() *GCPStorage {
	return &GCPStorage{}
}

type GCPStorage struct {

}

func(s *GCPStorage) Create(bucketName string) error {
	fmt.Println("Creating GCP storage bucket:", bucketName)
	return nil
}

func NewGCPNetwork() *GCPNetwork {
	return &GCPNetwork{}
}

type GCPNetwork struct {

}

func(s *GCPNetwork) Configure(name string) error {
	fmt.Println("Configuring GCP network:", name)
	return nil
}