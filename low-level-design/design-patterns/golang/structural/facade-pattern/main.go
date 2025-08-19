package main

import (
	"facade-pattern/facade"
	"fmt"

	
)


func main(){

	fmt.Println("Facade Pattern")

	fmt.Println("Creating GCP resources using Facade")
	gcpFacade := facade.NewGCPFacade()
	if err := gcpFacade.Create(); err != nil {
		panic(fmt.Errorf("error creating GCP resources: %v", err))
	}
	fmt.Println("GCP resources created successfully")

	fmt.Println("Creating Azure resources using Facade")
	azureFacade := facade.NewAzureFacade()
	if err := azureFacade.Create(); err != nil {
		panic(fmt.Errorf("error creating Azure resources: %v", err))
	}
	fmt.Println("Azure resources created successfully")

	fmt.Println("Destroying GCP resources using Facade")
	if err := gcpFacade.Destroy(); err != nil {
		panic(fmt.Errorf("error destroying GCP resources: %v", err))
	}
	fmt.Println("GCP resources destroyed successfully")

	fmt.Println("Destroying Azure resources using Facade")
	if err := azureFacade.Destroy(); err != nil {
		panic(fmt.Errorf("error destroying Azure resources: %v", err))
	}
}