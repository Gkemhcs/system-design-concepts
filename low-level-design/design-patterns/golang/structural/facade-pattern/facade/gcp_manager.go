package facade

import "fmt"

func NewGCPBlockStorageManager() GCPBlockStorageManager {
	return GCPBlockStorageManager{}
}

type GCPBlockStorageManager struct {
}

func (m *GCPBlockStorageManager) Create()error {
	// Implementation for creating a GCP block storage
	fmt.Println("creating GCP block storage")
	return nil 
}
func (m *GCPBlockStorageManager) Delete()error{
	// Implementation for deleting a GCP block storage
	fmt.Println("deleting GCP block storage")
	return nil 
}

func NewGCPNetworkManager() GCPNetworkManager {
	return GCPNetworkManager{}
}

type GCPNetworkManager struct {
}

func (m *GCPNetworkManager) Create() error {
	// Implementation for creating a GCP network
	fmt.Println("creating GCP network")
	return nil
}
func (m *GCPNetworkManager) Delete() error {
	// Implementation for deleting a GCP network
	fmt.Println("deleting GCP network")
	return nil
}

func NewGCPVMManager() GCPVMManager {
	return GCPVMManager{}
}

type GCPVMManager struct {
}

func (m *GCPVMManager) Create() error {
	// Implementation for creating a GCP VM
	fmt.Println("creating GCP VM")
	return m.Start()
}

func (m *GCPVMManager) Delete() error {
	// Implementation for deleting a GCP VM
	fmt.Println("deleting GCP VM")
	return nil
}
func (m *GCPVMManager) Start() error {

	fmt.Println("starting GCP VM")
	return nil
}

func (m *GCPVMManager) Stop() error {
	// Implementation for stopping a GCP VM
	fmt.Println("stopping GCP VM")
	return nil
}
