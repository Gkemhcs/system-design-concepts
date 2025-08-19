package main

import (
	abstractfactory "abstract-design-pattern/abstract-factory"
	"fmt"
)

func main() {

	fmt.Println("Abstract Factory Pattern Example")
	
	fmt.Println("-------  Using Azure Factory    -----------")
	azureFactory := abstractfactory.NewAzureFactory()

	azureCompute := azureFactory.CreateCompute()
	azureStorage := azureFactory.CreateStorage()
	azureNetwork := azureFactory.CreateNetwork()

	azureStorage.Create("my-storage-account")
	azureNetwork.Configure("my-vnet")
	azureCompute.Start()
	azureCompute.Stop()


	fmt.Println("-------  Using GCP	 Factory    -----------")
	gcpFactory := abstractfactory.NewGCPFactory()
	gcpCompute := gcpFactory.CreateCompute()
	gcpStorage := gcpFactory.CreateStorage()
	gcpNetwork := gcpFactory.CreateNetwork()

	gcpNetwork.Configure("my-gcp-vnet")
	gcpStorage.Create("my-gcp-storage-bucket")
	gcpCompute.Start()
	gcpCompute.Stop()

}
