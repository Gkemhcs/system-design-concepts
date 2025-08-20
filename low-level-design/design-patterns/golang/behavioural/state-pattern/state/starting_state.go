package state

import (
	"errors"
	"fmt"
)

func NewStartingState() *StartingState {
	return &StartingState{}
}

type StartingState struct {
}

func (s *StartingState) Start(vm *VM) error {
	fmt.Printf("%s vm is already starting \n",vm.name)
	return errors.New("vm is already starting")
}

func (s *StartingState) Stop(vm *VM) error {
	fmt.Printf("%s stopping the vm \n",vm.name)
	vm.SetState(NewStoppedState())
	return nil
}

func (s *StartingState) Restart(vm *VM) error {
	fmt.Printf("%s restarting the vm \n",vm.name)
	vm.SetState(NewRestartingState())
	return nil
}

func (s *StartingState) Suspend(vm *VM) error {
	fmt.Printf("%s suspending the vm \n",vm.name)
	vm.SetState(NewSuspendedState())
	return nil
}
func (s *StartingState) GetName() string {
	return "Starting"
}
