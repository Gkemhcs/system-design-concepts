package command

func NewCreateVMCommand(vmService *VMService, vmName string) *CreateVMCommand {
	return &CreateVMCommand{
		vmService: vmService,
		vmName:    vmName,
	}
}

type CreateVMCommand struct {
	vmService *VMService
	vmName    string
}

func (command *CreateVMCommand) Execute() {
	command.vmService.Create(command.vmName)
}


func NewDeleteVMCommand(vmService *VMService, vmName string) *DeleteVMCommand {
	return &DeleteVMCommand{
		vmService: vmService,
		vmName:    vmName,
	}
}

type DeleteVMCommand struct {
	vmService *VMService
	vmName    string
}

func (command *DeleteVMCommand) Execute() {
	command.vmService.Delete(command.vmName)
}


