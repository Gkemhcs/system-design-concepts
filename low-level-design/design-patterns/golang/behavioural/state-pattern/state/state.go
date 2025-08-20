package state

func NewVM(vmName string,state VMState) *VM {
	return &VM{
		name :vmName,
		currentState: state,
	}
}

func (vm *VM) Start() error {
	return vm.currentState.Start(vm)
}

func (vm *VM) Stop() error {
	return vm.currentState.Stop(vm)
}
func (vm *VM) Restart() error {
	return vm.currentState.Restart(vm)
}

func (vm *VM) Suspend() error {
	return vm.currentState.Suspend(vm)
}

func (vm *VM) SetState(state VMState) {
	vm.currentState = state
}

type VM struct {
	name string 
	currentState VMState
}

type VMState interface {
	Start(vm *VM) error
	Stop(vm *VM) error
	Restart(vm *VM) error
	Suspend(vm *VM) error
	GetName() string
}
