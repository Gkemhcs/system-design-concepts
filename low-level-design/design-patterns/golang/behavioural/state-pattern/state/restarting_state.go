package state

import (
	"errors"
	"fmt"
)

func NewRestartingState() *RestartingState {
	return &RestartingState{}
}

type RestartingState struct {
}

func (s *RestartingState) Start(vm *VM) error {
	fmt.Printf("%s vm is already restarting \n",vm.name)
	return errors.New("vm is already restarting")
}

func (s *RestartingState) Stop(vm *VM) error {
	fmt.Printf("%s stopping the vm \n",vm.name)
	vm.SetState(NewStoppedState())
	return nil
}
func (s *RestartingState) Restart(vm *VM) error {
	fmt.Printf("%s vm is already restarting \n",vm.name)
	return errors.New("vm is already restarting")
}
func (s *RestartingState) Suspend(vm *VM) error {
	fmt.Printf("%s suspending the vm \n",vm.name)
	vm.SetState(NewSuspendedState())
	return nil
}
func (s *RestartingState) GetName() string {
	return "Restarting"
}
