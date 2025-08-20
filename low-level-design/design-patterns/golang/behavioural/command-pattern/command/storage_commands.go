package command

func NewCreateStorageCommand(storageService *StorageService, vmName string)*CreateStorageCommand{
	return &CreateStorageCommand{
		storageService: storageService,
		bucketName:     vmName,
	}
}

type CreateStorageCommand struct {
	storageService *StorageService
	bucketName     string
}

func(command *CreateStorageCommand) Execute() {
	command.storageService.Create(command.bucketName)
}



func NewDeleteStorageCommand(storageService *StorageService, vmName string)*DeleteStorageCommand{
	return &DeleteStorageCommand{
		storageService: storageService,
		bucketName:     vmName,
	}
}

type DeleteStorageCommand struct {
	storageService *StorageService
	bucketName     string
}

func(command *DeleteStorageCommand) Execute() {
	command.storageService.Delete(command.bucketName)
}

