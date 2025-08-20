package state

import (
	"errors"
	"fmt"
)

func NewSuspendedState() *SuspendedState {
	return &SuspendedState{}
}

type SuspendedState struct {
}

func (s *SuspendedState) Start(vm *VM) error {
	fmt.Printf(" starting the vm  %s \n", vm.name)
	vm.SetState(NewStartingState())
	return nil
}
func (s *SuspendedState) Stop(vm *VM) error {
	fmt.Printf(" stopping the vm  %s \n", vm.name)
	vm.SetState(NewStoppedState())
	return nil
}

func (s *SuspendedState) Restart(vm *VM) error {
	fmt.Printf(" restarting the vm  %s \n", vm.name)
	vm.SetState(NewRestartingState())
	return nil
}
func (s *SuspendedState) Suspend(vm *VM) error {
	fmt.Printf("%s vm is already suspended \n", vm.name)
	return errors.New("vm is already suspended")

}

func (s *SuspendedState) GetName() string {
	return "Suspended"
}
