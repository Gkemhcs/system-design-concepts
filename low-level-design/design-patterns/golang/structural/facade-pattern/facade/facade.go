package facade

type Facade interface {
	Create() error
	Destroy() error
}

func NewGCPFacade() *GCPFacade {
	return &GCPFacade{
		blockStorageManager: NewGCPBlockStorageManager(),
		networkManager:      NewGCPNetworkManager(),
		vmManager:           NewGCPVMManager(),
	}
}

type GCPFacade struct {
	blockStorageManager GCPBlockStorageManager
	networkManager      GCPNetworkManager
	vmManager           GCPVMManager
}

func (f *GCPFacade) Create() error {
	if err := f.blockStorageManager.Create(); err != nil {
		return err
	}
	if err := f.networkManager.Create(); err != nil {
		return err
	}
	if err := f.vmManager.Create(); err != nil {
		return err
	}
	return nil
}

func (f *GCPFacade) Destroy() error {
	if err := f.blockStorageManager.Delete(); err != nil {
		return err
	}
	if err := f.networkManager.Delete(); err != nil {
		return err
	}
	if err := f.vmManager.Delete(); err != nil {
		return err
	}
	return nil
}

func NewAzureFacade() *AzureFacade {
	return &AzureFacade{
		blockStorageManager: NewAzureBlockStorageManager(),
		networkManager:      NewAzureNetworkManager(),
		vmManager:           NewAzureVMManager(),
	}
}

type AzureFacade struct {
	blockStorageManager AzureBlockStorageManager
	networkManager      AzureNetworkManager
	vmManager           AzureVMManager
}

func (f *AzureFacade) Create() error {
	if err := f.blockStorageManager.Create(); err != nil {
		return err
	}
	if err := f.networkManager.Create(); err != nil {
		return err
	}
	if err := f.vmManager.Create(); err != nil {
		return err
	}
	return nil
}
func (f *AzureFacade) Destroy() error {

	if err := f.blockStorageManager.Delete(); err != nil {
		return err
	}
	if err := f.networkManager.Delete(); err != nil {
		return err
	}
	if err := f.vmManager.Delete(); err != nil {
		return err
	}
	return nil
}
