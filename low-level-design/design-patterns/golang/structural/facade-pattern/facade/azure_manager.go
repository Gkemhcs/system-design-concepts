package facade

import "fmt"

func NewAzureBlockStorageManager() AzureBlockStorageManager {
	return AzureBlockStorageManager{}
}

type AzureBlockStorageManager struct {
}

func (m *AzureBlockStorageManager) Create() error {
	// Implementation for creating block storage in Azure
	fmt.Println("Creating block storage in Azure")
	return nil
}

func (m *AzureBlockStorageManager) Delete() error {
	// Implementation for deleting block storage in Azure
	fmt.Println("Deleting block storage in Azure")
	return nil
}

func NewAzureNetworkManager() AzureNetworkManager {
	return AzureNetworkManager{}
}

type AzureNetworkManager struct {
}

func (m *AzureNetworkManager) Create() error {
	// Implementation for creating network in Azure
	fmt.Println("Creating network in Azure")
	return nil
}

func (m *AzureNetworkManager) Delete() error {
	// Implementation for deleting network in Azure
	fmt.Println("Deleting network in Azure")
	return nil
}

func NewAzureVMManager() AzureVMManager {
	return AzureVMManager{}
}

type AzureVMManager struct {
}

func (m *AzureVMManager) Create() error {
	// Implementation for creating VM in Azure
	fmt.Println("Creating VM in Azure")

	return m.Start()
}

func (m *AzureVMManager) Delete() error {
	// Implementation for deleting VM in Azure
	fmt.Println("Deleting VM in Azure")
	return nil
}
func (m *AzureVMManager) Start() error {
	fmt.Println("Starting VM in Azure")
	return nil
}

func (m *AzureVMManager) Stop() error {
	fmt.Println("Stopping VM in Azure")
	return nil
}
