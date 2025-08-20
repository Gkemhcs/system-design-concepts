package main

import "command-pattern/command"

func main() {
	vmService := command.NewVMService()
	storageService := command.NewStorageService()
	createVMCommand := command.NewCreateVMCommand(vmService, "vm1")
	deleteVMCommand := command.NewDeleteVMCommand(vmService, "vm1")
	createStorageCommand := command.NewCreateStorageCommand(storageService, "bucket1")
	deleteStorageCommand := command.NewDeleteStorageCommand(storageService, "bucket1")
	invoker := command.NewInvoker()

	invoker.ExecuteCommand(createVMCommand)
	invoker.ExecuteCommand(deleteVMCommand)
	invoker.ExecuteCommand(createStorageCommand)
	invoker.ExecuteCommand(deleteStorageCommand)

}
